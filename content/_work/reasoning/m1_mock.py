# t1-mock-1 reasoning part: 25 questions, every answer machine-verified
import mk
import common as C
from engines import venn_config_svg, venn_matches, walk, dir_name, count_triangles

qs = []
PID = 'q-t1-mock-1-reasoning-%d'

# 1 letter analogy --------------------------------------------------------
a, b, c = 'CGKN', 'EIMP', 'DJOT'
correct = 'FLQV'
C.check_letter_analogy(a, b, c, correct, ['FLQV', 'FLQW', 'GLRV', 'FKQV'])
assert [C.dm(x, y) for x, y in zip(a, b)] == [2, 2, 2, 2]
qs.append(C.Q(PID % 1, '**%s : %s :: %s : ?**' % (a, b, c),
              ['FLQV', 'FLQW', 'GLRV', 'FKQV'], correct,
              "Each letter of CGKN moves 2 places forward to give EIMP (C to E, G to I, K to M, N to P). Applying +2 to DJOT gives **FLQV**.",
              "+2 throughout: D to F, J to L, O to Q, T to V.", 'easy', 'analogy', 'letter analogy (constant shift)', 40))

# 2 number analogy --------------------------------------------------------
pairs, probe, correct2 = [(3, 15), (4, 24)], 6, 48
C.check_num_analogy(pairs, probe, correct2, [48, 44, 54, 36])
qs.append(C.Q(PID % 2, '**3 : 15 :: 4 : 24 :: 6 : ?**', [48, 44, 54, 36], 48,
              "3 × 5 = 15 and 4 × 6 = 24 — the second number is **n × (n + 2)**. So 6 × 8 = **48**.",
              "n × (n + 2): 6 × 8 = 48.", 'easy', 'analogy', 'number analogy (n × (n+2))', 40))

# 3 word analogy ----------------------------------------------------------
tool_of = {'chef': 'knife', 'tailor': 'needle', 'carpenter': 'saw', 'farmer': 'plough', 'doctor': 'stethoscope'}
product_of = {'tailor': 'shirt', 'chef': 'dish', 'carpenter': 'chair'}
assert tool_of['tailor'] == 'needle' and product_of['tailor'] == 'shirt'
assert 'cloth' not in tool_of.values()
qs.append(C.Q(PID % 3, '**Chef : Knife :: Tailor : ?**', ['Needle', 'Shirt', 'Cloth', 'Machine'], 'Needle',
              "A chef's working tool is the knife; a tailor's working tool is the **needle**. Shirt is the product, cloth is the raw material, and a machine is not the hand tool that parallels the knife.",
              "Second word = the trade's tool, not its product or material.", 'easy', 'analogy', 'word analogy (worker-tool)', 35))

# 4 classification letters ------------------------------------------------
tri, odd = ['ADG', 'BEH', 'SVY'], 'OQT'
assert all(tuple(mk.CL['steps'](w)) == (3, 3) for w in tri)
assert tuple(mk.CL['steps'](odd)) == (2, 3)
qs.append(C.Q(PID % 4, 'Find the odd group of letters: **ADG, BEH, SVY, OQT**',
              ['OQT', 'ADG', 'BEH', 'SVY'], 'OQT',
              "In ADG, BEH and SVY the gap between consecutive letters is +3, +3 (A to D to G etc.). In OQT the gaps are +2 then +3 (O to Q to T), so **OQT** is the odd one.",
              "Write the letter gaps under each cluster.", 'easy', 'classification', 'letter odd-one-out (gap pattern)', 40))

# 5 classification numbers ------------------------------------------------
_cube = mk.CL['is_cube']
assert all(_cube(n) for n in (125, 216, 343)) and not _cube(400)
qs.append(C.Q(PID % 5, 'Find the odd one out: **125, 216, 343, 400**', [400, 125, 216, 343], 400,
              "125 = 5³, 216 = 6³ and 343 = 7³ are perfect cubes; 400 is not a cube (it is 20²). Odd one: **400**.",
              "Check cubes first: 5³, 6³, 7³ … 400 is not among them.", 'easy', 'classification', 'number odd-one-out (cubes)', 35))

