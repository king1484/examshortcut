"""Build reasoning/figure-series: notes, patterns and practice questions.

A frame is rendered from a state (a frozenset of components: arrow angle, shaded
quarter, border place, stroke count). Series states are produced by explicit rules,
so the answer frame is the rule applied once more, and every wrong option is a state
that breaks exactly one rule. Distinct states render distinct SVGs (asserted), so
each question has exactly one correct option by construction.
"""
import math
import random
from hashlib import md5

from _lib import load, set_sub, upsert, Q, finish
from figure_series_notes import NOTES, PATTERNS, PYQS

d = load("figure-series")

# ================================================================ frame renderer
HEAD = ('<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 {w} 52" width="{w}" height="52" '
        'fill="none" stroke="currentColor" stroke-width="1.5" stroke-linecap="round" '
        'stroke-linejoin="round">')
FRAME = '<polygon points="3,3 49,3 49,49 3,49"/>'
PLACES = [(9, 9), (26, 9), (43, 9), (43, 26), (43, 43), (26, 43), (9, 43), (9, 26)]
PLACE_NAMES = ["top-left corner", "top-middle", "top-right corner", "right-middle",
               "bottom-right corner", "bottom-middle", "bottom-left corner", "left-middle"]
QK = ["TL", "TR", "BR", "BL"]
QNAMES = {"TL": "top-left", "TR": "top-right", "BR": "bottom-right", "BL": "bottom-left"}
QPTS = {"TL": "3,3 26,3 26,26 3,26", "TR": "26,3 49,3 49,26 26,26",
        "BR": "26,26 49,26 49,49 26,49", "BL": "3,26 26,26 26,49 3,49"}
DIRS = {0: "up", 45: "up-right", 90: "right", 135: "down-right", 180: "down",
        225: "down-left", 270: "left", 315: "up-left"}
KORD = {"quarter": 0, "strokes": 1, "ring": 2, "square": 3, "cross": 4, "plus": 5,
        "dot": 6, "arrow": 7}


def comp_svg(c):
    kind, arg = c
    if kind == "quarter":
        return '<polygon points="%s" fill="currentColor" fill-opacity="0.35"/>' % QPTS[arg]
    if kind == "strokes":
        return "".join('<line x1="%g" y1="21" x2="%g" y2="31"/>' % (x, x)
                       for x in (26 + (i - (arg - 1) / 2) * 5 for i in range(arg)))
    if kind == "dot":
        x, y = PLACES[arg]
        return '<circle cx="%d" cy="%d" r="3.36" fill="currentColor"/>' % (x, y)
    if kind == "ring":
        x, y = PLACES[arg]
        return '<circle cx="%d" cy="%d" r="6"/>' % (x, y)
    if kind == "square":
        x, y = PLACES[arg]
        return '<rect x="%d" y="%d" width="10" height="10"/>' % (x - 5, y - 5)
    if kind in ("cross", "plus"):
        x, y = PLACES[arg]
        if kind == "cross":
            return ('<line x1="%g" y1="%g" x2="%g" y2="%g"/><line x1="%g" y1="%g" x2="%g" y2="%g"/>'
                    % (x - 3.36, y - 3.36, x + 3.36, y + 3.36, x - 3.36, y + 3.36, x + 3.36, y - 3.36))
        return ('<line x1="%g" y1="%d" x2="%g" y2="%d"/><line x1="%d" y1="%g" x2="%d" y2="%g"/>'
                % (x - 4.2, y, x + 4.2, y, x, y - 4.2, x, y + 4.2))
    if kind == "arrow":
        a = math.radians(arg)
        ux, uy = math.sin(a), -math.cos(a)
        px, py = math.cos(a), math.sin(a)
        tx, ty = 26 + 11 * ux, 26 + 11 * uy
        bx, by = 26 - 11 * ux, 26 - 11 * uy
        b1x, b1y = tx - 3.43 * ux + 2.06 * px, ty - 3.43 * uy + 2.06 * py
        b2x, b2y = tx - 3.43 * ux - 2.06 * px, ty - 3.43 * uy - 2.06 * py
        return ('<line x1="%g" y1="%g" x2="%g" y2="%g"/>'
                '<polyline points="%g,%g %g,%g %g,%g"/>'
                % (bx, by, tx, ty, b1x, b1y, tx, ty, b2x, b2y))
    raise ValueError(kind)


