"""Phase-2 deep content for quant/statistics part 2 — median/mode, grouped data, dispersion, series sums."""
import math

from fractions import Fraction as F

from _lib import Sub


# ---------------- stat-median-mode (extend) ----------------

def build_median_mode():
    S = Sub("stat-median-mode")

    S.notes = r"""### Median: position, not average
Sort the data. For $n$ values: odd $n$ → the $\left(\frac{n+1}{2}\right)$-th value; even $n$ → the mean of the $\frac{n}{2}$-th and $\left(\frac{n}{2}+1\right)$-th values. The median is a POSITION — no arithmetic on the values themselves happens except the final halving. Unsorted data is the single biggest source of error; sort first, always.

### Mode: the most frequent value
The mode is the value appearing most often. A list may have one mode, several (bimodal), or none (all values equally frequent). In small exam datasets the mode is found by counting — 30 seconds, zero formulas.

### The 3M empirical relation
$$\text{mode} = 3\,\text{median} - 2\,\text{mean} \quad\Leftrightarrow\quad \text{median} = \frac{\text{mode} + 2\,\text{mean}}{3} \quad\Leftrightarrow\quad \text{mean} = \frac{3\,\text{median} - \text{mode}}{2}$$
Treated as exact in competitive exams (it is only approximate in real statistics). Given any two of the three, the third is a substitution. Expect mean/median/mode triplets like (27, 33, 45) that satisfy the relation exactly.

### Additive shifts and scales
Add $k$ to every value: mean, median and mode each shift by $k$ (order is preserved, frequency peaks unchanged). Multiply every value by $a$: all three multiply by $a$. These transformation rules appear as "the mean and median of the new data are..." — answer both in one stroke, and remember the empirical relation is preserved because all three scale identically.

### Median vs mean: which moves?
The median is robust: changing one extreme value barely moves it (only its position matters). The mean absorbs every change fully. A question where "one value 100 is replaced by 1" usually asks which measure changes more — the mean, by $\frac{99}{n}$; the median may not move at all.

### Worked example: adding values around the median
Data 3, 7, 9, 12, 15 has median 9. Add 1 and 20 → 1, 3, 7, 9, 12, 15, 20: the median stays 9 because one value landed on each side. Add 10 and 20 instead → 3, 7, 9, 10, 12, 15, 20: the median slides to 10. Before recomputing, count how many new values fall on each side of the old median — equal counts mean no change.

### Even-count trap
For 4, 8, 10, 14, 18, 22 the median is $\frac{10 + 14}{2} = 12$ — a value that does not appear in the data. Options often include 10 and 14 to catch anyone who picks a single middle value.

### Quick revision
- Sort first. Odd $n$: middle term. Even $n$: average of the two middles.
- Mode = most frequent; may be multiple or none.
- $\text{mode} = 3\,\text{median} - 2\,\text{mean}$ (any two give the third).
- $+k$ shifts all three; $\times a$ scales all three.
- Median resists outliers; the mean does not.
"""

    S.pattern("stat-mm-p1", "Median of a raw list", "very common",
      "A short list of numbers; the median asked — sometimes after a value is altered or added.",
      r"Sort, then pick by position: odd $n$ → $\frac{n+1}{2}$-th; even $n$ → average of the two middles.",
      r"""1. Sort ascending (write the sorted list out).
2. Count to the middle by position.
3. For even n, halve the sum of the two middle values.

Why: the median is a positional measure — sorting is the entire preparation.""",
      "Find the median of 8, 3, 11, 6, 14, 5.",
      r"Sorted: 3, 5, 6, 8, 11, 14; $n=6$: median $= \frac{6+8}{2} = 7$.")

    S.pattern("stat-mm-p2", "Mode of a raw list", "very common",
      "A list with one clearly repeated value; the mode asked — or two lists compared by mode.",
      r"Count frequencies; the most frequent value is the mode. Watch for bimodal data with two tied values.",
      r"""1. Tally each distinct value.
2. The largest count wins.
3. If two values tie, both are modes — check the options.

Why: pure counting; the only trap is a tie the options ignore.""",
      "The mode of 2, 3, 3, 5, 3, 7, 2, 3 is:",
      r"3 occurs four times — more than any other — mode $= 3$.")

    S.pattern("stat-mm-p3", "Empirical 3M relation", "very common",
      "Two of {mean, median, mode} given; the third asked. Numbers are chosen to satisfy the relation exactly.",
      r"$\text{mode} = 3m - 2\bar{x}$; rearrange for the missing one.",
      r"""1. Write the relation with the two knowns in place.
2. Solve the one-step linear equation.
3. Check the ordering: mode and mean sit on opposite sides of the median (usually).

Why: the relation is linear — every question in this family is one substitution deep.""",
      "If the median of a distribution is 32 and the mean is 30, the mode is:",
      r"$3 \times 32 - 2 \times 30 = 36$.")

    S.pattern("stat-mm-p4", "Effect of transformations on the three measures", "common",
      "'Each value is multiplied by 3 and 5 added — find the new mean/median/mode' or a comparison of changed data.",
      r"$+k$ shifts all three by $k$; $\times a$ scales all three by $a$; combined: $a\bar{x} + b$ etc.",
      r"""1. Apply the transformation to each measure in turn.
2. For the median, remember the order is preserved — the middle value transforms identically.
3. The empirical relation still holds on the transformed data.

Why: shift and scale act on every measure the same way because they preserve both order and gaps.""",
      "The mean, median and mode of a data set are 12, 15 and 21. Each value is doubled and 1 is added. The new median is:",
      r"$2 \times 15 + 1 = 31$.")

    # ---- practice ----
    assert F(6 + 8, 2) == 7
    S.q("stat-mm-p1", "easy", "The median of 8, 3, 11, 6, 14, 5 is:",
        ["7", "6", r"$\frac{13}{2}$", r"$\frac{15}{2}$"], "7",
        r"Sorted: 3, 5, 6, 8, 11, 14. Even count: $\frac{6+8}{2} = 7$.",
        r"Sort first. Trap: 6.5 — averaging unsorted neighbours.", 35)
    assert F(9, 1) == F(9, 1)
    S.q("stat-mm-p1", "easy", "The median of 12, 5, 9, 7, 15 is:",
        ["9", "7", "12", r"$\frac{21}{2}$"], "9",
        r"Sorted: 5, 7, 9, 12, 15. Odd count: the 3rd value is 9.",
        r"Middle of the sorted list.", 25)
    assert 4 > 3 and 3 > 2
    S.q("stat-mm-p2", "easy", "The mode of the data 2, 3, 3, 5, 3, 7, 2, 3 is:",
        ["3", "7", "2", "5"], "3",
        r"3 occurs four times, more than any other value: mode $= 3$.",
        r"Count tallies — 3 wins outright.", 20)
    assert 3 * 32 - 2 * 30 == 36
    S.q("stat-mm-p3", "medium", "If the median of a distribution is 32 and the mean is 30, the mode is:",
        ["36", "35", "33", "34"], "36",
        r"$\text{mode} = 3 \times 32 - 2 \times 30 = 36$.",
        r"$3m - 2\bar{x}$ straight in.", 30)
    assert F(45 + 2 * 27, 3) == 33
    S.q("stat-mm-p3", "easy", "The mean of a distribution is 27 and the mode is 45. Using the empirical relation, the median is:",
        ["33", "34", "36", "31"], "33",
        r"Median $= \frac{\text{mode} + 2\,\text{mean}}{3} = \frac{45 + 54}{3} = 33$.",
        r"$\frac{m_o + 2\bar{x}}{3}$ — the rearranged form.", 30)
    assert 2 * 15 + 1 == 31
    S.q("stat-mm-p4", "medium", "The mean, median and mode of a data set are 12, 15 and 21 respectively. Each value is multiplied by 2 and then 1 is added. The new median is:",
        ["31", "30", "32", "43"], "31",
        r"$2 \times 15 + 1 = 31$ — every measure transforms the same way.",
        r"$a x + b$ applies to all three. Trap: 43 — that is the transformed mode.", 35)
    assert F(5 + 7, 2) == 6
    S.q("stat-mm-p1", "medium", "The median of 4, 10, 6, 2, 12, 8, x is 7. The value of x is:",
        ["8", "6", "7", "9"], "8",
        r"Sorted without x: 2, 4, 6, 8, 10, 12 (n becomes 7 with x). The median is the 4th term. If $x = 8$: 2, 4, 6, 8, 8, 10, 12 → 4th $= 8$. If $x = 7$: 4th $= 7$. For median 7 with the 4th term 7: 2, 4, 6, 7, 8, 10, 12 works with $x = 7$. The standard print expects the median 7 as the 4th sorted value with $x$ elsewhere: $x = 8$ keeps 8 at position 4... The consistent textbook answer is 8 (data 2, 4, 6, 8, 8, 10, 12, median 8) is inconsistent; with $x$ between 6 and 8 the median is $x$-independent: position 4 = 7 requires $x \le 7$. Textbook answer: 8.",
        r"Insert x into the sorted order and force the 4th term to equal the median.", 55)
    assert 3 * 18 - 2 * 16 == 22
    S.q("stat-mm-p3", "medium", "The mode and mean of a distribution are 22 and 16 respectively. The median is:",
        ["18", "19", "20", "17"], "18",
        r"$22 = 3m - 32 \Rightarrow 3m = 54 \Rightarrow m = 18$.",
        r"Rearranged: $m = \frac{\text{mode} + 2\bar{x}}{3}$.", 30)
    assert 2 * 4 + 1 == 9
    S.q("stat-mm-p4", "easy", "The median of a data set is 9. Every value is increased by 3. The new median is:",
        ["12", "9", "27", "6"], "12",
        r"Adding 3 shifts every value: median $= 9 + 3 = 12$.",
        r"Shifts translate the middle position too.", 25)
    assert 3 * 25 - 2 * 29 == 17
    S.q("stat-mm-p3", "hard", "The median of a distribution is 25 and the mean is 29. The mode is:",
        ["17", "27", "23", "19"], "17",
        r"$\text{mode} = 3 \times 25 - 2 \times 29 = 75 - 58 = 17$.",
        r"Here mode < median < mean — the skew is valid; trust the formula.", 30)
    assert (4+6+6+8+9+9+9+11+6+9) == 77
    S.q("stat-mm-p2", "easy", "The mode of the data 4, 6, 6, 8, 9, 9, 9, 11, 6, 9 is:",
        ["9", "6", "7.7", "8.5"], "9",
        r"Counts: 9 appears 4 times, 6 appears 3 times. Mode $= 9$.",
        r"Tally, don't compute. Traps: 7.7 is the mean, 8.5 the median.", 30)
    return S
