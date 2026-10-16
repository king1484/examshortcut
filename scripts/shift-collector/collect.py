"""Stage 1 of the shift-analysis pipeline: collect sources for one exam day.

    py -3.12 scripts/shift-collector/collect.py --date 2026-10-06 [--shift 1]

Finds the newest YouTube shift-review videos (date-sorted search), pulls their
transcripts, scrapes a few web articles, and writes
scripts/shift-collector/packs/<date>/pack.json for the synthesis stage.
No API keys needed. Needs: yt-dlp, youtube-transcript-api, requests, bs4.
"""
import argparse, datetime as dt, json, os, random, re, sys, time
from concurrent.futures import ThreadPoolExecutor
from urllib.parse import quote_plus

import requests
from bs4 import BeautifulSoup
import yt_dlp
from youtube_transcript_api import YouTubeTranscriptApi
from youtube_transcript_api.proxies import GenericProxyConfig
from youtube_transcript_api._errors import IpBlocked, NoTranscriptFound, RequestBlocked, TranscriptsDisabled
from quality import balanced_videos

HERE = os.path.dirname(os.path.abspath(__file__))
CACHE = os.path.join(HERE, "cache")
UA = {"User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 Chrome/126 Safari/537.36"}
MONTHS = ["january", "february", "march", "april", "may", "june", "july", "august", "september", "october", "november", "december"]
ORD = {1: ["1st", "first", "shift 1", "shift-1", "s1", "1 shift"], 2: ["2nd", "second", "shift 2", "shift-2", "s2", "2 shift"], 3: ["3rd", "third", "shift 3", "shift-3", "s3", "3 shift"]}
SHIFT_END_IST = {1: (11, 0), 2: (14, 30), 3: (18, 0)}
MAX_TRANSCRIPT_CHARS = 14000


def date_re(d: dt.date):
    m = MONTHS[d.month - 1]
    ms = f"(?:{m}|{m[:3]})"
    day = f"0?{d.day}"
    suf = "(?:st|nd|rd|th)?"
    a = rf"(?<![\d\-&,/]){day}{suf}\s*{ms}\b"                      # 6 october / 6th oct
    b = rf"\b{ms}\s*{day}(?!\d)(?!{suf}\s*(?:shift|sh\b)){suf}(?![\-&]|,\s*\d{{1,2}}\b(?!\d{{2}}))"   # october 6 / oct 6th (not "oct 2nd shift")
    c = rf"(?<!\d){d.day:02d}[/\-.]{d.month:02d}(?!\d)"
    return re.compile(f"{a}|{b}|{c}", re.I)


class SearchLogger:
    # yt-dlp errors can contain proxy credentials; report only route availability below.
    def debug(self, message):
        pass

    def warning(self, message):
        pass

    def error(self, message):
        pass


def yt_search(query: str, n: int = 25, use_proxy: bool = True):
    url = f"https://www.youtube.com/results?search_query={quote_plus(query)}&sp=CAI%253D"  # sorted by upload date
    opts = {"quiet": True, "extract_flat": True, "playlistend": n, "skip_download": True,
            "socket_timeout": 15, "retries": 1, "extractor_retries": 1, "logger": SearchLogger(),
            **({"proxy": PROXY} if use_proxy and PROXY else {})}
    with yt_dlp.YoutubeDL(opts) as y:
        info = y.extract_info(url, download=False)
    return [{"id": e["id"], "title": e.get("title") or "", "channel": e.get("channel") or e.get("uploader") or ""}
            for e in (info.get("entries") or []) if e.get("id")]


def yt_meta(vid: str):
    with yt_dlp.YoutubeDL({"quiet": True, "skip_download": True}) as y:
        i = y.extract_info(f"https://www.youtube.com/watch?v={vid}", download=False)
    return {"upload_date": i.get("upload_date"), "timestamp": i.get("timestamp"), "duration": i.get("duration"),
            "views": i.get("view_count"), "is_live": i.get("is_live"), "channel": i.get("channel")}


def _proxy_url():
    """Optional proxy for transcript fetches (YouTube rate-limits home/cloud IPs). Env YT_PROXY or proxy.txt, host:port:user:pass."""
    raw = os.environ.get("YT_PROXY", "")
    f = os.path.join(HERE, "proxy.txt")
    if not raw and os.path.exists(f):
        raw = open(f, encoding="utf8").read().strip()
    if not raw:
        return None
    if "://" in raw:
        return raw
    h, p, u, pw = raw.split(":", 3)
    return f"http://{u}:{pw}@{h}:{p}"


