# build series topic (number + letter + alphanumeric + wrong-number)
import common as C


def check_wrong_number(given, wrong_value, rule, n0=1):
    """rule(i) = correct i-th term. Exactly the position holding wrong_value may mismatch."""
    mism = [i for i, v in enumerate(given, start=n0) if rule(i) != v]
    wpos = given.index(wrong_value) + n0
    assert mism == [wpos], (mism, wpos, [rule(i) for i in range(n0, n0 + len(given))])
    fixed = [rule(i) for i in range(n0, n0 + len(given))]
    assert fixed[wpos - n0] != wrong_value
    return fixed


def check_alpha(letters, numbers, ans_letter, ans_num, opts, num_rule='ap'):
    """letters/numbers: given tracks (no '?'); assert tracks follow one simple rule; assemble
    answer; every wrong option must fail at least one track."""
    seq_l = list(letters) + [ans_letter]
    lsteps = [((C.p(seq_l[i + 1]) - C.p(seq_l[i])) % 26) for i in range(len(seq_l) - 1)]
    assert len(set(lsteps)) == 1, lsteps
    if num_rule == 'ap':
        nsteps = [numbers[i + 1] - numbers[i] for i in range(len(numbers) - 1)] + [ans_num - numbers[-1]]
        ok = len(set(nsteps)) == 1
        nfits = lambda n: len(set(n)) == 1
    else:
        nsteps = [numbers[i + 1] / numbers[i] for i in range(len(numbers) - 1)] + [ans_num / numbers[-1]]
        ok = len(set(nsteps)) == 1
        nfits = lambda n: len(set(n)) == 1
    assert ok, nsteps
    correct = ans_letter + str(ans_num)
    assert correct in opts
    for o in opts:
        if o == correct:
            continue
        ol = list(lsteps)
        ol[-1] = ((C.p(o[0]) - C.p(seq_l[-2])) % 26)
        if num_rule == 'ap':
            on = [numbers[i + 1] - numbers[i] for i in range(len(numbers) - 1)] + [int(o[1:]) - numbers[-1]]
        else:
            on = [numbers[i + 1] / numbers[i] for i in range(len(numbers) - 1)] + [int(o[1:]) / numbers[-1]]
        assert (len(set(ol)) > 1) or (not nfits(on)), ('wrong option also fits both tracks', o)
    return correct


subs = []

subs.append(C.sub(
    'series-idea', 'How every series is cracked',
    "A series question shows 5-6 terms and asks for the next (or a missing middle) term. Every CGL series is built by one small rule — your job is to name it before the clock names it for you.\n\n**The universal method: the difference ladder.** Subtract neighbours. If the differences are constant, you have an AP. If not, subtract again (second differences). Repeat until a row is constant, then climb back up. Most CGL series die at the second row. If differences *look* meaningless, switch families: multiply (GP), alternate, or squares/cubes.\n\nReading the ladder tells you the family instantly:\n\n| What you see | Family to try |\n|---|---|\n| Differences constant | AP (add k) |\n| Second differences constant | based on n² |\n| Each term ≈ previous × k | GP / ×k ± r |\n| Ratios of differences constant | ×k on differences |\n| Two clean mini-rows (odd/even positions) | interleaved series |\n| Differences are 1, 8, 27... or 1, 3, 5... | cubes / odd numbers added |",
    tricks=[C.T(
        'Difference ladder in 10 seconds',
        "Write the terms with gaps and subtract under them, twice if needed. A constant row anywhere fixes the whole rule; extend the row one step and climb back up to get the answer.",
        "**Q.** 9, 16, 25, 36, 49, ?\n\n**Sol.** Differences: 7, 9, 11, 13 → next 15. 49 + 15 = **64**. (One glance confirms these are squares 3² to 8² — both readings give 64.)",
        "Ladder first; family names come free afterwards."),
    ],
    mistakes=[
        "Extending only the difference row and forgetting to add back to the last term.",
        "Trying exotic rules before finishing the ladder — 80% of CGL series are ladder-friendly.",
        "Assuming the missing term is always last; CGL often hides '?' in the middle, where the ladder must run both ways.",
    ]))

