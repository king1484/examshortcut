from _lib import *
from fractions import Fraction as Fr

# ------------------------------------------------------------------ checks
assert F(1020 - 850, 850) == F(1, 5)
assert F(960 - 816, 960) == F(15, 100)
assert Fr(460, 115) * 100 == 400
assert 1 - Fr(9, 10) * Fr(8, 10) == F(28, 100)
assert Fr(14, 10) * Fr(9, 10) == F(126, 100)
assert Fr(960, 20) * 100 == 4800
assert 1600 * Fr(8, 10) * Fr(7, 8) == 1120 and 1600 - 1120 == 480
assert F(480, 1600) == F(3, 10)
assert 1000 * Fr(5, 4) * Fr(85, 100) == Fr(2125, 2) and F(5, 4) * Fr(17, 20) == F(17, 16)
assert Fr(17, 16) * Fr(4, 25) == F(17, 100)  # 6.25%
assert Fr(12, 10) / Fr(75, 100) == Fr(8, 5)  # M4: MP/CP = 1.2/0.75 -> 60%
assert Fr(1200, 125) * 100 == 960 and Fr(1200, 75) * 100 == 1600
assert 960 + 1600 == 2560 and F(160, 2560) == F(1, 16)
assert F(1680, 120) * 100 == 1400 and F(1680, 80) * 100 == 2100
assert 1400 + 2100 == 3500 and 3360 - 3500 == -140 and F(140, 3500) == F(1, 25)
assert Fr(9, 10) * Fr(8, 10) == F(18, 25) and F(100, 100) - F(72, 100) == F(28, 100)
# M5: claims 10% loss, gives 800 g per kg -> gain 12.5%
assert Fr(90, 100) / Fr(80, 100) == Fr(9, 8) and F(1, 8) == F(125, 1000)
# M7: buys 10% extra, sells 10% short -> 110/90 - 1 = 2/9
assert Fr(110, 90) - 1 == F(2, 9)
# H1 chain
assert Fr(12, 10) * Fr(125, 100) * Fr(11, 10) == Fr(33, 20) and 2000 * Fr(33, 20) == 3300
# H2: 12.5% profit vs 6% loss on CP 280
assert 280 * F(25, 200) == 35
assert 280 * F(94, 100) == Fr(1316, 5)
assert Fr(315, 1) - Fr(1316, 5) == Fr(518, 10)
assert F(518, 10) / 280 == F(185, 1000)
# S1/S2/S4/S5
assert F(72, 480) == F(15, 100)
assert Fr(624, 96) * 100 == 650
assert Fr(12, 10) / Fr(9, 10) == Fr(4, 3) and 600 * Fr(4, 3) == 800
assert F(100, 900) == F(1, 9)

