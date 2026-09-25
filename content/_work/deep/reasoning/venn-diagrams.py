# -*- coding: utf-8 -*-
"""Deep content for venn-diagrams.json. Idempotent: upserts by id.
Every numeric answer is computed by set algebra; every diagram answer is derived
from the pairwise relations (computed from predicates for number sets)."""
import sys, os
from itertools import product
from fractions import Fraction as F
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
from _lib import *
from venn_content import (NOTES_IDEA, NOTES_TWO, NOTES_THREE, NOTES_REL,
                          P_IDEA, P_TWO, P_THREE, P_REL, PYQS)

T = "venn-diagrams"
d = load(T)
I, TW, TH, R = "venn-idea", "two-set-operations", "three-set-operations", "relation-diagrams"


# ---------------- set-algebra engine ----------------
def three(a, b, c, ab, bc, ac, abc, total=None):
    """Region counts for three sets from the usual data; asserts no negative region."""
    r = {
        (1, 0, 0): a - ab - ac + abc, (0, 1, 0): b - ab - bc + abc, (0, 0, 1): c - bc - ac + abc,
        (1, 1, 0): ab - abc, (0, 1, 1): bc - abc, (1, 0, 1): ac - abc, (1, 1, 1): abc,
    }
    assert all(v >= 0 for v in r.values()), r
    u = sum(r.values())
    assert u == a + b + c - ab - bc - ac + abc
    if total is not None:
        assert total >= u
        r[(0, 0, 0)] = total - u
    return r


def cnt(r, f):
    return sum(v for k, v in r.items() if f(*k))


def two(a, b, both, total):
    r = {(1, 0): a - both, (0, 1): b - both, (1, 1): both, (0, 0): total - (a + b - both)}
    assert all(v >= 0 for v in r.values()), r
    return r


def regions_of(expr, n=3):
    return frozenset(k for k in product((0, 1), repeat=n) if expr(*k))


def expr_q(id, phrase_fn, ans, wrong, **kw):
    """ans / wrong are (text, lambda) pairs; answer must be the ONLY option matching the phrase."""
    target = regions_of(phrase_fn)
    assert regions_of(ans[1]) == target, id
    for w in wrong:
        assert regions_of(w[1]) != target, (id, w[0])
    return Q(id, ans=ans[0], wrong=[w[0] for w in wrong], **kw)


# ---------------- diagram classifier ----------------
def rel_from_sets(X, Y):
    if X <= Y:
        return "sub"
    if Y <= X:
        return "sup"
    if not (X & Y):
        return "dis"
    return "ovl"


SHAPE = {
    "nested": "Three nested circles, one inside the next",
    "two_in": "Two separate circles inside a third circle",
    "two_ovl_in": "Two intersecting circles inside a third circle",
    "in_out": "One circle inside a second; the third separate from both",
    "in_cross": "One circle inside a second; the third intersecting both",
    "in_cross_outer": "One circle inside a second; the third intersecting only the outer circle",
    "in_overlap": "Two intersecting circles, with the third inside their common part",
    "two_sep_cross": "Two separate circles, with the third intersecting both",
    "all_over": "Three circles, each pair intersecting",
    "pair_plus_sep": "Two intersecting circles and a third separate circle",
    "all_sep": "Three completely separate circles",
}


def classify(rels):
    """rels: {(i,j): 'sub'|'sup'|'dis'|'ovl'} for i<j over items 0,1,2."""
    full = {}
    for (i, j), r in rels.items():
        full[(i, j)] = r
        full[(j, i)] = {"sub": "sup", "sup": "sub"}.get(r, r)
    sub = {(i, j) for (i, j), r in full.items() if r == "sub"}
    if len(sub) == 3:
        return "nested"
    if len(sub) == 2:
        (a, b), (c, e) = sorted(sub)
        if b == e:                       # two small ones inside the same big one
            return "two_in" if full[(a, c)] == "dis" else "two_ovl_in"
        if a == c:                       # one small inside two big ones
            assert full[(b, e)] == "ovl"
            return "in_overlap"
        raise AssertionError(rels)
    if len(sub) == 1:
        (a, b), = sub
        c = ({0, 1, 2} - {a, b}).pop()
        ra, rb = full[(c, a)], full[(c, b)]
        if ra == "dis" and rb == "dis":
            return "in_out"
        if ra == "ovl" and rb == "ovl":
            return "in_cross"
        if ra == "dis" and rb == "ovl":
            return "in_cross_outer"
        raise AssertionError(rels)
    nd = sum(1 for (i, j), r in rels.items() if r == "dis")
    return {0: "all_over", 1: "two_sep_cross", 2: "pair_plus_sep", 3: "all_sep"}[nd]


