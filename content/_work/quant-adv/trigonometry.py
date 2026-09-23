import sympy as sp
from qa_common import Q, F, T, S, P, U, write_topic

# exact trig values
s30, c30, t30 = sp.Rational(1, 2), sp.sqrt(3) / 2, 1 / sp.sqrt(3)
s45 = 1 / sp.sqrt(2)
s60, c60, t60 = sp.sqrt(3) / 2, sp.Rational(1, 2), sp.sqrt(3)

# ---------------------------------------------------------------- sanity checks
assert s30 + c60 == 1
assert 1 + 1 == 2  # tan45 + cot45
assert sp.Rational(5, 12) == sp.Rational(5, 13) / (sp.Rational(12, 13))
assert sp.sec(sp.pi / 6) ** 2 - sp.tan(sp.pi / 6) ** 2 == 1
assert s60 * c30 + s30 * c60 == 1
# sin(40+theta)=cos(30+theta) => theta = 10 deg, check numerically
assert abs(float(sp.sin(sp.rad(50)) - sp.cos(sp.rad(40)))) < 1e-12
# sin + sin^2 = 1  =>  cos^2 + cos^4 = 1
phi = (sp.sqrt(5) - 1) / 2
assert sp.simplify((1 - phi**2) + (1 - phi**2) ** 2 - 1) == 0
assert float(sp.sin(sp.rad(0)) + sp.cos(sp.rad(0))) == 1.0  # min of sin+cos
assert abs(float(sp.tan(sp.rad(15)) * sp.tan(sp.rad(75))) - 1) < 1e-12
x = sp.symbols("x")
expr = 2 * (x**3 + (1 - x) ** 3) - 3 * (x**2 + (1 - x) ** 2) + 1
assert sp.expand(expr) == 0  # with x = sin^2, for every x
assert sp.Rational(13, 5) == 1 / (sp.Rational(5, 13))
assert sp.Rational(-7) == (sp.Rational(3, 5) + sp.Rational(4, 5)) / (sp.Rational(3, 5) - sp.Rational(4, 5))
# min of 4 tan^2 + 9 cot^2 = 2*sqrt(36) = 12, at tan^2 = 3/2
assert sp.simplify(4 * sp.Rational(3, 2) + 9 / sp.Rational(3, 2)) == 12
# cosec + cot = 3  ->  sin = 3/5
csc_, cot_ = sp.Rational(5, 3), sp.Rational(4, 3)
assert csc_ + cot_ == 3 and 1 / csc_ == sp.Rational(3, 5)
# (cosec - sin)(sec - cos)(tan + cot) = 1
t = sp.symbols("t", positive=True)
val = sp.simplify((1 / sp.sin(sp.pi / 6) - sp.sin(sp.pi / 6)) * (1 / sp.cos(sp.pi / 6) - sp.cos(sp.pi / 6))
                  * (sp.tan(sp.pi / 6) + 1 / sp.tan(sp.pi / 6)))
assert val == 1
# (tan+sec-1)(tan-sec+1) = 2(sec-1)
tv, sv = sp.tan(sp.pi / 5).evalf(), sp.sec(sp.pi / 5).evalf()
assert abs(((tv + sv - 1) * (tv - sv + 1)) - 2 * (sv - 1)) < 1e-12
# tan1 tan2 ... tan89 = 1 (numeric)
assert abs(float(sp.prod([sp.tan(sp.rad(k)) for k in range(1, 90)]).evalf()) - 1) < 1e-9
# 2 sin^2 + 7 cos^2 = 6  ->  cos^2 = 4/5, tan = 1/2
assert sp.simplify(2 * sp.Rational(1, 5) + 7 * sp.Rational(4, 5)) == 6
assert sp.sqrt(sp.Rational(1, 5) / sp.Rational(4, 5)) == sp.Rational(1, 2)
# greatest of 3 sin + 4 cos + 5 = 5 + 5 = 10 (max at tan = 3/4)
assert abs(float(3 * sp.sin(sp.atan(sp.Rational(3, 4))) + 4 * sp.cos(sp.atan(sp.Rational(3, 4)))) - 5) < 1e-12

