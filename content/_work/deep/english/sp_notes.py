# Notes + per-subtopic patterns for spelling (Phase 2 deep content).
from _lib import P

S = {}

S["spell-ie-rule"] = {
"notes": """### The rule is about sound, not letters
'i before e except after c' only works for the **long 'ee' sound**. Say the word first, then apply the rule:
- **'ee' sound, no c before it -> ie:** believe, achieve, relieve, retrieve, grief, field, niece, piece, siege, yield, shriek, brief.
- **'ee' sound straight after c -> ei:** receive, deceive, perceive, conceive, ceiling, receipt, deceit, conceit.
- **'ay' sound -> ei:** neighbour, weigh, weight, eight, vein, rein, reign, beige, freight, sleigh.
- **'eye' sound -> ei:** height, sleight, and one pronunciation of either and neither.
Most spelling mistakes come from applying the c-rule to a word that does not have an 'ee' sound.

### When c is followed by ie
Two groups break the simple 'after c' rule, and papers use both:
1. **c sounds 'sh'** — here 'ci' together makes the 'sh' sound, and the e belongs to the next sound: ancient, efficient, sufficient, proficient, deficient, deficiency, conscience, species. Every word ending in **-cient** or **-ciency** is in this group.
2. **i and e are in separate syllables** — sci-ence, so-ci-e-ty, fan-ci-er. The rule only covers ie/ei as one sound.
So 'proficient' is correct and 'proficeint' is wrong, even though the letters come after a c.

### The exceptions worth learning
These have the 'ee' sound (or no clear sound) but still take ei with no c:
- **seize, weird, protein, caffeine, either, neither** — 'ee' sound, ei spelling.
- **leisure, foreign, sovereign, forfeit, counterfeit, heir, their** — ei with other sounds.
- **friend** keeps ie even though it has a short 'e' sound; **mischief** and **sieve** keep ie with a short 'i'.
Learn them as one short list; the rest of the ie/ei words follow the sound rule.

### Words built from a base keep the base spelling
Longer words keep the ie/ei of the base word: achieve -> achievement, relieve -> relief, grieve -> grievance -> grievous, receive -> receipt -> receptionist, deceive -> deceit -> deceitful, perceive -> perception. If you know the short word, you know the long one. Note that 'receipt' also keeps a silent **p** (from Latin *recepta*), which is often dropped.

### How the options are built
Setters usually give four versions of one word:
1. the correct spelling,
2. the ie/ei swap (recieve),
3. the swap plus another slip (reciept),
4. a sound-spelling (receve, retreeve).
Find the ie/ei spot first, check whether a c is right before it, then check the sound. The other slips usually rule themselves out.

### Quick revision
- Say the word: the rule applies only to the 'ee' sound.
- 'ee' sound: ie, except straight after c (receive, ceiling, receipt).
- 'ay' sound -> ei (neighbour, weigh, reign); 'eye' sound -> ei (height).
- c + ie when c sounds 'sh' (ancient, efficient, species) or i and e are separate syllables (science, society).
- Exceptions: seize, weird, protein, caffeine, either, neither, leisure, foreign, sovereign, forfeit, counterfeit, heir, their; friend keeps ie.
- Derived words keep the base: achievement, grievance, deceitful, receipt.
""",
"patterns": [
 P("sir1", "Long 'ee' with no c: ie", "very common",
   "The options differ only in ie/ei and the letter before the pair is not c (achieve, retrieve, grievance, niece).",
   "1. Say the word — the pair makes an 'ee' sound.\n2. Check the letter before it: not c.\n3. Choose ie; reject sound-spellings like 'retreeve'.\n\n*Why it works:* for the 'ee' sound, ie is the default spelling.",
   "Retrieve / Retreive / Retrive / Retreeve", "**Retrieve** — 'ee' sound after r, so ie."),
 P("sir2", "Straight after c: ei", "very common",
   "The ie/ei pair comes directly after a c (receipt, deceit, perceive, ceiling).",
   "1. Confirm the c is directly before the pair.\n2. Confirm the 'ee' sound (re-CEIPT, de-CEIT).\n3. Choose ei, and check for extra letters (the silent p in receipt).\n\n*Why it works:* the 'except after c' part of the rule is reliable for the 'ee' sound.",
   "Receipt / Reciept / Receit / Reciet", "**Receipt** — after c the order is ei, and the silent p stays."),
 P("sir3", "ei exceptions with no c", "common",
   "The word is from the exception list: seize, weird, foreign, leisure, sovereign, counterfeit, forfeit, protein.",
   "1. Recognise the word as an exception.\n2. Choose ei even though there is no c.\n3. Check the rest of the word (foreigner: -eign-, not -iegn-).\n\n*Why it works:* setters pick these words because the general rule gives the wrong answer.",
   "Seize / Sieze / Seeze / Siese", "**Seize** — an 'ee' word with ei and no c; it is on the exception list."),
 P("sir4", "c + ie when c sounds 'sh' (-cient, -ciency, species)", "common",
   "The word has a c followed by ie but the c sounds 'sh' or the i and e are in different syllables: proficient, deficiency, species, society.",
   "1. Say the c: is it 'sh' (effi-SHENT) or part of 'sci-ence'?\n2. If yes, keep ie after the c.\n3. Reject options that force ei after the c (proficeint).\n\n*Why it works:* the c-rule only covers the one-sound 'ee' pair; 'cie' with a 'sh' sound is a different letter group.",
   "Proficient / Proficeint / Profficient / Proficent", "**Proficient** — c sounds 'sh' (pro-FI-shent), so ie follows c, like efficient and ancient."),
]}

