# Error-spotting notes + patterns, part B: article-preposition, pronoun-conjunction,
# comparison-wordchoice, and the NEW subtopic es-verbs-structure.
from _lib import P

S = {}

S["es-article-preposition"] = {
"notes": r"""### Articles: three questions
1. **A or an?** Decide by the FIRST SOUND, not the letter. Vowel sound → an: *an hour, an honest man, an MLA, an X-ray*. Consonant sound → a: *a university, a European, a one-rupee coin* (u, Eu, one all begin with a consonant sound y/w).
2. **The or nothing?** Use **the** when the noun is already known, specified by a phrase, one of its kind (*the sun, the Ganga*), or a superlative (*the best, the holiest*).
3. **Zero article**: plural or uncountable nouns used in a general sense take no article — *Women are running **hostels** now*; *Honesty **is** the best policy* (abstract idea); meals, languages, games: *have **dinner**, speak **Tamil**, play **cricket***.
Trap: *a best / a most* is always wrong — a superlative needs **the**.

### Prepositions: fixed pairs win
Most exam questions are not about direction or place — they test **fixed pairs**: a verb/adjective/noun that always travels with one preposition.
- Verb pairs: *abide **by**, abide **in**, accompany (no preposition), accuse **of**, apologise **to** (person) **for** (act), approve **of**, apply **to** (organisation) **for** (post), consist **of**, depend **on**, insist **on**, interfere **with/in**, prefer X **to** Y, comply **with**, deal **with**, jump **to** conclusions.
- Adjective pairs: *afraid **of**, angry **with** (person) **at** (thing), capable **of**, fond **of**, good **at**, married **to**, senior/junior **to**, different **from**, devoid **of**.
- Noun pairs: *cause **of**, reason **for**, solution **to**, comparison **with/between**.

### Time and place in one breath
- **in** long periods (in June, in 2026, in the morning); **on** days and dates (on Monday, on 15 August); **at** clock points (at 9 a.m., at night, at dawn).
- **since** + starting point with perfect tenses (since morning); **for** + length (for two hours); **during** + a period inside which something happens (during the rains); **within** + a limit (within a week).
- **between** two things; **among** more than two: *The land was divided **between** the two brothers; the sweets were shared **among** the children.*

### Method
1. If the blank follows a verb/adjective/noun, first recall its fixed partner — meaning rarely matters.
2. If the blank is about time or place, sort the options by the size of the time/place (at < on < in).
3. Watch pairs with two colours: *angry with/at*, *apply to/for*, *agree with (person)/to (proposal)*.

### Quick revision
- an hour, an MLA — a university, a European: sound, not spelling.
- Superlative → the; first mention → a/an; general plurals and meals → no article.
- insist on, accuse of, capable of, prefer to, comply with, jump to conclusions.
- in June / on Monday / at nine; since a point / for a length / during a period.
- angry with a person, at a thing; apply to an office, for a post.
""",
"patterns": [
 P("esa1", "A vs an — by sound", "very common",
   "The options or the suspect part differ only in a/an before a noun, or the error sentence places an/an/a before a word.",
   "1. Say the next word aloud; hear its first sound.\n2. Vowel sound → an (an hour, an MLA); consonant sound → a (a university, a one-day match).\n3. Ignore spelling — the letter is a decoy.\n\n*Why it works:* the rule follows speech, and words like university (y-sound) or hour (silent h) break the letter rule.",
   "\"She reached the hall an hour late because of (1) ______ MLA's convoy.\" a / an / the / no article",
   "MLA is said 'em-el-ay' — vowel sound first → **an MLA's convoy**. 'A MLA's' is the error."),
 P("esa2", "The with superlatives and unique nouns", "common",
   "A superlative (best, holiest) or a one-of-a-kind noun (sun, Ganga) appears with a or no article instead of the.",
   "1. Spot the superlative form or the unique noun.\n2. Superlative → the, always.\n3. One-of-a-kind or already-specified noun → the.\n\n*Why it works:* 'the' singles out one item from its group; a superlative and a unique noun both do exactly that.",
   "\"The Ganga is considered (1) ______ holiest of the rivers in India.\" a / an / the / no article",
   "Holiest is a superlative → **the holiest**. 'A holiest' is wrong — indefinites cannot sit on superlatives."),
 P("esa3", "Adjective + fixed preposition", "common",
   "An adjective (capable, afraid, angry, fond) is followed by a preposition blank or a suspect preposition.",
   "1. Find the adjective just before the blank.\n2. Recall its fixed partner: capable OF, angry WITH (person), fond OF, good AT.\n3. The preposition that follows one adjective is not negotiable by sense.\n\n*Why it works:* adjective-preposition pairs are frozen by usage; logic ('capable in' sounds plausible) does not unfreeze them.",
   "\"The new recruit is quite capable (1) ______ handling this difficult client.\" of / to / in / for",
   "Fixed pair **capable of** + -ing → of. 'Capable to handle' would be wrong even with the infinitive."),
 P("esa4", "Verb + fixed preposition / idiom", "very common",
   "A verb or verb phrase (insist, comply, accuse, jump) is followed by its preposition, and one option breaks the idiom.",
   "1. Identify the verb phrase ending at the blank.\n2. Recall the frozen pair: insist ON, comply WITH, accuse OF, jump TO conclusions.\n3. Where two partners exist (apply TO an office / FOR a post), let the noun after the blank choose.\n\n*Why it works:* these pairs are memorised chunks; the wrong option is always a look-alike from another pair.",
   "\"The coach did not agree with the umpire, but he complied (1) ______ the rules.\" by / with / to / for",
   "Fixed pair **comply with** → with. 'Comply by' mixes it up with 'abide by'."),
]}

