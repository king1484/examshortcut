"""Phase-2 deep content for quant/percentage — more/less module."""
import os
import sys

sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
from _lib import Sub


def build_moreless():
    S = Sub("pct-more-less")
    S.notes = r"""### The base decides everything
"A is x% more than B" uses **B** as the base; "B is ?% less than A" uses **A** as the base. Different denominators → different percentages. From 100 to 125 is $+25\%$, but from 125 back to 100 is $-20\%$ — a 25% rise is undone by a 20% fall, never by a 25% fall.

### The flip formulas
$$\text{More} \to \text{less}: \frac{100x}{100 + x}\%, \qquad \text{Less} \to \text{more}: \frac{100x}{100 - x}\%$$
Standard pairs to memorise: 25% more ↔ 20% less; 20% less ↔ 25% more; 50% more ↔ $33\frac{1}{3}$% less; 20% more ↔ $16\frac{2}{3}$% less.
Sanity check that kills wrong options: the "less" answer is always **smaller** than x, the "more" answer is always **bigger** than x.

### Assume the base = 100
The bullet-proof method: set the unmentioned quantity to 100, compute both values, then compute the asked percentage on its own base.
Example: A is 60% more than B → B = 100, A = 160 → B is $\frac{60}{160} \times 100 = 37.5\%$ less than A.
This also handles the recovery version: production falls from 1,500 to 1,200 → to regain 1,500 it must now rise by $\frac{300}{1200} \times 100 = 25\%$, not 20% — the base shrank, so the recovery percentage is always **bigger** than the fall.

### Chains of percentages
A = 30% of B and B = 40% of C → $A = \frac{30}{100} \times \frac{40}{100} \times C = 12\%$ of C. **Multiply** the fractions — never add.
Workplace version: 40% of the employees are graduates and 25% of the graduates are post-graduates → post-graduates $= \frac{40}{100} \times \frac{25}{100} = 10\%$ of all employees. The two percentages sit on different totals, so they chain.

### How the examiner flips the wording
Same arithmetic, four costumes:
- "A's salary is 25% more than B's" ↔ "B's salary is 20% less than A's".
- "A is heavier than B by 25%..." — weight of B is the base.
- "If A's income is 25% more than B's, B's income is less than A's by what %?" — the classic flip.
- "The marks of A are 20% less than B" → A/B = 4/5, so B is $\frac{1}{4}$ more = 25% more. Convert to the ratio A : B = 80 : 100 whenever the wording tangles you.

### Speed pairs worth memorising
| "more than" | equals "less than" (the other way) |
|---|---|
| 25% more | 20% less |
| $33\frac{1}{3}$% more | 25% less |
| 50% more | $33\frac{1}{3}$% less |
| $66\frac{2}{3}$% more | 40% less |
| 100% more | 50% less |
Reading the table right to left covers the "less → more" questions too.

### Quick revision
- More→less: $\frac{100x}{100 + x}$. Less→more: $\frac{100x}{100 - x}$.
- Base = 100 solves every variant, including chained ones.
- Chains: multiply fractions of successive bases.
- Recovery % > fall %; "less" answer < x < "more" answer.
"""

    S.pattern("pct-m1", "'More than' flipped to 'less than'", "very common",
        "'A's income is x% more than B's — B's income is what % less than A's?' The base changes mid-question.",
        r"\text{less}\% = \frac{100x}{100 + x}",
        r"""1. Flip formula: $\frac{100x}{100 + x}\%$ less.
2. Or set B = 100 → A = 100 + x; the gap x sits on base (100 + x).
3. Ratio route: A : B = (100 + x) : 100; less % = excess/base × 100.

Why: the same gap is x% of B but a smaller % of the bigger A.""",
        "A's income is 60% more than B's. B's income is what per cent less than A's?",
        r"B = 100, A = 160 → gap 60 on base 160 → $\frac{60}{160} \times 100 = 37.5\%$ less.")
    S.pattern("pct-m2", "'Less than' flipped to 'more than'", "very common",
        "'B is x% less than A — A is what % more than B?' Also appears as 'by what % must it rise to get back?'",
        r"\text{more}\% = \frac{100x}{100 - x}",
        r"""1. Flip formula: $\frac{100x}{100 - x}\%$ more.
2. Or set A = 100 → B = 100 − x; the gap x sits on the smaller base (100 − x).
3. Recovery version: fall from F to N → rise needed $= \frac{F - N}{N} \times 100\%$ — base is the reduced value.

Why: after a fall the base is smaller, so the matching rise is always the bigger number.""",
        "The production of a factory falls from 1,500 units to 1,200 units. By what per cent must it now increase to reach 1,500 units again?",
        r"Gap $= 300$ on the reduced base 1,200 → $\frac{300}{1200} \times 100 = 25\%$. (Not 20% — that would undo it on the old base.)")
    S.pattern("pct-m3", "Chained percentages (A is a% of B, B is b% of C)", "common",
        "'40% of the employees are graduates, 25% of the graduates are post-graduates' — a percentage of a percentage.",
        r"A = \frac{a}{100} \times \frac{b}{100} \times C \ \Rightarrow\ A = \frac{ab}{100}\% \text{ of } C",
        r"""1. Write each statement as a fraction of its own base.
2. Multiply the fractions: $\frac{a}{100} \times \frac{b}{100} \times C$.
3. Read A as $\frac{ab}{100}\%$ of the outermost base C.

Why: each percentage sits on a different total, so they compose multiplicatively — the same logic as successive discounts.""",
        "In an office, 40% of the employees are graduates and 25% of the graduates are post-graduates. Post-graduates form what per cent of all employees?",
        r"$\frac{40}{100} \times \frac{25}{100} = \frac{10}{100}$ → 10% of all employees. (Adding 40 + 25 = 65% is the trap.)")

    assert abs(60 / 160 * 100 - 37.5) < 1e-9
    S.q("pct-m1", "easy",
        "A's income is 60% more than B's. B's income is what per cent less than A's?",
        ["37.5%", "40%", "35%", "60%"], "37.5%",
        r"""Let B = 100 → A = 160. Gap = 60, base = 160.
$\frac{60}{160} \times 100 = 37.5\%$. (60% is the trap — wrong base.)""",
        None, 30)
    assert abs(50 / 150 * 100 - 100 / 3) < 1e-9
    S.q("pct-m1", "medium",
        "The price of a car is 50% more than that of a bike. The price of the bike is what per cent less than that of the car?",
        [r"$33\frac{1}{3}$%", "50%", "30%", "25%"], r"$33\frac{1}{3}$%",
        r"""Bike = 100 → car = 150. $\frac{50}{150} \times 100 = 33\frac{1}{3}\%$.""",
        None, 35)
    assert abs(20 / 80 * 100 - 25) < 1e-9
    S.q("pct-m2", "easy",
        "B's salary is 20% less than A's. A's salary is what per cent more than B's?",
        ["25%", "20%", "22.5%", "30%"], "25%",
        r"""A = 100 → B = 80. Gap = 20 on base 80 → $\frac{20}{80} \times 100 = 25\%$.""",
        None, 30)
    assert abs(25 / 75 * 100 - 100 / 3) < 1e-9
    S.q("pct-m2", "medium",
        "The population of village B is 25% less than that of village A. The population of A is what per cent more than that of B?",
        [r"$33\frac{1}{3}$%", "25%", "30%", "20%"], r"$33\frac{1}{3}$%",
        r"""A = 100 → B = 75. $\frac{25}{75} \times 100 = 33\frac{1}{3}\%$.""",
        None, 35)
    assert abs(0.3 * 0.4 * 100 - 12) < 1e-9
    S.q("pct-m3", "easy",
        "A is 30% of B, and B is 40% of C. Then A is what per cent of C?",
        ["12%", "10%", "14%", "70%"], "12%",
        r"""$A = \frac{30}{100} \times \frac{40}{100} \times C = \frac{12}{100}C$ → 12% of C.""",
        None, 25)
    assert abs(0.4 * 0.25 * 100 - 10) < 1e-9
    S.q("pct-m3", "medium",
        "In an office, 40% of the employees are graduates and 25% of the graduates are post-graduates. What per cent of the total employees are post-graduates?",
        ["10%", "65%", "15%", "6.5%"], "10%",
        r"""$\frac{40}{100} \times \frac{25}{100} = \frac{10}{100}$ → 10%.
(65% adds percentages on different bases — the classic trap.)""",
        None, 35)
    assert abs((1 / 6) / (7 / 6) * 100 - 100 / 7) < 1e-9
    S.q("pct-m1", "hard",
        r"A's height is $16\frac{2}{3}\%$ more than B's height. B's height is what per cent less than A's height?",
        [r"$14\frac{2}{7}$%", r"$16\frac{2}{3}$%", "14%", "15%"], r"$14\frac{2}{7}$%",
        r"""$16\frac{2}{3}\% = \frac{1}{6}$ → A : B = 7 : 6.
B is less by $\frac{1}{7} = 14\frac{2}{7}\%$ of A's height.""",
        r"Flip check: $\frac{100 \times 16\frac{2}{3}}{116\frac{2}{3}} = \frac{100/6}{7/6} = \frac{100}{7} = 14\frac{2}{7}\%$ ✓.", 45)
    assert 400 == 100 * 100 // 25
    S.q("pct-m2", "hard",
        "The daily water usage of city B is 75% less than that of city A. City A's usage is what per cent more than city B's?",
        ["300%", "75%", r"$133\frac{1}{3}$%", "400%"], "300%",
        r"""A = 100 → B = 25. Gap = 75 on base 25 → $\frac{75}{25} \times 100 = 300\%$.
(400% would answer 'A is what % of B'.)""",
        None, 45)
    S.q("pct-m3", "medium",
        "A's salary is 25% of B's salary, and B's salary is 20% of C's salary. A's salary is what per cent of C's salary?",
        ["5%", "45%", "4%", "50%"], "5%",
        r"""$A = \frac{25}{100} \times \frac{20}{100} \times C = \frac{5}{100}C$ → 5% of C.""",
        "Take C = 100 → B = 20 → A = 5, same result.", 35)
    assert abs(300 / 1200 * 100 - 25) < 1e-9
    S.q("pct-m2", "medium",
        "The output of a machine falls from 1,500 units to 1,200 units. By what per cent must the output increase to reach 1,500 units again?",
        ["25%", "20%", "30%", "22.5%"], "25%",
        r"""Required rise $= 300$ units on the reduced base 1,200 → $\frac{300}{1200} \times 100 = 25\%$.""",
        None, 35)
    S.pattern("pct-m4", "Two quantities compared through a common base", "common",
        "'A is x% more than C and B is y% more than C — A is what % of B?' Both percentages sit on the same hidden base.",
        r"A : B = (100 + x) : (100 + y) \ \Rightarrow\ \frac{A}{B} = \frac{100 + x}{100 + y} \times 100\%",
        r"""1. Set the common base C = 100.
2. A = 100 + x and B = 100 + y.
3. The asked ratio is A/B × 100 — one division.

Why: a shared base turns two independent percentages into one ratio.""",
        "A's height is 50% more than C's, and B's height is 20% more than C's. B's height is what per cent of A's height?",
        r"C = 100 → A = 150, B = 120 → $\frac{120}{150} \times 100 = 80\%$.")

    assert abs(125 / 150 * 100 - 83.33333333333333) < 1e-6
    S.q("pct-m4", "easy",
        "A's salary is 25% more than C's salary, and B's salary is 50% more than C's salary. A's salary is what per cent of B's salary?",
        [r"$83\frac{1}{3}$%", "75%", "80%", "85%"], r"$83\frac{1}{3}$%",
        r"""Let C = 100 → A = 125, B = 150.
$\frac{125}{150} \times 100 = 83\frac{1}{3}\%$.""",
        None, 30)
    assert abs(120 / 150 * 100 - 80) < 1e-9
    S.q("pct-m4", "medium",
        "The output of plant X is 50% more than that of plant Z, and the output of plant Y is 20% more than that of plant Z. The output of Y is what per cent of that of X?",
        ["80%", "70%", "85%", "75%"], "80%",
        r"""Z = 100 → X = 150, Y = 120 → $\frac{120}{150} \times 100 = 80\%$.""",
        None, 35)
    return S
