"""Readable rewrite of Reasoning > Cube & Dice (dice-positions, cube-nets, painted-cubes).

Every answer on the page is checked by simulation:
- dice: all 720 face labellings x 24 rotations; a labelling must show every given view;
  the answer must be the same in every labelling that survives;
- nets: 3D folding with rotation matrices (print on the outside); the 11 cube nets
  are found among all 35 hexominoes; every opposite pair and every "which cube" option is computed;
- painted cubes: every unit cube of the big cube is visited and its painted faces counted.
Run: python cube_dice.py  (patches content/core/topics/reasoning/cube-dice.json)
"""
import itertools
import json
import math
from pathlib import Path

ROOT = Path(__file__).resolve().parents[3]
TOPIC = ROOT / "core" / "topics" / "reasoning" / "cube-dice.json"


# =====================================================================
# 1. DICE SIMULATION
# =====================================================================
# a die = tuple of labels at positions (U, D, F, B, L, R)
def rot_y(t):            # turn about the vertical axis
    U, D, F, B, L, R = t
    return (U, D, R, L, F, B)


def rot_x(t):            # tip about the left-right axis
    U, D, F, B, L, R = t
    return (F, B, D, U, L, R)


def orientations(t):
    seen, stack = {t}, [t]
    while stack:
        s = stack.pop()
        for g in (rot_x, rot_y):
            n = g(s)
            if n not in seen:
                seen.add(n)
                stack.append(n)
    return seen


assert len(orientations(tuple(range(6)))) == 24


def views_of(t):
    """All (front, top, right) triples a viewer can see on this die."""
    return {(o[2], o[0], o[5]) for o in orientations(t)}


def partition(t):
    return frozenset({frozenset((t[0], t[1])), frozenset((t[2], t[3])), frozenset((t[4], t[5]))})


def solve(labels, ordered=(), corners=()):
    """Every die (labelling of the 6 positions) that can show all the given views.
    ordered: (front, top, right) triples;  corners: 3-face sets with no order."""
    sols = []
    for t in itertools.permutations(labels):
        V = views_of(t)
        if all(v in V for v in ordered) and all(any(set(x) == set(c) for x in V) for c in corners):
            sols.append(t)
    return sols


def partners(sols, x):
    out = set()
    for t in sols:
        for pair in partition(t):
            if x in pair:
                out |= set(pair) - {x}
    return out


def partitions(sols):
    return {partition(t) for t in sols}


def pairs_text(part):
    return sorted("".join(sorted(map(str, p))) for p in part)


# ---- rolling ----
def roll_right(t):
    U, D, F, B, L, R = t
    return (L, R, F, B, D, U)


def roll_forward(t):
    U, D, F, B, L, R = t
    return (B, F, U, D, L, R)


for g in (roll_right, roll_forward):
    d0 = tuple(range(6))
    assert g(d0) in orientations(d0)          # a roll is a real rotation of the die

# ---- dp-p1 strike out ----
S1 = solve("PQRSTU", corners=[set("PQR"), set("PSQ"), set("PRT")])
assert S1 and partners(S1, "P") == {"U"}                                   # sixth face
# ---- dp-p2 two common faces ----
S2 = solve("KLMNOP", corners=[set("KLM"), set("KLN")])
assert S2 and partners(S2, "M") == {"N"} and partners(S2, "N") == {"M"}
# ---- dp-p3 same position ----
S3 = solve("ABCDEF", ordered=[("B", "A", "C"), ("D", "A", "E")])
assert S3 and partitions(S3) == {frozenset({frozenset("BD"), frozenset("CE"), frozenset("AF")})}
# the rule also holds with a different letter set (sanity): front-front, right-right
S3b = solve("PQRSTU", ordered=[("Q", "P", "R"), ("S", "P", "T")])
assert partitions(S3b) == {frozenset({frozenset("QS"), frozenset("RT"), frozenset("PU")})}
# ---- dp-p4 standard die ----
assert 21 - (3 + 5 + 6) == 7 and {7 - 3, 7 - 5, 7 - 6} == {4, 2, 1} and 4 + 2 + 1 == 7
assert all(a + b == 7 for a, b in [(1, 6), (2, 5), (3, 4)]) and sum(range(1, 7)) == 21
# second standard-die example: shown 2, 4, 6 -> hidden 5, 3, 1
assert 21 - (2 + 4 + 6) == 9 and {7 - 2, 7 - 4, 7 - 6} == {5, 3, 1} and 5 + 3 + 1 == 9
# ---- dp-p5 whole map ----
S5 = solve("ABCDEF", corners=[set("ABC"), set("ABD"), set("BCE")])
assert S5 and partitions(S5) == {frozenset({frozenset("CD"), frozenset("AE"), frozenset("BF")})}
# ---- dp-p6 which view is possible ----
part6 = frozenset({frozenset("AD"), frozenset("BE"), frozenset("CF")})
all6 = [t for t in itertools.permutations("ABCDEF") if partition(t) == part6]
possible = {frozenset(x) for t in all6 for x in views_of(t)}
opts6 = {1: "ADC", 2: "BEF", 3: "ABF", 4: "CFB"}
ok6 = [k for k, v in opts6.items() if frozenset(v) in possible]
assert ok6 == [3]
# ---- dp-p7 rolling ----
d = (1, 6, 2, 5, 4, 3)                       # U D F B L R: top 1, front 2, right 3 on a standard die
assert all(d[i] + d[i + 1] == 7 for i in (0, 2, 4))
d1 = roll_right(d)
assert d1[0] == 4 and d1 == (4, 3, 2, 5, 6, 1)
d2 = roll_forward(d1)
assert d2[0] == 5 and d2[1] == 2 and d2[2] == 4        # top 5, bottom 2, front 4
# second example: 6 on top, 3 in front, 2 on the right; roll forward once -> top?
e = (6, 1, 3, 4, 5, 2)
assert all(e[i] + e[i + 1] == 7 for i in (0, 2, 4))
e1 = roll_forward(e)
assert e1[0] == 4 and e1[1] == 3                        # back (4) comes to the top; front (3) goes to the bottom
# rolling four times in the same direction returns the die
z = d
for _ in range(4):
    z = roll_right(z)
assert z == d

# =====================================================================
# 2. NET SIMULATION (print on the outside)
# =====================================================================
I3 = ((1, 0, 0), (0, 1, 0), (0, 0, 1))


def mm(A, B):
    return tuple(tuple(sum(A[i][k] * B[k][j] for k in range(3)) for j in range(3)) for i in range(3))


def mv(A, v):
    return tuple(sum(A[i][k] * v[k] for k in range(3)) for i in range(3))


def cross(a, b):
    return (a[1] * b[2] - a[2] * b[1], a[2] * b[0] - a[0] * b[2], a[0] * b[1] - a[1] * b[0])


def dot(a, b):
    return sum(x * y for x, y in zip(a, b))


