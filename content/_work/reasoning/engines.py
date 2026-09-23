"""Verification engines + SVG builders for reasoning content."""
import itertools
from fractions import Fraction as Fr


def PL(*pts):
    """Turn a polyline point list into a list of ((x1,y1),(x2,y2)) segments."""
    return list(zip(pts, pts[1:]))

# ====================================================================== SVG basics
def svg(w, h, body, sw=1.5):
    return ('<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 %s %s" width="%s" height="%s" fill="none" '
            'stroke="currentColor" stroke-width="%s" stroke-linecap="round" stroke-linejoin="round">%s</svg>'
            % (w, h, w, h, sw, body))


def num(x):
    x = float(x)
    return ('%.2f' % x).rstrip('0').rstrip('.')


def line(x1, y1, x2, y2, dash=False, sw=None):
    extra = ' stroke-dasharray="3 2"' if dash else ''
    if sw:
        extra += ' stroke-width="%s"' % sw
    return '<line x1="%s" y1="%s" x2="%s" y2="%s"%s/>' % (num(x1), num(y1), num(x2), num(y2), extra)


def poly(pts, fill=False, closed=True, dash=False, op=None):
    tag = 'polygon' if closed else 'polyline'
    f = ' fill="currentColor"' if fill else ''
    if fill and op:
        f += ' fill-opacity="%s"' % op
    d = ' stroke-dasharray="3 2"' if dash else ''
    return '<%s points="%s"%s%s/>' % (tag, ' '.join('%s,%s' % (num(x), num(y)) for x, y in pts), f, d)


def circ(cx, cy, r, fill=False, op=None):
    f = ' fill="currentColor"' if fill else ''
    if fill and op:
        f += ' fill-opacity="%s"' % op
    return '<circle cx="%s" cy="%s" r="%s"%s/>' % (num(cx), num(cy), num(r), f)


def text(x, y, s, size=12, anchor='middle', transform=None, weight=None):
    tr = ' transform="%s"' % transform if transform else ''
    wt = ' font-weight="%s"' % weight if weight else ''
    s = str(s).replace('&', '&amp;').replace('<', '&lt;').replace('>', '&gt;')
    return ('<text x="%s" y="%s" font-size="%s" text-anchor="%s" fill="currentColor" stroke="none" '
            'font-family="sans-serif"%s%s>%s</text>' % (num(x), num(y), size, anchor, wt, tr, s))


# ====================================================================== blood relations
class Fam:
    """Tiny family graph. rel(a,b) -> what a is to b."""

    def __init__(self):
        self.g, self.par, self.sp, self.grp = {}, {}, {}, {}

    def add(self, *ns):
        for n in ns:
            self.g.setdefault(n, None)
            self.par.setdefault(n, set())
            self.grp.setdefault(n, n)

    def m(self, *ns):
        for n in ns:
            self.add(n)
            self.g[n] = 'M'
        return self

    def f(self, *ns):
        for n in ns:
            self.add(n)
            self.g[n] = 'F'
        return self

    def child(self, c, parent):
        self.add(c, parent)
        self.par[c].add(parent)
        return self

    def marry(self, a, b):
        self.add(a, b)
        self.sp[a] = b
        self.sp[b] = a
        return self

    def _root(self, x):
        while self.grp[x] != x:
            x = self.grp[x]
        return x

    def sib(self, a, b):
        self.add(a, b)
        ra, rb = self._root(a), self._root(b)
        if ra != rb:
            self.grp[ra] = rb
        return self

    def close(self):
        changed = True
        while changed:
            changed = False
            for c, ps in self.par.items():
                for x in list(ps):
                    s = self.sp.get(x)
                    if s and s not in ps:
                        ps.add(s)
                        changed = True
            # common parent -> same sibling group
            names = list(self.g)
            for a, b in itertools.combinations(names, 2):
                if self.par[a] & self.par[b] and self._root(a) != self._root(b):
                    self.grp[self._root(a)] = self._root(b)
                    changed = True
            # sibling groups share parents
            groups = {}
            for n in names:
                groups.setdefault(self._root(n), []).append(n)
            for mem in groups.values():
                u = set().union(*[self.par[x] for x in mem])
                for x in mem:
                    if self.par[x] != u:
                        self.par[x] = set(u)
                        changed = True
        return self

    def sibs(self, x):
        r = self._root(x)
        return {n for n in self.g if n != x and self._root(n) == r}

    def rel(self, a, b):
        self.close()
        g = self.g[a]

        def t(mt, ft, nt):
            return mt if g == 'M' else ft if g == 'F' else nt
        P, S, sp = self.par, self.sibs, self.sp.get
        if sp(b) == a:
            return t('husband', 'wife', 'spouse')
        if a in P[b]:
            return t('father', 'mother', 'parent')
        if b in P[a]:
            return t('son', 'daughter', 'child')
        if a in S(b):
            return t('brother', 'sister', 'sibling')
        gp = set().union(*[P[x] for x in P[b]]) if P[b] else set()
        if a in gp:
            return t('grandfather', 'grandmother', 'grandparent')
        ggp = set().union(*[P[x] for x in gp]) if gp else set()
        if a in ggp:
            return t('great-grandfather', 'great-grandmother', 'great-grandparent')
        gpa = set().union(*[P[x] for x in P[a]]) if P[a] else set()
        if b in gpa:
            return t('grandson', 'granddaughter', 'grandchild')
        ggpa = set().union(*[P[x] for x in gpa]) if gpa else set()
        if b in ggpa:
            return t('great-grandson', 'great-granddaughter', 'great-grandchild')
        for x in P[b]:
            side = {'M': 'paternal', 'F': 'maternal'}.get(self.g[x], '?')
            if a in S(x):
                return side + ' ' + t('uncle', 'aunt', 'uncle/aunt')
            for s in S(x):
                if sp(s) == a:
                    return t('uncle', 'aunt', 'uncle/aunt') + ' (by marriage, %s)' % side
        for s in S(b):
            if s in P[a]:
                return t('nephew', 'niece', 'nephew/niece')
        if sp(b):
            for s in S(sp(b)):
                if s in P[a]:
                    return t('nephew', 'niece', 'nephew/niece')
        for x in P[a]:
            for y in P[b]:
                if x in S(y):
                    return 'cousin'
        if sp(b) and a in P[sp(b)]:
            return t('father-in-law', 'mother-in-law', 'parent-in-law')
        if sp(a) and b in P[sp(a)]:
            return t('son-in-law', 'daughter-in-law', 'child-in-law')
        if sp(b) and a in S(sp(b)):
            return t('brother-in-law', 'sister-in-law', 'sibling-in-law')
        for s in S(b):
            if sp(s) == a:
                return t('brother-in-law', 'sister-in-law', 'sibling-in-law')
        if sp(b):
            for s in S(sp(b)):
                if sp(s) == a:
                    return t('brother-in-law (co-brother)', 'sister-in-law (co-sister)', 'in-law')
        # grand nephew / grand niece: child of nephew
        for s in S(b):
            kids = {k for k in self.g if s in P[k]}
            for k in kids:
                if k in P[a]:
                    return t('grandnephew', 'grandniece', 'grandnephew/niece')
        return None


