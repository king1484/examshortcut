# build direction-distance topic (topic 8)
import math
import common as C
import engines as E


def dist(p):
    return math.hypot(p[0], p[1])


def km(v):
    return '%s km' % v


def m(v):
    return '%s m' % v


def heading_after(start, turns):
    """turns: list of ('CW'|'ACW'|'ABOUT', n)"""
    cw = ['N', 'E', 'S', 'W']
    d = start
    for t, n in turns:
        if t == 'ABOUT':
            d = cw[(cw.index(d) + 2) % 4]
        elif t == 'CW':
            d = cw[(cw.index(d) + n) % 4]
        else:
            d = cw[(cw.index(d) - n) % 4]
    return d


subs = []

subs.append(C.sub(
    'direction-idea', 'Direction conventions and displacement',
    "Direction questions track a walker on an invisible grid. Fix the conventions first:\n\n- **North is up, East is right**, South down, West left; North-East sits between North and East, and so on for the four diagonal directions.\n- **Facing North:** left = West, right = East. **Facing South:** left = East, right = West. (A 'left turn' depends on where you face — this is the number-one trap.)\n- 'Towards the sunrise' = **East**; 'towards the sunset' = **West**.\n- The **shortest distance** from start is the straight line joining start to finish — never the sum of the legs walked.\n\nComputationally: assign each leg a horizontal and vertical component (North: +y, South: −y, East: +x, West: −x), add them up, and apply Pythagoras:\n\n$$\\text{shortest distance} = \\sqrt{x^2 + y^2}$$\n\nMost CGL answers are Pythagorean triples — 3-4-5, 6-8-10, 5-12-13, 9-12-15 — so a clean square root usually means you are on track.",
    formulas=[
        C.F('Shortest distance', 'd = \\sqrt{x^2 + y^2}', 'x = net east-west movement, y = net north-south movement.'),
        C.F('Triple shortcut', '3\\text{-}4\\text{-}5 \\times k', 'Legs (3k, 4k) give distance 5k: check 6-8-10, 9-12-15, 12-16-20.'),
        C.F('Turn directions', '\\text{left/right} = \\text{facing}\\pm90^\\circ', 'Left/right are relative to current facing; about-turn is 180°.'),
    ],
    tricks=[
        C.T(
            'Two-axis bookkeeping',
            "Keep two running totals: EAST-WEST and NORTH-SOUTH. East and West cancel each other; North and South cancel each other. The endpoint is (EW, NS) and distance is the square root of the sum of squares.",
            "**Q.** 8 km east, 6 km west, 3 km east — how far from start?\n\n**Sol.** EW: +8 − 6 + 3 = +5; NS: 0. Distance = **5 km, East**. (17 km is the total walked, not the displacement.)",
            "Signed totals per axis; everything else is one square root."),
        C.T(
            'Triple recognition',
            "When the two net components come out as 3k and 4k (any order), the answer is 5k with no calculation: (6, 8) → 10, (9, 12) → 15, (12, 5) → 13.",
            "**Q.** 6 m east, then right and 8 m south. Distance from start?\n\n**Sol.** (6, 8) = 2×(3, 4) → **10 m**.",
            "Scan for a multiple of 3-4-5 or 5-12-13 before touching a square root."),
    ],
    mistakes=[
        "Adding the legs (total path) instead of the straight-line displacement.",
        "Turning left/right as if absolute (facing South, 'left' is East, not West).",
        "Mixing the order of components — direction of the displacement needs its correct sign on each axis.",
    ]))

subs.append(C.sub(
    'final-direction', 'Direction faced and net direction',
    "Two sub-formats:\n\n1. **Which direction is X facing now?** — pure turn-tracking. A clock-wise turn of 90° maps N→E→S→W→N; anticlockwise runs N→W→S→E→N. An about-turn adds 180°. Turn, update the heading, repeat.\n2. **In which direction is the endpoint from the start?** — finish the walk, note the final (x, y), and read the direction from signs: (+x, +y) = North-East, (−x, +y) = North-West, (+x, −y) = South-East, (−x, −y) = South-West; a zero component drops that word.\n\nBoth take seconds *if* you write the heading after every turn instead of trusting memory across three turns.",
    formulas=[
        C.F('Clockwise cycle', 'N \\to E \\to S \\to W \\to N', 'Every right turn moves one step along this cycle.'),
        C.F('Anticlockwise cycle', 'N \\to W \\to S \\to E \\to N', 'Every left turn moves one step along this cycle.'),
        C.F('Sign reading', '(x>0,y>0) \\Rightarrow NE', 'Signs of the net components give the quadrant.'),
    ],
    tricks=[
        C.T(
            'Write the heading down each time',
            "After every turn, overwrite a single letter (N/E/S/W). Three written letters beat one mental chain — and if a wrong option appears, each written heading is checkable.",
            "**Q.** Facing West, a man turns 90° clockwise, then 180° anticlockwise. Final facing?\n\n**Sol.** W --90° CW--> N --180° ACW--> **South**.",
            "One letter, overwritten per turn."),
    ],
    mistakes=[
        "Applying 'left = West' regardless of current facing.",
        "Counting a 180° turn as two separate questions' worth of turns.",
        "Reading the *final facing* when the question asks direction-from-start (or vice versa).",
    ]))