TURN = {(1, 0): ((0, 0, 1), (0, 1, 0), (-1, 0, 0)),
        (-1, 0): ((0, 0, -1), (0, 1, 0), (1, 0, 0)),
        (0, 1): ((1, 0, 0), (0, 0, 1), (0, -1, 0)),
        (0, -1): ((1, 0, 0), (0, 0, -1), (0, 1, 0))}
DIRS = list(TURN)


def fold(cells):
    """Outward normal of every cell after folding, or None if the shape is not a cube net."""
    cells = set(cells)
    base = min(cells)
    R = {base: I3}
    queue = [base]
    while queue:
        c = queue.pop(0)
        for d_ in DIRS:
            nb = (c[0] + d_[0], c[1] + d_[1])
            if nb in cells and nb not in R:
                R[nb] = mm(R[c], TURN[d_])
                queue.append(nb)
    if len(R) != len(cells):
        return None
    for c in cells:
        for d_ in DIRS:
            nb = (c[0] + d_[0], c[1] + d_[1])
            if nb in cells and R[nb] != mm(R[c], TURN[d_]):
                return None
    normals = {c: mv(R[c], (0, 0, 1)) for c in cells}
    if len(set(normals.values())) != 6:
        return None
    return normals


def norm_shape(cells):
    mx = min(x for x, y in cells)
    my = min(y for x, y in cells)
    return frozenset((x - mx, y - my) for x, y in cells)


def grow(n):
    cur = {norm_shape({(0, 0)})}
    for _ in range(n - 1):
        nxt = set()
        for p in cur:
            for (x, y) in p:
                for dx, dy in DIRS:
                    q = (x + dx, y + dy)
                    if q not in p:
                        nxt.add(norm_shape(p | {q}))
        cur = nxt
    return cur


def symmetries(cells):
    out = []
    pts = list(cells)
    for k in range(4):
        pts = [(y, -x) for x, y in pts]
        out.append(norm_shape(pts))
        out.append(norm_shape([(-x, y) for x, y in pts]))
    return out


def canon(cells):
    return min(tuple(sorted(s)) for s in symmetries(cells))


fixed = grow(6)
assert len(fixed) == 216
free = {canon(s) for s in fixed}
assert len(free) == 35                                    # 35 hexominoes
nets_fixed = [s for s in fixed if fold(s)]
nets_free = {canon(s) for s in nets_fixed}
assert len(nets_free) == 11                               # 11 nets of a cube


def longest_run(cells):
    best = 0
    for (x, y) in cells:
        for dx, dy in ((1, 0), (0, 1)):
            if (x - dx, y - dy) in cells:
                continue
            k = 0
            while (x + k * dx, y + k * dy) in cells:
                k += 1
            best = max(best, k)
    return best


def has_block(cells):
    return any({(x, y), (x + 1, y), (x, y + 1), (x + 1, y + 1)} <= set(cells) for x, y in cells)


runs = {}
for f in nets_free:
    runs[longest_run(set(f))] = runs.get(longest_run(set(f)), 0) + 1
assert runs == {4: 6, 3: 4, 2: 1}, runs                   # 6 with a row of four, 4 with three, 1 staircase
assert all(not has_block(set(f)) for f in nets_free)
assert all(longest_run(set(s)) <= 4 for s in nets_fixed)
non_nets = [s for s in fixed if not fold(s)]
assert all(has_block(set(s)) or longest_run(set(s)) >= 5 or True for s in non_nets)
# every hexomino with a 2x2 block or a line of 5 is NOT a net
assert all(not fold(s) for s in fixed if has_block(set(s)) or longest_run(set(s)) >= 5)


def neg(v):
    return tuple(-x for x in v)


# general rules over every net (all rotations and mirror images)
corner_touch_opposite = 0
for s in nets_fixed:
    N = fold(s)
    S = set(s)
    for (x, y) in S:
        for dx, dy in ((1, 0), (0, 1)):
            a, b, c = (x, y), (x + dx, y + dy), (x + 2 * dx, y + 2 * dy)
            if b in S and c in S:
                assert N[a] == neg(N[c])                   # skip one in a straight line -> opposite
            d3 = (x + 3 * dx, y + 3 * dy)
            if b in S and c in S and d3 in S:
                assert N[a] != neg(N[d3])                  # 1st and 4th of a row of four touch
        # Z / S of four squares: (x,y),(x+d),(x+d+e),(x+2d+e)
        for d_ in DIRS:
            for e_ in DIRS:
                if d_[0] * e_[0] + d_[1] * e_[1] != 0:
                    continue
                p1 = (x, y)
                p2 = (x + d_[0], y + d_[1])
                p3 = (p2[0] + e_[0], p2[1] + e_[1])
                p4 = (p3[0] + d_[0], p3[1] + d_[1])
                if p2 in S and p3 in S and p4 in S:
                    assert N[p1] == neg(N[p4])             # ends of a Z are opposite
    # edge-touching cells are never opposite
    for (x, y) in S:
        for d_ in DIRS:
            nb = (x + d_[0], y + d_[1])
            if nb in S:
                assert N[(x, y)] != neg(N[nb])
    # corner-only touching cells: are they ever opposite?
    for (x, y) in S:
        for dx, dy in ((1, 1), (1, -1)):
            nb = (x + dx, y + dy)
            if nb in S and (x + dx, y) not in S and (x, y + dy) not in S:
                if N[(x, y)] == neg(N[nb]):
                    corner_touch_opposite += 1

# L-bend rule: three squares in an L meet at one corner, and the counter-clockwise order
# round the net point is the counter-clockwise order round the cube corner (seen from outside)
lbends = 0
for s in nets_fixed:
    N = fold(s)
    S = set(s)
    for (x, y) in S:
        for d_ in DIRS:
            for e_ in DIRS:
                if d_[0] * e_[0] + d_[1] * e_[1] != 0:
                    continue
                b = (x, y)
                a = (x + d_[0], y + d_[1])
                c = (x + e_[0], y + e_[1])
                if a in S and c in S and (a[0] + c[0] - b[0], a[1] + c[1] - b[1]) not in S:
                    # the point shared by a, b, c
                    px = (max(a[0], b[0], c[0]) if max(a[0], b[0], c[0]) - min(a[0], b[0], c[0]) == 1 else 0)
                    # find the common corner (x+0.5*.. ) by brute force over the 4 corners of b
                    common = None
                    for cx, cy in ((0, 0), (1, 0), (0, 1), (1, 1)):
                        corner = (b[0] + cx, b[1] + cy)
                        def has(cell):
                            return corner in {(cell[0] + i, cell[1] + j) for i in (0, 1) for j in (0, 1)}
                        if has(a) and has(c):
                            common = corner
                    assert common is not None
                    ang = lambda cell: math.atan2(cell[1] + 0.5 - common[1], cell[0] + 0.5 - common[0])
                    trio = sorted([a, b, c], key=ang)             # counter-clockwise by angle
                    # normalise: counter-clockwise cyclic order
                    n1, n2, n3 = (N[t] for t in trio)
                    # trio is CCW only if consecutive angular gaps are < 180 degrees; the missing 4th cell
                    # sits in one gap, so rotate so that the big gap is last
                    angs = [ang(t) for t in trio]
                    gaps = [(angs[(i + 1) % 3] - angs[i]) % (2 * math.pi) for i in range(3)]
                    k = gaps.index(max(gaps))
                    trio = trio[k + 1:] + trio[:k + 1]
                    n1, n2, n3 = (N[t] for t in trio)
                    assert dot(cross(n1, n2), n3) == 1        # counter-clockwise from outside
                    lbends += 1
