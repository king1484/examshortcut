"""Notes + patterns for the analogy topic (imported by analogy.py)."""
from _lib import P, PYQ

NOTES = {}
PATTERNS = {}

# ---------------------------------------------------------------- analogy-idea
NOTES["analogy-idea"] = """### What is an analogy?
An analogy is a comparison of two relationships. In daily life you may say, "a teacher works in a school just as a doctor works in a hospital". Both pairs share one link: *a person and the place where that person works*. In the exam this is written as **Teacher : School :: Doctor : Hospital**. Read the single colon ( : ) as "is to" and the double colon ( :: ) as "as".

The question shows three terms and hides the fourth, or shows one pair and asks you to pick a matching pair. You are **not** tested on how much you know about the words or numbers. You are tested on one skill: can you name the link correctly and copy it without changing it?

### The four-step method
1. **Say the link as one full sentence.** "The second word is the young one of the first." "The second number is the first multiplied by 5." "Each letter moves 2 places forward."
2. **Keep the direction.** If the first pair goes adult → young, the second pair must also go adult → young. Cow : Calf :: Horse : **Foal**, not Horse : Mare.
3. **Apply the same sentence to the third term.** Do not invent a new rule for the second pair.
4. **Test every option.** If two options seem to fit, your sentence is too loose. Make it sharper (add gender, add "measures", add "made from") until only one option survives.

### Kinds of analogy
| Kind | Example | What decides the answer |
|---|---|---|
| Word | Pen : Write :: Knife : Cut | meaning or use |
| Letter | ACE : BDF :: GIK : HJL | alphabet positions |
| Number | 3 : 27 :: 5 : 125 | an arithmetic rule |
| Mixed | C5 : F10 :: H8 : K16 | a letter rule and a number rule |
| Number set | (2, 4, 8) and (3, 9, 27) | one rule joining all three numbers |

### Formats of the question
- **Single blank at the end**: A : B :: C : ? — the most common form.
- **Blank at another place**: ? : B :: C : D or A : ? :: C : D. Find the rule from the complete pair and run it **backwards** if needed. If 5 : 125 is "cube", then ? : 64 means "which number cubed gives 64?" — the answer is 4.
- **Three-term analogy**: A : B : C :: D : E : ? — one rule joins all three terms in order. In 2 : 4 : 8, the terms are 2¹, 2², 2³, so 3 : 9 : ? needs 3³ = 27.
- **Double blank**: A : ? :: ? : D — each option gives two words or numbers. Put both into the blanks and keep the option where both halves follow the same rule.
- **Pair selection**: "Select the pair that is related in the same way as X : Y". Name the link of X : Y and test all four pairs.

### Precision decides close options
Many options come from the same field on purpose. In **Thermometer : Temperature :: Odometer : ?**, the options may be Distance, Speed, Kilometre and Car. All are about vehicles, but the link is "instrument : quantity it measures". An odometer measures **distance**; speed is measured by a speedometer, and a kilometre is only a *unit* of distance. The sharper sentence removes the traps.

### Common traps
- Reversing the direction (young → adult in one pair, adult → young in the other).
- Picking an option only because it is from the same topic (another animal, another number), not because it has the same link.
- Using one rule for the first pair and a slightly different rule for the second pair.
- Stopping at the first option that "looks right" without checking the other three.

### Quick revision
- ":" = is to, "::" = as. The link must be copied exactly, in the same direction.
- Method: name the link in one sentence → apply → test all four options.
- Missing first term? Run the rule backwards (divide instead of multiply, subtract instead of add).
- Three-term: one rule links all three terms in order. Double blank: both halves must use the same rule.
- Two options fit? Sharpen the sentence (gender, unit vs quantity, tool vs product, part vs material).
"""

PATTERNS["analogy-idea"] = [
    P("an-p1", "Missing term in the first or second place (? : B :: C : D)", "common",
      "The question mark is not at the end, e.g. '? : 64 :: 5 : 125' or 'Dog : ? :: Horse : Neigh'.",
      "1. Find the link from the complete pair.\n2. Write it as an equation or sentence (B = A³, 'second word is the sound of the first').\n3. Run it backwards for the missing term (take the cube root, find the animal that makes the sound).\n\n*Why it works:* the link is the same in both pairs; only the unknown's position has moved.",
      "**? : 64 :: 5 : 125**",
      "5 : 125 means 125 = 5³. So ? : 64 needs ?³ = 64, and 4³ = 64. **Answer: 4.**",
      formula=r"A = f^{-1}(B)"),
    P("an-p2", "Close options — choose the exact relation", "common",
      "All four options come from the same field (all instruments, all family words, all parts of a book). Two or three look right at first sight.",
      "1. Write the link as a sharp sentence ('instrument : what it measures', not just 'related to cars').\n2. Test each option with that sentence.\n3. Reject options that are a unit, a tool, a material or a place when the link needs a quantity, product or whole.\n\n*Why it works:* the setter places same-field traps; only the exact relation survives a precise sentence.",
      "**Thermometer : Temperature :: Odometer : ?** (Speed / Distance / Kilometre / Car)",
      "Link: instrument : quantity it measures. An odometer measures **distance**. Speed is measured by a speedometer; a kilometre is a unit, not a quantity; a car only carries the odometer. **Answer: Distance.**"),
    P("an-p3", "Three-term analogy (A : B : C :: D : E : ?)", "occasional",
      "Each side has three terms, e.g. '2 : 4 : 8 :: 3 : 9 : ?' or 'ACE : BDF : CEG :: JLN : KMO : ?'.",
      "1. Find how the 1st term becomes the 2nd, and how the 2nd becomes the 3rd.\n2. Check whether it is one rule (×2, ×2) or a power pattern (a, a², a³).\n3. Apply the same two steps to the second group.\n\n*Why it works:* three terms fix the rule more firmly than two, so there is usually only one fit.",
      "**2 : 4 : 8 :: 3 : 9 : ?**",
      "2, 4, 8 are 2¹, 2², 2³. So 3, 9, ? must be 3¹, 3², 3³ = 27. (Doubling 9 to get 18 is the trap — 3 → 9 is not doubling.) **Answer: 27.**",
      formula=r"a : a^2 : a^3"),
    P("an-p4", "Double blank — choose the pair that fills both blanks", "occasional",
      "Two question marks, e.g. '? : Calf :: Horse : ?' — each option gives two items.",
      "1. Put option 1 into both blanks and read both pairs.\n2. Name the link of each pair. Keep the option only if both links are the same and in the same direction.\n3. Repeat for the other options (only one survives).\n\n*Why it works:* a wrong pair usually fits one blank well but creates a different link in the other.",
      "**? : Calf :: Horse : ?** (Cow, Foal) / (Bull, Stable) / (Cow, Mare) / (Goat, Kid)",
      "(Cow, Foal): Cow : Calf is adult : young; Horse : Foal is adult : young ✓. (Bull, Stable) mixes young with home; (Cow, Mare) mixes young with female; Goat : Calf is wrong. **Answer: Cow, Foal.**"),
]

