# build mathematical-operations topic (topic 5)
from fractions import Fraction
from itertools import combinations
import common as C


def ev(nums, ops):
    """BODMAS evaluation. nums: numbers; ops: '+','-','*','/'. Exact fractions."""
    nums = [Fraction(n) for n in nums]
    ops = list(ops)
    i = 0
    while i < len(ops):
        if ops[i] in '*/':
            a, b = nums[i], nums[i + 1]
            v = a * b if ops[i] == '*' else a / b
            nums[i:i + 2] = [v]
            ops[i:i + 1] = []
        else:
            i += 1
    res = nums[0]
    for o, b in zip(ops, nums[1:]):
        res = res + b if o == '+' else res - b
    return res


def ltr(nums, ops):
    res = Fraction(nums[0])
    for o, b in zip(ops, nums[1:]):
        res = res * b if o == '*' else res / b if o == '/' else (res + b if o == '+' else res - b)
    return res


def fmt(v):
    return str(int(v)) if isinstance(v, int) else (str(int(v)) if Fraction(v).denominator == 1 else '%d/%d' % (Fraction(v).numerator, Fraction(v).denominator))


def py_ops(ops):
    """['+','×','÷','−'] -> ['+','*','/','-']"""
    return {'+': '+', '-': '-', '−': '-', '×': '*', '÷': '/'}[ops] if isinstance(ops, str) else [py_ops(o) for o in ops]


def disp_ops(ops):
    return {'+': '+', '-': '−', '*': '×', '/': '÷'}[ops] if isinstance(ops, str) else [disp_ops(o) for o in ops]


def expr_str(nums, ops):
    out = str(nums[0])
    for o, n in zip(disp_ops(ops), nums[1:]):
        out += ' %s %s' % (o, n)
    return out


def apply_map(ops, mp):
    return [mp.get(o, o) for o in ops]


def swap_vals(nums, i, j):
    n = list(nums)
    n[i], n[j] = n[j], n[i]
    return n


def all_pair_swaps(nums, ops, disp=False):
    """value of expression after swapping every pair of number positions"""
    res = {}
    for i, j in combinations(range(len(nums)), 2):
        res[(nums[i], nums[j])] = ev(swap_vals(nums, i, j), ops)
    return res


subs = []

subs.append(C.sub(
    'mathops-idea', 'Operator puzzles and BODMAS',
    "These questions play with the *operators* of an arithmetic expression: they swap meanings ('+' means '÷'), swap numbers, or ask which equation is correctly balanced. The arithmetic itself is school-level — the test is **discipline**, not maths.\n\nTwo non-negotiables:\n\n1. **Substitute first, calculate second.** Rewrite the expression with the new operators, then compute. Substituting while calculating is where sign slips happen.\n2. **BODMAS** — Brackets, Orders, Division/Multiplication (equal rank, left to right), Addition/Subtraction (equal rank, left to right). Almost every wrong option in this topic is a *left-to-right* evaluation of a correctly substituted expression.\n\nSpend two calm seconds writing the substituted line; the rest is arithmetic you cannot get wrong.",
    formulas=[
        C.F('BODMAS order', 'B \\to O \\to D/M \\to A/S', 'D and M share a rank and resolve left to right; so do A and S.'),
        C.F('Substitution map', '\\{+,-,\\times,\\div\\} \\to \\{+,-,\\times,\\div\\}', 'A bijection: rewrite every operator before touching any number.'),
    ],
    tricks=[
        C.T(
            'Rewrite the whole line, then compute',
            "Under the given expression, write the substituted operators in the same positions. Only then evaluate with BODMAS. One rewritten line prevents every 'multiplied out of habit' error.",
            "**Q.** If '+' means '×', evaluate 6 + 2 × 4 − 1.\n\n**Sol.** Substituted: 6 × 2 + 4 − 1. BODMAS: 6×2 = 12; 12 + 4 = 16; 16 − 1 = **15**.",
            "Substitution on paper, evaluation under it — never simultaneously."),
    ],
    mistakes=[
        "Applying the substitution to only some operators (the last one is most often forgotten).",
        "Evaluating strictly left to right when BODMAS is expected — the examiner counts on exactly this.",
        "Reading the mapping backwards: '+' means '÷' means wherever + *appears*, write ÷.",
    ]))

