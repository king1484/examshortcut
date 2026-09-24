"""Dictionary-order topic build: notes + patterns + practice + pyqPatterns.

Every answer is computed in this script: real sorts via sorted(), letter positions
via an A-Z strip, word ranks via a multiset-permutation rank function.
"""
import os
import string
import sys
from collections import Counter
from math import factorial

sys.path.insert(0, os.path.dirname(__file__))
from _lib import *  # noqa
from dictionary_order_notes import NOTES, PATTERNS, PYQS

d = load("dictionary-order")

for sid, notes in NOTES.items():
    set_sub(d, sid, notes=notes, patterns=PATTERNS[sid])

# ------------------------------------------------- verification helpers
AL = string.ascii_uppercase


def pos(c):
    return AL.index(c) + 1


def let(n):
    return AL[n - 1]


def word_rank(word):
    c = Counter(word)
    rank = 1
    for ch in word:
        for x in sorted(c):
            if c[x] <= 0:
                continue
            if x >= ch:
                break
            c[x] -= 1
            total = sum(c.values())
            denom = 1
            for v in c.values():
                if v > 0:
                    denom *= factorial(v)
            rank += factorial(total) // denom
            c[x] += 1
        c[ch] -= 1
    return rank


def sorted_list(words):
    return sorted(words)


def same_positions(word):
    s = sorted(word)
    return sum(1 for a, b in zip(word, s) if a == b)


# self-test against known values (incl. the topic's own solved example)
assert word_rank("MACHINE") == 3610
assert word_rank("BEAD") == 11
assert same_positions("PLANET") == 2
assert let(15) == "O" and pos("T") == 20

NQ = []
_ctr = {}


def A(sub, pat, q, ans, wrong, solution, diff="medium", shortcut=None, t=45):
    _ctr[sub] = _ctr.get(sub, 0) + 1
    NQ.append(Q(f"{sub}-p{_ctr[sub]:02d}", q, ans, wrong, solution, shortcut=shortcut,
                diff=diff, sub=sub, pat=pat, t=t))


# ================= dict-idea =================
# p01
order = sorted_list(["Market", "Marble", "Margin"])
assert order[0] == "Marble"
A("dict-idea", "dc-p1", "Which word comes **first** in the dictionary?",
  "Marble", ["Market", "Margin", "Marginal"],
  "All share MAR. 4th letters: b (Marble), k (Market), g (Margin). b is earliest → **Marble** comes first.",
  diff="easy", shortcut="Ignore the shared part; only the first differing letter votes.")
# p02
order = sorted_list(["Panda", "Pants", "Panel", "Panorama"])
assert order == ["Panda", "Panel", "Panorama", "Pants"] and order[-1] == "Pants"
A("dict-idea", "dc-p1", "Which word comes **last** in the dictionary?",
  "Pants", ["Panda", "Panel", "Panorama"],
  "All share PAN. 4th letters: d (Panda), e (Panel), o (Panorama), t (Pants). t is the latest → **Pants** comes last.",
  diff="easy", shortcut="The biggest deciding letter wins the last slot.")
# p03
order = sorted_list(["Sand", "Sandwich", "Sandy", "Sandal"])
assert order[0] == "Sand"
A("dict-idea", "dc-p2", "Arrange as in a dictionary: **Sand, Sandwich, Sandy, Sandal.** Which comes **first**?",
  "Sand", ["Sandal", "Sandy", "Sandwich"],
  "Sand is a prefix of the other three, and a prefix always sorts **before** its extensions → **Sand** first.",
  diff="medium", shortcut="Bare stem beats every extension of itself.")
# p04
order = sorted_list(["Car", "Cart", "Carton", "Cargo"])
assert order == ["Car", "Cargo", "Cart", "Carton"] and order[-1] == "Carton"
A("dict-idea", "dc-p2", "Arrange as in a dictionary: **Car, Cart, Carton, Cargo.** Which comes **last**?",
  "Carton", ["Car", "Cart", "Cargo"],
  "Car is the prefix of the rest → Car first. Extensions by 4th letter: g (Cargo) vs t (Cart, Carton) → g < t, so Cargo precedes both. Cart is the prefix of Carton → Cart, then Carton. Full order: Car, Cargo, Cart, Carton → last = **Carton**.",
  diff="medium", shortcut="Prefix first; then the deepest letter decides the end of the list.")