subs.append(C.sub(
    'number-series', 'Number series',
    "The CGL number-series rule bank, in frequency order:\n\n1. **Linear recurrence**: a(n+1) = k·a(n) ± r — e.g. 5, 11, 23, 47, 95 is ×2 + 1.\n2. **Second-difference (n² family)**: 2, 6, 12, 20, 30 is n² + n; 3, 8, 15, 24 is n² − 1.\n3. **Cube/jump differences**: differences are 1, 8, 27, 64 (cubes) or 1, 2, 4, 8 (powers of 2).\n4. **Rising multipliers**: ×2, ×3, ×4 — e.g. 7, 14, 42, 168, 840.\n5. **Alternating/interleaved**: two mini-series on odd and even positions.\n6. **Fibonacci style**: each term = sum of previous two.\n\n**Uniqueness discipline**: after guessing the rule, check it reproduces *every* given term — not just the last. If two rules both fit, the exam keeps the second rule's answer out of the options; if your answer is missing, drop the rule, don't force it.",
    formulas=[
        C.F('AP / ladder', 'a_n = a_1 + (n-1)d', 'd = common difference from the ladder.'),
        C.F('Recurrence xk plus r', 'a_{n+1} = k \\cdot a_n \\pm r', 'Test k = 2, 3 first with r = ±1, ±2.'),
        C.F('n-squared family', 'a_n = n^2 \\pm k \\text{ or } n^2 + n', 'Second difference 2 ⇒ n²; second difference 2k ⇒ k·n².'),
        C.F('Geometric', 'a_n = a_1 \\cdot r^{\\,n-1}', 'Constant ratio r; check ×2, ×3, ×1.5.'),
    ],
    tricks=[
        C.T(
            'Ratio test before exotic rules',
            "Divide each term by the previous one. Constant ratio → GP. Ratio drifting by +1 each time → rising multipliers. Neither → back to the ladder.",
            "**Q.** 7, 14, 42, 168, ?\n\n**Sol.** Ratios: 2, 3, 4 → next ratio 5. 168 × 5 = **840**.",
            "One division per gap; rising multipliers announce themselves immediately."),
        C.T(
            'Interleaved split for jumpy series',
            "If the series jumps up-down-up-down, write odd-position terms in one row and even-position terms below. Each row is a friendly AP/GP; extend both, then read the term that falls on '?'",
            "**Q.** 2, 9, 4, 13, 6, 17, ?\n\n**Sol.** Row A (odd): 2, 4, 6 → 8. Row B (even): 9, 13, 17 → 21. '?' is 7th term → **8**.",
            "Splitting kills panic; each row is solvable in 3 seconds."),
        C.T(
            'Cubes and powers hiding in the ladder',
            "Memorise the signature ladders: 1, 8, 27, 64 (cubes), 1, 3, 5, 7 (odds), 2, 4, 8, 16 (powers of 2), 1, 4, 9, 16 (squares). When the first difference row matches a signature, the series is solved.",
            "**Q.** 12, 13, 21, 48, 112, ?\n\n**Sol.** Differences: 1, 8, 27, 64 → cubes! Next difference 125. 112 + 125 = **237**.",
            "The ladder names the family — never subtract twice when the first row already looks famous."),
    ],
    mistakes=[
        "Fitting ×2+1 from the first pair only and never verifying on the third term.",
        "Missing mixed operators (×2+1 vs ×2) — check the residual r on every step.",
        "In interleaved series, reading the answer from the wrong row (count positions carefully).",
    ]))

