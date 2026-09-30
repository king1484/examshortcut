"""Readable rewrite of English > Error Spotting (all 7 subtopics).

Plain English, short sentences, tables for rules, one method per error type.
Every fact from the old notes/concept is kept; new pattern ids continue each subtopic's prefix.
Run: python error_spotting.py  (patches content/core/topics/english/error-spotting.json in place)
"""
import json
import re
from pathlib import Path

ROOT = Path(__file__).resolve().parents[3]
TOPIC = ROOT / "core" / "topics" / "english" / "error-spotting.json"


def pat(pid, name, freq, spot, steps, why, q, ex_steps, answer, formula=None):
    return {"id": pid, "name": name, "frequency": freq, "howToSpot": spot, "formula": formula,
            "steps": steps, "why": why, "example": {"q": q, "steps": ex_steps, "answer": answer}}


def mis(wrong, right):
    return {"wrong": wrong, "right": right}


SUBS = {}

# =====================================================================
# 1. Checklist
# =====================================================================
SUBS["es-checklist"] = dict(
    concept=(
        "An error-spotting question shows one sentence cut into four parts. One part has a grammar fault, and you pick that part. "
        "Do not hunt at random. Check the sentence in a fixed order, because most errors sit in the first four checks."
    ),
    notes=r"""### What the question asks
A sentence is cut into three or four parts and printed with slashes. One part has an error. You only find the faulty part. You do not rewrite it.

SSC, Railway and Banking papers ask 3 to 5 of these in the English section.

> **Example:** *The quality of the mangoes / were not / up to the mark / this season.* The verb *were* is wrong. The subject is *quality*, so the verb is **was**. Pick part 2.

### The eight checks in order
Check the sentence in this order. Stop at the first check that catches a part.

| Check | Ask yourself | Example |
|---|---|---|
| 1. Subject and verb | What is the true subject? Does the verb match it? | *The quality of the mangoes **were*** |
| 2. Tense | Is there a time word? Does the verb obey it? | *has left two days **ago*** |
| 3. Verb form | Should it be -ing or to + verb? | *He enjoys **to sing*** |
| 4. Article | What is the first sound of the next word? | ***an** university* |
| 5. Preposition | Which word does it depend on? | *insisted **for*** |
| 6. Pronoun and pair words | Right case? Right partner word? | *between you and **I*** |
| 7. Comparison | Any double form? | ***more** bigger* |
| 8. Word choice | Any repeated idea or wrong twin word? | *return **back*** |

About two-thirds of all errors live in checks 1 to 4. So this order saves time.

### The method in three passes
1. **Read for sense.** Read the whole sentence once at normal speed. Your ear catches about half the errors.
2. **Find the verb and its subject.** Cover any phrase between them with your finger.
3. **Walk the checklist.** Stop at the first rule that catches a part. Check that part once, then mark it.

> **Tip:** Say the corrected sentence in your head. It must sound like ordinary formal English. If your fix changes two parts, you misread the sentence. Start again.

### When two parts look wrong
Ask two questions. Which part breaks a **rule**? Which part only *looks odd*? Choose the part you can convict by a named rule.

*No sooner had / the referee blew / the whistle than / the crowd cheered.* Part 1 (*had*) feels odd, but *no sooner had* is correct. Part 2 breaks a rule: after *had*, use the participle **blown**.

> **Rule:** Trust the rule, not the feeling. A part with no rule against it is innocent.

### The No error option
Papers keep 2 or 3 "No error" items in a set. If every part passes the eight checks, choose "No error". Do not invent a fault.

> **Watch:** Never choose "No error" just because nothing jumped out. Run the checks first.

### Where errors hide
- Next to a phrase that interrupts, such as *of the mangoes* or *along with his friends*. The verb hides its fault there.
- In the last part. It often holds a *since / for*, a *a / an* or a tag. Eyes slow down by then.
- Not in a tail phrase like *of the pending bill*. It is usually innocent.
- Not in a part that only ends with a full stop.

### Time plan
Spend about 30 seconds on each question. If two passes find nothing, mark your best guess and move on. Come back only if time is left.
""",
    tricks=[
        {"title": "The sweep in one line",
         "body": "Verb first: find the subject and check its number. Then tense words. Then a / an / the by sound. Then the preposition partner. Only then pronouns, pairs and word choice.",
         "example": {"q": "One of my friends / are going / to London / next week.",
                     "steps": ["Check 1: the true subject is 'one', which is singular.", "So the verb must be 'is going'.", "The later checks never run."],
                     "answer": "Part 2 (are going)"}},
        {"title": "Strip the middle",
         "body": "Delete the phrase between the subject and the verb, such as 'of my friends' or 'as well as the players'. Read the bare skeleton. Agreement errors become loud."},
        {"title": "Earn the No error answer",
         "body": "Choose 'No error' only after the full sweep. About one in five of these items hides a quiet agreement or preposition fault."},
    ],
    mistakes=[
        mis("Matching the verb with the noun nearest to it.", "Find the true subject. Cover the phrase in between."),
        mis("Marking the part that only sounds clumsy.", "Awkward is not always wrong. Mark only a part that breaks a named rule."),
        mis("Starting the hunt in the middle and skipping the first part.", "Check the first part too. Pronoun and connector errors sit there."),
        mis("Finding two errors and freezing.", "Re-check the second one. It is usually standard usage you misjudged."),
        mis("Choosing 'No error' because the sentence sounds fine at speed.", "Run all eight checks before you choose it."),
    ],
    revision=[
        "Read for sense, find the subject and verb, then walk the eight checks.",
        "Interrupting phrases hide agreement errors. Cover them.",
        "Rule beats feeling: pick the part that breaks a rule.",
        "No error is a real option. Earn it by finishing the checks.",
        "The eight checks: agreement, tense, verb form, article, preposition, pronoun and pairs, comparison, word choice.",
        "The last part often hides since / for, a / an or a tag.",
    ],
    patterns=[
        pat("esc1", "Divided sentence: find the faulty part", "very common",
            "The stem says the sentence is divided into parts and one part has an error. The four options are the four parts.",
            ["Read the whole sentence for sense.", "Find the verb and its true subject. Cover interrupting phrases.",
             "Walk the eight checks in order.", "Pick the part that breaks a rule."],
            "The format shows where the fault is, so a rule-based scan beats a guess.",
            "Find the part with the error. (a) The price of vegetables (b) have risen sharply (c) in the last (d) two months.",
            ["The true subject is 'price', which is singular.", "'Vegetables' sits next to the verb, but it is only part of 'of vegetables'.",
             "The verb should be 'has risen'."],
            "(b) have risen sharply"),
        pat("esc2", "Divided sentence with No error as an option", "very common",
            "The sentence has three parts and the fourth option is 'No error'.",
            ["Run the same eight-check scan.", "If every part passes, choose 'No error'.", "If one part fails, pick it and ignore the 'No error' bait."],
            "Papers mix in a few no-error items to catch guessers on both sides.",
            "Find the part with the error. (a) My cousin has been (b) working in this bank (c) since last April. (d) No error",
            ["'Has been working' is present perfect continuous, and it fits 'since'.", "'Last April' is a point in time, so 'since' is right.",
             "All parts pass."],
            "(d) No error"),
        pat("esc3", "Two suspects: the rule decides", "common",
            "Two parts look doubtful. One only feels odd. The other breaks a definite rule.",
            ["Mark both suspects.", "For each one, name the rule it would break.", "A part with no rule against it is innocent.", "Pick the part you can convict by a named rule."],
            "Setters place one bait that feels wrong and one true error.",
            "Find the part with the error. (a) No sooner had (b) the referee blew (c) the whistle than (d) the crowd cheered.",
            ["Part (a) feels odd, but 'no sooner had' is correct.", "After 'had', the participle is needed.", "The participle of 'blow' is 'blown', so use 'had blown'."],
            "(b) the referee blew"),
        pat("esc4", "Fragments from different sentences", "occasional",
            "Each option is a piece of a different sentence. Only one piece is ungrammatical.",
            ["Treat each option as a mini sentence.", "Find the true subject of each piece before judging its verb.", "Exactly one option fails a rule."],
            "Short pieces hide agreement errors because the subject and verb sit close together.",
            "Which piece is wrong? (a) The news of the floods have reached (b) The furniture in these rooms is (c) Mathematics is my favourite (d) Neither of the two answers is",
            ["'News' is singular, so (a) needs 'has reached'.", "'Furniture' is singular, so 'is' is right.",
             "'Mathematics' and 'neither of' take singular verbs, so (c) and (d) are right."],
            "(a) The news of the floods have reached"),
        pat("esc5", "Small word error in the last part", "common",
            "The last part holds a small word: a / an, a preposition, or since / for. The first parts look fine.",
            ["Read the last part slowly, word by word.", "Say each article aloud and check its first sound.", "Check each preposition against the word it depends on."],
            "Eyes slow down near the end, so setters hide the small errors there.",
            "Find the part with the error. (a) She has been (b) learning music (c) since five years. (d) No error",
            ["'Five years' is a length of time.", "A length takes 'for', not 'since'.", "Correct: 'for five years'."],
            "(c) since five years"),
    ],
)

