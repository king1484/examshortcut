"""Notes + patterns for the blood-relations topic (Phase 2 deep content)."""

NOTES = {}

NOTES["blood-relations-idea"] = """### What the topic really tests
Blood-relation questions never test your knowledge of families. They test whether you can turn spoken sentences into a small drawing without a single mistake. That drawing is called a **family tree**. Once the tree is correct, the answer is read off it in one line. Almost every wrong answer in this topic comes from a wrong tree, and a wrong tree almost always comes from one of two bad habits: assuming a gender that was never stated, or answering in the wrong direction.

### The symbols (use them every time)
Draw people as small boxes, one generation per row:
- **M** or a `+` sign beside a name for a male; **F** or `−` for a female.
- A **double line** (`=`) between a husband and wife.
- An **arrow pointing down** from parent to child.
- A **horizontal line** between brothers and sisters.
Elders go on the top rows, their children below them, grandchildren below that. Two people joined by marriage always sit on the same row.

### The three-step method
1. **Fix the genders first.** Read every word of the question and mark a gender only where a word gives it: father, brother, son, uncle, nephew, husband, grandfather → male; mother, sister, daughter, aunt, niece, wife, grandmother → female. Words like cousin, child, person give **no** gender. Leave those blank. Never guess.
2. **Turn each sentence into an arrow.** "Rita's son is Amit" becomes Rita → Amit (M). "Suresh is Meena's brother" puts both under the same parents' arrow. Do this one sentence at a time, in any order.
3. **Read the answer from the tree.** Find the two people named in the question, count the steps between them (each arrow is one generation), and write the relation in the direction the question asks.

### The direction rule (the biggest mark-saver)
"How is A related to B?" always means: **describe A from B's side** — A is B's ___. So start at B, walk the tree to A, and name what A is to B. If the question says "How is B related to A?", the same tree gives the opposite word: if A is B's grandmother, B is A's grandson. Practise reading both directions from one tree — the exam recycles the same tree with the question reversed.

### Generation counting
Each parent-child arrow is one generation:
- 1 arrow up = father/mother; 2 up = grandfather/grandmother; 3 up = great-grandfather/great-grandmother.
- 1 arrow down = son/daughter; 2 down = grandson/granddaughter; 3 down = great-grandson.
- Sideways (same parents) = brother/sister; sideways through a marriage = brother-in-law/sister-in-law.
- Parent's brother or sister = uncle/aunt. Uncle's or aunt's child = **cousin**, never nephew.
- Sibling's child = nephew (boy) or niece (girl).

### "Only" words
- **Only child** = the person has no brother and no sister.
- **Only son** = no other boys; there may still be daughters.
- **Only daughter** = no other girls; there may still be sons.
These three lines solve a large share of the tricky questions, so read the exact word — son, daughter or child — before drawing.

### Quick revision
- Draw the tree; never hold a chain in your head.
- Mark a gender only when a word states it. Blank means "leave blank".
- "How is A related to B?" = name A from B's side.
- Each arrow = one generation: 1 up father, 2 up grandfather, 1 down son, 2 down grandson.
- Parent's sibling = uncle/aunt; their child = cousin; sibling's child = nephew/niece.
- Only child ≠ only son ≠ only daughter — read the exact word."""

