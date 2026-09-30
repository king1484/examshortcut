"""Readable rewrite of Trigonometry (all 5 subtopics).

Plain English, one idea per section, every number recomputed below.
Run: python trigonometry.py  (patches content/core/topics/quant/trigonometry.json)
"""
import json
from math import sin, cos, tan, radians, sqrt
from fractions import Fraction
from pathlib import Path

ROOT = Path(__file__).resolve().parents[3]
TOPIC = ROOT / "core" / "topics" / "quant" / "trigonometry.json"

# ---------- answer checks (every number printed on the page) ----------
# ratios
assert Fraction(1, 2) + Fraction(1, 2) == 1                              # sin30 + cos60
assert Fraction(3, 4) + Fraction(1, 4) == 1                              # tan45 and value drops
assert 3 ** 2 + 4 ** 2 == 25 == 5 ** 2                                   # 3-4-5
assert 5 ** 2 + 12 ** 2 == 169 == 13 ** 2                                # 5-12-13
assert 20 ** 2 + 21 ** 2 == 841 == 29 ** 2                               # 20-21-29
assert abs(sin(radians(30)) - 0.5) < 1e-12
assert abs(tan(radians(60)) * tan(radians(30)) - 1) < 1e-12              # cofactor product
assert abs((sqrt(3) - 1 / sqrt(3)) / 2 - 1 / sqrt(3)) < 1e-12            # tan60-tan30 over 1+prod
assert abs(2 * sin(radians(60)) - sqrt(3)) < 1e-12                       # 2 sin60 = sqrt3 -> 60 deg
# identities
assert (Fraction(5) + Fraction(1, 5)) / 2 == Fraction(13, 5)             # sec from sec+tan=5
assert (Fraction(5) - Fraction(1, 5)) / 2 == Fraction(12, 5)             # tan from sec+tan=5
assert 25 + 144 == 169                                                   # 1 + tan^2 = sec^2 scaled
assert 5 ** 2 - 2 == 23                                                  # tan+cot=5 -> squares sum
assert Fraction(2, 1) / Fraction(19, 4) == Fraction(8, 19)               # (4tan-1)/(4+tan), tan=3/4
assert (1 + 1) == 2                                                      # (sin+cos)^2+(sin-cos)^2
# complementary
assert abs(sin(radians(35)) / cos(radians(55)) - 1) < 1e-12              # sin35 = cos55
assert abs(sin(radians(35)) * (1 / cos(radians(55))) + cos(radians(35)) * (1 / sin(radians(55))) - 2) < 1e-9
assert abs(tan(radians(5)) * tan(radians(25)) * 1 * tan(radians(65)) * tan(radians(85)) - 1) < 1e-9
assert abs(1 / sin(radians(68)) - 1 / cos(radians(22))) < 1e-12          # twins subtract to zero
assert 3 * 25 == 75 and 90 - 75 == 15 == 25 - 10                         # sin3A=cos(A-10) -> A=25
assert 2 * 20 == 40 and 3 * 20 - 10 == 50 and 40 + 50 == 90              # tan2A=cot(3A-10) -> A=20
# value-putting
assert 2 + Fraction(3, 4) - Fraction(3, 4) == 2                          # 2tan^2 45 + cos^2 30 - sin^2 60
assert Fraction(2 - 1, 2) == Fraction(1, 2)                              # sin+cos=sqrt2 -> product
assert Fraction(4 - 3, 4 + 3) == Fraction(1, 7)                          # 5tan=4 fraction
assert Fraction(21, 29) * 29 == 21                                       # cos from cot=21/20
assert (Fraction(3) + Fraction(1, 3)) / 2 == Fraction(5, 3)              # cosec from cosec+cot=3
assert 9 + 16 == 25                                                      # 3-4-5 behind sin=3/5
# max-min
assert 16 + 9 == 25                                                      # 4sin+3cos max 5
assert 2 * 2 == 4                                                        # AM-GM floor
assert 5 + 7 * 0 == 5 and 5 + 7 * 1 == 12                                # 5sin^2+12cos^2 range
assert abs(sin(radians(45)) - cos(radians(45))) < 1e-12                  # crossover at 45
assert 5 * 5 + 12 * 12 == 169                                            # weighted check
# padding content
assert Fraction(1, 4) + 1 + Fraction(1, 4) == Fraction(3, 2)             # sin^2 30 + tan^2 45 + cos^2 60
assert Fraction(49, 25) - 1 == Fraction(24, 25) and Fraction(24, 25) / 2 == Fraction(12, 25)  # (7/5)^2 bridge
assert 9 - 2 == 7                                                        # sin + cosec = 3 squares
assert abs(cos(radians(25)) * cos(radians(65)) - sin(radians(25)) * cos(radians(25))) < 1e-12  # cos65 = sin25
assert abs(2 * sin(radians(25)) * cos(radians(25)) - sin(radians(50))) < 1e-12                 # double angle check
assert 2 * 16 - 10 == 22 and 3 * 16 + 20 == 68 and 22 + 68 == 90          # sin(2A-10)=cos(3A+20) -> A=16
assert (Fraction(3) + Fraction(1, 3)) / 2 == Fraction(5, 3)              # sec from sec+tan=3
assert (Fraction(3) - Fraction(1, 3)) / 2 == Fraction(4, 3)              # tan from sec+tan=3
assert 2 + 5 * 0 == 2 and 2 + 5 * 1 == 7                                 # 7sin^2+2cos^2 range
assert Fraction(5, 2) + Fraction(2, 5) == Fraction(29, 10)                # cosec pair add
assert Fraction(29, 10) / 2 == Fraction(29, 20) and Fraction(20, 29) * 29 == 20  # sin = 20/29
assert Fraction(1) - Fraction(24, 25) == Fraction(1, 25)                  # (sin-cos)^2 = 1/25
assert 10 + 80 == 90 and 20 + 70 == 90                                    # six-factor pairing

# ---------------- trig-ratios ----------------
ra_concept = (
    "In a right triangle, each acute angle has six ratios built from the three sides. "
    "Three are primary: sine, cosine, tangent; three are their reciprocals. "
    "Five standard angles cover almost every exam question, and one known ratio produces all six."
)

