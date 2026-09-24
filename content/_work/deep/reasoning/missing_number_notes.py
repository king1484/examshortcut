"""Missing-number topic: NOTES + PATTERNS (imported by missing-number.py)."""
import os
import sys

sys.path.insert(0, os.path.dirname(__file__))
from _lib import P  # noqa

NOTES = {}

NOTES["missing-number-idea"] = """### One hidden rule, found by systematic guessing

A figure — grids, circles, triangles — carries a hidden rule connecting its numbers; one cell is missing. You are not looking for THE rule, only for A simple rule that fits every complete row/segment and gives one of the options.

**The standard search order.** For each complete row (or matching pair of cells), test in this sequence and stop at the first rule that fits everywhere:
1. Sums and differences: third = first + second, or their difference.
2. Products and quotients: third = first × second (watch a constant ×, like 2ab).
3. Squares and near-squares: third = a², a² + b, a² + b², a² − 1 — numbers like 25, 26, 48, 49 are square magnets.
4. Mixed: first² ± second, (first + second)², first × second ± constant.

**Fit everywhere, not somewhere.** A rule that works on one row is a coincidence. Every complete row must reproduce its third number (and every complete grid must reproduce the other grid's numbers) before you trust it on the missing cell. Two rows fitting 'a + b' while the third fits 'a × b' means the rule is wrong — real exam rules are uniform.

**Two-grid puzzles.** When two complete grids sit beside an incomplete one, the rule lives *inside* each grid (usually row by row), and the second grid simply repeats the first grid's rule with different numbers. Solve grid 1 completely first, verify on grid 2, then apply to grid 3.

**Segments (circles, triangles).** Match positions: opposite segments, or corner-vs-centre. Common segment rules: opposite pairs share a constant sum; centre = sum (or product) of corners; each ring adds a constant.

**Option-driven pruning.** If the missing cell must be, say, odd, every even option dies — check parity first. If rows are increasing, a decreasing option dies. Prune before deep work; with two options left, often only one fits a plausible rule.

### Quick revision
- Test rules in order: + / − → × / ÷ → squares → mixed (a² ± b, (a+b)²...).
- The rule must fit EVERY complete row/segment — one fit is a coincidence.
- Two grids: solve grid 1, verify on grid 2, apply to grid 3.
- Segments: match opposite positions; centre often = sum/product of corners.
- Prune by parity and trend before hunting the rule."""

NOTES["grid-row-rules"] = """### The CGL workhorse: grids where rows (or columns) share a rule

The format: a 3×3 grid — sometimes two complete grids and a third with a hole. Each row obeys the same rule turning its first two numbers into its third. Everything is row-arithmetic; the skill is finding the rule fast.

**The two-number bridge.** Cover the third column and hunt a bridge from column 1 to column 2 — or from columns 1+2 to column 3. The classic bridges, in testing order:
- $c = a + b$ and $c = a - b$ (or $|a-b|$) — check signs.
- $c = a \\times b$; then $c = 2ab$, $c = ab + k$, $c = ab - k$ with a small constant.
- $c = a^2 + b$, $c = b^2 + a$, $c = a^2 + b^2$ — the Pythagorean look (3-4-25, 5-12-169).
- $c = (a + b)^2$ or $(a - b)^2$ — results like 49, 64, 144 are squares.
- Digit tricks (see the digit-operations lesson): digit sums and reversals.

**Confirm on every row.** Compute the candidate rule on all complete rows. A rule fitting row 1 and row 3 but not row 2 is dead — keep hunting. This one habit separates solvers from guessers.

**Column rules.** When rows refuse every bridge, the rule runs down the columns: third row = f(first row, second row) cell by cell, or column 2 = average of columns 1 and 3, or column 3 = column 1 − column 2. Same procedure, transposed.

**Two complete grids.** Solve the left grid's rule first (it has no hole), verify it reproduces the middle grid, then apply to the right one. The rule never changes between grids; only the numbers do.

**Circle and triangle figures.** Match by position: opposite segments of a circle (constant sum or product), corners vs centre of a triangle (centre = sum or product of corners), inner ring vs outer ring. Write the matched pairs as little equations and look for the common thread.

### Quick revision
- Bridge hunt order: + / − → × / ÷ → ×2, ab ± k → a²+b, b²+a, a²+b² → (a±b)².
- The rule must reproduce EVERY complete row (and grid 2 in two-grid puzzles).
- Rows stuck → test columns; grids stuck → test opposite segments / centre vs corners.
- Squares in the options (25, 49, 144) beg for a square-based rule.
- Digit sums and reversals are fair game — see digit-operations."""

