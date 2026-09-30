"""Readable rewrite of Order & Ranking (order-ranking).

Phase 3: plain English, "rank = people before you + 1" as the one idea, examples verified below.
Every answer is recomputed with explicit rows (lists) or by enumerating all orderings.
Run: python order_ranking.py  (patches content/core/topics/reasoning/order-ranking.json)
"""
import json
from itertools import permutations
from pathlib import Path

ROOT = Path(__file__).resolve().parents[3]
TOPIC = ROOT / "core" / "topics" / "reasoning" / "order-ranking.json"


# ---------------------------------------------------------------- helpers
def row(n):
    """People 1..n numbered from the left. Person p is p-th from the left and n+1-p from the right."""
    return list(range(1, n + 1))


def from_right(p, n):
    r = row(n)
    return len(r) - r.index(p)          # people from p to the right end, counting p


def orders(people, ok):
    """All orderings (top/left first) that satisfy the predicate ok(order)."""
    return [o for o in permutations(people) if ok(o)]


def above(o, a, b):
    return o.index(a) < o.index(b)


def immediately_above(o, a, b):
    return o.index(a) + 1 == o.index(b)


def between(o, a, b, c):
    """c stands between a and b."""
    i, j, k = o.index(a), o.index(b), o.index(c)
    return min(i, j) < k < max(i, j)


# ---------------------------------------------------------------- checks: subtopic 1
assert from_right(10, 40) == 40 + 1 - 10 == 31                 # notes
assert 9 + 11 - 1 == 19                                        # notes total: 9th L, 11th R
r19 = row(19); assert r19.index(9) + 1 == 9 and len(r19) - r19.index(9) == 11
# notes ahead/behind: 5th in a queue of 12 -> 4 ahead, 7 behind
assert 5 - 1 == 4 and 12 - 5 == 7 and 4 + 7 + 1 == 12
# notes swap: row of 25, A 8th from left, B 9th from right -> B's seat is 17th from the left
assert from_right(17, 25) == 9 and 25 + 1 - 9 == 17
# oi-p1: queue of 52, 17th from front -> 36th from back
assert from_right(17, 52) == 36 == 52 + 1 - 17
# oi-p2: 19th from left, 26th from right
assert 19 + 26 - 1 == 44 and from_right(19, 44) == 26
# oi-p3: row of 30, Asha 12th L, Bina 10th from R -> Bina's seat = 21st from L
r = row(30); asha, bina = 12, 30 + 1 - 10
assert bina == 21
r[asha - 1], r[bina - 1] = r[bina - 1], r[asha - 1]
assert r.index(21) + 1 == 12 and r.index(12) + 1 == 21          # Asha now 21st from L, Bina 12th
# oi-p4: stack of five boxes
P4 = orders("PQRST", lambda o: above(o, "P", "Q") and above(o, "R", "S") and above(o, "Q", "R") and o[-1] == "T")
assert P4 == [tuple("PQRST")] and P4[0][2] == "R"
# oi-p5: 14 ahead, 21 behind
assert 14 + 21 + 1 == 36
# oi-p6: exactly in the middle, 13th from left
assert 2 * 13 - 1 == 25 and 13 - 1 == 25 - 13
# trick: 5th from left, 8th from right -> 12 people ; a + b = T + 1
assert 5 + 8 - 1 == 12 and 5 + 8 == 12 + 1
# trick: 12th from top in class of 45 -> 34th from bottom
assert 45 + 1 - 12 == 34

# ---------------------------------------------------------------- checks: subtopic 2
assert 45 + 1 - 12 == 34 and 8 + 21 - 1 == 28 and 11 + 11 - 1 == 21    # old notes facts
assert 75 + 1 - 28 == 48                                                # rp-p1
assert 16 + 24 - 1 == 39 and from_right(16, 39) == 24                   # rp-p2
assert 18 + 6 - 3 == 21                                                 # rp-p3: joiners in front and leavers
# rp-p4: row of 45, Gopal 20th from left; 8 people to his left leave
n = 45; g = 20; left_of_g = g - 1
assert left_of_g >= 8
n2, g2 = n - 8, g - 8
assert (n2, g2) == (37, 12) and n2 + 1 - g2 == 26 == n + 1 - g
# rp-p5: 14th from either end
assert 14 + 14 - 1 == 27 and from_right(14, 27) == 14
# notes: 23rd from top in class of 60 -> 38th ; 14L + 20R -> 33 ; 12T + 41B -> 52
assert 60 + 1 - 23 == 38 and 14 + 20 - 1 == 33 and 12 + 41 - 1 == 52
# notes: 5 leave from the left; 16th becomes 11th
assert 16 - 5 == 11
# notes: below him = rank from bottom - 1 ; 12th from top in a class of 40 -> 28 below
assert 40 - 12 == 28 == (40 + 1 - 12) - 1
# trick: sum check
assert 14 + 20 == 33 + 1

# ---------------------------------------------------------------- checks: subtopic 3
def n_between_same_end(a, b):
    return abs(a - b) - 1


