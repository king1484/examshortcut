from _lib import *

# ------------------------------------------------------------------ checks
assert F(10 + 1, 2) == F(11, 2)
assert 5 * 27 == 135
assert 15 * 3 + 5 == 50
assert 30 * 14 == 420 and 31 * 15 == 465 and 465 - 420 == 45
assert 30 - 2 == 28 and 5 * 30 == 150 and 28 + 29 + 30 + 31 + 32 == 150
assert 10 * F(77, 2) == 385
assert 9 * 27 == 243 and 8 * 25 == 200 and 243 - 200 == 43
assert 24 + F(44 - 20, 8) == 27
# batsman: 16 innings avg A, scores 87 in 17th, avg +3 -> avg after = 39
import sympy as sp
A = sp.symbols("A")
sol = sp.solve(sp.Eq(17 * (A + 3), 16 * A + 87), A)
assert sol == [36] and 36 + 3 == 39
# class: 60 students avg 50, 20 girls avg 40 -> boys avg 55
assert F(60 * 50 - 20 * 40, 40) == 55
# manager: 15 workers avg 250, add manager -> avg 300 -> manager 1050
assert 300 + 15 * (300 - 250) == 1050 and 15 * 250 + 1050 == 16 * 300
# avg of squares of first 10 naturals
assert F(10 * 11 * 21, 6 * 10) == F(77, 2) == F(385, 10)
# temperature: Mon-Wed avg 37, Tue-Thu avg 34, Mon 40 -> Thu 31
assert 3 * 37 == 111 and 3 * 34 == 102 and 102 - (111 - 40) == 31
# 11 numbers avg 50, first 6 avg 49, last 6 avg 52 -> 6th = 56
assert 6 * 49 + 6 * 52 - 11 * 50 == 56
# A B C avg 84, D joins avg 80 -> D 68; A = 78 -> B + C = 174; E replaces A, avg 79 -> E 74
assert 4 * 80 - 3 * 84 == 68 and 3 * 84 - 78 == 174 and 4 * 79 - (174 + 68) == 74
# 8 numbers avg 20; first two 15.5, next three 21 1/3; 6th 5 less than 7th, 8th 7 more than 7th -> 8th = 28
tot8 = 8 * 20
assert 2 * F(31, 2) + 3 * F(64, 3) == 31 + 64 == 95
rem = tot8 - 95
assert rem == 65
x = sp.symbols("x")
sol = sp.solve(sp.Eq(x + (x + 5) + (x + 12), 65), x)
assert sol == [16] and 16 + 12 == 28
# solved: 8 numbers avg 32.5 -> 260
assert 8 * F(65, 2) == 260
# solved: weighted boys/girls -> 11.4
assert F(20 * 12 + 30 * 11, 50) == F(57, 5) == F(114, 10)

