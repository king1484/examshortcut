"""Phase-2 deep content for quant/average. Run: py -3 average.py"""
import os
import sys

sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
from _lib import apply_topic
from avg_basics_incl import build_basics, build_incl
from avg_weighted_misc import build_weighted, build_misc


def P(pattern, frequency, howToSpot, approach, subtopic, q, sol):
    return {"pattern": pattern, "frequency": frequency, "howToSpot": howToSpot, "approach": approach,
            "subtopic": subtopic, "example": {"q": q, "solution": sol}}


PYQ = [
    P("Person joins / leaves, average changes", "very common",
      "The average age, weight or salary of a group is given; a teacher, manager or new member joins (or someone leaves) and the new average is stated.",
      "Change both averages into totals and subtract. Shortcut: newcomer = new average + n × rise; leaver = new average + n × fall. Check with totals.",
      "avg-inclusion-exclusion",
      "The average age of 30 students is 14 years. When the teacher's age is included, the average rises by 1 year. Find the teacher's age.",
      "Teacher = 15 + 30 × 1 = 45 years. (Check: 31 × 15 − 30 × 14 = 465 − 420 = 45.)"),
    P("Replacement of one member / wrong entry", "very common",
      "One person is replaced by another, or a value was copied wrongly, and the average changes by a known amount. The count stays the same.",
      "Change in total = n × change in average, and all of it belongs to the replaced value. For a wrong entry, the average moves by (correct − wrong)/n.",
      "avg-inclusion-exclusion",
      "The average weight of 10 men rises by 1.5 kg when one man weighing 58 kg is replaced by a new man. Find the new man's weight.",
      "58 + 10 × 1.5 = 73 kg."),
    P("Batsman / bowler average", "common",
      "'Scores x in the nth innings and his average rises by d', or a bowler's runs-per-wicket average improves after a match.",
      "Write the old and new totals. Batsman: new average = x − (n − 1)d. Bowler: aW + r = (a − d)(W + w), solve for W.",
      "avg-misc",
      "A batsman scores 87 runs in his 17th innings and his average rises by 3. Find his new average.",
      "87 − 16 × 3 = 39. (Old average 36: 16 × 36 + 87 = 663 = 17 × 39.)"),
    P("Weighted average of groups", "very common",
      "Boys and girls, sections, or workers and managers with separate averages; the combined average or a missing group average is asked.",
      "Totals first: combined = Σ(n × average) ÷ Σn. The answer lies closer to the bigger group. For a missing group, subtract known totals from the overall total.",
      "avg-weighted",
      "30 boys average 42 kg and 20 girls average 37 kg. Find the class average.",
      "(1260 + 740) ÷ 50 = 40 kg."),
    P("Group sizes from averages (balance method)", "common",
      "Both group averages and the combined average are given; the ratio or number of members in a group is asked.",
      "Sizes are in the reverse ratio of the distances from the combined average: n₁ : n₂ = (x̄₂ − x̄) : (x̄ − x̄₁). The group closer to the mean is bigger.",
      "avg-weighted",
      "The class average is 58; boys average 62 and girls 52. Find boys : girls.",
      "(58 − 52) : (62 − 58) = 6 : 4 = 3 : 2."),
    P("Average of standard series and consecutive numbers", "very common",
      "Average of the first n naturals, odd or even numbers, squares, cubes, or of consecutive / equally spaced numbers.",
      "Use the table: (n + 1)/2, n, n + 1. Equally spaced numbers: average = middle term = (first + last)/2.",
      "avg-basics",
      "Find the average of all multiples of 6 between 1 and 100.",
      "6, 12, …, 96 → (6 + 96)/2 = 51."),
    P("Sum bridge and uniform operations", "common",
      "Average and count given with some values known, or every value is increased, multiplied or divided by the same number.",
      "Sum = average × count, then subtract known values. A uniform operation acts on the average in the same order: ×k then +c gives kA + c.",
      "avg-basics",
      "The average of 6 numbers is 15. Each number is multiplied by 3 and then increased by 5. Find the new average.",
      "15 × 3 + 5 = 50."),
    P("Overlapping averages and split sets", "occasional",
      "Averages over overlapping windows (Mon–Thu and Tue–Fri; first 7 and last 7 of 13) or parts of a set with a relation between unknowns.",
      "All averages to sums. Overlapping days: subtract and the shared days cancel. First/last parts: shared term = part sums − total. Split set: one variable for the unknown.",
      "avg-misc",
      "The average of 11 numbers is 50. The first 6 average 49 and the last 6 average 52. Find the 6th number.",
      "294 + 312 − 550 = 56."),
    P("Ages over time", "common",
      "Average age of a family n years ago or at a marriage / birth, with a child or member added later.",
      "Bring every average to the same year: a fixed group's average rises 1 per year. Then use totals and adjust the count.",
      "avg-misc",
      "Five years ago the average age of a husband and wife was 25. Now the average of husband, wife and child is 22. Child's age?",
      "Couple now = 50 + 10 = 60; family = 66 → child = 6 years."),
]

# arithmetic behind the pyq examples
assert 31 * 15 - 30 * 14 == 45 and 58 + 10 * 1.5 == 73
assert 16 * 36 + 87 == 17 * 39 and (1260 + 740) / 50 == 40
assert (6 + 96) / 2 == 51 and 15 * 3 + 5 == 50
assert 6 * 49 + 6 * 52 - 11 * 50 == 56 and 3 * 22 - (2 * 25 + 10) == 6

if __name__ == "__main__":
    subs = [build_basics(), build_incl(), build_weighted(), build_misc()]
    apply_topic("average", subs, PYQ)
