"""Helpers used only by the coding-decoding build scripts. Loaded with cdh() below."""
import os
import sys

sys.path.insert(0, os.path.dirname(__file__))
from _lib import *  # noqa


def tup(a, b):
    """'C→E (+2), U→W (+2)' style explanation of the slot-wise shift from a to b."""
    return ", ".join(f"{x}→{y} ({sgn(d)})" for x, y, d in zip(a, b, diffs(a, b)))


def posl(word):
    """'C(3) A(1) T(20)'"""
    return " ".join(f"{c}({pos(c)})" for c in word)


def rposl(word):
    return " ".join(f"{c}({rpos(c)})" for c in word)


def opps(word):
    return ", ".join(f"{c}↔{let(27 - pos(c))}" for c in word)


def solve_sets(items, codes):
    """items: list of lists of words (or letters); codes: list of lists of code tokens.
    Word->code is a bijection that maps each sentence's word-set onto its code-set.
    Returns (candidates dict, list of all consistent full mappings)."""
    words = sorted({w for s in items for w in s})
    toks = sorted({c for s in codes for c in s})
    assert len(words) == len(toks), (words, toks)
    for s, c in zip(items, codes):
        assert len(set(s)) == len(s) == len(c) == len(set(c)), (s, c)
    cand = {}
    for w in words:
        cand[w] = [c for c in toks
                   if all((w in s) == (c in cs) for s, cs in zip(items, codes))]
    sols = []

    def bt(i, used, cur):
        if i == len(words):
            sols.append(dict(cur))
            return
        w = words[i]
        for c in cand[w]:
            if c not in used:
                cur[w] = c
                used.add(c)
                bt(i + 1, used, cur)
                used.discard(c)
                del cur[w]

    bt(0, set(), {})
    assert sols, "no consistent mapping"
    return cand, sols


def possible(items, codes, w):
    _, sols = solve_sets(items, codes)
    return {m[w] for m in sols}


def fixed(items, codes, w):
    p = possible(items, codes, w)
    assert len(p) == 1, (w, p)
    return next(iter(p))
