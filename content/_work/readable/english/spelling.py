"""Readable rewrite of English > Spelling (all 5 subtopics).

Plain English, short sentences, tables for word lists, one method per question type.
Every fact from the old notes is kept; new pattern ids continue each subtopic's prefix.
Run: python spelling.py  (patches content/core/topics/english/spelling.json in place)
"""
import json
import re
from pathlib import Path

ROOT = Path(__file__).resolve().parents[3]
TOPIC = ROOT / "core" / "topics" / "english" / "spelling.json"


def pat(pid, name, freq, spot, steps, why, q, ex_steps, answer, formula=None):
    return {"id": pid, "name": name, "frequency": freq, "howToSpot": spot, "formula": formula,
            "steps": steps, "why": why, "example": {"q": q, "steps": ex_steps, "answer": answer}}


def mis(wrong, right):
    return {"wrong": wrong, "right": right}


SUBS = {}

# =====================================================================
# 1. ie / ei
# =====================================================================
SUBS["spell-ie-rule"] = dict(
    concept=(
        "The old rhyme says: *i before e, except after c*. It works only when the pair makes the long 'ee' sound. "
        "Say the word first, then apply the rule. "
        "The paper also uses a short list of exceptions, such as *weird*, *seize* and *foreign*. Learn that list by heart."
    ),
    notes=r"""### The rule in one line
Write **ie** when the pair sounds like a long 'ee' and no **c** comes before it.

- believe, achieve, grief, field, shield, niece, piece
- After **c**, the order flips to **ei**: receive, deceive, perceive, conceive, ceiling

> **Rule:** *i before e, except after c, or when it sounds like 'ay' as in neighbour and weigh.*

### Sound decides the spelling
Say the word before you apply the rule. The rule needs the 'ee' sound.

| Sound of the pair | Spelling | Words |
|---|---|---|
| 'ee', no c before it | ie | believe, achieve, relieve, retrieve, brief, siege, yield, shriek |
| 'ee', straight after c | ei | receive, deceive, perceive, conceive, ceiling, receipt, deceit, conceit |
| 'ay' | ei | neighbour, weigh, weight, eight, vein, rein, reign, beige, freight, sleigh |
| 'eye' | ei | height, sleight |

Height is not covered by the rhyme. Its 'ei' sounds like 'eye', so treat it as an exception.

> **Watch:** Most mistakes come from using the c-rule on a word that has no 'ee' sound.

### When c is followed by ie
Two groups keep **ie** after a c.

1. **The c sounds 'sh'.** The letters 'ci' make the 'sh' sound. Examples: ancient, efficient, sufficient, proficient, deficient, deficiency, conscience, species.
2. **The i and e are in different syllables.** Examples: sci-ence, so-ci-e-ty, fan-ci-er.

Every word ending in **-cient** or **-ciency** is in the first group. So *proficient* is right and *proficeint* is wrong.

### The exception list
These words break the rule. Learn them as one list.

- **'ee' sound, but ei:** seize, weird, protein, caffeine, either, neither
- **ei with other sounds:** leisure, foreign, sovereign, forfeit, counterfeit, heir, their
- **ie with a short vowel:** friend, mischief, sieve

> **Tip:** Remember *friend* as fr-I-END. It ends with END.

### Long words keep the base spelling
A longer word keeps the ie or ei of its base word.

- achieve, achievement
- grieve, grievance
- deceive, deceit, deceitful
- perceive, perception
- receive, receipt (keep the silent **p** in receipt)

### A quick pair table
Fix one word of each pair and its partner follows.

| Word | Its partner |
|---|---|
| believe | achieve |
| receive | deceive |
| height | weight |
| foreign | sovereign |

### How the options are built
The setter gives four versions of one word.

1. The correct spelling.
2. The ie/ei swap, such as *recieve*.
3. The swap plus another slip, such as *reciept*.
4. A sound spelling, such as *receve*.

Find the pair first. Check for a c before it. Then check the sound. The other slips usually rule themselves out.
""",
    tricks=[
        {"title": "The c-test",
         "body": "Is there a c right before the pair? Then choose ei (receive). No c? Usually choose ie (believe). Ten exceptions override this: weird, seize, height, foreign, sovereign, leisure, either, neither, their, protein.",
         "example": {"q": "Which is correct: deceive or decieve?",
                     "steps": ["The pair follows a c.", "After c the order is ei."],
                     "answer": "deceive"}},
        {"title": "Rhyme-anchor pairs",
         "body": "Some words match each other. Height and weight match. Believe and achieve match. Receive and deceive match. Fix one word of a pair and you get its partner free."},
        {"title": "Say it in syllables",
         "body": "Say the word slowly in your head: be-lieve, re-ceive. Your ear often confirms what your eye doubts."},
    ],
    mistakes=[
        mis("Applying 'except after c' to words with no 'ee' sound, such as *neighbour*.", "Say the word first. The c-rule works only for the long 'ee' sound."),
        mis("Writing *recieve* or *decieve*.", "After c, the order is ei: receive, deceive, perceive, conceive."),
        mis("Writing *proficeint* or *sufficeint* because a c comes before the pair.", "When c sounds 'sh', the spelling is -cient: proficient, sufficient, ancient."),
        mis("Writing *wierd*, *sieze* or *foriegn* by the ie habit.", "These are exceptions with ei and no c: weird, seize, foreign."),
        mis("Writing *freind* or *mischeif*.", "Friend and mischief keep ie. Remember fr-I-END."),
        mis("Dropping the silent p in *receipt*, as in *receit*.", "Receipt keeps its silent p."),
    ],
    revision=[
        "The rule applies only to the long 'ee' sound.",
        "'ee' sound: ie, except straight after c (receive, ceiling, receipt).",
        "'ay' sound gives ei (neighbour, weigh, reign). 'eye' sound gives ei (height).",
        "c + ie is right when c sounds 'sh' (ancient, efficient, species) or the letters are in separate syllables (science, society).",
        "Exceptions: seize, weird, protein, caffeine, either, neither, leisure, foreign, sovereign, forfeit, counterfeit, heir, their.",
        "Friend, mischief and sieve keep ie.",
        "Derived words keep the base spelling: achievement, grievance, deceitful, receipt.",
    ],
    patterns=[
        pat("sir1", "Long 'ee' with no c: ie", "very common",
            "The options differ only in ie/ei. The letter before the pair is not c (achieve, retrieve, grievance, niece).",
            ["Say the word. The pair makes an 'ee' sound.", "Check the letter before the pair. It is not c.", "Choose ie.", "Reject sound spellings like *retreeve*."],
            "For the 'ee' sound, ie is the default spelling.",
            "Retrieve / Retreive / Retrive / Retreeve",
            ["The pair makes an 'ee' sound.", "The letter before it is r, not c.", "So the pair is ie."],
            "Retrieve"),
        pat("sir2", "Straight after c: ei", "very common",
            "The pair comes directly after a c (receipt, deceit, perceive, ceiling).",
            ["Confirm the c is right before the pair.", "Confirm the 'ee' sound (re-CEIPT, de-CEIT).", "Choose ei.", "Check for extra letters, such as the silent p in receipt."],
            "The 'except after c' part of the rule is reliable for the 'ee' sound.",
            "Receipt / Reciept / Receit / Reciet",
            ["The pair follows c, so it is ei.", "Receipt keeps its silent p.", "Only one option has both."],
            "Receipt"),
        pat("sir3", "ei exceptions with no c", "common",
            "The word is on the exception list: seize, weird, foreign, leisure, sovereign, counterfeit, forfeit, protein.",
            ["Recognise the word as an exception.", "Choose ei even though there is no c.", "Check the rest of the word. Foreign has -eign-, not -iegn-."],
            "Setters pick these words because the general rule gives the wrong answer.",
            "Seize / Sieze / Seeze / Siese",
            ["Seize has the 'ee' sound but takes ei.", "There is no c, yet the word is on the exception list."],
            "Seize"),
        pat("sir4", "c + ie when c sounds 'sh'", "common",
            "A c is followed by ie, but the c sounds 'sh' or the i and e are in different syllables: proficient, deficiency, species, society.",
            ["Say the c. Does it sound 'sh' (effi-SHENT)?", "If yes, keep ie after the c.", "Reject options that force ei after the c, such as *proficeint*."],
            "The c-rule covers only the one-sound 'ee' pair. A 'cie' with a 'sh' sound is a different letter group.",
            "Proficient / Proficeint / Profficient / Proficent",
            ["The c sounds 'sh': pro-FI-shent.", "So ie follows the c, as in efficient and ancient.", "Only one option has ie and a single f."],
            "Proficient"),
        pat("sir5", "'ay' or 'eye' sound: ei", "common",
            "The pair does not sound like 'ee'. It sounds like 'ay' (weigh, reign, vein) or 'eye' (height).",
            ["Say the word. Is the sound 'ay' or 'eye'?", "If yes, choose ei.", "Ignore the c-rule."],
            "Such words follow the 'or when sounded like ay' part of the rhyme.",
            "Neighbour / Nieghbour / Neighbur / Naibour",
            ["The pair sounds like 'ay'.", "So it is ei: neighbour."],
            "Neighbour"),
        pat("sir6", "Longer word from a base word", "occasional",
            "The word is built from a base: achievement, grievance, deceitful, perception.",
            ["Find the base word (achieve, grieve, deceive).", "Copy its ie or ei exactly.", "Then check the ending."],
            "A longer word keeps the ie/ei of its base word.",
            "Achievement / Acheivement / Achievment / Achiivement",
            ["The base is achieve, with ie.", "The suffix -ment is added and the e stays.", "Only one option keeps both."],
            "Achievement"),
    ],
)

