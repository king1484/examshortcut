# build venn-diagrams topic (topic 12)
from itertools import product
import common as C

# ---- relation checker (SSC convention: subset iff necessary, disjoint iff
# impossible, otherwise draw overlapping circles) ----
N_IND = 4


def rel_models(terms, defs):
    for bits in product([0, 1], repeat=N_IND * len(terms)):
        m = {}
        for ti, t in enumerate(terms):
            m[t] = frozenset(j for j in range(N_IND) if bits[j * len(terms) + ti])
        if all(m[t] for t in terms) and all(p(m) for p in defs):
            yield m


def ent(terms, defs, fn):
    return all(fn(m) for m in rel_models(terms, defs))


def poss(terms, defs, fn):
    return any(fn(m) for m in rel_models(terms, defs))


def check_rel(terms, defs, x, y, expect):
    """expect in subset/disjoint/overlap per SSC drawing convention."""
    subset = ent(terms, defs, lambda m, x=x, y=y: m[x] <= m[y])
    meet = poss(terms, defs, lambda m, x=x, y=y: bool(m[x] & m[y]))
    got = 'subset' if subset else ('disjoint' if not meet else 'overlap')
    assert got == expect, (x, y, expect, got)
    return got


subs = []

subs.append(C.sub(
    'venn-idea', 'What a Venn diagram encodes',
    "A Venn diagram is a picture of set membership: every point inside a circle belongs to that category; overlap regions belong to both. Two habits solve most CGL venn questions:\n\n1. **Region bookkeeping.** Name the 4 regions of a two-circle diagram (only A, only B, both, neither) and the 8 regions of a three-circle one. Every question is a sum or difference of named regions.\n2. **Relation reading.** 'Choose the right diagram for X, Y, Z' asks about *definitional* relations: is one category ALWAYS inside another (nested circles)? Can they NEVER meet (separate circles)? Otherwise (overlap possible but not forced) draw intersecting circles.\n\nDraw the regions and label them with the given numbers before computing — unlabelled diagrams cause double-counting errors.",
    formulas=[
        C.F('Two-set inclusion-exclusion', '|A \\cup B| = |A| + |B| - |A \\cap B|',
            'The intersection is counted twice on the right, so subtract once.'),
        C.F('Only-regions', '|A \\setminus B| = |A| - |A \\cap B|',
            "'Only A' is A minus the overlap."),
    ],
    tricks=[
        C.T(
            'Label regions, don’t imagine them',
            "Write the numbers INTO the regions: |A∩B| in the lens, only-A and only-B in the moons, neither outside. Sums become single looks instead of formula recalls.",
            "**Q.** 60 students; 35 like tea, 30 coffee, 10 both. How many like neither?\n\n**Sol.** Tea-only 25 + both 10 + coffee-only 20 = 55 inside; 60 − 55 = **5**.",
            "Fill the diagram first; the answer is whatever region is left empty times its count."),
    ],
    mistakes=[
        "Counting the intersection twice when totalling.",
        "Treating 'like tea' (including both) as 'like only tea'.",
        "Forgetting the 'neither' region sits outside both circles.",
    ]))

subs.append(C.sub(
    'two-set-operations', 'Two-circle counting',
    "With two sets there are exactly four regions: only A, only B, both, neither. Every two-circle question is a sum or difference of these:\n\n- **Union** (at least one) = only A + only B + both.\n- **Only A** = |A| − both; **Only B** = |B| − both.\n- **Neither** = grand total − union.\n\nExam data typically gives |A|, |B| and the overlap (or hides one of them behind the union). Rearranging the inclusion-exclusion identity recovers any missing region in one step.",
    formulas=[
        C.F('Two-set inclusion-exclusion', '|A \\cup B| = |A| + |B| - |A \\cap B|',
            'The intersection is counted twice on the right, so subtract once.'),
        C.F('Only-regions', '|A \\setminus B| = |A| - |A \\cap B|',
            "'Only A' is A minus the overlap."),
        C.F('Neither', '\\text{neither} = \\text{total} - |A \\cup B|',
            'Everyone outside both circles.'),
    ],
    tricks=[
        C.T(
            'Label regions, don’t imagine them',
            "Write the numbers INTO the regions: the lens, the two moons, and outside. Sums become single looks instead of formula recalls.",
            "**Q.** 60 students; 35 like tea, 30 coffee, 10 both. How many like neither?\n\n**Sol.** Tea-only 25 + both 10 + coffee-only 20 = 55 inside; 60 − 55 = **5**.",
            "Fill the diagram first; the answer is whatever region is left, counted."),
    ],
    mistakes=[
        "Counting the intersection twice when totalling.",
        "Treating 'like tea' (including both) as 'like only tea'.",
        "Forgetting the 'neither' region sits outside both circles.",
    ]))