# 6 number series ---------------------------------------------------------
C.check_number_series([5, 11, 23, 47, '?'], [95, 91, 94, 96], 95, must_fit='LIN')
qs.append(C.Q(PID % 6, 'Find the missing term: **5, 11, 23, 47, ?**', [95, 91, 94, 96], 95,
              "Each term = previous × 2 + 1: 5×2+1 = 11, 11×2+1 = 23, 23×2+1 = 47, so next = 47×2+1 = **95**.",
              "×2 + 1 throughout.", 'easy', 'series', 'number series (×2 + 1)', 40))

# 7 letter series ---------------------------------------------------------
C.check_letter_series(['B', 'D', 'G', 'K', 'P', '?'], ['V', 'U', 'W', 'T'], 'V')
qs.append(C.Q(PID % 7, 'Find the next letter: **B, D, G, K, P, ?**', ['V', 'U', 'W', 'T'], 'V',
              "Gaps: B to D = +2, D to G = +3, G to K = +4, K to P = +5. Next gap +6: P (16) + 6 = 22, the 22nd letter is **V**.",
              "Increasing gaps +2, +3, +4, +5, +6.", 'medium', 'series', 'letter series (growing gap)', 45))

# 8 letter-cluster series -------------------------------------------------
C.check_letter_series(['ACE', 'BDF', 'CEG', 'DFH', '?'], ['EGI', 'FGH', 'EFH', 'EGH'], 'EGI')
qs.append(C.Q(PID % 8, 'Find the next group: **ACE, BDF, CEG, DFH, ?**', ['EGI', 'FGH', 'EFH', 'EGH'], 'EGI',
              "Every letter moves +1 from group to group: 1st letters A, B, C, D give **E**; 2nd letters C, D, E, F give **G**; 3rd letters E, F, G, H give **I**. Next group **EGI**.",
              "Track each position separately: all +1.", 'medium', 'series', 'letter-cluster series (parallel +1)', 45))

# 9 coding (letters) ------------------------------------------------------
mk.CD['check_word_code']('TEACHER', 'VGCEJGT', 'COLLEGE', 'EQNNGIG', ['EQNNGIG', 'EQNNGIH', 'EPNNGIG', 'DQNNGIG'])
qs.append(C.Q(PID % 9, "In a code, **TEACHER** is written as **VGCEJGT**. How will **COLLEGE** be written in that code?",
              ['EQNNGIG', 'EQNNGIH', 'EPNNGIG', 'DQNNGIG'], 'EQNNGIG',
              "Every letter of TEACHER moves +2 to give VGCEJGT (T to V, E to G, A to C, and so on). Shifting COLLEGE by +2: C to E, O to Q, L to N, L to N, E to G, G to I, E to G — **EQNNGIG**.",
              "+2 shift applied to every letter.", 'easy', 'coding-decoding', 'letter coding (constant shift)', 40))

# 10 coding (numbers) -----------------------------------------------------
mk.CD["check_number_coding"]('CAT', 24, 'DOG', 26, [26, 25, 27, 30])
assert C.p('C') + C.p('A') + C.p('T') == 24
qs.append(C.Q(PID % 10, "If **CAT** is coded as **24**, how will **DOG** be coded?",
              [26, 25, 27, 30], 26,
              "Code = sum of letter positions: C(3) + A(1) + T(20) = 24. So DOG = 4 + 15 + 7 = **26**.",
              "Add the alphabet values.", 'easy', 'coding-decoding', 'number coding (letter-position sum)', 40))

# 11 mathematical operations ----------------------------------------------
base_nums = [8, 4, 2, 6, 3]
sub_ops = mk.MO['apply_map'](['×', '+', '−', '÷'], {'×': '+', '+': '/', '−': '*', '÷': '-'})
val = mk.MO['ev'](base_nums, sub_ops)
assert val == 17, val
assert mk.MO['ev'](base_nums, ['*', '+', '-', '/']) == 32
qs.append(C.Q(PID % 11, "If **×** means **+**, **+** means **÷**, **−** means **×** and **÷** means **−**, find the value of\n\n**8 × 4 + 2 − 6 ÷ 3**",
              [17, 32, 33, 21], 17,
              "After the substitution the expression becomes 8 + 4 ÷ 2 × 6 − 3. BODMAS: ÷ and × first, left to right — 4 ÷ 2 = 2, then 2 × 6 = 12. Then 8 + 12 − 3 = **17**. (Solving without substituting gives 32 — a trap option.)",
              "Rewrite with the new signs, then apply BODMAS.", 'medium', 'mathematical-operations', 'symbol substitution (BODMAS)', 60))

