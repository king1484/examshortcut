from _lib import *
from fractions import Fraction as Fr

# ------------------------------------------------------------------ checks
assert F(30, 40 * 4) == F(3, 16) and 40 * F(3, 4) == 30 and 40 - 30 == 10
assert F(10, 15) == F(2, 3)
assert 80 - 8 == 72 and F(72, 8) == 9
assert F(6, 6) == 1
assert 40 * F(3, 5) == 24 and Fr(12, 25) == F(12, 25) and abs(float(Fr(12, 25)) - 0.48) < 1e-12
assert F(50, 5) == 10 and F(40, 20) == 2 and 20 - 10 == 10
assert 40 * F(5, 8) == 25 and 40 * F(3, 8) == 15 and 25 * F(7, 5) == 35 and 35 - 15 == 20
assert 100 * Fr(4, 5)**2 == 64
assert Fr(3, 4) * Fr(1, 2) + Fr(5, 8) * Fr(1, 2) == Fr(11, 16)
assert F(1, 5) == F(20, 100)
assert F(2, 5) == F(20, 50) and F(3, 5) == F(30, 50)
assert F(20, 4) == 5 and 60 / 5 == 12
# H1: 7:5, remove 9 L, refill water -> 7:9
x = Fr(36)
milk0 = x * Fr(7, 12)
assert milk0 == 21
milk1 = milk0 - 9 * Fr(7, 12)
assert milk1 == Fr(63, 4) and milk1 / x == Fr(7, 16)
# H2: 40 L, thrice 10% replacement
assert 40 * Fr(9, 10)**3 == Fr(729, 25) and Fr(729, 25) == 29 + Fr(4, 25)
assert Fr(729, 25) / (40 - Fr(729, 25)) == Fr(729, 271)
# H3: two replacements of 8 L, wine:water 16:9
assert Fr(4, 5)**2 == F(16, 25) and 8 * 5 == 40
# solved
assert F(6, 4) == Fr(3, 2)                       # S1 cheaper:dearer = 3:2
assert 60 * F(40, 100) == 24 and Fr(24, 120) == Fr(1, 5)   # S2: add 60 L water
assert 60 * Fr(9, 10)**2 == Fr(243, 5) and Fr(243, 5) == 48 + Fr(3, 5)  # S3
assert 36 * F(5, 6) == 30 and 30 * F(3, 5) - 6 == 12       # S4
assert F(2, 5) == F(2000, 5000) and F(1, 1) == F(30, 30)   # S5 men:women 1:1

