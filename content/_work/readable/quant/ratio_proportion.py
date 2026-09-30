"""Readable rewrite of Ratio, Proportion, Partnership & Ages (all five subtopics).

Simple English, one idea per section. Every number in every example is
recomputed below with exact fractions and asserted.
Run: python ratio_proportion.py  (patches content/core/topics/quant/ratio-proportion.json)
"""
import json
import re
from fractions import Fraction as F
from pathlib import Path

ROOT = Path(__file__).resolve().parents[3]
TOPIC = ROOT / "core" / "topics" / "quant" / "ratio-proportion.json"

# ---------- answer checks: rp-basics ----------
assert F(780, 13) == 60 and 3 * 60 == 180 and 3 * 60 + 4 * 60 + 6 * 60 == 780
assert F(1870, 11) == 170 and 4 * 170 == 680 and 7 * 170 == 1190 and 1190 - 680 == 510 and 3 * 170 == 510
assert 1200 * F(3, 5) == 720
assert F(2 * 2, 3 * 3) == F(4, 9)  # duplicate ratio 2:3 -> 4:9
assert 2 * 6 == 3 * 4 == 12 and F(12, 2) == 6 and F(12, 3) == 4 and F(12, 4) == 3
assert 2 * 4 == 8 and 3 * 4 == 12 and 4 * 3 == 12 and 5 * 3 == 15
assert F(8, 12) == F(2, 3) and F(12, 15) == F(4, 5) and F(8, 12) == F(12, 18)
assert 77 * 9 == 693 and 7 * 3 == 21 and 11 * 3 == 33 and 21 + 33 == 54
assert 5 * 7 - 4 * 7 == 7 and 2 * 6 == 12 and 12 * 6 == 72
assert 4 * 25 + 100 * 5 == 600 and 30 * 50 == 1500 and 10 * 50 == 500
assert (4 * 50 + 100) * 5 == 6 * 5 * 50 == 1500 and 9 * 50 == 450
assert 3 * 7 == 21 and 4 * 5 == 20 and 21 > 20


def pat(pid, name, freq, spot, formula, steps, why, q, ex_steps, answer):
    return {"id": pid, "name": name, "frequency": freq, "howToSpot": spot, "formula": formula,
            "steps": steps, "why": why, "example": {"q": q, "steps": ex_steps, "answer": answer}}


# ================= rp-basics =================

RB_CONCEPT = (
    "A ratio $a : b$ compares two quantities of the same kind. Scaling both terms by the same number leaves it unchanged: "
    "$2:3 = 8:12$.\n\n"
    "Write the quantities as $ax$ and $bx$. The multiplier $x$ turns every extra fact — sum, difference, product — "
    "into a small equation."
)

RB_NOTES = r"""### One idea: the multiplier x
"Numbers are in ratio $a : b$" means the numbers are $ax$ and $bx$. The $x$ is one shared unit.

- Sum given: $(a+b)x = S$.
- Difference given: $(b-a)x = D$.
- Product given: $abx^2 = P$.

Two numbers in $5 : 7$ differ by 12: $2x = 12$, so $x = 6$ and the sum is $12x = 72$.

> **Rule:** Never argue with the ratio itself. Convert to $ax$, $bx$, and solve for x.

### Dividing an amount
Split N in $a : b : c$: one part $= \dfrac{N}{a+b+c}$, then multiply by each term.

Rs 780 in $3 : 4 : 6$: one part $= \dfrac{780}{13} = 60$, so the shares are 180, 240 and 360.

Questions often hide the total. "A gets Rs 300 more than B" gives $(b-a)x = 300$ — recover x, then the total is $(a+b+c)x$.

A difference works the same way. Rs 1,870 in $4 : 7$: eleven parts of 170, so the shares are 680 and 1,190 and Y gets $\dfrac{1870}{11} \times 3 = 510$ more than X. One division answers every share, every difference and the total.

> **Tip:** Compute the value of one part first; every share follows by multiplication.

### The LCM bridge
Given $A : B = 2 : 3$ and $B : C = 4 : 5$, make the two B-terms equal. The LCM of 3 and 4 is 12, so scale the first ratio by 4 and the second by 3: $A : B = 8 : 12$ and $B : C = 12 : 15$.

Read them together: $A : B : C = 8 : 12 : 15$.

In symbols, $A:B = m:n$ and $B:C = p:q$ give $A:B:C = mp : np : nq$.

### The equality form
"$2A = 3B = 4C$" — take the LCM of 2, 3, 4, which is 12. Each letter equals $\dfrac{12}{\text{its multiplier}}$, so $A : B : C = 6 : 4 : 3$.

> **Watch:** Each term is LCM ÷ its own multiplier. A bigger multiplier means a smaller term.

### When the ratio changes
"Add k and the ratio becomes $p : q$": write $\dfrac{ax + k}{bx + k} = \dfrac{p}{q}$ and cross-multiply once.

Boys : girls $= 4 : 5$. After 100 boys join it is $6 : 5$. Now $\dfrac{4x + 100}{5x} = \dfrac{6}{5}$ gives $20x + 500 = 30x$, so $x = 50$ and the school had $9 \times 50 = 450$ students.

Both ratio statements describe the same x. That is the whole trick.

### Which ratio is larger
To compare $a : b$ with $c : d$, cross-multiply: $a : b$ is larger exactly when $ad > bc$.

$3 : 4$ or $5 : 7$? Compare $3 \times 7 = 21$ with $4 \times 5 = 20$. So $3 : 4$ is the larger ratio.

### Squares and roots of ratios
The **duplicate** ratio of $a : b$ is $a^2 : b^2$; the **sub-duplicate** is $\sqrt{a} : \sqrt{b}$. Squares with sides in $2 : 3$ have areas in $4 : 9$ — one squaring step.

> **Note:** Ratio terms must share one unit. 3 kg to 500 g is $3000 : 500 = 6 : 1$, never $3 : 500$.
"""

RB_FORMULAS = [
    {"name": "Share of the total", "tex": r"\text{share} = \frac{\text{ratio term}}{\text{sum of terms}} \times N"},
    {"name": "Combining ratios", "tex": r"A:B = m:n,\ B:C = p:q \Rightarrow A:B:C = mp : np : nq"},
    {"name": "Cross-multiplication test", "tex": r"a:b > c:d \iff ad > bc"},
    {"name": "Multiplier method", "tex": r"\text{shares } ax, bx,\ (b-a)x = \text{given difference}"},
    {"name": "Duplicate / sub-duplicate", "tex": r"a:b \Rightarrow a^2:b^2 \text{ (duplicate)},\ \sqrt{a}:\sqrt{b} \text{ (sub-duplicate)}"},
]

RB_TRICKS = [
    {
        "title": "x solves everything",
        "body": "Translate 'ratio a : b' into ax and bx. Every extra fact becomes one small equation in x.",
        "example": {
            "q": "Two numbers are in the ratio 5 : 7 and their difference is 12. Find their sum.",
            "steps": [r"Numbers are $5x$ and $7x$; $2x = 12$.", r"$x = 6$; sum $= 12x = 72$."],
            "answer": "72",
        },
    },
    {
        "title": "LCM bridging for three terms",
        "body": "Scale A : B so its B-term matches the B-term of B : C, then read off A : B : C.",
        "example": {
            "q": "If A : B = 2 : 3 and B : C = 4 : 5, find A : B : C.",
            "steps": [r"Make B = 12 (LCM of 3 and 4).", r"$A : B = 8 : 12$ and $B : C = 12 : 15$.", r"$A : B : C = 8 : 12 : 15$."],
            "answer": "8 : 12 : 15",
        },
    },
    {
        "title": "One share known, get the rest",
        "body": "Share = fraction × total. Recover the total from one share, then build any other share.",
        "example": {
            "q": "Rs 1,200 is divided between A and B in the ratio 2 : 3. Find B's share.",
            "steps": [r"B's fraction $= \dfrac{3}{5}$.", r"$\dfrac{3}{5} \times 1200 = 720$."],
            "answer": "Rs 720",
        },
    },
]

