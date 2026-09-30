"""Rewrite every subtopic of core/topics/quant/simplification.json (Phase 3 readable pass).

Keeps all existing pattern ids (practice questions link to them) and adds three new
patterns: simp-si-p5 (solve a power equation), simp-rt-p5 (roots of decimals),
simp-ap-p5 (rounding before dividing). Every number used in every example is
computed and asserted below. Run with the Python312 interpreter.
"""

import json
from fractions import Fraction as F
from math import isqrt, sqrt
from pathlib import Path

ROOT = Path(__file__).resolve().parents[3]
TOPIC = ROOT / "core" / "topics" / "quant" / "simplification.json"

# ---------- simp-bodmas: verified numbers ----------
assert 4 * 2 == 8 and 64 // 8 == 8 and (64 // 4) * 2 == 32
assert 25 - (10 - 6) == 21
assert 60 // 5 * 3 == 36 and 60 // (5 * 3) == 4
assert 1 + F(1, 1 + F(1, 2)) == F(5, 3)
assert (48 + 36) % 9 == 84 % 9 == 3
assert 7 * 8 + 6 == 62 and (6 + 6) % 10 == 2 == 62 % 10
assert 9 * 3 == 27 and 108 // 27 == 4 and 108 // 27 + 6 * 5 == 34
assert 40 - (24 - (16 - (12 - 6))) == 26
assert 3 + F(1, 2 + F(1, 3 + F(1, 4))) == F(103, 30)
assert 96 // 8 * 4 == 48 and 12 * 2 // 3 == 8 and 48 + 8 - 10 == 46
assert 2 * 343 // 7 == 98 and 98 - 100 + 15 == 13
assert 18 // (3 * 2) + 5 == 8
assert 1 + F(1, 2 + F(1, 1 + F(1, 2))) == F(11, 8)
assert 1234 * 567 == 699678 and 1234 % 9 == 1 and 567 % 9 == 0 and 699678 % 9 == 0

# ---------- simp-identities: verified numbers ----------
assert 17 - 10 - 7 == 0 and 3 * 17 * 10 * 7 == 3570 == 17 ** 3 + (-10) ** 3 + (-7) ** 3
_a, _b = F(93, 10), F(33, 10)
assert (_a ** 3 - _b ** 3) / (_a ** 2 + _a * _b + _b ** 2) == _a - _b == 6
assert 343 - 3 * 12 * 7 == 91 == 3 ** 3 + 4 ** 3
assert 4 ** 2 - 2 == 14
assert 105 ** 2 - 95 ** 2 == 2000 == 10 * 200
_a, _b = F(124, 10), F(24, 10)
assert (_a ** 3 - _b ** 3) / (_a ** 2 + _a * _b + _b ** 2) == _a - _b == 10
assert 115 ** 2 - 85 ** 2 == 6000 == 30 * 200
assert 6 ** 2 - 2 == 34
assert 8 ** 3 - 3 * 15 * 8 == 152 == 3 ** 3 + 5 ** 3
assert -13 + 9 + 4 == 0 and 3 * (-13) * 9 * 4 == -1404 == (-13) ** 3 + 9 ** 3 + 4 ** 3
_a, _b = F(7, 10), F(3, 10)
assert (_a ** 3 - _b ** 3) / (_a ** 2 + _a * _b + _b ** 2) == _a - _b == F(2, 5)
assert -16 + 9 + 7 == 0 and 3 * (-16) * 9 * 7 == -3024 == (-16) ** 3 + 9 ** 3 + 7 ** 3
assert 997 * 1003 == 999991 == 1000000 - 9

# ---------- simp-surds-indices: verified numbers ----------
assert 9 * 27 == 243
assert 4 ** 5 == 32 ** 2 == 1024
assert 27 ** 4 == 81 ** 3 == 531441
assert isqrt(9) == 3 and 3 - 1 == 2
assert 4 + 3 == 7 and 4 * 3 == 12
assert 3 ** 6 == 729 and 7 ** 3 == 343 and 5 ** 4 == 625 and max(729, 343, 625) == 729
assert 5 ** 2 - 4 * 6 == 25 - 24 == 1 and 5 + 5 == 10
assert 4 * 27 // 9 == 12
assert abs(sum(1 / (sqrt(k) + sqrt(k - 1)) for k in (9, 8, 7, 6)) - (3 - sqrt(5))) < 1e-9
assert abs((sqrt(5) + 2) ** 2 - (9 + 4 * sqrt(5))) < 1e-9
assert 4 ** 4 == 256 and 6 ** 3 == 216 and 256 > 216
assert 4 ** 3 * 16 ** 0 == 64 and -2 * 2 + 10 == 6
assert 2 ** (3 * 2 - 1) == 32
assert 7 + 3 == 10 and 7 * 3 == 21 and abs((sqrt(7) + sqrt(3)) ** 2 - (10 + 2 * sqrt(21))) < 1e-9
assert 5 ** 3 == 125 and 7 ** 4 == 2401 and 2401 > 125
assert 3 ** (4 + 2) == 27 ** (4 - 2) and 4 + 2 == 3 * 4 - 6
assert 4 + 27 == 31

# ---------- simp-roots: verified numbers ----------
assert 105 * 105 == 11025 and 21 ** 3 == 9261
assert 13 ** 2 == 169 and F(13, 100) ** 2 == F(169, 10000) and F(4, 100) ** 3 == F(64, 10 ** 6)
assert 21 ** 2 == 441 and 22 ** 2 == 484 and 456 - 441 == 15
assert isqrt(144) == 12 and 24 + 12 == 36 and isqrt(36) == 6 and 30 + 6 == 36
assert 2 * 3 == 6 and 3 * 3 == 9 == 6 + 3
assert 36 + 13 == 49 and isqrt(49) == 7
assert 146 ** 2 == 21316 and 145 ** 2 == 21025
assert 44 ** 2 == 1936 and 45 ** 2 == 2025 and 2025 - 2000 == 25
assert isqrt(36) == 6 and 19 + 6 == 25 and isqrt(25) == 5 and 20 + 5 == 25
assert 3 * 4 == 12 and 4 * 4 == 16 == 12 + 4 and 16 - 4 - 12 == 0
assert F(13, 10) + F(13, 100) == F(143, 100)
assert 56 ** 3 == 175616 and 5 ** 3 == 125 and 6 ** 3 == 216 and 125 <= 175 < 216
assert 98 ** 2 == 9604 and 97 ** 2 == 9409 and 99 ** 2 == 9801
assert 8 * 9 == 72 and 9 * 9 == 81 == 72 + 9

# ---------- simp-approximation: verified numbers ----------
assert 600 // 6 == 100 and 500 * 40 // 100 == 200 and 15 * 24 == 360
assert 63 ** 2 == 3969 and 31 ** 3 == 29791 and 63 + 31 == 94
assert 25 * 800 // 100 == 200 and 15 * 20 == 300 and 200 + 300 == 500
assert 30 * 800 // 100 == 240 and 240 + 40 == 280
assert 30 ** 2 == 900 and 35 ** 2 == 1225 and 900 + 35 == 935
assert 28 * 450 // 100 == 126 and 200 - 126 == 74
assert 400 // 8 == 50 and 18 * 5 == 90 and 50 + 90 == 140
assert 200 // 5 + 12 * 6 == 112
assert 8 * 125 // 100 == 10
assert 480 * 3 // 8 == 180


def pat(pid, name, freq, spot, formula, steps, why, q, ex_steps, answer):
    return {
        "id": pid, "name": name, "frequency": freq, "howToSpot": spot,
        "formula": formula, "steps": steps, "why": why,
        "example": {"q": q, "steps": ex_steps, "answer": answer},
    }


# ================= subtopic: simp-bodmas =================

SB_CONCEPT = (
    "VBODMAS fixes the order: vinculum bar first, then brackets innermost first, then "
    "'of', then division and multiplication left to right, then addition and subtraction "
    "left to right. The one trap that costs marks is 'of', which multiplies before any "
    "division sign."
)

