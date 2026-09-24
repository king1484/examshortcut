# t1-mock-2 and t1-mock-3 reasoning parts: 25 questions each, every answer machine-verified
# run from this directory:  python build_t1_mocks_2_3.py
import glob
import json
import math
import os
from collections import Counter
from fractions import Fraction as Fr
from itertools import combinations

import mk
import common as C
from engines import (venn_config_svg, venn_matches, venn3_svg, walk, dir_name, count_triangles, PL)

# ---------------------------------------------------------------- cross-mock duplicate guard
# preload every OTHER existing reasoning part so mk.fresh() rejects duplicates of them too
MINE = ('t1-mock-2', 't1-mock-3')
for f in glob.glob(os.path.join(C.MOCK_DIR, '*--reasoning.json')):
    d = json.load(open(f, encoding='utf-8'))
    if d['mockId'] in MINE:
        continue
    keys = mk._seen.setdefault(d['mockId'], set())
    for q in d['questions']:
        keys.add((mk._norm(q['q']), mk._norm(q.get('figure') or '')))

OPT_C = ['Only conclusion I follows', 'Only conclusion II follows', 'Both I and II follow', 'Neither I nor II follows']
OPT_A = ['Only assumption I is implicit', 'Only assumption II is implicit', 'Both I and II are implicit',
         'Neither I nor II is implicit']
FOLLOW = {'restate', 'definite', 'implied', 'implicit', 'practical'}
NOTS = {'extreme', 'outside', 'contradict', 'overgeneral', 'reverse', 'not-needed'}


def verdict(t1, t2, opts):
    for t in (t1, t2):
        assert t in FOLLOW or t in NOTS, t
    a, b = t1 in FOLLOW, t2 in FOLLOW
    return opts[{(True, False): 0, (False, True): 1, (True, True): 2, (False, False): 3}[(a, b)]]


def letter_rev_shift_check(a, b, c, correct, options):
    """a : b :: c : ?  where b = reverse(a) shifted by k. Only that rule may land on an option."""
    ks = [k for k in range(-13, 14) if C.sh(a[::-1], k) == b]
    assert len(ks) == 1, ks
    assert C.sh(c[::-1], ks[0]) == correct and correct in options
    per_index = C.shv(c, C.diffs(a, b))                 # the other rule that reproduces a -> b
    assert per_index not in options, per_index
    return ks[0]


def place_answers(qs, slots):
    assert len(slots) == len(qs)
    for qd, s in zip(qs, slots):
        mk.move(qd, s)


def difficulty_spread(qs, label, want):
    c = Counter(q['difficulty'] for q in qs)
    print(label, 'difficulty:', dict(c))
    assert (c['easy'], c['medium'], c['hard']) == want, c


def subtopic_spread(qs):
    want = {'analogy': 3, 'classification': 2, 'series': 3, 'coding-decoding': 2, 'mathematical-operations': 1,
            'missing-number': 1, 'blood-relations': 2, 'direction-distance': 1, 'order-ranking': 1,
            'seating-arrangement': 1, 'syllogism': 1, 'venn-diagrams': 1, 'dictionary-order': 1,
            'statement-conclusion': 1, 'counting-figures': 1, 'mirror-water-image': 1,
            'paper-folding-cutting': 1, 'cube-dice': 1}
    got = Counter(mk.SUBTOPIC_MAP.get(q['subtopic'], q['subtopic']) for q in qs)
    assert got == Counter(want), got


# =====================================================================================
#                                     T1 MOCK 2
# =====================================================================================
qs = []
PID = 'q-t1-mock-2-reasoning-%d'

# 1 letter analogy (opposite letters) ------------------------------------------------
o1 = ['TIRK', 'TIRJ', 'KRIT', 'THRK']
C.check_letter_analogy('FLOW', 'UOLD', 'GRIP', 'TIRK', o1)
assert C.opps('FLOW') == 'UOLD' and C.opps('GRIP') == 'TIRK'
qs.append(C.Q(PID % 1, '**FLOW : UOLD :: GRIP : ?**', o1, 'TIRK',
              "Each letter of FLOW is replaced by its **opposite letter** (the pair adds up to 27): F(6) and U(21), L(12) and O(15), O(15) and L(12), W(23) and D(4). "
              "Opposites of GRIP: G(7) to T(20), R(18) to I(9), I(9) to R(18), P(16) to K(11) — **TIRK**.",
              "Spot opposite pairs with the 27-sum rule (or the EJOTY / AZ-BY-CX memory list).",
              'medium', 'analogy', 'letter analogy (opposite letters)', 45))

# 2 number analogy (n^3 - 1) -----------------------------------------------------------
C.check_num_analogy([(4, 63), (6, 215)], 7, 342, [342, 343, 341, 350])
qs.append(C.Q(PID % 2, '**4 : 63 :: 6 : 215 :: 7 : ?**', [342, 343, 341, 350], 342,
              "4³ = 64 and 64 − 1 = 63; 6³ = 216 and 216 − 1 = 215. The rule is **n³ − 1**, so 7³ − 1 = 343 − 1 = **342**.",
              "Both second numbers sit just below a cube: n³ − 1.", 'easy', 'analogy', 'number analogy (n³ − 1)', 40))

# 3 word analogy (instrument : quantity measured) ----------------------------------
measures = {'Thermometer': 'Temperature', 'Anemometer': 'Wind speed', 'Hygrometer': 'Humidity',
            'Barometer': 'Air pressure', 'Rain gauge': 'Rainfall'}
o3 = ['Wind speed', 'Humidity', 'Air pressure', 'Rainfall']
assert measures['Anemometer'] == 'Wind speed' and all(v in measures.values() for v in o3)
qs.append(C.Q(PID % 3, '**Thermometer : Temperature :: Anemometer : ?**', o3, 'Wind speed',
              "A thermometer measures temperature; an anemometer measures **wind speed**. The other options belong to other instruments: humidity (hygrometer), air pressure (barometer), rainfall (rain gauge).",
              "Instrument : what it measures.", 'easy', 'analogy', 'word analogy (instrument-measure)', 30))

# 4 classification (odd number pair, n^2 - 1) -----------------------------------------
pairs4 = [(6, 35), (8, 63), (10, 99), (12, 145)]
fit4 = [b == a * a - 1 for a, b in pairs4]
assert fit4 == [True, True, True, False]
o4 = ['12 – 145', '6 – 35', '8 – 63', '10 – 99']
qs.append(C.Q(PID % 4, 'Find the odd number pair: **6 – 35, 8 – 63, 10 – 99, 12 – 145**', o4, '12 – 145',
              "In each pair the second number is (first)² − 1: 6² − 1 = 35, 8² − 1 = 63, 10² − 1 = 99. But 12² − 1 = 143, not 145, so **12 – 145** is the odd pair.",
              "Check n² − 1 (equivalently (n − 1)(n + 1): 5 × 7, 7 × 9, 9 × 11, 11 × 13 = 143).",
              'medium', 'classification', 'odd number pair (n² − 1)', 45))

# 5 classification (musical instruments) ---------------------------------------------
kind5 = {'Tabla': 'percussion', 'Mridangam': 'percussion', 'Dholak': 'percussion', 'Sitar': 'string'}
assert Counter(kind5.values()) == Counter({'percussion': 3, 'string': 1})
qs.append(C.Q(PID % 5, 'Find the odd one out: **Tabla, Mridangam, Sitar, Dholak**', ['Sitar', 'Tabla', 'Mridangam', 'Dholak'], 'Sitar',
              "Tabla, Mridangam and Dholak are **percussion** instruments (played by striking a drum skin). The **Sitar** is a string instrument, so it is the odd one.",
              "Group by how the instrument is played: struck vs plucked.", 'easy', 'classification', 'word odd-one-out (category)', 30))

