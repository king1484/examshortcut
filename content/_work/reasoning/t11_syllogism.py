# build syllogism topic (topic 11)
from itertools import product
import common as C

N_IND = 4


def models_gen(terms):
    for bits in product([0, 1], repeat=N_IND * len(terms)):
        m = {}
        for ti, t in enumerate(terms):
            m[t] = frozenset(j for j in range(N_IND) if bits[j * len(terms) + ti])
        yield m


def ALL(a, b): return lambda m: m[a] <= m[b]
def NO(a, b): return lambda m: not (m[a] & m[b])
def SOME(a, b): return lambda m: bool(m[a] & m[b])
def SOMENOT(a, b): return lambda m: bool(m[a] - m[b])
def ONLYFEW(a, b): return lambda m: bool(m[a] & m[b]) and bool(m[a] - m[b])


def syl(terms, prem, i1, p1, i2, p2, expect):
    """i1/i2: conclusion predicates as definite statements; p1/p2: same
    predicate used as a POSSIBILITY statement (True = consistent with
    premises). expect in onlyI/onlyII/both/neither/either."""
    def sat(m):
        return all(t and True for t in ()) or True

    def prem_ok(m):
        return all(m[t] for t in terms) and all(p(m) for p in prem)

    def ent(fn):
        return all(fn(m) for m in models_gen(terms) if prem_ok(m))

    def poss(fn):
        return any(fn(m) for m in models_gen(terms) if prem_ok(m))

    f1 = poss(i1) if p1 else ent(i1)
    f2 = poss(i2) if p2 else ent(i2)
    either = (not f1 and not f2
              and ent(lambda m: i1(m) or i2(m)))
    got = {('onlyI' if f1 and not f2 else 'onlyII' if f2 and not f1
            else 'both' if f1 and f2 else 'either' if either else 'neither')}
    assert expect in got, (expect, sorted(got), f1, f2, either)
    return f1, f2, either


subs = []

subs.append(C.sub(
    'syllogism-idea', 'What a syllogism is and how to test it',
    "A syllogism gives 2-3 'statements' taken as TRUE, plus conclusions that must be judged: do they follow necessarily? The four statement forms:\n\n- **All A are B** (A inside B, overlap allowed only as A ⊆ B).\n- **No A is B** (two disjoint circles).\n- **Some A are B** (circles overlap, with at least the overlap populated).\n- **Some A are not B** (A has at least one member outside B).\n\nThe bullet-proof method is the **minimal-diagram + test** method: draw the least-committal diagram that satisfies the statements (e.g. 'Some A are B' = two overlapping circles), then try to **violate** each conclusion while keeping the statements true. If some valid diagram violates the conclusion, it does NOT follow. A conclusion follows only when every valid diagram keeps it true. The classic error is drawing the diagram you *want* (drawing A inside B because a conclusion says so) — that proves nothing.",
    formulas=[
        C.F('Transitivity of All', 'A \\subset B \\wedge B \\subset C \\Rightarrow A \\subset C',
            "'All A are B + All B are C → All A are C' is the only freely chained rule."),
        C.F('Conversion of All', '\\text{All } A \\subset B \\Rightarrow \\text{Some } B \\subset A',
            "Valid (classes are assumed non-empty): 'Some B are A' follows."),
        C.F('Conversion of No / Some', '\\text{No } A \\cap B \\Leftrightarrow \\text{No } B \\cap A;\\quad \\text{Some } A \\cap B \\Leftrightarrow \\text{Some } B \\cap A',
            "Both convert symmetrically."),
    ],
    tricks=[
        C.T(
            'Hunt for one counter-diagram',
            "To kill a conclusion, you need just ONE diagram satisfying all statements that breaks it. Ask: 'can the two circles stay apart / can this element sit outside?' If yes, the conclusion fails.",
            "**Q.** Statements: Some pens are scales. Do 'Some scales are pens' and 'All scales are pens' follow?\n\n**Sol.** 'Some scales are pens' converts ✓. 'All scales are pens' — draw a scale outside every pen; statements still hold → does NOT follow.",
            "One violating diagram is enough to reject; demanding diagrams can never prove a conclusion."),
    ],
    mistakes=[
        "Drawing the conclusion's diagram instead of the statements'.",
        "Rejecting a conclusion only because it 'feels' strong — test it.",
        "Forgetting conversions: Some B are A follows from All A are B.",
    ]))

