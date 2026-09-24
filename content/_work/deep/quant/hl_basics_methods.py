"""Phase-2 deep content for quant/hcf-lcm — basics & methods modules."""
import os
import sys
from fractions import Fraction
from math import gcd

sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
from _lib import Sub, fr


def lcm(a, b):
    return a * b // gcd(a, b)


def build_basics():
    S = Sub("hl-basics")
    S.notes = r"""### What are HCF and LCM?
**HCF (Highest Common Factor, also called GCD)** of some numbers is the **largest** number that divides each of them exactly. **LCM (Lowest Common Multiple)** is the **smallest** number that is exactly divisible by each of them.
Example: for 12 and 18 the common factors are 1, 2, 3, 6, so HCF $= 6$; the multiples of 12 and 18 first meet at 36, so LCM $= 36$.

### Five rules that solve most questions
1. **Size order:** HCF $\le$ every number $\le$ LCM (for numbers $\ge 1$). An option that breaks this is wrong at sight.
2. **Product relation (two numbers only):** $\text{HCF} \times \text{LCM} = a \times b$. Check: $6 \times 36 = 216 = 12 \times 18$. It does **not** hold for three numbers — never use it there.
3. **Missing number:** if one number, the HCF and the LCM are known, the other number $= \frac{\text{HCF} \times \text{LCM}}{\text{given number}}$. Example: HCF 18, LCM 378, one number 54 → other $= \frac{18 \times 378}{54} = 126$.
4. **Co-prime numbers** (numbers whose HCF is 1): LCM = product. Consecutive integers are always co-prime, so their LCM is just their product.
5. **LCM is always a multiple of the HCF.** An option that is not a multiple of the given HCF is wrong at sight.

### Numbers given in a ratio
Numbers in ratio $a : b$ (with a, b co-prime) and HCF $h$ are $ha$ and $hb$:
- LCM $= h \cdot a \cdot b$, sum $= h(a + b)$, difference $= h(b - a)$, product $= h^2 ab$.
Example: ratio 3 : 4, HCF 6 → numbers 18 and 24 → LCM $= 6 \times 3 \times 4 = 72$, sum $= 42$.
Working backwards: if a 5 : 7 pair has LCM 140, then $h \times 5 \times 7 = 140$ → $h = 4$ → numbers 20 and 28.

### HCF of numbers that are close or related
- The HCF divides every **difference**: $\gcd(a, b)$ divides $a - b$. So two numbers 20 apart can never have HCF 12 — a fast option-killer.
- Consecutive integers: HCF = 1, LCM = their product.
- **"Other factors of the LCM":** if the HCF is $h$ and the remaining factors of the LCM are $m$ and $n$ (co-prime), the numbers are $hm$ and $hn$, and LCM $= hmn$.
Example: HCF 23 with other factors 13 and 14 → numbers 299 and 322, LCM $= 23 \times 13 \times 14 = 4186$.

### Counting pairs (a preview)
"How many pairs of numbers have product P and HCF h?" — write them as $ha, hb$ with $\gcd(a, b) = 1$, so $ab = \frac{P}{h^2}$. The answer is the number of **co-prime** factor pairs of $\frac{P}{h^2}$ (worked fully in the two-step-cases subtopic).

### Quick revision
- Two numbers: HCF × LCM = product. Three numbers: no such rule.
- Co-prime → HCF 1, LCM = product. Consecutive integers are co-prime.
- Ratio a : b with HCF h → numbers ha, hb; LCM = hab; sum = h(a + b).
- LCM is a multiple of the HCF; HCF divides every difference.
"""

    S.pattern("hl-b1", "Find the HCF or LCM of small numbers directly", "very common",
        r"'Find the HCF of 96 and 404' or 'the LCM of 12, 15 and 20 is' — plain computation, no story.",
        r"\text{HCF} = \text{common primes, lowest powers}; \quad \text{LCM} = \text{all primes, highest powers}",
        r"""1. Factorise each number into primes.
2. HCF: multiply the primes common to ALL numbers, taking the lowest power of each.
3. LCM: multiply every prime that appears, taking the highest power of each.

Why: a common divisor cannot use more of any prime than the number with the fewest; a common multiple needs at least the richest stock of every prime.""",
        r"Find the LCM of 16, 24 and 36.",
        r"$16 = 2^4$, $24 = 2^3 \cdot 3$, $36 = 2^2 \cdot 3^2$. LCM $= 2^4 \times 3^2 = 144$.")
    S.pattern("hl-b2", "HCF × LCM = product (two numbers)", "very common",
        "Any two of {product, HCF, LCM, one number} are given and a third is asked.",
        r"\text{HCF} \times \text{LCM} = a \times b \ \Rightarrow\ b = \frac{\text{HCF} \times \text{LCM}}{a}",
        r"""1. Write the product relation (valid for exactly two numbers).
2. Fill in the three known values and divide to get the fourth.
3. Sanity check: the HCF must divide the LCM.

Why: writing $a = ha'$, $b = hb'$ with co-prime $a', b'$, the LCM is $ha'b'$, so HCF × LCM $= h^2 a'b' = ab$.""",
        r"The HCF of two numbers is 18 and their LCM is 378. If one number is 54, find the other.",
        r"Other $= \frac{18 \times 378}{54} = \frac{6804}{54} = 126$. Check: $\gcd(54, 126) = 18$ and LCM $= 378$.")
    S.pattern("hl-b3", "Numbers in a given ratio, HCF or LCM known", "very common",
        "'Two numbers are in ratio m : n and their HCF (or LCM) is …' — then a sum, difference or the LCM is asked.",
        r"\text{numbers} = hm, hn; \quad \text{LCM} = hmn, \quad \text{sum} = h(m+n)",
        r"""1. Treat the ratio parts m, n as co-prime (cancel the ratio first if needed).
2. HCF given: numbers are hm and hn. LCM given: $h = \frac{\text{LCM}}{mn}$.
3. Answer whatever is asked (sum, difference, product, LCM).

Why: the ratio fixes only the shape; the HCF is the scale factor h.""",
        r"Two numbers are in the ratio 5 : 7 and their LCM is 140. Find the difference of the numbers.",
        r"$h = \frac{140}{5 \times 7} = 4$ → numbers 20 and 28 → difference $8$.")
    S.pattern("hl-b4", "HCF given with the 'other factors' of the LCM", "common",
        "'The HCF of two numbers is 29 and the other two factors of their LCM are 15 and 13. Find the numbers.'",
        r"\text{numbers} = hm, hn \ \ (m, n \text{ co-prime}); \quad \text{LCM} = hmn",
        r"""1. The numbers are h × (first other factor) and h × (second other factor).
2. The two 'other factors' must be co-prime — if not, the data is impossible.
3. LCM = h × m × n if it is asked too.

Why: LCM = HCF × (leftover co-prime parts), by the structure of HCF and LCM.""",
        r"The HCF of two numbers is 23 and the other two factors of their LCM are 13 and 14. Find the greater number.",
        r"Numbers: $23 \times 13 = 299$ and $23 \times 14 = 322$. Greater $= 322$. (LCM would be $23 \times 13 \times 14 = 4186$.)")
    S.pattern("hl-b5", "Co-prime, consecutive and other property questions", "common",
        "'The LCM of two co-prime numbers is …, one is …' or 'which pair is co-prime?' — the word co-prime or consecutive appears.",
        r"\gcd(a, b) = 1 \Rightarrow \text{LCM} = ab; \qquad \gcd(a, b) \mid (a - b)",
        r"""1. Co-prime + LCM given: divide the LCM by the given number to get the other.
2. 'Which pair is co-prime?': test each pair for a common factor > 1.
3. Difference-based checks: the HCF must divide the difference of the numbers.

Why: with no common prime, nothing cancels — so the LCM is the plain product.""",
        "The LCM of two co-prime numbers is 221 and one of them is 13. Find the other.",
        r"Co-prime → LCM = product → other $= \frac{221}{13} = 17$. (Indeed $221 = 13 \times 17$.)")

    assert gcd(72, 120) == 24 and lcm(72, 120) == 360
    S.q("hl-b1", "easy", r"What is the HCF of 72 and 120?",
        ["24", "12", "36", "6"], "24",
        r"""$72 = 2^3 \times 3^2$, $120 = 2^3 \times 3 \times 5$.
Common primes with lowest powers: $2^3 \times 3 = 24$.""",
        r"Both divide by 24: $72 = 3 \times 24$, $120 = 5 \times 24$; nothing bigger does.", 35)
    L = lcm(lcm(16, 24), 36)
    assert L == 144
    S.q("hl-b1", "medium", "What is the LCM of 16, 24 and 36?",
        ["144", "72", "288", "96"], "144",
        r"""$16 = 2^4$, $24 = 2^3 \times 3$, $36 = 2^2 \times 3^2$.
LCM $= 2^4 \times 3^2 = 16 \times 9 = 144$.""",
        "72 uses $2^3$ (one 2 short); 288 is a common multiple but not the least.", 45)
    o = 18 * 378 // 54
    assert o == 126 and gcd(54, 126) == 18 and lcm(54, 126) == 378
    S.q("hl-b2", "easy",
        "The HCF of two numbers is 18 and their LCM is 378. If one number is 54, find the other number.",
        ["126", "108", "144", "162"], "126",
        r"""$\text{HCF} \times \text{LCM} = a \times b$ → other $= \frac{18 \times 378}{54} = 126$.
Check: $\gcd(54, 126) = 18$ and LCM$(54, 126) = 378$ ✓.""",
        None, 40)
    L = 2160 // 12
    assert L == 180 and L % 12 == 0
    S.q("hl-b2", "easy",
        "The product of two numbers is 2160 and their HCF is 12. Find their LCM.",
        ["180", "160", "150", "210"], "180",
        r"""$\text{LCM} = \frac{\text{product}}{\text{HCF}} = \frac{2160}{12} = 180$.
Check: 180 is a multiple of the HCF 12 ✓.""",
        None, 30)
    assert 3 * 6 == 18 and 4 * 6 == 24 and lcm(18, 24) == 72 and 18 + 24 == 42
    S.q("hl-b3", "easy",
        "Two numbers are in the ratio 3 : 4 and their HCF is 6. Find the sum of the numbers.",
        ["42", "35", "48", "40"], "42",
        r"""Numbers: $3 \times 6 = 18$ and $4 \times 6 = 24$. Sum $= 42$.
(Their LCM is $6 \times 3 \times 4 = 72$.)""",
        "Sum = HCF × (sum of ratio parts) = 6 × 7 = 42.", 35)
    h = 140 // (5 * 7)
    assert h == 4 and gcd(20, 28) == 4 and lcm(20, 28) == 140 and 28 - 20 == 8
    S.q("hl-b3", "medium",
        "Two numbers are in the ratio 5 : 7 and their LCM is 140. Find the difference between the numbers.",
        ["8", "12", "4", "16"], "8",
        r"""$\text{LCM} = h \times 5 \times 7 = 35h = 140$ → $h = 4$.
Numbers: 20 and 28 → difference $= 8$.""",
        None, 45)
    a, b = 23 * 13, 23 * 14
    assert a == 299 and b == 322 and gcd(a, b) == 23 and lcm(a, b) == 23 * 13 * 14
    S.q("hl-b4", "medium",
        "The HCF of two numbers is 23 and the other two factors of their LCM are 13 and 14. Find the greater number.",
        ["322", "299", "4186", "345"], "322",
        r"""Numbers: $23 \times 13 = 299$ and $23 \times 14 = 322$.
Their LCM is $23 \times 13 \times 14 = 4186$ ✓. Greater number $= 322$.""",
        "4186 is the LCM, not a number; 299 is the smaller one.", 45)
    a, b = 17 * 11, 17 * 13
    assert a == 187 and b == 221 and gcd(a, b) == 17 and lcm(a, b) == 17 * 11 * 13
    S.q("hl-b4", "medium",
        "The HCF of two numbers is 17 and the other two factors of their LCM are 11 and 13. Find the greater number.",
        ["221", "187", "2431", "204"], "221",
        r"""Numbers: $17 \times 11 = 187$ and $17 \times 13 = 221$ (11 and 13 are co-prime).
Greater number $= 221$. The LCM is $17 \times 11 \times 13 = 2431$.""",
        None, 45)
    assert 221 == 13 * 17 and gcd(13, 17) == 1
    S.q("hl-b5", "easy",
        "The LCM of two co-prime numbers is 221. If one of them is 13, find the other number.",
        ["17", "13", "221", "34"], "17",
        r"""Co-prime numbers have HCF 1, so LCM = product.
Other number $= \frac{221}{13} = 17$.""",
        None, 30)
    pairs = [("14 and 21", (14, 21)), ("16 and 25", (16, 25)), ("27 and 36", (27, 36)), ("30 and 48", (30, 48))]
    cop = [l for l, (x, y) in pairs if gcd(x, y) == 1]
    assert cop == ["16 and 25"], cop
    S.q("hl-b5", "medium",
        "Which one of the following pairs of numbers is co-prime?",
        [p[0] for p in pairs], "16 and 25",
        r"""Co-prime means HCF = 1.
$\gcd(14, 21) = 7$, $\gcd(27, 36) = 9$, $\gcd(30, 48) = 6$, but $\gcd(16, 25) = 1$.
So 16 and 25 are co-prime.""",
        "Two numbers need not both be prime to be co-prime — 16 and 25 are not prime, yet share no factor.", 40)
    return S


