# build blood-relations topic (topic 7)
import common as C

G = {}  # name -> {'g': 'M'/'F', 'parents': set, 'spouse': name|None}


def person(name, gender, parents=(), spouse=None):
    G[name] = {'g': gender, 'parents': set(parents), 'spouse': spouse}


def reset():
    G.clear()


def parents(x):
    return set(G[x]['parents'])


def children(x):
    return {q for q in G if x in G[q]['parents']}


def siblings(x):
    px = parents(x)
    if not px:
        return set()
    return {q for q in G if q != x and parents(q) & px}


def rel(a, b):
    """set of relation names: how is b related to a"""
    out = set()
    if a == b:
        return out
    pa, pb = parents(a), parents(b)
    ga, gb = G[a]['g'], G[b]['g']
    if b in pa:
        out.add('father' if gb == 'M' else 'mother')
    for x in pa:
        if G[x]['spouse'] == b:
            out.add('father' if gb == 'M' else 'mother')
    if a in pb:
        out.add('son' if gb == 'M' else 'daughter')
    if pa and pb and (pa & pb):
        out.add('brother' if gb == 'M' else 'sister')
    gp_a = set()
    for x in pa:
        gp_a |= parents(x)
    if b in gp_a:
        out.add('grandfather' if gb == 'M' else 'grandmother')
    gp_b = set()
    for x in pb:
        gp_b |= parents(x)
    if a in gp_b:
        out.add('grandson' if gb == 'M' else 'granddaughter')
    for x in pa:
        if b in siblings(x):
            out.add('uncle' if gb == 'M' else 'aunt')
    sib_a = siblings(a)
    for x in pb:
        if x in sib_a:
            out.add('nephew' if gb == 'M' else 'niece')
    for x in pa:
        for y in pb:
            if x != y and y in siblings(x):
                out.add('cousin')
    sp = G[a]['spouse']
    if sp == b:
        out.add('husband' if gb == 'M' else 'wife')
    if sp:
        if b in parents(sp):
            out.add('father-in-law' if gb == 'M' else 'mother-in-law')
        if b in siblings(sp):
            out.add('brother-in-law' if gb == 'M' else 'sister-in-law')
    spb = G[b]['spouse']
    if spb is not None:
        if a in G[spb]['parents']:
            out.add('son-in-law' if gb == 'M' else 'daughter-in-law')
        elif spb in sib_a:
            out.add('brother-in-law' if gb == 'M' else 'sister-in-law')
    return out


def check_rel(a, b, correct, distractors):
    r = rel(a, b)
    assert correct in r, ('missing true relation', a, b, correct, r)
    for d in distractors:
        assert d not in r, ('distractor also holds', a, b, d, r)


subs = []

subs.append(C.sub(
    'blood-relations-idea', 'How to solve blood-relation questions',
    "Every blood-relation question is a hidden **family tree**. The questions never need social knowledge — only disciplined bookkeeping. The universal method:\n\n1. **Draw the tree.** Use a symbol per person, `+` for male, `−` for female, a `=` for marriage, and a vertical line for parent→child. CGL toppers draw; they do not hold chains in their head.\n2. **Decode one statement at a time**, adding each person to the tree *at the generation where they belong*.\n3. **Read the answer off the tree** along the shortest path between the two named people.\n\nTwo rules keep the tree honest:\n\n- **Never assume gender.** 'Cousin', 'child of X' give no gender; only father/brother/son/uncle etc. fix it as male, mother/sister/daughter/aunt as female.\n- **Watch the direction.** 'How is A related to B?' asks for the relation *from B's side* — B's ___ is A. Reversing the direction is the single biggest mark-loser here.\n\nGeneration check: every marriage joins two people of the same generation; every 'son of' drops one generation down. If your finished tree shows a person as their own ancestor, re-read a statement — you transposed a direction.",
    formulas=[
        C.F('Symmetry pairs', '\\text{father} \\leftrightarrow \\text{son},\\ \\text{mother} \\leftrightarrow \\text{daughter},\\ \\text{uncle} \\leftrightarrow \\text{nephew}', "Every relation has a mirror: if A is B's uncle, B is A's nephew (or niece)."),
        C.F('In-law map', '\\text{spouse of child} \\to \\text{son/daughter-in-law};\\ \\text{parent of spouse} \\to \\text{father/mother-in-law}', 'Sibling of spouse, or spouse of sibling → brother/sister-in-law.'),
        C.F('Cousin', "\\text{cousin} = \\text{child of a parent's sibling}", "Aunt/uncle's children are cousins — never 'nephew'."),
    ],
    tricks=[
        C.T(
            'Two-column decoding',
            "Write each statement as an arrow in the margin: 'Suresh's daughter is Pooja' becomes `Suresh → Pooja (−)`. Arrows point parent → child. When every statement is an arrow, the tree draws itself and direction mistakes disappear.",
            "**Q.** 'A is B's sister. C is A's mother. How is C related to B?'\n\n**Sol.** Arrows: C → A(−), C → ? ; A–B are siblings → C → B. C is the mother of both → C is B's **mother**.",
            "Arrows parent→child, always; siblings then share the same arrowhead."),
    ],
    mistakes=[
        "Assuming a gender for a person the statements never fix.",
        "Answering the reversed relation ('Pooja's grandfather' vs 'grandson of Pooja' direction).",
        "Mixing generations when 'only son/daughter' statements appear.",
    ]))

