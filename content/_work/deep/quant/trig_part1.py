"""Phase-2 deep content for quant/trigonometry — ratios, identities."""
from fractions import Fraction as F

from _lib import Sub


# ---------------- trig-ratios ----------------

def build_ratios():
    S = Sub("trig-ratios")

    S.notes = r"""### The standard-value table (build it, don't memorise it)
$$\sin: \frac{\sqrt0}{2}, \frac{\sqrt1}{2}, \frac{\sqrt2}{2}, \frac{\sqrt3}{2}, \frac{\sqrt4}{2} \text{ at } 0^\circ, 30^\circ, 45^\circ, 60^\circ, 90^\circ$$
cos is the same list read backwards; tan = sin/cos gives $0, \frac{1}{\sqrt3}, 1, \sqrt3, \infty$. Then reciprocals give cosec, sec, cot. The $\frac{\sqrt{k}}{2}$ construction means the table can never be forgotten under pressure.

### One ratio → the whole triangle
Any single ratio pins the triangle's SHAPE: draw a right triangle with sides in that ratio, get the third side by Pythagoras, read off every other ratio.
- $\sin\theta = \frac{3}{5}$ → sides 3-4-5 → $\tan\theta = \frac34$.
- $\cos\theta = \frac{12}{13}$ → 5-12-13 → $\sin\theta = \frac{5}{13}$, $\tan\theta = \frac{5}{12}$.
- $\tan\theta = \frac{1}{\sqrt7}$ → hyp $\sqrt{1+7} = 2\sqrt2$ → $\cosec\theta = 2\sqrt2$.
Keep ratios as fractions to the end; rationalise only the final answer if options are surd-free.

### Two sides → every ratio
Given two sides of the right triangle: third side first (Pythagoras), then name the angle carefully — the ratio asked is relative to a SPECIFIC acute angle: opposite/hyp for its sine, adjacent/hyp for its cosine. "The smaller angle" sits opposite the shorter leg. Triangles 5-12-13, 7-24-25, 8-15-17, 9-40-41 and their multiples supply almost all exam numbers.

### Combining ratios safely
When an expression mixes functions ($\sec 60^\circ + \cosec 30^\circ$, $\cot 30^\circ + \tan 60^\circ$), reduce each term to the $\sin$/$\cos$ table values first, then add — do not invent product rules. The angle-difference formula $\tan(A - B) = \frac{\tan A - \tan B}{1 + \tan A \tan B}$ occasionally appears disguised as a pure 60/30 evaluation; recognising it turns a messy fraction into $\tan 30^\circ$.

### Quick revision
- $\sin$ column $\frac{\sqrt{0,1,2,3,4}}{2}$; cos reversed; tan $= \frac{\sin}{\cos}$.
- One ratio → 3-4-5 / 5-12-13 / 7-24-25 triangle → all ratios.
- Smaller acute angle ⟷ shorter opposite leg.
- $\tan(60^\circ - 30^\circ)$ identity rescues $\frac{\tan A - \tan B}{1+\tan A\tan B}$ expressions.
"""

    S.pattern("trig-ra-p1", "Standard values at 0/30/45/60/90", "very common",
      "A sum/difference of ratios at special angles asked directly.",
      r"Read each term off the $\frac{\sqrt{k}}{2}$ table; add last.",
      r"""1. Convert every function to its table value (sec/cot too — reciprocals of the cos/tan rows).
2. Keep surds as surds; add only matching radicals.
3. Rationalise only at the very end if options demand it.

Why: each term is a fixed constant — the question only tests retrieval plus one line of arithmetic.""",
      "The value of $\\sin 30^\\circ + \\cos 60^\\circ$ is:",
      r"$\frac12 + \frac12 = 1$. Both are the table's middle entries.")
    S.pattern("trig-ra-p2", "One given ratio → the other ratios", "very common",
      "'If sinθ = 3/5, find tanθ' — one ratio given (sometimes in a surd form), others asked.",
      r"Construct the 3-4-5 (or matching) triangle; read the asked ratio off it.",
      r"""1. Write opp/adj from the given ratio; complete the triangle with Pythagoras.
2. Read the asked ratio; rationalise surds at the end.
3. Sign checks are unnecessary for acute exam angles — everything positive.

Why: one ratio fixes the shape, so every other ratio is a re-reading of the same triangle.""",
      "If $\\sin\\theta = \\frac{3}{5}$ ($\\theta$ acute), the value of $\\tan\\theta$ is:",
      r"Triangle 3-4-5: $\tan\theta = \frac{\text{opp}}{\text{adj}} = \frac34$.")
    S.pattern("trig-ra-p3", "Two sides of the triangle → ratios", "common",
      "Two sides of a right triangle given (or hyp + one side); a named ratio of one acute angle asked.",
      r"Third side by Pythagoras, then $\sin = \frac{\text{opp}}{\text{hyp}}$, $\cos = \frac{\text{adj}}{\text{hyp}}$ w.r.t. the NAMED angle.",
      r"""1. Complete the triangle (5-12-13, 7-24-25, 8-15-17 multiples).
2. Identify the angle: 'opposite the shorter leg' = smaller angle.
3. Opposite/adjacent w.r.t. that angle — the top exam trap is flipping them.

Why: the triangle is fully determined; only the naming of the angle can go wrong.""",
      "In a triangle right-angled at B, AB = 5 cm and BC = 12 cm. The value of sin A is:",
      r"AC $= 13$; $\sin A = \frac{\text{opp}}{\text{hyp}} = \frac{BC}{AC} = \frac{12}{13}$. Note the opposite side to A is BC, not AB.")
    S.pattern("trig-ra-p4", "Mixed-function combinations", "common",
      "Expressions mixing sec, cosec, cot at special angles — or a tan-difference formula hidden inside a fraction.",
      r"Reciprocal table entries; $\tan(A-B) = \frac{\tan A - \tan B}{1 + \tan A\tan B}$ rescues the disguised ones.",
      r"""1. Replace sec/cosec/cot by reciprocals of table values.
2. If the expression matches $\frac{\tan A - \tan B}{1 + \tan A \tan B}$, rewrite as $\tan(A - B)$ and read the table once.
3. Compare with the options in surd form first; rationalise only if needed.

Why: the fraction pattern is invisible until you look for it — that's the entire difficulty of these questions.""",
      "The value of $\\frac{\\tan 60^\\circ - \\tan 30^\\circ}{1 + \\tan 60^\\circ \\tan 30^\\circ}$ is:",
      r"$= \tan(60^\circ - 30^\circ) = \tan 30^\circ = \frac{1}{\sqrt3}$.")

    # ---- practice ----
    assert F(1, 2) + F(1, 2) == 1
    S.q("trig-ra-p1", "easy", "The value of $\\sin 30^\\circ + \\cos 60^\\circ$ is:",
        ["$1$", "$\\frac{1}{2}$", "$\\frac{\\sqrt{3}}{2}$", "$2$"], "$1$",
        r"""$\sin 30^\circ = \frac12$ and $\cos 60^\circ = \sin 30^\circ = \frac12$; sum $= 1$.""",
        r"Complementary twins: both read $\frac{\sqrt1}{2}$. Trap: $\frac12$ (evaluating only one term).", 30)
    assert 1 + 2 * F(1, 2) - 1 == 1
    S.q("trig-ra-p1", "medium", "The value of $\\tan 45^\\circ + 2\\cos 60^\\circ - \\sin 90^\\circ$ is:",
        ["$1$", "$2$", "$0$", "$\\frac{1}{2}$"], "$1$",
        r"""$1 + 2 \times \frac12 - 1 = 1 + 1 - 1 = 1$.""",
        r"$1 + 1 - 1 = 1$. Trap: $2$ (forgetting the coefficient is already consumed).", 30)
    assert F(3, 1) + F(3, 1) == 2 * F(3, 1)
    S.q("trig-ra-p1", "medium", "The value of $\\cot 30^\\circ + \\tan 60^\\circ$ is:",
        ["$2\\sqrt{3}$", "$\\sqrt{3}$", "$2\\sqrt{2}$", "$\\frac{2}{\\sqrt{3}}$"], "$2\\sqrt{3}$",
        r"""$\cot 30^\circ = \sqrt3$ and $\tan 60^\circ = \sqrt3$; sum $= 2\sqrt3$.""",
        r"Both terms are $\sqrt3$. Trap: $\sqrt3$ (assuming they cancel or one is $\frac{1}{\sqrt3}$).", 30)
    assert 3 ** 2 + 4 ** 2 == 5 ** 2
    S.q("trig-ra-p2", "easy", "If $\\sin\\theta = \\frac{3}{5}$ ($\\theta$ acute), the value of $\\tan\\theta$ is:",
        ["$\\frac{3}{4}$", "$\\frac{4}{3}$", "$\\frac{4}{5}$", "$\\frac{5}{4}$"], "$\\frac{3}{4}$",
        r"""opp $= 3k$, hyp $= 5k$ → adj $= 4k$ (3-4-5). $\tan\theta = \frac34$.""",
        r"$\tan = \frac{3}{4}$. Trap: $\frac43$ (tan of the OTHER acute angle).", 30)
    assert F(13, 12) - F(5, 12) == F(8, 12) == F(2, 3)
    S.q("trig-ra-p2", "medium", "If $\\cos\\theta = \\frac{12}{13}$ ($\\theta$ acute), the value of $\\sec\\theta - \\tan\\theta$ is:",
        ["$\\frac{2}{3}$", "$\\frac{5}{12}$", "$\\frac{13}{5}$", "$\\frac{3}{2}$"], "$\\frac{2}{3}$",
        r"""Triangle 5-12-13: $\sec\theta = \frac{13}{12}$, $\tan\theta = \frac{5}{12}$.

$\sec\theta - \tan\theta = \frac{13 - 5}{12} = \frac{8}{12} = \frac23$.""",
        r"$\frac{13}{12} - \frac{5}{12} = \frac23$. Trap: $\frac{5}{12}$ — that is $\tan\theta$ itself.", 40)
    assert 1 + 7 == 8 and (2 * 2 ** F(1, 2)) ** 2 == 8
    S.q("trig-ra-p2", "hard", "If $\\tan\\theta = \\frac{1}{\\sqrt{7}}$ ($\\theta$ acute), the value of $\\cosec^2\\theta$ is:",
        ["$8$", "$7$", "$\\sqrt{8}$", "$\\frac{8}{7}$"], "$8$",
        r"""opp $= 1$, adj $= \sqrt7$ → hyp $= \sqrt{1 + 7} = 2\sqrt2$.

$\cosec\theta = \frac{\text{hyp}}{\text{opp}} = 2\sqrt2$; $\cosec^2\theta = 8$.""",
        r"$\cosec^2 = 1 + \cot^2 = 1 + 7 = 8$ — the identity does it in one line. Trap: $\sqrt8$ (forgot to square).", 50)
    assert 5 ** 2 + 12 ** 2 == 13 ** 2
    S.q("trig-ra-p3", "easy", "In $\\triangle ABC$ right-angled at $B$, $AB = 5$ cm and $BC = 12$ cm. The value of $\\sin A$ is:",
        ["$\\frac{12}{13}$", "$\\frac{5}{13}$", "$\\frac{5}{12}$", "$\\frac{12}{5}$"], "$\\frac{12}{13}$",
        r"""AC $= \sqrt{25 + 144} = 13$. Side opposite to $A$ is $BC = 12$: $\sin A = \frac{12}{13}$.""",
        r"Opposite to A is BC, not AB. Trap: $\frac{5}{13}$ (reading the wrong leg as opposite).", 30)
    assert 7 ** 2 + 24 ** 2 == 25 ** 2
    S.q("trig-ra-p3", "medium", "In a right triangle the hypotenuse is $25$ cm and one leg is $7$ cm. The cosine of the angle opposite the $7$ cm leg is:",
        ["$\\frac{24}{25}$", "$\\frac{7}{25}$", "$\\frac{7}{24}$", "$\\frac{24}{7}$"], "$\\frac{24}{25}$",
        r"""Third leg $= \sqrt{625 - 49} = 24$ (7-24-25). The angle opposite $7$ has adjacent leg $24$:

$\cos = \frac{24}{25}$.""",
        r"Opposite 7 → adjacent is 24 → $\cos = \frac{24}{25}$. Trap: $\frac{7}{25}$ (that is the SINE of the same angle).", 40)
    assert 2 + 2 == 4
    S.q("trig-ra-p4", "medium", "The value of $\\sec 60^\\circ + \\cosec 30^\\circ$ is:",
        ["$4$", "$2$", "$2\\sqrt{3}$", "$3$"], "$4$",
        r"""$\sec 60^\circ = \frac{1}{\cos 60^\circ} = 2$ and $\cosec 30^\circ = \frac{1}{\sin 30^\circ} = 2$; sum $= 4$.""",
        r"$2 + 2 = 4$. Trap: $2$ (assuming the two terms cancel or equal 1).", 30)
    assert F(4, 3) - F(1, 3) == 1
    S.q("trig-ra-p4", "medium", "The value of $\\sec^2 30^\\circ - \\tan^2 30^\\circ$ is:",
        ["$1$", "$\\frac{1}{3}$", "$0$", "$2$"], "$1$",
        r"""$\sec^2\theta - \tan^2\theta = 1$ for every $\theta$ where defined — the answer is $1$ without any table work.

(Indeed $\sec^2 30^\circ = \frac43$, $\tan^2 30^\circ = \frac13$.)""",
        r"The identity $\sec^2 - \tan^2 = 1$ is angle-independent. Trap: $\frac13$ — computing entries and slipping.", 25)
    return S