# 6 number series (squares of primes) ------------------------------------------------
s6 = [4, 9, 25, 49, 121]
assert [int(math.isqrt(x)) for x in s6] == [2, 3, 5, 7, 11] and all(math.isqrt(x) ** 2 == x for x in s6)
assert all(mk.CL['is_prime'](math.isqrt(x)) for x in s6) and 13 ** 2 == 169
C.check_number_series(s6 + ['?'], [169, 144, 196, 225], 169)
qs.append(C.Q(PID % 6, 'Find the next term: **4, 9, 25, 49, 121, ?**', [169, 144, 196, 225], 169,
              "The terms are squares of consecutive **prime numbers**: 2², 3², 5², 7², 11². The next prime after 11 is 13, so the next term is 13² = **169**. (144 = 12² is the trap — 12 is not prime.)",
              "Take square roots: 2, 3, 5, 7, 11 are primes, so next is 13².",
              'medium', 'series', 'number series (squares of primes)', 45))

# 7 letter series with wrap-around (growing gap) --------------------------------------
C.check_letter_series(['C', 'F', 'J', 'O', 'U', '?'], ['B', 'A', 'Z', 'C'], 'B')
assert [C.p(x) for x in 'CFJOU'] == [3, 6, 10, 15, 21] and C.L(21 + 7) == 'B'
qs.append(C.Q(PID % 7, 'Find the next letter: **C, F, J, O, U, ?**', ['B', 'A', 'Z', 'C'], 'B',
              "Positions: C = 3, F = 6, J = 10, O = 15, U = 21. The gaps grow: +3, +4, +5, +6, so the next gap is +7. 21 + 7 = 28, and after Z the count restarts: 28 − 26 = 2 = **B**.",
              "Growing gap; when you cross Z, subtract 26.", 'hard', 'series', 'letter series (growing gap, wrap past Z)', 50))

# 8 alphanumeric series -----------------------------------------------------------------
terms8 = ['BF2', 'DH6', 'FJ12', 'HL20']
nxt8 = C.sh(terms8[-1][:2], 2) + str(5 * 6)
for i, t in enumerate(terms8):
    n = i + 1
    assert t[:2] == C.sh('BF', 2 * i) and int(t[2:]) == n * (n + 1)
assert nxt8 == 'JN30'
o8 = ['JN30', 'JM30', 'JN28', 'KN30']
qs.append(C.Q(PID % 8, 'Find the next term: **BF2, DH6, FJ12, HL20, ?**', o8, 'JN30',
              "Both letters move +2 each time: B, D, F, H, **J** and F, H, J, L, **N**. The numbers are 1 × 2, 2 × 3, 3 × 4, 4 × 5, so next is 5 × 6 = **30**. Next term: **JN30**.",
              "Split into letter part (+2, +2) and number part n(n + 1).", 'medium', 'series', 'alphanumeric series', 50))

# 9 coding: reverse + shift ---------------------------------------------------------------
o9 = ['OFESBH', 'HBSEFO', 'OFESBG', 'NEDRAG']
mk.CD['check_word_code']('PLANET', 'UFOBMQ', 'GARDEN', 'OFESBH', o9)
assert C.sh('PLANET'[::-1], 1) == 'UFOBMQ' and C.sh('GARDEN'[::-1], 1) == 'OFESBH'
qs.append(C.Q(PID % 9, "In a certain code language, **PLANET** is written as **UFOBMQ**. How will **GARDEN** be written in that language?", o9, 'OFESBH',
              "Write PLANET in reverse: TENALP. Now move every letter +1: T to U, E to F, N to O, A to B, L to M, P to Q — **UFOBMQ**. "
              "For GARDEN: reverse gives NEDRAG, then +1 gives **OFESBH**.",
              "If the code's first letter is near the word's last letter, suspect 'reverse, then shift'.",
              'medium', 'coding-decoding', 'letter coding (reverse + shift)', 50))

# 10 coding: letter-to-digit substitution ------------------------------------------------
code10 = {}
for w, c in (('ROSE', '6821'), ('CHAIR', '73456')):
    for ch, dg in zip(w, c):
        assert code10.get(ch, dg) == dg, ('inconsistent', ch)
        code10[ch] = dg
assert len(set(code10.values())) == len(code10)
ans10 = ''.join(code10[ch] for ch in 'SEARCH')
assert ans10 == '214673'
o10 = ['214673', '214763', '216473', '241673']
qs.append(C.Q(PID % 10, "If **ROSE** is coded as **6821** and **CHAIR** is coded as **73456**, how will **SEARCH** be coded?", o10, ans10,
              "Match letters to digits position by position. ROSE = 6821 gives R = 6, O = 8, S = 2, E = 1. CHAIR = 73456 gives C = 7, H = 3, A = 4, I = 5, R = 6 (R = 6 again, confirming the code). "
              "SEARCH = S E A R C H = 2 1 4 6 7 3 = **214673**.",
              "Build a letter-digit table once, then read the new word off it.", 'medium', 'coding-decoding', 'letter-digit substitution', 50))

# 11 mathematical operations (letters for signs) --------------------------------------
v11 = mk.MO['ev']([36, 4, 5, 12, 7], ['/', '*', '+', '-'])
assert v11 == 50
assert mk.MO['ev']([36, 4, 5, 12, 7], ['/', '*', '-', '+']) == 40
qs.append(C.Q(PID % 11, "If **A** means **÷**, **B** means **×**, **C** means **+** and **D** means **−**, find the value of\n\n**36 A 4 B 5 C 12 D 7**",
              [50, 40, 45, 38], 50,
              "Replace the letters: 36 ÷ 4 × 5 + 12 − 7. BODMAS, ÷ and × left to right: 36 ÷ 4 = 9, 9 × 5 = 45. Then 45 + 12 − 7 = **50**. (Swapping C and D by mistake gives 40.)",
              "Rewrite with signs, then BODMAS.", 'easy', 'mathematical-operations', 'letter-for-sign substitution', 45))

# 12 missing number (a^2 + b^2) ----------------------------------------------------------
mk.MN['check_missing']([(5, 3, 34), (6, 2, 40)], (7, 4), 65, [65, 57, 53, 45])
qs.append(C.Q(PID % 12, "Find the missing number.\n\n| 5 | 3 | 34 |\n|---|---|---|\n| 6 | 2 | 40 |\n| 7 | 4 | **?** |",
              [65, 57, 53, 45], 65,
              "Row rule: (first)² + (second)². Check: 5² + 3² = 25 + 9 = 34 and 6² + 2² = 36 + 4 = 40. So 7² + 4² = 49 + 16 = **65**.",
              "Third number far bigger than the product: try sum of squares.", 'medium', 'missing-number', 'row grid (sum of squares)', 50))

