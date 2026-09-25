"""Phase-2 deep content for reasoning/cube-dice. Idempotent: `py -3 cube-dice.py`.

Every answer comes from cube_dice_engine: dice views are enumerated over the 24 cube
rotations, a puzzle answer is accepted only when an exhaustive search over all 720
face assignments leaves exactly one candidate for the opposite face, nets are folded
by exact quarter-turns (screen coordinates, so handedness matches the drawing), and
painted-cube counts are brute-forced cube by cube against the closed forms.
"""
import hashlib
import itertools
import os
import random
import sys
from itertools import permutations

sys.path.insert(0, os.path.dirname(__file__))
from _lib import Q, finish, load, set_sub, upsert  # noqa
from cube_dice_engine import (  # noqa
    AXES, FACE_ORDER, SRC, adjacent_pairs, can_view, die_svg, fold,
    forced_opposite, impossible_triples, make_die, neg, net_opposites, net_svg,
    opp_map, paint_counts, view_i, views_of, NAME)
from cube_dice_notes import NOTES, PATTERNS, PYQS  # noqa

T = "cube-dice"
d = load(T)
for sid, notes in NOTES.items():
    set_sub(d, sid, notes=notes, patterns=PATTERNS[sid])
d["pyqPatterns"] = PYQS

NQ = []
_ctr = {}


def nid(sub):
    _ctr[sub] = _ctr.get(sub, 0) + 1
    return f"{sub}-p{_ctr[sub]:02d}"


def mk_rng(name):
    return random.Random(int(hashlib.md5(name.encode()).hexdigest(), 16))


# ================================================================== net layouts
NETS = {
    "T":      [(1, 0), (0, 1), (1, 1), (2, 1), (3, 1), (1, 2)],
    "row4":   [(0, 1), (1, 1), (2, 1), (3, 1), (1, 0), (2, 2)],
    "endtabs": [(0, 1), (1, 1), (2, 1), (3, 1), (0, 0), (3, 2)],
    "stair":  [(0, 0), (1, 0), (1, 1), (2, 1), (2, 2), (3, 2)],
    "zig":    [(0, 0), (1, 0), (1, 1), (2, 1), (3, 1), (3, 2)],
    "col4":   [(1, 0), (1, 1), (1, 2), (1, 3), (0, 1), (2, 2)],
    "cross":  [(1, 0), (0, 1), (1, 1), (2, 1), (1, 2), (1, 3)],
    "lshape": [(0, 0), (1, 0), (1, 1), (1, 2), (1, 3), (2, 3)],
    "ishape": [(1, 0), (1, 1), (1, 2), (1, 3), (0, 1), (2, 1)],
}

# ================================================================== facts used in notes/patterns
# painting: brute force vs closed forms
for _n in range(2, 9):
    _c = paint_counts(_n)
    assert _c[3] == 8 and _c[2] == 12 * (_n - 2) and _c[1] == 6 * (_n - 2) ** 2 \
        and _c[0] == (_n - 2) ** 3, _n
    assert sum(_c.values()) == _n ** 3
for _a, _b, _c3 in ((5, 4, 3), (6, 4, 3), (6, 5, 4), (7, 5, 2)):
    _p = paint_counts(_a, _b, _c3)
    assert _p[3] == 8
    assert _p[2] == 4 * ((_a - 2) + (_b - 2) + (_c3 - 2))
    assert _p[1] == 2 * ((_a - 2) * (_b - 2) + (_b - 2) * (_c3 - 2) + (_c3 - 2) * (_a - 2))
    assert _p[0] == (_a - 2) * (_b - 2) * (_c3 - 2)
assert [paint_counts(3)[k] for k in (3, 2, 1, 0)] == [8, 12, 6, 1]
assert [paint_counts(4)[k] for k in (3, 2, 1, 0)] == [8, 24, 24, 8]
assert paint_counts(5, 4, 3)[2] == 24 and paint_counts(5, 4, 3)[0] == 6
assert paint_counts(6, 5, 4)[1] == 52 and paint_counts(6, 4, 3)[0] == 8

