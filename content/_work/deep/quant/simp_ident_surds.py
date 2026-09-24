"""Phase-2 deep content for quant/simplification — identities, surds, roots, approximation."""
import sys, os, math
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
from fractions import Fraction as F
from _lib import Sub, nearest, fr, num

of = r"\text{ of }"


def build_identities():
    S = Sub("simp-identities")
    S.notes = r"""### Why identities?
Many simplification questions are just **algebraic identities** with numbers pasted in. If you can see the shape, the answer comes in one line — no cubing of 3.3 needed.

### The identities you must know
| Identity | Read as |
|---|---|
| $(a+b)^2 = a^2 + 2ab + b^2$ | square of sum |
| $(a-b)^2 = a^2 - 2ab + b^2$ | square of difference |
| $(a+b)(a-b) = a^2 - b^2$ | difference of squares |
| $a^3 + b^3 = (a+b)(a^2 - ab + b^2)$ | sum of cubes |
| $a^3 - b^3 = (a-b)(a^2 + ab + b^2)$ | difference of cubes |
| $(a \pm b)^3 = a^3 \pm b^3 \pm 3ab(a \pm b)$ | cube of sum/difference |
| $a^3 + b^3 + c^3 - 3abc = (a+b+c)(a^2+b^2+c^2-ab-bc-ca)$ | three-variable |

**Zero-sum magic:** if $a + b + c = 0$, the long factor is not zero, so $a^3 + b^3 + c^3 = 3abc$.
Example: $25^3 + (-17)^3 + (-8)^3 = 3 \times 25 \times (-17) \times (-8) = 10200$.

### Identity fractions (the most asked shape)
Because $a^3 + b^3 = (a+b)(a^2 - ab + b^2)$, the bracket cancels:
$$\frac{a^3 + b^3}{a^2 - ab + b^2} = a+b, \qquad \frac{a^3 - b^3}{a^2 + ab + b^2} = a-b$$
Example: $\frac{(15.2)^3 - (5.2)^3}{(15.2)^2 + 15.2 \times 5.2 + (5.2)^2} = 15.2 - 5.2 = 10$.
Check the middle sign: **minus** in the denominator pairs with **plus** on top.

### Shortcuts from the squares
- $(a+b)^2 + (a-b)^2 = 2(a^2 + b^2)$
- $(a+b)^2 - (a-b)^2 = 4ab$
- $a^2 + b^2 = (a+b)^2 - 2ab$
- $a^3 + b^3 = (a+b)^3 - 3ab(a+b)$
Example: with $a+b = 7$, $ab = 12$: $a^3 + b^3 = 343 - 3 \times 12 \times 7 = 91$.

### The x + 1/x family (asked again and again)
If $x + \frac{1}{x} = k$, then:
- $x^2 + \frac{1}{x^2} = k^2 - 2$
- $x^3 + \frac{1}{x^3} = k^3 - 3k$
- $x^4 + \frac{1}{x^4} = (k^2-2)^2 - 2$
If $x - \frac{1}{x} = k$, then $x^2 + \frac{1}{x^2} = k^2 + 2$ and $x^3 - \frac{1}{x^3} = k^3 + 3k$.
Example: $x + \frac{1}{x} = 4$ → $x^2 + \frac{1}{x^2} = 16 - 2 = 14$.

### Numbers near a round value
$105^2 - 95^2 = (105-95)(105+95) = 10 \times 200 = 2000$. Use $a^2 - b^2$ whenever two squares sit close together.

### Cubes when a sum and a product are given
If $a+b$ and $ab$ are known, never cube anything big:
- $a^2 + b^2 = (a+b)^2 - 2ab$
- $a^3 + b^3 = (a+b)^3 - 3ab(a+b)$
Example: $a+b = 10$, $ab = 21$ → $a^2 + b^2 = 100 - 42 = 58$.
The same two facts give $a^3 - b^3$ if you first find $a-b$ from $(a-b)^2 = (a+b)^2 - 4ab$.

### How to attack any identity question
1. Look at the **denominator first** (if there is one) — it tells you which factor will cancel.
2. Match the **signs** to pick plus or minus identities; a wrong middle sign is the classic trap.
3. Substitute only at the last step; keep $a$, $b$ symbolic until the expression is fully factored.

### Quick revision
- $\frac{a^3 \pm b^3}{a^2 \mp ab + b^2} = a \pm b$.
- $a+b+c = 0$ → cubes sum to $3abc$.
- $x+\frac1x = k$: squares give $k^2-2$, cubes give $k^3-3k$.
- $(a+b)^2 - (a-b)^2 = 4ab$.
- Difference of squares for near numbers.
"""

    S.pattern("simp-id-p1", "Identity fraction: cubes over the quadratic factor", "very common",
        "A fraction with a³ + b³ (or a³ − b³) on top — often decimals — and a² − ab + b² (or a² + ab + b²) below.",
        r"\frac{a^3 \pm b^3}{a^2 \mp ab + b^2} = a \pm b",
        r"""1. Check the sign in the denominator: minus below pairs with plus above; plus below pairs with minus above.
2. Cancel the common quadratic factor.
3. The answer is just a + b (or a − b).

Why: $a^3 \pm b^3 = (a \pm b)(a^2 \mp ab + b^2)$ — the denominator is literally the second factor.""",
        r"$\frac{(15.2)^3 - (5.2)^3}{(15.2)^2 + 15.2 \times 5.2 + (5.2)^2}$ = ?",
        r"Denominator is $a^2+ab+b^2$ → value $= 15.2 - 5.2 = 10$.")
    S.pattern("simp-id-p2", "Squares near each other; (x+y)² and (x−y)² combos", "very common",
        "$105^2 - 95^2$-type questions, or the value of $(x+y)^2 + (x-y)^2$ for given x, y.",
        r"a^2 - b^2 = (a-b)(a+b),\quad (x+y)^2 + (x-y)^2 = 2(x^2+y^2)",
        r"""1. Difference of two squares → factor it, never square the big numbers.
2. $(x+y)^2 + (x-y)^2 = 2x^2 + 2y^2$; their difference is $4xy$.

Why: the cross terms ($\pm 2xy$) cancel or double depending on the combination.""",
        r"Find $105^2 - 95^2$.",
        r"$(105-95)(105+95) = 10 \times 200 = 2000$.")
    S.pattern("simp-id-p3", r"x + 1/x family (squares, cubes, fourth powers)", "very common",
        r"'If $x + \frac{1}{x} = 4$, find $x^2 + \frac{1}{x^2}$' — the minus version is equally common.",
        r"x^2+\tfrac{1}{x^2} = k^2 \mp 2,\quad x^3\pm\tfrac{1}{x^3} = k^3 \mp 3k",
        r"""1. Square the given sum — the cross term is always 2.
2. Subtract 2 (plus version) or add 2 (minus version).
3. For cubes use $k^3 \mp 3k$; for fourth powers, square the squared result and subtract 2.

Why: $\left(x \pm \frac1x\right)^2 = x^2 + \frac{1}{x^2} \pm 2$.""",
        r"If $x - \frac{1}{x} = 5$, find $x^2 + \frac{1}{x^2}$.",
        r"$25 + 2 = 27$.")
    S.pattern("simp-id-p4", "Given a + b and ab: find a² + b², a³ + b³", "very common",
        "The pair sum and product are given; the target is a square-sum, cube-sum or similar symmetric value.",
        r"a^2+b^2 = (a+b)^2-2ab,\quad a^3+b^3 = (a+b)^3-3ab(a+b)",
        r"""1. Write the target in terms of (a+b) and ab.
2. Substitute the two given numbers.
3. If asked for a and b themselves, spot small integer pairs.

Why: every symmetric expression in a and b is a function of (a+b) and ab.""",
        r"If $a+b = 7$, $ab = 12$, find $a^3+b^3$.",
        r"$343 - 3 \times 12 \times 7 = 91$ (the numbers are 3 and 4).")
    S.pattern("simp-id-p5", "Zero-sum cubes: a³ + b³ + c³ = 3abc", "common",
        "Three cubes (fractions or signed numbers) whose bases add up to 0.",
        r"a+b+c = 0 \Rightarrow a^3+b^3+c^3 = 3abc",
        r"""1. Add the three bases — confirm the sum is 0.
2. Multiply the bases together, then by 3.
3. Mind the signs: two negatives multiply to a plus.

Why: $a^3+b^3+c^3 - 3abc = (a+b+c)(\dots)$, so a zero sum forces the cube-sum to equal $3abc$.""",
        r"Find $25^3 + (-17)^3 + (-8)^3$.",
        r"Bases: $25-17-8 = 0$ → $3 \times 25 \times 17 \times 8 = 10200$.")

    v = F(27, 10) ** 3 + F(33, 10) ** 3
    den = F(27, 10) ** 2 - F(27, 10) * F(33, 10) + F(33, 10) ** 2
    assert v / den == 6
    S.q("simp-id-p1", "easy",
        r"Simplify: $\frac{(2.7)^3 + (3.3)^3}{(2.7)^2 - 2.7 \times 3.3 + (3.3)^2}$",
        ["6", "0.6", "11.9", "2.7"], "6",
        r"Denominator is $a^2 - ab + b^2$, so the numerator factors as $(a+b)(a^2-ab+b^2)$. Value $= a + b = 2.7 + 3.3 = 6$.",
        "Trap 0.6 = 6 ÷ 10 if you cube 2.7 wrongly.", 35)
    v = F(152, 10) ** 3 - F(52, 10) ** 3
    den = F(152, 10) ** 2 + F(152, 10) * F(52, 10) + F(52, 10) ** 2
    assert v / den == 10
    S.q("simp-id-p1", "easy",
        r"Simplify: $\frac{(15.2)^3 - (5.2)^3}{(15.2)^2 + 15.2 \times 5.2 + (5.2)^2}$",
        ["10", "20.4", "15.2", "5.2"], "10",
        r"$a^3 - b^3 = (a-b)(a^2 + ab + b^2)$, so the value is simply $a - b = 15.2 - 5.2 = 10$.",
        None, 35)
    v = 105 ** 2 - 95 ** 2
    assert v == 2000
    S.q("simp-id-p2", "easy", r"Find the value of $105^2 - 95^2$.",
        ["2000", "1000", "400", "19900"], str(v),
        r"$105^2 - 95^2 = (105-95)(105+95) = 10 \times 200 = 2000$.",
        "Trap 19,900: computing both squares fully and mis-subtracting is slow and error-prone.", 30)
    v = (34 + 16) ** 2 + (34 - 16) ** 2
    assert v == 2 * (34 ** 2 + 16 ** 2) == 2824
    S.q("simp-id-p2", "medium",
        r"If $x = 34$ and $y = 16$, find the value of $(x+y)^2 + (x-y)^2$.",
        ["2824", "1412", "2500", "3250"], str(v),
        r"""$(x+y)^2 + (x-y)^2 = 2x^2 + 2y^2 = 2(34^2 + 16^2) = 2(1156 + 256) = 2824$.""",
        r"Trap 1412 is $x^2 + y^2$ — you forgot the factor 2.", 40)
    S.q("simp-id-p3", "easy",
        r"If $x + \frac{1}{x} = 4$, find the value of $x^2 + \frac{1}{x^2}$.",
        ["14", "16", "18", "12"], "14",
        r"$x^2 + \frac{1}{x^2} = \left(x + \frac{1}{x}\right)^2 - 2 = 16 - 2 = 14$.",
        None, 30)
    S.q("simp-id-p3", "medium",
        r"If $x - \frac{1}{x} = 5$, find the value of $x^2 + \frac{1}{x^2}$.",
        ["27", "23", "25", "29"], "27",
        r"""$\left(x - \frac{1}{x}\right)^2 = x^2 - 2 + \frac{1}{x^2} = 25$.
So $x^2 + \frac{1}{x^2} = 25 + 2 = 27$.""",
        r"Minus version: add 2, not subtract.", 35)
    S.q("simp-id-p4", "easy",
        r"If $a + b = 10$ and $ab = 21$, find the value of $a^2 + b^2$.",
        ["58", "79", "121", "100"], "58",
        r"$a^2 + b^2 = (a+b)^2 - 2ab = 100 - 42 = 58$.",
        None, 30)
    v = 7 ** 3 - 3 * 12 * 7
    assert v == 91 and 4 ** 3 + 3 ** 3 == v
    S.q("simp-id-p4", "medium",
        r"If $a + b = 7$ and $ab = 12$, find the value of $a^3 + b^3$.",
        ["91", "559", "235", "139"], str(v),
        r"$a^3 + b^3 = (a+b)^3 - 3ab(a+b) = 343 - 3 \times 12 \times 7 = 343 - 252 = 91$.",
        r"Check: the numbers are 3 and 4, and $27 + 64 = 91$ ✓.", 40)
    v = F(1, 2) ** 3 + F(1, 3) ** 3 + F(-5, 6) ** 3
    assert v == 3 * F(1, 2) * F(1, 3) * F(-5, 6) == F(-5, 12)
    S.q("simp-id-p5", "hard",
        r"Find the value of $\left(\frac{1}{2}\right)^3 + \left(\frac{1}{3}\right)^3 + \left(-\frac{5}{6}\right)^3$.",
        [fr(v), fr(-v), fr(F(-3, 8)), fr(F(-1, 6))], fr(v),
        r"""$\frac{1}{2} + \frac{1}{3} - \frac{5}{6} = \frac{3+2-5}{6} = 0$. Zero sum!
So cube-sum $= 3abc = 3 \times \frac{1}{2} \times \frac{1}{3} \times \left(-\frac{5}{6}\right) = -\frac{5}{12}$.""",
        None, 55)
    v = 25 ** 3 + (-17) ** 3 + (-8) ** 3
    assert v == 3 * 25 * (-17) * (-8) == 10200
    S.q("simp-id-p5", "hard",
        r"Find the value of $25^3 + (-17)^3 + (-8)^3$.",
        ["10200", "9826", "10500", "10000"], str(v),
        r"""$25 - 17 - 8 = 0$, so the cubes add up to $3abc$:
$3 \times 25 \times (-17) \times (-8) = 3 \times 25 \times 136 = 10200$.""",
        "Two minuses multiply to a plus.", 50)
    return S