NOTES["family-tree-puzzles"] = """### What these questions look like
You get three to six sentences about one family, then a question: "How is X related to Y?", "How many males are there?", or "Who is the grandfather of Z?" The sentences are deliberately **shuffled** — the wife is mentioned before the husband, the grandfather after the grandchild. Reading them in the given order and answering from memory is exactly how marks are lost. The sentences are raw material; you must build the tree, then answer.

### Top-down reconstruction
Start with the **oldest** person — the one who is nobody's child in the whole set. Place them at the top. Then attach everyone else:
1. Hang the named children below their parent.
2. Join husbands and wives with `=` on the same row.
3. Repeat until every name in the question sits on the tree.
A tree built this way never needs revising, because each sentence fits an empty slot instead of fighting the earlier ones.

### Reading relations from the finished tree
- Find both people. The relation is the **shortest path** between them.
- Going up through A's parent to B: B is a grandparent. Going down through A's child to B: B is a grandchild.
- Crossing a marriage line adds "**-in-law**": spouse's mother = mother-in-law, sibling's spouse or spouse's sibling = brother/sister-in-law, child's spouse = son/daughter-in-law.
- Two people whose parents are brothers/sisters are **cousins** — one generation apart, joined sideways, not up or down.

### Counting questions
"How many males/females?" and "How many members?" are read straight off the tree, tick by tick:
1. Write +/− beside every name while drawing, only where a sentence fixes the gender.
2. Count the ticks for the asked gender. Blank-gender names are **not** counted — and if the question forces a total, the blanks are the trap.
3. Grandparents' generation, married-in wives/husbands, and children all count. A person who is only named as "X's spouse" counts too.

### Chain questions
Some puzzles shrink to two or three sentences: "Mohan is Rekha's father. Ramesh is Mohan's father. How is Ramesh related to Rekha?" Even here, draw the two arrows. Then simply count: two arrows up from Rekha = grandparent level; Ramesh is male = **grandfather**. Three arrows down from someone = great-grandchild. The arrow count fixes the relation family, the gender fixes the exact word.

### Quick revision
- Rebuild top-down: oldest at the top, children below, marriages on the same row.
- Shortest path on the tree = the relation.
- Every marriage crossing adds "-in-law".
- Aunt's/uncle's child = cousin; sibling's child = nephew/niece.
- Counting: tick genders while drawing; never count a name whose gender stayed blank.
- Chains: count arrows for generations, then apply gender."""

NOTES["pointing-introduction"] = """### What these questions look like
"Pointing to a man, Rita said, 'He is the only son of my mother's mother's only child.' How is the man related to Rita?" — the whole tree is hidden inside **one spoken phrase**. The speaker is always part of the family, and the photo person is described through a chain of "my ___'s ___" links. Decode the chain, place the two people, and read the relation.

### Peel the phrase inside-out
Work from the **innermost** "my ___" outward, one layer per line of rough work:
1. Replace "my" with the speaker's name. "My mother's mother" → Rita's mother's mother = Rita's maternal grandmother.
2. Apply each next "'s ___" to what you have. "...'s only child" → that grandmother's single child = Rita's mother.
3. Continue: "the only son of (Rita's mother)" → Rita's brother.
4. Answer: the man is Rita's **brother**.
Writing one line per layer takes twenty seconds and prevents the classic error of collapsing two links into one.

### The self-reference alarm
Some phrases fold back onto the speaker:
- "My mother's **only child**" = the speaker (no one else exists).
- "My father's **only son**" = the speaker, **if the speaker is male**; if the speaker is female, it is her brother.
- "My mother's **only daughter**" = the speaker, if female; her sister, if male.
Whenever one of these appears, test it first. The question is then really about the speaker's own son, daughter, brother or sister. For example, "He is the son of my father's only son", said by a man, means "He is **my son**".

### Gender and "cannot be determined"
- A phrase fixes a gender only through a gendered word. "My mother's husband" is male; "my father's child" may be anyone.
- If the final relation depends on a gender or a sibling count the phrase never fixes, the answer is **"Cannot be determined"** — a real option in this format, not a trap. Example: "the man is the son of one of my grandfather's sons" — he could be the speaker's brother (son of the speaker's father) or a cousin (son of an uncle). Both readings fit, so no single relation is certain.
- Watch for the reverse direction: "How is the speaker related to the person shown?" needs the opposite word of what the phrase gives.

### The standard word bank
Photograph questions reuse the same blocks: grandfather's only son = father; mother's only child = the speaker; father's sister = aunt; aunt's daughter = cousin; brother's niece = the speaker's own daughter (when the speaker is the only sister); father's only brother = uncle. Learn these decodings once — the exam just re-orders them.

### Quick revision
- Decode inside-out: replace "my" first, one "'s ___" per line.
- Test the self-reference ("my mother's only child" = speaker) before anything else.
- Only son bars boys only; only daughter bars girls only.
- If a needed gender/sibling fact is missing, the answer is "Cannot be determined".
- Read the question's direction: person-to-speaker, or speaker-to-person.
- Memorise the blocks: grandfather's only son = father; aunt's daughter = cousin; brother's niece = your daughter."""