# =====================================================================
# 2. Subject-verb agreement
# =====================================================================
SUBS["es-sva"] = dict(
    concept=(
        "Agreement errors are the biggest error family in SSC English. "
        "The verb must match the true subject in number. The trap is always the same: extra words sit between the subject and the verb. "
        "Cover those words and match the verb with what is left."
    ),
    notes=r"""### The core idea
A singular subject takes a singular verb (with -s in the present). A plural subject takes a plural verb. The whole game is finding the **true subject**.

> **Example:** *The list of candidates **is** long.* The subject is *list*, not *candidates*. So the verb is singular.

### Cover the middle
The subject is never inside a phrase that starts with *of, with, along with, as well as, together with, besides, like, unlike* or *including*.

- Right: The captain, as well as the players, **was** fined.
- Wrong: The captain, as well as the players, **were** fined.
- Right: The quality of the mangoes **was** poor.

Ask: "What is the sentence talking about?" That word is the subject.

> **Rule:** Words like *along with, together with, in addition to* and *and not* never make a plural subject. The verb follows the first subject.

### Words that are always singular
- **Each, every, everyone, nobody, either, neither** take a singular verb.
- **One of the + plural noun** is singular: *One of my friends **is** a pilot.*
- **Many a + singular noun** is singular: *Many a student **has** failed.*
- **Neither of / either of + plural noun** is singular: *Neither of the answers **is** correct.*
- **Every ... and every ...** stays singular: *Every man and every woman **was** counted.*

### Either or, neither nor
With *either ... or* and *neither ... nor*, the verb agrees with the **nearer** subject.

- Neither the manager nor his **assistants were** present.
- Either Ramesh or his **cousins are** coming.

> **Tip:** Ignore the first subject. Look only at the noun just before the verb.

### A number of and the number of
| Phrase | Meaning | Verb |
|---|---|---|
| A number of students | many students | plural: *were absent* |
| The number of students | the count | singular: *was small* |

The small word *a* or *the* decides everything.

### Relative clauses
The verb after *who, which* or *that* agrees with the noun it points back to.

- *He is one of those officers who **work** late.* The pronoun points to *officers*, so the verb is plural.
- *He is the only officer who **works** late.* The pronoun points to *officer*, so the verb is singular.

### Special nouns
- **Collective nouns** (team, committee, jury, family): singular when they act as one unit. Plural when members disagree. *The committee **has** decided. The jury **were** divided.*
- **Look plural, act singular:** news, mathematics, physics, economics. *The news **is** good.*
- **Pair nouns** (scissors, trousers, spectacles) take a plural verb. *A pair of* takes a singular verb.
- **Amounts and distances** as one unit are singular: *Ten kilometres **is** a long walk.*
- **Titles** are singular: *'Gulliver's Travels' **is** a satire.*
- **Two nouns joined by and** are usually plural. One idea or one person is singular: *Bread and butter **is** his breakfast.*

The passive follows the same rule. *The letters **was** delivered* is wrong. Say *were delivered*.
""",
    tricks=[
        {"title": "Hunt the subject backwards",
         "body": "Start at the verb and walk backwards past every 'of ...' phrase. The first noun or pronoun with no preposition in front is the subject."},
        {"title": "Nearness rule flash",
         "body": "See neither ... nor or either ... or with two subjects? The verb matches the second one. The item usually solves at once.",
         "example": {"q": "Neither the manager nor / the employees was / present at / the meeting.",
                     "steps": ["The nearer subject is 'employees'.", "It is plural, so the verb is 'were'."],
                     "answer": "Part 2 (was)"}},
        {"title": "A quantity is singular",
         "body": "Money, distance, time and weight taken as one amount use a singular verb, even in plural form: 'Ten kilometres is a long walk.'"},
    ],
    mistakes=[
        mis("Using a plural verb after each, every or either ('Each of the boys have').", "Each, every and either are singular. Say 'Each of the boys has'."),
        mis("Treating 'a number of' and 'the number of' as the same.", "A number of = plural verb. The number of = singular verb."),
        mis("Making news, mathematics and physics plural because they end in -s.", "They are singular. The news is good."),
        mis("Writing 'one of my friends who works' when the who-clause needs the plural.", "In 'one of those officers who work', the pronoun points to 'officers'."),
        mis("Agreeing the verb with the noun after 'as well as' or 'along with'.", "The verb follows the first subject."),
    ],
    revision=[
        "Never let the nearest noun decide. Cover the interrupting phrase.",
        "each / every / one of / many a / neither of: singular verb.",
        "neither ... nor and either ... or: the verb agrees with the nearer subject.",
        "a number of: plural. The number of: singular.",
        "news, mathematics, physics: singular. spectacles, scissors: plural.",
        "as well as, along with, together with: the verb follows the first subject.",
    ],
    patterns=[
        pat("esv1", "One of / every one of + plural noun", "very common",
            "The sentence has 'one of the ...' or 'each of the ...' just before the verb. The verb's number is in doubt.",
            ["Find the head word: 'one' or 'each', not the plural noun after 'of'.", "Head word singular: use a singular verb.", "Check the tense separately."],
            "The plural noun sits next to the verb and pulls the eye. The rule outranks the pull.",
            "Find the part with the error. (a) One of the laptops (b) displayed at the expo (c) were sold (d) within an hour.",
            ["The subject is 'one', which is singular.", "'Laptops' is only part of 'of the laptops'.", "Correct: 'was sold'."],
            "(c) were sold"),
        pat("esv2", "Either ... or / neither ... nor", "very common",
            "Two subjects are joined by either ... or or neither ... nor. The verb comes after the second one.",
            ["Ignore the first subject.", "Look at the subject just before the verb.", "Match the verb with that subject's number."],
            "The nearness rule is fixed, and setters make the two subjects differ in number.",
            "Find the part with the error. (a) Neither the collector (b) nor his assistants (c) was available (d) at the camp site.",
            ["The nearer subject is 'assistants', which is plural.", "The verb must be plural.", "Correct: 'were available'."],
            "(c) was available"),
        pat("esv3", "Each / every / many a + singular verb", "common",
            "The subject starts with each, every, many a, or 'every ... and every ...'.",
            ["Each, every and many a are singular.", "'Every boy and every girl' stays singular because every repeats.", "Match the verb, and match a later his / her, not their."],
            "These words point to members one at a time, so the verb stays singular.",
            "Find the part with the error. (a) Every man and every woman (b) in the village (c) were counted (d) in the survey.",
            ["'Every ... and every ...' is singular.", "So the verb must be singular.", "Correct: 'was counted'."],
            "(c) were counted"),
        pat("esv4", "A number of and the number of", "common",
            "The subject phrase is 'a / the number of + plural noun'. Only the small word a or the differs.",
            ["'A number of' means many: plural verb.", "'The number of' means the count: singular verb.", "Read the word before 'number' slowly."],
            "One small word flips the number, and the options exploit a careless read.",
            "Find the part with the error. (a) The number of accidents (b) on this highway (c) have fallen (d) after the new signals.",
            ["'The number of' means the count, which is singular.", "The verb must be singular.", "Correct: 'has fallen'."],
            "(c) have fallen"),
        pat("esv5", "Verb after who / which / that", "common",
            "The sentence has 'one of those ...' or 'the only ...' followed by who or that and a verb.",
            ["Find the noun the pronoun points back to.", "'One of those + plural noun who': plural verb.", "'The only + singular noun who': singular verb."],
            "The relative pronoun takes its number from the noun before it.",
            "Find the part with the error. (a) She is one of those doctors (b) who always treats (c) poor patients (d) for free.",
            ["'Who' points back to 'doctors', which is plural.", "So the verb must be plural.", "Correct: 'who always treat'."],
            "(b) who always treats"),
        pat("esv6", "Special singular subjects", "common",
            "The subject is a title, an amount, a distance, or a word like news or mathematics.",
            ["Spot the special noun: news, mathematics, an amount, a title.", "Treat it as one unit: singular verb.", "Pair nouns like scissors take a plural verb."],
            "These nouns look plural but name one thing, so the verb is singular.",
            "Find the part with the error. (a) Five hundred rupees (b) were the fine (c) for driving without (d) a licence.",
            ["Five hundred rupees is one amount.", "One amount takes a singular verb.", "Correct: 'was the fine'."],
            "(b) were the fine"),
    ],
)