NOTES["digit-operations"] = """### When the rule lives inside the digits

A large family of missing-number puzzles never add the *values* — they operate on **digits**: sums of digits, reversed digits, products of digits. Recognising the family early saves minutes.

**The digit-sum rule.** $S(n)$ = sum of a number's digits: $S(47) = 11$. Typical rules:
- third = $S(a) + S(b)$ — e.g. 47 and 38 give $11 + 11 = 22$;
- third = $S(a + b)$ — add first, then sum digits (68 → 14);
- third = $2 \\times S(a)$ — doubling a digit sum.
Tell them apart by testing one complete row with each variant; only one will fit both rows.

**The reversal family.** $R(n)$ = the number with digits reversed: $R(43) = 34$. Common rules:
- third = $R(a) + R(b)$ — the classic 'reversed-sum' grid (34 + 41 = 75);
- third = $|R(a) - b|$;
- third = $R(a + b)$ — add first, then flip (39 → 93).
Reversal rules produce third numbers whose digits are the 'mirror image' of the row's story — options like 75 next to 43 and 14 are a waving flag.

**The digit-product rule.** $P(n)$ = product of digits: $P(47) = 28$. Rules: third = $P(a)$, third = $P(a) + P(b)$, third = $P(a) \\times S(b)$. Zero is the instant tell — a row containing 0 or 10 has digit product 0, which usually kills product rules on sight.

**Spotting the family.** Hints that the rule is digit-based:
- The third numbers are far too small or too large for plain sums/products of the values.
- Options cluster near digit-scale numbers (5-30) while the values are two-digit.
- The same digits recur across rows (43/34, 62/26) — reversal is in play.

**Verification is cheap here.** Digit rules are one line of arithmetic per row — check all complete rows, not just one. And compute the final answer with the SAME variant that fit, not with the variant you tried first.

### Quick revision
- $S(n)$ = digit sum (47 → 11); $R(n)$ = reversal (43 → 34); $P(n)$ = digit product (47 → 28).
- Standard rules: $S(a)+S(b)$, $S(a+b)$, $2S(a)$, $R(a)+R(b)$, $|R(a)-b|$, $R(a+b)$, $P(a)+P(b)$.
- Test each variant on a complete row; only one fits all rows.
- Options far smaller than the values → digit rule; mirror-looking pairs → reversal.
- Zeros kill digit-product rules instantly."""

PATTERNS = {}

PATTERNS["missing-number-idea"] = [
    P("mn-p1", "Third number from two: linear rules", "very common",
        "Rows of two/three numbers where the third is a plain sum, difference or multiple of the first.",
        "1. Test c = ka (constant multiple) and c = a ± b.\n2. k must be the same in every row.\n3. Apply to the incomplete row.\n\n*Why it works:* the simplest rules are linear, so they are tried first.",
        "**Rows: 4 → 20, 6 → 30, 5 → ?**",
        "Second = 5 × first in both rows → 5 × 5 = **25**.", None),
    P("mn-p2", "Square-based rules", "very common",
        "Third numbers near perfect squares (25, 26, 35, 48, 49...).",
        "1. Test c = a² ± b, c = a² ± 1, c = a² + b².\n2. Square the first number and see what the leftover equals.\n3. Verify on all rows before answering.\n\n*Why it works:* squares plus a small correction are a favourite exam construction.",
        "**Rows: 3 → 10, 4 → 17, 5 → ?**",
        "10 = 3² + 1, 17 = 4² + 1 → 5² + 1 = **26**.", None),
    P("mn-p3", "Two-grid analogy", "common",
        "Two complete grids and a third with a missing cell.",
        "1. Find grid 1's row rule.\n2. Verify it reproduces grid 2 exactly.\n3. Apply it to grid 3's incomplete row.\n\n*Why it works:* the second grid is a free verification of the rule.",
        "**Grid 1 rows: (2,3,7), (3,4,13). Grid 2 rows: (4,5,?), (5,6,31).**",
        "Grid 1: c = a×b + 1 (7, 13). Grid 2 row 2: 5×6+1 = 31 ✓ → ? = 4×5+1 = **21**.", None),
    P("mn-p4", "Verify-then-answer discipline", "common",
        "Any figure where several rules 'almost' fit, or a cross/2×2 layout.",
        "1. Candidate rule must fit every complete row/segment AND match an option.\n2. For 2×2 crosses: test diagonal products and sums too.\n3. Reject a rule that fits two rows but fails the third.\n\n*Why it works:* exam figures are built from one uniform rule; near-misses are bait.",
        "**Rows: 9 → 81, 12 → 144, 15 → ?**",
        "Both rows square the first number → 15² = **225**.", None),
]