# ---------------------------------------------------------------- letter-analogy
NOTES["letter-analogy"] = """### What is a letter analogy?
Here the terms are letters or groups of letters (called *clusters*), such as **CAT : FDW :: PIN : ?**. The link is always a rule about **alphabet positions**. There is no meaning to find — only counting.

### Step 1: turn letters into numbers
Give every letter its place in the alphabet: A = 1, B = 2 ... Z = 26. Counting from A every time is slow, so learn the **EJOTY** anchors:

| Letter | E | J | O | T | Y |
|---|---|---|---|---|---|
| Position | 5 | 10 | 15 | 20 | 25 |

Now any letter is a small hop from an anchor: R = T − 2 = 18, L = J + 2 = 12, W = Y − 2 = 23.

Also learn the **opposite pairs** (they add up to 27): A-Z, B-Y, C-X, D-W, E-V, F-U, G-T, H-S, I-R, J-Q, K-P, L-O, M-N. A handy memory line: "**G**o **T**o **H**ell **S**ir" gives G-T and H-S.

### Step 2: subtract slot by slot
Write the position of each letter of the first cluster, then of the second cluster, and subtract. The list of changes is called the **shift tuple**. Example: CAT → FDW. C(3)→F(6) is +3, A(1)→D(4) is +3, T(20)→W(23) is +3. Tuple = (+3, +3, +3). Apply it to PIN: P+3 = S, I+3 = L, N+3 = Q → **SLQ**.

### Wrap-around
After Z the alphabet starts again at A. So Y + 3 = B (25 + 3 = 28, and 28 − 26 = 2 = B). Going back from A also wraps: B − 3 = Y (2 − 3 = −1, and −1 + 26 = 25 = Y).

### The rule bank
1. **Constant shift** — every letter moves the same number of places. EHKN : GJMP is +2 on every letter.
2. **Different shift per slot** — the tuple is not flat but has a pattern: (+1, +2, +3, +4) or (+2, −1, +2, −1). Copy the whole tuple exactly.
3. **Opposite letters** — each letter becomes its opposite (position 27 − p). GOLD : TLOW. Spot it when the pairs of letters add up to 27.
4. **Reversal** — the cluster is written backwards (LAMP : PMAL). It may be combined with a shift: RING → reverse GNIR → +1 → HOJS.
5. **Rearrangement** — letters are swapped in pairs (PLAY : LPYA), or each half is reversed (WINTER : NIWRET), or the first and last letters change places.

### How to pick the rule fast
- Read the second cluster backwards first. If you see the first cluster (or it shifted), it is reversal.
- If the second cluster has the **same letters** in a new order, it is rearrangement.
- Check the first pair of letters: do they add to 27? Then test opposite letters.
- Otherwise subtract positions and read the tuple.

### Worked example
**DRIVE : FUMAK :: PLANT : ?** D→F +2, R→U +3, I→M +4, V→A +5 (22 + 5 = 27 → A), E→K +6. Tuple (+2, +3, +4, +5, +6). PLANT: P+2 = R, L+3 = O, A+4 = E, N+5 = S, T+6 = Z → **ROESZ**.

### Quick revision
- EJOTY: E5, J10, O15, T20, Y25. Opposite pairs add to 27.
- Subtract slot by slot; the tuple is the rule; apply the same tuple.
- Past Z subtract 26; before A add 26.
- Same letters, new order → rearrangement. Backwards → reversal (maybe + shift).
- Missing first cluster → run the tuple backwards (subtract instead of add).
"""

