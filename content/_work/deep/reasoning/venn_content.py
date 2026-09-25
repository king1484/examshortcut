# -*- coding: utf-8 -*-
"""Notes, patterns and pyqPatterns for venn-diagrams.json (imported by venn-diagrams.py)."""
from _lib import P, PYQ

NOTES_IDEA = r"""### What a Venn diagram shows
A Venn diagram is a picture of **membership**. Each circle is a group (people who drink tea, even numbers, doctors). A point inside a circle belongs to that group. A point where two circles overlap belongs to both. The rectangle around the circles is the **universal set** — everyone being talked about — and the space outside all circles holds those who belong to none.

The diagram is only useful if you read it by **regions**, not by circles. A region is a piece of the picture that cannot be split further by any circle line.

### Counting regions
- **Two** intersecting circles make **4** regions: only A, only B, both, neither.
- **Three** mutually intersecting circles make **8** regions: 3 "only" regions, 3 "exactly two" regions, 1 "all three" region and 1 "none" region.
- In general each region is a yes/no answer for every circle, so n circles drawn with every overlap give 2ⁿ regions (including the outside).
- Circle A alone is made of **4** of the 8 regions in a three-circle diagram: only A, A-and-B only, A-and-C only, and all three.

### Words → set symbols
| Phrase | Symbol | Regions (three circles) |
|---|---|---|
| in A or B (at least one) | A ∪ B | everything inside A or B |
| in both A and B | A ∩ B | A-B only **plus** all three |
| in A but not B | A − B | only A **plus** A-C only |
| in A and B but not C | (A ∩ B) − C | A-B only |
| in exactly one of A, B | (A ∪ B) − (A ∩ B) | only A, only B |
| in none | outside all circles | the "none" region |

The commonest slip is to read "in both A and B" as the single A-and-B-only region. "Both A and B" says nothing about C, so the all-three region is included.

### Reading numbers off a diagram
When the numbers are written region by region, every question is just **adding the right regions**. Suppose a survey of news habits — Newspaper (N), TV (T), Radio (R) — gives: only N 20, only T 25, only R 5, N-T only 15, T-R only 6, N-R only 4, all three 10, none 15 (total 100).
- Total newspaper readers = 20 + 15 + 4 + 10 = **49** (all four N-regions).
- At least two sources = 15 + 6 + 4 + 10 = **35**.
- Exactly one source = 20 + 25 + 5 = **50**.
- Not TV = total − all T-regions = 100 − 56 = **44**.
- At most one source = exactly one + none = 50 + 15 = **65**.

### Negative phrases
- **Neither / none** is the outside region.
- **Not A** is everything outside circle A, including the none region.
- **At most one** includes those in no circle at all.
- **Either A or B but not both** is the two "only" regions.

### Method that never fails
1. Write the region numbers (or letters) in the picture.
2. Turn the phrase into a list of regions.
3. Add those regions only once each.

### Quick revision
- Read by regions; two circles = 4 regions, three circles = 8 (including outside).
- "Both A and B" includes the all-three region; "A and B only" does not.
- A − B keeps the parts of A outside B, whatever C does.
- Not A includes the none region; at most one = exactly one + none.
- List the regions first, then add each one once.
"""

