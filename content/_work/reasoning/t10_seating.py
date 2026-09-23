# build seating-arrangement topic (topic 10)
from itertools import permutations
import common as C


def lin_sols(people, clue):
    """All rows (tuples, index 0 = viewer's left) consistent with clue(pos)."""
    return [p for p in permutations(people)
            if clue({x: i for i, x in enumerate(p)})]


def circ_sols(people, clue, anchor):
    """All circular seatings (clockwise, anchor fixed at seat 0) fitting
    clue(pos, n). Facing centre: left nbr = (i+1)%n, right nbr = (i-1)%n."""
    rest = [x for x in people if x != anchor]
    n = len(people)
    out = []
    for p in permutations(rest):
        arr = (anchor,) + p
        pos = {x: i for i, x in enumerate(arr)}
        if clue(pos, n):
            out.append(arr)
    return out


def one(sols, tag):
    assert len(sols) == 1, (tag, 'non-unique', sols)
    return sols[0]


subs = []

subs.append(C.sub(
    'seating-idea', 'How seating puzzles are set',
    "A seating puzzle gives a set of people and a set of positional clues; you must rebuild the exact seating and then answer ('who is opposite D?', 'who sits third from the left?'). Two families cover the whole topic:\n\n1. **Linear** — everyone in one row, usually 'facing north'. The row's left/right ends belong to the **viewer**: the left end is on your left in the sketch. When a row **faces south**, each person's own left and right flip — a person facing south has their left toward your right. The ends never flip.\n2. **Circular** — around a table, 'facing centre' by default. For a person facing the centre, the **left-hand neighbour is the next person clockwise**; the right-hand neighbour is the next anticlockwise. If they face **outward**, both flip.\n\nMethod that never fails: draw n blanks, fill every 'extreme end / middle / opposite' clue first (they pin seats absolutely), then chain the relative clues ('second to the left of…'), and use every negative clue ('not adjacent', 'not at an end') only at the end to kill remaining options.",
    formulas=[
        C.F('Circular neighbour rule', 'L(i) = (i+1) \\bmod n,\\ R(i) = (i-1) \\bmod n',
            'Seats numbered clockwise, everyone facing centre. Both swap if facing outward.'),
        C.F('Opposite seats', 'i \\leftrightarrow (i + n/2) \\bmod n',
            'Only when n is even; odd tables have no opposite seat.'),
        C.F('Viewer vs person', '\\text{person faces south} \\Rightarrow \\text{their left} = \\text{your right}',
            "Applies only to the person's own left/right, never to the row ends."),
    ],
    tricks=[
        C.T(
            'Pin the absolutes first',
            "Extreme ends, exact middles, 'opposite', 'fourth from left' fix specific seats before any chaining. Fill those, and the remaining people usually fall into one or two slots.",
            "**Q.** Six seats, B at the extreme left, F at the extreme right, D immediately right of B, C immediately left of F.\n\n**Sol.** B _ D _ C F with two blanks; the two leftover names (A, E) go in seats 2 and 4 — one more clue finishes it. Absolutes did the scaffolding.",
            "Ends/middle/opposite clues are free information — place them before touching chains."),
    ],
    mistakes=[
        "Applying left/right flips to the row's ends — ends belong to the viewer, only individuals flip.",
        "Forgetting the facing-outward flip in circular puzzles.",
        "Ignoring 'not adjacent / not at an end' until the answer, not the solving.",
    ]))

