"""Dictionary-order topic: NOTES + PATTERNS (imported by dictionary-order.py)."""
import os
import sys

sys.path.insert(0, os.path.dirname(__file__))
from _lib import P  # noqa

NOTES = {}

NOTES["dict-idea"] = """### One rule runs the whole topic

A real dictionary sorts words letter by letter from the left, and so does every question in this topic. At the **first position where two words differ**, the word with the **earlier letter** comes first. That single rule answers every arrangement question — the skill is applying it without getting lost.

**The comparison algorithm.** To order any group of words:
1. Compare the first letters. Words sort into groups by their first letter: all A-words before all B-words, and so on.
2. Inside a group, compare the second letters; then the third; keep going until the words separate.
3. If one word runs out of letters while matching the other word letter for letter (Cart vs Carton), the **shorter word comes first** — it is a prefix of the longer one.

Work with paper, not memory: stack the words vertically so the columns line up, then scan column by column. The first column that is not identical splits the group into sub-groups; recurse inside each sub-group.

**Two classic traps.**
- *The later-letter trap:* early matches lull you into relaxing. Scant, Scan, Scandal all share S-C-A-N; the decision hides at the fifth letter (t vs nothing vs d). Stay letter-by-letter to the very end.
- *The prefix trap:* a shorter word that matches a longer one's start always comes **before** it — Scan before Scant, Play before Player. Options routinely offer the reverse because it 'feels' longer-word-first.

**Words with same letters, different order.** Angel vs Angle: identical multiset of letters, but the third letter (e vs n) splits them — Angel first. The rule never changes: first differing position, earlier letter wins.

**Reading the question direction.** "Which comes first / last", "which is third", "which pair is adjacent", "which comes just after X" — all four are the same sort followed by a different lookup. Do the full sort once, number the slots 1-2-3-4-5, and answer any of these variants from the numbered list.

### Quick revision
- Sort letter by letter from the left; the first differing letter decides.
- A shorter word that is a prefix of a longer one comes first (Scan → Scant → Scandal).
- Stack words vertically and scan columns — never juggle in your head.
- Same letters, different order: the first differing position still decides (Angel before Angle).
- Sort once, number the slots, then answer 'first / last / third / adjacent' from the list.

**Where marks are actually lost.** Almost never in the rule — always in execution: a misread letter pair (m/n, r/s), a forgotten prefix, or answering 'first' when the question asked 'last'. The numbered-line habit kills all three: order on paper, read the slot, and reread the question's direction word (first / last / second / middle) before marking."""

NOTES["arrange-words"] = """### The standard 4-6 word arrangement

This is the topic's workhorse: a list of 4-6 similar words, and one lookup — "which comes third", "which is last", "which comes just after X", "which is second from the right". The method never changes; only the lookup does.

**Step 1 — group by the shared stem.** Exam words almost always share a long prefix (Stat-, Colon-, Dec-). Find the stem and draw it once; only the letters **after** the stem matter. Statue, Status, Statute, Stature, Station all share STAT — the fight starts at the fifth letter.

**Step 2 — split at the first difference.** Line up the words, ignore the common stem, and look at the next letter of each. Sort by those letters. Ties inside a letter move one position deeper. In the STAT family: Station (i) separates immediately; Statue/Status/Statute/Stature all show E/S/E/R at position six, then sort by the seventh where needed.

**Step 3 — apply the prefix rule inside ties.** When one word is a stem-with-nothing (Colon inside Colonial... but also Decamp family: Decay vs December), remember: exact prefix sorts before its extensions; among extensions, the next letter decides.

**Step 4 — number and read.** Write the final order as a numbered line, 1 to N, then answer whatever was asked:
- "Third word" → slot 3.
- "Second from the right" → slot N−1.
- "Just after X" → slot of X plus one.
- "Adjacent pair" → two words whose slot numbers differ by exactly 1.

**Speed practice pays twice.** These questions are pure procedure — the same 30-second routine solves every one. Errors come almost only from mis-comparing one letter pair (mixing up m/n order, reading r before s) or from mis-counting slots ('second from right' vs 'second'). Both are prevented by the numbered line: letters decide the order, numbers decide the answer.

**Check with extremes.** Before locking an answer, confirm the obvious: the word with the alphabetically earliest deep letter should sit near the left end, the latest near the right end. If your final order violates that instinct, re-scan column two — a transposed pair is the usual cause.

### Quick revision
- Strip the shared stem; the battle starts at the first letter after it.
- Prefix (bare stem) sorts before any extension of itself.
- Write the full numbered order, then read the requested slot off it.
- 'Second from the right' = slot N−1; 'just after X' = X's slot + 1.
- Sanity-check: earliest deciding letter at the left end, latest at the right.

**Time target.** A practiced 5-word arrangement takes 30-40 seconds: 5 for the stem, 15 for the column scan, 10 for the numbered line, 5 for the lookup. If you are past a minute, you are re-sorting in your head — restart on paper; it is faster than a third mental pass."""

