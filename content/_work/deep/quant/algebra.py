"""Phase-2 deep content for quant/algebra.json — driver.

Upserts notes/patterns/practice per subtopic and rewrites pyqPatterns (enriched).
Idempotent: re-running never duplicates or drops existing questions.
"""
import math
import os
import sys

sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
from _lib import apply_topic
from fractions import Fraction as F

from alg_id_rec import build_identities, build_reciprocal
from alg_three_surds import build_three, build_surds
from alg_poly_max import build_poly, build_maxmin

# ---- verified examples for the enriched pyqPatterns ----
assert 6 ** 3 - 3 * 6 == 198
assert 7 ** 3 - 3 * 12 * 7 == 91
assert abs((2 + math.sqrt(3)) ** 2 + 1 / (2 + math.sqrt(3)) ** 2 - 14) < 1e-9
assert 6 * (36 - 33) == 18
assert (4 - (-3)) == 7
assert abs(4.7 + 2.3 - 7) < 1e-9
assert 8 - 12 + 8 - 5 == -1
assert 7 + 4 * 2 - 4 == 11

PYQ = [
    {
        "pattern": "$x+\\frac1x=k$ → higher powers",
        "frequency": "very common",
        "howToSpot": "Given $x+\\frac1x$, $x-\\frac1x$ or a quadratic with equal end coefficients; asked for $x^3+\\frac1{x^3}$, $x^4+\\frac1{x^4}$, $x^5+\\frac1{x^5}$.",
        "approach": "Climb the ladder: square and subtract 2; cube with $k^3-3k$; fifth rung $= (k^2-2)(k^3-3k)-k$. Recognise special values ($1,\\ -1,\\ \\sqrt3$) for cyclic exponents.",
        "subtopic": "alg-reciprocal",
        "example": {
            "q": "If $x+\\frac1x=6$, then $x^3+\\frac1{x^3}$ is:",
            "solution": "$6^3 - 3\\times6 = 216 - 18 = 198$.",
        },
    },
    {
        "pattern": "Given $a\\pm b$ and $ab$, find $a^3\\pm b^3$ / $a^4+b^4$",
        "frequency": "very common",
        "howToSpot": "Two conditions on two variables and a symmetric expression to evaluate.",
        "approach": "Never solve for $a,b$. Build upward: $(a\\pm b)^2 \\mp 2ab$ for squares, $(a\\pm b)^3 \\mp 3ab(a\\pm b)$ for cubes, $(a^2+b^2)^2-2a^2b^2$ for fourth powers.",
        "subtopic": "alg-identities",
        "example": {
            "q": "If $a+b=7$ and $ab=12$, then $a^3+b^3$ is:",
            "solution": "$343 - 3\\times12\\times7 = 343 - 252 = 91$.",
        },
    },
    {
        "pattern": "Conjugate surd $x=p+\\sqrt q$",
        "frequency": "very common",
        "howToSpot": "$x=2+\\sqrt3$, $3-2\\sqrt2$, $\\frac{1}{\\sqrt5-2}$ etc., asked for $x^2+\\frac1{x^2}$ or a polynomial in $x$.",
        "approach": "Check $p^2-q=1$ → $\\frac1x=p-\\sqrt q$; then $x+\\frac1x = 2p$ and run the ladder. Otherwise reduce the polynomial modulo the minimal quadratic.",
        "subtopic": "alg-surds",
        "example": {
            "q": "If $x=2+\\sqrt3$, then $x^2+\\frac1{x^2}$ is:",
            "solution": "$\\frac1x = 2-\\sqrt3$ → $x+\\frac1x = 4$ → $x^2+\\frac1{x^2} = 14$.",
        },
    },
    {
        "pattern": "$a^3+b^3+c^3-3abc$ / zero-sum cubes",
        "frequency": "common",
        "howToSpot": "Three variables with $a+b+c$ given, or expressions like $(x-y)^3+(y-z)^3+(z-x)^3$.",
        "approach": "Factor form $s(s^2-3P)$; zero sum → cube-sum $= 3abc$; power sum $s^3 - 3sP + 3R$ when $abc$ is in play.",
        "subtopic": "alg-three-var",
        "example": {
            "q": "If $a+b+c=6$ and $ab+bc+ca=11$, then $a^3+b^3+c^3-3abc$ is:",
            "solution": "$6\\times(36-33) = 18$.",
        },
    },
    {
        "pattern": "Sum of squares equal to zero",
        "frequency": "common",
        "howToSpot": "An equation like $x^2+y^2+z^2-2x+4y-6z+14=0$ or $a^2+b^2+c^2=ab+bc+ca$.",
        "approach": "Complete squares so the constants cancel; each square is zero, giving exact values. The pairwise form forces $a=b=c$.",
        "subtopic": "alg-identities",
        "example": {
            "q": "If $x^2+y^2-8x+6y+25=0$, then $x-y$ is:",
            "solution": "$(x-4)^2+(y+3)^2=0$ → $x=4$, $y=-3$ → $x-y=7$.",
        },
    },
    {
        "pattern": "Big-number / decimal simplification",
        "frequency": "common",
        "howToSpot": "Fractions with cubes over quadratics of the same two numbers, e.g. $\\frac{p^3+q^3}{p^2-pq+q^2}$.",
        "approach": "Match the identity using the sign of the denominator's middle term; answer is $p\\pm q$.",
        "subtopic": "alg-identities",
        "example": {
            "q": "The value of $\\dfrac{4.7^3+2.3^3}{4.7^2-4.7\\times2.3+2.3^2}$ is:",
            "solution": "$p^2-pq+q^2$ under $p^3+q^3$ → the fraction $= 4.7+2.3 = 7$.",
        },
    },
    {
        "pattern": "Linear equations, graphs, remainder",
        "frequency": "occasional",
        "howToSpot": "Condition for unique/no/infinite solutions, area of triangle with axes, remainder or factor of a polynomial.",
        "approach": "Ratios of coefficients; area $= \\frac{c^2}{2ab}$ from the intercepts; remainder $= p(\\alpha)$ by direct substitution.",
        "subtopic": "alg-linear-poly",
        "example": {
            "q": "The remainder when $x^3-3x^2+4x-5$ is divided by $(x-2)$ is:",
            "solution": "$p(2) = 8-12+8-5 = -1$.",
        },
    },
    {
        "pattern": "Maximum / minimum value",
        "frequency": "occasional",
        "howToSpot": "'Least value of $4x+\\frac9x$', 'greatest value of $7+4x-x^2$'.",
        "approach": "AM ≥ GM for $ax+\\frac bx$ (value $2\\sqrt{ab}$); complete the square for quadratics (vertex $c-\\frac{b^2}{4a}$).",
        "subtopic": "alg-maxmin",
        "example": {
            "q": "The greatest value of $7+4x-x^2$ is:",
            "solution": "$-(x-2)^2+11 \\le 11$ → greatest value 11 at $x=2$.",
        },
    },
]

apply_topic("algebra", [build_identities(), build_reciprocal(), build_three(), build_surds(), build_poly(), build_maxmin()], PYQ)
print("OK algebra")