subs.append(C.sub(
    'three-set-operations', 'Three-circle counting',
    "With three sets A, B, C the master formula is\n\n|A∪B∪C| = |A| + |B| + |C| − |A∩B| − |B∩C| − |A∩C| + |A∩B∩C|.\n\nTwo derived region-counts appear constantly:\n\n- **Exactly two** = (|A∩B| − all3) + (|B∩C| − all3) + (|A∩C| − all3): each pairwise figure includes the triple region, which must be stripped from both pairs it contaminates.\n- **Exactly one** = union − exactly-two − all-three.\n\nExam data usually gives the seven numbers directly (three singles, three pairs, one triple); plug them into the 8 regions and add or subtract as asked.",
    formulas=[
        C.F('Three-set union', '|A \\cup B \\cup C| = \\sum|A| - \\sum|A \\cap B| + |A \\cap B \\cap C|',
            'Add singles, subtract pairs, re-add the triple.'),
        C.F('Exactly two sets', '\\sum (|A \\cap B|) - 3|A \\cap B \\cap C|',
            'Sum of the three pairwise figures minus three times the triple.'),
        C.F('Exactly one set', '|A \\cup B \\cup C| - \\text{exactly two} - \\text{all three}',
            'Strip the multi-set members from the union.'),
    ],
    tricks=[
        C.T(
            'Triple-strip subtraction',
            "Whenever a question says 'exactly two', your reflex is: pairwise sums overcount the core by 3. Compute pairwise sums, subtract 3×(all three), done.",
            "**Q.** |A∩B| = 8, |B∩C| = 7, |A∩C| = 6, all three = 3.\n\n**Sol.** Exactly two = (8+7+6) − 3×3 = **12**.",
            "'Exactly' always means: subtract every richer region, as many times as it was counted."),
    ],
    mistakes=[
        "Using pairwise figures as 'exactly two' without stripping the triple region.",
        "Sign slips on the +all-three term in the union formula.",
        "Adding 'neither/none' into the union before subtracting from the grand total.",
    ]))

subs.append(C.sub(
    'relation-diagrams', 'Choosing the correct diagram',
    "For 'Which diagram represents Doctors, Men, Writers?' style questions, decide each pair with two tests:\n\n1. **Necessity test** — is every X definitionally a Y? (Every mother is a female.) → circle of X drawn **inside** Y.\n2. **Impossibility test** — can X and Y never share a member? (A square and a triangle.) → **separate** circles.\n3. Otherwise — overlap possible but neither forced (doctors and writers) → **intersecting** circles.\n\nSame-type categories usually intersect; category-of-category pairs (squares/rectangles/polygons) nest; mutually exclusive definitions separate.",
    tricks=[
        C.T(
            'Test one pair at a time',
            "Never judge the whole picture at once. Run necessity/impossibility on each pair; the correct option is the only one agreeing on every pair.",
            "**Q.** Mothers, Females, Engineers.\n\n**Sol.** Mothers ⊂ Females (necessity). Engineers ∩ Females possible (female engineers) and Engineers ⊄ Females (male engineers) → intersecting. Match the option reflecting both facts.",
            "One wrong pair eliminates an option — work pair by pair until one option survives."),
    ],
    mistakes=[
        "Drawing engineers inside females because most examples in mind are female.",
        "Making mutually-overlappable categories fully separate.",
        "Missing a third category's relation to the nested pair.",
    ]))