subtopics = [
 sub("mix-basics", "Mixture Concentration & Amounts",
  md(r"A mixture holds ingredients in a fixed ratio or concentration. The two working quantities are:",
     "",
     r"- **Amount of each ingredient** from the ratio: in 40 L of milk : water $= 3:1$, milk $= 40 \times \frac{3}{4} = 30$ L.",
     r"- **Concentration (per cent)** of an ingredient: $\frac{\text{amount of ingredient}}{\text{total volume}} \times 100$.",
     "",
     r"When something is added or drained, only ONE of the two quantities changes — track that one and rebuild the ratio.",
     "",
     r"Adding water dilutes; adding pure ingredient strengthens; removing mixture removes **both** ingredients proportionally."),
  [formula("Amount from ratio", r"\text{part} = \text{total} \times \frac{\text{part's share}}{\text{sum of shares}}"),
   formula("Concentration", r"C = \frac{\text{ingredient}}{\text{mixture}} \times 100\%"),
   formula("Adding water", r"C' = \frac{A}{M + w} \quad (A \text{ unchanged})"),
   formula("Removing mixture", r"\text{each ingredient} \to \text{same fraction removed}")],
  [trick("Track the constant ingredient",
         "Water added ⇒ milk unchanged. Everything hinges on the unchanged part.",
         "A 40-litre mixture has milk and water in the ratio 3 : 1. How much water does it contain?",
         r"Water $= 40 \times \frac{1}{4} = 10$ litres."),
   trick("Rebuild the per cent after dilution",
         "Milk fixed, total grows — divide again.",
         "20 litres of a mixture contains 60% milk. After adding 5 litres of water, the milk percentage is:",
         r"Milk $= 12$ L; new total $= 25$ L ⇒ $\frac{12}{25} = 48\%$."),
   trick("Ratio change ⇒ one equation",
         "Set the unchanged quantity against the wanted ratio.",
         "A 50-litre mixture of milk and water in the ratio 4 : 1 needs how much water to become 2 : 1?",
         r"Milk 40 L must be $\frac{2}{3}$: water total $= 20$ ⇒ add $20 - 10 = 10$ litres.")],
  [r"Changing both parts of a ratio when only the denominator changed (adding water leaves milk untouched).",
   "Adding x litres of water and thinking the milk percentage drops by x%.",
   r"Taking the ratio share of the wrong ingredient ($\frac{1}{4}$ vs $\frac{3}{4}$).",
   "Forgetting the total volume changes when anything is added (even when mixture is drained first)."]),

 sub("mix-alligation", "Rule of Alligation",
  md("Alligation mixes two ingredients of known 'strength' (price, %, speed, average) to hit a target mean:",
     "",
     r"$$\text{cheaper quantity} : \text{dearer quantity} = (\text{dearer} - \text{mean}) : (\text{mean} - \text{cheaper})$$",
     "",
     r"It is the weighted average solved backwards: $\bar{v} = \frac{n_1 v_1 + n_2 v_2}{n_1 + n_2}$, so $\frac{n_1}{n_2} = \frac{v_2 - \bar{v}}{\bar{v} - v_1}$.",
     "",
     r"**Works whenever the quantity mixes linearly** — prices, percentages (milk, acid, alcohol), average ages, average salaries, average speeds for equal times.",
     "",
     "The mean must always lie BETWEEN the two strengths; the distances give the quantities, crossing over."),
  [formula("Alligation ratio", r"\frac{n_1}{n_2} = \frac{v_2 - \bar{v}}{\bar{v} - v_1}"),
   formula("Weighted average", r"\bar{v} = \frac{n_1 v_1 + n_2 v_2}{n_1 + n_2}"),
   formula("Cheaper : dearer", r"(d - m) : (m - c)"),
   formula("Water as free ingredient", r"\text{milk} : \text{water} = (m - 0) : (c - m), \ c > m")],
  [trick("Cross over the distances",
         "Dearer-minus-mean and mean-minus-cheaper swap sides — that's the whole rule.",
         "In what ratio must rice at ₹36/kg be mixed with rice at ₹24/kg so that the mixture costs ₹30/kg?",
         r"Cheaper : dearer $= (36-30) : (30-24) = 1 : 1$."),
   trick("Water costs zero",
         "Dilution questions are alligation with one strength = 0.",
         "Water must be added to 60 litres of milk at ₹24/litre so that the mixture is worth ₹20/litre. Water to add:",
         r"Milk : water $= (20 - 0) : (24 - 20) = 5 : 1$ ⇒ $60/5 = 12$ litres of water."),
   trick("Alligation on averages",
         "Any average — salary, age, marks — alligates the same way.",
         "A class of 50 has an average weight of 42 kg; boys average 45 kg, girls 40 kg. The number of girls is:",
         r"Boys : girls $= (42-40) : (45-42) = 2 : 3$ ⇒ girls $= 30$.")],
  [r"Not crossing over — writing cheaper : dearer = (mean − cheaper) : (dearer − mean), which inverts the ratio.",
   "Alligating a mean that lies outside the two values (impossible — check bounds first).",
   "Forgetting water/pure ingredient has strength 0% or 100%, not 'no value'.",
   "Using alligation where averaging is not linear (e.g. average speeds for unequal distances)."]),

 sub("mix-replacement", "Replacement & Repeated Operations",
  md(r"Remove some mixture and replace it with another liquid — each operation multiplies the original liquid by a shrink factor.",
     "",
     r"**Equal-volume replacements** (take r litres from a vessel of C litres, any number of times):",
     r"$$\text{original liquid left} = C\left(1 - \frac{r}{C}\right)^n$$",
     "",
     r"**Different replacement strengths:** multiply the surviving fractions: $\left(1 - \frac{r_1}{C}\right)\left(1 - \frac{r_2}{C}\right)\cdots$",
     "",
     r"**Partial removal of one ingredient** (drawn mixture changes only the drawn part): remove the ingredient's proportional share: lost = removed $\times \frac{\text{ingredient fraction}}{1}$.",
     "",
     r"The ratio of original : added liquid after n operations is $\left(1-\frac{r}{C}\right)^n : \left[1 - \left(1-\frac{r}{C}\right)^n\right]$."),
  [formula("Repeated equal replacement", r"C\left(1 - \frac{r}{C}\right)^n"),
   formula("Milk : water after n ops", r"\left(1-\frac{r}{C}\right)^n : \left[1-\left(1-\frac{r}{C}\right)^n\right]"),
   formula("Proportional removal", r"\text{lost} = \text{removed volume} \times \frac{\text{ingredient share}}{\text{total}}"),
   formula("Chain of replacements", r"C \prod_k \left(1 - \frac{r_k}{C}\right)")],
  [trick("The (1 − r/C)ⁿ shrink",
         "One fraction per operation; multiply.",
         "From a vessel full of milk, 8 litres are drawn and replaced with water; the operation is repeated once more. The ratio of milk to water in the vessel (capacity 80 L) is:",
         r"Milk left $= 80 \times \frac{9}{10} = 72$ after one draw ⇒ milk : water $= 72 : 8 = 9 : 1$."),
   trick("Two operations, wine : water",
         "Square the shrink factor; the complement is the water.",
         "8 litres are drawn from a cask full of wine and replaced with water; this is done once more. The ratio of wine to water is then 16 : 9. The capacity of the cask is:",
         r"$\left(1 - \frac{8}{C}\right)^2 = \frac{16}{25}$ ⇒ $1 - \frac{8}{C} = \frac{4}{5}$ ⇒ $C = 40$ litres."),
   trick("Draw-and-refill with a ratio shift",
         "Removing uniform mixture deletes each ingredient proportionally; only the drawn fraction matters.",
         "A vessel has milk and water in the ratio 7 : 5. Nine litres of the mixture are removed and replaced with water, making the ratio 7 : 9. The quantity of milk initially is:",
         r"Total T: milk goes from $\frac{7}{12}T$ to $\frac{7}{16}T$; drawn milk $= 9 \times \frac{7}{12}$, so $\frac{7T}{12} - \frac{63}{12} = \frac{7T}{16}$ ⇒ $T = 36$ ⇒ milk $= 21$ litres.")],
  [r"Using $C\left(1 - \frac{r}{C}\right)^n$ when different volumes are drawn each time — multiply the varying factors instead.",
   "Forgetting the vessel's total stays constant when you replace (drain + refill keeps capacity).",
   "Computing water left by shrinking water too — added water enters whole, only the original liquid shrinks.",
   "In ratio-shift problems, subtracting the drawn amount from the total as well as from the ingredient (total is unchanged after refill)."]),

 sub("mix-ratio-profit", "Milk–Water Ratio & Profit by Adulteration",
  md(r"The seller's game: mix in free (or cheap) water and sell at the milk price.",
     "",
     r"**Profit % when water is mixed and the mixture is sold at cost:**",
     r"$$\text{profit\%} = \frac{\text{water}}{\text{milk}} \times 100 = \frac{w}{m} \times 100$$",
     "",
     r"**To reach a wanted ratio**, fix the constant ingredient and solve for the added one — one linear equation, never a system.",
     "",
     r"**To alter an alloy**, compute each metal from the current ratio first, then add/subtract the named metal and rebuild."),
  [formula("Adulteration profit", r"\text{profit\%} = \frac{\text{water}}{\text{milk}} \times 100"),
   formula("Ratio target", r"\frac{m}{w + x} = \text{wanted ratio} \Rightarrow x"),
   formula("Alloy rebuild", r"\text{metal} = \text{alloy weight} \times \frac{\text{share}}{\text{sum of shares}}"),
   formula("SP of mixture", r"\text{SP} = (\text{milk}) \times \text{milk price} + (\text{water}) \times 0")],
  [trick("Water-over-milk is the profit",
         "Adulteration profit = free litres per honest litre.",
         "A milkman mixes 1 litre of water with every 5 litres of milk and sells the mixture at the cost price of milk. His profit per cent is:",
         r"$\frac{1}{5} \times 100 = 20\%$."),
   trick("Hit the target ratio by addition",
         "Keep the bigger quantity constant; solve for the addition.",
         "36 litres of a mixture has milk and water in the ratio 5 : 1. How much water must be added to make the ratio 5 : 3?",
         r"Milk 30 L stays; water must reach $30 \times \frac{3}{5} = 18$ ⇒ add $18 - 6 = 12$ litres."),
   trick("Rebuild the alloy, then change one metal",
         "Convert ratio to grams, adjust, re-ratio.",
         "An alloy of 40 g contains zinc and copper in the ratio 5 : 3. How much copper must be added to make the ratio 5 : 7?",
         r"Zinc 25 g, copper 15 g; want zinc : copper $= 5 : 7$ ⇒ copper $= 35$ ⇒ add $20$ g.")],
  [r"Computing profit on the mixture instead of the milk cost (profit = water/milk, sold at cost).",
   "Adding water and expecting the milk quantity to stretch — only water grows.",
   r"In alloy problems, adding to the total and to one metal without updating the other ratio leg.",
   "Misreading 'ratio 5 : 7' as 'add 7 parts' instead of solving for the new copper amount."]),

 sub("mix-mixtures", "Mixing Two Mixtures",
  md(r"When two ready mixtures (each with its own ratio) are combined, work with **fractions of one chosen ingredient** — never with both ratios at once.",
     "",
     r"$$\text{mixed fraction} = \frac{\sum (\text{volume}_i \times \text{fraction}_i)}{\sum \text{volume}_i}$$",
     "",
     r"Alligation shortcut: to get a target milk fraction f, mix volumes in the ratio $(f_2 - f) : (f - f_1)$ where $f_1, f_2$ are the two vessels' milk fractions.",
     "",
     "Convert each ratio to the fraction of the SAME ingredient first (milk or water), then mix."),
  [formula("Blend of two mixtures", r"f = \frac{V_1 f_1 + V_2 f_2}{V_1 + V_2}"),
   formula("Volumes for target fraction", r"\frac{V_1}{V_2} = \frac{f_2 - f}{f - f_1}"),
   formula("Fraction from ratio", r"f_{\text{milk}} = \frac{m}{m + w}")],
  [trick("Fractions first, then average",
         "Ratio → milk fraction per vessel → weighted average.",
         "Two vessels contain milk and water in the ratios 3 : 1 and 5 : 3. Equal volumes are mixed. The ratio of milk to water in the new mixture is:",
         r"Milk fraction $= \frac{1}{2}\left(\frac{3}{4} + \frac{5}{8}\right) = \frac{11}{16}$ ⇒ milk : water $= 11 : 5$."),
   trick("Alligate the fractions",
         "Target fraction sits between the two vessel fractions; distances give volumes.",
         "Vessel A has 70% milk, vessel B has 30% milk. In what ratio should they be mixed to get a 50% milk mixture?",
         r"$V_A : V_B = (50 - 30) : (70 - 50) = 1 : 1$."),
   trick("Unequal volumes — weight the fractions",
         "Multiply each vessel's milk fraction by its volume before adding.",
         "A 60-litre vessel has milk and water in the ratio 2 : 1 and a 40-litre vessel in the ratio 1 : 1. They are poured together. The milk fraction of the blend is:",
         r"Milk $= 60 \times \frac{2}{3} + 40 \times \frac{1}{2} = 60$; total 100 L ⇒ $60\%$ milk.")],
  [r"Averaging the two ratios directly ($3{:}1$ and $5{:}3$ do not average to $4{:}2$).",
   "Mixing fractions of milk with fractions of water inconsistently — pick one ingredient.",
   "Ignoring unequal volumes when blending two mixtures.",
   "Forgetting to reduce each ratio to its fraction of the total before blending."]),
]

