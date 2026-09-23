# build order-ranking topic (topic 9)
from itertools import permutations
import common as C


def other_end(n, pos):
    return n + 1 - pos


def check_order(items, constraints):
    """constraints: list of (a, b) meaning a ranks above (better/taller/...) b.
    Transitive closure is applied automatically. Returns the unique total
    order or raises."""
    cons = set(constraints)
    changed = True
    while changed:  # transitive closure
        changed = False
        for a, b in list(cons):
            for c, d in list(cons):
                if b == c and (a, d) not in cons:
                    cons.add((a, d))
                    changed = True
    sols = [p for p in permutations(items)
            if all(p.index(a) < p.index(b) for a, b in cons)]
    assert len(sols) == 1, ('ambiguous order', items, sorted(cons), len(sols))
    return sols[0]


subs = []

subs.append(C.sub(
    'order-idea', 'How ranking questions work',
    "People (or objects) stand in a line or carry ranks, and you must convert between viewpoints: top↔bottom, left↔right, front↔back. The entire topic runs on two ideas:\n\n1. **Mirror conversion**: if there are $n$ positions, the person at position $p$ from one end sits at position $n + 1 - p$ from the other. The '+1' exists because the person's own seat is counted on both sides.\n2. **Two-viewpoint total**: if the same person is $a$-th from one end and $b$-th from the other, then $n = a + b - 1$.\n\nEverything else — 'how many between', overlaps, joined queues — is these two formulas plus careful reading. Draw a tiny line of boxes for any question that involves three or more people; the 5 seconds of drawing prevents every 'off by one' answer.",
    formulas=[
        C.F('Mirror position', 'p' + "' = n + 1 - p", 'Position from the other end.'),
        C.F('Total from two ranks', 'n = a + b - 1', 'Same person, ranked from both ends.'),
        C.F('Between count', '\\text{between} = |a - b| - 1', 'Two positions measured from the SAME end.'),
    ],
    tricks=[
        C.T(
            'Draw the end-zones',
            "Sketch a short row of boxes. Fill in what you know at the ends: 'a-th from left' means a−1 people before her. Counting the unknowns at each end replaces every formula with a picture.",
            "**Q.** In a row of 40, A is 11th from the left. How many are to her right?\n\n**Sol.** 11th from left → 10 before her; 40 − 11 = **29 to her right** (she is 30th from the right).",
            "a-th from an end = (a−1) people beyond that end. The rest is subtraction."),
    ],
    mistakes=[
        "Forgetting the +1/−1 corrections — the examiner sets traps exactly one away from the answer.",
        "Mixing viewpoints: subtracting a 'from the right' rank from a 'from the left' rank directly.",
        "Assuming the answer must be one less or one more than a listed option — compute first.",
    ]))

subs.append(C.sub(
    'rank-position', 'Ranks and positions',
    "Single-person rank conversions and totals:\n\n- **Convert an end**: 12th from top in a class of 45 → 45 + 1 − 12 = 34th from bottom.\n- **Find the total**: 8th from the left and 21st from the right → n = 8 + 21 − 1 = 28.\n- **'Same from both ends'**: 11th from either end → n = 11 + 11 − 1 = 21.\n\nWatch the exam's phrasing variants: 'how many students scored less than him' = his rank **from the bottom**, 'precedes him' = people before his position, 'queue joined from the front' shifts every old position forward by the number of joiners.",
    tricks=[
        C.T(
            'Sanity-span check',
            "The two ranks of one person must satisfy a + b = n + 1. Before marking a total, add the given ranks: if the sum is not total-plus-one, one of the numbers was misread.",
            "**Q.** K is 12th from the left and 19th from the right. Total?\n\n**Sol.** 12 + 19 = 31, so n = 31 − 1 = **30**. Check: 12th from left has 11 left of her; 19th from right has 18 right of her; 11 + 1 + 18 = 30 ✓.",
            "a + b = n + 1 is a two-second self-check built into every question."),
    ],
    mistakes=[
        "Using n = a + b (no −1).",
        "Treating '11th from either end' as two different people's ranks.",
        "Missing queue shifts when people join or leave ahead of the person.",
    ]))