def build_surds():
    S = Sub("simp-surds-indices")
    S.notes = r"""### What are surds and indices?
**Indices** are powers: $2^5$ means 2 multiplied 5 times. **Surds** are roots that stay irrational, like $\sqrt{3}$ or $\sqrt[3]{5}$. Simplification questions ask you to bend both into easy shapes.

### Laws of indices
- $a^m \times a^n = a^{m+n}$, $\frac{a^m}{a^n} = a^{m-n}$
- $(a^m)^n = a^{mn}$
- $a^0 = 1$, $a^{-n} = \frac{1}{a^n}$
- $a^{1/n} = \sqrt[n]{a}$, $a^{m/n} = (\sqrt[n]{a})^m$

**Equation solving:** make every base the same, then set the powers equal.
Example: $2^{x+3} \times 4^{x-1} = 128$ → $2^{x+3+2x-2} = 2^7$ → $3x + 1 = 7$ → $x = 2$.
Fractional-index values: $(32)^{2/5} = (2^5)^{2/5} = 2^2 = 4$; $(81)^{3/4} = 27$.

### Rationalising the denominator
Multiply top and bottom by the **conjugate** (same terms, opposite middle sign):
$$\frac{1}{\sqrt{a}+\sqrt{b}} = \frac{\sqrt{a}-\sqrt{b}}{a-b}$$
So $\frac{1}{\sqrt7 - \sqrt6} = \sqrt7 + \sqrt6$, and $\frac{1}{\sqrt9+\sqrt8} = \sqrt9 - \sqrt8$.
A **telescoping chain** collapses to its ends. The plus-form chain:
$$\frac{1}{\sqrt9+\sqrt8} + \frac{1}{\sqrt8+\sqrt7} + \dots + \frac{1}{\sqrt2+1} = (\sqrt9-\sqrt8) + (\sqrt8-\sqrt7) + \dots + (\sqrt2-1) = \sqrt9 - 1 = 2.$$
Watch the form: a chain of $\frac{1}{\sqrt{k}+\sqrt{k-1}}$ terms turns into $\sqrt{k}-\sqrt{k-1}$ and only the two ends survive.

### Roots of surds: the a + 2√b split
To find $\sqrt{a + 2\sqrt{b}}$, find two numbers $x, y$ with $x + y = a$ and $xy = b$. Then the answer is $\sqrt{x} + \sqrt{y}$ (or $\sqrt x - \sqrt y$ when the middle sign is minus).
Example: $\sqrt{11 + 6\sqrt2} = \sqrt{11 + 2\sqrt{18}}$; $x + y = 11$, $xy = 18$ → $x, y = 9, 2$ → answer $\sqrt9 + \sqrt2 = 3 + \sqrt2$.

### Comparing surds
Put every surd to the power of the **LCM of the root orders** and compare the results.
$\sqrt3, \sqrt[4]{7}, \sqrt[3]{5}$: raise to the 12th power → $3^6 = 729$, $7^3 = 343$, $5^4 = 625$. So $\sqrt3$ is the largest.

### Surd plus its reciprocal
If $x = a + \sqrt{b}$, then $\frac{1}{x}$ is usually $a - \sqrt{b}$-type. Example: $x = 5 + 2\sqrt6$ → $\frac{1}{x} = 5 - 2\sqrt6$ (check: product = $25 - 24 = 1$). So $x + \frac{1}{x} = 10$.
The condition is $a^2 - b = 1$ (or a perfect square): only then does the product land on a whole number. Always do this one-line check before writing the reciprocal.

### Typical exam traps
- $(a^m)^n = a^{mn}$, **not** $a^{m+n}$: $(2^3)^2 = 64$, not $2^5$.
- Negative power flips the base: $2^{-3} = \frac{1}{8}$ — an option pair (8 vs $\frac{1}{8}$) usually tests exactly this.
- $\sqrt{a+b}$ is **not** $\sqrt a + \sqrt b$: $\sqrt{9+16} = 5$, not 7.
- In $\sqrt{a + 2\sqrt b}$, forget to write the middle term as $2\sqrt b$ and the split fails: $6\sqrt2 = 2\sqrt{18}$, so $b = 18$, not 2.

### Quick revision
- Same base → equate exponents; fractional power = root first, then power.
- Conjugate rationalises; telescoping chains collapse to first minus last.
- $\sqrt{a+2\sqrt b}$: split $a$ into two factors of $b$.
- Compare surds via LCM-of-orders power.
- $x = a+2\sqrt b$-type → reciprocal is $a-2\sqrt b$.
"""

    S.pattern("simp-si-p1", "Indices: evaluate powers or solve a power equation", "very common",
        r"Fractional/negative powers to evaluate like $(32)^{2/5}$, or an equation like $2^{x+3} \times 4^{x-1} = 128$.",
        r"a^m \times a^n = a^{m+n},\quad (a^m)^n = a^{mn},\quad a^{-n} = \tfrac{1}{a^n}",
        r"""1. Rewrite every number as a power of one prime ($32 = 2^5$, $81 = 3^4$).
2. Add the exponents on the left; write the right side as a power too.
3. Equate exponents and solve.

Why: equal bases make the equation an ordinary linear equation in the exponent.""",
        r"Find $(32)^{2/5} \times (81)^{3/4} \div (27)^{2/3}$.",
        r"$= 2^2 \times 3^3 \div 3^2 = 4 \times 3 = 12$.")
    S.pattern("simp-si-p2", "Rationalisation and telescoping surd fractions", "very common",
        r"Fractions like $\frac{1}{\sqrt7-\sqrt6}$, sums of many such fractions, or a surd plus its reciprocal.",
        r"\frac{1}{\sqrt{a}\pm\sqrt{b}} = \frac{\sqrt{a}\mp\sqrt{b}}{a-b}",
        r"""1. Multiply top and bottom by the conjugate.
2. For a long sum, rationalise each term — the middle roots cancel (telescoping) and only the ends survive.
3. If $x = a + \sqrt b$ with $a^2 - b = 1$, then $\frac{1}{x} = a - \sqrt b$.

Why: $(\sqrt a + \sqrt b)(\sqrt a - \sqrt b) = a - b$ removes every root from the denominator.""",
        r"Find $\frac{1}{\sqrt{9}+\sqrt{8}} + \frac{1}{\sqrt{8}+\sqrt{7}} + \dots + \frac{1}{\sqrt{2}+1}$.",
        r"Each term $= \sqrt k - \sqrt{k-1}$; the chain collapses to $\sqrt9 - 1 = 2$.")
    S.pattern("simp-si-p3", r"Root of a surd: $\sqrt{a + 2\sqrt{b}}$", "common",
        r"Expressions like $\sqrt{11+6\sqrt2}$, $\sqrt{9+4\sqrt5}$, or a plus/minus pair of such roots.",
        r"\sqrt{a + 2\sqrt{b}} = \sqrt{x} + \sqrt{y} \text{ where } x+y = a,\ xy = b",
        r"""1. Write the middle term as $2\sqrt b$ ($6\sqrt2 = 2\sqrt{18}$).
2. Find two numbers with sum $a$ and product $b$.
3. Answer $= \sqrt x + \sqrt y$ (or their difference for the minus form).

Why: $(\sqrt x + \sqrt y)^2 = x + y + 2\sqrt{xy}$ matches the given form exactly.""",
        r"Find $\sqrt{11 + 6\sqrt{2}}$.",
        r"$x+y = 11$, $xy = 18$ → 9 and 2 → $3 + \sqrt2$.")
    S.pattern("simp-si-p4", "Comparing surds; surd with its reciprocal", "common",
        "'Which is largest: √3, ⁴√7, ³√5?' or 'if x = 5 + 2√6, find x + 1/x'.",
        r"\sqrt[n]{a} > \sqrt[m]{b} \iff a^{m} > b^{n} \text{ (compare at the LCM of orders)}",
        r"""1. Raise every surd to the LCM of the root orders; compare the results.
2. For $x = a + 2\sqrt b$: check $a^2 - b$; if it is 1 (or a perfect square), $1/x$ is the conjugate.
3. Add or subtract as asked — the roots cancel.

Why: powers remove the roots; conjugates multiply to a whole number.""",
        r"Which is greater: $\sqrt[3]{4}$ or $\sqrt[4]{6}$?",
        r"12th powers: $4^4 = 256$ vs $6^3 = 216$ → $\sqrt[3]{4}$.")

    # 2^(x+3) * 4^(x-1) = 128
    assert 2 ** (2 + 3) * 4 ** (2 - 1) == 128 and 3 * 2 + 1 == 7
    S.q("simp-si-p1", "easy",
        r"If $2^{x+3} \times 4^{x-1} = 128$, what is the value of $x$?",
        ["2", "1", "3", r"$\frac{5}{3}$"], "2",
        r"""$4^{x-1} = (2^2)^{x-1} = 2^{2x-2}$ and $128 = 2^7$.
So $2^{(x+3)+(2x-2)} = 2^7$ → $3x + 1 = 7$ → $x = 2$.""",
        None, 40)
    assert round((32) ** (2 / 5), 6) == 4.0 and round((81) ** (3 / 4), 6) == 27.0 and round((27) ** (2 / 3), 6) == 9.0
    assert 4 * 27 / 9 == 12
    S.q("simp-si-p1", "medium",
        r"Find the value of $(32)^{\frac{2}{5}} \times (81)^{\frac{3}{4}} \div (27)^{\frac{2}{3}}$.",
        ["12", "4", "36", "108"], "12",
        r"""$(32)^{2/5} = (2^5)^{2/5} = 4$; $(81)^{3/4} = (3^4)^{3/4} = 27$; $(27)^{2/3} = 9$.
$4 \times 27 \div 9 = 12$.""",
        None, 45)
    S.q("simp-si-p2", "easy",
        r"The value of $\frac{1}{\sqrt{7} - \sqrt{6}}$ is:",
        [r"$\sqrt{7} + \sqrt{6}$", r"$\sqrt{7} - \sqrt{6}$", r"$\frac{1}{\sqrt{7}} + \frac{1}{\sqrt{6}}$", r"$\frac{\sqrt{7} - \sqrt{6}}{13}$"],
        r"$\sqrt{7} + \sqrt{6}$",
        r"Multiply top and bottom by $\sqrt7 + \sqrt6$: denominator $= 7 - 6 = 1$. Value $= \sqrt7 + \sqrt6$.",
        None, 30)
    v = sum(1 / (math.sqrt(k) + math.sqrt(k - 1)) for k in range(2, 10))
    assert abs(v - 2) < 1e-9
    S.q("simp-si-p2", "hard",
        r"Find the value of $\frac{1}{\sqrt{9}+\sqrt{8}} + \frac{1}{\sqrt{8}+\sqrt{7}} + \dots + \frac{1}{\sqrt{2}+1}$.",
        ["2", "1", "3", "4"], "2",
        r"""Rationalise each term with its conjugate: $\frac{1}{\sqrt{k}+\sqrt{k-1}} = \sqrt{k} - \sqrt{k-1}$.
The sum collapses (telescopes): $(\sqrt9 - \sqrt8) + (\sqrt8 - \sqrt7) + \dots + (\sqrt2 - 1) = \sqrt9 - 1 = 2$.""",
        "Every middle surd appears twice with opposite signs and cancels.", 60)
    S.q("simp-si-p3", "medium",
        r"Find the value of $\sqrt{11 + 6\sqrt{2}}$.",
        [r"$3 + \sqrt{2}$", r"$2 + \sqrt{3}$", r"$\sqrt{2} + \sqrt{3}$", r"$3 - \sqrt{2}$"],
        r"$3 + \sqrt{2}$",
        r"""Write $6\sqrt2 = 2\sqrt{18}$. Need $x + y = 11$, $xy = 18$ → $x, y = 9, 2$.
$\sqrt{11 + 2\sqrt{18}} = \sqrt9 + \sqrt2 = 3 + \sqrt2$. Check: $(3+\sqrt2)^2 = 9 + 2 + 6\sqrt2$ ✓.""",
        None, 45)
    S.q("simp-si-p3", "medium",
        r"Find the value of $\sqrt{9 + 4\sqrt{5}}$.",
        [r"$2 + \sqrt{5}$", r"$\sqrt{5} - 2$", r"$4 + \sqrt{5}$", r"$1 + 2\sqrt{5}$"],
        r"$2 + \sqrt{5}$",
        r"""$4\sqrt5 = 2\sqrt{20}$. Need $x + y = 9$, $xy = 20$ → $x, y = 5, 4$.
Answer $= \sqrt5 + \sqrt4 = \sqrt5 + 2$. Check: $(2+\sqrt5)^2 = 4 + 5 + 4\sqrt5$ ✓.""",
        None, 40)
    pairs = [(r"$\sqrt{3}$", 3 ** 6), (r"$\sqrt[4]{7}$", 7 ** 3), (r"$\sqrt[3]{5}$", 5 ** 4), (r"$\sqrt[6]{25}$", 25 ** 2)]
    vals = [p[1] for p in pairs]
    assert vals == [729, 343, 625, 625] and max(vals) == 729
    S.q("simp-si-p4", "medium",
        r"Which of the following is the largest? $\sqrt{3},\ \sqrt[4]{7},\ \sqrt[3]{5},\ \sqrt[6]{25}$",
        [p[0] for p in pairs], pairs[0][0],
        r"""Raise each to the power 12 (LCM of 2, 3, 4, 6):
$\sqrt3 \to 3^6 = 729$; $\sqrt[4]{7} \to 7^3 = 343$; $\sqrt[3]{5} \to 5^4 = 625$; $\sqrt[6]{25} \to 25^2 = 625$.
Largest base value 729 → $\sqrt3$ is the largest.""",
        "The 6th root of 25 equals 5 to the 1/3 — it ties with ∛5.", 45)
    assert 4 ** 4 > 6 ** 3
    S.q("simp-si-p4", "easy",
        r"Which of the two numbers is greater: $\sqrt[3]{4}$ or $\sqrt[4]{6}$?",
        [r"$\sqrt[3]{4}$", r"$\sqrt[4]{6}$", "Both are equal", "Cannot be compared"], r"$\sqrt[3]{4}$",
        r"""Raise both to the power 12: $(\sqrt[3]{4})^{12} = 4^4 = 256$; $(\sqrt[4]{6})^{12} = 6^3 = 216$.
$256 > 216$, so $\sqrt[3]{4}$ is greater.""",
        None, 30)
    x = 5 + 2 * math.sqrt(6)
    inv = 1 / x
    assert abs(inv - (5 - 2 * math.sqrt(6))) < 1e-9
    S.q("simp-si-p4", "medium",
        r"If $x = 5 + 2\sqrt{6}$, find the value of $x + \frac{1}{x}$.",
        ["10", "12", "8", "5"], "10",
        r"""$\frac{1}{5 + 2\sqrt6} = \frac{5 - 2\sqrt6}{25 - 24} = 5 - 2\sqrt6$.
So $x + \frac{1}{x} = (5 + 2\sqrt6) + (5 - 2\sqrt6) = 10$.""",
        None, 40)
    return S
