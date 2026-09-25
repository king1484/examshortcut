"""Phase-2 deep content for reasoning/counting-figures. Idempotent: `py -3 counting-figures.py`.

Every figure is generated from a line model (nonverbal_lib.Fig). The answer is the
brute-force count from the same model (points + merged lines, exact Fractions), and
it is asserted against the stored option.
"""
import math
import os
import sys

sys.path.insert(0, os.path.dirname(__file__))
from _lib import *  # noqa
from nonverbal_lib import *  # noqa
from nonverbal_lib import P as PT
from counting_figures_notes import NOTES, PATTERNS, PYQS

T = "counting-figures"
d = load(T)

for sid, notes in NOTES.items():
    set_sub(d, sid, notes=notes, patterns=PATTERNS[sid])
d["pyqPatterns"] = PYQS

NQ = []
_ctr = {}


def A(sub, pat, fig_svg, q, ans, wrong, solution, diff="medium", shortcut=None, t=45):
    _ctr[sub] = _ctr.get(sub, 0) + 1
    ans = str(ans)
    ws = []
    for w in wrong:
        w = str(w)
        if w != ans and w not in ws and int(w) > 0:
            ws.append(w)
    assert len(ws) >= 3, (sub, ans, wrong)
    NQ.append(Q(f"{sub}-p{_ctr[sub]:02d}", q, ans, ws[:3], solution, shortcut=shortcut,
                diff=diff, sub=sub, pat=pat, t=t, figure=fig_svg))


def sizes_text(fig):
    sz = fig.tri_sizes()
    parts = [f"{int(k) if k.denominator == 1 else k}× size: {v}" for k, v in sorted(sz.items())]
    return "; ".join(parts)


def dims_text(rects):
    c = Counter()
    for r in rects:
        xs = sorted({p[0] for p in r})
        ys = sorted({p[1] for p in r})
        if len(xs) == 2 and len(ys) == 2:
            w, h = xs[1] - xs[0], ys[1] - ys[0]
            c[f"{min(w, h)} × {max(w, h)}"] += 1
        else:
            c["tilted"] += 1
    order = sorted(c, key=lambda k: (k == "tilted", [int(x) for x in k.split(" × ")] if k != "tilted" else []))
    return ", ".join(f"{k}: {c[k]}" for k in order)


TRI_Q = "How many triangles are there in the given figure?"
SQ_Q = "How many squares are there in the given figure?"
RECT_Q = "How many rectangles (squares included) are there in the given figure?"
LINE_Q = "What is the minimum number of straight lines needed to draw the given figure?"

# ------------------------------------------------------------------ checks of values quoted in the notes
assert len(tri_apex(3, 0).triangles()) == 10 and len(tri_apex(2, 1).triangles()) == 12
assert [len(tri_grid(n).triangles()) for n in range(1, 6)] == [1, 5, 13, 27, 48]
sq_dm = rect(0, 0, 4, 4).add((0, 0), (4, 4)).add((4, 0), (0, 4)).add((2, 0), (2, 4)).add((0, 2), (4, 2))
assert len(sq_dm.triangles()) == 16 and sq_dm.count_lines() == 8
assert len(rect(0, 0, 4, 4).add((0, 0), (4, 4)).add((4, 0), (0, 4)).triangles()) == 8
assert len(grid(4, 3).squares()) == 20 and len(grid(3, 2).rectangles()) == 18
assert len(grid(4, 4).rectangles()) == 100 and len(grid(3, 3).rectangles()) == 36
assert len(grid(2, 2).squares()) == 5 and len(grid(2, 2).rectangles()) == 9
assert sum(k * k for k in range(1, 9)) == 204
assert grid(3, 2).count_lines() == 7 and grid(5, 4).count_lines() == 11


def medians():
    A_, B_, C_ = (0, 12), (12, 12), (6, 0)
    return Fig().poly([A_, B_, C_]).add(A_, (9, 6)).add(B_, (3, 6)).add(C_, (6, 12))


assert len(medians().triangles()) == 16 and medians().tri_sizes() == Counter({1: 6, 2: 3, 3: 6, 6: 1})