def frame_svg(state):
    return FRAME + "".join(comp_svg(c) for c in sorted(state, key=lambda c: (KORD[c[0]], c[1])))


def option_svg(state):
    return (HEAD.format(w=52) + frame_svg(state) + "</svg>")


def series_svg(states):
    n = len(states)
    w = 58 * n + 52
    out = [HEAD.format(w=w)]
    for i, s in enumerate(states):
        out.append('<g transform="translate(%d,0)">%s</g>' % (58 * i, frame_svg(s)))
    x0 = 58 * n + 3
    out.append('<polygon points="%d,3 %d,3 %d,49 %d,49" stroke-dasharray="3 2"/>'
               % (x0, x0 + 46, x0 + 46, x0))
    out.append('<text x="%d" y="32" font-size="18" text-anchor="middle" fill="currentColor" '
               'stroke="none" font-family="sans-serif">?</text>' % (x0 + 23))
    return "".join(out) + "</svg>"


# ================================================================ engine self-checks
assert PLACES[1] == (26, 9) and PLACES[3] == (43, 26) and PLACES[6] == (9, 43)
_up = option_svg(frozenset({("arrow", 0)}))
assert '<line x1="26" y1="37" x2="26" y2="15"/>' in _up
assert '<polyline points="28.06,18.43 26,15 23.94,18.43"/>' in _up
_r90 = option_svg(frozenset({("arrow", 90)}))
assert '<line x1="15" y1="26" x2="37" y2="26"/>' in _r90
assert '<polyline points="33.57,28.06 37,26 33.57,23.94"/>' in _r90
assert 'points="3,3 26,3 26,26 3,26" fill="currentColor" fill-opacity="0.35"' in \
    option_svg(frozenset({("quarter", "TL")}))
_s5 = option_svg(frozenset({("strokes", 5)}))
for x in (16, 21, 26, 31, 36):
    assert '<line x1="%d" y1="21" x2="%d" y2="31"/>' % (x, x) in _s5
_d0 = option_svg(frozenset({("dot", 0)}))
assert '<circle cx="9" cy="9" r="3.36" fill="currentColor"/>' in _d0
assert '<circle cx="43" cy="26" r="3.36" fill="currentColor"/>' in \
    option_svg(frozenset({("dot", 3)}))
_ser4 = series_svg([frozenset({("arrow", 0)})] * 4)
assert 'viewBox="0 0 284 52"' in _ser4 and '<g transform="translate(174,0)">' in _ser4
assert '<polygon points="235,3 281,3 281,49 235,49"' in _ser4 and 'x="258"' in _ser4
_ser3 = series_svg([frozenset({("arrow", 0)})] * 3)
assert 'viewBox="0 0 226 52"' in _ser3 and '<polygon points="177,3 223,3 223,49 177,49"' in _ser3
# notes worked examples
assert [DIRS[(0 + 45 * k) % 360] for k in range(5)] == \
    ["up", "up-right", "right", "down-right", "down"]
assert [(0 + 2 * k) % 8 for k in range(4)] == [0, 2, 4, 6] and (6 + 2) % 8 == 0
_s7 = option_svg(frozenset({("strokes", 7)}))
assert '<line x1="11" y1="21" x2="11" y2="31"/>' in _s7 and \
    '<line x1="41" y1="21" x2="41" y2="31"/>' in _s7
assert [QNAMES[QK[(0 + k) % 4]] for k in range(5)] == \
    ["top-left", "top-right", "bottom-right", "bottom-left", "top-left"]

# ================================================================ rule builders
def seeded(name):
    return random.Random(int(md5(name.encode()).hexdigest(), 16))


def cw(step):
    return "clockwise" if step > 0 else "anticlockwise"


def distinct(cands, ans, want=3):
    out = []
    for c in cands:
        if c != ans and c not in out:
            out.append(c)
        if len(out) == want:
            break
    assert len(out) == want
    return out


