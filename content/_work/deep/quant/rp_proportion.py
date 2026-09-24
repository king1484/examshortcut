"""Phase-2 deep content for quant/ratio-proportion — proportion module."""
import os
import sys

sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
from _lib import Sub


def build_proportion():
    S = Sub("rp-proportion")
    S.notes = r"""### The core identity
$a : b :: c : d$ means $\frac{a}{b} = \frac{c}{d}$, and equivalently $ad = bc$ — **extremes × extremes = means × means** (a and d are the extremes, b and c the means). Every 'find the missing term' question is one cross-multiplication away.

### The three named proportionals
- **Fourth proportional** to $a, b, c$: solve $\frac{a}{b} = \frac{c}{d}$ → $d = \frac{bc}{a}$ (four distinct numbers).
- **Third proportional** to $a, b$: solve $\frac{a}{b} = \frac{b}{x}$ → $x = \frac{b^2}{a}$ (the middle term repeats — that is what 'third' means).
- **Mean proportional** between $a$ and $b$: $x = \sqrt{ab}$, from $\frac{a}{x} = \frac{x}{b}$. It is the geometric mean; the arithmetic mean $\frac{a+b}{2}$ is the planted trap.

### Continued proportion
$a, b, c$ are in continued proportion when $\frac{a}{b} = \frac{b}{c}$, i.e. $b^2 = ac$. So b is automatically the mean proportional of a and c. Any one member from the other two: $a = \frac{b^2}{c}$, $c = \frac{b^2}{a}$, $b = \sqrt{ac}$. Four numbers $a, b, c, d$ with $\frac{b}{a} = \frac{c}{b} = \frac{d}{c}$ form a geometric progression — the same equations apply term by term.

### Componendo and dividendo
If $\frac{a}{b} = \frac{c}{d} = k$, then adding and subtracting numerator and denominator: $\frac{a+b}{a-b} = \frac{c+d}{c-d}$.
The exam use runs it backwards: given $\frac{x+y}{x-y} = \frac{p}{q}$, jump straight to $\frac{x}{y} = \frac{p + q}{p - q}$. Example: $\frac{x+y}{x-y} = \frac{5}{3}$ → $\frac{x}{y} = \frac{8}{2} = 4$.
With coefficient twists like $\frac{5x - 3y}{5x + 3y} = \frac{2}{7}$, apply C&D first to get $\frac{5x}{3y} = \frac{9}{5}$, then rearrange.

### Order matters
"Fourth proportional to 4, 9, 12" and "fourth proportional to 12, 9, 4" are different numbers — the terms stay in the order written. Write the proportion exactly as the question lists the terms before cross-multiplying.

### A worked chain putting it together
"Three numbers a, b, c are in continued proportion with b = 12 and a + c = 26." Then $ac = b^2 = 144$, so a and c are the factor pair of 144 summing to 26 — that is 8 and 18. The numbers are 8, 12, 18 (check: $8 : 12 = 12 : 18 = 2 : 3$ ✓). Exam numbers are always built so the factor pair comes out clean; if yours doesn't, re-read the question, not the method.

### The three means
Arithmetic mean $\frac{a+b}{2}$, geometric (mean proportional) $\sqrt{ab}$, harmonic mean $\frac{2ab}{a+b}$ — the exam asks for the **mean proportional**, i.e. the geometric mean. "The mean proportional between 3 and 12 is 6, not 7.5."

### Quick revision
- $ad = bc$ for $a : b :: c : d$.
- Fourth: $\frac{bc}{a}$. Third: $\frac{b^2}{a}$. Mean: $\sqrt{ab}$.
- Continued proportion: $b^2 = ac$.
- C&D: $\frac{x}{y} = \frac{p+q}{p-q}$ from $\frac{x+y}{x-y} = \frac{p}{q}$.
"""

    S.pattern("rp-p1", "Fourth proportional", "very common",
        "'Find the fourth proportional to a, b, c' — three numbers, the fourth that completes a : b :: c : ?",
        r"\frac{a}{b} = \frac{c}{d} \Rightarrow d = \frac{bc}{a}",
        r"""1. Write the proportion in the exact order given: a : b :: c : d.
2. Cross-multiply: ad = bc.
3. $d = \frac{bc}{a}$ — one division.

Why: the fourth term must preserve the same ratio pair-wise as the first three.""",
        "The fourth proportional to 8, 12 and 18 is:",
        r"$d = \frac{12 \times 18}{8} = 27$. (Check: $\frac{8}{12} = \frac{18}{27} = \frac{2}{3}$ ✓.)")
    S.pattern("rp-p2", "Third proportional", "common",
        "'Find the third proportional to a and b' — only two numbers; the middle repeats (a : b :: b : ?).",
        r"\frac{a}{b} = \frac{b}{x} \Rightarrow x = \frac{b^2}{a}",
        r"""1. Repeat the second term: a : b :: b : x.
2. Cross-multiply: ax = b².
3. $x = \frac{b^2}{a}$.

Why: 'third proportional to a and b' is the third member of a continued proportion starting a, b.""",
        "The third proportional to 9 and 12 is:",
        r"$x = \frac{12^2}{9} = 16$. (Check: $\frac{9}{12} = \frac{12}{16} = \frac{3}{4}$ ✓.)")
    S.pattern("rp-p3", "Mean proportional", "very common",
        "'Find the mean proportional between a and b' — the number x with a : x :: x : b.",
        r"x = \sqrt{ab}",
        r"""1. Multiply the two numbers.
2. Take the square root (it must come out exact in exam numbers).
3. Sanity check: x² = ab. The arithmetic mean (a+b)/2 is NOT the answer.

Why: the mean proportional is the self-repeating middle term, i.e. the geometric mean.""",
        "The mean proportional between 12 and 48 is:",
        r"$\sqrt{12 \times 48} = \sqrt{576} = 24$. (Check: $\frac{12}{24} = \frac{24}{48} = \frac{1}{2}$ ✓.)")
    S.pattern("rp-p4", "Continued proportion (find a member)", "common",
        "'a, b, c are in continued proportion; given two of them, find the third' — sometimes disguised as a geometric progression.",
        r"b^2 = ac \ \Rightarrow\ b = \sqrt{ac},\ a = \frac{b^2}{c},\ c = \frac{b^2}{a}",
        r"""1. Write the defining equation $\frac{a}{b} = \frac{b}{c}$, i.e. $b^2 = ac$.
2. Substitute the two known members and solve.
3. The middle term is the mean proportional of the outer two.

Why: 'continued proportion' fixes one exact relationship among the three members.""",
        "The numbers x, 12 and 18 are in continued proportion. Find x.",
        r"$12^2 = 18x$ → $x = \frac{144}{18} = 8$. (Check: $\frac{8}{12} = \frac{12}{18} = \frac{2}{3}$ ✓.)")
    S.pattern("rp-p5", "Componendo and dividendo", "common",
        "$(x + y)/(x - y)$ given as a ratio; find x : y — sometimes with coefficients attached to x and y.",
        r"\frac{x + y}{x - y} = \frac{p}{q} \Rightarrow \frac{x}{y} = \frac{p + q}{p - q}",
        r"""1. Apply C&D: the sum-over-difference of each side is equal.
2. $\frac{x}{y} = \frac{p+q}{p-q}$ — read it directly.
3. With coefficients ($\frac{mx \pm ny}{mx \pm ny}$), C&D gives $\frac{mx}{ny}$; divide off m : n.

Why: one application converts the sum/difference form into the pure ratio, saving a full solve.""",
        "If $\\frac{a+b}{a-b} = \\frac{7}{5}$, then $a : b$ equals:",
        r"C&D: $\frac{a}{b} = \frac{7 + 5}{7 - 5} = 6$ → $a : b = 6 : 1$.")

    assert 12 * 18 // 8 == 27
    S.q("rp-p1", "easy", "The fourth proportional to 8, 12 and 18 is:",
        ["27", "24", "30", "32"], "27",
        r"""$\frac{8}{12} = \frac{18}{d}$ → $8d = 216$ → $d = 27$.
Shortcut: $d = \frac{12 \times 18}{8} = 27$.""",
        None, 25)
    assert 144 // 9 == 16
    S.q("rp-p2", "easy", "The third proportional to 9 and 12 is:",
        ["16", "15", "18", "20"], "16",
        r"""$9 : 12 :: 12 : x$ → $9x = 144$ → $x = 16$.""",
        None, 25)
    import math
    assert math.isqrt(12 * 48) == 24
    S.q("rp-p3", "easy", "The mean proportional between 12 and 48 is:",
        ["24", "30", "20", "36"], "24",
        r"""Mean proportional $= \sqrt{12 \times 48} = \sqrt{576} = 24$.""",
        None, 25)
    assert math.isqrt(3 * 48) == 12
    S.q("rp-p4", "medium",
        "Three numbers a, b, c are in continued proportion. If a = 3 and c = 48, then b is:",
        ["12", "16", "9", "24"], "12",
        r"""$b^2 = ac = 3 \times 48 = 144$ → $b = 12$.
Check: $\frac{3}{12} = \frac{12}{48} = \frac{1}{4}$ ✓.""",
        None, 35)
    assert 24 * 20 % 15 == 0 and 24 * 20 // 15 == 32
    S.q("rp-p1", "medium", "The fourth proportional to 15, 24 and 20 is:",
        ["32", "30", "28", "36"], "32",
        r"""$d = \frac{24 \times 20}{15} = 32$.
(Check: $\frac{15}{24} = \frac{5}{8}$ and $\frac{20}{32} = \frac{5}{8}$ ✓.)""",
        None, 35)
    assert abs(1.2 ** 2 / 0.8 - 1.8) < 1e-9
    S.q("rp-p2", "medium", "The third proportional to 0.8 and 1.2 is:",
        ["1.8", "1.6", "2.0", "1.44"], "1.8",
        r"""$x = \frac{(1.2)^2}{0.8} = \frac{1.44}{0.8} = 1.8$.
(Check: $\frac{0.8}{1.2} = \frac{2}{3}$ and $\frac{1.2}{1.8} = \frac{2}{3}$ ✓.)""",
        None, 35)
    assert abs(math.sqrt(0.08 * 0.18) - 0.12) < 1e-9
    S.q("rp-p3", "medium", "The mean proportional between 0.08 and 0.18 is:",
        ["0.12", "0.13", "1.2", "0.0144"], "0.12",
        r"""$\sqrt{0.08 \times 0.18} = \sqrt{0.0144} = 0.12$.
(Decimal trap: $\sqrt{0.0144} \ne 1.2$.)""",
        None, 35)
    assert 144 % 18 == 0 and 144 // 18 == 8
    S.q("rp-p4", "medium",
        "The numbers x, 12 and 18 are in continued proportion. The value of x is:",
        ["8", "6", "9", "10"], "8",
        r"""$12^2 = 18x$ → $x = \frac{144}{18} = 8$.""",
        None, 35)
    S.q("rp-p5", "medium",
        r"If $\frac{a+b}{a-b} = \frac{7}{5}$, then $a : b$ equals:",
        ["6 : 1", "7 : 5", "2 : 1", "3 : 1"], "6 : 1",
        r"""By componendo and dividendo: $\frac{a}{b} = \frac{7 + 5}{7 - 5} = \frac{12}{2} = 6$ → $a : b = 6 : 1$.""",
        None, 35)
    assert abs((5 * 27 - 3 * 25) / (5 * 27 + 3 * 25) - 2 / 7) < 1e-9  # x:y = 27:25 satisfies
    S.q("rp-p5", "hard",
        r"If $\frac{5x - 3y}{5x + 3y} = \frac{2}{7}$, then $x : y$ equals:",
        ["27 : 25", "25 : 27", "9 : 5", "5 : 9"], "27 : 25",
        r"""Componendo and dividendo: $\frac{5x}{3y} = \frac{2 + 7}{7 - 2} = \frac{9}{5}$.
So $25x = 27y$ → $x : y = 27 : 25$.""",
        None, 50)
    return S