PATTERNS["letter-analogy"] = [
    P("an-p5", "Constant shift letter-cluster analogy", "very common",
      "Every letter of the second cluster is the same number of places ahead of (or behind) the matching letter of the first cluster.",
      "1. Subtract positions slot by slot (use EJOTY).\n2. Confirm the tuple is flat (+k, +k, +k).\n3. Add k to every letter of the third cluster, wrapping past Z.\n\n*Why it works:* the whole cluster moves as one block, so one number describes the rule.",
      "**EHKN : GJMP :: RUXA : ?**",
      "E→G, H→J, K→M, N→P are all +2. RUXA + 2: R→T, U→W, X→Z, A→C → **TWZC**.",
      formula=r"c_i = w_i + k \pmod{26}"),
    P("an-p6", "Different shift for each slot (rising or alternating tuple)", "common",
      "The changes are not equal but form a pattern: +1, +2, +3, +4 or +2, −1, +2, −1.",
      "1. Write the full tuple from the first pair.\n2. Do not average it or 'correct' it — copy it exactly.\n3. Apply slot 1's change to letter 1, slot 2's to letter 2, and so on.\n\n*Why it works:* the rule is attached to the position in the cluster, not to the letter.",
      "**CFIL : DHLP :: GJMP : ?**",
      "C→D +1, F→H +2, I→L +3, L→P +4. GJMP: G+1 = H, J+2 = L, M+3 = P, P+4 = T → **HLPT**.",
      formula=r"c_i = w_i + d_i"),
    P("an-p7", "Opposite-letter analogy (and opposite + reverse)", "common",
      "The letters of the first pair add up to 27 (G + T, O + L). Sometimes the opposite cluster is also written backwards.",
      "1. Check one pair: position sum 27 means opposite letters.\n2. Replace each letter of the third cluster by its opposite (27 − position).\n3. If the model cluster was also reversed, reverse your result too.\n\n*Why it works:* opposite letters are a fixed swap table (A-Z, B-Y ... M-N).",
      "**GOLD : TLOW :: IRON : ?**",
      "G(7)+T(20) = 27, so opposite letters. I↔R, R↔I, O↔L, N↔M → **RILM**.",
      formula=r"c = 27 - p"),
    P("an-p8", "Reversal and reverse-plus-shift analogy", "common",
      "Reading the second cluster backwards gives the first cluster, or gives it with every letter moved by the same step.",
      "1. Reverse the second cluster and compare with the first.\n2. Same letters → pure reversal. Every letter off by k → reverse then shift by k.\n3. Do the same two steps, in the same order, on the third cluster.\n\n*Why it works:* reversal changes order, the shift changes letters; the two steps are independent.",
      "**RING : HOJS :: BELL : ?**",
      "RING backwards = GNIR; +1 on each gives HOJS. BELL backwards = LLEB; +1 → **MMFC**.",
      formula=None),
    P("an-p9", "Rearrangement analogy (swapped pairs, halves reversed)", "occasional",
      "The second cluster uses exactly the same letters as the first, only in a new order.",
      "1. Number the letters of the first cluster 1, 2, 3 ...\n2. Write the order in which they appear in the second cluster (e.g. 2-1-4-3).\n3. Rearrange the third cluster in the same order.\n\n*Why it works:* the rule is a fixed position map, so letter values do not matter.",
      "**PLAY : LPYA :: GIFT : ?**",
      "PLAY (1-2-3-4) → LPYA is order 2-1-4-3 (pairs swapped). GIFT in order 2-1-4-3 → **IGTF**.",
      formula=None),
]

# ---------------------------------------------------------------- word-analogy
NOTES["word-analogy"] = """### What is a word analogy?
You get a pair of meaningful words, like **Chef : Kitchen**, and a third word. You must find the word that has the same link with the third word. The exam uses a small, fixed bank of links again and again. If you learn the bank, most questions become quick.

### The two-question test
For every option ask:
1. **What is the link?** Say it as a sentence: "a chef *works in* a kitchen".
2. **Does the option make the same sentence with the third word?** "A pilot works in a cockpit" ✓. "A pilot flies an aeroplane" ✗ (different link).

### The relation bank
| Link | Examples |
|---|---|
| Worker : tool | Surgeon : Scalpel, Mason : Trowel, Woodcutter : Axe, Tailor : Needle |
| Worker : place of work | Chef : Kitchen, Judge : Court, Scientist : Laboratory |
| Worker : product | Poet : Poem, Cobbler : Shoes, Weaver : Cloth, Composer : Symphony |
| Adult : young one | Cow : Calf, Horse : Foal, Goat : Kid, Deer : Fawn, Frog : Tadpole |
| Animal : sound | Lion : Roar, Donkey : Bray, Frog : Croak, Horse : Neigh, Owl : Hoot |
| Animal : home | Lion : Den, Bee : Hive, Horse : Stable, Dog : Kennel, Pig : Sty |
| Male : female | Lion : Lioness, Peacock : Peahen, Drake : Duck, Ram : Ewe |
| Individual : group | Fish : Shoal, Wolf : Pack, Lion : Pride, Cattle : Herd, Ship : Fleet |
| Country : currency | India : Rupee, Japan : Yen, Thailand : Baht, Bangladesh : Taka |
| Country : capital | Nepal : Kathmandu, Bhutan : Thimphu, Egypt : Cairo, Canada : Ottawa |
| Instrument : quantity measured | Barometer : Pressure, Hygrometer : Humidity, Anemometer : Wind speed |
| Unit : quantity | Newton : Force, Pascal : Pressure, Joule : Energy, Ampere : Current |
| Study : subject | Ornithology : Birds, Ichthyology : Fishes, Entomology : Insects |
| Product : raw material | Glass : Sand, Paper : Wood, Butter : Milk, Jaggery : Sugarcane |
| Part : whole | Petal : Flower, Page : Book, Player : Team |
| Tool : action | Needle : Sew, Spade : Dig, Knife : Cut, Pen : Write |
| Cause : effect | Rain : Flood, Drought : Famine, Virus : Disease |
| Same meaning (synonym) | Begin : Commence, Abandon : Desert |
| Opposite meaning (antonym) | Ancient : Modern, Scarce : Abundant |
| Degree (mild : strong) | Warm : Hot, Breeze : Gale, Smile : Laugh |

### Precision rules
- **Unit vs quantity vs instrument.** Pascal is a unit, pressure is a quantity, barometer is an instrument. Keep the same type on both sides.
- **Tool vs product vs raw material.** For a weaver: loom is the tool, thread is the raw material, cloth is the product.
- **Young vs female.** Foal is a young horse; mare is a female horse. Do not mix them.
- **Degree direction.** Warm : Hot goes mild → strong, so Breeze : **Gale**, not Breeze : Air.
- **Synonym vs antonym.** If the model pair has the same meaning, the answer must have the same meaning, not the opposite.

### Worked example
**Cobbler : Shoes :: Weaver : ?** (Loom / Cloth / Thread / Tailor). Link: a cobbler *makes* shoes — worker : product. A weaver makes **cloth**. Loom is the tool and thread is the raw material, both traps.

### Quick revision
- Say the link as a sentence; test every option with the same sentence.
- Learn the bank: worker (tool / place / product), animal (young / sound / home / group / female), country (currency / capital), instrument or unit : quantity, study : subject, product : material, part : whole, tool : action, cause : effect, synonym, antonym, degree.
- Same field is not enough — the link type must match exactly.
- Keep direction: if the model goes whole → part, the answer must go whole → part.
"""

