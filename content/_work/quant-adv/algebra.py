import sympy as sp
from qa_common import Q, F, T, S, P, U, write_topic

x, y, z, a, b, c, k = sp.symbols("x y z a b c k")
sq = sp.sqrt

# ---------------------------------------------------------------- trick-example checks
assert 5**3 + 2**3 == 7**3 - 3 * 10 * 7 == 133
assert sp.nsimplify((sp.Rational(83, 10)**3 - sp.Rational(37, 10)**3) / (sp.Rational(83, 10)**2 + sp.Rational(83, 10) * sp.Rational(37, 10) + sp.Rational(37, 10)**2)) == sp.Rational(46, 10)
assert sp.expand((a + b)**3 - (a - b)**3 - 6 * a**2 * b) == 2 * b**3
assert sp.expand((x - 2)**2 + (y + 3)**2 - (x**2 + y**2 - 4 * x + 6 * y + 13)) == 0
# x + 1/x = 1 -> x^3 = -1
r = sp.solve(x**2 - x + 1, x)[0]
assert sp.simplify(sum(r**p for p in (30, 24, 18, 12, 6, 0))) == 6
r = sp.solve(x**2 - 4 * x + 1, x)[0]
assert [sp.simplify(r**n + r**-n) for n in (2, 4, 3)] == [14, 194, 52]
r = sp.solve(3 * x**2 - 7 * x + 3, x)[0]
assert sp.simplify(r**2 + r**-2) == sp.Rational(31, 9)
r = sp.solve(2 * x + 1 / (3 * x) - 5, x)[0]
assert sp.simplify(4 * r**2 + 1 / (9 * r**2)) == sp.Rational(71, 3)
assert sp.simplify(((x - y)**3 + (y - z)**3 + (z - x)**3) / (9 * (x - y) * (y - z) * (z - x))) == sp.Rational(1, 3)
assert 25**3 + 24**3 + 23**3 - 3 * 25 * 24 * 23 == 216
assert sp.Rational(1, -2) + sp.Rational(1, -2) + 4 == 3
v = sq(5) + 2
assert sp.simplify(v**2 + v**-2) == 18
assert sp.simplify((2 + sq(3))**2 - (7 + 4 * sq(3))) == 0
assert sp.simplify((3 - sq(5))**2 - (14 - 6 * sq(5))) == 0
assert (sq(12) - sq(11)).evalf() < (sq(11) - sq(10)).evalf()
assert sp.simplify(sum(1 / (sq(n) + sq(n + 1)) for n in range(1, 9))) == 2
assert sp.Rational(1, 2) * 4 * 10 == 20
f = 2 * x**3 - 3 * x**2 + 4 * x - 5
assert f.subs(x, 2) == 7
assert (2 * 2 + 3 * 3, 3 * 2 - 3) == (13, 3)
assert sp.minimum(x + 16 / x, x, sp.Interval.open(0, sp.oo)) == 8
assert sp.minimum(x**2 - 8 * x + 21, x) == 5
assert sp.maximum(x * (12 - 2 * x) / 3, x, sp.Interval(0, 6)) == 6