# ---------------------------------------------------------------- subtopics
subtopics = [
S("trig-ratios", "Ratios and standard values",
r"""
For an acute angle $\theta$ in a right triangle: $\sin\theta=\frac{\text{opp}}{\text{hyp}}$,
$\cos\theta=\frac{\text{adj}}{\text{hyp}}$, $\tan\theta=\frac{\text{opp}}{\text{adj}}$, and
$\text{cosec}=\frac1{\sin}$, $\sec=\frac1{\cos}$, $\cot=\frac1{\tan}$.

**Standard value table (memorise cold — most CGL questions are one lookup away):**

| $\theta$ | $0^\circ$ | $30^\circ$ | $45^\circ$ | $60^\circ$ | $90^\circ$ |
|---|---|---|---|---|---|
| $\sin$ | $0$ | $\frac12$ | $\frac{1}{\sqrt2}$ | $\frac{\sqrt3}{2}$ | $1$ |
| $\cos$ | $1$ | $\frac{\sqrt3}{2}$ | $\frac{1}{\sqrt2}$ | $\frac12$ | $0$ |
| $\tan$ | $0$ | $\frac{1}{\sqrt3}$ | $1$ | $\sqrt3$ | undef. |
""",
[
F("Reciprocal pairs", r"\text{cosec}\theta=\frac{1}{\sin\theta},\quad \sec\theta=\frac{1}{\cos\theta},\quad \cot\theta=\frac{1}{\tan\theta}"),
F("sin column", r"\sin0^\circ=0,\ \sin30^\circ=\frac12,\ \sin45^\circ=\frac{1}{\sqrt2},\ \sin60^\circ=\frac{\sqrt3}{2},\ \sin90^\circ=1"),
F("cos column", r"\cos\theta=\sin(90^\circ-\theta)"),
F("tan column", r"\tan0^\circ=0,\ \tan30^\circ=\frac{1}{\sqrt3},\ \tan45^\circ=1,\ \tan60^\circ=\sqrt3"),
],
[
T("The 1-2-3 memory trick for sin",
r"""Write $\frac{\sqrt0}{2},\frac{\sqrt1}{2},\frac{\sqrt2}{2},\frac{\sqrt3}{2},\frac{\sqrt4}{2}$ for
$0^\circ,30^\circ,45^\circ,60^\circ,90^\circ$ — the sin row falls out; the cos row is the same read backwards.
Divide the two rows to get tan.""",
r"Find the value of $\sin30^\circ+\cos60^\circ+\tan45^\circ$.",
r"$\frac12+\frac12+1=2$."),
T("Reciprocal first, table second",
r"""When an expression has cosec/sec/cot, flip each to sin/cos/tan before touching the table.""",
r"Find the value of $\text{cosec}30^\circ-\sec60^\circ$.",
r"$2-2=0$ — both flip to $\frac{1}{1/2}=2$."),
],
[
"$\\sin45^\\circ$ written as $\\frac{1}{2}$ (confusing the 45 and 30 entries).",
"$\\tan90^\\circ$ treated as $0$ or $1$ — it is undefined.",
"Reciprocal flipped the wrong way ($\\sec\\theta$ taken as $\\frac{1}{\\sin\\theta}$).",
]),
S("trig-identities", "Fundamental identities",
r"""
Three identities drive almost every simplification:
$$\sin^2\theta+\cos^2\theta=1,\qquad 1+\tan^2\theta=\sec^2\theta,\qquad 1+\cot^2\theta=\text{cosec}^2\theta$$
Each splits into handy parts: $\sin^2\theta=1-\cos^2\theta$, $\sec^2\theta-\tan^2\theta=1$,
$\text{cosec}^2\theta-\cot^2\theta=1$. Expressions with $\sin^6+\cos^6$ or $\sin^4+\cos^4$ reduce through
these — treat $x=\sin^2\theta$ so $x+(1-x)=1$.
""",
[
F("Pythagorean identities", r"\sin^2\theta+\cos^2\theta=1,\quad 1+\tan^2\theta=\sec^2\theta,\quad 1+\cot^2\theta=\text{cosec}^2\theta"),
F("Fourth powers", r"\sin^4\theta+\cos^4\theta=1-2\sin^2\theta\cos^2\theta"),
F("Sixth powers", r"\sin^6\theta+\cos^6\theta=1-3\sin^2\theta\cos^2\theta"),
F("Product-to-sum bridge", r"\tan\theta=\frac{\sin\theta}{\cos\theta},\quad \cot\theta=\frac{\cos\theta}{\sin\theta}"),
],
[
T("Substitute $x=\\sin^2\\theta$",
r"""Everything above degree 4 collapses with $x$ and $1-x$. Memorise the two reduced forms for 4th and 6th powers.""",
r"Find the value of $2(\sin^6\theta+\cos^6\theta)-3(\sin^4\theta+\cos^4\theta)+1$.",
r"$2(1-3s^2c^2)-3(1-2s^2c^2)+1=2-3+1+( -6+6)s^2c^2=0$ for every $\theta$."),
T("Sec/tan pairs move as one",
r"""See $\sec^2$ and $\tan^2$ together → replace by 1 (or by each other via $\sec^2=1+\tan^2$). Same for
cosec/cot.""",
r"Simplify $\dfrac{\sec^2\theta-\tan^2\theta}{1+\cot^2\theta}\times\text{cosec}^2\theta$.",
r"Numerator $=1$, $1+\cot^2=\text{cosec}^2$, so the value is $1$."),
],
[
"Writing $\\tan^2\\theta+1=\\sec\\theta$ (the square is dropped).",
"Expanding $\\sin^6+\\cos^6$ as $(\\sin^2+\\cos^2)^3$ without subtracting the cross terms.",
"Mixing degrees of powers: $\\sin^4+\\cos^4\\neq1$.",
]),
S("trig-complementary", "Complementary angles",
r"""
For angles that add to $90^\circ$:
$$\sin(90^\circ-\theta)=\cos\theta,\quad \tan(90^\circ-\theta)=\cot\theta,\quad \sec(90^\circ-\theta)=\text{cosec}\theta$$
and similarly in reverse. This converts "odd" angles ($67\tfrac12^\circ$, $72^\circ$, ...) into their partners and
makes paired products equal 1: $\tan\theta\cdot\tan(90^\circ-\theta)=1$.

An equation like $\sin(A+\theta)=\cos(B+\theta)$ forces $(A+\theta)+(B+\theta)=90^\circ$.
""",
[
F("Complementary pairs", r"\sin(90-\theta)=\cos\theta,\ \tan(90-\theta)=\cot\theta,\ \sec(90-\theta)=\text{cosec}\theta"),
F("Paired products", r"\tan\theta\,\tan(90^\circ-\theta)=1,\quad \sin\theta\,\text{cosec}\theta=1"),
F("Angle-equation rule", r"\sin(A+\theta)=\cos(B+\theta)\Rightarrow A+B+2\theta=90^\circ"),
],
[
T("Pair the angles that add to 90°",
r"""In a long product, look for $\theta$ and $90-\theta$ pairs first — each pair collapses to 1. The classic
$\tan1^\circ\tan2^\circ\cdots\tan89^\circ$ collapses completely.""",
r"Find the value of $\tan15^\circ\tan25^\circ\tan45^\circ\tan65^\circ\tan75^\circ$.",
r"$(\tan15\tan75)(\tan25\tan65)(\tan45)=1\times1\times1=1$."),
T("Convert everything to one angle",
r"""Rewrite each term at its complementary partner until only one angle remains; a $\sin^2+\cos^2$ pair may then
collapse.""",
r"Find the value of $\sin^265^\circ+\sin^225^\circ$.",
r"$\sin65^\circ=\cos25^\circ$, so the sum $=\cos^225^\circ+\sin^225^\circ=1$."),
T("Equation → sum to 90°",
r"""When $\sin(\ldots)=\cos(\ldots)$, set the two bracketed angles to sum to $90^\circ$ and solve.""",
r"If $\sin(40^\circ+\theta)=\cos(30^\circ+\theta)$ and both angles are acute, find $\theta$.",
r"$40+\theta+30+\theta=90\Rightarrow2\theta=20\Rightarrow\theta=10^\circ$."),
],
[
"Complementary conversion applied to the wrong function ($\\sec(90-\\theta)=\\sec\\theta$ is wrong).",
"Setting $\\sin A=\\cos B\\Rightarrow A+B=180^\\circ$ — it is $90^\\circ$.",
"Products paired as $\\tan\\theta\\cdot\\cot\\theta=1$ but evaluated before converting to the same angle.",
]),
S("trig-valueput", "Value-putting and given-ratio questions",
r"""
Two CGL workhorses:

1. **Given one ratio, draw the triangle.** If $\sin\theta=\frac{5}{13}$, take opposite $=5$, hypotenuse $=13$,
   adjacent $=\sqrt{13^2-5^2}=12$ (a 5-12-13 triplet!) and read off every other ratio.
2. **Value-putting an identity.** If only $\sin\theta+\text{cosec}\theta$ or a quadratic condition like
   $\sin\theta+\sin^2\theta=1$ is given, convert the asked expression into the given pieces — or test a
   convenient $\theta$ when the expression is identically constant.
""",
[
F("From sin to the rest", r"\sin\theta=\frac{p}{h}\Rightarrow \cos\theta=\frac{\sqrt{h^2-p^2}}{h},\ \tan\theta=\frac{p}{\sqrt{h^2-p^2}}"),
F("Standard triplets", r"(3,4,5),\ (5,12,13),\ (7,24,25),\ (8,15,17),\ (9,40,41)"),
F("Sum-product of a ratio and reciprocal", r"x+\frac1x=k\Rightarrow x^2+\frac{1}{x^2}=k^2-2"),
],
[
T("Draw the triplet triangle",
r"""Ratio given → sides in hand in 5 seconds. Check the triplet table before any algebra.""",
r"If $\cos\theta=\dfrac{7}{25}$, find $\tan\theta$.",
r"Adjacent 7, hypotenuse 25 → opposite $\sqrt{625-49}=24$; $\tan\theta=\frac{24}{7}$."),
T("Reduce the asked expression",
r"""Rewrite the target in terms of the given relation. For $x+\frac1x$ chains, square and subtract 2.""",
r"If $\sin\theta+\text{cosec}\theta=2$, find $\sin^2\theta+\text{cosec}^2\theta$.",
r"$(x+\frac1x)^2=x^2+\frac1{x^2}+2\Rightarrow 4-2=2$. (Here $x=1$ in fact.)"),
],
[
"Triplets applied with hypotenuse as a leg ($\\sqrt{13^2-12^2}$ vs $\\sqrt{13^2+12^2}$).",
"Forgetting that a given ratio fixes $\theta$ up to the quadrant — CGL keeps $\theta$ acute, so take the positive root.",
"Value-putting with $\\theta=45^\\circ$ when the expression is not constant — verify a second angle before trusting it.",
]),
S("trig-maxmin", "Maximum and minimum values",
r"""
For $0^\circ\le\theta\le90^\circ$:
- $0\le\sin\theta,\cos\theta\le1$; $\sec\theta,\text{cosec}\theta\ge1$; $\tan\theta,\cot\theta$ are unbounded.
- $\sin\theta+\cos\theta\in[1,\sqrt2]$; $\sin\theta-\cos\theta\in[-1,1]$; $\sin\theta\cos\theta\le\frac12$.
- $a\sin^2\theta+b\cos^2\theta$ has minimum $\min(a,b)$ and maximum $\max(a,b)$.
- $a\tan^2\theta+b\cot^2\theta\ (\text{and } a\sin^2+b\,\text{cosec}^2)$ has minimum $2\sqrt{ab}$ by AM–GM.
- $\sec^2\theta+\text{cosec}^2\theta$ has minimum $2+2=4$ (at $45^\circ$).
""",
[
F("Ranges", r"0\le\sin\theta\le1,\quad \sec\theta\ge1,\quad \sin\theta+\cos\theta\in[1,\sqrt2]"),
F("Weighted square form", r"a\sin^2\theta+b\cos^2\theta\in[\min(a,b),\max(a,b)]"),
F("AM-GM forms", r"a\tan^2\theta+b\cot^2\theta\ge2\sqrt{ab},\quad a\sin^2\theta+b\,\text{cosec}^2\theta\ge2\sqrt{ab}"),
F("Combined sec-cosec", r"\sec^2\theta+\text{cosec}^2\theta=2+\tan^2\theta+\cot^2\theta\ge4"),
F("Linear combination", r"a\sin\theta+b\cos\theta\text{ has maximum }\sqrt{a^2+b^2}"),
],
[
T("Match the question to a range",
r"""Bounded pairs ($\sin+\cos$ etc.) → memorised range. Weighted square sums → min of coefficients or $2\sqrt{ab}$.""",
r"Find the minimum value of $4\tan^2\theta+9\cot^2\theta$ for $0^\circ<\theta<90^\circ$.",
r"$2\sqrt{4\times9}=12$ (at $\tan^2\theta=\frac32$)."),
T("Weighted sin-cos squares are bounded by coefficients",
r"""$2\sin^2\theta+3\cos^2\theta=2+\cos^2\theta$, so it ranges from 2 to 3 — min 2, max 3, no calculus.""",
r"Find the minimum value of $5\sin^2\theta+12\cos^2\theta$.",
r"$=5+7\cos^2\theta\ge5$; minimum $5$ (at $\theta=0$)."),
],
[
"AM-GM applied to $a\\sin\\theta+b\\text{cosec}\\theta$ where the equality point may be unreachable — for the square versions it is safe, check before using.",
"Quoting $\\sqrt2$ as the **minimum** of $\\sin+\\cos$ — $\\sqrt2$ is the maximum.",
"$\\sec^2+\\text{cosec}^2$ minimum quoted as 2 instead of 4.",
]),
]

