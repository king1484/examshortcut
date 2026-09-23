from _lib import *
import sympy as sp

S = sp.sqrt
R = sp.Rational

def fv(*exprs):
    return [float(sp.N(e, 30)) for e in exprs]

# ------------------------------------------------------------------ trick example checks
assert F(64, 4 * 2) == 8
assert 2 + F(1) / (2 + F(1) / (2 + F(1, 2))) == F(29, 12)
assert 3456 * 789 == 2726784 and sum(map(int, "2726784")) == 36
assert F(8**3 - 5**3, 8**2 + 8 * 5 + 5**2) / 10 == F(3, 10)
assert (-12)**3 + 7**3 + 5**3 == 3 * (-12) * 7 * 5 == -1260
assert 998 * 1002 == 999996
x = sp.symbols("x")
assert sp.solve(sp.Eq(2 * x - 1, 3 * (x - 3)), x) == [8] and 5**(2 * 8 - 1) == 125**(8 - 3)
assert sp.expand((S(5) + S(3))**2) == 8 + 2 * S(15)
assert 3**2 > 2**3
assert 47**3 == 103823
assert 88**2 == 7744 and 85**2 == 7225
assert 6**2 == 30 + 6
assert abs(399.87 / 7.99 + 18.03 * 4.97 - 140) < 1
assert F(16, 100) * 25 == F(25, 100) * 16 == 4

