"""Readable rewrite of Reasoning > Syllogism (4 subtopics).

Every verdict is computed by enumerating region models: with n terms there are 2^n - 1 regions
(inside at least one term); a model says which regions hold at least one member. Every term class
is assumed non-empty. A definite conclusion follows when it holds in ALL models; a possibility
holds when it holds in at least ONE; either-or means neither follows alone but every model
satisfies at least one of the two.
Run: python syllogism.py  (patches content/core/topics/reasoning/syllogism.json)
"""
import json
from itertools import product
from pathlib import Path

ROOT = Path(__file__).resolve().parents[3]
TOPIC = ROOT / "core" / "topics" / "reasoning" / "syllogism.json"

# ------------------------------------------------------------------ model enumeration
_cache = {}


def models(terms):
    terms = tuple(terms)
    if terms in _cache:
        return _cache[terms]
    n = len(terms)
    regions = list(range(1, 2 ** n))
    out = []
    for bits in product([0, 1], repeat=len(regions)):
        pop = [r for r, b in zip(regions, bits) if b]
        if all(any(r >> i & 1 for r in pop) for i in range(n)):
            out.append(pop)
    _cache[terms] = out
    return out


def holds(st, terms, pop):
    kind, x, y = st
    if kind == "Poss":
        raise ValueError
    ix, iy = terms.index(x), terms.index(y)
    has = lambda r, i: r >> i & 1
    if kind == "All": return not any(has(r, ix) and not has(r, iy) for r in pop)
    if kind == "No": return not any(has(r, ix) and has(r, iy) for r in pop)
    if kind == "Some": return any(has(r, ix) and has(r, iy) for r in pop)
    if kind == "SomeNot": return any(has(r, ix) and not has(r, iy) for r in pop)
    if kind == "Few": return holds(("Some", x, y), terms, pop) and holds(("SomeNot", x, y), terms, pop)
    raise ValueError(kind)


def valid(stmts, terms):
    return [p for p in models(terms) if all(holds(s, terms, p) for s in stmts)]


def terms_of(stmts, concls):
    t = []
    for s in list(stmts) + [c[1:] for c in concls]:
        for w in s[1:]:
            if w not in t: t.append(w)
    return tuple(t)


def verdict(stmts, concl, terms=None):
    """concl = (mode, kind, x, y) with mode 'def' or 'poss'. Returns True/False."""
    terms = terms or terms_of(stmts, [concl])
    vm = valid(stmts, terms)
    assert vm, "statements are inconsistent"
    ok = [holds(concl[1:], terms, p) for p in vm]
    return all(ok) if concl[0] == "def" else any(ok)


def classify(stmts, concls):
    terms = terms_of(stmts, concls)
    vm = valid(stmts, terms)
    assert vm
    t = [verdict(stmts, c, terms) for c in concls]
    if all(t): return "Both I and II follow"
    if t[0]: return "Only I follows"
    if t[1]: return "Only II follows"
    legal = ({concls[0][1], concls[1][1]} in ({"All", "SomeNot"}, {"Some", "No"})
             and concls[0][2:] == concls[1][2:])          # exam convention: only these two opposite pairs
    if legal and all(c[0] == "def" for c in concls) and all(any(holds(c[1:], terms, p) for c in concls) for p in vm):
        return "Either I or II follows"
    return "Neither I nor II follows"


def D(kind, x, y): return ("def", kind, x, y)
def P(kind, x, y): return ("poss", kind, x, y)


def txt(s):
    kind, x, y = s[-3:] if len(s) == 4 else s
    return {"All": f"All {x} are {y}", "No": f"No {x} are {y}", "Some": f"Some {x} are {y}",
            "SomeNot": f"Some {x} are not {y}", "Few": f"Only a few {x} are {y}"}[kind] + "."


def ctxt(c):
    mode, kind, x, y = c
    if mode == "def": return txt((kind, x, y))
    p = {"All": f"All {x} being {y}", "No": f"No {x} being {y}", "Some": f"Some {x} being {y}",
         "SomeNot": f"Some {x} not being {y}"}[kind]
    return p + " is a possibility."


LET = "ABCD"


def mk(stmts, concls, k=0):
    ans = classify(stmts, concls)
    labels = ["Only I follows", "Only II follows", "Both I and II follow", "Neither I nor II follows"]
    if ans == "Either I or II follows":
        labels[2] = ans
    assert ans in labels
    order = labels[k:] + labels[:k]
    q = ("**Statements**\n" + "\n".join(f"- {txt(s)}" for s in stmts)
         + "\n\n**Conclusions**\n" + "\n".join(f"- {r}. {ctxt(c)}" for r, c in zip(["I", "II"], concls))
         + "\n\n**Options**\n" + "\n".join(f"- ({LET[i]}) {o}" for i, o in enumerate(order)))
    return {"q": q, "answer": f"({LET[order.index(ans)]}) {ans}", "label": ans}


def ex(e, steps):
    return {"q": e["q"], "steps": steps, "answer": e["answer"]}


# ------------------------------------------------------------------ rule table (asserted)
A, B, C = "A", "B", "C"
def follows(stmts, kind, x, y): return verdict(stmts, D(kind, x, y))
def possible(stmts, kind, x, y): return verdict(stmts, P(kind, x, y))