PATTERNS["word-analogy"] = [
    P("an-p10", "Worker : tool / workplace / product", "very common",
      "The first word is a person with a job (mason, cobbler, author, pilot).",
      "1. Decide which of the three links it is: tool used, place of work, or thing produced.\n2. Find the same link for the new worker.\n3. Reject options that are one of the other two links (a tool when the model needs a product).\n\n*Why it works:* every worker has a tool, a place and a product — the setter uses the other two as traps.",
      "**Cobbler : Shoes :: Weaver : ?** (Loom / Cloth / Thread / Tailor)",
      "A cobbler makes shoes (worker : product). A weaver makes **cloth**. Loom = tool, thread = raw material. **Answer: Cloth.**"),
    P("an-p11", "Animal : young one / sound / home / group", "very common",
      "One word is an animal or bird and the other is its baby, its cry, its shelter or its group name.",
      "1. Identify which animal fact is being used.\n2. Recall the same fact for the new animal.\n3. Make sure the option is not a different fact about the same animal (sound instead of home).\n\n*Why it works:* each animal has one standard word for each fact, learnt in school.",
      "**Lion : Den :: Bee : ?** (Honey / Hive / Swarm / Buzz)",
      "A den is the lion's home. A bee's home is a **hive**. Honey is its product, swarm its group, buzz its sound. **Answer: Hive.**"),
    P("an-p12", "Country : currency / capital", "common",
      "A country is paired with its money or its capital city.",
      "1. See whether the model pair is currency or capital.\n2. Recall the same for the new country.\n3. The other options are real currencies/capitals of other countries — be exact.\n\n*Why it works:* only one option belongs to the given country.",
      "**India : Rupee :: Thailand : ?** (Yuan / Baht / Ringgit / Dong)",
      "Rupee is India's currency. Thailand's currency is the **baht**. Yuan = China, ringgit = Malaysia, dong = Vietnam. **Answer: Baht.**"),
    P("an-p13", "Instrument or unit : quantity", "common",
      "A measuring instrument (barometer, hygrometer) or an SI unit (newton, pascal) is paired with what it measures.",
      "1. Note the type of each word: instrument, unit or quantity.\n2. Keep the same type pattern for the answer.\n3. Recall the fact (anemometer → wind speed, pascal → pressure).\n\n*Why it works:* the traps are usually a unit when a quantity is needed, or a nearby quantity.",
      "**Newton : Force :: Pascal : ?** (Power / Pressure / Energy / Current)",
      "The newton is the unit of force. The pascal is the unit of **pressure**. (Power = watt, energy = joule, current = ampere.) **Answer: Pressure.**"),
    P("an-p14", "Study : subject, product : raw material, part : whole", "common",
      "Words like '-logy' sciences, or a finished product and what it is made from, or a small part and the whole thing.",
      "1. Name the link: 'is the study of', 'is made from', 'is a part of'.\n2. Apply it to the third word.\n3. Watch the direction: product → material, not material → product.\n\n*Why it works:* these links have one clear answer each once the direction is fixed.",
      "**Butter : Milk :: Jaggery : ?** (Sugar / Sugarcane / Sweet / Tea)",
      "Butter is made from milk (product : raw material). Jaggery is made from **sugarcane** juice. Sugar is another product, not the material. **Answer: Sugarcane.**"),
    P("an-p15", "Synonym, antonym and degree pairs", "common",
      "Two ordinary words that mean the same, the opposite, or a milder and stronger form of the same idea.",
      "1. Decide: same meaning, opposite meaning, or mild → strong.\n2. Find the option with that link to the third word.\n3. Reject the option that has the other type (an antonym when a synonym is needed).\n\n*Why it works:* the setter usually places one synonym and one antonym among the options.",
      "**Warm : Hot :: Breeze : ?** (Air / Gale / Calm / Rain)",
      "Hot is a stronger degree of warm. A stronger degree of a breeze is a **gale**. Calm is the opposite; air is just the general word. **Answer: Gale.**"),
    P("an-p16", "Tool : action and cause : effect", "common",
      "An object and what it is used to do (needle : sew), or an event and what it leads to (rain : flood).",
      "1. Say 'X is used to ...' or 'X leads to ...'.\n2. Complete the same sentence for the third word.\n3. Reject places, users and materials connected to the object.\n\n*Why it works:* the answer must be an action or a result, which removes noun traps quickly.",
      "**Needle : Sew :: Spade : ?** (Garden / Dig / Soil / Farmer)",
      "A needle is used to sew. A spade is used to **dig**. Garden = place, soil = what is dug, farmer = user. **Answer: Dig.**"),
]