NOTES["coded-relations"] = """### What these questions look like
The exam defines private symbols and hands you a coded string: "'P + Q' means P is the father of Q; 'P × Q' means P is the sister of Q. In 'A + B × C', how is A related to C?" No tree exists yet — you build one from the string. This is the Tier-2 favourite because one well-made string can ask any relation in it.

### Decode pairwise, never as a whole
Break the string into symbol-sized sentences, left to right:
1. `A + B` → "A is the father of B."
2. `B × C` → "B is the sister of C."
Now draw: A above B; B and C share the same parents (sisters do), so A sits above C as well. Read the asked pair: A is C's **father**. Two operators ≈ three people; three operators ≈ four people. A four-person string like `A + B − C × D` is the same loop one more time.

### The gender bookkeeping
Each symbol fixes the gender of its **first** person only: father/son/brother/husband/uncle → the first person is male; mother/daughter/sister/wife/aunt → female. "Sibling/cousin/child of" symbols fix nothing. So:
- In `A + B × C`, A's gender is fixed by "+" (male), B's by "×" (female), C's by **nothing**.
- If the asked relation needs a gender nobody fixed, the answer must be the neutral word ("sibling", "cousin", "parent") or "cannot be determined".
Mark +/− under each letter as you decode. The final answer usually turns on exactly one of these marks.

### Reading the pair direction
"How is A related to C?" = name A from C's side. Decode `A + B` as "A is the father of B", but if the question asks "How is B related to A?", the same symbol gives **son** (or daughter, if B's gender shows female elsewhere). Symbols read left-to-right, questions read either way — always answer the question's direction, not the string's.

### Strings where a person appears twice
Longer expressions reuse letters: `A + B + C` means A is the father of B and B is the father of C, so A is C's **grandfather**. Chains of the same symbol add generations; chains of different symbols mix a generation step with a sideways step. Draw the tree — do not try to feel the answer.

### Quick revision
- Decode one symbol at a time; each symbol = one sentence = one tree link.
- A symbol fixes the first person's gender only; blanks stay blank.
- Parent of one sibling is parent of all siblings.
- Same symbol twice = +1 generation (father → grandfather).
- Answer in the question's direction; use neutral words for blank genders.
- Check the tree before marking: no person can be their own ancestor."""

PATTERNS = {}

PATTERNS["blood-relations-idea"] = [
    {
        "id": "br-p1",
        "name": "Direction of the asked relation (A to B vs B to A)",
        "frequency": "very common",
        "howToSpot": "'How is A related to B?' or 'How is B related to A?' over a one or two-line family statement.",
        "formula": None,
        "logic": "1. Draw the one or two arrows the statement gives.\n2. Start from the person named AFTER 'related to' — that is your viewpoint.\n3. Walk to the other person and name what they are from this side.\n\n*Why it works:* the same tree gives opposite words in opposite directions; fixing the viewpoint first removes the most common error in the topic.",
        "example": {"q": "**Sunita is the mother of Deepak. How is Deepak related to Sunita?**",
                    "solution": "Arrow: Sunita → Deepak. Viewpoint is Sunita; Deepak sits one arrow down and is male → Deepak is her **son**."},
    },
    {
        "id": "br-p2",
        "name": "Gender-pinned and cannot-be-determined cases",
        "frequency": "common",
        "howToSpot": "The options include 'Cannot be determined', or the chain ends in a word (cousin, child, sibling) that fixes no gender.",
        "formula": None,
        "logic": "1. Mark a gender only for people with gendered words (father, sister, wife...).\n2. Check whether the asked relation needs a blank gender.\n3. If it does, answer the neutral word or 'Cannot be determined'; if not, read the tree.\n\n*Why it works:* every wrong gender in your tree produces a wrong option that looks perfectly logical — blanks are safer than guesses.",
        "example": {"q": "**A and B are siblings. C is A's mother. How is B related to C?**",
                    "solution": "A and B share the parent C → B is C's child. B's gender is never stated → **son or daughter — cannot be determined** (accept the neutral 'child' if offered)."},
    },
    {
        "id": "br-p3",
        "name": "Single-link chains (parent/child/sibling pairs)",
        "frequency": "very common",
        "howToSpot": "Two short sentences, each naming one link, e.g. 'R is the father of S. T is the sister of S.'",
        "formula": None,
        "logic": "1. Draw one arrow per sentence (parent → child; siblings on one row).\n2. Merge: people under the same arrow are siblings.\n3. Read the two-person path asked in the question.\n\n*Why it works:* two links already fix a three-person tree; the answer is the one path between the named pair.",
        "example": {"q": "**R is the father of S. T is the sister of S. How is T related to R?**",
                    "solution": "R → S and T is S's sister, so R → T as well. T is one arrow down from R and female → R's **daughter**."},
    },
    {
        "id": "br-p4",
        "name": "How many members (family-count arithmetic)",
        "frequency": "common",
        "howToSpot": "'How many members/daughters/sons are there in the family?' after a short family description.",
        "formula": None,
        "logic": "1. Draw the family exactly as described — one box per person, including spouses.\n2. Count the asked group by ticking boxes (do not forget a named wife or husband).\n3. Re-read for words like 'only', 'each', 'at least' that change the count.\n\n*Why it works:* counting from a drawing never double-counts; counting from memory usually does.",
        "example": {"q": "**A couple has 3 sons, and each son has 2 daughters. How many female members are in the family?**",
                    "solution": "Wife (1) + 3 × 2 = 6 granddaughters = **7** female members. (The sons and the father are male and are not counted.)"},
    },
]

