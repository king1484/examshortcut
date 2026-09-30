"""Readable rewrite of English > Sentence Improvement (all 6 subtopics).

Plain English, short sentences, tables, one method per fault type.
Old facts are kept; every new pattern id continues the subtopic prefix (sik5, sit5, ...).
Run: python sentence_improvement.py  (patches content/core/topics/english/sentence-improvement.json in place)
"""
import json
import re
from pathlib import Path

ROOT = Path(__file__).resolve().parents[3]
TOPIC = ROOT / "core" / "topics" / "english" / "sentence-improvement.json"


def pat(pid, name, freq, spot, steps, why, q, ex_steps, answer, formula=None):
    return {"id": pid, "name": name, "frequency": freq, "howToSpot": spot, "formula": formula,
            "steps": steps, "why": why, "example": {"q": q, "steps": ex_steps, "answer": answer}}


def mis(wrong, right):
    return {"wrong": wrong, "right": right}


SUBS = {}

# =====================================================================
# 1. Elimination ladder
# =====================================================================
SUBS["si-elimination"] = dict(
    concept=(
        "In a sentence improvement question, one part of the sentence is in bold. "
        "Four options offer a replacement, and one of them is usually *No substitution required*. "
        "You are not looking for the best-sounding English. You are looking for the one option that passes every grammar test the bold part failed."
    ),
    notes=r"""### What the question asks
One part of the sentence is bold. Decide if that part has a fault. If it does, pick the option that repairs it.

Only the bold part may change. The rest of the sentence stays as it is.

> **Rule:** Read the full sentence first. The word *before* the bold part often decides the answer (yesterday, did, each, no sooner).

### The elimination ladder
Go down these five steps. Cross out options as you go.

| Step | Question to ask | What it removes |
|---|---|---|
| 1. Verb form and tense | Does the verb suit its time word and helper? | Tense clashes, wrong form after did or have |
| 2. Agreement | Does the verb match the real subject? | Plural verbs after each, one of, the list of |
| 3. Structure | Is the order and pairing standard? | Broken inversion, mixed pairs |
| 4. Word choice | Is this the fixed partner word? | insisted for, angry on, return back |
| 5. Economy | Does an option say the same in fewer words? | Extra words (but do not over-cut) |

In most questions, two options die at step 1 or 2. Steps 3 and 4 then split the last two.

### Two kinds of wrong option
Wrong options come in two types.

- **Repeat-fault options** keep the same fault in new clothes: *more better* becomes *more good*. Cross them out at once.
- **New-fault options** fix one fault but add another. *Hardly ... than* replaces a wrong word with a wrong partner.

A good option must be cleaner than the original. It must not be wrong in a different way.

### When one fix adds a second fault
Take this sentence: *My friend has gone to Delhi yesterday.* The fault is *has gone* with *yesterday*. The fix is **went**.

*Had gone* looks like a fix. It removes the present perfect, but it needs an earlier past event. The sentence has none. So it is wrong.

> **Watch:** After you pick an option, read the whole sentence again. A fix that clashes with another word is not a fix.

### Families of decoys
Options often come from one word's relatives.

- **Look-alikes:** effect / affect, loose / lose, advice / advise.
- **Form changes:** brave / bravely / braveness.
- **Double markers:** more better, most shortest.
- **Helper swaps:** has, had, was, did in every mix.

Name the family, then pick the member that fits the job of the slot.

### No substitution required
This option is correct in about one question out of four. It is a real answer, not a decoy.

Before you choose it, run steps 1 to 3 once. Never choose it just because the sentence "sounds fine".

> **Tip:** Two options both fix the fault? Choose the one that changes less and keeps the meaning. The exam improves grammar, not ideas.
""",
    tricks=[
        {"title": "Find the anchor before you read the options",
         "body": "Look for the time word or helper verb near the bold part. Decide what the verb must look like. Then pick the option that matches your form.",
         "example": {"q": "She **has met** him yesterday evening. (met / has meet / was met / No substitution required)",
                     "steps": ["The anchor is 'yesterday', a finished past time.", "A finished past time needs the simple past.", "Simple past of meet is 'met'. The other two fail at step 1."],
                     "answer": "met"}},
        {"title": "Tag every option with its flaw",
         "body": "In your head, label each option: 'plural verb', 'wrong partner', 'breaks inversion'. If no option has a flaw, the answer is No substitution required."},
        {"title": "Meaning guard",
         "body": "Two options are both grammatical? Choose the one that keeps the original meaning word for word. An option that changes who did what is wrong."},
    ],
    mistakes=[
        mis("Choosing a correct option that changes the meaning (active to passive, an added doer).", "Keep the meaning. Change only what the fault needs."),
        mis("Choosing 'No substitution required' because the sentence sounds natural.", "Run the tense, agreement and structure checks first."),
        mis("Repairing a part that is not in bold.", "Only the bold part may change."),
        mis("Missing the anchor word outside the bold part.", "Read the whole sentence before you look at the options."),
        mis("Picking an option that fixes one fault and adds another.", "Read the finished sentence again once."),
    ],
    revision=[
        "Read the whole sentence. The anchor is often outside the bold part.",
        "Ladder: tense, agreement, structure, word choice, economy.",
        "Cross out options that repeat the fault. Cross out options that add a new fault.",
        "No substitution required is a real answer. Check steps 1 to 3 before you pick it.",
        "Two options fix the fault? The smaller change that keeps the meaning wins.",
        "Watch the decoy families: effect / affect, brave / bravely, more better, helper swaps.",
    ],
    patterns=[
        pat("sik1", "Single fault with repeat-fault decoys", "very common",
            "The bold part has one clear fault. Two or three options repeat the same fault (more good for more better, have been for was).",
            ["Name the fault and its rule.", "Cross out every option that still breaks the rule.", "Compare the survivors and pick the smallest clean repair."],
            "Repeat-fault options trap students who fix the fault in their head and stop reading.",
            "The quality of the mangoes **were** not satisfactory this season. (was / have been / No substitution required / are being)",
            ["The real subject is 'quality', which is singular.", "So the helper must be singular: 'was'.", "'Have been' and 'are being' repeat the plural fault."],
            "was"),
        pat("sik2", "No substitution required", "very common",
            "The bold part is already standard English. The other options are 'repairs' that break it.",
            ["Run the tense, agreement and structure checks on the bold part.", "If it passes every check, do not invent a fault.", "Choose No substitution required."],
            "Every paper has a few correct originals. Changing a correct sentence is a common self-made error.",
            "She **has been teaching** in this school since 2015. (teaches / is teaching / No substitution required / has taught)",
            ["'Since 2015' points to an action that started then and continues.", "That needs the present perfect continuous: 'has been teaching'.", "Each other option breaks that meaning."],
            "No substitution required"),
        pat("sik3", "Decoy families around the bold word", "common",
            "The options are relatives of the bold word: adjective and adverb forms, noun forms, effect / affect type twins.",
            ["Decide the job of the slot: does it describe a noun or an action?", "Cross out family members that do the wrong job.", "Keep the one whose meaning fits the sentence."],
            "Sorting the family by job, not by sound, clears the set.",
            "The soldier was praised for his **brave** act during the rescue. (bravely / No substitution required / braveness / bravest)",
            ["The slot describes the noun 'act'.", "A word that describes a noun is an adjective: 'brave'.", "Bravely is an adverb and braveness is a noun. So the original is right."],
            "No substitution required"),
        pat("sik4", "Two-fault trap options", "common",
            "One tempting option fixes the visible fault but adds a second one: a wrong sequence, a broken pair or a wrong word type.",
            ["Fix the visible fault in your head first.", "Test each tempting option against the other words in the sentence.", "Reject any option that needs a second repair."],
            "'Had gone yesterday' feels fixed. Only a second look shows the new fault.",
            "My friend **has gone** to Delhi yesterday to attend an interview. (went / had gone / No substitution required / has went)",
            ["'Yesterday' needs the simple past: 'went'.", "'Had gone' needs an earlier past event, and the sentence has none.", "'Has went' keeps the fault and adds another."],
            "went"),
        pat("sik5", "Meaning guard between clean options", "occasional",
            "Every option is grammatical. One of them changes who does the action (active to passive) or adds a new doer.",
            ["Say who does the action in the original.", "Cross out options that change the doer or the meaning.", "If the original is correct, pick No substitution required."],
            "The exam corrects grammar. It does not ask you to rewrite the idea.",
            "**The police caught the thief** after a long chase. (The thief was caught by the police / No substitution required / The thief caught the police / Caught the thief the police)",
            ["The original is a correct active sentence.", "The passive option is also correct English, but nothing asks for it.", "The other two options change the meaning or break the order."],
            "No substitution required"),
    ],
)