subs.append(C.sub(
    'possibility-cases', 'Possibility conclusions',
    "'X is a possibility' asks a different question: not 'is X forced?' but 'is X **consistent** with the statements?'. A possibility conclusion **follows** if you can draw even ONE diagram satisfying the statements where X also holds; it fails only when the statements make X impossible.\n\nSo 'All A being B is a possibility' usually follows unless a statement explicitly blocks it (typically a 'No' statement cutting across). Read carefully: a definite conclusion ('All A are B') needs to hold in **every** diagram; a possibility conclusion needs to hold in **at least one**.",
    tricks=[
        C.T(
            'One supporting diagram wins for possibility',
            "For possibility conclusions, flip your thinking: you are now the defence lawyer. Build one diagram where the possibility is true alongside all statements — done, it follows.",
            "**Q.** Statements: All keys are metal. Some metal is rusty. 'All rusty things being keys is a possibility' — follows?\n\n**Sol.** Draw rusty ⊆ keys, keys ⊆ metal, and a second metal piece outside keys. All statements + possibility hold → **follows**.",
            "Definite = survive every diagram; possibility = survive in one diagram."),
    ],
    mistakes=[
        "Testing a possibility conclusion like a definite one (demanding it hold everywhere).",
        "Declaring a possibility false when a 'No' statement doesn't actually touch the terms.",
    ]))

subs.append(C.sub(
    'either-or', 'Either-or (complementary pairs)',
    "When neither conclusion follows individually, check whether the two form a **complementary pair** — two statements that together cover every case and never fail simultaneously:\n\n- **(All A are B) + (Some A are not B)**\n- **(Some A are B) + (No A is B)**\n\nBoth pairs are exact negations of each other. If neither follows on its own but the statements cannot break both at once, the answer is **'Either I or II follows'**. Note the trap: 'Some A are not B' pairs with 'All A are B' — NOT with 'No A is B'.",
    tricks=[
        C.T(
            'Spot the negation pair',
            "Scan the two conclusions for the word pairs (All … , Some … not) or (Some … , No …) about the SAME two terms. If found and neither follows individually, mark either-or — no diagram needed.",
            "**Q.** Conclusions: I. Some shirts are red. II. No shirt is red.\n\n**Sol.** Same terms, Some/No pair, neither provable from 'Some shirts are blue'-type statements → **either-or**.",
            "Complementary pair = exact logical negations about the same two terms."),
    ],
    mistakes=[
        "Pairing 'No A is B' with 'Some A are not B' — they are not negations.",
        "Marking either-or when one conclusion already follows on its own.",
    ]))

subs.append(C.sub(
    'definite-cases', 'Only-a-few and definite-case rulings',
    "Two high-frequency modern patterns:\n\n- **Only a few A are B** = 'Some A are B' **and** 'Some A are not B' — both at once. It is stronger than 'some': the part of A outside B is guaranteed. (It says nothing about B outside A.)\n- **A few / Many A are B** = plain 'Some A are B'.\n\nConsequences worth memorising: from 'Only a few A are B', the conclusions 'Some A are not B' and 'Some A are B' both follow; 'All A are B' does not.",
    tricks=[
        C.T(
            "Split 'only a few' on sight",
            "Rewrite every 'Only a few A are B' as two arrows — ✓Some A are B, ✓Some A are not B — and feed both into your diagram. Everything else is ordinary syllogism.",
            "**Q.** Only a few cups are plates. All plates are bowls. Does 'Some cups are not bowls' follow?\n\n**Sol.** The cup outside plates: is it outside bowls? Not necessarily — plates aren't all the bowls... the non-plate cup may still be a bowl → does NOT follow.",
            "The guaranteed non-B cup is not automatically a non-bowl."),
    ],
    mistakes=[
        "Reading 'Only a few A are B' as 'No A is B' or as plain 'Some'.",
        "Adding 'All B are A' to 'Only a few A are B' — not implied.",
    ]))

