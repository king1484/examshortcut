"""Phase-2 deep content for quant/ratio-proportion — basics module."""
import os
import sys

sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
from _lib import Sub


def build_basics():
    S = Sub("rp-basics")
    S.notes = r"""### The multiplier x solves everything
"Numbers are in the ratio $a : b$" means the numbers are $ax$ and $bx$. Every extra fact is a one-line equation in x:
- Sum given: $(a + b)x = S$.
- Difference given: $(b - a)x = D$.
- Product given: $abx^2 = P$ → take a square root.
Once x is known, both numbers, their sum, difference and product are immediate. Sum of parts $= (a+b)x$, so 1 part $= \frac{S}{a + b}$.

### Dividing an amount in a ratio
For $N$ split in $a : b : c$, the shares are $\frac{a}{a+b+c}N$, $\frac{b}{a+b+c}N$, $\frac{c}{a+b+c}N$. Fastest form: value of one part $= \frac{N}{a+b+c}$, then multiply.
Questions hide the total: "A gets ₹300 more than B" → $(b - a)x = 300$ → recover x → total $= (a + b + c)x$.

### Combining two ratios (the LCM bridge)
Given $A : B = m : n$ and $B : C = p : q$, make the B-terms equal: scale the first by p, the second by n (or both to the LCM of the two B values). Then $A : B : C = mp : np : nq$.
Read the answer from the middle out: the A-term comes from the first ratio, the C-term from the second, and B is the common bridge value.
The one-equality version: $2A = 3B = 4C$ → take the LCM of 2, 3, 4 (here 12): $A : B : C = 6 : 4 : 3$. Each term = LCM ÷ its multiplier.

### Long chains
For $A : B$, $B : C$, $C : D$ given and $A : D$ asked, multiply the fractions: $\frac{A}{D} = \frac{A}{B} \times \frac{B}{C} \times \frac{C}{D}$, then reduce.

### When a ratio changes
"Add k to each term and the ratio becomes p : q": $\frac{ax + k}{bx + k} = \frac{p}{q}$ — one cross-multiplication gives x. Subtractions work the same with −k. The two ratio statements share the SAME x; that is the whole trick.

### Comparing two ratios
To compare $a : b$ with $c : d$, cross-multiply: $a : b$ is greater exactly when $ad > bc$. Example: which is larger, $3 : 4$ or $5 : 7$? Compare $3 \times 7 = 21$ with $4 \times 5 = 20$ → $3 : 4$ wins.
Duplicate and sub-duplicate ratios come up in harder questions: $a : b$ squared is $a^2 : b^2$ (duplicate), $\sqrt{a} : \sqrt{b}$ is the sub-duplicate. "The ratio of the areas of two squares whose sides are in ratio 2 : 3" is simply $4 : 9$.

### Same kind, same unit
Ratio terms must measure the same kind of quantity in the same unit — ₹ with ₹, kg with kg. A question giving "3 kg to 500 g" expects $3000 : 500 = 6 : 1$, not $3 : 500$. Converting units FIRST is half the answer in mixed-unit questions (speeds km/h vs m/s, hours vs minutes, ₹ vs paise).

### Quick revision
- Ratio terms are ax, bx — x is the universal unknown.
- 1 part = total ÷ (sum of ratio terms).
- Bridge: equalise the shared letter; kA = kB = kC → LCM route.
- Changed ratio → equate the two expressions of the same quantity.
"""

    S.pattern("rp-b1", "Divide an amount in a given ratio", "very common",
        "A sum of money (or prize, rent, sweets) is split in m : n : p; a share, a difference of shares, or the total is asked.",
        r"\text{share} = \frac{\text{term}}{\text{sum of terms}} \times N, \quad \text{1 part} = \frac{N}{m + n + p}",
        r"""1. Add the ratio terms to get total parts.
2. One part = amount ÷ total parts.
3. Multiply the part by the asked term; for a difference, multiply by the gap between terms.

Why: the ratio fixes each share as a fixed fraction of the whole.""",
        "₹780 is divided among A, B and C in the ratio 3 : 4 : 6. What is A's share?",
        r"Total parts 13 → 1 part $= \frac{780}{13} = 60$ → A $= 3 \times 60 = ₹180$.")
    S.pattern("rp-b2", "Combine ratios into A : B : C", "very common",
        "'A : B = 2 : 3 and B : C = 4 : 5, find A : B : C' — or the compact form '2A = 3B = 4C'.",
        r"A:B = m:n,\ B:C = p:q \Rightarrow A:B:C = mp : np : nq; \quad kA = lB = mC \Rightarrow \text{LCM of } k, l, m",
        r"""1. Two-ratio form: scale both ratios so the common letter has the same value (LCM bridge).
2. One-equality form: divide the LCM of the multipliers by each multiplier.
3. Long chains: multiply fractions (A/B × B/C × …) and reduce.

Why: the shared term must mean the same number in both ratios before they can be merged.""",
        "If $2A = 3B = 4C$, then $A : B : C$ is:",
        r"LCM(2, 3, 4) = 12 → $A : B : C = \frac{12}{2} : \frac{12}{3} : \frac{12}{4} = 6 : 4 : 3$.")
    S.pattern("rp-b3", "Multiplier with sum / difference / product", "very common",
        "'Two numbers are in ratio a : b and their sum/difference/product is …' — one extra fact, one equation.",
        r"ax \pm bx = (a \pm b)x, \qquad abx^2 = P \Rightarrow x = \sqrt{P/(ab)}",
        r"""1. Write the numbers as ax and bx.
2. Translate the given fact: sum → (a + b)x, difference → (b − a)x, product → abx².
3. Solve for x, then build whatever is asked (often sum, difference, or the numbers themselves).

Why: every statistic of the pair is a multiple of x (or x²), so one fact fixes x.""",
        "The ratio of two numbers is 7 : 11 and their product is 693. Find the sum of the numbers.",
        r"$77x^2 = 693$ → $x^2 = 9$ → x = 3 → numbers 21 and 33 → sum = 54.")
    S.pattern("rp-b4", "Ratio changes when a quantity is added / subtracted", "common",
        "'The ratio of boys to girls is 4 : 5; after 100 boys join, it becomes 6 : 5' — a fixed number moves in and out.",
        r"\frac{ax \pm k}{bx \pm k} = \frac{p}{q}",
        r"""1. Write the original counts as ax, bx.
2. Add or subtract k ONLY on the side mentioned (or on both, as the question says).
3. Equate to the new ratio and cross-multiply → x.

Why: adding a fixed number breaks the proportionality, so the ratio genuinely changes and pins down x.""",
        "The ratio of boys to girls in a school is 4 : 5. If 100 more boys join the school, the ratio becomes 6 : 5. How many students were there in the school originally?",
        r"$\frac{4x + 100}{5x} = \frac{6}{5}$ → $20x + 500 = 30x$ → x = 50 → originally $9 \times 50 = 450$.")

    assert 780 // 13 * 3 == 180
    S.q("rp-b1", "easy",
        "₹780 is divided among A, B and C in the ratio 3 : 4 : 6. What is A's share?",
        ["₹180", "₹240", "₹360", "₹300"], "₹180",
        r"""Total parts = 13 → 1 part $= \frac{780}{13} = ₹60$.
A's share $= 3 \times 60 = ₹180$.""",
        None, 30)
    assert 1870 // 11 == 170 and 170 * 3 == 510
    S.q("rp-b1", "medium",
        "A sum of ₹1,870 is divided between X and Y in the ratio 4 : 7. How much does Y get more than X?",
        ["₹510", "₹680", "₹340", "₹850"], "₹510",
        r"""Total parts = 11 → 1 part $= \frac{1870}{11} = ₹170$.
Difference = $(7 - 4)$ parts $= 3 \times 170 = ₹510$.""",
        None, 35)
    S.q("rp-b2", "medium",
        "If A : B = 2 : 5 and B : C = 6 : 7, then A : B : C is:",
        ["12 : 30 : 35", "12 : 35 : 30", "2 : 5 : 7", "6 : 30 : 35"], "12 : 30 : 35",
        r"""Make B common: LCM of 5 and 6 = 30.
A : B = 2 : 5 = 12 : 30; B : C = 6 : 7 = 30 : 35 → $12 : 30 : 35$.""",
        "2 : 5 : 7 is the trap from adding ratios instead of bridging.", 40)
    assert 6 * 2 == 12 and 12 // 2 == 6 and 12 // 3 == 4 and 12 // 4 == 3
    S.q("rp-b2", "medium",
        "If $2A = 3B = 4C$, then $A : B : C$ is:",
        ["6 : 4 : 3", "3 : 4 : 6", "2 : 3 : 4", "4 : 3 : 6"], "6 : 4 : 3",
        r"""LCM(2, 3, 4) = 12. Divide 12 by each multiplier:
$A = \frac{12}{2} = 6$, $B = \frac{12}{3} = 4$, $C = \frac{12}{4} = 3$ → $6 : 4 : 3$.""",
        None, 40)
    S.q("rp-b2", "hard",
        "If A : B = 2 : 3, B : C = 4 : 5 and C : D = 6 : 7, then A : D is:",
        ["16 : 35", "15 : 35", "16 : 33", "18 : 35"], "16 : 35",
        r"""$\frac{A}{D} = \frac{A}{B} \times \frac{B}{C} \times \frac{C}{D} = \frac{2}{3} \times \frac{4}{5} \times \frac{6}{7} = \frac{48}{105} = \frac{16}{35}$.
So $A : D = 16 : 35$.""",
        None, 50)
    assert 156 // 13 == 12 and 12 * 9 == 108
    S.q("rp-b3", "easy",
        "Two numbers are in the ratio 4 : 9 and their sum is 156. The larger number is:",
        ["108", "96", "112", "84"], "108",
        r"""Total parts = 13 → 1 part $= \frac{156}{13} = 12$.
Larger number $= 9 \times 12 = 108$.""",
        None, 30)
    assert 7 * 11 * 9 == 693 and 7 * 3 + 11 * 3 == 54
    S.q("rp-b3", "medium",
        "The ratio of two numbers is 7 : 11 and their product is 693. The sum of the numbers is:",
        ["54", "48", "60", "66"], "54",
        r"""Numbers $7x, 11x$ → $77x^2 = 693$ → $x^2 = 9$ → $x = 3$.
Numbers 21 and 33 → sum = 54.""",
        None, 40)
    S.q("rp-b4", "medium",
        "Two numbers are in the ratio 3 : 5. If 9 is added to each number, the ratio becomes 3 : 4. The numbers are:",
        ["9 and 15", "12 and 20", "6 and 10", "15 and 25"], "9 and 15",
        r"""$\frac{3x + 9}{5x + 9} = \frac{3}{4}$ → $12x + 36 = 15x + 27$ → $x = 3$.
Numbers: 9 and 15. Check: $\frac{18}{24} = \frac{3}{4}$ ✓.""",
        None, 40)
    assert (4 * 50 + 5 * 50) == 450
    S.q("rp-b4", "medium",
        "The ratio of boys to girls in a school is 4 : 5. If 100 more boys join the school, the ratio becomes 6 : 5. How many students were there in the school originally?",
        ["450", "500", "400", "550"], "450",
        r"""$\frac{4x + 100}{5x} = \frac{6}{5}$ → $20x + 500 = 30x$ → $x = 50$.
Boys 200, girls 250 → total $= 450$.""",
        None, 45)
    return S