subs.append(C.sub(
    'family-tree-puzzles', 'Multi-statement tree puzzles',
    "The statement-list format: three to six sentences describe one family, then a relation is asked. The sentences are deliberately shuffled — husbands before wives, elders after juniors — so that reading them *in order* gives a tangled tree. Reorder, don't obey: place the oldest generation first, hang the children under them, then attach marriages.\n\n**Worked skeleton** (the shape CGL reuses constantly):\n\n- Dhanraj = Kamla; children Suresh (M), Veena (−)\n- Suresh = Rita; children Amit (M), Pooja (−)\n- Veena = Mohan; son Rohit (M)\n- Amit = Sneha; son Karan (M)\n\nFrom this one tree you can answer: Rohit↔Pooja (cousins), Dhanraj↔Pooja (grandfather), Sneha↔Rita (daughter-in-law), Kamla↔Rohit (grandmother), and counting questions ('how many males?' — six here: Dhanraj, Suresh, Mohan, Amit, Rohit, Karan).\n\n**Chain questions** compress the same idea: 'Mohan is Rekha's father. Ramesh is Mohan's father. How is Ramesh related to Rekha?' Two arrows up from Rekha — Mohan, then Ramesh — grandfather. Count the arrows; each arrow is one generation.",
    tricks=[
        C.T(
            'Top-down reconstruction',
            "Find the person who is nobody's child (the oldest named) and start there. Every other statement then attaches downward or sideways by marriage. A tree built top-down never needs revising.",
            "**Q.** 'Rita's son is Amit. Amit's son is Karan. How is Karan related to Rita?'\n\n**Sol.** Rita → Amit → Karan, two arrows down from Rita: Karan is her **grandson**.",
            "The elder-most statement is the tree root; build downward from it."),
        C.T(
            'Arrow-count for generations',
            "Relation from arrow count: 1 down = son/daughter, 2 down = grandson/granddaughter, 1 up = father/mother, 2 up = grandfather/grandmother. Sideways through a marriage adds '-in-law'.",
            "**Q.** 'Mohan is Rekha's father. Ramesh is Mohan's father. How is Ramesh related to Rekha?'\n\n**Sol.** Rekha ↑ Mohan ↑ Ramesh — two arrows up → **grandfather**.",
            "Count arrows first, fix gender second — the count picks the relation family."),
    ],
    mistakes=[
        "Reading statements in exam order instead of reconstructing generation-wise.",
        "Calling an uncle's child a nephew — that child is a cousin.",
        "Forgetting that a spouse's siblings are also brothers/sisters-in-law.",
    ]))