def mr_arrow(name, rng):
    step = rng.choice([45, 90, 135]) * rng.choice([1, -1])
    a0 = rng.randrange(8) * 45
    seq = [(a0 + k * step) % 360 for k in range(5)]
    states = [frozenset({("arrow", a)}) for a in seq[:4]]
    ans = frozenset({("arrow", seq[4])})
    names = [DIRS[a] for a in seq]
    sol = (f"The arrow turns **{abs(step)}° {cw(step)}** each step: "
           + " → ".join(names[:4]) + f". Next it points **{names[4]}**.")
    wrongs = distinct([frozenset({("arrow", (seq[4] + o) % 360)})
                       for o in (45, -45, 90, -90, 135)] + [frozenset({("arrow", seq[3])})], ans)
    return states, ans, wrongs, sol


def mr_border(name, rng):
    kind = rng.choice(["dot", "ring", "square"])
    step = rng.choice([1, 2, 3]) * rng.choice([1, -1])
    p0 = rng.randrange(8)
    seq = [(p0 + k * step) % 8 for k in range(5)]
    states = [frozenset({(kind, p)}) for p in seq[:4]]
    ans = frozenset({(kind, seq[4])})
    path = " → ".join(PLACE_NAMES[p] for p in seq[:4])
    sol = (f"The {kind} moves **{abs(step)} place{'s' if abs(step) > 1 else ''} {cw(step)}** "
           f"each step: {path}. Next: place {seq[4]}, the **{PLACE_NAMES[seq[4]]}**.")
    wrongs = distinct([frozenset({(kind, (seq[4] + o) % 8)})
                       for o in (1, -1, 2, -2)] + [frozenset({(kind, seq[3])})], ans)
    return states, ans, wrongs, sol


def mr_quarter(name, rng):
    step = rng.choice([1, -1])
    q0 = rng.randrange(4)
    seq = [(q0 + k * step) % 4 for k in range(5)]
    states = [frozenset({("quarter", QK[q])}) for q in seq[:4]]
    ans = frozenset({("quarter", QK[seq[4]])})
    path = " → ".join(QNAMES[QK[q]] for q in seq[:4])
    sol = (f"The shaded quarter moves **{cw(step)}**: {path}. Next: the "
           f"**{QNAMES[QK[seq[4]]]}** quarter.")
    wrongs = [frozenset({("quarter", QK[q])}) for q in range(4) if q != seq[4]][:3]
    assert len(wrongs) == 3
    return states, ans, wrongs, sol


def mr_combo(name, rng):
    astep = rng.choice([45, 90]) * rng.choice([1, -1])
    a0 = rng.randrange(8) * 45
    qstep = rng.choice([1, -1])
    q0 = rng.randrange(4)
    use_dot = rng.random() < 0.5
    dstep = rng.choice([1, 2]) * rng.choice([1, -1])
    d0 = rng.randrange(8)
    states = []
    for k in range(4):
        comp = {("arrow", (a0 + k * astep) % 360), ("quarter", QK[(q0 + k * qstep) % 4])}
        if use_dot:
            comp.add(("dot", (d0 + k * dstep) % 8))
        states.append(frozenset(comp))
    comp = {("arrow", (a0 + 4 * astep) % 360), ("quarter", QK[(q0 + 4 * qstep) % 4])}
    if use_dot:
        comp.add(("dot", (d0 + 4 * dstep) % 8))
    ans = frozenset(comp)
    qn = [QNAMES[QK[(q0 + k * qstep) % 4]] for k in range(5)]
    an = [DIRS[(a0 + k * astep) % 360] for k in range(5)]
    sol = ("Three rules." if use_dot else "Two rules.")
    sol += (f" The shading moves **one quarter {cw(qstep)}**: " + " → ".join(qn[:4])
            + f" → next **{qn[4]}**.")
    sol += (f" The arrow turns **{abs(astep)}° {cw(astep)}**: " + " → ".join(an[:4])
            + f" → next **{an[4]}**.")
    if use_dot:
        dn = [PLACE_NAMES[(d0 + k * dstep) % 8] for k in range(5)]
        sol += (f" The dot moves **{abs(dstep)} place{'s' if abs(dstep) > 1 else ''} "
                f"{cw(dstep)}**: " + " → ".join(dn[:4]) + f" → next the **{dn[4]}**.")
    sol += (f" The answer follows every rule: the {qn[4]} quarter shaded and the arrow "
            f"pointing {an[4]}" + (f", with the dot at the {dn[4]}" if use_dot else "") + ".")
    awrong = [(ans | {("arrow", (a0 + 4 * astep + o) % 360)}) - {("arrow", (a0 + 4 * astep) % 360)}
              for o in (45, -45, 90)]
    qwrong = [(ans | {("quarter", QK[(q0 + 4 * qstep + s) % 4])}) - {("quarter", QK[(q0 + 4 * qstep) % 4])}
              for s in (1, 2, 3)]
    cands = awrong + qwrong
    if use_dot:
        cands += [(ans | {("dot", (d0 + 4 * dstep + o) % 8)}) - {("dot", (d0 + 4 * dstep) % 8)}
                  for o in (1, -1, 2)]
    wrongs = distinct(cands, ans)
    return states, ans, wrongs, sol


