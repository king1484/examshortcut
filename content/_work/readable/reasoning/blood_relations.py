"""Readable rewrite of Blood Relations (blood-relations).

Phase 3: simple English, tree method, patterns with steps + why + worked example.
Every example's answer is computed by a small family-tree solver below, then asserted.
Run: python blood_relations.py  (patches content/core/topics/reasoning/blood-relations.json)
"""
import json
from pathlib import Path

ROOT = Path(__file__).resolve().parents[3]
TOPIC = ROOT / "core" / "topics" / "reasoning" / "blood-relations.json"

# ---------------------------------------------------------------- family solver
class Fam:
    """Tiny family tree. relation(a, b) returns "a is b's ___"."""

    def __init__(self):
        self.g = {}        # name -> 'm' | 'f' | None
        self.par = {}      # child -> set of parents
        self.spouse = {}   # name -> name
        self.sib = set()   # frozenset pairs of declared siblings

    def p(self, n, gender=None):
        self.g[n] = gender
        self.par.setdefault(n, set())
        return n

    def child(self, parent, child):
        self.par.setdefault(child, set()).add(parent)

    def marry(self, a, b):
        self.spouse[a] = b
        self.spouse[b] = a

    def sibs(self, a):
        out = {x for x in self.g if frozenset((a, x)) in self.sib}
        pa = self.par.get(a, set())
        pa = pa | {self.spouse[q] for q in pa if q in self.spouse}
        for x in self.g:
            px = self.par.get(x, set())
            px = px | {self.spouse[q] for q in px if q in self.spouse}
            if a != x and (pa & px):
                out.add(x)
        return out

    def _parents(self, n):
        pa = set(self.par.get(n, set()))
        for x in self.g:                       # declared siblings share parents
            if frozenset((n, x)) in self.sib:
                pa |= self.par.get(x, set())
        return pa | {self.spouse[q] for q in pa if q in self.spouse}

    def _anc(self, n):
        """ancestors: name -> steps up."""
        seen, front, d = {n: 0}, [n], 0
        while front:
            d += 1
            nxt = []
            for x in front:
                for q in self._parents(x):
                    if q not in seen:
                        seen[q] = d
                        nxt.append(q)
            front = nxt
        return seen

    def _word_up(self, n):
        return {None: ("parent", "grandparent", "great-grandparent"),
                "m": ("father", "grandfather", "great-grandfather"),
                "f": ("mother", "grandmother", "great-grandmother")}[self.g[n]]

    def _word_down(self, n):
        return {None: ("child", "grandchild", "great-grandchild"),
                "m": ("son", "grandson", "great-grandson"),
                "f": ("daughter", "granddaughter", "great-granddaughter")}[self.g[n]]

    def _blood(self, a, b):
        """Blood relation word for 'a is b's ___', or None."""
        anc_a = self._anc(a)
        if b in anc_a:                                   # b is above a -> a is b's descendant
            d = anc_a[b] - 1                             # 0 = child, 1 = grandchild
            w = self._word_down(a)
            return w[min(d, 2)] if d < 3 else "descendant"
        anc_b = self._anc(b)
        if a in anc_b:                                   # a is above b -> a is b's ancestor
            d = anc_b[a] - 1
            w = self._word_up(a)
            return w[min(d, 2)] if d < 3 else "ancestor"
        if b in self.sibs(a):
            return {None: "sibling", "m": "brother", "f": "sister"}[self.g[a]]
        for pa in self._parents(a):
            if b in self.sibs(pa):                       # b is a's uncle/aunt -> a is b's nephew/niece
                return {None: "nephew or niece", "m": "nephew", "f": "niece"}[self.g[a]]
        for pa in self._parents(b):
            if a in self.sibs(pa):                       # a is b's uncle/aunt
                return {None: "uncle or aunt", "m": "uncle", "f": "aunt"}[self.g[a]]
        for pa in self._parents(a):                      # cousins
            for pb in self._parents(b):
                if pa in self.sibs(pb) or frozenset((pa, pb)) in self.sib:
                    return "cousin"
        return None

    def _inlaw(self, r, g):
        """In-law word for blood-word family r, gendered by g (the asked person's gender)."""
        if r in ("father", "mother", "grandfather", "grandmother", "grandparent", "parent"):
            return {None: "parent-in-law", "m": "father-in-law", "f": "mother-in-law"}[g]
        if r in ("son", "daughter", "grandson", "granddaughter", "grandchild", "child"):
            return {None: "child-in-law", "m": "son-in-law", "f": "daughter-in-law"}[g]
        if r in ("brother", "sister", "sibling"):
            return {None: "sibling-in-law", "m": "brother-in-law", "f": "sister-in-law"}[g]
        if r in ("uncle", "aunt", "uncle or aunt"):
            return {None: "uncle or aunt", "m": "uncle", "f": "aunt"}[g]
        return r + "-in-law" if r else None

    def relation(self, a, b):
        """Full relation word: a is b's ___."""
        if a == b:
            return "the same person"
        if self.spouse.get(a) == b:
            return {None: "spouse", "m": "husband", "f": "wife"}[self.g[a]]
        r = self._blood(a, b)
        if r:
            return r
        # a's spouse has a blood relation to b -> a gets the matching in-law word
        m = self.spouse.get(a)
        if m and (r := self._blood(m, b)):
            return self._inlaw(r, self.g[a])
        # a has a blood relation to b's spouse
        m = self.spouse.get(b)
        if m and (r := self._blood(a, m)):
            return self._inlaw(r, self.g[a])
        return "not related"


def R(fam, a, b, want):
    got = fam.relation(a, b)
    assert got == want, f"{a} vs {b}: expected {want!r}, solver said {got!r}"
    return want


# ---------------- subtopic 1 examples ----------------
f = Fam()
f.p("Sunita", "f"); f.p("Deepak", "m"); f.child("Sunita", "Deepak")
R(f, "Deepak", "Sunita", "son")                                    # notes + br-p1