subtopics = [
 sub("pl-basics", "Profit, Loss and CP–SP Basics",
  md(r"Profit and loss are **always calculated on the cost price (CP)** unless stated otherwise.",
     "",
     r"$$\text{Profit} = SP - CP, \qquad \text{Loss} = CP - SP$$",
     r"$$\text{Profit\%} = \frac{\text{Profit}}{CP} \times 100, \qquad SP = CP\left(\frac{100 \pm x}{100}\right)$$",
     "",
     r"**Multiplier chips:** profit of 20% → SP = 1.2 × CP; loss of 15% → SP = 0.85 × CP. Percentages as fractions are faster: 12.5% = $\frac{1}{8}$, 16⅔% = $\frac{1}{6}$, 8⅓% = $\frac{1}{12}$.",
     "",
     r"To recover CP from SP at x% profit: $CP = \frac{100 \cdot SP}{100 + x}$ — divide by the chip, don't take x% of SP."),
  [formula("Profit / loss per cent", r"\text{P\%} = \frac{SP - CP}{CP} \times 100"),
   formula("Selling price", r"SP = CP\left(1 \pm \frac{x}{100}\right)"),
   formula("Cost price from SP", r"CP = \frac{SP}{1 \pm \frac{x}{100}} = \frac{100 \cdot SP}{100 \pm x}"),
   formula("No profit, no loss", r"SP = CP")],
  [trick("Fraction ⇄ percentage swap",
         "Convert the profit % to a fraction; SP/CP becomes a clean ratio.",
         "A trader sells a cycle for ₹1,020 that cost him ₹850. Find the profit per cent.",
         r"Profit = 170; $\frac{170}{850} = \frac{1}{5} = 20\%$."),
   trick("Divide by the chip to get CP",
         "SP given with a profit/loss %: undo the multiplier.",
         "A machine is sold for ₹624 at a loss of 4%. Its cost price is:",
         r"$CP = \frac{624}{0.96} = 650$, i.e. ₹650."),
   trick("Two prices, same % — scale linearly",
         "If the same article at another CP/SP keeps the same profit %, everything scales by the same factor.",
         "By selling 15 pens a man recovers the cost of 12 pens. His gain per cent is:",
         r"Gain on 12 pens' cost = 3 pens ⇒ $\frac{3}{12} = 25\%$.")],
  [r"Calculating profit % on SP instead of CP (a ₹20 profit on SP 120 is NOT 16⅔% gain).",
   r"Recovering CP as $SP - x\% \text{ of } SP$ — that's the SP-based error again.",
   "Mixing up profit and loss chips (0.9 is a 10% loss, not a 10% discount on profit).",
   "Ignoring that 'gain of 25%' and 'marked 25% up' refer to different bases (CP vs MP)."]),

 sub("pl-successive", "Successive Changes & Equivalent Single Change",
  md("Two percentage changes applied one after another do **not** simply add — the second acts on the already-changed value.",
     "",
     r"$$\text{Net change} = a + b + \frac{ab}{100} \quad (\text{use } -b \text{ for a decrease})$$",
     "",
     r"- Same change x twice: increase $2x + \frac{x^2}{100}$; decrease $2x - \frac{x^2}{100}$.",
     r"- Two discounts of $d_1, d_2$: equivalent single discount $= d_1 + d_2 - \frac{d_1 d_2}{100}$.",
     "",
     r"**Chip method:** multiply $(1 \pm a/100)(1 \pm b/100)$ — this never fails, even for three changes, and reverses cleanly."),
  [formula("Two successive changes", r"\text{net} = a + b + \frac{ab}{100}"),
   formula("Same change twice (increase)", r"2x + \frac{x^2}{100}"),
   formula("Same change twice (decrease)", r"2x - \frac{x^2}{100}"),
   formula("Equivalent single discount", r"D = d_1 + d_2 - \frac{d_1 d_2}{100}")],
  [trick("Multiply the chips",
         "Chips work for any mix of increases and decreases, in any order.",
         "A price is increased by 20% and then the new price is decreased by 10%. Net change?",
         r"$1.20 \times 0.90 = 1.08$ ⇒ net **+8%** (not +10%)."),
   trick("The d₁ + d₂ − d₁d₂/100 formula",
         "Two discounts collapse in one line.",
         "Find the single discount equivalent to two successive discounts of 20% and 10%.",
         r"$20 + 10 - \frac{200}{100} = 28\%$."),
   trick("Work backwards through chips",
         "For 'find the second change given the net', divide the net chip by the first chip.",
         "After a rise of 25% a value was changed again and ended 15% up overall. Find the second change.",
         r"$1.15 / 1.25 = 0.92$ ⇒ a **decrease of 8%**.")],
  [r"Adding successive discounts directly (20% + 10% = 30% is wrong; the answer is 28%).",
   "For a profit then a loss, using +ab/100 where the sign must be negative.",
   "Applying the second discount on the original marked price instead of the reduced price.",
   "Assuming the order of changes matters — chip multiplication is commutative."]),

 sub("pl-marked-discount", "Marked Price, Discount and the CP–MP–SP Chain",
  md("The full chain: trader **marks up** CP to MP, then allows a **discount** on MP to reach SP.",
     "",
     r"$$\text{Discount} = MP - SP, \qquad \text{Discount\% is always on MP}$$",
     r"$$MP = CP \times \frac{100 + g}{100 - d}, \qquad SP = MP\left(\frac{100 - d}{100}\right)$$",
     "",
     r"Multi-level trade (manufacturer → wholesaler → retailer) chains the same way: multiply each markup factor $\left(1 + \frac{x}{100}\right)$.",
     "",
     r"If a discount of d% still leaves a gain of g%, the markup on CP must be $\frac{(100+g)}{(100-d)} - 1$ times CP."),
  [formula("Discount per cent", r"\text{D\%} = \frac{MP - SP}{MP} \times 100"),
   formula("Marked price for target gain", r"MP = CP \cdot \frac{100 + g}{100 - d}"),
   formula("SP through the chain", r"SP = CP\left(1 + \frac{m}{100}\right)\left(1 - \frac{d}{100}\right)"),
   formula("Multi-level markups", r"\text{Final} = \text{Base} \times \prod \left(1 + \frac{x_k}{100}\right)")],
  [trick("Build the MP/CP ratio",
         "Gain g% and discount d% together fix MP as a multiple of CP.",
         "After allowing a discount of 10% on the marked price a trader still gains 20%. The marked price is how much per cent above the cost price?",
         r"$\frac{MP}{CP} = \frac{120}{90} = \frac{4}{3}$ ⇒ **33⅓%** above CP."),
   trick("Markup chip then discount chip",
         "One chip for the markup, one for the discount.",
         "An article costing ₹1,000 is marked 25% above cost and sold at a 15% discount. Find the profit per cent.",
         r"$SP = 1000 \times 1.25 \times 0.85 = 1062.50$ ⇒ profit $6.25\%$, i.e. ₹62.50."),
   trick("Trade-chain multiplication",
         "Each middleman's markup is one chip.",
         "A manufacturer sells to a wholesaler at 20% profit, the wholesaler to a retailer at 25% profit, and the retailer to a customer at 10% profit. If the customer pays ₹3,300, the manufacturing cost is:",
         r"$2000 \times 1.2 \times 1.25 \times 1.1 = 3300$ ⇒ cost = **₹2,000**.")],
  [r"Taking the discount on CP instead of MP.",
   r"Forgetting that profit % is still on CP while discount % is on MP — the two bases differ.",
   "In trade chains, adding the markups (20 + 25 + 10 = 55%) instead of multiplying chips (65%).",
   "Reading 'marked 25% above cost' as MP = 125 when CP = 100 — right — but then applying discount % to CP."]),

 sub("pl-dishonest", "Dishonest Dealer, False Weights & Claims",
  md("The dealer cheats on the **quantity**, not the price. Compare true goods against paid goods.",
     "",
     r"**Sells at CP with false weight:** using w g instead of W g gives",
     r"$$\text{gain\%} = \frac{W - w}{w} \times 100$$",
     "",
     r"**Claims a loss but cheats on weight:** claims L% loss but gives c% less weight ⇒ true multiplier $= \frac{100 - L}{100 - c}$.",
     "",
     r"**Cheats both ways** — takes b% extra while buying and gives s% less while selling: multiplier $= \frac{100 + b}{100 - s}$.",
     "",
     "Setup a per-1000 g table: what he pays for, what he actually gets, what he actually gives."),
  [formula("False weight gain", r"\text{gain\%} = \frac{\text{true weight} - \text{used weight}}{\text{used weight}} \times 100"),
   formula("Claimed loss + short weight", r"\text{multiplier} = \frac{100 - L}{100 - c}"),
   formula("Cheat at both ends", r"\text{multiplier} = \frac{100 + b}{100 - s}"),
   formula("True gain from multiplier", r"\text{gain\%} = (\text{multiplier} - 1) \times 100")],
  [trick("The W−w over w rule",
         "Loss to the customer is measured against what the dealer actually gave.",
         "A shopkeeper sells rice at cost price but uses a weight of 900 g for 1 kg. Find his gain per cent.",
         r"$\frac{1000 - 900}{900} \times 100 = 11\frac{1}{9}\%$."),
   trick("Claimed loss can still be a gain",
         "Compare the money per TRUE gram, not per claimed gram.",
         "A merchant claims to sell at a 10% loss but gives only 800 g per kg. Find his actual gain or loss.",
         r"Per true kg he receives $0.90$ and pays $0.80$: gain $= \frac{0.9 - 0.8}{0.8} = 12.5\%$."),
   trick("Both-ends multiplier",
         "Multiply the buy-side gain chip by the sell-side chip.",
         "A dishonest dealer takes 10% more goods than he pays for and sells 10% less than the true weight. His gain per cent is:",
         r"$\frac{110}{90} - 1 = \frac{2}{9} = 22\frac{2}{9}\%$ gain.")],
  [r"Using $\frac{W-w}{W}$ instead of $\frac{W-w}{w}$ (the base is what the buyer actually received).",
   "Believing a '10% loss' claim without checking the weight.",
   "In both-ends cheating, adding the two percentages instead of multiplying chips.",
   "Mixing up which side the cheat favours — dealer gains when buying AND when selling."]),

 sub("pl-same-price-cases", "Same Selling Price: One Profit, One Loss",
  md("Two articles sold at the **same price**, one at x% profit and the other at x% loss, always end in a **net loss**:",
     "",
     r"$$\text{Net loss\%} = \left(\frac{x}{10}\right)^2 = \frac{x^2}{100}$$",
     "",
     r"Why: total $CP = \frac{S}{1 + x/100} + \frac{S}{1 - x/100} > 2S$. The loss is small but never zero.",
     "",
     "If asked for amounts, reconstruct each CP by dividing the common SP by its chip."),
  [formula("Net loss for equal ±x%", r"\text{net loss\%} = \frac{x^2}{100}"),
   formula("Reconstructed costs", r"CP_1 = \frac{S}{1 + x/100}, \quad CP_2 = \frac{S}{1 - x/100}"),
   formula("Overall position", r"\text{Loss} = CP_1 + CP_2 - 2S")],
  [trick("The x²/100 reflex",
         "Same SP, opposite equal % → straight to the loss formula.",
         "Two mobiles are sold for ₹1,200 each — one at a 25% profit and the other at a 25% loss. Find the overall per cent loss.",
         r"Loss% $= \frac{625}{100} = 6.25\%$. (Verify: CPs 960 and 1,600, total 2,560; SP 2,400; loss 160 = 6.25%.)"),
   trick("Reconstruct both CPs, then total",
         "Divide the common SP by each chip.",
         "Two articles are sold for ₹1,680 each; one at 20% profit, the other at 20% loss. Find the net loss in rupees.",
         r"CPs: $\frac{1680}{1.2} = 1400$ and $\frac{1680}{0.8} = 2100$; total 3,500 vs SP 3,360 ⇒ loss **₹140** (4%).")],
  [r"Concluding 'no profit no loss' because the percentages cancel — the base amounts differ, so there is always a loss.",
   r"Using $\frac{x^2}{100}$ when the profit and loss percentages are unequal — reconstruct CPs instead.",
   "Reporting the loss per cent as the loss amount (₹140 is not 140%).",
   "Dividing SP by the wrong chip (profit article: divide by 1 + x/100, loss article: by 1 − x/100)."]),
]

