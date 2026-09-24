# Error-spotting notes + patterns, part A: checklist, sva, tense.
from _lib import P

S = {}

S["es-checklist"] = {
"notes": r"""### What error-spotting asks
A sentence is cut into three or four parts, printed with slashes. One part contains a grammar error, and you must pick that part. You do not have to correct the sentence — only to locate the fault. SSC, Railway and Banking papers ask 3 to 5 of these in the English section.

Think of yourself as a checker at a toll gate: vehicles (parts) pass by, and you stop the one that is overloaded. You do not unload it — you only stop it.

### The eight checks, in attack order
1. **Subject-verb agreement**: find the true subject; ignore words between it and the verb. (*The quality of the mangoes **was** poor.*)
2. **Tense and time anchors**: does the verb match the time words? (*yesterday* → past; *since 2019* → perfect; *when/if* clauses about the future → present tense.)
3. **Verb form**: finite verb, gerund, infinitive. (*He enjoys **singing***, not *to sing*.)
4. **Article**: a/an by sound; the for known or one-of-a-kind.
5. **Preposition**: fixed pairs — *angry with, insist on, consist of.*
6. **Pronoun and conjunction**: case (*between you and me*), relative (*whom we met*), correlative pairs (*no sooner…than*).
7. **Degree of comparison**: *bigger*, never *more bigger*; *superior to*, never *than*.
8. **Word choice and redundancy**: *return back → return*; *effect → affect*.

### The method: three passes
- **Pass 1 — read for sense.** Read the whole sentence. An error often makes the meaning silly, and the nonsense points at the part.
- **Pass 2 — find the verb and its subject.** Cover the interrupting phrase with your finger. Half of all errors die here.
- **Pass 3 — walk the checklist.** Move through the eight checks in order; stop at the first rule that convicts a part.

### The two-suspects rule
Sometimes two parts look wrong. Ask: *which one breaks a RULE, and which one merely looks odd?*
- "No sooner had / the results **were declared** / than students began / celebrating." — Part 1 looks odd (had?) but is correct; part 2 breaks the rule that after *had* the participle follows (*had been declared*). Trust the rule, not the feeling.

### "No error" discipline
When "No error" is an option, most papers keep 2 or 3 no-error questions in a set. Do not invent a fault: if every part passes the checklist, choose "No error" without fear. But never choose it merely because nothing jumped out — run the eight checks first.

### Where errors usually hide
- The verb almost always hides its fault next to an interrupting phrase (*of the mangoes, as well as the players, along with his friends*).
- The last part often carries the *since/for*, *a/an*, or tag-question trap, because eyes slow down by then.
- A part that merely ends with a full stop is rarely the error.

### Time plan
About 30 to 40 seconds per question. If two passes find nothing, mark your best guess and move on; return only if time remains.

### Quick revision
- Read for sense → find subject-verb core → walk the 8 checks.
- Interrupting phrases hide agreement errors; cover them with a finger.
- Rule beats feeling: pick the part that breaks a rule, not the one that merely looks odd.
- *No error* is a real option — but earn it by finishing the checklist.
- Common faults: agreement, tense anchor, verb form, article, preposition pair, pronoun case, comparison, redundancy.
""",
"patterns": [
 P("esc1", "Divided sentence — find the faulty part (no 'No error' option)", "very common",
   "The stem says the sentence is divided into parts and one part contains an error; four options are the four parts themselves.",
   "1. Read the whole sentence for sense.\n2. Find the verb and its true subject; cover interrupting phrases.\n3. Walk the 8-point checklist (agreement, tense, verb form, article, preposition, pronoun, comparison, word choice).\n4. Pick the part that breaks a rule.\n\n*Why it works:* the format never hides the fault's location; a rule-based scan finds it faster than intuition.",
   "\"The number of scholarships / have increased / this year / across the state.\"",
   "True subject = the number (singular), though *scholarships* sits next to the verb. Part 2 breaks the rule: **have increased → has increased**. Pick part 2."),
 P("esc2", "Divided sentence with 'No error' as an option", "very common",
   "The sentence is divided into three parts and the fourth option is 'No error'.",
   "1. Run the same 8-check scan.\n2. If every part passes, accept 'No error' — do not manufacture a fault.\n3. If one part fails, pick it and ignore the 'No error' bait.\n\n*Why it works:* papers mix 2-3 no-error items into a set to punish guessers on both sides — those who never pick it and those who always pick it.",
   "\"She has been / living in this colony / since her marriage.\" Options: the three parts / No error",
   "Has been living (perfect, correct); in this colony (fine); since her marriage (point of time with since, correct). All parts pass → **No error**."),
 P("esc3", "Two suspicious parts — the rule decides", "common",
   "Two parts look doubtful at first glance; one merely feels odd while the other breaks a definite rule.",
   "1. Mark both suspects.\n2. For each, name the rule it would break.\n3. A part with no rule against it is innocent, however odd it feels; pick the part you can convict by a named rule.\n\n*Why it works:* setters place one 'feel-bait' and one true error; intuition convicts the bait, rules convict the error.",
   "\"No sooner had / the results were declared / than students began / celebrating outside.\"",
   "Part 1 feels odd ('had'?) but *no sooner had* is exactly right. Part 2 breaks a rule: after *had*, the participle is needed → *had been declared*. Pick part 2."),
 P("esc4", "Fragments from different sentences — find the faulty fragment", "occasional",
   "Each option is a fragment of a DIFFERENT sentence; only one fragment is ungrammatical.",
   "1. Treat each option as a mini-sentence and run the 8-check scan on it, one at a time.\n2. Find the true subject of each fragment before judging its verb.\n3. Exactly one option will fail a rule; the other three are complete, correct pieces.\n\n*Why it works:* fragments disguise agreement errors, because the subject and verb sit far apart in a short phrase.",
   "(a) The news of the floods have reached (b) The furniture in these rooms is (c) Mathematics is my favourite (d) Neither of the two answers is",
   "*News* is singular (a fails: **has** reached). Furniture, mathematics and neither-of are all singular subjects with singular verbs (is/my favourite/is) — correct. Pick (a)."),
]}