subs.append(C.sub(
    'letter-series', 'Letter series',
    "Letters hide number series. Convert A=1 ... Z=26 (EJOTY: E=5, J=10, O=15, T=20, Y=25) and every letter series becomes a number series with wrap-around after Z.\n\nTypical CGL letter rules:\n1. **Constant step per letter**: B, D, F, H (+2 each).\n2. **Rising step**: B, D, G, K, P (steps 2, 3, 4, 5).\n3. **Alternating steps**: A, C, B, D, C, E (steps +2, −1 repeating).\n4. **Two-track clusters**: in 'AZ, BY, CX' the first letters climb +1 while second letters fall −1.\n\nTreat multi-letter clusters slot by slot — each letter-position is its own mini-series.",
    formulas=[
        C.F('Slot steps', 's_i = Q(L_{i+1}) - Q(L_i) \\pmod{26}', 'Steps per slot decide the rule; wrap Y→B counts as +3.'),
        C.F('Two-track cluster', 'Q(\\text{first}_i) = a + d_1 i,\\quad Q(\\text{second}_i) = b + d_2 i', 'Tracks are independent; solve both.'),
    ],
    tricks=[
        C.T(
            'Step row under the letters',
            "Write positions over the letters and steps between them. One clean step row (+2, +2, +2...) or a rising row (2, 3, 4, 5) ends the question.",
            "**Q.** B, D, G, K, ?\n\n**Sol.** Steps: +2, +3, +4 → next +5. K(11) + 5 = P(16) → **P**.",
            "Steps convert letters to arithmetic — never eyeball letter gaps."),
        C.T(
            'Wrap-around fluency',
            "After Z the alphabet restarts: Y + 4 = C. Practise from EJOTY anchors — every jump is at most 13, take the shorter direction.",
            "**Q.** X, Z, B, ?\n\n**Sol.** X(24) +2 = Z(26), Z + 2 = B(2), B + 2 = **D**. The +2 step survives the wrap.",
            "Wrap steps are the number one source of wrong letter answers — always add positions mod 26."),
    ],
    mistakes=[
        "Counting backwards through Z incorrectly (Z − 2 is X, not 'nothing').",
        "Missing rising steps: treating +2, +3, +4 as a flat '+3 average' gives a wrong letter.",
        "Applying one track's step to both tracks of a cluster pair.",
    ]))

subs.append(C.sub(
    'alphanumeric-series', 'Alphanumeric series',
    "Terms mix a letter and a number ('A3, D6, G9, J12, ?'). The letter track and the number track are **independent series**. Solve each separately, then bolt the answer together: letter from track 1, number from track 2.\n\nCommon track rules: letters step ±2/±3 (or reverse), numbers run an AP (step 3), a ×2 GP, or squares (1, 4, 9, 16). Nothing couples the tracks — if you ever need the number to compute the letter, you have misread the question.",
    tricks=[C.T(
        'Two columns, two answers, one bolt',
        "Make a letter column and a number column. Solve the letter column (step row), solve the number column, then write them side by side in the original order.",
        "**Q.** A3, D6, G9, J12, ?\n\n**Sol.** Letters: A, D, G, J (+3) → M. Numbers: 3, 6, 9, 12 (+3) → 15. Answer **M15**.",
        "Tracks are independent — an error stays inside one column."),
    ],
    mistakes=[
        "Reading 'A3' as one base-30 code instead of two independent tracks.",
        "Multiplying numbers when the track is a plain AP (check +3 vs ×2 quickly).",
        "Mixing up the bolt order (writing 15M) — always mirror the question's order.",
    ]))