assert follows([("All", A, B), ("All", B, C)], "All", A, C)
assert follows([("Some", A, B), ("All", B, C)], "Some", A, C)
assert follows([("All", A, B), ("No", B, C)], "No", A, C) and follows([("All", A, B), ("No", B, C)], "No", C, A)
assert follows([("No", A, B), ("Some", B, C)], "SomeNot", C, A)
assert not follows([("Some", A, B), ("Some", B, C)], "Some", A, C) and not follows([("Some", A, B), ("Some", B, C)], "SomeNot", A, C)
assert not follows([("SomeNot", A, B), ("All", B, C)], "SomeNot", A, C) and not follows([("SomeNot", A, B), ("All", B, C)], "Some", A, C)
assert follows([("All", A, B)], "Some", B, A) and not follows([("All", A, B)], "All", B, A)
assert follows([("No", A, B)], "No", B, A) and follows([("Some", A, B)], "Some", B, A)
assert not follows([("Some", A, B)], "SomeNot", B, A) and not follows([("SomeNot", A, B)], "SomeNot", B, A)
assert follows([("All", A, B), ("Some", A, C)], "Some", B, C)
assert not follows([("Some", A, B), ("No", B, C)], "No", A, C) and follows([("Some", A, B), ("No", B, C)], "SomeNot", A, C)
# possibility facts
assert not possible([("All", A, B)], "No", B, A) and possible([("All", A, B)], "All", B, A) and possible([("All", A, B)], "SomeNot", B, A)
assert not possible([("Few", A, B)], "All", A, B) and possible([("Few", A, B)], "All", B, A) and not possible([("Few", A, B)], "No", A, B)
assert possible([("Some", A, B)], "All", A, B) and possible([("Some", A, B)], "All", B, A) and possible([("Some", A, B)], "SomeNot", A, B)
# either-or facts
def always(stmts, x, y, k1, k2):
    t = terms_of(stmts, [D(k1, x, y), D(k2, x, y)])
    return all(holds((k1, x, y), t, p) or holds((k2, x, y), t, p) for p in valid(stmts, t))
assert always([], A, B, "All", "SomeNot") and always([], A, B, "Some", "No")
assert not always([], A, B, "No", "SomeNot") and not always([], A, B, "All", "No")
# only a few
assert follows([("Few", A, B)], "Some", A, B) and follows([("Few", A, B)], "SomeNot", A, B)
assert not follows([("Few", A, B)], "SomeNot", B, A) and follows([("Few", A, B)], "Some", B, A)

# ------------------------------------------------------------------ examples: syllogism-idea
E1 = mk([("Some", "pens", "books"), ("All", "books", "files")], [D("Some", "pens", "files"), D("All", "pens", "files")], 0)
assert E1["label"] == "Only I follows"
SY1 = ex(E1, ["The shared term is books. The pen that is a book is also a file, so I follows.",
              "For II, draw one pen outside books. All statements still hold, so II fails."])

E2 = mk([("All", "rings", "coins"), ("All", "coins", "metals")], [D("Some", "metals", "rings"), D("All", "metals", "rings")], 1)
assert E2["label"] == "Only I follows"
SY2 = ex(E2, ["Chain the All statements: rings sit inside coins, and coins sit inside metals.",
              "So all rings are metals, and the reverse form 'Some metals are rings' follows too.",
              "II runs the chain backwards. A metal that is not a coin breaks it, so II fails."])

E3 = mk([("No", "walls", "doors"), ("Some", "doors", "gates")], [D("SomeNot", "gates", "walls"), D("No", "gates", "walls")], 2)
assert E3["label"] == "Only I follows"
SY3 = ex(E3, ["The shared term is doors. A gate that is a door cannot be a wall, so I follows.",
              "For II, a gate that is not a door might still be a wall. So II fails."])

E4 = mk([("Some", "tables", "chairs")], [D("Some", "chairs", "tables"), D("All", "chairs", "tables")], 3)
assert E4["label"] == "Only I follows"
SY4 = ex(E4, ["'Some' converts freely, so I follows.", "II adds a new claim about every chair. The statement never says that."])

E17 = mk([("All", "cups", "plates"), ("All", "plates", "bowls"), ("No", "bowls", "jars")],
         [D("No", "cups", "jars"), D("No", "jars", "plates")], 0)
assert E17["label"] == "Both I and II follow"
SY17 = ex(E17, ["Chain the first two: cups sit inside plates, and plates sit inside bowls.",
                "No bowl is a jar, so nothing inside bowls can be a jar. Cups and plates are inside bowls.",
                "That gives both I and II, because 'No' reads the same in both directions."])

E18 = mk([("SomeNot", "birds", "pets"), ("All", "pets", "animals")], [D("SomeNot", "birds", "animals"), D("No", "birds", "animals")], 1)
assert E18["label"] == "Neither I nor II follows"
SY18 = ex(E18, ["The bird outside pets is the only bird we are sure of.",
                "That bird may or may not be an animal. Nothing links it to animals.",
                "So I and II both fail. A 'Some-not' does not travel through an All."])

E20 = mk([("Some", "boxes", "bags"), ("Some", "bags", "sacks")], [D("Some", "boxes", "sacks"), D("Some", "sacks", "boxes")], 2)
assert E20["label"] == "Neither I nor II follows"
SY20 = ex(E20, ["The box that is a bag and the bag that is a sack can be different bags.",
                "Draw the two overlaps apart. Boxes and sacks never meet.",
                "Two 'Some' statements never join. Neither conclusion follows."])