# ====================================================================== syllogism
def _models(cats):
    n = len(cats)
    regions = list(range(1, 2 ** n))
    for mask in range(1, 2 ** len(regions)):
        present = [r for i, r in enumerate(regions) if mask >> i & 1]
        if all(any(r >> j & 1 for r in present) for j in range(n)):
            yield present


def _holds(st, present, idx):
    kind, A, B = st
    a, b = 1 << idx[A], 1 << idx[B]
    if kind == 'all':
        return not any(r & a and not r & b for r in present)
    if kind == 'no':
        return not any(r & a and r & b for r in present)
    if kind == 'some':
        return any(r & a and r & b for r in present)
    if kind == 'snot':
        return any(r & a and not r & b for r in present)
    raise ValueError(kind)


def syllogism(premises, conclusions):
    """premises/conclusions: tuples (kind, A, B); kind in all/no/some/snot;
    a conclusion may be ('can', (kind,A,B)) = possibility. Returns list of booleans (follows?)."""
    cats = sorted({x for st in premises for x in st[1:]} |
                  {x for c in conclusions for x in (c[1][1:] if c[0] == 'can' else c[1:])})
    assert len(cats) <= 4, cats
    idx = {c: i for i, c in enumerate(cats)}
    models = [m for m in _models(cats) if all(_holds(pr, m, idx) for pr in premises)]
    assert models, 'premises inconsistent'
    out = []
    for c in conclusions:
        if c[0] == 'can':
            out.append(any(_holds(c[1], m, idx) for m in models))
        else:
            out.append(all(_holds(c, m, idx) for m in models))
    return out


def syl_answer(premises, concl, with_either=False):
    """map to the standard 4/5-option answer text for two conclusions"""
    f = syllogism(premises, concl)
    if len(concl) == 2:
        if f == [True, True]:
            return 'Both conclusions I and II follow'
        if f == [True, False]:
            return 'Only conclusion I follows'
        if f == [False, True]:
            return 'Only conclusion II follows'
        # neither: check complementary pair
        c1, c2 = concl
        comp = False
        if c1[0] != 'can' and c2[0] != 'can' and {c1[1], c1[2]} == {c2[1], c2[2]}:
            kinds = {c1[0], c2[0]}
            if (kinds == {'some', 'no'}) or (kinds == {'all', 'snot'} and c1[1:] == c2[1:]):
                comp = True
        if comp:
            assert with_either, 'either-or case: needs Either option'
            return 'Either conclusion I or II follows'
        return 'Neither conclusion I nor II follows'
    raise ValueError


# ====================================================================== geometry: counting
def _line_key(p1, p2):
    (x1, y1), (x2, y2) = p1, p2
    a, b = y2 - y1, x1 - x2
    c = a * x1 + b * y1
    k = a if a != 0 else b
    return (Fr(a) / k, Fr(b) / k, Fr(c) / k)