# ---------------------------------------------------------------- number-analogy
NOTES["number-analogy"] = """### What is a number analogy?
You get a pair like **4 : 20** and a third number, say 7. The first pair hides an arithmetic rule. You apply the same rule to 7. Here 20 = 4 × 5, so 7 × 5 = 35.

### Step 1: the size test
Look at how big the second number is compared with the first. It tells you which family to try first.

| What you see | Family to try first |
|---|---|
| Second number a little bigger | add or subtract, or ×2 ± small number |
| Second number about k times bigger | ×k ± r |
| Second number near the square of the first | a² ± r, a(a + 1), (a + 1)² |
| Second number huge | a³ ± r |
| Two-digit numbers, answer small | digit sum, digit product |
| Digits look swapped | reverse the digits |

### Step 2: know your squares and cubes
Squares 1 to 20: 1, 4, 9, 16, 25, 36, 49, 64, 81, 100, 121, 144, 169, 196, 225, 256, 289, 324, 361, 400.
Cubes 1 to 12: 1, 8, 27, 64, 125, 216, 343, 512, 729, 1000, 1331, 1728.
When you see 35, think 36 − 1. When you see 126, think 125 + 1. When you see 72, think 8 × 9 = a(a + 1) for a = 8.

### The rule bank
1. **Linear**: b = k·a ± r. Example 9 : 40 → 9 × 4 + 4 = 40; so 13 → 13 × 4 + 4 = 56.
2. **Square based**: b = a² ± r, a(a + 1), a(a − 1). Example 6 : 35 → 6² − 1; so 9 → 80.
3. **Cube based**: b = a³ ± r. Example 4 : 65 → 4³ + 1; so 5 → 126.
4. **Digit based**: product of digits (47 → 4 × 7 = 28), sum of digits, square of the digit sum (36 → (3 + 6)² = 81), reversed digits (34 → 43).
5. **Chain of pairs**: 4 : 20 :: 6 : 42 :: 8 : ? — two model pairs fix the rule. 4 × 5, 6 × 7, so 8 × 9 = 72.

### Why you must test the rule, and use the options
One pair can fit many rules. 7 : 23 fits 7 × 3 + 2 and also 7 × 2 + 9. For 11 these give 35 and 31. The examiner keeps only one of these answers in the options. So:
- Find the simplest natural rule and compute the answer.
- If your answer is **not** in the options, try the next family. Do not force a rule.
- If two model pairs are given, your rule must fit **both**.

### The whole-number note
Many papers add: "Operations should be performed on the whole numbers, without breaking them into digits." When this note is present, do **not** use digit sums or digit products. Only use operations on the full number (×, +, squares, cubes).

### Pair-selection form
"Select the pair in which the numbers are related in the same way as 7 : 49." Find the link (a²), then check all four pairs. Only 9 : 81 keeps the link. Check each pair fully — the traps are near misses like 8 : 60.

### Worked example
**8 : 72 :: 12 : ?** 72 is 8 × 9 = a(a + 1). So 12 × 13 = **156**. Traps: 144 (12², forgot the +a), 132 (12 × 11, used a − 1).

### Quick revision
- Size test first: small change → linear; near a square → a² ± r; huge → cube.
- Know squares to 20 and cubes to 12 by heart.
- Check the rule on the model pair before using it; answer missing → change family.
- Whole-number note present → no digit tricks.
- Pair-selection: one rule, test every pair completely.
"""

PATTERNS["number-analogy"] = [
    P("an-p17", "Linear rule: b = k × a ± r", "very common",
      "The second number is a few times the first, plus or minus a small number (7 : 23, 9 : 40).",
      "1. Divide b by a to guess k (23 ÷ 7 ≈ 3).\n2. Find r = b − k·a (23 − 21 = 2).\n3. Apply k·c + r to the third number, then check the answer is in the options.\n\n*Why it works:* most setters build number pairs with one multiplication and one small addition.",
      "**9 : 40 :: 13 : ?**",
      "9 × 4 + 4 = 40. So 13 × 4 + 4 = **56**. (52 forgets the +4.)",
      formula=r"b = k\,a + r"),
    P("an-p18", "Square or cube based rule", "very common",
      "The second number is close to a square or cube of the first (6 : 35, 4 : 65, 8 : 72).",
      "1. Compare b with a² and a³.\n2. Note the difference (35 = 36 − 1; 65 = 64 + 1) or the product form (72 = 8 × 9).\n3. Apply the same form to the third number.\n\n*Why it works:* squares and cubes grow fast, so a large jump almost always means a power.",
      "**6 : 35 :: 9 : ?**",
      "35 = 6² − 1. So 9² − 1 = **80**. (81 forgets the −1.)",
      formula=r"b = a^2 \pm r,\; a^3 \pm r,\; a(a+1)"),
    P("an-p19", "Digit-based rule (sum, product, reversal)", "common",
      "Two-digit numbers where the second number is small or looks like the digits rearranged (47 : 28, 36 : 81, 34 : 43).",
      "1. Try digit product, digit sum and the square of the digit sum.\n2. Try reversing the digits.\n3. Use this family only when the whole-number note is NOT given.\n\n*Why it works:* digit rules explain pairs that no simple ×k ± r rule can.",
      "**47 : 28 :: 59 : ?**",
      "4 × 7 = 28 (product of digits). So 5 × 9 = **45**. (14 is the digit sum trap.)",
      formula=None),
    P("an-p20", "Select the number pair with the same relation", "common",
      "'Select the option in which the numbers share the same relationship as 7 : 49' — the options are complete pairs.",
      "1. Find the rule of the model pair.\n2. Test all four pairs with that rule.\n3. If two pairs fit, look for a sharper rule that fits the model and only one option.\n\n*Why it works:* the traps are near misses (off by 1 or 2), which a full calculation catches.",
      "**Select the pair related like 13 : 41.** (17 : 53 / 15 : 44 / 19 : 55 / 21 : 62)",
      "41 = 13 × 3 + 2. Test: 17 × 3 + 2 = 53 ✓; 15 → 47, 19 → 59, 21 → 65 ✗. **Answer: 17 : 53.**",
      formula=r"b = f(a)"),
]