subs.append(C.sub(
    'between-overlapping', 'People between two positions',
    "Three standard shapes:\n\n1. **Both from the same end**: between = |a − b| − 1.\n2. **From opposite ends**: convert one rank first (position from the other end = n + 1 − p), then subtract.\n3. **Overlapping ranks**: A is 10th from the left, B is 25th from the left, in a row of 20 — impossible unless ranks overlap; the between-count formula still works after conversion, but the exam usually avoids true contradictions.\n\nFor the **'middle person'** variant (odd gap), the middle position between ranks a and b (same end) is (a + b) ÷ 2 — it must come out as a whole number; if it does not, the question intends 'two middle people' and asks something else.",
    tricks=[
        C.T(
            'Convert, then count',
            "Never subtract ranks from different ends. Convert one with n + 1 − p, then |a − b| − 1.",
            "**Q.** Row of 30: A is 10th from the left, B is 12th from the right. How many sit between?\n\n**Sol.** B from the left = 30 + 1 − 12 = 19th. Between = 19 − 10 − 1 = **8**.",
            "One conversion, one subtraction, one final −1."),
    ],
    mistakes=[
        "Subtracting a left-rank from a right-rank directly.",
        "Dropping the final −1 (counting the endpoints themselves).",
        "Using n + 1 − p twice, converting both ranks.",
    ]))

subs.append(C.sub(
    'arrangement-comparison', 'Ordering and comparison chains',
    "'P is taller than Q but shorter than R… who is second tallest?' The constraints sort a small set — five people, five or six statements. The reliable method:\n\n1. Write each statement as an inequality fragment: 'P taller than Q' → P > Q.\n2. Chain all fragments into one ordering, or brute-force by hand when fragments branch.\n3. Read the answer from the final chain.\n\nA complete CGL puzzle always has a **unique** chain. If two orderings satisfy your reading of the statements, you misread one — usually 'X is taller than Y' vs 'Y is taller than X', or a hidden 'immediately taller'. Note the special comparatives: 'immediately above' fixes adjacency; 'between A and B' fixes position, not just inequality.",
    tricks=[
        C.T(
            'Longest-chain first',
            "Find the person who appears in the most statements and build outwards from them. The chain assembles in one pass instead of three.",
            "**Q.** A > B; C > A; D > C but D < E. Order?\n\n**Sol.** Chain the A–C–D–E spine: E > D > C > A > B — unique. Middle (third tallest) = **C**.",
            "Start from the most-mentioned name; attach the rest one fragment at a time."),
    ],
    mistakes=[
        "Answering from a partial chain before all statements are used.",
        "Ignoring 'immediately' — adjacency changes 'second tallest' answers.",
        "Accepting two possible orders without re-reading the statements.",
    ]))

patterns = [
    C.P('Rank from the other end', 'very common',
        "'nth from top/bottom (left/right) in a group of N — rank from the other end?'",
        "n' = N + 1 − n."),
    C.P('Total from two ranks', 'very common',
        "'X is a-th from one end and b-th from the other. How many in all?'",
        "n = a + b − 1; check with a + b = n + 1."),
    C.P('How many between', 'very common',
        "Two people's positions; count the people between them.",
        "Put both ranks on the same end, then |a − b| − 1."),
    C.P('Middle person', 'occasional',
        "Position of the person exactly between two known ranks.",
        "(a + b) ÷ 2 from the shared end; must be a whole number."),
    C.P('Queue joining / leaving', 'occasional',
        "People join or leave a queue ahead of the tracked person.",
        "Shift the tracked position by the net change at the front."),
    C.P('Comparison chain puzzle', 'very common',
        "Taller/heavier/faster statements; who is tallest, second, lightest…",
        "Inequality fragments → one unique chain → read the asked slot."),
]

examples = []