def rels_from_sets(S):
    return {(i, j): rel_from_sets(S[i], S[j]) for i in range(3) for j in range(i + 1, 3)}


def dq(id, words, rels, wrong_keys, solution, shortcut, diff, pat, t=40):
    shape = classify(rels)
    ans = SHAPE[shape]
    wrong = [SHAPE[k] for k in wrong_keys]
    assert ans not in wrong, id
    q = f"Which diagram correctly represents **{words[0]}, {words[1]} and {words[2]}**?"
    return Q(id, q, ans, wrong, solution, shortcut, diff, R, pat, t)


# number domains for exact relation checks
Z = set(range(-300, 301))
HALVES = {F(k, 2) for k in range(-200, 201)}

# ---------------- scenario S1 (news habits) ----------------
S1 = {(1, 0, 0): 20, (0, 1, 0): 25, (0, 0, 1): 5, (1, 1, 0): 15, (0, 1, 1): 6,
      (1, 0, 1): 4, (1, 1, 1): 10, (0, 0, 0): 15}
assert sum(S1.values()) == 100
S1TXT = ("A survey of **100 people** on how they get news — Newspaper (N), TV (T) and Radio (R) — "
         "gave these region counts:\n\n"
         "- Only N: 20 · Only T: 25 · Only R: 5\n"
         "- N and T only: 15 · T and R only: 6 · N and R only: 4\n"
         "- All three: 10 · None of the three: 15\n\n")
s1_two_plus = cnt(S1, lambda n, t, r: n + t + r >= 2)
s1_N = cnt(S1, lambda n, t, r: n)
s1_NR_notT = cnt(S1, lambda n, t, r: (n or r) and not t)
s1_one = cnt(S1, lambda n, t, r: n + t + r == 1)
s1_notT = cnt(S1, lambda n, t, r: not t)
s1_atmost1 = cnt(S1, lambda n, t, r: n + t + r <= 1)
assert (s1_two_plus, s1_N, s1_NR_notT, s1_one, s1_notT, s1_atmost1) == (35, 49, 29, 50, 44, 65)

n_regions3 = len(list(product((0, 1), repeat=3)))
n_inA = len([k for k in product((0, 1), repeat=3) if k[0]])
n_regions2 = len(list(product((0, 1), repeat=2)))

