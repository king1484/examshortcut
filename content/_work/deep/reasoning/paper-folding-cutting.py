"""Phase-2 deep content for reasoning/paper-folding-cutting. Idempotent: `py -3 paper-folding-cutting.py`.

Every answer comes from paper_fold_engine: the sheet is folded by exact reflection
(Fractions) on a half-unit lattice, a punch makes one hole at every original lattice
point whose folded position is the punch, and holes/layers are brute-forced from that
model - never reasoned out by hand. Figure options are drawn with the same model, so
option SVGs are distinct exactly when the hole sets differ.
"""
import os
import sys
from fractions import Fraction as F

sys.path.insert(0, os.path.dirname(__file__))
from _lib import Q, finish, load, set_sub, upsert  # noqa
from paper_fold_engine import build, cross, fold_svg, min_gap, reflect, sheet_svg, sgn  # noqa
from paper_folding_cutting_notes import NOTES, PATTERNS, PYQS  # noqa

T = "paper-folding-cutting"
d = load(T)
for sid, notes in NOTES.items():
    set_sub(d, sid, notes=notes, patterns=PATTERNS[sid])
d["pyqPatterns"] = PYQS

NQ = []
_ctr = {}


def nid(sub):
    _ctr[sub] = _ctr.get(sub, 0) + 1
    return f"{sub}-p{_ctr[sub]:02d}"


# ================================================================== facts used in the notes
# vertical fold keeps height; main diagonal swaps x and y; anti-diagonal (x,y)->(S-y,S-x)
p1 = build([("V", "L")])
assert p1.holes([(6.5, 1.5)]) == {(1.5, 1.5), (6.5, 1.5)}
pd = build([("D", ("main", "TR"))])
assert pd.holes([(1.5, 2.5)]) == {(2.5, 1.5), (1.5, 2.5)}
pa = build([("D", ("anti", "TL"))])
assert pa.holes([(6.5, 6.5)]) == {(6.5, 6.5), (1.5, 1.5)}
# quarter fold: 4 corner holes for a punch near the open corner (worked example)
pq = build([("V", "L"), ("H", "T")])
assert pq.holes([(6.5, 6.5)]) == {(6.5, 6.5), (1.5, 1.5), (6.5, 1.5), (1.5, 6.5)}
# crease punches merge: centre of a quarter fold -> 1 hole; one crease -> 2 holes
assert pq.holes([(4, 4)]) == {(4, 4)}
assert pq.holes([(6.5, 4)]) == {(6.5, 4), (1.5, 4)}
# strip fold: doubled part 2 holes, single part 1 hole
ps = build([("VS", (2, "L"))])
assert ps.holes([(3.5, 1.5)]) == {(3.5, 1.5), (0.5, 1.5)}
assert ps.holes([(3.5, 1.5), (6.5, 6.5)]) == {(3.5, 1.5), (0.5, 1.5), (6.5, 6.5)}
# notes example: top quarter folded down, then half left over right -> 4 + 2 = 6 holes
pe = build([("HS", (2, "T")), ("V", "L")])
assert len(pe.holes([(5.5, 2.5)])) == 4 and len(pe.holes([(5.5, 6.5)])) == 2
# letter fold on S=6: two strip folds give 3 layers, halving again gives 6
pl = build([("VS", (4, "R")), ("VS", (2, "L"))], S=6)
assert pl.layers((3, 1)) == 3
assert build([("VS", (4, "R")), ("VS", (2, "L")), ("V", "L")], S=6).layers((3.5, 1)) == 6
# full folds double: 3 folds, 1 punch -> 8 holes
assert len(build([("V", "L"), ("H", "T"), ("V", "R")]).holes([(5.5, 5.5)])) == 8
assert len(build([("V", "L"), ("H", "T"), ("V", "R"), ("H", "B")]).holes([(5.5, 5.5)])) == 16


# ================================================================== question builders
def on_paper(p, q):
    """Exact point-in-mesh test against the folded paper q (Fractions)."""
    for t in q.tris:
        ds = [cross(t[i], t[(i + 1) % 3], p) for i in range(3)]
        if all(v >= 0 for v in ds) or all(v <= 0 for v in ds):
            return True
    return False


def chain(folds, punches):
    """Visible hole marks as the folds are undone one by one (last fold first).

    Undoing a fold gives every mark a mirror copy across that fold line - but only
    where the folded-over flap actually reached, i.e. only if the reflected point
    lies on the intermediate paper. The final entry must equal the brute-forced
    hole count."""
    pp = build(folds)
    marks = {(F(x), F(y)) for x, y in punches}
    out = [len(marks)]
    for j in reversed(range(len(folds))):
        _reg, a, b, _mover = pp.stages[j]
        qj = build(folds[:j])
        marks |= {r for m in marks for r in (reflect(a, b, m),)
                  if r != m and on_paper(r, qj)}
        if j:
            out.append(len(marks))
    assert len(marks) == len(pp.holes(punches)), "unfold chain disagrees with the model"
    out.append(len(marks))
    return out


