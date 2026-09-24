# Sentence-improvement notes + patterns, part A: elimination, tense-sequence, agreement.
from _lib import P

S = {}

S["si-elimination"] = {
"notes": r"""### What sentence improvement asks
One segment of the sentence is printed in bold. Four substitutes are offered, usually including **No substitution required**. Your job: decide whether the bold part is faulty, and if it is, pick the substitute that repairs it — and only it.

### The elimination ladder (four rungs)
1. **Name the highlighted part's job.** Is it a verb, a tense, an article + noun, a preposition, a connector, a comparison phrase? The job tells you which rulebook page to open.
2. **Run the matching rule.** Verb → agreement and tense anchors; article → sound rule; connector → fixed pairs. If the bold part survives its own rule, check whether any other rule touches it.
3. **Kill the repeat-fault options.** Many options repeat the very fault you are fixing (*more better → more good*). Kill them at once; they are not competitors.
4. **Kill the new-fault options.** Some options repair fault A but plant fault B (*Hardly…than* instead of *Hardly…when*). A substitute must be cleaner than the original, not differently wrong.
5. If the bold part is standard English, choose **No substitution required** without hesitation.

### The two-fault trap
Examiners build one option that fixes the visible fault and breaks a hidden rule:
- *My friend has gone to Delhi yesterday.* → the fault is *has gone* with *yesterday*; the fix is **went**. *Had gone* also removes the perfect, but it creates a wrong sequence (nothing earlier exists to outrank). One fix, two faults removed — that is the answer's test.

### Decoy families
Options usually come in families around the bold word:
- **Sound-alike / look-alike**: *effect / affect, loose / lose, advice / advise.*
- **Form-shifts**: adjective ↔ adverb (*brave / bravely*), noun forms (*braveness*).
- **Marker-doubles**: *more better, most shortest, more preferable.*
- **Helper-swaps**: *has / had / was / did* in every combination.
Learn to name the family; the correct option is the family member that matches the rule.

### Smallest-change principle
When two options both fix the fault, prefer the one that changes less. Exams reward the repair, not a rewrite. If an option replaces the whole structure while another fixes one word, test the one-word fix first.

### Timing
Improvement items are fast: 30 to 40 seconds. Read the sentence once fully, name the job, run the rule, walk the ladder.

### Quick revision
- Name the job of the bold part → open the matching rulebook page.
- Kill options that repeat the fault; kill options that plant a new fault.
- *No substitution required* is a full citizen — choose it when the original is standard.
- Watch decoy families: effect/affect, brave/bravely, more better, helper swaps.
- Two options both fix the fault? The smaller, cleaner change wins.
""",
"patterns": [
 P("sik1", "Single-fault fix with repeat-fault decoys", "very common",
   "The bold part has one clear fault; two or three options repeat the same fault in a new dress (more good for more better, was being for were).",
   "1. Name the fault and its rule.\n2. Strike out every option that still breaks that same rule.\n3. Compare the survivors — pick the clean, smallest repair.\n\n*Why it works:* repeat-fault decoys punish candidates who fix the fault only in their head and stop reading the options.",
   "\"The quality of the mangoes (were) not satisfactory this season.\" was / have been / No substitution required / are being",
   "True subject = quality (singular) → **was**. 'Have been' and 'are being' repeat the plural fault; strike them out, then compare *was* with the original."),
 P("sik2", "No-substitution discipline", "very common",
   "The bold part is already standard English; the other options are 'repairs' that break it.",
   "1. Run the full rule check on the bold part itself.\n2. If it passes every rule (tense anchor, agreement, pair, comparison), do not invent work.\n3. Choose **No substitution required** and move on.\n\n*Why it works:* papers include 2-3 correct originals per set; changing a correct sentence is the most common self-inflicted error.",
   "\"She (has been teaching) in this school since 2015.\" teaches / is teaching / No substitution required / has taught",
   "Perfect continuous + *since 2015* + still continuing → **has been teaching** is exactly right. Every offered change breaks the frame → No substitution required."),
 P("sik3", "Decoy families around the bold word", "common",
   "The options are near-twins of the bold word: adjective/adverb pairs, noun forms, effect/affect-type twins.",
   "1. Decide the job of the slot: describing a noun or an action?\n2. Cut the family members that do the wrong job (adverb where an adjective sits).\n3. Of the survivors, keep the one whose meaning fits the sentence.\n\n*Why it works:* option families are built from one word's relatives; sorting them by job (not by sound) clears the set.",
   "\"The soldier was praised for his (brave) act during the rescue.\" bravely / No substitution required / braveness / bravest",
   "The slot describes the noun *act* → adjective: **brave** is correct. *Bravely* (adverb), *braveness* (noun) and *bravest* (wrong count) are the family decoys → No substitution required."),
 P("sik4", "Two-fault trap options", "common",
   "One tempting option fixes the visible fault but plants a second one (a wrong sequence, a broken pair, a wrong part of speech).",
   "1. Fix the visible fault in your head first.\n2. Test every option that seems to fix it against the OTHER rules in the sentence (time words, pairs, count).\n3. Reject any option that needs a second repair; keep the option that leaves the sentence fully standard.\n\n*Why it works:* 'has gone yesterday → had gone yesterday' *feels* fixed; only the second pass exposes the new sequence fault.",
   "\"My friend (has gone) to Delhi yesterday to attend an interview.\" went / had gone / No substitution required / has went",
   "The anchor *yesterday* demands simple past → **went**. 'Had gone' removes the perfect but creates a sequence with no earlier event; 'has went' keeps the fault and adds another."),
]}