subs.append(C.sub(
    'pointing-introduction', 'Pointing and introducing',
    "*'Pointing to a man, Rita said, \"He is the only son of my mother's mother's only child.\"'* — the pointing format hides the tree inside **spoken phrases**, and the speaker is always part of the tree. Decode each phrase from the inside out, in layers:\n\n1. Resolve the innermost possessive first ('my mother's mother' = maternal grandmother).\n2. Apply 'only child' / 'only son' / 'only daughter' carefully — 'only son' does *not* mean no other children, it means no other **sons**.\n3. Remember the speaker is a person in the tree. 'My mother's only child' = **the speaker** — the fastest self-reference in the topic.\n4. Finally answer: the man/woman in the photo is [relation] of the speaker.\n\nThe classic trap: 'my father's only son' when the speaker is male = **the speaker himself**. CGL exploits this constantly; a son of that person can then be the speaker's own son or brother depending on the remaining phrase.",
    tricks=[
        C.T(
            'Peel the phrase inside-out',
            "Underline the innermost 'my ___' and resolve outward, one layer per line. Then place speaker and target in a two-person sketch.",
            "**Q.** 'Pointing to a man, Sunita said, \"He is the only son of my mother's mother's only child.\"'\n\n**Sol.** My mother's mother's only child = Sunita's mother. Her only son = Sunita's brother. The man is Sunita's **brother**.",
            "One layer per line; the speaker enters the tree at layer one."),
        C.T(
            'The self-reference alarm',
            "Whenever a phrase like 'my father's only son' or 'my mother's only daughter' appears, test whether it resolves to the speaker. If the speaker's gender fits, it does — and the question is really about the speaker's own child, sibling or spouse.",
            "**Q.** 'Pointing to Ketan, Meera said, \"His mother is the only child of my mother.\"'\n\n**Sol.** Only child of Meera's mother = Meera. So Ketan's mother = Meera → Ketan is Meera's **son**.",
            "Self-reference collapses two layers at once — instant shortcut when spotted."),
    ],
    mistakes=[
        "Taking 'only son' to mean 'only child'.",
        "Forgetting the speaker is in the tree (missing the self-reference).",
        "Answering the photo-person's relation in the reverse direction ('the man's sister' instead of 'her brother').",
    ]))

subs.append(C.sub(
    'coded-relations', 'Coded (symbol) relations',
    "The Tier-2 favourite: *'P + Q means P is the father of Q; P − Q means P is the mother of Q; ...'* Then a coded string like `A + B × C` must be decoded into a real relation.\n\n**Method:**\n\n1. Rewrite the string as nested statements: `A + B × C` = (A is the father of B) and (B is the sister of C).\n2. Build the mini-tree: place A above B; B and C are siblings, so A (the shared parent side) sits above both.\n3. Read off the asked pair — here A is the **father** of C.\n\nGender bookkeeping is the whole game. Each symbol fixes the *first* person's gender (father → male, mother → female, sister → female). A symbol like 'X is the sibling of Y' fixes nothing. Track genders under the letters as you decode; the answer usually turns on one of them.\n\nLonger strings (A + B × C − D) are the same loop: decode pairwise, extend the tree, read the final pair. Never decode the whole string at once.",
    tricks=[
        C.T(
            'Decode pairwise, tree under it',
            "For each operator, write its one-line sentence beneath the string, then draw the tree. Two operators ≈ four people; three ≈ five.",
            "**Q.** 'X % Y' = X is the wife of Y; 'X # Y' = X is the sister of Y. In `M % N # O`, how is M related to O?\n\n**Sol.** M is the wife of N; N is the sister of O. M is the wife of O's sister → **sister-in-law**.",
            "Pairwise decoding turns a 6-symbol string into 3 plain sentences."),
        C.T(
            'Gender audit before answering',
            "Before marking, check every needed gender is *pinned by a symbol*. If the asked relation needs a gender nobody fixed, the answer is the gender-neutral form (cousin, sibling-in-law phrasing) — or you have mis-decoded.",
            "**Q.** 'P @ Q' = P is the son of Q; 'P & Q' = P is the husband of Q. In `P @ Q & R`, how is R related to P?\n\n**Sol.** P is the son of Q; Q is the husband of R. R is Q's wife, Q is P's parent → R is P's **mother**.",
            "Q's male gender (husband) is what converts 'parent of P' into 'mother'."),
    ],
    mistakes=[
        "Decoding `A + B × C` as 'A is the father of C' *and* forgetting to verify the sibling link connects the right pair.",
        "Assuming the gender of a person whose operator fixes none (e.g. 'brother of Y' fixes the first, not Y).",
        "Reading the final question in the reverse direction (M↔O mix-ups).",
    ]))