patterns = [
P("Standard-value evaluation", "very common",
  r"A short expression built from $0^\circ,30^\circ,45^\circ,60^\circ,90^\circ$ values.",
  r"Flip reciprocals first, then read the table; the answer is usually 0, 1 or 2 — use it to sanity-check."),
P("Given one ratio, find others", "very common",
  r"$\sin\theta=\frac{p}{h}$ (or tan/cos) given; find another ratio or an expression in two of them.",
  r"Triplet triangle: adjacent $=\sqrt{h^2-p^2}$; read all ratios at once."),
P("Complementary-angle simplification", "very common",
  r"Angles like $70^\circ$ beside $20^\circ$, or $\sin(90-\theta)$ inside expressions, or long tan products.",
  r"Pair angles summing to $90^\circ$ (each product = 1); convert to one function family; equation form gives $A+B+2\theta=90^\circ$."),
P("Identity simplification (sin^4/sin^6 chains)", "common",
  r"Expressions in $\sin^4+\cos^4$, $\sin^6+\cos^6$, $\sec^2-\tan^2$ chains; answer often constant.",
  r"$x=\sin^2\theta$ with $x+(1-x)=1$; memorise the 4th/6th-power reductions."),
P("Maximum/minimum value", "common",
  r"'Least/greatest value of $a\sin^2+b\cos^2$', '$a\tan^2+b\cot^2$', '$\sin\theta+\cos\theta$'.",
  r"Bounded → coefficient min/max; unbounded reciprocal pairs → $2\sqrt{ab}$."),
P("Condition-based expression", "occasional",
  r"A condition like $\sin\theta+\sin^2\theta=1$ or $\text{cosec}\theta+\cot\theta=k$; find a related expression.",
  r"Derive companions: $\cos^2=1-\sin^2$, $\text{cosec}-\cot=\frac{1}{k}$; eliminate $\theta$."),
]