# ---------------- trig-identities ----------------

def build_identities():
    S = Sub("trig-identities")

    S.notes = r"""### The three identity engines
$$\sin^2\theta + \cos^2\theta = 1,\qquad 1 + \tan^2\theta = \sec^2\theta,\qquad 1 + \cot^2\theta = \cosec^2\theta$$
Every identity question runs one of three engines:
1. **Divide by $\cos^2$** (or $\sin^2$): $\frac{\sin^2}{\cos^2} + 1 = \frac{1}{\cos^2}$ is the second identity — so any $\sec^2 \pm \tan^2$ combination converts to a single ratio.
2. **Pair products**: $(\sec\theta + \tan\theta)(\sec\theta - \tan\theta) = 1$, $(\cosec\theta + \cot\theta)(\cosec\theta - \cot\theta) = 1$ — conjugate pairs whose product is 1.
3. **Squares of sums**: $(\sin\theta \pm \cos\theta)^2 = 1 \pm 2\sin\theta\cos\theta$ — links "sin+cos = m" questions to "sin·cos" questions.

### The sin+cos / sin−cos web
Given $\sin\theta + \cos\theta = m$: squaring gives $\sin\theta\cos\theta = \frac{m^2 - 1}{2}$, and $(\sin\theta - \cos\theta)^2 = 2 - m^2$. Given $\sec\theta + \tan\theta = m$, the conjugate gives $\sec\theta - \tan\theta = \frac1m$ — then adding/subtracting the pair returns $\sec\theta$ and $\tan\theta$ individually (this 2-step unlocks $\sin\theta$ via a triangle).

### Convert-to-sin-cos for anything composite
For fractions mixing tan/sin/cos with an unknown coefficient ("if $\tan\theta = \frac34$, find $\frac{4\sin\theta - \cos\theta}{4\cos\theta + \sin\theta}$"): divide numerator and denominator by $\cos\theta$ — everything becomes $t = \tan\theta$, one substitution, one fraction. Squared combos like $\tan^2\theta + \cot^2\theta$ come from squaring $\tan\theta + \cot\theta$ and subtracting 2.

### Quick revision
- $\sin^2 + \cos^2 = 1$; divide it by $\cos^2$ or $\sin^2$ for the other two.
- $(\sec + \tan)(\sec - \tan) = 1$; same for cosec/cot.
- $(\sin \pm \cos)^2 = 1 \pm 2\sin\cos$; $\sin\cos = \frac{(\sin+\cos)^2 - 1}{2}$.
- Composite fractions: divide top and bottom by $\cos\theta$.
- $\tan\theta + \cot\theta = \sec\theta\,\cosec\theta$; squaring then subtracting 2 gives the squared sum.
"""

    S.pattern("trig-id-p1", "Conjugate pairs: sec±tan, cosec±cot", "very common",
      "'If secθ + tanθ = m, find secθ − tanθ' (or the reverse) — or the pair used to extract individual ratios.",
      r"(\sec\theta + \tan\theta)(\sec\theta - \tan\theta) = 1",
      r"""1. The conjugate is its reciprocal: $\sec\theta - \tan\theta = \frac1m$.
2. To extract $\tan\theta$: subtract the pair ($2\tan\theta = m - \frac1m$).
3. Then a 3-4-5 style triangle gives sin/cos if asked.

Why: the product being exactly 1 makes every question in this family a two-line reciprocal computation.""",
      "If $\\sec\\theta + \\tan\\theta = 5$ ($\\theta$ acute), the value of $\\sec\\theta - \\tan\\theta$ is:",
      r"$\sec\theta - \tan\theta = \frac{1}{\sec\theta + \tan\theta} = \frac15$.")
    S.pattern("trig-id-p2", "sin²+cos² expansions and squares of sums", "very common",
      "Expressions like (sinθ ± cosθ)², or a product like (cosecθ − sinθ)(secθ − cosθ)(tanθ + cotθ) to simplify.",
      r"(\sin\theta \pm \cos\theta)^2 = 1 \pm 2\sin\theta\cos\theta; convert everything to sin/cos and cancel.",
      r"""1. Expand squares: the cross term $2\sin\theta\cos\theta$ and the 1 dominate.
2. For composite products, convert each bracket to sin/cos: $\cosec\theta - \sin\theta = \frac{\cos^2\theta}{\sin\theta}$ etc., then cancel.
3. Constants fall out — most of these expressions are pure numbers (1 or 2).

Why: every term is secretly $\sin^2 + \cos^2 = 1$ wearing a costume.""",
      "The value of $(\\sin\\theta + \\cos\\theta)^2 + (\\sin\\theta - \\cos\\theta)^2$ is:",
      r"$= 1 + 2\sin\theta\cos\theta + 1 - 2\sin\theta\cos\theta = 2$. Cross terms cancel.")
    S.pattern("trig-id-p3", "Substituting tan via divide-by-cos", "very common",
      "tanθ given; a linear fraction in sinθ and cosθ asked — coefficients on both.",
      r"Divide numerator and denominator by $\cos\theta$; the fraction becomes one in $t = \tan\theta$.",
      r"""1. $\frac{a\sin\theta + b\cos\theta}{c\cos\theta + d\sin\theta} = \frac{a\tan\theta + b}{c + d\tan\theta}$.
2. Substitute $t$; simplify the single fraction.
3. Keep fractions exact ($t = \frac34$, not 0.75).

Why: division by $\cos\theta$ is legal (nonzero for acute angles) and converts two unknowns into one.""",
      "If $\\tan\\theta = \\frac{3}{4}$, the value of $\\frac{4\\sin\\theta - \\cos\\theta}{4\\cos\\theta + \\sin\\theta}$ is:",
      r"Divide by $\cos\theta$: $\frac{4 \times \frac34 - 1}{4 + \frac34} = \frac{2}{\frac{19}{4}} = \frac{8}{19}$.")
    S.pattern("trig-id-p4", "Squared sums via squaring (tan+cot, sin+cosec)", "common",
      "'If tanθ + cotθ = k, find tan²θ + cot²θ' — or an equation like sinθ + cosecθ = 2 that forces a special value.",
      r"Square the given: $(x + \frac{1}{x})^2 = x^2 + \frac{1}{x^2} + 2$, so subtract 2. Equations equal to 2 force $x = 1$.",
      r"""1. Square the given sum; subtract 2 for the squared-pair answer.
2. AM-GM shortcut: $x + \frac1x \ge 2$, with equality only at $x = 1$ — so "= 2" means $\tan\theta = \sin\theta = 1$, i.e. $\theta = 45^\circ$ / $90^\circ$ respectively.
3. Read off the asked power exactly (squared vs fourth).

Why: the self-reciprocal structure makes both the bound and the equality case immediate.""",
      "If $\\tan\\theta + \\cot\\theta = 5$ ($\\theta$ acute), the value of $\\tan^2\\theta + \\cot^2\\theta$ is:",
      r"Square: $25 = \tan^2\theta + \cot^2\theta + 2$, so $\tan^2\theta + \cot^2\theta = 23$.")

    # ---- practice ----
    assert F(1, 5) == 1 / F(5, 1)
    S.q("trig-id-p1", "medium", "If $\\sec\\theta + \\tan\\theta = 5$ ($\\theta$ acute), the value of $\\sec\\theta - \\tan\\theta$ is:",
        ["$\\frac{1}{5}$", "$5$", "$\\frac{1}{3}$", "$4$"], "$\\frac{1}{5}$",
        r"""$(\sec\theta + \tan\theta)(\sec\theta - \tan\theta) = \sec^2\theta - \tan^2\theta = 1$.

So $\sec\theta - \tan\theta = \frac15$.""",
        r"Conjugate = reciprocal: $\frac15$. Trap: $4$ (subtracting instead of using the product).", 35)
    assert F(1, 2) + F(1, 2) == 1
    S.q("trig-id-p1", "hard", "If $\\sec\\theta + \\tan\\theta = 5$ ($\\theta$ acute), the value of $\\tan\\theta$ is:",
        ["$\\frac{12}{5}$", "$\\frac{5}{12}$", "$\\frac{13}{12}$", "$\\frac{3}{5}$"], "$\\frac{12}{5}$",
        r"""Subtract the conjugate: $2\tan\theta = 5 - \frac15 = \frac{24}{5}$ → $\tan\theta = \frac{12}{5}$.

(5-12-13 triangle: $\sin\theta = \frac{5}{13}$ if ever asked.)""",
        r"$\tan = \frac{m - 1/m}{2} = \frac{12}{5}$. Trap: $\frac{5}{12}$ — the inverse fraction.", 50)
    assert (F(1, 2) + F(1, 2)) ** 2 + (F(1, 2) - F(1, 2)) ** 2 == 2
    S.q("trig-id-p2", "easy", "The value of $(\\sin\\theta + \\cos\\theta)^2 + (\\sin\\theta - \\cos\\theta)^2$ is:",
        ["$2$", "$1$", "$0$", "$4$"], "$2$",
        r"""Expanding: $(1 + 2sc) + (1 - 2sc) = 2$ for every $\theta$.""",
        r"Cross terms cancel: $2$. Trap: $1$ (using $\sin^2 + \cos^2 = 1$ and forgetting the second bracket).", 25)
    import math
    _t = math.radians(30)
    assert abs((1 / math.sin(_t) - math.sin(_t)) * (1 / math.cos(_t) - math.cos(_t)) * (math.tan(_t) + 1 / math.tan(_t)) - 1) < 1e-9
    S.q("trig-id-p2", "medium", "The value of $(\\cosec\\theta - \\sin\\theta)(\\sec\\theta - \\cos\\theta)(\\tan\\theta + \\cot\\theta)$ is:",
        ["$1$", "$0$", "$2$", "$\\tan\\theta\\,\\cot\\theta$"], "$1$",
        r"""$\cosec\theta - \sin\theta = \frac{\cos^2\theta}{\sin\theta}$; $\sec\theta - \cos\theta = \frac{\sin^2\theta}{\cos\theta}$; $\tan\theta + \cot\theta = \frac{1}{\sin\theta\cos\theta}$.

Product $= \frac{\cos^2 \cdot \sin^2}{\sin\theta \cdot \cos\theta \cdot \sin\theta\cos\theta} = 1$.""",
        r"Convert all three, cancel to $1$. Trap: $0$ (assuming one bracket vanishes — none does).", 45)
    assert F(2, 1) / F(19, 4) == F(8, 19)
    S.q("trig-id-p3", "medium", "If $\\tan\\theta = \\frac{3}{4}$, the value of $\\frac{4\\sin\\theta - \\cos\\theta}{4\\cos\\theta + \\sin\\theta}$ is:",
        ["$\\frac{8}{19}$", "$\\frac{19}{8}$", "$\\frac{1}{2}$", "$\\frac{8}{13}$"], "$\\frac{8}{19}$",
        r"""Divide top and bottom by $\cos\theta$:

$\frac{4 \times \frac34 - 1}{4 + \frac34} = \frac{2}{\frac{19}{4}} = \frac{8}{19}$.""",
        r"$\frac{4t - 1}{4 + t} = \frac{8}{19}$. Trap: $\frac{8}{13}$ (using $t = \frac34$ as $t = \frac43$).", 40)
    assert 5 ** 2 - 2 == 23
    S.q("trig-id-p3", "medium", "If $\\tan\\theta = 3$, the value of $\\frac{2\\sin\\theta + \\cos\\theta}{\\sin\\theta - 2\\cos\\theta}$ is:",
        ["$7$", "$-7$", "$\\frac{7}{5}$", "$-\\frac{1}{7}$"], "$7$",
        r"""Divide top and bottom by $\cos\theta$:

$\frac{2\tan\theta + 1}{\tan\theta - 2} = \frac{6 + 1}{3 - 2} = \frac71 = 7$.""",
        r"$\frac{2t+1}{t-2} = 7$. Trap: $-7$ — a sign slip reading $t - 2$ as $2 - t$.", 35)
    assert 3 * 3 + 1 == 10
    S.q("trig-id-p4", "easy", "If $\\sin\\theta = \\cos\\theta$ ($\\theta$ acute), then $\\theta$ equals:",
        ["$45^\\circ$", "$30^\\circ$", "$60^\\circ$", "$90^\\circ$"], "$45^\\circ$",
        r"""Divide by $\cos\theta$: $\tan\theta = 1$ → $\theta = 45^\circ$.""",
        r"$\tan = 1$ at $45^\circ$ only. Trap: $90^\circ$ (where $\sin = 1$, $\cos = 0$ — not equal).", 25)
    assert 1 + 1 == 2
    S.q("trig-id-p4", "hard", "If $\\sin\\theta + \\cosec\\theta = 2$ ($\\theta$ acute), the value of $\\sin^2\\theta + \\cosec^2\\theta$ is:",
        ["$2$", "$4$", "$1$", "$\\sqrt{2}$"], "$2$",
        r"""$s + \frac1s = 2 \Rightarrow s^2 - 2s + 1 = 0 \Rightarrow s = 1$.

So $\sin\theta = 1$, and $\sin^2\theta + \cosec^2\theta = 1 + 1 = 2$.""",
        r"The sum 2 forces $\sin\theta = 1$: both squares are 1. Trap: $4$ (squaring the given sum).", 50)
    return S