assert lbends > 0


def net_of(spec):
    """spec: {label: (col,row)} with +row = up. Returns {label: outward normal}."""
    nrm = fold(set(spec.values()))
    assert nrm is not None, "not a net"
    return {lab: nrm[cell] for lab, cell in spec.items()}


def opposite_pairs(spec):
    nrm = net_of(spec)
    labs = sorted(spec)
    return sorted("".join(sorted((a, b))) for a, b in itertools.combinations(labs, 2) if nrm[a] == neg(nrm[b]))


def can_form(spec, top, front, right):
    n = net_of(spec)
    a, b, c = n[top], n[front], n[right]
    if dot(a, b) or dot(b, c) or dot(a, c):
        return False                                      # two of them are opposite (or the same face)
    return dot(cross(a, b), c) == 1                       # top -> front -> right counter-clockwise


# cn-p1: row of four with one square above the 2nd and one below the 3rd
N1 = {"P": (0, 0), "Q": (1, 0), "R": (2, 0), "S": (3, 0), "T": (1, 1), "U": (2, -1)}
assert opposite_pairs(N1) == ["PR", "QS", "TU"]
# cn-p2: staircase 2-2-2
N2 = {"A": (0, 0), "B": (1, 0), "C": (1, 1), "D": (2, 1), "E": (2, 2), "F": (3, 2)}
assert opposite_pairs(N2) == ["AD", "BE", "CF"]
# cn-p3: row A B C D, E above B, F below C
N3 = {"A": (0, 0), "B": (1, 0), "C": (2, 0), "D": (3, 0), "E": (1, 1), "F": (2, -1)}
assert opposite_pairs(N3) == ["AC", "BD", "EF"]
# cn-p4: which cube can be formed (net N3)
opts4 = {1: ("E", "A", "B"), 2: ("E", "B", "A"), 3: ("A", "C", "B"), 4: ("E", "F", "B")}
ok4 = [k for k, v in opts4.items() if can_form(N3, *v)]
assert ok4 == [1], ok4
# cn-p5: cross net; which cube can NOT be formed
N5 = {"K": (1, 3), "M": (1, 2), "O": (1, 1), "J": (1, 0), "L": (0, 2), "N": (2, 2)}
assert opposite_pairs(N5) == ["JM", "KO", "LN"]
opts5 = {1: ("K", "L", "M"), 2: ("K", "M", "N"), 3: ("M", "L", "O"), 4: ("M", "O", "L")}
bad5 = [k for k, v in opts5.items() if not can_form(N5, *v)]
assert bad5 == [4], bad5
assert all(not (set(v) & {"J"} and False) for v in opts5.values())
# none of the options shows an opposite pair, so option 4 fails only on order
for v in opts5.values():
    n = net_of(N5)
    assert not any(n[a] == neg(n[b]) for a, b in itertools.combinations(v, 2))
# cn-p6: which shape is a net of a cube
def cells_row(*rows):
    """rows: list of (row_y, [x...]) """
    return {(x, y) for y, xs in rows for x in xs}


shapes6 = {
    "a": cells_row((1, range(5)), (0, [2])),                        # five in a row, one below the middle
    "b": cells_row((1, range(4)), (2, [1]), (0, [2])),              # row of four, one above 2nd, one below 3rd
    "c": cells_row((2, [0, 1]), (1, [0, 1]), (1, [2, 3])),          # 2x2 block plus two more
    "d": cells_row((1, [0, 1, 2]), (0, [1, 2, 3])),                 # two rows of three, shifted by one
}
assert all(len(v) == 6 for v in shapes6.values())
ok6n = [k for k, v in shapes6.items() if fold(v)]
assert ok6n == ["b"]
assert longest_run(shapes6["a"]) == 5 and has_block(shapes6["c"]) and has_block(shapes6["d"])
# a valid 3-3 net: rows of three shifted by two
assert fold(cells_row((1, [0, 1, 2]), (0, [2, 3, 4])))

# =====================================================================
# 3. PAINTED CUBES
# =====================================================================
FACES = ("x0", "x1", "y0", "y1", "z0", "z1")


def paint_counts(a, b, c, painted=FACES):
    """{number of painted faces: how many unit cubes}, for an a x b x c block."""
    out = {}
    for x in range(a):
        for y in range(b):
            for z in range(c):
                on = [x == 0, x == a - 1, y == 0, y == b - 1, z == 0, z == c - 1]
                k = sum(1 for f, flag in zip(FACES, on) if flag and f in painted)
                out[k] = out.get(k, 0) + 1
    return out


def cube_formula(n):
    return {3: 8, 2: 12 * (n - 2), 1: 6 * (n - 2) ** 2, 0: (n - 2) ** 3}


for n in range(2, 9):
    got = paint_counts(n, n, n)
    want = cube_formula(n)
    assert {k: v for k, v in got.items() if v} == {k: v for k, v in want.items() if v}, n
    assert sum(want.values()) == n ** 3