S["si-tense-sequence"] = {
"notes": r"""### The anchor decides, again
In improvement items the bold part is often a verb whose tense fights a visible anchor. Circle the anchor before touching the options.

| Anchor in the sentence | Required form |
|---|---|
| yesterday, last week, ago, in 2019 | simple past |
| since + point, for + length, so far, already, yet | perfect (or perfect continuous) |
| every day, at nine (habit) | simple present |
| when / if / until + future meaning | simple present inside the clause |
| by the time + past, earlier of two past events | past perfect |
| said / asked / told (past reporting) | backshifted past forms |

### Reported speech: two rules, not one
1. **Backshift**: after a past reporting verb, move the tense one step back — *has locked → had locked*, *will → would*, *is → was*.
2. **Statement order**: an indirect question loses question order — *asked why **he was** late* (never *why was he late*), and takes one connective only — *asked **whether*** (never *that whether*), *asked **why*** (never *that why*).

### Conditional frames travel in pairs
- Real future: **if + present, will + verb** → *If he apologises, I will withdraw the case.*
- Unreal present: **if + past (were for all persons), would + verb** → *If I were the collector, I would act.*
- Unreal past: **if + had + participle, would have + participle** → *If he had studied, he would have cleared.*
The bold verb may sit in either half; check that the pair matches one row of the table.

### Since / for with continuing action
*Since 2015, for twenty years, since childhood* + an action still true → **has/have been + -ing**: *He has been working in the same mill for twenty-two years* (not *is working*). The anchor *for + length* cannot live with the plain present continuous.

### Watch the second verb too
Some sentences carry two verbs and the anchor governs both. *He **has left** for Delhi and **will return** next month* — the anchor *next month* is future, so *will return* is right, and nothing else in the sentence pulls *has left* into the past. But *He **has left** for Delhi and **will return** next week* with *when he **will reach***… breaks: the when-clause must read *when he reaches*. After substituting the bold verb, glance at the unbolded verbs once — a fix that clashes with them is not a fix.

### How improvement differs from error-spotting
Here the wrong form is already underlined — your task is to produce the right form, not to find it. So after every fix, re-read the WHOLE sentence once: a substitute that fixes the verb but clashes with a word outside the bold part is a trap.

### Quick revision
- Circle the anchor first; the verb obeys it.
- ago / yesterday → simple past; since + point → perfect; for + length + continuing → has been -ing.
- Reported questions: backshift + statement order + one connective (why / whether).
- Conditionals come in three fixed pairs; match the pair, don't mix halves.
- Re-read the whole sentence after substituting — the trap may sit outside the bold part.
""",
"patterns": [
 P("sit1", "Anchor-based tense fix", "very common",
   "The bold verb's tense contradicts a time word sitting in plain sight (already, yesterday, by the time, every morning).",
   "1. Circle the anchor.\n2. Read the anchor's required form off the table.\n3. Pick the option that matches; reject options that shift tense again (has → had) without a second event.\n\n*Why it works:* tense questions are anchor questions; with the anchor circled, the options sort themselves.",
   "\"When I reached the station, the train (already left).\" had already left / has already left / No substitution required / already leaves",
   "The train left BEFORE I reached → earlier past event → **had already left**. *Has already left* reaches into the present and breaks the past story."),
 P("sit2", "Reported-speech backshift and order fix", "common",
   "The sentence reports what someone asked or said (asked, told, enquired) and the bold part keeps question order, misses the backshift, or glues 'that' to a wh-word.",
   "1. Spot the past reporting verb.\n2. Backshift the tense one step; restore statement order (subject before helper).\n3. Keep exactly one connective: why / whether / if.\n\n*Why it works:* indirect speech is direct speech pushed through two fixed machines — backshift and order — and options break one machine each.",
   "\"The teacher asked the boy (why was he) late again.\" why he was / No substitution required / why is he / that why he was",
   "Indirect question → statement order + backshift: asked **why he was** late again. 'Why was he' keeps question order; 'that why' glues two connectives."),
 P("sit3", "Conditional half repair", "common",
   "An if-sentence has mismatched halves: will inside the if-clause, or a real-future frame where an unreal one is meant (If I was → were).",
   "1. Read both halves of the conditional.\n2. Match them to one of the three fixed pairs.\n3. Real future takes if + present; unreal present takes were; unreal past takes had + participle.\n\n*Why it works:* the if-clause never hosts will (real future) or would have (unreal past); the options exploit exactly these two guests.",
   "\"If he (will apologise) sincerely, I will withdraw the complaint.\" apologises / No substitution required / would apologise / apologised",
   "Real future condition → if + **apologises**; the main clause keeps *will withdraw*. 'Would apologise' is the unreal-present form and breaks the pair."),
 P("sit4", "Since / for with a continuing action", "common",
   "The sentence names a starting point or a length of time (since 1998, for twenty years) while the bold verb is in a plain present or present continuous.",
   "1. Ask: does the action still continue? (since + a past point usually says yes.)\n2. Continuing action → has/have been + -ing (or has/have + participle for states).\n3. Reject the plain present and the continuous that ignores the length.\n\n*Why it works:* the perfect exists to tie a past starting point to now; the plain present cuts the tie.",
   "\"My father (is working) in the same mill for twenty-two years.\" has been working / No substitution required / works / had been working",
   "*For twenty-two years* + still employed → **has been working**. The plain continuous drops the 'still going' meaning that the length demands."),
]}