NEW = [
 # ================= venn-idea =================
 expr_q("venn-idea-p01", lambda d_, s, p: d_ and s and not p,
        ("(D ∩ S) − P", lambda d_, s, p: d_ and s and not p),
        [("D ∩ S ∩ P", lambda d_, s, p: d_ and s and p),
         ("D ∩ S", lambda d_, s, p: d_ and s),
         ("(D ∪ S) − P", lambda d_, s, p: (d_ or s) and not p)],
        q="In a three-circle diagram of Doctors (D), Singers (S) and Players (P), which expression shows the people who are **doctors and singers but not players**?",
        solution="The phrase needs D and S together, with P removed: **(D ∩ S) − P**, the single D-S-only region. D ∩ S alone also contains the all-three region; D ∩ S ∩ P is only the all-three region; (D ∪ S) − P also includes people who are only doctors or only singers.",
        shortcut="'And' → ∩, 'but not' → −. Check whether the all-three region sneaks in.",
        diff="easy", sub=I, pat="vn-p1", t=40),
 expr_q("venn-idea-p02", lambda a, b, c: (a or b) and not (a and b),
        ("(A ∪ B) − (A ∩ B)", lambda a, b, c: (a or b) and not (a and b)),
        [("A ∪ B", lambda a, b, c: a or b),
         ("A ∩ B", lambda a, b, c: a and b),
         ("A − B", lambda a, b, c: a and not b)],
        q="Which expression shows the elements that belong to **exactly one of A and B**?",
        solution="Exactly one = in A or B, but not in both: **(A ∪ B) − (A ∩ B)**, which is only A + only B. A ∪ B also includes the overlap; A ∩ B is the overlap itself; A − B misses the only-B part.",
        shortcut="Exactly one = union minus overlap.",
        diff="medium", sub=I, pat="vn-p1"),
 expr_q("venn-idea-p03", lambda a, b, c: c and not a and not b,
        ("C − (A ∪ B)", lambda a, b, c: c and not (a or b)),
        [("C − (A ∩ B)", lambda a, b, c: c and not (a and b)),
         ("C − A", lambda a, b, c: c and not a),
         ("(A ∪ B) − C", lambda a, b, c: (a or b) and not c)],
        q="Which expression shows the elements that are **in C but in neither A nor B**?",
        solution="'Neither A nor B' means outside A **and** outside B, i.e. outside A ∪ B. So the set is **C − (A ∪ B)** = only C. C − (A ∩ B) wrongly keeps C-elements that are in just one of A, B; C − A still keeps the B-C-only region; (A ∪ B) − C is the opposite region.",
        shortcut="Neither A nor B = remove the union, not the overlap.",
        diff="hard", sub=I, pat="vn-p1", t=55),
 Q("venn-idea-p04", S1TXT + "How many people use **at least two** of the three sources?",
   str(s1_two_plus), ["25", "45", "31"],
   "At least two = the three exactly-two regions + all three = 15 + 6 + 4 + 10 = **35**. 25 misses the all-three region; 45 wrongly adds the 'none' group.",
   "At least two = exactly-two regions + centre.", "easy", I, "vn-p2", 40, check=s1_two_plus),
 Q("venn-idea-p05", S1TXT + "How many people **read the newspaper** (with or without other sources)?",
   str(s1_N), ["20", "39", "35"],
   "All four regions inside N: only N 20 + N-T 15 + N-R 4 + all three 10 = **49**. 20 is only-N; 39 forgets the all-three region.",
   "A whole circle = its 4 regions.", "medium", I, "vn-p2", check=s1_N),
 Q("venn-idea-p06", S1TXT + "How many people use the **newspaper or the radio but not TV**?",
   str(s1_NR_notT), ["25", "39", "45"],
   "Regions in N or R and outside T: only N 20 + only R 5 + N-R only 4 = **29**. 25 forgets the N-R region; 39 wrongly adds the all-three region, which contains TV watchers.",
   "Remove every region that touches T.", "medium", I, "vn-p2", check=s1_NR_notT),
 Q("venn-idea-p07", "Three circles are drawn so that every pair overlaps and there is a region common to all three. Counting the space outside all circles, how many separate **regions** does the diagram have?",
   str(n_regions3), ["7", "6", "9"],
   "Each region is a yes/no choice for each circle: 2 × 2 × 2 = **8** (7 inside the circles + 1 outside). 7 forgets the outside region.",
   "n circles → 2ⁿ regions including outside.", "easy", I, "vn-p3", 30, check=n_regions3),
 Q("venn-idea-p08", "In a standard diagram of three mutually intersecting circles A, B and C, **how many regions** together make up circle A?",
   str(n_inA), ["3", "1", "7"],
   "Circle A is split by B and C into: only A, A-B only, A-C only and all three = **4** regions. 1 is only A; 3 forgets the centre.",
   "A region inside A is a yes/no choice for B and C: 2 × 2 = 4.", "medium", I, "vn-p3", 35, check=n_inA),
 Q("venn-idea-p09", "Two intersecting circles are drawn inside a rectangle that stands for the universal set. How many separate **regions** does the picture have?",
   str(n_regions2), ["3", "2", "5"],
   "Only A, only B, both, and the part of the rectangle outside both circles = **4**. 3 forgets the outside region.",
   "Two circles → 2² = 4 regions.", "easy", I, "vn-p3", 30, check=n_regions2),
 Q("venn-idea-p10", S1TXT + "How many people use **exactly one** source?",
   str(s1_one), ["65", "35", "45"],
   "Exactly one = only N + only T + only R = 20 + 25 + 5 = **50**. 65 wrongly adds the 15 who use none; 35 is the at-least-two count.",
   "Exactly one = the three 'only' regions.", "medium", I, "vn-p4", check=s1_one),
 Q("venn-idea-p11", S1TXT + "How many people **do not watch TV**?",
   str(s1_notT), ["56", "75", "29"],
   "TV regions = 25 + 15 + 6 + 10 = 56, so not TV = 100 − 56 = **44**. 75 subtracts only the 'only T' region; 29 forgets the 15 who use nothing.",
   "Not T = total − whole T circle (the none group stays in).", "easy", I, "vn-p4", 40, check=s1_notT),
 Q("venn-idea-p12", S1TXT + "How many people use **at most one** of the three sources?",
   str(s1_atmost1), ["50", "85", "35"],
   "At most one = exactly one + none = 50 + 15 = **65**. 50 forgets that zero sources is also 'at most one'; 35 is the at-least-two count.",
   "At most one = total − at least two = 100 − 35.", "hard", I, "vn-p4", 55, check=s1_atmost1),
]