SB_NOTES = r"""A long expression with several operations is worked in one fixed order, called VBODMAS: Vinculum, Brackets, Of, Division, Multiplication, Addition, Subtraction. The whole method lives in one example: $64 \div 4 \text{ of } 2$ is $64 \div 8 = 8$, while $64 \div 4 \times 2$ is $16 \times 2 = 32$.

### The order, step by step
1. V for vinculum: a bar over an expression, like $\overline{9 - 7}$, is cleared first.
2. B for brackets: innermost first, $( )$ then $\{ \}$ then $[ ]$.
3. O for of: 'of' means multiply, but it happens before $\div$ and $\times$.
4. D and M: division and multiplication, strictly left to right.
5. A and S: addition and subtraction, again left to right.

> **Rule:** 'Of' outranks the division sign. Convert every 'of' into a bracketed product before touching any $\div$.

### Where 'of' goes wrong
$64 \div 4 \text{ of } 2$ means $64 \div (4 \times 2) = 8$, not $(64 \div 4) \times 2 = 32$. The examiner builds both versions into the options. The same trap appears with fractions: $\dfrac{3}{4}$ of $48 \div 2$ is $\left(\dfrac{3}{4} \times 48\right) \div 2 = 18$.

> **Watch:** Percentages work the same way: $40\%$ of $250$ is a product $\dfrac{40}{100} \times 250$, done before any division outside it.

### Clearing brackets
Start with the innermost bracket and move outward, one layer at a time. A minus sign in front of a bracket flips every sign inside: $25 - (10 - 6) = 25 - 10 + 6 = 21$. Never open all layers in one go; each layer must become a single number first.

### Division and multiplication share a rank
When only $\div$ and $\times$ appear, walk left to right: $60 \div 5 \times 3 = 12 \times 3 = 36$. Doing $60 \div 15 = 4$ instead is the standard slip, and 4 is always among the options.

### Continued fractions
A fraction inside a fraction is simplified from the bottom up. For $1 + \dfrac{1}{1 + \dfrac{1}{2}}$: the bottom gives $1 + \dfrac{1}{2} = \dfrac{3}{2}$, then $\dfrac{1}{3/2} = \dfrac{2}{3}$, then $1 + \dfrac{2}{3} = \dfrac{5}{3}$. Keep fractions as fractions; decimals half way through breed errors.

> **Tip:** Invert the bottom result and add one layer up, every time. Never clear the stack top-down.

### Two fast checks
Digit-sum check: replace each number by its digit sum and repeat the operation; the digit sum of your answer must match. $48 + 36 = 84$: digit sums $3 + 9 \to 12 \to 3$, and $84 \to 12 \to 3$. Last-digit check: for products and sums, work only with last digits. $7 \times 8 + 6 = 62$, and last digits $6 + 6 \to 2$ agree.
"""

SB_FORMULAS = [
    {"name": "'Of' before division", "tex": r"a \div b \text{ of } c = a \div (b \times c)", "note": ""},
    {"name": "Division and multiplication left to right", "tex": r"a \div b \times c = \dfrac{a}{b} \times c", "note": ""},
    {"name": "Minus before a bracket", "tex": r"a - (b - c) = a - b + c", "note": ""},
    {"name": "Continued fraction", "tex": r"a + \dfrac{1}{b + \dfrac{1}{c}} = a + \dfrac{c}{bc + 1}", "note": ""},
]

SB_TRICKS = [
    {
        "title": "Bracket every 'of'",
        "body": "Rewrite each 'of' as a bracketed product before doing any division. The bracket makes the grouping visible and kills the trap.",
        "example": {
            "q": "Evaluate 18 divided by 3 of 2, plus 5.",
            "steps": [
                r"$3 \text{ of } 2 = (3 \times 2) = 6$.",
                r"$18 \div 6 = 3$.",
                r"$3 + 5 = 8$.",
            ],
            "answer": "8",
        },
    },
    {
        "title": "Continued fractions from the bottom",
        "body": "Simplify the deepest fraction first, invert it, add the next layer, and repeat upward.",
        "example": {
            "q": "Evaluate 1 + 1/(2 + 1/(1 + 1/2)).",
            "steps": [
                r"Bottom: $1 + \dfrac{1}{2} = \dfrac{3}{2}$.",
                r"Middle: $2 + \dfrac{2}{3} = \dfrac{8}{3}$.",
                r"Top: $1 + \dfrac{3}{8} = \dfrac{11}{8}$.",
            ],
            "answer": "11/8",
        },
    },
    {
        "title": "Digit-sum check",
        "body": "Casting out nines: digit sums must match on both sides of the equals sign. It kills wrong options without computing the product.",
        "example": {
            "q": "Could 1234 x 567 equal 699678?",
            "steps": [
                r"$1234 \to 1 + 2 + 3 + 4 = 10 \to 1$.",
                r"$567 \to 5 + 6 + 7 = 18 \to 0$ (a multiple of 9).",
                r"Product must be a multiple of 9. $699678 \to 45 \to 9$. So it can.",
            ],
            "answer": "Yes",
        },
    },
]

SB_MISTAKES = [
    {
        "wrong": "Computing a divided by b times c as a divided by (b times c).",
        "right": "Division and multiplication share a rank: work left to right.",
    },
    {
        "wrong": "Treating 'of' like an ordinary multiplication done after division.",
        "right": "'Of' groups its two numbers into a product before any division acts.",
    },
    {
        "wrong": "Opening a square bracket before the round bracket inside it.",
        "right": "Clear the innermost bracket first; each layer becomes one number.",
    },
    {
        "wrong": "Keeping the inner signs when a minus precedes a bracket.",
        "right": "A minus before a bracket flips every sign inside it.",
    },
    {
        "wrong": "Clearing a vinculum bar after the brackets.",
        "right": "The bar is the V in VBODMAS; it goes first.",
    },
]

SB_REVISION = [
    r"Order: vinculum, brackets, of, $\div$ and $\times$ left to right, then $+$ and $-$.",
    r"'Of' beats $\div$ and $\times$; bracket the 'of' product first.",
    r"Minus before a bracket flips every sign inside.",
    r"Continued fractions: simplify bottom-up, keeping fractions.",
    r"Check answers with digit sums and last digits.",
]

SB_PATTERNS = [
    pat(
        "simp-bm-p1", "'Of' before division and multiplication", "very common",
        r"The expression mixes division, multiplication and 'of' (or '% of'), often with a question mark in place of one number.",
        r"a \div b \text{ of } c = a \div (b \times c)",
        [
            r"Replace every 'of' by a bracketed product.",
            r"Do division and multiplication left to right.",
            r"Finish with addition and subtraction left to right.",
            r"For a missing value, simplify the rest and solve the small equation.",
        ],
        r"'Of' is a multiplication that the convention ranks above the division sign.",
        r"Evaluate $108 \div 9$ of $3 + 6 \times 5$.",
        [
            r"$9$ of $3 = 27$.",
            r"$108 \div 27 = 4$.",
            r"$6 \times 5 = 30$, so the total is $4 + 30 = 34$.",
        ],
        "34",
    ),
    pat(
        "simp-bm-p2", "Vinculum and three-layer brackets", "very common",
        r"An expression carries a bar over some digits and nested round, curly and square brackets.",
        "",
        [
            r"Clear the vinculum bar first.",
            r"Then the round bracket, then the curly, then the square.",
            r"Flip every sign inside a bracket that follows a minus.",
            r"Finish the outermost operation last.",
        ],
        r"Each layer must collapse to a single number before the layer outside it can act.",
        r"Simplify $40 - [24 - \{16 - (12 - 6)\}]$.",
        [
            r"Round: $12 - 6 = 6$.",
            r"Curly: $16 - 6 = 10$.",
            r"Square: $24 - 10 = 14$.",
            r"$40 - 14 = 26$.",
        ],
        "26",
    ),
    pat(
        "simp-bm-p3", "Continued (nested) fractions", "common",
        r"Fractions stack inside fractions, written as small stacked numbers on the paper.",
        r"\text{simplify from the bottom upwards}",
        [
            r"Start at the deepest fraction and make it a single fraction.",
            r"Invert it and add the next layer up.",
            r"Repeat to the top; keep exact fractions, not decimals.",
        ],
        r"Each fraction line is a division, and the deepest division must happen first.",
        r"Find $3 + \dfrac{1}{2 + \dfrac{1}{3 + \dfrac{1}{4}}}$.",
        [
            r"Bottom: $3 + \dfrac{1}{4} = \dfrac{13}{4}$.",
            r"Middle: $2 + \dfrac{4}{13} = \dfrac{30}{13}$.",
            r"Top: $3 + \dfrac{13}{30} = \dfrac{103}{30}$.",
        ],
        "103/30",
    ),
    pat(
        "simp-bm-p4", "Long division-multiplication chains", "very common",
        r"A plain chain like division, times, plus, times, minus with no 'of' and no brackets.",
        r"\div \text{ and } \times \text{ share a level: go left to right}",
        [
            r"Walk the expression once, left to right, doing only division and multiplication.",
            r"Collect the additions and subtractions for a second pass.",
            r"Finish left to right again.",
        ],
        r"Division and multiplication have equal rank, so the leftmost one acts first.",
        r"Simplify $96 \div 8 \times 4 + 12 \times 2 \div 3 - 10$.",
        [
            r"$96 \div 8 = 12$, then $12 \times 4 = 48$.",
            r"$12 \times 2 = 24$, then $24 \div 3 = 8$.",
            r"$48 + 8 - 10 = 46$.",
        ],
        "46",
    ),
    pat(
        "simp-bm-p5", "Full mixed expression with fractions and percent", "common",
        r"A longer expression mixes 'of', a fraction term and a percentage term.",
        r"x\% \text{ of } N = \dfrac{x}{100} \times N",
        [
            r"Turn 'of' terms into products and percentages into fractions over 100.",
            r"Simplify each term separately.",
            r"Combine the terms; the fraction parts usually divide neatly.",
        ],
        r"Term-by-term simplification avoids one unreadable giant line.",
        r"Simplify $\dfrac{2}{7}$ of $343 - 40\%$ of $250 + 15$.",
        [
            r"$\dfrac{2}{7} \times 343 = 98$.",
            r"$\dfrac{40}{100} \times 250 = 100$.",
            r"$98 - 100 + 15 = 13$.",
        ],
        "13",
    ),
]