pyq = [
 pat("Direct profit/loss per cent", "very common",
     "CP and SP given (or one derivable in one step); find the profit or loss per cent.",
     "Find the difference, divide by CP, multiply by 100. Fraction equivalents (1/8 = 12.5%) skip the arithmetic."),
 pat("CP or SP reconstruction", "very common",
     "One of CP/SP given with the profit or loss % — find the other.",
     "Apply or undo the chip: SP = CP × (1 ± x/100). 'Had it been sold for ₹k more/less…' ⇒ the k spans the difference of two percentages of CP."),
 pat("Successive discounts / price changes", "very common",
     "'Two successive discounts of 20% and 10%', or a rise followed by a fall.",
     r"Chips multiply; equivalent single discount $= d_1 + d_2 - \frac{d_1d_2}{100}$. Never add discounts."),
 pat("MP–discount–profit chain", "very common",
     "Marked x% above cost, discount y% allowed, find gain % (or work back to MP).",
     r"$\frac{MP}{CP} = \frac{100+g}{100-d}$ fixes any one of MP/CP, gain, discount from the other two."),
 pat("Dishonest dealer / false weight", "common",
     "False weights, short measure, or a claimed loss with cheating on quantity.",
     r"$\text{gain\%} = \frac{W - w}{w} \times 100$; for claims, compare money per TRUE unit. Cheating at both ends multiplies chips."),
 pat("Same SP, one profit one loss", "common",
     "Two items sold at the same price with equal ±x% — the net result.",
     r"Net loss% $= \frac{x^2}{100}$; if amounts are asked, reconstruct both CPs."),
 pat("Multi-level markup (trade chain)", "occasional",
     "Manufacturer → wholesaler → retailer, each adding a profit %.",
     "Multiply the markup chips end to end; divide to walk backwards to the base cost."),
 pat("Cost of goods sold / goods-based cases", "occasional",
     "'Sells at CP the quantity equal to the cost of 20 units', 'recover the cost of 12 pens by selling 15'.",
     "Set up units: profit in units ÷ cost in units = gain fraction. Translate words into a fraction of CP."),
]

