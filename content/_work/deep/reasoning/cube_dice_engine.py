"""Exact geometry for cube-dice: cube rotations, dice views, net folding, painted counts.

Faces are the six axis directions of a cube (integer 3-vectors). A die assigns one
label to each face; a view of a die is read from the model by applying one of the 24
rotations. Nets are folded by exact quarter-turns about shared edges, so every
opposite-pair / can-form claim is enumerated from the model, never worked out by hand.
Painted-cube counts are brute-forced cube by cube.
"""
import random
from itertools import permutations


def add(a, b):
    return (a[0] + b[0], a[1] + b[1], a[2] + b[2])


def neg(a):
    return (-a[0], -a[1], -a[2])


def dot(a, b):
    return a[0] * b[0] + a[1] * b[1] + a[2] * b[2]


def cross(a, b):
    return (a[1] * b[2] - a[2] * b[1],
            a[2] * b[0] - a[0] * b[2],
            a[0] * b[1] - a[1] * b[0])


def scale(a, k):
    return (a[0] * k, a[1] * k, a[2] * k)


def rot90(v, h):
    """Rotate v by +90 deg (right-hand rule) about axis h (integer vectors)."""
    return add(cross(h, v), scale(h, dot(h, v)))


AXES = {"U": (0, 1, 0), "D": (0, -1, 0), "F": (0, 0, 1),
        "B": (0, 0, -1), "R": (1, 0, 0), "L": (-1, 0, 0)}
NAME = {v: k for k, v in AXES.items()}
FACE_ORDER = ("U", "D", "F", "B", "R", "L")


def mvec(M, v):
    """Image of v under the rotation M (M[0], M[1], M[2] are the images of x, y, z)."""
    return tuple(sum(M[k][i] * v[i] for i in range(3)) for k in range(3))


def mmul(A, B):
    """Composition: apply B, then A."""
    return tuple(mvec(A, B[k]) for k in range(3))


_ID = ((1, 0, 0), (0, 1, 0), (0, 0, 1))
_GEN = (((1, 0, 0), (0, 0, 1), (0, -1, 0)),    # +90 about x
        ((0, 0, -1), (0, 1, 0), (1, 0, 0)),    # +90 about y
        ((0, 1, 0), (-1, 0, 0), (0, 0, 1)))    # +90 about z


def _rots():
    seen = {_ID}
    fr = [_ID]
    while fr:
        nx = []
        for M in fr:
            for G in _GEN:
                C = mmul(G, M)
                if C not in seen:
                    seen.add(C)
                    nx.append(C)
        fr = nx
    assert len(seen) == 24
    return sorted(seen)


ROTS = _rots()

# For each rotation, the source faces (front, top, right) that land on (F, U, R).
SRC = []
for _M in ROTS:
    _Minv = tuple(zip(*_M))                     # transpose = inverse rotation
    SRC.append(tuple(NAME[mvec(_Minv, AXES[c])] for c in "FUR"))
SRC.sort()
assert len(SRC) == 24 and len(set(SRC)) == 24


# ================================================================ dice
def make_die(rng, labels):
    lab = list(labels)
    rng.shuffle(lab)
    return dict(zip(FACE_ORDER, lab))


def view_i(die, i):
    return tuple(die[c] for c in SRC[i])


def views_of(die):
    return {view_i(die, i) for i in range(24)}


def can_view(die, v):
    return v in views_of(die)


def forced_opposite(labels, views, target):
    """All labels that could be opposite `target` in SOME assignment of the labels to
    faces consistent with every view. A puzzle answer is sound only if this is a
    single label - the enumeration is the proof."""
    outs = set()
    for perm in permutations(labels):
        A = dict(zip(FACE_ORDER, perm))
        ok = True
        for v in views:
            if not any(tuple(A[c] for c in s) == v for s in SRC):
                ok = False
                break
        if ok:
            f = next(fc for fc in FACE_ORDER if A[fc] == target)
            outs.add(A[NAME[neg(AXES[f])]])
    return outs


def opp_map_from_pairs(pairs):
    m = {}
    for a, b in pairs:
        m[a] = b
        m[b] = a
    return m


# ================================================================ nets
def fold_net(cells):
    """Fold a net (dict (x, y) -> label, label side toward the viewer) into a cube.
    The lexicographically first square becomes the front face. Asserts the net is
    connected and really folds into a cube."""
    origin = min(cells)
    frames = {origin: ((0, 1, 0), (1, 0, 0), (0, 0, 1))}
    stack = [origin]
    while stack:
        s = stack.pop()
        u, r, n = frames[s]
        for dvec, himg in (((1, 0), u), ((0, 1), neg(r)),
                           ((-1, 0), neg(u)), ((0, -1), r)):
            nb = (s[0] + dvec[0], s[1] + dvec[1])
            if nb in cells and nb not in frames:
                frames[nb] = tuple(rot90(v, himg) for v in (u, r, n))
                stack.append(nb)
    assert len(frames) == len(cells), "net is not connected"
    cube = {}
    for cell, lab in cells.items():
        f = NAME[frames[cell][2]]
        assert f not in cube, "two squares fold onto the same face"
        cube[f] = lab
    return cube


