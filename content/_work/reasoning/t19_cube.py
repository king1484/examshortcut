# build cube-dice topic (topic 19); dice answers via engines.dice_solutions, nets via fold_net, painted cubes by brute force
import itertools
import common as C
from engines import (dice_solutions, opposite_of, fold_net, view_ok, rotations, OPP,
                     cube_svg, dice_row_svg, net_svg)

NOTE = " (Ignore the orientation of the letters/numbers.)"


def opp_unique(labels, views, ask):
    sols = dice_solutions(labels, views)
    assert sols, 'inconsistent views'
    ans = {opposite_of(c, ask) for c in sols}
    assert len(ans) == 1, (views, ask, ans)
    return ans.pop()


def views_q(id, labels, views, ask, wrong, sol, sc, d, pat, t=45):
    ans = opp_unique(labels, views, ask)
    assert ans not in wrong and ask not in wrong and len(set(wrong)) == 3
    k = len(views)
    q = ("%s different positions of the same dice are shown. Which %s is on the face opposite to **%s**?%s"
         % ({2: 'Two', 3: 'Three'}[k], 'number' if labels[0].isdigit() else 'letter', ask, NOTE))
    return C.Q(id, q, [ans] + wrong, ans, sol, sc=sc, d=d, sub='dice-positions', pat=pat, t=t, fig=dice_row_svg(views))


def net_opp_q(id, net, ask, wrong, sol, sc, d, pat, t=40):
    cube = fold_net(net)
    ans = opposite_of(cube, ask)
    assert ans not in wrong and ask not in wrong and len(set(wrong)) == 3
    q = "The given sheet is folded to form a cube. Which face will be opposite to the face showing **%s**?%s" % (ask, NOTE)
    return C.Q(id, q, [ans] + wrong, ans, sol, sc=sc, d=d, sub='cube-nets', pat=pat, t=t, fig=net_svg(net))


def net_cube_q(id, net, good, bads, sol, sc, d, pat, t=55):
    cube = fold_net(net)
    assert view_ok(cube, good)
    for b in bads:
        assert not view_ok(cube, b), b
    opts = [cube_svg(*good)] + [cube_svg(*b) for b in bads]
    assert len(set(opts)) == 4
    q = "The given sheet is folded to form a cube. Which of the following cubes can be formed?" + NOTE
    return C.Q(id, q, opts, opts[0], sol, sc=sc, d=d, sub='cube-nets', pat=pat, t=t, fig=net_svg(net))


def paint_counts(a, b, c):
    cnt = {}
    for x, y, z in itertools.product(range(a), range(b), range(c)):
        f = 0
        for v, n in ((x, a), (y, b), (z, c)):
            f += (v == 0) + (v == n - 1)
        cnt[f] = cnt.get(f, 0) + 1
    return cnt


