"""Phase-2 deep content for quant/algebra.json — identities + reciprocal modules."""
import os
import sys

sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
from fractions import Fraction as F

from _lib import Sub, fr


def build_identities():
    S = Sub("alg-identities")

    S.notes = r"""### The five working identities
$$(a+b)^2 = a^2 + 2ab + b^2 \quad (a-b)^2 = a^2 - 2ab + b^2 \quad a^2-b^2 = (a+b)(a-b)$$
$$a^3+b^3 = (a+b)(a^2-ab+b^2) \qquad a^3-b^3 = (a-b)(a^2+ab+b^2)$$
Everything else in this subtopic is these five rearranged. Read them BOTH ways: expanding, and factoring a big expression into something you can divide out.

### The symmetric machine: given $a \pm b$ and $ab$
Almost every question hands you $a+b$ (or $a-b$) and $ab$, then asks for a higher symmetric expression. Never solve for $a$ and $b$ — rebuild from the top:
$$a^2+b^2 = (a+b)^2 - 2ab \qquad a^3+b^3 = (a+b)^3 - 3ab(a+b) \qquad a^3-b^3 = (a-b)^3 + 3ab(a-b)$$
$$a^4+b^4 = (a^2+b^2)^2 - 2a^2b^2$$
With $a+b = 5$, $ab = 6$: $a^2+b^2 = 13$, then $a^4+b^4 = 169 - 2\cdot36 = 97$. Two identities chained — that is the whole game. For a minus-stem, $a^2+b^2$ works the same way from $(a-b)^2 + 2ab$.

### Big numbers: match the identity first
Large decimals and cubes are always an identity in disguise. Scan the denominator's middle term:
- $p^2 - pq + q^2$ under a numerator $p^3+q^3$ → the fraction collapses to $p+q$ (since $p^3+q^3 = (p+q)(p^2-pq+q^2)$).
- $p^2 + pq + q^2$ with numerator $p^3-q^3$ → collapses to $p-q$.
So $\frac{4.7^3 + 2.3^3}{4.7^2 - 4.7\times2.3 + 2.3^2} = 4.7 + 2.3 = 7$ in one line. For sums like $873^2 + 127^2 + 873\times127$, notice the structure $a^2+b^2+ab = (a+b)^2 - ab$ with $a+b = 1000$.

### Sum of squares = zero
A quadratic-type equation in several variables with real solutions is often a perfect-square sum:
$$x^2 + y^2 - 8x + 6y + 25 = (x-4)^2 + (y+3)^2 = 0$$
Squares are never negative, so each must be exactly zero → $x = 4$, $y = -3$. The same trick with three variables: complete every square and force each to zero; then any requested combination ($x-y$, $x+y+z$, …) is read off directly. A close cousin: $a^2+b^2+c^2 = ab+bc+ca \iff a=b=c$, because the difference is half of $(a-b)^2+(b-c)^2+(c-a)^2$.

### Direct evaluation
$(103\times97) = (100+3)(100-3) = 9991$ and $105^2 - 95^2 = 200\times10 = 2000$ — spot the $(a\pm b)$ forms around a round base. For products of two-digit numbers near 100, the base-100 split is faster than multiplication.

### Common traps
- Expanding $(a+b)^3$ and forgetting the $3ab(a+b)$ term — always cross-check with a small case.
- Using $a^3+b^3$ with the WRONG trinomial ($p^2+pq+q^2$ belongs to $p^3-q^3$, not $p^3+q^3$).
- Trying to find $a$ and $b$ individually from $a+b$ and $ab$ — wasted time, and the surds get ugly.
- Missing that "sum of squares = 0" pins every variable exactly.

### Quick revision
- $a^2+b^2 = (a\pm b)^2 \mp 2ab$; $a^3\pm b^3 = (a\pm b)^3 \mp 3ab(a\pm b)$; $a^4+b^4 = (a^2+b^2)^2 - 2a^2b^2$.
- Denominator $p^2 \mp pq + q^2$ → fraction $= p \pm q$.
- $a^2+b^2+c^2 = ab+bc+ca \Rightarrow a=b=c$.
- Squares summing to zero → each square is 0.
"""

    S.pattern("alg-p1", "Symmetric expressions from a±b and ab", "very common",
        "Two conditions like $a+b=7$, $ab=12$ are given and a higher symmetric expression ($a^3\\pm b^3$, $a^2+b^2$, $a^4+b^4$, $xy$) is asked.",
        r"a^3+b^3 = (a+b)^3 - 3ab(a+b), \quad a^3-b^3 = (a-b)^3 + 3ab(a-b)",
        r"""1. Never solve for the variables individually.
2. Build upward: $(a\pm b)$ and $ab$ → $a^2+b^2$ → $a^3\pm b^3$ → $a^4+b^4$.
3. Each rung reuses the previous one — chain two identities at most.

Why: the expressions asked are all symmetric polynomials in $a,b$, hence expressible through $a+b$ and $ab$ alone.""",
        "If $a+b=7$ and $ab=12$, then $a^3+b^3$ is:",
        r"$7^3 - 3\times12\times7 = 343 - 252 = 91$. No need to find $a$ and $b$ (they are 3 and 4).")
    S.pattern("alg-p2", "Big-number simplification by identity", "very common",
        "Fractions of cubes over trinomials, or large squared terms like $873^2+127^2+873\\times127$, dressed up as arithmetic.",
        r"\frac{p^3\pm q^3}{p^2 \mp pq + q^2} = p \pm q; \qquad a^2+b^2+ab = (a+b)^2 - ab",
        r"""1. Match the denominator to a trinomial factor of a cube identity.
2. The fraction collapses to the SUM (if the middle term is negative) or the DIFFERENCE (positive middle term).
3. For $a^2+b^2+ab$ shapes, rewrite around $a+b$ and subtract $ab$.

Why: the trinomial $p^2 \mp pq + q^2$ is exactly what survives when a cube is divided by $p \pm q$.""",
        "The value of $\\dfrac{198^3 + 12^3}{198^2 - 198\\times12 + 12^2}$ is:",
        r"Denominator $= p^2 - pq + q^2$ → fraction $= 198 + 12 = 210$. Never expand the cubes.")
    S.pattern("alg-p3", "Sum of squares equal to zero", "very common",
        "One equation in two or three variables like $x^2+y^2-8x+6y+25=0$, or $a^2+b^2+c^2=ab+bc+ca$; a linear combination is asked.",
        r"x^2+y^2-8x+6y+25 = (x-4)^2+(y+3)^2 = 0",
        r"""1. Group $x$-terms and $y$-terms and complete both squares; the constant should cancel exactly.
2. Each square is $\ge 0$, so the sum is zero only if every square is zero.
3. Read off each variable, then compute the asked combination.
4. The three-variable twin: $a^2+b^2+c^2-ab-bc-ca = \frac12[(a-b)^2+(b-c)^2+(c-a)^2] = 0 \Rightarrow a=b=c$.

Why: squares exhaust the constant, and non-negativity turns one equation into a full solution.""",
        "If $a^2+b^2+c^2 = ab+bc+ca$ and $a+b+c = 15$, then $ab+bc+ca$ is:",
        r"The condition forces $a=b=c=5$ → $ab+bc+ca = 3\times25 = 75$. Or: twice the target $= (a+b+c)^2 - (a^2+b^2+c^2) = 225 - 75 = 150$.")
    S.pattern("alg-p4", "Direct identity evaluation", "common",
        "Products or differences of round numbers: $103\\times97$, $105^2-95^2$, $(52)^2-(48)^2$ — expandable by a base-$100$ or $(a\\pm b)$ split.",
        r"(a+b)(a-b) = a^2-b^2",
        r"""1. Write each number as round base $\pm$ small offset (103 = 100+3, 97 = 100−3).
2. Apply $(a+b)(a-b)$ or $(a\pm b)^2$ directly.
3. Compute in the base (100² = 10000) — no long multiplication.

Why: numbers near a round base make the $(a\pm b)$ expansion trivial mental arithmetic.""",
        "The value of $105^2 - 95^2$ is:",
        r"$(105+95)(105-95) = 200\times10 = 2000$.")

    # ---- practice (alg-identities) ----
    assert (105 + 95) * (105 - 95) == 2000
    S.q("alg-p4", "easy",
        "The value of $105^2 - 95^2$ is:",
        ["2000", "100", "400", "20"], "2000",
        r"$105^2-95^2 = (105+95)(105-95) = 200\times10 = 2000$.",
        None, 25)
    assert 103 * 97 == 10000 - 9
    S.q("alg-p4", "easy",
        "The value of $103 \\times 97$ is:",
        ["9991", "9981", "9999", "9891"], "9991",
        r"$(100+3)(100-3) = 100^2 - 3^2 = 10000 - 9 = 9991$.",
        None, 25)
    v = 7 ** 3 - 3 * 12 * 7
    assert v == 91
    S.q("alg-p1", "medium",
        "If $a+b=7$ and $ab=12$, then $a^3+b^3$ is equal to:",
        ["91", "97", "85", "279"], "91",
        r"$a^3+b^3 = (a+b)^3 - 3ab(a+b) = 343 - 3\times12\times7 = 343 - 252 = 91$.",
        None, 35)
    v = 5 ** 3 + 3 * 6 * 5
    assert v == 215
    S.q("alg-p1", "medium",
        "If $a-b=5$ and $ab=6$, then $a^3-b^3$ is equal to:",
        ["215", "125", "185", "235"], "215",
        r"$a^3-b^3 = (a-b)^3 + 3ab(a-b) = 125 + 3\times6\times5 = 215$.",
        None, 35)
    xy = (100 - 58) / F(2)
    assert xy == 21
    S.q("alg-p1", "medium",
        "If $x+y=10$ and $x^2+y^2=58$, then $xy$ is equal to:",
        ["21", "42", "20", "24"], "21",
        r"$x^2+y^2 = (x+y)^2-2xy$ → $58 = 100 - 2xy$ → $xy = 21$.",
        None, 35)
    v = 13 ** 2 - 2 * 36
    assert v == 97
    S.q("alg-p1", "hard",
        "If $x+y=5$ and $x^2+y^2=13$, then $x^4+y^4$ is equal to:",
        ["97", "119", "169", "73"], "97",
        r"$xy = \frac{25-13}{2} = 6$. Then $x^4+y^4 = (x^2+y^2)^2 - 2x^2y^2 = 169 - 72 = 97$.",
        None, 50)
    assert (198 + 12) == 210
    S.q("alg-p2", "medium",
        "The value of $\\dfrac{198^3 + 12^3}{198^2 - 198\\times12 + 12^2}$ is:",
        ["210", "186", "246", "21"], "210",
        r"$p^3+q^3 = (p+q)(p^2-pq+q^2)$ → the fraction $= 198+12 = 210$.",
        None, 35)
    v = 873 ** 2 + 127 ** 2 + 873 * 127
    assert v == 889129 and 1000 ** 2 - 873 * 127 == 889129
    S.q("alg-p2", "medium",
        "The value of $873\\times873 + 127\\times127 + 873\\times127$ is:",
        ["889129", "889139", "889119", "881129"], "889129",
        r"$a^2+b^2+ab = (a+b)^2 - ab = 1000000 - 110871 = 889129$.",
        None, 45)
    assert (4 - (-3)) == 7
    S.q("alg-p3", "medium",
        "If $x^2+y^2-8x+6y+25=0$, then the value of $x-y$ is:",
        ["7", "1", "-7", "12"], "7",
        r"$(x-4)^2+(y+3)^2 = 0$ → $x = 4$, $y = -3$ → $x-y = 7$.",
        None, 45)
    assert 3 * 25 == 75 and 15 * 15 - 3 * 50 == 75
    S.q("alg-p3", "hard",
        "If $a^2+b^2+c^2 = ab+bc+ca$ and $a+b+c=15$, then the value of $ab+bc+ca$ is:",
        ["75", "50", "25", "100"], "75",
        r"The condition forces $a=b=c=5$ → $ab+bc+ca = 75$.",
        "Check: $(a+b+c)^2 = a^2+b^2+c^2+2(ab+bc+ca) = 3P+2P = 225$ → $P = 75$.", 50)
    return S