solved = []
assert F(72, 480) == F(15, 100)
solved.append(Q("pld-s01", "A trader buys a fan for ₹480 and sells it for ₹552. His profit per cent is:",
  ["12%", "14%", "15%", "18%"], 2, 15,
  md(r"Profit = $552 - 480 = 72$.",
     r"$\frac{72}{480} \times 100 = 15\%$."),
  "72/480 = 3/20 = 15%.",
  "easy", "pl-basics", "direct profit", 25))

assert Fr(624, 96) * 100 == 650
solved.append(Q("pld-s02", "A camera is sold for ₹624 at a loss of 4%. The cost price of the camera is:",
  ["₹600", "₹640", "₹650", "₹660"], 2, 650,
  md(r"$CP = \frac{624}{0.96} = 650$, i.e. ₹650."),
  "96% of CP = 624 ⇒ CP = 624 × 25/24 = 650.",
  "easy", "pl-basics", "find CP", 30))

assert 1 - Fr(9, 10) * Fr(8, 10) == F(28, 100)
solved.append(Q("pld-s03", "Successive discounts of 20% and 10% are equivalent to a single discount of:",
  ["30%", "28%", "25%", "27%"], 1, 28,
  md(r"$1 - 0.80 \times 0.90 = 0.28$ ⇒ single discount of **28%**.",
     r"Formula check: $20 + 10 - \frac{20 \times 10}{100} = 28\%$."),
  "d₁ + d₂ − d₁d₂/100 = 28%.",
  "easy", "pl-successive", "successive discounts", 25))