# 13 blood relations (coded symbols) ---------------------------------------------------
B = mk.BL
B['reset']()
B['person']('P', 'M')
B['person']('Q', 'M', parents=('P',))
B['person']('R', 'F', parents=('P',), spouse='S')
B['person']('S', 'M', spouse='R')
B['check_rel']('S', 'P', 'father-in-law', ['father', 'brother-in-law', 'uncle'])
assert 'sister' in B['rel']('Q', 'R') and 'brother' in B['rel']('R', 'Q')
qs.append(C.Q(PID % 13, "**A # B** means A is the father of B, **A $ B** means A is the brother of B, and **A @ B** means A is the wife of B.\n\nIf **P # Q $ R @ S**, how is **P** related to **S**?",
              ['Father-in-law', 'Father', 'Brother-in-law', 'Uncle'], 'Father-in-law',
              "Decode left to right: P # Q — P is the father of Q. Q $ R — Q is the brother of R, so R is also P's child. R @ S — R is the wife of S, so R is P's daughter and S is her husband. "
              "P is the father of S's wife, i.e. P is S's **father-in-law**.",
              "Chain the symbols one link at a time; a daughter's husband makes the father a father-in-law.",
              'hard', 'blood-relations', 'coded relations (symbols)', 60))

# 14 blood relations (maternal side) ----------------------------------------------------
B['reset']()
B['person']('GF', 'M')
B['person']('Arjun', 'M', parents=('GF',))
B['person']('Mom', 'F', parents=('GF',), spouse='Dad')
B['person']('Dad', 'M', spouse='Mom')
B['person']('Kavya', 'F', parents=('Mom', 'Dad'))
B['check_rel']('Kavya', 'GF', 'grandfather', ['uncle', 'father', 'father-in-law'])
B['check_rel']('Kavya', 'Arjun', 'uncle', ['father'])
qs.append(C.Q(PID % 14, "**Arjun** is the only brother of **Kavya's** mother. How is Arjun's father related to Kavya?",
              ['Grandfather', 'Uncle', 'Father', 'Father-in-law'], 'Grandfather',
              "Arjun and Kavya's mother are siblings, so Arjun's father is also the father of Kavya's mother. The mother's father is Kavya's (maternal) **grandfather**.",
              "Mother's brother's father = mother's father.", 'easy', 'blood-relations', 'relation through a sibling', 35))

# 15 direction ---------------------------------------------------------------------------
x, y, d = walk('S', [('F', 10), ('L', 6), ('L', 18), ('R', 9)])
assert (x, y) == (15, 8) and math.hypot(x, y) == 17 and dir_name(x, y) == 'North-East'
o15 = ['17 m North-East', '17 m South-East', '23 m North-East', '15 m East']
qs.append(C.Q(PID % 15, "Starting from his house, **Neeraj** walks 10 m towards south, turns left and walks 6 m, turns left again and walks 18 m, and then turns right and walks 9 m. How far and in which direction is he now from his house?",
              o15, '17 m North-East',
              "Take the house as (0, 0). South 10 m: (0, −10). Facing south, a left turn faces **east**: 6 m gives (6, −10). Another left faces **north**: 18 m gives (6, 8). A right turn faces **east**: 9 m gives (15, 8). "
              "Distance = √(15² + 8²) = √289 = **17 m**; he is east and north of the house, so **North-East**.",
              "Net east 6 + 9 = 15, net north 18 − 10 = 8; (8, 15, 17) is a Pythagorean triplet.",
              'medium', 'direction-distance', 'grid walk (Pythagoras)', 60))

# 16 order / ranking (interchange) --------------------------------------------------------
sols16 = []
for N in range(1, 101):
    rohit_left = N - 17 + 1
    if rohit_left >= 1 and rohit_left != 14 and rohit_left == 22:
        sols16.append(N)
assert sols16 == [38]
qs.append(C.Q(PID % 16, "In a row of students, **Priya** is 14th from the left end and **Rohit** is 17th from the right end. When they interchange their positions, Priya becomes **22nd from the left** end. How many students are there in the row?",
              [38, 39, 37, 31], 38,
              "After the interchange Priya stands exactly where Rohit stood. So Rohit's old place is 22nd from the left and 17th from the right. Total = 22 + 17 − 1 = **38**. "
              "(Adding 14 + 17 = 31 uses the wrong pair of positions.)",
              "Same seat seen from both ends: left + right − 1.", 'medium', 'order-ranking', 'rank interchange', 50))

# 17 seating (circular, facing centre) ----------------------------------------------------
def clue17(pos, n):
    L = lambda x, k=1: (pos[x] + k) % n      # facing the centre: left = next seat clockwise
    R = lambda x, k=1: (pos[x] - k) % n
    return (pos['D'] == (pos['A'] + 3) % n
            and pos['F'] == L('D', 2)
            and pos['B'] not in (L('A'), R('A'))
            and pos['C'] == R('E'))


arr17 = mk.SE['one'](mk.SE['circ_sols'](list('ABCDEF'), clue17, 'A'), 'm2-q17')
assert arr17 == ('A', 'C', 'E', 'D', 'B', 'F'), arr17
opp17 = arr17[(arr17.index('C') + 3) % 6]
assert opp17 == 'B'
qs.append(C.Q(PID % 17, "Six friends **A, B, C, D, E and F** sit around a circular table, equally spaced and facing the centre. **A** sits opposite **D**. **F** sits second to the left of **D**. **B** is not an immediate neighbour of **A**. **C** sits to the immediate right of **E**. Who sits opposite **C**?",
              ['B', 'F', 'E', 'D'], opp17,
              "Number the seats 1 to 6 clockwise with A at seat 1; for people facing the centre, **left = clockwise**. D is opposite A: seat 4. F is second to the left of D: seat 6. "
              "A's neighbours are seats 2 and 6, so B (not next to A) must take seat 3 or 5. C is immediately right of E, i.e. C is one seat anticlockwise of E. With seats 2, 3, 5 free, the only fit is E = 3, C = 2, which leaves B = 5. "
              "Clockwise order: A, C, E, D, B, F. Opposite C (seat 2) is seat 5: **B**.",
              "Fix A, place the opposite/definite clues first, then test the pair clue in the remaining seats.",
              'hard', 'seating-arrangement', 'circular table (facing centre)', 90))

# 18 syllogism ------------------------------------------------------------------------------
SY = mk.SY
SY['syl'](['doctors', 'teachers', 'singers'],
          [SY['SOME']('doctors', 'teachers'), SY['ALL']('teachers', 'singers')],
          SY['SOME']('doctors', 'singers'), False, SY['ALL']('singers', 'doctors'), False, 'onlyI')
qs.append(C.Q(PID % 18, "**Statements:** Some doctors are teachers. All teachers are singers.\n\n**Conclusions:**\nI. Some doctors are singers.\nII. All singers are doctors.\n\nWhich of the conclusions follow(s)?",
              OPT_C, OPT_C[0],
              "The doctors who are teachers lie inside Singers (all teachers are singers), so some doctors are definitely singers — I **follows**. "
              "Singers can include many people who are neither teachers nor doctors, so II **does not follow**. Answer: **Only I**.",
              "Some + All (in that order) gives a 'Some' conclusion; 'All' reversed never follows.",
              'medium', 'syllogism', 'some + all chain', 45))