# =====================================================================
# 3. Tense
# =====================================================================
SUBS["es-tense"] = dict(
    concept=(
        "Every sentence has a time word (an *anchor*) such as yesterday, since 2019 or when. The verb must obey it. "
        "Tense errors have a few fixed shapes. Look for will inside a time clause. Look for since and for mixed up. "
        "Look for a missing past perfect, and for a perfect tense next to a finished time."
    ),
    notes=r"""### The anchor decides the tense
An **anchor** is a word that names the time: yesterday, since 2019, by the time, as soon as. The verb must match it. A tense error means the verb and the anchor disagree.

> **Example:** *He has left two days ago.* The anchor *ago* names a finished time. Use the simple past: **He left two days ago.**

### The main anchors
| Anchor | Tense | Example |
|---|---|---|
| yesterday, last week, ago, in 2019 | simple past | He **left** two days ago. |
| since + point, for + length, so far, yet, already, just | perfect forms | She **has been teaching** since 2015. |
| every day, usually | simple present | The shop **opens** at nine. |
| when / if / until / as soon as (future meaning) | simple present | I will call when the meeting **ends**. |
| earlier of two past events | past perfect | The train **had left** before I reached. |
| a general truth | simple present | The earth **moves** round the sun. |

### Rules examiners love
1. **No will in a time or condition clause.** After *when, before, after, until, as soon as, if, unless*, use the simple present for the future. Right: *when the meeting ends*. Wrong: *when the meeting will end*.
2. **Since and for.** *Since* takes a point (since 2015, since morning). *For* takes a length (for ten years). *Since ten years* is wrong.
3. **Past perfect for the earlier event.** With two past actions, the earlier one takes *had + participle*. Clue words: *by the time, before, already*.
4. **No perfect with a finished time.** *Has gone* clashes with *yesterday, last week, in 2019*.
5. **General truths stay in the present.** *The teacher explained that the earth **moves** round the sun.*
6. **Past reporting verb.** *Said, asked* pull the reported clause back: *said that she **was** busy*. A general truth is the exception (rule 5).

> **Watch:** Do not force the past perfect everywhere. After *before* or *after*, the perfect is optional if the order is already clear.

### Since and for with the perfect continuous
*Has / have been + -ing* pairs with *since* or *for*.

- *She has been working here **for** ten years.*
- *It has been raining **since** he left.* (a past clause after since, present perfect in the main clause)

### The two-step method
1. Circle the time word in every part.
2. Check each verb against the table above.

If a verb inside a *when / if / until* clause has *will*, or a perfect tense stands next to *ago*, you have found the error.

> **Tip:** *Used to* and *would* show a past habit. Say *used to*, never *use to*.
""",
    tricks=[
        {"title": "Circle every anchor",
         "body": "Circle yesterday, ago, since, for, by the time, when and next week before you judge any verb. Most tense items solve themselves.",
         "example": {"q": "When I reached / the station, the train / already left / without a whistle.",
                     "steps": ["Two past events: the train left first, then I reached.", "The earlier event needs the past perfect.", "Correct: 'had already left'."],
                     "answer": "Part 3 (already left)"}},
        {"title": "The will check",
         "body": "Scan for will inside a when / if / until clause with future meaning. SSC plants this error again and again."},
        {"title": "Since and for sorting",
         "body": "Since + starting point (since Monday, since 2019, since childhood). For + length (for ten years, for a week). The wrong partner is the answer."},
    ],
    mistakes=[
        mis("Using the present perfect with a finished time ('I have met him yesterday').", "Use the simple past: 'I met him yesterday'."),
        mis("Moving only half the sentence back: 'He said he will come'.", "Move the whole clause back: 'He said he would come'."),
        mis("Using the past perfect whenever two past verbs appear.", "Use it only to show which action came first."),
        mis("Writing 'since' with a length of time because it sounds formal.", "Length takes 'for': for ten years."),
        mis("Putting will inside the when-clause.", "Use the simple present in the when-clause. Keep will in the main clause."),
    ],
    revision=[
        "ago, yesterday, last ...: simple past only. Never has / have.",
        "since + point of time. for + length of time.",
        "when / if / until / as soon as (future): simple present. No will inside.",
        "Earlier of two past events: had + participle.",
        "General truths stay in the simple present, even in reported speech.",
        "has / have been + -ing pairs with since or for.",
    ],
    patterns=[
        pat("est1", "Will inside a when / if / until clause", "very common",
            "The sentence is about the future. A clause starting with when, if or until has will + verb.",
            ["Find the time or condition word.", "If it points to the future, its clause takes the simple present.", "Keep will only in the main clause."],
            "The future helper never enters a time clause in English.",
            "Find the part with the error. (a) The chief guest will not leave (b) the venue until (c) the programme will conclude. (d) No error",
            ["'Until' starts a time clause about the future.", "The clause needs the simple present.", "Correct: 'until the programme concludes'."],
            "(c) the programme will conclude"),
        pat("est2", "Since vs for", "very common",
            "A perfect or perfect continuous verb is followed by a time phrase. The choice is between since and for.",
            ["Ask what the phrase names: a point or a length.", "Point (2015, morning): since.", "Length (ten years, two hours): for."],
            "The two words split all time phrases between them.",
            "Find the part with the error. (a) My uncle has been teaching (b) in this school (c) since fifteen years. (d) No error",
            ["'Fifteen years' is a length.", "A length takes 'for'.", "Correct: 'for fifteen years'."],
            "(c) since fifteen years"),
        pat("est3", "Past perfect for the earlier past event", "common",
            "Two past actions are in one sentence, often with before, after, by the time or already.",
            ["Put the two actions on a timeline.", "The earlier one takes had + participle.", "The later one takes the simple past."],
            "The past perfect marks the earlier of two past events. Without it, the order is lost.",
            "Find the part with the error. (a) When we reached the hall, (b) the play already began, (c) so we watched (d) from the back.",
            ["The play began before we reached.", "So the play is the earlier event.", "Correct: 'had already begun'."],
            "(b) the play already began"),
        pat("est4", "Present perfect with a finished time", "common",
            "A has / have / had + participle stands next to yesterday, ago, last week or in 2019.",
            ["Look for ago, yesterday, last ... or a year next to a perfect form.", "A finished time needs the simple past.", "Correct the verb part."],
            "The present perfect connects to now. A finished time cuts that link.",
            "Find the part with the error. (a) Ravi has left (b) for Hyderabad (c) two days ago (d) to attend an interview.",
            ["'Two days ago' is a finished time.", "The present perfect cannot go with it.", "Correct: 'Ravi left'."],
            "(a) Ravi has left"),
        pat("est5", "General truth pulled into the past", "occasional",
            "A sentence reports what someone said, and the reported clause states a scientific or permanent fact.",
            ["Check the reported clause for a general truth.", "Such truths stay in the simple present.", "A past form there is the error."],
            "Sequence of tenses has a standing exception for facts that are always true.",
            "Find the part with the error. (a) The teacher explained (b) that the earth (c) moved around the sun. (d) No error",
            ["'The earth moves round the sun' is a permanent fact.", "It stays in the simple present.", "Correct: 'moves around the sun'."],
            "(c) moved around the sun"),
        pat("est6", "Past reporting verb, unchanged verb inside", "common",
            "A past reporting verb (said, asked) is followed by a clause that still has will, can or a present form.",
            ["Spot the past reporting verb.", "Check the verb in the reported clause.", "Move it back one step: will to would, can to could, is to was."],
            "A past reporting verb pulls the reported clause into the past.",
            "Find the part with the error. (a) She said that (b) she will meet us (c) at the station (d) the next morning.",
            ["'Said' is past.", "'Will' must move back to 'would'.", "Correct: 'she would meet us'."],
            "(b) she will meet us"),
    ],
)

