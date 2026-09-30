"""Readable rewrite of the Average topic (all 4 subtopics).

Simple English, short sentences, totals-first method.
Every number shown on the page is recomputed below with exact fractions.
Run: python average.py  (patches content/core/topics/quant/average.json in place)
"""
import json
from fractions import Fraction as F
from pathlib import Path

ROOT = Path(__file__).resolve().parents[3]
TOPIC = ROOT / "core" / "topics" / "quant" / "average.json"


def apply(data, sub_id, concept, notes, formulas, tricks, mistakes, revision, patterns):
    sub = next(s for s in data["subtopics"] if s["id"] == sub_id)
    old_ids = {p["id"] for p in sub.get("patterns", [])}
    assert old_ids <= {p["id"] for p in patterns}, f"{sub_id}: never drop a pattern id"
    assert 2500 <= len(notes) <= 5000, (sub_id, len(notes))
    sub.update(concept=concept, notes=notes.strip() + "\n", formulas=formulas, tricks=tricks,
               mistakes=mistakes, revision=revision, patterns=patterns)


def pat(pid, name, freq, spot, formula, steps, why, q, ex_steps, answer):
    return {"id": pid, "name": name, "frequency": freq, "howToSpot": spot, "formula": formula,
            "steps": steps, "why": why, "example": {"q": q, "steps": ex_steps, "answer": answer}}


# =========================== avg-basics ===========================
# answer checks
assert 20 + 30 + 25 + 35 + 40 == 150 and F(150, 5) == 30                       # friends example
assert 4 * 25 == 100 and 100 - (20 + 30 + 18) == 32                            # notes: fourth number
assert 5 * 27 == 135 and 135 - (20 + 31 + 25 + 18) == 41                       # b1 example
assert 25 ** 2 == 625 and F(625, 25) == 25                                     # first 25 odd
assert sum(range(2, 61, 2)) == 930 and F(930, 30) == 31                        # first 30 even
assert F(11 * 21, 6) == F(77, 2) == F(385, 10)                                 # squares n=10 -> 38.5
assert (1 + 8) / 2 == 4.5 and F(2 * 9, 4) == F(9, 2)                          # cubes n=2 -> 4.5
assert 48 + 3 * 2 == 54                                                        # notes: largest even
assert 45 - 4 * 2 == 37                                                        # b3 example: smallest odd
assert F(6 + 96, 2) == 51                                                      # multiples of 6
assert 15 * 3 + 5 == 50                                                        # b4 old example
assert F(18 + 4, 2) == 11                                                      # b4 example
assert sum([-16, -9, -4, 2, 7]) == -20 and 300 + F(-20, 5) == 296              # assumed mean notes
assert sum([-4, 2, 7, 13, 17]) == 35 and 400 + F(35, 5) == 407                 # b5 example
assert 30 + 2 == 32                                                            # trick: 5 consecutive

b_concept = (
    "An average is one number that stands for a whole list: **average = sum ÷ count**. "
    "The exam-useful direction is the reverse: **sum = average × count**.\n\n"
    "Add k to every value and the average rises by k. Multiply every value by k and the average is "
    "multiplied by k.\n\n"
    "For lists with equal gaps (consecutive numbers, multiples of k) the average is the **middle term**. "
    "Standard lists have fixed averages: first n odd numbers average n, first n even numbers average n + 1."
)

b_notes = r"""### What an average is
An average is one number that stands for a whole list. It is what each one gets when the total is shared equally.

Five friends have ₹20, ₹30, ₹25, ₹35 and ₹40. Total = ₹150. Shared equally: $150 \div 5 = ₹30$. So the average is ₹30. Another name for it is the arithmetic mean.

> **Rule:** Average = sum of values ÷ number of values. Turn it around and you get the working tool: sum = average × count.

### The sum bridge
Most exam questions live on the turned-around form **sum = average × count**.

1. Change every average into a sum.
2. Add or subtract with the sums.
3. Divide again only at the last step.

> **Example:** The average of 4 numbers is 25, and three of them are 20, 30 and 18. Sum = $4 \times 25 = 100$. The known values add to 68. Fourth number = $100 - 68 = 32$.

### Properties that save time
- The average always sits between the smallest and the largest value.
- Add k to every value → the average rises by k. Subtract k → it falls by k.
- Multiply every value by k → the average gets multiplied by k. Divide → it gets divided by k.
- Apply changes in the order given: "× 3, then + 5" on an average of 15 gives $15 \times 3 + 5 = 50$.
- Each value's gap from the average (its deviation) adds up to zero across the whole list.

### Standard series averages
Learn this table by heart. Here n is the **count of terms**, not the last term.

| Series | Average |
|---|---|
| First n natural numbers | $\dfrac{n+1}{2}$ |
| First n odd numbers | $n$ |
| First n even numbers | $n+1$ |
| Squares of the first n naturals | $\dfrac{(n+1)(2n+1)}{6}$ |
| Cubes of the first n naturals | $\dfrac{n(n+1)^2}{4}$ |

> **Tip:** First 30 even numbers average $30 + 1 = 31$. First 25 odd numbers average 25. No adding needed.

### Numbers with equal gaps
Consecutive numbers, consecutive even or odd numbers, and multiples of k all climb by one fixed step. Their average is the **middle term**, which is also $\dfrac{\text{first} + \text{last}}{2}$.

> **Example:** 7 consecutive even numbers average 48. The middle (4th) number is 48. Step up by 2, three times: largest = $48 + 6 = 54$.

Multiples of 6 up to 100 run from 6 to 96. Average = $\dfrac{6 + 96}{2} = 51$.

### Close numbers: the assumed-mean method
To average numbers huddled close together, pick a round value nearby. Write each number's gap (+ or −) from it. Average the gaps. Add the result back.

284, 291, 296, 302, 307 sit around 300. Gaps: $-16, -9, -4, +2, +7$. Gap total = $-20$. Average gap = $-20 \div 5 = -4$. Average = $300 - 4 = 296$.

> **Tip:** This method replaces one big addition with small ones. Use it for lists of marks, weights or prices.
"""

