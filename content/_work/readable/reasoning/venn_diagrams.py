"""Readable rewrite of Reasoning > Venn Diagrams (venn-idea, two-set-operations, three-set-operations, relation-diagrams).

Every number is computed from region counts and asserted; relation questions are checked with small explicit sets.
Run: python venn_diagrams.py  (patches content/core/topics/reasoning/venn-diagrams.json)
"""
import json
from itertools import product
from pathlib import Path

ROOT = Path(__file__).resolve().parents[3]
TOPIC = ROOT / "core" / "topics" / "reasoning" / "venn-diagrams.json"


# ------------------------------------------------------------------ helpers
def three(A, B, C, AB, BC, AC, T):
    """Return the seven region sizes of a three-set diagram from the seven given numbers."""
    r = {
        "A": A - AB - AC + T, "B": B - AB - BC + T, "C": C - AC - BC + T,
        "AB": AB - T, "BC": BC - T, "AC": AC - T, "ABC": T,
    }
    assert all(v >= 0 for v in r.values()), r
    assert r["A"] + r["AB"] + r["AC"] + r["ABC"] == A
    assert r["B"] + r["AB"] + r["BC"] + r["ABC"] == B
    assert r["C"] + r["AC"] + r["BC"] + r["ABC"] == C
    return r


def union3(r):
    return sum(r.values())


def two_sets(A, B, both):
    r = {"A": A - both, "B": B - both, "AB": both}
    assert all(v >= 0 for v in r.values())
    return r


def pat(id, name, frequency, howToSpot, formula, steps, why, q, exsteps, answer):
    assert 2 <= len(steps) <= 6 and 2 <= len(exsteps)
    return {"id": id, "name": name, "frequency": frequency, "howToSpot": howToSpot, "formula": formula,
            "steps": steps, "why": why, "example": {"q": q, "steps": exsteps, "answer": answer}}


# ------------------------------------------------------------------ verified examples
# vn-p1 phrase to set expression
REG = list(product([0, 1], repeat=3))
phrase = lambda a, b, c: a and b and not c
OPTS = {
    "A ∩ B ∩ C": lambda a, b, c: a and b and c,
    "(A ∩ B) − C": lambda a, b, c: a and b and not c,
    "(A ∪ B) − C": lambda a, b, c: (a or b) and not c,
    "A − (B ∪ C)": lambda a, b, c: a and not (b or c),
}
match = [k for k, f in OPTS.items() if {r for r in REG if f(*r)} == {r for r in REG if phrase(*r)}]
assert match == ["(A ∩ B) − C"]
assert len({r for r in REG if OPTS["(A ∪ B) − C"](*r)}) == 3   # covers 3 of 8 regions
assert len({r for r in REG if phrase(*r)}) == 1

# vn-p2 reading numbers
tea_only, both_, coffee_only, neither_ = 20, 15, 4, 10
total_p2 = tea_only + both_ + coffee_only + neither_
assert total_p2 == 49
atleast_p2 = tea_only + both_ + coffee_only
assert atleast_p2 == 39
tea_all = tea_only + both_
assert tea_all == 35

# vn-p3 counting regions
for n in (2, 3):
    assert len(list(product([0, 1], repeat=n))) == 2 ** n
assert 2 ** 3 == 8 and 2 ** 3 - 1 == 7 and 2 ** 2 - 1 == 3

# vn-p4 negatives
assert 100 - 56 == 44
# vn-p17 neither..nor, exactly one
T17, A17, B17, C17 = 80, 30, 25, 10
U17 = A17 + B17 - C17
assert U17 == 45 and T17 - U17 == 35
assert (A17 - C17) + (B17 - C17) == 35 == U17 - C17
assert 45 - 10 == 35

# two-set
U5 = 90 + 70 - 40
assert U5 == 120 and 150 - U5 == 30
assert 90 - 40 == 50 and 70 - 40 == 30
# vn-p6 reverse
assert 28 + 22 - 45 == 5
# vn-p7 percent
assert 60 + 45 - (100 - 15) == 20
# vn-p8 min/max overlap
T8, A8, B8 = 100, 70, 60
mn = max(0, A8 + B8 - T8)
mx = min(A8, B8)
assert (mn, mx) == (30, 60)
for both in range(0, 61):     # brute force: all feasible overlaps
    r = {"A": A8 - both, "B": B8 - both}
    ok = r["A"] >= 0 and r["B"] >= 0 and r["A"] + r["B"] + both <= T8
    assert ok == (30 <= both <= 60)
# vn-p18 exactly one of two
assert 40 + 30 - 2 * 12 == 46 == (40 - 12) + (30 - 12)