# 19 Venn (numbers in regions) --------------------------------------------------------------
cnt19 = {'a': 12, 'b': 9, 'c': 15, 'ab': 5, 'ac': 7, 'bc': 4, 'abc': 3}
ans19 = cnt19['ac'] + cnt19['bc']
assert ans19 == 11
traps19 = [cnt19['ac'] + cnt19['bc'] + cnt19['abc'], cnt19['ab'] + cnt19['ac'] + cnt19['bc'], cnt19['c'] + cnt19['ac'] + cnt19['bc']]
assert traps19 == [14, 16, 26] and ans19 not in traps19
fig19 = venn3_svg({'a': 'Players', 'b': 'Singers', 'c': 'Graduates'}, cnt19)
qs.append(C.Q(PID % 19, "In the given diagram, the circles represent **Players**, **Singers** and **Graduates**, and the numbers show how many persons are in each region. How many **graduates are either players or singers, but not both**?",
              [11, 14, 16, 26], ans19,
              "We need the Graduates circle, but only the parts shared with exactly one of the other two circles: Graduates ∩ Players only = 7, and Graduates ∩ Singers only = 4. "
              "The centre (3) is excluded because those persons are both players and singers. Answer = 7 + 4 = **11**.",
              "Pick the two lens regions inside Graduates, leave out the centre.",
              'medium', 'venn-diagrams', 'reading a three-circle diagram', 50, fig=fig19))

# 20 dictionary order -----------------------------------------------------------------------
w20 = ['Sequence', 'Sequential', 'Sequel', 'Sequin', 'Sequester']
order20 = sorted(range(5), key=lambda i: w20[i].lower())
ans20 = ', '.join(str(i + 1) for i in order20)
assert ans20 == '3, 1, 2, 5, 4', ans20
o20 = ['3, 1, 2, 5, 4', '3, 2, 1, 5, 4', '1, 3, 2, 5, 4', '3, 1, 2, 4, 5']
qs.append(C.Q(PID % 20, "Arrange the following words in the order in which they would appear in an English dictionary.\n\n1. Sequence  2. Sequential  3. Sequel  4. Sequin  5. Sequester",
              o20, ans20,
              "All five begin with **sequ**. The 5th letter splits them: Sequ**e**l, Sequ**e**nce, Sequ**e**ntial, Sequ**e**ster come before Sequ**i**n. "
              "Among the 'seque-' words compare the 6th letter: seque**l** (l) < seque**n**ce, seque**n**tial (n) < seque**s**ter (s). Sequence is a prefix of Sequential, so it comes first. "
              "Order: Sequel (3), Sequence (1), Sequential (2), Sequester (5), Sequin (4) — **3, 1, 2, 5, 4**.",
              "A word that is the start of another word always comes before it.",
              'medium', 'dictionary-order', 'dictionary sequence (common prefix)', 60))

# 21 statement-conclusion -----------------------------------------------------------------
ans21 = verdict('reverse', 'extreme', OPT_C)
assert ans21 == OPT_C[3]
qs.append(C.Q(PID % 21, "**Statement:** Most of the students who scored above 90% in the board examination had taken coaching at Sunrise Academy.\n\n**Conclusions:**\nI. Every student who takes coaching at Sunrise Academy scores above 90%.\nII. A student who does not take coaching cannot score above 90%.\n\nWhich of the conclusions follow(s)?",
              OPT_C, ans21,
              "The statement is about **toppers**: most of them went to the academy. I reverses this into a claim about **every** academy student — the statement says nothing of academy students who scored less, so I does not follow. "
              "II is an extreme claim; 'most' toppers means some toppers did not take this coaching, and nothing is said about uncoached students at all. Neither follows.",
              "Watch for reversed direction (A mostly B does not mean B always A) and 'cannot/every' words.",
              'medium', 'statement-conclusion', 'two conclusions (reversed + extreme)', 45))

# 22 counting triangles --------------------------------------------------------------------
segs22 = PL((4, 0), (0, 6), (8, 6), (4, 0)) + PL((2, 3), (6, 3), (4, 6), (2, 3)) + [((4, 0), (4, 6))]
n22 = count_triangles(segs22)
assert n22 == 13, n22
qs.append(C.Q(PID % 22, mk.CF['QT'], ['13', '12', '11', '15'], str(n22),
              "The inner triangle joins the mid-points of the sides, and a vertical line runs from the top vertex to the middle of the base. Count by size:\n\n"
              "- **Smallest pieces:** the top triangle is cut into 2 halves, the inverted centre triangle is cut into 2 halves, plus the 2 bottom-corner triangles — 6.\n"
              "- **Whole top triangle** and **whole inverted triangle** — 2.\n"
              "- **Top half + centre half on each side** (apex, side mid-point, base mid-point) — 2.\n"
              "- **Each half of the big triangle** (split by the vertical line) — 2.\n"
              "- **The big triangle** — 1.\n\n"
              "Total = 6 + 2 + 2 + 2 + 1 = **13**.",
              "Count in size layers and note each layer's left/right symmetry to avoid double counting.",
              'hard', 'counting-figures', 'triangles (mid-point triangle + median)', 75, fig=mk.CF['fig'](segs22)))

# 23 mirror image (text) --------------------------------------------------------------------
q23 = mk.MI['str_q'](PID % 23, 'BJ5KF2', 'mirror',
                     "A vertical mirror on the right reverses the order of the characters (the last one, 2, comes first) and flips each character left-to-right. None of B, J, 5, K, F, 2 is left-right symmetric, so every character appears reversed. Only the option that both reverses the order and flips every character is correct.",
                     "Mirror on the side: order reverses and each character flips sideways; top and bottom stay.",
                     'easy', 'text mirror image', 40)
qs.append(q23)

# 24 paper folding (two folds, off-centre punch) --------------------------------------------
PF = mk.PF
q24, holes24 = PF['fold_q'](PID % 24, [PF['VL'], PF['HT']], [(Fr(7, 2), Fr(5, 2))],
                            "The left half is folded onto the right half, then the top half is folded down; the punch, near the right edge just below the horizontal crease, goes through all four layers. "
                            "Unfold the second fold: the hole is reflected across the horizontal centre line, giving a second hole near the right edge just above the centre line. "
                            "Unfold the first fold: both are reflected across the vertical centre line to the left edge. Result: **4 holes** — a close pair near the middle of the right edge and a close pair near the middle of the left edge, each pair straddling the horizontal centre line.",
                            "Unfold in reverse order; each fold doubles the holes as mirror images across that crease.",
                            'hard', 'two folds, one punch', 70)
assert holes24 == 4
stg24 = PF['stages']([PF['VL'], PF['HT']], [(Fr(7, 2), Fr(5, 2))])
assert stg24[-1] == {(Fr(7, 2), Fr(5, 2)), (Fr(7, 2), Fr(3, 2)), (Fr(1, 2), Fr(5, 2)), (Fr(1, 2), Fr(3, 2))}
qs.append(q24)

# 25 cube net (opposite face) ---------------------------------------------------------------
net25 = {(1, 0): 'P', (0, 1): 'Q', (1, 1): 'R', (2, 1): 'S', (3, 1): 'T', (1, 2): 'U'}
q25 = mk.CB['net_opp_q'](PID % 25, net25, 'R', ['P', 'Q', 'U'],
                         "In a straight strip of four faces (Q, R, S, T), alternate faces are opposite: Q–S and **R–T**. The two faces sticking out (P above R, U below R) are opposite each other. So the face opposite R is **T**.",
                         "Row of four: skip one face to find the opposite.", 'easy', 'cube net (opposite face)', 35)
qs.append(q25)

subtopic_spread(qs)
difficulty_spread(qs, 't1-mock-2', (7, 13, 5))
place_answers(qs, [2, 0, 3, 1, 1, 3, 0, 2, 3, 2, 1, 0, 0, 1, 2, 3, 2, 3, 0, 1, 1, 0, 3, 2, 3])
mk.finish('t1-mock-2', qs, 25)

