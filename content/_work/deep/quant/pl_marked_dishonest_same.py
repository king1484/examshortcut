"""Phase-2 deep content for quant/profit-loss-discount — marked-price, dishonest, same-SP modules."""
import os
import sys
from fractions import Fraction as F

sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
from _lib import Sub, num, rs, mixed


def P(x):
    x = F(x)
    return (num(x) if x.denominator in (1, 2, 4, 5, 8, 10, 16, 20, 25, 40, 50, 100) else mixed(x)) + "%"


def build_marked():
    S = Sub("pl-marked-discount")
    S.notes = r"""### The full chain: CP → MP → SP
A shopkeeper does not sell at cost. He writes a higher price on the label — the **marked price (MP)**, also called the list price or tag price — and then offers a **discount** on it.
$$\text{Discount} = MP - SP, \qquad \text{Discount\% is always calculated on MP}$$
Buying at ₹800, tagging ₹1,000 and selling at ₹900: discount ₹100 = 10% of MP; profit ₹100 = 12.5% of CP. The discount is never a percentage of CP.

### The master relation
$$MP = CP \times \frac{100 + g}{100 - d}$$
where g is the final gain% and d the discount%. Any one of markup, discount, gain fixes the other two. Marked 40% above CP with a 10% discount: $1.4 \times 0.9 = 1.26$ → profit 26%.

### One-step and two-step versions
- "What should the markup be to allow 10% discount and still gain 17%?" → $\frac{117}{90} = 1.3$ → mark 30% above CP.
- Marked ₹1,200, sold at 15% off → SP $= ₹1{,}020$, discount $= ₹180 = 15\%$ of MP.
- Find the gain: marked 25% above CP, discount 10% → $1.25 \times 0.9 = 1.125$ → gain 12.5%.

### Working backwards
MP ₹1,500 sold for ₹1,275 → discount 15%. If that left a gain of g%, build CP by dividing the SP by the gain chip: SP ₹1,275 at 15% discount and 25% profit → CP $= 1275 \div 1.25 = ₹1{,}020$. Exam numbers are always chosen to come out whole — if yours do not, re-read the question.

### Multi-level trade chains
Manufacturer → wholesaler → retailer → customer: each stage multiplies its own chip.
Cost ₹4,000, then +25%, +20%, +10%: $4000 \times 1.25 \times 1.2 \times 1.1 = ₹6{,}600$.
Each trader's profit is on HIS own purchase price, not on the original cost. Working backwards, divide by the chips in reverse order.

### Discount schemes
- Flat d% is one step × $\frac{100-d}{100}$.
- "Buy 5 get 1 free" → pay for 5, receive 6 → discount $= \frac{1}{6} = 16\frac{2}{3}\%$.
- "Buy 19 get 1 free" → $\frac{1}{20} = 5\%$ — the free item counts against what you RECEIVE, not what you pay for.
- A flat discount always beats successive discounts of the same total: 40% flat leaves 0.60, while 30% + 10% leaves $0.7 \times 0.9 = 0.63$.

### Common traps
- Taking discount% on CP or SP instead of MP.
- Subtracting the discount from the markup (40% up − 10% down is 26% up, not 30%: $1.4 \times 0.9 = 1.26$).
- In a chain, applying every markup to the manufacturer's cost only.

### Quick revision
- Discount% is on MP; profit% is on CP.
- $MP = CP \times \frac{100+g}{100-d}$; multiply chips through the chain.
- Markup% $= \left(\frac{100+g}{100-d} - 1\right) \times 100$.
- Free-item offers: discount = free ÷ total received.
"""

    S.pattern("pl-m1", "Discount per cent (and discount amount) from MP and SP", "very common",
        "MP and SP (or the discount in rupees) are given; the discount per cent or amount is asked.",
        r"\text{Discount\%} = \frac{MP - SP}{MP} \times 100",
        r"""1. Discount $= MP - SP$.
2. Divide by MP (never by SP or CP) and multiply by 100.
3. For the rupee value, take that per cent of MP.

Why: a discount is a reduction offered on the tagged price.""",
        "An article marked ₹900 is sold for ₹765. Find the discount per cent.",
        r"$\frac{135}{900} \times 100 = 15\%$. Discount amount $= ₹135$.")
    S.pattern("pl-m2", "Marked price for a target profit after discount", "very common",
        "'At what price should he mark to allow a d% discount and still gain g%?' — CP given, MP asked.",
        r"MP = CP \times \frac{100 + g}{100 - d}",
        r"""1. Write the chain: CP × markup chip × discount chip = SP.
2. Set $SP = CP \times \frac{100+g}{100}$ and divide by the discount chip.
3. Or apply the formula directly.

Why: MP must absorb both the discount and the desired gain.""",
        "An article costing ₹800 is to be sold at a 20% discount and still gain 20%. The marked price should be:",
        r"$MP = 800 \times \frac{120}{80} = ₹1{,}200$. Check: $1200 \times 0.8 = 960 = 800 \times 1.2$.")
    S.pattern("pl-m3", "Markup per cent from discount and profit", "very common",
        "'Allows d% discount and still gains g% — the marked price is what per cent above cost?'",
        r"\text{markup\%} = \left(\frac{100 + g}{100 - d} - 1\right) \times 100",
        r"""1. Compute $\frac{100+g}{100-d}$ — this is MP as a multiple of CP.
2. Subtract 1 and multiply by 100.
3. Take CP = 100 and trace the rupees if the formula feels abstract.

Why: the ratio of MP to CP depends only on the two percentages.""",
        "A trader allows a 25% discount on the marked price and still gains 20%. The marked price is what per cent above the cost price?",
        r"$\frac{120}{75} = 1.6$ → marked 60% above CP. (CP 100 → MP 160 → SP 120.)")
    S.pattern("pl-m4", "Multi-level trade chain (profit of the last trader)", "common",
        "Manufacturer sells to wholesaler, wholesaler to retailer, retailer to customer, each at a profit per cent; the final price or total rise is asked.",
        r"\text{final} = \text{cost} \times \prod \frac{100 + x_i}{100}",
        r"""1. Write each stage's chip ($1.25 = +25\%$, $1.1 = +10\%$ …).
2. Multiply all chips with the base cost (or divide backwards from the final price).
3. Each trader's profit% is on his own purchase price.

Why: every stage treats its buying price as its cost.""",
        "A manufacturer sells a TV to a wholesaler at 25% profit, the wholesaler to a retailer at 20% profit, and the retailer to a customer at 10% profit. If it cost ₹4,000 to make, the customer pays:",
        r"$4000 \times 1.25 \times 1.2 \times 1.1 = ₹6{,}600$. Total rise $= 65\%$.")
    S.pattern("pl-m5", "Discount schemes: free items and flat offers", "common",
        "'Buy 5 get 1 free', 'pay for 12 take 14', or comparing a scheme with a flat discount.",
        r"\text{discount\%} = \frac{\text{free items}}{\text{items received}} \times 100",
        r"""1. Count what the customer PAYS for and what he RECEIVES.
2. Discount% $=$ free ÷ received × 100.
3. Compare schemes by the kept fraction, not by the label.

Why: the seller spreads the cost of the free items over the whole batch.""",
        "'Buy 4 get 1 free' — what discount is the shop really giving?",
        r"Pay for 4, get 5 → discount $= \frac{1}{5} \times 100 = 20\%$.")

    d = F(900 - 765) / 900 * 100
    assert d == 15
    S.q("pl-m1", "easy", "An article marked at ₹900 is sold for ₹765. The discount per cent is:",
        ["15%", "13.5%", "17.6%", "12%"], P(d),
        r"Discount $= ₹135$; discount% $= \frac{135}{900} \times 100 = 15\%$ (on MP).",
        "17.6% wrongly divides by SP — the discount is on the marked price.", 25)
    d = F(750 - 600) / 750 * 100
    assert d == 20
    S.q("pl-m1", "medium",
        "A shopkeeper marks a bag at ₹750 and sells it for ₹600. The discount per cent is:",
        ["20%", "25%", "16.67%", "22%"], P(d),
        r"$\frac{150}{750} \times 100 = 20\%$.",
        "25% treats ₹750 as a cost price — ₹600 is 80% of the tag price.", 30)
    mp = 800 * F(120, 80)
    assert mp == 1200 and 1200 * F(8, 10) == 800 * F(6, 5)
    S.q("pl-m2", "medium",
        "A trader buys an article for ₹800 and wants a profit of 20% after allowing a 20% discount. At what price should he mark the article?",
        ["₹1,200", "₹1,280", "₹1,152", "₹1,000"], rs(mp),
        r"$MP = 800 \times \frac{120}{80} = ₹1{,}200$. Check: $1200 - 20\% = ₹960 = 800 + 20\%$.",
        "₹1,000 marks up 20% and forgets the discount comes out of the marked price.", 40)
    mp = 1350 * F(6, 5) * F(4, 3)
    assert mp == 2160 and mp * F(3, 4) == 1350 * F(6, 5)
    S.q("pl-m2", "hard",
        "A dealer purchases a cycle for ₹1,350 and allows a discount of 25% on the marked price. To gain 20%, the marked price should be:",
        ["₹2,160", "₹2,000", "₹1,890", "₹2,250"], rs(mp),
        r"Required SP $= 1350 \times 1.2 = ₹1{,}620$, which is 75% of MP → $MP = 1620 \times \frac{4}{3} = ₹2{,}160$.",
        r"₹2,250 adds 25% of ₹1,800 — the chain is $1350 \times \frac{6}{5} \times \frac{4}{3}$.", 45)
    mark = (F(120, 75) - 1) * 100
    assert mark == 60
    S.q("pl-m3", "easy",
        "A shopkeeper allows a discount of 25% on the marked price and still gains 20%. The marked price is what per cent above the cost price?",
        ["60%", "45%", "50%", "66.67%"], P(mark),
        r"$\frac{100+20}{100-25} = \frac{120}{75} = 1.6$ → 60% above CP. Check: CP 100 → MP 160 → SP 120.",
        "45% simply adds 20 + 25; the discount eats into the markup.", 30)
    mark = (F(108, 90) - 1) * 100
    assert mark == 20
    S.q("pl-m3", "medium",
        "After allowing a discount of 10% on the marked price, a trader gains 8%. The marked price is what per cent above the cost price?",
        ["20%", "18%", "19.8%", "22%"], P(mark),
        r"$\frac{108}{90} = 1.2$ → 20% above CP. (CP 100 → MP 120 → SP 108.)",
        "18% is 8 + 10 — percentages of different bases do not add.", 35)
    final = 4000 * F(5, 4) * F(6, 5) * F(11, 10)
    assert final == 6600
    S.q("pl-m4", "hard",
        "A manufacturer sells a washing machine to a wholesaler at 25% profit, the wholesaler sells it to a retailer at 20% profit, and the retailer sells it to a customer at 10% profit. If the manufacturing cost is ₹4,000, the price paid by the customer is:",
        ["₹6,600", "₹6,160", "₹7,150", "₹5,500"], rs(final),
        r"$4000 \times \frac{5}{4} \times \frac{6}{5} \times \frac{11}{10} = 4000 \times \frac{33}{20} = ₹6{,}600$.",
        "₹7,150 is 4000 × 1.25 × 1.2 × 1.1 × 1.1 — the retailer's profit acts once.", 50)
    rise = (F(6, 5) * F(4, 3) * F(11, 10) - 1) * 100
    assert rise == 76
    S.q("pl-m4", "medium",
        "A product passes from the manufacturer to the wholesaler (20% profit), then to the retailer (33⅓% profit) and finally to the customer (10% profit). The customer's price is what per cent more than the manufacturer's cost?",
        ["76%", "63%", "70%", "65%"], P(rise),
        r"$\frac{6}{5} \times \frac{4}{3} \times \frac{11}{10} = \frac{264}{150} = 1.76$ → 76% more.",
        "63% adds the three percentages; the chips multiply.", 40)
    disc = F(1, 6) * 100
    S.q("pl-m5", "medium",
        "A stationer announces 'buy 10, get 2 free'. The discount per cent offered is:",
        [r"$16\frac{2}{3}$%", "20%", "15%", "25%"], P(disc),
        r"Pay for 10, receive 12 → discount $= \frac{2}{12} \times 100 = 16\frac{2}{3}\%$.",
        "20% divides by the paid-for items — divide by what the customer receives.", 30)
    S.q("pl-m5", "hard",
        "A trader offers 'buy 19, get 1 free' on a book. Another shop offers a flat 6% discount. Which offer is better for the customer, and by how much (per cent)?",
        ["Flat 6% is better by 1%", "'Buy 19 get 1 free' is better by 1%", "Both are equal", "Flat 6% is better by 0.5%"],
        "Flat 6% is better by 1%",
        r"'Buy 19 get 1 free' $= \frac{1}{20} \times 100 = 5\%$ off. Flat 6% gives 1% more.",
        "The scheme's discount is 1/20 of what you RECEIVE, not 1/19.", 35)
    return S