subs = [
    C.sub('dice-positions', 'Dice: finding opposite faces from positions',
          "A die (cube) has 6 faces: each face touches 4 others and is **opposite** exactly 1. When several views of the same die are shown, use these rules:\n\n"
          "1. **Adjacent-four rule** — a face seen next to four different faces is opposite the sixth one.\n"
          "2. **Two common faces** — if two views share two faces, the remaining face in each view is opposite the other one.\n"
          "3. **Same position** — if one face is common and it sits in the **same position** in both views, the faces in matching positions are opposite (front ↔ front, right ↔ right).\n"
          "4. **Never together** — two faces seen together in any view can never be opposite.\n\n"
          "A **standard die** has opposite faces summing to 7: (1, 6), (2, 5), (3, 4).",
          formulas=[C.F('Standard die', '1+6 = 2+5 = 3+4 = 7', 'Opposite faces of a standard die.')],
          tricks=[C.T('Eliminate the neighbours',
                      "List every face seen with the asked face; strike them out. If only one face is left, it is the answer — no rotation needed.",
                      "**Q.** 4 is seen with 1, 2, 3 and 5. What is opposite 4?",
                      "Only 6 is never seen with 4, so **6**."),
                  C.T('Two common faces',
                      "Two views sharing two faces: the leftover faces are opposite.",
                      "**Q.** Views show (A, B, C) and (A, B, D). Opposite of C?",
                      "A and B are common, so **D**.")],
          mistakes=["Declaring two faces opposite just because they never appear together — check that the other four are all ruled out.",
                    "Applying the same-position rule when the common face is in different positions.",
                    "Forgetting that a standard-die fact (sum 7) only holds when the question says the die is standard."]),
    C.sub('cube-nets', 'Cube nets: folding a sheet into a cube',
          "An open (unfolded) cube is a **net** of 6 squares. To find opposite faces without folding mentally:\n\n"
          "- In any straight row or column, faces with **exactly one square between them** are opposite.\n"
          "- In a **Z (or S) shape** of four squares, the two end squares are opposite.\n"
          "- Two squares that touch along an edge in the net are always adjacent on the cube.\n\n"
          "To test whether a drawn cube can be made: first reject any cube that shows two opposite faces together; then check the order of the three visible faces around their shared corner.",
          tricks=[C.T('Skip one',
                      "Along a line of squares, skip one: 1st ↔ 3rd, 2nd ↔ 4th.",
                      "**Q.** Row A B C D in a net. Opposite of B?",
                      "Skip C → **D**.")],
          mistakes=["Treating squares that only meet at a corner in the net as opposite.",
                    "Accepting a cube that shows two faces which are opposite in the net.",
                    "Ignoring the order (clockwise/anticlockwise) of the three visible faces."]),
    C.sub('painted-cubes', 'Painted cube cut into small cubes',
          "A cube of side n painted on all faces and cut into n³ unit cubes gives:\n\n"
          "- 3 faces painted: the 8 corner cubes\n- 2 faces painted: edge cubes, 12(n − 2)\n- 1 face painted: face centres, 6(n − 2)²\n- no face painted: the inner core, (n − 2)³\n\n"
          "For a cuboid a × b × c, think the same way: corners 8, edges 4[(a−2)+(b−2)+(c−2)], faces 2[(a−2)(b−2)+(b−2)(c−2)+(c−2)(a−2)], core (a−2)(b−2)(c−2) (when every side is at least 2).",
          formulas=[C.F('Two faces painted', '12(n-2)', 'Cubes on the edges, excluding corners.'),
                    C.F('One face painted', '6(n-2)^2', 'Cubes in the middle of each face.'),
                    C.F('No face painted', '(n-2)^3', 'Hidden inner cube.')],
          tricks=[C.T('Check the total',
                      "8 + 12(n−2) + 6(n−2)² + (n−2)³ = n³. Use it to verify your counts.",
                      "**Q.** n = 3: check the four counts.",
                      "8 + 12 + 6 + 1 = 27 = 3³.")],
          mistakes=["Using n instead of (n − 2) in the formulas.",
                    "Forgetting that corner cubes always have 3 painted faces, whatever n is."]),
]

patterns = [
    C.P('Opposite face from two/three positions', 'very common',
        "Two or three drawings of the same die; ask the face opposite to X.",
        "Adjacent-four rule, two-common-faces rule, or same-position rule."),
    C.P('Standard die (sum 7)', 'occasional',
        "The die is stated to be standard / ordinary.",
        "Opposite pairs 1-6, 2-5, 3-4."),
    C.P('Opposite face in a net', 'very common',
        "An unfolded sheet with 6 labelled squares.",
        "Skip-one in a line; ends of a Z are opposite."),
    C.P('Which cube can be formed', 'common',
        "Net in the question, four cubes in the options.",
        "Reject cubes showing an opposite pair; then check the corner order."),
    C.P('Painted cube cut into pieces', 'common',
        "Cube painted and cut into n³ small cubes.",
        "8 / 12(n−2) / 6(n−2)² / (n−2)³."),
]

# ------------------------------------------------------------------- examples
examples = []
examples.append(views_q(
    'rsn-cube-ex1', list('123456'), [('1', '2', '3'), ('1', '5', '4')], '2', ['3', '4', '6'],
    "Face 1 is common to both views and sits in the **same position** (top). So faces in matching positions are opposite: the front faces 2 and 5 are opposite (and so are the right faces 3 and 4). Opposite of 2 is **5**.",
    "Common face in the same place → match the other positions.", 'easy', 'opposite face from two/three positions', 35))