subtopics = [
 sub("simp-bodmas", "BODMAS, 'of', brackets & vinculum",
  md("**Order of operations (VBODMAS):**",
     "",
     "1. **V**inculum (bar) — e.g. $\\overline{5-3}$",
     "2. **B**rackets, innermost first: ( ) → { } → [ ]",
     "3. **O**f (a multiplication that is done **before** ÷ and ×)",
     "4. **D**ivision and **M**ultiplication — left to right",
     "5. **A**ddition and **S**ubtraction — left to right",
     "",
     r"The key CGL trap is **'of'**: $64 \div 4 \text{ of } 2 = 64 \div 8 = 8$, but $64 \div 4 \times 2 = 32$.",
     "",
     "**Continued fractions** are simplified from the bottom up. A minus sign before a bracket flips every sign inside it."),
  [formula("'of' before division", r"a \div b \text{ of } c = \frac{a}{b \times c}"),
   formula("÷ and × left to right", r"a \div b \times c = \frac{a}{b} \times c"),
   formula("Removing a bracket after minus", r"a - (b - c) = a - b + c"),
   formula("Continued fraction (bottom-up)", r"a + \cfrac{1}{b + \cfrac{1}{c}} = a + \frac{c}{bc + 1}")],
  [trick("'of' binds tighter than ÷",
         "Convert every 'of' into a bracketed product before touching ÷.",
         r"Evaluate $64 \div 4 \text{ of } 2$.",
         r"$4 \text{ of } 2 = 8$, so $64 \div 8 = 8$ (not $16 \times 2 = 32$)."),
   trick("Continued fractions bottom-up",
         "Start with the lowest fraction, invert and add step by step.",
         r"Evaluate $2 + \cfrac{1}{2 + \cfrac{1}{2 + \frac{1}{2}}}$.",
         r"$2 + \frac{1}{2} = \frac{5}{2}$ → $2 + \frac{2}{5} = \frac{12}{5}$ → $2 + \frac{5}{12} = \frac{29}{12}$."),
   trick("Digit-sum (casting out 9s) option check",
         "Digit sum of a product = digit sum of (digit sum × digit sum). Kills wrong options in long multiplication without computing.",
         r"Which could be $3456 \times 789$: 2726784 or 2726874 or 2762784?",
         "Digit sums: 3456 → 9, 789 → 6, so product ≡ 9 × 6 = 54 → 9. 2+7+2+6+7+8+4 = 36 → 9 ✓. The other two also give 36 — so combine with the unit digit (6 × 9 = 54 → 4) and magnitude; exact value 2726784.")],
  [r"Doing $a \div b \times c$ as $a \div (b \times c)$.",
   "Ignoring 'of' and treating it like ordinary ×, which is done after ÷.",
   "Not removing the vinculum (bar) first.",
   "Forgetting to flip signs when removing a bracket preceded by a minus."]),

 sub("simp-identities", "Algebraic identities in numerical simplification",
  md("Many CGL simplification questions are identities in disguise. Spot the shape, name $a$ and $b$, and the answer is often just $a+b$ or $a-b$.",
     "",
     "| Looks like | Equals |",
     "|---|---|",
     r"| $\frac{a^3 + b^3}{a^2 - ab + b^2}$ | $a + b$ |",
     r"| $\frac{a^3 - b^3}{a^2 + ab + b^2}$ | $a - b$ |",
     r"| $\frac{a^2 - b^2}{a - b}$ | $a + b$ |",
     r"| $\frac{(a+b)^2 - (a-b)^2}{ab}$ | 4 |",
     r"| $\frac{(a+b)^2 + (a-b)^2}{a^2 + b^2}$ | 2 |",
     "",
     r"Also: if $a + b + c = 0$ then $a^3 + b^3 + c^3 = 3abc$."),
  [formula("Square of sum / difference", r"(a \pm b)^2 = a^2 \pm 2ab + b^2"),
   formula("Difference of squares", r"a^2 - b^2 = (a+b)(a-b)"),
   formula("Sum of cubes", r"a^3 + b^3 = (a+b)(a^2 - ab + b^2)"),
   formula("Difference of cubes", r"a^3 - b^3 = (a-b)(a^2 + ab + b^2)"),
   formula("Cube of sum", r"(a+b)^3 = a^3 + b^3 + 3ab(a+b)"),
   formula("Three cubes", r"a^3 + b^3 + c^3 - 3abc = (a+b+c)(a^2+b^2+c^2-ab-bc-ca)"),
   formula("Zero-sum case", r"a + b + c = 0 \Rightarrow a^3 + b^3 + c^3 = 3abc")],
  [trick("Pattern-match the fraction",
         "If the numerator has cubes and the denominator has three terms with a middle product, it is a sum/difference-of-cubes identity.",
         r"Simplify $\frac{0.8 \times 0.8 \times 0.8 - 0.5 \times 0.5 \times 0.5}{0.8 \times 0.8 + 0.8 \times 0.5 + 0.5 \times 0.5}$.",
         r"Form $\frac{a^3 - b^3}{a^2 + ab + b^2} = a - b$ with $a = 0.8$, $b = 0.5$ ⇒ $0.3$."),
   trick("a + b + c = 0 ⇒ cubes = 3abc",
         "Check if the three bases add to zero before cubing anything.",
         r"Find $(-12)^3 + 7^3 + 5^3$.",
         r"$-12 + 7 + 5 = 0$ ⇒ value $= 3 \times (-12) \times 7 \times 5 = -1260$."),
   trick("Products around a round number",
         r"$(n - d)(n + d) = n^2 - d^2$.",
         r"Find $998 \times 1002$.",
         r"$1000^2 - 2^2 = 1000000 - 4 = 999996$.")],
  ["Using $a^2 + ab + b^2$ with the sum-of-cubes numerator (sign of the middle term must be opposite).",
   "Expanding decimals by brute force instead of naming a and b.",
   r"Writing $(a+b)^3 = a^3 + b^3$."]),

 sub("simp-surds-indices", "Surds & indices",
  md("**Laws of indices** let you rewrite everything with a common base (usually a prime). Once bases match, equate exponents.",
     "",
     r"**Surds** are irrational roots like $\sqrt{3}$. Rationalise by multiplying with the conjugate: $\frac{1}{\sqrt{a} + \sqrt{b}} = \frac{\sqrt{a} - \sqrt{b}}{a - b}$.",
     "",
     r"**Square root of a surd:** $\sqrt{a + 2\sqrt{b}} = \sqrt{x} + \sqrt{y}$ where $x + y = a$ and $xy = b$. E.g. $\sqrt{7 + 4\sqrt{3}} = \sqrt{7 + 2\sqrt{12}} = 2 + \sqrt{3}$.",
     "",
     r"**Comparing surds:** raise all to the LCM of the root orders. E.g. compare $\sqrt[3]{3}$ and $\sqrt{2}$ by raising to 6th power: 9 vs 8."),
  [formula("Product / quotient", r"a^m \cdot a^n = a^{m+n},\quad \frac{a^m}{a^n} = a^{m-n}"),
   formula("Power of power", r"(a^m)^n = a^{mn},\quad (ab)^n = a^n b^n"),
   formula("Zero & negative index", r"a^0 = 1,\quad a^{-n} = \frac{1}{a^n}"),
   formula("Fractional index", r"a^{p/q} = \sqrt[q]{a^p}"),
   formula("Rationalisation", r"\frac{1}{\sqrt{a} \pm \sqrt{b}} = \frac{\sqrt{a} \mp \sqrt{b}}{a - b}"),
   formula("Root of a surd", r"\sqrt{a \pm 2\sqrt{b}} = \sqrt{x} \pm \sqrt{y},\ x + y = a,\ xy = b,\ x > y"),
   formula("Reciprocal of a unit surd", r"x = a + \sqrt{b},\ a^2 - b = 1 \Rightarrow \frac{1}{x} = a - \sqrt{b}")],
  [trick("Common base, then equate powers",
         "Write both sides as powers of the same prime.",
         r"If $5^{2x - 1} = 125^{x - 3}$, find $x$.",
         r"$125 = 5^3$ ⇒ $2x - 1 = 3x - 9$ ⇒ $x = 8$."),
   trick("Split a + 2√b",
         "Find two numbers with sum a and product b; the root is √(larger) ± √(smaller).",
         r"Simplify $\sqrt{8 + 2\sqrt{15}}$.",
         r"Sum 8, product 15 ⇒ 5 and 3 ⇒ $\sqrt{5} + \sqrt{3}$."),
   trick("LCM of root orders to compare",
         "Raise every surd to the LCM of the orders so all become integers.",
         r"Which is larger, $\sqrt[3]{3}$ or $\sqrt{2}$?",
         r"Raise to 6th power: $(\sqrt[3]{3})^6 = 9$, $(\sqrt{2})^6 = 8$ ⇒ $\sqrt[3]{3}$ is larger.")],
  [r"Writing $\sqrt{a + b} = \sqrt{a} + \sqrt{b}$ — false.",
   r"Treating $a^{-n}$ as $-a^n$.",
   "Comparing surds of different orders by their radicands directly.",
   r"Adding exponents when bases differ ($2^3 \times 3^2 \neq 6^5$)."]),

 sub("simp-roots", "Square roots & cube roots",
  md("**Perfect squares** never end in 2, 3, 7 or 8, and end in an even number of zeros. **Unit digit map for squares:** a root ending in 1 or 9 → square ends in 1; 2/8 → 4; 3/7 → 9; 4/6 → 6; 5 → 5.",
     "",
     "**Cube unit digits** are one-to-one: 1↔1, 4↔4, 5↔5, 6↔6, 9↔9, 0↔0, and the swaps 2↔8, 3↔7.",
     "",
     "**Decimals:** the square root of a decimal with 2n decimal places has n places ($\\sqrt{0.0169} = 0.13$); a cube root of 3n places has n places.",
     "",
     r"**Infinite radicals:** if $n = k(k+1)$, then $\sqrt{n + \sqrt{n + \cdots}} = k + 1$ and $\sqrt{n - \sqrt{n - \cdots}} = k$. Also $\sqrt{x\sqrt{x\sqrt{x \cdots}}} = x$."),
  [formula("Product rule", r"\sqrt{ab} = \sqrt{a}\,\sqrt{b},\quad \sqrt[3]{ab} = \sqrt[3]{a}\,\sqrt[3]{b}"),
   formula("Infinite radical (plus)", r"\sqrt{n + \sqrt{n + \sqrt{n + \cdots}}} = \frac{1 + \sqrt{1 + 4n}}{2}"),
   formula("Infinite radical (minus)", r"\sqrt{n - \sqrt{n - \sqrt{n - \cdots}}} = \frac{-1 + \sqrt{1 + 4n}}{2}"),
   formula("Infinite nested product", r"\sqrt{x\sqrt{x\sqrt{x \cdots}}} = x"),
   formula("Finite nested product", r"\sqrt{x\sqrt{x\sqrt{x}}} = x^{7/8}", "n roots: exponent (2ⁿ − 1)/2ⁿ")],
  [trick("Cube root by unit digit + leading group",
         "Last digit of the root from the cube-digit map; first digit = largest cube not exceeding the leading group (digits left of the last three).",
         r"Find $\sqrt[3]{103823}$.",
         r"Ends in 3 ⇒ root ends in 7. Leading group 103: $4^3 = 64 \le 103 < 125$ ⇒ 4. Root $= 47$."),
   trick("Square root of a perfect square",
         "Unit digit gives two candidates; compare with the square of the middle value (…5) to pick one.",
         r"Find $\sqrt{7744}$.",
         r"Ends in 4 ⇒ root ends in 2 or 8. $77$ lies between $8^2$ and $9^2$ ⇒ 8_. $85^2 = 7225 < 7744$ ⇒ take the larger: $88$."),
   trick("n = k(k + 1) radicals",
         "Factor n as two consecutive integers. Plus-signs give the larger one, minus-signs the smaller.",
         r"Find $\sqrt{30 + \sqrt{30 + \sqrt{30 + \cdots}}}$.",
         r"$30 = 5 \times 6$ ⇒ value $= 6$ (check: $6^2 = 30 + 6$).")],
  ["Miscounting decimal places when taking roots of decimals.",
   "Picking the negative root of the quadratic for an infinite radical (value is always positive).",
   "Assuming a number ending in 1, 4, 5, 6, 9 must be a perfect square — the unit digit only rules out, never confirms."]),

 sub("simp-approximation", "Approximation",
  md("Replace every number with the nearest 'friendly' value (whole numbers, round percentages, perfect squares), compute, then pick the **nearest** option. Options in approximation questions are usually far apart, so a small rounding error does not matter.",
     "",
     "- Round decimals to the nearest integer: 49.98 → 50.",
     "- Percentages → fractions: 24.9% → ¼, 33.2% → ⅓.",
     r"- Near-perfect squares: $\sqrt{1225.2} \approx 35$.",
     "- When rounding two numbers that are multiplied, round one up and the other down if possible to cancel errors."),
  [formula("Percentage swap", r"x\% \text{ of } y = y\% \text{ of } x"),
   formula("Near-square root", r"\sqrt{n^2 + k} \approx n + \frac{k}{2n}"),
   formula("Percent-fraction anchors", r"12.5\% = \tfrac{1}{8},\ 16.67\% = \tfrac{1}{6},\ 33.33\% = \tfrac{1}{3},\ 37.5\% = \tfrac{3}{8}")],
  [trick("Round and compute",
         "Round each term to the nearest convenient number and compute mentally.",
         r"Approximately evaluate $399.87 \div 7.99 + 18.03 \times 4.97$.",
         r"$400 \div 8 + 18 \times 5 = 50 + 90 = 140$."),
   trick("Swap the percentage",
         "If x% of y is awkward, compute y% of x instead.",
         "Find 16% of 25.",
         "= 25% of 16 = ¼ × 16 = 4.")],
  ["Rounding every number in the same direction in a product, compounding the error.",
   "Choosing an option by computing exactly — wastes time; approximations are designed for mental math.",
   "Forgetting 'of' and BODMAS order while approximating."]),
]