# =====================================================================================
#                                     T1 MOCK 3
# =====================================================================================
qs = []
PID = 'q-t1-mock-3-reasoning-%d'

# 1 letter analogy (reverse + 1) --------------------------------------------------------
o1 = ['LSPX', 'XPSL', 'LSPY', 'KROW']
k1 = letter_rev_shift_check('MIND', 'EOJN', 'WORK', 'LSPX', o1)
assert k1 == 1
qs.append(C.Q(PID % 1, '**MIND : EOJN :: WORK : ?**', o1, 'LSPX',
              "Write MIND backwards: D N I M. Move each letter +1: E O J N — that is the given code. Do the same with WORK: backwards K R O W, then +1 gives **LSPX**. "
              "(XPSL is WORK + 1 without reversing — the trap.)",
              "Code starts with the letter after the word's LAST letter (D to E): reverse first, then shift.",
              'medium', 'analogy', 'letter analogy (reverse + shift)', 50))

# 2 number analogy (n^2 + n + 1) ---------------------------------------------------------
def check_num_analogy_ext(pairs, probe, correct, options):
    """common.check_num_analogy plus the x^2 + x + k family (not in the stock list)."""
    rules = C._nat_num_rules(pairs)
    for k in range(-10, 11):
        f = (lambda k: lambda x: x * x + x + k)(k)
        if all(f(a) == b for a, b in pairs):
            rules.append(('x^2+x%+d' % k, f))
    assert rules
    hits = {str(f(probe)) for _, f in rules if str(f(probe)) in [str(o) for o in options]}
    assert hits == {str(correct)}, (hits, [(n, f(probe)) for n, f in rules])


check_num_analogy_ext([(7, 57), (9, 91)], 12, 157, [157, 156, 145, 169])
assert all(b == a * a + a + 1 for a, b in [(7, 57), (9, 91), (12, 157)])
qs.append(C.Q(PID % 2, '**7 : 57 :: 9 : 91 :: 12 : ?**', [157, 156, 145, 169], 157,
              "7² + 7 + 1 = 49 + 7 + 1 = 57 and 9² + 9 + 1 = 81 + 9 + 1 = 91. The rule is **n² + n + 1**, so 12² + 12 + 1 = 144 + 13 = **157**.",
              "Second number just above n²: 57 − 49 = 8 = 7 + 1, 91 − 81 = 10 = 9 + 1.",
              'medium', 'analogy', 'number analogy (n² + n + 1)', 50))

# 3 word analogy (branch of medicine : organ) -------------------------------------------------
study = {'Cardiology': 'Heart', 'Nephrology': 'Kidney', 'Hepatology': 'Liver', 'Neurology': 'Nerves', 'Pulmonology': 'Lungs'}
o3 = ['Kidney', 'Liver', 'Nerves', 'Lungs']
assert study['Nephrology'] == 'Kidney' and all(v in study.values() for v in o3)
qs.append(C.Q(PID % 3, '**Cardiology : Heart :: Nephrology : ?**', o3, 'Kidney',
              "Cardiology is the branch of medicine dealing with the heart; **nephrology** deals with the **kidney** (Greek *nephros*). Liver is hepatology, nerves is neurology and lungs is pulmonology.",
              "Branch of medicine : organ it treats.", 'easy', 'analogy', 'word analogy (science-organ)', 30))

# 4 classification (odd pair, n^3 + 1) ---------------------------------------------------------
pairs4 = [(3, 28), (5, 126), (4, 65), (6, 215)]
assert [b == a ** 3 + 1 for a, b in pairs4] == [True, True, True, False] and 6 ** 3 + 1 == 217
o4 = ['6 – 215', '3 – 28', '5 – 126', '4 – 65']
qs.append(C.Q(PID % 4, 'Find the odd number pair: **3 – 28, 5 – 126, 4 – 65, 6 – 215**', o4, '6 – 215',
              "In 3 – 28, 5 – 126 and 4 – 65 the second number is (first)³ **+ 1**: 27 + 1, 125 + 1, 64 + 1. For 6 the rule gives 216 + 1 = 217, but the pair shows 215 (= 6³ − 1). So **6 – 215** is odd.",
              "Recognise cubes 27, 64, 125, 216 and check the sign of the ±1.", 'medium', 'classification', 'odd number pair (n³ + 1)', 45))

# 5 classification (rivers by drainage) ---------------------------------------------------------
drain = {'Ganga': 'Bay of Bengal', 'Godavari': 'Bay of Bengal', 'Krishna': 'Bay of Bengal', 'Narmada': 'Arabian Sea'}
assert Counter(drain.values()) == Counter({'Bay of Bengal': 3, 'Arabian Sea': 1})
qs.append(C.Q(PID % 5, 'Find the odd one out: **Ganga, Godavari, Narmada, Krishna**', ['Narmada', 'Ganga', 'Godavari', 'Krishna'], 'Narmada',
              "Ganga, Godavari and Krishna flow eastward and drain into the **Bay of Bengal**. The **Narmada** flows westward through a rift valley and drains into the **Arabian Sea**, so it is the odd one.",
              "Sort rivers by where they meet the sea: east-flowing vs west-flowing.", 'medium', 'classification', 'word odd-one-out (geography)', 35))

# 6 number series (differences are squares) ------------------------------------------------------
s6 = [1, 2, 6, 15, 31, 56]
assert [b - a for a, b in zip(s6, s6[1:])] == [1, 4, 9, 16, 25] and 56 + 36 == 92
C.check_number_series(s6 + ['?'], [92, 91, 88, 97], 92, must_fit='D3')
qs.append(C.Q(PID % 6, 'Find the next term: **1, 2, 6, 15, 31, 56, ?**', [92, 91, 88, 97], 92,
              "Differences: 2 − 1 = 1, 6 − 2 = 4, 15 − 6 = 9, 31 − 15 = 16, 56 − 31 = 25 — these are 1², 2², 3², 4², 5². The next difference is 6² = 36, so the next term is 56 + 36 = **92**.",
              "When first differences look irregular, test them against squares/cubes.", 'hard', 'series', 'number series (square differences)', 60))

# 7 letter-pair series (opposite pairs, growing gap) -------------------------------------------------
C.check_letter_series(['AZ', 'CX', 'FU', 'JQ', '?'], ['OL', 'OK', 'NL', 'PM'], 'OL')
assert all(C.p(w[0]) + C.p(w[1]) == 27 for w in ['AZ', 'CX', 'FU', 'JQ', 'OL'])
qs.append(C.Q(PID % 7, 'Find the next term: **AZ, CX, FU, JQ, ?**', ['OL', 'OK', 'NL', 'PM'], 'OL',
              "First letters A, C, F, J move +2, +3, +4, so next is +5: J + 5 = **O**. Second letters Z, X, U, Q move −2, −3, −4, so next is −5: Q − 5 = **L**. Answer **OL** (check: O and L are opposite letters, like every pair here).",
              "Each pair is an opposite pair (sum 27): find the first letter, the second is its opposite.",
              'medium', 'series', 'letter-pair series (growing gap)', 50))