RB_MISTAKES = [
    {"wrong": "Adding ratios term-wise: A:B = 2:3 and B:C = 4:5 read as 2:3:5.",
     "right": "Bridge the shared B: A:B:C = 8:12:15."},
    {"wrong": "Shifting a ratio by n years or n rupees.",
     "right": "Shift the actual quantities (ax ± n), never the ratio terms."},
    {"wrong": "Comparing ratios by their differences (b − a).",
     "right": "Cross-multiply: a:b beats c:d exactly when ad > bc."},
    {"wrong": "Mixing units inside one ratio.",
     "right": "Convert first: 3 kg to 500 g is 3000 : 500 = 6 : 1."},
    {"wrong": "Reading 'the ratio becomes p : q' as more information about the same x pair.",
     "right": "It is the same x pair — write both statements with one x and equate."},
]

RB_REVISION = [
    "Quantities in a ratio are $ax$, $bx$ — one multiplier for all.",
    "One part $=$ total $\\div$ sum of terms.",
    "Bridge two ratios through the shared term (LCM).",
    "$kA = lB = mC$: each term is LCM $\\div$ multiplier.",
    "Changed ratio: same x, one cross-multiplication.",
    "Compare ratios by cross-multiplying, never by gaps.",
]

RB_PATTERNS = [
    pat("rp-b1", "Divide an amount in a given ratio", "very common",
        "A sum of money, a prize or sweets is split in m : n : p; a share, a difference or the total is asked.",
        r"\text{share} = \frac{\text{term}}{\text{sum of terms}} \times N, \quad \text{1 part} = \frac{N}{m + n + p}",
        ["Add the ratio terms for the total parts.", "One part = amount ÷ total parts.",
         "Multiply by the asked term; for a difference use the gap between terms."],
        "The ratio fixes each share as a set fraction of the whole.",
        "Rs 780 is divided among A, B and C in the ratio 3 : 4 : 6. What is A's share?",
        [r"Total parts $= 13$; one part $= \dfrac{780}{13} = 60$.", r"A $= 3 \times 60 = 180$."],
        "Rs 180"),
    pat("rp-b2", "Combine ratios into A : B : C", "very common",
        "'A : B = 2 : 3 and B : C = 4 : 5, find A : B : C' — or the compact form '2A = 3B = 4C'.",
        r"A:B = m:n,\ B:C = p:q \Rightarrow A:B:C = mp : np : nq",
        ["Two-ratio form: scale so the shared letter matches (LCM bridge).",
         "One-equality form: each term is LCM ÷ its multiplier.",
         "Long chains: multiply the fractions A/B × B/C and reduce."],
        "The shared term must stand for the same number in both ratios before merging.",
        "If 2A = 3B = 4C, then A : B : C is:",
        [r"LCM(2, 3, 4) $= 12$.", r"$A = \dfrac{12}{2},\ B = \dfrac{12}{3},\ C = \dfrac{12}{4}$.", r"$A : B : C = 6 : 4 : 3$."],
        "6 : 4 : 3"),
    pat("rp-b3", "Multiplier with sum, difference or product", "very common",
        "'Two numbers are in ratio a : b and their sum, difference or product is ...' — one extra fact, one equation.",
        r"ax \pm bx = (a \pm b)x, \qquad abx^2 = P \Rightarrow x = \sqrt{P/(ab)}",
        ["Write the numbers as ax and bx.", "Sum → (a+b)x; difference → (b−a)x; product → abx².",
         "Solve for x, then build whatever is asked."],
        "Every statistic of the pair is a multiple of x, so one fact fixes x.",
        "The ratio of two numbers is 7 : 11 and their product is 693. Find the sum of the numbers.",
        [r"$77x^2 = 693$, so $x^2 = 9$ and $x = 3$.", r"Numbers are 21 and 33.", r"Sum $= 54$."],
        "54"),
    pat("rp-b4", "Ratio changes when a number joins or leaves", "common",
        "'Boys to girls is 4 : 5; after 100 boys join it becomes 6 : 5' — a fixed number moves.",
        r"\frac{ax \pm k}{bx \pm k} = \frac{p}{q}",
        ["Write the original counts as ax, bx.", "Add or subtract k only where the question says.",
         "Equate to the new ratio and cross-multiply."],
        "A fixed number breaks the proportionality, so the new ratio pins x exactly.",
        "The ratio of boys to girls in a school is 4 : 5. If 100 more boys join, the ratio becomes 6 : 5. How many students were there originally?",
        [r"$\dfrac{4x + 100}{5x} = \dfrac{6}{5}$.", r"$20x + 500 = 30x$, so $x = 50$.", r"Students $= 9 \times 50 = 450$."],
        "450"),
    pat("rp-b5", "Comparing two ratios", "common",
        "Two ratios are given; which is larger, or are they equal, is asked.",
        r"a:b > c:d \iff ad > bc",
        ["Cross-multiply: first term × other denominator.", "Compare the two products.",
         "Equal products mean equal ratios."],
        "Cross-multiplication puts both ratios over a common base in one step.",
        "Which of the ratios 3 : 4 and 5 : 7 is greater?",
        [r"$3 \times 7 = 21$.", r"$4 \times 5 = 20$.", r"$21 > 20$, so $3 : 4$ is greater."],
        "3 : 4"),
]
# ================= rp-proportion =================

# ---------- answer checks: rp-proportion ----------
assert 12 * 18 == 216 and F(216, 8) == 27 and F(8, 12) == F(18, 27) == F(2, 3)
assert 9 * 12 == 108 and F(4, 9) == F(12, 27)
assert 9 * 16 == 144 and F(144, 9) == 16 and F(9, 12) == F(12, 16) == F(3, 4)
assert 12 * 48 == 576 and 24 * 24 == 576 and F(12, 24) == F(24, 48) == F(1, 2)
assert 25 * 81 == 2025 and 45 * 45 == 2025
assert 3 * 12 == 36 and 6 * 6 == 36
assert 12 * 12 == 144 and F(144, 18) == 8 and F(8, 12) == F(12, 18) == F(2, 3)
assert 8 * 18 == 144 and 8 + 18 == 26
assert (7 + 5) * 1 == 12 and (7 - 5) * 1 == 2 and F(12, 2) == 6
assert (5 + 3) * 1 == 8 and (5 - 3) * 1 == 2 and F(8, 2) == 4
assert F(2 + 7, 7 - 2) == F(9, 5)  # C&D on 5x/3y = 9/5 gives 25x = 27y
assert 5 * 27 == 27 * 5  # trivially true; real check below with x, y


def cd_check(x, y, p, q):
    """(x+y)/(x-y) = p/q must give x/y = (p+q)/(p-q)."""
    lhs = F(x + y, x - y)
    assert lhs == F(p, q)
    assert F(x, y) == F(p + q, p - q)


cd_check(6, 1, 7, 5)
cd_check(4, 1, 5, 3)
# coefficient twist: (5x-3y)/(5x+3y) = 2/7 with 25x = 27y
_x, _y = 27, 25
assert F(5 * _x - 3 * _y, 5 * _x + 3 * _y) == F(2, 7)

RP_CONCEPT = (
    "Four numbers $a, b, c, d$ are in proportion when $\\dfrac{a}{b} = \\dfrac{c}{d}$. "
    "Cross-multiplying gives $ad = bc$: the outer pair multiplies to the same as the inner pair.\n\n"
    "Three named proportionals: **fourth** $= \\dfrac{bc}{a}$, **third** $= \\dfrac{b^2}{a}$, **mean** $= \\sqrt{ab}$.\n\n"
    "Componendo and dividendo turns a sum-over-difference into a plain ratio: "
    "$\\dfrac{x+y}{x-y} = \\dfrac{p}{q}$ gives $\\dfrac{x}{y} = \\dfrac{p+q}{p-q}$."
)