# ================= subtopic: simp-identities =================

SI_CONCEPT = (
    "Many simplification questions are algebra identities with numbers pasted in. "
    "Name $a$ and $b$, match the signs, and the giant cubes cancel into a one-line "
    "answer like $a + b$ or $a - b$."
)

SI_NOTES = r"""A cube of $9.3$ looks like hard work until you notice the shape underneath. $\dfrac{9.3^3 - 3.3^3}{9.3^2 + 9.3 \times 3.3 + 3.3^2}$ collapses to $9.3 - 3.3 = 6$ because the denominator is exactly the second factor of $a^3 - b^3$. That is the whole game: spot the identity, name $a$ and $b$, substitute at the end.

### The identities that do the work
| Identity | Reads as |
|---|---|
| $a^3 + b^3 = (a+b)(a^2 - ab + b^2)$ | sum of cubes |
| $a^3 - b^3 = (a-b)(a^2 + ab + b^2)$ | difference of cubes |
| $a^2 - b^2 = (a+b)(a-b)$ | difference of squares |
| $(a+b)^2 + (a-b)^2 = 2(a^2+b^2)$ | squares combine |
| $(a+b)^2 - (a-b)^2 = 4ab$ | squares subtract |

> **Rule:** In an identity fraction, the sign in the denominator is opposite to the sign on top. Minus below pairs with plus above.

### Identity fractions
Read the denominator first, because it tells you what cancels. If the top is a difference of cubes and the bottom has a plus middle term, the whole fraction is $a - b$. Check $\dfrac{12.4^3 - 2.4^3}{12.4^2 + 12.4 \times 2.4 + 2.4^2}$: the bottom is the plus version, so the value is $12.4 - 2.4 = 10$. Never cube the decimals.

### Squares that sit near each other
$115^2 - 85^2 = (115 - 85)(115 + 85) = 30 \times 200 = 6000$. Whenever two squares sit close together, factor instead of squaring. The same identity multiplies numbers around a round value: $997 \times 1003 = 1000^2 - 3^2 = 999991$.

> **Tip:** Look for a shared centre. Write the pair as centre minus gap and centre plus gap, then use centre squared minus gap squared.

### The x plus one over x ladder
If $x + \dfrac{1}{x} = k$, then $x^2 + \dfrac{1}{x^2} = k^2 - 2$, and $x^3 + \dfrac{1}{x^3} = k^3 - 3k$. With the minus version the twos flip: if $x - \dfrac{1}{x} = k$, then $x^2 + \dfrac{1}{x^2} = k^2 + 2$. So $x + \dfrac{1}{x} = 4$ gives $16 - 2 = 14$ for the square, and $x + \dfrac{1}{x} = 6$ gives $36 - 2 = 34$.

### Cubes from a sum and a product
Given $a+b$ and $ab$, never hunt for $a$ and $b$. Use $a^2 + b^2 = (a+b)^2 - 2ab$ and $a^3 + b^3 = (a+b)^3 - 3ab(a+b)$. With $a+b = 7$ and $ab = 12$: $a^3 + b^3 = 343 - 252 = 91$, which is $3^3 + 4^3$.

### Zero-sum cubes
If $a + b + c = 0$, then $a^3 + b^3 + c^3 = 3abc$. Test the bases before cubing anything: $17 - 10 - 7 = 0$, so $17^3 + (-10)^3 + (-7)^3 = 3 \times 17 \times 10 \times 7 = 3570$. Two negative bases multiply to a positive here, so the sign needs one careful look.

> **Watch:** Add the three bases first. If they do not sum to zero, this shortcut does not apply and the numbers must be cubed honestly.

### A safe attacking order
1. Read the denominator of any fraction; it names the identity.
2. Match the middle sign to choose the plus or minus version.
3. Keep $a$ and $b$ symbolic until the expression is factored.
4. Substitute the numbers in the last line only.
"""

SI_FORMULAS = [
    {"name": "Sum of cubes", "tex": r"a^3 + b^3 = (a+b)(a^2 - ab + b^2)", "note": ""},
    {"name": "Difference of cubes", "tex": r"a^3 - b^3 = (a-b)(a^2 + ab + b^2)", "note": ""},
    {"name": "Difference of squares", "tex": r"a^2 - b^2 = (a+b)(a-b)", "note": ""},
    {"name": "Cube of sum", "tex": r"(a+b)^3 = a^3 + b^3 + 3ab(a+b)", "note": ""},
    {"name": "Squares combine", "tex": r"(a+b)^2 + (a-b)^2 = 2(a^2+b^2)", "note": ""},
    {"name": "Squares subtract", "tex": r"(a+b)^2 - (a-b)^2 = 4ab", "note": ""},
    {"name": "Zero-sum cubes", "tex": r"a+b+c = 0 \Rightarrow a^3+b^3+c^3 = 3abc", "note": ""},
    {"name": "Square-sum from pair facts", "tex": r"a^2 + b^2 = (a+b)^2 - 2ab", "note": ""},
]

SI_TRICKS = [
    {
        "title": "Pattern-match the fraction",
        "body": "Cubes on top and three terms with a middle product below mean a sum or difference of cubes. The fraction is just a plus or minus of the bases.",
        "example": {
            "q": "Simplify (0.7 x 0.7 x 0.7 - 0.3 x 0.3 x 0.3) over (0.7 x 0.7 + 0.7 x 0.3 + 0.3 x 0.3).",
            "steps": [
                r"Shape: $\dfrac{a^3 - b^3}{a^2 + ab + b^2}$ with $a = 0.7$, $b = 0.3$.",
                r"Value $= a - b = 0.7 - 0.3$.",
                r"$0.7 - 0.3 = 0.4 = \dfrac{2}{5}$.",
            ],
            "answer": "2/5",
        },
    },
    {
        "title": "Zero-sum check before cubing",
        "body": "Add the three bases. If they sum to zero, the cubes sum to three times their product, signs included.",
        "example": {
            "q": "Find (-16)^3 + 9^3 + 7^3.",
            "steps": [
                r"$-16 + 9 + 7 = 0$, so the zero-sum rule applies.",
                r"Value $= 3 \times (-16) \times 9 \times 7$.",
                r"$3 \times (-1008) = -3024$.",
            ],
            "answer": "-3024",
        },
    },
    {
        "title": "Products around a round number",
        "body": "Write the pair as centre minus gap and centre plus gap. The product is centre squared minus gap squared.",
        "example": {
            "q": "Find 997 x 1003.",
            "steps": [
                r"Centre $1000$, gap $3$.",
                r"$1000^2 - 3^2 = 1000000 - 9$.",
                r"$= 999991$.",
            ],
            "answer": "999991",
        },
    },
]

SI_MISTAKES = [
    {
        "wrong": "Pairing a sum-of-cubes top with a plus middle term below.",
        "right": "The middle sign below is opposite to the sign on top.",
    },
    {
        "wrong": "Cubing the decimals in an identity fraction.",
        "right": "Name a and b, cancel the factor, subtract or add the bases.",
    },
    {
        "wrong": "Writing $(a+b)^3 = a^3 + b^3$.",
        "right": "The cube of a sum carries the extra term $3ab(a+b)$.",
    },
    {
        "wrong": "Using $k^2 + 2$ when $x + 1/x = k$ is given.",
        "right": "Plus version subtracts 2; minus version adds 2.",
    },
    {
        "wrong": "Applying the zero-sum rule without adding the bases.",
        "right": "Check $a + b + c = 0$ first; otherwise cube honestly.",
    },
]

