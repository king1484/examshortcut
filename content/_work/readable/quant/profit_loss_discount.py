"""Readable rewrite of Profit, Loss & Discount (all five subtopics).

Simple English, one idea per section. Every number in every example is
recomputed below with exact fractions and asserted.
Run: python profit_loss_discount.py  (patches content/core/topics/quant/profit-loss-discount.json)
"""
import json
import re
from fractions import Fraction as F
from pathlib import Path

ROOT = Path(__file__).resolve().parents[3]
TOPIC = ROOT / "core" / "topics" / "quant" / "profit-loss-discount.json"

# ---------- answer checks: pl-basics ----------
assert 1400 - 1250 == 150 and F(150, 1250) * 100 == 12
assert 2400 + 150 == 2550
assert 1140 * F(20, 19) == 1200 and 624 * F(25, 24) == 650
assert F(14, 100) * 2400 == 336 and F(92, 100) * 2400 == 2208 and F(106, 100) * 2400 == 2544
assert 2544 - 2208 == 336
assert (720 + 560) == 2 * 640 and 720 - 640 == 80 and 640 - 560 == 80
assert F(15 - 12, 12) * 100 == 25
assert 4 * F(15, 4) == 15 and 4 * F(24, 5) == F(96, 5)
assert F(20 * 15, 4) == 75 and F(20 * 24, 5) == 96 and F(96 - 75, 75) * 100 == 28
assert 1530 * F(10, 9) == 1700 and 1700 * F(11, 10) == 1870
assert 600 * F(11, 10) == 660 and 600 * F(4, 5) * F(5, 4) == 600 and 660 - 60 == 600
assert 1020 - 850 == 170 and F(170, 850) == F(1, 5)

# ---------- answer checks: pl-successive ----------
assert 20 + 15 - F(20 * 15, 100) == 32
assert 10 + 20 - F(10 * 20, 100) == 28
assert 5000 * F(9, 10) * F(19, 20) == 4275
assert F(9, 10) * F(4, 5) * F(3, 4) == F(27, 50) and 100 - 54 == 46
assert 30 + 10 - F(30 * 10, 100) == 37 and F(3, 100) * 2400 == 72
assert 1600 * F(17, 20) == 1360 and F(1224, 1360) == F(9, 10)
assert F(5184, 6400) == F(81, 100) == F(9, 10) ** 2
assert F(13, 10) * F(9, 10) ** 2 == F(1053, 1000) and (F(1053, 1000) - 1) * 100 == F(53, 10)
assert 30000 * F(6, 5) * F(4, 5) == 28800 and 30000 - 28800 == 1200
assert F(115, 125) == F(23, 25) and (1 - F(23, 25)) * 100 == 8

# ---------- answer checks: pl-marked-discount ----------
assert 1000 - 900 == 100 and F(100, 1000) * 100 == 10 and F(100, 800) * 100 == F(25, 2)
assert F(14, 10) * F(9, 10) == F(63, 50) and (F(63, 50) - 1) * 100 == 26
assert F(117, 90) == F(13, 10)
assert 900 - 765 == 135 and F(135, 900) * 100 == 15
assert 800 * F(120, 80) == 1200 and 1200 * F(4, 5) == 960 == 800 * F(6, 5)
assert F(120, 75) == F(8, 5) and (F(8, 5) - 1) * 100 == 60 and F(3, 4) * 160 == 120
assert 4000 * F(5, 4) * F(6, 5) * F(11, 10) == 6600 and (F(6600, 4000) - 1) * 100 == 65
assert 2000 * F(6, 5) * F(5, 4) * F(11, 10) == 3300
assert 1200 * F(17, 20) == 1020
assert F(5, 4) * F(9, 10) == F(9, 8) and (F(9, 8) - 1) * 100 == F(25, 2)
assert 1275 * F(20, 17) == 1500 and 1275 * F(4, 5) == 1020
assert F(1, 5) * 100 == 20 and F(1, 20) * 100 == 5 and F(1, 6) * 100 == F(50, 3)
assert 1000 * F(5, 4) * F(17, 20) == F(2125, 2) and F(2125, 2) - 1000 == F(125, 2) and F(125, 2) / 1000 == F(1, 16)

# ---------- answer checks: pl-dishonest ----------
assert F(100, 900) * 100 == F(100, 9) == 11 + F(1, 9)
assert F(200, 800) * 100 == 25 and F(250, 750) * 100 == F(100, 3)
assert F(1000 * 100, 125) == 800
assert F(90, 80) == F(9, 8) and (F(9, 8) - 1) * 100 == F(25, 2)
assert F(80, 80) == 1
assert F(110, 90) == F(11, 9) and (F(11, 9) - 1) * 100 == F(200, 9) == 22 + F(2, 9)
assert F(110, 80) == F(11, 8) and (F(11, 8) - 1) * 100 == F(75, 2)
assert F(6, 5) * F(5, 4) == F(3, 2) and (F(3, 2) - 1) * 100 == 50

# ---------- answer checks: pl-same-price-cases ----------
assert F(625, 100) == F(25, 4)
assert 1200 * F(4, 5) == 960 and 1200 * F(4, 3) == 1600
assert 960 + 1600 == 2560 and 2 * 1200 == 2400 and 2560 - 2400 == 160
assert F(160, 2560) * 100 == F(25, 4)
assert 960 * F(5, 6) == 800 and 960 * F(5, 4) == 1200 and 2000 - 1920 == 80 and F(80, 2000) * 100 == 4
assert 1680 * F(5, 6) == 1400 and 1680 * F(5, 4) == 2100 and 3500 - 3360 == 140 and F(140, 3500) * 100 == 4
assert 1980 * F(10, 11) == 1800 and 1980 * F(10, 9) == 2200 and 4000 - 3960 == 40
assert 1155 * F(10, 11) == 1050 and 1155 * F(40, 33) == 1400 and 2450 - 2310 == 140
assert F(5, 6) + F(5, 4) == F(25, 12) and F(1, 12) * 600 == 50
assert 20 * 20 == 100 * 4 and 25 * 25 == 625
assert 25 * 25 == 625 and F(25, 4) * 100 == 625
assert F(1, 36) * 100 == F(25, 9) == 2 + F(7, 9)
assert F(100) * F(5, 6) == F(250, 3) and F(100) * F(5, 4) == 125
assert F(25) - F(50, 3) == F(25, 3) and F(250, 3) + 125 == F(625, 3)
assert F(25, 3) / F(625, 3) == F(1, 25)


def pat(pid, name, freq, spot, formula, steps, why, q, ex_steps, answer):
    return {"id": pid, "name": name, "frequency": freq, "howToSpot": spot, "formula": formula,
            "steps": steps, "why": why, "example": {"q": q, "steps": ex_steps, "answer": answer}}


# ================= pl-basics =================

PLB_CONCEPT = (
    "**Cost price (CP)** is what the seller paid; **selling price (SP)** is what the buyer pays. "
    "Profit means SP is above CP; loss means SP is below CP.\n\n"
    "Profit and loss per cent are always measured on CP. Turn each per cent into a multiplier: "
    "a profit of $20\\%$ means $SP = CP \\times \\dfrac{6}{5}$."
)

