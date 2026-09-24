import math
from _lib import Sub, ind


def build():
    S = Sub("ns-remainders")
    S.notes = r"""### What is a remainder?
When you share 47 sweets among 5 children equally, each gets 9 and 2 are left over. Here 47 is the **dividend**, 5 the **divisor**, 9 the **quotient** and 2 the **remainder**. The remainder is always smaller than the divisor.

### The division formula
$$\text{Dividend} = \text{Divisor} \times \text{Quotient} + \text{Remainder}$$
$47 = 5 \times 9 + 2$. Almost every "find the dividend / divisor" question is just this formula. Example: divisor 24, quotient 13, remainder 17 → dividend $= 24 \times 13 + 17 = 329$.

### Rule 1: divisor-multiple rule
If $N$ leaves remainder $r$ when divided by $D$, and $d$ is a **factor** of $D$, then $N$ leaves $r \bmod d$ when divided by $d$.
Example: $N \div 342$ leaves 47. Since $342 = 18 \times 19$, $N \div 18$ leaves $47 \bmod 18 = 11$.
If $d$ is **not** a factor of $D$, the remainder cannot be fixed.

### Rule 2: remainders of sums and products
The remainder of a sum (or product) = remainder of the sum (or product) of the individual remainders.
Example: $(1021 \times 1023 \times 1025) \div 17$: remainders 1, 3, 5 → $1 \times 3 \times 5 = 15$ → remainder 15.
This lets you replace huge numbers by tiny ones before multiplying.

### Rule 3: negative remainders
A remainder can be written as a negative number to keep things small. $67 \div 68$ leaves 67, which is the same as $-1$. So $67^{67} \div 68$ leaves $(-1)^{67} = -1$, i.e. $68 - 1 = 67$. If your final answer is negative, add the divisor.

### Rule 4: large powers
Look for a small power that gives remainder $1$ or $-1$.
- $2^3 = 8$ leaves 1 with 7, so $2^{100} = (2^3)^{33} \times 2$ leaves $1 \times 2 = 2$.
- $5^2 = 25$ leaves $-1$ with 13, so $5^4$ leaves 1.
- **Base one more than divisor:** $(d+1)^n \div d$ always leaves 1.
- **Base one less than divisor:** $(d-1)^n \div d$ leaves 1 if $n$ is even, $d - 1$ if $n$ is odd.
- **Fermat's rule:** if $p$ is prime and does not divide $a$, then $a^{p-1}$ leaves 1 with $p$.

### Rule 5: remainder of $kN$, $N^2$, $N^3$
If $N \div d$ leaves $r$, then $kN$ leaves $kr \bmod d$ and $N^2$ leaves $r^2 \bmod d$. Just work with $r$.

### Rule 6: successive division
"Divided successively by 3 and 5 leaves remainders 2 and 3" means: divide $N$ by 3 (remainder 2), then divide that **quotient** by 5 (remainder 3). Work backwards from the last step: start with the smallest quotient 0 (or 1 if asked), and rebuild: $x = \text{divisor} \times \text{next} + \text{remainder}$.

### Rule 7: sum of factorials
From $4! = 24$ onwards every factorial is a multiple of 12, and from $5!$ onwards a multiple of 10 and 120. So for $1! + 2! + \dots + 100!$ divided by 12, only $1! + 2! + 3! = 9$ matters.

### Quick revision
- Dividend = divisor × quotient + remainder; remainder < divisor.
- New divisor is a factor of the old → answer = old remainder mod new divisor.
- Reduce each number first, then add/multiply the remainders.
- Use $\pm 1$ remainders for big powers; add the divisor to a negative answer.
- $(d+1)^n \to 1$; $(d-1)^n \to 1$ or $d-1$.
- Successive division: rebuild from the last divisor backwards.
"""

    S.pattern("ns-rm-p1", "Remainder with a factor of the old divisor", "very common",
        "'A number divided by 527 leaves 64; what is the remainder when it is divided by 17?' — the new divisor divides the old one.",
        r"N = Dq + r,\ d \mid D \Rightarrow N \bmod d = r \bmod d",
        r"""1. Check that the new divisor $d$ is a factor of the old divisor $D$.
2. Answer $= r \bmod d$ (divide the old remainder by the new divisor).

Why: $Dq$ is a multiple of $d$, so only $r$ decides the remainder.""",
        "A number leaves remainder 29 when divided by 91. Find the remainder when it is divided by 13.",
        r"$91 = 7 \times 13$, so 13 is a factor. $29 \bmod 13 = 3$. Answer **3**.")
    S.pattern("ns-rm-p2", "Remainder of a product or sum of numbers", "very common",
        r"'Find the remainder when $1021 \times 1023 \times 1025$ is divided by 17' or a sum of factorials divided by a small number.",
        r"(a \times b) \bmod d = [(a \bmod d)(b \bmod d)] \bmod d",
        r"""1. Replace each number by its remainder (negative remainders are allowed).
2. Multiply/add the small remainders, reducing again when needed.
3. If the final value is negative, add the divisor.

Why: every number is (multiple of $d$) + remainder, and the multiples of $d$ never affect the remainder.""",
        r"Find the remainder when $98 \times 97 \times 96$ is divided by 99.",
        r"Remainders $-1, -2, -3$. Product $= -6$ → add 99 → **93**.")
    S.pattern("ns-rm-p3", "Remainder of a large power", "very common",
        r"A power like $5^{70}$, $3^{101}$ or $67^{67} + 67$ divided by a small number.",
        r"a^{p-1} \equiv 1 \pmod p,\quad (d-1)^n \equiv (-1)^n \pmod d",
        r"""1. Reduce the base with respect to the divisor.
2. Find the smallest power that gives remainder 1 or −1.
3. Split the exponent using that power; handle the leftover part.

Why: once some power gives 1, the remainders repeat in a cycle.""",
        r"Find the remainder when $2^{100}$ is divided by 7.",
        r"$2^3 = 8 \equiv 1$. $2^{100} = (2^3)^{33} \times 2 \equiv 1 \times 2$. Remainder **2**.")
    S.pattern("ns-rm-p4", "Division formula: find dividend, divisor or a new remainder", "common",
        "Relations like 'divisor is 5 times the quotient and 3 times the remainder', or 'a number divided by 68 gives quotient 269 and remainder 0; find the remainder with 67'.",
        r"\text{Dividend} = \text{Divisor} \times \text{Quotient} + \text{Remainder}",
        r"""1. Write the unknowns in terms of the one given value (usually the remainder).
2. Find divisor and quotient, then use the formula.
3. For a changed divisor, compute the number first, then divide again.

Why: the formula is the definition of division; everything else is substitution.""",
        "In a division, the divisor is 3 times the remainder and the quotient is 12. If the remainder is 7, find the dividend.",
        r"Divisor $= 21$. Dividend $= 21 \times 12 + 7 = 259$.")
    S.pattern("ns-rm-p5", r"Remainder of $kN$, $N^2$ or a combination, given $N \bmod d$", "common",
        "'When N is divided by 7 the remainder is 3. Find the remainder when $N^3 + 2N$ is divided by 7.' Or two numbers' remainders are given and their sum/product is asked.",
        r"N \equiv r \Rightarrow kN \equiv kr,\ N^2 \equiv r^2 \pmod d",
        r"""1. Replace $N$ by its remainder $r$ everywhere.
2. Simplify and reduce by $d$.
3. Quick check: take the smallest such $N$ (e.g. $N = r$) and divide directly.

Why: $N = dq + r$, and every term containing $dq$ is a multiple of $d$.""",
        "N leaves remainder 5 when divided by 9. What remainder does 4N leave?",
        r"$4 \times 5 = 20$, $20 \bmod 9 = 2$. Answer **2**.")
    S.pattern("ns-rm-p6", "Successive division", "occasional",
        "'A number is divided successively by 3, 5 and 7 leaving remainders 2, 3, 4' — each divisor acts on the previous quotient.",
        r"x = d_1 y + r_1,\ y = d_2 z + r_2,\ \dots",
        r"""1. Start from the last divisor: take its quotient as 0 (smallest number) unless told otherwise.
2. Rebuild backwards: number = divisor × (next number) + remainder.
3. For the remainder with the product of divisors, the smallest number itself is the answer.

Why: successive division is just the division formula applied again and again.""",
        "Find the smallest number that leaves remainders 1 and 2 when divided successively by 4 and 5.",
        r"Last step: quotient 0, so the second number $= 2$. First number $= 4 \times 2 + 1 = 9$. Check: $9 \div 4 = 2$ r 1, $2 \div 5 = 0$ r 2 ✓.")

    # practice
    v = 64 % 17
    assert 527 == 17 * 31 and v == 13
    S.q("ns-rm-p1", "easy", "A number when divided by 527 leaves a remainder of 64. What will be the remainder when the same number is divided by 17?",
        ["13", "64", "12", "4"], str(v),
        r"$527 = 17 \times 31$, so 17 is a factor of 527. Remainder $= 64 \bmod 17 = 64 - 51 = 13$.",
        "Old remainder ÷ new divisor.", 30)
    v = 71 % 12
    assert 84 % 12 == 0 and v == 11
    S.q("ns-rm-p1", "easy", "A number divided by 84 leaves remainder 71. What is the remainder when the number is divided by 12?",
        ["11", "7", "1", "5"], str(v),
        r"12 divides 84, so the remainder is $71 \bmod 12 = 71 - 60 = 11$.",
        None, 25)
    v = 47 % 15
    assert 195 % 15 == 0 and v == 2
    S.q("ns-rm-p1", "medium", "When a number is divided by 195 the remainder is 47. When the same number is divided by 15, the remainder is:",
        ["2", "17", "47", "12"], str(v),
        r"$195 = 15 \times 13$. Remainder $= 47 \bmod 15 = 47 - 45 = 2$.",
        "Trap: 47 itself is bigger than 15, so it cannot be the remainder.", 30)

    v = (1021 * 1023 * 1025) % 17
    assert v == 15
    S.q("ns-rm-p2", "medium", r"What is the remainder when $1021 \times 1023 \times 1025$ is divided by 17?",
        ["15", "1", "9", "13"], str(v),
        r"$1020 = 17 \times 60$, so the remainders are 1, 3 and 5. Product $= 1 \times 3 \times 5 = 15$, which is less than 17. Remainder **15**.",
        "Spot 1020 = 17 × 60 and write each number as 1020 + small.", 45)
    v = sum(math.factorial(i) for i in range(1, 101)) % 12
    assert v == 9
    S.q("ns-rm-p2", "medium", r"What is the remainder when $1! + 2! + 3! + \dots + 100!$ is divided by 12?",
        ["9", "3", "0", "33"], str(v),
        r"From $4! = 24$ onwards every term is a multiple of 12. So only $1! + 2! + 3! = 1 + 2 + 6 = 9$ matters. Remainder **9**.",
        None, 40)

    v = pow(3, 101, 8)
    assert v == 3
    S.q("ns-rm-p3", "medium", r"What is the remainder when $3^{101}$ is divided by 8?",
        ["3", "1", "5", "7"], str(v),
        r"$3^2 = 9$ leaves 1 with 8. $3^{101} = (3^2)^{50} \times 3$ leaves $1 \times 3 = 3$.",
        None, 35)
    v = pow(5, 70, 13)
    assert v == 12
    S.q("ns-rm-p3", "hard", r"What is the remainder when $5^{70}$ is divided by 13?",
        ["12", "1", "5", "8"], str(v),
        r"""$5^2 = 25 = 26 - 1$, so $5^2$ leaves $-1$ with 13.
$5^{70} = (5^2)^{35}$ leaves $(-1)^{35} = -1$.
Remainder $= 13 - 1 = 12$.""",
        "Find a power giving −1; odd count of (−1) → divisor − 1.", 50)
    v = (pow(67, 67, 68) + 67) % 68
    assert v == 66
    S.q("ns-rm-p3", "hard", r"What is the remainder when $67^{67} + 67$ is divided by 68?",
        ["66", "1", "0", "67"], str(v),
        r"""$67 \equiv -1 \pmod{68}$. So $67^{67} \equiv (-1)^{67} = -1$.
$67^{67} + 67 \equiv -1 + 67 = 66$.""",
        "Base one less than divisor, odd power → −1.", 45)

    divisor = 5 * 48
    quotient = divisor // 12
    v = divisor * quotient + 48
    assert (divisor, quotient, v) == (240, 20, 4848)
    S.q("ns-rm-p4", "medium", "In a division sum, the divisor is 12 times the quotient and 5 times the remainder. If the remainder is 48, what is the dividend?",
        [ind(4848), ind(4800), ind(4688), ind(5808)], ind(v),
        r"""Divisor $= 5 \times 48 = 240$. Quotient $= 240 \div 12 = 20$.
Dividend $= 240 \times 20 + 48 = 4848$.""",
        "Trap 4,800: forgetting to add the remainder.", 50)
    n = 68 * 269
    v = n % 67
    assert v == 1
    S.q("ns-rm-p4", "easy", "A number when divided by 68 gives quotient 269 and remainder 0. What will be the remainder when the same number is divided by 67?",
        ["1", "0", "2", "3"], str(v),
        r"""Number $= 68 \times 269 = 18292$. $18292 = 67 \times 273 + 1$. Remainder **1**.""",
        r"$68 \times 269 = (67 + 1) \times 269$ → remainder $= 269 \bmod 67 = 1$.", 40)

    v = (3 ** 3 + 2 * 3) % 7
    assert all((N ** 3 + 2 * N) % 7 == v for N in range(3, 200, 7)) and v == 5
    S.q("ns-rm-p5", "medium", r"When a positive integer $N$ is divided by 7 the remainder is 3. What is the remainder when $N^3 + 2N$ is divided by 7?",
        ["5", "3", "6", "2"], str(v),
        r"Replace $N$ by 3: $3^3 + 2 \times 3 = 27 + 6 = 33$. $33 \bmod 7 = 5$.",
        "Take N = 3 itself and divide directly.", 40)
    v = (13 * 11) % 17
    assert all((a * b) % 17 == v for a in range(13, 300, 17) for b in range(11, 300, 17)) and v == 7
    S.q("ns-rm-p5", "medium", "Two numbers, when divided by 17, leave remainders 13 and 11 respectively. What is the remainder when their product is divided by 17?",
        ["7", "2", "24", "6"], str(v),
        r"Product of remainders $= 13 \times 11 = 143 = 17 \times 8 + 7$. Remainder **7**.",
        r"Negative remainders: $(-4)(-6) = 24 \to 7$.", 35)

    for n in range(1, 500):
        q1, r1 = divmod(n, 4)
        q2, r2 = divmod(q1, 5)
        if (r1, r2) == (1, 4):
            first = n
            break
    assert first == 17 and all(((20 * k + 17) // 4) % 5 == 4 for k in range(50))
    S.q("ns-rm-p6", "hard", "A number when divided successively by 4 and 5 leaves remainders 1 and 4 respectively. What is the remainder when the number is divided by 20?",
        ["17", "21", "1", "9"], "17",
        r"""Let the number be $N = 4q + 1$ and $q = 5k + 4$.
$N = 4(5k + 4) + 1 = 20k + 17$.
So $N$ leaves remainder **17** when divided by 20.""",
        r"Remainder with product $= d_1 r_2 + r_1 = 4 \times 4 + 1 = 17$.", 60)
    for n in range(1, 500):
        q1, r1 = divmod(n, 3)
        q2, r2 = divmod(q1, 5)
        q3, r3 = divmod(q2, 7)
        if (r1, r2, r3) == (2, 3, 4):
            first = n
            break
    assert first == 71
    S.q("ns-rm-p6", "medium", "What is the smallest number which, when divided successively by 3, 5 and 7, leaves remainders 2, 3 and 4 respectively?",
        ["71", "53", "107", "89"], str(first),
        r"""Work backwards. Last quotient = 0, so the number before division by 7 is 4.
Before division by 5: $5 \times 4 + 3 = 23$.
Before division by 3: $3 \times 23 + 2 = 71$.
Check: $71 = 3 \times 23 + 2$, $23 = 5 \times 4 + 3$, $4 = 7 \times 0 + 4$ ✓.""",
        None, 60)
    return S