def ac_count(name, rng):
    n0 = rng.choice([1, 2, 3])
    delta = rng.choice([1, 2])
    ngiven = 3 if delta == 2 else rng.choice([3, 4])
    seqn = [n0 + k * delta for k in range(ngiven + 1)]
    assert 1 <= seqn[-1] <= 7
    states = [frozenset({("strokes", n)}) for n in seqn[:ngiven]]
    ans = frozenset({("strokes", seqn[-1])})
    sol = (f"Strokes: {', '.join(str(n) for n in seqn[:ngiven])} — **{delta} more** each step. "
           f"Next: **{seqn[-1]} strokes**.")
    wrongs = distinct([frozenset({("strokes", seqn[-1] + o)})
                       for o in (-1, -2, 1, 2, -3) if 1 <= seqn[-1] + o <= 9]
                      + [frozenset({("strokes", seqn[-2])})], ans)
    return states, ans, wrongs, sol


def ac_dots(name, rng):
    c0 = rng.randrange(4)                       # corner k sits at border place (c0*2 + 2k) % 8
    d = rng.choice([1, -1])
    places = [(2 * c0 + 2 * k * d) % 8 for k in range(4)]
    states = [frozenset({("dot", p) for p in places[:k + 1]}) for k in range(3)]
    ans = frozenset({("dot", p) for p in places})
    cn = [PLACE_NAMES[p] for p in places]
    sol = (f"A dot is **added at the next corner {cw(d)}** each step: {cn[0]}; then {cn[1]}; "
           f"then {cn[2]}. Next: **4 dots, one in every corner** (the new one at the {cn[3]}).")
    wrongs = [
        frozenset({("dot", p) for p in places[:3]}),
        frozenset({("dot", p) for p in places[:3]} | {("dot", (places[3] + d) % 8)}),
        frozenset({("dot", p) for p in places[:3]} | {("dot", (places[1] + d) % 8)}),
    ]
    wrongs = distinct(wrongs, ans)
    assert all(len(w) == 4 for w in wrongs[1:])
    return states, ans, wrongs, sol


def ac_alt(name, rng):
    n0 = rng.choice([1, 2])
    seqn = [n0 + k for k in range(5)]
    assert seqn[-1] <= 7
    pair = rng.choice([(0, 180), (180, 0)])     # arrow alternates up / down
    seqa = [pair[k % 2] for k in range(5)]
    states = [frozenset({("strokes", seqn[k]), ("arrow", seqa[k])}) for k in range(4)]
    ans = frozenset({("strokes", seqn[4]), ("arrow", seqa[4])})
    an = [DIRS[a] for a in seqa]
    sol = (f"Two rules. The strokes increase by one: {', '.join(str(n) for n in seqn[:4])} → "
           f"**{seqn[4]}**. The arrow alternates {an[0]}, {an[1]} → next **{an[4]}**. Only the "
           f"figure with {seqn[4]} strokes and the arrow pointing **{an[4]}** fits both.")
    wrongs = distinct([
        frozenset({("strokes", seqn[4]), ("arrow", seqa[3])}),
        frozenset({("strokes", seqn[4] - 1), ("arrow", seqa[4])}),
        frozenset({("strokes", seqn[4] - 1), ("arrow", seqa[3])}),
    ], ans)
    return states, ans, wrongs, sol