# ---------------------------------------------------------------- mixed-analogy
NOTES["mixed-analogy"] = """### What is a mixed analogy?
Mixed analogies join two worlds: letters and numbers, or words and numbers. The good news is that each part follows its own simple rule. You solve the parts one at a time and then put the answer together.

### Type 1: letter-number clusters
Example: **C5 : F10 :: H8 : ?**
- Letter track: C(3) → F(6) is +3. So H(8) + 3 = K.
- Number track: 5 → 10 is × 2. So 8 × 2 = 16.
- Answer: **K16**.

The two tracks do not affect each other. Solve the letters with positions (EJOTY helps) and the numbers with arithmetic. If a cluster has two letters (B3D), each letter slot has its own shift.

Sometimes the number is built **from** the letter: D16, F36, H64 — each number is the square of its letter's position (D = 4, 4² = 16). Then the next letter decides the number.

### Type 2: word → number
Example: **CAT : 24 :: BAT : ?**
The number comes from the letter positions of the word. The rule bank:
1. **Sum of positions**: CAT = 3 + 1 + 20 = 24.
2. **Sum × k or sum ± r**: DOG = 26, coded as 52 → × 2.
3. **Reverse positions** (A = 26, B = 25 ... Z = 1): each letter counts as 27 − p.
4. **Number of letters** × something (rare).

Work out the sum for the model word first; then compare it with the given number to find the extra step.

### Type 3: letter → number
Example: **C : 9 :: E : ?** C is the 3rd letter and 9 = 3². So E (5th) gives 5² = **25**. Other common rules: 2 × position, reverse position (B → 25), position + constant.

### Type 4: same-relation word pairs
"Select the pair that is related in the same way as Tailor : Needle." Say the link — *worker : tool* — and test all four pairs. Traps are pairs from the same world with a different link: Doctor : Hospital (workplace), Author : Book (product).

### Solving method in short
1. Split the term into its parts (letters, numbers, word, number).
2. Find one small rule per part from the model pair.
3. Apply each rule to the matching part of the third term.
4. Join the parts and look for the exact combination in the options (traps change just one part).

### Common mistakes
- Solving the letter part correctly but copying the wrong number (or the reverse). Options usually differ in only one part.
- Using A = 0 instead of A = 1 when counting positions.
- For word → number, forgetting the extra × k or + r that the model pair revealed.
- In pair selection, choosing a pair from the same topic instead of the same link.

### Quick revision
- Split, solve each track, then join.
- Letter tracks: positions and shifts. Number tracks: +, ×, squares.
- Word → number: first try the plain sum of positions, then × k or ± r.
- Letter → number: position, 2 × position, position², reverse position (27 − p).
- Pair selection: one link sentence tested on all four pairs.
"""

PATTERNS["mixed-analogy"] = [
    P("an-p22", "Letter-number cluster analogy", "common",
      "Terms like 'C5 : F10' or 'P7R : S14U' mix letters and numbers.",
      "1. Split each term into a letter track and a number track.\n2. Find the letter shift and the number rule separately.\n3. Apply both to the third term and join the parts.\n\n*Why it works:* the tracks are independent, so each one is a tiny, easy question.",
      "**C5 : F10 :: H8 : ?**",
      "Letters: C → F is +3, so H → K. Numbers: 5 → 10 is × 2, so 8 → 16. **Answer: K16.**"),
    P("an-p23", "Word to number (sum of letter positions)", "common",
      "A word is paired with a number, e.g. 'CAT : 24 :: BAT : ?'.",
      "1. Add the positions of the model word's letters.\n2. Compare the sum with the given number: equal, × k, or ± r.\n3. Find the sum for the new word and apply the same extra step.\n\n*Why it works:* setters build the number from letter positions in one or two simple steps.",
      "**RAM : 32 :: SHAM : ?**",
      "R + A + M = 18 + 1 + 13 = 32 (plain sum). SHAM = 19 + 8 + 1 + 13 = **41**.",
      formula=r"\text{code} = k\sum p_i + r"),
    P("an-p24", "Select the word pair with the same relation", "common",
      "A model pair followed by four complete word pairs: 'Select the pair related in the same way as Tailor : Needle'.",
      "1. Write the link of the model pair as a sentence.\n2. Put each option pair into that sentence.\n3. Only one pair should make a true sentence in the same direction.\n\n*Why it works:* traps share the topic but not the link (workplace instead of tool).",
      "**Tailor : Needle** — (Painter : Brush / Doctor : Hospital / Author : Book / Farmer : Crop)",
      "Link: worker : tool used. Painter uses a brush ✓. Hospital = workplace, book and crop = products. **Answer: Painter : Brush.**"),
    P("an-p25", "Letter to number (position-based)", "occasional",
      "A single letter is paired with a number, e.g. 'C : 9 :: E : ?' or 'B : 25 :: D : ?'.",
      "1. Write the letter's position (and its reverse position 27 − p).\n2. See how the number is built: p², 2p, 27 − p, p + r.\n3. Apply the same build to the new letter.\n\n*Why it works:* only a few simple formulas are used, and each is quick to test.",
      "**C : 9 :: E : ?**",
      "C is 3rd and 9 = 3². E is 5th, so 5² = **25**.",
      formula=r"n = p^2,\; 2p,\; 27-p"),
]