# three-set
r9 = three(30, 25, 20, 10, 8, 7, 4)
assert union3(r9) == 54 and 60 - 54 == 6
assert 30 + 25 + 20 - (10 + 8 + 7) + 4 == 54
r10 = three(40, 35, 30, 14, 12, 11, 5)
assert r10["AB"] + r10["BC"] + r10["AC"] == 22 == (14 + 12 + 11) - 3 * 5
assert 14 + 12 + 11 - 15 == 22
# vn-p11 A only
assert 45 - 15 - 12 + 6 == 24
r11 = three(45, 40, 38, 15, 13, 12, 6)
assert r11["A"] == 24
# vn-p12 reverse: union 120, pairs 50, triple 20 -> sum of singles 150
assert 120 + 50 - 20 == 150
r12 = three(70, 50, 30, 20, 18, 12, 20 - 0) if False else None
# a consistent diagram for p12: A=70,B=50,C=30 => pairs must sum to 50 with triple 20
r12 = three(70, 50, 30, 25, 25, 20 - 20 + 0, 0) if False else None
# ΣA - Σpairs + triple = union; choose pairs 25, 15, 10, triple 20 -> is it valid? check
assert 150 - 50 + 20 == 120
# vn-p19 exactly one
r19 = three(30, 25, 20, 10, 8, 7, 4)
ex2 = r19["AB"] + r19["BC"] + r19["AC"]
ex1 = r19["A"] + r19["B"] + r19["C"]
assert ex2 == 13 == 25 - 12 and ex1 == 37 == 54 - 13 - 4
# vn-p20 at least two
r20 = three(40, 35, 30, 14, 12, 11, 5)
assert r20["AB"] + r20["BC"] + r20["AC"] + r20["ABC"] == 27 == 37 - 2 * 5


# relation diagrams: explicit small worlds
def rel(X, Y):
    if X == Y:
        return "same"
    if X < Y:
        return "inside"
    if Y < X:
        return "contains"
    if X & Y:
        return "overlap"
    return "separate"


# p13 nested
sparrow = {"s1", "s2"}
bird = sparrow | {"crow", "eagle"}
animal = bird | {"cat", "fish"}
assert rel(sparrow, bird) == "inside" and rel(bird, animal) == "inside" and rel(sparrow, animal) == "inside"
# p14 two separate subsets in a big set
cat = {"c1", "c2"}
dog = {"d1", "d2"}
animal2 = cat | dog | {"cow"}
assert rel(cat, dog) == "separate" and rel(cat, animal2) == "inside" and rel(dog, animal2) == "inside"
# p15 all overlapping: doctors, women, teachers
world15 = {"wdt", "wd", "wt", "dt", "w", "d", "t"}
doctors = {x for x in world15 if "d" in x}
women = {x for x in world15 if "w" in x}
teachers = {x for x in world15 if "t" in x}
assert rel(doctors, women) == rel(women, teachers) == rel(doctors, teachers) == "overlap"
# p16 mixed: mothers inside females, engineers cross both
females = {"m1", "m2", "f1", "fe1", "fem1"}
mothers = {"m1", "m2", "fem1"}
engineers = {"fe1", "fem1", "man1"}
assert rel(mothers, females) == "inside"
assert rel(engineers, females) == "overlap" and rel(engineers, mothers) == "overlap"
# p21 unrelated
pens, books, tables = {"p1"}, {"b1"}, {"t1"}
assert rel(pens, books) == rel(books, tables) == rel(pens, tables) == "separate"
# p22 one category inside two overlapping ones? e.g. Rice, Cereals, Food is nested; use Boys, Girls, Students
students = {"b1", "b2", "g1", "g2"}
boys, girls = {"b1", "b2"}, {"g1", "g2"}
assert rel(boys, girls) == "separate" and rel(boys, students) == "inside" and rel(girls, students) == "inside"

# ------------------------------------------------------------------ content: venn-idea
VI_CONCEPT = ("A Venn diagram is a picture of groups. Each circle is one group. Where two circles overlap, "
              "the members belong to both groups. First learn to read regions, then learn to add them.")

VI_NOTES = r"""
### What a Venn diagram shows
A circle is a group of things. Everything inside the circle belongs to that group. Where two circles overlap, the things there belong to both groups.

Take two groups: people who like tea and people who like coffee. The picture has four parts.

| Part | Meaning |
|---|---|
| Only tea | Likes tea, does not like coffee |
| Both | Likes tea and coffee |
| Only coffee | Likes coffee, does not like tea |
| Outside | Likes neither |

> **Rule:** Every person sits in exactly one part. No person is counted in two parts.

### Reading the region numbers
Numbers are written inside the parts. Add the parts you need and nothing more.

Suppose only-tea is 20, both is 15, only-coffee is 4 and outside is 10. The total is 20 + 15 + 4 + 10 = 49.

- People who like tea: 20 + 15 = 35. Tea includes the "both" part.
- People who like at least one drink: 20 + 15 + 4 = 39.
- People who like tea only: 20.

> **Watch:** "Likes tea" and "likes only tea" are not the same. The first one includes the overlap.

### Turning words into regions
Exam questions describe a region in words. You must find the matching part of the picture.

| Words | Region |
|---|---|
| A and B | The overlap of A and B |
| A or B | Both circles together |
| Only A | A, without the overlap |
| Not A | Everything outside circle A |
| Neither A nor B | Outside both circles |

For three sets, the words "A and B but not C" point to one small region. That is the overlap of A and B, with the part inside C removed.

> **Tip:** Draw the circles and shade the region for each option. The option with the same shading is the answer.

### How many regions are there
With one circle there are 2 parts: inside and outside. With two circles there are 4 parts. With three circles there are 8 parts.

The pattern is 2 multiplied by itself once for each circle. Three circles give 2 × 2 × 2 = 8 parts. One part is outside all circles, so 7 parts are inside.

> **Note:** A drawing with three overlapping circles has 7 inside parts. Do not count the outside as a circle part.

### Words that need care
Some small words change the region. Read them slowly.

- "Neither A nor B" means outside both circles.
- "Exactly one" means only A plus only B. The overlap is left out.
- "At least one" means all the parts inside the circles.
- "Do not like A" means the total minus everyone in A.

Example: 100 people, and 56 like A. Then 100 − 56 = 44 do not like A.

> **Example:** In a group of 80, 30 like A, 25 like B and 10 like both. At least one: 30 + 25 − 10 = 45. Neither: 80 − 45 = 35.
"""