def ac_shrink(name, rng):
    n0 = rng.choice([5, 6, 7])
    seqn = [n0 - k for k in range(5)]
    assert seqn[-1] >= 1
    kind = rng.choice(["dot", "ring", "square"])
    step = rng.choice([1, 2]) * rng.choice([1, -1])
    p0 = rng.randrange(8)
    seqp = [(p0 + k * step) % 8 for k in range(5)]
    states = [frozenset({("strokes", seqn[k]), (kind, seqp[k])}) for k in range(4)]
    ans = frozenset({("strokes", seqn[4]), (kind, seqp[4])})
    dn = [PLACE_NAMES[p] for p in seqp]
    sol = (f"Two rules. The strokes decrease by one: {', '.join(str(n) for n in seqn[:4])} → "
           f"**{seqn[4]}**. The {kind} moves **{abs(step)} place{'s' if abs(step) > 1 else ''} "
           f"{cw(step)}**: " + " → ".join(dn[:4]) + f" → next the **{dn[4]}**. The answer has "
           f"{seqn[4]} stroke{'s' if seqn[4] > 1 else ''} and the {kind} at the {dn[4]}.")
    wrongs = distinct([
        frozenset({("strokes", seqn[4] + 1), (kind, seqp[4])}),
        frozenset({("strokes", seqn[4]), (kind, (seqp[4] + 1) % 8)}),
        frozenset({("strokes", seqn[4] + 1), (kind, (seqp[4] - 1) % 8)}),
    ], ans)
    return states, ans, wrongs, sol


def build(name, sub, pat, diff, t, rule):
    rng = seeded(name)
    states, ans, wrongs, sol = rule(name, rng)
    av = frame_svg(ans)
    wv = [frame_svg(w) for w in wrongs]
    assert len({av} | set(wv)) == 4
    return Q(name, "Select the figure that will come next in the given series.",
             option_svg(ans), [option_svg(w) for w in wrongs], sol,
             diff=diff, sub=sub, pat=pat, t=t, figure=series_svg(states))


# ================================================================ questions
QS = [
    build("movement-rotation-p01", "movement-rotation", "mr-p1", "medium", 40, mr_arrow),
    build("movement-rotation-p02", "movement-rotation", "mr-p1", "easy", 30, mr_arrow),
    build("movement-rotation-p03", "movement-rotation", "mr-p2", "easy", 35, mr_border),
    build("movement-rotation-p04", "movement-rotation", "mr-p2", "medium", 40, mr_border),
    build("movement-rotation-p05", "movement-rotation", "mr-p3", "easy", 30, mr_quarter),
    build("movement-rotation-p06", "movement-rotation", "mr-p3", "medium", 35, mr_quarter),
    build("movement-rotation-p07", "movement-rotation", "mr-p4", "medium", 50, mr_combo),
    build("movement-rotation-p08", "movement-rotation", "mr-p4", "hard", 60, mr_combo),
    build("addition-change-p01", "addition-change", "ac-p1", "easy", 30, ac_count),
    build("addition-change-p02", "addition-change", "ac-p1", "medium", 35, ac_count),
    build("addition-change-p03", "addition-change", "ac-p2", "easy", 30, ac_dots),
    build("addition-change-p04", "addition-change", "ac-p2", "medium", 35, ac_dots),
    build("addition-change-p05", "addition-change", "ac-p3", "medium", 45, ac_alt),
    build("addition-change-p06", "addition-change", "ac-p3", "hard", 55, ac_alt),
    build("addition-change-p07", "addition-change", "ac-p4", "medium", 50, ac_shrink),
    build("addition-change-p08", "addition-change", "ac-p4", "hard", 55, ac_shrink),
]

upsert(d["practice"], QS)
set_sub(d, "movement-rotation", notes=NOTES["movement-rotation"], patterns=PATTERNS["movement-rotation"])
set_sub(d, "addition-change", notes=NOTES["addition-change"], patterns=PATTERNS["addition-change"])
d["pyqPatterns"] = PYQS
finish("figure-series", d)