patterns = [
    C.P('Two-statement definite', 'very common',
        "Classic 2 statements + 2 conclusions (Some/No/All mixtures).",
        "Minimal diagram, then hunt counter-diagrams for each conclusion."),
    C.P('Three-statement chain', 'common',
        "A chained 'All' plus a crossing 'Some/No'.",
        "Chain the All-links first; place the Some/No statement last."),
    C.P('Possibility conclusion', 'very common',
        "'… is a possibility' phrasing.",
        "Find one diagram supporting it; blocked only by No-statements crossing the terms."),
    C.P('Either-or complementary pair', 'very common',
        "Neither follows alone; conclusions are negation pairs.",
        "(All, Some-not) or (Some, No) about the same terms → either-or."),
    C.P('Only-a-few statements', 'common',
        "'Only a few A are B' phrasing.",
        "Split into Some A are B + Some A are not B, then solve normally."),
    C.P('Conversion-based conclusion', 'occasional',
        "Correct conclusion is the reversed 'Some B are A'.",
        "Remember All→Some and No/Some reversals before rejecting."),
]

examples = []

# ex1: neither follows
syl(['teachers', 'graduates', 'postgrads'],
    [ALL('teachers', 'graduates'), SOME('graduates', 'postgrads')],
    SOME('teachers', 'postgrads'), False, ALL('graduates', 'teachers'), False,
    'neither')
examples.append(C.Q(
    'rsn-syllogism-ex1',
    "**Statements:** All teachers are graduates. Some graduates are postgraduates.\n\n**Conclusions:** I. Some teachers are postgraduates. II. All graduates are teachers.",
    ['Neither I nor II follows', 'Only I follows', 'Only II follows', 'Both I and II follow'],
    'Neither I nor II follows',
    "Minimal diagram: teachers inside graduates; postgraduates overlapping graduates — possibly away from teachers. That diagram breaks I, so I fails. Postgraduates outside graduates breaks II's premise-side... more directly, graduates extend beyond teachers, so II fails too. **Neither follows.**",
    sc="Overlap the 'some' circle away from the 'All' circle — that one diagram kills conclusion I; the All arrow never reverses for II.",
    d='easy', sub='syllogism-idea', pat='two-statement definite', t=40))

# ex2: both follow (chain + conversion)
syl(['roses', 'flowers', 'plants'],
    [ALL('roses', 'flowers'), ALL('flowers', 'plants')],
    ALL('roses', 'plants'), False, SOME('plants', 'roses'), False,
    'both')
examples.append(C.Q(
    'rsn-syllogism-ex2',
    "**Statements:** All roses are flowers. All flowers are plants.\n\n**Conclusions:** I. All roses are plants. II. Some plants are roses.",
    ['Both I and II follow', 'Only I follows', 'Only II follows', 'Neither follows'],
    'Both I and II follow',
    "Chain the All's: roses ⊂ flowers ⊂ plants → I follows. Roses are non-empty and sit inside plants, so some plants are roses → II follows. **Both follow.**",
    sc="All-chains carry forward, and 'All A are B' always gifts you 'Some B are A'.",
    d='easy', sub='syllogism-idea', pat='conversion-based conclusion', t=40))

# ex3: either-or
syl(['mangoes', 'sweets'],
    [SOME('mangoes', 'sweets')],
    ALL('mangoes', 'sweets'), False, SOMENOT('mangoes', 'sweets'), False,
    'either')
