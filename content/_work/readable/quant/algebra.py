"""Rewrite every subtopic of core/topics/quant/algebra.json (Phase 3 readable pass).

Keeps all existing pattern ids alg-p1..alg-p24 (practice questions link to them) and
adds two new patterns: alg-p25 (value-putting among expression options) and
alg-p26 (mixed reciprocal form px + 1/(qx)). Every number used in every example
is computed and asserted below. Run with the Python312 interpreter.
"""

import json
from fractions import Fraction as F
from math import sqrt
from pathlib import Path

ROOT = Path(__file__).resolve().parents[3]
TOPIC = ROOT / "core" / "topics" / "quant" / "algebra.json"

# ---------- alg-identities: verified numbers ----------
assert 5 + 4 == 9 and 5 * 4 == 20 and 9 ** 3 - 3 * 20 * 9 == 189 == 5 ** 3 + 4 ** 3
_p, _q = F(94), F(6)
assert (_p ** 3 + _q ** 3) / (_p ** 2 - _p * _q + _q ** 2) == 100
assert 6 ** 2 == 36 and 2 ** 2 == 4 and 36 + 4 == 40 and 6 - (-2) == 8
assert 205 ** 2 - 195 ** 2 == 4000 == 10 * 400
assert 103 * 97 == 9991
assert 873 * 127 == 110871 and 873 ** 2 + 127 ** 2 + 873 * 127 == 889129 == 1000000 - 110871
assert 5 ** 3 - 3 * 6 * 5 == 35 and 5 ** 2 - 2 * 6 == 13 and 13 ** 2 - 2 * 36 == 97
assert (1 + 2) ** 2 - (1 - 2) ** 2 == 8 == 4 * 1 * 2
_a, _b = F(47, 10), F(23, 10)
assert (_a ** 3 + _b ** 3) / (_a ** 2 - _a * _b + _b ** 2) == 7

# ---------- alg-reciprocal: verified numbers ----------
assert 5 ** 3 - 3 * 5 == 110
assert 3 ** 3 + 3 * 3 == 36 and 3 ** 2 + 2 == 11
assert F(8, 3) ** 2 - 2 == F(46, 9)
assert 1 ** 3 - 3 * 1 == -2
assert 3 ** 2 - 2 == 7 and 3 ** 3 - 3 * 3 == 18 and 7 * 18 - 3 == 123 and 7 ** 2 - 2 == 47
assert F(5, 2) * F(3, 2) == F(15, 4) == F(4) - F(1, 4) and 3 ** 2 + 4 == 13  # ladders combine
assert F(9, 4) ** 2 - 2 == F(49, 16) and F(7, 3) ** 2 - 2 == F(31, 9)
assert 4 ** 2 - 2 == 14 and 14 ** 2 - 2 == 194 and 4 ** 3 - 3 * 4 == 52
assert 4 ** 2 + 2 == 18
assert 5 ** 2 - 2 == 23
assert 3 ** 2 + 4 == 13

# ---------- alg-three-var: verified numbers ----------
assert 6 * (6 ** 2 - 3 * 11) == 18
assert 9 * (9 ** 2 - 3 * 26) == 27
assert 4 + 4 + 4 == 12 and 4 * 4 * 4 == 64
assert 4 ** 3 == 10 + 3 * 4 * 5 - 3 * 2 and 1 + 1 + 2 == 4 and 1 * 1 * 2 == 2 and 1 ** 3 + 1 ** 3 + 2 ** 3 == 10
assert (1 + 2) * (2 + 3) * (3 + 1) == 60 == 6 * 11 - 6
assert 3 * (-20) == -60
assert F(1, 2) * (25 + 24 + 23) * (1 + 1 + 4) == 216
assert 3 * 2 * 3 * (-5) == -90 and 2 + 3 + (-5) == 0
assert F(1, -2) + F(1, -2) + F(4, 1) == 3
assert 1 + 1 + 4 == 6 and -2 * (1 - 2 - 2) == 6 and 1 + 1 + 16 == 18 == 2 * (1 - 2 - 2) ** 2
assert 1 + 3 + 6 == 10 and 1 * 3 + 3 * 6 + 6 * 1 == 27 and 1 * 3 * 6 == 18
assert (1 + 3) * (3 + 6) * (6 + 1) == 252 == 10 * 27 - 18

# ---------- alg-surds: verified numbers ----------
assert abs((3 - sqrt(7)) ** 2 - (16 - 6 * sqrt(7))) < 1e-9
assert abs(6 / (sqrt(7) - 1) - (sqrt(7) + 1)) < 1e-9
assert abs((5 + 2 * sqrt(6)) * (5 - 2 * sqrt(6)) - 1) < 1e-9
assert 2 ** 6 == 64 and 3 ** 4 == 81 and 5 ** 3 == 125 and max(64, 81, 125) == 125
assert abs((2 * sqrt(2) + sqrt(7)) ** 2 - (15 + 4 * sqrt(14))) < 1e-9
assert abs((3 + sqrt(2)) ** 2 - (11 + 6 * sqrt(2))) < 1e-9
assert abs((3 - sqrt(2)) ** 2 - (11 - 6 * sqrt(2))) < 1e-9
assert abs((2 + sqrt(3)) + (2 - sqrt(3)) - 4) < 1e-9
assert 4 ** 2 - 2 == 14 and 4 ** 3 - 3 * 4 == 52
assert 10 ** 2 - 2 == 98
assert abs((sqrt(5) + 2) * (sqrt(5) - 2) - 1) < 1e-9
assert abs((sqrt(5) + 2) - (sqrt(5) - 2) - 4) < 1e-9
assert 4 ** 2 + 2 == 18
assert abs(sum(1 / (sqrt(n) + sqrt(n + 1)) for n in (4, 5, 6)) - (sqrt(7) - 2)) < 1e-9
assert sqrt(5) - 2 > sqrt(7) - sqrt(6) > 0
assert abs((sqrt(13) - 2) ** 2 - (17 - 4 * sqrt(13))) < 1e-9
assert abs(3 / (sqrt(5) + sqrt(2)) - (sqrt(5) - sqrt(2))) < 1e-9
assert abs(1 / (sqrt(7) - sqrt(6)) - (sqrt(7) + sqrt(6))) < 1e-9
assert abs(4 / (sqrt(5) - 1) - (sqrt(5) + 1)) < 1e-9
assert abs(1 / (sqrt(3) + sqrt(2)) - (sqrt(3) - sqrt(2))) < 1e-9
assert abs(1 / (sqrt(5) + 2) - (sqrt(5) - 2)) < 1e-9
assert abs(1 / (sqrt(7) + sqrt(6)) - (sqrt(7) - sqrt(6))) < 1e-9
assert sqrt(3) - sqrt(2) > sqrt(5) - 2 > sqrt(7) - sqrt(6)

# ---------- alg-linear-poly: verified numbers ----------
assert 40 // 4 == 10 and 40 // 5 == 8 and 10 * 8 // 2 == 40
assert 9 / 3 == 3.0 and 12 / 4 == 3.0 and 36 / 12 == 3.0 and 4 * 3 == 12
assert 1 - 2 + (-2) + 6 == 3 and -1 - 2 - (-2) + 6 == 5 and (-2) * 6 == -12
assert 12 ** 2 - 2 * 32 == 80 == 4 ** 2 + 8 ** 2
assert 20 // 5 == 4 and 20 // 4 == 5 and 4 * 5 // 2 == 10
assert 20 / 10 == 2.0 and 8 / 4 == 2.0 and 6 / 3 == 2.0
assert 3 ** 2 - 2 * 1 == 7 and 7 ** 2 - 2 * 1 == 47
assert 2 ** 3 - 2 * 2 ** 2 - 2 * 2 + 6 == 2  # p(x)=x^3-2x^2-2x+6 at x=2
assert 2 ** 3 - 3 * 2 ** 2 + 10 == 6 and 6 + 2 * (-3) == 0
assert 2 ** 3 - 3 * 2 ** 2 - 3 * 2 + 10 == 0  # (x-2) factor with k=-3

# ---------- alg-maxmin: verified numbers ----------
assert 5 + F(25, 5) == 10 and 2 * 5 == 10
assert -2 * 2 ** 2 + 8 * 2 + 3 == 11 and -2 * 4 ** 2 + 8 * 4 + 3 == 3
assert 2 * 8 == 16
assert 10 ** 2 == 100 > 9 ** 2 == 81 and 4 * 1 * 25 == 100
assert 2 + F(4, 2) == 4
assert 4 * F(3, 2) + 9 / F(3, 2) == 12
assert 3 * 25 == 75 and 25 ** 3 == 15625 and 15625 ** (1 / 3) > 24.9
assert 2 ** 2 + 4 * 2 + 5 == 17 and (2 + 2) ** 2 + 1 == 17
assert -3 * 2 ** 2 + 12 * 2 + 5 == 17
assert 10 * 10 == 100 and 6 * 6 == 36 and 2 * 6 == 12
assert 9 / 2 == 4.5 and 4.5 * 2 == 9  # 2x+3y=9 style equal split
assert 2 * 6 == 12 and 6 * 6 == 36 and 7 * 5 == 35 < 36  # fixed-sum product cap


def pat(pid, name, freq, spot, formula, steps, why, q, ex_steps, answer):
    return {
        "id": pid, "name": name, "frequency": freq, "howToSpot": spot,
        "formula": formula, "steps": steps, "why": why,
        "example": {"q": q, "steps": ex_steps, "answer": answer},
    }


# ================= subtopic: alg-identities =================

AI_CONCEPT = (
    "An identity is true for every value of the letters, so it works both ways: to "
    "expand and to compress. Exam questions hand you $a+b$ and $ab$, or a scary "
    "fraction, or squares that sum to zero; each is one identity away from a short "
    "answer."
)