subs.append(C.sub(
    'linear-arrangement', 'Single-row arrangements',
    "Everyone in one line, normally facing north. Vocabulary decoded:\n\n- **'k-th to the left/right of X'** — count k seats from X in that direction (k = 2 means one person in between).\n- **'immediate left/right / neighbour'** — adjacent seat, no gap.\n- **'between'** — anywhere strictly inside; **'immediately between'** — the very next seat on both sides is the named pair.\n- **'extreme end'** — first or last seat.\n\nBuild order: ends and middle seats → fixed-distance clues ('third to the right of…') → adjacency pairs → negative clues. If the same face direction confuses you, physically rotate your rough sketch so everyone 'faces' up; your left is then their left.",
    tricks=[
        C.T(
            "Chain links, don't guess gaps",
            "'Second to the right of A' pins B exactly two seats from A — mark it with an arrow as soon as you read it. A puzzle of six clues usually has four such arrows; the picture completes itself.",
            "**Q.** C sits third from the left; A sits second to the right of C; B is adjacent to both C and A.\n\n**Sol.** C at seat 3 → A at seat 5 → B must touch both → seat 4. One arrow each, done.",
            "Every relative clue is an arrow of fixed length — draw all arrows before placing anyone optional."),
    ],
    mistakes=[
        "Counting 'second to the right' as one seat away.",
        "Treating 'sits between' as 'immediately between'.",
        "Missing that south-facing rows flip each person's left/right.",
    ]))

subs.append(C.sub(
    'circular-arrangement', 'Round-table arrangements',
    "For people facing the centre (the default), fix the geometry once: **left neighbour = clockwise, right neighbour = anticlockwise.** 'Opposite' exists only for an even number of people: seat i is opposite seat i + n/2.\n\nRotation is the puzzle-setter's freedom: clues never tell you 'seat 1', so start by placing any one person anywhere and build the circle around them — every other clue is relative to people, not seats. Facing-outward variants flip left/right; mixed facing ('A faces centre, B faces outward') is rare in CGL and usually restricted to 4–5 people.",
    tricks=[
        C.T(
            'Walk the circle in one direction',
            "Take the longest adjacency chain and lay it out clockwise without thinking: 'D is to the immediate left of B, C to the immediate left of D, E to the immediate left of C' is just the clockwise string B → D → C → E. Close the loop with the last clue.",
            "**Q.** Facing centre: A is to the immediate right of B; D to the immediate left of B; C to the immediate left of D; E to the immediate left of C.\n\n**Sol.** Left-walk from B: B, D, C, E, and A sits at B's right — the string closes as B D C E (A) — fully forced.",
            "'Immediate left' chains concatenate into one clockwise string — walk it instead of solving seat by seat."),
    ],
    mistakes=[
        "Using clockwise as the right-hand side for centre-facing people — it is the left.",
        "Hunting for an 'opposite' person at an odd-sized table.",
        "Placing people by seat numbers instead of relative to a fixed anchor.",
    ]))

subs.append(C.sub(
    'puzzle-strategy', 'Exam strategy for puzzles',
    "Seating questions come in sets of 3–5 sharing one puzzle. Budget rules:\n\n- **Read all clues before drawing anything.** Negative clues ('Q does not face the centre') often decide the last seat instantly.\n- **Solve once, answer many.** The first question costs 90–120 seconds; questions 2–4 of the same puzzle cost 15–20 seconds each because the seating is already on paper.\n- **Skip cleanly.** If after one full pass the seating still has two live configurations, park the set and return — CGL reasoning has cheaper marks elsewhere.\n- **Verify with one closed loop:** walk left-neighbour links around your final circle; if the string doesn't close, an arrow was drawn backwards.",
    tricks=[
        C.T(
            'Two-configuration bail-out',
            "When exactly two seatings survive all clues, check what the QUESTION asks: if both configurations give the same answer, mark it and move on — you never needed the extra clue you thought was missing.",
            "**Q.** After all clues, A and B could swap (seats 2/3). Question: who is opposite E?\n\n**Sol.** If A/B's two seats are both on the same side, the seat opposite E is unchanged — answer stands either way.",
            "The question only needs the asked seat, not the full unique seating."),
    ],
    mistakes=[
        "Restarting the sketch for every question in the set instead of reusing it.",
        "Spending 3+ minutes hoping a fifth re-read reveals a clue that isn't there.",
        "Answering from a partial sketch without checking the remaining clues still hold.",
    ]))