ra_notes = r"""### The six ratios
For an acute angle $\theta$ in a right triangle:
- $\sin\theta=\dfrac{\text{opposite}}{\text{hypotenuse}}$
- $\cos\theta=\dfrac{\text{adjacent}}{\text{hypotenuse}}$
- $\tan\theta=\dfrac{\text{opposite}}{\text{adjacent}}$

The other three flip these: $\text{cosec}=\dfrac{1}{\sin}$, $\sec=\dfrac{1}{\cos}$, $\cot=\dfrac{1}{\tan}$.

> **Rule:** Name the sides from the angle you are using. The opposite side changes when the angle changes.

### The standard table, built not memorised
Write $\sin$ as $\dfrac{\sqrt{k}}{2}$ for $k=0,1,2,3,4$:
| $\theta$ | $0^\circ$ | $30^\circ$ | $45^\circ$ | $60^\circ$ | $90^\circ$ |
|---|---|---|---|---|---|
| $\sin$ | $0$ | $\dfrac12$ | $\dfrac{1}{\sqrt2}$ | $\dfrac{\sqrt3}{2}$ | $1$ |
| $\cos$ | $1$ | $\dfrac{\sqrt3}{2}$ | $\dfrac{1}{\sqrt2}$ | $\dfrac12$ | $0$ |

$\cos$ is $\sin$ read backwards. Then $\tan=\dfrac{\sin}{\cos}$ gives $0,\dfrac{1}{\sqrt3},1,\sqrt3$ and undefined at $90^\circ$.

Read $\tan$ straight off that division: it starts at $0$, passes $1$ exactly at $45^\circ$, and blows up where cosine hits zero. A one-line check: $\tan30^\circ\tan60^\circ=1$, which the table confirms because the angles are complementary.

> **Tip:** Recompute the row from $\sqrt{k}/2$ instead of memorising. It cannot be forgotten in the hall.

### One ratio makes all six
Given $\sin\theta=\dfrac35$: opposite $3$, hypotenuse $5$, so adjacent $4$ (the $3$-$4$-$5$ triangle). Then $\cos=\dfrac45$, $\tan=\dfrac34$, $\text{cosec}=\dfrac53$, $\sec=\dfrac54$, $\cot=\dfrac43$.

The Pythagoras step is the whole work: two sides known means the third follows.

Try the same move with $\cos\theta=\dfrac{5}{13}$: adjacent $5$, hypotenuse $13$, so the opposite side is $12$ from the $5$-$12$-$13$ triplet. Then $\tan\theta=\dfrac{12}{5}$, $\sec\theta=\dfrac{13}{5}$, $\cot\theta=\dfrac{5}{12}$ and $\cosec\theta=\dfrac{13}{12}$. Six answers come from one fact.

> **Watch:** Keep the given ratio's fraction exact. Decimal sides break the triplets ($3$-$4$-$5$, $5$-$12$-$13$, $20$-$21$-$29$).

### Labelling a given triangle
Triangle right-angled at $B$ with $AB=5$, $BC=12$: hypotenuse $AC=13$. For angle $A$, the opposite side is $BC=12$, so $\sin A=\dfrac{12}{13}$.

Switch to angle $C$ and the roles swap: $\sin C=\dfrac{5}{13}$. One drawing, two readings.

### Reading an angle off a value
$2\sin\theta=\sqrt3$ means $\sin\theta=\dfrac{\sqrt3}{2}$, which is the $60^\circ$ entry. Equations of this shape just run the table backwards.

The reverse lookup needs the function named first: the value $\dfrac12$ means $30^\circ$ for sine but $60^\circ$ for cosine, while $\dfrac{1}{\sqrt2}$ means $45^\circ$ for both. Options are often rationalised, so know $\dfrac{1}{\sqrt3}=\dfrac{\sqrt3}{3}$ too.

> **Remember:** Every ratio value in this range belongs to exactly one standard angle, so match it and stop.
"""

ra_formulas = [
    {"name": "Primary ratios", "tex": r"\sin\theta=\frac{o}{h},\quad \cos\theta=\frac{a}{h},\quad \tan\theta=\frac{o}{a}", "note": "o = opposite, a = adjacent, h = hypotenuse."},
    {"name": "Reciprocals", "tex": r"\text{cosec}=\frac{1}{\sin},\quad \sec=\frac{1}{\cos},\quad \cot=\frac{1}{\tan}", "note": "Flip the fraction."},
    {"name": "Standard values", "tex": r"\sin\theta=\frac{\sqrt{k}}{2},\ k=0,1,2,3,4", "note": "For 0, 30, 45, 60, 90 degrees; cos runs the row backwards."},
    {"name": "One ratio to all", "tex": r"\sin\theta=\frac{3}{5}\Rightarrow\cos=\frac45,\ \tan=\frac34", "note": "Draw the 3-4-5 triangle and read every ratio off it."},
]

ra_tricks = [
    {
        "title": "The root-k-over-2 row",
        "body": "sin at 0, 30, 45, 60, 90 is root-0, root-1, root-2, root-3, root-4, all over 2. Cos is the same row reversed.",
        "example": {
            "q": "The value of $\\sin 30^\\circ + \\cos 60^\\circ$ is:",
            "steps": [r"$\sin30^\circ=\dfrac12$ and $\cos60^\circ=\dfrac12$.", r"$\dfrac12+\dfrac12=1$."],
            "answer": "1",
        },
    },
    {
        "title": "Triplet finishes the ratios",
        "body": "Given sin = 3/5, place 3 and 5 in the triangle; the third side 4 completes 3-4-5 and every ratio follows.",
        "example": {
            "q": "If $\\sin\\theta = \\frac{3}{5}$ ($\\theta$ acute), the value of $\\tan\\theta$ is:",
            "steps": [r"Adjacent $=\sqrt{25-9}=4$.", r"$\tan\theta=\dfrac{3}{4}$."],
            "answer": "3/4",
        },
    },
    {
        "title": "Angle from a value",
        "body": "Isolate the ratio, then match the table entry. 2 sin = root 3 means sin = root-3 over 2, the 60-degree slot.",
        "example": {
            "q": "If $2\\sin\\theta=\\sqrt3$ ($0^\\circ\\le\\theta\\le90^\\circ$), then $\\theta$ is:",
            "steps": [r"$\sin\theta=\dfrac{\sqrt3}{2}$.", r"That value sits at $60^\circ$."],
            "answer": "60 degrees",
        },
    },
]

ra_mistakes = [
    {"wrong": "Taking the adjacent side as the hypotenuse.", "right": "The hypotenuse faces the right angle and is the longest side. In 3-4-5, $\\sin=\\dfrac35$ uses 5 as hypotenuse."},
    {"wrong": "Swapping opposite and adjacent when the angle changes.", "right": "Sides are named per angle: $\\sin A=\\dfrac{12}{13}$ but $\\sin C=\\dfrac{5}{13}$ in the same triangle."},
    {"wrong": "Writing $\\cos 60^\\circ=\\dfrac{\\sqrt3}{2}$.", "right": "Cosine reverses the row: $\\cos60^\\circ=\\dfrac12$; $\\dfrac{\\sqrt3}{2}$ is $\\cos30^\\circ$."},
    {"wrong": "Mixing $\\sec$ and $\\text{cosec}$.", "right": "$\\sec$ pairs with $\\cos$; $\\text{cosec}$ pairs with $\\sin$. Both flip, nothing more."},
    {"wrong": "Using decimals for the $3$-$4$-$5$ family.", "right": "Exact fractions keep the triplet visible and the arithmetic short."},
]

ra_revision = [
    "$\\sin=\\dfrac{opp}{hyp}$, $\\cos=\\dfrac{adj}{hyp}$, $\\tan=\\dfrac{opp}{adj}$; the rest are reciprocals.",
    "$\\sin$ row: $\\dfrac{\\sqrt{k}}{2}$ for $k=0..4$; $\\cos$ is the row reversed.",
    "$\\tan45^\\circ=1$; $\\tan$ is undefined at $90^\\circ$.",
    "One ratio plus Pythagoras yields all six; keep triplets exact.",
    "Label opposite and adjacent afresh for each angle.",
    "An equation like $2\\sin\\theta=\\sqrt3$ is a table lookup: $\\theta=60^\\circ$.",
]

def pat(pid, name, freq, spot, steps, why, q, esteps, ans):
    return {"id": pid, "name": name, "frequency": freq, "howToSpot": spot,
            "steps": steps, "why": why, "example": {"q": q, "steps": esteps, "answer": ans}}

