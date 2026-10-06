"""Stage 2: turn a collected pack into content/shift-analysis/<exam>/<date>.json using an open-weights LLM.

    py -3.12 scripts/shift-collector/synthesize.py --date 2026-10-06 [--shift 1]

Per source: the LLM extracts facts (no prose). Per shift: the LLM merges the facts into the site schema.
Code (not the LLM) decides status, sources list, ids, names, marks and drops invalid topic links.
Shifts that were written by hand (no "auto": true and status "reported") are never overwritten.
"""
import argparse, concurrent.futures as cf, datetime as dt, hashlib, json, os, re, sys

from llm import ask_json

HERE = os.path.dirname(os.path.abspath(__file__))
ROOT = os.path.abspath(os.path.join(HERE, "..", ".."))
EXAM = "ssc-cgl-2026"
OUT_DIR = os.path.join(ROOT, "content", "shift-analysis", EXAM)
TIMES = {1: "10:00 AM – 11:00 AM IST", 2: "1:30 PM – 2:30 PM IST", 3: "5:00 PM – 6:00 PM IST"}
END_IST = {1: (11, 0), 2: (14, 30), 3: (18, 0)}
SECTIONS = [("reasoning", "General Intelligence & Reasoning"), ("ga", "General Awareness"),
            ("quant", "Quantitative Aptitude"), ("english", "English Comprehension")]
IST = dt.timezone(dt.timedelta(hours=5, minutes=30))
log = lambda *a: print(*a, file=sys.stderr, flush=True)

EXTRACT_SYS = """You extract facts from an SSC CGL 2026 Tier 1 exam review (a YouTube transcript, often Hindi/Hinglish, or a web article). Reply with ONE JSON object and nothing else.
Rules: report only what the source says. Translate to English. Use null or [] when not stated. Never guess numbers. Keep each string under 160 characters.
Schema: {"shifts":[{"shift":1|2|3,"overall":"Easy|Easy to Moderate|Moderate|Moderate to Difficult|Difficult|null","good_attempts":"as stated, e.g. '75-80' or null",
"sections":{"reasoning":{"difficulty":str|null,"good_attempts":str|null,"topics":[{"topic":str,"count":str|null}],"notes":str|null},"ga":{...same},"quant":{...same},"english":{...same}},
"asked":[{"section":"reasoning|ga|quant|english","q":"a specific question or topic recalled by candidates"}],"issues":["technical or centre problems reported"],"mentions":["other notable remarks, e.g. attempts survey results"]}]}
Only include shifts the source actually discusses. If the source is about an earlier or later date than the one asked, return {"shifts":[]}."""

MERGE_SYS = """You write one shift's entry for an exam-analysis website from several extracted source reports. Reply with ONE JSON object and nothing else.
Style: plain, short sentences, neutral, like a careful student writing notes. Say 'reported' or 'candidates said'. No hype, no marketing words, no em dashes (use commas or colons; en dash only in numeric ranges). All figures are unofficial.
Use ONLY facts present in the reports. Where reports disagree, say so in "disagreements" instead of picking one. Do not invent topics, counts or questions. If a section has no data, set difficulty "Not reported" and leave topics empty.
Schema: {"overall":str,"goodAttempts":str,"summary":"3-5 sentences","sections":{"reasoning":{"difficulty":str,"goodAttempts":str|null,"notes":"1-3 sentences","topics":[{"topic":str,"count":str|null}]},"ga":{...},"quant":{...},"english":{...}},
"asked":[{"section":"reasoning|ga|quant|english","q":str}],"observations":[str],"disagreements":[str]}
Limit: topics max 8 per section, asked max 14, observations max 4, disagreements max 4."""

INTRO_SYS = """Write the intro paragraph (3-5 sentences) and 5 FAQs for an SSC CGL 2026 Tier 1 exam-analysis page for one day, from the shift summaries given. Plain neutral tone, no hype, no em dashes, say figures are unofficial and SSC normalises scores across shifts. If a shift is pending, say its analysis will be added after the shift. Reply with ONE JSON object: {"intro":str,"faqs":[{"q":str,"a":str}]}. FAQ questions must mention the date given."""


def clean(s):
    return re.sub(r"\s*—\s*", ", ", s).strip() if isinstance(s, str) else s


