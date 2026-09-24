"""Verification helpers for classification (odd-one-out) questions."""
import os
import sys

sys.path.insert(0, os.path.dirname(__file__))
from _lib import pos, steps  # noqa: E402

VOWELS = set("AEIOU")


def isprime(n):
    if n < 2:
        return False
    i = 2
    while i * i <= n:
        if n % i == 0:
            return False
        i += 1
    return True


def issq(n):
    r = int(round(n ** 0.5))
    return r * r == n


def iscube(n):
    r = int(round(n ** (1 / 3)))
    return any((r + e) ** 3 == n for e in (-1, 0, 1))


def dsum(n):
    return sum(int(c) for c in str(n))


def dprod(n):
    p = 1
    for c in str(n):
        p *= int(c)
    return p


def odd_by(items, rule):
    """Items for which rule is False."""
    return [x for x in items if not rule(x)]


def one_breaks(items, rule, ans):
    bad = odd_by(items, rule)
    assert bad == [ans], f"rule breakers {bad} != [{ans}] for {items}"
    return ans


def only_fits(items, rule, ans):
    good = [x for x in items if rule(x)]
    assert good == [ans], f"rule fitters {good} != [{ans}] for {items}"
    return ans


def _three_one(items, f):
    """If f splits items 3+1, return the lone item, else None."""
    vals = [f(x) for x in items]
    for v in set(vals):
        if vals.count(v) == 3:
            return items[[i for i, w in enumerate(vals) if w != v][0]]
    return None


def alt_num(items, ans):
    """No other obvious number property may single out a DIFFERENT item.
    Positive properties (multiple of k, square, cube, same digit sum ...) count only when
    three items SHARE them; prime/parity count both ways."""
    probs = []
    both = {"prime": isprime, "even": lambda n: n % 2 == 0}
    for name, f in both.items():
        lone = _three_one(items, f)
        if lone is not None and lone != ans:
            probs.append((name, lone))
    positive = {f"mult{k}": (lambda k: lambda n: n % k == 0)(k) for k in range(3, 20)}
    positive.update({"square": issq, "cube": iscube})
    for name, f in positive.items():
        vals = [f(x) for x in items]
        if vals.count(True) == 3:
            lone = items[vals.index(False)]
            if lone != ans:
                probs.append((name, lone))
    for name, f in {"dsum": dsum, "dprod": dprod, "ndig": lambda n: len(str(n))}.items():
        lone = _three_one(items, f)
        if lone is not None and lone != ans:
            probs.append((name, lone))
    assert not probs, f"alternative rules point elsewhere for {items} (ans {ans}): {probs}"


def alt_letters(items, ans):
    """Step tuples / vowel counts must not single out a different cluster."""
    for name, f in {"steps": lambda w: tuple(steps(w)),
                    "vowels": lambda w: sum(c in VOWELS for c in w),
                    "psum": lambda w: sum(pos(c) for c in w)}.items():
        lone = _three_one(items, f)
        assert lone is None or lone == ans, f"{name} singles out {lone} not {ans} in {items}"