subs.append(C.sub(
    'sign-substitution', 'Sign substitution',
    "The standard format: *'If + means ÷, − means ×, × means +, ÷ means −, then <expression> = ?'* All four operators are reassigned at once. Workflow: write the mapping, rewrite the expression, evaluate with BODMAS.\n\nKnow the three planted options in almost every such question:\n\n- the **correct** value (substitution + BODMAS),\n- the **original-expression** value (candidate ignored the mapping),\n- the **left-to-right** value of the substituted line (candidate skipped BODMAS).\n\nComputing the original value as a cross-check takes ten seconds and tells you which trap is laid out.",
    tricks=[
        C.T(
            'Compute the trap values too',
            "After the correct value, evaluate the original expression once. If that number sits among the options, you have confirmed the examiner's design and your own substitution in one stroke.",
            "**Q.** If '+' means '÷' and '×' means '+', evaluate 8 + 4 × 2.\n\n**Sol.** Substituted: 8 ÷ 4 + 2 = 2 + 2 = **4**. Original value: 8 + 4×2 = 16 — an 'ignored the mapping' trap.",
            "Two evaluations — substituted and original — finish and self-check the question."),
    ],
    mistakes=[
        "Changing numbers instead of operators (the mapping speaks only of signs).",
        "Losing track when the same operator appears twice — every occurrence must be replaced.",
        "Forgetting that after substitution the ÷/× may sit where +/− used to, changing the BODMAS order.",
    ]))

subs.append(C.sub(
    'interchange-signs', 'Interchanging signs and numbers',
    "Twin of substitution, but the change is a **symmetric swap**: 'interchange + and ×' (and sometimes two numbers, e.g. 2 and 8). Wherever one symbol stood, the other now stands, and vice versa. Apply every swap in a single rewrite, then BODMAS.\n\nThe **fix-the-equation** variant gives a false equation and asks which two numbers (or signs), if interchanged, make it correct. This is a *sweep*, not an insight: try the pairs in a fixed order (say, always from the left), evaluate each rewritten equation in writing, and stop at the pair that balances. With four numbers there are at most six pairs — under a minute of arithmetic, with zero guessing.",
    tricks=[
        C.T(
            'Swap table in the margin',
            "Write 'a ↔ b', 'op1 ↔ op2' at the left, rewrite the expression once with all swaps applied, evaluate.",
            "**Q.** Interchange + with × and 2 with 6 in 2 + 6 × 3.\n\n**Sol.** After swap: 6 × 2 + 3 = 12 + 3 = **15**.",
            "One rewrite covering every swap beats applying them piecemeal."),
        C.T(
            'Fixed-order sweep for fix-the-equation',
            "Sweep pairs left to right: (n1,n2), (n1,n3), (n1,n4), (n2,n3), (n2,n4), (n3,n4). One written value per row; the row matching the RHS is the answer. If no row matches, you mis-evaluated something — redo the row, not the method.",
            "**Q.** Make 8 × 4 − 6 + 3 = 35 correct by interchanging two numbers.\n\n**Sol.** Sweep: (8,4) → 4×6−8+3 = 19 ✗; (8,6) → 6×4−8+3 = 19 ✗; (8,3) → 3×4−6+8 = 14 ✗; (4,6) → 8×6−4+3 = 47 ✗; (4,3) → 8×3−6+4 = 22 ✗; (6,3) → 8×4−3+6 = **35** ✓. Swap **6 and 3**.",
            "Six written trials, always in the same order — mechanical and safe."),
    ],
    mistakes=[
        "Swapping the signs but forgetting the numbers (or the reverse) in two-part interchanges.",
        "Swapping numbers that appear more than once without checking every occurrence.",
        "Abandoning the sweep halfway — the correct pair is often the last one you would try.",
    ]))