# ------------------------------------------------------------------ possibility-cases
E5 = mk([("Some", "cars", "trucks"), ("Some", "trucks", "buses")], [P("All", "buses", "cars"), D("No", "cars", "buses")], 0)
assert E5["label"] == "Only I follows"
SY5 = ex(E5, ["For I, draw all buses inside cars. The car-truck overlap and the truck-bus overlap still hold. So I follows.",
              "For II, cars and buses may overlap. So 'No car is a bus' is not forced, and II fails."])

E6 = mk([("All", "tables", "desks"), ("No", "desks", "shelves")], [P("All", "shelves", "tables"), D("No", "shelves", "tables")], 1)
assert E6["label"] == "Only II follows"
SY6 = ex(E6, ["Tables sit inside desks, and no desk is a shelf. So no table can be a shelf. II follows.",
              "For I, all shelves would sit inside tables, and so inside desks. That breaks 'No desk is a shelf'. I fails."])

E7 = mk([("Few", "lamps", "bulbs")], [P("All", "lamps", "bulbs"), P("All", "bulbs", "lamps")], 1)
assert E7["label"] == "Only II follows"
SY7 = ex(E7, ["'Only a few lamps are bulbs' means some lamps are bulbs and some lamps are not bulbs.",
              "I asks for all lamps to be bulbs. The lamp that is not a bulb blocks it.",
              "II asks for all bulbs to be lamps. Draw bulbs inside lamps and keep one lamp outside. It works, so II follows."])

E8 = mk([("All", "ships", "boats"), ("Some", "boats", "rafts")], [P("All", "rafts", "ships"), D("Some", "ships", "rafts")], 2)
assert E8["label"] == "Only I follows"
SY8 = ex(E8, ["For I, draw rafts inside ships, and ships inside boats. The boat-raft overlap still exists. So I follows.",
              "II is a definite claim. The raft that is a boat may not be a ship. So II fails."])

E19 = mk([("All", "lions", "cats")], [P("No", "cats", "lions"), P("Some", "cats", "lions")], 3)
assert E19["label"] == "Only II follows"
SY19 = ex(E19, ["Every lion is a cat, and lions exist. So at least one cat is a lion.",
                "I needs no cat to be a lion. That is impossible, so I fails.",
                "II is already true in every picture. So it is certainly possible."])

# ------------------------------------------------------------------ either-or
E9 = mk([("All", "rings", "metals"), ("Some", "metals", "heavy")], [D("All", "rings", "heavy"), D("SomeNot", "rings", "heavy")], 0)
assert E9["label"] == "Either I or II follows"
SY9 = ex(E9, ["Same two terms: rings and heavy. The pair is 'All' and 'Some-not'.",
              "Test each alone. The statements do not fix how rings relate to heavy. Neither follows alone.",
              "Either every ring is heavy, or some ring is not. Nothing else can happen."])

E10 = mk([("All", "keys", "metals")], [D("Some", "keys", "iron"), D("No", "keys", "iron")], 2)
assert E10["label"] == "Either I or II follows"
SY10 = ex(E10, ["Same two terms: keys and iron. The pair is 'Some' and 'No'.",
                "The statement does not link keys to iron, so neither follows alone.",
                "Keys and iron either share a member or do not. One of the two is always true."])

E11 = mk([("All", "cups", "dishes"), ("Some", "dishes", "pots")], [D("No", "cups", "pots"), D("SomeNot", "cups", "pots")], 3)
assert E11["label"] == "Neither I nor II follows"
SY11 = ex(E11, ["The pair is 'No' and 'Some-not'. That is not a complementary pair.",
                "Draw every cup inside pots. Then I fails, and II fails as well.",
                "Both can be false together, so there is no either-or. The answer is neither."])

E12 = mk([("All", "pens", "books"), ("No", "books", "files"), ("Some", "files", "bags")],
         [D("Some", "bags", "pens"), D("No", "bags", "pens")], 1)
assert E12["label"] == "Either I or II follows"
SY12 = ex(E12, ["The conclusions use bags and pens. They form the pair 'Some' and 'No'.",
                "A bag can be a pen, and a bag can fail to be one. Neither follows alone.",
                "The other statements do not settle the bags-pens link. So the answer is either-or."])

E22 = mk([("All", "pens", "books"), ("All", "books", "files")], [D("All", "pens", "files"), D("SomeNot", "pens", "files")], 0)
assert E22["label"] == "Only I follows"
SY22 = ex(E22, ["The pair is 'All' and 'Some-not', so it looks like an either-or.",
                "Test each alone first. Chain the statements: all pens are files. I follows.",
                "Because I follows alone, the answer is 'Only I'. Never choose either-or here."])

# ------------------------------------------------------------------ definite cases
E13 = mk([("Few", "pens", "pencils")], [D("SomeNot", "pens", "pencils"), D("SomeNot", "pencils", "pens")], 1)
assert E13["label"] == "Only I follows"
SY13 = ex(E13, ["Split the statement: some pens are pencils, and some pens are not pencils.",
                "I is the second half, so it follows.",
                "II is about pencils outside pens. The statement says nothing about that side. II fails."])

E14 = mk([("Few", "cups", "plates"), ("All", "plates", "bowls")], [D("Some", "cups", "bowls"), D("SomeNot", "cups", "bowls")], 3)
assert E14["label"] == "Only I follows"
SY14 = ex(E14, ["The cup that is a plate is also a bowl. So I follows.",
                "The cup that is not a plate may still be a bowl. So II fails."])