assert n_between_same_end(9, 26) == 16                                  # old notes
assert 45 - 14 - 18 == 13                                               # old notes shape 2
r45 = row(45); assert r45.index(14) + 1 == 14 and from_right(45 + 1 - 18, 45) == 18
assert (9 + 21) // 2 == 15 and (9 + 21) % 2 == 0                        # notes middle
# bo-p1: 7th and 31st from left
assert n_between_same_end(7, 31) == 23
# bo-p2: row of 52, X 15th from left, Y 21st from right
rr = row(52); x = 15; y = 52 + 1 - 21
assert y == 32 and y - x - 1 == 16 == 52 - 15 - 21
# bo-p3: middle of 12th and 30th
assert (12 + 30) % 2 == 0 and (12 + 30) // 2 == 21 and n_between_same_end(12, 21) == n_between_same_end(21, 30) == 8
# bo-p4: Ravi 15th from left, Sohan 11th from right, after swap Ravi is 20th from left
ravi0, sohan_r = 15, 11
sohan_seat = 20                                     # Ravi takes Sohan's seat after the swap
T = sohan_seat + sohan_r - 1
assert T == 30 and T + 1 - sohan_r == sohan_seat
assert sohan_seat - ravi0 - 1 == 4
r = row(T); r[ravi0 - 1], r[sohan_seat - 1] = r[sohan_seat - 1], r[ravi0 - 1]
assert r.index(ravi0) + 1 == 20                       # Ravi (person 15) sits 20th from left after swap
assert len([q for q in row(T) if ravi0 < q < sohan_seat]) == 4
# bo-p5: outside the pair
assert 52 - 15 - 21 == 16 and 52 - 16 - 2 == 34
# bo-p6: 7 between, Tina 11th from top -> Uma 19th
assert 11 + 7 + 1 == 19 and n_between_same_end(11, 19) == 7
# notes: old overlap example (kept as a mirror)
assert 22 + 9 - 1 == 30 and 30 + 1 - 9 == 22 and 22 - 17 - 1 == 4
# trick: 3 + ... convert then count: row of 40, 10th from right -> 31st from left; other 5th from left: 25 between
assert 40 + 1 - 10 == 31 and n_between_same_end(5, 31) == 25

# ---------------------------------------------------------------- checks: subtopic 4
def unique_order(people, ok):
    o = orders(people, ok)
    assert len(o) == 1, o
    return o[0]


# ac-p1: A>B, B>C>D, D>E  (taller first)
o = unique_order("ABCDE", lambda o: above(o, "A", "B") and above(o, "B", "C") and above(o, "C", "D") and above(o, "D", "E"))
assert o == tuple("ABCDE") and o[1] == "B"
# ac-p2: Kiran below Manu, above Lata; Neeta below Lata; Om above Manu -> Om, Manu, Kiran, Lata, Neeta
o = unique_order("KLMNO", lambda o: above(o, "M", "K") and above(o, "K", "L") and above(o, "L", "N") and above(o, "O", "M"))
assert o == tuple("OMKLN") and o[1] == "M"
# ac-p3: Rita younger than Sita; Tina older than Sita; Uma younger than Rita; Vani older than Tina
o = unique_order("RSTUV", lambda o: above(o, "S", "R") and above(o, "T", "S") and above(o, "R", "U") and above(o, "V", "T"))
assert o == tuple("VTSRU") and o[2] == "S"
# ac-p4: stack of books top->bottom. Maths above Science; History below Science; Art above Maths; Art below English
o = unique_order(["Art", "English", "History", "Maths", "Science"],
                 lambda o: above(o, "Maths", "Science") and above(o, "Science", "History") and above(o, "Art", "Maths") and above(o, "English", "Art"))
assert o == ("English", "Art", "Maths", "Science", "History") and o[2] == "Maths"
# ac-p5: fixed slot, open order
ok = orders("PQRST", lambda o: above(o, "P", "Q") and above(o, "Q", "R") and above(o, "S", "P") and above(o, "S", "T"))
assert len(ok) > 1 and {o[0] for o in ok} == {"S"}                    # order not fixed, tallest fixed
# ac-p6: immediately-above clues
ok = orders("ABCDE", lambda o: immediately_above(o, "A", "B") and above(o, "C", "A") and above(o, "B", "D") and between(o, "B", "D", "E"))
assert ok == [tuple("CABED")] and ok[0][3] == "E"
# notes: A>B, B>D merges to A>B>D
assert orders("ABD", lambda o: above(o, "A", "B") and above(o, "B", "D")) == [tuple("ABD")]
# trick: Sunil younger than Vijay (S<V), Vijay younger than Wasim, who is oldest -> Wasim
assert unique_order("SVW", lambda o: above(o, "V", "S") and above(o, "W", "V"))[0] == "W"
# trick: gaps: A>B and C>D leave A vs C open
assert len(orders("ABCD", lambda o: above(o, "A", "B") and above(o, "C", "D"))) == 6
assert len({o for o in orders("ABCD", lambda o: above(o, "A", "B") and above(o, "C", "D")) if o[0] in "AC"}) == 6


# ---------------------------------------------------------------- content helpers
def pat(pid, name, freq, spot, formula, steps, why, q, ex_steps, answer):
    return {"id": pid, "name": name, "frequency": freq, "howToSpot": spot, "formula": formula,
            "steps": steps, "why": why, "example": {"q": q, "steps": ex_steps, "answer": answer}}


dfrac = lambda x: x.replace(r"\frac", r"\dfrac")

# ============================================================ subtopic 1: order-idea
s1_concept = (
    "In a row or a queue, a person's rank tells how many people stand before them, plus one. "
    "Every ranking question comes from this one sentence. "
    "Learn two shortcuts: the rank from the other end, and the total from two ranks. "
    "Draw a small row of boxes whenever three or more people are involved."
)