PLB_NOTES = r"""### The words you need
- **Cost price (CP)**: what the seller paid. Add transport or repair costs (overheads) to it.
- **Selling price (SP)**: what the buyer pays the seller.
- **Profit** = SP - CP when SP is bigger. **Loss** = CP - SP when SP is smaller.

A fan bought for Rs 1,250 and sold for Rs 1,400 gives a profit of Rs 150.

> **Rule:** Profit and loss per cent are always calculated on CP, unless the question clearly says otherwise.

### Profit and loss per cent
$$\text{Profit\%} = \frac{\text{Profit}}{CP} \times 100$$

For the fan: $\dfrac{150}{1250} \times 100 = 12\%$. Dividing by SP instead gives $10\dfrac{5}{7}\%$, the classic wrong option.

Overheads join the CP first: bought at 2,400 plus 150 transport makes CP 2,550.

### Multipliers, called chips
Profit of $x\%$ means $SP = CP \times \dfrac{100+x}{100}$. Loss of $x\%$ means $SP = CP \times \dfrac{100-x}{100}$.

| Change | Chip | | Change | Chip |
|---|---|---|---|---|
| $20\%$ profit | $6/5$ | | $10\%$ loss | $9/10$ |
| $25\%$ profit | $5/4$ | | $12.5\%$ loss | $7/8$ |
| $16\dfrac{2}{3}\%$ profit | $7/6$ | | $5\%$ loss | $19/20$ |

Going back from SP to CP, divide by the chip. A table sold for 1,140 at a $5\%$ loss: $CP = 1140 \times \dfrac{20}{19} = 1200$.

> **Tip:** Write every per cent as a chip fraction before touching the rupees.

### Two selling prices, one cost price
"Sold at $8\%$ loss; had it been sold for Rs 336 more, the gain would be $6\%$."

1. The two SPs are $92\%$ and $106\%$ of the same CP.
2. Their gap is $8 + 6 = 14\%$ of CP, and it equals Rs 336.
3. $14\%$ of CP $= 336$, so CP $= 2400$.

> **Example:** Selling at Rs 720 gives as much profit as the loss on selling at Rs 560. CP sits exactly midway: $\dfrac{720+560}{2} = 640$.

> **Watch:** Loss and gain percents add when one SP is below CP and the other above it; two gains subtract.

### Counting articles instead of rupees
"The CP of 15 articles equals the SP of 12." The seller receives money for 15 by giving goods that cost him 12. Profit $= \dfrac{15-12}{12} \times 100 = 25\%$.

"Buys 4 for Rs 15 and sells 5 for Rs 24": take 20 articles, the common count. CP $= 75$, SP $= 96$, profit $= 28\%$.

> **Watch:** Divide by the articles he gives away, not the number named first.

### Changed cost and changed price together
"A man sells at $10\%$ profit. Had he bought at $20\%$ less and sold for Rs 60 less, he would gain $25\%$. Find the CP."

1. Let CP $= C$. First story: $SP = 1.1C$.
2. Second story: $CP = 0.8C$ and $SP = 0.8C \times 1.25 = C$.
3. So $1.1C - 60 = C$, giving $0.1C = 60$ and $C = 600$.

> **Careful:** Always rebuild the SP from your CP as a final check. Exam numbers come out whole; if yours do not, re-read the question.
"""

PLB_FORMULAS = [
    {"name": "Profit / loss per cent", "tex": r"\text{P\%} = \frac{SP - CP}{CP} \times 100", "note": "Always on CP."},
    {"name": "Selling price", "tex": r"SP = CP \times \frac{100 \pm x}{100}", "note": "Plus for profit, minus for loss."},
    {"name": "Cost price from SP", "tex": r"CP = SP \times \frac{100}{100 \pm x}", "note": "Divide by the chip."},
    {"name": "Equal profit and loss at two prices", "tex": r"CP = \frac{S_1 + S_2}{2}", "note": "When profit at S1 equals loss at S2."},
]

PLB_TRICKS = [
    {
        "title": "Fraction swap for the per cent",
        "body": "Turn the profit into a fraction of CP and the per cent falls out. $170/850$ is clearly $1/5$.",
        "example": {
            "q": "A trader sells a cycle for Rs 1,020 that cost him Rs 850. Find the profit per cent.",
            "steps": [r"Profit $= 1020 - 850 = 170$.", r"$\dfrac{170}{850} = \dfrac{1}{5} = 20\%$."],
            "answer": "20%",
        },
    },
    {
        "title": "Divide by the chip to get CP",
        "body": "A loss of $4\%$ means the chip $96/100$. Divide the SP by the chip, nothing else.",
        "example": {
            "q": "A machine is sold for Rs 624 at a loss of 4%. Find its cost price.",
            "steps": [r"Loss $4\%$: chip $= \dfrac{96}{100} = \dfrac{24}{25}$.", r"$CP = 624 \times \dfrac{25}{24} = 650$."],
            "answer": "Rs 650",
        },
    },
    {
        "title": "Same per cent scales linearly",
        "body": "When the profit per cent is fixed, CP and SP scale together. Article counts often hide a clean ratio.",
        "example": {
            "q": "By selling 15 pens a shopkeeper recovers the cost of 12 pens. Find his gain per cent.",
            "steps": [r"He gets money for 15 pens by giving 12.", r"Gain $= \dfrac{3}{12} = 25\%$."],
            "answer": "25%",
        },
    },
]

PLB_MISTAKES = [
    {"wrong": "Working out the profit per cent on SP.", "right": "Profit and loss per cent are always on CP."},
    {"wrong": "Recovering CP as SP minus $x\%$ of SP.", "right": "Undo the chip: $CP = SP \\times \\dfrac{100}{100 \\pm x}$."},
    {"wrong": "Forgetting transport or repair in the CP.", "right": "Add all overheads to the buying price first."},
    {"wrong": "In article-count sums, dividing by the wrong count.", "right": "Divide the extra articles by the articles given away."},
    {"wrong": "Reading 'gain of $25\%$' and 'marked $25\%$ up' as the same thing.", "right": "Gain compares SP with CP; markup compares MP with CP. Different quantities."},
]

PLB_REVISION = [
    "Profit $=$ SP $-$ CP; loss $=$ CP $-$ SP.",
    "Profit and loss per cent are always on CP (plus overheads).",
    "SP $=$ CP $\\times$ chip; CP $=$ SP $\\div$ chip.",
    "Two SPs: rupee gap $=$ per cent gap of CP.",
    "Equal profit and loss at two prices: CP is the average.",
    "CP of $a$ articles $=$ SP of $b$: profit $= \\dfrac{a-b}{b} \\times 100$.",
]

PLB_PATTERNS = [
    pat("pl-b1", "Profit or loss per cent from CP and SP", "very common",
        "CP and SP are given, sometimes with a transport or repair cost, and the per cent is asked.",
        r"\text{Profit\%} = \frac{SP - CP}{CP} \times 100",
        ["Add any overheads to the CP.", "Find profit or loss = SP - CP.",
         "Divide by CP, never by SP.", "Multiply by 100."],
        "Profit is measured against the money the seller actually invested.",
        "A fan bought for Rs 1,250 is sold for Rs 1,400. Find the profit per cent.",
        [r"Profit $= 1400 - 1250 = 150$.", r"$\dfrac{150}{1250} \times 100 = 12$."],
        "12%"),
    pat("pl-b2", "Find CP or SP from a profit or loss per cent", "very common",
        "One price and the per cent are given; the other price is asked.",
        r"SP = CP \times \frac{100 \pm x}{100}, \quad CP = SP \times \frac{100}{100 \pm x}",
        ["Write the chip for the per cent.", "CP to SP: multiply. SP to CP: divide.",
         "Reduce the chip to a small fraction for speed."],
        "SP is CP scaled by the chip, so reversing the journey divides.",
        "A table sold for Rs 1,140 gives a loss of 5%. Find its cost price.",
        [r"Loss $5\%$: chip $= \dfrac{19}{20}$.", r"$CP = 1140 \times \dfrac{20}{19} = 1200$."],
        "Rs 1,200"),
    pat("pl-b3", "Two selling prices around one CP", "very common",
        "'Sold at a% loss; had it been sold for Rs k more, the gain would be b%.'",
        r"CP = \frac{k \times 100}{a + b}",
        ["Write both SPs as percents of the CP.", "Add the percents (loss and gain on opposite sides).",
         "That per cent of CP equals the rupee gap k.", "Divide to find CP."],
        "Both SPs are percents of the same CP, so only the per cent gap moves the SP.",
        "An article sold at 8% loss would have given a 6% gain if sold for Rs 336 more. Find the cost price.",
        [r"Percents: $92\%$ and $106\%$; gap $= 14\%$ of CP.", r"$14\%$ of CP $= 336$.", r"$CP = 336 \times \dfrac{100}{14} = 2400$."],
        "Rs 2,400"),
    pat("pl-b4", "Article-count questions", "common",
        "'CP of 15 articles equals SP of 12', or rates like 'buys 4 for Rs 15 and sells 5 for Rs 24'.",
        r"\text{Profit\%} = \frac{\text{articles bought} - \text{articles sold}}{\text{articles sold}} \times 100",
        ["For 'CP of a = SP of b', take the price of one article as 1.", "Profit per cent = (a - b) over b, times 100.",
         "For rates like 4-for-15, take the LCM of the counts so both sides cover the same number of articles."],
        "Fixing a common count turns the story into an ordinary CP-SP comparison.",
        "The cost price of 15 articles is equal to the selling price of 12 articles. Find the profit per cent.",
        [r"He receives 15 article-prices for goods costing 12.", r"$\dfrac{15 - 12}{12} \times 100 = 25$."],
        "25%"),
    pat("pl-b5", "New selling price for a different gain", "common",
        "'Sold for Rs 1,530 at 10% loss; at what price should it be sold to gain 10%?'",
        r"SP_2 = SP_1 \times \frac{100 + b}{100 - a}",
        ["Go back to the CP by dividing by the first chip.", "Multiply by the new chip for the wanted gain.",
         "For a changed CP as well, write both stories with CP as the unknown and equate."],
        "The CP is the anchor that links every selling story.",
        "An article sold for Rs 1,530 gives a loss of 10%. At what price should it be sold to gain 10%?",
        [r"$CP = 1530 \times \dfrac{10}{9} = 1700$.", r"$SP = 1700 \times \dfrac{11}{10} = 1870$."],
        "Rs 1,870"),
    pat("pl-b6", "Equal profit and loss at two prices", "common",
        "'Selling at Rs 720 gives as much profit as the loss on selling at Rs 560.' The CP is asked.",
        r"CP = \frac{S_1 + S_2}{2}",
        ["Note the two selling prices, one above and one below the CP.", "Equal profit and loss puts the CP exactly midway.",
         "Average the two prices."],
        "The two prices sit at equal distances from the CP, so the CP is their average.",
        "Selling an article at Rs 720 gives as much profit as the loss on selling it at Rs 560. Find the cost price.",
        [r"CP is midway between 560 and 720.", r"$CP = \dfrac{560 + 720}{2} = 640$.", r"Check: $720 - 640 = 80 = 640 - 560$."],
        "Rs 640"),
]

