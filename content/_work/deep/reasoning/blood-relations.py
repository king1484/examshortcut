"""Blood-relations topic build: notes + patterns + practice + pyqPatterns.

Every answer is derived from a coded family tree (Fam + rel2) inside this script.
"""
import os
import re
import sys
from collections import defaultdict

sys.path.insert(0, os.path.dirname(__file__))
from _lib import *  # noqa
from blood_relations_notes import NOTES, PATTERNS

d = load("blood-relations")

# ---------------------------------------------------------------- tree engine
class Fam:
    def __init__(s):
        s.sex, s.par, s.kids, s.sp = {}, defaultdict(set), defaultdict(set), {}

    def person(s, n, sex=None):
        s.sex.setdefault(n, sex)
        return n

    def child(s, p, c):
        s.person(p); s.person(c)
        s.par[c].add(p); s.kids[p].add(c)

    def marry(s, a, b):
        s.sp[a] = b; s.sp[b] = a

    def sib(s, a, b):
        return bool(s.par[a] and s.par[b] and (s.par[a] & s.par[b]))

    def eff_par(s, c):
        out = set(s.par[c])
        for p in list(s.par[c]):
            if p in s.sp:
                out.add(s.sp[p])
        return out

    def eff_kids(s, a):
        out = set(s.kids[a])
        if a in s.sp:
            out |= s.kids[s.sp[a]]
        return out


def up(f, x, y):
    """Generations from x up to ancestor y (1 = parent); None if y is not an ancestor."""
    cur, level = {x}, 0
    while cur and level < 6:
        level += 1
        nxt = set()
        for p in cur:
            nxt |= f.eff_par(p)
        if y in nxt:
            return level
        cur = nxt
    return None


def rel(f, a, b):
    """Blood relation: a is b's ___ (None if ambiguous or not blood)."""
    g = f.sex.get(a)
    k = up(f, b, a)          # a is an ancestor of b
    if k == 1:
        return {"M": "father", "F": "mother"}.get(g)
    if k == 2:
        return {"M": "grandfather", "F": "grandmother"}.get(g)
    if k and k >= 3:
        return {"M": "great-grandfather", "F": "great-grandmother"}.get(g)
    k = up(f, a, b)          # a is a descendant of b
    if k == 1:
        return {"M": "son", "F": "daughter"}.get(g)
    if k == 2:
        return {"M": "grandson", "F": "granddaughter"}.get(g)
    if k and k >= 3:
        return {"M": "great-grandson", "F": "great-granddaughter"}.get(g)
    if f.sib(a, b):
        return {"M": "brother", "F": "sister"}.get(g)
    for p in f.par[b]:                       # a is b's uncle/aunt
        if f.sib(a, p):
            return {"M": "uncle", "F": "aunt"}.get(g)
    for p in f.eff_par(a):                   # a is b's nephew/niece
        if p != b and f.sib(p, b):
            return {"M": "nephew", "F": "niece"}.get(g)
    for pa in f.par[a]:                      # cousins
        for pb in f.par[b]:
            if pa != pb and f.sib(pa, pb):
                return "cousin"
    return None


def rel2(f, a, b):
    """rel() plus one marriage crossing (-in-law); the head word keeps a's gender."""
    r = rel(f, a, b)
    if r:
        return r
    if b in f.sp:
        r = rel(f, a, f.sp[b])
        if r:
            return r + "-in-law"
    if a in f.sp:
        r = rel(f, f.sp[a], b)
        if not r:
            return None
        g = f.sex.get(a)
        if r in ("father", "mother"):
            return "father-in-law" if g == "M" else "mother-in-law"
        if r in ("son", "daughter"):
            return "son-in-law" if g == "M" else "daughter-in-law"
        if r in ("brother", "sister"):
            return "brother-in-law" if g == "M" else "sister-in-law"
        if r in ("uncle", "aunt"):
            return "uncle" if g == "M" else "aunt"
        if r in ("nephew", "niece"):
            return "nephew" if g == "M" else "niece"
    return None


_TOK = re.compile(r"[A-Za-z]+|[^A-Za-z\s]")


def coded(expr, defs, seed=0):
    """Build a Fam from 'A+B-C' and defs {op: (relation-of-first-to-second, first's sex)}."""
    f = Fam()
    toks = _TOK.findall(expr.replace(" ", ""))
    people = {}
    n = [0]

    def nm(t):
        if t not in people:
            n[0] += 1
            people[t] = f"P{n[0]}"
        return people[t]

    sibops = []
    for i in range(0, len(toks) - 1, 2):
        a, op, b = toks[i], toks[i + 1], toks[i + 2]
        A, B = nm(a), nm(b)
        rname, g = defs[op]
        f.person(A)
        f.sex[A] = g  # a symbol's gender is authoritative
        if rname in ("father", "mother"):
            f.child(A, B)
        elif rname in ("son", "daughter"):
            f.child(B, A)
        elif rname in ("brother", "sister"):
            sibops.append((A, B))  # defer: merge parents once parent links exist
        elif rname in ("husband", "wife"):
            f.marry(A, B)
        else:
            raise ValueError(rname)
    for A, B in sibops:
        pb = sorted(f.par[B])
        pa = sorted(f.par[A])
        if not pb and not pa:
            n[0] += 1
            p = f"#u{n[0]}"
            f.person(p)
            f.child(p, B)
            f.child(p, A)
        else:
            for p in sorted(set(pb) | set(pa)):
                f.child(p, A)
                f.child(p, B)
    return f, people


