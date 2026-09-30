"""Shared helpers for the GA Ancient History rewrite (ancient_history.py)."""


def pat(pid, name, freq, spot, steps, why, q, ex_steps, answer):
    return {"id": pid, "name": name, "frequency": freq, "howToSpot": spot, "formula": None,
            "steps": steps, "why": why, "example": {"q": q, "steps": ex_steps, "answer": answer}}


def trick(title, body, q=None, steps=None, answer=None):
    t = {"title": title, "body": body}
    if q:
        t["example"] = {"q": q, "steps": steps, "answer": answer}
    return t


def mk(wrong, right):
    return {"wrong": wrong, "right": right}
