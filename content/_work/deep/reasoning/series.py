"""Phase-2 deep content for reasoning/series. Idempotent: run with `py -3 series.py`."""
import itertools
import os
import random
import sys
from fractions import Fraction as F

sys.path.insert(0, os.path.dirname(__file__))
from _lib import *  # noqa
from series_content import NOTES, PATTERNS

T = "series"
d = load(T)

# ---------------- helpers ----------------

def fmt(x):
    if isinstance(x, F):
        if x.denominator == 1:
            return str(x.numerator)
        den = x.denominator
        while den % 2 == 0:
            den //= 2
        while den % 5 == 0:
            den //= 5
        if den == 1:
            return ("%.6f" % float(x)).rstrip("0").rstrip(".")
        return r"$\frac{%d}{%d}$" % (x.numerator, x.denominator)
    return str(x)


def show(terms, hide=()):
    return ", ".join("?" if i in hide else fmt(t) for i, t in enumerate(terms))


def gen_add(a, ds):
    out = [a]
    for x in ds:
        out.append(out[-1] + x)
    return out


def gen_rec(a, n, f):
    out = [a]
    for i in range(n - 1):
        out.append(f(out[-1], i))
    return out


def inter(x, y):
    out = []
    for i in range(max(len(x), len(y))):
        if i < len(x):
            out.append(x[i])
        if i < len(y):
            out.append(y[i])
    return out


def dl(terms):
    return ", ".join(fmt(b - a) for a, b in zip(terms, terms[1:]))


PN = "Select the number that can replace the question mark (?) in the following series."
PL = "Select the letter that can replace the question mark (?) in the following series."
PC = "Select the letter-cluster that can replace the question mark (?) in the following series."
PA = "Select the term that can replace the question mark (?) in the following series."
P2 = "Select the pair of numbers that can replace the two question marks (?) in the following series, in order."
PW = "In the following series, one number is **wrong**. Find the wrong number."
PWL = "In the following series, one term is **wrong**. Find the wrong term."
PB = ("Select the combination of letters that when sequentially placed in the blanks of the given series "
      "will complete the series.")

Qs = []


def nq(id, terms, k, wrong, sol, short, diff, sub, pat, t=45, prompt=PN, rule=None):
    """terms = full generated series; k = index asked. If k is the last index, series shown up to '?'."""
    if rule is not None:
        assert list(rule) == list(terms), f"{id}: terms do not match rule"
    shown = terms if k < len(terms) - 1 else terms
    q = f"{prompt}\n\n**{show(shown, {k})}**"
    Qs.append(Q(id, q, fmt(terms[k]), [fmt(w) if not isinstance(w, str) else w for w in wrong],
                sol, short, diff, sub, pat, t, check=fmt(terms[k])))


def lq(id, terms, k, wrong, sol, short, diff, sub, pat, t=40, prompt=PL):
    q = f"{prompt}\n\n**{show(terms, {k})}**"
    Qs.append(Q(id, q, terms[k], wrong, sol, short, diff, sub, pat, t, check=terms[k]))


def wq(id, true_terms, idx, bad, others, sol, short, diff, sub, pat, t=50, prompt=PW):
    shown = list(true_terms)
    shown[idx] = bad
    dev = [i for i in range(len(shown)) if shown[i] != true_terms[i]]
    assert dev == [idx], f"{id}: deviation {dev}"
    assert idx not in others and len(others) == 3
    for i in others:
        assert shown[i] == true_terms[i]
    opts = [fmt(shown[i]) for i in others]
    assert fmt(bad) not in opts
    q = f"{prompt}\n\n**{show(shown)}**"
    Qs.append(Q(id, q, fmt(bad), opts, sol, short, diff, sub, pat, t, check=fmt(shown[idx])))


def periodic(s, p):
    return all(s[i] == s[i % p] for i in range(len(s)))


def blank_parts(full, blanks):
    disp = " ".join("_" if i in blanks else c for i, c in enumerate(full))
    ans = "".join(full[i] for i in blanks)
    return disp, ans


def fill(full, blanks, cand):
    s = list(full)
    for i, c in zip(sorted(blanks), cand):
        s[i] = c
    return "".join(s)


def blank_check(id, full, blanks, period=None):
    blanks = sorted(blanks)
    disp, ans = blank_parts(full, blanks)
    assert fill(full, blanks, ans) == full
    if period:
        assert periodic(full, period), f"{id}: not periodic {period}"
        # every blank must be decidable from a visible letter in its column
        for b in blanks:
            col = [i for i in range(len(full)) if i % period == b % period and i not in blanks]
            assert col, f"{id}: blank {b} has no visible letter in its column"
    return disp, ans