patterns = [
    C.P('Extreme ends + adjacency row', 'very common',
        "Ends pinned, immediate neighbours chained.",
        "Place ends first, then connect neighbour pairs; leftover people fill the last seats."),
    C.P('Fixed-distance row', 'very common',
        "'k-th to the left/right of X' clues.",
        "Draw fixed-length arrows from each anchor; arrows lock seats absolutely."),
    C.P('South-facing / flipped row', 'occasional',
        "Row faces south, so each person's left/right is mirrored.",
        "Flip only the individuals' left/right; the row's ends stay viewer-fixed."),
    C.P('Circular facing centre', 'very common',
        "Round table, left = clockwise, right = anticlockwise.",
        "Anchor one person, walk immediate-left chains around the circle."),
    C.P('Circular facing outward', 'occasional',
        "Same table but both flips reverse.",
        "Reuse the facing-centre result with left/right swapped."),
    C.P('Two-variable circular (couples/genders)', 'occasional',
        "Eight people, husband-wife pairs, opposite and adjacency clues.",
        "First place the named relation web, then drop spouses into leftover compatibility."),
    C.P('Negative-clue finish', 'common',
        "'Not adjacent / not at an end / does not face centre' decides between survivors.",
        "Collect all negatives in a margin list; apply only when ≤2 configurations remain."),
]

examples = []

# ex1 (linear)
ex1 = one(lin_sols(
    ['A', 'B', 'C', 'D', 'E'],
    lambda p: p['B'] == 0 and p['E'] == 4 and p['D'] == p['B'] + 1 and p['C'] == p['E'] - 1),
    'ex1')
assert ex1 == ('B', 'D', 'A', 'C', 'E'), ex1
examples.append(C.Q(
    'rsn-seating-ex1',
    "Five friends **A, B, C, D and E sit in a row facing north. B sits at the extreme left end, E at the extreme right end. D sits immediately to the right of B, and C sits immediately to the left of E.** Who sits in the **middle** of the row?",
    ['A', 'C', 'D', 'E'], 'A',
    "Place the absolutes: B (seat 1), E (seat 5), then D right of B (seat 2) and C left of E (seat 4). The only person left, **A**, takes the middle seat 3.",
    sc="Absolutes first — ends and fixed adjacencies leave the answer by elimination.",
    d='easy', sub='linear-arrangement', pat='extreme ends + adjacency row', t=45))

# ex2 (circular facing centre)
ex2 = one(circ_sols(
    ['A', 'B', 'C', 'D', 'E'],
    lambda p, n: (p['A'] == (p['B'] - 1) % n and p['D'] == (p['B'] + 1) % n
                  and p['C'] == (p['D'] + 1) % n and p['E'] == (p['C'] + 1) % n),
    'A'), 'ex2')
assert ex2 == ('A', 'B', 'D', 'C', 'E'), ex2
assert (ex2.index('A') + 2) % 5 == ex2.index('D')
examples.append(C.Q(
    'rsn-seating-ex2',
    "Five people **A, B, C, D and E sit around a circular table, all facing the centre. A is to the immediate right of B; D is to the immediate left of B; C is to the immediate left of D; E is to the immediate left of C.** Who sits **second to the left of A**?",
    ['D', 'C', 'E', 'B'], 'D',
    "Facing the centre, left = clockwise. Walk clockwise from B: D, C, E; A closes the circle at B's right. Clockwise order: A, B, D, C, E. Second to the left of A = two seats clockwise = **D**.",
    sc="Chain the 'immediate left' clues into one clockwise string, close it, then count.",
    d='medium', sub='circular-arrangement', pat='circular facing centre', t=60))

# ex3 (linear, negative clue)
ex3 = one(lin_sols(
    ['P', 'Q', 'R', 'S'],
    lambda p: p['Q'] == 3 and p['P'] != p['Q'] - 1 and p['R'] == p['P'] - 1),
    'ex3')
assert ex3 == ('R', 'P', 'S', 'Q'), ex3
examples.append(C.Q(
    'rsn-seating-ex3',
    "Four people **P, Q, R and S sit in a row facing north. Q sits at the extreme right end. P is not adjacent to Q. R sits immediately to the left of P.** Who sits **second from the left end**?",
    ['P', 'S', 'R', 'Q'], 'P',
    "Q (seat 4). P must avoid seat 3 (next to Q), and R needs the seat on P's left — so P = seat 2, R = seat 1. S takes seat 3. Second from the left = **P**.",
    sc="The negative clue removes one seat; 'immediately left' then forces the only pair left.",
    d='easy', sub='linear-arrangement', pat='negative-clue finish', t=40))

