"""Phase-2 deep content for quant/trigonometry — complementary, valueput, maxmin."""
import math

from fractions import Fraction as F

from _lib import Sub


# ---------------- trig-complementary ----------------

def build_complementary():
    S = Sub("trig-complementary")

    S.notes = r"""### The complementary pair rules
For any angle $\theta$: $\sin(90^\circ - \theta) = \cos\theta$, $\tan(90^\circ - \theta) = \cot\theta$, $\sec(90^\circ - \theta) = \cosec\theta$ — and each reversed. The switch only happens between the three PAIRS (sin↔cos, tan↔cot, sec↔cosec); sin to sin at $90^\circ - \theta$ never changes function.
$$\sin\theta = \cos(90^\circ - \theta),\quad \tan\theta = \cot(90^\circ - \theta),\quad \sec\theta = \cosec(90^\circ - \theta)$$

### The working algorithm
1. Scan the expression for angles that sum to $90^\circ$ in pairs ($20^\circ$ & $70^\circ$, $35^\circ$ & $55^\circ$, $5^\circ$ & $85^\circ$...).
2. Convert ONE angle of each pair so both terms share an angle: $\sec 55^\circ = \cosec 35^\circ = \frac{1}{\sin 35^\circ}$.
3. Fractions collapse ($x \cdot \frac1x$), products of the form $\tan\theta\cot\theta$ become 1, and the expression evaluates to a small constant.

### Product chains
Products like $\tan 5^\circ \tan 25^\circ \tan 45^\circ \tan 65^\circ \tan 85^\circ$ pair into $\tan\theta \cdot \tan(90^\circ - \theta) = \tan\theta\cot\theta = 1$ with $\tan 45^\circ = 1$ left over. The full run $\tan 1^\circ \tan 2^\circ \cdots \tan 89^\circ$ is 1 for the same reason — 44 cancelling pairs around the middle term.

### Finding the angle itself
Equations pairing different functions at related angles resolve by forcing the SAME function: $\sin 3A = \cos(A - 10^\circ)$ becomes $\sin 3A = \sin(90^\circ - (A - 10^\circ))$, so the angles match: $3A = 100^\circ - A$. Equivalently, complementary-function arguments must sum to $90^\circ$: $\sec 2\theta = \cosec(\theta + 30^\circ)$ gives $2\theta + \theta + 30^\circ = 90^\circ$.

### The tan 45° anchor and half-chain variants
$\tan 45^\circ = 1$ is the middle term of every full chain and the most common "unpaired" value in short products. Half-chains behave the same: $\tan 10^\circ \tan 20^\circ \tan 70^\circ \tan 80^\circ = (10,80)(20,70) = 1$, and cot chains like $\cot 15^\circ \cot 35^\circ \cot 55^\circ \cot 75^\circ$ collapse identically because complementary cots are still reciprocals. One caution: the collapse needs PAIRS summing to $90^\circ$ — if a product holds $\tan 20^\circ \tan 50^\circ \tan 40^\circ$, the $20/70$ pairing is absent, so convert through cot and simplify before trusting a pattern.

### Quick revision
- Only three switches exist: sin↔cos, tan↔cot, sec↔cosec, argument → $90^\circ - x$.
- Hunt pairs summing to $90^\circ$; convert, then cancel.
- $\tan\theta \cdot \tan(90^\circ - \theta) = 1$; full chains $\tan 1^\circ \cdots \tan 89^\circ = 1$.
- Angle equations: set complementary arguments to sum to $90^\circ$, solve linearly.
"""

    S.pattern("trig-co-p1", "Pair conversion to collapse a sum", "very common",
      "A short sum/product whose angles pair to 90 degrees (35 & 55, 20 & 70...).",
      r"$\sin\theta = \cos(90^\circ-\theta)$ etc.; convert one of each pair and cancel.",
      r"""1. List the angles; find the 90-degree pairs.
2. Convert the odd-pair function: $\sec 55^\circ = \frac{1}{\cos 55^\circ} = \frac{1}{\sin 35^\circ}$.
3. Each term becomes $x \cdot \frac1x = 1$; read the sum.

Why: the exam numbers never share a function until you flip one — that flip is the entire question.""",
      "The value of $\\sin 35^\\circ \\sec 55^\\circ + \\cos 35^\\circ \\cosec 55^\\circ$ is:",
      r"$\sec 55^\circ = \frac{1}{\sin 35^\circ}$ and $\cosec 55^\circ = \frac{1}{\cos 35^\circ}$: sum $= 1 + 1 = 2$.")
    S.pattern("trig-co-p2", "Product chains pairing to 1", "common",
      "Long products of tangents/cots at many small angles, with 45 in the middle or symmetric ends.",
      r"$\tan\theta \cdot \tan(90^\circ - \theta) = 1$; pair from the ends inward.",
      r"""1. Pair $\theta$ with $90^\circ - \theta$ from both ends.
2. Each pair contributes 1; any middle $\tan 45^\circ$ also contributes 1.
3. The product is 1 unless an unpaired angle remains — rare, and then it is stated.

Why: complementary tangents are reciprocals, so the chain self-destructs into a product of ones.""",
      "The value of $\\tan 5^\\circ \\tan 25^\\circ \\tan 45^\\circ \\tan 65^\\circ \\tan 85^\\circ$ is:",
      r"Pairs: $\tan 5 \tan 85 = 1$, $\tan 25 \tan 65 = 1$, $\tan 45 = 1$. Product $= 1$.")
    S.pattern("trig-co-p3", "Finding the angle from complementary equality", "very common",
      "'If sin 3A = cos(A − 10), find A' — different functions at related angles, one unknown angle.",
      r"Force the same function: $\cos x = \sin(90^\circ - x)$; then equate arguments. Shortcut: complementary arguments sum to 90.",
      r"""1. Rewrite so both sides carry the same function.
2. Equate the arguments (or set them to sum to $90^\circ$ for complementary pairs).
3. Solve the resulting linear equation; verify the angle keeps every argument in range.

Why: equality of different functions is meaningless until one side is converted — then it is class-8 algebra.""",
      "If $\\sin 3A = \\cos(A - 10^\\circ)$, the value of $A$ is:",
      r"$\cos(A - 10^\circ) = \sin(90^\circ - A + 10^\circ)$, so $3A = 100^\circ - A$ → $A = 25^\circ$.")
    S.pattern("trig-co-p4", "Difference of complementary twins = 0", "common",
      "'Find cos 50° − sin 40°' style — two terms that LOOK unrelated.",
      r"$\sin(90^\circ - \theta) = \cos\theta$: the two terms are identical; the difference is 0.",
      r"""1. Check the arguments: $50 + 40 = 90$ → twins.
2. $\sin 40^\circ = \cos 50^\circ$; the expression is zero.
3. Same trick for $\cosec 68^\circ - \sec 22^\circ$, $\tan 81^\circ - \cot 9^\circ$.

Why: the question only wins if you don't check for the 90-degree sum — checking it ends the question instantly.""",
      "The value of $\\cosec 68^\\circ - \\sec 22^\\circ$ is:",
      r"$\sec 22^\circ = \cosec(90^\circ - 22^\circ) = \cosec 68^\circ$; difference $= 0$.")

    # ---- practice ----
    assert 50 + 40 == 90
    S.q("trig-co-p4", "easy", "The value of $\\cos 50^\\circ - \\sin 40^\\circ$ is:",
        ["$0$", "$1$", "$\\frac{1}{2}$", "$\\sqrt{2}$"], "$0$",
        r"""$50^\circ + 40^\circ = 90^\circ$: $\sin 40^\circ = \cos 50^\circ$; difference $= 0$.""",
        r"Twins cancel. Trap: $1$ or $\frac12$ — treating them as unrelated values.", 25)
    assert 35 + 55 == 90 and 1 + 1 == 2
    S.q("trig-co-p1", "medium", "The value of $\\sin 35^\\circ \\sec 55^\\circ + \\cos 35^\\circ \\cosec 55^\\circ$ is:",
        ["$2$", "$1$", "$0$", "$\\sqrt{2}$"], "$2$",
        r"""$\sec 55^\circ = \frac{1}{\cos 55^\circ} = \frac{1}{\sin 35^\circ}$; $\cosec 55^\circ = \frac{1}{\sin 55^\circ} = \frac{1}{\cos 35^\circ}$.

Each product is 1: sum $= 2$.""",
        r"Both flip to reciprocals: $1 + 1 = 2$. Trap: $1$ (cancelling only one pair).", 40)
    assert 68 + 22 == 90
    S.q("trig-co-p4", "easy", "The value of $\\sec 22^\\circ - \\cosec 68^\\circ$ is:",
        ["$0$", "$1$", "$2$", "$\\sec 22^\\circ$"], "$0$",
        r"""$\cosec 68^\circ = \sec(90^\circ - 68^\circ) = \sec 22^\circ$; difference $= 0$.""",
        r"$22 + 68 = 90$: identical twins. Trap: $\sec 22^\circ$ (dropping the second term).", 25)
    assert 5 + 85 == 90 and 25 + 65 == 90
    S.q("trig-co-p2", "medium", "The value of $\\tan 5^\\circ \\tan 25^\\circ \\tan 45^\\circ \\tan 65^\\circ \\tan 85^\\circ$ is:",
        ["$1$", "$0$", "$\\sqrt{3}$", "$5$"], "$1$",
        r"""$\tan 5^\circ \tan 85^\circ = 1$ and $\tan 25^\circ \tan 65^\circ = 1$ (complementary pairs); $\tan 45^\circ = 1$.

Product $= 1$.""",
        r"Pair the ends: $1$. Trap: $0$ — nothing here is zero; every factor is finite and positive.", 40)
    assert 12 + 78 == 90 and F(1, 3) * F(3, 1) == 1
    S.q("trig-co-p2", "medium", "The value of $\\tan 12^\\circ \\tan 30^\\circ \\tan 60^\\circ \\tan 78^\\circ$ is:",
        ["$1$", "$\\frac{1}{\\sqrt{3}}$", "$\\sqrt{3}$", "$\\frac{1}{3}$"], "$1$",
        r"""$\tan 12^\circ \tan 78^\circ = 1$; $\tan 30^\circ \tan 60^\circ = \frac{1}{\sqrt3} \times \sqrt3 = 1$.

Product $= 1$.""",
        r"Two pairs: $1 \times 1 = 1$. Trap: $\frac{1}{3}$ (squaring the 30-60 pair instead of multiplying).", 40)
    assert 3 * 25 == 75 and 75 + 15 == 90
    S.q("trig-co-p3", "medium", "If $\\sin 3A = \\cos(A - 10^\\circ)$, the value of $A$ is:",
        ["$25^\\circ$", "$20^\\circ$", "$30^\\circ$", "$15^\\circ$"], "$25^\\circ$",
        r"""Complementary arguments: $3A + (A - 10^\circ) = 90^\circ$ → $4A = 100^\circ$ → $A = 25^\circ$.""",
        r"$4A = 100$: $A = 25^\circ$. Trap: $20^\circ$ (dropping the $-10^\circ$).", 40)
    assert 2 * 20 + 20 + 30 == 90
    S.q("trig-co-p3", "medium", "If $\\sec 2\\theta = \\cosec(\\theta + 30^\\circ)$, the value of $\\theta$ is:",
        ["$20^\\circ$", "$30^\\circ$", "$15^\\circ$", "$25^\\circ$"], "$20^\\circ$",
        r"""$\sec x = \cosec(90^\circ - x)$: the arguments must satisfy $2\theta + \theta + 30^\circ = 90^\circ$.

$3\theta = 60^\circ$ → $\theta = 20^\circ$.""",
        r"$3\theta = 60$: $\theta = 20^\circ$. Trap: $30^\circ$ (setting $2\theta = \theta + 30$, the wrong pairing).", 40)
    assert 30 + 30 + 30 == 90
    S.q("trig-co-p3", "easy", "If $\\tan\\theta = \\cot(30^\\circ + \\theta)$, the value of $\\theta$ is:",
        ["$30^\\circ$", "$45^\\circ$", "$15^\\circ$", "$60^\\circ$"], "$30^\\circ$",
        r"""Complementary arguments: $\theta + 30^\circ + \theta = 90^\circ$ → $2\theta = 60^\circ$ → $\theta = 30^\circ$.""",
        r"$2\theta = 60$: $\theta = 30^\circ$. Trap: $45^\circ$ (tan $=$ cot only at 45 when the angles are EQUAL, not complementary).", 30)
    assert 1 + 44 + 44 == 89
    S.q("trig-co-p2", "hard", "The value of $\\tan 1^\\circ \\tan 2^\\circ \\tan 3^\\circ \\cdots \\tan 89^\\circ$ is:",
        ["$1$", "$0$", "$89$", "$\\sqrt{3}$"], "$1$",
        r"""Pair $1^\circ$ with $89^\circ$, $2^\circ$ with $88^\circ$, ..., $44^\circ$ with $46^\circ$: 44 pairs each multiplying to 1.

$\tan 45^\circ = 1$ remains in the middle. Product $= 1$.""",
        r"44 cancelling pairs + $\tan 45^\circ$: product $1$. Trap: $0$ — no factor is zero (tan 0 is absent).", 55)
    assert 15 + 75 == 90 and 35 + 55 == 90
    S.q("trig-co-p1", "medium", "The value of $\\cot 15^\\circ \\cot 35^\\circ \\cot 55^\\circ \\cot 75^\\circ$ is:",
        ["$1$", "$0$", "$\\sqrt{3}$", "$\\cot 15^\\circ$"], "$1$",
        r"""Complementary cots are reciprocals: $\cot 15^\circ \cot 75^\circ = 1$ (since $15 + 75 = 90$) and $\cot 35^\circ \cot 55^\circ = 1$.

Product $= 1$.""",
        r"Pairs $(15, 75)$ and $(35, 55)$: $1 \times 1 = 1$. Trap: assuming cot-cot pairs don't cancel — complementary cots are still reciprocals.", 40)
    assert 27 + 63 == 90 and 35 + 55 == 90
    S.q("trig-co-p2", "medium", "The value of $\\tan 27^\\circ \\tan 35^\\circ \\tan 45^\\circ \\tan 55^\\circ \\tan 63^\\circ$ is:",
        ["$1$", "$0$", "$45$", "$\\sqrt{3}$"], "$1$",
        r"""$27 + 63 = 90$ and $35 + 55 = 90$: both pairs multiply to 1; $\tan 45^\circ = 1$.

Product $= 1$.""",
        r"Two complementary pairs + the 45° anchor: $1$. Trap: $0$ — no factor vanishes.", 40)
    assert 14 + 76 == 90 and 31 + 59 == 90
    S.q("trig-co-p1", "hard", "The value of $\\sin^2 14^\\circ + \\sin^2 31^\\circ + \\sin^2 59^\\circ + \\sin^2 76^\\circ$ is:",
        ["$2$", "$1$", "$4$", "$\\sqrt{2}$"], "$2$",
        r"""$\sin 76^\circ = \cos 14^\circ$ and $\sin 59^\circ = \cos 31^\circ$ (each pair sums to $90^\circ$).

So the sum $= (\sin^2 14^\circ + \cos^2 14^\circ) + (\sin^2 31^\circ + \cos^2 31^\circ) = 1 + 1 = 2$.""",
        r"Re-pair into two $\sin^2 + \cos^2 = 1$ groups. Trap: $1$ — there are TWO independent pairs here.", 55)
    return S


