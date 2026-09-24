"""Phase-2 deep content for quant/simplification — roots & approximation modules."""
import math
from _lib import Sub, nearest, num


def build_roots():
    S = Sub("simp-roots")
    S.notes = r"""### What you need about roots
A **square root** asks: which number times itself gives this? $\sqrt{11025} = 105$ because $105 \times 105 = 11025$. A **cube root** asks: which number cubed gives this? $\sqrt[3]{9261} = 21$.

### Spotting and finding perfect squares
- A perfect square never ends in 2, 3, 7 or 8, and never in an **odd** number of zeros.
- Last-digit map (root → square): 1 or 9 → 1; 2 or 8 → 4; 3 or 7 → 9; 4 or 6 → 6; 5 → 5; 0 → 0.
- To find $\sqrt{11025}$: pair digits from the right (1 | 10 | 25). First pair: $1^2 = 1$ → first digit 1. Double it (2); find digit $d$ so that $2d \times d$ fits 10 → $d = 4$ ($24 \times 4 = 96$)? 96 fits under 110? wait — work with 010 remainder 10: bring down 25 → 1025; $24\Box \times \Box \le 1025$ → $245 \times 5 = 1225$ too big, $244 \times 4 = 976$ ✓ → root 105? The long-division method always lands exactly; in exams you mostly **match options** with the last-digit map and a rough size check.

**Size check:** count digit pairs. A 5-digit number (like 11025 → pairs 1, 10, 25) has a 3-digit root. Between $100^2 = 10000$ and $110^2 = 12100$; last digit 5 → root ends in 5 → 105.

### Cube roots in seconds
Group digits in **threes** from the right. The number of groups = number of root digits.
- Unit digit of cube → unit digit of root: 1↔1, 4↔4, 5↔5, 6↔6, 9↔9, 0↔0, and swaps 2↔8, 3↔7.
Example: $\sqrt[3]{9261}$: groups 9 | 261. Cube ends in 1 → root ends in 1. $2^3 = 8 \le 9 < 27 = 3^3$ → first digit 2. Root = **21**.

### Roots of decimals
The decimal point just shifts: $\sqrt{0.0169} = 0.13$ (2 decimal places in → 1 in the root); $\sqrt[3]{0.000064} = 0.04$ (6 places → 2 places).

### Least number to make a perfect square
"Find the least number to be **subtracted** from N": take $\sqrt{N}$, keep the whole part $k$, answer $= N - k^2$.
"Least number to be **added**": use $(k+1)^2$; answer $= (k+1)^2 - N$.
Example: $N = 1300$: $36^2 = 1296 < 1300 < 1369 = 37^2$ → add 69.

### Nested radicals
- **Infinite $\sqrt{a+\sqrt{a+\dots}}$** equals the positive root of $x^2 = a + x$. For $a = 6$: $x^2 - x - 6 = 0$ → $x = 3$.
- **Infinite $\sqrt{a \times \sqrt{a \times \dots}}$** equals $a$.
- **Finite nests** are worked from the **inside out**: $\sqrt{30 + \sqrt{24 + \sqrt{144}}} = \sqrt{30 + \sqrt{36}} = \sqrt{36} = 6$.
- Quick identity: if $n = k(k+1)$ then $\sqrt{n + \sqrt{n + \dots}} = k+1$ (e.g. 12 = 3 × 4 → 4) and $\sqrt{n - \sqrt{n - \dots}} = k$.

### Root equations
Move the root to one side, square both sides once: $\sqrt{1 + \frac{x}{225}} = \frac{16}{15}$ → $1 + \frac{x}{225} = \frac{256}{225}$ → $x = 31$.

### Quick revision
- Perfect squares: last digit in {0,1,4,5,6,9}; size from digit pairs; exact digit from the map.
- Cube root: groups of three digits; unit-digit swap map.
- Subtract → $N - k^2$; add → $(k+1)^2 - N$.
- Infinite $\sqrt{a+\sqrt{a+\dots}}$: solve $x^2 = a + x$.
- Nested roots: inside out.
"""

    S.pattern("simp-rt-p1", "Square root or cube root of a perfect power", "very common",
        r"'Find $\sqrt{11025}$' or 'Find $\sqrt[3]{9261}$' — the number under the root is a perfect square/cube (options are clean).",
        r"\text{square: digit pairs; cube root: digit triples, unit digits mapped}",
        r"""1. For a cube root, group digits in threes from the right; the count of groups = root's digit count; use the unit-digit swap map (2↔8, 3↔7) and a size check for the first digit.
2. For a square root, pair digits from the right to fix the root's size, then use the last-digit map (root 2/8 → square ends 4, root 3/7 → 9, etc.).
3. Always verify by squaring/cubing the option.

Why: option-matching with the unit-digit map is much faster than long division.""",
        r"Find $\sqrt[3]{9261}$.",
        r"Groups 9 | 261 → two digits; cube ends in 1 → root ends in 1; $2^3 = 8 \le 9$ → **21**.")
    S.pattern("simp-rt-p2", "Least number to add or subtract to reach a perfect square", "very common",
        "'Least number which must be added to (or subtracted from) N so the result is a perfect square.'",
        r"\text{subtract: } N - k^2, \quad \text{add: } (k+1)^2 - N \text{ where } k = \lfloor\sqrt{N}\rfloor",
        r"""1. Find the whole part $k$ of $\sqrt N$ (bracket N between two squares).
2. Subtract case: answer $= N - k^2$.
3. Add case: answer $= (k+1)^2 - N$.

Why: the nearest squares on either side of N are exactly $k^2$ and $(k+1)^2$.""",
        "Least number to add to 1300 for a perfect square?",
        r"$36^2 = 1296 < 1300 < 1369 = 37^2$ → add $1369 - 1300 = 69$.")
    S.pattern("simp-rt-p3", "Nested radicals (finite) and simple root equations", "common",
        r"A stack like $\sqrt{30+\sqrt{24+\sqrt{144}}}$, or an equation where $x$ sits under a square root.",
        r"\text{evaluate from the innermost root outward; for equations, square both sides once}",
        r"""1. Start at the deepest root and replace it by its value.
2. Move one layer out at a time — each root now becomes exact.
3. If $x$ is under a root, isolate the root and square both sides.

Why: each layer is built to collapse into the next perfect square.""",
        r"Find $\sqrt{30 + \sqrt{24 + \sqrt{144}}}$.",
        r"$\sqrt{144} = 12$ → $24+12 = 36$ → $\sqrt{36} = 6$ → $30+6 = 36$ → answer $6$.")
    S.pattern("simp-rt-p4", r"Infinite radicals: $\sqrt{a+\sqrt{a+\dots}}$ and $\sqrt{a\times\sqrt{a\times\dots}}$", "common",
        "The pattern repeats forever — 'infinite' or '⋯' appears, or the expression just trails off.",
        r"x = \sqrt{a + x} \ \text{(plus form)}, \qquad x = \sqrt{ax} \ \text{(product form)}, \qquad \sqrt{k(k+1)+\sqrt{\dots}} = k+1",
        r"""1. Call the whole expression $x$; the tail inside equals $x$ again.
2. Plus form: $x^2 = a + x$ → solve the quadratic, keep the positive root (shortcut: if $a = k(k+1)$, the answer is $k+1$).
3. Product form: $x^2 = ax$ → $x = a$ (ignore $x = 0$).

Why: self-similarity turns the infinite tower into one equation.""",
        r"Find $\sqrt{6 + \sqrt{6 + \sqrt{6 + \cdots}}}$.",
        r"$x^2 = 6 + x$ → $(x-3)(x+2) = 0$ → $x = 3$ (since $6 = 2 \times 3$, answer $k+1 = 3$).")

    assert 105 ** 2 == 11025 and 100 ** 2 < 11025 < 110 ** 2
    S.q("simp-rt-p1", "easy", r"Find the value of $\sqrt{11025}$.",
        ["105", "115", "125", "1005"], "105",
        r"""Digit pairs from the right: 1 | 10 | 25 → a three-digit root.
$100^2 = 10000$ and $110^2 = 12100$, so the root is between 100 and 110. A square ending in 25 comes from a root ending in 5 → **105**.
Check: $105^2 = 11025$ ✓.""",
        None, 40)
    assert 21 ** 3 == 9261 and 9261 // 1000 == 9
    S.q("simp-rt-p1", "easy", r"Find the value of $\sqrt[3]{9261}$.",
        ["21", "31", "11", "27"], "21",
        r"""Groups of three from the right: 9 | 261 → a two-digit root.
Cube ends in 1 → root ends in 1 (or 9 wait: only 1³ ends in 1). First group $8 \le 9$ → tens digit 2. Root = **21**.""",
        "Unit-digit map: cube ends 1 → root ends 1; 2³ = 8 fits under 9.", 35)
    assert abs(0.04 ** 3 - 0.000064) < 1e-12
    S.q("simp-rt-p1", "medium", r"Find the value of $\sqrt[3]{0.000064}$.",
        ["0.04", "0.4", "0.004", "0.02"], "0.04",
        r"$0.000064 = 64 \times 10^{-6}$ and $\sqrt[3]{64} = 4$, $\sqrt[3]{10^{-6}} = 10^{-2}$. Value $= 4 \times 0.01 = 0.04$.",
        "6 decimal places → 2 decimal places in the root.", 35)
    k = int(math.isqrt(9238))
    v = 9238 - k * k
    assert k == 96 and v == 22 and (k + 1) ** 2 > 9238
    S.q("simp-rt-p2", "medium",
        "What is the least number that must be subtracted from 9238 so that the result is a perfect square?",
        ["22", "74", "96", "19"], str(v),
        r"""$\sqrt{9238}$ lies between $96^2 = 9216$ and $97^2 = 9409$.
$9238 - 9216 = 22$ → subtract **22** to land on 9216.""",
        "Trap 96: that is the root, not the number subtracted.", 50)
    k = int(math.isqrt(1300))
    v = (k + 1) ** 2 - 1300
    assert k == 36 and v == 69
    S.q("simp-rt-p2", "medium",
        "What is the least number that must be added to 1300 so that the result is a perfect square?",
        ["69", "31", "36", "25"], str(v),
        r"""$36^2 = 1296 < 1300 < 1369 = 37^2$.
So the next square is 1369, and $1369 - 1300 = 69$.""",
        "Trap 31 would be right only if 36² were above 1300.", 45)
    v = math.isqrt(30 + math.isqrt(24 + math.isqrt(144)))
    assert math.isqrt(144) == 12 and 24 + 12 == 36 and 30 + 6 == 36 and v == 6
    S.q("simp-rt-p3", "medium", r"Find the value of $\sqrt{30 + \sqrt{24 + \sqrt{144}}}$.",
        ["6", "8", "4", "12"], str(v),
        r"""Inside out: $\sqrt{144} = 12$; $24 + 12 = 36$; $\sqrt{36} = 6$; $30 + 6 = 36$; $\sqrt{36} = 6$.""",
        None, 40)
    x = 225 * ((16 / 15) ** 2 - 1)
    assert abs(x - 31) < 1e-9 and 225 + 31 == 256
    S.q("simp-rt-p3", "medium",
        r"If $\sqrt{1 + \dfrac{x}{225}} = \dfrac{16}{15}$, what is the value of $x$?",
        ["31", "41", "25", "1"], "31",
        r"""Square both sides: $1 + \frac{x}{225} = \frac{256}{225}$.
$\frac{x}{225} = \frac{256 - 225}{225} = \frac{31}{225}$ → $x = 31$.""",
        None, 40)
    # infinite radical sqrt(6+sqrt(6+...))
    r = 3
    assert abs(r * r - (6 + r)) < 1e-12
    S.q("simp-rt-p4", "medium", r"Find the value of $\sqrt{6 + \sqrt{6 + \sqrt{6 + \cdots \infty}}}$.",
        ["3", "6", "2", "12"], "3",
        r"""Let $x = \sqrt{6 + \sqrt{6 + \dots}}$. Then $x^2 = 6 + x$, i.e. $x^2 - x - 6 = 0$.
$(x-3)(x+2) = 0$ → $x = 3$ (positive root).""",
        "Shortcut: 6 = 2 × 3 = k(k+1) with k = 2 → answer k + 1 = 3.", 40)
    S.q("simp-rt-p4", "medium", r"Find the value of $\sqrt{20 \times \sqrt{20 \times \sqrt{20 \times \cdots \infty}}}$.",
        ["20", "400", "10", "5"], "20",
        r"""Let $x = \sqrt{20x}$. Squaring: $x^2 = 20x$ → $x = 20$ (non-zero root).
The infinite product-radical always equals the number itself.""",
        None, 35)
    return S