# ================= pl-successive =================

PLS_CONCEPT = (
    "Successive changes happen one after another, and the second change works on the value the first one left. "
    "So two changes never simply add: discounts of $20\\%$ and $10\\%$ equal one discount of $28\\%$.\n\n"
    "The safe method: write what fraction of the price each change **keeps**, and multiply."
)

PLS_NOTES = r"""### What successive means
A shop cuts a bill by $20\%$, then gives $10\%$ more off the reduced bill. The second $10\%$ falls on the smaller amount left after the first cut.

So the total discount is less than $20 + 10 = 30\%$. It is actually $28\%$.

> **Rule:** Each new change works on the value left by the previous change, never on the original price.

### Two changes: a + b + ab/100
For two changes of $a\%$ and $b\%$ (use a minus sign for a fall):

$$\text{net} = a + b + \frac{ab}{100}$$

For two **discounts** $d_1$ and $d_2$ the kept-fraction version becomes:

$$\text{single discount} = d_1 + d_2 - \frac{d_1 d_2}{100}$$

$20\%$ and $15\%$: $35 - 3 = 32\%$. $10\%$ and $20\%$: $30 - 2 = 28\%$.

> **Careful:** Never add discounts directly. $10\% + 20\% = 30\%$ is the trap option.

### Chips work for any number of changes
A discount of $d\%$ keeps $\dfrac{100-d}{100}$ of the price. Multiply the kept fractions.

Three discounts of $10\%$, $20\%$, $25\%$: $\dfrac{9}{10} \times \dfrac{4}{5} \times \dfrac{3}{4} = \dfrac{27}{50}$. The customer pays $54\%$, so the single discount is $46\%$, not $55\%$.

A marked price of Rs 5,000 with $10\%$ and $5\%$ off: $5000 \times \dfrac{9}{10} \times \dfrac{19}{20} = 4275$.

> **Tip:** The order of the changes does not matter. Multiply in whatever order is easiest.

### Comparing two offers
"Flat $40\%$" against "$30\%$ then $10\%$": the second is $30 + 10 - 3 = 37\%$. The flat offer is better by $3\%$ of the bill.

If that difference is Rs 72, the bill is $72 \div \dfrac{3}{100} = 2400$.

> **Note:** A single discount always beats successive discounts that add up to the same number.

### Finding a missing discount
MP Rs 1,600, first discount $15\%$, final price Rs 1,224.

1. After $15\%$: $1600 \times \dfrac{17}{20} = 1360$.
2. Second discount: $\dfrac{1360 - 1224}{1360} = \dfrac{136}{1360} = 10\%$.

Two equal discounts take Rs 6,400 to Rs 5,184: kept $= \dfrac{5184}{6400} = \dfrac{81}{100} = \left(\dfrac{9}{10}\right)^2$, so each discount is $10\%$.

> **Watch:** The second discount is a per cent of the price after the first discount, never of the MP.

### A rise and then a fall
A price raised $20\%$ then cut $20\%$ ends $4\%$ lower: $\dfrac{6}{5} \times \dfrac{4}{5} = \dfrac{24}{25}$.

A TV priced Rs 30,000 goes to Rs 36,000, then to Rs 28,800. The final price is Rs 1,200 below the original.

An article marked $30\%$ above CP and sold after two $10\%$ discounts: $\dfrac{13}{10} \times \dfrac{9}{10} \times \dfrac{9}{10} = 1.053$, a profit of $5.3\%$.

> **Example:** After a rise of $25\%$ a value was changed again and ended $15\%$ up overall. Second change: $\dfrac{115}{125} = \dfrac{23}{25}$, a cut of $8\%$.
"""

PLS_FORMULAS = [
    {"name": "Two successive changes", "tex": r"\text{net} = a + b + \frac{ab}{100}", "note": "Use negative b for a fall."},
    {"name": "Same change twice (rise)", "tex": r"2x + \frac{x^2}{100}"},
    {"name": "Same change twice (fall)", "tex": r"2x - \frac{x^2}{100}"},
    {"name": "Equivalent single discount", "tex": r"D = d_1 + d_2 - \frac{d_1 d_2}{100}", "note": "For two discounts."},
    {"name": "Kept fraction", "tex": r"\text{kept} = \prod \frac{100 - d_i}{100}", "note": "Any number of discounts; customer pays this share."},
]

PLS_TRICKS = [
    {
        "title": "Multiply the chips",
        "body": "Chips handle any mix of rises and falls, in any order, and extend to three or more changes.",
        "example": {
            "q": "A price is increased by 20% and the new price is then decreased by 10%. Find the net change.",
            "steps": [r"$\dfrac{6}{5} \times \dfrac{9}{10} = \dfrac{27}{25}$.", r"$1.08$ means a net rise of $8\%$."],
            "answer": "8% increase",
        },
    },
    {
        "title": "One line for two discounts",
        "body": "Two discounts collapse with $d_1 + d_2 - \\dfrac{d_1 d_2}{100}$. One line, no chips.",
        "example": {
            "q": "Find the single discount equal to successive discounts of 20% and 10%.",
            "steps": [r"$20 + 10 - \dfrac{20 \times 10}{100}$", r"$= 30 - 2 = 28$."],
            "answer": "28%",
        },
    },
    {
        "title": "Work backwards for the missing change",
        "body": "Net chip divided by the known chip gives the unknown chip.",
        "example": {
            "q": "After a rise of 25%, a value was changed again and ended 15% up overall. Find the second change.",
            "steps": [r"Net chip $= \dfrac{23}{20}$, first chip $= \dfrac{5}{4}$.", r"$\dfrac{23}{20} \div \dfrac{5}{4} = \dfrac{23}{25}$, a fall of $8\%$."],
            "answer": "8% decrease",
        },
    },
]

PLS_MISTAKES = [
    {"wrong": "Adding discounts: $20\% + 10\% = 30\%$.",
     "right": "Use $d_1 + d_2 - \\dfrac{d_1 d_2}{100} = 28\\%$."},
    {"wrong": "Applying the second discount to the original marked price.",
     "right": "The second discount falls on the already reduced price."},
    {"wrong": "Writing $+\\dfrac{ab}{100}$ for a rise followed by a fall.",
     "right": "Give b a minus sign when it is a fall."},
    {"wrong": "Using the two-change formula once for three discounts.",
     "right": "Multiply three kept fractions instead."},
    {"wrong": "Believing the order of discounts changes the answer.",
     "right": "Chips multiply; multiplication order does not matter."},
]