pyq = [
 pat("Two-ingredient mixing to a target price/strength", "very common",
     "Rice at two rates, two acid strengths, two alloys — 'in what ratio to mix for ₹X / x%'.",
     "Alligation: cheaper : dearer = (dearer − mean) : (mean − cheaper). Cross the distances."),
 pat("Replacement with water (repeated)", "very common",
     "Draw r litres, refill, repeat n times; find what's left or the final ratio.",
     r"$C(1 - r/C)^n$ for the original liquid; the complement is the replacement. Square/cube the shrink factor."),
 pat("Add water / add ingredient to change concentration", "common",
     "How much water to add to dilute from a% to b% — or ingredient to strengthen.",
     "Alligate with water = 0 (or pure = 100). Or fix the unchanged quantity and solve one equation."),
 pat("Milk–water ratio after adding/draining", "common",
     "A ratio is given; water added or mixture removed; find the new ratio or the addition.",
     "Track the constant ingredient, set the wanted ratio, solve for the single unknown volume."),
 pat("Adulteration profit (water in milk)", "common",
     "Water mixed and sold at cost — find profit %, or water needed for a target profit.",
     "Profit % = water/milk × 100 when sold at cost. Reverse: water = profit% of milk."),
 pat("Mixing two ready mixtures", "common",
     "Two vessels with their own milk:water ratios combined (equal or unequal volumes).",
     "Convert each ratio to an ingredient fraction, weight by volume, rebuild the ratio."),
 pat("Alligation on averages (salary, age, marks, speed)", "common",
     "Group averages and the combined average are given; find group sizes or one average.",
     "Same crossing rule: n₁ : n₂ = (v₂ − mean) : (mean − v₁)."),
 pat("Dishonest ratios: replacing part of stock", "occasional",
     "A trader replaces sold milk with water to keep volume, or draws partial mixture with a ratio shift.",
     "Apply the proportional-removal rule; the drawn amount deletes each ingredient by its own share."),
]

