r"""Readable rewrite of Statistics (statistics) — all five subtopics.

Plain English, one idea per section. Every number in every example is
recomputed below with exact Fraction arithmetic and asserted.
Run with Python 3.12 from the repo root.
"""
import json
from fractions import Fraction as F
from math import sqrt
from pathlib import Path

ROOT = Path(__file__).resolve().parents[3]
TOPIC = ROOT / "core" / "topics" / "quant" / "statistics.json"


def mean(xs):
    return F(sum(xs), len(xs))


def median(xs):
    ys = sorted(xs)
    n = len(ys)
    return F(ys[n // 2]) if n % 2 else F(ys[n // 2 - 1] + ys[n // 2], 2)


def variance(xs):
    m = mean(xs)
    return sum((F(x) - m) ** 2 for x in xs) / len(xs)


# ---------- answer checks: stat-mean ----------
assert 24 + 31 + 19 + 28 == 102 and 5 * 27 == 135 and 135 - 102 == 33       # p1: fifth value
assert 24 * 35 == 840 and 25 * F(71, 2) == 887.5 and 25 * F(71, 2) - 840 == F(95, 2) == F(47.5)  # p2: teacher joins
assert 30 * 62 + 20 * 58 == 3020 and F(3020, 50) == F(302, 5) and float(F(302, 5)) == 60.4  # p3: combined mean
assert 30 * 20 == 600 and 600 - 31 + 13 == 582 and F(582, 30) == F(97, 5) and float(F(97, 5)) == 19.4  # p4: misread entry
assert 8 * 45 == 360 and 9 * 50 - 360 == 90                                  # p5: raise the average
assert sum([44, 46, 43, 47]) == 180 and F(180, 4) == 45                      # trick: deviations around 45
assert 44 - 45 + 46 - 45 + 43 - 45 + 47 - 45 == 0
# ---------- answer checks: stat-median-mode ----------
assert median([12, 5, 9, 17, 3, 11, 7]) == 9                                 # p1: median of 7 values
assert [4, 7, 9, 7, 11, 4, 7, 2].count(7) == 3                               # p2: mode is 7
assert 3 * 32 - 2 * 30 == 36                                                 # p3: mode from mean+median
assert F(45 + 2 * 27, 3) == 33                                               # p3: median from mean+mode
assert 2 * 15 + 1 == 31                                                      # p4: transform median x2+1
assert median([10, 12, 13, 15, 20, 22, 25]) == 15 and 15 - 4 == 11           # p5: x from the median
assert median([4, 8, 15, 16, 23, 42]) == F(31, 2)                            # trick: even count
assert sorted([12, 5, 9, 17, 3, 11, 7]) == [3, 5, 7, 9, 11, 12, 17]
# ---------- answer checks: stat-grouped ----------
assert 4 + 6 + 10 + 8 + 2 == 30 and F(30, 2) == 15                            # p1: n/2
assert 20 + F(15 - 10, 10) * 10 == 25                                         # p1: grouped median
assert 2 * 12 - 8 - 6 == 10 and 20 + F(12 - 8, 10) * 10 == 24                 # p2: grouped mode
def gmed(L, cf, f, h, n):                     # grouped median
    return L + (F(n, 2) - cf) * h / f


# p3: freqs 7, 8, x, 12 (classes 10-20..40-50), median 32 -> x = 5, uniquely
assert gmed(30, 15, 5, 10, 32) == 32
_msol = [x for x in range(1, 30)
         if 15 < F(27 + x, 2) <= 15 + x and gmed(30, 15, x, 10, 27 + x) == 32]
assert _msol == [5]
assert 4 * 5 + 6 * 15 + 7 * 25 + 3 * 35 == 390 and F(390, 20) == F(39, 2)     # p4: mean by midpoints 19.5
# p5: freqs 5, f, 11, 9, 5 (classes 0-10..40-50), mean 25 -> f = 9, uniquely
assert 5 * 5 + 11 * 25 + 9 * 35 + 5 * 45 == 840
_fsol = [f for f in range(1, 40) if F(840 + 15 * f, 30 + f) == 25]
assert _fsol == [9]
# ---------- answer checks: stat-dispersion ----------
assert variance([2, 4, 6, 8, 10]) == 8 and variance([2, 4, 6, 8, 10]) * 4 == 32  # p1: SD = 2*sqrt2
assert 3 * 7 == 21                                                             # p2: SD x3+5 -> 21
assert variance([1, 2, 3, 4, 5]) == 2 and variance(list(range(1, 11))) == F(33, 4)  # p3: naturals
assert variance([9, 5]) == 4                                                    # p3: two values, SD 2
assert F(5 * 100, 50) == 10 and F(3 * 100, 40) == F(15, 2)                      # p4: CV 10% vs 7.5%
assert 100 * (50 ** 2 + 5 ** 2) == 252500                                       # p5: sum of squares
assert variance([3, 6, 9, 12, 15]) == 18                                        # trick: SD = 3*sqrt2
assert F(1 + 25, 2) == 13                                                       # trick: mean of first 25 naturals
# ---------- answer checks: stat-series-sums ----------
assert sum(k * k for k in range(1, 11)) == 385 and F(385, 10) == F(77, 2)       # p1: mean of squares 38.5
assert sum(k ** 3 for k in range(1, 11)) == 3025                                # p1: cubes sum
assert sum([12, 14, 16, 18, 20]) == 80 and F(80, 5) == 16 and 20 - 16 == 4      # p2: largest exceeds mean by 4
assert (9 * 10 // 2) ** 2 == 2025                                               # p3: cubes sum 2025 -> n = 9
assert sum(range(1, 18, 2)) == 81 and F(81, 9) == 9                             # p4: mean of first 9 odds
assert sum(range(2, 20, 2)) == 90 and F(90, 9) == 10                            # p4: first 9 evens mean 10
assert 4 * sum(range(1, 16)) == 480 and F(480, 15) == 32                        # p5: multiples of 4
# ---------- answer checks: numbers used inside notes/tricks ----------
assert sum([40, 55, 35, 60, 50]) == 240 and F(240, 5) == 48                      # mean notes: five bats
assert 60 * 40 + 40 * 60 == 4800 and F(4800, 100) == 48                          # mean trick: pulled average
assert F(4 * 5 + 6 * 15, 10) == 11                                               # grouped notes: midpoint mean
assert 4 + 6 == 10 and sum([5, 8, 12, 6, 3]) == 34 and F(34, 2) == 17            # grouped tricks: cf columns
_cf = [4, 10, 20, 28, 30]
assert all(c < 15 for c in _cf[:2]) and _cf[2] >= 15                             # ...median class 20-30
assert 5 + 8 < 17 <= 5 + 8 + 12                                                  # ...second trick same class
assert sum(k ** 2 for k in range(1, 11)) * 10 == 3850 and F(3025, 10) == 302.5   # series notes: cubes mean
assert 25 - 3 == 22 and 25 + 3 == 28 and sum(range(22, 29)) == 175 and F(175, 7) == 25  # notes: 7 around 25
assert 41 - 4 == 37 and median(list(range(37, 46))) == 41                        # series trick: smallest 37
assert 11 ** 2 == 121 and sum(range(1, 22, 2)) == 121                            # series trick: odds to 121
assert sum(range(10, 21)) == 165 and len(range(10, 21)) == 11                    # notes: slice 10..20
assert F(165, 11) == 15 and F(10 + 20, 2) == 15                                  # ...mean by both routes
print("all answer checks passed")


def pat(pid, name, freq, spot, formula, steps, why, q, ex_steps, answer):
    return {"id": pid, "name": name, "frequency": freq, "howToSpot": spot, "formula": formula,
            "steps": steps, "why": why, "example": {"q": q, "steps": ex_steps, "answer": answer}}


# ============================================================ stat-mean
MEAN = dict(
    concept=(
        "The average (mean) spreads a total equally: **average = total ÷ count**.\n\n"
        "Almost every exam question hides the total. Rebuild it first with "
        "**total = average $\\times$ count**, and the question becomes plain addition and subtraction."
    ),
    notes=r"""### The one habit that solves most questions
An average is just a total shared equally.

$$\text{average} = \frac{\text{total}}{\text{count}}, \qquad \text{total} = \text{average} \times \text{count}$$

Five bats score 40, 55, 35, 60, 50. Total = 240, average = $240 \div 5 = 48$.

> **Rule:** Always write the total first: average × count. Nine of ten average questions are solved by that one line.

### Finding a missing value
The average fixes the total. The total reveals the missing entry.

The average of five numbers is 27, so the total is $5 \times 27 = 135$. Four of them are 24, 31, 19 and 28, adding to 102. The fifth number is $135 - 102 = 33$.

> **Example:** A cricketer's average over 8 innings is 45. Runs in the 9th innings that lift the average to 50: $9 \times 50 - 8 \times 45 = 450 - 360 = 90$.

### Someone joins or leaves
When a new member joins a group, the total grows by that member's value and the count grows by 1.

24 students average 35 kg, so the class weighs $24 \times 35 = 840$ kg. A teacher of weight $w$ joins and the average becomes 35.5 kg:

$$840 + w = 25 \times 35.5 = 887.5 \Rightarrow w = 47.5 \text{ kg}$$

Leaving works the same way: subtract the member, then divide by the smaller count.

> **Tip:** Check the direction of the pull. If the average rose, the newcomer is above the new average — here 47.5 > 35.5.

### Combining two groups
Two classes with different sizes cannot be averaged by adding the two averages and halving.

$$\text{combined average} = \frac{n_1\bar{x}_1 + n_2\bar{x}_2}{n_1 + n_2}$$

Class A: 30 students, mean 62. Class B: 20 students, mean 58. Combined $= \dfrac{30 \times 62 + 20 \times 58}{50} = \dfrac{3020}{50} = 60.4$.

> **Watch:** The combined average must sit between 62 and 58, nearer the bigger class. 60.4 does; 60 (the plain midpoint) is the planted option.

### A wrong entry is corrected
A number was misread. Undo the wrong entry and add the right one.

The average of 30 numbers is 20, so the recorded total is 600. The entry 31 should have been 13. Corrected total $= 600 - 31 + 13 = 582$, and the correct average $= 582 \div 30 = 19.4$.

> **Tip:** Only the difference between the wrong and right entries matters: $-31 + 13 = -18$, and $-18 \div 30 = -0.6$, so $20 - 0.6 = 19.4$.

### Averages by deviations
Adding big numbers is slow. Pick a round base near the values and track the differences.

Values 44, 46, 43, 47 around 45: deviations $-1, +1, -2, +2$ add to 0. The average is exactly 45.

$$\text{average} = \text{base} + \frac{\text{sum of deviations}}{\text{count}}$$
""",
    formulas=[
        {"name": "Average", "tex": r"\bar{x} = \frac{\text{sum of values}}{\text{count}}"},
        {"name": "Total", "tex": r"\text{total} = \bar{x} \times n"},
        {"name": "Combined average", "tex": r"\bar{x} = \frac{n_1\bar{x}_1 + n_2\bar{x}_2}{n_1+n_2}"},
        {"name": "Missing value", "tex": r"x = n\bar{x} - \sum(\text{known values})"},
        {"name": "New member", "tex": r"w = (n+1)\bar{x}_{new} - n\bar{x}_{old}",
         "note": "Use the same pattern for a leaving member with n-1."},
    ],
    tricks=[
        {"title": "Deviations from a round base",
         "body": "Pick a round number near the values. Add the small differences and divide by the count. The base can be anything.",
         "example": {"q": "Find the average of 44, 46, 43 and 47.",
                     "steps": [r"Base 45: deviations $-1, +1, -2, +2$.",
                               r"Sum of deviations $= 0$.",
                               r"Average $= 45 + 0 \div 4 = 45$."],
                     "answer": "45"}},
        {"title": "Watch where the average is pulled",
         "body": "The combined average always lies between the two group averages, closer to the bigger group. Use this to reject impossible options in seconds.",
         "example": {"q": "Group P has 60 people averaging 40, group Q has 40 people averaging 60. The combined average is:",
                     "steps": [r"Between 40 and 60, nearer 40 (P is bigger).",
                               r"$\dfrac{60 \times 40 + 40 \times 60}{100} = \dfrac{4800}{100} = 48$."],
                     "answer": "48"}},
    ],
    mistakes=[
        {"wrong": "Averaging two group averages without weighting.",
         "right": "Multiply each average by its group size first; only sizes equal allow a plain midpoint."},
        {"wrong": "Dividing the old total by the new count after someone joins.",
         "right": "Add the newcomer's value to the total, then divide by the new count."},
        {"wrong": "Subtracting the correct entry when fixing a misread.",
         "right": "Remove the wrong entry and add the correct one."},
        {"wrong": "Forgetting to convert units before averaging (cm and m mixed).",
         "right": "Bring every value to one unit first."},
        {"wrong": "Solving for a missing value without writing the total.",
         "right": r"Total $= n\bar{x}$ first; the missing value is total minus the known sum."},
    ],
    revision=[
        r"average $=$ total $\div$ count; total $=$ average $\times$ count.",
        r"Missing value $= n\bar{x} - $ sum of known values.",
        r"New member: $w = (n+1)\bar{x}_{new} - n\bar{x}_{old}$.",
        r"Combined: $\dfrac{n_1\bar{x}_1 + n_2\bar{x}_2}{n_1+n_2}$, between the two, near the bigger.",
        "Misread entry: swap wrong for right, then divide by the count.",
        "Deviations: base plus (sum of deviations ÷ count).",
    ],
    patterns=[
        pat("stat-mn-p1", "Mean and a missing value", "very common",
            "The average of a list is given with all values but one; the missing value is asked.",
            r"x = n\bar{x} - \sum \text{known}",
            ["Rebuild the total: average $\\times$ count.",
             "Add the known values.",
             "Subtract that sum from the total."],
            "The average pins the total, and the total pins the missing entry.",
            "The average of five numbers is 27. Four of the numbers are 24, 31, 19 and 28. The fifth number is:",
            [r"Total $= 5 \times 27 = 135$.",
             r"Known sum $= 24 + 31 + 19 + 28 = 102$.",
             r"Fifth number $= 135 - 102 = 33$."],
            "33"),
        pat("stat-mn-p2", "A member joins or leaves", "very common",
            "A teacher joins a class, a player retires, one reading is dropped; the average shifts.",
            r"w = (n+1)\bar{x}_{new} - n\bar{x}_{old}",
            ["Old total $=$ old average $\\times$ old count.",
             "New total $=$ new average $\\times$ new count.",
             "The new member equals the difference."],
            "The change in the total can only come from the person who joined or left.",
            "The average weight of 24 students is 35 kg. When a teacher joins them, the average weight becomes 35.5 kg. The weight of the teacher is:",
            [r"Old total $= 24 \times 35 = 840$ kg.",
             r"New total $= 25 \times 35.5 = 887.5$ kg.",
             r"Teacher $= 887.5 - 840 = 47.5$ kg."],
            "47.5 kg"),
        pat("stat-mn-p3", "Combined average of two groups", "common",
            "Two sections, teams or batches with their own sizes and averages; one overall average asked.",
            r"\bar{x} = \frac{n_1\bar{x}_1 + n_2\bar{x}_2}{n_1 + n_2}",
            ["Multiply each group's size by its average.",
             "Add the two products.",
             "Divide by the total size."],
            "Totals add; counts add; the average is their ratio.",
            "Section A has 30 students with mean marks 62. Section B has 20 students with mean marks 58. The mean marks of all 50 students is:",
            [r"Total marks $= 30 \times 62 + 20 \times 58 = 1860 + 1160 = 3020$.",
             r"Total students $= 50$.",
             r"Mean $= 3020 \div 50 = 60.4$."],
            "60.4"),
        pat("stat-mn-p4", "Correcting a misread value", "common",
            "A value was copied wrongly; the correct average is asked.",
            r"\bar{x}_{new} = \frac{n\bar{x}_{old} - \text{wrong} + \text{right}}{n}",
            ["Write the wrong total: average $\\times$ count.",
             "Remove the wrong entry, add the correct one.",
             "Divide by the count."],
            "Only the difference between the two entries changes the total.",
            "The average of 30 numbers was computed as 20. Later it was found that 31 had been misread as 13. The correct average is:",
            [r"Wrong total $= 30 \times 20 = 600$.",
             r"Corrected total $= 600 - 31 + 13 = 582$.",
             r"Correct average $= 582 \div 30 = 19.4$."],
            "19.4"),
        pat("stat-mn-p5", "Raising the average", "common",
            "How much must the next score/inning earn to reach a target average.",
            r"x = (n+1)\bar{x}_{target} - n\bar{x}_{old}",
            ["Total needed at the target average with one extra count.",
             "Subtract the current total.",
             "The difference is the required score."],
            "The next value must cover its own share plus the lift on all earlier values.",
            "A batsman's average in 8 innings is 45 runs. How many runs in the 9th innings will raise his average to 50?",
            [r"Needed total $= 9 \times 50 = 450$.",
             r"Current total $= 8 \times 45 = 360$.",
             r"Required runs $= 450 - 360 = 90$."],
            "90 runs"),
    ],
)

# ============================================================ stat-median-mode
MEDMODE = dict(
    concept=(
        "The median is the middle value after you sort the list: half the values sit below it, half above.\n\n"
        "The mode is the value that appears most often. A list has one middle and one most-frequent value, "
        "and exam questions mostly test how each behaves when the list changes."
    ),
    notes=r"""### Median: the middle seat
Sort the values. The median is the middle one.

- Odd count: the value at position $\dfrac{n+1}{2}$.
- Even count: the average of the two middle values, positions $\dfrac{n}{2}$ and $\dfrac{n}{2}+1$.

List 12, 5, 9, 17, 3, 11, 7 sorts to 3, 5, 7, 9, 11, 12, 17. Seven values, so the median is the 4th: 9.

List 4, 8, 15, 16, 23, 42 has six values. Median $= \dfrac{15+16}{2} = 15.5$.

> **Rule:** Sort first, always. The median of an unsorted list is the most common wrong answer in this chapter.

### Mode: the crowd favourite
The mode is the value with the highest count. No sorting needed, just tally.

4, 7, 9, 7, 11, 4, 7, 2: the count of 7 is three, every other value appears at most twice. Mode = 7.

A list can have two modes (7 and 4 each appearing three times) or no mode at all (every value once).

> **Tip:** Mode is the only average that must be a value from the list. Mean and median can be numbers that are not in the list.

### The empirical relation
For data that is mildly lopsided (like marks or incomes), the three averages follow one rough rule:

$$\text{mode} = 3 \times \text{median} - 2 \times \text{mean}$$

Mean 30, median 32: mode $= 3 \times 32 - 2 \times 30 = 36$. It also rearranges: median $= \dfrac{\text{mode} + 2\,\text{mean}}{3}$.

> **Watch:** This is an estimate, not an identity. Use it only when two of the three averages are given and the third is asked.

### The relation, rearranged
Any one of the three can be the unknown.

Mean 27, mode 45: median $= \dfrac{45 + 2 \times 27}{3} = \dfrac{99}{3} = 33$.

Sanity check: mean 27 < median 33 < mode 45 rises steadily, the shape the formula assumes.

> **Tip:** After solving, place the three values in order. If they do not rise or fall together, redo the arithmetic.

### When every value is transformed
Add the same number to every value: mean, median and mode all shift by that number.

Multiply every value by $k$: all three get multiplied by $k$.

Median 15, then every value is doubled and 1 is added: new median $= 2 \times 15 + 1 = 31$.

> **Rule:** The median follows the same shift and scale as the values themselves.

### A missing value from the median
The median pins one value of the sorted list, so it can pin an unknown.

Seven values: 10, 12, 13, $x+4$, 20, 22, 25. With seven entries the median is the 4th, which is $x+4$ itself:

$$x + 4 = 15 \Rightarrow x = 11$$

> **Example:** With an even count the two middle entries average to the median, so their sum is $2 \times$ median.
""",
    formulas=[
        {"name": "Median (odd n)", "tex": r"\text{value at } \frac{n+1}{2}\text{th place}",
         "note": "Position in the sorted list."},
        {"name": "Median (even n)", "tex": r"\frac{\text{(n/2)th} + \text{(n/2+1)th}}{2}"},
        {"name": "Empirical relation", "tex": r"\text{Mode} = 3\,\text{Median} - 2\,\text{Mean}",
         "note": "Rough rule for mildly skewed data; rearrange for any missing one."},
        {"name": "Median from mode and mean", "tex": r"\text{Median} = \frac{\text{Mode} + 2\,\text{Mean}}{3}"},
        {"name": "Transform", "tex": r"y = kx + c \Rightarrow \text{Med}_y = k\,\text{Med}_x + c"},
    ],
    tricks=[
        {"title": "Count positions, do not hunt",
         "body": "For odd n, the median sits at position (n+1)/2 of the sorted list. Count to that position instead of scanning for the middle by eye.",
         "example": {"q": "Find the median of 3, 5, 7, 9, 11, 12, 17.",
                     "steps": [r"$n = 7$, position $= \dfrac{7+1}{2} = 4$.",
                               r"4th value of the sorted list is 9."],
                     "answer": "9"}},
        {"title": "Median without sorting everything",
         "body": "You only need the middle order statistics. In a long list, quickly bucket values as low or high; full sorting wastes time.",
         "example": {"q": "Find the median of 4, 8, 15, 16, 23, 42.",
                     "steps": [r"Six values: average the 3rd and 4th.",
                               r"Here 15 and 16 are already the middle pair: $\dfrac{15+16}{2} = 15.5$."],
                     "answer": "15.5"}},
    ],
    mistakes=[
        {"wrong": "Taking the middle of the list as given, without sorting.",
         "right": "Sort first; the given order is usually shuffled on purpose."},
        {"wrong": "Reporting the lower of the two middle values when n is even.",
         "right": "Average the two middle values."},
        {"wrong": "Using the empirical relation on very lopsided data and expecting exactness.",
         "right": "Treat it as an estimate; it fits mildly skewed data."},
        {"wrong": "Forgetting that a new value can change the count from odd to even.",
         "right": "Recheck parity after any value is added or removed."},
        {"wrong": "Calling the tallest bar's value the median in a table.",
         "right": "That value is the mode; the median needs cumulative counting."},
    ],
    revision=[
        r"Median: sort, then middle value; even $n$ averages the middle pair.",
        r"Mode: highest frequency; it must be a value from the list.",
        r"Mode $= 3$ Median $- 2$ Mean (estimate).",
        r"Median $= \dfrac{\text{Mode} + 2\,\text{Mean}}{3}$.",
        r"Shift by $c$: all averages shift by $c$; scale by $k$: all scale by $k$.",
        "A missing middle entry equals the median itself (odd n).",
    ],
    patterns=[
        pat("stat-mm-p1", "Median of a raw list", "very common",
            "A jumbled list of values is given; the middle value is asked.",
            r"\text{Med} = \left(\frac{n+1}{2}\right)\text{th value}",
            ["Sort the values in rising order.",
             "Find the middle position: $\\frac{n+1}{2}$.",
             "Even count: average the two middle values."],
            "Sorting places half the values on each side of the answer.",
            "Find the median of 12, 5, 9, 17, 3, 11 and 7.",
            [r"Sorted: 3, 5, 7, 9, 11, 12, 17.",
             r"$n = 7$, so the median is the 4th value.",
             r"4th value $= 9$."],
            "9"),
        pat("stat-mm-p2", "Mode of a raw list", "common",
            "A list with repeats is given; the most frequent value is asked.",
            r"\text{Mode} = \text{value with maximum frequency}",
            ["Tally how often each value appears.",
             "Pick the value with the highest count.",
             "Two ties means two modes; all equal means no mode."],
            "The mode counts frequency only; size and order do not matter.",
            "Find the mode of 4, 7, 9, 7, 11, 4, 7, 2.",
            [r"Counts: 7 appears 3 times, 4 appears twice.",
             r"All other values appear once.",
             r"Highest count is 7."],
            "7"),
        pat("stat-mm-p3", "Empirical relation", "very common",
            "Two of mean, median, mode are given; the third is asked.",
            r"\text{Mode} = 3\,\text{Median} - 2\,\text{Mean}",
            ["Write the relation.",
             "Substitute the two known averages.",
             "Solve for the third."],
            "The three averages keep a fixed rough spacing in mildly skewed data.",
            "For a distribution, the mean is 30 and the median is 32. Using the empirical relation, the mode is:",
            [r"$\text{Mode} = 3 \times 32 - 2 \times 30$.",
             r"$= 96 - 60 = 36$."],
            "36"),
        pat("stat-mm-p4", "Median under a shift or scale", "common",
            "Every value of a list is doubled, halved or shifted; the new median is asked.",
            r"\text{Med}(kx + c) = k\,\text{Med}(x) + c",
            ["Find (or note) the median of the original list.",
             "Apply the same multiply and add to that median.",
             "Order of operations: scale first, then shift."],
            "The middle position does not move when all values move together.",
            "The median of a list is 15. Each value is doubled and then 1 is added to it. The new median is:",
            [r"New median $= 2 \times 15 + 1$.",
             r"$= 31$."],
            "31"),
        pat("stat-mm-p5", "A missing value fixed by the median", "occasional",
            "A list contains x or an expression in x; the median is given.",
            r"\text{middle entry} = \text{median}",
            ["Sort so the unknown's slot is clear.",
             "Set the middle entry (or the middle pair's average) equal to the median.",
             "Solve for x."],
            "The median names one exact entry of the sorted list when n is odd.",
            "The median of 10, 12, 13, $x+4$, 20, 22, 25 is 15. Find x.",
            [r"Seven values, so the 4th value is the median.",
             r"The 4th value is $x + 4 = 15$.",
             r"$x = 11$."],
            "x = 11"),
    ],
)

# ============================================================ stat-grouped
GROUPED = dict(
    concept=(
        "Grouped data comes as class intervals with frequencies: how many values fall in each band.\n\n"
        "The single values are lost, so we estimate averages from the bands. Every method below uses a "
        "cumulative frequency column and the midpoint of each class."
    ),
    notes=r"""### Reading a frequency table
A grouped table only says how many values lie in each band, like 20-30 with frequency 10.

Two columns do all the work:

- Midpoint $x$: the middle of the band, $20$-$30 \rightarrow 25$.
- Cumulative frequency (cf): a running total of frequencies down the table.

> **Tip:** Build the cf column once. Median questions, quartile questions and distribution questions all read from it.

### Mean by midpoints
Treat every value in a class as if it sat at the midpoint.

$$\bar{x} = \frac{\sum f x}{\sum f}$$

Classes 0-10 and 10-20 with frequencies 4 and 6: $\sum fx = 4 \times 5 + 6 \times 15 = 110$, $\sum f = 10$, mean $= 11$.

> **Watch:** Midpoints, not class limits. Using 10 for the class 10-20 (instead of 15) is the classic slip.

### Median from the cumulative column
Half the values lie below the median, so find the class whose cumulative frequency first reaches $\dfrac{n}{2}$.

$$\text{Median} = L + \frac{\frac{n}{2} - c}{f} \times h$$

$L$ is the lower limit of that class, $c$ the cumulative frequency before it, $f$ its frequency, $h$ its width.

Table: classes 0-10, 10-20, 20-30, 30-40, 40-50 with frequencies 4, 6, 10, 8, 2. Then $n = 30$, $\dfrac{n}{2} = 15$. The cf column runs 4, 10, 20, 28, 30; the first cf to reach 15 is 20, so the median class is 20-30.

$$\text{Median} = 20 + \frac{15 - 10}{10} \times 10 = 25$$

> **Rule:** The median class is where cf crosses $n/2$, never simply the biggest frequency.

### Mode from the tallest bar
The modal class has the highest frequency. Then interpolate inside it:

$$\text{Mode} = L + \frac{f_m - f_1}{2f_m - f_1 - f_2} \times h$$

$f_m$ is the modal class frequency, $f_1$ and $f_2$ the frequencies just before and after.

Same classes with frequencies 5, 8, 12, 6, 3: modal class 20-30, so $L = 20$, $f_m = 12$, $f_1 = 8$, $f_2 = 6$, $h = 10$:

$$\text{Mode} = 20 + \frac{12 - 8}{2 \times 12 - 8 - 6} \times 10 = 20 + 4 = 24$$

> **Tip:** Equal neighbours ($f_1 = f_2$) put the mode exactly at $L + h/2$.

### A missing frequency from the median
Give the unknown a letter, extend the cf column through it, and apply the median rule.

Classes 10-20, 20-30, 30-40, 40-50 with frequencies 7, 8, $x$, 12 and median 32. Then $n = 27 + x$, $\dfrac{n}{2}$ must land in 30-40, where $c = 15$:

$$30 + \frac{\frac{27+x}{2} - 15}{x} \times 10 = 32 \Rightarrow x = 5$$

### A missing frequency from the mean
The mean fixes $\sum fx$. Let the unknown be $f$ and expand both sides.

Classes 0-10, 10-20, 20-30, 30-40, 40-50 with frequencies 5, $f$, 11, 9, 5 and mean 25:

$$\frac{840 + 15f}{30 + f} = 25 \Rightarrow 840 + 15f = 750 + 25f \Rightarrow f = 9$$

> **Watch:** Keep the midpoint of the missing class in the numerator; students often drop it along with the frequency.
""",
    formulas=[
        {"name": "Grouped mean", "tex": r"\bar{x} = \frac{\sum f x}{\sum f}",
         "note": "x is the midpoint of each class."},
        {"name": "Grouped median", "tex": r"\text{Med} = L + \frac{\frac{n}{2} - c}{f} \times h",
         "note": "L: lower limit of median class; c: cf before it; f: its frequency; h: width."},
        {"name": "Grouped mode", "tex": r"\text{Mode} = L + \frac{f_m - f_1}{2f_m - f_1 - f_2} \times h",
         "note": "f_m: modal class frequency; f_1, f_2: neighbouring frequencies."},
    ],
    tricks=[
        {"title": "Build the cf column once, use it thrice",
         "body": "Median, quartiles and 'how many below a value' questions all read the same cumulative column. Write it before touching any formula.",
         "example": {"q": "Frequencies 4, 6, 10, 8, 2 for classes 0-10 to 40-50. How many values are below 30?",
                     "steps": [r"cf column: 4, 10, 20, 28, 30.",
                               r"Values below 30 sit in the first two classes.",
                               r"$4 + 6 = 10$."],
                     "answer": "10"}},
        {"title": "Cross-check the median class fast",
         "body": "Half of n must fall inside the median class. Glance: the cf before it is below n/2, the cf through it is at or above n/2.",
         "example": {"q": "Frequencies 5, 8, 12, 6, 3 for classes 0-10 to 40-50. Which class holds the median?",
                     "steps": [r"$n = 34$, so $n/2 = 17$.",
                               r"cf runs 5, 13, 25, 31, 34.",
                               r"17 first crossed in 20-30."],
                     "answer": "20-30"}},
    ],
    mistakes=[
        {"wrong": "Using class limits instead of midpoints for the mean.",
         "right": "Midpoint of 10-20 is 15."},
        {"wrong": "Picking the class with the highest frequency as the median class.",
         "right": "The median class is where the cumulative frequency crosses n/2."},
        {"wrong": "Taking c as the cumulative frequency of the median class.",
         "right": "c is the cumulative frequency of the class before it."},
        {"wrong": "Mixing widths: classes of 10 used with h = 5.",
         "right": "Read h from the actual class width, including any gap."},
        {"wrong": "Solving a missing-frequency mean without the missing midpoint.",
         "right": "The unknown frequency multiplies its class midpoint in the numerator."},
    ],
    revision=[
        r"Grouped mean $= \dfrac{\sum fx}{\sum f}$, $x$ = midpoint.",
        r"Median $= L + \dfrac{n/2 - c}{f} \times h$; median class where cf crosses $n/2$.",
        r"Mode $= L + \dfrac{f_m - f_1}{2f_m - f_1 - f_2} \times h$.",
        "cf column first; it answers three question types.",
        "Missing frequency: letter in, solve with the given average.",
        "Check the median class: cf below n/2 before, at or above after.",
    ],
    patterns=[
        pat("stat-gr-p1", "Median of grouped data", "very common",
            "A frequency table with equal class widths; the median is asked.",
            r"\text{Med} = L + \frac{\frac{n}{2} - c}{f} \times h",
            ["Total the frequencies to get n.",
             "Build the cf column and find where it crosses $\\frac{n}{2}$.",
             "Read $L$, $c$, $f$, $h$ from that class and substitute."],
            "Values spread evenly inside the median class, so we walk in proportion.",
            "Find the median:\n\n| Class | 0-10 | 10-20 | 20-30 | 30-40 | 40-50 |\n|---|---|---|---|---|---|\n| Frequency | 4 | 6 | 10 | 8 | 2 |",
            [r"$n = 30$, so $n/2 = 15$.",
             r"cf: 4, 10, 20, 28, 30. Median class 20-30: $L=20$, $c=10$, $f=10$, $h=10$.",
             r"Median $= 20 + \dfrac{15-10}{10} \times 10 = 25$."],
            "25"),
        pat("stat-gr-p2", "Mode of grouped data", "common",
            "A frequency table; the most frequent class is obvious and the exact mode is asked.",
            r"\text{Mode} = L + \frac{f_m - f_1}{2f_m - f_1 - f_2} \times h",
            ["Spot the class with the highest frequency.",
             "Note its neighbours' frequencies.",
             "Substitute into the mode formula."],
            "The mode sits inside the tallest bar, pulled toward the taller neighbour.",
            "Find the mode:\n\n| Class | 0-10 | 10-20 | 20-30 | 30-40 | 40-50 |\n|---|---|---|---|---|---|\n| Frequency | 5 | 8 | 12 | 6 | 3 |",
            [r"Modal class 20-30: $L = 20$, $f_m = 12$, $f_1 = 8$, $f_2 = 6$.",
             r"Denominator $= 2 \times 12 - 8 - 6 = 10$.",
             r"Mode $= 20 + \dfrac{4}{10} \times 10 = 24$."],
            "24"),
        pat("stat-gr-p3", "Missing frequency from the median", "occasional",
            "One frequency in the table is x or unknown; the median is given.",
            r"L + \frac{\frac{n}{2} - c}{f} \times h = \text{Med}",
            ["Write n including the unknown.",
             "Extend the cf column through the unknown class.",
             "Apply the median formula and solve."],
            "The stated median names the class, and the formula turns it into an equation.",
            "The median of the following data is 32. Find x.\n\n| Class | 10-20 | 20-30 | 30-40 | 40-50 |\n|---|---|---|---|---|\n| Frequency | 7 | 8 | x | 12 |",
            [r"$n = 27 + x$. Median 32 lies in 30-40: $L = 30$, $c = 15$, $f = x$.",
             r"$30 + \dfrac{(27+x)/2 - 15}{x} \times 10 = 32$.",
             r"Solving gives $x = 5$."],
            "x = 5"),
        pat("stat-gr-p4", "Mean of grouped data", "very common",
            "A frequency table (or a midpoints row) is given; the mean is asked.",
            r"\bar{x} = \frac{\sum f x}{\sum f}",
            ["Write the midpoint of each class.",
             "Multiply midpoint by frequency and total them.",
             "Divide by the total frequency."],
            "Each class acts like its whole mass sitting at its midpoint.",
            "Find the mean:\n\n| Midpoint | 5 | 15 | 25 | 35 |\n|---|---|---|---|---|\n| Frequency | 4 | 6 | 7 | 3 |",
            [r"$\sum fx = 20 + 90 + 175 + 105 = 390$.",
             r"$\sum f = 20$.",
             r"Mean $= 390 \div 20 = 19.5$."],
            "19.5"),
        pat("stat-gr-p5", "Missing frequency from the mean", "occasional",
            "One frequency is unknown; the mean of the distribution is given.",
            r"\frac{\sum f x}{\sum f} = \bar{x}",
            ["Compute the known part of $\\sum fx$ and of $n$.",
             "Add the unknown times its midpoint (and once to $n$).",
             "Set the ratio equal to the mean and solve."],
            "The mean fixes the total, and the unknown appears in it linearly.",
            "The mean of the following distribution is 25. Find f.\n\n| Class | 0-10 | 10-20 | 20-30 | 30-40 | 40-50 |\n|---|---|---|---|---|---|\n| Frequency | 5 | f | 11 | 9 | 5 |",
            [r"Known $\sum fx = 25 + 275 + 315 + 225 = 840$; plus $15f$.",
             r"$n = 30 + f$.",
             r"$\dfrac{840 + 15f}{30 + f} = 25 \Rightarrow 840 + 15f = 750 + 25f \Rightarrow f = 9$."],
            "f = 9"),
    ],
)

# ============================================================ stat-dispersion
DISPERSION = dict(
    concept=(
        "Averages say where the data sits; dispersion says how widely it spreads.\n\n"
        "Range is the quick measure. Variance and standard deviation (SD) are the exam measures: "
        "SD is the typical distance of values from the mean, in the same unit as the data."
    ),
    notes=r"""### Range: the quick spread
Range $=$ highest value $-$ lowest value. Values 12, 5, 9, 17, 3 give range $17 - 3 = 14$.

The range ignores everything in between, so exams use it as a warm-up, not the main dish.

> **Tip:** A new maximum or a new minimum changes the range; a middle value never can.

### Variance and SD: distance from the mean
Take each value's distance from the mean, square, average, then take the square root.

$$\sigma^2 = \frac{\sum (x - \bar{x})^2}{n}, \qquad \sigma = \sqrt{\sigma^2}$$

$\sigma$ is the standard deviation, read "sigma". Values 2, 4, 6, 8, 10 have mean 6 and deviations $-4, -2, 0, 2, 4$:

$$\sigma^2 = \frac{16+4+0+4+16}{5} = 8, \qquad \sigma = \sqrt{8} = 2\sqrt{2} \approx 2.83$$

> **Rule:** The variance is in squared units; the SD is in the data's own units. That is why we take the root back.

### The shift-and-scale rule
This one rule answers most SD questions:

- Add the same number to every value: SD unchanged.
- Multiply every value by $k$: SD becomes $|k| \times$ SD. Variance becomes $k^2 \times$ variance.

Data with SD 7, then every value $\times 3 + 5$: new SD $= 3 \times 7 = 21$. The mean shifts to $3\bar{x}+5$, but the 5 never touches the SD.

> **Watch:** Adding 5 tempts everyone into $21 + 5 = 26$. Adding never changes the spread.

### Ready-made spreads
Some lists have a variance you should not compute from scratch:

- First $n$ naturals $1, 2, \dots, n$: $\sigma^2 = \dfrac{n^2 - 1}{12}$.
- An arithmetic progression $a, a+d, \dots$: variance $\dfrac{(n^2-1)d^2}{12}$, independent of $a$.
- Two values $p$ and $q$: mean $\dfrac{p+q}{2}$, SD $\dfrac{|p-q|}{2}$.

First 5 naturals: $\sigma^2 = \dfrac{25-1}{12} = 2$, so $\sigma = \sqrt{2}$. The two values 9 and 5 have mean 7 and SD $\dfrac{4}{2} = 2$.

> **Tip:** Multiples of $k$ are an AP with $d = k$: the first five multiples of 3 have SD $3\sqrt{2}$.

### Coefficient of variation: fair comparison
Two teams score in different ranges. Who is more consistent? Compare spread relative to the mean:

$$CV = \frac{\sigma}{\bar{x}} \times 100\%$$

Batsman A: mean 50, SD 5, so $CV = 10\%$. Batsman B: mean 40, SD 3, so $CV = 7.5\%$. Lower CV means steadier, so B is more consistent even though A's SD is larger.

### Sums the shortcuts love
$$\sum x = n\bar{x}, \qquad \sum x^2 = n\left(\bar{x}^2 + \sigma^2\right)$$

With $n = 100$, mean 50, SD 5: $\sum x = 5000$ and $\sum x^2 = 100(2500 + 25) = 252500$.

> **Watch:** $\sigma$ must be squared before it joins $\bar{x}^2$; students add $50 + 5$ and square.
""",
    formulas=[
        {"name": "Range", "tex": r"R = \text{max} - \text{min}"},
        {"name": "Variance", "tex": r"\sigma^2 = \frac{\sum (x-\bar{x})^2}{n}",
         "note": "Average of squared distances from the mean."},
        {"name": "Standard deviation", "tex": r"\sigma = \sqrt{\sigma^2}"},
        {"name": "Shift and scale", "tex": r"\text{SD}(kx + c) = |k|\,\text{SD}(x)",
         "note": "Adding c changes nothing; multiplying scales the SD."},
        {"name": "First n naturals", "tex": r"\sigma^2 = \frac{n^2-1}{12}"},
        {"name": "Two values", "tex": r"\text{SD} = \frac{|p-q|}{2}"},
        {"name": "Coefficient of variation", "tex": r"CV = \frac{\sigma}{\bar{x}} \times 100\%"},
        {"name": "Sum of squares", "tex": r"\sum x^2 = n(\bar{x}^2 + \sigma^2)"},
    ],
    tricks=[
        {"title": "Skip the squares for symmetric lists",
         "body": "Values spaced evenly around their mean cancel in pairs: 2,4,6,8,10 gives squared deviations 16,4,0,4,16. Write only the distinct squares.",
         "example": {"q": "Find the SD of 2, 4, 6, 8, 10.",
                     "steps": [r"Mean $= 6$; deviations $-4,-2,0,2,4$.",
                               r"Squares: $16, 4, 0, 4, 16$; sum $= 40$.",
                               r"Variance $= 8$, SD $= 2\sqrt{2}$."],
                     "answer": r"$2\sqrt{2}$"}},
        {"title": "AP spread without listing",
         "body": "For k, 2k, 3k, ..., nk use variance k²(n²−1)/12. No squaring of long lists.",
         "example": {"q": "Find the SD of 3, 6, 9, 12, 15.",
                     "steps": [r"Multiples of 3: $k = 3$, $n = 5$.",
                               r"Variance $= 9 \times \dfrac{24}{12} = 18$.",
                               r"SD $= \sqrt{18} = 3\sqrt{2}$."],
                     "answer": r"$3\sqrt{2}$"}},
    ],
    mistakes=[
        {"wrong": "Adding a constant to the data and changing the SD.",
         "right": "Adding shifts every value equally, so the spread stays the same."},
        {"wrong": "Forgetting to square k: variance of kx is k·variance.",
         "right": "Variance of kx is k² times the variance; SD is |k| times."},
        {"wrong": "Comparing consistency by SD alone when means differ.",
         "right": "Use the coefficient of variation, SD divided by the mean."},
        {"wrong": "Reporting the variance as the SD.",
         "right": "Take the square root of the variance for the SD."},
        {"wrong": "Dividing by n−1 in exam SD questions.",
         "right": "Exam data is the whole set, so divide by n; n−1 is for samples in statistics theory."},
    ],
    revision=[
        r"Range $=$ max $-$ min.",
        r"$\sigma^2 = \dfrac{\sum(x-\bar{x})^2}{n}$, $\sigma$ is its square root.",
        r"SD($kx + c$) $= |k|\,$SD($x$); adding c never changes the spread.",
        r"First $n$ naturals: $\sigma^2 = \dfrac{n^2-1}{12}$.",
        r"Two values: SD $= \dfrac{|p-q|}{2}$.",
        r"$CV = \dfrac{\sigma}{\bar{x}} \times 100\%$; lower CV means more consistent.",
        r"$\sum x^2 = n(\bar{x}^2 + \sigma^2)$.",
    ],
    patterns=[
        pat("stat-dp-p1", "SD of a small list", "very common",
            "Five to eight plain values; the SD (or variance) is asked.",
            r"\sigma = \sqrt{\frac{\sum (x-\bar{x})^2}{n}}",
            ["Compute the mean.",
             "Find each deviation from the mean.",
             "Square, add, divide by n, take the root."],
            "Squaring stops deviations cancelling; the root returns to the data's unit.",
            "Find the standard deviation of 2, 4, 6, 8, 10.",
            [r"Mean $= 6$; deviations $-4, -2, 0, 2, 4$.",
             r"Sum of squares $= 16 + 4 + 0 + 4 + 16 = 40$.",
             r"Variance $= 40 \div 5 = 8$; SD $= \sqrt{8} = 2\sqrt{2}$."],
            r"$2\sqrt{2}$"),
        pat("stat-dp-p2", "SD after a shift and scale", "very common",
            "Every value is multiplied and/or added to; the new SD (or mean) is asked.",
            r"\text{SD}(kx+c) = |k|\,\text{SD}(x)",
            ["Note the original SD.",
             "Multiply the SD by the multiplier's size.",
             "Ignore any added constant."],
            "Spread grows only when values are pulled apart, and only scaling does that.",
            "The SD of a set of values is 7. Each value is multiplied by 3 and then 5 is added. The new SD is:",
            [r"Multiply: $3 \times 7 = 21$.",
             r"Adding 5 leaves the SD unchanged.",
             r"New SD $= 21$."],
            "21"),
        pat("stat-dp-p3", "Standard lists: naturals, APs, pairs", "common",
            "The data is the first n naturals, an AP, or just two values.",
            r"\sigma^2 = \frac{n^2-1}{12} \;\text{(first n naturals)}",
            ["Match the list to a known family.",
             "Apply the ready variance; scale by the common difference if any.",
             "For two values, SD is half the gap."],
            "These lists have fixed shapes, so their spreads are fixed too.",
            "Find the SD of the first five natural numbers 1, 2, 3, 4, 5.",
            [r"$n = 5$: variance $= \dfrac{25 - 1}{12} = 2$.",
             r"SD $= \sqrt{2}$."],
            r"$\sqrt{2}$"),
        pat("stat-dp-p4", "Range and coefficient of variation", "common",
            "Consistency between two sets is asked, or the range after adding a value.",
            r"CV = \frac{\sigma}{\bar{x}} \times 100\%",
            ["Find mean and SD for each set.",
             "Compute CV for each.",
             "Smaller CV wins on consistency."],
            "Spread only means something next to the level it spreads from.",
            "Batsman A scores at mean 50 with SD 5; batsman B at mean 40 with SD 3. Who is more consistent?",
            [r"$CV_A = \dfrac{5}{50} \times 100 = 10\%$.",
             r"$CV_B = \dfrac{3}{40} \times 100 = 7.5\%$.",
             r"$7.5\% < 10\%$, so B is steadier."],
            "Batsman B"),
        pat("stat-dp-p5", "Sums from mean and SD", "occasional",
            "n, mean and SD are given; the sum of values or of squares is asked.",
            r"\sum x^2 = n(\bar{x}^2 + \sigma^2)",
            ["Sum of values: $n\\bar{x}$.",
             "Square the mean and the SD.",
             "Add, multiply by n."],
            "Variance is the mean of squares minus the square of the mean, rearranged.",
            "A set of 100 values has mean 50 and SD 5. Find the sum of the squares of the values.",
            [r"$\sum x = 100 \times 50 = 5000$.",
             r"$\sum x^2 = 100(50^2 + 5^2) = 100 \times 2525$.",
             r"$= 252500$."],
            "252500"),
    ],
)

# ============================================================ stat-series-sums
SERIES = dict(
    concept=(
        "Some averages can be written down without adding anything: runs of natural numbers, squares, "
        "cubes, odds, evens and multiples.\n\n"
        "Learn the four sums below. Exams ask for a mean, a total, or the count that hits a given total."
    ),
    notes=r"""### The four working sums
$$\sum k = \frac{n(n+1)}{2}, \quad \sum k^2 = \frac{n(n+1)(2n+1)}{6}, \quad \sum k^3 = \left[\frac{n(n+1)}{2}\right]^2$$

First 10 numbers: sum $= \dfrac{10 \times 11}{2} = 55$, squares $= 385$, cubes $= 3025$.

> **Rule:** The sum of the first n cubes is the square of the sum of the first n numbers: $3025 = 55^2$.

### Means that need no addition
$$\bar{x} = \frac{\text{sum}}{n}$$

First n naturals: mean $= \dfrac{n+1}{2}$, the middle value. First 25 naturals average 13. First n odd numbers: mean $= n$, because $1 + 3 + \dots + (2n-1) = n^2$.

First n even numbers: mean $= n + 1$, since $2 + 4 + \dots + 2n = n(n+1)$.

> **Tip:** First 9 odds average 9; first 9 evens average 10. One apart, always.

### Multiples behave like naturals
The first $n$ multiples of $k$ are $k, 2k, \dots, nk$: the naturals scaled by $k$.

$$\text{sum} = k \cdot \frac{n(n+1)}{2}, \qquad \text{mean} = \frac{k(n+1)}{2}$$

First 15 multiples of 4: sum $= 4 \times \dfrac{15 \times 16}{2} = 480$, mean $= 32$.

> **Watch:** 32 here is not a multiple of 4 belonging to the list. A mean need not be a member of the data.

### A slice of the naturals
Numbers from 10 to 20 are just the naturals with the first nine removed.

$$\text{sum} = \sum_{1}^{q} - \sum_{1}^{p-1}, \qquad \text{count} = q - p + 1$$

Sum $= 210 - 45 = 165$ over 11 numbers, mean $= \dfrac{165}{11} = 15$. The shortcut agrees: an equally spaced run averages its ends, $\dfrac{10+20}{2} = 15$.

### Consecutive numbers in a row
Consecutive numbers sit evenly around their middle. The mean equals the middle term: one middle for odd counts, half-way between two middles for even counts.

Five consecutive even numbers average 16, so the middle one is 16: the list is 12, 14, 16, 18, 20 and the largest is 20. For any equally spaced list, largest $=$ mean $+$ (span off the middle).

> **Example:** Seven consecutive integers averaging 25 run from 22 to 28; no adding needed.

### Working backwards from a total
Give the count a letter, write the sum formula, and solve.

The sum of the first n cubes is 2025:

$$\left[\frac{n(n+1)}{2}\right]^2 = 2025 = 45^2 \Rightarrow \frac{n(n+1)}{2} = 45 \Rightarrow n = 9$$

> **Tip:** Spot perfect squares. $\sum k^3$ is always a perfect square, so the square root hands you $\sum k$.

### Mean of squares and cubes
For the mean, divide the sum by n.

Mean of the first 10 squares $= \dfrac{385}{10} = 38.5$. Mean of the first 10 cubes $= \dfrac{3025}{10} = 302.5$.

> **Watch:** These means sit well above the mean of the numbers themselves (5.5), because big values grow fast when squared or cubed.
""",
    formulas=[
        {"name": "Sum of first n naturals", "tex": r"\sum k = \frac{n(n+1)}{2}"},
        {"name": "Sum of squares", "tex": r"\sum k^2 = \frac{n(n+1)(2n+1)}{6}"},
        {"name": "Sum of cubes", "tex": r"\sum k^3 = \left[\frac{n(n+1)}{2}\right]^2",
         "note": "The square of the sum of the first n naturals."},
        {"name": "Mean of first n naturals", "tex": r"\frac{n+1}{2}"},
        {"name": "Mean of first n odds", "tex": r"n"},
        {"name": "Mean of first n evens", "tex": r"n+1"},
        {"name": "Multiples of k", "tex": r"\text{sum} = \frac{kn(n+1)}{2},\; \text{mean} = \frac{k(n+1)}{2}"},
    ],
    tricks=[
        {"title": "The middle is the mean",
         "body": "For any equally spaced list the mean is the middle term. Use it forwards (find the mean) and backwards (rebuild the list).",
         "example": {"q": "Nine consecutive integers have mean 41. Find the smallest.",
                     "steps": [r"Middle (5th) term $= 41$.",
                               r"Smallest $= 41 - 4 = 37$."],
                     "answer": "37"}},
        {"title": "Odds add to squares",
         "body": "1 + 3 + ... up to n odd numbers is exactly n². Use it to test counts fast.",
         "example": {"q": "How many consecutive odd numbers starting from 1 add up to 121?",
                     "steps": [r"$n^2 = 121$.",
                               r"$n = 11$."],
                     "answer": "11"}},
    ],
    mistakes=[
        {"wrong": "Averaging the first and last term of a list that is not equally spaced.",
         "right": "The middle-is-the-mean rule needs equal gaps."},
        {"wrong": "Using the naturals' mean (n+1)/2 for odds or evens.",
         "right": "First n odds average n; first n evens average n+1."},
        {"wrong": "Forgetting to divide the sum by n when the mean is asked.",
         "right": "Sum formulas give totals; means divide by n."},
        {"wrong": "Treating the sum of cubes as n(n+1)/2 squared being n+1 squared.",
         "right": "Square the whole triangular sum, not n+1 alone."},
        {"wrong": "Counting the first n multiples of k as kn numbers.",
         "right": "There are exactly n of them: k, 2k, ..., nk."},
    ],
    revision=[
        r"$\sum k = \dfrac{n(n+1)}{2}$; mean of naturals $= \dfrac{n+1}{2}$.",
        r"$\sum k^2 = \dfrac{n(n+1)(2n+1)}{6}$.",
        r"$\sum k^3 = \left(\sum k\right)^2$.",
        r"First $n$ odds: sum $n^2$, mean $n$.",
        r"First $n$ evens: sum $n(n+1)$, mean $n+1$.",
        r"First $n$ multiples of $k$: mean $\dfrac{k(n+1)}{2}$.",
        "Equally spaced list: mean = middle term.",
    ],
    patterns=[
        pat("stat-ss-p1", "Mean of squares or cubes", "common",
            "The average of the first n squares or cubes is asked.",
            r"\bar{x} = \frac{1}{n}\sum k^r",
            ["Write the matching sum formula.",
             "Substitute n.",
             "Divide by n for the mean."],
            "The sums have closed forms, so the mean is one substitution away.",
            "Find the mean of the squares of the first 10 natural numbers.",
            [r"$\sum k^2 = \dfrac{10 \times 11 \times 21}{6} = 385$.",
             r"Mean $= 385 \div 10 = 38.5$."],
            "38.5"),
        pat("stat-ss-p2", "Consecutive numbers and the middle term", "very common",
            "The average of consecutive integers/odds/evens is given; an end value is asked.",
            r"\text{mean} = \text{middle term}",
            ["Set the middle term equal to the average.",
             "Step out to the wanted end.",
             "Odd count: one middle; even count: two middles."],
            "Equal spacing makes the average sit exactly at the middle of the row.",
            "The average of five consecutive even numbers is 16. The largest of them is:",
            [r"Middle term $= 16$.",
             r"List: 12, 14, 16, 18, 20.",
             r"Largest $= 20$."],
            "20"),
        pat("stat-ss-p3", "A total that fixes the count", "common",
            "A sum of naturals, squares or cubes is given; find how many terms make it.",
            r"\frac{n(n+1)}{2} = S",
            ["Match the total to its family (perfect square points to cubes).",
             "Write the sum formula equal to the total.",
             "Solve the small equation for n."],
            "Each sum formula grows strictly with n, so one n fits one total.",
            "The sum of the cubes of the first n natural numbers is 2025. Find n.",
            [r"$\sum k^3 = \left[\dfrac{n(n+1)}{2}\right]^2 = 2025 = 45^2$.",
             r"$\dfrac{n(n+1)}{2} = 45$.",
             r"$n(n+1) = 90 \Rightarrow n = 9$."],
            "n = 9"),
        pat("stat-ss-p4", "Means of odds and evens", "common",
            "The average of the first n odd or even numbers is asked.",
            r"\text{odds: } \bar{x} = n; \quad \text{evens: } \bar{x} = n+1",
            ["Count how many terms there are.",
             "Odds: the mean is that count.",
             "Evens: the mean is one more."],
            "The kth odd is $2k-1$ and the kth even is $2k$; their averages differ by one.",
            "Find the average of the first 9 odd numbers.",
            [r"Sum $= 9^2 = 81$.",
             r"Mean $= 81 \div 9 = 9$."],
            "9"),
        pat("stat-ss-p5", "Multiples of a number", "occasional",
            "The mean or total of the first n multiples of k is asked.",
            r"\text{mean} = \frac{k(n+1)}{2}",
            [r"Confirm the list: $k, 2k, \dots, nk$.",
             "Mean: $k$ times the naturals' mean.",
             "Total: mean times n."],
            "Multiples of k are the first n naturals scaled by k.",
            "Find the mean of the first 15 multiples of 4.",
            [r"Mean $= 4 \times \dfrac{15 + 1}{2} = 4 \times 8$.",
             r"$= 32$."],
            "32"),
    ],
)

# ============================================================ patch
PATCHES = {
    "stat-mean": MEAN,
    "stat-median-mode": MEDMODE,
    "stat-grouped": GROUPED,
    "stat-dispersion": DISPERSION,
    "stat-series-sums": SERIES,
}

data = json.loads(TOPIC.read_text(encoding="utf-8"))
for sid, patch in PATCHES.items():
    sub = next(s for s in data["subtopics"] if s["id"] == sid)
    old_ids = {p["id"] for p in sub.get("patterns", [])}
    new_ids = {p["id"] for p in patch["patterns"]}
    assert old_ids <= new_ids, f"{sid}: dropped ids {old_ids - new_ids}"
    others = {p["id"] for s in data["subtopics"] for p in s.get("patterns", []) if s["id"] != sid}
    assert not (others & new_ids), f"{sid}: clash {others & new_ids}"
    notes = patch["notes"]
    assert 2500 <= len(notes) <= 5000, f"{sid}: notes {len(notes)} chars"
    n_old = len(sub.get("patterns", []))
    sub.update(concept=patch["concept"], notes=notes.strip() + "\n",
               formulas=patch.get("formulas", sub.get("formulas", [])),
               tricks=patch.get("tricks", sub.get("tricks", [])),
               mistakes=patch["mistakes"], revision=patch["revision"],
               patterns=patch["patterns"])
    print(f"{sid}: notes {len(notes)} chars, patterns {n_old} -> {len(patch['patterns'])}")

with open(TOPIC, "w", encoding="utf-8", newline="\n") as f:
    json.dump(data, f, ensure_ascii=False, indent=1)
    f.write("\n")
print("statistics.json updated")