S["es-sva"] = {
"notes": r"""### The core idea
The verb must match its **true subject** in number: singular subject → singular verb (with -s in the present), plural subject → plural verb (no -s). The whole game of subject-verb agreement (SVA) is finding the true subject, because the exam hides it behind interrupting words.

### Find the true subject: cover the middle
The subject is NEVER inside a phrase that begins with *of, with, along with, as well as, together with, besides, like, unlike, including*.
- Correct: The **list** of candidates **is** long. Incorrect: The list of candidates **are** long.
- Correct: The captain, as well as the players, **was** felicitated. Incorrect: …**were** felicitated.
- Correct: The quality of the mangoes **was** poor.
Ask: *what thing does the sentence talk about?* That word is your subject.

### Each, every, everyone, one of — always singular
- Correct: Each of the boys **has** submitted. Incorrect: Each of the boys **have** submitted.
- Correct: Every one of the players **was** fit.
- Correct: One of my friends **is** a pilot. (subject = one, not friends)
- **Many a + singular noun** takes a singular verb: Correct: Many a student **has** failed. Incorrect: Many a student **have** failed.

### Either/or and neither/nor — the nearness rule
With *either…or* and *neither…nor*, the verb agrees with the **nearer** subject.
- Correct: Neither the manager nor his **assistants were** present.
- Correct: Either Ramesh or his **cousins are** coming.
- But *neither of / either of + plural noun* is singular: Correct: Neither of the answers **is** correct.

### A number of vs the number of
- **A number of** = many → plural verb: A number of students **were** absent.
- **The number of** = the count → singular verb: The number of students **was** small.

### Collective nouns and special singulars
- Collective nouns (team, committee, jury, family) usually take a singular verb: The committee **has** published its report.
- Nouns that look plural but are singular: news, mathematics, physics, economics: The news **is** good.
- Pair nouns (scissors, trousers, spectacles) take a plural verb: My spectacles **are** missing.
- Amounts and distances as one unit take a singular verb: Ten kilometres **is** a long walk.
- Two nouns joined by *and* usually take a plural verb, BUT a single idea or one person takes singular: *Bread and butter **is** his breakfast*; *The poet and philosopher **has** arrived* (one person).

### Quick check in three steps
1. Underline the verb. 2. Cross out every phrase between the verb and the noun before it. 3. Match number with the remaining noun, then apply the special rules above.

### Quick revision
- Never let the nearest noun decide — cover the interrupting phrase.
- each / every / one of / many a / neither of → singular verb.
- neither…nor / either…or → verb agrees with the NEARER subject.
- a number of → plural; the number of → singular.
- news, mathematics, physics → singular; spectacles, scissors → plural.
- as well as, along with, with → verb follows the FIRST subject.
""",
"patterns": [
 P("esv1", "'One of / every one of + plural noun' agreement", "very common",
   "The sentence has 'one of the …' or 'each/every one of the …' just before the verb, and the options differ in the verb's number.",
   "1. Remember: the subject is ONE (or each/every one), not the plural noun after 'of'.\n2. Singular subject → singular verb.\n3. Check the tense separately; number is decided first.\n\n*Why it works:* the plural noun sits next to the verb and pulls the eye; the rule outranks the pull.",
   "\"One of the laptops displayed at the expo (1) ______ sold within an hour.\" Choose the error: were / was / is / are",
   "Subject = one (singular) → one **was** sold. 'Were sold' is the error."),
 P("esv2", "Either…or / neither…nor — verb follows the nearer subject", "very common",
   "Two subjects joined by either…or or neither…nor, with the verb placed after the second one.",
   "1. Ignore the first subject entirely.\n2. Look at the subject just BEFORE the verb (the nearer one).\n3. Match the verb to that subject's number.\n\n*Why it works:* the nearness rule is absolute in standard grammar, and the setter always makes the two subjects differ in number.",
   "\"Neither the collector nor his assistants (1) ______ available at the camp site.\" was / were / is / has been",
   "Nearer subject = assistants (plural) → **were** available. 'Was' agrees with the distant 'collector' and is wrong."),
 P("esv3", "Each / every / many a + singular verb", "common",
   "The subject begins with each, every, many a, or every…and every….",
   "1. Each, every and many a are unconditionally singular.\n2. Even 'every boy and every girl' stays singular when *every* repeats before both nouns.\n3. Match the verb (and the following possessive, which may be his/her, not their).\n\n*Why it works:* these words point to members one at a time, so English keeps the verb singular.",
   "\"Every man and every woman in the village (1) ______ counted in the survey.\" were / was / are / have been",
   "'Every … and every …' keeps the verb singular → **was** counted. 'Were' wrongly follows the pair idea."),
 P("esv4", "A number of vs the number of", "common",
   "The subject phrase is 'a/the number of + plural noun' — the only difference is the small word a/the.",
   "1. 'A number of' means MANY → plural verb.\n2. 'The number of' means THE COUNT → singular verb.\n3. Read the article before 'number' slowly; the whole question lives in it.\n\n*Why it works:* one letter of meaning (indefinite vs definite) flips the number, and the options exploit the miss.",
   "\"The number of accidents on this highway (1) ______ fallen after the new signals.\" have / has / are / were",
   "'The number of' = the count, singular → **has** fallen. 'Have fallen' treats it as plural."),
]}