def fp_q(pat, folds, punches, mode_at=None, diff="medium", t=60):
    sub = "fold-punch"
    qid = nid(sub)
    pp = build(folds)
    ans = pp.holes(punches)
    assert len(ans) >= 1, qid
    if len(ans) >= 2:
        assert min_gap(sorted(ans)) >= 1, f"{qid}: holes too close"
    S = pp.S
    cands = []
    if mode_at is not None:
        cands.append(build(folds, mode_at=mode_at).holes(punches))       # rotated, not reflected
    if len(folds) >= 2:
        cands.append(build(folds[:-1]).holes(punches))                    # last unfold forgotten
    cands.append({(S - x, y) for x, y in ans})                            # mirrored left-right
    cands.append({(x, S - y) for x, y in ans})                            # mirrored top-bottom
    cands.append({(S - x, S - y) for x, y in ans})                        # half turn
    for dx, dy in ((0.5, 0.5), (0.5, -0.5), (-0.5, 0.5), (-0.5, -0.5),
                   (1, 0), (0, 1), (-1, 0), (0, -1)):                     # punch at a nearby spot
        try:
            sh = [(x + dx, y + dy) for x, y in punches]
            cands.append(build(folds).holes(sh))
        except AssertionError:
            pass
    seen, wrong = {frozenset(ans)}, []
    for c in cands:
        if frozenset(c) in seen:
            continue
        seen.add(frozenset(c))
        wrong.append(sheet_svg(sorted(c)))
        if len(wrong) == 3:
            break
    assert len(wrong) == 3, f"{qid}: not enough distinct distractors"
    ch = chain(folds, punches)
    sol = ("A punch goes through every layer, so it opens into one hole per layer. Unfold in "
           "reverse order, mirroring the holes across each fold line: the count goes "
           + " - ".join(str(c) for c in ch) + ".")
    if len(set(ch)) == 1:
        sol += " The copies keep landing on the same spot because the punch sits on a crease."
    NQ.append(Q(qid,
                "A square sheet of paper is folded as shown by the dashed lines and arrows, "
                "and then punched at the marked position(s). How will the sheet look when it "
                "is opened?",
                sheet_svg(sorted(ans)), wrong, sol,
                shortcut="Count first: each full fold doubles the holes; then check positions.",
                diff=diff, sub=sub, pat=pat, t=t, figure=fold_svg(pp, punches)))


def count_q(pat, folds, punches, S=8, ans=None, wrong=(), diff="medium", t=30,
            text=None, figure=False, sol=None):
    sub = "layers-count"
    qid = nid(sub)
    pp = build(folds, S=S)
    holes = pp.holes(punches)
    check = len(holes)
    if ans is not None:
        assert ans == check, f"{qid}: computed {check} != stored {ans}"
    lay = [pp.layers(p) for p in punches]
    if sol is None:
        sol = ("Layers under the punch" + ("es" if len(punches) > 1 else "") + ": "
               + ", ".join(str(x) for x in lay)
               + f", so the opened sheet has {lay[0] if len(lay) == 1 else ' + '.join(str(x) for x in lay)}"
               + f" = {check} h" + ("ole." if check == 1 else "oles."))
        ch = chain(folds, punches)
        if len(folds) > 1 and len(set(ch)) > 1:
            sol += " Unfolding one fold at a time: " + " - ".join(str(c) for c in ch) + "."
    NQ.append(Q(qid, text, str(check), [str(w) for w in wrong], sol,
                shortcut="Holes = sum of the layers under each punch.",
                diff=diff, sub=sub, pat=pat, t=t,
                figure=fold_svg(pp, punches) if figure else None))


def layer_q(pat, layers, ans, wrong, text, diff="medium", t=30):
    NQ.append(Q(nid("layers-count"), text, str(ans), [str(w) for w in wrong],
                "Doubling for every full fold; a three-way fold contributes its factor "
                "directly.", shortcut="Multiply the layer factor of each step.",
                diff=diff, sub="layers-count", pat=pat, t=t, check=layers))


# ================================================================== fold-punch questions
# fp-p1: single half fold ------------------------------------------------------
fp_q("fp-p1", [("V", "L")], [(6.5, 1.5)], mode_at=0, diff="easy")
fp_q("fp-p1", [("H", "B")], [(1.5, 1.5)], mode_at=0, diff="easy")

# fp-p2: quarter fold ----------------------------------------------------------
fp_q("fp-p2", [("V", "L"), ("H", "T")], [(6.5, 6.5)], mode_at=0, diff="medium")
fp_q("fp-p2", [("V", "R"), ("H", "B")], [(3.5, 3.5)], mode_at=1, diff="medium")

# fp-p3: diagonal fold ---------------------------------------------------------
fp_q("fp-p3", [("D", ("main", "TR"))], [(1.5, 2.5)], mode_at=0, diff="medium")
fp_q("fp-p3", [("D", ("anti", "TL"))], [(6.5, 6.5)], mode_at=0, diff="medium")

