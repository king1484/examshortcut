"""Shared helpers for Phase-2 deep-content build scripts (reasoning topics).

Usage in a topic script:

    from _lib import *
    d = load("analogy")
    set_sub(d, "letter-analogy", notes=NOTES, patterns=[P(...), ...])
    add_sub(d, {...full new subtopic...}, after="number-analogy")      # optional
    upsert(d["practice"], [Q(...), ...])
    d["pyqPatterns"] = [PYQ(...), ...]
    finish("analogy", d)

Everything is upserted by id, so re-running a script is idempotent.
"""
import hashlib
import json
import os
import random
import re
import subprocess
import sys
from collections import Counter

sys.stdout.reconfigure(encoding="utf-8")

ROOT = os.path.abspath(os.path.join(os.path.dirname(__file__), "..", "..", "..", ".."))
TOPIC_DIR = os.path.join(ROOT, "content", "core", "topics", "reasoning")


def path(topic):
    return os.path.join(TOPIC_DIR, topic + ".json")


def load(topic):
    with open(path(topic), encoding="utf-8") as f:
        return json.load(f)


def save(topic, data):
    with open(path(topic), "w", encoding="utf-8") as f:
        json.dump(data, f, ensure_ascii=False, indent=1)
        f.write("\n")


# ---------------- letter helpers (A=1 ... Z=26) ----------------

def pos(c):
    return ord(c.upper()) - 64


def let(n):
    return chr((n - 1) % 26 + 65)


def shift(word, k):
    """Shift each letter by k (int) or by a per-slot list/tuple k (cycled)."""
    if isinstance(k, int):
        k = [k]
    return "".join(let(pos(c) + k[i % len(k)]) for i, c in enumerate(word))


def opp(word):
    """Opposite letters (A<->Z, B<->Y ...): 27 - position."""
    return "".join(let(27 - pos(c)) for c in word)


def rev(word):
    return word[::-1]


def psum(word):
    return sum(pos(c) for c in word)


def rpos(c):
    """Reverse position: Z=1 ... A=26."""
    return 27 - pos(c)


def diffs(word_a, word_b):
    """Slot-wise shift tuple from a to b, in range -12..13."""
    out = []
    for a, b in zip(word_a, word_b):
        d = (pos(b) - pos(a)) % 26
        if d > 13:
            d -= 26
        out.append(d)
    return out


def steps(word):
    """Steps between consecutive letters inside one cluster (wrap-aware, -12..13)."""
    return diffs(word[:-1], word[1:])


def sgn(n):
    return f"+{n}" if n >= 0 else f"−{abs(n)}"


# ---------------- builders ----------------

def P(id, name, frequency, howToSpot, logic, ex_q, ex_sol, formula=None):
    assert frequency in ("very common", "common", "occasional"), (id, frequency)
    return {
        "id": id,
        "name": name,
        "frequency": frequency,
        "howToSpot": howToSpot,
        "formula": formula,
        "logic": logic,
        "example": {"q": ex_q, "solution": ex_sol},
    }


def Q(id, q, ans, wrong, solution, shortcut=None, diff="medium", sub=None, pat=None,
      t=45, check=None, figure=None):
    """Build a Question. `ans` is the correct option text; `wrong` the 3 distractors.
    If `check` is given it must equal `ans` (computed value vs stored value)."""
    ans = str(ans)
    wrong = [str(w) for w in wrong]
    if check is not None:
        assert str(check) == ans, f"{id}: computed {check!r} != stored {ans!r}"
    opts = [ans] + wrong
    assert len(opts) == 4, f"{id}: need exactly 3 distractors"
    assert len(set(opts)) == 4, f"{id}: duplicate options {opts}"
    assert diff in ("easy", "medium", "hard"), id
    assert sub and pat, id
    rnd = random.Random(int(hashlib.md5(id.encode()).hexdigest(), 16))
    others = wrong[:]
    rnd.shuffle(others)
    idx = rnd.randrange(4)
    options = others[:idx] + [ans] + others[idx:]
    return {
        "id": id,
        "q": q,
        "figure": figure,
        "options": options,
        "answer": idx,
        "solution": solution,
        "shortcut": shortcut,
        "difficulty": diff,
        "subtopic": sub,
        "pattern": pat,
        "timeSec": t,
    }


def PYQ(pattern, frequency, howToSpot, approach, subtopic, ex_q=None, ex_sol=None):
    return {
        "pattern": pattern,
        "frequency": frequency,
        "howToSpot": howToSpot,
        "approach": approach,
        "subtopic": subtopic,
        "example": {"q": ex_q, "solution": ex_sol} if ex_q else None,
    }


# ---------------- mutation helpers ----------------

def upsert(lst, items):
    idx = {x["id"]: i for i, x in enumerate(lst)}
    for it in items:
        if it["id"] in idx:
            lst[idx[it["id"]]] = it
        else:
            idx[it["id"]] = len(lst)
            lst.append(it)


def get_sub(d, sid):
    for s in d["subtopics"]:
        if s["id"] == sid:
            return s
    raise KeyError(sid)


def set_sub(d, sid, **fields):
    s = get_sub(d, sid)
    s.update(fields)
    return s


def add_sub(d, sub, after=None):
    """Insert (or replace) a full new subtopic by id."""
    for i, s in enumerate(d["subtopics"]):
        if s["id"] == sub["id"]:
            d["subtopics"][i] = sub
            return
    if after is None:
        d["subtopics"].append(sub)
        return
    for i, s in enumerate(d["subtopics"]):
        if s["id"] == after:
            d["subtopics"].insert(i + 1, sub)
            return
    d["subtopics"].append(sub)