# ---------------------------------------------------------------- subtopics
subtopics = [
S("alg-identities", "Basic algebraic identities",
r"""
An **identity** is true for every value of the variables, so it can be used both ways: to expand and to
compress. In CGL, identities are tested in three ways:

1. **Given $a+b$ (or $a-b$) and $ab$, find $a^2+b^2$, $a^3\pm b^3$ or $a^4+b^4$.** Never solve for $a$ and $b$ separately — build the answer from the given pieces.
2. **Big-number simplification.** Expressions such as $\frac{p^3+q^3}{p^2-pq+q^2}$ with decimals are just $p+q$ in disguise.
3. **Sum of squares equal to zero.** If $(\ldots)^2+(\ldots)^2+(\ldots)^2=0$ over real numbers, each bracket is zero. Questions hide this as $x^2+y^2-4x+6y+13=0$; complete the squares to expose it.
""",
[
F("Square of sum / difference", r"(a\pm b)^2=a^2\pm 2ab+b^2"),
F("Difference of squares", r"a^2-b^2=(a+b)(a-b)"),
F("Sum & difference of the two squares", r"(a+b)^2+(a-b)^2=2(a^2+b^2),\quad (a+b)^2-(a-b)^2=4ab"),
F("Cube of sum", r"(a+b)^3=a^3+b^3+3ab(a+b)"),
F("Cube of difference", r"(a-b)^3=a^3-b^3-3ab(a-b)"),
F("Sum of cubes", r"a^3+b^3=(a+b)(a^2-ab+b^2)=(a+b)^3-3ab(a+b)"),
F("Difference of cubes", r"a^3-b^3=(a-b)(a^2+ab+b^2)=(a-b)^3+3ab(a-b)"),
F("Square of trinomial", r"(a+b+c)^2=a^2+b^2+c^2+2(ab+bc+ca)"),
F("Fourth-power factorisation", r"a^4+a^2b^2+b^4=(a^2+ab+b^2)(a^2-ab+b^2)"),
F("Fourth powers from sum and product", r"a^4+b^4=(a^2+b^2)^2-2a^2b^2"),
],
[
T("Build higher powers from $a+b$ and $ab$",
r"""Memorise the chain: $a^2+b^2=(a+b)^2-2ab$, then $a^3+b^3=(a+b)^3-3ab(a+b)$. For differences use
$(a-b)^2=(a+b)^2-4ab$. No need to find $a$ and $b$.""",
r"If $a+b=7$ and $ab=10$, find $a^3+b^3$.",
r"$a^3+b^3=(a+b)^3-3ab(a+b)=343-3(10)(7)=343-210=133$. (Check: $a=5, b=2$ gives $125+8=133$.)"),
T("Recognise the identity inside decimals",
r"""$\frac{p^3+q^3}{p^2-pq+q^2}=p+q$ and $\frac{p^3-q^3}{p^2+pq+q^2}=p-q$. If the denominator's middle sign is
**opposite** to the numerator's sign, the identity fits.""",
r"Simplify $\dfrac{8.3^3-3.7^3}{8.3^2+8.3\times 3.7+3.7^2}$.",
r"It is $\frac{p^3-q^3}{p^2+pq+q^2}$ with $p=8.3,\ q=3.7$, so the value is $p-q=4.6$."),
T("Value-putting for expression options",
r"""When options are algebraic expressions, substitute small numbers (e.g. $a=1, b=1$ or $a=2, b=1$) in the
question and in each option. Test a second pair if two options tie. Avoid values that make denominators zero.""",
r"$(a+b)^3-(a-b)^3-6a^2b$ equals: (a) $2b^3$ (b) $6ab^2$ (c) $2a^3$ (d) $0$",
r"Put $a=1,b=1$: $8-0-6=2$. Options give (a) 2, (b) 6, (c) 2, (d) 0. Tie between (a) and (c); put $a=2,b=1$: $27-1-24=2$; (a) gives 2, (c) gives 16. Answer $2b^3$."),
T("Complete the squares when an equation equals zero",
r"""Group $x$-terms and $y$-terms, complete each square, and check that the leftover constants cancel.
Then each square must be zero.""",
r"If $x^2+y^2-4x+6y+13=0$, find $x$ and $y$.",
r"$(x^2-4x+4)+(y^2+6y+9)=0\Rightarrow (x-2)^2+(y+3)^2=0$, so $x=2,\ y=-3$."),
],
[
"Writing $(a+b)^2=a^2+b^2$ — the $2ab$ term is the most common loss of marks.",
"Using $a^3-b^3=(a-b)^3-3ab(a-b)$; the correct sign is **plus**: $(a-b)^3+3ab(a-b)$.",
"Value-putting with $a=b$ or with zero: many options collapse to the same number. Always use two different non-zero values.",
"In the decimal identity, checking only the numerator: the denominator's middle sign decides which identity applies.",
]),

S("alg-reciprocal", r"$x+\frac{1}{x}$ type expressions",
r"""
If $x+\frac1x=k$ is known, every expression of the form $x^n+\frac{1}{x^n}$ can be built from $k$ without solving
for $x$. The same works for $x-\frac1x$ and for mixed forms like $2x+\frac{1}{3x}$.

**How it is disguised in CGL:**
- a quadratic like $x^2-4x+1=0$ (divide by $x$: $x+\frac1x=4$);
- a surd like $x=2+\sqrt3$ (then $\frac1x=2-\sqrt3$);
- a special value: $x+\frac1x=1,\ -1,\ \sqrt3,\ \sqrt2$ gives cyclic powers of $x$.
""",
[
F("Square", r"x^2+\frac{1}{x^2}=\left(x+\frac1x\right)^2-2=\left(x-\frac1x\right)^2+2"),
F("Cube (sum)", r"x^3+\frac{1}{x^3}=\left(x+\frac1x\right)^3-3\left(x+\frac1x\right)", "if $x+\\frac1x=k$ then it is $k^3-3k$"),
F("Cube (difference)", r"x^3-\frac{1}{x^3}=\left(x-\frac1x\right)^3+3\left(x-\frac1x\right)"),
F("Fourth power", r"x^4+\frac{1}{x^4}=\left(x^2+\frac{1}{x^2}\right)^2-2"),
F("Fifth power", r"x^5+\frac{1}{x^5}=\left(x^2+\frac{1}{x^2}\right)\left(x^3+\frac{1}{x^3}\right)-\left(x+\frac1x\right)"),
F("Link between sum and difference", r"\left(x+\frac1x\right)^2-\left(x-\frac1x\right)^2=4"),
F("Quadratic to reciprocal form", r"ax^2-bx+a=0\ \Rightarrow\ x+\frac1x=\frac ba"),
F("Mixed form", r"\left(px+\frac{1}{qx}\right)^2=p^2x^2+\frac{1}{q^2x^2}+\frac{2p}{q}"),
],
[
T("The ladder",
r"""From $k=x+\frac1x$: $x^2+\frac{1}{x^2}=k^2-2$, $x^4+\frac{1}{x^4}=(k^2-2)^2-2$, $x^8+\frac{1}{x^8}=\ldots$ — keep
squaring and subtracting 2. For the cube use $k^3-3k$.""",
r"If $x+\frac1x=4$, find $x^2+\frac{1}{x^2}$, $x^4+\frac{1}{x^4}$ and $x^3+\frac{1}{x^3}$.",
r"$16-2=14$; $14^2-2=194$; $4^3-3(4)=64-12=52$."),
T("Special values give cyclic powers",
r"""
| If $x+\frac1x=$ | Then |
|---|---|
| $2$ | $x=1$ |
| $-2$ | $x=-1$ |
| $1$ | $x^3=-1$ (so $x^6=1$) |
| $-1$ | $x^3=1$ |
| $\sqrt3$ | $x^6=-1$ (so $x^{12}=1$) |
| $\sqrt2$ | $x^4=-1$ (so $x^8=1$) |

Reduce every exponent using the cycle.""",
r"If $x+\frac1x=1$, find $x^{30}+x^{24}+x^{18}+x^{12}+x^6+1$.",
r"$x+\frac1x=1\Rightarrow x^2-x+1=0\Rightarrow x^3=-1\Rightarrow x^6=1$. Every term is a power of $x^6$, so each equals 1. Sum $=6$."),
T("Divide the quadratic by $x$",
r"""$ax^2-bx+a=0$ (equal first and last coefficients) means $x+\frac1x=\frac ba$. Spot equal end coefficients instantly.""",
r"If $3x^2-7x+3=0$, find $x^2+\frac{1}{x^2}$.",
r"Divide by $3x$: $x+\frac1x=\frac73$. Then $x^2+\frac1{x^2}=\frac{49}{9}-2=\frac{31}{9}$."),
T(r"Mixed form $px+\frac{1}{qx}$",
r"""Squaring gives a middle term $2\cdot px\cdot\frac{1}{qx}=\frac{2p}{q}$, not 2.""",
r"If $2x+\frac{1}{3x}=5$, find $4x^2+\frac{1}{9x^2}$.",
r"Square: $4x^2+\frac{1}{9x^2}+2\cdot 2x\cdot\frac{1}{3x}=25\Rightarrow 4x^2+\frac{1}{9x^2}=25-\frac43=\frac{71}{3}$."),
],
[
"Subtracting 2 instead of adding 2 when going from $x-\\frac1x$ to $x^2+\\frac{1}{x^2}$.",
"Writing $x^3+\\frac{1}{x^3}=k^3-3$ instead of $k^3-3k$.",
"Taking only the positive root of $\\left(x-\\frac1x\\right)^2$ when no condition like $x>1$ is given — check the options.",
"For $2x+\\frac{1}{3x}$ type, using a middle term of 2 instead of $\\frac{2p}{q}$.",
]),

S("alg-three-var", r"$a^3+b^3+c^3-3abc$ and conditional identities",
r"""
The three-variable cube identity is a CGL favourite because it has two useful forms and a powerful special case.

- If $a+b+c=0$, then $a^3+b^3+c^3=3abc$. Questions hide the zero sum, e.g. $(x-y)+(y-z)+(z-x)=0$.
- If $a^2+b^2+c^2=ab+bc+ca$, then $(a-b)^2+(b-c)^2+(c-a)^2=0$, so $a=b=c$.
- For numbers that are close together (like 25, 24, 23), use the half-sum-of-squared-differences form.
""",
[
F("Main identity", r"a^3+b^3+c^3-3abc=(a+b+c)(a^2+b^2+c^2-ab-bc-ca)"),
F("Half form", r"a^3+b^3+c^3-3abc=\tfrac12(a+b+c)\left[(a-b)^2+(b-c)^2+(c-a)^2\right]"),
F("Zero-sum case", r"a+b+c=0\ \Rightarrow\ a^3+b^3+c^3=3abc"),
F("Equal-variables case", r"a^2+b^2+c^2=ab+bc+ca\ \Rightarrow\ a=b=c"),
F("Pairwise products", r"ab+bc+ca=\frac{(a+b+c)^2-(a^2+b^2+c^2)}{2}"),
F("Cyclic differences", r"(a-b)^3+(b-c)^3+(c-a)^3=3(a-b)(b-c)(c-a)"),
],
[
T("Hunt for a hidden zero sum",
r"""$(x-y)+(y-z)+(z-x)=0$ always, so the sum of their cubes is $3(x-y)(y-z)(z-x)$. Similarly
$(a^2-b^2)+(b^2-c^2)+(c^2-a^2)=0$.""",
r"Find $\dfrac{(x-y)^3+(y-z)^3+(z-x)^3}{9(x-y)(y-z)(z-x)}$.",
r"Numerator $=3(x-y)(y-z)(z-x)$, so the value is $\frac{3}{9}=\frac13$."),
T("Close numbers: use the half form",
r"""When $a,b,c$ differ by small amounts, $(a-b)^2+(b-c)^2+(c-a)^2$ is tiny and easy to compute.""",
r"Find $25^3+24^3+23^3-3\times25\times24\times23$.",
r"$\tfrac12(72)\left[1^2+1^2+2^2\right]=36\times6=216$."),
T("Value-putting under a condition",
r"""If a condition like $a+b+c=0$ is given, pick numbers that satisfy it (e.g. $1,1,-2$) and evaluate.""",
r"If $a+b+c=0$, find $\dfrac{a^2}{bc}+\dfrac{b^2}{ca}+\dfrac{c^2}{ab}$.",
r"Put $a=1,b=1,c=-2$: $\frac{1}{-2}+\frac{1}{-2}+\frac{4}{1}=3$. (Algebraically it is $\frac{a^3+b^3+c^3}{abc}=\frac{3abc}{abc}=3$.)"),
],
[
"Using $a^3+b^3+c^3=3abc$ without first checking that $a+b+c=0$.",
"Dropping the $\\tfrac12$ in the half form, which doubles the answer.",
"Sign slips with negatives: for $a=11,b=-5,c=-6$, $3abc=3(11)(-5)(-6)=+990$.",
]),

S("alg-surds", "Surds: rationalisation and square roots of surds",
r"""
A **surd** is an irrational root like $\sqrt3$. CGL asks you to rationalise denominators, simplify nested
roots such as $\sqrt{7+4\sqrt3}$, compare surds, and — most often — use a conjugate pair whose product is 1.

**Conjugate pairs with product 1:** $(2+\sqrt3)(2-\sqrt3)=1$, $(3+2\sqrt2)(3-2\sqrt2)=1$, $(\sqrt5+2)(\sqrt5-2)=1$,
$(\sqrt2+1)(\sqrt2-1)=1$. So if $x=2+\sqrt3$, then $\frac1x=2-\sqrt3$ and $x+\frac1x=4$ — this links surds to the
$x+\frac1x$ ladder.
""",
[
F("Rationalising", r"\frac{1}{\sqrt a+\sqrt b}=\frac{\sqrt a-\sqrt b}{a-b}"),
F("Conjugate product", r"(\sqrt a+\sqrt b)(\sqrt a-\sqrt b)=a-b"),
F("Square root of a surd", r"\sqrt{a+2\sqrt b}=\sqrt m+\sqrt n,\ \text{where } m+n=a,\ mn=b"),
F("Square root (minus)", r"\sqrt{a-2\sqrt b}=\sqrt m-\sqrt n\ \ (m>n)"),
F("Product-1 pair", r"x=p+\sqrt q,\ p^2-q=1\ \Rightarrow\ \frac1x=p-\sqrt q,\ x+\frac1x=2p"),
F("Telescoping sum", r"\sum_{n=1}^{N-1}\frac{1}{\sqrt n+\sqrt{n+1}}=\sqrt N-1"),
],
[
T("Spot the product-1 conjugate",
r"""If $x=p+\sqrt q$ and $p^2-q=1$, write $\frac1x=p-\sqrt q$ at once. Then use $x+\frac1x=2p$ or
$x-\frac1x=2\sqrt q$ and the reciprocal ladder.""",
r"If $x=\sqrt5+2$, find $x^2+\frac{1}{x^2}$.",
r"$\frac1x=\sqrt5-2$, so $x-\frac1x=4$. Then $x^2+\frac1{x^2}=4^2+2=18$."),
T(r"Denest $\sqrt{a\pm2\sqrt b}$ by sum-product",
r"""Make the coefficient of the inner root 2 (e.g. $4\sqrt3=2\sqrt{12}$), then find two numbers with sum $a$ and
product $b$.""",
r"Simplify $\sqrt{14-6\sqrt5}$.",
r"$6\sqrt5=2\sqrt{45}$. Numbers with sum 14 and product 45: 9 and 5. So $\sqrt{14-6\sqrt5}=\sqrt9-\sqrt5=3-\sqrt5$."),
T("Compare differences of roots",
r"""$\sqrt a-\sqrt b=\frac{a-b}{\sqrt a+\sqrt b}$. With the same $a-b$, the pair with the **larger** roots gives the **smaller** difference.""",
r"Which is greater: $\sqrt{12}-\sqrt{11}$ or $\sqrt{11}-\sqrt{10}$?",
r"Both numerators are 1; $\sqrt{12}+\sqrt{11}>\sqrt{11}+\sqrt{10}$, so $\sqrt{11}-\sqrt{10}$ is greater."),
T("Telescoping rationalisation",
r"""Each $\frac{1}{\sqrt n+\sqrt{n+1}}=\sqrt{n+1}-\sqrt n$; the middle terms cancel, leaving last minus first.""",
r"Find $\frac{1}{\sqrt1+\sqrt2}+\frac{1}{\sqrt2+\sqrt3}+\cdots+\frac{1}{\sqrt8+\sqrt9}$.",
r"$=(\sqrt2-1)+(\sqrt3-\sqrt2)+\cdots+(\sqrt9-\sqrt8)=\sqrt9-1=2$."),
],
[
"Writing $\\sqrt a+\\sqrt b=\\sqrt{a+b}$.",
"Denesting without first making the inner coefficient 2 (use $4\\sqrt3=2\\sqrt{12}$).",
"For $\\sqrt{a-2\\sqrt b}$, writing the smaller root first and getting a negative value.",
]),

S("alg-linear-poly", "Linear equations, graphs and polynomials",
r"""
**Pair of linear equations** $a_1x+b_1y=c_1$, $a_2x+b_2y=c_2$ represent two lines. Compare the ratios of
coefficients to decide the number of solutions.

**Graphs:** the line $ax+by=c$ cuts the $x$-axis at $\frac ca$ and the $y$-axis at $\frac cb$. With the axes it
forms a right triangle — its area is a common one-liner.

**Polynomials:** the remainder when $f(x)$ is divided by $x-a$ is $f(a)$ (remainder theorem); if $f(a)=0$,
then $x-a$ is a factor (factor theorem). For a quadratic $ax^2+bx+c$, sum of roots $=-\frac ba$ and
product $=\frac ca$.
""",
[
F("Unique solution", r"\frac{a_1}{a_2}\neq\frac{b_1}{b_2}", "lines intersect"),
F("No solution", r"\frac{a_1}{a_2}=\frac{b_1}{b_2}\neq\frac{c_1}{c_2}", "parallel lines"),
F("Infinitely many solutions", r"\frac{a_1}{a_2}=\frac{b_1}{b_2}=\frac{c_1}{c_2}", "coincident lines"),
F("Intercept form", r"\frac xp+\frac yq=1"),
F("Area with the axes", r"\text{Area}=\frac12\cdot\left|\frac ca\right|\cdot\left|\frac cb\right|=\frac{c^2}{2|ab|}"),
F("Slope of ax+by+c=0", r"m=-\frac ab"),
F("Remainder theorem", r"f(x)\div(x-a)\Rightarrow R=f(a);\quad f(x)\div(px-q)\Rightarrow R=f\!\left(\tfrac qp\right)"),
F("Roots of a quadratic", r"\alpha+\beta=-\frac ba,\quad \alpha\beta=\frac ca"),
],
[
T("Area with axes from intercepts",
r"""Put $y=0$ for the $x$-intercept and $x=0$ for the $y$-intercept, then area $=\frac12\times|p|\times|q|$.""",
r"Find the area of the triangle formed by $5x-2y=20$ and the coordinate axes.",
r"Intercepts: $x=4$ and $y=-10$. Area $=\frac12\times4\times10=20$ sq units."),
T("Remainder = put the zero of the divisor",
r"""No long division. For divisor $x-2$, put $x=2$; for $2x+1$, put $x=-\frac12$.""",
r"Find the remainder when $2x^3-3x^2+4x-5$ is divided by $x-2$.",
r"$f(2)=16-12+8-5=7$."),
T("Intersection point: test the options",
r"""For 'the lines meet at' questions, substitute each option into both equations — usually faster than solving.""",
r"Where do $2x+3y=13$ and $3x-y=3$ intersect? (a) $(2,3)$ (b) $(3,2)$ (c) $(1,0)$ (d) $(5,1)$",
r"$(2,3)$: $4+9=13$ ✓ and $6-3=3$ ✓. Answer (a)."),
],
[
"Taking a negative intercept as negative area — use absolute values.",
"Mixing up the 'no solution' and 'infinitely many' conditions — the constant-term ratio decides.",
"For divisor $2x-1$ putting $x=1$ or $x=-\\frac12$ instead of $x=\\frac12$.",
]),

S("alg-maxmin", "Maxima and minima (AM ≥ GM, quadratics)",
r"""
Two tools cover almost every CGL max–min question:

1. **AM ≥ GM** for positive quantities: $\frac{a+b}{2}\ge\sqrt{ab}$, equality when $a=b$. So $ax+\frac bx$
   ($x>0$) is smallest when the two terms are equal, and the minimum is $2\sqrt{ab}$.
2. **Completing the square / vertex** for quadratics: $ax^2+bx+c$ has its turning point at $x=-\frac{b}{2a}$.
   If $a>0$ this is a minimum, if $a<0$ a maximum.
""",
[
F("AM–GM", r"\frac{a+b}{2}\ge\sqrt{ab}\quad(a,b>0)"),
F("Min of ax + b/x", r"ax+\frac bx\ge 2\sqrt{ab},\ \text{at } x=\sqrt{\tfrac ba}"),
F("Vertex of a quadratic", r"x=-\frac{b}{2a},\quad \text{extreme value}=\frac{4ac-b^2}{4a}"),
F("Fixed sum", r"x+y=S\ \Rightarrow\ xy\le\frac{S^2}{4}"),
F("Fixed product", r"xy=P\ \Rightarrow\ x+y\ge 2\sqrt P"),
],
[
T(r"Equal-terms rule for $ax+\frac bx$",
r"""Minimum $=2\sqrt{ab}$. No calculus needed.""",
r"Find the minimum value of $x+\frac{16}{x}$ for $x>0$.",
r"$2\sqrt{1\times16}=8$ (at $x=4$)."),
T("Complete the square",
r"""Write the quadratic as $(x-h)^2+m$; the minimum is $m$. For a negative leading coefficient write $M-(x-h)^2$; the maximum is $M$.""",
r"Find the minimum value of $x^2-8x+21$.",
r"$x^2-8x+21=(x-4)^2+5$, so the minimum is $5$ (at $x=4$)."),
T("Fixed weighted sum → equalise the parts",
r"""If $px+qy=S$ with $x,y>0$, the product $(px)(qy)$ is greatest when $px=qy=\frac S2$.""",
r"If $2x+3y=12$ with $x,y>0$, find the maximum of $xy$.",
r"$2x=3y=6\Rightarrow x=3,\ y=2$, so the maximum of $xy$ is $6$."),
],
[
"Applying AM–GM when a term can be negative (e.g. $x+\\frac1x$ for $x<0$ has no minimum of 2).",
"Reporting the $x$ where the extreme occurs instead of the extreme value itself.",
"Calling the vertex a minimum when the leading coefficient is negative.",
]),
]

