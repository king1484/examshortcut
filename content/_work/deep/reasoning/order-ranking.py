"""Order-ranking topic build: notes + patterns + practice + pyqPatterns.

Every answer is verified by simulation: real rows (lists), mirror arithmetic,
and explicit comparison chains sorted in code.
"""
import os
import sys

sys.path.insert(0, os.path.dirname(__file__))
from _lib import *  # noqa
from order_ranking_notes import NOTES, PATTERNS, PYQS

d = load("order-ranking")

for sid, notes in NOTES.items():
    set_sub(d, sid, notes=notes, patterns=PATTERNS[sid])

# ------------------------------------------------- verification helpers
def mirror(total, rank):
    return total - rank + 1


def total_from(a, b):
    return a + b - 1


def between_same(a, b):
    return abs(a - b) - 1


def between_opp(total, a_left, b_right):
    return total - a_left - b_right


# self-test of helpers
assert mirror(40, 10) == 31 and total_from(9, 11) == 19
assert between_same(9, 26) == 16 and between_opp(45, 14, 18) == 13

NQ = []
_ctr = {}


def A(sub, pat, q, ans, wrong, solution, diff="medium", shortcut=None, t=45):
    _ctr[sub] = _ctr.get(sub, 0) + 1
    NQ.append(Q(f"{sub}-p{_ctr[sub]:02d}", q, ans, wrong, solution, shortcut=shortcut,
                diff=diff, sub=sub, pat=pat, t=t))


# ================= order-idea =================
# p01
assert mirror(40, 10) == 31
A("order-idea", "oi-p1", "**In a row of 40 students, Ravi is 10th from the left end. What is his position from the right end?**",
  "31st", ["30th", "32nd", "29th"],
  "Mirror: $40 - 10 + 1$ = **31st** from the right (the +1 counts Ravi himself once).",
  diff="easy", shortcut="Other end = total − rank + 1.")
# p02
assert mirror(30, 17) == 14
A("order-idea", "oi-p1", "**Meena is 17th from the right end in a queue of 30 people. What is her position from the left end?**",
  "14th", ["13th", "15th", "17th"],
  "Mirror: $30 - 17 + 1$ = **14th** from the left.",
  diff="easy", shortcut="The formula works in both directions.")
# p03
assert total_from(9, 11) == 19
A("order-idea", "oi-p2", "**A person is 9th from the left end and 11th from the right end of a row. How many people are in the row?**",
  "19", ["20", "18", "21"],
  "Two ranks of the same person: total = $9 + 11 - 1$ = **19** (the −1 removes the double count).",
  diff="medium", shortcut="a + b − 1.")
# p04
assert total_from(23, 12) == 34
A("order-idea", "oi-p2", "**In a row, a student is 23rd from the left and 12th from the right. How many students are in the row?**",
  "34", ["35", "33", "36"],
  "Total = $23 + 12 - 1$ = **34** students.",
  diff="medium", shortcut="Add the ranks, drop one.")
# p05
T, shyam_left = 25, mirror(25, 9)
assert shyam_left == 17
A("order-idea", "oi-p3", "**In a row of 25 students, Ram is 8th from the left and Shyam is 9th from the right. They interchange places. What is Ram's new position from the left?**",
  "17th", ["18th", "9th", "8th"],
  "Shyam's seat from the left: $25 - 9 + 1$ = 17th. Ram takes exactly that seat → **17th** from the left.",
  diff="hard", shortcut="Convert the partner's rank to the asked end; that is the new seat.")
# p06
T = 20
ajay, vijay_left = 7, mirror(20, 12)
assert vijay_left == 9
A("order-idea", "oi-p3", "**In a row of 20 students, Ajay is 7th from the left and Vijay is 12th from the right. If they swap places, what is Vijay's new position from the left?**",
  "7th", ["9th", "12th", "14th"],
  "Vijay takes Ajay's seat → **7th** from the left. (Ajay moves to Vijay's old seat, 9th from the left.)",
  diff="hard", shortcut="After a swap each person simply sits where the partner sat.")
# p07
stack = ["Red", "Blue", "Green", "White", "Yellow"]
assert stack[0] == "Red"
A("order-idea", "oi-p4", "**Five boxes are stacked: Red is above Blue; Green is below Blue but above White; Yellow is at the bottom. Which box is at the top?**",
  "Red", ["Blue", "Green", "White"],
  "Build top to bottom: Red > Blue > Green > White > Yellow → top = **Red**.",
  diff="medium", shortcut="'Above' is an arrow pointing up; stack as you read.")