solved = []
assert F(6, 4) == Fr(3, 2)
solved.append(Q("mix-s01", "In what ratio must rice costing ₹30 per kg be mixed with rice costing ₹20 per kg so that the mixture is worth ₹24 per kg?",
  ["1 : 2", "2 : 1", "2 : 3", "3 : 2"], 3, (1, Fr(2, 3)),
  md(r"Cheaper : dearer $= (30 - 24) : (24 - 20) = 6 : 4 = 3 : 2$."),
  "Alligation: dearer−mean : mean−cheaper, crossed over ⇒ 3 : 2.",
  "easy", "mix-alligation", "price alligation", 30))

assert 60 * F(40, 100) == 24 and Fr(24, 120) == Fr(1, 5)
solved.append(Q("mix-s02", "60 litres of a 40% acid solution is diluted by adding water so that the solution becomes 20% acid. The quantity of water added is:",
  ["40 litres", "50 litres", "60 litres", "80 litres"], 2, 60,
  md(r"Acid $= 60 \times 0.4 = 24$ L must be $20\%$ of the new total.",
     r"New total $= \frac{24}{0.2} = 120$ L ⇒ add $120 - 60 = 60$ litres."),
  "Acid constant: 24/0.20 = 120 total ⇒ 60 L water.",
  "easy", "mix-basics", "dilution", 30))

