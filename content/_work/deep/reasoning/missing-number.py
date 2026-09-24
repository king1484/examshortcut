"""Missing-number topic build: notes + patterns + practice + pyqPatterns.

Every grid is GENERATED from its rule in code (the third cells are computed,
never typed), and an ambiguity guard runs a library of ~60 common exam rules
over the complete rows: every library rule that reproduces all complete rows
must predict the same answer, otherwise the question is rejected.
"""
import os
import sys

sys.path.insert(0, os.path.dirname(__file__))
from _lib import *  # noqa
from missing_number_notes import NOTES, PATTERNS, PYQS

d = load("missing-number")

for sid, notes in NOTES.items():
    set_sub(d, sid, notes=notes, patterns=PATTERNS[sid])


# ------------------------------------------------- digit helpers
def S(n):
    return sum(int(c) for c in str(n))


def R(n):
    return int(str(n)[::-1])


def Pd(n):
    out = 1
    for c in str(n):
        out *= int(c)
    return out


assert S(47) == 11 and R(43) == 34 and Pd(47) == 28
assert S(29) + S(14) + 2 == 18 and S(38) + S(25) + 2 == 20  # existing q5 rule
assert R(43 + 14) == 75 and R(34 + 43) == 77                 # existing q11 rule


# ------------------------------------------------- candidate rule library
def lib2(a, b):
    c = {
        "a+b": a + b, "|a-b|": abs(a - b), "a*b": a * b,
        "(a+b)*2": (a + b) * 2, "(a+b)*3": (a + b) * 3,
        "a*(b-1)": a * (b - 1), "b*(a-1)": b * (a - 1),
        "a^2+b": a * a + b, "a^2-b": a * a - b, "b^2+a": b * b + a, "b^2-a": b * b - a,
        "a^2+b^2": a * a + b * b, "|a^2-b^2|": abs(a * a - b * b),
        "(a+b)^2": (a + b) ** 2, "(a-b)^2": (a - b) ** 2,
        "ab-(a+b)": a * b - a - b, "ab+a+b": a * b + a + b,
        "2a+b": 2 * a + b, "a+2b": a + 2 * b, "3a-b": 3 * a - b, "3b-a": 3 * b - a,
        "2ab": 2 * a * b, "2ab-1": 2 * a * b - 1, "2ab+1": 2 * a * b + 1,
        "S(a)+S(b)": S(a) + S(b), "S(a+b)": S(a + b), "S(a)*S(b)": S(a) * S(b),
        "R(a)+R(b)": R(a) + R(b), "R(a+b)": R(a + b), "|R(a)-b|": abs(R(a) - b),
        "P(a)+P(b)": Pd(a) + Pd(b), "S(a)*b": S(a) * b, "2S(a)+b": 2 * S(a) + b,
        "S(a)+b": S(a) + b, "a-b": a - b, "b-a": b - a,
    }
    for k in range(-3, 4):
        if k:
            c[f"ab{k:+d}"] = a * b + k
            c[f"a+b{k:+d}"] = a + b + k
            c[f"S(a)+S(b){k:+d}"] = S(a) + S(b) + k
    if (a + b) % 2 == 0:
        c["(a+b)/2"] = (a + b) // 2
    if b and a % b == 0:
        c["a/b"] = a // b
    return c


def lib1(a):
    c = {f"{k}a": k * a for k in range(1, 11)}
    c.update({"a^2": a * a, "a^2+1": a * a + 1, "a^2-1": a * a - 1, "a^2+a": a * a + a,
              "a^2-a": a * a - a, "a^3": a ** 3, "2a+1": 2 * a + 1, "2a-1": 2 * a - 1,
              "3a+1": 3 * a + 1, "S(a)": S(a), "P(a)": Pd(a), "R(a)": R(a),
              "a^2+2": a * a + 2, "a^2-2": a * a - 2, "2a^2": 2 * a * a})
    return c