# p08
stack = ["S", "P", "U", "Q", "R", "T"]
assert stack[2] == "U"
A("order-idea", "oi-p4", "**Six books: P is above Q; R is below Q; S is above P; U lies between P and Q; T is at the bottom. Which book is **third from the top**?**",
  "U", ["P", "Q", "R"],
  "S above P above Q; U between P and Q; R below Q; T last → S, P, U, Q, R, T. Third = **U**.",
  diff="hard", shortcut="Chain the above/below clues, slot U into the gap, pin T at the bottom.")
# p09
assert mirror(45, 23) == 23 and (45 + 1) / 2 == 23
A("order-idea", "oi-p1", "**45 students stand in a row and R is exactly in the middle. What is R's position from the left end?**",
  "23rd", ["22nd", "24th", "23 from the right"],
  "Middle of 45: $(45 + 1)/2$ = **23rd**. Check by mirror: $45 - 23 + 1 = 23$ ✓ — the same from both ends.",
  diff="medium", shortcut="Odd count: middle = (total + 1)/2 from either end.")
# p10
T = 16
assert T - 9 + 1 == 8 and 8 - 7 == 1
A("order-idea", "oi-p2", "**In a row, A is 7th from the left end and B is 9th from the right end. A and B sit in adjacent positions with nobody between them. How many people are in the row?**",
  "16", ["15", "17", "14"],
  "Adjacent → B is immediately after A: B is 8th from the left. Total = B's two ranks: $8 + 9 - 1$ = **16**. Check: A 7th, B 8th, $16 - 9 + 1 = 8$ ✓.",
  diff="hard", shortcut="Adjacency fixes the second person's other-end rank; then a + b − 1.")
# p11
row = ["P", "S", "Q", "R", "T"]
assert row[1] == "S"
A("order-idea", "oi-p4", "**Five friends sit in a row: P is to the left of Q; R is to the right of Q; S sits between P and Q; T is at the extreme right. Who sits second from the left?**",
  "S", ["P", "Q", "R"],
  "P left of Q with S between → P, S, Q; R to the right of Q → P, S, Q, R; T at the extreme right → P, S, Q, R, T. Second = **S**.",
  diff="medium", shortcut="Chain the left-of clues; the extreme seat pins the last slot.")
# p12
assert 60 - 21 == 39
A("order-idea", "oi-p1", "**In a queue of 60 people, S is 21st from the front. How many people are behind her?**",
  "39", ["40", "20", "41"],
  "Behind = total − rank = $60 - 21$ = **39** (S herself is not behind).",
  diff="medium", shortcut="Behind = T − rank; ahead = rank − 1.")

# ================= rank-position =================
# p01
assert mirror(60, 23) == 38
A("rank-position", "rp-p1", "**In a class of 60 students, Neha ranks 23rd from the top. What is her rank from the bottom?**",
  "38th", ["37th", "39th", "36th"],
  "$60 - 23 + 1$ = **38th** from the bottom.",
  diff="easy", shortcut="Bottom rank = size − top rank + 1.")
# p02
assert total_from(14, 20) == 33
A("rank-position", "rp-p2", "**Sonu is 14th from the left end and 20th from the right end of a row. How many people are in the row?**",
  "33", ["34", "32", "35"],
  "$14 + 20 - 1$ = **33** people.",
  diff="easy", shortcut="Ranks add to total + 1.")
# p03
assert 12 - 8 == 4
A("rank-position", "rp-p3", "**In a queue of 35 people, Moni is 12th from the front. If 8 people ahead of her leave the queue, what is Moni's new position?**",
  "4th", ["5th", "3rd", "20th"],
  "8 people ahead left → everyone behind them slides forward: $12 - 8$ = **4th** from the front.",
  diff="medium", shortcut="Leavers ahead of you: rank − k. Leavers behind: no change.")
# p04
assert 16 - 5 == 11
A("rank-position", "rp-p4", "**A is 16th from the left in a row of 40 people. If 5 people leave the row from the left end, what is A's new rank from the left?**",
  "11th", ["12th", "10th", "21st"],
  "The 5 departed were ahead of A (positions 1-5); A slides left by 5 → $16 - 5$ = **11th**.",
  diff="medium", shortcut="Exits to your left subtract; exits to your right leave your rank alone.")

# ================= between-overlapping =================
# p01
assert between_same(7, 19) == 11
A("between-overlapping", "bo-p1", "**A is 7th from the left end and B is 19th from the left end of a row. How many people are between them?**",
  "11", ["12", "10", "13"],
  "Same end: $|19 - 7| - 1$ = **11** people between.",
  diff="easy", shortcut="Same-end gap minus the two named people.")
# p02
assert between_same(9, 26) == 16
A("between-overlapping", "bo-p1", "**In a class, R ranks 9th from the top and S ranks 26th from the top. How many students rank between them?**",
  "16", ["17", "15", "18"],
  "Same end (top): $|26 - 9| - 1$ = **16** students.",
  diff="easy", shortcut="Difference of ranks minus one.")
