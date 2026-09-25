"""Phase-2 deep content for quant/profit-loss-discount. Run: py -3 profit-loss-discount.py"""
import os
import sys
from fractions import Fraction

sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
from _lib import apply_topic
from pl_basics_successive import build_basics, build_successive
from pl_marked_dishonest_same import build_marked, build_dishonest, build_same


def P(pattern, frequency, howToSpot, approach, subtopic, q, sol):
    return {"pattern": pattern, "frequency": frequency, "howToSpot": howToSpot, "approach": approach,
            "subtopic": subtopic, "example": {"q": q, "solution": sol}}


PYQ = [
    P("Direct profit/loss per cent", "very common",
      "CP and SP are given (or the CP follows in one step, e.g. with a repair cost) and the profit or loss per cent is asked.",
      "Profit or loss = SP − CP; divide by CP (never by SP) and multiply by 100. Overheads join the CP first. Fraction chips (12.5% = 1/8) skip the arithmetic.",
      "pl-basics",
      "A cycle bought for ₹850 is sold for ₹1,020. Find the profit per cent.",
      "Profit = 170 → 170/850 × 100 = 20%."),
    P("CP or SP reconstruction", "very common",
      "One of CP/SP is given with the profit or loss per cent — find the other price.",
      "Multiply or divide by the chip (100 ± x)/100. 'Had it been sold for ₹k more, gain b% instead of loss a%' ⇒ k = (a + b)% of CP.",
      "pl-basics",
      "A trader sells a scooter at a loss of 5%. Had he sold it for ₹960 more, he would have gained 15%. Find the CP.",
      "20% of CP = 960 → CP = ₹4,800."),
    P("Successive discounts / price changes", "very common",
      "'Two successive discounts of 20% and 10%', or a price that rises and then falls by given per cents.",
      "Chips multiply; equivalent single discount = d1 + d2 − d1d2/100. Same % up and down ends at −x²/100%. Never add discounts.",
      "pl-successive",
      "The marked price of a sofa is ₹1,600. It is sold after two successive discounts of 20% and 12.5%. Find the selling price.",
      "1600 × 4/5 × 7/8 = ₹1,120."),
    P("MP–discount–profit chain", "very common",
      "Marked x% above cost, a discount of y% allowed — find the gain per cent, or work back to the MP for a target gain.",
      "MP/CP = (100 + g)/(100 − d) fixes any one of markup, discount, gain from the other two. Trace CP = 100 through the chain to check.",
      "pl-marked-discount",
      "A trader allows a discount of 25% on the marked price and still gains 20%. The marked price is what per cent above the cost price?",
      "(120/75 − 1) × 100 = 60%."),
    P("Dishonest dealer / false weight", "common",
      "False weights, short measures, or a claimed loss with cheating on the quantity.",
      "gain% = (W − w)/w × 100 for short weight at CP; for claims compare money per true unit: (100 − L)/(100 − c). Cheating at both ends multiplies chips (100 + b)/(100 − s).",
      "pl-dishonest",
      "A milkman sells at the cost price but gives only 800 mL per litre. Find his gain per cent.",
      "200/800 × 100 = 25%."),
    P("Same SP, one profit one loss", "common",
      "Two items sold at the same price with equal ±x% — the net result in per cent or rupees.",
      "Net loss% = x²/100 of the total CP. For rupees, reconstruct both CPs by dividing the common SP by the chips.",
      "pl-same-price-cases",
      "Two articles are sold at ₹1,200 each, one at 25% profit and the other at 25% loss. Find the overall loss per cent.",
      "(6.25%). CPs 960 and 1600, total 2560; loss ₹160 = 6.25% of CP."),
    P("Multi-level markup (trade chain)", "occasional",
      "Manufacturer → wholesaler → retailer → customer, each adding a profit per cent.",
      "Multiply the markup chips end to end; divide to walk backwards to the base cost. Each trader's profit acts on his own purchase price.",
      "pl-marked-discount",
      "A manufacturer sells at 20% profit to a wholesaler, who sells at 25% profit to a retailer, who sells at 10% profit to a customer. Overall rise over the manufacturing cost?",
      "1.2 × 1.25 × 1.1 = 1.65 → 65%."),
    P("Cost of goods sold / goods-based cases", "occasional",
      "'The CP of 15 articles equals the SP of 12', 'buys 4 for ₹15, sells 5 for ₹24', free-item offers.",
      "Fix a common count of articles (LCM of the counts) and compare CP and SP; for counts, profit% = extra ÷ articles given × 100. Free-item offers: discount = free ÷ received.",
      "pl-basics",
      "If the cost price of 15 articles is equal to the selling price of 12 articles, find the profit per cent.",
      "(15 − 12)/12 × 100 = 25%."),
]

# arithmetic behind the pyq examples
assert (1020 - 850) / 850 * 100 == 20
assert 960 * 100 / 20 == 4800
assert 1600 * Fraction(4, 5) * Fraction(7, 8) == 1120
assert 160 * Fraction(3, 4) == 100 * Fraction(6, 5)
assert 200 / 800 * 100 == 25
assert 1200 / Fraction(5, 4) + 1200 / Fraction(3, 4) == 2560 and 160 / 2560 * 100 == 6.25
assert abs(1.2 * 1.25 * 1.1 - 1.65) < 1e-12
assert (15 - 12) / 12 * 100 == 25

if __name__ == "__main__":
    subs = [build_basics(), build_successive(), build_marked(), build_dishonest(), build_same()]
    apply_topic("profit-loss-discount", subs, PYQ)