# =====================================================================
# 2. Doubling
# =====================================================================
SUBS["spell-doubling"] = dict(
    concept=(
        "A final consonant doubles before a vowel suffix only when the word ends in vowel + consonant "
        "and the stress is on the last syllable. So *begin* becomes *beginning*, but *visit* becomes *visited*. "
        "Some words also carry fixed double letters, such as *accommodate* and *committee*. Count those letters."
    ),
    notes=r"""### The three conditions
The final consonant doubles when all three are true.

1. The word ends in **consonant + vowel + consonant** (be**gin**, o**ccur**, re**fer**).
2. The suffix begins with a **vowel** (-ing, -ed, -ance, -ence).
3. The **stress** falls on the last syllable (be-**GIN**, pre-**FER**).

Results: begin, beginning. Prefer, preferred. Regret, regretted.

> **Rule:** Say the word. Find the stressed syllable. If it is the last one, double the final consonant.

### Why the letter doubles
Doubling keeps the vowel short. *Hoping* has a long 'o' (from hope). *Hopping* has a short 'o' (from hop). Long words follow the same idea when the last syllable is stressed.

- om-**IT**: omitted, omitting
- re-**GRET**: regretted, regrettable
- ad-**MIT**: admitted, admittance
- trans-**FER**: transferred, transferring
- com-**PEL**: compelled
- for-**GET**: forgetting

### When the letter stays single
If the stress is earlier, add the suffix directly.

- **DE**-vel-op: developed
- **BUD**-get: budgeted
- **PROF**-it: profited
- **LIM**-it: limited
- **BEN**-e-fit: benefited
- **TAR**-get: targeted
- **VIS**-it: visited
- **OF**-fer: offered

The letter also stays single after two vowels (rain, rained) or two consonants (help, helped). It stays single before a consonant suffix: commit, commitment.

> **Watch:** *Benefitted* and *targetted* look natural. They are wrong.

### Stress can move
The stress may shift in the longer word. Say the new word, not the old one.

- re-**FER**, re-**FERR**-ing, but **REF**-er-ence (one r)
- pre-**FER**, pre-**FERR**-ed, but **PREF**-er-ence

### Words that simply have double letters
Some doubles are part of the word. Learn them by counting.

| Word | Doubles |
|---|---|
| accommodation | cc and mm |
| possession | ss and ss |
| committee | mm, tt and ee |
| embarrass | rr and ss |
| millennium | ll and nn |
| necessary | one c, double s |
| recommend | one c, double m |
| tomorrow | one m, double r |
| harass | one r, double s |
| parallel | one r, ll in the middle, one l at the end |

> **Tip:** Write each option's doubles in the margin. For *necessary*: c1 s2. Then compare.

### Three quick examples
- **Begin** ends in g-i-n, and the stress is on the last syllable. So *beginning* has two n's.
- **Visit** is stressed on the first syllable. So *visited* has one t.
- **Occur** is stressed on the last syllable. So *occurred* has two r's.

### British forms
Indian exams use British spelling. A word ending in a single vowel + l doubles the l whatever the stress: travel, travelled; cancel, cancelled; label, labelled. American English writes *traveled*. Pick the British form.
""",
    tricks=[
        {"title": "Stress decides doubling",
         "body": "Say the word. If the last syllable is stressed, double the consonant before a vowel suffix (begin, beginning; occur, occurred). If not, do not double (benefit, benefited).",
         "example": {"q": "Which is correct: benefitted or benefited?",
                     "steps": ["BEN-e-fit has the stress on the first syllable.", "So the t stays single."],
                     "answer": "benefited"}},
        {"title": "Double-double checklist",
         "body": "Five words need two sets of double letters: accommodate (c, m), committee (m, t), embarrass (r, s), occurrence (c, r), millennium (l, n). Count them."},
        {"title": "Letter census",
         "body": "Count the repeated letters in each option. Accommodate must show two c's and two m's. Embarrass must show two r's and two s's. Cut any option that fails the count."},
    ],
    mistakes=[
        mis("Writing *benefitted* or *targetted*.", "The stress is early, so the t stays single: benefited, targeted."),
        mis("Writing *begining* or *refering*.", "The last syllable is stressed, so the letter doubles: beginning, referring."),
        mis("Writing *accomodate* or *comittee* with one set of doubles.", "Count both sets: accommodate has cc and mm. Committee has mm, tt and ee."),
        mis("Doubling the wrong letter in *neccessary* or *reccomend*.", "Necessary has one c and double s. Recommend has one c and double m."),
        mis("Writing *traveled* when the options are British.", "British English doubles the l: travelled, cancelled, labelled."),
        mis("Writing *prefference* by copying *preferred*.", "The stress moves in the longer word. Preference has one r after the f."),
    ],
    revision=[
        "Double only when the last syllable is stressed and the suffix starts with a vowel: omitted, regrettable, transferred.",
        "Stress earlier means no double: developed, budgeted, profited, limited, galloped.",
        "Say the new word. Reference and preference have one r.",
        "Learn by count: accommodation, possession, address, success.",
        "Necessary (one c, two s), recommend (one c, two m), tomorrow (one m, two r), harass (one r, two s).",
        "British forms: travelled, cancelled, labelled.",
    ],
    patterns=[
        pat("sdb1", "Stressed final syllable: double", "very common",
            "A base ends in one vowel + one consonant (omit, regret, transfer) and takes -ed, -ing or -able. The options differ in single or double.",
            ["Say the base word and find the stress: om-IT, re-GRET.", "If the last syllable is stressed and the suffix starts with a vowel, double the last consonant.", "Do not double any other letter. The m of omit stays single."],
            "Doubling keeps the stressed vowel short.",
            "Omitted / Ommitted / Omited / Ommited",
            ["The stress is on -MIT.", "So the t doubles.", "The m stays single."],
            "Omitted"),
        pat("sdb2", "Unstressed final syllable: no double", "very common",
            "The base is stressed early (DEvelop, BUDget, PROFit) and a double-letter option looks tempting.",
            ["Say the base: DE-vel-op, BUD-get.", "The stress is not on the last syllable.", "Add the suffix directly.", "Reject every option with a doubled final consonant."],
            "With no stress on the last syllable, there is no short vowel to protect.",
            "Developed / Developped / Develloped / Divelopped",
            ["The stress is on the first syllable: DE-vel-op.", "So the p stays single."],
            "Developed"),
        pat("sdb3", "Words with two sets of doubles", "common",
            "The word is from the two-sets list: accommodation, possession, address, success, assassinate.",
            ["Count both sets of doubles. Accommodation has cc and mm.", "Remove any option with only one set.", "Check the ending last."],
            "Wrong options usually keep one double and drop the other, so a count finds them.",
            "Possession / Posession / Possesion / Posesion",
            ["Possession has ss and ss.", "Each wrong option drops at least one double."],
            "Possession"),
        pat("sdb4", "Words with only one double", "common",
            "The word is often over-doubled: necessary, recommend, tomorrow, harass, occasion.",
            ["Recall which letter doubles. Necessary: s only. Recommend: m only.", "Remove options that double the wrong letter or both letters.", "Check the vowels last."],
            "This group is tested by adding a double where none belongs.",
            "Necessary / Neccessary / Necessery / Neccesary",
            ["Necessary has one c and double s.", "Neccessary and Neccesary have two c's.", "Necessery changes a vowel."],
            "Necessary"),
        pat("sdb5", "British single l: travelled, cancelled", "occasional",
            "The base ends in a single vowel + l (travel, cancel, label) and the suffix is -ed or -ing.",
            ["Check the last letters: vowel + l.", "Double the l, whatever the stress.", "Choose the British form."],
            "Indian exams follow British spelling.",
            "Cancelled / Canceled / Cancelld / Cancelted",
            ["Cancel ends in vowel + l.", "British English doubles the l.", "So the word is cancelled."],
            "Cancelled"),
        pat("sdb6", "Stress moves in the longer word", "occasional",
            "The options include both referring and reference style forms (preferred, preference, referring, reference).",
            ["Say the new word, not the base.", "Is the stress still on the last syllable of the base? Then double.", "If the stress moved earlier, keep the letter single."],
            "The stress decides doubling, and it shifts in words like reference.",
            "Preferred / Prefered / Preferrred / Prefferred",
            ["Say pre-FERR-ed. The stress is on the last syllable of prefer.", "So the r doubles.", "The f stays single."],
            "Preferred"),
    ],
)

