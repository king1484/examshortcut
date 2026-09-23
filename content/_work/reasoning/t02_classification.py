# build classification (odd one out) topic
import common as C

def is_prime(n):
    if n < 2:
        return False
    i = 2
    while i * i <= n:
        if n % i == 0:
            return False
        i += 1
    return True

def is_square(n):
    r = int(n ** 0.5)
    return r * r in (n, n + 0 if r * r == n else n) or (r + 1) * (r + 1) == n or r * r == n

def is_sq(n):
    r = int(n ** 0.5)
    return r * r == n

def is_cube(n):
    r = round(n ** (1 / 3))
    return r ** 3 == n or (r + 1) ** 3 == n or (r - 1) ** 3 == n

def steps(cluster):
    return [C.dm(cluster[i], cluster[i + 1]) for i in range(len(cluster) - 1)]

subs = []

subs.append(C.sub(
    'classification-idea', 'The idea of odd one out',
    "Classification gives four/five items that look similar and asks which one **does not belong**. Every question hides a *rule that three options obey and one breaks*. Your whole job is to find that rule fast.\n\nThe rule can sit at any of these levels:\n- **Category** (sparrow, crow, parrot, *bat* — bat is a mammal, the rest are birds)\n- **Function/property** (keyboard, mouse, scanner, *monitor* — monitor is output)\n- **Number property** (17, 23, 29, *33* — 33 is not prime)\n- **Letter structure** (ACE, BDF, GIK, *MOP* — MOP does not keep a constant +2 step)\n- **Relation in a pair** (three creator-creation pairs, one creator-material pair)\n\nStrategy order for CGL: test **number/letter properties first** (they are objective), then **function**, then **category**. If two options look odd, you are at the wrong level — go one level deeper (all squares? then odd vs even squares).",
    tricks=[C.T(
        'Write the majority rule, not the exception',
        "Instead of hunting for the odd item, write the rule the *other three* follow ('three are primes'). Then confirm each of the three obeys it and the remaining one breaks it. This prevents choosing an option that is merely unusual rather than breaking the rule.",
        "**Q.** 21, 35, 49, 63, 56\n\n**Sol.** Majority rule: multiples of 7 (21, 35, 49, 63 ✓). 56 is also a multiple of 7 — so this rule makes nobody odd; go deeper: 21, 35, 49, 63 are all **odd**; 56 is even → **56** is the odd one.",
        "If your first rule makes two items odd, the real rule is one level deeper."),
    ],
    mistakes=[
        "Stopping at the first difference found instead of testing it on ALL options — the difference must separate exactly 1 from the rest.",
        "Assuming the odd item must be the 4th/5th option; CGL shuffles positions freely.",
        "Using loose categories ('all are animals') where a tighter one exists ('all are birds') — always prefer the tightest rule that still groups 3+ options.",
    ]))

subs.append(C.sub(
    'word-classification', 'Word odd one out',
    "Four words from overlapping fields; one breaks the shared category or function. CGL recycles the same pools:\n\n| Pool | Common odd ones |\n|---|---|\n| Animals | bat/mammal among birds, whale among fish, snake among legged reptiles |\n| Computer parts | monitor/speaker (output) among input devices, or vice versa |\n| Geography | sea/ocean (saline) among freshwater bodies |\n| Science | a *symptom* (fever) among diseases, a *unit* that is not base SI |\n| Occupations | an amateur activity among professions |\n\nThe exam expects school-level GK only. If two words look odd at category level, check a **property** level (even/odd, edible/non-edible, living/non-living, input/output).",
    tricks=[C.T(
        'Two-level drill: category, then property',
        "First find the broad category word shared by three. If the fourth also fits that category, switch to a binary property (salt/fresh, input/output, base/derived, male/female) — one of the four will be the only one on the other side.",
        "**Q.** Snake, Crocodile, Lizard, Whale\n\n**Sol.** Category 'reptile' fails to exclude whale (a mammal) cleanly? It does exclude whale — but verify: snake, crocodile, lizard are reptiles, whale is a mammal → **Whale**. If instead the list were Snake, Crocodile, Lizard, Turtle, all four are reptiles, and the property level (venomous/non-venomous) would decide.",
        "Category first; if 2 candidates remain, a binary property splits them."),
    ],
    mistakes=[
        "Choosing by rarity ('turtle is uncommon') instead of a structural difference.",
        "Missing the functional split in device questions — CGL loves input vs output.",
        "Overlooking that a word can belong to two categories (bat: mammal AND flying animal); pick the option where all others share a category that the odd one cannot join.",
    ]))

