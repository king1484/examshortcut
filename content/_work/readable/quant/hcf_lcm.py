"""Rewrite every subtopic of core/topics/quant/hcf-lcm.json (Phase 3 readable pass).

Keeps all existing pattern ids (practice questions link to them) and adds two new
patterns: hl-m5 (LCM of two large numbers) and hl-r5 (LCM + r inside a digit
bound). Every number used in every example is computed and asserted below.
Run with the Python312 interpreter.
"""

import json
from fractions import Fraction as F
from math import gcd, lcm
from pathlib import Path

ROOT = Path(__file__).resolve().parents[3]
TOPIC = ROOT / "core" / "topics" / "quant" / "hcf-lcm.json"

# ---------- hl-basics: verified numbers ----------
assert gcd(12, 18) == 6 and lcm(12, 18) == 36 and 6 * 36 == 216 == 12 * 18
assert 15 * 225 // 45 == 75 and gcd(45, 75) == 15 and lcm(45, 75) == 225
assert 6 * 3 == 18 and 6 * 4 == 24 and lcm(18, 24) == 72 == 6 * 3 * 4 and 6 * (3 + 4) == 42
assert 252 % (4 * 9) == 0 and 252 // 36 == 7 and gcd(28, 63) == 7 and lcm(28, 63) == 252
assert gcd(60, 84) == 12 and lcm(60, 84) == 420 == 12 * 5 * 7
assert gcd(108, 144) == 36 and lcm(12, 15, 20) == 60
assert 12 * 240 // 48 == 60 and gcd(48, 60) == 12 and lcm(48, 60) == 240
assert 700 % 35 == 0 and 700 // 35 == 20 and gcd(100, 140) == 20 and lcm(100, 140) == 700 and 100 + 140 == 240
assert 17 * 11 == 187 and 17 * 16 == 272 and gcd(187, 272) == 17 and lcm(187, 272) == 2992 == 17 * 11 * 16
assert 312 // 13 == 24 and gcd(13, 24) == 1 and lcm(13, 24) == 312
assert gcd(27, 72) == 9 and lcm(27, 72) == 216 == 9 * 3 * 8
assert 42 * 70 == 2940 and gcd(42, 70) == 14 and lcm(42, 70) == 210 and 2940 // 14 == 210
_pairs216 = [(m, n) for m in range(1, 7) for n in range(m, 7) if m * n == 6 and gcd(m, n) == 1]
assert _pairs216 == [(1, 6), (2, 3)]
assert lcm(6, 36) == 36 and lcm(12, 18) == 36 and 6 * 36 == 216 and 12 * 18 == 216

# ---------- hl-methods: verified numbers ----------
assert gcd(24, 36, 50) == 2 and lcm(24, 36, 50) == 1800 == 2 ** 3 * 3 ** 2 * 5 ** 2
assert 432 == 2 * 180 + 72 and 180 == 2 * 72 + 36 and 72 == 2 * 36 and gcd(432, 180) == 36
assert lcm(432, 180) == 2160 and 432 * 180 // 36 == 2160
assert gcd(1617, 903) == 21 and 1617 == 21 * 77 and 903 == 21 * 43
assert 1617 == 1 * 903 + 714 and 903 == 1 * 714 + 189 and 714 == 3 * 189 + 147
assert 189 == 1 * 147 + 42 and 147 == 3 * 42 + 21 and 42 == 2 * 21 + 0
_M2 = (2 ** 3 * 3 ** 2 * 5, 2 ** 2 * 3 ** 3 * 7, 2 * 3 ** 2 * 5 ** 2)
assert _M2 == (360, 756, 450)
assert gcd(*_M2) == 18 == 2 * 3 ** 2 and lcm(*_M2) == 37800 == 2 ** 3 * 3 ** 3 * 5 ** 2 * 7
assert F(gcd(2, 8, 10), lcm(3, 9, 27)) == F(2, 27)
assert F(2, 3) / F(2, 27) == 9 and F(8, 9) / F(2, 27) == 12 and F(10, 27) / F(2, 27) == 5
assert F(lcm(2, 8, 10), gcd(3, 9, 27)) == F(40, 3)
assert F(40, 3) / F(2, 3) == 20 and F(40, 3) / F(8, 9) == 15 and F(40, 3) / F(10, 27) == 36
assert gcd(63, 105, 210) == 21
assert lcm(15, 20, 45) == 180 and 180 % 15 == 0 and 180 % 20 == 0 and 180 % 45 == 0
assert gcd(240, 2700) == 60 and lcm(240, 2700) == 10800 == 2 ** 4 * 3 ** 3 * 5 ** 2
assert lcm(18, 24, 30) == 360 == 2 ** 3 * 3 ** 2 * 5
assert F(gcd(3, 5, 7), lcm(4, 6, 8)) == F(1, 24)
assert F(3, 4) / F(1, 24) == 18 and F(5, 6) / F(1, 24) == 20 and F(7, 8) / F(1, 24) == 21
assert lcm(20, 25, 40) == 200
assert 1617 // 21 == 77 and 77 * 903 == 69531 and lcm(1617, 903) == 69531 and 1617 * 903 // 21 == 69531

# ---------- hl-word-problems: verified numbers ----------
assert gcd(65, 117) == 13 and 70 % 13 == 5 and 125 % 13 == 8
assert lcm(9, 12, 15) == 180 and 185 % 9 == 185 % 12 == 185 % 15 == 5
assert lcm(5, 6, 8) == 120 and 119 % 5 == 4 and 119 % 6 == 5 and 119 % 8 == 7
assert lcm(6, 8, 12) == 24
assert gcd(840, 560) == 280 and 840 * 560 // 280 ** 2 == 6
assert lcm(6, 9, 12) == 36 and 35 % 6 == 5 and 35 % 9 == 8 and 35 % 12 == 11
assert lcm(10, 15, 20) == 60
assert gcd(42, 49) == 7 and 42 // 7 + 49 // 7 == 6 + 7 == 13
assert gcd(240, 180) == 60
assert gcd(996, 744) == 12 and 1000 % 12 == 4 and 750 % 12 == 6
assert lcm(12, 16, 24) == 48 and 56 % 12 == 56 % 16 == 56 % 24 == 8
assert lcm(12, 15, 18, 30) == 180 == 2 ** 2 * 3 ** 2 * 5