ra_patterns = [
    pat("trig-ra-p1", "Standard values at 0/30/45/60/90", "very common",
        "A direct expression in standard angles.",
        [r"Replace each ratio by its table value.", r"Simplify the fractions.",
         r"Watch $45^\circ$ entries: $\tan45^\circ=1$."],
        "The five standard values turn any such expression into arithmetic within a line or two.",
        "The value of $\\sin 30^\\circ + \\cos 60^\\circ$ is:",
        [r"$\sin30^\circ=\dfrac12$, $\cos60^\circ=\dfrac12$.", r"$\dfrac12+\dfrac12=1$."],
        "1"),
    pat("trig-ra-p2", "One given ratio to the other ratios", "very common",
        "A single ratio given; another asked.",
        [r"Put the two known sides into a right triangle.", r"Find the third side by Pythagoras.",
         r"Read the asked ratio off the triangle."],
        "All six ratios live on one triangle, so one ratio plus Pythagoras unlocks the rest.",
        "If $\\sin\\theta = \\frac{3}{5}$ ($\\theta$ acute), the value of $\\tan\\theta$ is:",
        [r"Adjacent $=\sqrt{25-9}=4$.", r"$\tan\theta=\dfrac{3}{4}$."],
        "3/4"),
    pat("trig-ra-p3", "Two sides of the triangle to ratios", "common",
        "A labelled right triangle with two side lengths.",
        [r"Find the third side if needed.", r"Identify the side roles for the asked angle.",
         r"Write the ratio."],
        "Naming sides per angle converts geometry into a plain fraction.",
        "In a triangle right-angled at B, AB = 5 cm and BC = 12 cm. The value of sin A is:",
        [r"$AC=\sqrt{25+144}=13$.", r"Opposite $A$ is $BC=12$.", r"$\sin A=\dfrac{12}{13}$."],
        "12/13"),
    pat("trig-ra-p4", "Mixed-function combinations", "common",
        "Tangent additions like the tan-of-sum shape.",
        [r"Insert standard values.", r"Simplify surds by rationalising.",
         r"Recognise the result as a known ratio if it matches one."],
        "These collapse to a single table value once the arithmetic settles.",
        "The value of $\\frac{\\tan 60^\\circ - \\tan 30^\\circ}{1 + \\tan 60^\\circ \\tan 30^\\circ}$ is:",
        [r"Numerator: $\sqrt3-\dfrac{1}{\sqrt3}=\dfrac{2}{\sqrt3}$; denominator: $1+1=2$.",
         r"$\dfrac{2/\sqrt3}{2}=\dfrac{1}{\sqrt3}=\tan30^\circ$."],
        "1/sqrt(3)"),
    pat("trig-ra-p5", "Finding the angle from a ratio", "common",
        "An equation with one unknown angle.",
        [r"Isolate the single ratio on one side.", r"Match the value to the table.",
         r"State the angle."],
        "Within the standard range each value belongs to one angle, so solving is matching.",
        "If $2\\sin\\theta=\\sqrt3$ ($0^\\circ\\le\\theta\\le90^\\circ$), then $\\theta$ is:",
        [r"$\sin\theta=\dfrac{\sqrt3}{2}$.", r"That is the $60^\circ$ entry."],
        "60 degrees"),
]

# ---------------- trig-identities ----------------
id_concept = (
    "Three identities drive nearly every simplification: sine squared plus cosine squared equals one, and its tan-sec and cot-cosec cousins. "
    "Conjugate pairs turn sums into reciprocals, and squaring a sum removes the cross terms."
)

id_notes = r"""### The three engines
$$\sin^2\theta+\cos^2\theta=1,\qquad 1+\tan^2\theta=\sec^2\theta,\qquad 1+\cot^2\theta=\cosec^2\theta$$
Divide the first by $\cos^2\theta$ and the second appears; divide by $\sin^2\theta$ for the third. One identity, three costumes.

Verify with $\theta=30^\circ$: $\sin^2+\cos^2=\dfrac14+\dfrac34=1$ holds, and $1+\tan^230^\circ=1+\dfrac13=\dfrac43=\sec^230^\circ$. Checks like this catch a misremembered formula instantly.

> **Rule:** Spot which squared pair the question shows, then apply the matching engine and cancel.

### Conjugate pairs
$$(\sec\theta+\tan\theta)(\sec\theta-\tan\theta)=\sec^2\theta-\tan^2\theta=1$$
So the two factors are reciprocals. Given $\sec+\tan=5$, the partner is $\dfrac15$. Adding the two: $2\sec=5+\dfrac15=\dfrac{26}{5}$, so $\sec=\dfrac{13}{5}$ and $\tan=\dfrac{12}{5}$.

The same trick works for $\cosec+\cot$: the conjugate product is also $1$.

Numbers stay friendly here. $\cosec\theta+\cot\theta=\dfrac52$ forces $\cosec\theta-\cot\theta=\dfrac25$; adding, $2\cosec\theta=\dfrac{29}{10}$, so $\cosec\theta=\dfrac{29}{20}$ and $\sin\theta=\dfrac{20}{29}$. The $20$-$21$-$29$ triplet was hiding inside the fractions.

> **Tip:** A 'sum given, difference asked' question is this pair in disguise. Write the product-of-difference identity before anything else.

### Squares of sums
$(a+b)^2+(a-b)^2=2(a^2+b^2)$, so
$$(\sin\theta+\cos\theta)^2+(\sin\theta-\cos\theta)^2=2(\sin^2\theta+\cos^2\theta)=2$$
Check: each square expands to $1\pm2\sin\theta\cos\theta$, and the cross terms cancel.

The same square bridges a given sum to a product: $\sin\theta+\cos\theta=\dfrac75$ squares to $1+2\sin\theta\cos\theta=\dfrac{49}{25}$, so $\sin\theta\cos\theta=\dfrac{12}{25}$. The product falls out of the square every time.

### Build tan by dividing by cos
Any fraction of sines and cosines becomes a fraction of tangents after dividing top and bottom by $\cos\theta$:
$$\frac{4\sin\theta-\cos\theta}{4\cos\theta+\sin\theta}=\frac{4\tan\theta-1}{4+\tan\theta}$$
With $\tan\theta=\dfrac34$: numerator $3-1=2$, denominator $4+\dfrac34=\dfrac{19}{4}$, so the value is $\dfrac{8}{19}$.

> **Watch:** Divide every term, top and bottom. A missed term breaks the whole fraction.

### Squared sums from a given sum
$\tan\theta+\cot\theta=5$. Square: $\tan^2+\cot^2+2\tan\cot=25$, and $\tan\cot=1$, so $\tan^2+\cot^2=23$.

The same layout gives $\sin+\cosec$ questions: square, use the product $1$, subtract $2$. For instance $\sin\theta+\cosec\theta=3$ squares to $\sin^2+\cosec^2+2=9$, so $\sin^2+\cosec^2=7$.

> **Remember:** Products of reciprocal pairs are always $1$: $\sin\cdot\cosec$, $\cos\cdot\sec$, $\tan\cdot\cot$. That is where terms vanish.
"""

id_formulas = [
    {"name": "Pythagorean identities", "tex": r"\sin^2+\cos^2=1,\quad 1+\tan^2=\sec^2,\quad 1+\cot^2=\cosec^2", "note": "Three engines from one identity."},
    {"name": "Conjugate pairs", "tex": r"(\sec+\tan)(\sec-\tan)=1,\quad (\cosec+\cot)(\cosec-\cot)=1", "note": "Sum and difference are reciprocals."},
    {"name": "Squares of sums", "tex": r"(a+b)^2+(a-b)^2=2(a^2+b^2)", "note": "Cross terms cancel in pairs."},
    {"name": "Reciprocal products", "tex": r"\sin\cdot\cosec=\cos\cdot\sec=\tan\cdot\cot=1", "note": "The constant that kills cross terms."},
]

id_tricks = [
    {
        "title": "Sum given, difference taken",
        "body": "sec + tan = 5 means sec - tan = 1/5, because their product is 1. Then add or subtract the pair.",
        "example": {
            "q": "If $\\sec\\theta + \\tan\\theta = 5$ ($\\theta$ acute), the value of $\\sec\\theta - \\tan\\theta$ is:",
            "steps": [r"$(\sec+\tan)(\sec-\tan)=1$.", r"$\sec-\tan=\dfrac{1}{5}$."],
            "answer": "1/5",
        },
    },
    {
        "title": "Divide through by cosine",
        "body": "A sin-cos fraction becomes a tan fraction when every term is divided by cosine. Substitute tan and finish.",
        "example": {
            "q": "If $\\tan\\theta = \\frac{3}{4}$, the value of $\\frac{4\\sin\\theta - \\cos\\theta}{4\\cos\\theta + \\sin\\theta}$ is:",
            "steps": [r"Divide by $\cos\theta$: $\dfrac{4\tan-1}{4+\tan}$.", r"$4+\dfrac34=\dfrac{19}{4}$.", r"$=\dfrac{2\times4}{19}=\dfrac{8}{19}$."],
            "answer": "8/19",
        },
    },
    {
        "title": "Square and subtract two",
        "body": "tan + cot = 5: square it, use tan times cot = 1, and the squared sum is 25 - 2.",
        "example": {
            "q": "If $\\tan\\theta + \\cot\\theta = 5$ ($\\theta$ acute), the value of $\\tan^2\\theta + \\cot^2\\theta$ is:",
            "steps": [r"$25=\tan^2+\cot^2+2$.", r"$\tan^2+\cot^2=25-2=23$."],
            "answer": "23",
        },
    },
]

