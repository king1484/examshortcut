"""Phase-2 deep content for quant/ratio-proportion. Run: py -3 ratio-proportion.py"""
import os
import sys

sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
from _lib import apply_topic
from rp_basics import build_basics
from rp_proportion import build_proportion
from rp_partnership import build_partnership
from rp_ages import build_ages
from rp_money import build_money


def P(pattern, frequency, howToSpot, approach, subtopic, q, sol):
    return {"pattern": pattern, "frequency": frequency, "howToSpot": howToSpot, "approach": approach,
            "subtopic": subtopic, "example": {"q": q, "solution": sol}}


PYQ = [
    P("Divide an amount in a given ratio", "very common",
      "A sum (inheritance, bonus, scholarship) split among 2-3 people in ratio m : n : p; find a share, or a share given the total/difference.",
      "One part = total ÷ sum of terms; multiply by the asked term. If one share or the difference is given, recover the multiplier x first.",
      "rp-basics",
      "A sum of ₹2,500 is divided among A, B and C in the ratio 2 : 3 : 5. What is the largest share?",
      "Total parts = 10 → 1 part = 250 → largest (C) = 5 × 250 = ₹1,250."),
    P("Combine two ratios into A : B : C", "very common",
      "'A : B = …, B : C = …, find A : B : C' or a quantity-based version ('twice of A = thrice of B').",
      "LCM bridge: scale both ratios so the shared term is equal. 'kA = lB = mC' → A : B : C = (LCM/k) : (LCM/l) : (LCM/m).",
      "rp-basics",
      "If A : B = 2 : 5 and B : C = 6 : 7, find A : B : C.",
      "Bridge B to 30: A : B = 12 : 30, B : C = 30 : 35 → A : B : C = 12 : 30 : 35."),
    P("Mean / third / fourth proportional", "common",
      "Direct definition question: 'mean proportional between a and b', 'third proportional to a and b', 'fourth proportional to a, b, c'.",
      "√(ab), b²/a, bc/a respectively — write the proportion first (a : b :: b : ? repeats the middle; a : b :: c : ? does not). Pure formula recall.",
      "rp-proportion",
      "Find the third proportional to 12 and 18.",
      "12 : 18 :: 18 : x → x = 18²/12 = 27."),
    P("Partnership profit division", "very common",
      "2-3 partners, capitals (sometimes changed mid-year or joined late), profit at year end; find a share or the total.",
      "Ratio of capital × months (sum capital × months per stretch for mid-year changes), then fraction × profit. Working partner: their cut comes off the profit first.",
      "rp-partnership",
      "A invests ₹30,000 for 12 months and B invests ₹40,000 for 6 months. Out of a profit of ₹28,800, find A's share.",
      "Capital-months 360000 : 240000 = 3 : 2 → A = 3/5 × 28800 = ₹17,280."),
    P("Ages: present and shifted ratios", "very common",
      "'Ratio of present ages is a : b; after/before n years it is p : q' or 'father is k times the son'.",
      "Write ages ax, bx; shift both by n (add for hence, subtract for ago); equate to p : q; cross-multiply once. The constant age-difference is a free checker.",
      "rp-ages",
      "The present ages of two persons are in the ratio 4 : 5. After 16 years the ratio will be 6 : 7. Find the sum of their present ages.",
      "7(4x + 16) = 6(5x + 16) → x = 8 → ages 32 and 40 → sum 72 years."),
    P("Income–expenditure–savings ratios", "common",
      "Two ratios (income, expenditure) plus equal or unequal savings; find an income or an expenditure.",
      "Incomes ax, bx and expenditures py, qy (different multipliers); two savings equations; subtract or eliminate y.",
      "rp-money-applications",
      "Incomes of A and B are in ratio 8 : 5 and expenditures in 5 : 3. If each saves ₹1,200, find A's income.",
      "8x − 5y = 1200, 5x − 3y = 1200 → y = 1.5x → 0.5x = 1200 → A = 8x = ₹19,200."),
    P("Coin denomination ratios", "occasional",
      "50p/25p/10p (or ₹1/50p) coins in a ratio with total value; find a coin count or the total number of coins.",
      "Price one full set (Σ count × value, one unit only), divide the total value by the set value to get sets, multiply back for counts.",
      "rp-money-applications",
      "A bag has 50-paise, 25-paise and 10-paise coins in the ratio 7 : 6 : 5 amounting to ₹550. Find the number of 25-paise coins.",
      "Set value = 550 paise = ₹5.50 → 100 sets → 25p coins = 6 × 100 = 600."),
    P("Componendo–dividendo", "occasional",
      "(x + y)/(x − y) given as a ratio; find x : y or x : (x + y), sometimes with coefficients on x and y.",
      "Jump formula: x/y = (p + q)/(p − q). With coefficients, C&D first gives mx : ny, then divide off the coefficients. Check the direction (sum over difference).",
      "rp-proportion",
      "If (x + y)/(x − y) = 5/3, find x : y.",
      "x : y = (5 + 3) : (5 − 3) = 8 : 2 = 4 : 1."),
]

if __name__ == "__main__":
    subs = [build_basics(), build_proportion(), build_partnership(), build_ages(), build_money()]
    apply_topic("ratio-proportion", subs, PYQ)
