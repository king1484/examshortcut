"""Phase-2 deep content for quant/mixture-alligation — basics + alligation modules."""
import os
import sys
from fractions import Fraction as F

sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
from _lib import Sub, num, rs, mixed


def P(x):
    x = F(x)
    return (num(x) if x.denominator in (1, 2, 4, 5, 8, 10, 16, 20, 25, 40, 50, 100) else mixed(x)) + "%"


def build_basics():
    S = Sub("mix-basics")
    S.notes = r"""### What a mixture is
Two or more ingredients combined by quantity or by cost. Every mixture question reduces to one bookkeeping idea: **track the component amounts** (litres of milk, kg of salt, rupees of cost) through each operation, keeping the total consistent.

### The two-column ledger
Write each ingredient's quantity and its "value" (price per kg, % strength, litres of milk). Then:
- Total quantity = sum of the quantities.
- Total value = sum of quantity × value, ingredient by ingredient.
- **Mean value** $= \frac{\text{total value}}{\text{total quantity}}$.
40 kg of rice at ₹6 plus 60 kg at ₹7: total ₹660 over 100 kg → mean ₹6.60/kg. This one line solves every "find the average price of the mixture" question.

### Ratios inside the mixture
When a mixture holds milk and water in a ratio like 7:5, the parts share the total: 12 parts = 72 L → 1 part = 6 L → milk 42 L, water 30 L. Adding water grows only the water column and the total; the milk column does not move. **Adding one ingredient leaves the other ingredient's absolute quantity untouched** — every ratio question turns on this.

### Adding to shift a ratio
"A 40 L mixture has milk and water 3:1; how much milk makes it 4:1?" Water is fixed at 10 L; milk must become 4 × 10 = 40 L, so add 10 L. Routine:
1. Convert the ratio to absolute amounts (parts × total/parts).
2. Freeze the unchanged component.
3. Solve for the added quantity so the new ratio holds.

### Percentage strength
Concentration questions are the same ledger in per cent. A 150 L solution at 60% acid holds 90 L of acid; adding x litres of pure acid gives $\frac{90 + x}{150 + x} = 0.75$ — one linear equation. Watch the base: after adding, the **denominator grows too**.

### Alloys and blended units
Alloys (copper:zinc 5:3 in a 24 g piece → 15 g and 9 g) and 'mixing sugar at two rates' are identical arithmetic: fix the component quantity, adjust the total, recompute the ratio. The value can be rupees, litres, grams — the method never changes.

### Common slips
- Applying the new ratio to the *old* total instead of the grown total.
- Treating a percentage of the mixture as a percentage of the other ingredient (25% water in the mixture is a $\frac{25}{75} = 33\frac{1}{3}\%$ water-to-milk ratio).
- Adding quantities in litres while the ratio is in parts without converting.

### Quick revision
- Mean price = total value ÷ total quantity.
- Parts: total ÷ (sum of ratio) = one part.
- Adding X changes only X's column — freeze the other component.
- New ratio → new equation in one unknown.
- % of mixture vs % of the other ingredient are different fractions.
"""

    S.pattern("mix-v1", "Mean price / average of the mixture", "very common",
              "Quantities and unit prices are given; the mean price of the mixture is asked.",
              r"\text{mean} = \frac{\sum q_i p_i}{\sum q_i}",
              r"""1. Multiply each quantity by its price; add to get the total value.
2. Divide by the total quantity.
3. Fractions of rupees are normal — ₹6.60 is a clean exam answer.

Why: the mean value is value-weighted, not count-weighted.""",
              "40 kg of rice at ₹6 per kg is mixed with 60 kg of rice at ₹7 per kg. The average price of the mixture is:",
              r"$\frac{40 \times 6 + 60 \times 7}{100} = ₹6.60$ per kg.")
    S.pattern("mix-v2", "Ratio to absolute amounts", "very common",
              "A ratio (milk:water 7:5) with a total quantity is given — extract each part.",
              r"\text{one part} = \frac{\text{total}}{\text{sum of ratio terms}}",
              r"""1. Divide the total by the sum of the ratio terms.
2. Multiply out each component.
3. For ratios inside the mixture, remember every operation keeps some column fixed.

Why: ratios are relative; the total converts them to litres or kg.""",
              "A 72-litre mixture has milk and water in the ratio 7:5. The quantity of water is:",
              r"$\frac{72}{12} = 6$ per part → water $= 5 \times 6 = 30$ L, milk 42 L.")
    S.pattern("mix-v3", "Adding an ingredient to change the ratio", "very common",
              "'How much X must be added so the ratio becomes a:b?'",
              r"\frac{\text{component}_1}{\text{component}_2 + x} = \frac{a}{b}\ \ \text{or}\ \ \frac{\text{component}_1 + x}{\text{component}_2} = \frac{a}{b}",
              r"""1. Get absolute amounts from the original ratio and total.
2. Freeze the component not being added.
3. Set the new ratio as an equation and solve for x.

Why: only the added column grows; the other is untouched.""",
              "A 40-litre mixture has milk and water in the ratio 3:1. How much milk must be added to make the ratio 4:1?",
              r"Water $= 10$ L stays; milk must reach $40$ L → add $40 - 30 = 10$ L.")
    S.pattern("mix-v4", "Percentage strength of a solution", "common",
              "A solution's concentration is given; after adding solvent or solute, find the new strength.",
              r"\text{strength} = \frac{\text{amount of solute}}{\text{total volume}} \times 100",
              r"""1. Compute the solute amount from the percentage.
2. Add to the solute (or leave it) and grow the total as required.
3. Write the new fraction and convert to a per cent.

Why: percentages are fractions of the *current* total, which changes.""",
              "150 L of a solution contains 60% acid. How much pure acid must be added to make it 75% acid?",
              r"Acid $= 90$; $\frac{90+x}{150+x} = \frac{3}{4}$ → $x = 90$ L.")
    S.pattern("mix-v5", "Alloys and multi-part blending", "common",
              "Alloys with metal ratios, or a blend whose parts are used in further mixing.",
              r"\text{component} = \frac{\text{ratio term}}{\text{sum}} \times \text{total}",
              r"""1. Convert each alloy's ratio to grams (or kg) of each metal.
2. Pool the columns across all sources.
3. Read the new ratio (or solve for the addition needed).

Why: metals from different sources simply add up column-wise.""",
              "An alloy has copper and zinc in the ratio 5:3. In 24 g of it, how much copper must be added to make the ratio 3:1?",
              r"Copper 15 g, zinc 9 g; zinc fixed → copper $= 27$ g → add 12 g.")

    S.q("mix-v1", "easy",
        "40 kg of rice costing ₹6 per kg is mixed with 60 kg of rice costing ₹7 per kg. The average cost of the mixture per kg is:",
        ["₹6.60", "₹6.50", "₹6.75", "₹7"], "₹6.60",
        r"$\frac{40 \times 6 + 60 \times 7}{100} = \frac{660}{100} = ₹6.60$.",
        "₹6.50 is the simple midpoint — weights are 40 and 60, not equal.", 25)
    S.q("mix-v1", "medium",
        "In what ratio must rice at ₹320 per kg be mixed with rice at ₹250 per kg so that the mixture costs ₹300 per kg?",
        ["2:5", "5:2", "1:2", "3:5"], "2:5",
        r"Dear:cheap $= (320-300):(300-250) = 20:50 = 2:5$.",
        "5:2 reverses the alligation arms.", 30)
    S.q("mix-v2", "easy",
        "A 72-litre mixture contains milk and water in the ratio 7:5. The quantity of water in the mixture is:",
        ["30 litres", "42 litres", "36 litres", "25 litres"], "30 litres",
        r"Part $= \frac{72}{12} = 6$ → water $= 5 \times 6 = 30$ L.",
        "42 L is the milk; 36 L is half the total.", 25)
    S.q("mix-v2", "medium",
        "A mixture of 81 litres contains milk and water in the ratio 8:1. How much water must be added to make the ratio 8:3?",
        ["18 litres", "9 litres", "27 litres", "12 litres"], "18 litres",
        r"Milk 72 L fixed → water must become $\frac{72 \times 3}{8} = 27$ L → add $27 - 9 = 18$ L.",
        "27 L is the final water, not the addition.", 30)
    S.q("mix-v3", "easy",
        "A 40-litre mixture has milk and water in the ratio 3:1. How much milk should be added to make the ratio 4:1?",
        ["10 litres", "5 litres", "8 litres", "12 litres"], "10 litres",
        r"Water 10 L fixed; milk must become $4 \times 10 = 40$ L → add $40 - 30 = 10$ L.",
        "The total grows to 50 L — don't scale the old 40 L.", 25)
    S.q("mix-v3", "medium",
        "20 kg of sugar at ₹45 per kg is mixed with 30 kg at ₹52 per kg. The average price of the mixture per kg is:",
        ["₹49.20", "₹48.50", "₹50", "₹48"], "₹49.20",
        r"$\frac{20 \times 45 + 30 \times 52}{50} = \frac{2460}{50} = ₹49.20$.",
        "₹48.50 is the midpoint; the 30 kg batch pulls the mean up.", 30)
    S.q("mix-v4", "medium",
        "A solution of 150 litres contains 60% acid. How much pure acid should be added to make the solution 75% acid?",
        ["90 litres", "60 litres", "75 litres", "112.5 litres"], "90 litres",
        r"Acid $= 90$ L; $\frac{90 + x}{150 + x} = \frac{3}{4}$ → $360 + 4x = 450 + 3x$ → $x = 90$ L.",
        "112.5 L is 75% of 150 — the total volume grows when acid is added.", 35)
    S.q("mix-v4", "medium",
        "A 40-litre solution of milk contains 90% milk. After 10 litres of water is added, the percentage of milk in the solution is:",
        ["72%", "80%", "75%", "64%"], "72%",
        r"Milk $= 36$ L; new total $= 50$ L → $\frac{36}{50} \times 100 = 72\%$.",
        "80% keeps the old denominator 45 — the total became 50.", 30)
    S.q("mix-v5", "medium",
        "An alloy contains copper and zinc in the ratio 5:3. In 24 grams of this alloy, how much copper should be added to make the ratio 3:1?",
        ["12 grams", "9 grams", "15 grams", "8 grams"], "12 grams",
        r"Copper 15 g, zinc 9 g; zinc stays 9 g → copper $= 3 \times 9 = 27$ g → add 12 g.",
        "The zinc column is frozen; only copper grows.", 30)
    S.q("mix-v5", "hard",
        "A bucket has 30 litres of a milk-water mixture in the ratio 4:1. If 2 litres of milk and 4 litres of water are added, the new ratio is:",
        ["13:5", "5:2", "4:1", "6:5"], "13:5",
        r"Milk 24, water 6 → after adding: $26$ and $10$ → $26:10 = 13:5$.",
        "Both columns grew — compute each before ratioing.", 35)
    return S