def build_dishonest():
    S = Sub("pl-dishonest")
    S.notes = r"""### The idea
A dishonest dealer cheats on the **quantity**, not on the printed price. He charges for 1 kg but hands over 900 g, or uses a short measure. Compare what he **charges for** against what he **actually gives** — the gain is always bigger than it looks.

### Sells at cost price with a false weight
He uses w grams instead of a true W (usually 1000 g), at the cost price:
$$\text{gain\%} = \frac{W - w}{w} \times 100$$
900 g per kg: $\frac{100}{900} = 11\frac{1}{9}\%$. 800 g: $\frac{200}{800} = 25\%$. 750 g: $\frac{250}{750} = 33\frac{1}{3}\%$.
**Why divide by w?** His cost is for the w grams he actually handed over; his income is for W grams. Profit% is measured on the goods that left his shop.

### Reverse: gain given, find the false weight
Gains 25% at cost price → $\frac{1000 - w}{w} = \frac{25}{100}$ → $w = 800$ g. In general $w = W \times \frac{100}{100 + \text{gain\%}}$. The answer is always below the true weight.

### Claims a loss but cheats on weight
"Claims a 10% loss but gives only 800 g per kg." For every 800 g delivered he charges the price of a "10%-loss kilo" = 0.9 of the true kilo price:
$$\text{multiplier} = \frac{100 - L}{100 - c} = \frac{90}{80} = 1.125 \ \Rightarrow\ 12\frac{1}{2}\% \text{ gain}$$
Equal claim and shortfall (20% loss, 20% short) give exactly **no profit, no loss** — a favourite option.

### Cheats at both ends
Takes b% extra while buying and gives s% less while selling (everything at cost price):
$$\text{multiplier} = \frac{100 + b}{100 - s}$$
10% extra, 10% less: $\frac{110}{90} = \frac{11}{9}$ → gain $22\frac{2}{9}\%$. 10% extra, 20% less: $\frac{110}{80} = 1.375$ → 37.5% gain.

### Short weight plus a price rise
Uses an 800 g weight AND sells 20% above cost: money per false kilo $= 1.2 \times$ the true kilo price, goods given $= 0.8$ → $\frac{1.2}{0.8} = 1.5$ → 50% gain. Write the two cheats as chips and divide.

### How to attack any version
1. Fix a true unit (1 kg, 1 litre, 1 metre).
2. Write what he receives and what he gives, in units of that true measure.
3. Gain% $= \left(\frac{\text{received}}{\text{given}} - 1\right) \times 100$.

Worked mini-case: a pulse seller takes 110 kg while paying for 100 kg (₹40 per kg → ₹4,000), and later hands over 90 kg while charging for 100 kg (₹4,000). Per ₹4,000 he receives 110 kg and gives away 90 kg, so the multiplier is $\frac{110}{90} = \frac{11}{9}$ → gain $22\frac{2}{9}\%$ — no rupee arithmetic needed beyond the two counts.

### Quick revision
- False weight at CP: $\frac{W - w}{w} \times 100$ — divide by what he gives.
- Claimed loss L% with c% short weight: $\frac{100 - L}{100 - c} - 1$.
- Both ends: $\frac{100+b}{100-s} - 1$.
- Equal claim and shortfall → 0%.
"""

    S.pattern("pl-d1", "False weight sold at cost price", "very common",
        "'Sells at cost price but uses a weight of 800 g / 900 g for a kilogram' — the gain per cent is asked.",
        r"\text{gain\%} = \frac{W - w}{w} \times 100",
        r"""1. Take the true weight W (usually 1000 g) and the false weight w.
2. Gain% $= \frac{W - w}{w} \times 100$ — divide by w, the weight actually given.
3. Sanity check: smaller w → bigger gain.

Why: his cost is for w grams, his income is for W grams, and profit% is on the goods he actually parted with.""",
        "A shopkeeper sells sugar at cost price but uses a weight of 900 g for 1 kg. His gain per cent?",
        r"$\frac{1000 - 900}{900} \times 100 = 11\frac{1}{9}\%$.")
    S.pattern("pl-d2", "Reverse: gain per cent given, find the false weight", "common",
        "'Gains 25% while selling at cost price — what weight does he use instead of 1 kg?'",
        r"w = W \times \frac{100}{100 + \text{gain\%}}",
        r"""1. Write $\frac{W - w}{w} = \frac{g}{100}$.
2. Solve: $w = W \times \frac{100}{100 + g}$.
3. The false weight is always less than W.

Why: the gain fraction fixes the ratio of true to false weight.""",
        "A dishonest dealer sells at cost price and gains 25%. What weight does he give for a kilogram?",
        r"$w = 1000 \times \frac{100}{125} = 800$ g.")
    S.pattern("pl-d3", "Claimed loss with short weight", "common",
        "'Claims to sell at a loss of L% but gives c% less weight' — the true gain or loss is asked.",
        r"\text{multiplier} = \frac{100 - L}{100 - c}, \qquad \text{gain\%} = (\text{multiplier} - 1) \times 100",
        r"""1. Write the price he charges per true kg: $(100 - L)\%$ of the kilo price.
2. Write what the goods he gives should have cost: $(100 - c)\%$.
3. Divide the two; above 1 means a gain.

Why: he collects the 'loss-price' of a full kilo but supplies only part of it.""",
        "A merchant claims a 10% loss but gives only 800 g per kg. His true result?",
        r"$\frac{90}{80} = 1.125$ → $12\frac{1}{2}\%$ gain.")
    S.pattern("pl-d4", "Cheats while buying and selling", "common",
        "'Takes 10% extra while buying and gives 10% less while selling, at cost price' — overall gain per cent.",
        r"\text{gain\%} = \left(\frac{100 + b}{100 - s} - 1\right) \times 100",
        r"""1. Buying b% extra means he owns $\frac{100+b}{100}$ units per unit paid.
2. Selling s% short means each unit sold costs him only $\frac{100-s}{100}$ units.
3. Divide the chips; the excess over 1 is his gain.

Why: the two cheats multiply because they act at different stages.""",
        "A dealer takes 10% extra goods while buying and gives 10% less while selling, all at cost price. His gain per cent?",
        r"$\frac{110}{90} = \frac{11}{9}$ → gain $= \frac{2}{9} \times 100 = 22\frac{2}{9}\%$.")
    S.pattern("pl-d5", "False weight plus a higher price", "occasional",
        "The dealer both uses a short weight AND sells above cost price — a two-cheat multiplier.",
        r"\text{gain\%} = \left(\frac{\text{price chip} \times W}{w} - 1\right) \times 100",
        r"""1. Price chip: $1 + \frac{m}{100}$ for a markup m%.
2. Weight kept: w/W as a fraction.
3. Gain% $= \left(\frac{\text{price chip} \times W}{w} - 1\right) \times 100$.

Why: charging more per false kilo and giving less per true kilo are independent chips.""",
        "A seller uses an 800 g weight and sells 20% above cost price. His gain per cent?",
        r"$\frac{1.2 \times 1000}{800} = 1.5$ → 50% gain.")

    g = F(100, 900) * 100
    assert g == F(100, 9)
    S.q("pl-d1", "easy",
        "A dishonest shopkeeper sells rice at the cost price but uses a weight of 900 grams in place of 1 kg. His gain per cent is:",
        [r"$11\frac{1}{9}$%", "10%", r"$12\frac{1}{2}$%", r"$9\frac{1}{11}$%"], P(g),
        r"$\frac{1000 - 900}{900} \times 100 = 11\frac{1}{9}\%$.",
        "10% divides by 1000 — profit is on the 900 g he actually gave.", 30)
    g = F(200, 800) * 100
    assert g == 25
    S.q("pl-d1", "easy",
        "A trader sells at cost price but gives only 800 grams per kilogram. His gain per cent is:",
        ["25%", "20%", "22.5%", "28%"], P(g),
        r"$\frac{1000 - 800}{800} \times 100 = 25\%$.", None, 25)
    g = F(250, 750) * 100
    assert g == F(100, 3)
    S.q("pl-d1", "medium",
        "A vegetable vendor sells at the cost price but uses a weight of 750 g for a kilogram. His gain per cent is:",
        [r"$33\frac{1}{3}$%", "25%", "30%", r"$37\frac{1}{2}$%"], P(g),
        r"$\frac{250}{750} \times 100 = 33\frac{1}{3}\%$.",
        "Every 3 parts given earn 1 part extra.", 30)
    w = 1000 * F(100, 125)
    assert w == 800
    S.q("pl-d2", "medium",
        "A dishonest dealer professes to sell goods at the cost price but earns a profit of 25%. The weight he uses for a kilogram is:",
        ["800 g", "750 g", "850 g", "700 g"], f"{num(w)} g",
        r"$\frac{1000 - w}{w} = \frac{25}{100}$ → $w = 800$ g.",
        "750 g would give 33⅓%, more than the stated gain.", 35)
    g = F(100, 9)
    w = F(1000) / (1 + g / 100)
    assert w == 900
    S.q("pl-d2", "hard",
        r"A merchant sells at the cost price and gains $11\frac{1}{9}\%$ by cheating on the weight. How many grams does he give in place of one kilogram?",
        ["900 g", "890 g", "910 g", "850 g"], f"{num(w)} g",
        r"$w = 1000 \times \frac{100}{100 + \frac{100}{9}} = 1000 \times \frac{900}{1000} = 900$ g.",
        r"$11\frac{1}{9}\% = \frac{1}{9}$ — a ninth of what he gives, so 100 g on 900 g.", 40)
    m = F(90, 80)
    assert m == F(9, 8)
    ans = P((m - 1) * 100) + " gain"
    S.q("pl-d3", "medium",
        "A merchant claims to sell at a 10% loss but gives only 800 grams per kilogram. His actual gain or loss per cent is:",
        [ans, "10% loss", "2.5% gain", "No profit, no loss"], ans,
        r"Per true kg he charges 90% of the price but gives 80% of the goods: $\frac{90}{80} = 1.125$ → $12\frac{1}{2}\%$ gain.",
        "The 'loss' is on a kilo he never gives — compare money against true weight.", 40)
    m = F(80, 80)
    assert m == 1
    S.q("pl-d3", "medium",
        "A shopkeeper claims to sell at a 20% loss but gives only 20% less in weight. His actual result is:",
        ["No profit, no loss", "20% gain", "10% loss", "25% gain"], "No profit, no loss",
        r"$\frac{100-20}{100-20} = 1$ → no profit, no loss.",
        "He charges for 0.8 kg exactly what 0.8 kg cost him.", 35)
    m = F(110, 80)
    assert m == F(11, 8)
    S.q("pl-d4", "medium",
        "A dishonest dealer takes 10% more goods than he pays for while buying and gives 20% less than the true weight while selling, everything at cost price. His gain per cent is:",
        ["37.5%", "33.33%", "30%", "22.22%"], P((m - 1) * 100),
        r"$\frac{110}{80} = \frac{11}{8} = 1.375$ → 37.5% gain.",
        "30% adds the two cheats; they multiply instead.", 40)
    m = F(110, 90)
    assert m == F(11, 9)
    S.q("pl-d4", "hard",
        "A trader gains extra goods of 10% at the time of buying and sells 10% short of the true weight, charging the cost price throughout. His profit per cent is:",
        [r"$22\frac{2}{9}$%", "20%", r"$21\frac{1}{9}$%", "25%"], P((m - 1) * 100),
        r"$\frac{110}{90} = \frac{11}{9}$ → gain $= \frac{2}{9} \times 100 = 22\frac{2}{9}\%$.",
        "20% would be the gain if only one cheat existed.", 45)
    m = F(120, 80)
    assert m == F(3, 2)
    S.q("pl-d5", "medium",
        "A shopkeeper uses a weight of 800 g for a kilogram and sells his goods 20% above the cost price. His gain per cent is:",
        ["50%", "40%", "45%", "44%"], P((m - 1) * 100),
        r"$\frac{1.2 \times 1000}{800} = \frac{3}{2}$ → 50% gain.",
        "44% multiplies 20% and 25% — wrong, because the base changes after each cheat.", 40)
    m = F(110 * 1000, 95000)
    assert m == F(22, 19)
    S.q("pl-d5", "hard",
        "A milkman sells 10% above the cost price per litre but his one-litre measure actually holds 950 mL. His gain per cent is:",
        [r"$15\frac{15}{19}$%", "10.5%", "20%", r"$13\frac{3}{19}$%"], P((m - 1) * 100),
        r"Per true litre he charges $1.1 \times \frac{1000}{950} = \frac{22}{19}$ times the cost → gain $\frac{3}{19} \times 100 = 15\frac{15}{19}\%$.",
        "10.5% treats the two cheats as small additions.", 50)
    return S