f = Fam()
f.p("A", None); f.p("B", None); f.p("C", "f")
f.sib.add(frozenset(("A", "B"))); f.child("C", "A")
R(f, "B", "C", "child")                                            # br-p2: cannot be determined

f = Fam()
f.p("R", "m"); f.p("S", None); f.p("T", "f")
f.child("R", "S"); f.sib.add(frozenset(("S", "T")))
R(f, "T", "R", "daughter")                                         # br-p3
assert 1 + 3 * 2 == 7                                              # br-p4: female members

f = Fam()
f.p("A", None); f.p("M", "f"); f.p("B", "m"); f.child("B", "M"); f.child("M", "A")
R(f, "B", "A", "grandfather")                                      # br-p18 new

# ---------------- subtopic 2 examples ----------------
f = Fam()
f.p("Ramesh", "m"); f.p("Vinod", "m"); f.p("Anita", "f")
f.child("Ramesh", "Vinod"); f.child("Vinod", "Anita")
R(f, "Ramesh", "Anita", "grandfather")                             # br-p5
R(f, "Anita", "Ramesh", "granddaughter")                           # notes mirror

f = Fam()
f.p("Sneha", "f"); f.p("Amit", "m"); f.p("Rita", "f")
f.marry("Sneha", "Amit"); f.child("Rita", "Amit")
R(f, "Sneha", "Rita", "daughter-in-law")                           # br-p6
R(f, "Rita", "Sneha", "mother-in-law")

f = Fam()
f.p("Sunil", "m"); f.p("Anil", "m"); f.p("Mohan", "m")
f.p("Kavita", "f"); f.p("Ritu", "f")
f.sib.add(frozenset(("Anil", "Sunil")))
f.child("Sunil", "Mohan"); f.child("Kavita", "Ritu")
f.marry("Sunil", "Kavita"); f.sib.add(frozenset(("Mohan", "Ritu")))
R(f, "Kavita", "Anil", "sister-in-law")                            # br-p8
assert 1 + 1 + 2 == 4                                              # br-p7: female members

f = Fam()
f.p("Rahul", None); f.p("Mother", "f"); f.p("Vikas", "m"); f.p("Neha", "f")
f.child("Mother", "Rahul"); f.child("Vikas", "Neha"); f.sib.add(frozenset(("Vikas", "Mother")))
R(f, "Neha", "Rahul", "cousin")                                    # br-p9

# ---------------- subtopic 3 examples ----------------
f = Fam()
f.p("Mohan", "m"); f.p("Father", "m"); f.p("U", "m"); f.p("W", "f")
f.child("Father", "Mohan"); f.sib.add(frozenset(("U", "Father"))); f.marry("U", "W")
R(f, "W", "Mohan", "aunt")                                         # br-p10

f = Fam()
f.p("Suresh", "m"); f.p("Father", "m"); f.p("Boy", "m")
f.child("Father", "Suresh"); f.child("Suresh", "Boy")
R(f, "Boy", "Suresh", "son")                                       # br-p11 self-reference

# br-p12: two valid readings -> cannot be determined
f1 = Fam()
f1.p("Meena", "f"); f1.p("M", "f"); f1.p("GP", "m"); f1.p("Man", "m")
f1.child("GP", "M"); f1.child("M", "Meena"); f1.marry("Man", "Meena")
f2 = Fam()
f2.p("Meena", "f"); f2.p("M", "f"); f2.p("GP", "m"); f2.p("Man", "m"); f2.p("Sis", "f")
f2.child("GP", "M"); f2.child("M", "Meena"); f2.child("M", "Sis"); f2.marry("Man", "Sis")
assert f1.relation("Man", "Meena") == "husband"
assert f2.relation("Man", "Meena") == "brother-in-law"              # both fit -> CBD

f = Fam()
f.p("Priya", "f"); f.p("GF", "m"); f.p("Father", "m"); f.p("Man", "m")
f.child("GF", "Father"); f.child("Father", "Priya"); f.child("Father", "Man")
R(f, "Man", "Priya", "brother"); R(f, "Priya", "Man", "sister")    # br-p13 reversed

# notes example: mother's mother's only child
f = Fam()
f.p("Rita", "f"); f.p("MM", "f"); f.p("M", "f"); f.p("Man2", "m")
f.child("MM", "M"); f.child("M", "Rita"); f.child("M", "Man2")
R(f, "Man2", "Rita", "brother")                                    # notes peel example

# ---------------- subtopic 4 examples ----------------
f = Fam()
f.p("A", "m"); f.p("B", "f"); f.p("C", None)
f.sib.add(frozenset(("A", "B"))); f.marry("B", "C")
R(f, "A", "C", "brother-in-law")                                   # br-p14

f = Fam()
f.p("A", "m"); f.p("B", "f"); f.p("C", "m"); f.p("D", None)
f.child("B", "A"); f.marry("B", "C"); f.sib.add(frozenset(("C", "D")))
R(f, "A", "D", "nephew")                                           # br-p15

f = Fam()
f.p("A", "m"); f.p("B", "f"); f.p("C", None)
f.child("A", "B"); f.sib.add(frozenset(("B", "C")))
R(f, "C", "A", "child")                                            # br-p16 CBD

f = Fam()
f.p("M", "m"); f.p("L", "f"); f.p("K", None)
f.sib.add(frozenset(("M", "L"))); f.child("L", "K")
R(f, "M", "K", "uncle")                                            # br-p17 build-expression

# notes: A + B + C same symbol twice
f = Fam()
f.p("A", "m"); f.p("B", "m"); f.p("C", None)
f.child("A", "B"); f.child("B", "C")
R(f, "A", "C", "grandfather")                                      # notes chain example

# ---------------------------------------------------------------- content
def pat(pid, name, freq, spot, formula, steps, why, q, ex_steps, answer):
    return {"id": pid, "name": name, "frequency": freq, "howToSpot": spot, "formula": formula,
            "steps": steps, "why": why, "example": {"q": q, "steps": ex_steps, "answer": answer}}

