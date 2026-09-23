"""Shared helpers for building SSC CGL General Awareness content.

Usage in a build script (same folder):
    from gacommon import Q, save_topic, save_mock, ROOT
Run with:  py -3 build_xxx.py
"""
import json
import os
import re

ROOT = os.path.abspath(os.path.join(os.path.dirname(__file__), "..", "..", "ssc-cgl"))
TOPIC_DIR = os.path.join(ROOT, "topics", "ga")
MOCK_DIR = os.path.join(ROOT, "mocks", "parts")
SECTION_DIR = os.path.join(ROOT, "sections")

GA_TOPICS = [
    "ancient-history", "medieval-history", "modern-history", "art-culture", "polity",
    "indian-geography", "world-geography", "economy", "physics", "chemistry", "biology",
    "static-gk", "current-affairs",
]
ORDER = {t: i + 1 for i, t in enumerate(GA_TOPICS)}

DIFFS = {"easy", "medium", "hard"}
FREQS = {"very common", "common", "occasional"}
IMPORTANCE = {"high", "medium", "low"}


def Q(id, q, options, answer, solution, shortcut=None, difficulty="medium",
      subtopic="", pattern="", timeSec=30, figure=None, **extra):
    d = {
        "id": id,
        "q": q,
        "figure": figure,
        "options": list(options),
        "answer": answer,
        "solution": solution,
        "shortcut": shortcut,
        "difficulty": difficulty,
        "subtopic": subtopic,
        "pattern": pattern,
        "timeSec": timeSec,
    }
    d.update(extra)
    return d


def _norm(s):
    return re.sub(r"\s+", " ", str(s).strip().lower())


def validate_question(x, where=""):
    tag = f"{where}:{x.get('id')}"
    for k in ["id", "q", "figure", "options", "answer", "solution", "shortcut",
              "difficulty", "subtopic", "pattern", "timeSec"]:
        assert k in x, f"{tag} missing {k}"
    assert re.fullmatch(r"[a-z0-9]+(-[a-z0-9]+)*", x["id"]), f"{tag} bad id"
    assert isinstance(x["q"], str) and x["q"].strip(), f"{tag} empty q"
    opts = x["options"]
    assert isinstance(opts, list) and len(opts) == 4, f"{tag} needs 4 options"
    assert all(isinstance(o, str) and o.strip() for o in opts), f"{tag} empty option"
    assert len({_norm(o) for o in opts}) == 4, f"{tag} options not unique: {opts}"
    assert isinstance(x["answer"], int) and 0 <= x["answer"] < 4, f"{tag} answer out of range"
    assert isinstance(x["solution"], str) and x["solution"].strip(), f"{tag} empty solution"
    assert x["shortcut"] is None or (isinstance(x["shortcut"], str) and x["shortcut"].strip()), f"{tag} bad shortcut"
    assert x["difficulty"] in DIFFS, f"{tag} bad difficulty"
    assert isinstance(x["subtopic"], str) and x["subtopic"], f"{tag} empty subtopic"
    assert isinstance(x["pattern"], str) and x["pattern"], f"{tag} empty pattern"
    assert isinstance(x["timeSec"], int) and 5 <= x["timeSec"] <= 300, f"{tag} bad timeSec"
    if x.get("group") is not None:
        assert isinstance(x["group"], str)


def _write(path, data):
    os.makedirs(os.path.dirname(path), exist_ok=True)
    with open(path, "w", encoding="utf-8") as f:
        json.dump(data, f, ensure_ascii=False, indent=1)
    with open(path, encoding="utf-8") as f:
        json.load(f)  # re-parse check
    return path