# ---------------------------------------------------------------- patterns
patterns = [
P(r"$x+\frac1x=k$ → higher powers", "very common",
  r"Given $x+\frac1x$, $x-\frac1x$ or a quadratic with equal end coefficients; asked for $x^3+\frac1{x^3}$, $x^4+\frac1{x^4}$, $x^5+\frac1{x^5}$.",
  r"Use the ladder: square and subtract 2; cube with $k^3-3k$. Recognise special values ($1,\ \sqrt3$, etc.) for cyclic powers."),
P(r"Given $a\pm b$ and $ab$, find $a^3\pm b^3$ / $a^4+b^4$", "very common",
  r"Two conditions on two variables and a symmetric expression to evaluate.",
  r"Never solve for $a,b$. Use $(a+b)^3-3ab(a+b)$, $(a-b)^3+3ab(a-b)$, $(a^2+b^2)^2-2a^2b^2$."),
P(r"Conjugate surd $x=p+\sqrt q$", "very common",
  r"$x=2+\sqrt3$, $3-2\sqrt2$, $\frac{1}{\sqrt5-2}$ etc., asked for $x^2+\frac1{x^2}$ or a polynomial in $x$.",
  r"Check $p^2-q=1$ → $\frac1x=p-\sqrt q$; or form the quadratic $x^2-2px+1=0$ and reduce the polynomial with it."),
P(r"$a^3+b^3+c^3-3abc$ / zero-sum cubes", "common",
  r"Three variables with $a+b+c$ given, or expressions like $(x-y)^3+(y-z)^3+(z-x)^3$.",
  r"Use the factor form or half form; if the sum is zero, replace the sum of cubes by $3abc$."),
P("Sum of squares equal to zero", "common",
  r"An equation like $x^2+y^2+z^2-2x+4y-6z+14=0$ or $a^2+b^2+c^2=ab+bc+ca$.",
  r"Complete squares so the constants cancel; each square is zero, giving exact values."),
P("Big-number / decimal simplification", "common",
  r"Fractions with cubes over quadratics of the same two numbers, e.g. $\frac{p^3+q^3}{p^2-pq+q^2}$.",
  r"Match the identity using the sign of the denominator's middle term; answer is $p\pm q$."),
P("Linear equations, graphs, remainder", "occasional",
  r"Condition for unique/no/infinite solutions, area of triangle with axes, remainder or factor of a polynomial.",
  r"Ratios of coefficients; intercepts; put the zero of the divisor."),
P("Maximum / minimum value", "occasional",
  r"'Least value of $4x+\frac9x$', 'greatest value of $5+12x-3x^2$'.",
  r"AM ≥ GM for $ax+\frac bx$; complete the square for quadratics."),
]

