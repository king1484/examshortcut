"""Shared helpers for the non-verbal reasoning build scripts
(counting-figures, mirror-water-image, paper-folding-cutting, cube-dice,
embedded-figures, figure-series).

Two parts:
  1. SVG writer  - every figure is built from a model, never typed by hand.
  2. Line-figure engine - exact (Fraction) geometry: merge collinear segments,
     find all crossing points, and brute-force count triangles, squares,
     rectangles and straight lines.
"""
import itertools
import re
from collections import Counter
from fractions import Fraction as F

# ------------------------------------------------------------------ SVG
SW = "1.5"


def num(v):
    v = float(v)
    s = ("%.1f" % v)
    if s.endswith(".0"):
        s = s[:-2]
    if s == "-0":
        s = "0"
    return s


def svg(w, h, body, sw=SW):
    s = (f'<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 {num(w)} {num(h)}" '
         f'width="{num(w)}" height="{num(h)}" fill="none" stroke="currentColor" '
         f'stroke-width="{sw}" stroke-linecap="round" stroke-linejoin="round">{body}</svg>')
    check_svg(s)
    return s


def check_svg(s, limit=3072):
    assert s.startswith("<svg") and s.endswith("</svg>")
    assert "<script" not in s and "href" not in s.replace('xmlns="http://www.w3.org/2000/svg"', "")
    assert "url(" not in s
    # no hard-coded colours: only currentColor / none
    for m in re.finditer(r'(fill|stroke)="([^"]+)"', s):
        assert m.group(2) in ("currentColor", "none"), m.group(0)
    assert "#" not in s and "rgb" not in s, "hard-coded colour"
    assert len(s.encode("utf-8")) <= limit, f"SVG too big: {len(s)} bytes"


def ln(x1, y1, x2, y2, extra=""):
    return f'<line x1="{num(x1)}" y1="{num(y1)}" x2="{num(x2)}" y2="{num(y2)}"{extra}/>'


def poly(pts, extra=""):
    return '<polygon points="' + " ".join(f"{num(x)},{num(y)}" for x, y in pts) + f'"{extra}/>'


def pline(pts, extra=""):
    return '<polyline points="' + " ".join(f"{num(x)},{num(y)}" for x, y in pts) + f'"{extra}/>'


def circ(cx, cy, r, filled=False, extra=""):
    f = ' fill="currentColor"' if filled else ""
    return f'<circle cx="{num(cx)}" cy="{num(cy)}" r="{num(r)}"{f}{extra}/>'


def txt(x, y, s, size=12, extra=""):
    return (f'<text x="{num(x)}" y="{num(y)}" font-size="{size}" text-anchor="middle" '
            f'fill="currentColor" stroke="none" font-family="sans-serif"{extra}>{s}</text>')


DASH = ' stroke-dasharray="3 2"'
SHADE = ' fill="currentColor" fill-opacity="0.35"'
LIGHT = ' fill="currentColor" fill-opacity="0.12"'


def g(body, dx=0, dy=0):
    return f'<g transform="translate({num(dx)},{num(dy)})">{body}</g>'


# ------------------------------------------------------------------ line-figure engine

def P(x, y):
    return (F(x), F(y))


