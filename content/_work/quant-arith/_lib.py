"""Shared builder + verifier for the quant arithmetic topic scripts.

Every question goes through Q(), which asserts that the option marked correct
equals the value computed in Python (`ans`) and that all distractors differ.
write_topic() validates the whole topic against content/SCHEMA.md and dumps JSON.
"""
import json
import math
import os
import re
from fractions import Fraction as F

ROOT = os.path.abspath(os.path.join(os.path.dirname(__file__), "..", ".."))
OUT_DIR = os.path.join(ROOT, "ssc-cgl", "topics", "quant")


def md(*lines):
    return "\n".join(lines)


# ---------------------------------------------------------------- parsing
_UNIT_RE = re.compile(
    r"\s*(km/h|km/hr|kmph|m/s|km|metres|metre|m|hours|hour|hrs|hr|h|days|day|minutes|minute|min|"
    r"seconds|second|sec|s|years|year|yrs|months|month|litres|litre|L|ml|kg|g|cm|men|women|"
    r"boys|girls|persons|person|workers|units|unit|paise|marks|students|pens|articles|items|"
    r"rounds|times|litres|runs|numbers|pages|toffees|coins|notes)\.?$"
)


def _clean(s):
    t = s.replace("$", "").replace("₹", "").replace("Rs.", "").replace("Rs", "")
    t = t.replace("\\%", "").replace("%", "").replace("\\,", "").strip()
    t = re.sub(r"(?<=\d),(?=\d{2})", "", t)  # Indian / western thousands separators
    for _ in range(3):
        t = _UNIT_RE.sub("", t).strip()
    return t


def _scalar(t):
    t = t.strip().replace("−", "-").replace("–", "-")
    neg = False
    if t.startswith("-"):
        neg = True
        t = t[1:].strip()
    elif t.startswith("+"):
        t = t[1:].strip()
    t = t.replace("\\dfrac", "\\frac").replace("\\tfrac", "\\frac")
    m = re.fullmatch(r"(\d+)\s*\\frac\{(\d+)\}\{(\d+)\}", t)
    if m:
        v = int(m.group(1)) + F(int(m.group(2)), int(m.group(3)))
    else:
        m = re.fullmatch(r"\\frac\{(\d+(?:\.\d+)?)\}\{(\d+(?:\.\d+)?)\}", t)
        if m:
            v = F(m.group(1)) / F(m.group(2))
        else:
            m = re.fullmatch(r"(\d+(?:\.\d+)?)\s*/\s*(\d+(?:\.\d+)?)", t)
            if m:
                v = F(m.group(1)) / F(m.group(2))
            else:
                m = re.fullmatch(r"\d+(?:\.\d+)?", t)
                if not m:
                    raise ValueError("cannot parse scalar: %r" % t)
                v = F(t)
    return -v if neg else v


def parse(s):
    """Option string -> Fraction, or tuple of Fractions (ratio, normalised)."""
    t = _clean(s)
    if ":" in t:
        parts = [_scalar(_clean(p)) for p in t.split(":")]
        g = parts[0]
        return tuple(p / g for p in parts)
    return _scalar(t)


def _norm(v):
    if isinstance(v, tuple):
        g = F(v[0])
        return tuple(F(x) / g for x in v)
    return v


def _eq(a, b):
    a, b = _norm(a), _norm(b)
    if isinstance(a, tuple) or isinstance(b, tuple):
        if not (isinstance(a, tuple) and isinstance(b, tuple)) or len(a) != len(b):
            return False
        return all(_eq(x, y) for x, y in zip(a, b))
    if isinstance(a, F) and isinstance(b, (F, int)):
        return a == b
    if isinstance(b, F) and isinstance(a, int):
        return a == b
    return abs(float(a) - float(b)) <= 1e-6 * max(1.0, abs(float(b)))


# ---------------------------------------------------------------- questions
ALL_IDS = set()


def Q(id, q, options, answer, ans, solution, shortcut, difficulty, subtopic, pattern, timeSec,
      vals=None, figure=None):
    """Build a question dict and verify it.

    ans   : computed correct value (number / Fraction / tuple ratio) or a str
            (then options[answer] must equal it exactly).
    vals  : optional explicit numeric values for the 4 options (e.g. surds built with sympy).
    """
    assert id not in ALL_IDS, "duplicate id " + id
    ALL_IDS.add(id)
    assert isinstance(options, list) and len(options) == 4, id + ": need 4 options"
    assert len(set(options)) == 4, id + ": duplicate option strings"
    assert 0 <= answer < 4, id
    assert difficulty in ("easy", "medium", "hard"), id
    if isinstance(ans, str):
        assert options[answer] == ans, "%s: marked %r but computed %r" % (id, options[answer], ans)
    else:
        if vals is None:
            vals = [parse(o) for o in options]
        assert len(vals) == 4
        assert _eq(vals[answer], ans), "%s: marked option %r (=%s) but computed %s" % (
            id, options[answer], vals[answer], ans)
        for i, v in enumerate(vals):
            if i != answer:
                assert not _eq(v, ans), "%s: distractor %r equals the answer" % (id, options[i])
        for i in range(4):
            for j in range(i + 1, 4):
                assert not _eq(vals[i], vals[j]), "%s: options %d and %d are equal" % (id, i, j)
    return {
        "id": id, "q": q, "figure": figure, "options": options, "answer": answer,
        "solution": solution, "shortcut": shortcut, "difficulty": difficulty,
        "subtopic": subtopic, "pattern": pattern, "timeSec": timeSec,
    }