E15 = mk([("Some", "doctors", "singers"), ("All", "singers", "dancers")], [D("Some", "doctors", "dancers"), D("SomeNot", "doctors", "singers")], 0)
assert E15["label"] == "Only I follows"
SY15 = ex(E15, ["Treat 'A few' like 'Some'. Some doctors are singers, and every singer is a dancer.",
                "So some doctors are dancers. I follows.",
                "II needs a doctor outside singers. 'A few' does not guarantee it, so II fails."])

E16 = mk([("Few", "birds", "pets"), ("No", "pets", "stones")], [D("SomeNot", "birds", "stones"), P("All", "birds", "stones")], 2)
assert E16["label"] == "Only I follows"
SY16 = ex(E16, ["Some birds are pets. A pet is never a stone. So some birds are not stones. I follows.",
                "II asks for all birds to be stones. The bird that is a pet would have to be a stone. II fails."])

E21 = mk([("Few", "trees", "plants"), ("Few", "plants", "shrubs")], [D("Some", "trees", "shrubs"), D("SomeNot", "trees", "shrubs")], 1)
assert E21["label"] == "Neither I nor II follows"
SY21 = ex(E21, ["Each 'only a few' gives some and some-not. The two links do not join up.",
                "The trees that are plants may all be shrubs, or none of them may be. Neither claim is forced."])


def block(e):
    return "\n".join(f"- {s}" for s in e["steps"])


# ------------------------------------------------------------------ text
CONCEPT = {
    "syllogism-idea": (
        "A syllogism gives two or three statements that you must accept as true. Then you judge conclusions. "
        "A conclusion follows only if it holds in **every** picture that fits the statements.\n\n"
        "Real-world facts do not matter. Try to break each conclusion with one picture."),
    "possibility-cases": (
        "A possibility conclusion asks a lighter question: can this be true without breaking a statement? "
        "One supporting picture is enough to make it follow.\n\n"
        "It fails only when a statement makes it impossible."),
    "either-or": (
        "Sometimes neither conclusion follows on its own, but they are exact opposites. Then one of them is true in every picture, and the answer is 'Either I or II follows'.\n\n"
        "Only two shapes of pairs qualify. Always test each conclusion alone first."),
    "definite-cases": (
        "'Only a few A are B' means two things at once: some A are B and some A are not B. "
        "'A few' and 'Many' mean plain 'Some'.\n\n"
        "Split the statement first. Then treat it like any other syllogism."),
}

N1 = f"""### What a syllogism asks
You get two or three statements. Accept them as true, even when they sound silly. Then you get conclusions to judge.

A conclusion **follows** only if it is true in every picture that fits the statements. One picture that breaks it is enough to reject it.

> **Rule:** Assume every group named in the statements has at least one member.

### The four statement forms
| Statement | Meaning |
|---|---|
| All A are B | Every A is inside B. B may be bigger. |
| No A are B | A and B never meet. |
| Some A are B | At least one member is in both. |
| Some A are not B | At least one A lies outside B. |

**All** and **No** describe the whole group. **Some** only promises that one member exists. That makes conclusions built on 'some' easy to break.

### Safe reversals
| Statement | Reversal that follows |
|---|---|
| All A are B | Some B are A |
| No A are B | No B are A |
| Some A are B | Some B are A |
| Some A are not B | none |

> **Watch:** 'All A are B' does not give 'All B are A'. 'Some A are not B' does not give 'Some B are not A'.

### Chains that work
- All A are B and All B are C give **All A are C**.
- Some A are B and All B are C give **Some A are C**.
- All A are B and No B are C give **No A are C**.
- No A are B and Some B are C give **Some C are not A**.

### Chains that do not work
- Two 'Some' statements never join. Some A are B and Some B are C give nothing about A and C.
- A 'Some-not' does not pass through an All. The A that is outside B may or may not be a C.

### Try to break the conclusion
Do not draw a picture that helps the conclusion. Draw the smallest picture that fits the statements. Then ask whether you can move one group to make the conclusion false.

If you can, the conclusion fails. If you cannot, it follows.

### Reading the options
Judge conclusion I and conclusion II separately. Then look at the options.

- Only I follows: II can be broken.
- Only II follows: I can be broken.
- Both follow: neither can be broken.
- Neither follows: both can be broken.

Never let one conclusion influence the other. Each one has its own test.

### A worked example
{E1["q"]}

**Solution**
{block(SY1)}

Answer: **{SY1["answer"]}**.
"""

