# -*- coding: utf-8 -*-
"""Brute-force seating solver used by seating-arrangement.py.

Row:    seats 1..n numbered west -> east (a north-facing person's left end is seat 1).
        face[x] = +1 (north) or -1 (south).  'b is k-th to the right of a'  ->  pos[b] = pos[a] + k*face[a].
Circle: seats 0..n-1 numbered clockwise seen from above.
        face[x] = +1 (towards centre: left = clockwise) or -1 (outward: left = anticlockwise).
        'b is k-th to the left of a'  ->  pos[b] = pos[a] + k*face[a]  (mod n).
Rows2:  two parallel rows of m seats, row 0 faces south, row 1 faces north; seat i of row 0
        faces seat i of row 1. pos[x] = (row, i), i = 1..m west -> east.
"""
from itertools import permutations


class V:
    """A candidate arrangement with helper predicates."""

    def __init__(self, kind, n, pos, face, attr=None):
        self.kind, self.n, self.p, self.face, self.a = kind, n, pos, face, attr or {}

    # ---- generic ----
    def at(self, x, i):
        return self.p[x] == i

    def who(self, i):
        for k, v in self.p.items():
            if v == i:
                return k
        return None

    def has(self, attr):
        for k, v in self.a.items():
            if v == attr:
                return k
        raise KeyError(attr)

    def _step(self, x, k):
        """seat k places to x's LEFT (k may be negative = right)."""
        if self.kind == "row":
            return self.p[x] - k * self.face[x]
        if self.kind == "circle":
            return (self.p[x] + k * self.face[x]) % self.n
        r, i = self.p[x]
        f = -1 if r == 0 else 1        # row 0 faces south, row 1 faces north
        return (r, i - k * f)

    def L(self, x, y, k=1):
        """y is k-th to the left of x."""
        return self.p[y] == self._step(x, k)

    def R(self, x, y, k=1):
        """y is k-th to the right of x."""
        return self.p[y] == self._step(x, -k)

    def left_of(self, x, k=1):
        return self.who(self._step(x, k))

    def right_of(self, x, k=1):
        return self.who(self._step(x, -k))

    def adj(self, x, y):
        if self.kind == "row":
            return abs(self.p[x] - self.p[y]) == 1
        if self.kind == "circle":
            return (self.p[x] - self.p[y]) % self.n in (1, self.n - 1)
        (r1, i1), (r2, i2) = self.p[x], self.p[y]
        return r1 == r2 and abs(i1 - i2) == 1

    def end(self, x):
        if self.kind == "row":
            return self.p[x] in (1, self.n)
        return self.p[x][1] in (1, self.n)

    def opp(self, x, y):
        if self.kind == "circle":
            return (self.p[x] - self.p[y]) % self.n == self.n // 2
        (r1, i1), (r2, i2) = self.p[x], self.p[y]
        return r1 != r2 and i1 == i2

    def opp_of(self, x):
        if self.kind == "circle":
            return self.who((self.p[x] + self.n // 2) % self.n)
        r, i = self.p[x]
        return self.who((1 - r, i))

    def gap(self, x, y):
        """people strictly between x and y in a row."""
        return abs(self.p[x] - self.p[y]) - 1

    def between(self, x, y, z):
        """y sits immediately between x and z."""
        return self.adj(x, y) and self.adj(y, z) and x != z

    def mid(self, x, y, z):
        """y sits exactly midway between x and z (row)."""
        return 2 * self.p[y] == self.p[x] + self.p[z]


def solve(kind, people, n=None, face=None, clues=(), rows0=None, attrs=None, fix_first=True):
    """Return every arrangement (as V) satisfying all clues.
    kind: 'row' | 'circle' | 'rows2'.  face: dict or +1/-1 for everyone.
    rows2: rows0 = people in row 0 (south-facing); the rest are in row 1.
    attrs: optional list of attribute values to permute over people."""
    people = list(people)
    n = n or len(people)
    if not isinstance(face, dict):
        face = {x: (face if face is not None else 1) for x in people}
    sols = []
    if kind == "rows2":
        r0 = list(rows0)
        r1 = [x for x in people if x not in r0]
        m = len(r0)
        seat_sets = []
        for p0 in permutations(range(1, m + 1)):
            for p1 in permutations(range(1, m + 1)):
                pos = {x: (0, i) for x, i in zip(r0, p0)}
                pos.update({x: (1, i) for x, i in zip(r1, p1)})
                seat_sets.append(pos)
        n = m
    elif kind == "circle":
        seat_sets = []
        rest = people[1:] if fix_first else people
        seats = list(range(1, n)) if fix_first else list(range(n))
        for perm in permutations(seats, len(rest)):
            pos = {people[0]: 0} if fix_first else {}
            pos.update(dict(zip(rest, perm)))
            seat_sets.append(pos)
    else:
        seat_sets = [dict(zip(people, perm)) for perm in permutations(range(1, n + 1), len(people))]
    attr_sets = [None]
    if attrs:
        attr_sets = [dict(zip(people, ap)) for ap in permutations(attrs)]
    for pos in seat_sets:
        for at in attr_sets:
            v = V(kind, n, pos, face, at)
            if all(c(v) for c in clues):
                sols.append(v)
    return sols


def show(v):
    if v.kind == "rows2":
        m = v.n
        r0 = " ".join(v.who((0, i)) or "_" for i in range(1, m + 1))
        r1 = " ".join(v.who((1, i)) or "_" for i in range(1, m + 1))
        s = f"row0(S): {r0} | row1(N): {r1}"
    elif v.kind == "circle":
        s = "clockwise: " + " ".join(v.who(i) or "_" for i in range(v.n))
    else:
        s = "W->E: " + " ".join(v.who(i) or "_" for i in range(1, v.n + 1))
    if v.a:
        s += "  attrs: " + ", ".join(f"{k}={x}" for k, x in sorted(v.a.items()))
    return s