# ex1
assert other_end(40, 15) == 26
examples.append(C.Q(
    'rsn-order-ranking-ex1',
    "In a class of **40 students**, Meena ranks **15th from the top**. What is her rank from the bottom?",
    ['26th', '25th', '27th', '24th'], '26th',
    "Rank from the other end = 40 + 1 − 15 = **26th**. (25th forgets the +1.)",
    sc="One formula: n + 1 − p.",
    d='easy', sub='rank-position', pat='rank from the other end', t=25))

# ex2
assert 12 + 19 - 1 == 30
examples.append(C.Q(
    'rsn-order-ranking-ex2',
    "In a row of students, **Karan is 12th from the left and 19th from the right.** How many students are in the row?",
    ['30', '31', '29', '32'], '30',
    "n = 12 + 19 − 1 = **30**. Check: 11 students left of him + Karan + 18 to his right = 30 ✓.",
    sc="Add the two ranks, subtract one.",
    d='easy', sub='rank-position', pat='total from two ranks', t=25))

# ex3: comparison chain
order = check_order(['A', 'B', 'C', 'D', 'E'],
                    [('A', 'B'), ('C', 'A'), ('D', 'C'), ('E', 'D')])
assert order == ('E', 'D', 'C', 'A', 'B'), order
examples.append(C.Q(
    'rsn-order-ranking-ex3',
    "**A is taller than B. C is taller than A. D is taller than C but shorter than E.** Who is the **third tallest**?",
    ['C', 'A', 'D', 'B'], 'C',
    "Chain the statements: E > D > C > A > B. Third tallest = **C**. (The chain is forced — each statement slots exactly one person.)",
    sc="Build one chain E > D > C > A > B and read the slot; no trial and error needed.",
    d='easy', sub='arrangement-comparison', pat='comparison chain puzzle', t=35))

# ex4: between with conversion
assert other_end(36, 9) == 28 and 28 - 15 - 1 == 12
examples.append(C.Q(
    'rsn-order-ranking-ex4',
    "In a row of **36 students, A is 15th from the left and B is 9th from the right.** How many students sit **between** A and B?",
    ['12', '13', '11', '21'], '12',
    "B from the left = 36 + 1 − 9 = 28th. Between = 28 − 15 − 1 = **12**.",
    sc="Convert the right-rank to a left-rank first; then difference minus one.",
    d='medium', sub='between-overlapping', pat='how many between', t=40))

# ---------------------------------------------------------------- practice
pr = []

# 1
assert other_end(45, 12) == 34
pr.append(C.Q(
    'rsn-order-ranking-1',
    "In a class of **45 students, Ravi ranks 12th from the top**. What is his rank from the bottom?",
    ['34th', '33rd', '35th', '32nd'], '34th',
    "45 + 1 − 12 = **34th**.",
    sc="n + 1 − p.",
    d='easy', sub='rank-position', pat='rank from the other end', t=25))

# 2
assert 8 + 21 - 1 == 28
pr.append(C.Q(
    'rsn-order-ranking-2',
    "In a row of students, **Sita is 8th from the left and 21st from the right.** How many students are in the row?",
    ['28', '29', '27', '30'], '28',
    "n = 8 + 21 − 1 = **28**.",
    sc="Sum of the two ranks minus 1.",
    d='easy', sub='rank-position', pat='total from two ranks', t=25))

# 3
assert other_end(40, 11) == 30
pr.append(C.Q(
    'rsn-order-ranking-3',
    "In a row of **40 students, A is 11th from the left end.** What is A's position from the right end?",
    ['30th', '29th', '31st', '28th'], '30th',
    "40 + 1 − 11 = **30th**.",
    sc="Mirror formula n + 1 − p.",
    d='easy', sub='rank-position', pat='rank from the other end', t=25))

# 4: between with conversion
assert other_end(30, 12) == 19 and 19 - 10 - 1 == 8
pr.append(C.Q(
    'rsn-order-ranking-4',
    "In a row of **30 students, A is 10th from the left and B is 12th from the right.** How many students are **between** A and B?",
    ['8', '9', '7', '6'], '8',
    "B from the left = 30 + 1 − 12 = 19th. Between = 19 − 10 − 1 = **8**.",
    sc="Convert B to a left-rank, subtract, drop the endpoints.",
    d='medium', sub='between-overlapping', pat='how many between', t=40))