patterns = [
    C.P('Two-set region count', 'very common',
        "Two circles, find neither / only-one / union.",
        "Inclusion-exclusion or direct region sums."),
    C.P('Three-set union / none', 'very common',
        "Seven region numbers, find union or none.",
        "Full inclusion-exclusion with the +triple correction."),
    C.P('Exactly two / exactly one', 'common',
        "'Members in exactly two activities' style.",
        "Pairwise sums − 3×triple for exactly two."),
    C.P('Reverse region puzzle', 'occasional',
        "Union and two regions given; find the intersection.",
        "Rearrange |A∪B| = |A| + |B| − x for the unknown region."),
    C.P('Percentage-based sets', 'common',
        "70% play X, 60% Y, 40% both…",
        "Same formulas on percentages; neither = 100 − union%."),
    C.P('Choose-the-diagram', 'very common',
        "Three categories; pick the correct circle arrangement.",
        "Per-pair necessity/impossibility tests; eliminate options pair-wise."),
]

examples = []

# ex1 (two-set)
v1 = 60 - (35 + 30 - 10)
assert v1 == 5
examples.append(C.Q(
    'rsn-venn-ex1',
    "In a class of **60 students, 35 like tea, 30 like coffee and 10 like both.** How many students like **neither** tea nor coffee?",
    ['5', '15', '25', '0'], '5',
    "Inside the circles: 35 + 30 − 10 = 55. Neither = 60 − 55 = **5**.",
    sc="Add both counts, subtract the overlap once, subtract from the total.",
    d='easy', sub='two-set-operations', pat='two-set region count', t=35))

# ex2 (exactly two)
assert (8 + 7 + 6) - 3 * 3 == 12
examples.append(C.Q(
    'rsn-venn-ex2',
    "In a survey, **8 people read A and B, 7 read B and C, 6 read A and C, and 3 read all three.** How many read **exactly two** papers?",
    ['12', '21', '9', '15'], '12',
    "(8 − 3) + (7 − 3) + (6 − 3) = **12**. Each pairwise figure wrongly includes the triple readers.",
    sc="Pairwise sum minus 3 × triple.",
    d='medium', sub='three-set-operations', pat='exactly two / exactly one', t=45))

# ex3 (relation)
check_rel(['doctors', 'men', 'writers'], [], 'doctors', 'men', 'overlap')
check_rel(['doctors', 'men', 'writers'], [], 'doctors', 'writers', 'overlap')
check_rel(['doctors', 'men', 'writers'], [], 'men', 'writers', 'overlap')
examples.append(C.Q(
    'rsn-venn-ex3',
    "Which diagram correctly represents **Doctors, Men and Writers**?",
    ['Three circles, each pair intersecting',
     'Doctors inside Men; Writers a separate circle',
     'Three completely separate circles',
     'Doctors and Writers both inside the Men circle'],
    'Three circles, each pair intersecting',
    "No category is definitionally inside another (a doctor need not be a man; men need not write), and none is impossible to combine. So all three circles pairwise intersect.",
    sc="Run necessity (nesting) and impossibility (separation) tests pair by pair; neither applies here.",
    d='easy', sub='relation-diagrams', pat='choose-the-diagram', t=40))

# ex4 (3-set none)
u = 90 + 80 + 70 - 40 - 35 - 30 + 15
assert u == 150 and 200 - u == 50
examples.append(C.Q(
    'rsn-venn-ex4',
    "Of **200 people, 90 drink coffee, 80 tea, 70 milk; 40 coffee and tea, 35 tea and milk, 30 coffee and milk; 15 all three.** How many drink **none**?",
    ['50', '30', '20', '60'], '50',
    "Union = 90+80+70−40−35−30+15 = 150. None = 200 − 150 = **50**.",
    sc="Add singles, subtract pairs, re-add triple, subtract from total.",
    d='medium', sub='three-set-operations', pat='three-set union / none', t=55))