subs.append(C.sub(
    'wrong-number', 'Wrong number in the series',
    "Here the series is **already complete** but one term was corrupted. You must find which term breaks the rule — not what should replace it. Method: build the difference ladder as usual; the corrupted term shows up as the place where the ladder stops making sense.\n\nStrategy: test the rule on terms 1-3 and terms 4-6 separately. The half that agrees gives you the family; the term in the other half that refuses to fit is the culprit. Verify by checking that the rule reproduces **all other terms exactly**.",
    tricks=[C.T(
        'Ladder with one broken rung',
        "Compute all differences; all but one gap will follow the pattern (constant, rising, doubling). The term touching the odd gap(s) is the wrong one.",
        "**Q.** 2, 5, 10, 17, 26, 38\n\n**Sol.** These should be n² + 1: 2, 5, 10, 17, 26, **37**. The last term 38 breaks it → **38** is wrong. (Differences 3, 5, 7, 9 are clean; the last jump is 12, not 11.)",
        "Find the family from the clean majority; the leftover term is the answer."),
    ],
    mistakes=[
        "Reporting the *correct* value (37) instead of the wrong given term (38) — read the question twice.",
        "Choosing a rule that fits only the first three terms; always test it on the tail too.",
        "Forgetting that exactly ONE term is wrong — if two refuse to fit, your family is wrong.",
    ]))

patterns = [
    C.P('Number series — second-difference (n² family)',
        'very common',
        "Differences form an AP (4, 6, 8, 10...) so second differences are constant.",
        "Ladder to the constant row, extend one step, climb back. Recognise n²+n and n²−1 shapes."),
    C.P('Number series — recurrence ×k ± r',
        'very common',
        "Each term is k times the previous plus a small constant (×2+1, ×3−2...).",
        "Ratio test then fit k and r on the first two steps; verify on the third before extending."),
    C.P('Letter series — constant or rising step',
        'very common',
        "Single letters with a fixed step (BDFH) or steps rising by 1 (BDGKP).",
        "Position + step row; EJOTY anchors make each jump oral."),
    C.P('Number series — cube/odd/powered differences',
        'common',
        "First difference row matches a famous series: 1, 8, 27... or 1, 3, 5... or 2, 4, 8...",
        "Memorise the signature ladders; extend the signature and add back."),
    C.P('Interleaved two-in-one series',
        'common',
        "Terms alternate between two independent mini-series (2, 9, 4, 13, 6, 17...).",
        "Split odd/even positions into two rows; extend both; read the row owning '?'."),
    C.P('Wrong number identification',
        'common',
        "A complete series where exactly one term breaks the rule; options are terms of the series.",
        "Ladder shows the broken rung; verify the rule reproduces every other term."),
    C.P('Alphanumeric two-track series',
        'common',
        "Terms like A3, D6, G9 mix a letter track and a number track.",
        "Two independent columns; solve each; bolt the answer in the question's order."),
    C.P('Letter-cluster series (slot steps)',
        'common',
        "Clusters like AZ, BY, CX or AD, CF, EH advance by fixed steps per slot.",
        "One step row per slot; apply the final step to the last cluster."),
]

# ---------------------------------------------------------------- solved examples
examples = []
C.check_number_series([2, 6, 12, 20, 30, '?'], [42, 40, 44, 46], 42, must_fit='D2')
examples.append(C.Q(
    'rsn-series-ex1',
    "Find the next term: **2, 6, 12, 20, 30, ?**",
    [42, 40, 44, 46],
    42,
    "Differences: 4, 6, 8, 10 → next difference 12. 30 + 12 = **42**. (Terms are n² + n: 1²+1, 2²+2, ... 6²+6 = 42.)",
    sc="Ladder once → differences rise by 2 → add 12. Never compute 6² + 6 from scratch unless the ladder stalls.",
    d='easy', sub='number-series', pat='number series — second-difference (n² family)', t=35))

C.check_number_series([5, 11, 23, 47, 95, '?'], [191, 189, 193, 187], 191, must_fit='LIN')
examples.append(C.Q(
    'rsn-series-ex2',
    "Find the next term: **5, 11, 23, 47, 95, ?**",
    [191, 189, 193, 187],
    191,
    "Ratios hover near 2: test ×2 + 1. 5×2+1 = 11 ✓, 11×2+1 = 23 ✓, 23×2+1 = 47 ✓, 47×2+1 = 95 ✓. So 95×2+1 = **191**.",
    sc="Verified recurrence in four seconds — check k·a±r on every step, not just the first.",
    d='easy', sub='number-series', pat='number series — recurrence ×k ± r', t=35))