# 5: between, one rank from back
assert other_end(50, 20) == 31 and 31 - 16 - 1 == 14
pr.append(C.Q(
    'rsn-order-ranking-5',
    "In a queue of **50 people, X is 16th from the front and Y is 20th from the back.** How many people are **between** X and Y?",
    ['14', '15', '13', '16'], '14',
    "Y from the front = 50 + 1 − 20 = 31st. Between = 31 − 16 − 1 = **14**.",
    sc="Same-end conversion first; then difference − 1.",
    d='medium', sub='between-overlapping', pat='how many between', t=40))

# 6: middle person
assert (9 + 21) % 2 == 0 and (9 + 21) // 2 == 15
pr.append(C.Q(
    'rsn-order-ranking-6',
    "In a queue, **A is 9th from the front and B is 21st from the front.** Who stands **exactly in the middle** of A and B (in position, not count)?",
    ['15th from the front', '14th from the front', '16th from the front', '15th from the back'], '15th from the front',
    "Middle position = (9 + 21) ÷ 2 = **15th from the front**. (The count of people between them is 11 — different question.)",
    sc="Average the two same-end positions.",
    d='easy', sub='between-overlapping', pat='middle person', t=30))

# 7: same from both ends
assert 11 + 11 - 1 == 21
pr.append(C.Q(
    'rsn-order-ranking-7',
    "**Bulbul is 11th from either end of a queue.** How many people are in the queue?",
    ['21', '22', '20', '23'], '21',
    "n = 11 + 11 − 1 = **21**. (She is the exact middle of an odd-length queue.)",
    sc="'Either end' means both ranks are the same number.",
    d='easy', sub='rank-position', pat='total from two ranks', t=25))

# 8
assert 17 + 18 - 1 == 34
pr.append(C.Q(
    'rsn-order-ranking-8',
    "**A is 17th from the left and 18th from the right in a row.** How many people are in the row?",
    ['34', '35', '33', '36'], '34',
    "n = 17 + 18 − 1 = **34**.",
    sc="a + b − 1.",
    d='easy', sub='rank-position', pat='total from two ranks', t=25))

# 9: heights second tallest
order = check_order(['P', 'Q', 'R', 'S', 'T'],
                    [('P', 'Q'), ('R', 'P'),
                     ('S', 'R'), ('S', 'P'), ('S', 'Q'), ('S', 'T'),
                     ('Q', 'T')])
assert order == ('S', 'R', 'P', 'Q', 'T'), order
pr.append(C.Q(
    'rsn-order-ranking-9',
    "**P is taller than Q but shorter than R. S is the tallest of all. T is shorter than Q.** Who is the **second tallest**?",
    ['R', 'P', 'Q', 'S'], 'R',
    "Chain: S > R > P > Q > T. Second tallest = **R**. (S is fixed at the top by 'tallest of all'; R > P > Q comes from the other statements.)",
    sc="Pin the extreme first ('tallest of all'), then chain the rest.",
    d='medium', sub='arrangement-comparison', pat='comparison chain puzzle', t=45))

# 10: weights lightest
order = check_order(['A', 'B', 'C', 'D', 'E'],
                    [('A', 'B'), ('B', 'C'), ('D', 'A'), ('C', 'E')])
assert order == ('D', 'A', 'B', 'C', 'E'), order
pr.append(C.Q(
    'rsn-order-ranking-10',
    "**A is heavier than B. C is lighter than B. D is heavier than A. E is lighter than C.** Who is the **lightest**?",
    ['E', 'C', 'B', 'A'], 'E',
    "Chain: D > A > B > C > E. Lightest = **E**. (Each 'lighter than' points downward; the chain bottoms out at E.)",
    sc="One chain from the heaviest statement to the lightest; the last name is the answer.",
    d='medium', sub='arrangement-comparison', pat='comparison chain puzzle', t=45))