# 8 alphanumeric series (growing letter gap, x3 numbers) ----------------------------------------------
terms8 = ['K2', 'M6', 'P18', 'T54']
gaps8 = [C.p(b[0]) - C.p(a[0]) for a, b in zip(terms8, terms8[1:])]
nums8 = [int(t[1:]) for t in terms8]
assert gaps8 == [2, 3, 4] and all(b == 3 * a for a, b in zip(nums8, nums8[1:]))
ans8 = C.L(C.p('T') + 5) + str(54 * 3)
assert ans8 == 'Y162'
o8 = ['Y162', 'Y158', 'X162', 'Z162']
qs.append(C.Q(PID % 8, 'Find the next term: **K2, M6, P18, T54, ?**', o8, ans8,
              "Letters: K to M is +2, M to P is +3, P to T is +4, so next is +5: T (20) + 5 = 25 = **Y**. Numbers: 2, 6, 18, 54 — each is ×3, so next is 54 × 3 = **162**. Next term: **Y162**.",
              "Treat letters and numbers as two separate series.", 'medium', 'series', 'alphanumeric series (mixed rules)', 55))

# 9 coding (word-code language) ---------------------------------------------------------------
sent9 = [('sky is blue', 'ka mo ti'), ('blue ink pen', 'ti re su'), ('pen is red', 'su mo na')]
words9 = sorted({w for s, _ in sent9 for w in s.split()})
codes9 = sorted({c for _, c in sent9 for c in c.split()})
from itertools import permutations
maps9 = []
for perm in permutations(codes9):
    mp = dict(zip(words9, perm))
    if all(sorted(mp[w] for w in s.split()) == sorted(c.split()) for s, c in sent9):
        maps9.append(mp)
assert {mp['sky'] for mp in maps9} == {'ka'}, maps9
qs.append(C.Q(PID % 9, "In a certain code language, **'sky is blue'** is written as **'ka mo ti'**, **'blue ink pen'** is written as **'ti re su'**, and **'pen is red'** is written as **'su mo na'**. What is the code for **'sky'**?",
              ['ka', 'mo', 'ti', 'na'], 'ka',
              "Compare sentences two at a time. 'blue' is common to the 1st and 2nd sentences, and so is 'ti' — blue = ti. 'is' is common to the 1st and 3rd, and so is 'mo' — is = mo. "
              "(Similarly pen = su from the 2nd and 3rd.) In 'sky is blue' = 'ka mo ti', the codes mo and ti are taken, so sky = **ka**.",
              "Common word ↔ common code; the leftover code is the answer.", 'medium', 'coding-decoding', 'word-code language (common words)', 60))

# 10 coding (position-wise increasing shift) ----------------------------------------------------
o10 = ['GKVL', 'GKVM', 'GJVL', 'HKVL']
mk.CD['check_word_code']('LAMP', 'MCPT', 'FISH', 'GKVL', o10)
assert C.diffs('LAMP', 'MCPT') == [1, 2, 3, 4] and C.shv('FISH', [1, 2, 3, 4]) == 'GKVL'
qs.append(C.Q(PID % 10, "In a certain code language, **LAMP** is written as **MCPT**. How will **FISH** be written in that language?", o10, 'GKVL',
              "Compare letter by letter: L to M is +1, A to C is +2, M to P is +3, P to T is +4 — the shift equals the letter's position. "
              "For FISH: F + 1 = G, I + 2 = K, S + 3 = V, H + 4 = L — **GKVL**.",
              "Write the gap under each letter; +1, +2, +3, +4 is a favourite CGL pattern.", 'hard', 'coding-decoding', 'letter coding (increasing shift)', 55))

# 11 mathematical operations (interchange two signs) -----------------------------------------------
nums11, ops11 = [20, 4, 3, 6, 2], ['/', '+', '*', '-']
target11 = 25
assert mk.MO['ev'](nums11, ops11) == 21 != target11
res11 = {}
for a, b in combinations('/+*-', 2):
    sw = [b if o == a else a if o == b else o for o in ops11]
    res11[(a, b)] = mk.MO['ev'](nums11, sw)
hits11 = [k for k, v in res11.items() if v == target11]
assert hits11 == [('/', '-')], res11
o11 = ['÷ and −', '+ and ×', '÷ and ×', '+ and −']
qs.append(C.Q(PID % 11, "Which two signs should be **interchanged** to make the following equation correct?\n\n**20 ÷ 4 + 3 × 6 − 2 = 25**",
              o11, '÷ and −',
              "As written, 20 ÷ 4 + 3 × 6 − 2 = 5 + 18 − 2 = 21, so a swap is needed. Test the options:\n\n"
              "- ÷ and −: 20 − 4 + 3 × 6 ÷ 2 = 20 − 4 + 9 = **25** ✓\n"
              "- + and ×: 20 ÷ 4 × 3 + 6 − 2 = 15 + 4 = 19\n"
              "- ÷ and ×: 20 × 4 + 3 ÷ 6 − 2 = 78.5\n"
              "- + and −: 20 ÷ 4 − 3 × 6 + 2 = −11\n\n"
              "Answer: **÷ and −**.",
              "Try the options one by one with BODMAS; drop any swap that makes a fraction appear.",
              'hard', 'mathematical-operations', 'interchange two signs', 75))

# 12 missing number (a^2 - b^2) -----------------------------------------------------------------
mk.MN['check_missing']([(7, 3, 40), (6, 4, 20)], (8, 5), 39, [39, 40, 52, 89])
qs.append(C.Q(PID % 12, "Find the missing number.\n\n| 7 | 3 | 40 |\n|---|---|---|\n| 6 | 4 | 20 |\n| 8 | 5 | **?** |",
              [39, 40, 52, 89], 39,
              "Row rule: (first)² − (second)². Check: 49 − 9 = 40 and 36 − 16 = 20. So 8² − 5² = 64 − 25 = **39**. "
              "(89 comes from adding the squares; 40 from (a + b) × 4, which fails row 2.)",
              "a² − b² = (a + b)(a − b): 13 × 3 = 39.", 'medium', 'missing-number', 'row grid (difference of squares)', 55))

# 13 blood relations (in-law) ------------------------------------------------------------------
B['reset']()
B['person']('P', 'F')
B['person']('Z', 'M')
B['person']('Q', 'F', parents=('P',), spouse='R')
B['person']('R', 'M', parents=('Z',), spouse='Q')
B['person']('U', 'M', parents=('Z',))
B['person']('S', 'F', parents=('Q', 'R'))
B['person']('T', 'M', parents=('Q', 'R'))
B['check_rel']('Q', 'U', 'brother-in-law', ['brother', 'uncle', 'son-in-law'])
qs.append(C.Q(PID % 13, "**P** is the mother of **Q**. Q is married to **R**. R is the father of **S** and **T**. **U** is the brother of R. How is U related to Q?",
              ['Brother-in-law', 'Brother', 'Uncle', 'Son-in-law'], 'Brother-in-law',
              "R is the father of S and T and is married to Q, so Q is R's wife. U is R's brother, i.e. U is the brother of Q's husband — Q's **brother-in-law**. "
              "(U is the uncle of S and T, not of Q; P and S, T are extra information.)",
              "Husband's brother = brother-in-law; ignore the extra names.", 'medium', 'blood-relations', 'family description (in-law)', 55))