b_formulas = [
    {"name": "Definition", "tex": r"\bar{x} = \frac{\sum x_i}{n} \iff \sum x_i = n\bar{x}", "note": "The sum form is the one you use."},
    {"name": "Shift property", "tex": r"\overline{x_i + k} = \bar{x} + k,\quad \overline{k\, x_i} = k\bar{x}", "note": "Adding k shifts the average by k; multiplying by k scales it."},
    {"name": "First n naturals / odd / even", "tex": r"\frac{n+1}{2},\quad n,\quad n+1", "note": "n = how many terms."},
    {"name": "Squares / cubes", "tex": r"\frac{(n+1)(2n+1)}{6},\quad \frac{n(n+1)^2}{4}"},
    {"name": "Equal gaps", "tex": r"\text{average} = \frac{\text{first} + \text{last}}{2} = \text{middle term}"},
]

b_tricks = [
    {
        "title": "Flip to the sum first",
        "body": "Never push averages around. Change them to sums, adjust, divide back at the end.",
        "example": {
            "q": "The average of 8 numbers is 32.5. Find their sum.",
            "steps": ["Sum = average × count.", r"Sum = $32.5 \times 8 = 260$."],
            "answer": "260",
        },
    },
    {
        "title": "Same operation on every value",
        "body": "Do to the average exactly what is done to each value, in the same order.",
        "example": {
            "q": "The average of 6 numbers is 15. Each number is multiplied by 3 and then increased by 5. Find the new average.",
            "steps": [r"Multiply first: $15 \times 3 = 45$.", r"Then add 5: $45 + 5 = 50$."],
            "answer": "50",
        },
    },
    {
        "title": "Equal gaps: jump from the middle",
        "body": "The average of evenly spaced numbers is the middle term. Step out from it instead of adding everything.",
        "example": {
            "q": "The average of 5 consecutive numbers is 30. Find the largest.",
            "steps": ["Middle (3rd) number = 30.", r"Largest = $30 + 2 = 32$."],
            "answer": "32",
        },
    },
]

b_mistakes = [
    {"wrong": "Giving a sum where the question asks for the average.", "right": "Read the last line: total or per-item value? Divide by the count before answering."},
    {"wrong": "Averaging two group averages of different sizes.", "right": "Only totals can be combined. Convert each group to size × average first."},
    {"wrong": r"Using the sum formula $\frac{n(n+1)}{2}$ and forgetting to divide by n.", "right": "The formula gives the sum. The average is the sum ÷ n."},
    {"wrong": "Applying just one of two ordered operations (× 3 then + 5).", "right": "Apply both, in the stated order: $15 \times 3 + 5 = 50$."},
    {"wrong": "Stepping by 1 when the list is of consecutive even or odd numbers.", "right": "Consecutive even or odd numbers step by 2. Use the gap of the series."},
]

b_revision = [
    "Sum = average × count. Work in sums, divide at the end.",
    "Every value + k → average + k; every value × k → average × k.",
    "Equal gaps → average = middle term = (first + last)/2.",
    r"First n naturals $\frac{n+1}{2}$; first n odd $n$; first n even $n+1$.",
    r"Squares $\frac{(n+1)(2n+1)}{6}$; cubes $\frac{n(n+1)^2}{4}$.",
    "Close numbers → assumed mean + average of the gaps.",
]

b_patterns = [
    pat("avg-b1", "Sum from average / one missing value", "very common",
        "An average and a count are given. The total is asked, or one value is missing from a list of known values.",
        r"\text{Sum} = \text{Average} \times n",
        ["Multiply the average by the count to get the sum.", "Add up the values you already know.", "Subtract: what is left is the missing value (or the asked total)."],
        "The average is only the sum shared equally, so the sum carries all the information.",
        "The average of 5 numbers is 27. Four of them are 20, 31, 25 and 18. Find the fifth number.",
        [r"Sum = $5 \times 27 = 135$.", r"Known values add to $20 + 31 + 25 + 18 = 94$.", r"Fifth number = $135 - 94 = 41$."],
        "41"),
    pat("avg-b2", "Average of standard series", "very common",
        "'Find the average of the first n natural / odd / even numbers', or of their squares or cubes.",
        r"\frac{n+1}{2},\quad n,\quad n+1,\quad \frac{(n+1)(2n+1)}{6},\quad \frac{n(n+1)^2}{4}",
        ["Spot the series and n, the count of terms.", "Take the average straight from the table.", "For even numbers ending at 2n, n is half the last term."],
        "Each table value is the series-sum formula already divided by n.",
        "Find the average of the first 30 even natural numbers.",
        [r"Series: even numbers. Average = $n + 1$.", r"$n = 30$, so the average is $30 + 1 = 31$.", r"Check: sum $= 930$, and $930 \div 30 = 31$."],
        "31"),
    pat("avg-b3", "Consecutive numbers and equal gaps", "very common",
        "'The average of 7 consecutive even numbers is 48 — find the largest', or the average of the multiples of k in a range.",
        r"\text{Average} = \text{middle term} = \frac{\text{first} + \text{last}}{2}",
        ["Place the average at the middle term of the list.", "Step out from the middle by the gap (1 for consecutive, 2 for even/odd, k for multiples).", "For a range of multiples, use (first + last) ÷ 2."],
        "Equal gaps balance on both sides of the middle, so the middle term is the mean.",
        "The average of 9 consecutive odd numbers is 45. Find the smallest of them.",
        ["Middle (5th) number = 45.", r"Step down by 2, four times: $45 - 8 = 37$."],
        "37"),
    pat("avg-b4", "Same operation on every value", "common",
        "'Each number is multiplied by 4 / increased by 6 / divided by 2' — the new average is asked.",
        r"\text{new average} = k \times A + c \quad (\text{same order as stated})",
        ["Do to the old average exactly what is done to each value.", "Keep the stated order of operations.", "Addition shifts the average; multiplication scales it."],
        "A uniform change moves the sum and the average exactly the way it moves each single value.",
        "The average of 7 numbers is 18. Each number is increased by 4 and then divided by 2. Find the new average.",
        [r"Increase: $18 + 4 = 22$.", r"Divide: $22 \div 2 = 11$."],
        "11"),
    pat("avg-b5", "Assumed mean (deviation method)", "common",
        "A short list of 4-8 close numbers (weights, marks, runs) is given and their average is asked.",
        r"\text{Average} = \text{assumed value} + \frac{\text{sum of deviations}}{n}",
        ["Pick a round number near the middle.", "Write each value's gap from it, with a + or − sign.", "Add the gaps and divide by n.", "Add the result to the assumed value."],
        "Shifting every value by the same amount shifts the average by that amount.",
        "Find the average of 396, 402, 407, 413 and 417.",
        ["Assume 400. Gaps: $-4, +2, +7, +13, +17$.", r"Gap total = $35$; average gap = $35 \div 5 = 7$.", r"Average = $400 + 7 = 407$."],
        "407"),
]

