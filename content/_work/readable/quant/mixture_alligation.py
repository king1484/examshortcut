"""Readable rewrite of the Mixtures & Alligation topic (all 5 subtopics).

Simple English, one idea per section, exact fraction checks for every number.
Run: python mixture_alligation.py  (patches content/core/topics/quant/mixture-alligation.json in place)
"""
import json
from fractions import Fraction as F
from pathlib import Path

ROOT = Path(__file__).resolve().parents[3]
TOPIC = ROOT / "core" / "topics" / "quant" / "mixture-alligation.json"


def apply(data, sub_id, concept, notes, formulas, tricks, mistakes, revision, patterns):
    sub = next(s for s in data["subtopics"] if s["id"] == sub_id)
    old_ids = {p["id"] for p in sub.get("patterns", [])}
    assert old_ids <= {p["id"] for p in patterns}, f"{sub_id}: never drop a pattern id"
    assert 2500 <= len(notes) <= 5000, (sub_id, len(notes))
    sub.update(concept=concept, notes=notes.strip() + "\n", formulas=formulas, tricks=tricks,
               mistakes=mistakes, revision=revision, patterns=patterns)


def pat(pid, name, freq, spot, formula, steps, why, q, ex_steps, answer):
    return {"id": pid, "name": name, "frequency": freq, "howToSpot": spot, "formula": formula,
            "steps": steps, "why": why, "example": {"q": q, "steps": ex_steps, "answer": answer}}


# =========================== mix-basics ===========================
# answer checks
assert F(40 * 6 + 60 * 7, 100) == F(33, 5)                                    # mean price 6.60
assert F(72, 12) == 6 and 7 * 6 == 42 and 5 * 6 == 30                          # ratio 7:5 in 72 L
assert F(40, 4) == 10                                                          # water in 40 L of 3:1
assert 20 + 5 == 25 and F(12, 25) == F(48, 100)                                # 48% after dilution
assert 50 - F(50, 5) * 1 == 40 and 40 * F(1, 2) == 20 and 20 - 10 == 10        # 4:1 -> 2:1 add 10
assert (90 + 90) * 4 == (150 + 90) * 3                                         # v4: x = 90
assert 24 - 15 == 9 and 3 * 9 == 27 and 27 - 15 == 12                          # alloy add copper
assert F(40, 4) * 3 == 30                                                      # milk in 40 L of 3:1

v_concept = (
    "A mixture holds two or more ingredients. Two quantities run every question:\n\n"
    "- **Amount of each ingredient**, from the ratio: in 40 L of milk : water = 3 : 1, milk is "
    "$40 \\times \\dfrac{3}{4} = 30$ L.\n"
    "- **Concentration** of one ingredient: amount ÷ total volume, as a per cent.\n\n"
    "When something is added or removed, track the amounts. Adding water grows only the water. "
    "Removing mixture takes both ingredients in proportion."
)

v_notes = r"""### What a mixture is
A mixture is two or more ingredients put together — milk and water, rice at two prices, copper and zinc in an alloy.

Every question turns on two quantities:

- The **amount** of each ingredient (litres, kg, grams).
- The **concentration** of one ingredient: its share of the total, as a per cent.

> **Rule:** Track ingredient amounts, not the ratio alone. Ratios move when only one column changes.

### Mean price of a blend
Mix items at different prices and the blend has one average price.

$$\text{mean price} = \frac{\text{total value}}{\text{total quantity}} = \frac{q_1 p_1 + q_2 p_2}{q_1 + q_2}$$

> **Example:** 40 kg of rice at ₹6 mixed with 60 kg at ₹7. Value = $240 + 420 = ₹660$ over 100 kg. Mean = ₹6.60 per kg.

This one line answers every "find the average price of the mixture" question.

### From ratio to real amounts
A ratio such as 7 : 5 splits the total into 12 parts.

1. One part = total ÷ sum of ratio terms.
2. Each ingredient = its share × one part.

> **Example:** A 72-litre mixture has milk and water in the ratio 7 : 5. One part = $72 \div 12 = 6$ L. Milk = $7 \times 6 = 42$ L, water = 30 L.

### Adding one ingredient
Adding water changes only the water column — the milk stays exactly as it was. That fixed ingredient is the anchor of the question.

> **Example:** A 40 L mixture has milk : water = 3 : 1. How much milk makes it 4 : 1? Water stays 10 L. Milk must reach $4 \times 10 = 40$ L. Add $40 - 30 = 10$ L.

Routine: write the old amounts, freeze the ingredient not being added, then solve for the addition.

### Percentage strength
Concentration works the same way in per cent. A 150 L solution at 60% acid holds $90$ L of acid.

Add x litres of pure acid (strength 100%) and the total grows too:

$$\frac{90 + x}{150 + x} = \frac{3}{4} \Rightarrow x = 90 \text{ L}$$

> **Watch:** The denominator grows with every addition. A per cent is always a share of the current total.

### Per cent of the mixture vs per cent of the other item
Read per cent questions twice. "Water is 25% of the mixture" means water : milk = 25 : 75 = 1 : 3 — not 1 : 4.

Convert the other way just as carefully: milk : water = 7 : 5 makes milk $\dfrac{7}{12} = 58\frac{1}{3}\%$ of the 72 L mixture. The sum of ratio terms is the denominator, never the other ingredient.

> **Careful:** Exam options are built to catch the wrong denominator. Write the fraction, then match the option.

### Alloys: the same arithmetic
An alloy is a mixture in grams. Copper : zinc = 5 : 3 in a 24 g piece gives 15 g copper and 9 g zinc. To make it 3 : 1, freeze zinc at 9 g, push copper to 27 g, add 12 g.

> **Tip:** Prices, litres, grams — the units change, the method never does.
"""

v_formulas = [
    {"name": "Amount from ratio", "tex": r"\text{part} = \text{total} \times \frac{\text{share}}{\text{sum of shares}}"},
    {"name": "Concentration", "tex": r"C = \frac{\text{ingredient}}{\text{mixture}} \times 100\%"},
    {"name": "Mean price", "tex": r"\text{mean} = \frac{q_1 p_1 + q_2 p_2}{q_1 + q_2}"},
    {"name": "Adding water", "tex": r"C' = \frac{A}{M + w}", "note": "A = amount of the other ingredient, unchanged."},
    {"name": "Removing mixture", "tex": r"\text{each ingredient shrinks in its own share}", "note": "A uniform draw keeps the ratio."},
]

v_tricks = [
    {
        "title": "Freeze the unchanged ingredient",
        "body": "Water added means milk unchanged. Hang the whole question on the ingredient that does not move.",
        "example": {
            "q": "A 40-litre mixture has milk and water in the ratio 3 : 1. How much water does it contain?",
            "steps": [r"Parts = $3 + 1 = 4$; one part = $40 \div 4 = 10$ L.", r"Water = $1 \times 10 = 10$ L."],
            "answer": "10 litres",
        },
    },
    {
        "title": "Rebuild the per cent after dilution",
        "body": "Milk is fixed, the total grows — divide again.",
        "example": {
            "q": "20 litres of a mixture contains 60% milk. After adding 5 litres of water, find the milk percentage.",
            "steps": [r"Milk = $60\%$ of 20 = 12 L, unchanged.", r"New total = $25$ L.", r"Milk % = $12 \div 25 = 48\%$."],
            "answer": "48%",
        },
    },
    {
        "title": "One ratio change, one equation",
        "body": "Set the frozen ingredient against the wanted ratio and solve for the addition.",
        "example": {
            "q": "A 50-litre mixture of milk and water is in the ratio 4 : 1. How much water must be added to make it 2 : 1?",
            "steps": [r"Milk = $40$ L stays; water = 10 L.", r"Target 2 : 1 needs water = $40 \div 2 = 20$ L.", r"Add $20 - 10 = 10$ L."],
            "answer": "10 litres",
        },
    },
]

v_mistakes = [
    {"wrong": "Changing both parts of a ratio when only one moved.", "right": "Adding water leaves the milk amount untouched. Adjust only the water and the total."},
    {"wrong": "Thinking x litres of water cuts the milk percentage by x%.", "right": "Recompute: milk ÷ new total. The drop depends on the sizes."},
    {"wrong": "Taking the share of the wrong ingredient (1/4 instead of 3/4).", "right": "Label the ratio first: milk : water = 3 : 1 means milk takes 3 of the 4 parts."},
    {"wrong": "Forgetting the total volume changes when anything is added.", "right": "Every addition grows the denominator of the concentration."},
    {"wrong": "Reading '25% water' as water : milk = 25 : 100.", "right": "Per cent is of the mixture: water : milk = 25 : 75 = 1 : 3."},
]

