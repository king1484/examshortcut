"""Lattice-figure engine for embedded-figures.

A figure is a set of unit edges on a square lattice (horizontal, vertical and the two
diagonals). Embedding is a subset test over translated edge sets - rotation is NOT
allowed, exactly like the exam wording. Every accept/reject below is that mechanical
test, never an eyeball judgement.
"""
import random

STEP = 12          # px per lattice unit, matches the topic's existing SVGs
MARGIN = 5


def norm(edges):
    """Normalize an edge set so its smallest x and y are 0."""
    xs = [p[0] for e in edges for p in e]
    ys = [p[1] for e in edges for p in e]
    mx, my = min(xs), min(ys)
    return frozenset(frozenset(((x - mx, y - my), (z - mx, w - my)))
                     for e in edges for x, y in [tuple(e)[0:1] for _ in [0]] for z, w in [tuple(e)[1]] for x, y in [(x, y)])


def norm2(edges):
    return frozenset(frozenset(((x - mx, y - my), (z - mx, w - my)))
                     for e in edges
                     for (x, y), (z, w) in [sorted(e)]
                     for mx, my in [(min(p[0] for e2 in edges for p in e2),
                                     min(p[1] for e2 in edges for p in e2))])


def bbox(edges):
    xs = [p[0] for e in edges for p in e]
    ys = [p[1] for e in edges for p in e]
    return max(xs), max(ys)


def transform(edges, kind):
    """mirrorV (left-right flip), mirrorH (top-bottom flip), rot90, rot180."""
    w, h = bbox(edges)

    def tp(p):
        x, y = p
        if kind == "id":
            return (x, y)
        if kind == "mirrorV":
            return (w - x, y)
        if kind == "mirrorH":
            return (x, h - y)
        if kind == "rot90":
            return (h - y, x)
        if kind == "rot180":
            return (w - x, h - y)
        raise ValueError(kind)

    return frozenset(frozenset((tp(a), tp(b))) for a, b in edges)


def lattice_edges(cx, cy):
    """All unit edges (H, V and both diagonals) of a cx x cy cell lattice."""
    pool = set()
    for x in range(cx):
        for y in range(cy + 1):
            pool.add(frozenset(((x, y), (x + 1, y))))
    for x in range(cx + 1):
        for y in range(cy):
            pool.add(frozenset(((x, y), (x, y + 1))))
    for x in range(cx):
        for y in range(cy):
            pool.add(frozenset(((x, y), (x + 1, y + 1))))
            pool.add(frozenset(((x + 1, y), (x, y + 1))))
    return pool


def translate(edges, dx, dy):
    return frozenset(frozenset(((x + dx, y + dy), (z + dx, w + dy)))
                     for e in edges for (x, y), (z, w) in [tuple(e)])


def embeds(part, big):
    """(found, offset): does `part` appear in `big` under translation only?"""
    pw, ph = bbox(part)
    bw, bh = bbox(big)
    for dx in range(bw - pw + 1):
        for dy in range(bh - ph + 1):
            t = translate(part, dx, dy)
            if t <= big:
                return True, (dx, dy)
    return False, None


def random_part(rng, n_edges, cx=2, cy=2):
    """A connected-ish part of n_edges unit edges, grown from one starting edge."""
    pool = sorted(lattice_edges(cx, cy))
    start = rng.choice(pool)
    fig = {start}
    nodes = set(start)
    while len(fig) < n_edges:
        cand = [e for e in pool if e not in fig and nodes & set(e)]
        if not cand:
            break
        e = rng.choice(cand)
        fig.add(e)
        nodes |= set(e)
    return frozenset(fig)


def near_miss(rng, part, pool):
    """Variants of `part` with one stroke missing, moved or re-angled."""
    out = []
    edges = sorted(part)
    rng.shuffle(edges)
    extra = sorted(pool - part)
    rng.shuffle(extra)
    for e in edges:                                   # missing stroke
        out.append((frozenset(f for f in part if f != e), "missing"))
        break
    for e in edges:                                   # replaced stroke
        for e2 in extra:
            q = frozenset(f for f in part if f != e) | {e2}
            if len(q) == len(part) and q != part:
                out.append((q, "replaced"))
                break
        break
    for e in sorted(part):                            # re-angled diagonal
        (x, y), (z, w) = sorted(e)
        if abs(x - z) == 1 and abs(y - w) == 1:
            e2 = frozenset(((x, w), (z, y)))
            if e2 not in part:
                out.append((frozenset(f for f in part if f != e) | {e2}, "reangled"))
                break
    return out


def region_name(ox, oy, pw, ph, cx, cy):
    def one(o, size, span, low, high, mid):
        return low if o == 0 else (high if o + size >= span else mid)
    hs = "left" if ox == 0 else ("right" if ox + pw >= cx else "centre")
    vs = "upper" if oy == 0 else ("lower" if oy + ph >= cy else "middle")
    if hs == "centre" and vs == "middle":
        return "the middle"
    return f"{vs}-{hs}"


def stroke_desc(edges):
    nh = sum(1 for e in edges for (x, y), (z, w) in [sorted(e)] if y == w)
    nv = sum(1 for e in edges for (x, y), (z, w) in [sorted(e)] if x == z)
    nd = len(edges) - nh - nv
    bits = []
    if nh:
        bits.append(f"{nh} horizontal stroke" + ("s" if nh > 1 else ""))
    if nv:
        bits.append(f"{nv} vertical stroke" + ("s" if nv > 1 else ""))
    if nd:
        bits.append(f"{nd} slanting stroke" + ("s" if nd > 1 else ""))
    return " and ".join(bits)


def fig_svg(edges, cellsx, cellsy=None):
    cellsy = cellsy if cellsy is not None else cellsx
    w = STEP * cellsx + 2 * MARGIN
    h = STEP * cellsy + 2 * MARGIN
    out = ['<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 %d %d" width="%d" '
           'height="%d" fill="none" stroke="currentColor" stroke-width="1.4" '
           'stroke-linecap="round" stroke-linejoin="round">' % (w, h, w, h)]
    for e in sorted(edges, key=sorted):
        (x, y), (z, w2) = sorted(e)
        out.append('<line x1="%d" y1="%d" x2="%d" y2="%d"/>'
                   % (MARGIN + STEP * x, MARGIN + STEP * y,
                      MARGIN + STEP * z, MARGIN + STEP * w2))
    out.append("</svg>")
    return "".join(out)