# =====================================================================
# 4. Article and preposition
# =====================================================================
SUBS["es-article-preposition"] = dict(
    concept=(
        "Articles are a sound decision. Use *a* or *an* by the first sound of the next word, not its first letter. "
        "Use *the* for a known, unique or superlative noun. "
        "Prepositions are fixed partners: find the word the preposition depends on, and recall its usual partner."
    ),
    notes=r"""### A or an
Decide by the **first sound**, not the letter.

| Sound | Article | Examples |
|---|---|---|
| vowel sound | an | an hour, an honest man, an MLA, an X-ray |
| consonant sound | a | a university, a European, a one-rupee coin |

*University, Euro* and *one* begin with a *y* or *w* sound, which is a consonant sound.

> **Tip:** Say the phrase aloud. *An university* fails the ear at once.

### The, or no article
Use **the** when the noun is:
- already known or made clear by a phrase (*the girl in blue*)
- one of its kind (*the sun, the Ganga*)
- a superlative or an ordinal (*the best, the holiest, the first*)

> **Watch:** *A best* and *a most* are always wrong. A superlative needs **the**.

Use **no article** in these cases:
- Plural or uncountable nouns in a general sense: *Women are running hostels now.*
- Abstract ideas: *Honesty is the best policy.*
- Meals, languages, games: *have dinner, speak Tamil, play cricket.*
- School, college or hospital in their purpose sense: *go to school.*

### Prepositions: fixed pairs win
Most questions test **fixed pairs**, not direction or place. Find the word the preposition hangs on and recall its partner.

**Verbs**
- abide by, accuse of, approve of, consist of, depend on
- insist on, interfere with, comply with, deal with, jump to conclusions
- apologise to (person) for (act), apply to (office) for (post)
- prefer X to Y

**Adjectives**
- afraid of, capable of, fond of, devoid of, good at
- angry with (person) at (thing), married to, different from
- senior to, junior to

**Nouns**
- cause of, reason for, solution to, comparison with

Some pairs have two forms. Let the noun after the blank choose: *apply to an office*, *apply for a post*.

*Accompany* takes no preposition.

> **Example:** *He is married with a doctor.* The fixed pair is *married to*. Correct: **He is married to a doctor.**

Some pairs change meaning with the preposition. *Look at* means glance. *Look for* means search. *Look after* means take care of. Learn the pair with its meaning.

### Time and place words
- **in** for long periods: in June, in 2026, in the morning.
- **on** for days and dates: on Monday, on 15 August.
- **at** for clock points: at 9 a.m., at night, at dawn.
- **since** + starting point. **for** + length. **during** + a period inside which something happens. **within** + a limit.
- **between** two things. **among** more than two: *The land was divided **between** the two brothers. The sweets were shared **among** the children.*

### Method
1. If the blank follows a verb, adjective or noun, recall its fixed partner. Meaning rarely helps.
2. If it is time or place, sort by size: at, then on, then in.
3. Read each preposition on its own. It often hides at the end of a long part.
""",
    tricks=[
        {"title": "Say it aloud",
         "body": "Articles are sound decisions. Say the phrase. 'An university' fails the ear because of the 'yu' sound. 'A honest man' fails too.",
         "example": {"q": "The children / were playing / in a garden / near an university.",
                     "steps": ["'University' starts with a 'yu' consonant sound.", "So the article is 'a'."],
                     "answer": "Part 4 (an university, should be a university)"}},
        {"title": "Governor chant",
         "body": "Underline the word the preposition depends on. Recite its partner: insist on, angry with (person), prefer to, married to. A wrong partner is the answer."},
        {"title": "The with superlatives",
         "body": "Superlatives and ordinals need the: 'the most intelligent girl', 'the first attempt'. A bare superlative hides an article error."},
    ],
    mistakes=[
        mis("Choosing 'an' for words that start with a vowel letter but a consonant sound (university, union, one).", "Go by sound: a university, a union, a one-rupee coin."),
        mis("Using 'than' after senior, junior, superior, inferior or prefer.", "These words take 'to'."),
        mis("Writing 'angry on him' or 'consists in students' by literal translation.", "Learn the fixed pair: angry with him, consists of students."),
        mis("Adding 'the' before school, hospital or home in the purpose sense.", "Say 'go to school' when you mean attend."),
        mis("Using 'a best' or 'a most'.", "A superlative takes 'the'."),
    ],
    revision=[
        "an hour, an MLA. a university, a European. Sound, not spelling.",
        "Superlative: the. First mention: a / an. General plurals and meals: no article.",
        "insist on, accuse of, capable of, prefer to, comply with, jump to conclusions.",
        "in June, on Monday, at nine. since a point, for a length, during a period.",
        "angry with a person, at a thing. apply to an office, for a post.",
        "between two, among more than two.",
    ],
    patterns=[
        pat("esa1", "A vs an by sound", "very common",
            "The suspect part has a or an before a word. The word's first letter and its first sound may disagree.",
            ["Say the next word aloud.", "Vowel sound: an (an hour, an MLA).", "Consonant sound: a (a university, a one-day match).", "Ignore the spelling."],
            "The rule follows speech, and words like university or hour break the letter rule.",
            "Find the part with the error. (a) She reached the hall (b) an hour late (c) because of a MLA's convoy. (d) No error",
            ["MLA is said 'em-el-ay'.", "It starts with a vowel sound.", "Correct: 'an MLA's convoy'."],
            "(c) because of a MLA's convoy"),
        pat("esa2", "The with superlatives and unique nouns", "common",
            "A superlative (best, holiest) or a one-of-a-kind noun (sun, Ganga) has a or no article instead of the.",
            ["Spot the superlative or the unique noun.", "A superlative always takes the.", "A one-of-a-kind noun takes the."],
            "'The' picks out one item from its group. A superlative and a unique noun both do that.",
            "Find the part with the error. (a) The Ganga is considered (b) a holiest of (c) the rivers in India. (d) No error",
            ["'Holiest' is a superlative.", "A superlative takes 'the'.", "Correct: 'the holiest'."],
            "(b) a holiest of"),
        pat("esa3", "Adjective + fixed preposition", "common",
            "An adjective (capable, afraid, angry, fond) is followed by a suspect preposition.",
            ["Find the adjective before the preposition.", "Recall its partner: capable of, angry with (person), fond of, good at.", "Do not choose by sense."],
            "Adjective and preposition pairs are frozen by usage.",
            "Find the part with the error. (a) The new recruit (b) is quite capable to (c) handling this (d) difficult client.",
            ["The adjective is 'capable'.", "Its fixed partner is 'of'.", "Correct: 'capable of handling'."],
            "(b) is quite capable to"),
        pat("esa4", "Verb + fixed preposition", "very common",
            "A verb (insist, comply, accuse, jump) is followed by a preposition, and one option breaks the pair.",
            ["Find the verb before the preposition.", "Recall the pair: insist on, comply with, accuse of, jump to conclusions.", "For two-way pairs, let the noun after the blank choose."],
            "These pairs are memorised chunks. The wrong option is a look-alike from another pair.",
            "Find the part with the error. (a) The coach did not agree with the umpire, (b) but he complied (c) by the rules (d) of the match.",
            ["The verb is 'comply'.", "Its partner is 'with'.", "'Comply by' mixes it up with 'abide by'."],
            "(c) by the rules"),
        pat("esa5", "Time, place and between / among", "common",
            "The suspect part has in, on, at, between or among with a time, a place or a group.",
            ["Name the time or place: a long period, a day, a clock point.", "Long period: in. Day or date: on. Clock point: at.", "Two things: between. More than two: among."],
            "Each word covers a fixed size of time or place.",
            "Find the part with the error. (a) The sweets were shared (b) between the (c) forty children (d) of the school.",
            ["'Between' is for two.", "Forty children is more than two.", "Correct: 'among the forty children'."],
            "(b) between the"),
        pat("esa6", "Extra article before a language, meal or game", "occasional",
            "An article stands before a language, a meal, a game or a general plural noun.",
            ["Spot the noun: language, meal, game or general idea.", "General use takes no article.", "Delete the article."],
            "Zero article is the rule for general use, and an added article breaks it.",
            "Find the part with the error. (a) She speaks (b) the Tamil (c) very fluently (d) and plays cricket.",
            ["'Tamil' is a language name in general use.", "It takes no article.", "Correct: 'speaks Tamil'."],
            "(b) the Tamil"),
    ],
)