PATTERNS["family-tree-puzzles"] = [
    {
        "id": "br-p5",
        "name": "Chain relations across generations",
        "frequency": "very common",
        "howToSpot": "Sentences like 'A's son is B, B's daughter is C' — each sentence hangs one person below the last.",
        "formula": None,
        "logic": "1. Draw the chain top-down, one arrow per sentence.\n2. Count arrows between the asked pair: 1 = parent/child, 2 = grandparent/grandchild, 3 = great-grandparent.\n3. Fix the exact word with the gender.\n\n*Why it works:* generation distance and gender are the only two facts a relation needs; the chain gives both by counting.",
        "example": {"q": "**Ramesh is the father of Vinod. Vinod is the father of Anita. How is Ramesh related to Anita?**",
                    "solution": "Ramesh → Vinod → Anita: two arrows up from Anita, male → **grandfather**."},
    },
    {
        "id": "br-p6",
        "name": "In-law relations",
        "frequency": "very common",
        "howToSpot": "A wife/husband appears, and the asked pair are not blood relatives (spouse's parent, sibling's spouse, child's spouse).",
        "formula": None,
        "logic": "1. Draw the marriage with `=` on one row.\n2. Apply the in-law map: spouse's parent = mother/father-in-law; sibling's spouse or spouse's sibling = brother/sister-in-law; child's spouse = son/daughter-in-law.\n3. If two marriages chain (spouse of spouse's sibling), take one crossing at a time.\n\n*Why it works:* every '-in-law' word is exactly one marriage crossing away from a plain blood relation.",
        "example": {"q": "**Sneha is the wife of Rita's son Amit. How is Sneha related to Rita?**",
                    "solution": "Sneha married Rita's child → one marriage crossing from 'daughter' → **daughter-in-law**."},
    },
    {
        "id": "br-p7",
        "name": "Counting males and females in a full tree",
        "frequency": "common",
        "howToSpot": "A multi-sentence tree plus 'How many male/female members are there?'",
        "formula": None,
        "logic": "1. Draw the full tree; write +/− beside each name only where a word fixes it.\n2. Count ticks for the asked gender — including married-in spouses.\n3. Leave blank-gender names out, and re-read 'only' statements before finalising.\n\n*Why it works:* ticking while drawing turns a memory test into a five-second count.",
        "example": {"q": "**Mr. and Mrs. Rao have two sons. The elder son's wife and their two daughters live with them. How many females?**",
                    "solution": "Mrs. Rao + daughter-in-law + 2 granddaughters = **4** females (the husband and the two sons are male)."},
    },
    {
        "id": "br-p8",
        "name": "Shuffled multi-statement reconstruction",
        "frequency": "very common",
        "howToSpot": "Four to six sentences in a jumbled order describing one family, then 'How is X related to Y?'",
        "formula": None,
        "logic": "1. Find the person nobody calls a child — the tree root.\n2. Attach children, then marriages, until every name sits on the tree.\n3. Answer from the shortest path between the asked pair.\n\n*Why it works:* statements given out of order still describe one tree; rebuilding top-down makes each statement fit one empty slot.",
        "example": {"q": "**Anil is the brother of Sunil. Sunil is the father of Mohan. Ritu is the daughter of Kavita. Mohan is the brother of Ritu. How is Kavita related to Anil?**",
                    "solution": "Mohan and Ritu share parents; Ritu's mother is Kavita, so Sunil's wife is Kavita. Wife of Anil's brother → **sister-in-law**."},
    },
    {
        "id": "br-p9",
        "name": "Cousin relations across two branches",
        "frequency": "common",
        "howToSpot": "One family splits into two married children; the asked pair come from different branches.",
        "formula": None,
        "logic": "1. Place the common grandparents at the top; hang the two siblings below them.\n2. Hang each sibling's children on their own branch.\n3. The two children of the siblings are cousins — whatever their genders.\n\n*Why it works:* cousins are children of siblings; no other path connects two branches.",
        "example": {"q": "**Rahul's mother's brother is Vikas. Vikas's daughter is Neha. How is Neha related to Rahul?**",
                    "solution": "Vikas is a sibling of Rahul's mother; Neha is Vikas's child. Children of siblings → **cousin**."},
    },
]

