"""Phase-2 deep content for quant/time-work. Run: py -3 time-work.py"""
import os
import sys
from fractions import Fraction as F

sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
from _lib import apply_topic
from tw_rates import build_basics, build_eff
from tw_pipes_md import build_pipes, build_mandays
from tw_cases import build_cases


def P(pattern, frequency, howToSpot, approach, subtopic, q, sol):
    return {"pattern": pattern, "frequency": frequency, "howToSpot": howToSpot, "approach": approach,
            "subtopic": subtopic, "example": {"q": q, "solution": sol}}


PYQ = [
    P("Two or three people working together", "very common",
      "Individual completion times are given and the time working together is asked — or the reverse, with the together time given and one person's time missing.",
      "Take the job as LCM units and add the daily rates; for two people use ab/(a+b). To find a missing worker, subtract his partners' rates from the together rate. The combined time must be less than the fastest individual time.",
      "tw-basics",
      "A can finish a job in 15 days and B in 10 days. Working together, they finish it in:",
      "Job = 30 units; A does 2/day, B does 3/day → 5/day → 6 days."),
    P("Pipes & cisterns", "very common",
      "Fill pipes and an outlet (or a leak) act on a tank; the fill time is asked, or a pipe opens mid-way and the tank must be re-solved in stages.",
      "Mark inlets + and outlets −, set the tank as LCM units, and take the net rate. A fill–drain pair alone is ab/(b−a). For staged problems, compute the stage-1 work first, then divide the remainder by the new net rate.",
      "tw-pipes",
      "A pipe fills a tank in 12 hours and another empties the full tank in 24 hours. With both open, the tank fills in:",
      "Net rate = 1/12 − 1/24 = 1/24 → 24 hours."),
    P("Efficiency comparisons", "common",
      "'A is twice/thrice as efficient as B', an efficiency ratio like 3 : 2, or a percent such as '50% more efficient', with a together time or one individual time given.",
      "Convert everything to a rate ratio first (50% more = 3:2). Weaker worker = 1 unit/day, stronger = k units/day, so the job = (k+1) × together-days units; divide by each rate for individual times.",
      "tw-efficiency",
      "A is twice as efficient as B and together they finish a work in 18 days. B alone takes:",
      "Job = 3 × 18 = 54 units → B alone 54 days (A alone 27)."),
    P("A leaves or joins mid-work", "common",
      "Someone works a few days and then leaves (or joins late); the remaining or total time, or the fraction each person did, is asked.",
      "Work actually done = rate × days. Subtract it from the job and hand the remainder to the continuing workers at their own rate. For a late joiner, add the solo phase to the team phase.",
      "tw-cases",
      "A can do a work in 12 days and B in 18 days. A works 3 days and leaves. B alone finishes the rest in:",
      "A did 3/12 = 1/4 → B needs (3/4) × 18 = 13.5 days."),
    P("Alternate days", "common",
      "A and B work one day each in turn (someone starts); the total time or the finishing day is asked.",
      "Count progress per 2-day cycle: 1/T_A + 1/T_B per cycle. Complete the full cycles that fit, then walk the leftover day by day — checking whose turn each leftover day is.",
      "tw-cases",
      "A can do a job in 3 days and B in 6 days. Working on alternate days starting with A, the job is finished in:",
      "Cycle = 1/3 + 1/6 = 1/2 per 2 days → exactly 2 cycles = 4 days."),
    P("Men–days–hours chain", "common",
      "Men, days and hours per day appear in two scenarios (efficiency too, sometimes); one value of the second scenario is missing.",
      "Equate the products: M1D1H1E1 = M2D2H2E2 for the same work. Put everything that grows with time beside M and solve for the missing quantity; more men always means fewer days.",
      "tw-man-days",
      "12 men working 8 hours a day finish a work in 15 days. 18 men working 10 hours a day will finish it in:",
      "12 × 15 × 8 = 1440 man-hours → 1440 ÷ (18 × 10) = 8 days."),
    P("Provisions / consumption", "common",
      "A garrison, fort or hostel has food for M men for D days; after some days men join or leave and the remaining duration is asked.",
      "Stock = M × D man-days. Subtract M × t for the days already passed, then divide the remaining stock by the new headcount.",
      "tw-man-days",
      "A garrison of 400 men has food for 25 days. After 5 days, 100 more men join. The food now lasts:",
      "Stock left = 400 × 20 = 8000 man-days → 8000 ÷ 500 = 16 days."),
    P("Wages distribution", "common",
      "A total wage for a jointly completed job is given; one worker's share is asked, sometimes with unequal days or an unknown third worker.",
      "Shares follow work done: rate × days for each worker, as a ratio. Equal days reduce it to the rate ratio; find an unknown member's rate as team rate minus the others.",
      "tw-cases",
      "A and B earn ₹600 together. A alone does the job in 10 days, B in 15 days. A's share is:",
      "Rates 3 : 2 → A gets (3/5) × 600 = ₹360."),
]

# arithmetic behind the pyq examples
assert 30 // (2 + 3) == 6 and 12 * 24 // (24 - 12) == 24
assert 3 * 18 == 54
assert F(3, 4) * 18 == F(27, 2)
assert (1 / 3 + 1 / 6) == 0.5 and 12 * 15 * 8 == 1440
assert 400 * 20 // 500 == 16 and 600 * 3 // 5 == 360

if __name__ == "__main__":
    subs = [build_basics(), build_eff(), build_pipes(), build_mandays(), build_cases()]
    apply_topic("time-work", subs, PYQ)