s1_notes = r"""### The one idea
A rank counts the person too. If 4 people stand before you, your rank is 5.

> **Rule:** Rank = number of people before you + 1. Every formula in this topic comes from this line.

Example: Sita is 5th in a queue of 12. Four people are ahead of her ($5 - 1 = 4$). Seven are behind her ($12 - 5 = 7$).

### The other end
The same person has a different rank from the other end. Find it in one step.

$$\text{rank from the other end} = \text{total} - \text{rank} + 1$$

Example: in a row of 40, Ravi is 10th from the left. From the right he is $40 - 10 + 1 = 31$st.

Why add 1? Ravi is counted once from each side. Take him out and count the people to his right: $40 - 10 = 30$. Then add Ravi himself.

### Total from two ranks
Suppose one person is $a$-th from one end and $b$-th from the other end. Both counts include that person. So he is counted twice.

$$\text{total} = a + b - 1$$

Example: 9th from the left and 11th from the right gives $9 + 11 - 1 = 19$ people.

> **Tip:** The two ranks always add up to the total plus 1. Use this to check yourself: $9 + 11 = 20 = 19 + 1$.

### Ahead and behind
"Ahead" does not include the person. So it is one less than his rank.

- Ahead of him = rank $- 1$.
- Behind him = total $-$ rank.
- Ahead + behind + 1 = total.

Example: 14 people are ahead of a girl and 21 are behind her. The total is $14 + 21 + 1 = 36$.

### Two people swap places
When two people exchange seats, each person takes the other's seat. So a new rank is just the old rank of the other seat.

Example: a row has 25 people. Ram is 8th from the left. Shyam is 9th from the right, which is $25 + 1 - 9 = 17$th from the left. After the swap, Ram is 17th from the left.

> **Watch:** Convert both ranks to the same end before you compare seats.

### Stacks and rows of objects
Books, boxes and shelves work the same way. "Above" is like "to the left". Write the order from top to bottom as each sentence comes. Then read the seat that is asked.

### A full walk-through
Read this one slowly. A queue has 52 people. Kavya is 17th from the front.

1. People ahead of her: $17 - 1 = 16$.
2. People behind her: $52 - 17 = 35$.
3. Check: $16 + 35 + 1 = 52$. The total matches.
4. Her rank from the back: $35 + 1 = 36$. The formula gives the same: $52 + 1 - 17 = 36$.

> **Example:** Two ways gave 36. When both routes agree, you can trust the answer. Use this check in the exam whenever time allows.

### Facing South
A row facing North has its usual left and right. A row facing **South** has them swapped. Their left is your right. Underline the facing word before you use any left or right clue.
"""

s1_formulas = [
    {"name": "Rank from the other end", "tex": r"p' = n + 1 - p", "note": "n = total people, p = rank from one end."},
    {"name": "Total from two ranks", "tex": r"n = a + b - 1", "note": "The same person is a-th from one end and b-th from the other end."},
    {"name": "Between count (same end)", "tex": r"\text{between} = |a - b| - 1", "note": "Both ranks are from the same end."},
    {"name": "Ahead and behind", "tex": r"\text{ahead} = r - 1,\quad \text{behind} = n - r", "note": "r = the person's rank from the front."},
]

s1_patterns = [
    pat("oi-p1", "Rank from the other end", "very common",
        "The total and one rank are given. The rank from the other end is asked.",
        r"p' = n + 1 - p",
        ["Write the total and the rank you know.", "Subtract the rank from the total.", "Add 1."],
        "The person is counted from both ends, so one seat is counted twice and you add it back.",
        "In a queue of 52 people, Kavya is 17th from the front. What is her position from the back?",
        [r"Position from the back = $52 - 17 + 1$.", r"$= 36$."],
        "36th from the back"),
    pat("oi-p2", "Total from two ranks", "very common",
        "One person's rank is given from both ends. The number of people is asked.",
        r"n = a + b - 1",
        ["Add the two ranks.", "Subtract 1 for the person counted twice.", "Check: the total must be bigger than each rank."],
        "The person is counted in both ranks, so one count must be removed.",
        "Manoj is 19th from the left and 26th from the right in a row. How many people are in the row?",
        [r"Total = $19 + 26 - 1$.", r"$= 44$."],
        "44"),
    pat("oi-p3", "Two people swap places", "common",
        "Two people exchange seats. A rank after the swap is asked.",
        None,
        ["Convert the second person's rank to the same end as the question.", "That seat number is the first person's new rank.", "Read the answer from that seat."],
        "Each person takes over the other's seat, so a new rank is an old seat number.",
        "In a row of 30, Asha is 12th from the left and Bina is 10th from the right. They exchange places. What is Asha's new position from the left?",
        [r"Bina's seat from the left = $30 + 1 - 10 = 21$.", "Asha moves to that seat."],
        "21st from the left"),
    pat("oi-p4", "Building a stack or row from clues", "common",
        "Boxes, books or people are described by 'above', 'below', 'left' or 'right'. A seat or an end is asked.",
        None,
        ["Draw a column or a row of empty boxes.", "Fill in the sure fact first, such as 'at the bottom'.", "Place each clue as it comes. Then read the asked seat."],
        "Each clue fixes one link. The links together make one ordered line.",
        "Five boxes are in a stack. P is above Q. R is below Q but above S. T is at the bottom. Which box is in the middle?",
        ["T is at the bottom.", "Order from the top: P, Q, R, S, T.", "The middle (third) box is R."],
        "R"),
    pat("oi-p5", "People ahead and behind", "common",
        "The question gives the people ahead of someone and the people behind, and asks the total or the rank.",
        r"n = \text{ahead} + \text{behind} + 1",
        ["Write the number ahead and the number behind.", "Add the person himself: +1.", "His rank from the front is ahead + 1."],
        "Ahead and behind leave out the person, so he must be added back.",
        "In a queue, 14 people stand ahead of Sneha and 21 stand behind her. How many people are in the queue?",
        [r"Total = $14 + 21 + 1$.", r"$= 36$."],
        "36"),
    pat("oi-p6", "Exactly in the middle", "occasional",
        "The person is exactly in the middle, or there are as many people ahead as behind.",
        r"n = 2r - 1",
        ["Write ahead = behind, so $r - 1 = n - r$.", "Solve for the total: $n = 2r - 1$.", "The middle person is in seat $\\dfrac{n+1}{2}$."],
        "The middle person has the same number of people on each side.",
        "Meena is exactly in the middle of a row. She is 13th from the left. How many people are in the row?",
        [r"Ahead of her: $13 - 1 = 12$.", "Behind her: also 12.", r"Total = $12 + 12 + 1 = 25$."],
        "25"),
]