def _param(p, base, d):
    return (Fr(p[0]) - base[0]) * d[0] + (Fr(p[1]) - base[1]) * d[1]


def maximal_segments(segs):
    segs = [((Fr(a), Fr(b)), (Fr(c), Fr(d))) for (a, b), (c, d) in segs]
    groups = {}
    for p1, p2 in segs:
        groups.setdefault(_line_key(p1, p2), []).append((p1, p2))
    out = []
    for k, ss in groups.items():
        base = ss[0][0]
        d = (ss[0][1][0] - ss[0][0][0], ss[0][1][1] - ss[0][0][1])
        iv = []
        for p1, p2 in ss:
            t1, t2 = _param(p1, base, d), _param(p2, base, d)
            pts = sorted([(t1, p1), (t2, p2)])
            iv.append(pts)
        iv.sort()
        cur = iv[0]
        for nx in iv[1:]:
            if nx[0][0] <= cur[1][0]:
                if nx[1][0] > cur[1][0]:
                    cur = [cur[0], nx[1]]
            else:
                out.append((cur[0][1], cur[1][1]))
                cur = nx
        out.append((cur[0][1], cur[1][1]))
    return out


def _on_seg(p, s):
    (x1, y1), (x2, y2) = s
    x, y = p
    if (x2 - x1) * (y - y1) - (y2 - y1) * (x - x1) != 0:
        return False
    return min(x1, x2) <= x <= max(x1, x2) and min(y1, y2) <= y <= max(y1, y2)


def _intersect(s, t):
    (x1, y1), (x2, y2) = s
    (x3, y3), (x4, y4) = t
    den = (x1 - x2) * (y3 - y4) - (y1 - y2) * (x3 - x4)
    if den == 0:
        return None
    px = ((x1 * y2 - y1 * x2) * (x3 - x4) - (x1 - x2) * (x3 * y4 - y3 * x4)) / den
    py = ((x1 * y2 - y1 * x2) * (y3 - y4) - (y1 - y2) * (x3 * y4 - y3 * x4)) / den
    p = (px, py)
    if _on_seg(p, s) and _on_seg(p, t):
        return p
    return None


def _points(ms):
    pts = set()
    for s in ms:
        pts.add(s[0])
        pts.add(s[1])
    for s, t in itertools.combinations(ms, 2):
        q = _intersect(s, t)
        if q:
            pts.add(q)
    return pts


def count_triangles(segs):
    ms = maximal_segments(segs)
    pts = sorted(_points(ms))
    on = {q: [i for i, s in enumerate(ms) if _on_seg(q, s)] for q in pts}

    def conn(a, b):
        return bool(set(on[a]) & set(on[b]))
    n = 0
    for a, b, c in itertools.combinations(pts, 3):
        if (b[0] - a[0]) * (c[1] - a[1]) - (b[1] - a[1]) * (c[0] - a[0]) == 0:
            continue
        if conn(a, b) and conn(b, c) and conn(a, c):
            # the connecting segment must be the side itself: common segment containing both points
            n += 1
    return n


def count_rects(segs, squares_only=False):
    """axis-aligned rectangles whose 4 sides lie on drawn segments"""
    ms = maximal_segments(segs)
    pts = _points(ms)

    def covered(a, b):
        return any(_on_seg(a, s) and _on_seg(b, s) for s in ms)
    xs = sorted({q[0] for q in pts})
    ys = sorted({q[1] for q in pts})
    n = 0
    for x1, x2 in itertools.combinations(xs, 2):
        for y1, y2 in itertools.combinations(ys, 2):
            if squares_only and (x2 - x1) != (y2 - y1):
                continue
            A, B, C, D = (x1, y1), (x2, y1), (x2, y2), (x1, y2)
            if covered(A, B) and covered(B, C) and covered(C, D) and covered(D, A):
                n += 1
    return n


def seg_svg(segs, scale=10, pad=4, sw=1.5, extra=''):
    xs = [c for s in segs for c in (s[0][0], s[1][0])]
    ys = [c for s in segs for c in (s[0][1], s[1][1])]
    w = (max(xs) - min(xs)) * scale + 2 * pad
    h = (max(ys) - min(ys)) * scale + 2 * pad
    ox, oy = min(xs), min(ys)
    body = ''.join(line((a[0] - ox) * scale + pad, (a[1] - oy) * scale + pad,
                        (b[0] - ox) * scale + pad, (b[1] - oy) * scale + pad) for a, b in segs)
    return svg(num(w), num(h), body + extra, sw)


# ====================================================================== paper folding
def reflect(pt, l1, l2):
    (x, y), (x1, y1), (x2, y2) = [tuple(map(Fr, v)) for v in (pt, l1, l2)]
    dx, dy = x2 - x1, y2 - y1
    t = ((x - x1) * dx + (y - y1) * dy) / (dx * dx + dy * dy)
    fx, fy = x1 + t * dx, y1 + t * dy
    return (2 * fx - x, 2 * fy - y)


def _side(pt, l1, l2):
    (x, y), (x1, y1), (x2, y2) = pt, l1, l2
    return (x2 - x1) * (y - y1) - (y2 - y1) * (x - x1)