subs.append(C.sub(
    'number-classification', 'Number odd one out',
    "Three or four numbers share a number-theory property; one breaks it. The property bank, in testing order:\n\n1. **Prime vs composite** (most frequent)\n2. **Perfect square / cube / power**\n3. **Multiples** (of 7, 9, 11, 13...)\n4. **Digit properties** — digit sum 9, digit product, repeating digits\n5. **Parity** (odd/even) — usually the *second* level when all share property 1-3\n6. **Divisibility by 11** (alternate digit sums equal)\n\nTwo-level questions are rising: all four may be squares, but three are squares of *odd* numbers. Always check the survivors for a shared sub-property before answering.",
    formulas=[
        C.F('Divisibility by 11', '|S_{odd} - S_{even}| \\equiv 0 \\pmod{11}', 'S = sums of alternate digits; e.g. 2728: (2+2)-(7+8) = -11 → divisible.'),
        C.F('Perfect square endings', 'n^2 \\in \\{0,1,4,5,6,9\\}', 'A square never ends in 2, 3, 7 or 8 — instant elimination.'),
        C.F('Digit sum 9 rule', '9 \\mid n \\iff S(n) \\equiv 0 \\pmod 9', 'Numbers with digit sum exactly 9: 45, 54, 63, 72, 81.'),
    ],
    tricks=[
        C.T(
            'Last-digit scan for squares',
            "Squares end only in 0, 1, 4, 5, 6, 9. If three numbers are squares, any option ending in 2/3/7/8 is instantly odd — no squaring needed.",
            "**Q.** 144, 324, 576, 500\n\n**Sol.** All end in even digits, but squares must end in 0/1/4/5/6/9 — 500 ends in 0 (possible), so test values: 144 = 12², 324 = 18², 576 = 24², 500 is between 22² = 484 and 23² = 529 → **500** is not a square.",
            "Ending check eliminates; root check confirms — together under 10 seconds."),
        C.T(
            'Prime check by small divisors',
            "To test primality divide by 2, 3, 5, 7 only (for numbers under 121). 33 = 3 × 11, 51 = 3 × 17, 57 = 3 × 19, 91 = 7 × 13 — CGL's favourite fake primes.",
            "**Q.** 17, 51, 41, 43\n\n**Sol.** 17, 41, 43 are prime; 51 = 3 × 17 → **51**.",
            "Memorise the fake-prime list: 33, 51, 57, 91, 119, 133, 143 (11×13)."),
    ],
    mistakes=[
        "Ignoring that 1 is neither prime nor composite; 2 is the only even prime.",
        "Calling 56 odd among multiples of 7 without noticing 56 is also a multiple — check the rule against every option.",
        "Overlooking a two-level structure (odd squares vs even squares) and marking a valid square as the answer for the wrong reason.",
    ]))

subs.append(C.sub(
    'letter-classification', 'Letter-cluster odd one out',
    "Each option is a small letter cluster; three share an internal structure and one breaks it. Read each cluster as **steps between its letters** (A=1...Z=26, wrap around). The structure bank:\n\n1. **Constant step**: ACE (+2), BDF (+2), GIK (+2).\n2. **Mixed constant steps**: ABD (+1, +2).\n3. **Vowel patterns**: clusters with exactly one vowel vs none vs all vowels.\n4. **Opposite pairs**: AZ, BY, CX (positions sum to 27).\n5. **Consecutive runs**: ABC, KLM, STU.\n6. **Pair structures**: pairs where second letter = first + k.\n\nCompute steps for all four options in one pass; the odd cluster's step tuple differs. This converts a 'feel' question into arithmetic.",
    formulas=[
        C.F('Step of a cluster', 's_i = Q(L_{i+1}) - Q(L_i) \\pmod{26}', 'Compute steps for every option; three must match as tuples.'),
        C.F('Opposite-pair sum', 'Q(X) + Q(Y) = 27', 'Letter pairs whose positions add to 27 (AZ, BY, ..., MN).'),
    ],
    tricks=[
        C.T(
            'Step tuples in one line',
            "Under each cluster write its steps: ACE → (2,2), BDF → (2,2), GIK → (2,2), MOP → (2,1). The mismatched tuple is the answer — no naming of vowels needed.",
            "**Q.** ACE, BDF, GIK, MOP\n\n**Sol.** ACE (+2,+2), BDF (+2,+2), GIK (+2,+2), MOP (+2,+1) → **MOP**.",
            "Steps make letter classification as objective as number classification."),
        C.T(
            'Vowel count as tiebreaker',
            "If step tuples coincide or the clusters differ in length, count vowels (A, E, I, O, U). Three clusters with exactly one vowel and one with none (or two) is a complete CGL pattern.",
            "**Q.** BGT, CFD, HLM, APT\n\n**Sol.** Vowel counts: 0, 0, 0, 1 (A) → **APT**. (Steps here don't separate the options cleanly, so the vowel level decides.)",
            "Circle vowels first when clusters look irregular."),
    ],
    mistakes=[
        "Computing steps without wrapping (Y to B is +3, not −23).",
        "Forgetting U is a vowel; 'QST' has no vowel even though Q *looks* vowel-ish next to U.",
        "Reading pairs left-to-right when the structure is right-to-left (ZYX, Wax...); check both directions before concluding.",
    ]))