# =====================================================================
# 2. Tense and sequence
# =====================================================================
SUBS["si-tense-sequence"] = dict(
    concept=(
        "Many improvement questions bold a verb whose tense clashes with a word in plain sight, like *yesterday*, *since* or *already*. "
        "Find that word first. It tells you the tense. "
        "Then check the other verbs in the sentence, because tense is always about a pair of times."
    ),
    notes=r"""### The anchor word decides the tense
Circle the time word before you look at the options. It fixes the form of the bold verb.

| Anchor in the sentence | Form needed |
|---|---|
| yesterday, last week, ago, in 2019 | simple past |
| since + a point, for + a length, so far, already, yet | perfect or perfect continuous |
| every day, at nine (habit) | simple present |
| when / if / until with a future meaning | simple present inside that clause |
| by the time + past, or the earlier of two past events | past perfect |
| said, asked, told (past reporting verb) | backshifted past forms |

> **Example:** *When I reached the station, the train had already left.* The train left first, so it takes the past perfect.

### Since and for
*Since 2015*, *for twenty years* and *since childhood* link a past start to now. If the action still goes on, use **has / have been + -ing**.

*He has been working in the same mill for twenty-two years.* The plain *is working* does not fit *for + length*.

### Reported speech needs two changes
After a past reporting verb, make two changes.

1. **Backshift.** Move the tense one step back: *has locked* becomes *had locked*, *will* becomes *would*, *is* becomes *was*.
2. **Statement order.** An indirect question is no longer a question. Say *asked why he was late*, not *why was he late*.

Use one connective only: *asked whether* or *asked why*. Never *asked that whether*.

### Conditional sentences come in pairs
Each type has a fixed pair of halves.

- **Real future:** if + present, will + verb. *If he apologises, I will withdraw the case.*
- **Unreal present:** if + past (were for every person), would + verb. *If I were the collector, I would act.*
- **Unreal past:** if + had + participle, would have + participle. *If he had studied, he would have cleared it.*

> **Watch:** The bold verb may sit in either half. Check that both halves match one row.

### Continuous or simple?
Continuous forms need an action in progress. *She was cooking when the guests arrived* is not the same as *She cooked when the guests arrived*. The first says she was busy. The second says two events followed each other.

Pick the form that keeps the original meaning.

### Check the other verbs
Some sentences have two verbs. *He has left for Delhi and will return next month* is correct. The anchor *next month* is future, so *will return* is right.

After you pick an option, look at the verbs that are not in bold. A fix that clashes with them is a trap.

> **Tip:** The wrong form is already marked in bold. Your job is to write the right form. Re-read the whole sentence once after every fix.
""",
    tricks=[
        {"title": "The yesterday test",
         "body": "See a finished-time word? Cross out every perfect and continuous option at once. Usually one option is left.",
         "example": {"q": "The train **has left** before we reached the station. (had left / has been leaving / leave / No substitution required)",
                     "steps": ["Both events are in the past. The train left first.", "The earlier event takes the past perfect: 'had left'.", "'Has left' is present perfect and cannot go with 'reached'."],
                     "answer": "had left"}},
        {"title": "Backshift plus straight order",
         "body": "In a reported question, two things change: the tense moves back and the order becomes a statement. Each wrong option usually breaks one of these. Check both."},
        {"title": "Since and for health check",
         "body": "'Since 2015' or 'for ten years' with a continuing action needs 'has / have been'. Options without it die at once."},
    ],
    mistakes=[
        mis("Using the present perfect with 'yesterday' or 'last year' because it sounds formal.", "A finished past time takes the simple past."),
        mis("Backshifting the tense but keeping question order in reported speech.", "Do both: 'asked why he was late'."),
        mis("Changing a correct perfect to the simple past when 'since' or 'for' is present.", "Keep has / have been for a continuing action."),
        mis("Changing continuous to simple (or back) and altering the meaning.", "Keep the meaning: was cooking is not the same as cooked."),
        mis("Putting 'will' inside an if-clause or a when-clause.", "Use the simple present there. 'Will' belongs to the main clause."),
    ],
    revision=[
        "Circle the anchor word first. The verb obeys it.",
        "ago, yesterday, last week gives simple past.",
        "since + point gives perfect; for + length + still going gives has been -ing.",
        "Reported questions: backshift, statement order, one connective.",
        "Conditionals come in three fixed pairs. Do not mix the halves.",
        "Re-read the whole sentence after your fix. The trap may sit outside the bold part.",
    ],
    patterns=[
        pat("sit1", "Anchor-based tense fix", "very common",
            "The bold verb's tense clashes with a time word in plain sight (already, yesterday, by the time, every morning).",
            ["Circle the anchor.", "Read the needed form from the table.", "Pick the matching option. Reject options that shift tense again without a second event."],
            "Tense questions are anchor questions. With the anchor circled, the options sort themselves.",
            "When I reached the station, the train **already left**. (had already left / has already left / No substitution required / already leaves)",
            ["The train left before I reached. That is the earlier past event.", "The earlier event takes the past perfect: 'had already left'.", "'Has already left' reaches into the present and breaks the story."],
            "had already left"),
        pat("sit2", "Reported speech: backshift and order", "common",
            "The sentence reports what someone asked or said (asked, told, enquired). The bold part keeps question order, misses the backshift, or joins 'that' to a wh-word.",
            ["Spot the past reporting verb.", "Backshift the tense one step and restore statement order.", "Keep one connective only: why, whether or if."],
            "Indirect speech has two rules, and each wrong option breaks one.",
            "The teacher asked the boy **why was he** late again. (why he was / No substitution required / why is he / that why he was)",
            ["An indirect question takes statement order: subject before helper.", "The tense stays in the past after 'asked'.", "'That why' has two connectives, so it is wrong."],
            "why he was"),
        pat("sit3", "Conditional half repair", "common",
            "An if-sentence has mismatched halves: 'will' inside the if-clause, or a real-future frame where an unreal one is meant.",
            ["Read both halves of the sentence.", "Match them to one of the three fixed pairs.", "Real future: if + present. Unreal present: were. Unreal past: had + participle."],
            "The if-clause never holds 'will' in a real-future sentence.",
            "If he **will apologise** sincerely, I will withdraw the complaint. (apologises / No substitution required / would apologise / apologised)",
            ["The main clause has 'will withdraw', so this is a real future.", "The if-clause takes the simple present: 'apologises'.", "'Would apologise' belongs to the unreal present and breaks the pair."],
            "apologises"),
        pat("sit4", "Since / for with a continuing action", "common",
            "The sentence gives a starting point or a length of time (since 1998, for twenty years). The bold verb is in a plain present or present continuous.",
            ["Ask: does the action still continue?", "If yes, use has / have been + -ing.", "Reject the plain present that ignores the length of time."],
            "The perfect ties a past start to now. The plain present cuts that tie.",
            "My father **is working** in the same mill for twenty-two years. (has been working / No substitution required / works / had been working)",
            ["'For twenty-two years' gives a length of time up to now.", "He still works there, so the action continues.", "Use the present perfect continuous: 'has been working'."],
            "has been working"),
        pat("sit5", "Future meaning inside a when or until clause", "common",
            "The bold verb sits in a clause with when, as soon as, until or before, and the sentence talks about the future.",
            ["Find the main clause and check that it uses will.", "Put the time clause in the simple present.", "Reject 'will' and 'would' inside the time clause."],
            "A time clause with future meaning uses the simple present. 'Will' goes only in the main clause.",
            "The match will begin as soon as the rain **will stop**. (stops / No substitution required / would stop / stopped)",
            ["The main clause is 'the match will begin', which is future.", "The 'as soon as' clause must be in the simple present.", "So 'will stop' becomes 'stops'."],
            "stops"),
    ],
)