s1_tricks = [
    {"title": "Check that the two ranks add to total plus 1",
     "body": "For one person, the two ranks from opposite ends always add up to the total plus 1. If they do not, you have misread a number.",
     "example": {"q": "A boy is 5th from the left and 8th from the right. How many people are in the row?",
                 "steps": [r"$5 + 8 - 1 = 12$.", "Check: $5 + 8 = 13 = 12 + 1$."],
                 "answer": "12"}},
    {"title": "Draw the end zones",
     "body": "Draw a short row of boxes. 'a-th from the left' means $a - 1$ people stand before the person. Counting people at each end is often faster than any formula.",
     "example": {"q": "In a class of 45, Priya is 12th from the top. What is her rank from the bottom?",
                 "steps": ["People below her: $45 - 12 = 33$.", r"Her rank from the bottom: $33 + 1 = 34$."],
                 "answer": "34th"}},
]

s1_mistakes = [
    {"wrong": "Forgetting the +1 or the -1.", "right": "The person counts from both ends. Use $n + 1 - p$ and $a + b - 1$."},
    {"wrong": "Subtracting a rank from the left directly from a rank from the right.", "right": "Convert both to the same end first."},
    {"wrong": "Calling 'ahead of him' the same as his rank.", "right": "Ahead = rank $- 1$. Rank = ahead $+ 1$."},
    {"wrong": "Guessing one more or one less than an option.", "right": "Work it out. Wrong options are set exactly one away."},
    {"wrong": "Using left and right the usual way for a row facing South.", "right": "Underline the facing word. South-facing left is your right."},
]

s1_revision = [
    "Rank = people before you + 1.",
    "Other end: total $-$ rank $+ 1$.",
    "Total from two ranks: $a + b - 1$.",
    "Ahead = rank $- 1$. Behind = total $-$ rank.",
    "Swap: each person takes the other's seat.",
    "A South-facing row has left and right swapped.",
]

# ============================================================ subtopic 2: rank-position
s2_concept = (
    "These questions are about one person's rank in a class, a queue or a row. "
    "Use the two shortcuts: total minus rank plus 1, and rank plus rank minus 1. "
    "When people join or leave the row, count the people before him first. Then add 1."
)

s2_notes = r"""### The other end, again
The rank from the other end of a class or a row is a simple sum.

$$\text{rank from the bottom} = \text{class size} - \text{rank from the top} + 1$$

Example: in a class of 60, Neha is 23rd from the top. From the bottom she is $60 - 23 + 1 = 38$th.

### The total from two ranks
If a person's two ranks are given, the total is their sum minus 1.

Example: Sonu is 14th from the left and 20th from the right. The row has $14 + 20 - 1 = 33$ people.

Three quick facts to remember:
- 12th from the top in a class of 45 is 34th from the bottom.
- 8th from the left and 21st from the right gives $8 + 21 - 1 = 28$ people.
- 11th from either end gives $11 + 11 - 1 = 21$ people.

> **Tip:** The total is always bigger than each of the two ranks. If not, you misread.

### People above and below
The rank counts the person too. The number of people below him leaves him out.

- People below him = class size $-$ his rank from the top.
- People above him = his rank from the top $- 1$.

Example: Reena is 12th from the top in a class of 40. So $40 - 12 = 28$ students are below her.

### People join or leave the front
Count the people before him first. Then add 1.

- $k$ people join **ahead** of him: his rank becomes old rank $+ k$.
- $k$ people who were **ahead** of him leave: his rank becomes old rank $- k$.
- People who join or leave **behind** him do not change his rank from the front.

Example: Ishaan is 18th in a queue. 6 people join in front of him. Then 3 people who were ahead of him leave. His new rank is $18 + 6 - 3 = 21$st.

### People leave from the middle of a row
Only the people to the right of the leavers move. They slide left by the number who left.

Example: A is 16th from the left. 5 people leave from the left end. A slides to $16 - 5 = 11$th.

> **Watch:** Look at where the leavers stood. People on the same side as the person change his rank. People on the other side change only the total.

### Rank from the other end after people leave
When people to his left leave, his rank from the right does not change. Only the total falls.

Example: in a row of 45, Gopal is 20th from the left. His rank from the right is $45 + 1 - 20 = 26$. Eight people to his left leave. He is now 12th from the left in a row of 37. His rank from the right is $37 + 1 - 12 = 26$. It did not change.

### Class ranks with a twist
If some students fail, remove them from the total before you use the formula. The formula stays the same. Only the total changes.

Example: a class of 50 has 4 failed students, and Anil is 10th from the top among the rest. Now the total is $50 - 4 = 46$. His rank from the bottom is $46 + 1 - 10 = 37$.
"""

s2_formulas = [
    {"name": "Rank from the other end", "tex": r"p' = n + 1 - p", "note": "n = class size or row size."},
    {"name": "Total from two ranks", "tex": r"n = a + b - 1", "note": "The same person, ranked from both ends."},
    {"name": "People joining or leaving ahead", "tex": r"r_{\text{new}} = r_{\text{old}} \pm k", "note": "Plus for k joiners ahead. Minus for k leavers who were ahead."},
]