S["es-pronoun-conjunction"] = {
"notes": r"""### Pronoun case: who is doing what
- **Subject pronouns** (I, we, he, she, they) do the action; **object pronouns** (me, us, him, her, them) receive it.
- After a preposition, always the object form: *between you and **me*** (never 'between you and I'); *for **him** and **me***.
- After *let*, the object form: *Let **him** and **me** finish.*
- Compare to save someone: *She is taller than **I** (am)*, but a verbless comparison in speech takes 'me' — exams accept *than I* with the verb understood.
- **Possessives**: its (belonging to it) vs it's (= it is); whose vs who's (= who is); their vs there vs they're. *It's tail* is always wrong; *its tail* is right.

### Relative pronouns
- **who** = subject of the clause: *The lawyer **who** took our case.*
- **whom** = object: *The lawyer **whom** we met.* (We met HIM → whom.)
- **whose** = possession, for people AND things: *the building **whose** roof leaked* (never 'which roof').
- **which** = things; **that** = people or things in defining clauses.
Quick test: replace the relative with *he/she/it* (→ who) or *him/her/it* (→ whom).

### Correlative conjunctions travel in pairs
- *not only … **but also*** — never 'but…also' missing the match of the first half.
- *no sooner … **than*** — never 'no sooner…when'.
- *hardly / scarcely … **when*** — never '…than'.
- *either … **or***; *neither … **nor***; *not only before verbs but also before nouns* must sit in matching positions.
The correlative often drags word order with it: *No sooner had the train left **than**…* (had + subject + participle).

### Connectives in reported speech
- Reported **yes/no** question → *if / whether*, and never 'that whether': *She asked **whether** I had locked the door.*
- Reported **wh-** question keeps the wh-word and drops *that*: *The judge asked **why** he had changed his statement* (never 'asked that why').
- Reported order/request → *to* + verb: *The coach told them **to** warm up.*

### Order and agreement of pronouns
For politeness, the second person comes first and the speaker last: *you and **I**, you and **he**, he and **I*** — never 'I and you'. When the same pronoun could be subject or object, test with the verb: *My brother and **I** went* (we went), but *They invited my brother and **me*** (they invited us).

### Each other vs one another
Traditional rule: **each other** for two, **one another** for more than two: *The two sisters helped each other; the six labourers helped one another.* Exams still reward this split.

### Quick revision
- Preposition or 'let' → object pronoun: between you and me.
- its ≠ it's; whose ≠ who's.
- whom when him/her would fit; whose for possession (even of things).
- no sooner…than; hardly…when; not only…but also.
- asked whether / asked why — never 'that whether' or 'that why'.
- two → each other; many → one another.
""",
"patterns": [
 P("esp1", "Pronoun case after a preposition or 'let'", "very common",
   "A preposition (between, for, to, with) or the word 'let' is followed by a pronoun in the subject form (I, he, she, they).",
   "1. Find the preposition or 'let' before the pronoun.\n2. Objects take object forms: me, him, her, us, them.\n3. Never 'between you and I' — the preposition demands 'me'.\n\n*Why it works:* 'you and I' sounds formal and polite, so it is the classic planted error.",
   "\"The award was shared between Ravi and (1) ______, though the judges had earlier picked only Ravi.\" he / him / his / himself",
   "After the preposition **between** → object form: **him**. 'Between Ravi and he' is the planted error."),
 P("esp2", "Relative pronoun choice (who / whom / whose / which)", "common",
   "A clause introduced by who/whom/whose/which contains the error, usually with the wrong case or 'which roof' for possession.",
   "1. Locate the relative clause and its verb.\n2. If the relative does the clause's action → who; if it receives it (him/her fits) → whom.\n3. Possession → whose, even for buildings and things.\n\n*Why it works:* the him-substitution test settles who/whom in seconds, and 'which' for possession has no defence.",
   "\"The building (1) ______ roof was damaged in the storm is being repaired.\" which / whose / who's / that",
   "Possession (the roof OF the building) → **whose** roof. 'Which roof' reads as 'choose a roof' — wrong."),
 P("esp3", "Correlative pair mismatch (no sooner…than, not only…but also)", "common",
   "The sentence opens with no sooner, hardly, scarcely, or not only, and the second half carries the wrong partner word (when instead of than) or a broken verb order.",
   "1. Circle the first half of the pair.\n2. Recall its fixed partner: no sooner…THAN; hardly/scarcely…WHEN; not only…BUT ALSO.\n3. Check the word order too: 'No sooner had + subject + participle'.\n\n*Why it works:* the pairs are frozen; swapping the partner word is the most planted error in the section.",
   "\"No sooner had the train left (1) ______ the passengers began complaining.\" when / than / then / that",
   "Fixed pair **no sooner…than** → than. 'When' belongs with hardly/scarcely."),
 P("esp4", "Possessive and form errors (its / it's, their forms)", "common",
   "The suspect part contains its/it's, their/there, whose/who's or another possessive-lookalike pair.",
   "1. Expand the apostrophe version: it's = it is; who's = who is.\n2. If the expansion makes no sense, the plain possessive (its, whose, their) is needed.\n3. A possessive before a noun never takes an apostrophe.\n\n*Why it works:* the apostrophe versions are contractions, and the sentence rarely wants a contraction before a noun.",
   "\"The committee published (1) ______ annual report before the audit could even begin.\" it's / its / their's / it is",
   "**Its** annual report (possessive, no apostrophe). 'It's' = it is → 'it is annual report' is nonsense."),
 P("esp5", "Connective in reported questions", "occasional",
   "The sentence reports a question (asked, wanted to know, enquired) and the connective is that + wh-word, or 'that whether'.",
   "1. Spot the reporting verb (asked, wanted to know).\n2. Yes/no question → whether or if (never 'that whether').\n3. Wh-question → the wh-word alone; 'that' must not stand before it.\n\n*Why it works:* the exam joins two legal connectives ('that' + 'why') into one illegal chunk.",
   "\"Mother wanted to know (1) ______ I had locked the back door.\" that whether / whether / that if / that why",
   "A yes/no question in reported speech → **whether** (or if). 'That whether' stacks two connectives — the planted error."),
]}

