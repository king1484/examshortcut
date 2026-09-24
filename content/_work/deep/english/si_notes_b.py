# Sentence-improvement notes + patterns, part B: comparison-structure, precision-fixes, structure-inversion.
from _lib import P

S = {}

S["si-comparison-structure"] = {
"notes": r"""### The four comparison repairs
1. **Double marker**: *more better, most shortest, more preferable* → drop the extra word (*better, shortest, preferable*). A comparative or superlative is already marked; never mark it twice.
2. **Like with like (that of / those of)**: compare the same kind of thing. *The climate of Shimla is cooler than **that of** Delhi* (climate with climate); *The roads of Bhopal are wider than **those of** Indore* (roads with roads). *That* for a singular noun, *those* for a plural.
3. **Latin comparatives take to**: *senior to, junior to, superior to, inferior to, prior to, preferable to, prefer X to Y* — never *than*.
4. **Count the items**: exactly two → comparative (*the larger of the two*); three or more → superlative (*the largest of the five*). *Of all…* → superlative.

### How the options are built
- One option repeats the fault with new paint: *more better → more good*; *senior than → more senior than*.
- One option fixes the marker but breaks the count: *the most effective* kept where only two items exist.
- One option replaces *than Delhi* with a full clause (*Delhi's streets are*) — this produces a doubled sentence and is never the cleanest repair.
- The clean repair changes only what the fault requires.

### Words that are already marked
Some words carry their degree inside them and refuse extra markers: *better, worse, elder, former, latter, major, minor, superior, inferior, prior, senior, junior, preferable, perfect, unique, ideal, complete.* Say *better*, never *more better*; say *unique*, never *most unique* — a unique thing has no scale to climb. When such a word sits in the bold part, the correct option is almost always the plain form, and the decoys add *more/most* to it.

### Counting traps
The count is often announced inside the sentence: *of the two routes*, *of all the models*, *one of the finest*. Read that phrase before judging the form. *Of all* demands -est/most; *of the two* demands -er/more.

### Whole-sentence check
After substituting, re-read: the fix must not create a second fault. *Those of* with a singular noun, *prefer to* with *than* still trailing, or a superlative left without *the* — each is a new fault wearing the old fix's clothes.

### Quick revision
- more better / most shortest → cut the doubled marker.
- climate vs city → that of (singular) / those of (plural).
- senior, junior, superior, inferior, prior, preferable → TO; prefer → TO.
- of the two → comparative; of all → superlative (with the).
- Reject options that fix the marker but break the count, or turn the sentence into a doubled clause.
""",
"patterns": [
 P("sic1", "Double-marker fix", "very common",
   "The bold part contains more + -er or most + -est (more better, far more better, most shortest).",
   "1. Identify the marked form (better, shortest).\n2. Delete the doubled marker — the fix is a subtraction, not a substitution.\n3. Reject options that swap one doubling for another (more good) or destroy the comparison (good).\n\n*Why it works:* the double marker is pure redundancy; the correct option is the one that simply stops marking twice.",
   "\"The second model is (far more better) than the first.\" far better / No substitution required / more good / best",
   "**Far better** keeps the intensifier and drops the doubled marker. 'More good' re-doubles; 'best' breaks the two-item frame with *than*."),
 P("sic2", "That-of / those-of repair", "very common",
   "The sentence compares 'the X of A' with a bare place or person ('than Delhi', 'than most cereals'), so unlike things are being compared.",
   "1. Name the two things being compared.\n2. They must be the same kind: X with X.\n3. Insert that of (singular X) or those of (plural X) before the second item.\n\n*Why it works:* 'the roads of Bhopal vs Indore' compares roads with a city; *those of* quietly rebuilds the missing 'the roads of'.",
   "\"The streets of Mysuru are cleaner than (Bangalore).\" those of Bangalore / that of Bangalore / No substitution required / Bangalore's streets",
   "Streets (plural) vs streets → **those of Bangalore**. *That of* is singular; 'Bangalore's streets are' doubles the clause."),
 P("sic3", "Latin comparative / prefer repair", "common",
   "The bold part pairs senior, junior, superior, inferior, prior, preferable (or prefer) with than (or another wrong partner).",
   "1. Spot the Latin comparative or *prefer*.\n2. Its partner is **to**, always.\n3. Reject options that keep *than* in any dress (more senior than) or switch the meaning (prefer to → liking).\n\n*Why it works:* these words came into English with their own preposition attached; *than* belongs only to -er/more comparatives.",
   "\"My sister (prefers coffee than) tea in winter.\" prefers coffee to / No substitution required / prefer coffee to / is preferring coffee than",
   "**Prefer X to Y**: prefers coffee **to** tea. 'Prefer coffee than' keeps the fault; the bare 'prefer' loses the -s agreement."),
 P("sic4", "Count-of-items repair (two vs three-plus)", "common",
   "The sentence announces the count (of the two, of all, of the five) and the bold form has the wrong degree.",
   "1. Find the count phrase (of the two / of all).\n2. Two → comparative with the; three or more → superlative with the.\n3. Pick the option with the right degree and keep *the* in place.\n\n*Why it works:* the degree is not a style choice — the announced count fixes it, and the options include the neighbouring degree as the decoy.",
   "\"Iron is (the most useful) of the two metals for construction.\" the more useful / No substitution required / more useful / useful most",
   "**Of the two** metals → comparative: **the more useful**. 'The most useful' would need three or more metals; 'more useful' drops the required *the*."),
]}