PLS_REVISION = [
    "Each change acts on what the last one left.",
    "Two changes: $a + b + \\dfrac{ab}{100}$ with signs.",
    "Two discounts: $d_1 + d_2 - \\dfrac{d_1 d_2}{100}$.",
    "Any number of changes: multiply the kept fractions.",
    "Up $x\%$ then down $x\%$: net fall of $\\dfrac{x^2}{100}\%$.",
    "Missing change: net chip $\\div$ known chip.",
]

PLS_PATTERNS = [
    pat("pl-s1", "Equivalent single discount", "very common",
        "'Successive discounts of 20% and 15% equal a single discount of?' Two or three discounts, no rupees.",
        r"d = d_1 + d_2 - \frac{d_1 d_2}{100}",
        ["For two discounts, use the one-line formula.", "For three or more, multiply kept fractions and subtract from 100%.",
         "Check the answer is less than the plain sum."],
        "Each later discount acts on an already reduced price.",
        "Find a single discount equivalent to successive discounts of 20% and 15%.",
        [r"$20 + 15 - \dfrac{20 \times 15}{100}$.", r"$= 35 - 3 = 32$."],
        "32%"),
    pat("pl-s2", "Price after successive discounts", "very common",
        "A marked price and two or three discounts are given; the price paid is asked.",
        r"SP = MP \times \frac{100 - d_1}{100} \times \frac{100 - d_2}{100}",
        ["Write each discount as a kept fraction.", "Multiply the MP by all the kept fractions.",
         "Cancel before multiplying."],
        "Every discount scales the running price by its kept fraction.",
        "The marked price of an article is Rs 5,000 and discounts of 10% and 5% are given. What does the customer pay?",
        [r"Kept fractions: $\dfrac{9}{10}$ and $\dfrac{19}{20}$.", r"$5000 \times \dfrac{9}{10} = 4500$.", r"$4500 \times \dfrac{19}{20} = 4275$."],
        "Rs 4,275"),
    pat("pl-s3", "Flat discount versus successive discounts", "common",
        "A flat per cent is compared with two successive percents, often through a rupee difference.",
        r"\text{difference} = (\text{single} - \text{equivalent})\% \text{ of the price}",
        ["Convert the successive discounts to one equivalent discount.", "Subtract it from the flat discount.",
         "That gap, as a per cent of the bill, gives the rupee difference."],
        "Both offers start from the same price, so only the per cent gap matters.",
        "The difference between a 40% flat discount and successive discounts of 30% and 10% on a bill is Rs 72. Find the bill.",
        [r"Successive $= 30 + 10 - 3 = 37\%$.", r"Gap $= 3\%$ of the bill $= 72$.", r"Bill $= 72 \times \dfrac{100}{3} = 2400$."],
        "Rs 2,400"),
    pat("pl-s4", "Find a missing discount", "common",
        "MP, the final price and one discount are given (or 'two equal discounts'); the other discount is asked.",
        r"\frac{100 - d_2}{100} = \frac{SP}{MP \times \frac{100 - d_1}{100}}",
        ["Apply the known discount to the MP.", "Divide the final price by that reduced price to get the second kept fraction.",
         "For two equal discounts, take the square root of SP over MP."],
        "The second discount is a per cent of the price after the first.",
        "An article marked Rs 1,600 is sold for Rs 1,224 after two discounts, the first being 15%. Find the second discount.",
        [r"After $15\%$: $1600 \times \dfrac{17}{20} = 1360$.", r"$\dfrac{1224}{1360} = \dfrac{9}{10}$, so the second discount is $10\%$."],
        "10%"),
    pat("pl-s5", "Markup followed by cuts", "common",
        "'Marked 30% above CP, then two discounts of 10%' or 'increased 20% then decreased 20%'; profit or net change asked.",
        r"\text{net} = a + b + \frac{ab}{100} \ \text{or multiply all chips}",
        ["Write every rise and fall as a chip.", "Multiply the chips.",
         "Subtract 1 for the net change; same x up and down loses $\dfrac{x^2}{100}$ per cent."],
        "The second change acts on a different base from the first, so chips must multiply.",
        "An article is marked 30% above its cost price and sold after successive discounts of 10% and 10%. Find the profit per cent.",
        [r"Chips: $\dfrac{13}{10} \times \dfrac{9}{10} \times \dfrac{9}{10}$.", r"$= \dfrac{1053}{1000} = 1.053$.", r"Profit $= 5.3\%$."],
        "5.3%"),
]

# ================= pl-marked-discount =================

PLM_CONCEPT = (
    "The label price is the **marked price (MP)**. The seller marks CP up to MP, then cuts MP by a **discount** to reach SP.\n\n"
    "Discount per cent is on MP; profit per cent is on CP. Multiply one chip per step: markup chip, then discount chip."
)

PLM_NOTES = r"""### The chain: CP to MP to SP
A shopkeeper does not sell at cost. He writes a higher price on the label, then offers a discount on it.

$$\text{Discount} = MP - SP, \qquad \text{Discount\% on MP}$$

Buy at Rs 800, tag at Rs 1,000, sell at Rs 900. The discount is Rs 100, which is $10\%$ of MP. The profit is Rs 100, which is $12.5\%$ of CP. Same hundred rupees, two different percents.

> **Rule:** Discount per cent is on MP; profit per cent is on CP. Never mix the two bases.

### The master relation
$$MP = CP \times \frac{100 + g}{100 - d}$$

Here $g$ is the final gain per cent and $d$ the discount per cent. Any two of markup, discount and gain fix the third.

Marked $40\%$ above CP with a $10\%$ discount: $\dfrac{14}{10} \times \dfrac{9}{10} = 1.26$, a profit of $26\%$.

"What markup allows a $10\%$ discount and still gains $17\%$?" $\dfrac{117}{90} = 1.3$, so mark $30\%$ above CP.

### One chain, any missing link
- Marked Rs 1,200, sold at $15\%$ off: $SP = 1200 \times \dfrac{17}{20} = 1020$.
- Marked $25\%$ above CP, discount $10\%$: $\dfrac{5}{4} \times \dfrac{9}{10} = \dfrac{9}{8}$, a gain of $12.5\%$.
- SP Rs 1,275 after a $15\%$ discount and a $25\%$ profit: $MP = 1275 \times \dfrac{20}{17} = 1500$ and $CP = 1275 \times \dfrac{4}{5} = 1020$.

> **Tip:** Exam numbers come out whole. If yours do not, re-read the question before doubting the method.

### Multi-level trade chains
Manufacturer to wholesaler to retailer to customer: each stage multiplies its own chip on **its own purchase price**.

A TV costs Rs 4,000 to make. The maker sells at $25\%$ profit, the wholesaler at $20\%$, the retailer at $10\%$:

$$4000 \times \frac{5}{4} \times \frac{6}{5} \times \frac{11}{10} = 6600$$

The customer pays $65\%$ above the making cost. To work backwards, divide by the chips in reverse order.

> **Watch:** Never add the markups. $25 + 20 + 10 = 55\%$ is the trap; multiply chips to get $65\%$.

### Free-item offers
- "Buy 5, get 1 free": pay for 5, receive 6. Discount $= \dfrac{1}{6} = 16\dfrac{2}{3}\%$.
- "Buy 4, get 1 free": discount $= \dfrac{1}{5} = 20\%$.
- "Buy 19, get 1 free": discount $= \dfrac{1}{20} = 5\%$.

> **Key:** Discount $=$ free items $\div$ items received. The free item counts in what you receive, not what you pay for.

### Flat against successive
A flat $40\%$ leaves $\dfrac{60}{100}$ of the price. Successive $30\%$ and $10\%$ leave $\dfrac{7}{10} \times \dfrac{9}{10} = \dfrac{63}{100}$.

The flat offer is always better for the buyer when the numbers add up the same.
"""