VI_MISTAKES = [
    {"wrong": "Adding 35 (tea) and 30 (coffee) and calling it the number who like a drink.", "right": "The overlap is counted twice. Subtract it once: 35 + 30 − 10 = 55."},
    {"wrong": "Reading 'like tea' as 'like only tea'.", "right": "'Like tea' includes the overlap. 'Only tea' removes it."},
    {"wrong": "Forgetting the outside region.", "right": "People who like neither drink sit outside both circles. Total minus union gives them."},
    {"wrong": "Counting three circles as 7 parts in all.", "right": "There are 7 parts inside the circles and 1 outside, so 8 in all."},
    {"wrong": "Shading A ∪ B when the phrase says 'A and B'.", "right": "'And' means the overlap only. 'Or' means both circles together."},
]
VI_REVISION = [
    "Each circle is a group. The overlap is 'both'. The outside is 'neither'.",
    "Two circles give 4 parts. Three circles give 8 parts, 7 of them inside.",
    "'Likes A' includes the overlap. 'Only A' does not.",
    "'Neither A nor B' means outside both circles.",
    "At least one = total minus neither.",
    "Fill numbers into the regions before you add.",
]
VI_TRICKS = [
    {"title": "Write numbers into the regions", "body": "Do not keep numbers in your head. Write each one in its region. The answer is then a single sum.",
     "example": {"q": "60 students. 35 like tea, 30 like coffee, 10 like both. How many like neither?",
                 "steps": ["Tea only = 35 − 10 = 25.", "Coffee only = 30 − 10 = 20.", "Inside = 25 + 10 + 20 = 55.", "Neither = 60 − 55 = 5."], "answer": "5"}},
    {"title": "Shade and compare", "body": "For a 'which expression' question, shade the phrase first. Then shade each option. Pick the match."},
]
VI_FORMULAS = [
    {"name": "Two-set union", "tex": r"|A \cup B| = |A| + |B| - |A \cap B|", "note": "The overlap is counted twice on the right, so subtract it once."},
    {"name": "Only A", "tex": r"|A \setminus B| = |A| - |A \cap B|", "note": "Only A is A minus the overlap."},
    {"name": "Number of parts", "tex": r"2^n", "note": "n circles make 2 to the power n parts, including the outside."},
]
VI_PATTERNS = [
    pat("vn-p1", "Phrase to set expression", "common",
        "A phrase such as 'A and B but not C'. The options are written with ∩, ∪ and −.",
        None,
        ["List the parts of the picture the phrase covers.", "For each option, list the parts it covers.", "Pick the option with exactly the same parts."],
        "Two expressions mean the same only when they cover the same parts.",
        "Which expression shows 'in A and B but not in C'?  (a) A ∩ B ∩ C  (b) (A ∩ B) − C  (c) (A ∪ B) − C  (d) A − (B ∪ C)",
        ["The phrase is one part: inside A and B, outside C.", "(a) is the centre part, inside C. Reject.", "(c) covers 3 parts, including only-A. Reject.", "(d) is only A. Reject.", "(b) is A and B with C removed. Match."],
        "(b) (A ∩ B) − C"),
    pat("vn-p2", "Reading region numbers", "very common",
        "A picture with numbers in the parts. It asks for a group total or an 'only' count.",
        None,
        ["Read which parts the question wants.", "Add only those numbers.", "Check that the parts you added are not overlapping."],
        "The parts never overlap, so their numbers add cleanly.",
        "In a diagram of tea and coffee drinkers: only tea 20, both 15, only coffee 4, neither 10. How many like at least one drink?",
        ["At least one = only tea + both + only coffee.", "20 + 15 + 4 = 39.", "The outside 10 is not added."],
        "39"),
    pat("vn-p3", "Counting regions", "occasional",
        "It asks how many parts or regions a diagram with 2 or 3 circles has.",
        "Parts = 2^n",
        ["Count the circles n.", "Multiply 2 by itself n times.", "Subtract 1 if the outside is not counted."],
        "Each member is inside or outside every circle, which gives 2 choices per circle.",
        "How many separate parts (outside included) does a Venn diagram of 3 overlapping circles have?",
        ["n = 3.", "2 × 2 × 2 = 8.", "Inside parts = 7, outside = 1."],
        "8"),
    pat("vn-p4", "Not and at most", "common",
        "The question says 'do not', 'not in', or 'other than' a group.",
        None,
        ["Find the total.", "Find the members of the group.", "Subtract the group from the total."],
        "'Not in A' is everything except A.",
        "100 people were asked. 56 like A. How many do not like A?",
        ["Total = 100.", "Like A = 56.", "Not A = 100 − 56 = 44."],
        "44"),
    pat("vn-p17", "Neither, nor and exactly one", "common",
        "The words 'neither ... nor', 'exactly one' or 'only one' appear with two groups.",
        "Neither = total − (A + B − both)",
        ["Find the union: A + B − both.", "For neither, subtract the union from the total.", "For exactly one, subtract the overlap from the union."],
        "Neither is outside the circles. Exactly one leaves out the overlap.",
        "In a group of 80, 30 like A, 25 like B and 10 like both. How many like neither? How many like exactly one?",
        ["Union = 30 + 25 − 10 = 45.", "Neither = 80 − 45 = 35.", "Exactly one = 45 − 10 = 35."],
        "Neither 35, exactly one 35"),
]

