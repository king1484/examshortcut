# build paper-folding-cutting topic (topic 17); every hole pattern comes from engines.fold_sim
from fractions import Fraction as Fr
import common as C
from engines import fold_sim, fold_question_svg, holes_svg, reflect, inside, clip

S = 4
VL = ((2, 0), (2, 4), (3, 2))     # left half folded onto the right half
VR = ((2, 0), (2, 4), (1, 2))     # right half folded onto the left half
HT = ((0, 2), (4, 2), (2, 3))     # top half folded down
HB = ((0, 2), (4, 2), (2, 1))     # bottom half folded up
D1 = ((0, 0), (4, 4), (1, 3))     # top-right triangle folded onto bottom-left
D2 = ((4, 0), (0, 4), (3, 3))     # top-left triangle folded onto bottom-right

QF = ("A square sheet of paper is folded as shown by the dashed lines and arrows, and then punched at the marked "
      "position(s). How will the sheet look when it is completely unfolded?")


def F(pt):
    return tuple(map(Fr, pt))


def stages(folds, punches):
    """hole sets after unfolding 0, 1, ..., all folds (reverse order)."""
    reg, full = fold_sim(S, folds, punches)
    holes = {F(q) for q in punches}
    out = [set(holes)]
    for k in range(len(folds) - 1, -1, -1):
        l1, l2, kp = folds[k]
        new = set(holes)
        for q in holes:
            r = reflect(q, l1, l2)
            if inside(r, reg[k]):
                new.add(r)
        holes = new
        out.append(set(holes))
    assert holes == full
    return out


TRANS = [lambda p: (S - p[0], p[1]), lambda p: (p[0], S - p[1]), lambda p: (p[1], p[0]),
         lambda p: (S - p[1], S - p[0]), lambda p: (S - p[1], p[0]), lambda p: (S - p[0], S - p[1])]


def distractors(folds, punches):
    st = stages(folds, punches)
    full = frozenset(st[-1])
    cands = [frozenset(s) for s in st[:-1][::-1]]                 # partially unfolded
    cands += [frozenset(t(p) for p in full) for t in TRANS]       # wrongly oriented
    cands += [frozenset(t(p) for p in s) for s in st[:-1] for t in TRANS]
    out = []
    for c in cands:
        if c != full and c not in out and len(c) > 0:
            out.append(c)
    # prefer: one partial, then oriented variants, keep 3
    assert len(out) >= 3, 'not enough distractors'
    return full, out[:3]


def fold_q(id, folds, punches, sol, sc, d, pat, t=50, place=None):
    full, wrong = distractors(folds, punches)
    opts = [holes_svg(S, full)] + [holes_svg(S, w) for w in wrong]
    assert len(set(opts)) == 4
    return C.Q(id, QF, opts, opts[0], sol, sc=sc, d=d, sub='fold-punch', pat=pat, t=t,
               fig=fold_question_svg(S, folds, punches), place=place), len(full)


subs = []

subs.append(C.sub(
    'fold-punch', 'Folding and punching: unfolding the pattern',
    "When a folded sheet is punched, the punch goes through **every layer** under that spot. Unfolding is done **in reverse order**: undo the last fold first, and each time every existing hole gets a **mirror copy across that fold line** (on the part that was folded over).\n\n"
    "Checklist:\n1. Note the order of folds and the final punch position.\n2. Undo the last fold: reflect each hole across its line.\n3. Repeat for each earlier fold.\n4. Compare positions (not just the count) with the options.\n\n"
    "A hole lands only where the folded-over flap actually covered the punch: if a narrow strip is folded over, holes punched outside the strip stay single.",
    tricks=[
        C.T(
            'Reflect, do not rotate',
            "Each unfold is a mirror reflection across the fold line — a hole near the top-right, unfolded across a vertical midline, reappears near the top-left at the same height.",
            "**Q.** A sheet is folded left-over-right and punched near the top-right corner. Where are the holes after unfolding?\n\n**Sol.** Reflect across the vertical midline: one hole top-right, one top-left, both at the same height.",
            "Same distance from the fold line on the other side."),
        C.T(
            'Layer count shortcut',
            "Holes in the final sheet = punches × layers at the punched spot. Each full half-fold doubles the layers: 1 fold → 2, 2 folds → 4, 3 folds → 8.",
            "**Q.** A sheet folded in half twice is punched once. How many holes?\n\n**Sol.** Layers = 2 × 2 = 4 → **4** holes.",
            "Count first to eliminate options, then check positions."),
    ],
    mistakes=[
        "Unfolding in the original order instead of the reverse order.",
        "Rotating hole positions instead of reflecting them.",
        "Assuming every punch doubles, even where the flap does not reach.",
    ]))