examples.append(C.Q(
    'rsn-syllogism-ex3',
    "**Statement:** Some mangoes are sweet.\n\n**Conclusions:** I. All mangoes are sweet. II. Some mangoes are not sweet.",
    ['Either I or II follows', 'Only I follows', 'Only II follows', 'Neither follows'],
    'Either I or II follows',
    "I and II are exact negations of each other, so at least one must be true — but the statement alone fixes neither. **Either I or II follows.**",
    sc="(All …) + (Some … not) on the same terms with no individual proof = either-or.",
    d='easy', sub='either-or', pat='either-or complementary pair', t=35))

# ex4: possibility
syl(['doors', 'wooden', 'brown'],
    [ALL('doors', 'wooden'), SOME('wooden', 'brown')],
    ALL('doors', 'brown'), True, NO('doors', 'brown'), False,
    'onlyI')
examples.append(C.Q(
    'rsn-syllogism-ex4',
    "**Statements:** All doors are wooden. Some wooden things are brown.\n\n**Conclusions:** I. All doors being brown is a possibility. II. No door is brown.",
    ['Only I follows', 'Only II follows', 'Both follow', 'Neither follows'],
    'Only I follows',
    "I: draw doors inside the brown part of wooden — every statement still holds, so the possibility is consistent → I follows. II: the diagram just built breaks it, and nothing forces doors away from brown either. **Only I follows.**",
    sc="Possibility = one supporting diagram; II's 'No' isn't forced by anything.",
    d='medium', sub='possibility-cases', pat='possibility conclusion', t=50))

# ---------------------------------------------------------------- practice
pr = []
OPT = ['Only conclusion I follows', 'Only conclusion II follows',
       'Both conclusions follow', 'Neither conclusion follows']
OPT_E = ['Either conclusion I or II follows', 'Only conclusion I follows',
         'Only conclusion II follows', 'Neither conclusion follows']

# 1: both follow
syl(['pens', 'books', 'copies'],
    [ALL('pens', 'books'), ALL('books', 'copies')],
    ALL('pens', 'copies'), False, SOME('copies', 'pens'), False, 'both')
pr.append(C.Q(
    'rsn-syllogism-1',
    "**Statements:** All pens are books. All books are copies.\n\n**Conclusions:** I. All pens are copies. II. Some copies are pens.",
    OPT, 'Both conclusions follow',
    "pens ⊂ books ⊂ copies gives I. Since pens exist inside copies, II follows too. **Both.**",
    sc="All-chain forward + the free 'Some' reversal.",
    d='easy', sub='syllogism-idea', pat='three-statement chain', t=40))

# 2: only I
syl(['dogs', 'cats', 'rats'],
    [SOME('dogs', 'cats'), ALL('cats', 'rats')],
    SOME('dogs', 'rats'), False, ALL('rats', 'dogs'), False, 'onlyI')
pr.append(C.Q(
    'rsn-syllogism-2',
    "**Statements:** Some dogs are cats. All cats are rats.\n\n**Conclusions:** I. Some dogs are rats. II. All rats are dogs.",
    OPT, 'Only conclusion I follows',
    "The dog-cat overlap sits inside rats, so some dogs are rats — I follows. Rats spread beyond dogs, so II fails. **Only I.**",
    sc="Drop the shared element of a Some+All chain into the third term.",
    d='easy', sub='syllogism-idea', pat='two-statement definite', t=40))

# 3: only I
syl(['glass', 'metal', 'solids'],
    [NO('glass', 'metal'), SOME('metal', 'solids')],
    SOMENOT('solids', 'glass'), False, ALL('glass', 'solids'), False, 'onlyI')