# self-test of the engine against the topic's own solved examples
_f = Fam()
_f.person("D", "M"); _f.person("C", "F"); _f.person("A", "F"); _f.person("B", "M")
_f.child("D", "C"); _f.child("C", "A"); _f.child("C", "B")
assert rel2(_f, "A", "D") == "granddaughter"
assert rel2(_f, "D", "A") == "grandfather"
_f2 = Fam(); _f2.person("Mohan", "M"); _f2.person("Rekha", "F"); _f2.person("Ramesh", "M")
_f2.child("Mohan", "Rekha"); _f2.child("Ramesh", "Mohan")
assert rel2(_f2, "Ramesh", "Rekha") == "grandfather"
_f3, pp = coded("A+B÷C", {"+": ("son", "M"), "÷": ("wife", "F")})
assert rel2(_f3, pp["A"], pp["C"]) == "son"
_f4 = Fam()
for nme, sx in (("P", "M"), ("Q", "F"), ("R", "M"), ("S", "M"), ("T", "F")):
    _f4.person(nme, sx)
_f4.marry("P", "Q"); _f4.child("P", "R"); _f4.child("P", "S"); _f4.marry("R", "T")
assert rel2(_f4, "S", "T") == "brother-in-law"

# ---------------------------------------------------------------- wiring
for sid, notes in NOTES.items():
    set_sub(d, sid, notes=notes, patterns=PATTERNS[sid])

NQ = []
_ctr = {}


def A(sub, pat, q, ans, wrong, solution, diff="medium", shortcut=None, t=45):
    _ctr[sub] = _ctr.get(sub, 0) + 1
    NQ.append(Q(f"{sub}-p{_ctr[sub]:02d}", q, ans, wrong, solution, shortcut=shortcut,
                diff=diff, sub=sub, pat=pat, t=t))


# ================= blood-relations-idea =================
# p01
f = Fam(); f.person("Sunita", "F"); f.person("Deepak", "M"); f.child("Sunita", "Deepak")
assert rel2(f, "Deepak", "Sunita") == "son"
A("blood-relations-idea", "br-p1", "**Sunita is the mother of Deepak.** How is **Deepak related to Sunita**?",
  "Son", ["Brother", "Nephew", "Father"],
  "One arrow runs from Sunita down to Deepak. Asked from Sunita's side, Deepak sits one generation below and is male → her **son**. (Brother would need a shared parent with Sunita; nephew needs Deepak to be a sibling's child.)",
  diff="easy", shortcut="Start from the person named after 'related to'; count arrows from there.")
# p02
f = Fam(); f.person("Ravi", "M"); f.person("Meena", "F"); f.person("Shobha", "F")
f.child("Meena", "Ravi"); f.child("Shobha", "Meena")
assert rel2(f, "Shobha", "Ravi") == "grandmother"
A("blood-relations-idea", "br-p1", "**Ravi is the son of Meena. Meena is the daughter of Shobha.** How is **Shobha related to Ravi**?",
  "Grandmother", ["Grandfather", "Mother", "Aunt"],
  "Ravi ↑ Meena ↑ Shobha: two arrows up from Ravi, and Shobha is female → **grandmother**. (Aunt would need Shobha to be a sibling of a parent.)",
  diff="easy", shortcut="Two up-arrows = grandparent level; the gender picks the exact word.")
# p03
f = Fam(); f.person("P", "M"); f.person("Q", "F"); f.person("R", "M")
f.marry("P", "Q"); f.child("R", "P")
assert rel2(f, "R", "Q") == "father-in-law"
A("blood-relations-idea", "br-p1", "**P is the husband of Q. R is the father of P.** How is **R related to Q**?",
  "Father-in-law", ["Father", "Uncle", "Brother-in-law"],
  "P and Q are married; R is P's father. One marriage crossing from 'father' → R is Q's **father-in-law**.",
  diff="medium", shortcut="Husband's father = father-in-law; every marriage line adds '-in-law'.")
# p04
f = Fam(); f.person("A", "F"); f.person("B"); f.person("C", "F")
f.child("C", "A"); f.child("C", "B")
assert f.sex.get("B") is None and rel2(f, "B", "C") is None
A("blood-relations-idea", "br-p2", "**A is the sister of B. C is the mother of A and B.** How is **B related to C**?",
  "Cannot be determined", ["Son", "Daughter", "Brother"],
  "B shares C with A, so B is C's child. But no word in the question fixes B's gender ('sibling' words fix nothing) → **cannot be determined**. (Assuming 'brother' because A is a sister is exactly the planted error.)",
  diff="medium", shortcut="Blank gender = blank answer; 'sister of B' tells us about A, never about B.")
# p05
f = Fam(); f.person("M", "M"); f.person("N", "F"); f.person("O", "M"); f.person("P")
f.child("N", "M"); f.child("#u1", "N"); f.child("#u1", "O"); f.child("O", "P")
assert rel2(f, "N", "P") == "aunt"
A("blood-relations-idea", "br-p2", "**M is the son of N. N is the sister of O. O is the father of P.** How is **N related to P**?",
  "Aunt", ["Uncle", "Mother", "Grandmother"],
  "O is P's father; N is O's sister. A parent's sister is an **aunt** — N's gender is fixed female by 'sister'. (Uncle is the mirror word; grandmother skips a generation.)",
  diff="medium", shortcut="Parent's sibling = uncle/aunt; 'sister' pins N female.")
# p06
f = Fam(); f.person("X", "F"); f.person("Y"); f.person("Z", "M"); f.person("W", "M")
f.child("X", "Y"); f.child("X", "Z"); f.child("W", "X")
assert rel2(f, "W", "Y") == "grandfather"
A("blood-relations-idea", "br-p2", "**X is the mother of Y. Z is the brother of Y. W is the father of X.** How is **W related to Y**?",
  "Grandfather", ["Grandmother", "Uncle", "Cannot be determined"],
  "W → X → Y: two arrows up from Y, and W is male → **grandfather**. Y's own gender is unknown, but the grandparent word never needs it. (Uncle would need W to be a sibling of a parent, not a parent of one.)",
  diff="medium", shortcut="Count the arrows first; Y's unknown gender does not block this answer.")