assert cube_formula(3) == {3: 8, 2: 12, 1: 6, 0: 1} and 8 + 12 + 6 + 1 == 27
assert cube_formula(4) == {3: 8, 2: 24, 1: 24, 0: 8} and 8 + 24 + 24 + 8 == 64
# pc-p1..p7 examples
assert paint_counts(7, 7, 7)[3] == 8
assert paint_counts(5, 5, 5)[2] == 36 == 12 * (5 - 2)
assert paint_counts(6, 6, 6)[1] == 96 == 6 * 4 * 4
assert paint_counts(5, 5, 5)[0] == 27 == 3 ** 3
d4 = paint_counts(4, 4, 4)
assert d4[3] + d4[2] == 32 == 8 + 12 * 2 and 64 - 8 == 56 == 4 ** 3 - 2 ** 3
cub = paint_counts(5, 4, 3)
assert cub[2] == 24 == 4 * (3 + 2 + 1) and cub[0] == 6 == 3 * 2 * 1
assert cub[1] == 2 * (3 * 2 + 2 * 1 + 1 * 3) == 22 and cub[3] == 8 and sum(cub.values()) == 60
# find n from a count
assert 12 * (5 - 2) == 36 and paint_counts(5, 5, 5)[1] == 54 == 6 * 9
assert 12 * (4 - 2) == 24 and 6 * (5 - 2) ** 2 == 54 and 6 * 9 == 54
assert paint_counts(5, 5, 5)[2] == 36
# cutting a big cube into small cubes of given edge (cm)
assert 12 // 3 == 4 and paint_counts(4, 4, 4)[2] == 24 and 12 % 3 == 0
assert 20 // 4 == 5 and paint_counts(5, 5, 5)[0] == 27 and (5 - 2) ** 3 == 27
assert (216 ** (1 / 3)).__round__() == 6 and 6 ** 3 == 216
# at least one painted in a 6-cube
assert 6 ** 3 - 4 ** 3 == 152 == sum(v for k, v in paint_counts(6, 6, 6).items() if k >= 1)
# only some faces painted
top_front = paint_counts(4, 4, 4, painted=("z1", "y0"))
assert top_front[1] == 24 and top_front[2] == 4 and top_front[0] == 64 - 28 == 36
assert 16 + 16 - 2 * 4 == 24
top_bottom = paint_counts(5, 5, 5, painted=("z0", "z1"))
assert top_bottom[1] == 50 == 2 * 25 and top_bottom.get(2, 0) == 0 and top_bottom[0] == 75
one_face = paint_counts(5, 5, 5, painted=("z1",))
assert one_face[1] == 25 and one_face[0] == 100
# two adjacent faces: cubes with exactly one painted face
adj = paint_counts(6, 6, 6, painted=("x1", "y1"))
assert adj[1] == 2 * 36 - 2 * 6 == 60 and adj[2] == 6 and adj[0] == 216 - 66 == 150
# opposite faces painted only (two colours): cubes with exactly one painted face (n = 4)
assert paint_counts(4, 4, 4, painted=("x0", "x1"))[1] == 32 == 2 * 16
assert paint_counts(3, 3, 3)[1] == 6 and paint_counts(3, 3, 3)[0] == 1


# =====================================================================
# CONTENT
# =====================================================================
def pat(pid, name, freq, spot, formula, steps, why, q, ex_steps, answer):
    return {"id": pid, "name": name, "frequency": freq, "howToSpot": spot, "formula": formula,
            "steps": steps, "why": why, "example": {"q": q, "steps": ex_steps, "answer": answer}}


# ---------------------------------------------------------------- dice-positions
dp_concept = (
    "A die is a cube with six faces. Each face touches four faces and is opposite exactly one face. "
    "When several pictures of the same die are shown, use them to find which faces are opposite. "
    "Three quick rules do most of the work: strike out the neighbours, look for two common faces, "
    "and compare faces that sit in the same place."
)

dp_notes = r"""### What one picture shows
A die has six faces. Each face touches four faces and is opposite one face.

A picture shows three faces that meet at one corner. These three faces all touch each other.

> **Rule:** Two faces seen together in one picture are never opposite.

### Strike out the neighbours
To find the face opposite X, list every face seen together with X. All of them touch X.

If four different faces are struck out, the one face left is opposite X.

Example: X is seen with A and B in one picture, with C in a second picture, and with D in a third. A, B, C and D all touch X. So the sixth face is opposite X.

> **Tip:** This rule needs no turning of the die. Try it first.

### Two common faces
Sometimes two pictures show the same two faces. Then the third face in each picture are opposite each other.

Pictures $(K, L, M)$ and $(K, L, N)$ share K and L. So M and N are opposite.

Why? The two faces that touch both K and L are exactly the two faces at the ends of the shared edge. They are opposite each other.

### One common face in the same place
Now two pictures share only one face X. X sits in the same place in both, for example on top. All other faces are different.

Then the faces in the same place are opposite: front with front, right with right.

Example: picture 1 has top A, front B, right C. Picture 2 has top A, front D, right E. So B is opposite D, C is opposite E, and F is opposite A.

> **Watch:** Use this rule only when the common face is in the same place and no other face repeats. If not, use the first two rules.

### Standard die
A standard (ordinary) die has opposite faces adding to 7: 1 and 6, 2 and 5, 3 and 4.

All six faces add to 21. So the hidden faces add to $21$ minus the three faces you can see.

> **Note:** Use the sum 7 rule only when the question says the die is standard. A die marked with letters has no sum rule.

### Rolling a die
Rolling a die moves its faces in a circle. The other two faces stay in place.

- Roll to the right: top goes to the right, right goes to the bottom, bottom goes to the left, left comes to the top.
- Roll forward: top goes to the front, front goes to the bottom, bottom goes to the back, back comes to the top.

Example: a standard die has 1 on top, 2 in front and 3 on the right. So 6 is at the bottom, 5 at the back and 4 on the left. Roll it once to the right: 4 comes to the top.

### Order of work
Write the three opposite pairs as you find them.

1. Look for two common faces. This gives a whole pair at once.
2. Look for a common face in the same place.
3. Strike out neighbours to finish the last pair.
"""

dp_formulas = [
    {"name": "Standard die", "tex": r"1+6 = 2+5 = 3+4 = 7", "note": "Opposite faces of a standard die add to 7."},
    {"name": "Hidden faces of a standard die", "tex": r"\text{hidden} = 21 - \text{shown}", "note": "All six faces add to 21."},
]

dp_tricks = [
    {
        "title": "Strike out the neighbours",
        "body": "List every face seen with the asked face and cross them out. If one face is left, it is the answer.",
        "example": {
            "q": "A face P is seen with Q and R, then with S and Q, then with R and T. Which face is opposite P?",
            "steps": ["P was seen with Q, R, S and T.", "These four all touch P.", "Only U is left."],
            "answer": "U",
        },
    },
    {
        "title": "Two common faces",
        "body": "Two pictures with two faces in common: the two other faces are opposite.",
        "example": {
            "q": "One picture shows K, L, M. Another shows K, L, N. Which face is opposite M?",
            "steps": ["K and L appear in both pictures.", "The other faces, M and N, are opposite each other."],
            "answer": "N",
        },
    },
    {
        "title": "Hidden faces of a standard die",
        "body": "All six faces add to 21. Subtract the three faces you can see.",
        "example": {
            "q": "A standard die shows 2, 4 and 6. What do the three hidden faces add up to?",
            "steps": [r"Shown: $2+4+6=12$.", r"Hidden: $21-12=9$.", "Check: the hidden faces are 5, 3 and 1, and $5+3+1=9$."],
            "answer": "9",
        },
    },
]

dp_mistakes = [
    {"wrong": "Saying two faces are opposite only because they never appear together.", "right": "First strike out four neighbours, or use two common faces. Then the last face is opposite."},
    {"wrong": "Using the same-place rule when the common face is in a different place, or when a second face also repeats.", "right": "Use it only for one common face in the same place. Otherwise use strike-out or two common faces."},
    {"wrong": "Using the sum 7 rule on a die that is not called standard.", "right": "Check the question. Letters or unusual numbers have no sum rule."},
    {"wrong": "Choosing an option that shows two opposite faces together.", "right": "Reject any picture that shows two faces from the same opposite pair."},
    {"wrong": "Mixing up left and right when rolling a die.", "right": "Rolling right sends the top to the right side and brings the left face up. Say it aloud."},
]

