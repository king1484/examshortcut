"""Phase-2 deep content for quant/algebra.json — three-var + surds modules."""
import math
import os
import sys

sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
from fractions import Fraction as F

from _lib import Sub


def build_three():
    S = Sub("alg-three-var")

    S.notes = r"""### The identity and its two forms
$$a^3+b^3+c^3-3abc = (a+b+c)(a^2+b^2+c^2-ab-bc-ca)$$
The trinomial in brackets rewrites using the sum alone:
$$a^3+b^3+c^3-3abc = (a+b+c)\left[(a+b+c)^2 - 3(ab+bc+ca)\right]$$
Everything the exam asks routes through these two forms. With $a+b+c = 6$ and $ab+bc+ca = 11$: the value is $6\times(36-33) = 18$.

### The zero-sum shortcut
If $a+b+c = 0$, the left factor vanishes and the identity collapses to
$$a^3+b^3+c^3 = 3abc$$
This one shortcut answers a whole family: "if $a+b+c=0$, $abc=8$, find $a^3+b^3+c^3$" → 24. It also explains why $(x-y)^3+(y-z)^3+(z-x)^3 = 3(x-y)(y-z)(z-x)$ — the three terms sum to zero, so the cube-sum is 3×(product). Terms like $(b+c-3a)$ are engineered the same way: check whether the three brackets add to zero FIRST, before any expansion.

### The equal case
$$a^2+b^2+c^2-ab-bc-ca = \tfrac12\left[(a-b)^2+(b-c)^2+(c-a)^2\right] \ge 0$$
So the bracket above is zero exactly when $a = b = c$. Hence $a^2+b^2+c^2 = ab+bc+ca \iff a=b=c$. If additionally $a+b+c$ is known, every symmetric expression follows: with sum 9 and that condition, $a=b=c=3$ and $a^2+b^2+c^2 = 27$.

### Power sums
The full expansion of the cube of the sum:
$$a^3+b^3+c^3 = (a+b+c)^3 - 3(a+b+c)(ab+bc+ca) + 3abc$$
Given any three of the four quantities ($a+b+c$, $ab+bc+ca$, $abc$, $a^3+b^3+c^3$), the fourth drops out in one line. E.g. sum 9, pairwise 11, abc 6 → $729 - 297 + 18 = 450$. A useful companion: $(a+b)(b+c)(c+a) = (a+b+c)(ab+bc+ca) - abc$, and $(a+b+c)^3 = a^3+b^3+c^3 + 3(a+b)(b+c)(c+a)$. The pair form is also how $(x+y+z)^3 - x^3-y^3-z^3 = 3(x+y)(y+z)(z+x)$ is proved — subtract the individual cubes from the expansion.

### How to attack any question
1. Is a bracket-sum zero (like $x-y$, $y-z$, $z-x$)? → cubes sum to 3×product.
2. Is $a+b+c$ given with $ab+bc+ca$? → factor/half form for $a^3+b^3+c^3-3abc$.
3. Is $abc$ involved? → power-sum expansion.
4. Does $a^2+b^2+c^2$ equal $ab+bc+ca$? → all variables equal.

### Common traps
- Forgetting the $+3abc$ term in the power-sum expansion (the commonest algebra slip in CGL).
- Expanding $(x-y)^3+(y-z)^3+(z-x)^3$ brute-force — it is 3×product, instantly.
- Missing the half in $\frac12[(a-b)^2+\dots]$ when proving the equal case.
- Sign errors when a variable is negative (e.g. $c=-6$ with $a=11$, $b=-5$).

### Quick revision
- $a^3+b^3+c^3-3abc = (a+b+c)\left[(a+b+c)^2-3(ab+bc+ca)\right]$.
- $a+b+c=0 \Rightarrow a^3+b^3+c^3 = 3abc$.
- $(x-y)^3+(y-z)^3+(z-x)^3 = 3(x-y)(y-z)(z-x)$.
- $a^2+b^2+c^2 = ab+bc+ca \iff a=b=c$.
- $a^3+b^3+c^3 = s^3 - 3sP + 3R$ where $s$ = sum, $P$ = pairwise, $R$ = product.
"""

    S.pattern("alg-p9", "Zero-sum cubes", "very common",
        "A bracket sum of zero is hidden in the stem: $a+b+c=0$, or terms like $(x-y)^3+(y-z)^3+(z-x)^3$.",
        r"a+b+c=0 \Rightarrow a^3+b^3+c^3=3abc",
        r"""1. Check whether the three terms (or the three variables) add to zero.
2. If yes, replace the cube-sum by 3×(product) — done in one line.
3. For $(x-y)^3+(y-z)^3+(z-x)^3$ the product is $(x-y)(y-z)(z-x)$.

Why: with zero sum the big identity reduces to exactly this, for any three terms adding to zero.""",
        "If $(x-y)=2$ and $(y-z)=3$, then $(x-y)^3+(y-z)^3+(z-x)^3$ equals:",
        r"""Brackets sum to 0 → cube-sum $= 3(x-y)(y-z)(z-x)$.
$z-x = -(2+3) = -5$ → value $= 3\times2\times3\times(-5) = -90$.""")
    S.pattern("alg-p10", "Factor / half form of the cube identity", "very common",
        "$a+b+c$ and $ab+bc+ca$ (or $a^2+b^2+c^2$) given; $a^3+b^3+c^3-3abc$ asked.",
        r"a^3+b^3+c^3-3abc = s(s^2-3P)",
        r"""1. Write $s = a+b+c$, $P = ab+bc+ca$.
2. If $a^2+b^2+c^2$ is given instead: $P = \frac{s^2-(a^2+b^2+c^2)}{2}$.
3. Answer $= s(s^2-3P)$.

Why: the bracket is exactly $(a+b+c)^2 - 3P$ after substituting $a^2+b^2+c^2 = s^2-2P$.""",
        "If $a+b+c=6$ and $ab+bc+ca=11$, then $a^3+b^3+c^3-3abc$ equals:",
        r"$6\times(36 - 33) = 18$.")
    S.pattern("alg-p11", "Equal variables case", "common",
        "The condition $a^2+b^2+c^2 = ab+bc+ca$ (or a rearranged version) appears; conclude all variables are equal.",
        r"a^2+b^2+c^2-ab-bc-ca = \tfrac12[(a-b)^2+(b-c)^2+(c-a)^2] = 0 \Rightarrow a=b=c",
        r"""1. Recognise the half-sum-of-squares form; the condition forces $a=b=c$.
2. Substitute the common value $= \frac{a+b+c}{3}$.
3. Evaluate any symmetric expression from there.

Why: squares are non-negative, so their sum vanishes only pairwise.""",
        "If $x^2+y^2+z^2 = xy+yz+zx$ and $x+y+z=9$, then $x^2+y^2+z^2$ equals:",
        r"$x=y=z=3$ → $x^2+y^2+z^2 = 27$.")
    S.pattern("alg-p12", "Power sums with abc", "common",
        r"Three of $\{a+b+c,\ ab+bc+ca,\ abc,\ a^3+b^3+c^3\}$ are given; the fourth is asked.",
        r"s^3 = a^3+b^3+c^3 + 3sP - 3R",
        r"""1. Write the expansion $a^3+b^3+c^3 = s^3 - 3sP + 3R$.
2. Substitute the three known quantities.
3. Solve for the fourth — one linear step, no factoring of cubics.

Why: the cube of the sum expands into exactly these symmetric pieces.""",
        "If $a+b+c=6$, $abc=6$ and $a^3+b^3+c^3=90$, then $ab+bc+ca$ equals:",
        r"$216 = 90 + 18P - 18$ → $18P = 144$ → $P = 8$.")

    # ---- practice (alg-three-var) ----
    assert 3 * 8 == 24
    S.q("alg-p9", "easy",
        "If $a+b+c=0$ and $abc=8$, then the value of $a^3+b^3+c^3$ is:",
        ["24", "8", "16", "0"], "24",
        r"Zero sum → $a^3+b^3+c^3 = 3abc = 24$.",
        None, 25)
    assert 3 * 2 * 3 * (-5) == -90
    S.q("alg-p9", "easy",
        "If $x-y=2$ and $y-z=3$, then the value of $(x-y)^3+(y-z)^3+(z-x)^3$ is:",
        ["-90", "90", "-30", "30"], "-90",
        r"Brackets sum to 0 → cube-sum $= 3(x-y)(y-z)(z-x)$. $z-x = -5$ → $3\times2\times3\times(-5) = -90$.",
        None, 30)
    assert 3 * 1 == 3
    S.q("alg-p11", "easy",
        "If $a+b+c=3$ and $ab+bc+ca=3$, then the value of $a^3+b^3+c^3$ is:",
        ["3", "9", "27", "1"], "3",
        r"$a^2+b^2+c^2 = 9-6 = 3 = ab+bc+ca$ → $a=b=c=1$ → cube-sum $= 3$.",
        None, 35)
    v = 6 * (36 - 33)
    assert v == 18
    S.q("alg-p10", "medium",
        "If $a+b+c=6$ and $ab+bc+ca=11$, then the value of $a^3+b^3+c^3-3abc$ is:",
        ["18", "27", "36", "54"], "18",
        r"$s(s^2-3P) = 6\times(36-33) = 18$.",
        None, 35)
    P = (81 - 29) / F(2)
    v = 9 * (81 - 3 * P)
    assert P == 26 and v == 27
    S.q("alg-p10", "medium",
        "If $a+b+c=9$ and $a^2+b^2+c^2=29$, then the value of $a^3+b^3+c^3-3abc$ is:",
        ["27", "81", "54", "243"], "27",
        r"$P = \frac{81-29}{2} = 26$ → $s(s^2-3P) = 9\times(81-78) = 27$.",
        None, 40)
    v = 9 ** 3 - 3 * 9 * 11 + 3 * 6
    assert v == 450
    S.q("alg-p12", "medium",
        "If $a+b+c=9$, $ab+bc+ca=11$ and $abc=6$, then the value of $a^3+b^3+c^3$ is:",
        ["450", "468", "432", "720"], "450",
        r"$a^3+b^3+c^3 = 9^3 - 3\times9\times11 + 3\times6 = 729 - 297 + 18 = 450$.",
        None, 45)
    P8 = F(216 - 90 + 18, 3 * 6)
    assert P8 == 8
    S.q("alg-p12", "easy",
        "If $a+b+c=6$, $abc=6$ and $a^3+b^3+c^3=90$, then the value of $ab+bc+ca$ is:",
        ["8", "9", "6", "12"], "8",
        r"$s^3 = 216 = 90 + 3\times6\times P - 3\times6$ → $18P = 144$ → $P = 8$.",
        None, 35)
    assert 3 * 4 * 5 * 6 == 360
    S.q("alg-p10", "medium",
        "If $x+y=4$, $y+z=5$ and $z+x=6$, then the value of $(x+y+z)^3-x^3-y^3-z^3$ is:",
        ["360", "120", "180", "240"], "360",
        r"$(x+y+z)^3-x^3-y^3-z^3 = 3(x+y)(y+z)(z+x) = 3\times4\times5\times6 = 360$.",
        "Sum $= \\frac{4+5+6}{2} = 7.5$ if ever needed.", 45)
    a, b, c = complex(2, 0), complex(-1, 1), complex(-1, -1)
    assert abs(a + b + c) < 1e-9
    assert abs((a ** 3 + b ** 3 + c ** 3) - 3 * a * b * c) < 1e-9
    assert abs(((a ** 3 + b ** 3 + c ** 3) / (a * b * c)) ** 2 - 9) < 1e-9
    S.q("alg-p9", "hard",
        "If $a+b+c=0$, then the value of $\\dfrac{(a^3+b^3+c^3)^2}{a^2b^2c^2}$ is:",
        ["9", "3", "6", "1"], "9",
        r"Zero sum → $a^3+b^3+c^3 = 3abc$ → the ratio $= \frac{(3abc)^2}{(abc)^2} = 9$.",
        None, 50)
    Q = F(81, 3)
    assert Q == 27
    S.q("alg-p11", "medium",
        "If $x^2+y^2+z^2 = xy+yz+zx$ and $x+y+z=9$, then the value of $x^2+y^2+z^2$ is:",
        ["27", "81", "9", "54"], "27",
        r"The condition forces $x=y=z=3$ → $x^2+y^2+z^2 = 27$.",
        None, 40)
    return S