assert 60 * Fr(9, 10)**2 == Fr(243, 5)
solved.append(Q("mix-s03", "A vessel contains 60 litres of milk. 6 litres are drawn and replaced with water, and the operation is repeated once more. The quantity of milk left in the vessel is:",
  ["48 litres", "48.6 litres", "49 litres", "50.4 litres"], 1, Fr(243, 5),
  md(r"$60\left(1 - \frac{6}{60}\right)^2 = 60 \times 0.81 = 48.6$ litres."),
  "Shrink twice by 9/10: 60 × 0.81 = 48.6 L.",
  "medium", "mix-replacement", "repeated replacement", 40))

assert 36 * F(5, 6) == 30 and 30 * F(3, 5) - 6 == 12
solved.append(Q("mix-s04", "36 litres of a mixture contains milk and water in the ratio 5 : 1. How much water must be added to make the ratio 5 : 3?",
  ["8 litres", "10 litres", "12 litres", "18 litres"], 2, 12,
  md(r"Milk $= 36 \times \frac{5}{6} = 30$ L (unchanged).",
     r"Water must become $30 \times \frac{3}{5} = 18$ L ⇒ add $18 - 6 = 12$ litres."),
  "Milk constant at 30; water 6 → 18 by the 5 : 3 ratio ⇒ +12 L.",
  "medium", "mix-ratio-profit", "ratio target", 35))