patterns = [
    C.P('Mixed-statement family tree', 'very common',
        "3-6 shuffled sentences describing one family; 'How is X related to Y?'",
        "Rebuild the tree top-down generation by generation, then read the shortest path."),
    C.P('Pointing to a photograph', 'very common',
        "'Pointing to X, Y said, \"He/She is ...\" — find the relation.",
        "Peel the phrase inside-out; test the self-reference ('my mother's only child') first."),
    C.P('Symbol-coded relations', 'common',
        "'P + Q means P is the father of Q' plus a coded string.",
        "Decode pairwise into plain sentences, draw the mini-tree, read the final pair."),
    C.P('Chain relations', 'common',
        "Two or three 'A is B's father/mother' links in a row.",
        "Count arrows (generations) up or down, then fix gender."),
    C.P('Counting males/females', 'common',
        "A full tree plus 'how many male members are there?'",
        "Draw the tree; tick gender only where a statement fixes it; count ticks and knowns."),
    C.P('In-law relations', 'common',
        "Questions about wives of sons, husbands of sisters, parents of spouses.",
        "Apply the in-law map: spouse-of-child, parent-of-spouse, sibling-of-spouse."),
]

examples = []

# ex1: chain -> granddaughter
reset()
person('A', 'F')
person('B', 'M', parents=('C',))
person('A2', 'M', parents=('C',))  # placeholder to give B a sibling? not needed
person('C', 'F')
person('D', 'M')
G['A']['parents'] = {'C'}
G['B']['parents'] = {'C'}
G['C']['parents'] = {'D'}
check_rel('D', 'A', 'granddaughter', ['daughter', 'niece', 'grandmother', 'aunt'])
examples.append(C.Q(
    'rsn-blood-relations-ex1',
    "**A is B's sister. C is the mother of A and B. D is the father of C.** How is A related to D?",
    ['Granddaughter', 'Daughter', 'Niece', 'Aunt'], 'Granddaughter',
    "Tree: D → C → (A, B). A is two generations below D and female, so A is D's **granddaughter**. (Daughter skips a generation; niece would need A to be a sibling's child — D has no sibling here.)",
    sc="Two arrows up from A to D → grandchild; A is female → granddaughter.",
    d='easy', sub='family-tree-puzzles', pat='chain relations', t=35))

# ex2: direction emphasis
reset()
person('Rekha', 'F')
person('Mohan', 'M', parents=('Ramesh',))
person('Ramesh', 'M')
G['Rekha']['parents'] = {'Mohan'}
check_rel('Rekha', 'Ramesh', 'grandfather', ['father', 'grandson', 'uncle', 'nephew'])
examples.append(C.Q(
    'rsn-blood-relations-ex2',
    "**Mohan is Rekha's father. Ramesh is Mohan's father.** How is Ramesh related to Rekha?",
    ['Grandfather', 'Father', 'Grandson', 'Uncle'], 'Grandfather',
    "Rekha ↑ Mohan ↑ Ramesh. From Rekha it is two generations up, and Ramesh is male → **grandfather**. Had the question asked 'Rekha is Ramesh's ___', the answer would be granddaughter — direction decides.",
    sc="Count generations between the pair, then apply the asked direction.",
    d='easy', sub='family-tree-puzzles', pat='chain relations', t=30))

# ex3: coded son
reset()
person('B', 'F', spouse='C')
person('C', 'M', spouse='B')
person('A', 'M', parents=('B', 'C'))
check_rel('C', 'A', 'son', ['grandson', 'nephew', 'brother-in-law', 'brother'])
examples.append(C.Q(
    'rsn-blood-relations-ex3',
    "'**P + Q**' means **P is the son of Q** and '**P ÷ Q**' means **P is the wife of Q**. In the expression '**A + B ÷ C**', how is **A related to C**?",
    ['Son', 'Grandson', 'Nephew', 'Brother'], 'Son',
    "Decode pairwise: A + B → A is the son of B. B ÷ C → B is the wife of C. So A is the son of C's wife, and since B is female and married to C, A is C's **son**. (Grandson would need A to be a generation lower — he is directly B's child.)",
    sc="Decode pairwise; B's gender from 'wife' is what makes A a son of C, not a step-nephew.",
    d='medium', sub='coded-relations', pat='symbol-coded relations', t=45))