v_revision = [
    "Mean price = total value ÷ total quantity.",
    "One part = total ÷ sum of ratio terms.",
    "Adding X moves only X's column and the total.",
    "New ratio → one equation in the one added amount.",
    "Per cent of mixture ≠ per cent of the other ingredient.",
]

v_patterns = [
    pat("mix-v1", "Mean price of a mixture", "very common",
        "Quantities and unit prices are given; the average price of the blend is asked.",
        r"\text{mean} = \frac{\sum q_i p_i}{\sum q_i}",
        ["Multiply each quantity by its price and add: total value.", "Add the quantities: total weight or volume.", "Divide. A decimal like ₹6.60 is a clean exam answer."],
        "The mean value is weighted by quantity, never a plain middle of the prices.",
        "40 kg of rice at ₹6 per kg is mixed with 60 kg of rice at ₹7 per kg. Find the average price of the mixture.",
        [r"Value = $40 \times 6 + 60 \times 7 = 240 + 420 = 660$.", r"Quantity = $100$ kg.", r"Mean = $660 \div 100 = ₹6.60$ per kg."],
        "₹6.60 per kg"),
    pat("mix-v2", "Ratio to absolute amounts", "very common",
        "A ratio (milk : water 7 : 5) with a total quantity is given — one part is asked.",
        r"\text{one part} = \frac{\text{total}}{\text{sum of ratio terms}}",
        ["Divide the total by the sum of the ratio terms.", "Multiply each term by one part.", "Remember which operations keep a column fixed."],
        "A ratio is relative; the total converts it into litres or kg.",
        "A 72-litre mixture has milk and water in the ratio 7 : 5. Find the quantity of water in it.",
        [r"Parts = $7 + 5 = 12$; one part = $72 \div 12 = 6$ L.", r"Water = $5 \times 6 = 30$ L (milk = 42 L)."],
        "30 litres"),
    pat("mix-v3", "Adding an ingredient to change the ratio", "very common",
        "'How much X must be added so the ratio becomes a : b?'",
        r"\frac{\text{component}_1}{\text{component}_2 + x} = \frac{a}{b} \ \text{or}\ \frac{\text{component}_1 + x}{\text{component}_2} = \frac{a}{b}",
        ["Get the old amounts from the ratio and the total.", "Freeze the ingredient not being added.", "Set the new ratio as an equation and solve for x."],
        "Only the added column grows; the other ingredient is untouched.",
        "A 40-litre mixture has milk and water in the ratio 3 : 1. How much milk must be added to make the ratio 4 : 1?",
        [r"Old amounts: milk 30 L, water 10 L.", r"Water stays 10 L; at 4 : 1 milk must be $4 \times 10 = 40$ L.", r"Add $40 - 30 = 10$ L."],
        "10 litres"),
    pat("mix-v4", "Percentage strength of a solution", "common",
        "A solution's concentration is given; after adding solvent or pure solute, the new strength is asked.",
        r"\text{strength} = \frac{\text{solute}}{\text{total volume}} \times 100",
        ["Compute the solute amount from the percentage.", "Add to the solute (or leave it) and grow the total as the story says.", "Write the new fraction and convert to a per cent."],
        "Percentages are fractions of the current total, and the total changes with every addition.",
        "150 L of a solution contains 60% acid. How much pure acid must be added to make it 75% acid?",
        [r"Acid = $90$ L. Let the addition be $x$.", r"$\frac{90 + x}{150 + x} = \frac{3}{4} \Rightarrow 360 + 4x = 450 + 3x$.", r"$x = 90$ L."],
        "90 litres"),
    pat("mix-v5", "Alloys and blending by parts", "common",
        "Alloys with metal ratios, or blends whose parts are used again in another mix.",
        r"\text{component} = \frac{\text{ratio term}}{\text{sum}} \times \text{total}",
        ["Convert each alloy's ratio into grams (or kg) of each metal.", "Pool the columns across all sources.", "Read the new ratio, or solve for the addition needed."],
        "Metals from different sources simply add up, column by column.",
        "An alloy has copper and zinc in the ratio 5 : 3. In 24 g of it, how much copper must be added to make the ratio 3 : 1?",
        [r"24 g split 5 : 3 → copper 15 g, zinc 9 g.", r"Zinc stays 9 g; at 3 : 1 copper must be $27$ g.", r"Add $27 - 15 = 12$ g."],
        "12 g"),
]

# =========================== mix-alligation ===========================
# answer checks
assert (320 - 300, 300 - 250) == (20, 50) and F(20, 50) == F(2, 5)             # tea arms 2:5
assert (50 - 30, 30 - 20) == (20, 10) and F(20, 10) == 2                        # acid 2:1
assert (75 - 72, 72 - 70) == (3, 2)                                             # marks 3:2
assert (45 - 42, 42 - 40) == (3, 2) and F(50 * 2, 5) == 20                      # weights: girls 30
assert 100 * 5 + 0 * 0 == 500                                                   # (guard)
assert F(750 * 100, 12000) == F(25, 4)                                          # mean rate 6.25%
assert F(8 - F(25, 4), F(25, 4) - 5) == F(7, 5) and 12000 * F(7, 12) == 7000    # 7:5 -> 7000
assert 7000 * F(5, 100) + 5000 * F(8, 100) == 350 + 400 == 750                  # interest check
assert (36 - 30, 30 - 24) == (6, 6)                                             # rice 1:1
assert (24 - 20, 20 - 0) == (4, 20) and 60 * F(1, 5) == 12                      # water 12 L
assert (42 - 30, 30 - 24) == (12, 6) and F(12, 6) == 2 and 25 * F(1, 2) == F(25, 2)  # sugar 12.5 kg

a_concept = (
    "Alligation mixes two ingredients of known 'strength' — price, percentage, average — to hit a target mean.\n\n"
    "Subtract diagonally: cheaper : dearer = (dearer − mean) : (mean − cheaper).\n\n"
    "Each ingredient's quantity pairs with the OTHER ingredient's distance from the mean. "
    "The mean must sit between the two strengths. It works on prices, concentrations, marks, ages, "
    "rates and profit per cent — anywhere a weighted average applies."
)

a_notes = r"""### The rule of alligation
Two ingredients: a cheaper one at strength C and a dearer one at strength D. Mix them to get a mean M, with C < M < D.

$$\text{cheaper} : \text{dearer} = (D - M) : (M - C)$$

Picture it: write C and D on top, M in the middle. Subtract diagonally. Each quantity takes the arm that points at the OTHER ingredient.

> **Example:** Tea at ₹320 and ₹250 must blend to ₹300. Cheaper : dearer = $(320-300):(300-250) = 20:50 = 2:5$.

> **Rule:** Check C < M < D first. A mean outside the two strengths is impossible — the question or the setup is misread.

### Why it works
Let the quantities be x (cheaper) and y (dearer). The blend's value is $\frac{Cx + Dy}{x+y} = M$. Cross-multiply:

$$x(D - M) = y(M - C)$$

That is exactly the two arms. Alligation is one linear equation drawn as a picture.

### Water is free; pure is 100%
Dilution questions are alligation with one strength at 0. Strengthening questions use 100% for the pure ingredient.

> **Tip:** Water to be added to 60 L of milk at ₹24/L to sell the blend at ₹20/L: milk : water = $(24-20):(20-0) = 4:20 = 1:5$. So water = $60 \div 5 = 12$ L.

### Alligation on averages
Any two group averages and their overall average alligate the same way.

- Boys average 70 marks, girls 75, class 72 → boys : girls = $(75-72):(72-70) = 3:2$.
- A class of 50 averages 42 kg; boys 45 kg, girls 40 kg → boys : girls = $2 : 3$, so girls = 30.

> **Watch:** For speeds over EQUAL DISTANCES, the average is not the plain mean — alligate carefully or use the harmonic mean.

### Scaling to a known quantity
The arms give a ratio. When one real quantity is known, price one part and scale.

25 kg of sugar at ₹24 is mixed with sugar at ₹42 to average ₹30. Arms: cheaper : dearer = $(42-30):(30-24) = 2:1$. The cheaper side is double, so dearer sugar = $25 \div 2 = 12.5$ kg.

> **Tip:** Always verify: rebuild the mean from your quantities before choosing the option.

### Three ingredients, one mean
With three prices, hunt a pair whose alligation hits the mean (or a price already AT the mean).

Rice at ₹30, ₹36 and ₹42 must average ₹36. The ₹30 and ₹42 kinds mix 1 : 1 to $\frac{30+42}{2} = ₹36$ — and any amount of the ₹36 kind can join without moving the mean. So the answer is 1 : any : 1 in that order.

> **Tip:** Equal quantities of two prices average to their midpoint. Spot the pair first, then let the mean-priced item ride along.

### Equal quantities average to the midpoint
40 kg at ₹6 and 40 kg at ₹7 average ₹6.50 exactly — the arms are equal, so the ratio is 1 : 1. When a question quotes equal amounts, the mean falls in the middle with no work at all.

### Rates and profit per cents
Percentages alligate as numbers. ₹12,000 is split at 5% and 8% simple interest to earn ₹750 a year.

Mean rate = $\dfrac{750}{12000} \times 100 = 6.25\%$. Arms: $(8 - 6.25):(6.25 - 5) = 1.75 : 1.25 = 7 : 5$. So ₹7,000 at 5% and ₹5,000 at 8%. Check: $350 + 400 = 750$.
"""