# ---------------------------------------------------------------- practice
pr = []

# 1
q1 = one(lin_sols(
    ['A', 'B', 'C', 'D', 'E', 'F'],
    lambda p: p['C'] == 2 and p['A'] == p['C'] + 2 and p['B'] == p['C'] + 1
    and p['D'] == 0 and p['E'] == 5), 'q1')
assert q1 == ('D', 'F', 'C', 'B', 'A', 'E'), q1
pr.append(C.Q(
    'rsn-seating-1',
    "Six friends **A, B, C, D, E and F sit in a row facing north. C sits third from the left end. A sits second to the right of C. B is an immediate neighbour of both C and A. D sits at the extreme left end and E at the extreme right end.** Who sits **exactly between C and A**?",
    ['B', 'F', 'D', 'E'], 'B',
    "C at seat 3 → A at seat 5. The only seat touching both C (3) and A (5) is seat 4 → **B**. (D and E take the ends, so F sits at seat 2.)",
    sc="Fixed-distance arrows first; a neighbour-of-both clue is just the seat in between.",
    d='easy', sub='linear-arrangement', pat='fixed-distance row', t=45))

# 2
q2 = one(lin_sols(
    ['J', 'K', 'L', 'M', 'N', 'O', 'P'],
    lambda p: p['M'] == 3 and p['L'] == 2 and p['O'] == 4 and p['J'] == 0
    and p['K'] == 6 and p['P'] == p['O'] + 1), 'q2')
assert q2 == ('J', 'N', 'L', 'M', 'O', 'P', 'K'), q2
pr.append(C.Q(
    'rsn-seating-2',
    "Seven people **J, K, L, M, N, O and P sit in a row facing north. M sits exactly in the middle. L sits immediately to the left of M and O immediately to the right of M. J sits at the extreme left end, K at the extreme right end. P sits between O and K.** Who sits **second from the left end**?",
    ['N', 'L', 'M', 'O'], 'N',
    "Middles first: M (seat 4), L (3), O (5). Ends: J (1), K (7). P between O and K → seat 6. The only person left, **N**, takes seat 2.",
    sc="Five clues pin five seats; the answer is the leftover person's slot.",
    d='easy', sub='linear-arrangement', pat='extreme ends + adjacency row', t=50))

# 3 (south-facing)
q3 = one(lin_sols(
    ['R', 'S', 'T', 'U', 'V'],
    lambda p: p['R'] == 2 and p['T'] == p['R'] + 2 and p['V'] == p['R'] - 1
    and p['S'] == 0), 'q3')
assert q3 == ('S', 'V', 'R', 'U', 'T'), q3
pr.append(C.Q(
    'rsn-seating-3',
    "Five friends **R, S, T, U and V sit in a row facing south. R sits in the exact middle. T sits second to the left of R. V sits immediately to the right of R. S sits at an extreme end.** Who sits **immediately to the left of R** (from R's own facing)?",
    ['U', 'V', 'T', 'S'], 'U',
    "Facing south, R's left is the viewer's right. R (seat 3) → T is second to R's left = seat 5; V immediately to R's right = seat 2; S takes seat 1, leaving **U at seat 4 — immediately to R's left** (viewer's right of R).",
    sc="South-facing row: swap 'left' and 'right' for the people, keep the end seats as drawn.",
    d='hard', sub='linear-arrangement', pat='south-facing / flipped row', t=60))

# 4 (negative clue)
q4 = one(lin_sols(
    ['P', 'Q', 'R', 'S', 'T', 'W'],
    lambda p: p['P'] == 0 and p['Q'] == 5 and p['R'] == 1 and p['T'] != p['R'] + 1
    and p['S'] == p['W'] + 1 and p['T'] == p['S'] + 1), 'q4')