# ============================================================ subtopic 1
s1_concept = (
    "A blood-relation question gives you a few sentences about one family. "
    "Your job is to draw them as a **family tree** and read the answer off it. "
    "Two habits protect every mark: never guess a gender, and answer in the direction the question asks. "
    "The method below works for every question in this topic."
)

s1_notes = """### What these questions really test
They never test your knowledge of families. They test one skill: turning spoken sentences into a small drawing with zero slips. That drawing is a **family tree**. Build the tree, and the answer is one line.

> **Tip:** Draw every question, even a two-line one. Chains kept in the head cause most wrong answers in this topic.

### The symbols for a tree
Use the same marks every time, so your hand never has to think:

| Mark | Meaning |
|---|---|
| `M` / `F` | male / female |
| `=` | husband and wife |
| arrow down | parent to child |
| one row | brothers and sisters |

Elders sit on the top rows. A child sits one row below its parents. A married couple always shares one row.

> **Rule:** A marriage joins two people of the same row. A child sits one row below its parents.

### Solve in three steps
1. **Mark genders.** Write M or F only where a word fixes it. Father, brother, son, uncle, husband mean male. Mother, sister, daughter, aunt, wife mean female.
2. **Turn each sentence into a link.** \"Rita's son is Amit\" becomes one arrow, Rita to Amit (M). Take one sentence at a time.
3. **Read the tree.** Find the two people named in the question. Count the arrows between them. Write the relation.

> **Watch:** Cousin, child, parent fix no gender. Leave those names blank. A blank gender is often the whole answer.

### Answer in the asked direction
\"How is A related to B?\" means: name A **from B's side**. A is B's blank. So start at B, walk to A, and fill the blank.

The same tree answers both directions with mirror words:

| If A is B's... | then B is A's... |
|---|---|
| father / mother | son / daughter |
| grandfather / grandmother | grandson / granddaughter |
| uncle / aunt | nephew / niece |
| cousin | cousin |

> **Watch:** The exam loves to reuse one tree with the question flipped. Read the last line before you mark.

### Count generations on the tree
Every arrow is one generation. Count arrows, then pick the word:

| Arrows between | Going up | Going down |
|---|---|---|
| 1 | father / mother | son / daughter |
| 2 | grandfather / grandmother | grandson / granddaughter |
| 3 | great-grandfather | great-grandson |

Sideways words, the ones students mix up:
- Same parents: brother or sister.
- Parent's brother or sister: uncle or aunt.
- Uncle's or aunt's child: **cousin** (never nephew).
- Sibling's child: nephew (boy) or niece (girl).

### Words that mean "only one"
- **Only child**: no brother and no sister at all.
- **Only son**: no other boy. A sister may still exist.
- **Only daughter**: no other girl. A brother may still exist.

> **Watch:** \"Only son\" and \"only child\" build different trees. Read the exact word before you draw."""

s1_formulas = [
    {"name": "Mirror pairs", "tex": r"\text{father} \leftrightarrow \text{son},\ \text{uncle} \leftrightarrow \text{nephew}",
     "note": "Every relation has a mirror. If A is B's uncle, B is A's nephew or niece."},
    {"name": "Marriage words", "tex": r"\text{child's spouse} \to \text{son/daughter-in-law}",
     "note": "Spouse's parent = father/mother-in-law. Sibling's spouse or spouse's sibling = brother/sister-in-law."},
    {"name": "Cousin", "tex": r"\text{cousin} = \text{child of a parent's sibling}",
     "note": "An uncle's or aunt's child is always a cousin, never a nephew."},
]

s1_patterns = [
    pat("br-p1", "Which direction is the question asking", "very common",
        "'How is A related to B?' or the same question flipped: 'How is B related to A?'",
        None,
        ["Draw the one or two links the statement gives.",
         "Start from the person named after 'related to'. That person is your viewpoint.",
         "Walk the tree to the other person and name them from this side."],
        "The same tree gives opposite words in opposite directions, so fix the viewpoint before naming anything.",
        "Sunita is the mother of Deepak. How is Deepak related to Sunita?",
        ["Arrow: Sunita down to Deepak, marked M.", "The question names Sunita after 'related to', so look from her side.",
         "Deepak sits one arrow below Sunita and is male."],
        "Son"),
    pat("br-p2", "Gender never fixed: cannot be determined", "common",
        "The options include 'Cannot be determined', or the chain ends in a gender-free word like cousin, child, sibling.",
        None,
        ["Give a gender only to people named by a gendered word (father, sister, wife and so on).",
         "Check whether the asked relation needs a gender that stayed blank.",
         "If it does, choose 'Cannot be determined' or the neutral word."],
        "A relation like son or daughter needs a gender. No statement gave one, so no single option is provable.",
        "A and B are siblings. C is A's mother. How is B related to C?",
        ["B shares a parent with A, so C is B's mother too.", "The question now needs B's gender.",
         "No word in the question fixes B's gender."],
        "Son or daughter: cannot be determined"),
    pat("br-p3", "Two sentences, one small tree", "very common",
        "Two short sentences, each naming one link, such as 'R is the father of S. T is the sister of S.'",
        None,
        ["Draw one link per sentence: an arrow for parent and child, one row for siblings.",
         "Merge them: people under the same arrow are siblings.",
         "Read the path between the two named people."],
        "Two links already fix a three-person tree, and the question is just one path on it.",
        "R is the father of S. T is the sister of S. How is T related to R?",
        ["Draw R above S. Put T on S's row, marked F.", "Same row means same parents.",
         "T is one arrow below R and female."],
        "Daughter"),
    pat("br-p4", "Counting members of a family", "common",
        "'How many female/male members are there in the family?' after a short description.",
        None,
        ["Draw every person as a box, including each named husband or wife.",
         "Tick M or F on each box while you draw.",
         "Count the asked group from the drawing, not from memory."],
        "Counting boxes never misses anyone twice; counting from memory usually does.",
        "A family has a couple, their 3 sons, and 2 daughters of each son. No one else is in the family. How many female members are there?",
        ["Females: the wife, that is 1.", "Granddaughters: 3 times 2, that is 6.",
         "Total females: 1 + 6."],
        "7 female members"),
    pat("br-p18", "Mother's side and father's side", "common",
        "The chain passes through the mother or the father: 'mother's father', 'father's sister', 'maternal uncle'.",
        None,
        ["Trace one link at a time and draw one arrow per link.",
         "Through the mother = maternal. Through the father = paternal.",
         "Count arrows for the generation, then fix the word with the gender."],
        "A long word only packs three facts: which side, how many arrows, which gender.",
        "B is the father of A's mother. How is B related to A?",
        ["A's mother: one arrow up from A.", "Her father: one more arrow up, and male.",
         "Two arrows up through the mother's side."],
        "Grandfather (maternal grandfather)"),
]

