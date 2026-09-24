# -*- coding: utf-8 -*-
"""Deep content for syllogism.json — every answer verified by a finite model checker.

Method: represent each world as the set of populated Venn regions (n terms -> 2^n-1
regions).  A world is VALID if every statement is true in it and every named class is
non-empty (exam convention).  A definite conclusion follows iff true in ALL valid
worlds; a possibility conclusion follows iff true in SOME valid world; an either-or
pair must be exact negations (true in exactly one of I/II in every valid world) and
neither may follow alone.  Existing questions are re-checked and reported.
"""
from _lib import *

# ---------------- mechanical syllogism solver ----------------

def _base(kind, a, b, W, n):
    ai, bi = 1 << a, 1 << b
    if kind == "A":   # all a are b
        return not any((r & ai) and not (r & bi) for r in W)
    if kind == "N":   # no a is b
        return not any((r & ai) and (r & bi) for r in W)
    if kind == "S":   # some a are b
        return any((r & ai) and (r & bi) for r in W)
    if kind == "SN":  # some a are not b
        return any((r & ai) and not (r & bi) for r in W)
    if kind == "OAF":  # only a few a are b = Some a-b AND Some a not b
        return (_base("S", a, b, W, n) and _base("SN", a, b, W, n))
    raise ValueError(kind)


def valid_worlds(n, stmts):
    """All subsets of the 2^n-1 regions where every statement holds and all n
    named classes are non-empty."""
    out = []
    nreg = (1 << n) - 1
    for bits in range(1, 1 << nreg):
        W = [r for r in range(1, nreg + 1) if (bits >> (r - 1)) & 1]
        cover = 0
        for r in W:
            cover |= r
        if cover != (1 << n) - 1:          # some named class empty -> not a model
            continue
        if all(_base(k, a, b, W, n) for (k, a, b) in stmts):
            out.append(W)
    return out


def solve(terms, stmts, c1, c2):
    """Return 'I' | 'II' | 'both' | 'either' | 'neither'.
    stmts: list of (kind, termA, termB) using term NAMES.
    c1/c2: (mode, kind, termA, termB), mode in {'def','poss'}."""
    idx = {t: i for i, t in enumerate(terms)}
    S = [(k, idx[a], idx[b]) for (k, a, b) in stmts]
    n = len(terms)
    Ws = valid_worlds(n, S)
    assert Ws, "no valid world"

    def holds(c, W):
        return _base(c[1], idx[c[2]], idx[c[3]], W, n)

    def f(c):
        if c[0] == "def":
            return all(holds(c, W) for W in Ws)
        return any(holds(c, W) for W in Ws)

    f1, f2 = f(c1), f(c2)
    if f1 and f2:
        return "both"
    if f1:
        return "I"
    if f2:
        return "II"
    if c1[0] == "def" and c2[0] == "def":
        if all(holds(c1, W) != holds(c2, W) for W in Ws):
            return "either"
    return "neither"


# ---------------- option scaffolding ----------------

STD = ["Only conclusion I follows", "Only conclusion II follows",
       "Both conclusions follow", "Neither conclusion follows"]
EO = ["Only conclusion I follows", "Only conclusion II follows",
      "Either conclusion I or II follows", "Neither conclusion follows"]
PICK = {"I": 0, "II": 1, "both": 2, "either": 2, "neither": 3}


def sq(qid, stmt_txt, c1_txt, c2_txt, terms, stmts, c1, c2, use_eo,
       expected, sol, short, diff, pat, t):
    v = solve(terms, stmts, c1, c2)
    assert v == expected, f"{qid}: engine says {v}, designed {expected}"
    opts = EO if use_eo else STD
    ans = opts[PICK[v]]
    wrong = [o for o in opts if o != ans]
    q = (f"**Statements:** {stmt_txt}\n\n**Conclusions:**\nI. {c1_txt}\nII. {c2_txt}\n\n"
         "Which of the conclusions follow(s)?")
    return Q(qid, q, ans, wrong, sol, short, diff, SUB, pat, t)


d = load("syllogism")

# ---------------- notes ----------------

NOTES_IDEA = """### What is a syllogism?
A syllogism gives you two or three **statements** that you must accept as true, and a set of **conclusions**. You must decide which conclusions follow *necessarily*. The topic of the sentences is irrelevant — if the paper says "All cats are engineers", you accept it and reason from it. Real-world truth never matters here.

### The four statement forms
| Statement | Meaning | Least-committal picture |
|---|---|---|
| All A are B | every A is inside B; B may be bigger | A-circle inside B-circle |
| No A is B | the two classes never meet | two separate circles |
| Some A are B | at least one member sits in both | two overlapping circles |
| Some A are not B | at least one member of A sits outside B | A-circle partly outside B |

Notice the asymmetry: **All** and **No** fix the whole class, while **Some** fixes only that at least one member exists. That is why conclusions built on "some" are weak and easy to break.

### The minimal-diagram method
1. Draw the **least-committal** diagram that satisfies all statements — never draw what a conclusion wants. "Some A are B" is two overlapping circles, nothing more.
2. For each conclusion, try to **break** it: move the free parts of the diagram while keeping every statement true.
3. If even one valid diagram breaks the conclusion, it **does not follow**. If no valid diagram can break it, it **follows**.

This is the opposite of how students usually work. You are not collecting evidence for a conclusion; you are acting as its enemy. One successful attack kills it.

### Moves that are always legal
- **All-chain**: All A are B + All B are C → All A are C (and hence Some C are A).
- **Conversion of All**: All A are B → Some B are A (classes are never empty in these exams).
- **Conversion of Some**: Some A are B → Some B are A.
- **Conversion of No**: No A is B → No B is A.
- **Some + All chain**: Some A are B + All B are C → Some A are C. The shared member travels through.
- **No + Some**: Some B are C + No A is B → Some C are not A (the shared member inherits B's exile from A).

### Moves that look legal but are not
- All A are B **does not** give All B are A (B may be much bigger).
- Some A are B **does not** give Some A are not B (possibly all A are B).
- No A is B + No B is C gives **nothing** about A and C.
- Some A are B + Some B are C gives **nothing** definite about A and C.

### Worked example
Statements: No glass is metal. Some metals are solids.
Conclusion I: Some solids are not glass. Conclusion II: All glasses are solids.
The metal-that-is-solid cannot be glass, so that solid is "a solid not a glass" — I follows. Glass has no fixed link with solids, so a diagram with all glass inside solids and another with glass outside are both valid — II is breakable, so it fails.

### Common traps
- Drawing the conclusion's picture instead of the statements'.
- Rejecting "Some B are A" because it "reverses" the statement — that reversal is always valid.
- Judging a conclusion from the first diagram you drew instead of asking whether a second diagram could break it.

### Quick revision
- Accept statements as true; ignore real life.
- Draw the least-committal diagram, then hunt one counter-diagram per conclusion.
- Legal: All-chains, All→Some, Some/No conversions, Some+All travel, No+Some exile.
- Illegal: reverse-All, Some→Some-not, No+No chains, Some+Some chains.
- Follows = true in every valid diagram. Break it once = reject.
"""