S["spell-doubling"] = {
"notes": """### Why the consonant doubles
Doubling protects the short vowel. In 'hoping' the single p leaves a long 'o' (hope); in 'hopping' the double p keeps the short 'o' (hop). English applies the same idea to longer words, but only when the **last syllable is stressed**:
- om-**IT** -> omitted, omitting
- re-**GRET** -> regretted, regrettable
- ad-**MIT** -> admitted, admittance
- trans-**FER** -> transferred, transferring
- com-**PEL** -> compelled
- for-**GET** -> forgotten, forgetting

### When the consonant does not double
If the stress is on an earlier syllable, add the suffix directly:
- **DE**-vel-op -> developed, developing
- **BUD**-get -> budgeted
- **PROF**-it -> profited
- **LIM**-it -> limited
- **GAL**-lop -> galloped
- **OF**-fer -> offered; **HAP**-pen -> happened
The consonant also stays single if the word ends in two vowels + consonant (**rain** -> rained, **cool** -> cooled) or two consonants (**help** -> helped), or if the suffix starts with a consonant (**commit** -> commitment, **regret** -> regretful).

### Stress can move
Watch words where the stress shifts in the longer form: re-**FER** -> re-**FERR**-ing, but **REF**-er-ence has only one r; pre-**FER** -> pre-**FERR**-ed, but **PREF**-er-ence and **PREF**-er-able. Say the new word, not the old one.

### Words that simply have double letters
Some doubles have nothing to do with suffixes — they are just part of the word. Learn these by counting:
- **Two or more sets of doubles:** accommodation (cc, mm), possession (ss, ss), address (dd, ss), success (cc, ss), assassinate (ss, ss), committee (mm, tt, ee), embarrass (rr, ss), millennium (ll, nn).
- **One set only:** necessary (one c, double s), recommend (one c, double m), tomorrow (one m, double r), harass (one r, double s), occasion (double c, one s), parallel (one r, double l in the middle, one l at the end), dilemma (one l, double m).

### A letter-count routine
For a double-letter item, write each option's doubles in the margin: necessary = c1 s2; neccessary = c2 s2; necesary = c1 s1. Compare with the pattern you know. This takes about ten seconds and catches mistakes you would miss by just looking at the word.

### British forms in the exam
Indian exams follow British spelling. In British English, words ending in a single vowel + l double the l before a vowel suffix whatever the stress: travel -> travelled, cancel -> cancelled, label -> labelled. American English uses travel -> traveled. If an item offers only one of these as the answer, choose the British form.

### Quick revision
- Double only when the last syllable is stressed and the suffix starts with a vowel: omitted, regrettable, transferred.
- Stress earlier -> no double: developed, budgeted, profited, limited, galloped.
- Say the new word: reference and preference have one r.
- Learn by count: accommodation, possession, address, success; necessary (1 c, 2 s), recommend (1 c, 2 m), tomorrow (1 m, 2 r), harass (1 r, 2 s).
- British: travelled, cancelled, labelled.
""",
"patterns": [
 P("sdb1", "Stressed final syllable: double", "very common",
   "A base ending in one vowel + one consonant (omit, regret, transfer) takes -ed, -ing or -able; the options differ in single vs double.",
   "1. Say the base word and find the stress: om-IT, re-GRET.\n2. If the last syllable is stressed and the suffix starts with a vowel, double the consonant.\n3. Do not double any other letter (the m of omit stays single).\n\n*Why it works:* doubling keeps the stressed short vowel short.",
   "Omitted / Ommitted / Omited / Ommited", "**Omitted** — stress on -MIT, so the t doubles; the m stays single."),
 P("sdb2", "Unstressed final syllable: no double", "very common",
   "The base is stressed on an earlier syllable (DEvelop, BUDget, PROFit) and a double-letter option looks tempting.",
   "1. Say the base: DE-vel-op, BUD-get.\n2. The stress is not on the last syllable, so add the suffix directly.\n3. Reject every option with a doubled final consonant.\n\n*Why it works:* with no stress on the last syllable there is no short vowel to protect.",
   "Developed / Developped / Develloped / Divelopped", "**Developed** — stress on -VEL-, so the p stays single."),
 P("sdb3", "Words with two sets of doubles", "common",
   "The word is from the two-sets list: accommodation, possession, address, success, assassinate.",
   "1. Count both sets of doubles: accommodation = cc + mm.\n2. Remove any option that has only one set.\n3. Check the ending last (-tion, -sion).\n\n*Why it works:* distractors usually keep one double and drop the other, so a quick count finds them.",
   "Possession / Posession / Possesion / Posesion", "**Possession** — ss + ss; each distractor drops at least one double."),
 P("sdb4", "Words with only one double", "common",
   "The word is often over-doubled: necessary, recommend, tomorrow, harass, occasion.",
   "1. Recall which letter doubles: necessary -> s only; recommend -> m only.\n2. Remove options that double the wrong letter or both letters.\n3. Check the vowels last (necessary, not necessery).\n\n*Why it works:* this group is tested by adding a double where there is none.",
   "Necessary / Neccessary / Necessery / Neccesary", "**Necessary** — one c, double s: 'one collar, two sleeves'."),
]}

