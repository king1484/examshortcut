"""Shared helpers for the Quant-Advanced topic builders.

Every question is built through Q(), which checks that the computed answer matches exactly one
option and that all four option values are pairwise different. write_topic() validates the whole
topic dict (counts, ids, subtopic refs, LaTeX hygiene) and writes UTF-8 JSON, then re-parses it.
"""
import json
import os
import random
import re
from collections import Counter

import sympy as sp

HERE = os.path.dirname(os.path.abspath(__file__))
CONTENT = os.path.dirname(os.path.dirname(HERE))
TOPIC_DIR = os.path.join(CONTENT, "ssc-cgl", "topics", "quant")
SECTION_DIR = os.path.join(CONTENT, "ssc-cgl", "sections")

CTRL = re.compile(r"[\x00-\x08\x0b\x0c\x0e-\x1f]")


def _num(v):
    return sp.nsimplify(v) if isinstance(v, float) else sp.sympify(v)


def same(a, b):
    """True if two option values are equal (strings compare exactly, numbers/expressions symbolically)."""
    if isinstance(a, str) or isinstance(b, str):
        return isinstance(a, str) and isinstance(b, str) and a == b
    a, b = _num(a), _num(b)
    d = sp.simplify(a - b)
    if d == 0:
        return True
    syms = sorted(d.free_symbols, key=str)
    if syms:
        rnd = random.Random(7)
        for _ in range(6):
            sub = {s: sp.Rational(rnd.randint(2, 40), rnd.randint(1, 9)) for s in syms}
            try:
                if abs(complex(sp.N(d.subs(sub), 40))) > 1e-9:
                    return False
            except (TypeError, ZeroDivisionError):
                continue
        return True
    return abs(complex(sp.N(d, 50))) < 1e-12


def fmt(v):
    if isinstance(v, str):
        return v
    v = _num(v)
    if v.is_Integer:
        return str(int(v))
    if v.is_Rational:
        return f"${sp.latex(v)}$"
    return f"${sp.latex(v)}$"


def U(unit, *vals):
    """Options with a unit suffix: U(' cm', 12, 5) -> [('12 cm', 12), ('5 cm', 5)]."""
    out = []
    for v in vals:
        if isinstance(v, tuple):
            out.append(v)
        else:
            out.append((f"{fmt(v)}{unit}", v))
    return out


def Q(id, q, opts, correct, solution, shortcut, difficulty, subtopic, pattern, timeSec, figure=None):
    labels, vals = [], []
    for o in opts:
        if isinstance(o, tuple):
            labels.append(o[0])
            vals.append(o[1])
        else:
            labels.append(fmt(o))
            vals.append(o)
    assert len(labels) == 4, f"{id}: need 4 options"
    hits = [i for i, v in enumerate(vals) if same(v, correct)]
    assert len(hits) == 1, f"{id}: correct value {correct!r} matches options {hits} of {vals!r}"
    for i in range(4):
        for j in range(i + 1, 4):
            assert not same(vals[i], vals[j]), f"{id}: options {i} and {j} have equal value {vals[i]!r}"
    assert len(set(labels)) == 4, f"{id}: duplicate option labels {labels}"
    assert difficulty in ("easy", "medium", "hard"), id
    return {
        "id": id,
        "q": q.strip(),
        "figure": figure.strip() if figure else None,
        "options": labels,
        "answer": hits[0],
        "solution": solution.strip(),
        "shortcut": shortcut.strip() if shortcut else None,
        "difficulty": difficulty,
        "subtopic": subtopic,
        "pattern": pattern,
        "timeSec": int(timeSec),
    }


def F(name, tex, note=None):
    d = {"name": name, "tex": tex.strip()}
    if note:
        d["note"] = note
    return d


def T(title, body, q=None, solution=None):
    return {"title": title, "body": body.strip(),
            "example": ({"q": q.strip(), "solution": solution.strip()} if q else None)}


def S(id, title, concept, formulas, tricks, mistakes):
    return {"id": id, "title": title, "concept": concept.strip(), "formulas": formulas,
            "tricks": tricks, "mistakes": mistakes}


def P(pattern, frequency, howToSpot, approach):
    assert frequency in ("very common", "common", "occasional")
    return {"pattern": pattern, "frequency": frequency, "howToSpot": howToSpot, "approach": approach}