PLM_FORMULAS = [
    {"name": "Discount per cent", "tex": r"\text{D\%} = \frac{MP - SP}{MP} \times 100", "note": "On the marked price."},
    {"name": "Marked price for a target gain", "tex": r"MP = CP \times \frac{100 + g}{100 - d}", "note": "g = gain%, d = discount%."},
    {"name": "SP through the chain", "tex": r"SP = CP\left(1 + \frac{m}{100}\right)\left(1 - \frac{d}{100}\right)", "note": "m = markup%."},
    {"name": "Markup per cent", "tex": r"\text{markup\%} = \left(\frac{100+g}{100-d} - 1\right) \times 100"},
    {"name": "Multi-level markups", "tex": r"\text{final} = \text{cost} \times \prod \frac{100 + x_k}{100}", "note": "One chip per trader."},
    {"name": "Free-item discount", "tex": r"\text{discount\%} = \frac{\text{free}}{\text{received}} \times 100"},
]

PLM_TRICKS = [
    {
        "title": "Build the MP-over-CP ratio",
        "body": "Gain $g\%$ and discount $d\%$ together fix MP as a multiple of CP: $\\dfrac{100+g}{100-d}$.",
        "example": {
            "q": "After allowing a 10% discount a trader still gains 20%. The marked price is what per cent above cost?",
            "steps": [r"$\dfrac{MP}{CP} = \dfrac{120}{90} = \dfrac{4}{3}$.", r"Markup $= 33\dfrac{1}{3}\%$."],
            "answer": "33 1/3% above CP",
        },
    },
    {
        "title": "Markup chip then discount chip",
        "body": "Two fractions give the whole story from CP to SP in one line.",
        "example": {
            "q": "An article costing Rs 1,000 is marked 25% above cost and sold at a 15% discount. Find the profit per cent.",
            "steps": [r"$SP = 1000 \times \dfrac{5}{4} \times \dfrac{17}{20} = 1062.50$.", r"Profit $= \dfrac{62.5}{1000} = 6.25\%$."],
            "answer": "6.25%",
        },
    },
    {
        "title": "Trade chains multiply",
        "body": "One chip per middleman. Work backwards from the final price by dividing in reverse order.",
        "example": {
            "q": "A manufacturer sells to a wholesaler at 20% profit, the wholesaler to a retailer at 25% profit, and the retailer to a customer at 10% profit. The customer pays Rs 3,300. Find the manufacturing cost.",
            "steps": [r"Chips: $\dfrac{6}{5} \times \dfrac{5}{4} \times \dfrac{11}{10}$.", r"$3300 \div \left(\dfrac{6}{5} \times \dfrac{5}{4} \times \dfrac{11}{10}\right) = 2000$."],
            "answer": "Rs 2,000",
        },
    },
]

PLM_MISTAKES = [
    {"wrong": "Taking the discount per cent on CP.",
     "right": "The discount always acts on the marked price."},
    {"wrong": "Markup minus discount: $40\%$ up, $10\%$ off called $30\%$ up.",
     "right": "Multiply: $\\dfrac{14}{10} \\times \\dfrac{9}{10} = 1.26$, so $26\%$ up."},
    {"wrong": "Adding chain markups: $20 + 25 + 10 = 55\%$.",
     "right": "Multiply chips: $1.2 \\times 1.25 \\times 1.1 = 1.65$, a $65\%$ rise."},
    {"wrong": "Taking every trader's profit on the manufacturer's cost.",
     "right": "Each stage's per cent is on its own purchase price."},
    {"wrong": "Reading 'buy 4 get 1 free' as a $25\%$ discount.",
     "right": "Discount is $\\dfrac{1}{5} = 20\\%$, free over received."},
]

PLM_REVISION = [
    "Discount per cent on MP; profit per cent on CP.",
    "$MP = CP \\times \\dfrac{100+g}{100-d}$.",
    "Markup $\\% = \\left(\\dfrac{100+g}{100-d} - 1\\right) \\times 100$.",
    "Chains: one chip per stage, multiply; backwards, divide in reverse.",
    "Free items: discount $=$ free $\\div$ received.",
    "Flat beats successive discounts of the same total.",
]

PLM_PATTERNS = [
    pat("pl-m1", "Discount per cent from MP and SP", "very common",
        "MP and SP (or the discount in rupees) are given; the discount per cent or amount is asked.",
        r"\text{Discount\%} = \frac{MP - SP}{MP} \times 100",
        ["Discount = MP - SP.", "Divide by MP, never by SP or CP.", "Multiply by 100 for the per cent."],
        "A discount is a cut offered on the tagged price, so MP is the base.",
        "An article marked Rs 900 is sold for Rs 765. Find the discount per cent.",
        [r"Discount $= 900 - 765 = 135$.", r"$\dfrac{135}{900} \times 100 = 15$."],
        "15%"),
    pat("pl-m2", "Marked price for a target profit after discount", "very common",
        "'At what price should he mark the article to allow a d% discount and still gain g%?'",
        r"MP = CP \times \frac{100 + g}{100 - d}",
        ["Write the chain CP x markup chip x discount chip = SP.", "Set SP to the wanted gain chip of CP.",
         "Divide by the discount chip to get MP."],
        "The MP must absorb both the discount and the desired gain.",
        "An article costing Rs 800 is to be sold at a 20% discount and still gain 20%. Find the marked price.",
        [r"$MP = 800 \times \dfrac{120}{80} = 1200$.", r"Check: $1200 \times \dfrac{4}{5} = 960 = 800 \times \dfrac{6}{5}$."],
        "Rs 1,200"),
    pat("pl-m3", "Markup per cent from discount and profit", "very common",
        "'Allows a d% discount and still gains g%. The marked price is what per cent above cost?'",
        r"\text{markup\%} = \left(\frac{100+g}{100-d} - 1\right) \times 100",
        ["Compute the ratio of 100+g to 100-d.", "Subtract 1 and multiply by 100.",
         "Trace CP = 100 through MP to SP as a check."],
        "The ratio of MP to CP depends only on the two percents.",
        "A trader allows a 25% discount on the marked price and still gains 20%. The marked price is what per cent above the cost price?",
        [r"$\dfrac{120}{75} = \dfrac{8}{5}$.", r"Markup $= \dfrac{3}{5} \times 100 = 60\%$.", r"Check: CP 100, MP 160, SP $= \dfrac{3}{4} \times 160 = 120$."],
        "60%"),
    pat("pl-m4", "Multi-level trade chain", "common",
        "Manufacturer to wholesaler to retailer to customer, each at his own profit per cent.",
        r"\text{final} = \text{cost} \times \prod \frac{100 + x_i}{100}",
        ["Write each stage's chip.", "Multiply all chips with the base cost.",
         "Working from the final price, divide by the chips in reverse order."],
        "Every stage treats its buying price as its own cost.",
        "A manufacturer sells a TV to a wholesaler at 25% profit, the wholesaler to a retailer at 20% profit, and the retailer to a customer at 10% profit. If it cost Rs 4,000 to make, what does the customer pay?",
        [r"Chips: $\dfrac{5}{4}, \dfrac{6}{5}, \dfrac{11}{10}$.", r"$4000 \times \dfrac{5}{4} = 5000$, then $6000$, then $6600$.", r"Total rise $= 65\%$."],
        "Rs 6,600 (65% above cost)"),
    pat("pl-m5", "Free-item and flat offers", "common",
        "'Buy 5 get 1 free', 'pay for 12 take 14', or comparing a scheme with a flat discount.",
        r"\text{discount\%} = \frac{\text{free items}}{\text{items received}} \times 100",
        ["Count what the customer pays for and what he receives.", "Discount per cent = free over received, times 100.",
         "Compare schemes by the kept fraction, not the label."],
        "The seller spreads the cost of the free items over the whole batch.",
        "A shop offers 'buy 4 get 1 free' on pens. What discount per cent is this?",
        [r"Pay for 4, receive 5.", r"Discount $= \dfrac{1}{5} \times 100 = 20\%$."],
        "20%"),
]

# ================= pl-dishonest =================

PLD_CONCEPT = (
    "A dishonest dealer cheats on the **quantity**, not the printed price. He charges for a full kilogram but hands over less.\n\n"
    "Compare what he charges for with what he actually gives. "
    "Gain per cent $=$ (goods charged $-$ goods given) $\\div$ goods given $\\times 100$."
)