# =====================================================================
# 5. Pronoun and conjunction
# =====================================================================
SUBS["es-pronoun-conjunction"] = dict(
    concept=(
        "Pronouns change form by their job: subject forms do the action, object forms receive it. "
        "Correlative pairs such as *no sooner ... than* always travel together. "
        "Most errors are the wrong pronoun case, the wrong partner word, or a wrong connective in reported speech."
    ),
    notes=r"""### Pronoun case: who does what
- **Subject pronouns** do the action: I, we, he, she, they.
- **Object pronouns** receive it: me, us, him, her, them.
- After a preposition, use the object form: *between you and **me***, *for **him** and **me***.
- After *let*, use the object form: *Let **him** and **me** finish.*
- With *than*, add the hidden verb in your head: *She is taller than **I** (am).* Exams accept *than I*.

> **Rule:** Between you and I is always wrong. A preposition needs the object form.

### Look-alike words
- **its** means belonging to it. **it's** means it is.
- **whose** means belonging to whom. **who's** means who is.
- **their, there, they're** are three different words.
- Before a noun, a possessive never takes an apostrophe. *It's tail* is wrong. *Its tail* is right.

### Relative pronouns
- **who** is the subject of the clause: *The lawyer **who** took our case.*
- **whom** is the object: *The lawyer **whom** we met.*
- **whose** shows possession, for people and things: *the building **whose** roof leaked*.
- **which** is for things. **that** is for people or things in defining clauses.

> **Tip:** Replace the pronoun with he or him. *He* fits: use who. *Him* fits: use whom.

### Correlative pairs
Pair words travel together. Check that both halves match.

| Pair | Example | Wrong partner |
|---|---|---|
| no sooner ... than | No sooner had the train left **than** the bell rang. | when |
| hardly / scarcely ... when | Hardly had he sat down **when** the phone rang. | than |
| not only ... but also | She not only sings **but also** dances. | but only |
| either ... or; neither ... nor | verb agrees with the nearer subject | first subject |
| both ... and | Both Ram **and** his brother came. | as well as |
| lest ... should | Work hard lest you **should** fail. | will not |
| whether ... or | I asked whether he would come **or** not. | nor |

What follows *not only* must match what follows *but also*: verb with verb, noun with noun.

After *did*, use the base verb: *No sooner did the bell **ring** than ...*. After *had*, use the participle: *No sooner had the bell **rung** than ...*.

### Connectives in reported speech
- Reported **yes/no** question: use *if* or *whether*. Never *that whether*.
- Reported **wh-** question: keep the wh-word and drop *that*. *He asked **why** he had changed his statement.*
- Reported order or request: use *to + verb*. *The coach told them **to** warm up.*

### Order and agreement
- Normal order is second person, third person, first person: *you, he and I*. Never *I and you*.
- To admit a fault, put yourself first: *I, you and he are to blame.*
- *Each, everyone, somebody, nobody* take singular pronouns: *Each of the boys did his work.* Exam keys follow *his / her*.
- **Each other** is for two. **One another** is for more than two.
- A pronoun that repeats the subject is wrong: *My friend he came* is wrong.
""",
    tricks=[
        {"title": "Preposition plus I? Kill it",
         "body": "Between you and I, for he and I: all wrong. After a preposition, use the object form every time.",
         "example": {"q": "Between you and I, / the new manager / has no / practical experience.",
                     "steps": ["'Between' is a preposition.", "A preposition takes the object form.", "Correct: 'between you and me'."],
                     "answer": "Part 1"}},
        {"title": "Did plus base form",
         "body": "After did, does or do, the verb keeps its base form: 'No sooner did the bell ring'. A past form after did is always an error."},
        {"title": "Cover and match the pair",
         "body": "Cover everything except the pair words. If one half stands with the wrong partner (hardly ... than), that part is the error."},
    ],
    mistakes=[
        mis("Using 'whom' as the subject, or 'who' after a preposition ('to who').", "Subject: who. After a preposition or as object: whom."),
        mis("Writing 'between him and she'.", "Both pronouns after 'between' are objects: between him and her."),
        mis("Pairing hardly / scarcely with 'than' and no sooner with 'when'.", "Hardly / scarcely go with when. No sooner goes with than."),
        mis("Marking 'everyone ... their' without knowing the key.", "SSC keys follow his / her. Mark accordingly when the options force a choice."),
        mis("Writing 'that whether' or 'that why' in a reported question.", "Use 'whether' or 'why' alone."),
    ],
    revision=[
        "After a preposition or let: the object pronoun. Between you and me.",
        "its is not it's. whose is not who's.",
        "who does, whom receives, whose owns (even for things).",
        "no sooner ... than. hardly ... when. not only ... but also.",
        "asked whether, asked why. Never 'that whether' or 'that why'.",
        "two: each other. Many: one another.",
    ],
    patterns=[
        pat("esp1", "Pronoun case after a preposition or let", "very common",
            "A preposition (between, for, to, with) or let is followed by a subject-form pronoun (I, he, she, they).",
            ["Find the preposition or let before the pronoun.", "Use the object forms: me, him, her, us, them.", "Never say between you and I."],
            "'You and I' sounds polite, so it is the classic planted error.",
            "Find the part with the error. (a) The award was shared (b) between Ravi and he, (c) though the judges had earlier (d) picked only Ravi.",
            ["'Between' is a preposition.", "It takes the object form.", "Correct: 'between Ravi and him'."],
            "(b) between Ravi and he"),
        pat("esp2", "Who / whom / whose / which", "common",
            "A clause starts with who, whom, whose or which, and the case or the word is wrong.",
            ["Find the relative clause and its verb.", "The pronoun does the action: who. It receives it (him fits): whom.", "Possession: whose, even for buildings and things."],
            "The him test settles who and whom in seconds. 'Which roof' has no defence.",
            "Find the part with the error. (a) The building (b) which roof was damaged (c) in the storm (d) is being repaired.",
            ["The roof belongs to the building.", "Possession needs 'whose'.", "Correct: 'whose roof was damaged'."],
            "(b) which roof was damaged"),
        pat("esp3", "Correlative pair mismatch", "common",
            "The sentence has no sooner, hardly, scarcely or not only. The second half has the wrong partner or a broken verb.",
            ["Circle the first half of the pair.", "Recall its partner: no sooner ... than. hardly / scarcely ... when. not only ... but also.", "Check the word order after it."],
            "The pairs are frozen, so swapping the partner word is the most planted error.",
            "Find the part with the error. (a) No sooner had the train left (b) when the passengers (c) began complaining (d) about the delay.",
            ["'No sooner' pairs with 'than'.", "'When' belongs with hardly or scarcely.", "Correct: 'than the passengers'."],
            "(b) when the passengers"),
        pat("esp4", "Its / it's and other look-alikes", "common",
            "The suspect part has its / it's, whose / who's, or their / there.",
            ["Expand it's to it is and who's to who is.", "If the expansion makes no sense, use the plain possessive.", "A possessive before a noun never takes an apostrophe."],
            "The apostrophe forms are contractions, and a noun after them needs a possessive.",
            "Find the part with the error. (a) The committee published (b) it's annual report (c) before the audit (d) could even begin.",
            ["'It's' means 'it is'.", "'It is annual report' makes no sense.", "Correct: 'its annual report'."],
            "(b) it's annual report"),
        pat("esp5", "Connective in reported questions", "occasional",
            "The sentence reports a question (asked, wanted to know). The connective is 'that + wh-word' or 'that whether'.",
            ["Spot the reporting verb.", "Yes/no question: whether or if.", "Wh-question: the wh-word alone."],
            "The wrong option joins two legal connectives into one illegal chunk.",
            "Find the part with the error. (a) Mother wanted to know (b) that whether I had (c) locked the back door (d) before leaving.",
            ["The reported question is yes/no.", "It takes 'whether' or 'if'.", "Correct: 'whether I had locked'."],
            "(b) that whether I had"),
        pat("esp6", "Myself as a subject; a repeated pronoun", "common",
            "The subject holds a -self pronoun (myself, himself), or a pronoun repeats the subject.",
            ["Check the subject slot.", "A -self pronoun is never the subject. Use I, he or she.", "Delete a pronoun that only repeats the subject."],
            "-self pronouns show the doer and receiver are the same, so they cannot stand alone as a subject.",
            "Find the part with the error. (a) My friend and myself (b) attended the seminar (c) held at the (d) district library.",
            ["'Myself' cannot be a subject.", "Use the subject form 'I'.", "Correct: 'My friend and I'."],
            "(a) My friend and myself"),
    ],
)