def clip(polyg, l1, l2, keep_pt):
    """keep the part of convex polygon on the same side of line as keep_pt"""
    s0 = _side(keep_pt, l1, l2)
    assert s0 != 0
    out = []
    n = len(polyg)
    for i in range(n):
        P, Qp = polyg[i], polyg[(i + 1) % n]
        sp_, sq = _side(P, l1, l2) * s0, _side(Qp, l1, l2) * s0
        if sp_ >= 0:
            out.append(P)
        if (sp_ > 0 and sq < 0) or (sp_ < 0 and sq > 0):
            t = sp_ / (sp_ - sq)
            out.append((P[0] + t * (Qp[0] - P[0]), P[1] + t * (Qp[1] - P[1])))
    # dedupe
    res = []
    for q in out:
        if not res or res[-1] != q:
            res.append(q)
    if len(res) > 1 and res[0] == res[-1]:
        res.pop()
    return res


def inside(pt, polyg):
    """strict interior of convex polygon"""
    signs = []
    n = len(polyg)
    for i in range(n):
        s = _side(pt, polyg[i], polyg[(i + 1) % n])
        if s == 0:
            return False
        signs.append(s > 0)
    return all(signs) or not any(signs)


def fold_sim(side, folds, punches):
    """folds: list of (l1, l2, keep_pt). Returns (regions list, final hole set)."""
    reg = [[(Fr(0), Fr(0)), (Fr(side), Fr(0)), (Fr(side), Fr(side)), (Fr(0), Fr(side))]]
    for l1, l2, kp in folds:
        l1, l2, kp = tuple(map(Fr, l1)), tuple(map(Fr, l2)), tuple(map(Fr, kp))
        reg.append(clip(reg[-1], l1, l2, kp))
    holes = {tuple(map(Fr, q)) for q in punches}
    for q in holes:
        assert inside(q, reg[-1]), ('punch outside final region', q)
    for k in range(len(folds) - 1, -1, -1):
        l1, l2, kp = folds[k]
        prev = reg[k]
        new = set(holes)
        for q in holes:
            r = reflect(q, l1, l2)
            if inside(r, prev):
                new.add(r)
        holes = new
    return reg, holes


def _arrow(x1, y1, x2, y2):
    import math
    ang = math.atan2(y2 - y1, x2 - x1)
    a1, a2 = ang + 2.6, ang - 2.6
    h = 4
    return (line(x1, y1, x2, y2) +
            poly([(x2 + h * math.cos(a1), y2 + h * math.sin(a1)), (x2, y2),
                  (x2 + h * math.cos(a2), y2 + h * math.sin(a2))], closed=False))


def _centroid(pg):
    return (sum(q[0] for q in pg) / len(pg), sum(q[1] for q in pg) / len(pg))


def fold_question_svg(side, folds, punches, scale=12, pad=7, cut_shape='circle'):
    reg, _ = fold_sim(side, folds, punches)
    panel = side * scale + 2 * pad
    gap = 10
    body = ''
    n = len(folds)
    for k in range(n + 1):
        ox = k * (panel + gap)
        tf = lambda q: (ox + pad + float(q[0]) * scale, pad + float(q[1]) * scale)
        # ghost of the full sheet for orientation
        body += poly([tf(q) for q in reg[0]], dash=True) if k > 0 else ''
        body += poly([tf(q) for q in reg[k]], fill=True, op='0.12')
        body += poly([tf(q) for q in reg[k]])
        if k < n:
            l1, l2, kp = folds[k]
            # fold line clipped to the region: draw across the region bounds
            a = tf(l1)
            b = tf(l2)
            body += line(a[0], a[1], b[0], b[1], dash=True, sw=1.2)
            # moving part centroid -> reflected
            l1f, l2f = tuple(map(Fr, l1)), tuple(map(Fr, l2))
            other = [q for q in reg[k]]
            # pick a point in the moving part: reflect keep point
            mv = reflect(tuple(map(Fr, kp)), l1f, l2f)
            mpart = clip(reg[k], l1f, l2f, mv)
            c1 = _centroid(mpart)
            c2 = reflect(c1, l1f, l2f)
            p1, p2 = tf(c1), tf(c2)
            # shorten arrow
            body += _arrow(p1[0] + (p2[0] - p1[0]) * 0.15, p1[1] + (p2[1] - p1[1]) * 0.15,
                           p1[0] + (p2[0] - p1[0]) * 0.8, p1[1] + (p2[1] - p1[1]) * 0.8)
        else:
            for q in punches:
                c = tf(q)
                body += circ(c[0], c[1], 2.6, fill=True) if cut_shape == 'circle' else ''
        if k < n:
            body += text(ox + panel + gap / 2, panel / 2 + 3, '→', 9)
    W = (n + 1) * panel + n * gap
    return svg(num(W), num(panel), body, 1.2)


