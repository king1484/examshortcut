"""Phase-2 deep content for quant/mixture-alligation — replacement, ratio-profit, mixtures-of-mixtures."""
import os
import sys
from fractions import Fraction as F

sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
from _lib import Sub, num, rs, mixed


def P(x):
    x = F(x)
    return (num(x) if x.denominator in (1, 2, 4, 5, 8, 10, 16, 20, 25, 40, 50, 100) else mixed(x)) + "%"


# --- arithmetic behind every answer (verified before any build) ---
assert 80 * F(9, 10) ** 2 == F(324, 5)                      # 64.8 L
assert 40 * F(9, 10) ** 3 == F(729, 25)                     # 29.16 L
assert 60 - 12 == 48 and 48 * 4 == 12 * 16                  # 4:1
assert 60 * F(4, 5) ** 2 == F(192, 5) and F(192, 5) * 9 == F(108, 5) * 16  # 38.4 : 21.6 = 16:9
assert 50 * F(4, 5) ** 2 == 32                              # x = 10 reverse case
assert 100 * F(3, 4) ** 2 == F(225, 4) and F(225, 4) * 7 == F(175, 4) * 9  # 56.25 : 43.75 = 9:7
assert F(16, 81) == F(2, 3) ** 4 and 8 * 3 == 24            # cask 16:65 -> 24 L
assert F(42, 38) == F(21, 19) and 80 * F(7, 10) - 14 == 42  # 21:19
assert F(42, 8) == F(21, 4) and 50 * F(4, 5) - 8 + 10 == 42  # 21:4
assert F(88, 32) == F(11, 4) and 40 * F(2, 3) - F(16, 3) + 8 == F(88, 3)   # 11:4
assert F(1, 5) * 100 == 20 and F(25, 75) * 100 == F(100, 3)  # water gains
assert F(1, 6) * 100 == F(50, 3) and F(25, 100) == F(1, 4)    # ratios from gains
assert (2 * 30 + 3 * 40) / 5 == 36 and 45 * 4 == 36 * 5      # rice blend 25%
assert (40 * 25 + 10 * 35) / 50 == 27 and 27 * F(5, 4) == F(135, 4)        # 33.75
assert (120 * 1 + 60 * 2) / 3 == 80 and 120 / F(3, 2) == 80  # ghee:oil 1:2
assert (80 * 24 + 40 * 36) / 120 == 28 and 28 * F(5, 4) == 35              # rice SP 35
assert 250 * F(3, 2) * F(4, 5) == 300                        # tea net 20%
assert F(9, 8) ** 2 - 1 == F(17, 64)                         # 8:1 mixture gain 26.5625%