# p05
order = sorted_list(["Surge", "Surgeon", "Surreal", "Surplus", "Sure"])
assert order == ["Sure", "Surge", "Surgeon", "Surplus", "Surreal"] and order[2] == "Surgeon"
A("dict-idea", "dc-p3", "Arrange as in a dictionary: **Sure, Surge, Surgeon, Surreal, Surplus.** Which comes **third**?",
  "Surgeon", ["Surge", "Surplus", "Surreal"],
  "All share SUR. 4th letters: e (Sure), g (Surge, Surgeon), p (Surplus), r (Surreal); e < g < p < r. Inside the g-pair, Surge is the prefix of Surgeon → Surge first. Full order: Sure, Surge, Surgeon, Surplus, Surreal → third = **Surgeon**.",
  diff="hard", shortcut="Sort the 4th letters e < g < p < r; the prefix splits the g-pair.")
# p06
order = sorted_list(["Kite", "Kind", "Kill", "Kingdom"])
assert order == ["Kill", "Kind", "Kingdom", "Kite"] and order[1] == "Kind"
A("dict-idea", "dc-p3", "Arrange as in a dictionary: **Kite, Kind, Kill, Kingdom.** Which comes **second**?",
  "Kind", ["Kill", "Kite", "Kingdom"],
  "All share KI. 3rd letters: l (Kill), n (Kind, Kingdom), t (Kite); l < n < t. Inside the n-pair, Kind is the prefix of Kingdom → Kind first. Full order: Kill, Kind, Kingdom, Kite → second = **Kind**.",
  diff="medium", shortcut="Sort the 3rd letters l < n < t; the prefix splits the n-pair.")
# p07
order = sorted_list(["Melon", "Melody", "Mellow", "Member"])
adj = [(order[i], order[i + 1]) for i in range(3)]
assert ("Melon", "Melody") in adj or ("Melody", "Melon") in adj
A("dict-idea", "dc-p4", "Arrange as in a dictionary: **Melon, Melody, Mellow, Member.** Which pair sits on **adjacent** slots?",
  "Melon and Melody", ["Member and Melody", "Melon and Member", "Mellow and Member"],
  "4th letters: o (Melon), o (Melody), l (Mellow), b (Member) → Member, Mellow, then Melody (5th d) before Melon (5th n). Order: Member, Mellow, Melody, Melon → the last two are adjacent: **Melon and Melody**.",
  diff="medium", shortcut="Write the numbered order; adjacency is just slots differing by one.")
# p08
order = sorted_list(["Freeze", "Fridge", "Friend", "Fright"])
assert order[1] == "Fridge"
A("dict-idea", "dc-p1", "Arrange as in a dictionary: **Freeze, Fridge, Friend, Fright.** Which comes **second**?",
  "Fridge", ["Freeze", "Friend", "Fright"],
  "FR common. 3rd letters: e (Freeze) vs i (the rest) → Freeze first. The i-group: 4th letters d (Fridge), e (Friend), g (Fright) → Fridge, Friend, Fright. Second = **Fridge**.",
  diff="medium", shortcut="First split at the 3rd letter, then sort the bigger group by the 4th.")
# p09
order = sorted_list(["Play", "Player", "Plays"])
assert order[0] == "Play"
A("dict-idea", "dc-p2", "Which word would a dictionary list **first**: Play, Player or Plays?",
  "Play", ["Player", "Plays", "Any of the three"],
  "Play is a prefix of both Player and Plays, so it sorts before them → **Play** first.",
  diff="easy", shortcut="Prefix beats extensions — no deeper comparison needed.")
# p10
order = sorted_list(["Regal", "Region", "Regime", "Register", "Regret"])
assert order == ["Regal", "Regime", "Region", "Register", "Regret"] and order[-1] == "Regret"
A("dict-idea", "dc-p3", "Arrange as in a dictionary: **Regal, Region, Regime, Register, Regret.** Which comes **last**?",
  "Regret", ["Register", "Region", "Regime"],
  "All share REG. 4th letters: a (Regal), i (Regime, Region, Register), r (Regret); a < i < r, so Regal first and Regret **last** — no 5th letter can rescue Register because its 4th letter (i) already loses to r. Order: Regal, Regime, Region, Register, Regret → last = **Regret**.",
  diff="hard", shortcut="The 4th-letter sort (a < i < r) already fixes both ends of this list.")