# 14 blood relations (which expression) --------------------------------------------------------
# + father of, - wife of, x brother of, / daughter of.  Goal: R is the maternal uncle of T.
def fam(expr):
    """expr: list like ['R','x','P','-','Q','+','T'] -> (parents dict, gender dict, siblings pairs)"""
    par, gen, sib, wife = {}, {}, [], {}
    for a, op, b in zip(expr[0::2], expr[1::2], expr[2::2]):
        if op == '+':
            gen[a] = 'M'; par.setdefault(b, set()).add(a)
        elif op == '-':
            gen[a] = 'F'; gen[b] = 'M'; wife[b] = a
        elif op == 'x':
            gen[a] = 'M'; sib.append((a, b))
        elif op == '/':
            gen[a] = 'F'; par.setdefault(a, set()).add(b)
    for kid, ps in par.items():           # a father's wife is the child's mother
        for p_ in list(ps):
            if p_ in wife:
                ps.add(wife[p_])
    return par, gen, sib


def maternal_uncle(expr, u, t):
    par, gen, sib = fam(expr)
    mothers = [p_ for p_ in par.get(t, ()) if gen.get(p_) == 'F']
    sibs = {x for pr in sib for x in pr if u in pr} - {u}
    return gen.get(u) == 'M' and any(m in sibs for m in mothers)


exprs14 = {'R × P − Q + T': ['R', 'x', 'P', '-', 'Q', '+', 'T'],
           'R × Q + T': ['R', 'x', 'Q', '+', 'T'],
           'R + P − Q + T': ['R', '+', 'P', '-', 'Q', '+', 'T'],
           'T ÷ P × R': ['T', '/', 'P', 'x', 'R']}
truth14 = {k: maternal_uncle(v, 'R', 'T') for k, v in exprs14.items()}
assert truth14 == {'R × P − Q + T': True, 'R × Q + T': False, 'R + P − Q + T': False, 'T ÷ P × R': False}, truth14
qs.append(C.Q(PID % 14, "**A + B** means A is the father of B; **A − B** means A is the wife of B; **A × B** means A is the brother of B; **A ÷ B** means A is the daughter of B.\n\nWhich of the following expressions means that **R is the maternal uncle of T**?",
              list(exprs14), 'R × P − Q + T',
              "Maternal uncle = brother of T's **mother**. Check each option:\n\n"
              "- **R × P − Q + T:** R is the brother of P, P is the wife of Q, Q is the father of T — so P is T's mother and R is her brother ✓\n"
              "- R × Q + T: R is the brother of T's **father** Q — paternal uncle ✗\n"
              "- R + P − Q + T: R is the **father** of T's mother P — maternal grandfather ✗\n"
              "- T ÷ P × R: T is the daughter of P and P is the brother of R, so P is T's father — R is on the father's side ✗",
              "Work backwards from T: find T's mother first, then look for her brother.",
              'hard', 'blood-relations', 'coded relations (which expression)', 90))

# 15 direction ------------------------------------------------------------------------------
x, y, d = walk('W', [('F', 12), ('R', 5), ('R', 20), ('R', 11)])
assert (x, y) == (8, -6) and math.hypot(x, y) == 10 and dir_name(x, y) == 'South-East'
o15 = ['10 m South-East', '10 m North-East', '14 m South-East', '10 m South-West']
qs.append(C.Q(PID % 15, "**Rohan** walks 12 m towards west, turns right and walks 5 m, turns right again and walks 20 m, and then turns right once more and walks 11 m. How far and in which direction is he from his starting point?",
              o15, '10 m South-East',
              "Start at (0, 0). West 12 m: (−12, 0). Facing west, a right turn faces **north**: 5 m gives (−12, 5). Right again faces **east**: 20 m gives (8, 5). Right again faces **south**: 11 m gives (8, −6). "
              "Distance = √(8² + 6²) = **10 m**; he is east and south of the start, so **South-East**.",
              "Net east 20 − 12 = 8, net south 11 − 5 = 6; 6-8-10 triplet.", 'medium', 'direction-distance', 'grid walk (Pythagoras)', 60))

# 16 order / ranking (minimum number) ---------------------------------------------------------------
tot16 = set()
for N in range(1, 101):
    mona = N - 18 + 1                     # Mona's position from the left
    if N >= 12 and 1 <= mona <= N and mona != 12 and abs(mona - 12) - 1 == 5:
        tot16.add(N)
assert tot16 == {23, 35} and min(tot16) == 23
qs.append(C.Q(PID % 16, "In a row of girls, **Rita** is 12th from the left end and **Mona** is 18th from the right end. There are exactly **5 girls between** them. What is the **minimum** possible number of girls in the row?",
              [23, 35, 24, 29], 23,
              "Two cases.\n\n- **Mona to the right of Rita:** Mona is 12 + 5 + 1 = 18th from the left and 18th from the right, so total = 18 + 18 − 1 = 35.\n"
              "- **Mona to the left of Rita:** Mona is 12 − 5 − 1 = 6th from the left and 18th from the right, so total = 6 + 18 − 1 = 23.\n\n"
              "The minimum is **23**. (35 is the maximum — the usual trap.)",
              "Minimum = overlapping case: (12 + 18) − (5 + 2) = 23.", 'hard', 'order-ranking', 'row with persons between (min case)', 75))

# 17 seating (linear, 7 persons) ----------------------------------------------------------------
def clue17b(pos):
    return (pos['S'] == 2
            and abs(pos['V'] - pos['S']) == 3
            and pos['T'] == pos['V'] + 1
            and pos['Q'] in (0, 6)
            and abs(pos['R'] - pos['S']) != 1
            and abs(pos['U'] - pos['Q']) == 1)


arr17 = mk.SE['one'](mk.SE['lin_sols'](list('PQRSTUV'), clue17b), 'm3-q17')
assert arr17 == ('Q', 'U', 'S', 'P', 'R', 'V', 'T'), arr17
mid17 = arr17[3]
assert mid17 == 'P'
qs.append(C.Q(PID % 17, "Seven persons **P, Q, R, S, T, U and V** sit in a row facing north. **S** sits third from the left end. Exactly two persons sit between **S** and **V**. **T** sits to the immediate right of V. **Q** sits at one of the extreme ends, and **U** is an immediate neighbour of Q. **R** is not an immediate neighbour of S. Who sits exactly in the **middle** of the row?",
              ['P', 'R', 'S', 'U'], mid17,
              "Number the seats 1 to 7 from the left (facing north, right = higher number). S = 3. Two persons between S and V puts V at 6 (seat 0 does not exist). T is immediately right of V: T = 7. "
              "Q is at an end, and seat 7 is taken, so Q = 1 and U (next to Q) = 2. Seats 4 and 5 remain for P and R; R cannot be next to S (seat 3), so R = 5 and P = 4. "
              "Row: Q, U, S, P, R, V, T. The middle seat (4) is **P**.",
              "Fix the definite seat (S), then the chained clue V-T, then the ends.", 'hard', 'seating-arrangement', 'linear row (7 persons)', 90))

# 18 syllogism (three statements, possibility) ----------------------------------------------------
SY['syl'](['cups', 'plates', 'bowls', 'spoons'],
          [SY['SOME']('cups', 'plates'), SY['ALL']('plates', 'bowls'), SY['NO']('bowls', 'spoons')],
          SY['SOMENOT']('cups', 'spoons'), False, SY['ALL']('bowls', 'cups'), True, 'both')