C.check_letter_series(['B', 'D', 'G', 'K', '?'], ['P', 'Q', 'O', 'N'], 'P')
examples.append(C.Q(
    'rsn-series-ex3',
    "Find the next letter: **B, D, G, K, ?**",
    ['P', 'Q', 'O', 'N'],
    'P',
    "Steps: B→D +2, D→G +3, G→K +4 → next step +5. K(11) + 5 = 16 → **P**.",
    sc="Rising steps 2, 3, 4, 5 — write the step row, then jump from T? No: from K using EJOTY (K is 11, +5 → 16 = P).",
    d='easy', sub='letter-series', pat='letter series — constant or rising step', t=35))

fixed = check_wrong_number([3, 6, 12, 24, 46, 96], 46, lambda i: 3 * 2 ** (i - 1))
assert fixed == [3, 6, 12, 24, 48, 96]
C.simple_rules([3, 6, 12, 24, 48, 96])
examples.append(C.Q(
    'rsn-series-ex4',
    "Find the wrong term: **3, 6, 12, 24, 46, 96**",
    ['6', '12', '24', '46'],
    '46',
    "The clean reading is ×2: 3, 6, 12, 24, **48**, 96. Every step doubles except 24 → 46 → **46** is the wrong term.",
    sc="Ratio test: 2, 2, 2, ~1.9, ~2.09 — the odd ratio sits on 46.",
    d='medium', sub='wrong-number', pat='wrong number identification', t=40))

# ---------------------------------------------------------------- practice
pr = []

# 1 D2 number
C.check_number_series([100, 96, 88, 76, 60, '?'], [40, 44, 42, 36], 40, must_fit='D2')
pr.append(C.Q('rsn-series-1',
              "Find the next term: **100, 96, 88, 76, 60, ?**",
              [40, 44, 42, 36],
              40,
              "Differences: −4, −8, −12, −16 → next −20. 60 − 20 = **40**.",
              sc="Second difference constant (−4) → extend the difference row and climb back.",
              d='easy', sub='number-series', pat='number series — second-difference (n² family)', t=35))

# 2 GP
C.check_number_series([4, 12, 36, 108, '?'], [324, 216, 312, 340], 324, must_fit='GP')
pr.append(C.Q('rsn-series-2',
              "Find the next term: **4, 12, 36, 108, ?**",
              [324, 216, 312, 340],
              324,
              "Ratio is constant: ×3 each step. 108 × 3 = **324**.",
              sc="Constant ratio → GP; multiply the last term by 3, nothing else.",
              d='easy', sub='number-series', pat='number series — recurrence ×k ± r', t=30))

# 3 cube diffs
C.check_number_series([12, 13, 21, 48, 112, '?'], [237, 236, 225, 240], 237)
pr.append(C.Q('rsn-series-3',
              "Find the next term: **12, 13, 21, 48, 112, ?**",
              [237, 236, 225, 240],
              237,
              "Differences: 1, 8, 27, 64 — perfect **cubes**. Next difference 5³ = 125. 112 + 125 = **237**.",
              sc="The moment the ladder reads 1, 8, 27, 64 you are done — add 125.",
              d='medium', sub='number-series', pat='number series — cube/odd/powered differences', t=40))

# 4 rising multipliers
C.check_number_series([7, 14, 42, 168, '?'], [840, 672, 820, 504], 840)
pr.append(C.Q('rsn-series-4',
              "Find the next term: **7, 14, 42, 168, ?**",
              [840, 672, 820, 504],
              840,
              "Multipliers: ×2, ×3, ×4 → next ×5. 168 × 5 = **840**.",
              sc="Ratio row 2, 3, 4 announces rising multipliers — extend it, don't average it.",
              d='medium', sub='number-series', pat='number series — cube/odd/powered differences', t=40))