def good_distractor(full, blanks, cand):
    s = fill(full, blanks, cand)
    if s == full:
        return False
    return not any(periodic(s, p) for p in range(1, len(s) // 2 + 1))


def auto_distractors(id, full, blanks, preferred=()):
    blanks = sorted(blanks)
    ans = "".join(full[i] for i in blanks)
    letters = sorted(set(full))
    pool = []
    for w in preferred:
        pool.append(w)
    perms = sorted(set("".join(p) for p in itertools.permutations(ans)))
    rnd = random.Random(id)
    rnd.shuffle(perms)
    pool += perms
    for i in range(len(ans)):
        for c in letters:
            pool.append(ans[:i] + c + ans[i + 1:])
    out = []
    for w in pool:
        if len(w) == len(ans) and w != ans and w not in out and good_distractor(full, blanks, w):
            out.append(w)
        if len(out) == 3:
            break
    assert len(out) == 3, id
    return out


def bq(id, full, blanks, sol, short, diff, pat, period=None, t=45, preferred=()):
    blanks = sorted(blanks)
    disp, ans = blank_check(id, full, blanks, period)
    wrong = auto_distractors(id, full, blanks, preferred)
    for w in wrong:
        assert good_distractor(full, blanks, w), (id, w)
    q = f"{PB}\n\n**{disp}**"
    Qs.append(Q(id, q, ans, wrong, sol, short, diff, "letter-blank-series", pat, t, check=ans))


def L(n):
    return let(n)


def lp(c):
    return f"{c}({pos(c)})"


# ---------------- blank-series pattern examples (computed) ----------------
def blank_example(full, blanks, period, how):
    disp, ans = blank_check("ex", full, blanks, period)
    return (f"**{disp}**", f"{how} Blanks in order: **{ans}**.")


BEX = {
    "fixed": blank_example("abcabcabcabc", [2, 6, 10], 3,
                           "Block **abc** repeats (12 places = 4 blocks of 3). Filling column-wise gives abc | abc | abc | abc."),
    "growing": blank_example("aababcabcd", [1, 4, 7, 9], None,
                             "Parts of length 1, 2, 3, 4: a | ab | abc | abcd."),
    "mirror": blank_example("pqrrqppqrrqp", [1, 3, 7, 10], 6,
                            "Block **pqrrqp** (pqr, then rqp) repeats twice: pqrrqp | pqrrqp."),
    "rotating": blank_example("abcbcacab", [1, 5, 6], None,
                              "Each block moves its first letter to the end: abc | bca | cab."),
}

# ---------------- subtopic notes + patterns ----------------
PATS = PATTERNS(P, BEX)

NEW_SUB = {
    "id": "letter-blank-series",
    "title": "Repeating letter series — fill the blanks",
    "concept": "A line of small letters has some blanks (a _ c a b _ a b c _ b c). You choose the option whose letters, "
               "placed in the blanks from left to right, make the whole line follow one repeating pattern. "
               "The pattern is a fixed block, a growing block, a mirror block or a rotating block.",
    "formulas": [],
    "tricks": [
        {
            "title": "Write the blocks one below another",
            "body": "Guess the block size from the total number of places (12 → try 3, 4 or 6). Write the blocks in rows; "
                    "each column must hold one letter, so every blank copies the visible letter in its column.",
            "example": {
                "q": "**Q.** a _ c a b _ a b c _ b c",
                "solution": "Block of 3: a_c / ab_ / abc / _bc. Columns are a, b, c → blanks **b, c, a** → answer **bca**.",
            },
        },
        {
            "title": "Double letter = mirror turn",
            "body": "When you see 'rr' or 'cc' inside the line, the block probably reads forward and then backward "
                    "(pqr rqp). Fill the second half as the first half reversed.",
            "example": {
                "q": "**Q.** p _ r r _ p p q _ r q _",
                "solution": "Block pqrrqp twice → blanks **q, q, r, p** → answer **qqrp**.",
            },
        },
    ],
    "mistakes": [
        "Choosing the block size by eye instead of counting total places — the wrong size makes two options look right.",
        "Reading the answer letters in column order instead of left-to-right blank order.",
        "Not re-reading the filled line once; a single swapped letter breaks the repeat.",
    ],
}
add_sub(d, NEW_SUB, after="wrong-number")

for sid in ["series-idea", "number-series", "letter-series", "alphanumeric-series", "wrong-number",
            "letter-blank-series"]:
    set_sub(d, sid, notes=NOTES[sid], patterns=PATS[sid])

# sanity-check pattern examples that are numeric
assert gen_add(6, [5, 10, 15, 20, 25])[-1] == 81
assert gen_rec(7, 5, lambda x, i: 2 * x + 1) == [7, 15, 31, 63, 127]
assert gen_rec(2, 5, lambda x, i: 3 * x - 1)[-1] == 122
assert [n * n - 1 for n in range(1, 7)][-1] == 35
assert gen_add(3, [1, 3, 6, 10, 15])[-1] == 38
assert gen_rec(1, 6, lambda x, i: x * (i + 1) + (i + 1))[-1] == 445
assert gen_add(5, [1, 4, 9, 16, 25])[-1] == 60
assert let(16 + 4) == "T" and let(15 + 6) == "U" and let(17) == "Q"

# ---------------- practice: series-idea ----------------
S = "series-idea"
t = gen_add(7, [5] * 5)
nq("series-idea-p01", t, 5, [33, 31, 37], f"Differences: {dl(t[:-1])} → constant **+5**. 27 + 5 = **32**.",
   "Slow, even growth = add a constant.", "easy", S, "se-p1", 25)
t = gen_rec(3, 6, lambda x, i: 2 * x)
nq("series-idea-p02", t, 5, [72, 60, 92], "Each term is double the previous one (**×2**). 48 × 2 = **96**.",
   "Terms doubling → ratio test first.", "easy", S, "se-p1", 25)
t = gen_add(1, [1, 4, 9, 16, 25])
nq("series-idea-p03", t, 5, [47, 55, 63],
   f"Differences: {dl(t[:-1])} = 1², 2², 3², 4² → next 5² = 25. 31 + 25 = **56**.",
   "When the difference row is 1, 4, 9, 16, add the next square.", "medium", S, "se-p1", 45)
t = [n * n for n in range(2, 8)]
nq("series-idea-p04", t, 2, [15, 18, 20], "Terms are 2², 3², ?, 5², 6², 7² → ? = 4² = **16**.",
   "Recognise squares at sight: 4, 9, _, 25, 36, 49.", "easy", S, "se-p2", 25)
t = gen_rec(5, 6, lambda x, i: 2 * x - 2)
nq("series-idea-p05", t, 3, [24, 28, 30],
   "Rule from the visible terms: 5×2 − 2 = 8, 8×2 − 2 = 14 → **×2 − 2**. ? = 14×2 − 2 = **26**. "
   "Check the right side: 26×2 − 2 = 50 ✓ and 50×2 − 2 = 98 ✓.",
   "A middle answer must fit both neighbours — check the term after the gap.", "medium", S, "se-p2", 45)
t = gen_add(2, [1, 4, 9, 16, 25])
nq("series-idea-p06", t, 4, [30, 31, 35],
   "Differences on the left: 1, 4, 9 (squares) → the next gaps are 16 and 25. ? = 16 + 16 = **32**. "
   "Check: 32 + 25 = 57 ✓.",
   "Gap after ? must be the next square: 57 − 32 = 25 ✓.", "hard", S, "se-p2", 55)
t = gen_rec(F(240), 6, lambda x, i: x / 2)
nq("series-idea-p07", t, 5, [7, 5, 10], "Each term is **÷2**. 15 ÷ 2 = **7.5**.",
   "Halving series: don't round off, decimals are allowed.", "easy", S, "se-p3", 25)
t = gen_rec(F(1, 2), 5, lambda x, i: x * 3)
nq("series-idea-p08", t, 4, [27, 40, "41.5"], "Each term is **×3**: 0.5 → 1.5 → 4.5 → 13.5 → 13.5 × 3 = **40.5**.",
   "Ignore the decimal point while spotting the rule: 5, 15, 45, 135 → ×3.", "medium", S, "se-p3", 40)
t = [F(2 * n + 1, 2 * n + 3) for n in range(5)]
nq("series-idea-p09", t, 4, [r"$\frac{9}{10}$", r"$\frac{11}{13}$", r"$\frac{8}{11}$"],
   "Numerators: 1, 3, 5, 7 → next 9. Denominators: 3, 5, 7, 9 → next 11. Answer **9/11**.",
   "Fractions = two series: top row and bottom row.", "medium", S, "se-p3", 40)

def pair_q(id, terms, ks, wrong, sol, short, diff, pat, t=45):
    q = f"{P2}\n\n**{show(terms, set(ks))}**"
    ans = ", ".join(fmt(terms[k]) for k in ks)
    Qs.append(Q(id, q, ans, wrong, sol, short, diff, S, pat, t, check=ans))

t = gen_add(3, [4] * 5)
pair_q("series-idea-p10", t, [1, 4], ["7, 18", "6, 19", "8, 20"],
       "The visible terms 3, 11, 15, 23 need a step of **+4** (11 → 15). First ? = 3 + 4 = 7; second ? = 15 + 4 = 19. Answer **7, 19**.",
       "Find the step from two neighbours that are both visible (11, 15).", "easy", "se-p4", 30)
t = gen_rec(2, 6, lambda x, i: 3 * x)
pair_q("series-idea-p11", t, [2, 4], ["18, 108", "24, 162", "18, 160"],
       "2 → 6 is ×3, and 486 = 162 × 3. So the rule is **×3**: 6 × 3 = 18, 54 × 3 = 162. Answer **18, 162**.",
       "Both numbers must fit ×3 — an option with one wrong number is out.", "medium", "se-p4", 40)
t = [n * n + 1 for n in range(1, 8)]
pair_q("series-idea-p12", t, [3, 5], ["17, 36", "16, 37", "18, 38"],
       "Terms are n² + 1: 1²+1 = 2, 2²+1 = 5, 3²+1 = 10, **4²+1 = 17**, 5²+1 = 26, **6²+1 = 37**, 7²+1 = 50. Answer **17, 37**.",
       "Each visible term is one more than a square.", "medium", "se-p4", 45)

# ---------------- practice: number-series ----------------
S = "number-series"
t = gen_add(11, [2, 4, 6, 8, 10])
nq("number-series-p01", t, 5, [39, 43, 40], f"Differences: {dl(t[:-1])} → next +10. 31 + 10 = **41**.",
   "Gaps rise by 2 each time.", "easy", S, "se-p5", 30)
t = gen_add(120, [-1, -3, -5, -7, -9])
nq("number-series-p02", t, 5, [97, 93, 96], "Differences: −1, −3, −5, −7 → next −9. 104 − 9 = **95**.",
   "Falling series: subtract odd numbers in order.", "medium", S, "se-p5", 35)
t = gen_rec(3, 6, lambda x, i: 2 * x + 1)
nq("number-series-p03", t, 5, [125, 126, 129], "Each term = previous × 2 + 1 (3→7→15→31→63). 63 × 2 + 1 = **127**.",
   "×2+1 series are all one less than powers of 2: 4−1, 8−1, 16−1 ... → 128 − 1.", "easy", S, "se-p6", 30)
t = gen_rec(4, 6, lambda x, i: 3 * x - 2)
nq("number-series-p04", t, 5, [732, 728, 734],
   "4×3 − 2 = 10, 10×3 − 2 = 28, 28×3 − 2 = 82, 82×3 − 2 = 244. Next: 244 × 3 − 2 = **730**.",
   "Ratio ≈ 3 with a left-over of −2 every step.", "medium", S, "se-p6", 45)
t = [n * n - 1 for n in range(2, 8)]
nq("number-series-p05", t, 5, [46, 49, 50], "Terms are n² − 1: 2²−1, 3²−1 ... 6²−1 = 35. Next: 7² − 1 = **48**.",
   "Each term is one less than a square.", "easy", S, "se-p7", 30)
t = [n ** 3 + 1 for n in range(1, 7)]
nq("number-series-p06", t, 5, [215, 216, 218], "Terms are n³ + 1: 1+1, 8+1, 27+1, 64+1, 125+1. Next: 6³ + 1 = **217**.",
   "Near-cube numbers: 9, 28, 65, 126 sit just above 8, 27, 64, 125.", "medium", S, "se-p7", 40)
t = [n * (n + 1) for n in range(2, 8)]
nq("number-series-p07", t, 5, [54, 58, 49], "Terms are n(n+1): 2×3, 3×4, 4×5, 5×6, 6×7. Next: 7 × 8 = **56**.",
   "Product of two consecutive numbers — differences are 6, 8, 10, 12, 14.", "easy", S, "se-p7", 30)
t = gen_add(2, [3, 6, 10, 15, 21])
nq("number-series-p08", t, 5, [56, 51, 58],
   "First differences: 3, 6, 10, 15. Second differences: 3, 4, 5 → next 6. Next first difference = 15 + 6 = 21. 36 + 21 = **57**.",
   "Two ladder rows: the second row is 3, 4, 5, 6.", "medium", S, "se-p8", 50)
t = gen_add(4, [2, 5, 10, 17, 26])
nq("number-series-p09", t, 5, [62, 55, 59],
   "First differences: 2, 5, 10, 17. Second differences: 3, 5, 7 → next 9. Next first difference = 17 + 9 = 26. 38 + 26 = **64**.",
   "First differences are n² + 1 (2, 5, 10, 17, 26).", "hard", S, "se-p8", 60)
t = inter([3, 6, 12, 24], [50, 45, 40, 35])
nq("number-series-p10", t, 7, [48, 30, 36],
   "Odd places: 3, 6, 12, 24 (×2). Even places: 50, 45, 40 (−5). The 8th term is an even place: 40 − 5 = **35**.",
   "Up-down series → split odd and even places.", "medium", S, "se-p9", 45)
t = inter([1, 2, 4, 8], [3, 6, 12, 24])
nq("number-series-p11", t, 7, [16, 20, 36],
   "Odd places: 1, 2, 4, 8 (×2). Even places: 3, 6, 12 (×2) → next 24. The 8th term is an even place → **24**.",
   "Two doubling series written alternately.", "medium", S, "se-p9", 45)
t = gen_rec(2, 6, lambda x, i: x * (i + 1) + (i + 1))
nq("number-series-p12", t, 5, [560, 570, 452],
   "2×1+1 = 3, 3×2+2 = 8, 8×3+3 = 27, 27×4+4 = 112. Next: 112×5 + 5 = **565**.",
   "Fast, uneven growth → try ×1+1, ×2+2, ×3+3 ...", "hard", S, "se-p10", 60)
t = gen_rec(5, 7, lambda x, i: x + 1 if i % 2 == 0 else 2 * x)
nq("number-series-p13", t, 6, [28, 52, 55], "Operations take turns: +1, ×2, +1, ×2, +1, then ×2. 27 × 2 = **54**.",
   "Look at pairs: 5→6 (+1), 6→12 (×2) and repeat.", "medium", S, "se-p10", 40)
t = gen_add(10, [2, -3, 4, -5, 6])
nq("number-series-p14", t, 5, [3, 12, 15], "Changes: +2, −3, +4, −5 → next +6. 8 + 6 = **14**.",
   "Sizes rise by 1 and signs alternate.", "medium", S, "se-p10", 40)
t = [2, 3]
for _ in range(5):
    t.append(t[-1] + t[-2])
nq("number-series-p15", t, 6, [29, 33, 35], "Each term = sum of the previous two: 8 + 13 = 21, so next = 13 + 21 = **34**.",
   "Fibonacci: 2, 3, 5, 8, 13, 21, 34.", "easy", S, "se-p11", 30)
t = [1, 2, 3]
for _ in range(4):
    t.append(t[-1] + t[-2] + t[-3])
nq("number-series-p16", t, 6, [31, 34, 36],
   "Each term = sum of the previous three: 1+2+3 = 6, 2+3+6 = 11, 3+6+11 = 20. Next: 6 + 11 + 20 = **37**.",
   "Sum of two fails (11 + 20 = 31 ≠ next pattern), so try the previous three.", "hard", S, "se-p11", 60)
t = gen_add(7, [2, 3, 5, 7, 11, 13])
nq("number-series-p17", t, 6, [46, 47, 50], "Differences: 2, 3, 5, 7, 11 — prime numbers. Next prime 13. 35 + 13 = **48**.",
   "Difference row = primes in order.", "hard", S, "se-p12", 50)
t = gen_add(10, [1, 2, 4, 8, 16])
nq("number-series-p18", t, 5, [33, 40, 49], "Differences: 1, 2, 4, 8 (powers of 2) → next 16. 25 + 16 = **41**.",
   "Differences doubling = powers of 2.", "medium", S, "se-p12", 40)

# ---------------- practice: letter-series ----------------
S = "letter-series"
t = [L(3 + 4 * i) for i in range(6)]
lq("letter-series-p01", t, 5, ["V", "X", "U"], "Positions 3, 7, 11, 15, 19 → +4. 19 + 4 = 23 = **W**.",
   "W = Y − 2 (anchor).", "easy", S, "se-p13", 25)
t = [L(26 - 3 * i) for i in range(6)]
lq("letter-series-p02", t, 5, ["L", "J", "M"], "Positions 26, 23, 20, 17, 14 → −3. 14 − 3 = 11 = **K**.",
   "Backward constant step.", "easy", S, "se-p13", 25)
t = [L(20 + 3 * i) for i in range(6)]
assert t == ["T", "W", "Z", "C", "F", "I"]
lq("letter-series-p03", t, 5, ["H", "J", "G"],
   "Positions: T(20), W(23), Z(26), then 29 − 26 = 3 = C, 6 = F → step +3 with wrap-around. F(6) + 3 = 9 = **I**.",
   "After Z, start again at A: Z + 3 = C.", "medium", S, "se-p13", 35)
t = [L(x) for x in gen_add(3, [1, 2, 3, 4, 5])]
lq("letter-series-p04", t, 5, ["Q", "S", "P"], "Steps: +1, +2, +3, +4 → next +5. M(13) + 5 = 18 = **R**.",
   "R = T − 2.", "easy", S, "se-p14", 30)
t = [L(x) for x in gen_add(2, [1, 2, 3, 4, 5, 6])]
lq("letter-series-p05", t, 6, ["V", "X", "U"], "Steps: +1, +2, +3, +4, +5 → next +6. Q(17) + 6 = 23 = **W**.",
   "Step row 1, 2, 3, 4, 5, 6.", "medium", S, "se-p14", 35)
t = [L(x) for x in gen_add(25, [-2, -3, -4, -5, -6])]
lq("letter-series-p06", t, 5, ["F", "D", "G"], "Positions 25, 23, 20, 16, 11 → steps −2, −3, −4, −5 → next −6. 11 − 6 = 5 = **E**.",
   "Falling steps grow by one each time.", "medium", S, "se-p14", 35)
t = inter([L(1 + 2 * i) for i in range(4)], [L(26 - 2 * i) for i in range(3)])
lq("letter-series-p07", t, 6, ["F", "T", "H"] if False else ["F", "T", "I"],
   "Odd places A, C, E (+2) → next G. Even places Z, X, V (−2). The 7th term is an odd place → **G**.",
   "Split the up-down series into two.", "medium", S, "se-p15", 35)
t = [L(x) for x in gen_add(2, [3, -1, 3, -1, 3, -1])]
lq("letter-series-p08", t, 6, ["K", "J", "G"], "Steps take turns: +3, −1, +3, −1, +3 → next −1. I(9) − 1 = 8 = **H**.",
   "Two-step cycle: forward 3, back 1.", "medium", S, "se-p15", 40)
t = ["".join(L(s + 5 * i + 2 * j) for j in range(3)) for i, s in enumerate([2] * 5)]
assert t == ["BDF", "GIK", "LNP", "QSU", "VXZ"]
lq("letter-series-p09", t, 4, ["UWY", "VXY", "WYA"],
   "Inside every cluster the letters go +2 (B D F). First letters B, G, L, Q → +5 → V. So the cluster is V, X, Z = **VXZ**.",
   "Solve slot 1 (+5) and keep the inside gap (+2).", "medium", S, "se-p16", 40, prompt=PC)
t = [L(1 + 2 * i) + L(26 - 2 * i) for i in range(5)]
lq("letter-series-p10", t, 4, ["IS", "HR", "JR"], "First letters A, C, E, G (+2) → I. Second letters Z, X, V, T (−2) → R. Answer **IR**.",
   "Two slots moving in opposite directions.", "medium", S, "se-p16", 35, prompt=PC)
t = [L(11 + i) + L(16 - i) + L(21 + i) for i in range(4)]
assert t == ["KPU", "LOV", "MNW", "NMX"]
lq("letter-series-p11", t, 3, ["NLX", "OMX", "NMY"],
   "Slot 1: K, L, M (+1) → N. Slot 2: P, O, N (−1) → M. Slot 3: U, V, W (+1) → X. Answer **NMX**.",
   "Three slots, three mini-series.", "hard", S, "se-p16", 45, prompt=PC)
t = [L(n * n) for n in range(1, 6)]
lq("letter-series-p12", t, 4, ["X", "Z", "U"], "Positions 1, 4, 9, 16 are squares. Next square 25 = **Y**.",
   "A, D, I, P, Y — the square letters.", "medium", S, "se-p17", 35)
t = [L(p) for p in [2, 3, 5, 7, 11, 13]]
lq("letter-series-p13", t, 5, ["L", "N", "O"], "Positions 2, 3, 5, 7, 11 are primes. Next prime 13 = **M**.",
   "Irregular steps 1, 2, 2, 4 → test primes on the positions.", "hard", S, "se-p17", 45)

# ---------------- practice: alphanumeric-series ----------------
S = "alphanumeric-series"
def aq(id, terms, k, wrong, sol, short, diff, pat, t=40):
    q = f"{PA}\n\n**{show(terms, {k})}**"
    Qs.append(Q(id, q, terms[k], wrong, sol, short, diff, S, pat, t, check=terms[k]))

t = [L(2 + 2 * i) + str(2 ** (i + 1)) for i in range(5)]
aq("alphanumeric-series-p01", t, 4, ["I32", "J30", "K32"],
   "Letters B, D, F, H (+2) → J. Numbers 2, 4, 8, 16 (×2) → 32. Answer **J32**.",
   "Two columns: letters +2, numbers ×2.", "easy", "se-p18", 30)
t = [str(3 + 4 * i) + L(26 - 3 * i) for i in range(5)]
aq("alphanumeric-series-p02", t, 4, ["19O", "18N", "21N"],
   "Numbers 3, 7, 11, 15 (+4) → 19. Letters Z, W, T, Q (−3) → N. Answer **19N**.",
   "Number first, letter second — keep the same format.", "medium", "se-p18", 35)
t = [L(x) + str((i + 1) ** 2) for i, x in enumerate(gen_add(1, [2, 3, 4, 5, 6]))]
assert t[-1] == "U36"
aq("alphanumeric-series-p03", t, 5, ["T36", "U35", "V36"],
   "Letters A, C, F, J, O → steps +2, +3, +4, +5 → next +6 → U. Numbers 1, 4, 9, 16, 25 (squares) → 36. Answer **U36**.",
   "Letter track has rising steps; number track is squares.", "hard", "se-p18", 50)
t = [L(3 * i) + str(3 * i) for i in range(1, 6)]
aq("alphanumeric-series-p04", t, 4, ["P15", "O14", "N15"],
   "Each number equals its letter's position (C=3, F=6, I=9, L=12). Next letter L + 3 = O (15) → **O15**.",
   "Number = letter position; only the letter needs working.", "easy", "se-p19", 25)
t = [L(2 * i) + str((2 * i) ** 2) for i in range(1, 6)]
aq("alphanumeric-series-p05", t, 4, ["J81", "I100", "K100"],
   "Number = (letter position)²: B(2)→4, D(4)→16, F(6)→36, H(8)→64. Next letter J(10) → 100. Answer **J100**.",
   "Test 'number = position²' on one term, then confirm on all.", "medium", "se-p19", 40)
t = [L(26 - 2 * i) + str(26 - 2 * i) for i in range(5)]
aq("alphanumeric-series-p06", t, 3, ["T21", "U20", "S19"],
   "Numbers are the letters' positions: Z26, X24, V22. Letters go −2 → T, whose position is 20. Answer **T20**.",
   "Backward letters, number = position.", "easy", "se-p19", 25)
t = [L(1 + 3 * i) + L(2 + 3 * i) + str(2 ** (i + 1)) for i in range(5)]
aq("alphanumeric-series-p07", t, 4, ["LM32", "MN24", "NO32"],
   "First letters A, D, G, J (+3) → M. Second letters B, E, H, K (+3) → N. Numbers 2, 4, 8, 16 (×2) → 32. Answer **MN32**.",
   "Three columns: slot 1, slot 2, number.", "medium", "se-p20", 40)
t = [str(2 * (i + 1)) + L(3 + 2 * i) + L(26 - 2 * i) for i in range(5)]
aq("alphanumeric-series-p08", t, 4, ["10KS", "10JR", "12KR"],
   "Numbers 2, 4, 6, 8 (+2) → 10. Middle letters C, E, G, I (+2) → K. Last letters Z, X, V, T (−2) → R. Answer **10KR**.",
   "Solve each slot; the last slot runs backwards.", "medium", "se-p20", 45)
t = [L(16 + 2 * i) + str(3 * (i + 1)) + L(17 + 2 * i) for i in range(5)]
assert t[:2] == ["P3Q", "R6S"]
aq("alphanumeric-series-p09", t, 4, ["X15Y", "X12Y", "Y15X"],
   "First letters P, R, T, V (+2) → X. Numbers 3, 6, 9, 12 (+3) → 15. Last letters Q, S, U, W (+2) → Y. Answer **X15Y**.",
   "Last letter is always the next letter after the first one.", "medium", "se-p20", 45)
t = [L(4 + 3 * i) + str(5 * (i + 1)) for i in range(5)]
aq("alphanumeric-series-p10", t, 2, ["K15", "J16", "I15"],
   "Letters D, G, _, M, P (+3) → J. Numbers 5, 10, _, 20, 25 (+5) → 15. Answer **J15**.",
   "Both tracks pass through the gap evenly.", "easy", "se-p21", 30)
t = [str(2 * 3 ** i) + L(25 - 3 * i) for i in range(5)]
aq("alphanumeric-series-p11", t, 2, ["18T", "24S", "16S"],
   "Numbers 2, 6, _, 54, 162 (×3) → 18. Letters Y, V, _, P, M (−3) → S. Answer **18S**.",
   "Check: 18 × 3 = 54 ✓ and S − 3 = P ✓.", "medium", "se-p21", 40)
t = [L(26 - 3 * i) + str((i + 1) ** 3) for i in range(5)]
aq("alphanumeric-series-p12", t, 2, ["T25", "U27", "S27"],
   "Letters Z, W, _, Q, N (−3) → T. Numbers 1, 8, _, 64, 125 (cubes) → 27. Answer **T27**.",
   "Numbers are cubes 1³ to 5³.", "hard", "se-p21", 45)

# ---------------- practice: wrong-number ----------------
S = "wrong-number"
tt = gen_add(5, [4] * 5)
wq("wrong-number-p01", tt, 4, 22, [2, 3, 5],
   "Rule +4: 5, 9, 13, 17, **21**, 25. The shown 22 breaks it (gaps 5 and 3 around it) → **22**.",
   "The wrong term sits between two bad gaps.", "easy", S, "se-p22", 30)
tt = gen_add(3, [2, 4, 6, 8, 10, 12])
wq("wrong-number-p02", tt, 5, 34, [2, 3, 6],
   "Gaps should be 2, 4, 6, 8, 10, 12: 3, 5, 9, 15, 23, **33**, 45. The shown 34 is wrong → **34**.",
   "Gaps 11 and 11 replace 10 and 12 — the term between them is wrong.", "medium", S, "se-p22", 45)
tt = gen_add(100, [-3, -6, -9, -12, -15])
wq("wrong-number-p03", tt, 5, 54, [1, 3, 4],
   "Gaps: −3, −6, −9, −12 → next −15. 70 − 15 = **55**, but 54 is shown → **54**.",
   "Falling gaps in the 3-times table.", "medium", S, "se-p22", 45)
tt = gen_rec(2, 6, lambda x, i: 3 * x)
wq("wrong-number-p04", tt, 4, 164, [1, 3, 5],
   "Rule ×3: 2, 6, 18, 54, **162**, 486. The shown 164 is wrong → **164**.",
   "486 ÷ 3 = 162, so 164 cannot be right.", "easy", S, "se-p23", 30)
tt = gen_rec(5, 6, lambda x, i: 2 * x + 1)
wq("wrong-number-p05", tt, 3, 48, [2, 4, 5],
   "Rule ×2 + 1: 5, 11, 23, **47**, 95, 191. The shown 48 is wrong → **48**.",
   "An even number in a ×2+1 series (all odd terms) is the culprit.", "medium", S, "se-p23", 45)
tt = gen_rec(4, 6, lambda x, i: 3 * x - 2)
wq("wrong-number-p06", tt, 4, 246, [2, 3, 5],
   "Rule ×3 − 2: 4, 10, 28, 82, **244**, 730. The shown 246 is wrong; note 730 = 244 × 3 − 2 → **246**.",
   "Rebuild from the start; the next term is made from the correct value.", "hard", S, "se-p23", 60)
tt = [n ** 3 for n in range(1, 7)]
wq("wrong-number-p07", tt, 4, 124, [1, 2, 3],
   "Cubes 1³ to 6³: 1, 8, 27, 64, **125**, 216. The shown 124 is wrong → **124**.",
   "124 is a near-miss of 125 = 5³.", "easy", S, "se-p24", 25)
tt = [n * (n + 1) for n in range(1, 7)]
wq("wrong-number-p08", tt, 4, 31, [1, 3, 5],
   "Terms are n(n+1): 2, 6, 12, 20, **30**, 42. The shown 31 is wrong → **31**.",
   "All terms of n(n+1) are even — 31 is odd.", "medium", S, "se-p24", 40)
tt = [n ** 3 - 1 for n in range(1, 7)]
wq("wrong-number-p09", tt, 3, 65, [1, 2, 4],
   "Terms are n³ − 1: 0, 7, 26, **63**, 124, 215. The shown 65 is wrong (it is 4³ + 1) → **65**.",
   "Every other term is one less than a cube.", "hard", S, "se-p24", 55)
tt = gen_rec(3, 6, lambda x, i: x * (i + 1) + (i + 1))
wq("wrong-number-p10", tt, 4, 138, [1, 2, 3],
   "Rule ×1+1, ×2+2, ×3+3 ...: 3, 4, 10, 33, **136**, 685 (136×5 + 5 = 685). The shown 138 is wrong → **138**.",
   "Check each step with its own multiplier.", "hard", S, "se-p25", 60)
tt = inter([2, 4, 6, 8], [10, 13, 16, 19])
wq("wrong-number-p11", tt, 6, 9, [2, 3, 5],
   "Odd places: 2, 4, 6, **8** (+2). Even places: 10, 13, 16, 19 (+3). The 7th term shows 9 instead of 8 → **9**.",
   "Split the series; the error hides in one half.", "medium", S, "se-p25", 45)
tt = [L(2 + 3 * i) + L(4 + 3 * i) for i in range(5)]
assert tt == ["BD", "EG", "HJ", "KM", "NP"]
wq("wrong-number-p12", tt, 3, "KN", [1, 2, 4],
   "Each cluster has a gap of +2 inside and first letters go B, E, H, K, N (+3). So the 4th term should be **KM**; the shown **KN** is wrong.",
   "Check the gap inside every cluster first.", "medium", S, "se-p26", 45, prompt=PWL)
tt = [L(x) for x in gen_add(3, [3, 4, 5, 6, 7])]
assert tt == ["C", "F", "J", "O", "U", "B"]
wq("wrong-number-p13", tt, 4, "T", [1, 2, 3],
   "Steps +3, +4, +5, +6, +7: C, F, J, O, **U**, B (U + 7 wraps to B). The shown **T** is wrong.",
   "Rising steps; the last step wraps past Z.", "hard", S, "se-p26", 55, prompt=PWL)

# ---------------- practice: letter-blank-series ----------------
PAT = "se-p27"
bq("letter-blank-series-p01", "abcabcabcabc", [1, 5, 9, 10],
   "Block **abc** (12 places = 4 blocks). Filled line: abc | abc | abc | abc. Blanks in order: b, c, a, b → **bcab**.",
   "Column check: every block is a-b-c.", "easy", PAT, 3, 35)
bq("letter-blank-series-p02", "pqrspqrspqrs", [2, 4, 7, 9, 11],
   "Block **pqrs** repeats 3 times: pqrs | pqrs | pqrs. Blanks in order: r, p, s, q, s → **rpsqs**.",
   "12 places → try a block of 4.", "medium", PAT, 4, 45)
bq("letter-blank-series-p03", "baabbaabbaab", [0, 3, 6, 9],
   "Block **baab** repeats: baab | baab | baab. Blanks in order: b, b, a, a → **bbaa**.",
   "Blocks of 4 starting and ending with b.", "medium", PAT, 4, 45)
PAT = "se-p28"
bq("letter-blank-series-p04", "aababcabcd", [1, 4, 7, 9],
   "Parts grow by one letter: a | ab | abc | abcd. Blanks in order: a, b, b, d → **abbd**.",
   "Split as 1 + 2 + 3 + 4 places.", "medium", PAT, None, 45)
bq("letter-blank-series-p05", "abaabbaaabbb", [1, 3, 6, 10],
   "Parts: ab | aabb | aaabbb (each letter one more time in every part). Blanks in order: b, a, a, b → **baab**.",
   "Split as 2 + 4 + 6 places.", "hard", PAT, None, 55)
bq("letter-blank-series-p06", "xyxyyxyyyxyyyy", [2, 4, 8, 12],
   "Parts: xy | xyy | xyyy | xyyyy — one more y each time. Blanks in order: x, y, y, y → **xyyy**.",
   "Every part starts with x; count the y's: 1, 2, 3, 4.", "medium", PAT, None, 50)
PAT = "se-p29"
bq("letter-blank-series-p07", "pqrrqppqrrqp", [1, 3, 7, 10],
   "Block **pqrrqp** (pqr, then back rqp) repeats twice. Blanks in order: q, r, q, q → **qrqq**.",
   "The double r marks the turning point.", "medium", PAT, 6, 45)
bq("letter-blank-series-p08", "abcdcbabcdcba", [2, 5, 7, 10, 12],
   "Letters climb a→d and come back: a b c d c b | a b c d c b | a. Blanks in order: c, b, b, c, a → **cbbca**.",
   "Up to d, down to a, and up again.", "hard", PAT, 6, 55)
bq("letter-blank-series-p09", "mnoonmmnoonm", [2, 4, 6, 9],
   "Block **mnoonm** repeats twice: mno | onm | mno | onm. Blanks in order: o, n, m, o → **onmo**.",
   "The double o marks the turn.", "easy", PAT, 6, 40)
PAT = "se-p30"
bq("letter-blank-series-p10", "abcdbcdacdabdabc", [1, 6, 10, 15],
   "Blocks of 4, each starting one letter later: abcd | bcda | cdab | dabc. Blanks in order: b, d, a, c → **bdac**.",
   "Each block = previous block with its first letter moved to the end.", "hard", PAT, None, 60)
bq("letter-blank-series-p11", "xyzyzxzxy", [1, 5, 6],
   "Blocks of 3: xyz | yzx | zxy (first letter moves to the end). Blanks in order: y, x, z → **yxz**.",
   "Three blocks, three rotations.", "medium", PAT, None, 40)
bq("letter-blank-series-p12", "pqrrpqqrp", [2, 4, 7],
   "Blocks of 3: pqr | rpq | qrp (last letter moves to the front). Blanks in order: r, p, r → **rpr**.",
   "Rotation to the right: the last letter comes first.", "medium", PAT, None, 45)
# (p12 uses the right-rotation form; the pattern covers both directions)

upsert(d["practice"], Qs)

# ---------------- correctness fixes / checks on existing questions ----------------
def ans_text(qid):
    for q in d["solvedExamples"] + d["practice"]:
        if q["id"] == qid:
            return q["options"][q["answer"]]
    raise KeyError(qid)

assert ans_text("rsn-series-ex1") == str(6 * 6 + 6)
assert ans_text("rsn-series-ex2") == str(95 * 2 + 1)
assert ans_text("rsn-series-ex3") == L(11 + 5)
assert ans_text("rsn-series-ex4") == "46"
assert ans_text("rsn-series-1") == str(60 - 20)
assert ans_text("rsn-series-2") == str(108 * 3)
assert ans_text("rsn-series-3") == str(112 + 125)
assert ans_text("rsn-series-4") == str(168 * 5)
assert ans_text("rsn-series-5") == str(18 + 29)
assert ans_text("rsn-series-6") == "8"
assert ans_text("rsn-series-7") == "13.5"
assert ans_text("rsn-series-8") == str(5 * 5 - 1)
assert ans_text("rsn-series-9") == L(7 + 4)
assert ans_text("rsn-series-10") == "DW"
assert ans_text("rsn-series-11") == "D"
assert ans_text("rsn-series-12") == L(2 + 2)
assert ans_text("rsn-series-13") == "M15"
assert ans_text("rsn-series-14") == "R16"
assert ans_text("rsn-series-15") == "38"

# ---------------- pyqPatterns ----------------
d["pyqPatterns"] = [
    PYQ("Growing-difference number series", "very common",
        "Terms rise slowly and the gaps between them rise (or fall) by a fixed amount.",
        "Write the difference row and continue it. If the first row is not regular, take a second row. Add the next difference to the last term.",
        "number-series", "**11, 13, 17, 23, 31, ?**", "Differences 2, 4, 6, 8 → next 10. 31 + 10 = **41**."),
    PYQ("Multiply-and-add series (×k ± r)", "very common",
        "Terms roughly double or triple each time.",
        "Divide a term by the one before to guess k, then find the small constant left over. Confirm the same k and r on every step before applying it.",
        "number-series", "**4, 10, 28, 82, ?**", "Rule ×3 − 2. 82 × 3 − 2 = **244**."),
    PYQ("Squares, cubes and n(n+1) series", "common",
        "Terms sit on or just beside perfect squares or cubes (3, 8, 15, 24 or 2, 9, 28, 65).",
        "Compare each term with the nearest square or cube and find the fixed adjustment. Use the next n. Knowing squares to 30 and cubes to 15 makes this instant.",
        "number-series", "**2, 9, 28, 65, ?**", "Terms are n³ + 1. 5³ + 1 = **126**."),
    PYQ("Mixed-operation and alternate series", "common",
        "Growth is uneven (×1+1, ×2+2 ...) or the series goes up and down.",
        "First try splitting odd and even places into two series. If that fails, list the operation used at each step and continue the operation pattern.",
        "number-series", "**2, 3, 8, 27, 112, ?**", "×1+1, ×2+2, ×3+3, ×4+4 → next ×5+5: 112 × 5 + 5 = **565**."),
    PYQ("Missing term in the middle", "very common",
        "The '?' is between given terms instead of at the end.",
        "Find the rule from the visible terms on both sides. Fill the gap from the left neighbour and check that the right neighbour follows from your answer.",
        "series-idea", "**5, 8, 14, ?, 50, 98**", "Rule ×2 − 2. ? = 14 × 2 − 2 = **26**; check 26 × 2 − 2 = 50 ✓."),
    PYQ("Letter and letter-cluster series", "very common",
        "Single letters or groups of 2-4 letters follow a step (BDF, GIK, LNP ...).",
        "Convert letters to positions with the EJOTY anchors. For clusters, solve each slot as its own series. Remember wrap-around after Z.",
        "letter-series", "**AZ, CX, EV, GT, ?**", "First letters +2 → I; second letters −2 → R. Answer **IR**."),
    PYQ("Alphanumeric series", "common",
        "Terms mix letters and numbers (A3, D6, G9 or 2CZ, 4EX).",
        "Split into a letter column and a number column. Check first whether the number equals the letter's position. Solve each column and join the answer in the same format.",
        "alphanumeric-series", "**B2, D4, F8, H16, ?**", "Letters +2 → J; numbers ×2 → 32. Answer **J32**."),
    PYQ("Wrong number in the series", "common",
        "The series has no '?'; the question asks which term is wrong, and the options are terms of the series.",
        "Find the rule from the first few terms and rebuild the series from the start. The one term that does not match is the answer. A wrong term spoils both gaps around it.",
        "wrong-number", "**2, 6, 18, 54, 164, 486**", "Rule ×3 gives 162, not 164 → **164** is wrong."),
    PYQ("Fill the blanks in a repeating letter series", "very common",
        "A line of small letters with blanks, e.g. 'a _ c a b _ a b c _ b c'; options are letter groups.",
        "Count the places and guess the block size. Write the blocks one under another and fill each blank from its column. Watch for growing, mirror and rotating blocks.",
        "letter-blank-series", "**a _ c a b _ a b c _ b c**", "Block abc repeats. Blanks: b, c, a → **bca**."),
]
# verify pyq example numbers
assert gen_rec(4, 5, lambda x, i: 3 * x - 2)[-1] == 244
assert 5 ** 3 + 1 == 126

finish(T, d)
