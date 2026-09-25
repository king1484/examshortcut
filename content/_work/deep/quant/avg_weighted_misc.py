"""Phase-2 deep content for quant/average — weighted + misc modules."""
import os
import sys
from fractions import Fraction as F

sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
from _lib import Sub, num, mixed


def build_weighted():
    S = Sub("avg-weighted")
    S.notes = r"""### Why a simple average of averages goes wrong
Section A has 20 students with average 60 and section B has 80 students with average 40. The average of the two averages is 50, but the real class average is $\frac{20 \times 60 + 80 \times 40}{100} = 44$. The bigger section pulls the answer towards its own average. When groups have different sizes, each average must be **weighted** by its group size.

### The weighted-average formula
$$\bar{x} = \frac{n_1 \bar{x}_1 + n_2 \bar{x}_2 + \cdots}{n_1 + n_2 + \cdots}$$
In words: turn every group's average into a total ($n \times$ average), add the totals, divide by the total count.
Example: 30 boys average 42 kg and 20 girls average 37 kg → $\frac{1260 + 740}{50} = 40$ kg.

### Where the combined average sits
- It always lies between the smallest and the largest group average.
- It is closer to the average of the bigger group.
- If the groups are equal in size, it is exactly the simple average of the group averages.
These three facts let you reject options without any calculation.

### Finding a missing group average
Class of 40 averages 65; the 25 boys average 62. Class total $= 2600$, boys' total $= 1550$, so the 15 girls total $1050$ → girls' average $70$.
Always: missing total = overall total − known totals.

### Finding group sizes: the balance (alligation) method
When both group averages and the combined average are known, the sizes are in the **opposite** ratio of the distances from the combined average:
$$\frac{n_1}{n_2} = \frac{\bar{x}_2 - \bar{x}}{\bar{x} - \bar{x}_1}$$
Class average 58, boys 62, girls 52 → boys : girls $= (58 - 52) : (62 - 58) = 6 : 4 = 3 : 2$.
Think of a see-saw: the heavier group sits closer to the balance point.
Workers example: overall ₹8,000, 7 technicians at ₹12,000 (4000 above), the rest at ₹6,000 (2000 below) → technicians : rest $= 2000 : 4000 = 1 : 2$ → rest $= 14$, total $21$.

### When sizes are given as a ratio or a fraction
Boys : girls $= 3 : 2$ with averages 150 cm and 140 cm → treat the ratio as the counts: $\frac{3 \times 150 + 2 \times 140}{5} = 146$ cm.
"One-fourth of the class averages 72 and the class average is 60" → take the class as 4 parts: $4 \times 60 = 72 + 3x$ → $x = 56$ for the rest.

### Common traps
- Reversing the ratio in the balance method (the group CLOSER to the mean is the BIGGER one).
- Taking the simple average of averages when sizes differ.
- Forgetting that the group averages must bracket the combined average — if they do not, re-read the question.

### Quick revision
- Combined average $= \frac{\sum n_i \bar{x}_i}{\sum n_i}$.
- Missing group: overall total − known totals, then divide.
- Sizes: $n_1 : n_2 = (\bar{x}_2 - \bar{x}) : (\bar{x} - \bar{x}_1)$.
- Ratio or fraction of sizes → use them directly as counts.
"""

    S.pattern("avg-w1", "Combined average of two or more groups", "very common",
        "Two or three groups (boys/girls, sections, batches) with their sizes and averages; the overall average is asked.",
        r"\bar{x} = \frac{n_1 \bar{x}_1 + n_2 \bar{x}_2 + n_3 \bar{x}_3}{n_1 + n_2 + n_3}",
        r"""1. Multiply each group's size by its average to get its total.
2. Add all totals; add all sizes.
3. Divide. The answer must lie closer to the bigger group's average.

Why: an average is a total shared by a count, so only totals can be added.""",
        "30 boys average 42 kg and 20 girls average 37 kg. Find the average weight of all 50.",
        r"$\frac{30 \times 42 + 20 \times 37}{50} = \frac{1260 + 740}{50} = 40$ kg.")
    S.pattern("avg-w2", "Missing average of one group", "very common",
        "The overall average and one group's average are given; the other group's average is asked.",
        r"\bar{x}_2 = \frac{(n_1 + n_2)\bar{x} - n_1 \bar{x}_1}{n_2}",
        r"""1. Overall total $=$ total count $\times$ overall average.
2. Subtract the known group's total.
3. Divide the rest by the other group's size.

Why: the two totals must add up to the overall total.""",
        "The average marks of 40 students is 65. The 25 boys average 62. Find the girls' average.",
        r"$\frac{2600 - 1550}{15} = \frac{1050}{15} = 70$.")
    S.pattern("avg-w3", "Group sizes (or ratio) from the averages", "common",
        "All three averages are known (two groups + combined) and the ratio or number in a group is asked.",
        r"n_1 : n_2 = (\bar{x}_2 - \bar{x}) : (\bar{x} - \bar{x}_1)",
        r"""1. Find how far each group average is from the combined average.
2. Sizes are in the REVERSE ratio of these distances.
3. Scale the ratio to the given total if a number is asked.

Why: the extra above the mean from one group must balance the shortfall below the mean from the other.""",
        "Class average 58; boys average 62; girls average 52. Find boys : girls.",
        r"Distances: boys $4$, girls $6$ → boys : girls $= 6 : 4 = 3 : 2$.")
    S.pattern("avg-w4", "Group sizes given as a ratio or a fraction", "common",
        "'Boys and girls are in the ratio 3 : 2' or 'one-fourth of the students average …' instead of actual counts.",
        r"\bar{x} = \frac{a\bar{x}_1 + b\bar{x}_2}{a + b}",
        r"""1. Use the ratio parts (or fraction parts) as if they were the counts.
2. Apply the weighted-average formula or solve for the missing average.

Why: the weighted average depends only on the proportions of the groups, not the actual counts.""",
        "Boys and girls are in the ratio 3 : 2. Boys average 150 cm and girls 140 cm. Class average?",
        r"$\frac{3 \times 150 + 2 \times 140}{5} = \frac{730}{5} = 146$ cm.")

    a = F(30 * 42 + 20 * 37, 50)
    assert a == 40
    S.q("avg-w1", "easy",
        "The average weight of 30 boys is 42 kg and that of 20 girls is 37 kg. The average weight of all 50 students is:",
        ["40 kg", "39.5 kg", "41 kg", "39 kg"], "40 kg",
        r"$\frac{30 \times 42 + 20 \times 37}{50} = \frac{1260 + 740}{50} = 40$ kg.",
        "39.5 is the simple average of 42 and 37 — wrong because the groups differ in size.", 30)
    a = F(20 * 60 + 30 * 70 + 50 * 54, 100)
    assert a == 60
    S.q("avg-w1", "medium",
        "Three sections of a class have 20, 30 and 50 students, whose average marks are 60, 70 and 54 respectively. The average marks of all the students are:",
        ["60", r"$61\frac{1}{3}$", "62", "58"], num(a),
        r"Total $= 1200 + 2100 + 2700 = 6000$ for 100 students → average $= 60$.",
        r"$61\frac{1}{3}$ is the unweighted mean of 60, 70, 54 — the trap.", 40)
    a = F(20 * 15 + 30 * 20, 50)
    assert a == 18
    S.q("avg-w1", "easy",
        "The average of 20 numbers is 15 and the average of another 30 numbers is 20. The average of all 50 numbers is:",
        ["18", "17.5", "17", "18.5"], num(a),
        r"$\frac{300 + 600}{50} = 18$.", None, 25)
    g = F(40 * 65 - 25 * 62, 15)
    assert g == 70
    S.q("avg-w2", "medium",
        "The average marks of 40 students in a class is 65. If the average marks of the 25 boys is 62, the average marks of the girls is:",
        ["70", "68", "72", "67.5"], num(g),
        r"Class total $= 2600$; boys $= 1550$; girls $= 1050$ over 15 → $70$.", None, 35)
    l = F(50 * 38 - 30 * 36, 20)
    assert l == 41
    S.q("avg-w2", "easy",
        "The average of 50 numbers is 38. If the average of the first 30 numbers is 36, the average of the remaining 20 numbers is:",
        ["41", "40", "42", "39"], num(l),
        r"$\frac{1900 - 1080}{20} = \frac{820}{20} = 41$.",
        r"First 30 are 2 below → 60 short; the 20 must cover it → $38 + \frac{60}{20} = 41$.", 30)
    # w3
    rb, rg = 58 - 52, 62 - 58
    assert F(rb, rg) == F(3, 2)
    S.q("avg-w3", "medium",
        "The average marks of a class are 58. The boys average 62 and the girls average 52. The ratio of the number of boys to the number of girls is:",
        ["3 : 2", "2 : 3", "31 : 26", "5 : 3"], "3 : 2",
        r"Boys : girls $= (58 - 52) : (62 - 58) = 6 : 4 = 3 : 2$.",
        "The group closer to the mean (boys, 4 away) is the larger group — 2 : 3 is the reversed-ratio trap.", 35)
    n = [n for n in range(8, 100) if 7 * 12000 + (n - 7) * 6000 == 8000 * n]
    assert n == [21]
    S.q("avg-w3", "hard",
        "The average salary of all the workers in a workshop is ₹8,000. The average salary of 7 technicians is ₹12,000 and that of the rest is ₹6,000. The total number of workers is:",
        ["21", "22", "14", "28"], "21",
        r"""Let the total be n. $7 \times 12000 + (n - 7) \times 6000 = 8000n$
→ $84000 + 6000n - 42000 = 8000n$ → $2000n = 42000$ → $n = 21$.""",
        r"Technicians are 4000 above, the rest 2000 below → technicians : rest $= 1 : 2$ → rest $= 14$, total $= 21$.", 50)
    girls = 48 * F(74 - 71, (74 - 71) + (71 - 66))
    assert girls == 18
    S.q("avg-w3", "medium",
        "In a class of 48 students the average score is 71. The boys average 74 and the girls average 66. The number of girls is:",
        ["18", "30", "16", "20"], "18",
        r"""Boys : girls $= (71 - 66) : (74 - 71) = 5 : 3$.
Girls $= 48 \times \frac{3}{8} = 18$.""",
        "30 is the number of boys — read what is asked.", 40)
    a = F(3 * 150 + 2 * 140, 5)
    assert a == 146
    S.q("avg-w4", "medium",
        "In a class, the ratio of boys to girls is 3 : 2. The average height of the boys is 150 cm and that of the girls is 140 cm. The average height of the class is:",
        ["146 cm", "145 cm", "144 cm", "147 cm"], "146 cm",
        r"$\frac{3 \times 150 + 2 \times 140}{5} = \frac{730}{5} = 146$ cm.",
        "144 cm is the reversed-weights trap; 145 cm ignores the weights.", 30)
    x = (4 * 60 - 72) / F(3)
    assert x == 56
    S.q("avg-w4", "hard",
        "The average marks of a class are 60. One-fourth of the students have an average of 72. The average marks of the remaining students are:",
        ["56", "54", "48", "57"], num(x),
        r"Take the class as 4 students: total $= 240$. One of them has 72, so the other 3 have $168$ → average $56$.",
        r"The quarter is 12 above; the other three-quarters must be $\frac{12}{3} = 4$ below → $56$.", 45)
    b = F(8 * 68 - 3 * 72, 5)
    assert b == F(656, 10)
    S.q("avg-w4", "hard",
        "In a school, the ratio of boys to girls is 5 : 3. The average score of the whole school is 68 and the average score of the girls is 72. The average score of the boys is:",
        ["65.6", "64", "66.5", "70.4"], num(b),
        r"Take 5 boys and 3 girls: total $= 8 \times 68 = 544$; girls $= 216$; boys $= 328$ → $\frac{328}{5} = 65.6$.",
        r"Girls are 4 above: 3 × 4 = 12 extra, spread over 5 boys → boys are 2.4 below → $65.6$.", 50)
    return S