# 5 Fibonacci
C.check_number_series([3, 4, 7, 11, 18, 29, '?'], [47, 48, 46, 45], 47)
pr.append(C.Q('rsn-series-5',
              "Find the next term: **3, 4, 7, 11, 18, 29, ?**",
              [47, 48, 46, 45],
              47,
              "Each term is the sum of the previous two: 3+4 = 7, 4+7 = 11, 7+11 = 18, 11+18 = 29. Next: 18+29 = **47**.",
              sc="A slowly accelerating series with no clean ratio is Fibonacci-style — test term(n−1)+term(n−2).",
              d='medium', sub='number-series', pat='number series — cube/odd/powered differences', t=40))

# 6 interleaved
C.check_number_series([2, 9, 4, 13, 6, 17, '?'], [8, 10, 7, 21], 8, must_fit='ALT')
pr.append(C.Q('rsn-series-6',
              "Find the next term: **2, 9, 4, 13, 6, 17, ?**",
              [8, 10, 7, 21],
              8,
              "Split positions: odd slots 2, 4, 6 → next **8**; even slots 9, 13, 17 (+4 each). The 7th term belongs to the odd row → **8**.",
              sc="Up-down jumping = interleaved; solve the row that owns '?'.",
              d='medium', sub='number-series', pat='interleaved two-in-one series', t=40))

# 7 alternating operations
C.check_number_series([96, 48, 50, 25, 27, '?'], [13.5, 13, 15, 54], 13.5)
pr.append(C.Q('rsn-series-7',
              "Find the next term: **96, 48, 50, 25, 27, ?**",
              ['13.5', '13', '15', '54'],
              '13.5',
              "Operations alternate: ÷2, +2, ÷2, +2. So 27 ÷ 2 = **13.5**. (96÷2=48, 48+2=50, 50÷2=25, 25+2=27 ✓.)",
              sc="When ÷ and + alternate, no number series trick applies — just extend the operation cycle.",
              d='medium', sub='number-series', pat='interleaved two-in-one series', t=40))

# 8 middle missing
C.check_number_series([3, 8, 15, '?', 35, 48], [24, 22, 26, 25], 24, must_fit='D2')
pr.append(C.Q('rsn-series-8',
              "Find the missing term: **3, 8, 15, ?, 35, 48**",
              [24, 22, 26, 25],
              24,
              "Differences: 5, 7, 9 then 13 — the middle gap must be **11** (odd numbers). So ? = 15 + 11 = **24**. (Terms are n² − 1: 2²−1 = 3, ..., 7²−1 = 48.)",
              sc="Ladder both ways: the difference row 5, 7, 9, 11, 13 must stay symmetric around the gap.",
              d='medium', sub='number-series', pat='number series — second-difference (n² family)', t=45))

# 9 letter single rising
C.check_letter_series(['A', 'B', 'D', 'G', '?'], ['K', 'L', 'J', 'M'], 'K')
pr.append(C.Q('rsn-series-9',
              "Find the next letter: **A, B, D, G, ?**",
              ['K', 'L', 'J', 'M'],
              'K',
              "Steps: +1, +2, +3 → next +4. G(7) + 4 = 11 → **K**.",
              sc="Step row 1, 2, 3, 4 — add 4 to G using EJOTY (7+4 = 11 = K).",
              d='easy', sub='letter-series', pat='letter series — constant or rising step', t=30))

# 10 letter pairs two-track
C.check_letter_series(['AZ', 'BY', 'CX', '?'], ['DW', 'DV', 'DX', 'EW'], 'DW')
pr.append(C.Q('rsn-series-10',
              "Find the next cluster: **AZ, BY, CX, ?**",
              ['DW', 'DV', 'DX', 'EW'],
              'DW',
              "First letters: A, B, C (+1) → D. Second letters: Z, Y, X (−1) → W. Answer **DW**.",
              sc="Two-track clusters: one row climbs, the other falls — extend both rows independently.",
              d='easy', sub='letter-series', pat='letter-cluster series (slot steps)', t=30))