def patch_q(d, qid, **fields):
    """Correct fields of an EXISTING question (solvedExamples or practice)."""
    for q in d.get("solvedExamples", []) + d.get("practice", []):
        if q["id"] == qid:
            q.update(fields)
            return q
    raise KeyError(qid)


# ---------------- checks ----------------

BAD = re.compile(r"[\x00-\x08\x0b\x0c\x0e-\x1f]")


def scan_ctrl(obj, where="$"):
    bad = []
    if isinstance(obj, str):
        if BAD.search(obj):
            bad.append(f"{where}: {obj[:60]!r}")
    elif isinstance(obj, dict):
        for k, v in obj.items():
            bad += scan_ctrl(v, f"{where}.{k}")
    elif isinstance(obj, list):
        for i, v in enumerate(obj):
            bad += scan_ctrl(v, f"{where}[{i}]")
    return bad


def check(d):
    errs = []
    bad = scan_ctrl(d)
    errs += [f"control char at {b}" for b in bad]
    for s in [s for s in d["subtopics"] if False]:
        pass
    sub_ids = [s["id"] for s in d["subtopics"]]
    assert len(sub_ids) == len(set(sub_ids)), "duplicate subtopic ids"
    pat_ids = []
    for s in d["subtopics"]:
        for p in s.get("patterns", []):
            pat_ids.append(p["id"])
    dup = [k for k, v in Counter(pat_ids).items() if v > 1]
    if dup:
        errs.append(f"duplicate pattern ids {dup}")
    qids = [q["id"] for q in d["solvedExamples"] + d["practice"]]
    dupq = [k for k, v in Counter(qids).items() if v > 1]
    if dupq:
        errs.append(f"duplicate question ids {dupq}")
    pat_set = set(pat_ids)
    use = Counter()
    per_sub = Counter()
    diffc = Counter()
    for q in d["practice"]:
        per_sub[q.get("subtopic")] += 1
        if q.get("pattern") in pat_set:
            use[q["pattern"]] += 1
            diffc[q["difficulty"]] += 1
        if q.get("subtopic") not in sub_ids:
            errs.append(f"{q['id']}: unknown subtopic {q.get('subtopic')}")
        if len(q["options"]) != 4 or len(set(q["options"])) != 4:
            errs.append(f"{q['id']}: bad options")
        if not (0 <= q["answer"] <= 3):
            errs.append(f"{q['id']}: bad answer index")
    # new questions must point at a pattern of their own subtopic
    pat_owner = {p["id"]: s["id"] for s in d["subtopics"] for p in s.get("patterns", [])}
    for q in d["practice"]:
        if q.get("pattern") in pat_owner and pat_owner[q["pattern"]] != q["subtopic"]:
            errs.append(f"{q['id']}: pattern {q['pattern']} belongs to {pat_owner[q['pattern']]}, not {q['subtopic']}")
    rows = []
    for s in d["subtopics"]:
        n = len(s.get("notes", ""))
        ps = s.get("patterns", [])
        if not (2500 <= n <= 5000):
            errs.append(f"{s['id']}: notes length {n} outside 2500-5000")
        if not (4 <= len(ps) <= 8):
            errs.append(f"{s['id']}: {len(ps)} patterns (need 4-8)")
        if per_sub[s["id"]] < 12:
            errs.append(f"{s['id']}: only {per_sub[s['id']]} practice questions")
        for p in ps:
            if use[p["id"]] < 2:
                errs.append(f"{p['id']}: used by {use[p['id']]} practice questions (need >=2)")
            for k in ("id", "name", "frequency", "howToSpot", "formula", "logic", "example"):
                if k not in p:
                    errs.append(f"{p['id']}: missing {k}")
        if "notes" in s and "### Quick revision" not in s["notes"]:
            errs.append(f"{s['id']}: notes lack '### Quick revision'")
        if re.search(r"https?://|www\.|Source:", s.get("notes", "")):
            errs.append(f"{s['id']}: notes contain a URL/Source line")
        rows.append((s["id"], n, len(ps), per_sub[s["id"]]))
    pyq = d.get("pyqPatterns", [])
    if not (6 <= len(pyq) <= 10):
        errs.append(f"pyqPatterns count {len(pyq)} (need 6-10)")
    for p in pyq:
        for k in ("pattern", "frequency", "howToSpot", "approach", "subtopic", "example"):
            if k not in p:
                errs.append(f"pyq '{p.get('pattern')}' missing {k}")
        if p.get("subtopic") not in sub_ids:
            errs.append(f"pyq '{p.get('pattern')}' unknown subtopic {p.get('subtopic')}")
    return errs, rows, diffc


def finish(topic, d, before=None):
    errs, rows, diffc = check(d)
    save(topic, d)
    print(f"\n== {topic}: {len(d['subtopics'])} subtopics, {len(d['practice'])} practice, "
          f"{len(d.get('pyqPatterns', []))} pyqPatterns")
    print(f"{'subtopic':32} {'notes':>6} {'pats':>5} {'prac':>5}")
    for r in rows:
        print(f"{r[0]:32} {r[1]:>6} {r[2]:>5} {r[3]:>5}")
    tot = sum(diffc.values()) or 1
    print("new-question difficulty mix:", {k: f"{v} ({100*v//tot}%)" for k, v in diffc.items()})
    if rows:
        print("notes avg chars:", sum(r[1] for r in rows) // len(rows))
    if errs:
        print("\nTARGET PROBLEMS:")
        for e in errs:
            print("  -", e)
    else:
        print("all targets met")
    r = subprocess.run(["node", "scripts/validate-content.mjs"], cwd=ROOT, capture_output=True, text=True)
    print(r.stdout.strip().splitlines()[-1] if r.stdout.strip() else r.stdout, r.stderr[-2000:])
    return errs