# fp-p4: strip (partial) fold --------------------------------------------------
fp_q("fp-p4", [("VS", (2, "L"))], [(3.5, 1.5), (6.5, 6.5)], mode_at=0, diff="medium")
fp_q("fp-p4", [("HS", (6, "B"))], [(1.5, 5.5), (4.5, 1.5)], mode_at=0, diff="medium")

# fp-p5: three folds -----------------------------------------------------------
fp_q("fp-p5", [("V", "L"), ("H", "T"), ("D", ("anti", "TL"))], [(6.5, 7.5)], mode_at=2,
     diff="hard", t=90)
fp_q("fp-p5", [("V", "L"), ("H", "B"), ("V", "R")], [(4.5, 1.5)], mode_at=0, diff="hard", t=90)

# fp-p6: punch on a fold line --------------------------------------------------
fp_q("fp-p6", [("V", "L"), ("H", "T")], [(4, 4)], diff="hard", t=90)      # both creases -> 1 hole
fp_q("fp-p6", [("V", "R"), ("H", "B")], [(3.5, 4)], diff="hard", t=90)    # one crease -> 2 holes

# ================================================================== layers-count questions
# lc-p1: holes after full folds ------------------------------------------------
count_q("lc-p1", [("V", "L"), ("H", "T"), ("V", "R")], [(5.5, 5.5), (4.5, 6.5)],
        wrong=(12, 8, 6), diff="easy",
        text="A square sheet of paper is folded in half three times (each fold halves the "
             "folded sheet again), and then **two** holes are punched through all the layers. "
             "How many holes will the opened sheet have?")
count_q("lc-p1", [("V", "L"), ("H", "T"), ("V", "R"), ("H", "B")], [(5.5, 5.5)],
        wrong=(12, 32, 8), diff="medium",
        text="A square sheet is folded in half four times, and one hole is punched through "
             "all the layers. How many holes appear when it is opened?")

# lc-p2: holes after a strip fold ----------------------------------------------
count_q("lc-p2", [("VS", (2, "L"))], [(3.5, 1.5), (2.5, 6.5), (6.5, 6.5)],
        wrong=(6, 4, 3), diff="medium",
        text="A square sheet has its left quarter folded over onto the quarter next to it. "
             "Then three holes are punched: two through the doubled part and one through the "
             "single part. How many holes does the opened sheet have?")
count_q("lc-p2", [("HS", (2, "T")), ("V", "L")], [(5.5, 2.5), (5.5, 6.5)],
        wrong=(4, 8, 3), diff="hard", t=45,
        text="The top quarter of a square sheet is folded down, and then the whole sheet is "
             "folded in half from left to right. One hole is punched where the folded flap "
             "lies and one hole below it. How many holes does the opened sheet have?")

# lc-p3: punch on a crease -----------------------------------------------------
count_q("lc-p3", [("V", "L")], [(4, 1.5)], wrong=(2, 4, 3), diff="medium",
        text="A square sheet is folded in half from left to right, and one hole is punched "
             "exactly on the folded edge (the crease), halfway up. How many holes does the "
             "opened sheet have?",
        sol="A punch on a crease makes no separate copy: the mirror image of the hole across "
            "the fold line falls on the same spot, so the two plies open as just **1** hole, "
            "on the crease.")
count_q("lc-p3", [("D", ("main", "TR"))], [(1.5, 1.5)], wrong=(2, 3, 4), diff="hard", t=45,
        text="A square sheet is folded along its diagonal and one hole is punched exactly on "
             "the folded (diagonal) edge. How many holes does the opened sheet have?",
        sol="The punch sits on the crease itself, so its mirror copy across the diagonal "
            "coincides with it. The opened sheet shows only **1** hole, on the diagonal.")

# lc-p4: number of layers ------------------------------------------------------
layer_q("lc-p4", 3, 3, (2, 4, 6), diff="easy",
        text="A rectangular sheet is folded into three equal strips, the way a letter is "
             "folded before going into an envelope. How many layers of paper are there?")
layer_q("lc-p4", 6, 6, (3, 5, 9), diff="medium",
        text="A sheet is folded into three equal strips and then folded in half once more. "
             "How many layers of paper are there now?")

# lc-p5: hole count from a figure ----------------------------------------------
count_q("lc-p5", [("V", "L"), ("H", "T")], [(6.5, 6.5), (5.5, 5.5)],
        wrong=(4, 6, 2), diff="medium", figure=True,
        text="A square sheet of paper is folded as shown, and then punched at the two marked "
             "positions. How many holes will the opened sheet have?")
count_q("lc-p5", [("HS", (6, "B"))], [(1.5, 5.5), (5.5, 5.5), (4.5, 1.5)],
        wrong=(6, 4, 3), diff="hard", t=60, figure=True,
        text="A square sheet of paper is folded as shown, and then punched at the three "
             "marked positions. How many holes will the opened sheet have?")

# ================================================================== save
upsert(d["practice"], NQ)
finish(T, d)