# ====================== avg-inclusion-exclusion ======================
# answer checks
assert 25 * 16 - 24 * 15 == 40 and 16 + 24 * 1 == 40                          # i1 + notes
assert 31 * 15 - 30 * 14 == 45 and 15 + 30 * 1 == 45                          # trick: teacher
assert 11 * 36 - 10 * 34 == 396 - 340 == 56                                   # notes leaver
assert 12 * 40 - 11 * 38 == 480 - 418 == 62                                   # i2 example
assert 65 + 8 * F(5, 2) == 85                                                 # notes replacement
assert 78 - 9 * 2 == 60                                                       # i3 example
assert 9 * 27 - 8 * 25 == 243 - 200 == 43                                     # trick: exclusion
assert 62 + F(84 - 48, 30) == F(316, 5) == F(3160, 50)                        # i4 notes 63.2
assert 48 + F(72 - 27, 25) == F(249, 5)                                       # i4 example 49.8
assert 40 * 13 - 30 * 12 == 520 - 360 == 160 and F(160, 10) == 16             # i5 + notes

i_concept = (
    "When a member joins or leaves and the average changes, work with **totals**, not averages.\n\n"
    "- Join: newcomer = new average + n × rise, with n the OLD count.\n"
    "- Leave: leaver = old total − new total of the rest.\n"
    "- Replace: new value = old value + n × (change in average). The count does not change.\n\n"
    "A wrongly copied value shifts the total by (correct − wrong), so the average shifts by that ÷ n."
)

i_notes = r"""### The habit: work with totals
A group has an average. Then one member joins, leaves, or is swapped out, and the average changes. Averages cannot be added or removed. Totals can.

1. Old total = old count × old average.
2. New total = new count × new average.
3. The joining or leaving value is the difference of the two totals.

> **Rule:** Never move an average. Move the total (count × average), then divide at the end.

### Someone joins
n members average A. One person joins, and the n + 1 members average B.

$$\text{newcomer} = (n+1)B - nA = B + n(B - A)$$

In words: the newcomer carries his own share B, plus the rise $B - A$ for each of the n old members.

> **Example:** 24 students average 15 years. With the teacher included, the average becomes 16. Teacher = $16 + 24 \times 1 = 40$ years. Check: $25 \times 16 - 24 \times 15 = 40$.

### Someone leaves
n members average A. One leaves, and the remaining $n-1$ average B.

$$\text{leaver} = nA - (n-1)B$$

11 numbers average 36, so the sum is 396. One number is removed; the other 10 average 34, sum 340. Removed number = $396 - 340 = 56$.

> **Watch:** If the average falls after someone leaves, the leaver was above the old average. If it rises, the leaver was below it.

### Someone is replaced
The count stays n. Only the total changes, and it changes by $n \times$ (change in average).

$$\text{new value} = \text{old value} + n \times (\text{change in average})$$

The average weight of 8 people rises by 2.5 kg when one person is replaced. The old person weighed 65 kg. New person = $65 + 8 \times 2.5 = 85$ kg. If the average falls, subtract instead. If TWO members are replaced, their pair's total changes by $n \times$ change — split it between them as the question directs.

### A wrong entry is found
A value was copied wrongly — say 84 was read as 48. The total is off by exactly (correct − wrong).

$$\text{correct average} = \text{wrong average} + \frac{\text{correct} - \text{wrong}}{n}$$

30 students average 62 marks, with 84 read as 48. Correct average = $62 + \dfrac{36}{30} = 63.2$. With two errors, add both corrections, with their signs, before dividing.

### A whole group joins
k new members join n old ones, and the average becomes B.

$$\text{group total} = (n+k)B - nA, \qquad \text{group average} = \frac{(n+k)B - nA}{k}$$

30 students average 12 years. Ten new students join and the average becomes 13. Newcomers' total = $40 \times 13 - 30 \times 12 = 160$. Their average = $160 \div 10 = 16$ years. If k members LEAVE instead, their total = $nA - (n-k)B$ — the same bridge, walked the other way.

> **Tip:** Check every answer: new total ÷ new count must equal the stated new average.
"""

i_formulas = [
    {"name": "Joining member", "tex": r"\text{value} = A' + n(A' - A)", "note": "n = old count; A' = new average."},
    {"name": "Leaving member", "tex": r"\text{value} = A' + n(A - A')", "note": "A' = average of the remaining n members."},
    {"name": "Replacement", "tex": r"\text{new} = \text{old} + n(A' - A)", "note": "The count does not change."},
    {"name": "Count change both ways", "tex": r"\text{total of newcomers} = \text{new total} - \text{old total}"},
]

i_tricks = [
    {
        "title": "Joining: own share plus extras",
        "body": "New value = new average + (old count) × (average jump).",
        "example": {
            "q": "The average age of 30 students is 14 years. Their teacher joins them and the average becomes 15 years. Find the teacher's age.",
            "steps": [r"Jump in average = $15 - 14 = 1$ year.", r"Teacher = $15 + 30 \times 1 = 45$ years.", r"Check: $31 \times 15 - 30 \times 14 = 465 - 420 = 45$."],
            "answer": "45 years",
        },
    },
    {
        "title": "Replacement: the jump times n",
        "body": "Only the swapped item changes the sum, and it changes by n × (average jump).",
        "example": {
            "q": "The average of 8 numbers is 24. If 20 is replaced by 44, find the new average.",
            "steps": [r"Sum rises by $44 - 20 = 24$.", r"Jump = $24 \div 8 = 3$.", r"New average = $24 + 3 = 27$."],
            "answer": "27",
        },
    },
    {
        "title": "Exclusion: subtract the totals",
        "body": "Old total − (new count × new average) = the removed value.",
        "example": {
            "q": "The average of 9 numbers is 27. One number is excluded and the average of the rest becomes 25. Find the excluded number.",
            "steps": [r"Old total = $9 \times 27 = 243$.", r"New total = $8 \times 25 = 200$.", r"Excluded = $243 - 200 = 43$."],
            "answer": "43",
        },
    },
]

