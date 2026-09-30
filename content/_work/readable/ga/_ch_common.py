"""Shared helpers for the chemistry readable rewrite."""


def pat(pid, name, freq, spot, steps, why, q, ex_steps, answer, formula=None):
    return {"id": pid, "name": name, "frequency": freq, "howToSpot": spot, "formula": formula,
            "steps": steps, "why": why, "example": {"q": q, "steps": ex_steps, "answer": answer}}


def mis(wrong, right):
    return {"wrong": wrong, "right": right}


def trick(title, body, q=None, steps=None, answer=None):
    ex = None
    if q:
        ex = {"q": q, "steps": steps, "answer": answer}
    return {"title": title, "body": body, "example": ex}