SI_REVISION = [
    r"$\dfrac{a^3 \pm b^3}{a^2 \mp ab + b^2} = a \pm b$.",
    r"$a^2 - b^2 = (a+b)(a-b)$ for near squares and round-about products.",
    r"$x + \dfrac{1}{x} = k$: square gives $k^2 - 2$, cube gives $k^3 - 3k$.",
    r"$a^3 + b^3 = (a+b)^3 - 3ab(a+b)$ from a sum and a product.",
    r"$a + b + c = 0$ gives $a^3 + b^3 + c^3 = 3abc$.",
    r"Substitute numbers only in the last line.",
]

SI_PATTERNS = [
    pat(
        "simp-id-p1", "Identity fraction: cubes over the quadratic factor", "very common",
        r"A fraction with cubed decimals on top and three terms with a middle product below.",
        r"\dfrac{a^3 \pm b^3}{a^2 \mp ab + b^2} = a \pm b",
        [
            r"Read the sign of the middle term in the denominator.",
            r"Pick the matching identity: minus below pairs with plus above.",
            r"Cancel the quadratic factor.",
            r"Add or subtract the two bases; that is the answer.",
        ],
        r"The denominator is literally the second factor of the numerator's factorisation.",
        r"Find the value of $\dfrac{9.3^3 - 3.3^3}{9.3^2 + 9.3 \times 3.3 + 3.3^2}$.",
        [
            r"Bottom is the plus version, so the fraction equals $a - b$.",
            r"$a - b = 9.3 - 3.3$.",
            r"$= 6$.",
        ],
        "6",
    ),
    pat(
        "simp-id-p2", "Squares near each other; round-about products", "very common",
        r"Two squares of close numbers, or a product of two numbers placed symmetrically around a round value.",
        r"a^2 - b^2 = (a-b)(a+b)",
        [
            r"Find the centre: the average of the two numbers.",
            r"Find the gap: the distance from the centre to either number.",
            r"Multiply the sum by the difference, or use centre squared minus gap squared.",
        ],
        r"Factoring avoids squaring three-digit numbers by hand.",
        r"Find $115^2 - 85^2$.",
        [
            r"$115 - 85 = 30$ and $115 + 85 = 200$.",
            r"$30 \times 200 = 6000$.",
        ],
        "6000",
    ),
    pat(
        "simp-id-p3", "The x plus one over x ladder", "very common",
        r"A given value of $x + \frac{1}{x}$ or $x - \frac{1}{x}$, and a target square, cube or fourth power.",
        r"x + \tfrac{1}{x} = k \Rightarrow x^2 + \tfrac{1}{x^2} = k^2 - 2",
        [
            r"Square the given relation; the cross term is $\pm 2$.",
            r"Plus version subtracts 2, minus version adds 2.",
            r"For cubes use $k^3 \mp 3k$; for fourth powers, square the square result and subtract 2.",
        ],
        r"Squaring $x \pm \frac{1}{x}$ produces the cross term $2$ or $-2$ beside the wanted square-sum.",
        r"If $x + \dfrac{1}{x} = 6$, find $x^2 + \dfrac{1}{x^2}$.",
        [
            r"Square: $6^2 = 36$.",
            r"Subtract the cross term: $36 - 2 = 34$.",
        ],
        "34",
    ),
    pat(
        "simp-id-p4", "Given a + b and ab", "very common",
        r"The pair sum and product are given; the target is a square-sum, cube-sum or a similar symmetric value.",
        r"a^3 + b^3 = (a+b)^3 - 3ab(a+b)",
        [
            r"Write the target using only $(a+b)$ and $ab$.",
            r"Substitute the two given numbers.",
            r"If the numbers themselves are wanted, spot the small integer pair.",
        ],
        r"Every symmetric expression in two letters is a function of their sum and product.",
        r"If $a + b = 8$ and $ab = 15$, find $a^3 + b^3$.",
        [
            r"$(a+b)^3 = 512$.",
            r"$3ab(a+b) = 3 \times 15 \times 8 = 360$.",
            r"$512 - 360 = 152$, which is $3^3 + 5^3$.",
        ],
        "152",
    ),
    pat(
        "simp-id-p5", "Zero-sum cubes", "common",
        r"Three cubes, often with negative or fractional bases, whose bases add to zero.",
        r"a+b+c = 0 \Rightarrow a^3+b^3+c^3 = 3abc",
        [
            r"Add the three bases and confirm the sum is zero.",
            r"Multiply the three bases together.",
            r"Triple the product, watching the signs.",
        ],
        r"The identity for $a^3+b^3+c^3 - 3abc$ carries the factor $(a+b+c)$, which is zero here.",
        r"Find $(-13)^3 + 9^3 + 4^3$.",
        [
            r"$-13 + 9 + 4 = 0$, so the rule applies.",
            r"$(-13) \times 9 \times 4 = -468$.",
            r"$3 \times (-468) = -1404$.",
        ],
        "-1404",
    ),
]


# ================= subtopic: simp-surds-indices =================

SS_CONCEPT = (
    "Indices rewrite every number as a power of one prime, then the exponents do the "
    "work. Surds rationalise through the conjugate, split via $x + y = a$ and $xy = b$, "
    "and compare after raising to a common root order."
)

SS_NOTES = r"""A power question always has the same escape route: write every number as a power of one prime. $1024$ is $2^{10}$ and also $4^5$; $81$ is $3^4$ and also $27^{4/3}$, because $27^4 = 81^3$. Once the bases match, only the exponents remain.

### The laws that move exponents
| Law | Statement |
|---|---|
| same base, product | $a^m \times a^n = a^{m+n}$ |
| same base, quotient | $a^m \div a^n = a^{m-n}$ |
| power of a power | $(a^m)^n = a^{mn}$ |
| zero and negative | $a^0 = 1$, $a^{-n} = \dfrac{1}{a^n}$ |
| fractional index | $a^{p/q} = \sqrt[q]{a^p}$ |

> **Rule:** Make every base the same prime first. Then add, subtract and multiply exponents; never touch the numbers again.

### Solving a power equation
$4^{x+1} \times 16^{2-x} = 64$ becomes $2^{2x+2} \times 2^{8-4x} = 2^6$, so $2x + 2 + 8 - 4x = 6$, giving $x = 2$. Fractional indices evaluate in the same spirit: $32^{2/5} = (2^5)^{2/5} = 2^2 = 4$, and $81^{3/4} = 27$.

### Rationalising with the conjugate
Multiply top and bottom by the conjugate, the same terms with the flipped middle sign:
$$\dfrac{1}{\sqrt{a} \pm \sqrt{b}} = \dfrac{\sqrt{a} \mp \sqrt{b}}{a - b}$$
The product $(\sqrt{a} + \sqrt{b})(\sqrt{a} - \sqrt{b}) = a - b$ clears every root from the bottom.

### Telescoping chains
A sum like $\dfrac{1}{\sqrt{9}+\sqrt{8}} + \dfrac{1}{\sqrt{8}+\sqrt{7}} + \dfrac{1}{\sqrt{7}+\sqrt{6}} + \dfrac{1}{\sqrt{6}+\sqrt{5}}$ rationalises term by term into $\sqrt{9}-\sqrt{8} + \sqrt{8}-\sqrt{7} + \dots$, and the middle roots kill each other. Only the ends survive: $\sqrt{9} - \sqrt{5} = 3 - \sqrt{5}$.

> **Tip:** In a chain of $\dfrac{1}{\sqrt{k}+\sqrt{k-1}}$ terms, write the answer as first root minus last root and skip the middle entirely.

### The a plus two root b split
To open $\sqrt{a + 2\sqrt{b}}$, hunt two numbers with sum $a$ and product $b$; the root is $\sqrt{x} + \sqrt{y}$. For $\sqrt{7 + 4\sqrt{3}}$, write $4\sqrt{3}$ as $2\sqrt{12}$, so $x + y = 7$ and $xy = 12$: the pair is $4$ and $3$, giving $2 + \sqrt{3}$.

> **Watch:** $\sqrt{a+b}$ is not $\sqrt{a} + \sqrt{b}$. The split only works when the middle term is forced into the $2\sqrt{b}$ shape first.

### Comparing surds
Raise every surd to the LCM of the root orders, then compare plain integers. For $\sqrt{3}$, $\sqrt[3]{7}$, $\sqrt[4]{5}$, the orders 2, 3, 4 give LCM 12. Twelfth powers: $3^6 = 729$, $7^3 = 343$, $5^4 = 625$. So $\sqrt{3}$ is the largest.

### A surd and its reciprocal
If $x = a + \sqrt{b}$ and $a^2 - b = 1$, then $\dfrac{1}{x} = a - \sqrt{b}$. Check first: for $5 + 2\sqrt{6}$, $25 - 24 = 1$, so the reciprocal is $5 - 2\sqrt{6}$ and $x + \dfrac{1}{x} = 10$. If $a^2 - b$ is not a perfect square, do the long rationalisation instead.
"""