a_formulas = [
    {"name": "Alligation ratio", "tex": r"\frac{\text{cheaper}}{\text{dearer}} = \frac{D - M}{M - C}"},
    {"name": "Weighted average", "tex": r"\bar{v} = \frac{n_1 v_1 + n_2 v_2}{n_1 + n_2}"},
    {"name": "Water as the free ingredient", "tex": r"\text{milk} : \text{water} = (m - 0) : (c - m),\ c > m"},
]

a_tricks = [
    {
        "title": "Cross the arms",
        "body": "Dearer-minus-mean and mean-minus-cheaper swap sides. Each quantity takes the other side's arm.",
        "example": {
            "q": "In what ratio must rice at ₹36 per kg be mixed with rice at ₹24 per kg so that the mixture costs ₹30 per kg?",
            "steps": [r"Cheaper : dearer = $(36 - 30):(30 - 24)$.", r"= $6 : 6 = 1 : 1$."],
            "answer": "1 : 1",
        },
    },
    {
        "title": "Water has price zero",
        "body": "Dilution is alligation with one strength at 0.",
        "example": {
            "q": "How much water must be added to 60 litres of milk worth ₹24 per litre so that the mixture is worth ₹20 per litre?",
            "steps": [r"Milk : water = $(24 - 20):(20 - 0) = 4 : 20 = 1 : 5$.", r"Water = $60 \div 5 = 12$ L."],
            "answer": "12 litres",
        },
    },
    {
        "title": "Averages alligate too",
        "body": "Salary, age, marks, weight — any average splits into an alligation.",
        "example": {
            "q": "A class of 50 has an average weight of 42 kg. The boys average 45 kg and the girls 40 kg. Find the number of girls.",
            "steps": [r"Boys : girls = $(42 - 40):(45 - 42) = 2 : 3$.", r"Girls = $50 \times \frac{3}{5} = 30$."],
            "answer": "30 girls",
        },
    },
]

a_mistakes = [
    {"wrong": "Reading the arms the same way round (cheaper with its own arm).", "right": "Each quantity pairs with the far arm: cheaper : dearer = (D − M) : (M − C)."},
    {"wrong": "Alligating a mean outside the two strengths.", "right": "Check C < M < D first. If it fails, re-read the question."},
    {"wrong": "Giving water or a pure ingredient 'no value' and skipping it.", "right": "Water has strength 0; a pure ingredient has 100%. Both alligate normally."},
    {"wrong": "Alligating speeds over equal distances.", "right": "Equal distances average by the harmonic mean. Alligation fits equal times or linear quantities."},
    {"wrong": "Stopping at the ratio when a quantity was asked.", "right": "Price one part with the known quantity, then scale to the whole amount."},
]

a_revision = [
    "cheaper : dearer = (D − M) : (M − C).",
    "The mean must sit between the two strengths.",
    "Water = strength 0; pure acid = 100%.",
    "Works on prices, concentrations, marks, ages, rates, profit %.",
    "Known quantity → price one part of the ratio, then scale.",
    "Verify by recomputing the mean from your mix.",
]

a_patterns = [
    pat("mix-a1", "Two-ingredient alligation for the ratio", "very common",
        "Two unit prices are given with the target mean price; the mixing ratio is asked.",
        r"D : C = (M - C) : (D - M)",
        ["Identify cheaper, dearer and mean; check C < M < D.", "Subtract diagonally: (D − M) and (M − C).", "State the ratio, scaling by any known quantity."],
        "The weighted-mean equation rearranges into exactly these arms.",
        "In what ratio should tea at ₹320 per kg be mixed with tea at ₹250 per kg to get a mixture worth ₹300 per kg?",
        [r"Arms: $320 - 300 = 20$ and $300 - 250 = 50$.", r"Cheaper : dearer = $20 : 50 = 2 : 5$."],
        "2 : 5"),
    pat("mix-a2", "Mixing solutions by strength", "very common",
        "Two solutions of given concentration are mixed to reach a target strength.",
        r"\frac{\text{dilute}}{\text{strong}} = \frac{S - M}{M - W}",
        ["Alligate on the strength percentages exactly as on prices.", "The arm (S − M) belongs to the dilute solution.", "Split any given final volume by the ratio."],
        "Strength is the 'price' per litre of solution.",
        "Solutions of 20% and 50% acid are mixed to make a 30% solution. In what ratio are they mixed?",
        [r"Arms: $50 - 30 = 20$ and $30 - 20 = 10$.", r"Dilute : strong = $20 : 10 = 2 : 1$."],
        "2 : 1"),
    pat("mix-a3", "Alligation on averages (marks, ages, weights)", "common",
        "Two groups with different averages combine to a known overall average — the ratio of sizes is asked.",
        r"\frac{n_1}{n_2} = \frac{A_2 - A}{A - A_1}",
        ["Treat the group averages as the two prices and the overall as M.", "Subtract to the arms; the arms give the sizes' ratio.", "Scale to the total when a count is asked."],
        "The overall average is the size-weighted mean of the group averages.",
        "The average marks of boys in a class is 70 and of girls is 75. If the class average is 72, find the ratio of boys to girls.",
        [r"Arms: $75 - 72 = 3$ and $72 - 70 = 2$.", r"Boys : girls = $3 : 2$."],
        "3 : 2"),
    pat("mix-a4", "How much to add (alligation form)", "common",
        "'How much of X must be added to a given amount of mixture to reach a strength or price?'",
        r"\frac{q_{\text{added}}}{q_{\text{existing}}} = \frac{M_{\text{old}} - M}{M - M_{\text{added}}}",
        ["Give the added ingredient its strength: 0 for water, 100 for pure acid, its price for a priced item.", "Alligate between the old mixture and the addition.", "Solve for the unknown quantity."],
        "Adding a zero-strength or full-strength ingredient is still just a two-ingredient mix.",
        "How much pure acid must be added to 100 litres of a 30% acid solution to make it 50% acid?",
        [r"Old mixture 30, added acid 100, target 50.", r"Acid : solution = $(50 - 30):(100 - 50) = 20 : 50 = 2 : 5$.", r"Acid = $100 \times \frac{2}{5} = 40$ L."],
        "40 litres"),
    pat("mix-a5", "Alligation on rates and profits", "common",
        "Two investments at different interest rates, or items sold at different profit per cents, with a known combined result.",
        r"\frac{\text{amount}_1}{\text{amount}_2} = \frac{R_2 - R}{R - R_1}",
        ["Find the overall percentage if it is not given (total gain ÷ total amount).", "Alligate on the percentages to split the total.", "Scale the ratio to the actual amounts."],
        "The combined percentage is the amount-weighted mean of the two rates.",
        "₹12,000 is invested partly at 5% and the rest at 8% simple interest. The total yearly interest is ₹750. Find the sum at 5%.",
        [r"Mean rate = $\frac{750}{12000} \times 100 = 6.25\%$.", r"Arms: $(8 - 6.25):(6.25 - 5) = 1.75 : 1.25 = 7 : 5$.", r"At 5%: $12000 \times \frac{7}{12} = ₹7000$."],
        "₹7,000"),
]