def holes_svg(side, holes, scale=12, pad=6):
    s = side * scale + 2 * pad
    body = poly([(pad, pad), (pad + side * scale, pad), (pad + side * scale, pad + side * scale), (pad, pad + side * scale)])
    for q in sorted(holes):
        body += circ(pad + float(q[0]) * scale, pad + float(q[1]) * scale, 2.6, fill=True)
    return svg(num(s), num(s), body, 1.2)


# ====================================================================== embedded figures
def prims(segs):
    """decompose integer-grid segments (H, V or 45-degree) into unit primitives"""
    out = set()
    for (x1, y1), (x2, y2) in segs:
        dx, dy = x2 - x1, y2 - y1
        n = max(abs(dx), abs(dy))
        assert dx == 0 or dy == 0 or abs(dx) == abs(dy), 'only H/V/diagonal'
        sx, sy = (dx > 0) - (dx < 0), (dy > 0) - (dy < 0)
        for i in range(n):
            a = (x1 + i * sx, y1 + i * sy)
            b = (a[0] + sx, a[1] + sy)
            out.add(tuple(sorted([a, b])))
    return out


def embeds(main_segs, part_segs):
    M, O = prims(main_segs), prims(part_segs)
    mx = [c for pr in M for pt in pr for c in pt]
    xs = [pt[0] for pr in M for pt in pr]
    ys = [pt[1] for pr in M for pt in pr]
    oxs = [pt[0] for pr in O for pt in pr]
    oys = [pt[1] for pr in O for pt in pr]
    hits = []
    for tx in range(min(xs) - min(oxs), max(xs) - max(oxs) + 1):
        for ty in range(min(ys) - min(oys), max(ys) - max(oys) + 1):
            moved = {tuple(sorted([(a[0] + tx, a[1] + ty), (b[0] + tx, b[1] + ty)])) for a, b in O}
            if moved <= M:
                hits.append((tx, ty))
    return hits


def grid_svg(segs, scale=9, pad=4, size=None):
    xs = [c for s in segs for c in (s[0][0], s[1][0])]
    ys = [c for s in segs for c in (s[0][1], s[1][1])]
    if size:
        W, H = size
    else:
        W, H = max(xs), max(ys)
    ox, oy = 0, 0
    body = ''.join(line(a[0] * scale + pad, a[1] * scale + pad, b[0] * scale + pad, b[1] * scale + pad) for a, b in segs)
    return svg(num(W * scale + 2 * pad), num(H * scale + 2 * pad), body, 1.4)


def normalize(segs):
    xs = [c for s in segs for c in (s[0][0], s[1][0])]
    ys = [c for s in segs for c in (s[0][1], s[1][1])]
    mx, my = min(xs), min(ys)
    return [((a[0] - mx, a[1] - my), (b[0] - mx, b[1] - my)) for a, b in segs]


# ====================================================================== dice / cube
POS = ['U', 'D', 'F', 'B', 'L', 'R']
OPP = {'U': 'D', 'D': 'U', 'F': 'B', 'B': 'F', 'L': 'R', 'R': 'L'}


def _rot_yaw(c):
    n = dict(c)
    n['R'], n['B'], n['L'], n['F'] = c['F'], c['R'], c['B'], c['L']
    return n


def _rot_pitch(c):
    n = dict(c)
    n['F'], n['D'], n['B'], n['U'] = c['U'], c['F'], c['D'], c['B']
    return n


def rotations(c):
    seen, todo = [], [dict(c)]
    keyf = lambda d: tuple(d[p] for p in POS)
    keys = set()
    while todo:
        x = todo.pop()
        k = keyf(x)
        if k in keys:
            continue
        keys.add(k)
        seen.append(x)
        todo += [_rot_yaw(x), _rot_pitch(x)]
    assert len(seen) == 24
    return seen


def view_ok(cube, view):
    top, front, right = view
    return any(r['U'] == top and r['F'] == front and r['R'] == right for r in rotations(cube))


def dice_solutions(labels, views):
    sols = []
    seen = set()
    for perm in itertools.permutations(labels):
        c = dict(zip(POS, perm))
        canon = min(tuple(r[p] for p in POS) for r in rotations(c))
        if canon in seen:
            continue
        seen.add(canon)
        if all(view_ok(c, v) for v in views):
            sols.append(c)
    return sols


def opposite_of(cube, lab):
    for p_, v in cube.items():
        if v == lab:
            return cube[OPP[p_]]