# ================= two-set =================
r = two(90, 70, 40, 150)
t01 = r[(0, 0)]
r = two(140, 120, 140 + 120 - (250 - 30), 250)
t02 = r[(0, 1)]
t03 = 30 + 15 + 8
onlyCF = 46 - 6 - 10
onlyF = onlyCF // 3
onlyC = 2 * onlyF
assert onlyC + onlyF == onlyCF
t04 = onlyC + 10
neither_pct = 100 - (65 + 40 - 20)
t05 = 3000 * 100 // neither_pct
assert t05 * neither_pct == 3000 * 100
pass_both_pct = 100 - (35 + 25 - 10)
t06 = 250 * 100 // pass_both_pct
t07 = max(0, 45 + 35 - 60)
t08 = 80 - max(50, 40)
# brute-force the extreme cases for t07/t08 over every feasible overlap
feas = [x for x in range(0, 61) if 45 - x >= 0 and 35 - x >= 0 and 60 - (80 - x) >= 0]
assert min(feas) == t07
feas2 = [80 - (90 - x) for x in range(0, 41) if 80 - (90 - x) >= 0]
assert max(feas2) == t08

NEW += [
 Q("two-set-operations-p01", "In a housing society of **150 families, 90 have a car, 70 have a two-wheeler and 40 have both**. How many families have **neither**?",
   str(t01), ["70", "40", "10"],
   "At least one = 90 + 70 − 40 = 120. Neither = 150 − 120 = **30**. 70 comes from 150 − (50 + 30), which forgets the 40 families who have both.",
   "Neither = total − (A + B − both).", "easy", TW, "vn-p5", 40, check=t01),
 Q("two-set-operations-p02", "Of **250 employees, 140 speak Hindi, 120 speak Telugu and 30 speak neither**. How many speak **only Telugu**?",
   str(t02), ["120", "40", "100"],
   "At least one = 250 − 30 = 220. Both = 140 + 120 − 220 = 40. Only Telugu = 120 − 40 = **80**. 40 is the 'both' figure; 100 is only Hindi.",
   "Find both first, then subtract it from the circle.", "medium", TW, "vn-p5", check=t02),
 Q("two-set-operations-p03", "In a group, **30 people like mango, 15 like only guava, 12 like both mango and guava, and 8 like neither**. How many people are in the group?",
   str(t03), ["65", "41", "45"],
   "The 30 mango-lovers already include the 12 who like both. Group = mango 30 + only guava 15 + neither 8 = **53**. 65 adds the 12 a second time.",
   "Check whether a given figure is a whole circle or an 'only' region.", "medium", TW, "vn-p6", check=t03),
 Q("two-set-operations-p04", "In a class of **46 students, 10 play both cricket and football and 6 play neither**. The number who play **only cricket is twice** the number who play only football. How many play **cricket**?",
   str(t04), ["20", "40", "26"],
   "Only C + only F = 46 − 6 − 10 = 30, with only C = 2 × only F → only F = 10, only C = 20. Cricket = only C + both = 20 + 10 = **30**. 20 is only cricket.",
   "Fill the four boxes; the ratio splits the 'only' total.", "medium", TW, "vn-p6", 55, check=t04),
 Q("two-set-operations-p05", "In a town, **65% of adults read a Hindi paper, 40% read an English paper and 20% read both**. If **3,000 adults read neither**, how many adults are there in the town?",
   f"{t05:,}", ["15,000", "4,500", "30,000"],
   f"Read at least one = 65 + 40 − 20 = 85%, so neither = {neither_pct}%. {neither_pct}% = 3,000 → total = 3,000 × 100 ÷ {neither_pct} = **20,000**.",
   "Find the percent of the known group, then scale up.", "medium", TW, "vn-p7", check=f"{t05:,}"),
 Q("two-set-operations-p06", "In an examination, **35% of candidates failed in Mathematics, 25% failed in English and 10% failed in both**. If **250 candidates passed in both** subjects, how many candidates appeared?",
   str(t06), ["625", "400", "1000"],
   f"Failed at least one = 35 + 25 − 10 = 50%, so passed both = {pass_both_pct}%. Total = 250 × 100 ÷ {pass_both_pct} = **500**. 625 comes from 100 − 35 − 25 = 40%, which forgets to add back the 10% who failed both.",
   "Passed both = 100 − (fail₁ + fail₂ − fail both).", "hard", TW, "vn-p7", 60, check=t06),
 Q("two-set-operations-p07", "In a class of **60 students, 45 like tea and 35 like coffee**. What is the **minimum** number of students who like both?",
   str(t07), ["35", "10", "0"],
   "The circles can be pushed apart only until they fill the class: 45 + 35 − 60 = **20** must overlap. 35 is the *maximum* (coffee fully inside tea); 0 is impossible because 45 + 35 > 60.",
   "Min both = A + B − N (not below 0).", "medium", TW, "vn-p8", check=t07),
 Q("two-set-operations-p08", "In a group of **80 people, 50 like cricket and 40 like hockey**. What is the **maximum** number of people who like **neither** game?",
   str(t08), ["0", "10", "40"],
   "Neither is largest when the circles cover as few people as possible — hockey fully inside cricket. Then at least one = 50 and neither = 80 − 50 = **30**. 0 is the minimum; 10 is the minimum overlap.",
   "Max neither = N − larger set.", "hard", TW, "vn-p8", 55, check=t08),
]