# ---------------------------------------------------------------- solved examples
solved = []

# S1: x - 1/x = 4 -> x^3 - 1/x^3
r = sp.solve(x - 1 / x - 4, x)[0]
ans = sp.simplify(r**3 - r**-3)
solved.append(Q("alg-s01",
r"If $x-\frac1x=4$, then what is the value of $x^3-\frac{1}{x^3}$?",
[52, 64, 76, 72], ans,
r"""
Use $x^3-\frac1{x^3}=\left(x-\frac1x\right)^3+3\left(x-\frac1x\right)$.

$=4^3+3(4)=64+12=76$.
""",
r"""For the **difference** form, cube and **add** three times: $k^3+3k=64+12=76$. (For the sum form you subtract: $k^3-3k$.)""",
"easy", "alg-reciprocal", r"$x-\frac1x=k$ → cube", 40))

# S2: 2x+3y=12, xy=6 -> 8x^3+27y^3
sol = sp.solve([2 * x + 3 * y - 12, x * y - 6], [x, y])
vals = {sp.simplify(8 * s[0]**3 + 27 * s[1]**3) for s in sol}
assert len(vals) == 1
ans = vals.pop()
solved.append(Q("alg-s02",
r"If $2x+3y=12$ and $xy=6$, then the value of $8x^3+27y^3$ is:",
[1296, 432, 1728, 540], ans,
r"""
Let $p=2x$ and $q=3y$. Then $p+q=12$ and $pq=6xy=36$.

$p^3+q^3=(p+q)^3-3pq(p+q)=1728-3(36)(12)=1728-1296=432$.
""",
r"""Treat $2x$ and $3y$ as single terms: $8x^3+27y^3=(2x+3y)^3-18xy(2x+3y)=1728-18\cdot6\cdot12=432$.
Trap: 1296 is the subtracted term, 1728 is just $12^3$.""",
"medium", "alg-identities", r"given $a+b$ and $ab$, find $a^3+b^3$", 60))

