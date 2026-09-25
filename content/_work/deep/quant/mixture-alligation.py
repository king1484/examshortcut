"""Phase-2 deep content for quant/mixture-alligation. Run: py -3 mixture-alligation.py"""
import os
import sys
from fractions import Fraction

sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
from _lib import apply_topic
from mix_basics_alligation import build_basics, build_alligation
from mix_rep_profit_mix import build_replacement, build_ratioprofit
from mix_mixtures_final import build_mixtures


def P(pattern, frequency, howToSpot, approach, subtopic, q, sol):
    return {"pattern": pattern, "frequency": frequency, "howToSpot": howToSpot, "approach": approach,
            "subtopic": subtopic, "example": {"q": q, "solution": sol}}


PYQ = [
    P("Two-ingredient mixing (alligation)", "very common",
      "Two unit prices with a target mean price — the mixing ratio is asked.",
      "Alligate: dearer : cheaper = (M − C) : (D − M); the mean must sit between the prices. Scale the arms by any known quantity.",
      "mix-alligation",
      "In what ratio must tea at ₹320 per kg be mixed with tea at ₹250 per kg so that the mixture costs ₹300 per kg?",
      "Dearer : cheaper = (300 − 250) : (320 − 300) = 50 : 20 = 5 : 2."),
    P("Repeated replacement", "very common",
      "x litres drawn from C litres and replaced with water, n times — find what remains or the final ratio.",
      "Milk left = C(1 − x/C)^n; water = C − milk. Reverse problems take the n-th root of the final fraction.",
      "mix-replacement",
      "A vessel contains 80 litres of pure milk. 8 litres are drawn and replaced with water; the operation is repeated once more. Find the milk left.",
      "80 × (9/10)² = 64.8 litres."),
    P("Add water / add ingredient", "very common",
      "'How much water (or milk) must be added to reach a given strength or ratio?'",
      "Freeze the unchanged component, grow the total, set one linear equation. Water's 'price' is 0, so alligation also works.",
      "mix-basics",
      "How much water must be added to 60 litres of milk so that milk forms 75% of the new mixture?",
      "Milk stays 60 L and must be 75% → total 80 L → add 20 L."),
    P("Milk-water ratio bookkeeping", "common",
      "A ratio plus a total (or an operation) is given — extract component amounts or the new ratio.",
      "Parts × total/parts-sum = litres per component. Adding one ingredient leaves the other column untouched; a draw preserves the internal ratio.",
      "mix-basics",
      "A 40-litre mixture has milk and water in the ratio 3:1. How much milk must be added to make the ratio 4:1?",
      "Water 10 L fixed → milk must reach 40 L → add 10 L."),
    P("Adulteration profit", "common",
      "A costly item is cut with a cheap (or free) one and sold at cost or marked price — find gain % or the ratio.",
      "Water sold at milk's price gains water/milk × 100; 'p% of the mixture' is p/(100−p) per unit milk. For a target gain, alligate to the blend CP = SP ÷ (1 + g/100).",
      "mix-ratio-profit",
      "A milkman adds water equal to one-fifth of the milk and sells the mixture at cost price. His gain per cent is:",
      "(1/5) × 100 = 20%."),
    P("Mixing two mixtures", "common",
      "Two ready mixtures (given ratios or strengths) are combined — final ratio or strength is asked.",
      "Reduce each to the key-component fraction, pool the columns. For a target strength, alligate the fractions; the target must lie between them.",
      "mix-mixtures",
      "Vessels of milk:water 4:1 and 3:2 are mixed in equal volumes. Find the milk : water ratio of the blend.",
      "Milk fraction = (4/5 + 3/5)/2 = 7/10 → 7 : 3."),
    P("Alligation on averages", "common",
      "Two group averages with a known overall — class marks, speeds over equal distances, wages.",
      "Alligate on the averaged quantity: sizes' ratio = (A₂ − A) : (A − A₁). Equal distances alligate the times, not the speeds.",
      "mix-alligation",
      "The average marks of boys is 70 and of girls is 75. If the class average is 72, the ratio of boys to girls is:",
      "(75 − 72) : (72 − 70) = 3 : 2."),
    P("Dishonest stock replacement / watered stock", "common",
      "A trader replaces sold goods with inferior stock, or sells watered milk — quantitative gain is asked.",
      "Run the replacement multiplier C(1 − x/C)^n for stock; for watered milk sold at cost, the gain is the water : milk ratio in per cent.",
      "mix-replacement",
      "A milkman mixes water equal to 25% of the milk in his can and sells the mixture at the cost price of milk. His gain per cent is:",
      "Water : milk = 1 : 4 → gain 25%."),
]

# arithmetic behind the pyq examples
assert Fraction(300 - 250, 320 - 300) == Fraction(5, 2)
assert 80 * Fraction(9, 10) ** 2 == Fraction(324, 5)
assert Fraction(60 * 4, 3) - 60 == 20
assert 40 - 30 == 10 and 30 * 4 == 10 * 4 + 80
assert Fraction(1, 5) * 100 == 20 and Fraction(25, 100 - 25) * 100 == Fraction(100, 3)
assert Fraction(1, 2) * (Fraction(4, 5) + Fraction(3, 5)) == Fraction(7, 10)
assert Fraction(75 - 72, 72 - 70) == Fraction(3, 2)
assert Fraction(1, 4) * 100 == 25

if __name__ == "__main__":
    subs = [build_basics(), build_alligation(), build_replacement(), build_ratioprofit(), build_mixtures()]
    apply_topic("mixture-alligation", subs, PYQ)