def build_misc():
    S = Sub("avg-misc")
    S.notes = r"""### Batsman and bowler questions
A batsman's **average** = total runs ÷ number of innings (here every innings counts as "out").
The standard question: "He scores x runs in his nth innings and his average rises by d." Let the new average be A. Then the old average was $A - d$ for $n - 1$ innings:
$$(n-1)(A - d) + x = nA \ \Rightarrow\ A = x - (n-1)d$$
Example: 98 runs in the 20th innings raise the average by 2 → new average $= 98 - 19 \times 2 = 60$.
The same bridge answers "how many must he score in the next innings to raise his average from 42 to 45 after 10 innings?" → $11 \times 45 - 10 \times 42 = 75$.

A **bowler's average** is runs given ÷ wickets taken, and a LOWER value is better. If his average is a, and in a match he takes w wickets for r runs so that the average falls by d, with W wickets before the match:
$$aW + r = (a - d)(W + w)$$
Average 12.4, 5 wickets for 26 runs, improves by 0.4 → $12.4W + 26 = 12(W + 5)$ → $W = 85$.

### Overlapping windows
The average of Monday to Thursday and the average of Tuesday to Friday share Tuesday, Wednesday and Thursday. Subtract the sums and the shared days cancel:
$$\text{Fri} - \text{Mon} = 4 \times (\text{second average} - \text{first average})$$
If one of the two end days is known (or their ratio), the other follows at once.
The "first 7 and last 7 of 13 numbers" question works the same way: the 7th number is counted twice, so
$$\text{middle} = \text{first-part sum} + \text{last-part sum} - \text{total sum}$$
13 numbers average 30; first 7 average 27; last 7 average 35 → 7th $= 189 + 245 - 390 = 44$.

### Split sets with relations
"The average of 6 numbers is 30; the first two average 24, the next two 33; of the remaining two, one is 4 more than the other." Go to sums: $180 - 48 - 66 = 66$ for the last two → $x + x + 4 = 66$ → 31 and 35.
Name the smallest unknown x and write every other unknown in terms of x.

### Ages over time
Every member of a group ages 1 year each year, so the **average age also rises by 1 per year** (for the same members).
- n years ago, a family's average was A; now it is $A + n$ for the same members.
- A child born later adds its age to the total and 1 to the count.
- "Average age of the family at the birth of the youngest": take the present total, subtract the youngest's age from **every other** member and the youngest itself: $\frac{\text{total} - (\text{members}) \times \text{youngest's age}}{\text{members} - 1}$.
Example: 5 members average 24, youngest 8 → at the youngest's birth: $\frac{120 - 5 \times 8}{4} = 20$.

### Checking your answer
Rebuild the story with totals: old total, change, new total, new count. If the new total ÷ new count matches the stated average, you are right.

### Quick revision
- Batsman: new average $= x - (n-1)d$; needed score $=$ new total $-$ old total.
- Bowler: runs-per-wicket totals on both sides of the match.
- Overlap: difference of ends $=$ window size × difference of averages; shared middle $=$ part sums − total.
- Split set: sums first, one variable.
- Ages: average age rises 1 per year for a fixed group.
"""

    S.pattern("avg-m1", "Batsman: score that changes the average", "very common",
        "'Scores x in the nth innings and raises his average by d' or 'how many runs needed next innings to reach an average'.",
        r"A_{\text{new}} = x - (n-1)d, \qquad \text{needed} = (n+1)A' - nA",
        r"""1. Write old total $= (n-1)(A - d)$ and new total $= nA$.
2. Their difference is the score in the nth innings; solve for A.
3. For 'runs needed', subtract old total from the target total.

Why: the new score must lift every earlier innings by d and still leave its own share A.""",
        "A batsman scores 98 in his 20th innings and his average rises by 2. His new average?",
        r"$98 - 19 \times 2 = 60$. Check: $19 \times 58 + 98 = 1200 = 20 \times 60$.")
    S.pattern("avg-m2", "Overlapping windows (days, first-k and last-k)", "common",
        "Averages over two overlapping sets — Mon–Thu and Tue–Fri, or first 7 and last 7 of 13 numbers.",
        r"\text{end}_2 - \text{end}_1 = k(\bar{b} - \bar{a}), \qquad \text{shared} = S_1 + S_2 - S",
        r"""1. Convert both averages to sums.
2. Subtract (days) — shared items cancel — or add and remove the total (first/last parts) — the shared item is left.
3. Use the extra fact (one end, or a ratio) to finish.

Why: shared values appear in both sums and vanish on subtraction.""",
        "The average of 13 numbers is 30. The first 7 average 27 and the last 7 average 35. Find the 7th number.",
        r"$7 \times 27 + 7 \times 35 - 13 \times 30 = 189 + 245 - 390 = 44$.")
    S.pattern("avg-m3", "Split set with relations between the unknowns", "common",
        "Averages of parts of a set plus 'one is 4 more than the other' or 'first is twice the second'.",
        r"\text{unknown part} = nA - \sum(\text{known parts})",
        r"""1. Change every average into a sum.
2. Get the leftover sum for the unknown values.
3. Write the unknowns with one variable x from the relation and solve.

Why: once everything is a sum, the question is a one-variable equation.""",
        "Six numbers average 30; the first two average 24 and the next two 33. Of the last two, one is 4 more than the other. The larger is?",
        r"Leftover $= 180 - 48 - 66 = 66$ → $2x + 4 = 66$ → $x = 31$ → larger $= 35$.")
    S.pattern("avg-m4", "Ages over time (family and groups)", "common",
        "Average ages 'n years ago' or 'at the time of marriage / birth of the youngest', with members added later.",
        r"\text{average after } t \text{ years} = A + t \ \ (\text{same members})",
        r"""1. Move every average to the SAME year (add t for each year passed).
2. Convert to totals and include or remove the new/old members.
3. At the birth of a member: subtract his age from every member, and drop him from the count.

Why: each person ages one year per year, so a fixed group's total rises by n per year.""",
        "A family of 5 averages 24 years. The youngest is 8. What was the average age of the family at the birth of the youngest?",
        r"Then: $120 - 5 \times 8 = 80$ shared by 4 people → $20$ years.")
    S.pattern("avg-m5", "Bowling average (runs per wicket)", "occasional",
        "'A bowler's average is 12.4 runs per wicket; he takes 5 wickets for 26 runs and his average improves by 0.4.'",
        r"aW + r = (a - d)(W + w)",
        r"""1. Let W be the wickets before the match; runs given so far $= aW$.
2. After the match: runs $aW + r$, wickets $W + w$, average $a - d$ (improvement means it falls).
3. Solve the linear equation for W.

Why: bowling average is a runs-per-wicket average, so the same total bridge applies.""",
        "A bowler's average is 12.4 runs per wicket. He takes 5 wickets for 26 runs and his average improves by 0.4. Wickets taken before this match?",
        r"$12.4W + 26 = 12(W + 5)$ → $0.4W = 34$ → $W = 85$.")

    A = 98 - 19 * 2
    assert 19 * (A - 2) + 98 == 20 * A
    S.q("avg-m1", "medium",
        "A batsman scores 98 runs in his 20th innings and thereby increases his average by 2 runs. His average after the 20th innings is:",
        ["60", "58", "62", "56"], str(A),
        r"""Let the new average be A. Then $19(A - 2) + 98 = 20A$ → $A = 98 - 38 = 60$.""",
        r"$x - (n-1)d = 98 - 19 \times 2 = 60$. (58 is the OLD average.)", 40)
    need = 11 * 45 - 10 * 42
    assert need == 75
    S.q("avg-m1", "medium",
        "A batsman has an average of 42 runs after 10 innings. How many runs must he score in the 11th innings to raise his average to 45?",
        ["75", "72", "48", "78"], str(need),
        r"Target total $= 11 \times 45 = 495$; present total $= 420$. Needed $= 75$.",
        r"$45 + 10 \times 3 = 75$ (own share + 3 for each earlier innings).", 35)
    W = [w for w in range(1, 500) if F(124, 10) * w + 26 == 12 * (w + 5)]
    assert W == [85]
    S.q("avg-m5", "hard",
        "A bowler's average is 12.4 runs per wicket. He takes 5 wickets for 26 runs in a match and his average improves by 0.4. The number of wickets he had taken before this match is:",
        ["85", "90", "80", "72"], "85",
        r"""Let W wickets before. $12.4W + 26 = 12(W + 5)$ → $0.4W = 34$ → $W = 85$.""",
        "90 is the total AFTER the match.", 50)
    W = [w for w in range(1, 500) if 16 * w + 30 == F(31, 2) * (w + 6)]
    assert W == [126]
    S.q("avg-m5", "hard",
        "A bowler conceded runs at an average of 16 runs per wicket. In his next match he took 6 wickets for 30 runs, which lowered his average by 0.5. How many wickets had he taken before this match?",
        ["126", "132", "120", "63"], "126",
        r"""$16W + 30 = 15.5(W + 6) = 15.5W + 93$ → $0.5W = 63$ → $W = 126$.""",
        "132 is the count after the match; 63 forgets to divide by 0.5.", 50)
    mid = 7 * 27 + 7 * 35 - 13 * 30
    assert mid == 44
    S.q("avg-m2", "medium",
        "The average of 13 numbers is 30. The average of the first 7 numbers is 27 and that of the last 7 numbers is 35. The 7th number is:",
        ["44", "42", "46", "31"], str(mid),
        r"The 7th number is in both parts: $189 + 245 - 390 = 44$.", None, 40)
    diff = 4 * (38 - 37)
    part = F(diff, 9 - 8)
    fri = 9 * part
    assert diff == 4 and fri == 36
    S.q("avg-m2", "medium",
        "The average temperature from Monday to Thursday was 37°C and from Tuesday to Friday was 38°C. If the temperatures on Monday and Friday were in the ratio 8 : 9, the temperature on Friday was:",
        ["36°C", "32°C", "40°C", "34°C"], "36°C",
        r"""(Tue + Wed + Thu + Fri) − (Mon + Tue + Wed + Thu) $= 4 \times 38 - 4 \times 37 = 4$ → Fri − Mon $= 4$.
Ratio 8 : 9 differs by 1 part → 1 part $= 4$ → Friday $= 36$°C (Monday 32°C).""", None, 45)
    rest = 6 * 30 - 2 * 24 - 2 * 33
    x = F(rest - 4, 2)
    assert x == 31 and x + 4 == 35
    S.q("avg-m3", "medium",
        "The average of 6 numbers is 30. The average of the first two is 24 and that of the next two is 33. Of the remaining two numbers, one is 4 more than the other. The larger of these two numbers is:",
        ["35", "33", "31", "37"], num(x + 4),
        r"Last two sum $= 180 - 48 - 66 = 66$. $x + (x + 4) = 66$ → $x = 31$, larger $= 35$.",
        "Their average is 33, and they differ by 4 → 33 ± 2.", 40)
    c = F(90, 10)
    assert 2 * (3 * c) + 3 * c + c == 90 and 6 * c == 54
    S.q("avg-m3", "hard",
        "The average of three numbers is 30. The first number is twice the second, and the second is three times the third. The largest number is:",
        ["54", "27", "9", "45"], num(6 * c),
        r"""Let the third be x → second $3x$, first $6x$. Sum $10x = 90$ → $x = 9$.
Largest (first) $= 54$.""", None, 40)
    a = F(5 * 24 - 5 * 8, 4)
    assert a == 20
    S.q("avg-m4", "medium",
        "The average age of a family of 5 members is 24 years. The youngest member is 8 years old. The average age of the family at the time of the birth of the youngest member was:",
        ["20 years", "16 years", "18 years", "22 years"], "20 years",
        r"""Present total $= 120$. 8 years ago each of the 5 was 8 years younger: $120 - 40 = 80$.
But the youngest was just born (age 0), so only 4 members counted → $\frac{80}{4} = 20$ years.""",
        "16 divides by 5 — the youngest did not yet exist.", 45)
    child = 3 * 22 - 2 * (25 + 5)
    assert child == 6
    S.q("avg-m4", "medium",
        "Five years ago, the average age of a husband and wife was 25 years. Today, the average age of the husband, the wife and their child is 22 years. The age of the child is:",
        ["6 years", "16 years", "11 years", "1 year"], "6 years",
        r"""Couple's total now $= 2 \times 25 + 10 = 60$. Family total $= 3 \times 22 = 66$. Child $= 6$ years.""",
        "16 forgets that the couple aged 5 years each.", 40)
    a_now = 90 - (2 * 24 + 8)
    assert a_now == 34 and a_now + 4 == 38
    S.q("avg-m4", "hard",
        "The present average age of A, B and C is 30 years. Four years ago, the average age of B and C was 24 years. What will be A's age 4 years from now?",
        ["38 years", "34 years", "46 years", "42 years"], "38 years",
        r"""A + B + C $= 90$ now. B + C now $= 48 + 8 = 56$. So A $= 34$ now → 4 years hence $= 38$.""",
        "46 forgets to age B and C by 4 years each.", 45)
    return S