# ex4: brother-in-law
reset()
person('P', 'M', spouse='Q')
person('Q', 'F', spouse='P')
person('R', 'M', parents=('P', 'Q'))
person('S', 'M', parents=('P', 'Q'))
person('T', 'F', spouse='R')
check_rel('T', 'S', 'brother-in-law', ['cousin', 'son', 'uncle', 'brother'])
examples.append(C.Q(
    'rsn-blood-relations-ex4',
    "**P and Q are a married couple, P being the husband. R and S are their sons. T is R's wife.** How is **S related to T**?",
    ['Brother-in-law', 'Cousin', 'Son', 'Uncle'], 'Brother-in-law',
    "S is the brother of R, and T is R's wife — so S is the **brother-in-law** of T (husband's brother).",
    sc="Spouse's sibling, or sibling's spouse — either route gives brother/sister-in-law.",
    d='easy', sub='family-tree-puzzles', pat='in-law relations', t=35))

# ---------------------------------------------------------------- practice
pr = []

# 1: cousin
reset()
person('Dad', 'M')
person('Suresh', 'M', parents=('Dad',))
person('Veena', 'F', parents=('Dad',))
person('Pooja', 'F', parents=('Suresh',))
person('Rohit', 'M', parents=('Veena',))
check_rel('Pooja', 'Rohit', 'cousin', ['brother', 'nephew', 'uncle', 'niece'])
pr.append(C.Q(
    'rsn-blood-relations-1',
    "**Suresh and Veena are siblings. Pooja is Suresh's daughter. Rohit is Veena's son.** How is **Rohit related to Pooja**?",
    ['Cousin', 'Brother', 'Nephew', 'Uncle'], 'Cousin',
    "Pooja and Rohit are children of siblings — they are **cousins**. (Nephew would need Rohit to be a child of Pooja's brother; uncle would need him to be a brother of Pooja's parent.)",
    sc="Children of siblings = cousins, whatever the genders.",
    d='easy', sub='family-tree-puzzles', pat='chain relations', t=35))

# 2: grandfather
reset()
person('Dhanraj', 'M')
person('Suresh', 'M', parents=('Dhanraj',))
person('Pooja', 'F', parents=('Suresh',))
check_rel('Pooja', 'Dhanraj', 'grandfather', ['father', 'grandson', 'uncle', 'father-in-law'])
pr.append(C.Q(
    'rsn-blood-relations-2',
    "**Dhanraj's son is Suresh. Suresh's daughter is Pooja.** How is **Dhanraj related to Pooja**?",
    ['Grandfather', 'Father', 'Grandson', 'Uncle'], 'Grandfather',
    "Pooja ↑ Suresh ↑ Dhanraj: two generations up, male → **grandfather**.",
    sc="Two up-arrows from Pooja land on Dhanraj — grandparent level.",
    d='easy', sub='family-tree-puzzles', pat='chain relations', t=30))

# 3: daughter-in-law
reset()
person('Rita', 'F')
person('Amit', 'M', parents=('Rita',), spouse='Sneha')
person('Sneha', 'F', spouse='Amit')
check_rel('Rita', 'Sneha', 'daughter-in-law', ['daughter', 'niece', 'sister-in-law', 'aunt'])
pr.append(C.Q(
    'rsn-blood-relations-3',
    "**Rita's son is Amit. Amit's wife is Sneha.** How is **Sneha related to Rita**?",
    ['Daughter-in-law', 'Daughter', 'Niece', 'Sister-in-law'], 'Daughter-in-law',
    "Sneha is the wife of Rita's son → **daughter-in-law**. (Sister-in-law would need Sneha to be a sibling of Rita or of Rita's spouse.)",
    sc="Wife of my child = daughter-in-law; parent of my spouse = mother/father-in-law.",
    d='easy', sub='family-tree-puzzles', pat='in-law relations', t=30))