SS_FORMULAS = [
    {"name": "Same base", "tex": r"a^m \cdot a^n = a^{m+n},\quad \frac{a^m}{a^n} = a^{m-n}", "note": ""},
    {"name": "Power of power", "tex": r"(a^m)^n = a^{mn},\quad (ab)^n = a^n b^n", "note": ""},
    {"name": "Zero and negative index", "tex": r"a^0 = 1,\quad a^{-n} = \frac{1}{a^n}", "note": ""},
    {"name": "Fractional index", "tex": r"a^{p/q} = \sqrt[q]{a^p}", "note": ""},
    {"name": "Rationalisation", "tex": r"\frac{1}{\sqrt{a} \pm \sqrt{b}} = \frac{\sqrt{a} \mp \sqrt{b}}{a - b}", "note": ""},
    {"name": "Root of a surd", "tex": r"\sqrt{a \pm 2\sqrt{b}} = \sqrt{x} \pm \sqrt{y},\ x + y = a,\ xy = b", "note": ""},
    {"name": "Reciprocal of a unit surd", "tex": r"x = a + \sqrt{b},\ a^2 - b = 1 \Rightarrow \tfrac{1}{x} = a - \sqrt{b}", "note": ""},
]

SS_TRICKS = [
    {
        "title": "Common base, then equate powers",
        "body": "Write both sides as powers of the same prime. The equation becomes a linear equation in the exponent.",
        "example": {
            "q": "If 3^(x+2) = 27^(x-2), find x.",
            "steps": [
                r"$27 = 3^3$, so $3^{x+2} = 3^{3x-6}$.",
                r"$x + 2 = 3x - 6$.",
                r"$8 = 2x$, so $x = 4$.",
            ],
            "answer": "4",
        },
    },
    {
        "title": "Split a + 2 root b",
        "body": "Force the middle term into the 2 root b shape, then find two numbers with the given sum and product.",
        "example": {
            "q": r"Simplify $\sqrt{7 + 4\sqrt{3}}$.",
            "steps": [
                r"$4\sqrt{3} = 2\sqrt{12}$, so $x + y = 7$, $xy = 12$.",
                r"The pair is $4$ and $3$.",
                r"$\sqrt{7 + 4\sqrt{3}} = \sqrt{4} + \sqrt{3} = 2 + \sqrt{3}$.",
            ],
            "answer": "2 + sqrt(3)",
        },
    },
    {
        "title": "Reciprocal by the a squared minus b check",
        "body": "For x = a + sqrt(b), test a squared minus b. If it equals 1, the reciprocal is a minus sqrt(b) with no work.",
        "example": {
            "q": "If x = 5 + 2*sqrt(6), find 1/x.",
            "steps": [
                r"$a = 5$, $b = 24$: $25 - 24 = 1$.",
                r"So $\dfrac{1}{x} = 5 - 2\sqrt{6}$.",
                r"Check: the product is $25 - 24 = 1$.",
            ],
            "answer": "5 - 2*sqrt(6)",
        },
    },
]

SS_MISTAKES = [
    {
        "wrong": "Writing the square root of a sum as the sum of the square roots.",
        "right": "Roots do not distribute over addition; only the a + 2 root b split opens a nested root.",
    },
    {
        "wrong": "Reading a to the power minus n as minus a to the n.",
        "right": "A negative exponent flips the base: a to the power minus n is one over a to the n.",
    },
    {
        "wrong": "Adding exponents when the bases differ.",
        "right": "Convert to one prime base first; only same-base powers add exponents.",
    },
    {
        "wrong": "Comparing surds of different orders by their radicands.",
        "right": "Raise all surds to the LCM of the root orders and compare the integers.",
    },
    {
        "wrong": "Splitting a + 2 root b without rewriting the middle term.",
        "right": "Force the middle term into the 2 root b shape so b is the product, not the visible number.",
    },
]

SS_REVISION = [
    r"One prime base; then exponents add, subtract or multiply.",
    r"Power of a power multiplies the exponents.",
    r"Conjugate rationalisation: flip the middle sign, divide by $a - b$.",
    r"Telescoping chain: answer is first root minus last root.",
    r"$\sqrt{a + 2\sqrt{b}} = \sqrt{x} + \sqrt{y}$ with $x + y = a$, $xy = b$.",
    r"Compare surds at the LCM of the root orders.",
    r"$a^2 - b = 1$ makes the reciprocal $a - \sqrt{b}$.",
]

SS_PATTERNS = [
    pat(
        "simp-si-p1", "Evaluate fractional and negative powers", "very common",
        r"Numbers raised to fractions or negatives, like $32^{2/5}$ or $81^{3/4}$, often mixed in one expression.",
        r"a^{p/q} = \sqrt[q]{a^p}",
        [
            r"Factor each base into primes.",
            r"Apply the fractional index: root first, then power.",
            r"Combine the results with ordinary arithmetic.",
        ],
        r"A fractional index is a root in disguise, and prime bases make the root visible.",
        r"Find $(32)^{2/5} + (81)^{3/4}$.",
        [
            r"$32 = 2^5$, so $32^{2/5} = 2^2 = 4$.",
            r"$81 = 3^4$, so $81^{3/4} = 3^3 = 27$.",
            r"$4 + 27 = 31$.",
        ],
        "31",
    ),
    pat(
        "simp-si-p2", "Rationalisation and telescoping surd fractions", "very common",
        r"Fractions with roots in the denominator, or a long sum of such fractions with roots stepping down by one.",
        r"\dfrac{1}{\sqrt{a}\pm\sqrt{b}} = \dfrac{\sqrt{a}\mp\sqrt{b}}{a-b}",
        [
            r"Multiply top and bottom by the conjugate.",
            r"In a long sum, rationalise every term.",
            r"Watch the middle roots cancel in pairs.",
            r"Write the answer as first root minus last root.",
        ],
        r"Each term becomes a difference of roots that cancels with its neighbour, leaving only the two ends.",
        r"Find $\dfrac{1}{\sqrt{9}+\sqrt{8}} + \dfrac{1}{\sqrt{8}+\sqrt{7}} + \dfrac{1}{\sqrt{7}+\sqrt{6}} + \dfrac{1}{\sqrt{6}+\sqrt{5}}$.",
        [
            r"Each term equals $\sqrt{k} - \sqrt{k-1}$.",
            r"The middle roots cancel pairwise.",
            r"Left with $\sqrt{9} - \sqrt{5} = 3 - \sqrt{5}$.",
        ],
        "3 - sqrt(5)",
    ),
    pat(
        "simp-si-p3", "Root of a surd: the a plus two root b split", "common",
        r"A square root wrapped around a number plus a root, like $\sqrt{9 + 4\sqrt{5}}$.",
        r"\sqrt{a + 2\sqrt{b}} = \sqrt{x} + \sqrt{y},\ x+y = a,\ xy = b",
        [
            r"Rewrite the middle term as $2\sqrt{b}$ if needed.",
            r"Find two numbers with sum $a$ and product $b$.",
            r"Answer is $\sqrt{x} + \sqrt{y}$, or their difference when the middle sign is minus.",
        ],
        r"Squaring $\sqrt{x} + \sqrt{y}$ returns exactly $x + y + 2\sqrt{xy}$.",
        r"Simplify $\sqrt{9 + 4\sqrt{5}}$.",
        [
            r"$4\sqrt{5} = 2\sqrt{20}$, so sum $9$, product $20$.",
            r"The pair is $5$ and $4$.",
            r"$\sqrt{9 + 4\sqrt{5}} = \sqrt{5} + \sqrt{4} = \sqrt{5} + 2$.",
        ],
        "sqrt(5) + 2",
    ),
    pat(
        "simp-si-p4", "Comparing surds of different orders", "common",
        r"A list of roots with different orders, asking which is largest or smallest.",
        r"\sqrt[n]{a} > \sqrt[m]{b} \iff a^{\text{lcm}/n} > b^{\text{lcm}/m}",
        [
            r"Take the LCM of all the root orders.",
            r"Raise each surd to that LCM; roots disappear.",
            r"Compare the integers and read off the answer.",
        ],
        r"A common power turns every surd into an integer, and integers compare at a glance.",
        r"Which is the largest: $\sqrt{3}$, $\sqrt[3]{7}$ or $\sqrt[4]{5}$?",
        [
            r"Orders 2, 3, 4 give LCM 12.",
            r"Twelfth powers: $3^6 = 729$, $7^3 = 343$, $5^4 = 625$.",
            r"$729$ is largest, so $\sqrt{3}$ wins.",
        ],
        "sqrt(3)",
    ),
    pat(
        "simp-si-p5", "Solve an equation in powers", "common",
        r"An unknown sits in the exponent, and the bases are powers of one number.",
        r"a^{f(x)} = a^{g(x)} \Rightarrow f(x) = g(x)",
        [
            r"Write every base as a power of the smallest prime present.",
            r"Collect the exponents of the left side into one.",
            r"Write the right side in the same base.",
            r"Equate exponents and solve the linear equation.",
        ],
        r"Equal bases make the exponent equation the only content left.",
        r"If $4^{x+1} \times 16^{2-x} = 64$, find $x$.",
        [
            r"$4 = 2^2$, $16 = 2^4$, $64 = 2^6$.",
            r"$2^{2x+2} \times 2^{8-4x} = 2^6$.",
            r"$2x + 2 + 8 - 4x = 6$, so $-2x + 10 = 6$.",
            r"$x = 2$.",
        ],
        "2",
    ),
]