# ---------------------------------------------------------------- number-set-analogy (NEW)
NOTES["number-set-analogy"] = """### What is a number-set analogy?
This is a newer and very common form. You are shown two or more **sets** of numbers, such as (6, 13, 27) and (8, 17, 35). All numbers inside a set are linked by the same rule. You must pick the option set whose numbers follow **the same rule**.

The question usually carries a note: *"Operations should be performed on the whole numbers, without breaking down the numbers into their constituent digits. E.g. 13: operations on 13 such as adding, subtracting or multiplying 13 are allowed; breaking 13 into 1 and 3 is not allowed."* So only use +, −, ×, ÷, squares and cubes of the full numbers. No digit tricks.

### How the rule can be built
There are four families you will meet again and again.

**1. Chain rule (first → second → third).** The same step is used twice. In (6, 13, 27): 6 × 2 + 1 = 13 and 13 × 2 + 1 = 27. Check (8, 17, 35): 8 × 2 + 1 = 17, 17 × 2 + 1 = 35 ✓. The step can also change: (4, 9, 27) is +5 then × 3.

**2. Third from the first two.** The third number is made from the other two: product (3, 8, 24), sum of squares (4, 5, 41 because 16 + 25 = 41), twice the sum (5, 9, 28).

**3. Power sets.** Numbers are powers or near-powers of the first: (2, 4, 8) is a, a², a³; (3, 10, 28) is a, a² + 1, a³ + 1; (7, 49, 56) is a, a², a + a².

**4. Middle links the outer two.** The middle number is made from the two outer numbers: (5, 35, 7) because 5 × 7 = 35; (8, 13, 18) because 13 is the average of 8 and 18. Or the first is the sum of the other two: (14, 5, 9).

### Method
1. Take the first model set. Try the chain rule: how does the 1st become the 2nd? Does the same step turn the 2nd into the 3rd?
2. If not, try the third from the first two: a + b, a × b, a² + b², (a + b) × k.
3. If not, try powers, then the middle-link family.
4. **Confirm the rule on the second model set.** A rule that fits only one set is wrong.
5. Test the four options one by one. Exactly one fits. Traps are usually off by 1 to 3 in the last number.

### Worked example
Sets: (4, 5, 41), (3, 7, 58). Chain? 4 → 5 is +1 but 5 → 41 is not +1. Third from first two: 4² + 5² = 16 + 25 = 41 ✓; 3² + 7² = 9 + 49 = 58 ✓. Options: (2, 6, 40), (5, 4, 40), (6, 3, 36), (1, 8, 64). 2² + 6² = 4 + 36 = 40 ✓; 25 + 16 = 41 ✗; 36 + 9 = 45 ✗; 1 + 64 = 65 ✗. **Answer: (2, 6, 40).**

### Speed tips
- Check the **last number first** in each option — traps usually change only that.
- If the numbers grow about ×2 each step, try ×2 ± 1; about ×3, try ×3 ± 1.
- Numbers like 26, 37, 50, 65 are squares + 1; 28, 65, 126 are cubes + 1.

### Quick revision
- Obey the whole-number note: no digit sums or products.
- Four families: chain (a → b → c), third from first two, power sets, middle links outer.
- The rule must fit every model set before you test options.
- Test all options fully; exactly one follows the rule.
"""

PATTERNS["number-set-analogy"] = [
    P("an-p26", "Chain rule sets (a → b → c by the same step)", "very common",
      "In each set the numbers grow step by step: (6, 13, 27), (8, 17, 35).",
      "1. Find the step from the 1st to the 2nd number (× k ± r or + r).\n2. Check the same step takes the 2nd to the 3rd.\n3. Confirm on the other model set, then test the options.\n\n*Why it works:* a repeated step is the simplest rule that links three numbers.",
      "Sets **(6, 13, 27)** and **(8, 17, 35)**. Which set follows the same rule: (5, 11, 23) / (7, 15, 30) / (9, 19, 38) / (4, 9, 20)?",
      "Rule: × 2 + 1 each step (6 → 13 → 27). (5, 11, 23): 5×2+1 = 11, 11×2+1 = 23 ✓. The others fail at the last number. **Answer: (5, 11, 23).**",
      formula=r"b = k a + r,\; c = k b + r"),
    P("an-p27", "Third number from the first two", "common",
      "The third number is bigger than both and looks like a product, a sum of squares or a multiple of the sum.",
      "1. Try a × b, a + b, a² + b², (a + b) × k on the model sets.\n2. Keep the one that fits every model set.\n3. Apply it to each option's first two numbers and compare with its third.\n\n*Why it works:* the first two numbers are 'inputs' and the third is the 'output'.",
      "Sets **(3, 8, 24)** and **(5, 6, 30)**. Which follows the same rule: (7, 4, 28) / (6, 5, 32) / (9, 3, 36) / (8, 2, 18)?",
      "Rule: third = first × second (3 × 8 = 24, 5 × 6 = 30). 7 × 4 = 28 ✓; 30, 27, 16 fail the others. **Answer: (7, 4, 28).**",
      formula=r"c = a \times b,\; a^2+b^2,\; k(a+b)"),
    P("an-p28", "Power sets (a, a², a³ and near-powers)", "common",
      "The second number is the square of the first, the third looks like a cube, or both are 'square + 1' and 'cube + 1'.",
      "1. Compare the 2nd number with a² and the 3rd with a³ (or a + a²).\n2. Note any ± r.\n3. Test each option by building a², a³ from its first number.\n\n*Why it works:* powers grow so fast that they are easy to recognise.",
      "Sets **(3, 10, 28)** and **(4, 17, 65)**. Which follows the same rule: (5, 26, 126) / (6, 37, 215) / (2, 5, 8) / (7, 50, 342)?",
      "Rule: (a, a² + 1, a³ + 1). 5: 25 + 1 = 26, 125 + 1 = 126 ✓. 6 needs 217, 2 needs 9, 7 needs 344. **Answer: (5, 26, 126).**",
      formula=r"(a,\; a^2+1,\; a^3+1)"),
    P("an-p29", "Middle number links the outer two (or first = sum of the others)", "occasional",
      "The middle number is the product or the average of the outer two, or the first number equals the sum of the other two.",
      "1. Multiply, add and average the outer numbers; compare with the middle.\n2. Also test first = second + third.\n3. Confirm on all model sets, then test the options.\n\n*Why it works:* setters sometimes hide the 'output' in the middle instead of at the end.",
      "Sets **(5, 35, 7)** and **(4, 36, 9)**. Which follows the same rule: (6, 48, 8) / (3, 24, 9) / (7, 56, 9) / (2, 18, 8)?",
      "Middle = first × third (5 × 7 = 35, 4 × 9 = 36). 6 × 8 = 48 ✓; 27, 63 and 16 fail the others. **Answer: (6, 48, 8).**",
      formula=r"b = a \times c,\; b = \tfrac{a+c}{2}"),
]