assert F(42 - 40, 45 - 42) == Fr(2, 3)
solved.append(Q("mix-s05", "In an office of 60 employees, the average salary is ₹8,000. Managers average ₹10,000 and executives average ₹6,000. The number of managers is:",
  ["20", "25", "30", "35"], 2, 30,
  md(r"Managers : executives $= (8000 - 6000) : (10000 - 8000) = 1 : 1$.",
     r"Managers $= 30$."),
  "Alligation on averages: distances 2000 and 2000 ⇒ equal split.",
  "easy", "mix-alligation", "average alligation", 30))

# ------------------------------------------------------------------ practice
P = []

assert 40 * F(1, 4) == 10
P.append(Q("mix-q01", "A 40-litre mixture contains milk and water in the ratio 3 : 1. The quantity of water in the mixture is:",
  ["8 litres", "10 litres", "12 litres", "15 litres"], 1, 10,
  md(r"Water $= 40 \times \frac{1}{4} = 10$ litres."),
  "1 part of 4 ⇒ 40/4 = 10 L.",
  "easy", "mix-basics", "amount from ratio", 20))

assert F(10, 15) == F(2, 3)
P.append(Q("mix-q02", "In what ratio should a 25% acid solution be mixed with a 50% acid solution to obtain a 40% acid solution?",
  ["1 : 2", "2 : 1", "2 : 3", "3 : 2"], 2, (1, Fr(3, 2)),
  md(r"$V_{25} : V_{50} = (50 - 40) : (40 - 25) = 10 : 15 = 2 : 3$."),
  "Cross the distances from the mean 40 ⇒ 2 : 3.",
  "easy", "mix-alligation", "strength alligation", 25))

assert F(72, 8) == 9
P.append(Q("mix-q03", "A vessel contains 80 litres of pure milk. 8 litres are withdrawn and replaced with water. The ratio of milk to water in the vessel now is:",
  ["7 : 1", "8 : 1", "9 : 1", "10 : 1"], 2, (1, Fr(1, 9)),
  md(r"Milk left $= 72$ L, water $= 8$ L ⇒ $9 : 1$."),
  "One 10% draw: milk 72, water 8.",
  "easy", "mix-replacement", "single replacement", 25))

assert F(6, 6) == 1
P.append(Q("mix-q04", "In what ratio must rice at ₹36 per kg be mixed with rice at ₹24 per kg so that the mixture costs ₹30 per kg?",
  ["1 : 2", "1 : 1", "2 : 1", "3 : 2"], 1, (1, 1),
  md(r"Cheaper : dearer $= (36 - 30) : (30 - 24) = 6 : 6 = 1 : 1$."),
  "Mean 30 is midway ⇒ equal quantities.",
  "easy", "mix-alligation", "price alligation", 25))

assert 40 * F(3, 5) == 24 and Fr(12, 25) == F(12, 25)
P.append(Q("mix-q05", "20 litres of a mixture contains 60% milk. After 5 litres of water are added, the percentage of milk in the mixture is:",
  ["44%", "46%", "48%", "50%"], 2, 48,
  md(r"Milk $= 12$ L; new total $= 25$ L ⇒ $\frac{12}{25} = 48\%$."),
  "Milk fixed at 12; 12/25 = 48%.",
  "easy", "mix-basics", "dilution", 25))