def build_replacement():
    S = Sub("mix-replacement")
    S.notes = r"""### The repeated-replacement formula
A vessel holds C litres of pure milk (or any component). x litres are drawn out and replaced with water; this is done n times. Because the mixture is uniform, each operation removes **the same fraction** $\frac{x}{C}$ of whatever is in the vessel. After n rounds the milk left is
$$\text{milk} = C\left(1 - \frac{x}{C}\right)^n$$
80 L, 8 L drawn and replaced, twice: $80 \times \left(\frac{9}{10}\right)^2 = 64.8$ L. The water is simply $C - \text{milk}$ (the total never changes when you replace what you remove).

### Why the fraction form works
Each operation multiplies the remaining milk by $\left(1 - \frac{x}{C}\right)$ — the milk is drawn proportionally, the water topping-up adds no milk. Multiplying is why powers appear; the same one-liner handles two, three or four rounds without any table.

### One operation only
A single draw-replace needs no formula: subtract x litres of the component directly, add x of the other. From 60 L of milk, remove 12 L, add water: milk 48, water 12 → 4:1. A second operation then multiplies by $\frac{48}{60}$: milk $= 48 \times \frac{48}{60} = 38.4$ → ratio $16:9$. Note $\frac{48}{60} = 1 - \frac{12}{60}$ — consistent with the formula.

### Removing from a mixed vessel
If the vessel is *already* a mixture in ratio m:w, a draw of x litres takes each component in proportion — the **ratio inside the vessel is unchanged**; only the volume shrinks. Adding anything afterwards is what shifts the ratio. From milk:water 7:3 in 80 L (56, 24), remove 20 L (14, 6) — still 7:3 in 60 L; add 20 L water → 42:38.

### Reverse problems
Given the final quantity, extract x or n:
- $C\left(1-\frac{x}{C}\right)^2 = 32$ with C = 50 → $\left(1-\frac{x}{50}\right)^2 = \frac{16}{25}$ → $x = 10$ L.
- Final ratio gives the fraction: wine : water 16:65 → wine fraction $\frac{16}{81} = \left(\frac{2}{3}\right)^4$ → four operations with $\frac{x}{C} = \frac{1}{3}$.
Take roots — square for two operations, fourth root for four — and match against perfect powers.

### Common slips
- Subtracting x litres of milk every round even after the vessel is diluted (that is the $\left(1-\frac{x}{C}\right)^n$ trap).
- Forgetting the *total stays C* when you replace, so 'milk : water' pairs milk with $C - $ milk.
- Using addition instead of multiplication across rounds.

### Quick revision
- $n$ rounds: milk $= C\left(1-\frac{x}{C}\right)^n$; water $= C -$ milk.
- One round: plain subtraction; two rounds: multiply twice.
- Drawing from a uniform mixture preserves its internal ratio.
- Reverse: match the final fraction to a perfect power.
- Total is constant when you replace what you remove.
"""

    S.pattern("mix-p1", "Repeated replacement (formula)", "very common",
              "x litres drawn and replaced with water, n times, from C litres of pure milk/wine — find what remains.",
              r"\text{left} = C\left(1 - \frac{x}{C}\right)^n",
              r"""1. Compute the kept fraction $1 - \frac{x}{C}$.
2. Raise it to the number of operations.
3. Multiply by C; water = C − milk if asked.

Why: each round removes the same *fraction* of whatever milk is present.""",
              "A vessel contains 80 litres of pure milk. 8 litres are drawn and replaced with water, and the operation is repeated once more. Find the milk left.",
              r"$80 \times \left(\frac{9}{10}\right)^2 = 64.8$ litres.")
    S.pattern("mix-p2", "One or two draws — ratio form", "very common",
              "A single draw-replace, or a second round from the diluted vessel — find the final ratio.",
              r"\text{after round 2: } \frac{\text{milk}}{\text{water}} = \left(1-\frac{x}{C}\right)^2 : \left[1-\left(1-\frac{x}{C}\right)^2\right]",
              r"""1. Round 1: subtract x litres of milk, add x water — read the ratio.
2. Round 2: multiply the milk by the kept fraction again.
3. Pair the final milk with (C − milk).

Why: only milk keeps shrinking; water absorbs the difference.""",
              "From 60 litres of pure milk, 12 litres are removed and replaced with water. Find the ratio of milk to water now.",
              r"Milk 48, water 12 → 4:1.")
    S.pattern("mix-p3", "Reverse — find x or the capacity", "common",
              "The final quantity or ratio is given; find the drawn amount x, the capacity C, or the number of rounds.",
              r"\left(1-\frac{x}{C}\right)^n = \frac{\text{final fraction}}{1}",
              r"""1. Divide the final milk by C to get the kept fraction.
2. Take the n-th root and match to a perfect power.
3. Solve $1 - \frac{x}{C} = $ root for the unknown.

Why: the formula is invertible once you spot the power.""",
              "A cask full of wine: 8 litres drawn and replaced with water, the operation performed three more times. Wine : water is finally 16 : 65. Find the capacity.",
              r"Wine fraction $= \frac{16}{81} = \left(\frac{2}{3}\right)^4$ → $1 - \frac{8}{C} = \frac{2}{3}$ → C = 24 litres.")
    S.pattern("mix-p4", "Drawing from an already-mixed vessel", "common",
              "The vessel starts as a mixture (not pure); a draw is followed by an addition.",
              r"\text{draw splits components in the vessel's own ratio}",
              r"""1. Convert the starting ratio to litres of each component.
2. Remove x litres split in that ratio — the ratio is unchanged.
3. Add the new ingredient to the required column and re-ratio.

Why: a uniform mixture yields its components proportionally.""",
              "80 litres of a milk-water mixture in ratio 7:3 has 20 litres drawn off, then 20 litres of water added. Find the new ratio.",
              r"Start 56, 24; draw removes 14, 6 → 42, 18; add 20 water → 42:38 = 21:19.")
    S.pattern("mix-p5", "Replace with the same component (enriching)", "occasional",
              "Mixture loses some of one component and is topped up with the *other* one — ratios tighten instead of dilute.",
              r"\text{remove in ratio, then add the pure component}",
              r"""1. Split the removed volume by the current ratio.
2. Subtract from the matching columns; the total dips by x.
3. Add x litres of the topping component to its column.

Why: the topping-up choice decides which column swells.""",
              "From 50 litres of a milk-water mixture in ratio 4:1, 10 litres are removed and replaced with pure milk. Find the new ratio.",
              r"Draw removes 8 milk, 2 water → 32, 8; add 10 milk → 42:8 = 21:4.")

    S.q("mix-p1", "medium",
        "A vessel contains 80 litres of pure milk. 8 litres are drawn out and replaced with water, and this operation is repeated once more. The quantity of milk left is:",
        ["64.8 litres", "64 litres", "72 litres", "66.4 litres"], "64.8 litres",
        r"$80 \times \left(\frac{9}{10}\right)^2 = 64.8$ L.",
        "64 L subtracts 8 L twice — the second draw takes milk *and* water.", 30)
    S.q("mix-p1", "hard",
        "A cask has 40 litres of pure milk. 4 litres are drawn and replaced with water; this is done 3 times in all. The milk remaining is:",
        ["29.16 litres", "28 litres", "30 litres", "29.6 litres"], "29.16 litres",
        r"$40 \times \left(\frac{9}{10}\right)^3 = \frac{29160}{1000} = 29.16$ L.",
        r"Three rounds → the kept fraction cubed, not $40 - 3 \times 4$.", 40)
    S.q("mix-p2", "easy",
        "From a vessel full of 60 litres of pure milk, 12 litres are taken out and replaced by water. The ratio of milk to water in the vessel now is:",
        ["4:1", "5:1", "3:1", "2:1"], "4:1",
        r"Milk $= 48$, water $= 12$ → $4:1$.",
        "The total is still 60 — milk pairs with the water that filled in.", 25)
    S.q("mix-p2", "hard",
        "From 60 litres of pure milk, 12 litres are drawn and replaced with water; then 12 litres of the mixture are drawn and replaced with water again. The final ratio of milk to water is:",
        ["16:9", "4:1", "25:11", "3:2"], "16:9",
        r"Milk $= 60\left(\frac{48}{60}\right)^2 = 38.4$; water $= 21.6$ → $38.4:21.6 = 16:9$.",
        r"$\left(\frac{4}{5}\right)^2 = \frac{16}{25}$ of the vessel is milk — water takes the other 9 parts.", 40)
    S.q("mix-p3", "hard",
        "A vessel has 50 litres of pure milk. x litres are drawn and replaced with water, and the operation is performed twice. If 32 litres of milk remain, x is:",
        ["10 litres", "5 litres", "12.5 litres", "8 litres"], "10 litres",
        r"$50\left(1-\frac{x}{50}\right)^2 = 32$ → $\left(1-\frac{x}{50}\right)^2 = \frac{16}{25}$ → $1-\frac{x}{50} = \frac{4}{5}$ → $x = 10$ L.",
        r"Match $\frac{32}{50} = \frac{16}{25}$ to $\left(\frac{4}{5}\right)^2$ — two rounds, square root.", 45)
    S.q("mix-p3", "medium",
        "100 litres of pure milk loses 25 litres to a draw, which is replaced with water; then a second 25-litre draw is replaced with water. The ratio of milk to water now is:",
        ["9:7", "3:1", "1:1", "7:5"], "9:7",
        r"Milk $= 100\left(\frac{3}{4}\right)^2 = 56.25$; water $= 43.75$ → $56.25:43.75 = 9:7$.",
        r"$\left(\frac{3}{4}\right)^2 = \frac{9}{16}$ milk → 16 parts total, 9 milk : 7 water.", 35)
    S.q("mix-p4", "hard",
        "A cask is full of wine. 8 litres are drawn and replaced with water; the operation is performed three more times. The ratio of wine to water is finally 16:65. The capacity of the cask is:",
        ["24 litres", "32 litres", "48 litres", "64 litres"], "24 litres",
        r"Wine fraction $= \frac{16}{81} = \left(\frac{2}{3}\right)^4$ → $1-\frac{8}{C} = \frac{2}{3}$ → $C = 24$ L.",
        r"Four operations in all → fourth root; 16:65 pairs wine with water, so use $\frac{16}{81}$.", 45)
    S.q("mix-p4", "medium",
        "80 litres of a milk-water mixture in the ratio 7:3 has 20 litres drawn off and replaced by water. The new ratio of milk to water is:",
        ["21:19", "7:3", "3:2", "2:1"], "21:19",
        r"Start 56, 24 → draw removes 14, 6 → 42, 18; add 20 water → $42:38 = 21:19$.",
        "The draw itself keeps 7:3 inside the 20 litres.", 35)
    S.q("mix-p5", "hard",
        "From 50 litres of a milk-water mixture in the ratio 4:1, 10 litres are removed and replaced with pure milk. The new ratio of milk to water is:",
        ["21:4", "4:1", "5:1", "9:2"], "21:4",
        r"Draw removes 8 milk, 2 water → 32, 8; add 10 milk → $42:8 = 21:4$.",
        "Here the milk column *grows* — the replacement is milk, not water.", 40)
    S.q("mix-p5", "medium",
        "A vessel has 40 litres of milk and water in the ratio 2:1. 8 litres of the mixture are removed and 8 litres of pure milk are added. The new ratio of milk to water is:",
        ["11:4", "2:1", "3:1", "7:2"], "11:4",
        r"Milk $\frac{80}{3}$, water $\frac{40}{3}$; the draw removes $\frac{16}{3}$ milk and $\frac{8}{3}$ water → $\frac{64}{3}$, $\frac{32}{3}$; add 8 milk → $\frac{88}{3}:\frac{32}{3} = 11:4$.",
        r"Work in thirds: the draw splits 8 litres as $5\frac{1}{3}$ and $2\frac{2}{3}$.", 40)
    return S