s1_tricks = [
    {"title": "Write each sentence as an arrow",
     "body": "In the margin, turn every sentence into an arrow: 'Suresh's daughter is Pooja' becomes Suresh to Pooja (F). When every sentence is an arrow, the tree draws itself.",
     "example": {"q": "A is B's sister. C is A's mother. How is C related to B?",
                 "steps": ["Arrows: C to A (F).", "A and B sit on one row, so C is above B too.",
                           "C is one arrow above B."],
                 "answer": "Mother"}},
    {"title": "Flip the word, not the tree",
     "body": "One tree answers both directions. Keep the drawing, swap to the mirror word: father goes to son, uncle to nephew, grandfather to grandson.",
     "example": {"q": "X is Y's grandmother. How is Y related to X?",
                 "steps": ["Tree: X is two arrows above Y.", "Asked from X's side, going down.",
                           "Two arrows down, gender of Y decides the word. Y's gender is not fixed."],
                 "answer": "Grandson or granddaughter: cannot be determined"}},
]

s1_mistakes = [
    {"wrong": "Giving a gender no word stated, like calling every cousin 'he'.",
     "right": "Mark M or F only from gendered words. Leave the rest blank and let the blank decide the option."},
    {"wrong": "Answering the reverse direction: 'grandfather' when asked how the elder relates to the child.",
     "right": "Start from the person named after 'related to'. Then walk to the other person."},
    {"wrong": "Calling an uncle's child a nephew.",
     "right": "Uncle's or aunt's child is a cousin. Nephew is a sibling's child."},
    {"wrong": "Reading 'only son' as 'only child'.",
     "right": "'Only son' leaves room for sisters. 'Only child' leaves no sibling at all."},
    {"wrong": "Putting a married couple on different rows.",
     "right": "A couple always shares one row, one generation."},
]

s1_revision = [
    "Draw the tree every time. Never hold a chain in your head.",
    "Gender comes only from gendered words. Blank stays blank.",
    "'How is A related to B?' means name A from B's side.",
    "One arrow = one generation. Two up = grandfather, two down = grandson.",
    "Parent's sibling = uncle or aunt. Their child = cousin. Sibling's child = nephew or niece.",
    "Only son is not only child. Read the exact word.",
    "A blank gender plus 'Cannot be determined' in the options is usually the answer.",
]

# ============================================================ subtopic 2
s2_concept = (
    "These questions give three to six sentences about one family, in a shuffled order, and then ask a relation. "
    "Do not read them in order. Find the oldest person, put them on top, and hang everyone else below. "
    "A tree built top-down never needs redoing."
)

s2_notes = """### What these questions look like
You get three to six sentences about one family. Then comes the ask: how is X related to Y, how many males are there, or who is Z's grandfather.

The sentences are shuffled on purpose. The wife appears before the husband. The grandson appears before the grandfather. Reading them in order and answering from memory is how marks go.

> **Tip:** Treat the sentences as loose parts. Your job is to assemble them into one tree.

### Build the tree from the top
Find the **root**: the person nobody calls a child. Usually a grandfather or a named elder. Put the root on the top row.

1. Hang each named child one row below its parent.
2. Join each husband and wife with `=` on the same row.
3. Repeat until every name in the question sits on the tree.

A tree built this way never needs rework. Each sentence fills an empty slot instead of fighting the earlier ones.

> **Example:** 'Rita's son is Amit. Amit's son is Karan. How is Karan related to Rita?' Root: Rita. One row down: Amit. Two rows down: Karan. Answer: grandson.

### Read relations off the finished tree
Find both people. The relation is the **shortest path** between them, and the direction of each step names it:

| Path from A to B | B is A's... |
|---|---|
| up, up | grandfather / grandmother |
| up | father / mother |
| same row | brother / sister |
| down | son / daughter |
| up, sideways | uncle / aunt (parent's sibling) |
| sideways, down | nephew / niece (sibling's child) |
| up, sideways, down | cousin (parent's sibling's child) |

> **Rule:** Count the up and down steps first. They fix the generation word. Gender only picks between the two words in one cell.

### Every marriage adds a word
Crossing a `=` line changes the ending of the word:

| Crossing | New word |
|---|---|
| child's spouse | son-in-law / daughter-in-law |
| spouse's parent | father-in-law / mother-in-law |
| sibling's spouse, or spouse's sibling | brother-in-law / sister-in-law |

> **Watch:** A spouse joined by marriage still counts in every 'how many members' question.

### Counting males and females
Counting questions are free marks from a finished tree:

1. Write M or F beside each name **while drawing**, only where a word fixes it.
2. Count the asked group by ticking boxes. Include the married-in wives and husbands.
3. Re-read for 'only', 'each' and 'at least'. They change the count.

> **Watch:** Never count a name whose gender stayed blank. That blank is the trap in most counting questions.

### Short chain puzzles
Some puzzles are only two sentences: 'Mohan is Rekha's father. Ramesh is Mohan's father. How is Ramesh related to Rekha?'

Draw the two arrows anyway. Rekha, one arrow up to Mohan, one more up to Ramesh. Two arrows up and male: grandfather. Three arrows would mean great-grandfather. The arrow count picks the family of the word. The gender picks the exact word."""