def nearest(options_vals, exact):
    """Index of option nearest to `exact` (for 'approximately' questions); asserts clear winner."""
    d = sorted((abs(float(v) - float(exact)), i) for i, v in enumerate(options_vals))
    assert d[1][0] - d[0][0] > 0, "ambiguous approximation"
    return d[0][1]


# ---------------------------------------------------------------- topic helpers
def formula(name, tex, note=None):
    d = {"name": name, "tex": tex}
    if note:
        d["note"] = note
    return d


def trick(title, body, q, solution):
    return {"title": title, "body": body, "example": {"q": q, "solution": solution}}


def sub(id, title, concept, formulas, tricks, mistakes):
    return {"id": id, "title": title, "concept": concept, "formulas": formulas,
            "tricks": tricks, "mistakes": mistakes}


def pat(pattern, frequency, howToSpot, approach):
    assert frequency in ("very common", "common", "occasional")
    return {"pattern": pattern, "frequency": frequency, "howToSpot": howToSpot, "approach": approach}


# ---------------------------------------------------------------- validation
_CTRL = re.compile(r"[\x00-\x08\x0b-\x1f]")


def _check_text(s, where):
    assert isinstance(s, str), where
    assert not _CTRL.search(s), "control char (non-raw backslash?) in " + where + ": " + repr(s[:80])
    # inline math segments
    body = s.replace("$$", "\x00DISPLAY\x00")
    n = body.count("$")
    assert n % 2 == 0, "unbalanced $ in %s: %r" % (where, s[:120])
    segs = body.split("$")[1::2]
    for seg in segs:
        assert "\n" not in seg, "newline inside inline math in %s: %r" % (where, seg)
        assert not re.search(r"(?<!\\)%", seg), "unescaped % in math in %s: %r" % (where, seg)
        assert "₹" not in seg, "rupee sign inside math in %s" % where
    for seg in s.split("$$")[1::2]:
        assert not re.search(r"(?<!\\)%", seg), "unescaped % in display math in %s" % where
    assert s.count("$$") % 2 == 0, "unbalanced $$ in " + where
    if s.count("{") != s.count("}"):
        raise AssertionError("unbalanced braces in %s: %r" % (where, s[:200]))


def _walk(o, where="root"):
    if isinstance(o, dict):
        for k, v in o.items():
            if k == "tex":
                assert "$" not in v, "tex must not contain $ at " + where
                assert v.count("{") == v.count("}"), "unbalanced braces in tex at " + where
                assert not _CTRL.search(v), "control char in tex at " + where
                assert not re.search(r"(?<!\\)%", v), "unescaped % in tex at " + where
            else:
                _walk(v, where + "." + str(k))
    elif isinstance(o, list):
        for i, v in enumerate(o):
            _walk(v, "%s[%d]" % (where, i))
    elif isinstance(o, str):
        _check_text(o, where)


def write_topic(t):
    req = ["id", "sectionId", "title", "order", "importance", "avgQuestions", "summary",
           "subtopics", "pyqPatterns", "solvedExamples", "practice"]
    for k in req:
        assert k in t, "missing " + k
    assert t["sectionId"] == "quant"
    assert t["importance"] in ("high", "medium", "low")
    assert set(t["avgQuestions"]) == {"tier1", "tier2"}
    subs = t["subtopics"]
    assert 3 <= len(subs) <= 7, "subtopics count"
    sub_ids = [s["id"] for s in subs]
    assert len(set(sub_ids)) == len(sub_ids)
    for s in subs:
        assert s["concept"] and s["formulas"], s["id"]
        assert 2 <= len(s["tricks"]) <= 4, "tricks count in " + s["id"]
        assert s["mistakes"], s["id"]
        for tr in s["tricks"]:
            assert tr["title"] and tr["body"] and tr["example"]["q"] and tr["example"]["solution"]
    assert 4 <= len(t["pyqPatterns"]) <= 8, "pyqPatterns count"
    assert 3 <= len(t["solvedExamples"]) <= 5, "solvedExamples count"
    assert len(t["practice"]) == 15, "practice count"
    ids = set()
    for qq in t["solvedExamples"] + t["practice"]:
        assert qq["id"] not in ids
        ids.add(qq["id"])
        assert qq["subtopic"] in sub_ids, "%s: unknown subtopic %s" % (qq["id"], qq["subtopic"])
    for qq in t["solvedExamples"]:
        assert qq["shortcut"], qq["id"] + ": solved example needs shortcut"
    diffs = [qq["difficulty"] for qq in t["practice"]]
    cnt = {d: diffs.count(d) for d in ("easy", "medium", "hard")}
    assert 4 <= cnt["easy"] <= 6 and 6 <= cnt["medium"] <= 8 and 2 <= cnt["hard"] <= 4, cnt
    # every subtopic should be tested at least once somewhere
    used = {qq["subtopic"] for qq in t["solvedExamples"] + t["practice"]}
    missing = set(sub_ids) - used
    assert not missing, "subtopics never tested: %s" % missing
    _walk(t)
    os.makedirs(OUT_DIR, exist_ok=True)
    path = os.path.join(OUT_DIR, t["id"] + ".json")
    with open(path, "w", encoding="utf-8") as f:
        json.dump(t, f, ensure_ascii=False, indent=1)
    with open(path, encoding="utf-8") as f:
        json.load(f)
    print("OK %s: %d subtopics, %d patterns, %d solved, %d practice %s -> %s" % (
        t["id"], len(subs), len(t["pyqPatterns"]), len(t["solvedExamples"]),
        len(t["practice"]), cnt, path))