def _walk_strings(obj, path=""):
    if isinstance(obj, str):
        yield path, obj
    elif isinstance(obj, dict):
        for k, v in obj.items():
            yield from _walk_strings(v, f"{path}.{k}")
    elif isinstance(obj, list):
        for i, v in enumerate(obj):
            yield from _walk_strings(v, f"{path}[{i}]")


def check_strings(obj):
    problems = []
    for path, s in _walk_strings(obj):
        if CTRL.search(s):
            problems.append(f"{path}: control character (non-raw string?)")
        if "\\\\" in s:
            problems.append(f"{path}: double backslash")
        if s.count("$") % 2:
            problems.append(f"{path}: odd number of $")
        if not s.lstrip().startswith("<svg") and s.count("{") != s.count("}"):
            problems.append(f"{path}: unbalanced braces")
        if path.endswith(".figure") and s:
            for need in ("viewBox", "currentColor", "<text"):
                if need not in s:
                    problems.append(f"{path}: figure missing {need}")
    return problems


def spread(qs):
    """Rotate each question's options by a deterministic shift so correct answers spread over A-D."""
    import zlib
    for q in qs:
        i = zlib.crc32(q["id"].encode()) % 4
        if i:
            q["options"] = q["options"][i:] + q["options"][:i]
            q["answer"] = (q["answer"] - i) % 4
    return qs


def validate_topic(t):
    errs = []
    sub_ids = [s["id"] for s in t["subtopics"]]
    if not 4 <= len(sub_ids) <= 8:
        errs.append(f"subtopics count {len(sub_ids)}")
    if len(set(sub_ids)) != len(sub_ids):
        errs.append("duplicate subtopic ids")
    for s in t["subtopics"]:
        if not 2 <= len(s["tricks"]) <= 4:
            errs.append(f"{s['id']}: tricks {len(s['tricks'])}")
        if not s["formulas"]:
            errs.append(f"{s['id']}: no formulas")
        if not s["mistakes"]:
            errs.append(f"{s['id']}: no mistakes")
        for tr in s["tricks"]:
            if not tr.get("example"):
                errs.append(f"{s['id']}: trick '{tr['title']}' without example")
    if not 4 <= len(t["pyqPatterns"]) <= 8:
        errs.append(f"pyqPatterns {len(t['pyqPatterns'])}")
    if not 3 <= len(t["solvedExamples"]) <= 5:
        errs.append(f"solvedExamples {len(t['solvedExamples'])}")
    if len(t["practice"]) != 15:
        errs.append(f"practice {len(t['practice'])}")
    qids = [q["id"] for q in t["solvedExamples"] + t["practice"]]
    if len(set(qids)) != len(qids):
        errs.append(f"duplicate question ids {[k for k, v in Counter(qids).items() if v > 1]}")
    for q in t["solvedExamples"] + t["practice"]:
        if q["subtopic"] not in sub_ids:
            errs.append(f"{q['id']}: unknown subtopic {q['subtopic']}")
    for q in t["solvedExamples"]:
        if not q["shortcut"]:
            errs.append(f"{q['id']}: solved example needs shortcut")
    errs += check_strings(t)
    return errs


def write_json(obj, path):
    os.makedirs(os.path.dirname(path), exist_ok=True)
    with open(path, "w", encoding="utf-8") as f:
        json.dump(obj, f, ensure_ascii=False, indent=1)
        f.write("\n")
    with open(path, encoding="utf-8") as f:
        json.load(f)


def write_topic(t):
    spread(t["solvedExamples"])
    spread(t["practice"])
    errs = validate_topic(t)
    if errs:
        raise SystemExit("VALIDATION FAILED:\n  " + "\n  ".join(errs))
    path = os.path.join(TOPIC_DIR, f"{t['id']}.json")
    write_json(t, path)
    diff = Counter(q["difficulty"] for q in t["practice"])
    ans = Counter(q["answer"] for q in t["solvedExamples"] + t["practice"])
    subs = Counter(q["subtopic"] for q in t["practice"])
    print(f"OK {t['id']}: {len(t['subtopics'])} subtopics, {len(t['pyqPatterns'])} patterns, "
          f"{len(t['solvedExamples'])} solved, {len(t['practice'])} practice")
    print(f"   difficulty {dict(diff)}  answer-index spread {dict(sorted(ans.items()))}")
    print(f"   practice by subtopic {dict(subs)}")
    print(f"   wrote {path} ({os.path.getsize(path)} bytes)")