class Fig:
    """A figure = list of straight segments with exact coordinates."""

    def __init__(self, segs=None):
        self.segs = []
        for s in segs or []:
            self.add(*s)

    def add(self, a, b):
        a, b = P(*a), P(*b)
        if a != b:
            self.segs.append((a, b))
        return self

    def poly(self, pts, closed=True):
        pts = list(pts)
        for i in range(len(pts) - (0 if closed else 1)):
            self.add(pts[i], pts[(i + 1) % len(pts)])
        return self

    def extend(self, other):
        self.segs += other.segs
        return self

    # ---- analysis (cached)
    def analyse(self):
        if getattr(self, "_done", False):
            return
        self.lines = merge(self.segs)          # maximal drawn segments
        pts = set()
        for key, t0, t1, a, b in self.lines:
            pts.add(a)
            pts.add(b)
        L = self.lines
        for i in range(len(L)):
            for j in range(i + 1, len(L)):
                p = inter(L[i], L[j])
                if p is not None:
                    pts.add(p)
        self.pts = sorted(pts)
        self.idx = {p: i for i, p in enumerate(self.pts)}
        n = len(self.pts)
        self.on = [set() for _ in range(n)]     # point -> set of line indices
        for li, l in enumerate(L):
            for pi, p in enumerate(self.pts):
                if on_line(l, p):
                    self.on[pi].add(li)
        self.conn = [[bool(self.on[i] & self.on[j]) for j in range(n)] for i in range(n)]
        self._done = True

    def triangles(self):
        self.analyse()
        n = len(self.pts)
        out = []
        for i in range(n):
            for j in range(i + 1, n):
                if not self.conn[i][j]:
                    continue
                for k in range(j + 1, n):
                    if self.conn[i][k] and self.conn[j][k] and not (self.on[i] & self.on[j] & self.on[k]):
                        if cross(self.pts[i], self.pts[j], self.pts[k]) != 0:
                            out.append((self.pts[i], self.pts[j], self.pts[k]))
        return out

    def rectangles(self):
        """All rectangles (any orientation) whose four sides are drawn."""
        self.analyse()
        n = len(self.pts)
        found = set()
        for b in range(n):
            B = self.pts[b]
            nb = [a for a in range(n) if a != b and self.conn[a][b]]
            for a, c in itertools.combinations(nb, 2):
                A, C = self.pts[a], self.pts[c]
                if (A[0] - B[0]) * (C[0] - B[0]) + (A[1] - B[1]) * (C[1] - B[1]) != 0:
                    continue
                if self.on[a] & self.on[b] & self.on[c]:
                    continue
                D = (A[0] + C[0] - B[0], A[1] + C[1] - B[1])
                d = self.idx.get(D)
                if d is None or not (self.conn[c][d] and self.conn[d][a]):
                    continue
                found.add(frozenset((A, B, C, D)))
        return [tuple(r) for r in found]

    def squares(self):
        out = []
        for r in self.rectangles():
            pts = list(r)
            d = sorted(dist2(pts[0], p) for p in pts[1:])
            if d[0] == d[1]:
                out.append(r)
        return out

    def count_lines(self, direction=None):
        """Number of maximal straight lines; direction in (None,'h','v','slant')."""
        self.analyse()
        c = 0
        for key, t0, t1, a, b in self.lines:
            dx, dy = b[0] - a[0], b[1] - a[1]
            kind = "h" if dy == 0 else ("v" if dx == 0 else "slant")
            if direction is None or direction == kind:
                c += 1
        return c

    def tri_sizes(self):
        """Counter: area / smallest-area -> count."""
        ts = self.triangles()
        areas = [abs(cross(*t)) for t in ts]
        m = min(areas)
        return Counter(a / m for a in areas)

    # ---- rendering
    def svg(self, scale=1, pad=5, extra_body="", sw=SW, labels=None):
        """labels: {point: (letter, dx, dy)} - letter drawn next to the point."""
        if labels:
            pad = max(pad, 12)
        xs = [p[0] for s in self.segs for p in s]
        ys = [p[1] for s in self.segs for p in s]
        x0, y0 = min(xs), min(ys)
        w = float(max(xs) - x0) * scale + 2 * pad
        h = float(max(ys) - y0) * scale + 2 * pad
        body = ""
        for key, t0, t1, a, b in merge(self.segs):
            body += ln(pad + float(a[0] - x0) * scale, pad + float(a[1] - y0) * scale,
                       pad + float(b[0] - x0) * scale, pad + float(b[1] - y0) * scale)
        for p, (s, dx, dy) in (labels or {}).items():
            p = P(*p)
            body += txt(pad + float(p[0] - x0) * scale + dx, pad + float(p[1] - y0) * scale + dy + 3.5, s, size=10)
        return svg(w, h, body + extra_body, sw=sw)

    def named_triangles(self, labels):
        """List triangles as letter strings; every triangle corner must be labelled."""
        lab = {P(*p): v[0] for p, v in labels.items()}
        order = "".join(v[0] for v in labels.values())
        out = []
        for t in self.triangles():
            assert all(p in lab for p in t), "unlabelled triangle corner"
            out.append("".join(sorted((lab[p] for p in t), key=order.index)))
        return sorted(out, key=lambda s: [order.index(c) for c in s])


def cross(a, b, c):
    return (b[0] - a[0]) * (c[1] - a[1]) - (b[1] - a[1]) * (c[0] - a[0])


def dist2(a, b):
    return (a[0] - b[0]) ** 2 + (a[1] - b[1]) ** 2


def line_key(a, b):
    A = b[1] - a[1]
    B = a[0] - b[0]
    C = A * a[0] + B * a[1]
    f = A if A != 0 else B
    return (A / f, B / f, C / f)


def param(key, p):
    # parameter along the line: x if not vertical, else y
    return p[0] if key[1] != 0 else p[1]


def merge(segs):
    groups = {}
    for a, b in segs:
        k = line_key(a, b)
        ta, tb = param(k, a), param(k, b)
        if ta > tb:
            a, b, ta, tb = b, a, tb, ta
        groups.setdefault(k, []).append((ta, tb, a, b))
    out = []
    for k, iv in groups.items():
        iv.sort()
        cur = list(iv[0])
        for t0, t1, a, b in iv[1:]:
            if t0 <= cur[1]:
                if t1 > cur[1]:
                    cur[1], cur[3] = t1, b
            else:
                out.append((k, cur[0], cur[1], cur[2], cur[3]))
                cur = [t0, t1, a, b]
        out.append((k, cur[0], cur[1], cur[2], cur[3]))
    return out