# ---------- hl-remainder-cases: verified numbers ----------
assert 182 % 5 == 182 % 6 == 2 and 182 % 7 == 0
assert min(n for n in range(1, 200) if n % 5 == n % 6 == 2 and n % 7 == 0) == 182
assert 1020 % 60 == 0 and 960 % 60 == 0 and 1020 // 60 == 17
assert 48 // 4 == 12 and [(a, b) for a in range(1, 13) for b in range(a, 13) if a * b == 12 and gcd(a, b) == 1] == [(1, 12), (3, 4)]
assert 4 * (3 + 4) == 28 and gcd(12, 16) == 4 and lcm(12, 16) == 48 and 12 + 16 == 28
assert 1764 // 14 ** 2 == 9 and [(a, b) for a in range(1, 10) for b in range(a, 10) if a * b == 9 and gcd(a, b) == 1] == [(1, 9)]
assert gcd(14, 126) == 14 and 14 * 126 == 1764 and lcm(14, 126) == 126
assert 123 - 51 == 72 and 171 - 123 == 48 and 171 - 51 == 120 and gcd(72, 48, 120) == 24
assert 51 % 24 == 123 % 24 == 171 % 24 == 3
assert lcm(12, 15, 20) == 60 and 99960 % 60 == 0 and 99999 % 60 == 39 and 99999 - 39 == 99960 and 99960 // 60 == 1666
assert 675 % 6 == 675 % 7 == 675 % 8 == 3 and 675 % 5 == 0
assert min(n for n in range(1, 700) if n % 6 == n % 7 == n % 8 == 3 and n % 5 == 0) == 675
assert [(a, b) for a in range(1, 7) for b in range(a, 7) if a * b == 6 and gcd(a, b) == 1] == [(1, 6), (2, 3)]
assert gcd(6, 36) == 6 and lcm(6, 36) == 36 and gcd(12, 18) == 6 and lcm(12, 18) == 36
assert 109 - 61 == 48 and 133 - 109 == 24 and 133 - 61 == 72 and gcd(48, 24, 72) == 24
assert 61 % 24 == 109 % 24 == 133 % 24 == 13
assert 736 % 3 == 736 % 5 == 736 % 7 == 1 and 736 % 8 == 0
assert min(n for n in range(1, 800) if n % 3 == n % 5 == n % 7 == 1 and n % 8 == 0) == 736
assert lcm(9, 12) == 36 and 108 % 36 == 0 and 72 % 36 == 0
assert 180 // 6 == 30 and [(a, b) for a in range(1, 31) for b in range(a, 31) if a * b == 30 and gcd(a, b) == 1] == [(1, 30), (2, 15), (3, 10), (5, 6)]
assert gcd(30, 36) == 6 and lcm(30, 36) == 180 and 30 + 36 == 66
assert min(n for n in range(1000, 2000) if n % 6 == n % 7 == n % 8 == 3) == 1011
assert 1011 % 6 == 1011 % 7 == 1011 % 8 == 3 and 1008 % 6 == 1008 % 7 == 1008 % 8 == 0


def pat(pid, name, freq, spot, formula, steps, why, q, ex_steps, answer):
    return {
        "id": pid, "name": name, "frequency": freq, "howToSpot": spot,
        "formula": formula, "steps": steps, "why": why,
        "example": {"q": q, "steps": ex_steps, "answer": answer},
    }


# ================= subtopic: hl-basics =================

HB_CONCEPT = (
    "The HCF is the largest number that divides every given number; the LCM is the "
    "smallest number that every given number divides. For two numbers, HCF times LCM "
    "equals their product. Numbers in a ratio are the ratio parts times the HCF."
)

HB_NOTES = r"""The HCF (highest common factor) is the largest number that divides each given number exactly. The LCM (lowest common multiple) is the smallest number that each given number divides exactly. For 12 and 18 the common factors are 1, 2, 3 and 6, so the HCF is 6; their multiples first meet at 36, so the LCM is 36.

### The size order
The HCF is never bigger than the smallest number. The LCM is never smaller than the largest number. So HCF $\le$ every number $\le$ LCM, for numbers of 1 or more. This order kills wrong options at sight.

> **Rule:** HCF $\le$ smallest number, and LCM $\ge$ largest number. An option breaking this order is wrong.

### The product relation
For exactly two numbers, HCF times LCM equals the product of the two numbers. Check on 12 and 18: $6 \times 36 = 216 = 12 \times 18$. The rule fails for three numbers, so never use it there. One common use is finding a missing number: other number $= \dfrac{\text{HCF} \times \text{LCM}}{\text{given number}}$.

> **Example:** HCF 15, LCM 225, one number 45. The other is $\dfrac{15 \times 225}{45} = 75$. Check: $\gcd(45, 75) = 15$ and $\text{LCM} = 225$.

### Numbers in a ratio
Numbers in ratio $a : b$ (parts co-prime) with HCF $h$ are $ha$ and $hb$. Then:
- LCM $= h \times a \times b$
- sum $= h(a + b)$
- difference $= h(b - a)$

Ratio 3 : 4 with HCF 6 gives 18 and 24, LCM $6 \times 12 = 72$, sum $6 \times 7 = 42$. Working backwards from an LCM: ratio 4 : 9 and LCM 252 give $h = \dfrac{252}{4 \times 9} = 7$, so the numbers are 28 and 63.

> **Tip:** Ratio and LCM given: divide the LCM by the product of the ratio parts. That quotient is the HCF.

### Co-prime and close numbers
Co-prime numbers have HCF 1, so their LCM is simply their product. Consecutive integers are always co-prime. The HCF also divides every difference of the numbers: two numbers 20 apart can never have HCF 12, because 12 does not divide 20.

One more standard shape: the HCF is $h$, and the other two factors of the LCM are $m$ and $n$ (co-prime). The numbers are $hm$ and $hn$, and the LCM is $hmn$. HCF 12 with other factors 5 and 7 gives numbers 60 and 84, and LCM $12 \times 35 = 420$.

> **Watch:** The LCM is always a multiple of the HCF. An LCM option that is not a multiple of the given HCF is wrong at sight.

### Counting pairs
A question may ask how many pairs of numbers have a given product $P$ and HCF $h$. Write the numbers as $ha$ and $hb$ with co-prime $a$ and $b$, so $ab = \dfrac{P}{h^2}$. The answer is the number of co-prime factor pairs of that quotient. The pair $(1, \text{quotient})$ counts as one pair. For product 216 with HCF 6: $\dfrac{216}{36} = 6$, and 6 has co-prime pairs $(1, 6)$ and $(2, 3)$, so 2 pairs exist: 6 with 36, and 12 with 18.
"""

HB_FORMULAS = [
    {"name": "Product relation (two numbers)", "tex": r"\text{HCF} \times \text{LCM} = a \times b", "note": ""},
    {"name": "Other number", "tex": r"b = \dfrac{\text{HCF} \times \text{LCM}}{a}", "note": ""},
    {"name": "Co-prime case", "tex": r"\gcd(a, b) = 1 \Rightarrow \text{LCM}(a, b) = ab", "note": ""},
    {"name": "HCF divides every difference", "tex": r"\gcd(a, b) \mid (a - b)", "note": ""},
    {"name": "LCM is a multiple of the HCF", "tex": r"\gcd(a, b) \mid \text{LCM}(a, b)", "note": ""},
    {"name": "Ratio pair", "tex": r"\text{numbers} = hm,\ hn; \quad \text{LCM} = hmn", "note": ""},
]

HB_TRICKS = [
    {
        "title": "Ratio split",
        "body": "Numbers in ratio a : b (co-prime parts) with HCF h are ha and hb. LCM = h times a times b; sum = h times (a plus b).",
        "example": {
            "q": "Two numbers are in the ratio 3 : 8 and their HCF is 9. Find their LCM.",
            "steps": [
                r"Numbers: $9 \times 3 = 27$ and $9 \times 8 = 72$.",
                r"LCM $= 9 \times 3 \times 8$.",
                r"$= 216$.",
            ],
            "answer": "216",
        },
    },
    {
        "title": "Product divided by HCF",
        "body": "Given any two of product, HCF, LCM, the product relation settles the third in one division.",
        "example": {
            "q": "The product of two numbers is 2940 and their HCF is 14. Find the LCM.",
            "steps": [
                r"$\text{HCF} \times \text{LCM} = \text{product}$.",
                r"$\text{LCM} = \dfrac{2940}{14}$.",
                r"$= 210$.",
            ],
            "answer": "210",
        },
    },
    {
        "title": "Co-prime pairs from the quotient",
        "body": "For pair-count questions, divide the product by the square of the HCF, then count co-prime factor pairs of the result.",
        "example": {
            "q": "The product of two numbers is 216 and their HCF is 6. How many such pairs exist?",
            "steps": [
                r"$ab = \dfrac{216}{6^2} = 6$.",
                r"Co-prime pairs of 6: $(1, 6)$ and $(2, 3)$.",
                r"So 2 pairs: 6 with 36, and 12 with 18.",
            ],
            "answer": "2",
        },
    },
]