def fold_net(net):
    """net: dict (x,y)->label. Returns cube dict U,D,F,B,L,R for the net printed side OUT,
    with the first-listed cell as the TOP face."""
    cells = list(net)
    start = cells[0]
    # rolling: state world-dir -> body-face
    init = {d: d for d in ['D', 'U', 'N', 'S', 'E', 'W']}
    moves = {(1, 0): 'E', (-1, 0): 'W', (0, 1): 'S', (0, -1): 'N'}

    def roll(st, d):
        n = dict(st)
        if d == 'E':
            n['D'], n['W'], n['U'], n['E'] = st['E'], st['D'], st['W'], st['U']
        elif d == 'W':
            n['D'], n['E'], n['U'], n['W'] = st['W'], st['D'], st['E'], st['U']
        elif d == 'S':
            n['D'], n['N'], n['U'], n['S'] = st['S'], st['D'], st['N'], st['U']
        elif d == 'N':
            n['D'], n['S'], n['U'], n['N'] = st['N'], st['D'], st['S'], st['U']
        return n
    body = {}
    stack = [(start, init)]
    seen = {start}
    while stack:
        cell, st = stack.pop()
        assert st['D'] not in body, 'invalid net (face reused)'
        body[st['D']] = net[cell]
        for (dx, dy), d in moves.items():
            nb = (cell[0] + dx, cell[1] + dy)
            if nb in net and nb not in seen:
                seen.add(nb)
                stack.append((nb, roll(st, d)))
    assert len(body) == 6, 'invalid net'
    # rolling = printed-side-in; reflect top/bottom to get printed-side-out
    return {'U': body['D'], 'D': body['U'], 'F': body['S'], 'B': body['N'], 'R': body['E'], 'L': body['W']}


def cube_svg(top, front, right, size=34):
    s, dpt = size, size * 0.5
    x0, y0 = 4, 4 + dpt
    F = [(x0, y0), (x0 + s, y0), (x0 + s, y0 + s), (x0, y0 + s)]
    Tp = [(x0, y0), (x0 + s, y0), (x0 + s + dpt, y0 - dpt), (x0 + dpt, y0 - dpt)]
    R = [(x0 + s, y0), (x0 + s + dpt, y0 - dpt), (x0 + s + dpt, y0 + s - dpt), (x0 + s, y0 + s)]
    body = poly(F) + poly(Tp) + poly(R)
    body += text(x0 + s / 2, y0 + s / 2 + 5, front, 14)
    body += text(x0 + s / 2 + dpt / 2, y0 - dpt / 2 + 4, top, 10)
    body += text(x0 + s + dpt / 2, y0 + s / 2 - dpt / 2 + 4, right, 10)
    W = x0 + s + dpt + 4
    H = y0 + s + 4
    return svg(num(W), num(H), body, 1.3)


def dice_row_svg(views, size=34):
    parts = []
    s, dpt = size, size * 0.5
    unit = 4 + s + dpt + 4 + 6
    body = ''
    for i, (t, f, r) in enumerate(views):
        ox = i * unit
        x0, y0 = ox + 4, 4 + dpt
        F = [(x0, y0), (x0 + s, y0), (x0 + s, y0 + s), (x0, y0 + s)]
        Tp = [(x0, y0), (x0 + s, y0), (x0 + s + dpt, y0 - dpt), (x0 + dpt, y0 - dpt)]
        R = [(x0 + s, y0), (x0 + s + dpt, y0 - dpt), (x0 + s + dpt, y0 + s - dpt), (x0 + s, y0 + s)]
        body += poly(F) + poly(Tp) + poly(R)
        body += text(x0 + s / 2, y0 + s / 2 + 5, f, 14)
        body += text(x0 + s / 2 + dpt / 2, y0 - dpt / 2 + 4, t, 10)
        body += text(x0 + s + dpt / 2, y0 + s / 2 - dpt / 2 + 4, r, 10)
    W = len(views) * unit - 6
    H = 4 + dpt + s + 4
    return svg(num(W), num(H), body, 1.3)


def net_svg(net, cell=24, pad=3):
    xs = [c[0] for c in net]
    ys = [c[1] for c in net]
    body = ''
    for (x, y), lab in net.items():
        X, Y = pad + (x - min(xs)) * cell, pad + (y - min(ys)) * cell
        body += poly([(X, Y), (X + cell, Y), (X + cell, Y + cell), (X, Y + cell)])
        body += text(X + cell / 2, Y + cell / 2 + 5, lab, 13)
    W = (max(xs) - min(xs) + 1) * cell + 2 * pad
    H = (max(ys) - min(ys) + 1) * cell + 2 * pad
    return svg(num(W), num(H), body, 1.3)


# ====================================================================== mirror / water images (text)
def string_image_svg(s, order_rev, hflip, vflip, fs=16, cw=13):
    n = len(s)
    chars = list(reversed(s)) if order_rev else list(s)
    W = n * cw + 10
    H = fs + 12
    base = 6 + fs * 0.8
    cy = base - fs * 0.35
    body = ''
    for i, ch in enumerate(chars):
        cx = 5 + cw * i + cw / 2
        tr = []
        if hflip:
            tr.append('translate(%s,0) scale(-1,1)' % num(2 * cx))
        if vflip:
            tr.append('translate(0,%s) scale(1,-1)' % num(2 * cy))
        body += text(cx, base, ch, fs, transform=' '.join(tr) if tr else None, weight='600')
    return svg(num(W), num(H), body)


# ====================================================================== figure-series renderer
SLOTS = [(0, 0), (1, 0), (2, 0), (2, 1), (2, 2), (1, 2), (0, 2), (0, 1)]  # clockwise from top-left