NOTES_POSS = """### What a possibility conclusion asks
A definite conclusion says: "this **must** be true". A possibility conclusion says: "this **can** be true without breaking any statement". The question "All A being B is a possibility" is asking only whether some picture that satisfies the statements can also have A inside B. You are no longer the prosecutor hunting counter-examples — you are the defence lawyer who needs just **one** supporting diagram.

### The one-diagram rule
1. Read the possibility as a request: "may I draw A inside B (or A meeting B, etc.)?"
2. Try to build that picture while keeping every statement true.
3. If you succeed even once, the possibility **follows**. If every attempt collides with a statement, it fails.

### What blocks a possibility
Almost always a **No statement** cutting across the terms. If some A is definitely a C, and No C is B, then putting all A inside B would force that C-member into B — a collision. The possibility dies. Two weaker blockers:
- An **Only a few A are B** statement forbids "All A are B", but still allows most other possibilities.
- A **Some A are not B** statement (given directly) also forbids All A are B, but allows A to move freely otherwise.

Anything not touching the terms of the possibility is irrelevant — a "No" about two far-away classes never blocks anything.

### Definite vs possibility — the mirror pair
| Conclusion type | To prove it | To kill it |
|---|---|---|
| Definite ("follows") | must hold in every diagram | find ONE diagram that breaks it |
| Possibility | find ONE diagram that supports it | show EVERY diagram collides |

So the same sentence ("All A are B") can fail as a definite conclusion and still follow as a possibility. Statements "All keys are locks, some locks are doors": "Some keys are doors" fails (the door-lock overlap can dodge keys), but "All keys being doors is a possibility" follows (draw all keys inside the key-door overlap).

### Worked examples
1. Statements: Some books are novels. All novels are stories. Conclusion: All books being stories is a possibility. Draw all books inside stories (the book-novel part is fine, the rest of the books too) — nothing objects → follows.
2. Statements: Some phones are cameras. No camera is a charger. Conclusion: All phones being chargers is a possibility. The phone-camera member is a camera, so it can never be a charger — the picture is impossible → does not follow.

### Speed habits
- Possibility questions are usually **faster** than definite ones — one clever diagram ends the debate.
- If a "No" statement's two classes do not both touch your terms, ignore it and answer "follows".
- When one option says "X is a possibility" and the other is a definite claim, solve the definite one with counter-examples first; often only one survives.

### Quick revision
- Possibility = consistent with the statements = one supporting diagram is enough.
- Definite = forced = must survive every diagram.
- Only a crossing "No" (or an explicit Some-not / only-a-few on the same pair) can kill a possibility.
- The shared member of a "Some" statement must obey every statement that mentions its class.
- Same pair can fail as definite and pass as possibility — read the wording carefully.
"""

NOTES_EO = """### What an either-or pair is
Sometimes neither conclusion follows on its own, but the two conclusions are **exact opposites** of each other. In that case one of them must be true in every possible picture — the exam answer is **"Either I or II follows"**. This is not generosity; it is logic. If two statements are negations, no valid diagram can make both false.

### The two legal complementary pairs
About the **same two terms**, in any order:

| Pair | Why they are negations |
|---|---|
| All A are B  +  Some A are not B | either every A is inside B, or at least one A is outside — nothing else can happen |
| Some A are B  +  No A is B | either the classes meet, or they never do — nothing else can happen |

### The three-step test
1. Check the pair: same two terms, and one of the two legal shapes above? If not, either-or is impossible.
2. Test each conclusion separately with the counter-diagram method. If **either one follows alone**, answer "Only I/II follows" — never either-or.
3. If neither follows alone, answer "Either I or II follows".

Step 2 before step 3 — the commonest error is jumping to either-or when one conclusion was actually provable.

### Traps that break the pair
- **Different terms.** "All cups are bowls" + "Some cups are not plates" look like the (All, Some-not) shape but the second pair is cups–plates, not cups–bowls. Both can fail at once → neither follows.
- **No + Some-not is NOT a pair.** "No pencil is an eraser" and "Some pencils are not erasers" can both be false — when all pencils are erasers. They are not negations.
- **Reversed terms are fine.** "Some A are B" and "No B is A" are still negations (both links are symmetric), so the pair still works.
- **One conclusion contradicts a statement.** It then fails immediately, but the other still needs checking — the pair rule only applies when neither follows alone.

### Worked examples
1. Statements: Some flowers are red. No flower is blue. Conclusions: I. All flowers are red. II. Some flowers are not red. Same pair (flowers–red), legal (All, Some-not) shape, neither provable → either-or.
2. Statements: All beds are sofas. Conclusions: I. Some sofas are beds. II. No sofa is a bed. I follows at once by conversion — so the answer is "Only I follows", NOT either-or. This is the classic trap.

### Why the rule is safe
Take the (Some, No) pair about A–B. In any valid diagram either the A–B overlap is populated (I true) or empty (II true). Since every class is non-empty, there is no third option and no way to lose both. The same argument covers (All, Some-not): A is either fully inside B or it is not.

### Quick revision
- Legal pairs only: (All, Some-not) and (Some, No) — same two terms.
- Order of work: check the shape → test each conclusion alone → only then mark either-or.
- If one follows alone, pick it; never mark either-or.
- No + Some-not is a fake pair; different-term pairs are fake.
- Reversed word order does not spoil the pair.
"""

NOTES_DEF = """### What "only a few" really says
Modern papers use three graded phrases:
- **Some A are B** — at least one A is a B. Nothing more.
- **A few / Many A are B** — exactly the same as Some. Treat them as synonyms.
- **Only a few A are B** — two statements welded into one: **Some A are B AND Some A are not B**. The part of A outside B is *guaranteed*, not just possible.

So "Only a few cups are plates" gives you a definite gift: a part of the cups lies outside plates. But it says **nothing** about B: plates may be almost all cups or almost none — only the A-side is fixed.

### Immediate consequences
From **Only a few A are B**:
- ✓ Some A are B (follows)
- ✓ Some A are not B (follows)
- ✗ All A are B (contradicted)
- ✗ No A is B (contradicted)
- ✗ All B are A, Some B are not A — nothing is fixed on the B side

The guaranteed "A outside B" member still moves freely with respect to any third class C: if All B are C, that member *may or may not* be a C. Do not chain "Some A are not B" through an All the way students chain "Some A are B".

### Combining with All statements
Only a few A are B + All B are C:
- ✓ Some A are C — the A∩B member is a C.
- ✗ Some A are not C — the non-B A's are not pinned outside C.
This one-directional behaviour is the most tested subtlety of the whole subtopic.

### Worked examples
1. Only a few keys are brass. All brass items are metal. No metal is plastic. Conclusion: Some keys are not plastic. The key-that-is-brass is metal, hence not plastic — that key is "a key not a plastic" → follows. But "All keys being plastic is a possibility" fails: that same key can never be plastic.
2. A few students are athletes. All athletes are fit. Conclusion: Some students are fit — follows (a few = some, then the shared member travels). Conclusion: All students are athletes — fails.

### How exam questions use it
- A conclusion pair where one half is "Some A are not B" — check whether an only-a-few statement already guarantees it.
- A possibility conclusion "All A being B is a possibility" — if an only-a-few A-B statement exists, it is dead on arrival.
- Mixed with plain Some statements to see if you notice which side is guaranteed.

### Common mistakes
- Reading "only a few" as "few = almost none" and inventing a No statement.
- Reading it as plain Some and missing the guaranteed outside part.
- Concluding "Some B are not A" from it — the B side is never fixed.

### Quick revision
- Only a few A are B = Some A are B + Some A are not B (A-side guaranteed split).
- A few / many = plain Some.
- Follows at once: Some A are B, Some A are not B. Dead at once: All A are B, No A is B.
- B-side stays free: no conclusion about B outside A.
- The guaranteed non-B member of A does not automatically escape any third class.
"""