# S3: sqrt(11 + 2 sqrt30)
target = sq(11 + 2 * sq(30))
solved.append(Q("alg-s03",
r"The value of $\sqrt{11+2\sqrt{30}}$ is:",
[(r"$\sqrt{15}+\sqrt2$", sq(15) + sq(2)), (r"$\sqrt6+\sqrt5$", sq(6) + sq(5)),
 (r"$\sqrt{10}+\sqrt3$", sq(10) + sq(3)), (r"$\sqrt6-\sqrt5$", sq(6) - sq(5))], target,
r"""
Write $\sqrt{11+2\sqrt{30}}=\sqrt m+\sqrt n$. Squaring: $m+n+2\sqrt{mn}=11+2\sqrt{30}$, so $m+n=11$, $mn=30$.

The numbers are 6 and 5, so the value is $\sqrt6+\sqrt5$.
""",
r"""Sum 11, product 30 → 6 and 5. Answer $\sqrt6+\sqrt5$. Check a trap option quickly: $(\sqrt{15}+\sqrt2)^2=17+2\sqrt{30}$ ✗.""",
"easy", "alg-surds", "square root of a surd", 35))

# S4: factor theorem
kv = sp.solve((x**3 - k * x**2 + 5 * x - 6).subs(x, 2), k)[0]
solved.append(Q("alg-s04",
r"If $(x-2)$ is a factor of $x^3-kx^2+5x-6$, then the value of $k$ is:",
[-3, 2, 3, 4], kv,
r"""
By the factor theorem, $f(2)=0$:

$8-4k+10-6=0\Rightarrow 12-4k=0\Rightarrow k=3$.
""",
r"""Put the zero of the divisor ($x=2$) and equate to 0 — no division needed.""",
"easy", "alg-linear-poly", "factor theorem", 30))