i_mistakes = [
    {"wrong": "Using the old average where the new one belongs.", "right": "Label both averages first: A old, B new. The formula reads off B for shares."},
    {"wrong": "Counting the newcomer inside n.", "right": "In the joining formula, n is the count BEFORE the newcomer arrives."},
    {"wrong": "For a replacement, changing the new number by just the average jump.", "right": "The swap changes the total by n × jump, so the new value moves by n × jump."},
    {"wrong": "Subtracting when the average rises (or adding when it falls).", "right": "Fix the sign from the story: rise = plus, fall = minus, for joiners and replacements alike."},
    {"wrong": "Correcting a wrong entry by editing the average directly.", "right": "Adjust the total by (correct − wrong), then divide by n."},
]

i_revision = [
    r"Join: newcomer $= B + n(B - A)$, n = old count.",
    r"Leave: leaver $= nA - (n-1)B$.",
    "Replace: new = old ± n × (change in average).",
    "Wrong entry: average shifts by (correct − wrong) ÷ n.",
    "Group joins: group total = (n+k)B − nA, then ÷ k for their average.",
    "Check: new total ÷ new count = stated new average.",
]

i_patterns = [
    pat("avg-i1", "One member joins — find the newcomer", "very common",
        "A teacher, manager or new player joins a group and the average age, salary or weight moves by a given amount.",
        r"x = B + n(B - A) = (n+1)B - nA",
        ["Write the old total nA and the new total (n+1)B.", "Subtract: the newcomer is the difference.", "Shortcut: newcomer = B + n × rise. If the average falls, the rise is negative."],
        "The newcomer supplies his own share and lifts every old member by the change.",
        "The average age of 24 students is 15 years. Including their teacher, it becomes 16 years. Find the teacher's age.",
        [r"Newcomer = $16 + 24 \times 1$.", r"= $40$ years.", r"Check: $25 \times 16 - 24 \times 15 = 400 - 360 = 40$."],
        "40 years"),
    pat("avg-i2", "One member leaves — the removed value", "common",
        "'One number is excluded / one member leaves, and the average of the rest becomes …'.",
        r"\text{removed} = nA - (n-1)B",
        ["Old total = nA.", "Remaining total = (n − 1)B.", "Subtract the two totals; divide later only if the new average is asked instead."],
        "Removing one value changes the sum and the count by known amounts, and nothing else.",
        "The average of 12 numbers is 40. One number is removed and the average of the remaining numbers is 38. Find the removed number.",
        [r"Old total = $12 \times 40 = 480$.", r"New total = $11 \times 38 = 418$.", r"Removed = $480 - 418 = 62$."],
        "62"),
    pat("avg-i3", "One member is replaced", "very common",
        "'A new man replaces one weighing 65 kg and the average increases by 2.5 kg.' The count does not change.",
        r"\text{new} = \text{old} \pm n \times d",
        ["Keep the count n the same.", "Change in total = n × change in average.", "New member = old member + that change (subtract if the average fell)."],
        "Only one value changed, so the whole change in the total belongs to it.",
        "The average weight of 9 persons falls by 2 kg when a person weighing 78 kg is replaced by a newcomer. Find the newcomer's weight.",
        [r"Total falls by $9 \times 2 = 18$ kg.", r"Newcomer = $78 - 18 = 60$ kg."],
        "60 kg"),
    pat("avg-i4", "A wrongly recorded value is corrected", "common",
        "'Later it was found that 84 had been misread as 48.' The correct average is asked.",
        r"\text{correct avg} = \text{wrong avg} + \frac{\text{correct} - \text{wrong}}{n}",
        ["For each error, work out (correct value − wrong value), keeping the sign.", "Add the corrections.", "Divide by n and add to the wrong average."],
        "An error changes the total by exactly (correct − wrong) and nothing else.",
        "The average of 25 marks was calculated as 48. Later, 72 was found to have been misread as 27. Find the correct average.",
        [r"Correction = $72 - 27 = 45$.", r"Shift = $45 \div 25 = 1.8$.", r"Correct average = $48 + 1.8 = 49.8$."],
        "49.8"),
    pat("avg-i5", "A whole group joins or leaves", "common",
        "k new students join (or k leave), the new overall average is given, and the group's own average is asked.",
        r"\text{group average} = \frac{(n+k)B - nA}{k}",
        ["Old total = nA; new total = (n + k)B.", "The difference is the joining group's total.", "Divide by k for their average. For a swap of k members, the total changes by n × change."],
        "The same total bridge as for a single member, taken k people at once.",
        "30 students have an average age of 12 years. 10 new students join and the average becomes 13 years. Find the average age of the new students.",
        [r"New total = $40 \times 13 = 520$; old total = $30 \times 12 = 360$.", r"Newcomers' total = $520 - 360 = 160$.", r"Their average = $160 \div 10 = 16$ years."],
        "16 years"),
]