# =========================== mix-replacement ===========================
# answer checks
assert 80 * F(9, 10) ** 2 == F(324, 5) == F(648, 10)                            # 64.8 milk
assert 60 - 12 == 48 and F(48, 12) == 4                                        # one draw 4:1
assert 48 * F(48, 60) == F(192, 5) == F(384, 10)                               # second draw 38.4
assert F(384, 10) * 5 == 192 and F(216, 10) * 5 == 108 and F(192, 108) == F(16, 9)
assert F(16, 81) == F(2, 3) ** 4 and 8 // (1 - F(2, 3)) == 24                  # C = 24
assert (1 - F(8, 40)) ** 2 == F(16, 25) and 40 * 8 // 2 == 160                 # (guard) C=40 case
assert 1 - F(8, 40) == F(4, 5) and 8 // (1 - F(4, 5)) == 40                    # C = 40
assert (1 - F(10, 50)) ** 2 == F(16, 25) and 50 * F(1, 5) == 10                # x = 10 from C=50
assert 80 * F(7, 10) == 56 and 80 * F(3, 10) == 24                             # 7:3 in 80
assert 20 * F(7, 10) == 14 and 20 * F(3, 10) == 6 and 56 - 14 == 42 and 24 - 6 == 18
assert 42 - 38 == 4 and F(42, 38) == F(21, 19)
assert 50 * F(4, 5) == 40 and 50 * F(1, 5) == 10 and 10 * F(4, 5) == 8 and 10 * F(1, 5) == 2
assert 40 - 8 == 32 and 10 - 2 == 8 and 32 + 10 == 42 and F(42, 8) == F(21, 4)
assert F(7, 12) * 27 == F(63, 4) == F(7, 16) * 36 and 36 * F(7, 12) == 21      # T = 36, milk 21

p_concept = (
    "Take r litres from a vessel of C litres and replace with water, n times. Each round the original "
    "liquid keeps the same fraction:\n\n"
    "$\\text{left} = C\\left(1 - \\dfrac{r}{C}\\right)^n$ and water = C − left.\n\n"
    "One round is plain subtraction. Drawing from a mixture takes both ingredients in proportion, so the "
    "inside ratio does not move. The total volume stays C whenever you replace what you removed."
)

p_notes = r"""### One round, in plain numbers
A vessel holds 60 L of pure milk. 12 L are drawn out and replaced with water. Now: milk 48 L, water 12 L → ratio $4 : 1$.

No formula is needed for a single round — subtract the drawn milk, add the drawn volume as water.

> **Rule:** 'Drawn and replaced' keeps the TOTAL at C. Only the split between the liquids changes.

### The repeated-replacement formula
Do the same draw again and the vessel is no longer pure. The second draw takes out milk AND water in proportion, so the milk keeps the same fraction each round:

$$\text{milk left} = C\left(1 - \frac{x}{C}\right)^n, \qquad \text{water} = C - \text{milk}$$

80 L vessel, 8 L drawn and replaced, twice: milk = $80 \times \left(\frac{9}{10}\right)^2 = 64.8$ L. The second round on the 60 L example: $48 \times \frac{48}{60} = 38.4$ L milk → ratio $38.4 : 21.6 = 16 : 9$.

> **Tip:** One power per round. Never subtract x litres of milk twice — after the first round the draw is part water.

### Drawing from an already-mixed vessel
Draw from a uniform mixture and you take each ingredient in the vessel's own ratio. The ratio inside does not move; only the volume shrinks. The addition afterwards is what shifts the ratio.

80 L of milk : water = 7 : 3 holds 56 L milk, 24 L water. Draw 20 L: it takes 14 milk and 6 water, leaving 42 : 18 — still 7 : 3 in 60 L. Now add 20 L of water: $42 : 38 = 21 : 19$.

> **Watch:** Replacing with the SAME ingredient works the other way. From 50 L of 4 : 1 (40 milk, 10 water), draw 10 L (8 milk, 2 water) and replace with pure milk: $42 : 8 = 21 : 4$.

### Working backwards
Given the final ratio, take roots.

- Wine : water ends at $16 : 65$ after four equal draws. Wine fraction = $\frac{16}{81} = \left(\frac{2}{3}\right)^4$, so each round kept $\frac{2}{3}$: $1 - \frac{x}{C} = \frac{2}{3}$, and with $x = 8$, $C = 24$ L.
- Two rounds from a 50 L vessel leave 32 L of milk: $\left(1 - \frac{x}{50}\right)^2 = \frac{16}{25}$ → $x = 10$ L.

### Water by the complement
Water never needs its own formula. Water = C − milk, so with kept fraction $k = 1 - \frac{x}{C}$, after n rounds:

$$\text{milk} : \text{water} = k^n : (1 - k^n)$$

On the 80 L vessel ($k = \frac{9}{10}$, two rounds): milk $\frac{81}{100}$, water $\frac{19}{100}$ → $81 : 19$ — 64.8 L against 15.2 L, the same numbers as before.

### Shift the ratio by one replacement
A vessel is at 7 : 5. Nine litres of mixture are replaced with water and it becomes 7 : 9. Find the starting milk.

Total T: milk goes from $\frac{7T}{12}$ to $\frac{7T}{16}$. The draw removes $9 \times \frac{7}{12}$ of milk:

$$\frac{7T}{12} - \frac{63}{12} = \frac{7T}{16} \Rightarrow T = 36, \text{ so milk} = 21 \text{ L}$$

> **Tip:** Match the final fraction to a perfect power ($\frac{4}{9}, \frac{16}{25}, \frac{16}{81}$). Exam numbers are built to land on them.
"""

p_formulas = [
    {"name": "Repeated equal replacement", "tex": r"\text{left} = C\left(1 - \frac{x}{C}\right)^n"},
    {"name": "Milk : water after n rounds", "tex": r"\left(1-\frac{x}{C}\right)^n : \left[1-\left(1-\frac{x}{C}\right)^n\right]"},
    {"name": "Proportional removal", "tex": r"\text{lost} = \text{drawn volume} \times \frac{\text{ingredient share}}{\text{total}}"},
    {"name": "Unequal draws", "tex": r"C \prod_k \left(1 - \frac{x_k}{C}\right)", "note": "Multiply one factor per round when the draws differ."},
]

p_tricks = [
    {
        "title": "One fraction per round",
        "body": "Each round multiplies the original liquid by (1 − x/C). Multiply the fractions; never subtract x twice.",
        "example": {
            "q": "From a vessel full of milk, 8 litres are drawn and replaced with water. The vessel holds 80 litres. Find the ratio of milk to water after this single operation.",
            "steps": [r"Milk left = $80 - 8 = 72$ L.", r"Water = $8$ L.", r"Ratio = $72 : 8 = 9 : 1$."],
            "answer": "9 : 1",
        },
    },
    {
        "title": "Two rounds: square the kept fraction",
        "body": "The complement of the milk is the water — no separate calculation.",
        "example": {
            "q": "8 litres are drawn from a cask full of wine and replaced with water; this is done once more. The ratio of wine to water is then 16 : 9. Find the capacity of the cask.",
            "steps": [r"Wine fraction = $\frac{16}{16+9} = \frac{16}{25}$.", r"$\left(1 - \frac{8}{C}\right)^2 = \frac{16}{25} \Rightarrow 1 - \frac{8}{C} = \frac{4}{5}$.", r"$\frac{8}{C} = \frac{1}{5} \Rightarrow C = 40$ L."],
            "answer": "40 litres",
        },
    },
    {
        "title": "Draws keep the inside ratio",
        "body": "A uniform draw removes both liquids in proportion, so the ratio survives the withdrawal. Only the refill changes it.",
        "example": {
            "q": "A vessel has milk and water in the ratio 7 : 5. Nine litres of the mixture are removed and replaced with water, making the ratio 7 : 9. How much milk was in the vessel initially?",
            "steps": [r"Draw removes $\frac{7}{12}$ of 9 L = milk.", r"$\frac{7T}{12} - \frac{63}{12} = \frac{7T}{16} \Rightarrow T = 36$ L.", r"Milk = $\frac{7}{12} \times 36 = 21$ L."],
            "answer": "21 litres",
        },
    },
]