# nets fold; the skip-one / Z / leftover facts quoted in solutions
FOLD = {}
for _name, _layout in NETS.items():
    _cells = {p: l for p, l in zip(_layout, "ABCDEF")}
    _cube = fold(_cells)
    FOLD[_name] = (_cells, _cube)
    assert len(net_opposites(_cube)) == 3, _name
_op = opp_map(FOLD["row4"][1])
assert _op["A"] == "C" and _op["B"] == "D" and _op["E"] == "F"          # row skip-one
_op = opp_map(FOLD["col4"][1])
assert _op["A"] == "C" and _op["B"] == "D" and _op["E"] == "F"          # column skip-one
_op = opp_map(FOLD["stair"][1])
assert _op["A"] == "D"                                                  # Z ends (labels ABCDEF)
_op = opp_map(FOLD["zig"][1])
assert _op["A"] == "D"                                                  # Z ends
_op = opp_map(FOLD["T"][1])
assert _op["B"] == "D" and _op["A"] == "F" and _op["C"] == "E"
_op = opp_map(FOLD["cross"][1])
assert _op["A"] == "E" and _op["B"] == "D" and _op["C"] == "F"
# notes worked example: row L,M,N; K above M; O below M; J below O
_wex = {(0, 1): "L", (1, 1): "M", (2, 1): "N", (1, 0): "K", (1, 2): "O", (1, 3): "J"}
_wc = fold(_wex)
assert net_opposites(_wc) == [("J", "M"), ("K", "O"), ("L", "N")]
assert can_view(_wc, ("M", "K", "N")) and not can_view(_wc, ("M", "K", "L"))
# cn-p4 pattern example: column K,M,O,J with L left of M and N right of M
_ish = {(1, 0): "K", (1, 1): "M", (1, 2): "O", (1, 3): "J", (0, 1): "L", (2, 1): "N"}
_ic = fold(_ish)
assert net_opposites(_ic) == [("J", "M"), ("K", "O"), ("L", "N")]
assert can_view(_ic, ("M", "K", "N")) and not can_view(_ic, ("M", "K", "L"))

# dice notes worked example: views (P,Q,R),(R,S,P),(Q,T,R)
_lab = "PQRSTU"
_views = [("P", "Q", "R"), ("R", "S", "P"), ("Q", "T", "R")]
for _x, _y in (("P", "T"), ("Q", "S"), ("R", "U")):
    assert forced_opposite(_lab, _views, _x) == {_y}


def check_full_map(labels, views):
    """Opposite map forced by the views, or None if two assignments disagree."""
    o = {}
    found = False
    for perm in permutations(labels):
        A = dict(zip(FACE_ORDER, perm))
        ok = True
        for v in views:
            if not any(tuple(A[c] for c in s) == v for s in SRC):
                ok = False
                break
        if not ok:
            continue
        found = True
        for f in FACE_ORDER:
            lab = A[f]
            p = A[NAME[neg(AXES[f])]]
            if lab in o and o[lab] != p:
                return None
            o[lab] = p
    return o if found else None


# ================================================================== dice-positions
def dp1(name, labels, nviews, diff="medium", t=45):
    rng = mk_rng(name)
    die = make_die(rng, labels)
    target = labels[0]
    idx = list(range(24))
    rng.shuffle(idx)
    for comb in itertools.combinations(idx, nviews):
        vs = [view_i(die, i) for i in comb]
        others = set()
        ok = True
        for v in vs:
            o = [x for x in v if x != target]
            if len(o) != 2:
                ok = False
                break
            others.update(o)
        if not ok or len(others) != 4:
            continue
        ans = next(x for x in labels if x != target and x not in others)
        if forced_opposite(labels, vs, target) != {ans}:
            continue
        wrong = [x for x in labels if x not in (target, ans)]
        rng.shuffle(wrong)
        groups = ", then with ".join(" and ".join(x for x in v if x != target) for v in vs)
        sol = (f"Across the views, **{target}** is seen with {groups} — four different "
               f"faces, and every one of them touches it. The only face never seen with "
               f"**{target}** is **{ans}**, so it must be the opposite face.")
        q = (f"{'Three' if nviews == 3 else 'Two'} different positions of the same dice "
             f"are shown. Which letter is on the face opposite to **{target}**? "
             f"(Ignore the orientation of the letters/numbers.)")
        NQ.append(Q(nid("dice-positions"), q, ans, wrong[:3], sol,
                    shortcut="Strike out every face seen with the asked face; the last one left is opposite.",
                    diff=diff, sub="dice-positions", pat="dp-p1", t=t, figure=die_svg(vs)))
        return
    raise AssertionError(name)


