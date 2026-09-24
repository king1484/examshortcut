"""Phase-2 deep content for quant/percentage — basics & change modules."""
import os
import sys

sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
from _lib import Sub, num


def build_basics():
    S = Sub("pct-basics")
    S.notes = r"""### What does "per cent" mean?
Per cent means **out of hundred**: $x\% = \frac{x}{100}$. So 35% of a quantity means 35 parts out of every 100 parts of it: $35\% \text{ of } N = \frac{35N}{100}$.
Percentages let us compare unlike totals: 36/60 in one test and 45/75 in another are both 60% — instantly comparable.

### The fraction table (memorise cold — it pays for the whole topic)
| Fraction | % | Fraction | % |
|---|---|---|---|
| 1/2 | 50% | 1/8 | 12.5% |
| 1/3 | $33\frac{1}{3}$% | 3/8 | 37.5% |
| 2/3 | $66\frac{2}{3}$% | 1/6 | $16\frac{2}{3}$% |
| 1/4 | 25% | 5/6 | $83\frac{1}{3}$% |
| 3/4 | 75% | 1/7 | $14\frac{2}{7}$% |
| 1/5 | 20% | 1/9 | $11\frac{1}{9}$% |
| 2/5 | 40% | 1/12 | $8\frac{1}{3}$% |
| 5/8 | 62.5% | 1/16 | 6.25% |

### Four moves that answer every basic question
1. **x% of N** → fraction × N. $12.5\%$ of 960 $= \frac{1}{8} \times 960 = 120$.
2. **Recover the whole** from a part: if $p\%$ of N is k, then $N = \frac{100k}{p}$. 35% of N is 189 → $N = \frac{189 \times 100}{35} = 540$.
3. **One quantity as a % of another**: $\frac{A}{B} \times 100$. 45 out of 360 → $\frac{45}{360} \times 100 = 12.5\%$. The base sits right after the words "of" or "out of".
4. **Swap trick**: $x\%$ of $y = y\%$ of $x$. $4\%$ of 25 $= 25\%$ of 4 $= 1$.

### Chained percentages on the same base
$35\%$ of N $+ 45\%$ of N $= 80\%$ of N — add the percentages first when the base is the same. The same works for subtraction: "spent 30% on rent and 25% on food → 55% gone, 45% left."
But successive changes of the same quantity do **not** add — that is a different (and famous) trap covered in the increase/decrease subtopic.

### Using the unit-percent
1% of N is N ÷ 100. Build any percentage from tens and ones: 24% of 650 → 10% is 65, so 24% = 2 × 65 + 4 × 6.5 = 130 + 26 = 156. This mental decomposition is faster than any written multiplication.
The same idea runs in reverse: "what % is 78 of 650?" → 78 ÷ 6.5 = 12%.

### Percentages in everyday exam language
"60% of the students are boys" → 40% are girls, and any part = total × fraction. If 35% of the class are girls and there are 21 girls, the class size = 21 × 100/35 = 60. The exam always keeps totals whole, so a fractional total is a free signal that your arithmetic slipped.
Discount is a percentage of the marked price, and tax in these questions is simply added on the reduced amount afterwards.

### Where the base sits
"A is 20% of B" → B is the base. "What % of B is A?" → base is B again. Exam favourite: a fall from ₹250 to ₹200 is a 20% fall (base 250), but rising back from ₹200 to ₹250 is a 25% rise (base 200) — same ₹50, different base.

### Quick revision
- $x\% = \frac{x}{100}$; the fraction table is the speed key.
- Part → whole: $N = \frac{100k}{p}$.
- "What % of": divide by the base, × 100.
- $x\%$ of $y = y\%$ of $x$.
- Same base → add/subtract the percentages directly.
"""

    S.pattern("pct-b1", "Find x% of a number (fraction table)", "very common",
        "'What is 24% of 650?' or 'find $12\\frac{1}{2}$% of 960' — a direct percentage of a given number.",
        r"x\% \text{ of } N = \frac{x}{100} \times N",
        r"""1. Replace x% by its table fraction (12.5% → 1/8, 16⅔% → 1/6 …).
2. Divide N by the denominator, multiply by the numerator.
3. For ugly percentages, build them from 10% and 1% of N.

Why: percentages are fractions with a fixed denominator — the table just gives friendlier denominators.""",
        "Find $12\\frac{1}{2}$% of 960.",
        r"$12\frac{1}{2}\% = \frac{1}{8}$ → $\frac{960}{8} = 120$. No long multiplication anywhere.")
    S.pattern("pct-b2", "Recover the base, then apply another percentage", "very common",
        "'If 35% of a number is 189, find 80% of it' — a part is given, a different part is asked.",
        r"N = \frac{100k}{p}, \quad \text{then } q\% \text{ of } N = \frac{qk}{p}",
        r"""1. Recover the whole: $N = \frac{\text{part} \times 100}{p}$.
2. Take the asked percentage of N.
3. Shortcut: find 1% of N (k ÷ p) and scale — 1% × 80 gives 80% directly.

Why: both parts are fixed fractions of the same whole, so the whole unlocks every other part.""",
        "If 35% of a number is 189, what is 80% of that number?",
        r"$N = \frac{189 \times 100}{35} = 540$; $80\%$ of 540 $= 432$.")
    S.pattern("pct-b3", "Fraction ↔ percentage conversion", "very common",
        "'Express 5/16 as a percentage' or 'write 87.5% as a fraction' — pure conversion, both directions.",
        r"\frac{p}{q} \times 100\%, \qquad x\% = \frac{x}{100} = \text{reduce the fraction}",
        r"""1. Fraction → %: multiply by 100 (equivalently, scale the table value: 1/8 = 12.5% → 5/8 = 62.5%).
2. % → fraction: put x over 100, reduce. Use the table in reverse for standard values.
3. Decimals shift two places: 0.375 = 37.5%.

Why: 'per cent' is just a denominator of 100; conversion moves the number across that fixed denominator.""",
        "Express $\\frac{5}{16}$ as a percentage.",
        r"$\frac{5}{16} \times 100 = \frac{125}{4} = 31.25\%$ (1/16 is 6.25%, so 5 of them are 31.25%).")
    S.pattern("pct-b4", "One quantity as a percentage of another", "very common",
        "'45 is what per cent of 360?' / 'A's income is what % of B's?' — two quantities, the base named after 'of'.",
        r"\frac{\text{part}}{\text{base}} \times 100\%",
        r"""1. Identify the base (the value after 'of').
2. Divide the part by the base, multiply by 100.
3. Comparative version: 'A is x% and B is y% more than C' → A is $\frac{100 + x}{100 + y} \times 100\%$ of B.

Why: a percentage always needs a base; the question names it with 'of'.""",
        "Two numbers are respectively 20% and 50% more than a third number. The first number is what per cent of the second?",
        r"Let the third number be 100 → numbers 120 and 150. $\frac{120}{150} \times 100 = 80\%$.")

    assert 650 * 24 == 15600 * 100 // 100 and 650 * 0.24 == 156.0
    S.q("pct-b1", "easy", "What is 24% of 650?",
        ["156", "150", "162", "144"], "156",
        r"""$24\%$ of 650 $= \frac{24 \times 650}{100} = 156$.
Mentally: 10% of 650 = 65 → 24% = 2 × 65 + 4 × 6.5 = 130 + 26 = 156.""",
        None, 25)
    assert 960 / 8 == 120
    S.q("pct-b1", "easy", r"Find $12\frac{1}{2}\%$ of 960.",
        ["120", "116", "124", "128"], "120",
        r"""$12\frac{1}{2}\% = \frac{1}{8}$ → $\frac{960}{8} = 120$.""",
        None, 25)
    n = 189 * 100 // 35
    assert n == 540 and n * 0.8 == 432.0
    S.q("pct-b2", "medium",
        "If 35% of a number is 189, then 80% of that number is:",
        ["432", "426", "440", "420"], "432",
        r"""Number $= \frac{189 \times 100}{35} = 540$.
$80\%$ of 540 $= 432$.""",
        "1% of the number = 189/35 = 5.4 → 80% = 5.4 × 80 = 432.", 40)
    n = 72 * 100 // 15
    assert n == 480 and n * 0.45 == 216.0
    S.q("pct-b2", "medium",
        "If 15% of a number is 72, then 45% of the same number is:",
        ["216", "210", "220", "208"], "216",
        r"""Shortcut: $45\% = 3 \times 15\%$ → $3 \times 72 = 216$.
(Full method: number $= \frac{72 \times 100}{15} = 480$, then $45\%$ of 480 = 216.)""",
        None, 30)
    assert 5 / 16 * 100 == 31.25
    S.q("pct-b3", "easy", r"Expressed as a percentage, $\frac{5}{16}$ is equal to:",
        ["31.25%", "3.125%", "62.5%", "32.5%"], "31.25%",
        r"""$\frac{5}{16} \times 100 = \frac{125}{4} = 31.25\%$.
Table route: $\frac{1}{16} = 6.25\%$ → $5 \times 6.25\% = 31.25\%$.""",
        None, 30)
    S.q("pct-b3", "medium",
        r"When written as a fraction in lowest terms, 87.5% is equal to:",
        [r"$\frac{7}{8}$", r"$\frac{8}{7}$", r"$\frac{3}{8}$", r"$\frac{5}{8}$"], r"$\frac{7}{8}$",
        r"""$87.5\% = \frac{87.5}{100} = \frac{875}{1000} = \frac{7}{8}$.
Table route: $12.5\% = \frac{1}{8}$ and $87.5 = 7 \times 12.5$ → $\frac{7}{8}$.""",
        None, 35)
    assert 360 * 0.125 == 45.0
    S.q("pct-b4", "easy", "45 is what per cent of 360?",
        ["12.5%", "12%", "13.5%", "14%"], "12.5%",
        r"""$\frac{45}{360} \times 100 = \frac{100}{8} = 12.5\%$.""",
        None, 25)
    assert 9000 / 7200 * 100 == 125.0
    S.q("pct-b4", "easy",
        "A's monthly income is ₹9,000 and B's monthly income is ₹7,200. A's income is what per cent of B's income?",
        ["125%", "120%", "80%", "140%"], "125%",
        r"""$\frac{9000}{7200} \times 100 = 125\%$.
(The question compares A with B — B is the base. 80% would be B as a % of A.)""",
        None, 25)
    S.q("pct-b4", "medium",
        "Two numbers are respectively 20% and 50% more than a third number. The first number is what per cent of the second number?",
        ["80%", "75%", "85%", "70%"], "80%",
        r"""Let the third number be 100 → the numbers are 120 and 150.
$\frac{120}{150} \times 100 = 80\%$.""",
        "Setting the third number to 100 kills the algebra — always do this.", 40)
    assert 63 / 3 + 42 / 6 == 28.0
    S.q("pct-b1", "medium",
        r"Find the value of $33\frac{1}{3}\%$ of 63 $+$ $16\frac{2}{3}\%$ of 42.",
        ["28", "24", "30", "26"], "28",
        r"""$33\frac{1}{3}\% = \frac{1}{3}$ → $\frac{63}{3} = 21$.
$16\frac{2}{3}\% = \frac{1}{6}$ → $\frac{42}{6} = 7$. Total $= 28$.""",
        None, 35)
    return S