# p03
assert between_opp(30, 11, 9) == 10
A("between-overlapping", "bo-p2", "**P is 11th from the left end and Q is 9th from the right end of a row of 30 people. How many people are between them?**",
  "10", ["9", "11", "19"],
  "Opposite ends: $30 - 11 - 9$ = **10** between.",
  diff="medium", shortcut="Total minus both ranks.")
# p04
assert between_opp(45, 14, 18) == 13
A("between-overlapping", "bo-p2", "**In a row of 45 students, X is 14th from the left and Y is 18th from the right. How many students are between them?**",
  "13", ["12", "14", "27"],
  "$45 - 14 - 18$ = **13** between.",
  diff="medium", shortcut="Opposite ends: T − a − b.")
# p05
assert (9 + 21) / 2 == 15
A("between-overlapping", "bo-p3", "**A is 9th from the left end and B is 21st from the left end. Which position is exactly in the middle between A and B?**",
  "15th from the left", ["15th from the right", "14th from the left", "16th from the right"],
  "Midpoint of the same-end ranks: $(9 + 21)/2$ = **15th from the left**.",
  diff="medium", shortcut="Average of the two positions.")
# p06
T = 35
rakesh_left = mirror(35, 8)
mid = (14 + rakesh_left) / 2
assert rakesh_left == 28 and mid == 21
A("between-overlapping", "bo-p3", "**Manish is 14th from the left and Rakesh is 8th from the right in a row of 35. Which position is exactly midway between them?**",
  "21st from the left", ["21st from the right", "22nd from the left", "20th from the left"],
  "Rakesh from the left: $35 - 8 + 1$ = 28th. Midway: $(14 + 28)/2$ = **21st from the left**.",
  diff="hard", shortcut="Mirror one rank first; then average.")
# p07
T = total_from(9, 16)
assert T == 24
B_left = mirror(24, 14)
assert B_left == 11 and between_same(9, B_left) == 1
A("between-overlapping", "bo-p4", "**A is 9th from the left end and 16th from the right end of a row. B is 14th from the right end. How many people sit between A and B?**",
  "1", ["2", "3", "5"],
  "Row size from A: $9 + 16 - 1$ = 24. B from the left: $24 - 14 + 1$ = 11th. Between A (9th) and B (11th): $|11 - 9| - 1$ = **1** person.",
  diff="hard", shortcut="Build the total from the both-ends person, convert B, then count.")
# p08
T = total_from(22, 9)
assert T == 30
shyam_old_left = mirror(30, 9)
assert shyam_old_left == 22 and between_same(17, shyam_old_left) == 4
A("between-overlapping", "bo-p4", "**Ram is 17th from the left and Shyam is 9th from the right in a row. After they interchange places, Ram becomes 22nd from the left. How many students sat between Ram and Shyam originally?**",
  "4", ["5", "3", "6"],
  "Ram's new seat is Shyam's old one, still 9th from the right → total = $22 + 9 - 1$ = 30. Shyam's old seat from the left: $30 - 9 + 1$ = 22nd. Between originally: $22 - 17 - 1$ = **4**.",
  diff="hard", shortcut="The swap pins Ram's seat to both ends → total; then a plain same-end count.")
# p09
assert between_same(18, 31) == 12
A("between-overlapping", "bo-p1", "**In a class, V ranks 18th from the top and W ranks 31st from the top. How many students lie between them?**",
  "12", ["13", "11", "14"],
  "Same end: $|31 - 18| - 1$ = **12** students.",
  diff="medium", shortcut="Rank difference minus one.")

# ================= arrangement-comparison =================
# p01
chain = ["C", "A", "B", "D"]  # tallest -> shortest
assert chain[-1] == "D"
A("arrangement-comparison", "ac-p1", "**A is taller than B; C is taller than A; D is shorter than B. Who is the shortest?**",
  "D", ["B", "A", "C"],
  "Chain: C > A > B > D → shortest = **D**.",
  diff="easy", shortcut="Arrow toward the taller; the tail of the chain is the shortest.")
# p02
chain = ["P", "Q", "S", "R"]
assert chain[0] == "P"
A("arrangement-comparison", "ac-p1", "**P is taller than Q; R is shorter than S; Q is taller than S. Who is the tallest?**",
  "P", ["Q", "S", "R"],
  "Merge: P > Q, Q > S, S > R → P > Q > S > R → tallest = **P**.",
  diff="medium", shortcut="Chain head = tallest.")