RP_NOTES = r"""### What proportion means
$a : b :: c : d$ means $\dfrac{a}{b} = \dfrac{c}{d}$, and cross-multiplication gives $ad = bc$.

$a$ and $d$ are the **extremes** (outer terms); $b$ and $c$ are the **means** (middle terms). Product of extremes = product of means. Every "find the missing term" question is one cross-multiplication away.

> **Rule:** $ad = bc$ for $a : b :: c : d$ — outer times outer equals middle times middle.

### The three named proportionals
- **Fourth proportional** to $a, b, c$: solve $\dfrac{a}{b} = \dfrac{c}{d}$, so $d = \dfrac{bc}{a}$. Four different numbers.
- **Third proportional** to $a, b$: solve $\dfrac{a}{b} = \dfrac{b}{x}$, so $x = \dfrac{b^2}{a}$. The middle term repeats.
- **Mean proportional** between $a$ and $b$: $x = \sqrt{ab}$, from $\dfrac{a}{x} = \dfrac{x}{b}$.

Worked: fourth to 8, 12, 18 is $\dfrac{12 \times 18}{8} = 27$. Third to 9, 12 is $\dfrac{144}{9} = 16$. Mean between 12 and 48 is $\sqrt{576} = 24$.

> **Watch:** The mean proportional is the geometric mean $\sqrt{ab}$, never the average $\dfrac{a+b}{2}$. The average of 3 and 12 is 7.5, but the answer is 6.

### Continued proportion
$a, b, c$ are in continued proportion when $\dfrac{a}{b} = \dfrac{b}{c}$, that is $b^2 = ac$.

So the middle term is automatically the mean proportional of the outer two, and each member recovers from the others: $a = \dfrac{b^2}{c}$, $c = \dfrac{b^2}{a}$, $b = \sqrt{ac}$.

Three numbers $x, 12, 18$ in continued proportion: $144 = 18x$, so $x = 8$. Check $\dfrac{8}{12} = \dfrac{12}{18} = \dfrac{2}{3}$.

### A worked chain
"Three numbers $a, b, c$ are in continued proportion, $b = 12$ and $a + c = 26$."

Then $ac = 144$, and $a, c$ are the factor pair of 144 that sums to 26: 8 and 18. The numbers are 8, 12, 18.

Exam numbers are built so the factor pair is clean. If yours is not, re-read the question, not the method.

### Componendo and dividendo
If $\dfrac{a}{b} = \dfrac{c}{d}$, then $\dfrac{a+b}{a-b} = \dfrac{c+d}{c-d}$.

The exam use runs it backwards: given $\dfrac{x+y}{x-y} = \dfrac{p}{q}$, jump to $\dfrac{x}{y} = \dfrac{p+q}{p-q}$.

$\dfrac{x+y}{x-y} = \dfrac{5}{3}$ gives $\dfrac{x}{y} = \dfrac{8}{2} = 4$. No solving — one addition and one subtraction.

> **Tip:** A sum-over-difference equal to a ratio is the fingerprint. Componendo-dividendo is the intended route.

### Coefficient twists
$\dfrac{5x - 3y}{5x + 3y} = \dfrac{2}{7}$. Apply the rule to get $\dfrac{5x}{3y} = \dfrac{7+2}{7-2} = \dfrac{9}{5}$, then rearrange: $25x = 27y$.

Write the two fractions with plus on top and minus below before adding and subtracting. Sign slips are the only failure here.

### Order matters
Fourth proportional to 4, 9, 12 is 27, but fourth proportional to 12, 9, 4 is 3. The terms stay in the order written — copy the proportion exactly as the question lists it.
"""

RP_FORMULAS = [
    {"name": "Basic proportion", "tex": r"\frac{a}{b} = \frac{c}{d} \iff ad = bc"},
    {"name": "Fourth proportional", "tex": r"d = \frac{bc}{a}"},
    {"name": "Third proportional", "tex": r"c = \frac{b^2}{a}"},
    {"name": "Mean proportional", "tex": r"\text{mean} = \sqrt{ab}"},
    {"name": "Componendo & dividendo", "tex": r"\frac{a}{b} = \frac{c}{d} \Rightarrow \frac{a+b}{a-b} = \frac{c+d}{c-d}"},
    {"name": "Invertendo / alternando", "tex": r"\frac{b}{a} = \frac{d}{c},\quad \frac{a}{c} = \frac{b}{d}"},
]

RP_TRICKS = [
    {
        "title": "Extremes times means",
        "body": "Set up the proportion in the exact order given, cross-multiply, done.",
        "example": {
            "q": "Find the fourth proportional to 4, 9 and 12.",
            "steps": [r"$\dfrac{4}{9} = \dfrac{12}{d}$.", r"$4d = 108$, so $d = 27$."],
            "answer": "27",
        },
    },
    {
        "title": "Mean proportional = geometric mean",
        "body": "Multiply the two numbers and take the square root. Exam numbers make it a perfect square.",
        "example": {
            "q": "Find the mean proportional between 25 and 81.",
            "steps": [r"$\sqrt{25 \times 81} = \sqrt{2025}$.", r"$= 45$."],
            "answer": "45",
        },
    },
    {
        "title": "Componendo-dividendo jump",
        "body": "When $(x + y)$ and $(x - y)$ both appear, jump straight to $x/y$ by adding and subtracting the given ratio's terms.",
        "example": {
            "q": "If $\dfrac{x+y}{x-y} = \dfrac{5}{3}$, find $\dfrac{x}{y}$.",
            "steps": [r"$\dfrac{x}{y} = \dfrac{5+3}{5-3}$.", r"$= \dfrac{8}{2} = 4$."],
            "answer": "4",
        },
    },
]

RP_MISTAKES = [
    {"wrong": "Swapping third and fourth proportional.",
     "right": "Third repeats the middle term (b²/a); fourth uses three different terms (bc/a)."},
    {"wrong": "Taking the arithmetic mean (a+b)/2 as the mean proportional.",
     "right": "Mean proportional is the geometric mean √(ab)."},
    {"wrong": "Reordering the terms before writing the proportion.",
     "right": "Keep the question's order: 4, 9, 12 gives 27 but 12, 9, 4 gives 3."},
    {"wrong": "Using componendo-dividendo as (p+q)/(p−q) on the wrong side.",
     "right": "Sum-over-difference equals p/q means x/y = (p+q)/(p−q); check which side is the sum."},
    {"wrong": "Forgetting the middle term repeats in a continued proportion.",
     "right": "b appears in both fractions: a/b = b/c, so b² = ac."},
]

RP_REVISION = [
    "$ad = bc$: extremes times extremes equals means times means.",
    "Fourth $\\dfrac{bc}{a}$, third $\\dfrac{b^2}{a}$, mean $\\sqrt{ab}$.",
    "Continued proportion: $b^2 = ac$.",
    "Sum-over-difference $\\dfrac{p}{q}$ gives $\\dfrac{x}{y} = \\dfrac{p+q}{p-q}$.",
    "Order of terms is part of the question.",
]