NOTES_TWO = r"""### The four regions
Two overlapping circles A and B split the universe into four parts: **only A**, **only B**, **both**, **neither**. Every two-set question is a sum or a difference of these four numbers. Write them in the picture before doing anything else.

### Core formulas
- n(A ∪ B) = n(A) + n(B) − n(A ∩ B). The overlap is subtracted once because it was counted in both circles.
- Only A = n(A) − both; only B = n(B) − both.
- Exactly one = only A + only B = n(A) + n(B) − 2 × both.
- Neither = total − n(A ∪ B).
- Total = only A + only B + both + neither.

### Worked example
In a society of 150 families, 90 have a car, 70 have a two-wheeler and 40 have both.
- At least one = 90 + 70 − 40 = 120.
- Neither = 150 − 120 = **30**.
- Only car = 90 − 40 = 50; only two-wheeler = 70 − 40 = 30.
A common wrong answer is 70: taking only car + only two-wheeler = 80 and then 150 − 80, which forgets the 40 who have both.

### Reverse puzzles
Sometimes the question gives the answer regions and asks for a circle total or for the overlap. Use the same four boxes and fill in what you know.
- Given union and the two totals: both = n(A) + n(B) − union.
- If everybody is in at least one set: union = total, so both = n(A) + n(B) − total.
- Ratio clues: "only cricket is twice only football", with only C + only F = 30, gives only F = 10, only C = 20.

### Percentages
Treat the whole group as 100 and work in percent. Convert to people only at the end.
- 35% failed maths, 25% failed English, 10% failed both → failed at least one = 50%, so passed both = 50%. If 250 passed both, total = 250 ÷ 0.5 = 500.
- The trap: 100 − 35 − 25 = 40% "passed both" forgets that the 10% who failed both were subtracted twice.

### Maximum and minimum overlap
When the overlap is not given, it can move within limits (total N, sets of size a and b):
- **Maximum both** = the smaller set, min(a, b) — the small circle sits fully inside the big one.
- **Minimum both** = a + b − N, or 0 if that is negative — the circles overlap only as much as they are forced to.
- **Maximum neither** = N − max(a, b) — again when the smaller circle sits inside the larger.
- **Minimum neither** = N − (a + b), or 0 if negative.
Example: 60 students, 45 like tea, 35 like coffee → both is at least 45 + 35 − 60 = 20 and at most 35.

### Quick revision
- Four boxes: only A, only B, both, neither — fill them first.
- Union = A + B − both; neither = total − union; exactly one = A + B − 2 × both.
- Everyone in at least one set → both = A + B − total.
- Percent questions: work in %, convert at the end; passed both ≠ 100 − fail₁ − fail₂.
- Max both = smaller set; min both = A + B − N (not below 0); max neither = N − larger set.
"""

NOTES_THREE = r"""### The eight regions
Three circles A, B, C give seven regions inside and one outside:
- **Only A, only B, only C** — exactly one set.
- **A-B only, B-C only, A-C only** — exactly two sets.
- **A-B-C** — all three.
- **None** — outside all circles.

Always fill the diagram **from the centre outwards**: all three first, then the exactly-two regions, then the only regions, then none.

### The master formula
n(A ∪ B ∪ C) = n(A) + n(B) + n(C) − n(A∩B) − n(B∩C) − n(A∩C) + n(A∩B∩C)

Why the triple is added back: it is counted 3 times in the singles, removed 3 times in the pairs, so it would be lost without the last term.

### Region formulas
- A-B only = n(A∩B) − all three (and the same for the other two pairs).
- Only A = n(A) − n(A∩B) − n(A∩C) + all three.
- Exactly two = (sum of pairwise) − 3 × all three.
- At least two = (sum of pairwise) − 2 × all three.
- Exactly one = union − exactly two − all three.

### Worked example
In a club of 60 members, 30 play cricket (C), 25 football (F), 20 hockey (H); 10 play C and F, 8 play F and H, 7 play C and H, and 4 play all three.
- Centre: 4.
- Exactly two: C-F only 10 − 4 = 6; F-H only 8 − 4 = 4; C-H only 7 − 4 = 3.
- Only C = 30 − 6 − 3 − 4 = 17; only F = 25 − 6 − 4 − 4 = 11; only H = 20 − 4 − 3 − 4 = 9.
- Union = 17 + 11 + 9 + 6 + 4 + 3 + 4 = 54 (the formula gives 30 + 25 + 20 − 10 − 8 − 7 + 4 = 54 as well).
- None = 60 − 54 = **6**.
Forgetting the "+ 4" gives a union of 50 and a wrong answer of 10.

### Reverse questions
- **Find the triple** from the union: rearrange the master formula. With singles 25, 30, 20, pairs 10, 8, 7 and union 55: 75 − 25 + x = 55, so x = 5.
- **Exactly-counts to sum of circles**: if 60 people are in exactly one set, 30 in exactly two and 10 in all three, then n(A) + n(B) + n(C) = 60 + 2 × 30 + 3 × 10 = 150, because a person in two circles is counted twice.

### Percent data
When the three sets are given in percent, take the total as 100 and use the same formulas. If 50%, 40% and 30% like three kinds of songs, with pairs 20%, 15%, 10% and all three 5%, the union is 80% and **20%** like none. Convert to people only at the end.

### Checks that catch mistakes
- No region can be negative. If "only A" comes out negative, a number was misread.
- The seven inside regions must add up to the union.
- "At least two" is always greater than or equal to "exactly two".

### Quick revision
- Fill from the centre: triple → exactly-two → only → none.
- Union = ΣA − Σpairs + triple.
- Exactly two = Σpairs − 3 × triple; at least two = Σpairs − 2 × triple.
- Only A = A − AB − AC + triple.
- ΣA = exactly one + 2 × exactly two + 3 × all three.
- Check: no negative region; seven regions sum to the union.
"""

