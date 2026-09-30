"""Rewrite every subtopic of core/topics/quant/number-system.json (Phase 3 readable pass).

Keeps all existing pattern ids (practice questions link to them) and adds two new
patterns: ns-dv-p7 (divisibility by 7) and ns-rm-p7 (factorial-sum remainder).
Every number used in every example is computed and asserted below.
Run with the Python312 interpreter.
"""

import json
from fractions import Fraction as F
from math import factorial, gcd, isqrt
from pathlib import Path

ROOT = Path(__file__).resolve().parents[3]
TOPIC = ROOT / "core" / "topics" / "quant" / "number-system.json"

# ---------- ns-types-counting: verified numbers ----------
assert 300 // 4 + 300 // 6 - 300 // 12 == 100
_t7 = list(range(14, 99, 7))
assert len(_t7) == 13 and sum(_t7) == 728 and len(_t7) * (14 + 98) // 2 == 728
assert 845327 // 1000 % 10 == 5 and 5 * 1000 - 5 == 4995
assert 407 == 11 * 37 and isqrt(407) == 20
assert 9 + 90 * 2 + (200 - 99) * 3 == 492
assert 74 - 47 == 27 == 9 * (7 - 4)
assert 300 // 7 - 99 // 7 == 28
assert 221 == 13 * 17
assert 6 * 9999 == 59994
assert 20 * 21 * 41 // 6 - 10 * 11 * 21 // 6 == 2870 - 385 == 2485
assert 9 + 180 + 251 * 3 == 942
assert 500 // 17 - 99 // 17 == 24
assert 8 * 9999 == 79992
assert (48 - 12) // 2 + 1 == 19 and 19 * (12 + 48) // 2 == 570

# ---------- ns-divisibility: verified numbers ----------
sol_72 = [(x, y) for x in range(10) for y in range(10) if (60804 + 1000 * x + 10 * y) % 72 == 0]
assert sol_72 == [(3, 6), (7, 2)]
assert 824 == 8 * 103 and 864 == 8 * 108
assert all(x + y == 9 for x, y in sol_72)
assert 67824 % 72 == 0 and 63864 % 72 == 0
assert (9 + 8 + 8) - (5 + 2 + 7) == 11 and 782859 % 11 == 0 and 782859 // 11 == 71169
assert 29 + 15 == 44 and 29 - 15 == 14
assert pow(29, 18, 44) == pow(15, 18, 44) and pow(29, 18, 14) == pow(15, 18, 14)
assert 3 ** 15 * (1 + 3 + 9) == 3 ** 15 + 3 ** 16 + 3 ** 17 and (1 + 3 + 9) == 13
assert (3 ** 15 + 3 ** 16 + 3 ** 17) % 13 == 0
assert 3286 % 29 == 9 and 3286 + 20 == 3306 == 29 * 114
assert 276276 == 276 * 1001 and 1001 == 7 * 11 * 13
assert 276276 % 7 == 0 and 276276 % 11 == 0 and 276276 % 13 == 0
assert 359 - 2 * 8 == 343 == 7 * 49 and 3598 % 7 == 0
assert (5 + 4 + 4) == 13 and (7 + 8 + 9) == 24 and 24 - 13 == 11
assert 948475 % 11 == 0
assert 8357 % 12 == 5 and 8357 + 7 == 8364 == 12 * 697
assert (pow(17, 25, 40) + pow(23, 25, 40)) % 40 == 0
assert 484484 % 13 == 0
assert 36 % 4 == 0 and 36 % 6 == 0 and 36 % 24 == 12
assert [x for x in range(10) if (37084 + 1000 * x) % 12 == 0] == [2, 5, 8]
assert (37084 + 2000) % 12 == 0

# ---------- ns-remainders: verified numbers ----------
assert 342 == 18 * 19 and 47 % 19 == 9 and 47 % 18 == 11
assert (98 * 97 * 96) % 99 == 93
assert (-1) * (-2) * (-3) == -6 and (-6) % 99 == 93
assert 95 % 3 == 2 and pow(2, 95, 7) == 4
assert 3 * 5 == 15 and 4 * 15 == 60 and 60 * 15 + 5 == 905
assert (4 ** 3 + 4) % 11 == 2 and (15 ** 3 + 15) % 11 == 2
assert 9 % 4 == 1 and 9 // 4 == 2 and 2 % 5 == 2
assert sum(factorial(i) for i in range(1, 51)) % 15 == 3
assert (1 + 2 + 6 + 24) == 33 and 33 % 15 == 3 and 120 % 15 == 0
assert 24 * 13 + 17 == 329
assert (1021 % 17, 1023 % 17, 1025 % 17) == (1, 3, 5)
assert (1021 * 1023 * 1025) % 17 == 15
assert pow(2, 100, 7) == 2
assert (4 * 5) % 9 == 2
assert pow(15, 47, 16) == 15
assert 29 % 8 == 5

# ---------- ns-unit-digit: verified numbers ----------
assert pow(4, 63, 10) == 4 and pow(9, 72, 10) == 1 and pow(8, 41, 10) == 8
assert (4 * 1 * 8) % 10 == 2
assert (pow(7, 105) - pow(3, 58)) % 10 == 8
assert (2 ** 31 * 5 ** 17 * 3 ** 9) % 10 == 0
assert pow(21, 20, 4) == 1 and pow(7, 21 ** 20, 10) == 7
assert pow(71, 36, 100) == 21 and (7 * 36) % 10 == 2
assert 67 % 4 == 3 and pow(8, 67, 10) == 2
assert (pow(6, 25, 10) + pow(9, 31, 10)) % 10 == 5
assert sum(factorial(i) for i in range(1, 51)) % 10 == 3
assert pow(3, 4 ** 5, 10) == 1
assert pow(41, 27, 100) == 81 and (4 * 27) % 10 == 8
assert 2463 % 4 == 3 and pow(1357, 2463, 10) == 3

