"""Phase-2 deep content for quant/average — basics + inclusion/exclusion modules."""
import os
import sys
from fractions import Fraction as F

sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
from _lib import Sub, num, rs, mixed


def build_basics():
    S = Sub("avg-basics")
    S.notes = r"""### What is an average?
An average is one number that stands for a whole group. If five friends have ₹20, ₹30, ₹25, ₹35 and ₹40, the total is ₹150. Shared equally, each would get $150 \div 5 = ₹30$. That ₹30 is the **average** (also called the arithmetic mean).
$$\text{Average} = \frac{\text{Sum of observations}}{\text{Number of observations}}$$
An "observation" simply means one value in the list.

### The sum bridge — the most useful idea
Turn the formula around: $\text{Sum} = \text{Average} \times n$. Almost every average question is solved by changing averages into sums, doing the adding or subtracting with sums, and only at the end dividing again.
Example: the average of 4 numbers is 25 and three of them are 20, 30 and 18. Sum $= 4 \times 25 = 100$, so the fourth $= 100 - 68 = 32$.

### Properties you should know
- The average always lies between the smallest and the largest value.
- Add (or subtract) k to every value → the average goes up (or down) by k.
- Multiply (or divide) every value by k → the average is multiplied (or divided) by k.
- Do the operations in the same order: "×3 then +5" on an average of 15 gives $15 \times 3 + 5 = 50$.
- The deviations (differences) of all values from the average add up to zero.

### Standard averages (learn by heart)
| Series | Average |
|---|---|
| First n natural numbers | $\frac{n+1}{2}$ |
| First n odd numbers | $n$ |
| First n even numbers | $n+1$ |
| Squares of first n naturals | $\frac{(n+1)(2n+1)}{6}$ |
| Cubes of first n naturals | $\frac{n(n+1)^2}{4}$ |
Example: first 20 even numbers (2 to 40) → average 21. First 25 odd numbers → average 25.

### Consecutive numbers and equal gaps
When numbers go up by the same step (consecutive, consecutive even, multiples of 7 …) the average is the **middle term**, which is also $\frac{\text{first} + \text{last}}{2}$.
7 consecutive even numbers with average 48 → middle (4th) is 48 → numbers 42 to 54 → largest 54.
Multiples of 6 from 1 to 100: 6, 12, …, 96 → average $\frac{6 + 96}{2} = 51$.

### Assumed-mean (deviation) method
To average numbers that are close together, pick a round "assumed" value, write each number as a plus or minus gap from it, average the gaps and add back.
284, 291, 296, 302, 307 around 300: gaps $-16, -9, -4, +2, +7$ → total $-20$ → average gap $-4$ → average $296$. No big addition needed.

### Common traps
- Average of averages is NOT the overall average when groups are of different sizes (see weighted average).
- Consecutive even/odd numbers step by 2, not 1.
- Read "each number is multiplied by 3 and then increased by 5" in order.

### Quick revision
- Sum = average × count; change everything to sums.
- Shift by k → average shifts by k; scale by k → average scales by k.
- Equal steps → average = middle term = (first + last)/2.
- Series table: $\frac{n+1}{2}$, $n$, $n+1$.
- Close numbers → assumed-mean method.
"""

    S.pattern("avg-b1", "Sum from average / missing value from the sum", "very common",
        "An average and a count are given; the total, or one missing value among known values, is asked.",
        r"\text{Sum} = \text{Average} \times n",
        r"""1. Multiply average by the number of values to get the sum.
2. Subtract the known values from that sum.
3. What is left is the missing value (or the asked total).

Why: the average is only the sum shared equally, so the sum carries all the information.""",
        "The average of 4 numbers is 25. Three of them are 20, 30 and 18. Find the fourth.",
        r"Sum $= 4 \times 25 = 100$; known $= 68$ → fourth $= 32$.")
    S.pattern("avg-b2", "Average of standard series (naturals, odd, even, squares, cubes)", "very common",
        "'Average of the first n natural / odd / even numbers' or of their squares or cubes.",
        r"\frac{n+1}{2},\quad n,\quad n+1,\quad \frac{(n+1)(2n+1)}{6},\quad \frac{n(n+1)^2}{4}",
        r"""1. Identify the series and n (count of terms, not the last term).
2. Read the average straight from the table.
3. For even numbers up to 2n, n is half the last term.

Why: each table value is the series-sum formula divided by n.""",
        "Find the average of the first 25 odd numbers.",
        r"Average of first n odd numbers $= n$ → $25$. (Sum $= 25^2 = 625$, $625 \div 25 = 25$.)")
    S.pattern("avg-b3", "Consecutive numbers / equal-gap series", "very common",
        "'Average of 7 consecutive even numbers is 48 — find the largest', or average of multiples of k in a range.",
        r"\text{Average} = \text{middle term} = \frac{\text{first} + \text{last}}{2}",
        r"""1. The average is the middle term of the list.
2. Step out from the middle by the common gap (1 for consecutive, 2 for even/odd, k for multiples).
3. For a range of multiples, average = (first multiple + last multiple)/2.

Why: equal gaps are balanced on both sides of the middle, so the middle is the mean.""",
        "The average of 7 consecutive even numbers is 48. Find the largest.",
        r"Middle (4th) term $= 48$; three steps of 2 up → $48 + 6 = 54$.")
    S.pattern("avg-b4", "Same operation on every value", "common",
        "'Each number is multiplied by 4 / increased by 6 / divided by 2' — the new average is asked.",
        r"\text{new average} = k \times A + c \ \ (\text{apply in the stated order})",
        r"""1. Apply the same operations to the old average, in the same order.
2. Addition shifts the average; multiplication scales it.

Why: sum and average respond to a uniform change exactly like each single value does.""",
        "The average of 6 numbers is 15. Each is multiplied by 3 and then increased by 5. New average?",
        r"$15 \times 3 + 5 = 50$.")
    S.pattern("avg-b5", "Assumed mean (deviation method)", "common",
        "A list of 4-8 close numbers (weights, marks, runs) is given and their average is asked.",
        r"\text{Average} = \text{assumed value} + \frac{\text{sum of deviations}}{n}",
        r"""1. Pick a round number near the middle.
2. Write each value's gap from it (+ or −) and add the gaps.
3. Divide the gap total by n and add to the assumed value.

Why: shifting every value by the same amount shifts the average by that amount.""",
        "Find the average of 284, 291, 296, 302 and 307.",
        r"Gaps from 300: $-16, -9, -4, +2, +7$ → total $-20$ → $\frac{-20}{5} = -4$ → average $296$.")

    # ---- practice ----
    a = F(455, 10) * 12
    assert a == 546
    S.q("avg-b1", "easy", "The average of 12 numbers is 45.5. The sum of these numbers is:",
        ["546", "540", "552", "500.5"], num(a),
        r"Sum $= 45.5 \times 12 = 546$.", None, 25)
    fifth = 5 * 36 - (30 + 42 + 28 + 45)
    assert fifth == 35
    S.q("avg-b1", "medium",
        "The average of five numbers is 36. Four of the numbers are 30, 42, 28 and 45. The fifth number is:",
        ["35", "36", "39", "33"], str(fifth),
        r"Sum $= 5 \times 36 = 180$. Known four $= 145$. Fifth $= 180 - 145 = 35$.",
        "Gaps from 36: −6, +6, −8, +9 → total +1, so the fifth must be 1 below 36 = 35.", 35)
    a = F(sum(range(1, 50, 2)), 25)
    assert a == 25
    S.q("avg-b2", "easy", "The average of the first 25 odd natural numbers is:",
        ["25", "26", "12.5", "50"], num(a),
        r"Average of the first n odd numbers is n → $25$. Check: sum $= 25^2 = 625$, $625 \div 25 = 25$.", None, 20)
    a = F(sum(range(2, 41, 2)), 20)
    assert a == 21
    S.q("avg-b2", "easy", "The average of the first 20 even natural numbers is:",
        ["21", "20", "10.5", "22"], num(a),
        r"Average of the first n even numbers is $n + 1 = 21$. (2 to 40 → $\frac{2+40}{2} = 21$.)", None, 20)
    a = F(sum(i ** 3 for i in range(1, 9)), 8)
    assert a == 162
    S.q("avg-b2", "hard", "The average of the cubes of the first 8 natural numbers is:",
        ["162", "1296", "144", "170"], num(a),
        r"""Sum of cubes $= \left(\frac{8 \times 9}{2}\right)^2 = 36^2 = 1296$.
Average $= \frac{1296}{8} = 162$.""",
        r"Direct: $\frac{n(n+1)^2}{4} = \frac{8 \times 81}{4} = 162$.", 45)
    nums = [48 + 2 * k for k in range(-3, 4)]
    assert sum(nums) / 7 == 48 and max(nums) == 54
    S.q("avg-b3", "easy", "The average of 7 consecutive even numbers is 48. The largest of them is:",
        ["54", "51", "56", "52"], "54",
        r"The 4th (middle) number is 48. Numbers: 42, 44, 46, **48**, 50, 52, 54. Largest $= 54$.",
        "Largest = middle + 3 × 2 = 54. (51 comes from stepping by 1.)", 25)
    m = [k for k in range(1, 101) if k % 6 == 0]
    a = F(sum(m), len(m))
    assert a == 51
    S.q("avg-b3", "medium", "The average of all the multiples of 6 between 1 and 100 is:",
        ["51", "50", "48", "54"], num(a),
        r"""Multiples: 6, 12, …, 96 (16 terms, equal gaps).
Average $= \frac{6 + 96}{2} = 51$.""",
        "Equal gaps → (first + last)/2 — no need to count the terms.", 35)
    for n in (5, 10, 37):
        base = list(range(n - 2, n + 3))
        assert F(sum(base + [n + 3, n + 4]), 7) == n + 1
    S.q("avg-b3", "hard",
        "The average of five consecutive natural numbers is n. If the next two consecutive numbers are also included, the average of the seven numbers becomes:",
        ["n + 1", "n + 2", "n + 1.5", "n"], "n + 1",
        r"""Numbers: $n-2, n-1, n, n+1, n+2$ (sum $5n$). Next two: $n+3, n+4$.
New sum $= 5n + 2n + 7 = 7n + 7$ → average $= n + 1$.""",
        "Seven consecutive numbers from n−2 to n+4 → middle term is n+1.", 45)
    a = 21 * 4
    S.q("avg-b4", "easy", "The average of 8 numbers is 21. If each number is multiplied by 4, the new average is:",
        ["84", "25", "168", "21"], str(a),
        r"Multiplying every value by 4 multiplies the average by 4: $21 \times 4 = 84$.", None, 20)
    a = F(40 - 6, 2)
    assert a == 17
    S.q("avg-b4", "medium",
        "The average of 10 numbers is 40. Each number is first decreased by 6 and then divided by 2. The new average is:",
        ["17", "14", "34", "20"], num(a),
        r"Apply the same steps to the average: $(40 - 6) \div 2 = 17$.",
        "Order matters: 40 ÷ 2 − 6 = 14 is the trap.", 30)
    vals = [284, 291, 296, 302, 307]
    a = F(sum(vals), 5)
    assert a == 296
    S.q("avg-b5", "medium", "Find the average of 284, 291, 296, 302 and 307.",
        ["296", "295", "297", "298"], num(a),
        r"""Sum $= 1480$, average $= \frac{1480}{5} = 296$.""",
        r"Assumed mean 300: gaps $-16, -9, -4, +2, +7$ → total $-20$ → $300 - 4 = 296$.", 35)
    vals = [F(485, 10), 52, F(505, 10), 47, F(545, 10), F(535, 10)]
    a = sum(vals) / 6
    assert a == 51
    S.q("avg-b5", "medium",
        "The weights of six children are 48.5 kg, 52 kg, 50.5 kg, 47 kg, 54.5 kg and 53.5 kg. Their average weight is:",
        ["51 kg", "50.5 kg", "51.5 kg", "52 kg"], "51 kg",
        r"Sum $= 306$ kg → average $= \frac{306}{6} = 51$ kg.",
        r"Assumed 50: gaps $-1.5, +2, +0.5, -3, +4.5, +3.5$ → total $+6$ → $50 + 1 = 51$ kg.", 40)
    return S