# 12 missing number -------------------------------------------------------
rows = [(4, 7, 33), (5, 3, 20)]
mk.MN["check_missing"](rows, (6, 2), 17, [17, 12, 22, 16])
qs.append(C.Q(PID % 12, "Find the missing number.\n\n| 4 | 7 | 33 |\n|---|---|---|\n| 5 | 3 | 20 |\n| 6 | 2 | **?** |",
              [17, 12, 22, 16], 17,
              "Row rule: (first × second) + 5. Check: 4 × 7 + 5 = 33 and 5 × 3 + 5 = 20. So 6 × 2 + 5 = **17**.",
              "first × second + 5.", 'easy', 'missing-number', 'row grid (product + constant)', 45))

# 13 blood relations ------------------------------------------------------
BLr = mk.BL
BLr["reset"]()
BLr["person"]('Ravi', 'M')
BLr["person"]('Sita', 'F', parents=('Ravi',))
BLr["person"]('Vikram', 'M')
BLr["person"]('Sita', 'F', parents=('Ravi',), spouse='Vikram')
BLr["person"]('Kunal', 'M', parents=('Sita', 'Vikram'))
BLr["person"]('Meena', 'F', parents=('Sita', 'Vikram'))
BLr["check_rel"]('Ravi', 'Meena', 'granddaughter', ['daughter', 'niece', 'grandmother'])
qs.append(C.Q(PID % 13, "**Ravi** is the father of **Sita**. Sita is married to **Vikram**, and they have two children, **Kunal** and **Meena**. How is Meena related to Ravi?",
              ['Granddaughter', 'Daughter', 'Niece', 'Grandmother'], 'Granddaughter',
              "Sita is Ravi's daughter, and Meena is Sita's daughter — so Meena is Ravi's **granddaughter**.",
              "Two generations below, through the daughter.", 'easy', 'blood-relations', 'direct family tree', 35))

# 14 blood relations (uncle) ---------------------------------------------
BLr["reset"]()
BLr["person"]('O', 'M')
BLr["person"]('P2', 'F', spouse='O')
BLr["person"]('A', 'M', parents=('O', 'P2'))
BLr["person"]('B', 'F', parents=('O', 'P2'), spouse='D1')
BLr["person"]('D1', 'M', spouse='B')
BLr["person"]('C', 'F', parents=('B', 'D1'))
BLr["check_rel"]('C', 'A', 'uncle', ['grandfather', 'father', 'brother'])
qs.append(C.Q(PID % 14, "**A** is the brother of **B**, and B is the mother of **C**. How is A related to C?",
              ['Uncle', 'Grandfather', 'Father', 'Brother'], 'Uncle',
              "A is the brother of C's mother, so A is C's maternal **uncle**.",
              "Mother's brother = uncle.", 'easy', 'blood-relations', 'sibling-of-parent chain', 40))

# 15 direction ------------------------------------------------------------
x, y, d = walk('N', [('F', 5), ('R', 8), ('R', 5), ('L', 4)])
assert (x, y) == (12, 0) and dir_name(x, y) == 'East'
qs.append(C.Q(PID % 15, "**Ravi** walks 5 km towards north, then turns right and walks 8 km. He turns right again and walks 5 km, then turns left and walks 4 km. How far and in which direction is he from the starting point?",
              ['12 km East', '12 km West', '13 km North-East', '22 km East'], '12 km East',
              "North 5, then right (east) 8, right (south) 5, left (east) 4. The 5 km north and 5 km south cancel; east total = 8 + 4 = **12 km East**.",
              "Opposite legs cancel; add same-direction legs.", 'easy', 'direction-distance', 'grid walk (cancelling legs)', 45))

# 16 order / ranking ------------------------------------------------------
order = mk.OR['check_order'](['A', 'B', 'C', 'D', 'E'], [('A', 'B'), ('C', 'A'), ('D', 'C'), ('B', 'E')])
assert order == ('D', 'C', 'A', 'B', 'E'), order
qs.append(C.Q(PID % 16, "Among five trees, **A** is taller than **B** but shorter than **C**. **D** is taller than **C**, and **E** is shorter than **B**. Which tree is the second tallest?",
              ['C', 'A', 'D', 'B'], 'C',
              "Chain the clues: D > C > A > B > E. The second tallest is **C**.",
              "Build one chain: D > C > A > B > E.", 'easy', 'order-ranking', 'ordering by comparisons', 40))