subs.append(C.sub(
    'pair-classification', 'Pair odd one out',
    "Each option is a **pair** (word:word or number:number). Three pairs share the same relation; one does not. The method is exactly the analogy method — name the majority relation, then test each pair against it:\n\n- Word pairs: worker-workplace, creator-creation, animal-home, instrument-quantity.\n- Number pairs: b = k·a ± r, reversal (27:72), squares (5:25), multiples.\n- Letter pairs: constant shift (AB:DE is +3/+3... test!), opposite letters.\n\nThe trap is a pair with the same *topic* but a different *relation* — 'Painter : Canvas' sits beside creator-creation pairs but is creator-**surface**.",
    tricks=[C.T(
        'Relation sentence, then four ticks',
        "Form the relation sentence from three pairs that clearly agree, then tick/cross all four options. In number pairs, compute k and r for each pair — three will match.",
        "**Q.** 3:9, 7:49, 9:81, 11:132\n\n**Sol.** 3:9, 7:49, 9:81 are n:n². 11² = 121, but the pair says 132 → **11:132**.",
        "One relation sentence + four quick ticks settles pair classification."),
    ],
    mistakes=[
        "Matching topics instead of relations (all four pairs about artists, only three creator-creation).",
        "In number pairs, testing the relation only on the odd-looking pair and not on the other three.",
        "Missing sign: 12:6 and 18:9 are 'half', while 20:10 fits too — but 14:7 + 'half' means 9:3 does not; direction matters.",
    ]))

patterns = [
    C.P('Number odd one out — prime vs composite',
        'very common',
        "Three primes and one composite (or multiples of a hidden number).",
        "Divisibility scan by 2, 3, 5, 7; recall fake primes 33, 51, 57, 91, 143."),
    C.P('Number odd one out — square/cube/multiple',
        'very common',
        "Three perfect squares/cubes (or multiples of k) and one that is not.",
        "Ending-digit check for squares, then root/cube check; for multiples, divide mentally."),
    C.P('Word odd one out — category break',
        'very common',
        "Four nouns from one field; one belongs to a different biological/functional category.",
        "Name the category of the majority; a binary property (input/output, salt/fresh) splits ties."),
    C.P('Letter-cluster odd one out — step mismatch',
        'very common',
        "Three clusters keep a constant or patterned step; one breaks it.",
        "Write step tuples under all four clusters in one pass; the odd tuple is the answer."),
    C.P('Pair odd one out — relation break',
        'common',
        "Four word:number/word:word pairs, three sharing one relation.",
        "Form the majority relation sentence (or k, r for numbers); test each pair."),
    C.P('Two-level number odd one out',
        'common',
        "All four share property 1 (e.g. all squares); three share property 2 (odd squares).",
        "After property 1 matches all four, immediately look for parity/digit-level splits."),
    C.P('Vowel-structure cluster odd one out',
        'common',
        "Clusters differ in vowel count or position rather than steps.",
        "Count vowels A, E, I, O, U in each cluster; 3-vs-1 split decides."),
]

# ---------------------------------------------------------------- solved examples
examples = []
assert is_prime(17) and is_prime(23) and is_prime(29) and not is_prime(33)
examples.append(C.Q(
    'rsn-classification-ex1',
    "Find the odd one out: **17, 23, 29, 33**",
    ['17', '23', '29', '33'],
    '33',
    "17, 23 and 29 are all **prime**. 33 = 3 × 11 is composite → **33** is the odd one.",
    sc="Fake primes to memorise: 33 (3×11), 51 (3×17), 57 (3×19), 91 (7×13), 143 (11×13).",
    d='easy', sub='number-classification', pat='number odd one out — prime vs composite', t=30))

