"""Phase-2 deep content for quant/percentage — population & election module."""
import os
import sys

sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
from _lib import Sub


def build_population():
    S = Sub("pct-population-election")
    S.notes = r"""### Growth and depreciation over years
Value after n years at r% per annum: $P\left(1 \pm \frac{r}{100}\right)^n$ — plus for growth, minus for depreciation.
Different rates in different years: multiply the chips one after another; never average the rates.
Example: 40,000 → +10% then −5%: $40000 \times \frac{11}{10} \times \frac{19}{20} = 41{,}800$.
Handy exact chips: 10% → $\frac{11}{10}$ or $\frac{9}{10}$; 20% → $\frac{6}{5}$; 25% → $\frac{5}{4}$; 5% → $\frac{21}{20}$; 12.5% → $\frac{9}{8}$ or $\frac{7}{8}$.

### Backwards questions (present given, past asked)
Present = P × chip¹ × chip² …, so divide by the chips to go back.
Example: a machine is worth ₹8,100 after two yearly depreciations of 10%: $8100 \div \frac{9}{10} \div \frac{9}{10} = ₹10{,}000$.
Do **not** divide by the net change (1 − 20% ≠ 0.9 × 0.9 = 0.81).

### Watch the walk-through with P = 100
For any multi-year story, take the starting value as 100 and track it year by year:
+10% then −5% then +20%: $100 \to 110 \to 104.5 \to 125.4$ — the final value is 125.4% of the start, a net +25.4%.
This kills every option at a glance and needs no formula at all. When the answer choices are far apart (they usually are), even rough chips decide the question: "is it above or below 41,000?" is enough.

### Elections — the two golden rules
1. Every candidate's share is a percentage of the **valid** votes, never of the total polled.
2. Margin = (winner% − loser%) × valid votes.
With invalid votes, chain once more: valid = (100 − invalid%) of the polled.
Example: 20% of the polled votes are invalid, the winner polls 60% of the valid votes and wins by 1,200 → margin = 20% of valid → valid = 6,000 = 80% of polled → polled = 7,500.

### One-candidate and turnout variants
- "x% did not vote / their votes were invalid" → handle the turnout first, then split the rest.
- A candidate who withdraws: subtract that share before splitting between the remaining two.
- "Winner got 55% of the total votes (no invalid votes)": margin = (2 × 55 − 100)% = 10% of the votes.

### Depreciation nuance
"Depreciates 10% p.a. for 2 years" is $\left(\frac{9}{10}\right)^2 = 0.81$ — a total fall of **19%**, not 20%. The "20%" option is always planted.

### Elections — one more worked shape
"A candidate got 30% of the total valid votes and lost by 4,000": the winner has 70%, so the margin is 40% of the valid votes → valid $= \frac{4000 \times 100}{40} = 10{,}000$ and the loser's votes $= 3{,}000$. Everything again reduces to one equation on valid votes. If the question instead names "total voters on the roll" with a turnout of 80%, the valid votes sit inside the turnout: roll → turnout → valid → shares, left to right, one chip each.

### Quick revision
- $P_n = P \times \text{chip}^n$; chips multiply; go back by dividing.
- Different rates → different chips, applied in order.
- Elections: everything sits on valid votes; margin = share gap × valid.
- $\left(1 - \frac{r}{100}\right)^2 \ne 1 - \frac{2r}{100}$.
"""

    S.pattern("pct-p1", "Population growth over n years", "very common",
        "'A town's population is P and increases at r% per annum — population after n years?'",
        r"P_n = P\left(1 + \frac{r}{100}\right)^n",
        r"""1. Write the chip $\frac{100 + r}{100}$.
2. Multiply P by chipⁿ (or apply chip n times).
3. Two different rates in two years → multiply the two different chips.

Why: each year's growth sits on the grown value, so the changes compound multiplicatively.""",
        "The population of a town is 6,400 and increases at 25% per annum. What will it be after 2 years?",
        r"Chip $\frac{5}{4}$ → $6400 \times \frac{25}{16} = 10{,}000$. (64 hundred → 100 hundred.)")
    S.pattern("pct-p2", "Backwards: present value → past value / depreciation", "very common",
        "'The present population is X; it grew at r% p.a. — find the population n years ago' or 'a machine worth M depreciates at r% p.a. — value after n years'.",
        r"\text{past} = \text{present} \div \left(1 + \frac{r}{100}\right)^n, \qquad \text{value after n yrs} = P\left(1 - \frac{r}{100}\right)^n",
        r"""1. Forward: multiply by the depreciation chipⁿ.
2. Backward: divide the present value by the growth chipⁿ — never divide by the net %.
3. Check the answer by growing it forward once.

Why: compounding is not symmetric — undo a 25% rise with ÷(5/4), not with −25%.""",
        "The present population of a town is 16,000. If it has been growing at 25% per annum, what was its population 2 years ago?",
        r"Past $= \frac{16000}{(5/4)^2} = 16000 \times \frac{16}{25} = 10{,}240$.")
    S.pattern("pct-p3", "Two different rates in consecutive years", "common",
        "'Increases by 10% in the first year and decreases by 5% in the second' — rates differ or a sign flips.",
        r"P_n = P \times \text{chip}_1 \times \text{chip}_2 \times \cdots",
        r"""1. One chip per year, signs included: +5% → 21/20, −10% → 9/10.
2. Multiply the chips in order (or take P = 100 and walk through).
3. For 'what was it 3 years ago', divide by all three chips.

Why: each year's rate applies to the value left by the previous year.""",
        "The population of a town is 80,000. It increases by 5% in the first year and decreases by 10% in the second year. What is the population at the end of the second year?",
        r"$80000 \times \frac{21}{20} \times \frac{9}{10} = 75{,}600$. (Averaging +5 and −10 = −5% gives 76,000 — wrong.)")
    S.pattern("pct-p4", "Election with valid/invalid votes and margin", "very common",
        "'In an election, x% of the votes were invalid; the winner got y% of the valid votes and won by M votes.'",
        r"\text{margin} = \frac{W - L}{100} \times \text{valid votes}, \quad \text{valid} = \frac{100 - \text{invalid}}{100} \times \text{polled}",
        r"""1. Chain: polled → valid (drop the invalid %) → shares of the winner and loser.
2. Margin = share gap × valid votes; equate it to the given margin.
3. Two candidates: L = 100 − W (on valid votes).

Why: candidates' percentages are defined on valid votes, so every equation must sit on that base.""",
        "In an election between two candidates, 20% of the votes polled were invalid. The winner got 60% of the valid votes and won by 1,200 votes. How many votes were polled in all?",
        r"Valid = 0.8 × polled; margin = 20% of valid = 1200 → valid = 6000 → polled = $\frac{6000}{0.8} = 7{,}500$.")

    assert 50000 * 1.21 == 60500.0
    S.q("pct-p1", "easy",
        "The population of a town is 50,000 and it increases by 10% per annum. What will be its population after 2 years?",
        ["60,500", "60,000", "61,000", "62,500"], "60,500",
        r"""$50000 \times \frac{11}{10} \times \frac{11}{10} = 50000 \times 1.21 = 60{,}500$.""",
        "60,000 comes from adding 10 + 10 = 20% — growth compounds.", 30)
    assert 6400 * 1.5625 == 10000.0
    S.q("pct-p1", "medium",
        "The population of a village is 6,400 and it increases at 25% per annum. Its population after 2 years will be:",
        ["10,000", "9,600", "10,400", "12,500"], "10,000",
        r"""$6400 \times \frac{5}{4} \times \frac{5}{4} = 6400 \times \frac{25}{16} = 10{,}000$.""",
        None, 35)
    assert 12500 * 0.81 == 10125.0
    S.q("pct-p2", "easy",
        "A machine costing ₹12,500 depreciates at 10% per annum. Its value after 2 years is:",
        ["₹10,125", "₹10,000", "₹10,250", "₹11,000"], "₹10,125",
        r"""$12500 \times \frac{9}{10} \times \frac{9}{10} = 12500 \times 0.81 = ₹10{,}125$.""",
        "₹10,000 assumes a 20% total fall — the two years lose only 19%.", 30)
    assert 16000 == 10240 * 1.5625
    S.q("pct-p2", "medium",
        "The present population of a town is 16,000. If it has been increasing at 25% per annum, its population 2 years ago was:",
        ["10,240", "10,400", "10,000", "12,000"], "10,240",
        r"""Past $= \frac{16000}{(5/4)^2} = 16000 \times \frac{16}{25} = 10{,}240$.""",
        None, 40)
    assert 80000 * 1.05 * 0.9 == 75600.0
    S.q("pct-p3", "medium",
        "The population of a town is 80,000. It increases by 5% in the first year and decreases by 10% in the second year. The population at the end of the second year is:",
        ["75,600", "76,000", "75,000", "76,400"], "75,600",
        r"""$80000 \times \frac{21}{20} \times \frac{9}{10} = 84000 \times 0.9 = 75{,}600$.""",
        None, 40)
    assert abs(20000 * 1.2 * 1.15 * 0.9 - 24840) < 1e-6
    S.q("pct-p3", "hard",
        "A factory's output rose by 20% in the first year and 15% in the second year, then fell by 10% in the third year to 24,840 units. The output 3 years ago was:",
        ["20,000", "20,500", "19,800", "21,000"], "20,000",
        r"""$O \times 1.2 \times 1.15 \times 0.9 = 24840$ → $O \times 1.242 = 24840$ → $O = 20{,}000$.""",
        None, 55)
    assert 96000 * 1.25 * 0.8 == 96000.0
    S.q("pct-p3", "medium",
        "The population of a town is 96,000. It increases by 25% in the first year and decreases by 20% in the second year. The population at the end of the second year is:",
        ["96,000", "97,000", "95,000", "1,00,000"], "96,000",
        r"""$96000 \times \frac{5}{4} \times \frac{4}{5} = 96{,}000$ — the chips are reciprocals, so the town is back where it started.""",
        None, 40)
    assert 2700 * 100 == 27000 * 10
    S.q("pct-p4", "medium",
        "In an election between two candidates, the winner got 55% of the valid votes and won by 2,700 votes. The number of valid votes polled was:",
        ["27,000", "25,000", "30,000", "22,000"], "27,000",
        r"""Shares: 55% vs 45% → margin = 10% of valid votes.
$0.10 \times V = 2700$ → V = 27,000.""",
        None, 40)
    assert 0.85 * 12000 == 10200 and 10200 * 0.2 == 2040
    S.q("pct-p4", "hard",
        "In an election between two candidates, 15% of the total votes polled were invalid. The winner got 60% of the valid votes and won by 2,040 votes. The total number of votes polled was:",
        ["12,000", "11,500", "12,500", "13,000"], "12,000",
        r"""Valid = 85% of polled. Winner 60%, loser 40% → margin = 20% of valid.
Valid $= \frac{2040}{0.20} = 10{,}200$ → polled $= \frac{10200}{0.85} = 12{,}000$.""",
        None, 55)
    return S