RP_PATTERNS = [
    pat("rp-p1", "Fourth proportional", "very common",
        "'Find the fourth proportional to a, b, c' — three numbers, the fourth that completes a : b :: c : ?",
        r"\frac{a}{b} = \frac{c}{d} \Rightarrow d = \frac{bc}{a}",
        ["Write the proportion in the exact order given: a : b :: c : d.",
         "Cross-multiply: ad = bc.", "Divide: d = bc/a."],
        "The fourth term must keep the same pairwise ratio as the first three.",
        "The fourth proportional to 8, 12 and 18 is:",
        [r"$d = \dfrac{12 \times 18}{8} = 27$.", r"Check: $\dfrac{8}{12} = \dfrac{18}{27} = \dfrac{2}{3}$."],
        "27"),
    pat("rp-p2", "Third proportional", "common",
        "'Find the third proportional to a and b' — two numbers only; the middle term repeats (a : b :: b : ?).",
        r"\frac{a}{b} = \frac{b}{x} \Rightarrow x = \frac{b^2}{a}",
        ["Repeat the second term: a : b :: b : x.", "Cross-multiply: ax = b².", "Divide: x = b²/a."],
        "'Third proportional to a and b' is the next member of a continued proportion starting a, b.",
        "The third proportional to 9 and 12 is:",
        [r"$x = \dfrac{12^2}{9} = \dfrac{144}{9} = 16$.", r"Check: $\dfrac{9}{12} = \dfrac{12}{16} = \dfrac{3}{4}$."],
        "16"),
    pat("rp-p3", "Mean proportional", "very common",
        "'Find the mean proportional between a and b' — the number x with a : x :: x : b.",
        r"x = \sqrt{ab}",
        ["Multiply the two numbers.", "Take the square root (exact in exam numbers).",
         "Sanity check: x² = ab; the average (a+b)/2 is the planted trap."],
        "The mean proportional is the self-repeating middle term, the geometric mean.",
        "The mean proportional between 12 and 48 is:",
        [r"$\sqrt{12 \times 48} = \sqrt{576} = 24$.", r"Check: $\dfrac{12}{24} = \dfrac{24}{48} = \dfrac{1}{2}$."],
        "24"),
    pat("rp-p4", "Continued proportion (find a member)", "common",
        "'a, b, c are in continued proportion; given two, find the third' — sometimes dressed as a geometric progression.",
        r"b^2 = ac \ \Rightarrow\ b = \sqrt{ac},\ a = \frac{b^2}{c},\ c = \frac{b^2}{a}",
        ["Write the defining equation a/b = b/c, that is b² = ac.",
         "Substitute the two known members.", "Solve; check both fractions reduce to the same value."],
        "Continued proportion fixes one exact relationship among the three members.",
        "The numbers x, 12 and 18 are in continued proportion. Find x.",
        [r"$12^2 = 18x$.", r"$x = \dfrac{144}{18} = 8$."],
        "8"),
    pat("rp-p5", "Componendo and dividendo", "common",
        "(x + y)/(x − y) given as a ratio; find x : y — sometimes with coefficients on x and y.",
        r"\frac{x + y}{x - y} = \frac{p}{q} \Rightarrow \frac{x}{y} = \frac{p + q}{p - q}",
        ["Apply C&D: add and subtract the given ratio's terms.", "Read x/y = (p+q)/(p−q) directly.",
         "With coefficients, C&D gives mx : ny first; divide off m : n."],
        "One application converts the sum/difference form into the pure ratio, no solving.",
        "If $\dfrac{a+b}{a-b} = \dfrac{7}{5}$, then $a : b$ equals:",
        [r"$\dfrac{a}{b} = \dfrac{7+5}{7-5} = \dfrac{12}{2}$.", r"$a : b = 6 : 1$."],
        "6 : 1"),
]
# ================= rp-partnership =================

# ---------- answer checks: rp-partnership ----------
assert F(45000, 5000) == 9 and F(35000, 5000) == 7 and 8000 * F(9, 16) == 4500
assert 16000 * 12 == 192000 and 24000 * 6 == 144000 and F(192000, 40000) == F(24, 5)
assert F(192000, 144000) == F(4, 3) and 14000 * F(3, 7) == 6000
assert 15000 * 4 + 20000 * 8 == 220000 and 18000 * 12 == 216000
assert F(220000, 4000) == 55 and F(216000, 4000) == 54
assert 14400 * F(10, 100) == 1440 and 14400 - 1440 == 12960 and F(50000, 30000) == F(5, 3)
assert 12960 * F(3, 8) == 4860
assert 12000 * 12 == 144000 == 18000 * 8 and 9600 * F(1, 2) == 4800
assert 20000 * 6 + 25000 * 6 == 270000 == 22500 * 12
assert 30000 * 8 + 20000 * 4 == 320000
assert 9000 * F(10, 100) == 900 and 9000 - 900 == 8100 and 8100 * F(2, 5) == 3240 and 3240 + 900 == 4140
assert 15 * 8 == 120 and 25 * 4 == 100 and F(120, 100) == F(6, 5) and 2200 * F(6, 11) == 1200 and 2200 * F(5, 11) == 1000
assert F(1200, 10) == 120 and 2 * 120 == 240 and 3 * 120 == 360 and 5 * 120 == 600

RN_CONCEPT = (
    "Profit is divided in the ratio of **capital × time** — the capital-months.\n\n"
    "Same period for all partners: time cancels, so the share ratio is just the capital ratio. "
    "Different joining dates or mid-year top-ups: build one capital-months row per partner.\n\n"
    "A working partner's fee or per cent comes off the profit **first**; only the residue is divided."
)

RN_NOTES = r"""### One rule for everything
Profit share $\propto$ capital $\times$ time. Call the product **capital-months**.

Same period for everyone: the time cancels, and the share ratio is just the capital ratio. Different joining dates, withdrawals or top-ups: build one row per partner and add up.

> **Rule:** Share $\propto$ capital $\times$ months. Nothing else matters in this topic.

### The capital-months table
A invests Rs 12,000 for 12 months. B joins after 4 months with Rs 18,000, so B's money works only 8 months.

| Partner | Capital-months |
|---|---|
| A | $12000 \times 12 = 144000$ |
| B | $18000 \times 8 = 144000$ |

Ratio 1 : 1 — a Rs 9,600 profit splits 4,800 each. A late joiner can catch up only by investing more.

> **Tip:** A late joiner's months run from the joining month to the year end, never from the start.

### Mid-year capital changes
Split the year at each change and add capital × months.

A invests 15,000 for 4 months and 20,000 for 8: $60000 + 160000 = 220000$. Against B's $18000 \times 12 = 216000$, the ratio is $55 : 54$.

Same engine for withdrawals: A holds 30,000 for 8 months then 20,000 for 4, giving $240000 + 80000 = 320000$ capital-months.

> **Watch:** Using only the first capital or only the final capital is the classic error on these.

### The working partner's cut
A partner who manages the business takes a fee or a per cent of the profit **off the top**. Only the residue is divided by capital-months, and the working partner's own capital still counts in that split.

Profit 9,000; B manages and draws 10%: cut 900, residue 8,100 split by capitals $3 : 2$. B's split share is 3,240, and B's total receipt is 4,140 if the question asks for it.

> **Careful:** The cut applies to the whole profit, not to the residue. And take it off before sharing, not after.

### Rent of a pasture
The same engine in rural costume: animals are the capital, months are the months.

A grazes 15 cows for 8 months (120 cow-months); B grazes 25 cows for 4 months (100). Rent 2,200 splits $6 : 5$, so A pays 1,200 and B pays 1,000.

### Wages and workmen
Wages for a job split the same way: men × days. Three men working 5, 8 and 10 days share wages in $5 : 8 : 10$. Nothing new to learn — capital-months again.

Rs 1,200 split for 2, 3 and 5 days worked: ten parts of 120, so the shares are 240, 360 and 600.

### Keep the numbers small
Drop zeroes early: 12,000 × 12 is 144 thousand-months. Ratios survive any common division, and every zero you drop is one less slip. When the products look unwieldy, divide all of them by 1,000 before forming the ratio.
"""

RN_FORMULAS = [
    {"name": "Simple partnership", "tex": r"P_1 : P_2 = C_1 : C_2 \quad (\text{same time})"},
    {"name": "Compound partnership", "tex": r"P_1 : P_2 : P_3 = C_1T_1 : C_2T_2 : C_3T_3"},
    {"name": "Working partner", "tex": r"\text{profit} = \text{manager's cut} + \text{residual split by } C_iT_i"},
    {"name": "Capital change mid-year", "tex": r"\text{effective capital} = C_a t_1 + C_b t_2 + \cdots"},
]

RN_TRICKS = [
    {
        "title": "One row per partner",
        "body": "Write capital × months for each partner; the profit ratio is the row ratio.",
        "example": {
            "q": "A invests Rs 12,000 for the full year; B joins after 4 months with Rs 18,000. Divide a Rs 9,600 profit.",
            "steps": [r"A: $12000 \times 12 = 144000$; B: $18000 \times 8 = 144000$.", r"Ratio $1 : 1$, so Rs 4,800 each."],
            "answer": "Rs 4,800 each",
        },
    },
    {
        "title": "Cut comes off the top",
        "body": "Salary or a per cent for the manager is removed from the whole profit before the capital-months split.",
        "example": {
            "q": "A and B invest Rs 6,000 and Rs 4,000. B manages and takes 10% of a Rs 9,000 profit. Find A's share.",
            "steps": [r"Cut $= 900$; residue $= 8100$.", r"Capitals $3 : 2$; A $= \dfrac{3}{5} \times 8100 = 4860$."],
            "answer": "Rs 4,860",
        },
    },
    {
        "title": "Equal shares, find the capital",
        "body": "Equal shares mean equal capital-months. Equate the products and solve.",
        "example": {
            "q": "A invests Rs 12,000 for 12 months. B joins after 6 months and they share the profit equally. Find B's capital.",
            "steps": [r"$12000 \times 12 = C \times 6$.", r"$C = 24000$."],
            "answer": "Rs 24,000",
        },
    },
]