# p11
order = sorted_list(["Honest", "Honey", "Hong", "Honk", "Honour"])
assert order == ["Honest", "Honey", "Hong", "Honk", "Honour"] and order[2] == "Hong"
A("dict-idea", "dc-p4", "Arrange as in a dictionary: **Honest, Honey, Hong, Honk, Honour.** Which word is exactly in the **middle**?",
  "Hong", ["Honest", "Honk", "Honour"],
  "All share HON. 4th letters: e (Honest, Honey), g (Hong), k (Honk), o (Honour); e < g < k < o. The e-pair: 5th letters e (Honest) vs y (Honey) → Honest first. Full order: Honest, Honey, Hong, Honk, Honour → middle (slot 3 of 5) = **Hong**.",
  diff="medium", shortcut="Order the 4th letters e < g < k < o; slot 3 of five is the middle.")

# ================= arrange-words =================
# p01
order = sorted_list(["Chalk", "Charm", "Chart", "Chase", "Chatter"])
assert order == ["Chalk", "Charm", "Chart", "Chase", "Chatter"] and order[3] == "Chase"
A("arrange-words", "aw-p1", "Arrange as in a dictionary: **Chalk, Charm, Chart, Chase, Chatter.** Which is the **fourth** word?",
  "Chase", ["Charm", "Chart", "Chatter"],
  "All share CHA. 4th letters: l (Chalk), r (Charm, Chart), s (Chase), t (Chatter); l < r < s < t. The r-pair: 5th letters m (Charm) vs t (Chart) → Charm first. Full order: Chalk, Charm, Chart, Chase, Chatter → fourth = **Chase**.",
  diff="medium", shortcut="Sort the 4th letters; only the r-pair needs one more letter.")
# p02
order = sorted_list(["Colonel", "Colony", "Column", "Colour", "Colossus"])
assert order == ["Colonel", "Colony", "Colossus", "Colour", "Column"]
assert order[order.index("Colony") + 1] == "Colossus"
A("arrange-words", "aw-p3", "Arrange as in a dictionary: **Colonel, Colony, Column, Colour, Colossus.** Which word comes **just after Colony**?",
  "Colossus", ["Colour", "Column", "Colonel"],
  "All share COL. 4th letters: o (Colonel, Colony, Colour, Colossus) vs u (Column) → the o-group first. 5th letters: n (Colonel, Colony), s (Colossus), u (Colour); n < s < u. The n-pair: 6th letters e (Colonel) vs y (Colony) → Colonel, Colony. Full order: Colonel, Colony, Colossus, Colour, Column → just after Colony = **Colossus**.",
  diff="hard", shortcut="u sends Column last; inside the o-group sort 5th letters n < s < u.")
# p03
order = sorted_list(["Panther", "Pant", "Pantomime", "Pantry"])
assert order == ["Pant", "Panther", "Pantomime", "Pantry"] and order[-1] == "Pantry"
A("arrange-words", "aw-p3", "Which word comes **last** in the dictionary: **Panther, Pant, Pantomime, Pantry**?",
  "Pantry", ["Pant", "Panther", "Pantomime"],
  "Pant is the prefix of all → first. 5th letters of the rest: h (Panther), o (Pantomime), r (Pantry); h < o < r. Order: Pant, Panther, Pantomime, Pantry → last = **Pantry**.",
  diff="easy", shortcut="Prefix first; then h < o < r lines up the rest.")
# p04
order = sorted_list(["Judge", "Judo", "Joust", "Journal", "Jostle"])
assert order == ["Jostle", "Journal", "Joust", "Judge", "Judo"] and order[-2] == "Judge"
A("arrange-words", "aw-p4", "Arrange as in a dictionary: **Judge, Judo, Joust, Journal, Jostle.** Which word is **second from the right**?",
  "Judge", ["Judo", "Journal", "Jostle"],
  "2nd letters: o (Jostle, Journal, Joust) vs u (Judge, Judo); o < u → the o-group comes first. 3rd letters: s (Jostle) vs u (Journal, Joust) → Jostle first. 4th letters: r (Journal) vs s (Joust) → Journal, Joust. Full order: Jostle, Journal, Joust, Judge, Judo → slot 5 + 1 − 2 = 4 → **Judge**.",
  diff="hard", shortcut="The 2nd letter splits J-o... before J-u... — check column two before assuming a shared stem.")