# ---------------------------------------------------------------- practice
pr = []

r = sp.solve(x + 1 / x - 5, x)[0]
pr.append(Q("alg-q01",
r"If $x+\frac1x=5$, then what is the value of $x^2+\frac{1}{x^2}$?",
[25, 23, 27, 21], sp.simplify(r**2 + r**-2),
r"$x^2+\frac1{x^2}=\left(x+\frac1x\right)^2-2=25-2=23$.",
r"Square and subtract 2: $25-2=23$. (27 comes from adding 2 — the $x-\frac1x$ rule.)",
"easy", "alg-reciprocal", r"$x+\frac1x=k$ → square", 25))

sol = sp.solve([a + b - 9, a * b - 14], [a, b])
v = {sp.simplify(s[0]**2 + s[1]**2) for s in sol}.pop()
pr.append(Q("alg-q02",
r"If $a+b=9$ and $ab=14$, then $a^2+b^2$ is equal to:",
[53, 109, 67, 25], v,
r"$a^2+b^2=(a+b)^2-2ab=81-28=53$.",
r"$81-2(14)=53$. Traps: $81+28=109$, $81-14=67$, $81-56=25$ (that is $(a-b)^2$).",
"easy", "alg-identities", r"given $a+b$ and $ab$", 25))

p_, q_ = sp.Rational(47, 10), sp.Rational(23, 10)
v = (p_**3 + q_**3) / (p_**2 - p_ * q_ + q_**2)
pr.append(Q("alg-q03",
r"Simplify: $\dfrac{4.7^3+2.3^3}{4.7^2-4.7\times2.3+2.3^2}$",
[("7", 7), ("2.4", sp.Rational(24, 10)), ("10.81", sp.Rational(1081, 100)), ("1", 1)], v,
r"""
This is $\frac{p^3+q^3}{p^2-pq+q^2}$ with $p=4.7,\ q=2.3$. Since $p^3+q^3=(p+q)(p^2-pq+q^2)$, the value is $p+q=7$.
""",
r"Numerator has $+$, denominator's middle sign is $-$ → answer is the sum $4.7+2.3=7$.",
"easy", "alg-identities", "decimal simplification by identity", 30))