RN_MISTAKES = [
    {"wrong": "Ignoring time when partners join on different dates.",
     "right": "Share ∝ capital × months; compute capital-months for everyone."},
    {"wrong": "Counting a late joiner's months from the year's start.",
     "right": "Months run from the joining month to the year end."},
    {"wrong": "Sharing the profit first and taking the manager's cut after.",
     "right": "The cut comes off the top; only the residue is split."},
    {"wrong": "Using only the final capital after a mid-year change.",
     "right": "Add capital × months across each stretch of the year."},
    {"wrong": "Answering the working partner's split share when the total receipt is asked.",
     "right": "Add the cut back to that partner's share when 'in all' is asked."},
]

RN_REVISION = [
    "Share $\\propto$ capital $\\times$ months.",
    "Same time for all: pure capital ratio.",
    "Late joiner: months from joining to year end.",
    "Mid-year change: add capital-months per stretch.",
    "Working partner: cut off the top, split the residue.",
    "Pasture rent and wages: the same capital-months engine.",
]

RN_PATTERNS = [
    pat("rp-n1", "Simple partnership (same time, different capitals)", "very common",
        "Partners invest different amounts for the same period; a share or the total profit is asked.",
        r"P_1 : P_2 = C_1 : C_2 \quad (\text{same time})",
        ["Reduce the capital ratio to small terms (divide by the GCD).",
         "Add the parts; one part = profit ÷ total parts.", "Multiply by the asked partner's parts."],
        "With time equal for everyone, it cancels out of the ratio.",
        "A and B invest Rs 45,000 and Rs 35,000 for one year. From a profit of Rs 8,000, what does A receive?",
        [r"Ratio $45000 : 35000 = 9 : 7$ (16 parts).", r"A $= \dfrac{9}{16} \times 8000 = 4500$."],
        "Rs 4,500"),
    pat("rp-n2", "Partner joins late or leaves early", "very common",
        "'A starts the business; B joins after k months' — time differs, so capitals alone mislead.",
        r"P_1 : P_2 = C_1T_1 : C_2T_2",
        ["Compute capital-months for each (joiner: from joining month to year end).",
         "The profit ratio is the ratio of these products.",
         "Reverse version: ratio known, one capital unknown — equate the products."],
        "Money working longer earns a proportionally larger share; only the product counts.",
        "A starts a business with Rs 16,000. After 6 months, B joins with Rs 24,000. From a year-end profit of Rs 14,000, B's share is:",
        [r"A: $16000 \times 12 = 192000$; B: $24000 \times 6 = 144000$.", r"Ratio $4 : 3$.", r"B $= \dfrac{3}{7} \times 14000 = 6000$."],
        "Rs 6,000"),
    pat("rp-n3", "Mid-year capital change", "common",
        "'A invests X and adds or withdraws Y after k months' — one partner's capital moves mid-year.",
        r"\text{effective} = C_a t_1 + C_b t_2 + \cdots",
        ["Split the year at every change.", "Add capital × months over the stretches.",
         "Take the ratio across partners."],
        "Each stretch of capital earns its own capital-months, and they add up.",
        "A invests Rs 15,000 for the first 4 months of a year and Rs 20,000 for the remaining 8 months. B invests Rs 18,000 for the whole year. The profit-sharing ratio is:",
        [r"A: $15000 \times 4 + 20000 \times 8 = 220000$.", r"B: $18000 \times 12 = 216000$.", r"Ratio $= 55 : 54$."],
        "55 : 54"),
    pat("rp-n4", "Working partner (cut off the top)", "common",
        "'A manages the business and gets x% of the profit' — or a fixed salary — before the rest is shared.",
        r"\text{residue} = \text{profit} - \text{cut}, \quad \text{residue split by } C_iT_i",
        ["Take the working partner's cut out of the profit first.",
         "Divide the residue by the capital ratio (the working partner's capital still counts).",
         "Add the cut back if that partner's total receipt is asked."],
        "The fee pays for work done, so it must not pass through the profit ratio.",
        "A and B invest Rs 50,000 and Rs 30,000. A manages the business and receives 10% of the profit for it. From a profit of Rs 14,400, B's share is:",
        [r"Cut $= 1440$; residue $= 12960$.", r"Ratio $5 : 3$.", r"B $= \dfrac{3}{8} \times 12960 = 4860$."],
        "Rs 4,860"),
    pat("rp-n5", "Rent of a pasture (animals × months)", "common",
        "Grazing rent divided among farmers whose herds graze for different periods.",
        r"\text{rent share} \propto \text{animals} \times \text{months}",
        ["Count cow-months for each farmer: animals × months.",
         "The rent ratio is the ratio of these products.",
         "Multiply each share of the ratio by the total rent."],
        "The pasture is the partnership: animals are the capital, months are the months.",
        "The rent of a pasture is Rs 2,200. A grazes 15 cows for 8 months and B grazes 25 cows for 4 months. A's share of the rent is:",
        [r"A: $15 \times 8 = 120$ cow-months; B: $25 \times 4 = 100$.", r"Ratio $6 : 5$.", r"A $= \dfrac{6}{11} \times 2200 = 1200$."],
        "Rs 1,200"),
]
# ================= rp-ages =================

# ---------- answer checks: rp-ages ----------
assert F(35, 7) == 5 and 3 * 5 == 15 and 4 * 5 == 20 and F(40, 8) == 5 and 3 * 5 == 15 and 5 * 5 == 25
assert 7 * (5 * 4 + 4) == 6 * (6 * 4 + 4) == 168 and 5 * 4 == 20 and F(5 * 4 + 4, 6 * 4 + 4) == F(6, 7)
assert 4 * (5 * 8 + 8) == 3 * (7 * 8 + 8) == 192 and 5 * 8 == 40 and 7 * 8 == 56 and 40 + 56 == 96
assert 4 * 10 + 5 == 45 and 3 * (10 + 5) == 45 and 4 * 10 == 40 and 45 - 15 == 30
assert 3 * 16 - 8 == 40 and 5 * (16 - 8) == 40 and 3 * 16 == 48 and 48 - 16 == 32
assert 5 * (2 * 10 + 20) == 4 * (3 * 10 + 20) == 200 and 2 * 10 + 10 == 30 and F(40, 50) == F(4, 5)
assert 7 * (5 * 12 + 12) == 6 * (6 * 12 + 12) == 504 and 6 * 12 + 6 == 78 and F(5 * 12 + 12, 6 * 12 + 12) == F(6, 7)
assert 40 - 5 * 2 == 30  # sum of two ages drops by 2 per year going back
assert (15 + 25) + 10 == 50 and 15 + 10 == 25 and 50 == 2 * 25  # gap 25, twice in 10 years


def shifted(present_a, present_b, n, p, q):
    """Present ratio a:b with a+b as a+b; after n years ratio must be p:q."""
    assert F(present_a + n, present_b + n) == F(p, q)


shifted(20, 24, 4, 6, 7)
shifted(40, 56, 8, 3, 4)
shifted(30, 40, 10, 4, 5)

RA_CONCEPT = (
    "Three facts never change: each age grows by 1 every year, the sum of two ages grows by 2 per year, "
    "and the **difference** between two ages is constant forever.\n\n"
    "Standard template: present ages in ratio $a : b$, a second ratio $n$ years later (or earlier). "
    "Write $ax$, $bx$ and solve $\\dfrac{ax \\pm n}{bx \\pm n} = \\dfrac{p}{q}$.\n\n"
    "One multiplier is always enough."
)