subtopics = [
 sub("avg-basics", "Average & the sum bridge",
  md(r"$\text{Average} = \dfrac{\text{Sum of observations}}{\text{Number of observations}}$. The useful direction is the reverse: **Sum = Average × n** — most CGL average questions are solved by converting to sums immediately.",
     "",
     "**Properties:**",
     r"- If every observation is increased by k, the average increases by k (same for −, ×, ÷).",
     r"- The average is always between the smallest and largest observation.",
     r"- If all numbers are equal, average = each number; the sum of deviations from the average is zero.",
     "",
     r"**Standard averages** (memorise): first n naturals $= \frac{n+1}{2}$; first n odd $= n$; first n even $= n+1$; squares $= \frac{(n+1)(2n+1)}{6}$; cubes $= \frac{(n+1)^2}{4}$.",
     r"**Consecutive numbers:** average = middle term = $\frac{\text{first} + \text{last}}{2}$."),
  [formula("Definition", r"\bar{x} = \frac{\sum x_i}{n} \iff \sum x_i = n\bar{x}"),
   formula("Shift property", r"\overline{x_i + k} = \bar{x} + k,\quad \overline{k x_i} = k\bar{x}"),
   formula("First n naturals / odd / even", r"\frac{n+1}{2},\quad n,\quad n+1"),
   formula("Squares / cubes", r"\frac{(n+1)(2n+1)}{6},\quad \frac{(n+1)^2}{4}"),
   formula("Consecutive / AP terms", r"\text{average} = \frac{\text{first} + \text{last}}{2} = \text{middle term}")],
  [trick("Sum = average × n first",
         "Never manipulate averages directly — flip to sums, adjust, divide back.",
         "The average of 8 numbers is 32.5. Find their sum.",
         "Sum = 8 × 32.5 = 260."),
   trick("Uniform shift",
         "Adding k to every number just adds k to the average.",
         "The average of 6 numbers is 15. If each number is multiplied by 3 and increased by 5, find the new average.",
         r"New average $= 15 \times 3 + 5 = 50$."),
   trick("Middle of consecutive terms",
         "For evenly spaced numbers, the average is the central value — no addition needed.",
         "The average of 5 consecutive numbers is 30. Find the largest.",
         "Middle = 30 ⇒ numbers 28…32 ⇒ largest **32**.")],
  ["Reporting a sum where an average is asked (read the units).",
   "Averaging two averages with different group sizes (a 40-60 'average of averages' error).",
   r"Using $\frac{n(n+1)}{2}$-style sums without dividing by n when the average is asked.",
   "For 'each multiplied by 3 and increased by 5', applying only one of the two operations."]),

 sub("avg-inclusion-exclusion", "Members joining or leaving",
  md("When a new member joins (or one leaves) and the average changes, the key quantity is the **total sum**, not the average.",
     "",
     r"- New member whose entry changes the average from $A$ to $A'$ (group of n): value $= A' + n(A' - A)$.",
     r"- Member leaving: removed value $= A' + n(A - A')$, where A' is the new average of the remaining n.",
     r"- Replacement of one member: new − old $= n(A' - A)$, i.e. replaced value $= \text{old} + n(\text{change})$.",
     "",
     r"Equivalent view: the new member must carry the extra $n(A' - A)$ for all the old members **plus** his own share $A'$."),
  [formula("Joining member", r"\text{value} = A' + n(A' - A)"),
   formula("Leaving member", r"\text{value} = A' + n(A - A')"),
   formula("Replacement", r"\text{new} = \text{old} + n(A' - A)"),
   formula("Count change both ways", r"\text{total of newcomers} = \text{new total} - \text{old total}")],
  [trick("Joining: own share + extras",
         "New value = new average + (number of old members) × (average jump).",
         "The average age of 30 students is 14 years. When their teacher joins, the average becomes 15. Find the teacher's age.",
         "Teacher = 15 + 30 × 1 = **45 years**. (Check: 420 + 45 = 465 = 31 × 15 ✓)"),
   trick("Replacement: n × jump added",
         "Only the swapped item changes the sum, by exactly n × (average change).",
         "The average of 8 numbers is 24. If 20 is replaced by 44, the new average is:",
         "Jump = (44 − 20)/8 = 3 ⇒ new average = 24 + 3 = **27**."),
   trick("Exclusion: subtract the sums",
         "Old total − (new count × new average) = removed value.",
         "The average of 9 numbers is 27. If one number is excluded the average becomes 25. Find the excluded number.",
         "9 × 27 − 8 × 25 = 243 − 200 = **43**.")],
  ["Using the OLD average where the NEW one is needed in the member formula.",
   "Counting the new member inside n (n refers to the members BEFORE the change in the joining formula).",
   "For replacement, computing the new number as old + change (missing the factor n).",
   "Sign errors when the average falls instead of rising."]),

 sub("avg-weighted", "Weighted average & two-group problems",
  md(r"When groups of different sizes are combined, the combined average is the **weighted** mean:",
     "",
     r"$$\bar{x} = \frac{n_1 \bar{x}_1 + n_2 \bar{x}_2 + n_3 \bar{x}_3}{n_1 + n_2 + n_3}$$",
     "",
     "It always lies closer to the bigger group's average. Alligation (cross method) works too — see the Mixture topic.",
     "",
     "**Two unknown averages:** if a group's average is missing, compute total sums group-wise and divide. Keep every product written down; these questions are pure bookkeeping."),
  [formula("Weighted mean", r"\bar{x} = \frac{\sum n_i \bar{x}_i}{\sum n_i}"),
   formula("Missing group average", r"\bar{x}_2 = \frac{N\bar{x} - n_1\bar{x}_1}{n_2}"),
   formula("Alligation cross", r"\frac{n_1}{n_2} = \frac{\bar{x}_2 - \bar{x}}{\bar{x} - \bar{x}_1}")],
  [trick("Totals, not averages",
         "Convert each group to a total, add, divide by the combined count.",
         "In a class of 60 students, 20 girls have an average of 40 marks. If the class average is 50, find the boys' average.",
         r"Boys' total = 3000 − 800 = 2200 ⇒ average $= \frac{2200}{40} = 55$."),
   trick("Balance point intuition",
         "The combined average divides the gap between the two group averages in the ratio n₂ : n₁ (inverse of sizes).",
         "20 boys average 12 years, 30 girls average 11 years. Combined average?",
         r"$\frac{240 + 330}{50} = 11.4$ years — four parts from 11, one from 12, as 30 : 20 predicts."),
   trick("Newcomer pushing a known average",
         "Combined-average questions with a single newcomer reduce to value = A' + n(A' − A).",
         "15 workers average ₹250 in wages. A manager joins and the average becomes ₹300. Find the manager's wage.",
         "Manager = 300 + 15 × 50 = **₹1,050**.")],
  ["Combining averages directly (30 and 40 do not average to 35 unless the groups are equal).",
   "Dividing by the wrong combined count (students + teacher, workers + manager).",
   "Weighing with the wrong side of the alligation cross.",
   "Rounding intermediate sums — these questions usually come out exact; a decimal mid-way means a slip."]),

 sub("avg-misc", "Batsman problems, overlapping sums & multi-step sets",
  md(r"**Batsman/cricketer template:** a score in the next innings raises the average by d. If the new average is A' after n innings, the score was $A' + (n-1)d$. Rearranged: new average $= \frac{\text{old total} + \text{score}}{n}$.",
     "",
     "**Overlapping sums** (temperatures, marks): if the average of Mon–Wed is a and of Tue–Thu is b, subtracting gives Thu − Mon = 3(b − a). Give one endpoint to find the other.",
     "",
     "**Split sets:** an average over n numbers with partial averages over overlapping or consecutive chunks is solved by converting every average to a sum and using one variable for the unknown chunk."),
  [formula("Batsman score", r"\text{score} = A' + (n-1)d"),
   formula("Batsman new average", r"A' = \frac{(n-1)A + \text{score}}{n}"),
   formula("Overlap subtraction", r"\text{(Thu)} - \text{(Mon)} = 3(b - a)"),
   formula("Split sums", r"n\bar{x} = \sum_{\text{chunks}} (\text{chunk total})")],
  [trick("Batsman: work in totals",
         "Old total + new score = new count × new average.",
         "A batsman scores 87 in his 17th innings and thereby increases his average by 3. Find his average after the 17th innings.",
         r"$16(A - 3) + 87 = 17A$... solve: let new average be A: $17A = 16(A-3) + 87$ ⇒ $A = 39$."),
   trick("Overlap: subtract the sums",
         "The shared days cancel, leaving the difference of the end days.",
         "The average temperature of Mon, Tue, Wed is 37°C and of Tue, Wed, Thu is 34°C. If Monday was 40°C, find Thursday.",
         "Thu = 102 − (111 − 40) = **31°C**."),
   trick("One variable for the unknown chunk",
         "Name the smallest unknown x, express the rest from the given relations, and let the leftover sum close the equation.",
         "8 numbers average 20. First two average 15.5, next three average 21⅓. The 6th is 5 less than the 7th, and the 8th is 7 more than the 7th. Find the 8th.",
         "Leftover total = 160 − 95 = 65. Let 6th = x: x + (x+5) + (x+12) = 65 ⇒ x = 16 ⇒ 8th = **28**.")],
  ["In batsman problems, multiplying by n instead of (n − 1) for the old total.",
   "Subtracting the averages (37 − 34) and reporting 3 as Thu − Mon without multiplying by the overlap length rule.",
   "Forgetting that the 'next' chunk overlaps the previous one (11 numbers: first 6 and last 6 share the 6th).",
   "Setting the relations backwards (6th is 5 LESS than 7th ⇒ 7th = 6th + 5)."]),
]