# ---------------------------------------------------------------- practice
pr = []

# 1 (reverse: intersection from union and regions)
assert 40 - 15 - 12 == 13
pr.append(C.Q(
    'rsn-venn-1',
    "In a group, **|A ∪ B| = 40**, the number of elements in **A only is 15** and in **B only is 12**. How many elements are in **both A and B**?",
    ['13', '15', '12', '28'], '13',
    "Union = only-A + only-B + both → 40 = 15 + 12 + both → both = **13**.",
    sc="The three inside-regions sum to the union.",
    d='easy', sub='two-set-operations', pat='reverse region puzzle', t=35))

# 2 (union of hockey/cricket)
assert 40 + 25 - 12 == 53
pr.append(C.Q(
    'rsn-venn-2',
    "In a school, **40 students play hockey, 25 play cricket and 12 play both.** How many students play **hockey or cricket** (at least one)?",
    ['53', '65', '77', '41'], '53',
    "40 + 25 − 12 = **53**.",
    sc="Singles minus overlap.",
    d='easy', sub='two-set-operations', pat='two-set region count', t=30))

# 3 (percentages)
assert 100 - (70 + 60 - 40) == 10
pr.append(C.Q(
    'rsn-venn-3',
    "In a survey, **70% of people watch cricket, 60% watch football and 40% watch both.** What percentage watch **neither**?",
    ['10%', '30%', '0%', '20%'], '10%',
    "Union = 70 + 60 − 40 = 90%. Neither = 100 − 90 = **10%**.",
    sc="Percentages behave exactly like counts — total is 100.",
    d='easy', sub='two-set-operations', pat='percentage-based sets', t=35))

# 4 (everybody plays)
assert 50 + 40 - 80 == 10
pr.append(C.Q(
    'rsn-venn-4',
    "In a class of **80 students, every student plays at least one of chess and carrom. 50 play chess and 40 play carrom.** How many play **both**?",
    ['10', '20', '30', '12'], '10',
    "At least one = 80 → 50 + 40 − both = 80 → both = **10**.",
    sc="'Everyone plays' pins the union equal to the class strength.",
    d='easy', sub='two-set-operations', pat='two-set region count', t=35))

# 5 (three-set union)
u3 = 30 + 25 + 20 - 8 - 7 - 6 + 3
assert u3 == 57
pr.append(C.Q(
    'rsn-venn-5',
    "Three sets satisfy **|A| = 30, |B| = 25, |C| = 20, |A∩B| = 8, |B∩C| = 7, |A∩C| = 6, |A∩B∩C| = 3.** Find **|A ∪ B ∪ C|**.",
    ['57', '54', '60', '51'], '57',
    "30 + 25 + 20 − 8 − 7 − 6 + 3 = **57**.",
    sc="Sum, subtract pairs, re-add the triple.",
    d='medium', sub='three-set-operations', pat='three-set union / none', t=45))

# 6 (only A)
assert 45 - 25 == 20
pr.append(C.Q(
    'rsn-venn-6',
    "In a colony of newspaper readers, **45 people read the Herald, 25 read both the Herald and the Tribune.** How many read **only the Herald**?",
    ['20', '25', '70', '45'], '20',
    "Only Herald = 45 − 25 = **20**.",
    sc="'Only X' = X minus the overlap.",
    d='easy', sub='two-set-operations', pat='two-set region count', t=25))

# 7 (total from regions)
assert 15 + 10 + 8 + 6 + 5 + 4 + 2 == 50
pr.append(C.Q(
    'rsn-venn-7',
    "A club's three sports sections show: **15 members in badminton only, 10 in tennis only, 8 in chess only, 6 in badminton and tennis only, 5 in tennis and chess only, 4 in badminton and chess only, and 2 in all three.** How many members play **at least one** of the three sports?",
    ['50', '48', '52', '45'], '50',
    "The seven regions are disjoint — add them: 15+10+8+6+5+4+2 = **50**.",
    sc="When every region is given 'only'-style, no formula — just add.",
    d='easy', sub='three-set-operations', pat='three-set union / none', t=40))