# p05
order = sorted_list(["Decamp", "Decay", "Deceive", "Decent", "December"])
assert order == ["Decamp", "Decay", "Deceive", "December", "Decent"]
assert order[order.index("Deceive") - 1] == "Decay"
A("arrange-words", "aw-p2", "Arrange as in a dictionary: **Decamp, Decay, Deceive, Decent, December.** Which word comes **immediately before Deceive**?",
  "Decay", ["Decamp", "December", "Decent"],
  "All share DEC. 4th letters: a (Decamp, Decay), e (the rest) → the a-pair first: 5th letters m (Decamp) vs y (Decay) → Decamp, Decay. The e-group by 5th letters: i (Deceive), m (December), n (Decent). Full order: Decamp, Decay, Deceive, December, Decent → before Deceive = **Decay**.",
  diff="hard", shortcut="Sort the 4th letters a < e; the a-pair hides Decamp vs Decay at the 5th letter.")
# p06
order = sorted_list(["Statue", "Status", "Station", "Statute", "Stature"])
assert order == ["Station", "Statue", "Stature", "Status", "Statute"] and order[2] == "Stature"
A("arrange-words", "aw-p1", "Arrange as in a dictionary: **Statue, Status, Station, Statute, Stature.** Which is **third from the left**?",
  "Stature", ["Statue", "Status", "Statute"],
  "All share STAT. 5th letters: i (Station) vs u (the rest) → Station first. The u-group by 6th letters: e (Statue), r (Stature), s (Status), t (Statute); e < r < s < t. Full order: Station, Statue, Stature, Status, Statute → third = **Stature**.",
  diff="medium", shortcut="Compare position 6: e < r < s < t — Statue, Stature, Status, Statute.")
# p07
order = sorted_list(["Mystery", "Mystic", "Myself", "Myopia"])
assert order == ["Myopia", "Myself", "Mystery", "Mystic"] and order[0] == "Myopia"
A("arrange-words", "aw-p2", "Arrange as in a dictionary: **Mystery, Mystic, Myself, Myopia.** Which comes **first**?",
  "Myopia", ["Myself", "Mystery", "Mystic"],
  "MY common. 3rd letters: s (Mystery, Mystic, Myself) vs o (Myopia); o < s → **Myopia** first, whatever happens later. (Full order: Myopia, Myself, Mystery, Mystic.)",
  diff="medium", shortcut="The earliest 3rd letter ends the contest at once — check the o-word first.")

# ================= letter-position =================
# p01
assert let(15) == "O"
A("letter-position", "lp-p1", "Which is the **15th letter** of the English alphabet?",
  "O", ["N", "P", "M"],
  "EJOTY anchor: O = 15. The 15th letter is **O**.",
  diff="easy", shortcut="E=5, J=10, O=15, T=20, Y=25 — read anchors, never count from A.")
# p02
assert pos("S") - pos("G") - 1 == 11
A("letter-position", "lp-p1", "How many letters of the English alphabet are there **between G and S**?",
  "11", ["12", "13", "10"],
  "pos S = 19, pos G = 7. Letters between = 19 − 7 − 1 = **11** ('between' excludes both ends).",
  diff="easy", shortcut="Difference of positions minus one.")
# p03
assert let(27 - 9) == "R"
A("letter-position", "lp-p2", "Which letter is **9th from the right** of the English alphabet?",
  "R", ["S", "Q", "I"],
  "k-th from the right = position 27 − k from the left: 27 − 9 = 18 → **R**.",
  diff="medium", shortcut="Mirror number 27: from-right k ↔ from-left 27−k.")
# p04
assert 27 - pos("T") == 7
A("letter-position", "lp-p2", "What is the position of the letter **T from the right** of the English alphabet?",
  "7th", ["6th", "8th", "20th"],
  "T is 20th from the left (EJOTY anchor T=20). Mirror: 27 − 20 = **7th** from the right.",
  diff="medium", shortcut="Anchor first, then 27 − position.")
# p05
assert let(12 + 4) == "P"
A("letter-position", "lp-p3", "Which letter is **4th to the right of the 12th letter from the left**?",
  "P", ["O", "Q", "N"],
  "12th letter = L; 4 steps right: 12 + 4 = 16 → **P**.",
  diff="medium", shortcut="Convert to numbers, add right-steps, read off T=20 anchor (16 = T − 4).")