# p07
f = Fam(); f.person("R", "M"); f.person("S"); f.person("T", "F")
f.child("R", "S"); f.child("R", "T")
assert rel2(f, "T", "R") == "daughter"
A("blood-relations-idea", "br-p3", "**R is the father of S. T is the sister of S.** How is **T related to R**?",
  "Daughter", ["Son", "Niece", "Cousin"],
  "T and S share the parent R, so R → T as well. T is one arrow down from R and female → his **daughter**. (Niece needs T to be a sibling's child.)",
  diff="easy", shortcut="Siblings hang under the same arrow; one arrow down + female = daughter.")
# p08
f = Fam(); f.person("Deepa", "F"); f.person("Manoj", "M"); f.person("Kishan", "M")
f.child("Manoj", "Deepa"); f.child("Kishan", "Manoj")
assert rel2(f, "Deepa", "Kishan") == "granddaughter"
A("blood-relations-idea", "br-p3", "**Deepa is the daughter of Manoj. Manoj is the son of Kishan.** How is **Deepa related to Kishan**?",
  "Granddaughter", ["Grandson", "Daughter", "Niece"],
  "Deepa ↑ Manoj ↑ Kishan: two arrows up from Deepa, and Deepa is female → Kishan's **granddaughter**.",
  diff="easy", shortcut="Two down-arrows from Kishan land on Deepa — grandchild level.")
# p09
f = Fam(); f.person("A", "F"); f.person("B", "F"); f.person("C", "M")
f.child("B", "A"); f.child("B", "C")
assert f.kids["B"] == {"A", "C"} and f.sex["C"] == "M" and rel2(f, "C", "A") == "brother"
A("blood-relations-idea", "br-p3", "**A is the only daughter of B. B is the mother of C.** How is **C related to A**?",
  "Brother", ["Sister", "Cannot be determined", "Cousin"],
  "B has exactly one daughter (A), so C must be a **son**. A and C share the mother B → C is A's **brother**. The word 'only daughter' quietly fixes C's gender — that is the whole question.",
  diff="medium", shortcut="'Only daughter' = every other child is a boy.")
# p10
f = Fam()
f.person("H", "M"); f.person("W", "F")
for i in range(3):
    s = f"S{i}"; f.person(s, "M"); f.child("H", s); f.child("W", s)
    for j in range(2):
        g = f"G{i}{j}"; f.person(g, "F"); f.child(s, g)
nfem = sum(1 for x, sx in f.sex.items() if sx == "F")
assert nfem == 7
A("blood-relations-idea", "br-p4", "**A couple has 3 sons, and each son has 2 daughters. How many female members are in the family?**",
  "7", ["6", "8", "9"],
  "Count from the tree: the wife (1) + each son's 2 daughters (3 × 2 = 6) = **7** female members. The husband and the 3 sons are male; nobody else exists.",
  diff="medium", shortcut="Draw 8 boxes, tick the 7 females — never count in the air.")
# p11
f = Fam()
for nme, sx in (("P", "M"), ("Q", "F"), ("R", "M"), ("S", "F"), ("T", "M"), ("U", "F")):
    f.person(nme, sx)
f.marry("P", "Q"); f.child("P", "R"); f.marry("R", "S"); f.child("R", "U")
nfem = sum(1 for x, sx in f.sex.items() if sx == "F")
assert nfem == 3
A("blood-relations-idea", "br-p4", "**P and Q are a married couple, P is the husband. R is their son. S is R's wife. T is S's brother. U is R's daughter.** How many **female members** are in the family?",
  "3", ["2", "4", "Cannot be determined"],
  "Females: Q (the wife), S (R's wife) and U (R's daughter) = **3**. P, R and T are male — T's gender is fixed by 'brother', so nothing is left blank.",
  diff="medium", shortcut="Tick a gender under every name first; then the count is one line.")
# p12
f = Fam()
for nme, sx in (("GF", "M"), ("GM", "F"), ("SO", "M"), ("SW", "F"), ("K1", "M"), ("K2", "F")):
    f.person(nme, sx)
f.marry("GF", "GM"); f.child("GF", "SO"); f.marry("SO", "SW"); f.child("SO", "K1"); f.child("SO", "K2")
nmal = sum(1 for x, sx in f.sex.items() if sx == "M")
assert nmal == 3
A("blood-relations-idea", "br-p4", "**A family has a grandfather and his wife, their son and his wife, and the son's two children — one boy and one girl. How many male members are there?**",
  "3", ["2", "4", "5"],
  "Males: the grandfather, the son and the grandson = **3**. The grandmother, the daughter-in-law and the granddaughter are female. Six members in all, split 3 + 3.",
  diff="easy", shortcut="Two generations of couples plus two children; tick males only.")

# ================= family-tree-puzzles =================
# p01
f = Fam()
for nme, sx in (("Anil", "M"), ("Sunil", "M"), ("Mohan", "M"), ("Ritu", "F"), ("Kavita", "F")):
    f.person(nme, sx)
f.child("#g1", "Anil"); f.child("#g1", "Sunil"); f.child("Sunil", "Mohan"); f.child("Sunil", "Ritu")
f.marry("Sunil", "Kavita")
assert rel2(f, "Kavita", "Anil") == "sister-in-law"
A("family-tree-puzzles", "br-p8", "**Anil is the brother of Sunil. Sunil is the father of Mohan. Ritu is the daughter of Kavita. Mohan is the brother of Ritu.** How is **Kavita related to Anil**?",
  "Sister-in-law", ["Sister", "Mother", "Aunt"],
  "Mohan and Ritu share parents; Ritu's mother is Kavita, so Kavita is Sunil's wife. Wife of Anil's brother → Anil's **sister-in-law**. (Aunt would need Kavita on the parents' generation of Anil — she is on Anil's own row.)",
  shortcut="Rebuild top-down: the shared-parent sentence joins the scattered names.")