PLD_NOTES = r"""### The idea
A dealer sells rice "at cost price" but uses a 900 g weight for every kilogram. His price looks honest; his scale is not.

To judge him, put two numbers side by side: what he charges for (1000 g) and what he gives (900 g).

> **Rule:** Gain per cent $= \dfrac{\text{charged} - \text{given}}{\text{given}} \times 100$. The base is what he gives.

### False weight at cost price
He uses $w$ grams in place of a true $W$ grams (usually $W = 1000$ g):

$$\text{gain\%} = \frac{W - w}{w} \times 100$$

- 900 g per kg: $\dfrac{100}{900} = 11\dfrac{1}{9}\%$
- 800 g per kg: $\dfrac{200}{800} = 25\%$
- 750 g per kg: $\dfrac{250}{750} = 33\dfrac{1}{3}\%$

His cost covers only the 900 g that left the shop, while he was paid for 1000 g. That is why the base is $w$.

> **Watch:** Dividing by $W$ instead of $w$ gives $10\%$ instead of $11\dfrac{1}{9}\%$. That wrong answer is always sitting in the options.

### The reverse: gain given, find the weight
A dealer gains $25\%$ while selling at cost price. Then $\dfrac{1000 - w}{w} = \dfrac{1}{4}$, so $w = 800$ g.

In general $w = W \times \dfrac{100}{100 + \text{gain\%}}$. The answer always lands below the true weight.

> **Tip:** If your $w$ comes out above 1000 g, you flipped the fraction.

### Claims a loss, gives short weight
"Claims to sell at a $10\%$ loss but gives only 800 g per kg."

He charges $90\%$ of the true kilo price for every 800 g he hands over:

$$\frac{100 - L}{100 - c} = \frac{90}{80} = 1.125$$

So he truly gains $12.5\%$. An equal claim and shortfall, like a claimed $20\%$ loss with $20\%$ short weight, gives exactly no profit and no loss.

> **Careful:** A claimed loss can hide a real gain. Always check the weight.

### Cheating at both ends
He takes $b\%$ extra goods while buying and gives $s\%$ less while selling, all at cost price:

$$\text{multiplier} = \frac{100 + b}{100 - s}$$

$10\%$ extra in, $10\%$ short out: $\dfrac{110}{90} = \dfrac{11}{9}$, a gain of $22\dfrac{2}{9}\%$.

Pulse seller's version: he pays for 100 kg but takes 110 kg; later he charges for 100 kg but hands over 90 kg. Per rupee paid, received $\div$ given $= \dfrac{110}{90}$. Same multiplier, no rupee arithmetic needed.

### Short weight plus a price rise
He uses an 800 g weight **and** sells $20\%$ above cost. Price chip $\dfrac{6}{5}$, weight chip $\dfrac{1000}{800} = \dfrac{5}{4}$:

$$\frac{6}{5} \times \frac{5}{4} = \frac{3}{2} \Rightarrow 50\% \text{ gain}$$

> **Example:** Two cheats acting together multiply. Charging more per false kilo and giving less per true kilo are independent.
"""

PLD_FORMULAS = [
    {"name": "False weight gain", "tex": r"\text{gain\%} = \frac{W - w}{w} \times 100", "note": "W = true weight, w = weight used; divide by w."},
    {"name": "Weight from a given gain", "tex": r"w = W \times \frac{100}{100 + \text{gain\%}}"},
    {"name": "Claimed loss with short weight", "tex": r"\text{multiplier} = \frac{100 - L}{100 - c}", "note": "L = claimed loss%, c = short weight%."},
    {"name": "Cheat at both ends", "tex": r"\text{multiplier} = \frac{100 + b}{100 - s}", "note": "b = extra taken while buying, s = shortfall while selling."},
    {"name": "True gain from multiplier", "tex": r"\text{gain\%} = (\text{multiplier} - 1) \times 100"},
]

PLD_TRICKS = [
    {
        "title": "The W minus w over w rule",
        "body": "At cost price, the only question is which weight goes below the line. It is the weight he gives.",
        "example": {
            "q": "A shopkeeper sells rice at cost price but uses a 900 g weight for 1 kg. Find his gain per cent.",
            "steps": [r"$\dfrac{1000 - 900}{900} \times 100$.", r"$= \dfrac{100}{900} \times 100 = 11\dfrac{1}{9}\%$."],
            "answer": "11 1/9%",
        },
    },
    {
        "title": "A claimed loss can still be a gain",
        "body": "Judge money per true gram, not per claimed gram.",
        "example": {
            "q": "A merchant claims to sell at a 10% loss but gives only 800 g per kg. Find his true result.",
            "steps": [r"Per true kg he charges $0.9$ of the kilo price.", r"Per true kg he gives goods worth $0.8$.", r"$\dfrac{0.9}{0.8} = 1.125$, a $12.5\%$ gain."],
            "answer": "12.5% gain",
        },
    },
    {
        "title": "Both-ends multiplier",
        "body": "Buy-side chip over sell-side chip. Two fractions, one division.",
        "example": {
            "q": "A dealer takes 10% extra goods while buying and gives 10% less than the true weight while selling. Find his gain per cent.",
            "steps": [r"$\dfrac{110}{90} = \dfrac{11}{9}$.", r"$\dfrac{2}{9} \times 100 = 22\dfrac{2}{9}$."],
            "answer": "22 2/9% gain",
        },
    },
]

PLD_MISTAKES = [
    {"wrong": "Dividing by the true weight: $\\dfrac{100}{1000} = 10\%$.",
     "right": "Divide by the weight given: $\\dfrac{100}{900} = 11\\dfrac{1}{9}\%$."},
    {"wrong": "Believing a claimed loss without checking the weight.",
     "right": "Compute the multiplier $\\dfrac{100-L}{100-c}$ first."},
    {"wrong": "Adding the two cheats: $10\% + 10\% = 20\%$.",
     "right": "Multiply chips: $\\dfrac{110}{90} \\Rightarrow 22\\dfrac{2}{9}\%$."},
    {"wrong": "Calling an equal claim and shortfall a profit.",
     "right": "A claimed loss of L% with exactly L% short weight is exactly break-even."},
    {"wrong": "Losing track of which side each cheat helps.",
     "right": "He gains at both ends: extra goods coming in, short goods going out."},
]

PLD_REVISION = [
    "False weight at CP: gain $= \\dfrac{W-w}{w} \\times 100$, base $w$.",
    "From gain to weight: $w = W \\times \\dfrac{100}{100 + g}$.",
    "Claimed loss with short weight: $\\dfrac{100-L}{100-c} - 1$.",
    "Both ends: $\\dfrac{100+b}{100-s} - 1$.",
    "Equal claim and shortfall $\\Rightarrow$ zero profit.",
    "Weight cheat and price cheat multiply as chips.",
]