def guard2(rows, q_in, ans):
    """rows: complete (a, b, c) rows; q_in: (a, b) of the incomplete row."""
    fits = [k for k in lib2(*rows[0][:2])
            if all(lib2(a, b).get(k) == c for a, b, c in rows)]
    preds = {k: lib2(*q_in).get(k) for k in fits}
    bad = {k: v for k, v in preds.items() if v != ans}
    assert not bad, f"ambiguous: {bad} vs answer {ans}"
    return fits


def guard1(rows, q_in, ans):
    fits = [k for k in lib1(rows[0][0]) if all(lib1(a).get(k) == c for a, c in rows)]
    bad = {k: lib1(q_in)[k] for k in fits if lib1(q_in)[k] != ans}
    assert not bad, f"ambiguous: {bad} vs answer {ans}"
    return fits


def grid_text(rows, lead="Find the missing number:"):
    lines = ["**" + "   ".join(str(x) for x in r) + "**" for r in rows]
    return lead + "\n\n" + "\n\n".join(lines)


def make2(rule, inputs, q_in, rule_name):
    """Build complete rows from a rule; run the ambiguity guard; return (rows, ans)."""
    rows = [(a, b, rule(a, b)) for a, b in inputs]
    ans = rule(*q_in)
    fits = guard2(rows, q_in, ans)
    assert rule_name in fits, (rule_name, fits)
    return rows, ans


NQ = []
_ctr = {}


def A(sub, pat, q, ans, wrong, solution, diff="medium", shortcut=None, t=45):
    _ctr[sub] = _ctr.get(sub, 0) + 1
    NQ.append(Q(f"{sub}-p{_ctr[sub]:02d}", q, ans, wrong, solution, shortcut=shortcut,
                diff=diff, sub=sub, pat=pat, t=t))


def row_q(rows, q_in):
    return grid_text([r for r in rows] + [(q_in[0], q_in[1], "?")])


# ================= missing-number-idea =================
IDEA = "missing-number-idea"

# p01  c = 4a (one-input pairs)
pairs = [(3, 12), (7, 28)]
assert guard1(pairs, 9, 36)
A(IDEA, "mn-p1", grid_text([(3, 12), (7, 28), (9, "?")]),
  36, [27, 32, 40],
  "Second number = 4 × first: 3 × 4 = 12 ✓, 7 × 4 = 28 ✓. So 9 × 4 = **36**. (27 uses ×3, which fits neither row.)",
  diff="easy", shortcut="Divide the output by the input — a constant quotient means a constant multiplier.", t=25)

# p02  c = 2a + b
rows, ans = make2(lambda a, b: 2 * a + b, [(3, 4), (5, 2)], (6, 5), "2a+b")
assert ans == 17
A(IDEA, "mn-p1", row_q(rows, (6, 5)),
  ans, [11, 16, 30],
  "a + b gives 7 and 7, not 10 and 12 — the first number counts twice. Rule: third = 2 × first + second: 6 + 4 = 10 ✓, 10 + 2 = 12 ✓. So 12 + 5 = **17**. (16 doubles the wrong number.)",
  diff="easy", shortcut="Output just above a + b by exactly one input → that input is doubled.", t=35)

# p03  c = 3a − b
rows, ans = make2(lambda a, b: 3 * a - b, [(5, 4), (6, 2)], (8, 3), "3a-b")
assert ans == 21
A(IDEA, "mn-p1", row_q(rows, (8, 3)),
  ans, [11, 5, 24],
  "Sum and product both fail (9, 20 against 11). Rule: third = 3 × first − second: 15 − 4 = 11 ✓, 18 − 2 = 16 ✓. So 24 − 3 = **21**. (24 forgets to subtract the second number.)",
  diff="medium", shortcut="Output between a and 3a → try ka ± b.")

# p04  c = a² + 1
pairs = [(3, 10), (6, 37)]
assert guard1(pairs, 8, 65)
A(IDEA, "mn-p2", grid_text([(3, 10), (6, 37), (8, "?")]),
  65, [64, 63, 72],
  "10 = 3² + 1 and 37 = 6² + 1. So 8² + 1 = **65**. (64 is the bare square — the near-miss.)",
  diff="easy", shortcut="Outputs one above a perfect square → a² + 1.", t=30)