HB_MISTAKES = [
    {
        "wrong": "Using HCF x LCM = product for three numbers.",
        "right": "The relation holds for exactly two numbers only.",
    },
    {
        "wrong": "Forgetting the co-prime pair (1, quotient) when counting pairs.",
        "right": "That pair is always valid; include it in the count.",
    },
    {
        "wrong": "Reading 'greatest number that divides' as an LCM question.",
        "right": "'Greatest that divides' is HCF; 'least that is divisible by' is LCM.",
    },
    {
        "wrong": "Taking the HCF of a ratio pair to be the ratio itself.",
        "right": "The HCF is the scale factor h; the ratio only gives the co-prime parts.",
    },
    {
        "wrong": "Reporting an LCM that is not a multiple of the HCF.",
        "right": "The LCM is always a multiple of the HCF; recheck the arithmetic.",
    },
]

HB_REVISION = [
    r"Two numbers: $\text{HCF} \times \text{LCM} = ab$. Three numbers: no such rule.",
    r"Co-prime numbers: HCF 1, LCM product. Consecutive integers are co-prime.",
    r"Ratio $a : b$ with HCF $h$: numbers $ha$, $hb$; LCM $hab$; sum $h(a + b)$.",
    r"HCF divides every difference; LCM is a multiple of the HCF.",
    r"Other factors $m$, $n$ of the LCM: numbers $hm$, $hn$; LCM $hmn$.",
    r"Pair count: co-prime factor pairs of product $\div h^2$.",
]

HB_PATTERNS = [
    pat(
        "hl-b1", "Find the HCF or LCM of small numbers directly", "very common",
        r"The question asks plainly for the HCF or LCM of two or three small numbers, with no story around it.",
        r"\text{HCF} = \text{common primes, lowest powers}; \quad \text{LCM} = \text{all primes, highest powers}",
        [
            r"Factorise each number into primes.",
            r"HCF: multiply the primes common to all numbers, at the lowest power of each.",
            r"LCM: multiply every prime that appears, at the highest power of each.",
            r"Sanity check: HCF at most the smallest number, LCM at least the largest.",
        ],
        r"A common divisor cannot use more of any prime than the poorest number holds; a common multiple needs the richest stock of every prime.",
        r"Find the LCM of 12, 15 and 20.",
        [
            r"$12 = 2^2 \times 3$, $15 = 3 \times 5$, $20 = 2^2 \times 5$.",
            r"Take the highest power of every prime: $2^2$, $3$, $5$.",
            r"LCM $= 4 \times 3 \times 5 = 60$.",
        ],
        "60",
    ),
    pat(
        "hl-b2", "HCF x LCM = product (two numbers)", "very common",
        r"Any two of product, HCF, LCM and one number are given, and a third value is asked.",
        r"\text{HCF} \times \text{LCM} = a \times b \ \Rightarrow\ b = \dfrac{\text{HCF} \times \text{LCM}}{a}",
        [
            r"Confirm exactly two numbers are involved.",
            r"Write the product relation and fill in the three known values.",
            r"Divide to get the fourth value.",
            r"Check: the HCF must divide the LCM, and the HCF must divide both numbers.",
        ],
        r"Writing $a = ha'$ and $b = hb'$ with co-prime parts, the LCM is $ha'b'$, so HCF times LCM equals $ab$.",
        r"The HCF of two numbers is 12, their LCM is 240, and one number is 48. Find the other number.",
        [
            r"Other $= \dfrac{12 \times 240}{48}$.",
            r"$= \dfrac{2880}{48} = 60$.",
            r"Check: $\gcd(48, 60) = 12$ and $\text{LCM} = 240$.",
        ],
        "60",
    ),
    pat(
        "hl-b3", "Numbers in a given ratio, HCF or LCM known", "very common",
        r"Two numbers are in a ratio and the HCF or LCM is given; a sum, difference or the numbers themselves are asked.",
        r"\text{numbers} = hm,\ hn; \quad \text{LCM} = hmn, \quad \text{sum} = h(m + n)",
        [
            r"Cancel the ratio to co-prime parts $m : n$ first.",
            r"HCF given: the numbers are $hm$ and $hn$.",
            r"LCM given: $h = \dfrac{\text{LCM}}{mn}$, then the numbers are $hm$ and $hn$.",
            r"Answer what is asked: sum, difference, product or the numbers.",
        ],
        r"The ratio fixes only the shape of the pair; the HCF is the scale factor that stretches it.",
        r"Two numbers are in the ratio 5 : 7 and their LCM is 700. Find their sum.",
        [
            r"$h = \dfrac{700}{5 \times 7} = \dfrac{700}{35} = 20$.",
            r"Numbers: $20 \times 5 = 100$ and $20 \times 7 = 140$.",
            r"Sum $= 100 + 140 = 240$.",
        ],
        "240",
    ),
    pat(
        "hl-b4", "HCF given with the other factors of the LCM", "common",
        r"The HCF is given together with the two leftover factors of the LCM, and the numbers are asked.",
        r"\text{numbers} = hm,\ hn \ \ (m, n \text{ co-prime}); \quad \text{LCM} = hmn",
        [
            r"The numbers are HCF times the first other factor, and HCF times the second.",
            r"The two other factors must be co-prime; otherwise the data is impossible.",
            r"If asked, the LCM is HCF times the product of the two factors.",
        ],
        r"The LCM equals the HCF times the leftover co-prime parts, by the structure of the two ideas.",
        r"The HCF of two numbers is 17 and the other two factors of their LCM are 11 and 16. Find the greater number.",
        [
            r"Numbers: $17 \times 11 = 187$ and $17 \times 16 = 272$.",
            r"$\gcd(11, 16) = 1$, so the data is valid.",
            r"Greater number $= 272$.",
        ],
        "272",
    ),
    pat(
        "hl-b5", "Co-prime, consecutive and property questions", "common",
        r"The word co-prime or consecutive appears, or a pair must be tested for being co-prime.",
        r"\gcd(a, b) = 1 \Rightarrow \text{LCM}(a, b) = ab",
        [
            r"Co-prime with LCM given: divide the LCM by the given number to get the other.",
            r"Testing a pair for co-prime: check for any common factor above 1.",
            r"Difference checks: a common factor must divide the difference of the pair.",
        ],
        r"With no common prime between them, nothing cancels, so the LCM is the plain product.",
        r"The LCM of two co-prime numbers is 312 and one of them is 13. Find the other number.",
        [
            r"Co-prime, so LCM $=$ product.",
            r"Other $= \dfrac{312}{13} = 24$.",
            r"Check: $\gcd(13, 24) = 1$.",
        ],
        "24",
    ),
]


# ================= subtopic: hl-methods =================

HM_CONCEPT = (
    "Prime factorisation reads HCF from the lowest powers and LCM from the highest "
    "powers. Long division finds the HCF of two big numbers fast, and one division "
    "gives the LCM. Fractions swap the rules: HCF of tops over LCM of bottoms."
)