N2 = f"""### What a possibility conclusion asks
A definite conclusion says: this **must** be true. A possibility conclusion says: this **can** be true.

You are now looking for one picture only. If some picture fits every statement and also makes the possibility true, the possibility follows.

> **Rule:** For a possibility, one supporting picture is enough. It follows unless a statement blocks it.

### The one-picture method
1. Read the possibility as a request. For example: can I put all buses inside cars?
2. Try to draw it. Keep every statement true, especially every overlap.
3. If you can, it follows. If every attempt collides with a statement, it fails.

### What blocks a possibility
- **A No statement.** If no desk is a shelf, then no table inside desks can be a shelf.
- **A forced overlap.** If every lion is a cat, no cat can fail to be a lion in all cases. 'No cat is a lion' is impossible.
- **Only a few.** 'Only a few A are B' rules out 'All A are B'. It also rules out 'No A are B'.

> **Watch:** Groups are never empty. So a possibility that empties a group always fails.

### What stays possible
Most other cases stay possible. From 'Some A are B', all of these can be true: all A are B, all B are A, some A are not B.

From 'Only a few A are B', 'All B are A' is still possible. Draw B inside A and keep one A outside.

### Two conclusions together
Often one conclusion is a possibility and the other is definite. Judge them by different standards. The definite one needs every picture. The possibility needs one picture.

Then match the pair to the options: only I, only II, both or neither.

### Words that signal a possibility
Look for 'is a possibility', 'may be true' or 'can be true'. These words change the question from 'must' to 'can'.

Without them, treat the conclusion as definite.

### A quick self-check
After you pick an answer, test it once. If you said a possibility fails, name the statement that blocks it. If you said it follows, name the picture that shows it.

Both answers should be easy to say in one sentence.

### A worked example
{E5["q"]}

**Solution**
{block(SY5)}

Answer: **{SY5["answer"]}**.
"""

N3 = f"""### What an either-or pair is
Sometimes neither conclusion follows on its own, but the two conclusions are exact opposites. Then one of them is true in every picture. The answer is **Either I or II follows**.

This is logic, not luck. If two conclusions are negations of each other, no picture can make both false.

### The two legal pairs
Both conclusions must use the **same two terms**, in either order.

| Pair | Why it covers every case |
|---|---|
| All A are B and Some A are not B | Either every A is inside B, or one A is outside. |
| Some A are B and No A are B | Either A and B meet, or they do not. |

### The three-step test
1. Check the pair. Same two terms? One of the two legal shapes? If not, there is no either-or.
2. Test each conclusion alone. If one follows, the answer is 'Only I' or 'Only II'.
3. If neither follows alone, the answer is 'Either I or II follows'.

> **Rule:** Always do step 2 before step 3. A conclusion that follows alone rules out either-or.

### Pairs that look right but are not
- **Different terms.** 'All A are B' and 'Some A are not C' are not opposites.
- **No and Some-not.** Both can be false. A group inside B has some A in B, but no A outside B.
- **All and No.** Both can be false when A partly overlaps B.
- **Some and Some-not.** Both can be true together, so exams do not treat them as a pair.

> **Watch:** Two conclusions that are both false at the same time are never an either-or pair.

### Extra statements
With three statements, ignore the extra one while you check the pair shape. It matters only in step 2, where it may prove one conclusion alone.

### Where it shows up in the options
The option 'Either I or II follows' appears only when the answer is truly either-or. If you see it, do not pick it by habit.

Check the pair shape and run the alone test before you choose it.

### Why the pairs work
Take 'All A are B' and 'Some A are not B'. A is either entirely inside B or not. There is no third case.

Take 'Some A are B' and 'No A are B'. The two groups either share a member or they share none. Again there is no third case.

### A worked example
{E10["q"]}

**Solution**
{block(SY10)}

Answer: **{SY10["answer"]}**.
"""

N4 = f"""### What only a few really says
Modern papers use three phrases.

- **Some A are B**: at least one A is a B. Nothing more.
- **A few** and **Many A are B**: exactly the same as Some.
- **Only a few A are B**: two facts at once. Some A are B, and some A are not B.

So 'Only a few cups are plates' guarantees a cup outside plates. It says nothing about plates that are not cups.

> **Rule:** Split 'only a few' into two arrows. Feed both into your picture.

### What follows at once
From **Only a few A are B**:
- Some A are B follows.
- Some A are not B follows.
- All A are B is false.
- No A are B is false.
- Anything about B outside A is undecided.

### Combining with All
Take 'Only a few A are B' and 'All B are C'.
- Some A are C follows. The A that is a B is also a C.
- Some A are not C does **not** follow. The A outside B may still be a C.

> **Watch:** Only the A-and-B member travels through the All. The A-outside-B member does not.

### Combining with No
Take 'Only a few A are B' and 'No B are C'. Then some A are not C follows, because the A that is a B cannot be a C.

But 'All A are C' is impossible in this case. It would put that A into C.

### Two only-a-few statements
'Only a few A are B' and 'Only a few B are C' do not join. The A-and-B members and the B-and-C members can be different members.

### Three phrases side by side
| Phrase | Some A are B | Some A are not B |
|---|---|---|
| Some A are B | Yes | Not fixed |
| A few / Many A are B | Yes | Not fixed |
| Only a few A are B | Yes | Yes |

Only the last phrase guarantees the outside part. That is the whole difference between them. Do not read 'A few' or 'Many' as 'only a few'. They promise the overlap and nothing else.

### Checking with a picture
Draw the outside A member as a dot beside the B circle. Then ask whether the dot has to sit inside C. If it can sit either way, the conclusion is not forced.

Watch which side each conclusion is about. 'Some A are not B' talks about the A side. 'Some B are not A' talks about the B side.

'Only a few A are B' fixes the first and leaves the second open.

### A worked example
{E14["q"]}

**Solution**
{block(SY14)}

Answer: **{SY14["answer"]}**.
"""