subs.append(C.sub(
    'shadow-direction', 'Shadow questions',
    "The sun's position fixes the shadow:\n\n- **Morning:** sun in the **East** → every shadow points **West**.\n- **Evening:** sun in the **West** → every shadow points **East**.\n- At local noon (in India) the shadow points roughly **North**.\n\nThe standard phrasings, decoded:\n\n- 'Shadow falls **behind** him' → he faces **opposite** the shadow.\n- 'Shadow falls **in front / towards him**' → he faces **along** the shadow.\n- 'Shadow to his **left/right**' → he faces perpendicular, on the stated side.\n\nConvert to a sentence about facing first, then run the walk. Do not skip the conversion — answering 'which way is the shadow' instead of 'which way is he facing' is the classic half-error.",
    tricks=[
        C.T(
            'One-line conversion',
            "Rewrite the shadow sentence as a facing sentence before doing anything else: morning + behind = facing East; evening + in front = facing East; morning + shadow on the left = facing South (shadow West is on the left of a South-facing person).",
            "**Q.** One evening, Ramesh's shadow falls exactly in front of him. Which direction is he facing?\n\n**Sol.** Evening shadow points East; shadow in front means he faces along it → **East**.",
            "Shadow sentence → facing sentence → answer. Three words per step."),
    ],
    mistakes=[
        "Using the evening shadow direction (East) in a morning question.",
        "Answering the shadow's direction instead of the person's facing.",
        "Forgetting shadow-left/right flips when the facing flips.",
    ]))

subs.append(C.sub(
    'relative-position', 'Position of one point from another',
    "'C is 5 km East of A; A is 2 km North of B — in which direction is C from B?' Two anchored statements chain into one picture: place the *reference* person first (B), attach A relative to B, then C relative to A. The answer is read straight from the sketch.\n\nCare points:\n\n- **Direction reverses with reference**: 'C from B' (C relative to B) is the opposite corner of 'B from C'.\n- Distances may be enough for a diagonal ('how far is C from B?' → Pythagoras on the two components).\n- With three or more people, name the sketch's axes once (up = North) and place everyone before answering anything.",
    tricks=[
        C.T(
            'Place the final reference first',
            "Start the sketch with the person the question asks FROM ('direction of C from B' → draw B at origin), then attach the chain. The answer is simply where C lands on the page.",
            "**Q.** A is 5 km North of B; C is 5 km East of A. Direction of C from B?\n\n**Sol.** B at origin → A above it → C to A's right: C sits 5 East, 5 North of B → **North-East**.",
            "Anchor at the asked-from person; the chain then hangs downward."),
    ],
    mistakes=[
        "Drawing A first when B is the asked-from reference.",
        "Reporting 'C from B' when the question asked 'B from C'.",
        "Adding distances that need Pythagoras instead.",
    ]))

patterns = [
    C.P('Shortest distance between start and finish', 'very common',
        "A multi-leg walk; 'how far is he from the starting point?'",
        "Net components per axis, then Pythagoras; look for a 3-4-5 multiple."),
    C.P('Direction of the endpoint from start', 'very common',
        "A walk with left/right turns; 'in which direction is he from the start?'",
        "Track (x, y) signs at the endpoint; quadrant names the direction."),
    C.P('Final facing after turns', 'common',
        "'Facing X, turns right, then about turn...' — which way now?",
        "Cycle N→E→S→W (right); write the heading after every turn."),
    C.P('Shadow-based facing', 'common',
        "Morning/evening shadow behind/in front/left — find the facing.",
        "Shadow points West in the morning, East in the evening; convert to a facing sentence."),
    C.P('Relative position of two people', 'common',
        "'A is 5 km north of B; C is 3 km east of A — direction of C from B?'",
        "Sketch with the asked-from person at the origin; read off the quadrant."),
    C.P('Distance between two walkers', 'occasional',
        "Two people start together, walk different routes; find the gap.",
        "Compute both endpoints from the same origin, then the distance between them."),
]