# ================= three-set =================
h01r = three(30, 25, 20, 10, 8, 7, 4, total=60)
h01 = h01r[(0, 0, 0)]
h02r = three(50, 40, 30, 20, 15, 10, 5, total=100)
h02 = h02r[(0, 0, 0)]
h03r = three(40, 35, 30, 15, 12, 10, 5)
h03 = cnt(h03r, lambda a, b, c: a + b + c == 2)
h04r = three(30, 28, 25, 12, 10, 9, 4, total=70)
h04 = cnt(h04r, lambda a, b, c: a + b + c == 1)
h05r = three(45, 38, 30, 15, 10, 12, 6)
h05 = h05r[(1, 0, 0)]
# Hindi (H), Kannada (K), Tamil (T): H 35, K 40, T 30, HK 18, KT 15, HT 12, HKT 7
h06r = three(35, 40, 30, 18, 15, 12, 7)
h06 = h06r[(0, 1, 0)]
h07 = next(x for x in range(0, 50) if 25 + 30 + 20 - 10 - 8 - 7 + x == 55)
three(25, 30, 20, 10, 8, 7, h07)
h08_all = 100 - 60 - 30
h08 = 60 + 2 * 30 + 3 * h08_all

NEW += [
 Q("three-set-operations-p01", "A sports club has **60 members: 30 play cricket, 25 play football and 20 play hockey; 10 play cricket and football, 8 play football and hockey, 7 play cricket and hockey, and 4 play all three**. How many members play **none** of the three?",
   str(h01), ["10", "14", "4"],
   "Union = 30 + 25 + 20 − 10 − 8 − 7 + 4 = 54. None = 60 − 54 = **6**. 10 comes from forgetting to add back the 4 who play all three.",
   "Union = ΣA − Σpairs + triple.", "easy", TH, "vn-p9", 50, check=h01),
 Q("three-set-operations-p02", "In a survey, **50% of people like Hindi songs, 40% like Tamil songs and 30% like Punjabi songs; 20% like Hindi and Tamil, 15% like Tamil and Punjabi, 10% like Hindi and Punjabi, and 5% like all three**. What percentage like **none** of the three?",
   f"{h02}%", ["25%", "15%", "30%"],
   "Union = 50 + 40 + 30 − 20 − 15 − 10 + 5 = 80%. None = 100 − 80 = **20%**. 25% forgets the '+ 5'.",
   "Percent data works exactly like counts.", "medium", TH, "vn-p9", check=f"{h02}%"),
 Q("three-set-operations-p03", "For three sets, **|A ∩ B| = 15, |B ∩ C| = 12, |A ∩ C| = 10 and |A ∩ B ∩ C| = 5**. How many elements belong to **exactly two** of the sets?",
   str(h03), ["37", "27", "32"],
   "Each pairwise figure contains the triple once: (15 − 5) + (12 − 5) + (10 − 5) = 10 + 7 + 5 = **22**. 37 is the raw pairwise sum; 27 is 'at least two' (22 + 5).",
   "Exactly two = Σpairs − 3 × triple.", "medium", TH, "vn-p10", check=h03),
 Q("three-set-operations-p04", "In a school club of **70 students, 30 take Music, 28 take Dance and 25 take Drama; 12 take Music and Dance, 10 take Dance and Drama, 9 take Music and Drama, and 4 take all three**. How many take **exactly one** activity?",
   str(h04), ["56", "45", "19"],
   "Only Music = 30 − 12 − 9 + 4 = 13; only Dance = 28 − 12 − 10 + 4 = 10; only Drama = 25 − 10 − 9 + 4 = 10. Exactly one = **33**. 56 is the union; 19 is exactly two.",
   "Exactly one = union − exactly two − triple = 56 − 19 − 4.", "medium", TH, "vn-p10", 60, check=h04),
 Q("three-set-operations-p05", "For three sets, **|A| = 45, |A ∩ B| = 15, |A ∩ C| = 12 and |A ∩ B ∩ C| = 6**. How many elements are in **only A**?",
   str(h05), ["18", "30", "33"],
   "Only A = 45 − 15 − 12 + 6 = **24**. Subtracting both pairs removes the triple twice, so it is added back once; 18 forgets that.",
   "Only A = A − AB − AC + ABC.", "medium", TH, "vn-p11", check=h05),
 Q("three-set-operations-p06", "In an office, **40 people speak Kannada; 18 speak Kannada and Hindi, 15 speak Kannada and Tamil, and 7 speak all three languages**. How many speak **only Kannada**?",
   str(h06), ["7", "22", "33"],
   "Only Kannada = 40 − 18 − 15 + 7 = **14**. 7 forgets to add back the 7 who were subtracted twice; 22 subtracts only the Hindi overlap.",
   "Subtract both pairs, add the triple back once.", "medium", TH, "vn-p11", check=h06),
 Q("three-set-operations-p07", "For three sets, **|A| = 25, |B| = 30, |C| = 20, |A ∩ B| = 10, |B ∩ C| = 8, |A ∩ C| = 7** and **|A ∪ B ∪ C| = 55**. How many elements are in **all three** sets?",
   str(h07), ["10", "0", "3"],
   "55 = 25 + 30 + 20 − 10 − 8 − 7 + x = 50 + x → x = **5**. Check: only A = 13, only B = 17, only C = 10 — no region is negative.",
   "Rearrange the master formula for the missing term.", "hard", TH, "vn-p12", 55, check=h07),
 Q("three-set-operations-p08", "Each of **100 people reads at least one of three magazines. 60 read exactly one and 30 read exactly two**. What is the **sum of the readerships** of the three magazines?",
   str(h08), ["100", "120", "130"],
   f"All three = 100 − 60 − 30 = {h08_all}. A reader of two magazines is counted twice and a reader of three is counted three times: 60 + 2 × 30 + 3 × {h08_all} = **150**. 100 counts each person once.",
   "ΣA = exactly one + 2 × exactly two + 3 × all three.", "hard", TH, "vn-p12", 60, check=h08),
]