# ---------------------------------------------------------------- solved examples
solved = []

solved.append(Q("trig-s01",
r"Find the value of $\dfrac{2\tan30^\circ}{1-\tan^230^\circ}$.",
[(r"$\sqrt{3}$", sp.sqrt(3)), (r"$\frac{1}{\sqrt{3}}$", 1 / sp.sqrt(3)), ("1", 1), (r"$\frac{\sqrt{3}}{2}$", sp.sqrt(3) / 2)], sp.sqrt(3),
r"""
$\tan30^\circ=\frac{1}{\sqrt3}$:

$\dfrac{2/\sqrt3}{1-\frac13}=\dfrac{2/\sqrt3}{2/3}=\dfrac{3}{\sqrt3}=\sqrt3$.
""",
r"Recognise the form: $\frac{2t}{1-t^2}=\tan2\theta$ with $\theta=30^\circ$ → $\tan60^\circ=\sqrt3$, no fractions at all.",
"easy", "trig-ratios", "standard values in double-angle form", 35))

solved.append(Q("trig-s02",
r"If $\cos\theta=\dfrac{7}{25}$, then the value of $\tan\theta$ is:",
[(r"$\frac{24}{7}$", sp.Rational(24, 7)), (r"$\frac{7}{24}$", sp.Rational(7, 24)), (r"$\frac{25}{24}$", sp.Rational(25, 24)), (r"$\frac{24}{25}$", sp.Rational(24, 25))], sp.Rational(24, 7),
r"""
Adjacent side $=7$, hypotenuse $=25$; opposite $=\sqrt{25^2-7^2}=\sqrt{576}=24$.

$\tan\theta=\frac{24}{7}$.
""",
r"7-24-25 triplet: see 7 and 25, write 24 instantly. Trap: $\frac{7}{24}$ is $\cot\theta$.",
"easy", "trig-valueput", "given ratio → triplet triangle", 30))