PROXY = _proxy_url()
PROXIES = {"http": PROXY, "https": PROXY} if PROXY else None


class Blocked(Exception):
    pass


def ytdlp_captions(vid: str):
    """Second route: yt-dlp's ios / web_embedded player clients still return caption tracks when the
    default client is bot-checked. Format errors are ignored (we only want the subtitle URLs)."""
    last = "no captions"
    for client in ("ios", "web_embedded"):
        opts = {"quiet": True, "no_warnings": True, "skip_download": True, "ignore_no_formats_error": True,
                "extractor_args": {"youtube": {"player_client": [client]}}, **({"proxy": PROXY} if PROXY else {})}
        try:
            with yt_dlp.YoutubeDL(opts) as y:
                i = y.extract_info(f"https://www.youtube.com/watch?v={vid}", download=False)
        except Exception as e:  # noqa
            last = "bot check" if "not a bot" in str(e) else str(e)[:80]
            continue
        pools = [i.get("subtitles") or {}, i.get("automatic_captions") or {}]
        for lang in ("en", "en-orig", "en-IN", "hi", "hi-orig"):
            for pool in pools:
                for f in pool.get(lang, []):
                    if f.get("ext") != "json3":
                        continue
                    r = requests.get(f["url"], headers=UA, timeout=25, proxies=PROXIES)
                    if r.status_code == 429:
                        raise Blocked("timedtext 429")
                    if r.status_code != 200:
                        continue
                    j = r.json()
                    text = " ".join("".join(sg.get("utf8", "") for sg in ev.get("segs", [])) for ev in j.get("events", []))
                    text = re.sub(r"\s+", " ", text).strip()
                    if text:
                        return {"lang": lang, "text": text}
        last = "no captions"
    raise RuntimeError(last)


INVIDIOUS = ["https://inv.nadeko.net", "https://yewtu.be"]


def invidious_captions(vid: str):
    for base in INVIDIOUS:
        try:
            r = requests.get(f"{base}/api/v1/captions/{vid}", headers=UA, timeout=20)
            tracks = r.json().get("captions") or []
            if not tracks:
                continue
            pick = next((t for t in tracks if t["languageCode"].startswith("en")), None) or next((t for t in tracks if t["languageCode"].startswith("hi")), tracks[0])
            v = requests.get(base + pick["url"], headers=UA, timeout=30).text
            lines = [l.strip() for l in v.splitlines() if l.strip() and "-->" not in l and not l.startswith(("WEBVTT", "Kind:", "Language:", "NOTE"))]
            text = re.sub(r"<[^>]+>", "", " ".join(lines))
            text = re.sub(r"\s+", " ", text)
            # auto-captions repeat each line twice; collapse immediate repeats
            out, prev = [], None
            for w in re.split(r"(?<=[.!?।])\s+|\s{2,}", text):
                if w != prev:
                    out.append(w)
                prev = w
            if len(text) > 200:
                return {"lang": pick["languageCode"], "text": " ".join(out)}
        except Exception:  # noqa
            continue
    return None


def yt_transcript(vid: str):
    api = YouTubeTranscriptApi(proxy_config=GenericProxyConfig(http_url=PROXY, https_url=PROXY)) if PROXY else YouTubeTranscriptApi()
    for langs in (["en", "en-IN", "hi"], None):
        try:
            if langs:
                t = api.fetch(vid, languages=langs)
            else:
                t = next(iter(api.list(vid))).fetch()
            text = " ".join(s.text.replace("\n", " ") for s in t)
            return {"lang": getattr(t, "language_code", ""), "text": text}
        except (IpBlocked, RequestBlocked):
            try:
                return ytdlp_captions(vid)
            except Blocked:
                return {"lang": "", "text": "", "error": "ip blocked", "blocked": True}
            except Exception as e:  # noqa
                err = str(e)[:120]
                if err == "bot check":
                    return {"lang": "", "text": "", "error": "ip blocked", "blocked": True}
                return {"lang": "", "text": "", "error": err}
        except (TranscriptsDisabled, NoTranscriptFound):
            err = "no captions"
        except Exception as e:  # noqa
            err = str(e)[:120]
    return {"lang": "", "text": "", "error": err}