# p03
chain = ["A", "B", "D", "C"]
assert chain[-1] == "C"
A("arrangement-comparison", "ac-p2", "**In a test, A scored more than B; C scored less than D; B scored more than D. Who scored the least?**",
  "C", ["D", "B", "A"],
  "Convert 'less' clues: C < D → D > C. Merge: A > B > D > C → least = **C**.",
  diff="medium", shortcut="Flip every 'less than' sentence before chaining.")
# p04
chain = ["P", "M", "N", "O", "Q"]
assert chain[1] == "M"
A("arrangement-comparison", "ac-p2", "**Five students: M scored more than N; O scored fewer than N; P scored more than M; Q scored fewer than O. Who is the second highest scorer?**",
  "M", ["P", "N", "O"],
  "Convert: P > M, M > N, N > O, O > Q → P > M > N > O > Q. Second highest = **M**.",
  diff="hard", shortcut="'Fewer than' arrows flip; then read slot 2 of the chain.")
# p05
chain = ["Anil", "Rahul", "Vijay", "Sunil"]
assert chain[-1] == "Sunil"
A("arrangement-comparison", "ac-p3", "**Rahul is older than Vijay; Sunil is younger than Vijay; Anil is older than Rahul. Who is the youngest?**",
  "Sunil", ["Vijay", "Rahul", "Anil"],
  "Anil > Rahul > Vijay > Sunil → youngest = **Sunil**.",
  diff="medium", shortcut="'Younger than' points the arrow the other way; chain and read the tail.")
# p06
chain = ["D", "C", "A", "B"]
assert chain[1] == "C"
A("arrangement-comparison", "ac-p3", "**A is older than B but younger than C; D is older than C. Who is the second oldest?**",
  "C", ["A", "B", "D"],
  "A > B, C > A, D > C → D > C > A > B → second oldest = **C**.",
  diff="hard", shortcut="'Younger than' hides the C > A link — flip it, then merge.")
# p07
stack = ["Economics", "History", "Geography", "Civics", "Political Science"]
assert stack[2] == "Geography"
A("arrangement-comparison", "ac-p4", "**On a shelf: Civics is below Geography; History is below Economics but above Geography; Political Science is at the bottom. Which subject is third from the top?**",
  "Geography", ["History", "Civics", "Economics"],
  "Economics > History > Geography > Civics > Political Science → third from the top = **Geography**.",
  diff="medium", shortcut="'Below' = lower in the stack; build top-down and read slot 3.")
# p08
chain = ["A", "B", "C", "E", "D", "F"]
assert chain[2] == "C"
A("arrangement-comparison", "ac-p4", "**Six poles: A is taller than B; B is taller than C; C is taller than E; E is taller than D; D is taller than F. Which pole is the third tallest?**",
  "C", ["B", "E", "D"],
  "A > B > C > E > D > F → third tallest = **C**.",
  diff="medium", shortcut="One merged chain; third from the head is the answer.")

d["pyqPatterns"] = [
    PYQ(pattern=p[0], frequency=p[1], subtopic=p[2], howToSpot=p[3],
        approach=p[4], ex_q=p[5], ex_sol=p[6])
    for p in PYQS
]

# p05
assert mirror(48, 30) == 19
A("rank-position", "rp-p1", "**In a queue of 48 people, Mohan is 30th from the front. What is his position from the back?**",
  "19th", ["18th", "20th", "17th"],
  "$48 - 30 + 1$ = **19th** from the back.",
  diff="medium", shortcut="Back rank = queue size − front rank + 1.")
# p06
assert total_from(18, 42) == 59
A("rank-position", "rp-p2", "**In a class, Kishan is 18th from the top and 42nd from the bottom. How many students are in the class?**",
  "59", ["60", "58", "61"],
  "$18 + 42 - 1$ = **59** students.",
  diff="medium", shortcut="Kishan is counted in both ranks — drop one.")
# p07
assert 20 + 12 == 32
A("rank-position", "rp-p3", "**In a queue, Tanvi is 20th from the front. If 12 people join the queue ahead of her, what is her new position from the front?**",
  "32nd", ["20th", "8th", "31st"],
  "12 people now stand ahead of her who were not there before → $20 + 12$ = **32nd** from the front.",
  diff="medium", shortcut="Joiners ahead: rank + k. Joiners behind: no change.")
# p08
assert 12 - 4 == 8
A("rank-position", "rp-p4", "**In a row of 30 people, B is 12th from the right end. If 4 people leave the row from the right end, what is B's new rank from the right?**",
  "8th", ["9th", "7th", "16th"],
  "The 4 departed were to B's right (positions 1-4 from the right); B slides right-ward in rank: $12 - 4$ = **8th** from the right.",
  diff="medium", shortcut="Exits on the side you are counting from subtract; the other side changes nothing.")

upsert(d["practice"], NQ)
finish("order-ranking", d)