HM_NOTES = r"""Every HCF or LCM question starts by picking a method. Small numbers yield to prime factorisation, two big numbers to long division, fractions to the cross rule, and decimals to shifting the point. For 24, 36 and 50: $24 = 2^3 \times 3$, $36 = 2^2 \times 3^2$, $50 = 2 \times 5^2$, so the HCF is $2$ and the LCM is $2^3 \times 3^2 \times 5^2 = 1800$.

### Prime factorisation
Write each number as a product of primes, one row per number in a small table.
- HCF: multiply the primes common to every number, each at its lowest power.
- LCM: multiply every prime that appears, each at its highest power.

Reading the table column by column does the work: column minima give the HCF, column maxima give the LCM. If no prime is common to all numbers, the HCF is 1.

> **Rule:** HCF takes the lowest powers of common primes; LCM takes the highest powers of all primes.

### Long division for two big numbers
Divide the bigger number by the smaller. Then divide the old divisor by the remainder. Repeat until the remainder is 0; the last non-zero divisor is the HCF. For 432 and 180: $432 = 2 \times 180 + 72$, then $180 = 2 \times 72 + 36$, then $72 = 2 \times 36 + 0$. The HCF is 36. The LCM then falls out as $\dfrac{432 \times 180}{36} = 2160$.

For three numbers, chain the process: HCF of the first two, then HCF of that result with the third.

> **Tip:** After the HCF, get the LCM as product divided by HCF. Never multiply the numbers out fully first; cancel the HCF first.

### Numbers already in prime-power form
When the question hands you numbers like $2^4 \times 3 \times 5$ and $2^2 \times 3^3 \times 5^2$, skip factorising. HCF: lowest power of each prime, here $2^2 \times 3 \times 5 = 60$. LCM: highest power of each prime, here $2^4 \times 3^3 \times 5^2 = 10800$. Multiply out only at the end.

### Fractions: the cross rule
$$\text{HCF} = \dfrac{\text{HCF of numerators}}{\text{LCM of denominators}}, \qquad \text{LCM} = \dfrac{\text{LCM of numerators}}{\text{HCF of denominators}}$$
The two rules mirror each other, so swap them deliberately. HCF of $\dfrac{2}{3}, \dfrac{8}{9}, \dfrac{10}{27}$ is $\dfrac{\gcd(2, 8, 10)}{\text{LCM}(3, 9, 27)} = \dfrac{2}{27}$.

> **Watch:** Reduce every fraction to lowest terms before applying the cross rule; a reducible fraction corrupts both lists.

### Decimals: shift the point
Count the largest number of decimal places, multiply everything by that power of 10, solve as whole numbers, then shift the point back. LCM of $0.15, 0.20, 0.45$: work with $15, 20, 45$, whose LCM is 180, so the answer is 1.80.

> **Example:** Check by dividing: $1.80 \div 0.15 = 12$, $1.80 \div 0.20 = 9$, $1.80 \div 0.45 = 4$. All whole, so 1.80 is right.

### Choosing a method fast
Small numbers: factorise mentally. Two big numbers: long division. Prime-power form: read minima and maxima. Fractions: cross rule. Decimals: clear the point, restore it at the end.
"""

HM_FORMULAS = [
    {"name": "HCF by factors", "tex": r"\text{HCF} = p_1^{\min} \times p_2^{\min} \times \cdots", "note": "common primes, lowest powers"},
    {"name": "LCM by factors", "tex": r"\text{LCM} = p_1^{\max} \times p_2^{\max} \times \cdots", "note": "all primes, highest powers"},
    {"name": "HCF of fractions", "tex": r"\text{HCF}\!\left(\dfrac{a}{b}, \dfrac{c}{d}\right) = \dfrac{\gcd(a, c)}{\text{LCM}(b, d)}", "note": ""},
    {"name": "LCM of fractions", "tex": r"\text{LCM}\!\left(\dfrac{a}{b}, \dfrac{c}{d}\right) = \dfrac{\text{LCM}(a, c)}{\gcd(b, d)}", "note": ""},
    {"name": "LCM from the HCF", "tex": r"\text{LCM}(a, b) = \dfrac{a \times b}{\gcd(a, b)}", "note": ""},
]

HM_TRICKS = [
    {
        "title": "Row of prime powers",
        "body": "Write each number as a row of prime powers in a small grid. LCM reads the column maxima, HCF the common minima. Three numbers take under thirty seconds.",
        "example": {
            "q": "Find the LCM of 18, 24 and 30.",
            "steps": [
                r"$18 = 2 \times 3^2$, $24 = 2^3 \times 3$, $30 = 2 \times 3 \times 5$.",
                r"Column maxima: $2^3$, $3^2$, $5$.",
                r"LCM $= 8 \times 9 \times 5 = 360$.",
            ],
            "answer": "360",
        },
    },
    {
        "title": "Cross rule for fractions",
        "body": "HCF of fractions: HCF of tops over LCM of bottoms. LCM of fractions: LCM of tops over HCF of bottoms.",
        "example": {
            "q": "Find the HCF of 3/4, 5/6 and 7/8.",
            "steps": [
                r"HCF of tops: $\gcd(3, 5, 7) = 1$.",
                r"LCM of bottoms: $\text{LCM}(4, 6, 8) = 24$.",
                r"HCF $= \dfrac{1}{24}$.",
            ],
            "answer": "1/24",
        },
    },
    {
        "title": "Shift the decimal point",
        "body": "Multiply by the power of 10 that clears every decimal, solve as integers, then shift the point back by the same number of places.",
        "example": {
            "q": "Find the LCM of 0.2, 0.25 and 0.4.",
            "steps": [
                r"Two decimal places: work with $20, 25, 40$.",
                r"$\text{LCM}(20, 25, 40) = 200$.",
                r"Shift back two places: $2.00$.",
            ],
            "answer": "2",
        },
    },
]

HM_MISTAKES = [
    {
        "wrong": "Taking the HCF of fractions as HCF of tops over HCF of bottoms.",
        "right": "The denominator of the HCF is the LCM of the bottoms.",
    },
    {
        "wrong": "Skipping the reduction of fractions before the cross rule.",
        "right": "Reduce every fraction to lowest terms first.",
    },
    {
        "wrong": "Giving the LCM the lowest powers and the HCF the highest.",
        "right": "HCF reads minima, LCM reads maxima.",
    },
    {
        "wrong": "Returning a whole-number answer for a decimals question.",
        "right": "The scale factor of 10 must be divided back out at the end.",
    },
    {
        "wrong": "Stopping long division at the first zero remainder divisor shown.",
        "right": "The HCF is the last non-zero divisor, not any earlier divisor.",
    },
]

HM_REVISION = [
    r"HCF: common primes, lowest powers. LCM: every prime, highest powers.",
    r"Long division: last non-zero divisor is the HCF; LCM $= \dfrac{ab}{\text{HCF}}$.",
    r"Three or more numbers: chain the HCF pairwise.",
    r"Prime-power form: read minima and maxima straight off.",
    r"Fractions: HCF of tops over LCM of bottoms, and the mirror for LCM.",
    r"Decimals: clear the point, solve, restore the same number of places.",
]