def build_incl():
    S = Sub("avg-inclusion-exclusion")
    S.notes = r"""### The situation
A group has an average. Then something happens: a person joins, a person leaves, one person is swapped for another, or a wrong value is found and corrected. The new average is given (or asked). The whole topic runs on one habit: **work with totals, not averages.**

### Someone joins
Old group: n members, average A. After one person joins, the average of the n + 1 members is B.
$$\text{Newcomer} = (n+1)B - nA = B + n(B - A)$$
Think of it in words: the newcomer must bring his own share B **plus** the rise $(B - A)$ for each of the n old members.
Example: 24 students average 15 years; with the teacher the average is 16. Teacher $= 16 + 24 \times 1 = 40$ years.

### Someone leaves
n members average A; one leaves and the remaining $n - 1$ average B.
$$\text{Leaver} = nA - (n-1)B$$
Example: 11 numbers average 36 (sum 396). After one is removed, 10 numbers average 34 (sum 340). Removed number $= 56$.
If the average **falls** when someone leaves, the leaver was above the old average; if it rises, the leaver was below it.

### Someone is replaced
The count stays n. Only the sum changes, and it changes by $n \times (\text{change in average})$.
$$\text{New person} = \text{Old person} + n \times (\text{change in average})$$
Example: the average weight of 8 people rises by 2.5 kg when a new person replaces one weighing 65 kg → new person $= 65 + 8 \times 2.5 = 85$ kg. If the average falls, subtract instead.
If two people are replaced, the pair's total changes by $n \times$ (change), so their average changes by that ÷ 2.

### Wrong value corrected
A value was copied wrongly (84 written as 48). The sum is off by the difference, so
$$\text{Correct average} = \text{Wrong average} + \frac{\text{correct} - \text{wrong}}{n}$$
30 students, average 62, with 84 read as 48: correct average $= 62 + \frac{36}{30} = 63.2$.
With two errors, add both corrections (with signs) before dividing.

### A group joins or leaves
k new members join n old ones and the average becomes B:
$$\text{Sum of newcomers} = (n+k)B - nA, \quad \text{their average} = \frac{(n+k)B - nA}{k}$$
30 students average 12 years; 10 join and the average becomes 13 → newcomers' sum $= 520 - 360 = 160$ → average 16 years.

### Checking your answer
Always verify with totals: new total ÷ new count must give the stated new average. Options are often built from forgetting to multiply the change by n, or multiplying by $n + 1$ in a replacement.

### Quick revision
- Join: newcomer $= B + n(B - A)$.
- Leave: leaver $= nA - (n-1)B$.
- Replace: new $=$ old $\pm n \times$ change.
- Wrong entry: average changes by (correct − wrong)/n.
- A group: work out the group's total from totals, then divide by its size.
"""

    S.pattern("avg-i1", "One member joins — find the newcomer's value", "very common",
        "A teacher, manager or new player joins a group; the average age/salary/weight goes up or down by a given amount.",
        r"x = B + n(B - A) = (n+1)B - nA",
        r"""1. Old total $= nA$; new total $= (n+1)B$.
2. Newcomer $=$ new total $-$ old total.
3. Shortcut: newcomer $= B + n \times$ (rise). If the average falls, the rise is negative.

Why: the newcomer supplies his own share and lifts every old member by the change.""",
        "The average age of 24 students is 15 years. Including the teacher, it becomes 16 years. Teacher's age?",
        r"$16 + 24 \times 1 = 40$ years. (Check: $25 \times 16 - 24 \times 15 = 400 - 360 = 40$.)")
    S.pattern("avg-i2", "One member leaves — find the removed value or the new average", "common",
        "'One number is excluded / a member leaves, the average of the rest becomes …'.",
        r"\text{removed} = nA - (n-1)B",
        r"""1. Old total $= nA$.
2. Remaining total $= (n-1)B$ (or old total − removed value, if the value is given).
3. Subtract to get the missing piece; divide if the new average is asked.

Why: removing a value only changes the sum and the count by known amounts.""",
        "The average of 11 numbers is 36. After removing one number, the average of the rest is 34. Find the removed number.",
        r"$11 \times 36 - 10 \times 34 = 396 - 340 = 56$.")
    S.pattern("avg-i3", "Replacement — one (or two) members swapped", "very common",
        "'A new man replaces one weighing 65 kg and the average increases by 2.5 kg' — the count does not change.",
        r"\text{new} = \text{old} \pm n \times d",
        r"""1. The count n stays the same.
2. Change in total $= n \times$ change in average.
3. New member $=$ old member $+$ that change (subtract if the average fell).

Why: only one value changed, so the whole change in the total belongs to it.""",
        "The average weight of 8 persons rises by 2.5 kg when a new person replaces one weighing 65 kg. Weight of the new person?",
        r"$65 + 8 \times 2.5 = 85$ kg.")
    S.pattern("avg-i4", "Wrongly recorded value corrected", "common",
        "'Later it was found that 84 was misread as 48' — the correct average is asked.",
        r"\text{correct avg} = \text{wrong avg} + \frac{\text{correct} - \text{wrong}}{n}",
        r"""1. For each error, find (correct value − wrong value), keeping the sign.
2. Add these corrections.
3. Divide by n and add to the wrong average.

Why: an error changes the total by exactly (correct − wrong) and nothing else.""",
        "The average of 30 marks was 62, but 84 was read as 48. The correct average is?",
        r"$62 + \frac{84 - 48}{30} = 62 + 1.2 = 63.2$.")
    S.pattern("avg-i5", "A group joins or leaves together", "common",
        "k new students join (or k leave / k are swapped) and the new average is given; the group's average is asked.",
        r"\text{group average} = \frac{(n+k)B - nA}{k}",
        r"""1. Old total $= nA$; new total $= (n+k)B$.
2. The difference is the joining group's total.
3. Divide by k for their average. For a swap of k members, total change $= n \times$ change.

Why: same total-bridge as a single member, just for k people at once.""",
        "30 students average 12 years. 10 new students join and the average becomes 13 years. Average age of the new students?",
        r"$40 \times 13 - 30 \times 12 = 160$ → $\frac{160}{10} = 16$ years.")

    t = 25 * 16 - 24 * 15
    assert t == 40
    S.q("avg-i1", "easy",
        "The average age of 24 students in a class is 15 years. When the teacher's age is included, the average becomes 16 years. The teacher's age is:",
        ["40 years", "39 years", "41 years", "31 years"], f"{t} years",
        r"New total $= 25 \times 16 = 400$; old total $= 24 \times 15 = 360$. Teacher $= 40$ years.",
        r"Teacher $= 16 + 24 \times 1 = 40$.", 30)
    m = 21 * 19500 - 20 * 18000
    assert m == 49500
    S.q("avg-i1", "medium",
        "The average monthly salary of 20 employees is ₹18,000. When the manager's salary is added, the average rises by ₹1,500. The manager's monthly salary is:",
        ["₹49,500", "₹48,000", "₹51,000", "₹30,000"], rs(m),
        r"""New average $= ₹19{,}500$ for 21 people → total $= ₹4{,}09{,}500$.
Old total $= 20 \times 18000 = ₹3{,}60{,}000$. Manager $= ₹49{,}500$.""",
        r"$19500 + 20 \times 1500 = ₹49{,}500$. (₹48,000 uses the OLD average as his own share.)", 40)
    r_ = 11 * 36 - 10 * 34
    assert r_ == 56
    S.q("avg-i2", "easy",
        "The average of 11 numbers is 36. If one number is removed, the average of the remaining numbers becomes 34. The number removed is:",
        ["56", "54", "58", "46"], str(r_),
        r"$11 \times 36 - 10 \times 34 = 396 - 340 = 56$.",
        r"Leaver $=$ new average $+ n \times$ fall $= 34 + 11 \times 2 = 56$.", 30)
    a = F(6 * 28 - 4, 5)
    assert a == F(328, 10)
    S.q("avg-i2", "medium",
        "The average age of a family of 6 members is 28 years. If the age of the youngest member, 4 years, is excluded, the average age of the remaining members is:",
        ["32.8 years", "32 years", "33.6 years", "27.33 years"], "32.8 years",
        r"Total $= 6 \times 28 = 168$. Without the youngest: $168 - 4 = 164$ for 5 members → $\frac{164}{5} = 32.8$ years.",
        None, 35)
    a2 = 28 - F(4, 6)
    assert a2 != a
    w = 65 + 8 * F(5, 2)
    assert w == 85
    S.q("avg-i3", "easy",
        "The average weight of 8 persons increases by 2.5 kg when a new person comes in place of one of them weighing 65 kg. The weight of the new person is:",
        ["85 kg", "82.5 kg", "87.5 kg", "75 kg"], "85 kg",
        r"Increase in total $= 8 \times 2.5 = 20$ kg. New person $= 65 + 20 = 85$ kg.", None, 25)
    nt = 48 - 12 * F(3, 2)
    assert nt == 30
    S.q("avg-i3", "medium",
        "When a teacher aged 48 years is replaced by a new teacher, the average age of the 12 teachers of a school decreases by 1.5 years. The age of the new teacher is:",
        ["30 years", "46.5 years", "36 years", "33 years"], "30 years",
        r"Fall in total $= 12 \times 1.5 = 18$ years. New teacher $= 48 - 18 = 30$ years.",
        "Average fell → the new person is younger by n × fall.", 30)
    pair = 12 + 18 + 5 * 3
    assert F(pair, 2) == F(45, 2)
    S.q("avg-i3", "hard",
        "The average of 5 numbers increases by 3 when two of them, 12 and 18, are replaced by two new numbers. The average of the two new numbers is:",
        ["22.5", "18", "45", "25.5"], num(F(pair, 2)),
        r"""Increase in total $= 5 \times 3 = 15$.
New pair's sum $= 12 + 18 + 15 = 45$ → average $= 22.5$.""",
        "18 comes from adding 3 to the old pair's average — the rise belongs to all 5 numbers.", 45)
    a = 62 + F(84 - 48, 30)
    assert a == F(632, 10)
    S.q("avg-i4", "medium",
        "The average marks of 30 students were found to be 62. Later it was discovered that a score of 84 had been wrongly entered as 48. The correct average is:",
        ["63.2", "60.8", "63.6", "62.4"], num(a),
        r"Correction to total $= 84 - 48 = +36$. Correct average $= 62 + \frac{36}{30} = 63.2$.", None, 35)
    a = F(50 * 36 + (48 - 23) + (36 - 60), 50)
    assert a == F(3602, 100)
    S.q("avg-i4", "hard",
        "The average of 50 observations was 36. It was later found that the observation 48 was wrongly taken as 23 and the observation 36 was wrongly taken as 60. The correct average is:",
        ["36.02", "36.98", "35.5", "36.5"], num(a),
        r"""Corrections: $48 - 23 = +25$ and $36 - 60 = -24$ → net $+1$.
Correct total $= 1800 + 1 = 1801$ → average $= 36.02$.""",
        "Adding both differences as +25 and +24 gives the trap 36.98.", 50)
    g = F(40 * 13 - 30 * 12, 10)
    assert g == 16
    S.q("avg-i5", "medium",
        "The average age of 30 students is 12 years. When 10 new students join, the average age becomes 13 years. The average age of the new students is:",
        ["16 years", "14 years", "13 years", "15 years"], "16 years",
        r"New total $= 40 \times 13 = 520$; old $= 360$. New students' total $= 160$ → average 16 years.",
        r"Each newcomer: $13 + \frac{30 \times 1}{10} = 16$.", 35)
    new_sum = 5 * 48 + 45 * (F(524, 10) - 52)
    assert new_sum / 5 == F(516, 10)
    S.q("avg-i5", "hard",
        "The average weight of 45 students is 52 kg. Five students whose average weight is 48 kg leave, and five new students join in their place. The average weight of the class becomes 52.4 kg. The average weight of the five new students is:",
        ["51.6 kg", "52.4 kg", "44.4 kg", "48.4 kg"], "51.6 kg",
        r"""The count stays 45, so the total rises by $45 \times 0.4 = 18$ kg.
Leavers' total $= 5 \times 48 = 240$ → joiners' total $= 240 + 18 = 258$ → average $= 51.6$ kg.""",
        r"$48 + \frac{45 \times 0.4}{5} = 48 + 3.6 = 51.6$ kg.", 55)
    return S