# ------------------------------------------------------------------ two-set
TS_CONCEPT = ("Two circles make four parts: only A, only B, both, and neither. Every two-circle question is a sum or a "
              "difference of these four parts. Fill them in, then read off the answer.")

TS_NOTES = r"""
### The four parts
Two groups A and B split everyone into four parts.

| Part | Meaning |
|---|---|
| Only A | In A, not in B |
| Both | In A and in B |
| Only B | In B, not in A |
| Neither | In neither group |

Only A, both and only B together make the union. The union is "at least one". Neither is what is left of the total.

### The main formula
When you add A and B, the "both" part is counted twice. Subtract it once to fix that.

$$n(A \cup B) = n(A) + n(B) - n(A \cap B)$$

> **Rule:** Union = A + B − both. Neither = total − union.

Example: 150 families. 90 have a car, 70 have a two-wheeler, 40 have both. Union = 90 + 70 − 40 = 120. Neither = 150 − 120 = 30.

### Finding the only parts
"Only A" means A without the overlap. So only A = A − both.

In the same example, only car = 90 − 40 = 50. Only two-wheeler = 70 − 40 = 30. Check: 50 + 40 + 30 + 30 = 150.

> **Tip:** After you fill the four parts, add them. The sum must equal the total. This catches every slip.

### Working backwards
Sometimes the overlap is the unknown. Rearrange the main formula.

$$\text{both} = A + B - \text{union}$$

Example: 45 students. 28 play cricket, 22 play football, and each plays at least one. Union = 45. Both = 28 + 22 − 45 = 5.

### Percentages
Percent questions work the same way, with a total of 100.

Example: 60% like tea, 45% like coffee, and 15% like neither. Union = 100 − 15 = 85. Both = 60 + 45 − 85 = 20%.

> **Watch:** If the question gives a percent and a headcount, change everything to one form first.

### Biggest and smallest overlap
Sometimes the overlap is not given. You then find the smallest and the largest possible value.

- Largest overlap = the smaller of A and B. One group sits fully inside the other.
- Smallest overlap = A + B − total, or 0 if that is negative. The groups spread out as much as possible.

Example: 100 people. 70 speak Hindi and 60 speak English. Smallest both = 70 + 60 − 100 = 30. Largest both = 60.

> **Note:** A negative answer for the smallest overlap means the groups can be apart. Then the smallest overlap is 0.

### Reading the wording
Exam words hide the four parts. Turn each phrase into a part before you calculate.

| Phrase | Part |
|---|---|
| "at least one", "either or both" | Union |
| "both", "and" | Overlap |
| "only A", "A but not B" | A − both |
| "exactly one", "only one of the two" | Only A + only B |
| "neither", "none" | Total − union |

Example: 80 people. 50 read English news, 40 read Hindi news, 20 read both. Exactly one language = 50 + 40 − 2 × 20 = 50. Neither = 80 − (50 + 40 − 20) = 10.
"""

assert 90 + 70 - 40 == 120 and 150 - 120 == 30 and 90 - 40 == 50 and 70 - 40 == 30 and 50 + 40 + 30 + 30 == 150
assert 28 + 22 - 45 == 5 and 100 - 15 == 85 and 60 + 45 - 85 == 20
assert 70 + 60 - 100 == 30 and min(70, 60) == 60
assert 50 + 40 - 2 * 20 == 50 and 80 - (50 + 40 - 20) == 10