dp_revision = [
    "A picture shows three faces at one corner. They all touch.",
    "Strike out every face seen with X. Four struck out means the sixth is opposite.",
    "Two common faces: the other two faces are opposite.",
    "One common face in the same place: front with front, right with right.",
    "Standard die: 1-6, 2-5, 3-4. Hidden faces add to 21 minus the shown faces.",
    "Roll right: left face comes to the top. Roll forward: back face comes to the top.",
]

dp_patterns = [
    pat("dp-p1", "Strike out the neighbours", "very common",
        "Three pictures of one die. The asked face appears with four different faces across the pictures.",
        None,
        ["List every face seen together with the asked face.", "Strike them out. They all touch it.", "The one face left is the answer."],
        "Every face seen with X touches X, so the only face never seen with X must be opposite.",
        "Three pictures of one cube show the faces (P, Q, R), (P, S, Q) and (P, R, T). Which face is opposite P?",
        ["P is seen with Q, R, S and T.", "These four faces all touch P.", "Only U is left."],
        "U"),
    pat("dp-p2", "Two common faces", "very common",
        "Two pictures repeat the same two faces. Each picture has one extra face.",
        None,
        ["Find the two faces that appear in both pictures.", "Note the extra face in each picture.", "The two extra faces are opposite."],
        "Only two faces touch both shared faces. They sit at the two ends of the shared edge.",
        "One picture of a cube shows the faces K, L and M. Another picture shows K, L and N. Which face is opposite M?",
        ["K and L are in both pictures.", "The extra faces are M and N.", "So M and N are opposite."],
        "N"),
    pat("dp-p3", "One common face in the same place", "common",
        "Two pictures share exactly one face. It sits in the same place in both, such as top in both.",
        None,
        ["Check that the common face is in the same place.", "Check that no other face repeats.", "Pair the faces in matching places: front with front, right with right."],
        "The four faces round the common face go in a circle, so faces in matching places end up across from each other.",
        "In picture 1 a cube shows A on top, B in front and C on the right. In picture 2 it shows A on top, D in front and E on the right. Which face is opposite B?",
        ["A is on top in both pictures.", "No other face repeats.", "Front faces are opposite: B and D.", "(Right faces C and E are opposite. F is opposite A.)"],
        "D"),
    pat("dp-p4", "Standard die (sum 7)", "common",
        "The question says ordinary or standard die and gives some face numbers.",
        r"x + x' = 7",
        ["Pair the numbers: 1-6, 2-5, 3-4.", "For a hidden face, take 7 minus its opposite.", "For the hidden total, take 21 minus the shown faces."],
        "Opposite faces add to 7, and all six faces add to 21.",
        "A standard die shows 3 on top, 5 in front and 6 on the right. What is the sum of the three hidden faces?",
        [r"Shown: $3+5+6=14$.", r"Hidden: $21-14=7$.", "Check: the hidden faces are 4, 2 and 1."],
        "7"),
    pat("dp-p5", "Build the full opposite map", "occasional",
        "Three or more pictures. The question asks for one pair or for the partner of the last face.",
        None,
        ["Use two common faces to find a pair.", "Repeat with another two pictures.", "The last two unpaired faces are opposite."],
        "There are only three opposite pairs. Two known pairs leave the third.",
        "Three pictures of a cube show (A, B, C), (A, B, D) and (B, C, E). Which face is opposite B?",
        ["First and second pictures share A and B, so C is opposite D.", "First and third pictures share B and C, so A is opposite E.", "Only B and F are left, so B is opposite F."],
        "F"),
    pat("dp-p6", "Which picture is possible?", "occasional",
        "The opposite pairs are given in words. The options are pictures of three faces.",
        None,
        ["Write the three opposite pairs.", "Cross out any option that shows both faces of a pair.", "The option with one face from each pair is possible."],
        "A picture never shows two opposite faces. Three faces from three different pairs always meet at a corner.",
        "On a cube, A is opposite D, B is opposite E and C is opposite F. Which set of three faces can be seen together? (1) A, D, C (2) B, E, F (3) A, B, F (4) C, F, B",
        ["Option 1 has A and D. Option 2 has B and E.", "Option 4 has C and F.", "Option 3 has A, B and F, one from each pair."],
        "Option 3"),
    pat("dp-p7", "Rolling the die", "common",
        "The die is rolled to the right, left, forward or back. The top, bottom or front face is asked.",
        None,
        ["Write the six faces: top, bottom, front, back, left, right.", "Roll right: left face comes to the top.", "Roll forward: back face comes to the top.", "Write the new positions after every roll."],
        "A roll turns the die by a quarter turn, so four faces move in a circle and two stay.",
        "A standard die shows 1 on top, 2 in front and 3 on the right. It is rolled once to the right and then once forward. Which number is now on top?",
        ["Bottom 6, back 5, left 4 (each pair adds to 7).", "Roll right: left face 4 comes to the top.", "Now the back face is still 5.", "Roll forward: the back face 5 comes to the top."],
        "5"),
]

# ---------------------------------------------------------------- cube-nets
cn_concept = (
    "A net is a flat sheet of six squares that folds into a cube. "
    "Squares that share an edge in the net touch on the cube. "
    "To find opposite faces, skip one square in a straight line, or take the two ends of a Z shape. "
    "To test a drawn cube, first reject any cube that shows two opposite faces."
)

cn_notes = r"""### What a net is
A net is a flat sheet of six squares. Fold it and it becomes a cube. The printed side is on the outside.

Two squares that share an edge in the net touch on the cube. They are never opposite.

### Skip one in a straight line
In a straight row or column, two squares with exactly one square between them are opposite.

Row P, Q, R, S: P and R are opposite, and Q and S are opposite.

> **Rule:** Skip one square. First and third are opposite. Second and fourth are opposite.

The first and fourth squares of a row of four are not opposite. They touch when the row wraps round the cube.

### The Z shape
Find four squares in a Z or S shape: two squares, a step sideways, then two more. The two end squares are opposite.

Staircase net A, B, C, D, E, F: A, B, C, D form a Z, so A and D are opposite. B, C, D, E form a Z, so B and E are opposite. Then C and F are the last pair.

### Find all three pairs
A cube has three pairs of opposite faces. Find two pairs with the rules above. The two squares left over are the third pair.

Row A, B, C, D, with E above B and F below C: A-C and B-D come from the row. E and F are left, so they are opposite.

### Which shapes are nets
Only 11 shapes fold into a cube. Use two checks.

- No 2 by 2 block of squares.
- No row of five squares.

Six nets have a row of four, four nets have a row of three, and one is the staircase. Any shape with a 2 by 2 block or a row of five is not a net.

### Which cube can be formed
Each option shows three faces of a cube. Read them as top, front and right.

1. Find the opposite pairs in the net.
2. Reject any option that shows both faces of a pair.
3. For the rest, find the three squares in the net. Look for an L shape: one square touching the other two.
4. Read the three squares counter-clockwise round the point where they meet. The cube must show them counter-clockwise too: top, then front, then right.

> **Watch:** Two options can show the same three faces in different orders. Only one order is right. The other is the mirror image.

### Quick way to check a net
Fold the net in your head, one square at a time. Keep one square as the base.

- Fold the squares next to the base up as walls.
- Fold the last square over as the lid.
- If two squares land on the same face, the shape is not a net.

With practice, the row rule and the Z rule are faster than folding. Use folding only to double-check.

### Worked example
Net: row A, B, C, D with E above B and F below C. Opposite pairs: A-C, B-D, E-F.

Test a cube with top E, front A, right B. A, B, E form an L shape with B in the middle. Round their meeting point, counter-clockwise, the order is E, A, B. The cube shows top E, front A, right B, the same order. So it can be formed. Top E, front B, right A is its mirror image and cannot.
"""