assert [is_sq(x) for x in (121, 225, 289, 196)] == [True] * 4
assert 196 % 2 == 0 and all(x % 2 == 1 for x in (121, 225, 289))
examples.append(C.Q(
    'rsn-classification-ex2',
    "Find the odd one out: **121, 225, 289, 196**",
    ['121', '225', '289', '196'],
    '196',
    "All four are perfect squares (11², 15², 17², 14²) — so the square rule is level one. Level two: 121, 225, 289 are squares of **odd** numbers; 196 = 14² is the square of an even number → **196**.",
    sc="When every option passes property 1, drop to parity of the root — odd vs even square.",
    d='medium', sub='number-classification', pat='two-level number odd one out', t=40))

assert [steps(x) for x in ('ACE', 'BDF', 'GIK')] == [[2, 2]] * 3 and steps('MOP') == [2, 1]
examples.append(C.Q(
    'rsn-classification-ex3',
    "Find the odd one out: **ACE, BDF, GIK, MOP**",
    ['ACE', 'BDF', 'GIK', 'MOP'],
    'MOP',
    "Step tuples: ACE (+2, +2), BDF (+2, +2), GIK (+2, +2), MOP (+2, **+1**) → **MOP** breaks the constant +2 step.",
    sc="Write the step tuple under each cluster; three identical tuples expose the fourth instantly.",
    d='medium', sub='letter-classification', pat='letter-cluster odd one out — step mismatch', t=35))

examples.append(C.Q(
    'rsn-classification-ex4',
    "Find the odd one out: **Keyboard, Mouse, Scanner, Monitor**",
    ['Keyboard', 'Mouse', 'Scanner', 'Monitor'],
    'Monitor',
    "Keyboard, mouse and scanner are **input** devices; a monitor is an **output** device → **Monitor**.",
    sc="Device lists in CGL split input/output almost every time — classify direction first.",
    d='easy', sub='word-classification', pat='word odd one out — category break', t=25))

# ---------------------------------------------------------------- practice
pr = []

# 1 number prime
assert is_prime(41) and is_prime(53) and is_prime(59) and not is_prime(51)
pr.append(C.Q('rsn-classification-1',
              "Find the odd one out: **41, 51, 53, 59**",
              ['41', '51', '53', '59'],
              '51',
              "41, 53, 59 are prime; **51 = 3 × 17** is composite.",
              sc="51 is a stock fake prime (3 × 17); divide by 3 when in doubt.",
              d='easy', sub='number-classification', pat='number odd one out — prime vs composite', t=30))

# 2 number cubes
assert is_cube(8) and is_cube(27) and is_cube(64) and not is_cube(100)
pr.append(C.Q('rsn-classification-2',
              "Find the odd one out: **8, 27, 64, 100**",
              ['8', '27', '64', '100'],
              '100',
              "8 = 2³, 27 = 3³, 64 = 4³ are cubes; 100 lies between 4³ = 64 and 5³ = 125, and is not a cube → **100**.",
              sc="Cube roots to 10 by heart; check the gap between neighbouring cubes.",
              d='easy', sub='number-classification', pat='number odd one out — square/cube/multiple', t=30))

# 3 multiple of 7
assert all(x % 7 == 0 for x in (35, 56, 63)) and 72 % 7 != 0
pr.append(C.Q('rsn-classification-3',
              "Find the odd one out: **35, 56, 63, 72**",
              ['35', '56', '63', '72'],
              '72',
              "35 = 5 × 7, 56 = 8 × 7, 63 = 9 × 7 — all multiples of 7. 72 = 8 × 9 is not → **72**.",
              sc="Scan for the divisibility rule the three 'look-alike' numbers share.",
              d='easy', sub='number-classification', pat='number odd one out — square/cube/multiple', t=30))