PATTERNS["grid-row-rules"] = [
    P("gr-p1", "Row sums and differences", "very common",
        "Third column close to the sum or difference of the first two.",
        "1. Test c = a + b on all rows; then c = |a − b|.\n2. Watch sign traps (a − b vs b − a).\n3. Apply the fitting rule to the incomplete row.\n\n*Why it works:* the default construction of exam grids.",
        "**Rows: (5,8,13), (6,9,15), (7,11,?)**",
        "c = a + b fits every row → 7 + 11 = **18**.", None),
    P("gr-p2", "Products, doubled products and squares", "common",
        "Third column much larger than the first two, or a perfect square.",
        "1. Test c = ab, then 2ab, then ab ± k.\n2. If c is a square, test a² + b² and (a+b)².\n3. Fit all rows.\n\n*Why it works:* multiplicative and square rules create the 'too big' signature.",
        "**Rows: (3,4,25), (6,8,100), (5,12,?)**",
        "25 = 3² + 4², 100 = 6² + 8² → 5² + 12² = **169**.", None),
    P("gr-p3", "Column rules", "common",
        "Rows refuse every bridge; try the grid vertically.",
        "1. Test column3 = column1 ± column2 (cell by cell down the rows).\n2. Test column2 = (column1 + column3) / 2.\n3. Confirm on every complete column.\n\n*Why it works:* transposing the rule is the standard disguise.",
        "**Rows: (10,14,18), (22,25,28), (30,?,40)**",
        "Column 2 = average of columns 1 and 3 (14, 25) → (30+40)/2 = **35**.", None),
    P("gr-p4", "Circle and triangle segments", "common",
        "Numbers around a circle or in triangle corners with a centre.",
        "1. Pair opposite segments; test constant sum, then product.\n2. For triangles: centre vs sum/product of corners.\n3. Verify on every matched pair.\n\n*Why it works:* segment figures repeat one relation across matched positions.",
        "**Circle: opposite pairs 12–8, 15–5, 18–?**",
        "Each pair sums to 20 → ? = 20 − 18 = **2**.", None),
]

PATTERNS["digit-operations"] = [
    P("do-p1", "Digit-sum rules", "very common",
        "Third numbers are small (5-30) while values are two-digit.",
        "1. S(n) = digit sum. Test c = S(a) + S(b), then c = S(a + b).\n2. Test on a complete row first, then everywhere.\n3. Apply the fitting variant to the missing cell.\n\n*Why it works:* digit sums shrink big numbers into option-sized ones.",
        "**Rows: (36,24,15), (28,19,20), (47,38,?)**",
        "S(36)+S(24) = 9+6 = 15 ✓; S(28)+S(19) = 10+10 = 20 ✓ → S(47)+S(38) = 11+11 = **22**.", None),
    P("do-p2", "Reversal rules", "very common",
        "Digits mirror across the row (43 beside 34); third numbers look like flipped sums.",
        "1. R(n) = reversed digits. Test c = R(a) + R(b).\n2. Then |R(a) − b| and R(a + b).\n3. Check on all rows.\n\n*Why it works:* reversal is the most reused digit trick in CGL grids.",
        "**Rows: (23,14,73), (45,12,75), (62,23,?)**",
        "R(23)+R(14) = 32+41 = 73 ✓; R(45)+R(12) = 54+21 = 75 ✓ → R(62)+R(23) = 26+32 = **58**.", None),
    P("do-p3", "Digit-product rules", "common",
        "Third numbers too small even for digit sums, or options under ~30.",
        "1. P(n) = product of digits. Test c = P(a), then P(a) + P(b).\n2. A 0 in the values usually kills product rules — check first.\n3. Fit everywhere.\n\n*Why it works:* digit products collapse two-digit numbers into tiny ones.",
        "**Rows: (24,8), (35,15), (47,?)**",
        "P(24) = 8, P(35) = 15 → P(47) = 4×7 = **28**.", None),
    P("do-p4", "Mixed digit arithmetic", "common",
        "Digit sums combined with the other value: multiply, double, or weight.",
        "1. Test c = 2·S(a), c = S(a) × b, c = S(a) + b.\n2. The b-value stays whole while the digit-sum shrinks a.\n3. Verify variant on all rows.\n\n*Why it works:* mixing one digit op with one raw value hides the rule one level deeper.",
        "**Rows: (24,3,18), (35,2,16), (47,2,?)**",
        "S(24)×3 = 6×3 = 18 ✓; S(35)×2 = 8×2 = 16 ✓ → S(47)×2 = 11×2 = **22**.", None),
]

PYQS = [
    ("Row-rule hunt in a grid", "very common", "grid-row-rules",
     "A 3×3 grid with one missing cell; rows (or columns) share a hidden rule.",
     "Test bridges in order: a+b, |a−b|, ab, 2ab, ab±k, a²+b², (a+b)² — fit on every complete row before applying.",
     "**Rows: (6,3,15), (8,4,28), (9,5,?)**",
     "Plain a+b fails (9, 12). Divide out: 15 = 5×3, 28 = 7×4 — the multipliers 5, 7 are one less than the first numbers → c = (a−1)×b → (9−1)×5 = **40**."),
    ("Two grids, one rule", "common", "grid-row-rules",
     "Two complete grids and an incomplete third.",
     "Derive the rule on the first grid, verify it on the second, then apply to the third.",
     "**Grid 1: (2,3,7),(3,4,13). Grid 2: (4,5,?),(5,6,31)**",
     "c = a×b + 1 → 31 ✓ → 4×5 + 1 = **21**."),
    ("Digit-sum grid", "common", "digit-operations",
     "Third numbers tiny compared with the values.",
     "S(a)+S(b) first, then S(a+b); fit on all complete rows.",
     "**Rows: (29,14,18), (38,25,20), (56,34,?)**",
     "S(29)+S(14) = 11+5 = 16, but the answer is 18 — a constant +2 gap. Check row 2: S(38)+S(25) = 11+7 = 18, +2 = 20 ✓ → rule is S(a)+S(b)+2 → 11+7+2 = **20**."),
]