subs.append(C.sub(
    'layers-count', 'Counting layers and holes',
    "Many questions only need a count. Track the number of **layers** under each punch:\n\n"
    "- a full half-fold (vertical, horizontal or diagonal through the centre) doubles the layers everywhere on the folded result;\n"
    "- a partial fold (a strip folded over) doubles layers only inside the covered strip.\n\n"
    "Total holes = Σ (layers under each punch). With n full half-folds and p punches, holes = p × 2ⁿ.",
    formulas=[
        C.F('Holes after full half-folds', 'H = p \\times 2^{n}', 'p punches through n full half-folds.'),
    ],
    tricks=[
        C.T(
            'Doubling chain',
            "Write 1 → 2 → 4 → 8 as you read each full fold; multiply by the number of punches at the end.",
            "**Q.** Folded in half three times, 2 punches. Holes?\n\n**Sol.** 2 × 2³ = **16**.",
            "p × 2ⁿ for full folds."),
    ],
    mistakes=[
        "Adding 2 per fold instead of doubling.",
        "Doubling a punch that sits outside a partially folded strip.",
    ]))

patterns = [
    C.P('Single fold, punch', 'very common',
        "One vertical/horizontal half-fold, one or two punches.",
        "Reflect each hole across the fold line."),
    C.P('Two folds, punch', 'very common',
        "Folded into quarters, then punched.",
        "Unfold the second fold first, then the first; expect 4 holes per punch."),
    C.P('Diagonal fold', 'common',
        "A square folded along a diagonal into a triangle.",
        "Reflect across the diagonal: (x, y) swaps to (y, x) for the main diagonal."),
    C.P('Partial (strip) fold', 'occasional',
        "Only a strip is folded over, so layers differ across the sheet.",
        "Double only the punches that lie inside the covered strip."),
    C.P('Hole count only', 'common',
        "Text question: number of holes after n folds and p punches.",
        "p × 2ⁿ, adjusted for partial folds."),
]

examples = []

q, n = fold_q('rsn-folding-ex1', [VL], [(3, 1)],
              "The left half was folded onto the right half and the punch made near the top-right. Unfold: reflect the hole across the vertical midline → a second hole near the **top-left** at the same height. Final: **2 holes, both in the top half**, one on each side.",
              "One fold → 2 holes, mirror images across the fold line.", 'easy', 'single fold, punch', t=35)
assert n == 2
examples.append(q)

q, n = fold_q('rsn-folding-ex2', [VL, HT], [(3, 3)],
              "Unfold in reverse. Last fold (top onto bottom): the hole near the bottom-right gets a copy at the top-right. First fold (left onto right): both holes get copies on the left. Final: **4 holes, one near each corner region**, symmetric about both midlines.",
              "Two full folds → 4 layers → 4 holes.", 'medium', 'two folds, punch', t=45)
assert n == 4
examples.append(q)

q, n = fold_q('rsn-folding-ex3', [D1], [(1, 3)],
              "The sheet was folded along the diagonal from top-left to bottom-right. Unfolding reflects the hole across that diagonal: a hole near the bottom-left reappears near the **top-right**, at the same distance from the diagonal. Final: **2 holes**.",
              "Diagonal fold: mirror across the diagonal, not across a midline.", 'medium', 'diagonal fold', t=45)
assert n == 2
examples.append(q)