net1 = {(0, 1): 'A', (1, 1): 'B', (2, 1): 'C', (3, 1): 'D', (1, 0): 'E', (2, 2): 'F'}
examples.append(net_opp_q(
    'rsn-cube-ex2', net1, 'E', ['A', 'B', 'D'],
    "A, B, C, D lie in one row: skipping one square, A is opposite C and B is opposite D. The two remaining faces, E and F, must be opposite each other. So **F** is opposite E.",
    "Pair up the row first; the leftovers pair with each other.", 'easy', 'opposite face in a net', 35))

net2 = {(1, 0): 'K', (0, 1): 'L', (1, 1): 'M', (2, 1): 'N', (1, 2): 'O', (1, 3): 'J'}
c2 = fold_net(net2)
good = next((r['U'], r['F'], r['R']) for r in rotations(c2) if r['F'] == 'M' and r['U'] == 'K')
assert good == ('K', 'M', 'N')
examples.append(net_cube_q(
    'rsn-cube-ex3', net2, good, [('K', 'O', 'L'), ('J', 'M', 'L'), ('K', 'N', 'M')],
    "Opposite pairs from the net: K–O and M–J (skip one in the column K, M, O, J) and L–N (skip one in the row L, M, N). The cube with K and O together and the one with J and M together are impossible. Of the two left, fold the net with M facing you: K folds up to the top and N folds to the right, which is exactly the cube with K on top, M in front and N on the right. The cube with N in front and M on the right has the same three faces but in the reverse order around the corner, so it cannot be formed.",
    "First strike out cubes showing an opposite pair.", 'medium', 'which cube can be formed', 60))

pc = paint_counts(4, 4, 4)
assert pc[2] == 24 == 12 * (4 - 2)
examples.append(C.Q(
    'rsn-cube-ex4',
    "A cube of side 4 cm is painted red on all its faces and then cut into small cubes of side 1 cm. How many small cubes have **exactly two** faces painted?",
    ['24', '8', '16', '32'], '24',
    "n = 4. Cubes with exactly two painted faces lie along the 12 edges, excluding the corners: each edge has n − 2 = 2 of them. Total 12 × 2 = **24**.",
    sc="12(n − 2) = 12 × 2.", d='easy', sub='painted-cubes', pat='painted cube cut into pieces', t=30))

# ------------------------------------------------------------------- practice
pr = []
pr.append(views_q(
    'rsn-cube-1', list('ABCDEF'), [('A', 'B', 'C'), ('A', 'D', 'B')], 'C', ['A', 'E', 'F'],
    "A and B appear in both views — two common faces. The remaining face of the first view (C) and the remaining face of the second view (D) must therefore be opposite. Answer **D**.",
    "Two common faces → leftovers are opposite.", 'easy', 'opposite face from two/three positions', 30))

pr.append(views_q(
    'rsn-cube-2', list('PQRSTU'), [('P', 'Q', 'R'), ('R', 'S', 'P'), ('Q', 'U', 'R')], 'P', ['Q', 'S', 'T'],
    "Views 1 and 3 share Q and R, so their leftover faces P (view 1) and U (view 3) are opposite. Answer **U**.",
    "Pick the pair of views with two common faces.", 'medium', 'opposite face from two/three positions', 45))

pr.append(views_q(
    'rsn-cube-3', list('123456'), [('4', '1', '2'), ('4', '3', '1'), ('4', '5', '3')], '4', ['1', '3', '5'],
    "4 appears with 1 and 2 (view 1), 3 and 1 (view 2), 5 and 3 (view 3). So 4 is adjacent to 1, 2, 3 and 5. The only face never seen with 4 is **6**, which must be opposite.",
    "Adjacent-four rule.", 'easy', 'opposite face from two/three positions', 35))

pr.append(views_q(
    'rsn-cube-4', list('XYZWVT'), [('X', 'Y', 'Z'), ('W', 'Y', 'V')], 'Z', ['X', 'W', 'T'],
    "Y is common and in the **same position** (front) in both views. So faces in matching positions are opposite: top X ↔ top W, right Z ↔ right V. Opposite of Z is **V**.",
    "Same position of the common face.", 'medium', 'opposite face from two/three positions', 40))