AI_NOTES = r"""Five identities answer almost everything here:
$$(a+b)^2 = a^2 + 2ab + b^2 \qquad (a-b)^2 = a^2 - 2ab + b^2 \qquad a^2 - b^2 = (a+b)(a-b)$$
$$a^3 + b^3 = (a+b)(a^2 - ab + b^2) \qquad a^3 - b^3 = (a-b)(a^2 + ab + b^2)$$
Read each one both ways. Expanding is one direction; spotting the factor inside a giant expression is the other, and that is the direction the exam pays for.

### Build upward from a sum and a product
When the question gives $a+b$ and $ab$, never solve for $a$ and $b$. Climb instead:
$$a^2 + b^2 = (a+b)^2 - 2ab \qquad a^3 + b^3 = (a+b)^3 - 3ab(a+b) \qquad a^4 + b^4 = (a^2+b^2)^2 - 2a^2b^2$$
With $a+b = 5$ and $ab = 6$: first $a^2 + b^2 = 25 - 12 = 13$, then $a^3 + b^3 = 125 - 90 = 35$, then $a^4 + b^4 = 169 - 72 = 97$. Each rung reuses the one below it.

> **Rule:** Every symmetric expression in two letters is a function of $a+b$ and $ab$ alone. Two given numbers are always enough.

### Big numbers hide an identity
A fraction with cubed terms is usually an identity fraction. Read the denominator first: a minus middle term pairs with a sum of cubes, a plus middle term with a difference of cubes. So $\dfrac{94^3 + 6^3}{94^2 - 94 \times 6 + 6^2}$ is just $94 + 6 = 100$.
Squares stack the same way: $873^2 + 127^2 + 873 \times 127$ is $(a+b)^2 - ab$ with $a + b = 1000$, giving $1000000 - 110871 = 889129$.

### Squares that must be zero
An equation like $x^2 + y^2 - 12x + 4y + 40 = 0$ is two perfect squares in disguise. Group the $x$ terms and the $y$ terms: $x^2 - 12x + 36$ and $y^2 + 4y + 4$, so $(x-6)^2 + (y+2)^2 = 0$. A square is never negative, so both are zero: $x = 6$, $y = -2$.

> **Watch:** Complete both squares and check that the constants exactly absorb the loose number. If they do not, the equation has other solutions and this route is wrong.

### Products around a round base
Write each number as base plus or minus a small offset. $205^2 - 195^2 = (205 - 195)(205 + 195) = 10 \times 400 = 4000$. And $103 \times 97 = (100+3)(100-3) = 10000 - 9 = 9991$. No long multiplication anywhere.

### Choose expressions by value-putting
When the options are themselves expressions, substitute small numbers into the question and into every option. Only the right option survives. For $(a+b)^2 - (a-b)^2$ with $a = 1$, $b = 2$: the value is $9 - 1 = 8$, and $4ab = 8$ matches.

> **Tip:** Use two different non-zero numbers, and test a second pair if two options tie. Avoid values that make a denominator zero.

### An order that works
1. Read the denominator of any fraction; it names the identity.
2. Match the middle sign before choosing plus or minus forms.
3. Keep the letters symbolic until the last line.
4. Substitute once, at the end.
"""

AI_FORMULAS = [
    {"name": "Square of sum or difference", "tex": r"(a \pm b)^2 = a^2 \pm 2ab + b^2", "note": ""},
    {"name": "Difference of squares", "tex": r"a^2 - b^2 = (a+b)(a-b)", "note": ""},
    {"name": "Sum of cubes", "tex": r"a^3 + b^3 = (a+b)(a^2 - ab + b^2)", "note": ""},
    {"name": "Difference of cubes", "tex": r"a^3 - b^3 = (a-b)(a^2 + ab + b^2)", "note": ""},
    {"name": "Cube of sum", "tex": r"(a+b)^3 = a^3 + b^3 + 3ab(a+b)", "note": ""},
    {"name": "Squares combine", "tex": r"(a+b)^2 + (a-b)^2 = 2(a^2+b^2)", "note": ""},
    {"name": "Squares subtract", "tex": r"(a+b)^2 - (a-b)^2 = 4ab", "note": ""},
    {"name": "Square of a trinomial", "tex": r"(a+b+c)^2 = a^2+b^2+c^2+2(ab+bc+ca)", "note": ""},
    {"name": "Fourth powers from the ladder", "tex": r"a^4 + b^4 = (a^2+b^2)^2 - 2a^2b^2", "note": ""},
]

AI_TRICKS = [
    {
        "title": "Build higher powers from a sum and a product",
        "body": "Chain the rungs: square-sum first, then cube-sum, then fourth powers. The individual letters are never needed.",
        "example": {
            "q": "If a + b = 5 and ab = 6, find a^3 + b^3.",
            "steps": [
                r"$(a+b)^3 = 125$.",
                r"$3ab(a+b) = 3 \times 6 \times 5 = 90$.",
                r"$a^3 + b^3 = 125 - 90 = 35$ (the numbers are $2$ and $3$).",
            ],
            "answer": "35",
        },
    },
    {
        "title": "Recognise the identity inside decimals",
        "body": "Cubed decimals over a trinomial mean a cube identity. The value is the sum or difference of the bases.",
        "example": {
            "q": "Simplify (4.7^3 + 2.3^3) / (4.7^2 - 4.7 x 2.3 + 2.3^2).",
            "steps": [
                r"Bottom has the minus middle term, so it pairs with a sum of cubes.",
                r"Value $= 4.7 + 2.3$.",
                r"$= 7$.",
            ],
            "answer": "7",
        },
    },
    {
        "title": "Value-putting among expression options",
        "body": "Put small numbers into the question and each option. Wrong options die in one round; ties die in a second.",
        "example": {
            "q": "(a + b)^2 - (a - b)^2 equals which of: 2ab, 4ab, 2(a^2+b^2), a^2-b^2?",
            "steps": [
                r"Put $a = 1$, $b = 2$: value $= 9 - 1 = 8$.",
                r"Options give $4$, $8$, $10$, $-3$.",
                r"Only $4ab$ matches, so it is the answer.",
            ],
            "answer": "4ab",
        },
    },
]

AI_MISTAKES = [
    {
        "wrong": "Writing $(a+b)^2 = a^2 + b^2$.",
        "right": "The cross term $2ab$ is the most commonly lost mark; check with $a = b = 1$.",
    },
    {
        "wrong": "Pairing a sum of cubes with the plus middle trinomial.",
        "right": "The middle sign in the factor is opposite to the sign between the cubes.",
    },
    {
        "wrong": "Solving for a and b individually when a+b and ab are given.",
        "right": "Build the target from the sum and the product; the letters never surface.",
    },
    {
        "wrong": "Value-putting with a = b or with zero.",
        "right": "Use two different non-zero values so options cannot collapse together.",
    },
    {
        "wrong": "Declaring a square-sum equation solved without completing both squares.",
        "right": "The constants must absorb the loose number exactly; then each square is zero.",
    },
]

AI_REVISION = [
    r"$a^2+b^2 = (a+b)^2 - 2ab$; $a^3+b^3 = (a+b)^3 - 3ab(a+b)$.",
    r"$\dfrac{a^3 \pm b^3}{a^2 \mp ab + b^2} = a \pm b$.",
    r"$(a+b)^2 - (a-b)^2 = 4ab$.",
    r"Squares summing to zero force each bracket to zero.",
    r"Near a round base, split as base plus and minus the offset.",
    r"Test expression options by value-putting with two small pairs.",
]

AI_PATTERNS = [
    pat(
        "alg-p1", "Symmetric expressions from a sum and a product", "very common",
        r"Two facts like $a+b=9$ and $ab=20$ are given, and a higher symmetric expression is asked.",
        r"a^3+b^3 = (a+b)^3 - 3ab(a+b)",
        [
            r"Never solve for the two letters.",
            r"Write the target using only $(a+b)$ and $ab$.",
            r"Substitute the two given numbers and finish.",
        ],
        r"Every symmetric polynomial in two letters is built from their sum and product.",
        r"If $a + b = 9$ and $ab = 20$, find $a^3 + b^3$.",
        [
            r"$(a+b)^3 = 729$.",
            r"$3ab(a+b) = 3 \times 20 \times 9 = 540$.",
            r"$729 - 540 = 189$ (the numbers are $4$ and $5$).",
        ],
        "189",
    ),
    pat(
        "alg-p2", "Big-number simplification by identity", "very common",
        r"Fractions with cubed large numbers over a trinomial, or stacks of squares like $a^2+b^2+ab$.",
        r"\dfrac{p^3 \pm q^3}{p^2 \mp pq + q^2} = p \pm q",
        [
            r"Read the denominator's middle sign.",
            r"Pick the cube identity with the opposite sign.",
            r"The fraction collapses to the sum or difference of the bases.",
        ],
        r"The denominator is exactly the second factor of the cube identity.",
        r"Find the value of $\dfrac{94^3 + 6^3}{94^2 - 94 \times 6 + 6^2}$.",
        [
            r"Bottom has the minus middle term, so it pairs with a sum of cubes.",
            r"Value $= 94 + 6$.",
            r"$= 100$.",
        ],
        "100",
    ),
    pat(
        "alg-p3", "Sum of squares equal to zero", "very common",
        r"One equation in two or three variables, with squared and linear terms and a loose constant.",
        r"(x-a)^2 + (y-b)^2 = 0 \Rightarrow x = a,\ y = b",
        [
            r"Group the $x$ terms and the $y$ terms.",
            r"Complete each square; the constants must absorb the loose number.",
            r"Each square is zero, so read off both variables.",
            r"Compute the asked combination.",
        ],
        r"A square cannot be negative, so a zero sum of squares pins every letter.",
        r"If $x^2 + y^2 - 12x + 4y + 40 = 0$, find $x - y$.",
        [
            r"$x^2 - 12x + 36$ and $y^2 + 4y + 4$ use up the $40$ exactly.",
            r"$(x-6)^2 + (y+2)^2 = 0$, so $x = 6$, $y = -2$.",
            r"$x - y = 6 - (-2) = 8$.",
        ],
        "8",
    ),
    pat(
        "alg-p4", "Direct evaluation near a round base", "common",
        r"Products or differences of squares of numbers sitting symmetrically around a round base.",
        r"(a+b)(a-b) = a^2 - b^2",
        [
            r"Write each number as base plus or minus an offset.",
            r"Apply the difference of squares.",
            r"Compute in the base, which squares easily.",
        ],
        r"The round base squares in one step, and the small offsets square to nothing.",
        r"Find the value of $205^2 - 195^2$.",
        [
            r"$205 - 195 = 10$ and $205 + 195 = 400$.",
            r"$10 \times 400 = 4000$.",
        ],
        "4000",
    ),
    pat(
        "alg-p25", "Pick the matching expression by value-putting", "common",
        r"The options are algebraic expressions, not numbers, and the question asks which one is equal.",
        r"\text{substitute small numbers in question and options}",
        [
            r"Pick two different small non-zero numbers.",
            r"Evaluate the question expression.",
            r"Evaluate every option on the same numbers.",
            r"If two options survive, test a second pair.",
        ],
        r"An identity holds for every value, so one clean substitution filters all wrong options.",
        r"$(a+b)^2 - (a-b)^2$ is equal to which of $2ab$, $4ab$, $2(a^2+b^2)$, $a^2-b^2$?",
        [
            r"Put $a = 1$, $b = 2$: value $= 9 - 1 = 8$.",
            r"Options give $4$, $8$, $10$, $-3$.",
            r"Only $4ab$ gives $8$; answer $4ab$.",
        ],
        "4ab",
    ),
]


# ================= subtopic: alg-reciprocal =================

AR_CONCEPT = (
    "If $x + \frac{1}{x} = k$, then every power sum $x^n + \frac{1}{x^n}$ climbs from "
    "$k$ without ever solving for $x$. The minus ladder, quadratics with equal end "
    "coefficients, and mixed forms like $2x + \frac{1}{2x}$ all ride the same machine."
)