A, B, C = 11, -5, -6
pr.append(Q("alg-q04",
r"If $a=11$, $b=-5$ and $c=-6$, then the value of $a^3+b^3+c^3$ is:",
[-990, 990, 330, 0], A**3 + B**3 + C**3,
r"""
$a+b+c=11-5-6=0$, so $a^3+b^3+c^3=3abc=3(11)(-5)(-6)=990$.
""",
r"Zero sum spotted → $3abc$. Two negatives make the product positive: $+990$.",
"easy", "alg-three-var", "a+b+c=0 ⇒ sum of cubes = 3abc", 30))

xi = sp.solve((3 * x + 4 * y - 24).subs(y, 0), x)[0]
yi = sp.solve((3 * x + 4 * y - 24).subs(x, 0), y)[0]
pr.append(Q("alg-q05",
r"What is the area (in square units) of the triangle formed by the line $3x+4y=24$ and the coordinate axes?",
[48, 24, 12, 96], sp.Rational(1, 2) * xi * yi,
r"""
$x$-intercept: put $y=0$ → $x=8$. $y$-intercept: put $x=0$ → $y=6$.

Area $=\frac12\times8\times6=24$ square units.
""",
r"Area $=\frac{c^2}{2ab}=\frac{576}{2\times12}=24$.",
"easy", "alg-linear-poly", "area of triangle made by a line with axes", 30))

X = 3 + 2 * sq(2)
pr.append(Q("alg-q06",
r"If $x=3+2\sqrt2$, then what is the value of $x^2+\frac{1}{x^2}$?",
[36, 34, 32, 38], sp.simplify(X**2 + X**-2),
r"""
$\frac1x=\frac{1}{3+2\sqrt2}=\frac{3-2\sqrt2}{9-8}=3-2\sqrt2$.

So $x+\frac1x=6$ and $x^2+\frac1{x^2}=36-2=34$.
""",
r"$3^2-(2\sqrt2)^2=1$ → conjugate is the reciprocal. $x+\frac1x=2\times3=6$ → $36-2=34$.",
"medium", "alg-surds", r"conjugate surd $x=p+\sqrt q$", 40))

r = sp.solve(x + 1 / x - 3, x)[0]
pr.append(Q("alg-q07",
r"If $x+\frac1x=3$, then the value of $x^5+\frac{1}{x^5}$ is:",
[123, 126, 129, 117], sp.simplify(r**5 + r**-5),
r"""
$x^2+\frac1{x^2}=9-2=7$; $x^3+\frac1{x^3}=27-9=18$.

$x^5+\frac1{x^5}=\left(x^2+\frac1{x^2}\right)\left(x^3+\frac1{x^3}\right)-\left(x+\frac1x\right)=7\times18-3=123$.
""",
r"Multiply the 2nd and 3rd powers and subtract the 1st: $7\times18-3=123$. (126 forgets to subtract.)",
"medium", "alg-reciprocal", r"$x+\frac1x=k$ → fifth power", 50))

r = sp.solve(x**2 - 4 * x + 1, x)[0]
pr.append(Q("alg-q08",
r"If $x^2-4x+1=0$, then what is the value of $x^4+\frac{1}{x^4}$?",
[196, 194, 198, 142], sp.simplify(r**4 + r**-4),
r"""
Divide by $x$: $x-4+\frac1x=0\Rightarrow x+\frac1x=4$.

$x^2+\frac1{x^2}=16-2=14$, then $x^4+\frac1{x^4}=14^2-2=194$.
""",
r"Ladder: $4\to14\to194$ (square, minus 2, each step).",
"medium", "alg-reciprocal", "quadratic with equal end coefficients", 40))

sol = sp.solve([sp.diff(a**2 + b**2 + c**2 + 35 - 2 * (a - 3 * b + 5 * c), s) for s in (a, b, c)], [a, b, c])
assert (a**2 + b**2 + c**2 + 35 - 2 * (a - 3 * b + 5 * c)).subs(sol) == 0
assert sp.expand((a - 1)**2 + (b + 3)**2 + (c - 5)**2 - (a**2 + b**2 + c**2 + 35 - 2 * (a - 3 * b + 5 * c))) == 0
pr.append(Q("alg-q09",
r"If $a^2+b^2+c^2+35=2(a-3b+5c)$, where $a,b,c$ are real, then the value of $a-b+c$ is:",
[3, 9, -1, 7], (a - b + c).subs(sol),
r"""
Move everything to one side: $a^2-2a+b^2+6b+c^2-10c+35=0$.

Since $35=1+9+25$: $(a-1)^2+(b+3)^2+(c-5)^2=0$, so $a=1,\ b=-3,\ c=5$.

$a-b+c=1+3+5=9$.
""",
r"Constant $35=1^2+3^2+5^2$ confirms perfect squares. Read the values from the coefficients: $a=1, b=-3, c=5$ → $9$. (3 is $a+b+c$ — a trap.)",
"medium", "alg-identities", "sum of squares equal to zero", 50))

s1, s2 = 12, 50
p2 = sp.Rational(s1**2 - s2, 2)
v = s1 * (s2 - p2)
# cross-check with actual numbers satisfying the conditions
sol = sp.solve([a + b + c - 12, a**2 + b**2 + c**2 - 50, a - 3], [a, b, c])
assert all(sp.simplify(s[0]**3 + s[1]**3 + s[2]**3 - 3 * s[0] * s[1] * s[2] - v) == 0 for s in sol)
pr.append(Q("alg-q10",
r"If $a+b+c=12$ and $a^2+b^2+c^2=50$, then what is the value of $a^3+b^3+c^3-3abc$?",
[1164, 36, 72, 18], v,
r"""
$ab+bc+ca=\frac{(a+b+c)^2-(a^2+b^2+c^2)}{2}=\frac{144-50}{2}=47$.

$a^3+b^3+c^3-3abc=(a+b+c)\left[(a^2+b^2+c^2)-(ab+bc+ca)\right]=12(50-47)=36$.
""",
r"$12\times(50-47)=36$. Trap 1164 adds 47 instead of subtracting.",
"medium", "alg-three-var", r"$a^3+b^3+c^3-3abc$ from sum and sum of squares", 50))