MISTAKES = {
    "syllogism-idea": [
        {"wrong": "Rejecting a statement because it is false in real life.", "right": "Accept every statement as true. Reason only from the statements."},
        {"wrong": "Reading 'All A are B' as 'All B are A'.", "right": "All does not reverse. Only 'Some B are A' follows."},
        {"wrong": "Joining two 'Some' statements into a conclusion.", "right": "Two 'Some' statements never join. Draw the overlaps apart to test."},
        {"wrong": "Passing a 'Some-not' through an All.", "right": "The A outside B may or may not be a C. Nothing follows."},
        {"wrong": "Drawing the picture that supports the conclusion.", "right": "Draw the smallest picture that fits the statements. Then try to break the conclusion."},
    ],
    "possibility-cases": [
        {"wrong": "Looking for a picture where the possibility must hold.", "right": "You need only one picture where it can hold."},
        {"wrong": "Ignoring the 'No' statement when you draw the possibility.", "right": "A 'No' statement blocks every picture that puts a member across it."},
        {"wrong": "Saying 'No B are A' is possible after 'All A are B'.", "right": "Groups are non-empty. A member of A is a member of B, so B and A must meet."},
        {"wrong": "Saying 'All A are B' is possible after 'Only a few A are B'.", "right": "Only a few guarantees an A outside B, so that possibility is dead."},
        {"wrong": "Judging a definite conclusion by the one-picture rule.", "right": "A definite conclusion must hold in every picture."},
    ],
    "either-or": [
        {"wrong": "Choosing either-or when one conclusion follows alone.", "right": "Test each conclusion alone first. If one follows, choose 'Only I' or 'Only II'."},
        {"wrong": "Treating 'No' and 'Some-not' as an opposite pair.", "right": "They can both be false. Only (All, Some-not) and (Some, No) are opposites."},
        {"wrong": "Pairing conclusions that use different terms.", "right": "Both conclusions must use the same two terms."},
        {"wrong": "Treating 'All' and 'No' as a pair.", "right": "Both are false when A only partly overlaps B."},
        {"wrong": "Skipping the pair check because the statements are long.", "right": "Extra statements only matter in the alone test. The pair shape decides the rest."},
    ],
    "definite-cases": [
        {"wrong": "Reading 'A few' or 'Many' as 'only a few'.", "right": "They mean plain 'Some'. No outside part is guaranteed."},
        {"wrong": "Assuming 'only a few A are B' says something about B outside A.", "right": "It only fixes the A side. B outside A is undecided."},
        {"wrong": "Passing the outside-A member through 'All B are C'.", "right": "Only the A-and-B member travels. The outside member may or may not be a C."},
        {"wrong": "Thinking 'only a few' allows 'All A are B'.", "right": "It guarantees an A outside B, so 'All A are B' is false."},
        {"wrong": "Joining two only-a-few statements.", "right": "The overlaps can be different members. Nothing joins."},
    ],
}

REVISION = {
    "syllogism-idea": [
        "Accept the statements as true. A conclusion follows only if it holds in every picture.",
        "All converts to Some. No and Some convert both ways. Some-not does not convert.",
        "Chains that work: All+All, Some+All, All+No, No+Some (gives Some-not).",
        "Two 'Some' statements never join. A 'Some-not' does not pass through an All.",
        "Draw the smallest picture and try to break the conclusion with one counter-picture.",
        "Assume every named group has at least one member.",
    ],
    "possibility-cases": [
        "A possibility needs one supporting picture. A definite conclusion needs every picture.",
        "A 'No' statement blocks a possibility that pushes a member across it.",
        "Groups are non-empty. 'All A are B' makes 'No B are A' impossible.",
        "'Only a few A are B' rules out 'All A are B' but leaves 'All B are A' possible.",
        "Judge a mixed pair by different standards. Then match the options.",
    ],
    "either-or": [
        "Either-or needs neither conclusion alone and an exact opposite pair.",
        "Legal pairs: (All, Some-not) and (Some, No), on the same two terms.",
        "(No, Some-not) and (All, No) can both be false. They are not pairs.",
        "Test each conclusion alone first. One that follows ends the either-or idea.",
        "Extra statements do not change the pair shape.",
    ],
    "definite-cases": [
        "Only a few A are B = Some A are B + Some A are not B.",
        "A few and Many = plain Some. Nothing is guaranteed outside.",
        "Only the A-and-B member travels through All B are C.",
        "Only a few A are B makes 'All A are B' and 'No A are B' false.",
        "Nothing is fixed about B outside A.",
    ],
}

TRICKS = {
    "syllogism-idea": [
        {"title": "Find the shared term", "body": "The conclusion must join the two outer terms. Find the term that appears in both statements, and ask what travels through it.",
         "example": {"q": "All pens are books. Some books are files. Does 'Some pens are files' follow?", "steps": ["The shared term is books.", "The files that are books may not be pens.", "Draw the file-books outside pens."], "answer": "No."}},
        {"title": "One counter-picture kills it", "body": "You do not need to prove a conclusion. You need only one picture that fits the statements and breaks it."},
    ],
    "possibility-cases": [
        {"title": "Defence lawyer thinking", "body": "For a possibility, flip your mindset. Build one picture where it holds. Done."},
    ],
    "either-or": [
        {"title": "Spot the opposite pair", "body": "Look for (All, Some-not) or (Some, No) on the same two terms. Then test each alone.",
         "example": {"q": "I. Some shirts are red. II. No shirts are red. The statements never mention red. Answer?", "steps": ["Same terms, and the pair is Some and No.", "Neither follows alone.", "So one of them holds in every picture."], "answer": "Either I or II follows."}},
    ],
    "definite-cases": [
        {"title": "Split on sight", "body": "Rewrite every 'Only a few A are B' as two lines: Some A are B, and Some A are not B. Then solve as normal."},
    ],
}