def dp2(name, labels, diff="medium", t=40):
    rng = mk_rng(name)
    die = make_die(rng, labels)
    idx = list(range(24))
    rng.shuffle(idx)
    for i in idx:
        v1 = view_i(die, i)
        for j in idx:
            if j == i:
                continue
            v2 = view_i(die, j)
            sh = set(v1) & set(v2)
            if len(sh) != 2:
                continue
            l1 = next(x for x in v1 if x not in sh)
            l2 = next(x for x in v2 if x not in sh)
            if forced_opposite(labels, [v1, v2], l1) != {l2}:
                continue
            c1, c2 = sorted(sh)
            wrong = [x for x in labels if x not in (l1, l2)]
            rng.shuffle(wrong)
            sol = (f"The two views share **{c1}** and **{c2}** — two common faces, so each "
                   f"of them touches the other faces shown. The face left over in the first "
                   f"view (**{l1}**) and the face left over in the second (**{l2}**) must "
                   f"therefore be opposite each other.")
            q = (f"Two different positions of the same dice are shown. Which letter is on "
                 f"the face opposite to **{l1}**? (Ignore the orientation of the letters/numbers.)")
            NQ.append(Q(nid("dice-positions"), q, l2, wrong[:3], sol,
                        shortcut="Two common faces in two views: the leftovers are opposite.",
                        diff=diff, sub="dice-positions", pat="dp-p2", t=t, figure=die_svg([v1, v2])))
            return
    raise AssertionError(name)


def dp3(name, labels, diff="medium", t=45):
    rng = mk_rng(name)
    die = make_die(rng, labels)
    SLOT = {0: "front", 1: "top", 2: "right"}
    idx = list(range(24))
    rng.shuffle(idx)
    for i in idx:
        v1 = view_i(die, i)
        for j in idx:
            if j == i:
                continue
            v2 = view_i(die, j)
            sh = [x for x in v1 if x in v2]
            if len(sh) != 1:
                continue
            c = sh[0]
            if v1.index(c) != v2.index(c):
                continue
            s = v1.index(c)
            for t2 in range(3):
                if t2 == s:
                    continue
                x, y = v1[t2], v2[t2]
                if forced_opposite(labels, [v1, v2], x) != {y}:
                    continue
                wrong = [w for w in labels if w not in (x, y)]
                rng.shuffle(wrong)
                sol = (f"**{c}** is common to both views and sits in the **same position** "
                       f"(the {SLOT[s]} face in both). So faces in matching positions are "
                       f"opposite: the {SLOT[t2]} face of the first view (**{x}**) is "
                       f"opposite the {SLOT[t2]} face of the second (**{y}**).")
                q = (f"Two different positions of the same dice are shown. Which letter is "
                     f"on the face opposite to **{x}**? (Ignore the orientation of the "
                     f"letters/numbers.)")
                NQ.append(Q(nid("dice-positions"), q, y, wrong[:3], sol,
                            shortcut="Common face in the same place: match the other positions.",
                            diff=diff, sub="dice-positions", pat="dp-p3", t=t,
                            figure=die_svg([v1, v2])))
                return
    raise AssertionError(name)