def build_methods():
    S = Sub("hl-methods")
    S.notes = r"""### The two standard methods
**1. Prime factorisation (best for two to four numbers).** Write every number as a product of primes.
- HCF = product of the primes **common to all**, each with its **lowest** power.
- LCM = product of **all** primes that appear, each with its **highest** power.
Example: $32 = 2^5$, $36 = 2^2 \cdot 3^2$, $45 = 3^2 \cdot 5$ → nothing is common to all three, so HCF $= 1$; LCM $= 2^5 \cdot 3^2 \cdot 5 = 1440$.
A small table helps: one row per number, one column per prime. HCF = read column **minima**; LCM = read column **maxima**.

**2. Long (successive) division (fastest for two big numbers).** Divide the bigger number by the smaller; then keep dividing the last divisor by the last remainder. The last non-zero divisor is the HCF. Then LCM $= \frac{a \times b}{\text{HCF}}$.
Example: HCF of 4052 and 12576:
$12576 = 3 \times 4052 + 420$ → $4052 = 9 \times 420 + 272$ → $420 = 272 + 148$ → $272 = 148 + 124$ → $148 = 124 + 24$ → $124 = 5 \times 24 + 4$ → $24 = 6 \times 4 + 0$. HCF $= 4$.
For three numbers: take the HCF of the first two, then the HCF of that value with the third.

### Fractions: the cross rule
$$\text{HCF} = \frac{\text{HCF of numerators}}{\text{LCM of denominators}}, \qquad \text{LCM} = \frac{\text{LCM of numerators}}{\text{HCF of denominators}}$$
Example: HCF of $\frac{2}{3}, \frac{8}{9}, \frac{10}{27}$ is $\frac{\gcd(2, 8, 10)}{\text{LCM}(3, 9, 27)} = \frac{2}{27}$.
Why it works: writing all fractions over the LCM of the denominators turns them into whole numbers; the HCF (or LCM) of those whole numbers, divided back by that LCM of denominators, gives exactly this rule.

### Decimals: shift the point, then shift it back
1. Multiply every number by the same power of 10 so all become integers (use as many zeros as the largest number of decimal places).
2. Find the HCF or LCM of the integers.
3. Put the decimal point back with that many places.
Example: HCF of $0.54, 1.8, 7.2$ → work with $54, 180, 720$ → HCF $= 18$ → answer $0.18$.

### Numbers already given as prime products
If the numbers come as $2^3 \cdot 3 \cdot 5$-style products, skip factorising: HCF takes the **minimum** power of each prime across the numbers, LCM the **maximum**. Example: HCF of $2^3 \cdot 3^2 \cdot 5^4$ and $2^2 \cdot 3^3 \cdot 5^2$ is $2^2 \cdot 3^2 \cdot 5^2 = 180$.

### Choosing a method fast
- Small numbers (say up to 100): factorise mentally.
- Two big numbers: long division.
- Prime-product form: read min/max powers directly.
- Fractions: cross rule. Decimals: clear the point, restore it at the end.

### Quick revision
- HCF: common primes, lowest powers. LCM: every prime, highest powers.
- Division method: last non-zero divisor is the HCF; LCM = product ÷ HCF.
- Fractions: HCF of tops over LCM of bottoms (and the mirror image for LCM).
- Decimals: clear the decimal point first, restore the same number of places at the end.
"""

    S.pattern("hl-m1", "HCF by successive (long) division", "common",
        "Two or three larger numbers and the HCF is asked — the numbers are too big to factorise comfortably.",
        r"\gcd(a, b): \text{ divide } a \text{ by } b, \text{ then } b \text{ by the remainder, } \dots \text{ last non-zero divisor is the HCF}; \quad \text{LCM} = \frac{ab}{\gcd(a,b)}",
        r"""1. Divide the bigger number by the smaller; note the remainder.
2. Divide the old divisor by the remainder; repeat until the remainder is 0.
3. The last non-zero divisor is the HCF. For a third number, repeat with (HCF, third number).
4. LCM of two numbers = product ÷ HCF.

Why: any common divisor of a and b also divides every remainder, so the process preserves the common divisors while shrinking the numbers.""",
        r"Find the HCF of 4052 and 12576.",
        r"$12576 = 3 \times 4052 + 420$ → $4052 = 9 \times 420 + 272$ → … → $24 = 6 \times 4 + 0$. HCF $= 4$.")
    S.pattern("hl-m2", "HCF / LCM from prime-power form (min vs max powers)", "common",
        "The numbers are given as prime products, like $2^3 \\times 3^2 \\times 5^4$, or the HCF and LCM of power-form numbers are asked.",
        r"\text{HCF} = \prod p_i^{\min}, \qquad \text{LCM} = \prod p_i^{\max}",
        r"""1. List each prime that appears anywhere.
2. HCF: for each prime take the SMALLEST exponent across all the numbers (skip primes missing from any number).
3. LCM: for each prime take the LARGEST exponent anywhere.
4. Multiply out only at the end.

Why: the HCF must fit inside every number; the LCM must contain every number.""",
        r"Find the HCF of $2^3 \times 3^2 \times 5^4$, $2^2 \times 3^3 \times 5^2$ and $2^4 \times 3 \times 5^3$.",
        r"Lowest powers: $2^2$, $3^1$, $5^2$ → HCF $= 4 \times 3 \times 25 = 300$. (The LCM would be $2^4 \times 3^3 \times 5^4$. )")
    S.pattern("hl-m3", "HCF and LCM of fractions (cross rule)", "very common",
        "A list of fractions like 2/3, 8/9, 10/27 with HCF or LCM asked.",
        r"\text{HCF} = \frac{\gcd(\text{numerators})}{\text{LCM}(\text{denominators})}, \qquad \text{LCM} = \frac{\text{LCM}(\text{numerators})}{\gcd(\text{denominators})}",
        r"""1. Reduce each fraction to lowest terms first.
2. For the HCF: HCF of the tops, LCM of the bottoms.
3. For the LCM: LCM of the tops, HCF of the bottoms.
4. Sanity check: every given fraction ÷ HCF should be a whole number; LCM ÷ every fraction should be a whole number.

Why: putting all fractions over the LCM of denominators turns them into integers, and the ordinary HCF/LCM of those integers gives the rule.""",
        r"Find the HCF of $\frac{2}{3}$, $\frac{8}{9}$ and $\frac{10}{27}$.",
        r"$\frac{\gcd(2, 8, 10)}{\text{LCM}(3, 9, 27)} = \frac{2}{27}$. Check: each fraction ÷ $\frac{2}{27}$ is whole (9, 12, 5).")
    S.pattern("hl-m4", "HCF and LCM of decimals", "common",
        "Decimals like 0.54, 1.8, 7.2 with HCF or LCM asked — answers have a decimal point.",
        r"\text{scale by } 10^k \to \gcd/\text{lcm of integers} \to \text{scale back by } 10^k",
        r"""1. Count the largest number of decimal places among the values.
2. Multiply every value by that power of 10 so all become integers.
3. Find the HCF or LCM of the integers.
4. Divide the result by the same power of 10.

Why: multiplying everything by a common scale factor multiplies HCF and LCM by the same factor — so undo it at the end.""",
        "Find the LCM of 0.12, 0.18 and 0.30.",
        r"× 100 → 12, 18, 30 → LCM 180 → restore two places → 1.80. Check: $1.8 \div 0.12 = 15$ ✓.")

    assert gcd(135, 225) == 45
    S.q("hl-m1", "easy", "Find the HCF of 135 and 225 using the division method.",
        ["45", "15", "75", "27"], "45",
        r"""$225 = 1 \times 135 + 90$; $135 = 1 \times 90 + 45$; $90 = 2 \times 45 + 0$.
Last non-zero divisor $= 45$.""",
        None, 35)
    assert gcd(4052, 12576) == 4
    S.q("hl-m1", "hard", "Find the HCF of 4052 and 12576.",
        ["4", "8", "12", "2"], "4",
        r"""Successive division: $12576 = 3 \times 4052 + 420$ → $4052 = 9 \times 420 + 272$ → $420 = 272 + 148$ → $272 = 148 + 124$ → $148 = 124 + 24$ → $124 = 5 \times 24 + 4$ → $24 = 6 \times 4 + 0$.
HCF $= 4$.""",
        None, 75)
    assert gcd(gcd(96, 240), 384) == 48
    S.q("hl-m1", "medium", "Find the HCF of 96, 240 and 384.",
        ["48", "24", "96", "16"], "48",
        r"""$\gcd(96, 240)$: $240 = 2 \times 96 + 48$; $96 = 2 \times 48 + 0$ → 48.
$\gcd(48, 384)$: 384 is a multiple of 48 → HCF of all three $= 48$.""",
        None, 45)
    h = gcd(gcd(2 ** 3 * 3 ** 2 * 5 ** 4, 2 ** 2 * 3 ** 3 * 5 ** 2), 2 ** 4 * 3 * 5 ** 3)
    assert h == 2 ** 2 * 3 * 5 ** 2 == 300
    S.q("hl-m2", "medium",
        r"Find the HCF of $2^3 \times 3^2 \times 5^4$, $2^2 \times 3^3 \times 5^2$ and $2^4 \times 3 \times 5^3$.",
        ["300", "900", "150", "60"], "300",
        r"""Take each prime at its lowest power across the three numbers:
$2^2$ (lowest of 3, 2, 4), $3^1$ (lowest of 2, 3, 1), $5^2$ (lowest of 4, 2, 3).
HCF $= 4 \times 3 \times 25 = 300$.""",
        "900 picks $3^2$ — but the third number has only $3^1$.", 50)
    assert lcm(2 ** 3 * 3 ** 2, 2 * 3 ** 4) == 2 ** 3 * 3 ** 4 == 648
    S.q("hl-m2", "easy", r"Find the LCM of $2^3 \times 3^2$ and $2 \times 3^4$.",
        ["648", "216", "324", "72"], "648",
        r"""Highest powers: $2^3$ and $3^4$.
LCM $= 8 \times 81 = 648$.""",
        "216 = $2^3 \\times 3^3$ takes the wrong (lower) power of 3.", 35)
    h, L, one = 2 ** 3 * 3, 2 ** 5 * 3 ** 3 * 5, 2 ** 3 * 3 * 5
    other = h * L // one
    assert h == 24 and L == 4320 and one == 120 and other == 864
    assert gcd(one, other) == h and lcm(one, other) == L
    S.q("hl-m2", "hard",
        r"The HCF of two numbers is $2^3 \times 3$ and their LCM is $2^5 \times 3^3 \times 5$. If one number is $2^3 \times 3 \times 5$, find the other number.",
        ["864", "432", "288", "720"], "864",
        r"""Other $= \frac{\text{HCF} \times \text{LCM}}{\text{given number}} = \frac{(2^3 \times 3) \times (2^5 \times 3^3 \times 5)}{2^3 \times 3 \times 5} = 2^5 \times 3^3 = 864$.
Check: $\gcd(120, 864) = 24$ ✓ and LCM$(120, 864) = 4320$ ✓.""",
        None, 70)
    F1, F2 = Fraction(4, 9), Fraction(10, 21)
    LF = Fraction(lcm(F1.numerator, F2.numerator), gcd(F1.denominator, F2.denominator))
    assert LF == Fraction(20, 3) and (LF / F1).denominator == 1 and (LF / F2).denominator == 1
    S.q("hl-m3", "easy",
        r"Find the LCM of $\frac{4}{9}$ and $\frac{10}{21}$.",
        [fr(Fraction(20, 3)), fr(Fraction(40, 63)), fr(Fraction(20, 9)), fr(Fraction(2, 3))], fr(Fraction(20, 3)),
        r"""LCM of numerators: $\text{LCM}(4, 10) = 20$. HCF of denominators: $\gcd(9, 21) = 3$.
LCM $= \frac{20}{3}$.
Check: $\frac{20}{3} \div \frac{4}{9} = 15$ ✓ and $\frac{20}{3} \div \frac{10}{21} = 14$ ✓ — both whole.""",
        r"Trap $\frac{40}{63}$ divides the LCM of tops by the LCM of bottoms — the bottoms need the HCF.", 40)
    HF = Fraction(gcd(gcd(8, 16), 20), lcm(lcm(9, 27), 81))
    assert HF == Fraction(4, 81)
    assert all((Fraction(f) / HF).denominator == 1 for f in ("8/9", "16/27", "20/81"))
    S.q("hl-m3", "medium",
        r"Find the HCF of $\frac{8}{9}$, $\frac{16}{27}$ and $\frac{20}{81}$.",
        [fr(Fraction(4, 81)), fr(Fraction(4, 9)), fr(Fraction(8, 81)), fr(Fraction(20, 81))], fr(Fraction(4, 81)),
        r"""HCF of numerators: $\gcd(8, 16, 20) = 4$. LCM of denominators: $\text{LCM}(9, 27, 81) = 81$.
HCF $= \frac{4}{81}$.""",
        None, 45)
    assert lcm(lcm(12, 18), 30) == 180
    assert 180 / 0.12 == 1500 and 180 / 0.18 == 1000 and 180 / 0.30 == 600
    S.q("hl-m4", "easy", "Find the LCM of 0.12, 0.18 and 0.30.",
        ["1.8", "0.9", "3.6", "18"], "1.8",
        r"""Clear decimals (× 100): 12, 18, 30 → LCM $= 180$.
Two decimal places → answer $= 1.80$.
Check: $1.8 \div 0.12 = 15$, $1.8 \div 0.18 = 10$, $1.8 \div 0.30 = 6$ — all whole ✓.""",
        None, 40)
    assert gcd(gcd(144, 360), 72) == 72
    S.q("hl-m4", "medium", "Find the HCF of 1.44, 3.6 and 0.72.",
        ["0.72", "0.36", "0.18", "7.2"], "0.72",
        r"""Clear decimals (× 100): 144, 360, 72 → $\gcd = 72$.
Restore two decimal places → HCF $= 0.72$.
Check: $1.44 \div 0.72 = 2$, $3.6 \div 0.72 = 5$, $0.72 \div 0.72 = 1$ ✓.""",
        "0.36 also divides all three, but the HCF must be the greatest such number.", 45)
    return S