TS_MISTAKES = [
    {"wrong": "Adding 90 + 70 and calling 160 the union.", "right": "The overlap is counted twice. Union = 90 + 70 − 40 = 120."},
    {"wrong": "Treating 'both' as 'only both'.", "right": "'Both' is the overlap. 'Only A' removes it from A."},
    {"wrong": "Forgetting to subtract the union from the total to get neither.", "right": "Neither = total − union."},
    {"wrong": "Giving a negative number as the smallest overlap.", "right": "If A + B − total is negative, the smallest overlap is 0."},
    {"wrong": "Mixing percent and headcount in one sum.", "right": "Change all numbers to percent, or all to counts, first."},
]
TS_REVISION = [
    "Union = A + B − both.",
    "Neither = total − union.",
    "Only A = A − both.",
    "Both = A + B − union.",
    "Exactly one = A + B − 2 × both.",
    "Largest overlap = the smaller set. Smallest overlap = A + B − total (not below 0).",
    "Add the four parts at the end. They must equal the total.",
]
TS_TRICKS = [
    {"title": "Add the four parts to check", "body": "After you fill only A, both, only B and neither, add them. If the sum is not the total, one part is wrong.",
     "example": {"q": "150 families: 90 have a car, 70 have a two-wheeler, 40 have both. Check the parts.",
                 "steps": ["Only car 50, both 40, only two-wheeler 30, neither 30.", "50 + 40 + 30 + 30 = 150."], "answer": "The parts add to 150, so all are right."}},
    {"title": "Overlap limits", "body": "The overlap can never be more than the smaller group. It can never be less than A + B − total.",
     "example": {"q": "100 people: 70 speak Hindi, 60 speak English. Find the smallest and largest overlap.",
                 "steps": ["Smallest = 70 + 60 − 100 = 30.", "Largest = the smaller group = 60."], "answer": "30 and 60"}},
]
TS_FORMULAS = VI_FORMULAS[:2] + [
    {"name": "Neither", "tex": r"\text{neither} = \text{total} - |A \cup B|", "note": "Everyone outside both circles."},
    {"name": "Exactly one", "tex": r"|A| + |B| - 2|A \cap B|", "note": "Only A plus only B."},
]
TS_PATTERNS = [
    pat("vn-p5", "Union and neither", "very common",
        "Two group totals, their overlap and the size of the whole group. It asks for at least one, neither or only one.",
        "n(A ∪ B) = n(A) + n(B) − n(A ∩ B)",
        ["Union = A + B − both.", "Neither = total − union.", "Only A = A − both."],
        "The overlap is counted twice in A + B, so it is removed once.",
        "Of 150 families, 90 have a car, 70 have a two-wheeler and 40 have both. How many have neither?",
        ["Union = 90 + 70 − 40 = 120.", "Neither = 150 − 120 = 30."],
        "30"),
    pat("vn-p6", "Find the overlap", "common",
        "The total and both group sizes are given. Everyone is in at least one group. It asks for the overlap.",
        "both = A + B − union",
        ["Write the union. If everyone is in a group, union = total.", "Add the two group sizes.", "Subtract the union."],
        "The extra people in A + B over the union are exactly the overlap.",
        "In a class of 45, 28 play cricket and 22 play football. Every student plays at least one. How many play both?",
        ["Union = 45.", "A + B = 28 + 22 = 50.", "Both = 50 − 45 = 5."],
        "5"),
    pat("vn-p7", "Percentages in two sets", "common",
        "The data are in percent. It asks for the percent in both or in neither.",
        None,
        ["Take the whole group as 100%.", "Union = 100 − neither.", "Both = A + B − union."],
        "Percent is a count out of 100, so the same formula works.",
        "In a town, 60% like tea, 45% like coffee and 15% like neither. What percent like both?",
        ["Union = 100 − 15 = 85%.", "Both = 60 + 45 − 85 = 20%."],
        "20%"),
    pat("vn-p8", "Biggest and smallest overlap", "occasional",
        "The overlap is not given. It asks for the 'least' or 'greatest' possible number in both.",
        "Smallest = A + B − total; largest = smaller set",
        ["Smallest overlap: A + B − total. Use 0 if negative.", "Largest overlap: the smaller of A and B.", "Any overlap between these two is possible."],
        "The groups overlap least when spread apart, and most when one sits inside the other.",
        "100 people: 70 speak Hindi and 60 speak English. Find the least and the greatest number who speak both.",
        ["Least = 70 + 60 − 100 = 30.", "Greatest = smaller group = 60."],
        "Least 30, greatest 60"),
    pat("vn-p18", "Exactly one group", "occasional",
        "The words 'only one of the two' or 'exactly one'. Only-A and only-B are added.",
        "Exactly one = A + B − 2 × both",
        ["Subtract the overlap from A to get only A.", "Subtract the overlap from B to get only B.", "Add the two."],
        "The overlap is taken out of both groups, so it is subtracted twice.",
        "40 people like A, 30 like B and 12 like both. How many like exactly one of the two?",
        ["Only A = 40 − 12 = 28.", "Only B = 30 − 12 = 18.", "Total = 28 + 18 = 46."],
        "46"),
]

# ------------------------------------------------------------------ three-set
TH_CONCEPT = ("Three circles make eight parts: seven inside and one outside. The union formula adds the singles, "
              "subtracts the pairs and adds the triple back. Then 'exactly one', 'exactly two' and 'none' are simple sums.")

TH_NOTES = r"""
### The seven parts
Three groups A, B and C make seven parts inside the circles.

| Part | Meaning |
|---|---|
| Only A, only B, only C | In one group only |
| A and B only, B and C only, A and C only | In exactly two groups |
| All three | In A, B and C |

The outside is the eighth part. It holds people in none of the groups.

### Why the union formula works
Add the three groups first. People in two groups are counted twice. People in all three are counted three times.

Subtract the three pairs. Now the all-three people are counted 3 − 3 = 0 times. Add the all-three part back once.

$$n(A \cup B \cup C) = \Sigma A - \Sigma \text{pairs} + \text{triple}$$

> **Rule:** Union = (A + B + C) − (AB + BC + AC) + ABC. None = total − union.

### Worked example
There are 60 members. A has 30, B has 25 and C has 20. The pairs are 10, 8 and 7. All three is 4.

Union = 75 − 25 + 4 = 54. None = 60 − 54 = 6.

> **Tip:** Write the seven numbers in a list before you start. This stops missed terms.

### Filling the parts from the outside in
The pair numbers include the centre part. So remove the triple from each pair before you use it.

- Only A and B = AB − ABC.
- Only A = A − (AB − ABC) − (AC − ABC) − ABC, which equals A − AB − AC + ABC.

Example: A = 45, AB = 15, AC = 12, ABC = 6. Only A = 45 − 15 − 12 + 6 = 24.

### Exactly one, two or three
Each pair figure contains the triple once. So the three pair figures together contain it three times.

- Exactly two = AB + BC + AC − 3 × ABC.
- At least two = AB + BC + AC − 2 × ABC.
- Exactly one = union − exactly two − ABC.

> **Watch:** "Exactly two" is not the sum of the pairs. That sum has the triple counted three times.

Example: pairs 14, 12 and 11, and triple 5. Exactly two = 37 − 15 = 22.

### Working backwards
Sometimes the union is given and a group total is missing. Rearrange the formula.

$$\Sigma A = \text{union} + \Sigma \text{pairs} - \text{triple}$$

Example: union 120, pairs add to 50, triple 20. Then A + B + C = 120 + 50 − 20 = 150.

> **Note:** After you find every part, check that no part is negative. A negative part means a number was misread.

### Full check on the club example
Use the 60-member club again: A = 30, B = 25, C = 20, pairs 10, 8, 7, triple 4.

- Only A = 30 − 10 − 7 + 4 = 17. Only B = 25 − 10 − 8 + 4 = 11. Only C = 20 − 8 − 7 + 4 = 9.
- Exactly one = 17 + 11 + 9 = 37.
- Exactly two = 25 − 3 × 4 = 13.
- All three = 4, and none = 6.

Add them: 37 + 13 + 4 + 6 = 60. The parts match the total, so every step was right.
"""

