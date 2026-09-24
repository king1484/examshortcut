"""Phase-2 deep content for quant/ratio-proportion — ages module."""
import os
import sys

sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
from _lib import Sub


def build_ages():
    S = Sub("rp-ages")
    S.notes = r"""### The three invariants
- Each person's age grows by **1 every year** — add n to BOTH ages for a shift of n years, and 2n to a sum of two ages.
- The **difference** of two ages never changes (32-year gap now is 32 forever).
- The **ratio** keeps changing — that is what the questions exploit.

### The multiplier template
Present ages in ratio $a : b$ → write them as $ax$ and $bx$. The shifted condition becomes one equation:
$$\frac{ax + n}{bx + n} = \frac{p}{q} \quad \text{(n years hence)}, \qquad \frac{ax - n}{bx - n} = \frac{p}{q} \quad \text{(n years ago)}.$$
One cross-multiplication gives x. If the question gives a sum or difference instead of a ratio, $(a+b)x$ or $(b-a)x$ is that value — no shift needed.

### The constant-difference checker
After solving, verify: the age difference now must equal the difference at any other time. For a father 3 times the son with son 16: gap = 32; eight years ago it was still 32 (24 vs 8 — father 5 times ✓, matching the given 5 : 1). This check kills half the wrong options without solving anything.

### 'k times' questions
"Father is k times the son" → father = k·son. Use the son as the variable; the second condition (after/before n years) gives one linear equation. Remember the ratio number DROPS as time moves forward (k decreases: 5 times → 3 times), never grows, for an older–younger pair.

### Double-ratio questions
A ratio 'n years ago' AND a ratio 'n years hence' → ages $(ax - n, bx - n)$ and $(ax + n, bx + n)$: two equations, one unknown x — eliminate by subtracting or cross-multiplying both. The 2n gap between the two time points is the easiest slip.

### The sum trick for two people
Sum of ages grows by exactly 2 per year (two people) or 2n per n years. So "the sum of present ages is 40; what was it 5 years ago?" — answer 30, no ratios needed. Combined with a ratio, the sum pins the pair instantly: ratio 3 : 5 with sum 40 → parts of 5 → 15 and 25.

### Three-person ages
Ratios among three people (A : B : C = 4 : 5 : 6) work exactly like two — write 4x, 5x, 6x. Only pairwise conditions appear in exams ("A is 6 years older than C" → 2x = 6), because three independent shifts would over-determine the problem.

### Typical wrong options, decoded
- Shifting the ratio instead of the ages: "ratio 4 : 5 now, 5 : 6 after n years" answered with ages $4 + n, 5 + n$ — the 4 : 5 ratio never applies again.
- Adding n to only one person's age.
- For 'k times', setting the ELDER as the unknown k times over — the younger must carry the single x.

### Quick revision
- Ages = ax, bx; shift adds/subtracts n on both.
- Difference constant; sum changes by 2 per year.
- k times → write the larger as k × smaller.
- Two shifted ratios → two equations in the same x.
"""

    S.pattern("rp-a1", "Present ratio with sum or difference", "very common",
        "'Ages are in ratio a : b and their sum (or difference) is S' — no time shift at all.",
        r"(a + b)x = S \ \text{or} \ (b - a)x = D",
        r"""1. Total parts = a + b (or the gap = b − a for a difference).
2. One part = S ÷ total parts.
3. Multiply by the asked person's parts.

Why: with no shift, this is a plain ratio division of the given total.""",
        "The ages of two brothers are in the ratio 3 : 4 and the sum of their ages is 35 years. The younger brother's age is:",
        r"7 parts = 35 → 1 part = 5 → younger $= 3 \times 5 = 15$ years.")
    S.pattern("rp-a2", "Ratio now and ratio after/before n years", "very common",
        "'The present ages are in ratio a : b; after (or before) n years the ratio will be p : q.'",
        r"\frac{ax \pm n}{bx \pm n} = \frac{p}{q}",
        r"""1. Write present ages as ax, bx.
2. Add or subtract n on BOTH, equate to p : q.
3. Cross-multiply once and solve for x.

Why: both ages move by the same n, so the ratio shifts in a way that pins x exactly.""",
        "The present ages of P and Q are in the ratio 5 : 6. Four years from now, the ratio will become 6 : 7. P's present age is:",
        r"$\frac{5x + 4}{6x + 4} = \frac{6}{7}$ → $35x + 28 = 36x + 24$ → x = 4 → P = 20 years.")
    S.pattern("rp-a3", "'k times as old' questions", "very common",
        "'A father is 4 times as old as his daughter; after 5 years he will be 3 times as old' — one multiple now, another later.",
        r"F = kS, \quad F \pm n = k'(S \pm n)",
        r"""1. Take the younger age as S; the elder is kS.
2. Apply the second condition at the shifted time.
3. Solve the small linear equation; check the constant difference.

Why: both conditions are statements about the same two numbers at two dates.""",
        "A mother is 4 times as old as her daughter. After 5 years, the mother will be 3 times as old as the daughter. The mother's present age is:",
        r"$4d + 5 = 3(d + 5)$ → $d = 10$ → mother $= 40$ years. (Gap 30 is constant: 40/10 now, 45/15 later ✓.)")
    S.pattern("rp-a4", "Two shifted ratios (ago and hence)", "common",
        "'n years ago the ratio was a : b, and n years hence it will be p : q' — two snapshots bracket the present.",
        r"\frac{ax - n}{bx - n} = \frac{a'}{b'}, \qquad \frac{ax + n}{bx + n} = \frac{p}{q}",
        r"""1. Write both equations in the same x.
2. Cross-multiply each (or subtract the two statements — the 2n shift cancels x cleanly).
3. Solve for x, then build the present ages.

Why: both snapshots describe the same present ages, x links them.""",
        "Ten years ago the ages of A and B were in the ratio 2 : 3. Ten years from now the ratio will be 4 : 5. A's present age is:",
        r"$\frac{2x + 20}{3x + 20} = \frac{4}{5}$ → $10x + 100 = 12x + 80$ → x = 10 → A $= 2(10) + 10 = 30$ years.")

    assert 35 // 7 * 3 == 15
    S.q("rp-a1", "easy",
        "The ages of two brothers are in the ratio 3 : 4 and the sum of their ages is 35 years. The younger brother's age is:",
        ["15 years", "20 years", "12 years", "18 years"], "15 years",
        r"""Total parts = 7 → 1 part = 5.
Younger $= 3 \times 5 = 15$ years (elder 20).""",
        None, 25)
    assert 48 // 16 == 3
    S.q("rp-a1", "easy",
        "The present ages of A and B are in the ratio 6 : 7 and the difference of their ages is 4 years. A's present age is:",
        ["24 years", "28 years", "20 years", "30 years"], "24 years",
        r"""1 part = 4 (the difference is one part) → A $= 6 \times 4 = 24$ years.""",
        None, 25)
    assert (5 * 4 + 4) * 7 == 6 * (6 * 4 + 4)
    S.q("rp-a2", "medium",
        "The present ages of P and Q are in the ratio 5 : 6. Four years from now, the ratio of their ages will be 6 : 7. P's present age is:",
        ["20 years", "24 years", "16 years", "28 years"], "20 years",
        r"""$\frac{5x + 4}{6x + 4} = \frac{6}{7}$ → $35x + 28 = 36x + 24$ → $x = 4$.
P $= 5 \times 4 = 20$ years.""",
        None, 40)
    S.q("rp-a2", "medium",
        "The ages of A and B are in the ratio 7 : 9. Six years ago, the ratio of their ages was 5 : 7. The sum of their present ages is:",
        ["48 years", "42 years", "54 years", "36 years"], "48 years",
        r"""$\frac{7x - 6}{9x - 6} = \frac{5}{7}$ → $49x - 42 = 45x - 30$ → $x = 3$.
Ages 21 and 27 → sum $= 48$ years.""",
        None, 40)
    assert 4 * 10 + 5 == 3 * 15
    S.q("rp-a3", "medium",
        "A mother is 4 times as old as her daughter. After 5 years, the mother will be 3 times as old as the daughter. The mother's present age is:",
        ["40 years", "36 years", "44 years", "45 years"], "40 years",
        r"""Let the daughter be d → mother 4d.
$4d + 5 = 3(d + 5)$ → $d = 10$ → mother $= 40$ years.""",
        None, 40)
    assert (15 + 25 + 10) == 2 * (15 + 10)
    S.q("rp-a3", "medium",
        "Rohit is 25 years older than his son. Ten years from now, Rohit will be twice as old as his son. The son's present age is:",
        ["15 years", "12 years", "18 years", "20 years"], "15 years",
        r"""Son s → Rohit $s + 25$.
$s + 25 + 10 = 2(s + 10)$ → $s = 15$ years.""",
        None, 40)
    assert (2 * 10 + 20) * 5 == 4 * (3 * 10 + 20)
    S.q("rp-a4", "hard",
        "Ten years ago, the ages of A and B were in the ratio 2 : 3. Ten years from now, the ratio of their ages will be 4 : 5. A's present age is:",
        ["30 years", "32 years", "28 years", "36 years"], "30 years",
        r"""Ten years ago: 2x, 3x; ten years hence: $2x + 20$, $3x + 20$.
$\frac{2x + 20}{3x + 20} = \frac{4}{5}$ → $10x + 100 = 12x + 80$ → $x = 10$.
A now $= 2 \times 10 + 10 = 30$ years.""",
        None, 50)
    assert (3 * 4 + 8) * 7 == 5 * (5 * 4 + 8)
    S.q("rp-a4", "hard",
        "Four years ago, the ages of A and B were in the ratio 3 : 5. Four years from now, the ratio will be 5 : 7. The sum of their present ages is:",
        ["40 years", "36 years", "44 years", "48 years"], "40 years",
        r"""Four years ago: 3x, 5x; four years hence: $3x + 8$, $5x + 8$.
$\frac{3x + 8}{5x + 8} = \frac{5}{7}$ → $21x + 56 = 25x + 40$ → $x = 4$.
Ages now: 16 and 24 → sum $= 40$ years.""",
        None, 50)
    return S