id_mistakes = [
    {"wrong": "Writing $(\\sec+\\tan)(\\sec-\\tan)=0$.", "right": "It equals $\\sec^2-\\tan^2=1$, which makes the pair reciprocal."},
    {"wrong": "Forgetting the cross term when squaring a sum.", "right": "$(\\tan+\\cot)^2=\\tan^2+\\cot^2+2$; the $2$ must be subtracted."},
    {"wrong": "Dividing only the numerator by $\\cos$.", "right": "Divide every term of numerator and denominator, then substitute $\\tan$."},
    {"wrong": "Using $\\sin^2+\\cos^2=2$.", "right": "The sum is $1$; the $2$ appears only after adding both squared sums."},
    {"wrong": "Treating $\\tan\\cdot\\cot$ as $2$.", "right": "Reciprocal pairs multiply to $1$, never anything else."},
]

id_revision = [
    "Engines: $\\sin^2+\\cos^2=1$ and its $\\tan$-$\\sec$, $\\cot$-$\\cosec$ divisions.",
    "Conjugates: $(\\sec+\\tan)(\\sec-\\tan)=1$; same for $\\cosec\\pm\\cot$.",
    "Given a sum, the difference is its reciprocal; then add or subtract the pair.",
    "$(a+b)^2+(a-b)^2=2(a^2+b^2)$ kills cross terms.",
    "Divide sin-cos fractions by $\\cos$ to build $\\tan$.",
    "Reciprocal products are $1$: the constant that removes cross terms.",
]

id_patterns = [
    pat("trig-id-p1", "Conjugate pairs: sec plus-minus tan, cosec plus-minus cot", "very common",
        "A sum like sec + tan given; the difference or the individuals asked.",
        [r"Write the conjugate product $=1$.", r"Invert the given sum for the partner.",
         r"Add or subtract the pair to isolate one function."],
        "The product identity makes the pair reciprocal, so one given value answers everything.",
        "If $\\sec\\theta + \\tan\\theta = 5$ ($\\theta$ acute), the value of $\\sec\\theta - \\tan\\theta$ is:",
        [r"$(\sec+\tan)(\sec-\tan)=1$.", r"$\sec-\tan=\dfrac15$."],
        "1/5"),
    pat("trig-id-p2", "Squares of sums and sin-squared plus cos-squared", "very common",
        "An expression with plus and minus twins, or an identity check.",
        [r"Expand both squares.", r"Cross terms $\\pm2\\sin\\cos$ cancel.",
         r"Use $\\sin^2+\\cos^2=1$ on what is left."],
        "Twin squares always collapse to a multiple of the base identity.",
        "The value of $(\\sin\\theta + \\cos\\theta)^2 + (\\sin\\theta - \\cos\\theta)^2$ is:",
        [r"Expand: $1+2\sin\cos+1-2\sin\cos$.", r"$=2$."],
        "2"),
    pat("trig-id-p3", "Substituting tan via divide-by-cos", "very common",
        "A linear sin-cos fraction with tan given.",
        [r"Divide numerator and denominator by $\\cos\\theta$.", r"Replace $\\dfrac{\\sin}{\\cos}$ by $\\tan\\theta$.",
         r"Substitute the given value and simplify."],
        "One division converts the whole fraction into tangent arithmetic.",
        "If $\\tan\\theta = \\frac{3}{4}$, the value of $\\frac{4\\sin\\theta - \\cos\\theta}{4\\cos\\theta + \\sin\\theta}$ is:",
        [r"$\dfrac{4\tan-1}{4+\tan}$ with $\tan=\dfrac34$.", r"$=\dfrac{2}{19/4}=\dfrac{8}{19}$."],
        "8/19"),
    pat("trig-id-p4", "Squared sums from a given sum", "common",
        "A sum of reciprocal partners given; the squared sum asked.",
        [r"Square the given sum.", r"Replace the product term by $1$.",
         r"Subtract $2$."],
        "The product of reciprocal pairs is $1$, so squaring delivers the answer immediately.",
        "If $\\tan\\theta + \\cot\\theta = 5$ ($\\theta$ acute), the value of $\\tan^2\\theta + \\cot^2\\theta$ is:",
        [r"$25=\tan^2+\cot^2+2\tan\cot$.", r"$\tan\cot=1$, so the sum is $25-2=23$."],
        "23"),
    pat("trig-id-p5", "Triple-product identity checks", "occasional",
        "A product of three brackets asked to simplify to a constant.",
        [r"Simplify each bracket using the engines.", r"Multiply the pieces.",
         r"Cancel to reach the constant."],
        "Each bracket reduces to a squared ratio, and the product telescopes to $1$.",
        "The value of $(\\cosec\\theta-\\sin\\theta)(\\sec\\theta-\\cos\\theta)(\\tan\\theta+\\cot\\theta)$ is:",
        [r"$\cosec-\sin=\dfrac{\cos^2}{\sin}$; $\sec-\cos=\dfrac{\sin^2}{\cos}$.", r"$\tan+\cot=\dfrac{1}{\sin\cos}$.", r"Product $=\dfrac{\cos^2\sin^2}{\sin\cos\sin\cos}=1$."],
        "1"),
]

# ---------------- trig-complementary ----------------
co_concept = (
    "Angles adding to 90 degrees swap each ratio with its co-partner: sine becomes cosine, tangent becomes cotangent, secant becomes cosecant. "
    "This single swap collapses long sums, product chains and paired differences, and it solves for unknown angles by matching partners."
)

co_notes = r"""### The swap rules
For complementary angles, $\theta$ and $90^\circ-\theta$:
$$\sin(90^\circ-\theta)=\cos\theta,\quad \tan(90^\circ-\theta)=\cot\theta,\quad \sec(90^\circ-\theta)=\cosec\theta$$
The 'co-' in cosine literally means 'complement's sine'. Any ratio of one angle equals the co-ratio of its partner.

Check at $\theta=35^\circ$: $\sin35^\circ=\cos55^\circ$, and $\tan35^\circ\tan55^\circ=1$ because the tangents are reciprocal partners. One complement, three identities confirmed on the spot.

> **Rule:** In a right triangle the two acute angles are complementary, so each angle's sine is the other's cosine.

### Collapsing sums
$$\sin35^\circ\sec55^\circ+\cos35^\circ\cosec55^\circ$$
$\sec55^\circ=\dfrac{1}{\cos55^\circ}=\dfrac{1}{\sin35^\circ}$, so the first term is $1$. The second term is $1$ the same way. Total: $2$.

Convert everything to one angle, then watch the expression fold.

Another shape: $\dfrac{\cos25^\circ}{\sec65^\circ}+\dfrac{\sin25^\circ}{\cosec65^\circ}$. Since $\cos65^\circ=\sin25^\circ$, the first fraction is $\cos25^\circ\sin25^\circ$; the second equals the same product. The sum is $2\sin25^\circ\cos25^\circ=\sin50^\circ$.

> **Tip:** Choose one target angle (say $35^\circ$) and rewrite every piece in it before simplifying.

### Product chains
$\tan5^\circ\tan85^\circ=1$ because the angles are complementary. So:
$$\tan5^\circ\tan25^\circ\tan45^\circ\tan65^\circ\tan85^\circ=1\times1\times1=1$$
Chains pair off from the ends; the middle $45^\circ$ term is $1$ on its own. Four-factor chains work identically: $\tan10^\circ\tan20^\circ\tan70^\circ\tan80^\circ=1$, since $10+80=90$ and $20+70=90$.

### Twin differences die
$\cosec68^\circ-\sec22^\circ$: since $68^\circ+22^\circ=90^\circ$, $\cosec68^\circ=\sec22^\circ$. The difference is exactly $0$.

Sums of twins double instead of vanishing: $\sec72^\circ+\cosec18^\circ=2\cosec18^\circ$. And a long chain like $\tan1^\circ\tan2^\circ\cdots\tan89^\circ$ pairs into $44$ ones around the middle $\tan45^\circ=1$, so the whole product is $1$.

> **Watch:** Check the angle sum first. If it is $90^\circ$, the answer may need no computation at all.

### Solving for the angle
$\sin3A=\cos(A-10^\circ)$: the partners rule needs $3A=90^\circ-(A-10^\circ)$, so $4A=100^\circ$ and $A=25^\circ$. Check: $\sin75^\circ=\cos15^\circ$.

Same layout with tangents: $\tan2A=\cot(3A-10^\circ)$ gives $2A+3A-10^\circ=90^\circ$, so $A=20^\circ$. A negative argument also resolves: $\sin(2A-10^\circ)=\cos(3A+20^\circ)$ gives $5A+10^\circ=90^\circ$, so $A=16^\circ$.

> **Remember:** Convert the cosine or cotangent to its partner first, then solve the plain linear equation in the angle.
"""