# =====================================================================
# 6. Comparison, redundancy, word choice
# =====================================================================
SUBS["es-comparison-wordchoice"] = dict(
    concept=(
        "Comparison errors are double forms (*more bigger*), broken logic (*bigger than any city*) and a wrong *than* after Latin words like *superior*. "
        "Word-choice errors are repeated ideas (*return back*) and look-alike words (*advice, advise*). "
        "Learn the short lists below and the errors show up at once."
    ),
    notes=r"""### Degrees of comparison
- Use one shape only: *bigger*, never *more bigger*. *Most beautiful*, never *beautifullest*.
- **Two things:** comparative. *The shorter of the two routes.*
- **More than two:** superlative. *The shortest of the five routes.*
- A superlative takes **the**. *A best* is wrong.
- Latin comparatives take **to**, not *than*: superior to, inferior to, senior to, junior to, prior to, preferable to.
- **Prefer X to Y.** *I prefer tea to coffee.* Never *prefer than*.
- **Elder** is for family and takes no *than*. Use **older than** everywhere else.

### Compare like with like
- A member compared with its own group needs **other**.
  - Right: *Nagpur is hotter than **any other** city in Maharashtra.*
  - Wrong: *... than any city in Maharashtra.* Nagpur would be hotter than itself.
- Repeat the noun or use **that of / those of** when you compare qualities.
  - Right: *The climate of Ooty is cooler than **that of** Bengaluru.*
  - Wrong: *... cooler than Bengaluru.* That compares a climate with a city.

> **Watch:** *The sooner, the better* is a legal double comparative. *More better* never is.

### Redundancy: one idea, one word
Cut the second word: return back, repeat again, revert back, final conclusion, close proximity, sufficient enough, cooperate together, adequate enough, couple together.

Also cut: *both of you two* (say both of you), *discuss about* (say discuss), *enter into a room* (say enter a room). *Each and every* is not needed: choose one in formal writing.

Some verbs need no preposition: discuss the plan, attack the fort, resemble his father, marry her.

### Few, little, less, elder
| Pair | Rule | Example |
|---|---|---|
| few / a few | few = almost none. a few = some | Few men are wise. A few students stayed. |
| little / a little | little = hardly any. a little = some | There is a little water left. |
| much / many | much + uncountable. many + countable | much help, many friends |
| fewer / less | fewer + countable. less + uncountable | fewer books, less sugar |
| farther / further | farther = distance. further = additional | further details |
| lie / lay | lie: lay, lain. lay (put): laid | He lay down. He laid the pen down. |

### Confusable pairs
| Pair | Meaning |
|---|---|
| advice / advise | advice = suggestion (noun). advise = to suggest (verb) |
| effect / affect | effect = result (noun). affect = to influence (verb) |
| lose / loose | lose = misplace. loose = not tight |
| principal / principle | principal = head, main. principle = a rule of conduct |
| stationary / stationery | stationary = not moving. stationery = paper, pens |
| quite / quiet | quite = rather. quiet = silent |

### Method
1. See a comparison? Check the shape, the number of items, the *to* words, and the *any other / that of* logic.
2. No comparison? Look for a repeated idea or a wrong twin. Ask: does the word's job (noun or verb) match its form?

Word order also lands here. Adverbs of frequency come before the main verb but after *be*: *He always is* is wrong. Say *He is always*.
""",
    tricks=[
        {"title": "Scan for more + er",
         "body": "Look for more before a comparative (more bigger) or most before a superlative. That is an error at once.",
         "example": {"q": "Delhi is / more bigger / than Agra / in area.",
                     "steps": ["'Bigger' is already a comparative.", "'More' doubles it.", "Correct: 'bigger than Agra'."],
                     "answer": "Part 2 (more bigger)"}},
        {"title": "Flinch at echo pairs",
         "body": "In pairs like return back, repeat again and revert back, the second word repeats the first. These are planted answers."},
        {"title": "The that-of test",
         "body": "When two nouns' qualities are compared, the second noun needs that of or those of: 'The roads of Delhi are wider than those of Patna.'"},
    ],
    mistakes=[
        mis("Writing 'Mumbai is bigger than any city in India'.", "Add 'other': bigger than any other city in India."),
        mis("Using 'than' after prefer, senior, junior, superior or inferior.", "These take 'to' only."),
        mis("Treating 'a little' and 'a few' as errors.", "They are positive forms. Only 'little' and 'few' alone are negative."),
        mis("Marking a long phrase as redundant just because it is wordy.", "SSC items mark echo pairs like return back, not every long phrase."),
        mis("Comparing a quality with a place ('cooler than Bengaluru').", "Use that of / those of: cooler than that of Bengaluru."),
    ],
    revision=[
        "Never more bigger, most shortest or a best.",
        "superior, senior, junior, prior, preferable: to, not than.",
        "A thing compared with its own group: any other.",
        "Climate against city: use that of / those of.",
        "Kill echoes: return back, repeat again, discuss about.",
        "advice (noun) / advise (verb). effect (noun) / affect (verb). lose / loose.",
    ],
    patterns=[
        pat("esk1", "Double or mixed comparative forms", "very common",
            "The part has more + -er, most + -est, or a superlative used for exactly two items.",
            ["Circle the adjective and its marker.", "Use one shape only: -er or more.", "Count the items. Two: comparative. Three or more: superlative with the."],
            "'More better' sounds strong, which is why setters plant it.",
            "Find the part with the error. (a) Of the two routes, (b) this one is the most shortest (c) and also the safer (d) for heavy trucks.",
            ["There are two routes, so a comparative is needed.", "'Most shortest' doubles the marker.", "Correct: 'the shorter'."],
            "(b) this one is the most shortest"),
        pat("esk2", "Redundant word pairs", "very common",
            "One idea is said twice: return back, repeat again, revert back, both of you two.",
            ["Ask of each word: does a neighbour already say this?", "'Back' after return, 'again' after repeat: cut one.", "The part with the doubled word is the error."],
            "These doubles are common in daily speech, so they feel normal.",
            "Find the part with the error. (a) Please repeat again (b) what you said (c) about the revised (d) reporting time.",
            ["'Repeat' already means say again.", "'Again' adds nothing.", "Correct: 'Please repeat what you said'."],
            "(a) Please repeat again"),
        pat("esk3", "Confusable word swap", "common",
            "A near-twin word sits in the wrong job: a noun where a verb is needed, or the wrong member of a sound-alike pair.",
            ["Decide the job: noun or verb?", "advice = noun, advise = verb. effect = noun, affect = verb. lose = misplace, loose = not tight.", "Read for sense. The wrong twin makes the sentence silly."],
            "The pairs differ by one letter, and both exist in English, so spell-check cannot help.",
            "Find the part with the error. (a) Be careful, (b) or you might loose (c) the documents (d) you collected today.",
            ["The meaning needed is 'misplace'.", "'Loose' means not tight.", "Correct: 'lose'."],
            "(b) or you might loose"),
        pat("esk4", "Comparison logic: any other, that of, to", "common",
            "The comparison is well formed but broken in logic: a member against its own group, or two unlike things, or than after a Latin word.",
            ["Name the two things compared.", "Same group: add other / any other.", "Different kinds (climate vs city): use that of / those of.", "superior, senior, junior, prior: use to."],
            "The ear accepts 'than any city'. Only the logic check catches it.",
            "Find the part with the error. (a) This model is (b) more superior than (c) the one we bought (d) last year.",
            ["'Superior' is a Latin comparative, so it takes 'to'.", "'More' also doubles it.", "Correct: 'superior to'."],
            "(b) more superior than"),
        pat("esk5", "Few, little, fewer, less and elder", "common",
            "The part has few, little, less, fewer, much, many or elder, and the noun is countable or not.",
            ["Is the noun countable? Countable: few, fewer, many. Uncountable: little, less, much.", "Family only and no than: elder.", "Few and little are negative. A few and a little are positive."],
            "Countable and uncountable words are easy to swap under time pressure.",
            "Find the part with the error. (a) There were (b) less people (c) at the meeting (d) this year.",
            ["'People' is countable.", "A countable noun takes 'fewer'.", "Correct: 'fewer people'."],
            "(b) less people"),
        pat("esk6", "Verbs that need no preposition", "occasional",
            "A verb like discuss, attack, resemble or marry is followed by an extra preposition.",
            ["Spot the verb and the word after it.", "Discuss, attack, resemble, marry take no preposition.", "Delete the extra word."],
            "These verbs already carry the meaning of the preposition.",
            "Find the part with the error. (a) The committee will (b) discuss about (c) the new rules (d) on Monday.",
            ["'Discuss' needs no preposition.", "'About' is extra.", "Correct: 'discuss the new rules'."],
            "(b) discuss about"),
    ],
)