examples = []

# ex1: 3-4-5
p = E.walk('N', [('F', 3), ('R', 4)])
assert p == (4, 3, 'E') and dist(p) == 5
examples.append(C.Q(
    'rsn-direction-ex1',
    "**Ravi walks 3 km towards North, turns right and walks 4 km.** How far is he from the starting point?",
    ['5 km', '7 km', '1 km', '6 km'], '5 km',
    "North 3 km, then right (East) 4 km: components (4, 3). Shortest distance = √(4² + 3²) = √25 = **5 km**. (7 km is the distance walked — not asked.)",
    sc="(3, 4) legs are the 3-4-5 triple — the answer is 5 without computing.",
    d='easy', sub='direction-idea', pat='shortest distance between start and finish', t=35))

# ex2: endpoint direction
p = E.walk('S', [('F', 5), ('L', 3), ('L', 5)])
assert p == (3, 0, 'N'), p
examples.append(C.Q(
    'rsn-direction-ex2',
    "**Maya walks 5 km South, turns left and walks 3 km, then turns left and walks 5 km.** In which direction is she from the starting point?",
    ['East', 'West', 'North', 'South'], 'East',
    "South 5 → (0, −5). Facing South, left = East: +3 → (3, −5). Facing East, left = North: +5 → (3, 0). The y-components cancelled; she is **3 km East** of the start.",
    sc="Opposite legs of equal length cancel — only the East 3 km survives.",
    d='easy', sub='final-direction', pat='direction of the endpoint from start', t=40))

# ex3: shadow morning
examples.append(C.Q(
    'rsn-direction-ex3',
    "One morning, a man starts walking and his **shadow falls exactly behind him**. Which direction is he facing?",
    ['East', 'West', 'North', 'South'], 'East',
    "In the morning the sun is in the East, so every shadow points **West**. A shadow falling behind him means his back is to the West — he faces **East**.",
    sc="Morning shadow = West; 'behind' ⇒ face opposite the shadow.",
    d='easy', sub='shadow-direction', pat='shadow-based facing', t=30))

# ex4: relative direction
examples.append(C.Q(
    'rsn-direction-ex4',
    "**P is 4 km East of Q. R is 3 km South of P.** In which direction is **R from Q**?",
    ['South-East', 'North-East', 'South-West', 'East'], 'South-East',
    "Put Q at the origin: P is (+4, 0), R is (+4, −3). Both x and y components are non-zero, signs (+, −) → **South-East** (exactly 5 km away, by the triple).",
    sc="Anchor at Q (the asked-from point); R lands in the (+, −) quadrant.",
    d='easy', sub='relative-position', pat='relative position of two people', t=35))

# ---------------------------------------------------------------- practice
pr = []

# 1: 6-8-10
p = E.walk('E', [('F', 6), ('R', 8)])
assert p == (6, -8, 'S') and dist(p) == 10
pr.append(C.Q(
    'rsn-direction-1',
    "**Asha walks 6 m towards East, turns right and walks 8 m.** How far is she from the starting point?",
    ['10 m', '14 m', '2 m', '12 m'], '10 m',
    "Components (6, 8) = 2 × (3, 4) → distance = 2 × 5 = **10 m**. (14 m is the path walked.)",
    sc="6-8 is the doubled 3-4 triple → 10.",
    d='easy', sub='direction-idea', pat='shortest distance between start and finish', t=30))

# 2: 9-12-15
p = E.walk('S', [('F', 9), ('R', 12)])
assert p == (-12, -9, 'W') and dist(p) == 15
pr.append(C.Q(
    'rsn-direction-2',
    "**Vikram walks 9 km towards South, then turns right and walks 12 km.** How far is he from the start?",
    ['15 km', '21 km', '3 km', '18 km'], '15 km',
    "Components (12, 9) = 3 × (4, 3) → distance = 3 × 5 = **15 km**.",
    sc="9-12 legs → 15 by the triple; no square root needed.",
    d='easy', sub='direction-idea', pat='shortest distance between start and finish', t=30))

# 3: out-and-back rectangle
p = E.walk('N', [('F', 12), ('R', 5), ('R', 12)])
assert p == (5, 0, 'S') and dist(p) == 5
pr.append(C.Q(
    'rsn-direction-3',
    "**Neha walks 12 m North, turns right and walks 5 m, then turns right and walks 12 m.** How far is she from the starting point?",
    ['5 m', '29 m', '17 m', '24 m'], '5 m',
    "North 12 and South 12 cancel completely; only the East 5 m remains → **5 m**. (29 m is the total distance walked.)",
    sc="Equal out-and-back legs on one axis vanish; only the crosswise leg survives.",
    d='easy', sub='direction-idea', pat='shortest distance between start and finish', t=35))