# 11: marks highest
order = check_order(['M', 'N', 'O', 'P', 'Q'],
                    [('M', 'N'), ('N', 'O'), ('P', 'M'), ('M', 'Q'), ('Q', 'N')])
assert order == ('P', 'M', 'Q', 'N', 'O'), order
pr.append(C.Q(
    'rsn-order-ranking-11',
    "In a test, **M scored more than N, O scored less than N, P scored more than M, and Q scored less than M but more than N.** Who scored the **highest**?",
    ['P', 'M', 'Q', 'N'], 'P',
    "Chain: P > M > Q > N > O. Highest = **P**. (Q sits between M and N, exactly as stated.)",
    sc="'More than' chains head upward; the chain's top is the answer.",
    d='medium', sub='arrangement-comparison', pat='comparison chain puzzle', t=45))

# 12: total from two ranks
assert 13 + 57 - 1 == 69
pr.append(C.Q(
    'rsn-order-ranking-12',
    "In a class test, **Mohan ranks 13th from the top and 57th from the bottom.** How many students appeared for the test?",
    ['69', '70', '68', '71'], '69',
    "n = 13 + 57 − 1 = **69**.",
    sc="a + b − 1, then sanity-check a + b = n + 1.",
    d='easy', sub='rank-position', pat='total from two ranks', t=25))

# 13: queue joining
assert 9 + 5 == 14
pr.append(C.Q(
    'rsn-order-ranking-13',
    "In a queue of 30 people, **A is 9th from the front. If 5 new people join the queue at the front**, what is A's new position from the front?",
    ['14th', '13th', '15th', '4th'], '14th',
    "Every old position shifts back by 5: 9 + 5 = **14th**. (The queue length also grows to 35, but only front-joins affect A's rank.)",
    sc="Front joiners push the tracked person back one-for-one.",
    d='easy', sub='rank-position', pat='queue joining / leaving', t=30))

# 14: swap positions
assert other_end(40, 15) == 26
pr.append(C.Q(
    'rsn-order-ranking-14',
    "In a row of **40 students, A is 15th from the left and B is 25th from the left.** If **A and B interchange their positions**, what is **B's new position from the right**?",
    ['26th', '25th', '24th', '27th'], '26th',
    "After the swap B occupies A's old spot: 15th from the left. From the right = 40 + 1 − 15 = **26th**.",
    sc="An interchange just re-labels the two positions — reuse the mirror formula on the new spot.",
    d='medium', sub='rank-position', pat='rank from the other end', t=40))

# 15: ages third oldest
order = check_order(['V', 'W', 'X', 'Y', 'Z'],
                    [('X', 'Y'), ('W', 'Z'), ('V', 'X'), ('W', 'V'), ('Y', 'Z')])
assert order == ('W', 'V', 'X', 'Y', 'Z'), order
pr.append(C.Q(
    'rsn-order-ranking-15',
    "**X is older than Y. Z is younger than W. V is older than X. W is older than V. Y is older than Z.** Who is the **third oldest**?",
    ['X', 'V', 'Y', 'W'], 'X',
    "Chain: W > V > X > Y > Z (W is pinned above V; V above X; X above Y; Y above Z; and Z < W is automatic). Third oldest = **X**.",
    sc="Build the spine W > V > X, then hang Y and Z below X.",
    d='hard', sub='arrangement-comparison', pat='comparison chain puzzle', t=50))

assert len(pr) == 15

t = C.topic(
    'order-ranking', 'Order & Ranking', 'medium', {'tier1': '1-2', 'tier2': '1-2'},
    "Rank-conversion and ordering puzzles: ranks from either end, totals from two ranks, people between two positions, queue shifts, and taller/heavier comparison chains. Two formulas (n + 1 − p and a + b − 1) plus the between-count run the entire numeric half; the comparison half is inequality chaining into one unique order. Speed comes from drawing a mini-row and from the built-in check a + b = n + 1.",
    subs, patterns, examples, pr)

C.write_topic(t)
print('OK order-ranking')
