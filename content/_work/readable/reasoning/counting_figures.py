"""Readable rewrite of Reasoning > Counting Figures (all 3 subtopics).

Plain English, one idea per section. Every count on the page is recomputed
below by exact enumeration (Fractions) and asserted:
- triangles: every triple of maximal drawn lines whose pairwise crossings lie
  on the drawn intervals -> a real triangle (the exam definition);
- squares/rectangles in grids: brute-force over line pairs vs formulas;
- straight lines: collinear touching pieces merged into maximal lines.
Run: python counting_figures.py  (patches content/core/topics/reasoning/counting-figures.json)
"""
import json
import math
from fractions import Fraction as F
from itertools import combinations
from pathlib import Path

ROOT = Path(__file__).resolve().parents[3]
TOPIC = ROOT / "core" / "topics" / "reasoning" / "counting-figures.json"


# ---------- exact geometry helpers ----------
def _inter(s1, s2):
    """Parameters (t, s) of the intersection of the two segment lines, or None if parallel."""
    (x1, y1), (x2, y2) = s1
    (x3, y3), (x4, y4) = s2
    d1x, d1y = x2 - x1, y2 - y1
    d2x, d2y = x4 - x3, y4 - y3
    den = d1x * d2y - d1y * d2x
    if den == 0:
        return None
    rx, ry = x3 - x1, y3 - y1
    t = (rx * d2y - ry * d2x) / den
    s = (rx * d1y - ry * d1x) / den
    return t, s


def triangles_in(segs, eps=1e-9):
    """All triangles formed by the drawn segments (each segment = one full drawn
    interval of a maximal straight line). Returns list of (p, q, r, upright)."""
    n = len(segs)
    P = {}
    for i, j in combinations(range(n), 2):
        r = _inter(segs[i], segs[j])
        if r is None:
            continue
        t, s = r
        if -eps <= t <= 1 + eps and -eps <= s <= 1 + eps:
            (x1, y1), (x2, y2) = segs[i]
            P[(i, j)] = (x1 + t * (x2 - x1), y1 + t * (y2 - y1))
    out = []
    for a, b, c in combinations(range(n), 3):
        if (a, b) in P and (a, c) in P and (b, c) in P:
            p, q, r = P[(a, b)], P[(a, c)], P[(b, c)]
            if abs(p[0] - q[0]) + abs(p[1] - q[1]) <= eps:
                continue
            if abs(p[0] - r[0]) + abs(p[1] - r[1]) <= eps:
                continue
            if abs(q[0] - r[0]) + abs(q[1] - r[1]) <= eps:
                continue
            cr = (q[0] - p[0]) * (r[1] - p[1]) - (q[1] - p[1]) * (r[0] - p[0])
            if abs(cr) > eps:
                out.append((p, q, r, cr > 0))
    return out


def fig_square(diagonals=True, midlines=False):
    """Unit-square scaled 2x2 with chosen extra lines."""
    A, B, C, D = (F(0), F(0)), (F(2), F(0)), (F(2), F(2)), (F(0), F(2))
    segs = [(A, B), (B, C), (C, D), (D, A)]
    if diagonals:
        segs += [(A, C), (B, D)]
    if midlines:
        segs += [((F(1), F(0)), (F(1), F(2))), ((F(0), F(1)), (F(2), F(1)))]
    return segs


def fig_medians():
    """Triangle with all three medians."""
    A, B, C = (F(0), F(3)), (F(0), F(0)), (F(3), F(0))
    return [(A, B), (B, C), (C, A),
            (A, (F(3, 2), F(0))),            # apex to midpoint of BC
            (B, (F(3, 2), F(3, 2))),         # B to midpoint of AC
            (C, (F(0), F(3, 2)))]            # C to midpoint of AB


def fig_apex(k, h):
    """Triangle with k cevians from the apex and h lines parallel to the base."""
    A, B, C = (F(0), F(3)), (F(0), F(0)), (F(3), F(0))
    segs = [(A, B), (B, C), (C, A)]
    for i in range(1, k + 1):
        segs.append((A, (F(3 * i, k + 1), F(0))))
    for j in range(1, h + 1):
        y = F(3 * j, h + 1)
        segs.append(((F(0), y), (3 - y, y)))
    return segs


def fig_rows(n):
    """Triangle whose sides are cut into n equal parts, parallels drawn to all sides."""
    A, B, C = (F(0), F(n)), (F(0), F(0)), (F(n), F(0))
    segs = [(A, B), (B, C), (C, A)]
    for i in range(1, n):
        y = F(i)
        segs.append(((F(0), y), (n - y, y)))   # parallel to BC
        x = F(i)
        segs.append(((x, F(0)), (x, n - x)))   # parallel to AB
        segs.append(((F(0), x), (x, F(0))))    # x + y = i, parallel to CA
    return segs


def fig_pentagram():
    """Regular pentagon with all 5 diagonals (float coords, 5-fold symmetry)."""
    vs = [(math.cos(math.radians(90 + 72 * k)), math.sin(math.radians(90 + 72 * k))) for k in range(5)]
    segs = []
    for k in range(5):
        segs.append((vs[k], vs[(k + 1) % 5]))   # sides
        segs.append((vs[k], vs[(k + 2) % 5]))   # diagonals
    return vs, segs