assert Fr(12, 10) / Fr(9, 10) == Fr(4, 3)
solved.append(Q("pld-s04", "A shopkeeper allows a 10% discount on the marked price of an article and still makes a profit of 20%. The marked price is what per cent above the cost price?",
  ["30%", "$33\\frac{1}{3}$%", "25%", "36%"], 1, Fr(100, 3),
  md(r"$SP = 1.20\,CP$ and $SP = 0.90\,MP$ ⇒ $MP = \frac{1.2}{0.9}CP = \frac{4}{3}CP$.",
     "So MP is 33⅓% above CP. (E.g. CP ₹600 → MP ₹800, SP ₹720.)"),
  "MP/CP = (100 + g)/(100 − d) = 120/90 = 4/3.",
  "medium", "pl-marked-discount", "MP-discount-profit", 40))

assert F(100, 900) == F(1, 9)
solved.append(Q("pld-s05", "A dishonest shopkeeper sells sugar at the cost price but uses a weight of 900 grams in place of 1 kg. His gain per cent is:",
  ["9%", "10%", "$11\\frac{1}{9}$%", "12.5%"], 2, F(100, 9),
  md(r"Gain is on the 900 g he actually gave: $\frac{1000 - 900}{900} \times 100 = 11\frac{1}{9}\%$."),
  "W − w over w: 100/900 = 11⅑%.",
  "medium", "pl-dishonest", "false weight", 35))

# ------------------------------------------------------------------ practice
P = []

assert F(170, 850) == F(1, 5)
P.append(Q("pld-q01", "A cycle bought for ₹850 is sold for ₹1,020. The profit per cent is:",
  ["15%", "18%", "20%", "22%"], 2, 20,
  md(r"Profit $= 170$; $\frac{170}{850} = \frac{1}{5} = 20\%$."),
  "170/850 = 1/5 ⇒ 20%.",
  "easy", "pl-basics", "direct profit", 20))

assert F(144, 960) == F(15, 100)
P.append(Q("pld-q02", "An article costing ₹960 is sold for ₹816. The loss per cent is:",
  ["12%", "15%", "18%", "20%"], 1, 15,
  md(r"Loss $= 144$; $\frac{144}{960} \times 100 = 15\%$."),
  "144/960 = 3/20 ⇒ 15%.",
  "easy", "pl-basics", "direct loss", 20))

assert Fr(460, 115) * 100 == 400
P.append(Q("pld-q03", "By selling a table for ₹460 a trader gains 15%. The cost price of the table is:",
  ["₹391", "₹400", "₹414", "₹420"], 1, 400,
  md(r"$CP = \frac{460}{1.15} = 400$, i.e. ₹400."),
  "115% of CP = 460 ⇒ CP = 460 × 20/23 = 400.",
  "easy", "pl-basics", "find CP", 25))

