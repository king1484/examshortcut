# t1-pyq-2025 reasoning part: 25 questions mirroring the 2025 Tier 1 distribution
# (letter-cluster heavy, essentially no non-verbal)
import mk
import common as C
from engines import walk, dir_name

qs = []
PID = 'q-t1-pyq-2025-reasoning-%d'

# ---- letter-cluster series (5) ------------------------------------------
# 1
C.check_letter_series(['ABD', 'BEG', 'CHJ', 'DKM', '?'], ['ENP', 'EMQ', 'ENQ', 'FMQ'], 'ENP')
qs.append(C.Q(PID % 1, 'Find the next group: **ABD, BEG, CHJ, DKM, ?**',
              ['ENP', 'EMQ', 'ENQ', 'FMQ'], 'ENP',
              "1st letters A, B, C, D move +1, giving **E**. 2nd letters B, E, H, K move +3, giving **N**. 3rd letters D, G, J, M also move +3, giving **P**. Next group **ENP**.",
              "Each position has its own constant step: +1, +3, +3.", 'medium', 'series', 'letter-cluster series (per-slot steps)', 50))

# 2
C.check_letter_series(['ZA', 'YB', 'XC', '?'], ['WD', 'WV', 'VD', 'XD'], 'WD')
qs.append(C.Q(PID % 2, 'Find the next group: **ZA, YB, XC, ?**',
              ['WD', 'WV', 'VD', 'XD'], 'WD',
              "First letters run backwards: Z, Y, X, **W**. Second letters run forwards: A, B, C, **D**. Next group **WD**.",
              "Two counters moving in opposite directions.", 'easy', 'series', 'letter-cluster series (opposite moves)', 40))

# 3
C.check_letter_series(['AZ', 'BY', 'CX', '?'], ['DW', 'DV', 'CW', 'DX'], 'DW')
qs.append(C.Q(PID % 3, 'Find the next group: **AZ, BY, CX, ?**',
              ['DW', 'DV', 'CW', 'DX'], 'DW',
              "First letters move forward: A, B, C, **D**; second letters move backward: Z, Y, X, **W**. Next group **DW**.",
              "First letter +1, second letter −1.", 'easy', 'series', 'letter-cluster series (opposite moves)', 40))

# 4
C.check_letter_series(['BDA', 'CEB', 'DFC', '?'], ['EGD', 'EGC', 'FGE', 'DGC'], 'EGD')
qs.append(C.Q(PID % 4, 'Find the next group: **BDA, CEB, DFC, ?**',
              ['EGD', 'EGC', 'FGE', 'DGC'], 'EGD',
              "Every letter moves +1 across groups: B, C, D give **E**; D, E, F give **G**; A, B, C give **D**. Next group **EGD**.",
              "All three positions advance by +1.", 'easy', 'series', 'letter-cluster series (parallel +1)', 40))

# 5
C.check_letter_series(['ACX', 'BDW', 'CEV', '?'], ['DFU', 'DFV', 'DEU', 'DGU'], 'DFU')
qs.append(C.Q(PID % 5, 'Find the next group: **ACX, BDW, CEV, ?**',
              ['DFU', 'DFV', 'DEU', 'DGU'], 'DFU',
              "1st letters A, B, C go +1 → **D**; 2nd letters C, D, E go +1 → **F**; 3rd letters X, W, V go −1 → **U**. Next group **DFU**.",
              "Two positions forward, one backward.", 'medium', 'series', 'letter-cluster series (mixed moves)', 45))

# ---- word analogy (2) ----------------------------------------------------
# 6
part_of = {'book': 'pages', 'ladder': 'rungs', 'chain': 'links', 'house': 'bricks'}
assert part_of['ladder'] == 'rungs'
qs.append(C.Q(PID % 6, '**Book : Pages :: Ladder : ?**',
              ['Rungs', 'Wood', 'Climbing', 'Steps'], 'Rungs',
              "A book is made up of pages; a ladder is made up of **rungs** (the horizontal steps). Wood is the material and climbing is the action, not the parts.",
              "Whole : its parts.", 'easy', 'analogy', 'word analogy (whole-part)', 35))