NOTES_REL = r"""### What the question asks
You get three words (Doctors, Men, Writers; Even numbers, Odd numbers, Prime numbers) and must choose the circle picture that shows how the groups are related. There are no numbers — only **relationships**.

### Two tests for every pair
Look at the three pairs one at a time: (1, 2), (2, 3), (1, 3).
1. **Inside test.** Is every member of X *always* a member of Y? Every sparrow is a bird → the Sparrows circle is drawn **inside** Birds.
2. **Apart test.** Can X and Y *never* share a member? No number is both even and odd → the two circles are drawn **separate**.
3. If neither test holds, some members can be in both and some cannot → the circles **intersect**.

Judge by definition, not by what is usual. A doctor *can* be a woman and a woman *can* be a doctor, so Doctors and Women intersect.

### The shapes that appear
| Relationship | Picture | Example |
|---|---|---|
| X ⊂ Y ⊂ Z | three nested circles | Sparrows, Birds, Animals |
| X, Y separate, both inside Z | two separate circles inside a third | Pens, Pencils, Stationery |
| X, Y intersect, both inside Z | two intersecting circles inside a third | Even numbers, Multiples of 3, Integers |
| X ⊂ Y, Z apart from both | one inside another, third separate | Whales, Mammals, Fish |
| X ⊂ Y, Z crosses both | one inside another, third intersecting both | Fathers, Men, Doctors |
| X ⊂ Y, Z crosses only Y | third cuts the outer circle only | Natural numbers, Integers, Negative numbers |
| X, Y intersect, Z inside their overlap | third inside the common part | Multiples of 5, Multiples of 7, Multiples of 35 |
| X, Y separate, Z crosses both | two separate circles joined by a third | Even numbers, Odd numbers, Prime numbers |
| all pairs intersect | three intersecting circles | Teachers, Women, Singers |
| two intersect, third apart | two intersecting circles and a separate one | Women, Engineers, Rivers |
| no links | three separate circles | Pens, Rivers, Tigers |

### Tricky cases
- **Number sets** are exact: check a sample. 2 is even and prime, 3 is odd and prime, 9 is odd and not prime — so Primes cross both Even and Odd while Even and Odd never meet.
- **"Crosses only the outer circle."** Negative numbers include −1 (an integer) and −½ (not an integer), and no negative number is a natural number. So the Negative circle cuts Integers but stays away from the Naturals circle inside it.
- **Inside their overlap.** Every multiple of 35 is a multiple of both 5 and 7, so it sits inside the common part of those two circles.
- **Gender words.** Fathers ⊂ Men; Mothers ⊂ Women; Men and Women are separate.

### Method
1. Write the three pairs.
2. Mark each pair **inside**, **apart** or **cross**.
3. Match the three marks to the picture — do not jump to a picture from the first pair alone.

### Quick revision
- For each pair: always both → inside; never both → apart; else → cross.
- Judge by definition, not by what is common.
- Test number sets with small examples (2, 3, 9, −1, −½).
- A third circle can cross both, only the outer, or sit inside an overlap — check each pair separately.
- Decide all three pairs before picking the picture.
"""