PLD_PATTERNS = [
    pat("pl-d1", "False weight sold at cost price", "very common",
        "'Sells at cost price but uses a weight of 900 g for 1 kg.' The gain per cent is asked.",
        r"\text{gain\%} = \frac{W - w}{w} \times 100",
        ["Take the true weight W and the false weight w.", "Gain = (W - w) over w, times 100.",
         "Sanity check: smaller w means bigger gain."],
        "His cost is for the w grams he gave; his income is for W grams.",
        "A shopkeeper sells sugar at cost price but uses a weight of 900 g in place of 1 kg. Find his gain per cent.",
        [r"$\dfrac{1000 - 900}{900} \times 100 = \dfrac{100}{900} \times 100$.", r"$= 11\dfrac{1}{9}$."],
        "11 1/9%"),
    pat("pl-d2", "Gain given, find the false weight", "common",
        "'He gains 25% while selling at cost price. What weight does he give for a kilogram?'",
        r"w = W \times \frac{100}{100 + \text{gain\%}}",
        ["Write the gain as a fraction: 25% = 1/4.", "Solve (1000 - w) over w equals 1/4.",
         "The answer must be below the true weight."],
        "The gain fraction fixes the ratio of true to false weight.",
        "A dishonest dealer sells at cost price and still gains 25%. What weight does he give in place of 1 kg?",
        [r"$w = 1000 \times \dfrac{100}{125}$.", r"$= 800$ g."],
        "800 g"),
    pat("pl-d3", "Claimed loss with short weight", "common",
        "'Claims a loss of L% but gives c% less weight.' The true gain or loss is asked.",
        r"\text{gain\%} = \left(\frac{100 - L}{100 - c} - 1\right) \times 100",
        ["Write the price he charges per true kilo: (100 - L)%.", "Write the worth of goods he gives: (100 - c)%.",
         "Divide the first by the second."],
        "He collects the loss-price of a full kilo but supplies only part of it.",
        "A merchant claims to sell at a 10% loss but gives only 800 g per kg. What is his true gain or loss per cent?",
        [r"$\dfrac{90}{80} = \dfrac{9}{8}$.", r"$\dfrac{1}{8} = 12.5\%$ gain."],
        "12.5% gain"),
    pat("pl-d4", "Cheating while buying and selling", "common",
        "'Takes 10% extra while buying and gives 10% less while selling, at cost price.'",
        r"\text{gain\%} = \left(\frac{100 + b}{100 - s} - 1\right) \times 100",
        ["Buying b% extra means he owns (100 + b) units per 100 paid for.", "Selling s% short means each 100 units sold cost him (100 - s).",
         "Divide and subtract 1."],
        "The two cheats act at different stages, so they multiply.",
        "A dealer takes 10% extra goods while buying and gives 10% less while selling, all at cost price. Find his gain per cent.",
        [r"$\dfrac{110}{90} = \dfrac{11}{9}$.", r"$\dfrac{2}{9} \times 100 = 22\dfrac{2}{9}$."],
        "22 2/9%"),
    pat("pl-d5", "False weight plus a higher price", "occasional",
        "The dealer both uses a short weight and sells above cost price.",
        r"\text{gain\%} = \left(\text{price chip} \times \frac{W}{w} - 1\right) \times 100",
        ["Write the price chip for the markup.", "Write the weight ratio W over w.", "Multiply the two and subtract 1."],
        "Charging more per false kilo and giving less per true kilo are independent chips.",
        "A seller uses an 800 g weight in place of 1 kg and sells 20% above cost price. Find his gain per cent.",
        [r"Price chip $\dfrac{6}{5}$, weight ratio $\dfrac{5}{4}$.", r"$\dfrac{6}{5} \times \dfrac{5}{4} = \dfrac{3}{2}$.", r"Gain $= 50\%$."],
        "50%"),
]

# ================= pl-same-price-cases =================

PLQ_CONCEPT = (
    "Two articles sell at the **same price**. One makes $x\\%$ profit, the other $x\\%$ loss. "
    "The result is always a **net loss** of $\\dfrac{x^2}{100}$ per cent.\n\n"
    "The loss article's cost price is the bigger one, so its loss outweighs the profit. "
    "For rupee answers, rebuild each cost price by dividing the common SP by its chip."
)

PLQ_NOTES = r"""### The setup
Two articles are sold for the same price. One carries a profit of $x\%$, the other a loss of $x\%$.

Most students guess "no profit, no loss". The answer is always a net loss.

> **Rule:** Net loss $= \dfrac{x^2}{100}$ per cent of the total cost price.

### Quick values worth memorising
- $x = 10$: loss $1\%$
- $x = 20$: loss $4\%$
- $x = 25$: loss $6.25\%$
- $x = 16\dfrac{2}{3}\% = \dfrac{1}{6}$: loss $\left(\dfrac{1}{6}\right)^2 = \dfrac{1}{36} = 2\dfrac{7}{9}\%$

> **Watch:** "No profit, no loss" is the trap option. It is always wrong here.

### Why the loss always wins
Take a common SP of Rs 100 and $x = 20$.

- Profit article: $CP = 100 \div \dfrac{6}{5} = 83\dfrac{1}{3}$, gain $= 16\dfrac{2}{3}$.
- Loss article: $CP = 100 \div \dfrac{4}{5} = 125$, loss $= 25$.

The loss (Rs 25) beats the gain (Rs $16\dfrac{2}{3}$). The gap, Rs $8\dfrac{1}{3}$, is exactly $4\%$ of the total CP Rs $208\dfrac{1}{3}$. Dividing by a chip below 1 always moves further than dividing by one above 1.

### Full reconstruction in rupees
When rupees are asked, rebuild both cost prices.

Two watches sell at Rs 960 each, at $20\%$ profit and $20\%$ loss:

1. $CP_1 = 960 \times \dfrac{5}{6} = 800$, $CP_2 = 960 \times \dfrac{5}{4} = 1200$.
2. Total CP $= 2000$, total SP $= 1920$.
3. Loss $= 80 = 4\%$ of 2000. The formula agrees.

Other quick cases: Rs 1,680 each gives CPs 1,400 and 2,100, loss Rs 140. Rs 1,980 each at $\pm 10\%$ gives CPs 1,800 and 2,200, loss Rs 40.

> **Tip:** The loss per cent depends only on $x$. Change the SP and the per cent does not move.

### Unequal percentages break the shortcut
One article at $10\%$ profit, the other at $17.5\%$ loss, both at Rs 1,155.

$CP$s: $1155 \times \dfrac{10}{11} = 1050$ and $1155 \times \dfrac{40}{33} = 1400$. Total CP 2,450, total SP 2,310, loss Rs 140.

> **Careful:** Use $\dfrac{x^2}{100}$ only when the two percents are equal in size.

### Working backwards from the loss
Total loss Rs 50 with $\pm 20\%$ on the same SP:

$$\frac{5S}{6} + \frac{5S}{4} = \frac{25S}{12}, \quad \text{loss} = \frac{S}{12} = 50 \Rightarrow S = 600$$

Given only the loss per cent, find $x$: $x^2 = 100 \times \text{loss\%}$, so $x = 10\sqrt{\text{loss\%}}$. A $4\%$ loss means $x = 20$; a $6.25\%$ loss means $x = 25$.

> **Note:** The loss item's CP is always the bigger one. If your rebuild says otherwise, you inverted a chip.

### How the options are built
- "No profit, no loss" - the instinct answer, always wrong.
- $\dfrac{x^2}{200}\%$ - half the correct loss.
- $\dfrac{2x^2}{100}\%$ - double the correct loss.
- $\dfrac{x^2}{100}\%$ - the correct answer.

One rupee option usually applies the loss per cent to the SP instead of the total CP. Check the base before choosing.
"""

PLQ_FORMULAS = [
    {"name": "Net loss for equal plus-minus x%", "tex": r"\text{net loss\%} = \frac{x^2}{100}", "note": "Per cent of total CP."},
    {"name": "Reconstructed costs", "tex": r"CP_1 = \frac{S}{1 + x/100}, \quad CP_2 = \frac{S}{1 - x/100}", "note": "S = common selling price."},
    {"name": "Loss in rupees", "tex": r"\text{loss} = CP_1 + CP_2 - 2S"},
    {"name": "x from the loss per cent", "tex": r"x = 10\sqrt{\text{loss\%}}"},
]

PLQ_TRICKS = [
    {
        "title": "The x squared over 100 reflex",
        "body": "Same SP, opposite equal percents: write the loss per cent straight away.",
        "example": {
            "q": "Two mobiles are sold for Rs 1,200 each, one at 25% profit and the other at 25% loss. Find the overall loss per cent.",
            "steps": [r"Loss $= \dfrac{25 \times 25}{100}$.", r"$= 6.25\%$. (CPs 960 and 1,600; loss Rs 160 of 2,560.)"],
            "answer": "6.25% loss",
        },
    },
    {
        "title": "Rebuild both cost prices",
        "body": "Divide the common SP by each chip, add the CPs, compare with twice the SP.",
        "example": {
            "q": "Two articles are sold for Rs 1,680 each, one at 20% profit and the other at 20% loss. Find the net loss in rupees.",
            "steps": [r"CPs: $1680 \times \dfrac{5}{6} = 1400$ and $1680 \times \dfrac{5}{4} = 2100$.", r"Total CP 3,500 vs total SP 3,360.", r"Loss $= 140$, which is $4\%$ of 3,500."],
            "answer": "Rs 140 (4%)",
        },
    },
]