subs.append(C.sub(
    'balance-equation', 'Balancing and operator-filling',
    "Three shapes live here:\n\n1. **Pick the correct equation** — four complete equations are offered; exactly one is arithmetically true. Evaluate all four with BODMAS, in writing, and tick the true one. This is the cheapest correct mark in the whole section (four one-line evaluations, ~40 seconds).\n2. **Fill the operator blanks** — '5 ? 2 ? 3 = 13' with sign-pair options like (×, +). Test each pair in order; the balancing pair wins.\n3. **Choose the sign set** — three blanks, options are full sign sets such as '÷, +, ×'. Same method: evaluate each set, keep the one that matches the RHS.\n\nThe examiner plants one option that would be true if evaluated left to right but fails under BODMAS (or vice versa). If your evaluation disagrees with the key, re-check the *order of operations* before re-checking the arithmetic.",
    tricks=[
        C.T(
            'Evaluate all, then eliminate',
            "In pick-the-correct-equation, evaluate every option in a written value column. Exactly one row matches its RHS; the column doubles as your final check.",
            "**Q.** Which is correct? 24 ÷ 6 − 2 × 3 = 1 / 5 × 4 + 6 ÷ 2 = 23 / 9 + 6 ÷ 2 − 3 = 11 / 7 × 2 + 8 ÷ 4 = 18.\n\n**Sol.** Values: 4−6 = −2 ✗; 20+3 = 23 ✓; 9+3−3 = 9 ✗; 14+2 = 16 ✗. Answer: the second.",
            "A four-row value column settles it; never stop at the first 'plausible' option."),
    ],
    mistakes=[
        "Scanning options for a 'nice-looking' equation instead of evaluating.",
        "Testing only the first blank of a sign pair — the second sign is where the balance usually breaks.",
        "Ignoring equal ranks: ÷ then × must be done left to right, not 'multiplication always first'.",
    ]))

patterns = [
    C.P('Full four-operator substitution', 'very common',
        "'If + means ÷, − means ×, × means +, ÷ means −, then <expr> = ?'",
        "Rewrite the whole line with new operators, evaluate with BODMAS; expect the original-value trap among the options."),
    C.P('Pick the correct equation', 'very common',
        "Four complete equations; exactly one is true.",
        "Evaluate all four in a written value column; the true one is the answer."),
    C.P('Two-sign or sign + number interchange', 'common',
        "'Interchange + and ×' (sometimes also two numbers), then evaluate.",
        "One margin rewrite applying all swaps at once, then BODMAS."),
    C.P('Fix the equation by swapping numbers', 'common',
        "A false equation; some pair of numbers makes it true — find the pair.",
        "Fixed-order sweep of all pairs with one written value per row."),
    C.P('Fill the operator blanks', 'common',
        "'5 ? 2 ? 3 = 13' with sign-pair or sign-set options.",
        "Evaluate each candidate set with BODMAS until one balances."),
    C.P('Substitution with brackets', 'occasional',
        "Substitution where the expression carries brackets.",
        "Substitute first; brackets still resolve first inside BODMAS."),
]

examples = []

# ---- ex1: four-operator substitution --------------------------------------
# expr 6 + 2 × 4 ÷ 2 − 2 ; map + -> ×, × -> +, ÷ -> −, − -> ÷
nums = [6, 2, 4, 2, 2]
ops = ['+', '×', '÷', '−']
mp = {'+': '×', '×': '+', '÷': '−', '−': '÷'}
sub_o = py_ops(apply_map(ops, mp))
orig_o = py_ops(ops)
v, v_orig, v_ltr = ev(nums, sub_o), ev(nums, orig_o), ltr(nums, sub_o)
assert (v, v_orig, v_ltr) == (15, 8, 7), (v, v_orig, v_ltr)
examples.append(C.Q(
    'rsn-mathops-ex1',
    "If **+ means ×**, **− means ÷**, **× means +** and **÷ means −**, then the value of **6 + 2 × 4 ÷ 2 − 2** is:",
    ['15', '8', '7', '11'], '15',
    "Substitute: 6 + 2 × 4 ÷ 2 − 2 → **6 × 2 + 4 − 2 ÷ 2**. BODMAS: 6×2 = 12; 2÷2 = 1; 12 + 4 − 1 = **15**. The option 8 is the original expression's value 6 + 8÷2 − 2 (mapping ignored), and 7 is the left-to-right value of the substituted line (BODMAS skipped).",
    sc="Rewrite the full line once with new operators, then BODMAS — never substitute while calculating.",
    d='medium', sub='sign-substitution', pat='full four-operator substitution', t=45))

