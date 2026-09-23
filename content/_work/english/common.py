"""Shared helpers for building English content JSON files (SSC CGL).

Every builder script imports from here. Assertions enforce the schema in content/SCHEMA.md.
"""
import json
import os
import re
from collections import Counter

HERE = os.path.dirname(os.path.abspath(__file__))
CONTENT = os.path.normpath(os.path.join(HERE, "..", ".."))
TOPIC_DIR = os.path.join(CONTENT, "ssc-cgl", "topics", "english")
MOCK_DIR = os.path.join(CONTENT, "ssc-cgl", "mocks", "parts")
SECTION_DIR = os.path.join(CONTENT, "ssc-cgl", "sections")

ENGLISH_IDS = [
    "reading-comprehension", "cloze-test", "error-spotting", "sentence-improvement",
    "fill-in-the-blanks", "synonyms-antonyms", "one-word-substitution", "idioms-phrases",
    "spelling", "active-passive", "direct-indirect", "sentence-rearrangement", "grammar-essentials",
]

ID_RE = re.compile(r"^[a-z0-9]+(-[a-z0-9]+)*$")
DIFFS = {"easy", "medium", "hard"}


def q(id, text, options, answer, solution, shortcut=None, difficulty="medium", subtopic="",
      pattern="", timeSec=45, passage=None, group=None, figure=None):
    d = {
        "id": id,
        "q": text.strip(),
        "figure": figure,
        "options": list(options),
        "answer": answer,
        "solution": solution.strip(),
        "shortcut": shortcut.strip() if shortcut else None,
        "difficulty": difficulty,
        "subtopic": subtopic,
        "pattern": pattern,
        "timeSec": timeSec,
    }
    if passage is not None:
        d["passage"] = passage.strip()
    if group is not None:
        d["group"] = group
    return d


def check_question(x, allowed_subtopics=None, need_shortcut=False):
    where = x.get("id", "?")
    for k in ["id", "q", "figure", "options", "answer", "solution", "shortcut", "difficulty",
              "subtopic", "pattern", "timeSec"]:
        assert k in x, f"{where}: missing {k}"
    assert ID_RE.match(x["id"]), f"bad id {x['id']}"
    assert isinstance(x["q"], str) and x["q"], where
    opts = x["options"]
    assert isinstance(opts, list) and len(opts) == 4, f"{where}: needs 4 options"
    assert all(isinstance(o, str) and o.strip() for o in opts), f"{where}: empty option"
    norm = [o.strip().lower() for o in opts]
    assert len(set(norm)) == 4, f"{where}: duplicate options {opts}"
    assert isinstance(x["answer"], int) and 0 <= x["answer"] <= 3, f"{where}: answer out of range"
    assert x["difficulty"] in DIFFS, f"{where}: difficulty"
    assert x["subtopic"], f"{where}: subtopic empty"
    if allowed_subtopics is not None:
        assert x["subtopic"] in allowed_subtopics, f"{where}: subtopic {x['subtopic']} not in {allowed_subtopics}"
    assert x["pattern"], f"{where}: pattern empty"
    assert isinstance(x["timeSec"], int) and x["timeSec"] > 0, where
    assert x["solution"].strip(), f"{where}: empty solution"
    if need_shortcut:
        assert x["shortcut"], f"{where}: solved example needs shortcut"


def check_groups(qs):
    groups = {}
    for x in qs:
        g = x.get("group")
        if g:
            groups.setdefault(g, []).append(x)
        elif "passage" in x:
            raise AssertionError(f"{x['id']}: passage without group")
    for g, items in groups.items():
        assert "passage" in items[0] and items[0]["passage"], f"group {g}: first question lacks passage"
        assert all("passage" not in it for it in items[1:]), f"group {g}: passage repeated"
        # group members must be contiguous
        idxs = [i for i, x in enumerate(qs) if x.get("group") == g]
        assert idxs == list(range(idxs[0], idxs[0] + len(idxs))), f"group {g} not contiguous"
    return groups


def md_table(headers, rows):
    out = ["| " + " | ".join(headers) + " |", "|" + "|".join(["---"] * len(headers)) + "|"]
    for r in rows:
        assert len(r) == len(headers), r
        out.append("| " + " | ".join(str(c) for c in r) + " |")
    return "\n".join(out)