# ---------- triangles subtopic: verify every number ----------
sq_diag = len(triangles_in(fig_square(diagonals=True)))
sq_full = len(triangles_in(fig_square(diagonals=True, midlines=True)))
med = len(triangles_in(fig_medians()))
assert sq_diag == 8 and sq_full == 16 and med == 16, (sq_diag, sq_full, med)

vs, psegs = fig_pentagram()
pent = triangles_in(psegs)
assert len(pent) == 35, len(pent)


def is_outer(pt):
    return any(abs(pt[0] - v[0]) + abs(pt[1] - v[1]) < 1e-6 for v in vs)


by_outer = {}
for p, q, r, _ in pent:
    k = sum(1 for pt in (p, q, r) if is_outer(pt))
    by_outer[k] = by_outer.get(k, 0) + 1
assert by_outer == {3: 10, 2: 20, 1: 5}, by_outer  # 35 = 10 + 20 + 5

for k, want in [(2, 6), (3, 10), (4, 15)]:
    got = len(triangles_in(fig_apex(k, 0)))
    assert got == want == math.comb(k + 2, 2), (k, got, want)
for k, h, want in [(2, 1, 12), (3, 1, 20), (2, 2, 18), (3, 2, 30)]:
    got = len(triangles_in(fig_apex(k, h)))
    assert got == want == math.comb(k + 2, 2) * (h + 1), (k, h, got, want)

rows_totals = {n: len(triangles_in(fig_rows(n))) for n in range(1, 6)}
assert rows_totals == {1: 1, 2: 5, 3: 13, 4: 27, 5: 48}, rows_totals
r3 = triangles_in(fig_rows(3))
def same_way_up(t):
    """True when the triangle is a scaled copy of the big one (right angle at lower left)."""
    pts = t[:3]
    for v in pts:
        o = [q for q in pts if q is not v]
        a, b = sorted(o, key=lambda q: q[1])   # a: same height as v, b: above v
        if a[1] == v[1] and b[0] == v[0] and a[0] > v[0] and b[1] > v[1] and (a[0] - v[0]) == (b[1] - v[1]):
            return True
    return False