# 4: aunt
reset()
person('GP', 'M')
person('Suresh', 'M', parents=('GP',))
person('Veena', 'F', parents=('GP',))
person('Pooja', 'F', parents=('Suresh',))
check_rel('Pooja', 'Veena', 'aunt', ['mother', 'grandmother', 'cousin', 'niece'])
pr.append(C.Q(
    'rsn-blood-relations-4',
    "**Veena is the sister of Suresh. Pooja is the daughter of Suresh.** How is **Veena related to Pooja**?",
    ['Aunt', 'Mother', 'Grandmother', 'Cousin'], 'Aunt',
    "Veena is the sister of Pooja's father → Pooja's **aunt**. (Cousin would require Veena to be a *child* of a sibling of Pooja's parent.)",
    sc="Parent's sibling = aunt/uncle; sibling's child = nephew/niece. Keep the two apart.",
    d='easy', sub='family-tree-puzzles', pat='chain relations', t=30))

# 5: grandmother
reset()
person('Kamla', 'F')
person('Veena', 'F', parents=('Kamla',))
person('Rohit', 'M', parents=('Veena',))
check_rel('Rohit', 'Kamla', 'grandmother', ['mother', 'aunt', 'granddaughter', 'niece'])
pr.append(C.Q(
    'rsn-blood-relations-5',
    "**Kamla is the mother of Veena. Veena's son is Rohit.** How is **Kamla related to Rohit**?",
    ['Grandmother', 'Mother', 'Aunt', 'Granddaughter'], 'Grandmother',
    "Rohit ↑ Veena ↑ Kamla: two generations up, female → **grandmother** (mother's mother).",
    sc="Maternal or paternal doesn't change the answer — grandparent either way.",
    d='easy', sub='family-tree-puzzles', pat='chain relations', t=30))

# 6: count males
reset()
person('Dhanraj', 'M', spouse='Kamla')
person('Kamla', 'F', spouse='Dhanraj')
person('Suresh', 'M', parents=('Dhanraj', 'Kamla'), spouse='Rita')
person('Rita', 'F', spouse='Suresh')
person('Amit', 'M', parents=('Suresh', 'Rita'), spouse='Sneha')
person('Pooja', 'F', parents=('Suresh', 'Rita'))
person('Sneha', 'F', spouse='Amit')
person('Veena', 'F', parents=('Dhanraj', 'Kamla'), spouse='Mohan')
person('Mohan', 'M', spouse='Veena')
person('Rohit', 'M', parents=('Veena', 'Mohan'))
person('Karan', 'M', parents=('Amit', 'Sneha'))
males = sum(1 for n in G if G[n]['g'] == 'M')
females = len(G) - males
assert males == 6 and females == 5, (males, females)
pr.append(C.Q(
    'rsn-blood-relations-6',
    "**Dhanraj and his wife Kamla have two children — Suresh and Veena. Suresh's wife is Rita; their children are Amit and Pooja. Veena's husband is Mohan; their son is Rohit. Amit's wife is Sneha; their son is Karan.** How many **male members** are there in the family?",
    ['6', '5', '7', '4'], '6',
    "Males: Dhanraj, Suresh, Mohan, Amit, Rohit, Karan = **6**. Females: Kamla, Rita, Pooja, Sneha, Veena = 5. Tick each gender off the drawn tree, never from memory.",
    sc="Mark +/− beside every name while reading; counting then takes five seconds.",
    d='medium', sub='family-tree-puzzles', pat='counting males/females', t=50))

# 7: pointing brother
reset()
person('GMM', 'F')
person('Meena', 'F', parents=('GMM',))
person('Sunita', 'F', parents=('Meena',))
person('Manoj', 'M', parents=('Meena',))
check_rel('Sunita', 'Manoj', 'brother', ['cousin', 'uncle', 'nephew', 'son'])
pr.append(C.Q(
    'rsn-blood-relations-7',
    "Pointing to a man, Sunita said, **\"He is the only son of my mother's mother's only child.\"** How is the man related to Sunita?",
    ['Brother', 'Cousin', 'Uncle', 'Nephew'], 'Brother',
    "Inside-out: my mother's mother's only child = Sunita's mother. Her only son = Sunita's brother. The man is Sunita's **brother**. ('Only son' bars other boys, not other children — Sunita herself is the daughter.)",
    sc="Resolve the innermost 'my ...' first; 'only child' of the maternal grandmother = the mother.",
    d='medium', sub='pointing-introduction', pat='pointing to a photograph', t=45))

