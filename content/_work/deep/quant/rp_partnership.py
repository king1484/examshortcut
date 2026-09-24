"""Phase-2 deep content for quant/ratio-proportion — partnership module."""
import os
import sys

sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
from _lib import Sub


def build_partnership():
    S = Sub("rp-partnership")
    S.notes = r"""### One rule runs the whole subtopic
Profit is divided in the ratio of **capital × time** (capital-months). Same period → the time cancels and only the capital ratio matters. Different joining dates, withdrawals or top-ups → build one row per partner:
$$\text{share}_i \propto C_1t_1 + C_2t_2 + \cdots$$
Then each partner's money = fraction × profit. Nothing else exists in this topic.

### The capital-months table
| Partner | Working |
|---|---|
| A: ₹12,000 for 12 months | $12000 \times 12 = 144000$ |
| B: ₹18,000 for 8 months (joined after 4) | $18000 \times 8 = 144000$ |
Ratio 144 : 144 = 1 : 1. Months for a late joiner run from the JOINING month to the end of the year, never from the start.

### Mid-year capital changes
Split the year into stretches and add capital × months across them: A holds ₹30,000 for 8 months, then ₹20,000 for 4 → $30000 \times 8 + 20000 \times 4 = 320000$ capital-months. Using only the final capital (or only the first) is the classic error.
The inverse question appears too: "they share profits equally, B joined after 6 months — find B's capital": equate the capital-month products.

### Working partners
A partner who works takes a **salary/fee/commission out of the profit first**; only the residue is divided by capital-months (which still include the working partner's own capital-months).
Example: profit ₹9,000; B manages and draws 10% → cut ₹900 → residue ₹8,100 split by capitals. The cut percentage applies to the whole profit, not to the residue.

### Comparing two claims
"Who got more?" and "difference between shares" need only the capital-month ratio: difference = gap parts × value of one part. Reduce the capital-month numbers by their GCD early — the arithmetic stays tiny (₹'000 units help).

### How the questions vary the story
Same capital-months engine, four costumes:
- **Rent of a pasture:** grazers pay in ratio of (animals × months) — cows are the "capital".
- **Wages of a contractor:** workers' wages split by (men × days) — identical arithmetic.
- **Consumption of a granary:** provisions last longer or shorter as (men × days) changes — the inverse uses the same product.
- **Sleeping vs working partner:** the sleeping partner invests only; the working one takes the fee — combine patterns rp-n4 with any of the above.

### Unit discipline
Drop the zeroes early: 12,000 × 12 = 144 'thousand-months' — write 144, not 144000. Ratios are what survive, and every zero you cancel is one less chance of an arithmetic slip. If the products look unwieldy, divide all of them by 1000 (or 10000) before forming the ratio; the ratio is unchanged.

### Quick revision
- Share ∝ capital × months. Same period → capital ratio.
- Late joiner: months from joining to year-end.
- Capital change: add capital × months per stretch.
- Working partner: cut from the top, share the residue.
"""

    S.pattern("rp-n1", "Simple partnership (same time, different capitals)", "very common",
        "Partners invest different amounts for the same period; profit share or total profit asked.",
        r"P_1 : P_2 = C_1 : C_2 \quad (\text{same time})",
        r"""1. Reduce the capital ratio to small terms (divide by the GCD).
2. Add the parts; one part = profit ÷ total parts.
3. Multiply by the asked partner's parts.

Why: with time equal for everyone, it cancels out of the ratio.""",
        "A and B invest ₹45,000 and ₹35,000 for one year. From a profit of ₹8,000, what does A receive?",
        r"Ratio $45000 : 35000 = 9 : 7$ (16 parts) → A $= \frac{9}{16} \times 8000 = ₹4{,}500$.")
    S.pattern("rp-n2", "Partner joins late / leaves early (capital × time)", "very common",
        "'A starts the business; B joins after k months' — time differs, so capitals alone mislead.",
        r"P_1 : P_2 = C_1T_1 : C_2T_2",
        r"""1. Compute capital-months: investment × months in business (joiner: from joining month to year-end).
2. The profit ratio is the ratio of these products.
3. Reverse version: ratio known, one capital unknown → equate the products.

Why: money working for longer deserves a proportionally larger share — only the product counts.""",
        "A starts a business with ₹16,000. After 6 months, B joins with ₹24,000. From a year-end profit of ₹14,000, B's share is:",
        r"A: $16000 \times 12 = 192000$; B: $24000 \times 6 = 144000$ → ratio 4 : 3 → B $= \frac{3}{7} \times 14000 = ₹6{,}000$.")
    S.pattern("rp-n3", "Mid-year capital change", "common",
        "'A invests X and adds/withdraws Y after k months' — or 'invested a for 4 months and b for the rest'.",
        r"\text{effective} = C_a t_1 + C_b t_2 + \cdots",
        r"""1. Split the year at every change.
2. Add capital × months over the stretches.
3. Take the ratio across partners; a single partner with changes just sums their own stretches.

Why: each stretch of capital earns its own capital-months, and they add up.""",
        "A invests ₹15,000 for the first 4 months of a year and ₹20,000 for the remaining 8 months. B invests ₹18,000 for the whole year. The profit-sharing ratio is:",
        r"A: $15000 \times 4 + 20000 \times 8 = 220000$; B: $18000 \times 12 = 216000$ → $55 : 54$.")
    S.pattern("rp-n4", "Working partner (salary / commission off the top)", "common",
        "'B manages the business and gets x% of the profit' — or a fixed salary — before the rest is shared.",
        r"\text{residue} = \text{profit} - \text{cut}, \quad \text{residue split by } C_iT_i",
        r"""1. Take the working partner's cut out of the profit FIRST.
2. Divide the residue by the capital-month ratio (the working partner's capital still counts).
3. Add the cut back to that partner's receipt if the total payment is asked.

Why: the fee is for work done, so it must not be distorted by the profit ratio.""",
        "A and B invest ₹50,000 and ₹30,000. A manages the business and receives 10% of the profit for it. From a profit of ₹14,400, B's share is:",
        r"Cut $= ₹1{,}440$ → residue $= ₹12{,}960$; ratio $5 : 3$ → B $= \frac{3}{8} \times 12960 = ₹4{,}860$.")

    assert 8000 // 16 == 500 and 9 * 500 == 4500
    S.q("rp-n1", "easy",
        "A and B invest ₹45,000 and ₹35,000 in a business for one year. Out of a profit of ₹8,000, A's share is:",
        ["₹4,500", "₹3,500", "₹4,800", "₹4,200"], "₹4,500",
        r"""Ratio $= 45000 : 35000 = 9 : 7$ → 16 parts.
A $= \frac{9}{16} \times 8000 = ₹4{,}500$.""",
        None, 30)
    assert 9000 // 10 == 900 and 3 * 900 == 2700
    S.q("rp-n1", "easy",
        "A, B and C invest ₹20,000, ₹30,000 and ₹50,000 respectively in a business. Out of a profit of ₹9,000, B's share is:",
        ["₹2,700", "₹2,400", "₹3,000", "₹1,800"], "₹2,700",
        r"""Ratio $= 2 : 3 : 5$ (10 parts) → 1 part $= ₹900$.
B $= 3 \times 900 = ₹2{,}700$.""",
        None, 30)
    assert 16000 * 12 == 192000 and 24000 * 6 == 144000 and 14000 // 7 == 2000
    S.q("rp-n2", "medium",
        "A starts a business with ₹16,000. After 6 months, B joins with ₹24,000. Out of a total profit of ₹14,000 at the end of the year, B's share is:",
        ["₹6,000", "₹8,000", "₹7,000", "₹5,600"], "₹6,000",
        r"""A: $16000 \times 12 = 192000$; B: $24000 \times 6 = 144000$.
Ratio $= 192 : 144 = 4 : 3$ → B $= \frac{3}{7} \times 14000 = ₹6{,}000$.""",
        None, 40)
    assert 9000 * 12 == 18000 * 6
    S.q("rp-n2", "medium",
        "A invests ₹9,000 for the whole year. B joins after 6 months, and at the end of the year they share the profit equally. B's investment is:",
        ["₹18,000", "₹9,000", "₹12,000", "₹24,000"], "₹18,000",
        r"""Equal shares → equal capital-months: $9000 \times 12 = C \times 6$ → C $= ₹18{,}000$.""",
        None, 40)
    assert 30000 * 8 + 20000 * 4 == 320000 and 20000 * 12 == 240000
    S.q("rp-n3", "medium",
        "A starts a business with ₹30,000 and withdraws ₹10,000 after 8 months. B invests ₹20,000 for the whole year. The profit-sharing ratio is:",
        ["4 : 3", "3 : 2", "2 : 1", "5 : 3"], "4 : 3",
        r"""A: $30000 \times 8 + 20000 \times 4 = 320000$; B: $20000 \times 12 = 240000$.
Ratio $= 320 : 240 = 4 : 3$.""",
        None, 45)
    total = 25000 * 12 + 30000 * 9 + 40000 * 6
    assert total == 300000 + 270000 + 240000
    from math import gcd
    g = gcd(gcd(300000, 270000), 240000)
    assert (300000 // g, 270000 // g, 240000 // g) == (10, 9, 8) and 33750 // 27 == 1250
    S.q("rp-n2", "hard",
        "A starts a business with ₹25,000. After 3 months B joins with ₹30,000, and after another 3 months C joins with ₹40,000. Out of a year-end profit of ₹33,750, C's share is:",
        ["₹10,000", "₹9,000", "₹11,250", "₹12,500"], "₹10,000",
        r"""A: $25000 \times 12 = 300000$; B: $30000 \times 9 = 270000$; C: $40000 \times 6 = 240000$.
Ratio $= 300 : 270 : 240 = 10 : 9 : 8$ (27 parts) → C $= \frac{8}{27} \times 33750 = ₹10{,}000$.""",
        None, 55)
    assert 28000 * 125 == 3500 * 1000 and 24500 // 5 == 4900 and 3 * 4900 + 3500 == 18200
    S.q("rp-n4", "medium",
        "A and B invest ₹36,000 and ₹24,000 in a business. A, the working partner, receives 12.5% of the profit for managing it. On an annual profit of ₹28,000, A receives in all:",
        ["₹18,200", "₹16,800", "₹17,500", "₹19,000"], "₹18,200",
        r"""Cut $= 12.5\%$ of 28000 $= ₹3{,}500$ → residue $= ₹24{,}500$.
Capital ratio $= 3 : 2$ → A $= \frac{3}{5} \times 24500 = ₹14{,}700$; total $= 14700 + 3500 = ₹18{,}200$.""",
        None, 50)
    assert 12960 % 8 == 0 and 3 * 1620 == 4860
    S.q("rp-n4", "hard",
        "A invests ₹50,000 and B ₹30,000 in a business. A manages it and receives 10% of the profit for management. Out of a profit of ₹14,400, B's share is:",
        ["₹4,860", "₹5,400", "₹4,320", "₹4,680"], "₹4,860",
        r"""Cut $= ₹1{,}440$ → residue $= ₹12{,}960$; ratio $= 50000 : 30000 = 5 : 3$.
B $= \frac{3}{8} \times 12960 = ₹4{,}860$.""",
        None, 55)
    assert 15000 * 4 + 20000 * 8 == 220000 and 18000 * 12 == 216000
    S.q("rp-n3", "hard",
        "A invests ₹15,000 for the first 4 months of a year and ₹20,000 for the remaining 8 months. B invests ₹18,000 for the whole year. The ratio in which they share the profit is:",
        ["55 : 54", "25 : 24", "4 : 5", "55 : 53"], "55 : 54",
        r"""A: $15000 \times 4 + 20000 \times 8 = 220000$; B: $18000 \times 12 = 216000$.
Ratio $= 220 : 216 = 55 : 54$.""",
        None, 50)
    return S