NOTES["letter-position"] = """### Positions, mirrors and letter arithmetic

These questions treat the alphabet as a numbered strip of 26 tiles and ask who stands where. Three tools cover everything.

**Tool 1 — absolute positions (EJOTY).** Memorise five anchors: **E=5, J=10, O=15, T=20, Y=25**. Every other position is a small step from an anchor: G = J − 3 = 7; R = T − 2 = 18; W = Y + 2 = 23. With anchors, "which is the 15th letter" is instant (O), and "how many letters between G and S" is 19 − 7 − 1 = 11 (subtract positions, minus one — the letters *between* exclude both ends).

**Tool 2 — the mirror (from the right).** The letter that is k-th from the **right** stands at position $27 - k$ from the left (and vice versa: position p from the left is $27 - p$ from the right). So the 9th from the right = $27 - 9 = 18$th from the left = R; and T (20th from left) is $27 - 20 = 7$th from the right. The number 27 is the whole trick: 26 letters plus one.

**Tool 3 — letter arithmetic.** "4th to the right of the 12th from the left": convert every clause to a from-the-left position, then add or subtract on the strip. From-the-left + right-steps = add; left-steps = subtract. When a clause says "from the right", convert first ($27-k$), then do the arithmetic:
- 4th right of 12th from left → $12 + 4 = 16$ → P.
- 6th left of 8th from right → $27 - 8 = 19$, then $19 - 6 = 13$ → M.

Watch the two directions: 'to the right of' adds toward Z; 'to the left of' subtracts toward A — because the strip is drawn left = A … right = Z.

**Tool 4 — modified alphabets.** Variants rewrite the strip first, then ask a position:
- *Full reverse:* Z first … A last; position p in the reverse strip = letter $27 - p$ of the normal strip.
- *Half reverse:* first half A-M written backwards, second half normal (or Z-N backwards). Write the new 26-letter strip once, then answer by counting — never by juggling formulas.

**Check every answer by touch.** Confirm with anchors: position 16 must be near T (20) — 4 steps before T is P ✓. If your letter lands more than 5 away from the predicted anchor, recount; that five-second habit catches nearly every off-by-one.

### Quick revision
- EJOTY anchors: E=5, J=10, O=15, T=20, Y=25; step from them, never from A.
- Between G and S: $19-7-1=11$; 'between' excludes both ends.
- Mirror: k-th from right $= 27-k$ from left (and the reverse).
- Multi-clause: convert everything to from-the-left, then add (right) or subtract (left).
- Modified strip: write it out once, then count on paper.

**Off-by-one defence.** Every wrong answer in this subtopic is off by exactly one step: counting the end letter in 'between', forgetting the +1 in the mirror (27, not 26), or stepping the wrong way after 'to the left of'. Anchor-verify the final letter (it must sit within 5 of the predicted anchor) and both errors disappear."""

NOTES["word-formation"] = """### Rank of a word, and other letter-bag questions

Two families live here. Both are procedures — learn the steps once and every instance falls.

**Family 1 — dictionary rank of a word.** "The letters of PRIME are arranged in all possible ways as in a dictionary; what is the rank of PRIME?" The rank counts how many arrangements come **before** the word, plus one. Procedure:
1. Write the word's letters in alphabetical order (E, I, M, P, R for PRIME).
2. Scan the word left to right. At each position, count how many *unused* letters are **smaller** than the current letter. Each smaller letter would start a block of arrangements: add (count) × (arrangements of the remaining letters).
3. 'Arrangements of the remaining letters' = factorial of how many letters are left — divided by the factorials of any repeated-letter counts (a word with two E's has half as many distinct arrangements).
4. Fix the current letter as used and move right. The final total + 1 is the rank.

Example skeleton for PRIME: P is 4th smallest of {E,I,M,P,R} → 3 × 4! before it; then R is 4th of {E,I,M,R} → 3 × 3!; then I is 2nd of {E,I,M} → 1 × 2!; then M is 2nd of {E,M} → 1 × 1!; E is 1st → 0. Rank = 72 + 18 + 2 + 1 + 1 = 94.

**Family 2 — alphabetised spellings.** "If the letters of TABLE are rearranged in alphabetical order, how many letters keep their position?" Write the word, write its letters sorted (A B E L T), and compare column by column. Only exact matches count. TABLE: only L (position 4) matches → one letter.

**Family 3 — form the word from the letters.** "Which word can be formed from the letters of CONVERSATION?" Check each option letter by letter against the bag: cross off a bag letter for every use. Two details decide these: **repeats** (the bag has two O's and two N's — using three O's fails) and **missing letters** (one absent letter kills the option). Scan for the rarest letter in each option first; that fails or passes fastest.

**Family 4 — neighbours in the arrangement list.** "All arrangements of BAT in dictionary order — which is 4th?" The list is short: write it out (ABT, ATB, BAT, BTA, TAB, TBA) and count. For 3 distinct letters the whole list is 6 words; writing it beats any formula.

### Quick revision
- Rank = count smaller-letter blocks position by position + 1; divide by repeat factorials.
- Alphabetise-and-compare: only exact same-position letters count.
- Word-formation: cross off bag letters; watch double letters and one missing letter.
- 3-letter words: write all 6 arrangements and count slots.
- Sanity: the rank must not exceed n! (7! = 5040 for a 7-letter word)."""