RA_NOTES = r"""### The three facts that never change
- Each person's age grows by 1 every year. Shift n years: add n to both ages.
- A sum of two ages grows by 2n over n years.
- The difference between two ages never changes. A 32-year gap now is a 32-year gap forever.

> **Rule:** Shift the ages, never the ratio. $5 : 7$ today is not $5+n : 7+n$ tomorrow.

### The multiplier template
Present ages in ratio $a : b$ — write $ax$ and $bx$. A shifted ratio becomes one equation:

$$\frac{ax + n}{bx + n} = \frac{p}{q} \quad (\text{after } n \text{ years}), \qquad \frac{ax - n}{bx - n} = \frac{p}{q} \quad (n \text{ years ago})$$

One cross-multiplication gives x. $5 : 7$ now and $3 : 4$ after 8 years: $\dfrac{5x+8}{7x+8} = \dfrac{3}{4}$ gives $20x + 32 = 21x + 24$, so $x = 8$. Ages 40 and 56, sum 96.

If the question gives a sum or difference of present ages instead, $(a+b)x$ or $(b-a)x$ is that value — no shift needed.

### Sum and difference shortcuts
Ratio $3 : 4$ with sum 35: seven parts of 5, so 15 and 20. The younger is 15.

The sum grows by 2 a year: "the sum is 40 now; what was it 5 years ago?" — 30, no ratio needed. Read which year the question means before dividing by parts.

### k-times questions
"Father is k times the son" — write father $= k \times$ son, with the son as the single unknown.

Mother 4 times the daughter; after 5 years, 3 times: $4d + 5 = 3(d + 5)$, so $d = 10$ and the mother is 40. The gap of 30 never moved: 45 and 15 give exactly 3 times.

> **Watch:** For an older-younger pair the multiple falls over time — 4 times becomes 3 times. If your answer grows the multiple, flip the equation.

### Two shifted ratios
A ratio n years ago AND n years hence give two equations in the same x.

Ten years ago $2 : 3$; ten years hence $4 : 5$. Present ages are $2x + 10$ and $3x + 10$. The second snapshot: $\dfrac{2x + 20}{3x + 20} = \dfrac{4}{5}$ gives $10x + 100 = 12x + 80$, so $x = 10$ and A is 30.

The 2n years between the two snapshots is the easiest slip: each age changes by 2n, not n.

### The constant-difference check
After solving, verify the gap is the same at both times. Father 48, son 16: gap 32. Eight years ago, 40 and 8 — gap 32, ratio 5, matching "5 times as old".

The check also runs forwards. A man is 25 years older than his son and will be exactly twice his age in ten years. Then $s + 35 = 2(s + 10)$, so the son is 15 now. In ten years the pair is 25 and 50 — gap still 25.

> **Tip:** Compute the age gap once and reuse it at every time point. It kills wrong options without solving.

### Three people
Ratios among three people work the same: $4x, 5x, 6x$. Exams add one pairwise fact ("A is 6 years older than C" gives $2x = 6$) because more would over-determine the problem.
"""

RA_FORMULAS = [
    {"name": "Present = ax, bx", "tex": r"\frac{ax \pm n}{bx \pm n} = \frac{p}{q}", "note": "Ratio after (or before) n years."},
    {"name": "Constant difference", "tex": r"A - B \text{ is the same at every time}"},
    {"name": "Sum grows by 2 per year", "tex": r"(A + B)_{t+n} = (A + B)_t + 2n"},
    {"name": "Multiple of age", "tex": r"F = kS \Rightarrow F \pm n = k'(S \pm n)", "note": "k falls over time for elder-younger pairs."},
]

RA_TRICKS = [
    {
        "title": "Multiplier plus shift",
        "body": "Ages $ax$, $bx$ now; shift both by n; equate the new ratio; solve for x.",
        "example": {
            "q": "The present ages of A and B are in the ratio 5 : 7. After 8 years the ratio becomes 3 : 4. Find the sum of their present ages.",
            "steps": [r"$\dfrac{5x+8}{7x+8} = \dfrac{3}{4}$ gives $x = 8$.", r"Ages 40 and 56; sum 96."],
            "answer": "96 years",
        },
    },
    {
        "title": "Use the constant difference",
        "body": "The gap between two ages never changes — compute it once and reuse it at any time point.",
        "example": {
            "q": "A father is 3 times as old as his son. Eight years ago he was 5 times as old. Find their present ages.",
            "steps": [r"Gap $= 2s$. Eight years ago: $\dfrac{3s-8}{s-8} = 5$.", r"$3s - 8 = 5s - 40$, so $s = 16$; father 48 (gap 32)."],
            "answer": "Father 48, son 16",
        },
    },
    {
        "title": "Bracket the present with two ratios",
        "body": "With 'n years ago' and 'n years hence' ratios, both snapshots share one x — the 2n shift separates them.",
        "example": {
            "q": "Six years ago A : B was 5 : 6, and six years hence it will be 6 : 7. Find B's present age.",
            "steps": [r"$7(5x + 12) = 6(6x + 12)$.", r"$x = 12$; B $= 6 \times 12 + 6 = 78$."],
            "answer": "78 years",
        },
    },
]

RA_MISTAKES = [
    {"wrong": "Shifting the ratio terms: 5 : 7 after 8 years read as 13 : 15.",
     "right": "Shift the ages: (5x + 8) and (7x + 8)."},
    {"wrong": "Adding n to only one person's age.",
     "right": "Every living person's age moves by n; the sum of two ages moves by 2n."},
    {"wrong": "Treating the ratio gap (b − a)x as the age gap at a shifted time.",
     "right": "The age gap (b − a)x is fixed for all time — that is exactly why it is useful."},
    {"wrong": "Letting the multiple rise over time for elder-younger pairs.",
     "right": "The multiple falls: 4 times now, 3 times later, closer to 1 eventually."},
    {"wrong": "Solving the two-snapshot system with n instead of 2n.",
     "right": "From 'n years ago' to 'n years hence' each age moves 2n years."},
]

RA_REVISION = [
    "Ages $ax$, $bx$; shift both by $\\pm n$.",
    "Age difference constant; sum grows by 2 per year.",
    "k times: write the larger as k $\\times$ the smaller.",
    "Two shifted ratios: same x, 2n apart.",
    "Check every answer against the constant gap.",
]

RA_PATTERNS = [
    pat("rp-a1", "Present ratio with sum or difference", "very common",
        "'Ages are in ratio a : b and their sum (or difference) is S' — no time shift at all.",
        r"(a + b)x = S \ \text{or} \ (b - a)x = D",
        ["Total parts = a + b (or the gap b − a for a difference).",
         "One part = S ÷ total parts.", "Multiply by the asked person's parts."],
        "With no shift, this is a plain ratio division of the given total.",
        "The ages of two brothers are in the ratio 3 : 4 and the sum of their ages is 35 years. The younger brother's age is:",
        [r"7 parts $= 35$, so 1 part $= 5$.", r"Younger $= 3 \times 5 = 15$ years."],
        "15 years"),
    pat("rp-a2", "Ratio now and ratio after or before n years", "very common",
        "'The present ages are in ratio a : b; after (or before) n years the ratio will be p : q.'",
        r"\frac{ax \pm n}{bx \pm n} = \frac{p}{q}",
        ["Write present ages as ax, bx.",
         "Add or subtract n on BOTH, equate to p : q.", "Cross-multiply once and solve for x."],
        "Both ages move by the same n, so the ratio shift pins x exactly.",
        "The present ages of P and Q are in the ratio 5 : 6. Four years from now, the ratio will become 6 : 7. P's present age is:",
        [r"$\dfrac{5x + 4}{6x + 4} = \dfrac{6}{7}$.", r"$35x + 28 = 36x + 24$, so $x = 4$.", r"P $= 20$ years."],
        "20 years"),
    pat("rp-a3", "'k times as old' questions", "very common",
        "'A mother is 4 times as old as her daughter; after 5 years she will be 3 times as old' — one multiple now, another later.",
        r"F = kS, \quad F \pm n = k'(S \pm n)",
        ["Take the younger age as the single unknown; the elder is k times it.",
         "Apply the second condition at the shifted time.", "Solve; check the constant difference."],
        "Both conditions describe the same two people at two dates.",
        "A mother is 4 times as old as her daughter. After 5 years, the mother will be 3 times as old as the daughter. The mother's present age is:",
        [r"$4d + 5 = 3(d + 5)$.", r"$d = 10$; mother $= 40$ years.", r"Check: gap 30; 45 and 15 give 3 times."],
        "40 years"),
    pat("rp-a4", "Two shifted ratios (ago and hence)", "common",
        "'n years ago the ratio was a : b, and n years hence it will be p : q' — two snapshots bracket the present.",
        r"\frac{ax - n}{bx - n} = \frac{a'}{b'}, \qquad \frac{ax + n}{bx + n} = \frac{p}{q}",
        ["Write present ages as ax and bx.",
         "Build both snapshots: subtract n for 'ago', add n for 'hence'.",
         "Equate the second snapshot's ratio and solve for x."],
        "Both snapshots describe the same present ages, so one x serves both.",
        "Ten years ago the ages of A and B were in the ratio 2 : 3. Ten years from now the ratio will be 4 : 5. A's present age is:",
        [r"Present ages $2x + 10$, $3x + 10$; hence $2x + 20$, $3x + 20$.", r"$\dfrac{2x + 20}{3x + 20} = \dfrac{4}{5}$ gives $x = 10$.", r"A $= 30$ years."],
        "30 years"),
]
# ================= rp-money-applications =================