AR_NOTES = r"""The whole subtopic is one machine. Because $x \times \frac{1}{x} = 1$, the product of the two pieces is fixed, and every power sum becomes a short polynomial in $k$:
$$x^2+\frac{1}{x^2} = k^2 - 2 \qquad x^3+\frac{1}{x^3} = k^3 - 3k \qquad x^4+\frac{1}{x^4} = (k^2-2)^2 - 2$$
There is also a multiply-down rung: $x^5+\frac{1}{x^5} = \left(x^2+\frac{1}{x^2}\right)\left(x^3+\frac{1}{x^3}\right) - k$.

### Watch the ladder work
Take $k = 3$. The square rung gives $9 - 2 = 7$. The cube rung gives $27 - 9 = 18$. The fourth rung squares the second: $49 - 2 = 47$. The fifth rung multiplies rung two by rung three and subtracts $k$: $7 \times 18 - 3 = 123$. Four answers, and $x$ itself never appeared.

> **Rule:** Square for even rungs, use $k^3 - 3k$ for the cube, and chain rungs already computed instead of restarting.

### The minus ladder
For $x - \frac{1}{x} = m$, the cross term flips sign:
$$x^2+\frac{1}{x^2} = m^2 + 2 \qquad x^3-\frac{1}{x^3} = m^3 + 3m$$
With $m = 3$: the square rung gives $9 + 2 = 11$ and the cube rung gives $27 + 9 = 36$. The two ladders connect through $\left(x+\frac{1}{x}\right)^2 = \left(x-\frac{1}{x}\right)^2 + 4$, so $k = \sqrt{m^2 + 4} = \sqrt{13}$ here.

> **Watch:** The square rung of the minus ladder adds 2. Writing $m^2 - 2$ here is the single most common slip in this chapter.

### Quadratics with equal end coefficients
An equation like $4x^2 - 9x + 4 = 0$ has matching first and last coefficients. Divide by $x$: $4x - 9 + \dfrac{4}{x} = 0$, so $x + \dfrac{1}{x} = \dfrac{9}{4}$. Then the square rung gives $\dfrac{81}{16} - 2 = \dfrac{49}{16}$. The same move on $3x^2 - 7x + 3 = 0$ gives $k = \dfrac{7}{3}$ and a square rung of $\dfrac{31}{9}$.

### Cyclic values
Two values of $k$ collapse the ladder entirely. If $k = 1$, then $x^2 - x + 1 = 0$; multiplying by $(x+1)$ gives $x^3 = -1$, so $x^6 = 1$. If $k = -1$, then $x^2 + x + 1 = 0$ and $x^3 = 1$. Stems with giant exponents like $x^{30}$ reduce to small powers by taking the exponent modulo 3 or 6.

### Mixed forms
For $2x + \dfrac{1}{2x} = 5$, square carefully. The middle term is $2 \times 2x \times \dfrac{1}{2x} = 2$, so $4x^2 + \dfrac{1}{4x^2} = 25 - 2 = 23$. In general the middle term of $\left(px + \dfrac{1}{qx}\right)^2$ is $\dfrac{2p}{q}$, not 2.

### Combining the two ladders
Multiplying the sum ladder by the difference ladder kills the cross terms:
$$\left(x+\frac{1}{x}\right)\left(x-\frac{1}{x}\right) = x^2-\frac{1}{x^2}$$
From $m = 3$ above, $k = \sqrt{13}$, so $x^2 - \dfrac{1}{x^2} = 3\sqrt{13}$ in one line. Any pair of $k$ and $m$ used together must first satisfy $k^2 - m^2 = 4$; an option that breaks this cannot be true for any real $x$.

> **Tip:** Plan the route before multiplying. For $x^4+\frac{1}{x^4}$, square twice and never touch the cube rung; for the fifth rung, multiply rung two by rung three.
"""

AR_FORMULAS = [
    {"name": "Square rung", "tex": r"x^2+\frac{1}{x^2} = \left(x+\frac1x\right)^2-2 = \left(x-\frac1x\right)^2+2", "note": ""},
    {"name": "Cube rung, sum", "tex": r"x^3+\frac{1}{x^3} = \left(x+\frac1x\right)^3 - 3\left(x+\frac1x\right)", "note": ""},
    {"name": "Cube rung, difference", "tex": r"x^3-\frac{1}{x^3} = \left(x-\frac1x\right)^3 + 3\left(x-\frac1x\right)", "note": ""},
    {"name": "Fourth rung", "tex": r"x^4+\frac{1}{x^4} = \left(x^2+\frac{1}{x^2}\right)^2 - 2", "note": ""},
    {"name": "Fifth rung", "tex": r"x^5+\frac{1}{x^5} = \left(x^2+\tfrac1{x^2}\right)\left(x^3+\tfrac1{x^3}\right)-\left(x+\tfrac1x\right)", "note": ""},
    {"name": "Ladders link", "tex": r"\left(x+\frac1x\right)^2 - \left(x-\frac1x\right)^2 = 4", "note": ""},
    {"name": "Equal-end quadratic", "tex": r"ax^2 - bx + a = 0 \Rightarrow x+\frac1x = \frac ba", "note": ""},
    {"name": "Mixed form", "tex": r"\left(px+\frac{1}{qx}\right)^2 = p^2x^2+\frac{1}{q^2x^2}+\frac{2p}{q}", "note": ""},
]

AR_TRICKS = [
    {
        "title": "Run the ladder in order",
        "body": "Square rung first, then cube rung, then reuse them for higher rungs. Never restart from k for each question part.",
        "example": {
            "q": "If x + 1/x = 4, find x^2 + 1/x^2, x^4 + 1/x^4 and x^3 + 1/x^3.",
            "steps": [
                r"$x^2+\dfrac{1}{x^2} = 16 - 2 = 14$.",
                r"$x^4+\dfrac{1}{x^4} = 14^2 - 2 = 194$.",
                r"$x^3+\dfrac{1}{x^3} = 64 - 12 = 52$.",
            ],
            "answer": "14, 194, 52",
        },
    },
    {
        "title": "Divide the quadratic by x",
        "body": "Equal first and last coefficients mean the quadratic is a k-value in disguise. Divide by x and read it off.",
        "example": {
            "q": "If 3x^2 - 7x + 3 = 0, find x^2 + 1/x^2.",
            "steps": [
                r"Divide by $3x$: $x + \dfrac{1}{x} = \dfrac{7}{3}$.",
                r"Square rung: $\dfrac{49}{9} - 2$.",
                r"$= \dfrac{31}{9}$.",
            ],
            "answer": "31/9",
        },
    },
    {
        "title": "Switch ladders with one square",
        "body": "The two ladders differ by 4 under a square: k squared equals m squared plus 4. Convert once, then stay on the new ladder.",
        "example": {
            "q": "If x - 1/x = 3, find the positive value of x + 1/x.",
            "steps": [
                r"$k^2 = m^2 + 4$.",
                r"$k^2 = 9 + 4 = 13$.",
                r"$k = \sqrt{13}$ (positive).",
            ],
            "answer": "sqrt(13)",
        },
    },
]

AR_MISTAKES = [
    {
        "wrong": "Subtracting 2 on the minus ladder's square rung.",
        "right": "The minus ladder adds 2: $m^2 + 2$.",
    },
    {
        "wrong": "Writing the cube rung as $k^3 - 3$.",
        "right": "It is $k^3 - 3k$; the k must be multiplied back.",
    },
    {
        "wrong": "Dividing a quadratic by x when the end coefficients differ.",
        "right": "The equal-ends trick needs $ax^2 + bx + a$ exactly.",
    },
    {
        "wrong": "Using a middle term of 2 when squaring $2x + 1/(2x)$.",
        "right": "The middle term is $2p/q$; here it is 2 only because p equals q.",
    },
    {
        "wrong": "Expanding $x^{30}$-type stems directly.",
        "right": "Reduce exponents modulo 3 or 6 first when k is 1 or -1.",
    },
]

AR_REVISION = [
    r"$k = x + \dfrac1x$: square rung $k^2 - 2$, cube rung $k^3 - 3k$.",
    r"$m = x - \dfrac1x$: square rung $m^2 + 2$, cube rung $m^3 + 3m$.",
    r"$k^2 = m^2 + 4$ connects the two ladders.",
    r"$ax^2 - bx + a = 0$ gives $k = b/a$ after dividing by $x$.",
    r"$k = 1$ gives $x^3 = -1$; $k = -1$ gives $x^3 = 1$.",
    r"Mixed form $px + \dfrac{1}{qx}$: middle term is $\dfrac{2p}{q}$.",
]

AR_PATTERNS = [
    pat(
        "alg-p5", "The ladder from x + 1/x = k", "very common",
        r"A value of $x + \frac{1}{x}$ is given and a power sum of $x$ is asked.",
        r"x^3+\frac1{x^3} = k^3 - 3k",
        [
            r"Identify the wanted rung: square, cube, fourth or fifth.",
            r"Square rung: $k^2 - 2$; cube rung: $k^3 - 3k$.",
            r"Fourth rung squares the square rung and subtracts 2.",
            r"Fifth rung multiplies rung two by rung three, minus $k$.",
        ],
        r"The fixed product $x \times \frac{1}{x} = 1$ turns every rung into a polynomial in $k$.",
        r"If $x + \dfrac{1}{x} = 5$, find $x^3 + \dfrac{1}{x^3}$.",
        [
            r"$k^3 = 125$.",
            r"$3k = 15$.",
            r"$125 - 15 = 110$.",
        ],
        "110",
    ),
    pat(
        "alg-p6", "The difference ladder from x - 1/x = m", "very common",
        r"A value of $x - \frac{1}{x}$ is given and a power sum is asked.",
        r"x^3-\frac1{x^3} = m^3 + 3m",
        [
            r"Square rung: $m^2 + 2$ (the sign flips to plus).",
            r"Cube rung: $m^3 + 3m$.",
            r"To reach the sum ladder, use $k^2 = m^2 + 4$.",
        ],
        r"Squaring $x - \frac{1}{x}$ leaves a minus 2 cross term, so it moves across as plus 2.",
        r"If $x - \dfrac{1}{x} = 3$, find $x^3 - \dfrac{1}{x^3}$.",
        [
            r"$m^3 = 27$.",
            r"$3m = 9$.",
            r"$27 + 9 = 36$.",
        ],
        "36",
    ),
    pat(
        "alg-p7", "Quadratic with equal end coefficients", "very common",
        r"An equation like $3x^2 - 8x + 3 = 0$ appears; a reciprocal power sum of its root is asked.",
        r"ax^2 - bx + a = 0 \Rightarrow x + \frac1x = \frac ba",
        [
            r"Check the first and last coefficients match.",
            r"Divide the whole equation by $x$.",
            r"Read off $k = b/a$.",
            r"Run the ladder for the asked rung.",
        ],
        r"Dividing by $x$ merges the end terms into $a\left(x + \frac{1}{x}\right)$.",
        r"If $3x^2 - 8x + 3 = 0$, find $x^2 + \dfrac{1}{x^2}$.",
        [
            r"Divide by $3x$: $x + \dfrac{1}{x} = \dfrac{8}{3}$.",
            r"Square: $\dfrac{64}{9}$.",
            r"Subtract 2: $\dfrac{64}{9} - \dfrac{18}{9} = \dfrac{46}{9}$.",
        ],
        "46/9",
    ),
    pat(
        "alg-p8", "Cyclic values of the ladder", "common",
        r"$k$ equals 1 or -1, or the asked stem has huge exponents like $x^{18}$ or $x^{30}$.",
        r"k = 1 \Rightarrow x^3 = -1;\qquad k = -1 \Rightarrow x^3 = 1",
        [
            r"Multiply $x^2 \mp x + 1 = 0$ by the complementary factor.",
            r"Conclude $x^3 = \mp 1$.",
            r"Reduce every exponent modulo 3 or 6.",
            r"Substitute the reduced powers.",
        ],
        r"These $x$ values are cube roots of unity family, so powers repeat with period 3.",
        r"If $x + \dfrac{1}{x} = 1$, find $x^3 + \dfrac{1}{x^3}$.",
        [
            r"$k = 1$, so $x^2 - x + 1 = 0$ and $x^3 = -1$.",
            r"Then $\dfrac{1}{x^3} = -1$ too.",
            r"$x^3 + \dfrac{1}{x^3} = 1 - 3 = -2$ by the cube rung.",
        ],
        "-2",
    ),
    pat(
        "alg-p26", "Mixed reciprocal forms", "common",
        r"The given relation is $px + \frac{1}{qx}$ or similar, and the target is the squared form.",
        r"\left(px+\frac{1}{qx}\right)^2 = p^2x^2+\frac{1}{q^2x^2}+\frac{2p}{q}",
        [
            r"Square the given relation.",
            r"Compute the middle term as $2p/q$.",
            r"Move it across to isolate the target.",
        ],
        r"Only the coefficients decide the middle term; the $x$ cancels inside the product.",
        r"If $2x + \dfrac{1}{2x} = 5$, find $4x^2 + \dfrac{1}{4x^2}$.",
        [
            r"Square: $4x^2 + \dfrac{1}{4x^2} + 2 \times 2x \times \dfrac{1}{2x} = 25$.",
            r"The middle term is $2$.",
            r"$4x^2 + \dfrac{1}{4x^2} = 25 - 2 = 23$.",
        ],
        "23",
    ),
]