pr.append(views_q(
    'rsn-cube-5', list('123456'), [('1', '2', '3'), ('6', '4', '3')], '3', ['1', '2', '6'],
    "3 appears with 1 and 2 in the first view and with 6 and 4 in the second. So 3 is adjacent to 1, 2, 4 and 6; the only remaining face, **5**, is opposite 3.",
    "Adjacent-four rule.", 'medium', 'opposite face from two/three positions', 40))

# standard die: brute-force over the 2 standard dice (both chiralities) consistent with the view
std = []
for perm in itertools.permutations('123456'):
    c = dict(zip(['U', 'D', 'F', 'B', 'L', 'R'], perm))
    if all(int(c[p]) + int(c[OPP[p]]) == 7 for p in c) and c['U'] == '2' and c['F'] == '6' and c['R'] == '4':
        std.append(c)
assert std and all(int(c['D']) + int(c['B']) + int(c['L']) == 9 for c in std)
pr.append(C.Q(
    'rsn-cube-6',
    "An ordinary die, whose opposite faces always add up to 7, shows 2 on top, 6 in front and 4 on the right. What is the sum of the numbers on the bottom, back and left faces?",
    ['9', '12', '7', '15'], '9',
    "Opposite faces add to 7: bottom = 7 − 2 = 5, back = 7 − 6 = 1, left = 7 − 4 = 3. Sum = 5 + 1 + 3 = **9**.",
    sc="3 × 7 − (2 + 6 + 4) = 21 − 12 = 9.", d='easy', sub='dice-positions', pat='standard die (sum 7)', t=30))

net3 = {(0, 0): 'P', (1, 0): 'Q', (1, 1): 'R', (2, 1): 'S', (2, 2): 'T', (3, 2): 'U'}
pr.append(net_opp_q(
    'rsn-cube-7', net3, 'Q', ['P', 'R', 'U'],
    "The net is a staircase. Q, R, S, T form a Z shape of four squares, and the end squares of a Z are opposite: Q ↔ T. (Similarly P ↔ S and R ↔ U.) Answer **T**.",
    "Ends of a Z are opposite.", 'medium', 'opposite face in a net', 45))

net4 = {(0, 0): '1', (1, 0): '2', (2, 0): '3', (2, 1): '4', (3, 1): '5', (4, 1): '6'}
pr.append(net_opp_q(
    'rsn-cube-8', net4, '2', ['1', '3', '4'],
    "Rows of three: 1 ↔ 3 (skip 2) and 4 ↔ 6 (skip 5). The remaining two faces, 2 and 5, are opposite (they are also the ends of the Z formed by 2, 3, 4, 5). Answer **5**.",
    "Pair the rows first; the leftovers pair up.", 'medium', 'opposite face in a net', 40))

net5 = {(1, 0): 'K', (0, 1): 'L', (1, 1): 'M', (2, 1): 'N', (1, 2): 'O', (1, 3): 'J'}
cube5 = fold_net(net5)
pairs = {frozenset((a, opposite_of(cube5, a))) for a in 'KLMNOJ'}
assert pairs == {frozenset('KO'), frozenset('MJ'), frozenset('LN')}
pr.append(C.Q(
    'rsn-cube-9',
    "The given sheet is folded to form a cube. Which pair of letters will be on **opposite** faces?" + NOTE,
    ['M and J', 'K and M', 'L and O', 'N and J'], 'M and J',
    "In the column K, M, O, J skip one square: K ↔ O and M ↔ J. In the row L, M, N: L ↔ N. So **M and J** are opposite. K and M, L and O, N and J all share an edge in the net or after folding, so they are adjacent.",
    sc="Skip one along each line.", d='easy', sub='cube-nets', pat='opposite face in a net', t=35, fig=net_svg(net5)))

net6 = {(0, 0): '1', (0, 1): '2', (1, 1): '3', (2, 1): '4', (3, 1): '5', (3, 2): '6'}
c6 = fold_net(net6)
opp6 = {a: opposite_of(c6, a) for a in '123456'}
assert opp6['2'] == '4' and opp6['3'] == '5' and opp6['1'] == '6'
good6 = next((r['U'], r['F'], r['R']) for r in rotations(c6) if r['F'] == '3' and r['U'] == '1')
assert good6 == ('1', '3', '4'), good6
pr.append(net_cube_q(
    'rsn-cube-10', net6, good6, [('1', '4', '3'), ('6', '3', '1'), ('2', '3', '4')],
    "Opposite pairs: in the row 2, 3, 4, 5 → 2 ↔ 4 and 3 ↔ 5; the leftovers 1 ↔ 6. So a cube showing 1 with 6, or 2 with 4, is impossible. Between the two cubes with 1, 3, 4: fold with 3 facing you — 1 (attached above 2, which folds to the left) comes over the top, and 4 folds to the right. So 1 on top, 3 in front, 4 on the right is correct; the version with 4 in front and 3 on the right has the reverse order.",
    "Reject opposite pairs first, then check the corner order.", 'hard', 'which cube can be formed', 70))