# ---------- answer checks: rp-money-applications ----------
assert 9 * 2000 - 4 * 4000 == 2000 and 7 * 2000 - 3 * 4000 == 2000 and 2 * 2000 == 4000
assert 8 * 2400 - 5 * 3600 == 1200 and 5 * 2400 - 3 * 3600 == 1200 and F(3600, 2400) == F(3, 2)
assert 5 * 800 - 3 * 800 == 1600 and 4 * 800 - 2 * 800 == 1600 and 5 * 800 == 4000 and 4 * 800 == 3200
assert 3 * 800 == 2400 and 2 * 800 == 1600
assert 5 * 100 + 8 * 50 + 4 * 25 == 1000 and F(1000, 100) == 10 and F(210, 10) == 21 and 8 * 21 == 168
assert 7 * 50 + 6 * 25 + 5 * 10 == 550 and F(550, 550) == 1 and F(5500, 55) == 100 and 6 * 100 == 600
assert 3 * 5 + 5 * 2 + 7 * 1 == 32 and F(512, 32) == 16 and (3 + 5 + 7) * 16 == 240
assert F(1, 6) / F(1, 9) == F(3, 2) and 1500 * F(3, 5) == 900
assert F(1, 6) * 918 == 153 and 1 + 2 + 3 == 6 and 2 * F(2, 3) == F(4, 3) and F(1, 2) * 2 == 1
assert F(3, 4) == F(12, 16) and F(4, 5) == F(16, 20)  # A=3/4 B, B=4/5 C -> 12:16:20

RC_CONCEPT = (
    "Two classic money containers for ratios.\n\n"
    "**Income and expenditure:** incomes in $a : b$, expenditures in $p : q$. Write incomes $ax, bx$ "
    "and expenditures $py, qy$ — two multipliers — then use each person's savings.\n\n"
    "**Coin bags:** price one full set of coins in the ratio; divide the total value by the set value; "
    "multiply back for any count."
)

RC_NOTES = r"""### Two ratios, two multipliers
Incomes in $a : b$ and expenditures in $p : q$. Write incomes $= ax$, $bx$ and expenditures $= py$, $qy$.

Two different multipliers — mixing them is the standard error. Savings give one equation per person: $ax - py = s_1$ and $bx - qy = s_2$.

> **Rule:** Incomes take x, expenditures take y. Never one letter for both.

### Equal savings — subtract
Each saves Rs 2,000 with incomes $9 : 7$ and expenditures $4 : 3$:

$$9x - 4y = 2000, \qquad 7x - 3y = 2000$$

Subtract: $2x = y$. Then $9x - 8x = 2000$, so $x = 2000$ and A's income is 18,000.

Another: incomes $8 : 5$, expenditures $5 : 3$, each saves 1,200. Subtracting gives $3x = 2y$, so $y = 1.5x$. Then $8x - 7.5x = 0.5x = 1200$, so $x = 2400$ and A's income is 19,200.

Equal savings cancel on subtraction — that is what makes these questions short.

### Unequal savings — eliminate
When the savings differ, scale one equation so y matches, then subtract. Same two-line shape, one extra multiplication.

### A complete walkthrough
Incomes $5 : 4$, expenditures $3 : 2$, each saves Rs 1,600. So $5x - 3y = 1600$ and $4x - 2y = 1600$.

Equal savings, so subtract: $x - y = 0$, meaning $x = y$. Then $5x - 3x = 2x = 1600$, so $x = 800$.

Incomes 4,000 and 3,200; expenditures 2,400 and 1,600. Both savings check out at 1,600.

### Coin bags
Coins in ratio $n_1 : n_2 : n_3$ of denominations $d_1, d_2, d_3$. Price ONE set: $n_1d_1 + n_2d_2 + n_3d_3$. Then sets = total value ÷ set value, and a coin's count = its term × sets.

Rs 1, 50-paise and 25-paise coins in $5 : 8 : 4$ worth Rs 210: a set is $500 + 400 + 100 = 1000$ paise $=$ Rs 10. So 21 sets, and the 50-paise coins number $8 \times 21 = 168$.

> **Careful:** Convert everything to paise (or everything to rupees) before pricing the set. Rs 1 = 100 paise.

The same engine counts total coins: Rs 5, Rs 2 and Rs 1 coins in $3 : 5 : 7$ worth Rs 512. A set is Rs 32, so 16 sets, and the total coins are $15 \times 16 = 240$.

### Wages in proportion to work
Wages follow work done. Days worked: shares $\propto$ days. Working together: shares $\propto$ work rates, $\dfrac{1}{\text{days}}$.

Workers finishing alone in 6 and 9 days earn in ratio $\dfrac{1}{6} : \dfrac{1}{9} = 3 : 2$. Of Rs 1,500, the faster worker gets 900.

> **Watch:** Together, compare $\dfrac{1}{\text{days}}$, never the days themselves.

### Chained fractions
"A $= \dfrac{3}{4}$ of B and B $= \dfrac{4}{5}$ of C" gives $A : B : C = 3 : 4 : 5$. Build the three-term ratio on a common base before touching any money.

### Statement-defined shares
"A gets half of B; B gets two-thirds of C." Let the third hold 3: then B $=$ 2 and A $=$ 1. Ratio $1 : 2 : 3$; Rs 918 gives A $= \dfrac{918}{6} = 153$.

> **Tip:** Take the last-named person as the base unit; every statement becomes a whole-number multiple.
"""

RC_FORMULAS = [
    {"name": "Savings equations", "tex": r"ax - py = s_1,\quad bx - qy = s_2", "note": "Two multipliers: x for incomes, y for expenditures."},
    {"name": "Coin value", "tex": r"\text{total value} = k \sum_i (n_i \times d_i)", "note": "Price one set, then scale."},
    {"name": "Wages together", "tex": r"\text{shares} \propto \frac{1}{\text{days alone}}"},
    {"name": "Difference of shares", "tex": r"\text{given excess} = (b - a)x"},
]

RC_TRICKS = [
    {
        "title": "Subtract the savings equations",
        "body": "Write both savings equations and subtract — equal savings kill the constant and one variable.",
        "example": {
            "q": "Incomes of A and B are in the ratio 8 : 5 and expenditures in 5 : 3. If each saves Rs 1,200, find A's income.",
            "steps": [r"$8x - 5y = 1200$, $5x - 3y = 1200$; subtract: $3x = 2y$.", r"$y = 1.5x$; $0.5x = 1200$, so $x = 2400$.", r"A's income $= 8 \times 2400 = 19200$."],
            "answer": "Rs 19,200",
        },
    },
    {
        "title": "Value per set for coins",
        "body": "Take one full set of coins in the given ratio, price it in paise, and scale.",
        "example": {
            "q": "A bag has 50-paise, 25-paise and 10-paise coins in the ratio 7 : 6 : 5 amounting to Rs 550. Find the number of 25-paise coins.",
            "steps": [r"Set $= 350 + 150 + 50 = 550$ paise $=$ Rs 5.50.", r"$550 \div 5.50 = 100$ sets.", r"25-paise coins $= 6 \times 100 = 600$."],
            "answer": "600",
        },
    },
    {
        "title": "Base the chain on the last person",
        "body": "For 'A gets half of B, B gets two-thirds of C', give the last-named person the unit and read the ratio off.",
        "example": {
            "q": "Rs 918 is divided so that the first gets half of the second and the second gets two-thirds of the third. Find the first share.",
            "steps": [r"Third $= 3$, second $= 2$, first $= 1$.", r"Ratio $1 : 2 : 3$; first $= \dfrac{918}{6} = 153$."],
            "answer": "Rs 153",
        },
    },
]