# =====================================================================
# 3. Suffix endings
# =====================================================================
SUBS["spell-suffix-endings"] = dict(
    concept=(
        "Three suffix pairs cause most ending mistakes: *-able / -ible*, *-ance / -ence* and *-ant / -ent*. "
        "No rule is perfect, but two tests work well. Ask if the stem is a complete word. Then think of the matching noun or adjective. "
        "Learn the word families in the tables as units."
    ),
    notes=r"""### -able or -ible
Use the whole-word test. Remove the ending and look at what is left.

- Complete word: usually **-able** (accept-able, comfort-able, depend-able, remark-able, avail-able).
- Not a word: usually **-ible** (poss-ible, horr-ible, vis-ible, cred-ible, aud-ible, feas-ible).

Some complete stems still take -ible: accessible, flexible, digestible, contemptible, collapsible. Learn them as a short list.

> **Watch:** *Indispensable* is a common trap. The stem *dispense* is a whole word, so it takes -able.

A related noun in -ssion or -sion often signals -ible: permission, permissible; division, divisible; comprehension, comprehensible.

### -ance or -ence, -ant or -ent
The noun and its adjective share the same vowel. Learn one form and you have both.

| Adjective | Noun |
|---|---|
| relevant | relevance |
| significant | significance |
| tolerant | tolerance |
| brilliant | brilliance |
| permanent | permanence |
| confident | confidence |
| obedient | obedience |
| coincident | coincidence |

Some words take -ance without a matching adjective: surveillance, perseverance, maintenance, grievance, appearance, resistance, allegiance, nuisance, hindrance, assistance.

> **Tip:** Words from *fer* take -ence: reference, preference, difference, inference.

When stuck, think of the adjective. *Relevent* is wrong because the adjective is *relevant*.

### Keep or drop the final e
- **Drop the e** before a vowel suffix: write, writing; desire, desirable; use, usable; hope, hoping.
- **Keep the e** before a consonant suffix: hope, hopeful; manage, management; care, careful.
- **Keep the e after soft c or g** before a or o: notice, noticeable; change, changeable; courage, courageous; outrage, outrageous.

Exceptions that drop the e: argument, truly, ninth, wholly.

### The -y ending
After a consonant, change y to i: happy, happiness; busy, business; carry, carried.
After a vowel, keep the y: enjoy, enjoyment; pay, payable.
Before -ing, keep the y: carrying, studying.

### The -cient family
Sufficient, efficient, proficient and ancient all end in **-cient**. Science and conscience end in **-ence**: conscience is con + science.

### How to use this in the exam
1. Find where the options differ. It is usually the last four or five letters.
2. Run one test: whole word? matching adjective? soft c or g?
3. If no test applies, use the word families above.

Two words to remember: the noun from *maintain* is **maintenance**, and the word for 'able to be heard' is **audible**.
""",
    tricks=[
        {"title": "Root trace",
         "body": "Strip the suffix and look at the root. Exist gives existence. Maintain gives maintenance. Resist gives resistance. Persist gives persistence. The root's own spelling helps decide the ending."},
        {"title": "-fer means -ence",
         "body": "Nouns from *fer* take -ence: reference, preference, difference, inference. The verb doubles by stress: refer, referring."},
        {"title": "The -cient family",
         "body": "Sufficient, efficient and ancient all end in -cient. Science is sci + ence, and conscience is con + science.",
         "example": {"q": "Which is correct: efficent, efficiant or efficient?",
                     "steps": ["The word belongs to the -cient family.", "So the ending is -cient."],
                     "answer": "efficient"}},
    ],
    mistakes=[
        mis("Writing *independant* or *persistant* by sound.", "Match the adjective: independent, persistent, dependent."),
        mis("Writing *resistence* or *maintainance*.", "Resistance takes -ance. The noun from maintain is maintenance."),
        mis("Writing *noticable* or *changable*.", "Keep the e after a soft c or g: noticeable, changeable."),
        mis("Writing *responsable* or *indispensible*.", "Use the whole-word test: responsible has a non-word stem, so -ible. Indispensable has a whole-word stem, so -able."),
        mis("Writing *sufficent* or *efficiant*.", "These end in -cient: sufficient, efficient, ancient."),
        mis("Writing *arguement* or *truely*.", "Argue and true lose the e: argument, truly."),
    ],
    revision=[
        "Complete-word stem gives -able (acceptable, indispensable). Non-word stem gives -ible (possible, visible, audible).",
        "A -ssion or -sion noun often signals -ible: permissible, divisible, comprehensible. Accessible and flexible are exceptions to learn.",
        "-ant goes with -ance, and -ent goes with -ence: relevant, relevance; permanent, permanence.",
        "Drop the e before a vowel suffix (writing, desirable). Keep it after soft c or g (noticeable, advantageous).",
        "Maintenance, not maintainance. Truly, argument and ninth drop the e.",
        "Sufficient, efficient, ancient end in -cient.",
    ],
    patterns=[
        pat("sse1", "-ance or -ence", "very common",
            "The options differ only in -ance/-ence (perseverance, coincidence, surveillance).",
            ["Think of the matching adjective or verb: coincident gives coincidence.", "Match the vowel: -ant goes with -ance, -ent with -ence.", "If there is no matching form, use the families you know (surveillance, perseverance)."],
            "A noun and its adjective share the same vowel.",
            "Coincidence / Coincidance / Coinsidence / Coincedence",
            ["The adjective is coincident.", "So the noun ends in -ence.", "Coinsidence changes a consonant."],
            "Coincidence"),
        pat("sse2", "-able or -ible", "common",
            "The options differ in -able/-ible (responsible, indispensable, accessible).",
            ["Remove the ending. Is the stem a complete word?", "Complete word: choose -able. Not a word: choose -ible.", "Check the -sion clue: permission, permissible."],
            "-able was added to complete English words. -ible came with Latin stems.",
            "Responsible / Responsable / Resposible / Responsibel",
            ["Remove the ending: 'respons' is not a whole word.", "So the ending is -ible."],
            "Responsible"),
        pat("sse3", "Keep or drop the final e", "common",
            "The base ends in e (write, advantage, notice) and the options differ in whether the e stays.",
            ["Does the suffix start with a vowel? Drop the e (writing, desirable).", "Is there a soft c or g before a or o? Keep the e (advantageous).", "Consonant suffix? Keep the e (management), except truly, argument, ninth."],
            "The e is dropped only when it has no job to do.",
            "Advantageous / Advantagous / Advantageus / Advantagious",
            ["The base is advantage, with a soft g.", "The e keeps the g soft before -ous."],
            "Advantageous"),
        pat("sse4", "-ant or -ent adjective", "common",
            "The options differ in -ant/-ent (relevant, permanent, brilliant), often with a vowel swap earlier in the word.",
            ["Think of the matching noun: relevance gives relevant.", "Check the letters before the ending too (re-LE-vant, per-MA-nent).", "Remove any option that fails either check."],
            "The noun keeps the same vowel as the adjective.",
            "Relevant / Relevent / Revelant / Relavant",
            ["The noun is relevance, so the adjective ends in -ant.", "Revelant swaps two letters.", "Relavant changes a vowel."],
            "Relevant"),
        pat("sse5", "-cient family", "common",
            "The word means enough, skilled or very old and ends in -cient (sufficient, efficient, proficient, ancient).",
            ["Spot the 'shent' sound at the end.", "Choose -cient.", "Reject -cent, -ciant and -ceint."],
            "All the words in this family share one ending.",
            "Sufficient / Sufficent / Sufficiant / Suficient",
            ["The ending sounds 'shent', so it is -cient.", "The word also has a double f."],
            "Sufficient"),
        pat("sse6", "-y ending changes", "occasional",
            "The base ends in y (happy, busy, carry, enjoy) and takes a suffix.",
            ["Look at the letter before y.", "After a consonant, change y to i (happiness, carried).", "After a vowel, keep y (enjoyment, payable)."],
            "The y changes only when a consonant comes before it.",
            "Happiness / Happyness / Hapiness / Happines",
            ["Happy ends in consonant + y.", "So y becomes i.", "The ending -ness adds a double s."],
            "Happiness"),
    ],
)