# =========================== avg-weighted ===========================
# answer checks
assert F(20 * 60 + 80 * 40, 100) == 44                                        # notes: sections
assert F(30 * 42 + 20 * 37, 50) == F(2000, 50) == 40                          # w1
assert 40 * 65 == 2600 and 25 * 62 == 1550 and F(2600 - 1550, 15) == 70       # w2
assert (58 - 52, 62 - 58) == (6, 4) and F(6, 4) == F(3, 2)                    # w3
assert F(3 * 150 + 2 * 140, 5) == 146                                         # w4
assert (8000 - 6000, 12000 - 8000) == (2000, 4000) and F(2000, 4000) == F(1, 2)  # w5 arms
assert 7 * 12000 + 14 * 6000 == 84000 + 84000 == 21 * 8000                    # w5 check
assert 4 * 60 == 240 and F(240 - 72, 3) == 56                                 # notes: fraction sizes
assert 60 * 50 - 20 * 40 == 3000 - 800 == 2200 and F(2200, 40) == 55          # trick 1
assert F(20 * 12 + 30 * 11, 50) == F(570, 50) == F(57, 5)                     # trick 2: 11.4
assert 300 + 15 * 50 == 1050                                                  # trick 3

w_concept = (
    "When groups of different sizes are combined, the combined average is the **weighted** mean:\n\n"
    "total of all values ÷ total count. Turn each group's average into a total (size × average) first.\n\n"
    "The combined average always sits closer to the bigger group's average. With equal group sizes it is "
    "the plain middle of the two averages.\n\n"
    "With two group averages and the combined average known, the group sizes sit in the reverse ratio of "
    "their distances from the combined average."
)

w_notes = r"""### Why averaging averages fails
Section A has 20 students with average 60. Section B has 80 students with average 40. The middle of 60 and 40 is 50, but the real class average is $\dfrac{20 \times 60 + 80 \times 40}{100} = 44$.

The bigger section pulls the answer towards its own average. So each group must be weighted by its size.

> **Rule:** Combined average = (sum of all group totals) ÷ (sum of all sizes). A group total = size × its average.

### The weighted-average method
Work in three moves, every time.

1. Total of each group = size × average.
2. Add all the totals. Add all the sizes.
3. Divide.

> **Example:** 30 boys average 42 kg and 20 girls average 37 kg. Combined = $\dfrac{1260 + 740}{50} = 40$ kg.

### Where the combined average sits
Three facts that kill wrong options without calculation:

- It always lies between the smallest and the largest group average.
- It lies closer to the average of the **bigger** group.
- Equal group sizes → it is the plain middle of the group averages.

> **Tip:** If an option sits outside the two group averages, cross it out at once.

### One group's average missing
Class of 40 averages 65 marks. The 25 boys average 62. Find the girls' average.

Class total = $40 \times 65 = 2600$. Boys' total = $25 \times 62 = 1550$. Girls' total = $2600 - 1550 = 1050$ over 15 girls → 70.

> **Rule:** Missing total = overall total − known totals. Then divide by that group's own size.

### Finding the sizes: the balance method
Both group averages and the combined average are known; a size is asked. The sizes sit in the **reverse** ratio of the distances from the combined average:

$$\frac{n_1}{n_2} = \frac{\bar{x}_2 - \bar{x}}{\bar{x} - \bar{x}_1}$$

Class average 58, boys 62, girls 52. Distances: boys 4, girls 6. So boys : girls = $6 : 4 = 3 : 2$.

Picture a see-saw: the heavier group sits closer to the balance point. Scale the ratio up to the given total when a count is asked.

> **Watch:** The group closer to the combined average is the bigger one. Reversing this ratio is the classic wrong option.

### Sizes given as a ratio or a fraction
No real counts? Use the ratio parts as the counts.

Boys : girls = 3 : 2, averages 150 cm and 140 cm → $\dfrac{3 \times 150 + 2 \times 140}{5} = 146$ cm.

"One-fourth of a class averages 72 and the whole class averages 60." Take the class as 4 parts: $4 \times 60 = 240 = 72 + 3x$, so the other three parts average $x = 56$.

> **Tip:** The weighted average depends only on the proportions, never on the actual headcount.
"""

w_formulas = [
    {"name": "Weighted mean", "tex": r"\bar{x} = \frac{\sum n_i \bar{x}_i}{\sum n_i}"},
    {"name": "Missing group average", "tex": r"\bar{x}_2 = \frac{N\bar{x} - n_1\bar{x}_1}{n_2}", "note": "N = total count, overall average known."},
    {"name": "Sizes from distances", "tex": r"\frac{n_1}{n_2} = \frac{\bar{x}_2 - \bar{x}}{\bar{x} - \bar{x}_1}", "note": "Reverse ratio of the distances."},
]

w_tricks = [
    {
        "title": "Totals, not averages",
        "body": "Turn each group into a total, add, divide by the combined count.",
        "example": {
            "q": "In a class of 60 students, the 20 girls average 40 marks. The class average is 50. Find the boys' average.",
            "steps": [r"Class total = $60 \times 50 = 3000$; girls = $20 \times 40 = 800$.", r"Boys' total = $3000 - 800 = 2200$ over 40 boys.", r"Boys' average = $2200 \div 40 = 55$."],
            "answer": "55",
        },
    },
    {
        "title": "Feel the balance point",
        "body": "The combined average splits the gap between the group averages in the ratio n₂ : n₁, the reverse of the sizes.",
        "example": {
            "q": "20 boys average 12 years and 30 girls average 11 years. Find the combined average age.",
            "steps": [r"Totals: $240 + 330 = 570$.", r"Combined = $570 \div 50 = 11.4$ years.", "The answer sits 0.4 above 11 and 0.6 below 12 — closer to the girls, the bigger group."],
            "answer": "11.4 years",
        },
    },
    {
        "title": "One newcomer is a tiny second group",
        "body": "A single new member changing a group average is just a weighted average with k = 1. Use value = B + n(B − A).",
        "example": {
            "q": "15 workers average ₹250 in daily wages. A manager joins and the average becomes ₹300. Find the manager's wage.",
            "steps": [r"Jump = $300 - 250 = 50$.", r"Manager = $300 + 15 \times 50$.", r"= ₹1050."],
            "answer": "₹1,050",
        },
    },
]

w_mistakes = [
    {"wrong": "Averaging the two averages when the groups differ in size.", "right": "Weight each average by its group size: (n₁x̄₁ + n₂x̄₂) ÷ (n₁ + n₂)."},
    {"wrong": "Dividing by the wrong count (students + teacher, workers + manager).", "right": "List every member of the combined group before dividing."},
    {"wrong": "Reading the balance ratio forwards (closer group = smaller).", "right": "The group closer to the combined average is the bigger one."},
    {"wrong": "Rounding a total halfway through.", "right": "These questions come out exact. A messy decimal mid-way means a slip, so recheck the totals."},
    {"wrong": "Group averages that do not bracket the combined average.", "right": "The combined average must sit between the group averages. If not, re-read the question."},
]