# p06
assert let(27 - 8 - 6) == "M"
A("letter-position", "lp-p3", "Which letter is **6th to the left of the 8th letter from the right**?",
  "M", ["N", "L", "O"],
  "8th from the right = 27 − 8 = 19 (S). 6 steps left: 19 − 6 = 13 → **M**.",
  diff="hard", shortcut="Mirror first (27−8), then subtract the left-steps.")
# p07
strip = AL[12::-1] + AL[13:]  # M..A then N..Z
assert strip[9] == "D"
A("letter-position", "lp-p4", "The first half of the alphabet (A-M) is written in **reverse order**, followed by N-Z. Which letter is **10th from the left** of the new arrangement?",
  "D", ["E", "C", "F"],
  "New strip: M L K J I H G F E D C B A N O P ... Count to 10: M(1) L(2) K(3) J(4) I(5) H(6) G(7) F(8) E(9) D(10) → **D**.",
  diff="medium", shortcut="Write the new strip once; then it is plain counting.")
# p08
strip2 = AL[:13] + AL[:12:-1]  # A..M then Z..N
assert strip2[19] == "T"
A("letter-position", "lp-p4", "The alphabet is written as A to M, followed by **Z to N in reverse**. Which letter is **20th from the left** of this arrangement?",
  "T", ["U", "S", "G"],
  "New strip positions 1-13: A-M; positions 14-26: Z, Y, X, W, V, U, T, S ... 20th = 14 + 6 → count from Z: Z(14) Y(15) X(16) W(17) V(18) U(19) T(20) → **T**.",
  diff="hard", shortcut="Position 20 sits 6 steps into the reversed half starting at Z (position 14).")

# ================= word-formation =================
# p01
assert word_rank("CAB") == 5
A("word-formation", "wf-p1", "All arrangements of the letters of **CAB** are listed as in a dictionary. What is the **rank of CAB**?",
  "5", ["4", "6", "3"],
  "Letters sorted: A, B, C. Position 1 (C): A and B are smaller → 2 × 2! = 4 arrangements come first. Positions 2-3 (A, B): nothing smaller. Rank = 4 + 1 = **5** (list: ABC, ACB, BAC, BCA, CAB).",
  diff="medium", shortcut="Small words: write the 6-item list and count — same answer, zero algebra.")
# p02
assert word_rank("MONSTER") == 1001
A("word-formation", "wf-p1", "The letters of **MONSTER** are arranged in all possible ways as in a dictionary. What is the **rank of MONSTER**?",
  "1001", ["1010", "999", "1111"],
  "Sorted letters: E, M, N, O, R, S, T. M: E smaller → 1 × 6! = 720. O (left M,E,N): E, N smaller → 2 × 4! = 48. N (left E): 1 × 3! = 6. S (left O,R): O, R smaller → 2 × 2! = 4. T (left R): 1 × 1! = 1. E: 0. Rank = 720 + 48 + 6 + 4 + 1 + 1 = **1001**.",
  diff="hard", shortcut="Track the unused set after each fix; multiply the smaller-letter count by the remaining factorial.")
# p03
assert word_rank("PRIME") == 94
A("word-formation", "wf-p1", "If the letters of **PRIME** are arranged in all possible ways as in a dictionary, what is the **rank of PRIME**?",
  "94", ["92", "96", "119"],
  "Sorted letters: E, I, M, P, R. P: E, I, M smaller → 3 × 4! = 72. R (left E, I, M): 3 smaller → 3 × 3! = 18. I (left E, M): 1 smaller → 1 × 2! = 2. M (left E): 1 × 1! = 1. E: 0. Rank = 72 + 18 + 2 + 1 + 1 = **94**.",
  diff="medium", shortcut="720-then-720 style: the first letter usually contributes the bulk.")
# p04
assert same_positions("TABLE") == 1
A("word-formation", "wf-p2", "If the letters of **TABLE** are rearranged in alphabetical order, how many letters **keep their original position**?",
  "One", ["Two", "None", "Three"],
  "TABLE vs its sorted form ABE L T: T-A-B-L-E under A-B-E-L-T → only L sits at position 4 in both → **one** letter.",
  diff="easy", shortcut="Write one word under the other; count exact column matches only.")