def shape_at(kind, cx, cy, r=4.2):
    if kind == 'dot':
        return circ(cx, cy, r * 0.8, fill=True)
    if kind == 'ring':
        return circ(cx, cy, r * 0.85)
    if kind == 'sq':
        return poly([(cx - r * .8, cy - r * .8), (cx + r * .8, cy - r * .8), (cx + r * .8, cy + r * .8), (cx - r * .8, cy + r * .8)], fill=True)
    if kind == 'tri':
        return poly([(cx, cy - r), (cx + r, cy + r * .8), (cx - r, cy + r * .8)])
    if kind == 'x':
        return line(cx - r * .8, cy - r * .8, cx + r * .8, cy + r * .8) + line(cx - r * .8, cy + r * .8, cx + r * .8, cy - r * .8)
    if kind == 'plus':
        return line(cx - r, cy, cx + r, cy) + line(cx, cy - r, cx, cy + r)
    raise ValueError(kind)


ARROW_DIRS = {0: (0, -1), 1: (1, -1), 2: (1, 0), 3: (1, 1), 4: (0, 1), 5: (-1, 1), 6: (-1, 0), 7: (-1, -1)}


def frame_svg(state, size=46, pad=3):
    """state: dict with optional keys slots{idx:kind}, arrow (0-7, 0=up, clockwise), shade (0-3 quadrant TL,TR,BR,BL),
    lines (int, short strokes at bottom-centre), diag (bool)"""
    s = size
    body = ''
    o = pad
    if state.get('shade') is not None:
        q = state['shade']
        qx = [(o, o), (o + s / 2, o), (o + s / 2, o + s / 2), (o, o + s / 2)]
        offs = {0: (0, 0), 1: (s / 2, 0), 2: (s / 2, s / 2), 3: (0, s / 2)}[q]
        body += poly([(x + offs[0], y + offs[1]) for x, y in qx], fill=True, op='0.35')
    body += poly([(o, o), (o + s, o), (o + s, o + s), (o, o + s)])
    if state.get('cross'):
        body += line(o + s / 2, o, o + s / 2, o + s, dash=True, sw=0.8) + line(o, o + s / 2, o + s, o + s / 2, dash=True, sw=0.8)
    for idx, kind in state.get('slots', {}).items():
        gx, gy = SLOTS[idx % 8]
        cx = o + 6 + gx * (s - 12) / 2
        cy = o + 6 + gy * (s - 12) / 2
        body += shape_at(kind, cx, cy)
    if state.get('arrow') is not None:
        dx, dy = ARROW_DIRS[state['arrow'] % 8]
        import math
        ln = 11 / math.hypot(dx, dy)
        cx, cy = o + s / 2, o + s / 2
        x2, y2 = cx + dx * ln, cy + dy * ln
        x1, y1 = cx - dx * ln, cy - dy * ln
        body += _arrow(x1, y1, x2, y2)
    if state.get('lines'):
        n = state['lines']
        for i in range(n):
            x = o + s / 2 - (n - 1) * 2.5 + i * 5
            body += line(x, o + s / 2 - 5, x, o + s / 2 + 5)
    return body, s + 2 * pad


def frame_only(state):
    b, w = frame_svg(state)
    return svg(num(w), num(w), b)


def series_row_svg(states, qmark=True):
    body = ''
    unit = None
    x = 0
    for st in states:
        b, w = frame_svg(st)
        body += '<g transform="translate(%s,0)">%s</g>' % (num(x), b)
        x += w + 6
        unit = w
    if qmark:
        body += poly([(x + 3, 3), (x + unit - 3, 3), (x + unit - 3, unit - 3), (x + 3, unit - 3)], dash=True)
        body += text(x + unit / 2, unit / 2 + 6, '?', 18)
        x += unit
    else:
        x -= 6
    return svg(num(x), num(unit), body)


# ====================================================================== venn helpers
def venn3_svg(labels, counts, names=None, W=170, H=150):
    """3 circles A(left) B(right) C(bottom) with numbers in regions.
    counts: dict with keys among 'a','b','c','ab','ac','bc','abc'. verified by point-in-circle."""
    C = {'a': (62, 58), 'b': (108, 58), 'c': (85, 98)}
    r = 40
    pos = {'a': (42, 48), 'b': (128, 48), 'c': (85, 122), 'ab': (85, 40), 'ac': (57, 88), 'bc': (113, 88), 'abc': (85, 72)}
    import math
    for key, (x, y) in pos.items():
        ins = ''.join(k for k in 'abc' if math.hypot(x - C[k][0], y - C[k][1]) < r)
        assert ins == key, (key, ins)
    body = ''.join(circ(cx, cy, r) for cx, cy in C.values())
    for key, v in counts.items():
        x, y = pos[key]
        body += text(x, y + 4, v, 11)
    lab = {'a': (18, 16), 'b': (152, 16), 'c': (85, 146)}
    for k, nm in labels.items():
        x, y = lab[k]
        body += text(x, y, nm, 10)
    return svg(W, H, body, 1.3)