pr.append(C.Q(
    'rsn-syllogism-3',
    "**Statements:** No glass is metal. Some metals are solids.\n\n**Conclusions:** I. Some solids are not glass. II. All glasses are solids.",
    OPT, 'Only conclusion I follows',
    "The solid that is metal cannot be glass (glass and metal never meet) → some solids are not glass: I follows. Glass has no forced link with solids → II fails. **Only I.**",
    sc="A 'Some metal are solid' element inherits metal's full exile from glass.",
    d='medium', sub='syllogism-idea', pat='two-statement definite', t=45))

# 4: either-or
syl(['flowers', 'red', 'blue'],
    [SOME('flowers', 'red'), NO('flowers', 'blue')],
    ALL('flowers', 'red'), False, SOMENOT('flowers', 'red'), False, 'either')
pr.append(C.Q(
    'rsn-syllogism-4',
    "**Statements:** Some flowers are red. No flower is blue.\n\n**Conclusions:** I. All flowers are red. II. Some flowers are not red.",
    OPT_E, 'Either conclusion I or II follows',
    "The red part of flowers isn't fixed as all or some-not, so neither conclusion is provable — but they are exact negations, so one of them must hold. **Either-or.**",
    sc="(All, Some-not) pair on the same terms = complementary.",
    d='medium', sub='either-or', pat='either-or complementary pair', t=45))

# 5: either-or (Some/No pair)
syl(['cars', 'buses', 'trucks'],
    [ALL('cars', 'buses'), SOME('trucks', 'buses')],
    SOME('cars', 'trucks'), False, NO('cars', 'trucks'), False, 'either')
pr.append(C.Q(
    'rsn-syllogism-5',
    "**Statements:** All cars are buses. Some trucks are buses.\n\n**Conclusions:** I. Some cars are trucks. II. No car is a truck.",
    OPT_E, 'Either conclusion I or II follows',
    "Cars sit inside buses, trucks somewhere in buses too — but the statements never fix whether cars meet trucks. I and II are exact negations of each other, so they cannot both fail. **Either-or.**",
    sc="Same two terms, (Some …) vs (No …), neither provable → complementary pair.",
    d='medium', sub='either-or', pat='either-or complementary pair', t=50))

# 6: only II (possibility blocked + derived some-not)
syl(['apples', 'mangoes', 'bananas'],
    [SOME('apples', 'mangoes'), NO('mangoes', 'bananas')],
    ALL('apples', 'bananas'), True, SOMENOT('apples', 'bananas'), False,
    'onlyII')
pr.append(C.Q(
    'rsn-syllogism-6',
    "**Statements:** Some apples are mangoes. No mango is a banana.\n\n**Conclusions:** I. All apples being bananas is a possibility. II. Some apples are not bananas.",
    OPT, 'Only conclusion II follows',
    "I: an apple-mango element can never be a banana, so filling all apples into bananas is impossible → I fails. II: that same apple-mango element is an apple outside bananas → II follows. **Only II.**",
    sc="The shared 'Some' element must obey BOTH statements — trace it through.",
    d='hard', sub='possibility-cases', pat='possibility conclusion', t=65))

# 7: only I (possibility)
syl(['roads', 'streets', 'lanes'],
    [ALL('roads', 'streets'), SOME('streets', 'lanes')],
    ALL('lanes', 'roads'), True, SOMENOT('lanes', 'streets'), False, 'onlyI')
pr.append(C.Q(
    'rsn-syllogism-7',
    "**Statements:** All roads are streets. Some streets are lanes.\n\n**Conclusions:** I. All lanes being roads is a possibility. II. Some lanes are not streets.",
    OPT, 'Only conclusion I follows',
    "I: draw lanes inside roads (roads inside streets) — consistent with both statements → possibility holds. II: the lane-street overlap may cover all lanes, so II isn't forced. **Only I.**",
    sc="Possibility needs one friendly diagram; here nothing blocks it.",
    d='medium', sub='possibility-cases', pat='possibility conclusion', t=55))