def dp5(name, labels, diff="medium", t=60):
    rng = mk_rng(name)
    die = make_die(rng, labels)
    idx = list(range(24))
    rng.shuffle(idx)
    for comb in itertools.combinations(idx, 3):
        vs = [view_i(die, i) for i in comb]
        if len(set().union(*map(set, vs))) != 6:
            continue
        o = check_full_map(labels, vs)
        if not o:
            continue
        pairs = sorted({tuple(sorted(p)) for p in o.items()})
        assert len(pairs) == 3
        p0 = pairs[0]
        ans = f"{p0[0]} and {p0[1]}"
        wrong = adjacent_pairs(die, rng, 3)
        assert ans not in wrong
        ptxt = ", ".join(f"{a}–{b}" for a, b in pairs)
        sol = (f"Match views that share two faces: each such match makes the two "
               f"leftover faces opposite. Working through the three views, the "
               f"opposite pairs of this die are {ptxt}.")
        q = ("Three different positions of the same dice are shown. Which of these "
             "pairs shows two **opposite** faces? (Ignore the orientation of the "
             "letters/numbers.)")
        NQ.append(Q(nid("dice-positions"), q, ans, wrong, sol,
                    shortcut="Pair up the views that share two faces; the leftovers pair last.",
                    diff=diff, sub="dice-positions", pat="dp-p5", t=t,
                    figure=die_svg(vs)))
        return
    raise AssertionError(name)


def dp6(name, labels, diff="medium", t=45):
    rng = mk_rng(name)
    die = make_die(rng, labels)
    opp = opp_map(die)
    a, b, c = labels[0], labels[1], labels[2]
    pa, pb, pc = opp[a], opp[b], opp[c]
    vs = views_of(die)
    ans_v = sorted(vs)[rng.randrange(24)]
    assert can_view(die, ans_v)
    wrong_v = []
    for x, px in ((a, pa), (b, pb), (c, pc)):
        for y in sorted(die.values()):
            if y not in (x, px) and (x, px, y) not in wrong_v:
                wrong_v.append((x, px, y))
                break
    for w in wrong_v:
        assert w not in vs
        assert len(set(w)) == 3
    assert len(set(wrong_v)) == 3 and ans_v not in wrong_v
    sol = (f"A real view can never show two opposite faces together. Three options show a "
           f"pair from ({a}–{pa}, {b}–{pb}, {c}–{pc}), so they are impossible. The remaining "
           f"view shows one face from each opposite pair, and such a view can always be "
           f"turned up on the die.")
    q = (f"In a die, the face **{a}** is opposite **{pa}**, **{b}** is opposite **{pb}** "
         f"and **{c}** is opposite **{pc}**. Which of the following views can be formed? "
         f"(Ignore the orientation of the letters/numbers.)")
    NQ.append(Q(nid("dice-positions"), q, die_svg([ans_v]), [die_svg([w]) for w in wrong_v],
                sol, shortcut="Reject every view that shows an opposite pair.",
                diff=diff, sub="dice-positions", pat="dp-p6", t=t))


# dice-positions questions
dp1("dp1a", "ABCDEF", 3, "medium", 45)
dp1("dp1b", "123456", 2, "easy", 35)
dp2("dp2a", "GHIJKL")
dp2("dp2b", "MNOPQR")
dp3("dp3a", "STUVWX")
dp3("dp3b", "PQRSTU")

# dp-p4: standard die (text questions)
_a, _b, _c = 3, 5, 6
_s = _a + _b + _c
assert 21 - _s == 7
NQ.append(Q(nid("dice-positions"),
            f"An ordinary die, whose opposite faces always add up to 7, shows **{_a}** on "
            f"top, **{_b}** in front and **{_c}** on the right. What is the sum of the "
            f"numbers on the bottom, back and left faces?",
            21 - _s, [21 - _a - _b, 21 - _a - _c, 21 - _b - _c],
            f"Opposite faces add to 7: bottom = 7 − {_a} = {7 - _a}, back = 7 − {_b} = "
            f"{7 - _b}, left = 7 − {_c} = {7 - _c}. Sum = {7 - _a} + {7 - _b} + {7 - _c} "
            f"= **{21 - _s}**. (Check: 3 × 7 − {_s} = {21 - _s}.)",
            shortcut="Hidden sum = 21 − (shown sum).",
            diff="easy", sub="dice-positions", pat="dp-p4", t=30, check=21 - _s))