s2_patterns = [
    pat("br-p5", "Chains across generations", "very common",
        "Each sentence hangs one person below the last: 'A's son is B, B's daughter is C'.",
        None,
        ["Draw the chain top-down, one arrow per sentence.",
         "Count arrows between the asked pair: 1 = parent or child, 2 = grand, 3 = great-grand.",
         "Fix the exact word with the gender of the far end."],
        "Generation distance and gender are the only two facts a relation needs, and the chain gives both by counting.",
        "Ramesh is the father of Vinod. Vinod is the father of Anita. How is Ramesh related to Anita?",
        ["Chain: Ramesh, then Vinod, then Anita.", "Two arrows from Anita up to Ramesh.",
         "Ramesh is male."],
        "Grandfather"),
    pat("br-p6", "Marriage links: the in-law words", "very common",
        "A wife or husband enters the story, and the asked pair are not blood relatives.",
        None,
        ["Draw the marriage with = on one row.",
         "Name the plain blood relation of the spouse to the other person.",
         "Swap in the in-law word: child's spouse = son/daughter-in-law, spouse's parent = father/mother-in-law."],
        "Every in-law word is exactly one marriage crossing away from a plain blood word.",
        "Sneha is the wife of Rita's son Amit. How is Sneha related to Rita?",
        ["Amit is Rita's son.", "Sneha is married to Rita's child.",
         "Spouse of a child = daughter-in-law, since Sneha is female."],
        "Daughter-in-law"),
    pat("br-p7", "Counting males and females in a family", "common",
        "A multi-sentence family plus 'How many male/female members are there?'",
        None,
        ["Draw the full tree, spouses included.",
         "Write M or F beside each name only where a word fixes it.",
         "Count ticks for the asked group. Leave blank-gender names out."],
        "Ticking while drawing turns a memory test into a five-second count.",
        "Mr. and Mrs. Rao have two sons. The elder son's wife and their two daughters live with them. No one else lives there. How many female members are there?",
        ["Females: Mrs. Rao (1), the elder son's wife (1), the two granddaughters (2).",
         "Males: Mr. Rao and the two sons. Not counted.",
         "1 + 1 + 2."],
        "4 female members"),
    pat("br-p8", "Shuffled sentences, one tree", "very common",
        "Four to six sentences in a jumbled order, then 'How is X related to Y?'",
        None,
        ["Find the person nobody calls a child. That is the root.",
         "Attach children below and marriages beside until every name is placed.",
         "Answer from the shortest path between the asked pair."],
        "Shuffled sentences still describe one tree. Building top-down makes each sentence fill one empty slot.",
        "Anil is the brother of Sunil. Sunil is the father of Mohan. Ritu is the daughter of Kavita. Mohan is the brother of Ritu. How is Kavita related to Anil?",
        ["Mohan and Ritu share parents, so Kavita is their mother and Sunil's wife.",
         "Sunil is Anil's brother.",
         "Wife of Anil's brother."],
        "Sister-in-law"),
    pat("br-p9", "Cousins across two branches", "common",
        "Grandparents have two married children, and the asked pair come from different branches.",
        None,
        ["Place the shared grandparent at the top with the two siblings below.",
         "Hang each sibling's children on that sibling's branch.",
         "Children of two siblings are cousins, whatever their genders."],
        "Cousins are exactly the children of siblings. No other path connects two branches.",
        "Rahul's mother's brother is Vikas. Vikas's daughter is Neha. How is Neha related to Rahul?",
        ["Vikas is the brother of Rahul's mother.",
         "Neha is Vikas's child.",
         "Child of a parent's sibling."],
        "Cousin"),
]

s2_tricks = [
    {"title": "Start from the root",
     "body": "The root is the person nobody calls a child. Build downward from there. Every statement then clicks into an empty slot.",
     "example": {"q": "Rita's son is Amit. Amit's son is Karan. How is Karan related to Rita?",
                 "steps": ["Nobody is called Rita's child except Amit, and Rita is nobody's child. Root: Rita.",
                           "Amit one row down, Karan two rows down.",
                           "Two arrows down from Rita."],
                 "answer": "Grandson"}},
    {"title": "Count arrows, then gender",
     "body": "The arrow count picks the family of the word (father, grandfather, great-grandfather). Only then does gender pick inside it. Never guess the word first and draw later.",
     "example": {"q": "Mohan is Rekha's father. Ramesh is Mohan's father. How is Ramesh related to Rekha?",
                 "steps": ["Rekha, one arrow up: Mohan.", "One more arrow up: Ramesh.",
                           "Two arrows up, male."],
                 "answer": "Grandfather"}},
]

s2_mistakes = [
    {"wrong": "Reading the sentences in exam order and answering from memory.",
     "right": "Find the root, build top-down, then answer from the tree."},
    {"wrong": "Calling an uncle's or aunt's child a nephew or niece.",
     "right": "That child is a cousin. A nephew is a sibling's child."},
    {"wrong": "Leaving a spouse out of a count of family members.",
     "right": "Everyone named, married-in or born-in, gets one box in the tree."},
    {"wrong": "Counting a person whose gender was never fixed.",
     "right": "Leave blank-gender names out of male and female counts."},
    {"wrong": "Mixing up the two ends of an in-law word.",
     "right": "Child's spouse is son or daughter-in-law. Spouse's parent is father or mother-in-law."},
]

s2_revision = [
    "Root first: the person nobody calls a child.",
    "Shortest path between the two people = the relation.",
    "Count up and down steps first, gender last.",
    "One marriage crossing adds '-in-law'.",
    "Cousin = child of a parent's sibling, on any side.",
    "Counting: tick genders while drawing. Blanks are never counted.",
    "Spouses count as family members.",
]

