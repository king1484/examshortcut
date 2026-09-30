"""Phase 3 (readable lessons) checks for topic files.

python content/_work/readable/validate.py content/core/topics/quant/time-work.json [...]
Compares against the committed version (git HEAD) so no id or pattern id disappears.
Exit code 1 if any check fails.
"""
import json
import re
import subprocess
import sys
from pathlib import Path

REPO = Path(__file__).resolve().parents[3]
TRAPS = re.compile(r"\b(trap|traps|mistake|mistakes|pitfall|quick revision|revision|recap|summary)\b", re.I)


def head_version(path: Path):
    rel = path.resolve().relative_to(REPO).as_posix()
    try:
        out = subprocess.run(["git", "show", f"HEAD:{rel}"], cwd=REPO, capture_output=True, check=True)
        return json.loads(out.stdout.decode("utf-8"))
    except Exception:
        return None


def long_sentences(text: str, limit=30):
    plain = re.sub(r"\$\$.*?\$\$|\$[^$]*\$", "X", text, flags=re.S)
    plain = re.sub(r"^\s*(?:[-*>]|\d+[.)])\s*", "", plain, flags=re.M)
    return [s.strip() for s in re.split(r"(?<=[.!?])\s+|\n", plain) if len(s.split()) > limit]


def check(path: Path):
    errs, warns = [], []
    t = json.loads(path.read_text(encoding="utf-8"))
    old = head_version(path)
    if old:
        old_sub = [s["id"] for s in old["subtopics"]]
        new_sub = [s["id"] for s in t["subtopics"]]
        missing = [x for x in old_sub if x not in new_sub]
        if missing: errs.append(f"subtopic ids removed: {missing}")
        old_q = {q["id"] for q in old.get("practice", [])}
        new_q = {q["id"] for q in t.get("practice", [])}
        if old_q - new_q: errs.append(f"practice ids removed: {sorted(old_q - new_q)[:5]}")
        old_p = {p["id"] for s in old["subtopics"] for p in s.get("patterns", [])}
        new_p = {p["id"] for s in t["subtopics"] for p in s.get("patterns", [])}
        if old_p - new_p: errs.append(f"pattern ids removed: {sorted(old_p - new_p)}")
    all_p = [p["id"] for s in t["subtopics"] for p in s.get("patterns", [])]
    dup = {x for x in all_p if all_p.count(x) > 1}
    if dup: errs.append(f"duplicate pattern ids: {sorted(dup)}")

    for s in t["subtopics"]:
        sid = s["id"]
        E = lambda m: errs.append(f"{sid}: {m}")
        W = lambda m: warns.append(f"{sid}: {m}")
        c = s.get("concept", "")
        if not c or "$$" in c: E("concept missing or has display math")
        n = s.get("notes", "")
        if not 2200 <= len(n) <= 5500: E(f"notes length {len(n)} (want 2500-5000)")
        elif not 2500 <= len(n) <= 5000: W(f"notes length {len(n)} (target 2500-5000)")
        heads = re.findall(r"^###\s+(.*)$", n, re.M)
        if not 4 <= len(heads) <= 9: E(f"{len(heads)} ### sections (want 4-8)")
        for h in heads:
            if TRAPS.search(h): E(f"notes section '{h}' belongs in mistakes/revision")
            if re.match(r"^\d", h): E(f"numbered heading '{h}'")
        if re.search(r"^#{1,2}\s", n, re.M) or re.search(r"^####", n, re.M): E("only ### headings allowed")
        if "http" in n or "www." in n: E("link in notes")
        if not re.search(r"^>\s*\*\*(Rule|Tip|Watch|Note|Example|Remember|Shortcut|Careful|Key)\b", n, re.M | re.I):
            W("no callouts in notes")
        pats = s.get("patterns", [])
        if len(pats) < 3: E(f"only {len(pats)} patterns")
        elif len(pats) < 5: W(f"{len(pats)} patterns (5-8 where the subtopic has them)")
        for p in pats:
            pid = p.get("id")
            if not p.get("howToSpot"): E(f"{pid} no howToSpot")
            st = p.get("steps") or []
            if not 2 <= len(st) <= 6: E(f"{pid} steps count {len(st)}")
            if not p.get("why"): E(f"{pid} no why")
            ex = p.get("example") or {}
            if not ex.get("q") or not ex.get("steps") or not ex.get("answer"): E(f"{pid} example needs q, steps, answer")
            if p.get("frequency") not in ("very common", "common", "occasional"): E(f"{pid} bad frequency {p.get('frequency')!r}")
        m = s.get("mistakes", [])
        if not 3 <= len(m) <= 8 or not all(isinstance(x, dict) and x.get("wrong") and x.get("right") for x in m):
            E("mistakes must be 3-8 {wrong, right} objects")
        r = s.get("revision", [])
        if not 3 <= len(r) <= 9 or not all(isinstance(x, str) and x for x in r): E("revision must be 3-9 strings")
        for k in s.get("tricks", []):
            ex = k.get("example")
            if ex and not (ex.get("steps") and ex.get("answer")) and not ex.get("solution"): E(f"trick '{k.get('title')}' example incomplete")
        blob = json.dumps(s, ensure_ascii=False)
        # every string field must have balanced $ (odd count = broken math)
        def walk(o):
            if isinstance(o, str):
                if o.replace("\\$", "").count("$") % 2: E(f"unbalanced $ in: {o[:60]}")
            elif isinstance(o, list): [walk(x) for x in o]
            elif isinstance(o, dict): [walk(v) for v in o.values()]
        walk(s)
        for ls in long_sentences(n + "\n" + c)[:3]:
            W(f"long sentence ({len(ls.split())} words): {ls[:70]}…")
        if re.search(r"[A-Za-z ]\$\\frac", blob): W("inline \\frac inside a sentence; prefer \\dfrac")
    return errs, warns


def main(paths):
    sys.stdout.reconfigure(encoding="utf-8", errors="replace")
    bad = False
    for p in paths:
        errs, warns = check(Path(p))
        print(f"== {p}: {len(errs)} errors, {len(warns)} warnings")
        for e in errs: print("  ERROR", e)
        for w in warns[:12]: print("  warn ", w)
        bad |= bool(errs)
    sys.exit(1 if bad else 0)


if __name__ == "__main__":
    main(sys.argv[1:])