def api_transcript(vid: str):
    """Fallback when YouTube blocks this IP: a free anonymous third-party API (freetranscriptapi.com,
    ~20 requests/hour/IP, no key) that fetches the captions from its own IPs."""
    try:
        r = requests.get("https://api.freetranscriptapi.com/v1/transcript", params={"video_url": vid}, headers=UA, timeout=45)
    except Exception as e:  # noqa
        return {"lang": "", "text": "", "error": "api: " + str(e)[:80]}
    if r.status_code == 429:
        return {"lang": "", "text": "", "error": "api rate limited", "blocked": True}
    if r.status_code != 200:
        return {"lang": "", "text": "", "error": f"api HTTP {r.status_code}"}
    j = r.json()
    segs = j.get("transcript") or []
    text = " ".join((x.get("text") if isinstance(x, dict) else str(x)).replace("\n", " ") for x in segs)
    return {"lang": j.get("language", ""), "text": text} if text.strip() else {"lang": "", "text": "", "error": "api: empty"}


def transcript(vid: str, use_yt: bool = True, use_api: bool = True):
    """YouTube direct (proxy, yt-dlp) first, then the free API. Flags report which route is blocked."""
    t = {"lang": "", "text": "", "error": "skipped"}
    if use_yt:
        t = yt_transcript(vid)
        if t.get("text"):
            return t
        # A blocked/proxied request can surface as "no captions", so never trust that: try the API too.
        print(f"  yt transcript {vid}: {t.get('error', '?')[:110]}", file=sys.stderr)
        t["yt_blocked"] = True            # blocked or any other failure: try the free API fallback
    if use_api:
        a = api_transcript(vid)
        if not a.get("text"):
            print(f"  api transcript {vid}: {a.get('error', '?')[:110]}", file=sys.stderr)
        a["yt_blocked"] = bool(use_yt)
        if a.get("text") or a.get("blocked"):
            return a
        return {**a, "yt_blocked": bool(use_yt)}
    return {**t, "blocked": True}


def title_matches(title: str, d: dt.date, shift: int | None):
    t = title.lower()
    if "cgl" not in t or any(w in t for w in ("technician", "expected", "most repeated", "previous year", "pyq")):
        return False
    if not date_re(d).search(t):
        return False
    if shift:
        others = [s for s in (1, 2, 3) if s != shift]
        has_me = any(k in t for k in ORD[shift])
        has_other = any(k in t for s in others for k in ORD[s])
        multi = "1st" in t and "2nd" in t
        return has_me or multi or not has_other
    return True


def find_videos(d: dt.date, shift: int | None):
    day = f"{d.day} {MONTHS[d.month - 1].capitalize()}"
    shifts = [shift] if shift else [1, 2, 3]
    queries = []
    for s in shifts:
        o = {1: "1st", 2: "2nd", 3: "3rd"}[s]
        queries += [f"SSC CGL {day} 2026 {o} shift review analysis", f"SSC CGL exam review today {day} shift {s}",
                    f"SSC CGL {MONTHS[d.month-1].capitalize()} {d.day} 2026 {o} shift"]
    queries += [f"SSC CGL {day} 2026 all shift analysis"]
    # Probe one query before starting the pool. A dead proxy must not abort collection
    # or be retried by every search worker. Direct search and article collection still run.
    use_proxy = bool(PROXY)
    try:
        first = yt_search(queries[0], use_proxy=use_proxy)
    except yt_dlp.utils.DownloadError:
        if not use_proxy:
            print("YouTube search unavailable; continuing with article sources", file=sys.stderr)
            return []
        print("YouTube proxy unavailable; retrying search directly", file=sys.stderr)
        use_proxy = False
        try:
            first = yt_search(queries[0], use_proxy=False)
        except yt_dlp.utils.DownloadError:
            print("Direct YouTube search unavailable; continuing with article sources", file=sys.stderr)
            return []

    failed = []
    def search_remaining(query):
        try:
            return yt_search(query, use_proxy=use_proxy)
        except yt_dlp.utils.DownloadError:
            failed.append(query)
            return []

    seen, cands = set(), []
    with ThreadPoolExecutor(6) as ex:
        for res in [first, *ex.map(search_remaining, queries[1:])]:
            for r in res:
                if r["id"] not in seen:
                    seen.add(r["id"]); cands.append(r)
    if failed:
        print(f"YouTube: {len(failed)} searches unavailable; retaining other results", file=sys.stderr)
    keep = [c for c in cands if title_matches(c["title"], d, shift)]
    print(f"videos: {len(cands)} found, {len(keep)} title-match", file=sys.stderr)
    return keep