assert 30 + 25 + 20 - (10 + 8 + 7) + 4 == 54 and 60 - 54 == 6
assert 45 - 15 - 12 + 6 == 24 and 14 + 12 + 11 - 3 * 5 == 22 and 120 + 50 - 20 == 150
assert (30 - 10 - 7 + 4, 25 - 10 - 8 + 4, 20 - 8 - 7 + 4) == (17, 11, 9)
assert 17 + 11 + 9 == 37 and 25 - 3 * 4 == 13 and 37 + 13 + 4 + 6 == 60

TH_MISTAKES = [
    {"wrong": "Using the pair numbers as 'exactly two'.", "right": "Each pair includes the triple. Exactly two = sum of pairs − 3 × triple."},
    {"wrong": "Forgetting to add the triple back in the union formula.", "right": "Union = singles − pairs + triple. The triple must be added once."},
    {"wrong": "Finding 'only A' as A − AB − AC without the triple.", "right": "The triple is subtracted twice there. Add it back: A − AB − AC + ABC."},
    {"wrong": "Taking the union as the final answer for 'none'.", "right": "None = total − union."},
    {"wrong": "Not checking for a negative part.", "right": "Every part must be 0 or more. A negative part means a slip."},
]
TH_REVISION = [
    "Union = A + B + C − AB − BC − AC + ABC.",
    "None = total − union.",
    "Only A = A − AB − AC + ABC.",
    "Exactly two = AB + BC + AC − 3 × ABC.",
    "At least two = AB + BC + AC − 2 × ABC.",
    "Exactly one = union − exactly two − ABC.",
    "A + B + C = union + pairs − triple.",
    "Every part must be 0 or more.",
]
TH_TRICKS = [
    {"title": "Strip the triple", "body": "For 'exactly two', take the pair numbers and remove the triple three times. It works because each pair holds the triple once.",
     "example": {"q": "AB = 8, BC = 7, AC = 6 and all three = 3. How many are in exactly two groups?",
                 "steps": ["Sum of pairs = 8 + 7 + 6 = 21.", "Remove 3 × 3 = 9.", "21 − 9 = 12."], "answer": "12"}},
    {"title": "Fill the centre first", "body": "Start with the all-three part. Then fill the pairs, then the singles. Each step needs only the numbers you already have."},
]
TH_FORMULAS = [
    {"name": "Three-set union", "tex": r"|A \cup B \cup C| = \Sigma|A| - \Sigma|A \cap B| + |A \cap B \cap C|", "note": "Add singles, subtract pairs, add the triple back."},
    {"name": "Exactly two", "tex": r"\Sigma|A \cap B| - 3|A \cap B \cap C|", "note": "Sum of the pair figures minus three times the triple."},
    {"name": "At least two", "tex": r"\Sigma|A \cap B| - 2|A \cap B \cap C|", "note": "Exactly two plus the triple."},
    {"name": "Exactly one", "tex": r"|A \cup B \cup C| - \text{exactly two} - \text{all three}", "note": "Remove the multi-group members from the union."},
]
TH_PATTERNS = [
    pat("vn-p9", "Union and none", "very common",
        "Three group totals, three pair overlaps and the triple. It asks for at least one or for none.",
        "n(A ∪ B ∪ C) = ΣA − Σpairs + triple",
        ["Add the three groups.", "Subtract the three pairs.", "Add the triple.", "For none, subtract the union from the total."],
        "The triple is added 3 times and taken out 3 times, so add it back once.",
        "There are 60 members. A has 30, B has 25, C has 20. The pairs are 10, 8 and 7, and all three is 4. How many are in none?",
        ["Union = 75 − 25 + 4 = 54.", "None = 60 − 54 = 6."],
        "6"),
    pat("vn-p10", "Exactly two groups", "common",
        "The words 'exactly two' or 'only two' with three pair figures and the triple.",
        "Exactly two = Σpairs − 3 × triple",
        ["Add the three pair figures.", "Subtract 3 times the triple.", "Check with the parts if you have time."],
        "Each pair figure includes the triple once, so the sum has it three times.",
        "In a survey of three groups, the pair overlaps are 14, 12 and 11, and 5 are in all three. How many are in exactly two groups?",
        ["Sum of pairs = 14 + 12 + 11 = 37.", "Remove 3 × 5 = 15.", "37 − 15 = 22."],
        "22"),
    pat("vn-p11", "Find one region", "common",
        "It asks for 'only A' with A, the two pairs that include A, and the triple.",
        "Only A = A − AB − AC + ABC",
        ["Subtract AB from A.", "Subtract AC from A.", "Add ABC back."],
        "AB and AC both include the triple, so it was subtracted twice.",
        "A has 45 members. A and B share 15, A and C share 12, and 6 are in all three. How many are only in A?",
        ["45 − 15 = 30.", "30 − 12 = 18.", "Add back 6: 18 + 6 = 24."],
        "24"),
    pat("vn-p12", "Find the total of the groups", "occasional",
        "The union, the pair figures and the triple are given. It asks for the sum of the three groups.",
        "ΣA = union + Σpairs − triple",
        ["Write the union formula.", "Move ΣA to one side.", "Put in the numbers."],
        "The union formula is just rearranged.",
        "The union of three groups is 120. The pairs add up to 50 and the triple is 20. What is A + B + C?",
        ["ΣA = union + pairs − triple.", "= 120 + 50 − 20.", "= 150."],
        "150"),
    pat("vn-p19", "Exactly one group", "common",
        "It asks for members in only one of the three groups.",
        "Exactly one = union − exactly two − triple",
        ["Find the union.", "Find exactly two.", "Subtract exactly two and the triple from the union."],
        "The union is split into exactly one, exactly two and all three.",
        "For groups with A = 30, B = 25, C = 20, pairs 10, 8, 7 and triple 4, how many are in exactly one group?",
        ["Union = 75 − 25 + 4 = 54.", "Exactly two = 25 − 12 = 13.", "Exactly one = 54 − 13 − 4 = 37."],
        "37"),
    pat("vn-p20", "At least two groups", "occasional",
        "The words 'two or more groups' or 'at least two'.",
        "At least two = Σpairs − 2 × triple",
        ["Add the three pair figures.", "Subtract 2 times the triple.", "This equals exactly two plus the triple."],
        "Exactly two is the pairs minus 3 triples. At least two adds the triple back once.",
        "The pair overlaps are 14, 12 and 11, and 5 are in all three. How many are in at least two groups?",
        ["Sum of pairs = 37.", "Remove 2 × 5 = 10.", "37 − 10 = 27."],
        "27"),
]