def build_approx():
    S = Sub("simp-approximation")
    S.notes = r"""### What is an approximation question?
The question says "what approximate value comes in place of ?" — the numbers are deliberately awkward (1199.8, 24.98%, √2303.9) and the **options are far apart**. You are allowed to round every number to a friendly value, compute, and pick the closest option. Perfection is not wanted; speed is.

### The rounding rules
- Decimals round to the nearest whole number: 49.98 → 50, 15.02 → 15, 23.9 → 24.
- Percentages become fractions: 24.9% ≈ $\frac{1}{4}$, 33.3% ≈ $\frac{1}{3}$, 16.7% ≈ $\frac{1}{6}$, 12.5% = $\frac{1}{8}$, 19.9% ≈ $\frac{1}{5}$, 66.6% ≈ $\frac{2}{3}$.
- Near-perfect squares: √2303.9 ≈ 48 (since $48^2 = 2304$), √3968.9 ≈ 63, √625 ≈ 25.
- Near-perfect cubes: ∛29791.03 ≈ 31 ($31^3 = 29791$).
- Multiplying two rounded numbers? Round one **up** and the other **down** when you can — the errors cancel.

### The fraction–percentage anchors (learn cold)
| Fraction | Percent | Fraction | Percent |
|---|---|---|---|
| 1/2 | 50% | 1/9 | 11.1% |
| 1/3 | 33.3% | 1/11 | 9.09% |
| 1/4 | 25% | 1/12 | 8.33% |
| 1/5 | 20% | 1/8 | 12.5% |
| 1/6 | 16.67% | 2/5 | 40% |
| 1/7 | 14.28% | 3/4 | 75% |

So "16.98% of 800" → $\frac{1}{6} \times 800 ≈ 133$ — no pen needed.

### The usual question shapes
1. **One expression**: 29.9% of 1199.8 + 15.02 × 23.9 → $360 + 360 = 720$.
2. **Find ?**: 34.9% of 599.8 + ? = 299.9 → $210 + ? = 300$ → ? = 90.
3. **Roots and powers mixed**: (23.98)² + √2303.9 − 4.99 × 8.01 → $576 + 48 - 40 = 584$.
4. **Equation in ?**: (?)% of 650 + 40 = 350 → ? = 310/650 × 100 ≈ 48.

### How precise must you be?
Work to the nearest ten (or nearest hundred for big numbers), then choose the option nearest to your answer. If two options are close, redo only the step that separates them.

### Two worked mini-examples
- $\sqrt{3968.9} + \sqrt[3]{29791.03}$: $63^2 = 3969$ and $31^3 = 29791$, so the value is $63 + 31 = 94$. Both roots were placed next to perfect powers on purpose — that is how the setter builds the question.
- $\sqrt[3]{729.05} \times 12.99 ≈ 18.02\%$ of ?: left side $= 9 \times 13 = 117$. Then $? = 117 \times \frac{100}{18} ≈ 650$. When ? is on the **right of a percentage**, divide by the fraction instead of multiplying.

### Sanity checks that save marks
- **Size first:** decide whether the answer is in the tens, hundreds or thousands before computing — one option in each region is usually a decoy.
- **Direction of %:** "18% of ? = 117" means $? = 117 \div 0.18$ (bigger than 117); "?% of 650 = 310" means ? is a percentage (around 48). Mixing these two up flips the answer by orders of magnitude.
- **Balanced rounding:** for $15.02 \times 23.9$ use $15 \times 24$ — you rounded one factor down and the other up, so the error largely cancels.

### Quick revision
- Round everything; options are spaced 5–10% apart.
- Percent → fraction anchors; squares/cubes nearby.
- Round up-and-down pairs for products.
- Then pick the closest option, never recompute from scratch.
"""

    S.pattern("simp-ap-p1", "Mixed chain: % of, × and ÷ in one expression", "very common",
        r"'? ≈' with a chain like $29.9\% \text{ of } 1199.8 + 15.02 \times 23.9$ — awkward decimals everywhere.",
        r"\text{round every number to a friendly value, then compute exactly on the rounded numbers}",
        r"""1. Round each decimal to the nearest whole/ten (1199.8 → 1200, 23.9 → 24).
2. Convert percentages to the nearest fraction anchor (24.9% → 1/4).
3. Compute the rounded expression and pick the closest option.

Why: the options sit 5–10% apart, but rounding error is usually under 2%.""",
        r"$29.9\% \text{ of } 1199.8 + 15.02 \times 23.9 ≈ \ ?$",
        r"$30\%$ of $1200 = 360$; $15 \times 24 = 360$; total $≈ 720$.")
    S.pattern("simp-ap-p2", "Percentage chains and (?)% equations", "very common",
        "Two or more 'x% of N' terms added/subtracted, or an equation where ? is the unknown percentage.",
        r"(?)\% = \frac{\text{target} - \text{known part}}{\text{base}} \times 100",
        r"""1. Replace each % with its fraction anchor and each N with a round number.
2. For an equation, shift the known parts to the other side first.
3. Then ? (%) = remainder ÷ base × 100, rounded to the nearest option.

Why: 'percent of a round hundred' is a one-step mental product.""",
        r"$(?)\% \text{ of } 649.9 + 39.98 = 349.9$ — find ?.",
        r"$350 - 40 = 310$; $310/650 \times 100 ≈ 48$.")
    S.pattern("simp-ap-p3", "Roots and powers inside an approximation", "common",
        "The expression hides near-perfect squares/cubes: √2303.9, (23.98)², ∛29791.03.",
        r"\sqrt{N} \approx r \text{ if } r^2 \approx N; \quad (a.\!99)^2 \approx a^2",
        r"""1. Snap each root to the nearest perfect power: √3968.9 → 63 (since $63^2 = 3969$).
2. Snap each square to the rounded base: (23.98)² → 576.
3. Combine, then pick the nearest option.

Why: exam roots/squares are placed within 0.05 of a perfect power on purpose.""",
        r"$\sqrt{3968.9} + \sqrt[3]{29791.03} ≈ \ ?$",
        r"$63 + 31 = 94$ ($63^2 = 3969$, $31^3 = 29791$).")
    S.pattern("simp-ap-p4", "Find the missing value ?", "very common",
        "The ? is a full term of the equation, not necessarily a percentage: '34.9% of 599.8 + ? = 299.85'.",
        r"? = \text{(constant side)} - \text{(evaluated terms)}",
        r"""1. Evaluate every term that contains no ?.
2. Move it to the other side of the equation (addition ↔ subtraction; × ↔ ÷).
3. Round the result to the closest option; sanity-check its size.

Why: it is the same one-move algebra as the exact topic, just done on rounded numbers.""",
        r"$34.9\% \text{ of } 599.8 + ? = 299.85$ — find ?.",
        r"$35\%$ of $600 = 210$; $? ≈ 300 - 210 = 90$.")

    # p1 mixed chains
    exact = 0.299 * 1199.8 + 15.02 * 23.9
    opts, ans = nearest([("720", 720), ("660", 660), ("780", 780), ("600", 600)], exact, 0.04)
    assert abs(exact - 717.7) < 1
    S.q("simp-ap-p1", "easy",
        r"What approximate value will come in place of '?': $29.9\% \text{ of } 1199.8 + 15.02 \times 23.9 = \ ?$",
        opts, ans,
        rf"""Round: $30\%$ of $1200 = 360$; $15 \times 24 = 360$.
Answer $≈ 360 + 360 = 720$. (Exact value ${exact:.1f}$. Options are spaced ~10% apart, so rounding is safe.)""",
        r"30% of 1200 = 360 straight from the 3/10 anchor.", 40)
    exact = 23.98 ** 2 + math.sqrt(2304.2) - 4.99 * 8.01
    opts, ans = nearest([("584", 584), ("544", 544), ("624", 624), ("504", 504)], exact, 0.04)
    assert abs(exact - 583.07) < 1
    S.q("simp-ap-p1", "medium",
        r"What approximate value will come in place of '?': $(23.98)^2 + \sqrt{2303.9} - 4.99 \times 8.01 = \ ?$",
        opts, ans,
        rf"""Round: $24^2 = 576$; $\sqrt{{2304}} = 48$; $5 \times 8 = 40$.
$576 + 48 - 40 = 584$. (Exact ${exact:.1f}$.)""",
        None, 45)
    exact = 1249.85 / 24.98 + 0.199 * 799.9
    opts, ans = nearest([("209", 209), ("259", 259), ("159", 159), ("309", 309)], exact, 0.04)
    assert abs(exact - 209.2) < 1
    S.q("simp-ap-p1", "medium",
        r"What approximate value will come in place of '?': $1249.85 \div 24.98 + 19.9\% \text{ of } 799.9 = \ ?$",
        opts, ans,
        rf"""Round: $1250 \div 25 = 50$; $\frac{{1}}{{5}}$ of $800 = 160$.
$50 + 160 = 210$ → nearest option 209. (Exact ${exact:.1f}$.)""",
        "19.9% ≈ 1/5.", 40)
    # p2 percentage based
    exact = 0.2405 * 1199.9 + 0.1698 * 800.1
    opts, ans = nearest([("424", 424), ("374", 374), ("474", 474), ("324", 324)], exact, 0.04)
    assert abs(exact - 424.4) < 1
    S.q("simp-ap-p2", "easy",
        r"What approximate value will come in place of '?': $24.05\% \text{ of } 1199.9 + 16.98\% \text{ of } 800.1 = \ ?$",
        opts, ans,
        rf"""Round: $\frac{{1}}{{4}}$ of $1200 = 300$; $\frac{{1}}{{6}}$ of $800 ≈ 133$.
$300 + 133 = 433$ → nearest option 424. (Exact ${exact:.1f}$.)""",
        None, 40)
    exact = 0.4205 * 699.85 + 0.581 * 400.2
    opts, ans = nearest([("527", 527), ("487", 487), ("567", 567), ("447", 447)], exact, 0.04)
    assert abs(exact - 526.7) < 1
    S.q("simp-ap-p2", "medium",
        r"What approximate value will come in place of '?': $42.05\% \text{ of } 699.85 + 58.1\% \text{ of } 400.2 = \ ?$",
        opts, ans,
        rf"""Round: $42\%$ of $700 ≈ 294$; $58\%$ of $400 = 232$.
$294 + 232 = 526$ → option 527. (Exact ${exact:.1f}$.)""",
        None, 40)
    q = (349.9 - 39.98) / 649.9 * 100
    opts, ans = nearest([("48", 48), ("42", 42), ("54", 54), ("38", 38)], q, 0.06)
    assert abs(q - 47.69) < 0.5
    S.q("simp-ap-p2", "medium",
        r"What approximate value will come in place of '?': $(?)\% \text{ of } 649.9 + 39.98 = 349.9$",
        opts, ans,
        rf"""Move the known part: $(?)\%$ of $650 = 350 - 40 = 310$.
$? = \frac{{310}}{{650}} \times 100 ≈ 48$. (Exact ${q:.1f}$.)""",
        None, 45)
    # p3 roots
    exact = math.sqrt(3968.9) + 29791.03 ** (1 / 3)
    opts, ans = nearest([("94", 94), ("124", 124), ("64", 64), ("104", 104)], exact, 0.06)
    assert abs(exact - 94.0) < 0.5
    S.q("simp-ap-p3", "medium",
        r"What approximate value will come in place of '?': $\sqrt{3968.9} + \sqrt[3]{29791.03} = \ ?$",
        opts, ans,
        rf"""$63^2 = 3969$ → $\sqrt{{3968.9}} ≈ 63$. $31^3 = 29791$ → cube root $≈ 31$.
$63 + 31 = 94$.""",
        None, 40)
    exact = (math.sqrt(624.9) - math.sqrt(384.2)) * 8.03
    opts, ans = nearest([("43", 43), ("73", 73), ("23", 23), ("63", 63)], exact, 0.06)
    assert abs(exact - 43.3) < 0.5
    S.q("simp-ap-p3", "medium",
        r"What approximate value will come in place of '?': $(\sqrt{624.9} - \sqrt{384.2}) \times 8.03 = \ ?$",
        opts, ans,
        rf"""$\sqrt{{625}} = 25$; $\sqrt{{384}} ≈ 19.6$ (since $19.6^2 = 384.16$).
$(25 - 19.6) \times 8 ≈ 5.4 \times 8 = 43$.""",
        None, 45)
    # p4 find the missing value
    x = 299.85 - 0.349 * 599.8
    opts, ans = nearest([("90", 90), ("110", 110), ("70", 70), ("130", 130)], x, 0.06)
    assert abs(x - 90.4) < 0.6
    S.q("simp-ap-p4", "easy",
        r"If $34.9\% \text{ of } 599.8 + ? = 299.85$, then $? ≈$",
        opts, ans,
        rf"""$35\%$ of $600 = 210$.
$300 - 210 = 90$. (Exact ${x:.1f}$.)""",
        None, 35)
    y = 0.1998 * 1199.9 - 4.01 ** 2
    opts, ans = nearest([("224", 224), ("264", 264), ("184", 184), ("244", 244)], y, 0.04)
    assert abs(y - 223.8) < 1
    S.q("simp-ap-p4", "medium",
        r"What approximate value will come in place of '?': $19.98\% \text{ of } 1199.9 - (4.01)^2 = \ ?$",
        opts, ans,
        rf"""$20\%$ of $1200 = 240$; $4^2 = 16$.
$240 - 16 = 224$.""",
        None, 35)
    z = (729.05 ** (1 / 3) * 12.99) / 0.1802
    opts, ans = nearest([("650", 650), ("700", 700), ("600", 600), ("750", 750)], z, 0.04)
    assert abs(z - 649.2) < 2
    S.q("simp-ap-p4", "hard",
        r"What approximate value will come in place of '?': $\sqrt[3]{729.05} \times 12.99 ≈ 18.02\% \text{ of } \ ?$",
        opts, ans,
        rf"""$\sqrt[3]{{729}} = 9$; $9 \times 13 = 117$.
$117 ≈ 18\%$ of $?$ → $? = 117 \times \frac{{100}}{{18}} ≈ 650$.""",
        r"18% ≈ 2/11, so ? ≈ 117 × 11/2 = 643.5 → 650.", 50)
    return S