def build_change():
    S = Sub("pct-change")
    S.notes = r"""### Percentage change and its base
$$\%\ \text{change} = \frac{\text{final} - \text{initial}}{\text{initial}} \times 100$$
The denominator is the value **before** the change. ₹250 → ₹200 is a fall of $\frac{50}{250} = 20\%$; going back from ₹200 to ₹250 is a rise of $\frac{50}{200} = 25\%$. Same ₹50, different base, different percentage.

### The multiplier ("chip") idea — the master shortcut
Every change is a chip: $+20\% \to \times\frac{6}{5}$, $-25\% \to \times\frac{3}{4}$, $+8\% \to \times\frac{27}{25}$.
**Forward:** multiply the chips. **Backward:** divide by them.
Example: $+20\%$ then $-10\%$: $\frac{6}{5} \times \frac{9}{10} = \frac{27}{25}$ → net $+8\%$.
Example: two $-10\%$ steps leave 8100 → before: $8100 \times \frac{10}{9} \times \frac{10}{9} = 10000$.

### Two successive changes: $a + b + \frac{ab}{100}$
Keep the signs: $+30\%$ then $-20\%$: $30 - 20 - \frac{600}{100} = +4\%$. Both increases: $+15\%$ then $+12\%$: $15 + 12 + 1.8 = +28.8\%$.
Works only for exactly two changes; for three or more, chain the chips.

### The round-trip rule: $+x\%$ and $-x\%$ never cancel
Same size up then down (either order): net $= -\frac{x^2}{100}\%$.
$+20\%$ then $-20\%$: net $-4\%$. A fall of 25% then a rise of 25%: net $-6.25\%$. The percentage always lands a little **below** the start — remember this to kill "no change" options at sight.

### Numerator–denominator changes
If the numerator changes by $a\%$ and the denominator by $b\%$, the fraction's chip is $\frac{100 + a}{100 + b}$ (a ratio of chips):
numerator $+50\%$, denominator $-25\%$: $\frac{150}{100} \div \frac{75}{100} = 2$ → the fraction doubles ($+100\%$).

### Restoring the original value
To undo $+25\%$, **divide** by $\frac{5}{4}$ — do not apply $-25\%$. A salary of ₹50,000 after a 25% rise was $50000 \times \frac{4}{5} = ₹40{,}000$ before. Applying $-25\%$ gives 37,500 — the classic wrong answer.
Same for cuts: after a $12.5\%$ cut a price is ₹3,500 → original $= 3500 \div \frac{7}{8} = ₹4{,}000$.

### How the questions are dressed up
The same five ideas arrive as prices, salaries, output of a factory, exam scores, or the value of a share — the chips do not care about the story. Two changes in the wording ("and then", "subsequently", "after some months") always means successive; a single change with two numbers (from A to B) is a plain c1. The options are built from classic slips: wrong base in the change %, subtracting instead of dividing to undo, and "no change" for the round trip.

### Quick revision
- % change: base is the value before the change.
- Chips: multiply forward, divide backward.
- Two changes: $a + b + \frac{ab}{100}$ with signs.
- $+x\%$ and $-x\%$ in any order → net $-\frac{x^2}{100}\%$.
- Undo a change with the reciprocal chip, never the opposite percentage.
"""

    S.pattern("pct-c1", "Single percentage increase or decrease", "very common",
        "A value moves from A to B and the % change is asked — price, population, marks, anything.",
        r"\%\ \text{change} = \frac{\text{final} - \text{initial}}{\text{initial}} \times 100",
        r"""1. Compute the absolute change (final − initial).
2. Divide by the INITIAL value — the one before the change.
3. Multiply by 100; sign tells the direction.

Why: a percentage change always measures the movement against where the value started.""",
        "The salary of an employee rises from ₹18,000 to ₹20,700. Find the percentage increase.",
        r"Increase $= 2700$ on base 18000 → $\frac{2700}{18000} \times 100 = 15\%$.")
    S.pattern("pct-c2", "Two successive changes (net change)", "very common",
        "'Increased by a% and then decreased by b% — net change?' Often dressed as price, value or output.",
        r"a + b + \frac{ab}{100} \ \ (+\text{ increase},\ -\text{ decrease})",
        r"""1. Apply $a + b + \frac{ab}{100}$ with the signs of the two changes.
2. Or multiply the chips ($\frac{100+a}{100} \times \frac{100+b}{100}$) and read the net.
3. The chip method is safe for any number of changes.

Why: the second change acts on the changed value, and the $\frac{ab}{100}$ term is exactly that correction.""",
        "A number is increased by 15% and then decreased by 12%. The net change is:",
        r"$15 - 12 - \frac{15 \times 12}{100} = 3 - 1.8 = +3.2\%$. Chips: $\frac{23}{20} \times \frac{22}{25} = \frac{506}{500} = 1.012$.")
    S.pattern("pct-c3", "Same % up and down (round trip)", "very common",
        "'The price rises x% and then falls x%' (or falls then rises) — a guaranteed 'no change' trap among the options.",
        r"\text{net} = -\frac{x^2}{100}\%",
        r"""1. Write the net change as $-\frac{x^2}{100}\%$ — order does not matter.
2. Or verify with chips: $\frac{120}{100} \times \frac{80}{100} = \frac{24}{25} = 0.96$ → $-4\%$.
3. The final value is always BELOW the start (for any x > 0).

Why: the second change works on a bigger or smaller base, so the absolute swings differ.""",
        "The price of a commodity first rises by 20% and then falls by 20%. The net change in price is:",
        r"Net $= -\frac{20^2}{100} = -4\%$, a $4\%$ decrease. (Check: $100 \to 120 \to 96$.)")
    S.pattern("pct-c4", "Restore the original value (work backwards)", "very common",
        "The value AFTER the change(s) is given and the original is asked: 'after a 20% increase the population is 8,400…'.",
        r"\text{original} = \text{final} \div \text{(chip)} = \text{final} \times \frac{100}{100 + a}",
        r"""1. Write the chip of each change.
2. Divide the final value by the chips (or multiply by their reciprocals).
3. Never 'apply the opposite percentage' — that uses the wrong base.

Why: forward = multiply by chips, so backward = divide by the same chips.""",
        "After successive decreases of 10% and 20%, a number becomes 720. Find the number.",
        r"$N \times \frac{9}{10} \times \frac{4}{5} = 720$ → $N \times 0.72 = 720$ → $N = 1000$.")
    S.pattern("pct-c5", "Fraction changes: numerator and denominator move", "common",
        "'The numerator is increased by 20% and the denominator decreased by 10% — the fraction becomes?'",
        r"\text{new factor} = \frac{100 + a}{100 + b} \ \Rightarrow\ \%\ \text{change} = \frac{100 + a}{100 + b} - 1",
        r"""1. Write the chip of the numerator and of the denominator.
2. Divide the numerator chip by the denominator chip — that is the fraction's new factor.
3. Factor − 1 is the percentage change of the fraction.

Why: the fraction scales by (numerator chip)/(denominator chip), since denominator changes divide.""",
        r"The numerator of a fraction is increased by 50% and the denominator is decreased by 25%. The fraction becomes:",
        r"Chips: $\frac{3}{2}$ and $\frac{3}{4}$ → factor $= \frac{3}{2} \div \frac{3}{4} = 2$ → the fraction is doubled ($+100\%$).")

    assert (20700 - 18000) / 18000 * 100 == 15.0
    S.q("pct-c1", "easy",
        "The salary of an employee rises from ₹18,000 to ₹20,700 per month. The percentage increase in salary is:",
        ["15%", "12.5%", "16%", "18%"], "15%",
        r"""Increase $= 20700 - 18000 = 2700$ on the original ₹18,000.
$\frac{2700}{18000} \times 100 = 15\%$.""",
        None, 30)
    assert (800 - 720) / 800 * 100 == 10.0
    S.q("pct-c1", "easy",
        "The production of a factory falls from 800 units to 720 units. The percentage decrease is:",
        ["10%", "12%", "8%", "11%"], "10%",
        r"""Fall $= 80$ on the original 800 → $\frac{80}{800} \times 100 = 10\%$.""",
        None, 25)
    assert 1.25 * 0.8 == 1.0
    S.q("pct-c2", "easy",
        "A number is increased by 25% and then decreased by 20%. The net change in the number is:",
        ["No change", "5% increase", "5% decrease", "2.5% increase"], "No change",
        r"""$25 - 20 - \frac{25 \times 20}{100} = 5 - 5 = 0$.
Chips: $\frac{5}{4} \times \frac{4}{5} = 1$ → no change.""",
        None, 30)
    assert abs(1.15 * 0.88 - 1.012) < 1e-9
    S.q("pct-c2", "medium",
        "A number is increased by 15% and then decreased by 12%. The net percentage change is:",
        ["3.2% increase", "3% increase", "2.8% increase", "4.2% increase"], "3.2% increase",
        r"""$15 - 12 - \frac{15 \times 12}{100} = 3 - 1.8 = +3.2\%$.
Check with chips: $\frac{23}{20} \times \frac{22}{25} = \frac{506}{500} = 1.012$ ✓.""",
        None, 40)
    assert 1.2 * 0.8 == 0.96
    S.q("pct-c3", "easy",
        "The price of an article is first increased by 20% and then decreased by 20%. The net change in price is:",
        ["4% decrease", "No change", "4% increase", "2% decrease"], "4% decrease",
        r"""Net $= -\frac{20^2}{100} = -4\%$.
Check: ₹$100 \to 120 \to 96$.""",
        None, 25)
    assert 0.75 * 1.25 == 0.9375
    S.q("pct-c3", "medium",
        "The value of a share first falls by 25% and then rises by 25%. The net change in the value is:",
        ["6.25% decrease", "No change", "6.25% increase", "5% decrease"], "6.25% decrease",
        r"""Net $= -\frac{25^2}{100} = -6.25\%$ — order does not matter.
Check: ₹$100 \to 75 \to 93.75$.""",
        None, 35)
    assert 8400 * 100 // 120 == 7000
    S.q("pct-c4", "medium",
        "After an increase of 20%, the population of a town is 8,400. What was the population before the increase?",
        ["7,000", "6,720", "7,280", "7,200"], "7,000",
        r"""Population $\times \frac{120}{100} = 8400$ → population $= 8400 \times \frac{100}{120} = 7000$.""",
        "6,720 is 8,400 − 20% — applying the wrong base.", 35)
    assert 3500 * 1000 == 875 * 4000
    S.q("pct-c4", "medium",
        "After a reduction of 12.5% in its price, a gadget costs ₹3,500. What was its original price?",
        ["₹4,000", "₹3,937.50", "₹4,200", "₹3,850"], "₹4,000",
        r"""$12.5\% = \frac{1}{8}$ → present $= \frac{7}{8}$ of original.
Original $= 3500 \times \frac{8}{7} = ₹4{,}000$.""",
        "₹3,937.50 comes from adding 12.5% back — wrong base again.", 40)
    S.q("pct-c5", "medium",
        "The numerator of a fraction is increased by 50% and the denominator is decreased by 25%. As a result, the fraction:",
        ["increases by 100%", "increases by 75%", "increases by 50%", "increases by 25%"], "increases by 100%",
        r"""Numerator chip $\frac{3}{2}$, denominator chip $\frac{3}{4}$.
New factor $= \frac{3/2}{3/4} = 2$ → the fraction is doubled, i.e. a $100\%$ increase.""",
        None, 40)
    assert abs(0.9 / 0.8 - 1.125) < 1e-12
    S.q("pct-c5", "medium",
        "The numerator of a fraction is decreased by 10% and the denominator is decreased by 20%. The fraction becomes:",
        ["12.5% greater", "12.5% smaller", "10% greater", "30% smaller"], "12.5% greater",
        r"""Chips: $\frac{9}{10}$ and $\frac{8}{10}$ → factor $= \frac{9/10}{8/10} = \frac{9}{8} = 1.125$.
The fraction increases by $12.5\%$.""",
        None, 40)
    assert round(0.9 * 0.8, 10) == 0.72 and abs(720 / 0.72 - 1000) < 1e-9
    S.q("pct-c4", "hard",
        "A number, when successively decreased by 10% and 20%, becomes 720. The original number is:",
        ["1,000", "900", "960", "1,080"], "1,000",
        r"""$N \times \frac{9}{10} \times \frac{8}{10} = 720$ → $N \times 0.72 = 720$ → $N = 1000$.""",
        None, 45)
    assert abs(1.1 * 1.2 * 0.75 - 0.99) < 1e-12
    S.q("pct-c2", "hard",
        "A quantity is increased by 10%, then by 20%, and the result is decreased by 25%. The net change in the quantity is:",
        ["1% decrease", "No change", "1% increase", "5% decrease"], "1% decrease",
        r"""Chips: $\frac{11}{10} \times \frac{6}{5} \times \frac{3}{4} = \frac{198}{200} = 0.99$ → net $-1\%$.
(Take quantity 100: $100 \to 110 \to 132 \to 99$.)""",
        None, 50)
    return S