# =====================================================================
# 3. Agreement
# =====================================================================
SUBS["si-agreement"] = dict(
    concept=(
        "When the bold part holds a verb, first find the **real subject**. "
        "Phrases like *of the students* or *as well as the players* often stand between the subject and the verb. "
        "They do not change the number of the verb."
    ),
    notes=r"""### Find the real subject
When the bold part has a helper like *was / were, has / have, is / are*, run three checks.

1. Find the noun the sentence is about. That is the real subject.
2. Cross out the extra phrase. Phrases with *of, with, along with, as well as, together with, besides, including* never hold the subject.
3. Match the helper to the number of the real subject.

> **Example:** *The captain, as well as the openers, **was** blamed.* Cross out the extra phrase. What is left is *The captain was blamed*.

### Phrases that hide the subject
- *The bundle of old files **was** sent.* (bundle, not files)
- *The quality of the mangoes **was** poor.*
- *The list of holidays **has been** announced.*
- *One of the students **has** won.*

### One of, each of, neither of
These openers are always singular. The plural noun after *of* is a decoy.

- *One of my cousins **has settled** in Wellington.*
- *Each of the candidates **is** to report at nine.*
- *Neither of the two answers **was** acceptable.*

### The nearer-subject rule
With *either ... or*, *neither ... nor* and *not only ... but also*, the verb agrees with the **nearer** subject.

- *Either the secretary or the joint secretaries **are** responsible.*
- *Not only the students but also the warden **was** honoured.*

### Quantity and group words

| Phrase | Verb | Example |
|---|---|---|
| a number of + plural noun | plural | A number of films **have been** censored. |
| the number of + plural noun | singular | The number of films **has** fallen. |
| many a + singular noun | singular | Many a farmer **has** shifted to drip irrigation. |
| an amount seen as one unit | singular | Ten thousand rupees **is** a big amount. |

Collective nouns like *jury* and *committee* usually take a singular verb with *its*.

### Two subjects joined by and
Two nouns joined by *and* take a plural helper: *The principal and the secretary **were** present.* These are two people.

One person with one article is singular: *The principal and secretary **was** present.* Here one person holds both posts.

In the passive, the same check runs on the *be* helper. *The bridge **was** built. The bridges **were** built.* The participle never changes.

> **Tip:** Fix only the helper. Keep the rest of the bold part as it is. If the original already agrees, choose No substitution required.

### Verb form after a helper
- After *did, does, do*: use the base verb. *Did he arrive?* (not *did he arrived*)
- After *have, has, had*: use the past participle.
- After *be*: use -ing (continuous) or the participle (passive).
""",
    tricks=[
        {"title": "Cover the phrase and read the skeleton",
         "body": "Cover 'of the students' type phrases with a finger. Read what is left: 'One ___ won'. The right helper is now easy.",
         "example": {"q": "One of the students **have** won the quiz. (has / were / are / No substitution required)",
                     "steps": ["Cover 'of the students'.", "The skeleton is 'One ___ won'.", "'One' is singular, so the helper is 'has'."],
                     "answer": "has"}},
        {"title": "Check the helper chain",
         "body": "did takes the base verb, have takes the participle, be takes -ing or the participle. If the bold part has a helper, check its partner form first."},
        {"title": "Two subjects with and",
         "body": "Two subjects joined by 'and' take a plural verb. The exception is a pair that names one thing, like 'bread and butter is'."},
    ],
    mistakes=[
        mis("Agreeing with the nearest noun instead of the real subject.", "Cross out the of-phrase and find the head noun."),
        mis("Writing a participle after 'did' (did he arrived).", "After did, use the base verb: did he arrive."),
        mis("Choosing an option that changes active to passive or adds a doer.", "Fix only the helper. Keep the meaning."),
        mis("Accepting a plural verb after 'each of the + plural noun'.", "Each, one and neither stay singular."),
        mis("Treating 'as well as' like 'and'.", "As well as only adds information. It does not make the subject plural."),
    ],
    revision=[
        "of, with, along with, as well as: these phrases never hold the subject.",
        "one of, each of, neither of, many a: singular helper.",
        "either ... or, neither ... nor, not only ... but also: agree with the nearer subject.",
        "a number of: plural. The number of: singular. An amount as one unit: singular.",
        "Fix only the helper. Leave a correct participle alone.",
        "did + base verb; have + participle; be + -ing or participle.",
    ],
    patterns=[
        pat("sia1", "Phrase between subject and helper", "very common",
            "The bold helper (was / were, has / have) comes after 'X of Y' or 'X, as well as Y,' and was matched to the wrong noun.",
            ["Cross out the of / with / as-well-as phrase.", "Read only the real subject and the helper.", "Pick the helper that matches the subject. Leave the participle alone."],
            "The extra phrase sounds like the subject. Crossing it out removes the illusion.",
            "The captain, as well as the openers, **were** blamed for the collapse. (was / No substitution required / have been / are)",
            ["Cross out 'as well as the openers'.", "The subject is 'the captain', which is singular.", "So the helper is 'was'."],
            "was"),
        pat("sia2", "One of / each of / neither of", "very common",
            "The subject begins with one of, each of or neither of, and the bold helper is plural.",
            ["Spot the opener: one, each or neither.", "Remember that all three are singular. The plural noun after 'of' is a decoy.", "Choose the singular helper: has, is or was."],
            "These three openers are always singular, so the fix is mechanical.",
            "Each of the shortlisted candidates **are** to report by nine tomorrow. (is / No substitution required / were / have been)",
            ["The head word is 'each', which is singular.", "'Candidates' is only the decoy after 'of'.", "So the helper is 'is'."],
            "is"),
        pat("sia3", "Nearer-subject rule (or / nor / not only ... but also)", "common",
            "Two subjects are joined by either ... or, neither ... nor or not only ... but also. The bold helper agrees with the first subject.",
            ["Ignore the first subject.", "Look at the subject just before the helper.", "Match the helper to that nearer subject."],
            "This rule beats every other in paired subjects. Setters make the two subjects differ in number.",
            "Either the secretary or the joint secretaries **is** responsible for the circular. (are / No substitution required / was / has been)",
            ["The nearer subject is 'joint secretaries'.", "That subject is plural.", "So the helper is 'are'."],
            "are"),
        pat("sia4", "Quantity phrase (a number of / many a)", "common",
            "The subject is a quantity phrase: a number of, the number of or many a. The helper's number goes against the phrase's rule.",
            ["Read the phrase slowly: 'a number of' is plural and 'the number of' is singular.", "'Many a' + a singular noun is singular.", "Match the helper and keep the rest of the bold part."],
            "One small word before 'number' controls the verb. 'Many a' hides a singular verb under a plural meaning.",
            "A number of films **has been** censored this month. (have been / No substitution required / are been / was)",
            ["'A number of' means 'many'.", "So the subject is plural.", "The helper is 'have been'."],
            "have been"),
        pat("sia5", "Two subjects joined by and", "common",
            "Two nouns with 'and' come before the bold helper, and the helper is singular.",
            ["Check whether the nouns are two different people or things.", "Two subjects with 'and' take a plural helper.", "Only a pair naming one thing, like bread and butter, is singular."],
            "Each noun with its own article names a separate person, so the number is plural.",
            "The principal and the vice-principal **was** present at the function. (were / No substitution required / is / has been)",
            ["'The principal' and 'the vice-principal' are two people.", "Two subjects with 'and' are plural.", "Past tense plural helper: 'were'."],
            "were"),
    ],
)

