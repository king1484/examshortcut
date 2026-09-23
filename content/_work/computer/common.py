"""Shared builder + validator for the SSC CGL computer section files."""
import json, os, re

BASE = r"C:\Users\Vinay Singirikonda\Desktop\examshortcut\content\ssc-cgl"
OUT_TOPIC = os.path.join(BASE, "topics", "computer")
OUT_MOCK = os.path.join(BASE, "mocks", "parts")
OUT_SECTION = os.path.join(BASE, "sections")
KEBAB = re.compile(r"^[a-z0-9]+(-[a-z0-9]+)*$")
DIFFS = {"easy", "medium", "hard"}
TOPIC_IDS = ["computer-fundamentals", "hardware-memory", "software-os", "ms-word",
             "ms-excel", "ms-powerpoint", "internet-email", "networking",
             "cyber-security", "keyboard-shortcuts"]

_seen_ids = {}

def Q(qid, q, options, answer, solution, shortcut, difficulty, subtopic, pattern, timeSec=45):
    assert KEBAB.match(qid), f"bad id {qid}"
    assert isinstance(options, list) and len(options) == 4, f"{qid}: need 4 options"
    assert len(set(map(str, options))) == 4, f"{qid}: options not unique"
    assert isinstance(answer, int) and 0 <= answer <= 3, f"{qid}: bad answer idx"
    assert difficulty in DIFFS, f"{qid}: bad difficulty"
    assert isinstance(timeSec, int) and 10 <= timeSec <= 180, f"{qid}: bad timeSec"
    assert isinstance(solution, str) and solution.strip(), f"{qid}: empty solution"
    assert shortcut is None or (isinstance(shortcut, str) and shortcut.strip())
    assert KEBAB.match(subtopic), f"{qid}: bad subtopic id {subtopic}"
    for o in options:
        assert isinstance(o, str) and o.strip(), f"{qid}: empty option"
    assert isinstance(q, str) and q.strip()
    if qid in _seen_ids:
        raise AssertionError(f"duplicate id {qid} (also in {_seen_ids[qid]})")
    _seen_ids[qid] = "this session"
    return {"id": qid, "q": q, "figure": figure_default(), "options": options,
            "answer": answer, "solution": solution, "shortcut": shortcut,
            "difficulty": difficulty, "subtopic": subtopic, "pattern": pattern,
            "timeSec": timeSec}

def figure_default():
    return None

def validate_and_dump_topic(topic):
    assert set(topic) == {"id", "sectionId", "title", "order", "importance",
                          "avgQuestions", "summary", "subtopics", "pyqPatterns",
                          "solvedExamples", "practice"}, f"key mismatch in {topic.get('id')}: {sorted(topic)}"
    assert topic["id"] in TOPIC_IDS and topic["sectionId"] == "computer"
    assert topic["importance"] in {"high", "medium", "low"}
    assert isinstance(topic["order"], int)
    assert set(topic["avgQuestions"]) == {"tier1", "tier2"}
    sub_ids = []
    for s in topic["subtopics"]:
        assert set(s) == {"id", "title", "concept", "formulas", "tricks", "mistakes"}
        assert KEBAB.match(s["id"]), s["id"]
        sub_ids.append(s["id"])
        assert isinstance(s["concept"], str) and len(s["concept"]) > 100
        assert isinstance(s["formulas"], list)
        for f in s["formulas"]:
            assert set(f) == {"name", "tex", "note"}
        for t in s["tricks"]:
            assert set(t) == {"title", "body", "example"}
            assert "q" in t["example"] and "solution" in t["example"]
        assert isinstance(s["mistakes"], list) and s["mistakes"]
    assert len(sub_ids) == len(set(sub_ids))
    for p in topic["pyqPatterns"]:
        assert set(p) == {"pattern", "frequency", "howToSpot", "approach"}
        assert p["frequency"] in {"very common", "common", "occasional"}
    assert 3 <= len(topic["solvedExamples"]) <= 5, topic["id"]
    assert 12 <= len(topic["practice"]) <= 15, f"{topic['id']}: {len(topic['practice'])} practice"
    for grp in ("solvedExamples", "practice"):
        for q in topic[grp]:
            assert q["subtopic"] in sub_ids, f"{q['id']}: subtopic {q['subtopic']} not in {sub_ids}"
    path = os.path.join(OUT_TOPIC, topic["id"] + ".json")
    _dump(topic, path)
    return path

def _dump(obj, path):
    os.makedirs(os.path.dirname(path), exist_ok=True)
    with open(path, "w", encoding="utf-8") as fh:
        json.dump(obj, fh, ensure_ascii=False, indent=1)
    with open(path, encoding="utf-8") as fh:   # re-parse to prove valid JSON
        json.load(fh)
    print("OK wrote", path, os.path.getsize(path), "bytes")