# ---- ex2: interchange + and × ---------------------------------------------
# expr 3 × 4 + 5 − 6 ; swap + and x
nums = [3, 4, 5, 6]
ops = ['×', '+', '−']
sw = {'+': '×', '×': '+'}
sub_o = py_ops(apply_map(ops, sw))
orig_o = py_ops(ops)
v, v_orig, v_ltr = ev(nums, sub_o), ev(nums, orig_o), ltr(nums, sub_o)
assert (v, v_orig, v_ltr) == (17, 11, 29), (v, v_orig, v_ltr)
examples.append(C.Q(
    'rsn-mathops-ex2',
    "If the signs **+ and × are interchanged**, then the value of **3 × 4 + 5 − 6** is:",
    ['17', '11', '29', '23'], '17',
    "Swapping + and ×: 3 × 4 + 5 − 6 → **3 + 4 × 5 − 6**. BODMAS: 4×5 = 20; 3 + 20 − 6 = **17**. (11 is the unswapped value; 29 is what you get if you work strictly left to right: (3+4)×5−6.)",
    sc="Rewrite with the swapped signs, then multiply first — the swap changes which operator the BODMAS rank picks up.",
    d='easy', sub='interchange-signs', pat='two-sign or sign + number interchange', t=40))

# ---- ex3: fix the equation by swapping numbers ----------------------------
# expr 4 + 2 × 6 − 3 = 20 ; swap values 2 and 3 (positions 1,3)
nums = [4, 2, 6, 3]
ops = ['+', '×', '−']
o = py_ops(ops)
sw_vals = all_pair_swaps(nums, o)
hits = [pair for pair, val in sw_vals.items() if val == 20]
assert hits == [(2, 3)], (hits, sw_vals)          # unique pair (values 2 and 3)
assert ev(nums, o) != 20                           # printed equation is false as given
opts_pairs = ['2 and 3', '4 and 2', '6 and 3', '4 and 3']
assert all(p != '2 and 3' for p in opts_pairs[1:])
examples.append(C.Q(
    'rsn-mathops-ex3',
    "Which two numbers should be interchanged to make the following equation correct?\n\n**4 + 2 × 6 − 3 = 20**",
    opts_pairs, '2 and 3',
    "Sweep the pairs: (4,2) → 2 + 4×6 − 3 = 23 ✗; (4,6) → 6 + 2×4 − 3 = 11 ✗; (4,3) → 3 + 2×6 − 4 = 11 ✗; (2,6) → 4 + 6×2 − 3 = 13 ✗; (2,3) → 4 + 3×6 − 2 = 4 + 18 − 2 = **20** ✓. Interchanging **2 and 3** balances the equation (and no other pair does).",
    sc="Fixed-order sweep of all six pairs, one written value per row; only one row can match the RHS.",
    d='medium', sub='interchange-signs', pat='fix the equation by swapping numbers', t=60))

# ---- ex4: pick the correct equation ---------------------------------------
cands = [
    ([24, 6, 2, 3], ['/', '-', '*'], 1),
    ([5, 4, 6, 2], ['*', '+', '/'], 23),
    ([9, 6, 2, 3], ['+', '/', '-'], 11),
    ([7, 2, 8, 4], ['*', '+', '/'], 18),
]
truths = [ev(n, o) == t for n, o, t in cands]
assert truths == [False, True, False, False], (truths, [ev(n, o) for n, o, t in cands])
examples.append(C.Q(
    'rsn-mathops-ex4',
    "Which of the following equations is **correct**?",
    ['24 ÷ 6 − 2 × 3 = 1', '5 × 4 + 6 ÷ 2 = 23', '9 + 6 ÷ 2 − 3 = 11', '7 × 2 + 8 ÷ 4 = 18'],
    '5 × 4 + 6 ÷ 2 = 23',
    "Evaluate each with BODMAS: 24÷6−2×3 = 4−6 = −2 ✗; 5×4+6÷2 = 20+3 = **23** ✓; 9+6÷2−3 = 9+3−3 = 9 ✗ (not 11); 7×2+8÷4 = 14+2 = 16 ✗ (not 18). Only the second equation holds.",
    sc="A written value column for all four options — the true equation is the only row matching its RHS.",
    d='easy', sub='balance-equation', pat='pick the correct equation', t=40))

# ---------------------------------------------------------------- practice
pr = []

# q1: simple two-sign substitution
nums = [3, 4, 2]
o_sub = py_ops(['×', '−'])           # + -> ×, × -> -
o_orig = py_ops(['+', '×'])
v, v_orig, v_ltrorig = ev(nums, o_sub), ev(nums, o_orig), ltr(nums, o_orig)
assert (v, v_orig, v_ltrorig) == (10, 11, 14), (v, v_orig, v_ltrorig)
pr.append(C.Q(
    'rsn-mathops-1',
    "If **+ means ×** and **× means −**, then the value of **3 + 4 × 2** is:",
    ['10', '11', '14', '19'], '10',
    "Substituted: 3 × 4 − 2 = 12 − 2 = **10**. (11 is the original expression's value 3 + 4×2; 14 comes from (3+4)×2 — reading the original left to right.)",
    sc="Two operators swapped: rewrite, then multiply before subtracting.",
    d='easy', sub='sign-substitution', pat='full four-operator substitution', t=35))