pyq = [
 pat("BODMAS with 'of', brackets and vinculum", "very common",
     "Long expression with ÷, ×, 'of', nested brackets or a bar; options are small integers or fractions.",
     "Vinculum → innermost bracket → 'of' → ÷/× left to right → +/−. Convert mixed fractions to improper at the start."),
 pat("Identity-based fraction", "very common",
     r"Numerator with cubes/squares of decimals, denominator a matching quadratic, e.g. $\frac{a^3 + b^3}{a^2 - ab + b^2}$.",
     "Name a and b, match to the identity table, answer is a ± b. Never multiply out decimals."),
 pat("Surds: rationalise / √(a + 2√b) / reciprocal surds", "common",
     r"$\frac{\sqrt{5}+\sqrt{3}}{\sqrt{5}-\sqrt{3}}$, $\sqrt{11 + 6\sqrt{2}}$, $x = 3 + 2\sqrt{2}$ type expressions.",
     "Multiply by conjugate; split a + 2√b into sum/product; for unit surds (a² − b = 1) the reciprocal is just the conjugate."),
 pat("Indices equations", "common",
     r"Unknown in the exponent: $3^{x+2} + 3^x = 810$, $5^{2x-1} = 125^{x-3}$.",
     "Factor the smallest power or convert to a common prime base, then equate exponents. Options can be substituted quickly."),
 pat("Square/cube roots and nested radicals", "common",
     r"$\sqrt{248 + \sqrt{52 + \sqrt{144}}}$, $\sqrt[3]{4913}$, infinite radicals.",
     "Work from the innermost root outward; use unit-digit maps for perfect squares/cubes; use n = k(k+1) for infinite radicals."),
 pat("Comparing surds / fractions", "occasional",
     "'Which is the largest/smallest' with roots of different orders.",
     "Raise to the LCM of the root orders; for fractions use cross-multiplication or complements."),
 pat("Approximation", "occasional",
     "Decimals like 29.97% of 1199.8 with widely spaced options; 'approximate value of ?'.",
     "Round to friendly numbers, compute mentally, pick nearest option."),
]

