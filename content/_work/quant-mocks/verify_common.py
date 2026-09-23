"""Shared question builder + validator for the quant mock parts files."""
import json
import os

TOPICS = {
    "number-system", "simplification", "hcf-lcm", "percentage", "ratio-proportion",
    "average", "interest", "profit-loss-discount", "mixture-alligation", "time-work",
    "time-speed-distance", "algebra", "geometry", "mensuration-2d", "mensuration-3d",
    "trigonometry", "heights-distances", "statistics", "data-interpretation",
}
DIFFS = {"easy", "medium", "hard"}
PARTS = r"C:\Users\Vinay Singirikonda\Desktop\examshortcut\content\ssc-cgl\mocks\parts"


def Q(qid, q, options, answer, solution, shortcut, difficulty, subtopic, pattern, timeSec):
    assert len(options) == 4, qid + ": need 4 options"
    assert len(set(str(o) for o in options)) == 4, qid + ": duplicate options"
    assert isinstance(answer, int) and 0 <= answer <= 3, qid + ": bad answer index"
    assert difficulty in DIFFS, qid + ": bad difficulty"
    assert subtopic in TOPICS, qid + ": bad subtopic " + str(subtopic)
    assert isinstance(timeSec, int) and timeSec > 0, qid + ": bad timeSec"
    assert q and q.strip(), qid + ": empty q"
    assert solution and solution.strip(), qid + ": empty solution"
    assert shortcut is None or str(shortcut).strip(), qid + ": empty shortcut"
    return {
        "id": qid,
        "q": q,
        "figure": None,
        "options": [str(o) for o in options],
        "answer": answer,
        "solution": solution,
        "shortcut": shortcut,
        "difficulty": difficulty,
        "subtopic": subtopic,
        "pattern": pattern,
        "timeSec": timeSec,
    }


def finalize(mock_id, questions, expected_count):
    ids = [x["id"] for x in questions]
    assert len(ids) == len(set(ids)), "duplicate ids"
    assert len(questions) == expected_count, "expected %d questions, got %d" % (expected_count, len(questions))
    # Balance the position of the correct option across 0..3 (deterministic, order-safe:
    # rotating the options list cannot create duplicates or change which string is correct).
    for i, x in enumerate(questions):
        target = i % 4
        cur = x["answer"]
        correct = x["options"][cur]
        shift = (cur - target) % 4
        if shift:
            o = x["options"]
            x["options"] = o[shift:] + o[:shift]
            x["answer"] = target
        assert x["options"][x["answer"]] == correct, x["id"]
    from collections import Counter
    diff = Counter(x["difficulty"] for x in questions)
    topics = Counter(x["subtopic"] for x in questions)
    anspos = Counter(x["answer"] for x in questions)
    doc = {"mockId": mock_id, "sectionId": "quant", "questions": questions}
    out = os.path.join(PARTS, "%s--quant.json" % mock_id)
    os.makedirs(os.path.dirname(out), exist_ok=True)
    with open(out, "w", encoding="utf-8") as f:
        json.dump(doc, f, ensure_ascii=False, indent=1)
    # round-trip parse check
    back = json.load(open(out, encoding="utf-8"))
    assert len(back["questions"]) == expected_count
    for x in back["questions"]:
        assert len(x["options"]) == 4 and 0 <= x["answer"] <= 3
    print("WROTE %s  n=%d  diff=%s" % (out, len(questions), dict(diff)))
    print("  topics:", dict(topics))