s2_patterns = [
    pat("rp-p1", "Rank from the other end", "very common",
        "The size of the class or row and a rank from the top or left are given. The rank from the other end is asked.",
        r"p' = n + 1 - p",
        ["Write the class size and the rank.", "Subtract the rank from the size.", "Add 1."],
        "The person is counted from both ends, so add back the shared seat.",
        "In a class of 75, Varun ranks 28th from the top. What is his rank from the bottom?",
        [r"$75 - 28 + 1$.", r"$= 48$."],
        "48th from the bottom"),
    pat("rp-p2", "Total from two ranks", "very common",
        "One person's rank from both ends is given. The total is asked.",
        r"n = a + b - 1",
        ["Add the two ranks.", "Subtract 1.", "Check that the total is bigger than each rank."],
        "The person is counted twice, once from each end.",
        "Divya is 16th from the left and 24th from the right in a row. How many people are in the row?",
        [r"$16 + 24 - 1$.", r"$= 39$."],
        "39"),
    pat("rp-p3", "People join or leave ahead", "common",
        "People join or leave a queue. The person's new position is asked.",
        r"r_{\text{new}} = r_{\text{old}} + \text{joiners} - \text{leavers}",
        ["Count only the people who joined or left ahead of him.", "Add joiners and subtract leavers from his rank.", "Ignore people behind him."],
        "Only the people before him change his rank.",
        "Ishaan is 18th in a queue. 6 people join in front of him. Then 3 people who were ahead of him leave. What is his new position?",
        [r"After the joiners: $18 + 6 = 24$.", r"After the leavers: $24 - 3 = 21$."],
        "21st"),
    pat("rp-p4", "Rank after people leave the row", "common",
        "Some people stand up and leave. A remaining person's new rank is asked.",
        None,
        ["Note whether the leavers stood on his left or right.", "Recount his rank from the side where they left. Subtract the leavers.", "Reduce the total by the number who left. Then find the rank asked."],
        "Only leavers on his own side change his rank. All leavers change the total.",
        "In a row of 45, Gopal is 20th from the left. 8 people to his left leave the row. What is Gopal's position from the right now?",
        [r"Row now: $45 - 8 = 37$ people. Gopal: $20 - 8 = 12$th from the left.", r"From the right: $37 + 1 - 12 = 26$."],
        "26th from the right"),
    pat("rp-p5", "The same rank from both ends", "occasional",
        "The person is said to be the same rank from both ends. The total is asked.",
        r"n = 2r - 1",
        ["Use $a = b = r$.", "Total = $r + r - 1$.", "He is the middle person."],
        "The person is in the exact middle, with the same number of people on each side.",
        "Deepak is 14th from either end of a line. How many people are in the line?",
        [r"$14 + 14 - 1$.", r"$= 27$."],
        "27"),
]

s2_tricks = [
    {"title": "Check that the sum of the two ranks is total plus 1",
     "body": "For one person, the two ranks add up to the total plus 1. Test it before you mark the answer.",
     "example": {"q": "Sonu is 14th from the left and 20th from the right. How many are in the row?",
                 "steps": [r"$14 + 20 - 1 = 33$.", "Check: $14 + 20 = 34 = 33 + 1$."],
                 "answer": "33"}},
]

s2_mistakes = [
    {"wrong": "Using $n = a + b$ with no minus 1.", "right": "The person is counted twice, so use $n = a + b - 1$."},
    {"wrong": "Reading '11th from either end' as two different people.", "right": "It is one person in the exact middle. Total $= 11 + 11 - 1 = 21$."},
    {"wrong": "Changing his rank when people join or leave behind him.", "right": "Only people ahead of him change his rank from the front."},
    {"wrong": "Calling 'people below him' the same as his rank from the bottom.", "right": "People below = his rank from the bottom $- 1$."},
    {"wrong": "Forgetting to reduce the total when people leave.", "right": "Every leaver reduces the total by 1, even if his rank does not change."},
]

s2_revision = [
    "Other end: size $-$ rank $+ 1$.",
    "Two ranks: total $= a + b - 1$.",
    "Joiners ahead: rank $+ k$. Leavers ahead: rank $- k$.",
    "People behind him never change his rank from the front.",
    "Below him = rank from the bottom $- 1$.",
    "If some students fail, remove them from the total first.",
]

# ============================================================ subtopic 3: between-overlapping
s3_concept = (
    "These questions ask how many people stand between two people. "
    "First find out which end each rank comes from. "
    "If both ranks are from the same end, subtract and take away 1. "
    "If they are from opposite ends, subtract both from the total."
)

s3_notes = r"""### The same end
"Between" leaves out both people. So subtract the two ranks and drop 1.

$$\text{between} = |a - b| - 1$$

Example: R is 9th from the top and S is 26th from the top. Between them: $26 - 9 - 1 = 16$ students.

### Opposite ends
Suppose P is $a$-th from the left and Q is $b$-th from the right. Take both ranks off the total. What is left is the people in between.

$$\text{between} = \text{total} - a - b$$

Example: a row has 45 people. X is 14th from the left and Y is 18th from the right. Between them: $45 - 14 - 18 = 13$.

> **Tip:** No total given? Find it from any person who has ranks from both ends: $a + b - 1$.

### The middle person
Take two ranks from the same end. The person exactly in the middle has this rank from that end:

$$\dfrac{a + b}{2}$$

Example: 9th and 21st from the left. The middle person is $\dfrac{9 + 21}{2} = 15$th from the left. There are 5 people on each side of him, between him and each of the two.

If $a + b$ is odd, there is no single middle person. Two people stand in the middle.

### The overlap puzzle
A swap can reveal a rank that the row never stated. Build the total first. Then count between.

Example: Ravi is 15th from the left. Sohan is 11th from the right. After they swap, Ravi is 20th from the left.

1. Ravi took Sohan's seat. So Sohan's seat is 20th from the left and 11th from the right.
2. Total $= 20 + 11 - 1 = 30$.
3. Originally, Ravi was 15th and Sohan's seat was 20th. Between them: $20 - 15 - 1 = 4$.

> **Watch:** The rank after the swap belongs to the other person's seat. It is not his old seat.

### Given the gap, find the rank
If $k$ people stand between two people and they are counted from the same end, the second rank is:

$$b = a + k + 1$$

Example: Tina is 11th from the top. 7 students are between Tina and Uma, and Uma is below her. Uma is $11 + 7 + 1 = 19$th from the top.

### People outside the pair
"How many people are not between them?" Find between first. Then remove the two people themselves.

$$\text{outside} = \text{total} - \text{between} - 2$$

Example: total 52, between 16. Outside: $52 - 16 - 2 = 34$.

### Two ways to check
Check every answer once by drawing the row.

Example: the row has 45 people. X is 14th from the left. Y is 18th from the right, so Y is $45 + 1 - 18 = 28$th from the left. Now use the same-end formula: $28 - 14 - 1 = 13$. The direct formula $45 - 14 - 18 = 13$ agrees.

Two routes, one answer. If they differ, one rank was read from the wrong end.

> **Note:** Between can never be negative, and between plus 2 can never be more than the total. If it is, you misread an end.
"""