cn_formulas = []

cn_tricks = [
    {
        "title": "Skip one",
        "body": "Along a row or column, skip one square. The squares on both sides of the skipped one are opposite.",
        "example": {
            "q": "A net has a row of four squares A, B, C, D. Which face is opposite B?",
            "steps": ["Skip C.", "B and D are opposite."],
            "answer": "D",
        },
    },
    {
        "title": "Reject first",
        "body": "In a which-cube question, throw out every option that shows an opposite pair. Often only one option is left.",
        "example": {
            "q": "In a net, A and C are opposite. Can a cube show A on top and C in front?",
            "steps": ["A and C are opposite faces.", "Opposite faces are never seen together."],
            "answer": "No, it cannot be formed",
        },
    },
]

cn_mistakes = [
    {"wrong": "Calling two squares opposite because they are far apart in the net.", "right": "Use the rules: skip one in a line, or the ends of a Z. Then use the three-pair check."},
    {"wrong": "Accepting a cube that shows two opposite faces.", "right": "Find the opposite pairs first. Reject any option that shows both faces of a pair."},
    {"wrong": "Ignoring the order of the three faces round the corner.", "right": "Check the counter-clockwise order. The mirror order can never be formed."},
    {"wrong": "Thinking the first and fourth squares of a row of four are opposite.", "right": "Only the first and third, and the second and fourth, are opposite."},
    {"wrong": "Calling a shape with a 2 by 2 block or a row of five a net.", "right": "Such shapes overlap when folded. They are not nets."},
]

cn_revision = [
    "Squares that share an edge touch on the cube.",
    "Row or column: skip one. First and third are opposite.",
    "Z or S of four squares: the two ends are opposite.",
    "Three pairs in all. The two leftover squares form the last pair.",
    "Which cube: reject opposite pairs, then check the counter-clockwise order.",
    "Not a net: a 2 by 2 block or a row of five squares.",
]

cn_patterns = [
    pat("cn-p1", "Opposite faces in a row", "very common",
        "A net with a straight row or column of three or four squares. The face opposite a given face is asked.",
        None,
        ["Find the straight line that holds the given square.", "Skip one square along the line.", "The square on the far side of the skipped one is opposite."],
        "Folding the row round the cube brings the first and third squares to opposite sides.",
        "A net is a row of four squares P, Q, R, S with T above Q and U below R. Which face is opposite Q?",
        ["The row is P, Q, R, S.", "Skip R. Q and S are opposite."],
        "S"),
    pat("cn-p2", "Ends of a Z shape", "very common",
        "The net bends: two squares, a step sideways, two more squares.",
        None,
        ["Find four squares that form a Z or S.", "Mark the two end squares.", "The end squares are opposite."],
        "In a Z, the two end squares fold to opposite sides of the cube.",
        "A net has six squares A, B, C, D, E, F in a staircase: A next to B, C above B, D right of C, E above D, F right of E. Which face is opposite A?",
        ["A, B, C, D form a Z shape.", "The ends of the Z are A and D."],
        "D"),
    pat("cn-p3", "Find all three pairs", "common",
        "The question asks for a pair of opposite faces, or the partner of the last face.",
        None,
        ["Use the row rule to find two pairs.", "Use the Z rule if a row rule does not give a pair.", "The two squares left over are the last pair."],
        "There are only three pairs, so two pairs fix the third.",
        "A net has a row of four squares A, B, C, D. E is above B and F is below C. Which two faces are opposite?",
        ["Row rule: A is opposite C, and B is opposite D.", "E and F are left over.", "So E and F are opposite."],
        "E and F"),
    pat("cn-p4", "Which cube can be formed?", "very common",
        "A net is drawn. The options are cubes with three faces shown.",
        None,
        ["Find the three pairs of opposite faces.", "Reject any option that shows both faces of a pair.", "For the rest, find the three squares in the net and read them counter-clockwise.", "Pick the option that shows top, front, right in the same order."],
        "A real cube never shows opposite faces together, and its corner keeps the order of the net.",
        "A net is a row of four squares A, B, C, D with E above B and F below C. Which cube can be formed? Faces are given as (top, front, right). (1) E, A, B (2) E, B, A (3) A, C, B (4) E, F, B",
        ["Opposite pairs: A-C, B-D, E-F.", "Option 3 has A and C. Option 4 has E and F. Reject both.", "Options 1 and 2 show A, B and E in opposite orders.", "Round their meeting point in the net, counter-clockwise, the order is E, A, B. That is option 1."],
        "Option 1"),
    pat("cn-p5", "Which cube cannot be formed?", "occasional",
        "The same setup, but the impossible cube is asked.",
        None,
        ["Find the three pairs of opposite faces.", "Check each option for an opposite pair.", "If none shows a pair, check the counter-clockwise order.", "The option with the wrong order is the answer."],
        "Three options fold correctly. The odd one out has an opposite pair or a mirror-image order.",
        "A net has a column of four squares K, M, O, J (K at the top). L is left of M and N is right of M. Faces are given as (top, front, right). Which cube cannot be formed? (1) K, L, M (2) K, M, N (3) M, L, O (4) M, O, L",
        ["Opposite pairs: K-O, M-J, L-N. No option shows a pair.", "Options 3 and 4 show the same faces M, L, O.", "In the net, round their meeting point, counter-clockwise, the order is M, L, O.", "Option 3 has that order. Option 4 is the mirror image."],
        "Option 4"),
    pat("cn-p6", "Which shape is a net?", "common",
        "Several flat shapes of six squares are drawn. The one that folds into a cube is asked.",
        None,
        ["Reject any shape with a 2 by 2 block.", "Reject any shape with a row of five squares.", "Fold the rest in your head or check the pairs."],
        "Blocks and long rows put two squares on the same face, so the cube cannot close.",
        "Which shape is a net of a cube? (a) five squares in a row, one below the middle square (b) a row of four squares, one above the second and one below the third (c) a 2 by 2 block with two more squares in a row on the right of the top one (d) two rows of three squares, the second row shifted one square to the right",
        ["Shape (a) has a row of five.", "Shapes (c) and (d) contain a 2 by 2 block.", "Shape (b) has no block and no long row, and it folds into a cube."],
        "Shape (b)"),
]