S["si-precision-fixes"] = {
"notes": r"""### Small words, big marks
Many bold parts contain no verb at all — the fault is an article, a preposition, a doubled word, or a swapped twin. The options then differ by one or two small words, and speed comes from knowing the fixed pairs cold.

### Article: sound rule
- Vowel SOUND → an: *an hour, an honest man, an MLA, an X-ray.*
- Consonant sound → a: *a university, a European, a one-day match.*
- *A ancient route → **an** ancient route* (the a/an swap is the entire question).

### Preposition partners (frozen pairs)
- approve **of**, insist **on**, fond **of**, afraid **of**, capable **of**
- agree **with** (person) / **to** (proposal), angry **with** (person) / **at** (thing)
- apply **to** (office) / **for** (post), abide **by**, comply **with**
When the bold part is only the preposition, recall the partner and choose it — meaning will tempt you toward the wrong one.

### Redundancy: cut the echo
*revert back → revert; return back → return; repeat again → repeat; wrote back a reply → wrote a reply; final conclusion → conclusion.* One idea, one word. In improvement items the fix is a subtraction — the correct option is simply shorter.

### Swapped twins
| Wrong twin | Right twin | Why |
|---|---|---|
| advise (noun slot) | advice | advice = noun, advise = verb |
| effect (verb slot) | affect | affect = verb, effect = noun |
| loose (misplace) | lose | loose = not tight |
| principal (rule of conduct) | principle | principle = a rule |

### More pairs to keep ready
- **win / beat**: India *beat* Australia (beat takes the opponent); India *won* the match (win takes the prize).
- **say / tell**: she *said* that…; she *told me* that… (tell needs a person).
- **hear / listen**: *hear* is accidental; *listen to* is deliberate — *listen to the news*.
- **die of / die from**: *die of* a disease, *die from* an injury.
- **comprise**: the team *comprises* eleven players (no *of*); *is comprised of* in formal prose.
- **cope with**, deal with, but **cope up with is wrong** — a favourite Indian-English decoy.

### Pronoun case after prepositions
*Between you and **me*** (not I); *for **him** and **me***. The reflexive (*myself*) cannot replace the object pronoun — it is the standard decoy.

### Method
1. Name the small word's job (article? preposition? adverb of the pair?).
2. Recall the rule or pair.
3. Prefer the option that changes only the faulty word. If the bold part is already standard, choose **No substitution required**.

### Quick revision
- an hour, an MLA — a university, a European: sound, not spelling.
- approve of, insist on, fond of, agree with a person / to a plan.
- revert back, return back, repeat again → cut the echo.
- advice (n) / advise (v); affect (v) / effect (n); lose / loose.
- between you and me; myself never replaces me.
""",
"patterns": [
 P("sip1", "Preposition-partner repair", "very common",
   "The bold part is (or contains) the preposition after a verb or adjective, and the options are preposition swaps.",
   "1. Find the verb/adjective the preposition hangs on (approve, insist, fond).\n2. Recall its fixed partner: approve OF, insist ON, fond OF.\n3. Ignore options that change the rest of the phrase — only the partner needs repair.\n\n*Why it works:* preposition questions are memory questions; the partner is not chosen by logic but by usage.",
   "\"The committee does not approve (for) the proposal.\" of / No substitution required / with / to",
   "The fixed pair is approve **of** → 'does not approve of the proposal'. The other prepositions belong to different verbs."),
 P("sip2", "Article sound repair", "common",
   "The bold part is an article + word where the article contradicts the word's first sound (a honest, an useful, a MLA).",
   "1. Say the word after the article aloud.\n2. Vowel sound → an; consonant sound → a.\n3. Ignore the spelling — *hour* and *university* are the classic traps.\n\n*Why it works:* the rule follows speech, and exam words are picked so the letter and the sound disagree.",
   "\"The temple was built near (a ancient) trading route.\" an ancient / No substitution required / a ancients / the ancients",
   "**Ancient** begins with a vowel sound → **an ancient** trading route. Only the article needs repair — the smallest change wins."),
 P("sip3", "Redundancy cut", "very common",
   "The bold part carries an echo — return back, revert back, repeat again, wrote back a reply — and the correct option is simply shorter.",
   "1. Ask: does one word already contain the other's meaning?\n2. The repair is a subtraction: keep the single strong word.\n3. Reject options that keep the echo or alter the tense while 'fixing' it.\n\n*Why it works:* the echo feels natural in speech, so the eye skips it; the shorter option only looks too plain.",
   "\"Please (revert back) to my mail by Friday.\" revert to / No substitution required / revert back to / reversing to",
   "**Revert** already means 'come back' (in exam usage, reply) → *revert to my mail*. 'Back' is the echo; cut it and keep *to*."),
 P("sip4", "Swapped-twin repair", "common",
   "The bold word is the wrong member of a twin pair: advice/advise, effect/affect, lose/loose, principal/principle.",
   "1. Decide the slot's job: noun or verb?\n2. Map the job to the twin: advice (n) / advise (v); affect (v) / effect (n).\n3. Reject options that change the form further (advising, effecting) — the twin alone repairs the sentence.\n\n*Why it works:* both twins are real words, so nothing looks misspelt; only the part-of-speech test convicts the wrong one.",
   "\"The doctor's (advise) was to rest for a week.\" advice / No substitution required / advises / advising",
   "The slot is a noun (the subject of 'was') → the doctor's **advice**. *Advise* is the verb; *advising* changes the structure."),
]}