# ================= relation diagrams =================
nat = {x for x in Z if x >= 1}
whole = {x for x in Z if x >= 0}
even = {x for x in Z if x % 2 == 0}
odd = {x for x in Z if x % 2 == 1}
m3 = {x for x in Z if x % 3 == 0}
m4 = {x for x in Z if x % 4 == 0}
m5 = {x for x in Z if x % 5 == 0}
m7 = {x for x in Z if x % 7 == 0}
m35 = {x for x in Z if x % 35 == 0}
primes = {x for x in Z if x > 1 and all(x % k for k in range(2, int(x ** 0.5) + 1))}
nat_h = {x for x in HALVES if x.denominator == 1 and x >= 1}
int_h = {x for x in HALVES if x.denominator == 1}
neg_h = {x for x in HALVES if x < 0}

REL_NEW = [
 dq("relation-diagrams-p01", ["Natural numbers", "Whole numbers", "Integers"],
    rels_from_sets([nat, whole, Z]), ["two_in", "in_out", "all_over"],
    "Every natural number (1, 2, 3, …) is a whole number, and every whole number (0, 1, 2, …) is an integer → **three nested circles**.",
    "Each word is a type of the next → nested.", "easy", "vn-p13"),
 dq("relation-diagrams-p02", ["Sparrows", "Birds", "Animals"],
    {(0, 1): "sub", (1, 2): "sub", (0, 2): "sub"}, ["two_in", "in_cross", "all_over"],
    "Every sparrow is a bird and every bird is an animal → **three nested circles**.",
    "Type of a type → nested chain.", "easy", "vn-p13", 30),
 dq("relation-diagrams-p03", ["Pens", "Pencils", "Stationery"],
    {(0, 1): "dis", (0, 2): "sub", (1, 2): "sub"}, ["nested", "two_ovl_in", "all_sep"],
    "Pens and pencils are both stationery, but nothing is both a pen and a pencil → **two separate circles inside a third**.",
    "Two kinds of one thing that cannot overlap.", "easy", "vn-p14", 30),
 dq("relation-diagrams-p04", ["Whales", "Mammals", "Fish"],
    {(0, 1): "sub", (0, 2): "dis", (1, 2): "dis"}, ["two_in", "in_cross", "nested"],
    "Every whale is a mammal. No fish is a mammal, so fish share nothing with mammals or whales → **one circle inside a second; the third separate from both**.",
    "Test the third word against both circles.", "medium", "vn-p14"),
 dq("relation-diagrams-p05", ["Even numbers", "Multiples of 3", "Integers"],
    rels_from_sets([even, m3, Z]), ["two_in", "nested", "in_overlap"],
    "Both are sets of integers. 6 is even and a multiple of 3, 4 is only even, 9 is only a multiple of 3 → they intersect. So **two intersecting circles inside a third**.",
    "Two subsets of the big set — check whether they share members (6 does).", "medium", "vn-p14"),
 dq("relation-diagrams-p06", ["Teachers", "Women", "Singers"],
    {(0, 1): "ovl", (0, 2): "ovl", (1, 2): "ovl"}, ["all_sep", "two_ovl_in", "in_cross"],
    "A teacher may or may not be a woman or a singer, and a woman may or may not sing; all three can meet in one person → **three circles, each pair intersecting**.",
    "No word is a type of another and every pair can share → all intersect.", "easy", "vn-p15", 30),
 dq("relation-diagrams-p07", ["Women", "Engineers", "Rivers"],
    {(0, 1): "ovl", (0, 2): "dis", (1, 2): "dis"}, ["all_over", "two_sep_cross", "all_sep"],
    "Some women are engineers → those two intersect. A river is neither a woman nor an engineer → **two intersecting circles and a third separate circle**.",
    "Decide each pair; a non-person category stands apart.", "medium", "vn-p15"),
 dq("relation-diagrams-p08", ["Even numbers", "Odd numbers", "Prime numbers"],
    rels_from_sets([even, odd, primes]), ["all_over", "in_cross", "two_in"],
    "No number is both even and odd → separate. 2 is even and prime, 3 is odd and prime, while 4 and 9 are not prime → the Prime circle cuts both. Answer: **two separate circles, with the third intersecting both**.",
    "Test with 2, 3, 4, 9.", "hard", "vn-p15", 55),
 dq("relation-diagrams-p09", ["Fathers", "Men", "Doctors"],
    {(0, 1): "sub", (0, 2): "ovl", (1, 2): "ovl"}, ["in_out", "all_over", "in_cross_outer"],
    "Every father is a man → Fathers inside Men. Some fathers are doctors and some are not; some men are doctors → the Doctors circle crosses both. Answer: **one circle inside a second; the third intersecting both**.",
    "Draw the subset first, then test the third word against inner and outer.", "medium", "vn-p16"),
 dq("relation-diagrams-p10", ["Multiples of 4", "Multiples of 2", "Multiples of 3"],
    rels_from_sets([m4, even, m3]), ["two_ovl_in", "in_out", "in_overlap"],
    "Every multiple of 4 is a multiple of 2 → inside. 12 is a multiple of 4 (and 2) and of 3; 6 is a multiple of 2 and 3 but not 4; 9 is a multiple of 3 only → the third circle crosses both. Answer: **one circle inside a second; the third intersecting both**.",
    "Check 12, 6 and 9.", "medium", "vn-p16", 50),
 dq("relation-diagrams-p11", ["Multiples of 5", "Multiples of 7", "Multiples of 35"],
    rels_from_sets([m5, m7, m35]), ["two_ovl_in", "two_sep_cross", "nested"],
    "35 = 5 × 7, so every multiple of 35 is a multiple of both 5 and 7. Multiples of 5 and 7 overlap (35, 70) but neither contains the other (10, 14). Answer: **two intersecting circles, with the third inside their common part**.",
    "A common multiple sits in the overlap.", "medium", "vn-p16", 50),
 dq("relation-diagrams-p12", ["Natural numbers", "Integers", "Negative numbers"],
    rels_from_sets([nat_h, int_h, neg_h]), ["in_cross", "in_out", "two_sep_cross"],
    "Every natural number is an integer → inside. −1 is a negative integer, but −½ is negative and not an integer → Negative numbers cut Integers. No natural number is negative → it stays away from the inner circle. Answer: **one circle inside a second; the third intersecting only the outer circle**.",
    "Test −1 and −½; the third circle can touch the outer circle only.", "hard", "vn-p16", 60),
]
NEW += REL_NEW

