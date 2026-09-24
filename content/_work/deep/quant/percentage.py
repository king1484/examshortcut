"""Phase-2 deep content for quant/percentage. Run: py -3 percentage.py"""
import os
import sys

sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
from _lib import apply_topic
from pct_basics_change import build_basics, build_change
from pct_more_less import build_moreless
from pct_population import build_population
from pct_income import build_income


def P(pattern, frequency, howToSpot, approach, subtopic, q, sol):
    return {"pattern": pattern, "frequency": frequency, "howToSpot": howToSpot, "approach": approach,
            "subtopic": subtopic, "example": {"q": q, "solution": sol}}


PYQ = [
    P("x% of a number / fraction conversion", "very common",
      "'What is 35% of 480', '1/8 as a percentage', 'if p% of N is k find N'.",
      "Fraction table + one multiplication or division; recover the whole with N = 100k/p. Under 30 seconds — never long-multiply.",
      "pct-basics",
      "What is 35% of 480?",
      "Table route: 35% = 7/20 → 480 × 7/20 = 168. Or 10% is 48, so 35% = 3.5 × 48 = 168."),
    P("Successive percentage change", "very common",
      "Two or three changes applied one after another (price/population/marks), asking net change or final value.",
      "Multiplier chips (×6/5, ×3/4 …) or a + b + ab/100 for two changes. Up-then-down by the same rate → net −x²/100%. Three changes: chain the chips.",
      "pct-change",
      "The price of an article rises by 20% and then falls by 20%. What is the net change?",
      "Net = −20²/100 = −4%. Chips: 6/5 × 4/5 = 24/25 → a 4% decrease."),
    P("'More than / less than' flip", "very common",
      "'A's income is 25% more than B's; B's income is what % less than A's?' — the base changes mid-question.",
      "Flip formulas: 100x/(100+x) (more→less) and 100x/(100−x) (less→more). Or set the unmentioned quantity to 100. Chains of percentages: multiply fractions.",
      "pct-more-less",
      "A's income is 20% more than B's. B's income is what per cent less than A's?",
      "B = 100, A = 120 → gap 20 on base 120 → 100 × 20/120 = 16⅔% less."),
    P("Population / depreciation over years", "common",
      "Population grows or falls at stated yearly rates (same or different); find present, past, or future value.",
      "Chain the chips forward (×1.1, ×0.9 …); divide by them to go back. Two different rates: never average — multiply chips. (1 − r/100)² ≠ 1 − 2r/100.",
      "pct-population-election",
      "The population of a town is 40,000. It increases by 10% in the first year and decreases by 5% in the second. Population at the end of the second year?",
      "40000 × 11/10 × 19/20 = 44,000 × 0.95 = 41,800."),
    P("Election / voting percentages", "common",
      "Two candidates, invalid votes given, winner's share of valid votes and margin given; find total votes or votes got.",
      "Everything sits on VALID votes: valid = (100 − invalid)% of polled; margin = share gap × valid; then unmask the total.",
      "pct-population-election",
      "In an election, 20% of the votes polled were invalid. The winner got 60% of the valid votes and won by 1,200 votes. How many votes were polled?",
      "Margin = 20% of valid → valid = 6,000 = 80% of polled → polled = 7,500."),
    P("Pass marks with two candidates", "common",
      "One candidate fails by f marks at p%, another exceeds pass by e at q%; find maximum marks or the pass mark.",
      "(q − p)% of M = f + e. Solve M, then pass mark = pM/100 + f; verify with the second candidate.",
      "pct-marks-income",
      "A candidate scoring 33% fails by 45 marks; another scoring 45% gets 15 marks more than the pass marks. Find the maximum marks.",
      "12% of M = 45 + 15 = 60 → M = 500; pass mark = 165 + 45 = 210."),
    P("Price rise vs consumption / expenditure", "common",
      "'Price rises 20%, by what % reduce consumption to keep expenditure same' or the reverse (k kg more for a fixed outlay).",
      "Quantity factor = expenditure factor ÷ price factor; standard cut = 100r/(100+r)%. Outlay version: r% of the money buys the extra quantity at the reduced price.",
      "pct-marks-income",
      "A 20% cut in the price of oil lets a family buy 5 kg more for ₹400. Find the original price per kg.",
      "Saving = 20% of 400 = ₹80 → reduced price = 80/5 = ₹16 → original = 16 × 5/4 = ₹20."),
    P("Income–expenditure–savings change", "occasional",
      "Savings % given; income and expenditure change by given %; find the % change in savings.",
      "Set income = 100, track all three quantities with chips, and compute the new savings directly — the % change in savings is never guessed.",
      "pct-marks-income",
      "A person spends 80% of his income. Income rises 15% and expenditure rises 10%. Find the % increase in savings.",
      "100/80/20 → 115/88/27 → savings rise 7/20 × 100 = 35%."),
]

if __name__ == "__main__":
    subs = [build_basics(), build_change(), build_moreless(), build_population(), build_income()]
    apply_topic("percentage", subs, PYQ)