# 8: pointing sister
reset()
person('GF', 'M')
person('F', 'M', parents=('GF',))
person('Arjun', 'M', parents=('F',))
person('Usha', 'F', parents=('F',))
check_rel('Arjun', 'Usha', 'sister', ['cousin', 'niece', 'aunt', 'daughter'])
pr.append(C.Q(
    'rsn-blood-relations-8',
    "Pointing to a woman, Arjun said, **\"She is the daughter of my father's father's only son.\"** How is the woman related to Arjun?",
    ['Sister', 'Cousin', 'Niece', 'Aunt'], 'Sister',
    "My father's father's only son = Arjun's father. His daughter = Arjun's **sister**. ('Only son' pins the father as the grandfather's sole boy; Arjun's gender is given by his name being male in the sentence.)",
    sc="Grandfather → only son → your own father; his daughter is your sister.",
    d='medium', sub='pointing-introduction', pat='pointing to a photograph', t=45))

# 9: pointing husband
reset()
person('PF', 'M')
person('PM', 'F', spouse='PF')
person('Priya', 'F', parents=('PF', 'PM'), spouse='Vikram')
person('Bharat', 'M', parents=('PF', 'PM'))
person('Vikram', 'M', spouse='Priya')
person('Diya', 'F', parents=('Priya', 'Vikram'))
check_rel('Priya', 'Vikram', 'husband', ['brother-in-law', 'father', 'uncle', 'brother'])
pr.append(C.Q(
    'rsn-blood-relations-9',
    "Pointing to a man in a photograph, Priya said, **\"He is the father of my brother's niece.\"** How is the man related to Priya?",
    ['Husband', 'Brother-in-law', 'Father', 'Uncle'], 'Husband',
    "Priya's brother's niece = a daughter of Priya or of another sibling. Priya is the brother's only sister, so the niece is Priya's own daughter — and her father is Priya's **husband**.",
    sc="'My brother's niece' = your own daughter (when you are the only sister). Her father = your husband.",
    d='hard', sub='pointing-introduction', pat='pointing to a photograph', t=60))

# 10: pointing cousin
reset()
person('GF', 'M')
person('RamF', 'M', parents=('GF',))
person('Ramesh', 'M', parents=('RamF',))
person('SarA', 'F', parents=('GF',))
person('Deepa', 'F', parents=('SarA',))
check_rel('Ramesh', 'Deepa', 'cousin', ['sister', 'niece', 'aunt', 'daughter'])
pr.append(C.Q(
    'rsn-blood-relations-10',
    "Pointing to Deepa, Ramesh said, **\"She is the daughter of my father's sister.\"** How is Deepa related to Ramesh?",
    ['Cousin', 'Sister', 'Niece', 'Aunt'], 'Cousin',
    "My father's sister = Ramesh's aunt; her daughter = Ramesh's **cousin**. (Niece is the reverse — the child of one's own sibling.)",
    sc="Aunt's children are cousins; sibling's children are nephews/nieces.",
    d='easy', sub='pointing-introduction', pat='pointing to a photograph', t=35))

# 11: coded father
reset()
person('A', 'M', spouse='W')
person('W', 'F', spouse='A')
person('B', 'F', parents=('A', 'W'))
person('C', 'M', parents=('A', 'W'))
check_rel('C', 'A', 'father', ['grandfather', 'uncle', 'father-in-law', 'brother'])
pr.append(C.Q(
    'rsn-blood-relations-11',
    "'**P + Q**' means **P is the father of Q**; '**P × Q**' means **P is the sister of Q**. In '**A + B × C**', how is **A related to C**?",
    ['Father', 'Grandfather', 'Uncle', 'Father-in-law'], 'Father',
    "Decode pairwise: A + B → A is the father of B. B × C → B is the sister of C. Siblings share parents, so A is the father of C too → **Father**. (Grandfather needs an extra generation; none exists here.)",
    sc="Parent of one sibling = parent of all siblings in these puzzles.",
    d='medium', sub='coded-relations', pat='symbol-coded relations', t=45))