# =====================================================================
# 4. Trap words
# =====================================================================
SUBS["spell-trap-words"] = dict(
    concept=(
        "Some words are spelt wrongly again and again, so setters choose them. "
        "Each one hides a silent letter, a missing letter or a borrowed pattern. "
        "Learn the bank in small groups, and give each word a hook."
    ),
    notes=r"""### The word bank
Each word has one hidden letter or one missing letter. Use the hook.

| Correct | Hook |
|---|---|
| privilege | no d anywhere: priv-i-lege |
| rhythm | no vowel except y: Rh-y-th-m |
| government | the n of govern stays: govern + ment |
| environment | the n of environ stays: environ + ment |
| separate | there is 'a rat' in sePArATE |
| desperate | despERate: it ends in -erate |
| definite | ends in -inite: finite is inside |
| restaurant | rest-au-rant: the au sits in the middle |
| guarantee | gua first, then rantee |
| calendar | ends in -dar (a calender is a machine) |
| queue | five letters, only q speaks |
| vacuum | double u: vac-uum |
| liaison | lia-ison |
| grateful | grate + ful |

> **Tip:** Say the hook aloud once. Then cover the word and write it.

### Silent letters
Many trap words have a letter you do not say.

- **Silent p:** psychology, pneumonia, receipt, cupboard, raspberry
- **Silent d:** Wednesday, handkerchief, grandson
- **Silent b:** debt, doubt, subtle, plumber, tomb
- **Silent h:** rhythm, rhyme, exhaust, exhibition, ghost
- **Silent s:** island, aisle, debris
- **Silent n after m:** autumn, column, condemn, solemn

Say the word as it is spelt (WED-NES-DAY) to remember the silent letter.

### -ceed, -cede and -sede
- **-ceed:** only proceed, succeed and exceed
- **-sede:** only supersede
- **-cede:** every other word: precede, recede, concede, secede, intercede

> **Rule:** Three words end in -ceed, one ends in -sede, and all the rest end in -cede.

The related words procedure and success do not follow the same pattern. Procedure has one e, and success has a double c.

### When a root word changes
The longer word often changes the root. The wrong option keeps the root unchanged.

- pronounce, pronunciation (the o goes)
- explain, explanation
- maintain, maintenance
- exclaim, exclamation
- curious, curiosity
- four, forty (but fourteen)
- nine, ninth (but ninety and nineteen)
- argue, argument; true, truly; due, duly

### Borrowed words
French and Latin words keep their original spelling. Break them into parts.

- entrepreneur: entre + pre + neur
- bureaucracy: bureau + cracy
- connoisseur, rendezvous, reservoir, silhouette, camaraderie, liaison, questionnaire

The usual mistake is to swap letters inside a part, as in *entreprenuer*.

### Words to look at closely
- **parallel** has one r, a double l in the middle, and a single l at the end.
- **skiing** is right (ski + ing). Only *sking* is a wrong option.
- **cacti** and **cactuses** are both accepted plurals.
- **collectable** and **collectible** are both standard.
""",
    tricks=[
        {"title": "The n-test for -ment words",
         "body": "Government is govern + ment. Environment is environ + ment. The root's final n must survive. Ask what the root is, and the letter reappears.",
         "example": {"q": "Which is correct: goverment or government?",
                     "steps": ["The root is govern.", "Its n must stay before -ment."],
                     "answer": "government"}},
        {"title": "Three -ceed, one -sede",
         "body": "Proceed, succeed and exceed are the only -ceed words. Supersede is the only -sede word. Every other word with this sound ends in -cede."},
        {"title": "Plurals already plural",
         "body": "Criteria, phenomena and stimuli are already plurals. An option that adds -s to them (criterias) is wrong."},
    ],
    mistakes=[
        mis("Writing *priviledge* or *goverment* by sound.", "Use the hook: privilege has no d. Government keeps the n of govern."),
        mis("Writing *seperate* or *definate*.", "Separate has 'a rat' in it. Definite ends in -inite."),
        mis("Writing *preceed* or *procede*.", "Only proceed, succeed and exceed end in -ceed. Precede ends in -cede."),
        mis("Keeping the root unchanged: *pronounciation*, *nineth*.", "The root changes: pronunciation, ninth."),
        mis("Dropping the silent letter: *Wensday*, *dout*.", "Say the word as it is spelt: Wednesday, doubt."),
        mis("Swapping letters in a borrowed word: *entreprenuer*.", "Split it into parts: entre + pre + neur."),
    ],
    revision=[
        "Silent letters: psychology, Wednesday, subtle, rhythm, island, autumn.",
        "Only proceed, succeed and exceed end in -ceed. Only supersede ends in -sede. All others end in -cede.",
        "Root changes: pronunciation, explanation, forty, ninth, argument, truly.",
        "Government and environment keep the n of the root.",
        "Borrowed words: learn by parts (bureau + cracy, entre + pre + neur).",
        "Parallel has one r and a double l in the middle.",
        "Do not add -s to criteria, phenomena or stimuli.",
    ],
    patterns=[
        pat("stw1", "Silent letter", "very common",
            "The word contains a letter you do not say (Wednesday, psychology, subtle) and some options leave it out.",
            ["Recall the silent letter by saying the word as it is spelt (WED-NES-DAY).", "Remove every option that drops it.", "Check the order of the other letters."],
            "The most common mistake is to spell the word as it sounds.",
            "Wednesday / Wendesday / Wensday / Wednsday",
            ["Say it as spelt: Wed-nes-day.", "The d is silent but written.", "Only one option keeps it with all other letters."],
            "Wednesday"),
        pat("stw2", "-ceed, -cede or -sede", "common",
            "The options differ in -ceed / -cede / -sede, or in the vowel before the ending (precede, succeeded, exceed).",
            ["Is it proceed, succeed or exceed? Then -ceed.", "Is it supersede? Then -sede.", "Otherwise choose -cede."],
            "The list of exceptions is only four words long.",
            "Precede / Preceed / Presede / Priceed",
            ["Precede is not proceed, succeed or exceed.", "It is not supersede.", "So it ends in -cede."],
            "Precede"),
        pat("stw3", "Root letter changed in the longer word", "common",
            "The word comes from a root that changes its letters: pronounce to pronunciation, nine to ninth, four to forty.",
            ["Think of the root and how it changes.", "Remove the option that keeps the root unchanged.", "Check the remaining options letter by letter."],
            "The most common wrong option keeps the root as it is.",
            "Pronunciation / Pronounciation / Pronuntiation / Prononciation",
            ["Pronounce loses its o in the longer word.", "So it is pro-nun-ci-a-tion.", "Pronounciation keeps the root."],
            "Pronunciation"),
        pat("stw4", "Borrowed word", "common",
            "A French or Latin borrowing: entrepreneur, bureaucracy, connoisseur, rendezvous, silhouette.",
            ["Split the word into parts: bureau + cracy.", "Check each part in each option.", "Remove options with swapped letters inside a part."],
            "Borrowed words keep their original spelling, so part-by-part checking is reliable.",
            "Bureaucracy / Beaurocracy / Bureaucrasy / Burocracy",
            ["Split it: bureau + cracy.", "Beaurocracy swaps letters in bureau.", "Only one option has both parts right."],
            "Bureaucracy"),
        pat("stw5", "Missing letter: the root drops a letter", "common",
            "The word is truly, argument, ninth, forty, publicly or duly, and a wrong option keeps the extra letter.",
            ["Think of the base: true, argue, nine, four, public.", "Note which letter drops: true and argue lose e, nine loses e, four loses u.", "Choose the option with the drop."],
            "These words are tested by adding back the letter that the root loses.",
            "Truly / Truely / Trully / Truley",
            ["The base is true.", "It drops its e before -ly.", "So the word is tru-ly."],
            "Truly"),
        pat("stw6", "Root letter survives: govern-ment", "common",
            "The word ends in -ment (government, environment, embarrassment) and a wrong option drops a root letter.",
            ["Name the root: govern, environ, embarrass.", "Add -ment to the whole root.", "Check that no root letter is missing."],
            "The suffix -ment joins the whole root, so its last letter stays.",
            "Government / Goverment / Governmant / Govrnment",
            ["The root is govern.", "Add -ment: govern + ment.", "So the n stays."],
            "Government"),
    ],
)