def build_alligation():
    S = Sub("mix-alligation")
    S.notes = r"""### The rule of alligation
When two ingredients at 'prices' $C$ (cheaper) and $D$ (dearer) are mixed to give a mean $M$, the mixing ratio is fixed by the balance:
$$\frac{\text{quantity of dearer}}{\text{quantity of cheaper}} = \frac{M - C}{D - M}$$
Or the tilted diagram: write C and D at the top, M in the middle; each lower arm subtracts diagonally — left arm $= M - C$, right arm $= D - M$ — and the arms are the **ratio of quantities of the side you came from**.
Tea at ₹320 and ₹250 to sell at ₹300: dearer $= \frac{300-250}{320-300} = \frac{50}{20} = \frac{5}{2}$ of the cheaper → 2:5. The mean must always lie between C and D; if your ratio comes out negative, you have inverted an arm.

### Why it works
Let x and y be the quantities: $\frac{Cx + Dy}{x + y} = M$. Cross-multiplying: $x(D - M) = y(M - C)$ — exactly the arms. Alligation is one linear equation wearing a picture.

### The same rule everywhere
Any weighted mean splits into an alligation:
- **Speeds**: equal distances at speeds u and v → average $= \frac{2uv}{u+v}$; the *time* ratio is $\frac{v - A}{A - u}$.
- **Class averages**: boys average 70, girls 75, class 72 → boys : girls $= (75-72):(72-70) = 3:2$.
- **Interest rates**: two investments at 5% and 8% averaging 6.25% → amounts in 7:5.
- **Profit per cents**: items sold at 20% and 10% profit with a 14% overall → cost split 3:2.
In each case the 'price' is the quantity being averaged and the arms give the *weights*.

### Using quantities, not just ratios
When one actual quantity is known, scale the arms. 25 kg of sugar at ₹24 must be mixed with sugar at ₹42 to average ₹30: arms give cheaper : dearer $= (42-30):(30-24) = 2:1$, so dearer $= 25$ kg — the cheaper arm is double the dearer one.

### Strengths and fractions
Solution strengths work identically: 20% and 50% acid mixed to get 30% → $\frac{50-30}{30-20} = \frac{20}{10} = 2:1$ (dilute : strong). For two full mixtures, first reduce each to the fraction of the key component, then alligate on those fractions.

### Common slips
- Writing the arms upside down: cheaper : dearer $= (D-M):(M-C)$.
- Alligating on the wrong quantity (alligate times for equal distances, distances for equal times).
- Averaging three prices pairwise by gut — pair them so each pair brackets the mean, or use the ledger formula.

### Quick revision
- Dearer : cheaper $= (M-C) : (D-M)$.
- The mean sits between the two prices; arms subtract diagonally.
- Known quantity × arm ratio = actual weights.
- Works on prices, speeds, marks, rates, profit %, strengths.
- Verify: recompute the mean from the mixed ratio.
"""

    S.pattern("mix-a1", "Two-ingredient alligation for the ratio", "very common",
              "Two unit prices are given with the target mean price; the mixing ratio is asked.",
              r"D:C = (M - C) : (D - M)",
              r"""1. Identify cheaper, dearer and mean; check C < M < D.
2. Subtract diagonally: $(M-C)$ and $(D-M)$.
3. State the ratio of the dearer to cheaper — and scale by any known quantity.

Why: the weighted-mean equation rearranges into exactly these arms.""",
              "In what ratio should tea at ₹320 per kg be mixed with tea at ₹250 per kg to get a mixture worth ₹300 per kg?",
              r"D:C $= (300-250):(320-300) = 50:20 = 5:2$.")
    S.pattern("mix-a2", "Mixing solutions by strength", "very common",
              "Two solutions of given concentration are mixed to reach a target strength.",
              r"\frac{\text{dilute}}{\text{strong}} = \frac{S - M}{M - W}\ \ (W\%, S\%\ \text{strengths})",
              r"""1. Alligate on the strength fractions exactly as on prices.
2. If a final volume is fixed, split it by the ratio.
3. Watch which side is dilute — the arm $(S - M)$ belongs to it.

Why: strength is just the 'price' per litre of solution.""",
              "Solutions of 20% and 50% acid are mixed to make a 30% solution. The ratio of the 20% solution to the 50% solution is:",
              r"$(50-30):(30-20) = 20:10 = 2:1$.")
    S.pattern("mix-a3", "Alligation on averages (speeds, marks, ages)", "common",
              "Two groups with different averages combine to a known overall average — find the group sizes' ratio.",
              r"\frac{n_1}{n_2} = \frac{A_2 - A}{A - A_1}",
              r"""1. Treat the averages as the two prices and the overall as M.
2. Subtract to the arms; the arms are the sizes' ratio.
3. For speeds over equal distances, alligate the *times*, not the distances.

Why: the overall average is the size-weighted mean of the group averages.""",
              "The average marks of boys in a class is 70 and of girls is 75. If the class average is 72, the ratio of boys to girls is:",
              r"$(75-72):(72-70) = 3:2$.")
    S.pattern("mix-a4", "Find the quantity to add (alligation form)", "common",
              "'How much of X must be added to Y of the mixture to reach a given strength or price?'",
              r"\frac{q_{\text{added}}}{q_{\text{existing}}} = \frac{M_{\text{old}} - M}{M - M_{\text{added}}}",
              r"""1. Give the added ingredient its own 'price' (0 for water, 100 for pure acid, its cost price).
2. Alligate between the old mixture and the addition.
3. Solve for the unknown quantity.

Why: adding a zero-price ingredient is a two-price mixture.""",
              "How much pure acid must be added to 100 litres of a 30% acid solution to make it 50% acid?",
              r"Acid $= 30$; $\frac{30+x}{100+x} = \frac{1}{2}$ → $x = 40$ L. Alligation view: free water in the mix vs pure acid at 'price' 100%.")
    S.pattern("mix-a5", "Alligation on rates and profits", "common",
              "Two investments at different interest rates, or items sold at different profit per cents, with a known combined result.",
              r"\frac{\text{amount}_1}{\text{amount}_2} = \frac{R_2 - R}{R - R_1}",
              r"""1. Alligate on the percentages (rate or profit) to split the total amount.
2. Overall rate $= \frac{\text{total interest}}{\text{total sum}} \times 100$ if not given.
3. Convert back to actual parts by scaling the total.

Why: the combined percentage is the amount-weighted mean.""",
              "₹12,000 is invested partly at 5% and the rest at 8% simple interest. The total yearly interest is ₹750. Find each part.",
              r"Mean rate $= \frac{750}{12000} \times 100 = 6.25\%$ → 5% : 8% $= (8-6.25):(6.25-5) = 1.75:1.25 = 7:5$ → ₹7,000 and ₹5,000.")

    S.q("mix-a1", "easy",
        "In what ratio must wheat at ₹4.50 per kg be mixed with wheat at ₹5.20 per kg so that the mixture is worth ₹5 per kg?",
        ["2:5", "5:2", "1:3", "4:7"], "2:5",
        r"Cheap : dear $= (5.20-5):(5-4.50) = 0.20:0.50 = 2:5$.",
        r"Check: $\frac{4.5 \times 2 + 5.2 \times 5}{7} = \frac{35}{7} = ₹5$ — arms run diagonally.", 30)
    S.q("mix-a1", "medium",
        "How many kg of sugar costing ₹42 per kg must be mixed with 25 kg of sugar costing ₹24 per kg so that the mixture costs ₹30 per kg?",
        ["50 kg", "30 kg", "45 kg", "20 kg"], "50 kg",
        r"Cheap : dear $= (42-30):(30-24) = 12:6 = 2:1$ → cheap $= 2 \times 25 = 50$ kg.",
        "The ₹24 sugar is double the ₹42 sugar — arms $(42-30)$ and $(30-24)$.", 35)
    S.q("mix-a2", "easy",
        "Two solutions of 20% and 50% acid are mixed to obtain a 30% acid solution. The ratio in which they should be mixed is:",
        ["2:1", "1:2", "3:2", "1:1"], "2:1",
        r"Dilute : strong $= (50-30):(30-20) = 2:1$.",
        "1:2 reverses the arms.", 25)
    S.q("mix-a2", "hard",
        "Alloy A has copper and zinc in the ratio 4:1 and alloy B in the ratio 1:4. Equal weights of A and B are melted together. The ratio of copper to zinc in the new alloy is:",
        ["1:1", "4:1", "2:3", "5:4"], "1:1",
        r"Copper fraction $= \frac{1}{2}\left(\frac{4}{5} + \frac{1}{5}\right) = \frac{1}{2}$ → copper : zinc $= 1:1$.",
        "The deficits cancel: A's extra copper is exactly B's zinc.", 35)
    S.q("mix-a3", "medium",
        "A car covers two equal distances at 30 km/h and 45 km/h. The average speed for the whole journey is:",
        ["36 km/h", "37.5 km/h", "40 km/h", "35 km/h"], "36 km/h",
        r"Equal distances → $\frac{2 \times 30 \times 45}{30 + 45} = 36$ km/h. Alligation check: time ratio $= (45-36):(36-30) = 9:6 = 3:2$.",
        "37.5 is the arithmetic mean — valid only for equal *times*.", 30)
    S.q("mix-a3", "medium",
        "In a class, the average marks of boys is 70 and of girls is 75. If the class average is 72, the ratio of the number of boys to girls is:",
        ["3:2", "2:3", "4:3", "5:4"], "3:2",
        r"Boys : girls $= (75-72):(72-70) = 3:2$.",
        "The arm nearer the girls' average belongs to the boys.", 30)
    S.q("mix-a4", "easy",
        "How much water must be added to 60 litres of milk so that milk forms 75% of the new mixture?",
        ["20 litres", "15 litres", "24 litres", "30 litres"], "20 litres",
        r"Milk stays 60 L and must be 75% → total $= \frac{60 \times 4}{3} = 80$ L → water added $= 20$ L.",
        r"15 L makes milk 80% — check $\frac{60}{80} = 75\%$ only for 20 L.", 25)
    S.q("mix-a4", "medium",
        "A 20-litre mixture contains 10% water. How much water must be added to raise the water content to 25%?",
        ["4 litres", "5 litres", "6 litres", "8 litres"], "4 litres",
        r"Water 2 L, milk 18 L; milk must be 75% → total $= \frac{18 \times 4}{3} = 24$ L → add 4 L.",
        "25% of the *new* mixture — the total grows with the water.", 30)
    S.q("mix-a5", "hard",
        "A sum of ₹12,000 is lent partly at 5% and the remainder at 8% per annum simple interest. If the total yearly interest is ₹750, the sum lent at 8% is:",
        ["₹5,000", "₹7,000", "₹4,800", "₹6,000"], "₹5,000",
        r"Mean rate $= 6.25\%$; 5% : 8% parts $= (8-6.25):(6.25-5) = 7:5$ → at 8%: $\frac{5}{12} \times 12000 = ₹5{,}000$.",
        "₹7,000 is the 5% part — the bigger arm belongs to the dearer rate.", 40)
    S.q("mix-a5", "medium",
        "A shopkeeper sells article A at 20% profit and article B at 10% profit. If the overall profit is 14%, the ratio of the cost prices of A and B is:",
        ["2:3", "3:2", "1:2", "4:5"], "2:3",
        r"CP(A) : CP(B) $= (14-10):(20-14) = 4:6 = 2:3$.",
        "A's profit sits above the mean, so its arm is the smaller one.", 30)
    return S