HM_PATTERNS = [
    pat(
        "hl-m1", "HCF by successive (long) division", "common",
        r"Two or three larger numbers appear and the HCF is asked; the numbers are too big to factorise comfortably.",
        r"\gcd(a, b): \text{ divide, then divide the divisor by the remainder; the last non-zero divisor is the HCF}",
        [
            r"Divide the bigger number by the smaller and note the remainder.",
            r"Divide the previous divisor by that remainder.",
            r"Repeat until the remainder is 0.",
            r"The last non-zero divisor is the HCF; for a third number, chain once more.",
        ],
        r"Every common divisor of the two numbers also divides each remainder, so the process keeps the common divisors while the numbers shrink.",
        r"Find the HCF of 1617 and 903 by successive division.",
        [
            r"$1617 = 1 \times 903 + 714$.",
            r"$903 = 1 \times 714 + 189$, then $714 = 3 \times 189 + 147$.",
            r"$189 = 1 \times 147 + 42$, then $147 = 3 \times 42 + 21$, then $42 = 2 \times 21 + 0$.",
            r"HCF $= 21$.",
        ],
        "21",
    ),
    pat(
        "hl-m2", "HCF and LCM from prime-power form", "common",
        r"The numbers arrive as prime products like 2 cubed times 3 squared times 5, and HCF or LCM is asked.",
        r"\text{HCF} = \prod p_i^{\min}, \qquad \text{LCM} = \prod p_i^{\max}",
        [
            r"List every prime that appears in any number.",
            r"HCF: take the smallest exponent of each prime across all numbers; skip a prime missing from any number.",
            r"LCM: take the largest exponent of each prime anywhere.",
            r"Multiply out only at the end.",
        ],
        r"The HCF must fit inside every number; the LCM must contain every number.",
        r"Find the LCM of the numbers $2^3 \times 3^2 \times 5$, $2^2 \times 3^3 \times 7$ and $2 \times 3^2 \times 5^2$.",
        [
            r"Highest power of each prime: $2^3$, $3^3$, $5^2$, $7$.",
            r"LCM $= 8 \times 27 \times 25 \times 7$.",
            r"$= 37800$.",
        ],
        "37800",
    ),
    pat(
        "hl-m3", "HCF and LCM of fractions (cross rule)", "very common",
        r"A list of fractions like 2/3, 8/9, 10/27 is given and the HCF or LCM of the fractions is asked.",
        r"\text{HCF} = \dfrac{\gcd(\text{numerators})}{\text{LCM}(\text{denominators})}, \qquad \text{LCM} = \dfrac{\text{LCM}(\text{numerators})}{\gcd(\text{denominators})}",
        [
            r"Reduce each fraction to lowest terms.",
            r"For the HCF: HCF of the tops over LCM of the bottoms.",
            r"For the LCM: LCM of the tops over HCF of the bottoms.",
            r"Check: every fraction divided by the HCF is whole; the LCM divided by every fraction is whole.",
        ],
        r"Putting all fractions over the LCM of the denominators turns them into whole numbers, and the ordinary rules on those integers give the cross rule.",
        r"Find the LCM of 2/3, 8/9 and 10/27.",
        [
            r"LCM of tops: $\text{LCM}(2, 8, 10) = 40$.",
            r"HCF of bottoms: $\gcd(3, 9, 27) = 3$.",
            r"LCM $= \dfrac{40}{3}$. Check: $\dfrac{40}{3} \div \dfrac{8}{9} = 15$, whole.",
        ],
        "40/3",
    ),
    pat(
        "hl-m4", "HCF and LCM of decimals", "common",
        r"Decimal values like 0.63, 1.05 and 2.1 are given, and the answer carries a decimal point.",
        r"\text{scale by } 10^k \to \text{integer HCF or LCM} \to \text{scale back by } 10^k",
        [
            r"Count the largest number of decimal places among the values.",
            r"Multiply every value by that power of 10 so all become integers.",
            r"Find the HCF or LCM of the integers.",
            r"Divide the result by the same power of 10.",
        ],
        r"A common scale factor multiplies both HCF and LCM by itself, so undo it at the end.",
        r"Find the HCF of 0.63, 1.05 and 2.1.",
        [
            r"Two decimal places: work with $63, 105, 210$.",
            r"$\gcd(63, 105, 210) = 21$.",
            r"Shift back two places: HCF $= 0.21$.",
        ],
        "0.21",
    ),
    pat(
        "hl-m5", "LCM of two large numbers via the HCF", "common",
        r"The LCM of two numbers too large to factorise is asked directly, or the HCF was already found.",
        r"\text{LCM}(a, b) = \dfrac{a \times b}{\gcd(a, b)}",
        [
            r"Find the HCF first, by long division.",
            r"Divide one number by the HCF.",
            r"Multiply the quotient by the other number.",
            r"Never multiply the two big numbers first; cancel the HCF before multiplying.",
        ],
        r"The product of two numbers equals HCF times LCM, so dividing by the HCF leaves the LCM without a huge multiplication.",
        r"Find the LCM of 1617 and 903.",
        [
            r"HCF by division: $\gcd(1617, 903) = 21$.",
            r"Cancel first: $1617 \div 21 = 77$.",
            r"LCM $= 77 \times 903 = 69531$.",
        ],
        "69531",
    ),
]


# ================= subtopic: hl-word-problems =================

HW_CONCEPT = (
    "Word problems here sort into two families. Anything 'greatest that divides' is an "
    "HCF; anything 'least that is divisible by' is an LCM. Remainders shift the number "
    "first: subtract them for the HCF, add them back for the LCM."
)

HW_NOTES = r"""Every word problem in this topic is a dressed-up HCF or LCM question. The fastest first step is to name the family: 'greatest number that divides' means HCF, 'least number divisible by' means LCM. For bells that toll together every 6, 8 and 12 minutes, the gap is $\text{LCM} = 24$ minutes.

### The template table
| Question wording | Tool |
|---|---|
| Greatest number that divides a, b, c | HCF |
| Least number divisible by a, b, c | LCM |
| Largest tile, rod or biggest equal group | HCF |
| Bells or lights together again | LCM |
| Least number, remainder r with every divisor | LCM + r |
| Greatest number, remainder r with every divisor | HCF of (number - r) |

> **Tip:** 'Greatest' pairs with HCF; 'least' pairs with LCM. Fix the family first, then the arithmetic is short.

### Divides with remainders
'Find the greatest number which divides 70 and 125 leaving remainders 5 and 8.' The divisor must divide $70 - 5 = 65$ and $125 - 8 = 117$, so it divides their HCF. $\gcd(65, 117) = 13$. Check: $70 = 5 \times 13 + 5$ and $125 = 9 \times 13 + 8$.

> **Rule:** Subtract each remainder from its number, then take the HCF. The answer must exceed every remainder.

### Same remainder with every divisor
If N leaves remainder r with every divisor, then $N - r$ is divisible by all of them. The least such N is LCM + r. For divisors 9, 12, 15 with remainder 5: $\text{LCM} = 180$, so $N = 185$.

### Remainders that differ by a constant
When each remainder is the same amount c below its divisor, add c instead. For divisors 6, 9, 12 with remainders 5, 8, 11: each remainder is divisor $- 1$, so $N + 1$ is a common multiple. $N = \text{LCM}(6, 9, 12) - 1 = 36 - 1 = 35$. Check: $35 \bmod 6 = 5$, $35 \bmod 9 = 8$, $35 \bmod 12 = 11$.

> **Watch:** Each remainder must be smaller than its divisor. A remainder bigger than its divisor means the working stopped one step early.

### Bells, lights and laps
Convert every interval to one unit, then take the LCM. Buses leaving every 10, 15 and 20 minutes together at 6 a.m. meet again after $\text{LCM} = 60$ minutes, at 7 a.m. To count meetings inside a window, divide the window by the LCM; add 1 only if the starting moment itself counts.

### Tiles, rods, vessels and groups
The largest square tile has side $\gcd(L, W)$ in the same units; the tile count is $\dfrac{L \times W}{h^2}$. The longest rod cut from planks of 42 cm and 49 cm has length $\gcd = 7$ cm, giving $6 + 7 = 13$ pieces. Equal groups of people: the group size is the HCF of the counts.

> **Example:** A hall is 8.4 m by 5.6 m, so 840 cm by 560 cm. The largest square tile has side $\gcd(840, 560) = 280$ cm, and $\dfrac{840 \times 560}{280^2} = 6$ tiles.

### Units first
Convert everything before computing: 2 m 40 cm is 240 cm, and 3 hours is 180 minutes. Mixed units are the number-one error here, because the HCF or LCM changes with the unit.
"""