# =====================================================================
# 4. Comparison and structure
# =====================================================================
SUBS["si-comparison-structure"] = dict(
    concept=(
        "Comparison questions test four things. These are a doubled marker (*more better*), unlike things compared, *to* after *senior* and its kin, and the count of items. "
        "The right option is usually the smallest change. "
        "An option that rewrites half the sentence is only there to distract you."
    ),
    notes=r"""### Four repairs for comparisons
**1. Double marker.** *More better*, *most shortest* and *more preferable* mark the degree twice. Drop the extra word: *better*, *shortest*, *preferable*.

**2. Compare like with like.** Compare a thing with the same kind of thing.

- *The climate of Shimla is cooler than **that of** Delhi.* (climate with climate)
- *The roads of Bhopal are wider than **those of** Indore.* (roads with roads)

Use *that* for a singular noun and *those* for a plural noun.

**3. Latin comparatives take *to*.** After *senior, junior, superior, inferior, prior, preferable* and *prefer*, use **to**. Never use *than*.

- *He is senior to me.*
- *I prefer tea to coffee.*

**4. Count the items.** Exactly two items need the comparative: *the larger of the two*. Three or more need the superlative: *the largest of the five*. *Of all* needs the superlative.

> **Rule:** Read the count phrase (*of the two*, *of all*, *of the five*) before you judge the form.

### Words that are already marked
These words carry their degree inside them. They refuse *more* or *most*.

better, worse, elder, former, latter, major, minor, superior, inferior, prior, senior, junior, preferable, perfect, unique, ideal, complete.

Say *better*, never *more better*. Say *unique*, never *most unique*. A unique thing has no scale to climb.

### How the options are built
- One option repeats the fault in new clothes: *more better* becomes *more good*. *Senior than* becomes *more senior than*.
- One option fixes the marker but breaks the count. *The most effective* stays where only two items exist.
- One option turns *than Delhi* into a full clause like *Delhi's streets are*. This doubles the sentence and is never the cleanest fix.
- The clean repair changes only what the fault needs.

> **Tip:** Two options both fix the fault? Choose the smaller change.

### Worked pass
Take this sentence: *The climate of Shimla is more cooler than Delhi.* Work through it in three steps.

1. *More cooler* marks the degree twice. Drop *more*.
2. *Climate* is compared with *Delhi*, a city. Use *that of Delhi*.
3. The repaired line is *The climate of Shimla is cooler than that of Delhi.*

A good answer often fixes two small things at once. Look for both before you choose.

### Check the fix
After you substitute, read the whole sentence again. A new fault can hide inside the fix.

- *Those of* with a singular noun is wrong.
- *Prefer to* with *than* still after it is wrong.
- A superlative without *the* is wrong.

> **Watch:** *Than that of* is not always right. Use it only when the comparison is between things that belong to a place or person.
""",
    tricks=[
        {"title": "Insert that of or those of",
         "body": "Two 'the X of A' phrases are compared, but the second is bare. Add 'that of' for a singular noun or 'those of' for a plural noun.",
         "example": {"q": "The roads of Bhopal are wider than **Indore**. (those of Indore / that of Indore / Indore's roads are / No substitution required)",
                     "steps": ["The first noun is 'roads', which is plural.", "Roads must be compared with roads.", "Plural takes 'those of'."],
                     "answer": "those of Indore"}},
        {"title": "Check for a double marker",
         "body": "Look for more + a word that already has -er, or most + a word that already has -est. If you find one, the repair is a subtraction."},
        {"title": "Count first",
         "body": "Find the count phrase in the sentence. 'Of the two' means the comparative with 'the'. 'Of all' means the superlative."},
    ],
    mistakes=[
        mis("Choosing 'than that of' when the sentence does not compare two possessive phrases.", "Use 'that of' or 'those of' only when unlike things are compared."),
        mis("Fixing more better into more good.", "Drop the extra marker. Say 'better'."),
        mis("Writing 'senior than' or 'prefer X than Y'.", "Say 'senior to' and 'prefer X to Y'."),
        mis("Using the superlative when the sentence says 'of the two'.", "Two items need the comparative with 'the': the more useful."),
        mis("Treating 'No substitution required' as wrong because the sentence looks plain.", "Plain and correct are different from wrong."),
    ],
    revision=[
        "more better and most shortest: cut the doubled marker.",
        "Compare like with like: that of (singular), those of (plural).",
        "senior, junior, superior, inferior, prior, preferable, prefer: use to.",
        "Of the two: comparative with the. Of all: superlative with the.",
        "Already-marked words: better, elder, unique, perfect, ideal.",
        "Reject options that fix the marker but break the count.",
    ],
    patterns=[
        pat("sic1", "Double-marker fix", "very common",
            "The bold part has more + an -er word or most + an -est word (more better, far more better, most shortest).",
            ["Find the form that is already marked (better, shortest).", "Delete the extra marker. The fix is a subtraction.", "Reject options that swap one doubling for another (more good) or break the comparison."],
            "The double marker is pure repetition. The right option stops marking twice.",
            "The second model is **far more better** than the first. (far better / No substitution required / more good / best)",
            ["'Better' already means 'more good'.", "Keep the word 'far' and drop 'more'.", "'Best' does not fit a comparison with 'than'."],
            "far better"),
        pat("sic2", "That of / those of repair", "very common",
            "The sentence compares 'the X of A' with a bare name ('than Delhi'), so unlike things are compared.",
            ["Name the two things being compared.", "They must be the same kind: X with X.", "Add 'that of' (singular) or 'those of' (plural) before the second name."],
            "'Those of' quietly brings back the missing 'the streets of'.",
            "The streets of Mysuru are cleaner than **Bangalore**. (those of Bangalore / that of Bangalore / No substitution required / Bangalore's streets)",
            ["Streets are compared with a city. That is unlike.", "Streets must be compared with streets.", "Plural noun takes 'those of Bangalore'."],
            "those of Bangalore"),
        pat("sic3", "Latin comparative and prefer", "common",
            "The bold part joins senior, junior, superior, inferior, prior, preferable or prefer with 'than' or another wrong partner.",
            ["Spot the Latin comparative or 'prefer'.", "Its partner is always 'to'.", "Reject options that keep 'than' in any form (more senior than)."],
            "These words came into English with 'to' attached. 'Than' belongs only to -er and more forms.",
            "My sister **prefers coffee than** tea in winter. (prefers coffee to / No substitution required / prefer coffee to / is preferring coffee than)",
            ["The verb is 'prefers'. Its partner is 'to'.", "The subject 'my sister' is singular, so keep 'prefers'.", "'Prefer coffee to' drops the -s and breaks agreement."],
            "prefers coffee to"),
        pat("sic4", "Count of items (two or more)", "common",
            "The sentence says how many items there are (of the two, of all, of the five) and the bold form has the wrong degree.",
            ["Find the count phrase.", "Two items: comparative with 'the'. Three or more: superlative with 'the'.", "Pick the option with the right degree. Keep 'the'."],
            "The count fixes the degree. The neighbouring degree is the decoy.",
            "Iron is **the most useful** of the two metals for building bridges. (the more useful / No substitution required / more useful / useful most)",
            ["'Of the two metals' gives a count of two.", "Two items need the comparative: 'more useful'.", "Keep 'the': 'the more useful'."],
            "the more useful"),
        pat("sic5", "Words that are already absolute", "occasional",
            "The bold part adds more, most or very to a word like unique, perfect, ideal or complete.",
            ["Spot the absolute word.", "Remove the extra marker.", "Keep the plain word."],
            "An absolute word has no scale, so it cannot be compared.",
            "Every fingerprint is **most unique**, so police rely on it. (unique / No substitution required / more unique / very much unique)",
            ["'Unique' means one of a kind.", "A word like that has no degrees.", "Drop 'most': 'unique'."],
            "unique"),
    ],
)