PLQ_MISTAKES = [
    {"wrong": "Answering 'no profit no loss' because $+x$ and $-x$ cancel.",
     "right": "The percents act on different CPs; the result is always a loss of $\\dfrac{x^2}{100}\%$."},
    {"wrong": "Using $\\dfrac{x^2}{100}$ when the percents are unequal.",
     "right": "Rebuild both CPs from the SP and add."},
    {"wrong": "Reporting the loss per cent as the rupee loss.",
     "right": "Rupee loss $=$ total CP $-$ total SP; the per cent is on total CP."},
    {"wrong": "Dividing both SPs by the same chip.",
     "right": "Profit item by $1 + \\dfrac{x}{100}$; loss item by $1 - \\dfrac{x}{100}$."},
    {"wrong": "Applying the loss per cent to the total SP.",
     "right": "Loss per cent is measured on the total cost price."},
]

PLQ_REVISION = [
    "Equal $\\pm x\%$ on the same SP: loss $\\dfrac{x^2}{100}\%$.",
    "10 $\\to$ 1, 20 $\\to$ 4, 25 $\\to$ 6.25 per cent loss.",
    "CPs: divide the common SP by $1 \\pm \\dfrac{x}{100}$.",
    "Loss item's CP is always the bigger one.",
    "Unequal percents: rebuild both CPs, no shortcut.",
    "From loss per cent back to x: $x = 10\\sqrt{\\text{loss\\%}}$.",
]

PLQ_PATTERNS = [
    pat("pl-q1", "Net result for equal gain and loss on one SP", "very common",
        "'Two articles sold at the same price, one at x% profit and the other at x% loss. Overall result?'",
        r"\text{net loss\%} = \frac{x^2}{100}",
        ["Square x and divide by 100.", "State it as a loss, never a gain.",
         "Reject the 'no profit no loss' option."],
        "The loss side has the bigger CP, so its per cent dominates.",
        "Two articles are sold at the same price, one at 25% profit and the other at 25% loss. What is the net result?",
        [r"Loss $= \dfrac{25^2}{100} = \dfrac{625}{100}$.", r"$= 6.25\%$ of the total CP."],
        "6.25% loss"),
    pat("pl-q2", "Loss in rupees by rebuilding both CPs", "very common",
        "The common SP is given in rupees; the total loss or total CP is asked.",
        r"\text{loss} = \left(\frac{S}{1 + x/100} + \frac{S}{1 - x/100}\right) - 2S",
        ["Divide the SP by the profit chip for one CP.", "Divide by the loss chip for the other.",
         "Add the CPs, subtract twice the SP.", "Check: loss over total CP equals x squared over 100."],
        "Rupee answers need the actual cost prices, which the SP recovers.",
        "Two mobiles are sold at Rs 960 each, one at 20% profit and the other at 20% loss. Find the total loss.",
        [r"CPs: $960 \times \dfrac{5}{6} = 800$ and $960 \times \dfrac{5}{4} = 1200$.", r"Total CP $= 2000$, total SP $= 1920$.", r"Loss $= 80 = 4\%$ of 2000."],
        "Rs 80 (4% loss)"),
    pat("pl-q3", "Same SP with unequal percents", "common",
        "One at a% profit, the other at b% loss with a not equal to b, same SP.",
        r"\text{loss} = \left(\frac{S}{1 + a/100} + \frac{S}{1 - b/100}\right) - 2S",
        ["Build each CP from the SP with its own chip.", "Add the CPs and compare with twice the SP.",
         "Divide by the total CP for the per cent."],
        "Unequal percents break the x-squared shortcut, so rebuild.",
        "Two tables are sold at Rs 1,155 each, one at a 10% profit and the other at a 17.5% loss. Find the net result.",
        [r"CPs: $1155 \times \dfrac{10}{11} = 1050$ and $1155 \times \dfrac{40}{33} = 1400$.", r"Total CP $= 2450$, total SP $= 2310$.", r"Loss $= 140$."],
        "Rs 140 loss"),
    pat("pl-q4", "Find the common SP from the loss", "occasional",
        "The total loss in rupees is given; the common selling price is asked.",
        r"\text{loss} = \frac{x^2 S}{10000 - x^2}",
        ["Write both CPs in terms of S.", "Total CP minus 2S is the loss.", "Set it equal to the rupee loss and solve for S."],
        "The rupee loss is a fixed fraction of the total CP, so it fixes S.",
        "Two articles are sold at the same price, one at 20% profit and the other at 20% loss. The total loss is Rs 50. Find the selling price of each article.",
        [r"CP total $= \dfrac{5S}{6} + \dfrac{5S}{4} = \dfrac{25S}{12}$.", r"Loss $= \dfrac{S}{12} = 50$.", r"$S = 600$."],
        "Rs 600"),
    pat("pl-q5", "Find x from the loss per cent", "occasional",
        "The overall loss per cent is given and the equal profit and loss per cent x is asked.",
        r"x = 10\sqrt{\text{loss\%}}",
        ["Write x squared over 100 equal to the loss per cent.", "Take the square root.", "Multiply by 10."],
        "The loss per cent is x squared over 100, so the square root reverses it.",
        "Two articles sold at the same price, one at x% profit and the other at x% loss, give an overall loss of 4%. Find x.",
        [r"$\dfrac{x^2}{100} = 4$.", r"$x^2 = 400$.", r"$x = 20$."],
        "20%"),
]

# ================= write back =================

dfrac = lambda x: x.replace(r"\frac", r"\dfrac")

BLOCKS = [
    ("pl-basics", dict(concept=PLB_CONCEPT, notes=PLB_NOTES, formulas=PLB_FORMULAS,
                       tricks=PLB_TRICKS, mistakes=PLB_MISTAKES, revision=PLB_REVISION, patterns=PLB_PATTERNS)),
    ("pl-successive", dict(concept=PLS_CONCEPT, notes=PLS_NOTES, formulas=PLS_FORMULAS,
                           tricks=PLS_TRICKS, mistakes=PLS_MISTAKES, revision=PLS_REVISION, patterns=PLS_PATTERNS)),
    ("pl-marked-discount", dict(concept=PLM_CONCEPT, notes=PLM_NOTES, formulas=PLM_FORMULAS,
                                tricks=PLM_TRICKS, mistakes=PLM_MISTAKES, revision=PLM_REVISION, patterns=PLM_PATTERNS)),
    ("pl-dishonest", dict(concept=PLD_CONCEPT, notes=PLD_NOTES, formulas=PLD_FORMULAS,
                          tricks=PLD_TRICKS, mistakes=PLD_MISTAKES, revision=PLD_REVISION, patterns=PLD_PATTERNS)),
    ("pl-same-price-cases", dict(concept=PLQ_CONCEPT, notes=PLQ_NOTES, formulas=PLQ_FORMULAS,
                                 tricks=PLQ_TRICKS, mistakes=PLQ_MISTAKES, revision=PLQ_REVISION, patterns=PLQ_PATTERNS)),
]

data = json.loads(TOPIC.read_text(encoding="utf-8"))
for sid, block in BLOCKS:
    sub = next(s for s in data["subtopics"] if s["id"] == sid)
    patterns = block["patterns"]
    old_ids = {p["id"] for p in sub.get("patterns", [])}
    new_ids = {p["id"] for p in patterns}
    assert old_ids <= new_ids, (sid, old_ids - new_ids)
    all_other = {p["id"] for s in data["subtopics"] if s["id"] != sid for p in s.get("patterns", [])}
    assert not (all_other & new_ids), (sid, all_other & new_ids)
    notes = block["notes"].strip() + "\n"
    assert 2500 <= len(notes) <= 5000, (sid, len(notes))
    assert 4 <= len(re.findall(r"^### ", notes, re.M)) <= 8, sid
    block.update(notes=notes, mistakes=[{k: dfrac(v) for k, v in m.items()} for m in block["mistakes"]],
                 revision=[dfrac(r) for r in block["revision"]])
    sub.update(**block)
    print(f"{sid}: notes {len(notes)} chars, {len(patterns)} patterns (was {len(old_ids)})")

file_ids = [p["id"] for s in data["subtopics"] for p in s.get("patterns", [])]
assert len(file_ids) == len(set(file_ids)), "duplicate pattern ids in file"
TOPIC.write_text(json.dumps(data, ensure_ascii=False, indent=1) + "\n", encoding="utf-8")
print("profit-loss-discount.json updated")