upsert(d["practice"], NEW)
set_sub(d, I, notes=NOTES_IDEA, patterns=P_IDEA)
set_sub(d, TW, notes=NOTES_TWO, patterns=P_TWO)
set_sub(d, TH, notes=NOTES_THREE, patterns=P_THREE)
set_sub(d, R, notes=NOTES_REL, patterns=P_REL)
d["pyqPatterns"] = PYQS

# ---------------- re-check of existing questions (report only) ----------------
def ans_of(qid):
    for q in d["solvedExamples"] + d["practice"]:
        if q["id"] == qid:
            return q["options"][q["answer"]]


EXIST = {
    "rsn-venn-ex1": 60 - (35 + 30 - 10),
    "rsn-venn-ex2": (8 - 3) + (7 - 3) + (6 - 3),
    "rsn-venn-ex4": 200 - sum(three(90, 80, 70, 40, 35, 30, 15).values()),
    "rsn-venn-1": 40 - 15 - 12,
    "rsn-venn-2": 40 + 25 - 12,
    "rsn-venn-3": f"{100 - (70 + 60 - 40)}%",
    "rsn-venn-4": 50 + 40 - 80,
    "rsn-venn-5": sum(three(30, 25, 20, 8, 7, 6, 3).values()),
    "rsn-venn-6": 45 - 25,
    "rsn-venn-7": 15 + 10 + 8 + 6 + 5 + 4 + 2,
    "rsn-venn-8": cnt(three(22, 19, 17, 9, 7, 6, 4), lambda a, b, c: a + b + c == 1),
    "rsn-venn-11": 8 + 10 + (20 - 8) + 7,
    "rsn-venn-12": (25 - 8) + (20 - 8),
    "rsn-venn-13": 120 - sum(three(55, 45, 40, 20, 18, 15, 8).values()),
    "rsn-venn-14": cnt(three(99, 99, 99, 12, 10, 9, 5), lambda a, b, c: a + b + c >= 2),
    "rsn-venn-ex3": SHAPE["all_over"],
    "rsn-venn-9": None,  # nested (text differs from SHAPE wording) - checked by classify below
}
assert classify({(0, 1): "sub", (1, 2): "sub", (0, 2): "sub"}) == "nested"
assert classify({(0, 1): "sup", (0, 2): "ovl", (1, 2): "ovl"}) == "in_cross"      # Mothers, Females, Engineers
assert classify({(0, 1): "sup", (0, 2): "sup", (1, 2): "dis"}) == "two_in"        # Words, English, Hindi
bad = []
for qid, v in EXIST.items():
    if v is None or qid == "rsn-venn-ex3":
        continue
    if str(v) != ans_of(qid):
        bad.append((qid, v, ans_of(qid)))
print("existing-question re-check:", "ALL MATCH" if not bad else bad)

errs = finish(T, d)
assert not errs, errs