# p02
f = Fam()
for nme, sx in (("Ramesh", "M"), ("Vinod", "M"), ("Anita", "F"), ("Raju", "M")):
    f.person(nme, sx)
f.child("Ramesh", "Vinod"); f.child("Vinod", "Anita"); f.child("Anita", "Raju")
assert rel2(f, "Ramesh", "Raju") == "great-grandfather"
A("family-tree-puzzles", "br-p5", "**Ramesh is the father of Vinod. Vinod is the father of Anita. Anita is the mother of Raju.** How is **Ramesh related to Raju**?",
  "Great-grandfather", ["Grandfather", "Grandson", "Father"],
  "Ramesh → Vinod → Anita → Raju: three arrows up from Raju → great-grandparent level; male → **great-grandfather**. (Grandfather stops one generation short.)",
  diff="easy", shortcut="Three arrows = great-; two = grand-. Count before naming.")
# p03
f = Fam(); f.person("K", "F"); f.person("L", "M"); f.person("M", "M")
f.marry("K", "L"); f.child("M", "L")
assert rel2(f, "M", "K") == "father-in-law"
A("family-tree-puzzles", "br-p6", "**K is the wife of L. M is the father of L.** How is **M related to K**?",
  "Father-in-law", ["Father", "Uncle", "Brother-in-law"],
  "M is the father of K's husband → one marriage crossing from 'father' → **father-in-law**.",
  diff="easy", shortcut="Spouse's parent = mother/father-in-law, every time.")
# p04
f = Fam(); f.person("Ramesh", "M"); f.person("FA", "M"); f.person("Amit", "M")
f.child("Ramesh", "FA"); f.child("FA", "Amit")
assert rel2(f, "Ramesh", "Amit") == "grandfather"
A("family-tree-puzzles", "br-p5", "**Amit's father is the only son of Ramesh.** How is **Ramesh related to Amit**?",
  "Grandfather", ["Father", "Great-grandfather", "Uncle"],
  "'The only son of Ramesh' is a child of Ramesh — he is Amit's father. So Ramesh → (Amit's father) → Amit: two arrows up, male → **grandfather**.",
  diff="medium", shortcut="'Only son of X' is simply X's child (male); decode it and the chain is short.")
# p05
f = Fam()
for nme, sx in (("Dinesh", "M"), ("Gauri", "F"), ("Ashok", "M"), ("Nutan", "F"),
                ("Pankaj", "M"), ("Seema", "F"), ("Usha", "F"), ("Tinku", "M")):
    f.person(nme, sx)
f.marry("Dinesh", "Gauri"); f.child("Dinesh", "Ashok"); f.marry("Ashok", "Nutan")
f.child("Ashok", "Pankaj"); f.child("Ashok", "Seema"); f.marry("Pankaj", "Usha"); f.child("Pankaj", "Tinku")
nmal = sum(1 for x, sx in f.sex.items() if sx == "M")
assert nmal == 4
A("family-tree-puzzles", "br-p7", "**Dinesh and his wife Gauri have a son Ashok. Ashok married Nutan; their children are Pankaj and Seema. Pankaj married Usha; their son is Tinku.** How many **male members** are there?",
  "4", ["3", "5", "6"],
  "Tick genders on the tree: males are Dinesh, Ashok, Pankaj and Tinku = **4**. Females: Gauri, Nutan, Seema, Usha (4). Eight members in all.",
  shortcut="One +/− tick per name while reading; the count then takes five seconds.")
# p06
f = Fam(); f.person("Rahul", "M"); f.person("MOT", "F"); f.person("Vikas", "M"); f.person("Neha", "F")
f.child("#g1", "MOT"); f.child("#g1", "Vikas"); f.child("MOT", "Rahul"); f.child("Vikas", "Neha")
assert rel2(f, "Neha", "Rahul") == "cousin"
A("family-tree-puzzles", "br-p9", "**Rahul's mother's brother is Vikas. Vikas's daughter is Neha.** How is **Neha related to Rahul**?",
  "Cousin", ["Sister", "Niece", "Aunt"],
  "Vikas is a sibling of Rahul's mother; Neha is his child. Children of siblings → **cousin**. (Niece is the reverse — a sibling's child of Rahul would be Rahul's niece.)",
  diff="easy", shortcut="Two branches off one grandparent pair = cousins.")
# p07
f = Fam()
for nme, sx in (("A", "F"), ("B", "M"), ("C", "F"), ("D", "M")):
    f.person(nme, sx)
f.child("C", "A"); f.child("C", "B"); f.child("D", "C")
assert rel2(f, "A", "D") == "granddaughter"
A("family-tree-puzzles", "br-p5", "**A is B's sister. C is B's mother. D is C's father.** How is **A related to D**?",
  "Granddaughter", ["Daughter", "Niece", "Aunt"],
  "A and B share the mother C; C is D's daughter. So D → C → A: two arrows up from A, and A is female → D's **granddaughter**. (Niece would need A to be a child of D's *sibling* — she is a child of D's child.)",
  diff="hard", shortcut="Merge the sibling pair first; then it is one straight chain of two arrows.")
# p08
f = Fam()
for nme, sx in (("L", "M"), ("M", "M"), ("N", "F"), ("O", "F"), ("P", None)):
    f.person(nme, sx)
f.child("L", "M"); f.child("L", "N"); f.marry("M", "O"); f.child("N", "P")
assert rel2(f, "O", "P") == "aunt" and f.sex.get("P") is None
A("family-tree-puzzles", "br-p8", "**L is the father of M and N. M is the husband of O. N is the mother of P.** How is **O related to P**?",
  "Aunt", ["Mother", "Grandmother", "Sister"],
  "N is P's mother; M is N's brother; O is M's wife. So O is the wife of P's uncle → P's **aunt** (an aunt by marriage is still the aunt in these puzzles).",
  shortcut="Hang M and N under L first; the marriage and P slot in around them.")