set_sub(d, "syllogism-idea", notes=NOTES_IDEA)
set_sub(d, "possibility-cases", notes=NOTES_POSS)
set_sub(d, "either-or", notes=NOTES_EO)
set_sub(d, "definite-cases", notes=NOTES_DEF)

# ---------------- patterns ----------------

P_IDEA = [
 P("syl-p1", "Some + All chain (shared member travels)", "very common",
   "A 'Some A are B' statement followed by 'All B are C' (or the reverse order), with a conclusion about A and C.",
   "1. Spot the term B that appears in both statements.\n2. The guaranteed A∩B member is a B, so it is also a C — the conclusion 'Some A are C' is forced.\n3. Check any second conclusion independently (it usually reverses the All, which is illegal).\n\n*Why it works:* one real member travels through both statements; the rest of the classes stay free.",
   "**Some chairs are tables. All tables are desks.** Conclusions: I. Some chairs are desks. II. All desks are chairs.",
   "The chair-that-is-a-table is a desk → I follows. II reverses an All → fails. **Only I follows.**"),
 P("syl-p2", "All-chain with a conversion conclusion", "very common",
   "Two 'All' statements in a chain, and one conclusion is the reversed 'Some C are A' while the other reverses an All directly.",
   "1. Chain the All's: A ⊂ B ⊂ C gives All A are C.\n2. Convert freely: Some C are A also follows.\n3. Reject any 'All C are A' — the chain never runs backwards.\n\n*Why it works:* containment carries forward; the reverse needs new information the statements never give.",
   "**All stones are rocks. All rocks are minerals.** Conclusions: I. All stones are minerals. II. All minerals are stones.",
   "Stones ⊂ rocks ⊂ minerals → I follows. Minerals stretch beyond stones → II fails. **Only I follows.**"),
 P("syl-p3", "No + Some gives Some-not", "common",
   "A 'No A is B' plus a 'Some B are C' (or 'Some C are B'), conclusion about C and A.",
   "1. Find the shared class B.\n2. The guaranteed B∩C member cannot be an A, so it is 'a C that is not an A' → Some C are not A follows.\n3. Any stronger conclusion (No C is A, All C are A) is breakable.\n\n*Why it works:* the shared member inherits B's complete exile from A.",
   "**No lizard is a bird. Some birds are black.** Conclusion: Some black things are not lizards.",
   "The black bird is a bird, and no bird is a lizard → it is a black thing that is not a lizard. **Follows.**"),
 P("syl-p4", "Conversion-only pair (is the reversal enough?)", "common",
   "A single statement and two conclusions where one is its exact conversion and the other overreaches it.",
   "1. Recall: All→Some converts; Some converts; No converts.\n2. The conversion conclusion follows.\n3. The other conclusion adds a new quantifier (All, Some-not, No) that the statement never fixed → reject.\n\n*Why it works:* conversion only swaps the terms; it never strengthens the claim.",
   "**All actors are artists.** Conclusions: I. Some artists are actors. II. All artists are actors.",
   "All→Some conversion makes I follow; II is the illegal reverse of an All. **Only I follows.**"),
]

P_POSS = [
 P("syl-p5", "Plain possibility (nothing blocks it)", "very common",
   "'… is a possibility' wording and no No statement touching the two terms of the possibility.",
   "1. Try to draw the possibility (e.g. all A inside B) around the given statements.\n2. Keep every statement true — especially every Some-overlap.\n3. If one clean picture survives, the possibility follows.\n\n*Why it works:* a possibility needs one consistent diagram, not all of them.",
   "**All windows are doors. Some doors are gates.** Conclusion: All gates being windows is a possibility.",
   "Draw gates inside windows, windows inside doors, plus extra doors outside windows. Every statement holds → **follows.**"),
 P("syl-p6", "Possibility blocked by a No statement", "very common",
   "The statements contain 'No X is Y' and the possibility would push a member of X (or of a class that must meet X) into Y.",
   "1. Trace the guaranteed member created by a Some statement.\n2. Ask: could that member be forced into a forbidden class if the possibility were drawn?\n3. If yes, the possibility is impossible; also test the partner conclusion with the counter-method.\n\n*Why it works:* the shared member of a Some statement must obey every No statement that touches its class.",
   "**Some phones are cameras. No camera is a charger.** Conclusion: All phones being chargers is a possibility.",
   "The phone-camera member is a camera, so it can never be a charger — all phones inside chargers is impossible. **Does not follow.**"),
 P("syl-p7", "Possibility with only-a-few statements", "common",
   "An 'Only a few A are B' statement plus a possibility conclusion about A, B or a third class.",
   "1. Split only-a-few into Some + Some-not.\n2. 'All A being B' is now impossible — the guaranteed non-B part forbids it.\n3. Other possibilities (about third classes, or All B being A) are usually still alive — try to draw them.\n\n*Why it works:* only-a-few pins the A-side split; everything not touching that split stays free.",
   "**Only a few chairs are sofas. All sofas are furniture.** Conclusions: I. All chairs being furniture is a possibility. II. Some chairs are not sofas.",
   "I: draw every chair inside furniture (sofa-chairs are furniture, the rest too) — nothing objects → follows. II: guaranteed by only-a-few → follows. **Both follow.**"),
 P("syl-p8", "Possibility paired with a definite conclusion", "common",
   "One conclusion is a possibility, the other a definite claim about the same or another pair.",
   "1. Solve the definite conclusion first with the counter-diagram method.\n2. Then build one diagram for the possibility.\n3. Match the combined result to the options — 'only I', 'only II', 'both' or 'neither'.\n\n*Why it works:* the two halves use different standards (every diagram vs one diagram) and must be judged separately.",
   "**All shirts are clothes. Some clothes are expensive.** Conclusions: I. Some shirts are expensive. II. All expensive things being shirts is a possibility.",
   "I: the clothes-expensive overlap can dodge shirts → fails. II: draw all expensive things inside shirts (shirts inside clothes) — consistent → follows. **Only II follows.**"),
]