assert 1 - Fr(9, 10) * Fr(8, 10) == F(28, 100)
P.append(Q("pld-q04", "Two successive discounts of 10% and 20% are equivalent to a single discount of:",
  ["28%", "29%", "30%", "32%"], 0, 28,
  md(r"$10 + 20 - \frac{200}{100} = 28\%$."),
  "Formula: d₁ + d₂ − d₁d₂/100 = 28%.",
  "easy", "pl-successive", "successive discounts", 25))

assert Fr(14, 10) * Fr(9, 10) == F(126, 100)
P.append(Q("pld-q05", "A shopkeeper marks his goods 40% above the cost price and allows a discount of 10%. His profit per cent is:",
  ["24%", "26%", "28%", "30%"], 1, 26,
  md(r"$1.40 \times 0.90 = 1.26$ ⇒ profit **26%**."),
  "Chips 7/5 × 9/10 = 63/50 = 1.26.",
  "easy", "pl-marked-discount", "markup then discount", 30))

assert Fr(960, 20) * 100 == 4800
P.append(Q("pld-q06", "A man sells a scooter at a loss of 5%. Had he sold it for ₹960 more, he would have gained 15%. The cost price of the scooter is:",
  ["₹4,200", "₹4,500", "₹4,800", "₹5,000"], 2, 4800,
  md(r"The swing from $-5\%$ to $+15\%$ spans $20\%$ of CP.",
     r"$0.20 \times CP = 960$ ⇒ $CP = 4800$, i.e. ₹4,800."),
  "Difference of the two percentages = 20% of CP ⇒ 960/0.2 = 4,800.",
  "medium", "pl-basics", "price-shift CP", 40))

assert 1600 * Fr(8, 10) * Fr(7, 8) == 1120
P.append(Q("pld-q07", "The marked price of a sofa is ₹1,600. It is sold after two successive discounts of 20% and 12.5%. The selling price is:",
  ["₹1,080", "₹1,100", "₹1,120", "₹1,152"], 2, 1120,
  md(r"$1600 \times 0.80 = 1280$; $1280 \times 0.875 = 1120$."),
  "Chips: 1600 × 4/5 = 1,280; × 7/8 = 1,120.",
  "medium", "pl-successive", "successive discounts", 35))

assert 1000 * Fr(5, 4) * Fr(85, 100) == Fr(2125, 2)
P.append(Q("pld-q08", "An article costing ₹1,000 is marked 25% above cost and then sold at a 15% discount. The profit earned is:",
  ["₹50", "₹62.50", "₹75", "₹106.25"], 1, Fr(125, 2),
  md(r"$SP = 1000 \times 1.25 \times 0.85 = 1062.50$ ⇒ profit = **₹62.50**."),
  "1.25 × 0.85 = 1.0625 ⇒ profit 6.25% = ₹62.50.",
  "medium", "pl-marked-discount", "markup then discount", 35))

assert Fr(12, 10) / Fr(75, 100) == Fr(8, 5)
P.append(Q("pld-q09", "A trader allows a discount of 25% on the marked price and still gains 20%. The marked price is what per cent above the cost price?",
  ["40%", "50%", "55%", "60%"], 3, 60,
  md(r"$\frac{MP}{CP} = \frac{120}{75} = 1.6$ ⇒ **60%** above CP."),
  "MP/CP = (100+g)/(100−d) = 120/75 = 8/5.",
  "medium", "pl-marked-discount", "MP-discount-profit", 40))

assert Fr(90, 100) / Fr(80, 100) == Fr(9, 8)
P.append(Q("pld-q10", "A merchant claims to sell at a 10% loss but gives only 800 grams per kilogram. His actual gain or loss per cent is:",
  ["10% loss", "12.5% gain", "10% gain", "No loss, no gain"], 1, 12.5,
  md(r"Per true kg: he receives $0.90$ units of money and pays $0.80$.",
     r"Gain $= \frac{0.9 - 0.8}{0.8} \times 100 = 12.5\%$."),
  "Multiplier 0.9/0.8 = 9/8 ⇒ 12.5% gain despite the 'loss' claim.",
  "medium", "pl-dishonest", "claim + short weight", 40,
  vals=[-10, 12.5, 10, 0]))