S["spell-suffix-endings"] = {
"notes": """### Two corrections to the lists above
The noun from maintain is **maintenance** (never 'maintainance'), and the -ible word meaning 'able to be heard' is **audible** (there is no 'auditible'). Horrible, terrible, visible, audible and feasible all take -ible because their stems (horr-, terr-, vis-, aud-, feas-) are not complete English words.

### -able or -ible: the whole-word test
- If the stem is a **complete word**, the ending is usually **-able**: accept-able, comfort-able, depend-able, remark-able, avail-able, desir(e)-able.
- If the stem is **not a complete word**, the ending is usually **-ible**: poss-ible, horr-ible, vis-ible, cred-ible, ed-ible, plaus-ible, feas-ible.
- A few complete-word stems still take -ible: accessible, flexible, digestible, contemptible, collapsible. Learn these as a short list.
- Many -ible words have a related **-ssion** or **-sion** noun: permission/permissible, division/divisible, comprehension/comprehensible.
- **indispensable** is the most common trap: the stem 'dispense' is a complete word, so it takes -able.

### -ance/-ence and -ant/-ent go together
A word's -ance/-ence noun and its -ant/-ent adjective share the same vowel. Learn one form and you have the other:
- relevant -> relevance; significant -> significance; tolerant -> tolerance; brilliant -> brilliance
- permanent -> permanence; confident -> confidence; obedient -> obedience; coincident -> coincidence
- surveillance, perseverance, maintenance, grievance take -ance (persevere -> perseverance).
When stuck, think of the matching adjective: 'relevent' is wrong because 'relevant' is the adjective.

### Keep or drop the final e
- **Drop the e** before a suffix starting with a vowel: write -> writing, desire -> desirable, argue -> arguing, use -> usable, hope -> hoping.
- **Keep the e** before a suffix starting with a consonant: hope -> hopeful, manage -> management, care -> careful. Exceptions: argue -> argument, true -> truly, nine -> ninth, whole -> wholly.
- **Keep the e after soft c or g** before a or o, so the letter stays soft: notice -> noticeable, change -> changeable, courage -> courageous, advantage -> advantageous, outrage -> outrageous.

### The -y ending
Change y to i after a consonant, keep it after a vowel: happy -> happiness, busy -> business, carry -> carried, but enjoy -> enjoyment, pay -> payable. Keep y before -ing: carrying, studying.

### How to use this in the exam
1. Find the part where the options differ — usually the last four or five letters.
2. Apply one test: whole word? a matching adjective or noun? soft c or g?
3. If no test applies, it is a word you need to know by heart — use the family lists.

### Quick revision
- Complete-word stem -> -able (acceptable, indispensable); non-word stem -> -ible (possible, visible, audible).
- -ssion/-sion noun often signals -ible: permissible, divisible, comprehensible; learn accessible and flexible as exceptions.
- -ance goes with -ant, -ence with -ent: relevant/relevance, permanent/permanence.
- Drop e before a vowel suffix (writing, desirable); keep it after soft c or g (noticeable, advantageous).
- Maintenance, not maintainance; truly, argument, ninth drop the e.
""",
"patterns": [
 P("sse1", "-ance or -ence", "very common",
   "The options differ only in -ance/-ence (perseverance, coincidence, surveillance).",
   "1. Think of the matching adjective or verb: coincident -> coincidence.\n2. Match the vowel: -ant goes with -ance, -ent with -ence.\n3. If there is no matching form, use the word families you know (surveillance, perseverance).\n\n*Why it works:* a noun and its adjective share the same vowel.",
   "Coincidence / Coincidance / Coinsidence / Coincedence", "**Coincidence** — coincident -> coincidence."),
 P("sse2", "-able or -ible", "common",
   "The options differ in -able/-ible (responsible, indispensable, accessible).",
   "1. Remove the ending: is the stem a complete word?\n2. Complete word -> -able; not a word -> -ible.\n3. Check the -sion clue: permission/permissible, division/divisible.\n\n*Why it works:* -able was added to complete English words; -ible came with Latin stems.",
   "Responsible / Responsable / Resposible / Responsibel", "**Responsible** — 'respons' is not a complete word, so the ending is -ible."),
 P("sse3", "Keep or drop the final e", "common",
   "The base ends in e (write, advantage, notice) and the options differ in whether the e stays.",
   "1. Does the suffix start with a vowel? Drop the e (writing, desirable).\n2. Is there a soft c or g before a or o? Keep the e (advantageous).\n3. Consonant suffix: keep the e (management), except truly, argument, ninth.\n\n*Why it works:* the e either marks a long vowel or keeps c and g soft; it goes only when it has no job to do.",
   "Advantageous / Advantagous / Advantageus / Advantagious", "**Advantageous** — the e keeps the g soft before -ous."),
 P("sse4", "-ant or -ent adjective", "common",
   "The options differ in -ant/-ent (relevant, permanent, brilliant), usually along with a vowel swap earlier in the word.",
   "1. Think of the matching noun: relevance -> relevant, permanence -> permanent.\n2. Check the letters before the ending as well (re-LE-vant, per-MA-nent).\n3. Remove any option that fails either check.\n\n*Why it works:* the noun keeps the same vowel as the adjective.",
   "Relevant / Relevent / Revelant / Relavant", "**Relevant** — relevance -> relevant; 'revelant' also swaps two letters."),
]}

