"""Phase-2 deep content for quant/simplification. Run: py -3 simplification.py"""
import sys, os
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
from _lib import apply_topic
from simp_bodmas import build_bodmas
from simp_ident_surds import build_identities, build_surds
from simp_roots_approx import build_roots, build_approx


def P(pattern, frequency, howToSpot, approach, subtopic, q, sol):
    return {"pattern": pattern, "frequency": frequency, "howToSpot": howToSpot, "approach": approach,
            "subtopic": subtopic, "example": {"q": q, "solution": sol}}


PYQ = [
    P("VBODMAS with 'of' and brackets", "very common",
      "A long mixed expression with ÷, ×, 'of', brackets and a vinculum. The word 'of' is the trap marker.",
      "Follow VBODMAS strictly: vinculum, brackets innermost first, then 'of' (it multiplies but comes before ÷ and ×), then ÷ and × left to right, then + and −. A minus before a bracket flips every sign inside.",
      "simp-bodmas", r"Evaluate $64 \div 4 \text{ of } 2 + 8 \times 3$.",
      r"'of' first: $64 \div 8 = 8$, then $+ 24 = 32$."),
    P("Identity fractions: (a³±b³) over the quadratic", "very common",
      "A fraction whose top is a sum/difference of cubes (often decimals) and whose bottom is a²∓ab+b² or a²±ab+b².",
      "Match the denominator to the identity factor and cancel: (a³+b³)/(a²−ab+b²) = a+b; (a³−b³)/(a²+ab+b²) = a−b. Read the middle sign carefully — minus below pairs with plus above.",
      "simp-identities", r"$\frac{(15.2)^3-(5.2)^3}{(15.2)^2+15.2\times5.2+(5.2)^2}$ = ?",
      "Denominator a²+ab+b² → value = a − b = 10."),
    P("x + 1/x family", "very common",
      r"'If $x + \frac{1}{x} = 4$, find $x^2 + \frac{1}{x^2}$ (or $x^3 + \frac{1}{x^3}$, $x^4 + \frac{1}{x^4}$)' — also the minus version.",
      r"Square the given: $x^2 + \frac{1}{x^2} = k^2 - 2$ (plus) or $k^2 + 2$ (minus). Cube: $k^3 \mp 3k$. Fourth power: square the squared result and subtract 2.",
      "simp-identities", r"$x+\frac1x=4$ → $x^3+\frac{1}{x^3}$?",
      r"$4^3 - 3 \times 4 = 52$."),
    P("Indices equation with a common base", "very common",
      r"An equation like $2^{x+3} \times 4^{x-1} = 128$ or $3^{x+2} + 3^x = 810$.",
      "Write every term as a power of one prime (4 = 2², 25 = 5²). Take the common power outside if it is a sum. Then equate the exponents.",
      "simp-surds-indices", r"Solve $2^{x+3} \times 4^{x-1} = 128$.",
      r"$2^{3x+1} = 2^7$ → $x = 2$."),
    P("Rationalisation and surd sums", "very common",
      r"Fractions like $\frac{1}{\sqrt7-\sqrt6}$, sums of conjugate fractions, or a surd plus its reciprocal.",
      "Multiply top and bottom by the conjugate. Telescoping chains collapse to (first root − last root). If x = a+2√b type, then 1/x is the conjugate a−2√b.",
      "simp-surds-indices", r"$\frac{1}{\sqrt9+\sqrt8}+\dots+\frac{1}{\sqrt2+1}$ = ?",
      r"Each term is $\sqrt k - \sqrt{k-1}$; the sum collapses to $3 - 1 = 2$."),
    P("Root of a surd: √(a + 2√b)", "common",
      r"Expressions like $\sqrt{11+6\sqrt2}$ or $\sqrt{7+4\sqrt3}$ (and the two-root sum/difference versions).",
      r"Rewrite as $\sqrt{a+2\sqrt b}$; split $a = x+y$ with $xy = b$; the value is $\sqrt x+\sqrt y$. For a pair like $\sqrt{7+4\sqrt3} \pm \sqrt{7-4\sqrt3}$, take $x = 2+\sqrt3$, $y = 2-\sqrt3$ and add or subtract.",
      "simp-surds-indices", r"$\sqrt{11+6\sqrt2}$ = ?",
      r"$11 = 9+2$, $9 \times 2 = 18$ → $3+\sqrt2$."),
    P("Cube and square roots of perfect powers; least number for a square", "very common",
      "'Find ∛9261', '√11025', or 'least number to add/subtract to N to make a perfect square'.",
      "Cube root: group digits in threes, use the unit-digit swap map (2↔8, 3↔7) plus a size check. Square root: digit pairs, last-digit map and neighbours. For least add/subtract, bracket N between k² and (k+1)².",
      "simp-roots", "Least number to add to 1300 for a perfect square?",
      r"$37^2 = 1369$ → add $69$."),
    P("Infinite and nested radicals", "common",
      r"$\sqrt{6+\sqrt{6+\dots}}$, $\sqrt{20\times\sqrt{20\times\dots}}$, or a finite nest like $\sqrt{30+\sqrt{24+\sqrt{144}}}$. (already exists as solved example — same type, new numbers)",
      "Infinite plus-radical: solve $x^2 = a + x$ (or use $a = k(k+1)$ → answer $k+1$). Infinite product-radical: the answer is $a$. Finite nests: work from the innermost root outward.",
      "simp-roots", r"$\sqrt{20\times\sqrt{20\times\sqrt{20\times\cdots}}}$ = ?",
      r"$x^2 = 20x$ → $x = 20$."),
    P("Approximation with percentages, products and roots", "very common",
      "'What approximate value comes in place of ?' with decimals like 1199.8, 24.98%, √2303.9.",
      "Round every number to a friendly value (nearest ten, percentage → fraction, root → nearest perfect power), compute mentally, and pick the closest option. Options are spaced far apart; do not chase exact decimals.",
      "simp-approximation", r"$29.9\%$ of $1199.8 + 15.02 \times 23.9 ≈$ ?",
      r"$360 + 360 = 720$."),
]

if __name__ == "__main__":
    subs = [build_bodmas(), build_identities(), build_surds(), build_roots(), build_approx()]
    apply_topic("simplification", subs, PYQ)
