"""Open-weights LLM client with the same fallback chain as the LinkedIn AutoApply bot
(data/run_overrides.json LLM_FALLBACK_CHAIN + LLM_MODEL_OVERRIDES): every leg is an OpenAI-compatible
free endpoint, each leg its own quota bucket.

Keys come from env vars (GitHub secrets in CI). Locally, if unset, they are read from the bot's .env
(LINKEDIN_ENV) or Desktop\\llms.txt. Nothing is ever printed.
"""
import json, os, re, time
import requests

UA = {"User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/124.0 Safari/537.36"}
_HOME = os.path.expanduser("~")
LLMS_TXT = os.environ.get("LLMS_TXT", os.path.join(_HOME, "Desktop", "llms.txt"))
BOT_ENV = os.environ.get("LINKEDIN_ENV", os.path.join(_HOME, "Desktop", "LinkedInAutoApply", ".env"))
KEY_RE = {"OPENROUTER_API_KEY": r"sk-or-v1-[A-Za-z0-9]+", "NOUS_API_KEY": r"sk-nous-[A-Za-z0-9_\-]+", "NVIDIA_API_KEY": r"nvapi-[A-Za-z0-9_\-]+"}
CF_AI_ACCOUNT = os.environ.get("CF_AI_ACCOUNT_ID", "5d5fea1d5c65dfb79efc58929329da6a")

NOUS = "https://inference-api.nousresearch.com/v1/chat/completions"
KILO = "https://api.kilo.ai/api/gateway/v1/chat/completions"

# The bot's live LLM_FALLBACK_CHAIN, minus legs verified dead on 2026-10-06 (nous2 solar-pro4 and nous3 longcat-2.0 are no longer
# free -> 404; kilo2 ling-3.0-flash-fin model is gone), reordered so the legs that answered the probe come first.
PROVIDERS = [
    {"name": "ollamacloud", "url": "https://ollama.com/v1/chat/completions", "key": "OLLAMA_CLOUD_API_KEY", "model": "gpt-oss:120b", "extra": {}},
    {"name": "nous", "url": NOUS, "key": "NOUS_API_KEY", "model": "poolside/laguna-s-2.1:free", "extra": {"tags": ["user=examshortcut"]}},
    {"name": "agnes", "url": "https://apihub.agnes-ai.com/v1/chat/completions", "key": "AGNES_API_KEY", "model": "agnes-3.0-flash", "extra": {}},
    {"name": "kilo", "url": KILO, "key": "KILO_API_KEY", "model": "poolside/laguna-s-2.1:free", "extra": {}},
    {"name": "mistral", "url": "https://api.mistral.ai/v1/chat/completions", "key": "MISTRAL_API_KEY", "model": "mistral-small-latest", "extra": {}},
    {"name": "openrouter", "url": "https://openrouter.ai/api/v1/chat/completions", "key": "OPENROUTER_API_KEY",
     "model": "nvidia/nemotron-3-super-120b-a12b:free", "extra": {"reasoning": {"exclude": True}}},
    {"name": "cloudflare", "url": f"https://api.cloudflare.com/client/v4/accounts/{CF_AI_ACCOUNT}/ai/v1/chat/completions",
     "key": "CLOUDFLARE_API_KEY", "model": "@cf/qwen/qwen3.8-27b", "extra": {}},
    {"name": "nvidia", "url": "https://integrate.api.nvidia.com/v1/chat/completions", "key": "NVIDIA_API_KEY",
     "model": "nvidia/nemotron-3-ultra-550b-a55b", "extra": {}, "stream": True},
]

_THINK_RE = re.compile(r"<think>.*?</think>", re.DOTALL | re.IGNORECASE)
_dotenv = None


def _key(name):
    global _dotenv
    if os.environ.get(name):
        return os.environ[name].strip()
    if _dotenv is None:
        _dotenv = {}
        try:
            for line in open(BOT_ENV, encoding="utf8", errors="ignore"):
                m = re.match(r"\s*([A-Z0-9_]+)\s*=\s*(.*?)\s*$", line)
                if m:
                    _dotenv[m.group(1)] = m.group(2).strip("'\"")
        except OSError:
            pass
    if _dotenv.get(name):
        return _dotenv[name]
    if name in KEY_RE:
        try:
            m = re.search(KEY_RE[name], open(LLMS_TXT, encoding="utf8", errors="ignore").read())
            return m.group(0) if m else None
        except OSError:
            return None
    return None


def _ok(r):
    if r.status_code >= 400:
        raise RuntimeError(f"HTTP {r.status_code}: " + r.text[:120].replace("\n", " "))


def _call(p, messages, max_tokens):
    key = _key(p["key"])
    if not key:
        raise RuntimeError("no key")
    body = {"model": p["model"], "messages": messages, "max_tokens": max(max_tokens, 1024), "temperature": 0.2, **p["extra"]}
    h = {**UA, "Authorization": "Bearer " + key, "Content-Type": "application/json"}
    if p.get("stream"):
        body["stream"] = True
        out = []
        with requests.post(p["url"], json=body, headers=h, timeout=(20, 90), stream=True) as r:
            _ok(r)
            for line in r.iter_lines():
                if line and line.startswith(b"data: ") and line != b"data: [DONE]":
                    ch = json.loads(line[6:]).get("choices") or []
                    if ch:
                        out.append((ch[0].get("delta") or {}).get("content") or "")
        return _THINK_RE.sub("", "".join(out))
    r = requests.post(p["url"], json=body, headers=h, timeout=p.get("timeout", 240))
    _ok(r)
    ch = r.json().get("choices")
    if not ch:
        raise RuntimeError("no choices: " + r.text[:120].replace("\n", " "))
    m = ch[0]
    if m.get("finish_reason") == "length":
        raise RuntimeError("truncated")
    msg = m["message"]
    return _THINK_RE.sub("", msg.get("content") or msg.get("reasoning_content") or msg.get("reasoning") or "")


def extract_json(text):
    """First parseable JSON object in text (ignores fences and prose around it)."""
    dec = json.JSONDecoder()
    for m in re.finditer(r"\{", text):
        try:
            obj, _ = dec.raw_decode(text[m.start():])
            if isinstance(obj, dict):
                return obj
        except ValueError:
            continue
    raise ValueError("no JSON object in reply")


def ask_json(system, user, max_tokens=6000, log=print):
    messages = [{"role": "system", "content": system}, {"role": "user", "content": user}]
    last = None
    for p in PROVIDERS:
        for attempt in (1, 2):
            try:
                t0 = time.time()
                obj = extract_json(_call(p, messages, max_tokens))
                log(f"  llm {p['name']} ok {time.time()-t0:.0f}s")
                return obj
            except Exception as e:  # noqa
                last = f"{p['name']}: {str(e)[:100]}"
                log(f"  llm {last}")
                # quota / auth / missing key / timeout: the next attempt on the same leg can't help
                if any(k in last for k in ("429", "402", "401", "403", "no key", "Timeout", "timed out")):
                    break
                time.sleep(3)
    raise RuntimeError("all LLM providers failed: " + str(last))