# q2: four-operator substitution, different map
# expr 16 ÷ 4 + 3 × 6 − 2 ; map ÷->+, +->-, ×->÷, -->×
nums = [16, 4, 3, 6, 2]
ops = ['÷', '+', '×', '−']
mp = {'÷': '+', '+': '−', '×': '÷', '−': '×'}
o_sub, o_orig = py_ops(apply_map(ops, mp)), py_ops(ops)
v, v_orig = ev(nums, o_sub), ev(nums, o_orig)
assert v == 19 and v_orig == 20, (v, v_orig)   # 16+4 - 3÷6×2 = 20-1 ; orig 4+18-2
pr.append(C.Q(
    'rsn-mathops-2',
    "If **÷ means +**, **+ means −**, **× means ÷** and **− means ×**, then the value of **16 ÷ 4 + 3 × 6 − 2** is:",
    ['19', '20', '18', '21'], '19',
    "Substituted: 16 ÷ 4 + 3 × 6 − 2 → **16 + 4 − 3 ÷ 6 × 2**. BODMAS: 3÷6×2 = 1 (left to right); 16 + 4 − 1 = **19**. The value 20 belongs to the un-substituted expression (4 + 18 − 2) — the mapping-ignored trap.",
    sc="Rewrite all four operators first; handle the ÷/× run (3 ÷ 6 × 2) left to right.",
    d='medium', sub='sign-substitution', pat='full four-operator substitution', t=50))

# q3: sign + number interchange
# expr 2 + 8 × 3 − 5 ; swap + with ×, and 2 with 8
nums = [2, 8, 3, 5]
ops = ['+', '×', '−']
o_sub = py_ops(apply_map(ops, {'+': '×', '×': '+'}))
o_orig = py_ops(ops)
v, v_orig = ev([8, 2, 3, 5], o_sub), ev(nums, o_orig)
assert (v, v_orig) == (14, 21), (v, v_orig)    # 8×2+3−5 = 14 ; 2+24−5 = 21
pr.append(C.Q(
    'rsn-mathops-3',
    "If the signs **+ and ×** and the numbers **2 and 8** are interchanged, then the value of **2 + 8 × 3 − 5** is:",
    ['14', '21', '19', '8'], '14',
    "Apply both swaps in one rewrite: 2 + 8 × 3 − 5 → **8 × 2 + 3 − 5** = 16 + 3 − 5 = **14**. (21 is the value with no interchange at all: 2 + 24 − 5.)",
    sc="One rewrite carrying both swaps; then multiply before adding.",
    d='medium', sub='interchange-signs', pat='two-sign or sign + number interchange', t=45))

# q4: fill operator blanks
nums = [12, 4, 2]
cand = [('+', '-'), ('/', '*'), ('*', '/'), ('-', '/')]
vals = [ev(nums, [a, b]) for a, b in cand]
assert vals == [14, 6, 24, 10], vals           # only 12÷4×2 = 6
pr.append(C.Q(
    'rsn-mathops-4',
    "Which set of signs will make **12 ? 4 ? 2 = 6** correct?",
    ['+ and −', '÷ and ×', '× and ÷', '− and ÷'], '÷ and ×',
    "Test each pair: 12 + 4 − 2 = 14 ✗; 12 ÷ 4 × 2 = 3 × 2 = **6** ✓; 12 × 4 ÷ 2 = 24 ✗; 12 − 4 ÷ 2 = 10 ✗. **÷ and ×** balance the equation.",
    sc="The ÷/× pair works rank-to-rank left to right: 12 ÷ 4 × 2 — divide first, then multiply.",
    d='easy', sub='balance-equation', pat='fill the operator blanks', t=35))

