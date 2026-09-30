"""Readable rewrite: English > Synonyms & Antonyms (4 subtopics). Idempotent. Run with Python312."""
import sys
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parent))
from _rd_common import pat, mis, trick, sub, apply  # noqa: E402

SUBS = {}

# ---------------------------------------------------------------- 1. root words
SUBS["syn-root-word-method"] = sub(
    concept=("Most hard English words are built from small parts: a prefix, a root and a suffix. "
             "If you know about 40 of these parts, you can work out the meaning of words you have never seen. "
             "Use this method to guess an unknown word in a synonym or antonym question."),
    notes=r"""
### Why roots help
An unknown word is not a dead end. Most exam words are built from **prefix + root + suffix**.

Take MALEVOLENT. *Male-* means bad. *Vol* means wish. So the word means "wishing bad". Nearest meaning: hostile.

You do not need the whole dictionary. You only need to remove options that clearly clash with the parts you know.

### Prefixes to know
| Prefix | Meaning | Example |
|---|---|---|
| in-, im-, il-, ir-, un-, dis- | not | illegible, irregular |
| mal- | bad | malicious, malnutrition |
| bene- | good, well | benefactor, benevolent |
| circum- | around | circumvent, circumference |
| pre- / post- | before / after | precaution, postpone |
| sub- / super- | under / above | subordinate, supervise |
| mono- / poly- | one / many | monotone, polyglot |
| auto- | self | autobiography, autograph |

> **Tip:** A good prefix (bene-, eu-) and a bad prefix (mal-, dys-) point in opposite directions. Use this to remove options fast.

### Roots to know
| Root | Meaning | Example |
|---|---|---|
| spect / spec | look | inspect, spectator |
| vis / vid | see | visible, evident |
| aud | hear | audible, audience |
| dict | say | dictate, contradict |
| loqu | speak | eloquent, soliloquy |
| port | carry | transport, portable |
| tract | pull | attract, extract |
| chron | time | chronological, synchronise |
| anim | mind, spirit | unanimous, magnanimous |
| magn | great | magnitude, magnanimous |
| cred | believe | credible, credulous |
| rupt | break | interrupt, bankrupt |
| path | feeling | sympathy, apathy |
| phil | love | philanthropy, bibliophile |
| phob | fear | phobia, acrophobia |
| ver | truth | verify, veracity |

### Four steps to decode a word
1. **Split** the word: MAGNANIMOUS = magn + anim + ous.
2. **Translate** each part: great + spirit.
3. **Join** the meanings: great-spirited, so generous and forgiving.
4. **Match** with the options, and check the part of speech.

> **Example:** SOLILOQUY = soli (alone) + loqu (speak). It means speaking alone, as an actor does on stage.

### Suffixes tell the word class
Endings show whether a word is a noun, verb or adjective.
- -ous, -ful, -ive, -able: adjectives (dangerous, helpful).
- -tion, -ment, -ness: nouns (creation, movement).
- -ise, -ify: verbs (simplify).

Options often mix word classes. Matching the class removes one or two of them.

### Words that fool you
Five famous words look like they hold a helpful root, but the meaning is different.
- **enervate** means to weaken. It does not mean to give energy.
- **restive** means restless and hard to control. It does not mean calm.
- **inflammable** means easily set on fire. It does not mean "cannot burn".
- **invaluable** means extremely valuable. It does not mean worthless.
- **noisome** means foul-smelling. It has nothing to do with noise.

> **Watch:** If you already know a word, trust your memory over the root. Use roots only to guess unknown words.
""",
    patterns=[
        pat("srm-p1", "Prefix gives the direction", "very common",
            "The word starts with a strong prefix (mal-, bene-, in-, un-, dis-). Some options start with the opposite prefix.",
            ["Read the prefix: mal = bad, bene = good, in/un/dis = not.",
             "Decide if the meaning is good or bad, or a yes or a no.",
             "Remove options that point the other way.",
             "Pick the nearest of the rest."],
            "Prefixes keep the same meaning in thousands of words.",
            "Nearest in meaning to BENEVOLENT: (a) hostile (b) kindly (c) careless (d) clever",
            ["bene = good, so the word is a warm word.", "Hostile and careless are cold or bad. Remove them.",
             "Kindly matches 'wishing good'."], "(b) kindly"),
        pat("srm-p2", "Root gives the core meaning", "very common",
            "The word holds a root you know (spect, port, dict, chron, anim, magn), even if the whole word is new.",
            ["Cut off the prefix and suffix.", "Recall what the root means.",
             "Join the meanings of all the parts.", "Choose the option built on that idea."],
            "Latin and Greek roots keep their meaning in every English word that borrows them.",
            "Nearest in meaning to MAGNANIMOUS: (a) generous (b) proud (c) narrow-minded (d) timid",
            ["magn = great, anim = spirit.", "Great in spirit means big-hearted and generous."], "(a) generous"),
        pat("srm-p3", "Chunk a long word", "common",
            "The word is long and looks technical (circumvent, chronological, indispensable).",
            ["Cut the word where a known piece ends.", "Translate each piece into plain words.",
             "Join them into one short idea.", "Match that idea to an option."],
            "Long exam words are usually two or three small pieces stuck together.",
            "Nearest in meaning to CIRCUMVENT: (a) surround (b) bypass (c) confront (d) protect",
            ["circum = around, vent = come.", "To come around something means to go past it.",
             "Bypass matches. Confront is the opposite."], "(b) bypass"),
        pat("srm-p4", "False-root trap word", "common",
            "An option repeats the surface root: energise for enervate, calm for restive, worthless for invaluable.",
            ["Check the stem against the five fixed words.", "If it is on the list, use its fixed meaning.",
             "Treat the option that repeats the surface root as the trap."],
            "These five words are famous because their shape misleads.",
            "Nearest in meaning to ENERVATE: (a) energise (b) weaken (c) excite (d) strengthen",
            ["Enervate looks like energy, but it means to drain strength.", "Energise, excite and strengthen all point the wrong way.",
             "Weaken is the fixed meaning."], "(b) weaken"),
        pat("srm-p5", "Root family across two words", "occasional",
            "You know a root from one word, and the exam gives a new word with the same root.",
            ["Find the root in the new word.", "Think of a word you know with the same root.",
             "Borrow its meaning.", "Pick the option that fits."],
            "One known word unlocks its whole family.",
            "Nearest in meaning to LOQUACIOUS: (a) silent (b) talkative (c) lonely (d) angry",
            ["loqu = speak, as in eloquent.", "A word full of 'speak' means talkative.", "Silent is the opposite."],
            "(b) talkative"),
    ],
    mistakes=[
        mis("Skipping the prefix and guessing from the root alone.", "Read the prefix first. It tells you the direction of the meaning."),
        mis("Trusting a root when you already know the word.", "Your memory of the word beats the root. Roots are for unknown words."),
        mis("Picking energise for ENERVATE because it looks like energy.", "Learn the five fixed words: enervate, restive, inflammable, invaluable, noisome."),
        mis("Ignoring the word class.", "Check -ous, -tion, -ise endings. Remove options of a different class."),
        mis("Learning roots as a list only.", "Attach each root to two real words. Use the words to recall the root."),
    ],
    revision=[
        "Split, translate, join, match, check the word class.",
        "Prefixes: in/un/dis = not, mal = bad, bene = good, circum = around.",
        "Roots: spect = look, port = carry, dict = say, chron = time, anim = spirit, tract = pull, aud = hear.",
        "Five fixed words: enervate, restive, inflammable, invaluable, noisome.",
        "Good prefix and bad prefix point in opposite directions.",
        "Roots are a guessing tool. Known words come first.",
    ],
    tricks=[
        trick("Split, then eliminate",
              "Cut the unknown word at its joins, translate the parts you know, and remove options that clash. One sure root can remove two options.",
              "BENEVOLENT means: (a) cruel (b) kindly (c) talkative (d) angry",
              ["bene = good.", "Cruel and angry clash with good.", "Kindly stays."], "(b) kindly"),
        trick("Learn roots as families",
              "Learn words in root groups, not in alphabet order. The dict family: dictate, verdict, predict, contradict. The loqu family: eloquent, loquacious, soliloquy."),
        trick("Warm or cold",
              "Roots carry a feeling. Bene-, eu- and am- are warm. Mal-, dys-, phob- and mis- are cold. When stuck, pick an option with the same feeling."),
    ],
)