assert F(160, 2560) == F(1, 16)
P.append(Q("pld-q11", "Two mobile phones are sold at ₹1,200 each — one at a profit of 25% and the other at a loss of 25%. The overall result is:",
  ["No profit, no loss", "6.25% loss", "6.25% profit", "12.5% loss"], 1, -6.25,
  md(r"Net loss% $= \frac{25^2}{100} = 6.25\%$.",
     r"Check: CPs $= 1200/1.25 = 960$ and $1200/0.75 = 1600$; total 2,560 vs SP 2,400 ⇒ loss 160 = 6.25%."),
  "x²/100 reflex: 625/100 = 6.25% loss.",
  "medium", "pl-same-price-cases", "same SP profit-loss", 40,
  vals=[0, -6.25, 6.25, -12.5]))

assert Fr(110, 90) - 1 == F(2, 9)
P.append(Q("pld-q12", "A dishonest dealer takes 10% more goods than he pays for while buying, and gives 10% less than the true weight while selling. His gain per cent is:",
  ["20%", "$22\\frac{2}{9}$%", "$21\\frac{1}{9}$%", "23%"], 1, F(200, 9),
  md(r"Multiplier $= \frac{110}{90} = \frac{11}{9}$ ⇒ gain $= \frac{2}{9} = 22\frac{2}{9}\%$."),
  "Both-ends chips: (100+b)/(100−s) = 110/90; never add 10 + 10.",
  "hard", "pl-dishonest", "cheat both ends", 45))

assert Fr(12, 10) * Fr(125, 100) * Fr(11, 10) == Fr(33, 20)
P.append(Q("pld-q13", "A manufacturer sells a TV to a wholesaler at 20% profit, the wholesaler sells it to a retailer at 25% profit, and the retailer sells it to a customer at 10% profit. If the customer pays ₹3,300, the manufacturing cost of the TV is:",
  ["₹1,800", "₹2,000", "₹2,200", "₹2,500"], 1, 2000,
  md(r"$\text{Cost} \times 1.2 \times 1.25 \times 1.1 = 3300$.",
     r"$1.2 \times 1.25 \times 1.1 = 1.65$ ⇒ Cost $= \frac{3300}{1.65} = 2000$, i.e. ₹2,000."),
  "Trade-chain chips multiply to 33/20 ⇒ divide 3,300 by 1.65.",
  "hard", "pl-marked-discount", "trade chain", 50))

assert 280 * F(185, 1000) == F(518, 10)
P.append(Q("pld-q14", "A man sells an article at a profit of 12.5%. Had he sold it for ₹51.80 less, he would have incurred a loss of 6%. The cost price of the article is:",
  ["₹250", "₹270", "₹280", "₹300"], 2, 280,
  md(r"The price difference spans $12.5\% - (-6\%) = 18.5\%$ of CP.",
     r"$0.185 \times CP = 51.80$ ⇒ $CP = 280$, i.e. ₹280."),
  "18.5% ↔ ₹51.80 ⇒ CP = 5180/18.5 = 280.",
  "hard", "pl-basics", "price-shift CP", 50))

assert F(140, 3500) == F(1, 25)
P.append(Q("pld-q15", "Two articles are sold at ₹1,680 each; one at a profit of 20% and the other at a loss of 20%. The net loss on the whole transaction is:",
  ["₹120", "₹140", "₹160", "₹180"], 1, 140,
  md(r"CPs: $\frac{1680}{1.2} = 1400$ and $\frac{1680}{0.8} = 2100$; total $= 3500$.",
     r"Total SP $= 3360$ ⇒ loss $= 140$, i.e. ₹140 (which is $\frac{20^2}{100} = 4\%$)."),
  "Reconstruct CPs (1,400 + 2,100); loss = 3,500 − 3,360 = ₹140.",
  "hard", "pl-same-price-cases", "same SP profit-loss", 50))

topic = {
 "id": "profit-loss-discount", "sectionId": "quant", "title": "Profit, Loss & Discount", "order": 8,
 "importance": "high", "avgQuestions": {"tier1": 2, "tier2": 3},
 "summary": "The highest-yield arithmetic block in Tier 1. CP–SP basics, successive discounts, the marked-price chain and dishonest-dealer cases appear in nearly every shift; Tier 2 layers on trade chains and price-shift comparisons. Everything reduces to multiplier chips.",
 "subtopics": subtopics, "pyqPatterns": pyq, "solvedExamples": solved, "practice": P,
}
write_topic(topic)