pyq = [
 pat("Person joins / leaves, average changes", "very common",
     "Average age/weight/marks of a group; a teacher, manager or new member joins (or someone leaves); new average given.",
     "Convert to totals. Newcomer = A' + n(A' − A); leaver = A' + n(A − A'). Check with total sums."),
 pat("Replacement of an item", "common",
     "A number/weight is replaced by another; average changes by a known amount; find the new/old value.",
     "Change in sum = n × change in average. One line."),
 pat("Batsman's scoring innings", "common",
     "'Scores x in the nth innings and increases his average by d' — find new average or total runs.",
     "New total = (n−1)(A − d) + x = nA. Either form solves in one equation."),
 pat("Weighted average of two groups", "common",
     "Boys/girls, workers/managers, two sections with separate averages and a combined average.",
     "Total sums, then divide. Or alligation: sizes are inversely proportional to distances from the combined average."),
 pat("Average of first-n / consecutive series", "common",
     "Average of first 10 naturals, 20 odd numbers, consecutive integers, squares.",
     "Formula table: (n+1)/2, n, n+1; consecutive → middle term."),
 pat("Overlapping averages (Mon–Wed, Tue–Thu)", "occasional",
     "Averages over overlapping windows of days/matches; one endpoint known; find the other.",
     "Subtract sums: the shared items cancel; difference of end items = window size × average difference."),
 pat("Split-set with relations between terms", "occasional",
     "Overall average plus averages of chunks, plus 'one number is k less/more than another'; find a specific term.",
     "Everything to sums, name the smallest unknown x, close the equation with the leftover total."),
]

