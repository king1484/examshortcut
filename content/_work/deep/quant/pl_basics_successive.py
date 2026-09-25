"""Phase-2 deep content for quant/profit-loss-discount — basics + successive modules."""
import os
import sys
from fractions import Fraction as F

sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
from _lib import Sub, num, rs, mixed


def P(x):
    """Fraction percent -> option text like '12%' or '$10\\frac{5}{7}$%'."""
    x = F(x)
    return (num(x) if x.denominator in (1, 2, 4, 5, 8, 10, 20, 25, 40, 50, 100) else mixed(x)) + "%"


def build_basics():
    S = Sub("pl-basics")
    S.notes = r"""### The words you need
- **Cost price (CP)**: what the seller paid for the article, including any extra costs such as transport or repair ("overheads").
- **Selling price (SP)**: what the buyer pays the seller.
- **Profit (gain)** $= SP - CP$ when SP is bigger; **loss** $= CP - SP$ when SP is smaller.
A shopkeeper buys a fan for ₹1,250 and sells it for ₹1,400: profit $= ₹150$.

### Profit and loss per cent are always on CP
$$\text{Profit\%} = \frac{\text{Profit}}{CP} \times 100, \qquad \text{Loss\%} = \frac{\text{Loss}}{CP} \times 100$$
For the fan: $\frac{150}{1250} \times 100 = 12\%$. Dividing by SP (giving $10\frac{5}{7}\%$) is the most common wrong option.
If there are overheads, add them to the CP first: bought ₹2,400 + ₹150 transport → CP ₹2,550.

### Multipliers (chips) — the fast way
Profit of x% means $SP = CP \times \frac{100 + x}{100}$; loss of x% means $SP = CP \times \frac{100 - x}{100}$.
| Change | Chip |
|---|---|
| 20% profit | $\frac{6}{5}$ |
| 25% profit | $\frac{5}{4}$ |
| $16\frac{2}{3}\%$ profit | $\frac{7}{6}$ |
| 10% loss | $\frac{9}{10}$ |
| $12\frac{1}{2}\%$ loss | $\frac{7}{8}$ |
Going back from SP to CP means **dividing** by the chip: SP ₹1,140 at 5% loss → $CP = 1140 \div \frac{19}{20} = ₹1{,}200$.

### Two selling prices, one cost price
"At 8% loss; had he sold for ₹336 more he would gain 6%." The two SPs differ by $8 + 6 = 14\%$ of CP. So $14\%$ of CP $= 336$ → $CP = ₹2{,}400$.
Rule: difference in rupees $=$ difference in percentages (add them when one is a loss and the other a gain) of CP.
Same idea: "selling at ₹720 gives as much profit as the loss when selling at ₹560" → CP is exactly in the middle: $\frac{720 + 560}{2} = ₹640$.

### Counting articles instead of rupees
"CP of 15 articles = SP of 12 articles." Take the price of one article as 1. The seller gets money for 15 by giving only 12 → profit $= \frac{15 - 12}{12} \times 100 = 25\%$ (divide by the goods given, which are the ones that cost him).
"Buys 4 for ₹15, sells 5 for ₹24": find per-article prices (₹3.75 and ₹4.80), or use a common count of 20 articles: CP ₹75, SP ₹96 → profit 28%.

### Changing CP and SP together
"If he had bought it 20% cheaper and sold it ₹60 cheaper, he would gain 25%." Let CP = 100 units and write both stories as chips: $1.1 \times CP - 60 = 0.8 \times CP \times 1.25$ → $0.1 \times CP = 60$ → $CP = ₹600$.

### Quick revision
- Profit% and loss% are on CP (plus overheads).
- SP $= CP \times$ chip; CP $= SP \div$ chip.
- Two SPs: rupee gap $=$ % gap of CP.
- Article counts: profit% $= \frac{\text{extra}}{\text{articles given}} \times 100$.
- Always check the answer by rebuilding SP from CP.
"""

    S.pattern("pl-b1", "Profit or loss per cent from CP and SP", "very common",
        "CP and SP are given (maybe with transport or repair cost) and the profit or loss per cent is asked.",
        r"\text{Profit\%} = \frac{SP - CP}{CP} \times 100",
        r"""1. Add any overheads to the CP.
2. Profit (or loss) $= SP - CP$.
3. Divide by CP (never by SP) and multiply by 100.

Why: profit is measured against the money the seller invested.""",
        "A fan bought for ₹1,250 is sold for ₹1,400. Find the profit per cent.",
        r"$\frac{150}{1250} \times 100 = 12\%$.")
    S.pattern("pl-b2", "Find CP or SP from a profit / loss per cent", "very common",
        "One price and the profit or loss per cent are given; the other price is asked.",
        r"SP = CP \times \frac{100 \pm x}{100}, \qquad CP = SP \times \frac{100}{100 \pm x}",
        r"""1. Write the chip: $\frac{100 + x}{100}$ for profit, $\frac{100 - x}{100}$ for loss.
2. CP → SP: multiply. SP → CP: divide.
3. Reduce the chip to a small fraction for speed ($\frac{19}{20}$, $\frac{7}{6}$ …).

Why: SP is CP scaled by the chip, so reversing it means dividing.""",
        "A table sold for ₹1,140 gives a loss of 5%. Find its CP.",
        r"$1140 \times \frac{20}{19} = ₹1{,}200$.")
    S.pattern("pl-b3", "Two selling prices — 'had he sold for ₹x more'", "very common",
        "'Sold at a% loss; had he sold for ₹k more he would gain b%' or two SPs giving equal profit and loss.",
        r"CP = \frac{k \times 100}{a + b} \ \ (\text{loss } a\%, \text{ gain } b\%)",
        r"""1. Both SPs are chips of the same CP.
2. Their rupee difference equals the difference of the percentages of CP (loss and gain → add; two gains → subtract).
3. Divide the rupees by that percentage of CP.

Why: the CP is common, so only the percentage gap moves the SP.""",
        "Sold at 8% loss; had it been sold for ₹336 more, the gain would be 6%. Find the CP.",
        r"$14\%$ of CP $= 336$ → $CP = ₹2{,}400$.")
    S.pattern("pl-b4", "Article-count questions", "common",
        "'CP of 15 articles = SP of 12', 'buys 4 for ₹15 and sells 5 for ₹24', or lemons sold at so many per rupee.",
        r"\text{Profit\%} = \frac{\text{articles bought} - \text{articles sold}}{\text{articles sold}} \times 100",
        r"""1. For 'CP of a = SP of b': profit% $= \frac{a - b}{b} \times 100$ (loss if b > a).
2. For rates like '4 for ₹15', use the LCM of the counts so both prices are for the same number of articles.
3. For 'how many for ₹k', find the required SP of one article, then divide.

Why: fixing a common count turns the question into a normal CP–SP comparison.""",
        "The CP of 15 articles equals the SP of 12. Find the profit per cent.",
        r"$\frac{15 - 12}{12} \times 100 = 25\%$.")
    S.pattern("pl-b5", "New SP for a different gain / changed CP and SP", "common",
        "'Sold at ₹1,530 at a loss of 10%; at what price to gain 10%?' or 'bought 20% cheaper and sold ₹60 less, gain 25%'.",
        r"SP_2 = SP_1 \times \frac{100 + b}{100 - a}",
        r"""1. Go back to CP by dividing by the first chip.
2. Multiply by the new chip.
3. For a changed CP and SP, write both stories with the same CP as a variable and equate.

Why: CP is the anchor that links every selling scenario.""",
        "An article sold for ₹1,530 gives a loss of 10%. At what price should it be sold to gain 10%?",
        r"$CP = 1530 \times \frac{10}{9} = 1700$; $SP = 1700 \times \frac{11}{10} = ₹1{,}870$.")

    p = F(1400 - 1250, 1250) * 100
    assert p == 12
    S.q("pl-b1", "easy", "A shopkeeper buys a fan for ₹1,250 and sells it for ₹1,400. His profit per cent is:",
        ["12%", "$10\\frac{5}{7}$%", "15%", "11%"], P(p),
        r"Profit $= ₹150$. Profit% $= \frac{150}{1250} \times 100 = 12\%$.",
        r"$10\frac{5}{7}\%$ divides by SP — profit is always on CP.", 25)
    assert P(F(150, 1400) * 100) == "$10\\frac{5}{7}$%"
    p = F(2856 - 2550, 2550) * 100
    assert p == 12
    S.q("pl-b1", "medium",
        "A man buys an old scooter for ₹2,400 and spends ₹150 on its repairs. He sells it for ₹2,856. His profit per cent is:",
        ["12%", "19%", "10.5%", "13%"], P(p),
        r"CP $= 2400 + 150 = ₹2{,}550$. Profit $= 306$. Profit% $= \frac{306}{2550} \times 100 = 12\%$.",
        "19% ignores the repair cost — overheads are part of CP.", 35)
    cp = F(1140) / F(95, 100)
    assert cp == 1200
    S.q("pl-b2", "easy", "By selling a chair for ₹1,140 a trader loses 5%. The cost price of the chair is:",
        ["₹1,200", "₹1,197", "₹1,083", "₹1,180"], rs(cp),
        r"$CP = 1140 \times \frac{100}{95} = ₹1{,}200$.",
        "₹1,197 adds 5% of SP — the loss is 5% of CP, so divide by 0.95.", 25)
    sp = 2400 * F(7, 6)
    assert sp == 2800
    S.q("pl-b2", "easy",
        r"An article costs ₹2,400. To gain $16\frac{2}{3}\%$, it should be sold for:",
        ["₹2,800", "₹2,760", "₹2,880", "₹2,720"], rs(sp),
        r"$16\frac{2}{3}\% = \frac{1}{6}$ → $SP = 2400 \times \frac{7}{6} = ₹2{,}800$.", None, 25)
    cp = F(336 * 100, 8 + 6)
    assert cp == 2400 and cp * F(106, 100) - cp * F(92, 100) == 336
    S.q("pl-b3", "medium",
        "A man sells a watch at a loss of 8%. Had he sold it for ₹336 more, he would have gained 6%. The cost price of the watch is:",
        ["₹2,400", "₹4,200", "₹5,600", "₹16,800"], rs(cp),
        r"The two SPs differ by $8\% + 6\% = 14\%$ of CP. $14\%$ of CP $= 336$ → $CP = ₹2{,}400$.",
        "₹16,800 uses 8 − 6 = 2%; a loss and a gain are on opposite sides of CP, so add.", 35)
    C = [c for c in range(1, 5000) if F(11, 10) * c - 60 == F(8, 10) * c * F(5, 4)]
    assert C == [600]
    S.q("pl-b5", "hard",
        "A man bought an article and sold it at a gain of 10%. Had he bought it for 20% less and sold it for ₹60 less, he would have gained 25%. The cost price of the article is:",
        ["₹600", "₹500", "₹480", "₹660"], "₹600",
        r"""Let CP $= x$. Actual SP $= 1.1x$.
New CP $= 0.8x$, new SP $= 0.8x \times 1.25 = x$.
$1.1x - 60 = x$ → $x = ₹600$. Check: SP 660; new CP 480, new SP 600, gain $\frac{120}{480} = 25\%$.""",
        "0.8 × 1.25 = 1, so the new SP equals the old CP: 10% of CP = ₹60.", 55)
    p = F(15 - 12, 12) * 100
    assert p == 25
    S.q("pl-b4", "medium",
        "If the cost price of 15 articles is equal to the selling price of 12 articles, the profit per cent is:",
        ["25%", "20%", "15%", "30%"], P(p),
        r"Let each article cost ₹1. SP of 12 articles $= ₹15$, CP of 12 $= ₹12$ → profit $= \frac{3}{12} \times 100 = 25\%$.",
        "20% divides by 15 — divide by the articles actually sold (12).", 30)
    p = (F(24, 5) - F(15, 4)) / F(15, 4) * 100
    assert p == 28
    S.q("pl-b4", "hard",
        "A fruit seller buys oranges at 4 for ₹15 and sells them at 5 for ₹24. His profit per cent is:",
        ["28%", "21.875%", "25%", "30%"], P(p),
        r"""Take 20 oranges (LCM of 4 and 5). CP $= 5 \times 15 = ₹75$; SP $= 4 \times 24 = ₹96$.
Profit $= \frac{21}{75} \times 100 = 28\%$.""",
        "21.875% divides the gain by SP.", 45)
    cp_each = F(40, 45) / F(8, 10)
    sp_each = cp_each * F(6, 5)
    n_ = F(24) / sp_each
    assert n_ == 18
    S.q("pl-b4", "hard",
        "By selling 45 lemons for ₹40, a man loses 20%. How many lemons should he sell for ₹24 to gain 20%?",
        ["18", "20", "16", "24"], num(n_),
        r"""CP of 45 lemons $= 40 \div 0.8 = ₹50$ → CP of one $= ₹\frac{10}{9}$.
SP for 20% gain $= \frac{10}{9} \times \frac{6}{5} = ₹\frac{4}{3}$ each. Lemons for ₹24 $= 24 \div \frac{4}{3} = 18$.""",
        r"Money scales by $\frac{120}{80} = \frac{3}{2}$ per lemon: for ₹24 at the old rate he gives 27 lemons; at the new rate $27 \div \frac{3}{2} = 18$.", 55)
    cp = 1530 / F(9, 10)
    sp = cp * F(11, 10)
    assert cp == 1700 and sp == 1870
    S.q("pl-b5", "medium",
        "A mobile phone sold for ₹1,530 gives a loss of 10%. To gain 10%, it should be sold for:",
        ["₹1,870", "₹1,836", "₹1,683", "₹1,850"], rs(sp),
        r"$CP = 1530 \div 0.9 = ₹1{,}700$. $SP = 1700 \times 1.1 = ₹1{,}870$.",
        r"$1530 \times \frac{11}{9} = ₹1{,}870$ in one step. (₹1,836 adds 20% of ₹1,530 — wrong base.)", 30)
    cp = F(720 + 560, 2)
    sp = cp * F(5, 4)
    assert cp == 640 and 720 - cp == cp - 560 and sp == 800
    S.q("pl-b3", "medium",
        "The profit earned by selling an article for ₹720 is equal to the loss incurred by selling it for ₹560. At what price should it be sold to make a profit of 25%?",
        ["₹800", "₹780", "₹900", "₹820"], rs(sp),
        r"Profit = loss → CP is midway: $CP = \frac{720 + 560}{2} = ₹640$. SP for 25% gain $= 640 \times \frac{5}{4} = ₹800$.",
        "₹900 applies 25% to ₹720, not to the CP.", 35)
    return S