solved = []

val = 1 + F(1) / (1 + F(1) / (1 + F(1, 2)))
assert val == F(8, 5)
solved.append(Q("simp-s01", r"Simplify: $1 + \cfrac{1}{1 + \cfrac{1}{1 + \frac{1}{2}}}$",
  [r"$\frac{5}{3}$", r"$\frac{8}{5}$", r"$\frac{13}{8}$", r"$\frac{3}{2}$"], 1, val,
  md(r"Bottom-up: $1 + \frac{1}{2} = \frac{3}{2}$.",
     r"$1 + \frac{1}{3/2} = 1 + \frac{2}{3} = \frac{5}{3}$.",
     r"$1 + \frac{1}{5/3} = 1 + \frac{3}{5} = \frac{8}{5}$."),
  "Each level is 1 + (reciprocal of the level below): 3/2 → 5/3 → 8/5 (Fibonacci ratios: 2/1, 3/2, 5/3, 8/5).",
  "easy", "simp-bodmas", "continued fraction", 40))

e = S(7 + 4 * S(3)) + S(7 - 4 * S(3))
assert sp.nsimplify(e) == 4 and abs(float(e) - 4) < 1e-12
solved.append(Q("simp-s02", r"The value of $\sqrt{7 + 4\sqrt{3}} + \sqrt{7 - 4\sqrt{3}}$ is:",
  ["4", r"$2\sqrt{3}$", "2", "14"], 0, 4,
  md(r"$7 + 4\sqrt{3} = 7 + 2\sqrt{12}$: two numbers with sum 7 and product 12 are 4 and 3.",
     r"So $\sqrt{7 + 4\sqrt{3}} = \sqrt{4} + \sqrt{3} = 2 + \sqrt{3}$ and $\sqrt{7 - 4\sqrt{3}} = 2 - \sqrt{3}$.",
     r"Sum $= (2 + \sqrt{3}) + (2 - \sqrt{3}) = 4$."),
  r"Square the answer instead: $(\text{sum})^2 = 14 + 2\sqrt{49 - 48} = 16$ ⇒ sum $= 4$.",
  "medium", "simp-surds-indices", "root of surd a+2√b", 50,
  vals=fv(4, 2 * S(3), 2, 14)))