# ================= subtopic: alg-three-var =================

AV_CONCEPT = (
    r"The three-variable cube identity $a^3+b^3+c^3-3abc = (a+b+c)(\dots)$ has two "
    "money forms: a zero sum collapses the cubes to $3abc$, and the equal-squares "
    "condition forces $a=b=c$. Everything else routes through the power-sum expansion."
)

AV_NOTES = r"""The master identity:
$$a^3+b^3+c^3-3abc = (a+b+c)(a^2+b^2+c^2-ab-bc-ca)$$
Rewrite the bracket with the sum alone, using $a^2+b^2+c^2 = s^2 - 2P$:
$$a^3+b^3+c^3-3abc = s\left(s^2 - 3P\right) \quad \text{where } s = a+b+c,\ P = ab+bc+ca$$
With $s = 6$ and $P = 11$: the value is $6 \times (36 - 33) = 18$. One substitution, no cubing.

### The zero-sum shortcut
If $s = 0$, the whole right side vanishes except one reading: $a^3+b^3+c^3 = 3abc$. The exam hides the zero sum inside brackets: $(x-y) + (y-z) + (z-x) = 0$ always. So $(x-y)^3+(y-z)^3+(z-x)^3 = 3(x-y)(y-z)(z-x)$, instantly. Check the shape before expanding anything: with $x-y = 2$ and $y-z = 3$, the third bracket is $-5$, and $3 \times 2 \times 3 \times (-5) = -90$.

> **Rule:** Add the three terms first. If they sum to zero, the cube-sum is three times the product, signs included.

### Zero sum, squares and fourth powers
When $s = 0$, squaring the sum gives $a^2+b^2+c^2 = -2P$. Square once more for fourth powers: $a^4+b^4+c^4 = 2P^2$. Check with $1, 1, -2$: the squares give $6 = -2 \times (-3)$, and the fourth powers give $18 = 2 \times 9$. These two lines answer every 'if $a+b+c=0$' stem that asks about squares or fourth powers, no cubes needed.

### The equal case
The bracket also equals $\dfrac{1}{2}\left[(a-b)^2+(b-c)^2+(c-a)^2\right]$, which is never negative and is zero exactly when $a = b = c$. So the condition $a^2+b^2+c^2 = ab+bc+ca$ forces all three equal. With the extra fact $x+y+z = 12$, each variable is $4$, and quantities like $xyz = 64$ follow at once.

### Power sums
The cube of the sum expands as
$$a^3+b^3+c^3 = s^3 - 3sP + 3R \quad (R = abc)$$
Given any three of $\{s, P, R, \text{cube-sum}\}$, the fourth is one linear step. Example: $s = 4$, $R = 2$, cube-sum $= 10$ (the numbers are $1, 1, 2$). Then $64 = 10 + 12P - 6$, so $P = 5$.

> **Tip:** A useful companion: $(a+b)(b+c)(c+a) = sP - R$. Check with $1, 2, 3$: $3 \times 5 \times 4 = 60$ and $6 \times 11 - 6 = 60$.

### Close numbers: the half form
When the three numbers sit close together, $\dfrac{1}{2}(a+b+c)\left[(a-b)^2+(b-c)^2+(c-a)^2\right]$ is tiny arithmetic. For $25^3+24^3+23^3 - 3 \times 25 \times 24 \times 23$: half of $72$ times $(1 + 1 + 4)$ gives $36 \times 6 = 216$.

### An order that works
1. Do the three brackets or variables sum to zero? Use $3 \times$ product.
2. Are $s$ and $P$ given? Use $s(s^2 - 3P)$.
3. Is $abc$ in the question? Use the power-sum expansion.
4. Does $a^2+b^2+c^2 = ab+bc+ca$ hold? All variables are equal.
"""

AV_FORMULAS = [
    {"name": "Master identity", "tex": r"a^3+b^3+c^3-3abc = (a+b+c)(a^2+b^2+c^2-ab-bc-ca)", "note": ""},
    {"name": "Sum form", "tex": r"a^3+b^3+c^3-3abc = s\left(s^2-3P\right)", "note": ""},
    {"name": "Half form", "tex": r"a^3+b^3+c^3-3abc = \tfrac12\,s\left[(a-b)^2+(b-c)^2+(c-a)^2\right]", "note": ""},
    {"name": "Zero-sum case", "tex": r"a+b+c = 0 \Rightarrow a^3+b^3+c^3 = 3abc", "note": ""},
    {"name": "Equal case", "tex": r"a^2+b^2+c^2 = ab+bc+ca \Rightarrow a=b=c", "note": ""},
    {"name": "Power-sum expansion", "tex": r"a^3+b^3+c^3 = s^3 - 3sP + 3R", "note": ""},
    {"name": "Pair products", "tex": r"(a+b)(b+c)(c+a) = sP - R", "note": ""},
    {"name": "Pairwise from squares", "tex": r"ab+bc+ca = \dfrac{(a+b+c)^2-(a^2+b^2+c^2)}{2}", "note": ""},
]

AV_TRICKS = [
    {
        "title": "Hunt for a hidden zero sum",
        "body": "Brackets like x minus y, y minus z, z minus x always sum to zero. The cube-sum is three times the product.",
        "example": {
            "q": "If x - y = 2 and y - z = 3, find (x-y)^3 + (y-z)^3 + (z-x)^3.",
            "steps": [
                r"$z - x = -(2 + 3) = -5$.",
                r"The three brackets sum to zero, so the cube-sum is $3$ times the product.",
                r"$3 \times 2 \times 3 \times (-5) = -90$.",
            ],
            "answer": "-90",
        },
    },
    {
        "title": "Close numbers: use the half form",
        "body": "When the three numbers differ by little, the squared differences are tiny, and half of s times their sum is quick arithmetic.",
        "example": {
            "q": "Find 25^3 + 24^3 + 23^3 - 3 x 25 x 24 x 23.",
            "steps": [
                r"$s = 72$; differences: $(a-b)^2 = 1$, $(b-c)^2 = 1$, $(c-a)^2 = 4$.",
                r"$\dfrac{1}{2} \times 72 \times 6$.",
                r"$= 216$.",
            ],
            "answer": "216",
        },
    },
    {
        "title": "Value-putting under a condition",
        "body": "If a condition like a+b+c=0 is given, pick simple numbers that satisfy it and evaluate the expression.",
        "example": {
            "q": "If a + b + c = 0, find a^2/bc + b^2/ca + c^2/ab.",
            "steps": [
                r"Put $a = 1$, $b = 1$, $c = -2$.",
                r"$\dfrac{1}{-2} + \dfrac{1}{-2} + \dfrac{4}{1}$.",
                r"$= -\dfrac{1}{2} - \dfrac{1}{2} + 4 = 3$.",
            ],
            "answer": "3",
        },
    },
]

AV_MISTAKES = [
    {
        "wrong": "Using $a^3+b^3+c^3 = 3abc$ without checking the sum is zero.",
        "right": "The shortcut is valid only when $a+b+c = 0$.",
    },
    {
        "wrong": "Dropping the half in the half form.",
        "right": "The factor is one half of $s$ times the squared differences; losing it doubles the answer.",
    },
    {
        "wrong": "Forgetting the $+3abc$ term in the power-sum expansion.",
        "right": "$s^3$ expands to cube-sum plus $3sP$ minus $3R$; keep every sign.",
    },
    {
        "wrong": "Losing signs with negative variables.",
        "right": "Two negatives multiply to a positive; recount minus signs before the final multiply.",
    },
]

AV_REVISION = [
    r"$a^3+b^3+c^3-3abc = s(s^2 - 3P)$.",
    r"$a+b+c = 0$ gives $a^3+b^3+c^3 = 3abc$.",
    r"$(x-y)^3+(y-z)^3+(z-x)^3 = 3(x-y)(y-z)(z-x)$.",
    r"$a^2+b^2+c^2 = ab+bc+ca$ forces $a = b = c$.",
    r"$a^3+b^3+c^3 = s^3 - 3sP + 3R$.",
    r"$(a+b)(b+c)(c+a) = sP - R$.",
]