P_IDEA = [
 P("vn-p1", "Phrase to set expression", "common",
   "A phrase like 'doctors and singers but not players' with options written in ∩, ∪ and − symbols.",
   "1. List which regions the phrase covers.\n2. For each option, list the regions it covers.\n3. Pick the option whose regions match exactly.\n\n*Why it works:* two expressions mean the same only if they cover the same regions.",
   "Which expression shows 'in A and B but not C'?",
   "The phrase is the A-B-only region = **(A ∩ B) − C**. A ∩ B alone would also include the all-three region."),
 P("vn-p2", "Reading region numbers", "very common",
   "Numbers are given for each region (only A, A-B only, all three, none) and a question asks for a total.",
   "1. Turn the question into a list of regions.\n2. Add those region numbers, each once.\n3. Use total − region sum for 'not' questions.\n\n*Why it works:* regions never overlap, so adding them never double-counts.",
   "Only N 20, N-T only 15, N-R only 4, all three 10. How many read the newspaper?",
   "All N-regions: 20 + 15 + 4 + 10 = **49**."),
 P("vn-p3", "Counting regions", "occasional",
   "Asks how many regions a diagram has, or how many regions make up one circle.",
   "1. Each region is a yes/no choice for every circle.\n2. n circles with all overlaps → 2ⁿ regions including the outside.\n3. Regions inside one circle of three = 2² = 4.\n\n*Why it works:* every combination of in/out appears exactly once.",
   "How many regions does a diagram of three mutually intersecting circles have (including the outside)?",
   "2³ = **8**."),
 P("vn-p4", "Negative and 'at most' phrases", "common",
   "Phrases like not A, neither, at most one, either but not both.",
   "1. 'Not A' = total − all regions of A (includes the none region).\n2. 'At most one' = exactly one + none.\n3. 'Either but not both' = the two only-regions.\n\n*Why it works:* negative phrases are easiest as complements of positive ones.",
   "Total 100; the four T-regions add to 56. How many do not watch TV?",
   "100 − 56 = **44**."),
]

P_TWO = [
 P("vn-p5", "Union and neither", "very common",
   "Two totals, their overlap and the group size; asks at least one, neither or only one set.",
   "1. Union = A + B − both.\n2. Neither = total − union.\n3. Only A = A − both.\n\n*Why it works:* the overlap is counted twice in A + B, so it is removed once.",
   "150 families: 90 car, 70 two-wheeler, 40 both. How many have neither?",
   "Union = 90 + 70 − 40 = 120; neither = 150 − 120 = **30**.",
   "n(A ∪ B) = n(A) + n(B) − n(A ∩ B)"),
 P("vn-p6", "Reverse two-set puzzle", "common",
   "Some region values are given and a circle total, the overlap or the group size is asked; may include a ratio clue.",
   "1. Draw the four boxes: only A, only B, both, neither.\n2. Fill the known boxes.\n3. Solve for the missing box from the total or the ratio.\n\n*Why it works:* the four boxes always add to the total.",
   "30 like mango, 15 like only guava, 8 like neither. Group size?",
   "Mango (30, includes both) + only guava 15 + neither 8 = **53**."),
 P("vn-p7", "Percentage sets", "common",
   "Data given in percent; the answer may be in percent or in people.",
   "1. Work the whole problem in percent with total 100.\n2. Find the percent of the asked region.\n3. Convert: people = percent × total ÷ 100 (or total = people ÷ percent × 100).\n\n*Why it works:* percentages obey the same region algebra as counts.",
   "35% failed maths, 25% failed English, 10% failed both; 250 passed both. Total?",
   "Failed at least one = 50%, passed both = 50% → total = **500**."),
 P("vn-p8", "Maximum and minimum overlap", "occasional",
   "The overlap is not given; asks the largest or smallest possible both / neither.",
   "1. Max both = smaller set.\n2. Min both = A + B − N (0 if negative).\n3. Max neither = N − larger set; min neither = N − (A + B) (0 if negative).\n\n*Why it works:* the smaller circle can sit fully inside the larger, or the circles can be pushed apart until the total forces overlap.",
   "60 students; 45 tea, 35 coffee. Minimum who like both?",
   "45 + 35 − 60 = **20**.",
   "min both = max(0, A + B − N); max both = min(A, B)"),
]