def build_reciprocal():
    S = Sub("alg-reciprocal")

    S.notes = r"""### The ladder
If $x+\dfrac1x = k$, then every $x^n+\dfrac1{x^n}$ climbs from $k$ without ever finding $x$:
$$x^2+\frac1{x^2} = k^2-2 \qquad x^3+\frac1{x^3} = k^3-3k \qquad x^4+\frac1{x^4} = (x^2+\tfrac1{x^2})^2-2$$
and the multiply-down shortcut for the fifth rung:
$$x^5+\frac1{x^5} = \left(x^2+\frac1{x^2}\right)\left(x^3+\frac1{x^3}\right) - \left(x+\frac1x\right)$$
With $k=3$: $x^2+\frac1{x^2} = 7$, $x^3+\frac1{x^3} = 18$, $x^5+\frac1{x^5} = 7\times18-3 = 123$. Squaring again gives the fourth rung: $7^2-2 = 47$.

### The difference ladder
For $x-\dfrac1x = m$ the minus version works the same way, with **+2** in the square:
$$x^2+\frac1{x^2} = m^2+2 \qquad x^3-\frac1{x^3} = m^3+3m \qquad x^4+\frac1{x^4} = (m^2+2)^2-2$$
And the two ladders connect: $\left(x+\frac1x\right)^2 = \left(x-\frac1x\right)^2+4$. Given either one, the other is one square away — $x+\frac1x = \sqrt{m^2+4}$.

### Quadratics with equal end coefficients
$4x^2 - 9x + 4 = 0$ — first and last coefficient equal — divides cleanly by $x$:
$$4x - 9 + \frac4x = 0 \;\Rightarrow\; x+\frac1x = \frac94$$
So the quadratic IS the $k$-value in disguise. After that, run the ladder. Any $ax^2+bx+a=0$ gives $x+\frac1x = \frac ba$.

### Special values — the cyclic escape
Some $k$ values collapse the ladder entirely because $x$ satisfies a cyclotomic quadratic:
- $x+\frac1x = 1$ → $x^2-x+1 = 0$ → $x^3 = -1$ → $x^6 = x^9 = \dots = 1$.
- $x+\frac1x = -1$ → $x^2+x+1 = 0$ → $x^3 = 1$.
- $x+\frac1x = \sqrt3$ → $x^2+\frac1{x^2} = -1$ → $x^4 = -1$-type cycling ($x^6+\frac1{x^6} = -2$, $x^{18}$-type sums vanish to small integers).
For stems like $x^{18}+x^{12}+x^6+1$, reduce every exponent mod 3 (or mod 6) before doing anything.

### Which rung to compute
Plan the route BEFORE multiplying anything. For $k=5$ asking $x^4+\frac1{x^4}$: two squarings — $23$, then $23^2-2 = 527$ — never touch a cube. For fifth rungs, multiply rung 2 by rung 3 and subtract $k$; do not compute the sixth rung by cubing rung two. When a stem mixes sum and difference ladders (given $x-\frac1x$, asked about $x^3+\frac1{x^3}$), convert once with $k^2 = m^2+4$, then stay on the ladder that matches the asked sign.

### Common traps
- Using $k^2-2$ for the difference ladder (it is $m^2+2$).
- Writing $x^3+\frac1{x^3} = k^3-3$ instead of $k^3-3k$.
- Dividing a quadratic by $x$ when the end coefficients differ — that trick needs $ax^2+bx+a$.
- For a cyclic stem, expanding powers instead of reducing exponents first.

### Quick revision
- $k = x+\frac1x$: $x^2+\frac1{x^2} = k^2-2$, $x^3+\frac1{x^3} = k^3-3k$, $x^5+\frac1{x^5} = (k^2-2)(k^3-3k)-k$.
- $m = x-\frac1x$: $x^2+\frac1{x^2} = m^2+2$, $x^3-\frac1{x^3} = m^3+3m$; $k^2 = m^2+4$.
- $ax^2+bx+a=0$ → $x+\frac1x = \frac ba$.
- $k = 1$ → $x^3 = -1$; $k = -1$ → $x^3 = 1$; $k = \sqrt3$ → $x^2+\frac1{x^2} = -1$.
"""

    S.pattern("alg-p5", "Ladder from $x+\\frac1x=k$", "very common",
        "$x+\\frac1x = k$ given; $x^2+\\frac1{x^2}$, $x^3+\\frac1{x^3}$, $x^4+\\frac1{x^4}$ or $x^5+\\frac1{x^5}$ asked.",
        r"x^2+\frac1{x^2} = k^2-2; \quad x^3+\frac1{x^3} = k^3-3k; \quad x^4+\frac1{x^4} = (k^2-2)^2-2",
        r"""1. Square once: $x^2+\frac1{x^2} = k^2-2$ (the $2x\cdot\frac1x = 2$ cancels).
2. Cube for the third rung: $k^3-3k$.
3. Fourth rung: square the second. Fifth rung: multiply the second and third and subtract $k$.

Why: the product $x\cdot\frac1x = 1$ makes every rung a polynomial in $k$ alone.""",
        "If $x+\\frac1x=6$, then $x^3+\\frac1{x^3}$ is:",
        r"$6^3 - 3\times6 = 216 - 18 = 198$. One line, no solving for $x$.")
    S.pattern("alg-p6", "Difference ladder from $x-\\frac1x=m$", "very common",
        "$x-\\frac1x = m$ given; the squared rung or $x^3-\\frac1{x^3}$ is asked.",
        r"x^2+\frac1{x^2} = m^2+2; \quad x^3-\frac1{x^3} = m^3+3m; \quad k^2 = m^2+4",
        r"""1. Square: the cross term is $-2$ but it SUBTRACTS, so $x^2+\frac1{x^2} = m^2+2$.
2. Cube: $x^3-\frac1{x^3} = m^3+3m$ (the correction adds).
3. To switch ladders: $(x+\frac1x)^2 = (x-\frac1x)^2+4$.

Why: same expansions as the sum ladder with the sign of the cross term flipped.""",
        "If $x-\\frac1x=4$, then $x^3-\\frac1{x^3}$ is:",
        r"$4^3 + 3\times4 = 64+12 = 76$. (And $x^2+\frac1{x^2} = 18$. $x+\frac1x = \sqrt{20} = 2\sqrt5$.)")
    S.pattern("alg-p7", "Quadratic with equal end coefficients", "very common",
        "An equation like $4x^2-9x+4=0$ (equal first and last coefficients) is given; a rung of the ladder is asked.",
        r"ax^2+bx+a=0 \;\Rightarrow\; x+\frac1x = \frac ba",
        r"""1. Divide the whole equation by $x$ (legal: $x=0$ is not a root since $a\ne0$).
2. Read off $x+\frac1x = \frac ba$.
3. Climb the ladder as usual.

Why: dividing by $x$ merges the two end terms into $a(x+\frac1x)$.""",
        "If $4x^2-9x+4=0$, then $x^2+\\frac1{x^2}$ equals:",
        r"$x+\frac1x = \frac94$ → $x^2+\frac1{x^2} = \frac{81}{16}-2 = \frac{49}{16}$. No quadratic formula needed.")
    S.pattern("alg-p8", "Special / cyclic values", "common",
        "$k$ is $1$, $-1$, $\\sqrt3$ (or the asked expression has huge exponents like $x^{18}$); a small value is expected.",
        r"k=1 \Rightarrow x^3=-1; \quad k=-1 \Rightarrow x^3=1; \quad \text{reduce exponents mod } 3",
        r"""1. From $x+\frac1x = \pm1$, multiply through by $x$: $x^2\pm x+1 = 0$.
2. Multiply by $(x\mp1)$: $(x\mp1)(x^2\pm x+1) = x^3\mp1 = 0$ → $x^3 = \pm1$.
3. Reduce every exponent modulo 3 (or 6) and substitute.
4. For $k=\sqrt3$: $x^2+\frac1{x^2} = -1$, and higher even rungs alternate small values.

Why: these $x$ are cube roots of unity family — powers cycle with period 3.""",
        "If $x+\\frac1x=-1$, then $x^6+x^3+1$ equals:",
        r"$x^2+x+1=0$ → $x^3 = 1$ → $x^6+x^3+1 = 1+1+1 = 3$.")

    # ---- practice (alg-reciprocal) ----
    assert 4 ** 2 - 2 == 14
    S.q("alg-p5", "easy",
        "If $x+\\frac1x=4$, then the value of $x^2+\\frac1{x^2}$ is:",
        ["14", "18", "16", "12"], "14",
        r"$x^2+\frac1{x^2} = 4^2-2 = 14$.",
        None, 25)
    assert 2 ** 3 - 3 * 2 == 2
    S.q("alg-p5", "easy",
        "If $x+\\frac1x=2$, then the value of $x^3+\\frac1{x^3}$ is:",
        ["2", "8", "6", "11"], "2",
        r"$x^3+\frac1{x^3} = 2^3-3\times2 = 8-6 = 2$. (In fact $x=1$.)",
        None, 25)
    assert 3 ** 2 + 2 == 11
    S.q("alg-p6", "easy",
        "If $x-\\frac1x=3$, then the value of $x^2+\\frac1{x^2}$ is:",
        ["11", "9", "7", "13"], "11",
        r"$x^2+\frac1{x^2} = 3^2+2 = 11$.",
        None, 25)
    assert F(9, 4) ** 2 - 2 == F(49, 16)
    S.q("alg-p7", "easy",
        "If $3x^2-7x+3=0$, then the value of $x+\\frac1x$ is:",
        [fr(F(7, 3)), fr(F(3, 7)), fr(F(7, 9)), "3"], fr(F(7, 3)),
        r"Dividing by $3x$: $3x-7+\frac3x = 0$ → $x+\frac1x = \frac73$.",
        None, 30)
    x2 = F(3) - 2
    x4 = x2 * x2 - 2
    assert x2 == 1 and x4 == -1
    S.q("alg-p5", "medium",
        "If $x+\\frac1x=\\sqrt3$, then the value of $x^4+\\frac1{x^4}$ is:",
        ["-1", "1", "2", "-2"], "-1",
        r"$x^2+\frac1{x^2} = 3-2 = 1$ → $x^4+\frac1{x^4} = 1^2-2 = -1$.",
        None, 40)
    v = 34 * 198 - 6
    assert v == 6726
    S.q("alg-p5", "medium",
        "If $x+\\frac1x=6$, then the value of $x^5+\\frac1{x^5}$ is:",
        ["6726", "6720", "6732", "6606"], "6726",
        r"$x^2+\frac1{x^2} = 34$, $x^3+\frac1{x^3} = 198$ → $x^5+\frac1{x^5} = 34\times198-6 = 6726$.",
        None, 45)
    xr = complex(-0.5, 3 ** 0.5 / 2)
    assert abs(xr + 1 / xr + 1) < 1e-9 and abs(xr ** 6 + xr ** 3 + 1 - 3) < 1e-9
    S.q("alg-p8", "medium",
        "If $x+\\frac1x=-1$, then the value of $x^6+x^3+1$ is:",
        ["3", "1", "0", "2"], "3",
        r"$x^2+x+1=0$ → multiplying by $(x-1)$: $x^3-1=0$ → $x^3=1$ → the expression $= 1+1+1 = 3$.",
        None, 45)
    v = 4 ** 3 + 3 * 4
    assert v == 76
    S.q("alg-p6", "medium",
        "If $x-\\frac1x=4$, then the value of $x^3-\\frac1{x^3}$ is:",
        ["76", "52", "64", "88"], "76",
        r"$x^3-\frac1{x^3} = 4^3+3\times4 = 76$.",
        None, 40)
    assert F(9, 4) ** 2 - 2 == F(49, 16)
    S.q("alg-p7", "medium",
        "If $4x^2-9x+4=0$, then the value of $x^2+\\frac1{x^2}$ is:",
        [fr(F(49, 16)), fr(F(81, 16)), fr(F(17, 4)), fr(F(97, 16))], fr(F(49, 16)),
        r"$x+\frac1x = \frac94$ → $x^2+\frac1{x^2} = \frac{81}{16}-2 = \frac{49}{16}$.",
        None, 40)
    assert 1 ** 3 - 3 * 1 == -2
    S.q("alg-p8", "medium",
        "If $x+\\frac1x=1$, then the value of $x^3+\\frac1{x^3}$ is:",
        ["-2", "2", "1", "-1"], "-2",
        r"$x^3+\frac1{x^3} = 1^3-3\times1 = -2$. (Here $x^2-x+1=0$ → $x^3=-1$ — both routes agree.)",
        None, 35)
    return S
