import math
from itertools import combinations
from _lib import Sub


def divisors(n):
    return [d for d in range(1, n + 1) if n % d == 0]


def legendre(n, p):
    c, k = 0, p
    while k <= n:
        c += n // k
        k *= p
    return c


def trailing_zeros(n):
    z = 0
    while n % 10 == 0:
        n //= 10
        z += 1
    return z


def build():
    S = Sub("ns-factors")
    S.notes = r"""### Factors and multiples
A **factor** (divisor) of a number divides it exactly. Factors of 12 are 1, 2, 3, 4, 6, 12. A **multiple** is the opposite: 12, 24, 36 … are multiples of 12. Every question on "how many factors" starts with **prime factorisation** — writing the number as a product of primes.

### Prime factorisation
Keep dividing by the smallest prime that works. $720 = 2 \times 360 = 2 \times 2 \times 180 = \dots = 2^4 \times 3^2 \times 5$. Write it in power form: $N = p^a \times q^b \times r^c$.

### Number of factors
A factor of $2^4 \times 3^2 \times 5$ can take the power of 2 as 0, 1, 2, 3 or 4 (5 choices), the power of 3 as 0, 1 or 2 (3 choices), and the power of 5 as 0 or 1 (2 choices).
$$\text{Number of factors} = (a+1)(b+1)(c+1)$$
For 720: $5 \times 3 \times 2 = 30$ factors.

### Odd, even and special factors
- **Odd factors**: ignore the 2 completely. $3600 = 2^4 \times 3^2 \times 5^2$ → odd factors $= 3 \times 3 = 9$.
- **Even factors** = total − odd. For 3600: $45 - 9 = 36$.
- **Factors that are multiples of $k$**: divide $N$ by $k$ and count the factors of $N/k$. For 1440 and $k = 12$: $1440/12 = 120 = 2^3 \times 3 \times 5$ → $4 \times 2 \times 2 = 16$.
- **Perfect-square factors**: each power can only be even (0, 2, 4 …). **Perfect-cube factors**: powers 0, 3, 6 …

### Sum of factors
$$\text{Sum} = (1 + p + \dots + p^a)(1 + q + \dots + q^b)\dots$$
For $360 = 2^3 \times 3^2 \times 5$: $(1+2+4+8)(1+3+9)(1+5) = 15 \times 13 \times 6 = 1170$.
Sum of **even** factors: drop the 1 from the bracket of 2: $(2+4+8) \times \dots$

### Product of factors
If $N$ has $d$ factors, the product of all its factors is $N^{d/2}$. Factors pair up as $(1, N), (2, N/2), \dots$ — each pair multiplies to $N$.

### Writing N as a product of two factors
- Number of ways $= d/2$ (if $N$ is not a perfect square), or $(d+1)/2$ if it is (the square root pairs with itself).
- As a product of two **co-prime** factors: $2^{k-1}$, where $k$ = number of different primes in $N$.

### Trailing zeros
A zero at the end comes from a factor 10 = 2 × 5. In $n!$ there are always more 2s than 5s, so **count the 5s**:
$$\text{zeros in } n! = \left\lfloor \frac{n}{5} \right\rfloor + \left\lfloor \frac{n}{25} \right\rfloor + \left\lfloor \frac{n}{125} \right\rfloor + \dots$$
125! → 25 + 5 + 1 = 31 zeros. Quick way: keep dividing by 5 and add the quotients.
Careful with products like $5 \times 10 \times 15 \times \dots \times 100$: here 5s are plenty and 2s are fewer, so count both and take the smaller.

### Highest power of a prime in n!
Same successive division, but by the prime $p$: power of 3 in 100! $= 33 + 11 + 3 + 1 = 48$.
For a composite like 12 = $2^2 \times 3$: find the power of 2 (divide by 2 because of the square) and the power of 3; the answer is the smaller.

### Quick revision
- Factors: $(a+1)(b+1)(c+1)$; odd factors → drop 2.
- Multiples of $k$ among factors → factors of $N/k$.
- Sum: product of $(1 + p + \dots + p^a)$ brackets.
- Product of factors $= N^{d/2}$.
- Zeros in $n!$ = successive division by 5.
- Highest power of $p$ in $n!$ = successive division by $p$.
"""

    S.pattern("ns-fc-p1", "Number of factors (total, odd, even)", "very common",
        "'How many factors / divisors does 720 have?', 'how many odd (or even) factors …'.",
        r"N = p^a q^b r^c \Rightarrow d(N) = (a+1)(b+1)(c+1)",
        r"""1. Prime-factorise $N$.
2. Total: multiply (each power + 1).
3. Odd: leave out the power of 2. Even: total − odd.

Why: each factor is built by choosing a power for every prime independently.""",
        "How many factors does 252 have?",
        r"$252 = 2^2 \times 3^2 \times 7$ → $3 \times 3 \times 2 = 18$ factors.")
    S.pattern("ns-fc-p2", "Special factors: perfect squares/cubes, multiples of k", "common",
        "'How many factors of N are perfect cubes?', 'how many factors of 1440 are divisible by 12?'.",
        r"\#\{\text{factors divisible by } k\} = d(N/k)",
        r"""1. Perfect squares: count only even powers for each prime (0, 2, 4, …). Cubes: 0, 3, 6, …
2. Multiples of $k$: divide $N$ by $k$ and count the factors of the quotient.

Why: a factor divisible by $k$ is $k$ times a factor of $N/k$.""",
        r"How many factors of $2^5 \times 3^3$ are perfect squares?",
        r"Powers of 2: 0, 2, 4 (3 choices). Powers of 3: 0, 2 (2 choices). Answer $3 \times 2 = 6$.")
    S.pattern("ns-fc-p3", "Sum of factors (all, odd or even)", "common",
        "'Find the sum of all factors of 360', 'sum of even factors of 72'.",
        r"\sigma(N) = \prod \frac{p^{a+1}-1}{p-1} = (1+p+\dots+p^a)(1+q+\dots+q^b)",
        r"""1. Prime-factorise.
2. Write a bracket $(1 + p + p^2 + \dots)$ for each prime and multiply.
3. Even factors: bracket for 2 starts from 2. Odd factors: drop the bracket of 2.

Why: expanding the product gives every factor exactly once.""",
        "Find the sum of all factors of 60.",
        r"$60 = 2^2 \times 3 \times 5$ → $(1+2+4)(1+3)(1+5) = 7 \times 4 \times 6 = 168$.")
    S.pattern("ns-fc-p4", "Trailing zeros in a factorial or product", "very common",
        r"'How many zeros are there at the end of 125!?' or at the end of a product like $5 \times 10 \times \dots \times 100$.",
        r"Z(n!) = \left\lfloor \tfrac{n}{5} \right\rfloor + \left\lfloor \tfrac{n}{25} \right\rfloor + \left\lfloor \tfrac{n}{125} \right\rfloor + \dots",
        r"""1. For $n!$: divide $n$ by 5, divide the quotient by 5 again, … and add all quotients.
2. For other products: count 2s and 5s separately; zeros = the smaller count.

Why: each zero needs one 2 and one 5.""",
        "How many zeros are at the end of 80!?",
        r"$80 \div 5 = 16$, $16 \div 5 = 3$. Zeros $= 16 + 3 = 19$.")
    S.pattern("ns-fc-p5", "Highest power of a prime (or composite) dividing n!", "common",
        "'Find the largest n such that $3^n$ divides 100!', or 'highest power of 12 in 50!'.",
        r"E_p(n!) = \sum_{k \ge 1} \left\lfloor \frac{n}{p^k} \right\rfloor",
        r"""1. For a prime $p$: successive division of $n$ by $p$, add quotients.
2. For a composite, split into prime powers ($12 = 2^2 \times 3$), find each exponent, divide by the power needed, take the smallest.

Why: $\lfloor n/p \rfloor$ counts multiples of $p$, $\lfloor n/p^2 \rfloor$ adds the extra $p$ from multiples of $p^2$, and so on.""",
        "Highest power of 7 in 100!?",
        r"$100 \div 7 = 14$, $14 \div 7 = 2$. Answer $14 + 2 = 16$.")
    S.pattern("ns-fc-p6", "Product of factors; ways to write N as a product of two factors", "occasional",
        "'Find the product of all factors of 36', 'in how many ways can 360 be written as a product of two (co-prime) factors?'.",
        r"\prod d = N^{d(N)/2},\quad \text{pairs} = \frac{d(N)}{2},\quad \text{co-prime pairs} = 2^{k-1}",
        r"""1. Count factors $d(N)$.
2. Product of factors $= N^{d/2}$.
3. Ways as a product of two factors $= d/2$ ($(d+1)/2$ for a perfect square).
4. Co-prime pairs: each distinct prime goes wholly to one side → $2^k$ ordered splits, $2^{k-1}$ unordered.

Why: factors pair up as $(f, N/f)$.""",
        "Find the product of all factors of 12.",
        r"$12$ has 6 factors → product $= 12^{6/2} = 12^3 = 1728$. Check: $1 \times 2 \times 3 \times 4 \times 6 \times 12 = 1728$ ✓.")

    v = len(divisors(720))
    assert v == 30
    S.q("ns-fc-p1", "easy", "How many factors does 720 have?",
        ["30", "24", "36", "28"], str(v),
        r"$720 = 2^4 \times 3^2 \times 5$. Number of factors $= (4+1)(2+1)(1+1) = 30$.",
        None, 30)
    v = len([d for d in divisors(3600) if d % 2])
    assert v == 9
    S.q("ns-fc-p1", "medium", "How many odd factors does 3600 have?",
        ["9", "45", "36", "12"], str(v),
        r"$3600 = 2^4 \times 3^2 \times 5^2$. Odd factors ignore the 2: $(2+1)(2+1) = 9$.",
        "Trap 45 = all factors; 36 = even factors.", 35)

    n = 2 ** 6 * 3 ** 4 * 5 ** 3
    v = len([d for d in divisors(n) if round(d ** (1 / 3)) ** 3 == d])
    assert v == 12
    S.q("ns-fc-p2", "medium", r"How many factors of $2^6 \times 3^4 \times 5^3$ are perfect cubes?",
        ["12", "24", "18", "8"], str(v),
        r"""A perfect cube needs every power to be a multiple of 3.
- Power of 2: 0, 3, 6 → 3 choices.
- Power of 3: 0, 3 → 2 choices.
- Power of 5: 0, 3 → 2 choices.
Total $= 3 \times 2 \times 2 = 12$.""",
        None, 45)
    v = len([d for d in divisors(1440) if d % 12 == 0])
    assert v == 16
    S.q("ns-fc-p2", "medium", "How many factors of 1440 are divisible by 12?",
        ["16", "36", "12", "24"], str(v),
        r"$1440 \div 12 = 120 = 2^3 \times 3 \times 5$. Factors of 120 $= 4 \times 2 \times 2 = 16$. Each gives one factor of 1440 divisible by 12.",
        None, 45)

    v = sum(divisors(360))
    assert v == 1170
    S.q("ns-fc-p3", "medium", "What is the sum of all the factors of 360?",
        ["1170", "1080", "1200", "1152"], str(v),
        r"$360 = 2^3 \times 3^2 \times 5$. Sum $= (1+2+4+8)(1+3+9)(1+5) = 15 \times 13 \times 6 = 1170$.",
        None, 50)
    v = sum(d for d in divisors(72) if d % 2 == 0)
    assert v == 182
    S.q("ns-fc-p3", "hard", "What is the sum of all the even factors of 72?",
        ["182", "195", "13", "169"], str(v),
        r"""$72 = 2^3 \times 3^2$. An even factor must contain at least one 2.
Sum $= (2 + 4 + 8)(1 + 3 + 9) = 14 \times 13 = 182$.""",
        "All factors sum to 15 × 13 = 195; odd factors sum to 13; even = 195 − 13 = 182.", 50)

    v = trailing_zeros(math.factorial(125))
    assert v == 31
    S.q("ns-fc-p4", "easy", "How many zeros are there at the end of 125!?",
        ["31", "30", "25", "32"], str(v),
        r"$125 \div 5 = 25$, $25 \div 5 = 5$, $5 \div 5 = 1$. Zeros $= 25 + 5 + 1 = 31$.",
        None, 30)
    prod = 1
    for k in range(5, 101, 5):
        prod *= k
    v = trailing_zeros(prod)
    assert v == 18
    S.q("ns-fc-p4", "hard", r"How many zeros are there at the end of the product $5 \times 10 \times 15 \times 20 \times \dots \times 100$?",
        ["18", "24", "20", "22"], str(v),
        r"""The product $= 5^{20} \times (1 \times 2 \times \dots \times 20) = 5^{20} \times 20!$.
Number of 5s $= 20 + (20/5 + 20/25) = 20 + 4 = 24$.
Number of 2s (all come from 20!) $= 10 + 5 + 2 + 1 = 18$.
Zeros $=$ smaller count $= 18$.""",
        "Here 2s, not 5s, are the scarce factor.", 75)

    v = legendre(100, 3)
    assert v == 48
    S.q("ns-fc-p5", "medium", r"What is the largest value of $n$ such that $3^n$ divides $100!$?",
        ["48", "33", "44", "47"], str(v),
        r"$100 \div 3 = 33$, $33 \div 3 = 11$, $11 \div 3 = 3$, $3 \div 3 = 1$. Sum $= 33 + 11 + 3 + 1 = 48$.",
        None, 40)
    v = min(legendre(50, 2) // 2, legendre(50, 3))
    assert v == 22 and math.factorial(50) % 12 ** 22 == 0 and math.factorial(50) % 12 ** 23 != 0
    S.q("ns-fc-p5", "hard", r"What is the highest power of 12 that divides $50!$?",
        ["22", "23", "47", "16"], str(v),
        r"""$12 = 2^2 \times 3$.
Power of 2 in 50!: $25 + 12 + 6 + 3 + 1 = 47$ → number of $2^2$ blocks $= \lfloor 47/2 \rfloor = 23$.
Power of 3 in 50!: $16 + 5 + 1 = 22$.
Highest power of 12 $= \min(23, 22) = 22$.""",
        None, 70)

    prod = 1
    for d in divisors(36):
        prod *= d
    assert prod == 6 ** 9
    S.q("ns-fc-p6", "medium", "What is the product of all the factors of 36?",
        [r"$6^9$", r"$36^9$", r"$6^{18}$", r"$6^{10}$"], r"$6^9$",
        r"$36 = 2^2 \times 3^2$ has $3 \times 3 = 9$ factors. Product $= 36^{9/2} = (6^2)^{9/2} = 6^9$.",
        None, 45)
    k = 3  # distinct primes of 360
    pairs = {tuple(sorted((a, 360 // a))) for a in divisors(360) if math.gcd(a, 360 // a) == 1}
    assert len(pairs) == 2 ** (k - 1) == 4
    S.q("ns-fc-p6", "hard", "In how many ways can 360 be written as a product of two co-prime factors?",
        ["4", "8", "3", "12"], str(len(pairs)),
        r"""$360 = 2^3 \times 3^2 \times 5$ has 3 different primes. Each prime power must go completely to one factor.
Ordered splits $= 2^3 = 8$; unordered pairs $= 8/2 = 4$: $(1, 360), (8, 45), (9, 40), (5, 72)$.""",
        None, 60)
    pairs_all = {tuple(sorted((a, 360 // a))) for a in divisors(360)}
    assert len(pairs_all) == 12
    S.q("ns-fc-p6", "medium", "In how many ways can 360 be written as a product of two natural numbers (order not counted)?",
        ["12", "24", "13", "11"], str(len(pairs_all)),
        r"$360 = 2^3 \times 3^2 \times 5$ has $4 \times 3 \times 2 = 24$ factors. 360 is not a perfect square, so the factors pair up into $24 \div 2 = 12$ products.",
        None, 45)
    return S
