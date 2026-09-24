"""Shared helpers for the Phase-2 deep-content build scripts (quant arithmetic topics).

Each topic script builds Sub objects (notes + patterns + practice questions), then calls
apply_topic(). Everything is upserted by id, so re-running is idempotent.
"""
import json
import os
import re
import sys
import zlib
from collections import Counter
from fractions import Fraction

sys.stdout.reconfigure(encoding="utf-8")

ROOT = os.path.abspath(os.path.join(os.path.dirname(__file__), "..", "..", "..", ".."))
TOPIC_DIR = os.path.join(ROOT, "content", "core", "topics", "quant")


def path(topic):
    return os.path.join(TOPIC_DIR, topic + ".json")


def load(topic):
    with open(path(topic), encoding="utf-8") as f:
        return json.load(f)


def save(topic, data):
    with open(path(topic), "w", encoding="utf-8") as f:
        json.dump(data, f, ensure_ascii=False, indent=1)
        f.write("\n")


# ---------- formatting helpers ----------

def ind(n):
    """Indian digit grouping: 1234567 -> 12,34,567 (ints only)."""
    neg = n < 0
    s = str(abs(int(n)))
    if len(s) > 3:
        head, tail = s[:-3], s[-3:]
        parts = []
        while len(head) > 2:
            parts.insert(0, head[-2:])
            head = head[:-2]
        if head:
            parts.insert(0, head)
        s = ",".join(parts + [tail])
    return ("-" if neg else "") + s


def rs(n):
    return "₹" + ind(n)


def fr(x):
    """Fraction -> LaTeX string (inline $...$). Integers stay plain."""
    x = Fraction(x)
    if x.denominator == 1:
        return str(x.numerator)
    sign = "-" if x < 0 else ""
    return f"${sign}\\frac{{{abs(x.numerator)}}}{{{x.denominator}}}$"


def mixed(x):
    x = Fraction(x)
    if x.denominator == 1:
        return str(x.numerator)
    w, r = divmod(x.numerator, x.denominator)
    if w == 0:
        return fr(x)
    return f"${w}\\frac{{{r}}}{{{x.denominator}}}$"


def num(x):
    """Clean number: int if integral else trimmed decimal."""
    x = Fraction(x)
    if x.denominator == 1:
        return str(x.numerator)
    v = float(x)
    s = f"{v:.6f}".rstrip("0").rstrip(".")
    assert Fraction(s) == x, f"num(): {x} is not a short decimal"
    return s


def pct(x):
    return num(x) + "%"


def pick(pairs, exact, tol=1e-9):
    """pairs: [(label, numeric value)]. Returns (labels, the one label equal to exact)."""
    hits = [l for l, v in pairs if abs(float(v) - float(exact)) < tol]
    assert len(hits) == 1, ("pick: need exactly one match", exact, pairs)
    return [l for l, _ in pairs], hits[0]


def nearest(pairs, exact, min_gap=0.03):
    """Approximation questions: the correct option is the one nearest the exact value and every
    other option is at least min_gap (relative) further away."""
    ds = sorted((abs(float(v) - exact), l) for l, v in pairs)
    assert ds[1][0] - ds[0][0] >= min_gap * abs(exact), ("nearest: options too close", exact, pairs)
    return [l for l, _ in pairs], ds[0][1]


# ---------- builders ----------

class Sub:
    def __init__(self, sid, title=None):
        self.id = sid
        self.title = title
        self.fields = {}  # concept/formulas/tricks/mistakes for NEW subtopics only
        self.notes = None
        self.patterns = []
        self.questions = []

    def pattern(self, pid, name, frequency, howToSpot, formula, logic, ex_q, ex_sol):
        assert frequency in ("very common", "common", "occasional")
        self.patterns.append({
            "id": pid, "name": name, "frequency": frequency, "howToSpot": howToSpot,
            "formula": formula, "logic": logic, "example": {"q": ex_q, "solution": ex_sol},
        })

    def q(self, pat, diff, q, opts, ans, sol, sc=None, t=60):
        """opts: 4 option strings (any order, must include ans). ans: the Python-computed
        correct option string. The correct option is moved to a position picked by id hash."""
        assert diff in ("easy", "medium", "hard")
        qid = f"{self.id}-p{len(self.questions) + 1:02d}"
        opts = [str(o) for o in opts]
        ans = str(ans)
        assert len(opts) == 4, (qid, opts)
        assert len(set(opts)) == 4, (qid, "duplicate options", opts)
        assert opts.count(ans) == 1, (qid, "computed answer not in options", ans, opts)
        others = [o for o in opts if o != ans]
        pos = zlib.crc32(qid.encode()) % 4
        final = others[:pos] + [ans] + others[pos:]
        assert final[pos] == ans
        self.questions.append({
            "id": qid, "q": q, "figure": None, "options": final, "answer": pos,
            "solution": sol, "shortcut": sc, "difficulty": diff, "subtopic": self.id,
            "pattern": pat, "timeSec": t,
        })