P_EO = [
 P("syl-p9", "(All, Some-not) complementary pair", "very common",
   "Conclusions 'All A are B' and 'Some A are not B' — same two terms, neither follows alone.",
   "1. Confirm the two terms match.\n2. Test each alone: neither can be proved when the statements leave A's link with B open.\n3. Mark 'Either I or II follows'.\n\n*Why it works:* A is either wholly inside B or at least partly outside — no third option exists.",
   "**Some candles are lamps.** Conclusions: I. All candles are lamps. II. Some candles are not lamps.",
   "Neither is forced by the single Some statement, and they are exact negations. **Either I or II follows.**"),
 P("syl-p10", "(Some, No) complementary pair", "very common",
   "Conclusions 'Some A are B' and 'No A is B' about the same two terms.",
   "1. Confirm the pair and the terms.\n2. Check neither follows alone (the statements leave the A–B overlap undecided).\n3. Mark either-or.\n\n*Why it works:* the overlap is either populated or empty — one of the two must hold.",
   "**All keys are metal.** Conclusions: I. Some keys are iron. II. No key is iron.",
   "Nothing fixes keys against iron, so neither follows alone; the pair is a true negation pair. **Either I or II follows.**"),
 P("syl-p11", "Fake complementary pair (trap)", "common",
   "The conclusions LOOK like a legal pair but use different terms, or use (No, Some-not), or one of them actually follows alone.",
   "1. Check the terms word by word — both conclusions must use the same two classes.\n2. Reject the (No, Some-not) shape — it is not a negation pair.\n3. If one conclusion follows by itself, answer that one; never either-or.\n\n*Why it works:* the either-or shortcut is valid only for exact negations about one pair of terms.",
   "**Some pencils are erasers.** Conclusions: I. No pencil is an eraser. II. Some pencils are not erasers.",
   "I is contradicted by the statement. II is not forced. And they can both fail (all pencils are erasers) → **Neither follows.**"),
 P("syl-p12", "Either-or with three statements", "occasional",
   "A three-statement puzzle where the two conclusions ignore most of it and just form a negation pair.",
   "1. Ignore the extra statement while checking the pair shape — it only matters for step 2.\n2. Test each conclusion alone (the extra statement may occasionally prove one).\n3. If neither is provable, mark either-or.\n\n*Why it works:* the pair argument needs only the two conclusion terms; extra statements cannot create a third option.",
   "**All squares are rectangles. Some rectangles are big. No big thing is small.** Conclusions: I. Some squares are small. II. No square is small.",
   "Squares may or may not be big, so small links stay undecided; neither follows alone → **Either I or II follows.**"),
]

P_DEF = [
 P("syl-p13", "Only-a-few direct consequences", "very common",
   "A statement 'Only a few A are B' and conclusions quoting Some A are B / Some A are not B / All A are B / No A is B.",
   "1. Rewrite at once: Some A are B ✓ and Some A are not B ✓.\n2. All A are B and No A is B are both dead.\n3. Anything about the B-side (Some B are not A) is undecided.\n\n*Why it works:* 'only a few' welds two facts about the A-side and nothing about the B-side.",
   "**Only a few mangoes are sweet.** Conclusions: I. Some mangoes are sweet. II. All mangoes are sweet.",
   "I is half of the split → follows. II collides with the guaranteed non-sweet part → fails. **Only I follows.**"),
 P("syl-p14", "Only-a-few + All chain", "common",
   "'Only a few A are B' plus 'All B are C', conclusions about A and C.",
   "1. Some A are B, and that member is a C → Some A are C follows.\n2. The guaranteed non-B A-member is NOT automatically a non-C — do not chain the Some-not through.\n3. Test any possibility about third classes with one supporting diagram.\n\n*Why it works:* only the B-side member is guaranteed to travel; the outside member stays free.",
   "**Only a few cups are plates. All plates are dishes.** Conclusions: I. Some cups are dishes. II. Some cups are not dishes.",
   "The cup-that-is-a-plate is a dish → I follows. Non-plate cups may still be dishes → II fails. **Only I follows.**"),
 P("syl-p15", "'A few / Many' = plain Some", "common",
   "The statement reads 'A few A are B' or 'Many A are B' — students over-read it as only-a-few.",
   "1. Treat it exactly as 'Some A are B' — no guaranteed outside part.\n2. 'Some A are not B' now does NOT follow.\n3. Chain the Some member through any All statement as usual.\n\n*Why it works:* 'a few/many' only asserts existence of the overlap, unlike 'only a few'.",
   "**A few students are athletes. All athletes are fit.** Conclusions: I. Some students are fit. II. All students are athletes.",
   "The student-athlete is fit → I follows. II is the reverse-All trap → fails. **Only I follows.**"),
 P("syl-p16", "Only-a-few with possibility and No statements", "occasional",
   "An only-a-few puzzle whose conclusions mix a definite claim with an '… is a possibility'.",
   "1. Split only-a-few; use its guaranteed member for definite conclusions.\n2. For a possibility, try to draw it — only-a-few kills only 'All A are B' on its own pair.\n3. A No statement elsewhere can still block a possibility — trace the guaranteed member through it.\n\n*Why it works:* the guaranteed member obeys every statement; possibilities need one clean diagram elsewhere.",
   "**Only a few keys are brass. All brass items are metal. No metal is plastic.** Conclusions: I. Some keys are not plastic. II. All keys being plastic is a possibility.",
   "The key-that-is-brass is metal, never plastic → I follows. That same key cannot be plastic, so II is impossible. **Only I follows.**"),
]

set_sub(d, "syllogism-idea", patterns=P_IDEA)
set_sub(d, "possibility-cases", patterns=P_POSS)
set_sub(d, "either-or", patterns=P_EO)
set_sub(d, "definite-cases", patterns=P_DEF)