# ---------------- trig-valueput ----------------

def build_valueput():
    S = Sub("trig-valueput")

    S.notes = r"""### Putting values into expressions
Two flavours: (a) the angle is a STANDARD one ($30^\circ, 45^\circ, 60^\circ$) — read the table and compute; (b) an angle satisfying a condition ("$\tan\theta = 2$") — reduce the expression to a single ratio, then substitute. Both end in one small fraction; the work is entirely in the reduction.
$$2\tan^2 45^\circ + \cos^2 30^\circ - \sin^2 60^\circ = 2 + \tfrac34 - \tfrac34 = 2$$

### The sin+cos condition web
Given $\sin\theta + \cos\theta = m$:
- $\sin\theta\cos\theta = \frac{m^2 - 1}{2}$ (square the given).
- $\sin\theta - \cos\theta = \sqrt{2 - m^2}$ (from the difference squared).
- $\sin^3\theta + \cos^3\theta = m^3 - 3\sin\theta\cos\theta \cdot m$ via $x^3 + y^3 = (x+y)(x^2 - xy + y^2)$.
Special anchors: $m = \sqrt2$ gives $\sin\theta\cos\theta = \frac12$ ($\theta = 45^\circ$); $m = 1$ gives $\sin\theta\cos\theta = 0$ (endpoints).

### cot/tan triplet substitution
$\cot\theta = \frac{21}{20}$ means a 20-21-29 triangle: $\cos\theta = \frac{21}{29}$ directly. Any cot/tan given as a fraction of smallish integers is a triangle waiting to be drawn — faster than identities and immune to sign slips.

### Reducing linear fractions in sin and cos
$\frac{a\sin\theta + b\cos\theta}{c\cos\theta + d\sin\theta} \to \frac{a\tan\theta + b}{c + d\tan\theta}$ — divide by $\cos\theta$, substitute $t$, simplify. Works the same with $\cot$ if the expression is cot-heavy.

### The cosec/cot condition twin
Given $\cosec\theta + \cot\theta = k$: its conjugate $\cosec\theta - \cot\theta = \frac{1}{k}$ (product 1), so $\cosec\theta = \frac{k + \frac1k}{2}$ and $\cot\theta = \frac{k - \frac1k}{2}$. Since $\cosec^2 - \cot^2 = 1$, this family is the sec±tan engine wearing a different coat — and it finishes with $\sin\theta = \frac{2k}{k^2 + 1}$ directly. Example: $\cosec\theta + \cot\theta = 3$ gives $\cosec\theta = \frac{3 + \frac13}{2} = \frac53$, so $\sin\theta = \frac35$ — a 3-4-5 triangle in disguise.

### Reading the options like a setter
Options in this family are built from predictable slips: substituting the reciprocal of the given tan, forgetting the constant $+b$ term, dropping a minus sign when the denominator is negative, or reporting $\tan^2$ when $\tan$ was asked. After computing, name the slip each wrong option encodes — if you cannot, re-check your own arithmetic. And keep every substitution exact: $\tan\theta = \frac43$ stays a fraction; a decimal 1.33 is how sign and size errors sneak in.

### Quick revision
- Table entries at $0/30/45/60/90$; reduce everything to them.
- $\sin\cos = \frac{(\sin+\cos)^2 - 1}{2}$; $(\sin-\cos)^2 = 2 - (\sin+\cos)^2$.
- cot given as $\frac{p}{q}$ → triangle $(q, p, \sqrt{p^2+q^2})$.
- Divide linear fractions by $\cos\theta$; one substitution finishes them.
"""

    S.pattern("trig-vp-p1", "Standard angles in an expression", "very common",
      "An arithmetic expression in sin/cos/tan of 0/30/45/60/90 asked as a single value.",
      r"Substitute table values; simplify with exact fractions.",
      r"""1. Replace each ratio with its table entry (reciprocal functions included).
2. Compute with fractions ($\frac14, \frac34, \frac12$) — no decimals.
3. Cancel before adding where possible.

Why: it is pure table recall plus one tidy computation — the marks are in avoiding the $\sin^2 60$ vs $\sin 60$ slips.""",
      "The value of $2\\tan^2 45^\\circ + \\cos^2 30^\\circ - \\sin^2 60^\\circ$ is:",
      r"$2(1) + \frac34 - \frac34 = 2$. The last two terms cancel exactly.")
    S.pattern("trig-vp-p2", "sin+cos given → products and differences", "very common",
      "'sinθ + cosθ = m' given; sinθcosθ, sinθ − cosθ, or a cubic combo asked.",
      r"$\sin\cos = \frac{m^2-1}{2}$; $(\sin-\cos)^2 = 2 - m^2$; cube sums via $x^3+y^3 = (x+y)(x^2-xy+y^2)$.",
      r"""1. Square the given: $m^2 = 1 + 2\sin\theta\cos\theta$ → the product.
2. Difference: square root of $2 - m^2$ (positive since sin > cos or vice versa is possible — check signs only if options demand).
3. Cubes: factor as $(\sin + \cos)(1 - \sin\cos)$ and substitute both knowns.

Why: every quantity in this family is a symmetric function of $\sin$ and $\cos$ — the pair $(m, \sin\cos)$ determines all of them.""",
      "If $\\sin\\theta + \\cos\\theta = \\sqrt{2}$, the value of $\\sin\\theta\\cos\\theta$ is:",
      r"$2 = 1 + 2\sin\theta\cos\theta$ → $\sin\theta\cos\theta = \frac12$ (indeed $\theta = 45^\circ$).")
    S.pattern("trig-vp-p3", "tan/cot condition into a linear fraction", "very common",
      "'If 5 tanθ = 4' or tanθ = p/q; a fraction like (5sinθ − 3cosθ)/(5sinθ + 3cosθ) asked.",
      r"Divide by $\cos\theta$; the fraction becomes $\frac{5t - 3}{5t + 3}$ in $t = \tan\theta$.",
      r"""1. Convert the condition to $t = \tan\theta$ first.
2. Divide numerator and denominator by $\cos\theta$.
3. Substitute and simplify the single fraction exactly.

Why: the coefficients of the question are the SAME numbers as in the fraction — substitution must be mechanical, not improvised.""",
      "If $5\\tan\\theta = 4$, the value of $\\frac{5\\sin\\theta - 3\\cos\\theta}{5\\sin\\theta + 3\\cos\\theta}$ is:",
      r"$= \frac{5 \times \frac45 - 3}{5 \times \frac45 + 3} = \frac{1}{7}$. (Divide top and bottom by $\cos\theta$ first.)")
    S.pattern("trig-vp-p4", "cot/tan fraction → triangle → ratio", "common",
      "cotθ or tanθ given as a fraction like 21/20; a DIFFERENT ratio (cos, sin, sec) asked.",
      r"Draw the triangle with legs $q, p$; hyp $= \sqrt{p^2+q^2}$; read the asked ratio.",
      r"""1. $\cot\theta = \frac{21}{20}$ → adj 21, opp 20 → hyp 29.
2. Read the requested ratio from the same triangle.
3. Triplet families (3-4-5, 5-12-13, 8-15-17, 20-21-29) cover the exams.

Why: the condition fully determines the shape — one drawing replaces three identity manipulations.""",
      "If $\\cot\\theta = \\frac{21}{20}$ ($\\theta$ acute), the value of $\\cos\\theta$ is:",
      r"Triangle 20-21-29: $\cos\theta = \frac{\text{adj}}{\text{hyp}} = \frac{21}{29}$.")

    # ---- practice ----
    assert 2 * 1 + F(3, 4) - F(3, 4) == 2
    S.q("trig-vp-p1", "medium", "The value of $2\\tan^2 45^\\circ + \\cos^2 30^\\circ - \\sin^2 60^\\circ$ is:",
        ["$2$", "$1$", "$3$", "$\\frac{3}{2}$"], "$2$",
        r"""$2(1)^2 + \left(\frac{\sqrt3}{2}\right)^2 - \left(\frac{\sqrt3}{2}\right)^2 = 2 + \frac34 - \frac34 = 2$.""",
        r"Complementary squares cancel. Trap: $3$ (using $\sin^2 60 = \frac34$ for BOTH terms wrongly) or $\frac32$.", 35)
    assert F(1, 4) + F(1, 4) + 1 == F(3, 2)
    S.q("trig-vp-p1", "easy", "The value of $\\sin^2 30^\\circ + \\cos^2 60^\\circ + \\tan^2 45^\\circ$ is:",
        ["$\\frac{3}{2}$", "$2$", "$1$", "$\\frac{5}{4}$"], "$\\frac{3}{2}$",
        r"""$\sin^2 30^\circ = \frac14$, $\cos^2 60^\circ = \frac14$, $\tan^2 45^\circ = 1$.

Sum $= \frac14 + \frac14 + 1 = \frac32$.""",
        r"$\frac14 + \frac14 + 1 = \frac32$. Trap: $2$ — counting $\tan^2 45^\circ$ twice.", 25)
    assert F(2, 1) ** 2 - 1 == 3 and F(3, 1) == 3
    S.q("trig-vp-p2", "medium", "If $\\sin\\theta + \\cos\\theta = \\sqrt{2}$, the value of $\\sin\\theta\\cos\\theta$ is:",
        ["$\\frac{1}{2}$", "$1$", "$\\frac{\\sqrt{2}}{2}$", "$\\frac{1}{4}$"], "$\\frac{1}{2}$",
        r"""Squaring: $2 = 1 + 2\sin\theta\cos\theta$ → $\sin\theta\cos\theta = \frac12$.""",
        r"$\frac{m^2 - 1}{2} = \frac12$. Trap: $1$ (forgetting to divide by 2).", 35)
    assert 2 * 1 == 2
    S.q("trig-vp-p2", "hard", "If $\\sin\\theta + \\cos\\theta = \\sqrt{2}$, the value of $\\sin\\theta - \\cos\\theta$ is:",
        ["$0$", "$1$", "$\\frac{1}{\\sqrt{2}}$", "$\\sqrt{2}$"], "$0$",
        r"""$(\sin\theta - \cos\theta)^2 = 2 - (\sin\theta + \cos\theta)^2 = 2 - 2 = 0$.

So $\sin\theta = \cos\theta$ — indeed $\theta = 45^\circ$.""",
        r"$\sqrt{2 - 2} = 0$: at $45^\circ$ the difference vanishes. Trap: $1$ (using $2 - m$ instead of $2 - m^2$).", 45)
    assert 5 * F(4, 5) - 3 == 1 and 5 * F(4, 5) + 3 == 7
    S.q("trig-vp-p3", "hard", "If $5\\tan\\theta = 4$, the value of $\\frac{5\\sin\\theta - 3\\cos\\theta}{5\\sin\\theta + 3\\cos\\theta}$ is:",
        ["$\\frac{1}{7}$", "$\\frac{1}{2}$", "$7$", "$\\frac{2}{7}$"], "$\\frac{1}{7}$",
        r"""Divide by $\cos\theta$: $\frac{5\tan\theta - 3}{5\tan\theta + 3} = \frac{4 - 3}{4 + 3} = \frac17$.""",
        r"$\frac{5t - 3}{5t + 3} = \frac{1}{7}$. Trap: $\frac12$ (substituting $t = \frac54$ upside down).", 45)
    assert 3 * 2 + 1 == 7 and 2 + 3 == 5
    S.q("trig-vp-p3", "medium", "If $\\tan\\theta = 2$, the value of $\\frac{3\\sin\\theta + \\cos\\theta}{\\sin\\theta + 3\\cos\\theta}$ is:",
        ["$\\frac{7}{5}$", "$\\frac{5}{7}$", "$\\frac{3}{2}$", "$2$"], "$\\frac{7}{5}$",
        r"""Divide by $\cos\theta$: $\frac{3\tan\theta + 1}{\tan\theta + 3} = \frac{6 + 1}{2 + 3} = \frac75$.""",
        r"$\frac{3t+1}{t+3} = \frac75$. Trap: $\frac57$ — inverting the final fraction.", 35)
    assert 20 ** 2 + 21 ** 2 == 29 ** 2
    S.q("trig-vp-p4", "medium", "If $\\cot\\theta = \\frac{21}{20}$ ($\\theta$ acute), the value of $\\cos\\theta$ is:",
        ["$\\frac{21}{29}$", "$\\frac{20}{29}$", "$\\frac{21}{20}$", "$\\frac{20}{21}$"], "$\\frac{21}{29}$",
        r"""$\cot\theta = \frac{\text{adj}}{\text{opp}} = \frac{21}{20}$ → triangle 20-21-29.

$\cos\theta = \frac{21}{29}$.""",
        r"$\frac{21}{29}$. Trap: $\frac{20}{29}$ — that is $\sin\theta$ (cot's numerator is the ADJACENT side).", 40)
    assert 3 ** 2 + 4 ** 2 == 5 ** 2
    S.q("trig-vp-p4", "easy", "If $\\tan\\theta = \\frac{4}{3}$ ($\\theta$ acute), the value of $\\sec\\theta$ is:",
        ["$\\frac{5}{3}$", "$\\frac{3}{5}$", "$\\frac{5}{4}$", "$\\frac{4}{5}$"], "$\\frac{5}{3}$",
        r"""Triangle 3-4-5 with opp 4, adj 3: $\sec\theta = \frac{\text{hyp}}{\text{adj}} = \frac53$.""",
        r"$\frac53$. Trap: $\frac35$ — sec is hyp/ADJ, not adj/hyp.", 30)
    assert abs(math.sin(math.radians(45)) - 1 / math.sqrt(2)) < 1e-9
    S.q("trig-vp-p2", "medium", "If $\\sin\\theta - \\cos\\theta = 0$ and $\\theta$ is acute, the value of $\\sin\\theta$ is:",
        ["$\\frac{1}{\\sqrt{2}}$", "$\\frac{1}{2}$", "$1$", "$\\frac{\\sqrt{3}}{2}$"], "$\\frac{1}{\\sqrt{2}}$",
        r"""$\sin\theta = \cos\theta$ → $\tan\theta = 1$ → $\theta = 45^\circ$ → $\sin\theta = \frac{1}{\sqrt2}$.""",
        r"$45^\circ$: $\sin = \frac{1}{\sqrt2}$. Trap: $1$ (that is $\sin 90^\circ$).", 30)
    assert 2 * F(4, 5) - 1 == F(3, 5) and 2 + 3 * F(4, 5) == F(22, 5)
    S.q("trig-vp-p3", "medium", "If $2\\tan\\theta = \\frac{8}{5}$, the value of $\\frac{2\\sin\\theta - \\cos\\theta}{2\\cos\\theta + 3\\sin\\theta}$ is:",
        ["$\\frac{3}{22}$", "$\\frac{22}{3}$", "$\\frac{1}{11}$", "$\\frac{5}{22}$"], "$\\frac{3}{22}$",
        r"""$\tan\theta = \frac45$. Divide by $\cos\theta$:

$\frac{2 \times \frac45 - 1}{2 + 3 \times \frac45} = \frac{\frac35}{\frac{22}{5}} = \frac{3}{22}$.""",
        r"$\frac{2t - 1}{2 + 3t} = \frac{3}{22}$. Trap: $\frac{22}{3}$ — the fraction inverted.", 45)
    assert 3 + 4 == 7 and 4 - 3 == 1
    S.q("trig-vp-p2", "medium", "If $\\sin\\theta + \\cos\\theta = \\frac{7}{5}$, the value of $\\sin\\theta - \\cos\\theta$ is:",
        ["$\\frac{1}{5}$", "$\\frac{7}{5}$", "$\\frac{2}{5}$", "$\\frac{1}{7}$"], "$\\frac{1}{5}$",
        r"""$(\sin\theta - \cos\theta)^2 = 2 - \left(\frac75\right)^2 = 2 - \frac{49}{25} = \frac{1}{25}$.

So $\sin\theta - \cos\theta = \frac15$ (positive root for the acute $\theta$ in the standard exam setup).""",
        r"$\sqrt{2 - m^2} = \sqrt{\frac{1}{25}} = \frac15$. Trap: $\frac{7}{5}$ — that is the given sum itself.", 50)
    return S


