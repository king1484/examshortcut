"""Tiny open-weights LLM client with a fallback chain (OpenRouter -> Nous -> NVIDIA).

Keys come from env vars (OPENROUTER_API_KEY, NOUS_API_KEY, NVIDIA_API_KEY) or, if unset,
are read from Desktop\\llms.txt (override with LLMS_TXT). Nothing is ever printed.
"""
import json, os, re, time
import requests

UA = {"User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/124.0 Safari/537.36"}
LLMS_TXT = os.environ.get("LLMS_TXT", os.path.join(os.path.expanduser("~"), "Desktop", "llms.txt"))
KEY_RE = {"OPENROUTER_API_KEY": r"sk-or-v1-[A-Za-z0-9]+", "NOUS_API_KEY": r"sk-nous-[A-Za-z0-9_\-]+", "NVIDIA_API_KEY": r"nvapi-[A-Za-z0-9_\-]+"}


def _key(name):
    if os.environ.get(name):
        return os.environ[name]
    try:
        m = re.search(KEY_RE[name], open(LLMS_TXT, encoding="utf8", errors="ignore").read())
        return m.group(0) if m else None
    except OSError:
        return None


PROVIDERS = [
    {"name": "openrouter", "url": "https://openrouter.ai/api/v1/chat/completions", "key": "OPENROUTER_API_KEY",
     "model": "nvidia/nemotron-3-super-120b-a12b:free", "extra": {"reasoning": {"exclude": True}}, "timeout": 300},
    {"name": "nous", "url": "https://inference-api.nousresearch.com/v1/chat/completions", "key": "NOUS_API_KEY",
     "model": "stepfun/step-3.7-flash:free", "extra": {"tags": ["user=examshortcut"]}, "timeout": 300},
    {"name": "nvidia", "url": "https://integrate.api.nvidia.com/v1/chat/completions", "key": "NVIDIA_API_KEY",
     "model": "nvidia/nemotron-3-ultra-550b-a55b", "extra": {}, "timeout": 290, "stream": True},
]


def _ok(r):
    if r.status_code >= 400:
        raise RuntimeError(f"HTTP {r.status_code}: " + r.text[:120].replace("\n", " "))


def _call(p, messages, max_tokens):
    key = _key(p["key"])
    if not key:
        raise RuntimeError("no key")
    body = {"model": p["model"], "messages": messages, "max_tokens": max_tokens, "temperature": 0.2, **p["extra"]}
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
        return "".join(out)
    r = requests.post(p["url"], json=body, headers=h, timeout=p["timeout"])
    _ok(r)
    ch = r.json().get("choices")
    if not ch:
        raise RuntimeError("no choices: " + r.text[:120].replace("\n", " "))
    m = ch[0]
    if m.get("finish_reason") == "length":
        raise RuntimeError("truncated")
    return m["message"].get("content") or m["message"].get("reasoning_content") or ""


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
                if "429" in last or "402" in last or "no key" in last:
                    break
                time.sleep(3)
    raise RuntimeError("all LLM providers failed: " + str(last))