# 7
dwelling = {'bird': 'nest', 'bee': 'hive', 'horse': 'stable', 'lion': 'den', 'dog': 'kennel'}
assert dwelling['bee'] == 'hive' and dwelling['bird'] == 'nest'
qs.append(C.Q(PID % 7, '**Bird : Nest :: Bee : ?**',
              ['Hive', 'Honey', 'Swarm', 'Comb'], 'Hive',
              "A bird lives in a nest; a bee lives in a **hive**. Honey is the produce, swarm is the group and comb is only the storage structure inside.",
              "Animal : its dwelling.", 'easy', 'analogy', 'word analogy (animal-dwelling)', 35))

# ---- coding analogy (2) --------------------------------------------------
# 8
C.check_letter_analogy('SHOP', 'UJQR', 'WARM', 'YCTO', ['YCTO', 'YCTP', 'ZDUO', 'YCUN'])
assert [C.dm(x, y) for x, y in zip('SHOP', 'UJQR')] == [2, 2, 2, 2]
qs.append(C.Q(PID % 8, '**SHOP : UJQR :: WARM : ?**',
              ['YCTO', 'YCTP', 'XBSN', 'YCUN'], 'YCTO',
              "Each letter of SHOP moves +2: S to U, H to J, O to Q, P to R. Applying +2 to WARM: W to Y, A to C, R to T, M to O — **YCTO**.",
              "+2 shift on every letter.", 'medium', 'coding-decoding', 'coding analogy (constant shift)', 45))

# 9
mk.CD['check_number_coding']('DUST', 64, 'DISH', 40, [40, 41, 39, 45])
assert C.p('D') + C.p('U') + C.p('S') + C.p('T') == 64
qs.append(C.Q(PID % 9, "If **DUST** is coded as **64**, then **DISH** will be coded as",
              [40, 41, 39, 45], 40,
              "The code is the sum of the letter positions: D(4) + U(21) + S(19) + T(20) = 64. So DISH = 4 + 9 + 19 + 8 = **40**.",
              "Add alphabet values.", 'easy', 'coding-decoding', 'coding analogy (letter-position sum)', 40))

# ---- number / symbol odd-one-out (3) -------------------------------------
# 10
_isp = mk.CL['is_prime']
assert all(_isp(n) for n in (13, 17, 23)) and not _isp(21)
qs.append(C.Q(PID % 10, 'Find the odd one out: **13, 17, 21, 23**',
              [21, 13, 17, 23], 21,
              "13, 17 and 23 are prime numbers; 21 = 3 × 7 is not. Odd one: **21**.",
              "Check divisibility by 3 and 7 first: 21 splits.", 'easy', 'classification', 'number odd-one-out (primes)', 35))

# 11
rule11 = lambda a, b: a * b + 2
fits11 = [(3, 2, 8), (4, 3, 14), (2, 5, 12)]
bad11 = (6, 2, 15)
assert all(rule11(a, b) == c for a, b, c in fits11) and rule11(*bad11[:2]) != bad11[2]
qs.append(C.Q(PID % 11, 'Find the odd equation out:\n\n**(a)** 3 + 2 = 8  **(b)** 4 + 3 = 14  **(c)** 6 + 2 = 15  **(d)** 2 + 5 = 12',
              ['(c)', '(a)', '(b)', '(d)'], '(c)',
              "In (a), (b) and (d) the rule is **a × b + 2**: 3×2+2 = 8, 4×3+2 = 14, 2×5+2 = 12. But (c): 6×2+2 = 14, not 15. Odd one: **(c)**.",
              "Test 'a × b + 2' on each equation.", 'medium', 'classification', 'symbol odd-one-out (hidden rule)', 50))

# 12
_issq = mk.CL['is_sq']
assert all(_issq(n) for n in (144, 196, 256)) and not _issq(210)
qs.append(C.Q(PID % 12, 'Find the odd one out: **144, 196, 210, 256**',
              [210, 144, 196, 256], 210,
              "144 = 12², 196 = 14² and 256 = 16² are perfect squares; 210 is not a square. Odd one: **210**.",
              "Squares around: 12², 14², 16² — 210 falls between 14² and 15² = 225.", 'easy', 'classification', 'number odd-one-out (squares)', 35))