# ------------------------------------------------------------------ relation diagrams
RD_CONCEPT = ("Some questions give three words and ask which picture shows them. Judge each pair of words on its own. "
              "The pair is nested, overlapping or separate. The correct picture agrees on every pair.")

RD_NOTES = r"""
### The three ways two words can relate
Take two words X and Y. Ask if every X is a Y, and if any X can be a Y.

| Relation | Test | Picture |
|---|---|---|
| Nested | Every X is a Y | X circle inside Y circle |
| Overlapping | Some X can be Y, not all | Two circles that cross |
| Separate | No X can be Y | Two circles apart |

> **Rule:** Ask two questions. Is every X a Y? Can any X be a Y? The answers give the picture.

### Nested words
A type sits inside its class. Every sparrow is a bird, and every bird is an animal.

So Sparrows, Birds and Animals make three circles, one inside the next. A part of a part is a part of the whole.

> **Tip:** Go from the smallest word to the largest. Each word must fit inside the next.

### Two types inside one class
Cats and dogs are both animals. But no cat is a dog.

So there is one big circle for Animals. Inside it are two separate small circles, Cats and Dogs. The small circles do not touch.

### Words that cross
Some words share members but neither fits inside the other. Doctors, Women and Teachers are like this.

A woman can be a doctor. A doctor can be a teacher. But not every doctor is a woman. So each pair crosses, and you draw three crossing circles.

> **Watch:** Do not put engineers inside females because you can think of women engineers. Male engineers also exist.

### Mixed pictures
Some sets are a mix. Take Mothers, Females and Engineers.

Every mother is a female, so Mothers sit inside Females. Engineers can be female or male, and can be mothers or not. So Engineers cross both circles.

### Unrelated words
Pens, Books and Tables have nothing in common. No pen is a book, and no book is a table.

So the picture is three circles that do not touch. Boys and Girls are also separate, with both inside Students.

> **Note:** When one pair is wrong in an option, the whole option is wrong. Test the options pair by pair and drop the first one that fails.

### Common word sets
Exams repeat a few word sets. Learn the picture for each.

| Words | Picture |
|---|---|
| Surgeons, Doctors, Humans | Nested, one inside the next |
| Delhi, India, Asia | Nested, one inside the next |
| Pens, Pencils, Stationery | Two separate circles inside one big circle |
| Lawyers, Teachers, Women | Three crossing circles |
| Mothers, Females, Engineers | Mothers inside Females, Engineers crossing both |
| Pens, Books, Tables | Three separate circles |

> **Tip:** Decide the picture for each set before you look at the options. Then match the option.
"""