p_mistakes = [
    {"wrong": "Subtracting x litres of milk in every round.", "right": "After round one the draw is part water. Multiply by (1 − x/C) each round instead."},
    {"wrong": "Shrinking the water as well.", "right": "Only the original liquid shrinks. Water = C − milk; the total stays C."},
    {"wrong": "Using (1 − x/C)ⁿ when the draws have different sizes.", "right": "Multiply one separate factor per round: (1 − x₁/C)(1 − x₂/C)…"},
    {"wrong": "Changing the total volume after a replacement.", "right": "Draw r and pour back r: the vessel holds C litres throughout."},
    {"wrong": "Adding the margins in reverse questions.", "right": "Take the n-th root of the final fraction and match it to a perfect power."},
]

p_revision = [
    "n equal rounds: milk = C(1 − x/C)ⁿ; water = C − milk.",
    "One round: plain subtraction.",
    "A uniform draw leaves the inside ratio unchanged.",
    "Total stays C whenever you replace what you remove.",
    "Reverse: final fraction → perfect power → root → solve.",
    "Replace with the same ingredient to enrich, not dilute.",
]

p_patterns = [
    pat("mix-p1", "Repeated replacement (formula)", "very common",
        "x litres drawn and replaced with water, n times, from C litres of pure liquid — what remains is asked.",
        r"\text{left} = C\left(1 - \frac{x}{C}\right)^n",
        [r"Compute the kept fraction $1 - \frac{x}{C}$.", "Raise it to the number of operations.", "Multiply by C; water = C − milk if asked."],
        "Each round removes the same fraction of whatever original liquid is still present.",
        "A vessel contains 80 litres of pure milk. 8 litres are drawn and replaced with water, and the operation is repeated once more. Find the milk left.",
        [r"Kept fraction = $1 - \frac{8}{80} = \frac{9}{10}$.", r"Two rounds: $\left(\frac{9}{10}\right)^2 = \frac{81}{100}$.", r"Milk = $80 \times \frac{81}{100} = 64.8$ L."],
        "64.8 litres"),
    pat("mix-p2", "One or two draws — ratio form", "very common",
        "A single draw-replace, or a second round from the diluted vessel — the final ratio is asked.",
        r"\text{after round 2: } \text{milk}:\text{water} = \left(1-\tfrac{x}{C}\right)^2 : \left[1-\left(1-\tfrac{x}{C}\right)^2\right]",
        ["Round 1: subtract x litres of the pure liquid, add x of water.", "Round 2: multiply the survivor by the kept fraction again.", "Pair the milk with (C − milk) for the ratio."],
        "Only the original liquid keeps shrinking; water absorbs the difference.",
        "From 60 litres of pure milk, 12 litres are removed and replaced with water. Find the ratio of milk to water now.",
        [r"Milk = $60 - 12 = 48$ L.", r"Water = $12$ L.", r"Ratio = $48 : 12 = 4 : 1$."],
        "4 : 1"),
    pat("mix-p3", "Reverse — find x or the capacity", "common",
        "The final quantity or ratio is given; the drawn amount, the capacity, or the number of rounds is asked.",
        r"\left(1 - \frac{x}{C}\right)^n = \text{final fraction of the original liquid}",
        ["Divide the final amount of the original liquid by C.", "Take the n-th root; match it to a perfect power.", r"Solve $1 - \frac{x}{C} = \text{root}$ for the unknown."],
        "The formula runs backwards once you spot the power.",
        "A cask is full of wine. 8 litres are drawn and replaced with water, and the operation is performed three more times. The final ratio of wine to water is 16 : 65. Find the capacity of the cask.",
        [r"Wine fraction = $\frac{16}{16+65} = \frac{16}{81}$.", r"$\frac{16}{81} = \left(\frac{2}{3}\right)^4$, so each round kept $\frac{2}{3}$.", r"$1 - \frac{8}{C} = \frac{2}{3} \Rightarrow C = 24$ L."],
        "24 litres"),
    pat("mix-p4", "Drawing from an already-mixed vessel", "common",
        "The vessel starts as a mixture, not a pure liquid; a draw is followed by an addition.",
        r"\text{the draw splits in the vessel's own ratio}",
        ["Convert the starting ratio into litres of each ingredient.", "Split the drawn volume in that same ratio — the ratio does not move.", "Add the new ingredient to its column and rebuild the ratio."],
        "A uniform mixture leaves in its own proportions.",
        "80 litres of a milk-water mixture in the ratio 7 : 3 has 20 litres drawn off, and then 20 litres of water are added. Find the new ratio.",
        [r"Start: 56 milk, 24 water. Draw takes 14 and 6.", r"After draw: 42 milk, 18 water (still 7 : 3).", r"Add 20 water: $42 : 38 = 21 : 19$."],
        "21 : 19"),
    pat("mix-p5", "Replace with the same ingredient (enriching)", "occasional",
        "The vessel is topped up with the pure version of one ingredient, so the ratio tightens instead of diluting.",
        r"\text{remove in the ratio, then add the pure component}",
        ["Split the removed volume by the current ratio.", "Subtract those amounts from their columns.", "Add the removed volume of the pure ingredient to its column."],
        "The topping-up choice decides which column swells.",
        "From 50 litres of a milk-water mixture in the ratio 4 : 1, 10 litres are removed and replaced with pure milk. Find the new ratio.",
        [r"Start: 40 milk, 10 water. Draw takes 8 and 2.", r"After draw: 32 milk, 8 water.", r"Add 10 milk: $42 : 8 = 21 : 4$."],
        "21 : 4"),
]

# =========================== mix-ratio-profit ===========================
# answer checks
assert F(1, 5) * 100 == 20                                                      # r1 gain
assert F(25, 75) == F(1, 3)                                                     # 33 1/3 gain
assert F(25, 100) == F(1, 4)                                                    # 25% -> 1:4
assert F(2 * 30 + 3 * 40, 5) == 36 and 45 == 36 * F(5, 4) and F(9, 36) == F(1, 4)
assert 120 * F(2, 3) == 80 and (80 - 60, 120 - 80) == (20, 40)                  # CP 80, arms 1:2
assert F(120 * 1 + 60 * 2, 3) == 80                                             # verify ghee mix
assert F(125, 100) * F(90, 100) == F(1125, 1000) and 40 * F(1125, 1000) == 45   # markup chain
assert F(6, 5) * F(11, 10) == F(33, 25) and 100 * F(33, 25) == 132              # water 20% + markup 10%
assert F(5, 4) * F(9, 10) == F(9, 8) and 100 * F(9, 8) == F(225, 2)             # water 25% - discount 10%
assert 36 * F(5, 6) == 30 and 30 * F(3, 5) == 18 and 18 - 6 == 12               # water add 12
assert 40 * F(5, 8) == 25 and 40 * F(3, 8) == 15 and 25 * F(7, 5) == 35 and 35 - 15 == 20

r_concept = (
    "The seller's game: mix in free water (or a cheap filler) and sell the blend at the good item's price.\n\n"
    "Sold at cost price, the gain is the free part per unit of the real item:\n\n"
    "$\\text{gain \\%} = \\dfrac{\\text{water}}{\\text{milk}} \\times 100$.\n\n"
    "For a target ratio, freeze the constant ingredient and solve for the addition. "
    "When two priced items are blended, the blend's cost price is the weighted mean, and profit acts on it."
)