PATTERNS = {}

PATTERNS["dict-idea"] = [
    P("dc-p1", "First differing letter decides", "very common",
        "Two or three words sharing an opening; the question asks which comes first or last.",
        "1. Scan letter by letter to the first position where the words differ.\n2. The earlier letter at that position wins the earlier slot.\n3. Ignore how long the shared part is — only the first difference matters.\n\n*Why it works:* dictionary order is exactly lexicographic order on the left-most difference.",
        "**Which comes first in the dictionary: Market, Margin or Marble?**",
        "All share MAR; 4th letters k / g / b → b earliest → **Marble** comes first.", None),
    P("dc-p2", "Shorter prefix sorts first", "common",
        "One word is exactly the start of another (Sand, Sandwich) — a prefix pair.",
        "1. If word A matches word B letter for letter and A has no letters left, A is B's prefix.\n2. The prefix comes **before** the longer word.\n3. Among several extensions, compare the letter right after the stem.\n\n*Why it works:* a dictionary cannot fit anything between a word and itself, so the short form lists first.",
        "**Which of these comes first: Sand, Sandy, Sandwich or Sandal?**",
        "Sand is a prefix of the other three → **Sand** comes first.", None),
    P("dc-p3", "Deep ties beyond the third letter", "common",
        "4-6 words sharing a long stem where the decision hides at the 4th-6th letter.",
        "1. Strip the common stem and write only the tails.\n2. Sort tails letter by letter; the earliest tail letter takes the earliest slot.\n3. Prefix tails (empty tail) sort first inside their group.\n\n*Why it works:* the comparison rule does not care how deep the difference hides.",
        "**Arrange Sure, Surge, Surgeon, Surplus, Surreal. Which comes third?**",
        "4th letters: e / g / g / p / r → Sure, Surge, Surgeon, Surplus, Surreal → third = **Surgeon**.", None),
    P("dc-p4", "Slot lookups: middle and adjacent pairs", "common",
        "After sorting, the question asks for the middle word or an adjacent pair rather than first/last.",
        "1. Produce the full numbered order first — never answer adjacent questions by instinct.\n2. Middle of 5 words = slot 3; of 4 words, slots 2 and 3 share the middle.\n3. Adjacent = slot numbers differing by exactly 1.\n\n*Why it works:* every lookup variant reads off the same sorted list.",
        "**Arrange Melon, Melody, Mellow, Member. Which two are adjacent in the dictionary?**",
        "4th letters: b / l / l / o → Member, Mellow, Melody, Melon. Adjacent pair: **Melon and Melody**.", None),
]