# 8 (exactly one)
exactly_two = (9 - 4) + (7 - 4) + (6 - 4)
union = 22 + 19 + 17 - 9 - 7 - 6 + 4
assert exactly_two == 10 and union == 40 and union - exactly_two - 4 == 26
pr.append(C.Q(
    'rsn-venn-8',
    "Given **|A| = 22, |B| = 19, |C| = 17, |A∩B| = 9, |B∩C| = 7, |A∩C| = 6, |A∩B∩C| = 4** — how many elements belong to **exactly one** set?",
    ['26', '24', '30', '20'], '26',
    "Exactly two = (9−4)+(7−4)+(6−4) = 10. Exactly one = union − exactly two − triple = 40 − 10 − 4 = **26**.",
    sc="Union minus everyone in two or three sets.",
    d='hard', sub='three-set-operations', pat='exactly two / exactly one', t=70))

# 9 (relation nested chain)
def ALL(a, b): return lambda m: m[a] <= m[b]
def NO(a, b): return lambda m: not (m[a] & m[b])

NEST = [ALL('squares', 'rectangles'), ALL('rectangles', 'polygons')]
check_rel(['squares', 'rectangles', 'polygons'], NEST, 'squares', 'rectangles', 'subset')
check_rel(['squares', 'rectangles', 'polygons'], NEST, 'rectangles', 'polygons', 'subset')
check_rel(['squares', 'rectangles', 'polygons'], NEST, 'squares', 'polygons', 'subset')
pr.append(C.Q(
    'rsn-venn-9',
    "Which diagram correctly represents **Squares, Rectangles and Polygons**?",
    ['Squares inside Rectangles, both inside Polygons',
     'Three circles, each pair intersecting',
     'Squares and Rectangles intersecting, both inside Polygons',
     'Three completely separate circles'],
    'Squares inside Rectangles, both inside Polygons',
    "Every square is a rectangle and every rectangle is a polygon — a fully nested chain of circles.",
    sc="Necessity test passes for every pair → nested circles.",
    d='easy', sub='relation-diagrams', pat='choose-the-diagram', t=40))

# 10 (relation: mothers/females/engineers)
MFE = [ALL('mothers', 'females')]
check_rel(['mothers', 'females', 'engineers'], MFE, 'mothers', 'females', 'subset')
check_rel(['mothers', 'females', 'engineers'], [], 'mothers', 'engineers', 'overlap')
check_rel(['mothers', 'females', 'engineers'], [], 'females', 'engineers', 'overlap')
pr.append(C.Q(
    'rsn-venn-10',
    "Which diagram correctly represents **Mothers, Females and Engineers**?",
    ['Mothers inside Females; Engineers circle intersecting both',
     'All three circles intersecting equally',
     'Mothers and Engineers inside Females',
     'Engineers inside Females; Mothers separate'],
    'Mothers inside Females; Engineers circle intersecting both',
    "Every mother is definitionally a female → Mothers inside Females. Engineers can be male or female and may or may not be mothers → the Engineers circle crosses both.",
    sc="Definition decides nesting; possibility decides intersection.",
    d='medium', sub='relation-diagrams', pat='choose-the-diagram', t=50))

# 11 (reverse with neither)
total = 8 + 10 + 12 + 7
assert total == 37
pr.append(C.Q(
    'rsn-venn-11',
    "**|A ∩ B| = 8, |A − B| = 10, |B| = 20 and 7 elements belong to neither set.** What is the size of the **universal set** (all elements considered)?",
    ['37', '45', '38', '40'], '37',
    "B − A = 20 − 8 = 12. Total = 8 + 10 + 12 + 7 = **37**.",
    sc="Four disjoint regions: both, A-only, B-only, neither.",
    d='medium', sub='two-set-operations', pat='reverse region puzzle', t=50))

