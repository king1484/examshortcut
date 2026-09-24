"""Phase-2 deep content for quant/percentage — marks & income module."""
import os
import sys

sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
from _lib import Sub


def build_income():
    S = Sub("pct-marks-income")
    S.notes = r"""### Pass-marks problems
The pass mark is one fixed number seen from two candidates:
- A scores p% and **fails by** f marks → pass $= \frac{pM}{100} + f$.
- B scores q% and scores **e marks more than** the pass mark → pass $= \frac{qM}{100} - e$.
Equate the two: $\frac{(q - p)M}{100} = f + e$ → find M, then the pass mark.
Example: 33% fails by 45, 45% exceeds by 15 → 12% of M = 60 → M = 500, pass = 210.
Signs matter: fail-by pushes the pass mark **up** from the score, exceeds-by pulls it **down**.
Single-candidate version: if the pass mark is given directly, $\frac{pM}{100} + f = \text{pass}$ → M.

### Income–expenditure–savings bookkeeping
savings = income − expenditure. Set **income = 100** and all three numbers stay visible.
Example: spends 80% of income; income rises 15%, expenditure rises 10%:
$100/80/20 \to 115/88/27$ → savings rise $\frac{7}{20} \times 100 = 35\%$.
The percentage change in savings is almost never equal to the change in income — always recompute the new savings. If a person saves s% of income, expenditure is (100 − s)% of it.

### Price vs consumption
expenditure = price × quantity, so quantity chip = expenditure chip ÷ price chip.
- Price +25%, expenditure unchanged → quantity chip $= 1 \div \frac{5}{4} = \frac{4}{5}$ → cut 20%. (Standard formula: cut $= \frac{100r}{100 + r}\%$.)
- Price +20%, expenditure allowed to rise 8% → chip $= \frac{108}{120} = 0.9$ → cut 10%.
- Price +40%, consumption cut 25% → expenditure chip $= 1.4 \times 0.75 = 1.05$ → +5%.
Never equate the consumption cut to the price rise — they are related by division, not equality.

### Price cut with extra quantity
A price cut of r% on an outlay M saves r% of M; the saving buys the **extra** quantity at the reduced price.
reduced price = (r% of M) ÷ extra quantity → original price = reduced ÷ (1 − r/100).
Example: a 20% cut lets a family buy 5 kg more for ₹400 → saved = ₹80 → reduced price = 16/kg → original $= 16 \times \frac{5}{4} = ₹20$.

### Exam traps
- Fail-by and exceed-by act in opposite directions (+f, −e); a same-sign slip ruins M.
- Savings % change ≠ income % change; compute the new savings from scratch.
- Consumption cut ≠ price rise (20% ≠ 25%): divide the chips.
- Depreciation/price-cut chains: work in chips, not in added percentages.

### Quick revision
- $\frac{(q - p)M}{100} = f + e$ for two candidates.
- Income = 100 bookkeeping solves every savings question.
- Quantity chip = expenditure chip ÷ price chip.
- An r% cut saves r% of the outlay → extra quantity at the reduced price.
"""

    S.pattern("pct-i1", "Pass marks with two candidates", "very common",
        "'A candidate scoring p% fails by f marks; another scoring q% gets e marks more than the pass mark.'",
        r"\frac{(q - p)M}{100} = f + e \ \Rightarrow\ M = \frac{100(f + e)}{q - p}",
        r"""1. Write pass mark from each candidate: pM/100 + f and qM/100 − e.
2. Equate → (q − p)% of M = f + e → maximum marks M.
3. Pass mark = pM/100 + f (verify with the second candidate).

Why: both expressions equal the same pass mark; subtracting them cancels it and leaves M.""",
        "A candidate scoring 33% fails by 45 marks, while another scoring 45% gets 15 marks more than the pass marks. Find the maximum marks.",
        r"$12\%$ of M $= 45 + 15 = 60$ → M $= 500$; pass mark $= 165 + 45 = 210$.")
    S.pattern("pct-i2", "Income–expenditure–savings change", "very common",
        "'He spends 80% of his income; income rises a% and expenditure rises b% — % change in savings?'",
        r"\text{savings} = \text{income} - \text{expenditure}, \ \text{track with income} = 100",
        r"""1. Set income = 100; write expenditure and savings.
2. Apply the two % changes to income and expenditure separately.
3. New savings = new income − new expenditure; % change on the old savings.

Why: savings is a leftover, not a base — its % change must be computed, never guessed.""",
        "A person spends 80% of his income. His income increases by 15% and his expenditure increases by 10%. The percentage increase in his savings is:",
        r"Income 100/80/20 → 115/88/27 → savings rise $\frac{7}{20} \times 100 = 35\%$.")
    S.pattern("pct-i3", "Price rise vs consumption (expenditure target)", "very common",
        "'The price rises by r% — by what % must consumption be cut so the expenditure stays the same?' (Or the expenditure is allowed to move by s%.)",
        r"\text{cut}\% = \frac{100r}{100 + r}\%, \qquad \text{quantity chip} = \frac{\text{expenditure chip}}{\text{price chip}}",
        r"""1. Write chips: price $\frac{100 + r}{100}$, expenditure $\frac{100 + s}{100}$ (s = 0 for 'same').
2. Quantity chip = expenditure chip ÷ price chip.
3. 1 − quantity chip is the cut.

Why: expenditure = price × quantity, so quantity adjusts by the ratio of the other two chips.""",
        "The price of petrol rises by 25%. By what per cent must a family reduce its consumption so that the expenditure on petrol remains the same?",
        r"Quantity chip $= 1 \div \frac{5}{4} = \frac{4}{5}$ → cut $= 20\%$ ($= \frac{100 \times 25}{125}$).")
    S.pattern("pct-i4", "Price cut → extra quantity for the same money", "common",
        "'A reduction of r% in the price enables a family to buy k kg more for ₹M — find the (original/reduced) price.'",
        r"\text{reduced price} = \frac{r\% \text{ of } M}{k}, \qquad \text{original} = \frac{\text{reduced}}{1 - r/100}",
        r"""1. The r% cut saves r% of M — that saving is spent on the extra k units.
2. Reduced price = saving ÷ k.
3. Original price = reduced price ÷ (1 − r/100).

Why: the outlay is unchanged, so the money freed by the cut is exactly what buys the extra quantity.""",
        "A reduction of 20% in the price of cooking oil enables a family to buy 5 kg more for ₹400. The original price per kg is:",
        r"Saving = 20% of 400 = ₹80 → reduced price $= \frac{80}{5} = ₹16$ → original $= 16 \times \frac{5}{4} = ₹20$.")

    assert 0.5 * 500 == 250 and 0.4 * 500 == 200
    S.q("pct-i1", "medium",
        "In an examination, a candidate scoring 40% of the maximum marks fails by 20 marks, while another candidate scoring 50% gets 30 marks more than the pass marks. The maximum marks are:",
        ["500", "450", "550", "600"], "500",
        r"""Pass mark from A: $0.40M + 20$; from B: $0.50M - 30$.
$10\%$ of M $= 50$ → M $= 500$. Pass mark $= 220$ (both agree).""",
        None, 40)
    M = round((175 - 25) / 0.30)  # 30% of M = 150 -> M = 500
    assert M == 500 and round(0.30 * M, 6) + 25 == 175
    S.q("pct-i1", "medium",
        "In an examination, a candidate scoring 30% of the maximum marks fails by 25 marks. If the pass mark is 175, the maximum marks are:",
        ["500", "450", "520", "600"], "500",
        r"""$0.30M + 25 = 175$ → $0.30M = 150$ → M $= 500$.""",
        None, 35)
    assert (115 - 88 - 20) / 20 * 100 == 35.0  # savings 20 -> 27
    S.q("pct-i2", "medium",
        "A person spends 80% of his income. His income increases by 15% and his expenditure increases by 10%. His savings increase by:",
        ["35%", "45%", "40%", "55%"], "35%",
        r"""Income = 100 → spends 80, saves 20.
New: income 115, expenditure 88 → savings 27.
Increase $= \frac{7}{20} \times 100 = 35\%$.""",
        None, 40)
    assert (130 - 90 - 25) / 25 * 100 == 60.0  # savings 25 -> 40
    S.q("pct-i2", "medium",
        "Ravi saves 25% of his income. His income rises by 30% and his expenditure rises by 20%. His new savings are what per cent more than his earlier savings?",
        ["60%", "50%", "55%", "65%"], "60%",
        r"""Income = 100 → saves 25, spends 75.
New: income 130, expenditure 90 → savings 40.
Increase $= \frac{15}{25} \times 100 = 60\%$.""",
        None, 40)
    assert 100 * 25 // 125 == 20
    S.q("pct-i3", "easy",
        "The price of petrol rises by 25%. By what per cent must a motorist reduce his consumption so that his expenditure on petrol remains the same?",
        ["20%", "25%", "15%", "30%"], "20%",
        r"""Cut $= \frac{100 \times 25}{100 + 25} = \frac{2500}{125} = 20\%$.
Chip check: $\frac{5}{4} \times \frac{4}{5} = 1$ ✓.""",
        None, 30)
    assert abs(1.4 * 0.75 - 1.05) < 1e-9
    S.q("pct-i3", "medium",
        "The price of an item increases by 40% and a family cuts its consumption by 25%. The family's expenditure on the item:",
        ["increases by 5%", "decreases by 5%", "remains unchanged", "increases by 15%"], "increases by 5%",
        r"""Chip: $1.40 \times 0.75 = 1.05$ → expenditure increases by 5%.""",
        None, 35)
    p = 1200 * 20 / 100 / 6
    assert p == 40.0 and p / 0.8 == 50.0
    S.q("pct-i4", "hard",
        "A reduction of 20% in the price of cooking oil enables a family to buy 6 kg more for ₹1,200. The original price per kg of oil was:",
        ["₹50", "₹48", "₹45", "₹55"], "₹50",
        r"""Saving = 20% of 1200 = ₹240 → reduced price $= \frac{240}{6} = ₹40$/kg.
Original $= 40 \times \frac{100}{80} = ₹50$/kg.""",
        None, 50)
    rp = 2880 * 10 / 100 / 8
    assert rp == 36.0 and rp / 0.9 == 40.0
    S.q("pct-i4", "hard",
        "With a 10% fall in the price of rice, a family can buy 8 kg more rice for ₹2,880. The reduced price of rice per kg is:",
        ["₹36", "₹40", "₹32", "₹45"], "₹36",
        r"""Saving = 10% of 2880 = ₹288 → reduced price $= \frac{288}{8} = ₹36$/kg.
(Original price $= 36 \times \frac{100}{90} = ₹40$.)""",
        None, 50)
    return S
