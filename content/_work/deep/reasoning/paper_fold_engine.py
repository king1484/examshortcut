"""Paper-folding simulator for reasoning/paper-folding-cutting.

The sheet is an S x S square (model units, y down). It is sampled two ways:
  * a lattice of points with step 1/2 - every hole position we can punch;
  * a mesh of small triangles (each unit cell cut by its diagonals) - used only to
    draw the folded outline at each stage.
A fold is an exact reflection (Fractions) of everything on the moving side of a line.
After all folds, a punch at point p makes one hole at every ORIGINAL lattice point whose
folded position is p. So the unfolded pattern is brute-forced, not reasoned out.
"""
from fractions import Fraction as F

from nonverbal_lib import DASH, LIGHT, circ, ln, merge, pline, poly, svg, txt, num

HALF = F(1, 2)


def cross(a, b, p):
    return (b[0] - a[0]) * (p[1] - a[1]) - (b[1] - a[1]) * (p[0] - a[0])


def sgn(v):
    return (v > 0) - (v < 0)


def reflect(a, b, p):
    dx, dy = b[0] - a[0], b[1] - a[1]
    t = ((p[0] - a[0]) * dx + (p[1] - a[1]) * dy) / (dx * dx + dy * dy)
    fx, fy = a[0] + t * dx, a[1] + t * dy
    return (2 * fx - p[0], 2 * fy - p[1])


def rot_about(a, b, p):
    m = ((a[0] + b[0]) / 2, (a[1] + b[1]) / 2)
    return (2 * m[0] - p[0], 2 * m[1] - p[1])


class Paper:
    def __init__(self, S=8):
        self.S = F(S)
        n = 2 * S
        self.orig = [(F(i, 2), F(j, 2)) for i in range(n + 1) for j in range(n + 1)]
        self.cur = list(self.orig)
        tris = []
        for x in range(S):
            for y in range(S):
                c = (F(x) + HALF, F(y) + HALF)
                k = [(F(x), F(y)), (F(x + 1), F(y)), (F(x + 1), F(y + 1)), (F(x), F(y + 1))]
                for i in range(4):
                    tris.append((k[i], k[(i + 1) % 4], c))
        self.tris = tris
        self.stages = []          # (region polygon, fold line a, b, mover point)
        self.folds = []

    # ---------------------------------------------------------------- geometry of the current state
    def region_edges(self):
        uniq = {frozenset(t) for t in self.tris}
        cnt = {}
        for t in uniq:
            t = list(t)
            for i in range(3):
                e = frozenset((t[i], t[(i + 1) % 3]))
                cnt[e] = cnt.get(e, 0) + 1
        edges = [tuple(e) for e, c in cnt.items() if c == 1]
        return [(s[3], s[4]) for s in merge(edges)]

    def region(self):
        """Boundary of the folded shape as an ordered vertex loop."""
        segs = self.region_edges()
        adj = {}
        for a, b in segs:
            adj.setdefault(a, []).append(b)
            adj.setdefault(b, []).append(a)
        assert all(len(v) == 2 for v in adj.values()), "region is not a simple polygon"
        start = min(adj)
        loop = [start]
        prev, curp = None, start
        while True:
            nxt = adj[curp][0] if adj[curp][0] != prev else adj[curp][1]
            if nxt == start:
                break
            loop.append(nxt)
            prev, curp = curp, nxt
        assert len(loop) == len(segs)
        return loop

    def bbox(self):
        pts = [p for t in self.tris for p in t]
        xs = [p[0] for p in pts]
        ys = [p[1] for p in pts]
        return min(xs), min(ys), max(xs), max(ys)

    # ---------------------------------------------------------------- folding
    def fold_line(self, a, b, mover, mode="reflect", desc=""):
        s = sgn(cross(a, b, mover))
        assert s != 0
        fn = reflect if mode == "reflect" else rot_about
        self.stages.append((self.region(), a, b, mover))
        self.folds.append(desc)
        self.cur = [fn(a, b, p) if sgn(cross(a, b, p)) == s else p for p in self.cur]
        nt = []
        for t in self.tris:
            sg = {sgn(cross(a, b, p)) for p in t} - {0}
            assert len(sg) <= 1, "fold line cuts a mesh triangle"
            nt.append(tuple(fn(a, b, p) for p in t) if sg == {s} else t)
        self.tris = nt
        return self

    def fold(self, kind, arg=None, mode="reflect"):
        """kind: V/H half fold of the current box (arg = moving side L/R/T/B),
        VS/HS strip fold at absolute coordinate arg=(c, side),
        D diagonal of the current square box, arg=(main|anti, moving corner TL/TR/BL/BR),
        T halve the current right triangle, arg = moving corner of the box."""
        x0, y0, x1, y1 = self.bbox()
        corner = {"TL": (x0, y0), "TR": (x1, y0), "BL": (x0, y1), "BR": (x1, y1)}
        if kind == "V":
            c = (x0 + x1) / 2
            mv = {"L": (x0, (y0 + y1) / 2), "R": (x1, (y0 + y1) / 2)}[arg]
            d = {"L": "the left half is folded over onto the right half",
                 "R": "the right half is folded over onto the left half"}[arg]
            return self.fold_line((c, y0), (c, y1), mv, mode, d)
        if kind == "H":
            c = (y0 + y1) / 2
            mv = {"T": ((x0 + x1) / 2, y0), "B": ((x0 + x1) / 2, y1)}[arg]
            d = {"T": "the top half is folded down onto the bottom half",
                 "B": "the bottom half is folded up onto the top half"}[arg]
            return self.fold_line((x0, c), (x1, c), mv, mode, d)
        if kind == "VS":
            c, side = F(arg[0]), arg[1]
            mv = {"L": (x0, (y0 + y1) / 2), "R": (x1, (y0 + y1) / 2)}[side]
            d = f"only the {'left' if side == 'L' else 'right'} strip is folded over along the dashed line"
            return self.fold_line((c, y0), (c, y1), mv, mode, d)
        if kind == "HS":
            c, side = F(arg[0]), arg[1]
            mv = {"T": ((x0 + x1) / 2, y0), "B": ((x0 + x1) / 2, y1)}[side]
            d = f"only the {'top' if side == 'T' else 'bottom'} strip is folded over along the dashed line"
            return self.fold_line((x0, c), (x1, c), mv, mode, d)
        if kind == "D":
            which, mvc = arg
            if which == "main":
                a, b = (x0, y0), (x1, y1)
                d = "folded along the diagonal from top-left to bottom-right"
            else:
                a, b = (x1, y0), (x0, y1)
                d = "folded along the diagonal from top-right to bottom-left"
            names = {"TL": "top-left", "TR": "top-right", "BL": "bottom-left", "BR": "bottom-right"}
            return self.fold_line(a, b, corner[mvc], mode, d + f", the {names[mvc]} corner moving across")
        if kind == "T":
            loop = self.region()
            assert len(loop) == 3
            # right-angle vertex: the one whose two edges are perpendicular
            for i in range(3):
                p, q, r = loop[i], loop[(i + 1) % 3], loop[(i + 2) % 3]
                if (q[0] - p[0]) * (r[0] - p[0]) + (q[1] - p[1]) * (r[1] - p[1]) == 0:
                    mid = ((q[0] + r[0]) / 2, (q[1] + r[1]) / 2)
                    return self.fold_line(p, mid, corner[arg], mode,
                                          "the triangle is folded in half again into a smaller triangle")
            raise AssertionError("not a right triangle")
        raise ValueError(kind)

    # ---------------------------------------------------------------- punching
    def holes(self, punches):
        out = set()
        for p in punches:
            p = (F(p[0]), F(p[1]))
            hit = {o for o, c in zip(self.orig, self.cur) if c == p}
            assert hit, f"punch {p} is not on the folded paper"
            out |= hit
        return out

    def layers(self, p):
        p = (F(p[0]), F(p[1]))
        return sum(1 for c in self.cur if c == p)