solved.append(Q("trig-s03",
r"The value of $\tan1^\circ\tan2^\circ\tan3^\circ\cdots\tan89^\circ$ is:",
["1", "0", r"$\sqrt{3}$", "89"], "1",
r"""
Pair $\tan\theta$ with $\tan(90^\circ-\theta)=\cot\theta$: each pair multiplies to 1.

44 such pairs plus $\tan45^\circ=1$ give the product 1.
""",
r"Every angle pairs with its complement; middle term is $\tan45^\circ=1$. Product $=1$.",
"medium", "trig-complementary", "tan product 1 to 89", 40))

solved.append(Q("trig-s04",
r"The value of $(\text{cosec}\theta-\sin\theta)(\sec\theta-\cos\theta)(\tan\theta+\cot\theta)$ is:",
["1", "0", "2", r"$\tan\theta$"], "1",
r"""
Write everything over sin/cos:

$\text{cosec}\theta-\sin\theta=\frac{\cos^2\theta}{\sin\theta},\quad
\sec\theta-\cos\theta=\frac{\sin^2\theta}{\cos\theta},\quad
\tan\theta+\cot\theta=\frac{1}{\sin\theta\cos\theta}$.

Product $=\frac{\cos^2\theta}{\sin\theta}\cdot\frac{\sin^2\theta}{\cos\theta}\cdot\frac{1}{\sin\theta\cos\theta}=1$.
""",
r"Reduce each bracket to a single fraction; the $\sin^2\cos^2$ cancels completely → 1. (Check at $45^\circ$: $(\frac{1}{\sqrt2})^2\times2=1$.)",
"medium", "trig-identities", "cosec-sin / sec-cos product identity", 50))