# p09
f = Fam()
for nme, sx in (("Vijay", "M"), ("Reena", "F"), ("Sanjay", "M"), ("Meena", "F")):
    f.person(nme, sx)
f.marry("Vijay", "Reena"); f.child("#g1", "Reena"); f.child("#g1", "Sanjay"); f.marry("Sanjay", "Meena")
assert rel2(f, "Reena", "Meena") == "sister-in-law"
A("family-tree-puzzles", "br-p6", "**Vijay's wife Reena has a brother Sanjay. Sanjay's wife is Meena.** How is **Reena related to Meena**?",
  "Sister-in-law", ["Sister", "Cousin", "Aunt"],
  "Sanjay is Reena's brother, and Meena married him. A husband's sister is a **sister-in-law** — so Reena is Meena's sister-in-law.",
  diff="medium", shortcut="Sibling's spouse or spouse's sibling — both crossings give '-in-law'.")
# p10
f = Fam()
for nme, sx in (("MR", "M"), ("MS", "F"), ("S1", "M"), ("S2", "M"), ("DW", "F"), ("D1", "F"), ("D2", "F")):
    f.person(nme, sx)
f.marry("MR", "MS"); f.child("MR", "S1"); f.child("MR", "S2"); f.marry("S1", "DW")
f.child("S1", "D1"); f.child("S1", "D2")
nfem = sum(1 for x, sx in f.sex.items() if sx == "F")
assert nfem == 4
A("family-tree-puzzles", "br-p7", "**Mr. and Mrs. Rao have two sons. The elder son's wife and their two daughters also live with them.** How many **female members** are in the family?",
  "4", ["3", "5", "6"],
  "Females: Mrs. Rao, the daughter-in-law, and the two granddaughters = **4**. (Mr. Rao and the two sons are male.) Seven members in total.",
  shortcut="The two unmarried male sons are the decoys — tick genders, then count.")
# p11
f = Fam()
for nme, sx in (("Ravi", "M"), ("Sita", "F"), ("Geeta", "F"), ("Mohan", "M")):
    f.person(nme, sx)
f.child("#g1", "Ravi"); f.child("#g1", "Geeta"); f.child("Ravi", "Sita"); f.child("Geeta", "Mohan")
assert rel2(f, "Mohan", "Sita") == "cousin"
A("family-tree-puzzles", "br-p9", "**Sita is the daughter of Ravi. Ravi's sister is Geeta. Geeta's son is Mohan.** How is **Mohan related to Sita**?",
  "Cousin", ["Brother", "Nephew", "Uncle"],
  "Ravi and Geeta are siblings; Sita is Ravi's child and Mohan is Geeta's child. Children of siblings → **cousin**.",
  diff="medium", shortcut="Spot the married-in branches: each sibling's children are cousins to the other's.")

# ================= pointing-introduction =================
# p01
f = Fam()
for nme, sx in (("Rita", "F"), ("GF", "M"), ("FA", "M"), ("G", "F")):
    f.person(nme, sx)
f.child("GF", "FA"); f.child("FA", "Rita"); f.child("FA", "G")
assert rel2(f, "G", "Rita") == "sister"
A("pointing-introduction", "br-p10", "Pointing to a girl in a photograph, Rita said, **\"She is the daughter of my grandfather's only son.\"** How is the girl related to Rita?",
  "Sister", ["Cousin", "Niece", "Aunt"],
  "My grandfather's only son = Rita's father. His daughter = Rita's **sister**. ('Only son' pins the boy as Rita's father, so the girl cannot be a cousin.)",
  diff="easy", shortcut="Grandfather's only son = your own father — collapse that layer first.")
# p02
f = Fam()
for nme, sx in (("Mohan", "M"), ("FA", "M"), ("UN", "M"), ("AUNTY", "F")):
    f.person(nme, sx)
f.child("#g1", "FA"); f.child("#g1", "UN"); f.marry("UN", "AUNTY"); f.child("FA", "Mohan")
assert rel2(f, "AUNTY", "Mohan") == "aunt"
A("pointing-introduction", "br-p10", "Pointing to a woman, Mohan said, **\"She is the wife of my father's only brother.\"** How is the woman related to Mohan?",
  "Aunt", ["Mother", "Sister-in-law", "Cousin"],
  "Father's only brother = Mohan's uncle; the uncle's wife = Mohan's **aunt**.",
  diff="medium", shortcut="Father's brother = uncle; uncle's wife = aunt. Two blocks, one line.")
# p03
f = Fam()
for nme, sx in (("Neha", "F"), ("GM", "F"), ("BOY", "M")):
    f.person(nme, sx)
f.child("GM", "Neha"); f.child("Neha", "BOY")
assert rel2(f, "Neha", "BOY") == "mother" and f.kids["GM"] == {"Neha"}
A("pointing-introduction", "br-p11", "Pointing to a boy, Neha said, **\"His mother is the only daughter of my mother.\"** How is Neha related to the boy?",
  "Mother", ["Aunt", "Grandmother", "Sister"],
  "My mother's only daughter = Neha herself (her mother has exactly one daughter). So the boy's mother **is** Neha → Neha is his **mother**.",
  diff="medium", shortcut="'Only daughter of my mother' is the speaker, whenever the speaker is female.")
# p04
f = Fam()
for nme, sx in (("Suresh", "M"), ("FA", "M"), ("BOY", "M")):
    f.person(nme, sx)