# 4: turns only
h = heading_after('W', [('CW', 1), ('ACW', 2)])
assert h == 'S', h
pr.append(C.Q(
    'rsn-direction-4',
    "A man facing **West turns 90° clockwise, then 180° anticlockwise**. Which direction is he facing now?",
    ['South', 'East', 'North', 'West'], 'South',
    "West --90° clockwise--> North --180°--> **South**. A 180° turn flips the heading whatever its sense.",
    sc="Write the heading after each turn: W → N → S.",
    d='easy', sub='final-direction', pat='final facing after turns', t=30))

# 5: relative NE
pr.append(C.Q(
    'rsn-direction-5',
    "**A is 5 km North of B. C is 5 km East of A.** In which direction is **C from B**?",
    ['North-East', 'South-East', 'North-West', 'East'], 'North-East',
    "B at origin → A at (0, 5) → C at (5, 5). Both components positive → **North-East** of B (7.07 km away, if asked).",
    sc="Chain from B, the asked-from point: up 5, right 5 → NE.",
    d='easy', sub='relative-position', pat='relative position of two people', t=30))

# 6: signed totals
assert E.walk('E', [('F', 8), ('A', 'W', 6), ('A', 'E', 3)])[:2] == (5, 0)
pr.append(C.Q(
    'rsn-direction-6',
    "**Sameer walks 8 km East, then 6 km West, then 3 km East.** How far is he from the starting point?",
    ['5 km', '17 km', '11 km', '2 km'], '5 km',
    "Net East = 8 − 6 + 3 = 5 km; net North–South = 0 → **5 km East**. (17 km is the walking total.)",
    sc="One signed column for East-West; opposite directions subtract.",
    d='easy', sub='direction-idea', pat='shortest distance between start and finish', t=30))

# 7: evening shadow in front
pr.append(C.Q(
    'rsn-direction-7',
    "In the **evening**, Ramesh's shadow falls **exactly in front of him**. Which direction is he facing?",
    ['East', 'West', 'North', 'South'], 'East',
    "Evening sun is in the West, so shadows point **East**. A shadow in front means he faces along it → **East**.",
    sc="Evening shadow = East; 'in front' ⇒ facing the shadow's direction.",
    d='easy', sub='shadow-direction', pat='shadow-based facing', t=30))

# 8: three legs, direction from start
p = E.walk('S', [('F', 4), ('L', 4), ('L', 4)])
assert p == (4, 0, 'N'), p
pr.append(C.Q(
    'rsn-direction-8',
    "**Facing South, Sita walks 4 km, turns left and walks 4 km, then turns left again and walks 4 km.** In which direction is her endpoint from the start?",
    ['East', 'North', 'North-East', 'West'], 'East',
    "South 4 → (0, −4). Facing South, left = East → (4, −4). Facing East, left = North → (4, 0). Net: **4 km East**.",
    sc="The two South-North legs cancel; the middle leg decides.",
    d='medium', sub='final-direction', pat='direction of the endpoint from start', t=40))

# 9: two walkers
px = E.walk('N', [('F', 3), ('R', 4)])[:2]
py = E.walk('S', [('F', 4), ('R', 3)])[:2]
gap = dist((px[0] - py[0], px[1] - py[1]))
assert (px, py) == ((4, 3), (-3, -4)) and abs(gap - 9.899) < 0.01
pr.append(C.Q(
    'rsn-direction-9',
    "Two friends start from the same point. **X walks 3 km North and then 4 km East. Y walks 4 km South and then 3 km West.** How far apart are they now?",
    ['9.9 km', '7 km', '14 km', '5 km'], '9.9 km',
    "X is at (+4, +3); Y is at (−3, −4). Separation = √((4+3)² + (3+4)²) = √(49 + 49) = 7√2 ≈ **9.9 km**.",
    sc="Both walkers from the same origin; subtract components, then Pythagoras (√98 = 7√2).",
    d='hard', sub='relative-position', pat='distance between two walkers', t=60))