solved.append(Q("trig-s05",
r"The greatest value of $3\sin\theta+4\cos\theta+5$ (for $0^\circ\le\theta\le90^\circ$) is:",
["10", "5", "12", "9"], "10",
r"""
$a\sin\theta+b\cos\theta$ peaks at $\sqrt{a^2+b^2}$: here $\sqrt{3^2+4^2}=5$ (at $\tan\theta=\frac34$).

So the greatest value of the expression is $5+5=10$.
""",
r"$\sqrt{a^2+b^2}=5$ for the trig part, then add the constant: $5+5=10$. Trap: 12 (added $3+4+5$ directly).",
"medium", "trig-maxmin", "max of a sin + b cos + c", 45))

# ---------------------------------------------------------------- practice
pr = []

pr.append(Q("trig-q01",
r"The value of $\sin30^\circ+\cos60^\circ+\cot45^\circ$ is:",
["2", "1", "3", (r"$\frac{\sqrt{3}}{2}$", sp.sqrt(3) / 2)], "2",
r"$\frac12+\frac12+1=2$.",
r"Read the table: $\frac12+\frac12+1=2$. $\cot45^\circ=1$, not 0.",
"easy", "trig-ratios", "standard values sum", 25))

pr.append(Q("trig-q02",
r"The value of $\sec^2\theta-\tan^2\theta-\sin^2\theta$ is:",
[(r"$\cos^2\theta$", sp.cos(sp.pi / 7) ** 2), ("1", 1), ("0", 0), (r"$\sin^2\theta$", sp.sin(sp.pi / 7) ** 2)], sp.cos(sp.pi / 7) ** 2,
r"$\sec^2\theta-\tan^2\theta=1$, so the expression $=1-\sin^2\theta=\cos^2\theta$.",
r"$\sec^2-\tan^2=1$ (identity pair), then $1-\sin^2=\cos^2$.",
"easy", "trig-identities", "sec-tan identity pair", 30))

pr.append(Q("trig-q03",
r"The value of $\sin60^\circ\cos30^\circ+\cos60^\circ\sin30^\circ$ is:",
["1", (r"$\frac{\sqrt{3}}{2}$", sp.sqrt(3) / 2), (r"$\frac{1}{2}$", sp.Rational(1, 2)), (r"$\frac{3}{4}$", sp.Rational(3, 4))], "1",
r"$\frac{\sqrt3}{2}\cdot\frac{\sqrt3}{2}+\frac12\cdot\frac12=\frac34+\frac14=1$.",
r"This is $\sin(60+30)=\sin90^\circ=1$ — recognise the sine-addition shape instead of multiplying.",
"easy", "trig-ratios", "standard values product sum", 30))

pr.append(Q("trig-q04",
r"If $\sin\theta=\dfrac{5}{13}$, then $\tan\theta$ equals:",
[(r"$\frac{5}{12}$", sp.Rational(5, 12)), (r"$\frac{12}{5}$", sp.Rational(12, 5)), (r"$\frac{12}{13}$", sp.Rational(12, 13)), (r"$\frac{5}{13}$", sp.Rational(5, 13))], sp.Rational(5, 12),
r"Adjacent $=\sqrt{13^2-5^2}=12$, so $\tan\theta=\frac{5}{12}$.",
r"5-12-13 triplet → $\frac{5}{12}$. Trap: $\frac{12}{5}$ is $\cot\theta$.",
"easy", "trig-valueput", "given sin → tan by triplet", 25))

pr.append(Q("trig-q05",
r"If $\tan\theta=\dfrac{3}{4}$, the value of $\dfrac{\sin\theta+\cos\theta}{\sin\theta-\cos\theta}$ is:",
["-7", "7", (r"$-\frac{1}{7}$", sp.Rational(-1, 7)), (r"$\frac{7}{4}$", sp.Rational(7, 4))], "-7",
r"""
Divide numerator and denominator by $\cos\theta$:

$\dfrac{\tan\theta+1}{\tan\theta-1}=\dfrac{\frac34+1}{\frac34-1}=\dfrac{7/4}{-1/4}=-7$.
""",
r"Divide through by $\cos\theta$: $(t+1)/(t-1)$ with $t=\frac34$ → $-7$. (Same trick works for any sin/cos ratio expression.)",
"medium", "trig-valueput", "divide by cos to use tan", 40))