# 8: only II (3-statement)
syl(['keys', 'locks', 'doors', 'windows'],
    [ALL('keys', 'locks'), SOME('locks', 'doors'), NO('doors', 'windows')],
    SOME('keys', 'doors'), False, SOMENOT('locks', 'windows'), False, 'onlyII')
pr.append(C.Q(
    'rsn-syllogism-8',
    "**Statements:** All keys are locks. Some locks are doors. No door is a window.\n\n**Conclusions:** I. Some keys are doors. II. Some locks are not windows.",
    OPT, 'Only conclusion II follows',
    "I: the lock-door overlap can sit outside the keys region → not forced. II: the lock that is a door cannot be a window → that lock is 'a lock not a window' → follows. **Only II.**",
    sc="Carry the Some-element through both of its statements before judging.",
    d='hard', sub='syllogism-idea', pat='three-statement chain', t=70))

# 9: only I (only a few)
syl(['cups', 'plates', 'bowls'],
    [ONLYFEW('cups', 'plates'), ALL('plates', 'bowls')],
    SOMENOT('cups', 'plates'), False,
    NO('cups', 'bowls'), False, 'onlyI')
pr.append(C.Q(
    'rsn-syllogism-9',
    "**Statements:** Only a few cups are plates. All plates are bowls.\n\n**Conclusions:** I. Some cups are not plates. II. No cup is a bowl.",
    OPT, 'Only conclusion I follows',
    "'Only a few' guarantees a part of cups outside plates → I follows. The non-plate cups may still be bowls, and the plate-cups ARE bowls — so II fails. **Only I.**",
    sc="Only a few = Some + Some-not, nothing about the other circle.",
    d='medium', sub='definite-cases', pat='only-a-few statements', t=55))

# 10: only II (possibility)
syl(['chairs', 'tables', 'desks'],
    [ALL('chairs', 'tables'), SOME('tables', 'desks')],
    SOME('chairs', 'desks'), False, ALL('desks', 'chairs'), True, 'onlyII')
pr.append(C.Q(
    'rsn-syllogism-10',
    "**Statements:** All chairs are tables. Some tables are desks.\n\n**Conclusions:** I. Some chairs are desks. II. All desks being chairs is a possibility.",
    OPT, 'Only conclusion II follows',
    "I: the table-desk overlap can avoid chairs entirely → fails. II: desks can be drawn inside chairs (chairs inside tables) — fully consistent → possibility follows. **Only II.**",
    sc="Possibility: try to draw it; only a crossing 'No' can stop you.",
    d='medium', sub='possibility-cases', pat='possibility conclusion', t=55))

# 11: only II (possibility survives a No statement)
syl(['pages', 'files', 'folders'],
    [SOME('pages', 'files'), NO('files', 'folders')],
    SOME('pages', 'folders'), False, ALL('pages', 'files'), True, 'onlyII')
pr.append(C.Q(
    'rsn-syllogism-11',
    "**Statements:** Some pages are files. No file is a folder.\n\n**Conclusions:** I. Some pages are folders. II. All pages being files is a possibility.",
    OPT, 'Only conclusion II follows',
    "I: pages outside files can sit inside folders, and the file-pages cannot — so 'some pages are folders' is possible but not necessary → not a definite follow. II: all pages inside files keeps every statement true → possibility follows. **Only II.**",
    sc="A possibility can hold for a part no statement pins down.",
    d='hard', sub='possibility-cases', pat='possibility conclusion', t=65))

# 12: either-or (3 statements)
syl(['rings', 'circles', 'squares', 'triangles'],
    [ALL('rings', 'circles'), SOME('circles', 'squares'), NO('squares', 'triangles')],
    SOME('circles', 'triangles'), False, NO('circles', 'triangles'), False,
    'either')