NEW_SUB = {
    "id": "number-set-analogy",
    "title": "Number sets (triads) analogy",
    "concept": "Two or more sets of numbers such as (6, 13, 27) and (8, 17, 35) share one hidden rule; you pick the option set that follows the same rule. The rule links all numbers of a set — a repeated step (×2 + 1), the third made from the first two (a × b, a² + b²), powers (a, a², a³) or a middle number made from the outer two. Most papers add the note that operations must be done on whole numbers, so digit tricks are not allowed.",
    "formulas": [
        {"name": "Chain rule", "tex": r"b = ka + r,\; c = kb + r", "note": "Same step applied twice."},
        {"name": "Third from first two", "tex": r"c = ab,\; a^2 + b^2,\; k(a+b)", "note": "Test on every model set."},
        {"name": "Power set", "tex": r"(a,\; a^2 \pm r,\; a^3 \pm r)", "note": "Near-squares and near-cubes."},
    ],
    "tricks": [
        {
            "title": "Check the last number first",
            "body": "Build the rule from the model sets, then for each option compute only what the last number should be. Traps nearly always change the last number by 1 to 3, so this finds the answer in one pass.",
            "example": {
                "q": "**Q.** Sets (2, 4, 8) and (3, 9, 27). Which follows the same rule: (4, 16, 60) / (5, 25, 125) / (6, 36, 206) / (7, 49, 334)?",
                "solution": "Rule (a, a², a³). Last numbers should be 64, 125, 216, 343. Only (5, 25, 125) matches. **Answer: (5, 25, 125).**",
            },
        }
    ],
    "mistakes": [
        "Breaking numbers into digits when the question says to use whole numbers only.",
        "Accepting a rule that fits the first model set but not the second.",
        "Checking only the first two numbers of an option and missing that the third is off by one.",
    ],
}

# ---------------------------------------------------------------- topic-level pyqPatterns
PYQS = [
    PYQ("Letter-cluster analogy with a constant shift", "very common",
        "Three letter clusters and a blank, such as 'EHKN : GJMP :: RUXA : ?'. Every letter of the second cluster is the same number of places away from the first.",
        "Write positions using EJOTY, subtract slot by slot and confirm the change is the same everywhere. Add that change to each letter of the third cluster, wrapping past Z.",
        "letter-analogy", "**EHKN : GJMP :: RUXA : ?**", "Each letter moves +2 (E→G, H→J, K→M, N→P). RUXA + 2 = **TWZC**."),
    PYQ("Letter analogy with a per-slot, opposite or reversal rule", "common",
        "The shift is not the same for every letter, or letters pair to 27 (opposites), or the second cluster read backwards gives the first.",
        "Test in this order: backwards reading (reversal), 27-sum (opposites), then the full shift tuple. Copy the discovered rule exactly — the same tuple, the same order of steps.",
        "letter-analogy", "**GOLD : TLOW :: IRON : ?**", "G + T = 27, so letters are replaced by opposites. IRON → **RILM**."),
    PYQ("Word analogy from the standard relation bank", "very common",
        "A meaningful word pair (Mason : Trowel, Lion : Den, Newton : Force) and a third word with a blank.",
        "Say the link as one sentence (worker : tool, animal : home, unit : quantity) and test every option with it. Reject options from the same field that have a different link.",
        "word-analogy", "**Newton : Force :: Pascal : ?**", "The newton is the unit of force; the pascal is the unit of **pressure**."),
    PYQ("Number analogy with one model pair", "very common",
        "Pairs like '6 : 35 :: 9 : ?' or '9 : 40 :: 13 : ?'.",
        "Use the size test to choose the family (linear, square, cube, digit). Check the rule on the model pair, apply it, and if the answer is missing from the options move to the next family.",
        "number-analogy", "**6 : 35 :: 9 : ?**", "35 = 6² − 1, so 9² − 1 = **80**."),
    PYQ("Number sets (triads) with a common rule", "very common",
        "Two sets like (6, 13, 27) and (8, 17, 35), with the whole-number note; options are sets of three numbers.",
        "Try the chain rule, then 'third from the first two', then powers, then the middle-link family. Confirm on both model sets, then compute what each option's last number should be.",
        "number-set-analogy", "Sets **(4, 5, 41)** and **(3, 7, 58)**. Which follows the rule: (2, 6, 40) / (5, 4, 40)?", "Third = a² + b² (16 + 25 = 41, 9 + 49 = 58). 4 + 36 = 40 ✓ → **(2, 6, 40)**."),
    PYQ("Select the pair with the same relation", "common",
        "A model pair of words or numbers followed by four complete pairs.",
        "Write the link of the model pair once and test all four pairs completely. For numbers, compute each pair exactly — traps miss by one or two.",
        "mixed-analogy", "Select the pair related like **Tailor : Needle**: Painter : Brush / Doctor : Hospital.", "Worker : tool. A painter uses a brush → **Painter : Brush**."),
    PYQ("Mixed letter-number and word-number analogy", "common",
        "Terms such as 'C5 : F10 :: H8 : ?' or 'RAM : 32 :: SHAM : ?'.",
        "Split into a letter track and a number track, or compute the sum of letter positions for the word. Find one small rule per part and join the parts.",
        "mixed-analogy", "**RAM : 32 :: SHAM : ?**", "RAM = 18 + 1 + 13 = 32 (sum of positions). SHAM = 19 + 8 + 1 + 13 = **41**."),
    PYQ("Blank in another position, three-term and double-blank analogies", "occasional",
        "The question mark is in the first or second place, there are three terms per side, or there are two blanks with pair options.",
        "Find the rule from the complete pair and run it backwards if the first term is missing. For double blanks, put each option into both places and keep the one where both pairs share the same link.",
        "analogy-idea", "**? : 64 :: 5 : 125**", "125 = 5³, so ?³ = 64 → **4**."),
]
