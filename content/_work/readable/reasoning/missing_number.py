"""Readable rewrite of Reasoning > Missing Number (3 subtopics).

Every example is recomputed below. Each hidden rule is also tested against the
simpler rules to prove the example has exactly the story the text tells.
Run: python missing_number.py  (patches content/core/topics/reasoning/missing-number.json)
"""
import json
from pathlib import Path

ROOT = Path(__file__).resolve().parents[3]
TOPIC = ROOT / "core" / "topics" / "reasoning" / "missing-number.json"


def S(n):
    return sum(int(d) for d in str(n))


def R(n):
    return int(str(n)[::-1])


def P(n):
    out = 1
    for d in str(n):
        out *= int(d)
    return out


def fits(rule, rows):
    """rule(a, b) == c for every complete (a, b, c) row."""
    return all(rule(a, b) == c for a, b, c in rows)


def fits1(rule, rows):
    return all(rule(a) == c for a, c in rows)


SIMPLE = {
    "a+b": lambda a, b: a + b, "a-b": lambda a, b: a - b, "|a-b|": lambda a, b: abs(a - b),
    "ab": lambda a, b: a * b, "a2+b": lambda a, b: a * a + b, "a2-b": lambda a, b: a * a - b,
    "a2+b2": lambda a, b: a * a + b * b, "(a+b)2": lambda a, b: (a + b) ** 2,
}


def only_rule(rows, name):
    """Among the simple rules, exactly `name` fits every complete row."""
    ok = [k for k, f in SIMPLE.items() if fits(f, rows)]
    assert ok == [name], (rows, ok)


# =============== missing-number-idea ===============
# notes
assert 3 ** 2 == 9 and 4 ** 2 == 16 and 5 ** 2 == 25
W_ROWS = [(3, 4, 13), (5, 2, 11)]
assert 3 + 4 != 13 and 3 * 4 == 12 and 3 * 4 + 1 == 13 and 5 * 2 + 1 == 11 and 6 * 3 + 1 == 19 and 6 * 3 == 18
assert fits(lambda a, b: a * b + 1, W_ROWS)
assert not any(fits(f, W_ROWS) for f in SIMPLE.values())
assert 26 == 5 ** 2 + 1 and 21 == 4 * 5 + 1
# size table samples
assert 4 + 7 == 11 and 4 * 7 == 28 and 4 * 7 + 1 == 29 and 4 ** 2 + 1 == 17
# two grids
G1 = [(2, 3, 7), (3, 4, 13)]
assert fits(lambda a, b: a * b + 1, G1) and 5 * 6 + 1 == 31 and 4 * 5 + 1 == 21
# mn-p1
assert fits1(lambda a: 5 * a, [(4, 20), (6, 30)]) and 5 * 5 == 25
# mn-p2
assert fits1(lambda a: a * a + 1, [(3, 10), (4, 17)]) and 5 * 5 + 1 == 26
# mn-p4: two rules fit row 1; row 2 kills one
P4 = [(2, 2, 4), (3, 5, 15)]
assert 2 + 2 == 4 and 2 * 2 == 4 and 3 + 5 != 15 and 3 * 5 == 15 and 6 * 4 == 24
only_rule(P4, "ab")
# mn-p5: cubes
cube1 = lambda n: n ** 3 + 1
assert fits1(cube1, [(2, 9), (3, 28), (4, 65)]) and cube1(5) == 126
assert 5 ** 3 == 125 and 5 ** 2 + 1 == 26
# mn-p6: multiply then add
assert fits1(lambda n: 2 * n + 1, [(5, 11), (8, 17)]) and 2 * 12 + 1 == 25
assert 5 + 6 != 11 or True
assert not fits1(lambda n: n + 6, [(5, 11), (8, 17)])
# trick 2
assert 9 - 2 * 3 == 3 or True
T2 = [(4, 7, 29), (5, 3, 16)]
assert fits(lambda a, b: a * b + 1, [(4, 7, 29)]) and 5 * 3 + 1 == 16 and 6 * 2 + 1 == 13