PATTERNS["pointing-introduction"] = [
    {
        "id": "br-p10",
        "name": "Long pointing phrase decoded inside-out",
        "frequency": "very common",
        "howToSpot": "'Pointing to X, Y said, \"He/She is the ___ of my ___'s ___\"' — a chain of two or more possessives.",
        "formula": None,
        "logic": "1. Replace 'my' with the speaker's name.\n2. Resolve the innermost 'my ___' first, then apply one possessive link at a time, one line per layer.\n3. Read the final relation of the photo person to the speaker.\n\n*Why it works:* each layer is one small tree link; layers solved in order cannot tangle.",
        "example": {"q": "**Pointing to a woman, Mohan said, 'She is the wife of my father's only brother.' How is she related to Mohan?**",
                    "solution": "Father's only brother = Mohan's uncle. Wife of uncle = **aunt**."},
    },
    {
        "id": "br-p11",
        "name": "Self-reference trap (phrase resolves to the speaker)",
        "frequency": "common",
        "howToSpot": "Phrases like 'my mother's only child', 'my father's only son', or 'my mother's only daughter'.",
        "formula": None,
        "logic": "1. Test the self-reference first: 'my mother's only child' = the speaker.\n2. For 'only son/daughter', check the speaker's gender — it is the speaker if the gender fits, else a sibling.\n3. Re-read the sentence with the collapse done; the question is about the speaker's own child, sibling or spouse.\n\n*Why it works:* the setter hides the simplest tree (speaker + one more person) inside a long phrase.",
        "example": {"q": "**Pointing to a boy, Suresh said, 'He is the son of my father's only son.' How is the boy related to Suresh?**",
                    "solution": "Suresh is male, so his father's only son = Suresh himself. The boy is Suresh's **son**."},
    },
    {
        "id": "br-p12",
        "name": "Cannot-be-determined photo questions",
        "frequency": "common",
        "howToSpot": "The phrase mentions a set that is not pinned down — 'one of my uncle's sons', 'daughter of my grandfather's only child' — and 'Cannot be determined' sits in the options.",
        "formula": None,
        "logic": "1. Decode the phrase and list every person who could match.\n2. Check whether the speaker's own gender or a sibling count removes any of them.\n3. If two different relations remain possible, answer 'Cannot be determined'.\n\n*Why it works:* the format genuinely allows under-specified phrases; choosing a single relation when two fit is the planted error.",
        "example": {"q": "**Pointing to a man, Meena said, 'His wife is the daughter of my grandfather's only child.' How is the man related to Meena?**",
                    "solution": "Grandfather's only child = Meena's mother. Her daughters: Meena or a sister. The man is Meena's husband **or** her brother-in-law → **cannot be determined**."},
    },
    {
        "id": "br-p13",
        "name": "Reversed pointing (speaker's relation to the person shown)",
        "frequency": "common",
        "howToSpot": "'How is the speaker related to the person in the photograph?' — the reverse of the usual question.",
        "formula": None,
        "logic": "1. Decode the phrase exactly as usual.\n2. Note which direction the question wants: speaker-to-photo, not photo-to-speaker.\n3. Give the mirror word (brother ↔ sister, father ↔ son, aunt ↔ niece).\n\n*Why it works:* the phrase fixes one relation; the question just asks it from the other end.",
        "example": {"q": "**Pointing to a man, Priya said, 'He is the son of my grandfather's only son.' How is Priya related to the man?**",
                    "solution": "Grandfather's only son = Priya's father, so the man is her brother. Asked in reverse: Priya is his **sister**."},
    },
]