# p05  c = b² + a
rows, ans = make2(lambda a, b: b * b + a, [(3, 4), (5, 2)], (6, 5), "b^2+a")
assert ans == 31
A(IDEA, "mn-p2", row_q(rows, (6, 5)),
  ans, [41, 30, 61],
  "19 = 4² + 3 and 9 = 2² + 5 — the SECOND number is squared. Rule: third = second² + first. So 5² + 6 = **31**. (41 squares the wrong number: 6² + 5.)",
  diff="medium", shortcut="Try squaring each input in turn; only one choice fits both rows.")

# p06  c = (a + b)²
rows, ans = make2(lambda a, b: (a + b) ** 2, [(2, 3), (4, 2)], (3, 5), "(a+b)^2")
assert ans == 64
A(IDEA, "mn-p2", row_q(rows, (3, 5)),
  ans, [34, 15, 49],
  "25 and 36 are perfect squares: 25 = (2 + 3)², 36 = (4 + 2)². Rule: third = (first + second)². So (3 + 5)² = **64**. (34 = 3² + 5² squares separately.)",
  diff="hard", shortcut="Every output a perfect square → find what is being squared.")

# p07  two grids: c = ab + 1
g = [(3, 5), (4, 6)]
rows, ans = make2(lambda a, b: a * b + 1, g, (5, 7), "ab+1")
assert ans == 36
A(IDEA, "mn-p3",
  "Study the pattern and find the missing number.\n\n**Grid 1:** 3, 5, 16  **Grid 2:** 4, 6, 25  **Grid 3:** 5, 7, ?\n\n(Each grid is read left to right as one row.)",
  ans, [35, 12, 37],
  "Grid 1: 3 × 5 + 1 = 16; grid 2 confirms: 4 × 6 + 1 = 25 ✓. Grid 3: 5 × 7 + 1 = **36**. (35 is the bare product.)",
  diff="easy", shortcut="Solve grid 1, confirm on grid 2, apply to grid 3.", t=35)
assert rows == [(3, 5, 16), (4, 6, 25)]

# p08  two grids: c = ab − a
rows, ans = make2(lambda a, b: a * b - a, [(6, 4), (5, 7)], (8, 3), "a*(b-1)")
assert rows == [(6, 4, 18), (5, 7, 30)] and ans == 16
A(IDEA, "mn-p3",
  "Study the pattern and find the missing number.\n\n**Grid 1:** 6, 4, 18  **Grid 2:** 5, 7, 30  **Grid 3:** 8, 3, ?\n\n(Each grid is read left to right as one row.)",
  ans, [24, 21, 11],
  "Products 24 and 35 overshoot by exactly the first number (6 and 5). Rule: third = first × (second − 1): 6 × 3 = 18 ✓, 5 × 6 = 30 ✓. So 8 × 2 = **16**. (21 = 3 × 7 reduces the wrong factor.)",
  diff="medium", shortcut="Product too big by one input → that input's partner carries a −1.")

# p09  two grids: constant row sum 25
grids = [(8, 9, 8), (12, 6, 7)]
assert all(sum(r) == 25 for r in grids)
assert 25 - 10 - 4 == 11
A(IDEA, "mn-p3",
  "Study the pattern and find the missing number.\n\n**Grid 1:** 8, 9, 8  **Grid 2:** 12, 6, 7  **Grid 3:** 10, 4, ?\n\n(Each grid is read left to right as one row.)",
  11, [14, 6, 10],
  "No clean a-to-c bridge exists, so total the rows: 8 + 9 + 8 = 25 and 12 + 6 + 7 = 25. Every grid sums to 25 → 10 + 4 + ? = 25 → ? = **11**.",
  diff="medium", shortcut="When bridges fail, add each complete row — equal totals mean a constant-sum rule.")