# ---------------- new practice questions ----------------
SUB = "syllogism-idea"
new_idea = [
 sq("syllogism-idea-p01", "Some chairs are tables. All tables are desks.",
    "Some chairs are desks.", "Some desks are chairs.",
    ["chairs", "tables", "desks"],
    [("S", "chairs", "tables"), ("A", "tables", "desks")],
    ("def", "S", "chairs", "desks"), ("def", "S", "desks", "chairs"), False, "both",
    "The chair-that-is-a-table is a desk, so I follows; II is the free conversion of I, so it follows too. **Both follow.**",
    "Some+All: the shared member travels; then convert freely.",
    "easy", "syl-p1", 40),
 sq("syllogism-idea-p02", "Some kings are queens. All queens are wise.",
    "Some kings are wise.", "All wise people are kings.",
    ["kings", "queens", "wise"],
    [("S", "kings", "queens"), ("A", "queens", "wise")],
    ("def", "S", "kings", "wise"), ("def", "A", "wise", "kings"), False, "I",
    "The king-queen member is wise → I follows. 'All wise are kings' reverses an All → breakable → fails. **Only I.**",
    "Chain the Some member through the All; never reverse an All.",
    "medium", "syl-p1", 45),
 sq("syllogism-idea-p03", "All stones are rocks. All rocks are minerals.",
    "Some minerals are stones.", "All minerals are rocks.",
    ["stones", "rocks", "minerals"],
    [("A", "stones", "rocks"), ("A", "rocks", "minerals")],
    ("def", "S", "minerals", "stones"), ("def", "A", "minerals", "rocks"), False, "I",
    "Stones ⊂ rocks ⊂ minerals, and stones exist, so some minerals are stones → I follows. Minerals extend beyond rocks → II fails. **Only I.**",
    "All-chain forward + the free conversion; the chain never runs backwards.",
    "medium", "syl-p2", 45),
 sq("syllogism-idea-p04", "All telephones are devices. All devices are gadgets. Some gadgets are toys.",
    "Some telephones are toys.", "All telephones are gadgets.",
    ["telephones", "devices", "gadgets", "toys"],
    [("A", "telephones", "devices"), ("A", "devices", "gadgets"), ("S", "gadgets", "toys")],
    ("def", "S", "telephones", "toys"), ("def", "A", "telephones", "gadgets"), False, "II",
    "The gadget-toy overlap can sit entirely outside telephones → I fails. The chain gives telephones ⊂ gadgets → II follows. **Only II.**",
    "The All-chain is certain; a Some on a far pair is never forced.",
    "hard", "syl-p2", 60),
 sq("syllogism-idea-p05", "No lizard is a bird. Some birds are black.",
    "Some black things are not lizards.", "All black things are birds.",
    ["lizards", "birds", "black"],
    [("N", "lizards", "birds"), ("S", "birds", "black")],
    ("def", "SN", "black", "lizards"), ("def", "A", "black", "birds"), False, "I",
    "The black bird cannot be a lizard → I follows. Black things may include non-birds → II fails. **Only I.**",
    "The shared Some member inherits the No statement's exile.",
    "medium", "syl-p3", 45),
 sq("syllogism-idea-p06", "No pen is a pencil. All pencils are stationery.",
    "Some stationery is not a pen.", "No stationery is a pen.",
    ["pens", "pencils", "stationery"],
    [("N", "pens", "pencils"), ("A", "pencils", "stationery")],
    ("def", "SN", "stationery", "pens"), ("def", "N", "stationery", "pens"), False, "I",
    "Every pencil is stationery and no pencil is a pen → those stationery items are not pens → I follows. Stationery (other items) may well include pens → II fails. **Only I.**",
    "No + All chain: the pencil block inside stationery is permanently pen-free.",
    "hard", "syl-p3", 60),
 sq("syllogism-idea-p07", "All actors are artists.",
    "Some artists are actors.", "All artists are actors.",
    ["actors", "artists"],
    [("A", "actors", "artists")],
    ("def", "S", "artists", "actors"), ("def", "A", "artists", "actors"), False, "I",
    "All→Some conversion always follows (classes are never empty). The reverse All is not implied. **Only I.**",
    "Conversion of All = free Some; the reverse All is the trap.",
    "easy", "syl-p4", 35),
 sq("syllogism-idea-p08", "Some singers are dancers.",
    "Some dancers are singers.", "Some singers are not dancers.",
    ["singers", "dancers"],
    [("S", "singers", "dancers")],
    ("def", "S", "dancers", "singers"), ("def", "SN", "singers", "dancers"), False, "I",
    "I is the plain conversion → follows. II is possible but never forced (all singers could be dancers) → fails. **Only I.**",
    "Some converts both ways; Some never gives Some-not.",
    "medium", "syl-p4", 40),
]

SUB = "possibility-cases"
new_poss = [
 sq("possibility-cases-p01", "All windows are doors. Some doors are gates.",
    "All gates being windows is a possibility.", "Some windows are gates.",
    ["windows", "doors", "gates"],
    [("A", "windows", "doors"), ("S", "doors", "gates")],
    ("poss", "A", "gates", "windows"), ("def", "S", "windows", "gates"), False, "I",
    "I: draw gates inside windows, windows inside doors, with extra doors outside — consistent → follows. II: the door-gate overlap can avoid windows → not forced. **Only I.**",
    "Possibility needs one clean diagram; a Some overlap is never forced onto a third class.",
    "easy", "syl-p5", 45),
 sq("possibility-cases-p02", "Some spoons are forks.",
    "All forks being spoons is a possibility.", "No fork is a spoon.",
    ["spoons", "forks"],
    [("S", "spoons", "forks")],
    ("poss", "A", "forks", "spoons"), ("def", "N", "forks", "spoons"), False, "I",
    "I: draw all forks inside spoons — the Some overlap survives → follows. II is a definite No, nothing forces it → fails. **Only I.**",
    "With a lone Some statement, almost every possibility passes.",
    "medium", "syl-p5", 40),
 sq("possibility-cases-p03", "All cups are vessels. No vessel is a rod.",
    "All cups being rods is a possibility.", "Some vessels are not cups.",
    ["cups", "vessels", "rods"],
    [("A", "cups", "vessels"), ("N", "vessels", "rods")],
    ("poss", "A", "cups", "rods"), ("def", "SN", "vessels", "cups"), False, "neither",
    "I: cups sit inside vessels, and vessels never meet rods — so cups can never be rods → impossible. II: vessels could all be cups (nothing says otherwise) → not forced. **Neither follows.**",
    "A No statement across the possibility's terms kills it; outside classes stay free.",
    "medium", "syl-p6", 55),
 sq("possibility-cases-p04", "Some phones are cameras. No camera is a charger.",
    "All phones being chargers is a possibility.", "Some phones are not chargers.",
    ["phones", "cameras", "chargers"],
    [("S", "phones", "cameras"), ("N", "cameras", "chargers")],
    ("poss", "A", "phones", "chargers"), ("def", "SN", "phones", "chargers"), False, "II",
    "The phone-camera member is a camera, so it can never be a charger → I is impossible. That same member is a phone outside chargers → II follows. **Only II.**",
    "Trace the Some member through the No statement — it settles both conclusions.",
    "hard", "syl-p6", 65),
 sq("possibility-cases-p05", "Only a few chairs are sofas. All sofas are furniture.",
    "All chairs being furniture is a possibility.", "Some chairs are not sofas.",
    ["chairs", "sofas", "furniture"],
    [("OAF", "chairs", "sofas"), ("A", "sofas", "furniture")],
    ("poss", "A", "chairs", "furniture"), ("def", "SN", "chairs", "sofas"), False, "both",
    "I: draw every chair inside furniture (sofa-chairs are furniture, the rest join freely) — consistent → follows. II: guaranteed by only-a-few → follows. **Both.**",
    "Only-a-few kills only 'All A are B'; other possibilities stay open.",
    "hard", "syl-p7", 70),
 sq("possibility-cases-p06", "Only a few pens are markers.",
    "All pens being markers is a possibility.", "Some pens are not markers.",
    ["pens", "markers"],
    [("OAF", "pens", "markers")],
    ("poss", "A", "pens", "markers"), ("def", "SN", "pens", "markers"), False, "II",
    "Only-a-few guarantees pens outside markers, so all-pens-inside-markers is impossible → I fails. II is the guaranteed half → follows. **Only II.**",
    "'All … is a possibility' dies the moment an only-a-few touches the same pair.",
    "medium", "syl-p7", 50),
 sq("possibility-cases-p07", "All shirts are clothes. Some clothes are expensive.",
    "Some shirts are expensive.", "All expensive things being shirts is a possibility.",
    ["shirts", "clothes", "expensive"],
    [("A", "shirts", "clothes"), ("S", "clothes", "expensive")],
    ("def", "S", "shirts", "expensive"), ("poss", "A", "expensive", "shirts"), False, "II",
    "I: the clothes-expensive overlap can dodge shirts → fails. II: draw all expensive things inside shirts (shirts inside clothes) — every statement holds → follows. **Only II.**",
    "Definite and possibility use different standards — judge each on its own.",
    "hard", "syl-p8", 60),
 sq("possibility-cases-p08", "Some books are novels. All novels are stories.",
    "All books being stories is a possibility.", "Some stories are books.",
    ["books", "novels", "stories"],
    [("S", "books", "novels"), ("A", "novels", "stories")],
    ("poss", "A", "books", "stories"), ("def", "S", "stories", "books"), False, "both",
    "I: draw all books inside stories (the book-novel part already is; the rest joins) → follows. II: the book-novel member is a story → follows definitely. **Both.**",
    "A possibility passes when no No statement is near; the Some member still gifts a definite.",
    "medium", "syl-p8", 55),
]