reg, holes = fold_sim(S, [VL, HT, ((2, 2), (4, 4), (2, 4))], [(Fr(5, 2), Fr(7, 2))])
assert len(holes) == 8
examples.append(C.Q(
    'rsn-folding-ex4',
    "A square sheet of paper is folded in half, folded in half again, and then folded once more along the diagonal of the small square obtained. A single hole is punched through all the layers. How many holes will the sheet have when it is completely unfolded?",
    ['8', '6', '4', '16'], '8',
    "Each fold doubles the layers: 1 → 2 → 4 → 8. One punch through 8 layers gives **8** holes.",
    sc="1 punch × 2³.", d='easy', sub='layers-count', pat='hole count only', t=30))

# ---------------------------------------------------------------- practice
pr = []
specs = [
    ([VR], [(1, 3)], "The right half was folded onto the left half; the punch is near the bottom-left. Reflect across the vertical midline → a copy near the **bottom-right** at the same height. Final: **2 holes in the bottom half**.",
     "Reflect across the fold line.", 'easy', 'single fold, punch', 35, 2),
    ([HT], [(1, 3), (Fr(7, 2), Fr(5, 2))], "The top half was folded down. Each of the two punches in the bottom half gets a mirror copy in the top half at the same distance from the horizontal midline: the hole near the bottom-left edge reappears near the top-left edge, and the one just below the midline on the right reappears just above it. Final: **4 holes**.",
     "Two punches × 2 layers.", 'medium', 'single fold, punch', 45, 4),
    ([VL, HT], [(Fr(5, 2), Fr(7, 2))], "Unfold the second fold (top onto bottom): the hole near the bottom, just right of the centre line, gets a copy near the top. Unfold the first fold (left onto right): both get copies just left of the centre line. Final: **4 holes hugging the vertical midline**, two near the top edge and two near the bottom edge.",
     "Quarters fold → 4 holes; keep track of distance from each fold line.", 'medium', 'two folds, punch', 50, 4),
    ([HT, VL], [(Fr(7, 2), Fr(5, 2))], "Unfold the last fold (left onto right) first: the hole near the right edge just below the centre gets a copy near the left edge. Then unfold the top-onto-bottom fold: both get copies just above the horizontal midline. Final: **4 holes hugging the horizontal midline**, two near each side edge.",
     "Reverse order; mirror each time.", 'medium', 'two folds, punch', 50, 4),
    ([D1], [(Fr(1, 2), 2), (1, Fr(7, 2))], "Folded along the top-left to bottom-right diagonal. Each punch is reflected across that diagonal (swap its horizontal and vertical distances): the hole near the middle of the left edge reappears near the middle of the top edge; the one near the bottom-left corner reappears near the top-right side. Final: **4 holes**.",
     "Main diagonal: (x, y) ↔ (y, x).", 'hard', 'diagonal fold', 60, 4),
    ([D2], [(3, 2)], "Folded along the top-right to bottom-left diagonal, keeping the bottom-right triangle. The hole just right of the centre reflects across that diagonal to a spot just above the centre. Final: **2 holes**.",
     "Anti-diagonal: (x, y) ↔ (4 − y, 4 − x).", 'hard', 'diagonal fold', 55, 2),
    ([HB], [(1, 1), (3, Fr(1, 2))], "The bottom half was folded up. Each punch in the top half gets a copy in the bottom half, mirrored across the horizontal midline: the one near the top-left reappears near the bottom-left; the one at the top edge on the right reappears at the bottom edge on the right. Final: **4 holes**.",
     "Mirror across the horizontal midline.", 'medium', 'single fold, punch', 45, 4),
    ([((1, 0), (1, 4), (2, 2))], [(Fr(3, 2), 1), (3, 3)], "Only the left **quarter** strip was folded over, so it covers just the strip between the first and second quarter lines. The punch inside that strip goes through 2 layers and gets a copy in the left-most strip; the punch at the lower right is outside the strip, so it stays single. Final: **3 holes**.",
     "Partial fold: double only the covered punches.", 'hard', 'partial (strip) fold', 60, 3),
    ([VL, HT], [(Fr(5, 2), Fr(5, 2)), (Fr(7, 2), Fr(7, 2))], "Two punches through 4 layers → 8 holes. The punch just off the centre produces a tight group of 4 around the centre of the sheet; the punch near the corner produces one hole near each of the four corners. Final: **8 holes**.",
     "2 punches × 4 layers.", 'hard', 'two folds, punch', 60, 8),
    ([VL, HT, ((2, 2), (4, 4), (2, 4))], [(Fr(5, 2), Fr(7, 2))], "Three folds give 8 layers. Undo the diagonal fold of the small square first (the hole near its bottom-left gets a copy near its top-right), then the horizontal fold, then the vertical fold — every step doubles. Final: **8 holes**, arranged with full symmetry about both midlines and both diagonals.",
     "Quarter + diagonal = 8-fold symmetry.", 'hard', 'diagonal fold', 70, 8),
]
for i, (folds, punches, sol, sc, d, pat, t, expect) in enumerate(specs, start=1):
    q, n = fold_q('rsn-folding-%d' % i, folds, punches, sol, sc, d, pat, t=t)
    assert n == expect, (i, n)
    pr.append(q)