# p10  verify: a + b fits row 1 only; true rule ab − 2
rows, ans = make2(lambda a, b: a * b - 2, [(2, 4), (5, 3)], (6, 4), "ab-2")
assert rows[0][0] + rows[0][1] == rows[0][2]      # the planted coincidence
assert rows[1][0] + rows[1][1] != rows[1][2]
assert ans == 22
A(IDEA, "mn-p4", row_q(rows, (6, 4)),
  ans, [10, 24, 20],
  "Row 1 tempts with 2 + 4 = 6, but row 2 gives 5 + 3 = 8 ≠ 13 — the sum rule dies. Product − 2 fits both: 8 − 2 = 6 ✓, 15 − 2 = 13 ✓. So 24 − 2 = **22**. (10 is the sum rule that only fitted row 1.)",
  diff="medium", shortcut="A rule that fits one row is a coincidence until the second row agrees.")

# p11  verify: ab fits row 1 only; true rule a² + b
rows, ans = make2(lambda a, b: a * a + b, [(2, 4), (5, 3)], (6, 2), "a^2+b")
assert rows[0][0] * rows[0][1] == rows[0][2]      # planted coincidence
assert rows[1][0] * rows[1][1] != rows[1][2]
assert ans == 38
A(IDEA, "mn-p4", row_q(rows, (6, 2)),
  ans, [12, 40, 34],
  "Row 1 looks like a product (2 × 4 = 8), but row 2 breaks it (5 × 3 = 15 ≠ 28). Rule: first² + second: 4 + 4 = 8 ✓, 25 + 3 = 28 ✓. So 36 + 2 = **38**. (12 is the product rule; 34 subtracts instead of adding.)",
  diff="hard", shortcut="Test the second row before trusting the first.", t=55)

# p12  verify: one-input, multiplier changes → a² − a
pairs = [(4, 12), (7, 42)]
assert guard1(pairs, 9, 72)
A(IDEA, "mn-p4", grid_text([(4, 12), (7, 42), (9, "?")]),
  72, [81, 36, 90],
  "The multipliers differ (×3, then ×6), so no constant multiple fits. 12 = 4² − 4 and 42 = 7² − 7 ✓. So 9² − 9 = **72**. (81 is the bare square; 36 = 9 × 4 copies row 1's ×3 idea.)",
  diff="medium", shortcut="Changing multiplier equal to (a − 1) → a × (a − 1) = a² − a.")

# ================= grid-row-rules =================
GR = "grid-row-rules"

# p01 c = a − b
rows, ans = make2(lambda a, b: a - b, [(15, 7), (20, 9)], (18, 5), "|a-b|")
assert ans == 13
A(GR, "gr-p1", row_q(rows, (18, 5)),
  ans, [23, 12, 14],
  "Third = first − second: 15 − 7 = 8 ✓, 20 − 9 = 11 ✓. So 18 − 5 = **13**. (23 adds instead.)",
  diff="easy", shortcut="Output smaller than the first input → subtraction.", t=30)

# p02 c = a + b − 3
rows, ans = make2(lambda a, b: a + b - 3, [(8, 6), (9, 7)], (6, 5), "a+b-3")
assert ans == 8
A(GR, "gr-p1", row_q(rows, (6, 5)),
  ans, [11, 1, 9],
  "Sums are 14 and 16; the outputs are 11 and 13 — always 3 less. Rule: third = first + second − 3. So 11 − 3 = **8**. (11 is the bare sum; 1 is the difference.)",
  diff="medium", shortcut="Constant gap between output and a + b → a + b ± k.")

# p03 c = 2ab
rows, ans = make2(lambda a, b: 2 * a * b, [(3, 4), (5, 2)], (4, 6), "2ab")
assert ans == 48
A(GR, "gr-p2", row_q(rows, (4, 6)),
  ans, [24, 10, 49],
  "Products are 12 and 10; outputs are exactly double. Rule: third = 2 × first × second. So 2 × 24 = **48**. (24 is the undoubled product.)",
  diff="medium", shortcut="Output ÷ product constant → k × ab.")