NQ.append(Q(nid("dice-positions"),
            "An ordinary die, whose opposite faces always add up to 7, shows **2** on its "
            "top face. Which of the numbers 1 to 6 can **never** lie on a face adjacent "
            "to the 2?",
            5, [3, 4, 6],
            "The face opposite 2 is 7 − 2 = **5**. Opposite faces never touch, so 5 can "
            "never be adjacent to 2; every other number (1, 3, 4, 6) shares an edge with "
            "the 2 in some position.",
            shortcut="Never-adjacent = the opposite face = 7 − the number.",
            diff="easy", sub="dice-positions", pat="dp-p4", t=30, check=5))

dp5("dp5a", "ABCDEF", "hard", 60)
dp5("dp5b", "123456", "hard", 60)
dp6("dp6a", "GHIJKL")
dp6("dp6b", "MNOPQR")


# ================================================================== cube-nets
def cn_cells(layout_key, labels):
    return {p: l for p, l in zip(NETS[layout_key], labels)}


def cn1(name, layout_key, labels, target, line, diff="easy", t=35):
    rng = mk_rng(name)
    cells = cn_cells(layout_key, labels)
    cube = fold(cells)
    op = opp_map(cube)
    ans = op[target]
    wrong = [x for x in labels if x not in (target, ans)]
    rng.shuffle(wrong)
    allp = ", ".join(f"{a}–{b}" for a, b in net_opposites(cube))
    sol = (f"{line} In a straight line of the net, faces with exactly one square between "
           f"them are opposite. The three opposite pairs are {allp}. Answer **{ans}**.")
    q = (f"The given sheet is folded to form a cube. Which letter will be on the face "
         f"opposite to **{target}**? (Ignore the orientation of the letters/numbers.)")
    NQ.append(Q(nid("cube-nets"), q, ans, wrong[:3], sol,
                shortcut="In a row or column, skip one square.",
                diff=diff, sub="cube-nets", pat="cn-p1", t=t, figure=net_svg(cells)))


def cn2(name, layout_key, labels, target, zpath, diff="medium", t=40):
    rng = mk_rng(name)
    cells = cn_cells(layout_key, labels)
    cube = fold(cells)
    op = opp_map(cube)
    ans = op[target]
    wrong = [x for x in labels if x not in (target, ans)]
    rng.shuffle(wrong)
    allp = ", ".join(f"{a}–{b}" for a, b in net_opposites(cube))
    sol = (f"The squares {zpath} form a Z (or S) shape of four squares, and the two end "
           f"squares of a Z are opposite. The full pairs are {allp}. Answer **{ans}**.")
    q = (f"The given sheet is folded to form a cube. Which letter will be on the face "
         f"opposite to **{target}**? (Ignore the orientation of the letters/numbers.)")
    NQ.append(Q(nid("cube-nets"), q, ans, wrong[:3], sol,
                shortcut="Ends of a Z are opposite.",
                diff=diff, sub="cube-nets", pat="cn-p2", t=t, figure=net_svg(cells)))


def cn3(name, layout_key, labels, ans_pair, diff="medium", t=45):
    rng = mk_rng(name)
    cells = cn_cells(layout_key, labels)
    cube = fold(cells)
    op = opp_map(cube)
    a, b = ans_pair
    assert op[a] == b
    ans = f"{a} and {b}"
    wrong = adjacent_pairs(cube, rng, 3)
    assert ans not in wrong
    allp = ", ".join(f"{x}–{y}" for x, y in net_opposites(cube))
    sol = (f"Pair the straight lines first (skip one square), then the Z shapes; the two "
           f"squares still unpaired form the last pair. The three opposite pairs are "
           f"{allp}. Answer **{ans}**.")
    q = (f"The given sheet is folded to form a cube. Which pair of letters will be on "
         f"**opposite** faces? (Ignore the orientation of the letters/numbers.)")
    NQ.append(Q(nid("cube-nets"), q, ans, wrong, sol,
                shortcut="Pair the rows and Zs; the leftovers pair up.",
                diff=diff, sub="cube-nets", pat="cn-p3", t=t, figure=net_svg(cells)))