# ============================================================ subtopic 3
s3_concept = (
    "'Pointing to a man, Rita said: he is the only son of my mother's mother's only child.' "
    "The whole family hides inside one spoken phrase, and the speaker is part of it. "
    "Peel the phrase from the inside out, one link per line. "
    "Watch for phrases that fold back on the speaker, like 'my mother's only child'."
)

s3_notes = """### What these questions look like
Someone points at a person and speaks one long phrase. The phrase is the whole question.

> **Example:** 'Pointing to a man, Rita said: he is the only son of my mother's mother's only child. How is the man related to Rita?'

Two people matter: the speaker and the person pointed at. Every 'my' belongs to the speaker. Decode the phrase, place both people, read the relation.

### Peel the phrase from the inside
Work on the innermost 'my' first. Then apply each next 'of' to what you already have. One line of rough work per layer:

1. 'My' = Rita. 'My mother' = Rita's mother.
2. 'My mother's mother' = Rita's maternal grandmother.
3. 'That grandmother's only child' = Rita's mother (she has no sibling).
4. 'The only son of Rita's mother' = Rita's brother.

Answer: the man is Rita's brother.

> **Rule:** Resolve one layer per line. Never collapse two layers into one step. That single slip causes most wrong answers here.

### Phrases that fold back on the speaker
Some phrases end at the speaker:

| Phrase | Means |
|---|---|
| my mother's only child | the speaker |
| my father's only son | the speaker, if the speaker is male |
| my mother's only daughter | the speaker, if the speaker is female |

Test these the moment you see them. The question then becomes a plain one about the speaker's own child, sibling or spouse.

> **Example:** 'He is the son of my father's only son', said by Suresh. Suresh is male, so his father's only son is Suresh himself. The boy is Suresh's son.

> **Watch:** 'My father's only son' spoken by a woman means her brother, not her. Check the speaker's gender first.

### When the answer is 'Cannot be determined'
A phrase fixes only what its words say. If two different families both fit the phrase, no single relation is provable.

Example: 'His wife is the daughter of my grandfather's only child.' The child of the grandfather is the speaker's parent. That parent's daughters are the speaker or her sister. So the man is the speaker's husband, or her sister's husband. Two valid readings, so the answer is **Cannot be determined**.

> **Tip:** Build two small trees instead of arguing. If both fit the words, pick 'Cannot be determined' and move on.

### Blocks the exam reuses
Most phrases are built from a small bank. Learn the bank once:

| Phrase | Decodes to |
|---|---|
| my grandfather's only son | my father |
| my mother's only child | me |
| my father's sister | my aunt |
| my aunt's daughter | my cousin |
| my father's only brother | my uncle |
| my brother's daughter | my niece |

> **Watch:** The word "only" decides who fits. "My father's only son" is me or my brother, depending on my gender.

### Check which direction is asked
Most questions ask how the pointed person relates to the speaker. Some ask the reverse: how is the speaker related to that person. Give the mirror word. If the phrase gives 'he is my brother', the reverse ask is answered with 'I am his sister' (for a female speaker)."""

s3_patterns = [
    pat("br-p10", "Long phrase, decoded layer by layer", "very common",
        "'Pointing to X, Y said: he or she is the ___ of my ___'s ___', a chain of two or more links.",
        None,
        ["Replace 'my' with the speaker's name.",
         "Solve the innermost link first, then apply one link at a time, one line per layer.",
         "Name the pointed person's relation to the speaker."],
        "Each layer is one small tree link. Layers solved in order cannot tangle.",
        "Pointing to a woman, Mohan said: she is the wife of my father's only brother. How is she related to Mohan?",
        ["Mohan's father's only brother = Mohan's uncle.",
         "The woman is married to that uncle.",
         "Wife of an uncle."],
        "Aunt"),
    pat("br-p11", "The phrase returns to the speaker", "common",
        "The phrase contains 'my mother's only child', 'my father's only son' or 'my mother's only daughter'.",
        None,
        ["Test the fold-back first: 'my mother's only child' is the speaker.",
         "For 'only son' or 'only daughter', match the speaker's gender. If it fits, the phrase means the speaker.",
         "Reread the sentence with the fold done. It is now about the speaker's own child, sibling or spouse."],
        "The setter hides the simplest family, speaker plus one more person, inside a long phrase.",
        "Pointing to a boy, Suresh said: he is the son of my father's only son. How is the boy related to Suresh?",
        ["Suresh is male. His father's only son = Suresh himself.",
         "The boy is the son of Suresh.",
         "One arrow down from Suresh."],
        "Son"),
    pat("br-p12", "Two readings fit: cannot be determined", "common",
        "The phrase names a set rather than one person, like 'one of my grandfather's children', and 'Cannot be determined' sits in the options.",
        None,
        ["Decode the phrase and list every person who could match it.",
         "Check whether the speaker's own gender or an 'only' word removes any of them.",
         "If two different relations stay possible, answer 'Cannot be determined'."],
        "The phrase is genuinely under-specified. Picking one reading is the planted error.",
        "Pointing to a man, Meena said: his wife is the daughter of my grandfather's only child. How is the man related to Meena?",
        ["Grandfather's only child = Meena's mother.", "That mother's daughters: Meena, or a sister of Meena.",
         "The man could be Meena's husband or her sister's husband. Both fit."],
        "Cannot be determined"),
    pat("br-p13", "The reverse ask", "common",
        "'How is the speaker related to the person in the photograph?' instead of the usual direction.",
        None,
        ["Decode the phrase exactly as usual.",
         "Note the direction: speaker to person, not person to speaker.",
         "Give the mirror word of what the phrase produced."],
        "The phrase fixes one relation. The question only asks it from the other end.",
        "Pointing to a man, Priya said: he is the son of my grandfather's only son. How is Priya related to the man?",
        ["Grandfather's only son = Priya's father.", "The man is her father's son, so her brother.",
         "Asked from the man's side, going sideways."],
        "Sister"),
]

