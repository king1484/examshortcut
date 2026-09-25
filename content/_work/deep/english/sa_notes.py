# Notes + per-subtopic patterns for synonyms-antonyms (Phase 2 deep content).
S = {}


def P(id, name, freq, spot, logic, eq, es):
    return {"id": id, "name": name, "frequency": freq, "howToSpot": spot, "formula": None, "logic": logic,
            "example": {"q": eq, "solution": es}}


S["syn-root-word-method"] = {
"notes": """### Why roots work
A synonym question gives you a word and four options. When you do not know the word, you are not helpless: most hard exam words are built from **prefix + root + suffix**, and the same few dozen parts appear again and again. Decode the parts, and you can often choose the nearest meaning without ever having seen the word.

### The prefixes that appear most
| Prefix | Meaning | Example |
|---|---|---|
| in-, im-, il-, ir-, un-, dis- | not | indispensable (cannot be done without), illegible, irregular |
| mal- | bad | malicious, malnutrition |
| bene- | good, well | benefactor, benevolent |
| circum- | around | circumvent, circumference |
| pre-, post- | before, after | postpone, precaution |
| sub-, super- | under, above | subordinate, supervise |
| mono-, poly- | one, many | monotone, polyglot |
| auto- | self | autobiography, autograph |
| magn- | great | magnanimous, magnitude |
| chron- | time | chronological, chronicle |
| aud-, vis-, spect- | hear, see, look | audible, visible, inspect |
| port- | carry | portable, transport |
| dict- | say | dictate, contradict |
| tract- | pull | attract, extract |
| anim- | mind, spirit | magnanimous, unanimous |

### The method, step by step
1. **Split the word** into parts you recognise: MAGNANIMOUS = magn (great) + anim (mind, spirit) + ous (adjective ending).
2. **Translate the parts**: great-spirited → generous, ready to forgive.
3. **Match with the options**: generous is the nearest meaning.
4. **Check the part of speech**: -ous, -ful, -ive endings usually mean an adjective; -tion, -ment, -ness a noun. Your answer should match.

### When the method misleads: the false-root trap
A few famous words *look* like they contain a helpful root, but the meaning has drifted. Learn these five as fixed exceptions:
- **enervate** = to weaken (it looks like 'energy' but means the opposite).
- **restive** = restless, hard to control (it looks like 'rest' = calm).
- **inflammable** = easily set on fire (it does not mean 'not flammable').
- **invaluable** = extremely valuable (it does not mean 'worthless').
- **noisome** = foul-smelling (it has nothing to do with noise).

If you know the word directly, trust your memory over the root. Use the root only as a *guessing* tool for unknown words, and be extra careful when an option simply repeats the root's surface meaning — for enervate, the trap option is 'to energise'.

### Building speed
In practice, run a two-second prefix check on every option: *does its prefix match the stem word's prefix family?* If the stem has a positive prefix (bene-) and an option carries a negative one (mal-), the option is almost certainly wrong. This one habit removes one or two options in most questions even when you do not know any word fully.

### Quick revision
- Split → translate → match → check part of speech.
- Core prefixes: not (in/im/il/ir/un/dis), bad (mal), good (bene), around (circum), one/many (mono/poly), self (auto), before/after (pre/post).
- Core roots: spect (look), port (carry), dict (say), chron (time), anim (spirit), tract (pull), aud (hear).
- Memorise the false-root five: enervate, restive, inflammable, invaluable, noisome.
""",
"patterns": [
 P("srm-p1", "Prefix gives the direction (positive or negative)", "very common",
   "The stem word starts with a strong prefix (mal-, bene-, in-/un-/dis-) and one or two options start with opposite prefixes.",
   "1. Read the prefix: mal = bad, bene = good, in/un/dis = not.\n2. Fix the direction of the meaning before reading the options.\n3. Reject options whose direction clashes; choose the nearest positive/negative match.\n\n*Why it works:* prefixes are stable across thousands of words.",
   "*Nearest in meaning to MALICIOUS*", "mal = bad → intending harm → **spiteful**. Kind-hearted fails the direction check."),
 P("srm-p2", "Root gives the core meaning", "very common",
   "The stem contains a root you know (spect, port, dict, chron, anim) even if the whole word is unfamiliar.",
   "1. Strip the prefix and suffix; find the root.\n2. Recall the root's meaning (port = carry, chron = time).\n3. Pick the option built on that core idea.\n\n*Why it works:* Greek and Latin roots keep their meaning in every English word that borrows them.",
   "*Nearest in meaning to MAGNANIMOUS*", "magn (great) + anim (spirit) → **generous, forgiving**."),
 P("srm-p3", "Chunking a long word into known pieces", "common",
   "The word is long and technical-looking (chronological, indispensable, circumvent).",
   "1. Cut the word where a known piece ends: circum + vent.\n2. Translate piece by piece: around + come.\n3. Assemble: to come around → to get around a rule by cleverness.\n\n*Why it works:* long exam words are usually transparent stacks of two known pieces.",
   "*Nearest in meaning to CHRONOLOGICAL*", "chron = time → arranged in time order. Alphabetical is the planted wrong order."),
 P("srm-p4", "False-root trap words", "common",
   "An option simply repeats the surface root (energise for enervate, calm for restive, worthless for invaluable).",
   "1. Check the word against the memorised false-root list first.\n2. If it is on the list, ignore the apparent root and use the fixed meaning.\n3. Then treat the root-repeating option as the trap, not the answer.\n\n*Why it works:* these five words are famous precisely because their shape misleads.",
   "*Nearest in meaning to ENERVATE*", "**Weaken**, not energise. The 'energy' shape is the trap."),
],
}