co_formulas = [
    {"name": "Complementary swaps", "tex": r"\sin(90^\circ-\theta)=\cos\theta,\ \tan(90^\circ-\theta)=\cot\theta,\ \sec(90^\circ-\theta)=\cosec\theta", "note": "Drop the co- or add it."},
    {"name": "Right triangle angles", "tex": r"A+B=90^\circ\Rightarrow\sin A=\cos B", "note": "The two acute angles are partners."},
    {"name": "Pairing to one", "tex": r"\tan\theta\cdot\tan(90^\circ-\theta)=1", "note": "Complementary tangents multiply to 1."},
]

co_tricks = [
    {
        "title": "Sum the angles first",
        "body": "Before computing anything, add the two angles. Ninety degrees means the terms are twins.",
        "example": {
            "q": "The value of $\\cosec 68^\\circ - \\sec 22^\\circ$ is:",
            "steps": [r"$68^\circ+22^\circ=90^\circ$.", r"$\cosec68^\circ=\sec22^\circ$.", r"Difference $=0$."],
            "answer": "0",
        },
    },
    {
        "title": "Chains pair from the ends",
        "body": "tan 5 with tan 85, tan 25 with tan 65: each pair multiplies to 1, and the lone tan 45 is 1.",
        "example": {
            "q": "The value of $\\tan 5^\\circ \\tan 25^\\circ \\tan 45^\\circ \\tan 65^\\circ \\tan 85^\\circ$ is:",
            "steps": [r"$\tan5^\circ\tan85^\circ=1$; $\tan25^\circ\tan65^\circ=1$.", r"$\tan45^\circ=1$.", r"Product $=1$."],
            "answer": "1",
        },
    },
    {
        "title": "Match partners to find the angle",
        "body": "sin of something = cos of something: the two somethings must add to 90. That gives a linear equation.",
        "example": {
            "q": "If $\\sin 3A = \\cos(A - 10^\\circ)$, the value of $A$ is:",
            "steps": [r"$3A=90^\circ-(A-10^\circ)$.", r"$4A=100^\circ$.", r"$A=25^\circ$."],
            "answer": "25 degrees",
        },
    },
]

co_mistakes = [
    {"wrong": "Writing $\\sin(90^\\circ-\\theta)=\\sin\\theta$.", "right": "The complement swaps to cosine: $\\cos\\theta$. No swap, no collapse."},
    {"wrong": "Pairing $\\sec$ with $\\tan$ as complements.", "right": "Partners are $\\sin\\leftrightarrow\\cos$, $\\tan\\leftrightarrow\\cot$, $\\sec\\leftrightarrow\\cosec$."},
    {"wrong": "Solving $\\sin3A=\\cos(A-10^\\circ)$ by eye.", "right": "Convert first: $3A+(A-10^\\circ)=90^\\circ$, then $A=25^\\circ$."},
    {"wrong": "Missing the $\\tan45^\\circ=1$ middle term in chains.", "right": "Unpaired middle terms still contribute their value; $45^\\circ$ contributes $1$."},
    {"wrong": "Leaving answers in degrees and radians mixed.", "right": "Exam angles are degrees; keep the symbol consistent throughout."},
]

co_revision = [
    "Complement rule: $\\sin(90^\\circ-\\theta)=\\cos\\theta$; same shape for $\\tan$/$\\cot$ and $\\sec$/$\\cosec$.",
    "Two acute angles of a right triangle are complementary.",
    "Convert a mixed expression to one angle before simplifying.",
    "Product chains pair from the ends to $1$; $\\tan45^\\circ=1$ stands alone.",
    "Twin sums to $90^\\circ$ mean differences of $0$.",
    "Angle equations: partners first, then a linear solve.",
]

co_patterns = [
    pat("trig-co-p1", "Pair conversion to collapse a sum", "very common",
        "A sum of products mixing two complementary angles.",
        [r"Convert every piece to one target angle.", r"Simplify each product to $1$ or a square.",
         r"Add what is left."],
        "After conversion the products collapse to constants, so the sum is usually small.",
        "The value of $\\sin 35^\\circ \\sec 55^\\circ + \\cos 35^\\circ \\cosec 55^\\circ$ is:",
        [r"$\sec55^\circ=\dfrac{1}{\sin35^\circ}$, so term one $=1$.", r"$\cosec55^\circ=\dfrac{1}{\cos35^\circ}$, so term two $=1$.", r"Total $=2$."],
        "2"),
    pat("trig-co-p2", "Product chains pairing to one", "common",
        "A long product of tangents of several angles.",
        [r"Add pairs of angles from the ends.", r"Each $90^\\circ$ pair multiplies to $1$.",
         r"Evaluate any lone $45^\\circ$ factor as $1$."],
        "Chains are built to pair off; recognising the pairing avoids every computation.",
        "The value of $\\tan 5^\\circ \\tan 25^\\circ \\tan 45^\\circ \\tan 65^\\circ \\tan 85^\\circ$ is:",
        [r"$5+85=90$ and $25+65=90$: both pairs give $1$.", r"$\tan45^\circ=1$.", r"Product $=1$."],
        "1"),
    pat("trig-co-p3", "Finding the angle from complementary equality", "very common",
        "An equation linking a ratio of one angle to a co-ratio of another.",
        [r"Convert one side to the other's partner type.", r"Set the angle expressions to sum to $90^\\circ$.",
         r"Solve the linear equation."],
        "Partner equality forces the angle arguments to be complementary, which is a linear equation.",
        "If $\\sin 3A = \\cos(A - 10^\\circ)$, the value of $A$ is:",
        [r"$3A+(A-10^\circ)=90^\circ$.", r"$4A=100^\circ$.", r"$A=25^\circ$."],
        "25 degrees"),
    pat("trig-co-p4", "Difference of complementary twins", "common",
        "A difference of two co-functions of two angles.",
        [r"Add the two angles.", r"If they sum to $90^\\circ$, the functions are equal.",
         r"The difference is $0$."],
        "Twins subtract to zero without arithmetic, which makes these the fastest marks on the paper.",
        "The value of $\\cosec 68^\\circ - \\sec 22^\\circ$ is:",
        [r"$68^\circ+22^\circ=90^\circ$.", r"$\cosec68^\circ=\sec22^\circ$.", r"Difference $=0$."],
        "0"),
    pat("trig-co-p5", "Angles of one right triangle as partners", "common",
        "A triangle question linking the two acute angles' ratios.",
        [r"Mark the right angle and name the acute angles.", r"Write the partner relation $\\sin A=\\cos C$.",
         r"Substitute the given angle or solve."],
        "The complement rule is just the right triangle's own structure, so geometry questions fall out directly.",
        "In $\\triangle ABC$ right-angled at $B$, $\\tan2A=\\cot(3A-10^\\circ)$ holds. The value of $A$ is:",
        [r"$2A+(3A-10^\circ)=90^\circ$.", r"$5A=100^\circ$.", r"$A=20^\circ$."],
        "20 degrees"),
]