def pentagon(r=60, star_only=False):
    pts = [(round(r * math.sin(2 * math.pi * i / 5)) + r, round(-r * math.cos(2 * math.pi * i / 5)) + r)
           for i in range(5)]
    f = Fig()
    if not star_only:
        f.poly(pts)
    for i in range(5):
        f.add(pts[i], pts[(i + 2) % 5])
    return f, pts


pf, ppts = pentagon()
pt_outer = set(PT(*p) for p in ppts)
assert len(pf.triangles()) == 35
assert Counter(sum(p in pt_outer for p in t) for t in pf.triangles()) == Counter({3: 10, 2: 20, 1: 5})
assert pentagon(star_only=True)[0].count_lines() == 5


def hexagon(a=40, diag=True):
    h = round(a * math.sqrt(3) / 2)
    v = [(a, 0), (a // 2, h), (-a // 2, h), (-a, 0), (-a // 2, -h), (a // 2, -h)]
    v = [(x + a, y + h) for x, y in v]
    f = Fig().poly(v)
    if diag:
        for i in range(3):
            f.add(v[i], v[i + 3])
    return f


def hexagram(r=48):
    s = round(r * math.sqrt(3) / 2)
    t1 = [(0, -r), (s, r // 2), (-s, r // 2)]
    t2 = [(0, r), (s, -r // 2), (-s, -r // 2)]
    f = Fig().poly([(x + s, y + r) for x, y in t1]).poly([(x + s, y + r) for x, y in t2])
    return f


assert hexagon().count_lines() == 9 and hexagram().count_lines() == 6
assert len(tri_grid(3).triangles()) == 13 and tri_grid(3).count_lines() == 9
plus = Fig()
for (x, y) in [(1, 0), (0, 1), (1, 1), (2, 1), (1, 2)]:
    plus.extend(rect(x, y, x + 1, y + 1))
assert len(plus.rectangles()) == 11 and len(plus.squares()) == 5
assert len(grid(2, 2).poly([(1, 0), (2, 1), (1, 2), (0, 1)]).squares()) == 6

# ================================================================== triangles
# ct-p1 apex lines
for k, h, diff, wrong in [(5, 0, "easy", [15, 20, 18]), (2, 2, "medium", [12, 6, 16]), (4, 2, "hard", [30, 15, 40])]:
    f = tri_apex(k, h)
    n = len(f.triangles())
    assert n == (k + 1) * (k + 2) // 2 * (h + 1)
    base = (k + 1) * (k + 2) // 2
    cut = "" if h == 0 else (f" There {'is' if h == 1 else 'are'} {h} line{'s' if h > 1 else ''} parallel to the base, "
                             f"each crossing all the apex lines, so there are {h + 1} bases in all: {base} × {h + 1} = **{n}**.")
    sol = (f"Lines through the apex = {k} inner lines + 2 sides = {k + 2}. Any two of them make one triangle on a base: "
           f"C({k + 2}, 2) = ({k + 1} × {k + 2})/2 = {base}." + (cut if h else f" Total = **{n}**."))
    A("triangles", "ct-p1", f.svg(scale=11), TRI_Q, n, wrong, sol, diff=diff,
      shortcut=f"(k+1)(k+2)/2 × (h+1) with k = {k}, h = {h}.", t=35 if diff == "easy" else 50)

# ct-p2 squares / rectangles with diagonals
f = grid(2, 1, u=6).add((0, 0), (6, 6)).add((6, 0), (0, 6)).add((6, 0), (12, 6)).add((12, 0), (6, 6))
n = len(f.triangles())
sz = f.tri_sizes()
A("triangles", "ct-p2", f.svg(scale=10), TRI_Q, n, [16, 12, n + 2],
  f"Each square with both diagonals has 8 triangles, so the two squares give 16. Now look across the middle line: "
  f"two diagonals meet at the top end of the middle line and, with the long bottom side, form one big triangle; the "
  f"same happens upside down. That is {n - 16} more. By size (area in units of the smallest triangle) — {sizes_text(f)}. Total = **{n}**.",
  diff="medium", shortcut="8 per square + triangles that cross the shared side.", t=60)

f = rect(0, 0, 8, 8).add((0, 0), (8, 8)).add((8, 0), (0, 8)).add((4, 0), (4, 8)).add((0, 4), (8, 4)) \
    .poly([(4, 0), (8, 4), (4, 8), (0, 4)])
n = len(f.triangles())
A("triangles", "ct-p2", f.svg(scale=14), TRI_Q, n, [16, 24, n - 4],
  f"Start from the standard square with diagonals and midlines (16 triangles). The diamond joining the midpoints "
  f"cuts every corner into new triangles and makes others around the centre. By size (area in units of the smallest "
  f"triangle) — {sizes_text(f)}. Total = **{n}**.",
  diff="hard", shortcut="Count size by size; do each quarter the same way (symmetry).", t=75)

f = rect(0, 0, 12, 6).add((0, 0), (12, 6)).add((12, 0), (0, 6)).add((6, 0), (6, 6))
n = len(f.triangles())
A("triangles", "ct-p2", f.svg(scale=10), TRI_Q, n, [8, 6, n + 2],
  f"The rectangle with two diagonals alone has 8 triangles. The vertical midline passes through the centre and "
  f"splits the top and bottom triangles, adding new small and joined ones. By size (area in units of the smallest "
  f"triangle) — {sizes_text(f)}. Total = **{n}**.",
  diff="medium", shortcut="Rectangle + 2 diagonals = 8; then add what the new line creates.", t=55)

# ct-p3 triangle rows
for rows, diff, wrong in [(3, "medium", [9, 10, 12]), (4, "hard", [16, 20, 24])]:
    f = tri_grid(rows, u=4)
    n = len(f.triangles())
    ts = f.triangles()
    up = sum(1 for t in ts if sorted(p[1] for p in t)[0] < sorted(p[1] for p in t)[1])
    down = n - up
    A("triangles", "ct-p3", f.svg(scale=8), TRI_Q, n, wrong,
      f"There are {rows} rows, so {rows * rows} smallest triangles. Upright triangles of every size: {up}. "
      f"Upside-down triangles: {down}. Total = {up} + {down} = **{n}**.",
      diff=diff, shortcut="Rows 1, 2, 3, 4, 5 → 1, 5, 13, 27, 48.", t=45 if rows == 3 else 60)

# ct-p4 cevians
f = medians()
A("triangles", "ct-p4", f.svg(scale=10), TRI_Q, 16, [12, 6, 18],
  "All three medians meet at one centre point and make 6 smallest triangles. Two-piece triangles (a full side as "
  "base, the centre as top): 3. Three-piece triangles (each median cuts the big one into two halves): 6. The whole "
  "triangle: 1. Total = 6 + 3 + 6 + 1 = **16**.",
  diff="medium", shortcut="Triangle with 3 medians = 16 (memorise).", t=50)

f = Fig().poly([(0, 12), (12, 12), (6, 0)]).add((6, 0), (6, 12)).add((0, 12), (9, 6))
lab = {(6, 0): ("A", 0, -8), (0, 12): ("B", -7, 4), (12, 12): ("C", 7, 4), (6, 12): ("D", 0, 10),
       (9, 6): ("E", 8, 0), (6, 8): ("F", -7, 0)}
names = f.named_triangles(lab)
n = len(names)
A("triangles", "ct-p4", f.svg(scale=10, labels=lab), TRI_Q, n, [6, 7, 5],
  f"Use the letters on the figure (F is where the two inner lines cross). List triangles whose three sides are all "
  f"drawn: {', '.join(names)}. Total = **{n}**.",
  diff="medium", shortcut="Label corners and crossings; list triangles corner by corner.", t=60)
assert n == 8

f = Fig().poly([(0, 12), (12, 12), (6, 0)]).add((6, 0), (3, 12)).add((6, 0), (9, 12)).add((0, 12), (9, 6))
lab = {(6, 0): ("A", 0, -8), (0, 12): ("B", -7, 4), (3, 12): ("C", 0, 10), (9, 12): ("D", 0, 10),
       (12, 12): ("E", 7, 4), (9, 6): ("F", 8, 0), (F(18, 5), F(48, 5)): ("G", -8, -2),
       (F(54, 7), F(48, 7)): ("H", 0, -9)}
names = f.named_triangles(lab)
n = len(names)
with_a = [s for s in names if s[0] == "A"]
A("triangles", "ct-p4", f.svg(scale=10, labels=lab), TRI_Q, n, [10, 6, n - 2],
  f"Without line BF, the two lines from A give (3 × 4)/2 = 6 triangles on the base BE. Line BF crosses AC at G and "
  f"AD at H and creates more. Full list (corners named as in the figure): {', '.join(names)}. "
  f"Total = **{n}**.",
  diff="hard", shortcut="Start from the apex-line value 6, then add every triangle that uses line BF.", t=75)
assert len(with_a) >= 6

# ct-p5 composite
f, _ = pentagon()
A("triangles", "ct-p5", f.svg(scale=1.1), TRI_Q, 35, [30, 25, 10],
  "Sort the triangles by how many of the 5 outer corners they use. Three outer corners: every pair of corners is "
  "joined, so C(5, 3) = 10. Two outer corners: 20. One outer corner (the 5 points of the star): 5. "
  "Total = 10 + 20 + 5 = **35**.",
  diff="hard", shortcut="Pentagon with all diagonals = 35 (memorise).", t=60)

f = rect(0, 6, 12, 18).add((0, 6), (12, 18)).add((12, 6), (0, 18)).poly([(0, 6), (6, 0), (12, 6)], closed=False)
n = len(f.triangles())
A("triangles", "ct-p5", f.svg(scale=8), TRI_Q, n, [8, 10, n + 2],
  f"The square with both diagonals gives 8 triangles. The roof is 1 more triangle. No triangle can cross from the "
  f"roof into the square, because the roof's sloping sides stop at the top corners and do not continue any line "
  f"of the square. Total = 8 + 1 = **{n}**.",
  diff="easy", shortcut="Known part (8) + roof (1); check whether any triangle crosses the join.", t=40)
assert n == 9

f = hexagram()
n = len(f.triangles())
assert n == 8
A("triangles", "ct-p5", f.svg(scale=1.3), TRI_Q, n, [6, 2, 12],
  "Two big triangles overlap to form a six-point star. The 6 points of the star are small triangles, and the two big "
  "triangles count too. The middle is a hexagon (six sides), not a triangle. Total = 6 + 2 = **8**.",
  diff="easy", shortcut="Six-point star = 8 triangles.", t=35)

# ================================================================== squares-rectangles
for m_, n_, diff, wrong in [(4, 4, "easy", [16, 25, 29]), (5, 3, "medium", [15, 23, 29]), (5, 5, "medium", [25, 50, 45])]:
    f = grid(m_, n_, u=4)
    n = len(f.squares())
    terms = [(m_ - k + 1) * (n_ - k + 1) for k in range(1, min(m_, n_) + 1)]
    assert n == sum(terms)
    A("squares-rectangles", "sr-p1", f.svg(scale=5), SQ_Q, n, wrong,
      "The figure is a grid of " + f"{m_} columns and {n_} rows. Count size by size: "
      + ", ".join(f"{k} × {k}: {v}" for k, v in zip(range(1, len(terms) + 1), terms)) + f". Total = **{n}**.",
      diff=diff, shortcut=("1² + 2² + … + n²." if m_ == n_ else "Σ (m−k+1)(n−k+1)."), t=40)

for m_, n_, diff, wrong in [(3, 3, "easy", [14, 9, 30]), (6, 1, "easy", [6, 15, 12]), (4, 3, "medium", [20, 12, 48])]:
    f = grid(m_, n_, u=4)
    n = len(f.rectangles())
    assert n == math.comb(m_ + 1, 2) * math.comb(n_ + 1, 2)
    A("squares-rectangles", "sr-p2", f.svg(scale=5), RECT_Q, n, wrong,
      f"Vertical lines = {m_ + 1}, horizontal lines = {n_ + 1}. A rectangle is fixed by choosing 2 of each: "
      f"C({m_ + 1}, 2) × C({n_ + 1}, 2) = {math.comb(m_ + 1, 2)} × {math.comb(n_ + 1, 2)} = **{n}**.",
      diff=diff, shortcut=("Strip of m cells: m(m+1)/2." if n_ == 1 else "C(m+1,2) × C(n+1,2)."), t=40)

f = grid(5, 2, u=4)
R, S = len(f.rectangles()), len(f.squares())
A("squares-rectangles", "sr-p2", f.svg(scale=5),
  "How many rectangles that are **not** squares are there in the given figure?", R - S, [R, S, R - S - 2],
  f"All rectangles: C(6, 2) × C(3, 2) = 15 × 3 = {R}. Squares: 1 × 1 = 10, 2 × 2 = 4, total {S}. "
  f"Rectangles that are not squares = {R} − {S} = **{R - S}**.",
  diff="hard", shortcut="All rectangles − squares.", t=60)

f = grid(2, 2, u=4).poly([(4, 0), (8, 4), (4, 8), (0, 4)])
n = len(f.squares())
A("squares-rectangles", "sr-p3", f.svg(scale=10), SQ_Q, n, [5, 4, 7],
  f"Upright squares: 4 small + 1 big = 5. The diamond joining the middles of the sides is a tilted square: 1. "
  f"The midlines cut the diamond into triangles, not squares. Total = **{n}**.",
  diff="easy", shortcut="Grid squares + tilted squares.", t=35)

f = grid(4, 4, u=2).poly([(4, 0), (8, 4), (4, 8), (0, 4)])
n = len(f.squares())
A("squares-rectangles", "sr-p3", f.svg(scale=10), SQ_Q, n, [30, 32, 35],
  f"The 4 × 4 grid alone has 1 + 4 + 9 + 16 = 30 squares. The diamond through the middles of the four outer sides "
  f"adds 1 tilted square. The grid lines only cut the diamond into pieces, and no other tilted square has all four "
  f"sides drawn. Total = 30 + 1 = **{n}**.",
  diff="hard", shortcut="30 (grid) + 1 (diamond).", t=60)
assert n == 31

f = grid(2, 2, u=4).poly([(4, 0), (8, 4), (4, 8), (0, 4)]).poly([(2, 2), (6, 2), (6, 6), (2, 6)])
n = len(f.squares())
A("squares-rectangles", "sr-p3", f.svg(scale=10), SQ_Q, n, [6, 7, n + 2],
  f"Outer square: 1. Its four quarters (made by the midlines): 4. The diamond: 1. The inner square (joining the "
  f"middles of the diamond's sides): 1. The midlines cut the inner square into 4 small squares: 4. "
  f"Total = 1 + 4 + 1 + 1 + 4 = **{n}**.",
  diff="hard", shortcut="Outer grid 5 + diamond 1 + inner square 1 + its 4 quarters.", t=70)
assert n == 11 and Counter(len({p[0] for p in s}) for s in f.squares())[3] == 1  # exactly one tilted

A("squares-rectangles", "sr-p4", plus.svg(scale=20), RECT_Q, 11, [5, 9, 13],
  "Single cells: 5. Two cells: the centre with each of the 4 arms = 4. Three cells: the full middle row and the "
  "full middle column = 2. Total = 5 + 4 + 2 = **11**.",
  diff="medium", shortcut="Count by length: 1-cell, 2-cell, 3-cell rectangles.", t=45)

L = Fig()
for (x, y) in [(0, 0), (0, 1), (0, 2), (1, 2), (2, 2)]:
    L.extend(rect(x, y, x + 1, y + 1))
n = len(L.rectangles())
A("squares-rectangles", "sr-p4", L.svg(scale=20), RECT_Q, n, [5, 8, 12],
  f"By size — {dims_text(L.rectangles())}. The corner cell belongs to both the column and the row. Total = **{n}**.",
  diff="medium", shortcut="Column strip of 3 → 6, row strip of 3 → 6, corner cell counted twice → 6 + 6 − 1.", t=45)
assert n == 6 + 6 - 1

# 3 x 2 grid whose inner vertical line (x = 1) is missing in the top row
G = Fig()
for x in range(4):
    for y in range(2):
        if not (x == 1 and y == 0):
            G.add((x, y), (x, y + 1))
for y in range(3):
    for x in range(3):
        G.add((x, y), (x + 1, y))
n = len(G.rectangles())
full = len(grid(3, 2).rectangles())
A("squares-rectangles", "sr-p4", G.svg(scale=24), RECT_Q, n, [full, 15, n - 2],
  f"A full 3 × 2 grid would have 18 rectangles, but one small line in the top row is missing. Every rectangle that "
  f"needs that piece as a side is lost. Counting what is left by size — {dims_text(G.rectangles())}. "
  f"Total = **{n}**.",
  diff="hard", shortcut="Full-grid formula minus the rectangles that need the missing side.", t=70)

# ================================================================== straight-lines


def lines_sol(f, extra=""):
    h, v, s = f.count_lines("h"), f.count_lines("v"), f.count_lines("slant")
    return (f"Sweep one direction at a time. Horizontal: {h}. Vertical: {v}. Slanting: {s}{extra}. "
            f"Total = {h} + {v} + {s} = **{h + v + s}**.")


f = sq_dm
A("straight-lines", "sl-p1", f.svg(scale=16), LINE_Q, 8, [6, 10, 12], lines_sol(f),
  diff="easy", shortcut="Square + 2 diagonals + 2 midlines = 8.", t=30)

f = grid(2, 2, u=4)
for x in range(2):
    for y in range(2):
        f.add((4 * x, 4 * y), (4 * x + 4, 4 * y + 4)).add((4 * x + 4, 4 * y), (4 * x, 4 * y + 4))
n = f.count_lines()
A("straight-lines", "sl-p1", f.svg(scale=10), LINE_Q, n, [14, 10, 16],
  lines_sol(f, " (the cell diagonals join into longer lines: the 2 big corner-to-corner diagonals, plus 4 short "
               "lines, each joining the middles of two neighbouring sides)"),
  diff="medium", shortcut="Cell diagonals in one straight path join into one line.", t=50)
assert n == 12

f = grid(3, 1, u=4)
for x in range(3):
    f.add((4 * x, 0), (4 * x + 4, 4)).add((4 * x + 4, 0), (4 * x, 4))
n = f.count_lines()
A("straight-lines", "sl-p1", f.svg(scale=10), LINE_Q, n, [10, 14, 8],
  lines_sol(f, " (six cell diagonals; no two of them lie in one straight path)"),
  diff="medium", shortcut="Here every cell diagonal is its own line.", t=45)

f = rect(0, 0, 12, 6).add((0, 0), (12, 6)).add((12, 0), (0, 6)).add((6, 0), (6, 6))
n = f.count_lines()
A("straight-lines", "sl-p1", f.svg(scale=10), LINE_Q, n, [6, 9, 8], lines_sol(f),
  diff="easy", shortcut="4 sides + 2 diagonals + 1 midline.", t=30)

# sl-p2 one direction only
f = rect(0, 6, 12, 18).add((0, 6), (12, 18)).add((12, 6), (0, 18)).poly([(0, 6), (6, 0), (12, 6)], closed=False)
n = f.count_lines("slant")
A("straight-lines", "sl-p2", f.svg(scale=8), "How many **slanting** straight lines are there in the given figure?",
  n, [2, 6, 3],
  f"Slanting lines are neither horizontal nor vertical. The square has 2 diagonals and the roof has 2 sloping sides. "
  f"The roof sides do not lie on the diagonals' paths, so they are separate lines. Total = **{n}**.",
  diff="easy", shortcut="Count only the asked direction.", t=30)

f = tri_grid(4, u=4)
n = f.count_lines("h")
A("straight-lines", "sl-p2", f.svg(scale=8), "How many **horizontal** straight lines are there in the given figure?",
  n, [5, 3, 12],
  f"The big triangle has 4 rows of small triangles. There is one horizontal line under each row, the base included, "
  f"and the top corner is only a point. Horizontal lines = **{n}**. (All lines together would be {f.count_lines()}.)",
  diff="medium", shortcut="Horizontal lines = number of rows.", t=35)

f = rect(0, 0, 8, 8).add((0, 0), (8, 8)).add((8, 0), (0, 8)).poly([(4, 0), (8, 4), (4, 8), (0, 4)])
n = f.count_lines("slant")
A("straight-lines", "sl-p2", f.svg(scale=12), "How many **slanting** straight lines are there in the given figure?",
  n, [4, 8, 2],
  f"The square's 2 diagonals are slanting. The diamond has 4 sides; each is parallel to a diagonal but lies on a "
  f"different path, so each is a separate line. Total slanting lines = 2 + 4 = **{n}**.",
  diff="medium", shortcut="Parallel is not the same as in-line.", t=40)

# sl-p3 stars, polygons, triangle grids
f, _ = pentagon(star_only=True)
A("straight-lines", "sl-p3", f.svg(scale=1.1), LINE_Q, 5, [10, 6, 15],
  "Each point of the star is made by two long lines, and each long line runs from one point to another. There are "
  "**5** such lines (the star can be drawn without lifting the pen, one line at a time).",
  diff="easy", shortcut="Five-point star = 5 lines.", t=25)

f = hexagram()
A("straight-lines", "sl-p3", f.svg(scale=1.3), LINE_Q, 6, [12, 8, 3],
  "The six-point star is two big triangles laid over each other. Each triangle has 3 sides, and each side runs straight "
  "through the star. Total = 3 + 3 = **6**.",
  diff="medium", shortcut="Two triangles → 6 lines.", t=30)

f = hexagon()
A("straight-lines", "sl-p3", f.svg(scale=1.4), LINE_Q, 9, [12, 6, 8],
  "The hexagon has 6 sides. The 3 long diagonals each join opposite corners and pass through the centre as one "
  "straight line each. Total = 6 + 3 = **9**.",
  diff="easy", shortcut="Sides + long diagonals.", t=30)

f = tri_grid(3, u=4)
n = f.count_lines()
A("straight-lines", "sl-p3", f.svg(scale=10), LINE_Q, n, [12, 6, 13],
  f"There are 3 directions: horizontal, slanting left and slanting right. In each direction there is one line per row "
  f"(3 rows → 3 lines). Total = 3 × 3 = **{n}**.",
  diff="medium", shortcut="Rows × 3 directions.", t=40)

f, _ = pentagon()
A("straight-lines", "sl-p3", f.svg(scale=1.1), LINE_Q, 10, [5, 15, 8],
  "The pentagon has 5 sides and 5 diagonals (the star). Each is one straight line. Total = **10**.",
  diff="easy", shortcut="Sides + diagonals: 5 + 5.", t=30)

# sl-p4 grids
f = grid(5, 4, u=4)
A("straight-lines", "sl-p4", f.svg(scale=5), LINE_Q, 11, [9, 20, 10],
  "The grid has 5 columns and 4 rows. Vertical lines = 5 + 1 = 6. Horizontal lines = 4 + 1 = 5. Total = **11**.",
  diff="easy", shortcut="(m + 1) + (n + 1).", t=25)
assert f.count_lines() == 11

f = grid(4, 4, u=4).add((0, 0), (16, 16)).add((16, 0), (0, 16))
n = f.count_lines()
A("straight-lines", "sl-p4", f.svg(scale=5), LINE_Q, n, [10, 16, 14],
  f"Grid: 5 vertical + 5 horizontal = 10. The two long diagonals run corner to corner: 2 more. Total = **{n}**.",
  diff="medium", shortcut="(m+1) + (n+1) + 2.", t=35)
assert n == 12

f = grid(3, 3, u=4)
for x in range(3):
    for y in range(3):
        f.add((4 * x, 4 * y), (4 * x + 4, 4 * y + 4))
n = f.count_lines()
A("straight-lines", "sl-p4", f.svg(scale=7), LINE_Q, n, [17, 10, 15],
  f"Grid lines: 4 vertical + 4 horizontal = 8. Each cell has one diagonal going down to the right; diagonals that "
  f"touch end to end lie on one straight path. The paths are: the main diagonal (3 pieces), two paths of 2 pieces and "
  f"two of 1 piece = 5 lines. Total = 8 + 5 = **{n}**.",
  diff="hard", shortcut="Count diagonal paths, not pieces: 2 × 3 − 1 = 5.", t=60)
assert n == 13

upsert(d["practice"], NQ)
finish(T, d)