f.child("FA", "Suresh"); f.child("Suresh", "BOY")
assert rel2(f, "BOY", "Suresh") == "son" and f.kids["FA"] == {"Suresh"}
A("pointing-introduction", "br-p11", "Pointing to a boy, Suresh said, **\"He is the son of my father's only son.\"** How is the boy related to Suresh?",
  "Son", ["Nephew", "Brother", "Cousin"],
  "Suresh is male, so his father's only son = Suresh himself. The boy is Suresh's **son**. (Nephew would need a second son of the father — 'only son' rules him out.)",
  diff="hard", shortcut="Self-reference first: father's only son (male speaker) = the speaker.")
# p05
A("pointing-introduction", "br-p12", "Pointing to a man, Meena said, **\"His wife is the daughter of my grandfather's only child.\"** How is the man related to Meena?",
  "Cannot be determined", ["Husband", "Brother-in-law", "Father-in-law"],
  "Grandfather's only child = Meena's mother. Her daughters include Meena herself and possibly a sister — the phrase never says the daughter is Meena alone. So the man is Meena's husband **or** her brother-in-law → **cannot be determined**.",
  diff="medium", shortcut="List every woman who could be 'the daughter'; two candidates → no single relation.")
# p06
A("pointing-introduction", "br-p11", "Pointing to a man, Deepak said, **\"He is the only son of my father.\"** How is the man related to Deepak?",
  "Deepak himself", ["Deepak's brother", "Deepak's uncle", "Deepak's son"],
  "Deepak is male, and his father has exactly one son — Deepak. So the man in the photo is **Deepak himself**. The question is a mirror, not a family puzzle.",
  diff="easy", shortcut="'Only son of my father' + male speaker = the speaker.")
# p07
f = Fam()
for nme, sx in (("Sita", "F"), ("GM", "F"), ("MOT", "F"), ("MAN", "M")):
    f.person(nme, sx)
f.child("GM", "MOT"); f.child("MOT", "Sita"); f.child("MOT", "MAN")
assert f.kids["GM"] == {"MOT"} and rel2(f, "MAN", "Sita") == "brother"
A("pointing-introduction", "br-p10", "Pointing to a man, Sita said, **\"His mother is the only child of my grandmother.\"** How is the man related to Sita?",
  "Brother", ["Cousin", "Uncle", "Nephew"],
  "Grandmother's only child = Sita's mother. The man's mother is that same woman → they share a mother → the man is Sita's **brother** (Sita herself is a daughter, so the man is not her).",
  diff="medium", shortcut="Only child of the grandmother = the mother; her other child is your sibling.")
# p08
A("pointing-introduction", "br-p12", "Pointing to a man, Pooja said, **\"He is the son of one of my grandfather's sons.\"** How is the man related to Pooja?",
  "Cannot be determined", ["Brother", "Cousin", "Nephew"],
  "Grandfather's sons include Pooja's father and her uncles. The man could be her **brother** (son of her father) or her **cousin** (son of an uncle) — both readings fit the words → **cannot be determined**.",
  diff="hard", shortcut="'One of my grandfather's sons' is deliberately unpinned; do not collapse it to 'father'.")
# p09
f = Fam()
for nme, sx in (("Priya", "F"), ("GF", "M"), ("FA", "M"), ("MAN", "M")):
    f.person(nme, sx)
f.child("GF", "FA"); f.child("FA", "Priya"); f.child("FA", "MAN")
assert rel2(f, "Priya", "MAN") == "sister"
A("pointing-introduction", "br-p13", "Pointing to a photograph of a man, Priya said, **\"He is the son of my grandfather's only son.\"** How is **Priya related to the man**?",
  "Sister", ["Cousin", "Niece", "Daughter"],
  "Grandfather's only son = Priya's father; the man is his son → Priya's brother. The question asks it backwards: Priya is the man's **sister**.",
  diff="easy", shortcut="Decode as usual, then flip: 'How is the speaker related to X?' wants the mirror word.")
# p10
f = Fam()
for nme, sx in (("Geeta", "F"), ("GM", "F"), ("LADY", "F")):
    f.person(nme, sx)
f.child("GM", "LADY"); f.child("LADY", "Geeta")
assert f.kids["GM"] == {"LADY"} and rel2(f, "Geeta", "LADY") == "daughter"
A("pointing-introduction", "br-p13", "Pointing to a lady, Geeta said, **\"She is the only daughter of my mother's mother.\"** How is **Geeta related to the lady**?",
  "Daughter", ["Niece", "Granddaughter", "Cousin"],
  "My mother's mother = Geeta's grandmother; her only daughter = Geeta's mother (the lady). Asked in reverse: Geeta is her **daughter**.",
  diff="medium", shortcut="Decode the chain to 'mother', then answer the question's own direction.")

# ================= coded-relations =================
# p01
f, pp = coded("A+B-C", {"+": ("brother", "M"), "-": ("mother", "F")})
assert rel2(f, pp["A"], pp["C"]) == "uncle"
A("coded-relations", "br-p14", "'**P + Q**' means **P is the brother of Q**; '**P − Q**' means **P is the mother of Q**. In '**A + B − C**', how is **A related to C**?",
  "Uncle", ["Brother", "Father", "Aunt"],
  "Decode: A is B's brother; B is C's mother. So A is the brother of C's mother → C's **uncle** (A's gender is fixed male by '+').",
  diff="easy", shortcut="Mother's brother = maternal uncle; the '+' already made A male.")
# p02
f, pp = coded("A×B÷C", {"×": ("wife", "F"), "÷": ("sister", "F")})
assert rel2(f, pp["A"], pp["C"]) == "sister-in-law"
A("coded-relations", "br-p14", "'**P × Q**' means **P is the wife of Q**; '**P ÷ Q**' means **P is the sister of Q**. In '**A × B ÷ C**', how is **A related to C**?",
  "Sister-in-law", ["Wife", "Sister", "Aunt"],
  "A is B's wife; B is C's sister. Wife of the sibling → A is C's **sister-in-law**.",
  diff="medium", shortcut="Sibling's spouse = brother/sister-in-law; one crossing only.")