HW_FORMULAS = [
    {"name": "Same remainder r", "tex": r"N = \text{LCM}(d_1, d_2, \ldots) \times k + r", "note": ""},
    {"name": "Remainder is divisor minus c", "tex": r"r_i = d_i - c \Rightarrow N = \text{LCM} \times k - c", "note": ""},
    {"name": "Divides with remainders", "tex": r"\text{answer} = \gcd(a - r_1,\ b - r_2,\ c - r_3)", "note": ""},
    {"name": "Largest tile count", "tex": r"\text{tiles} = \dfrac{L \times W}{h^2}, \quad h = \gcd(L, W)", "note": ""},
]

HW_TRICKS = [
    {
        "title": "Subtract remainders, then HCF",
        "body": "For 'greatest number dividing a and b leaving remainders r1 and r2', the answer is the HCF of (a - r1) and (b - r2).",
        "example": {
            "q": "Find the greatest number which divides 1000 and 750 leaving remainders 4 and 6.",
            "steps": [
                r"$1000 - 4 = 996$ and $750 - 6 = 744$.",
                r"$\gcd(996, 744) = 12$.",
                r"Check: $1000 \bmod 12 = 4$ and $750 \bmod 12 = 6$.",
            ],
            "answer": "12",
        },
    },
    {
        "title": "LCM plus r",
        "body": "For 'least number leaving remainder r with each divisor', add r to the LCM of the divisors.",
        "example": {
            "q": "Find the least number which when divided by 12, 16 and 24 leaves remainder 8 in each case.",
            "steps": [
                r"$\text{LCM}(12, 16, 24) = 48$.",
                r"Least number $= 48 + 8 = 56$.",
                r"Check: $56 \bmod 12 = 56 \bmod 16 = 56 \bmod 24 = 8$.",
            ],
            "answer": "56",
        },
    },
    {
        "title": "Bells: add the LCM to the clock",
        "body": "Convert all intervals to one unit, take the LCM, and add it to the given start time.",
        "example": {
            "q": "Four lights blink every 12, 15, 18 and 30 seconds and blink together at noon. When do they next blink together?",
            "steps": [
                r"$\text{LCM}(12, 15, 18, 30) = 180$ seconds.",
                r"$180$ seconds $= 3$ minutes.",
                r"Noon $+ 3$ minutes $=$ 12:03.",
            ],
            "answer": "12:03",
        },
    },
]

HW_MISTAKES = [
    {
        "wrong": "Adding the remainder in a 'greatest number that divides' question.",
        "right": "That family needs the HCF of the numbers minus their remainders.",
    },
    {
        "wrong": "Mixing metres with centimetres, or minutes with seconds.",
        "right": "Convert all measurements to one unit before the HCF or LCM.",
    },
    {
        "wrong": "Reporting LCM + r when a larger value was demanded by a bound.",
        "right": "Fit LCM times k plus r into the stated range; the least uses k = 1.",
    },
    {
        "wrong": "Using the HCF where the question says 'divisible by all'.",
        "right": "'Divisible by all' is an LCM question; 'divides all' is HCF.",
    },
    {
        "wrong": "Counting the starting moment in a bells question without checking the wording.",
        "right": "Divide the window by the LCM; add 1 only if the start counts.",
    },
]

HW_REVISION = [
    r"'Greatest that divides' $\to$ HCF; 'least divisible by' $\to$ LCM.",
    r"Divides with remainders: subtract remainders, take HCF.",
    r"Same remainder r, least value: LCM $+ r$.",
    r"Each remainder $= $ divisor $- c$: least value LCM $- c$.",
    r"Bells and laps: LCM of intervals, then add to the clock.",
    r"Tiles and rods: HCF of dimensions; count $=$ area $\div h^2$ or total $\div h$.",
    r"Convert units before anything else.",
]

HW_PATTERNS = [
    pat(
        "hl-w1", "Greatest number dividing with given remainders", "very common",
        r"The question asks for the greatest number which divides two or three numbers leaving stated remainders.",
        r"\text{answer} = \gcd(a - r_1,\ b - r_2,\ c - r_3)",
        [
            r"Subtract each remainder from its number; the divisor divides each difference.",
            r"Take the HCF of the differences.",
            r"Check the answer exceeds every remainder.",
        ],
        r"The unknown divisor divides each N minus r, so it is a common factor, and the greatest one is the HCF.",
        r"Find the greatest number which divides 70 and 125 leaving remainders 5 and 8.",
        [
            r"$70 - 5 = 65$ and $125 - 8 = 117$.",
            r"$\gcd(65, 117) = 13$.",
            r"Check: $70 = 5 \times 13 + 5$, $125 = 9 \times 13 + 8$.",
        ],
        "13",
    ),
    pat(
        "hl-w2", "Least number leaving the same remainder (LCM + r)", "very common",
        r"The question asks for the least number which when divided by several divisors leaves the same remainder each time.",
        r"N = \text{LCM}(a, b, c) \times k + r",
        [
            r"Take the LCM of the divisors.",
            r"Add the remainder r for the least value.",
            r"With a bound (four-digit, above 1000), pick k so that LCM x k + r fits.",
        ],
        r"N minus r must be a common multiple of all divisors, and the least positive one is the LCM.",
        r"Find the least number which when divided by 9, 12 and 15 leaves remainder 5 in each case.",
        [
            r"$\text{LCM}(9, 12, 15) = 180$.",
            r"Least number $= 180 + 5 = 185$.",
            r"Check: $185 \bmod 9 = 185 \bmod 12 = 185 \bmod 15 = 5$.",
        ],
        "185",
    ),
    pat(
        "hl-w3", "Remainder is divisor minus c each time", "common",
        r"The remainders differ, but each one sits a fixed amount below its own divisor.",
        r"r_i = d_i - c \Rightarrow N = \text{LCM}(d_1, d_2, \ldots) \times k - c",
        [
            r"Subtract each remainder from its divisor; confirm the same value c every time.",
            r"Then N + c is divisible by every divisor.",
            r"The least N is LCM minus c.",
        ],
        r"Adding c repairs every division to an exact one, so N + c is a common multiple.",
        r"Find the least number which when divided by 5, 6 and 8 leaves remainders 4, 5 and 7.",
        [
            r"$5 - 4 = 1$, $6 - 5 = 1$, $8 - 7 = 1$, so $c = 1$.",
            r"$\text{LCM}(5, 6, 8) = 120$.",
            r"$N = 120 - 1 = 119$.",
        ],
        "119",
    ),
    pat(
        "hl-w4", "Bells, lights and laps meeting again", "common",
        r"Events repeat at different intervals, start together, and the question asks when they next coincide or how often.",
        r"\text{gap} = \text{LCM}(\text{intervals})",
        [
            r"Convert every interval to the same unit.",
            r"The LCM of the intervals is the gap between coincidences.",
            r"Add the gap to the start time, or divide the window by it to count meetings.",
            r"Check the wording for whether the starting moment counts.",
        ],
        r"Two repeating events coincide exactly at common multiples of their periods, and the first one is the LCM.",
        r"Three bells toll every 6, 8 and 12 minutes and toll together at 7 a.m. When do they next toll together?",
        [
            r"$\text{LCM}(6, 8, 12) = 24$ minutes.",
            r"$7$ a.m. $+ 24$ minutes.",
            r"$= 7$:$24$ a.m.",
        ],
        "7:24 a.m.",
    ),
    pat(
        "hl-w5", "Largest tile, rod, vessel or equal group", "common",
        r"The question asks for the largest square tile, longest equal rod, biggest vessel, or biggest identical groups.",
        r"\text{size} = \gcd(\text{dimensions}); \quad \#\text{tiles} = \dfrac{L \times W}{h^2}",
        [
            r"Convert all measurements to one unit.",
            r"The HCF of the dimensions or counts gives the size.",
            r"Divide the total by the HCF for the count of tiles, pieces or groups.",
        ],
        r"The tile or rod must fit each dimension a whole number of times, so it is a common divisor; the largest is the HCF.",
        r"A hall is 8.4 m long and 5.6 m wide. Find the largest square tile that paves it exactly, and the number of tiles.",
        [
            r"Metres to centimetres: $840$ and $560$.",
            r"Side $= \gcd(840, 560) = 280$ cm $= 2.8$ m.",
            r"Tiles $= \dfrac{840 \times 560}{280^2} = 6$.",
        ],
        "2.8 m side, 6 tiles",
    ),
]