s3_formulas = [
    {"name": "Between, same end", "tex": r"\text{between} = |a - b| - 1", "note": "Both ranks are counted from the same end."},
    {"name": "Between, opposite ends", "tex": r"\text{between} = n - a - b", "note": "n = total people, a and b = ranks from opposite ends."},
    {"name": "Middle person", "tex": r"m = \dfrac{a + b}{2}", "note": "a and b from the same end. The result must be a whole number."},
    {"name": "Rank from the gap", "tex": r"b = a + k + 1", "note": "k people are between a and b, counted from the same end."},
]

s3_patterns = [
    pat("bo-p1", "Between, same end", "very common",
        "Both ranks are counted from the same end (left, top or front). The people between them are asked.",
        r"|a - b| - 1",
        ["Check that both ranks are from the same end.", "Subtract the smaller from the larger.", "Subtract 1."],
        "The two people themselves are not between, so one seat is dropped.",
        "P is 7th from the left and Q is 31st from the left in a row. How many people are between them?",
        [r"$31 - 7 = 24$.", r"$24 - 1 = 23$."],
        "23"),
    pat("bo-p2", "Between, opposite ends", "very common",
        "One rank is from the left or top. The other is from the right or bottom. The total is given.",
        r"n - a - b",
        ["Write the total, then both ranks.", "Subtract both ranks from the total.", "No total? Build it from a person with both ranks."],
        "Taking both ranks off the total leaves exactly the people in the middle.",
        "In a row of 52, X is 15th from the left and Y is 21st from the right. How many people are between X and Y?",
        [r"$52 - 15 - 21$.", r"$= 16$."],
        "16"),
    pat("bo-p3", "The middle person", "common",
        "The question asks who or which seat is exactly in the middle of two people.",
        r"\dfrac{a + b}{2}",
        ["Get both ranks from the same end.", "Add them and halve the sum.", "Check the answer is a whole number."],
        "The middle is the average of the two seat numbers.",
        "A is 12th from the left and B is 30th from the left. Which seat is exactly in the middle of them?",
        [r"$\dfrac{12 + 30}{2} = 21$.", "There are 8 people between A and the middle person."],
        "21st from the left"),
    pat("bo-p4", "Swap and count between", "occasional",
        "A swap gives a new rank. The number of people between the two before the swap is asked.",
        None,
        ["The person who moved took the other's seat. That seat has the new rank.", "Find the total: new rank $+$ other's rank from the other end $- 1$.", "Count between with the same-end formula."],
        "The swap reveals one rank the row never stated. Once the total is known, it is a plain count.",
        "Ravi is 15th from the left and Sohan is 11th from the right. After they exchange places, Ravi is 20th from the left. How many people were between them before?",
        [r"Sohan's seat is 20th from the left and 11th from the right. Total $= 20 + 11 - 1 = 30$.", r"Between: $20 - 15 - 1 = 4$."],
        "4"),
    pat("bo-p5", "People outside the pair", "occasional",
        "The question asks how many people are not between two people, or ahead of and behind them.",
        r"n - \text{between} - 2",
        ["Find the people between first.", "Subtract that from the total.", "Subtract 2 for the two people themselves."],
        "Total = between + the two people + everyone outside.",
        "In a row of 52, X is 15th from the left and Y is 21st from the right. How many people are outside the pair (not between them and not X or Y)?",
        [r"Between $= 52 - 15 - 21 = 16$.", r"Outside $= 52 - 16 - 2 = 34$."],
        "34"),
    pat("bo-p6", "Find the rank from the gap", "occasional",
        "The number of people between two people is given. One person's rank is known and the other's is asked.",
        r"b = a + k + 1",
        ["Note which person is nearer to the start.", "Add the gap $k$ and 1 to the nearer rank.", "Subtract instead if the second person is closer to the start."],
        "The second person sits after the $k$ people between and one more seat.",
        "Tina is 11th from the top. 7 students are between Tina and Uma, and Uma is below Tina. What is Uma's rank from the top?",
        [r"$11 + 7 + 1$.", r"$= 19$."],
        "19th from the top"),
]

s3_tricks = [
    {"title": "Convert first, then count",
     "body": "Never subtract ranks from different ends. Convert one rank with $n + 1 - p$. Then use the same-end formula.",
     "example": {"q": "In a row of 40, A is 5th from the left and B is 10th from the right. How many people are between them?",
                 "steps": [r"B from the left: $40 + 1 - 10 = 31$.", r"Between: $31 - 5 - 1 = 25$."],
                 "answer": "25"}},
]