S["syn-elimination"] = {
"notes": """### You rarely need the exact word
A synonym question asks for the **nearest** meaning. You do not have to recall a dictionary definition; you only have to remove three options that are wrong in an obvious way. Options are built to fail on one of four filters, so run the filters in order.

### Filter 1: part of speech
Decide what the stem word is: ADAPTABLE ends in -able (adjective), ABOLISH is a verb, ABOLITION a noun.
- An adjective answer should be an adjective or adjective phrase.
- Trap: for the verb RELEASE, the noun 'freedom' is planted. It is related but not a match in part of speech.
If an option is a different part of speech, remove it unless no better option remains.

### Filter 2: class or family
The nearest meaning must belong to the **same class of idea**.
- DELUGE (a flood of water) → drizzle, drought and mist are all water or weather words, but only *flood* shares the class 'a large amount of water'.
- Remove options from a different class first: for DELUGE, an option like 'quarrel' dies instantly.

### Filter 3: degree
Within the right class, match the strength.
- TRIVIAL = of very little importance. 'Serious' and 'vital' are importance words of the wrong degree; the answer sits at the *low* end.
- ENORMOUS = huge; a mild word like 'big' is usually too weak when the stem has an extreme word.
If the stem word is extreme (enormous, furious, exhausted), the answer is normally extreme too.

### Filter 4: charge (positive or negative)
Note whether the word is pleasant or unpleasant:
- NOTORIOUS = famous for something bad → the answer must be negative (infamous), so 'well known' alone is not enough.
- HOSTILE, timid, generous, warm — each carries a charge. Keep only options with the same charge.

### If a sentence is given
Some papers print the word inside a sentence. The sentence overrides everything: SPEED can mean 'hurry' in one sentence and 'fastness' in another. Read the sentence, decide what the word does *there*, then match. Never answer from the word's most common meaning alone when a context is supplied.

### Order of operations in the exam
1. Say the stem word's meaning to yourself in one plain word.
2. Part of speech — remove mismatches.
3. Class — remove unrelated ideas.
4. Degree and charge — remove the survivors that are too weak or wrongly toned.
5. Choose the remaining option and read it back: "X means about the same as Y" should sound true.

### Quick revision
- Four filters in order: part of speech → class → degree → charge.
- Extreme stem word → extreme answer.
- NOTORIOUS is negative; its answer must be negative.
- With a sentence, the context meaning wins over the dictionary meaning.
- You need the *nearest*, not the perfect, match.
""",
"patterns": [
 P("sel-p1", "Part-of-speech filter", "very common",
   "Among the options one is a noun where the stem is a verb (or similar mismatch), often a related word like freedom for RELEASE.",
   "1. Fix the stem's part of speech from its ending and its use.\n2. Remove options of a different part of speech.\n3. Choose among the survivors.\n\n*Why it works:* a synonym must be replaceable in the same sentence slot.",
   "*Nearest in meaning to RELEASE*", "Verb → **set free**. 'Freedom' is the same family but a noun — the planted trap."),
 P("sel-p2", "Degree match", "common",
   "Two options share the right class but differ in strength (serious vs vital vs unimportant for TRIVIAL).",
   "1. Place the stem word on its scale (weak — strong; small — huge).\n2. Note whether it sits at an extreme.\n3. Pick the option at the same position on the scale.\n\n*Why it works:* nearest meaning means nearest in strength too.",
   "*Nearest in meaning to TRIVIAL*", "Low importance → **unimportant**. Serious and vital sit at the wrong end."),
 P("sel-p3", "Charge (tone) match", "common",
   "The stem is clearly positive or negative (hostile, notorious, generous), and one option has the right idea but the wrong tone.",
   "1. Label the stem + or -.\n2. Label each surviving option + or -.\n3. Keep only options with the same label.\n\n*Why it works:* a positive word can never be the nearest meaning of a negative one.",
   "*Nearest in meaning to HOSTILE*", "Negative → **unfriendly**. Calm and shy are not the charge of an enemy."),
 P("sel-p4", "Meaning from the sentence context", "common",
   "The word appears in CAPITALS inside a sentence, and the options are possible meanings.",
   "1. Read the whole sentence and say what the capitalised word does there.\n2. Ignore other meanings you know for that word.\n3. Match the sentence meaning to one option.\n\n*Why it works:* the examiner keys the answer to the context, not the dictionary.",
   "*His reply was LACONIC — just two words.*", "Two-word reply → **using very few words**."),
],
}