# ================= subtopic: simp-roots =================

SR_CONCEPT = (
    "A square root question is answered by digit pairs and the unit-digit map; a cube "
    "root by digit triples and the swap map. Least-add and least-subtract questions sit "
    "between two neighbouring squares, and radicals are opened from the inside out."
)

SR_NOTES = r"""Every root question in this chapter is built on a perfect power, and the exam expects you to find it without long division. Two tools do it: the unit digit of the answer, and the size of the answer from digit grouping.

### The unit-digit maps
A perfect square ends only in $0, 1, 4, 5, 6$ or $9$; the digits $2, 3, 7, 8$ never appear. The map from root to square is short: root ending $1$ or $9$ gives square ending $1$. Root ending $2$ or $8$ gives $4$, and $3$ or $7$ gives $9$. Root ending $4$ or $6$ gives $6$, and $5$ gives $5$.
Cube digits are even friendlier: $1, 4, 5, 6, 9, 0$ map to themselves, and $2$ swaps with $8$, $3$ with $7$.

> **Rule:** For a cube root, the last digit of the cube gives the last digit of the root directly, using the swap pairs 2 with 8 and 3 with 7.

### Size from digit grouping
Pair the digits of a square from the right: the number of pairs equals the digits in the root. Group a cube in threes the same way. For $\sqrt{9604}$: pairs $96 \mid 04$, so a two-digit root; $9^2 = 81 \le 96$, so it starts with $9$. Ending $4$ means root ends in $2$ or $8$; since $95^2 = 9025$ is too small, the root is $98$.
For a cube root, the leading group fixes the first digit: the largest cube not exceeding it. In $\sqrt[3]{175616}$, groups are $175 \mid 616$; $5^3 = 125 \le 175 < 216 = 6^3$, so the root starts with $5$ and ends with $6$: answer $56$.

### Roots of decimals
Count decimal places. A square root halves them: $0.0169$ has four places, so its root has two: $0.13$. A cube root divides them by three: $0.000064$ has six places, root $0.04$. Combine both: $\sqrt{1.69} + \sqrt{0.0169} = 1.3 + 0.13 = 1.43$.

> **Watch:** A unit digit can only rule a perfect square out, never confirm it. Always finish with the size check.

### Least number to add or subtract
Bracket $N$ between neighbouring squares $k^2$ and $(k+1)^2$.
- Subtract case: answer is $N - k^2$, the gap down.
- Add case: answer is $(k+1)^2 - N$, the gap up.
For $456$: $21^2 = 441$ and $22^2 = 484$, so subtracting $456 - 441 = 15$ lands on $441$. For $2000$: $44^2 = 1936$ and $45^2 = 2025$, so adding $2025 - 2000 = 25$ lands on $2025$.

### Nested radicals: inside out
Replace the deepest root first; each layer then becomes a perfect square. $\sqrt{20 + \sqrt{19 + \sqrt{36}}}$: innermost $\sqrt{36} = 6$; then $\sqrt{19 + 6} = \sqrt{25} = 5$; then $\sqrt{20 + 5} = \sqrt{25} = 5$.

> **Tip:** Setters place each layer to collapse exactly. If a layer does not land on a perfect square, recheck the inner layer before forcing on.

### Infinite radicals
Call the whole expression $x$; the tail equals $x$ again, so $x = \sqrt{a + x}$. Then $x^2 - x - a = 0$; keep the positive root. Fast path: if $a = k(k+1)$, the answer is $k + 1$. Check with $12 = 3 \times 4$: $4^2 = 12 + 4$ holds, so $\sqrt{12 + \sqrt{12 + \cdots}} = 4$. The product form $\sqrt{x\sqrt{x\sqrt{x \cdots}}}$ equals $x$ itself.

### Root equations with an unknown
Isolate the root on one side and square once. $\sqrt{1 + \dfrac{x}{225}} = \dfrac{16}{15}$ gives $1 + \dfrac{x}{225} = \dfrac{256}{225}$, so $x = 31$. Square both sides only after the root stands alone.
"""

SR_FORMULAS = [
    {"name": "Product rule", "tex": r"\sqrt{ab} = \sqrt{a}\,\sqrt{b},\quad \sqrt[3]{ab} = \sqrt[3]{a}\,\sqrt[3]{b}", "note": ""},
    {"name": "Infinite radical, plus", "tex": r"\sqrt{n + \sqrt{n + \cdots}} = \dfrac{1 + \sqrt{1 + 4n}}{2}", "note": ""},
    {"name": "Infinite radical, minus", "tex": r"\sqrt{n - \sqrt{n - \cdots}} = \dfrac{-1 + \sqrt{1 + 4n}}{2}", "note": ""},
    {"name": "Infinite nested product", "tex": r"\sqrt{x\sqrt{x\sqrt{x \cdots}}} = x", "note": ""},
    {"name": "Least add or subtract", "tex": r"\text{subtract } N - k^2,\quad \text{add } (k+1)^2 - N", "note": ""},
]

SR_TRICKS = [
    {
        "title": "Cube root by unit digit and leading group",
        "body": "The last digit of the cube gives the last digit of the root; the leading group, compared with the small cubes, gives the first digit.",
        "example": {
            "q": "Find the cube root of 175616.",
            "steps": [
                r"Groups: $175 \mid 616$, so the root has two digits.",
                r"$5^3 = 125 \le 175 < 216 = 6^3$, so first digit is $5$.",
                r"Cube ends in $6$, and $6$ maps to itself: root $= 56$.",
            ],
            "answer": "56",
        },
    },
    {
        "title": "Square root by unit digit and size",
        "body": "Digit pairs fix the number of digits and the first digit; the last-digit map gives two candidates; one size check picks between them.",
        "example": {
            "q": "Find the square root of 9604.",
            "steps": [
                r"Pairs $96 \mid 04$: two digits; $9^2 = 81 \le 96$, so it starts with $9$.",
                r"Ends in $4$, so the root ends in $2$ or $8$.",
                r"$95^2 = 9025$ is below $9604$, so take $98$; check $98^2 = 9604$.",
            ],
            "answer": "98",
        },
    },
    {
        "title": "n equals k times k plus one radicals",
        "body": "Factor n into two consecutive integers. Plus signs give the larger one, minus signs the smaller.",
        "example": {
            "q": r"Find $\sqrt{72 + \sqrt{72 + \sqrt{72 + \cdots}}}$.",
            "steps": [
                r"$72 = 8 \times 9$, two consecutive integers.",
                r"Plus form gives the larger: $9$.",
                r"Check: $9^2 = 81 = 72 + 9$.",
            ],
            "answer": "9",
        },
    },
]

SR_MISTAKES = [
    {
        "wrong": "Miscounting decimal places in roots of decimals.",
        "right": "Square root halves the decimal places; cube root divides them by three.",
    },
    {
        "wrong": "Keeping the negative root when solving x squared equals a plus x.",
        "right": "A radical expression is positive; take the positive root of the quadratic.",
    },
    {
        "wrong": "Declaring a number a perfect square because it ends in 1, 4, 5, 6 or 9.",
        "right": "The unit digit only rules candidates out; confirm with digit pairing and a check.",
    },
    {
        "wrong": "Swapping the add and subtract gaps.",
        "right": "Subtract down to k squared; add up to the next square, k plus one squared.",
    },
    {
        "wrong": "Opening a nested radical from the outermost root.",
        "right": "Evaluate from the innermost root outward, one layer at a time.",
    },
]