qs.append(C.Q(PID % 18, "**Statements:** Some cups are plates. All plates are bowls. No bowl is a spoon.\n\n**Conclusions:**\nI. Some cups are not spoons.\nII. All bowls being cups is a possibility.\n\nWhich of the conclusions follow(s)?",
              OPT_C, OPT_C[2],
              "The cups that are plates are also bowls, and no bowl is a spoon — so those cups are definitely not spoons: I **follows**. "
              "For II, nothing stops the Cups circle from covering the whole Bowls circle (cups and spoons have no restriction that clashes), so the possibility holds: II **follows**. Answer: **Both**.",
              "Definite chain Some → All → No gives 'Some ... not'; a possibility follows whenever no statement forbids it.",
              'medium', 'syllogism', 'three statements with possibility', 60))

# 19 Venn (best represents: chain) ------------------------------------------------------------------
rel19 = {('Teenagers', 'Students'): 'ov', ('Students', 'Senior citizens'): 'ov', ('Teenagers', 'Senior citizens'): 'dis'}
assert venn_matches('chain', rel19)
for bad in ('overlap3', 'in_overlap', 'overlap_plus_out'):
    assert not venn_matches(bad, rel19), bad
opts19 = [venn_config_svg(k) for k in ('chain', 'overlap3', 'in_overlap', 'overlap_plus_out')]
qs.append(C.Q(PID % 19, "Which of the following diagrams best represents the relationship among **Teenagers, Students and Senior citizens**?",
              opts19, opts19[0],
              "Some teenagers are students and some are not, so Teenagers and Students **overlap**. Some senior citizens are also students (adult learners), so Students and Senior citizens **overlap**. "
              "But no one can be a teenager and a senior citizen at the same time, so those two circles are **separate**. The diagram with three circles in a chain — middle one overlapping both, outer two apart — fits.",
              "Decide each pair separately: overlap, inside, or apart; then match the picture.",
              'medium', 'venn-diagrams', 'best-represents diagram (chain)', 50))

# 20 dictionary order (which comes third) ---------------------------------------------------------
w20 = ['Harbour', 'Harmony', 'Hardware', 'Harvest', 'Harness']
srt20 = sorted(w20, key=str.lower)
assert srt20 == ['Harbour', 'Hardware', 'Harmony', 'Harness', 'Harvest'], srt20
qs.append(C.Q(PID % 20, "When the following words are arranged as in an English dictionary, which word comes **third**?\n\n**Harbour, Harmony, Hardware, Harvest, Harness**",
              ['Harmony', 'Hardware', 'Harness', 'Harvest'], srt20[2],
              "All words start with **Har**; compare the 4th letter: Har**b**our (b), Har**d**ware (d), Har**m**ony (m), Har**n**ess (n), Har**v**est (v). Order: Harbour, Hardware, **Harmony**, Harness, Harvest. Third = **Harmony**.",
              "Common prefix — rank by the first letter that differs.", 'easy', 'dictionary-order', 'dictionary position (common prefix)', 40))

# 21 statement-assumption ---------------------------------------------------------------------------
ans21 = verdict('implicit', 'implicit', OPT_A)
assert ans21 == OPT_A[2]
qs.append(C.Q(PID % 21, "**Statement:** A notice near the lifts of an office building reads: \"In case of fire, use the staircase. Do not use the lifts.\"\n\n**Assumptions:**\nI. Lifts may be unsafe to use during a fire.\nII. Without the notice, some people might try to use the lifts during a fire.\n\nWhich of the assumptions is/are implicit in the statement?",
              OPT_A, ans21,
              "The instruction to avoid lifts only makes sense if lifts may be unsafe in a fire — I is implicit. A notice is put up only when the writer expects that people might otherwise do the wrong thing — II is implicit too. Answer: **Both**.",
              "Ask: 'Why would anyone write this?' — every reason the writer takes for granted is an implicit assumption.",
              'easy', 'statement-conclusion', 'statement and assumptions', 40))

# 22 counting triangles (2 apex lines + 2 cross lines) ------------------------------------------------
segs22 = mk.CF['cev'](2, 2)
n22 = count_triangles(segs22)
assert n22 == 18 == (2 + 1) * (2 + 2) // 2 * (2 + 1), n22
qs.append(C.Q(PID % 22, mk.CF['QT'], ['18', '12', '15', '24'], str(n22),
              "Two lines run from the top vertex to the base, and two lines cut across parallel to the base.\n\n"
              "Lines through the top vertex = 2 sides + 2 inner lines = 4. Any two of them, together with one horizontal line below the vertex, make a triangle: C(4, 2) = 6 triangles for **each** horizontal line. "
              "There are 3 horizontal lines (the base and the two cross lines), so the total is 6 × 3 = **18**. (Counting only the base layer gives 6, and base + one cross line gives 12.)",
              "For k apex lines and h cross lines: (k + 1)(k + 2)/2 × (h + 1) = 6 × 3 = 18.",
              'hard', 'counting-figures', 'triangles (apex lines + parallel line)', 75, fig=mk.CF['fig'](segs22)))

# 23 water image (text) ------------------------------------------------------------------------------
q23 = mk.MI['str_q'](PID % 23, 'RK4BE7', 'water',
                     "In a water image the order of the characters stays the same and each character is flipped **upside down**. K, B and E are top-bottom symmetric, so they look unchanged; R, 4 and 7 appear inverted. The option that keeps the order and inverts every character is correct.",
                     "Water image: same order, each character turned upside down (not left-right).",
                     'easy', 'text water image', 40)
qs.append(q23)

# 24 paper folding (two diagonal folds) ----------------------------------------------------------------
q24, holes24 = PF['fold_q'](PID % 24, [PF['D1'], PF['D2']], [(2, Fr(7, 2))],
                            "The sheet is folded along one diagonal (into a triangle) and then along the other diagonal (into a quarter-triangle); the punch goes through all four layers near the middle of the bottom edge. "
                            "Unfolding the second fold reflects the hole across the second diagonal, giving a hole near the middle of the left edge. Unfolding the first fold reflects both across the first diagonal, giving holes near the middle of the right and top edges. "
                            "Result: **4 holes**, one near the middle of each edge.",
                            "Two diagonal folds = 4 layers; the final pattern is symmetric about both diagonals.",
                            'hard', 'two diagonal folds', 75)
assert holes24 == 4
stg24 = PF['stages']([PF['D1'], PF['D2']], [(2, Fr(7, 2))])
assert stg24[-1] == {(Fr(2), Fr(7, 2)), (Fr(1, 2), Fr(2)), (Fr(7, 2), Fr(2)), (Fr(2), Fr(1, 2))}
qs.append(q24)

# 25 dice (three positions) ------------------------------------------------------------------------------
q25 = mk.CB['views_q'](PID % 25, list('123456'), [('1', '2', '3'), ('1', '5', '2'), ('6', '1', '3')], '1', ['2', '5', '6'],
                       "Collect every number seen **next to 1**: view 1 shows 2 and 3, view 2 shows 5 and 2, view 3 shows 6 and 3. So 2, 3, 5 and 6 are all adjacent to 1. A face has exactly four neighbours, so the only number left, **4**, is opposite 1.",
                       "List the neighbours of the asked face; the missing number is opposite.", 'medium', 'opposite face from three positions', 50)
qs.append(q25)

subtopic_spread(qs)
difficulty_spread(qs, 't1-mock-3', (4, 13, 8))
place_answers(qs, [1, 3, 0, 2, 3, 1, 2, 0, 0, 2, 3, 1, 2, 0, 1, 3, 1, 3, 2, 0, 3, 0, 1, 2, 1])
mk.finish('t1-mock-3', qs, 25)