# ---------------------------------------------------------------- 2. elimination
SUBS["syn-elimination"] = sub(
    concept=("A synonym question asks for the word closest in meaning. You do not need the exact dictionary meaning. "
             "You only need to remove three options that fail one of four filters: word class, idea class, strength and tone."),
    notes=r"""
### You need the nearest, not the perfect
A synonym is a word with almost the same meaning. The question asks for the **nearest** one.

Each wrong option is built to fail one filter. Run the filters in order and three options will fall out.

### Filter 1: word class
First decide if the given word is a noun, verb or adjective.
- ABOLISH is a verb. ABOLITION is a noun. ADAPTABLE is an adjective.
- The answer must be the same class.

Example: for the verb RELEASE, the noun "freedom" is a planted trap. It is related, but it is the wrong class.

### Filter 2: idea class
The answer must belong to the same group of ideas.

Take DELUGE, a flood of water. Drizzle and mist are also water words, but only *flood* means a very large amount of water.

Remove options from a different group first. For DELUGE, an option like "quarrel" goes at once.

### Filter 3: strength
Inside the right group, match the strength.
- TRIVIAL means of very little importance. It sits at the low end. Serious and vital are the wrong end.
- ENORMOUS means huge. The mild word "big" is too weak.

> **Rule:** If the given word is extreme (enormous, furious, exhausted), the answer is also extreme.

### Filter 4: tone
Say if the word is pleasant, unpleasant or neutral.
- NOTORIOUS means famous for something bad. Its answer must be negative, like *infamous*.
- "Celebrated" is also famous, but the tone is good. It is wrong.

SLIM and skinny both mean thin. Slim is pleasant. Skinny is not. Options are often chosen across this line.

### When a sentence is given
Some papers print the word inside a sentence. The sentence wins over the dictionary.
1. Read the whole sentence.
2. Say what the capital word means *there* in one plain word.
3. Match that plain word to an option.

> **Watch:** Association is not synonymy. Cinema goes with film, but the two words are not synonyms. Ask: can one word replace the other?

### Filters at work
| Given word | Wrong option | Filter that removes it |
|---|---|---|
| ABOLISH (verb) | abolition | word class |
| DELUGE | quarrel | idea class |
| TRIVIAL | vital | strength |
| NOTORIOUS | celebrated | tone |
| FUTILE | difficult | overlap |

Read each row as a small drill. Cover the last column and name the filter yourself.

Most questions need only two filters. Word class and tone remove the most options for the least effort, so try them first.

### The 20-second routine
1. Say the meaning in one plain word.
2. Remove wrong word classes.
3. Remove wrong idea groups.
4. Remove wrong strength or tone.
5. Read the answer back: "X means about the same as Y".
""",
    patterns=[
        pat("sel-p1", "Word-class filter", "very common",
            "One option is a noun where the given word is a verb, often a related word such as freedom for RELEASE.",
            ["Fix the class of the given word from its ending and use.", "Remove options of another class.",
             "Choose among what is left."],
            "A synonym must fit in the same slot of a sentence.",
            "Nearest in meaning to RELEASE: (a) freedom (b) set free (c) prison (d) hold",
            ["RELEASE is a verb.", "Freedom and prison are nouns. Remove them.", "Hold is a verb but the opposite. Set free stays."],
            "(b) set free"),
        pat("sel-p2", "Strength match", "common",
            "Two options are in the right group but differ in force (serious, vital, unimportant for TRIVIAL).",
            ["Place the given word on a scale from weak to strong.", "Note whether it sits at an end.",
             "Pick the option at the same spot."],
            "Nearest meaning also means nearest strength.",
            "Nearest in meaning to TRIVIAL: (a) serious (b) vital (c) unimportant (d) costly",
            ["TRIVIAL means of little importance.", "Serious and vital are at the high end.", "Unimportant is at the low end."],
            "(c) unimportant"),
        pat("sel-p3", "Tone match", "common",
            "The given word is clearly pleasant or unpleasant (hostile, notorious, generous), and one option has the idea in the wrong tone.",
            ["Mark the given word + or -.", "Mark each option + or -.", "Keep only options with the same mark."],
            "A pleasant word can never be the nearest meaning of an unpleasant one.",
            "Nearest in meaning to HOSTILE: (a) unfriendly (b) calm (c) shy (d) cheerful",
            ["HOSTILE is negative.", "Calm and cheerful are positive. Shy is a different idea.", "Unfriendly is negative and fits."],
            "(a) unfriendly"),
        pat("sel-p4", "Meaning from the sentence", "common",
            "The word is in CAPITALS inside a sentence, and the options are possible meanings.",
            ["Read the whole sentence.", "Say in one plain word what the capital word does there.",
             "Ignore other meanings you know for it.", "Match your plain word to an option."],
            "The answer is keyed to the sentence, not to the dictionary.",
            "His reply was LACONIC, just two words. (a) rude (b) brief (c) angry (d) loud",
            ["A two-word reply is very short.", "Laconic means using few words.", "Brief matches."], "(b) brief"),
        pat("sel-p5", "Overlap, not association", "common",
            "Options are related to the given word but do not mean the same (difficult, risky, tiring for FUTILE).",
            ["Say the meaning in your own words.", "Ask if each option can replace the word in a sentence.",
             "Keep the option that overlaps most."],
            "Related words are decoys. Only a true overlap is a synonym.",
            "Nearest in meaning to FUTILE: (a) difficult (b) pointless (c) risky (d) tiring",
            ["FUTILE means it has no chance of success.", "Difficult, risky and tiring can still succeed.", "Pointless means no use. It overlaps."],
            "(b) pointless"),
    ],
    mistakes=[
        mis("Choosing an option because it is related to the word.", "Choose the option that can replace the word in a sentence."),
        mis("Picking a noun for a verb because it looks close.", "Check the word class before the meaning."),
        mis("Taking a mild word for an extreme one (big for ENORMOUS).", "Match strength. An extreme word needs an extreme answer."),
        mis("Ignoring the tone (celebrated for NOTORIOUS).", "Mark the word + or - first. Keep only options with the same mark."),
        mis("Answering from the most common meaning when a sentence is given.", "Read the sentence and answer for the meaning used there."),
    ],
    revision=[
        "Four filters in order: word class, idea class, strength, tone.",
        "Extreme word means extreme answer.",
        "NOTORIOUS is negative, so the answer is negative (infamous).",
        "With a sentence, the sentence meaning wins.",
        "Related is not the same as synonym. Test by replacing.",
        "You need the nearest match, not a perfect one.",
    ],
    tricks=[
        trick("The replace test",
              "The right synonym can replace the word in most sentences. If the sentence changes meaning, the option is only related.",
              "ELOQUENT: (a) quiet (b) articulate (c) wealthy (d) careless",
              ["Eloquent means speaking well and with force.", "Articulate can replace it.", "Quiet is a decoy that is close to the opposite."],
              "(b) articulate"),
        trick("Tone sorts half the options",
              "Mark the given word + or - (notorious is -, celebrated is +). Options with the other mark can go without more thought."),
        trick("The strength ruler",
              "Draw a line from mild to extreme. Put the word and the two surviving options on it. The option at the same mark wins."),
    ],
)