# 12 (symmetric difference)
assert (25 - 8) + (20 - 8) == 29
pr.append(C.Q(
    'rsn-venn-12',
    "**|A| = 25, |B| = 20 and |A ∩ B| = 8.** How many elements are in **exactly one** of A and B?",
    ['29', '37', '17', '21'], '29',
    "Exactly one = (25 − 8) + (20 − 8) = 17 + 12 = **29**.",
    sc="Strip the lens from each circle and add the moons.",
    d='easy', sub='two-set-operations', pat='two-set region count', t=35))

# 13 (none from three sets)
u = 55 + 45 + 40 - 20 - 18 - 15 + 8
assert u == 95 and 120 - u == 25
pr.append(C.Q(
    'rsn-venn-13',
    "In a batch of **120 trainees: 55 know Python, 45 know Java, 40 know C++; 20 know Python and Java, 18 know Java and C++, 15 know Python and C++; 8 know all three.** How many trainees know **none** of the three?",
    ['25', '15', '30', '20'], '25',
    "Union = 55+45+40−20−18−15+8 = 95. None = 120 − 95 = **25**.",
    sc="Full inclusion-exclusion, then subtract from the batch.",
    d='medium', sub='three-set-operations', pat='three-set union / none', t=55))

# 14 (at least two)
at2 = (12 - 5) + (10 - 5) + (9 - 5) + 5
assert at2 == 21
pr.append(C.Q(
    'rsn-venn-14',
    "**|A∩B| = 12, |B∩C| = 10, |A∩C| = 9 and |A∩B∩C| = 5.** How many elements belong to **at least two** of the sets?",
    ['21', '31', '16', '26'], '21',
    "At least two = exactly two + all three = (12−5)+(10−5)+(9−5) + 5 = 7+5+4+5 = **21**. Shortcut: pairwise sum 31 counts the triple 3 times → 31 − 2×5 = 21.",
    sc="Pairwise sum − 2 × triple = at-least-two.",
    d='hard', sub='three-set-operations', pat='exactly two / exactly one', t=65))

# 15 (relation disjoint)
EHW = [ALL('english-words', 'words'), ALL('hindi-words', 'words'),
       NO('english-words', 'hindi-words')]
check_rel(['words', 'english-words', 'hindi-words'], EHW, 'english-words', 'words', 'subset')
check_rel(['words', 'english-words', 'hindi-words'], EHW, 'hindi-words', 'words', 'subset')
check_rel(['words', 'english-words', 'hindi-words'], EHW, 'english-words', 'hindi-words', 'disjoint')
pr.append(C.Q(
    'rsn-venn-15',
    "Which diagram correctly represents **Words, English words and Hindi words**?",
    ['English and Hindi circles inside Words, not overlapping each other',
     'Three circles, each pair intersecting',
     'English words inside Words; Hindi words a separate circle outside',
     'All three nested inside one another'],
    'English and Hindi circles inside Words, not overlapping each other',
    "Both are subsets of Words (necessity), and a word cannot be English and Hindi at once (impossibility) → two disjoint circles inside the big one.",
    sc="One pair needs the impossibility test — the other two are simple nestings.",
    d='medium', sub='relation-diagrams', pat='choose-the-diagram', t=50))

assert len(pr) == 15

t = C.topic(
    'venn-diagrams', 'Venn Diagrams', 'medium', {'tier1': '1-2', 'tier2': '1-3'},
    "Two question families: (1) region arithmetic — count union, intersection, only-regions, exactly-two, neither using inclusion-exclusion over labelled Venn regions; (2) relation selection — decide whether categories nest (definitional necessity), stay apart (impossibility) or intersect (possible but not forced). The arithmetic family is pure formula discipline; the relation family is two quick tests per pair. Label every region before computing and both become near-90% accuracy topics.",
    subs, patterns, examples, pr)

C.write_topic(t)
print('OK venn-diagrams')