def on_line(l, p):
    k, t0, t1, a, b = l
    if k[0] * p[0] + k[1] * p[1] != k[2]:
        return False
    t = param(k, p)
    return t0 <= t <= t1


def inter(l1, l2):
    (a1, b1, c1), (a2, b2, c2) = l1[0], l2[0]
    det = a1 * b2 - a2 * b1
    if det == 0:
        return None
    x = (c1 * b2 - c2 * b1) / det
    y = (a1 * c2 - a2 * c1) / det
    p = (x, y)
    if on_line(l1, p) and on_line(l2, p):
        return p
    return None


# ------------------------------------------------------------------ figure generators (models)

def grid(m, n, u=1, x0=0, y0=0):
    """m columns x n rows of u-sized cells."""
    f = Fig()
    for i in range(m + 1):
        f.add((x0 + i * u, y0), (x0 + i * u, y0 + n * u))
    for j in range(n + 1):
        f.add((x0, y0 + j * u), (x0 + m * u, y0 + j * u))
    return f


def rect(x0, y0, x1, y1):
    return Fig().poly([(x0, y0), (x1, y0), (x1, y1), (x0, y1)])


def tri_apex(k, h, base=12, height=10):
    """Triangle, k lines from the apex to the base (equal parts), h horizontal cuts."""
    B = F(base)
    H = F(height)
    apex = (B / 2, F(0))
    f = Fig().poly([apex, (F(0), H), (B, H)])
    for i in range(1, k + 1):
        f.add(apex, (B * i / (k + 1), H))
    for j in range(1, h + 1):
        y = H * j / (h + 1)
        half = (B / 2) * (y / H)
        f.add((B / 2 - half, y), (B / 2 + half, y))
    return f


def tri_grid(n, u=2):
    """Big triangle cut into n rows of small triangles (n^2 unit triangles)."""
    f = Fig()

    def xy(r, c):
        return (F(u) * (n - r + 2 * c) / 2 * 1, F(u) * r)

    for r in range(n):
        for c in range(r + 1):
            f.poly([xy(r, c), xy(r + 1, c), xy(r + 1, c + 1)])
    return f


# ------------------------------------------------------------------ shape model (isometries)
# A Shape lives on a W x H box (model units). Elements:
#   ("L", (x1,y1), (x2,y2))      segment
#   ("D", (x,y))                 filled dot
#   ("C", (x,y), r)              circle outline
#   ("S", ((x,y),...))           shaded polygon
#   ("O", ((x,y),...))           outline polygon
class Shape:
    def __init__(self, W, H, els=()):
        self.W, self.H = F(W), F(H)
        self.els = [self._norm(e) for e in els]

    @staticmethod
    def _p(p):
        return (F(p[0]), F(p[1]))

    def _norm(self, e):
        k = e[0]
        if k == "L":
            return ("L",) + tuple(sorted([self._p(e[1]), self._p(e[2])]))
        if k == "D":
            return ("D", self._p(e[1]))
        if k == "C":
            return ("C", self._p(e[1]), F(e[2]))
        if k in ("S", "O"):
            return (k, tuple(self._p(p) for p in e[1]))
        raise ValueError(k)

    def map(self, fn, W=None, H=None, only=None):
        """Apply point map fn to all elements (or only to element indexes in `only`)."""
        out = []
        for i, e in enumerate(self.els):
            if only is not None and i not in only:
                out.append(e)
                continue
            k = e[0]
            if k == "L":
                out.append(("L", fn(e[1]), fn(e[2])))
            elif k == "D":
                out.append(("D", fn(e[1])))
            elif k == "C":
                out.append(("C", fn(e[1]), e[2]))
            else:
                out.append((k, tuple(fn(p) for p in e[1])))
        return Shape(W if W is not None else self.W, H if H is not None else self.H, out)

    # isometries of the box
    def mirror(self, **kw):      # vertical mirror: left <-> right
        return self.map(lambda p: (self.W - p[0], p[1]), **kw)

    def water(self, **kw):       # horizontal mirror: top <-> bottom
        return self.map(lambda p: (p[0], self.H - p[1]), **kw)

    def rot180(self, **kw):
        return self.map(lambda p: (self.W - p[0], self.H - p[1]), **kw)

    def rot90(self, **kw):       # clockwise on screen (y down)
        return self.map(lambda p: (self.H - p[1], p[0]), W=self.H, H=self.W, **kw)

    def rot270(self, **kw):      # anticlockwise
        return self.map(lambda p: (p[1], self.W - p[0]), W=self.H, H=self.W, **kw)

    def transpose(self, **kw):   # mirror in the main diagonal
        return self.map(lambda p: (p[1], p[0]), W=self.H, H=self.W, **kw)

    def key(self):
        """Canonical form: equal keys <=> identical drawing."""
        ks = []
        for e in self.els:
            k = e[0]
            if k in ("S", "O"):
                pts = list(e[1])
                n = len(pts)
                cands = []
                for seq in (pts, pts[::-1]):
                    for i in range(n):
                        cands.append(tuple(seq[i:] + seq[:i]))
                ks.append((k, min(cands)))
            elif k == "L":
                ks.append(("L",) + tuple(sorted([e[1], e[2]])))
            else:
                ks.append(e)
        return (self.W, self.H, tuple(sorted(ks)))

    def body(self, u, dx=0, dy=0, sw=None):
        out = []
        T = lambda p: (float(p[0]) * u + dx, float(p[1]) * u + dy)  # noqa
        for e in self.els:
            k = e[0]
            if k == "L":
                a, b = T(e[1]), T(e[2])
                out.append(ln(a[0], a[1], b[0], b[1]))
            elif k == "D":
                a = T(e[1])
                out.append(circ(a[0], a[1], 2.6, True))
            elif k == "C":
                a = T(e[1])
                out.append(circ(a[0], a[1], float(e[2]) * u))
            elif k == "S":
                out.append(poly([T(p) for p in e[1]], SHADE))
            else:
                out.append(poly([T(p) for p in e[1]]))
        return "".join(out)

    def svg(self, u=10, pad=5, frame=False, mirror_line=None):
        """mirror_line: 'right' or 'below' draws a dashed mirror line next to the shape."""
        w = float(self.W) * u + 2 * pad
        h = float(self.H) * u + 2 * pad
        b = self.body(u, pad, pad)
        if frame:
            b = poly([(pad, pad), (w - pad, pad), (w - pad, h - pad), (pad, h - pad)], ' stroke-opacity="0.35"') + b
        if mirror_line == "right":
            b += ln(w + 4, 2, w + 4, h - 2, DASH) + txt(w + 4, h + 9, "M", 9)
            w += 10
            h += 10
        elif mirror_line == "below":
            b += ln(2, h + 4, w - 2, h + 4, DASH)
            h += 8
        return svg(w, h, b)