# q5: fill blanks 2
nums = [5, 2, 3]
cand = [('+', '*'), ('*', '+'), ('-', '*'), ('*', '-')]
vals = [ev(nums, [a, b]) for a, b in cand]
assert vals == [11, 13, -1, 7], vals
pr.append(C.Q(
    'rsn-mathops-5',
    "Which pair of signs will make **5 ? 2 ? 3 = 13** correct?",
    ['+ and ×', '× and +', '− and ×', '× and −'], '× and +',
    "5 + 2 × 3 = 5 + 6 = 11 ✗; 5 × 2 + 3 = 10 + 3 = **13** ✓; 5 − 2 × 3 = 5 − 6 = −1 ✗; 5 × 2 − 3 = 7 ✗. Answer: **× and +**.",
    sc="Under BODMAS the second sign's rank decides: × then + multiplies first (2×3? no — 5×2 first).",
    d='easy', sub='balance-equation', pat='fill the operator blanks', t=35))

# q6: pick the correct equation
cands = [
    ([15, 3, 2, 4], ['/', '+', '*'], 13),
    ([20, 4, 2, 6], ['-', '/', '+'], 16),
    ([7, 2, 8, 4], ['*', '+', '/'], 18),
    ([36, 6, 2, 1], ['/', '*', '+'], 14),
]
truths = [ev(n, o) == t for n, o, t in cands]
assert truths == [True, False, False, False], (truths, [ev(n, o) for n, o, t in cands])
pr.append(C.Q(
    'rsn-mathops-6',
    "Which of the following equations is **arithmetically correct**?",
    ['15 ÷ 3 + 2 × 4 = 13', '20 − 4 ÷ 2 + 6 = 16', '7 × 2 + 8 ÷ 4 = 18', '36 ÷ 6 × 2 + 1 = 14'],
    '15 ÷ 3 + 2 × 4 = 13',
    "Values: 15÷3+2×4 = 5+8 = **13** ✓; 20−4÷2+6 = 20−2+6 = 24 ✗; 7×2+8÷4 = 14+2 = 16 ✗; 36÷6×2+1 = 12+1 = 13 ✗ (not 14). Only the first equation is true.",
    sc="Four one-line evaluations; note 36 ÷ 6 × 2 must go left to right (12), not ×-first (3).",
    d='easy', sub='balance-equation', pat='pick the correct equation', t=40))

# q7: substitution with brackets
# (24 + 8) − 2 ÷ 4 ; map +->÷, -->×, ÷->+
inner = ev([24, 8], ['/'])
v = ev([inner, 2, 4], ['*', '+'])
v_orig = ev([ev([24, 8], ['+']), 2, 4], ['*', '/'])
assert (inner, v, v_orig) == (3, 10, 16), (inner, v, v_orig)
pr.append(C.Q(
    'rsn-mathops-7',
    "If **+ means ÷**, **− means ×** and **÷ means +**, then the value of **(24 + 8) − 2 ÷ 4** is:",
    ['10', '16', '18', '14'], '10',
    "Substitute (brackets still first): (24 + 8) − 2 ÷ 4 → (24 ÷ 8) × 2 + 4 = 3 × 2 + 4 = **10**. The un-substituted value is (32 × 2) ÷ 4 = 16 — the mapping-ignored trap.",
    sc="Resolve the bracket with its NEW operator, then sweep the rest by BODMAS.",
    d='medium', sub='sign-substitution', pat='substitution with brackets', t=50))

# q8: which equation becomes correct if + and - are interchanged
def swapped_eq(nums, ops):
    return ev(nums, [{'+': '-', '-': '+'}.get(o, o) for o in ops])

tests = [
    ([10, 4, 2, 3], ['-', '+', '*'], 8),
    ([12, 3, 6, 2], ['+', '-', '/'], 11),
    ([9, 6, 3, 4], ['+', '-', '*'], 5),
    ([15, 5, 4, 2], ['-', '+', '*'], 13),
]
res = [(ev(n, o), swapped_eq(n, o), t) for n, o, t in tests]
assert res[0][1] == 8 and all(r[1] != t for r, (_, _, t) in zip(res[1:], tests[1:])), res
# original printed values must NOT equal target (else true without swap)
assert res[0][0] != 8 and all(r[0] != t for r, (_, _, t) in zip(res[1:], tests[1:])), res
pr.append(C.Q(
    'rsn-mathops-8',
    "If the signs **+ and − are interchanged**, in which of the following equations does the equation become **correct**?",
    ['10 − 4 + 2 × 3 = 8', '12 + 3 − 6 ÷ 2 = 11', '9 + 6 − 3 × 4 = 5', '15 − 5 + 4 × 2 = 13'],
    '10 − 4 + 2 × 3 = 8',
    "Swap + and − in each option, then evaluate: 10 + 4 − 2×3 = 14 − 6 = **8** ✓. The others give 12 − 3 + 3 = 12 ✗; 9 − 6 + 12 = 15 ✗; 15 + 5 − 8 = 12 ✗.",
    sc="Interchange first, evaluate second — the RHS is untouched by a sign swap.",
    d='medium', sub='interchange-signs', pat='two-sign or sign + number interchange', t=50))