def cn4(name, layout_key, labels, diff="medium", t=60):
    rng = mk_rng(name)
    cells = cn_cells(layout_key, labels)
    cube = fold(cells)
    vs = views_of(cube)
    svs = sorted(vs)
    ans = svs[rng.randrange(len(svs))]
    wrong = []
    for w in impossible_triples(cube, rng):
        if w != ans and w not in wrong:
            wrong.append(w)
        if len(wrong) == 3:
            break
    assert len(wrong) == 3
    assert sum(1 for t3 in [ans] + wrong if t3 in vs) == 1, name
    allp = ", ".join(f"{x}–{y}" for x, y in net_opposites(cube))
    sol = (f"The opposite pairs of this net are {allp}, so any cube showing one of those "
           f"pairs together is impossible. Among the remaining options, only one has the "
           f"three faces in an order that folding can give; the others run the wrong way "
           f"round the corner. The cube shown in the answer can be formed.")
    q = ("The given sheet is folded to form a cube. Which of the following cubes can be "
         "formed? (Ignore the orientation of the letters/numbers.)")
    NQ.append(Q(nid("cube-nets"), q, die_svg([ans]), [die_svg([w]) for w in wrong], sol,
                shortcut="Reject opposite pairs first, then check the corner order.",
                diff=diff, sub="cube-nets", pat="cn-p4", t=t, figure=net_svg(cells)))


def cn5(name, layout_key, labels, diff="hard", t=60):
    rng = mk_rng(name)
    cells = cn_cells(layout_key, labels)
    cube = fold(cells)
    vs = sorted(views_of(cube))
    imps = impossible_triples(cube, rng)
    ans = imps[0]
    pool = vs[:]
    rng.shuffle(pool)
    wrong = []
    for v in pool:
        if v not in wrong:
            wrong.append(v)
        if len(wrong) == 3:
            break
    assert sum(1 for t3 in [ans] + wrong if tuple(t3) in set(vs)) == 3, name
    allp = ", ".join(f"{x}–{y}" for x, y in net_opposites(cube))
    sol = (f"The opposite pairs are {allp}. Three of the options only use faces that fold "
           f"next to each other in an order the cube allows; the remaining option cannot "
           f"be turned to match — it either shows an opposite pair or runs the faces the "
           f"wrong way round the corner. That one cannot be formed.")
    q = ("The given sheet is folded to form a cube. Which of the following cubes "
         "**cannot** be formed? (Ignore the orientation of the letters/numbers.)")
    NQ.append(Q(nid("cube-nets"), q, die_svg([ans]), [die_svg([w]) for w in wrong], sol,
                shortcut="Three cubes fold; find the one with a pair or a mirrored corner.",
                diff=diff, sub="cube-nets", pat="cn-p5", t=t, figure=net_svg(cells)))


# cube-nets questions
cn1("cn1a", "row4", "ABCDEF", "B", "The net has the row A, B, C, D.")
cn1("cn1b", "col4", "GHIJKL", "K", "The net has the column K, L, M, N.")
cn2("cn2a", "stair", "MNOPQR", "M", "M, N, O, P")
cn2("cn2b", "zig", "STUVWX", "S", "S, T, U, V")
cn3("cn3a", "T", "ABCDEF", ("B", "D"))
cn3("cn3b", "cross", "MNOPQR", ("M", "Q"))
cn4("cn4a", "lshape", "PQRSTU")
cn4("cn4b", "endtabs", "GHIJKL", "hard", 70)
cn4("cn4c", "ishape", "123456", "hard", 70)
cn5("cn5a", "cross", "ABCDEF")
cn5("cn5b", "row4", "QRSTUV")
cn5("cn5c", "ishape", "KLMNOP")