# ---------- ns-factors: verified numbers ----------
assert 420 == 2 ** 2 * 3 * 5 * 7 and (3 * 2 * 2 * 2) == 24
assert sum(1 for i in range(1, 421) if 420 % i == 0) == 24
assert 2 ** 6 * 3 ** 4 == 5184 and sum(1 for i in range(1, 5185) if 5184 % i == 0) == 35
assert sum(1 for i in range(1, 5185) if 5184 % i == 0 and isqrt(i) ** 2 == i) == 12
assert 90 == 2 * 3 ** 2 * 5 and (1 + 2) * (1 + 3 + 9) * (1 + 5) == 234
assert sum(i for i in range(1, 91) if 90 % i == 0) == 234
assert 90 // 5 + 90 // 25 == 21
assert 150 // 7 + 150 // 49 == 24
assert 48 == 2 ** 4 * 3 and sum(1 for i in range(1, 49) if 48 % i == 0) == 10
assert 720 == 2 ** 4 * 3 ** 2 * 5 and sum(1 for i in range(1, 721) if 720 % i == 0) == 30
assert 3600 == 2 ** 4 * 3 ** 2 * 5 ** 2 and sum(1 for i in range(1, 3601) if 3600 % i == 0) == 45
assert sum(1 for i in range(1, 3601) if 3600 % i == 0 and i % 2 == 1) == 9
assert sum(1 for i in range(1, 3601) if 3600 % i == 0 and i % 2 == 0) == 36
assert 1440 // 12 == 120 == 2 ** 3 * 3 * 5
assert sum(1 for i in range(1, 121) if 120 % i == 0) == 16
assert (1 + 2 + 4 + 8) * (1 + 3 + 9) * (1 + 5) == 1170
assert sum(i for i in range(1, 361) if 360 % i == 0) == 1170
assert 12 ** 3 == 1728 == 1 * 2 * 3 * 4 * 6 * 12
assert 125 // 5 + 125 // 25 + 125 // 125 == 31
assert 100 // 3 + 100 // 9 + 100 // 27 + 100 // 81 == 48
_p2 = 50 // 2 + 50 // 4 + 50 // 8 + 50 // 16 + 50 // 32
_p3 = 50 // 3 + 50 // 9 + 50 // 27
assert (_p2, _p3) == (47, 22) and min(_p2 // 2, _p3) == 22
assert 360 == 2 ** 3 * 3 ** 2 * 5
assert sum(1 for i in range(1, 361) if 360 % i == 0 and i % 2 == 0) == 18 == 3 * 3 * 2
assert (1 + 2 + 4 + 8) * (1 + 3 + 9) == 195
assert 1000 // 5 + 1000 // 25 + 1000 // 125 + 1000 // 625 == 249

# ---------- ns-fractions-decimals: verified numbers ----------
assert F(48, 90) == F(8, 15)
assert F(7, 9) + F(3, 9) + F(2, 9) == F(12, 9) == F(4, 3)
assert F(27, 150) == F(9, 50) and 50 == 2 * 5 ** 2 and F(9, 50) == F(18, 100)
assert 8 * 21 < 13 * 13 and 8 * 21 == 168 and 13 * 13 == 169
assert 48 * 5 % 2 == 0 and 48 * 5 // 2 == 120 and 120 * 3 % 4 == 0 and 120 * 3 // 4 == 90
assert F(72, 99) == F(8, 11)
assert F(47 - 4, 90) == F(43, 90) and 2 + F(43, 90) == F(223, 90)
assert 13 * 11 == 143 and 9 * 17 == 153 and 143 < 153
assert F(3, 5) - F(1, 4) == F(7, 20) and 63 * 20 % 7 == 0 and 63 * 20 // 7 == 180
assert F(245 - 2, 990) == F(27, 110)
assert F(1, 18) < F(1, 14) < F(1, 12) < F(2, 21)
assert 80 == 2 ** 4 * 5


def pat(pid, name, freq, spot, formula, steps, why, q, ex_steps, answer):
    return {
        "id": pid,
        "name": name,
        "frequency": freq,
        "howToSpot": spot,
        "formula": formula,
        "steps": steps,
        "why": why,
        "example": {"q": q, "steps": ex_steps, "answer": answer},
    }


# ================= subtopic: ns-types-counting =================

TC_CONCEPT = (
    "Numbers come in families: natural, whole, integers, rational and irrational. "
    "A prime has exactly two factors, and co-prime numbers share only the factor 1. "
    "This subtopic also covers place value, counting multiples in a range, sums of "
    "standard series, and reversed two-digit numbers."
)

TC_NOTES = r"""Every number in the exam belongs to one or more families. This lesson covers the families, prime and co-prime numbers, place value, counting multiples in a range, sums of standard series, page numbering, and reversed two-digit numbers. These are quick one-mark questions, so speed matters most.

### The number families

| Family | Members | Watch point |
|---|---|---|
| Natural | $1, 2, 3, \ldots$ | $0$ is not natural |
| Whole | $0, 1, 2, \ldots$ | smallest whole number is $0$ |
| Integers | $\ldots, -2, -1, 0, 1, 2, \ldots$ | $0$ is neither positive nor negative |
| Rational | $\dfrac{p}{q}$ with $q \ne 0$ | terminating and repeating decimals qualify |
| Irrational | never ends, never repeats | $\sqrt{2}$ and $\pi$; sums can still be rational |
| Real | rational and irrational together | every point on the number line |

> **Watch:** $0$ is whole but not natural, and $1$ is neither prime nor composite. Both lines appear as free marks.

### Prime, composite and co-prime
A prime has exactly two factors: $1$ and itself. A composite number has more than two factors. $2$ is the only even prime, and there are $25$ primes below $100$. Co-prime numbers share only the factor $1$: $8$ and $15$ are co-prime though neither is prime. Consecutive integers are always co-prime.

To test whether a number is prime, divide it by every prime up to its square root. For $221$ the square root is below $15$, and $221 = 13 \times 17$, so it is composite.

### Place value and face value
The face value of a digit is the digit itself. The place value is the digit times the value of its position. In $5,63,847$ the digit $6$ sits in the ten-thousands place, so its place value is $6 \times 10000 = 60000$ while its face value is $6$.

> **Rule:** Place value $-$ face value $=$ digit $\times$ (position value $- 1$). For $8$ in $9,28,475$: $8 \times 9999 = 79992$.

### Counting multiples in a range
Multiples of $k$ up to $n$ number exactly the whole-number part of $n \div k$. For a range, count up to the end and subtract the count before the start.

> **Rule:** Multiples of $k$ from $a$ to $b$ = $\left\lfloor \dfrac{b}{k} \right\rfloor - \left\lfloor \dfrac{a-1}{k} \right\rfloor$. Multiples of $7$ from $100$ to $300$: $42 - 14 = 28$.

Read the joining word with care. "Divisible by $4$ and $6$" means divisible by $\mathrm{LCM}(4, 6) = 12$, not by $24$. "Divisible by $4$ or $6$" adds the two counts and subtracts the multiples of $12$. "Neither" takes the total minus the "or" count.

### Sums of common series

| Series | Sum |
|---|---|
| $1 + 2 + \cdots + n$ | $\dfrac{n(n+1)}{2}$ |
| $1^2 + 2^2 + \cdots + n^2$ | $\dfrac{n(n+1)(2n+1)}{6}$ |
| $1^3 + 2^3 + \cdots + n^3$ | $\left[\dfrac{n(n+1)}{2}\right]^2$ |
| first $n$ odd numbers | $n^2$ |
| first $n$ even numbers | $n(n+1)$ |

For a sum that starts late, find the full sum and subtract the missing head. For $11^2$ to $20^2$: the sum up to $20$ is $2870$, the sum up to $10$ is $385$, and the answer is $2485$.

> **Tip:** Any evenly spaced list sums to: number of terms $\times$ (first $+$ last) $\div 2$. Evens from $12$ to $48$: $19$ terms, sum $19 \times 30 = 570$.

### Digits used in page numbering
Pages $1$ to $9$ use $9$ digits. Pages $10$ to $99$ use $90 \times 2 = 180$ digits. Each later page uses as many digits as it has. For $350$ pages: $9 + 180 + 251 \times 3 = 942$ digits. The reverse question subtracts $189$, divides by $3$, and adds $99$ to the quotient.

### Two-digit numbers and their reverse
Write the number as $10a + b$; its reverse is $10b + a$. Their difference is $9(a - b)$ and their sum is $11(a + b)$. A number that exceeds its reverse by $27$ has digits differing by $27 \div 9 = 3$. For example $74$ and $47$ differ by $27$.
"""

TC_FORMULAS = [
    {"name": "Multiples of k up to n", "tex": r"\left\lfloor \dfrac{n}{k} \right\rfloor", "note": ""},
    {"name": "Multiples of k from a to b", "tex": r"\left\lfloor \dfrac{b}{k} \right\rfloor - \left\lfloor \dfrac{a-1}{k} \right\rfloor", "note": ""},
    {"name": "Inclusion-exclusion", "tex": r"n(A \cup B) = n(A) + n(B) - n(A \cap B)", "note": "the overlap holds multiples of the LCM"},
    {"name": "Sum of first n natural numbers", "tex": r"\dfrac{n(n+1)}{2}", "note": ""},
    {"name": "Sum of squares", "tex": r"1^2 + 2^2 + \cdots + n^2 = \dfrac{n(n+1)(2n+1)}{6}", "note": ""},
    {"name": "Sum of cubes", "tex": r"1^3 + 2^3 + \cdots + n^3 = \left[\dfrac{n(n+1)}{2}\right]^2", "note": ""},
    {"name": "First n odd or even numbers", "tex": r"1 + 3 + \cdots + (2n-1) = n^2, \quad 2 + 4 + \cdots + 2n = n(n+1)", "note": ""},
    {"name": "Any arithmetic series", "tex": r"S = \dfrac{n}{2}(a + l)", "note": "terms times average of first and last"},
    {"name": "Digit reversal", "tex": r"(10a + b) - (10b + a) = 9(a - b), \quad (10a + b) + (10b + a) = 11(a + b)", "note": ""},
]

TC_TRICKS = [
    {
        "title": "Floor-division counting",
        "body": "Count multiples of k up to the end of the range, then subtract the multiples before the start. No listing needed.",
        "example": {
            "q": "How many numbers from 100 to 500 are divisible by 17?",
            "steps": [
                r"Up to $500$: $\left\lfloor \dfrac{500}{17} \right\rfloor = 29$.",
                r"Below $100$: $\left\lfloor \dfrac{99}{17} \right\rfloor = 5$.",
                r"Answer: $29 - 5 = 24$.",
            ],
            "answer": "24",
        },
    },
    {
        "title": "Place value in one product",
        "body": "Place value minus face value equals digit times (position value minus 1). The 9999 pattern does it in one line.",
        "example": {
            "q": "Find the difference between the place value and the face value of 8 in 9,28,475.",
            "steps": [
                r"Digit $8$ sits in the ten-thousands place: place value $= 8 \times 10000 = 80000$.",
                r"Difference $= 8 \times (10000 - 1) = 8 \times 9999 = 79992$.",
            ],
            "answer": "79992",
        },
    },
    {
        "title": "Middle term times count",
        "body": "For any evenly spaced list, the sum equals the number of terms times the middle term. The middle term is the average of first and last.",
        "example": {
            "q": "Find the sum of all even numbers from 12 to 48.",
            "steps": [
                r"Count: $\dfrac{48 - 12}{2} + 1 = 19$ terms.",
                r"Average $= \dfrac{12 + 48}{2} = 30$.",
                r"Sum $= 19 \times 30 = 570$.",
            ],
            "answer": "570",
        },
    },
]

TC_MISTAKES = [
    {
        "wrong": "Counting the end points when the question says between.",
        "right": "Between 1 and 100 means 2 to 99. From 1 to 100 includes both ends.",
    },
    {
        "wrong": "Treating 1 as a prime number.",
        "right": "1 is neither prime nor composite, and 2 is the only even prime.",
    },
    {
        "wrong": "In 'divisible by 3 or 5' questions, adding both counts and stopping.",
        "right": "Add both counts, then subtract the multiples of 15 once.",
    },
    {
        "wrong": "Using the sum formula for a series that starts away from 1.",
        "right": "Find the full sum up to the end, then subtract the sum before the start.",
    },
    {
        "wrong": "Reading 'divisible by 4 and 6' as divisible by 24.",
        "right": "It means divisible by LCM(4, 6) = 12. Join 'and' divisors through their LCM.",
    },
]

TC_REVISION = [
    r"Multiples of $k$ from $a$ to $b$: $\left\lfloor \dfrac{b}{k} \right\rfloor - \left\lfloor \dfrac{a-1}{k} \right\rfloor$.",
    r"'And' means the LCM; 'or' means add counts and subtract the LCM count.",
    r"Sum formulas: $\dfrac{n(n+1)}{2}$, $\dfrac{n(n+1)(2n+1)}{6}$, $\left[\dfrac{n(n+1)}{2}\right]^2$, $n^2$ for odd numbers.",
    r"Place value $-$ face value $=$ digit $\times$ (position value $- 1$).",
    r"Reversal: difference $= 9(a-b)$, sum $= 11(a+b)$.",
    r"$0$ is whole but not natural; $1$ is neither prime nor composite.",
]

TC_PATTERNS = [
    pat(
        "ns-tc-p1", "Counting numbers divisible by k in a range", "very common",
        r"A range is given and the question asks how many numbers in it are divisible by one or two given numbers. Words like and, or, neither or but not decide the method.",
        r"\left\lfloor \dfrac{b}{k} \right\rfloor - \left\lfloor \dfrac{a-1}{k} \right\rfloor",
        [
            r"For one divisor $k$: count multiples up to the end, then subtract the multiples before the start.",
            r"For 'by $x$ and $y$': count with $k = \mathrm{LCM}(x, y)$ instead of $x \times y$.",
            r"For 'by $x$ or $y$': add both counts, then subtract the count of the LCM once.",
            r"For 'neither': subtract the 'or' count from the size of the range.",
        ],
        r"Every k-th number is a multiple of k, so floor division counts them without any listing.",
        r"How many numbers from 1 to 300 are divisible by 4 or 6?",
        [
            r"By 4: $300 \div 4$ gives 75. By 6: $300 \div 6$ gives 50.",
            r"Both: multiples of $\mathrm{LCM}(4, 6) = 12$, and $300 \div 12 = 25$.",
            r"$75 + 50 - 25 = 100$.",
        ],
        "100",
    ),
    pat(
        "ns-tc-p2", "Sum of a series or of multiples in a range", "very common",
        r"The question asks for a sum: all two-digit multiples of a number, squares from one point to another, or the first n odd numbers.",
        r"S = \dfrac{n}{2}(a + l), \quad n = \dfrac{l - a}{d} + 1",
        [
            r"Count the terms: for multiples of $d$ from $a$ to $l$, the count is $\dfrac{l - a}{d} + 1$.",
            r"Add the first and last terms and halve the total to get the average.",
            r"Multiply: sum $=$ count $\times$ average.",
            r"For squares or cubes, take the full sum formula and subtract the head you do not need.",
        ],
        r"Pairing first with last, second with second-last, and so on gives equal totals, so the sum is the count times the average.",
        r"Find the sum of all two-digit multiples of 7.",
        [
            r"First two-digit multiple: $14$. Last: $98$.",
            r"Count: $\dfrac{98 - 14}{7} + 1 = 13$ terms.",
            r"Sum $= \dfrac{13 \times (14 + 98)}{2} = 13 \times 56 = 728$.",
        ],
        "728",
    ),
    pat(
        "ns-tc-p3", "Place value and face value", "common",
        r"A number is written with Indian commas and the question asks for the place value, the face value, or a combination of both for one digit.",
        r"\text{place value} = \text{digit} \times 10^{\text{position}}",
        [
            r"Mark positions from the right: ones, tens, hundreds, thousands, ten-thousands, lakhs.",
            r"Place value $=$ digit $\times$ that position's value. Face value $=$ the digit itself.",
            r"Do the asked operation: sum, difference or product.",
        ],
        r"Our system is positional, so the same digit is worth ten times more in each step to the left.",
        r"Find the difference between the place value and the face value of 5 in 8,45,327.",
        [
            r"Digit $5$ is in the thousands place: place value $= 5 \times 1000 = 5000$.",
            r"Face value $= 5$.",
            r"Difference $= 5000 - 5 = 4995$.",
        ],
        "4995",
    ),
    pat(
        "ns-tc-p4", "Classifying numbers: prime, rational, co-prime", "common",
        r"Options list numbers and the question asks which one is prime, rational, irrational, or co-prime with another.",
        None,
        [
            r"Test primes by dividing by every prime up to the square root of the number.",
            r"Simplify before classifying: a product of surds can collapse to a rational number.",
            r"Co-prime just needs HCF 1; neither number has to be prime.",
        ],
        r"A number is irrational only if its simplified value still has a decimal that never ends and never repeats.",
        r"Is 407 a prime number?",
        [
            r"$\sqrt{407}$ is just above $20$, so test primes up to $20$.",
            r"$407 = 11 \times 37$.",
            r"Two factors besides 1, so it is composite.",
        ],
        "No, 407 = 11 x 37",
    ),
    pat(
        "ns-tc-p5", "Digits used in page numbering", "common",
        r"The question asks how many digits a book of N pages needs, or gives the digit count and asks for the pages.",
        r"9 + 180 + 3(N - 99) \text{ for } 100 \le N \le 999",
        [
            r"Pages 1 to 9 use 9 digits at one digit each.",
            r"Pages 10 to 99 use $90 \times 2 = 180$ digits.",
            r"Pages beyond 99 use one digit per digit of the page number; multiply and add.",
            r"For the reverse question, strip 9 and 180 first, then divide what remains.",
        ],
        r"Each block of page numbers has a fixed digit length, so the count splits into three clean parts.",
        r"How many digits are used to number the pages of a 200-page book?",
        [
            r"Single-digit pages: $9$ digits.",
            r"Two-digit pages: $90 \times 2 = 180$ digits.",
            r"Pages 100 to 200: $101 \times 3 = 303$ digits.",
            r"Total: $9 + 180 + 303 = 492$.",
        ],
        "492",
    ),
    pat(
        "ns-tc-p6", "Two-digit numbers and digit reversal", "very common",
        r"The digits of a two-digit number are reversed and the number changes by a known amount, or consecutive numbers are summed.",
        r"(10a + b) - (10b + a) = 9(a - b), \quad (10a + b) + (10b + a) = 11(a + b)",
        [
            r"Write the number as $10a + b$ with $a$ the tens digit and $b$ the units digit.",
            r"A reversal difference divided by 9 gives the digit difference $a - b$.",
            r"A reversal sum divided by 11 gives the digit sum $a + b$.",
            r"For consecutive numbers, divide the sum by the count to get the middle number.",
        ],
        r"The tens digit is worth ten times the units digit, so a swap moves 9 per unit of digit difference.",
        r"A two-digit number exceeds the number formed by reversing its digits by 27. What is the difference between its digits?",
        [
            r"Difference $= 9(a - b) = 27$.",
            r"$a - b = 27 \div 9 = 3$.",
            r"Example: $74 - 47 = 27$.",
        ],
        "3",
    ),
]


# ================= subtopic: ns-divisibility =================

DV_CONCEPT = (
    "A number is divisible by d when d divides it with remainder 0. Quick tests exist "
    "for 2, 3, 4, 5, 8, 9, 10 and 11, and composite divisors split into co-prime parts. "
    "Powers follow their own rules: a to the n minus b to the n is always divisible by "
    "a minus b."
)

DV_NOTES = r"""A number $N$ is divisible by $d$ when $d$ divides $N$ exactly, leaving remainder $0$. Divisibility tests let you check this without long division. This lesson covers the basic tests, composite divisors, missing digits, power rules, and reaching the nearest multiple.

### The quick tests

| Divisor | Test | Example |
|---|---|---|
| $2, 5, 10$ | last digit even, $0$ or $5$, $0$ | $4,215$ by $5$ |
| $4$ | last two digits divisible by $4$ | $7,316 \to 16$ |
| $8$ | last three digits divisible by $8$ | $91,224 \to 224$ |
| $3, 9$ | digit sum divisible by $3$ or $9$ | $6,453 \to 18$ |
| $11$ | odd-place sum minus even-place sum is $0$ or a multiple of $11$ | see below |
| $7, 11, 13$ | alternating sum of three-digit blocks | $276,276 \to 276 - 276 = 0$ |

> **Rule:** For $11$, number the digits from the right. Take (odd-place sum) $-$ (even-place sum). For $948475$: odd places $5 + 4 + 4 = 13$, even places $7 + 8 + 9 = 24$, and $24 - 13 = 11$, so it is divisible by $11$.

### Composite divisors split into co-prime parts
There is no direct rule of $72$. Split the divisor into parts that share no factor, then check each part. Useful splits: $12 = 3 \times 4$, $24 = 3 \times 8$, $36 = 4 \times 9$, $72 = 8 \times 9$, $88 = 8 \times 11$, $99 = 9 \times 11$.

> **Watch:** Never split $24$ as $4 \times 6$. They share the factor $2$: the number $36$ passes both tests yet leaves remainder $12$ with $24$.

### Missing digit questions
When digits are hidden as $x$ and $y$, use the rule with the fewest choices first. The rule of $8$ pins the last three digits. The rule of $11$ gives one equation, the digit sum for $9$ gives another. Several pairs may work, but the asked quantity, usually $x + y$, stays the same in every valid pair.

### Divisibility of powers
Three rules cover almost every power question:

- $a^n - b^n$ is divisible by $a - b$ for every $n$.
- $a^n - b^n$ is divisible by $a + b$ when $n$ is even.
- $a^n + b^n$ is divisible by $a + b$ when $n$ is odd.

So $29^{18} - 15^{18}$ is divisible by both $29 - 15 = 14$ and $29 + 15 = 44$, and $17^{25} + 23^{25}$ is divisible by $40$ because $25$ is odd.

For sums of powers of one base, pull out the smallest power: $3^{25} + 3^{26} + 3^{27} = 3^{25}(1 + 3 + 9) = 3^{25} \times 13$.

### Special digit patterns
- A six-digit number written as a repeated three-digit block, like $276276$, equals $\overline{abc} \times 1001$, and $1001 = 7 \times 11 \times 13$.
- A three-digit number with equal digits, like $777 = 7 \times 111$, is divisible by $37$.
- A two-digit number plus its reverse equals $11(a + b)$; the difference is $9(a - b)$.
- The product of three consecutive integers is divisible by $6$.

### Divisibility by seven
Cut the last digit, double it, and subtract from what remains. Repeat until the number is small. If the result is divisible by $7$, so was the original: $3598 \to 359 - 16 = 343 = 7 \times 49$.

### Reaching the nearest multiple
To make $N$ divisible by $d$, divide and find the remainder $r$. Subtract $r$ to go down to the lower multiple, or add $d - r$ to go up. For $8357 \div 12$ the remainder is $5$, so adding $7$ gives $8364 = 12 \times 697$.

> **Example:** Largest four-digit multiple of a divisor: take $9999$, divide, and subtract the remainder from $9999$.
"""

DV_FORMULAS = [
    {"name": "Divisibility by 11", "tex": r"\left(\sum \text{odd-place digits}\right) - \left(\sum \text{even-place digits}\right) \in \{0, \pm 11, \pm 22, \ldots\}", "note": ""},
    {"name": "Composite divisor", "tex": r"pq \mid N \iff p \mid N \text{ and } q \mid N, \quad \gcd(p, q) = 1", "note": "split into co-prime parts only"},
    {"name": "Difference of powers", "tex": r"(a - b) \mid (a^n - b^n) \text{ for all } n", "note": ""},
    {"name": "Difference of even powers", "tex": r"(a + b) \mid (a^n - b^n) \text{ when } n \text{ is even}", "note": ""},
    {"name": "Sum of odd powers", "tex": r"(a + b) \mid (a^n + b^n) \text{ when } n \text{ is odd}", "note": ""},
    {"name": "Repeated block", "tex": r"\overline{abcabc} = \overline{abc} \times 1001 = \overline{abc} \times 7 \times 11 \times 13", "note": ""},
    {"name": "Divisibility by seven", "tex": r"N \to \left\lfloor \dfrac{N}{10} \right\rfloor - 2 \times (N \bmod 10)", "note": "repeat until small"},
]

DV_TRICKS = [
    {
        "title": "Split into co-prime factors",
        "body": "Break the divisor into parts with no common factor and test each part separately. Order the tests from the most restrictive first.",
        "example": {
            "q": "If the five-digit number 37x84 is divisible by 12, find the smallest value of x.",
            "steps": [
                r"$12 = 3 \times 4$. By $4$: last two digits $84$ already pass, for any $x$.",
                r"By $3$: digit sum $3 + 7 + x + 8 + 4 = 22 + x$ must be a multiple of $3$.",
                r"So $x \in \{2, 5, 8\}$ and the smallest is $2$.",
            ],
            "answer": "2",
        },
    },
    {
        "title": "The repeated-block family",
        "body": "Any six-digit number abcabc equals abc times 1001, so it is always divisible by 7, 11 and 13.",
        "example": {
            "q": "Which of 7, 11 and 13 divide 484484?",
            "steps": [
                r"$484484 = 484 \times 1001$.",
                r"$1001 = 7 \times 11 \times 13$.",
                r"All three divide it.",
            ],
            "answer": "All of 7, 11 and 13",
        },
    },
    {
        "title": "Sum of odd powers",
        "body": "For a to the n plus b to the n with odd n, check the options against a plus b first. No expansion is ever needed.",
        "example": {
            "q": "Is 17 to the power 25 plus 23 to the power 25 divisible by 40?",
            "steps": [
                r"The exponent $25$ is odd, so $a^n + b^n$ is divisible by $a + b$.",
                r"$17 + 23 = 40$.",
                r"Yes, exactly divisible by $40$.",
            ],
            "answer": "Yes",
        },
    },
]

DV_MISTAKES = [
    {
        "wrong": "Splitting a composite divisor into parts that share a factor, like 12 = 2 x 6.",
        "right": "Use co-prime parts only: 12 = 3 x 4. A number can pass 2 and 6 yet fail 12.",
    },
    {
        "wrong": "Checking only the last two digits for divisibility by 8.",
        "right": "The rule of 8 needs the last three digits.",
    },
    {
        "wrong": "For 11, forgetting that the difference of the two sums can be 0 or negative.",
        "right": "Accept 0, 11, 22 and also -11 as valid differences.",
    },
    {
        "wrong": "Using the (a + b) rule for a to the n plus b to the n when n is even.",
        "right": "That rule needs odd n. For even n only a minus b divides the difference.",
    },
    {
        "wrong": "Multiplying the two rules' answers instead of checking both divisibilities.",
        "right": "For 72 = 8 x 9 the number must pass both tests; nothing is multiplied.",
    },
]

DV_REVISION = [
    r"Last digit tests $2, 5, 10$; last two digits for $4$; last three for $8$.",
    r"Digit sum tests $3$ and $9$; alternating sums test $11$.",
    r"Composite divisor: split into co-prime parts and test each part.",
    r"$(a-b)$ always divides $a^n - b^n$; $(a+b)$ divides it when $n$ is even; $(a+b)$ divides $a^n + b^n$ when $n$ is odd.",
    r"$\overline{abcabc} = \overline{abc} \times 7 \times 11 \times 13$.",
    r"To reach a multiple: add $d - r$ or subtract $r$.",
]

DV_PATTERNS = [
    pat(
        "ns-dv-p1", "Missing digits for a composite divisor", "very common",
        r"A number with blanks x and y is said to be divisible by 72, 88, 99 or 36, and the options are values of x + y or x - y.",
        r"72 = 8 \times 9,\quad 88 = 8 \times 11,\quad 99 = 9 \times 11",
        [
            r"Split the divisor into co-prime factors.",
            r"Apply the rule with fewer choices first: $8$ fixes the last three digits, $11$ gives one equation.",
            r"Feed that result into the second rule, the digit sum for $9$ or the alternating sum for $11$.",
            r"List the working pairs; the asked sum or difference is the same in all of them.",
        ],
        r"A number divisible by two co-prime numbers is divisible by their product, and each rule cuts the possibilities.",
        r"If the five-digit number 6x8y4 is divisible by 72, find x + y.",
        [
            r"$72 = 8 \times 9$. Rule of $8$: the last three digits $8y4$ must divide by $8$.",
            r"$824 = 8 \times 103$ and $864 = 8 \times 108$, so $y = 2$ or $y = 6$.",
            r"Rule of $9$: digit sum $6 + x + 8 + y + 4 = 18 + x + y$ must divide by $9$.",
            r"$y = 2$ forces $x = 7$; $y = 6$ forces $x = 3$. Both give $x + y = 9$.",
        ],
        "9",
    ),
    pat(
        "ns-dv-p2", "Divisibility by 11 with a missing digit", "very common",
        r"A number like 7x2859 is divisible by 11 and one digit is hidden, or the options are numbers to pick from.",
        r"(\text{odd-place sum}) - (\text{even-place sum}) \in \{0, \pm 11, \pm 22, \ldots\}",
        [
            r"Number the digits from the right and add the odd places and the even places separately.",
            r"Subtract the two sums; the result must be $0$ or a multiple of $11$.",
            r"Solve for the missing digit, which must stay between $0$ and $9$.",
        ],
        r"Ten leaves remainder minus one with eleven, so place values flip between plus and minus.",
        r"If the number 7x2859 is divisible by 11, find x.",
        [
            r"From the right, odd places: $9 + 8 + x = 17 + x$. Even places: $5 + 2 + 7 = 14$.",
            r"Difference: $(17 + x) - 14 = 3 + x$ must be $0$ or $11$.",
            r"$3 + x = 11$ gives $x = 8$. Check: $782859 = 11 \times 71169$.",
        ],
        "8",
    ),
    pat(
        "ns-dv-p3", "Divisibility of a power of the form a to the n minus b to the n", "very common",
        r"Two big powers with the same exponent, added or subtracted, and the question asks which listed number divides them.",
        r"(a - b) \mid (a^n - b^n);\quad (a + b) \mid (a^n - b^n) \text{ for even } n;\quad (a + b) \mid (a^n + b^n) \text{ for odd } n",
        [
            r"Note whether the powers are added or subtracted, and whether $n$ is even or odd.",
            r"Compute $a - b$ and $a + b$.",
            r"Match against the options: the difference always works; the sum needs the right parity of $n$.",
        ],
        r"Factoring a to the n minus b to the n exposes both a minus b and, for even n, a plus b.",
        r"29 to the power 18 minus 15 to the power 18 is divisible by which of 14 and 44?",
        [
            r"$n = 18$ is even.",
            r"Divisible by $a - b = 14$ always, and by $a + b = 44$ because $n$ is even.",
            r"So both divide it.",
        ],
        "Both 14 and 44",
    ),
    pat(
        "ns-dv-p4", "Sum of powers of the same base", "common",
        r"A sum like 3 to the 25 plus 3 to the 26 plus 3 to the 27 appears and the question asks what divides it.",
        r"a^m + a^{m+1} + a^{m+2} = a^m(1 + a + a^2)",
        [
            r"Take the smallest power common to every term outside a bracket.",
            r"Add the powers inside the bracket to get one small number.",
            r"The bracket value divides the whole sum.",
        ],
        r"Every term shares the smallest power, and the bracket becomes a plain number.",
        r"Find a number other than a power of 3 that divides 3 to the power 15 plus 3 to the power 16 plus 3 to the power 17.",
        [
            r"Factor: $3^{15}(1 + 3 + 9)$.",
            r"$1 + 3 + 9 = 13$.",
            r"So the sum equals $3^{15} \times 13$ and is divisible by $13$.",
        ],
        "13",
    ),
    pat(
        "ns-dv-p5", "Least number to add or subtract to reach a multiple", "very common",
        r"The question asks what least number must be added to or subtracted from N so the result is divisible by d, or for the largest n-digit multiple.",
        r"\text{add} = d - (N \bmod d), \quad \text{subtract} = N \bmod d",
        [
            r"Divide $N$ by $d$ and note the remainder $r$.",
            r"To go down to the lower multiple, subtract $r$.",
            r"To go up to the next multiple, add $d - r$.",
            r"For the largest n-digit multiple, divide a string of nines and subtract its remainder.",
        ],
        r"Multiples of d sit d apart, and the remainder measures the distance to the lower one.",
        r"What least number must be added to 3286 to make it divisible by 29?",
        [
            r"$3286 = 29 \times 113 + 9$, so the remainder is $9$.",
            r"Add $29 - 9 = 20$.",
            r"Check: $3306 = 29 \times 114$.",
        ],
        "20",
    ),
    pat(
        "ns-dv-p6", "Special forms: repeated blocks and equal digits", "common",
        r"A six-digit number repeats a three-digit block, or a three-digit number has equal digits, and the question asks what always divides it.",
        r"\overline{abcabc} = \overline{abc} \times 7 \times 11 \times 13, \qquad \overline{aaa} = a \times 3 \times 37",
        [
            r"Write the number as its block times a fixed multiplier.",
            r"Factor the multiplier: $1001 = 7 \times 11 \times 13$ and $111 = 3 \times 37$.",
            r"Pick the option that divides the fixed multiplier.",
        ],
        r"The digit pattern builds a fixed multiplier no matter which digits are used.",
        r"Which of 7, 11 and 13 divide 276276?",
        [
            r"$276276 = 276 \times 1001$.",
            r"$1001 = 7 \times 11 \times 13$.",
            r"All three divide it.",
        ],
        "All of 7, 11 and 13",
    ),
    pat(
        "ns-dv-p7", "Divisibility by seven", "occasional",
        r"The divisor 7 appears with a three- or four-digit number, often in an options question asking which numbers divide it.",
        r"N \to \left\lfloor \dfrac{N}{10} \right\rfloor - 2 \times (N \bmod 10)",
        [
            r"Cut the last digit and double it.",
            r"Subtract that from the remaining front part.",
            r"Repeat until the number has two or three digits.",
            r"If the result is divisible by $7$, the original number is too.",
        ],
        r"Removing the last digit maps N to a smaller number with the same remainder apart from a factor, so divisibility survives.",
        r"Is 3598 divisible by 7?",
        [
            r"Cut $8$, double it: $359 - 16 = 343$.",
            r"$343 = 7 \times 49$.",
            r"Yes, divisible by $7$.",
        ],
        "Yes, since 343 = 7 x 49",
    ),
]


# ================= subtopic: ns-remainders =================

RM_CONCEPT = (
    "Every division obeys one formula: dividend = divisor x quotient + remainder, "
    "with the remainder smaller than the divisor. Remainders of sums and products can "
    "be found from the individual remainders, and big powers repeat in cycles."
)

RM_NOTES = r"""When 47 sweets are shared among 5 children, each gets 9 and 2 are left over. Here 47 is the dividend, 5 the divisor, 9 the quotient and 2 the remainder. The remainder is always smaller than the divisor. Every question in this lesson is built on that one idea.

### The division formula
$$\text{dividend} = \text{divisor} \times \text{quotient} + \text{remainder}$$

With divisor 24, quotient 13 and remainder 17, the dividend is $24 \times 13 + 17 = 329$. Questions that give two of the four quantities in words are asking for this formula.

> **Rule:** Write the formula first, fill in what is given, and solve for the missing piece. Check that the remainder stays below the divisor.

### Remainders add and multiply
The remainder of a sum or a product equals the remainder of the sum or product of the individual remainders. Replace each big number by its remainder first, then multiply small numbers.

For $(1021 \times 1023 \times 1025) \div 17$: the remainders are $1$, $3$ and $5$, and $1 \times 3 \times 5 = 15$, so the remainder is $15$.

### Negative remainders keep numbers small
A remainder may be written as a negative number. $98$ leaves $-1$ with $99$, and $97$ leaves $-2$. So $98 \times 97 \times 96$ leaves $(-1)(-2)(-3) = -6$, and adding the divisor gives $93$.

> **Tip:** If your final remainder is negative, add the divisor once. If it is still negative, add again.

### Big powers cycle
Powers repeat their remainders. Find a small power that leaves $1$ or $-1$, then split the exponent.

- $2^3 = 8$ leaves $1$ with $7$, so $2^{100} = (2^3)^{33} \times 2$ leaves $2$.
- A base one more than the divisor always leaves $1$.
- A base one less than the divisor leaves $1$ for even powers and $d - 1$ for odd powers.
- Fermat: for a prime $p$ that does not divide the base, $a^{p-1}$ leaves $1$ with $p$.

### When the new divisor divides the old
If $N$ leaves $r$ with divisor $D$, and the new divisor $d$ is a factor of $D$, then $N$ leaves $r \bmod d$ with $d$. Since $342 = 18 \times 19$, a remainder of $47$ with $342$ means remainders $11$ with $18$ and $9$ with $19$.

> **Watch:** This works one way only. Knowing the remainder with $d$ tells you nothing about the remainder with $D$.

### Dividing successively
'Divided successively by 4 and 5 leaving remainders 1 and 2' means: divide $N$ by $4$, then divide that quotient by $5$. Rebuild from the last step: the smallest final quotient is $0$, so the middle value is $0 \times 5 + 2 = 2$ and $N = 4 \times 2 + 1 = 9$.

### Factorial sums collapse early
From $5! = 120$ onwards every factorial is a multiple of $15$. So for $1! + 2! + \cdots + 50!$ divided by $15$, only $1 + 2 + 6 + 24 = 33$ matters, and the remainder is $3$.

> **Example:** A number leaves remainder 5 with 9. Then $4N$ leaves $4 \times 5 = 20$, and $20 \bmod 9 = 2$.
"""

RM_FORMULAS = [
    {"name": "Division algorithm", "tex": r"N = d \times q + r, \quad 0 \le r < d", "note": ""},
    {"name": "Product rule", "tex": r"\mathrm{rem}\left(\dfrac{a \times b}{d}\right) = \mathrm{rem}\left(\dfrac{R_a \times R_b}{d}\right)", "note": "same for sums"},
    {"name": "Fermat's little theorem", "tex": r"a^{p-1} \equiv 1 \pmod{p}, \quad p \text{ prime}, \ \gcd(a, p) = 1", "note": ""},
    {"name": "Divisor-multiple rule", "tex": r"N \equiv r \pmod{D},\ d \mid D \ \Rightarrow\ N \equiv r \pmod{d}", "note": "one-way rule"},
    {"name": "Base one more than divisor", "tex": r"(ad + 1)^n \equiv 1 \pmod{d}", "note": ""},
    {"name": "Base one less than divisor", "tex": r"(ad - 1)^n \equiv (-1)^n \pmod{d}", "note": "1 if n even, d - 1 if n odd"},
]

RM_TRICKS = [
    {
        "title": "Make the base plus or minus one",
        "body": "Write the base as (multiple of divisor) plus or minus 1. The whole power then collapses to plus or minus 1.",
        "example": {
            "q": "Find the remainder when 15 to the power 47 is divided by 16.",
            "steps": [
                r"$15 = 16 - 1$, so $15 \equiv -1 \pmod{16}$.",
                r"$15^{47} \equiv (-1)^{47} = -1$.",
                r"Add the divisor: $16 - 1 = 15$.",
            ],
            "answer": "15",
        },
    },
    {
        "title": "Negative remainders for products",
        "body": "When factors sit just below the divisor, replace each by a small negative remainder and multiply those.",
        "example": {
            "q": "Find the remainder when 98 x 97 x 96 is divided by 99.",
            "steps": [
                r"Remainders: $-1$, $-2$, $-3$.",
                r"Product: $(-1)(-2)(-3) = -6$.",
                r"Add the divisor: $99 - 6 = 93$.",
            ],
            "answer": "93",
        },
    },
    {
        "title": "Divisor is a factor, just reduce",
        "body": "If the new divisor divides the old one, reduce the old remainder by the new divisor. If it does not divide it, this shortcut is not available.",
        "example": {
            "q": "A number leaves remainder 29 when divided by 56. What is the remainder when it is divided by 8?",
            "steps": [
                r"$56 = 8 \times 7$, so $8$ is a factor of $56$.",
                r"$29 \bmod 8 = 5$.",
                r"Remainder $5$.",
            ],
            "answer": "5",
        },
    },
]

RM_MISTAKES = [
    {
        "wrong": "Leaving a negative remainder as the final answer.",
        "right": "Add the divisor once (or twice) until the remainder is between 0 and d - 1.",
    },
    {
        "wrong": "Using the divisor-multiple rule backwards, from a small divisor to a bigger one.",
        "right": "The rule only shrinks: from divisor D to its factor d, never the other way.",
    },
    {
        "wrong": "Applying Fermat when the divisor is not prime or shares a factor with the base.",
        "right": "Fermat needs a prime divisor that does not divide the base.",
    },
    {
        "wrong": "Multiplying the full big numbers before reducing.",
        "right": "Reduce every number to its remainder first, then multiply the small values.",
    },
    {
        "wrong": "Reading successive division as two separate divisions of the same number.",
        "right": "The second division acts on the quotient of the first, so rebuild backwards from the end.",
    },
]

RM_REVISION = [
    r"Dividend $=$ divisor $\times$ quotient $+$ remainder, and $r < d$.",
    r"Reduce each number first, then add or multiply the remainders.",
    r"Negative remainders keep arithmetic small; add the divisor to a negative result.",
    r"$(d+1)^n \to 1$; $(d-1)^n \to 1$ for even $n$, $d-1$ for odd $n$.",
    r"New divisor divides the old: answer is old remainder mod new divisor.",
    r"Successive division: rebuild from the last divisor backwards.",
    r"Factorials from $5!$ on are multiples of $15$, so early terms alone decide.",
]

RM_PATTERNS = [
    pat(
        "ns-rm-p1", "Remainder with a factor of the old divisor", "very common",
        r"A number leaves a remainder with a big divisor, and the question asks for the remainder with a smaller number that divides that divisor.",
        r"N = Dq + r,\ d \mid D \ \Rightarrow\ N \bmod d = r \bmod d",
        [
            r"Check that the new divisor $d$ truly divides the old divisor $D$.",
            r"Divide the old remainder $r$ by $d$.",
            r"The new remainder is $r \bmod d$.",
        ],
        r"The term Dq is a multiple of d, so only r decides the remainder.",
        r"A number leaves remainder 47 when divided by 342. What is the remainder when it is divided by 19?",
        [
            r"$342 = 18 \times 19$, so $19$ is a factor of $342$.",
            r"Reduce the old remainder: $47 \bmod 19$.",
            r"$47 = 2 \times 19 + 9$, so the remainder is $9$.",
        ],
        "9",
    ),
    pat(
        "ns-rm-p2", "Remainder of a product or sum", "very common",
        r"Several large numbers are multiplied or added and the remainder with a modest divisor is asked.",
        r"(a \times b) \bmod d = [(a \bmod d) \times (b \bmod d)] \bmod d",
        [
            r"Replace every number by its remainder; negative remainders are allowed.",
            r"Multiply or add the small remainders.",
            r"Reduce again by $d$, and add $d$ to any negative result.",
        ],
        r"Each number is a multiple of d plus a remainder, and multiples of d never change the remainder.",
        r"Find the remainder when 98 x 97 x 96 is divided by 99.",
        [
            r"Remainders with $99$: $98 \to -1$, $97 \to -2$, $96 \to -3$.",
            r"$(-1)(-2)(-3) = -6$.",
            r"Add the divisor: $99 - 6 = 93$.",
        ],
        "93",
    ),
    pat(
        "ns-rm-p3", "Remainder of a large power", "very common",
        r"A power like 2 to the 95 or 5 to the 70 is divided by a small number, usually 7, 9, 13 or a number near the base.",
        r"a^{p-1} \equiv 1 \pmod p, \qquad (d - 1)^n \equiv (-1)^n \pmod d",
        [
            r"Reduce the base with respect to the divisor.",
            r"Find the smallest power that leaves $1$ or $-1$.",
            r"Split the exponent using that power and keep the leftover part.",
            r"Multiply the leftover remainder by the cycle answer and reduce.",
        ],
        r"Once some power leaves remainder 1, the remainders repeat in a fixed cycle.",
        r"Find the remainder when 2 to the power 95 is divided by 7.",
        [
            r"$2^3 = 8$ leaves $1$ with $7$.",
            r"$95 = 3 \times 31 + 2$, so $2^{95} = (2^3)^{31} \times 2^2$.",
            r"Remainder: $1 \times 4 = 4$.",
        ],
        "4",
    ),
    pat(
        "ns-rm-p4", "Division formula: find the dividend", "common",
        r"The divisor and quotient are described in terms of the remainder, and the dividend is asked.",
        r"\text{dividend} = \text{divisor} \times \text{quotient} + \text{remainder}",
        [
            r"Write every unknown in terms of the one given value, usually the remainder.",
            r"Compute the divisor and the quotient.",
            r"Substitute into the division formula.",
            r"Check the remainder is smaller than the divisor.",
        ],
        r"The formula is the definition of division; everything else is substitution.",
        r"In a division, the quotient is three times the remainder and the divisor is four times the quotient. If the remainder is 5, find the dividend.",
        [
            r"Quotient $= 3 \times 5 = 15$.",
            r"Divisor $= 4 \times 15 = 60$.",
            r"Dividend $= 60 \times 15 + 5 = 905$.",
        ],
        "905",
    ),
    pat(
        "ns-rm-p5", "Remainder of an expression built from N", "common",
        r"The remainder of N with a divisor is given, and the question asks for the remainder of a multiple, square or cube of N.",
        r"N \equiv r \ \Rightarrow\ kN \equiv kr,\ N^2 \equiv r^2, \ N^3 \equiv r^3 \pmod d",
        [
            r"Replace $N$ by its remainder $r$ everywhere in the expression.",
            r"Compute the small expression.",
            r"Reduce by $d$; add $d$ if the result is negative.",
            r"Check with the smallest such $N$, which is $r$ itself.",
        ],
        r"N equals dq + r, and every term containing dq is a multiple of d.",
        r"When N is divided by 11 the remainder is 4. Find the remainder when N cubed plus N is divided by 11.",
        [
            r"Replace $N$ by $4$: $4^3 + 4 = 64 + 4 = 68$.",
            r"$68 \bmod 11$: $68 = 6 \times 11 + 2$.",
            r"Remainder $2$. Check with $N = 15$: $3390 \bmod 11 = 2$.",
        ],
        "2",
    ),
    pat(
        "ns-rm-p6", "Successive division", "occasional",
        r"A number is divided successively by two or three divisors, each acting on the previous quotient, and remainders are given.",
        r"x = d_1 y + r_1, \quad y = d_2 z + r_2",
        [
            r"Start from the last division and take its smallest quotient as $0$.",
            r"Rebuild one step left: value $=$ divisor $\times$ next value $+$ remainder.",
            r"Repeat until you reach the original number.",
            r"Verify by dividing forward again.",
        ],
        r"Successive division is the division formula applied along a chain, so rebuilding runs backwards.",
        r"Find the smallest number which leaves remainders 1 and 2 when divided successively by 4 and 5.",
        [
            r"Second step: quotient $0$, so the middle value is $0 \times 5 + 2 = 2$.",
            r"First step: $4 \times 2 + 1 = 9$.",
            r"Check: $9 \div 4 = 2$ remainder $1$, and $2 \div 5 = 0$ remainder $2$.",
        ],
        "9",
    ),
    pat(
        "ns-rm-p7", "Remainder of a factorial sum", "occasional",
        r"A sum like 1! + 2! + ... + n! is divided by a number such as 15, 12 or 10, and the remainder is asked.",
        None,
        [
            r"Note the divisor: from $5! = 120$ on, every factorial is a multiple of $15$, $10$ and $120$.",
            r"Keep only the factorials that are not multiples of the divisor.",
            r"Add them, reduce by the divisor, and done.",
        ],
        r"A factorial accumulates every smaller factor, so large factorials contain the divisor as a factor.",
        r"Find the remainder when 1! + 2! + 3! + ... + 50! is divided by 15.",
        [
            r"Every term from $5! = 120$ on is a multiple of $15$.",
            r"Add the first four: $1 + 2 + 6 + 24 = 33$.",
            r"$33 \bmod 15 = 3$.",
        ],
        "3",
    ),
]


# ================= subtopic: ns-unit-digit =================

UD_CONCEPT = (
    "The unit digit of a power depends only on the unit digit of the base and on the "
    "exponent's remainder when divided by four. Unit digits of powers repeat in short "
    "cycles, so huge expressions collapse to one digit in seconds."
)

UD_NOTES = r"""The unit digit is the last digit of a number, the ones place. Exams ask for the unit digit of monsters like $7^{105} \times 3^{58}$, numbers far too big to compute. The rescue: the unit digit of a product depends only on the unit digits of the factors. $1237 \times 48$ ends the same way as $7 \times 8 = 56$, that is, in $6$.

### Power cycles
Write out powers of $7$: the unit digits run $7, 9, 3, 1$, then repeat. This repeat length is the cyclicity.

| Base digit | Cycle | Length |
|---|---|---|
| $0, 1, 5, 6$ | never changes | $1$ |
| $4$ | $4, 6$ | $2$ |
| $9$ | $9, 1$ | $2$ |
| $2$ | $2, 4, 8, 6$ | $4$ |
| $3$ | $3, 9, 7, 1$ | $4$ |
| $7$ | $7, 9, 3, 1$ | $4$ |
| $8$ | $8, 4, 2, 6$ | $4$ |

> **Rule:** Divide the exponent by $4$. A remainder of $1$, $2$ or $3$ means use that power; a remainder of $0$ means use the fourth power. For $4$ and $9$, only odd or even matters.

### The method step by step
Take $8^{67}$. Keep the base digit $8$. Divide $67$ by $4$: remainder $3$. The third member of the cycle of $8$ is $2$, so the unit digit is $2$. Only the last two digits of a big exponent matter, because $100$ divides by $4$.

### Products, sums and differences
Find each unit digit first, then combine. For sums, add the digits and keep the last one. For differences, subtract; if the result is negative, add $10$. For $7^{105} - 3^{58}$: the digits are $7$ and $9$, and $7 - 9 = -2$, so the answer is $10 - 2 = 8$.

> **Watch:** The digit-borrow trick for a difference assumes the first number really is the larger one. The question usually ensures this.

### Free wins without cycles
- Any even number times any number ending in $5$ ends in $0$.
- An odd number times a number ending in $5$ ends in $5$.
- Every factorial from $5!$ on ends in $0$. So $1! + 2! + \cdots + 50!$ ends in $3$, from $1 + 2 + 6 + 24 = 33$.

### Power towers
For $7^{21^{20}}$ you need the exponent $21^{20}$ by $4$. Since $21$ leaves $1$ with $4$, so does $21^{20}$, and the unit digit is that of $7^1 = 7$. For $3^{4^5}$, the exponent $4^5$ is a multiple of $4$, so use $3^4$, giving $1$.

> **Tip:** For a tower, reduce the inner exponent first, then apply the outer cycle.

### Last two digits
For a base ending in $1$, like $71$ or $41$: the last digit stays $1$. The tens digit is the last digit of (tens digit of base times the exponent). For $71^{36}$: $7 \times 36 = 252$, keep $2$.
So the ending is $21$. For $41^{27}$: $4 \times 27 = 108$, keep $8$, ending $81$.

> **Example:** $6^{25} + 9^{31}$ ends in $6 + 9 = 15$, so the unit digit is $5$.
"""

UD_FORMULAS = [
    {"name": "Cyclicity rule", "tex": r"\text{unit}(a^n) = \text{unit}(a^r), \quad r = n \bmod 4 \ (r = 0 \Rightarrow r = 4)", "note": ""},
    {"name": "Cycles of two, three, seven, eight", "tex": r"2: 2,4,8,6 \quad 3: 3,9,7,1 \quad 7: 7,9,3,1 \quad 8: 8,4,2,6", "note": ""},
    {"name": "Factorials", "tex": r"n! \equiv 0 \pmod{10} \text{ for } n \ge 5", "note": ""},
    {"name": "Last two digits, base ending in one", "tex": r"(10a + 1)^n \text{ ends in } \left[(a \cdot n) \bmod 10\right] 1", "note": ""},
]

UD_TRICKS = [
    {
        "title": "Last two digits of the exponent",
        "body": "For division by four, only the last two digits of the exponent matter, because 100 is a multiple of 4.",
        "example": {
            "q": "Find the unit digit of 1357 to the power 2463.",
            "steps": [
                r"Base ends in $7$; only $63$ of the exponent matters.",
                r"$63 \bmod 4 = 3$, so use $7^3 = 343$.",
                r"Unit digit $3$.",
            ],
            "answer": "3",
        },
    },
    {
        "title": "Even times five ends in zero",
        "body": "If a product contains an even factor and a factor ending in 5, the unit digit is 0 without any cycle work.",
        "example": {
            "q": "Find the unit digit of 2 to the power 31 x 5 to the power 17 x 3 to the power 9.",
            "steps": [
                r"$2^{31}$ is even; $5^{17}$ ends in $5$.",
                r"Even times a number ending in $5$ ends in $0$.",
                r"The whole product ends in $0$.",
            ],
            "answer": "0",
        },
    },
    {
        "title": "Factorial sums stop at four terms",
        "body": "From 5! on, every factorial ends in 0, so a factorial sum's unit digit comes from the first four terms alone.",
        "example": {
            "q": "Find the unit digit of 1! + 2! + 3! + ... + 50!.",
            "steps": [
                r"Terms from $5!$ on end in $0$.",
                r"$1 + 2 + 6 + 24 = 33$.",
                r"Unit digit $3$.",
            ],
            "answer": "3",
        },
    },
]

UD_MISTAKES = [
    {
        "wrong": "Treating an exponent remainder of 0 as power 0.",
        "right": "Remainder 0 means use the fourth power of the cycle, not power 1.",
    },
    {
        "wrong": "Reducing the exponent mod 4 using only its last digit.",
        "right": "Use the last two digits of the exponent, since 100 is the multiple of 4.",
    },
    {
        "wrong": "Forgetting to borrow ten in a difference of unit digits.",
        "right": "7 minus 9 is negative: add 10 and answer 8.",
    },
    {
        "wrong": "Applying the cycle table to the whole base number.",
        "right": "Only the last digit of the base enters the table.",
    },
]

UD_REVISION = [
    r"Unit digit needs only the base's last digit and $n \bmod 4$.",
    r"Remainder $0$ means use the fourth power.",
    r"$0, 1, 5, 6$ never change; $4$ and $9$ have cycle $2$.",
    r"Even $\times$ ending-5 gives $0$; odd $\times$ ending-5 gives $5$.",
    r"$n!$ for $n \ge 5$ ends in $0$.",
    r"Negative digit difference: add $10$.",
    r"Base ending in $1$: tens digit $= ($base tens $\times$ exponent$) \bmod 10$.",
]

UD_PATTERNS = [
    pat(
        "ns-ud-p1", "Unit digit of a power or a product of powers", "very common",
        r"The question asks for the unit digit of one big power or of a product of two or three powers.",
        r"\text{unit}(a^n) = \text{unit}\left(a^{\,n \bmod 4}\right)",
        [
            r"Keep only the unit digit of each base.",
            r"Reduce each exponent mod $4$; for base digits $4$ and $9$, odd or even is enough.",
            r"Read each unit digit from its cycle.",
            r"Multiply the digits and keep the last one.",
        ],
        r"Unit digits of powers repeat every four steps or fewer, so only the exponent mod four matters.",
        r"Find the unit digit of 4 to the power 63 x 9 to the power 72 x 8 to the power 41.",
        [
            r"$4^{63}$: odd power of $4$ gives $4$. $9^{72}$: even power of $9$ gives $1$.",
            r"$8^{41}$: $41 \bmod 4 = 1$, cycle of $8$ starts at $8$.",
            r"$4 \times 1 \times 8 = 32$: unit digit $2$.",
        ],
        "2",
    ),
    pat(
        "ns-ud-p2", "Unit digit of a sum or difference of powers", "common",
        r"Powers joined by plus or minus, like 7 to the 105 minus 3 to the 58.",
        None,
        [
            r"Find the unit digit of each power separately.",
            r"Add or subtract those digits.",
            r"Keep the last digit; if a difference is negative, add $10$.",
        ],
        r"Carrying and borrowing never change the ones place beyond what the unit digits show.",
        r"Find the unit digit of 7 to the power 105 minus 3 to the power 58.",
        [
            r"$7^{105}$: $105 \bmod 4 = 1$, digit $7$.",
            r"$3^{58}$: $58 \bmod 4 = 2$, digit $9$.",
            r"$7 - 9 = -2$, add $10$: digit $8$.",
        ],
        "8",
    ),
    pat(
        "ns-ud-p3", "Unit digit of long products and factorial sums", "common",
        r"A product of many plain numbers, a product like 1 x 3 x 5 x ..., or a factorial sum 1! + 2! + ... + n!.",
        None,
        [
            r"Scan for an even factor together with a factor ending in $5$: answer $0$ at once.",
            r"For factorial sums, drop every term from $5!$ on.",
            r"Otherwise multiply unit digits step by step, keeping the last digit.",
        ],
        r"Two times five makes a ten, and a trailing zero survives every further multiplication.",
        r"Find the unit digit of 2 to the power 31 x 5 to the power 17 x 3 to the power 9.",
        [
            r"$2^{31}$ is even, and $5^{17}$ ends in $5$.",
            r"Their product ends in $0$.",
            r"Whatever multiplies it, the unit digit stays $0$.",
        ],
        "0",
    ),
    pat(
        "ns-ud-p4", "Power towers", "occasional",
        r"The exponent is itself a power, as in 7 to the power 21 to the power 20.",
        r"a^{b^c}: \text{reduce } b^c \bmod 4 \text{ first}",
        [
            r"Reduce the inner power modulo $4$.",
            r"Use that remainder on the cycle of the base digit.",
            r"If the inner base is even, its power is usually a multiple of $4$: use the fourth power.",
        ],
        r"Only the exponent's position in the four-cycle matters, whatever its size.",
        r"Find the unit digit of 7 to the power 21 to the power 20.",
        [
            r"$21 \equiv 1 \pmod 4$, so $21^{20} \equiv 1 \pmod 4$.",
            r"Use $7^1$.",
            r"Unit digit $7$.",
        ],
        "7",
    ),
    pat(
        "ns-ud-p5", "Last two digits of a power", "occasional",
        r"The question asks for the last two digits of a power whose base ends in 1, such as 71 or 41.",
        r"(10a + 1)^n \text{ ends in } \left[(a \cdot n) \bmod 10\right] 1",
        [
            r"Confirm the base ends in $1$; the last digit of the answer is $1$.",
            r"Multiply the base's tens digit by the exponent.",
            r"Keep the last digit of that product as the tens digit.",
        ],
        r"Expanding the power leaves the tens digit driven only by a times n, everything higher vanishes mod 100.",
        r"Find the last two digits of 71 to the power 36.",
        [
            r"Tens digit of base: $7$; exponent: $36$.",
            r"$7 \times 36 = 252$; keep the last digit $2$.",
            r"Last two digits: $21$.",
        ],
        "21",
    ),
]


# ================= subtopic: ns-factors =================

FC_CONCEPT = (
    "Write N as a product of primes, N = p to the a times q to the b times r to the c. "
    "The number of factors is (a+1)(b+1)(c+1), the sum of factors comes from bracket "
    "products, and trailing zeros of a factorial come from counting fives."
)

FC_NOTES = r"""A factor of a number divides it exactly. The factors of $12$ are $1, 2, 3, 4, 6, 12$. A multiple is the reverse idea: $12, 24, 36, \ldots$ Every question here starts from the prime factorisation, so that skill comes first.

### Prime factorisation
Keep dividing by the smallest prime that fits. $720 = 2 \times 360 = 2 \times 2 \times 180 = \cdots = 2^4 \times 3^2 \times 5$. Write the result in power form $N = p^a \times q^b \times r^c$; every method below reads the exponents.

### Counting factors
A factor of $2^4 \times 3^2 \times 5$ chooses one power of each prime. The power of $2$: $0, 1, 2, 3$ or $4$, so five choices. The power of $3$: $0, 1$ or $2$, so three choices.
The power of $5$: $0$ or $1$, so two choices.

> **Rule:** Number of factors $= (a+1)(b+1)(c+1)$. For $720$: $5 \times 3 \times 2 = 30$ factors.

### Odd, even and special factors
- Odd factors: drop the power of $2$ completely. For $3600 = 2^4 \times 3^2 \times 5^2$: odd factors $= 3 \times 3 = 9$.
- Even factors: total minus odd, here $45 - 9 = 36$.
- Factors that are multiples of $k$: divide $N$ by $k$ and count factors of the result. For $1440$ with $k = 12$: $1440 \div 12 = 120 = 2^3 \times 3 \times 5$, giving $16$.
- Perfect-square factors: every exponent may take even values only. Cube factors: $0, 3, 6, \ldots$

### Sum of factors
Write one bracket per prime and multiply.
$$\text{sum} = (1 + p + \cdots + p^a)(1 + q + \cdots + q^b) \cdots$$
For $360 = 2^3 \times 3^2 \times 5$: $(1 + 2 + 4 + 8)(1 + 3 + 9)(1 + 5) = 15 \times 13 \times 6 = 1170$. For the sum of even factors only, start the bracket of $2$ at $2$: $(2 + 4 + 8) \times \cdots$

> **Tip:** The bracket form also answers sum of odd factors: just delete the bracket of $2$.

### Product of factors and factor pairs
Factors pair as $(1, N), (2, N/2), \ldots$ and each pair multiplies to $N$. So the product of all factors of $N$ is $N^{d/2}$ where $d$ is the factor count: for $12$, with $6$ factors, the product is $12^3 = 1728$.

The same pairing counts the ways to write $N$ as a product of two factors: $d/2$ ways when $N$ is not a perfect square, $(d+1)/2$ when it is. For two co-prime factors the answer is $2^{k-1}$, with $k$ the number of distinct primes.

### Trailing zeros of factorials
A trailing zero needs a $10 = 2 \times 5$. Factorials hold more twos than fives, so count the fives: divide by $5$, then the quotient by $5$ again, and add.

> **Rule:** Zeros in $n! = \left\lfloor \dfrac{n}{5} \right\rfloor + \left\lfloor \dfrac{n}{25} \right\rfloor + \left\lfloor \dfrac{n}{125} \right\rfloor + \cdots$. For $125!$: $25 + 5 + 1 = 31$ zeros.

### Highest power of a prime in a factorial
Same successive division by the prime. The power of $3$ in $100!$ is $33 + 11 + 3 + 1 = 48$. For a composite such as $12 = 2^2 \times 3$, find each prime's power, divide the power of $2$ by $2$, and take the smaller result. In $50!$: twos give $47$, so $23$ twos-pairs, and threes give $22$; the answer is $22$.
"""

FC_FORMULAS = [
    {"name": "Number of factors", "tex": r"d(N) = (a + 1)(b + 1)(c + 1)", "note": ""},
    {"name": "Sum of factors", "tex": r"\sigma(N) = (1 + p + \cdots + p^a)(1 + q + \cdots + q^b) \cdots", "note": ""},
    {"name": "Even factors", "tex": r"a \times (b + 1)(c + 1)", "note": "when 2 has exponent a"},
    {"name": "Product of all factors", "tex": r"N^{d(N)/2}", "note": ""},
    {"name": "Trailing zeros in n factorial", "tex": r"\left\lfloor \dfrac{n}{5} \right\rfloor + \left\lfloor \dfrac{n}{25} \right\rfloor + \left\lfloor \dfrac{n}{125} \right\rfloor + \cdots", "note": ""},
    {"name": "Highest power of a prime in n factorial", "tex": r"\sum_{k \ge 1} \left\lfloor \dfrac{n}{p^k} \right\rfloor", "note": ""},
]

FC_TRICKS = [
    {
        "title": "Even factors: force one two",
        "body": "If N has two to the power a in it, even factors equal a times the factor count of the odd part.",
        "example": {
            "q": "How many even factors does 360 have?",
            "steps": [
                r"$360 = 2^3 \times 3^2 \times 5$.",
                r"Even factors $= 3 \times (2 + 1) \times (1 + 1) = 3 \times 3 \times 2$.",
                r"$= 18$.",
            ],
            "answer": "18",
        },
    },
    {
        "title": "Successive division by five",
        "body": "For trailing zeros, keep dividing n by 5 and add the quotients until the quotient is 0.",
        "example": {
            "q": "How many zeros end 1000!?",
            "steps": [
                r"$1000 \to 200 \to 40 \to 8 \to 1$.",
                r"Sum: $200 + 40 + 8 + 1$.",
                r"$249$ zeros.",
            ],
            "answer": "249",
        },
    },
    {
        "title": "Sum of factors as brackets",
        "body": "One bracket per prime, each running from 1 up to the full power. Multiply the brackets.",
        "example": {
            "q": "Find the sum of all factors of 72.",
            "steps": [
                r"$72 = 2^3 \times 3^2$.",
                r"Brackets: $(1 + 2 + 4 + 8)(1 + 3 + 9) = 15 \times 13$.",
                r"$= 195$.",
            ],
            "answer": "195",
        },
    },
]

FC_MISTAKES = [
    {
        "wrong": "Counting only n/5 for trailing zeros.",
        "right": "Add the extra fives from 25, 125 and higher powers of 5 as well.",
    },
    {
        "wrong": "Adding exponents instead of multiplying (a+1)(b+1)(c+1).",
        "right": "The choices per prime multiply, they never add.",
    },
    {
        "wrong": "Forgetting 1 and N as factors.",
        "right": "Both count; the formula (a+1)(b+1)(c+1) already includes them.",
    },
    {
        "wrong": "Adding the zero counts for a sum like 100! + 200!.",
        "right": "The sum keeps only the smaller count of trailing zeros.",
    },
    {
        "wrong": "Testing for a prime with squares of primes only.",
        "right": "Divide by every prime up to the square root of N.",
    },
]

FC_REVISION = [
    r"Factor count: $(a+1)(b+1)(c+1)$; odd factors: drop the $2$.",
    r"Multiples of $k$ among the factors: count factors of $N/k$.",
    r"Square factors: even exponents only; cube factors: $0, 3, 6, \ldots$",
    r"Sum: one bracket per prime, multiply the brackets.",
    r"Product of all factors: $N^{d/2}$.",
    r"Zeros in $n!$: keep dividing $n$ by $5$ and add quotients.",
    r"Composite power in $n!$: split into prime powers and take the smallest.",
]

FC_PATTERNS = [
    pat(
        "ns-fc-p1", "Number of factors: total, odd, even", "very common",
        r"The question asks how many factors or divisors a number has, or how many of them are odd or even.",
        r"N = p^a q^b r^c \ \Rightarrow\ d(N) = (a + 1)(b + 1)(c + 1)",
        [
            r"Prime-factorise $N$.",
            r"Total factors: multiply (each exponent $+ 1$).",
            r"Odd factors: ignore the power of $2$ entirely.",
            r"Even factors: total minus odd.",
        ],
        r"Each factor picks one power of every prime, and the choices are independent.",
        r"How many factors does 420 have?",
        [
            r"$420 = 2^2 \times 3 \times 5 \times 7$.",
            r"Total: $(2+1)(1+1)(1+1)(1+1) = 3 \times 2 \times 2 \times 2$.",
            r"$= 24$ factors.",
        ],
        "24",
    ),
    pat(
        "ns-fc-p2", "Special factors: squares, cubes, multiples of k", "common",
        r"The question asks how many factors of N are perfect squares, perfect cubes, or divisible by a given number.",
        r"\#\{\text{factors divisible by } k\} = d(N / k)",
        [
            r"For square factors, allow only even exponents $0, 2, 4, \ldots$ for every prime.",
            r"For cube factors, allow only $0, 3, 6, \ldots$",
            r"For multiples of $k$, divide $N$ by $k$ and count factors of the quotient.",
        ],
        r"A square factor carries even powers only; a factor divisible by k is k times a factor of N/k.",
        r"How many factors of 2 to the power 6 x 3 to the power 4 are perfect squares?",
        [
            r"Powers of $2$ available to a square: $0, 2, 4, 6$, that is $4$ choices.",
            r"Powers of $3$: $0, 2, 4$, that is $3$ choices.",
            r"$4 \times 3 = 12$ square factors.",
        ],
        "12",
    ),
    pat(
        "ns-fc-p3", "Sum of factors", "common",
        r"The question asks for the sum of all factors of N, or the sum of only the odd or only the even factors.",
        r"\sigma(N) = (1 + p + \cdots + p^a)(1 + q + \cdots + q^b) \cdots",
        [
            r"Prime-factorise $N$.",
            r"Write one bracket per prime, running from $1$ to the full power.",
            r"Multiply the brackets.",
            r"Odd sum: delete the bracket of $2$. Even sum: start that bracket at $2$.",
        ],
        r"Expanding the bracket product produces every factor exactly once.",
        r"Find the sum of all factors of 90.",
        [
            r"$90 = 2 \times 3^2 \times 5$.",
            r"Brackets: $(1 + 2)(1 + 3 + 9)(1 + 5)$.",
            r"$= 3 \times 13 \times 6 = 234$.",
        ],
        "234",
    ),
    pat(
        "ns-fc-p4", "Trailing zeros in a factorial or product", "very common",
        r"The question asks how many zeros end a factorial like 90!, or end a written-out product.",
        r"Z(n!) = \left\lfloor \dfrac{n}{5} \right\rfloor + \left\lfloor \dfrac{n}{25} \right\rfloor + \cdots",
        [
            r"Divide $n$ by $5$ and keep the whole part.",
            r"Divide that quotient by $5$ again, and keep going.",
            r"Add all the quotients.",
            r"For a plain product, count the twos and the fives and take the smaller count.",
        ],
        r"Each trailing zero needs one two and one five, and fives are the scarce partner.",
        r"How many zeros are at the end of 90 factorial?",
        [
            r"$90 \div 5 = 18$.",
            r"$18 \div 5 = 3$.",
            r"Zeros: $18 + 3 = 21$.",
        ],
        "21",
    ),
    pat(
        "ns-fc-p5", "Highest power of a prime or composite in a factorial", "common",
        r"The question asks for the largest n such that 7 to the n divides 150!, or the highest power of 12 in 50!.",
        r"E_p(n!) = \sum_{k \ge 1} \left\lfloor \dfrac{n}{p^k} \right\rfloor",
        [
            r"For a prime $p$: divide $n$ by $p$, then the quotient again, and add the quotients.",
            r"For a composite, split into prime powers.",
            r"Divide each prime's count by the power required.",
            r"Take the smallest result.",
        ],
        r"Floor division counts multiples of p, then the extra p carried by multiples of its square, and so on.",
        r"Find the highest power of 7 that divides 150 factorial.",
        [
            r"$150 \div 7 = 21$.",
            r"$21 \div 7 = 3$.",
            r"Total: $21 + 3 = 24$.",
        ],
        "7 to the power 24",
    ),
    pat(
        "ns-fc-p6", "Product of factors and factor pairs", "occasional",
        r"The question asks for the product of all factors of N, or in how many ways N can be written as a product of two factors.",
        r"\prod \text{factors} = N^{d/2}, \qquad \text{pairs} = \dfrac{d}{2} \ (N \text{ not a square})",
        [
            r"Count the factors $d$.",
            r"Product of factors: raise $N$ to $d/2$.",
            r"Two-factor products: $d/2$ ways, or $(d+1)/2$ for a perfect square.",
            r"Co-prime pairs: $2^{k-1}$ with $k$ distinct primes.",
        ],
        r"Factors pair as f with N over f, and each pair multiplies to N.",
        r"In how many ways can 48 be written as a product of two factors?",
        [
            r"$48 = 2^4 \times 3$, so $d = (4+1)(1+1) = 10$ factors.",
            r"$48$ is not a perfect square.",
            r"Ways: $10 \div 2 = 5$.",
        ],
        "5",
    ),
]


# ================= subtopic: ns-fractions-decimals =================

FD_CONCEPT = (
    "A fraction compares a part with the whole; a decimal writes the same idea in place value. "
    "Every terminating or repeating decimal is a fraction in disguise, and converting between the "
    "two forms follows two fixed rules."
)

FD_NOTES = r"""A fraction like $\dfrac{3}{4}$ means three parts out of four equal parts. The top number is the numerator, the bottom is the denominator. Fractions, decimals and percentages are three languages for the same quantity: $\dfrac{3}{4} = 0.75 = 75\%$.

### Comparing fractions in one step
Two rules save long division. Cross-multiplication: $\dfrac{a}{b}$ versus $\dfrac{c}{d}$, compare $ad$ with $bc$; the bigger product sits on the bigger fraction. Complement rule: if fractions sit close to $1$, compare what is missing. $\dfrac{13}{17}$ misses $\dfrac{4}{17}$, and $\dfrac{9}{11}$ misses $\dfrac{2}{11}$; since $\dfrac{4}{17} > \dfrac{2}{11}$, the first fraction is smaller. Equal numerators: the smaller denominator wins, because the same cake is cut into fewer pieces.

> **Tip:** Same numerator, smaller denominator: bigger fraction. Same denominator: bigger numerator wins.

### Converting a fraction to a decimal
Divide, and watch the remainders. If a remainder repeats, the digits repeat too. When the denominator (in lowest terms) has only $2$s and $5$s, the division must end.

> **Rule:** A fraction terminates only when its lowest-terms denominator equals $2^m \times 5^n$. Otherwise it repeats forever.

$\dfrac{9}{50} = \dfrac{18}{100} = 0.18$ terminates. $\dfrac{8}{13}$ must repeat, because $13$ has a prime factor other than $2$ or $5$.

### Repeating decimal to fraction
Pure repeating: numerator is the repeating block, denominator is as many nines as the block length. $0.\overline{7} = \dfrac{7}{9}$ and $0.\overline{72} = \dfrac{72}{99} = \dfrac{8}{11}$. Mixed, with non-repeating digits first: subtract. $0.4\overline{7} = \dfrac{47 - 4}{90} = \dfrac{43}{90}$ and $2.4\overline{7} = 2 + \dfrac{43}{90} = \dfrac{223}{90}$.

> **Rule:** All digits minus non-repeating digits, over as many nines as repeating digits followed by as many zeros as non-repeating digits.

### Adding repeating decimals
Convert each to a fraction first, then add. $0.\overline{7} + 0.\overline{3} + 0.\overline{2} = \dfrac{7 + 3 + 2}{9} = \dfrac{12}{9} = \dfrac{4}{3}$. With a common denominator of nine, the numerators simply add.

> **Watch:** Never add repeating decimals digit by digit; the shift between them breaks place value.

### Fraction of a quantity
"Two-fifths of a number" means multiply: $\dfrac{2}{5} \times N$. When a fraction of a number is given, divide to recover the number. If $\dfrac{2}{5}$ of a number is $48$, the number is $48 \times \dfrac{5}{2} = 120$.

> **Example:** $\dfrac{3}{5}$ of a number exceeds $\dfrac{1}{4}$ of it by $63$. Then $\left(\dfrac{3}{5} - \dfrac{1}{4}\right)N = \dfrac{7}{20}N = 63$, so $N = 180$.

### Continued fractions
A stack like $3 + \dfrac{1}{2 + \dfrac{1}{4}}$ unwinds from the bottom up: the innermost $\dfrac{1}{4}$ first, then the middle level, then add $3$. Keep every level as a fraction; never convert to decimals half way.
"""

FD_FORMULAS = [
    {"name": "Pure repeating decimal", "tex": r"0.\overline{ab} = \dfrac{ab}{99}", "note": ""},
    {"name": "Mixed repeating decimal", "tex": r"0.a\overline{bc} = \dfrac{abc - a}{990}", "note": ""},
    {"name": "Terminating test", "tex": r"\dfrac{p}{q} \text{ terminates} \iff q = 2^m \times 5^n", "note": "q in lowest terms"},
]

FD_TRICKS = [
    {
        "title": "Nines for pure repeats",
        "body": "One repeating digit gives 9 in the denominator, two give 99, three give 999.",
        "example": {
            "q": r"Write 0.\overline{45} as a fraction.",
            "steps": [
                r"Two repeating digits, so divide by $99$.",
                r"$0.\overline{45} = \dfrac{45}{99}$.",
                r"$= \dfrac{5}{11}$.",
            ],
            "answer": "5/11",
        },
    },
    {
        "title": "Zeros after nines for mixed repeats",
        "body": "Denominator: one 9 per repeating digit, then one 0 per non-repeating digit. Numerator: all digits minus the non-repeating block.",
        "example": {
            "q": "Convert 0.2\\overline{45} to a fraction.",
            "steps": [
                r"Non-repeating digit: $2$ (one digit). Repeating block: $45$ (two digits).",
                r"Numerator: $245 - 2 = 243$. Denominator: $990$.",
                r"$\dfrac{243}{990} = \dfrac{27}{110}$.",
            ],
            "answer": "27/110",
        },
    },
    {
        "title": "Compare what is missing",
        "body": "For fractions close to 1, compare the shortfalls instead of the fractions.",
        "example": {
            "q": "Which is largest: 11/12, 13/14, 17/18, 19/21?",
            "steps": [
                r"Shortfalls: $\dfrac{1}{12}, \dfrac{1}{14}, \dfrac{1}{18}, \dfrac{2}{21}$.",
                r"The smallest shortfall is $\dfrac{1}{18}$.",
                r"So $\dfrac{17}{18}$ is the largest.",
            ],
            "answer": "17/18",
        },
    },
]

FD_MISTAKES = [
    {
        "wrong": "0.2\\overline{45} = 245/999.",
        "right": "Mixed repeat subtracts: (245 - 2)/990 = 27/110.",
    },
    {
        "wrong": "Cutting a repeating decimal short, 0.33 for 1/3, then adding.",
        "right": "Convert to an exact fraction first, then add.",
    },
    {
        "wrong": "Testing termination on a reducible denominator, like 50 in 27/50 reduced wrongly.",
        "right": "Reduce the fraction first; only then check for 2s and 5s.",
    },
    {
        "wrong": "Adding numerators and denominators: 1/2 + 1/3 = 2/5.",
        "right": "Use a common denominator: 1/2 + 1/3 = 5/6.",
    },
]

FD_REVISION = [
    r"Same numerator: smaller denominator means bigger fraction.",
    r"Cross-multiply to compare: $ad$ against $bc$.",
    r"Terminates only when the lowest-terms denominator is $2^m 5^n$.",
    r"Pure repeat: block over nines. Mixed: subtract, then nines and zeros.",
    r"Convert repeating decimals to fractions before adding.",
    r"'Of' means multiply; recover the number by dividing.",
]

FD_PATTERNS = [
    pat(
        "ns-fd-p1", "Mixed repeating decimal to fraction", "very common",
        r"A decimal with some non-repeating digits and then a repeating block must be written as a fraction.",
        r"0.a\overline{bc} = \dfrac{abc - a}{990}",
        [
            r"Count the digits that do not repeat ($s$) and the digits that repeat ($r$).",
            r"Numerator: all digits after the point, minus the non-repeating block.",
            r"Denominator: $r$ nines followed by $s$ zeros.",
            r"Reduce the fraction.",
        ],
        r"Multiplying by the denominator shifts one repeat cycle into place, and subtraction cancels the tail.",
        r"Convert 0.53 repeating on the 3 into a fraction.",
        [
            r"Non-repeating: $5$ (one digit). Repeating: $3$ (one digit).",
            r"Numerator: $53 - 5 = 48$. Denominator: $90$.",
            r"$\dfrac{48}{90} = \dfrac{8}{15}$.",
        ],
        "8/15",
    ),
    pat(
        "ns-fd-p2", "Sum of repeating decimals", "common",
        r"Two or more repeating decimals must be added, or their sum compared with a whole number.",
        r"0.\overline{a} + 0.\overline{b} = \dfrac{a + b}{9}",
        [
            r"Convert every decimal to a fraction.",
            r"Bring the fractions to a common denominator.",
            r"Add and reduce.",
        ],
        r"Fractions are exact; truncated decimals are not, so convert before adding.",
        r"Find the value of 0.7 repeating, plus 0.3 repeating, plus 0.2 repeating.",
        [
            r"$0.\overline{7} = \dfrac{7}{9}$, $0.\overline{3} = \dfrac{3}{9}$, $0.\overline{2} = \dfrac{2}{9}$.",
            r"Sum: $\dfrac{7 + 3 + 2}{9} = \dfrac{12}{9}$.",
            r"$= \dfrac{4}{3}$.",
        ],
        "4/3",
    ),
    pat(
        "ns-fd-p3", "Terminating or repeating test", "common",
        r"The question asks whether a given fraction terminates, or which of several fractions does.",
        r"q = 2^m 5^n \Rightarrow \text{terminates}",
        [
            r"Reduce the fraction to lowest terms.",
            r"Factorise the denominator.",
            r"If only $2$s and $5$s appear, it terminates; the decimal places equal the larger of $m$ and $n$.",
        ],
        r"Dividing by 2s and 5s only ever shifts the decimal point; other primes leave a remainder cycle.",
        r"Does 27/150 terminate or repeat? If it terminates, write the decimal.",
        [
            r"Reduce: $\dfrac{27}{150} = \dfrac{9}{50}$.",
            r"$50 = 2 \times 5^2$, so it terminates.",
            r"$\dfrac{9}{50} = \dfrac{18}{100} = 0.18$.",
        ],
        "Terminating, 0.18",
    ),
    pat(
        "ns-fd-p4", "Comparing fractions", "very common",
        r"The question asks which fraction is greater, or to arrange fractions in order.",
        r"\dfrac{a}{b} > \dfrac{c}{d} \iff ad > bc",
        [
            r"Try the quick rules first: same numerator, or same denominator.",
            r"Otherwise cross-multiply and compare the products.",
            r"Near $1$: compare the shortfalls from $1$ instead.",
        ],
        r"Cross-multiplication clears denominators in one step, with no division.",
        r"Which is greater: 8/13 or 13/21?",
        [
            r"Cross-multiply: $8 \times 21 = 168$.",
            r"$13 \times 13 = 169$.",
            r"$169 > 168$, so $\dfrac{13}{21}$ is greater.",
        ],
        "13/21",
    ),
    pat(
        "ns-fd-p5", "Fraction word problems", "common",
        r"A fraction of a number is given, or one fraction of a quantity exceeds another by a stated amount.",
        "",
        [
            r"Name the unknown number $N$.",
            r"Translate each fraction phrase into multiplication by $N$.",
            r"Build one equation from the given relation.",
            r"Solve for $N$ and answer what is asked.",
        ],
        r"'Two-fifths of' is exactly $\dfrac{2}{5} \times N$, so sentences become equations line by line.",
        r"Two-fifths of a number is 48. What is three-quarters of the number?",
        [
            r"$\dfrac{2}{5} N = 48$, so $N = 48 \times \dfrac{5}{2} = 120$.",
            r"Three-quarters: $\dfrac{3}{4} \times 120$.",
            r"$= 90$.",
        ],
        "90",
    ),
]


# ================= write back =================

data = json.loads(TOPIC.read_text(encoding="utf-8"))
subs = {s["id"]: s for s in data["subtopics"]}


def apply(sid, concept, notes, formulas, tricks, mistakes, revision, patterns):
    sub = subs[sid]
    old = {p["id"] for p in sub["patterns"]}
    new = {p["id"] for p in patterns}
    assert old <= new, (sid, old - new)
    assert len(new) == len(patterns), (sid, "duplicate pattern ids")
    other = {
        p["id"]
        for s2 in data["subtopics"]
        if s2["id"] != sid
        for p in s2["patterns"]
    }
    assert not (new & other), (sid, new & other)
    assert 2500 <= len(notes) <= 5000, (sid, len(notes))
    sub.update(
        concept=concept,
        notes=notes,
        formulas=formulas,
        tricks=tricks,
        mistakes=mistakes,
        revision=revision,
        patterns=patterns,
    )


apply("ns-types-counting", TC_CONCEPT, TC_NOTES, TC_FORMULAS, TC_TRICKS, TC_MISTAKES, TC_REVISION, TC_PATTERNS)
apply("ns-divisibility", DV_CONCEPT, DV_NOTES, DV_FORMULAS, DV_TRICKS, DV_MISTAKES, DV_REVISION, DV_PATTERNS)
apply("ns-remainders", RM_CONCEPT, RM_NOTES, RM_FORMULAS, RM_TRICKS, RM_MISTAKES, RM_REVISION, RM_PATTERNS)
apply("ns-unit-digit", UD_CONCEPT, UD_NOTES, UD_FORMULAS, UD_TRICKS, UD_MISTAKES, UD_REVISION, UD_PATTERNS)
apply("ns-factors", FC_CONCEPT, FC_NOTES, FC_FORMULAS, FC_TRICKS, FC_MISTAKES, FC_REVISION, FC_PATTERNS)
apply("ns-fractions-decimals", FD_CONCEPT, FD_NOTES, FD_FORMULAS, FD_TRICKS, FD_MISTAKES, FD_REVISION, FD_PATTERNS)

TOPIC.write_text(json.dumps(data, ensure_ascii=False, indent=1) + "\n", encoding="utf-8")
print("rewrote", TOPIC.name, "-", len(data["subtopics"]), "subtopics")