# q9: plus/minus substitution only
nums = [15, 7, 4, 2]
o_sub = py_ops(['+', '−', '−'])      # − -> +, + -> -
o_orig = py_ops(['−', '+', '+'])
v, v_orig = ev(nums, o_sub), ev(nums, o_orig)
assert (v, v_orig) == (16, 14), (v, v_orig)
pr.append(C.Q(
    'rsn-mathops-9',
    "If **− means +** and **+ means −**, then the value of **15 − 7 + 4 + 2** is:",
    ['16', '14', '10', '26'], '16',
    "Substituted: 15 − 7 + 4 + 2 → **15 + 7 − 4 − 2** = 22 − 6 = **16**. (14 is the original line's value 15 − 7 + 4 + 2.)",
    sc="Only +/− swap: pure left-to-right addition-subtraction after the rewrite.",
    d='easy', sub='sign-substitution', pat='full four-operator substitution', t=35))

# q10: fix equation 2
nums = [8, 4, 6, 3]
ops = ['×', '−', '+']
o = py_ops(ops)
sw = all_pair_swaps(nums, o)
hits = [p for p, val in sw.items() if val == 35]
assert hits == [(6, 3)], (hits, sw)
assert ev(nums, o) == 29 != 35
pr.append(C.Q(
    'rsn-mathops-10',
    "Which two numbers should be interchanged to make the following equation correct?\n\n**8 × 4 − 6 + 3 = 35**",
    ['8 and 4', '4 and 6', '6 and 3', '8 and 3'], '6 and 3',
    "Sweep: (8,4) → 4×6−8+3 = 19 ✗; (4,6) → 8×6−4+3 = 47 ✗; (6,3) → 8×4−3+6 = 32 − 3 + 6 = **35** ✓. Interchanging **6 and 3** works (the remaining pairs give 14 and 22).",
    sc="Try the pair touching the last operator early — (6,3) — then confirm no earlier pair matched.",
    d='medium', sub='interchange-signs', pat='fix the equation by swapping numbers', t=60))

# q11: hard four-operator substitution
# expr 18 ÷ 6 − 3 × 2 + 4 ; map ÷->+, -->÷, ×->-, +->×
nums = [18, 6, 3, 2, 4]
ops = ['÷', '−', '×', '+']
mp = {'÷': '+', '−': '÷', '×': '−', '+': '×'}
o_sub, o_orig = py_ops(apply_map(ops, mp)), py_ops(ops)
v, v_orig, v_ltr = ev(nums, o_sub), ev(nums, o_orig), ltr(nums, o_sub)
assert (v, v_orig, v_ltr) == (12, 1, 24), (v, v_orig, v_ltr)
pr.append(C.Q(
    'rsn-mathops-11',
    "If **÷ means +**, **− means ÷**, **× means −** and **+ means ×**, then the value of **18 ÷ 6 − 3 × 2 + 4** is:",
    ['12', '24', '1', '10'], '12',
    "Substituted: 18 ÷ 6 − 3 × 2 + 4 → **18 + 6 ÷ 3 − 2 × 4**. BODMAS: 6÷3 = 2 and 2×4 = 8; 18 + 2 − 8 = **12**. (24 is the left-to-right value; 1 is the original expression's value 3 − 6 + 4.)",
    sc="Rewrite, then clear both ÷/× blocks before touching +/−.",
    d='hard', sub='sign-substitution', pat='full four-operator substitution', t=60))

# q12: interchange × and ÷
nums = [36, 4, 3, 5]
ops = ['÷', '×', '−']
swp = {'×': '÷', '÷': '×'}
o_sub = py_ops(apply_map(ops, swp))
o_orig = py_ops(ops)
v, v_orig = ev(nums, o_sub), ev(nums, o_orig)
assert (v, v_orig) == (43, 22), (v, v_orig)   # 36×4÷3−5 = 48−5 ; orig 9×3−5
pr.append(C.Q(
    'rsn-mathops-12',
    "If the signs **× and ÷ are interchanged**, then the value of **36 ÷ 4 × 3 − 5** is:",
    ['43', '22', '38', '25'], '43',
    "After the swap: 36 ÷ 4 × 3 − 5 → **36 × 4 ÷ 3 − 5** = 144 ÷ 3 − 5 = 48 − 5 = **43**. (22 is the unswapped value 9 × 3 − 5.)",
    sc="×/÷ swaps keep the same BODMAS rank — just read the rewritten line left to right within the rank.",
    d='easy', sub='sign-substitution', pat='two-sign or sign + number interchange', t=40))