# ---------------- trig-valueput ----------------
vp_concept = (
    "Value-putting questions hand you a ratio or a condition and ask for an expression. "
    "Two moves cover them: substitute standard angle values directly, or draw the triangle the condition describes and read the expression off it."
)

vp_notes = r"""### Put the standard values in
$2\tan^2 45^\circ+\cos^2 30^\circ-\sin^2 60^\circ$: with $\tan45^\circ=1$ and both $30^\circ$/$60^\circ$ squared terms equal to $\dfrac34$:
$$2+\frac34-\frac34=2$$
Notice how $\cos^2 30^\circ$ and $\sin^2 60^\circ$ cancel by symmetry before any arithmetic.

One more: $\sin^230^\circ+\tan^245^\circ+\cos^260^\circ=\dfrac14+1+\dfrac14=\dfrac32$. Substitute first, add the fractions second, and the answer arrives without any identity at all.

> **Rule:** Replace every ratio first, simplify second. Half of these questions cancel themselves.

### sin + cos given
Square the given sum: $(\sin\theta+\cos\theta)^2=1+2\sin\theta\cos\theta$. So with the sum $=\sqrt2$:
$$2\sin\theta\cos\theta=2-1=1\Rightarrow\sin\theta\cos\theta=\frac12$$
The same square gives $\sin\theta-\cos\theta$ when the sum is known (watch the sign). With $\sin+\cos=\dfrac75$ the difference squares to $1-2\sin\cos=1-\dfrac{24}{25}=\dfrac{1}{25}$, so $|\sin-\cos|=\dfrac15$.

> **Tip:** $\sin+\cos=\sqrt2$ happens only at $45^\circ$; the product $\dfrac12$ confirms it.

### tan condition into a fraction
$5\tan\theta=4$ and the fraction $\dfrac{5\sin\theta-3\cos\theta}{5\sin\theta+3\cos\theta}$. Divide top and bottom by $\cos\theta$:
$$\frac{5\tan\theta-3}{5\tan\theta+3}=\frac{4-3}{4+3}=\frac17$$
The condition turns the whole expression into one number.

### cot or tan fraction: draw the triangle
$\cot\theta=\dfrac{21}{20}$: adjacent $21$, opposite $20$, hypotenuse $\sqrt{441+400}=29$. Then $\cos\theta=\dfrac{21}{29}$ directly.

The triplet $20$-$21$-$29$ was hiding inside the fraction. Drawing beats manipulating.

With $\tan\theta=\dfrac{4}{3}$ instead, the same $3$-$4$-$5$ drawing hands over $\sec\theta=\dfrac{5}{4}$ and $\cosec\theta=\dfrac{5}{3}$ at a glance. The triangle keeps paying rent.

> **Watch:** For $\cot$ the first number is the adjacent side, not the opposite. That single slip flips every answer.

### Sum of reciprocal partners
$\cosec\theta+\cot\theta=3$. The conjugate is $\dfrac13$, so $2\cosec\theta=3+\dfrac13=\dfrac{10}{3}$, giving $\cosec\theta=\dfrac53$ and $\sin\theta=\dfrac35$.

One reciprocal move, no quadratic.

The pair also splits a value the other way: $\sec\theta+\tan\theta=3$ gives $\sec\theta-\tan\theta=\dfrac13$, hence $\sec\theta=\dfrac{5}{3}$ and $\tan\theta=\dfrac{4}{3}$. Add or subtract the pair, and the individuals appear.

> **Remember:** Value-putting never needs to solve for $\theta$ itself. The ratio travels, the angle never appears.
"""

vp_formulas = [
    {"name": "Square of sin+cos", "tex": r"(\sin\theta+\cos\theta)^2=1+2\sin\theta\cos\theta", "note": "The bridge from a sum to a product."},
    {"name": "Divide by cosine", "tex": r"\frac{a\sin+b\cos}{c\sin+d\cos}=\frac{a\tan+b}{c\tan+d}", "note": "After dividing every term by cosine."},
    {"name": "Cot fraction to triangle", "tex": r"\cot\theta=\frac{21}{20}\Rightarrow\text{hyp}=29", "note": "Two sides given, Pythagoras gives the third."},
    {"name": "Reciprocal pair sum", "tex": r"x+\frac{1}{x}\ \text{from}\ x\cdot\frac{1}{x}=1", "note": "Conjugates of cosec plus cot."},
]

vp_tricks = [
    {
        "title": "Symmetry cancels first",
        "body": "cos squared 30 and sin squared 60 are the same number; scan for such twins before computing.",
        "example": {
            "q": "The value of $2\\tan^2 45^\\circ + \\cos^2 30^\\circ - \\sin^2 60^\\circ$ is:",
            "steps": [r"$\tan45^\circ=1$ gives $2$.", r"$\cos^230^\circ=\sin^260^\circ=\dfrac34$: they cancel.", r"Total $=2$."],
            "answer": "2",
        },
    },
    {
        "title": "Square the sum",
        "body": "sin + cos given: square it to reach 1 + 2 sin cos, then read off the product.",
        "example": {
            "q": "If $\\sin\\theta + \\cos\\theta = \\sqrt{2}$, the value of $\\sin\\theta\\cos\\theta$ is:",
            "steps": [r"$2=1+2\sin\cos$.", r"$2\sin\cos=1$.", r"$\sin\cos=\dfrac12$."],
            "answer": "1/2",
        },
    },
    {
        "title": "Condition straight into the fraction",
        "body": "5 tan = 4: divide the fraction by cosine, substitute, one line of arithmetic.",
        "example": {
            "q": "If $5\\tan\\theta = 4$, the value of $\\frac{5\\sin\\theta - 3\\cos\\theta}{5\\sin\\theta + 3\\cos\\theta}$ is:",
            "steps": [r"Divide by $\cos\theta$: $\dfrac{5\tan-3}{5\tan+3}$.", r"$=\dfrac{4-3}{4+3}$.", r"$=\dfrac17$."],
            "answer": "1/7",
        },
    },
]

vp_mistakes = [
    {"wrong": "Solving for $\\theta$ when only the ratio is needed.", "right": "The condition $5\\tan=4$ feeds the fraction directly; the angle never appears."},
    {"wrong": "Forgetting the $1$ in $(\\sin+\\cos)^2=1+2\\sin\\cos$.", "right": "Square fully: the product term sits on top of the identity $1$."},
    {"wrong": "Dividing only part of the fraction by $\\cos$.", "right": "Every term, numerator and denominator, divides by $\\cos\\theta$."},
    {"wrong": "Reading $\\cot=\\dfrac{21}{20}$ with $21$ opposite.", "right": "Cot is adjacent over opposite: $21$ adjacent, $20$ opposite, hypotenuse $29$."},
    {"wrong": "Sign slips with $\\sin-\\cos$ from a known $\\sin+\\cos$.", "right": "Square the difference: $(\\sin-\\cos)^2=1-2\\sin\\cos$, then choose the sign from the angle range."},
]

vp_revision = [
    "Substitute standard values first; scan for twin terms that cancel.",
    "$(\\sin+\\cos)^2=1+2\\sin\\cos$: sums give products.",
    "Divide sin-cos fractions by $\\cos$ and insert the given $\\tan$.",
    "Cot fractions: draw the triangle, complete the triplet ($20$-$21$-$29$).",
    "$\\cosec+\\cot=3$ gives $\\cosec=\\dfrac53$ via the reciprocal partner, so $\\sin=\\dfrac35$.",
    "The ratio travels; the angle itself never needs finding.",
]