# 4 digit sum 9
assert sum(int(c) for c in '45') == 9 and sum(int(c) for c in '63') == 9 and sum(int(c) for c in '81') == 9 and sum(int(c) for c in '92') == 11
pr.append(C.Q('rsn-classification-4',
              "Find the odd one out: **45, 63, 81, 92**",
              ['45', '63', '81', '92'],
              '92',
              "Digit sums: 45 → 9, 63 → 9, 81 → 9, but 92 → 11. Three numbers have digit sum 9 (are multiples of 9); **92** does not.",
              sc="Two-digit multiples of 9: 18, 27, 36, 45, 54, 63, 72, 81, 90, 99 — spot them by digit sum.",
              d='easy', sub='number-classification', pat='number odd one out — square/cube/multiple', t=30))

# 5 odd squares (two-level)
assert is_sq(25) and is_sq(49) and is_sq(81) and is_sq(64)
assert all(x % 2 == 1 for x in (25, 49, 81)) and 64 % 2 == 0
pr.append(C.Q('rsn-classification-5',
              "Find the odd one out: **25, 49, 64, 81**",
              ['25', '49', '64', '81'],
              '64',
              "All are squares (5², 7², 8², 9²). 25, 49, 81 are squares of odd numbers; **64 = 8²** is the square of an even number → odd one out.",
              sc="Level 1 squares, level 2 parity of roots — the standard two-level climb.",
              d='medium', sub='number-classification', pat='two-level number odd one out', t=35))

# 6 number: divisible by 11
def d11(n):
    ds = [int(c) for c in str(n)]
    return abs(sum(ds[::2]) - sum(ds[1::2])) % 11 == 0
assert d11(2728) and d11(4917) and d11(6061) and not d11(3456)
pr.append(C.Q('rsn-classification-6',
              "Find the odd one out: **2728, 4917, 6061, 3456**",
              ['2728', '4917', '6061', '3456'],
              '3456',
              "Alternate-sum test for 11: 2728 → (2+2) − (7+8) = −11 ✓; 4917 → (4+1) − (9+7) = −11 ✓; 6061 → (6+6) − (0+1) = 11 ✓; 3456 → (3+5) − (4+6) = −2 ✗ → **3456**.",
              sc="Divisibility by 11: difference of alternate digit sums must be 0 or ±11.",
              d='medium', sub='number-classification', pat='number odd one out — square/cube/multiple', t=45))

# 7 word animals
pr.append(C.Q('rsn-classification-7',
              "Find the odd one out: **Sparrow, Crow, Parrot, Bat**",
              ['Sparrow', 'Crow', 'Parrot', 'Bat'],
              'Bat',
              "Sparrow, crow and parrot are **birds**; a bat is a **mammal** (it suckles its young; its wings are skin folds, not feathers) → **Bat**.",
              sc="'Flies' is the decoy level — classify by reproduction/body cover, not by flight.",
              d='easy', sub='word-classification', pat='word odd one out — category break', t=25))

# 8 word computer
pr.append(C.Q('rsn-classification-8',
              "Find the odd one out: **Printer, Speaker, Plotter, Router**",
              ['Printer', 'Speaker', 'Plotter', 'Router'],
              'Router',
              "Printer, speaker and plotter are **output** devices; a router is a **networking** device that forwards data packets → **Router**.",
              sc="CGL device pools now include network gear — classify by function, not by 'attached to computer'.",
              d='medium', sub='word-classification', pat='word odd one out — category break', t=30))

# 9 word geography
pr.append(C.Q('rsn-classification-9',
              "Find the odd one out: **River, Pond, Lake, Sea**",
              ['River', 'Pond', 'Lake', 'Sea'],
              'Sea',
              "River, pond and lake are **freshwater** bodies; the sea is **saline** → **Sea**.",
              sc="Water bodies split on salinity first, then on flow (flowing vs still).",
              d='easy', sub='word-classification', pat='word odd one out — category break', t=25))

# 10 word science
pr.append(C.Q('rsn-classification-10',
              "Find the odd one out: **Malaria, Typhoid, Cholera, Fever**",
              ['Malaria', 'Typhoid', 'Cholera', 'Fever'],
              'Fever',
              "Malaria, typhoid and cholera are **diseases** with specific causes (parasite, bacteria, bacteria); fever is a **symptom**, not a disease → **Fever**.",
              sc="Science lists often hide one abstract term among concrete ones — check 'is it a thing or a sign of a thing'.",
              d='easy', sub='word-classification', pat='word odd one out — category break', t=25))