# ================================================================== painted-cubes
def pc(name, n, want, wrong, stmt, why, diff="medium", t=35, cuboid=None):
    cnt = paint_counts(*(cuboid if cuboid else (n,)))
    ans = cnt[want]
    NQ.append(Q(nid("painted-cubes"), stmt, ans, wrong, why,
                shortcut=None, diff=diff, sub="painted-cubes",
                pat=f"pc-p{want + 1}" if cuboid is None else "pc-p6",
                t=t, check=ans))
    assert ans not in wrong and len(set(wrong)) == 3, name


# pc-p1: three faces painted (corners)
pc("pc1a", 6, 3, [24, 12, 48],
   "A cube of side 6 cm is painted on all its faces and then cut into small cubes of "
   "side 1 cm. How many small cubes have **three** faces painted?",
   "Only the corner cubes of the big cube touch three painted faces, and a cube has "
   "8 corners whatever its side. Answer **8**.", diff="easy", t=30)
pc("pc1b", 7, 3, [12, 24, 21],
   "A cube of side 7 units is painted on all faces and cut into 343 unit cubes. How "
   "many unit cubes have **exactly three** painted faces?",
   "Three painted faces happen only at the corners of the big cube: **8** of them, "
   "independent of the side length.", diff="easy", t=30)

# pc-p2: two faces painted (edges)
pc("pc2a", 5, 2, [60, 44, 25],
   "A cube of side 5 cm is painted on all its faces and then cut into 1 cm cubes. How "
   "many small cubes have **exactly two** faces painted?",
   "Exactly-two cubes sit on the 12 edges, excluding the 2 corner cubes of each edge: "
   "12 × (5 − 2) = 12 × 3 = **36**.", diff="easy", t=30)
pc("pc2b", 6, 2, [72, 56, 36],
   "A painted cube of side 6 is cut into unit cubes. How many unit cubes have exactly "
   "two painted faces?",
   "Each of the 12 edges keeps 6 − 2 = 4 non-corner cubes: 12 × 4 = **48**.", t=35)

# pc-p3: one face painted (face centres)
pc("pc3a", 4, 1, [96, 54, 8],
   "A cube of side 4 cm is painted on all faces and cut into 1 cm cubes. How many "
   "small cubes have **exactly one** face painted?",
   "On each face the cubes away from the edge form a (4 − 2) × (4 − 2) = 2 × 2 block. "
   "6 faces × 4 = **24**.", diff="easy", t=30)
pc("pc3b", 6, 1, [216, 150, 64],
   "A painted cube of side 6 is cut into unit cubes. How many unit cubes have exactly "
   "one painted face?",
   "Each face keeps an (6 − 2)² = 16 block of one-face cubes: 6 × 16 = **96**.", t=35)

# pc-p4: no face painted (core)
pc("pc4a", 5, 0, [98, 125, 54],
   "A cube of side 5 cm is painted on all its faces and then cut into 1 cm cubes. How "
   "many small cubes have **no** face painted?",
   "Strip one layer from every side: the unpainted core is (5 − 2)³ = 3³ = **27**.",
   diff="easy", t=30)
pc("pc4b", 6, 0, [152, 216, 96],
   "A painted cube of side 6 is cut into 216 unit cubes. How many unit cubes have no "
   "painted face?",
   "The inner block measures (6 − 2) × (6 − 2) × (6 − 2) = 4³ = **64**.", t=35)