# p04 c = a² + b²
rows, ans = make2(lambda a, b: a * a + b * b, [(1, 2), (2, 5)], (3, 6), "a^2+b^2")
assert ans == 45
A(GR, "gr-p2", row_q(rows, (3, 6)),
  ans, [81, 18, 36],
  "5 = 1² + 2² and 29 = 2² + 5² ✓. Rule: third = first² + second². So 9 + 36 = **45**. (81 = (3 + 6)² squares the sum instead.)",
  diff="hard", shortcut="Output neither sum nor product but beats both → sum of squares.", t=55)

# p05 column rule: middle column = average of outer columns
grid = [(6, 9, 12), (15, 20, 25), (8, None, 20)]
assert all(r[1] == (r[0] + r[2]) // 2 and (r[0] + r[2]) % 2 == 0 for r in grid[:2])
assert (8 + 20) // 2 == 14
A(GR, "gr-p3", grid_text([(6, 9, 12), (15, 20, 25), (8, "?", 20)]),
  14, [12, 28, 16],
  "The missing cell is in the middle, so read each row as (left, middle, right): 9 = (6 + 12) ÷ 2 ✓, 20 = (15 + 25) ÷ 2 ✓. Middle = average of the outer two → (8 + 20) ÷ 2 = **14**. (28 forgets to halve.)",
  diff="easy", shortcut="A middle cell sitting between its neighbours → average.", t=35)

# p06 column rule: row 3 = row 1 + row 2, cell by cell
top, mid = (4, 7, 3), (5, 2, 9)
bot = tuple(x + y for x, y in zip(top, mid))
assert bot == (9, 9, 12)
# no row rule links (a, b) -> c on the two complete rows
row_fits = [k for k in lib2(4, 7) if lib2(4, 7).get(k) == 3 and lib2(5, 2).get(k) == 9]
assert row_fits == [], row_fits
A(GR, "gr-p3", grid_text([top, mid, (9, 9, "?")]),
  12, [18, 9, 6],
  "Rows resist every bridge (4, 7 → 3 but 5, 2 → 9). Read down the columns instead: 4 + 5 = 9 ✓, 7 + 2 = 9 ✓ — the bottom row is the sum of the two above. So 3 + 9 = **12**. (18 = 9 + 9 is a row-wise guess.)",
  diff="medium", shortcut="Rows stuck → try columns: bottom = top ± middle, cell by cell.")

# p07 circle: opposite sectors sum to a constant
pairs = [(14, 9), (11, 12)]
assert len({a + b for a, b in pairs}) == 1 and pairs[0][0] + pairs[0][1] == 23
assert 23 - 16 == 7
A(GR, "gr-p4",
  "Numbers are written in the six sectors of a circle. Reading opposite sectors as pairs: **14 – 9**, **11 – 12**, **16 – ?**. Find the missing number.",
  7, [9, 25, 5],
  "Each opposite pair sums to the same total: 14 + 9 = 23, 11 + 12 = 23. So 16 + ? = 23 → ? = **7**. (9 copies a neighbour; 25 is 16 + 9.)",
  diff="medium", shortcut="Opposite sectors → constant sum (or product) first.", t=35)

# p08 triangle: centre = (first + second) × third corner
tri = [((2, 3, 4), 20), ((1, 5, 3), 18)]
rule = lambda x, y, z: (x + y) * z
assert all(rule(*c) == v for c, v in tri)
# plain alternatives must fail
assert not all(x * y * z == v for (x, y, z), v in tri)
assert not all(x + y + z == v for (x, y, z), v in tri)
assert not all(x * y + z == v for (x, y, z), v in tri)
assert rule(4, 2, 5) == 30
A(GR, "gr-p4",
  "In each triangle the corners are (left, right, top) and a number sits in the centre:\n\n**(2, 3, 4) → 20**\n\n**(1, 5, 3) → 18**\n\n**(4, 2, 5) → ?**",
  30, [40, 11, 28],
  "Product of corners fails (24 ≠ 20), sum fails (9). Rule: centre = (left + right) × top: (2 + 3) × 4 = 20 ✓, (1 + 5) × 3 = 18 ✓. So (4 + 2) × 5 = **30**. (40 is the product of all three corners.)",
  diff="hard", shortcut="Centre just below the corner product → try (x + y) × z.", t=55)

# ================= digit-operations =================
DO = "digit-operations"

# p01 S(a) + S(b)
rows, ans = make2(lambda a, b: S(a) + S(b), [(23, 41), (27, 45)], (35, 26), "S(a)+S(b)")
assert ans == 16
A(DO, "do-p1", row_q(rows, (35, 26)),
  ans, [61, 15, 7],
  "Outputs are far too small for sums of values → digit sums. S(23) + S(41) = 5 + 5 = 10 ✓; S(27) + S(45) = 9 + 9 = 18 ✓. So S(35) + S(26) = 8 + 8 = **16**. (61 is the plain sum.)",
  diff="easy", shortcut="Two-digit inputs, small outputs → add all the digits.", t=35)

# p02 S(a + b)
rows, ans = make2(lambda a, b: S(a + b), [(38, 27), (54, 18)], (46, 37), "S(a+b)")
assert ans == 11 and S(46) + S(37) == 20
A(DO, "do-p1", row_q(rows, (46, 37)),
  ans, [20, 83, 10],
  "Adding digit sums separately fails (11 + 9 = 20 ≠ 11). Add first, then sum the digits: 38 + 27 = 65 → 11 ✓; 54 + 18 = 72 → 9 ✓. So 46 + 37 = 83 → 8 + 3 = **11**. (20 is the separate digit-sum trap.)",
  diff="medium", shortcut="Carries make S(a+b) differ from S(a)+S(b) — test both.")

# p03 S(a) × S(b)
rows, ans = make2(lambda a, b: S(a) * S(b), [(12, 31), (22, 15)], (41, 23), "S(a)*S(b)")
assert ans == 25
A(DO, "do-p1", row_q(rows, (41, 23)),
  ans, [10, 64, 20],
  "S(12) = 3, S(31) = 4 → 3 × 4 = 12 ✓; S(22) = 4, S(15) = 6 → 24 ✓. Rule: product of digit sums. So S(41) × S(23) = 5 × 5 = **25**. (10 adds the digit sums.)",
  diff="hard", shortcut="Digit sums that multiply to the output → S(a) × S(b).", t=55)

# p04 R(a) + R(b)
rows, ans = make2(lambda a, b: R(a) + R(b), [(12, 23), (31, 14)], (21, 32), "R(a)+R(b)")
assert ans == 35 and 21 + 32 == 53
A(DO, "do-p2", row_q(rows, (21, 32)),
  ans, [53, 55, 45],
  "Reverse each input, then add: 21 + 32 = 53 ✓; 13 + 41 = 54 ✓. So 12 + 23 = **35**. (53 adds the unreversed inputs — which is exactly row 1's output, a planted trap.)",
  diff="easy", shortcut="Outputs look like sums of flipped numbers → reverse first.", t=35)

# p05 R(a + b)
rows, ans = make2(lambda a, b: R(a + b), [(25, 17), (38, 16)], (19, 33), "R(a+b)")
assert ans == 25 and 19 + 33 == 52
A(DO, "do-p2", row_q(rows, (19, 33)),
  ans, [52, 124, 26],
  "25 + 17 = 42 → reversed 24 ✓; 38 + 16 = 54 → reversed 45 ✓. Rule: reverse the sum. So 19 + 33 = 52 → **25**. (52 forgets to reverse; 124 reverses the inputs instead: 91 + 33.)",
  diff="medium", shortcut="Sum first, flip second.")

# p06 |R(a) − b|
rows, ans = make2(lambda a, b: abs(R(a) - b), [(52, 13), (71, 9)], (83, 20), "|R(a)-b|")
assert ans == 18 and 83 - 20 == 63
A(DO, "do-p2", row_q(rows, (83, 20)),
  ans, [63, 36, 58],
  "Plain difference fails (52 − 13 = 39). Reverse the first number, then subtract: 25 − 13 = 12 ✓; 17 − 9 = 8 ✓. So 38 − 20 = **18**. (63 = 83 − 20 skips the reversal; 36 reverses the difference instead.)",
  diff="hard", shortcut="Reverse only the two-digit input when the other is small.", t=55)

# p07 P(a) (one input)
pairs = [(24, 8), (36, 18)]
assert guard1(pairs, 57, 35)
A(DO, "do-p3", grid_text([(24, 8), (36, 18), (57, "?")]),
  35, [12, 75, 30],
  "8 = 2 × 4 and 18 = 3 × 6 — multiply the digits. So 5 × 7 = **35**. (12 adds the digits.)",
  diff="easy", shortcut="Output = digit product: check with the first pair.", t=30)

# p08 P(a) + P(b)
rows, ans = make2(lambda a, b: Pd(a) + Pd(b), [(23, 41), (32, 25)], (43, 62), "P(a)+P(b)")
assert ans == 24 and S(43) + S(62) == 15
A(DO, "do-p3", row_q(rows, (43, 62)),
  ans, [15, 105, 144],
  "Digit sums give 9, not 10, for row 1 — try digit products: 6 + 4 = 10 ✓; 6 + 10 = 16 ✓. So P(43) + P(62) = 12 + 12 = **24**. (15 adds digit sums; 144 multiplies the two products.)",
  diff="medium", shortcut="Digit sums miss by a little → switch to digit products.")

# p09 S(a) × b
rows, ans = make2(lambda a, b: S(a) * b, [(13, 5), (42, 3)], (51, 4), "S(a)*b")
assert ans == 24
A(DO, "do-p4", row_q(rows, (51, 4)),
  ans, [55, 204, 10],
  "S(13) × 5 = 4 × 5 = 20 ✓; S(42) × 3 = 6 × 3 = 18 ✓. Rule: digit sum of the first × second. So 6 × 4 = **24**. (204 multiplies the raw values; 10 adds instead of multiplying.)",
  diff="medium", shortcut="Small second input + two-digit first → shrink the first, keep the second.")

# p10 2S(a) + b
rows, ans = make2(lambda a, b: 2 * S(a) + b, [(25, 4), (31, 6)], (47, 3), "2S(a)+b")
assert ans == 25
A(DO, "do-p4", row_q(rows, (47, 3)),
  ans, [14, 22, 50],
  "S(25) = 7 → 2 × 7 + 4 = 18 ✓; S(31) = 4 → 2 × 4 + 6 = 14 ✓. Rule: twice the first number's digit sum plus the second. So 2 × 11 + 3 = **25**. (14 forgets to double; 22 forgets the + second.)",
  diff="hard", shortcut="Output − second number is even and small → 2 × digit sum.", t=55)

# ------------------------------------------------- verify PYQ / pattern examples
assert (9 - 1) * 5 == 40 and (6 - 1) * 3 == 15 and (8 - 1) * 4 == 28
assert S(56) + S(34) + 2 == 20
assert 16 - 6 == 10 and 25 - 3 == 22 and 49 - 2 == 47
assert 2 * 3 * 4 == 24 and 1 * 5 * 6 == 30 and 3 * 2 * 5 == 30
assert R(23) + R(14) == 73 and R(45) + R(12) == 75 and R(62) + R(23) == 58
assert Pd(24) + Pd(35) == 23 and Pd(43) + Pd(26) == 24 and Pd(52) + Pd(33) == 19
assert S(36) + S(24) == 15 and S(28) + S(19) == 20 and S(47) + S(38) == 22
assert S(24) * 3 == 18 and S(35) * 2 == 16 and S(47) * 2 == 22
assert (47 + 38) % 9 == 22 % 9

d["pyqPatterns"] = [
    PYQ(pattern=p[0], frequency=p[1], subtopic=p[2], howToSpot=p[3],
        approach=p[4], ex_q=p[5], ex_sol=p[6])
    for p in PYQS
]

upsert(d["practice"], NQ)
finish("missing-number", d)