# 17 seating (linear) -----------------------------------------------------
people = ['P', 'Q', 'R', 'S', 'T']


def clue(pos):
    return (pos['R'] == 2 and pos['P'] in (0, 4)
            and abs(pos['Q'] - pos['R']) == 1 and pos['T'] - pos['P'] == 3)


sols = mk.SE['lin_sols'](people, clue)
arr = mk.SE['one'](sols, 'm1-q17')
assert arr == ('P', 'Q', 'R', 'T', 'S'), arr
second_left = arr[1]
assert second_left == 'Q'
qs.append(C.Q(PID % 17, "Five friends **P, Q, R, S and T** sit in a row facing north. **R** sits exactly in the middle, **P** sits at one of the extreme ends, **Q** is an immediate neighbour of **R**, and **T** sits third to the right of **P**. Who sits **second from the left end**?",
              [second_left, 'P', 'S', 'T'], second_left,
              "T is third to the right of P, so P must be at the **left** end (seat 1), putting T at seat 4. R is in the middle (seat 3). Q touches R, so Q takes seat 2 (seat 4 is taken), leaving S at seat 5. Left to right: P, Q, R, T, S. Second from the left = **Q**.",
              "Directional clue 'third to the right' pins P's end first.", 'medium', 'seating-arrangement', 'linear row (fixed middle)', 60))

# 18 syllogism ------------------------------------------------------------
terms = ['pens', 'books', 'boxes']
prem = [mk.SY['ALL']('pens', 'books'), mk.SY['ALL']('books', 'boxes')]
mk.SY['syl'](terms, prem, (lambda m: m['pens'] <= m['boxes']), False,
             (lambda m: bool(m['boxes'] & m['pens'])), False, 'both')
qs.append(C.Q(PID % 18, "**Statements:** All pens are books. All books are boxes.\n\n**Conclusions:**\nI. All pens are boxes.\nII. Some boxes are pens.\n\nWhich of the conclusions follow(s)?",
              ['Both I and II follow', 'Only conclusion I follows', 'Only conclusion II follows', 'Neither I nor II follows'],
              'Both I and II follow',
              "Pens sit inside books, which sit inside boxes — so all pens are inside boxes (I **follows**). Pens exist, and each of them is a box, so some boxes are pens (II **follows**). Answer: **Both**.",
              "Nested circles: A in B in C gives A in C and some C are A.", 'easy', 'syllogism', 'two universal premises (chain)', 45))

# 19 Venn -----------------------------------------------------------------
rel_true = {('Doctors', 'Artists'): 'ov', ('Doctors', 'Humans'): 'in', ('Artists', 'Humans'): 'in'}
ans_kind = 'overlap_in_one'
assert venn_matches(ans_kind, rel_true)
for bad in ('overlap3', 'nested3', 'two_in_one'):
    assert not venn_matches(bad, rel_true), bad
opts_svg = [venn_config_svg(ans_kind), venn_config_svg('overlap3'), venn_config_svg('nested3'), venn_config_svg('two_in_one')]
qs.append(C.Q(PID % 19, "Which of the following diagrams best represents the relationship among **Doctors, Human beings and Artists**?",
              opts_svg, opts_svg[0],
              "Every doctor and every artist is a human being (both circles inside Humans), and one person can be both a doctor and an artist (the two inner circles **overlap**). Option A shows exactly this.",
              "Two professions inside the larger class, overlapping each other.", 'medium', 'venn-diagrams', 'best-represents diagram', 50))

# 20 dictionary order -----------------------------------------------------
words = ['Bracket', 'Braid', 'Bramble', 'Brave', 'Breach']
srt = sorted(w.lower() for w in words)
assert srt == ['bracket', 'braid', 'bramble', 'brave', 'breach'], srt
mid = words[2]
assert mid == 'Bramble'
qs.append(C.Q(PID % 20, "Arrange the words as in a dictionary and find the one that comes in the **middle**:\n\n**Bracket, Braid, Bramble, Brave, Breach**",
              ['Bramble', 'Braid', 'Brave', 'Bracket'], mid,
              "Compare letter by letter after Bra: **Bra**cket (c), **Bra**id (i), **Bra**mble (m), **Bra**ve (v) — c < i < m < v — and **Bre**ach comes last (e beats a at the third letter). Order: Bracket, Braid, **Bramble**, Brave, Breach. Middle = **Bramble**.",
              "Rank by the first differing letter.", 'easy', 'dictionary-order', 'dictionary arrangement', 45))