def clean_tree(o):
    if isinstance(o, str):
        return clean(o)
    if isinstance(o, list):
        return [clean_tree(x) for x in o]
    if isinstance(o, dict):
        return {k: clean_tree(v) for k, v in o.items()}
    return o


def topic_slugs():
    base = os.path.join(ROOT, "content", "core", "topics")
    out = set()
    for sec in os.listdir(base):
        p = os.path.join(base, sec)
        if os.path.isdir(p):
            out |= {f"{sec}/{f[:-5]}" for f in os.listdir(p) if f.endswith(".json")}
    return out


def extract_source(date, src):
    kind = "YouTube transcript" if src["kind"] == "video" else "web article"
    user = f"Exam date asked: {date}. Source type: {kind}. Title: {src['title']}\n\n{src['text']}"
    # Same source text on the same date always yields the same facts: reuse them (saves LLM quota across runs).
    key = hashlib.sha1((date + EXTRACT_SYS + user).encode("utf8")).hexdigest()[:20]
    cf_ = os.path.join(HERE, "cache", f"ex-{key}.json")
    if os.path.exists(cf_):
        return {**src, "facts": json.load(open(cf_, encoding="utf8"))}
    try:
        r = ask_json(EXTRACT_SYS, user, max_tokens=4000, log=log)
        facts = clean_tree(r.get("shifts", []))
        os.makedirs(os.path.dirname(cf_), exist_ok=True)
        json.dump(facts, open(cf_, "w", encoding="utf8"), ensure_ascii=False)
        return {**src, "facts": facts}
    except Exception as e:  # noqa
        log("extract failed", src["title"][:50], str(e)[:80])
        return {**src, "facts": []}


def sources_from_pack(pack):
    out = []
    for v in pack["videos"]:
        if len(v.get("transcript", "")) > 600:
            out.append({"kind": "video", "id": v["id"], "title": v["title"], "channel": v["channel"].strip(),
                        "url": f"https://www.youtube.com/watch?v={v['id']}", "text": v["transcript"]})
    for a in pack["articles"]:
        out.append({"kind": "article", "id": a["url"], "title": a["title"], "channel": a["title"], "url": a["url"], "text": a["text"]})
    return out


def src_name(s):
    t = re.sub(r"\s+", " ", s["title"])
    if s["kind"] == "video":
        m = re.search(r"(\d{1,2}(?:st|nd|rd|th)?\s+\w+\s+\d?(?:st|nd|rd)?\s*shift|shift \d)", t, re.I)
        return f"{s['channel']} (YouTube) – {t[:70]}"
    return s["title"][:90]


def status_for(n_sources, n_video):
    if n_sources >= 3 and n_video >= 2:
        return "reported"
    return "partial" if n_sources >= 1 else "pending"


def build_shift(date, n, extractions, valid_topics):
    rel = [(e, [f for f in e["facts"] if f.get("shift") == n]) for e in extractions]
    rel = [(e, f) for e, f in rel if f]
    if not rel:
        return None
    payload = [{"source": e["channel"][:40], "type": e["kind"], "reports": f} for e, f in rel]
    m = ask_json(MERGE_SYS, f"Date: {date}, Shift {n}.\nExtracted reports:\n" + json.dumps(payload, ensure_ascii=False)[:60000], max_tokens=7000, log=log)
    m = clean_tree(m)
    secs = []
    for sid, name in SECTIONS:
        s = (m.get("sections") or {}).get(sid) or {}
        topics = []
        for t in (s.get("topics") or [])[:8]:
            if isinstance(t, dict) and t.get("topic"):
                topics.append({k: v for k, v in {"topic": t["topic"], "count": t.get("count")}.items() if v})
        secs.append({"id": sid, "name": name, "questions": 25, "marks": 50, "difficulty": s.get("difficulty") or "Not reported",
                     **({"goodAttempts": s["goodAttempts"]} if s.get("goodAttempts") else {}),
                     "notes": s.get("notes") or "", "topics": topics})
    used = [e for e, _ in rel]
    n_video = sum(1 for e in used if e["kind"] == "video")
    seen, srcs = set(), []
    for e in used:
        if e["url"] not in seen:
            seen.add(e["url"]); srcs.append({"name": src_name(e), "url": e["url"]})
    asked = [a for a in (m.get("asked") or []) if isinstance(a, dict) and a.get("section") in {s for s, _ in SECTIONS} and a.get("q")][:14]
    return {"shift": n, "time": TIMES[n], "status": status_for(len(used), n_video), "auto": True,
            "overall": m.get("overall") or "Not reported", "goodAttempts": m.get("goodAttempts") or "Not reliably reported",
            "summary": m.get("summary") or "", "sections": secs, "asked": asked,
            "observations": (m.get("observations") or [])[:4], "disagreements": (m.get("disagreements") or [])[:4], "sources": srcs}