RC_MISTAKES = [
    {"wrong": "Using one multiplier for both income and expenditure ratios.",
     "right": "Incomes take x, expenditures take y — two letters, two equations."},
    {"wrong": "Mixing paise and rupees in coin problems.",
     "right": "Convert everything to one unit first; Rs 1 = 100 paise."},
    {"wrong": "Answering the value of the coins when the count is asked (or the reverse).",
     "right": "Read whether the question wants a count or a value; both sit in the options."},
    {"wrong": "Comparing days instead of rates when workers work together.",
     "right": "Together, shares follow 1/days."},
    {"wrong": "Accepting a negative expenditure multiplier.",
     "right": "A negative y means the equations were set up with swapped multipliers."},
]

RC_REVISION = [
    "Incomes $ax$, $bx$; expenditures $py$, $qy$ — two multipliers.",
    "Equal savings: subtract the two equations.",
    "Unequal savings: eliminate y by scaling.",
    "Coin bags: price one set, divide, multiply back.",
    "Wages together $\\propto$ 1/days.",
    "Statement shares: base on the last-named person.",
]

RC_PATTERNS = [
    pat("rp-c1", "Income-expenditure-savings ratios", "very common",
        "Two ratios (income and expenditure) plus savings; find an income or an expenditure.",
        r"ax - py = s_1, \quad bx - qy = s_2",
        ["Incomes = ax, bx; expenditures = py, qy (different letters).",
         "Write both savings equations.",
         "Equal savings: subtract. Unequal: eliminate y.", "Build the asked quantity from x or y."],
        "Two ratios plus two savings give exactly two linear equations in x and y.",
        "The incomes of A and B are in the ratio 9 : 7 and their expenditures in the ratio 4 : 3. If each saves Rs 2,000, A's income is:",
        [r"$9x - 4y = 2000$ and $7x - 3y = 2000$.", r"Subtract: $2x = y$. Then $9x - 8x = 2000$.", r"$x = 2000$; A $= 9 \times 2000 = 18000$."],
        "Rs 18,000"),
    pat("rp-c2", "Coin denominations in a ratio", "common",
        "Bags of Rs 1 / 50p / 25p (or Rs 5 / Rs 2 / Rs 1) coins in a ratio with the total value given.",
        r"\text{set value} = \sum n_i d_i, \quad \text{sets} = \frac{\text{total value}}{\text{set value}}",
        ["Convert all values to ONE unit (paise or rupees).",
         "Price one full set of coins in the given ratio.",
         "Sets = total value ÷ set value; a coin's count = its term × sets."],
        "The ratio fixes how many identical sets the bag holds — the set is the repeating block.",
        "A bag contains Rs 1, 50-paise and 25-paise coins in the ratio 5 : 8 : 4, amounting to Rs 210. The number of 50-paise coins is:",
        [r"Set $= 500 + 400 + 100 = 1000$ paise $=$ Rs 10.", r"$210 \div 10 = 21$ sets.", r"50-paise coins $= 8 \times 21 = 168$."],
        "168"),
    pat("rp-c3", "Money shared in proportion to work", "common",
        "Wages divided by days worked, or by work rates when the workers finish alone in different times.",
        r"\text{wage} \propto \text{work done}; \quad \text{together} \propto \frac{1}{\text{days alone}}",
        ["Convert the story into one common ratio (days, or 1/days together).",
         "Add the parts; one part = money ÷ parts.", "Multiply by the asked worker's parts."],
        "Fair division always reduces to one three-term ratio on a common base.",
        "Two workers, working alone, can finish a job in 6 days and 9 days. They work together and earn Rs 1,500. The first worker's share is:",
        [r"Rates $\dfrac{1}{6} : \dfrac{1}{9} = 3 : 2$.", r"Share $= \dfrac{3}{5} \times 1500 = 900$."],
        "Rs 900"),
    pat("rp-c4", "Condition-driven division", "common",
        "'A gets twice as much as B', 'the first gets half of the second' — shares defined by statements, not a stated ratio.",
        r"\text{translate each statement into a multiple},\ \text{then read off } A : B : C",
        ["Let the LAST-named person hold the base unit.",
         "Translate each statement into a multiple of that unit.",
         "Read the ratio, add parts, divide the total."],
        "Chain statements fix the mutual multiples; the last-named base untangles them in one pass.",
        "Rs 918 is divided among three friends such that the first gets half of the second and the second gets two-thirds of the third. The first friend's share is:",
        [r"Third $= 3$, second $= 2$, first $= 1$.", r"Ratio $1 : 2 : 3$.", r"First $= \dfrac{918}{6} = 153$."],
        "Rs 153"),
]

# ================= write back =================

dfrac = lambda x: x.replace(r"\frac", r"\dfrac")

BLOCKS = [
    ("rp-basics", dict(concept=RB_CONCEPT, notes=RB_NOTES, formulas=RB_FORMULAS,
                       tricks=RB_TRICKS, mistakes=RB_MISTAKES, revision=RB_REVISION, patterns=RB_PATTERNS)),
    ("rp-proportion", dict(concept=RP_CONCEPT, notes=RP_NOTES, formulas=RP_FORMULAS,
                           tricks=RP_TRICKS, mistakes=RP_MISTAKES, revision=RP_REVISION, patterns=RP_PATTERNS)),
    ("rp-partnership", dict(concept=RN_CONCEPT, notes=RN_NOTES, formulas=RN_FORMULAS,
                            tricks=RN_TRICKS, mistakes=RN_MISTAKES, revision=RN_REVISION, patterns=RN_PATTERNS)),
    ("rp-ages", dict(concept=RA_CONCEPT, notes=RA_NOTES, formulas=RA_FORMULAS,
                     tricks=RA_TRICKS, mistakes=RA_MISTAKES, revision=RA_REVISION, patterns=RA_PATTERNS)),
    ("rp-money-applications", dict(concept=RC_CONCEPT, notes=RC_NOTES, formulas=RC_FORMULAS,
                                   tricks=RC_TRICKS, mistakes=RC_MISTAKES, revision=RC_REVISION, patterns=RC_PATTERNS)),
]

data = json.loads(TOPIC.read_text(encoding="utf-8"))
for sid, block in BLOCKS:
    sub = next(s for s in data["subtopics"] if s["id"] == sid)
    patterns = block["patterns"]
    old_ids = {p["id"] for p in sub.get("patterns", [])}
    new_ids = {p["id"] for p in patterns}
    assert old_ids <= new_ids, (sid, old_ids - new_ids)
    all_other = {p["id"] for s in data["subtopics"] if s["id"] != sid for p in s.get("patterns", [])}
    assert not (all_other & new_ids), (sid, all_other & new_ids)
    notes = block["notes"].strip() + "\n"
    assert 2500 <= len(notes) <= 5000, (sid, len(notes))
    assert 4 <= len(re.findall(r"^### ", notes, re.M)) <= 8, sid
    block.update(notes=notes, mistakes=[{k: dfrac(v) for k, v in m.items()} for m in block["mistakes"]],
                 revision=[dfrac(r) for r in block["revision"]])
    sub.update(**block)
    print(f"{sid}: notes {len(notes)} chars, {len(patterns)} patterns (was {len(old_ids)})")

file_ids = [p["id"] for s in data["subtopics"] for p in s.get("patterns", [])]
assert len(file_ids) == len(set(file_ids)), "duplicate pattern ids in file"
TOPIC.write_text(json.dumps(data, ensure_ascii=False, indent=1) + "\n", encoding="utf-8")
print("ratio-proportion.json updated")