S["ant-prefix-flip"] = {
"notes": """### What 'most opposite' really asks
An antonym question gives a word and asks for the option **furthest** from it in meaning. Two words can both be unrelated to the stem; only one is its true opposite. Your job is to recognise which kind of opposite the exam wants.

### Three kinds of opposite
1. **Complementary** — one or the other, nothing between: alive / dead, present / absent, accept / refuse.
2. **Gradable** — two ends of a scale: hot / cold, maximum / minimum, abundant / scarce, minor / major.
3. **Direction or role** — opposite movements or roles: buy / sell, ascend / descend, employer / employee, immigrate / emigrate.

Before looking at the options, decide the kind: it stops you from choosing a merely *different* word.

### The prefix-flip trap
The most common wrong option is a word that **looks** opposite because of its prefix but actually means the same as the stem:
- **invaluable** = extremely valuable (so its opposite is worthless, and 'valuable' is the trap).
- **inflammable** = easily set on fire (opposite: fireproof; 'flammable' means the same, not the opposite).
- **disinterested** = impartial (not 'uninterested').
- **restive** = restless (not calm).
Rule: never build the opposite by sticking a prefix on the stem word. Know the stem's real meaning first, then find its opposite.

### The synonym trap
Every antonym question also carries at least one **synonym** of the stem among the options. For SUPERFLUOUS (more than needed), the options include extra and surplus — both mean the same as the stem. Learn to laugh at them: in an antonym question, a synonym option is always wrong. This one observation usually removes two of the four options immediately.

### Keep the part of speech
The opposite should be usable in the same slot: the opposite of the adjective TRANSPARENT is the adjective opaque, not the noun 'opacity'. If two options both fit the meaning, prefer the one matching the part of speech.

### Do not confuse opposite with absence
The opposite must **reverse** the meaning, not merely remove it:
- For GENEROUS, 'careful' is not enough; the reverse idea is mean or stingy.
- For BRAVE, 'calm' is not the opposite; cowardly is.
Ask: does this option describe the other end of the same scale, or just a different street?

### Quick revision
- Three kinds: complementary, gradable, direction/role.
- Never flip the prefix: invaluable = very valuable; inflammable = burns easily.
- A synonym in the options is always wrong here — strike it out first.
- Match the part of speech of the stem.
- The opposite must reverse the idea, not drop it.
""",
"patterns": [
 P("apf-p1", "True opposite on the same scale", "very common",
   "The stem and the right answer sit at the two ends of one scale; two options are unrelated words.",
   "1. Name the scale the stem lives on (quantity, size, temperature, willingness).\n2. Name the other end of the scale in plain words.\n3. Pick the option that sits at that other end.\n\n*Why it works:* antonyms are scale-mates, so fixing the scale fixes the answer.",
   "*Most opposite to SCARCE*", "Scale = quantity. Other end = plenty → **plentiful**."),
 P("apf-p2", "Prefix-flip false antonym", "very common",
   "One option is built by flipping a prefix (flammable, valuable) and looks like the opposite of the stem.",
   "1. Recall the stem's real meaning from memory, not from its shape.\n2. Check the false-flip list (invaluable, inflammable, disinterested, restive).\n3. Choose the option that genuinely reverses that meaning.\n\n*Why it works:* these words are planted exactly because their shape lies.",
   "*Most opposite to INVALUABLE*", "Invaluable = extremely valuable → opposite **worthless**. 'Valuable' is the shape trap."),
 P("apf-p3", "Strike the synonyms first", "very common",
   "Two or three options mean the same as the stem (extra, surplus, spare for superfluous).",
   "1. In an antonym question, delete every option that means the same as the stem.\n2. What remains is usually one true opposite plus one unrelated word.\n3. Choose the one on the same scale.\n\n*Why it works:* examiners always seed synonym decoys; removing them halves the work.",
   "*Most opposite to SUPERFLUOUS*", "Extra and surplus are synonyms → strike both → **essential** remains."),
 P("apf-p4", "Opposite with matching part of speech", "common",
   "Two options carry opposite ideas but different forms (opaque vs opacity; optimistic vs optimism).",
   "1. Fix the stem's part of speech.\n2. Prefer the opposite that shares it.\n3. Only fall back to the other form if nothing matches.\n\n*Why it works:* the replaced word must fit the same sentence slot.",
   "*Most opposite to ASCEND*", "Verb → **descend**. Rise and climb are synonyms; they fail the meaning check first anyway."),
],
}