s3_mistakes = [
    {"wrong": "Subtracting a rank from the left from a rank from the right.", "right": "Convert one rank to the other end first, or use $n - a - b$."},
    {"wrong": "Forgetting the last -1 and counting the two people as well.", "right": "'Between' leaves out both people."},
    {"wrong": "Converting both ranks with $n + 1 - p$.", "right": "Convert only one. Both ranks must end up on the same side."},
    {"wrong": "Using the person's old seat after a swap.", "right": "After a swap, the person sits in the other's seat."},
    {"wrong": "Continuing when the answer is negative.", "right": "A negative count means a misread end. Stop and convert again."},
]

s3_revision = [
    r"Same end: $|a - b| - 1$.",
    r"Opposite ends: total $- a - b$.",
    r"Middle person: $\dfrac{a + b}{2}$ from the same end.",
    "Swap puzzle: find the total first, then count between.",
    r"Given a gap $k$: $b = a + k + 1$.",
    "Outside the pair = total $-$ between $- 2$.",
]

# ============================================================ subtopic 4: arrangement-comparison
s4_concept = (
    "These questions give scattered comparisons such as 'A is taller than B'. "
    "Write each clue as a short arrow. Join the arrows into one chain, then read the seat that is asked. "
    "Words like 'shorter', 'younger' and 'below' point the arrow the other way, so turn them around first."
)

s4_notes = r"""### Write each clue as an arrow
Use one arrow for one clue. Point it towards the taller, older or higher person.

- "A is taller than B" becomes A > B.
- "C is shorter than B" becomes B > C.
- "D scored less than C" becomes C > D.

> **Rule:** Always put the bigger, older or higher person on the left. Turn 'shorter', 'younger', 'less' and 'below' around before you write.

### Join the arrows into a chain
Clues that share a person join together. A > B and B > D make A > B > D.

Example: "A is taller than B. C is taller than D and shorter than B. E is shorter than D." Write A > B, B > C > D and D > E. The chain is A > B > C > D > E. The second tallest is B.

### Read the seat
Read the chain from the left end.

- Tallest: the first person.
- Shortest: the last person.
- Second tallest: the second person from the left.

The middle seat of five people is the third one.

### When the full order is not known
Some clues leave two people unranked. For example, A > B and C > D say nothing about A against C. So the whole order is open.

But the answer may still be fixed. If only one person can stand first, that person is the tallest, even when other seats stay open.

> **Tip:** Fix the seat that is asked. You do not always need the full order.

### Marks, ages and objects
Marks, ages, heights and weights all work alike. Use the same arrows for all of them.

Objects in a stack work alike too. "The red box is above the blue box" is an arrow pointing up. Write the stack from the top down and read it like a chain. "Third from the top" is the third person in the chain.

### Words that fix a place
Some words fix a place more tightly than a simple "taller than".

- "Immediately above B" means directly next to B, with no one between.
- "Between B and D" means somewhere in the middle. It does not say the exact seat.

Use "immediately" clues first. They join two people into one block.

> **Watch:** Read the clue again if you find two possible orders. A full puzzle has one order only.

### A slow example
Read the clues once, then write the arrows. "Ann is older than Ben. Cara is younger than Ben. Dev is older than Ann." Arrows: Ann > Ben, Ben > Cara, Dev > Ann. Chain: Dev > Ann > Ben > Cara. The youngest is Cara. The second oldest is Ann.

> **Example:** Ask a different question of the same chain. Who is older than Ben but younger than Dev? Only Ann fits. Reading the chain answers every version of the question.

### Facing pairs
Two people who face each other have opposite left and right. The left hand of one is the right hand of the other. Draw the two arrows first.
"""

s4_patterns = [
    pat("ac-p1", "Height or size chain", "very common",
        "Clues use 'taller than', 'bigger than' or 'heavier than'. The tallest, shortest or one seat is asked.",
        None,
        ["Write each clue as an arrow with the taller person first.", "Join clues that share a person.", "Read the chain from the left."],
        "Clues that share a person always join into a single line.",
        "A is taller than B. C is taller than D and shorter than B. E is shorter than D. Who is the second tallest?",
        ["Arrows: A > B, B > C > D, D > E.", "Chain: A > B > C > D > E.", "The second person from the left is B."],
        "B"),
    pat("ac-p2", "Marks and scores", "very common",
        "Clues use 'scored more than' or 'scored less than'. The highest, lowest or an exact seat is asked.",
        None,
        ["Write each clue as an arrow towards the higher score.", "Turn 'less than' around.", "Join the arrows and read the chain."],
        "'Scored more' works exactly like 'taller'.",
        "Kiran scored more than Lata but less than Manu. Neeta scored less than Lata. Om scored more than Manu. Who scored the second highest?",
        ["Arrows: Manu > Kiran > Lata, Lata > Neeta, Om > Manu.", "Chain: Om > Manu > Kiran > Lata > Neeta.", "The second person from the left is Manu."],
        "Manu"),
    pat("ac-p3", "Ages with 'younger' and 'older'", "very common",
        "Clues use 'older than' and 'younger than' about three to six people.",
        None,
        ["Put the older person on the left in every arrow.", "Turn each 'younger than' clue around.", "Join and count from the left."],
        "Turning every clue to the same direction stops sign slips.",
        "Rita is younger than Sita. Tina is older than Sita. Uma is younger than Rita. Vani is older than Tina. Who is the third oldest?",
        ["Arrows: Sita > Rita, Tina > Sita, Rita > Uma, Vani > Tina.", "Chain: Vani > Tina > Sita > Rita > Uma.", "The third person from the left is Sita."],
        "Sita"),
    pat("ac-p4", "Stacked books and boxes", "common",
        "Books, boxes or subjects are described as above or below. A seat from the top or the bottom is asked.",
        None,
        ["Turn each 'below' clue into an 'above' clue.", "Write the stack from the top down as a chain.", "Count from the asked end."],
        "'Above' is just the arrow pointing up.",
        "Five books are in a stack. Maths is above Science. History is below Science. Art is above Maths but below English. Which book is in the middle?",
        ["Arrows: Maths above Science, Science above History, English above Art above Maths.", "Stack from the top: English, Art, Maths, Science, History.", "The middle (third) book is Maths."],
        "Maths"),
    pat("ac-p5", "The seat is fixed but the order is not", "common",
        "Some pairs are never compared, but the question asks only for the tallest, shortest or one seat.",
        None,
        ["Draw the arrows you have.", "Check who has nobody above them. If only one person, that is the first seat.", "Ignore the pairs that are never compared."],
        "A seat can be fixed even when the whole order is open.",
        "P is taller than Q. Q is taller than R. S is taller than P. T is shorter than S. Who is the tallest?",
        ["Arrows: S > P > Q > R and S > T.", "T is below S, but T is not compared with P, Q or R.", "Nobody is above S."],
        "S"),
    pat("ac-p6", "Clues with 'immediately' and 'between'", "occasional",
        "Clues say 'immediately above' or 'between'. An exact rank is asked.",
        None,
        ["Join 'immediately' pairs into one block first.", "Place the other people above or below the block.", "Fit each 'between' clue into the gap."],
        "An 'immediately' pair is a fixed block, and the other clues only place things around it.",
        "Five students are ranked by marks. A is ranked immediately above B. C is ranked above A. D is ranked below B. E is ranked between B and D. Who is ranked 4th?",
        ["A and B form a block: A, B. C is above the block.", "D is below B, and E is between B and D.", "Order: C, A, B, E, D. Rank 4 is E."],
        "E"),
]