# =====================================================================
# 5. Strategy
# =====================================================================
SUBS["spell-strategy"] = dict(
    concept=(
        "Spelling questions come in a few shapes. Some show four versions of one word. Some show four different words and ask for the wrong one. "
        "In both, you find the spot that differs or fails, and you apply one test. "
        "A short daily routine turns recognising words into spelling them."
    ),
    notes=r"""### Three question types
1. **Choose the correct spelling.** Four versions of one word. Compare the options letter by letter. Look only at the spot where they differ.
2. **Find the misspelt word.** Four different words, and one is wrong. You cannot compare, so check each word on its own.
3. **Misspelt word in a sentence.** The same as type 2, but the words sit in a sentence. Ignore the meaning and check each listed word alone.

A fourth type asks for a **plural or related form**, such as criterion to criteria.

### Four moves for a correct-spelling item
1. **Find the difference.** The options differ in one or two spots, such as recie-ve, recei-ve and rece-ve. Focus on that spot only.
2. **Apply the rule that spot obeys.** A c before the pair means ei. A root in -fer gives -ence. A stressed last syllable doubles. Otherwise it is a bank word.
3. **Say each option.** *Mis-CHEE-vious* has four syllables. Mischievous has three.
4. **Split into syllables.** Rest-au-rant needs the au. Check that no letter is missing.

### Checks for a word you cannot compare
Run four quick checks on each word.

1. **Doubles:** Are the double letters right? Tomorrow has one m and two r's.
2. **ie/ei:** Does the pair follow the sound rule?
3. **Ending:** -ance or -ence? -able or -ible? -ceed or -cede?
4. **Silent or dropped letters:** Wednesday, government, pronunciation.

> **Tip:** If three words pass easily, the fourth is the answer, even if you are unsure of it.

### Classical plurals
Latin and Greek nouns keep their original plurals.

| Ending | Plural | Examples |
|---|---|---|
| -on | -a | criterion, criteria; phenomenon, phenomena |
| -is | -es | crisis, crises; analysis, analyses; thesis, theses; basis, bases |
| -us | -i | stimulus, stimuli; radius, radii; nucleus, nuclei |
| -um | -a | medium, media; datum, data; curriculum, curricula |

> **Watch:** Adding -s to these plurals (criterias, crisises) is always wrong.

### Long words: split into syllables
Write the syllables and check each one.

- con-sci-en-tious (con + science + tious)
- mis-cel-la-ne-ous (double l, then -aneous)
- un-ne-ces-sa-ry (un + necessary)

A prefix does not change the root: un + necessary is unnecessary. Mis + spell is misspell. Dis + satisfied is dissatisfied. Two letters meet at the join, and the exam tests it.

### Time and daily plan
A spelling item should take 20 to 30 seconds. If you are torn between two options, pick the one that follows a rule. Setters write wrong options that look natural.

**Daily plan, 15 minutes:** learn 10 new words. Then write yesterday's 10 from memory and mark each miss. Write sentences with bank words and check them a day later.
""",
    tricks=[
        {"title": "Difference-first reading",
         "body": "Do not read four full words. Find the one position where they differ. That spot is the whole question.",
         "example": {"q": "Recieve / Receive / Receve / Reciev",
                     "steps": ["Find the differing spot: the ei/ie pair.", "A c comes before it, so ei."],
                     "answer": "Receive"}},
        {"title": "Syllable count",
         "body": "Count the syllables. Mischievous has three. Rhythm has two. A wrong spelling often forces a syllable that cannot be said."},
        {"title": "Write-from-memory drill",
         "body": "Seeing a word is not the same as spelling it. Cover the list, write the words, mark the misses and repeat tomorrow. The misses shrink each round."},
    ],
    mistakes=[
        mis("Reading all four options in full.", "Find the one spot where they differ and check only that."),
        mis("Adding -s to a classical plural: *criterias*, *crisises*.", "Use the classical plural: criteria, crises."),
        mis("Checking meaning in a misspelt-word-in-a-sentence item.", "Ignore the sentence and check each word on its own."),
        mis("Marking British forms like *recognised* as wrong.", "British forms are correct in these exams."),
        mis("Choosing the option that merely looks familiar.", "Choose the one that follows a rule: sound, stress or whole-word."),
        mis("Leaving a spelling item blank.", "Make one informed choice. There is no reason to skip it."),
    ],
    revision=[
        "Choose-the-correct: compare the options at the one spot where they differ.",
        "Find-the-misspelt: check doubles, ie/ei, ending and silent letters for each word.",
        "Classical plurals: criteria, phenomena, crises, analyses, stimuli, radii, media. Never add -s.",
        "Long words: split into syllables. Prefix + root keeps both letters (unnecessary, misspell).",
        "Unsure between two: pick the one that follows a rule.",
        "Spend 20 to 30 seconds per item.",
    ],
    patterns=[
        pat("sst5", "Choose the correct spelling", "very common",
            "Four versions of one word, and the question asks which is right.",
            ["Scan the four options and find the spot where they differ.", "Apply the rule that spot obeys.", "Say each option and check the syllables."],
            "The options are built to differ in one or two spots, so that spot is the whole question.",
            "Definitely / Definately / Definitly / Defenitely",
            ["The options differ in the vowel after the f.", "Definite ends in -inite, and -ly is added.", "Only one option matches."],
            "Definitely"),
        pat("sst1", "Find the misspelt word (four different words)", "common",
            "The four options are different words and the question asks which one is spelt wrongly.",
            ["Check each word against its known signature: doubles, ie/ei, ending, silent letters.", "Mark the words that pass clearly.", "The one that fails is the answer."],
            "Three words are correct, so one clear failure decides the item.",
            "Tommorow / Receive / Beginning / Calendar",
            ["Receive passes the c-test.", "Beginning has the stressed-syllable double.", "Calendar ends in -dar.", "Tomorrow has one m and double r."],
            "Tommorow"),
        pat("sst2", "Misspelt word inside a sentence", "common",
            "A sentence is given and the options are four words from it. One is misspelt.",
            ["Ignore the meaning of the sentence.", "Check each option on its own.", "Do not mark British forms such as recognised as wrong."],
            "The sentence is only a setting. The test is still one word.",
            "The comittee will announce its decision on Wednesday. Options: comittee / announce / decision / Wednesday",
            ["Announce, decision and Wednesday are right.", "Committee has mm, tt and ee."],
            "comittee"),
        pat("sst3", "Classical plural", "occasional",
            "The question asks for the plural of a Latin or Greek noun (criterion, crisis, analysis, phenomenon).",
            ["Identify the ending: -on, -is, -us or -um.", "Apply the change: -on to -a, -is to -es, -us to -i, -um to -a.", "Reject any option that adds -s to the plural."],
            "These words keep their original plurals in formal English.",
            "Plural of crisis: crises / crisises / crisis / crisies",
            ["Crisis ends in -is.", "The plural changes -is to -es."],
            "crises"),
        pat("sst4", "Long word: check syllable by syllable", "common",
            "A long word (conscientious, miscellaneous, unnecessary) with options that differ at one or two places.",
            ["Split the word into syllables.", "Check each syllable in each option, especially where a prefix meets the root.", "Choose the option with every syllable right."],
            "Long words are hard to take in at a glance, but each syllable is easy to check.",
            "Unnecessary / Unneccessary / Unecessary / Unnecesary",
            ["Split: un + necessary.", "Double n at the join.", "Necessary has one c and double s."],
            "Unnecessary"),
        pat("sst6", "Prefix + root: both letters stay", "occasional",
            "The word starts with a prefix that meets the same letter in the root (misspell, dissatisfied, unnecessary).",
            ["Split the prefix from the root.", "Write both parts in full.", "Keep both letters where they meet."],
            "A prefix never changes the root, so a double letter appears at the join.",
            "Misspell / Mispell / Misspel / Mispel",
            ["The prefix is mis and the root is spell.", "Both s letters stay at the join.", "Spell keeps both l's."],
            "Misspell"),
    ],
)