# p03
f, pp = coded("A#B@C", {"#": ("daughter", "F"), "@": ("father", "M")})
assert f.sex.get(pp["C"]) is None and f.par[pp["A"]] == f.par[pp["C"]]
A("coded-relations", "br-p14", "'**P # Q**' means **P is the daughter of Q**; '**P @ Q**' means **P is the father of Q**. In '**A # B @ C**', how is **C related to A**?",
  "Brother or sister", ["Brother", "Sister", "Father"],
  "A is B's daughter; C is B's child too → A and C share the parent B. But no symbol fixes C's gender → C is A's **brother or sister** (sibling). Choosing 'brother' or 'sister' alone assumes a gender the string never gave.",
  diff="hard", shortcut="Check which letters got a gender from a symbol; a blank gender forces the neutral word.")
# p04
f, pp = coded("A+B-C×D", {"+": ("son", "M"), "-": ("wife", "F"), "×": ("brother", "M")})
assert rel2(f, pp["A"], pp["D"]) == "nephew"
A("coded-relations", "br-p15", "'**P + Q**' means **P is the son of Q**; '**P − Q**' means **P is the wife of Q**; '**P × Q**' means **P is the brother of Q**. In '**A + B − C × D**', how is **A related to D**?",
  "Nephew", ["Cousin", "Son", "Uncle"],
  "A is B's son; B is C's wife → C is A's father. C is D's brother → D is a sibling of A's parent. A is male ('son') → A is D's **nephew**.",
  diff="medium", shortcut="Decode three sentences, draw four boxes; then the path A–C–D is one line.")
# p05
f, pp = coded("A%B&C/D", {"%": ("mother", "F"), "&": ("husband", "M"), "/": ("sister", "F")})
assert f.sp[pp["B"]] == pp["C"] and f.sib(pp["C"], pp["D"]) and f.sex[pp["B"]] == "M"
A("coded-relations", "br-p15", "'**P % Q**' means **P is the mother of Q**; '**P & Q**' means **P is the husband of Q**; '**P / Q**' means **P is the sister of Q**. In '**A % B & C / D**', how is **B related to D**?",
  "Brother-in-law", ["Husband", "Cousin", "Father"],
  "A is B's mother (so B is male from '&'); B is C's husband; C is D's sister. B is the husband of D's sister → B is D's **brother-in-law**.",
  diff="hard", shortcut="Husband of my sibling = brother-in-law; the '&'-gender makes B male, so no 'sister-in-law' trap.")
# p06
f, pp = coded("A#B@C", {"#": ("father", "M"), "@": ("sister", "F")})
assert f.par[pp["C"]] == {pp["A"]} and f.sex.get(pp["C"]) is None
A("coded-relations", "br-p16", "'**X # Y**' means **X is the father of Y**; '**X @ Y**' means **X is the sister of Y**. In '**A # B @ C**', how is **C related to A**?",
  "Son or daughter", ["Son", "Daughter", "Grandson"],
  "A is B's father; B is C's sister → A is C's father too. Asked from C's side: C is A's child — but no symbol fixes C's gender → **son or daughter**. (Grandson invents a generation that does not exist.)",
  diff="medium", shortcut="Parent of one sibling is parent of all siblings; the gender gap decides the wording.")
# p07
f, pp = coded("C+B-A", {"+": ("brother", "M"), "-": ("daughter", "F")})
assert rel2(f, pp["C"], pp["A"]) == "son"
A("coded-relations", "br-p16", "'**P − Q**' means **P is the daughter of Q**; '**P + Q**' means **P is the brother of Q**. In '**C + B − A**', how is **C related to A**?",
  "Son", ["Brother", "Father", "Nephew"],
  "C is B's brother; B is A's daughter. Siblings share parents, so A is C's parent too — and C is male ('brother') → C is A's **son**. (Nephew would need C to be a sibling's child; C is a direct child here.)",
  diff="medium", shortcut="Siblings share parents — carry the parent arrow across the '+' before answering.")
# p08
f, pp = coded("M+L-K", {"+": ("brother", "M"), "-": ("mother", "F")})
assert f.sib(pp["M"], pp["L"]) and f.par[pp["K"]] == {pp["L"]} and f.sex[pp["M"]] == "M"
A("coded-relations", "br-p17", "'**P + Q**' means **P is the brother of Q**; '**P − Q**' means **P is the mother of Q**; '**P ÷ Q**' means **P is the father of Q**. Which expression means '**M is the maternal uncle of K**'?",
  "M + L − K", ["M ÷ L − K", "M − L ÷ K", "M + L + K"],
  "Maternal uncle = mother's brother. 'M + L − K': M is L's brother, L is K's mother ✓. 'M ÷ L − K' makes M a father; 'M − L ÷ K' makes M the mother of K's father (a grandmother); 'M + L + K' makes M K's brother.",
  diff="hard", shortcut="Write the target as two sentences ('M is L's brother; L is K's mother') and match symbols to them.")
# p09
f, pp = coded("P+Q+S", {"+": ("son", "M")})
assert f.par[pp["Q"]] == {pp["S"]} and f.par[pp["P"]] == {pp["Q"]} and f.sex[pp["P"]] == "M"
A("coded-relations", "br-p17", "'**P + Q**' means **P is the son of Q**; '**P @ Q**' means **P is the father of Q**. Which expression means '**P is the grandson of S**'?",
  "P + Q + S", ["P @ Q + S", "Q + P + S", "P + Q @ S"],
  "Need: P is a son, of someone who is a child of S. 'P + Q + S': P is Q's son and Q is S's son → P is S's **grandson** ✓. 'P @ Q + S' makes P S's father; 'Q + P + S' makes Q the grandson; 'P + Q @ S' makes Q P's father but P S's son (one generation short).",
  diff="medium", shortcut="Grandson = two 'son' links in a chain — two '+' symbols in a row.")