w_revision = [
    "Combined average = sum of (size × average) ÷ sum of sizes.",
    "Missing group: overall total − known totals, then ÷ its own size.",
    "Sizes = reverse ratio of distances from the combined average.",
    "Ratio or fraction given → use the parts as counts.",
    "Combined average sits closer to the bigger group.",
]

w_patterns = [
    pat("avg-w1", "Combined average of two or more groups", "very common",
        "Two or three groups (boys/girls, sections, batches) with sizes and averages; the overall average is asked.",
        r"\bar{x} = \frac{n_1 \bar{x}_1 + n_2 \bar{x}_2 + n_3 \bar{x}_3}{n_1 + n_2 + n_3}",
        ["Multiply each group's size by its average to get its total.", "Add all the totals; add all the sizes.", "Divide. The answer must lie closer to the bigger group's average."],
        "An average is a total shared by a count, so only totals can be added.",
        "In a school, 30 boys average 42 kg and 20 girls average 37 kg. Find the average weight of all 50 students.",
        [r"Boys: $30 \times 42 = 1260$; girls: $20 \times 37 = 740$.", r"Total = $2000$ kg over 50 students.", r"Average = $2000 \div 50 = 40$ kg."],
        "40 kg"),
    pat("avg-w2", "Missing average of one group", "very common",
        "The overall average and one group's average are given; the other group's average is asked.",
        r"\bar{x}_2 = \frac{(n_1 + n_2)\bar{x} - n_1 \bar{x}_1}{n_2}",
        ["Overall total = total count × overall average.", "Subtract the known group's total.", "Divide the rest by the other group's size."],
        "The two group totals must add up to the overall total.",
        "The average marks of 40 students is 65. The 25 boys average 62 marks. Find the girls' average.",
        [r"Class total = $40 \times 65 = 2600$.", r"Boys = $25 \times 62 = 1550$, so girls have $1050$ marks.", r"Girls: $1050 \div 15 = 70$."],
        "70"),
    pat("avg-w3", "Group ratio from the averages", "common",
        "All three averages are known (two groups plus combined) and the ratio of sizes is asked.",
        r"n_1 : n_2 = (\bar{x}_2 - \bar{x}) : (\bar{x} - \bar{x}_1)",
        ["Find how far each group average is from the combined average.", "The sizes are in the reverse ratio of these distances.", "Scale the ratio to the given total if a count is asked."],
        "The surplus above the mean from one group must balance the shortfall from the other.",
        "A class averages 58 marks. The boys average 62 and the girls 52. Find boys : girls.",
        ["Distances: boys $62 - 58 = 4$; girls $58 - 52 = 6$.", "Sizes are the reverse: boys : girls = $6 : 4 = 3 : 2$."],
        "3 : 2"),
    pat("avg-w4", "Sizes given as a ratio or fraction", "common",
        "'Boys and girls are in the ratio 3 : 2' or 'one-fourth of the students average …' instead of real counts.",
        r"\bar{x} = \frac{a\bar{x}_1 + b\bar{x}_2}{a + b}",
        ["Use the ratio parts (or fraction parts) as if they were the counts.", "Apply the weighted-average formula.", "For a missing average, solve the one equation that is left."],
        "The weighted average depends only on the proportions of the groups.",
        "Boys and girls in a class are in the ratio 3 : 2. Boys average 150 cm in height and girls 140 cm. Find the average height of the class.",
        [r"Take 3 parts of boys and 2 of girls.", r"Total height = $3 \times 150 + 2 \times 140 = 730$ per 5 parts.", r"Average = $730 \div 5 = 146$ cm."],
        "146 cm"),
    pat("avg-w5", "A group count from the averages", "common",
        "The overall average and both group averages are known, one group's count is known, and the other count (or total) is asked.",
        r"n_1 : n_2 = (\bar{x} - \bar{x}_2) : (\bar{x}_1 - \bar{x})",
        ["Find the two distances from the overall average.", "The sizes follow the reverse ratio; pair each size with the group on the far side.", "Scale the ratio by the known group's count, then add for the total."],
        "Once the size ratio is fixed, the known count prices one part of it.",
        "A firm pays an average salary of ₹8,000. Its 7 technicians earn ₹12,000 each and the rest earn ₹6,000 each. How many employees does the firm have in total?",
        [r"Distances from 8000: technicians $+4000$, others $-2000$.", r"Size ratio technicians : others = $2000 : 4000 = 1 : 2$.", r"Others = $7 \times 2 = 14$; total = $7 + 14 = 21$."],
        "21 employees"),
]

# ============================= avg-misc =============================
# answer checks
assert 98 - 19 * 2 == 60 and 19 * 58 + 98 == 1200 == 20 * 60                  # m1 + notes
assert 11 * 45 - 10 * 42 == 495 - 420 == 75                                   # notes: needed runs
assert 87 - 16 * 3 == 39 and 16 * 36 + 87 == 663 == 17 * 39                   # trick 1
assert F(62, 5) * 85 + 26 == 1080 and 12 * (85 + 5) == 1080                   # m5 + notes
assert 3 * 37 == 111 and 3 * 34 == 102 and 40 + 102 - 111 == 31               # trick 2 overlap days
assert 7 * 27 == 189 and 7 * 35 == 245 and 13 * 30 == 390                     # m2
assert 189 + 245 - 390 == 44                                                  # 7th number
assert 6 * 30 == 180 and 180 - 2 * 24 - 2 * 33 == 66 and 31 + 35 == 66        # m3
assert 5 * 24 == 120 and 120 - 5 * 8 == 80 and F(80, 4) == 20                 # m4
assert 160 - 31 - 64 == 65 and 3 * 16 + 17 == 65 and 16 + 12 == 28            # trick 3 split set