S["si-agreement"] = {
"notes": r"""### The audit: find the true subject
When the bold part contains (or ends in) a verb with a helper — *was/were, has/have, is/are, does/do* — run the agreement audit:
1. **Find the true subject**: the noun the sentence is about.
2. **Cross out the interrupters**: phrases that begin with *of, with, along with, as well as, together with, besides, including* never contain the subject.
3. **Match the helper** to the subject's number.

### Interrupters that hide the subject
- *The bundle of old files **was** sent*… (bundle, not files)
- *The captain, as well as the openers, **was** blamed*… (as-well-as adds; it does not make a plural)
- *The quality of the mangoes **was** poor.*
- *The list of holidays **has been** announced.*

### One-of / each-of / neither-of — singular, always
- *One of my cousins **has settled** in Wellington.*
- *Each of the candidates **is** to report at nine.*
- *Neither of the two answers **was** acceptable.*

### Nearness rule for paired subjects
With *either…or, neither…nor, not only…but also*, the verb agrees with the **nearer** subject:
- *Either the secretary or the joint secretaries **are** responsible.*
- *Not only the students but also the wardens **were** honoured.*

### Quantity and collective phrases
- **A number of** + plural noun → plural verb: *A number of films **have been** censored this month.*
- **The number of** → singular: *The number of films **has** fallen.*
- **Many a** + singular noun → singular: *Many a farmer **has** shifted to drip irrigation.*
- Amounts as one unit → singular: *Ten thousand rupees **is** a big amount.*
- Collective nouns (jury, committee) → usually singular with *its*.

### Compound subjects and the passive
Two nouns joined by plain *and* take a plural helper: *The principal and the secretary **were** present* (two people). But one person with one article is singular: *The principal and secretary **was** present* (one person holding both posts). In the passive, the same audit runs on the *be* helper: *The bridge **was** built* (singular subject) but *The bridges **were** built*. The helper is always the first place to look, because it moves with the subject while the participle never changes.

### In improvement format
The bold part usually holds only the helper (*was / were / has / have*) or helper + participle. Fix the helper to the true subject and keep the rest of the bold part untouched — the smallest change wins. If the original already agrees, **No substitution required** is the answer.

### Quick revision
- of / with / along with / as well as → never the subject; the noun BEFORE the phrase is.
- one of, each of, neither of, many a → singular helper.
- either…or / neither…nor / not only…but also → nearer subject.
- a number of → plural; the number of → singular; amounts as units → singular.
- Fix only the helper; leave the participle alone unless it too is faulty.
""",
"patterns": [
 P("sia1", "Interrupter-phrase agreement fix", "very common",
   "The bold helper (was/were, has/have) sits after 'X of Y' or 'X, as well as Y,' and was matched to the wrong noun.",
   "1. Cross out the of/with/as-well-as phrase.\n2. Read the sentence with only the true subject and the helper.\n3. Pick the helper that matches the subject's number, leaving the participle untouched.\n\n*Why it works:* the interrupter is designed to be heard as the subject; crossing it out removes the illusion.",
   "\"The captain, as well as the openers, (were) blamed for the collapse.\" was / No substitution required / have been / are",
   "The subject is **the captain**; 'as well as the openers' only adds information → the captain **was** blamed. The plural helpers repeat the illusion."),
 P("sia2", "One-of / each-of / neither-of fix", "very common",
   "The subject phrase begins with one of, each of, or neither of, and the bold helper is plural.",
   "1. Remember the head word: one, each, neither — all singular.\n2. The plural noun after 'of' is a decoy.\n3. Choose the singular helper (has, is, was).\n\n*Why it works:* these three openers are unconditionally singular, so the fix is mechanical once you see the opener.",
   "\"Each of the shortlisted candidates (are) to report by nine tomorrow.\" is / No substitution required / were / have been",
   "**Each** → singular → each **is** to report. 'Were' and 'have been' follow the plural noun, not the opener."),
 P("sia3", "Nearness-rule fix (or / nor / not only…but also)", "common",
   "Two subjects are joined by either…or, neither…nor, or not only…but also, and the bold helper agrees with the FIRST subject instead of the nearer one.",
   "1. Ignore the first subject.\n2. Look at the subject just before the bold helper.\n3. Match the helper to that nearer subject.\n\n*Why it works:* the nearness rule outranks every other consideration in paired subjects, and the setter always makes the two subjects differ in number.",
   "\"Either the secretary or the joint secretaries (is) responsible for the circular.\" are / No substitution required / was / has been",
   "Nearer subject = joint secretaries (plural) → **are** responsible. 'Is' and 'was' follow the distant 'secretary'."),
 P("sia4", "Quantity-phrase agreement fix (a number of / many a)", "common",
   "The subject is a quantity phrase — a number of, the number of, many a — and the helper's number contradicts the phrase's rule.",
   "1. Read the phrase slowly: a number of (plural) or the number of (singular)?\n2. many a + singular noun → singular, despite the plural meaning.\n3. Match the helper, keep the rest of the bold part as it is.\n\n*Why it works:* the article before 'number' is one letter of print with full control of the verb; 'many a' hides a singular under a plural meaning.",
   "\"A number of films (has been) censored this month.\" have been / No substitution required / are been / was",
   "**A number of** = many → plural: a number of films **have been** censored. ('The number of films has…' would be the singular frame.)"),
]}