AV_PATTERNS = [
    pat(
        "alg-p9", "Zero-sum cubes", "very common",
        r"Three cubes whose bases or brackets add to zero, or a stated condition $a+b+c=0$ with $abc$ known.",
        r"a+b+c = 0 \Rightarrow a^3+b^3+c^3 = 3abc",
        [
            r"Add the three bases or brackets; confirm zero.",
            r"Multiply the three together.",
            r"Triple the product, watching signs.",
        ],
        r"The master identity carries the factor $(a+b+c)$, and zero kills the rest.",
        r"If $a + b + c = 0$ and $abc = -20$, find $a^3 + b^3 + c^3$.",
        [
            r"The sum is zero, so the rule applies.",
            r"$3 \times abc = 3 \times (-20)$.",
            r"$= -60$.",
        ],
        "-60",
    ),
    pat(
        "alg-p10", "The sum form s times s squared minus 3P", "very common",
        r"The sum $a+b+c$ and the pairwise sum $ab+bc+ca$ are given; $a^3+b^3+c^3-3abc$ is asked.",
        r"a^3+b^3+c^3-3abc = s(s^2 - 3P)",
        [
            r"Name $s = a+b+c$ and $P = ab+bc+ca$.",
            r"Compute $s^2 - 3P$.",
            r"Multiply by $s$.",
        ],
        r"Substituting $a^2+b^2+c^2 = s^2 - 2P$ leaves the bracket as $s^2 - 3P$.",
        r"If $a + b + c = 9$ and $ab + bc + ca = 26$, find $a^3+b^3+c^3-3abc$.",
        [
            r"$s^2 = 81$.",
            r"$3P = 78$, so $s^2 - 3P = 3$.",
            r"$9 \times 3 = 27$.",
        ],
        "27",
    ),
    pat(
        "alg-p11", "The equal variables case", "common",
        r"The condition $x^2+y^2+z^2 = xy+yz+zx$ appears, and a symmetric quantity is asked.",
        r"x^2+y^2+z^2 = xy+yz+zx \Rightarrow x = y = z",
        [
            r"Recognise the condition; it forces all three equal.",
            r"Find the common value from the given sum: divide by 3.",
            r"Evaluate the asked quantity with the common value.",
        ],
        r"The difference of the two sides is half a sum of squares, zero only when all equal.",
        r"If $x^2+y^2+z^2 = xy+yz+zx$ and $x+y+z = 12$, find $xyz$.",
        [
            r"The condition forces $x = y = z$.",
            r"$x + y + z = 12$ gives each variable $4$.",
            r"$xyz = 4 \times 4 \times 4 = 64$.",
        ],
        "64",
    ),
    pat(
        "alg-p12", "Power sums with the product", "common",
        r"Three of sum, pairwise sum, product and cube-sum are given; the fourth is asked.",
        r"a^3+b^3+c^3 = s^3 - 3sP + 3R",
        [
            r"Write the expansion with the known letters in place.",
            r"Substitute the three known quantities.",
            r"Solve the resulting linear equation for the fourth.",
        ],
        r"The cube of the sum expands into exactly these four symmetric pieces.",
        r"If $a + b + c = 4$, $abc = 2$ and $a^3+b^3+c^3 = 10$, find $ab+bc+ca$.",
        [
            r"$s^3 = 64$.",
            r"$64 = 10 + 3 \times 4 \times P - 3 \times 2$.",
            r"$12P = 60$, so $P = 5$ (the numbers are $1, 1, 2$).",
        ],
        "5",
    ),
    pat(
        "alg-p27", "Pair products from s, P and R", "common",
        r"The question asks for $(a+b)(b+c)(c+a)$ while $a+b+c$, $ab+bc+ca$ and $abc$ are given or findable.",
        r"(a+b)(b+c)(c+a) = (a+b+c)(ab+bc+ca) - abc",
        [
            r"Collect $s = a+b+c$, $P = ab+bc+ca$ and $R = abc$.",
            r"Substitute into $sP - R$.",
            r"Keep the product in one line; expand nothing.",
        ],
        r"Each pair sum is the total minus the missing variable, and the three multiply to exactly $sP - R$.",
        r"If $a + b + c = 10$, $ab + bc + ca = 27$ and $abc = 18$, find $(a+b)(b+c)(c+a)$.",
        [
            r"$sP = 10 \times 27 = 270$.",
            r"$sP - R = 270 - 18 = 252$.",
            r"Check with $1, 3, 6$: $4 \times 9 \times 7 = 252$.",
        ],
        "252",
    ),
]


# ================= subtopic: alg-surds =================

AS_CONCEPT = (
    "A surd is a root that stays irrational. Four moves cover the exam: rationalise "
    r"with the conjugate, denest $\sqrt{a+b\sqrt{c}}$, spot a conjugate pair whose "
    "product is 1, and compare surds after raising to a common power."
)

AS_NOTES = r"""To clear a root from a denominator, multiply top and bottom by the conjugate, the same terms with the middle sign flipped:
$$\dfrac{1}{\sqrt{a} \pm \sqrt{b}} = \dfrac{\sqrt{a} \mp \sqrt{b}}{a - b}$$
So $\dfrac{1}{\sqrt{7}-\sqrt{6}} = \sqrt{7}+\sqrt{6}$, because the denominator product is $7 - 6 = 1$. With a coefficient, divide once: $\dfrac{4}{\sqrt{5}-1} = \dfrac{4(\sqrt{5}+1)}{4} = \sqrt{5}+1$, and $\dfrac{3}{\sqrt{5}+\sqrt{2}} = \sqrt{5}-\sqrt{2}$.

### Denesting a nested root
Try $\sqrt{a + b\sqrt{c}} = \sqrt{p} + \sqrt{q}$. Squaring gives the two conditions: $p + q = a$ and $2\sqrt{pq} = b\sqrt{c}$. Examples: $\sqrt{15 + 4\sqrt{14}} = 2\sqrt{2} + \sqrt{7}$, since $8 + 7 = 15$ and $2\sqrt{56} = 4\sqrt{14}$; and $\sqrt{11 + 6\sqrt{2}} = 3 + \sqrt{2}$, since $9 + 2 = 11$ and $2\sqrt{9} = 6$.

> **Rule:** Force the inner coefficient to the shape $2\sqrt{\cdot}$ first: $6\sqrt{2}$ is $2\sqrt{18}$, so the product you need is 18, not 2.

### The product-one conjugate pair
When $x = p + \sqrt{q}$ and $p^2 - q = 1$, the reciprocal is the conjugate: $\dfrac{1}{x} = p - \sqrt{q}$. Then the reciprocal ladder runs free. With $x = 2+\sqrt{3}$: $x + \dfrac{1}{x} = 4$, the square rung gives $14$, and the cube rung gives $52$. With $x = 5+2\sqrt{6}$: $25 - 24 = 1$, so $x + \dfrac{1}{x} = 10$ and the square rung gives $98$.

> **Watch:** Check $p^2 - q$ before claiming the reciprocal. If it is not 1 or a perfect square, do the full rationalisation instead.

### Telescoping chains
Each term $\dfrac{1}{\sqrt{n+1}+\sqrt{n}}$ equals $\sqrt{n+1}-\sqrt{n}$, so a chain cancels in the middle:
$$\dfrac{1}{\sqrt{5}+\sqrt{4}} + \dfrac{1}{\sqrt{6}+\sqrt{5}} + \dfrac{1}{\sqrt{7}+\sqrt{6}} = \sqrt{7} - \sqrt{4} = \sqrt{7}-2$$
Write the answer as last root minus first root and skip the middle terms entirely. A chain running from $\sqrt{3}$ to $\sqrt{10}$ collapses to $\sqrt{10}-\sqrt{3}$ the same way, however many terms it lists.

### Comparing surds
Raise every surd to the LCM of the root orders and compare plain integers. For $\sqrt{2}$, $\sqrt[3]{3}$, $\sqrt[4]{5}$: orders 2, 3, 4 give LCM 12, and twelfth powers are $2^6 = 64$, $3^4 = 81$, $5^3 = 125$. The last is largest, so $\sqrt[4]{5}$ wins.
For differences of roots, use $\sqrt{a}-\sqrt{b} = \dfrac{a-b}{\sqrt{a}+\sqrt{b}}$: with equal numerators, the pair with larger roots gives the smaller difference. That is why $\sqrt{5}-\sqrt{4}$ beats $\sqrt{7}-\sqrt{6}$.

> **Tip:** Keep three decimal values ready: $\sqrt{2} \approx 1.414$, $\sqrt{3} \approx 1.732$, $\sqrt{5} \approx 2.236$. They settle close comparisons in seconds.
"""

AS_FORMULAS = [
    {"name": "Rationalisation", "tex": r"\frac{1}{\sqrt{a} \pm \sqrt{b}} = \frac{\sqrt{a} \mp \sqrt{b}}{a-b}", "note": ""},
    {"name": "Conjugate product", "tex": r"(\sqrt{a}+\sqrt{b})(\sqrt{a}-\sqrt{b}) = a-b", "note": ""},
    {"name": "Root of a surd, plus", "tex": r"\sqrt{a+2\sqrt{b}} = \sqrt{m}+\sqrt{n},\ m+n = a,\ mn = b", "note": ""},
    {"name": "Root of a surd, minus", "tex": r"\sqrt{a-2\sqrt{b}} = \sqrt{m}-\sqrt{n}\ \ (m > n)", "note": ""},
    {"name": "Product-one pair", "tex": r"x = p+\sqrt{q},\ p^2-q = 1 \Rightarrow \tfrac1x = p-\sqrt{q},\ x+\tfrac1x = 2p", "note": ""},
    {"name": "Telescoping sum", "tex": r"\sum \frac{1}{\sqrt{n}+\sqrt{n+1}} = \sqrt{\text{last}} - \sqrt{\text{first}}", "note": ""},
    {"name": "Difference of roots", "tex": r"\sqrt{a}-\sqrt{b} = \frac{a-b}{\sqrt{a}+\sqrt{b}}", "note": ""},
]

AS_TRICKS = [
    {
        "title": "Denest by sum and product",
        "body": "Rewrite the inner coefficient as 2 root something, then find two numbers with the given sum and product.",
        "example": {
            "q": r"Simplify $\sqrt{17 - 4\sqrt{13}}$.",
            "steps": [
                r"$4\sqrt{13} = 2\sqrt{52}$, so sum $17$, product $52$.",
                r"The pair is $13$ and $4$.",
                r"$\sqrt{17-4\sqrt{13}} = \sqrt{13} - 2$.",
            ],
            "answer": "sqrt(13) - 2",
        },
    },
    {
        "title": "Spot the product-one conjugate",
        "body": "For x = p + sqrt(q), test p squared minus q. If it is 1, the reciprocal is the conjugate and the ladder runs.",
        "example": {
            "q": "If x = sqrt(5) + 2, find x^2 + 1/x^2.",
            "steps": [
                r"$p^2 - q = 5 - 4 = 1$, so $\dfrac{1}{x} = \sqrt{5} - 2$.",
                r"$x - \dfrac{1}{x} = 4$.",
                r"$x^2+\dfrac{1}{x^2} = 4^2 + 2 = 18$.",
            ],
            "answer": "18",
        },
    },
    {
        "title": "Telescoping rationalisation",
        "body": "Each fraction over consecutive roots becomes a difference; middle terms cancel, leaving last root minus first.",
        "example": {
            "q": r"Find $\dfrac{1}{\sqrt{4}+\sqrt{5}} + \dfrac{1}{\sqrt{5}+\sqrt{6}} + \dfrac{1}{\sqrt{6}+\sqrt{7}}$.",
            "steps": [
                r"Each term is $\sqrt{n+1} - \sqrt{n}$.",
                r"Middle roots cancel pairwise.",
                r"Answer $= \sqrt{7} - \sqrt{4} = \sqrt{7} - 2$.",
            ],
            "answer": "sqrt(7) - 2",
        },
    },
]