def _dump(path, data):
    os.makedirs(os.path.dirname(path), exist_ok=True)
    with open(path, "w", encoding="utf-8") as f:
        json.dump(data, f, ensure_ascii=False, indent=1)
    with open(path, encoding="utf-8") as f:
        json.load(f)  # re-parse check
    return path


def write_topic(t):
    assert t["id"] in ENGLISH_IDS, t["id"]
    assert t["sectionId"] == "english"
    assert t["order"] == ENGLISH_IDS.index(t["id"]) + 1, f"order mismatch for {t['id']}"
    assert t["importance"] in {"high", "medium", "low"}
    assert set(t["avgQuestions"]) == {"tier1", "tier2"}
    subs = t["subtopics"]
    assert 3 <= len(subs) <= 8, f"{t['id']}: {len(subs)} subtopics"
    sub_ids = set()
    for s in subs:
        assert ID_RE.match(s["id"]) and s["id"] not in sub_ids, s["id"]
        sub_ids.add(s["id"])
        for k in ["title", "concept", "formulas", "tricks", "mistakes"]:
            assert k in s, f"{s['id']} missing {k}"
        assert len(s["concept"]) > 200, f"{s['id']}: concept too thin"
        assert s["tricks"], f"{s['id']}: no tricks"
        for tr in s["tricks"]:
            assert tr.get("title") and tr.get("body"), s["id"]
            if tr.get("example") is not None:
                assert tr["example"].get("q") and tr["example"].get("solution"), s["id"]
        assert s["mistakes"], f"{s['id']}: no mistakes"
    assert 4 <= len(t["pyqPatterns"]) <= 8, f"{t['id']}: {len(t['pyqPatterns'])} patterns"
    for p in t["pyqPatterns"]:
        assert p["frequency"] in {"very common", "common", "occasional"}
        assert p["pattern"] and p["howToSpot"] and p["approach"]
    se, pr = t["solvedExamples"], t["practice"]
    assert 3 <= len(se) <= 5, f"{t['id']}: {len(se)} solved"
    assert 12 <= len(pr) <= 15, f"{t['id']}: {len(pr)} practice"
    ids = set()
    for x in se + pr:
        assert x["id"] not in ids, f"dup id {x['id']}"
        ids.add(x["id"])
    for x in se:
        check_question(x, sub_ids, need_shortcut=True)
    for x in pr:
        check_question(x, sub_ids)
    check_groups(se)
    check_groups(pr)
    ordered = {
        "id": t["id"], "sectionId": "english", "title": t["title"], "order": t["order"],
        "importance": t["importance"], "avgQuestions": t["avgQuestions"], "summary": t["summary"].strip(),
        "subtopics": subs, "pyqPatterns": t["pyqPatterns"], "solvedExamples": se, "practice": pr,
    }
    path = _dump(os.path.join(TOPIC_DIR, t["id"] + ".json"), ordered)
    dist = Counter(x["answer"] for x in se + pr)
    print(f"OK {t['id']}: {len(subs)} subtopics, {len(t['pyqPatterns'])} patterns, "
          f"{len(se)} solved, {len(pr)} practice, answer dist {dict(sorted(dist.items()))}")
    return path


def write_mock(mock_id, questions, expected):
    assert len(questions) == expected, f"{mock_id}: {len(questions)} != {expected}"
    ids = set()
    for x in questions:
        assert x["id"] not in ids, f"dup id {x['id']}"
        ids.add(x["id"])
        check_question(x, set(ENGLISH_IDS))
    groups = check_groups(questions)
    data = {"mockId": mock_id, "sectionId": "english", "questions": questions}
    path = _dump(os.path.join(MOCK_DIR, f"{mock_id}--english.json"), data)
    dist = Counter(x["answer"] for x in questions)
    by_topic = Counter(x["subtopic"] for x in questions)
    print(f"OK {mock_id}: {len(questions)} Qs, groups {{{', '.join(f'{g}:{len(v)}' for g, v in groups.items())}}}, "
          f"answer dist {dict(sorted(dist.items()))}")
    print("   topics:", dict(by_topic))
    return path