def build(folds, S=8, mode_at=None):
    """folds: list of (kind, arg). mode_at: index of a fold done as a half turn (distractor)."""
    pp = Paper(S)
    for i, (k, a) in enumerate(folds):
        pp.fold(k, a, "rotate" if i == mode_at else "reflect")
    return pp


# ---------------------------------------------------------------- drawing
U = 6          # px per model unit (sheet 48 px for S = 8)
PAD = 7
PITCH = 72


def _arrow(a, b, mover, dx, u):
    m = ((a[0] + b[0]) / 2, (a[1] + b[1]) / 2)
    vx, vy = float(b[0] - a[0]), float(b[1] - a[1])
    L = (vx * vx + vy * vy) ** 0.5
    nx, ny = -vy / L, vx / L
    # point the normal towards the moving side
    if (float(mover[0] - m[0]) * nx + float(mover[1] - m[1]) * ny) < 0:
        nx, ny = -nx, -ny
    mx, my = float(m[0]) * u + dx, float(m[1]) * u + PAD
    s = (mx + nx * 8.4, my + ny * 8.4)
    e = (mx - nx * 7.2, my - ny * 7.2)
    # arrow head
    hx, hy = -nx, -ny
    px, py = -hy, hx
    h1 = (e[0] - hx * 3.4 + px * 2.1, e[1] - hy * 3.4 + py * 2.1)
    h2 = (e[0] - hx * 3.4 - px * 2.1, e[1] - hy * 3.4 - py * 2.1)
    return ln(s[0], s[1], e[0], e[1]) + pline([h1, e, h2])


def fold_svg(pp, punches, S=8, show_punch=True):
    u = U * 8 / S
    body = ""
    n = len(pp.stages)
    for i, (reg, a, b, mover) in enumerate(pp.stages):
        dx = PAD + i * PITCH
        T = lambda p: (float(p[0]) * u + dx, float(p[1]) * u + PAD)  # noqa
        if i > 0:
            body += poly([T((0, 0)), T((S, 0)), T((S, S)), T((0, S))], DASH)
        body += poly([T(p) for p in reg], LIGHT)
        A, B = T(a), T(b)
        body += ln(A[0], A[1], B[0], B[1], DASH)
        body += _arrow(a, b, mover, dx, u)
        body += txt(dx + S * u + 12, PAD + S * u / 2 + 3, "→", 9)
    dx = PAD + n * PITCH
    T = lambda p: (float(p[0]) * u + dx, float(p[1]) * u + PAD)  # noqa
    body += poly([T((0, 0)), T((S, 0)), T((S, S)), T((0, S))], DASH)
    body += poly([T(p) for p in pp.region()], LIGHT)
    if show_punch:
        for p in punches:
            c = T(p)
            body += circ(c[0], c[1], 2.6, True)
    return svg(dx + S * u + PAD, S * u + 2 * PAD, body, sw="1.2")


def sheet_svg(holes, S=8):
    u = 48 / S
    body = poly([(6, 6), (54, 6), (54, 54), (6, 54)])
    for p in sorted(holes):
        body += circ(6 + float(p[0]) * u, 6 + float(p[1]) * u, 2.6, True)
    return svg(60, 60, body, sw="1.2")


def min_gap(points):
    pts = sorted(points)
    best = None
    for i in range(len(pts)):
        for j in range(i + 1, len(pts)):
            d2 = (pts[i][0] - pts[j][0]) ** 2 + (pts[i][1] - pts[j][1]) ** 2
            best = d2 if best is None or d2 < best else best
    return best