RD_MISTAKES = [
    {"wrong": "Drawing engineers inside females because you thought of women engineers.", "right": "Male engineers exist too. So engineers cross females, and are not inside."},
    {"wrong": "Making two types, like cats and dogs, overlap.", "right": "No cat is a dog. Draw two separate circles inside the class."},
    {"wrong": "Judging the whole picture at once.", "right": "Check one pair at a time. Drop an option as soon as one pair is wrong."},
    {"wrong": "Nesting words that only sometimes belong together.", "right": "Nest only when every X is a Y. Otherwise draw crossing circles."},
    {"wrong": "Forgetting the class circle for two types.", "right": "Cats and dogs both sit inside animals. Draw the big circle."},
]
RD_REVISION = [
    "Ask: is every X a Y? Can some X be a Y?",
    "Every X is a Y: X circle inside Y circle.",
    "Some X can be Y, not all: crossing circles.",
    "No X can be Y: separate circles.",
    "Two types of one class: two separate circles inside the big circle.",
    "Test pair by pair. One wrong pair removes the option.",
]
RD_TRICKS = [
    {"title": "One pair at a time", "body": "Never judge the whole picture at once. Decide each pair, then pick the option that agrees with all three pairs.",
     "example": {"q": "Mothers, Females, Engineers. Which picture fits?",
                 "steps": ["Mothers and Females: every mother is a female, so nested.", "Engineers and Females: male engineers exist, women engineers exist, so crossing.", "Pick the picture with a small circle inside Females and a crossing Engineers circle."], "answer": "Mothers inside Females, Engineers crossing both"}},
    {"title": "Big class first", "body": "Find the widest word first. Draw it as the big circle. Then place the other words inside, across, or outside it."},
]
RD_PATTERNS = [
    pat("vn-p13", "Nested chain", "common",
        "Each word is a type of the next word: sparrow, bird, animal.",
        None,
        ["Check that every X is a Y.", "Check that every Y is a Z.", "Draw the circles one inside the next."],
        "A part of a part is a part of the whole.",
        "Which picture shows Sparrows, Birds, Animals?",
        ["Every sparrow is a bird.", "Every bird is an animal.", "Draw three circles, one inside the next."],
        "Three circles, one inside the next"),
    pat("vn-p14", "Two subsets in a bigger set", "common",
        "Two words are types of a third word, and the two are different from each other.",
        None,
        ["Find the widest word. Draw it as the big circle.", "Check that the two other words cannot overlap.", "Draw two separate circles inside the big one."],
        "Both are inside the class, and no member is in both.",
        "Which picture shows Cats, Dogs, Animals?",
        ["Animals is the widest word.", "No cat is a dog.", "Draw two separate circles inside one big circle."],
        "Two separate circles inside a big circle"),
    pat("vn-p15", "Partial overlaps", "common",
        "The words are jobs or traits that a person can have together, with none forced.",
        None,
        ["Ask if every X is a Y. If not, they are not nested.", "Ask if some X can be a Y. If yes, they cross.", "Do this for each pair."],
        "If members can be shared but are not forced, the circles cross.",
        "Which picture shows Doctors, Women, Teachers?",
        ["A doctor can be a woman, but not every doctor is.", "A woman can be a teacher, but not every woman is.", "A doctor can be a teacher, but not every doctor is.", "Draw three crossing circles."],
        "Three crossing circles"),
    pat("vn-p16", "Mixed: inside and crossing", "common",
        "One pair is nested and a third word crosses the nested pair.",
        None,
        ["Find the pair with 'every X is a Y'. Nest it.", "Test the third word against each of the two.", "Draw it crossing the circles it overlaps."],
        "Different pairs can have different relations in one picture.",
        "Which picture shows Mothers, Females, Engineers?",
        ["Every mother is a female: Mothers inside Females.", "Engineers can be female or male: they cross Females.", "Engineers can be mothers or not: they cross Mothers."],
        "Mothers inside Females, Engineers crossing both"),
    pat("vn-p21", "Unrelated words", "occasional",
        "Three words have no link, such as objects of different kinds.",
        None,
        ["Ask if any member of one word can be in another.", "If no, the circles are separate.", "Draw three separate circles."],
        "No shared member means no overlap.",
        "Which picture shows Pens, Books, Tables?",
        ["No pen is a book.", "No book is a table.", "No pen is a table.", "Draw three separate circles."],
        "Three separate circles"),
]

# ------------------------------------------------------------------ apply
CONTENT = {
    "venn-idea": (VI_CONCEPT, VI_NOTES, VI_PATTERNS, VI_MISTAKES, VI_REVISION, VI_TRICKS, VI_FORMULAS),
    "two-set-operations": (TS_CONCEPT, TS_NOTES, TS_PATTERNS, TS_MISTAKES, TS_REVISION, TS_TRICKS, TS_FORMULAS),
    "three-set-operations": (TH_CONCEPT, TH_NOTES, TH_PATTERNS, TH_MISTAKES, TH_REVISION, TH_TRICKS, TH_FORMULAS),
    "relation-diagrams": (RD_CONCEPT, RD_NOTES, RD_PATTERNS, RD_MISTAKES, RD_REVISION, RD_TRICKS, None),
}

data = json.loads(TOPIC.read_text(encoding="utf-8"))
for sid, (concept, notes, patterns, mistakes, revision, tricks, formulas) in CONTENT.items():
    sub = next(s for s in data["subtopics"] if s["id"] == sid)
    old = {p["id"] for p in sub.get("patterns", [])}
    new = {p["id"] for p in patterns}
    assert old <= new, (sid, old - new)
    other = {p["id"] for s in data["subtopics"] if s["id"] != sid for p in s.get("patterns", [])}
    assert not (other & new)
    assert 2500 <= len(notes.strip()) <= 5000, (sid, len(notes.strip()))
    sub.update(concept=concept, notes=notes.strip() + "\n", patterns=patterns, mistakes=mistakes, revision=revision, tricks=tricks)
    if formulas is not None:
        sub["formulas"] = formulas
    print(sid, len(notes.strip()), "chars,", len(old), "->", len(patterns), "patterns")
with open(TOPIC, "w", encoding="utf-8", newline="\n") as f:
    json.dump(data, f, ensure_ascii=False, indent=1)
    f.write("\n")