pr.append(Q("trig-q06",
r"If $\sin(40^\circ+\theta)=\cos(30^\circ+\theta)$, where both angles are acute, then $\theta$ equals:",
U("°", 10, 20, 5, 15), 10,
r"The angles must add to $90^\circ$: $(40+\theta)+(30+\theta)=90\Rightarrow2\theta=20\Rightarrow\theta=10^\circ$.",
r"Sum to 90: $70+2\theta=90$ → $\theta=10^\circ$. Trap: 20 (forgot to halve).",
"medium", "trig-complementary", "sin A = cos B angle equation", 35))

pr.append(Q("trig-q07",
r"If $\sin\theta+\sin^2\theta=1$, then the value of $\cos^2\theta+\cos^4\theta$ is:",
["1", "0", "2", (r"$\frac{1}{2}$", sp.Rational(1, 2))], "1",
r"""
From the condition, $\sin^2\theta=1-\sin\theta$, so $\cos^2\theta=1-\sin^2\theta=\sin\theta$.

Then $\cos^4\theta=\sin^2\theta=1-\sin\theta$.

Sum $=\sin\theta+1-\sin\theta=1$.
""",
r"$\cos^2=\sin$ and $\cos^4=\sin^2=1-\sin$ → total 1, without ever finding $\theta$.",
"medium", "trig-identities", "condition sin+sin^2=1", 45))

pr.append(Q("trig-q08",
r"The minimum value of $\sin\theta+\cos\theta$ for $0^\circ\le\theta\le90^\circ$ is:",
["1", (r"$\sqrt{2}$", sp.sqrt(2)), "0", (r"$\frac{1}{\sqrt{2}}$", 1 / sp.sqrt(2))], "1",
r"$\sin\theta+\cos\theta$ ranges from 1 (at $\theta=0^\circ$ or $90^\circ$) to $\sqrt2$ (at $45^\circ$). The minimum is 1.",
r"Range $[1,\sqrt2]$: min 1, max $\sqrt2$. Trap: $\sqrt2$ is the **maximum**.",
"medium", "trig-maxmin", "min of sin+cos", 30))

pr.append(Q("trig-q09",
r"The value of $\tan15^\circ\tan25^\circ\tan45^\circ\tan65^\circ\tan75^\circ$ is:",
["1", "0", (r"$\sqrt{3}$", sp.sqrt(3)), "5"], "1",
r"$\tan\theta\tan(90-\theta)=1$ pairs: $(\tan15\tan75)(\tan25\tan65)(\tan45)=1\cdot1\cdot1=1$.",
r"Complementary pairs collapse; $\tan45^\circ=1$ stands alone.",
"medium", "trig-complementary", "tan product with complementary pairs", 40))

pr.append(Q("trig-q10",
r"The value of $2(\sin^6\theta+\cos^6\theta)-3(\sin^4\theta+\cos^4\theta)+1$ is:",
["0", "1", "2", (r"$\sin^2\theta$", sp.sin(sp.pi / 7) ** 2)], "0",
r"""
Use $\sin^6+\cos^6=1-3s^2c^2$ and $\sin^4+\cos^4=1-2s^2c^2$ (where $s^2c^2=\sin^2\theta\cos^2\theta$):

$2(1-3s^2c^2)-3(1-2s^2c^2)+1=2-3+1+0=0$.
""",
r"The $s^2c^2$ terms cancel exactly: $-6+6=0$ → answer 0 for every $\theta$. (Try $\theta=45^\circ$ to confirm.)",
"medium", "trig-identities", "sin^6+cos^6 chain", 50))

pr.append(Q("trig-q11",
r"If $\cos\theta=\dfrac{12}{13}$, then $\text{cosec}\,\theta$ equals:",
[(r"$\frac{13}{5}$", sp.Rational(13, 5)), (r"$\frac{5}{13}$", sp.Rational(5, 13)), (r"$\frac{13}{12}$", sp.Rational(13, 12)), (r"$\frac{12}{5}$", sp.Rational(12, 5))], sp.Rational(13, 5),
r"Opposite $=\sqrt{13^2-12^2}=5$, so $\sin\theta=\frac5{13}$ and $\text{cosec}\theta=\frac{13}{5}$.",
r"5-12-13: $\sin=\frac5{13}$ → cosec $=\frac{13}{5}$ (flip). Trap: $\frac{13}{12}$ is $\sec\theta$.",
"medium", "trig-valueput", "given cos → cosec", 30))