PATTERNS["coded-relations"] = [
    {
        "id": "br-p14",
        "name": "Three-person decode (two symbols)",
        "frequency": "very common",
        "howToSpot": "Two symbol definitions and a string like 'A + B × C'; one pair's relation is asked.",
        "formula": None,
        "logic": "1. Translate each symbol into a plain sentence.\n2. Draw the mini-tree: shared parents for siblings, marriage on one row.\n3. Read the asked pair from the tree, watching which genders the symbols fixed.\n\n*Why it works:* two sentences already form a connected tree; the answer is one path on it.",
        "example": {"q": "'**P + Q**' means P is the brother of Q; '**P × Q**' means P is the wife of Q. In '**A + B × C**', how is A related to C?",
                    "solution": "A is B's brother; B is C's wife. Husband's brother → A is C's **brother-in-law**."},
    },
    {
        "id": "br-p15",
        "name": "Four-person string (three symbols)",
        "frequency": "common",
        "howToSpot": "Three symbol definitions; the string has three operators, e.g. 'A + B − C × D'.",
        "formula": None,
        "logic": "1. Decode symbol by symbol, left to right, drawing as you go.\n2. Each operator adds one person; link siblings under shared parents.\n3. Answer the asked pair; a gender no symbol fixed means a neutral word.\n\n*Why it works:* the string is just three sentences; three small links beat one long guess.",
        "example": {"q": "'**P + Q**' = P is the son of Q; '**P − Q**' = P is the wife of Q; '**P × Q**' = P is the brother of Q. In '**A + B − C × D**', how is A related to D?",
                    "solution": "A is B's son; B is C's wife → C is A's father; C is D's brother → A is D's **nephew** (A is male)."},
    },
    {
        "id": "br-p16",
        "name": "Reverse-direction ask in coded strings",
        "frequency": "common",
        "howToSpot": "The question asks 'How is C related to A?' while the string runs A ... B ... C.",
        "formula": None,
        "logic": "1. Decode and draw exactly as usual — do not reverse the string.\n2. Take the viewpoint the question names (C's side).\n3. Give the mirror word of what the path shows.\n\n*Why it works:* the tree is direction-free; only the final sentence must match the question's direction.",
        "example": {"q": "'**X # Y**' means X is the father of Y; '**X @ Y**' means X is the sister of Y. In '**A # B @ C**', how is C related to A?",
                    "solution": "A is B's father; B is C's sister → A is C's father too. Asked from C's side: C is A's **son or daughter** — C's gender is never fixed → 'cannot be determined' unless a neutral option exists."},
    },
    {
        "id": "br-p17",
        "name": "Build the expression for a given relation",
        "frequency": "occasional",
        "howToSpot": "'Which expression means M is the maternal uncle of K?' — options are strings, not words.",
        "formula": None,
        "logic": "1. Write the target as plain sentences ('M is the brother of K's mother').\n2. Pick symbols that state exactly those sentences, middle person included.\n3. Check every option symbol by symbol; reject any that changes a gender or a generation.\n\n*Why it works:* each option is one claimed tree; the correct one must reproduce the target sentences exactly.",
        "example": {"q": "'**P + Q**' = P is the brother of Q; '**P − Q**' = P is the mother of Q. Which expression means '**M is the maternal uncle of K**'?",
                    "solution": "Need: M is the brother of K's mother. 'M + L − K' says M is L's brother and L is K's mother ✓ → **M + L − K**."},
    },
]