assert q4 == ('P', 'R', 'W', 'S', 'T', 'Q'), q4
pr.append(C.Q(
    'rsn-seating-4',
    "Six friends **P, Q, R, S, T and W face north. P is at the extreme left end and Q at the extreme right end. R sits immediately to the right of P. T is not adjacent to R. S sits between W and T (with W immediately to S's left and T immediately to S's right).** Who sits **third from the left end**?",
    ['W', 'S', 'T', 'R'], 'W',
    "P (1), R (2), Q (6). W–S–T must occupy seats 3–5 in that order. T at seat 3 would touch R — banned — so T sits at seat 5, giving W at seat 3. Third from the left = **W**.",
    sc="The negative clue is the decider: it alone chooses between the two W–S–T placements.",
    d='medium', sub='linear-arrangement', pat='negative-clue finish', t=55))

# 5 (linear 7)
q5 = one(lin_sols(
    ['A', 'B', 'C', 'D', 'E', 'F', 'G'],
    lambda p: p['E'] == 6 and p['D'] == 5 and p['G'] == p['D'] - 2
    and p['B'] == p['G'] + 1 and p['A'] != p['B'] - 1 and p['A'] != p['B'] + 1
    and p['C'] == 0 and p['F'] == p['C'] + 1), 'q5')
assert q5 == ('C', 'F', 'A', 'G', 'B', 'D', 'E'), q5
pr.append(C.Q(
    'rsn-seating-5',
    "Seven students **A, B, C, D, E, F and G sit in a row facing north. E sits at an extreme end, with D immediately to E's left. G sits second to the left of D, and B sits immediately to the right of G. A is not adjacent to B. C sits at an extreme end, with F immediately to C's right.** Who sits **fourth from the left end**?",
    ['G', 'B', 'A', 'D'], 'G',
    "E (7), D (6). G = D − 2 = seat 4, B = seat 5. C at the other end (1), F (2). A must avoid B's neighbours — seats 4 and 6 are gone, so A takes seat 3. Fourth from the left = **G**.",
    sc="Ends + fixed distances pin six seats; the negative clue only confirms the leftover.",
    d='hard', sub='linear-arrangement', pat='fixed-distance row', t=70))