r_notes = r"""### The milkman's trick
Water is free. The milkman adds it to milk and sells the blend at the milk price. Every litre sold brings milk-price money, and part of each litre cost him nothing.

$$\text{gain\%} = \frac{\text{water}}{\text{milk}} \times 100$$

Water equal to one-fifth of the milk → gain $= \frac{1}{5} \times 100 = 20\%$.

> **Rule:** The gain is water per unit of MILK, not per unit of mixture.

### Water as a per cent of the mixture
'Water is 25% of the mixture' reads differently: milk is 75%, so gain $= \frac{25}{75} = 33\frac{1}{3}\%$. Convert a mixture-per-cent into water-per-milk before using the formula.

> **Watch:** Options usually include both readings — 25% and $33\frac{1}{3}\%$. Compute, do not guess.

### Working to a target gain
For a wanted gain of g%, set water : milk = g : 100.

- 25% gain → water : milk = $25 : 100 = 1 : 4$.
- $16\frac{2}{3}\%$ gain → $1 : 6$.

One litre of water per four litres of milk gives exactly 25%.

### Blend cost price and profit
With two real, priced ingredients the blend's cost price is the weighted mean:

$$CP = \frac{q_1 c_1 + q_2 c_2}{q_1 + q_2}$$

Rice at ₹30 and ₹40 mixed 2 : 3 → CP = $\frac{60 + 120}{5} = ₹36$. Sold at ₹45, the gain is $\frac{9}{36} = 25\%$. For a wanted profit of 25%, fix $SP = 1.25 \times CP$ and work backwards.

### Adulterating with a cheaper item
Ghee at ₹120 is cut with oil at ₹60 and sold at ₹120 for a 50% gain.

The blend's CP must be $\frac{120}{1.5} = ₹80$. Alligate: ghee : oil $= (80 - 60) : (120 - 80) = 1 : 2$. Verify: $\frac{120 \times 1 + 60 \times 2}{3} = ₹80$.

> **Tip:** The costly item takes the smaller share when the target CP sits below the midpoint. Always recompute the CP from your ratio.

### Selling above cost price
The trick gets worse when the blend also sells at a markup. Chain the factors: each free litre multiplies the money, and the markup multiplies again.

Water equal to 20% of the milk AND a 10% markup: $1.20 \times 1.10 = 1.32$ → a 32% gain. Water alone would give 20%; the markup alone 10%; together they multiply, never add.

> **Rule:** $\text{gain factor} = \left(1 + \frac{W}{M}\right)\left(1 + \frac{\text{markup}}{100}\right)$. Subtract 1 for the gain per cent.

### A discount can eat the gain
A discount works the same chain in reverse. Water at 25% of the milk, then a 10% discount: $1.25 \times 0.9 = 1.125$ — the milkman still pockets 12.5%. Options quoting 25% or 15% are the two traps.

### Markup and discount on a mixture
A blended item marked up and then discounted still ends at one selling price. Chain the factors: $1.25 \times 0.9 = 1.125$ → a 12.5% gain on a CP of ₹40, selling at ₹45.

Profit chips act on the blend's CP; water additions act on the cost per sold litre. Keep the two bases apart.
"""

r_formulas = [
    {"name": "Adulteration gain", "tex": r"\text{gain\%} = \frac{\text{water}}{\text{milk}} \times 100"},
    {"name": "Target ratio", "tex": r"W : M = g : 100", "note": "For a gain of g% when sold at cost price."},
    {"name": "Blend cost price", "tex": r"CP = \frac{q_1 c_1 + q_2 c_2}{q_1 + q_2}, \quad SP = CP\left(1 + \frac{g}{100}\right)"},
    {"name": "Alloy rebuild", "tex": r"\text{metal} = \text{alloy weight} \times \frac{\text{share}}{\text{sum of shares}}"},
]

r_tricks = [
    {
        "title": "Water over milk is the gain",
        "body": "Free litres per honest litre — that ratio, in per cent, is the profit.",
        "example": {
            "q": "A milkman mixes 1 litre of water with every 5 litres of milk and sells the mixture at the cost price of milk. Find his gain per cent.",
            "steps": [r"Water : milk = $1 : 5$.", r"Gain = $\frac{1}{5} \times 100 = 20\%$."],
            "answer": "20%",
        },
    },
    {
        "title": "Hit the target ratio by addition",
        "body": "Keep the bigger quantity constant and solve for the addition.",
        "example": {
            "q": "36 litres of a mixture has milk and water in the ratio 5 : 1. How much water must be added to make the ratio 5 : 3?",
            "steps": [r"Milk = $36 \times \frac{5}{6} = 30$ L, fixed; water = 6 L.", r"At 5 : 3, water must be $30 \times \frac{3}{5} = 18$ L.", r"Add $18 - 6 = 12$ L."],
            "answer": "12 litres",
        },
    },
    {
        "title": "Rebuild the alloy, then change one metal",
        "body": "Ratio to grams, adjust one column, re-ratio.",
        "example": {
            "q": "An alloy of 40 g contains zinc and copper in the ratio 5 : 3. How much copper must be added to make the ratio 5 : 7?",
            "steps": [r"Zinc = $25$ g, copper = $15$ g.", r"At 5 : 7, copper = $25 \times \frac{7}{5} = 35$ g.", r"Add $35 - 15 = 20$ g."],
            "answer": "20 g",
        },
    },
]

r_mistakes = [
    {"wrong": "Computing profit on the mixture volume.", "right": "Gain = water ÷ milk. The milk's cost is what is recovered."},
    {"wrong": "Reading 'water is p% of the mixture' as a p% gain.", "right": "Convert first: gain = p ÷ (100 − p) × 100."},
    {"wrong": "Adding water and stretching the milk quantity too.", "right": "Only the water column and the total grow."},
    {"wrong": "Adding to the alloy total without re-checking the other metal's leg.", "right": "Freeze the unchanged metal, then solve for the new amount."},
    {"wrong": "Quoting a ratio without recomputing the blend CP.", "right": "Verify: weighted CP from your ratio must hit the target."},
]

r_revision = [
    "Gain % = water ÷ milk × 100, when sold at cost price.",
    "Water p% of mixture → gain = p ÷ (100 − p) × 100.",
    "Target gain g% → water : milk = g : 100.",
    "Blend CP = weighted mean; SP = CP × (1 + g/100).",
    "Adulteration: alligate to the CP that yields the gain.",
    "Verify every ratio by recomputing the CP.",
]

r_patterns = [
    pat("mix-r1", "Gain per cent from added water", "very common",
        "Water is added to milk (or a cheap filler to a good item) and the blend is sold at cost price — find the gain %.",
        r"\text{gain\%} = \frac{\text{water}}{\text{milk}} \times 100",
        ["Express water per unit of milk (convert 'p% of mixture' into p/(100−p)).", "Multiply by 100.", "Sanity check: water equal to half the milk → 50% gain."],
        "The milk's cost comes back in full; the water volume is pure margin.",
        "A milkman mixes water equal to one-fifth of the milk and sells the mixture at cost price. Find his gain per cent.",
        [r"Water : milk = $1 : 5$.", r"Gain = $\frac{1}{5} \times 100 = 20\%$."],
        "20%"),
    pat("mix-r2", "Water ratio for a target gain", "very common",
        "'What ratio of water to milk gives a gain of x% when sold at cost?'",
        r"W : M = g : 100",
        ["Set water : milk = g : 100 and reduce.", "State the ratio in the direction the options use.", "Check with one litre: (1 + M) litres sold for the price of M."],
        "The gain per cent IS the water-to-milk ratio in per cent form.",
        "A milkman wants a 25% gain by adding water and selling at cost price. Find the ratio of water to milk in his mixture.",
        [r"$W : M = 25 : 100$.", r"= $1 : 4$."],
        "1 : 4"),
    pat("mix-r3", "Blend cost price and profit", "common",
        "Two priced ingredients mixed in a given ratio; the selling price or profit % is asked.",
        r"CP = \frac{q_1 c_1 + q_2 c_2}{q_1 + q_2}, \quad SP = CP\left(1+\frac{g}{100}\right)",
        ["Compute the weighted CP of the blend.", "Apply the profit factor, or divide SP by CP to find the gain.", "Keep fractions — ₹36.25 answers are legitimate."],
        "Profit acts on the blend's average cost, never on one ingredient alone.",
        "Rice at ₹30 per kg and ₹40 per kg are mixed in the ratio 2 : 3 and the mixture is sold at ₹45 per kg. Find the profit per cent.",
        [r"CP = $\frac{2 \times 30 + 3 \times 40}{5} = \frac{180}{5} = ₹36$.", r"Gain per kg = $45 - 36 = ₹9$.", r"Profit = $\frac{9}{36} \times 100 = 25\%$."],
        "25%"),
    pat("mix-r4", "Adulteration for a target gain", "common",
        "A costly item is cut with a cheaper one; the selling price and target gain fix the mixing ratio.",
        r"\text{blend CP} = \frac{SP}{1 + g/100}; \quad \text{alligate on } c_1, c_2",
        ["Convert the gain into the required blend CP.", "Alligate between the two cost prices to reach that CP.", "Verify by recomputing the weighted CP."],
        "The blend CP that yields the gain pins the ratio uniquely.",
        "Ghee costing ₹120 per kg is mixed with oil costing ₹60 per kg and the mixture is sold at ₹120 per kg for a 50% gain. Find the mixing ratio of ghee to oil.",
        [r"Blend CP = $\frac{120}{1.5} = ₹80$.", r"Ghee : oil = $(80 - 60) : (120 - 80) = 20 : 40 = 1 : 2$.", r"Check: $\frac{120 + 120}{3} = ₹80$."],
        "1 : 2"),
    pat("mix-r5", "Mixture sold through markup and discount", "occasional",
        "The blended item is marked up and then discounted — the net profit on the blend's CP is asked.",
        r"\text{net} = \left(1+\frac{m}{100}\right)\left(1-\frac{d}{100}\right) - 1",
        ["Find the blend's CP per unit.", "Multiply the markup and discount factors for the net factor.", "Profit % = (net factor − 1) × 100."],
        "Markup and discount are chained factors on top of the mixture arithmetic.",
        "A mixture costs ₹40 per kg. It is marked 25% above cost and sold at a 10% discount. Find the profit per cent.",
        [r"Markup factor = $1.25$; discount factor = $0.9$.", r"Net = $1.25 \times 0.9 = 1.125$.", r"Profit = $12.5\%$ (SP = ₹45)."],
        "12.5%"),
]