P_THREE = [
 P("vn-p9", "Three-set union and none", "very common",
   "Three totals, three pairwise overlaps and the triple; asks at least one or none.",
   "1. Union = ΣA − Σpairs + triple.\n2. None = total − union.\n3. Check that no region is negative.\n\n*Why it works:* the triple is added in 3 times and removed 3 times, so it is added back once.",
   "60 members: 30, 25, 20; pairs 10, 8, 7; all three 4. None?",
   "Union = 75 − 25 + 4 = 54; none = **6**.",
   "n(A∪B∪C) = ΣA − Σ(pairs) + n(A∩B∩C)"),
 P("vn-p10", "Exactly one / exactly two / at least two", "common",
   "Asks how many belong to exactly one, exactly two or at least two sets.",
   "1. Exactly two = Σpairs − 3 × triple.\n2. At least two = Σpairs − 2 × triple.\n3. Exactly one = union − exactly two − triple.\n\n*Why it works:* each pairwise figure contains the triple once.",
   "Pairs 15, 12, 10; triple 5. Exactly two?",
   "37 − 15 = **22**."),
 P("vn-p11", "Fill one region", "common",
   "Asks for one specific region: only A, or A-and-B-but-not-C.",
   "1. A-B only = n(A∩B) − triple.\n2. Only A = n(A) − n(A∩B) − n(A∩C) + triple.\n3. Fill from the centre outwards if more regions are needed.\n\n*Why it works:* subtracting both pairs removes the triple twice, so it is added back once.",
   "n(A) = 45, n(A∩B) = 15, n(A∩C) = 12, triple 6. Only A?",
   "45 − 15 − 12 + 6 = **24**."),
 P("vn-p12", "Reverse three-set puzzle", "occasional",
   "The union or the exactly-counts are given and the triple or the circle sum is asked.",
   "1. Rearrange the master formula for the unknown term.\n2. Or use ΣA = exactly one + 2 × exactly two + 3 × all three.\n3. Verify by filling the eight regions.\n\n*Why it works:* each person is counted once for every circle they are in.",
   "Everyone in at least one of three sets; 60 in exactly one, 30 in exactly two, 100 people. Sum of the three circle totals?",
   "All three = 10; ΣA = 60 + 60 + 30 = **150**."),
]

P_REL = [
 P("vn-p13", "Nested chain", "common",
   "Each word is a type of the next: sparrow → bird → animal.",
   "1. Check that every X is a Y and every Y is a Z.\n2. Draw the circles one inside the next.\n\n*Why it works:* subset of a subset is a subset.",
   "Sparrows, Birds, Animals.",
   "Every sparrow is a bird, every bird an animal → **three nested circles**."),
 P("vn-p14", "Subsets inside a bigger set", "very common",
   "Two words are kinds of the third word.",
   "1. Put both smaller groups inside the big circle.\n2. Decide whether the two smaller groups can share members: never → separate; sometimes → intersecting.\n3. If one group is inside another and the third is unrelated, draw the third apart.\n\n*Why it works:* the relation between the two small groups is separate from their relation to the big one.",
   "Pens, Pencils, Stationery.",
   "Both are stationery; nothing is both a pen and a pencil → **two separate circles inside a third**."),
 P("vn-p15", "Partial overlaps", "common",
   "No word is a kind of another; some pairs can share members, some cannot.",
   "1. Test each pair: can share → intersect; never → apart.\n2. All three share → three intersecting circles.\n3. Two share and the third is unrelated → two intersecting circles plus a separate one.\n\n*Why it works:* with no subsets, only the cross/apart choice matters for each pair.",
   "Teachers, Women, Singers.",
   "Every pair can share members → **three circles, each pair intersecting**."),
 P("vn-p16", "Mixed: inside plus crossing", "occasional",
   "One word is a kind of another and the third cuts across, or one sits inside the overlap of two.",
   "1. Draw the subset pair first.\n2. Test the third word against the inner and the outer circle separately.\n3. If the third word is a subset of two overlapping sets, place it inside their common part.\n\n*Why it works:* the third circle's relation to the inner circle can differ from its relation to the outer one.",
   "Fathers, Men, Doctors.",
   "Fathers ⊂ Men; a doctor can be a father or a man → **one inside another, third intersecting both**."),
]