assert 85**2 == 7225 and 86**2 == 7396 and 7250 - 7225 == 25
solved.append(Q("simp-s03", "What is the least number that must be subtracted from 7250 to make it a perfect square?",
  ["25", "146", "50", "36"], 0, 25,
  md(r"$85^2 = 7225$ and $86^2 = 7396$. The largest perfect square $\le 7250$ is 7225.",
     "Number to subtract = 7250 − 7225 = **25**."),
  "7250 ≈ 85² (since 85² = 7225, easy from '5-ending' squares: 8 × 9 = 72 → 7225). Difference 25. (146 is the amount to ADD to reach 86² — a common trap.)",
  "easy", "simp-roots", "least number for perfect square", 40))

a, b = F(73, 100), F(27, 100)
v = (a**3 + b**3) / (a**2 - a * b + b**2)
assert v == 1
solved.append(Q("simp-s04", r"Simplify: $\frac{0.73 \times 0.73 \times 0.73 + 0.27 \times 0.27 \times 0.27}{0.73 \times 0.73 - 0.73 \times 0.27 + 0.27 \times 0.27}$",
  ["0.46", "1", "0.5", "1.46"], 1, v,
  md(r"Let $a = 0.73$, $b = 0.27$. The expression is $\frac{a^3 + b^3}{a^2 - ab + b^2}$.",
     r"Since $a^3 + b^3 = (a + b)(a^2 - ab + b^2)$, the value is $a + b = 0.73 + 0.27 = 1$."),
  "Cubes on top, 'minus middle term' below ⇒ answer = a + b = 1.",
  "easy", "simp-identities", "identity-based fraction", 30))

ex = (1225.2 ** 0.5) * 3.98 + 0.1997 * 450
ov = [210, 230, 250, 270]
assert nearest(ov, ex) == 1
solved.append(Q("simp-s05", r"What is the approximate value of $\sqrt{1225.2} \times 3.98 + 19.97\% \text{ of } 450$?",
  ["210", "230", "250", "270"], 1, 230,
  md(r"$\sqrt{1225.2} \approx \sqrt{1225} = 35$; $3.98 \approx 4$ ⇒ $35 \times 4 = 140$.",
     r"$19.97\% \text{ of } 450 \approx 20\% \text{ of } 450 = 90$.",
     r"Total $\approx 140 + 90 = 230$ (exact value ≈ 229.2)."),
  "35 × 4 = 140; 20% of 450 = 90 ⇒ ≈ 230.",
  "easy", "simp-approximation", "approximation", 40))

# ------------------------------------------------------------------ practice
P = []

v = F(48, 4 * 3) + F(18 * 2, 6) - 5
assert v == 5 and F(48, 4) * 3 + 6 - 5 == 37
P.append(Q("simp-q01", r"Evaluate: $48 \div 4 \text{ of } 3 + 18 \times 2 \div 6 - 5$",
  ["3", "5", "7", "37"], 1, v,
  md(r"'of' first: $4 \text{ of } 3 = 12$ ⇒ $48 \div 12 = 4$.",
     r"$18 \times 2 \div 6 = 36 \div 6 = 6$.",
     r"$4 + 6 - 5 = 5$."),
  "Treat '4 of 3' as a bracket (12). Trap: ignoring 'of' gives 48 ÷ 4 × 3 = 36 and the answer 37.",
  "easy", "simp-bodmas", "BODMAS with of", 40))