SUB = "either-or"
new_eo = [
 sq("either-or-p01", "Some candles are lamps.",
    "All candles are lamps.", "Some candles are not lamps.",
    ["candles", "lamps"],
    [("S", "candles", "lamps")],
    ("def", "A", "candles", "lamps"), ("def", "SN", "candles", "lamps"), True, "either",
    "Neither half is forced by a lone Some statement, and they are exact negations about candles–lamps. **Either I or II follows.**",
    "(All, Some-not) on the same terms with no individual proof = either-or.",
    "easy", "syl-p9", 40),
 sq("either-or-p02", "All shirts are cotton.",
    "All shirts are white.", "Some shirts are not white.",
    ["shirts", "cotton", "white"],
    [("A", "shirts", "cotton")],
    ("def", "A", "shirts", "white"), ("def", "SN", "shirts", "white"), True, "either",
    "Nothing links shirts with white, so neither follows alone; the pair is a true negation pair. **Either I or II follows.**",
    "The statements may ignore the pair completely — the pair rule still works.",
    "medium", "syl-p9", 45),
 sq("either-or-p03", "Some rings are gold.",
    "Some rings are silver.", "No ring is silver.",
    ["rings", "gold", "silver"],
    [("S", "rings", "gold")],
    ("def", "S", "rings", "silver"), ("def", "N", "rings", "silver"), True, "either",
    "Gold is a decoy — silver is untouched, so neither conclusion is provable. Some/No on the same pair = complementary. **Either I or II follows.**",
    "Ignore the unused statement; judge only the conclusion pair.",
    "easy", "syl-p10", 40),
 sq("either-or-p04", "All keys are metal. Some metal is heavy.",
    "Some keys are iron.", "No key is iron.",
    ["keys", "metal", "heavy", "iron"],
    [("A", "keys", "metal"), ("S", "metal", "heavy")],
    ("def", "S", "keys", "iron"), ("def", "N", "keys", "iron"), True, "either",
    "Iron is never mentioned in the statements, so keys–iron stays open; the Some/No pair covers it. **Either I or II follows.**",
    "Three statements cannot close a pair the statements never touch.",
    "medium", "syl-p10", 50),
 sq("either-or-p05", "Some cups are plates.",
    "All cups are bowls.", "Some cups are not plates.",
    ["cups", "plates", "bowls"],
    [("S", "cups", "plates")],
    ("def", "A", "cups", "bowls"), ("def", "SN", "cups", "plates"), True, "neither",
    "The two conclusions look like an (All, Some-not) pair, but they use different second terms (bowls vs plates). A world with all cups inside plates and outside bowls fails both. **Neither follows.**",
    "Same-shape pair with mismatched terms is the classic fake — check the terms word by word.",
    "hard", "syl-p11", 60),
 sq("either-or-p06", "Some pencils are erasers.",
    "No pencil is an eraser.", "Some pencils are not erasers.",
    ["pencils", "erasers"],
    [("S", "pencils", "erasers")],
    ("def", "N", "pencils", "erasers"), ("def", "SN", "pencils", "erasers"), True, "neither",
    "I is contradicted by the statement. II is not forced. And both can fail together (all pencils are erasers) — No + Some-not is NOT a negation pair. **Neither follows.**",
    "(No, Some-not) is the fake pair students fall for; only (All, Some-not) and (Some, No) work.",
    "hard", "syl-p11", 60),
 sq("either-or-p07", "All beds are sofas.",
    "Some sofas are beds.", "No sofa is a bed.",
    ["beds", "sofas"],
    [("A", "beds", "sofas")],
    ("def", "S", "sofas", "beds"), ("def", "N", "sofas", "beds"), True, "I",
    "I follows at once by conversion (All→Some). Once one conclusion follows alone, never mark either-or, however tempting the pair looks. **Only I follows.**",
    "Step order: test each conclusion alone BEFORE using the either-or shortcut.",
    "medium", "syl-p11", 45),
 sq("either-or-p08", "Some windows are glass. All glass is transparent.",
    "All windows are glass.", "Some windows are not glass.",
    ["windows", "glass", "transparent"],
    [("S", "windows", "glass"), ("A", "glass", "transparent")],
    ("def", "A", "windows", "glass"), ("def", "SN", "windows", "glass"), True, "either",
    "The transparent chain does not pin windows fully inside or outside glass. Neither follows alone; the (All, Some-not) pair does. **Either I or II follows.**",
    "Extra true statements cannot create a third option for a negation pair.",
    "medium", "syl-p12", 55),
 sq("either-or-p09", "All squares are rectangles. Some rectangles are big. No big thing is small.",
    "Some squares are small.", "No square is small.",
    ["squares", "rectangles", "big", "small"],
    [("A", "squares", "rectangles"), ("S", "rectangles", "big"), ("N", "big", "small")],
    ("def", "S", "squares", "small"), ("def", "N", "squares", "small"), True, "either",
    "Squares may or may not be big, so their link with small stays open — neither follows alone. The Some/No pair is complementary. **Either I or II follows.**",
    "Chain what you can; if the pair's terms stay undecided, mark either-or.",
    "hard", "syl-p12", 65),
]