def fold(cells):
    """Fold a net given in SCREEN coordinates (y grows downward, as drawn).
    fold_net itself works in y-up maths coordinates, so mirror y first; that keeps
    the handedness of the folded cube identical to the drawn sheet."""
    return fold_net({(x, -y): lab for (x, y), lab in cells.items()})


def net_opposites(cube):
    pairs = set()
    for f in FACE_ORDER:
        o = NAME[neg(AXES[f])]
        pairs.add(tuple(sorted((cube[f], cube[o]))))
    ps = sorted(pairs)
    assert len(ps) == 3
    return ps


def opp_map(cube):
    return opp_map_from_pairs(net_opposites(cube))


# ================================================================ drawing
def die_svg(views):
    """One or more isometric dice in a row, each shown as (front, top, right)."""
    w = 59 + 65 * (len(views) - 1)
    out = ['<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 %d 59" width="%d" height="59" '
           'fill="none" stroke="currentColor" stroke-width="1.3" stroke-linecap="round" '
           'stroke-linejoin="round">' % (w, w)]
    for k, (f, t, r) in enumerate(views):
        o = 65 * k
        out.append('<polygon points="%d,21 %d,21 %d,55 %d,55"/>' % (4 + o, 38 + o, 38 + o, 4 + o))
        out.append('<polygon points="%d,21 %d,21 %d,4 %d,4"/>' % (4 + o, 38 + o, 55 + o, 21 + o))
        out.append('<polygon points="%d,21 %d,4 %d,38 %d,55"/>' % (38 + o, 55 + o, 55 + o, 38 + o))
        out.append('<text x="%d" y="43" font-size="14" text-anchor="middle" fill="currentColor" '
                   'stroke="none" font-family="sans-serif">%s</text>' % (21 + o, f))
        out.append('<text x="%s" y="16.5" font-size="10" text-anchor="middle" fill="currentColor" '
                   'stroke="none" font-family="sans-serif">%s</text>' % (29.5 + o, t))
        out.append('<text x="%s" y="33.5" font-size="10" text-anchor="middle" fill="currentColor" '
                   'stroke="none" font-family="sans-serif">%s</text>' % (46.5 + o, r))
    out.append("</svg>")
    return "".join(out)


def net_svg(cells):
    xs = [c[0] for c in cells]
    ys = [c[1] for c in cells]
    x0, y0 = min(xs), min(ys)
    w = (max(xs) - x0 + 1) * 27 + 3
    h = (max(ys) - y0 + 1) * 27 + 3
    out = ['<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 %d %d" width="%d" height="%d" '
           'fill="none" stroke="currentColor" stroke-width="1.3" stroke-linecap="round" '
           'stroke-linejoin="round">' % (w, h, w, h)]
    for cell in sorted(cells):
        px = 3 + (cell[0] - x0) * 27
        py = 3 + (cell[1] - y0) * 27
        out.append('<polygon points="%d,%d %d,%d %d,%d %d,%d"/>'
                   % (px, py, px + 24, py, px + 24, py + 24, px, py + 24))
        out.append('<text x="%d" y="%d" font-size="13" text-anchor="middle" fill="currentColor" '
                   'stroke="none" font-family="sans-serif">%s</text>'
                   % (px + 12, py + 17, cells[cell]))
    out.append("</svg>")
    return "".join(out)


# ================================================================ painted cubes
def paint_counts(a, b=None, c=None):
    """Brute-force counts of unit cubes by number of painted faces, for a cube of side
    a or a cuboid a x b x c, all faces painted."""
    if b is None:
        b = c = a
    out = {0: 0, 1: 0, 2: 0, 3: 0}
    for i in range(a):
        for j in range(b):
            for k in range(c):
                q = (i in (0, a - 1)) + (j in (0, b - 1)) + (k in (0, c - 1))
                out[q] += 1
    return out


# ================================================================ option helpers
def adjacent_pairs(die, rng, k):
    """k unordered pairs of labels that are NOT opposite, formatted 'X and Y'."""
    labels = sorted(die.values())
    opp = opp_map(die)
    cand = [(a, b) for i, a in enumerate(labels) for b in labels[i + 1:] if opp[a] != b]
    rng.shuffle(cand)
    return ["%s and %s" % p for p in cand[:k]]


def impossible_triples(die, rng):
    """(front, top, right) label triples that can NEVER be seen on this die."""
    vs = views_of(die)
    opp = opp_map(die)
    labels = sorted(die.values())
    cand = []
    for v in sorted(vs):
        for p in permutations(v):
            p = tuple(p)
            if p not in vs and p not in cand:
                cand.append(p)                       # right faces, wrong corner order
    for x in labels:
        for y in labels:
            for z in labels:
                if len({x, y, z}) == 3:
                    t3 = (x, y, z)
                    if t3 not in vs and t3 not in cand and \
                            (opp[x] == y or opp[x] == z or opp[y] == z):
                        cand.append(t3)              # an opposite pair shown together
    rng.shuffle(cand)
    return cand
