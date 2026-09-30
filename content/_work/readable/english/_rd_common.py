"""Shared helpers for the English readable rewrites (vocabulary topics)."""
import json
import re
import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parents[3]


def pat(pid, name, freq, spot, steps, why, q, ex_steps, answer, formula=None):
    return {"id": pid, "name": name, "frequency": freq, "howToSpot": spot, "formula": formula,
            "steps": steps, "why": why, "example": {"q": q, "steps": ex_steps, "answer": answer}}


def mis(wrong, right):
    return {"wrong": wrong, "right": right}


def trick(title, body, q=None, steps=None, answer=None):
    t = {"title": title, "body": body}
    if q:
        t["example"] = {"q": q, "steps": steps, "answer": answer}
    return t


def sub(concept, notes, patterns, mistakes, revision, tricks):
    return dict(concept=concept, notes=notes, patterns=patterns, mistakes=mistakes, revision=revision, tricks=tricks)


def long_lines(text, limit=22):
    plain = re.sub(r"\$\$.*?\$\$|\$[^$]*\$", "X", text, flags=re.S)
    plain = re.sub(r"^\s*(?:[-*>|]|\d+[.)])\s*", "", plain, flags=re.M)
    return [s for s in re.split(r"(?<=[.!?])\s+|\n", plain) if len(s.split()) > limit]


def apply(topic_name, SUBS):
    path = ROOT / "core" / "topics" / "english" / f"{topic_name}.json"
    data = json.loads(path.read_text(encoding="utf-8"))
    assert set(SUBS) == {s["id"] for s in data["subtopics"]}, "every subtopic must be rewritten"
    for s in data["subtopics"]:
        new = SUBS[s["id"]]
        old_ids = {p["id"] for p in s.get("patterns", [])}
        new_ids = [p["id"] for p in new["patterns"]]
        assert old_ids <= set(new_ids), (s["id"], old_ids - set(new_ids))
        assert len(new_ids) == len(set(new_ids)), s["id"]
        n = new["notes"].strip() + "\n"
        print(s["id"], "notes", len(n), "sections", len(re.findall(r"^### ", n, re.M)), "patterns", len(new_ids))
        if not 2500 <= len(n) <= 5000:
            print("  LENGTH OUT OF RANGE")
        for p in new["patterns"]:
            assert 3 <= len(p["steps"]) <= 5 and 2 <= len(p["example"]["steps"]) <= 5, p["id"]
        for ln in long_lines(n + "\n" + new["concept"]):
            print("  long:", ln[:90])
        s.update(concept=new["concept"], notes=n, tricks=new["tricks"], mistakes=new["mistakes"],
                 revision=new["revision"], patterns=new["patterns"])
    ids = [p["id"] for s in data["subtopics"] for p in s["patterns"]]
    assert len(ids) == len(set(ids)), "pattern id clash"
    path.write_text(json.dumps(data, ensure_ascii=False, indent=1) + "\n", encoding="utf-8", newline="\n")
    print("written", path.name)