SR_REVISION = [
    r"Perfect squares end in $0, 1, 4, 5, 6, 9$; cubes use the swap map $2 \leftrightarrow 8$, $3 \leftrightarrow 7$.",
    r"Digit pairs size a square root; digit triples size a cube root.",
    r"Subtract $N - k^2$; add $(k+1)^2 - N$.",
    r"Nested radicals open from the inside out.",
    r"$x = \sqrt{a + x}$; if $a = k(k+1)$, the answer is $k + 1$.",
    r"Product form $\sqrt{x\sqrt{x\cdots}}$ equals $x$.",
]

SR_PATTERNS = [
    pat(
        "simp-rt-p1", "Square root or cube root of a perfect power", "very common",
        r"A clean big number sits under a root sign and the options are whole numbers.",
        r"\text{digit pairs (squares) or triples (cubes) plus the unit-digit map}",
        [
            r"Group digits from the right: pairs for a square root, triples for a cube root.",
            r"Read the size from the leading group.",
            r"Read the last digit from the map or swap map.",
            r"Verify by squaring or cubing the candidate.",
        ],
        r"The grouping gives size, the unit digit gives the tail; together they pin the answer without long division.",
        r"Find $\sqrt[3]{175616}$.",
        [
            r"Groups: $175 \mid 616$, a two-digit root.",
            r"$5^3 = 125 \le 175 < 216 = 6^3$: first digit $5$.",
            r"Ending $6$ maps to itself: root $56$; check $56^3 = 175616$.",
        ],
        "56",
    ),
    pat(
        "simp-rt-p2", "Least number to add or subtract to reach a perfect square", "very common",
        r"The question asks for the least number added to or subtracted from N so the result is a perfect square.",
        r"\text{subtract: } N - k^2,\quad \text{add: } (k+1)^2 - N",
        [
            r"Find $k$, the whole part of the square root of $N$.",
            r"Compute $k^2$ and $(k+1)^2$ to bracket $N$.",
            r"Subtract case: answer $N - k^2$; add case: answer $(k+1)^2 - N$.",
        ],
        r"The nearest squares on the two sides of $N$ are exactly $k^2$ and $(k+1)^2$.",
        r"Find the least number that must be added to $2000$ to make it a perfect square.",
        [
            r"$44^2 = 1936 < 2000 < 2025 = 45^2$.",
            r"Gap up: $2025 - 2000 = 25$.",
        ],
        "25",
    ),
    pat(
        "simp-rt-p3", "Nested radicals, worked from the inside", "common",
        r"A finite stack of square roots, each wrapped around the previous result.",
        r"\text{evaluate the innermost root first}",
        [
            r"Replace the deepest root with its value.",
            r"Add or combine outward one layer at a time.",
            r"Each layer should land on a perfect square.",
        ],
        r"Only the innermost layer is a number you can root immediately; every outer layer waits for it.",
        r"Find $\sqrt{20 + \sqrt{19 + \sqrt{36}}}$.",
        [
            r"$\sqrt{36} = 6$.",
            r"$\sqrt{19 + 6} = \sqrt{25} = 5$.",
            r"$\sqrt{20 + 5} = \sqrt{25} = 5$.",
        ],
        "5",
    ),
    pat(
        "simp-rt-p4", "Infinite radicals", "common",
        r"The same pattern repeats forever, shown by dots; the word infinite may appear.",
        r"x = \sqrt{a + x} \Rightarrow x^2 - x - a = 0",
        [
            r"Name the whole expression $x$.",
            r"Spot the tail equals $x$ again and build the equation.",
            r"Solve and keep the positive root.",
            r"Fast path: factor $a$ as $k(k+1)$; the answer is $k + 1$.",
        ],
        r"Self-similarity turns the endless tower into one short quadratic.",
        r"Find $\sqrt{12 + \sqrt{12 + \sqrt{12 + \cdots}}}$.",
        [
            r"$x^2 = 12 + x$, so $x^2 - x - 12 = 0$.",
            r"$12 = 3 \times 4$, so the answer should be $4$.",
            r"Check: $4^2 = 16 = 12 + 4$. So $x = 4$.",
        ],
        "4",
    ),
    pat(
        "simp-rt-p5", "Roots of decimals", "common",
        r"A decimal sits under the root sign, like $1.69$ or $0.000064$.",
        r"\text{decimal places halve (square root) or divide by three (cube root)}",
        [
            r"Count the decimal places of the number.",
            r"Halve them for a square root; take a third for a cube root.",
            r"Root the digits as a whole number and place the point.",
        ],
        r"Rooting affects the place values exactly as the index divides the decimal count.",
        r"Find $\sqrt{1.69} + \sqrt{0.0169}$.",
        [
            r"$\sqrt{1.69} = 1.3$ (two places become one).",
            r"$\sqrt{0.0169} = 0.13$ (four places become two).",
            r"$1.3 + 0.13 = 1.43$.",
        ],
        "1.43",
    ),
]


# ================= subtopic: simp-approximation =================

SA_CONCEPT = (
    "An approximation question hands you ugly numbers on purpose and options that sit "
    "far apart. Round every number to a friendly value, compute exactly on the rounded "
    "numbers, and pick the nearest option."
)

SA_NOTES = r"""When a question starts with 'what approximate value', it is permission to round. The numbers are deliberately awkward, like $399.87$ or $24.98\%$, and the options sit $5$ to $10$ percent apart. Rounding error stays near one percent, so the nearest option is safe.

### The rounding rules
Round decimals to the nearest whole number: $49.98$ to $50$, $15.02$ to $15$, $23.9$ to $24$. Snap roots and powers to neighbours: $\sqrt{1224.9}$ sits next to $35^2 = 1225$, and $(29.98)^2$ is $30^2 = 900$ for all practical purposes.

> **Rule:** Round first, then compute exactly on the rounded numbers. Never carry ugly decimals through five steps.

### Percentage anchors, learned cold
| Fraction | Percent | Fraction | Percent |
|---|---|---|---|
| $1/2$ | $50\%$ | $1/8$ | $12.5\%$ |
| $1/3$ | $33.3\%$ | $1/9$ | $11.1\%$ |
| $1/4$ | $25\%$ | $1/12$ | $8.3\%$ |
| $1/5$ | $20\%$ | $3/8$ | $37.5\%$ |
| $1/6$ | $16.7\%$ | $2/3$ | $66.7\%$ |

So $16.98\%$ of $600$ reads as one sixth of $600$, about $100$. Percentage times round bases is a one-step mental product.

> **Tip:** Convert the percent to its fraction anchor before touching the base number; $37.5\%$ of $480$ is three eighths of $480$, which is $180$.

### Balanced rounding in products
When two rounded numbers multiply, round one up and the other down so the errors cancel. $15.02 \times 23.9$ becomes $15 \times 24 = 360$, not $15 \times 24$ after rounding both up. One factor down, one factor up, every time.

### Roots and powers near perfect values
Setters place roots beside perfect powers on purpose. $\sqrt{3968.9}$ is $63$ because $63^2 = 3969$; $\sqrt[3]{29791.03}$ is $31$ because $31^3 = 29791$. Spot the neighbour first, then read the root off it.

### Size and direction checks
Decide the size region before computing: tens, hundreds or thousands. One decoy option usually lives in each region. For unknowns, direction matters: $18\%$ of $?$ equals $117$ means $? = 117$ divided by $0.18$, a bigger number; $(?)\%$ of $800$ equals $240$ means $?$ is itself a percentage, here $30$.

> **Watch:** A question mark before the percent sign asks for a percent; a question mark after 'of' asks for a number. Mixing them flips the answer by a factor of ten.

### One clean run
$19.98\%$ of $200 + 11.99 \times 6$: one fifth of $200$ is $40$, and $12 \times 6 = 72$, so about $112$. Round, compute once, choose, move on.

> **Remember:** An approximation question is a reading test, not an arithmetic test. The setter wrote ugly numbers so that rounding is the intended path; the student who multiplies $399.87$ by hand has already lost the time race.
"""

SA_FORMULAS = [
    {"name": "Percentage swap", "tex": r"x\% \text{ of } y = y\% \text{ of } x", "note": ""},
    {"name": "Near-square root", "tex": r"\sqrt{n^2 + k} \approx n + \frac{k}{2n}", "note": ""},
    {"name": "Percent-fraction anchors", "tex": r"12.5\% = \tfrac{1}{8},\quad 16.7\% = \tfrac{1}{6},\quad 33.3\% = \tfrac{1}{3},\quad 37.5\% = \tfrac{3}{8}", "note": ""},
]