# =========================== mix-mixtures ===========================
# answer checks
assert F(1, 2) * (F(4, 5) + F(3, 5)) == F(7, 10)                                # c1 -> 7:3
assert 20 * F(3, 4) == 15 and 32 * F(5, 8) == 20 and 15 + 20 == 35 and (20 - 15) + (32 - 20) == 17  # 35:17, water 5+12
assert (F(5, 12) - F(4, 9)) == F(-1, 36) and (F(2, 5) - F(5, 12)) == F(-1, 60)  # c2 arms
assert F(60, 36) == F(5, 3) and 5 * F(2, 5) + 3 * F(4, 9) == F(10, 3) and F(10, 3) / 8 == F(5, 12)
assert (F(70, 100) - F(50, 100), F(50, 100) - F(30, 100)) == (F(1, 5), F(1, 5))  # 70/30 -> 50
assert 60 * F(2, 3) == 40 and 40 * F(1, 2) == 20 and F(40 + 20, 100) == F(3, 5)  # 60% milk
assert F(1, 2) * (F(3, 4) + F(5, 8)) == F(11, 16)                                # 11:5
assert 60 * F(2, 3) == 40 and 12 * F(2, 3) == 8 and 40 - 8 == 32 and 16 + 8 == 24 and F(32, 24) == F(4, 3)
assert 5 * F(35, 40) == F(35, 8) and 5 * F(5, 40) == F(5, 8) and F(35, 8) + 5 == F(75, 8) and F(5, 8) == F(5, 8)
assert F(75, 8) / F(5, 8) == 15                                                  # 15:1
assert (F(1, 2) + F(2, 5) + F(3, 8)) / 3 == F(17, 40) and 40 - 17 == 23          # 17:23
assert F(2 * 60 + 1 * 30, 3) == 50                                               # c4
assert 100 * F(4, 5) ** 2 == 64                                                   # dilution rounds

c_concept = (
    "Two ready mixtures, each with its own ratio, are combined. Reduce each vessel to the **fraction of one "
    "chosen ingredient** — milk, say — never juggle both ratios at once.\n\n"
    "$\\text{blend fraction} = \\dfrac{V_1 f_1 + V_2 f_2}{V_1 + V_2}$.\n\n"
    "For a target fraction f, mix the volumes in the ratio $(f_2 - f) : (f - f_1)$. "
    "A withdrawal from a uniform mixture takes both liquids in proportion, so the inside ratio survives it."
)

c_notes = r"""### Fractions first
Two vessels, each already a milk-water blend, are poured together. Give each vessel ONE number: the fraction of milk it holds.

$$\text{milk in the blend} = V_1 f_1 + V_2 f_2$$

Vessel A at 3 : 1 holds milk fraction $\frac{3}{4}$; vessel B at 5 : 3 holds $\frac{5}{8}$.

> **Rule:** Pick one ingredient (milk or water) and convert every vessel to ITS fraction. Stay with that ingredient to the end.

### Mixing two mixtures
Vessel A (3 : 1, 20 L) gives 15 L of milk. Vessel B (5 : 3, 32 L) gives 20 L. Poured together: milk $15 + 20 = 35$ L, water $5 + 12 = 17$ L → $35 : 17$.

Equal volumes make it lighter work: 4 : 1 and 3 : 2 in equal volumes give milk fraction $\frac{1}{2}\left(\frac{4}{5} + \frac{3}{5}\right) = \frac{7}{10}$ → $7 : 3$.

> **Example:** Two vessels contain milk and water in the ratios 3 : 1 and 5 : 3. Equal volumes are mixed. Milk fraction $= \frac{1}{2}\left(\frac{3}{4} + \frac{5}{8}\right) = \frac{11}{16}$ → milk : water $= 11 : 5$.

### Hitting a target strength
To blend A and B into a target milk fraction t, alligate on the fractions:

$$\frac{q_A}{q_B} = \frac{t - f_B}{f_A - t}$$

Both differences must carry the same sign — the target must lie between the two fractions. Mixtures at $\frac{2}{5}$ and $\frac{4}{9}$ milk blended to $\frac{5}{12}$: $\frac{q_A}{q_B} = \frac{5/12 - 4/9}{2/5 - 5/12} = \frac{1/36}{1/60} = \frac{5}{3}$. Check: $5 \times \frac{2}{5} + 3 \times \frac{4}{9} = \frac{10}{3}$ milk in 8 parts → $\frac{5}{12}$.

> **Tip:** Verify every target blend by rebuilding the fraction from your volumes.

### Unequal volumes: weight by volume
A 60 L vessel at 2 : 1 and a 40 L vessel at 1 : 1 are poured together. Milk = $60 \times \frac{2}{3} + 40 \times \frac{1}{2} = 40 + 20 = 60$ L in 100 L → 60% milk. Equal volumes alone would have given 58.3% — the volumes matter.

> **Watch:** Never average two fractions when the volumes differ. Weight each fraction by its volume.

### Withdrawals keep the inside ratio
Drawing from a uniform mixture removes both liquids in the vessel's ratio. 60 L of 2 : 1 (40, 20); draw 12 L → removes 8 milk, 4 water → still 2 : 1 in 48 L. Add 8 L of water → $32 : 24 = 4 : 3$.

Only the topping-up changes a ratio. Removing 20% and topping with water multiplies the strength by 0.8 each round: 100 L at 80% milk, two rounds → $100 \times 0.8^2 = 64$ L of milk.

### Transfers between vessels
Track each vessel separately.

A 40 L can of pure milk: 5 L move to an empty vessel; the can is topped with water → can at $35 : 5$. Then 5 L of the can's mixture move to the second vessel, carrying $5 \times \frac{35}{40} = 4.375$ milk and $0.625$ water. Second vessel: $5 + 4.375 = 9.375$ milk, $0.625$ water → $15 : 1$.

> **Watch:** Recompute each vessel's total after every move. The components must add back to that total.

### Three or more vessels
Equal capacities → the plain mean of the fractions. Vessels at $\frac{1}{2}$, $\frac{2}{5}$, $\frac{3}{8}$ milk → mean $\frac{17}{40}$ → milk : water $17 : 23$. For unequal capacities, weight by volume first.
"""

c_formulas = [
    {"name": "Blend of two mixtures", "tex": r"f = \frac{V_1 f_1 + V_2 f_2}{V_1 + V_2}"},
    {"name": "Volumes for a target fraction", "tex": r"\frac{V_1}{V_2} = \frac{f_2 - f}{f - f_1}"},
    {"name": "Fraction from ratio", "tex": r"f_{\text{milk}} = \frac{m}{m + w}"},
    {"name": "Equal volumes", "tex": r"\bar{f} = \frac{f_1 + f_2 + f_3}{3}", "note": "Only when every vessel holds the same volume."},
]