# 11 letter step mismatch
assert steps('BDF') == [2, 2] and steps('HJL') == [2, 2] and steps('NPR') == [2, 2] and steps('STV') == [1, 2]
pr.append(C.Q('rsn-classification-11',
              "Find the odd one out: **BDF, HJL, NPR, STV**",
              ['BDF', 'HJL', 'NPR', 'STV'],
              'STV',
              "Steps: BDF (+2, +2), HJL (+2, +2), NPR (+2, +2), STV (+1, +2) → **STV** breaks the pattern.",
              sc="Step tuples settle cluster odd-one-out in one written line.",
              d='medium', sub='letter-classification', pat='letter-cluster odd one out — step mismatch', t=35))

# 12 letter consecutive
assert steps('ABC') == [1, 1] and steps('KLM') == [1, 1] and steps('RST') == [1, 1] and steps('DEF') == [1, 1] and steps('XZB') == [2, 2]
pr.append(C.Q('rsn-classification-12',
              "Find the odd one out: **ABC, KLM, RST, XZB**",
              ['ABC', 'KLM', 'RST', 'XZB'],
              'XZB',
              "ABC, KLM, RST are three **consecutive** letters (+1, +1). XZB steps (+2, +2) — skipped letters → **XZB**.",
              sc="Runs of consecutive letters are spotted by eye; confirm one option with steps.",
              d='easy', sub='letter-classification', pat='vowel-structure cluster odd one out', t=30))

# 13 letter vowel
vowels = set('AEIOU')
opts13 = ['BCD', 'FGH', 'JKL', 'AEI']
counts13 = [sum(1 for ch in o if ch in vowels) for o in opts13]
assert counts13 == [0, 0, 0, 3]
pr.append(C.Q('rsn-classification-13',
              "Find the odd one out: **BCD, FGH, JLM, AEI**",
              opts13,
              'AEI',
              "BCD, FGH, JKL contain **no vowel**; AEI is made only of vowels → **AEI**.",
              sc="When steps look messy, count vowels — the A-E-I-O-U split is a favourite.",
              d='easy', sub='letter-classification', pat='vowel-structure cluster odd one out', t=30))

# 14 letter opposite pairs
def s27(pair):
    return C.p(pair[0]) + C.p(pair[1])
pairs14 = ['AZ', 'BY', 'CX', 'GT']
assert [s27(x) for x in pairs14[:3]] == [27, 27, 27] and s27('GT') == 27
# GT also sums to 27! Need a non-27 pair:
pairs14 = ['AZ', 'BY', 'CX', 'DW']
assert [s27(x) for x in pairs14[:3]] == [27] * 3 and s27('DW') == 27  # DW is also 27!
pairs14 = ['AZ', 'BY', 'CX', 'EV']
assert s27('EV') == 27  # also 27... most natural pairs sum to 27; use a 26 pair
pairs14 = ['AZ', 'BY', 'CX', 'FS']
assert s27('FS') == 6 + 19 == 25
pr.append(C.Q('rsn-classification-14',
              "Find the odd one out: **AZ, BY, CX, FS**",
              pairs14,
              'FS',
              "Position sums: A(1)+Z(26) = 27, B(2)+Y(25) = 27, C(3)+X(24) = 27 — opposite-letter pairs. F(6)+S(19) = **25** ≠ 27 → **FS**.",
              sc="Letter-pair odd one out: compute position sums; opposite pairs always total 27.",
              d='medium', sub='letter-classification', pat='letter-cluster odd one out — step mismatch', t=40))

# 15 pair odd one out (creator-creation)
pr.append(C.Q('rsn-classification-15',
              "Find the odd pair out: **Author : Book, Poet : Poem, Sculptor : Statue, Painter : Canvas**",
              ['Author : Book', 'Poet : Poem', 'Sculptor : Statue', 'Painter : Canvas'],
              'Painter : Canvas',
              "Author-book, poet-poem and sculptor-statue are **creator-creation** pairs. A canvas is the painter's **surface**, not his creation — the painting is → **Painter : Canvas**.",
              sc="Pair lists: write the majority relation once, then tick/cross each pair against it.",
              d='medium', sub='pair-classification', pat='pair odd one out — relation break', t=35))

topic_obj = C.topic(
    'classification', 'Classification (Odd One Out)', 'high', {'tier1': 3, 'tier2': 4},
    "Classification questions list four or five similar items and ask which one does not belong. The hidden rule — a shared category, number property or letter structure — must hold for every option except one. CGL asks 2-4 per shift, drawn from number properties, letter clusters, word categories and pairs.",
    subs, patterns, examples, pr)

C.write_topic(topic_obj)
print('OK classification')