# ================= subtopic: hl-remainder-cases =================

HR_CONCEPT = (
    "Harder questions chain one extra condition onto an LCM or HCF. Write N = LCM x k + r "
    "and let the condition pin down k, or rebuild numbers as h times co-prime parts from "
    "the HCF and LCM."
)

HR_NOTES = r"""The harder questions in this topic add one extra condition to a plain LCM or HCF setup. The master frame is $N = L \times k + r$, where $L$ is the LCM of the divisors. For divisors 5 and 6 with remainder 2: $L = 30$, so $N = 30k + 2$, giving 32, 62, 92, and so on.

### The master frame
$k = 1$ gives the least positive value; larger k walks up the same family. Any extra condition, such as divisibility by one more number or a digit bound, simply selects k.

> **Rule:** Write $N = L \times k + r$ first. Then fit the extra condition onto k.

### An extra divisibility condition
Test $k = 1, 2, 3, \ldots$ until $Lk + r$ satisfies the condition. For 'N leaves remainder 2 with 5 and 6, and N is divisible by 7': $N = 30k + 2$. Trying k gives 32, 62, 122, 152, 182, and $182 = 7 \times 26$ works. So $N = 182$.

### Least and greatest n-digit numbers
Multiples of $L$ are the candidates. Least four-digit multiple of 60: $1000 = 16 \times 60 + 40$, so add $60 - 40 = 20$ to reach 1020. Greatest works from the top: divide 99,999 by 60, subtract the remainder, and land on the greatest multiple under the bound.

> **Tip:** Step up from 10, 100, 1000 for the least; step down from 9, 99, 999 for the greatest. With a remainder r, fit $Lk + r$ inside the range instead of plain multiples.

### Rebuilding numbers from HCF and LCM
Numbers with HCF $h$ are $ha$ and $hb$ with co-prime parts, and $ab = \dfrac{\text{LCM}}{h}$. With HCF 4 and LCM 48: $ab = 12$, whose co-prime pairs are $(1, 12)$ and $(3, 4)$. A given sum picks the pair: sum 28 needs $a + b = 7$, so the parts are 3 and 4 and the numbers are 12 and 16.

> **Watch:** List only co-prime factor pairs. The pair $(2, 6)$ for $ab = 12$ is impossible, because the numbers would share an extra factor 2.

### Counting possible pairs
Count the co-prime factor pairs of $ab$, and remember the pair $(1, ab)$. Product 1764 with HCF 14 gives $ab = \dfrac{1764}{14^2} = 9$, and 9 has the single co-prime pair $(1, 9)$: the numbers must be 14 and 126. Count each unordered pair once, with the smaller part first, so $(1, 9)$ and $(9, 1)$ are the same pair.

### Sanity checks that catch slips
Two quick filters catch most slips in this subtopic. First, the HCF must divide the LCM, both numbers, and their sum and difference. Second, every rebuilt pair must multiply back to the product and carry the stated HCF. Run both checks before marking the answer.

### The same unknown remainder
When no remainder is given but it is the same for all numbers, the divisor divides every pairwise difference. For 51, 123 and 171: the differences are 72, 48 and 120, and $\gcd(72, 48, 120) = 24$. The common remainder is $51 \bmod 24 = 3$, the same for all three.

> **Example:** Check: $123 = 5 \times 24 + 3$ and $171 = 7 \times 24 + 3$. Both leave remainder 3, so 24 is right.
"""

HR_FORMULAS = [
    {"name": "Extra divisibility condition", "tex": r"N = Lk + r, \quad N \equiv 0 \pmod{p} \ \Rightarrow\ Lk \equiv -r \pmod{p}", "note": ""},
    {"name": "Reconstruction from HCF and LCM", "tex": r"ab = \dfrac{\text{LCM}}{h}, \quad \gcd(a, b) = 1, \quad \text{numbers} = ha,\ hb", "note": ""},
    {"name": "Pair count", "tex": r"\#\{(a, b): ab = M,\ \gcd(a, b) = 1,\ a \le b\}", "note": ""},
    {"name": "Same unknown remainder", "tex": r"\text{answer} = \gcd(a - b,\ b - c,\ a - c)", "note": ""},
]

HR_TRICKS = [
    {
        "title": "Test k until it clicks",
        "body": "Once N = LCM x k + r is written, only k remains. Test k = 1, 2, 3 against the extra condition; small values click fast.",
        "example": {
            "q": "Find the least number which leaves remainder 1 with 3, 5 and 7, and is divisible by 8.",
            "steps": [
                r"$L = \text{LCM}(3, 5, 7) = 105$, so $N = 105k + 1$.",
                r"Test: $106, 211, 316, 421, 526, 631, 736$; $736 = 8 \times 92$.",
                r"$N = 736$.",
            ],
            "answer": "736",
        },
    },
    {
        "title": "n-digit multiple scan",
        "body": "For the least n-digit multiple, divide the smallest n-digit number by the LCM and step up to the next multiple. For the greatest, subtract the remainder from the largest n-digit number.",
        "example": {
            "q": "Find the least three-digit number exactly divisible by 9 and 12.",
            "steps": [
                r"$\text{LCM}(9, 12) = 36$.",
                r"$100 = 2 \times 36 + 28$, so step up by $8$.",
                r"$108 = 3 \times 36$.",
            ],
            "answer": "108",
        },
    },
    {
        "title": "Sum or difference picks the pair",
        "body": "With HCF, LCM and a sum or difference given, list co-prime pairs of LCM / HCF and match h times the parts to the sum.",
        "example": {
            "q": "Two numbers have HCF 6, LCM 180 and sum 66. Find the numbers.",
            "steps": [
                r"$ab = \dfrac{180}{6} = 30$; co-prime pairs $(1, 30)$, $(2, 15)$, $(3, 10)$, $(5, 6)$.",
                r"Parts sum: $6(a + b) = 66$ gives $a + b = 11$.",
                r"Pair $(5, 6)$: numbers 30 and 36.",
            ],
            "answer": "30 and 36",
        },
    },
]