kv = sp.solve(sp.Eq(sp.Rational(2, 1) / (k - 1), sp.Rational(3, 6)), k)[0]
assert sp.Rational(3, 6) == sp.Rational(7, 14)
pr.append(Q("alg-q11",
r"For what value of $k$ will the system $2x+3y=7$ and $(k-1)x+6y=14$ have infinitely many solutions?",
[4, 5, 3, 7], kv,
r"""
For infinitely many solutions, $\frac{a_1}{a_2}=\frac{b_1}{b_2}=\frac{c_1}{c_2}$:

$\frac{2}{k-1}=\frac36=\frac{7}{14}=\frac12\Rightarrow k-1=4\Rightarrow k=5$.
""",
r"Second equation must be exactly double the first: $2\times2=4=k-1$, so $k=5$. (4 is $k-1$, a trap.)",
"medium", "alg-linear-poly", "consistency of linear equations", 40))

expr = 5 + 12 * x - 3 * x**2
pr.append(Q("alg-q12",
r"What is the maximum value of $5+12x-3x^2$?",
[2, 17, 20, 12], sp.maximum(expr, x),
r"""
$5+12x-3x^2=5-3(x^2-4x)=5-3\left[(x-2)^2-4\right]=17-3(x-2)^2$.

The maximum is $17$, at $x=2$.
""",
r"Vertex at $x=-\frac{b}{2a}=-\frac{12}{-6}=2$; value $=5+24-12=17$. (2 is the $x$ at which it occurs — a trap.)",
"medium", "alg-maxmin", "maximum of a quadratic", 45))

X = 1 / (2 - sq(3))
v = sp.simplify(X**3 - 2 * X**2 - 7 * X + 5)
assert sp.rem(x**3 - 2 * x**2 - 7 * x + 5, x**2 - 4 * x + 1, x) == 3
pr.append(Q("alg-q13",
r"If $x=\dfrac{1}{2-\sqrt3}$, then the value of $x^3-2x^2-7x+5$ is:",
[5, 3, 1, (r"$4\sqrt3$", 4 * sq(3))], v,
r"""
$x=\frac{1}{2-\sqrt3}=2+\sqrt3$, so $x-2=\sqrt3\Rightarrow x^2-4x+4=3\Rightarrow x^2-4x+1=0$.

Divide the cubic by $x^2-4x+1$: $x^3-2x^2-7x+5=(x^2-4x+1)(x+2)+3$.

Since $x^2-4x+1=0$, the value is $3$.
""",
r"Form the quadratic $x^2-4x+1=0$ from the surd, then reduce: $x^3=4x^2-x$, so the expression $=4x^2-x-2x^2-7x+5=2x^2-8x+5=2(4x-1)-8x+5=3$.",
"hard", "alg-surds", "polynomial value at a conjugate surd", 75))

v = sp.Rational(36 - (s := 36 - 18), 3)  # placeholder, recomputed below
S1_, S2_, S3_ = 6, 14, 36
e2 = sp.Rational(S1_**2 - S2_, 2)
abc = sp.Rational(S3_ - S1_ * (S2_ - e2), 3)
roots = sp.solve(x**3 - S1_ * x**2 + e2 * x - abc, x)
assert sorted(roots) == [1, 2, 3] and sum(r_**3 for r_ in roots) == 36
pr.append(Q("alg-q14",
r"If $a+b+c=6$, $a^2+b^2+c^2=14$ and $a^3+b^3+c^3=36$, then the value of $abc$ is:",
[12, 18, 6, 3], abc,
r"""
$ab+bc+ca=\frac{36-14}{2}=11$.

$a^3+b^3+c^3-3abc=(a+b+c)(a^2+b^2+c^2-ab-bc-ca)=6(14-11)=18$.

So $36-3abc=18\Rightarrow abc=6$.
""",
r"Guess small integers: $1,2,3$ have sum 6, squares 14, cubes 36 — so $abc=6$. Verify one condition beyond the given sum before trusting a guess.",
"hard", "alg-three-var", r"find $abc$ from power sums", 70))

r = sp.solve(x + 1 / x - sq(3), x)[0]
v = sp.simplify(sp.expand(r**18 + r**12 + r**6 + 1))
pr.append(Q("alg-q15",
r"If $x+\frac1x=\sqrt3$, then the value of $x^{18}+x^{12}+x^6+1$ is:",
[0, 1, 2, 4], v,
r"""
Cube both sides of $x+\frac1x=\sqrt3$: $x^3+\frac1{x^3}+3\left(x+\frac1x\right)=3\sqrt3\Rightarrow x^3+\frac1{x^3}=0$.

So $x^6=-1$. Then $x^{18}=(x^6)^3=-1$ and $x^{12}=(x^6)^2=1$.

Value $=-1+1-1+1=0$.
""",
r"Memorise: $x+\frac1x=\sqrt3\Rightarrow x^6=-1$. Substitute $x^6=-1$: $-1+1-1+1=0$.",
"hard", "alg-reciprocal", r"special value $x+\frac1x=\sqrt3$", 60))

topic = {
    "id": "algebra",
    "sectionId": "quant",
    "title": "Algebra",
    "order": 12,
    "importance": "high",
    "avgQuestions": {"tier1": 3, "tier2": 4},
    "summary": r"Identities, $x+\frac1x$ expressions, $a^3+b^3+c^3-3abc$, surds, linear equations and simple max–min. "
               r"Algebra gives 2–4 marks-rich questions in every CGL shift, and almost all of them fall to a handful of identities plus value-putting — the highest return per hour of study in advanced maths.",
    "subtopics": subtopics,
    "pyqPatterns": patterns,
    "solvedExamples": solved,
    "practice": pr,
}

if __name__ == "__main__":
    write_topic(topic)