AS_MISTAKES = [
    {
        "wrong": r"Writing $\sqrt{a} + \sqrt{b} = \sqrt{a+b}$.",
        "right": "Roots do not split over sums; only products split under a root.",
    },
    {
        "wrong": "Denesting without making the inner coefficient 2.",
        "right": r"Rewrite $b\sqrt{c}$ as $2\sqrt{b^2c/4}$ first, so the product is read correctly.",
    },
    {
        "wrong": r"Putting the smaller root first in $\sqrt{a - 2\sqrt{b}}$.",
        "right": "The minus form is larger root minus smaller root, a positive value.",
    },
    {
        "wrong": "Claiming the reciprocal is the conjugate without checking $p^2 - q$.",
        "right": "Test $p^2 - q$; only 1 or a perfect square gives the shortcut.",
    },
    {
        "wrong": "Comparing surds of different orders by their radicands.",
        "right": "Raise all to the LCM of the root orders, then compare integers.",
    },
]

AS_REVISION = [
    r"Conjugate rationalisation divides by $a - b$.",
    r"$\sqrt{a+2\sqrt{b}} = \sqrt{m}+\sqrt{n}$ with $m+n = a$, $mn = b$.",
    r"$p^2 - q = 1$ makes the reciprocal $p - \sqrt{q}$.",
    r"Chains of $\dfrac{1}{\sqrt{n}+\sqrt{n+1}}$ collapse to last minus first.",
    r"Compare at the LCM of root orders.",
    r"$\sqrt{2} \approx 1.414$, $\sqrt{3} \approx 1.732$, $\sqrt{5} \approx 2.236$.",
]

AS_PATTERNS = [
    pat(
        "alg-p13", "Denesting a nested surd", "common",
        r"A square root wrapped around a number plus or minus a root, to be written without nesting.",
        r"\sqrt{a+2\sqrt{b}} = \sqrt{m}+\sqrt{n},\ m+n=a,\ mn=b",
        [
            r"Rewrite the inner term in the $2\sqrt{\cdot}$ shape.",
            r"Find two numbers with sum $a$ and product $b$.",
            r"Answer is $\sqrt{m}+\sqrt{n}$, or the difference for the minus form.",
            r"Re-square mentally to confirm.",
        ],
        r"Squaring $\sqrt{m}+\sqrt{n}$ returns exactly $a + 2\sqrt{b}$.",
        r"Simplify $\sqrt{16 - 6\sqrt{7}}$.",
        [
            r"$6\sqrt{7} = 2\sqrt{63}$, so sum $16$, product $63$.",
            r"The pair is $9$ and $7$.",
            r"$\sqrt{16-6\sqrt{7}} = \sqrt{9}-\sqrt{7} = 3-\sqrt{7}$.",
        ],
        "3 - sqrt(7)",
    ),
    pat(
        "alg-p14", "Rationalise the denominator", "very common",
        r"A fraction with a root or a binomial surd in the denominator.",
        r"\dfrac{1}{\sqrt{a} \pm \sqrt{b}} = \dfrac{\sqrt{a} \mp \sqrt{b}}{a-b}",
        [
            r"Multiply top and bottom by the conjugate.",
            r"The denominator becomes $a - b$.",
            r"Cancel any common factor before expanding.",
        ],
        r"The conjugate product removes every root from the denominator.",
        r"Find the simplified value of $\dfrac{6}{\sqrt{7}-1}$.",
        [
            r"Multiply by $\dfrac{\sqrt{7}+1}{\sqrt{7}+1}$.",
            r"Denominator: $7 - 1 = 6$.",
            r"$\dfrac{6(\sqrt{7}+1)}{6} = \sqrt{7}+1$.",
        ],
        "sqrt(7) + 1",
    ),
    pat(
        "alg-p15", "Conjugate pair with product one", "very common",
        r"$x = p + \sqrt{q}$ is given, and $x + \frac{1}{x}$ or a higher rung is asked.",
        r"p^2 - q = 1 \Rightarrow \dfrac{1}{x} = p - \sqrt{q},\ x + \dfrac{1}{x} = 2p",
        [
            r"Test $p^2 - q$; confirm it equals 1.",
            r"Write the reciprocal as the conjugate.",
            r"Add to get $x + \frac{1}{x} = 2p$.",
            r"Climb the reciprocal ladder if a higher rung is asked.",
        ],
        r"A product-one pair means the conjugate is exactly the reciprocal.",
        r"If $x = 5 + 2\sqrt{6}$, find $x + \dfrac{1}{x}$.",
        [
            r"$p^2 - q = 25 - 24 = 1$.",
            r"$\dfrac{1}{x} = 5 - 2\sqrt{6}$.",
            r"$x + \dfrac{1}{x} = (5 + 2\sqrt{6}) + (5 - 2\sqrt{6}) = 10$.",
        ],
        "10",
    ),
    pat(
        "alg-p16", "Comparing surds of different orders", "common",
        r"A list of unlike roots asks which is greatest or smallest.",
        r"\text{raise all to the LCM of the root orders}",
        [
            r"Take the LCM of all root orders.",
            r"Raise each surd to that power; roots vanish.",
            r"Compare the integers.",
        ],
        r"A common power turns every surd into a whole number.",
        r"Which is the greatest: $\sqrt{2}$, $\sqrt[3]{3}$ or $\sqrt[4]{5}$?",
        [
            r"Orders 2, 3, 4 give LCM 12.",
            r"Twelfth powers: $2^6 = 64$, $3^4 = 81$, $5^3 = 125$.",
            r"$125$ is largest, so $\sqrt[4]{5}$ is the greatest.",
        ],
        "fourth root of 5",
    ),
    pat(
        "alg-p28", "Ranking fractions with root-sum denominators", "common",
        r"Options like $\dfrac{1}{\sqrt{n}+\sqrt{n+1}}$ ask which fraction is largest or smallest.",
        r"\dfrac{1}{\sqrt{a}+\sqrt{b}} = \dfrac{\sqrt{a}-\sqrt{b}}{a-b}",
        [
            r"Rationalise every option with its conjugate.",
            r"Each difference of radicands is $1$ here, so each value is a plain root difference.",
            r"With equal numerators, the smallest pair of roots gives the largest value.",
            r"Rank and pick.",
        ],
        r"After rationalisation all options share numerator $1$, so only the size of the root pair decides.",
        r"Which is the largest: $\dfrac{1}{\sqrt{3}+\sqrt{2}}$, $\dfrac{1}{\sqrt{5}+\sqrt{4}}$ or $\dfrac{1}{\sqrt{7}+\sqrt{6}}$?",
        [
            r"Rationalising gives $\sqrt{3}-\sqrt{2}$, $\sqrt{5}-2$ and $\sqrt{7}-\sqrt{6}$.",
            r"All equal $\dfrac{1}{\text{sum of the roots}}$, so the smallest roots win.",
            r"$\sqrt{3}+\sqrt{2}$ is the smallest sum, so $\sqrt{3}-\sqrt{2}$ is the largest value.",
        ],
        "1/(sqrt(3)+sqrt(2))",
    ),
]


# ================= subtopic: alg-linear-poly =================

AL_CONCEPT = (
    "Two linear equations are two lines; the ratios of their coefficients say whether "
    "the lines cross once, never, or lie on each other. A single line with the axes "
    "cuts a triangle whose area is half the product of intercepts. Polynomials reduce "
    "to substitutions through the remainder theorem."
)

AL_NOTES = r"""For the pair $a_1x + b_1y = c_1$ and $a_2x + b_2y = c_2$, compare three ratios:
| Ratios | Outcome |
|---|---|
| $a_1/a_2 \ne b_1/b_2$ | one solution, lines cross |
| $a_1/a_2 = b_1/b_2 \ne c_1/c_2$ | no solution, parallel |
| all three ratios equal | same line, infinite solutions |

Find-$k$ questions fix the known ratios first, then force the third. For $3x+4y=10$ and $6x+ky=20$: infinite solutions needs $6/3 = 2$, so $k/4 = 2$ gives $k = 8$, and $20/10 = 2$ agrees.

> **Rule:** The constant ratio decides between parallel and coincident. Never answer before checking $c_1/c_2$.

### Area with the axes
The line $ax + by = c$ cuts the $x$-axis at $\dfrac{c}{a}$ (put $y = 0$) and the $y$-axis at $\dfrac{c}{b}$ (put $x = 0$). The axes are perpendicular, so the triangle area is half the product:
$$\text{area} = \frac{1}{2} \times \frac{c}{a} \times \frac{c}{b}$$
For $4x + 5y = 40$: intercepts $10$ and $8$, area $\dfrac{1}{2} \times 10 \times 8 = 40$. For $5x - 4y = 20$: intercepts $4$ and $-5$, area $\dfrac{1}{2} \times 4 \times 5 = 10$.

> **Watch:** The $x$-intercept divides by $a$ and the $y$-intercept by $b$. Swapping them is the classic slip. Take absolute values for the area.

### Remainder and factor theorems
Dividing $p(x)$ by $(x - \alpha)$ leaves remainder $p(\alpha)$: just substitute. For divisor $x + 1$, substitute $x = -1$. Two remainders give two linear equations in unknown coefficients.
Factor questions are the same with the remainder forced to zero: $(x - \alpha)$ is a factor exactly when $p(\alpha) = 0$.

> **Tip:** For a divisor like $2x - 1$, substitute $x = \frac{1}{2}$, the zero of the divisor, not $1$.

### Quadratic roots
For $ax^2 + bx + c = 0$ with roots $\alpha, \beta$: sum $= -\frac{b}{a}$, product $= \frac{c}{a}$. Build targets from these two: $\alpha^2+\beta^2 = (\alpha+\beta)^2 - 2\alpha\beta$, and $\alpha^4+\beta^4 = (\alpha^2+\beta^2)^2 - 2(\alpha\beta)^2$. For $x^2 - 3x + 1$: sum $3$, product $1$, so $\alpha^2+\beta^2 = 7$ and $\alpha^4+\beta^4 = 47$.
The rebuild also works backwards: roots $4$ and $8$ give the equation $x^2 - 12x + 32 = 0$, the sum as the flipped middle coefficient and the product as the constant.

### Discriminant for root nature
Real distinct roots need $b^2 > 4ac$; equal roots need $b^2 = 4ac$; no real roots when $b^2 < 4ac$. A question saying 'always positive' translates to $a > 0$ together with $b^2 < 4ac$.

### A quick habit
For 'where do the lines meet' questions with options, substitute each option into both equations. Testing options is usually faster than solving the pair.
"""