S["es-tense"] = {
"notes": r"""### Tense errors: the anchor decides
Every sentence sits at a point in time, fixed by an **anchor** — a word or phrase that names the time (yesterday, since 2019, by the time, as soon as). The verb must obey the anchor. Tense questions fail when the verb and the anchor disagree.

### The main anchors and their verbs
| Anchor | Tense | Correct / Incorrect |
|---|---|---|
| yesterday, last week, ago, in 2019 | simple past | He **left** two days ago. / ~~He has left two days ago.~~ |
| since + point, for + length, so far, yet, already, just | perfect forms | She **has been teaching since 2015.** |
| every day, usually, now (habit) | simple present | The shop **opens** at nine. |
| when / if / until / as soon as + future meaning | simple present | **~~will open~~ → opens** |
| earlier of two past events | past perfect | The train **had left** before I reached. |
| universal truths | simple present | The earth **moves** round the sun. |

### Rules examiners love
1. **Time and condition clauses never take *will*.** After *when, before, after, until, as soon as, if, unless* pointing to the future, use the simple present: Correct: I will call you **when the meeting ends**. Incorrect: …**when the meeting will end**.
2. **Since vs for**: *since* + point of time (*since 2015, since morning*); *for* + length (*for ten years*). Incorrect: *since ten years*.
3. **Past perfect for the earlier event.** When two past actions are narrated, the earlier one takes *had + participle*: Correct: The patient **had died** before the doctor arrived. Signal words: *by the time, before, already*.
4. **Present perfect refuses finished-time words.** *Have gone* clashes with *yesterday, last week, in 2019*: Incorrect: *He has left for Hyderabad two days ago.* → Correct: *He left for Hyderabad two days ago.*
5. **Universal truths stay in the simple present**, even inside a past sentence: The teacher explained that the earth **moves** (not *moved*) round the sun.
6. **Sequence of tenses**: a past reporting verb pulls the reported clause into past forms — *said that she **was** busy* — but a universal truth is exempt (rule 5).

### Two-step method for tense questions
1. Find the anchor: circle the time words in every part.
2. Check the verb against the anchor table. If a verb sits inside a *when/if/until* clause with *will* in it, or next to *ago* in a perfect tense, you have found the error.

### Quick revision
- *ago / yesterday / last…* → simple past only; never with has/have.
- *since* + point, *for* + length — never *since ten years*.
- *when/if/until/as soon as* + future meaning → simple present (no *will* inside the clause).
- Earlier of two past events → past perfect (*had* + participle), cued by *by the time, before, already*.
- General truths stay simple present, even in reported past speech.
""",
"patterns": [
 P("est1", "Will inside a when / if / until clause", "very common",
   "The sentence talks about the future but the clause beginning with when/if/until/as soon as contains will + verb.",
   "1. Find the time or condition word (when, if, until, before, as soon as).\n2. If it points to the future, its clause must use the simple present.\n3. *Will* stays only in the main clause.\n\n*Why it works:* English fixed this rule long ago; the future helper never enters the time clause.",
   "\"The chief guest will not leave the venue until the cultural programme (1) ______.\" will conclude / concludes / concluded / is concluding",
   "*Until*-clause about the future → simple present: **concludes**. 'Will conclude' inside the clause is the error."),
 P("est2", "Since vs for", "very common",
   "A perfect or perfect-continuous verb is followed by a time phrase, and the choice is between since and for.",
   "1. Ask what the time phrase names: a POINT (2015, morning, marriage) or a LENGTH (ten years, two hours).\n2. Point → since; length → for.\n3. 'Since ten years' type phrases are planted errors.\n\n*Why it works:* the two words divide all time references between them; mixing them breaks the sentence.",
   "\"My uncle has been teaching in this school (1) ______ fifteen years.\" since / for / from / during",
   "Fifteen years is a length → **for**. 'Since fifteen years' is the classic planted error."),
 P("est3", "Past perfect for the earlier of two past events", "common",
   "Two past actions appear in one sentence, often with before, after, by the time, or already.",
   "1. Put the two actions on a timeline.\n2. The earlier one takes had + participle; the later one takes simple past.\n3. A plain past where the perfect belongs (or *will* after 'by the time') is the error.\n\n*Why it works:* past perfect exists precisely to mark the earlier of two pasts; dropping it erases the order.",
   "\"When we reached the hall, the play (1) ______, so we watched from the back.\" already began / had already begun / has already begun / was already beginning",
   "The play started BEFORE we reached → earlier event → past perfect: **had already begun**. 'Already began' loses the order."),
 P("est4", "Present perfect with a finished-time word", "common",
   "A has/have/had + participle sits next to yesterday, ago, last week, or another closed time slot.",
   "1. Look for ago, yesterday, last…, in 2019 next to a perfect form.\n2. A closed time slot demands the simple past.\n3. Correct the perfect form to simple past (or drop the time word — but the part with the verb is the error).\n\n*Why it works:* the present perfect connects to NOW; a finished-time word cuts that connection.",
   "\"Ravi (1) ______ for Hyderabad two days ago to attend an interview.\" has left / left / had left / was leaving",
   "'Two days ago' is a closed slot → simple past: **left**. 'Has left…ago' is the planted error."),
 P("est5", "Universal truth / general fact pulled into the past", "occasional",
   "A sentence reports what someone said or explained, and the reported clause states a scientific or permanent fact.",
   "1. Check the reported clause for a general truth (the earth, water, the sun, metals).\n2. Such truths stay in the simple present even after a past reporting verb.\n3. A past form there (moved, revolved) is the error.\n\n*Why it works:* sequence of tenses has a standing exception for facts that are always true.",
   "\"The teacher explained that the earth (1) ______ around the sun.\" moved / moves / had moved / was moving",
   "Universal truth → present: **moves**. 'Moved' wrongly applies the sequence-of-tenses rule to a permanent fact."),
]}
