"""Phase-2 deep content for quant/interest. Run: py -3 interest.py"""
import os
import sys
from fractions import Fraction

sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
from _lib import apply_topic
from int_si_ci import build_si, build_ci
from int_diff_inst_rate import build_cisidiff, build_instalments, build_ratetime


def P(pattern, frequency, howToSpot, approach, subtopic, q, sol):
    return {"pattern": pattern, "frequency": frequency, "howToSpot": howToSpot, "approach": approach,
            "subtopic": subtopic, "example": {"q": q, "solution": sol}}


PYQ = [
    P("Direct SI — find P, R or T", "very common",
      "Three of principal, rate, time and SI (or the amount) are given; the fourth is asked.",
      "SI = PRT/100; if an amount is given take SI = A − P first. 'n times in T years' gives R = 100(n−1)/T — the interest is only (n−1) times the principal.",
      "int-si",
      "A sum of money doubles itself in 10 years at simple interest. In how many years will it become triple itself?",
      "R = 100/10 = 10%; tripling needs 200% interest → 20 years."),
    P("Amount at compound interest (chips)", "very common",
      "P, R and a small whole number of years are given, compounded annually — amount or CI asked.",
      "A = P(1 + R/100)^T using fraction chips (10% → 11/10). Net per cents: 2 years at 10% → 21%, at 20% → 44%. For P from A, divide by the chip power.",
      "int-ci",
      "What sum will amount to ₹6,655 in 3 years at 10% per annum compound interest?",
      "6655 ÷ 1.1³ = 6655 ÷ 1.331 = ₹5,000."),
    P("CI − SI difference (2 or 3 years)", "very common",
      "'The difference between CI and SI for 2 (or 3) years is ₹d' — find the sum or the rate.",
      "2 years: P(R/100)². 3 years: P(R/100)²(3 + R/100). Reverse the factor to get P. With both CI and SI given, R = 200 × difference/SI for 2 years.",
      "int-ci-si-diff",
      "The difference between the compound interest and simple interest on a sum for 2 years at 10% per annum is ₹50. The sum is:",
      "P = 50 × 10000/100 = ₹5,000."),
    P("Half-yearly / quarterly compounding", "very common",
      "'Compounded half-yearly or quarterly', usually for 1–2 years including halves like 1½ years.",
      "Halve the rate and double the periods (quarter them for quarterly): A = P(1 + R/200)^(2T). Count periods carefully — 1½ years half-yearly is 3 periods.",
      "int-ci",
      "Find the compound interest on ₹10,000 at 20% per annum for 1½ years, compounded half-yearly.",
      "3 half-years at 10%: 10000 × 1.1³ = 13310 → CI ₹3,310."),
    P("Doubling / tripling chain", "common",
      "'Doubles in T years — when is it 4, 8, 16 times?' at CI, or the same chain at SI.",
      "CI: powers of 2 — 8 times in 3T. SI: linear — (n−1) rule, R = 100(n−1)/T. Mixing the two growth laws is the trap.",
      "int-ci-si-diff",
      "A sum doubles itself in 8 years at compound interest. In how many years will it become 8 times itself?",
      "8 = 2³ → 3 × 8 = 24 years."),
    P("Equal annual instalments", "common",
      "'A loan is repaid in 2 or 3 equal annual instalments at R% interest' — find the instalment or the loan.",
      "Discount each instalment: P = Σ x/(1+r)^k. 10%, 2 years: P = 210x/121. Verify with a zero-balance table. SI version: P = nx − (r/100)x·n(n−1)/2.",
      "int-instalments",
      "A loan of ₹3,310 at 10% per annum compound interest is repaid in 3 equal annual instalments. Each instalment is:",
      "3310 = x(10/11 + 100/121 + 1000/1331) → x = ₹1,331."),
    P("Different rates in different years", "common",
      "'8% in the first year, 10% in the second', compounded annually.",
      "Multiply year-wise chips: A = P(1+r₁)(1+r₂). A negative year (loss) uses its own chip. Never average the rates.",
      "int-ci",
      "₹25,000 is invested at 10% for the first year and 20% for the second, compounded annually. The amount is:",
      "25000 × 1.1 × 1.2 = ₹33,000."),
    P("Rate from consecutive amounts", "common",
      "Amounts after two consecutive years are given — at CI they fix the ratio, at SI the difference.",
      "CI: A₂/A₁ = 1 + R/100. SI: A₂ − A₁ = one year's interest = PR/100; subtract from the amount for P. Non-consecutive gaps: divide by the year gap.",
      "int-rate-time-cases",
      "A sum amounts to ₹4,840 in 2 years and ₹5,324 in 3 years at compound interest. The rate per annum is:",
      "5324/4840 = 1.1 → 10%."),
]

# arithmetic behind the pyq examples
assert 100 * (3 - 1) / 10 == 20 and 200 / 10 == 20
assert 6655 / Fraction(1331, 1000) == 5000
assert 50 * 10000 / 100 == 5000
assert 10000 * Fraction(11, 10) ** 3 == 13310
assert 3 * 8 == 24  # 8 times = 2^3, so 3 doubling periods of 8 years
assert 3310 * Fraction(1331, 3310) == 1331
assert abs(25000 * 1.1 * 1.2 - 33000) < 1e-9
assert Fraction(5324, 4840) == Fraction(11, 10)

if __name__ == "__main__":
    subs = [build_si(), build_ci(), build_cisidiff(), build_instalments(), build_ratetime()]
    apply_topic("interest", subs, PYQ)