s3_tricks = [
    {"title": "One layer per line",
     "body": "Underline the innermost 'my' and work outward. Each line of rough work resolves one 'of'. Then place the speaker and the target in a two-person sketch.",
     "example": {"q": "Pointing to a man, Sunita said: he is the only son of my mother's mother's only child. How is the man related to Sunita?",
                 "steps": ["My mother's mother = maternal grandmother.",
                           "Her only child = Sunita's mother.",
                           "That mother's only son = Sunita's brother."],
                 "answer": "Brother"}},
    {"title": "Scan for the fold-back",
     "body": "Before peeling anything, scan the phrase for 'my mother's only child', 'my father's only son', 'my mother's only daughter'. If one is there, test the speaker's gender against it first.",
     "example": {"q": "Pointing to Ketan, Meera said: his mother is the only child of my mother. How is Ketan related to Meera?",
                 "steps": ["The only child of Meera's mother is Meera herself.",
                           "So Ketan's mother is Meera.",
                           "One arrow down."],
                 "answer": "Son"}},
]

s3_mistakes = [
    {"wrong": "Reading 'only son' as 'only child'.",
     "right": "'Only son' bars other boys only. Sisters may exist."},
    {"wrong": "Forgetting the speaker is a person in the tree.",
     "right": "Every 'my' belongs to the speaker. Test fold-back phrases first."},
    {"wrong": "Answering in the reverse direction: 'his sister' instead of 'her brother'.",
     "right": "Check which person the question names after 'related to'."},
    {"wrong": "Peeling a three-layer phrase in one jump.",
     "right": "One layer per line. Slow rough work is fast here."},
    {"wrong": "Choosing a relation when two families both fit the phrase.",
     "right": "Build both readings. If both fit, answer 'Cannot be determined'."},
]

s3_revision = [
    "Replace 'my' with the speaker's name, then peel one layer per line.",
    "'My mother's only child' = the speaker.",
    "'My father's only son' = the speaker only if the speaker is male.",
    "Only son bars boys. Only daughter bars girls. Only child bars everyone.",
    "Two valid readings = 'Cannot be determined'.",
    "Check the asked direction before writing the word.",
    "Learn the block bank: grandfather's only son, aunt's daughter, father's only brother.",
]

# ============================================================ subtopic 4
s4_concept = (
    "The exam invents private symbols: 'P + Q means P is the father of Q'. Then a string like A + B x C hides a small family. "
    "Decode one symbol at a time into a plain sentence. Each symbol fixes the gender of its first letter only. "
    "Draw the tree, then answer in the question's direction."
)

s4_notes = """### What these questions look like
First come the definitions. Then a coded string, then a question about one pair in it.

> **Example:** 'A + B' means A is the brother of B. 'A x B' means A is the wife of B. In the string **A + B x C**, how is A related to C?

No tree exists yet. You build it from the string, symbol by symbol.

### Decode one symbol at a time
Cut the string at every symbol. Each cut gives one plain sentence:

1. A + B: A is the brother of B.
2. B x C: B is the wife of C.

Now draw. A and B share parents, so A sits beside B. B is married to C, so B and C share a row. Read the asked pair: A is the brother of C's wife, so A is C's **brother-in-law**.

> **Rule:** One symbol = one sentence = one link on the tree. Never decode a whole string in one breath.

### Track each letter's gender
This is the whole game. Every symbol fixes the gender of its **first** letter only:

| Symbol says | First letter becomes |
|---|---|
| father, son, brother, husband, uncle | male |
| mother, daughter, sister, wife, aunt | female |
| sibling, cousin, child, parent | no gender |

In A + B x C with the definitions above: A is male (from +), B is female (from x), C is not fixed by anything.

> **Watch:** If the answer needs a gender nobody fixed, the right reply is the neutral word or 'Cannot be determined'. C, above, could be male or female.

### The same symbol twice adds a generation
A + B + C, with + meaning 'father of', reads as: A is the father of B, and B is the father of C. So A is C's grandfather.

Each repeated parent symbol pushes one more generation. Mixed symbols mix a generation step with a sideways step: parent, then sibling, then spouse, and so on. Draw it. Do not try to feel the answer from the string.

> **Tip:** Under the string, write the gender mark for every letter as you decode it: A + B x C becomes A(m) + B(f) x C(?).

### Answer in the question's direction
Symbols read left to right. Questions read either way.

If A + B means 'A is the father of B', then 'How is A related to B?' is answered **father**, but 'How is B related to A?' needs B's gender. B was fixed only if some other symbol fixed it. Otherwise B is a child of A with no known gender: cannot be determined.

> **Watch:** Most wrong answers here come from answering the string's direction instead of the question's.

### Check your tree before marking
Two quick checks catch almost every slip:
- No person can be their own ancestor.
- Opposite genders for a marriage, where the symbol says husband or wife.

If either check fails, one symbol was decoded backwards. Find it before moving on."""