v = F(13, 100) * F(12, 10)
assert v == F(156, 1000)
P.append(Q("simp-q02", r"Find the value of $\sqrt{0.0169 \times 1.44}$.",
  ["0.0156", "0.156", "1.56", "15.6"], 1, v,
  md(r"$\sqrt{0.0169} = 0.13$ (4 decimal places → 2) and $\sqrt{1.44} = 1.2$.",
     r"Product $= 0.13 \times 1.2 = 0.156$."),
  "169 → 13, 144 → 12, 13 × 12 = 156. Decimal places: 4 + 2 = 6 inside the root → 3 outside ⇒ 0.156.",
  "easy", "simp-roots", "square root of decimals", 35))

v = sp.Integer(27)**R(2, 3) * sp.Integer(16)**R(-3, 4)
assert v == R(9, 8)
P.append(Q("simp-q03", r"What is the value of $(27)^{\frac{2}{3}} \times (16)^{-\frac{3}{4}}$?",
  [r"$\frac{9}{8}$", r"$\frac{8}{9}$", r"$\frac{3}{8}$", r"$\frac{9}{4}$"], 0, F(9, 8),
  md(r"$27^{2/3} = (3^3)^{2/3} = 3^2 = 9$.",
     r"$16^{-3/4} = (2^4)^{-3/4} = 2^{-3} = \frac{1}{8}$.",
     r"Product $= \frac{9}{8}$."),
  "Cube root of 27 is 3, squared 9. Fourth root of 16 is 2, cubed 8, negative index → 1/8. Answer 9/8.",
  "easy", "simp-surds-indices", "fractional indices", 35))

assert 17**3 == 4913
P.append(Q("simp-q04", r"Find $\sqrt[3]{4913}$.",
  ["13", "17", "23", "27"], 1, 17,
  md(r"4913 ends in 3 ⇒ the cube root ends in 7 (since $7^3 = 343$).",
     r"Leading group (digits before the last three) = 4: $1^3 = 1 \le 4 < 8 = 2^3$ ⇒ tens digit 1.",
     r"Root $= 17$. Check: $17^3 = 4913$ ✓."),
  "Unit digit map 3 ↔ 7 eliminates 13 and 23; 27³ is far above 5000 ⇒ 17.",
  "easy", "simp-roots", "cube root of perfect cube", 30))

inner = 3 - 2
v = 7 - (6 - (5 - (4 - inner)))
assert v == 3
P.append(Q("simp-q05", r"Simplify: $7 - [6 - \{5 - (4 - \overline{3 - 2})\}]$",
  ["1", "2", "3", "5"], 2, v,
  md(r"Vinculum first: $\overline{3 - 2} = 1$.",
     r"$(4 - 1) = 3$ → $\{5 - 3\} = 2$ → $[6 - 2] = 4$ → $7 - 4 = 3$."),
  "Work strictly inside-out: 1 → 3 → 2 → 4 → 3.",
  "easy", "simp-bodmas", "vinculum and brackets", 35))

a, b = F(23, 10), F(3, 10)
v = (a**3 - b**3) / (a**2 + a * b + b**2)
assert v == 2 and F(27, 1000) == b**3 and F(69, 100) == a * b and F(9, 100) == b**2
P.append(Q("simp-q06", r"Simplify: $\frac{(2.3)^3 - 0.027}{(2.3)^2 + 0.69 + 0.09}$",
  ["1.7", "2", "2.3", "2.6"], 1, v,
  md(r"$0.027 = (0.3)^3$, $0.69 = 2.3 \times 0.3$, $0.09 = (0.3)^2$.",
     r"So the expression is $\frac{a^3 - b^3}{a^2 + ab + b^2}$ with $a = 2.3$, $b = 0.3$.",
     r"Value $= a - b = 2.3 - 0.3 = 2$."),
  "Recognise 0.027 = 0.3³, then answer = 2.3 − 0.3 = 2. Trap 2.6 is a + b.",
  "medium", "simp-identities", "identity-based fraction", 45))

e = (S(5) + S(3)) / (S(5) - S(3)) + (S(5) - S(3)) / (S(5) + S(3))
assert sp.nsimplify(sp.simplify(e)) == 8
P.append(Q("simp-q07", r"The value of $\frac{\sqrt{5} + \sqrt{3}}{\sqrt{5} - \sqrt{3}} + \frac{\sqrt{5} - \sqrt{3}}{\sqrt{5} + \sqrt{3}}$ is:",
  ["4", "8", r"$2\sqrt{15}$", "16"], 1, 8,
  md(r"Common denominator $(\sqrt{5})^2 - (\sqrt{3})^2 = 2$.",
     r"Numerator $= (\sqrt{5} + \sqrt{3})^2 + (\sqrt{5} - \sqrt{3})^2 = 2(5 + 3) = 16$.",
     r"Value $= \frac{16}{2} = 8$."),
  r"$\frac{p}{q} + \frac{q}{p} = \frac{p^2 + q^2}{pq}$ with $p^2 + q^2 = 2(a + b) = 16$, $pq = a - b = 2$ ⇒ 8.",
  "medium", "simp-surds-indices", "rationalisation sum", 50,
  vals=fv(4, 8, 2 * S(15), 16)))