def web_articles(d: dt.date, shift: int | None, limit: int = 8):
    day = f"{d.day} {MONTHS[d.month - 1]}"
    q = f"SSC CGL 2026 tier 1 exam analysis {day} shift review good attempts"
    try:
        # The optional YouTube proxy is unrelated to web search and may be offline.
        r = requests.post("https://html.duckduckgo.com/html/", data={"q": q, "df": "w"}, headers=UA, timeout=25)
        r.raise_for_status()
        soup = BeautifulSoup(r.text, "html.parser")
        links = []
        for a in soup.select("a.result__a"):
            href = a.get("href", "")
            m = re.search(r"uddg=([^&]+)", href)
            if m:
                from urllib.parse import unquote
                href = unquote(m.group(1))
            if href.startswith("http") and "youtube.com" not in href:
                links.append((a.get_text(" ", strip=True), href))
    except requests.RequestException as e:
        print(f"Article search unavailable ({type(e).__name__}); retaining existing analysis", file=sys.stderr)
        links = []
    arts, seen = [], set()
    for title, href in links:
        if href in seen or len(arts) >= limit:
            continue
        seen.add(href)
        try:
            h = requests.get(href, headers=UA, timeout=25)
            h.raise_for_status()
            s = BeautifulSoup(h.text, "html.parser")
            for tag in s(["script", "style", "nav", "footer", "header", "aside", "form"]):
                tag.decompose()
            text = re.sub(r"\s+", " ", s.get_text(" ", strip=True))
            low = text.lower()
            if date_re(d).search(low) and "cgl" in low:
                arts.append({"title": title, "url": href, "text": text[:9000]})
        except Exception as e:  # noqa
            print("fetch failed", href, str(e)[:60], file=sys.stderr)
    return arts


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("--date", required=True)
    ap.add_argument("--shift", type=int, choices=(1, 2, 3))
    ap.add_argument("--max-videos", type=int, default=12)
    a = ap.parse_args()
    d = dt.date.fromisoformat(a.date)
    vids = find_videos(d, a.shift)
    vids = [v for v in vids if not (v.get("duration") and v["duration"] < 120)]   # drop shorts
    # Search results arrive grouped by query. Taking the first ten starved later shifts.
    # Round-robin across labelled shifts before filling spare slots with general reviews.
    vids = balanced_videos(vids, a.max_videos, ORD)
    os.makedirs(CACHE, exist_ok=True)
    yt_ok, api_ok = True, True         # False once that route is blocked: stop hammering it for this run
    for v in vids:  # one at a time, cached
        cf = os.path.join(CACHE, v["id"] + ".json")
        t = None
        if os.path.exists(cf):
            t = json.load(open(cf, encoding="utf8"))
            if not t.get("text") and (time.time() - os.path.getmtime(cf)) > 1800:
                t = None                      # empty result older than 30 min: captions may exist now
        if t is None and (yt_ok or api_ok):
            t = transcript(v["id"], use_yt=yt_ok, use_api=api_ok)
            if t.pop("yt_blocked", False):
                yt_ok = False
            if t.get("blocked"):
                api_ok = False
            if t.get("text"):                 # cache only real transcripts; "no captions" can be a disguised block
                json.dump(t, open(cf, "w", encoding="utf8"), ensure_ascii=False)
            time.sleep(random.uniform(1.0, 2.5))
        t = t or {"text": "", "error": "skipped: transcript routes blocked earlier in this run"}
        v["transcript"] = t["text"][:MAX_TRANSCRIPT_CHARS]
        v["transcript_lang"] = t.get("lang")
        if t.get("error"):
            v["transcript_error"] = t["error"]
    if not yt_ok:
        print("NOTE: YouTube blocked this IP; used the free transcript API fallback" if api_ok else "WARNING: YouTube and the fallback API are both blocked; try again later", file=sys.stderr)
    arts = web_articles(d, a.shift)
    pack = {"date": a.date, "shift": a.shift, "collected_at": dt.datetime.now(dt.timezone(dt.timedelta(hours=5, minutes=30))).isoformat(timespec="minutes"),
            "videos": vids, "articles": arts}
    out = os.path.join(HERE, "packs", a.date + (f"-s{a.shift}" if a.shift else ""))
    os.makedirs(out, exist_ok=True)
    with open(os.path.join(out, "pack.json"), "w", encoding="utf8") as f:
        json.dump(pack, f, ensure_ascii=False, indent=1)
    ok = sum(1 for v in vids if v.get("transcript"))
    print(f"{a.date} shift={a.shift}: {len(vids)} videos ({ok} with transcript), {len(arts)} articles -> {out}")


if __name__ == "__main__":
    main()