S["spell-trap-words"] = {
"notes": """### Corrections to the trap list above
Three entries in the trap list above need a closer look:
- **parallel** has **one r** and a **double l in the middle**, with a single l at the end: p-a-r-a-l-l-e-l.
- **skiing** is right (ski + ing); the only misspelling tested is 'sking'.
- **ninth**: nine drops its e before -th (ninth), but keeps it in **ninety** and **nineteen**.
Also, **cacti** and **cactuses** are both accepted plurals, and both **collectable** and **collectible** are standard. Neither of these should be the only answer in an item.

### Silent letters
Many trap words have a letter you do not pronounce:
- **Silent p:** psychology, pneumonia, receipt, cupboard, raspberry.
- **Silent d:** Wednesday, handkerchief, grandson.
- **Silent b:** debt, doubt, subtle, plumber, tomb.
- **Silent h:** rhythm, rhyme, exhaust, exhibition, ghost.
- **Silent s:** island, aisle, debris.
- **Silent n after m:** autumn, column, condemn, solemn.
Say the word slowly the way it is spelt (WED-NES-DAY) to remember the silent letter.

### -ceed, -cede and -sede
- **-ceed:** only proceed, succeed, exceed (and their forms: proceedings, succeeded, exceeding).
- **-sede:** only supersede.
- **-cede:** every other word — precede, recede, concede, secede, intercede.
Also note the vowel change in the related words: proceed -> **procedure** and succeed -> **success** keep the c but not the double e.

### When a root word changes its letters
- **pronounce -> pronunciation** — the o after 'pron' disappears (pro-NUN-ci-a-tion).
- **explain -> explanation**, **maintain -> maintenance**, **exclaim -> exclamation** — ai becomes a or e.
- **curious -> curiosity**, **generous -> generosity** — the u disappears.
- **four -> forty** (but fourteen), **nine -> ninth**.
- **argue -> argument**, **true -> truly**, **due -> duly**.
Remember these as pairs; the exam usually offers a spelling that keeps the root unchanged.

### Borrowed words
French and Latin borrowings keep their original spelling:
- **entrepreneur** (entre + pre + neur), **bureaucracy** (bureau + cracy), **connoisseur**, **rendezvous**, **reservoir**, **silhouette**, **camaraderie**, **liaison**, **questionnaire**.
Break them into parts: bureau + cracy, entre + pre + neur. The common mistake is to swap letters within a part ('entreprenuer').

### Quick revision
- Silent letters: psychology, Wednesday, subtle, rhythm, island, autumn.
- Only proceed, succeed and exceed end in -ceed; only supersede ends in -sede; everything else ends in -cede.
- Root changes: pronunciation, explanation, forty, ninth, argument, truly.
- Borrowed words: learn by parts (bureau + cracy, entre + pre + neur).
- Parallel = one r, double l in the middle.
""",
"patterns": [
 P("stw1", "Silent letter", "very common",
   "The word contains a letter you do not pronounce (Wednesday, psychology, subtle) and one or more options leave it out.",
   "1. Recall the silent letter by saying the word as it is spelt (WED-NES-DAY).\n2. Remove every option that drops it.\n3. Check the order of the remaining letters.\n\n*Why it works:* the most common mistake is to spell the word the way it sounds.",
   "Wednesday / Wendesday / Wensday / Wednsday", "**Wednesday** — Wed + nes + day; the d is silent but written."),
 P("stw2", "-ceed, -cede or -sede", "common",
   "The options differ in -ceed / -cede / -sede, or in the vowel before it (precede, succeeded, exceed).",
   "1. Is it proceed, succeed or exceed? Then -ceed.\n2. Is it supersede? Then -sede.\n3. Otherwise -cede.\n\n*Why it works:* the list of exceptions is only four words long.",
   "Precede / Preceed / Presede / Priceed", "**Precede** — not one of the three -ceed words, so -cede."),
 P("stw3", "Root letter changed in the longer word", "common",
   "The word comes from a root that changes its letters: pronounce -> pronunciation, nine -> ninth, four -> forty.",
   "1. Think of the root and how it changes.\n2. Remove the option that keeps the root unchanged (pronounciation, nineth).\n3. Check the remaining options letter by letter.\n\n*Why it works:* the most common wrong option keeps the root word as it is.",
   "Pronunciation / Pronounciation / Pronuntiation / Prononciation", "**Pronunciation** — the o of pronounce disappears: pro-nun-ci-a-tion."),
 P("stw4", "Borrowed word", "common",
   "A French or Latin borrowing: entrepreneur, bureaucracy, connoisseur, rendezvous, silhouette.",
   "1. Split the word into parts: bureau + cracy.\n2. Check each part in each option.\n3. Remove options with swapped letters inside a part (entreprenuer).\n\n*Why it works:* borrowed words keep their original spelling, so checking part by part is reliable.",
   "Bureaucracy / Beaurocracy / Bureaucrasy / Burocracy", "**Bureaucracy** — bureau + cracy."),
]}