# ---- blood relations (4) -------------------------------------------------
# 13
B = mk.BL
B['reset']()
B['person']('Rita', 'F')
B['person']('RitaMother', 'F')
B['person']('Rita', 'F', parents=('RitaMother',))
B['person']('Man13', 'M', parents=('Rita',))
B['check_rel']('Rita', 'Man13', 'son', ['nephew', 'brother', 'grandson'])
qs.append(C.Q(PID % 13, "Pointing to a man, Rita said, **'His mother is the only daughter of my mother.'** How is the man related to Rita?",
              ['Son', 'Nephew', 'Brother', 'Grandson'], 'Son',
              "The only daughter of Rita's mother is Rita herself. So the man's mother is Rita — the man is Rita's **son**.",
              "'Only daughter of my mother' = the speaker (if the speaker is female).", 'medium', 'blood-relations', 'pointing puzzle (only daughter)', 50))

# 14
B['reset']()
B['person']('P', 'F', spouse='PF14')
B['person']('PF14', 'M', spouse='P')
B['person']('Q', 'M', parents=('P', 'PF14'))
B['person']('R', 'M', parents=('P', 'PF14'))
B['check_rel']('P', 'R', 'son', ['grandson', 'nephew', 'brother'])
qs.append(C.Q(PID % 14, "Read the symbols: **P + Q** means P is the mother of Q; **Q − R** means Q is the brother of R. In the expression **P + Q − R**, how is R related to P?",
              ['Son', 'Grandson', 'Nephew', 'Brother'], 'Son',
              "P is the mother of Q, and Q is the brother of R — siblings share parents, so R is also P's child. R is male, so R is P's **son** (not grandson — only one generation is described).",
              "Siblings share the same parents.", 'medium', 'blood-relations', 'symbol expression (mother, brother)', 55))

# 15
B['reset']()
B['person']('M15', 'M')
B['person']('N15', 'M', parents=('M15', 'W15'))
B['person']('W15', 'F', spouse='M15')
B['person']('P15', 'F', parents=('M15', 'W15'), spouse='L15')
B['person']('L15', 'M', spouse='P15')
B['person']('K15', 'F', parents=('P15', 'L15'))
B['check_rel']('N15', 'K15', 'niece', ['daughter', 'granddaughter', 'sister'])
qs.append(C.Q(PID % 15, "**M** is the father of **N** and **P**. P is married to **L**, and L is the father of **K**. How is K related to N?",
              ['Niece', 'Daughter', 'Granddaughter', 'Sister'], 'Niece',
              "P is N's sister. K is P's daughter, so K is N's **niece**.",
              "Sibling's daughter = niece.", 'medium', 'blood-relations', 'two-generation tree', 45))

# 16
B['reset']()
B['person']('Girl', 'F')
B['person']('Father16', 'M')
B['person']('Mother16', 'F', spouse='Father16')
B['person']('Girl', 'F', parents=('Father16', 'Mother16'))
B['person']('Bro16', 'M', parents=('Father16', 'Mother16'), spouse='BroW')
B['person']('BroW', 'F', spouse='Bro16')
B['person']('Boy16', 'M', parents=('Bro16', 'BroW'))
B['check_rel']('Girl', 'Boy16', 'nephew', ['son', 'brother', 'grandson'])
qs.append(C.Q(PID % 16, "Introducing a boy, a girl said, **'He is the son of my father's only son.'** How is the boy related to the girl?",
              ['Nephew', 'Son', 'Brother', 'Grandson'], 'Nephew',
              "The girl's father's only son is the girl's brother. The boy is that brother's son — the girl's **nephew**.",
              "Father's only son = brother (of the girl).", 'medium', 'blood-relations', 'pointing puzzle (only son)', 50))

