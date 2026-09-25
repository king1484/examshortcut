"""Phase-2 deep content for quant/algebra.json — linear-poly + maxmin modules."""
import math
import os
import sys

sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
from fractions import Fraction as F

from _lib import Sub


def build_poly():
    S = Sub("alg-linear-poly")

    S.notes = r"""### Two lines, three outcomes
For $a_1x+b_1y=c_1$ and $a_2x+b_2y=c_2$ compare the ratios:
$$\frac{a_1}{a_2} \ne \frac{b_1}{b_2} \Rightarrow \text{unique solution} \qquad \frac{a_1}{a_2} = \frac{b_1}{b_2} \ne \frac{c_1}{c_2} \Rightarrow \text{no solution (parallel)} \qquad \frac{a_1}{a_2} = \frac{b_1}{b_2} = \frac{c_1}{c_2} \Rightarrow \text{infinitely many (same line)}$$
Find-k questions fix one ratio from the known pair and set it equal to (or apart from) the third: $3x+4y=10$, $6x+ky=20$ → infinitely many needs $\frac36 = \frac4k = \frac{10}{20}$ → $k=8$. No solution needs $\frac36 = \frac{k}{...}$ matched on the first two ratios but NOT on $c$: e.g. $2x+ky=5$, $4x+6y=10$ → $\frac24 = \frac k6 = \frac12$ gives $k=3$ and then $\frac55$-checking $c$: $\frac12 \ne \frac{10}{10}=1$ → indeed no solution at $k=3$ only if the $c$-ratio differs. Always finish the check with the $c$-ratio.

### Area with the axes
A line $ax+by=c$ cuts the axes at $\left(\frac ca, 0\right)$ and $\left(0, \frac cb\right)$:
$$\text{area} = \frac12 \times \frac ca \times \frac cb = \frac{c^2}{2ab}$$
$3x+4y=24$ → intercepts 8 and 6 → area 24. With axes and one more line, find the intersection first, then use the base-height read-off. This little formula answers a surprisingly common CGL question in five seconds.

### Remainder and factor theorems
Remainder theorem: dividing $p(x)$ by $(x-\alpha)$ leaves $p(\alpha)$ — just substitute. Dividing by $(x+1)$? Substitute $x=-1$. Two remainders give two linear equations in the unknown coefficients: $p(x)=x^4-2x^3+3x^2-ax+b$ with remainders 3 and 9 at $x=1$ and $x=-1$ → $p(1)=2-a+b=3$, $p(-1)=6+a+b=9$ → $a=1$, $b=2$.
Factor theorem: $(x-\alpha)$ is a factor $\iff p(\alpha)=0$. "Is a factor" questions are remainder questions with the remainder forced to zero.

### Quadratic roots
For $x^2-px+q=0$ (i.e. $ax^2+bx+c$): $\alpha+\beta = -\frac ba$, $\alpha\beta = \frac ca$. The standard follow-ups:
$$\alpha^2+\beta^2 = (\alpha+\beta)^2-2\alpha\beta \qquad \alpha^3+\beta^3 = (\alpha+\beta)^3-3\alpha\beta(\alpha+\beta) \qquad \frac1\alpha+\frac1\beta = \frac{\alpha+\beta}{\alpha\beta}$$
Roots real & distinct $\iff b^2-4ac>0$; equal $\iff =0$; no real roots $\iff <0$. A "for what $k$" question is just that inequality solved.

### Common traps
- Quoting the parallel-lines condition without checking the $c$-ratio (many "find k" questions hinge on it).
- Using $\frac cb$ as the $x$-intercept (it is the $y$-intercept).
- Substituting the wrong sign into the remainder theorem ($x+3$ → use $-3$).
- Sign slips in $\alpha+\beta = -b/a$ — it is MINUS $b$ over $a$.

### Quick revision
- Ratios decide: unequal → unique; equal-equal-unequal → none; all equal → infinite.
- Area with axes $= \frac{c^2}{2ab}$.
- Remainder $= p(\alpha)$; factor $\iff p(\alpha)=0$.
- $\alpha+\beta = -\frac ba$, $\alpha\beta = \frac ca$; $\alpha^3+\beta^3 = (\alpha+\beta)^3-3\alpha\beta(\alpha+\beta)$.
- Real distinct roots $\iff b^2 > 4ac$.
"""

    S.pattern("alg-p17", "Consistency of a linear pair (find k)", "common",
        "Two linear equations with an unknown $k$; asked whether there are unique / no / infinitely many solutions.",
        r"\frac{a_1}{a_2} \ne \frac{b_1}{b_2}\ (\text{unique}); \quad =\ \&\ \ne\ \frac{c_1}{c_2}\ (\text{none}); \quad =\ =\ (\text{infinite})",
        r"""1. Compute the $a$-ratio and $b$-ratio from the known coefficients.
2. Set them equal (or unequal) as the question demands and solve for $k$.
3. ALWAYS check the $c$-ratio: for "no solution" it must differ, for "infinite" it must match.

Why: two lines coincide, cross once, or never meet — the coefficient ratios tell you which, completely.""",
        "For what value of $k$ does $2x+ky=5$, $4x+6y=12$ have no solution?",
        r"No solution: $\frac{a_1}{a_2}=\frac{b_1}{b_2}\ne\frac{c_1}{c_2}$. $\frac24=\frac k6=\frac12$ → $k=3$, and $\frac{5}{12}\ne\frac12$ — consistent.")
    S.pattern("alg-p18", "Area of the triangle cut by a line from the axes", "common",
        "A line $ax+by=c$ with the coordinate axes bounds a triangle; its area is asked.",
        r"\text{area} = \frac12\cdot\frac ca\cdot\frac cb = \frac{c^2}{2ab}",
        r"""1. $x$-intercept: put $y=0$ → $x = \frac ca$.
2. $y$-intercept: put $x=0$ → $y = \frac cb$.
3. Area $= \frac12 \times$ product of intercepts.

Why: the axes are perpendicular, so the intercepts are exactly the base and height.""",
        "The area of the triangle formed by $3x+4y=24$ and the coordinate axes is:",
        r"Intercepts 8 and 6 → area $= \frac12\times8\times6 = 24$ square units.")
    S.pattern("alg-p19", "Remainder / factor theorem", "very common",
        "A polynomial divided by $(x-\\alpha)$ or $(x+\\alpha)$ — the remainder, an unknown coefficient, or the factor condition is asked.",
        r"p(x) \div (x-\alpha) \Rightarrow \text{remainder} = p(\alpha); \quad (x-\alpha)\ \text{factor} \iff p(\alpha)=0",
        r"""1. Substitute the zero of the divisor: $x-2$ → $x=2$; $x+1$ → $x=-1$.
2. For long divisors like $(x-1)(x+1)$, substitute each root separately and solve the resulting linear system.
3. For factor questions set $p(\alpha)=0$ and solve for the unknown coefficient.

Why: the remainder theorem reduces a whole division to one evaluation.""",
        "When $x^4-2x^3+3x^2-ax+b$ is divided by $(x-1)$ and $(x+1)$ the remainders are 3 and 9. Then $ab$ equals:",
        r"$p(1) = 2-a+b = 3$, $p(-1) = 6+a+b = 9$ → $a=1$, $b=2$ → $ab = 2$. Two substitutions, two linear equations.")
    S.pattern("alg-p20", "Quadratic roots and symmetric functions", "very common",
        r"A quadratic is given (or its $\alpha+\beta$, $\alpha\beta$); expressions in the roots, or the $k$ for a given root nature, are asked.",
        r"\alpha+\beta = -\frac ba, \quad \alpha\beta = \frac ca",
        r"""1. Read off $\alpha+\beta$ and $\alpha\beta$ from the coefficients (mind the minus).
2. Build the asked expression from squares/cubes: $\alpha^2+\beta^2$, $\alpha^3+\beta^3$, $\frac1\alpha+\frac1\beta$.
3. Root-nature questions: solve $b^2-4ac$ compared with 0.

Why: every symmetric rational function of the roots is a function of the two elementary ones.""",
        "If $\\alpha,\\beta$ are the roots of $x^2-3x+1=0$, then $\\alpha^4+\\beta^4$ equals:",
        r"$\alpha+\beta = 3$, $\alpha\beta = 1$ → $\alpha^2+\beta^2 = 7$ → $\alpha^4+\beta^4 = 49-2 = 47$.")

    # ---- practice (alg-linear-poly) ----
    assert F(2, 4) == F(3, 6) and F(5, 12) != F(1, 2)
    S.q("alg-p17", "medium",
        "For what value of $k$ will the system $2x+ky=5$ and $4x+6y=12$ have no solution?",
        ["3", "6", "2", "1.5"], "3",
        r"No solution needs $\frac{a_1}{a_2}=\frac{b_1}{b_2}\ne\frac{c_1}{c_2}$: $\frac24=\frac k6=\frac12$ → $k=3$, and $\frac{5}{12}\ne\frac12$ confirms the lines are distinct.",
        None, 45)
    area = F(8 * 4, 2)
    assert area == 16
    S.q("alg-p18", "easy",
        "What is the area (in square units) of the triangle formed by the line $x+2y=8$ and the coordinate axes?",
        ["16", "32", "8", "24"], "16",
        r"Intercepts: $x = 8$, $y = 4$ → area $= \frac12\times8\times4 = 16$.",
        None, 25)
    v = 8 - 12 + 8 - 5
    assert v == -1
    S.q("alg-p19", "easy",
        "What is the remainder when $x^3-3x^2+4x-5$ is divided by $(x-2)$?",
        ["-1", "1", "-5", "3"], "-1",
        r"$p(2) = 8-12+8-5 = -1$.",
        None, 25)
    S.q("alg-p20", "easy",
        "The roots of the equation $x^2-5x+6=0$ are:",
        ["2 and 3", "1 and 6", "-2 and -3", "-1 and -6"], "2 and 3",
        r"$\alpha+\beta = 5$, $\alpha\beta = 6$ → the roots are 2 and 3.",
        None, 25)
    v = 27 - 3 * 3 * 2
    assert v == 9
    S.q("alg-p20", "medium",
        "If $α$ and $β$ are the roots of $x^2-3x+2=0$, then the value of $α^3+β^3$ is:",
        ["9", "18", "27", "35"], "9",
        r"$\alpha+\beta = 3$, $\alpha\beta = 2$ → $\alpha^3+\beta^3 = 27 - 3\times2\times3 = 9$.",
        None, 35)
    k = 8 - 5
    assert k == 3 and (-1) - 3 + 9 == 5
    S.q("alg-p19", "medium",
        "If the polynomial $x^3+kx+9$ leaves remainder 5 when divided by $(x+1)$, then $k$ equals:",
        ["3", "-3", "5", "2"], "3",
        r"$p(-1) = -1-k+9 = 8-k = 5$ → $k = 3$.",
        None, 35)
    assert F(3, 6) == F(4, 8) == F(10, 20)
    S.q("alg-p17", "medium",
        "For what value of $k$ will the system $3x+4y=10$ and $6x+ky=20$ have infinitely many solutions?",
        ["8", "4", "2", "12"], "8",
        r"$\frac36=\frac4k=\frac{10}{20}=\frac12$ → $k = 8$.",
        None, 35)
    assert F(3 * 4, 2) == 6
    S.q("alg-p18", "medium",
        "The area (in square units) of the triangle formed by the line $4x+3y=12$ and the coordinate axes is:",
        ["6", "12", "3", "24"], "6",
        r"Intercepts 3 and 4 → area $= \frac12\times3\times4 = 6$.",
        None, 30)
    v = 7 ** 2 - 2 * 1
    assert v == 47
    S.q("alg-p20", "hard",
        "If $α$ and $β$ are the roots of $x^2-3x+1=0$, then the value of $α^4+β^4$ is:",
        ["47", "49", "45", "51"], "47",
        r"$\alpha+\beta=3$, $\alpha\beta=1$ → $\alpha^2+\beta^2 = 9-2 = 7$ → $\alpha^4+\beta^4 = 49-2 = 47$.",
        None, 50)
    aa, bb = 1, 2
    p = lambda x: x ** 4 - 2 * x ** 3 + 3 * x ** 2 - aa * x + bb
    assert p(1) == 3 and p(-1) == 9 and aa * bb == 2
    S.q("alg-p19", "hard",
        "When $p(x)=x^4-2x^3+3x^2-ax+b$ is divided by $(x-1)$ the remainder is 3, and when divided by $(x+1)$ the remainder is 9. The value of $ab$ is:",
        ["2", "3", "1", "-2"], "2",
        r"$p(1) = 2-a+b = 3$ → $b-a=1$; $p(-1) = 6+a+b = 9$ → $a+b=3$. Adding: $b=2$, $a=1$ → $ab=2$.",
        None, 50)
    return S