# q13: choose the sign set
nums = [24, 8, 4, 2]
cand = [('÷', '−', '×'), ('÷', '+', '×'), ('÷', '×', '+'), ('+', '÷', '×')]
vals = [ev(nums, py_ops(list(c))) for c in cand]
assert vals == [-5, 11, 14, 28], vals
pr.append(C.Q(
    'rsn-mathops-13',
    "Which set of signs will make **24 ? 8 ? 4 ? 2 = 11** correct?",
    ['÷, −, ×', '÷, +, ×', '÷, ×, +', '+, ÷, ×'], '÷, +, ×',
    "24 ÷ 8 − 4 × 2 = 3 − 8 = −5 ✗; 24 ÷ 8 + 4 × 2 = 3 + 8 = **11** ✓; 24 ÷ 8 × 4 + 2 = 12 + 2 = 14 ✗; 24 + 8 ÷ 4 × 2 = 24 + 4 = 28 ✗. The set **÷, +, ×** balances.",
    sc="Clear the ÷/× rank first in every candidate: 24÷8 = 3 and 4×2 = 8, then combine.",
    d='medium', sub='balance-equation', pat='fill the operator blanks', t=50))

# q14: substitution with brackets, positive answer
# (24 + 8) − 2 ÷ 4 variant already used; do (16 + 8) × 2 − 6 with map +->×, ×->−
nums_full = ([16, 8], '+'), (None,)
inner = ev([16, 8], ['*'])
v = ev([inner, 2, 6], ['-', '-'])
v_orig = ev([ev([16, 8], ['+']), 2, 6], ['*', '-'])
assert (inner, v, v_orig) == (128, 120, 42), (inner, v, v_orig)
pr.append(C.Q(
    'rsn-mathops-14',
    "If **+ means ×** and **× means −**, then the value of **(16 + 8) × 2 − 6** is:",
    ['120', '42', '112', '126'], '120',
    "Substituted: (16 + 8) × 2 − 6 → (16 × 8) − 2 − 6 = 128 − 2 − 6 = **120**. (42 is the un-substituted value (16 + 8) × 2 − 6 = 48 − 6.)",
    sc="Bracket first with the NEW operator, then a plain left-to-right −/− sweep.",
    d='medium', sub='sign-substitution', pat='substitution with brackets', t=50))

# q15: A+B notation substitution
# 20 + 5 − 2 with + meaning ÷ and − meaning ×
v = ev([20, 5, 2], ['/', '*'])
v_orig = ev([20, 5, 2], ['+', '*'])
v_ltrorig = ltr([20, 5, 2], ['+', '*'])
assert (v, v_orig, v_ltrorig) == (8, 30, 50), (v, v_orig, v_ltrorig)
pr.append(C.Q(
    'rsn-mathops-15',
    "If **'+' means '÷'** and **'−' means '×'**, then the value of **20 + 5 − 2** is:",
    ['8', '30', '50', '6'], '8',
    "Substituted: 20 + 5 − 2 → 20 ÷ 5 × 2. Same BODMAS rank, so left to right: 4 × 2 = **8**. (30 is the original value 20 + 10; 50 is (20 + 5) × 2.)",
    sc="After substitution, ÷ and × are equal-rank: 20 ÷ 5 × 2 must go strictly left to right.",
    d='easy', sub='sign-substitution', pat='full four-operator substitution', t=35))

assert len(pr) == 15

t = C.topic(
    'mathematical-operations', 'Mathematical Operations', 'medium', {'tier1': '1-2', 'tier2': '2'},
    "Operator-substitution puzzles: signs are redefined or interchanged, equations must be balanced, and the correct equation picked from four. The arithmetic is primary-school level — marks are lost to BODMAS slips and half-applied substitutions, not to difficulty. A disciplined rewrite-then-evaluate habit makes this one of the safest scoring topics in the paper.",
    subs, patterns, examples, pr)

C.write_topic(t)
print('OK mathematical-operations')