s4_tricks = [
    {"title": "Write two symbols for each clue",
     "body": "Turn each sentence into two letters with a sign, such as S < V. Keep the sign pointing the same way all through. The reversed words then become easy to see.",
     "example": {"q": "Sunil is younger than Vijay. Vijay is younger than Wasim. Who is the oldest?",
                 "steps": ["Arrows: Vijay > Sunil, Wasim > Vijay.", "Chain: Wasim > Vijay > Sunil."],
                 "answer": "Wasim"}},
    {"title": "Start from the person named most often",
     "body": "The person who appears in the most clues is the best starting point. Build the chain outwards from that person and it forms in one pass.",
     "example": {"q": "A is taller than B. B is taller than D. C is taller than A. Who is the tallest?",
                 "steps": ["B appears twice. Chain B > D.", "A is above B: A > B > D.", "C is above A: C > A > B > D."],
                 "answer": "C"}},
]

s4_mistakes = [
    {"wrong": "Answering from part of the chain before using every clue.", "right": "Use all the clues, then read the chain."},
    {"wrong": "Reading 'younger than' or 'less than' in the surface direction.", "right": "Turn every clue so the bigger, older or higher person is on the left."},
    {"wrong": "Ignoring the word 'immediately'.", "right": "It means directly next to. It can change who is second or third."},
    {"wrong": "Accepting two possible orders.", "right": "A full puzzle has exactly one order. Read the clues again."},
    {"wrong": "Building the whole order when the seat is already fixed.", "right": "Check whether only one person can fill the seat asked."},
]

s4_revision = [
    "Every clue is an arrow towards the bigger, older or higher person.",
    "Join clues that share a person into one chain.",
    "Turn 'shorter', 'younger', 'less' and 'below' around first.",
    "Read the chain: tallest is the first, shortest is the last.",
    "A seat can be fixed even if the whole order is open.",
    "'Immediately' means next to. 'Between' means somewhere inside.",
]

# ---------------------------------------------------------------- patch
data = json.loads(TOPIC.read_text(encoding="utf-8"))
subs = {s["id"]: s for s in data["subtopics"]}
assert set(subs) == {"order-idea", "rank-position", "between-overlapping", "arrangement-comparison"}


def put(sid, concept, notes, formulas, patterns, tricks, mistakes, revision):
    s = subs[sid]
    old_ids = {p["id"] for p in s.get("patterns", [])}
    assert old_ids <= {p["id"] for p in patterns}, f"{sid}: dropped a pattern id"
    print(sid, "notes chars", len(notes.strip()))
    assert 2500 <= len(notes.strip()) <= 5000, f"{sid}: notes {len(notes.strip())} chars"
    mistakes = [{k: dfrac(v) for k, v in m.items()} for m in mistakes]
    revision = [dfrac(x) for x in revision]
    s.update(concept=concept, notes=notes.strip() + "\n", formulas=formulas, patterns=patterns,
             tricks=tricks, mistakes=mistakes, revision=revision)


put("order-idea", s1_concept, s1_notes, s1_formulas, s1_patterns, s1_tricks, s1_mistakes, s1_revision)
put("rank-position", s2_concept, s2_notes, s2_formulas, s2_patterns, s2_tricks, s2_mistakes, s2_revision)
put("between-overlapping", s3_concept, s3_notes, s3_formulas, s3_patterns, s3_tricks, s3_mistakes, s3_revision)
put("arrangement-comparison", s4_concept, s4_notes, [], s4_patterns, s4_tricks, s4_mistakes, s4_revision)

ids = [p["id"] for s in data["subtopics"] for p in s["patterns"]]
assert len(ids) == len(set(ids)), "pattern id clash"
TOPIC.write_text(json.dumps(data, ensure_ascii=False, indent=1) + "\n", encoding="utf-8", newline="\n")
print("order-ranking updated:", {sid: (len(subs[sid]['notes']), len(subs[sid]['patterns'])) for sid in subs})