PYQS = [
 PYQ("Two-set region count", "very common",
     "Two totals and the overlap; asks at least one, only one or neither.",
     "Union = A + B − both; neither = total − union; only A = A − both.",
     "two-set-operations",
     "In a class of 60, 35 like tea, 30 like coffee and 10 like both. How many like neither?",
     "35 + 30 − 10 = 55; 60 − 55 = **5**."),
 PYQ("Reverse two-set puzzle", "common",
     "Some regions are given; the overlap, a circle total or the group size is asked.",
     "Draw four boxes (only A, only B, both, neither), fill the known ones and solve for the gap.",
     "two-set-operations",
     "Everyone in a class of 80 plays chess or carrom; 50 play chess and 40 carrom. How many play both?",
     "50 + 40 − 80 = **10**."),
 PYQ("Percentage-based sets", "common",
     "Data in percent, answer in percent or in people.",
     "Solve in percent with total 100, convert to people at the end.",
     "two-set-operations",
     "70% watch cricket, 60% football, 40% both. What percent watch neither?",
     "Union 90% → neither **10%**."),
 PYQ("Maximum / minimum overlap", "occasional",
     "Overlap not given; asks its largest or smallest possible value.",
     "Max both = smaller set; min both = A + B − N (not below 0); max neither = N − larger set.",
     "two-set-operations",
     "80 people; 50 like cricket, 40 hockey. Maximum who like neither?",
     "Hockey inside cricket → neither = 80 − 50 = **30**."),
 PYQ("Three-set union / none", "very common",
     "Three totals, three pairs, the triple and a group size.",
     "Union = ΣA − Σpairs + triple; none = total − union.",
     "three-set-operations",
     "200 people: coffee 90, tea 80, milk 70; pairs 40, 35, 30; all three 15. How many drink none?",
     "Union 150 → none **50**."),
 PYQ("Exactly two / exactly one", "common",
     "Asks for exactly one, exactly two or at least two sets.",
     "Exactly two = Σpairs − 3 × triple; at least two = Σpairs − 2 × triple; exactly one = union − exactly two − triple.",
     "three-set-operations",
     "Pairs 8, 7, 6 and all three 3. Exactly two?",
     "21 − 9 = **12**."),
 PYQ("Reading a region diagram", "common",
     "Numbers are written in each region; the question describes a group in words.",
     "List the regions the phrase covers and add them once each; use total − regions for 'not' phrases.",
     "venn-idea",
     "Only N 20, only T 25, only R 5, N-T 15, T-R 6, N-R 4, all 10. How many use exactly one source?",
     "20 + 25 + 5 = **50**."),
 PYQ("Choose-the-diagram", "very common",
     "Three words; options describe circle pictures.",
     "For each pair decide inside / apart / cross by definition, then match all three marks to one picture.",
     "relation-diagrams",
     "Even numbers, Odd numbers, Prime numbers.",
     "Even and odd never meet; 2 and 3 are prime → **two separate circles, with the third intersecting both**."),
]