# ---------------------------------------------------------------- 3. antonyms
SUBS["ant-prefix-flip"] = sub(
    concept=("An antonym is a word with the opposite meaning. The right option reverses the idea. "
             "It does not just differ, and it does not just remove the idea. "
             "Beware of words that look like opposites because of a prefix but really mean the same."),
    notes=r"""
### The opposite must reverse the idea
The question asks for the option that is **furthest** in meaning. Two words can both be unrelated to the given word. Only one is a true opposite.

Test with a pair of sentences.
- The manager praised the plan. / The manager criticised the plan. This is a clean contradiction.
- "Ignored" is not a contradiction of praised. It only removes the praise.

> **Rule:** An antonym stands at the other end of the same scale. It does not stand beside the word.

### Three kinds of opposite
| Kind | What it means | Examples |
|---|---|---|
| Complementary | One or the other, nothing between | alive / dead, present / absent |
| Gradable | Two ends of a scale | hot / cold, abundant / scarce |
| Direction or role | Opposite moves or roles | buy / sell, ascend / descend |

Decide the kind before you read the options. It stops you choosing a word that is only different.

### Prefixes that flip meaning
| Prefix | Effect | Examples |
|---|---|---|
| un- | not, reverse | unfair, untie |
| in- im- il- ir- | not | inactive, impossible, illogical, irregular |
| dis- | opposite, apart | disagree, disorder |
| non- | not | nonstop, nonviolent |
| mis- | wrongly | misjudge, misplace |
| de- | down, reverse | decrease, deflate |
| -less | without | harmless, restless |

The spelling in-, im-, il-, ir- follows the next sound: impossible, illegal, irregular.

### Prefix flips that lie
Some words look like opposites because of a prefix, but they mean the same as the stem.
- **invaluable** means extremely valuable. Its opposite is worthless.
- **inflammable** means easily set on fire. Its opposite is fireproof.
- **disinterested** means impartial.
- **restive** means restless, not calm.

> **Watch:** Never build an opposite by sticking a prefix on the stem. Know the true meaning first.

### Strike the synonyms first
Every antonym question hides one or two **synonyms** of the given word. For SUPERFLUOUS (more than needed), extra and surplus are synonyms. In an antonym question they are always wrong. Strike them out first.

### Keep the word class
The opposite of the adjective TRANSPARENT is the adjective *opaque*, not the noun "opacity". If two options both fit the meaning, choose the one in the same class.

### Word pairs worth banking
agree / disagree, permanent / temporary, expand / contract, vacant / occupied, native / foreign, superior / inferior, optimist / pessimist.

Learn each pair together. One pair gives you a synonym answer on one day and an antonym answer on another.

### A quick worked check
Question: most opposite to GENEROUS.
1. Kind of opposite: gradable. It is a scale of giving.
2. Strike synonyms such as kind and giving.
3. "Careful" only drops the idea. It does not reverse it.
4. Mean or stingy reverses it. Pick that.
""",
    patterns=[
        pat("apf-p1", "Opposite on the same scale", "very common",
            "The given word and the answer sit at two ends of one scale. Two options are unrelated words.",
            ["Name the scale (size, amount, warmth, willingness).", "Name the other end in plain words.",
             "Pick the option at that end."],
            "Antonyms are scale-mates, so the scale gives the answer.",
            "Most opposite to SCARCE: (a) rare (b) plentiful (c) costly (d) few",
            ["SCARCE is on the scale of amount, at the low end.", "Rare and few are also low. They are synonyms.", "Plentiful is the high end."],
            "(b) plentiful"),
        pat("apf-p2", "Prefix-flip false opposite", "very common",
            "One option is built by flipping a prefix (valuable, flammable) and looks like the opposite of the given word.",
            ["Recall the true meaning of the given word.", "Check the list: invaluable, inflammable, disinterested, restive.",
             "Pick the option that really reverses that meaning."],
            "These words are planted because their shape lies.",
            "Most opposite to INVALUABLE: (a) valuable (b) priceless (c) worthless (d) costly",
            ["INVALUABLE means extremely valuable.", "Valuable, priceless and costly are near-synonyms.", "Worthless is the opposite."],
            "(c) worthless"),
        pat("apf-p3", "Strike the synonyms first", "very common",
            "Two or three options mean the same as the given word (extra, surplus, spare for SUPERFLUOUS).",
            ["Delete every option that means the same as the given word.", "Usually one true opposite and one unrelated word remain.",
             "Pick the one on the same scale."],
            "Question setters always plant synonym decoys. Removing them halves the work.",
            "Most opposite to SUPERFLUOUS: (a) extra (b) surplus (c) essential (d) spare",
            ["SUPERFLUOUS means more than needed.", "Extra, surplus and spare all mean the same. Strike them.", "Essential means needed. It is the opposite."],
            "(c) essential"),
        pat("apf-p4", "Same word class", "common",
            "Two options carry the opposite idea but in different forms (opaque or opacity, descend or descent).",
            ["Fix the class of the given word.", "Prefer the option in the same class.", "Use the other form only if nothing matches."],
            "The opposite must fit the same slot in a sentence.",
            "Most opposite to ASCEND: (a) rise (b) climb (c) descend (d) descent",
            ["ASCEND is a verb meaning go up.", "Rise and climb are synonyms. Strike them.", "Descend and descent both mean down. Descend is the verb."],
            "(c) descend"),
        pat("apf-p5", "Direction or role pair", "common",
            "The given word is one move in a pair (borrow and lend, buy and sell).",
            ["Ask: who does the other side of this act?", "Name the reverse move in one word.", "Pick that option."],
            "In these pairs the opposite is the other person's action.",
            "Most opposite to BORROW: (a) lend (b) take (c) keep (d) ask",
            ["To borrow is to take something to use for a time.", "The reverse move is to give it for a time.", "That is lend."],
            "(a) lend"),
    ],
    mistakes=[
        mis("Choosing a word that only differs (careful for BRAVE).", "Pick the word at the other end of the scale (cowardly)."),
        mis("Building the opposite by adding a prefix (valuable for INVALUABLE).", "Learn the true meaning first. Invaluable means very valuable."),
        mis("Choosing a synonym because it 'feels close'.", "Strike every synonym at once. They are decoys."),
        mis("Taking absence as opposition (ignore for PRAISE).", "The opposite must reverse the idea (criticise)."),
        mis("Choosing a noun for an adjective (opacity for TRANSPARENT).", "Match the word class. The answer is opaque."),
    ],
    revision=[
        "Three kinds: complementary, gradable, direction or role.",
        "Invaluable means very valuable. Inflammable means burns easily.",
        "Strike synonyms first. They are always wrong in an antonym question.",
        "Match the word class of the given word.",
        "The opposite reverses the idea. It does not drop it.",
        "Bank words in pairs: agree/disagree, permanent/temporary.",
    ],
    tricks=[
        trick("Pair-of-sentences test",
              "Put the word and each option in the same short sentence. The option that gives a real contradiction is the antonym.",
              "Antonym of CORDIAL: (a) warm (b) polite (c) hostile (d) sincere",
              ["A cordial welcome and a hostile welcome contradict each other.", "A welcome can be cordial and polite, or cordial and sincere.",
               "So hostile is the opposite."], "(c) hostile"),
        trick("Guess the flip first",
              "Before reading the options, guess the opposite yourself (conformity, then nonconformity). If your guess is in the options, mark it."),
        trick("Absence is not opposition",
              "Cross out options that only lack the quality. Careful does not fight brave. Cowardly does."),
    ],
)