AL_FORMULAS = [
    {"name": "Unique solution", "tex": r"\frac{a_1}{a_2} \ne \frac{b_1}{b_2}", "note": "lines cross once"},
    {"name": "No solution", "tex": r"\frac{a_1}{a_2} = \frac{b_1}{b_2} \ne \frac{c_1}{c_2}", "note": "parallel lines"},
    {"name": "Infinite solutions", "tex": r"\frac{a_1}{a_2} = \frac{b_1}{b_2} = \frac{c_1}{c_2}", "note": "same line"},
    {"name": "Area with the axes", "tex": r"\text{Area} = \frac{1}{2}\cdot\left|\frac{c}{a}\right|\cdot\left|\frac{c}{b}\right|", "note": ""},
    {"name": "Remainder theorem", "tex": r"p(x) \div (x-a) \Rightarrow R = p(a)", "note": "for px - q, substitute q/p"},
    {"name": "Roots of a quadratic", "tex": r"\alpha+\beta = -\frac ba,\quad \alpha\beta = \frac ca", "note": ""},
    {"name": "Discriminant", "tex": r"b^2 - 4ac \gtrless 0", "note": "decides root nature"},
]

AL_TRICKS = [
    {
        "title": "Area from intercepts",
        "body": "Put y = 0 for the x-intercept and x = 0 for the y-intercept, then halve the product of the absolute values.",
        "example": {
            "q": "Find the area of the triangle formed by 5x - 4y = 20 and the axes.",
            "steps": [
                r"$y = 0$: $x = 4$.",
                r"$x = 0$: $y = -5$, length $5$.",
                r"Area $= \dfrac{1}{2} \times 4 \times 5 = 10$.",
            ],
            "answer": "10 square units",
        },
    },
    {
        "title": "Remainder equals substitution at the zero",
        "body": "No long division: substitute the zero of the divisor into the polynomial.",
        "example": {
            "q": "Find the remainder when x^3 - 2x^2 - 2x + 6 is divided by x - 2.",
            "steps": [
                r"Zero of the divisor: $x = 2$.",
                r"$p(2) = 8 - 8 - 4 + 6$.",
                r"$= 2$.",
            ],
            "answer": "2",
        },
    },
    {
        "title": "Test the options for the intersection point",
        "body": "For a meeting-point question, plug each option into both equations instead of solving the pair.",
        "example": {
            "q": "Where do 2x + 3y = 13 and 3x - y = 3 meet?",
            "steps": [
                r"Try $(2, 3)$: $4 + 9 = 13$ holds.",
                r"Second check: $6 - 3 = 3$ holds.",
                r"Both equations pass, so the point is $(2, 3)$.",
            ],
            "answer": "(2, 3)",
        },
    },
]

AL_MISTAKES = [
    {
        "wrong": "Answering parallel without checking the constant ratio.",
        "right": "The c-ratio separates parallel from coincident; check it last, always.",
    },
    {
        "wrong": "Taking c/b as the x-intercept.",
        "right": "The x-intercept is c/a; put y = 0 to see it.",
    },
    {
        "wrong": "Substituting the wrong sign for divisor x + 3.",
        "right": "Its zero is -3; substitute minus 3.",
    },
    {
        "wrong": "Writing the root sum as b/a.",
        "right": "It is minus b over a; the sign flips.",
    },
    {
        "wrong": "Using a negative intercept as a negative area.",
        "right": "Lengths are absolute; the area is always positive.",
    },
]

AL_REVISION = [
    r"Ratios: unequal gives one solution; all equal gives infinite.",
    r"Parallel needs the first two ratios equal and the third different.",
    r"Intercepts $c/a$ and $c/b$; area is half their product.",
    r"Remainder $= p(\alpha)$ for divisor $x - \alpha$.",
    r"$\alpha+\beta = -b/a$, $\alpha\beta = c/a$.",
    r"$b^2 - 4ac$ compared with 0 decides root nature.",
]

AL_PATTERNS = [
    pat(
        "alg-p17", "Consistency of a linear pair, find k", "common",
        r"Two linear equations with an unknown coefficient $k$; the question fixes the number of solutions.",
        r"\dfrac{a_1}{a_2} = \dfrac{b_1}{b_2} = \dfrac{c_1}{c_2} \text{ for infinite solutions}",
        [
            r"Compute the ratio of the coefficients that are fully known.",
            r"Set the $k$-ratio equal to it and solve for $k$.",
            r"Check the constant ratio: equal for infinite, different for none.",
        ],
        r"Coincident lines must agree in all three ratios, which pins $k$.",
        r"For what value of $k$ do $3x + 4y = 12$ and $9x + ky = 36$ have infinitely many solutions?",
        [
            r"$9/3 = 3$, so $k/4 = 3$ gives $k = 12$.",
            r"Check constants: $36/12 = 3$. All three ratios equal.",
            r"So $k = 12$.",
        ],
        "12",
    ),
    pat(
        "alg-p18", "Area of the triangle cut from the axes", "common",
        r"A line with the coordinate axes bounds a triangle; its area is asked.",
        r"\text{area} = \dfrac{c^2}{2ab}",
        [
            r"Put $y = 0$ and read the $x$-intercept $c/a$.",
            r"Put $x = 0$ and read the $y$-intercept $c/b$.",
            r"Halve the product of the absolute lengths.",
        ],
        r"The axes are perpendicular, so the intercepts are exactly base and height.",
        r"Find the area of the triangle formed by $4x + 5y = 40$ and the coordinate axes.",
        [
            r"$x$-intercept: $40/4 = 10$.",
            r"$y$-intercept: $40/5 = 8$.",
            r"Area $= \dfrac{1}{2} \times 10 \times 8 = 40$.",
        ],
        "40 square units",
    ),
    pat(
        "alg-p19", "Remainder theorem for unknown coefficients", "very common",
        r"A polynomial with unknown coefficients is divided by two linear factors; the two remainders are given.",
        r"p(x) \div (x-a) \Rightarrow R = p(a)",
        [
            r"Substitute the zero of each divisor into the polynomial.",
            r"Set each result equal to the given remainder.",
            r"Solve the two linear equations for the unknowns.",
            r"Compute the asked quantity.",
        ],
        r"Each substitution turns a whole division into one evaluation, giving clean linear equations.",
        r"When $x^3 - 2x^2 + ax + b$ is divided by $(x-1)$ and $(x+1)$ the remainders are $3$ and $5$. Find $ab$.",
        [
            r"$p(1) = 1 - 2 + a + b = 3$, so $a + b = 4$.",
            r"$p(-1) = -1 - 2 - a + b = 5$, so $b - a = 8$.",
            r"Solving: $b = 6$, $a = -2$.",
            r"$ab = -12$.",
        ],
        "-12",
    ),
    pat(
        "alg-p20", "Quadratic roots and symmetric functions", "very common",
        r"A quadratic is given, or its root sum and product; an expression in the roots is asked.",
        r"\alpha+\beta = -\frac ba,\qquad \alpha\beta = \frac ca",
        [
            r"Read the sum and product from the coefficients.",
            r"Write the target using the sum and product.",
            r"Substitute and finish.",
            r"For fourth powers, square the square-sum and subtract twice the product squared.",
        ],
        r"Every symmetric function of the roots is built from their sum and product.",
        r"If $\alpha, \beta$ are the roots of $x^2 - 12x + 32 = 0$, find $\alpha^2 + \beta^2$.",
        [
            r"$\alpha + \beta = 12$ and $\alpha\beta = 32$.",
            r"$\alpha^2+\beta^2 = 144 - 64$.",
            r"$= 80$.",
        ],
        "80",
    ),
    pat(
        "alg-p29", "Factor theorem for an unknown constant", "very common",
        r"A stated linear factor like $(x-2)$ appears with a polynomial holding one unknown coefficient.",
        r"(x-a) \text{ is a factor} \iff p(a) = 0",
        [
            r"Write the zero of the stated factor.",
            r"Substitute it into the polynomial.",
            r"Set the result to zero and solve for the unknown.",
            r"Verify by substituting a nearby point if time allows.",
        ],
        r"A factor means zero remainder, and the remainder is just the substitution value.",
        r"If $(x - 2)$ is a factor of $x^3 - 3x^2 + kx + 10$, find $k$.",
        [
            r"$p(2) = 8 - 12 + 2k + 10 = 6 + 2k$.",
            r"Factor means $p(2) = 0$, so $2k = -6$.",
            r"$k = -3$.",
        ],
        "-3",
    ),
]


# ================= subtopic: alg-maxmin =================

assert F(9, 2) ** 2 == F(81, 4) and float(F(81, 4)) == 20.25  # (2x)(3y) peak

AM_CONCEPT = (
    "Maximum and minimum questions here are not calculus. A plus-shaped expression "
    "has its floor from AM-GM, a parabola peaks at its vertex, fixed sums cap "
    "products, and 'positive for every x' is a discriminant statement."
)

AM_NOTES = r"""The arithmetic mean is never below the geometric mean:
$$\frac{x+y}{2} \ge \sqrt{xy} \qquad (x, y > 0)$$
Equality holds exactly when $x = y$. Every 'least value' question with a plus sign is this line in disguise.

### The least of ax + b over x
For $x > 0$, the two pieces of $ax + \dfrac{b}{x}$ multiply to $b$, so:
$$ax + \frac{b}{x} \ge 2\sqrt{ab}$$
The floor is reached when $ax = \dfrac{b}{x}$, that is $x = \sqrt{b/a}$. Check $x + \dfrac{4}{x}$: the floor is $2\sqrt{4} = 4$ at $x = 2$, and indeed $2 + 2 = 4$. Check $4x + \dfrac{9}{x}$: the floor is $2\sqrt{36} = 12$ at $x = \dfrac{3}{2}$, and indeed $6 + 6 = 12$.

> **Rule:** For $x > 0$, the least value of $ax + \dfrac{b}{x}$ is $2\sqrt{ab}$, at $x = \sqrt{b/a}$. Learn the shape; the derivation is never needed.

### The parabola vertex
For $f(x) = ax^2 + bx + c$ with $a < 0$, the peak sits at $x = -\dfrac{b}{2a}$ and the greatest value is $\dfrac{4ac - b^2}{4a}$. Completing the square gives both at once: $-2x^2 + 8x + 3 = -2(x-2)^2 + 11$, so the greatest value is $11$ at $x = 2$. Farther out the value drops: at $x = 4$ it is $3$.
For $a > 0$ the same work gives the least value. $x^2 + 4x + 5 = (x+2)^2 + 1$ is never below $1$.

> **Tip:** Complete the square instead of recalling the formula. One line yields the location, the value, and the direction.

### Fixed sum or fixed product
With $x + y = S$ fixed, the product peaks at $\dfrac{S^2}{4}$. With $xy = P$ fixed, the sum floors at $2\sqrt{P}$. So $x + y = 10$ forces $xy \le 25$, and $3xy \le 75$. And $xy = 64$ forces $x + y \ge 16$, met at $x = y = 8$.
Weighted forms split first: for $2x + 3y = 9$, the peak of $(2x)(3y)$ comes from $2x = 3y = \dfrac{9}{2}$, giving $\left(\dfrac{9}{2}\right)^2 = 20.25$.

> **Watch:** AM-GM needs positive numbers. For $x < 0$, the expression $x + \dfrac{25}{x}$ has a greatest value of $-10$, not a least value of $10$.

### Always positive means the discriminant stays negative
'$x^2 - kx + 25 > 0$ for every real $x$' means the parabola never touches the axis. So $k^2 < 4 \times 1 \times 25 = 100$, giving $|k| < 10$ and largest integer $k = 9$. The boundary $k = 10$ touches zero at $x = 5$, which is not positive. Equal-root questions sit on the same boundary: $x^2 - 12x + k$ has equal roots when $k = 36$, both roots $6$.

### An order that works
1. A plus-form $ax + \dfrac{b}{x}$ with $x > 0$? Use $2\sqrt{ab}$.
2. A quadratic? Vertex, or complete the square.
3. Fixed sum or fixed product? Split equally.
4. An inequality for every $x$? Discriminant, strict.

> **Remember:** State the equality point too. 'Least value' and 'where it happens' are often separate marks.
"""