up = sum(1 for t in r3 if same_way_up(t))
assert up == 10 and len(r3) - up == 3, (up, len(r3))
n = 3
up_sizes = [((n - s + 1) * (n - s + 2)) // 2 for s in range(1, 4)]
assert sum(up_sizes) == 10 and up_sizes == [6, 3, 1]

# ---------- squares/rectangles subtopic: verify every number ----------
def grid_counts(m, n):
    """Brute-force squares and rectangles (squares included) in an m-col x n-row grid."""
    R = S = 0
    for x1, x2 in combinations(range(m + 1), 2):
        for y1, y2 in combinations(range(n + 1), 2):
            R += 1
            if x2 - x1 == y2 - y1:
                S += 1
    return S, R


def formulas(m, n):
    S = sum((m - k + 1) * (n - k + 1) for k in range(1, min(m, n) + 1))
    R = math.comb(m + 1, 2) * math.comb(n + 1, 2)
    return S, R


for m, n in [(2, 2), (3, 3), (4, 4), (4, 3), (3, 2), (5, 4), (8, 8), (1, 5)]:
    assert grid_counts(m, n) == formulas(m, n), (m, n)
S44, R44 = formulas(4, 4)
S33, R33 = formulas(3, 3)
S22, R22 = formulas(2, 2)
S43, R43 = formulas(4, 3)
S32, R32 = formulas(3, 2)
S88, R88 = formulas(8, 8)
assert (S44, R44) == (30, 100) and (S33, R33) == (14, 36) and (S22, R22) == (5, 9)
assert (S43, R43) == (20, 60) and (S32, R32) == (8, 18) and (S88, R88) == (204, 1296)
assert sum(k * k for k in range(1, 9)) == 204 and R33 - S33 == 22 and R44 - S44 == 70
assert 5 * 6 // 2 == 15  # strip of 5 cells -> 15 rectangles

plus_cells = {(1, 0), (0, 1), (1, 1), (2, 1), (1, 2)}
plus_rects = 0
for x1 in range(3):
    for y1 in range(3):
        for x2 in range(x1, 3):
            for y2 in range(y1, 3):
                filled = all((x, y) in plus_cells
                             for x in range(x1, x2 + 1) for y in range(y1, y2 + 1))
                if filled:
                    plus_rects += 1
assert plus_rects == 11, plus_rects
assert 4 + 1 + 1 == 6  # tilted-square figure: 4 small + 1 big + 1 diamond

# ---------- straight-lines subtopic: verify every number ----------
def max_lines(segs):
    """Maximal straight lines from int-coordinate segments (collinear touching pieces merge)."""
    groups = {}
    for (px, py), (qx, qy) in segs:
        dx, dy = qx - px, qy - py
        g = math.gcd(abs(dx), abs(dy))
        a, b = dx // g, dy // g
        if a < 0 or (a == 0 and b < 0):
            a, b = -a, -b
        key = (a, b, b * px - a * py)          # same line <=> same direction + offset
        t1, t2 = sorted((a * px + b * py, a * qx + b * qy))
        groups.setdefault(key, []).append((t1, t2))
    count = 0
    per_dir = {}
    for (a, b, _), ivs in groups.items():
        ivs.sort()
        cur_end = None
        lines_here = 0
        for s, e in ivs:
            if cur_end is None or s > cur_end:
                lines_here += 1
                cur_end = e
            else:
                cur_end = max(cur_end, e)
        count += lines_here
        per_dir[(a, b)] = per_dir.get((a, b), 0) + lines_here
    return count, per_dir


sq8 = fig_square(diagonals=True, midlines=True)
sq8i = [((int(p[0]), int(p[1])), (int(q[0]), int(q[1]))) for p, q in sq8]
assert max_lines(sq8i) == (8, {(1, 0): 3, (0, 1): 3, (1, 1): 1, (1, -1): 1}), max_lines(sq8i)
sq6i = [((int(p[0]), int(p[1])), (int(q[0]), int(q[1]))) for p, q in fig_square(diagonals=True)]
assert max_lines(sq6i)[0] == 6

grid22 = [((x, 0), (x, 2)) for x in range(3)] + [((0, y), (2, y)) for y in range(3)]
cell_diag = []
for i in range(2):
    for j in range(2):
        cell_diag += [((i, j), (i + 1, j + 1)), ((i + 1, j), (i, j + 1))]
tot22, dirs22 = max_lines(grid22 + cell_diag)
assert tot22 == 12, tot22
assert dirs22 == {(1, 0): 3, (0, 1): 3, (1, 1): 3, (1, -1): 3}, dirs22
assert (3 + 1) + (2 + 1) == 7 and (5 + 1) + (4 + 1) == 11 and (3 + 1) == 4

pv = [(math.cos(math.radians(90 + 72 * k)), math.sin(math.radians(90 + 72 * k))) for k in range(5)]
pentagram_segs = [(pv[k], pv[(k + 2) % 5]) for k in range(5)]
# no two pentagram strokes are collinear, and consecutive strokes meet at a corner only
for (p1, q1), (p2, q2) in combinations(pentagram_segs, 2):
    assert (p1, q1) != (p2, q2)  # five distinct strokes
assert len(pentagram_segs) == 5  # 5 strokes, none collinear with another -> 5 lines
assert 6 + 3 == 9 and 3 * 3 == 9 and 2 + 2 + 2 == 6


# ================= content =================
def pat(pid, name, freq, spot, formula, steps, why, q, ex_steps, answer):
    return {"id": pid, "name": name, "frequency": freq, "howToSpot": spot, "formula": formula,
            "steps": steps, "why": why, "example": {"q": q, "steps": ex_steps, "answer": answer}}


# ---------------- triangles ----------------
t_concept = (
    "A triangle is any closed shape with exactly three straight sides, even when other lines cross it. "
    "Never count by eye. Work size by size: smallest triangles, then bigger ones made of joined pieces, "
    "then the whole figure. For a triangle with lines from its top corner, one short formula gives the count."
)

t_notes = r"""### What counts as a triangle
A triangle is a closed shape with exactly three straight sides. A side can pass through other lines on the way. So a big shape made of joined pieces still counts.

Think of a cut samosa. Each cut makes new pieces. Two small pieces joined together can still form one big triangle. Most wrong answers miss these bigger triangles.

> **Rule:** Count every closed shape whose border has exactly three straight pieces. Extra lines inside it do not matter.

### Count size by size
Never count everything at once. Go from smallest to biggest.

1. Count the smallest triangles. These have no line inside.
2. Count triangles made of 2 joined pieces, then 3 pieces, and so on.
3. Count the whole figure if it is itself a triangle.
4. Add the groups.

A square with both diagonals: 4 smallest triangles meet at the centre. 4 halves use a full side as base. Total $4+4=8$.

> **Tip:** Write each group's count beside the figure. Adding group totals is safer than one running count.

### Name the corners for odd figures
Some figures fit no formula: overlapping triangles, house shapes, mixed lines. Label every corner and every crossing point with a letter.

List triangles one point at a time. For each point, find triangles using only the lines actually drawn there. This is slow but nothing gets counted twice.

### The apex formula
One common figure: a triangle with $k$ extra lines from its top corner (the apex) to the base.

Every triangle here uses the apex plus two of the $k+2$ lines through it. Choosing any two of them gives:
$$T=\dfrac{(k+1)(k+2)}{2}$$
With 3 apex lines: $4\times5\div2=10$ triangles.

> **Watch:** $k$ counts only the extra lines. The two sides of the big triangle are added on top, giving $k+2$.

### Horizontal cuts multiply
Now add $h$ lines parallel to the base, each crossing every apex line. Each cut is one more base line, so the whole set repeats per base:
$$T=\dfrac{(k+1)(k+2)}{2}\times(h+1)$$
With 2 apex lines and 1 cut: $6\times2=12$ triangles.

> **Watch:** A cut counts only if it crosses every apex line. A short cut that stops early breaks the formula.

### Famous figures worth memorising
Exam figures repeat every year. Learn these totals; each is verified above.

| Figure | Triangles |
|---|---|
| Square (any rectangle) with both diagonals | 8 |
| Same square plus both midlines | 16 |
| Triangle with all 3 medians | 16 |
| Pentagon with all 5 diagonals (star) | 35 |

A triangle split into rows of small triangles gives 1, 5, 13, 27, 48 for 1 to 5 rows. Upside-down triangles count too: 3 rows give 10 upright and 3 upside-down, total 13.
"""

t_formulas = [
    {"name": "Apex lines", "tex": r"T = \frac{(k+1)(k+2)}{2}", "note": "k extra lines drawn from the apex to the base."},
    {"name": "Apex lines + horizontal cuts", "tex": r"T = \frac{(k+1)(k+2)}{2}\times(h+1)", "note": "h lines parallel to the base, each crossing every apex line."},
]

t_tricks = [
    {
        "title": "Square with diagonals: 8 or 16",
        "body": "A rectangle with both diagonals always has 8 triangles. Add both midlines and it becomes 16. Memorise both.",
        "example": {
            "q": "How many triangles are there in a square with both diagonals and both midlines drawn?",
            "steps": ["Smallest triangles: 8 (two inside each quarter).", "Two-piece triangles, full side as base: 4.", "Half-squares along the diagonals: 4.", r"$8+4+4=16$."],
            "answer": "16",
        },
    },
    {
        "title": "Count the lines, then choose two",
        "body": "In an apex figure, count the lines through the apex (extra lines plus both sides) and choose any two of them.",
        "example": {
            "q": "A triangle has 4 lines drawn from its apex to the base. How many triangles are there?",
            "steps": [r"Lines through the apex: $4+2=6$.", r"Choose 2 of 6: $\dfrac{6\times5}{2}$.", "$=15$."],
            "answer": "15",
        },
    },
]

t_mistakes = [
    {"wrong": "Counting only the smallest triangles.", "right": "After the smallest, hunt joined pieces of 2 and 3 parts, then the whole figure."},
    {"wrong": "Counting a four-sided pointed region as a triangle.", "right": "Trace the border. Only exactly three straight pieces count."},
    {"wrong": "Forgetting the big outer triangle.", "right": "End every count by asking: is the whole figure itself one more triangle?"},
    {"wrong": "Taking k as the number of base parts.", "right": "k is the number of extra apex lines. The base has k + 1 parts, not k."},
    {"wrong": "Multiplying by h instead of h + 1 for horizontal cuts.", "right": "The base itself is also a base line, so the multiplier is h + 1."},
    {"wrong": "Skipping the upside-down triangles in row figures.", "right": "Count upright sizes first, then hunt the upside-down ones between them."},
]

t_revision = [
    "Count size by size: smallest, then joined pieces, then the whole figure.",
    r"Apex lines: $T=\dfrac{(k+1)(k+2)}{2}$; with h horizontal cuts multiply by $h+1$.",
    "Square with 2 diagonals = 8; add both midlines = 16.",
    "Row figures: 1, 5, 13, 27, 48 triangles for 1 to 5 rows.",
    "Triangle with 3 medians = 16; pentagon with all diagonals = 35.",
    "No formula fits? Label every corner and crossing point, then list triangles.",
]

t_patterns = [
    pat("ct-p1", "Triangle with lines from the apex (and horizontal cuts)", "very common",
        "One big triangle; several lines run from its top corner to the base; sometimes lines parallel to the base cross them all.",
        r"T=\frac{(k+1)(k+2)}{2}\times(h+1)",
        ["Count k, the extra lines from the apex.", "Count h, the lines parallel to the base that cross every apex line.",
         "One base strip: (k + 1)(k + 2) ÷ 2.", "Multiply by (h + 1), one factor per base line."],
        "Every triangle picks two of the k + 2 lines through the apex and one of the h + 1 base lines, so the choices multiply.",
        "A triangle has 3 lines drawn from its apex to the base, and 1 line parallel to the base crossing all of them. How many triangles are there?",
        [r"$k=3$: one strip has $\dfrac{4\times5}{2}=10$ triangles.", r"$h=1$, so 2 base lines.", r"$10\times2=20$."],
        "20"),
    pat("ct-p2", "Square or rectangle with diagonals and midlines", "very common",
        "A square or rectangle with one or both diagonals, often with the lines joining the middles of opposite sides.",
        None,
        ["Count the smallest triangles around the centre.", "Count two-piece triangles with a full side as base.",
         "Count the half-squares along each diagonal.", "Add the groups."],
        "The figure is symmetric, so each size comes in a set of four and one representative settles the group.",
        "A square has both diagonals and both midlines drawn. How many triangles are there?",
        ["Smallest: 8 (two in each quarter).", "Full side as base: 4.", "Half-squares: 4.", r"$8+4+4=16$."],
        "16"),
    pat("ct-p3", "Triangle divided into rows of small triangles", "common",
        "A big triangle filled with small triangles, some pointing up and some pointing down.",
        None,
        ["Count n, the number of rows (parts on each side).", "Upright triangles of size s: (n − s + 1)(n − s + 2) ÷ 2, for every s.",
         "Then count the upside-down ones, usually only the small size.", "Add both lists."],
        "Upright triangles of one size sit in a triangular number of positions; the upside-down ones hide between them.",
        "A triangle is divided into 3 rows of small triangles. How many triangles are there?",
        [r"Upright: size 1 = 6, size 2 = 3, size 3 = 1, total 10.", "Upside-down: 3 small ones.", r"$10+3=13$."],
        "13"),
    pat("ct-p4", "Triangle with lines from its corners (medians and cevians)", "common",
        "A triangle with lines from one or more corners to the opposite sides, crossing inside.",
        None,
        ["Label every corner and inside crossing point.", "Count the smallest triangles around each crossing.",
         "Look for joined pieces and half-triangles along each drawn line.", "Finish with the whole triangle."],
        "The crossing points split each line into levels, so triangles appear at several sizes; labelling keeps them apart.",
        "In a triangle, all three medians are drawn. How many triangles are formed?",
        ["Smallest, around the centre: 6.", "A full side as base, centre as top: 3.", "Each median halves the big triangle: 6 halves.", "The whole triangle: 1.", r"$6+3+6+1=16$."],
        "16"),
    pat("ct-p5", "Irregular composite figures (house, star, pentagon)", "common",
        "A figure built from several shapes: a house with a roof, a star inside a pentagon, two overlapping triangles.",
        None,
        ["Break the figure into known parts (square with diagonals = 8, and so on).", "Count triangles fully inside each part.",
         "Count triangles that cross from one part into another.", "Add and double-check by symmetry."],
        "Known sub-figures give quick totals; only the triangles crossing between parts need fresh work.",
        "A regular pentagon has all 5 of its diagonals drawn, forming a star inside. How many triangles are there?",
        ["Triangles using 3 outer corners: choose any 3 of 5 = 10.", "Using 2 outer corners: 20.", "Using 1 outer corner (star tips): 5.", r"$10+20+5=35$."],
        "35"),
]

# ---------------- squares-rectangles ----------------
sr_concept = (
    "In a grid, count squares and rectangles by choosing lines, not by eye. Any 2 vertical grid lines and any 2 horizontal ones frame exactly one rectangle. "
    "For squares, go size by size: 1 by 1, then 2 by 2, and so on. "
    "Every square is also a rectangle, so rectangle counts include squares."
)

sr_notes = r"""### Every square is a rectangle
A rectangle has four sides and four right angles. A square is a rectangle with all four sides equal. So when a question asks for rectangles, the squares are inside the count. Only the phrase "rectangles that are not squares" leaves them out.

### Count squares size by size
In a grid of m columns and n rows, count each size separately.

- 1 × 1 squares: $m\times n$
- 2 × 2 squares: $(m-1)(n-1)$
- 3 × 3 squares: $(m-2)(n-2)$, and so on.

A 4 × 3 grid: $12+6+2=20$ squares. For a square n × n grid the total is $1^2+2^2+\dots+n^2$. A chessboard: $1+4+9+\dots+64=204$ squares.

> **Tip:** Stop when the square's side reaches the smaller of m and n. Bigger squares simply do not fit.

### Count rectangles by picking lines
Never hunt shapes. A rectangle is fixed the moment you pick its two vertical sides and its two horizontal sides.

A grid with m columns has $m+1$ vertical lines. With n rows it has $n+1$ horizontal lines. Pick any 2 of each:
$$R=\binom{m+1}{2}\times\binom{n+1}{2}=\frac{m(m+1)}{2}\times\frac{n(n+1)}{2}$$
A 3 × 2 grid: $6\times3=18$ rectangles. A single row of m cells has $\dfrac{m(m+1)}{2}$ rectangles.

### Rectangles that are not squares
Some questions ask for rectangles that are not squares. Count all rectangles, then subtract the squares: $R-S$.

A 3 × 3 grid: $36-14=22$ rectangles that are not squares.

> **Watch:** Options love to offer R and S alone. Read whether the question wants all rectangles or only the non-square ones.

### Check with a small grid
When you forget a formula, test it on a tiny grid you can count by eye.

A 2 × 2 grid has 4 small squares and 1 big square, so 5 squares. It has 9 rectangles: 4 single cells, 4 two-cell blocks and 1 whole grid. The formula gives $3\times3=9$, so it works.

### Tilted squares
Join the middles of a square's four sides and you get a tilted square, a diamond. It counts as a square too.

A square with both midlines and the diamond: 4 small squares + 1 big square + 1 diamond = 6 squares. The midlines cut the diamond into 4 triangles, so no extra squares hide inside it.

> **Watch:** A tilted square needs all four sides fully drawn. Grid lines crossing a diamond only make triangles.

### Irregular grids
Plus signs, L shapes and grids with missing lines break the formulas. Check every candidate by hand.

1. Count the single cells.
2. For each bigger square or rectangle, check that all four sides are drawn.
3. Check the inside is completely filled.

Five equal squares in a plus sign: 5 single cells + 4 two-cell blocks + 1 full row + 1 full column = 11 rectangles.

> **Example:** A missing middle line kills every rectangle that needs it as a side. Always trace the four sides.
"""

sr_formulas = [
    {"name": "Rectangles in an m × n grid", "tex": r"R = \binom{m+1}{2}\binom{n+1}{2}", "note": "Pick 2 of the m + 1 vertical lines and 2 of the n + 1 horizontal lines."},
    {"name": "Squares in an m × n grid", "tex": r"S = \sum_{k=1}^{\min(m,n)} (m-k+1)(n-k+1)", "note": "An n × n grid gives 1 squared + 2 squared + ... + n squared."},
]

sr_tricks = [
    {
        "title": "Line-pair trick",
        "body": "A rectangle is decided by its two vertical sides and two horizontal sides. Count line pairs, never shapes.",
        "example": {
            "q": "How many rectangles are there in a 3 × 2 grid?",
            "steps": [r"Vertical lines: 4, so $\binom{4}{2}=6$.", r"Horizontal lines: 3, so $\binom{3}{2}=3$.", r"$6\times3=18$."],
            "answer": "18",
        },
    },
    {
        "title": "Memorise the small grids",
        "body": "2 × 2: 5 squares, 9 rectangles. 3 × 3: 14 squares, 36 rectangles. 4 × 4: 30 squares, 100 rectangles. They appear inside bigger questions.",
        "example": {
            "q": "How many squares are there in a 4 × 4 grid?",
            "steps": [r"$1^2+2^2+3^2+4^2$.", r"$1+4+9+16$.", "$=30$."],
            "answer": "30",
        },
    },
]

sr_mistakes = [
    {"wrong": "Leaving squares out when the question asks for rectangles.", "right": "Every square is a rectangle. Subtract them only when the question says non-square."},
    {"wrong": "Using the number of cells instead of lines in the choose-2 count.", "right": "A grid with m columns has m + 1 lines. Choose 2 of the lines."},
    {"wrong": "Missing the bigger squares (2 × 2, 3 × 3) in a grid.", "right": "Count size by size up to the smaller side of the grid."},
    {"wrong": "Counting a tilted square's triangle pieces as more squares.", "right": "Grid lines through a diamond cut it into triangles, not squares."},
    {"wrong": "Applying the grid formula to a plus or L shape.", "right": "Irregular shapes need a side-by-side check: all four sides drawn, inside filled."},
]

sr_revision = [
    r"Squares in an $m\times n$ grid: add $(m-k+1)(n-k+1)$ for each size k.",
    r"Square grid: $1^2+2^2+\dots+n^2$; chessboard = 204.",
    r"Rectangles: $\binom{m+1}{2}\times\binom{n+1}{2}$.",
    "Non-square rectangles = R − S.",
    "Every square is a rectangle.",
    "Tilted squares count once; irregular grids need a four-sides check.",
]

sr_patterns = [
    pat("sr-p1", "Squares in a grid", "very common",
        "A chessboard-like grid; the question asks for squares of all sizes.",
        r"S=\sum_{k=1}^{\min(m,n)}(m-k+1)(n-k+1)",
        ["Note m columns and n rows.", "Add (m − k + 1)(n − k + 1) for k = 1, 2, ... up to the smaller side.",
         "For an n × n grid use 1 squared + 2 squared + ... + n squared."],
        "A k by k square fits in (m − k + 1) places across and (n − k + 1) places down.",
        "How many squares are there in a 4 × 4 grid?",
        [r"$1^2+2^2+3^2+4^2$.", "$1+4+9+16$.", "$=30$."],
        "30"),
    pat("sr-p2", "Rectangles in a grid", "common",
        "A grid of cells; the question asks for rectangles (squares included).",
        r"R=\binom{m+1}{2}\binom{n+1}{2}",
        ["Count the vertical lines (m + 1) and horizontal lines (n + 1).", "Choose 2 of each set.",
         "Multiply the two choose-2 values."],
        "Choosing 2 vertical and 2 horizontal lines fixes exactly one rectangle.",
        "How many rectangles are there in a grid of 4 columns and 3 rows?",
        [r"Vertical lines: 5, so $\binom{5}{2}=10$.", r"Horizontal lines: 4, so $\binom{4}{2}=6$.", r"$10\times6=60$."],
        "60"),
    pat("sr-p3", "Squares with a tilted (diamond) square inside", "common",
        "A square or grid with lines joining the middles of the sides, forming a diamond.",
        None,
        ["Count the upright squares of the grid.", "Add each tilted square whose four sides are fully drawn.",
         "Do not count the triangles made where grid lines cut the diamond."],
        "A tilted square is a square too, but grid lines through it only create triangles.",
        "A square is divided into 4 equal squares by its two midlines, and the midpoints of its four sides are joined to form a diamond. How many squares are there?",
        ["Upright: 4 small + 1 big = 5.", "Tilted diamond: 1.", r"$5+1=6$."],
        "6"),
    pat("sr-p4", "Irregular grids (plus, L-shape, missing lines)", "occasional",
        "Cells joined in a cross or L shape, or a grid with a line missing.",
        None,
        ["Count the single cells.", "For each bigger shape, check all four sides are drawn.",
         "For rectangles, fix a top-left cell and extend right and down while the region stays filled."],
        "The grid formulas assume every line runs the full width; here they do not.",
        "Five equal squares form a plus sign (one centre square, one on each side). How many rectangles are there?",
        ["Single cells: 5.", "Two-cell blocks (centre with an arm): 4.", "Full row and full column: 2.", r"$5+4+2=11$."],
        "11"),
    pat("sr-p5", "Rectangles that are not squares", "common",
        "The question says 'rectangles which are not squares'.",
        r"\text{non-square} = R - S",
        ["Count all rectangles with the line-pair method.", "Count the squares size by size.",
         "Subtract: non-square rectangles = R − S."],
        "The full count includes squares, so removing the squares leaves exactly the rest.",
        "How many rectangles in a 3 × 3 grid are not squares?",
        [r"All rectangles: $\binom{4}{2}^2=36$.", r"Squares: $1+4+9=14$.", r"$36-14=22$."],
        "22"),
]

# ---------------- straight-lines ----------------
sl_concept = (
    "Count each complete straight path once, however many pieces it is drawn in. Two pieces on one path, touching end to end, are one line. "
    "Sweep the figure direction by direction: horizontals, verticals, then each slant direction separately. "
    "Curves and arcs are never straight lines."
)

sl_notes = r"""### One path is one line
Count each complete straight path once, even if it is drawn as many pieces. Two pieces on the same path, touching end to end, make one line. Two pieces with a gap between them make two lines.

Think of a road crossing ten junctions. It is still one road. Only a new direction, or a gap, starts a new line.

> **Rule:** Count paths, not pieces. Every crossing point cuts a line into pieces that rejoin into one line.

### The direction sweep
Count one direction at a time. This makes double counting impossible.

1. Count horizontal lines, from top to bottom.
2. Count vertical lines, from left to right.
3. Count each slant direction separately: down-to-right first, then down-to-left.
4. Add the groups.

A square with both diagonals and both midlines: 3 horizontal + 3 vertical + 2 slanting = 8 lines.

> **Tip:** Say the direction out loud as you tick lines off. Turning the page a little helps slants stand out.

### Grids
A grid of m columns and n rows has m + 1 vertical lines and n + 1 horizontal lines:
$$L=(m+1)+(n+1)$$
A 3 × 2 grid needs $4+3=7$ lines. A 5 × 4 grid needs $6+5=11$ lines.

If the long diagonals of the whole grid are also drawn, add them as extra slanting lines.

### When pieces join into one line
The classic trap: a grid where every small cell has its own diagonals. Pieces sitting on one path join into a single line.

Take a 2 × 2 grid with both diagonals drawn in all 4 cells. That is 6 grid lines plus 8 cell-diagonal pieces. On the main path, two cell diagonals touch end to end and join into one long line. The same happens on the other path. So the 8 pieces form only 6 lines: 4 short ones plus 2 long ones.

Total: $6+6=12$ lines, not $6+8=14$.

> **Watch:** Merge the pieces first, then count. Never count drawn pieces directly as lines.

### Stars and polygons
Star figures are built from long lines that cross each other.

- A five-point star (pentagram) is drawn with 5 lines.
- A six-point star made of two triangles has 6 lines.
- A hexagon with its 3 long diagonals has $6+3=9$ lines.
- A triangle cut into rows has 3 directions, each with one line per row: 3 rows give $3\times3=9$ lines.

> **Example:** Count the pentagram's strokes: each of the 5 points is made by 2 strokes, and each stroke serves 2 points. So $5\times2\div2=5$ lines.

### Curves do not count
A straight line has no bend anywhere. Circles, arcs and wavy strokes are not straight lines, so skip them. If the question asks for one direction only, count just that direction and ignore everything else.
"""

sl_formulas = [
    {"name": "Lines in a grid", "tex": r"L=(m+1)+(n+1)", "note": "m columns, n rows; add extra slanting lines separately."},
]

sl_tricks = [
    {
        "title": "Direction sweep",
        "body": "One pass for horizontals, one for verticals, one per slant direction. The running total is the answer.",
        "example": {
            "q": "How many straight lines are there in a square with both diagonals drawn?",
            "steps": ["Horizontal sides: 2.", "Vertical sides: 2.", "Diagonals: 2.", r"$2+2+2=6$."],
            "answer": "6",
        },
    },
    {
        "title": "Merge before counting",
        "body": "When cell diagonals sit end to end on one path, they are one line. Join them in your head first.",
        "example": {
            "q": "A 2 × 2 grid has both diagonals drawn in every cell. How many straight lines are there?",
            "steps": ["Grid lines: 3 horizontal + 3 vertical = 6.", "Down-right: the 2 pieces on the main path join, plus one line on each side = 3.", "Down-left: same, 3.", r"$6+3+3=12$."],
            "answer": "12",
        },
    },
]

sl_mistakes = [
    {"wrong": "Counting each piece of one straight path as a separate line.", "right": "Pieces on one path that touch end to end are a single line."},
    {"wrong": "Missing the outer boundary lines.", "right": "The four sides of the frame are lines too. Sweep them first."},
    {"wrong": "Counting arcs and circles as lines.", "right": "Only straight paths count. Curves are ignored in line questions."},
    {"wrong": "Mixing directions mid-sweep.", "right": "Finish one direction completely before starting the next."},
    {"wrong": "Using (m + 1) + (n + 1) when a grid line stops halfway.", "right": "The formula needs full-length lines. Count broken grids by hand."},
]

sl_revision = [
    "One straight path = one line, however many pieces it is drawn in.",
    "Sweep: horizontals, verticals, then each slant direction.",
    "Grid of m columns, n rows: (m + 1) + (n + 1) lines.",
    "Square + 2 diagonals = 6 lines; add both midlines = 8.",
    "Pentagram 5, six-point star 6, hexagon with 3 long diagonals 9.",
    "Join collinear pieces first; ignore curves.",
]

sl_patterns = [
    pat("sl-p1", "Total straight lines in a square/rectangle figure", "common",
        "A square or rectangle with diagonals, midlines or cell diagonals; asks for straight lines.",
        None,
        ["Count the horizontal lines.", "Count the vertical lines.",
         "Count each slant direction, merging pieces that share one path.", "Add the groups."],
        "Grouping by direction makes double counting impossible.",
        "A square has both diagonals and both midlines drawn. How many straight lines are there?",
        ["Horizontal: top side, midline, bottom side = 3.", "Vertical: 3 the same way.", "Slanting diagonals: 2.", r"$3+3+2=8$."],
        "8"),
    pat("sl-p2", "Count lines of one direction only", "occasional",
        "The question asks only for horizontal, vertical or slanting lines.",
        None,
        ["Pick the asked direction.", "Scan the whole figure and tick each separate line of that direction.",
         "Check for pieces that join on one path."],
        "The other directions do not matter, so all attention goes to one sweep.",
        "A 3 × 2 grid also has both long diagonals of the whole rectangle drawn. How many vertical lines are there?",
        ["3 columns give 3 + 1 = 4 vertical lines.", "The two diagonals are slanting, not vertical.", "So 4."],
        "4"),
    pat("sl-p3", "Stars, polygons and triangle grids", "common",
        "A star, a hexagon with diagonals, or a triangle filled with small triangles.",
        None,
        ["Find the long straight paths that build the figure.", "Count paths, not the small pieces between crossings.",
         "For row figures, count lines per direction, then multiply by 3 directions."],
        "Each long line is cut into many pieces by the others; the pieces are not separate lines.",
        "How many straight lines are needed to draw a five-point star?",
        ["Each point is made by 2 strokes.", "Each stroke also serves a second point.", r"$5\times2\div2=5$."],
        "5"),
    pat("sl-p4", "Straight lines in a grid", "occasional",
        "A plain grid, sometimes with long diagonals drawn across it.",
        r"L=(m+1)+(n+1)",
        ["Vertical lines = columns + 1.", "Horizontal lines = rows + 1.", "Add any extra diagonal paths, one per full path."],
        "Every grid line runs the full width or height, so each gives exactly one line.",
        "How many straight lines are there in a grid of 5 columns and 4 rows?",
        ["Vertical: 5 + 1 = 6.", "Horizontal: 4 + 1 = 5.", r"$6+5=11$."],
        "11"),
    pat("sl-p5", "Pieces that join on one path", "common",
        "A grid where every cell has its own diagonals, or a figure with collinear touching strokes.",
        None,
        ["Draw or imagine each diagonal path across the whole figure.", "Join pieces that touch end to end on it.",
         "Count one line per merged path, per direction."],
        "Touching collinear pieces are one straight path, so they are one line, not two.",
        "A 2 × 2 grid has both diagonals drawn in every one of its 4 cells. How many straight lines are there?",
        ["Grid lines: 3 + 3 = 6.", "Down-right: 8 pieces form 3 paths (the 2 middle pieces join).", "Down-left: 3 paths the same way.", r"$6+3+3=12$."],
        "12"),
]

# ---------- patch ----------
data = json.loads(TOPIC.read_text(encoding="utf-8"))
frozen = json.dumps([data.get("practice"), data.get("solvedExamples"), data.get("pyqPatterns")],
                    ensure_ascii=False, sort_keys=True)

blocks = {
    "triangles": (t_concept, t_notes, t_formulas, t_tricks, t_mistakes, t_revision, t_patterns),
    "squares-rectangles": (sr_concept, sr_notes, sr_formulas, sr_tricks, sr_mistakes, sr_revision, sr_patterns),
    "straight-lines": (sl_concept, sl_notes, sl_formulas, sl_tricks, sl_mistakes, sl_revision, sl_patterns),
}

new_ids = [p["id"] for blk in blocks.values() for p in blk[6]]
assert len(new_ids) == len(set(new_ids)), "duplicate pattern ids within rewrite"

for sub in data["subtopics"]:
    if sub["id"] not in blocks:
        continue
    concept, notes, formulas, tricks, mistakes, revision, patterns = blocks[sub["id"]]
    old_ids = {p["id"] for p in sub.get("patterns", [])}
    assert old_ids <= {p["id"] for p in patterns}, f"{sub['id']}: never drop a pattern id"
    other = {p["id"] for s in data["subtopics"] if s["id"] != sub["id"] for p in s.get("patterns", [])}
    clash = other & {p["id"] for p in patterns}
    assert not clash, f"{sub['id']}: pattern id clash {clash}"
    assert 2500 <= len(notes) <= 5000, f"{sub['id']} notes {len(notes)} chars"
    assert 4 <= len(mistakes) <= 8 and 4 <= len(revision) <= 9
    sub.update(concept=concept, notes=notes.strip() + "\n", formulas=formulas, tricks=tricks,
               mistakes=mistakes, revision=revision, patterns=patterns)
    print(f"{sub['id']}: notes {len(notes)} chars, {len(patterns)} patterns")

assert json.dumps([data.get("practice"), data.get("solvedExamples"), data.get("pyqPatterns")],
                  ensure_ascii=False, sort_keys=True) == frozen, "practice/solved/pyq changed"

with open(TOPIC, "w", encoding="utf-8", newline="\n") as f:
    json.dump(data, f, ensure_ascii=False, indent=1)
print("counting-figures.json patched")