# =====================================================================
# 7. Verb forms, tags, conditionals, structure
# =====================================================================
SUBS["es-verbs-structure"] = dict(
    concept=(
        "These errors are not about agreement, tense, articles or prepositions. They sit in the shape of the sentence. "
        "Check the verb after another verb (-ing or to), the tag at the end, the two halves of an if-sentence, "
        "the shape of a list, adjective versus adverb, and modals."
    ),
    notes=r"""### Verb plus verb: -ing or to
Some verbs take the **-ing form** (gerund). Some take **to + verb** (infinitive).

| Group | Verbs | Example |
|---|---|---|
| -ing | enjoy, avoid, deny, suggest, mind, finish, keep, practise | He denied **taking** the file. |
| to + verb | want, hope, decide, agree, refuse, promise, manage, afford, learn | They decided **to leave** early. |
| preposition + -ing | interested in, good at, afraid of, capable of, insist on | good at **singing** |

> **Watch:** *Look forward to* takes -ing. Here *to* is a preposition. Right: *I look forward to **meeting** you.* Wrong: *to meet you.* Also *be used to + -ing*.

### Question tags
A tag repeats the helping verb, flips the sign, and ends with a pronoun that matches the subject.

- Positive statement, negative tag: *They have submitted their projects, **haven't they**?* Never *isn't it?*
- Negative statement, positive tag: *He doesn't smoke, **does he**?*
- Hidden negatives (never, rarely, seldom, hardly, scarcely, little) make the statement negative: *Suresh rarely misses his walk, **does he**?*
- *I am* takes *aren't I?* *Let's* takes *shall we?* An order takes *will you?*

### If-sentences: two halves, one pattern
| Type | If-part | Main part | Example |
|---|---|---|---|
| Real future | simple present | will + verb | If she **works** hard, she **will qualify**. |
| Unreal present | simple past | would + verb | If I **were** rich, I **would travel**. |
| Unreal past | had + participle | would have + participle | If I **had known**, I **would have left** earlier. |

The planted errors are *will* inside the if-part, and *would have* inside the if-part of an unreal past.

### Parallel lists
Items joined by *and, but, or, not only ... but also* must share one shape.

- Right: *The policy aims at **reducing** paperwork, **improving** transparency and **speeding** up files.*
- Wrong: *... and **to speed** up files.* One to-form breaks the list.
- Right: *She enjoys **cooking** and **gardening**.* Wrong: *cooking and **to garden**.*

### Adjective or adverb
- Adjectives describe **nouns**. Adverbs describe **actions**.
- After an action verb, use an adverb: *The engine runs **smoothly**.* Wrong: *runs smooth.*
- After a linking verb (be, seem, taste, smell, feel), use an adjective: *The mangoes taste **delicious**.* Wrong: *taste deliciously.*

### Modals: base verb only
After **can, could, may, might, must, shall, should, will, would**, use the base verb. No *to*. No *able to*.

- Right: *You must **submit** the form by Friday.* Wrong: *must **to submit**.*
- Right: *She could **not explain** the gap.* Wrong: *could not **able to explain**.* *Could* already says ability.

> **Tip:** Ability: can swim. Necessity: must go. Possibility: may come.
""",
    tricks=[
        {"title": "Flip the tag",
         "body": "Hear the end of the sentence. A positive statement needs a negative tag. A negative word (never, rarely, hardly) needs a positive tag."},
        {"title": "Unreal past conditional",
         "body": "After 'if' about the unreal past, use had + participle. 'Would have' in the if-part is the planted error."},
        {"title": "Copy the first item",
         "body": "In a list, the first item sets the shape (-ing, to + verb or noun). Every other item must copy it.",
         "example": {"q": "The policy aims at reducing paperwork, / improving transparency / and to speed up / file movement.",
                     "steps": ["The first two items are -ing forms.", "The third must copy them.", "Correct: 'and speeding up'."],
                     "answer": "Part 3 (and to speed up)"}},
    ],
    mistakes=[
        mis("Writing 'could able to' or 'can able to'.", "Can and could already carry ability. Use the base verb only."),
        mis("Writing 'He denied to take the file'.", "Deny, enjoy, avoid and suggest take -ing: denied taking."),
        mis("Tagging a positive statement with a positive tag ('They have come, isn't it?').", "Flip the sign and match the pronoun: haven't they?"),
        mis("Putting would have inside the if-part of an unreal past.", "Use had + participle in the if-part."),
        mis("Writing 'look forward to meet'.", "Here 'to' is a preposition. Say look forward to meeting."),
    ],
    revision=[
        "enjoy, avoid, deny, look forward to: -ing. want, decide, agree: to + verb.",
        "A preposition is followed by -ing.",
        "Tag: flip the helping verb and match the pronoun. rarely, never, hardly: positive tag.",
        "If-part: future uses the present. Unreal past uses had + participle.",
        "Lists keep one shape for every item.",
        "runs smoothly (action). tastes delicious (linking). After a modal, no to and no able to.",
    ],
    patterns=[
        pat("esf1", "Gerund or infinitive after a verb or preposition", "very common",
            "A verb follows another verb or a preposition. The options are -ing or to + verb.",
            ["Find the verb or preposition before the suspect verb.", "-ing group: enjoy, avoid, deny, suggest, look forward to, interested in, capable of.", "to group: want, decide, agree, refuse, manage.", "After a preposition, always -ing."],
            "The groups are fixed by habit. 'Look forward to see' is a common slip.",
            "Find the part with the error. (a) The children are (b) looking forward to see (c) the circus (d) next week.",
            ["In 'look forward to', 'to' is a preposition.", "A preposition takes -ing.", "Correct: 'looking forward to seeing'."],
            "(b) looking forward to see"),
        pat("esf2", "Question tag sign and pronoun", "very common",
            "The sentence ends with a short tag after a comma.",
            ["Find the helping verb of the statement.", "Flip its sign. Use a pronoun for the subject.", "Hidden negatives (never, rarely, hardly) need a positive tag."],
            "'Isn't it?' is used for every sentence in speech, so it is the default wrong tag.",
            "Find the part with the error. (a) Suresh rarely misses (b) his morning walk, (c) doesn't he? (d) No error",
            ["'Rarely' makes the statement negative.", "A negative statement takes a positive tag.", "Correct: 'does he?'."],
            "(c) doesn't he?"),
        pat("esf3", "Conditional half broken", "common",
            "An if-sentence has will inside the if-part, or would have inside the if-part of an unreal past.",
            ["Read both halves.", "Real future: if + present, will + verb.", "Unreal past: if + had + participle, would have + participle."],
            "'If I would have known' is common in speech. Standard English keeps would out of the if-part.",
            "Find the part with the error. (a) If I would have known (b) about the traffic, (c) I would have left (d) much earlier.",
            ["This is an unreal past.", "The if-part needs 'had + participle'.", "Correct: 'If I had known'."],
            "(a) If I would have known"),
        pat("esf4", "Broken parallelism in a list", "common",
            "Three items are joined by and or but, and one item changes shape.",
            ["Write the items in a column.", "Compare each item's shape with the first.", "The odd item is the error."],
            "The eye reads a list as one block, so a shape change hides.",
            "Find the part with the error. (a) My grandmother enjoys cooking, (b) to garden, (c) and taking long walks (d) in the park.",
            ["After 'enjoys', the list uses -ing forms.", "'To garden' breaks the shape.", "Correct: 'gardening'."],
            "(b) to garden"),
        pat("esf5", "Adjective or adverb after a verb", "occasional",
            "A word that describes an action is an adjective (runs smooth), or a word after a linking verb is an adverb (tastes deliciously).",
            ["Ask what the word describes: an action or the subject's state.", "Action: adverb (-ly).", "Subject state after a linking verb: adjective."],
            "Both errors sound natural in speech. The verb type decides which is standard.",
            "Find the part with the error. (a) The new engine (b) runs very smooth (c) and makes (d) hardly any noise.",
            ["'Runs' is an action verb.", "An action is described by an adverb.", "Correct: 'runs very smoothly'."],
            "(b) runs very smooth"),
        pat("esf6", "Modal + to or able to", "common",
            "A modal (can, could, must, should) is followed by 'to + verb' or by 'able to'.",
            ["Spot the modal and the verb after it.", "A modal takes the bare base verb.", "Delete 'to' or 'able to'."],
            "'Can able to' is a translation habit, and it appears in papers as often.",
            "Find the part with the error. (a) The candidate (b) could not able to explain (c) the gap in (d) his employment.",
            ["'Could' already carries ability.", "'Able to' repeats it.", "Correct: 'could not explain'."],
            "(b) could not able to explain"),
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