pr.append(C.Q(
    'rsn-syllogism-12',
    "**Statements:** All rings are circles. Some circles are squares. No square is a triangle.\n\n**Conclusions:** I. Some circles are triangles. II. No circle is a triangle.",
    OPT_E, 'Either conclusion I or II follows',
    "Neither I nor II is forced (circles may or may not touch triangles). They are negation pairs about circles-triangles, so they can't both fail. **Either-or.**",
    sc="Even with three statements, the pair test only needs the two conclusion terms.",
    d='hard', sub='either-or', pat='either-or complementary pair', t=65))

# 13: only I
syl(['numbers', 'letters', 'symbols', 'digits'],
    [SOME('numbers', 'letters'), ALL('letters', 'symbols'), NO('symbols', 'digits')],
    SOMENOT('numbers', 'digits'), False, ALL('letters', 'digits'), False,
    'onlyI')
pr.append(C.Q(
    'rsn-syllogism-13',
    "**Statements:** Some numbers are letters. All letters are symbols. No symbol is a digit.\n\n**Conclusions:** I. Some numbers are not digits. II. All letters are digits.",
    OPT, 'Only conclusion I follows',
    "A number-letter element is a letter → symbol → never a digit → I follows. II collides head-on with 'No symbol is a digit' → fails. **Only I.**",
    sc="One shared element propagated through three statements settles I.",
    d='medium', sub='syllogism-idea', pat='three-statement chain', t=60))

# 14: both follow (surprising Some-not)
syl(['squares', 'rectangles', 'circles'],
    [ALL('squares', 'rectangles'), NO('rectangles', 'circles')],
    NO('squares', 'circles'), False, SOMENOT('circles', 'squares'), False,
    'both')
pr.append(C.Q(
    'rsn-syllogism-14',
    "**Statements:** All squares are rectangles. No rectangle is a circle.\n\n**Conclusions:** I. No square is a circle. II. Some circles are not squares.",
    OPT, 'Both conclusions follow',
    "Squares live inside rectangles, and rectangles never meet circles → no square meets a circle: I follows. Circles are non-empty and entirely outside rectangles, hence entirely outside squares → at least one circle is not a square: II follows too. **Both.**",
    sc="A full exile (No) plus non-emptiness gives you a free 'Some … not' conclusion.",
    d='hard', sub='syllogism-idea', pat='two-statement definite', t=70))

# 15: only II (only a few + possibility)
syl(['villages', 'towns', 'cities'],
    [ALL('villages', 'towns'), ONLYFEW('towns', 'cities')],
    SOME('villages', 'cities'), False, ALL('villages', 'cities'), True,
    'onlyII')
pr.append(C.Q(
    'rsn-syllogism-15',
    "**Statements:** All villages are towns. Only a few towns are cities.\n\n**Conclusions:** I. Some villages are cities. II. All villages being cities is a possibility.",
    OPT, 'Only conclusion II follows',
    "I: the town-city overlap can sit entirely outside the villages → not forced. II: villages can be drawn inside the city-part of towns — consistent with 'only a few' (some towns stay outside cities) → possibility follows. **Only II.**",
    sc="'Only a few' says the city-part is small, never where your subject sits.",
    d='hard', sub='definite-cases', pat='only-a-few statements', t=70))

assert len(pr) == 15

t = C.topic(
    'syllogism', 'Syllogism', 'high', {'tier1': '3-5', 'tier2': '4-6'},
    "Syllogism questions hand you 2-3 statements (All / No / Some / Some-not / Only-a-few) as true and ask which conclusions follow. The reliable method is minimal-diagram plus counter-example hunting: draw the least-committal picture, then try to break each conclusion — a conclusion follows only if no valid diagram breaks it. Modern twists (possibility conclusions, either-or complementary pairs, 'only a few') all reduce to the same discipline with one twist: possibility needs just one supporting diagram, and either-or needs the two conclusions to be exact negations.",
    subs, patterns, examples, pr)

C.write_topic(t)
print('OK syllogism')