PATTERNS["arrange-words"] = [
    P("aw-p1", "Arrange and pick the slot", "very common",
        "4-6 words; 'which is the Nth word in dictionary order' (from the left).",
        "1. Strip the shared stem; sort by the first differing tail letter.\n2. Write the numbered order 1..N.\n3. Read slot N and check it against the extreme words.\n\n*Why it works:* one sort, then a positional lookup.",
        "**Arrange Chalk, Charm, Chart, Chase, Chatter. Which is the fourth word?**",
        "4th letters: l / r / r / s / t → Chalk, Charm, Chart, Chase, Chatter → fourth = **Chase**.", None),
    P("aw-p2", "Prefix vs later-letter battle", "very common",
        "The list mixes a bare stem with extensions that fight over a later letter.",
        "1. The bare stem sorts before all extensions.\n2. Extensions sort by the letter right after the stem; ties go one letter deeper.\n3. Re-scan the deciding column twice — one misread flips two slots.\n\n*Why it works:* first difference decides, at whatever depth it hides.",
        "**Arrange Mystery, Mystic, Myself, Myopia. Which comes first?**",
        "3rd letters: s / s / s / o → Myopia first; among the s-words, 4th letters e/t/t → Myself, then Mystery (5th e) before Mystic (5th i). First = **Myopia**.", None),
    P("aw-p3", "Extremes and immediate neighbours", "common",
        "'Which comes last / just after X / immediately before Y' — neighbour lookups on the sorted list.",
        "1. Sort fully and number the slots.\n2. 'Just after X' = X's slot + 1; 'immediately before Y' = Y's slot − 1.\n3. For 'last', only the deepest group's final word matters.\n\n*Why it works:* neighbours are slot arithmetic on the finished order.",
        "**Which comes just after Colony: Colonel, Colony, Column, Colour, Colossus?**",
        "Order: Colonel, Colony, Colossus, Colour, Column → just after Colony = **Colossus**.", None),
    P("aw-p4", "Counting from the right end", "common",
        "'Second from the right', 'third from the end' — the slot is counted from the back.",
        "1. Sort and number 1..N as usual.\n2. k-th from the right = slot N + 1 − k.\n3. Convert first, then read — do not count backwards on the raw list.\n\n*Why it works:* mirror of the slot lookup: the right end is slot N.",
        "**Arrange Judge, Judo, Joust, Journal, Jostle. Which word is second from the right?**",
        "Order: Jostle, Journal, Joust, Judge, Judo → slot 5 + 1 − 2 = 4 → **Judge**.", None),
]

PATTERNS["letter-position"] = [
    P("lp-p1", "Absolute position via EJOTY anchors", "very common",
        "'Which is the 15th letter' or 'how many letters between X and Y'.",
        "1. Step from the nearest anchor (E=5, J=10, O=15, T=20, Y=25).\n2. Between A and B: $|posA - posB| - 1$ ('between' excludes both ends).\n3. Confirm the letter sits within 5 of the predicted anchor.\n\n*Why it works:* five anchors turn 26 positions into five short hops.",
        "**How many letters of the alphabet are there between G and S?**",
        "$posS - posG - 1 = 19 - 7 - 1$ = **11**.", None),
    P("lp-p2", "Mirror positions from the right", "very common",
        "'k-th from the right' or 'position of letter X from the right'.",
        "1. From-right position = $27 - $ from-left position (and the reverse).\n2. Convert to from-left, answer with anchors, convert back if asked.\n3. Remember the 27: 26 letters + 1.\n\n*Why it works:* the mirror maps the strip onto itself around the midpoint.",
        "**What is the position of the letter T from the right of the alphabet?**",
        "$27 - 20$ = **7th** from the right.", None),
    P("lp-p3", "Letter arithmetic (left/right of a position)", "common",
        "'Which letter is 4th to the right of the 12th from the left' — two clauses in one question.",
        "1. Convert every clause to a from-the-left number (mirror any 'from the right').\n2. Right-steps add, left-steps subtract.\n3. Read the letter off the EJOTY anchors.\n\n*Why it works:* the alphabet strip is a number line in disguise.",
        "**Which letter is 6th to the left of the 8th letter from the right?**",
        "8th from right = $27-8=19$ (S); $19-6=13$ → **M**.", None),
    P("lp-p4", "Modified or reversed alphabet", "common",
        "'First half written in reverse', 'alphabet in reverse order', then a position question.",
        "1. Write the new 26-letter strip once on paper.\n2. Count the asked position on the new strip directly.\n3. For the full reverse only: reverse position p = normal letter $27 - p$.\n\n*Why it works:* a rewrite is a one-time setup; after that it is plain counting.",
        "**If the first half of the alphabet (A-M) is written in reverse order followed by N-Z, which letter is 10th from the left?**",
        "New strip: M L K J I H G F E D C B A N O ... → 10th = **D**.", None),
]