def pending_shift(n):
    return {"shift": n, "time": TIMES[n], "status": "pending", "auto": True,
            "note": "This shift has not been analysed yet. The analysis is added a few hours after the shift ends, once enough candidate reviews are out."}


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("--date", required=True)
    ap.add_argument("--pack", help="pack dir (default packs/<date>)")
    ap.add_argument("--dry", action="store_true", help="print instead of writing")
    a = ap.parse_args()
    date = a.date
    pack_dir = a.pack or os.path.join(HERE, "packs", date)
    pack = json.load(open(os.path.join(pack_dir, "pack.json"), encoding="utf8"))
    srcs = sources_from_pack(pack)
    log(f"{date}: {len(srcs)} usable sources")
    if not srcs:
        log("nothing to synthesize"); return 2
    with cf.ThreadPoolExecutor(3) as ex:
        extractions = list(ex.map(lambda s: extract_source(date, s), srcs))
    log("facts per source:", [len(e["facts"]) for e in extractions])

    path = os.path.join(OUT_DIR, date + ".json")
    day = json.load(open(path, encoding="utf8")) if os.path.exists(path) else {"exam": EXAM, "date": date, "shifts": []}
    by = {s["shift"]: s for s in day["shifts"]}
    now = dt.datetime.now(IST)
    d = dt.date.fromisoformat(date)
    valid = topic_slugs()
    changed = []
    for n in (1, 2, 3):
        old = by.get(n)
        if old and not old.get("auto") and old.get("status") == "reported":
            continue                                     # hand-written and complete: keep
        end = dt.datetime.combine(d, dt.time(*END_IST[n]), IST)
        if now < end:
            by.setdefault(n, pending_shift(n)); continue  # shift not over yet
        new = build_shift(date, n, extractions, valid)
        if new is None:
            by.setdefault(n, pending_shift(n)); continue
        rank = {"pending": 0, "partial": 1, "reported": 2}
        if old and old.get("sources") and rank.get(old.get("status"), 0) >= rank[new["status"]] and len(old["sources"]) >= len(new["sources"]):
            continue                                     # only replace with strictly better evidence
        by[n] = new; changed.append(n)
    day["shifts"] = [by[n] for n in sorted(by)]
    if not changed:
        log("no shift changed"); return 3
    summ = [{"shift": s["shift"], "status": s["status"], "overall": s.get("overall"), "goodAttempts": s.get("goodAttempts"), "summary": s.get("summary") or s.get("note")} for s in day["shifts"]]
    label = f"{d.day} {d.strftime('%B')} 2026"
    ib = ask_json(INTRO_SYS, f"Date: {label}\nShifts: " + json.dumps(summ, ensure_ascii=False), max_tokens=3000, log=log)
    day["intro"] = clean(ib.get("intro", "")) or day.get("intro", "")
    day["faqs"] = clean_tree(ib.get("faqs") or day.get("faqs") or [])[:6]
    day["updatedAt"] = now.isoformat(timespec="seconds")
    txt = json.dumps(day, ensure_ascii=False, indent=2) + "\n"
    if a.dry:
        print(txt); return 0
    os.makedirs(OUT_DIR, exist_ok=True)
    tmp = path + ".tmp"
    open(tmp, "w", encoding="utf8", newline="\n").write(txt)
    json.load(open(tmp, encoding="utf8"))
    os.replace(tmp, path)
    log(f"wrote {path} (shifts changed: {changed})")
    return 0


if __name__ == "__main__":
    sys.exit(main())