pr.append(Q("trig-q12",
r"The minimum value of $4\tan^2\theta+9\cot^2\theta$ (for acute $\theta$) is:",
["12", "13", "36", "6"], "12",
r"""
By AM–GM, $4\tan^2\theta+9\cot^2\theta\ge2\sqrt{4\times9}=12$,

with equality when $2\tan\theta=3\cot\theta$, i.e. $\tan^2\theta=\frac32$ (reachable since tan is unbounded).
""",
r"$2\sqrt{ab}=2\sqrt{36}=12$. Trap: 6 is $\sqrt{ab}$ (forgot to double), 13 is $a+b$.",
"hard", "trig-maxmin", "AM-GM min of tan^2+cot^2", 45))

pr.append(Q("trig-q13",
r"If $\text{cosec}\theta+\cot\theta=3$, then $\sin\theta$ equals:",
[(r"$\frac{3}{5}$", sp.Rational(3, 5)), (r"$\frac{5}{3}$", sp.Rational(5, 3)), (r"$\frac{4}{5}$", sp.Rational(4, 5)), (r"$\frac{1}{3}$", sp.Rational(1, 3))], sp.Rational(3, 5),
r"""
$\text{cosec}\theta-\cot\theta=\frac13$ (reciprocal pair). Adding the two:

$2\,\text{cosec}\theta=\frac{10}{3}\Rightarrow\text{cosec}\theta=\frac53\Rightarrow\sin\theta=\frac35$.
""",
r"Companion is $\frac1k=\frac13$; average the pair: cosec $=\frac{3+\frac13}{2}=\frac53$ → $\sin=\frac35$.",
"medium", "trig-valueput", "cosec+cot given", 50))

pr.append(Q("trig-q14",
r"The expression $(\tan\theta+\sec\theta-1)(\tan\theta-\sec\theta+1)$ equals:",
[(r"$2(\sec\theta-1)$", 2 * (sp.sec(sp.pi / 5) - 1)), ("1", 1), (r"$2\sec\theta$", 2 * sp.sec(sp.pi / 5)), (r"$\tan^2\theta$", sp.tan(sp.pi / 5) ** 2)], 2 * (sp.sec(sp.pi / 5) - 1),
r"""
Write the brackets as $[t+(s-1)][t-(s-1)]=t^2-(s-1)^2$ where $t=\tan\theta$, $s=\sec\theta$.

$=t^2-s^2+2s-1=-1+2s-1=2(\sec\theta-1)$, using $s^2-t^2=1$.
""",
r"Difference of squares, then $t^2-s^2=-1$: answer $2(\sec\theta-1)$. Quick check at $30^\circ$: LHS $\approx0.309$ = RHS.",
"hard", "trig-identities", "tan-sec difference of squares", 60))

pr.append(Q("trig-q15",
r"If $2\sin^2\theta+7\cos^2\theta=6$ and $0^\circ<\theta<90^\circ$, then $\tan\theta$ equals:",
[(r"$\frac{1}{2}$", sp.Rational(1, 2)), ("2", 2), (r"$\frac{1}{4}$", sp.Rational(1, 4)), (r"$\frac{1}{5}$", sp.Rational(1, 5))], sp.Rational(1, 2),
r"""
Write the left side as $2(\sin^2\theta+\cos^2\theta)+5\cos^2\theta=2+5\cos^2\theta$.

So $2+5\cos^2\theta=6\Rightarrow\cos^2\theta=\frac45$, hence $\sin^2\theta=\frac15$.

$\tan^2\theta=\frac{\sin^2\theta}{\cos^2\theta}=\frac{1/5}{4/5}=\frac14\Rightarrow\tan\theta=\frac12$ (acute).
""",
r"Anchor to $a(\sin^2+\cos^2)+(b-a)\cos^2$: solve for $\cos^2$, then $\tan^2=\frac{1-\cos^2}{\cos^2}$. Traps: 2 (reciprocal), $\frac14$ ($\tan^2$, forgot the root).",
"hard", "trig-identities", "weighted sin^2+cos^2 equation", 70))

topic = {
    "id": "trigonometry",
    "sectionId": "quant",
    "title": "Trigonometry",
    "order": 16,
    "importance": "high",
    "avgQuestions": {"tier1": 3, "tier2": 4},
    "summary": "Ratios, the standard-value table, the three identities, complementary angles, value-putting and max-min values. "
               "Tier 1 reliably holds 2-4 trig questions and they fall almost mechanically to the value table, one identity, or a 3-4-5 style triangle — among the cheapest marks in the paper.",
    "subtopics": subtopics,
    "pyqPatterns": patterns,
    "solvedExamples": solved,
    "practice": pr,
}

if __name__ == "__main__":
    write_topic(topic)
