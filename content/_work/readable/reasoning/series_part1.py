"""Series rewrite, part 1: helpers, series-idea, number-series. Imported by series.py."""
from fractions import Fraction as F


def diffs(s):
    return [b - a for a, b in zip(s, s[1:])]


def gen(first, step, n):
    """Series from a step function: step(prev, index) -> next."""
    out = [first]
    while len(out) < n:
        out.append(step(out[-1], len(out)))
    return out


def pos(c):
    return ord(c) - 64


def ch(n):
    return chr((n - 1) % 26 + 65)


def pat(pid, name, freq, spot, formula, steps, why, q, ex_steps, answer):
    return {"id": pid, "name": name, "frequency": freq, "howToSpot": spot, "formula": formula,
            "steps": steps, "why": why, "example": {"q": q, "steps": ex_steps, "answer": answer}}


def ex(q, steps, answer):
    return {"q": q, "steps": steps, "answer": answer}


# ====================== checks: series-idea ======================
assert [100 + 50 * i for i in range(4)] == [100, 150, 200, 250]
assert diffs([5, 9, 13, 17]) == [4] * 3
assert gen(3, lambda p, i: 2 * p + 1, 4) == [3, 7, 15, 31]
assert diffs([3, 8, 15, 24]) == [5, 7, 9] and [n * n for n in (2, 3, 4, 5)] == [4, 9, 16, 25]
s = [2, 5, 10, 17, 26]
assert diffs(s) == [3, 5, 7, 9] and 26 + 11 == 37 and [n * n + 1 for n in range(1, 6)][1:] == s[:0] + [5, 10, 17, 26]
assert gen(3, lambda p, i: 2 * p + 1, 5) == [3, 7, 15, 31, 63] and 7 * 2 + 1 == 15 and 15 * 2 + 1 == 31
assert 64 // 2 == 32 and [64 // 2 ** i for i in range(6)] == [64, 32, 16, 8, 4, 2]
assert F(1, 2) * 3 ** 4 * 1 == F(81, 2) and [F(1, 2) * 3 ** i for i in range(5)] == [F(1, 2), F(3, 2), F(9, 2), F(27, 2), F(81, 2)]
assert F(81, 2) == F(40.5)
assert [(2 * i - 1, 2 * i + 1) for i in (1, 2, 3, 4)][3] == (7, 9)
# two missing terms in the notes: 2, ?, 8, ?, 14, 17  (+3)
assert gen(2, lambda p, i: p + 3, 6) == [2, 5, 8, 11, 14, 17]
# se-p1
S1 = [6, 11, 21, 36, 56]
assert diffs(S1) == [5, 10, 15, 20] and 56 + 25 == 81
# se-p2
S2 = gen(7, lambda p, i: 2 * p + 1, 5)
assert S2 == [7, 15, 31, 63, 127]
# se-p3
assert [81 // 3 ** i for i in range(5)] == [81, 27, 9, 3, 1] and F(1, 3) == F(1) / 3
# se-p4
S4 = gen(1, lambda p, i: p + i, 7)
assert S4 == [1, 2, 4, 7, 11, 16, 22] and diffs(S4) == [1, 2, 3, 4, 5, 6]
# se-p31 (first term)
S31 = [6, 12, 20, 30, 42]
assert diffs(S31) == [6, 8, 10, 12] and 12 - 6 == 6
# trick: ladder in 10 seconds
T1 = [4, 7, 12, 19, 28]
assert diffs(T1) == [3, 5, 7, 9] and 28 + 11 == 39
T2 = [5, 8, 14, 23, 35]
assert diffs(T2) == [3, 6, 9, 12] and 35 + 15 == 50

SERIES_IDEA = dict(
    concept=(
        "A series is a list of numbers written in a fixed order. Every term comes from the one before it by one small rule. "
        "Your job is to name that rule, then find the next term or the missing term. "
        "The **difference ladder** finds the rule in most questions: subtract neighbours, and subtract again if needed."
    ),
    notes=r"""### What a series is
A series is a list of numbers in a fixed order. Each term comes from the one before it by the same small rule.

Think of a savings box. You save ₹100, ₹150 and ₹200. Next you save ₹250, because the rule is "add ₹50".

Exams ask series in three forms.

- **Next term:** 4, 9, 16, 25, ? Find the term after the last one.
- **Missing term:** 4, 9, ?, 25, 36. A term in the middle is hidden.
- **Wrong term:** one term in a full series is wrong. The wrong number lesson covers it.

### Look at the size first
Before you calculate, see how fast the terms grow.

| What you see | Likely rule |
|---|---|
| 5, 9, 13, 17: slow and steady | Add a number |
| 3, 7, 15, 31: nearly doubling | Multiply, maybe add a little |
| 8, 20, 10, 18, 12: up and down | Two series mixed together |
| 3, 8, 15, 24: just below 4, 9, 16, 25 | Squares |

### The difference ladder
Write the gap between each pair of neighbours. This is the first row of gaps.

> **Example:** 2, 5, 10, 17, 26. The gaps are 3, 5, 7, 9. They rise by 2, so the next gap is 11. The next term is 26 + 11 = **37**.

If the gaps are not clear, take the gaps of the gaps. Most exam series become clear in two rows.

| What the gaps show | Rule |
|---|---|
| All gaps equal | Add the same number |
| Gaps rise or fall evenly | Growing or shrinking gap |
| Gaps double | Powers of 2 are added |
| Gaps are 1, 4, 9, 16 | Squares are added |

### When the ladder fails
Try these in order.

1. **Ratio:** divide each term by the one before it.
2. **Alternate terms:** read places 1, 3, 5 and places 2, 4, 6 as two series.
3. **Squares and cubes:** look for terms near them.
4. **Mixed steps:** such as ×1 + 1, ×2 + 2, ×3 + 3.

### The missing term in the middle
Use the terms on **both sides** of the gap to find the rule. Then check twice. Your term must come from the one before it. The next term must come from your term.

> **Example:** 3, 7, ?, 31, 63. Each term is ×2 + 1. So ? = 7 × 2 + 1 = 15. Check: 15 × 2 + 1 = 31.

### Fractions, decimals and halving
Do not panic at decimals. The series 64, 32, 16, 8, 4 halves each time, so the next term is 2. The series 0.5, 1.5, 4.5, 13.5 is ×3, so the next term is 40.5.

For fractions, treat the tops and the bottoms as two series. In $\dfrac{1}{3}, \dfrac{3}{5}, \dfrac{5}{7}$ the tops go 1, 3, 5 and the bottoms go 3, 5, 7. Both rise by 2, so the next term is $\dfrac{7}{9}$.

### Two missing terms
Find the rule from the visible terms. Fill the first blank, then move on to the second. Check the term after each blank.

> **Tip:** Your rule must fit every term you can see, not just the last two.
""",
    formulas=[
        {"name": "Gap between terms", "tex": r"d_n = a_{n+1} - a_n", "note": "Write these gaps under the series. If they are not clear, take gaps of the gaps."},
        {"name": "Same number added", "tex": r"a_n = a_1 + (n - 1)d", "note": "d is the equal gap. Use it when the first row of gaps is constant."},
    ],
    tricks=[
        {"title": "Two rows of gaps in ten seconds",
         "body": "Write the gaps under the series. If they are not equal, write the gaps of the gaps. Stop when a row is clear. Then work back up.",
         "example": ex("Find the next term: 4, 7, 12, 19, 28, ?",
                       ["Gaps: 3, 5, 7, 9.", "The gaps rise by 2, so the next gap is 11.", "28 + 11 = 39."], "39")},
        {"title": "Say the rule aloud in words",
         "body": "Before you calculate, say the rule in one plain sentence, like 'add 3, then add 6, then add 9'. If you cannot say it in a sentence, the rule is wrong.",
         "example": ex("Find the next term: 5, 8, 14, 23, 35, ?",
                       ["Gaps: 3, 6, 9, 12.", "Rule in words: the gap grows by 3 each time.", "The next gap is 15. So 35 + 15 = 50."], "50")},
    ],
    mistakes=[
        {"wrong": "Guessing the rule from the last two terms only.", "right": "The rule must fit every term. Test it from the first term."},
        {"wrong": "Stopping after one row of gaps when it is not equal.", "right": "Take gaps of the gaps. The second row often shows the rule."},
        {"wrong": "Filling a middle blank without checking the next term.", "right": "Check that the term after the blank comes from your answer."},
        {"wrong": "Reading decimals or fractions as unusual rules.", "right": "Use the same ideas. Decimals follow ×k or ÷k. Fractions split into tops and bottoms."},
        {"wrong": "Trying squares first on every series.", "right": "Look at the size first. Slow growth means gaps. Fast growth means ratio."},
    ],
    revision=[
        "Look at the size first: slow growth adds, fast growth multiplies, up and down means two series.",
        "Difference ladder: first row of gaps, then the gaps of the gaps.",
        "If the ladder fails, try ratio, then alternate terms, then squares and cubes, then mixed steps.",
        "Missing term: check with the term before it and the term after it.",
        "Fractions: tops and bottoms are two separate series.",
        "The rule must fit every visible term.",
    ],
    patterns=[
        pat("se-p1", "Find the next term with the difference ladder", "very common",
            "The question shows five to seven terms ending in a '?'. Nothing is hidden in the middle.",
            None,
            ["Write the gaps under the series.", "If the gaps are not equal, write the gaps of the gaps.", "Continue the last row by one step.", "Climb back up: add to the last gap, then to the last term."],
            "The ladder turns a hard series into a short list of simple gaps.",
            "Find the next term: 6, 11, 21, 36, 56, ?",
            ["Gaps: 5, 10, 15, 20.", "The gaps rise by 5, so the next gap is 25.", "56 + 25 = 81."],
            "81"),
        pat("se-p2", "A missing term in the middle", "very common",
            "A '?' sits between the given terms, like 7, 15, ?, 63, 127.",
            None,
            ["Use the terms on both sides of the gap to find the rule.", "Find the missing term from the term before it.", "Check that the next term comes from your answer."],
            "The terms on both sides fix the rule, and the second check catches slips.",
            "Find the missing term: 7, 15, ?, 63, 127",
            ["15 = 7 × 2 + 1 and 127 = 63 × 2 + 1. The rule is ×2 + 1.", "? = 15 × 2 + 1 = 31.", "Check: 31 × 2 + 1 = 63."],
            "31"),
        pat("se-p3", "Fractions, decimals or halving", "common",
            "The terms are decimals, fractions, or keep getting divided, like 81, 27, 9, 3, 1.",
            None,
            ["Check the ratio between terms first: divide one term by the next.", "For fractions, write the tops and bottoms as two series.", "Apply the rule once to the last term."],
            "The same rules work on decimals and fractions. Only the numbers look different.",
            "Find the next term: 81, 27, 9, 3, 1, ?",
            ["27 ÷ 81 = 1/3, and 9 ÷ 27 = 1/3.", "Each term is the last one ÷ 3.", r"$1 \div 3 = \dfrac{1}{3}$."],
            r"$\dfrac{1}{3}$"),
        pat("se-p4", "Two missing terms: pick the right pair", "common",
            "Two '?' marks sit in one series, and each option is a pair of numbers.",
            None,
            ["Find the rule from the visible terms.", "Fill the first blank.", "Use the rule again to fill the second blank.", "Check the terms after both blanks."],
            "Each blank follows from the one before it, so fill them in order.",
            "Fill the blanks: 1, 2, 4, ?, 11, ?, 22",
            ["The first gaps are 1 and 2. Guess that the gaps rise by 1: 1, 2, 3, 4, 5, 6.", "First blank: 4 + 3 = 7. Check: 7 + 4 = 11.", "Second blank: 11 + 5 = 16. Check: 16 + 6 = 22."],
            "7 and 16"),
        pat("se-p31", "Find the first term", "occasional",
            "The '?' is at the start, like ?, 12, 20, 30, 42.",
            None,
            ["Write the gaps between the visible terms.", "Extend the gap row backwards by one step.", "Subtract that gap from the first visible term."],
            "A series can be read backwards just like forwards.",
            "Find the first term: ?, 12, 20, 30, 42",
            ["Gaps between the visible terms: 8, 10, 12. They rise by 2.", "Going back, the gap before 8 is 6.", "First term: 12 − 6 = 6. Check: 6, 12, 20, 30, 42 has gaps 6, 8, 10, 12."],
            "6"),
    ],
)

# ====================== checks: number-series ======================
assert gen(7, lambda p, i: p + 5, 5) == [7, 12, 17, 22, 27]
assert gen(11, lambda p, i: p + 2 * i, 5) == [11, 13, 17, 23, 31] and 31 + 10 == 41
assert gen(120, lambda p, i: p - (2 * i - 1), 4) == [120, 119, 116, 111]
assert gen(3, lambda p, i: 2 * p, 4) == [3, 6, 12, 24]
assert gen(3, lambda p, i: 2 * p + 1, 5) == [3, 7, 15, 31, 63]
assert gen(4, lambda p, i: 3 * p - 2, 4) == [4, 10, 28, 82] and 15 // 1 == 15
assert [n * n - 1 for n in range(2, 7)] == [3, 8, 15, 24, 35]
assert [n ** 3 + 1 for n in range(1, 5)] == [2, 9, 28, 65]
assert [n * (n + 1) for n in range(1, 6)] == [2, 6, 12, 20, 30]
t = [2, 5, 11, 21, 36]
assert diffs(t) == [3, 6, 10, 15] and diffs(diffs(t)) == [3, 4, 5] and 15 + 6 == 21 and 36 + 21 == 57
u = [10, 11, 13, 17, 25]
assert diffs(u) == [1, 2, 4, 8] and 25 + 16 == 41
alt = [3, 50, 6, 45, 12, 40, 24, 35]
assert alt[0::2] == [3, 6, 12, 24] and alt[1::2] == [50, 45, 40, 35]
assert gen(2, lambda p, i: p * i + i, 5)[:5] == [2, 3, 8, 27, 112]    # x1+1, x2+2 ...
assert 112 * 5 + 5 == 565
assert gen(5, lambda p, i: p + 1 if i % 2 else p * 2, 7) == [5, 6, 12, 13, 26, 27, 54]
assert gen(10, lambda p, i: p + (i + 1) * (1 if i % 2 else -1) + 0, 1) == [10]
sgn = [10]
for i, d in enumerate([2, -3, 4, -5, 6]):
    sgn.append(sgn[-1] + d)
assert sgn == [10, 12, 9, 13, 8, 14]
fib = [2, 3]
while len(fib) < 6:
    fib.append(fib[-1] + fib[-2])
assert fib == [2, 3, 5, 8, 13, 21]
tri = [1, 2, 3]
while len(tri) < 8:
    tri.append(sum(tri[-3:]))
assert tri == [1, 2, 3, 6, 11, 20, 37, 68]
# se-p5
P5 = [4, 6, 10, 16, 24]
assert diffs(P5) == [2, 4, 6, 8] and 24 + 10 == 34
# se-p6
P6 = gen(2, lambda p, i: 3 * p - 1, 5)
assert P6 == [2, 5, 14, 41, 122]
# se-p7
assert [n * n - 1 for n in range(1, 7)] == [0, 3, 8, 15, 24, 35]
# se-p8
P8 = [3, 4, 7, 13, 23]
assert diffs(P8) == [1, 3, 6, 10] and diffs(diffs(P8)) == [2, 3, 4] and 10 + 5 == 15 and 23 + 15 == 38
# se-p9
P9 = [1, 10, 2, 20, 3, 30, 4]
assert P9[0::2] == [1, 2, 3, 4] and P9[1::2] == [10, 20, 30]
# se-p10
P10 = gen(1, lambda p, i: p * i + i, 6)
assert P10 == [1, 2, 6, 21, 88, 445]
# se-p11
f11 = [1, 1]
while len(f11) < 7:
    f11.append(f11[-1] + f11[-2])
assert f11 == [1, 1, 2, 3, 5, 8, 13]
# se-p12
P12 = [5, 6, 10, 19, 35]
assert diffs(P12) == [1, 4, 9, 16] and 35 + 25 == 60
# tricks
R1 = gen(5, lambda p, i: 2 * p + 1, 5)
assert R1 == [5, 11, 23, 47, 95]
J = [12, 5, 14, 8, 16, 11, 18]
assert J[0::2] == [12, 14, 16, 18] and J[1::2] == [5, 8, 11]
C1 = [2, 3, 11, 38, 102]
assert diffs(C1) == [1, 8, 27, 64] and 102 + 125 == 227 and 5 ** 3 == 125

NUMBER_SERIES = dict(
    concept=(
        "Most number-series questions come from eight families. "
        "Learn the families, and each question becomes a quick check against a short list. "
        "Slow growth points to gaps. Fast growth points to multiplying. Going up and down points to two series mixed together."
    ),
    notes=r"""### The eight families
Almost every number series uses one of these rules.

| Family | Example | Next |
|---|---|---|
| Same or growing gap | 7, 12, 17, 22 | 27 |
| Multiply, then adjust | 3, 7, 15, 31 | 63 |
| Squares and cubes | 3, 8, 15, 24 | 35 |
| Gaps of gaps | 2, 5, 11, 21, 36 | 57 |
| Famous gaps | 10, 11, 13, 17, 25 | 41 |
| Alternate series | 3, 50, 6, 45, 12, 40 | 24 |
| Mixed steps | 2, 3, 8, 27, 112 | 565 |
| Sum of earlier terms | 2, 3, 5, 8, 13 | 21 |

### Add the same or a growing number
In 7, 12, 17, 22 the gap is always 5. This is an arithmetic progression (AP).

The gap can also grow. In 11, 13, 17, 23, 31 the gaps are 2, 4, 6, 8. The next gap is 10, so the next term is 41. The gap can fall too: 120, 119, 116, 111 has gaps 1, 3, 5, all taken away.

### Multiply, then add or subtract
Multiply by a fixed number, then add or subtract a small number. The series 3, 6, 12, 24 is ×2. The series 3, 7, 15, 31 is ×2 + 1. The series 4, 10, 28, 82 is ×3 − 2.

> **Tip:** Divide a big term by the one before it. If the answer is near 2 or 3, try ×2 or ×3. The small amount left over is the number to add or subtract.

### Squares and cubes
Learn squares up to 30 and cubes up to 15. Look for terms just above or below them.

- 3, 8, 15, 24, 35 is $n^2 - 1$.
- 2, 9, 28, 65 is $n^3 + 1$.
- 2, 6, 12, 20, 30 is $n \times (n + 1)$.

### Gaps of gaps, and famous gaps
Sometimes the first gaps are not equal, but the second gaps follow a rule.

> **Example:** 2, 5, 11, 21, 36. First gaps: 3, 6, 10, 15. Second gaps: 3, 4, 5. The next second gap is 6, so the next first gap is 21. The next term is 36 + 21 = **57**.

The gaps can also be squares (1, 4, 9, 16), cubes (1, 8, 27, 64), primes or powers of 2. In 10, 11, 13, 17, 25 the gaps are 1, 2, 4, 8. The next gap is 16, so the next term is 41.

### Alternate series
Two series are mixed. Places 1, 3, 5, 7 make one series. Places 2, 4, 6, 8 make another.

In 3, 50, 6, 45, 12, 40, 24, ? the odd places are 3, 6, 12, 24 (×2). The even places are 50, 45, 40 (−5). The eighth term is an even place, so it is 35.

> **Watch:** Suspect an alternate series when the terms jump up and down.

### Mixed steps and sums of earlier terms
The step changes in a fixed way.

- ×1 + 1, ×2 + 2, ×3 + 3: 2, 3, 8, 27, 112. The next term is 112 × 5 + 5 = 565.
- Two steps take turns: 5, 6, 12, 13, 26, 27. The steps are +1, ×2, +1, ×2, so the next term is 54.
- Signs change: 10, 12, 9, 13, 8. The steps are +2, −3, +4, −5, so the next step is +6 and the term is 14.

In a sum-of-earlier-terms series, each term is the sum of the last two: 2, 3, 5, 8, 13, 21. Or of the last three: 1, 2, 3, 6, 11, 20, 37.

### How to choose fast
1. Slow growth: use the ladder of gaps.
2. Fast growth: divide each term by the last one.
3. Up and down: split into odd and even places.
4. Terms near squares or cubes: use the family of squares and cubes.
5. Each term close to the sum of the two before: sum of earlier terms.
""",
    formulas=[
        {"name": "Same gap (AP)", "tex": r"a_n = a_1 + (n - 1)d", "note": "d is the equal gap from the ladder."},
        {"name": "Multiply then adjust", "tex": r"a_{n+1} = k \cdot a_n \pm r", "note": "Try k = 2 and 3 first, with r = 1 or 2."},
        {"name": "Squares family", "tex": r"a_n = n^2 \pm k \ \text{ or } \ n^2 + n", "note": "If the second gaps are all 2, the series is built on n squared."},
        {"name": "Same ratio (GP)", "tex": r"a_n = a_1 \cdot r^{\,n-1}", "note": "r is the fixed ratio. Test ×2, ×3 and ×1.5."},
    ],
    tricks=[
        {"title": "Ratio test before anything fancy",
         "body": "Divide each term by the one before it. If the result is close to 2 or 3, try ×k ± r. Find r from what is left over.",
         "example": ex("Find the next term: 5, 11, 23, 47, ?",
                       ["11 ÷ 5, 23 ÷ 11 and 47 ÷ 23 are all near 2.", "5 × 2 + 1 = 11, 11 × 2 + 1 = 23, 23 × 2 + 1 = 47.", "47 × 2 + 1 = 95."], "95")},
        {"title": "Split a jumpy series",
         "body": "If the terms go up and down, write the odd places on one line and the even places on another. Solve each line on its own. Then find which line the asked place belongs to.",
         "example": ex("Find the seventh term: 12, 5, 14, 8, 16, 11, ?",
                       ["Odd places: 12, 14, 16.", "Even places: 5, 8, 11.", "The seventh term is an odd place, so it is 16 + 2 = 18."], "18")},
        {"title": "Cubes hiding in the gaps",
         "body": "If the gaps grow very fast, check for cubes (1, 8, 27, 64, 125) or powers of 2 (1, 2, 4, 8, 16).",
         "example": ex("Find the next term: 2, 3, 11, 38, 102, ?",
                       ["Gaps: 1, 8, 27, 64. These are cubes.", "The next gap is 5³ = 125.", "102 + 125 = 227."], "227")},
    ],
    mistakes=[
        {"wrong": "Trying only 'add' on a series that grows fast.", "right": "Look at the size first. Fast growth needs a ratio test."},
        {"wrong": "Stopping at the first row of gaps.", "right": "Take the gaps of the gaps. Look for squares, cubes and powers of 2."},
        {"wrong": "Reading an up-and-down series as one series.", "right": "Split into odd and even places. Then find the place asked."},
        {"wrong": "Using the last two terms to guess the rule.", "right": "Test the rule on every term from the start."},
        {"wrong": "Forgetting that ×k ± r needs a small leftover.", "right": "After ×2 or ×3, find what is left over. That is the r."},
        {"wrong": "Giving the second-gap answer as the next term.", "right": "Climb back up: next second gap, then next gap, then next term."},
    ],
    revision=[
        "Slow growth: gaps. Fast growth: ratio. Up and down: two series. Near squares or cubes: powers.",
        "Same or growing gap: 7, 12, 17 (+5) and 11, 13, 17, 23 (+2, +4, +6).",
        "Multiply then adjust: 3, 7, 15, 31 is ×2 + 1.",
        "Squares and cubes: n² − 1, n³ + 1 and n(n + 1).",
        "Gaps of gaps: find the next second gap, then the next gap, then the term.",
        "Alternate series: split odd and even places and check which one the asked term is in.",
        "Sum of earlier terms: each term is the sum of the last two, or three, terms.",
    ],
    patterns=[
        pat("se-p5", "Same or growing gap", "very common",
            "The terms grow slowly and steadily. The gaps are equal, or they rise or fall by the same amount.",
            None,
            ["Write the gaps under the series.", "If the gaps are equal, add one more gap.", "If the gaps rise evenly, work out the next gap first."],
            "A steady gap and an evenly growing gap are the two simplest families.",
            "Find the next term: 4, 6, 10, 16, 24, ?",
            ["Gaps: 2, 4, 6, 8.", "The next gap is 10.", "24 + 10 = 34."],
            "34"),
        pat("se-p6", "Multiply, then add or subtract", "very common",
            "The terms roughly double or triple. The ratio is close to, but not exactly, the same.",
            r"a_{n+1} = k \cdot a_n \pm r",
            ["Divide a big term by the one before it.", "Try ×2 or ×3 on a small term.", "Find the number left over. That is r.", "Check the rule on every term."],
            "Multiplying with a small fix at each step grows fast and looks messy.",
            "Find the next term: 2, 5, 14, 41, ?",
            ["Try ×3: 2 × 3 = 6, and 5 is 1 less.", "14 = 5 × 3 − 1 and 41 = 14 × 3 − 1.", "Next: 41 × 3 − 1 = 122."],
            "122"),
        pat("se-p7", "Squares, cubes and n × (n + 1)", "very common",
            "The terms sit on or next to squares (4, 9, 16), cubes (8, 27, 64), or look like 2, 6, 12, 20.",
            r"n^2 \pm k,\ n^3 \pm k,\ n(n+1)",
            ["Compare each term with the nearest square or cube.", "Find the small number added or taken away.", "Check that it is the same for every term.", "Use the next n."],
            "Setters like squares and cubes because the terms grow in a way students can check.",
            "Find the next term: 0, 3, 8, 15, 24, ?",
            [r"$1^2 - 1 = 0$, $2^2 - 1 = 3$, $3^2 - 1 = 8$.", r"$4^2 - 1 = 15$ and $5^2 - 1 = 24$.", r"Next: $6^2 - 1 = 35$."],
            "35"),
        pat("se-p8", "Gaps of gaps", "common",
            "The first gaps are not equal, but they rise in a pattern like 1, 3, 6, 10.",
            None,
            ["Write the first gaps.", "Write the second gaps.", "Continue the second gaps by one step.", "Climb back to the next gap, then the next term."],
            "If the second gaps follow a rule, the first gaps are easy to extend.",
            "Find the next term: 3, 4, 7, 13, 23, ?",
            ["First gaps: 1, 3, 6, 10.", "Second gaps: 2, 3, 4. The next is 5.", "Next first gap = 10 + 5 = 15. Term = 23 + 15 = 38."],
            "38"),
        pat("se-p9", "Two series mixed together", "common",
            "The series goes up and down, or big and small terms take turns.",
            None,
            ["Write odd places on one line and even places on another.", "Solve each line on its own.", "Find whether the asked place is odd or even.", "Extend that line by one term."],
            "Two simple series woven together look like one messy series.",
            "Find the next term: 1, 10, 2, 20, 3, 30, ?",
            ["Odd places: 1, 2, 3. Even places: 10, 20, 30.", "The seventh term is an odd place.", "The odd line goes up by 1, so the term is 4."],
            "4"),
        pat("se-p10", "Mixed steps: ×1 + 1, ×2 + 2 and so on", "common",
            "The terms grow faster and faster with no fixed ratio, or two steps clearly take turns.",
            None,
            ["Try ×1 + 1 on the first pair.", "If the multiplier and the added number both rise by 1 each step, this is the rule.", "Check every pair, then apply the next multiplier."],
            "The multiplier keeps growing, so the ratio is never the same twice.",
            "Find the next term: 1, 2, 6, 21, 88, ?",
            ["1 × 1 + 1 = 2 and 2 × 2 + 2 = 6.", "6 × 3 + 3 = 21 and 21 × 4 + 4 = 88.", "Next: 88 × 5 + 5 = 445."],
            "445"),
        pat("se-p11", "Sum of the earlier terms", "occasional",
            "Each term is close to the sum of the two (or three) terms before it.",
            None,
            ["Add the first two terms and compare with the third.", "If it fits, add the last two terms for the next.", "If the terms are small changes off, try the last three."],
            "In a Fibonacci-type series, the gaps look just like the series itself.",
            "Find the next term: 1, 1, 2, 3, 5, 8, ?",
            ["1 + 1 = 2, 1 + 2 = 3, 2 + 3 = 5, 3 + 5 = 8.", "Each term is the sum of the last two.", "5 + 8 = 13."],
            "13"),
        pat("se-p12", "Gaps that are squares, cubes, primes or powers of 2", "occasional",
            "The gap row is a famous list: 1, 4, 9, 16, or 1, 8, 27, or 2, 3, 5, 7, or 1, 2, 4, 8.",
            None,
            ["Write the first gaps.", "Recognise the list of the gaps.", "Take the next number of that list.", "Add it to the last term."],
            "The gaps carry the rule, not the terms.",
            "Find the next term: 5, 6, 10, 19, 35, ?",
            ["Gaps: 1, 4, 9, 16. These are squares.", "The next square is 25.", "35 + 25 = 60."],
            "60"),
    ],
)
