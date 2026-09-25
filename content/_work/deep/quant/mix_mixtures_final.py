"""Phase-2 deep content for quant/mixture-alligation — mixtures-of-mixtures module."""
import os
import sys
from fractions import Fraction as F

sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
from _lib import Sub, num, rs, mixed

# --- arithmetic behind every answer ---
assert F(1, 2) * (F(4, 5) + F(3, 5)) == F(7, 10)                       # equal volumes 4:1 + 3:2
assert 15 + 20 == 35 and 5 + 12 == 17                                   # 35:17
assert F(5, 36) * 60 == F(25, 3) and F(1, 60) * 60 == 1                 # 5:3 target check
assert 5 * F(2, 5) + 3 * F(4, 9) == 8 * F(5, 12)
assert 30 + 20 == 50 and 50 - 30 == 20                                  # add milk to 5:1
assert 60 * F(2, 3) - 8 == 32 and 60 * F(1, 3) - 4 + 8 == 24            # 4:3
assert 21 + 10 == 31 and 9 + 10 == 19                                   # 31:19
assert F(35, 8) + 5 == F(75, 8) and F(5, 8) == F(5, 8)                  # second-vessel milk 9.375
assert F(75, 8) * 8 == 75 and F(5, 8) * 8 == 5                          # 15:1
assert (2 * 60 + 1 * 30) / 3 == 50                                      # 50% acid
assert 100 * F(4, 5) ** 2 == 64                                         # 64%
assert F(1, 3) * (F(1, 2) + F(2, 5) + F(3, 8)) == F(17, 40)             # three vessels
assert 2 * F(5, 8) + 3 * F(1, 3) == F(9, 4)                             # 9:11