net7 = {(0, 0): 'A', (1, 0): 'B', (2, 0): 'C', (1, 1): 'D', (1, 2): 'E', (1, 3): 'F'}
c7 = fold_net(net7)
assert opposite_of(c7, 'A') == 'C' and opposite_of(c7, 'B') == 'E' and opposite_of(c7, 'D') == 'F'
good7 = next((r['U'], r['F'], r['R']) for r in rotations(c7) if r['U'] == 'B' and r['F'] == 'D')
assert good7 == ('B', 'D', 'C'), good7
pr.append(net_cube_q(
    'rsn-cube-11', net7, good7, [('B', 'D', 'A'), ('A', 'D', 'C'), ('B', 'E', 'C')],
    "Opposite pairs: A ↔ C (row A, B, C) and B ↔ E, D ↔ F (column B, D, E, F). So cubes showing A with C or B with E are impossible. With D facing you and B folded over the top, C (to the right of B in the net) comes down on the right side and A on the left. So B top, D front, C right is correct; B top, D front, A right is its mirror and cannot be formed.",
    "Opposite pairs out; then fold around the front face.", 'hard', 'which cube can be formed', 70))

p5 = paint_counts(5, 5, 5)
assert p5[1] == 54 == 6 * 3 ** 2
pr.append(C.Q(
    'rsn-cube-12',
    "A cube of side 5 cm is painted on all faces and cut into 1 cm cubes. How many small cubes have **exactly one** face painted?",
    ['54', '36', '27', '72'], '54',
    "Each face has a (5 − 2) × (5 − 2) = 9 block of cubes with only that face painted. 6 faces × 9 = **54**.",
    sc="6(n − 2)² = 6 × 9.", d='easy', sub='painted-cubes', pat='painted cube cut into pieces', t=30))

p6 = paint_counts(6, 6, 6)
assert p6[0] == 64
pr.append(C.Q(
    'rsn-cube-13',
    "A cube of side 6 units is painted on all faces and then cut into 216 unit cubes. How many unit cubes have **no** face painted?",
    ['64', '125', '96', '27'], '64',
    "Remove the outer layer on every side: the unpainted core is (6 − 2)³ = 4³ = **64**.",
    sc="(n − 2)³.", d='easy', sub='painted-cubes', pat='painted cube cut into pieces', t=30))

pq = paint_counts(5, 4, 3)
two = pq[2]
assert two == 4 * ((5 - 2) + (4 - 2) + (3 - 2)) == 24
assert pq[0] == 3 * 2 * 1 and pq[3] == 8
pr.append(C.Q(
    'rsn-cube-14',
    "A cuboid 5 cm × 4 cm × 3 cm is painted on all faces and cut into 1 cm cubes. How many small cubes have **exactly two** faces painted?",
    ['24', '20', '28', '32'], '24',
    "Two-face cubes lie on the edges, excluding corners. There are 4 edges of each length: 4 × (5 − 2) + 4 × (4 − 2) + 4 × (3 − 2) = 12 + 8 + 4 = **24**.",
    sc="4[(a−2)+(b−2)+(c−2)] = 4 × 6.", d='medium', sub='painted-cubes', pat='painted cube cut into pieces', t=45))

assert len(pr) == 14
t = C.topic('cube-dice', 'Cube & Dice', 'medium', {'tier1': '0-1', 'tier2': '1-2'},
            "Dice questions ask for opposite faces from several positions (adjacent-four, two-common-faces and same-position rules), or from an unfolded net (skip one; ends of a Z). Painted-cube questions use 8, 12(n−2), 6(n−2)² and (n−2)³.",
            subs, patterns, examples, pr)
C.write_topic(t)
print('OK cube-dice')