# ---- mathematical operations (2) -----------------------------------------
# 17
val17 = mk.MO['ev']([15, 3, 10, 2, 4], ['+', '-', '*', '/'])
assert val17 == 13, val17
assert mk.MO['ev']([15, 3, 10, 2, 4], ['/', '+', '-', '*']) == 7
qs.append(C.Q(PID % 17, "If **÷** means **+**, **+** means **−**, **−** means **×** and **×** means **÷**, then find the value of\n\n**15 ÷ 3 + 10 − 2 × 4**",
              [13, 7, 4, 11], 13,
              "After substitution: 15 + 3 − 10 × 2 ÷ 4. BODMAS: × and ÷ first — 10 × 2 = 20, 20 ÷ 4 = 5. Then 15 + 3 − 5 = **13**. (The original expression without substitution gives 7 — a trap.)",
              "Substitute the signs, then BODMAS.", 'medium', 'mathematical-operations', 'symbol substitution (BODMAS)', 60))

# 18
from itertools import product as _prod
combos18 = [(o1, o2) for o1 in '+-*/' for o2 in '+-*/']
vals18 = {c: mk.MO['ev']([8, 4, 2], list(c)) for c in combos18}
hits18 = [c for c, v in vals18.items() if v == 30]
assert hits18 == [('*', '-')], (hits18, vals18)
qs.append(C.Q(PID % 18, "Which pair of signs, used in order, makes **8 _ 4 _ 2 = 30** correct?",
              ['× and −', '+ and ×', '− and +', '× and +'], '× and −',
              "Test the choices: 8 × 4 − 2 = 32 − 2 = **30**. No other pair of signs gives 30 (8 × 4 + 2 = 34, 8 + 4 × 2 = 16, 8 − 4 + 2 = 6, and so on).",
              "Try × first with each second sign; 32 needs −2.", 'medium', 'mathematical-operations', 'insert the signs', 55))

# ---- seating (1) ---------------------------------------------------------
people19 = list('ABCDEF')


def clue19(pos):
    return (pos['A'] == 1 and pos['B'] in (pos['A'] - 1, pos['A'] + 1)
            and pos['C'] == pos['B'] + 3 and pos['D'] == 5
            and abs(pos['E'] - pos['D']) != 1)


sols19 = mk.SE['lin_sols'](people19, clue19)
arr19 = mk.SE['one'](sols19, 'pyq-q19')
assert arr19 == ('B', 'A', 'E', 'C', 'F', 'D'), arr19
qs.append(C.Q(PID % 19, "Six friends **A, B, C, D, E and F** sit in a row facing north. **A** sits second from the left end, **B** sits adjacent to **A**, **C** sits third to the right of **B**, and **D** sits at the right end. **E** is not an immediate neighbour of **D**. Who sits **second from the right end**?",
              ['F', 'E', 'C', 'A'], 'F',
              "A is at seat 2. B adjacent to A; C = B + 3 forces B to seat 1 (if B were at seat 3, C would need seat 6, which D occupies). So B is at seat 1, C at seat 4, D at seat 6. E cannot touch D, so E takes seat 3, leaving F at seat 5. Row: B, A, E, C, F, D. Second from the right = **F**.",
              "The C = B + 3 clue pins B's side first.", 'hard', 'seating-arrangement', 'linear row (six people)', 70))

# ---- number analogy triads (2) -------------------------------------------
# 20
C.check_num_analogy([(6, 217), (4, 65)], 8, 513, [513, 512, 514, 640])
qs.append(C.Q(PID % 20, '**6 : 217 :: 4 : 65 :: 8 : ?**',
              [513, 512, 514, 640], 513,
              "6³ + 1 = 217 and 4³ + 1 = 65, so the rule is **n³ + 1**. Then 8³ + 1 = 512 + 1 = **513**.",
              "n³ + 1.", 'medium', 'analogy', 'number analogy (cubes + 1)', 45))

# 21
C.check_num_analogy([(7, 50), (5, 26)], 9, 82, [82, 81, 83, 90])
qs.append(C.Q(PID % 21, '**7 : 50 :: 5 : 26 :: 9 : ?**',
              [82, 81, 83, 90], 82,
              "7² + 1 = 50 and 5² + 1 = 26, so the rule is **n² + 1**. Then 9² + 1 = 81 + 1 = **82**.",
              "n² + 1.", 'medium', 'analogy', 'number analogy (squares + 1)', 45))