assert F(50, 5) == 10 and 20 - 10 == 10
P.append(Q("mix-q06", "A 50-litre mixture of milk and water is in the ratio 4 : 1. How much water must be added to make the ratio 2 : 1?",
  ["5 litres", "8 litres", "10 litres", "12 litres"], 2, 10,
  md(r"Milk 40 L must be $\frac{2}{3}$ of the new total ⇒ water total $= 20$ L.",
     r"Add $20 - 10 = 10$ litres."),
  "Milk constant 40 ⇒ water must reach 20 ⇒ +10 L.",
  "medium", "mix-basics", "ratio target", 35))

assert 25 * F(7, 5) == 35 and 35 - 15 == 20
P.append(Q("mix-q07", "An alloy of 40 grams contains zinc and copper in the ratio 5 : 3. How much copper must be added so that the ratio becomes 5 : 7?",
  ["15 g", "18 g", "20 g", "24 g"], 2, 20,
  md(r"Zinc 25 g, copper 15 g. Want $\frac{25}{15 + x} = \frac{5}{7}$ ⇒ $15 + x = 35$ ⇒ $x = 20$ g."),
  "Zinc constant 25; copper must reach 35 ⇒ add 20 g.",
  "medium", "mix-ratio-profit", "alloy rebuild", 35))

assert 100 * Fr(4, 5)**2 == 64
P.append(Q("mix-q08", "A vessel contains 100 litres of milk. 20 litres are drawn and replaced with water; the operation is performed twice in all. The quantity of milk left is:",
  ["60 litres", "64 litres", "68 litres", "72 litres"], 1, 64,
  md(r"$100\left(1 - \frac{20}{100}\right)^2 = 100 \times 0.64 = 64$ litres."),
  "Shrink twice by 4/5 ⇒ 64 L.",
  "medium", "mix-replacement", "repeated replacement", 35))

assert Fr(3, 4) * Fr(1, 2) + Fr(5, 8) * Fr(1, 2) == Fr(11, 16)
P.append(Q("mix-q09", "Two vessels contain milk and water in the ratios 3 : 1 and 5 : 3. Equal volumes from both are mixed. The ratio of milk to water in the resulting mixture is:",
  ["7 : 5", "8 : 5", "11 : 5", "11 : 6"], 2, (1, Fr(5, 11)),
  md(r"Milk fraction $= \frac{1}{2}\left(\frac{3}{4} + \frac{5}{8}\right) = \frac{11}{16}$ ⇒ milk : water $= 11 : 5$."),
  "Average the milk fractions (equal volumes): 11/16 ⇒ 11 : 5.",
  "medium", "mix-mixtures", "mixing two mixtures", 40))

assert F(1, 5) == F(20, 100)
P.append(Q("mix-q10", "A milkman mixes 1 litre of water with every 5 litres of milk and sells the mixture at the cost price of milk. His profit per cent is:",
  ["16.67%", "20%", "25%", "33.33%"], 1, 20,
  md(r"Profit $= \frac{\text{water}}{\text{milk}} \times 100 = \frac{1}{5} \times 100 = 20\%$."),
  "Free water per honest litre = profit fraction ⇒ 20%.",
  "medium", "mix-ratio-profit", "adulteration profit", 30))

assert F(2, 5) == F(20, 50) and F(3, 5) == F(30, 50)
P.append(Q("mix-q11", "In a class of 50 students the average marks are 42. Boys average 45 marks and girls average 40 marks. The number of girls in the class is:",
  ["20", "25", "30", "35"], 2, 30,
  md(r"Boys : girls $= (42 - 40) : (45 - 42) = 2 : 3$ ⇒ girls $= 50 \times \frac{3}{5} = 30$."),
  "Alligation on averages ⇒ 2 : 3 split ⇒ 30 girls.",
  "medium", "mix-alligation", "average alligation", 35))