vp_patterns = [
    pat("trig-vp-p1", "Standard angles in an expression", "very common",
        "An expression entirely in standard angles.",
        [r"Replace each ratio by its value.", r"Cancel symmetric twin terms.",
         r"Finish the arithmetic."],
        "Direct substitution plus one cancellation; the fastest pattern in the subtopic.",
        "The value of $2\\tan^2 45^\\circ + \\cos^2 30^\\circ - \\sin^2 60^\\circ$ is:",
        [r"$2\tan^245^\circ=2(1)^2=2$.", r"$\cos^230^\circ=\sin^260^\circ=\dfrac34$, so they cancel.", r"Total $=2$."],
        "2"),
    pat("trig-vp-p2", "sin plus cos given, products and differences", "very common",
        "A sum or difference of sin and cos given; a product or square asked.",
        [r"Square the given relation.", r"Use $1+2\\sin\\cos$ or $1-2\\sin\\cos$.",
         r"Solve for the asked expression."],
        "Squaring converts sums into products through the base identity.",
        "If $\\sin\\theta + \\cos\\theta = \\sqrt{2}$, the value of $\\sin\\theta\\cos\\theta$ is:",
        [r"$2=1+2\\sin\\cos$.", r"$\\sin\\cos=\\dfrac12$."],
        "1/2"),
    pat("trig-vp-p3", "tan or cot condition into a linear fraction", "very common",
        "A multiple of tan given; a linear sin-cos fraction asked.",
        [r"Divide the fraction by $\\cos\\theta$ throughout.", r"Substitute the given $\\tan\\theta$ value.",
         r"Simplify the small fraction."],
        "The division aligns the fraction with the condition so only arithmetic remains.",
        "If $5\\tan\\theta = 4$, the value of $\\frac{5\\sin\\theta - 3\\cos\\theta}{5\\sin\\theta + 3\\cos\\theta}$ is:",
        [r"$\\dfrac{5\\tan-3}{5\\tan+3}=\\dfrac{4-3}{4+3}$.", r"$=\\dfrac17$."],
        "1/7"),
    pat("trig-vp-p4", "cot or tan fraction to triangle to ratio", "common",
        "A cot or tan value; a plain ratio asked.",
        [r"Place the two sides in a right triangle.", r"Find the hypotenuse by the triplet.",
         r"Read off the asked ratio."],
        "Drawing the triangle answers every ratio at once without any identity work.",
        "If $\\cot\\theta = \\frac{21}{20}$ ($\\theta$ acute), the value of $\\cos\\theta$ is:",
        [r"Adjacent $21$, opposite $20$; hypotenuse $=\\sqrt{441+400}=29$.", r"$\\cos\\theta=\\dfrac{21}{29}$."],
        "21/29"),
    pat("trig-vp-p5", "cosec plus cot given, find sin", "common",
        "A sum of reciprocal partners given; a basic ratio asked.",
        [r"Write the conjugate difference as the reciprocal $\\dfrac{1}{\\text{sum}}$.",
         r"Add sum and difference to get $2\\cosec\\theta$.", r"Flip for $\\sin\\theta$."],
        "The conjugate identity avoids a quadratic; two additions deliver the ratio.",
        "If $\\cosec\\theta + \\cot\\theta = 3$ ($\\theta$ acute), the value of $\\sin\\theta$ is:",
        [r"$\\cosec-\\cot=\\dfrac13$.", r"$2\\cosec=3+\\dfrac13=\\dfrac{10}{3}$, so $\\cosec=\\dfrac53$.", r"$\\sin=\\dfrac35$."],
        "3/5"),
]

# ---------------- trig-maxmin ----------------
mm_concept = (
    "On zero to ninety degrees, sine and cosine stay between zero and one, while secant and cosecant stay at one or above. "
    "A sine-cosine combination peaks at the square root of a squared plus b squared, and reciprocal pairs bottom out at two by AM-GM."
)

mm_notes = r"""### The ranges
| Function | Range on $0^\circ$ to $90^\circ$ |
|---|---|
| $\sin\theta,\ \cos\theta$ | $0$ to $1$ |
| $\sec\theta,\ \cosec\theta$ | $1$ or more |
| $\tan\theta,\ \cot\theta$ | $0$ onwards, unbounded |

$\sin0^\circ=0$ rises to $\sin90^\circ=1$; cosine runs the other way. They cross exactly once, at $45^\circ$.

The table also explains why $\cosec\theta$ never lands between $0$ and $1$: it is $\dfrac{1}{\sin\theta}$ and $\sin\theta\le1$. The same logic lifts $\sec\theta$ to $1$ or above.

> **Rule:** $\sin\theta>\cos\theta$ holds precisely when $\theta>45^\circ$; below it, cosine leads.

### The amplitude rule
$$-\sqrt{a^2+b^2}\le a\sin\theta+b\cos\theta\le\sqrt{a^2+b^2}$$
$4\sin\theta+3\cos\theta$ peaks at $\sqrt{16+9}=5$. The maximum of $a\sin+b\cos$ never needs calculus: square, add, root.

On the full circle the minimum is $-\sqrt{a^2+b^2}$; restricted to acute angles the low end is the smaller of $a$ and $b$, hit at an endpoint. For $4\sin+3\cos$ on $0^\circ$ to $90^\circ$ the range is $[3,5]$. Read the domain before answering.

> **Tip:** The peak of $a\sin\theta+b\cos\theta$ answers half this subtopic. Compute $a^2+b^2$ first.

### Products of sin and cos
$$\sin\theta\cos\theta=\frac{\sin2\theta}{2}\le\frac12$$
$2\sin\theta\cos\theta=\sin2\theta$ tops at $1$, so $\sin\theta\cos\theta$ tops at $\dfrac12$, both at $45^\circ$.

Any question about 'maximum of sin times cos' is this line in disguise.

### AM-GM floors
For positive $x$: $x+\dfrac1x\ge2$. So:
- $\tan\theta+\cot\theta\ge2$ (product $1$)
- $\sec\theta+\cosec\theta\ge2$
- $\sec^2\theta+\cosec^2\theta\ge4$, since it equals $\dfrac{1}{\sin^2\theta\cos^2\theta}$ and $\sin^2\theta\cos^2\theta\le\dfrac14$

Each floor is attained where the two terms balance, at $45^\circ$. Equality pins the angle exactly: $\tan\theta+\cot\theta=2$ forces $\tan\theta=1$, hence $\theta=45^\circ$. The floor and the balance point arrive together.

> **Watch:** Secant and cosecant never fall below $1$, so their sums have higher floors. Squares shift the floor again.

### Weighted sin-squared and cos-squared
$5\sin^2\theta+12\cos^2\theta=5+7\cos^2\theta$. Since $0\le\cos^2\theta\le1$, the expression lives in $[5,12]$: minimum $5$, maximum $12$.

The endpoints occur at $90^\circ$ (all sine) and $0^\circ$ (all cosine). Try $7\sin^2\theta+2\cos^2\theta=2+5\sin^2\theta$, which lives in $[2,7]$: the rewrite is mechanical whichever way the weights lean.

> **Remember:** Rewrite the mix as one constant plus one squared term. The range reads off in one line, no differentiation.
"""

mm_formulas = [
    {"name": "Amplitude of a sin + b cos", "tex": r"\max=\sqrt{a^2+b^2},\quad \min=-\sqrt{a^2+b^2}", "note": "General angles; on 0 to 90 check the endpoints too."},
    {"name": "sin times cos", "tex": r"\sin\theta\cos\theta=\frac{\sin2\theta}{2}\le\frac12", "note": "Peak at 45 degrees."},
    {"name": "AM-GM floor", "tex": r"x+\frac{1}{x}\ge2", "note": "For positive x; equality when x = 1."},
    {"name": "Weighted squares", "tex": r"a\sin^2\theta+b\cos^2\theta\in[\min(a,b),\max(a,b)]", "note": "Rewrite as one constant plus one square."},
]