k = sp.symbols("k", positive=True)
sol = sp.solve(sp.Eq(k**2, 12 + k), k)
assert sol == [4]
P.append(Q("simp-q08", r"Find the value of $\sqrt{12 + \sqrt{12 + \sqrt{12 + \cdots \infty}}}$.",
  ["3", "4", "6", "12"], 1, 4,
  md(r"Let $x = \sqrt{12 + x}$ ⇒ $x^2 - x - 12 = 0$ ⇒ $(x - 4)(x + 3) = 0$.",
     r"Since $x > 0$, $x = 4$."),
  r"$12 = 3 \times 4$ (consecutive). With '+' signs the answer is the larger factor, **4**. (With '−' signs it would be 3.)",
  "medium", "simp-roots", "infinite radical", 35))

vals_ = [4**4, 2**6, 10**2, 5**3]
assert max(vals_) == 256 and vals_.index(256) == 0
opts = [r"$\sqrt[3]{4}$", r"$\sqrt{2}$", r"$\sqrt[6]{10}$", r"$\sqrt[4]{5}$"]
P.append(Q("simp-q09", r"Which of the following is the largest? $\sqrt[3]{4},\ \sqrt{2},\ \sqrt[6]{10},\ \sqrt[4]{5}$",
  opts, 0, opts[0],
  md("LCM of the root orders 3, 2, 6, 4 is 12. Raise each to the 12th power:",
     r"$(\sqrt[3]{4})^{12} = 4^4 = 256$, $(\sqrt{2})^{12} = 2^6 = 64$, $(\sqrt[6]{10})^{12} = 10^2 = 100$, $(\sqrt[4]{5})^{12} = 5^3 = 125$.",
     r"Largest: $\sqrt[3]{4}$."),
  r"Quick decimals: $\sqrt[3]{4} \approx 1.59$, $\sqrt{2} \approx 1.41$, $\sqrt[6]{10} \approx 1.47$, $\sqrt[4]{5} \approx 1.50$.",
  "medium", "simp-surds-indices", "compare surds", 60))

xx = sp.symbols("x")
sol = sp.solve(sp.Eq(3**(xx + 2) + 3**xx, 810), xx)
assert sol == [4]
P.append(Q("simp-q10", r"If $3^{x+2} + 3^{x} = 810$, then $x$ equals:",
  ["3", "4", "5", "6"], 1, 4,
  md(r"$3^{x+2} + 3^x = 3^x(9 + 1) = 10 \cdot 3^x = 810$.",
     r"$3^x = 81 = 3^4$ ⇒ $x = 4$."),
  r"Take out the smaller power: bracket = 10, so $3^x = 81$ ⇒ $x = 4$.",
  "medium", "simp-surds-indices", "indices equation", 40))

v = sp.sqrt(248 + sp.sqrt(52 + sp.sqrt(144)))
assert v == 16
P.append(Q("simp-q11", r"Find the value of $\sqrt{248 + \sqrt{52 + \sqrt{144}}}$.",
  ["14", "15.6", "16", "18"], 2, v,
  md(r"Innermost: $\sqrt{144} = 12$.",
     r"$\sqrt{52 + 12} = \sqrt{64} = 8$.",
     r"$\sqrt{248 + 8} = \sqrt{256} = 16$."),
  "Inside-out: 12 → 64 → 8 → 256 → 16.",
  "medium", "simp-roots", "nested square roots", 35))

ex = 0.2997 * 1199.8 + 15.02 * 23.99
ov = [700, 720, 740, 760]
assert nearest(ov, ex) == 1
P.append(Q("simp-q12", r"What approximate value should come in place of '?': $29.97\% \text{ of } 1199.8 + 15.02 \times 23.99 = \ ?$",
  ["700", "720", "740", "760"], 1, 720,
  md(r"$29.97\% \text{ of } 1199.8 \approx 30\% \text{ of } 1200 = 360$.",
     r"$15.02 \times 23.99 \approx 15 \times 24 = 360$.",
     r"Total $\approx 720$ (exact ≈ 719.9)."),
  "30% of 1200 = 360 and 15 × 24 = 360 ⇒ 720.",
  "medium", "simp-approximation", "approximation", 40))