# ---------------- trig-maxmin ----------------

def build_maxmin():
    S = Sub("trig-maxmin")

    S.notes = r"""### The amplitude formula (the workhorse)
For any angle $\theta$:
$$-\sqrt{a^2 + b^2} \ \le\ a\sin\theta + b\cos\theta \ \le\ +\sqrt{a^2 + b^2}$$
The maximum of $a\sin\theta + b\cos\theta$ is $\sqrt{a^2+b^2}$ and the minimum is its negative (unrestricted $\theta$); restricted to acute angles the range sits between the endpoint values — usually stated so the interior extremum is the answer. Instant values: $4\sin\theta + 3\cos\theta \to 5$, $5\sin\theta + 12\cos\theta \to 13$, $8\sin\theta - 15\cos\theta \to 17$ — Pythagorean pairs every time.
On $0^\circ \le \theta \le 90^\circ$: $\sin\theta + \cos\theta$ ranges from $1$ to $\sqrt2$ — max $\sqrt2$ at $45^\circ$, min $1$ at the endpoints.

### The product bound
$$\sin\theta\cos\theta \le \frac12, \qquad 2\sin\theta\cos\theta = \sin 2\theta \le 1$$
Both maxima occur at $\theta = 45^\circ$. Any multiple $k\sin\theta\cos\theta$ peaks at $\frac{k}{2}$.

### Self-reciprocal sums (AM-GM)
$$\tan^2\theta + \cot^2\theta \ge 2,\qquad \sec^2\theta + \cosec^2\theta \ge 4,\qquad \tan\theta + \cot\theta \ge 2$$
All attained at $\theta = 45^\circ$. The $\sec^2 + \cosec^2$ version: $\frac{1}{\sin^2\cos^2} \ge 4$ since $\sin^2\cos^2 \le \frac14$. Any $x + \frac1x \ge 2$ shape with $x > 0$ follows the same rule, equality at $x = 1$.

### Ordering and comparison facts
On $(0^\circ, 90^\circ)$: $\sin$ rises $0 \to 1$, $\cos$ falls $1 \to 0$, $\tan$ rises $0 \to \infty$. So $\sin 60^\circ > \sin 45^\circ > \sin 30^\circ$; $\sin\theta > \cos\theta \iff \theta > 45^\circ$; $\tan\theta = \cot\theta$ only at $45^\circ$. Also $\frac{1}{1+\sin^2\theta}$ is smallest when $\sin^2\theta$ is largest ($= 1$), giving minimum $\frac12$.

### The 45° equality case and restricted domains
Every bound in this block is attained at $\theta = 45^\circ$: the amplitude expressions reach $\pm\sqrt{a^2+b^2}$ only for unrestricted $\theta$ (the peak of $a\sin\theta + b\cos\theta$ sits at $\tan\theta = \frac{a}{b}$, which is acute for positive $a, b$ — so on $0^\circ$ to $90^\circ$ the max $\sqrt{a^2+b^2}$ IS reachable, while the negative minimum is cut off at the endpoint $-b$). Always read the domain: "for all $\theta$" allows the negative amplitude; "$0^\circ \le \theta \le 90^\circ$" floors the minimum at the endpoint value. Options often include both — the domain decides.

### Quick revision
- $a\sin\theta + b\cos\theta$: max $\sqrt{a^2+b^2}$, min $-\sqrt{a^2+b^2}$.
- $\sin\theta\cos\theta \le \frac12$; $2\sin\theta\cos\theta \le 1$, both at $45^\circ$.
- $\tan^2 + \cot^2 \ge 2$; $\sec^2 + \cosec^2 \ge 4$; $x + \frac1x \ge 2$ with equality at $x=1$.
- $\sin$ up, $\cos$ down on $(0^\circ, 90^\circ)$; crossover at $45^\circ$.
"""

    S.pattern("trig-mm-p1", "Max/min of a sinθ ± b cosθ", "very common",
      "'Find the maximum of 4sinθ + 3cosθ' — a linear combination with Pythagorean coefficients.",
      r"Max $= +\sqrt{a^2+b^2}$, min $= -\sqrt{a^2+b^2}$ for $a\sin\theta + b\cos\theta$.",
      r"""1. Read off $(a, b)$; compute $\sqrt{a^2 + b^2}$ — expect a triplet.
2. Maximum positive, minimum negative (unless $\theta$ is restricted; then check endpoints).
3. Quote both if 'range' is asked.

Why: the expression is a single wave with amplitude $\sqrt{a^2+b^2}$ — the formula IS the answer.""",
      "The maximum value of $4\\sin\\theta + 3\\cos\\theta$ is:",
      r"$\sqrt{4^2 + 3^2} = 5$. Minimum: $-5$ (unrestricted $\theta$).")
    S.pattern("trig-mm-p2", "Bounds of sinθ cosθ", "common",
      "Max/min of sinθcosθ or 2sinθcosθ (sometimes with a coefficient or a plus-one).",
      r"$\sin\theta\cos\theta \le \frac12$; $2\sin\theta\cos\theta = \sin2\theta \le 1$; both peak at $45^\circ$.",
      r"""1. Recognise the product form; halve the coefficient for the max of $k\sin\theta\cos\theta$.
2. Or convert to $\sin 2\theta$ and use the wave range.
3. Minimum on acute angles is $0$ (endpoint); quote only if asked.

Why: the product is the double-angle formula in disguise — one conversion bounds it.""",
      "The maximum value of $2\\sin\\theta\\cos\\theta$ ($\\theta$ acute) is:",
      r"$2\sin\theta\cos\theta = \sin 2\theta \le 1$, attained at $\theta = 45^\circ$.")
    S.pattern("trig-mm-p3", "AM-GM self-reciprocal sums", "common",
      "Minimum of tan²+cot², sec²+cosec², tan+cot — or an equation whose sum equals the bound.",
      r"$x + \frac1x \ge 2$; $\sec^2\theta + \cosec^2\theta = \frac{1}{\sin^2\theta\cos^2\theta} \ge 4$.",
      r"""1. Identify the self-reciprocal pair; quote the AM-GM bound.
2. $\sec^2 + \cosec^2$: combine to $\frac{1}{\sin^2\cos^2}$, then use $\sin\cos \le \frac12$.
3. Equality case: $\theta = 45^\circ$ in every one of these.

Why: reciprocal pairs cannot be small simultaneously — the product $x \cdot \frac1x = 1$ forces the sum up.""",
      "The minimum value of $\\sec^2\\theta + \\cosec^2\\theta$ is:",
      r"$= \frac{1}{\sin^2\theta\cos^2\theta} \ge \frac{1}{(1/2)^2} = 4$, at $\theta = 45^\circ$.")
    S.pattern("trig-mm-p4", "Ordering and crossover comparisons", "common",
      "'Which is largest: sin 30, sin 45, sin 60?'; 'sinθ > cosθ for which θ?'; minimum of 1/(1+sin²θ).",
      r"On $(0^\circ, 90^\circ)$: sin increases, cos decreases; crossover at $45^\circ$; denominators largest → fraction smallest.",
      r"""1. Monotonicity orders same-function comparisons instantly.
2. sin vs cos comparisons pivot at $45^\circ$.
3. For $\frac{1}{1+\sin^2\theta}$: minimise by maximising the denominator ($\sin^2\theta = 1$).

Why: the monotone staircase of the three functions on the acute quadrant decides everything without computation.""",
      "For $0^\\circ < \\theta < 90^\\circ$, $\\sin\\theta > \\cos\\theta$ holds when:",
      r"$\theta > 45^\circ$ — the crossover of the two graphs is at $45^\circ$.")

    # ---- practice ----
    assert 4 ** 2 + 3 ** 2 == 5 ** 2
    S.q("trig-mm-p1", "medium", "The maximum value of $4\\sin\\theta + 3\\cos\\theta$ is:",
        ["$5$", "$7$", "$4$", "$\\sqrt{7}$"], "$5$",
        r"""Amplitude $= \sqrt{4^2 + 3^2} = 5$; maximum $= 5$.""",
        r"$\sqrt{25} = 5$. Trap: $7$ (adding the coefficients) or $\sqrt7$ (adding squares without the root).", 35)
    assert 5 ** 2 + 12 ** 2 == 13 ** 2
    S.q("trig-mm-p1", "medium", "The minimum value of $5\\sin\\theta + 12\\cos\\theta$ (for all $\\theta$) is:",
        ["$-13$", "$13$", "$-17$", "$5$"], "$-13$",
        r"""Amplitude $= \sqrt{25 + 144} = 13$; the minimum is $-13$.""",
        r"$-\sqrt{169} = -13$. Trap: $13$ (forgetting the minus on the minimum).", 35)
    assert 1 ** 2 + 1 ** 2 == 2
    S.q("trig-mm-p1", "easy", "For $0^\\circ \\le \\theta \\le 90^\\circ$, the maximum value of $\\sin\\theta + \\cos\\theta$ is:",
        ["$\\sqrt{2}$", "$1$", "$2$", "$\\frac{1}{\\sqrt{2}}$"], "$\\sqrt{2}$",
        r"""$(\sin\theta + \cos\theta)^2 = 1 + 2\sin\theta\cos\theta \le 1 + 1 = 2$, so the max is $\sqrt2$ at $45^\circ$.

(Or: amplitude of the combination is $\sqrt{1^2+1^2} = \sqrt2$.)""",
        r"$\sqrt{1+1} = \sqrt2$ at $45^\circ$. Trap: $2$ (adding the individual maxima — they occur at different angles).", 30)
    assert F(1, 2)
    S.q("trig-mm-p2", "medium", "The maximum value of $\\sin\\theta\\cos\\theta$ ($\\theta$ acute) is:",
        ["$\\frac{1}{2}$", "$1$", "$\\frac{1}{4}$", "$\\frac{\\sqrt{3}}{4}$"], "$\\frac{1}{2}$",
        r"""$\sin\theta\cos\theta = \frac{\sin 2\theta}{2} \le \frac12$, at $\theta = 45^\circ$.""",
        r"$\frac12$ at $45^\circ$. Trap: $1$ — that is the max of $2\sin\theta\cos\theta$, not of the product.", 30)
    assert math.isclose(2 * math.sin(math.radians(45)) * math.cos(math.radians(45)), 1.0)
    S.q("trig-mm-p2", "easy", "The value of $2\\sin 45^\\circ \\cos 45^\\circ$ is:",
        ["$1$", "$\\frac{1}{2}$", "$\\frac{\\sqrt{3}}{2}$", "$2$"], "$1$",
        r"""$\sin 45^\circ = \cos 45^\circ = \frac{1}{\sqrt2}$: $2 \times \frac12 = 1$.

(Equivalently $2\sin\theta\cos\theta = \sin 2\theta = \sin 90^\circ = 1$.)""",
        r"$\sin 90^\circ = 1$ via the double angle. Trap: $\frac12$ — halving twice.", 25)
    assert F(2, 1) >= 2
    S.q("trig-mm-p3", "medium", "The minimum value of $\\tan^2\\theta + \\cot^2\\theta$ ($\\theta$ acute) is:",
        ["$2$", "$1$", "$4$", "$0$"], "$2$",
        r"""With $x = \tan^2\theta$: $x + \frac1x \ge 2$, equality at $x = 1$ i.e. $\theta = 45^\circ$.""",
        r"$2$ at $45^\circ$. Trap: $0$ — a positive term and its reciprocal cannot both vanish.", 35)
    assert 4 * 1 == 4
    S.q("trig-mm-p3", "hard", "The minimum value of $\\sec^2\\theta + \\cosec^2\\theta$ ($\\theta$ acute) is:",
        ["$4$", "$2$", "$8$", "$1$"], "$4$",
        r"""$\sec^2\theta + \cosec^2\theta = \frac{1}{\cos^2\theta} + \frac{1}{\sin^2\theta} = \frac{\sin^2\theta + \cos^2\theta}{\sin^2\theta\cos^2\theta} = \frac{1}{\sin^2\theta\cos^2\theta}$.

Since $\sin\theta\cos\theta \le \frac12$: the expression $\ge 4$, at $45^\circ$.""",
        r"$\frac{1}{(\sin\cos)^2} \ge 4$. Trap: $2$ — the bound for $\tan^2 + \cot^2$, not this pair.", 50)
    assert 30 < 45 < 60
    S.q("trig-mm-p4", "easy", "Which of the following is the largest?",
        ["$\\sin 60^\\circ$", "$\\sin 30^\\circ$", "$\\sin 45^\\circ$", "$\\cos 60^\\circ$"], "$\\sin 60^\\circ$",
        r"""$\sin$ increases on $(0^\circ, 90^\circ)$: $\sin 60^\circ = \frac{\sqrt3}{2} \approx 0.87$ beats $\sin 45^\circ \approx 0.71$, $\sin 30^\circ = 0.5$, and $\cos 60^\circ = 0.5$.""",
        r"$\sin 60^\circ$. Trap: $\cos 60^\circ = \sin 30^\circ$ — they tie at $0.5$, well below $\sin 45^\circ$.", 25)
    assert math.sin(math.radians(60)) > math.cos(math.radians(60)) > math.sin(math.radians(30))
    S.q("trig-mm-p4", "medium", "For $0^\\circ < \\theta < 90^\\circ$, the inequality $\\sin\\theta > \\cos\\theta$ holds when:",
        ["$\\theta > 45^\\circ$", "$\\theta < 45^\\circ$", "$\\theta = 45^\\circ$", "all acute $\\theta$"], "$\\theta > 45^\\circ$",
        r"""$\sin$ rises and $\cos$ falls; they cross at $45^\circ$. Beyond it, $\sin$ is on top.""",
        r"$\theta > 45^\circ$. Trap: $<$ — the directions of the two functions are easy to swap.", 30)
    assert F(1, 2) == 1 / 2
    S.q("trig-mm-p4", "medium", "The minimum value of $\\frac{1}{1 + \\sin^2\\theta}$ ($\\theta$ real) is:",
        ["$\\frac{1}{2}$", "$1$", "$\\frac{1}{\\sqrt{2}}$", "$0$"], "$\\frac{1}{2}$",
        r"""The fraction is smallest when the denominator is largest: $\sin^2\theta = 1$ gives $1 + 1 = 2$.

Minimum $= \frac12$.""",
        r"$\frac12$ at $\theta = 90^\circ$. Trap: $0$ — the fraction never reaches zero since $1 + \sin^2 \ge 1 > 0$.", 40)
    assert 8 ** 2 + 15 ** 2 == 17 ** 2
    S.q("trig-mm-p1", "hard", "The minimum value of $8\\sin\\theta - 15\\cos\\theta$ over all real $\\theta$ is:",
        ["$-17$", "$17$", "$-7$", "$-15$"], "$-17$",
        r"""Amplitude $= \sqrt{8^2 + 15^2} = \sqrt{289} = 17$; the expression ranges over $[-17, 17]$.

Minimum $= -17$.""",
        r"$-\sqrt{64 + 225} = -17$. Trap: $17$ (missing the minus) or $-7$ (subtracting the coefficients).", 50)
    assert F(36, 1) == 6 * 6
    S.q("trig-mm-p3", "medium", "The minimum value of $9\\tan^2\\theta + 4\\cot^2\\theta$ ($\\theta$ acute) is:",
        ["$12$", "$13$", "$6$", "$36$"], "$12$",
        r"""AM–GM: $9\tan^2\theta + 4\cot^2\theta \ge 2\sqrt{36} = 12$, equality at $\tan^2\theta = \frac23$.""",
        r"$2\sqrt{9 \times 4} = 12$. Trap: $13$ ($a + b$) or $6$ ($\sqrt{ab}$, forgot to double).", 45)
    return S