# 11 letter alternating steps
C.check_letter_series(['A', 'C', 'B', 'D', 'C', 'E', '?'], ['D', 'E', 'C', 'F'], 'D')
pr.append(C.Q('rsn-series-11',
              "Find the next letter: **A, C, B, D, C, E, ?**",
              ['D', 'E', 'C', 'F'],
              'D',
              "Steps alternate: +2, −1, +2, −1, +2 → next −1. E(5) − 1 = **D**.",
              sc="A saw-tooth step row (+2, −1 repeating) — extend the cycle, don't average.",
              d='medium', sub='letter-series', pat='letter series — constant or rising step', t=35))

# 12 letter wrap
C.check_letter_series(['X', 'Z', 'B', '?'], ['D', 'C', 'E', 'F'], 'D')
pr.append(C.Q('rsn-series-12',
              "Find the next letter: **X, Z, B, ?**",
              ['D', 'C', 'E', 'F'],
              'D',
              "Positions: X(24), Z(26), B(2) — steps +2, +2 across the Z-wrap. B(2) + 2 = **D**(4).",
              sc="Wrap-around: add positions mod 26 — Z + 2 restarts at B.",
              d='easy', sub='letter-series', pat='letter series — constant or rising step', t=30))

# 13 alphanumeric +3/+3
ans13 = check_alpha('ADGJ', [3, 6, 9, 12], 'M', 15, ['M15', 'M12', 'N15', 'L15'])
pr.append(C.Q('rsn-series-13',
              "Find the next term: **A3, D6, G9, J12, ?**",
              ['M15', 'M12', 'N15', 'L15'],
              'M15',
              "Letter track: A, D, G, J (+3) → M. Number track: 3, 6, 9, 12 (+3) → 15. Answer **M15**.",
              sc="Two independent +3 columns; bolt the results together.",
              d='easy', sub='alphanumeric-series', pat='alphanumeric two-track series', t=35))

# 14 alphanumeric -2 / x2
ans14 = check_alpha('ZXVT', [1, 2, 4, 8], 'R', 16, ['R16', 'R8', 'S16', 'P16'], num_rule='gp')
pr.append(C.Q('rsn-series-14',
              "Find the next term: **Z1, X2, V4, T8, ?**",
              ['R16', 'R8', 'S16', 'P16'],
              'R16',
              "Letter track: Z, X, V, T (−2 each) → R. Number track: 1, 2, 4, 8 (×2) → 16. Answer **R16**.",
              sc="Letters and numbers follow separate rules — a −2 letter track with a doubling number track.",
              d='medium', sub='alphanumeric-series', pat='alphanumeric two-track series', t=40))

# 15 wrong number
fixed15 = check_wrong_number([2, 5, 10, 17, 26, 38], 38, lambda i: i * i + 1)
assert fixed15 == [2, 5, 10, 17, 26, 37]
pr.append(C.Q('rsn-series-15',
              "Find the wrong term: **2, 5, 10, 17, 26, 38**",
              ['10', '17', '26', '38'],
              '38',
              "Terms follow n² + 1: 1²+1 = 2, 2²+1 = 5, 3²+1 = 10, 4²+1 = 17, 5²+1 = 26, but 6²+1 = **37**, not 38 → **38** is wrong.",
              sc="Differences 3, 5, 7, 9 are clean; the last gap (12) breaks the odd-number ladder.",
              d='medium', sub='wrong-number', pat='wrong number identification', t=40))

topic_obj = C.topic(
    'series', 'Series (Number & Letter)', 'high', {'tier1': 4, 'tier2': 5},
    "Series questions ask for the next or missing term of a number or letter sequence, or the term that spoils a given sequence. CGL asks 4-5 per Tier 1 shift. The universal tool is the difference ladder; the recurring families are AP, ×k±r, squares/cubes, interleaved pairs and stepped letter tracks.",
    subs, patterns, examples, pr)

C.write_topic(topic_obj)
print('OK series')