# count-only questions
_, h = fold_sim(S, [VL, HT, ((3, 2), (3, 4), (Fr(7, 2), 3))], [(Fr(7, 2), Fr(7, 2))])
assert len(h) == 8
pr.append(C.Q(
    'rsn-folding-11',
    "A square sheet of paper is folded in half three times (each time the folded sheet is halved again), and one hole is punched through all layers. How many holes appear when the sheet is unfolded?",
    ['8', '6', '3', '9'], '8',
    "Layers double with each full fold: 1 → 2 → 4 → 8. One punch → **8** holes.",
    sc="2³ × 1.", d='easy', sub='layers-count', pat='hole count only', t=25))

_, h = fold_sim(S, [VL, HT], [(Fr(5, 2), Fr(5, 2)), (Fr(7, 2), Fr(5, 2)), (3, Fr(7, 2))])
assert len(h) == 12
pr.append(C.Q(
    'rsn-folding-12',
    "A square sheet is folded in half and then in half again, and **three** separate holes are punched through all the layers. How many holes will the unfolded sheet have?",
    ['12', '6', '9', '8'], '12',
    "Two full folds give 4 layers; each punch makes 4 holes: 3 × 4 = **12**.",
    sc="p × 2ⁿ = 3 × 4.", d='easy', sub='layers-count', pat='hole count only', t=25, place=2))

_, h = fold_sim(S, [D1, ((0, 4), (2, 2), (1, 3 + Fr(1, 2)))], [(2, Fr(7, 2)), (1, Fr(19, 5))])
assert len(h) == 8, len(h)
pr.append(C.Q(
    'rsn-folding-13',
    "A square sheet is folded along one diagonal to form a triangle, and the triangle is folded in half again to form a smaller triangle. Two holes are then punched through all the layers. How many holes will there be when the sheet is unfolded?",
    ['8', '4', '6', '2'], '8',
    "Diagonal fold → 2 layers; halving the triangle → 4 layers. Two punches × 4 layers = **8** holes.",
    sc="2 × 2².", d='medium', sub='layers-count', pat='hole count only', t=35))

_, h = fold_sim(S, [((1, 0), (1, 4), (2, 2))], [(Fr(3, 2), 1), (Fr(3, 2), 3), (3, 2)])
assert len(h) == 5
pr.append(C.Q(
    'rsn-folding-14',
    "A square sheet is divided into four equal vertical strips. Only the left-most strip is folded over onto the strip next to it. Then three holes are punched: two in the double-layered strip and one in the right half of the sheet (single layer). How many holes are there after unfolding?",
    ['5', '6', '4', '3'], '5',
    "The two punches in the covered strip go through 2 layers → 2 × 2 = 4 holes. The punch in the single-layer region → 1 hole. Total **5**.",
    sc="Double only what the flap covers.", d='medium', sub='layers-count', pat='partial (strip) fold', t=40, place=3))

assert len(pr) == 14
t = C.topic(
    'paper-folding-cutting', 'Paper Folding & Cutting', 'medium', {'tier1': '0-1', 'tier2': '1-2'},
    "A folded sheet is punched or cut, and you must predict the unfolded pattern. Unfold in reverse order, reflecting every hole across each fold line; count layers first (p × 2ⁿ for full folds) to eliminate options, then match positions. Diagonal folds swap the two coordinates; partial folds double only what the flap covers.",
    subs, patterns, examples, pr)
C.write_topic(t)
print('OK paper-folding-cutting')