PATS = {
    "syllogism-idea": [
        dict(id="syl-p1", name="Some + All chain (shared member travels)", frequency="very common",
             howToSpot="'Some A are B' then 'All B are C' (or the other order). One conclusion links A and C.",
             steps=["Find the term that both statements share.", "The guaranteed A-and-B member is a B, so it is also a C.", "So 'Some A are C' follows.", "Test the other conclusion by drawing a counter-picture."],
             why="The member we are sure of travels through the All.", ex=SY1),
        dict(id="syl-p2", name="All-chain with a conversion conclusion", frequency="very common",
             howToSpot="Two 'All' statements form a chain. One conclusion turns the chain around.",
             steps=["Chain the All statements: A inside B inside C.", "'All A are C' follows.", "'Some C are A' also follows.", "Reject 'All C are A'. The chain never runs backwards."],
             why="Containment carries forward, and the reverse needs new information.", ex=SY2),
        dict(id="syl-p3", name="No + Some gives Some-not", frequency="common",
             howToSpot="'No A are B' and 'Some B are C'. The conclusion is about C and A.",
             steps=["Find the shared class B.", "The B-and-C member cannot be an A.", "So 'Some C are not A' follows.", "Reject stronger claims such as 'No C are A'."],
             why="The shared member inherits B's total exile from A.", ex=SY3),
        dict(id="syl-p4", name="Conversion-only pair", frequency="common",
             howToSpot="One statement and two conclusions. One is its plain reversal, and the other overreaches it.",
             steps=["Recall the safe reversals: All gives Some. Some and No reverse both ways.", "The reversal follows.", "The other conclusion adds a new claim. Reject it."],
             why="A reversal only swaps the terms. It never adds new information.", ex=SY4),
        dict(id="syl-p17", name="Three-statement chain", frequency="common",
             howToSpot="Three statements link four groups in a line, mostly All and No.",
             steps=["Chain the All statements from the left.", "Carry the chain through the group named in the No statement.", "Anything inside that group is also cut off from the last group.", "Remember to reverse a No statement freely."],
             why="Everything inside a group inherits that group's No relation.", ex=SY17),
        dict(id="syl-p18", name="Some-not does not travel", frequency="common",
             howToSpot="'Some A are not B' with 'All B are C'. The conclusions are about A and C.",
             steps=["Find the outside member: an A that is not a B.", "Ask whether it must be a C. Nothing forces it in or out.", "Draw it outside C, then draw it inside C.", "Neither conclusion is forced."],
             why="The All statement covers B only. It says nothing about members outside B.", ex=SY18),
        dict(id="syl-p20", name="Two Some statements", frequency="common",
             howToSpot="'Some A are B' and 'Some B are C'. Conclusions link A and C.",
             steps=["Note that the two overlaps may involve different members of B.", "Draw them apart.", "Test both conclusions in that picture.", "Neither follows."],
             why="A 'Some' promises one member. Two promises can point to different members.", ex=SY20),
    ],
    "possibility-cases": [
        dict(id="syl-p5", name="Plain possibility (nothing blocks it)", frequency="very common",
             howToSpot="The words 'is a possibility' appear, and no 'No' statement touches the two terms.",
             steps=["Try to draw the possibility around the statements.", "Keep every 'Some' overlap alive.", "If one clean picture survives, the possibility follows."],
             why="A possibility needs one consistent picture, not every picture.", ex=SY5),
        dict(id="syl-p6", name="Possibility blocked by a No statement", frequency="very common",
             howToSpot="A 'No X are Y' statement, and a possibility that would push X members into Y.",
             steps=["Trace the members that are sure to exist.", "Ask if the possibility would force one of them across the 'No'.", "If yes, the possibility fails.", "Test the partner conclusion separately."],
             why="A 'No' statement allows no crossing, whatever the picture.", ex=SY6),
        dict(id="syl-p7", name="Possibility with only-a-few statements", frequency="common",
             howToSpot="'Only a few A are B' and a possibility about A, B or a third group.",
             steps=["Split it into Some and Some-not.", "'All A are B' is now impossible.", "Try to draw the other possibilities, such as 'All B are A'.", "Keep the ones you can draw."],
             why="Only-a-few fixes the A side and leaves the B side open.", ex=SY7),
        dict(id="syl-p8", name="Possibility paired with a definite conclusion", frequency="common",
             howToSpot="One conclusion is a possibility. The other is a definite claim.",
             steps=["Test the definite one with a counter-picture.", "Build one picture for the possibility.", "Match the two results to the options."],
             why="The two halves use different standards.", ex=SY8),
        dict(id="syl-p19", name="Possibility that empties a group", frequency="occasional",
             howToSpot="After 'All A are B', a possibility such as 'No B are A'.",
             steps=["Remember that every group has at least one member.", "Every A is a B, so B and A meet.", "Any possibility that separates them fails."],
             why="If groups cannot be empty, an All statement forces an overlap.", ex=SY19),
    ],
    "either-or": [
        dict(id="syl-p9", name="(All, Some-not) complementary pair", frequency="very common",
             howToSpot="Conclusions 'All A are B' and 'Some A are not B'. The same two terms, and neither follows alone.",
             steps=["Check that the terms match.", "Test each conclusion alone.", "If neither follows, choose 'Either I or II'."],
             why="A is either wholly inside B or partly outside. No third case exists.", ex=SY9),
        dict(id="syl-p10", name="(Some, No) complementary pair", frequency="very common",
             howToSpot="Conclusions 'Some A are B' and 'No A are B' on the same two terms.",
             steps=["Check the terms and the pair shape.", "Test each alone.", "If neither follows, choose either-or."],
             why="Two groups either share a member or they do not.", ex=SY10),
        dict(id="syl-p11", name="Fake complementary pair", frequency="common",
             howToSpot="The conclusions look like a pair but use different terms, or use (No, Some-not), or one follows alone.",
             steps=["Compare the terms word by word.", "Reject the (No, Some-not) shape.", "If one conclusion follows alone, answer that one."],
             why="Both conclusions can be false together, so the either-or argument breaks.", ex=SY11),
        dict(id="syl-p12", name="Either-or with three statements", frequency="occasional",
             howToSpot="Three statements, but the two conclusions only ask about one pair of terms.",
             steps=["Ignore the extra statements while you check the pair shape.", "Test each conclusion alone. An extra statement might prove one.", "If neither is proved, choose either-or."],
             why="The pair argument needs only the two conclusions.", ex=SY12),
        dict(id="syl-p22", name="One of the pair is provable", frequency="common",
             howToSpot="The conclusions form a legal pair, but the statements give a chain that settles one of them.",
             steps=["Notice the legal pair.", "Do not stop there. Test each conclusion alone first.", "If one follows, answer 'Only' that one."],
             why="A conclusion that follows in every picture makes its opposite false in every picture.", ex=SY22),
    ],
    "definite-cases": [
        dict(id="syl-p13", name="Only-a-few direct consequences", frequency="very common",
             howToSpot="'Only a few A are B', and conclusions quoting Some, Some-not, All or No on A and B.",
             steps=["Rewrite as Some A are B and Some A are not B.", "All A are B and No A are B are false.", "Anything about B outside A is undecided."],
             why="Only-a-few welds two facts about the A side and says nothing about B.", ex=SY13),
        dict(id="syl-p14", name="Only-a-few + All chain", frequency="common",
             howToSpot="'Only a few A are B' and 'All B are C'. Conclusions are about A and C.",
             steps=["The A-and-B member is also a C, so 'Some A are C' follows.", "The A outside B is not tied to C.", "So 'Some A are not C' does not follow."],
             why="Only the B member travels through the All.", ex=SY14),
        dict(id="syl-p15", name="'A few / Many' = plain Some", frequency="common",
             howToSpot="The statement says 'A few A are B' or 'Many A are B'. Students over-read it as only-a-few.",
             steps=["Treat it exactly as 'Some A are B'.", "No outside part is guaranteed.", "Chain the Some member through any All."],
             why="'A few' and 'Many' only promise that the overlap exists.", ex=SY15),
        dict(id="syl-p16", name="Only-a-few with possibility and No statements", frequency="occasional",
             howToSpot="An only-a-few statement, a No statement and a mix of definite and possibility conclusions.",
             steps=["Split only-a-few into Some and Some-not.", "Trace the guaranteed member through the No statement.", "Test each conclusion by its own standard."],
             why="The No statement can cut off the guaranteed member from a third group.", ex=SY16),
        dict(id="syl-p21", name="Two only-a-few statements", frequency="occasional",
             howToSpot="'Only a few A are B' and 'Only a few B are C', with conclusions about A and C.",
             steps=["Split both statements.", "The A-and-B members and B-and-C members may differ.", "Draw the two overlaps apart.", "Neither Some nor Some-not is forced."],
             why="Each only-a-few links one pair. Two links do not join.", ex=SY21),
    ],
}