# ---------------------------------------------------------------- 4. strategy
SUBS["syn-ant-strategy"] = sub(
    concept=("Vocabulary questions are short and give quick marks. There is often one synonym and one antonym per paper. "
             "The plan is a 15-second routine in the exam, plus 15 minutes of daily word practice before it."),
    notes=r"""
### What the exam asks
Vocabulary appears in three shapes.
- A bare word, and you pick its synonym.
- A bare word, and you pick its antonym.
- A word in CAPITALS inside a sentence.

Each item takes about 15 seconds. There is no calculation. Marks depend on memory, so the plan is a word bank, not brilliance.

### The 15-second routine
1. **Direction.** Read the command first: nearest or most opposite.
2. **Tone.** Say if the word is positive, negative or neutral. This removes two options most of the time.
3. **Word class.** Adjective, verb or noun. The answer must match.
4. **Roots.** If the word is new, split it into prefix and root.
5. **Eliminate.** Strike the wrong-direction options and the unrelated one.
6. **Choose.** Pick the closer option in strength and tone.

> **Watch:** Most vocabulary errors are direction errors, not knowledge errors. Read "nearest" or "opposite" before anything else.

### Sentence-based items
When the word sits in a sentence, the sentence decides.
- Read the full sentence.
- Say the capital word in one plain word.
- Run the routine on that plain word.

> **Example:** His GAUNT face showed months of illness. Gaunt here means thin and bony. The most opposite option is plump.

### Build a word bank
- Add each new word from mock tests to a sheet: meaning, one synonym, one antonym.
- Revise the sheet once a week. Words you miss twice go on a short weak list.
- Learn words in opposite pairs: barren and fertile, scarce and plentiful. One memory slot stores two answers.
- Say each word in a sentence of your own. Using a word fixes it better than reading it.

Words worth banking: lucid, tenacious, vigilant, frugal, notorious, imminent, futile, mitigate, squander, abundant, indispensable.

### Weekly plan
| When | What |
|---|---|
| Daily, 15 minutes | 10 new words, read aloud, one sentence each |
| Daily | One root and its relatives |
| Weekly | A test of 30 mixed words, aim for 26 or more |
| After every mock | Note each missed word |

### In the exam room
- Do vocabulary early. It is quick and it does not need a long read.
- Do not spend more than 20 seconds on any one item.
- If a word is new, judge its tone from its parts and pick an option with the same tone.
- Mark unknown items and return only if time is left.

### Guessing rules
- Synonym question: an option that is the opposite of the word is wrong.
- Antonym question: any synonym option is wrong.
- If two options remain, the plainer word is more often the key than a rare, showy one.
- Do not leave a vocabulary item blank. An informed guess is better than nothing.
""",
    patterns=[
        pat("sas-p1", "Synonym of a word in a sentence", "very common",
            "A sentence has the key word in CAPITALS. The options are possible meanings.",
            ["Say the capital word in one plain word from the sentence.", "Use the tone and word-class filters.",
             "Match your plain word to the options."],
            "The sentence fixes the meaning the examiner has in mind.",
            "His account of the accident was COHERENT. (a) clear and logical (b) confused (c) lengthy (d) angry",
            ["An account that hangs together is easy to follow.", "Confused is the opposite. Lengthy and angry do not fit.",
             "Clear and logical fits."], "(a) clear and logical"),
        pat("sas-p2", "Antonym of a word in a sentence", "very common",
            "The same shape as the last one, but the question asks for the most opposite word.",
            ["Say the capital word in one plain word.", "Strike every option that means the same.",
             "Choose the option that truly reverses it."],
            "Striking the synonyms removes the decoys at once.",
            "His GAUNT face showed months of illness. Most opposite: (a) thin (b) plump (c) pale (d) tired",
            ["Gaunt here means thin and bony.", "Thin is a synonym. Pale and tired are related, not opposite.", "Plump reverses it."],
            "(b) plump"),
        pat("sas-p3", "Read the direction first", "common",
            "A set mixes synonym and antonym items. Check whether the question says nearest or most opposite.",
            ["Read the command word first.", "Then look at the given word and mark its tone.",
             "Strike opposites in a synonym question. Strike synonyms in an antonym question."],
            "Direction slips cost more marks than missing words.",
            "Most opposite to FRUGAL: (a) thrifty (b) wasteful (c) poor (d) careful",
            ["The command says most opposite.", "FRUGAL means careful with money. Thrifty and careful are synonyms.", "Wasteful reverses it."],
            "(b) wasteful"),
        pat("sas-p4", "Unknown word: root and context", "common",
            "The capital word is new, but its parts and the sentence each give a clue.",
            ["Split the word for a prefix or root (aud = hear).", "Check the meaning against the sentence.",
             "Choose the option both clues agree on."],
            "Two weak clues that point the same way are strong.",
            "Even in the last row the lecturer's voice was AUDIBLE. (a) able to be heard (b) very angry (c) recorded (d) sweet",
            ["aud means hear, and -ible means able to be.", "The sentence is about hearing the voice.", "Able to be heard fits."],
            "(a) able to be heard"),
        pat("sas-p5", "Recall from a memorised pair", "common",
            "The word is one half of a pair you have banked (barren and fertile).",
            ["Recognise the word.", "Recall its partner from the bank.", "Find the partner in the options."],
            "One pair in memory answers a synonym item and an antonym item.",
            "Most opposite to BARREN: (a) fertile (b) empty (c) dry (d) poor",
            ["BARREN means unable to produce crops.", "Empty and dry are related, not opposite.", "Fertile is the banked partner."],
            "(a) fertile"),
    ],
    mistakes=[
        mis("Starting with the options.", "Read the command word and the given word first."),
        mis("Mixing up nearest and most opposite.", "Underline the command word before you look at the options."),
        mis("Skipping the sentence and answering from the common meaning.", "In a sentence item, paraphrase the word from the sentence."),
        mis("Reading a word list once and stopping.", "Use each word in a sentence and revise it every week."),
        mis("Spending long on one unknown word.", "Take 15 seconds, split it, pick by tone, and move on."),
    ],
    revision=[
        "Routine: direction, tone, word class, roots, eliminate, choose.",
        "Sentence given: paraphrase the capital word first.",
        "Learn words in opposite pairs. Keep a mock-test word sheet.",
        "Antonym question: synonyms are wrong. Synonym question: opposites are wrong.",
        "Prefer the plainer survivor over the showy word.",
        "Never leave a vocabulary item blank.",
    ],
    tricks=[
        trick("Two passes",
              "Answer every sure vocabulary item in the first pass at 15 seconds each. Come back to the unknown words with the time left."),
        trick("Options show the scale",
              "If the options are kind, cruel, wealthy, talkative, the scale is temperament. Now guess the tone of the given word from its parts and pick a matching option."),
        trick("Words repeat across years",
              "Solve the last five years of synonym and antonym questions. Words come back within two to four years."),
    ],
)

if __name__ == "__main__":
    apply("synonyms-antonyms", SUBS)