s4_patterns = [
    pat("br-p14", "Two symbols, three letters", "very common",
        "Two symbol definitions and a string like A + B x C. One pair's relation is asked.",
        None,
        ["Translate each symbol into one plain sentence.",
         "Draw the mini tree: siblings share parents, couples share a row.",
         "Read the asked pair, using only the genders the symbols fixed."],
        "Two sentences already form one connected tree, and the answer is a single path on it.",
        "'P + Q' means P is the brother of Q. 'P x Q' means P is the wife of Q. In 'A + B x C', how is A related to C?",
        ["A is B's brother, so A is male.", "B is C's wife, so C is B's husband.",
         "A is the brother of C's wife."],
        "Brother-in-law"),
    pat("br-p15", "Three symbols, four letters", "common",
        "Three definitions and a string like A + B - C x D.",
        None,
        ["Decode left to right, one sentence per symbol, drawing as you go.",
         "Each symbol adds one person. Spouses of parents are parents too.",
         "Answer the asked pair. A gender no symbol fixed means a neutral word."],
        "The string is just three small links. Three small links beat one long guess.",
        "'P + Q' = P is the son of Q. 'P - Q' = P is the wife of Q. 'P x Q' = P is the brother of Q. In 'A + B - C x D', how is A related to D?",
        ["A is B's son, so A is male.", "B is C's wife, so C is A's father.",
         "C is D's brother, so D is A's aunt or uncle. A is D's sibling's son."],
        "Nephew"),
    pat("br-p16", "Reverse ask on a coded string", "common",
        "The string runs A ... B ... C but the question asks how C relates to A.",
        None,
        ["Decode and draw exactly as usual. Do not reverse the string.",
         "Take the viewpoint of the letter named after 'related to'.",
         "Give the mirror word, and check which genders were fixed."],
        "The tree has no direction. Only the final sentence must match the question's direction.",
        "'X # Y' means X is the father of Y. 'X @ Y' means X is the sister of Y. In 'A # B @ C', how is C related to A?",
        ["A is B's father, and B is C's sister, so A is C's parent too.",
         "Asked from A's side, going down one arrow.",
         "C's gender: no symbol fixed it."],
        "Son or daughter: cannot be determined"),
    pat("br-p17", "Build the string for a given relation", "occasional",
        "'Which expression means M is the maternal uncle of K?' The options are strings, not words.",
        None,
        ["Write the target as plain sentences, middle person included: M is the brother of K's mother.",
         "Pick symbols that state exactly those sentences.",
         "Check each option symbol by symbol. Reject any that changes a gender or a generation."],
        "Each option claims one tree. The correct option must rebuild the target sentences exactly.",
        "'P + Q' = P is the brother of Q. 'P - Q' = P is the mother of Q. Which expression means M is the maternal uncle of K?",
        ["Needed sentences: M is the brother of some L, and L is the mother of K.",
         "M + L gives the brother sentence. L - K gives the mother sentence.",
         "Joined: M + L - K."],
        "M + L - K"),
]

s4_tricks = [
    {"title": "Write the sentences under the string",
     "body": "For each symbol, write its one-line sentence under the string, then draw. Six symbols become three short sentences, and the drawing finishes the job.",
     "example": {"q": "'X % Y' = X is the wife of Y. 'X # Y' = X is the sister of Y. In 'M % N # O', how is M related to O?",
                 "steps": ["M is the wife of N.", "N is the sister of O.",
                           "M is married to O's sister."],
                 "answer": "Sister-in-law"}},
    {"title": "Audit genders before answering",
     "body": "Before marking, list every letter with the gender its symbols fixed. If the asked word needs a gender that stayed blank, the answer is the neutral word or 'Cannot be determined'.",
     "example": {"q": "'P @ Q' = P is the son of Q. 'P & Q' = P is the husband of Q. In 'P @ Q & R', how is R related to P?",
                 "steps": ["P is Q's son.", "Q is R's husband, so Q is male and R is his wife.",
                           "R is the wife of P's parent."],
                 "answer": "Mother"}},
]

s4_mistakes = [
    {"wrong": "Decoding a whole string in one breath.",
     "right": "Cut at every symbol. One sentence per cut, then draw."},
    {"wrong": "Fixing the gender of the second letter from the symbol.",
     "right": "'A is the brother of B' fixes A only. B stays blank until another symbol fixes it."},
    {"wrong": "Answering the string's direction instead of the question's.",
     "right": "Read the question. If it asks the reverse pair, give the mirror word."},
    {"wrong": "Forgetting the spouse of a parent is also a parent.",
     "right": "If B is C's wife and B is A's parent, then C is A's parent too."},
    {"wrong": "Marking 'Cannot be determined' without checking every symbol.",
     "right": "List the gender marks first. Only a truly blank needed gender allows that answer."},
]

s4_revision = [
    "One symbol = one sentence = one tree link.",
    "A symbol fixes the gender of its first letter only.",
    "Parent of one sibling is parent of all the siblings.",
    "Spouse of a parent is also a parent.",
    "Same parent symbol twice = one more generation.",
    "Answer the question's direction, not the string's.",
    "A needed gender that stayed blank = 'Cannot be determined'.",
]

# ---------------------------------------------------------------- patch
data = json.loads(TOPIC.read_text(encoding="utf-8"))
subs = {s["id"]: s for s in data["subtopics"]}
assert set(subs) == {"blood-relations-idea", "family-tree-puzzles", "pointing-introduction", "coded-relations"}

def put(sid, concept, notes, formulas, patterns, tricks, mistakes, revision):
    s = subs[sid]
    old_ids = {p["id"] for p in s.get("patterns", [])}
    assert old_ids <= {p["id"] for p in patterns}, f"{sid}: dropped a pattern id"
    assert 2500 <= len(notes) <= 5000, f"{sid}: notes {len(notes)} chars"
    s.update(concept=concept, notes=notes.strip() + "\n", formulas=formulas,
             patterns=patterns, tricks=tricks, mistakes=mistakes, revision=revision)

put("blood-relations-idea", s1_concept, s1_notes, s1_formulas, s1_patterns, s1_tricks, s1_mistakes, s1_revision)
put("family-tree-puzzles", s2_concept, s2_notes, [], s2_patterns, s2_tricks, s2_mistakes, s2_revision)
put("pointing-introduction", s3_concept, s3_notes, [], s3_patterns, s3_tricks, s3_mistakes, s3_revision)
put("coded-relations", s4_concept, s4_notes, [], s4_patterns, s4_tricks, s4_mistakes, s4_revision)

TOPIC.write_text(json.dumps(data, ensure_ascii=False, indent=1) + "\n", encoding="utf-8")
print("blood-relations updated:", {sid: (len(subs[sid]['notes']), len(subs[sid]['patterns'])) for sid in subs})