S["si-structure-inversion"] = {
"notes": r"""### Inversion: when the helper jumps first
Certain opening words force the helper BEFORE the subject:
- **No sooner … than**: *No sooner **had the train left** than the TTE began checking.*
- **Hardly / Scarcely … when**: *Hardly **had the results been announced** when the servers crashed.*
- **Negative adverbs** (never, seldom, rarely, little, nowhere): *Never **have I witnessed** such a peaceful poll.*
The frame is fixed: opener + helper + subject + main verb + partner word (than for no sooner, when for hardly/scarcely). Options break one part at a time — statement order, wrong partner, wrong helper — so test the three parts separately.
Both *no sooner* frames are legal: *No sooner **did he arrive** than…* and *No sooner **had he arrived** than…* — but each half must match its own frame.

### Dangling modifiers: the opener must describe the subject
An -ing or being opener borrows the main clause's subject:
- Wrong: ***Being a rainy day**, the mela was cancelled.* (The mela was not a rainy day.)
- Right: ***It being a rainy day**, the mela was cancelled.* (Or: *Because it was a rainy day…*)
- Wrong: *Having eaten our lunch, **the train** departed.* (The train ate nothing.)
- Right: *Having eaten our lunch, **we boarded** the train.*
Test: who performs the opener's action? That doer must be the subject.

### Parallelism: one shape down the list
Items joined by and/or/but keep one form: *typing, filing papers, and drafting mails* — not *typing, to file papers, and how to draft mails*. Correlatives too: *not only intelligent but also hardworking* — the words after *not only* and *but also* must be the same kind.

### Word order after reporting verbs
*Asked why **he was** late* — statement order, no *that*, backshifted tense. The improvement options usually offer the question order as a decoy.

### Two more structure repairs
- **Misplaced *only***: *only* sits before the word it limits. *Only he accompanied me* (nobody else came) vs *He accompanied only me* (nobody else was accompanied). Improvement options move *only* around; pick the spot that matches the intended sense.
- **Split infinitives and heavy splits**: keep the marker with its verb when the exam offers it — *to examine carefully* is safe; the exam rarely wants a rewrite here, so prefer **No substitution required** unless the order is truly wrong.

### Method for structure items
1. Find the opener or the connector that controls the architecture.
2. Recall its fixed frame (inversion order, doer of the -ing, list shape).
3. Pick the option that satisfies the frame — usually the one that reorders, not the one that rewords.

### Quick revision
- No sooner…THAN; hardly/scarcely…WHEN; opener forces helper-first order.
- Never/seldom/rarely at the front → inversion (Never have I seen).
- An -ing/being opener describes the main subject; if it cannot, rewrite with It being… or name the doer.
- Lists and correlatives stay parallel — same shape for every item.
- Reported questions: statement order + backshift, no 'that'.
""",
"patterns": [
 P("siv1", "No-sooner / hardly frame repair", "very common",
   "The sentence opens with No sooner or Hardly/Scarcely and the bold part (or its neighbourhood) shows statement order, a wrong partner (than vs when), or a mismatched helper.",
   "1. Name the frame: no sooner…THAN; hardly/scarcely…WHEN.\n2. Check the order: opener + helper + subject + verb.\n3. Check the helper-verb match (had + participle, did + base).\n4. Both 'no sooner' shapes are legal (had left / did leave) but each must stay inside its own frame.\n\n*Why it works:* the frame has three parts, and each wrong option breaks exactly one.",
   "\"No sooner (the train had left) the platform than the TTE began checking tickets.\" had the train left / No substitution required / the train had left / the train had leave",
   "**No sooner** demands inversion: no sooner **had the train left** than… 'The train had left' keeps statement order; 'had leave' breaks the participle."),
 P("siv2", "Negative-adverb inversion repair", "common",
   "The sentence opens with never, seldom, rarely or little and the bold part keeps normal statement order (I have, we see).",
   "1. Spot the negative adverb at the front.\n2. Invert: helper + subject + main verb (Never **have I** witnessed).\n3. Keep the tense; only the order changes.\n\n*Why it works:* fronted negatives pull the helper forward in standard English; the decoys reorder nothing and merely change tense.",
   "\"Never (I have) witnessed such a peaceful poll in this constituency.\" have I witnessed / I had witnessed / No substitution required / I have witness",
   "Fronted **Never** → inversion: never **have I witnessed**. Only the order changes; the tense stays present perfect."),
 P("siv3", "Dangling-modifier repair", "common",
   "The sentence begins with an -ing or being phrase, and the main-clause subject cannot be the doer of that phrase (Being a rainy day, the mela…).",
   "1. Ask who performs the opener's action or state.\n2. If the main subject cannot be the doer, the sentence dangles.\n3. Pick the option that names the doer as subject, or converts the opener to 'It being…' / a full clause.\n\n*Why it works:* English attaches the opener to the nearest noun; the repair either changes the subject or gives the opener a subject of its own.",
   "\"(Being a rainy day), the mela was cancelled by the committee.\" It being a rainy day / No substitution required / Being rainy day / Been a rainy day",
   "The mela cannot *be* a rainy day → **It being a rainy day**, the mela was cancelled. The absolute construction gives the opener its own subject."),
 P("siv4", "Parallelism repair in lists and correlatives", "common",
   "A list joined by and/or, or a not only…but also pair, mixes shapes: two -ing items and one to-item, or an adjective on one side and a clause on the other.",
   "1. Write the items in a column.\n2. Match each item's shape to the first.\n3. Pick the option that makes every item copy the same form — usually the uniform -ing list or the paired adjectives.\n\n*Why it works:* readers parse a list as one unit; the correct option restores one shape so the unit parses cleanly.",
   "\"The training module covers (typing, to file papers, and how to draft mails).\" typing, filing papers, and drafting mails / No substitution required / typing, filing papers, and to draft mails / typing, to file papers and draft mails",
   "Every item must be an -ing form: **typing, filing papers, and drafting mails**. The mixed shapes break the parallel line."),
]}