S["syn-ant-strategy"] = {
"notes": """### What the exam actually asks
In SSC, Railway and Banking papers, vocabulary appears in three shapes: a bare word for its synonym, a bare word for its antonym, and a word in CAPITALS inside a sentence. Tier 1 usually carries one synonym and one antonym; each is a 15-second mark with no calculation. This subtopic trains the routine that handles all three shapes.

### The 15-second routine
1. **Tone first**: say whether the word is positive, negative or neutral. This alone kills two options most of the time.
2. **Part of speech**: adjective, verb or noun — the answer must match.
3. **Root check**: if the word is unknown, try the prefix/root method.
4. **Eliminate to two**: strike the synonyms (in an antonym question) or the opposites (in a synonym question), and the unrelated word.
5. **Choose the nearest**: between the last two, pick the one closer in strength and tone, not the fancier word.

### Sentence-based items
When the word sits in a sentence, the sentence is the boss:
- Read the full sentence and paraphrase the capitalised word in one plain word.
- Then apply the same routine to your plain word, not to the printed word.
Example: *His GAUNT face showed months of illness.* Gaunt here = thin and bony; the most opposite option is plump, while thin and pale are meaning traps.

### Building the word bank
Vocabulary marks come from memory, so the plan is a bank, not brilliance:
- Add every new word from every mock test to a personal sheet with its meaning, one synonym, one antonym.
- Revise the sheet weekly; words you miss twice move to a small weak list.
- Learn words in opposite pairs (barren/fertile, scarce/plentiful, clement/harsh) — one memory slot stores two answers.
- High-frequency exam words worth banking: lucid, tenacious, vigilant, frugal, notorious, imminent, futile, mitigate, squander, abundant, indispensable.

### Guessing rules
- In a synonym question, an option that is the *opposite* of the stem is wrong; so is a word from a different class of idea.
- In an antonym question, any synonym option is wrong — strike it without reading further.
- If two options survive, the shorter plainer word is more often the keyed answer than a rare showy word.
- Never leave a vocabulary blank in exams without negative marking pressure issues — these are among the fastest questions on the paper, so bank them early and save time for grammar.

### Quick revision
- Routine: tone → part of speech → root → eliminate → nearest.
- Sentence given: paraphrase the capital word first.
- Learn in opposite pairs; keep a mock-test word sheet and revise weekly.
- Antonym question: synonyms are always wrong. Synonym question: opposites are always wrong.
- Prefer the plainer survivor over the showy one.
""",
"patterns": [
 P("sas-p1", "Synonym of a word inside a sentence", "very common",
   "A sentence with the key word in CAPITALS; the options are possible meanings.",
   "1. Paraphrase the capital word from the sentence's sense.\n2. Apply tone and part-of-speech filters.\n3. Match the paraphrase to the options.\n\n*Why it works:* the sentence fixes the sense the examiner keyed.",
   "*His account of the accident was COHERENT.*", "Account that hangs together → **clear and logical**."),
 P("sas-p2", "Antonym of a word inside a sentence", "very common",
   "Same shape as the synonym-in-sentence item but the stem asks for the most opposite option.",
   "1. Paraphrase the capital word.\n2. Strike every option that means the same as the paraphrase.\n3. Choose the remaining option that truly reverses it.\n\n*Why it works:* the synonym strike removes the planted decoys instantly.",
   "*His GAUNT face showed months of illness.*", "Gaunt = thin and bony → most opposite **plump**."),
 P("sas-p3", "Mixed drill: one stem, both directions", "common",
   "A set mixes synonym and antonym items; the habit to train is checking the direction asked before reading options.",
   "1. Read the command word first: nearest or most opposite.\n2. Only then look at the stem word and fix its tone.\n3. Apply the matching strike rule (synonyms out for antonyms; opposites out for synonyms).\n\n*Why it works:* most vocabulary errors are direction errors, not knowledge errors.",
   "*Most opposite to VICTORIOUS*", "Command = opposite → **defeated**. Triumphant and successful are synonym decoys."),
 P("sas-p4", "Unknown word: root plus context together", "common",
   "The capital word is unfamiliar, but the sentence and the word's parts each give a clue.",
   "1. Split the word for a prefix or root (aud = hear, port = carry).\n2. Check the split against the sentence: does 'able to be heard' fit the slot?\n3. Choose the option the two clues agree on.\n\n*Why it works:* two weak clues pointing the same way are strong together.",
   "*Even in the last row the lecturer's voice was AUDIBLE.*", "aud = hear → **able to be heard**."),
],
}