# p10
f, pp = coded("A-B+C-D", {"-": ("wife", "F"), "+": ("brother", "M")})
assert f.sp[pp["A"]] == pp["B"] and f.sib(pp["B"], pp["C"]) and f.sp[pp["D"]] == pp["C"]
A("coded-relations", "br-p17", "'**P − Q**' means **P is the wife of Q**; '**P + Q**' means **P is the brother of Q**. In '**A − B + C − D**', how is **D related to A**?",
  "Brother-in-law", ["Husband", "Uncle", "Father-in-law"],
  "A is B's wife; B is C's brother; C is D's wife. So D is the husband of A's husband's sister → A's **brother-in-law** (co-brother).",
  diff="hard", shortcut="Two marriage crossings from A: husband's sister's husband = brother-in-law.")

upsert(d["practice"], NQ)

d["pyqPatterns"] = [
    PYQ("Mixed-statement family tree", "very common",
        "3-6 shuffled sentences describe one family; the question asks 'How is X related to Y?' or 'How many males are there?'.",
        "Ignore the given order. Find the person nobody calls a child, place them at the top, hang children below, join marriages on the same row, and read the shortest path. Tick genders while drawing for counting questions.",
        "family-tree-puzzles",
        "**Anil is the brother of Sunil. Sunil is the father of Mohan. Ritu is the daughter of Kavita. Mohan is the brother of Ritu.** How is Kavita related to Anil?",
        "Mohan and Ritu share parents; Ritu's mother is Kavita → Kavita is Sunil's wife → Anil's **sister-in-law**."),
    PYQ("Pointing to a photograph", "very common",
        "'Pointing to X, Y said, \"He/She is the ___ of my ___'s ___\"' — the tree hides in one spoken phrase.",
        "Replace 'my' with the speaker's name and decode inside-out, one layer per line. Test the self-reference first ('my mother's only child' = the speaker), then read the final relation in the direction the question asks.",
        "pointing-introduction",
        "Pointing to a man, Sunita said, **\"He is the only son of my mother's mother's only child.\"** How is the man related to Sunita?",
        "Mother's mother's only child = Sunita's mother; her only son = Sunita's brother → **Brother**."),
    PYQ("Symbol-coded relations", "common",
        "'P + Q means P is the father of Q...' plus a coded string like A + B × C.",
        "Decode one symbol at a time into plain sentences, draw the mini-tree, and mark the gender each symbol fixes (a symbol fixes only its first person). Answer in the question's direction; a blank gender forces a neutral word or 'cannot be determined'.",
        "coded-relations",
        "'**P + Q**' means P is the son of Q; '**P ÷ Q**' means P is the wife of Q. In '**A + B ÷ C**', how is A related to C?",
        "A is B's son and B is C's wife → A is C's **son** (the couple's child)."),
    PYQ("Chain relations", "common",
        "Two or three short links in a row: 'A's son is B, B's daughter is C...'.",
        "Draw one arrow per sentence, count arrows between the asked pair (1 = parent/child, 2 = grand-, 3 = great-grand-), then fix the exact word with the gender.",
        "family-tree-puzzles",
        "**Mohan is Rekha's father. Ramesh is Mohan's father.** How is Ramesh related to Rekha?",
        "Two arrows up from Rekha, male → **Grandfather**."),
    PYQ("Counting males/females", "common",
        "A full family description plus 'How many male/female members are there?'.",
        "Draw the whole tree, write +/− beside every name only where a word fixes the gender (including married-in spouses), then count ticks. Never count a name whose gender stayed blank.",
        "family-tree-puzzles",
        "**Dinesh and Gauri have a son Ashok. Ashok married Nutan; children Pankaj and Seema. Pankaj married Usha; son Tinku. How many males?**",
        "Males: Dinesh, Ashok, Pankaj, Tinku = **4**."),
    PYQ("In-law relations", "common",
        "Wives, husbands, in-laws: 'wife of my son', 'father of my spouse', 'brother of my wife'.",
        "Apply the in-law map one crossing at a time: spouse's parent = father/mother-in-law; sibling's spouse or spouse's sibling = brother/sister-in-law; child's spouse = son/daughter-in-law.",
        "family-tree-puzzles",
        "**Rita's son is Amit. Amit's wife is Sneha.** How is Sneha related to Rita?",
        "Sneha married Rita's child → one crossing from 'daughter' → **daughter-in-law**."),
    PYQ("Direction and gender traps", "very common",
        "Short statements with 'How is A related to B?' where reversing the direction or guessing a gender gives a plausible wrong option.",
        "Start from the person named after 'related to'. Mark genders only where words state them; if the needed gender is blank, pick the neutral option or 'cannot be determined'. Never leave a chain in your head — one arrow per sentence on paper.",
        "blood-relations-idea",
        "**A and B are siblings. C is the mother of A and B.** How is B related to C?",
        "B is C's child, gender never stated → **cannot be determined**."),
    PYQ("Build the coded expression", "occasional",
        "'Which expression means M is the maternal uncle of K?' — the options are strings, not words.",
        "Write the target relation as two plain sentences ('M is the brother of K's mother'), then match symbols sentence by sentence. Reject options that change a gender or shift a generation.",
        "coded-relations",
        "'**P + Q**' = P is the brother of Q; '**P − Q**' = P is the mother of Q. Which means 'M is the maternal uncle of K'?",
        "Need M = brother of K's mother → **M + L − K** (M is L's brother, L is K's mother)."),
]

finish("blood-relations", d)