SUB = "definite-cases"
new_def = [
 sq("definite-cases-p01", "Only a few mangoes are sweet.",
    "Some mangoes are sweet.", "All mangoes are sweet.",
    ["mangoes", "sweet"],
    [("OAF", "mangoes", "sweet")],
    ("def", "S", "mangoes", "sweet"), ("def", "A", "mangoes", "sweet"), False, "I",
    "Only-a-few = Some + Some-not, so I follows. II is contradicted by the guaranteed non-sweet part. **Only I.**",
    "Split 'only a few' the moment you read it.",
    "easy", "syl-p13", 35),
 sq("definite-cases-p02", "Only a few books are novels.",
    "Some books are not novels.", "Some novels are books.",
    ["books", "novels"],
    [("OAF", "books", "novels")],
    ("def", "SN", "books", "novels"), ("def", "S", "novels", "books"), False, "both",
    "I is the guaranteed outside part → follows. II converts the Some half → follows. **Both.**",
    "Only-a-few gifts two conclusions: the split pair and its conversion.",
    "easy", "syl-p13", 40),
 sq("definite-cases-p03", "Only a few cups are plates. All plates are dishes.",
    "Some cups are dishes.", "Some cups are not dishes.",
    ["cups", "plates", "dishes"],
    [("OAF", "cups", "plates"), ("A", "plates", "dishes")],
    ("def", "S", "cups", "dishes"), ("def", "SN", "cups", "dishes"), False, "I",
    "The cup-that-is-a-plate is a dish → I follows. The non-plate cups may still be dishes → II fails. **Only I.**",
    "Only the B-side member chains through the All; the outside member stays free.",
    "medium", "syl-p14", 55),
 sq("definite-cases-p04", "All chairs are furniture. Only a few furniture items are costly.",
    "Some chairs are costly.", "All costly things being furniture is a possibility.",
    ["chairs", "furniture", "costly"],
    [("A", "chairs", "furniture"), ("OAF", "furniture", "costly")],
    ("def", "S", "chairs", "costly"), ("poss", "A", "costly", "chairs"), False, "II",
    "I: the furniture-costly overlap can sit outside chairs → fails. II: draw all costly things inside chairs (chairs inside furniture, some furniture outside) → consistent → follows. **Only II.**",
    "Only-a-few pins the split on ITS subject side only — everything else can be drawn freely.",
    "hard", "syl-p14", 70),
 sq("definite-cases-p05", "A few students are athletes. All athletes are fit.",
    "Some students are fit.", "All students are athletes.",
    ["students", "athletes", "fit"],
    [("S", "students", "athletes"), ("A", "athletes", "fit")],
    ("def", "S", "students", "fit"), ("def", "A", "students", "athletes"), False, "I",
    "'A few' = plain Some: the student-athlete is fit → I follows. II is the reverse-All trap. **Only I.**",
    "No guaranteed outside part with 'a few' — do not import only-a-few rules.",
    "medium", "syl-p15", 45),
 sq("definite-cases-p06", "Many Indian cities have metro rails.",
    "Some Indian cities have metro rails.", "All Indian cities have metro rails.",
    ["cities", "metro"],
    [("S", "cities", "metro")],
    ("def", "S", "cities", "metro"), ("def", "A", "cities", "metro"), False, "I",
    "'Many' = Some, so I follows. II overreaches — many is not all. **Only I.**",
    "Many / a few / some are one and the same in syllogisms.",
    "easy", "syl-p15", 35),
 sq("definite-cases-p07", "Only a few roads are wide. All wide roads are smooth.",
    "Some roads are smooth.", "All roads being smooth is a possibility.",
    ["roads", "wide", "smooth"],
    [("OAF", "roads", "wide"), ("A", "wide", "smooth")],
    ("def", "S", "roads", "smooth"), ("poss", "A", "roads", "smooth"), False, "both",
    "I: the road-that-is-wide is smooth → follows. II: draw all roads inside smooth (wide roads already are; non-wide roads join) → consistent → follows. **Both.**",
    "A possibility passes as long as no guaranteed member collides with it.",
    "hard", "syl-p16", 70),
 sq("definite-cases-p08", "Only a few workers are skilled.",
    "No worker is skilled.", "Some workers are skilled.",
    ["workers", "skilled"],
    [("OAF", "workers", "skilled")],
    ("def", "N", "workers", "skilled"), ("def", "S", "workers", "skilled"), False, "II",
    "Only-a-few asserts the overlap, so No is contradicted → I fails; II is its Some half → follows. **Only II.**",
    "'Only a few' never means 'none' — the overlap is asserted, not denied.",
    "medium", "syl-p16", 45),
 sq("definite-cases-p09", "Only a few flowers are fragrant.",
    "Some fragrant things are flowers.", "All fragrant things are flowers.",
    ["flowers", "fragrant"],
    [("OAF", "flowers", "fragrant")],
    ("def", "S", "fragrant", "flowers"), ("def", "A", "fragrant", "flowers"), False, "I",
    "I converts the Some half → follows. The fragrant class may spread far beyond flowers → II fails. **Only I.**",
    "The B-side is never fixed by only-a-few — no All, no Some-not on that side.",
    "medium", "syl-p13", 45),
 sq("definite-cases-p10", "Only a few keys are brass. All brass items are metal. No metal is plastic.",
    "Some keys are not plastic.", "All keys being plastic is a possibility.",
    ["keys", "brass", "metal", "plastic"],
    [("OAF", "keys", "brass"), ("A", "brass", "metal"), ("N", "metal", "plastic")],
    ("def", "SN", "keys", "plastic"), ("poss", "A", "keys", "plastic"), False, "I",
    "The key-that-is-brass is metal, hence never plastic — that key is 'a key not a plastic' → I follows. The same key blocks all keys inside plastic → II is impossible. **Only I.**",
    "Trace the only-a-few member through the All into the No — one journey settles both.",
    "hard", "syl-p16", 75),
]

upsert(d["practice"], new_idea + new_poss + new_eo + new_def)