# ---------------------------------------------------------------------
def long_lines(text, limit=24):
    plain = re.sub(r"\$\$.*?\$\$|\$[^$]*\$", "X", text, flags=re.S)
    plain = re.sub(r"^\s*(?:[-*>|]|\d+[.)])\s*", "", plain, flags=re.M)
    return [s for s in re.split(r"(?<=[.!?])\s+|\n", plain) if len(s.split()) > limit]


data = json.loads(TOPIC.read_text(encoding="utf-8"))
assert set(SUBS) == {s["id"] for s in data["subtopics"]}, "every subtopic must be rewritten"
for sub in data["subtopics"]:
    new = SUBS[sub["id"]]
    old_ids = {p["id"] for p in sub.get("patterns", [])}
    new_ids = [p["id"] for p in new["patterns"]]
    assert old_ids <= set(new_ids), (sub["id"], old_ids - set(new_ids))
    assert len(new_ids) == len(set(new_ids))
    n = new["notes"].strip() + "\n"
    assert 2500 <= len(n) <= 5000, (sub["id"], len(n))
    assert 4 <= len(re.findall(r"^### ", n, re.M)) <= 8, sub["id"]
    for p in new["patterns"]:
        assert 3 <= len(p["steps"]) <= 5 and 2 <= len(p["example"]["steps"]) <= 5, p["id"]
    for ln in long_lines(n + "\n" + new["concept"]):
        print("  long:", sub["id"], ln[:80])
    sub.update(concept=new["concept"], notes=n, tricks=new["tricks"], mistakes=new["mistakes"],
               revision=new["revision"], patterns=new["patterns"])
all_ids = [p["id"] for s in data["subtopics"] for p in s["patterns"]]
assert len(all_ids) == len(set(all_ids)), "pattern id clash"
TOPIC.write_text(json.dumps(data, ensure_ascii=False, indent=1) + "\n", encoding="utf-8", newline="\n")
for s in data["subtopics"]:
    print(s["id"], len(s["notes"]), "chars,", len(s["patterns"]), "patterns")