solved = []

assert 8 * F(65, 2) == 260
solved.append(Q("avg-s01", "The average of 8 numbers is 32.5. What is the sum of these numbers?",
  ["260", "262", "256", "264"], 0, 260,
  md(r"Sum $= 8 \times 32.5 = 260$."),
  "Sum = average × count: 8 × 32.5 = 260. Two seconds.",
  "easy", "avg-basics", "sum from average", 20))

assert F(20 * 12 + 30 * 11, 50) == F(57, 5)
solved.append(Q("avg-s02", "The average age of 20 boys is 12 years and that of 30 girls is 11 years. The average age of all the students is:",
  ["11.2 years", "11.4 years", "11.5 years", "11.6 years"], 1, F(57, 5),
  md(r"Total age $= 20 \times 12 + 30 \times 11 = 240 + 330 = 570$.",
     r"Average $= \frac{570}{50} = 11.4$ years."),
  "Weighted mean: the bigger group (girls) pulls the answer to 11.4 — closer to 11 than to 12.",
  "easy", "avg-weighted", "weighted average", 30))

assert 9 * 27 - 8 * 25 == 43
solved.append(Q("avg-s03", "The average of 9 numbers is 27. If one number is excluded, the average of the remaining numbers becomes 25. The excluded number is:",
  ["41", "43", "45", "47"], 1, 43,
  md(r"Excluded $= 9 \times 27 - 8 \times 25 = 243 - 200 = 43$."),
  "Total sums both ways and subtract — no formula needed.",
  "easy", "avg-inclusion-exclusion", "exclusion", 30))

assert 24 + F(24, 8) == 27
solved.append(Q("avg-s04", "The average of 8 numbers is 24. If the number 20 is replaced by 44, the new average will be:",
  ["25", "26", "27", "28"], 2, 27,
  md(r"Increase in sum $= 44 - 20 = 24$.",
     r"Increase in average $= \frac{24}{8} = 3$ ⇒ new average $= 27$."),
  "Average jumps by (change in the number)/8 = 24/8 = 3 ⇒ 24 + 3 = 27.",
  "easy", "avg-inclusion-exclusion", "replacement", 30))

A = sp.symbols("A")
sol = sp.solve(sp.Eq(17 * A, 16 * (A - 3) + 87), A)
assert sol == [39]
solved.append(Q("avg-s05", "A batsman scores 87 runs in his 17th innings and thus increases his average by 3 runs. His average after the 17th innings is:",
  ["36", "37", "39", "40"], 2, 39,
  md("Let the average after 17 innings be A.",
     r"Before: 16 innings at $(A - 3)$.",
     r"$16(A - 3) + 87 = 17A$ ⇒ $16A - 48 + 87 = 17A$ ⇒ $A = 39$."),
  "New total = old total + 87: 17A = 16(A−3) + 87 ⇒ A = 39. (Quick check: old avg 36, total 576; 576 + 87 = 663 = 17 × 39 ✓)",
  "medium", "avg-misc", "batsman innings", 50))

# ------------------------------------------------------------------ practice
P = []

assert F(11, 2) == 5.5
P.append(Q("avg-q01", "The average of the first 10 natural numbers is:",
  ["5", "5.5", "6", "6.5"], 1, F(11, 2),
  md(r"Average $= \frac{n+1}{2} = \frac{11}{2} = 5.5$."),
  "Consecutive 1–10: average = middle pair (5 + 6)/2 = 5.5.",
  "easy", "avg-basics", "first n naturals", 20))