# p05
assert same_positions("SIGNED") == 1
A("word-formation", "wf-p2", "If the letters of **SIGNED** are rearranged in alphabetical order, how many letters **keep their original position**?",
  "One", ["Two", "None", "Three"],
  "SIGNED vs its sorted form D-E-G-I-N-S → only G (position 3) matches → **one** letter.",
  diff="medium", shortcut="Compare columns; one match is the usual exam answer — verify, don't assume.")
# p06
bag = Counter("CONVERSATION")
for w, ok in [("CREATION", True), ("CARPENTER", False), ("TRANSPIRE", False), ("CONSUMER", False)]:
    need = Counter(w)
    assert ok == all(need[c] <= bag[c] for c in need)
A("word-formation", "wf-p3", "Which word **can be formed** from the letters of **CONVERSATION**?",
  "CREATION", ["CARPENTER", "TRANSPIRE", "CONSUMER"],
  "Bag: C, O×2, N×2, V, E, R, S, A, T, I. CREATION needs C, R, E, A, T, I, O, N — all present, no letter used twice. CARPENTER needs P (absent); TRANSPIRE needs P (absent); CONSUMER needs U and M (absent) → **CREATION**.",
  diff="medium", shortcut="Hunt the rarest letter of each option first; P/U fail three options instantly.")
# p07
bag = Counter("DISTRIBUTION")
for w, ok in [("STUDIO", True), ("BIRD", True), ("ROBUST", True), ("BRUSH", False)]:
    need = Counter(w)
    assert ok == all(need[c] <= bag[c] for c in need)
A("word-formation", "wf-p3", "Which word **cannot be formed** from the letters of **DISTRIBUTION**?",
  "BRUSH", ["STUDIO", "BIRD", "ROBUST"],
  "Bag: D, I×2, S, T×2, R, B, U, O, N. BRUSH needs **H**, which is not in the word → cannot be formed. STUDIO, BIRD and ROBUST use only available letters within their counts.",
  diff="easy", shortcut="One missing letter is enough — scan for absent letters first.")
# p08
arrs = sorted(["".join(p) for p in __import__("itertools").permutations("BAT")])
assert arrs[3] == "BTA"
A("word-formation", "wf-p4", "All arrangements of the letters of **BAT** are listed in dictionary order. Which is the **4th** word?",
  "BTA", ["BAT", "TAB", "ATB"],
  "Write the six: ABT, ATB, BAT, BTA, TAB, TBA. The 4th is **BTA**.",
  diff="medium", shortcut="Six arrangements, five seconds — write them out, no formula needed.")
# p09
arrs = sorted(["".join(p) for p in __import__("itertools").permutations("FAN")])
assert arrs[arrs.index("AFN") + 1] == "ANF"
A("word-formation", "wf-p4", "All arrangements of **FAN** are listed in dictionary order. Which word comes **immediately after AFN**?",
  "ANF", ["FAN", "FNA", "NAF"],
  "The list: AFN, ANF, FAN, FNA, NAF, NFA. After AFN = **ANF**.",
  diff="medium", shortcut="Same first letter → the deeper letter decides the neighbour.")

d["pyqPatterns"] = [
    PYQ(pattern=p[0], frequency=p[1], subtopic=p[2], howToSpot=p[3],
        approach=p[4], ex_q=p[5], ex_sol=p[6])
    for p in PYQS
]

# p08
order = sorted_list(["Silver", "Silk", "Sinful", "Single"])
assert order == ["Silk", "Silver", "Sinful", "Single"] and order[-2] == "Sinful"
A("arrange-words", "aw-p4", "Arrange as in a dictionary: **Silver, Silk, Sinful, Single.** Which word is **second from the right**?",
  "Sinful", ["Silver", "Single", "Silk"],
  "All share SI. 3rd letters: l (Silk, Silver) vs n (Sinful, Single); l < n. The l-pair: 4th k (Silk) vs v (Silver) → Silk, Silver. The n-pair: 4th f (Sinful) vs g (Single) → Sinful, Single. Full order: Silk, Silver, Sinful, Single → slot 4 + 1 − 2 = 3 → **Sinful**.",
  diff="medium", shortcut="Sort the 3rd letters l < n; then slot N+1−k for the right-count.")

upsert(d["practice"], NQ)
finish("dictionary-order", d)