def venn_config_svg(kind):
    """relation diagrams for 'best represents' questions. Returns (svg, pairwise relation dict)."""
    r = 16
    body = ''
    if kind == 'nested3':      # A in B in C
        body = circ(45, 38, 34) + circ(45, 42, 22) + circ(45, 46, 10)
        W, H = 90, 78
    elif kind == 'disjoint3':
        body = circ(18, 30, 13) + circ(50, 30, 13) + circ(82, 30, 13)
        W, H = 100, 60
    elif kind == 'two_in_one':  # A, B disjoint inside C
        body = circ(45, 38, 34) + circ(30, 38, 11) + circ(60, 38, 11)
        W, H = 90, 78
    elif kind == 'in_plus_out':  # A inside B, C separate
        body = circ(30, 34, 26) + circ(30, 38, 11) + circ(80, 34, 14)
        W, H = 104, 68
    elif kind == 'overlap3':     # all three mutually overlapping
        body = circ(34, 32, 20) + circ(58, 32, 20) + circ(46, 52, 20)
        W, H = 92, 80
    elif kind == 'overlap_plus_out':  # A,B overlap, C separate
        body = circ(26, 34, 18) + circ(50, 34, 18) + circ(92, 34, 14)
        W, H = 114, 68
    elif kind == 'chain':        # A-B overlap, B-C overlap, A,C disjoint
        body = circ(22, 32, 18) + circ(50, 32, 18) + circ(78, 32, 18)
        W, H = 100, 64
    elif kind == 'overlap_in_one':  # A,B overlap, both inside C
        body = circ(45, 38, 34) + circ(35, 38, 14) + circ(55, 38, 14)
        W, H = 90, 78
    elif kind == 'in_overlap':   # A inside B, B overlaps C, A not touching C
        body = circ(34, 36, 26) + circ(26, 36, 9) + circ(66, 36, 18)
        W, H = 92, 72
    elif kind == 'two_overlap_in':  # A inside C, B overlaps C (B not touching A)
        body = circ(34, 36, 26) + circ(24, 36, 9) + circ(62, 36, 16)
        W, H = 88, 72
    else:
        raise ValueError(kind)
    return svg(W, H, body, 1.4)


VENN_REL = {
    # pairwise relations between circles 0,1,2 (unordered pairs) : 'sub01' means 0 subset of 1
    'nested3': {(0, 1): 'in', (1, 2): 'in', (0, 2): 'in'},
    'disjoint3': {(0, 1): 'dis', (1, 2): 'dis', (0, 2): 'dis'},
    'two_in_one': {(0, 2): 'in', (1, 2): 'in', (0, 1): 'dis'},
    'in_plus_out': {(0, 1): 'in', (0, 2): 'dis', (1, 2): 'dis'},
    'overlap3': {(0, 1): 'ov', (1, 2): 'ov', (0, 2): 'ov'},
    'overlap_plus_out': {(0, 1): 'ov', (0, 2): 'dis', (1, 2): 'dis'},
    'chain': {(0, 1): 'ov', (1, 2): 'ov', (0, 2): 'dis'},
    'overlap_in_one': {(0, 2): 'in', (1, 2): 'in', (0, 1): 'ov'},
    'in_overlap': {(0, 1): 'in', (1, 2): 'ov', (0, 2): 'dis'},
}


def venn_matches(kind, rel):
    """rel: dict {(X,Y): 'in'(X subset Y)|'ov'|'dis'} over three class names. True if some assignment of
    classes to circles reproduces the diagram's relations exactly."""
    names = sorted({n for k in rel for n in k})
    assert len(names) == 3

    def get(R, a, b):
        if (a, b) in R:
            return R[(a, b)]
        if (b, a) in R:
            v = R[(b, a)]
            return {'in': 'has', 'has': 'in'}.get(v, v)
        raise KeyError((a, b))
    D = VENN_REL[kind]
    for perm in itertools.permutations(names):
        ok = True
        for i, j in itertools.combinations(range(3), 2):
            if get(D, i, j) != get(rel, perm[i], perm[j]):
                ok = False
                break
        if ok:
            return True
    return False


# ====================================================================== direction
DIRV = {'N': (0, 1), 'S': (0, -1), 'E': (1, 0), 'W': (-1, 0)}
LEFT = {'N': 'W', 'W': 'S', 'S': 'E', 'E': 'N'}
RIGHT = {v: k for k, v in LEFT.items()}


def walk(start_dir, steps):
    """steps: list of ('F',d) forward d, ('L',d) turn left then d, ('R',d) turn right then d, ('A','N',d) absolute."""
    x = y = 0
    d = start_dir
    for st in steps:
        if st[0] == 'A':
            d = st[1]
            dist = st[2]
        else:
            t, dist = st
            if t == 'L':
                d = LEFT[d]
            elif t == 'R':
                d = RIGHT[d]
        x += DIRV[d][0] * dist
        y += DIRV[d][1] * dist
    return x, y, d


def dir_name(x, y):
    ns = 'North' if y > 0 else 'South' if y < 0 else ''
    ew = 'East' if x > 0 else 'West' if x < 0 else ''
    if ns and ew:
        return ns + '-' + ew
    return ns or ew or 'same point'