assert 5 * 27 == 135
P.append(Q("avg-q02", "The average of 5 numbers is 27. If one more number 37 is included, the new average is:",
  ["28", "28.5", "29", "30"], 1, 28.5,
  md(r"Old sum $= 135$. New sum $= 135 + 37 = 172$.",
     r"New average $= \frac{172}{6} = 28.5$."),
  "37 is 10 above the old average; the extra 10 spreads over 6 numbers: 27 + 10/6 = 28.5.",
  "easy", "avg-inclusion-exclusion", "inclusion", 25))

assert 15 * 3 + 5 == 50
P.append(Q("avg-q03", "The average of 6 numbers is 15. If each number is multiplied by 3 and then increased by 5, the new average is:",
  ["45", "50", "53", "20"], 1, 50,
  md(r"New average $= 15 \times 3 + 5 = 50$."),
  "Linear operations pass through the average: ×3 then +5 ⇒ 50.",
  "easy", "avg-basics", "shifted average", 25))

assert 28 + 29 + 30 + 31 + 32 == 150
P.append(Q("avg-q04", "The average of 5 consecutive numbers is 30. The largest of these numbers is:",
  ["30", "31", "32", "34"], 2, 32,
  md("The middle (3rd) number is the average = 30.",
     "Numbers: 28, 29, 30, 31, 32 ⇒ largest **32**."),
  "Average = middle term ⇒ largest = 30 + 2 = 32.",
  "easy", "avg-basics", "consecutive average", 20))

assert 10 * F(77, 2) == 385
P.append(Q("avg-q05", "A batsman made 38.5 runs on average in 10 innings. His total runs are:",
  ["385", "375", "395", "405"], 0, 385,
  md(r"Total $= 38.5 \times 10 = 385$."),
  "Sum = average × innings = 385.",
  "easy", "avg-basics", "sum from average", 20))

assert 465 - 420 == 45
P.append(Q("avg-q06", "The average age of 30 students in a class is 14 years. When the teacher's age is included, the average age increases by one year. The teacher's age is:",
  ["31 years", "35 years", "45 years", "49 years"], 2, 45,
  md(r"Teacher $= 31 \times 15 - 30 \times 14 = 465 - 420 = 45$ years."),
  "Newcomer = new average + n × (jump) = 15 + 30 × 1 = 45.",
  "medium", "avg-inclusion-exclusion", "teacher joins", 35))

assert 6 * 49 + 6 * 52 - 11 * 50 == 56
P.append(Q("avg-q07", "The average of 11 numbers is 50. The average of the first 6 numbers is 49 and that of the last 6 is 52. The 6th number is:",
  ["54", "56", "58", "60"], 1, 56,
  md(r"6th $= 6 \times 49 + 6 \times 52 - 11 \times 50 = 294 + 312 - 550 = 56$."),
  "The 6th number is counted in both chunks: chunk sums add to total + 6th ⇒ 6th = 606 − 550 = 56.",
  "medium", "avg-misc", "overlapping chunks", 45))

sol = None
A = sp.symbols("A")
sol = sp.solve(sp.Eq(17 * A, 16 * (A - 3) + 87), A)
assert sol == [39]
P.append(Q("avg-q08", "A batsman scores 87 runs in his 17th innings, which increases his average by 3 runs. His average after the 17th innings is:",
  ["36", "38", "39", "42"], 2, 39,
  md(r"$16(A - 3) + 87 = 17A$ ⇒ $A = 39$."),
  "Old total 576 (16 × 36) + 87 = 663 = 17 × 39.",
  "medium", "avg-misc", "batsman innings", 45))

assert F(3000 - 800, 40) == 55
P.append(Q("avg-q09", "The average marks of 60 students in a class is 50. The average marks of the 20 girls is 40. The average marks of the boys is:",
  ["52.5", "54", "55", "57.5"], 2, 55,
  md(r"Boys $= 40$; boys' total $= 60 \times 50 - 20 \times 40 = 3000 - 800 = 2200$.",
     r"Boys' average $= \frac{2200}{40} = 55$."),
  "Alligation too: 20 : 40 (girls : boys) splits the 40–55... the combined 50 sits 10 from girls' 40 and 5 from boys' 55 ⇒ sizes 2 : 1 ✓.",
  "medium", "avg-weighted", "two groups", 40))

assert 300 + 15 * 50 == 1050
P.append(Q("avg-q10", "The average monthly wage of 15 workers is ₹250. A manager is appointed and the average wage becomes ₹300. The manager's monthly wage is:",
  ["₹550", "₹800", "₹1,050", "₹1,200"], 2, 1050,
  md(r"Manager = $16 \times 300 - 15 \times 250$ = ₹1,050."),
  "Manager = 300 + 15 × 50 = ₹1,050 (his own share plus the ₹50 raise for each of the 15).",
  "medium", "avg-weighted", "manager joins", 35))