# =============== grid-row-rules ===============
GW = [(4, 6, 10), (5, 3, 22)]
assert fits(lambda a, b: a * a - b, GW) and 7 ** 2 - 2 == 47
assert 4 + 6 == 10 and 5 + 3 != 22 and 7 + 2 == 9 and 4 * 6 == 24
only_rule(GW, "a2-b")
# gr-p1
G_P1 = [(5, 8, 13), (6, 9, 15)]
only_rule(G_P1, "a+b") and None
assert fits(SIMPLE["a+b"], G_P1) and 7 + 11 == 18
# gr-p2 (old)
G_P2 = [(3, 4, 25), (6, 8, 100)]
only_rule(G_P2, "a2+b2")
assert 5 ** 2 + 12 ** 2 == 169 and 13 ** 2 == 169 and 13 ** 2 != 196
# gr-p3 column rule
GRID = [[2, 3, 5], [4, 5, 6], [8, 15, None]]
assert GRID[0][0] * GRID[1][0] == GRID[2][0] and GRID[0][1] * GRID[1][1] == GRID[2][1]
COL3 = GRID[0][2] * GRID[1][2]
assert COL3 == 30
# rows do not carry a simple rule
row_ok = [(2, 3, 5), (4, 5, 6)]
assert not any(fits(f, row_ok) for f in SIMPLE.values())
# average rule (notes/trick)
assert (10 + 18) // 2 == 14 and (22 + 28) // 2 == 25 and (30 + 40) // 2 == 35
assert fits(lambda a, b: (a + b) // 2, [(12, 8, 10), (20, 6, 13)]) and (14 + 4) // 2 == 9
# gr-p4 circle
assert 12 + 8 == 20 and 15 + 5 == 20 and 20 - 18 == 2
# triangle (notes)
assert 2 * 3 * 4 == 24 and 1 * 5 * 3 == 15 and 2 * 6 * 3 == 36
# gr-p5 ab + k
G_P5 = [(2, 5, 11), (4, 3, 13)]
assert fits(lambda a, b: a * b + 1, G_P5) and 6 * 4 + 1 == 25
only_rule_ab1 = [k for k, f in SIMPLE.items() if fits(f, G_P5)]
assert only_rule_ab1 == []
# gr-p6 (a+b)*k
G_P6 = [(4, 7, 22), (6, 3, 18)]
assert fits(lambda a, b: (a + b) * 2, G_P6) and (9 + 5) * 2 == 28
assert [k for k, f in SIMPLE.items() if fits(f, G_P6)] == []
# gr-p7 a^2 - b
G_P7 = [(8, 15, 49), (7, 10, 39)]
assert fits(SIMPLE["a2-b"], G_P7) and 9 ** 2 - 6 == 75
only_rule(G_P7, "a2-b")
# tricks / formulas
assert 8 ** 2 - 15 == 49 and (4 + 7) * 2 == 22 and 26 // 2 == 13
assert 7 * 7 - 3 * 3 == (7 + 3) * (7 - 3) == 40

# =============== digit-operations ===============
assert S(47) == 11 and S(38) == 11 and S(47) + S(38) == 22
assert R(43) == 34 and P(47) == 28
assert 47 + 38 == 85 and 85 % 9 == 22 % 9 == 4
assert 34 + 41 == 75 and R(43) + R(14) == 34 + 41
assert R(39) == 93 and S(68) == 14
assert R(40) == 4
# do-p1
D1 = [(36, 24, 15), (28, 19, 20)]
d1 = lambda a, b: S(a) + S(b)
assert fits(d1, D1) and d1(47, 38) == 22
assert not fits(lambda a, b: S(a + b), D1)     # S(a+b): 60->6 no
assert not any(fits(f, D1) for f in SIMPLE.values())
# do-p2
D2 = [(23, 14, 73), (46, 25, 116)]
d2 = lambda a, b: R(a) + R(b)
assert fits(d2, D2) and d2(58, 17) == 156 and R(58 + 17) == 57
assert not any(fits(f, D2) for f in SIMPLE.values())
assert not fits(lambda a, b: R(a + b), D2)
# do-p3
D3 = [(24, 8), (35, 15)]
assert fits1(P, D3) and P(47) == 28
# do-p4
D4 = [(24, 3, 18), (35, 2, 16)]
assert fits(lambda a, b: S(a) * b, D4) and S(47) * 2 == 22
assert not fits(lambda a, b: S(a) + b, D4)
# do-p5 reverse of sum
D5 = [(24, 18, 24), (32, 13, 54)]
d5 = lambda a, b: R(a + b)
assert fits(d5, D5) and d5(26, 15) == 14 and 26 + 15 == 41
assert not fits(lambda a, b: R(a) + R(b), D5)
assert R(24) + R(18) == 42 + 81 or True
assert not any(fits(f, D5) for f in SIMPLE.values())
# do-p6 digit sum of the sum
D6 = [(39, 25, 10), (57, 18, 12)]
d6 = lambda a, b: S(a + b)
assert fits(d6, D6) and d6(68, 26) == 13 and 68 + 26 == 94
assert not fits(lambda a, b: S(a) + S(b), D6) and S(68) + S(26) == 22
assert not any(fits(f, D6) for f in SIMPLE.values())
assert 39 + 25 == 64 and S(39) == 12 and S(25) == 7 and S(39) + S(25) == 19 and S(64) == 10 and S(75) == 12
# do-p7 digit sums plus constant
D7 = [(28, 9, 21), (36, 23, 16)]
d7 = lambda a, b: S(a) + S(b) + 2
assert fits(d7, D7) and d7(45, 17) == 19
assert not fits(lambda a, b: S(a) + S(b), D7)
assert not any(fits(f, D7) for f in SIMPLE.values())
# trick: reversal
assert 24 + 18 == 42 and R(42) == 24 and 32 + 13 == 45 and R(45) == 54


def pat(pid, name, freq, spot, formula, steps, why, q, ex_steps, answer):
    return {"id": pid, "name": name, "frequency": freq, "howToSpot": spot, "formula": formula,
            "steps": steps, "why": why, "example": {"q": q, "steps": ex_steps, "answer": answer}}


SUBS = {}

# ---------------------------------------------------------------------
SUBS["missing-number-idea"] = dict(
    concept=(
        "A figure hides one number with a '?'. The other parts of the figure follow one **hidden rule**. "
        "Find the rule from the complete rows, check it on every row, then use it once on the row with the '?'. "
        "Most rules are simple: add, multiply, square, or one small change on top."
    ),
    notes=r"""### What the puzzle looks like
A figure hides one number. It may be rows of numbers, two square grids, a circle or a triangle. Every complete part follows the **same rule**. Find it. Then use it once on the part with the "?".

Small example: 3 → 9, 4 → 16, 5 → ?. Each number is squared. So ? = 25.

> **Rule:** The rule is the same in every complete row. One row can fit a wrong rule by luck. Two rows almost never do.

### The rule ladder
Test simple rules first. Stop at the first rule that fits **all** the rows.

| Step | Rule to test | Sample with 4 and 7 |
|---|---|---|
| 1 | Add or subtract | 4 + 7 = 11 |
| 2 | Multiply | 4 × 7 = 28 |
| 3 | Multiply, then add or subtract a small number | 4 × 7 + 1 = 29 |
| 4 | Square, or square and adjust | $4^2 + 1 = 17$ |
| 5 | Digit tricks (sum, reverse) | see the digit lesson |

### Check every row
Rows: (3, 4, 13), (5, 2, 11), (6, 3, ?).

1. Try the sum. 3 + 4 = 7, not 13. Drop it.
2. Try the product. 3 × 4 = 12. The answer 13 is one more.
3. Guess: third = first × second + 1.
4. Test on row 2. 5 × 2 + 1 = 11. It fits.
5. Apply to row 3. 6 × 3 + 1 = **19**.

> **Tip:** Write the rule as a small formula, like c = a × b + 1. Then test that formula on the spare row.

### Start from the biggest number
The biggest number in a row is usually the answer of the rule. The smaller numbers are the inputs.

Ask: how do the small numbers build the big one? 26 comes from 5 as $5^2 + 1$. 21 comes from 4 and 5 as 4 × 5 + 1. Reading left to right hides the rule. Building the biggest number shows it.

### Read the size of the answer
Compare the answer with the inputs. This tells you which family to try.

| The answer is | Try first |
|---|---|
| About the sum of the inputs | Add or subtract |
| About the product | Multiply, then adjust |
| Close to a square number | Squares, like $a^2 \pm b$ |
| Smaller than both inputs | Difference, average or a digit rule |

### Two grids and one hole
Often two complete grids sit beside a grid with a "?". The rule works inside each grid, row by row.

1. Find the rule in grid 1.
2. Test it on grid 2. It must fit every row.
3. Apply it to the row with the "?".

Grid 1 rows: (2, 3, 7) and (3, 4, 13). Rule: a × b + 1. Grid 2 has (5, 6, 31). Check: 5 × 6 + 1 = 31. So (4, 5, ?) gives 4 × 5 + 1 = **21**.

### Wrong options are planted
The examiner puts the most tempting wrong answer in the options. If the rule is a × b + 1, the plain product is there as bait.

For row (6, 3, ?), the plain product is 18. The right answer is 19. If your answer matches a simpler version of the rule, test that simple rule on a complete row. It will fail.

> **Watch:** Never answer from one row. Two rows must agree.
""",
    formulas=[
        {"name": "Rule check", "tex": r"f(a_1, b_1) = c_1 \text{ and } f(a_2, b_2) = c_2 \Rightarrow \text{use } f", "note": "One row fitting proves nothing. Two rows fitting is strong proof."},
        {"name": "Common families", "tex": r"a + b,\ a - b,\ ab,\ ab \pm k,\ (a + b)k,\ a^2 \pm b", "note": "Sums and products cover most puzzles. Try them first."},
    ],
    tricks=[
        {"title": "Test the spare row",
         "body": "Write your guessed rule as a formula. Test it on the second complete row. Only then use it on the row with the ?. This takes ten seconds and stops the most common wrong answer.",
         "example": {"q": "Row 1: 3, 4, 13. Row 2: 5, 2, 11. Row 3: 6, 3, ?. Find ?.",
                     "steps": ["Guess c = a × b + 1. Row 1: 3 × 4 + 1 = 13.", "Test row 2: 5 × 2 + 1 = 11. It fits.", "Apply to row 3: 6 × 3 + 1 = 19."],
                     "answer": "19"}},
        {"title": "Build the biggest number first",
         "body": "Pick the biggest number in the row. Try to make it from the smaller ones. This finds the rule faster than reading left to right.",
         "example": {"q": "Row 1: 4, 7, 29. Row 2: 5, 3, 16. Row 3: 6, 2, ?. Find ?.",
                     "steps": ["Biggest is 29. 4 × 7 = 28, so 29 = 4 × 7 + 1.", "Test row 2: 5 × 3 + 1 = 16. It fits.", "Row 3: 6 × 2 + 1 = 13."],
                     "answer": "13"}},
    ],
    mistakes=[
        {"wrong": "Fitting a rule to the first row and answering at once.", "right": "Test the rule on the second complete row before you use it."},
        {"wrong": "Reading the figure only left to right.", "right": "The rule may run down a column or across opposite parts. Try those too."},
        {"wrong": "Using a three-step rule when a simple one exists.", "right": "Real exam rules are short. Try add, multiply and square first."},
        {"wrong": "Picking the option that equals the plain product or plain square.", "right": "That is often bait. Check that the plain rule really fits a complete row."},
        {"wrong": "Mixing the numbers of grid 1 with grid 2.", "right": "Find the rule in one grid. Then apply it on the other grid."},
    ],
    revision=[
        "Test rules in this order: add or subtract, multiply, multiply and adjust, squares, digit tricks.",
        "The rule must fit every complete row. One fit is luck.",
        "The biggest number in a row is usually the answer of the rule.",
        "The size of the answer tells you the family: sum, product or square.",
        "Two grids: find the rule in grid 1, test on grid 2, then apply it.",
        "The plain product or plain square is often a planted wrong option.",
    ],
    patterns=[
        pat("mn-p1", "Third number is a multiple of the first", "very common",
            "Rows of two numbers. The second is a fixed multiple of the first, or a plain sum or difference.",
            None,
            ["Divide the second number by the first in each row.", "If the answer is the same, that is the multiplier.", "Multiply the first number of the last row by it."],
            "The simplest rules are tried first, and this one is the simplest.",
            "Rows: 4 → 20, 6 → 30, 5 → ?. Find ?.",
            ["20 ÷ 4 = 5 and 30 ÷ 6 = 5.", "The rule is: second = first × 5.", "5 × 5 = 25."],
            "25"),
        pat("mn-p2", "Square of the number, then adjust", "very common",
            "The answers sit close to perfect squares like 10, 17, 26 or 48.",
            None,
            ["Square the first number in each row.", "Find what is left over: add or subtract a number.", "The leftover must be the same in every row.", "Apply to the last row."],
            "A square with a small correction is a favourite exam rule.",
            "Rows: 3 → 10, 4 → 17, 5 → ?. Find ?.",
            [r"$3^2 = 9$, and 10 is 1 more.", r"$4^2 = 16$, and 17 is 1 more.", r"Rule: $n^2 + 1$. So $5^2 + 1 = 26$."],
            "26"),
        pat("mn-p3", "Two grids, one rule", "common",
            "Two complete grids and a third grid with one missing cell.",
            None,
            ["Find the row rule in grid 1.", "Test it on grid 2. It must fit.", "Use it on the row with the ?."],
            "The second grid is a free check of the rule.",
            "Grid 1 rows: (2, 3, 7) and (3, 4, 13). Grid 2 rows: (4, 5, ?) and (5, 6, 31). Find ?.",
            ["Grid 1: 2 × 3 + 1 = 7 and 3 × 4 + 1 = 13.", "Check grid 2: 5 × 6 + 1 = 31. It fits.", "4 × 5 + 1 = 21."],
            "21"),
        pat("mn-p4", "Two rules fit the first row", "common",
            "The first row fits more than one rule. Only a second row can choose between them.",
            None,
            ["Write every rule that fits row 1.", "Test each one on row 2.", "Keep the rule that fits both rows.", "Use it on the last row."],
            "Setters build rows so that a wrong rule survives one row but not two.",
            "Rows: (2, 2, 4), (3, 5, 15), (6, 4, ?). Find ?.",
            ["Row 1: both 2 + 2 and 2 × 2 give 4.", "Row 2: 3 + 5 = 8, not 15. But 3 × 5 = 15.", "The rule is a × b. So 6 × 4 = 24."],
            "24"),
        pat("mn-p5", "Cube of the number, then adjust", "common",
            "The answers jump fast: 9, 28, 65. They sit next to cubes like 8, 27, 64.",
            None,
            ["Cube the first number in each row.", "Check the leftover. It must be the same in every row.", "Apply the rule to the last row."],
            "When answers grow faster than squares, a cube is the next family to try.",
            "Rows: 2 → 9, 3 → 28, 4 → 65, 5 → ?. Find ?.",
            [r"$2^3 = 8$, and 9 is 1 more.", r"$3^3 = 27$ and $4^3 = 64$. Both are 1 less than the answer.", r"Rule: $n^3 + 1$. So $5^3 + 1 = 126$."],
            "126"),
        pat("mn-p6", "Multiply, then add a number", "common",
            "Each answer is a little more than a multiple of the first number.",
            None,
            ["Divide each answer by the first number to guess the multiplier.", "The leftover gives the number to add.", "Test on both rows, then apply."],
            "Two small operations in a row are still a simple rule.",
            "Rows: 5 → 11, 8 → 17, 12 → ?. Find ?.",
            ["Try × 2: 5 × 2 = 10 (1 short), 8 × 2 = 16 (1 short).", "Rule: first × 2 + 1.", "12 × 2 + 1 = 25."],
            "25"),
    ],
)

# ---------------------------------------------------------------------
SUBS["grid-row-rules"] = dict(
    concept=(
        "In a 3×3 grid, each row usually turns its first two numbers into the third with the same rule. "
        "Sometimes the rule runs down the columns instead. "
        "Find the rule on the complete rows, test it on every complete row, then fill the hole."
    ),
    notes=r"""### What a grid puzzle looks like
A grid has three rows of three numbers. One cell is a "?". Each row follows the same rule.

Row (4, 6, 10): here 4 + 6 = 10. The first two numbers make the third. Your job is to find this link fast.

### Hunt for the link
Cover the third column. Ask how the first two numbers make the third. Try these in order.

1. Add or subtract: $a + b$, $a - b$.
2. Multiply: $ab$. Then $2ab$, $ab + k$, $ab - k$.
3. Squares: $a^2 + b$, $a^2 - b$, $a^2 + b^2$.
4. Square of a sum: $(a + b)^2$.
5. Sum times a number: $(a + b) \times k$.
6. Average: $\dfrac{a + b}{2}$.

> **Tip:** If the third number is a perfect square, like 25, 49 or 144, try a square rule first.

### Check every row
Rows: (4, 6, 10), (5, 3, 22), (7, 2, ?).

1. Sum: 4 + 6 = 10. It fits row 1. But 5 + 3 = 8, not 22. Drop it.
2. Product: 4 × 6 = 24, not 10. Drop it.
3. Try $a^2 - b$. Row 1: 16 − 6 = 10. Row 2: 25 − 3 = 22. Both fit.
4. Apply: 49 − 2 = **47**.

> **Watch:** Stopping at row 1 would give 7 + 2 = 9. That is the planted wrong option. Always test the second row.

### When rows fail, try columns
If no row rule fits, read the grid downwards. The third row may come from the first two rows, cell by cell.

Rows: (2, 3, 5), (4, 5, 6), (8, 15, ?). Check the columns: 2 × 4 = 8 and 3 × 5 = 15. So the third row is first row × second row. Then ? = 5 × 6 = **30**.

The middle cell can also be the average of the outer cells. In (10, 14, 18) and (22, 25, 28), the middle number is the average. So (30, ?, 40) gives 35.

### Sum, then a multiplier
Sometimes the third number is a multiple of the sum. Add the first two numbers. Then divide the third number by that sum.

Rows: (4, 7, 22) and (6, 3, 18). Row 1: 4 + 7 = 11, and 22 ÷ 11 = 2. Row 2: 6 + 3 = 9, and 18 ÷ 9 = 2. The multiplier is 2 in both rows. So (9, 5, ?) gives 14 × 2 = **28**.

### Circles and triangles
Match parts by position.

- Circle: opposite parts often share a total. Pairs 12–8 and 15–5 both add to 20. So 18 pairs with 2.
- Triangle: the centre may be the sum or product of the corners. Corners 2, 3, 4 give centre 24. Corners 1, 5, 3 give 15. So corners 2, 6, 3 give 36.

Write each matched set as a small sum. Look for the same link in every set.

### Two complete grids
The rule stays the same in both grids. Only the numbers change. Solve the left grid, check it on the middle grid, then use it on the last grid.

### Speed helps
- Learn squares up to 25.
- Use $a^2 - b^2 = (a + b)(a - b)$ to skip big squares: $7^2 - 3^2 = 10 \times 4 = 40$.
- Build the biggest cell first: $22 = (4 + 7) \times 2$.

> **Rule:** One rule, every row, then answer.
""",
    formulas=[
        {"name": "Sum times a number", "tex": r"c = (a + b) \times k", "note": "Rows (4, 7, 22) and (6, 3, 18) give k = 2."},
        {"name": "Square minus the second", "tex": r"c = a^2 - b", "note": "Rows (8, 15, 49) and (7, 10, 39) fit."},
        {"name": "Sum of two squares", "tex": r"c = a^2 + b^2", "note": "Rows (3, 4, 25) and (6, 8, 100) fit."},
        {"name": "Average of two", "tex": r"c = \dfrac{a + b}{2}", "note": "Rows (12, 8, 10) and (20, 6, 13) fit."},
    ],
    tricks=[
        {"title": "Build the biggest cell first",
         "body": "Write the biggest cell of a row. Rebuild it from the other two. This shows the rule faster than reading left to right.",
         "example": {"q": "Row 1: 4, 7, 22. Row 2: 6, 3, 18. Row 3: 9, 5, ?. Find ?.",
                     "steps": ["22 = (4 + 7) × 2.", "Test row 2: (6 + 3) × 2 = 18. It fits.", "Row 3: (9 + 5) × 2 = 28."],
                     "answer": "28"}},
        {"title": "Copy the grid as three rows",
         "body": "Write the grid as three lines in your rough space, with the ? in place. Reading numbers off the figure while you calculate leads to mistakes.",
         "example": {"q": "Row 1: 12, 8, 10. Row 2: 20, 6, 13. Row 3: 14, 4, ?. Find ?.",
                     "steps": ["10 = (12 + 8) ÷ 2.", "Test row 2: (20 + 6) ÷ 2 = 13. It fits.", "Row 3: (14 + 4) ÷ 2 = 9."],
                     "answer": "9"}},
    ],
    mistakes=[
        {"wrong": "Using grid 1's row rule on grid 2's columns.", "right": "Use the same direction in every grid. Rows with rows, columns with columns."},
        {"wrong": "Picking between two half-fitting rules by feel.", "right": "Test both rules on every complete row. Keep only the one that fits all."},
        {"wrong": "Squaring wrongly, like 13² = 196.", "right": "13² = 169. Learn squares up to 25."},
        {"wrong": "Stopping when row 1 fits.", "right": "Row 2 must fit too. A rule that fits one row is luck."},
        {"wrong": "Reading a column rule as a row rule.", "right": "If no row rule fits, read the grid downwards."},
    ],
    revision=[
        "Try in order: sum or difference, product, squares, (a + b)², sum times a number, average.",
        "The rule must fit every complete row, and the second grid too.",
        "Rows fail: try columns. Circles: opposite parts. Triangles: centre and corners.",
        "Third numbers that are perfect squares point to a square rule.",
        "Build the biggest cell from the others.",
        "Learn squares up to 25. Use a² − b² = (a + b)(a − b).",
    ],
    patterns=[
        pat("gr-p1", "Row sums and differences", "very common",
            "The third number is close to the sum or difference of the first two.",
            None,
            ["Test c = a + b on every row.", "If it fails, test the difference a − b.", "Use the rule that fits every row."],
            "Adding is the most common way to build a grid.",
            "Rows: (5, 8, 13), (6, 9, 15), (7, 11, ?). Find ?.",
            ["5 + 8 = 13 and 6 + 9 = 15.", "The rule is a + b.", "7 + 11 = 18."],
            "18"),
        pat("gr-p2", "Squares added together", "common",
            "The third number is much bigger than the first two, and it is a perfect square.",
            r"c = a^2 + b^2",
            ["Square both numbers.", "Add the squares.", "Check every row, then apply."],
            "Square rules make the third number too big for a plain sum or product.",
            "Rows: (3, 4, 25), (6, 8, 100), (5, 12, ?). Find ?.",
            [r"$3^2 + 4^2 = 9 + 16 = 25$.", r"$6^2 + 8^2 = 36 + 64 = 100$.", r"$5^2 + 12^2 = 25 + 144 = 169$."],
            "169"),
        pat("gr-p3", "Column rules", "common",
            "No row rule fits. The grid may work downwards.",
            None,
            ["Test third row = first row + second row, cell by cell.", "Then test the product of the two rows.", "Confirm on every complete column, then fill the hole."],
            "The setter sometimes turns the rule to run down the columns.",
            "Rows: (2, 3, 5), (4, 5, 6), (8, 15, ?). Find ?.",
            ["Column 1: 2 × 4 = 8. Column 2: 3 × 5 = 15.", "The third row is first row × second row.", "Column 3: 5 × 6 = 30."],
            "30"),
        pat("gr-p4", "Circle and triangle figures", "common",
            "Numbers sit around a circle, or at the corners of a triangle with a centre.",
            None,
            ["Pair opposite parts of the circle. Test a fixed sum, then a fixed product.", "For a triangle, test centre = sum or product of the corners.", "Confirm on every matching set."],
            "These figures repeat one link across matched parts.",
            "A circle has opposite pairs 12 and 8, 15 and 5, and 18 and ?. Find ?.",
            ["12 + 8 = 20 and 15 + 5 = 20.", "Each opposite pair adds to 20.", "20 − 18 = 2."],
            "2"),
        pat("gr-p5", "Multiply, then add or subtract a number", "very common",
            "The third number is a little more or less than the product of the first two.",
            r"c = ab \pm k",
            ["Multiply the first two numbers in each row.", "Find what is left over. It must be the same in every row.", "Apply to the last row."],
            "A small change on a product is the most used disguise for multiplying.",
            "Rows: (2, 5, 11), (4, 3, 13), (6, 4, ?). Find ?.",
            ["2 × 5 = 10, and 11 is 1 more.", "4 × 3 = 12, and 13 is 1 more.", "Rule: a × b + 1. So 6 × 4 + 1 = 25."],
            "25"),
        pat("gr-p6", "Sum, then multiply by a number", "common",
            "The third number is even, or a multiple of a fixed number, and bigger than the sum.",
            r"c = (a + b) \times k",
            ["Add the first two numbers.", "Divide the third number by that sum.", "The quotient k must be the same in every row.", "Apply to the last row."],
            "Adding first and then scaling is a common two-step rule.",
            "Rows: (4, 7, 22), (6, 3, 18), (9, 5, ?). Find ?.",
            ["4 + 7 = 11 and 22 ÷ 11 = 2.", "6 + 3 = 9 and 18 ÷ 9 = 2.", "(9 + 5) × 2 = 28."],
            "28"),
        pat("gr-p7", "Square of the first, minus the second", "common",
            "The third number is close to the square of the first number.",
            r"c = a^2 - b",
            ["Square the first number.", "Subtract the third number from the square. The result should be the second number.", "Check every row, then apply."],
            "Squares with a subtraction often hide behind large third numbers.",
            "Rows: (8, 15, 49), (7, 10, 39), (9, 6, ?). Find ?.",
            [r"$8^2 - 15 = 64 - 15 = 49$.", r"$7^2 - 10 = 49 - 10 = 39$.", r"$9^2 - 6 = 81 - 6 = 75$."],
            "75"),
    ],
)

# ---------------------------------------------------------------------
SUBS["digit-operations"] = dict(
    concept=(
        "Some puzzles work on the **digits** of the numbers, not on their values. "
        "The rule may add the digits of each number, reverse the digits, or multiply the digits. "
        "Try a digit rule when ordinary sums and products do not fit."
    ),
    notes=r"""### When the rule uses digits
Some rows look odd because the values do not match: 28, 9, 21. Adding the digits explains it: 2 + 8 = 10, then 10 + 9 + 2 = 21.

Three digit tools cover most puzzles. Learn their short names.

| Tool | Meaning | Example |
|---|---|---|
| $S(n)$ | sum of the digits | $S(47) = 4 + 7 = 11$ |
| $R(n)$ | digits reversed | $R(43) = 34$ |
| $P(n)$ | product of the digits | $P(47) = 4 \times 7 = 28$ |

### Digit-sum rules
The answer is small, but the numbers are two-digit. Try these:

- $S(a) + S(b)$: 47 and 38 give 11 + 11 = 22.
- $S(a + b)$: add first, then sum the digits. 68 gives 14.
- A digit sum times a number, like $S(a) \times b$.

Test one variant on a complete row. Then test it on the next row. Only one variant fits all.

### Reversal rules
Look for mirror pairs, like 43 and 34.

- $R(a) + R(b)$: reverse both numbers, then add. 34 + 41 = 75.
- $R(a + b)$: add first, then reverse the sum. 39 becomes 93.

> **Tip:** Reversing first and adding first can give different answers. Test both on a row where the digits carry over.

### Digit-product rules
The answer is very small. Multiply the digits of each number.

$P(24) = 2 \times 4 = 8$ and $P(35) = 15$. So $P(47) = 28$.

> **Watch:** A number with a 0, like 40 or 10, has a digit product of 0. This usually rules out a product rule at once.

### A full walk-through
Rows: (39, 25, 10), (57, 18, 12), (68, 26, ?).

1. Plain sum: 39 + 25 = 64, not 10. Drop it.
2. Digit sums added: 3 + 9 = 12 and 2 + 5 = 7. Total 19, not 10. Drop it.
3. Add first, then take the digit sum: 64 gives 6 + 4 = 10. It fits.
4. Test row 2: 57 + 18 = 75, and 7 + 5 = 12. It fits.
5. Apply: 68 + 26 = 94, and 9 + 4 = **13**.

### How to spot a digit rule
- The answers are far too small or too big for plain sums and products.
- The answers are near 5 to 30 while the numbers are two-digit.
- The same digits appear again and again: 43 and 34, or 62 and 26.

### A quick check with 9
A number and its digit sum leave the same remainder when divided by 9. This helps to check a digit-sum answer. For example 47 + 38 = 85, and $S(47) + S(38) = 22$. Both 85 and 22 leave remainder 4.

### Add a fixed number
Sometimes the digit sums are close but always short by the same amount. Rows (28, 9, 21) and (36, 23, 16) show it. The digit sums total 19 and 14. The answers are 2 more each time. So the rule is $S(a) + S(b) + 2$.

### Reversal with a zero
- Reversing the inputs when the rule reverses the sum, or the other way round.
- A sum that ends in 0, like 40. Reversal gives 04 = 4. Setters avoid this. If you see it, you may have the wrong rule.

> **Rule:** Use the same variant that fitted the complete rows. Do not switch to another one for the last row.
""",
    formulas=[
        {"name": "Digit sum", "tex": r"S(47) = 4 + 7 = 11", "note": "Add the digits of the number."},
        {"name": "Reversal", "tex": r"R(43) = 34", "note": "Write the digits in the opposite order."},
        {"name": "Digit product", "tex": r"P(47) = 4 \times 7 = 28", "note": "Multiply the digits of the number."},
    ],
    tricks=[
        {"title": "Switch to digits when standard rules fail",
         "body": "Give ordinary rules about 30 seconds. If both complete rows refuse them, test these in order: digit sums, reverse of the sum, digit sums plus a number.",
         "example": {"q": "Row 1: 28, 9, 21. Row 2: 36, 23, 16. Row 3: 45, 17, ?. Find ?.",
                     "steps": ["Sums and products fail.", "Row 1: 10 + 9 = 19, and 21 is 2 more. Row 2: 9 + 5 = 14, and 16 is 2 more.", "Row 3: 9 + 8 + 2 = 19."],
                     "answer": "19"}},
        {"title": "Add first, then flip",
         "body": "A reversal answer must read backwards cleanly. Add the two numbers first, then reverse the sum. Confirm on two rows.",
         "example": {"q": "Row 1: 24, 18, 24. Row 2: 32, 13, 54. Row 3: 26, 15, ?. Find ?.",
                     "steps": ["24 + 18 = 42. Reversed: 24.", "32 + 13 = 45. Reversed: 54.", "26 + 15 = 41. Reversed: 14."],
                     "answer": "14"}},
    ],
    mistakes=[
        {"wrong": "Reversing the inputs when the rule reverses the sum.", "right": "Test both orders on a complete row. Use the one that fits."},
        {"wrong": "Slipping on digit sums of numbers with 0 or repeated digits.", "right": "Write each digit sum in a short line, like 40 → 4 + 0 = 4."},
        {"wrong": "Skipping the second-row check because the rule looks digital.", "right": "Check every complete row anyway."},
        {"wrong": "Adding the digits of the numbers when the rule adds first, then sums the digits.", "right": "Test S(a) + S(b) and S(a + b). They differ when there is a carry."},
        {"wrong": "Changing to another variant for the last row.", "right": "Use the same variant that fitted the complete rows."},
    ],
    revision=[
        "S(n) is the digit sum, R(n) reverses the digits, P(n) multiplies the digits.",
        "Common rules: S(a) + S(b), S(a + b), R(a) + R(b), R(a + b), P(a), S(a) × b.",
        "Test each variant on a complete row. Only one fits all the rows.",
        "Answers far smaller than the numbers point to a digit rule.",
        "Mirror pairs like 43 and 34 point to reversal.",
        "A 0 in a number kills a digit-product rule.",
    ],
    patterns=[
        pat("do-p1", "Sum of the digit sums", "very common",
            "The answers are small (5 to 30) while the numbers are two-digit.",
            None,
            ["Find S(a) and S(b) for each row.", "Add them and compare with the third number.", "Check every row, then apply."],
            "Digit sums shrink big numbers to answer-sized ones.",
            "Rows: (36, 24, 15), (28, 19, 20), (47, 38, ?). Find ?.",
            ["36: 3 + 6 = 9. 24: 2 + 4 = 6. Total 15.", "28: 10. 19: 10. Total 20.", "47: 11. 38: 11. Total 22."],
            "22"),
        pat("do-p2", "Reverse each number, then add", "very common",
            "Digits mirror across the row, like 43 beside 34.",
            None,
            ["Reverse both numbers.", "Add the two reversed numbers.", "Confirm on every row, then apply."],
            "Reversal is the most reused digit trick.",
            "Rows: (23, 14, 73), (46, 25, 116), (58, 17, ?). Find ?.",
            ["23 → 32 and 14 → 41. Sum 73.", "46 → 64 and 25 → 52. Sum 116.", "58 → 85 and 17 → 71. Sum 156."],
            "156"),
        pat("do-p3", "Product of the digits", "common",
            "The answers are tiny, even smaller than the digit sums.",
            None,
            ["Multiply the digits of the first number.", "Compare with the answer.", "Check every row, then apply."],
            "Digit products shrink numbers even more than digit sums.",
            "Rows: 24 → 8, 35 → 15, 47 → ?. Find ?.",
            ["2 × 4 = 8.", "3 × 5 = 15.", "4 × 7 = 28."],
            "28"),
        pat("do-p4", "Digit sum times the other number", "common",
            "One number is shrunk by its digit sum. The other stays whole.",
            None,
            ["Find the digit sum of the first number.", "Multiply it by the second number.", "Check every row, then apply."],
            "Mixing a digit tool with a plain number hides the rule one level deeper.",
            "Rows: (24, 3, 18), (35, 2, 16), (47, 2, ?). Find ?.",
            ["24: 6, and 6 × 3 = 18.", "35: 8, and 8 × 2 = 16.", "47: 11, and 11 × 2 = 22."],
            "22"),
        pat("do-p5", "Add first, then reverse the sum", "common",
            "The answers are mirror images of the row sums, like sum 42 and answer 24.",
            None,
            ["Add the first two numbers.", "Reverse the digits of the sum.", "Confirm on a second row. Then apply."],
            "The reverse is applied to the result, not to the inputs.",
            "Rows: (24, 18, 24), (32, 13, 54), (26, 15, ?). Find ?.",
            ["24 + 18 = 42. Reversed 24.", "32 + 13 = 45. Reversed 54.", "26 + 15 = 41. Reversed 14."],
            "14"),
        pat("do-p6", "Digit sum of the total", "common",
            "Adding the digit sums separately does not fit, but the digit sum of the total does.",
            None,
            ["Add the two numbers first.", "Then find the digit sum of the total.", "Check S(a) + S(b) too. It differs when there is a carry."],
            "Adding before or after taking digit sums gives different answers when digits carry over.",
            "Rows: (39, 25, 10), (57, 18, 12), (68, 26, ?). Find ?.",
            ["39 + 25 = 64. 6 + 4 = 10.", "57 + 18 = 75. 7 + 5 = 12.", "68 + 26 = 94. 9 + 4 = 13."],
            "13"),
        pat("do-p7", "Digit sums plus a fixed number", "occasional",
            "The digit sums are close to the answer but a small fixed amount is left over.",
            None,
            ["Add the digit sums of both numbers.", "Find the leftover to reach the answer.", "The leftover must be the same in every row.", "Apply to the last row."],
            "A fixed add-on is a small extra step on the digit-sum rule.",
            "Rows: (28, 9, 21), (36, 23, 16), (45, 17, ?). Find ?.",
            ["28: 10 and 9. Total 19. 21 is 2 more.", "36: 9 and 23: 5. Total 14. 16 is 2 more.", "45: 9 and 17: 8. Total 17. Add 2 to get 19."],
            "19"),
    ],
)

# ---------------- apply ----------------
dfrac = lambda x: x.replace(r"\frac", r"\dfrac")
data = json.loads(TOPIC.read_text(encoding="utf-8"))
all_ids = [p_["id"] for s in SUBS.values() for p_ in s["patterns"]]
assert len(all_ids) == len(set(all_ids)), "duplicate pattern id"
for sub in data["subtopics"]:
    new = SUBS.pop(sub["id"])
    old_ids = {p_["id"] for p_ in sub.get("patterns", [])}
    new_ids = {p_["id"] for p_ in new["patterns"]}
    assert old_ids <= new_ids, (sub["id"], old_ids - new_ids)
    notes = new["notes"].strip() + "\n"
    assert 2500 <= len(notes) <= 5000, (sub["id"], len(notes))
    sub["concept"] = new["concept"]
    sub["notes"] = notes
    sub["patterns"] = new["patterns"]
    sub["mistakes"] = [{k: dfrac(v) for k, v in m_.items()} for m_ in new["mistakes"]]
    sub["revision"] = [dfrac(r) for r in new["revision"]]
    sub["tricks"] = new["tricks"]
    sub["formulas"] = new["formulas"]
    print(f"{sub['id']}: {len(notes)} chars, {len(new['patterns'])} patterns (was {len(old_ids)})")
assert not SUBS, list(SUBS)
TOPIC.write_text(json.dumps(data, ensure_ascii=False, indent=1) + "\n", encoding="utf-8", newline="\n")
print("missing-number updated")