# ---- syllogism (1) -------------------------------------------------------
terms22 = ['cats', 'dogs', 'animals']
prem22 = [mk.SY['NO']('cats', 'dogs'), mk.SY['ALL']('dogs', 'animals')]
mk.SY['syl'](terms22, prem22,
             (lambda m: bool(m['animals'] & m['cats'])), False,
             (lambda m: not (m['dogs'] & m['cats'])), False, 'onlyII')
qs.append(C.Q(PID % 22, "**Statements:** No cat is a dog. All dogs are animals.\n\n**Conclusions:**\nI. Some animals are cats.\nII. No dog is a cat.\n\nWhich of the conclusions follow(s)?",
              ['Only conclusion II follows', 'Only conclusion I follows', 'Both I and II follow', 'Neither I nor II follows'],
              'Only conclusion II follows',
              "'No cat is a dog' works both ways, so II (**follows**). I is only possible, not certain — cats may sit inside or outside the animals circle, so it **does not follow**. Answer: **Only II**.",
              "Negative premises are symmetric; possibility is not a conclusion.", 'medium', 'syllogism', 'universal negative + universal positive', 50))

# ---- dictionary order (1) ------------------------------------------------
words23 = ['Temple', 'Tenant', 'Tell', 'Ten', 'Temper']
srt23 = sorted(w.lower() for w in words23)
assert srt23 == ['tell', 'temper', 'temple', 'ten', 'tenant'], srt23
qs.append(C.Q(PID % 23, "Arrange as per the dictionary and pick the word that comes **in the middle**:\n\n**Temple, Tenant, Tell, Ten, Temper**",
              ['Ten', 'Tenant', 'Temple', 'Temper'], 'Ten',
              "Dictionary order: **Tell, Temper, Temple, Ten, Tenant**. After 'te', the third letter decides: l < m < n. Among the m-words, Temper < Temple (fourth letter e < l). Among the n-words, Ten < Tenant (a word comes before its own extensions). The middle (third) word is **Ten**.",
              "Sort by the first differing letter, then by length.", 'medium', 'dictionary-order', 'dictionary arrangement', 50))

# ---- direction (1) -------------------------------------------------------
x24, y24, _ = walk('E', [('F', 6), ('L', 8), ('L', 6)])
assert (x24, y24) == (0, 8) and dir_name(x24, y24) == 'North'
qs.append(C.Q(PID % 24, "**Sita** walks 6 km towards east, then turns left and walks 8 km, and then turns left again and walks 6 km. How far and in which direction is she from her starting point?",
              ['8 km North', '10 km North-East', '8 km South', '14 km North'], '8 km North',
              "East 6, left → north 8, left → west 6. The 6 km east and 6 km west cancel, leaving **8 km North**.",
              "Equal opposite legs cancel.", 'easy', 'direction-distance', 'grid walk (cancelling legs)', 40))

# ---- order / ranking (1) -------------------------------------------------
assert mk.OR['other_end'](44, 8) == 37
qs.append(C.Q(PID % 25, "In a class of students, **Mohan ranks 8th from the top** and **37th from the bottom**. How many students are there in the class?",
              [44, 45, 43, 46], 44,
              "Total = top rank + bottom rank − 1 (Mohan is counted twice) = 8 + 37 − 1 = **44**.",
              "Rank from top + rank from bottom − 1.", 'easy', 'order-ranking', 'rank from both ends', 35))

# rebalance the answer key if needed --------------------------------------
from collections import Counter
cnt = Counter(q['answer'] for q in qs)
extra = max(cnt, key=lambda k: cnt[k])
room = min(cnt, key=lambda k: cnt[k])
if cnt[extra] - cnt[room] > 2:
    for qd in qs:
        if qd['answer'] == extra and cnt[extra] - cnt[room] > 2:
            mk.move(qd, room)
            cnt[extra] -= 1
            cnt[room] += 1

mk.finish('t1-pyq-2025', qs, 25)