def build_mixtures():
    S = Sub("mix-mixtures")
    S.notes = r"""### Mixing two finished mixtures
Two vessels, each already a milk-water (or acid-water) blend, are poured together. Reduce each vessel to the **fraction of the key component**, pool the columns, and read the new ratio:
$$\text{milk in blend} = q_1 f_1 + q_2 f_2, \qquad f = \frac{\text{milk}}{\text{total}}$$
Vessel A (milk:water 3:1, 20 L) gives 15 L milk; vessel B (5:3, 32 L) gives 20 L — together 35 : 17. Nothing deeper than bookkeeping.

### Choosing the mixing ratio for a target
To blend A and B into a target strength $t$ (as a milk fraction), alligate on the fractions:
$$\frac{q_A}{q_B} = \frac{t - f_B}{f_A - t}$$
Both differences must carry the same sign — the target must lie between $f_A$ and $f_B$. Vessels at $\frac{2}{5}$ and $\frac{4}{9}$ milk blended to $\frac{5}{12}$: $\frac{q_A}{q_B} = \frac{\frac{5}{12}-\frac{4}{9}}{\frac{2}{5}-\frac{5}{12}} = \frac{\frac{1}{36}}{\frac{1}{60}} = \frac{5}{3}$. Verify: $5 \times \frac{2}{5} + 3 \times \frac{4}{9} = \frac{10}{3}$ milk in 8 parts → $\frac{5}{12}$ ✓.

### Transfers between vessels
Drawing from a uniform mixture takes the components in the vessel's own ratio — the ratio inside survives a withdrawal. What changes it is the topping-up. Two classics:
- **Proportional draw, then top up**: 60 L of 2:1, remove 12 L (8 milk, 4 water — still 2:1), add 8 L water → 32:24 = 4:3.
- **Cross-transfer**: 40 L pure milk; 5 L moved to an empty vessel, replaced with water; then 5 L of the (now 35:5) mixture moved back. The second vessel ends at $9.375 : 0.625 = 15:1$. Track each vessel separately; volumes must balance.

### Equal capacities and three vessels
For equal volumes, the blended strength is the plain mean of the fractions: vessels at $\frac{1}{2}$, $\frac{2}{5}$, $\frac{3}{8}$ milk → $\frac{1}{3}\left(\frac{20+16+15}{40}\right) = \frac{17}{40}$ → milk : water 17:23. For unequal capacities, weight by the volumes first.

### Dilution by repeated fractions
Removing 20% of a vessel and topping with water multiplies the strength by 0.8 each round — the replacement formula in percentage clothes. 100 L at 80% milk, two rounds: $100 \times 0.8^2 = 64$ L of milk → 64%.

### One ledger, many vessels
Whatever the story — pouring, drawing, topping, blending — the method never changes: maintain a per-vessel, per-component table and update it operation by operation. The only decisions are (1) how a withdrawal splits (in the source's own ratio), and (2) which column an addition swells. Exam answers are built so that a wrong split or a missed total change lands on a distractor, so recompute the pooled total as a checksum — components must always add back to the vessel's volume.

### Quick revision
- Convert each vessel to its key-component fraction before pooling.
- Target blend: alligate the fractions; the target sits between them.
- A withdrawal preserves the internal ratio; an addition shifts it.
- Equal capacities → plain mean of strengths.
- Cross-transfers: keep a separate ledger per vessel.
"""

    S.pattern("mix-c1", "Two mixtures combined", "very common",
              "Two vessels with given milk-water ratios (and volumes) are mixed — find the final ratio.",
              r"\text{milk} = q_1 f_1 + q_2 f_2, \quad \text{water} = q_1(1-f_1) + q_2(1-f_2)",
              r"""1. Convert each vessel to litres of milk (fraction × volume).
2. Pool milk and water columns.
3. Reduce the ratio to smallest terms.

Why: components add linearly across vessels.""",
              "Vessels of milk:water 4:1 and 3:2 are mixed in equal volumes. Find the milk : water ratio of the blend.",
              r"Milk fraction $= \frac{1}{2}\left(\frac{4}{5} + \frac{3}{5}\right) = \frac{7}{10}$ → 7:3.")
    S.pattern("mix-c2", "Ratio to hit a target strength", "common",
              "'In what ratio must mixture A be mixed with mixture B to get milk : water = t?'",
              r"\frac{q_A}{q_B} = \frac{t - f_B}{f_A - t}",
              r"""1. Write each vessel's milk fraction and the target fraction.
2. Alligate on the fractions — same-sign differences.
3. Verify by recomputing the blend's strength.

Why: a target strength between the two source strengths fixes the weights.""",
              "Mixtures with milk:water 2:3 and 4:5 are blended to give milk : water = 5:7. Find the mixing ratio.",
              r"Fractions $\frac{2}{5}, \frac{4}{9}$; target $\frac{5}{12}$ → $\frac{q_A}{q_B} = \frac{\frac{5}{12}-\frac{4}{9}}{\frac{2}{5}-\frac{5}{12}} = 5:3$.")
    S.pattern("mix-c3", "Transfer and top-up between vessels", "common",
              "A quantity is drawn from one vessel into another (or replaced) — track both ledgers.",
              r"\text{withdrawal splits in the source's own ratio}",
              r"""1. Convert to component litres per vessel.
2. Move the drawn volume split in the source's ratio.
3. Apply additions; confirm each vessel's total separately.

Why: a uniform mixture leaves in its own proportions.""",
              "A 40-litre can of pure milk: 5 litres are moved to an empty vessel and the can is topped with water; then 5 litres of the can's mixture are moved to the second vessel. Milk : water in the second vessel?",
              r"After water: can 35, 5. The 5 L drawn carries 4.375 milk, 0.625 water → second vessel $9.375 : 0.625 = 15:1$.")
    S.pattern("mix-c4", "Strength of a blended solution", "common",
              "Two solutions of given concentration are mixed in a given ratio — the resulting strength is asked.",
              r"\text{strength} = \frac{q_1 s_1 + q_2 s_2}{q_1 + q_2}",
              r"""1. Compute solute from each solution.
2. Divide the pooled solute by the pooled volume.
3. Convert to a percentage.

Why: concentration is volume-weighted, never a plain average unless volumes match.""",
              "60% and 30% acid solutions are mixed in the ratio 2:1. The strength of the resulting solution is:",
              r"$\frac{2 \times 60 + 1 \times 30}{3} = 50\%$.")
    S.pattern("mix-c5", "Three vessels / equal capacities", "occasional",
              "Three (or more) blends combine, often in equal volumes.",
              r"\bar{f} = \frac{f_1 + f_2 + f_3}{3}\ \ \text{(equal volumes)}",
              r"""1. Write each vessel's milk fraction.
2. Equal volumes → average the fractions; else weight by volume.
3. Convert the mean fraction to the required ratio.

Why: with equal capacities the weights are all 1.""",
              "Three equal vessels hold milk : water 1:1, 2:3 and 3:5. Find the milk : water ratio of their mixture.",
              r"Mean fraction $= \frac{1}{3}\left(\frac{1}{2}+\frac{2}{5}+\frac{3}{8}\right) = \frac{17}{40}$ → 17:23.")

    S.q("mix-c1", "easy",
        "Two vessels contain milk and water in the ratios 4:1 and 3:2. Equal volumes from both are mixed. The ratio of milk to water in the new mixture is:",
        ["7:3", "7:2", "1:1", "3:2"], "7:3",
        r"Milk $= \frac{1}{2}\left(\frac{4}{5}+\frac{3}{5}\right) = \frac{7}{10}$ → milk : water $= 7:3$.",
        "Adding the ratios works here only because the volumes are equal — use fractions in general.", 30)
    S.q("mix-c1", "medium",
        "A 20-litre mixture has milk and water in the ratio 3:1, and a 32-litre mixture has them in 5:3. If both are poured into one container, the ratio of milk to water is:",
        ["35:17", "8:4", "31:19", "5:3"], "35:17",
        r"Milk $15 + 20 = 35$; water $5 + 12 = 17$ → 35:17.",
        "Add litres, not ratios — 3:1 and 5:3 cannot be summed directly.", 30)
    S.q("mix-c2", "hard",
        "In what ratio must a mixture of milk and water in the ratio 2:3 be mixed with one in the ratio 4:5 so that the new mixture has milk and water in the ratio 5:7?",
        ["5:3", "3:5", "1:1", "2:1"], "5:3",
        r"Fractions $\frac{2}{5}, \frac{4}{9}$, target $\frac{5}{12}$: $\frac{q_1}{q_2} = \frac{\frac{5}{12}-\frac{4}{9}}{\frac{2}{5}-\frac{5}{12}} = \frac{\frac{1}{36}}{\frac{1}{60}} = 5:3$.",
        r"Check: $5 \times \frac{2}{5} + 3 \times \frac{4}{9} = \frac{10}{3}$ milk in 8 parts → $\frac{5}{12}$ ✓.", 45)
    S.q("mix-c2", "medium",
        "A 40-litre mixture has milk and water in the ratio 3:1. How much milk must be added to make the ratio 5:1?",
        ["20 litres", "16 litres", "10 litres", "25 litres"], "20 litres",
        r"Water 10 L fixed; milk must reach $5 \times 10 = 50$ L → add $50 - 30 = 20$ L.",
        "The milk column grows from 30 to 50; the water never moves.", 30)
    S.q("mix-c3", "medium",
        "A 60-litre mixture has milk and water in the ratio 2:1. 12 litres of the mixture are removed and 8 litres of water are added. The new ratio of milk to water is:",
        ["4:3", "2:1", "3:2", "5:3"], "4:3",
        r"Draw removes 8 milk, 4 water → 32, 16; add 8 water → $32:24 = 4:3$.",
        "The 12 litres leave in the ratio 2:1 — not as pure milk.", 35)
    S.q("mix-c3", "easy",
        "Vessel A has 30 litres with milk : water 7:3; vessel B has 20 litres with milk : water 1:1. A's contents are poured into B. The final ratio of milk to water is:",
        ["31:19", "8:5", "7:5", "3:2"], "31:19",
        r"A: 21, 9; B: 10, 10 → total $31:19$.",
        "31 + 19 = 50, the pooled volume — a quick total check.", 25)
    S.q("mix-c3", "hard",
        "A can holds 40 litres of pure milk. 5 litres are transferred to an empty vessel and the can is topped up with water. Then 5 litres of the can's mixture are transferred to the second vessel. The ratio of milk to water in the second vessel is now:",
        ["15:1", "7:1", "8:1", "14:1"], "15:1",
        r"Can after water: 35, 5. The second 5-litre draw carries $\frac{35}{8} = 4.375$ milk and $0.625$ water → second vessel $9.375 : 0.625 = 15:1$.",
        "The can was 7:1 when the second draw left it — that ratio splits the 5 litres.", 45)
    S.q("mix-c4", "easy",
        "Solutions of 60% and 30% acid are mixed in the ratio 2:1. The strength of the resulting solution is:",
        ["50%", "45%", "55%", "48%"], "50%",
        r"$\frac{2 \times 60 + 1 \times 30}{3} = 50\%$.",
        "45% is the plain mean — the volumes differ.", 25)
    S.q("mix-c4", "hard",
        "100 litres of a solution contains 80% milk. 20 litres are drawn off and replaced with water; the operation is performed twice. The percentage of milk in the final solution is:",
        ["64%", "60%", "68%", "72%"], "64%",
        r"Milk $= 100 \times \left(\frac{80}{100}\right)^2 = 64$ L in 100 L → 64%.",
        r"Each round multiplies by $1 - \frac{20}{100} = 0.8$.", 35)
    S.q("mix-c5", "hard",
        "Three vessels of equal capacity hold milk and water in the ratios 1:1, 2:3 and 3:5. When all three are emptied together, the ratio of milk to water is:",
        ["17:23", "2:3", "6:9", "1:1"], "17:23",
        r"Milk fraction $= \frac{1}{3}\left(\frac{1}{2}+\frac{2}{5}+\frac{3}{8}\right) = \frac{1}{3} \times \frac{51}{40} = \frac{17}{40}$ → 17:23.",
        "Equal capacities average the fractions directly; 17 + 23 = 40 parts.", 40)
    S.q("mix-c5", "medium",
        "2 litres of a milk-water mixture in the ratio 5:3 are mixed with 3 litres of a mixture in the ratio 1:2. The ratio of milk to water in the result is:",
        ["9:11", "6:5", "3:5", "11:9"], "9:11",
        r"Milk $= 2 \times \frac{5}{8} + 3 \times \frac{1}{3} = \frac{5}{4} + 1 = \frac{9}{4}$; water $= \frac{11}{4}$ → 9:11.",
        "Total 5 litres splits as 2.25 and 2.75 — the fractions decide, not the ratios.", 35)
    return S