# 6 (circular 6, opposite)
q6 = one(circ_sols(
    ['K', 'L', 'M', 'N', 'O', 'P'],
    lambda p, n: p['P'] == (p['M'] + n // 2) % n and p['L'] == (p['K'] + n // 2) % n
    and p['N'] == (p['K'] + 1) % n and p['O'] == (p['M'] - 1) % n
    and p['L'] == (p['O'] - 1) % n, 'M'), 'q6')
assert q6 == ('M', 'K', 'N', 'P', 'L', 'O'), q6
assert (q6.index('N') + 3) % 6 == q6.index('O')
pr.append(C.Q(
    'rsn-seating-6',
    "Six friends **K, L, M, N, O and P sit around a circular table facing the centre. P sits opposite M, and K sits opposite L. N is to the immediate left of K. O is to the immediate right of M, and L is to the immediate right of O.** Who sits **opposite N**?",
    ['O', 'M', 'P', 'L'], 'O',
    "Facing centre: right = anticlockwise, left = clockwise. Fix M anywhere: O is at M's right (next anticlockwise), L at O's right, K opposite L, N at K's left, and P closes the circle opposite M. Order (clockwise from M): M, K, N, P, L, O. N's opposite = three seats clockwise = **O**.",
    sc="Anchor one person, unwind the left/right chain, then read n/2 steps across.",
    d='hard', sub='circular-arrangement', pat='circular facing centre', t=80, place=3))

# 7 (circular facing outward)
q7 = one(circ_sols(
    ['R', 'S', 'T', 'U', 'V'],
    lambda p, n: p['S'] == (p['R'] + 1) % n and p['T'] == (p['S'] + 1) % n
    and p['V'] == (p['U'] + 1) % n and p['R'] == (p['V'] + 1) % n,
    'R'), 'q7')
assert q7 == ('R', 'S', 'T', 'U', 'V'), q7
pr.append(C.Q(
    'rsn-seating-7',
    "Five people **R, S, T, U and V sit around a circular table facing outward (away from the centre). S is to the immediate right of R, T to the immediate right of S, V to the immediate right of U, and R to the immediate right of V.** Who sits **immediately to the left of T** (from T's own perspective)?",
    ['S', 'U', 'R', 'V'], 'S',
    "Facing outward, right = clockwise. Chain the rights: R → S → T, and U → V → R, so the clockwise order is R, S, T, U, V. Facing outward, T's left is anticlockwise — the seat just before T — which is **S**.",
    sc="Outward facing flips both hands: the 'left of T' seat is the anticlockwise neighbour.",
    d='hard', sub='circular-arrangement', pat='circular facing outward', t=70))

# 8 (couples circular 8)
q8 = one(circ_sols(
    ['A', 'B', 'C', 'D', 'P', 'Q', 'R', 'S'],
    lambda p, n: p['C'] == (p['A'] + 4) % n and p['B'] == (p['P'] + 4) % n
    and p['S'] == (p['Q'] + 4) % n and p['R'] == (p['A'] + 1) % n
    and p['Q'] == (p['P'] + 1) % n and p['D'] == (p['C'] + 1) % n
    and (p['Q'] == (p['A'] + 1) % n or p['Q'] == (p['A'] - 1) % n),
    'P'), 'q8')
assert q8 == ('P', 'Q', 'A', 'R', 'B', 'S', 'C', 'D'), q8
assert (q8.index('R') + 4) % 8 == q8.index('D')
pr.append(C.Q(
    'rsn-seating-8',
    "Four married couples — **(A, P), (B, Q), (C, R), (D, S)** — sit around a circular table facing the centre. **C sits opposite A; B opposite P; S opposite Q. R is to the immediate left of A, Q to the immediate left of P, and D to the immediate left of C. Q is an immediate neighbour of A.** Who sits **opposite R**?",
    ['D', 'S', 'C', 'A'], 'D',
    "Fix P anywhere: Q at P's left; B opposite P; S opposite Q. Q must touch A, and R sits at A's left with C opposite A and D at C's left — the string P, Q, A, R, B, S, C, D closes the circle. R, three... four seats across (8 seats → +4) faces **D**.",
    sc="Spouses opposite + left-neighbour chains: lay the 8-string down once, then read +4.",
    d='hard', sub='circular-arrangement', pat='two-variable circular (couples/genders)', t=110))

# 9 (linear 7 middle)
q9 = one(lin_sols(
    ['H', 'I', 'J', 'K', 'L', 'M', 'N'],
    lambda p: p['K'] == 3 and p['I'] == 5 and (p['M'] == 4 or p['M'] == 6)
    and p['J'] == p['M'] - 3 and (p['L'] == p['K'] - 1 or p['L'] == p['K'] + 1)
    and p['H'] == 0 and p['N'] == 6), 'q9')
assert q9 == ('H', 'J', 'L', 'K', 'M', 'I', 'N'), q9
pr.append(C.Q(
    'rsn-seating-9',
    "Seven students **H, I, J, K, L, M and N sit in a row facing north. K sits exactly in the middle. I sits second to the right of K. M is an immediate neighbour of I. J sits third to the left of M. L is an immediate neighbour of K. H sits at the extreme left end and N at the extreme right end.** Who sits **third from the right end**?",
    ['M', 'K', 'I', 'L'], 'M',
    "K (4), I (6). M touches I (seat 5 or 7); J = M − 3 must exist → M = 5 (else J = 4, K's seat). J = 2. L touches K → seat 3 (5 is taken). H (1), N (7). Seats: H, J, L, K, M, I, N — third from the right = **M**.",
    sc="Test the 'immediate neighbour' two ways; the impossible one falls to a fixed-distance clue.",
    d='hard', sub='linear-arrangement', pat='fixed-distance row', t=80, place=1))

# 10 (circular 5 between)
q10 = one(circ_sols(
    ['A', 'B', 'C', 'D', 'E'],
    lambda p, n: p['E'] == (p['C'] + 1) % n and p['B'] == (p['E'] + 1) % n
    and p['D'] == (p['B'] + 1) % n and p['A'] == (p['C'] - 1) % n,
    'A'), 'q10')
assert q10 == ('A', 'C', 'E', 'B', 'D'), q10
assert (q10.index('B') - 2) % 5 == q10.index('C')
pr.append(C.Q(
    'rsn-seating-10',
    "Five people **A, B, C, D and E sit around a circular table facing the centre. E sits between C and B (immediately), D sits immediately to the left of B, and A sits to the immediate right of C.** Who sits **second to the right of B**?",
    ['C', 'A', 'E', 'D'], 'C',
    "Facing centre: left = clockwise. From C clockwise: E (between C and B), then B, then D at B's left. A sits at C's right (anticlockwise), closing the circle. Clockwise: A, C, E, B, D. Second to the right of B = two anticlockwise = **C**.",
    sc="'Between' + 'immediate left' chains trace the clockwise order almost by themselves.",
    d='medium', sub='circular-arrangement', pat='circular facing centre', t=65))

# 11 (immediately between)
q11 = one(lin_sols(
    ['T', 'U', 'V', 'W', 'X', 'Y'],
    lambda p: p['V'] == 1 and p['X'] == 2 and p['W'] == 3 and p['Y'] == 4
    and p['T'] == 0 and p['U'] == 5), 'q11')
assert q11 == ('T', 'V', 'X', 'W', 'Y', 'U'), q11
pr.append(C.Q(
    'rsn-seating-11',
    "Six friends **T, U, V, W, X and Y face north. V sits second from the left end. W sits immediately between X and Y. T sits at the extreme left end and U at the extreme right end.** Who sits **second to the right of W**?",
    ['U', 'Y', 'X', 'V'], 'U',
    "T (1), V (2), U (6). The X–W–Y block must fit consecutively with W in the middle — only seats 3–4–5 work (seat 2 is V's). X (3), W (4), Y (5). Two to the right of W = seat 6 = **U**.",
    sc="A consecutive block only fits the leftover run of seats — place ends first, then slide the block.",
    d='medium', sub='linear-arrangement', pat='extreme ends + adjacency row', t=55))

# 12 (linear 8 hard)
q12 = one(lin_sols(
    ['A', 'B', 'C', 'D', 'E', 'F', 'G', 'H'],
    lambda p: p['A'] == p['E'] - 2 and p['E'] == p['D'] - 3 and p['G'] in (0, 7)
    and p['D'] in (0, 7) and p['C'] == p['A'] - 1 and p['B'] == p['E'] + 1
    and p['F'] == p['B'] + 1), 'q12')
assert q12 == ('G', 'C', 'A', 'H', 'E', 'B', 'F', 'D'), q12
pr.append(C.Q(
    'rsn-seating-12',
    "Eight friends **A, B, C, D, E, F, G and H sit in a row facing north. A sits second to the left of E. E sits third to the left of D. G and D sit at the two extreme ends. C is an immediate neighbour of A (on A's left). B sits immediately to the right of E, and F immediately to the right of B.** Who sits **third from the right end**?",
    ['B', 'F', 'E', 'C'], 'B',
    "Ends: G and D. D must leave three seats to its left for E, so D = seat 8, G = seat 1. E = D − 3 = seat 5; A = seat 3; C on A's left = seat 2; B = seat 6, F = seat 7. Remaining H takes seat 4. Third from the right = seat 6 = **B**.",
    sc="'Third to the left of an end' forces which end is which — start there and chain inward.",
    d='hard', sub='linear-arrangement', pat='fixed-distance row', t=90))

assert len(pr) == 12

t = C.topic(
    'seating-arrangement', 'Seating Arrangement', 'high', {'tier1': '3-5', 'tier2': '4-6'},
    "Seating puzzles — linear rows and circular tables — are the highest-value reasoning block in CGL, appearing as a linked set of 3-5 questions. Mastery is mechanical: pin absolute seats (ends, middle, opposite) first, chain the fixed-distance and immediate-neighbour clues as arrows, apply negative clues last, and read the answer off the finished sketch. Circular variants hinge on one convention — facing centre, left = clockwise — and flip when people face outward.",
    subs, patterns, examples, pr)

C.write_topic(t)
print('OK seating-arrangement')