assert F(10 * 11 * 21, 60) == F(77, 2)
P.append(Q("avg-q11", r"The average of the squares of the first 10 natural numbers is:",
  ["36.5", "38.5", "40.5", "42"], 1, F(77, 2),
  md(r"Sum of squares $= \frac{10 \times 11 \times 21}{6} = 385$.",
     r"Average $= \frac{385}{10} = 38.5$."),
  r"Formula $\frac{(n+1)(2n+1)}{6}$ with n = 10 ⇒ 385/10 = 38.5.",
  "medium", "avg-basics", "squares average", 30))

assert 102 - 71 == 31
P.append(Q("avg-q12", "The average temperature of Monday, Tuesday and Wednesday is 37°C and of Tuesday, Wednesday and Thursday is 34°C. If the temperature on Monday was 40°C, the temperature on Thursday is:",
  ["29°C", "31°C", "33°C", "35°C"], 1, 31,
  md("Mon + Tue + Wed = 111; Tue + Wed + Thu = 102.",
     "Thu = 102 − (Tue + Wed) = 102 − (111 − 40) = **31°C**."),
  "Thursday = Monday − 3 × (37 − 34) = 40 − 9 = 31.",
  "medium", "avg-misc", "overlapping days", 35))

assert 4 * 79 - 242 == 74
P.append(Q("avg-q13", "The average weight of three men A, B and C is 84 kg. A fourth man D joins them and the average weight of the four becomes 80 kg. If A weighs 78 kg and E replaces A, the average weight of B, C, D and E becomes 79 kg. E's weight is:",
  ["70 kg", "72 kg", "74 kg", "76 kg"], 2, 74,
  md("A + B + C = 252; D = 4 × 80 − 252 = 68.",
     "B + C = 252 − 78 = 174. B + C + D + E = 4 × 79 = 316.",
     r"E $= 316 - 174 - 68 = 74$ kg."),
  "Build every sum stepwise: 252 → D = 68 → B + C = 174 → E = 316 − 242 = 74.",
  "hard", "avg-inclusion-exclusion", "multi-step inclusion", 70))

assert 16 + 12 == 28
P.append(Q("avg-q14", "The average of 8 numbers is 20. The average of the first two is 15.5 and that of the next three is $21\\frac{1}{3}$. If the 6th number is 5 less than the 7th and the 8th is 7 more than the 7th, the 8th number is:",
  ["24", "26", "28", "30"], 2, 28,
  md("Total = 160. First five total = 31 + 64 = 95.",
     "Last three total = 65. Let the 6th be x: 6th + 7th + 8th = x + (x + 5) + (x + 12).",
     r"$3x + 17 = 65$ ⇒ $x = 16$ ⇒ 8th $= 16 + 12 = 28$."),
  "Leftover sum 65 across three numbers whose mean is 65/3 — anchor on the 7th: 6th = 7th − 5, 8th = 7th + 7 ⇒ 7th = 21 ⇒ 8th = 28.",
  "hard", "avg-misc", "split set relations", 75))

assert 57 == 3 * 19
P.append(Q("avg-q15", "The average age of a husband and wife at the time of their marriage was 23 years. After 5 years they have a one-year-old child. The average age of the family of three now is:",
  ["17 years", "18 years", "19 years", "20 years"], 2, 19,
  md("Marriage total = 2 × 23 = 46. After 5 years: 46 + 5 + 5 = 56.",
     "Child adds 1 year: total = 57.",
     r"Average $= \frac{57}{3} = 19$ years."),
  "Both adults age 5 (total 56), child is 1 ⇒ 57/3 = 19. (Trap: forgetting to add the child's own age.)",
  "hard", "avg-misc", "family ages", 50))

topic = {
 "id": "average", "sectionId": "quant", "title": "Average", "order": 6,
 "importance": "high", "avgQuestions": {"tier1": 1, "tier2": 2},
 "summary": "One guaranteed question in almost every Tier 1 shift: a member joining or leaving, a batsman's innings, or a weighted two-group average. The whole topic collapses to one habit — convert averages to sums (Sum = Avg × n) before touching anything.",
 "subtopics": subtopics, "pyqPatterns": pyq, "solvedExamples": solved, "practice": P,
}
write_topic(topic)