S["spell-strategy"] = {
"notes": """### Three question types
1. **Choose the correct spelling** — four versions of one word. Compare the options letter by letter and focus on the spot where they differ.
2. **Find the misspelt word** — four different words, one of them wrong. Here you cannot compare options, so check each word against what you know: its doubles, its ie/ei, its ending, any silent letters.
3. **Misspelt word in a sentence** — the same as type 2, but the words are inside a sentence. Ignore the meaning and check each listed word on its own.
A fourth type asks for a **plural or related form** (criterion -> criteria). This depends on knowing classical plurals.

### Checking a word you cannot compare
For type 2 and type 3 items, run four quick checks on each word:
1. **Doubles:** does it have the right double letters? (tomorrow: 1 m, 2 r; harass: 1 r, 2 s)
2. **ie/ei:** does the pair follow the sound rule? (achievement)
3. **Ending:** -ance/-ence, -able/-ible, -ceed/-cede?
4. **Silent or dropped letters:** Wednesday, government, pronunciation.
The misspelt word usually fails one check clearly. If three words pass easily, the fourth is the answer even if you are unsure of it.

### Classical plurals
Latin and Greek nouns keep their original plurals:
- **-on -> -a:** criterion -> criteria, phenomenon -> phenomena.
- **-is -> -es:** crisis -> crises, analysis -> analyses, thesis -> theses, basis -> bases.
- **-us -> -i:** stimulus -> stimuli, radius -> radii, nucleus -> nuclei.
- **-um -> -a:** medium -> media, datum -> data, curriculum -> curricula.
Adding -s to these plurals (criterias, crisises) is always wrong.

### Long words: split them into syllables
For long words like conscientious, miscellaneous or unnecessary, write the syllables and check each one:
- con-sci-en-tious (con + science + tious)
- mis-cel-la-ne-ous (double l, then -aneous)
- un-ne-ces-sa-ry (un + necessary: two n's where the prefix meets the word)
Prefixes do not change the root: un + necessary = unnecessary, mis + spell = misspell, dis + satisfied = dissatisfied. The double letter where the prefix meets the root is a common test.

### Time and guessing
A spelling item should take 20-30 seconds. If you are unsure between two options, choose the one that follows a rule (sound rule, stress rule, whole-word rule) over the one that simply looks familiar — setters often write the wrong option to look natural.

### Quick revision
- Choose-the-correct: compare the options at the one spot where they differ.
- Find-the-misspelt: check doubles, ie/ei, ending and silent letters for each word.
- Classical plurals: criteria, phenomena, crises, analyses, stimuli, radii, media — never add -s.
- Long words: split into syllables; prefix + root keeps both letters (unnecessary, misspell).
- Unsure between two: pick the one that follows a rule.
""",
"patterns": [
 P("sst1", "Find the misspelt word (four different words)", "common",
   "The four options are different words and the question asks which one is spelt wrongly.",
   "1. Check each word against its known signature: doubles, ie/ei, ending, silent letters.\n2. Mark the words that pass clearly.\n3. The one that fails is the answer.\n\n*Why it works:* three words are correct, so one clear failure decides the item.",
   "Tommorow / Receive / Beginning / Calendar", "**Tommorow** is wrong — tomorrow has one m and double r."),
 P("sst2", "Misspelt word inside a sentence", "common",
   "A sentence is given and the options are four words from it; one is misspelt.",
   "1. Ignore the meaning of the sentence.\n2. Check each option on its own, as in a find-the-misspelt item.\n3. Do not be distracted by British forms such as recognised — these are correct.\n\n*Why it works:* the sentence is only a setting; the test is still one word.",
   "The comittee will announce its decision on Wednesday. Options: comittee / announce / decision / Wednesday",
   "**comittee** is wrong — committee has double m, double t, double e."),
 P("sst3", "Classical plural", "occasional",
   "The question asks for the plural of a Latin or Greek noun (criterion, crisis, analysis, phenomenon).",
   "1. Identify the ending: -on, -is, -us, -um.\n2. Apply the classical change: -on -> -a, -is -> -es, -us -> -i, -um -> -a.\n3. Reject any option that adds -s to the plural.\n\n*Why it works:* these words keep their original plurals in formal English.",
   "Plural of crisis: crises / crisises / crisis / crisies", "**crises** — -is becomes -es."),
 P("sst4", "Long word: check syllable by syllable", "common",
   "A long word (conscientious, miscellaneous, unnecessary) with options that differ at one or two places.",
   "1. Split the word into syllables.\n2. Check each syllable in each option, especially where a prefix meets the root.\n3. The option with every syllable correct is the answer.\n\n*Why it works:* long words are hard to take in at a glance, but each syllable is easy to check.",
   "Unnecessary / Unneccessary / Unecessary / Unnecesary", "**Unnecessary** — un + necessary: double n at the join, one c, double s."),
]}