def build_same():
    S = Sub("pl-same-price-cases")
    S.notes = r"""### The setup
Two articles are sold for the **same price**: one at a profit of x%, the other at a loss of x%. Most people guess "no profit no loss". The answer is always a **net loss**.

### The net loss formula
$$\text{Net loss\%} = \frac{x^2}{100}\% \quad \text{of the total cost price}$$
20% and 20% → 4% loss. 25% → $6.25\%$. 10% → 1%. $16\frac{2}{3}\% = \frac{1}{6}$ → $\left(\frac{1}{6}\right)^2 = \frac{1}{36} = 2\frac{7}{9}\%$.

### Why there must be a loss
Loss% and gain% act on two **different** cost prices. The article sold at a loss has the bigger CP, so its percentage bites harder. With common SP S:
$$CP_{\text{profit}} = \frac{S}{1 + x/100}, \qquad CP_{\text{loss}} = \frac{S}{1 - x/100}$$
and the excess of $CP_{\text{loss}}$ over S is always greater than the excess of S over $CP_{\text{profit}}$, because dividing by a number below 1 moves further than multiplying by a number above 1.

### Full reconstruction (when rupees are asked)
Two watches sold at ₹960 each, at 20% profit and 20% loss:
- $CP_1 = 960 \div 1.2 = ₹800$; $CP_2 = 960 \div 0.8 = ₹1{,}200$.
- Total CP $= ₹2{,}000$, total SP $= ₹1{,}920$ → loss $= ₹80 = 4\%$ of ₹2,000. The formula checks out.

### Useful special cases
- SP ₹1,980 each at ±10%: CPs 1,800 and 2,200 → loss ₹40.
- SP ₹600 each at ±20%: CPs 500 and 750 → loss ₹50.
- The loss per cent depends only on x, never on the SP.
- Unequal percentages (say +20% and −17.5%) break the $x^2/100$ shortcut — rebuild both CPs from the SP and add.

### Where the loss hides — a fuller look
Take SP ₹100 on each article at ±20%. The profitable article cost $100 \div 1.2 = ₹83.33$, so the gain is ₹16.67. The loss-making article cost $100 \div 0.8 = ₹125$, so the loss is ₹25. Same ₹100 selling price, but the loss (₹25) beats the gain (₹16.67) — the gap $25 - 16.67 = ₹8.33$ is exactly 4% of the total CP ₹208.33.
The bigger the x, the wider the gap: at ±50% the loss is $\frac{2500}{100} = 25\%$ of CP.

### A three-step routine for every version
1. Name the common SP (call it S, or use the rupee value given).
2. Recover each CP with its own chip: divide by $1 + \frac{x}{100}$ for the gain item and by $1 - \frac{x}{100}$ for the loss item.
3. Add the CPs, add the SPs, and read off the profit or loss.

### How the options are built
- "No profit, no loss" — the instinct answer; always wrong here.
- $\frac{x^2}{200}\%$ — halves the correct loss.
- $\frac{2x^2}{100}\%$ — doubles it.
- The correct $\frac{x^2}{100}\%$.
For rupee versions, one option usually applies the loss per cent to the SP instead of the CP.

### Two quick checks
- The loss per cent must depend only on x: change the SP and the percentage does not move.
- The loss item's CP is always the bigger one — if your reconstruction says otherwise, a chip was inverted.

### Quick revision
- Equal ±x% on the same SP → loss $\frac{x^2}{100}\%$.
- CPs: divide the common SP by $1 \pm \frac{x}{100}$.
- Loss in rupees = total CP − total SP; check it equals $\frac{x^2}{100}\%$ of total CP.
- The result is never zero — "no profit no loss" is the trap.
"""

    S.pattern("pl-q1", "Net result per cent for equal gain and loss on the same SP", "very common",
        "'Two articles sold at the same price, one at x% profit and the other at x% loss — the overall result?'",
        r"\text{net loss\%} = \frac{x^2}{100}\%",
        r"""1. Compute $\frac{x^2}{100}$ — a loss, never zero.
2. Spot the "no profit no loss" option and reject it.
3. For a fractional x ($16\frac{2}{3}\% = \frac{1}{6}$), square the fraction.

Why: the loss-side CP is larger, so its percentage dominates.""",
        "Two articles are sold at the same price, one at 25% profit and the other at 25% loss. The net result?",
        r"Loss $= \frac{625}{100} = 6.25\%$ of the total CP.")
    S.pattern("pl-q2", "Loss in rupees (reconstruct both cost prices)", "very common",
        "The common SP is given in rupees; the total loss (or total CP) is asked.",
        r"\text{loss} = 2S - \left(\frac{S}{1 + x/100} + \frac{S}{1 - x/100}\right)",
        r"""1. Divide the SP by $1 + \frac{x}{100}$ and by $1 - \frac{x}{100}$ to get the two CPs.
2. Total CP − total SP = the loss in rupees.
3. Verify: loss ÷ total CP must equal $\frac{x^2}{100}\%$.

Why: rupee answers need the actual cost prices, which the SP recovers.""",
        "Two mobiles are sold at ₹960 each, one at 20% profit and the other at 20% loss. The total loss?",
        r"CPs 800 and 1200 → total 2000; SPs 1920 → loss ₹80 (4% of CP).")
    S.pattern("pl-q3", "Same SP with unequal profit and loss percentages", "common",
        "One at a% profit, the other at b% loss with a ≠ b, same SP — the overall result in rupees or per cent.",
        r"\text{loss} = \left(\frac{S}{1 - b/100} + \frac{S}{1 + a/100}\right) - 2S",
        r"""1. Build each CP from the common SP with its own chip.
2. Add the CPs; compare with the total SP.
3. Divide by the total CP for the net per cent.

Why: unequal percentages break the $x^2/100$ shortcut.""",
        "Two tables are sold at ₹1,155 each — one at a 10% profit, the other at a 17.5% loss. The net result?",
        r"CPs 1050 and 1400 → total 2450; SPs 2310 → loss ₹140.")
    S.pattern("pl-q4", "Find the common SP or the profit per cent from the total loss", "occasional",
        "The total loss in rupees (or the total CP) is given; the common selling price or x is asked.",
        r"\text{loss} = \frac{x^2}{100} \times \frac{2S}{1 - x^2/10000}",
        r"""1. Write both CPs in terms of the common SP: $\frac{S}{1+x/100} + \frac{S}{1-x/100}$.
2. Total loss = that sum − 2S.
3. Set the loss equal to the rupee value and solve for S (or for x).

Why: the loss in rupees is a fixed fraction of the total CP, so any one of loss, S or x gives the rest.""",
        "Two articles are sold at the same price, one at 20% profit and the other at 20% loss. The total loss is ₹50. The selling price of each?",
        r"CP total $= \frac{5S}{6} + \frac{5S}{4} = \frac{25S}{12}$; loss $= \frac{25S}{12} - 2S = \frac{S}{12} = 50$ → $S = ₹600$.")

    for x, exp in ((20, 4), (25, F(25, 4)), (10, 1), (15, F(9, 4))):
        assert F(x) ** 2 / 100 == exp
    S.q("pl-q1", "easy",
        "Two articles are sold at the same price. One is sold at a profit of 20% and the other at a loss of 20%. On the whole transaction there is:",
        ["a loss of 4%", "no profit, no loss", "a loss of 2%", "a profit of 4%"], "a loss of 4%",
        r"Net loss $= \frac{20^2}{100} = 4\%$ of the total CP.",
        "'No profit, no loss' is the standard trap — the two percentages act on different costs.", 25)
    g = F(25 ** 2, 100)
    assert g == F(25, 4)
    S.q("pl-q1", "easy",
        "A man sells two watches at the same price, one at a gain of 25% and the other at a loss of 25%. His overall loss per cent is:",
        ["6.25%", "12.5%", "5%", "0%"], P(g),
        r"$\frac{25^2}{100} = 6.25\%$.",
        "12.5% adds the percentages — they act on different costs.", 25)
    g = F(100, 36)
    assert F(1, 6) ** 2 * 100 == g
    S.q("pl-q1", "hard",
        r"Two cycles are sold at the same price, one at a gain of $16\frac{2}{3}\%$ and the other at a loss of $16\frac{2}{3}\%$. The net loss per cent on the total cost is:",
        [r"$2\frac{7}{9}$%", "3%", r"$1\frac{7}{9}$%", r"$2\frac{2}{9}$%"], P(g),
        r"$16\frac{2}{3}\% = \frac{1}{6}$ → net loss $= \left(\frac{1}{6}\right)^2 = \frac{1}{36} = 2\frac{7}{9}\%$.",
        "3% rounds the exact fraction 1/36 — keep it exact.", 40)
    cp1, cp2 = 960 * F(5, 6), 960 * F(5, 4)
    loss = (cp1 + cp2) - 2 * 960
    assert cp1 == 800 and cp2 == 1200 and loss == 80
    S.q("pl-q2", "medium",
        "Two mobile phones are sold at ₹960 each — one at a profit of 20% and the other at a loss of 20%. The loss on the whole transaction is:",
        ["₹80", "₹60", "₹100", "₹96"], rs(loss),
        r"CPs: $\frac{960}{1.2} = 800$ and $\frac{960}{0.8} = 1200$ → total ₹2,000. SPs ₹1,920 → loss ₹80.",
        "₹96 is 4% of the SPs; the loss per cent is on the CP.", 35)
    loss = (1980 * F(10, 11) + 1980 * F(10, 9)) - 2 * 1980
    assert loss == 40
    S.q("pl-q2", "medium",
        "Two fans are sold at ₹1,980 each, one at a gain of 10% and the other at a loss of 10%. The total loss is:",
        ["₹40", "₹36", "₹44", "₹198"], rs(loss),
        r"CPs: 1800 and 2200 → ₹4,000 total; SPs ₹3,960 → loss ₹40 (1% of CP).",
        "₹36 takes 1% of the two SPs — wrong base.", 35)
    loss = (600 * F(5, 6) + 600 * F(5, 4)) - 2 * 600
    assert loss == 50
    S.q("pl-q2", "hard",
        "Two toy cars are sold at ₹600 each, one at a 20% profit and the other at a 20% loss. The total loss in rupees is:",
        ["50", "40", "60", "24"], "50",
        r"CPs: 500 and 750 → total ₹1,250; SPs ₹1,200 → loss ₹50. Check: $\frac{50}{1250} = 4\%$.",
        "The 4% acts on the total CP, not on the SPs.", 35)
    sp = 1500 * F(5, 4)
    cp2 = sp * F(4, 3)
    tot = 1500 + cp2
    loss = tot - 2 * sp
    assert sp == 1875 and cp2 == 2500 and loss == 250
    S.q("pl-q2", "hard",
        "A man sells two cycles at the same price. On the first, which cost ₹1,500, he gains 25%. On the second he loses 25%. His total loss (in ₹) is:",
        ["₹250", "₹375", "₹150", "₹625"], rs(loss),
        r"SP $= 1500 \times 1.25 = ₹1{,}875$; second CP $= 1875 \div 0.75 = ₹2{,}500$. "
        r"Total CP ₹4,000, SP ₹3,750 → loss ₹250.",
        r"The 6.25% loss acts on ₹4,000: $4000 \times 0.0625 = 250$.", 45)
    cp1 = F(1155) / F(11, 10)
    cp2 = F(1155) / F(33, 40)
    loss = cp1 + cp2 - 2 * 1155
    assert cp1 == 1050 and cp2 == 1400 and loss == 140
    S.q("pl-q3", "hard",
        "Two tables are sold at ₹1,155 each — one at a profit of 10% and the other at a loss of 17.5%. The total loss (in ₹) is:",
        ["₹140", "₹82.50", "₹115.50", "₹210"], rs(loss),
        r"CPs: $\frac{1155}{1.1} = 1050$ and $\frac{1155}{0.825} = 1400$ → total ₹2,450. SPs ₹2,310 → loss ₹140.",
        "Unequal percentages need both CPs; 82.50 wrongly takes 7.5% of the SPs.", 50)
    cp1 = F(1200) / F(6, 5)
    cp2 = F(1200) / F(3, 4)
    loss = cp1 + cp2 - 2 * 1200
    assert cp1 == 1000 and cp2 == 1600 and loss == 200
    ans = "loses " + rs(loss)
    S.q("pl-q3", "hard",
        "A dealer sells two computers at ₹1,200 each, gaining 20% on the first and losing 25% on the second. On the whole transaction he:",
        [ans, "gains ₹100", "loses ₹120", "neither gains nor loses"], ans,
        r"CPs: $\frac{1200}{1.2} = 1000$ and $\frac{1200}{0.75} = 1600$ → total ₹2,600; SPs ₹2,400 → loss ₹200.",
        "The 25% loss (₹400) outweighs the 20% gain (₹200) because it acts on the bigger CP.", 50)
    # pl-q4: reverse — total loss given, find the common SP (x = 20, loss 4% of total CP)
    S_ = 600
    cpA, cpB = F(S_) * F(5, 6), F(S_) * F(5, 4)
    tot = cpA + cpB
    assert cpA == 500 and cpB == 750 and tot == 1250 and tot - 2 * S_ == 50
    S.q("pl-q4", "hard",
        "Two articles are sold at the same price, one at a profit of 20% and the other at a loss of 20%. If the total loss is ₹50, the selling price of each article is:",
        ["₹600", "₹500", "₹750", "₹625"], rs(S_),
        r"CPs: $\frac{S}{1.2} = \frac{5S}{6}$ and $\frac{S}{0.8} = \frac{5S}{4}$ → total $\frac{25S}{12}$. "
        r"Loss $= \frac{25S}{12} - 2S = \frac{S}{12} = 50$ → $S = ₹600$.",
        "Check: CPs 500 and 750, total 1250; 4% of 1250 = 50.", 50)
    # pl-q4 again: find x from loss and SP (SP 960 each, loss 80 -> 4% of CP -> x = 20)
    x_val = [x for x in (5, 10, 20, 25) if (F(x * x, 100)) * (F(960) * F(5, 6) + F(960) * F(5, 4)) / 100 == 80]
    assert x_val == [20]
    S.q("pl-q4", "medium",
        "Two tables are sold at ₹960 each, one at a profit of x% and the other at a loss of x%. If the total loss is ₹80, x equals:",
        ["20", "10", "25", "5"], str(x_val[0]),
        r"CPs: 800 and 1200 → total ₹2,000. Loss% $= \frac{80}{2000} \times 100 = 4\% = \frac{x^2}{100}$ → $x = 20$.",
        "₹80 is 4% of the CP — never of the SP (that would suggest x ≈ 4.1).", 45)
    return S