# ------------------------------------------------------------------ glyph strings (letters/digits)
# A glyph state is (char, fx, fy): fx = flipped left-right, fy = flipped top-bottom.
V_SYM = set("AHIMOTUVWXY08")       # look the same after a left-right flip
H_SYM = set("BCDEHIKOX038")        # look the same after a top-bottom flip
R_SYM = set("HINOSXZ08")           # look the same after a 180 degree turn


def glyph_canon(s):
    ch, fx, fy = s
    if ch == "M" and fy:
        ch, fy = "W", 0
    elif ch == "W" and fy:
        ch, fy = "M", 0
    if ch in R_SYM and fx and fy:
        fx = fy = 0
    if ch in V_SYM:
        fx = 0
    if ch in H_SYM:
        fy = 0
    if ch in R_SYM and fy and not fx:
        fx, fy = 1, 0
    return (ch, fx, fy)


def glyph_key(states):
    return tuple(glyph_canon(s) for s in states)


def g_plain(word):
    return [(c, 0, 0) for c in word]


def g_mirror(states):
    return [(c, 1 - fx, fy) for c, fx, fy in reversed(states)]


def g_water(states):
    return [(c, fx, 1 - fy) for c, fx, fy in states]


def g_rot180(states):
    return g_water(g_mirror(states))


def g_flip_in_place(states):
    """near miss: letters flipped left-right but order not reversed"""
    return [(c, 1 - fx, fy) for c, fx, fy in states]


def g_reverse_only(states):
    """near miss: order reversed but letters not flipped"""
    return list(reversed(states))


def glyph_svg(states, size=16, step=13):
    n = len(states)
    w = 10 + step * n
    parts = []
    for i, (c, fx, fy) in enumerate(states):
        cx = 5 + step * i + step / 2
        tr = ""
        if fx and fy:
            tr = f' transform="translate({num(2 * cx)},26.4) scale(-1,-1)"'
        elif fx:
            tr = f' transform="translate({num(2 * cx)},0) scale(-1,1)"'
        elif fy:
            tr = ' transform="translate(0,26.4) scale(1,-1)"'
        parts.append(f'<text x="{num(cx)}" y="18.8"{tr}>{c}</text>')
    body = (f'<g font-size="{size}" text-anchor="middle" fill="currentColor" stroke="none" '
            f'font-family="sans-serif" font-weight="600">' + "".join(parts) + "</g>")
    return svg(w, 28, body)