NOTES = {"syllogism-idea": N1, "possibility-cases": N2, "either-or": N3, "definite-cases": N4}


def pat(d):
    e = d["ex"]
    return {"id": d["id"], "name": d["name"], "frequency": d["frequency"], "howToSpot": d["howToSpot"],
            "formula": None, "steps": d["steps"], "why": d["why"],
            "example": {"q": e["q"], "steps": e["steps"], "answer": e["answer"]}}


data = json.loads(TOPIC.read_text(encoding="utf-8"))
all_new = [p["id"] for k in PATS for p in PATS[k]]
assert len(all_new) == len(set(all_new))
for sid in PATS:
    sub = next(s for s in data["subtopics"] if s["id"] == sid)
    old = {p["id"] for p in sub.get("patterns", [])}
    new = {p["id"] for p in PATS[sid]}
    assert old <= new, (sid, old - new)
    n = NOTES[sid]
    assert 2500 <= len(n) <= 5000, (sid, len(n))
    sub.update(concept=CONCEPT[sid], notes=n.strip() + "\n", patterns=[pat(d) for d in PATS[sid]],
               mistakes=MISTAKES[sid], revision=REVISION[sid], tricks=TRICKS[sid])
    print(sid, len(n), "chars,", len(old), "->", len(new), "patterns")
with open(TOPIC, "w", encoding="utf-8", newline="\n") as f:
    json.dump(data, f, ensure_ascii=False, indent=1)
    f.write("\n")