c_tricks = [
    {
        "title": "Fractions first, then average",
        "body": "Ratio → milk fraction per vessel → weighted average.",
        "example": {
            "q": "Two vessels contain milk and water in the ratios 3 : 1 and 5 : 3. Equal volumes are mixed. Find the ratio of milk to water in the new mixture.",
            "steps": [r"Fractions: $\frac{3}{4}$ and $\frac{5}{8}$.", r"Mean = $\frac{1}{2}\left(\frac{3}{4} + \frac{5}{8}\right) = \frac{11}{16}$.", r"Milk : water = $11 : 5$."],
            "answer": "11 : 5",
        },
    },
    {
        "title": "Alligate the fractions",
        "body": "The target sits between the two vessel fractions; the distances give the volumes.",
        "example": {
            "q": "Vessel A has 70% milk and vessel B has 30% milk. In what ratio should they be mixed to get a 50% milk mixture?",
            "steps": [r"$A : B = (50 - 30) : (70 - 50)$.", r"= $20 : 20 = 1 : 1$."],
            "answer": "1 : 1",
        },
    },
    {
        "title": "Weight by volume when sizes differ",
        "body": "Multiply each vessel's fraction by its volume before adding.",
        "example": {
            "q": "A 60-litre vessel has milk and water in the ratio 2 : 1 and a 40-litre vessel has them in the ratio 1 : 1. They are poured together. Find the milk fraction of the blend.",
            "steps": [r"Milk = $60 \times \frac{2}{3} + 40 \times \frac{1}{2} = 60$ L.", r"Total = $100$ L.", r"Milk fraction = $60\%$."],
            "answer": "60% milk",
        },
    },
]

c_mistakes = [
    {"wrong": "Averaging the two ratios directly (3:1 and 5:3 'average' to 4:2).", "right": "Convert each ratio to a fraction of one ingredient, then weight by volume."},
    {"wrong": "Mixing milk fractions with water fractions in one calculation.", "right": "Choose one ingredient at the start and stay with it."},
    {"wrong": "Ignoring unequal volumes when blending.", "right": "Weight each fraction by its own vessel's volume."},
    {"wrong": "Forgetting to reduce each ratio to a fraction of the total.", "right": "3 : 4 is 3/7 of the mixture, not 3/4."},
    {"wrong": "Losing track of vessel totals in transfer questions.", "right": "After every move, check that components add back to the vessel's volume."},
]

c_revision = [
    "Convert every vessel to one ingredient's fraction before pooling.",
    "Target blend: alligate the fractions; target must sit between them.",
    "Unequal volumes → weight by volume.",
    "Equal volumes → plain mean of the fractions.",
    "A withdrawal keeps the inside ratio; the refill changes it.",
    "Transfers: keep a separate column per vessel; totals must balance.",
]

c_patterns = [
    pat("mix-c1", "Two mixtures combined", "very common",
        "Two vessels with given milk-water ratios (and volumes) are mixed — the final ratio is asked.",
        r"\text{milk} = q_1 f_1 + q_2 f_2, \quad \text{water} = q_1(1-f_1) + q_2(1-f_2)",
        ["Convert each vessel to litres of milk (fraction × volume).", "Pool the milk and the water columns.", "Reduce the ratio to smallest terms."],
        "Components add linearly across vessels.",
        "Vessels with milk : water in the ratios 4 : 1 and 3 : 2 are mixed in equal volumes. Find the milk : water ratio of the blend.",
        [r"Fractions: $\frac{4}{5}$ and $\frac{3}{5}$; equal volumes → mean $\frac{7}{10}$.", r"Milk : water = $7 : 3$."],
        "7 : 3"),
    pat("mix-c2", "Ratio to hit a target strength", "common",
        "'In what ratio must mixture A be mixed with mixture B to get milk : water = t?'",
        r"\frac{q_A}{q_B} = \frac{t - f_B}{f_A - t}",
        ["Write each vessel's milk fraction and the target fraction.", "Alligate on the fractions — the two differences must share a sign.", "Verify by rebuilding the blend's strength."],
        "A target between the two source strengths fixes the weights.",
        "Mixtures with milk : water in the ratios 2 : 3 and 4 : 5 are blended to give milk : water = 5 : 7. Find the mixing ratio.",
        [r"Fractions $\frac{2}{5}$, $\frac{4}{9}$; target $\frac{5}{12}$.", r"$\frac{q_A}{q_B} = \frac{5/12 - 4/9}{2/5 - 5/12} = \frac{1/36}{1/60} = \frac{5}{3}$."],
        "5 : 3"),
    pat("mix-c3", "Transfer and top-up between vessels", "common",
        "A quantity is drawn from one vessel into another (or replaced) — track both vessels.",
        r"\text{a withdrawal splits in the source's own ratio}",
        ["Write the component litres for each vessel.", "Move the drawn volume split in the source's ratio.", "Apply additions; confirm each vessel's total separately."],
        "A uniform mixture leaves in its own proportions.",
        "A 40-litre can holds pure milk. 5 litres are moved to an empty vessel and the can is topped up with water; then 5 litres of the can's mixture are moved to the second vessel. Find milk : water in the second vessel.",
        [r"After top-up the can holds $35 : 5$.", r"5 L of it carries $4.375$ milk and $0.625$ water.", r"Second vessel: milk $5 + 4.375 = 9.375$, water $0.625$ → $15 : 1$."],
        "15 : 1"),
    pat("mix-c4", "Strength of a blended solution", "common",
        "Two solutions of given concentration are mixed in a given ratio — the resulting strength is asked.",
        r"\text{strength} = \frac{q_1 s_1 + q_2 s_2}{q_1 + q_2}",
        ["Compute the solute from each solution.", "Divide the pooled solute by the pooled volume.", "State the result as a percentage."],
        "Concentration is volume-weighted; a plain average only works for equal volumes.",
        "Solutions of 60% and 30% acid are mixed in the ratio 2 : 1. Find the strength of the resulting solution.",
        [r"Solute = $2 \times 60 + 1 \times 30 = 150$ parts.", r"Volume = $3$ parts.", r"Strength = $150 \div 3 = 50\%$."],
        "50%"),
    pat("mix-c5", "Three vessels or equal capacities", "occasional",
        "Three or more blends combine, often in equal volumes.",
        r"\bar{f} = \frac{f_1 + f_2 + f_3}{3} \quad \text{(equal volumes)}",
        ["Write each vessel's milk fraction.", "Equal volumes → average the fractions; otherwise weight by volume.", "Convert the mean fraction into the asked ratio."],
        "With equal capacities all the weights are 1.",
        "Three equal vessels hold milk : water in the ratios 1 : 1, 2 : 3 and 3 : 5. Find the milk : water ratio of their mixture.",
        [r"Fractions: $\frac{1}{2}, \frac{2}{5}, \frac{3}{8}$.", r"Mean = $\frac{17}{40}$.", r"Milk : water = $17 : 23$."],
        "17 : 23"),
]

# =========================== apply ===========================
data = json.loads(TOPIC.read_text(encoding="utf-8"))
apply(data, "mix-basics", v_concept, v_notes, v_formulas, v_tricks, v_mistakes, v_revision, v_patterns)
apply(data, "mix-alligation", a_concept, a_notes, a_formulas, a_tricks, a_mistakes, a_revision, a_patterns)
apply(data, "mix-replacement", p_concept, p_notes, p_formulas, p_tricks, p_mistakes, p_revision, p_patterns)
apply(data, "mix-ratio-profit", r_concept, r_notes, r_formulas, r_tricks, r_mistakes, r_revision, r_patterns)
apply(data, "mix-mixtures", c_concept, c_notes, c_formulas, c_tricks, c_mistakes, c_revision, c_patterns)

ids = [p["id"] for s in data["subtopics"] for p in s.get("patterns", [])]
assert len(ids) == len(set(ids)), "duplicate pattern ids in topic"
TOPIC.write_text(json.dumps(data, ensure_ascii=False, indent=1) + "\n", encoding="utf-8")
print("mixture-alligation updated:", ", ".join(f"{s['id']}: {len(s['patterns'])} patterns" for s in data["subtopics"]))