S["es-comparison-wordchoice"] = {
"notes": r"""### Degrees of comparison: the shape rules
- Positive → Comparative (-er / more) → Superlative (-est / most). Never mix shapes: *bigger*, never *more bigger*; *most beautiful*, never *beautifullest*.
- **Two things** → comparative; **more than two** → superlative: *the shorter of the two routes*; *the shortest of the five routes*.
- Superlatives take **the**: *the best* — 'a best' is wrong.
- Absolute (Latin) comparatives take **to**, not *than*: *superior **to**, inferior **to**, senior **to**, junior **to**, prior **to**, preferable **to**.
- **prefer X to Y** (never 'prefer than'): *I prefer tea to coffee.*

### Comparison logic: compare like with like
- Comparing a member with its own group needs **other / any other**: Correct: *Nagpur is hotter than **any other** city in Maharashtra.* Incorrect: *…than any city in Maharashtra* (Nagpur is one of them — it would be hotter than itself).
- Comparing possessions, repeat the noun or use *that of / those of*: Correct: *The climate of Ooty is cooler than **that of** Bengaluru.* Incorrect: *…cooler than Bengaluru* (climate vs city).
- Double comparatives for cause-effect are legal: *The sooner, the better* — but *more better* never is.

### Redundancy: one idea, one word
Cut the doubling: *return back → return; repeat again → repeat; revert back → revert; both of you two → both of you; final conclusion → conclusion; each and every (choose one in formal writing); discuss about → discuss; enter into a room → enter a room; couple together → couple; adequate enough → adequate.*
Also single-word verbs that need no preposition: *discuss (the plan), attack (the fort), resemble (his father), marry (her)*.

### Commonly confused pairs
| Pair | Noun/meaning 1 | Other |
|---|---|---|
| advice / advise | advice = a suggestion (noun) | advise = to suggest (verb) |
| effect / affect | effect = result (noun) | affect = to influence (verb) |
| lose / loose | lose = misplace | loose = not tight |
| principal / principle | principal = head, main | principle = a rule of conduct |
| stationary / stationery | stationary = not moving | stationery = paper, pens |
| quite / quiet | quite = rather | quiet = silent |

### Method
1. Spot a comparison? Check the shape (no double forms), the number (two vs many), the *to* verbs, and the *any other / that of* logic.
2. No comparison? Look for a doubled idea (redundancy) or a swapped confusable — read the sentence for sense: does the word's job (noun or verb) match its form?

### Quick revision
- Never *more bigger / most shortest / a best*.
- superior, senior, junior, prior, preferable → TO, not than.
- A thing compared with its own group → any other / the other.
- Climate vs city comparisons → that of / those of.
- Kill doubles: return back, repeat again, discuss about.
- advice (n) / advise (v); effect (n) / affect (v); lose / loose.
""",
"patterns": [
 P("esk1", "Double or mixed comparative forms", "very common",
   "The suspect part contains more + -er, most + -est, or a superlative used for exactly two items.",
   "1. Circle the adjective and its marker.\n2. One shape only: -er OR more — never both.\n3. Count the items: two → comparative (often 'the …er of the two'); three or more → superlative with the.\n\n*Why it works:* 'more better' sounds emphatic, which is exactly why it is planted.",
   "\"Of the two routes, this one is (1) ______ and the safer.\" the most shortest / the shorter / shortest / more shorter",
   "Two items → comparative: **the shorter**. 'Most shortest' doubles the superlative; 'more shorter' doubles the comparative."),
 P("esk2", "Redundant word pairs", "very common",
   "The sentence repeats an idea already carried by one word: return back, repeat again, both…two, revert back.",
   "1. Ask of each word: does a neighbour already say this?\n2. 'Back' after return/revert, 'again' after repeat, 'two' after both — cut one.\n3. The part carrying the doubled word is the error, even though the rest is spotless.\n\n*Why it works:* Indian English uses these doubles daily, so they feel normal — the exam counts on the habit.",
   "\"Please (1) ______ what you said about the revised reporting time.\" repeat again / repeat / say again twice / repeat once more again",
   "**Repeat** already means say again → 'repeat again' doubles the idea. The clean form is 'repeat what you said'."),
 P("esk3", "Confusable word swap (advice/advise, effect/affect, lose/loose)", "common",
   "A near-twin word sits in the wrong job: the noun form where the verb is needed, or the wrong member of a sound-alike pair.",
   "1. Decide the job: does this slot need a noun or a verb?\n2. advice = noun, advise = verb; effect = noun, affect = verb; lose = misplace, loose = not tight.\n3. Read for sense — the wrong twin usually makes the sentence silly.\n\n*Why it works:* the pairs differ by one letter or one sound, and both halves exist in English, so spell-check cannot save you.",
   "\"Be careful, or you might (1) ______ the documents you collected today.\" loose / lose / loosen / loss",
   "Needed meaning: misplace → **lose**. 'Loose' means not tight; 'loosen' means make less tight; 'loss' is a noun."),
 P("esk4", "Comparison logic (any other / than that of / Latin 'to')", "common",
   "The comparison is grammatically well-formed but logically broken: a member compared with its own group, or two unlike things compared.",
   "1. Name the two things being compared.\n2. Same group? Insert other/any other.\n3. Different categories (climate vs city)? Use that of / those of.\n4. superior/senior/junior/prior/preferable → to, never than.\n\n*Why it works:* the ear accepts 'than any city'; only the logic check convicts it.",
   "\"My chair is (1) ______ the one you bought last month.\" superior than / superior to / more superior than / superior from",
   "Latin comparative → **superior to** (never than). 'More superior' doubles the comparative on top of it."),
]}