def _strings(o):
    if isinstance(o, str):
        yield o
    elif isinstance(o, dict):
        for v in o.values():
            yield from _strings(v)
    elif isinstance(o, list):
        for v in o:
            yield from _strings(v)


def check_strings(data):
    bad = []
    for s in _strings(data):
        for ch in s:
            if ord(ch) < 32 and ch != "\n":
                bad.append((repr(ch), s[:80]))
                break
        if s.count("$") % 2:
            bad.append(("odd $ count", s[:80]))
        # literal backslash-n from a raw string (LaTeX commands like \neq, \not are lowercase)
        if re.search(r"\\n(?![a-z])", s):
            bad.append(("literal \\n", s[:80]))
    assert not bad, bad


def apply_topic(topic, subs, pyq=None, new_sub_after=None):
    data = load(topic)
    by_id = {s["id"]: s for s in data["subtopics"]}
    for sub in subs:
        if sub.id not in by_id:
            assert sub.title and sub.fields, f"new subtopic {sub.id} needs title + fields"
            entry = {"id": sub.id, "title": sub.title, **sub.fields}
            data["subtopics"].append(entry)
            by_id[sub.id] = entry
        entry = by_id[sub.id]
        if sub.fields and sub.title:
            entry["title"] = sub.title
            entry.update(sub.fields)
        entry["notes"] = sub.notes
        entry["patterns"] = sub.patterns
    # upsert practice
    pidx = {q["id"]: i for i, q in enumerate(data["practice"])}
    for sub in subs:
        for q in sub.questions:
            if q["id"] in pidx:
                data["practice"][pidx[q["id"]]] = q
            else:
                data["practice"].append(q)
                pidx[q["id"]] = len(data["practice"]) - 1
    if pyq is not None:
        data["pyqPatterns"] = pyq
    verify(data)
    save(topic, data)
    report(topic, data)
    return data


def verify(data):
    check_strings(data)
    sub_ids = {s["id"] for s in data["subtopics"]}
    pids = []
    for s in data["subtopics"]:
        n = len(s.get("notes") or "")
        assert 2500 <= n <= 5000, (s["id"], "notes length", n)
        assert 4 <= len(s.get("patterns", [])) <= 8, (s["id"], "patterns", len(s.get("patterns", [])))
        pids += [p["id"] for p in s["patterns"]]
    assert len(pids) == len(set(pids)), "duplicate pattern ids"
    pat_owner = {p["id"]: s["id"] for s in data["subtopics"] for p in s["patterns"]}
    cnt = Counter(q["subtopic"] for q in data["practice"])
    pcnt = Counter(q["pattern"] for q in data["practice"])
    for s in data["subtopics"]:
        assert cnt[s["id"]] >= 12, (s["id"], "practice", cnt[s["id"]])
        for p in s["patterns"]:
            assert pcnt[p["id"]] >= 2, (p["id"], "used", pcnt[p["id"]])
    for q in data["practice"]:
        assert q["subtopic"] in sub_ids, q["id"]
        if q["pattern"] in pat_owner:
            assert pat_owner[q["pattern"]] == q["subtopic"], (q["id"], "pattern from other subtopic")
    ids = [q["id"] for q in data["practice"] + data["solvedExamples"]]
    assert len(ids) == len(set(ids)), "duplicate question ids"
    for p in data.get("pyqPatterns", []):
        for k in ("pattern", "frequency", "howToSpot", "approach", "subtopic", "example"):
            assert k in p, (p.get("pattern"), k)
        assert p["subtopic"] in sub_ids, p["subtopic"]
    assert 6 <= len(data["pyqPatterns"]) <= 10, len(data["pyqPatterns"])


def report(topic, data):
    cnt = Counter(q["subtopic"] for q in data["practice"])
    diff = Counter(q["difficulty"] for q in data["practice"])
    ans = Counter(q["answer"] for q in data["practice"])
    print(f"\n== {topic}: {len(data['subtopics'])} subtopics, {len(data['practice'])} practice, "
          f"{len(data['pyqPatterns'])} pyqPatterns")
    print(f"{'subtopic':32} {'notes':>6} {'pats':>5} {'prac':>5}")
    tot = 0
    for s in data["subtopics"]:
        n = len(s["notes"])
        tot += n
        print(f"{s['id']:32} {n:6} {len(s['patterns']):5} {cnt[s['id']]:5}")
    print(f"notes avg {tot // len(data['subtopics'])} | difficulty {dict(diff)} | answer idx {dict(sorted(ans.items()))}")