# =====================================================================
# 5. Precision fixes
# =====================================================================
SUBS["si-precision-fixes"] = dict(
    concept=(
        "Some bold parts have no verb. The fault is a wrong small word: an article, a preposition, a pronoun, or a word that repeats another. "
        "The options then differ by one or two words. "
        "Learn the fixed partners well, because meaning alone will pull you towards the wrong one."
    ),
    notes=r"""### Small words, big marks
Many bold parts hold only an article, a preposition or a doubled word. The fix is small. Speed comes from knowing the fixed pairs.

### Articles follow sound
The sound of the next word decides *a* or *an*, not its spelling.

- Vowel sound gives **an**: *an hour, an honest man, an MLA, an X-ray*.
- Consonant sound gives **a**: *a university, a European, a one-day match*.
- *A ancient route* becomes ***an** ancient route*.

> **Rule:** Say the next word aloud. Listen to its first sound.

### Preposition partners
Each word has its own fixed preposition.

| Word | Partner |
|---|---|
| approve, insist, fond, afraid, capable | of, on, of, of, of |
| agree | with (a person), to (a proposal) |
| angry | with (a person), at (a thing) |
| apply | to (an office), for (a post) |
| abide, comply | by, with |

When only the preposition is bold, recall the partner and choose it.

### Cut the echo
Some pairs say one idea twice. Keep the single strong word.

*revert back* becomes *revert*. *return back* becomes *return*. *repeat again* becomes *repeat*. *final conclusion* becomes *conclusion*.

The right option is simply shorter.

### Swapped twins

| Wrong twin | Right twin | Why |
|---|---|---|
| advise (noun slot) | advice | advice is the noun, advise is the verb |
| effect (verb slot) | affect | affect is the verb, effect is the noun |
| loose (misplace) | lose | loose means not tight |
| principal (a rule) | principle | a principle is a rule |

### More pairs to keep ready
- **win / beat:** India *beat* Australia. India *won* the match.
- **say / tell:** She *said* that ... She *told me* that ... (tell needs a person).
- **hear / listen:** *hear* is by chance. *Listen to* is on purpose: *listen to the news*.
- **die of / die from:** *die of* a disease, *die from* an injury.
- **comprise:** The team *comprises* eleven players (no *of*).
- **cope with** is right. *Cope up with* is wrong.

### Pronouns after prepositions
Use the object form after a preposition: *between you and **me**, for **him** and **me***. The reflexive *myself* never replaces *me*.

> **Watch:** Also, *despite of* is wrong. Use *despite* or *in spite of*.

### Few and a few, elder and older
- *Few* means hardly any. It has a negative feel: *Few people came*.
- *A few* means some. It has a positive feel: *A few people came, so we began*.
- *Elder* is for family members and is not followed by *than*: *my elder brother*. Use *older* with *than*.
- *Farther* is about distance. *Further* is about more of something: *further details*.

**Method**
1. Name the job of the small word: article, preposition or pronoun.
2. Recall the rule or the fixed pair.
3. Choose the option that changes only the faulty word.
""",
    tricks=[
        {"title": "Sweep the small words",
         "body": "Read only the small words in the bold part: a, an, the, in, on, at, me, myself. A wrong one usually stands alone. Fix it and finish.",
         "example": {"q": "She is **a honest** woman. (an honest / the honest / honest / No substitution required)",
                     "steps": ["'Honest' starts with a vowel sound, because the h is silent.", "A vowel sound needs 'an'.", "'Honest' alone leaves 'She is honest woman', which is not correct."],
                     "answer": "an honest"}},
        {"title": "The myself firewall",
         "body": "A reflexive like 'myself' never replaces a plain object pronoun. Any option that offers 'myself' where 'me' belongs is a decoy."},
        {"title": "Redundancy flinch",
         "body": "Learn the fatal pairs: return back, repeat again, revert back, final conclusion. When one is bold, the shorter option is the key."},
    ],
    mistakes=[
        mis("Judging a / an by spelling (a hour, an university).", "Judge by sound: an hour, a university."),
        mis("Choosing 'myself' as a polite word for 'me'.", "Use 'me' as the object. 'Myself' needs the same person as the doer."),
        mis("Changing few to a few (or back) without checking the meaning.", "Few means hardly any. A few means some."),
        mis("Writing 'despite of'.", "Write 'despite' or 'in spite of'."),
        mis("Choosing a preposition by meaning alone.", "Recall the fixed partner: approve of, insist on, fond of."),
    ],
    revision=[
        "a / an follows sound: an hour, an MLA, a university, a European.",
        "approve of, insist on, fond of, agree with a person, agree to a plan.",
        "revert back, return back, repeat again: cut the echo.",
        "advice (noun) / advise (verb); affect (verb) / effect (noun); lose / loose.",
        "Between you and me. Myself never replaces me.",
        "win a match, beat a team; say that, tell a person.",
    ],
    patterns=[
        pat("sip1", "Preposition partner repair", "very common",
            "The bold part is (or holds) the preposition after a verb or adjective. The options are preposition swaps.",
            ["Find the verb or adjective the preposition hangs on.", "Recall its fixed partner: approve of, insist on, fond of.", "Ignore options that change the rest of the phrase."],
            "Preposition questions test memory. Usage picks the partner, not logic.",
            "The committee does not approve **for** the proposal. (of / No substitution required / with / to)",
            ["The verb is 'approve'.", "Its fixed partner is 'of'.", "The other prepositions belong to other verbs."],
            "of"),
        pat("sip2", "Article sound repair", "common",
            "The bold part is an article + a word, and the article disagrees with the word's first sound (a honest, an useful, a MLA).",
            ["Say the word after the article aloud.", "Vowel sound: an. Consonant sound: a.", "Ignore the spelling. Hour and university are the classic traps."],
            "The rule follows speech. Setters pick words where spelling and sound disagree.",
            "The temple was built near **a ancient** trading route. (an ancient / No substitution required / a ancients / the ancients)",
            ["'Ancient' starts with a vowel sound.", "So the article is 'an'.", "Only the article needs repair."],
            "an ancient"),
        pat("sip3", "Redundancy cut", "very common",
            "The bold part has an echo (return back, revert back, repeat again). The right option is simply shorter.",
            ["Ask: does one word already hold the other's meaning?", "Keep the single strong word.", "Reject options that keep the echo."],
            "The echo feels natural in speech, so the eye skips it.",
            "Please **revert back** to my mail by Friday. (revert to / No substitution required / revert back to / reversing to)",
            ["'Revert' already means to come back.", "'Back' repeats the idea.", "Cut it and keep 'to': 'revert to'."],
            "revert to"),
        pat("sip4", "Swapped twin repair", "common",
            "The bold word is the wrong member of a twin pair: advice / advise, effect / affect, lose / loose, principal / principle.",
            ["Decide the slot's job: noun or verb?", "Map the job to the twin: advice (noun), advise (verb).", "Reject options that change the form further (advising)."],
            "Both twins are real words. Only the noun or verb test shows the wrong one.",
            "The doctor's **advise** was to rest for a week. (advice / No substitution required / advises / advising)",
            ["The slot is a noun, because 'the doctor's ___' names a thing.", "The noun is 'advice'.", "'Advise' is the verb."],
            "advice"),
        pat("sip5", "Win / beat and say / tell", "occasional",
            "The bold verb takes the wrong object: a match after 'beat', an opponent after 'win', or a person after 'say'.",
            ["Check the object: a person or team, or a prize or match?", "beat + opponent; win + match or prize.", "say + that; tell + person."],
            "These pairs look alike but each verb takes one kind of object.",
            "India **won** Australia in the final. (beat / No substitution required / had won / was winning)",
            ["The object is 'Australia', an opponent.", "An opponent goes with 'beat'.", "'Win' goes with the match or the prize."],
            "beat"),
    ],
)