S["es-verbs-structure"] = {
"id": "es-verbs-structure",
"title": "Verb forms, question tags, conditionals and structure",
"concept": "Errors that are not agreement, tense, article or preposition, but live in the shape of the sentence: which verb form follows another verb (gerund or infinitive), the tag at the end of a statement, the two halves of a conditional, lists that must keep one shape, adjectives where adverbs are needed, and modal verbs that never take 'to' or 'able to' alongside.",
"formulas": [],
"tricks": [
 "Hear the sentence end: a statement + tag must flip sign — positive statement → negative tag, negative word (never, rarely, hardly) → positive tag.",
 "After 'if' about the unreal past, English wants had + participle — 'would have' in the if-clause is the planted error.",
 "A list is parallel: whatever shape the first item takes (-ing, to + verb, bare noun), the rest must copy it.",
],
"mistakes": [
 "Using 'could able to' or 'can able to' — can/could already carry ability; only the base verb follows.",
 "Writing 'He denied to take the file' — deny, enjoy, avoid, suggest take the -ing form, not the infinitive.",
 "Tagging a positive statement with a positive tag ('They have come, isn't it?') — the sign must flip and the pronoun must match the subject.",
],
"notes": r"""### Verb + verb: gerund or infinitive
Some verbs are followed by the **-ing form** (gerund), some by **to + verb** (infinitive), and a few by either with a meaning change.
- Always + -ing: **enjoy, avoid, deny, suggest, mind, finish, keep, practise, look forward to, be used to, insist on, interested in, capable of.** Correct: *He denied **taking** the file.* Incorrect: *He denied **to take** the file.*
- Always + to + verb: **want, hope, decide, agree, refuse, promise, manage, afford, learn.** Correct: *They decided **to leave** early.*
- **look forward to + -ing** is the most planted trap: Correct: *I look forward to **meeting** you.* Incorrect: *…to **meet** you.* (Here 'to' is a preposition, not part of the infinitive.)
- Preposition + -ing always: *interested in **painting**, good at **singing**, afraid of **falling**.*

### Question tags: flip the sign, match the pronoun
A tag repeats the helping verb of the statement, flips it negative/positive, and ends with a pronoun that matches the subject.
- Positive → negative tag: *They have submitted their projects, **haven't they**?* (never 'isn't it?')
- Negative → positive tag: *He doesn't smoke, **does he**?*
- **Hidden negatives** — never, rarely, seldom, hardly, scarcely, little — make the statement negative: *Suresh rarely misses his walk, **does he**?*
- *I am* → *aren't I?*; *Let's* → *shall we?*; an imperative → *will you?*

### Conditionals: two halves, one pattern
| Type | If-clause | Main clause | Example |
|---|---|---|---|
| Real future | simple present | will + verb | If she **works** hard, she **will qualify**. |
| Unreal present | simple past | would + verb | If I **were** rich, I **would travel**. |
| Unreal past | had + participle | would have + participle | If I **had known**, I **would have left** earlier. |
Planted errors: *will* inside the if-clause; *would have* inside the if-clause of the unreal past.

### Parallelism: keep the list in one shape
Items joined by *and / but / or / not only…but also* must share their form.
- Correct: *The policy aims at **reducing** paperwork, **improving** transparency, and **speeding** up file movement.*
- Incorrect: *…and **to speed** up file movement.* (One -ing among to-forms breaks the line.)
- Correct: *She enjoys **cooking** and **gardening**.* Incorrect: *She enjoys **cooking** and **to garden**.*

### Adjective or adverb?
- Adjectives describe **nouns**; adverbs describe **actions**.
- After an action verb → adverb: *The engine runs **smoothly**.* Incorrect: *runs smooth.*
- After sense/linking verbs (be, seem, taste, smell, feel, look when describing the subject) → adjective: *The mangoes taste **delicious**.* Incorrect: *taste deliciously* (the mangoes are delicious, they do not taste in a delicious manner).

### Modals: bare and unbending
After **can, could, may, might, must, shall, should, will, would** the base verb follows — no *to*, no *able to*:
- Correct: *You must **submit** the form by Friday.* Incorrect: *must **to submit***.
- Correct: *She could **not explain** the gap.* Incorrect: *could not **able to explain*** — 'could' already says ability; 'able to' says it again and breaks the grammar. Ability: *can swim*; necessity: *must go*; possibility: *may come*.

### Quick revision
- enjoy / avoid / deny / look forward to + -ing; want / decide / agree + to + verb.
- Preposition (in, of, at, to as preposition) + -ing.
- Tag = helping verb flipped + matching pronoun; rarely/never/hardly → positive tag.
- If-clause: future → present; unreal past → had + participle (never would have).
- Lists stay parallel: one shape for every item.
- Runs smoothly (action), tastes delicious (linking); must submit, could explain — never 'to' or 'able to' after a modal.
""",
"patterns": [
 P("esf1", "Gerund vs infinitive after a verb or preposition", "very common",
   "The suspect verb follows another verb or a preposition, and the options offer -ing vs to + verb forms.",
   "1. Identify the verb or preposition before the blank.\n2. -ing group: enjoy, avoid, deny, suggest, look forward to, interested in, capable of.\n3. to-group: want, decide, agree, refuse, manage.\n4. After a preposition (including the 'to' of look forward to), always -ing.\n\n*Why it works:* the two groups are fixed by habit; 'look forward to see' is the single most common Indian-English slip.",
   "\"The children are looking forward to (1) ______ the circus next week.\" see / seeing / be seeing / saw",
   "In **look forward to**, 'to' is a preposition → -ing follows: **seeing**. 'Look forward to see' is the planted error."),
 P("esf2", "Question tag sign and pronoun", "very common",
   "The sentence ends with a short tag after a comma, and the options are different tags (isn't it?, haven't they?, does he?).",
   "1. Find the helping verb of the statement.\n2. Flip its sign; the statement's subject becomes a pronoun in the tag.\n3. Hidden negatives (never, rarely, hardly) → positive tag.\n\n*Why it works:* 'isn't it?' is used for every statement in spoken Indian English, so it is the default wrong option.",
   "\"Suresh rarely misses his morning walk, (1) ______?\" doesn't he / does he / isn't it / hasn't he",
   "**Rarely** makes the statement negative → positive tag with the right helper: **does he**. 'Doesn't he' fails to flip; 'isn't it' matches no subject."),
 P("esf3", "Conditional half broken", "common",
   "An if-sentence shows the wrong pair: will inside the if-clause, or would have inside the if-clause of an unreal past.",
   "1. Read both halves of the conditional.\n2. Real future: if + present, will + verb in the main clause.\n3. Unreal past: if + had + participle, would have + participle — never 'would have' inside the if-clause.\n\n*Why it works:* 'If I would have known' is common in speech; standard English keeps would out of the if-clause.",
   "\"(1) ______ about the traffic, I would have left much earlier.\" If I would have known / If I had known / If I knew / If I have known",
   "Unreal past → if + **had known**; the main clause keeps 'would have left'. 'Would have known' belongs only in the main clause."),
 P("esf4", "Broken parallelism in a list", "common",
   "Three items are joined by and/but, and one item changes shape (two -ing forms and one to-form, or a noun among gerunds).",
   "1. List the joined items in a column.\n2. Check every item's shape against the first.\n3. Rewrite the odd item to copy the first — the odd item is the error.\n\n*Why it works:* the eye reads lists as a single unit, so a shape change hides until you check item by item.",
   "\"My grandmother enjoys cooking, (1) ______, and long walks in the park.\" to garden / gardening / garden / for gardening",
   "The list runs on gerunds after enjoys: cooking, **gardening**, (taking) walks. 'To garden' breaks the shape."),
 P("esf5", "Adjective where an adverb belongs (or the reverse)", "occasional",
   "A word describing an action is in adjective form (runs smooth), or a word after a linking verb is in adverb form (tastes deliciously).",
   "1. Ask what the word describes: an action (how it runs?) or the subject's state (how it tastes?).\n2. Action → adverb (-ly); subject state after a linking verb → adjective.\n3. The classic pair: runs smoothly / tastes delicious.\n\n*Why it works:* both errors sound natural in casual speech; the verb's type decides which is standard.",
   "\"The new engine runs very (1) ______ and hardly makes any noise.\" smooth / smoothly / smoothness / smoother",
   "'Runs' is an action verb → describe it with an adverb: **smoothly**. 'Runs smooth' leaves the action undescribed."),
 P("esf6", "Modal + to/able-to error", "common",
   "A modal (can, could, must, should) is followed by 'to + verb' or by 'able to', doubling or breaking the structure.",
   "1. Spot the modal and the verb after it.\n2. Modals take the bare base verb: must submit, could explain, can swim.\n3. 'Could able to' doubles ability — delete 'able to'; 'must to' doubles the marker — delete 'to'.\n\n*Why it works:* 'can able to' is a direct translation habit, and it appears in papers exactly as often.",
   "\"The candidate could not (1) ______ the gap in his employment.\" able to explain / explain / explaining / to explain",
   "After **could**, the bare base verb: could not **explain**. 'Able to explain' duplicates the ability already inside 'could'."),
]}