m_concept = (
    "**Batsman template:** a score of x in the nth innings lifts the average by d. The new average is "
    "$x - (n-1)d$; the score itself was (new total) − (old total).\n\n"
    "**Overlapping windows:** averages over two overlapping stretches differ only at their ends. "
    "Thu − Mon = 3 × (difference of the averages) for three-day windows.\n\n"
    "**Split sets and ages:** turn every average into a sum, use one variable for the unknown part, and "
    "remember a fixed group's average age rises by 1 each year."
)

m_notes = r"""### Batsman: the innings question
A batsman's average = total runs ÷ innings played. The standard question: he scores x runs in his nth innings and the average rises by d. Let the new average be A. Then:

$$(n-1)(A - d) + x = nA \quad\Rightarrow\quad A = x - (n-1)d$$

98 runs in the 20th innings lift the average by 2 → new average = $98 - 19 \times 2 = 60$.

> **Rule:** Score in the nth innings = new average + (n − 1) × rise. It must feed every past innings plus its own share.

The reverse question asks how many runs are needed. To lift an average from 42 to 45 in the 11th innings: needed = $11 \times 45 - 10 \times 42 = 75$.

### Bowler's average
A bowler's average = runs given ÷ wickets taken, and a LOWER value is better. Average a, then a match of w wickets for r runs makes it fall by d. With W wickets before the match:

$$aW + r = (a - d)(W + w)$$

Average 12.4; a match of 5 wickets for 26 runs improves it by 0.4 → $12.4W + 26 = 12(W + 5)$, so $W = 85$.

> **Watch:** "Improves" means the bowling average falls. Subtract, never add.

### Overlapping windows
The average of Mon–Wed is 37 and of Tue–Thu is 34. The two sums share Tue and Wed, so subtracting kills them:

$$\text{Thu} - \text{Mon} = 3 \times (34 - 37) = -9$$

Mon was 40°, so Thu = $40 - 9 = 31$°. Multiply the difference of averages by the length of the overlap.

### First-k and last-k share a middle
13 numbers average 30. The first 7 average 27 and the last 7 average 35. The 7th number sits in both halves, so it is counted twice:

$$\text{middle} = 7 \times 27 + 7 \times 35 - 13 \times 30 = 189 + 245 - 390 = 44$$

> **Tip:** Add the two part-sums and subtract the whole. What survives is the shared item.

### Split sets with relations
"The average of 6 numbers is 30. The first two average 24, the next two 33. Of the last two, one is 4 more than the other."

Sums first: total 180, first pair 48, second pair 66, so the last pair totals 66. Name the smaller x: $x + (x + 4) = 66$, so 31 and 35.

> **Rule:** Every average becomes a sum. Name ONE unknown x and write the rest in terms of it.

### Ages move together
Every member of a fixed group gets one year older each year, so the average age also rises by 1 per year.

- n years ago the group's average was A → today it is $A + n$ (same members).
- At the birth of the youngest: subtract the youngest's age from every member, and drop the youngest from the count. Five members average 24, youngest 8 → $\dfrac{120 - 5 \times 8}{4} = 20$.

> **Tip:** Rebuild the story with totals — old total, change, new total, new count. If new total ÷ new count misses the stated average, a step is wrong.
"""

m_formulas = [
    {"name": "Batsman score", "tex": r"\text{score} = A' + (n-1)d", "note": "A' = new average, d = rise."},
    {"name": "Batsman new average", "tex": r"A' = \frac{(n-1)A + \text{score}}{n} = x - (n-1)d"},
    {"name": "Overlap subtraction", "tex": r"\text{Thu} - \text{Mon} = 3(b - a)", "note": "Three-day windows; multiply by the overlap length."},
    {"name": "Shared middle item", "tex": r"\text{shared} = S_1 + S_2 - S_{\text{total}}"},
    {"name": "Split sums", "tex": r"n\bar{x} = \sum_{\text{chunks}} (\text{chunk total})", "note": "One equation per chunk."},
]

m_tricks = [
    {
        "title": "Batsman: stay in totals",
        "body": "Old total + new score = new count × new average.",
        "example": {
            "q": "A batsman scores 87 in his 17th innings and raises his average by 3. Find his average after the 17th innings.",
            "steps": [r"Let the new average be $A$: $17A = 16(A - 3) + 87$.", r"$17A = 16A + 39$, so $A = 39$."],
            "answer": "39",
        },
    },
    {
        "title": "Overlaps: subtract the sums",
        "body": "Shared days cancel, leaving only the difference of the end days.",
        "example": {
            "q": "The average temperature of Mon, Tue and Wed is 37°C; of Tue, Wed and Thu it is 34°C. If Monday was 40°C, find Thursday.",
            "steps": [r"Sums: $3 \times 37 = 111$ and $3 \times 34 = 102$.", r"Thu − Mon = $102 - 111 = -9$.", r"Thu = $40 - 9 = 31$°C."],
            "answer": "31°C",
        },
    },
    {
        "title": "One variable for the unknown chunk",
        "body": "Name the smallest unknown x, express the rest through it, and close the equation with the leftover sum.",
        "example": {
            "q": r"8 numbers average 20. The first two average 15.5 and the next three average $\dfrac{64}{3}$. The 6th number is 5 less than the 7th, and the 8th is 7 more than the 7th. Find the 8th number.",
            "steps": [r"Total = $160$; known chunks = $31 + 64 = 95$; leftover = $65$.", r"Let the 6th be $x$: $x + (x+5) + (x+12) = 65$.", r"$x = 16$, so the 8th = $16 + 12 = 28$."],
            "answer": "28",
        },
    },
]

m_mistakes = [
    {"wrong": "In batsman questions, multiplying by n for the old total.", "right": "Before the nth innings there are only n − 1 innings. Old total = (n − 1) × old average."},
    {"wrong": "Reporting the difference of two overlapping averages as the end-day difference.", "right": "Multiply the difference of averages by the overlap length (3 days → × 3)."},
    {"wrong": "Forgetting the two halves of 11 numbers share the 6th number.", "right": "First 6 + last 6 = 12 counts for 11 numbers: the middle one is counted twice."},
    {"wrong": "Setting a relation backwards ('the 6th is 5 less than the 7th').", "right": "Translate carefully: 6th = 7th − 5, so 7th = 6th + 5."},
    {"wrong": "Treating a bowling average like a batsman average (higher = better).", "right": "A bowler improves when the average falls. Use $aW + r = (a-d)(W+w)$."},
]