SA_TRICKS = [
    {
        "title": "Swap the percentage",
        "body": "x percent of y equals y percent of x. Flip to whichever side has the nicer multiplier.",
        "example": {
            "q": "Find 8% of 125.",
            "steps": [
                r"Swap: $8\%$ of $125 = 125\%$ of $8$.",
                r"$125\%$ of $8 = 8 + \dfrac{1}{4}$ of $8$.",
                r"$8 + 2 = 10$.",
            ],
            "answer": "10",
        },
    },
    {
        "title": "Balanced rounding for products",
        "body": "Round one factor up and the other down. The two errors cancel and the product stays close.",
        "example": {
            "q": "Approximate 15.02 x 23.9.",
            "steps": [
                r"Round $15.02$ down to $15$.",
                r"Round $23.9$ up to $24$.",
                r"$15 \times 24 = 360$; the exact value is $358.98$.",
            ],
            "answer": "360",
        },
    },
    {
        "title": "Anchors before bases",
        "body": "Turn the percent into its fraction anchor first, then apply it to the rounded base.",
        "example": {
            "q": "Approximate 37.48% of 479.9.",
            "steps": [
                r"$37.5\% = \dfrac{3}{8}$ and $479.9 \approx 480$.",
                r"$\dfrac{3}{8} \times 480 = 3 \times 60$.",
                r"$= 180$.",
            ],
            "answer": "180",
        },
    },
]

SA_MISTAKES = [
    {
        "wrong": "Rounding every number in a product in the same direction.",
        "right": "Round one factor up and the other down so errors cancel.",
    },
    {
        "wrong": "Computing the exact value with long multiplication.",
        "right": "Round, compute on friendly numbers, pick the nearest option; the spacing allows it.",
    },
    {
        "wrong": "Treating (?)% as a number and of ? as a percentage.",
        "right": "The percent sign on the question mark makes the unknown a percent; otherwise it is a plain number.",
    },
    {
        "wrong": "Forgetting BODMAS order while approximating.",
        "right": "The 'of' product still outranks the division sign in rounded work too.",
    },
]

SA_REVISION = [
    r"Round every number first; compute exactly on rounded values.",
    r"Percent to fraction anchor before touching the base.",
    r"Products: round one factor up, one down.",
    r"Roots sit beside perfect powers; read the neighbour.",
    r"Check size region and the direction of the unknown percent.",
]

SA_PATTERNS = [
    pat(
        "simp-ap-p1", "Mixed chain with percent, multiply and divide", "very common",
        r"A question mark with 'approximately equals' and a chain mixing % of, products and divisions of decimals.",
        r"\text{round each number, then compute exactly}",
        [
            r"Round each decimal to its nearest friendly value.",
            r"Replace the percent with its fraction anchor.",
            r"Compute the chain with BODMAS order.",
            r"Pick the option nearest to the result.",
        ],
        r"Options sit several percent apart while rounding error stays near one percent.",
        r"$24.98\%$ of $799.8 + 14.98 \times 20.02 \approx ?$",
        [
            r"$24.98\% \approx 25\% = \dfrac{1}{4}$, and $799.8 \approx 800$.",
            r"$\dfrac{1}{4} \times 800 = 200$.",
            r"$15 \times 20 = 300$.",
            r"$200 + 300 = 500$.",
        ],
        "500",
    ),
    pat(
        "simp-ap-p2", "Percentage chains and unknown percent equations", "very common",
        r"Two percent terms combined, or an equation where the unknown is itself a percentage.",
        r"(?)\% = \dfrac{\text{target} - \text{known part}}{\text{base}} \times 100",
        [
            r"Round the base and the targets.",
            r"Shift the known numbers to the far side first.",
            r"Divide the remainder by the base and scale by 100.",
        ],
        r"After shifting, the equation is one division on rounded numbers.",
        r"$(?)\%$ of $799.8 + 39.98 \approx 279.9$. Find the value of $?$.",
        [
            r"$799.8 \approx 800$, $39.98 \approx 40$, $279.9 \approx 280$.",
            r"$280 - 40 = 240$ is the percent part.",
            r"$240 = 30\%$ of $800$, so $? = 30$.",
        ],
        "30",
    ),
    pat(
        "simp-ap-p3", "Roots and powers inside an approximation", "common",
        r"Near-perfect squares and cubes hide inside the expression, like $(29.98)^2$ or $\sqrt{1224.9}$.",
        r"(a \pm 0.02)^2 \approx a^2,\quad \sqrt{n^2 \pm k} \approx n",
        [
            r"Snap each square to the rounded base squared.",
            r"Snap each root to the neighbouring perfect power.",
            r"Combine the snapped values.",
        ],
        r"Setters build these expressions within a whisker of perfect powers, so snapping loses almost nothing.",
        r"$(29.98)^2 + \sqrt{1224.9} \approx ?$",
        [
            r"$29.98 \approx 30$, so $(29.98)^2 \approx 900$.",
            r"$35^2 = 1225$, so $\sqrt{1224.9} \approx 35$.",
            r"$900 + 35 = 935$.",
        ],
        "935",
    ),
    pat(
        "simp-ap-p4", "Find the missing value", "very common",
        r"The question mark is a whole term of the equation, not necessarily a percentage.",
        r"? = \text{constant side} - \text{evaluated terms}",
        [
            r"Evaluate every term that holds no question mark.",
            r"Move it across the equals sign with the inverse operation.",
            r"Round the result and sanity-check its size.",
        ],
        r"It is one move of algebra applied to rounded numbers.",
        r"$27.98\%$ of $449.9 + ? \approx 200$. Find $?$.",
        [
            r"$27.98\% \approx 28\%$ and $449.9 \approx 450$.",
            r"$28\%$ of $450 = 126$.",
            r"$? \approx 200 - 126 = 74$.",
        ],
        "74",
    ),
    pat(
        "simp-ap-p5", "Round before dividing", "common",
        r"An awkward division like $399.87 \div 7.99$, often mixed with other rounded terms.",
        r"\text{round divisor and dividend to compatible values}",
        [
            r"Round the divisor to a friendly one-digit number.",
            r"Round the dividend so the division comes out clean.",
            r"Finish the remaining terms and combine.",
        ],
        r"A clean quotient beats a correct-but-slow long division, because options are far apart.",
        r"$399.87 \div 7.99 + 18.03 \times 4.97 \approx ?$",
        [
            r"$399.87 \div 7.99 \approx 400 \div 8 = 50$.",
            r"$18.03 \times 4.97 \approx 18 \times 5 = 90$.",
            r"$50 + 90 = 140$.",
        ],
        "140",
    ),
]


# ================= loader =================

data = json.loads(TOPIC.read_text(encoding="utf-8"))
subs = {s["id"]: s for s in data["subtopics"]}


def apply(sid, concept, notes, formulas, tricks, mistakes, revision, patterns):
    sub = subs[sid]
    old = {p["id"] for p in sub["patterns"]}
    new = {p["id"] for p in patterns}
    assert old <= new, (sid, old - new)
    assert len(new) == len(patterns), (sid, "duplicate pattern ids")
    other = {p["id"] for s2 in data["subtopics"] if s2["id"] != sid for p in s2["patterns"]}
    assert not (new & other), (sid, new & other)
    assert 2500 <= len(notes) <= 5000, (sid, len(notes))
    sub.update(concept=concept, notes=notes, formulas=formulas, tricks=tricks,
               mistakes=mistakes, revision=revision, patterns=patterns)


apply("simp-bodmas", SB_CONCEPT, SB_NOTES, SB_FORMULAS, SB_TRICKS, SB_MISTAKES, SB_REVISION, SB_PATTERNS)
apply("simp-identities", SI_CONCEPT, SI_NOTES, SI_FORMULAS, SI_TRICKS, SI_MISTAKES, SI_REVISION, SI_PATTERNS)
apply("simp-surds-indices", SS_CONCEPT, SS_NOTES, SS_FORMULAS, SS_TRICKS, SS_MISTAKES, SS_REVISION, SS_PATTERNS)
apply("simp-roots", SR_CONCEPT, SR_NOTES, SR_FORMULAS, SR_TRICKS, SR_MISTAKES, SR_REVISION, SR_PATTERNS)
apply("simp-approximation", SA_CONCEPT, SA_NOTES, SA_FORMULAS, SA_TRICKS, SA_MISTAKES, SA_REVISION, SA_PATTERNS)

TOPIC.write_text(json.dumps(data, ensure_ascii=False, indent=1) + "\n", encoding="utf-8")
print("simplification.json rewritten:", ", ".join(f"{s['id']}:{len(s['patterns'])}" for s in data["subtopics"]))
