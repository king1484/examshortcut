import math
from _lib import Sub


def build():
    S = Sub("ns-unit-digit")
    S.notes = r"""### What is the unit digit?
The **unit digit** is the last digit of a number (the ones place). In 4,587 the unit digit is 7. Exams ask for the unit digit of huge expressions like $7^{95} \times 3^{58}$ — numbers far too big to calculate. The good news: the unit digit of a product depends **only on the unit digits** of the numbers being multiplied. $1237 \times 48$ ends in the same digit as $7 \times 8 = 56$, i.e. 6.

### Powers repeat in a cycle
Write the powers of 7: $7, 49, 343, 2401, 16807 \dots$ Unit digits: 7, 9, 3, 1, 7, 9, 3, 1 … The pattern repeats every 4 powers. This repeating length is called **cyclicity**.

| Unit digit of base | Cycle of unit digits | Cycle length |
|---|---|---|
| 0, 1, 5, 6 | stays the same | 1 |
| 4 | 4, 6 | 2 (odd power 4, even power 6) |
| 9 | 9, 1 | 2 (odd power 9, even power 1) |
| 2 | 2, 4, 8, 6 | 4 |
| 3 | 3, 9, 7, 1 | 4 |
| 7 | 7, 9, 3, 1 | 4 |
| 8 | 8, 4, 2, 6 | 4 |

### The method for any power
1. Keep only the unit digit of the base: $2137^{754}$ → base digit 7.
2. Divide the exponent by 4 (only the last two digits of the exponent matter because 100 is a multiple of 4).
3. Remainder 1, 2, 3 → use that power. Remainder 0 → use power 4.
4. Read the unit digit: $754 \bmod 4 = 2$ → $7^2 = 49$ → answer 9.

### Products, sums and differences
- **Product:** find each unit digit, multiply them, keep the last digit.
- **Sum:** add the unit digits, keep the last digit.
- **Difference:** subtract the unit digits; if the result is negative, add 10. Example: $7^{105} - 3^{58}$ → 7 and 9 → $7 - 9 = -2$ → $10 - 2 = 8$. (This works only when the first number is actually bigger.)

### Shortcuts that save time
- Any even number × any number ending in 5 → unit digit 0.
- An odd number × a number ending in 5 → unit digit 5 (so $1 \times 3 \times 5 \times \dots \times 99$ ends in 5).
- $n!$ ends in 0 for every $n \ge 5$. So in $1! + 2! + \dots + 50!$ only $1! + 2! + 3! + 4! = 33$ matters → unit digit 3.
- Product of numbers ending in 1 and 6 keep the same digit when raised to any power.

### Power towers
For $17^{17^{17}}$ you need the exponent $17^{17}$ divided by 4. Since 17 leaves 1 with 4, $17^{17}$ also leaves 1. So the answer is the unit digit of $7^1 = 7$. For $3^{4^5}$ the exponent is a multiple of 4, so use $3^4$ → 1.

### Last two digits (bonus)
- Numbers ending in 1: last two digits of $(\dots a1)^n$ are: tens digit $= a \times (\text{unit digit of } n)$ (keep its last digit), units digit 1. Example: $31^{786}$ → $3 \times 6 = 18$ → 8 → **81**.
- Look for a power ending in 01: $7^4 = 2401$, so $7^{4k}$ ends in 01.

### Quick revision
- Only the base's unit digit and the exponent mod 4 matter.
- Remainder 0 → use the 4th power.
- 0, 1, 5, 6 never change; 4 and 9 have cycle 2.
- Even × 5 → 0; odd × 5 → 5; $n! \ (n \ge 5)$ → 0.
- Negative difference of unit digits → add 10.
"""

    S.pattern("ns-ud-p1", "Unit digit of a power or a product of powers", "very common",
        r"'Find the unit digit of $2137^{754}$' or of $4^{63} \times 9^{72} \times 8^{41}$.",
        r"\text{unit}(a^n) = \text{unit}\big(a^{\,n \bmod 4}\big),\ \text{use } 4 \text{ if } n \bmod 4 = 0",
        r"""1. Keep only the unit digit of each base.
2. Reduce each exponent mod 4 (mod 2 is enough for 4 and 9).
3. Find each unit digit and multiply them; keep the last digit.

Why: unit digits of powers repeat every 4 steps (or fewer).""",
        r"Find the unit digit of $(1573)^{47}$.",
        r"Base digit 3, $47 \bmod 4 = 3$ → $3^3 = 27$ → unit digit **7**.")
    S.pattern("ns-ud-p2", "Unit digit of a sum or difference of powers", "common",
        r"Powers joined by + or −, e.g. $7^{105} - 3^{58}$ or $2^{51} + 3^{52} + 4^{53} + 5^{54}$.",
        None,
        r"""1. Find the unit digit of each power separately.
2. Add (or subtract) those digits.
3. Keep the last digit; if a difference is negative, add 10.

Why: carrying and borrowing never affect the ones place beyond what the unit digits show.""",
        r"Find the unit digit of $6^{25} + 9^{31}$.",
        r"$6^{25}$ → 6. $9^{31}$ (odd) → 9. $6 + 9 = 15$ → unit digit **5**.")
    S.pattern("ns-ud-p3", "Unit digit of long products and factorial sums", "common",
        r"A product of several plain numbers, a product like $1 \times 3 \times 5 \times \dots$, or $1! + 2! + \dots + n!$.",
        None,
        r"""1. Look for an even number together with a 5 → answer 0 immediately.
2. For factorial sums, drop every term from $5!$ on (they end in 0).
3. Otherwise multiply unit digits step by step, keeping only the last digit.

Why: 2 × 5 = 10 produces a zero that stays forever.""",
        r"Find the unit digit of $1! + 2! + 3! + \dots + 99!$.",
        r"Terms from $5!$ end in 0. $1 + 2 + 6 + 24 = 33$ → unit digit **3**.")
    S.pattern("ns-ud-p4", "Power towers (exponent is itself a power)", "occasional",
        r"Expressions like $17^{17^{17}}$ or $3^{4^5}$.",
        r"a^{b^c}:\ \text{find } b^c \bmod 4 \text{ first}",
        r"""1. Find the remainder of the exponent $b^c$ when divided by 4 (use: odd $b$ with $b \bmod 4 = 1$ → 1; $b \bmod 4 = 3$ → 3 for odd $c$, 1 for even $c$; multiple of 4 → 0).
2. Use that remainder on the cycle of the base.

Why: only the exponent's position in the 4-cycle matters.""",
        r"Unit digit of $3^{4^5}$?",
        r"$4^5$ is a multiple of 4 → remainder 0 → use $3^4 = 81$ → **1**.")
    S.pattern("ns-ud-p5", "Last two digits of a power", "occasional",
        "'Find the last two digits of $31^{786}$' or of $7^{2008}$.",
        r"(10a+1)^n \text{ ends in } \big[(a \cdot n) \bmod 10\big]1",
        r"""1. If the base ends in 1: tens digit = (tens digit of base × unit digit of exponent), last digit only; units digit 1.
2. Otherwise find a power that ends in 01 (e.g. $7^4 = 2401$, $3^{20}$) and reduce the exponent.

Why: $(10a + 1)^n = 1 + 10an + (\text{multiples of } 100)$.""",
        r"Last two digits of $41^{27}$?",
        r"$4 \times 7 = 28$ → 8. Last two digits **81**.")

    v = pow(2137, 754, 10)
    assert v == 9
    S.q("ns-ud-p1", "easy", r"What is the unit digit of $(2137)^{754}$?",
        ["9", "1", "3", "7"], str(v),
        r"Unit digit of base = 7. $754 \bmod 4 = 2$ → $7^2 = 49$ → unit digit **9**.",
        "Only the last two digits of the exponent matter: 54 ÷ 4 leaves 2.", 30)
    v = (pow(4, 63, 10) * pow(9, 72, 10) * pow(8, 41, 10)) % 10
    assert v == 2
    S.q("ns-ud-p1", "medium", r"What is the unit digit of $4^{63} \times 9^{72} \times 8^{41}$?",
        ["2", "4", "6", "8"], str(v),
        r"""- $4^{63}$: odd power → 4.
- $9^{72}$: even power → 1.
- $8^{41}$: $41 \bmod 4 = 1$ → 8.
Product $4 \times 1 \times 8 = 32$ → unit digit **2**.""",
        None, 45)
    v = (pow(3694, 1793, 10) * pow(615, 317, 10) * pow(841, 491, 10)) % 10
    assert v == 0
    S.q("ns-ud-p1", "easy", r"What is the unit digit of $(3694)^{1793} \times (615)^{317} \times (841)^{491}$?",
        ["0", "4", "5", "2"], str(v),
        r"$(3694)^{1793}$ ends in 4 (odd power of 4). $(615)^{317}$ ends in 5. $(841)^{491}$ ends in 1. $4 \times 5 \times 1 = 20$ → unit digit **0**.",
        "Even × 5 → 0. No need to find exponents mod 4.", 30)

    v = (pow(7, 105) - pow(3, 58)) % 10
    assert v == 8
    S.q("ns-ud-p2", "medium", r"What is the unit digit of $7^{105} - 3^{58}$?",
        ["8", "2", "4", "6"], str(v),
        r"""$105 \bmod 4 = 1$ → $7^{105}$ ends in 7.
$58 \bmod 4 = 2$ → $3^{58}$ ends in 9.
$7 - 9$ is negative, so borrow: $17 - 9 = 8$. Unit digit **8**.""",
        "Trap 2 comes from doing 9 − 7. The first number is bigger, so borrow 10.", 45)
    v = (2 ** 51 + 3 ** 52 + 4 ** 53 + 5 ** 54) % 10
    assert v == 8
    S.q("ns-ud-p2", "medium", r"What is the unit digit of $2^{51} + 3^{52} + 4^{53} + 5^{54}$?",
        ["8", "6", "2", "0"], str(v),
        r"""- $2^{51}$: $51 \bmod 4 = 3$ → 8.
- $3^{52}$: $52 \bmod 4 = 0$ → use $3^4$ → 1.
- $4^{53}$: odd → 4.
- $5^{54}$ → 5.
Sum $= 8 + 1 + 4 + 5 = 18$ → **8**.""",
        None, 50)

    v = sum(math.factorial(i) for i in range(1, 51)) % 10
    assert v == 3
    S.q("ns-ud-p3", "easy", r"What is the unit digit of $1! + 2! + 3! + \dots + 50!$?",
        ["3", "0", "1", "7"], str(v),
        r"Every factorial from $5!$ onwards ends in 0. $1 + 2 + 6 + 24 = 33$ → unit digit **3**.",
        None, 30)
    v = (173 * 346 * 519 * 721) % 10
    assert v == 2
    S.q("ns-ud-p3", "easy", r"What is the unit digit of $173 \times 346 \times 519 \times 721$?",
        ["2", "4", "6", "8"], str(v),
        r"Unit digits: $3 \times 6 = 18 \to 8$; $8 \times 9 = 72 \to 2$; $2 \times 1 = 2$. Answer **2**.",
        None, 30)
    prod = 1
    for k in range(1, 100, 2):
        prod *= k
    v = prod % 10
    assert v == 5
    S.q("ns-ud-p3", "medium", r"What is the unit digit of the product $1 \times 3 \times 5 \times 7 \times \dots \times 99$ (all odd numbers from 1 to 99)?",
        ["5", "0", "1", "9"], str(v),
        r"The product contains 5 and has no even factor. Odd × (number ending in 5) always ends in 5. So the unit digit is **5**, not 0 (0 needs a factor 2).",
        None, 30)

    v = pow(17, 17 ** 17, 10)
    assert v == 7
    S.q("ns-ud-p4", "hard", r"What is the unit digit of $17^{17^{17}}$?",
        ["7", "9", "3", "1"], str(v),
        r"""We need the exponent $17^{17}$ divided by 4. $17 = 4 \times 4 + 1$, so every power of 17 leaves remainder 1 with 4.
So $17^{17^{17}}$ ends like $7^1$ → **7**.""",
        None, 50)
    v = pow(8, 7 ** 6, 10)
    assert v == 8 and (7 ** 6) % 4 == 1
    S.q("ns-ud-p4", "hard", r"What is the unit digit of $8^{7^{6}}$?",
        ["8", "4", "2", "6"], str(v),
        r"""Exponent $7^6$: $7 \equiv -1 \pmod 4$ and 6 is even, so $7^6$ leaves remainder 1 with 4.
So $8^{7^6}$ ends like $8^1$ → **8**.""",
        None, 50)

    v = pow(31, 786, 100)
    assert v == 81
    S.q("ns-ud-p5", "medium", r"What are the last two digits of $31^{786}$?",
        ["81", "61", "21", "41"], str(v),
        r"""$31^{786} = (30 + 1)^{786} = 1 + 786 \times 30 + (\text{multiples of } 100)$.
$786 \times 30 = 23580$ → ends in 80. $80 + 1 = 81$.""",
        r"Base ends in 1: tens digit $= 3 \times 6 = 18 \to 8$; answer 81.", 45)
    v = pow(7, 2008, 100)
    assert v == 1
    S.q("ns-ud-p5", "hard", r"What are the last two digits of $7^{2008}$?",
        ["01", "49", "43", "07"], "01",
        r"$7^4 = 2401$ ends in 01. $2008 = 4 \times 502$, so $7^{2008} = (7^4)^{502}$ ends in $01^{502}$ = **01**.",
        None, 50)
    return S