def build_surds():
    S = Sub("alg-surds")

    S.notes = r"""### Rationalising: multiply by 1, dressed up
To clear a surd from a denominator, multiply top and bottom by the conjugate:
$$\frac{1}{\sqrt7-\sqrt6} = \frac{\sqrt7+\sqrt6}{(\sqrt7-\sqrt6)(\sqrt7+\sqrt6)} = \sqrt7+\sqrt6$$
since $(\sqrt7-\sqrt6)(\sqrt7+\sqrt6) = 7-6 = 1$. With a coefficient, divide by it once: $\frac{4}{\sqrt5-1} = \frac{4(\sqrt5+1)}{4} = \sqrt5+1$, and $\frac{3}{\sqrt5+\sqrt2} = \sqrt5-\sqrt2$. The number under the pair must differ by exactly what the numerator supplies.

### Denesting $\sqrt{a+b\sqrt c}$
Try $\sqrt{a+b\sqrt c} = \sqrt p+\sqrt q$. Squaring: $p+q = a$ and $2\sqrt{pq} = b\sqrt c$. So find two numbers with sum $a$ and product $\frac{b^2c}{4}$:
$$\sqrt{15+4\sqrt{14}} = 2\sqrt2+\sqrt7 \quad (8+7 = 15,\; 2\sqrt{8\cdot7} = 4\sqrt{14})$$
$$\sqrt{11+6\sqrt2} = 3+\sqrt2 \quad (9+2 = 11,\; 2\sqrt9 = 6)$$
If the cross term is negative, take the positive root of the reversed pair: $\sqrt{11-6\sqrt2} = 3-\sqrt2$.

### The product-1 conjugate pair
When $x = p+\sqrt q$ satisfies $p^2-q = 1$, its reciprocal is the conjugate: $\frac1x = p-\sqrt q$. Then the reciprocal ladder runs for free:
$$x = 2+\sqrt3 \Rightarrow x+\frac1x = 4,\quad x^2+\frac1{x^2} = 14,\quad x^3+\frac1{x^3} = 52$$
With $x = 5+2\sqrt6$: $\frac1x = 5-2\sqrt6$ (since $25-24=1$), so $x+\frac1x = 10$ and $x^2+\frac1{x^2} = 100-2 = 98$. For $p^2-q = m \ne 1$, the pair multiplies to $m$: then $x+\frac mx$, and you divide by $\sqrt m$ to use the ladder.

### Reducing a polynomial in a surd
For $P(x)$ with $x = p+\sqrt q$, first reduce $P$ modulo the minimal quadratic $x^2-2px+(p^2-q) = 0$ — keep substituting $x^2 = 2px-(p^2-q)$ until everything is linear in $x$. Short cuts first, though: check whether the polynomial is symmetric (then the product-1 ladder applies) or whether $x^2$ itself simplifies.

### Telescoping and comparison
Each term of $\frac{1}{\sqrt{k+1}+\sqrt k} = \sqrt{k+1}-\sqrt k$ telescopes:
$$\frac1{\sqrt2+1}+\frac1{\sqrt3+\sqrt2}+\frac1{\sqrt4+\sqrt3}+\frac1{\sqrt5+\sqrt4} = \sqrt5-1$$
All interior terms cancel. For comparing surds, raise to a common power: $\sqrt2$ vs $\sqrt[3]3$ vs $\sqrt[4]4$ → compare $2^6 = 64$, $3^4 = 81$, $4^3 = 64$ → $\sqrt[3]3$ is the largest.

### Common traps
- Rationalising with the wrong conjugate sign (the denominator must get a DIFFERENCE to become rational).
- Denesting with $p+q$ and $2pq$ mismatched — always re-square to check.
- Forgetting $p^2-q=1$ before claiming $\frac1x$ is the conjugate.
- Assuming nested radicals simplify — some (like $\sqrt{6+\sqrt{11}}$) do not denest neatly; fall back to squaring the whole equation.

### Quick revision
- $\frac1{\sqrt a+\sqrt b} = \frac{\sqrt a-\sqrt b}{a-b}$.
- $\sqrt{a+b\sqrt c} = \sqrt p+\sqrt q$ with $p+q = a$, $2\sqrt{pq} = b\sqrt c$.
- $x = p+\sqrt q$, $p^2-q=1$ → $\frac1x = p-\sqrt q$; run the $x+\frac1x$ ladder.
- $\frac1{\sqrt{k+1}+\sqrt k} = \sqrt{k+1}-\sqrt k$ — telescopes.
- Compare surds by a common power: $2^6$ vs $3^4$ vs $4^3$.
"""

    S.pattern("alg-p13", "Denesting a nested surd", "common",
        "$\\sqrt{a+b\\sqrt c}$ to be written as $\\sqrt p+\\sqrt q$ (or simplified).",
        r"\sqrt{a+b\sqrt c} = \sqrt p+\sqrt q,\quad p+q=a,\ 2\sqrt{pq}=b\sqrt c",
        r"""1. Look for two numbers with sum $a$ and product $\frac{b^2c}{4}$.
2. Write $\sqrt p+\sqrt q$ from the pair.
3. Re-square mentally to confirm: $(\sqrt p+\sqrt q)^2 = a + 2\sqrt{pq}$.

Why: squaring the ansatz produces exactly the two matching conditions.""",
        "The simplified form of $\\sqrt{11+6\\sqrt2}$ is:",
        r"$3+\sqrt2$ — since $3+2 = 5$... check: $(3+\sqrt2)^2 = 9+2+6\sqrt2 = 11+6\sqrt2$. Correct.")
    S.pattern("alg-p14", "Rationalise the denominator", "very common",
        "A fraction with a surd (or binomial surd) denominator; simplify or compute.",
        r"\frac{1}{\sqrt a\pm\sqrt b} = \frac{\sqrt a\mp\sqrt b}{a-b}",
        r"""1. Multiply top and bottom by the conjugate of the denominator.
2. The denominator becomes $a-b$ (or $p^2-qn$ for $p\pm\sqrt q$ forms).
3. Cancel the common factor with the numerator before multiplying out.

Why: $(\sqrt a-\sqrt b)(\sqrt a+\sqrt b) = a-b$ removes the root from the denominator.""",
        "The simplified value of $\\dfrac{4}{\\sqrt5-1}$ is:",
        r"$\frac{4(\sqrt5+1)}{5-1} = \sqrt5+1$. Cancel the 4 first if the form allows.")
    S.pattern("alg-p15", "Conjugate pair $x\\cdot y = 1$", "very common",
        "$x = p+\\sqrt q$ (e.g. $2+\\sqrt3$, $5+2\\sqrt6$) given; $x+\\frac1x$, $x^2+\\frac1{x^2}$, $x^3+\\frac1{x^3}$ asked.",
        r"p^2-q=1 \Rightarrow \frac1x = p-\sqrt q",
        r"""1. Check $p^2-q$: if it equals 1, then $\frac1x = p-\sqrt q$.
2. $x+\frac1x = 2p$ — instant.
3. Climb the ladder: square (subtract 2), cube ($k^3-3k$).

Why: the conjugate is the exact reciprocal when the norm $p^2-q$ is 1.""",
        "If $x=2+\\sqrt3$, then $x^3+\\frac1{x^3}$ equals:",
        r"$\frac1x = 2-\sqrt3$ → $x+\frac1x = 4$ → $x^3+\frac1{x^3} = 64-12 = 52$.")
    S.pattern("alg-p16", "Telescoping / comparing surds", "common",
        "A sum of fractions $\\frac1{\\sqrt{k+1}+\\sqrt k}$ that cancels, or a comparison of unlike roots ($\\sqrt2$ vs $\\sqrt[3]3$ vs $\\sqrt[4]4$).",
        r"\frac1{\sqrt{k+1}+\sqrt k} = \sqrt{k+1}-\sqrt k; \qquad \text{compare via } a^{\text{lcm}}",
        r"""1. Rewrite each fraction as a difference of consecutive roots; the middle terms cancel.
2. For comparisons, raise everything to the LCM power and compare integers.
3. Keep the numeric values of small roots ready ($\sqrt2 = 1.414$, $\sqrt3 = 1.732$, $\sqrt5 = 2.236$).

Why: the conjugate turns each term into a telescoping difference; common powers make roots comparable.""",
        "The greatest of $\\sqrt2,\\ \\sqrt[3]3,\\ \\sqrt[4]4$ is:",
        r"Raise to the 12th power: $2^6 = 64$, $3^4 = 81$, $4^3 = 64$ → $\sqrt[3]3$ wins.")

    # ---- practice (alg-surds) ----
    assert abs((2 * math.sqrt(2) + math.sqrt(7)) ** 2 - (15 + 4 * math.sqrt(14))) < 1e-9
    S.q("alg-p13", "easy",
        "The simplified form of $\\sqrt{15+4\\sqrt{14}}$ is:",
        ["$2\\sqrt2+\\sqrt7$", "$2\\sqrt2-\\sqrt7$", "$\\sqrt2+2\\sqrt7$", "$\\sqrt{14}+1$"], "$2\\sqrt2+\\sqrt7$",
        r"$2\sqrt2+\sqrt7$: squares give $8+7 = 15$ and $2\sqrt{8\times7} = 4\sqrt{14}$. Verified.",
        None, 35)
    assert abs(1 / (math.sqrt(7) - math.sqrt(6)) - (math.sqrt(7) + math.sqrt(6))) < 1e-9
    S.q("alg-p14", "easy",
        "$\\dfrac{1}{\\sqrt7-\\sqrt6}$ is equal to:",
        ["$\\sqrt7+\\sqrt6$", "$\\sqrt6-\\sqrt7$", "$\\sqrt7-\\sqrt6$", "$1$"], "$\\sqrt7+\\sqrt6$",
        r"$(\sqrt7-\sqrt6)(\sqrt7+\sqrt6) = 7-6 = 1$ → the reciprocal is $\sqrt7+\sqrt6$.",
        None, 25)
    assert abs(4 / (math.sqrt(5) - 1) - (math.sqrt(5) + 1)) < 1e-9
    S.q("alg-p14", "easy",
        "The simplified value of $\\dfrac{4}{\\sqrt5-1}$ is:",
        ["$\\sqrt5+1$", "$\\sqrt5-1$", "$1-\\sqrt5$", "$4\\sqrt5$"], "$\\sqrt5+1$",
        r"$\frac{4(\sqrt5+1)}{5-1} = \sqrt5+1$.",
        None, 25)
    assert abs((2 + math.sqrt(3)) + 1 / (2 + math.sqrt(3)) - 4) < 1e-9
    S.q("alg-p15", "easy",
        "If $x=2+\\sqrt3$, then the value of $x+\\frac1x$ is:",
        ["4", "$2\\sqrt3$", "2", "$4\\sqrt3$"], "4",
        r"$\frac1x = 2-\sqrt3$ (since $4-3=1$) → $x+\frac1x = 4$.",
        None, 25)
    assert abs((2 + math.sqrt(3)) ** 2 + 1 / (2 + math.sqrt(3)) ** 2 - 14) < 1e-9
    S.q("alg-p15", "medium",
        "If $x=2+\\sqrt3$, then the value of $x^2+\\frac1{x^2}$ is:",
        ["14", "7", "12", "15"], "14",
        r"$x+\frac1x = 4$ → $x^2+\frac1{x^2} = 4^2-2 = 14$.",
        None, 30)
    assert abs((2 + math.sqrt(3)) ** 3 + 1 / (2 + math.sqrt(3)) ** 3 - 52) < 1e-9
    S.q("alg-p15", "medium",
        "If $x=2+\\sqrt3$, then the value of $x^3+\\frac1{x^3}$ is:",
        ["52", "48", "56", "64"], "52",
        r"$x+\frac1x = 4$ → $x^3+\frac1{x^3} = 4^3-3\times4 = 52$.",
        None, 35)
    assert abs(3 / (math.sqrt(5) + math.sqrt(2)) - (math.sqrt(5) - math.sqrt(2))) < 1e-9
    S.q("alg-p14", "medium",
        "The simplified value of $\\dfrac{3}{\\sqrt5+\\sqrt2}$ is:",
        ["$\\sqrt5-\\sqrt2$", "$\\sqrt5+\\sqrt2$", "$\\dfrac{\\sqrt5-\\sqrt2}{3}$", "$3$"], "$\\sqrt5-\\sqrt2$",
        r"$\frac{3(\sqrt5-\sqrt2)}{5-2} = \sqrt5-\sqrt2$.",
        None, 30)
    assert abs(1 / (math.sqrt(2) + 1) + 1 / (math.sqrt(3) + math.sqrt(2)) + 1 / (2 + math.sqrt(3)) + 1 / (math.sqrt(5) + 2) - (math.sqrt(5) - 1)) < 1e-9
    S.q("alg-p16", "medium",
        "The value of $\\dfrac1{\\sqrt2+1}+\\dfrac1{\\sqrt3+\\sqrt2}+\\dfrac1{\\sqrt4+\\sqrt3}+\\dfrac1{\\sqrt5+\\sqrt4}$ is:",
        ["$\\sqrt5-1$", "$\\sqrt5+1$", "$1-\\sqrt5$", "$2\\sqrt5$"], "$\\sqrt5-1$",
        r"""Each term is a root difference: $(\sqrt2-1)+(\sqrt3-\sqrt2)+(\sqrt4-\sqrt3)+(\sqrt5-\sqrt4)$.
Everything cancels except $\sqrt5-1$.""",
        None, 45)
    assert abs((3 + math.sqrt(2)) ** 2 - (11 + 6 * math.sqrt(2))) < 1e-9
    S.q("alg-p13", "medium",
        "The simplified form of $\\sqrt{11+6\\sqrt2}$ is:",
        ["$3+\\sqrt2$", "$3-\\sqrt2$", "$\\sqrt2+2\\sqrt3$", "$6\\sqrt2$"], "$3+\\sqrt2$",
        r"$(3+\sqrt2)^2 = 9+2+6\sqrt2 = 11+6\sqrt2$.",
        None, 35)
    assert abs(math.sqrt(2) ** 12 - 64) < 1e-9 and abs(3 ** 4 - 81) < 1e-9 and abs(4 ** 3 - 64) < 1e-9
    S.q("alg-p16", "medium",
        "The greatest among $\\sqrt2,\\ \\sqrt[3]3,\\ \\sqrt[4]4$ is:",
        ["$\\sqrt[3]3$", "$\\sqrt2$", "$\\sqrt[4]4$", "all are equal"], "$\\sqrt[3]3$",
        r"Raise to the 12th: $2^6 = 64$, $3^4 = 81$, $4^3 = 64$ → $\sqrt[3]3$ is greatest.",
        None, 40)
    assert abs((5 + 2 * math.sqrt(6)) ** 2 + 1 / (5 + 2 * math.sqrt(6)) ** 2 - 98) < 1e-9
    S.q("alg-p15", "hard",
        "If $x=5+2\\sqrt6$, then the value of $x^2+\\frac1{x^2}$ is:",
        ["98", "100", "96", "49"], "98",
        r"$\frac1x = 5-2\sqrt6$ ($25-24=1$) → $x+\frac1x = 10$ → $x^2+\frac1{x^2} = 100-2 = 98$.",
        None, 45)
    return S