PATTERNS["word-formation"] = [
    P("wf-p1", "Dictionary rank of a word", "very common",
        "'All arrangements listed as in a dictionary — what is the rank of the word?'",
        "1. Sort the letters alphabetically; scan the word left to right.\n2. At each position add (unused letters smaller than the current one) × (arrangements of the rest).\n3. Arrangements of the rest = factorial of the count, divided by repeat factorials.\n4. Fix the letter, move right; total + 1 = rank.\n\n*Why it works:* each smaller unused letter heads a full block of arrangements that come first.",
        "**Find the dictionary rank of the word CAB.**",
        "C: A and B smaller → 2 × 2! = 4. A fixed; B: nothing smaller. Rank = 4 + 1 = **5** (ABT-style list: ABC, ACB, BAC, BCA, CAB).", None),
    P("wf-p2", "Same-position count after alphabetising", "common",
        "'Letters rearranged in alphabetical order — how many letters occupy their original position?'",
        "1. Write the word; write its letters sorted beneath it.\n2. Compare column by column; count exact matches only.\n3. Answer as a number word if the options say so.\n\n*Why it works:* a position survives only if the sorted letter equals the original letter there.",
        "**If the letters of DERAIL are rearranged in alphabetical order, how many letters remain in their original position?**",
        "DERAIL vs ADEILR: D≠A, E≠D, R≠E, A≠I, I≠L, L≠R → **None**.", None),
    P("wf-p3", "Forming words from a letter bag", "common",
        "'Which word can/cannot be formed from the letters of X?'",
        "1. List the bag with repeat counts.\n2. For each option, check its rarest letter first; cross off bag letters as used.\n3. One missing letter, or one letter needed more often than it appears, kills the option.\n\n*Why it works:* forming a word is a multiset check — counts matter as much as presence.",
        "**Which word CANNOT be formed from the letters of DISTRIBUTION?**",
        "Bag has D,I,S,T,R,B,U,O,N (I×2, T×2). STUDIO ✓, BIRD ✓, ROBUST ✓, BRUSH needs **H** → cannot be formed.", None),
    P("wf-p4", "Neighbours in a short arrangement list", "common",
        "3-letter words: 'which is the 4th arrangement' or 'what comes just after X' in dictionary order.",
        "1. List all 3! = 6 arrangements in dictionary order (a few seconds of writing).\n2. Count to the asked slot, or read the requested neighbour.\n\n*Why it works:* for six items, writing the list is faster and safer than any formula.",
        "**All arrangements of FAN are listed in dictionary order. Which word comes immediately after AFN?**",
        "List: AFN, ANF, FAN, FNA, NAF, NFA → after AFN = **ANF**.", None),
]

PYQS = [
    ("Letter-by-letter sorting", "very common", "dict-idea",
     "Words with a shared opening; 'which comes first/last/third'.",
     "Compare to the first differing letter; earlier letter wins; prefix sorts before extensions; sort once, number, read.",
     "**Arrange Scant, Scan, Scandal. Which comes last?**",
     "Scan (prefix) → Scandal (5th d) → Scant (5th t) → last = **Scant**."),
    ("Slot picking in a 4-6 word sort", "very common", "arrange-words",
     "A list of near-identical words plus 'which is the Nth'.",
     "Strip the stem, sort tails letter by letter, number the list, read the slot; convert 'from the right' to N+1−k.",
     "**Arrange Statue, Status, Station, Statute, Stature. Which is third from the left?**",
     "Station, Statue, Stature, Status, Statute → third = **Stature**."),
    ("EJOTY positions and mirrors", "very common", "letter-position",
     "'Nth letter', 'k-th from the right', 'letters between X and Y'.",
     "Anchors E=5 J=10 O=15 T=20 Y=25; between = difference − 1; mirror = 27 − position.",
     "**Which letter is 9th from the right of the English alphabet?**",
     "$27 - 9 = 18$ → **R**."),
    ("Modified alphabet strips", "common", "letter-position",
     "'Half the alphabet reversed' plus a position lookup.",
     "Write the new strip once, then count on paper; full reverse: position p ↔ letter 27−p.",
     "**Alphabet reversed (Z first). Which letter is 5th from the left?**",
     "Z Y X W V → 5th = **V**."),
    ("Dictionary rank of a word", "very common", "word-formation",
     "'Rank of the word among all arrangements of its letters'.",
     "Position by position: smaller unused letters × arrangements of the rest; add, then +1; divide by repeat factorials.",
     "**Rank of BEAD among all arrangements of its letters?**",
     "B: A smaller → 1 × 3! = 6. E: A and D smaller → 2 × 2! = 4. A: nothing smaller. Rank = 6 + 4 + 0 + 1 = **11**."),
    ("Word from a letter bag", "common", "word-formation",
     "'Which word can/cannot be formed from the letters of X?'",
     "Bag with repeat counts; check each option's rarest letter first; a missing letter or an over-used repeated letter kills the option.",
     "**Which word CANNOT be formed from the letters of DISTRIBUTION: STUDIO, BIRD, ROBUST, BRUSH?**",
     "The bag has no **H** → BRUSH cannot be formed; the rest fit inside the letter counts."),
]