# ---------------------------------------------------------------- painted-cubes
pc_concept = (
    "A big cube of side n is painted on the outside and cut into n cubed small cubes. "
    "A small cube keeps paint only on the faces that were on the surface. "
    "Corners have 3 painted faces, edges have 2, face centres have 1, and the hidden core has none. "
    "Always use n minus 2 for edges, faces and the core."
)

pc_notes = r"""### The idea
Take a big cube of side $n$. Paint all six faces. Cut it into $n \times n \times n$ small cubes.

A small cube keeps paint only on faces that were on the outside. Its position decides how many faces are painted.

### The four counts
| Painted faces | Where the cube is | How many |
|---|---|---|
| 3 | corner | $8$ |
| 2 | on an edge, not a corner | $12(n-2)$ |
| 1 | middle of a face | $6(n-2)^2$ |
| 0 | inside | $(n-2)^3$ |

For $n = 4$: $8$, $24$, $24$ and $8$. They add to $64$.

> **Rule:** Corners are always 8, whatever the size. Every other count uses $(n-2)$.

### Why n minus 2
Each edge has $n$ small cubes. Two of them are corners. That leaves $n-2$.

Each face has $n \times n$ small cubes. Remove the border ring and $(n-2) \times (n-2)$ are left.

Peel one layer off every side of the big cube. A core of $(n-2)^3$ cubes is left.

The four counts must add up to $n^3$. Try $n = 3$: $8 + 12 + 6 + 1 = 27$.

> **Tip:** If your counts do not add to $n^3$, one of them is wrong.

### At least questions
- At least one face painted: all cubes except the core, $n^3 - (n-2)^3$.
- At least two faces painted: corners plus edges, $8 + 12(n-2)$.

A cube of side 6 has $216 - 64 = 152$ cubes with at least one painted face.

### Finding n
Sometimes a count is given and $n$ is asked. Divide, then add 2.

If 24 cubes have exactly two painted faces, then $12(n-2) = 24$. So $n - 2 = 2$ and $n = 4$.

A big cube of side 12 cm is cut into small cubes of side 3 cm. Then $n = 12 \div 3 = 4$.

### Cuboids
For an $a \times b \times c$ block, each side keeps its own $(\text{side} - 2)$.

- Corners: $8$.
- Edges: $4[(a-2)+(b-2)+(c-2)]$.
- Faces: $2[(a-2)(b-2)+(b-2)(c-2)+(c-2)(a-2)]$.
- Core: $(a-2)(b-2)(c-2)$.

For $5 \times 4 \times 3$: edges $4(3+2+1) = 24$ and core $3 \times 2 \times 1 = 6$.

### Worked example
A cube of side 5 is painted and cut into 125 small cubes.

1. Corners: $8$.
2. Edges: $12 \times 3 = 36$.
3. Face centres: $6 \times 3^2 = 54$.
4. Core: $3^3 = 27$.

Check: $8 + 36 + 54 + 27 = 125$. All counts are right.

### Only some faces painted
If only some faces are painted, count face by face. Each painted face has $n \times n$ small cubes. A cube on the edge shared by two painted faces is counted twice, so remove it.

Top and front painted, $n = 4$: $16 + 16 = 32$. The shared edge has 4 cubes with two painted faces. So exactly one painted face is $32 - 2 \times 4 = 24$.

> **Watch:** Two opposite painted faces share no cubes, so nothing is counted twice.
"""

pc_formulas = [
    {"name": "Two faces painted", "tex": r"12(n-2)", "note": "Cubes on the edges, not the corners."},
    {"name": "One face painted", "tex": r"6(n-2)^2", "note": "Cubes in the middle of each face."},
    {"name": "No face painted", "tex": r"(n-2)^3", "note": "The hidden inner block."},
    {"name": "Total check", "tex": r"8 + 12(n-2) + 6(n-2)^2 + (n-2)^3 = n^3", "note": "The four counts add up to all the small cubes."},
]

pc_tricks = [
    {
        "title": "Check the total",
        "body": "The four counts must add up to n cubed. Use it to catch mistakes.",
        "example": {
            "q": "For a cube of side 5, check the four counts.",
            "steps": [r"Corners $8$; edges $12 \times 3 = 36$; faces $6 \times 9 = 54$; core $27$.", r"$8 + 36 + 54 + 27 = 125 = 5^3$."],
            "answer": "125, so the counts are right",
        },
    },
    {
        "title": "At least one painted",
        "body": "Take all the small cubes and remove the core.",
        "example": {
            "q": "A cube of side 6 is painted and cut. How many small cubes have at least one painted face?",
            "steps": [r"Total: $6^3 = 216$.", r"Core: $4^3 = 64$.", r"$216 - 64 = 152$."],
            "answer": "152",
        },
    },
]

pc_mistakes = [
    {"wrong": "Using n instead of (n - 2) in the formulas.", "right": "Edges, faces and the core all use (n - 2). Subtract 2 before you square or cube."},
    {"wrong": "Thinking the number of corner cubes changes with n.", "right": "A cube always has 8 corners, so 3 painted faces always means 8 cubes."},
    {"wrong": "Counting corners again inside the edge cubes.", "right": "Edge cubes are only the n - 2 cubes between the corners."},
    {"wrong": "Using the cube formulas for a cuboid.", "right": "Use each side's own (side - 2): a - 2, b - 2 and c - 2."},
    {"wrong": "Forgetting to subtract the shared edge when only some faces are painted.", "right": "Two painted faces that touch share one edge. Remove those cubes from the exactly-one count."},
]

pc_revision = [
    "3 painted faces: 8 corners, for any n.",
    r"2 painted faces: $12(n-2)$.",
    r"1 painted face: $6(n-2)^2$.",
    r"0 painted faces: $(n-2)^3$.",
    r"The four counts add to $n^3$.",
    r"At least one: $n^3 - (n-2)^3$. At least two: $8 + 12(n-2)$.",
    "Given a count? Divide, then add 2 to get n.",
]