# ---------------- re-verify EXISTING questions (report only) ----------------
EXIST = [
 ("rsn-syllogism-1", ["pens", "books", "copies"], [("A","pens","books"),("A","books","copies")],
  ("def","S","pens","copies"), ("def","S","copies","pens"), "both"),
 ("rsn-syllogism-2", ["dogs", "cats", "rats"], [("S","dogs","cats"),("A","cats","rats")],
  ("def","S","dogs","rats"), ("def","A","rats","dogs"), "I"),
 ("rsn-syllogism-3", ["glass", "metal", "solids"], [("N","glass","metal"),("S","metal","solids")],
  ("def","SN","solids","glass"), ("def","A","glass","solids"), "I"),
 ("rsn-syllogism-4", ["flowers", "red", "blue"], [("S","flowers","red"),("N","flowers","blue")],
  ("def","A","flowers","red"), ("def","SN","flowers","red"), "either"),
 ("rsn-syllogism-5", ["cars", "buses", "trucks"], [("A","cars","buses"),("S","trucks","buses")],
  ("def","S","cars","trucks"), ("def","N","cars","trucks"), "either"),
 ("rsn-syllogism-6", ["apples", "mangoes", "bananas"], [("S","apples","mangoes"),("N","mangoes","bananas")],
  ("poss","A","apples","bananas"), ("def","SN","apples","bananas"), "II"),
 ("rsn-syllogism-7", ["roads", "streets", "lanes"], [("A","roads","streets"),("S","streets","lanes")],
  ("poss","A","lanes","roads"), ("def","SN","lanes","streets"), "I"),
 ("rsn-syllogism-8", ["keys", "locks", "doors", "windows"],
  [("A","keys","locks"),("S","locks","doors"),("N","doors","windows")],
  ("def","S","keys","doors"), ("def","SN","locks","windows"), "II"),
 ("rsn-syllogism-9", ["cups", "plates", "bowls"], [("OAF","cups","plates"),("A","plates","bowls")],
  ("def","SN","cups","plates"), ("def","N","cups","bowls"), "I"),
 ("rsn-syllogism-10", ["chairs", "tables", "desks"], [("A","chairs","tables"),("S","tables","desks")],
  ("def","S","chairs","desks"), ("poss","A","desks","chairs"), "II"),
 ("rsn-syllogism-11", ["pages", "files", "folders"], [("S","pages","files"),("N","files","folders")],
  ("def","S","pages","folders"), ("poss","A","pages","files"), "II"),
 ("rsn-syllogism-12", ["rings", "circles", "squares", "triangles"],
  [("A","rings","circles"),("S","circles","squares"),("N","squares","triangles")],
  ("def","S","circles","triangles"), ("def","N","circles","triangles"), "either"),
 ("rsn-syllogism-13", ["numbers", "letters", "symbols", "digits"],
  [("S","numbers","letters"),("A","letters","symbols"),("N","symbols","digits")],
  ("def","SN","numbers","digits"), ("def","A","letters","digits"), "I"),
 ("rsn-syllogism-14", ["squares", "rectangles", "circles"], [("A","squares","rectangles"),("N","rectangles","circles")],
  ("def","N","squares","circles"), ("def","SN","circles","squares"), "both"),
 ("rsn-syllogism-15", ["villages", "towns", "cities"], [("A","villages","towns"),("OAF","towns","cities")],
  ("def","S","villages","cities"), ("poss","A","villages","cities"), "II"),
 ("rsn-syllogism-ex1", ["teachers", "graduates", "postgraduates"],
  [("A","teachers","graduates"),("S","graduates","postgraduates")],
  ("def","S","teachers","postgraduates"), ("def","A","graduates","teachers"), "neither"),
 ("rsn-syllogism-ex2", ["roses", "flowers", "plants"], [("A","roses","flowers"),("A","flowers","plants")],
  ("def","A","roses","plants"), ("def","S","plants","roses"), "both"),
 ("rsn-syllogism-ex3", ["mangoes", "sweet"], [("S","mangoes","sweet")],
  ("def","A","mangoes","sweet"), ("def","SN","mangoes","sweet"), "either"),
 ("rsn-syllogism-ex4", ["doors", "wooden", "brown"], [("A","doors","wooden"),("S","wooden","brown")],
  ("poss","A","doors","brown"), ("def","N","doors","brown"), "I"),
]
bad = []
for qid, terms, stmts, c1, c2, exp in EXIST:
    v = solve(terms, stmts, c1, c2)
    if v != exp:
        bad.append((qid, v, exp))
print("existing-question re-check:", "ALL MATCH" if not bad else f"MISMATCH {bad}")

# ---------------- pyqPatterns (rewrite richer) ----------------
d["pyqPatterns"] = [
 PYQ("Two-statement definite", "very common",
     "Two statements (an All and a Some/No in some order) with two conclusions about the outer terms.",
     "Draw the least-committal diagram, then hunt one counter-diagram per conclusion. The Some-member travels through an All; a No statement exiles it. Reject every conclusion a single moved diagram can break.",
     "syllogism-idea",
     "**Some dogs are cats. All cats are rats.** Conclusions: I. Some dogs are rats. II. All rats are dogs.",
     "The dog-cat member is a rat → I follows. Rats spread beyond dogs → II fails. **Only I.**"),
 PYQ("Three-statement chain", "common",
     "Three statements, usually two All's and one Some/No, with conclusions that need the whole chain.",
     "Chain the All-links first (A⊂B⊂C), place the Some/No member last, and trace the guaranteed member through every statement it meets before judging any conclusion.",
     "syllogism-idea",
     "**All keys are locks. Some locks are doors. No door is a window.** Conclusions: I. Some keys are doors. II. Some locks are not windows.",
     "The lock-door overlap can dodge keys → I fails. That door-lock is never a window → II follows. **Only II.**"),
 PYQ("Possibility conclusion", "very common",
     "Any conclusion ending in 'is a possibility'.",
     "Build ONE diagram where the possibility holds alongside every statement. It fails only when a guaranteed member would be forced into a forbidden (No) class. Definite and possibility use opposite standards — never mix them.",
     "possibility-cases",
     "**All roads are streets. Some streets are lanes.** Conclusion: All lanes being roads is a possibility.",
     "Draw lanes inside roads, roads inside streets, extra streets outside → consistent → **follows.**"),
 PYQ("Either-or complementary pair", "very common",
     "Neither conclusion follows alone but the pair is (All, Some-not) or (Some, No) about the same two terms.",
     "Check the shape first, then test each conclusion alone — if either follows by itself, pick it. Only a true negation pair with no individual proof earns 'Either I or II follows'.",
     "either-or",
     "**Some flowers are red. No flower is blue.** Conclusions: I. All flowers are red. II. Some flowers are not red.",
     "Neither is provable and the pair is exact negation → **Either I or II follows.**"),
 PYQ("Only-a-few statements", "common",
     "'Only a few A are B' — the modern quantifier.",
     "Rewrite as Some A are B + Some A are not B. The A-side split is guaranteed; the B-side is free. Chain only the overlap member through All statements; never chain the outside member.",
     "definite-cases",
     "**Only a few cups are plates. All plates are bowls.** Conclusions: I. Some cups are not plates. II. No cup is a bowl.",
     "I is guaranteed → follows. Plate-cups are bowls and non-plate cups may be bowls → II fails. **Only I.**"),
 PYQ("Conversion-based conclusion", "occasional",
     "The correct conclusion is a reversal: Some B are A from All A are B, or swapped Some/No.",
     "Recall the free conversions — All→Some, Some↔Some, No↔No — before rejecting a conclusion as 'reversed'. The only illegal reversal is All B are A.",
     "syllogism-idea",
     "**All roses are flowers.** Conclusion: Some flowers are roses.",
     "All→Some conversion always holds (no class is empty) → **follows.**"),
 PYQ("Counter-example hunt", "common",
     "A conclusion that looks natural but rests on drawing the picture you want.",
     "Ask of every conclusion: can I move a free part of the diagram — push an overlap aside, extend a circle — while all statements stay true? One success rejects it. Follows only when no movement can break it.",
     "syllogism-idea",
     "**Some spoons are forks.** Conclusion: Some spoons are not forks.",
     "Draw all spoons inside the overlap — statements hold, conclusion breaks → **does not follow.**"),
 PYQ("Possibility blocked by a No statement", "common",
     "A possibility question whose statements include 'No X is Y' near the possibility's terms.",
     "Trace the member guaranteed by a Some or only-a-few statement. If drawing the possibility would push that member into the forbidden class, the possibility is impossible; otherwise it follows.",
     "possibility-cases",
     "**Some phones are cameras. No camera is a charger.** Conclusion: All phones being chargers is a possibility.",
     "The phone-camera member can never be a charger → **does not follow.**"),
]

errs = finish("syllogism", d)
assert not errs, errs