assert F(20, 4) == 5 and Fr(60, 5) == 12
P.append(Q("mix-q12", "How much water costing nothing must be added to 60 litres of milk at ₹24 per litre so that the mixture is worth ₹20 per litre?",
  ["10 litres", "12 litres", "15 litres", "20 litres"], 1, 12,
  md(r"Milk : water $= (20 - 0) : (24 - 20) = 5 : 1$.",
     r"Water $= \frac{60}{5} = 12$ litres."),
  "Water is the 0-price ingredient: alligate ⇒ 5 : 1 ⇒ 12 L.",
  "medium", "mix-alligation", "water as free ingredient", 35))

x = Fr(36)
assert x * Fr(7, 12) == 21 and (x * Fr(7, 12) - 9 * Fr(7, 12)) / x == Fr(7, 16)
P.append(Q("mix-q13", "A vessel contains milk and water in the ratio 7 : 5. When 9 litres of the mixture are removed and replaced with water, the ratio becomes 7 : 9. The quantity of milk in the vessel initially was:",
  ["18 litres", "21 litres", "24 litres", "28 litres"], 1, 21,
  md(r"Let total be T. Milk falls from $\frac{7T}{12}$ to $\frac{7T}{16}$; the 9 removed litres carry away $9 \times \frac{7}{12}$ milk.",
     r"$\frac{7T}{12} - \frac{63}{12} = \frac{7T}{16}$ ⇒ $7T \times 4 - 63 \times 4 = 7T \times 3$ ⇒ $T = 36$.",
     r"Milk $= \frac{7 \times 36}{12} = 21$ litres."),
  "Only milk shrinks, by the drawn fraction: solve the one-step equation, T = 36, milk = 21 L.",
  "hard", "mix-replacement", "partial removal ratio shift", 60))

assert 40 * Fr(9, 10)**3 == Fr(729, 25)
P.append(Q("mix-q14", "A vessel is full of 40 litres of pure milk. 4 litres are drawn and replaced with water, and this operation is repeated two more times (three replacements in all). The ratio of milk to water in the vessel is now:",
  ["729 : 271", "729 : 280", "81 : 19", "9 : 1"], 0, (1, Fr(271, 729)),
  md(r"Milk left $= 40\left(\frac{9}{10}\right)^3 = 29.16$ L ⇒ water $= 10.84$ L.",
     r"$29.16 : 10.84 = 729 : 271$."),
  "(9/10)³ = 729/1000 of the milk survives; ratio 729 : 271.",
  "hard", "mix-replacement", "triple replacement ratio", 55))

assert Fr(4, 5)**2 == F(16, 25) and 5 * 8 == 40
P.append(Q("mix-q15", "8 litres are drawn from a cask full of wine and replaced with water. The operation is performed once more, after which the cask contains wine and water in the ratio 16 : 9. The capacity of the cask is:",
  ["32 litres", "36 litres", "40 litres", "48 litres"], 2, 40,
  md(r"Wine fraction $= \frac{16}{25} = \left(1 - \frac{8}{C}\right)^2$.",
     r"$1 - \frac{8}{C} = \frac{4}{5}$ ⇒ $C = 40$ litres."),
  "16/25 = (4/5)² ⇒ each draw removes 1/5 ⇒ C = 40 L.",
  "hard", "mix-replacement", "reverse replacement", 55))

topic = {
 "id": "mixture-alligation", "sectionId": "quant", "title": "Mixtures & Alligation", "order": 9,
 "importance": "high", "avgQuestions": {"tier1": 1, "tier2": 2},
 "summary": "Alligation is the highest-leverage tool in arithmetic — it solves mixtures, dilutions, adulteration profits and even average-group questions in one crossing. Replacement chains and two-mixture blending complete the set. Expect one sure question per Tier 1 shift and more in Tier 2.",
 "subtopics": subtopics, "pyqPatterns": pyq, "solvedExamples": solved, "practice": P,
}
write_topic(topic)