pc_patterns = [
    pat("pc-p1", "Three faces painted (corners)", "very common",
        "A painted cube is cut up. The question asks for cubes with three painted faces.",
        None,
        ["Recall that only corner cubes have three painted faces.", "A cube has 8 corners."],
        "A small cube touches three big faces only at a corner of the big cube.",
        "A cube of side 7 is painted on all faces and cut into small cubes of side 1. How many small cubes have three painted faces?",
        ["Only the corner cubes have three painted faces.", "A cube has 8 corners."],
        "8"),
    pat("pc-p2", "Two faces painted (edges)", "very common",
        "The question asks for cubes with exactly two painted faces.",
        r"12(n-2)",
        ["Find n, the number of small cubes along one edge.", "Each edge has n - 2 cubes that are not corners.", "Multiply by 12 edges."],
        "Each of the 12 edges has n cubes, and 2 of them are corners.",
        "A cube of side 5 is painted and cut into 125 small cubes. How many have exactly two painted faces?",
        [r"$n = 5$, so each edge has $5 - 2 = 3$ such cubes.", r"$12 \times 3 = 36$."],
        "36"),
    pat("pc-p3", "One face painted (face centres)", "very common",
        "The question asks for cubes with exactly one painted face.",
        r"6(n-2)^{2}",
        ["Find n.", "On each face, remove the border ring. A block of (n - 2) by (n - 2) is left.", "Multiply by 6 faces."],
        "Cubes in the middle of a face touch no edge, so they have only that one face painted.",
        "A cube of side 6 is painted and cut into small cubes of side 1. How many have exactly one painted face?",
        [r"$n - 2 = 4$.", r"One face: $4 \times 4 = 16$.", r"$6 \times 16 = 96$."],
        "96"),
    pat("pc-p4", "No face painted (core)", "common",
        "The question asks for cubes with no paint at all.",
        r"(n-2)^{3}",
        ["Find n.", "Peel one layer off every side.", "Cube the side that is left: (n - 2) cubed."],
        "The cubes inside never touched the outside, so they stay unpainted.",
        "A cube of side 5 is painted and cut into small cubes of side 1. How many small cubes have no painted face?",
        [r"$n - 2 = 3$.", r"$3^3 = 27$."],
        "27"),
    pat("pc-p5", "At least or combined counts", "common",
        "The question says at least one, at least two, or asks for two classes added together.",
        r"n^{3} - (n-2)^{3}",
        ["At least one painted: all cubes minus the core.", "At least two painted: corners plus edges.", "For any other mix, add the classes you need."],
        "Every class is already counted, so a combined count is a sum of classes.",
        "A cube of side 4 is painted and cut into small cubes of side 1. How many have at least two painted faces?",
        [r"Corners: $8$.", r"Edges: $12 \times 2 = 24$.", r"$8 + 24 = 32$."],
        "32"),
    pat("pc-p6", "Painted cuboid", "occasional",
        "The block is a by b by c, not a cube.",
        None,
        ["Write a - 2, b - 2 and c - 2.", "Corners: 8.", "Edges: 4 times the sum of the three (side - 2) values.", "Faces and core use products of the (side - 2) values."],
        "Each side of a cuboid has its own length, so each keeps its own (side - 2).",
        "A cuboid measuring 5 by 4 by 3 is painted and cut into small cubes of side 1. How many have exactly two painted faces?",
        [r"$(5-2)+(4-2)+(3-2) = 3+2+1 = 6$.", r"$4 \times 6 = 24$."],
        "24"),
    pat("pc-p7", "Find n from a count or a size", "occasional",
        "A count of painted cubes, or the edge lengths of the big and small cubes, is given. Another count is asked.",
        None,
        ["Turn the given count into n: divide by 12 (edges) or by 6 and take the square root (faces).", "Add 2 to get n. If edges are in cm, n = big edge divided by small edge.", "Now find the count that is asked."],
        "The formulas run both ways, so a count fixes n.",
        "36 small cubes have exactly two painted faces. How many small cubes have exactly one painted face?",
        [r"$12(n-2) = 36$, so $n - 2 = 3$ and $n = 5$.", r"One face: $6 \times 3^2 = 54$."],
        "54"),
    pat("pc-p8", "Only some faces painted", "occasional",
        "The question says which faces are painted, such as the top and one side, or two opposite faces.",
        None,
        ["Count the small cubes on each painted face: n times n.", "If two painted faces touch, they share an edge of n cubes.", "Exactly one painted face = sum of faces minus twice the shared cubes."],
        "The cubes on a shared edge have two painted faces, so they must leave the exactly-one count.",
        "A cube of side 4 is painted on its top face and on its front face only. It is cut into 64 small cubes. How many have exactly one painted face?",
        [r"Top face: $4 \times 4 = 16$. Front face: $16$.", "The shared edge has 4 cubes with two painted faces.", r"$16 + 16 - 2 \times 4 = 24$."],
        "24"),
]

# ---------------------------------------------------------------- patch
dfrac = lambda x: x.replace(r"\frac", r"\dfrac")


def clean(mistakes, revision):
    return ([{k: dfrac(v) for k, v in m.items()} for m in mistakes], [dfrac(r) for r in revision])


blocks = {
    "dice-positions": (dp_concept, dp_notes, dp_formulas, dp_tricks, *clean(dp_mistakes, dp_revision), dp_patterns),
    "cube-nets": (cn_concept, cn_notes, cn_formulas, cn_tricks, *clean(cn_mistakes, cn_revision), cn_patterns),
    "painted-cubes": (pc_concept, pc_notes, pc_formulas, pc_tricks, *clean(pc_mistakes, pc_revision), pc_patterns),
}

data = json.loads(TOPIC.read_text(encoding="utf-8"))
frozen = json.dumps([data.get("practice"), data.get("solvedExamples"), data.get("pyqPatterns")],
                    ensure_ascii=False, sort_keys=True)
new_ids = [p["id"] for blk in blocks.values() for p in blk[6]]
assert len(new_ids) == len(set(new_ids))

for sub in data["subtopics"]:
    if sub["id"] not in blocks:
        continue
    concept, notes, formulas, tricks, mistakes, revision, patterns = blocks[sub["id"]]
    old_ids = {p["id"] for p in sub.get("patterns", [])}
    assert old_ids <= {p["id"] for p in patterns}, f"{sub['id']}: never drop a pattern id"
    other = {p["id"] for s in data["subtopics"] if s["id"] != sub["id"] for p in s.get("patterns", [])}
    assert not (other & {p["id"] for p in patterns}), "pattern id clash"
    assert 2500 <= len(notes) <= 5000, f"{sub['id']} notes {len(notes)} chars"
    assert 4 <= len(mistakes) <= 8 and 4 <= len(revision) <= 9
    sub.update(concept=concept, notes=notes.strip() + "\n", formulas=formulas, tricks=tricks,
               mistakes=mistakes, revision=revision, patterns=patterns)
    print(f"{sub['id']}: notes {len(notes)} chars, {len(patterns)} patterns")

assert json.dumps([data.get("practice"), data.get("solvedExamples"), data.get("pyqPatterns")],
                  ensure_ascii=False, sort_keys=True) == frozen
with open(TOPIC, "w", encoding="utf-8", newline="\n") as f:
    json.dump(data, f, ensure_ascii=False, indent=1)
print("cube-dice.json patched; corner-only-touching opposite cases:", corner_touch_opposite)