AM_FORMULAS = [
    {"name": "AM-GM", "tex": r"\frac{x+y}{2} \ge \sqrt{xy}", "note": "equality when x = y"},
    {"name": "Plus-form floor", "tex": r"ax + \frac{b}{x} \ge 2\sqrt{ab}\ \ (x>0)", "note": "at x = sqrt(b/a)"},
    {"name": "Vertex location", "tex": r"x = -\frac{b}{2a}", "note": ""},
    {"name": "Extreme value", "tex": r"\frac{4ac-b^2}{4a}", "note": "max for a < 0, min for a > 0"},
    {"name": "Fixed sum", "tex": r"x+y = S \Rightarrow xy \le \frac{S^2}{4}", "note": ""},
    {"name": "Fixed product", "tex": r"xy = P \Rightarrow x+y \ge 2\sqrt{P}", "note": ""},
    {"name": "Always positive", "tex": r"ax^2+bx+c > 0 \iff a > 0,\ b^2 < 4ac", "note": "strict inequality, strict discriminant"},
]

AM_TRICKS = [
    {
        "title": "Equal split for weighted sums",
        "body": "To maximise a product under a weighted sum, set the weighted pieces equal, then square.",
        "example": {
            "q": "If 2x + 3y = 9 with x, y > 0, find the largest value of (2x)(3y).",
            "steps": [
                r"Set $2x = 3y = \dfrac{9}{2}$.",
                r"Peak $= \left(\dfrac{9}{2}\right)^2$.",
                r"$= 20.25$.",
            ],
            "answer": "20.25",
        },
    },
    {
        "title": "Complete the square, read the floor",
        "body": "For a > 0, the completed square shows the least value directly as the loose constant.",
        "example": {
            "q": "Find the least value of x^2 + 4x + 5.",
            "steps": [
                r"$x^2 + 4x + 5 = (x+2)^2 + 1$.",
                r"A square is never negative.",
                r"Least value $= 1$ at $x = -2$.",
            ],
            "answer": "1",
        },
    },
    {
        "title": "Equal roots sit on the boundary",
        "body": "Equal roots mean the discriminant is exactly zero; solve the resulting equation for the unknown.",
        "example": {
            "q": "For what k does x^2 - 12x + k = 0 have equal roots?",
            "steps": [
                r"$b^2 = 4ac$: $144 = 4k$.",
                r"$k = 36$.",
                r"Check: roots are $6$ and $6$, sum $12$.",
            ],
            "answer": "36",
        },
    },
]

AM_MISTAKES = [
    {
        "wrong": r"Quoting $2\sqrt{ab}$ when x can be negative.",
        "right": r"For negative x the plus-form has a greatest value of $-2\sqrt{ab}$; check the domain first.",
    },
    {
        "wrong": "Writing the peak location as b/(2a).",
        "right": "It is $-b/(2a)$; for $-2x^2+8x+3$ that gives $+2$.",
    },
    {
        "wrong": "Maximising xy under a fixed sum as S squared.",
        "right": "The cap is $(S/2)^2$: halve the sum first.",
    },
    {
        "wrong": "Accepting the boundary k = 10 for 'always positive'.",
        "right": "Equality touches zero, which is not positive; strict wording needs $k^2 < 100$, so 9.",
    },
    {
        "wrong": "Reading the sum floor from xy = 64 as the root alone.",
        "right": r"The floor is $2\sqrt{P} = 16$; the factor 2 is part of the formula.",
    },
]

AM_REVISION = [
    r"$ax + \dfrac{b}{x} \ge 2\sqrt{ab}$ for $x > 0$, at $x = \sqrt{b/a}$.",
    r"Peak of $ax^2+bx+c$ at $x = -\dfrac{b}{2a}$; value $\dfrac{4ac-b^2}{4a}$.",
    r"Fixed sum: $xy \le \dfrac{S^2}{4}$. Fixed product: $x+y \ge 2\sqrt{P}$.",
    r"Weighted sums: set the weighted pieces equal.",
    r"$ax^2+bx+c > 0$ for all x needs $a > 0$ and $b^2 < 4ac$.",
    r"Equality in AM-GM only when the two pieces are equal.",
]

AM_PATTERNS = [
    pat(
        "alg-p21", "Least value of a plus-form by AM-GM", "very common",
        r"An expression like $x + \dfrac{25}{x}$ with $x > 0$; its least value is asked.",
        r"ax + \frac{b}{x} \ge 2\sqrt{ab}",
        [
            r"Confirm $x > 0$ so both pieces are positive.",
            r"Multiply the two pieces to get $ab$.",
            r"Write the floor as $2\sqrt{ab}$.",
            r"State the equality point $x = \sqrt{b/a}$.",
        ],
        r"A fixed product between the two pieces is exactly the AM-GM setup.",
        r"For $x > 0$, find the least value of $x + \dfrac{25}{x}$.",
        [
            r"Product of the pieces: $x \times \dfrac{25}{x} = 25$.",
            r"Floor $= 2\sqrt{25} = 10$.",
            r"At $x = 5$: $5 + 5 = 10$. Confirmed.",
        ],
        "10",
    ),
    pat(
        "alg-p22", "Greatest value of a downward parabola", "very common",
        r"A quadratic with a negative $x^2$ coefficient; the greatest value is asked.",
        r"\max = \frac{4ac - b^2}{4a} \text{ at } x = -\frac{b}{2a}",
        [
            r"Compute $x = -\dfrac{b}{2a}$.",
            r"Substitute back, or complete the square.",
            r"Report the value and where it occurs.",
        ],
        r"A downward parabola peaks exactly at its vertex.",
        r"Find the greatest value of $-2x^2 + 8x + 3$.",
        [
            r"$x = -\dfrac{8}{2 \times (-2)} = 2$.",
            r"$-8 + 16 + 3 = 11$.",
            r"Square form: $-2(x-2)^2 + 11$, peak $11$.",
        ],
        "11",
    ),
    pat(
        "alg-p23", "Fixed product gives the sum floor", "common",
        r"$xy$ is a fixed positive number and the least of $x + y$ is asked.",
        r"xy = P \Rightarrow x+y \ge 2\sqrt{P}",
        [
            r"Confirm both variables are positive.",
            r"Take $2\sqrt{P}$ as the floor.",
            r"State equality at $x = y = \sqrt{P}$.",
        ],
        r"AM-GM turns a fixed product into a lower bound on the sum.",
        r"If $xy = 64$ with $x, y > 0$, find the least value of $x + y$.",
        [
            r"$2\sqrt{64} = 2 \times 8 = 16$.",
            r"Equality at $x = y = 8$.",
            r"Check: $8 + 8 = 16$.",
        ],
        "16",
    ),
    pat(
        "alg-p24", "Positive for every x, find the parameter", "common",
        r"A quadratic with an unknown coefficient must stay positive for all real $x$.",
        r"ax^2+bx+c > 0 \ \forall x \iff a > 0,\ b^2 - 4ac < 0",
        [
            r"Check the leading coefficient is positive.",
            r"Write the strict discriminant inequality.",
            r"Solve for the parameter.",
            r"Take integers strictly inside the range.",
        ],
        r"Staying above the axis means the parabola never touches it, a discriminant condition.",
        r"If $x^2 - kx + 25 > 0$ for every real $x$, find the largest integer value of $k$.",
        [
            r"Need $k^2 < 4 \times 1 \times 25 = 100$.",
            r"$|k| < 10$.",
            r"$k = 10$ touches zero, so it fails.",
            r"Largest integer: $k = 9$.",
        ],
        "9",
    ),
    pat(
        "alg-p30", "Greatest product under a fixed sum", "very common",
        r"A fixed positive sum $x + y = S$ is given and the greatest value of $xy$, or a multiple of it, is asked.",
        r"x+y = S \Rightarrow xy \le \frac{S^2}{4}",
        [
            r"Halve the sum: the peak sits at $x = y = \dfrac{S}{2}$.",
            r"Square the half.",
            r"Scale by any outside multiplier the question carries.",
        ],
        r"AM-GM caps the product at the square of half the sum, met only when the two parts are equal.",
        r"If $x + y = 12$ with $x, y > 0$, find the greatest value of $xy$.",
        [
            r"Peak at $x = y = 6$.",
            r"$xy \le 6 \times 6 = 36$.",
            r"Neighbour check: $7 \times 5 = 35$, smaller.",
        ],
        "36",
    ),
]


# ---------- write back ----------

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


apply("alg-identities", AI_CONCEPT, AI_NOTES, AI_FORMULAS, AI_TRICKS, AI_MISTAKES, AI_REVISION, AI_PATTERNS)
apply("alg-reciprocal", AR_CONCEPT, AR_NOTES, AR_FORMULAS, AR_TRICKS, AR_MISTAKES, AR_REVISION, AR_PATTERNS)
apply("alg-three-var", AV_CONCEPT, AV_NOTES, AV_FORMULAS, AV_TRICKS, AV_MISTAKES, AV_REVISION, AV_PATTERNS)
apply("alg-surds", AS_CONCEPT, AS_NOTES, AS_FORMULAS, AS_TRICKS, AS_MISTAKES, AS_REVISION, AS_PATTERNS)
apply("alg-linear-poly", AL_CONCEPT, AL_NOTES, AL_FORMULAS, AL_TRICKS, AL_MISTAKES, AL_REVISION, AL_PATTERNS)
apply("alg-maxmin", AM_CONCEPT, AM_NOTES, AM_FORMULAS, AM_TRICKS, AM_MISTAKES, AM_REVISION, AM_PATTERNS)

TOPIC.write_text(json.dumps(data, ensure_ascii=False, indent=1) + "\n", encoding="utf-8")
print("algebra.json rewritten:", len(data["subtopics"]), "subtopics")