# hard
X = 3 + 2 * S(2)
e = S(X) - 1 / S(X)
assert abs(float(e) - 2) < 1e-12
assert abs(float(S(X) - (1 + S(2)))) < 1e-12 and abs(float(1 / S(X) - (S(2) - 1))) < 1e-12
P.append(Q("simp-q13", r"If $x = 3 + 2\sqrt{2}$, then the value of $\sqrt{x} - \frac{1}{\sqrt{x}}$ is:",
  ["1", r"$\sqrt{2}$", "2", r"$2\sqrt{2}$"], 2, 2,
  md(r"$x = 3 + 2\sqrt{2} = (\sqrt{2} + 1)^2$ ⇒ $\sqrt{x} = \sqrt{2} + 1$.",
     r"$\frac{1}{\sqrt{x}} = \frac{1}{\sqrt{2} + 1} = \sqrt{2} - 1$.",
     r"$\sqrt{x} - \frac{1}{\sqrt{x}} = (\sqrt{2} + 1) - (\sqrt{2} - 1) = 2$."),
  md(r"$\left(\sqrt{x} - \frac{1}{\sqrt{x}}\right)^2 = x + \frac{1}{x} - 2$.",
     r"$\frac{1}{x} = 3 - 2\sqrt{2}$ (since $9 - 8 = 1$) ⇒ $x + \frac{1}{x} = 6$ ⇒ square $= 4$ ⇒ value $= 2$."),
  "hard", "simp-surds-indices", "reciprocal surd expression", 75,
  vals=fv(1, S(2), 2, 2 * S(2))))

aa, bb = sp.symbols("a b", positive=True)
kk = 100.0
A_ = math.log(kk) / math.log(2)
B_ = math.log(kk) / math.log(3)
C_ = math.log(kk) / math.log(6)
assert abs(C_ - A_ * B_ / (A_ + B_)) < 1e-12
assert abs(C_ - (A_ + B_) / (A_ * B_)) > 0.1 and abs(C_ - A_ * B_) > 0.1 and abs(C_ - (A_ + B_)) > 0.1
opts = [r"$\frac{a+b}{ab}$", r"$\frac{ab}{a+b}$", r"$ab$", r"$a+b$"]
P.append(Q("simp-q14", r"If $2^a = 3^b = 6^c$, then $c$ is equal to:",
  opts, 1, opts[1],
  md(r"Let $2^a = 3^b = 6^c = k$. Then $2 = k^{1/a}$, $3 = k^{1/b}$, $6 = k^{1/c}$.",
     r"Since $6 = 2 \times 3$: $k^{1/c} = k^{1/a} \cdot k^{1/b} = k^{\frac{1}{a} + \frac{1}{b}}$.",
     r"$\frac{1}{c} = \frac{1}{a} + \frac{1}{b} = \frac{a + b}{ab}$ ⇒ $c = \frac{ab}{a + b}$."),
  r"Rule: when the bases multiply ($2 \times 3 = 6$), the reciprocals of the exponents add. Check with numbers: $2^{\log_2 36} = 3^{\log_3 36} = 6^2$ gives $c = 2$ and $\frac{ab}{a+b}$ matches.",
  "hard", "simp-surds-indices", "equal powers relation", 75))

num = F(1, 10)**3 + F(2, 100)**3
den = F(2, 10)**3 + F(4, 100)**3
v = num / den
assert v == F(1, 8)
P.append(Q("simp-q15", r"Simplify: $\frac{0.1 \times 0.1 \times 0.1 + 0.02 \times 0.02 \times 0.02}{0.2 \times 0.2 \times 0.2 + 0.04 \times 0.04 \times 0.04}$",
  ["0.0125", "0.125", "0.25", "0.5"], 1, v,
  md(r"Numerator $= 0.001 + 0.000008 = 0.001008$.",
     r"Denominator $= 0.008 + 0.000064 = 0.008064$.",
     r"Ratio $= \frac{0.001008}{0.008064} = \frac{1008}{8064} = \frac{1}{8} = 0.125$."),
  r"Every denominator number is exactly double the numerator one (0.2 = 2 × 0.1, 0.04 = 2 × 0.02), so denominator $= 2^3 \times$ numerator ⇒ answer $= \frac{1}{8} = 0.125$.",
  "hard", "simp-identities", "ratio of sums of cubes", 60))

topic = {
 "id": "simplification", "sectionId": "quant", "title": "Simplification", "order": 2,
 "importance": "medium", "avgQuestions": {"tier1": 2, "tier2": 1},
 "summary": "BODMAS, identity-based fractions, surds and indices, square/cube roots and approximation. These are the fastest marks in Tier 1 — usually 1–2 questions per shift — and the same skills (identities, surd handling) power the algebra questions.",
 "subtopics": subtopics, "pyqPatterns": pyq, "solvedExamples": solved, "practice": P,
}
write_topic(topic)