HR_MISTAKES = [
    {
        "wrong": "Answering LCM + r when an extra condition forces a larger multiple.",
        "right": "Fit N = LCM x k + r through the extra condition and take the smallest k that works.",
    },
    {
        "wrong": "Listing factor pairs of LCM / HCF without checking co-primality.",
        "right": "Only co-prime pairs are possible; drop the rest before matching the sum.",
    },
    {
        "wrong": "Forgetting the pair (1, M) when counting possibilities.",
        "right": "That pair is always co-prime and always counts.",
    },
    {
        "wrong": "Counting (a, b) and (b, a) as two pairs.",
        "right": "Order does not matter; count each pair once with a at most b.",
    },
    {
        "wrong": "Skipping the check that the HCF divides the sum or difference.",
        "right": "The HCF must divide both numbers, so it divides their sum and difference too.",
    },
]

HR_REVISION = [
    r"Master frame: $N = L \times k + r$; extra conditions only choose $k$.",
    r"Least n-digit multiple: step up from $10 \ldots 0$; greatest: step down from $99 \ldots 9$.",
    r"Numbers from HCF and LCM: $ab = \text{LCM} \div h$, co-prime parts only.",
    r"Pair count: co-prime factor pairs of LCM $\div h$ (or product $\div h^2$).",
    r"Same unknown remainder: HCF of pairwise differences.",
    r"Common remainder check: any number mod the answer, same value for all.",
]

HR_PATTERNS = [
    pat(
        "hl-r1", "Least or greatest n-digit number divisible by a set", "very common",
        r"The question asks for the least or greatest number of a given digit count divisible by several divisors.",
        r"\text{least: next multiple of } L \text{ at or above } 10^{n-1}; \quad \text{greatest: } 10^n - 1 - \left((10^n - 1) \bmod L\right)",
        [
            r"Take $L$ as the LCM of the divisors.",
            r"Least: divide the smallest n-digit number by $L$ and step up to the next multiple.",
            r"Greatest: divide the largest n-digit number by $L$ and subtract the remainder.",
            r"With a remainder r in the question, fit $Lk + r$ inside the range instead.",
        ],
        r"Multiples of the LCM are exactly the numbers divisible by every divisor; the digit bounds only pick where to stop.",
        r"Find the greatest five-digit number exactly divisible by 12, 15 and 20.",
        [
            r"$L = \text{LCM}(12, 15, 20) = 60$.",
            r"$99999 = 1666 \times 60 + 39$.",
            r"Greatest $= 99999 - 39 = 99960$.",
        ],
        "99960",
    ),
    pat(
        "hl-r2", "LCM + r with an extra condition", "common",
        r"An LCM plus remainder question carries one more filter, such as divisibility by another number or a digit bound.",
        r"N = Lk + r, \qquad \text{smallest } k \text{ meeting the condition wins}",
        [
            r"Write $N = L \times k + r$ with $L$ the LCM of the divisors.",
            r"Test $k = 1, 2, 3, \ldots$ against the extra condition.",
            r"With an n-digit bound, start k just above the bound minus r, divided by L.",
        ],
        r"N minus r is a multiple of L by construction; the extra condition only chooses which multiple.",
        r"Find the least number which leaves remainder 3 with 6, 7 and 8, and is divisible by 5.",
        [
            r"$L = \text{LCM}(6, 7, 8) = 168$, so $N = 168k + 3$.",
            r"Test k: $171, 339, 507, 675$; and $675 = 5 \times 135$.",
            r"$N = 675$.",
        ],
        "675",
    ),
    pat(
        "hl-r3", "Rebuild numbers from HCF and LCM; count pairs", "common",
        r"HCF and LCM are given with a sum, difference or bound; find the numbers, or count the possible pairs.",
        r"\text{numbers} = ha,\ hb; \quad \gcd(a, b) = 1, \quad ab = \dfrac{\text{LCM}}{h}",
        [
            r"Compute $ab = \text{LCM} \div h$ (or product $\div h^2$).",
            r"List factor pairs of $ab$ and keep only co-prime pairs.",
            r"Use the given sum or difference to pick the pair; the numbers are $ha$ and $hb$.",
            r"To count pairs, count the surviving co-prime pairs.",
        ],
        r"Two numbers with HCF h are h times two co-prime parts, and those parts must multiply to LCM divided by h.",
        r"The HCF and LCM of two numbers are 6 and 36. How many pairs of numbers fit?",
        [
            r"$ab = \dfrac{36}{6} = 6$.",
            r"Co-prime pairs of 6: $(1, 6)$ and $(2, 3)$.",
            r"Pairs: 6 with 36, and 12 with 18. That is 2 pairs.",
        ],
        "2",
    ),
    pat(
        "hl-r4", "Greatest number dividing with the same unknown remainder", "common",
        r"The question asks for the greatest number dividing a, b, c and leaving the same remainder in each case, with no remainder given.",
        r"\text{answer} = \gcd(a - b,\ b - c,\ a - c)",
        [
            r"Take the pairwise differences of the numbers.",
            r"The HCF of the differences is the greatest such divisor.",
            r"The common remainder is any number mod that HCF; confirm it is the same for all.",
        ],
        r"If two numbers leave the same remainder, their difference is exactly divisible by the divisor, so it divides every difference.",
        r"Find the greatest number which divides 61, 109 and 133 leaving the same remainder in each case.",
        [
            r"Differences: $109 - 61 = 48$, $133 - 109 = 24$, $133 - 61 = 72$.",
            r"$\gcd(48, 24, 72) = 24$.",
            r"Remainder: $61 \bmod 24 = 13$, and $109 \bmod 24 = 133 \bmod 24 = 13$.",
        ],
        "24",
    ),
    pat(
        "hl-r5", "LCM + r inside a digit bound", "common",
        r"The question asks for the least (or greatest) number of a given digit count leaving remainder r with several divisors.",
        r"N = L \times k + r, \quad 10^{n-1} \le N < 10^n",
        [
            r"Write $N = L \times k + r$ with $L$ the LCM of the divisors.",
            r"Least n-digit: take the smallest k with $Lk + r$ at or above the smallest n-digit number.",
            r"Greatest n-digit: take the largest k with $Lk + r$ at or below the largest n-digit number.",
            r"Check the remainder with every divisor.",
        ],
        r"The family of valid numbers is exactly LCM multiples plus r; the digit bound selects the first or last member.",
        r"Find the least four-digit number which leaves remainder 3 when divided by 6, 7 and 8.",
        [
            r"$L = \text{LCM}(6, 7, 8) = 168$, so $N = 168k + 3$.",
            r"Need $168k + 3 \ge 1000$, so $k \ge 5.97$, giving $k = 6$.",
            r"$N = 6 \times 168 + 3 = 1011$. Check: $1011 \bmod 6 = 1011 \bmod 7 = 1011 \bmod 8 = 3$.",
        ],
        "1011",
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


apply("hl-basics", HB_CONCEPT, HB_NOTES, HB_FORMULAS, HB_TRICKS, HB_MISTAKES, HB_REVISION, HB_PATTERNS)
apply("hl-methods", HM_CONCEPT, HM_NOTES, HM_FORMULAS, HM_TRICKS, HM_MISTAKES, HM_REVISION, HM_PATTERNS)
apply("hl-word-problems", HW_CONCEPT, HW_NOTES, HW_FORMULAS, HW_TRICKS, HW_MISTAKES, HW_REVISION, HW_PATTERNS)
apply("hl-remainder-cases", HR_CONCEPT, HR_NOTES, HR_FORMULAS, HR_TRICKS, HR_MISTAKES, HR_REVISION, HR_PATTERNS)

TOPIC.write_text(json.dumps(data, ensure_ascii=False, indent=1) + "\n", encoding="utf-8")
print("rewrote", TOPIC.name, "-", len(data["subtopics"]), "subtopics")