def build_maxmin():
    S = Sub("alg-maxmin")

    S.notes = r"""### AM ≥ GM — the one-line minimum
For positive quantities:
$$\frac{u+v}{2} \ge \sqrt{uv} \quad\text{with equality iff } u=v$$
Any expression $ax+\frac bx$ (for $x>0$) has minimum $2\sqrt{ab}$ at $x=\sqrt{b/a}$: $x+\frac4x \ge 2\sqrt4 = 4$; $4x+\frac9x \ge 2\sqrt{36} = 12$ at $x = \frac32$. The same idea handles substitution shapes: $(x-1)^2+\frac9{(x-1)^2} \ge 2\sqrt9 = 6$, since $(x-1)^2$ is positive for $x\ne1$. Three-term version: $x^2+\frac{250}x = x^2+\frac{125}x+\frac{125}x \ge 3\sqrt[3]{125\times125} = 75$ — split the extra term so all three pieces multiply to a constant.

### Completing the square — the quadratic extreme
$$ax^2+bx+c = a\left(x+\frac b{2a}\right)^2 + \left(c-\frac{b^2}{4a}\right)$$
$a>0$: the square is $\ge0$, so the minimum is $c-\frac{b^2}{4a}$ at $x=-\frac b{2a}$. $x^2+4x+5 = (x+2)^2+1 \ge 1$. $a<0$: maximum at the same vertex: $5+12x-3x^2 = -3(x-2)^2+17 \le 17$. Remember the two line-readings: least value for upward parabolas, greatest for downward ones — and check which one the question wants.

### Fixed sum / fixed product
- Fixed sum, product maximised: equal split. $x+y = 20$ → $xy \le 100$ at $x=y=10$.
- Fixed product, sum minimised: equal factors. $xy = 36$ → $x+y \ge 12$ at $x=y=6$.
Both are AM ≥ GM in disguise ($\frac{x+y}{2}\ge\sqrt{xy}$), and both are asked verbatim.

### Positive definite and the discriminant
$ax^2+bx+c>0$ for ALL real $x$ needs $a>0$ AND $b^2-4ac<0$: $4x^2-kx+25>0$ always → $k^2<400$ → largest integer $k = 19$. Root-nature reads the same table: real & distinct $\iff b^2>4ac$, equal $\iff b^2=4ac$, none real $\iff b^2<4ac$. For $x^2+kx+16$ to have real distinct roots, $k^2>64$ → $|k|>8$.

### Chained shapes
A hard stem often folds one tool inside another: the least value of $(x+\frac1x)^2-4(x+\frac1x)+5$ — set $t = x+\frac1x \ge 2$ first (AM ≥ GM), then $(t-2)^2+1 \ge 1$ (vertex). Two moves, each a standard one.

### Common traps
- Applying AM ≥ GM to $x+\frac4x$ without checking $x>0$ (for $x<0$ the expression is negative).
- Forgetting the vertex $x$-value when the question asks WHERE the minimum occurs, not just its value.
- Using $c-\frac{b^2}{4a}$ for a downward parabola as a minimum — that shape has no minimum.
- Missing that equality in AM ≥ GM needs the two pieces EQUAL, which pins $x$.

### Quick revision
- $ax+\frac bx \ge 2\sqrt{ab}$ for $x>0$; equality at $x=\sqrt{b/a}$.
- Vertex: $x=-\frac b{2a}$; extreme value $c-\frac{b^2}{4a}$ (min if $a>0$, max if $a<0$).
- Fixed sum → max product at equal split; fixed product → min sum at equal factors.
- Always positive: $a>0$ and $b^2<4ac$.
- Substitute $t = x+\frac1x \ge 2$ before completing the square.
"""

    S.pattern("alg-p21", "AM-GM least value of $ax+\\frac bx$", "very common",
        "'Least value of $x+\\frac4x$', '$4x+\\frac9x$', or a substitution shape like $(x-1)^2+\\frac9{(x-1)^2}$.",
        r"ax+\frac bx \ge 2\sqrt{ab}",
        r"""1. Confirm both pieces are positive for the allowed $x$.
2. Least value $= 2\sqrt{ab}$, attained where the two pieces are equal.
3. For substitution shapes, name the substituted square $t>0$ and reuse the same bound.

Why: AM ≥ GM is exact here because the two pieces multiply to the constant $ab$.""",
        "The least value of $(x-1)^2+\\dfrac9{(x-1)^2}$ (for $x\\ne1$) is:",
        r"AM ≥ GM on the two positive pieces: $\ge 2\sqrt9 = 6$, at $(x-1)^2 = 3$.")
    S.pattern("alg-p22", "Quadratic extreme by completing the square", "very common",
        "'Least value of $x^2+4x+5$' or 'greatest value of $5+12x-3x^2$' — a quadratic with both linear and constant terms.",
        r"ax^2+bx+c = a\left(x+\frac b{2a}\right)^2 + c-\frac{b^2}{4a}",
        r"""1. Vertex at $x = -\frac b{2a}$; extreme value $c-\frac{b^2}{4a}$.
2. $a>0$ → least value asked; $a<0$ → greatest value.
3. Complete the square mentally to double-check.

Why: the squared term can only push the value one way — away from the vertex.""",
        "The greatest value of $7+4x-x^2$ is:",
        r"$-(x-2)^2+11 \le 11$, attained at $x=2$. Greatest value $= 11$.")
    S.pattern("alg-p23", "Fixed sum / fixed product", "common",
        "Two positive numbers with a fixed sum (maximise the product) or fixed product (minimise the sum).",
        r"x+y=s \Rightarrow xy \le \frac{s^2}{4}; \qquad xy=p \Rightarrow x+y \ge 2\sqrt p",
        r"""1. Equal split is optimal in both directions — that is AM ≥ GM with equality.
2. Fixed sum $s$: max product $= \frac{s^2}{4}$ at $x=y=\frac s2$.
3. Fixed product $p$: min sum $= 2\sqrt p$ at $x=y=\sqrt p$.

Why: for a fixed sum the product is a downward parabola peaking at the midpoint (and vice versa).""",
        "The least value of $x+y$ for positive $x,y$ with $xy=36$ is:",
        r"$x+y \ge 2\sqrt{36} = 12$, at $x=y=6$.")
    S.pattern("alg-p24", "Always-positive / root nature via discriminant", "common",
        "'$4x^2-kx+25>0$ for all $x$' or 'find $k$ so that the roots are real and distinct' — a discriminant condition in disguise.",
        r"a>0 \text{ and } b^2-4ac<0 \Rightarrow \text{positive for all } x",
        r"""1. Translate the requirement: always positive = upward opening + no real roots.
2. Write $b^2 - 4ac$ and impose the right inequality.
3. Solve for $k$; if an integer is asked, take the floor/ceiling of the boundary.

Why: a positive quadratic never touches zero exactly when its discriminant is negative.""",
        "The largest integer $k$ for which $4x^2-kx+25>0$ for all real $x$ is:",
        r"Need $k^2 < 4\times4\times25 = 400$ → $|k| < 20$ → $k_{\max} = 19$.")

    # ---- practice (alg-maxmin) ----
    assert 2 * math.sqrt(4) == 4
    S.q("alg-p21", "easy",
        "For $x>0$, the least value of $x+\\dfrac4x$ is:",
        ["4", "2", "8", "1"], "4",
        r"$x+\frac4x \ge 2\sqrt{4} = 4$, at $x = 2$.",
        None, 25)
    assert 2 * math.sqrt(36) == 12
    S.q("alg-p21", "easy",
        "For $x>0$, the least value of $4x+\\dfrac9x$ is:",
        ["12", "6", "36", "13"], "12",
        r"$2\sqrt{4\times9} = 2\times6 = 12$, at $x = \frac32$.",
        None, 25)
    v = 5 - F(16, 4)
    assert v == 1
    S.q("alg-p22", "easy",
        "The least value of $x^2+4x+5$ is:",
        ["1", "4", "5", "0"], "1",
        r"$(x+2)^2+1 \ge 1$, attained at $x=-2$.",
        None, 25)
    assert F(20, 2) ** 2 == 100
    S.q("alg-p23", "easy",
        "If $x$ and $y$ are positive numbers with $x+y=20$, the maximum value of $xy$ is:",
        ["100", "96", "99", "64"], "100",
        r"Product peaks at the equal split: $10\times10 = 100$.",
        None, 25)
    v = 7 + 4 * 2 - 4
    assert v == 11
    S.q("alg-p22", "medium",
        "The greatest value of $7+4x-x^2$ is:",
        ["11", "7", "8", "12"], "11",
        r"$-(x-2)^2+11$ → greatest value 11 at $x=2$.",
        None, 35)
    assert 2 * math.sqrt(9) == 6
    S.q("alg-p21", "medium",
        "The least value of $(x-1)^2+\\dfrac9{(x-1)^2}$ (for $x \\ne 1$) is:",
        ["6", "3", "9", "5"], "6",
        r"Both pieces are positive; AM ≥ GM gives $2\sqrt9 = 6$, at $(x-1)^2 = 3$.",
        None, 35)
    assert 2 * math.sqrt(36) == 12
    S.q("alg-p23", "medium",
        "If $xy=36$ for positive $x,y$, the least value of $x+y$ is:",
        ["12", "6", "36", "13"], "12",
        r"$x+y \ge 2\sqrt{36} = 12$ at $x=y=6$.",
        None, 30)
    assert 19 ** 2 < 400 <= 20 ** 2
    S.q("alg-p24", "medium",
        "The largest integer value of $k$ for which $4x^2-kx+25>0$ for all real $x$ is:",
        ["19", "20", "21", "18"], "19",
        r"Need $k^2 < 400$ → $|k|<20$ → largest integer $k = 19$.",
        None, 45)
    v = 2 * 4 - 16 + 9
    assert v == 1
    S.q("alg-p22", "medium",
        "The least value of $2x^2-8x+9$ is:",
        ["1", "9", "2", "-1"], "1",
        r"$2(x-2)^2+1 \ge 1$, attained at $x=2$.",
        None, 35)
    t = F(2)
    assert t * t - 4 * t + 5 == 1
    S.q("alg-p21", "hard",
        "For $x>0$, the least value of $\\left(x+\\dfrac1x\\right)^2-4\\left(x+\\dfrac1x\\right)+5$ is:",
        ["1", "0", "2", "5"], "1",
        r"Let $t = x+\frac1x \ge 2$ (AM ≥ GM). Then $(t-2)^2+1$, increasing for $t\ge2$ → least $= 1$ at $t=2$ (i.e. $x=1$).",
        None, 55)
    v = 25 + 250 / F(5)
    assert v == 75 and 125 * 125 == 5 ** 6
    S.q("alg-p23", "hard",
        "For $x>0$, the least value of $x^2+\\dfrac{250}{x}$ is:",
        ["75", "50", "100", "25"], "75",
        r"""Split $x^2+\frac{125}x+\frac{125}x \ge 3\sqrt[3]{125\times125} = 3\times25 = 75$,
equal when $x^2 = \frac{125}x$, i.e. $x=5$ → $25+50 = 75$.""",
        None, 60)
    assert 10 ** 2 > 64 and 8 ** 2 == 64 and (-8) ** 2 == 64 and 0 ** 2 < 64
    S.q("alg-p24", "medium",
        "For which value of $k$ does the equation $x^2+kx+16=0$ have real and distinct roots?",
        ["10", "8", "-8", "0"], "10",
        r"Real & distinct needs $k^2 > 64$ → $|k|>8$. Only $k=10$ qualifies ($8$ and $-8$ give equal roots, $0$ gives complex).",
        None, 40)
    return S