# 10: four-leg direction, clean endpoint
p = E.walk('E', [('F', 5), ('R', 3), ('R', 5), ('R', 2)])
assert p == (0, -1, 'N'), p
assert E.dir_name(p[0], p[1]) == 'South'
pr.append(C.Q(
    'rsn-direction-10',
    "**Kiran starts facing East and walks 5 km, turns right and walks 3 km, turns right and walks 5 km, then turns right again and walks 2 km.** In which direction is she from the starting point?",
    ['South', 'North', 'East', 'West'], 'South',
    "East 5 → (5, 0); right → South 3 → (5, −3); right → West 5 → (0, −3); right → North 2 → (0, −1). The x-components cancel; 1 km of Southward drift remains → **South** of the start.",
    sc="Cancel East-West first (5 and 5); the leftover South 1 km decides the direction.",
    d='medium', sub='final-direction', pat='direction of the endpoint from start', t=45))

# 11: sunrise walk
p = E.walk('E', [('F', 10), ('L', 10)])
assert p == (10, 10, 'N'), p
pr.append(C.Q(
    'rsn-direction-11',
    "One morning, Amit walks **10 m towards the rising sun**, then turns left and walks 10 m. In which direction is he from his starting point?",
    ['North-East', 'North', 'South-East', 'East'], 'North-East',
    "Rising sun = East: he walks 10 m East, then turns left (facing East, left = North) 10 m. Endpoint (10, 10) → **North-East** of the start.",
    sc="Sunrise = East; facing East, left is North — (+, +) endpoint means North-East.",
    d='easy', sub='shadow-direction', pat='shadow-based facing', t=30))

# 12: three-leg net
p = E.walk('N', [('F', 7), ('R', 7), ('R', 7)])
assert p == (7, 0, 'S')
pr.append(C.Q(
    'rsn-direction-12',
    "**Rani walks 7 km North, turns right and walks 7 km East, then turns right and walks 7 km South.** What is her position relative to the start?",
    ['7 km East', '7 km North', 'At the starting point', '21 km away'], '7 km East',
    "North 7 and South 7 cancel; the East 7 km survives → she is **7 km East** of the start. (21 km is the distance walked.)",
    sc="Out-and-back legs cancel; only the middle leg counts.",
    d='easy', sub='final-direction', pat='direction of the endpoint from start', t=35))

# 13: 3-4-5 nested
p = E.walk('N', [('F', 5), ('R', 3), ('R', 9)])
assert p == (3, -4, 'S') and dist(p) == 5
pr.append(C.Q(
    'rsn-direction-13',
    "**Imran walks 5 km North, turns right and walks 3 km, then turns right again and walks 9 km.** How far is he from the starting point?",
    ['5 km', '17 km', '6 km', '11 km'], '5 km',
    "North 5 → (0, 5); right = East 3 → (3, 5); right = South 9 → (3, −4). Distance = √(9 + 16) = **5 km**.",
    sc="Components (3, 4) reappear after cancellation → the triple gives 5.",
    d='medium', sub='direction-idea', pat='shortest distance between start and finish', t=45))

# 14: two anchors
pr.append(C.Q(
    'rsn-direction-14',
    "**D is 6 km West of C. C is 4 km South of B.** In which direction is **B from D**?",
    ['North-East', 'North-West', 'South-East', 'South-West'], 'North-East',
    "Place D at the origin. 'D is 6 km West of C' puts C 6 km **East** of D. 'C is 4 km South of B' puts B 4 km **North** of C. So B sits at (+6, +4) from D → **North-East** of D.",
    sc="Anchor at D (the asked-from point); C hangs East, B hangs North of C.",
    d='medium', sub='relative-position', pat='relative position of two people', t=45))

# 15: marching orders
h = heading_after('N', [('ABOUT', 1)])
h2 = heading_after(h, [('CW', 1)])
assert h == 'S' and h2 == 'W', (h, h2)
pr.append(C.Q(
    'rsn-direction-15',
    "A soldier marching towards **North** is ordered **'about turn'**, and then **'right turn'**. In which direction is he marching now?",
    ['West', 'East', 'North', 'South'], 'West',
    "About turn: North → South. Right turn from South: South → **West** (right-hand cycle N→E→S→W).",
    sc="About turn = +180°; right turn = +90° on the N→E→S→W cycle.",
    d='easy', sub='final-direction', pat='final facing after turns', t=30))

assert len(pr) == 15

t = C.topic(
    'direction-distance', 'Direction & Distance', 'medium', {'tier1': '1-2', 'tier2': '1-2'},
    "Compass-walking puzzles: multi-leg journeys with left/right turns, questions on the shortest distance back, the direction faced, the endpoint's bearing from the start, and shadow-based facing. Everything reduces to two signed running totals plus one Pythagoras step, and most answers are 3-4-5 multiples. Shadow questions add one conversion line (morning shadow West, evening shadow East). A written trace of headings and components turns the whole topic into bookkeeping.",
    subs, patterns, examples, pr)

C.write_topic(t)
print('OK direction-distance')