m_revision = [
    "Batsman: new average = x − (n − 1)d; needed runs = new total − old total.",
    "Bowler: aW + r = (a − d)(W + w); 'improves' means falls.",
    "Overlap: end difference = overlap length × difference of averages.",
    "First-k and last-k: shared middle = part sums − whole sum.",
    "Split set: sums first, then one variable x.",
    "Fixed group: average age +1 per year; at a birth, subtract that age from everyone.",
]

m_patterns = [
    pat("avg-m1", "Batsman: the innings that moves the average", "very common",
        "'Scores x in his nth innings and raises his average by d', or 'how many runs in the next innings to reach a target average'.",
        r"A_{\text{new}} = x - (n-1)d, \qquad \text{needed} = (n+1)A' - nA",
        ["Write old total = (n − 1)(A − d) and new total = nA for the new average A.", "Solve for A, or subtract old total from target total when runs needed are asked.", "Check with the totals."],
        "The new score must lift every earlier innings by d and still leave its own share A.",
        "A batsman scores 98 runs in his 20th innings and raises his average by 2. Find his new average.",
        [r"New average = $98 - 19 \times 2$.", r"= $98 - 38 = 60$.", r"Check: $19 \times 58 + 98 = 1200 = 20 \times 60$."],
        "60"),
    pat("avg-m2", "Overlapping windows", "common",
        "Averages over two overlapping stretches — Mon–Wed and Tue–Thu, or the first 7 and last 7 of 13 numbers.",
        r"\text{end}_2 - \text{end}_1 = k(\bar{b} - \bar{a}), \qquad \text{shared} = S_1 + S_2 - S",
        ["Turn both averages into sums.", "Subtract the sums: the shared items cancel, leaving the end difference. For first-k/last-k, ADD and subtract the whole: the shared middle survives.", "Use the extra fact (one end value, or a ratio) to finish."],
        "Shared values appear in both sums, so they vanish on subtraction and double up on addition.",
        "The average of 13 numbers is 30. The average of the first 7 is 27 and of the last 7 is 35. Find the 7th number.",
        [r"Part sums: $7 \times 27 = 189$, $7 \times 35 = 245$; whole = $13 \times 30 = 390$.", r"7th number = $189 + 245 - 390$.", r"= $44$."],
        "44"),
    pat("avg-m3", "Split set with relations between unknowns", "common",
        "Averages of parts of a list, plus a tie such as 'one number is 4 more than the other'.",
        r"\text{unknown part} = nA - \sum (\text{known parts})",
        ["Change every average into a sum.", "Find the leftover sum for the unknown values.", "Write the unknowns with one variable x from the relation, then solve."],
        "Once everything is a sum, the question is one equation in one variable.",
        "Six numbers average 30. The first two average 24 and the next two 33. Of the last two, one is 4 more than the other. Find the larger of the last two.",
        [r"Total = $180$; first pair = $48$; second pair = $66$.", r"Last pair total = $180 - 48 - 66 = 66$.", r"$x + (x + 4) = 66 \Rightarrow x = 31$; larger = $35$."],
        "35"),
    pat("avg-m4", "Ages over time", "common",
        "Average ages 'n years ago' or 'at the birth of the youngest', with members added later.",
        r"\text{average after } t \text{ years} = A + t \quad (\text{same members})",
        ["Bring every average to the SAME year: add t for each year passed.", "Work in totals; include or remove members as the story demands.", "At a member's birth: subtract that age from every member, and drop one from the count."],
        "Each person ages one year per year, so a fixed group's total rises by n per year.",
        "A family of 5 members has an average age of 24 years. The youngest is 8. What was the average age of the family at the birth of the youngest?",
        [r"Present total = $5 \times 24 = 120$ years.", r"8 years ago everyone was 8 younger: $120 - 5 \times 8 = 80$ years over 4 members.", r"Average = $80 \div 4 = 20$ years."],
        "20 years"),
    pat("avg-m5", "Bowling average", "occasional",
        "'A bowler's average is 12.4 runs per wicket; he takes 5 wickets for 26 runs and the average improves by 0.4.'",
        r"aW + r = (a - d)(W + w)",
        ["Let W be the wickets before the match; runs given so far = aW.", "After the match: runs aW + r, wickets W + w, average a − d.", "Solve the linear equation for W."],
        "A bowling average is a runs-per-wicket average, so the same total bridge applies.",
        "A bowler's average is 12.4 runs per wicket. In a match he takes 5 wickets for 26 runs, and his average improves by 0.4. How many wickets did he have before this match?",
        [r"$12.4W + 26 = 12(W + 5)$.", r"$12.4W + 26 = 12W + 60 \Rightarrow 0.4W = 34$.", r"$W = 85$."],
        "85"),
]

# =========================== apply ===========================
data = json.loads(TOPIC.read_text(encoding="utf-8"))
apply(data, "avg-basics", b_concept, b_notes, b_formulas, b_tricks, b_mistakes, b_revision, b_patterns)
apply(data, "avg-inclusion-exclusion", i_concept, i_notes, i_formulas, i_tricks, i_mistakes, i_revision, i_patterns)
apply(data, "avg-weighted", w_concept, w_notes, w_formulas, w_tricks, w_mistakes, w_revision, w_patterns)
apply(data, "avg-misc", m_concept, m_notes, m_formulas, m_tricks, m_mistakes, m_revision, m_patterns)

ids = [p["id"] for s in data["subtopics"] for p in s.get("patterns", [])]
assert len(ids) == len(set(ids)), "duplicate pattern ids in topic"
TOPIC.write_text(json.dumps(data, ensure_ascii=False, indent=1) + "\n", encoding="utf-8")
print("average updated:", ", ".join(f"{s['id']}: {len(s['patterns'])} patterns" for s in data["subtopics"]))