def build_successive():
    S = Sub("pl-successive")
    S.notes = r"""### What "successive" means
Successive changes happen one after another, and **each new change works on the value left by the previous one**. A shop gives 20% off, and then a further 10% off on the reduced bill. The second 10% is on the smaller amount, so the total discount is less than 30%.

### Two changes: the $a + b + \frac{ab}{100}$ rule
For two changes of $a\%$ and $b\%$ (use minus for decreases):
$$\text{Net change} = a + b + \frac{ab}{100}$$
For two **discounts** $d_1$ and $d_2$ this becomes
$$\text{Equivalent single discount} = d_1 + d_2 - \frac{d_1 d_2}{100}$$
20% and 15% → $35 - 3 = 32\%$. 10% and 20% → $30 - 2 = 28\%$.

### Chips — works for any number of changes
Each discount $d\%$ keeps $\frac{100 - d}{100}$ of the price. Multiply the kept fractions:
10%, 20%, 25% → $0.9 \times 0.8 \times 0.75 = 0.54$ → the customer pays 54% → single discount $= 46\%$ (not 55%).
Price after discounts on a marked price (MP) of ₹5,000 at 10% and 5%: $5000 \times 0.9 \times 0.95 = ₹4{,}275$.
The order of the discounts does not matter — multiplication gives the same result either way.

### Comparing two offers
"40% flat" versus "30% + 10%": the second is $30 + 10 - 3 = 37\%$, so the flat offer saves 3% of the bill more. If the difference is ₹72, the bill is $\frac{72}{0.03} = ₹2{,}400$.
A single discount is always better for the buyer than successive discounts that add up to the same number.

### Finding a missing discount
MP ₹1,600, first discount 15%, final price ₹1,224. After the first discount the price is ₹1,360; the second discount $= \frac{1360 - 1224}{1360} = 10\%$.
Two equal discounts taking ₹6,400 to ₹5,184: kept fraction $= \frac{5184}{6400} = 0.81 = 0.9^2$ → each discount 10%.

### Increase then decrease
A price raised by 20% and then cut by 20% ends **4% lower**: $1.2 \times 0.8 = 0.96$. In general, up $x\%$ then down $x\%$ (either order) gives a loss of $\frac{x^2}{100}\%$. A TV priced ₹30,000 → ₹36,000 → ₹28,800: the buyer pays ₹1,200 less than the original.
Markup followed by successive discounts: marked 30% above CP, then 10% and 10% off → $1.3 \times 0.81 = 1.053$ → profit 5.3%.

### Common traps
- Adding discounts directly (10% + 20% = 30% is wrong).
- Taking the second discount on the original MP.
- For three discounts, using the two-change formula only once.

### Quick revision
- Two discounts: $d_1 + d_2 - \frac{d_1 d_2}{100}$.
- Any number: multiply the kept fractions $\frac{100 - d}{100}$.
- Up $x\%$ then down $x\%$ → net fall of $\frac{x^2}{100}\%$.
- Missing discount: divide the final price by the price after the known discounts.
"""

    S.pattern("pl-s1", "Equivalent single discount", "very common",
        "'Successive discounts of 20% and 15% are equal to a single discount of?' — two or three discounts, no rupee values.",
        r"d = d_1 + d_2 - \frac{d_1 d_2}{100}",
        r"""1. For two discounts, use $d_1 + d_2 - \frac{d_1 d_2}{100}$.
2. For three or more, multiply the kept fractions and subtract from 100%.
3. Check: the answer is less than the plain sum of discounts.

Why: each later discount acts on an already reduced price.""",
        "Find a single discount equivalent to successive discounts of 20% and 15%.",
        r"$20 + 15 - \frac{20 \times 15}{100} = 32\%$.")
    S.pattern("pl-s2", "Selling price after successive discounts", "very common",
        "A marked price and two or three discounts are given; the price paid is asked.",
        r"SP = MP \times \frac{100 - d_1}{100} \times \frac{100 - d_2}{100}",
        r"""1. Write each discount as a kept fraction (10% → 0.9, 12.5% → 7/8).
2. Multiply the MP by all kept fractions.

Why: every discount scales the current price by its kept fraction.""",
        "The marked price is ₹5,000; discounts of 10% and 5% are given. Find the price paid.",
        r"$5000 \times 0.9 \times 0.95 = ₹4{,}275$.")
    S.pattern("pl-s3", "Comparing a single discount with successive discounts", "common",
        "'The difference between a flat 40% discount and successive 30% and 10% is ₹72' — find the bill or the difference.",
        r"\text{difference} = (\text{single} - \text{equivalent}) \% \text{ of MP}",
        r"""1. Convert the successive discounts to one equivalent discount.
2. Subtract from the single discount to get the percentage gap.
3. That gap is a percentage of the MP; use it to find either value.

Why: both offers start from the same MP, so only the percentages differ.""",
        "Difference between a 40% discount and successive discounts of 30% and 10% on a bill is ₹72. Find the bill.",
        r"Successive $= 37\%$ → gap $3\%$ of bill $= 72$ → bill $= ₹2{,}400$.")
    S.pattern("pl-s4", "Find a missing discount", "common",
        "MP, final price and one discount are given (or 'two equal discounts'); the other discount is asked.",
        r"\frac{100 - d_2}{100} = \frac{SP}{MP \times \frac{100 - d_1}{100}}",
        r"""1. Apply the known discount to MP.
2. Compare the final price with that reduced price to get the second kept fraction.
3. For two equal discounts, take the square root of $\frac{SP}{MP}$.

Why: the second discount is a percentage of the price after the first.""",
        "MP ₹1,600; after two discounts, the first being 15%, the price is ₹1,224. Find the second discount.",
        r"After 15%: ₹1,360. $\frac{1224}{1360} = 0.9$ → second discount $10\%$.")
    S.pattern("pl-s5", "Raise then reduce (markup and successive cuts)", "common",
        "'Price increased by 20% and then decreased by 20%' or 'marked 30% above CP, then two discounts of 10%'.",
        r"\text{net} = a + b + \frac{ab}{100}, \quad \text{or multiply all chips}",
        r"""1. Write every rise and fall as a chip (1.3, 0.9, 0.9 …).
2. Multiply the chips; subtract 1 for the net change.
3. Same % up and down always ends below the start by $\frac{x^2}{100}\%$.

Why: the second change acts on a different base from the first.""",
        "An article is marked 30% above CP, then sold after successive discounts of 10% and 10%. Profit%?",
        r"$1.3 \times 0.9 \times 0.9 = 1.053$ → profit $5.3\%$.")

    def eq(*ds):
        k = F(1)
        for d in ds:
            k *= (1 - F(d) / 100)
        return (1 - k) * 100

    d = eq(20, 15)
    assert d == 32
    S.q("pl-s1", "easy", "Two successive discounts of 20% and 15% are equivalent to a single discount of:",
        ["32%", "35%", "33%", "30%"], P(d),
        r"$20 + 15 - \frac{20 \times 15}{100} = 35 - 3 = 32\%$.", None, 25)
    d = eq(10, 20, 25)
    assert d == 46
    S.q("pl-s1", "medium", "Three successive discounts of 10%, 20% and 25% are equivalent to a single discount of:",
        ["46%", "55%", "45%", "48%"], P(d),
        r"Kept: $0.9 \times 0.8 \times 0.75 = 0.54$ → single discount $= 100 - 54 = 46\%$.",
        "55% simply adds the three discounts.", 35)
    d = eq(F(25, 2), 20, 10)
    assert d == 37
    S.q("pl-s1", "hard", r"A single discount equivalent to successive discounts of $12\frac{1}{2}\%$, 20% and 10% is:",
        ["37%", "42.5%", "36%", "38%"], P(d),
        r"Kept: $\frac{7}{8} \times \frac{4}{5} \times \frac{9}{10} = \frac{252}{400} = 0.63$ → single discount $37\%$.", None, 40)
    sp = 5000 * F(9, 10) * F(19, 20)
    assert sp == 4275
    S.q("pl-s2", "easy",
        "The marked price of a washing machine is ₹5,000. It is sold after two successive discounts of 10% and 5%. The selling price is:",
        ["₹4,275", "₹4,250", "₹4,300", "₹4,225"], rs(sp),
        r"$5000 \times 0.9 = 4500$; $4500 \times 0.95 = ₹4{,}275$.",
        "₹4,250 takes a flat 15% — successive discounts give less than their sum.", 30)
    sp = 12500 * F(88, 100) * F(95, 100)
    assert sp == 10450
    S.q("pl-s2", "medium",
        "A laptop is marked at ₹12,500. The shopkeeper allows successive discounts of 12% and 5%. The customer pays:",
        ["₹10,450", "₹10,375", "₹10,625", "₹10,500"], rs(sp),
        r"$12500 \times 0.88 = 11000$; $11000 \times 0.95 = ₹10{,}450$.",
        "₹10,375 applies a flat 17%.", 35)
    diff = 8000 * F(7, 10) * F(95, 100) - 8000 * F(65, 100)
    assert diff == 120
    S.q("pl-s3", "medium",
        "On a marked price of ₹8,000, what is the difference between a single discount of 35% and two successive discounts of 30% and 5%?",
        ["₹120", "₹0", "₹400", "₹160"], rs(diff),
        r"""Single: $8000 \times 0.65 = ₹5{,}200$. Successive: $8000 \times 0.7 \times 0.95 = ₹5{,}320$.
Difference $= ₹120$.""",
        r"Successive $= 30 + 5 - 1.5 = 33.5\%$; gap $1.5\%$ of 8000 $= ₹120$.", 40)
    gap = 40 - eq(30, 10)
    bill = F(72) / gap * 100
    assert gap == 3 and bill == 2400
    S.q("pl-s3", "hard",
        "The difference between a discount of 40% and two successive discounts of 30% and 10% on a certain bill is ₹72. The amount of the bill is:",
        ["₹2,400", "₹7,200", "₹1,800", "₹720"], rs(bill),
        r"Successive $= 30 + 10 - 3 = 37\%$. Gap $= 3\%$ of bill $= 72$ → bill $= ₹2{,}400$.",
        "₹720 treats the 10% gap (40 − 30) as the difference.", 45)
    d2 = (1 - F(1224) / (1600 * F(85, 100))) * 100
    assert d2 == 10
    S.q("pl-s4", "medium",
        "An article marked at ₹1,600 is sold for ₹1,224 after two successive discounts. If the first discount is 15%, the second discount is:",
        ["10%", "8%", "12%", "9.5%"], P(d2),
        r"After 15%: $1600 \times 0.85 = ₹1{,}360$. Second discount $= \frac{1360 - 1224}{1360} \times 100 = 10\%$.",
        "12% would be (1360 − 1224)/... on the MP — the second discount is on ₹1,360.", 40)
    k = F(5184, 6400)
    assert k == F(81, 100)
    S.q("pl-s4", "hard",
        "After two equal successive discounts, an article marked at ₹6,400 is sold for ₹5,184. Each discount is:",
        ["10%", "9%", "12%", "9.5%"], "10%",
        r"Kept fraction $= \frac{5184}{6400} = 0.81 = 0.9^2$ → each discount $= 10\%$.",
        "9.5% halves the total 19% — successive discounts do not split evenly.", 40)
    for w in ("9%", "12%", "9.5%"):
        wd = F(w[:-1])
        assert (1 - wd / 100) ** 2 != k
    final = 30000 * F(6, 5) * F(4, 5)
    assert final == 28800
    S.q("pl-s5", "medium",
        "The price of a TV set, originally ₹30,000, is increased by 20% and later decreased by 20%. Compared with the original price, the final price is:",
        ["₹1,200 less", "the same", "₹1,200 more", "₹600 less"], "₹1,200 less",
        r"$30000 \times 1.2 = 36000$; $36000 \times 0.8 = 28800$ → ₹1,200 less.",
        r"Net $= -\frac{20^2}{100} = -4\%$ of ₹30,000 $= ₹1{,}200$ less.", 30)
    p = (F(13, 10) * F(9, 10) * F(9, 10) - 1) * 100
    assert p == F(53, 10)
    S.q("pl-s5", "hard",
        "A trader marks his goods 30% above the cost price and then allows two successive discounts of 10% each. His profit per cent is:",
        ["5.3%", "10%", "11%", "6.5%"], P(p),
        r"$1.3 \times 0.9 \times 0.9 = 1.053$ → profit $= 5.3\%$.",
        "10% subtracts 20% from 30%; the two discounts together are only 19%, and they act on 130.", 45)
    return S