# 12: coded sister-in-law
reset()
person('GP1', 'M')
person('GP2', 'F', spouse='GP1')
person('M', 'F', spouse='N')
person('N', 'F', spouse='M', parents=('GP1', 'GP2'))
person('O', 'M', parents=('GP1', 'GP2'))
check_rel('O', 'M', 'sister-in-law', ['wife', 'aunt', 'cousin', 'mother'])
pr.append(C.Q(
    'rsn-blood-relations-12',
    "'**X % Y**' means **X is the wife of Y**; '**X # Y**' means **X is the sister of Y**. In '**M % N # O**', how is **M related to O**?",
    ['Sister-in-law', 'Wife', 'Aunt', 'Cousin'], 'Sister-in-law',
    "Decode: M % N → M is the wife of N. N # O → N is the sister of O. So M is the wife of O's sister → M is O's **sister-in-law**.",
    sc="Wife of my sibling = sister-in-law — no gender needed for O.",
    d='medium', sub='coded-relations', pat='symbol-coded relations', t=45))

# 13: coded mother
reset()
person('Q', 'M', spouse='R')
person('R', 'F', spouse='Q')
person('P', 'M', parents=('Q',))
check_rel('P', 'R', 'mother', ['grandmother', 'aunt', 'sister', 'mother-in-law'])
pr.append(C.Q(
    'rsn-blood-relations-13',
    "'**P @ Q**' means **P is the son of Q**; '**P & Q**' means **P is the husband of Q**. In '**P @ Q & R**', how is **R related to P**?",
    ['Mother', 'Grandmother', 'Aunt', 'Sister'], 'Mother',
    "Decode: P @ Q → P is the son of Q. Q & R → Q is the husband of R, so Q is male and R is his wife. Q is P's parent, so R — Q's wife — is P's **mother**.",
    sc="The 'husband' symbol pins Q male, which upgrades 'spouse of my parent' to mother.",
    d='medium', sub='coded-relations', pat='symbol-coded relations', t=50))

# 14: grandson
reset()
person('Rita', 'F')
person('Amit', 'M', parents=('Rita',))
person('Karan', 'M', parents=('Amit',))
check_rel('Rita', 'Karan', 'grandson', ['son', 'nephew', 'cousin', 'grandfather'])
pr.append(C.Q(
    'rsn-blood-relations-14',
    "**Rita's son is Amit. Amit's son is Karan.** How is **Karan related to Rita**?",
    ['Grandson', 'Son', 'Nephew', 'Cousin'], 'Grandson',
    "Rita → Amit → Karan: two generations down from Rita, male → **grandson**.",
    sc="Two down-arrows from Rita = grandchild; Karan is a boy → grandson.",
    d='easy', sub='family-tree-puzzles', pat='chain relations', t=30))

# 15: nephew
reset()
person('GFa', 'M')
person('GFather', 'M', parents=('GFa',))
person('Girl', 'F', parents=('GFather',))
person('Bros', 'M', parents=('GFather',))
person('Boy', 'M', parents=('Bros',))
check_rel('Girl', 'Boy', 'nephew', ['son', 'brother', 'cousin', 'grandson'])
pr.append(C.Q(
    'rsn-blood-relations-15',
    "Introducing a boy, a girl said, **\"He is the son of my father's only son.\"** How is the boy related to the girl?",
    ['Nephew', 'Son', 'Brother', 'Cousin'], 'Nephew',
    "My father's only son = the girl's brother (the girl is a daughter, so 'only son' is her brother). The boy is her brother's son → her **nephew**.",
    sc="'Only son' of her father cannot be the girl — she is female — so it is her brother.",
    d='medium', sub='pointing-introduction', pat='pointing to a photograph', t=45))

assert len(pr) == 15

t = C.topic(
    'blood-relations', 'Blood Relations', 'high', {'tier1': '2-4', 'tier2': '2-3'},
    "One of the highest-yield reasoning topics: family-tree puzzles, pointing-at-photograph statements and symbol-coded chains, all solvable by drawing a small tree with parent-to-child arrows. Marks are lost to direction reversals and assumed genders, never to difficulty. A fixed decoding habit — inside-out for pointing questions, pairwise for coded strings, top-down for statement lists — makes nearly every question here a 30-45 second correct answer.",
    subs, patterns, examples, pr)

C.write_topic(t)
print('OK blood-relations')