# =====================================================================
# 6. Structure and inversion
# =====================================================================
SUBS["si-structure-inversion"] = dict(
    concept=(
        "Some bold parts fail in sentence shape, not in tense or agreement. "
        "Four shapes cover the exam: inversion after negative openers, dangling openers, matching shapes in lists and pairs, and statement order in reported questions. "
        "Each is a fixed pattern, so the right option is easy to spot once you know the shape."
    ),
    notes=r"""### Inversion: the helper jumps first
Some opening words force the helper *before* the subject.

- **No sooner ... than:** *No sooner **had the train left** than the TTE began checking.*
- **Hardly / Scarcely ... when:** *Hardly **had the results been announced** when the servers crashed.*
- **Negative adverbs** (never, seldom, rarely, little): *Never **have I witnessed** such a peaceful poll.*

The frame has three parts: opener, helper before subject, and the fixed partner word. Test each part on its own.

> **Watch:** *No sooner* pairs with **than**. *Hardly* and *scarcely* pair with **when**.

Both *No sooner did he arrive than* and *No sooner had he arrived than* are correct. Each half must stay inside its own frame.

### Dangling openers
An -ing or *being* opener borrows the subject of the main clause. That subject must be the doer.

- Wrong: *Being a rainy day, the mela was cancelled.* The mela was not a rainy day.
- Right: *It being a rainy day, the mela was cancelled.*
- Wrong: *Having eaten our lunch, the train departed.* The train ate nothing.
- Right: *Having eaten our lunch, we boarded the train.*

> **Tip:** Ask who does the opener's action. That person must be the subject.

### Parallel shapes
Items joined by *and, or, but* keep one shape.

- Right: *typing, filing papers, and drafting mails*.
- Wrong: *typing, to file papers, and how to draft mails*.

Pairs work the same way. After *not only* and *but also*, the two parts must be the same kind of word: *not only intelligent but also hardworking*.

### Reported questions
Inside a reported question, statement order returns. *He asked why I had left*, not *why did I leave*. There is no *that*, and the tense moves back.

### Two more structure repairs
- **Only:** put *only* before the word it limits. *Only he accompanied me* means nobody else came. *He accompanied only me* means he took nobody else.
- **Split infinitive:** *to examine carefully* is safe. The exam rarely asks you to change it, so prefer No substitution required unless the order is truly wrong.

### Worked pass
Take this sentence: *Hardly had she entered the hall than the lights went out.* Test it in three steps.

1. *Hardly* opens the sentence. The helper *had* comes before *she*. That part is right.
2. *Hardly* pairs with *when*, not *than*. That is the fault.
3. The repaired line is *Hardly had she entered the hall when the lights went out.*

Check the order first, then the partner word. The fault is often only the partner.

**Method**
1. Find the opener or the connector that controls the shape.
2. Recall its fixed frame: inversion order, the doer of the -ing, the list shape.
3. Pick the option that fits the frame. It is usually the one that reorders, not the one that rewords.
""",
    tricks=[
        {"title": "Opener triggers a flip",
         "body": "Negative word first? Expect helper before subject: had I reached, did he arrive. Then check the partner: than or when.",
         "example": {"q": "No sooner **he arrived** than the power failed. (did he arrive / he did arrive / had he arriving / No substitution required)",
                     "steps": ["'No sooner' opens the sentence, so the helper comes first.", "After 'did', the verb is the base form: 'arrive'.", "'Did he arrive' fits the frame with 'than'."],
                     "answer": "did he arrive"}},
        {"title": "Who does the -ing?",
         "body": "Name the doer of the opening action. If the main subject is not that doer, pick the option that makes the doer the subject."},
        {"title": "Shape match across pairs",
         "body": "Cover the pair words. Compare the shapes on both sides. If one side is a verb and the other a noun, that is the fault."},
    ],
    mistakes=[
        mis("Inverting a clause that has no negative opener.", "Invert only after openers like no sooner, hardly, never, seldom."),
        mis("Pairing 'Hardly ... than' or 'No sooner ... when'.", "No sooner goes with than. Hardly and scarcely go with when."),
        mis("Fixing a dangling opener by rewording the opener only.", "Change the subject so it names the doer."),
        mis("Mixing shapes in a list or pair (not only cheap but also it lasts long).", "Make every item the same kind of word."),
        mis("Keeping question order in a reported question.", "Use statement order: asked why he was late."),
    ],
    revision=[
        "No sooner ... than. Hardly / scarcely ... when. The helper comes before the subject.",
        "Never, seldom, rarely at the front: invert (Never have I seen).",
        "An -ing or being opener must describe the main subject.",
        "Lists and pairs keep one shape for every item.",
        "Reported questions: statement order, backshift, no 'that'.",
        "Only goes before the word it limits.",
    ],
    patterns=[
        pat("siv1", "No sooner / hardly frame repair", "very common",
            "The sentence opens with No sooner or Hardly / Scarcely. The bold part shows statement order, a wrong partner (than or when) or a wrong helper.",
            ["Name the frame: no sooner ... than; hardly / scarcely ... when.", "Check the order: opener, helper, subject, verb.", "Check the helper and verb match: had + participle, did + base verb."],
            "The frame has three parts, and each wrong option breaks exactly one.",
            "No sooner **the train had left** the platform than the TTE began checking tickets. (had the train left / No substitution required / the train had left / the train had leave)",
            ["'No sooner' needs the helper before the subject.", "So it is 'had the train left'.", "'The train had left' keeps statement order, and 'had leave' breaks the participle."],
            "had the train left"),
        pat("siv2", "Negative adverb inversion", "common",
            "The sentence opens with never, seldom, rarely or little. The bold part keeps normal order (I have, we see).",
            ["Spot the negative adverb at the front.", "Invert: helper, subject, main verb.", "Keep the tense. Only the order changes."],
            "A fronted negative pulls the helper forward. The decoys change tense but not order.",
            "Never **I have** witnessed such a peaceful poll in this constituency. (have I witnessed / I had witnessed / No substitution required / I have witness)",
            ["'Never' comes first, so the helper moves before the subject.", "Keep the present perfect.", "The order becomes 'have I witnessed'."],
            "have I witnessed"),
        pat("siv3", "Dangling modifier repair", "common",
            "The sentence begins with an -ing or being phrase, and the main subject cannot be its doer (Being a rainy day, the mela ...).",
            ["Ask who does the opener's action.", "If the main subject cannot do it, the sentence dangles.", "Pick the option that names the doer as subject or gives the opener its own subject (It being ...)."],
            "English attaches the opener to the nearest noun. The fix changes the subject or gives the opener a subject.",
            "**Being a rainy day**, the mela was cancelled by the committee. (It being a rainy day / No substitution required / Being rainy day / Been a rainy day)",
            ["The mela cannot be a rainy day.", "Give the opener its own subject: 'It'.", "'It being a rainy day, the mela was cancelled.'"],
            "It being a rainy day"),
        pat("siv4", "Parallel shape in lists and pairs", "common",
            "A list joined by and / or, or a not only ... but also pair, mixes shapes: two -ing items and one to-item, or an adjective and a clause.",
            ["Write the items in a column.", "Match every item's shape to the first.", "Pick the option that makes all items the same shape."],
            "A reader takes a list as one unit. One shape keeps the unit clean.",
            "The training module covers **typing, to file papers, and how to draft mails**. (typing, filing papers, and drafting mails / No substitution required / typing, filing papers, and to draft mails / typing, to file papers and draft mails)",
            ["The first item is 'typing', an -ing form.", "So every item must be an -ing form.", "That gives 'typing, filing papers, and drafting mails'."],
            "typing, filing papers, and drafting mails"),
        pat("siv5", "Order inside a reported question", "common",
            "The sentence reports a question (asked, wanted to know), and the bold part still has question order.",
            ["Spot the reporting verb and the wh-word.", "Put the subject before the helper.", "Keep the tense backshifted and use no 'that'."],
            "A reported question is a statement. It takes statement order.",
            "The officer asked the clerk **where was the file kept**. (where the file was kept / No substitution required / where is the file kept / that where the file was kept)",
            ["A reported question takes statement order.", "The subject 'the file' comes before 'was'.", "'That where' has two connectives."],
            "where the file was kept"),
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