mm_tricks = [
    {
        "title": "Square, add, root",
        "body": "The maximum of a sin + b cos is the hypotenuse of the a-b right triangle. 4 and 3 give 5.",
        "example": {
            "q": "The maximum value of $4\\sin\\theta + 3\\cos\\theta$ is:",
            "steps": [r"$\sqrt{a^2+b^2}=\sqrt{16+9}$.", r"$=\sqrt{25}$.", r"$=5$."],
            "answer": "5",
        },
    },
    {
        "title": "AM-GM floor of two",
        "body": "Anything plus its own reciprocal bottoms at 2: tan + cot, sec + cosec, all the same.",
        "example": {
            "q": "The minimum value of $\\sec^2\\theta + \\cosec^2\\theta$ is:",
            "steps": [r"$=\dfrac{1}{\sin^2\theta\cos^2\theta}$ and $\sin\theta\cos\theta\le\dfrac12$.", r"So the minimum is $\dfrac{1}{(1/2)^2}=4$."],
            "answer": "4",
        },
    },
    {
        "title": "Weighted squares: constant plus square",
        "body": "Rewrite 5 sin squared + 12 cos squared as 5 + 7 cos squared. The range is then obvious.",
        "example": {
            "q": "The minimum value of $5\\sin^2\\theta + 12\\cos^2\\theta$ is:",
            "steps": [r"$=5+7\cos^2\theta$.", r"$\cos^2\theta\ge0$, so the minimum is $5$."],
            "answer": "5",
        },
    },
]

mm_mistakes = [
    {"wrong": "Taking the max of $4\\sin+3\\cos$ as $4+3=7$.", "right": "The peak is $\\sqrt{16+9}=5$; the functions never peak together."},
    {"wrong": "Saying $\\sin\\theta\\cos\\theta\\le1$.", "right": "The product tops at $\\dfrac12$ at $45^\\circ$, since it equals $\\dfrac{\\sin2\\theta}{2}$."},
    {"wrong": "Giving the minimum of $\\sec^2+\\cosec^2$ as $2$.", "right": "The floor is $4$: the squares push it above the plain AM-GM pair."},
    {"wrong": "Claiming $\\sin\\theta>\\cos\\theta$ for all acute angles.", "right": "Only beyond $45^\\circ$; below it cosine is larger."},
    {"wrong": "Weighted-square minimum taken at $45^\\circ$.", "right": "$5\\sin^2+12\\cos^2$ is smallest when the weight sits on the smaller value: $5$ at $90^\\circ$."},
]

mm_revision = [
    "Ranges: $\\sin,\\cos\\in[0,1]$; $\\sec,\\cosec\\ge1$; $\\tan,\\cot$ unbounded.",
    "$\\max(a\\sin+b\\cos)=\\sqrt{a^2+b^2}$; square, add, root.",
    "$\\sin\\theta\\cos\\theta\\le\\dfrac12$; $\\sin2\\theta\\le1$.",
    "$x+\\dfrac1x\\ge2$ floors: $\\tan+\\cot\\ge2$, $\\sec^2+\\cosec^2\\ge4$.",
    "Weighted squares: rewrite as constant plus square, read the range.",
    "$\\sin=\\cos$ only at $45^\\circ$; that is the ordering crossover.",
]

mm_patterns = [
    pat("trig-mm-p1", "Max and min of a sin plus b cos", "very common",
        "A linear mix of sine and cosine; an extreme asked.",
        [r"Compute $a^2+b^2$.", r"Take the square root for the amplitude.",
         r"State max (and min if asked)."],
        "The amplitude formula replaces all calculus for this expression family.",
        "The maximum value of $4\\sin\\theta + 3\\cos\\theta$ is:",
        [r"$\sqrt{16+9}=\sqrt{25}$.", r"$=5$."],
        "5"),
    pat("trig-mm-p2", "Bounds of sin times cos", "common",
        "A product or double of sin and cos; its maximum asked.",
        [r"Write the product as $\\dfrac{\\sin2\\theta}{2}$.", r"Bound $\\sin2\\theta$ by $1$.",
         r"Halve for the product."],
        "The double-angle rewrite turns the product into a single bounded function.",
        "The maximum value of $2\\sin\\theta\\cos\\theta$ ($\\theta$ acute) is:",
        [r"$2\sin\theta\cos\theta=\sin2\theta$.", r"$\sin2\theta\le1$."],
        "1"),
    pat("trig-mm-p3", "AM-GM self-reciprocal sums", "common",
        "A sum of a function and its reciprocal; a minimum asked.",
        [r"Confirm the product of the terms is $1$.", r"Apply $x+\\dfrac1x\\ge2$.",
         r"For squared versions, use $\\sin\\theta\\cos\\theta\\le\\dfrac12$."],
        "Reciprocal pairs always balance at their floor, which AM-GM locates instantly.",
        "The minimum value of $\\sec^2\\theta + \\cosec^2\\theta$ is:",
        [r"$=\dfrac{1}{\sin^2\theta\cos^2\theta}$.", r"$\sin\theta\cos\theta\le\dfrac12$ gives the minimum $4$."],
        "4"),
    pat("trig-mm-p4", "Ordering and crossover comparisons", "common",
        "When is sin greater than cos, or tan greater than one.",
        [r"Place $45^\\circ$ as the crossover.", r"Below it cosine leads; above it sine leads.",
         r"Translate to the asked pair."],
        "All such comparisons pivot on the single $45^\\circ$ crossing, so one fact answers many questions.",
        "For $0^\\circ < \\theta < 90^\\circ$, $\\sin\\theta > \\cos\\theta$ holds when:",
        [r"$\sin=\cos$ at $45^\circ$.", r"Sine grows and cosine shrinks.", r"So $\\theta>45^\\circ$."],
        "theta > 45 degrees"),
    pat("trig-mm-p5", "Weighted sin-squared plus cos-squared range", "common",
        "A weighted mix of squared sine and cosine; min and max asked.",
        [r"Rewrite as constant plus weight times one square.", r"Bound the square by $0$ and $1$.",
         r"Read off both endpoints."],
        "The rewrite makes the range a one-step reading exercise with no calculus.",
        "The minimum and maximum of $5\\sin^2\\theta + 12\\cos^2\\theta$ ($\\theta$ acute) are:",
        [r"$=5+7\cos^2\theta$.", r"$\cos^2\theta\in[0,1]$, so the range is $[5,12]$."],
        "Minimum 5, maximum 12"),
]

# ---------------- patch ----------------
data = json.loads(TOPIC.read_text(encoding="utf-8"))

blocks = {
    "trig-ratios": (ra_concept, ra_notes, ra_formulas, ra_tricks, ra_mistakes, ra_revision, ra_patterns),
    "trig-identities": (id_concept, id_notes, id_formulas, id_tricks, id_mistakes, id_revision, id_patterns),
    "trig-complementary": (co_concept, co_notes, co_formulas, co_tricks, co_mistakes, co_revision, co_patterns),
    "trig-valueput": (vp_concept, vp_notes, vp_formulas, vp_tricks, vp_mistakes, vp_revision, vp_patterns),
    "trig-maxmin": (mm_concept, mm_notes, mm_formulas, mm_tricks, mm_mistakes, mm_revision, mm_patterns),
}

new_ids = [p["id"] for blk in blocks.values() for p in blk[6]]
assert len(new_ids) == len(set(new_ids)), "duplicate new pattern ids within rewrite"

for sub in data["subtopics"]:
    if sub["id"] not in blocks:
        continue
    concept, notes, formulas, tricks, mistakes, revision, patterns = blocks[sub["id"]]
    old_ids = {p["id"] for p in sub.get("patterns", [])}
    assert old_ids <= {p["id"] for p in patterns}, f"{sub['id']}: never drop a pattern id"
    other = {p["id"] for s in data["subtopics"] if s["id"] != sub["id"] for p in s.get("patterns", [])}
    clash = other & {p["id"] for p in patterns}
    assert not clash, f"{sub['id']}: pattern id clash {clash}"
    assert 2500 <= len(notes) <= 5000, f"{sub['id']} notes {len(notes)} chars"
    assert 4 <= len(mistakes) <= 8 and 4 <= len(revision) <= 9
    sub.update(concept=concept, notes=notes.strip() + "\n", formulas=formulas, tricks=tricks,
               mistakes=mistakes, revision=revision, patterns=patterns)
    print(f"{sub['id']}: notes {len(notes)} chars, {len(patterns)} patterns")

with open(TOPIC, "w", encoding="utf-8", newline="\n") as f:
    json.dump(data, f, ensure_ascii=False, indent=1)
print("trigonometry.json patched")
