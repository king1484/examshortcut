# build missing-number topic (topic 6)
import common as C


def ds(x):
    return sum(int(ch) for ch in str(abs(x)))


def rev2(x):
    s = str(x)
    return int(s[::-1]) if s[-1] != '0' else None


def row_families():
    """f(a,b) -> third cell. All 'reasonable' CGL row rules."""
    out = []
    for k in range(1, 61):
        out.append(('%d-(a+b)' % k, lambda a, b, k=k: k - a - b))
    for k in range(-20, 21):
        out.append(('a+b%+d' % k, lambda a, b, k=k: a + b + k))
        out.append(('a-b%+d' % k, lambda a, b, k=k: a - b + k))
        out.append(('a*b%+d' % k, lambda a, b, k=k: a * b + k))
    for k in range(1, 7):
        out.append(('a*b*%d' % k, lambda a, b, k=k: a * b * k))
        out.append(('a+b*%d' % k, lambda a, b, k=k: a + b * k))
        out.append(('a*%d+b' % k, lambda a, b, k=k: a * k + b))
        out.append(('a*%d-b' % k, lambda a, b, k=k: a * k - b))
        out.append(('b*%d+a' % k, lambda a, b, k=k: b * k + a))
        out.append(('b*%d-a' % k, lambda a, b, k=k: b * k - a))
    for k in range(1, 6):
        out.append(('(a+b)*%d' % k, lambda a, b, k=k: (a + b) * k))
        out.append(('(a-b)*%d' % k, lambda a, b, k=k: (a - b) * k))
    for k in range(2, 7):
        out.append(('(a*b)/%d' % k, lambda a, b, k=k: a * b // k if (a * b) % k == 0 else None))
        out.append(('(a+b)/%d' % k, lambda a, b, k=k: (a + b) // k if (a + b) % k == 0 else None))
    for k in range(-4, 5):
        if k:
            out.append(('a*(b%+d)' % k, lambda a, b, k=k: a * (b + k)))
            out.append(('b*(a%+d)' % k, lambda a, b, k=k: b * (a + k)))
    out.append(('a^2+b', lambda a, b: a * a + b))
    out.append(('a^2-b', lambda a, b: a * a - b))
    out.append(('b^2+a', lambda a, b: b * b + a))
    out.append(('b^2-a', lambda a, b: b * b - a))
    out.append(('a^2+b^2', lambda a, b: a * a + b * b))
    out.append(('a^2-b^2', lambda a, b: a * a - b * b))
    out.append(('a+b+ab', lambda a, b: a + b + a * b))
    for k in range(-10, 11):
        out.append(('ds(a)+ds(b)%+d' % k, lambda a, b, k=k: ds(a) + ds(b) + k))
    out.append(('rev(a+b)', lambda a, b: rev2(a + b)))
    out.append(('rev(a)+rev(b)', lambda a, b: (rev2(a) + rev2(b)) if str(a)[-1] != '0' and str(b)[-1] != '0' else None))
    out.append(('rev(a*b)', lambda a, b: rev2(a * b) if a * b < 100 else None))
    return out


FAMS = row_families()


def fitting(rows):
    fams = []
    for name, f in FAMS:
        ok = True
        for a, b, c in rows:
            try:
                v = f(a, b)
            except Exception:
                ok = False
                break
            if v is None or v != c:
                ok = False
                break
        if ok:
            fams.append((name, f))
    return fams


def check_missing(rows, probe, correct, options):
    """rows: solved (a,b,c) instances; probe: (a,b) with ?. Only `correct` may be
    reachable by any family that fits all solved rows."""
    fams = fitting(rows)
    assert fams, ('no family fits rows', rows)
    hits = set()
    for name, f in fams:
        try:
            v = f(*probe)
        except Exception:
            continue
        if v is not None and str(v) in [str(o) for o in options]:
            hits.add(str(v))
    assert hits == {str(correct)}, ('ambiguous', hits, correct, [(n, f(*probe)) for n, f in fams])
    return fams


subs = []

subs.append(C.sub(
    'missing-number-idea', 'How missing-number puzzles work',
    "A figure — two square grids, or concentric circles, or a triangle of numbers — carries a **hidden rule** connecting its cells. One cell is replaced by '?'. Your job is to extract the rule from the *complete* instances and apply it once.\n\nThe examiner's design guarantees the rule: the same relationship must hold in **every** complete row/segment. So the method is mechanical:\n\n1. **Read two complete rows** (or segments) side by side.\n2. **Test simple candidates** in order: sum, difference, product, 'multiply then add/subtract a constant', square, digit-sum. CGL rules are almost always one of these.\n3. **Confirm the candidate on the second complete row.** A rule that works on one row but not the other is wrong — this single check eliminates nearly every error.\n4. Apply the confirmed rule to the incomplete row.\n\nSpeed note: start from the biggest number in the row and ask 'how do the other two build it?' — most rules build the largest cell from the smaller ones.",
    formulas=[
        C.F('Rule confirmation', 'f(a_1,b_1)=c_1 \\ \\text{and} \\ f(a_2,b_2)=c_2 \\Rightarrow \\text{rule } f', 'Two agreeing instances pin the rule; one instance pins nothing.'),
        C.F('Common families', 'a+b,\\ a-b,\\ a \\times b,\\ ab \\pm k,\\ (a \\pm b)k,\\ a^2 \\pm b,\\ \\text{digitsum}', 'Test sums/products first — they cover ~80% of CGL puzzles.'),
    ],
    tricks=[
        C.T(
            'Two-row confirmation',
            "Never answer from one fitted row. Write the candidate rule symbolically ('c = a×b + 1'), check it on the second complete row, then apply. Ten seconds of checking prevents the most common wrong answer in this topic — a rule that fits only the first row.",
            "**Q.** Row 1: 3 4 13; Row 2: 5 2 11; Row 3: 6 3 ?\n\n**Sol.** Guess c = a×b + 1: check row 2: 5×2 + 1 = 11 ✓. Apply: 6×3 + 1 = **19**.",
            "Guess → confirm on the spare row → apply. In that order, every time."),
    ],
    mistakes=[
        "Fitting a rule to the first row only and answering immediately.",
        "Assuming left-to-right reading of the figure when the rule runs along columns or diagonals.",
        "Over-complicated rules (three operations) when a simple one fits both rows.",
    ]))

subs.append(C.sub(
    'grid-row-rules', 'Grids with row (or column) rules',
    "The classic CGL format: **two complete 3×3 grids and a third with one missing cell** — or a single grid whose rows share a rule. The rule runs row-wise ('in each row, third number = first × second + 1') or column-wise ('third column = first + second'); the reading direction does not matter to the method — a column rule on a grid is a row rule on its transposed rows.\n\n**Attack order** for two-grid puzzles: compare the *first rows* of both grids, then the *second rows*. Whichever pair shares a clean rule gives you f. For single grids, the two complete rows act as the two instances.\n\nTypical CGL rules, with a worked instance each:\n\n- $c = a \\times b + k$: 3, 4, 13 and 5, 2, 11 (k = 1)\n- $c = (a + b) \\times k$: 4, 7, 22 and 6, 3, 18 (k = 2)\n- $c = a \\times (b - 1)$: 6, 3, 15 and 8, 4, 28\n- $c = a^2 - b$: 8, 15, 49 and 7, 10, 39\n- $c = (a + b) \\div 2$: 12, 8, 10 and 20, 6, 13",
    tricks=[
        C.T(
            'Anchor on the largest cell',
            "Write the largest cell of a row first and rebuild it: 22 = (4 + 7) × 2, 49 = 8² − 15, 13 = 26 ÷ 2. Building the largest from the rest exposes the rule faster than scanning left to right.",
            "**Q.** Row 1: 4 7 22; Row 2: 6 3 18; Row 3: 9 5 ?\n\n**Sol.** 22 = (4+7)×2; confirm 18 = (6+3)×2 ✓. Answer (9+5)×2 = **28**.",
            "Largest cell = output; smaller cells = inputs. Almost always true in CGL."),
        C.T(
            'Transcribe the figure as rows',
            "Copy the grid into your rough column as three horizontal rows, question mark included. Reading values off the figure mid-calculation is where transposition errors come from.",
            "**Q.** A grid's rows are 12 8 10 / 20 6 13 / 14 4 ?\n\n**Sol.** 10 = (12+8)÷2 ✓, 13 = (20+6)÷2 ✓, so (14+4)÷2 = **9**.",
            "A three-line transcription beats squinting at the figure."),
    ],
    mistakes=[
        "Mixing up the two grids — applying grid 1's row to grid 2's columns.",
        "Choosing between two half-fitting rules by feel instead of testing both fully.",
        "Arithmetic slips on squares: 13² = 169, not 196.",
    ]))

subs.append(C.sub(
    'digit-operations', 'Digit-sum and digit-reversal rules',
    "A chunk of CGL missing-number puzzles operate on **digits**, not values:\n\n- **Digit-sum rule**: $c = \\text{digitsum}(a) + \\text{digitsum}(b) \\pm k$, e.g. 28, 9, 21 since 10 + 9 + 2 = 21 and 36, 23, 16 since 9 + 5 + 2 = 16.\n- **Reversal rule**: $c = \\text{reverse}(a + b)$, e.g. 43 + 14 = 57 → **75**; 34 + 43 = 77 → 77.\n\nThese look alien at first glance precisely because the *values* don't line up — that mismatch is the tell. If neither sums, products, nor squares fit the two complete rows, test digit operations before anything exotic.\n\nDigit-sum speed: add digits in pairs, and remember a number and its digit-sum are equal mod 9 — so digit-sum questions never need long addition.",
    tricks=[
        C.T(
            'The mismatch trigger',
            "If 30 seconds of standard rules fails on both rows, immediately test: (i) digit sums, (ii) reversed sum, (iii) product of digit sums. One of these fits in the large majority of 'stuck' puzzles.",
            "**Q.** 28 9 21 / 36 23 16 / 45 17 ?\n\n**Sol.** Sums/products fail. Digit sums: 10 + 9 = 19, and 21 − 19 = 2; confirm 9 + 5 = 14, 16 − 14 = 2 ✓. Answer 9 + 8 + 2 = **19**.",
            "Standard rules fail → digit operations, tested with the same two-row confirmation."),
        C.T(
            'Reversal sanity check',
            "A reversed-digit answer must read backwards cleanly: reverse(57) = 75. If the sum ends in 0 the reversal is not defined for CGL purposes — such puzzles avoid those sums, so if your sum ends in 0 you have the wrong rule.",
            "**Q.** 24 18 24 / 32 13 54 / 26 15 ?\n\n**Sol.** 24 + 18 = 42 → reversed 24 ✓; 32 + 13 = 45 → reversed 54 ✓. So 26 + 15 = 41 → reversed **14**.",
            "Sum first, then flip the two digits — a two-step rule, confirmed on two rows."),
    ],
    mistakes=[
        "Reversing the inputs instead of the sum (43 → 34) when the rule reverses the result.",
        "Digit-sum slips on numbers containing 0 or repeated digits.",
        "Abandoning the two-instance confirmation because the rule 'looks digital' — confirm it anyway.",
    ]))

patterns = [
    C.P('Two grids, row rule', 'very common',
        "Two complete grids plus a third carrying one '?'.",
        "Compare matching rows of the two complete grids, extract f, confirm, apply."),
    C.P('Single grid, rows share a rule', 'very common',
        "One grid; two rows complete, third row holds '?'.",
        "Fit f on rows 1–2, confirm, evaluate on row 3."),
    C.P('Column rule in a single grid', 'common',
        "Third column built from the first two: read each row as (a, b, c) and proceed identically.",
        "Transpose mentally: a column rule is a row rule on (col1, col2, col3)."),
    C.P('Circle / triangle segments', 'common',
        "Numbers arranged in sectors; each sector is a triplet.",
        "Treat each sector as a row; the complete sectors are your two instances."),
    C.P('Digit-sum rule', 'common',
        "Values resist sums/products/squares for two full seconds.",
        "Test c = digitsum(a) + digitsum(b) ± k with two-row confirmation."),
    C.P('Reversed-sum rule', 'occasional',
        "Third cell looks like a scrambled sum of the first two.",
        "Compute a + b, reverse the digits, confirm on the second row."),
]

examples = []

# ex1: sum = 20 rule across two grids
fams = check_missing([(7, 9, 4), (8, 5, 7)], (11, 3), 6, ['6', '5', '8', '4'])
examples.append(C.Q(
    'rsn-missing-number-ex1',
    "Study the pattern and find the missing number.\n\n**Grid 1:** 7, 9, 4  **Grid 2:** 8, 5, 7  **Grid 3:** 11, 3, ?\n\n(In each grid, the numbers are read left to right as one row.)",
    ['6', '5', '8', '4'], '6',
    "Test the row rule on both complete grids: 7 + 9 + 4 = 20 and 8 + 5 + 7 = 20 — the **row sum is always 20**. So 11 + 3 + ? = 20 → ? = **6**.",
    sc="Add a complete row; if two complete rows share the same total, the rule is 'sum = constant'.",
    d='easy', sub='grid-row-rules', pat='two grids, row rule', t=40))

# ex2: single grid rows c = a*b
check_missing([(4, 3, 12), (5, 4, 20)], (7, 2), 14, ['14', '9', '18', '21'])
examples.append(C.Q(
    'rsn-missing-number-ex2',
    "Find the missing number:\n\n**4   3   12**\n\n**5   4   20**\n\n**7   2   ?**",
    ['14', '9', '18', '21'], '14',
    "Each row: third = first × second. Check: 4×3 = 12 ✓; 5×4 = 20 ✓. So 7 × 2 = **14**.",
    sc="The largest cell factorises neatly into the other two — test the product rule first.",
    d='easy', sub='grid-row-rules', pat='single grid, rows share a rule', t=35))

# ex3: reversal rule
fams = check_missing([(24, 18, 24), (32, 13, 54)], (26, 15), 14, ['14', '41', '51', '62'])
examples.append(C.Q(
    'rsn-missing-number-ex3',
    "Find the missing number:\n\n**24   18   24**\n\n**32   13   54**\n\n**26   15   ?**",
    ['14', '41', '51', '62'], '14',
    "Plain sums fail (42 ≠ 24 as a value... but 24 is 42 reversed). Rule: **reverse the digits of (first + second)**. Check: 24+18 = 42 → 24 ✓; 32+13 = 45 → 54 ✓. So 26+15 = 41 → reversed = **14**. (41 is the unreversed sum — the planted trap.)",
    sc="When sums 'almost' match, check whether the third cell is the reversed sum.",
    d='medium', sub='digit-operations', pat='reversed-sum rule', t=50))

# ex4: digit-sum rule
check_missing([(28, 9, 21), (36, 23, 16)], (45, 17), 19, ['19', '17', '21', '26'])
examples.append(C.Q(
    'rsn-missing-number-ex4',
    "Find the missing number:\n\n**28    9    21**\n\n**36   23   16**\n\n**45   17    ?**",
    ['19', '17', '21', '26'], '19',
    "Digit-sum rule: third = digit-sum(first) + digit-sum(second) + 2. Check: 10 + 9 + 2 = 21 ✓; 9 + 5 + 2 = 16 ✓. So 9 + 8 + 2 = **19**.",
    sc="Sums/products fail → add the digits of each number, then look for the constant.",
    d='medium', sub='digit-operations', pat='digit-sum rule', t=50))

# ---------------------------------------------------------------- practice
pr = []

# 1: c = a*b + 1
check_missing([(3, 4, 13), (5, 2, 11)], (6, 3), 19, ['19', '18', '21', '15'])
pr.append(C.Q(
    'rsn-missing-number-1',
    "Find the missing number:\n\n**3   4   13**\n\n**5   2   11**\n\n**6   3   ?**",
    ['19', '18', '21', '15'], '19',
    "Rule: third = first × second + 1. Check: 3×4 + 1 = 13 ✓; 5×2 + 1 = 11 ✓. So 6×3 + 1 = **19**. (18 is the bare product — the near-miss trap.)",
    sc="Product first, then look for the small constant: +1 here.",
    d='easy', sub='grid-row-rules', pat='single grid, rows share a rule', t=35))

# 2: c = a - b
check_missing([(9, 2, 7), (12, 5, 7)], (15, 9), 6, ['6', '7', '8', '24'])
pr.append(C.Q(
    'rsn-missing-number-2',
    "Find the missing number:\n\n**9    2    7**\n\n**12   5    7**\n\n**15   9    ?**",
    ['6', '7', '8', '24'], '6',
    "Rule: third = first − second. Check: 9−2 = 7 ✓; 12−5 = 7 ✓. So 15 − 9 = **6**. (7 repeats in the first two rows — do not copy it into the third.)",
    sc="Same answer twice in a row is a coincidence trap; always derive, never pattern-copy.",
    d='easy', sub='grid-row-rules', pat='single grid, rows share a rule', t=30))

# 3: c = (a+b)*2
check_missing([(4, 7, 22), (6, 3, 18)], (9, 5), 28, ['28', '45', '14', '24'])
pr.append(C.Q(
    'rsn-missing-number-3',
    "Find the missing number:\n\n**4   7   22**\n\n**6   3   18**\n\n**9   5    ?**",
    ['28', '45', '14', '24'], '28',
    "22 = (4+7)×2; confirm 18 = (6+3)×2 ✓. Rule: third = (first + second) × 2. So (9+5)×2 = **28**. (45 is 9×5 — the product trap.)",
    sc="Large third cell with modest inputs → try (a+b)×k or a×b first.",
    d='easy', sub='grid-row-rules', pat='single grid, rows share a rule', t=35))

# 4: c = b*(a-1)
check_missing([(6, 3, 15), (8, 4, 28)], (5, 7), 28, ['28', '30', '35', '12'])
pr.append(C.Q(
    'rsn-missing-number-4',
    "Find the missing number:\n\n**6   3   15**\n\n**8   4   28**\n\n**5   7    ?**",
    ['28', '30', '35', '12'], '28',
    "15 = 3×(6−1) and 28 = 4×(8−1). Rule: third = second × (first − 1). So 7 × (5−1) = **28**. (35 = 7×5, ignoring the −1.)",
    sc="When a×b overshoots (30 vs 15), test a×(b−1) or b×(a−1) — the 'one less' family.",
    d='medium', sub='grid-row-rules', pat='single grid, rows share a rule', t=45))

# 5: digit-sum + 2
check_missing([(29, 14, 18), (38, 25, 20)], (56, 13), 17, ['17', '16', '15', '19'])
pr.append(C.Q(
    'rsn-missing-number-5',
    "Find the missing number:\n\n**29   14   18**\n\n**38   25   20**\n\n**56   13    ?**",
    ['17', '16', '15', '19'], '17',
    "Digit sums: 29 → 11, 14 → 5; 11 + 5 = 16 and 18 − 16 = 2. Confirm: 38 → 11, 25 → 7; 11 + 7 + 2 = 20 ✓. Rule: third = digitsum(first) + digitsum(second) + 2. So 11 + 4 + 2 = **17**.",
    sc="Standard rules dead for two seconds → switch to digit sums and find the constant.",
    d='medium', sub='digit-operations', pat='digit-sum rule', t=50))

# 6: c = a^2 - b
check_missing([(8, 15, 49), (7, 10, 39)], (6, 11), 25, ['25', '47', '36', '30'])
pr.append(C.Q(
    'rsn-missing-number-6',
    "Find the missing number:\n\n**8   15   49**\n\n**7   10   39**\n\n**6   11    ?**",
    ['25', '47', '36', '30'], '25',
    "49 = 8² − 15; confirm 39 = 7² − 10 = 49 − 10 ✓. Rule: third = (first)² − second. So 6² − 11 = 36 − 11 = **25**. (36 is 6² without subtracting 11.)",
    sc="Perfect-square third cells (49, 39? not 39... their bases 7, 7) — here the bases equal the first cell: test a² ± b.",
    d='medium', sub='grid-row-rules', pat='single grid, rows share a rule', t=45))

# 7: c = (a+b)/2
check_missing([(12, 8, 10), (20, 6, 13)], (14, 4), 9, ['9', '18', '10', '8'])
pr.append(C.Q(
    'rsn-missing-number-7',
    "Find the missing number:\n\n**12    8   10**\n\n**20    6   13**\n\n**14    4    ?**",
    ['9', '18', '10', '8'], '9',
    "10 = (12+8) ÷ 2; confirm 13 = (20+6) ÷ 2 = 26 ÷ 2 ✓. Rule: third = average of first two. So (14+4) ÷ 2 = **9**. (18 is the un-divided sum.)",
    sc="Third cell sitting between the other two → test their average.",
    d='easy', sub='grid-row-rules', pat='single grid, rows share a rule', t=35))

# 8: c = a*(b-1)
check_missing([(5, 6, 25), (7, 4, 21)], (9, 3), 18, ['18', '27', '24', '12'])
pr.append(C.Q(
    'rsn-missing-number-8',
    "Find the missing number:\n\n**5   6   25**\n\n**7   4   21**\n\n**9   3    ?**",
    ['18', '27', '24', '12'], '18',
    "25 = 5×(6−1); confirm 21 = 7×(4−1) ✓. Rule: third = first × (second − 1). So 9 × (3−1) = **18**. (27 = 9×3 is the bare product.)",
    sc="a×b too big by exactly a (or b) → the second factor carries a −1.",
    d='medium', sub='grid-row-rules', pat='single grid, rows share a rule', t=45))

# 9: column rule on a single grid (third column = first + second)
check_missing([(6, 5, 11), (9, 4, 13)], (8, 7), 15, ['15', '12', '13', '56'])
pr.append(C.Q(
    'rsn-missing-number-9',
    "Find the missing number:\n\n**6    5   11**\n\n**9    4   13**\n\n**8    7    ?**",
    ['15', '12', '13', '56'], '15',
    "In each row, third column = first + second: 6+5 = 11 ✓; 9+4 = 13 ✓. So 8 + 7 = **15**. (56 = 8×7 is the product trap.)",
    sc="Column-wise rule — read each row as (a, b, a+b); the check rows confirm instantly.",
    d='easy', sub='grid-row-rules', pat='column rule in a single grid', t=35))

# 10: (a-b)*4 segments
check_missing([(15, 12, 12), (20, 11, 36)], (17, 9), 32, ['32', '36', '27', '8'])
pr.append(C.Q(
    'rsn-missing-number-10',
    "Numbers are given in segments of a circular figure, each segment read as (outer, inner, centre):\n\n**15   12   12**\n\n**20   11   36**\n\n**17    9    ?**",
    ['32', '36', '27', '8'], '32',
    "12 = (15−12)×4; confirm 36 = (20−11)×4 = 9×4 ✓. Rule: centre = (outer − inner) × 4. So (17−9)×4 = **32**. (36 repeats the previous centre — a copy trap.)",
    sc="Small centres from big outers → difference × constant is the natural family.",
    d='medium', sub='grid-row-rules', pat='circle / triangle segments', t=45))

# 11: reversal with tricky distractors
fams = check_missing([(43, 14, 75), (34, 43, 77)], (26, 15), 14, ['14', '41', '51', '62'])
assert any(n == 'rev(a+b)' for n, f in fams)
pr.append(C.Q(
    'rsn-missing-number-11',
    "Find the missing number:\n\n**43   14   75**\n\n**34   43   77**\n\n**26   15    ?**",
    ['14', '41', '51', '62'], '14',
    "43 + 14 = 57 → reversed = 75 ✓; 34 + 43 = 77 → reversed = 77 ✓. Rule: third = reverse(first + second). So 26 + 15 = 41 → **14**. (41, 51, 62 are the sum and the reversed inputs — all traps.)",
    sc="Palindrome check row (77 → 77) is the giveaway that reversal is involved.",
    d='hard', sub='digit-operations', pat='reversed-sum rule', t=55))

# 12: a*b - (a+b)
check_missing([(9, 5, 31), (8, 6, 34)], (10, 4), 26, ['26', '36', '40', '30'])
pr.append(C.Q(
    'rsn-missing-number-12',
    "Find the missing number:\n\n**9   5   31**\n\n**8   6   34**\n\n**10  4    ?**",
    ['26', '36', '40', '30'], '26',
    "31 = 45 − 14 = 9×5 − (9+5); confirm 34 = 48 − 14 = 8×6 − (8+6) ✓. Rule: third = product − sum. So 40 − 14 = **26**. (40 is the bare product.)",
    sc="Constant 14 = a+b in both rows — subtract the sum from the product.",
    d='hard', sub='grid-row-rules', pat='single grid, rows share a rule', t=55))

# 13: simple sum rows (grid) — all third cells equal 13
check_missing([(4, 9, 13), (7, 6, 13)], (5, 8), 13, ['13', '40', '21', '3'])
pr.append(C.Q(
    'rsn-missing-number-13',
    "Find the missing number:\n\n**4    9   13**\n\n**7    6   13**\n\n**5    8    ?**",
    ['13', '40', '21', '3'], '13',
    "Third = first + second: 4 + 9 = 13 and 7 + 6 = 13. So 5 + 8 = **13**. The repeated 13s tempt you to copy — derive it; the rule happens to give 13 again, but only the derivation proves it. (40 = 5×8 is the product trap.)",
    sc="When every third cell matches, verify the sum rule before trusting a copy.",
    d='easy', sub='grid-row-rules', pat='single grid, rows share a rule', t=30))

# 14: a^2 - b^2
check_missing([(10, 6, 64), (12, 4, 128)], (9, 5), 56, ['56', '45', '70', '85'])
pr.append(C.Q(
    'rsn-missing-number-14',
    "Find the missing number:\n\n**10    6    64**\n\n**12    4   128**\n\n**9     5     ?**",
    ['56', '45', '70', '85'], '56',
    "64 = 100 − 36 = 10² − 6²; confirm 128 = 144 − 16 = 12² − 4² ✓. Rule: third = a² − b². So 81 − 25 = **56**. (45 = 9×5 is the product trap; 70 and 85 come from slipping the squares.)",
    sc="Both inputs squaring cleanly and a big third cell → a² − b².",
    d='hard', sub='grid-row-rules', pat='single grid, rows share a rule', t=60))

# 15: a+b+ab
check_missing([(7, 3, 31), (5, 6, 41)], (4, 8), 44, ['44', '40', '36', '32'])
pr.append(C.Q(
    'rsn-missing-number-15',
    "Find the missing number:\n\n**7   3   31**\n\n**5   6   41**\n\n**4   8    ?**",
    ['44', '40', '36', '32'], '44',
    "31 = 21 + 10 = 7×3 + 7 + 3; confirm 41 = 30 + 11 = 5×6 + 5 + 6 ✓. Rule: third = ab + a + b = (a+1)(b+1) − 1. So 32 + 4 + 8 = **44**. (40 = ab + 10 is the near-miss.)",
    sc="ab + a + b factorises as (a+1)(b+1) − 1 — a fast mental identity.",
    d='hard', sub='grid-row-rules', pat='single grid, rows share a rule', t=60))

assert len(pr) == 15

t = C.topic(
    'missing-number', 'Missing Number', 'medium', {'tier1': '1-2', 'tier2': '1-2'},
    "Figure-based puzzles — paired grids, single grids, circles — where one cell is hidden behind a numerical rule. Every rule connects the cells of a row (or segment), and the same rule is demonstrated by at least two complete instances. The winning habit is two-line verification: fit the rule on one complete row, confirm on the other, then apply. Digit-sum and digit-reversal variants reward students who switch families quickly when plain arithmetic stalls.",
    subs, patterns, examples, pr)

C.write_topic(t)
print('OK missing-number')