# pc-p5: combined counts
_c4 = paint_counts(4)
assert _c4[3] + _c4[2] == 32
NQ.append(Q(nid("painted-cubes"),
            "A cube of side 4 cm is painted on all faces and cut into 1 cm cubes. How many "
            "small cubes have **at least two** painted faces?",
            _c4[3] + _c4[2], [24, 56, 44],
            f"Corners plus edge cubes: {_c4[3]} + 12 × (4 − 2) = {_c4[3]} + {_c4[2]} = "
            f"**{_c4[3] + _c4[2]}**.",
            shortcut="At least two = corners + edges = 8 + 12(n − 2).",
            diff="medium", sub="painted-cubes", pat="pc-p5", t=40,
            check=_c4[3] + _c4[2]))
_c5 = paint_counts(5)
assert 5 ** 3 - _c5[0] == 98
NQ.append(Q(nid("painted-cubes"),
            "A painted cube of side 5 is cut into unit cubes. How many unit cubes have "
            "paint on **at least one** face?",
            5 ** 3 - _c5[0], [125, 27, 61],
            f"Everything except the hidden core: 5³ − (5 − 2)³ = 125 − {_c5[0]} = **98**.",
            shortcut="At least one = n³ − (n − 2)³.",
            diff="medium", sub="painted-cubes", pat="pc-p5", t=40,
            check=5 ** 3 - _c5[0]))

# pc-p6: cuboids
pc("pc6a", None, 0, [12, 6, 24],
   "A cuboid 6 cm × 4 cm × 3 cm is painted on all faces and cut into 1 cm cubes. How "
   "many small cubes have **no** face painted?",
   "Strip one layer from each side: the core measures (6 − 2) × (4 − 2) × (3 − 2) = "
   "4 × 2 × 1 = **8**.", diff="medium", t=45, cuboid=(6, 4, 3))
pc("pc6b", None, 1, [26, 78, 48],
   "A cuboid 6 × 5 × 4 is painted on all faces and cut into unit cubes. How many unit "
   "cubes have **exactly one** face painted?",
   "Each pair of opposite faces keeps a block away from the edges: 2 × [(6 − 2)(5 − 2) "
   "+ (5 − 2)(4 − 2) + (4 − 2)(6 − 2)] = 2 × (12 + 6 + 8) = 2 × 26 = **52**.",
   diff="hard", t=60, cuboid=(6, 5, 4))

# pc-p7: find n from a count
_e2 = 36
_n = _e2 // 12 + 2
assert _e2 % 12 == 0 and paint_counts(_n)[2] == _e2
NQ.append(Q(nid("painted-cubes"),
            f"A cube is painted on all its faces and cut into identical small cubes. "
            f"Exactly **{_e2}** small cubes have exactly two painted faces. How many "
            f"small cubes have exactly **one** painted face?",
            paint_counts(_n)[1], [45, 36, 72],
            f"12(n − 2) = {_e2} gives n − 2 = {_e2 // 12}, so n = {_n}. Then one-face "
            f"cubes = 6(n − 2)² = 6 × {_e2 // 12}² = 6 × {_e2 // 12 ** 2} = "
            f"**{paint_counts(_n)[1]}**.",
            shortcut="Divide by 12 to get n − 2, then use 6(n − 2)².",
            diff="hard", sub="painted-cubes", pat="pc-p7", t=50,
            check=paint_counts(_n)[1]))
_e2 = 48
_n = _e2 // 12 + 2
assert _e2 % 12 == 0 and paint_counts(_n)[2] == _e2
NQ.append(Q(nid("painted-cubes"),
            f"A painted cube is cut into unit cubes, and exactly **{_e2}** of them have "
            f"exactly two painted faces. How many unit cubes have **no** painted face?",
            paint_counts(_n)[0], [56, 27, 8],
            f"12(n − 2) = {_e2} gives n − 2 = {_e2 // 12}, so n = {_n}. The unpainted "
            f"core is (n − 2)³ = {_e2 // 12}³ = **{paint_counts(_n)[0]}**.",
            shortcut="Find n from 12(n − 2), then use (n − 2)³.",
            diff="hard", sub="painted-cubes", pat="pc-p7", t=50,
            check=paint_counts(_n)[0]))

# ================================================================== save
upsert(d["practice"], NQ)
finish(T, d)