# 21 statement-conclusion -------------------------------------------------
FOLLOW = {'restate', 'definite', 'implied', 'implicit', 'practical'}
NOTS = {'extreme', 'outside', 'contradict', 'overgeneral', 'not-needed', 'impractical', 'necessary-not-sufficient'}
OPT_C = ['Only conclusion I follows', 'Only conclusion II follows', 'Both I and II follow', 'Neither I nor II follows']


def ok21(tag):
    assert tag in FOLLOW or tag in NOTS, tag
    return tag in FOLLOW


def verdict2(t1, t2):
    a, b = ok21(t1), ok21(t2)
    return OPT_C[{(True, False): 0, (False, True): 1, (True, True): 2, (False, False): 3}[(a, b)]]


ans21 = verdict2('definite', 'outside')
assert ans21 == 'Only conclusion I follows'
qs.append(C.Q(PID % 21,
              "**Statement:** An office notice reads — all employees must submit their tax declaration forms by 30 June; forms received after this date will attract a late fee.\n\n**Conclusions:**\nI. Employees who submit the form after 30 June will have to pay a late fee.\nII. No employee submits the form before June.\n\nWhich of the conclusions follow(s)?",
              OPT_C, ans21,
              "I directly restates the penalty clause — **follows**. II claims nobody submits before June; the notice says nothing about early submissions — outside information, **does not follow**. Answer: **Only I**.",
              "Restatement follows; new absolute claims do not.", 'easy', 'statement-conclusion', 'two conclusions (notice)', 40))

# 22 counting figures -----------------------------------------------------
segs22 = mk.CF['cev'](2, 0)
n22 = count_triangles(segs22)
assert n22 == 6, n22
qs.append(C.Q(PID % 22, mk.CF['QT'], ['6', '5', '8', '9'], str(n22),
              "Two lines from the apex divide the triangle. Lines through the apex = 2 cevians + the 2 sides = 4; any two of them form a triangle: C(4, 2) = **6**.",
              "(k+1)(k+2)/2 with k = 2 gives 6.", 'easy', 'counting-figures', 'triangle with apex lines', 35,
              fig=mk.CF['fig'](segs22)))

# 23 mirror image ---------------------------------------------------------
q23 = mk.MI['str_q'](PID % 23, 'MUG35', 'mirror',
                     "A mirror reverses left and right: the letter order flips and every asymmetric character flips (G, 3, 5), while M and U look unchanged. Option A shows exactly this image.",
                     "Only characters that differ left-right actually change.", 'easy', 'letter mirror image', 40)
q23['subtopic'] = 'mirror-water-image'
qs.append(q23)

# 24 paper folding --------------------------------------------------------
q24, holes24 = mk.PF['fold_q'](PID % 24, [mk.PF['HT']], [(1, 3)],
                               "The top half is folded down across the horizontal centre line. The punch goes through both layers, so unfolding shows a pair of holes symmetric about the horizontal centre line.",
                               "One fold gives mirror pairs across the crease.", 'easy', 'single fold, one punch', 40)
assert holes24 == 2
qs.append(q24)

# 25 cube / dice ----------------------------------------------------------
q25 = mk.CB['views_q'](PID % 25, list('ABCDEF'), [('A', 'B', 'C'), ('A', 'C', 'D')], 'B', ['A', 'E', 'F'],
                       "Both views share faces A and C. With two common faces, the remaining face of each view is opposite the other: B (view 1) and D (view 2). Opposite of B is **D**.",
                       "Two common faces: the leftovers are opposite.", 'easy', 'opposite face from two positions', 35)
qs.append(q25)

# rebalance the key: move three of the nine A-answers to D
for _i in (16, 20, 25):
    _qd = qs[_i - 1]
    assert _qd['answer'] == 0 and _qd['id'].endswith('-%d' % _i), (_i, _qd['answer'])
    mk.move(_qd, 3)

mk.finish('t1-mock-1', qs, 25)