def save_topic(t, min_practice=15, max_practice=20):
    tid = t["id"]
    assert tid in GA_TOPICS, f"unknown topic id {tid}"
    t.setdefault("sectionId", "ga")
    t.setdefault("order", ORDER[tid])
    assert t["sectionId"] == "ga"
    assert t["order"] == ORDER[tid], f"{tid} order should be {ORDER[tid]}"
    for k in ["title", "importance", "avgQuestions", "summary", "subtopics",
              "pyqPatterns", "solvedExamples", "practice"]:
        assert k in t, f"{tid} missing {k}"
    assert t["importance"] in IMPORTANCE
    assert set(t["avgQuestions"]) == {"tier1", "tier2"}
    sub_ids = []
    for s in t["subtopics"]:
        for k in ["id", "title", "concept", "formulas", "tricks", "mistakes"]:
            assert k in s, f"{tid}/{s.get('id')} missing {k}"
        assert re.fullmatch(r"[a-z0-9]+(-[a-z0-9]+)*", s["id"]), f"bad subtopic id {s['id']}"
        for fm in s["formulas"]:
            assert set(fm) >= {"name", "tex"}, f"{s['id']} formula keys"
            fm.setdefault("note", "")
        for tr in s["tricks"]:
            assert "title" in tr and "body" in tr, f"{s['id']} trick keys"
            if tr.get("example") is not None:
                assert set(tr["example"]) >= {"q", "solution"}
        assert isinstance(s["mistakes"], list)
        sub_ids.append(s["id"])
    assert len(sub_ids) == len(set(sub_ids)), f"{tid} duplicate subtopic ids"
    for p in t["pyqPatterns"]:
        assert set(p) >= {"pattern", "frequency", "howToSpot", "approach"}, p
        assert p["frequency"] in FREQS, p["frequency"]
    assert 3 <= len(t["solvedExamples"]) <= 5, f"{tid} solvedExamples count {len(t['solvedExamples'])}"
    assert min_practice <= len(t["practice"]) <= max_practice, f"{tid} practice count {len(t['practice'])}"
    ids = set()
    stems = set()
    for x in t["solvedExamples"] + t["practice"]:
        validate_question(x, tid)
        assert x["id"] not in ids, f"{tid} duplicate question id {x['id']}"
        ids.add(x["id"])
        assert x["subtopic"] in sub_ids, f"{tid}:{x['id']} subtopic {x['subtopic']} not in {sub_ids}"
        st = _norm(x["q"])
        assert st not in stems, f"{tid}:{x['id']} duplicate question text"
        stems.add(st)
    ordered = ["id", "sectionId", "title", "order", "importance", "avgQuestions", "summary",
               "subtopics", "pyqPatterns", "solvedExamples", "practice"]
    out = {k: t[k] for k in ordered}
    path = _write(os.path.join(TOPIC_DIR, tid + ".json"), out)
    ans = [x["answer"] for x in t["practice"]]
    print(f"OK {path}: {len(sub_ids)} subtopics, {len(t['solvedExamples'])} solved, "
          f"{len(t['practice'])} practice, answer spread {[ans.count(i) for i in range(4)]}")
    return path


def save_mock(mock_id, questions, expected):
    assert len(questions) == expected, f"{mock_id} has {len(questions)} != {expected}"
    ids = set()
    for x in questions:
        validate_question(x, mock_id)
        assert x["subtopic"] in GA_TOPICS, f"{mock_id}:{x['id']} subtopic must be a GA topic id"
        assert x["id"] not in ids, f"{mock_id} dup id {x['id']}"
        ids.add(x["id"])
    path = _write(os.path.join(MOCK_DIR, f"{mock_id}--ga.json"),
                  {"mockId": mock_id, "sectionId": "ga", "questions": questions})
    ans = [x["answer"] for x in questions]
    dist = {}
    for x in questions:
        dist[x["subtopic"]] = dist.get(x["subtopic"], 0) + 1
    print(f"OK {path}: {len(questions)} Qs, answer spread {[ans.count(i) for i in range(4)]}, topics {dist}")
    return path


def save_section(sec):
    for k in ["id", "name", "short", "tier1", "tier2", "overview", "strategy", "topics"]:
        assert k in sec, f"section missing {k}"
    for t in sec["topics"]:
        assert os.path.exists(os.path.join(TOPIC_DIR, t + ".json")), f"topic file missing: {t}"
    return _write(os.path.join(SECTION_DIR, sec["id"] + ".json"), sec)


def all_topic_questions():
    """Return {normalised stem: (topic, id)} for every topic question already written."""
    out = {}
    for t in GA_TOPICS:
        p = os.path.join(TOPIC_DIR, t + ".json")
        if not os.path.exists(p):
            continue
        with open(p, encoding="utf-8") as f:
            d = json.load(f)
        for x in d["solvedExamples"] + d["practice"]:
            out[_norm(x["q"])] = (t, x["id"], x["options"][x["answer"]])
    return out