def build_ratioprofit():
    S = Sub("mix-ratio-profit")
    S.notes = r"""### Water sells for nothing — that is the whole trick
A milkman adds water to milk and sells the blend **at the cost price of milk**: every litre sold brings milk-price rupees, but part of the litre cost him nothing. His gain comes purely from the free water.
$$\text{gain\%} = \frac{\text{water}}{\text{milk}} \times 100$$
Water : milk 1:5 → gain 20%. Water is 25% *of the mixture* → milk is 75%, so gain $= \frac{25}{75} = 33\frac{1}{3}\%$. The two readings differ; the formula uses water per unit **milk**.

### Working backwards
For a target gain g%, set $\frac{W}{M} = \frac{g}{100}$: to gain 25%, water : milk = 1:4 (one litre of water per four of milk). To gain $16\frac{2}{3}\%$, $W : M = 1:6$. Options often include the inverted ratio and the mixture-fraction misread — compute, don't guess.

### Blends that must earn a profit
When two real ingredients are mixed, the blend's **cost price per kg** is the weighted mean:
$$CP = \frac{q_1 c_1 + q_2 c_2}{q_1 + q_2}$$
Selling price follows: for a 25% gain, $SP = 1.25 \times CP$. Rice ₹30 and ₹40 mixed 2:3 → CP ₹36; sell at ₹45 → 25% profit. Reverse: a required profit fixes the SP, and the alligation arms fix the mixing ratio that makes it possible.

### Adulteration with a cheaper item
Ghee at ₹120 cut with oil at ₹60, sold at ₹120 for a 50% gain: the blend's CP must be $\frac{120}{1.5} = ₹80$, so alligate: ghee : oil $= (80-60):(120-80) = 1:2$. Verify: $\frac{120 \times 1 + 60 \times 2}{3} = ₹80$ ✓ — the costly item takes the *smaller* share when the target CP sits below the two-price midpoint. The lesson: **always verify the blend's CP from your ratio before quoting the answer.**

### Marked price chains on a mixture
A marked-up-then-discounted sale still ends at one SP: chips multiply ($1.25 \times 0.9 = 1.125$ → 12.5% net gain). Compute the mixture's CP first, then run the markup chain on it.

### A worked case end to end
80 kg of rice at ₹24 is mixed with 40 kg at ₹36, and the trader wants 25%. Blend CP $= \frac{1920 + 1440}{120} = ₹28$; SP $= 28 \times 1.25 = ₹35$. Every adulteration question is this skeleton with one slot hidden — the ratio, the SP, or the gain. Fix any two and the third follows by the same three lines. Note the asymmetry: profit chips act on the blend's CP, while water additions act on the *cost per sold litre* — keep the two bases apart.

### Quick revision
- Water : milk = g : 100 for gain g% when sold at cost.
- 'Water is p% of the mixture' → gain $= \frac{p}{100-p} \times 100$.
- Blend CP = weighted mean; SP from the target profit.
- Adulteration: alligate to hit the CP that yields the gain.
- Verify every ratio by recomputing the CP.
"""

    S.pattern("mix-r1", "Gain % from added water", "very common",
              "Water is added to milk (or a cheap filler to a good item) and the blend is sold at cost price — find the gain %.",
              r"\text{gain\%} = \frac{\text{water}}{\text{milk}} \times 100",
              r"""1. Express water per unit milk (convert 'p% of mixture' → $\frac{p}{100-p}$).
2. Multiply by 100.
3. Sanity: water equal to half the milk → 50% gain.

Why: the milk's cost is fully recovered; the water volume is pure margin.""",
              "A milkman mixes water equal to one-fifth of the milk and sells the mixture at cost price. His gain per cent is:",
              r"$\frac{1}{5} \times 100 = 20\%$.")
    S.pattern("mix-r2", "Find the water ratio for a target gain", "very common",
              "'What ratio of water to milk gives a gain of x% when sold at cost?'",
              r"W : M = g : 100",
              r"""1. Set $\frac{W}{M} = \frac{g}{100}$ and reduce.
2. State the ratio in the units the options use (water:milk vs milk:water).
3. Cross-check with one litre: (1+M) litres sold for M litres' cost.

Why: the gain per cent *is* the water-to-milk ratio in per cent form.""",
              "A milkman wants a 25% gain by adding water and selling at cost price. The ratio of water to milk in his mixture is:",
              r"$W:M = 25:100 = 1:4$.")
    S.pattern("mix-r3", "Blend CP and profit on the mixture", "common",
              "Two priced ingredients mixed in a given ratio; the mixture's selling price or profit % is asked.",
              r"CP = \frac{q_1 c_1 + q_2 c_2}{q_1 + q_2}, \quad SP = CP\left(1+\frac{g}{100}\right)",
              r"""1. Compute the weighted CP of the blend.
2. Apply the profit chip (or divide the SP by it to find the gain).
3. Keep fractions — ₹36.25 answers are legitimate.

Why: profit acts on the blend's average cost, not on either ingredient.""",
              "Rice at ₹30 per kg and ₹40 per kg are mixed in the ratio 2:3 and sold at ₹45 per kg. Find the profit per cent.",
              r"CP $= \frac{2 \times 30 + 3 \times 40}{5} = ₹36$ → gain $= \frac{9}{36} \times 100 = 25\%$.")
    S.pattern("mix-r4", "Adulteration for a target gain", "common",
              "A costly item is cut with a cheaper one; the selling price and target gain fix the mixing ratio.",
              r"\text{blend CP must equal } \frac{SP}{1 + g/100};\quad \text{alligate on } C_1, C_2",
              r"""1. Convert the gain to the required blend CP.
2. Alligate between the two cost prices to reach that CP.
3. Verify by recomputing the weighted CP.

Why: the blend CP that yields the gain pins the ratio uniquely.""",
              "Ghee costing ₹120 per kg is mixed with oil costing ₹60 per kg and sold at ₹120 per kg for a 50% gain. Find the mixing ratio.",
              r"Blend CP must be $₹80$ → ghee : oil $= (80-60):(120-80) = 1:2$. Check: $\frac{120 \times 1 + 60 \times 2}{3} = ₹80$ ✓.")
    S.pattern("mix-r5", "Mixture sold through markup and discount", "occasional",
              "The blended item is marked up and then discounted — net profit over the blend's CP is asked.",
              r"\text{net} = \left(1+\frac{m}{100}\right)\left(1-\frac{d}{100}\right) - 1",
              r"""1. Find the blend's CP per unit.
2. Multiply the markup and discount chips to get the net factor.
3. Profit % = (net factor − 1) × 100.

Why: markup-discount is a chip chain on top of the mixture arithmetic.""",
              "A mixture costing ₹40 per kg is marked 25% above cost and sold at a 10% discount. The profit per cent is:",
              r"$1.25 \times 0.9 = 1.125$ → 12.5% profit (SP ₹45).")

    S.q("mix-r1", "easy",
        "A milkman adds water equal to one-fifth of the milk he has and sells the mixture at the cost price of milk. His gain per cent is:",
        ["20%", "25%", "16.67%", "33.33%"], "20%",
        r"$\frac{W}{M} = \frac{1}{5}$ → gain $= 20\%$.",
        "25% reads water as a fraction of the *mixture*; the gain is per unit milk.", 25)
    S.q("mix-r1", "medium",
        "Water forms 25% of a milk-water mixture which is sold at the cost price of milk. The gain per cent is:",
        [r"$33\frac{1}{3}$%", "25%", "20%", "50%"], f"{mixed(F(100, 3))}%",
        r"Milk is 75% → gain $= \frac{25}{75} \times 100 = 33\frac{1}{3}\%$.",
        "25% is the water share of the mixture, not the profit.", 30)
    S.q("mix-r2", "easy",
        "A milkman wants to gain 25% by adding water to milk and selling the mixture at cost price. The ratio of water to milk in his mixture is:",
        ["1:4", "4:1", "1:5", "1:3"], "1:4",
        r"$W:M = 25:100 = 1:4$.",
        "4:1 would be a 400% 'gain' — read which side is water.", 25)
    S.q("mix-r2", "medium",
        "A milk-water mixture in the ratio 6:1 (milk : water) is sold at the cost price of milk. The seller's gain per cent is:",
        [r"$16\frac{2}{3}$%", "20%", "15%", "14.28%"], f"{mixed(F(50, 3))}%",
        r"$\frac{W}{M} = \frac{1}{6}$ → gain $= 16\frac{2}{3}\%$.",
        r"14.28% is $\frac{1}{7}$ of the mixture — the base is milk.", 30)
    S.q("mix-r3", "easy",
        "Rice at ₹30 per kg and ₹40 per kg are mixed in the ratio 2:3, and the mixture is sold at ₹45 per kg. The profit per cent is:",
        ["25%", "20%", "12.5%", "28%"], "25%",
        r"CP $= \frac{60 + 120}{5} = ₹36$; gain $= \frac{45 - 36}{36} \times 100 = 25\%$.",
        "20% would use SP ₹43.20 — the blend CP is ₹36.", 30)
    S.q("mix-r3", "medium",
        "Sugar at ₹25 per kg (40 kg) is mixed with sugar at ₹35 per kg (10 kg). At what price per kg should the mixture be sold to gain 25%?",
        ["₹33.75", "₹32", "₹35", "₹31.25"], "₹33.75",
        r"CP $= \frac{1000 + 350}{50} = ₹27$; SP $= 27 \times \frac{5}{4} = ₹33.75$.",
        "₹31.25 marks up 25% of the cheaper sugar, not the blend CP.", 35)
    S.q("mix-r4", "hard",
        "Ghee costing ₹120 per kg is adulterated with oil costing ₹60 per kg and the blend sold at ₹120 per kg at a gain of 50%. The ratio of ghee to oil is:",
        ["1:2", "2:1", "1:1", "1:3"], "1:2",
        r"Blend CP $= \frac{120}{1.5} = ₹80$ → ghee : oil $= (80-60):(120-80) = 20:40 = 1:2$. Check: $\frac{120 + 120}{3} = 80$ ✓.",
        "2:1 gives CP ₹100 → only 20% gain; the dearer item is the smaller share.", 40)
    S.q("mix-r4", "medium",
        "A grocer mixes 80 kg of rice at ₹24 per kg with 40 kg at ₹36 per kg. To gain 25%, the selling price per kg should be:",
        ["₹35", "₹33", "₹36", "₹34"], "₹35",
        r"CP $= \frac{1920 + 1440}{120} = ₹28$; SP $= 28 \times 1.25 = ₹35$.",
        "₹33 rounds the blend CP to 26.4 and misapplies the chip.", 30)
    S.q("mix-r5", "hard",
        "A trader blends two teas costing ₹200 and ₹300 per kg equally, marks the blend 50% above its cost, and allows a 20% discount. His profit per cent is:",
        ["20%", "25%", "16.67%", "30%"], "20%",
        r"Blend CP $= ₹250$; MP $= 375$; SP $= 375 \times 0.8 = 300$ → gain $\frac{50}{250} = 20\%$.",
        r"Chips: $1.5 \times 0.8 = 1.2$ — the discount eats a third of the markup.", 40)
    S.q("mix-r5", "medium",
        "A milkman sells a milk-water mixture (milk : water = 8:1) at the marked price which is 12.5% above the cost of milk. His gain per cent is:",
        ["12.5%", "26.56%", "11.11%", "25%"], "26.56%",
        r"Cost per sold litre $= \frac{8}{9}$ of milk's CP; SP $= 1.125 \times$ CP → net $= 1.125 \times \frac{9}{8} - 1 = \frac{81}{64} - 1 = 26.5625\%$.",
        "The water is free, so the effective cost per sold litre falls below the milk price.", 45)
    return S
