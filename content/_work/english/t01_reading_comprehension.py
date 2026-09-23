from common import q, write_topic, md_table

# ---------------------------------------------------------------- passages
PASS_A = """Cities are quietly getting hotter than the countryside that surrounds them, and the gap is measured every night. On a summer evening, a village a few kilometres outside a metropolis may cool to a comfortable twenty-six degrees while the city itself still holds thirty-three. This difference, known as the urban heat island effect, arises not from global warming alone but from the way cities are built. Concrete, asphalt and brick absorb solar energy all day and release it slowly after sunset, so the city never truly cools. Fewer trees mean less shade and less of the cooling that water escaping from leaves provides. Waste heat from air conditioners, vehicles and industry adds a further burden.

The consequences fall unevenly. The poorest residents often live in dense, poorly ventilated neighbourhoods with tin roofs that turn bedrooms into ovens, and they cannot afford the electricity that cooling demands. Studies in several Indian cities have linked heat waves to falling productivity among construction and delivery workers, whose shifts rarely move to the cooler hours. Night-time heat is particularly dangerous because sleep is when the body repairs itself; hospitals report more admissions during hot nights even when the days seem tolerable.

Solutions need not wait for global action. Painting roofs white, mandating reflective materials for new construction, restoring ponds and planting street trees can lower local temperatures measurably within a single season. Ahmedabad's heat action plan, which pairs early warnings with cool-roof subsidies, has become a model studied by other developing countries. What these measures share is a simple insight: heat islands are created by design choices, and design choices can be remade. The city that planned itself into a heat trap can plan itself out of one."""

PASS_B = """The app has changed not only how we order food but what it means to have a job. Across the world, millions now earn through platforms that assign work task by task: a ride, a delivery, a design project. Companies celebrate this flexibility, and for some workers it is real — a student can drive between lectures, a parent can log off when the school day ends. Yet the same arrangement shifts nearly every risk of doing business onto the individual. The platform owns the technology, sets the price and directs the customer to the worker; the worker owns the vehicle, the fuel, the insurance and the idle hours between jobs.

Because a gig worker is classified as an independent partner rather than an employee, she generally falls outside labour laws written for factories and offices. No minimum wage applies to hours spent waiting for a request, no paid leave cushions an illness, and contributions to a pension depend entirely on what the worker chooses, or can afford, to set aside. Several countries are now experimenting with a middle category that would grant platform workers some protections without ending flexible scheduling.

Economists warn that the deeper cost may be invisible: a workforce that cannot plan a month ahead also cannot borrow, train or save with confidence. If algorithms increasingly decide who works and for how much, the question is not whether such work will disappear — it will grow — but whether the rules governing it will grow with it. Societies have rewritten labour law before, when work moved from fields to factories; the same imagination can be applied now."""

PASS_C = """There was a time when critics announced the death of the public library, confident that the internet had made buildings full of books redundant. The prediction has aged badly. Borrowing of printed books may have dipped in some cities, but library buildings are busier than they were a generation ago — because they have quietly become something more than warehouses for novels. In towns where a cup of coffee costs more than many can spare, the library remains the last indoor public space where no purchase is expected and no one asks you to leave.

Walk into any well-run city library this afternoon and you will find schoolchildren finishing homework at long tables, an unemployed man drafting job applications with a librarian's help, an elderly widow reading newspapers she cannot afford to subscribe to, and a coding club teaching teenagers in a side room. Librarians now spend as much time helping residents access government forms and digital services as they do recommending books.

This evolution has not been painless. Budgets trimmed by municipal councils force difficult choices between opening hours and new acquisitions, and smaller branches in poorer neighbourhoods — precisely those that need them most — are often the first to be marked for closure. Yet the case for investment has rarely been stronger. A society that worries about loneliness, digital exclusion and unequal schooling already owns an institution that addresses all three, staffed by professionals trained to help. The library needs not nostalgia but recognition: it is not a relic of the print age barely surviving; it is one of the few public institutions succeeding in both worlds."""

for name, p in [("A", PASS_A), ("B", PASS_B), ("C", PASS_C)]:
    n = len(p.split())
    assert 250 <= n <= 350, f"passage {name} has {n} words (need 250-350)"

# ---------------------------------------------------------------- subtopics
trap_table = md_table(
    ["Option type", "What it looks like", "How to kill it"],
    [
        ["Out of scope", "True in the real world, never said in the passage", "Ask: where is this stated? If nowhere, reject"],
        ["Too extreme", "uses *always, never, only, must, completely*", "Passages usually argue moderately; extremes overstate"],
        ["Reversal", "says the opposite of a stated line", "Re-read the line the option is built on"],
        ["Too narrow / too broad", "covers one example, or drags in ideas beyond the passage", "A title must cover the WHOLE passage, not one paragraph"],
        ["Verbatim bait", "copies a phrase but changes its use", "Word-for-word options in inference questions are usually wrong"],
    ],
)

tone_table = md_table(
    ["Tone", "Signature words", "Example signal"],
    [
        ["Neutral / informative", "states facts, figures, findings", "no praise or blame anywhere"],
        ["Critical", "flaws, fails to, merely, despite promises", "points out problems repeatedly"],
        ["Optimistic / appreciative", "promising, remarkably, has become a model", "highlights success and progress"],
        ["Sceptical / cautionary", "claimed, supposedly, yet, the deeper cost", "accepts a claim, then questions it"],
        ["Balanced / analytical", "however, on the other hand, both", "gives two sides, then weighs them"],
    ],
)

SUBTOPICS = [
    {
        "id": "rc-reading-strategy",
        "title": "How to attempt an RC passage in SSC exams",
        "concept": f"""An SSC reading-comprehension passage runs 250–350 words with 5 questions, and you get barely 6–8 minutes for the whole set. Speed comes from a fixed routine, not from reading faster in general.

**The SSC-tested routine (passage first, questions second):**
1. Read the passage once at full attention — about 2 minutes. You are reading for *structure*: what each paragraph does.
2. Read the questions (do not study all four options yet) — 30 seconds.
3. Return to the exact lines each question points to, and answer from those lines only.

Reading the passage first works better in SSC papers because questions constantly refer to "the author" and "the passage", and most details are asked in order of appearance, so one clean read lets you locate them from memory.

**Paragraph mapping.** As you finish each paragraph, tag it in three words: e.g. "para 1: cause of heat islands; para 2: who suffers; para 3: solutions". Detail answers then take seconds to find.

| Wrong habit | Why it fails | Do instead |
|---|---|---|
| Reading options before the passage | options plant false memories of "facts" | read passage first |
| Re-reading difficult sentences repeatedly | eats the clock, adds confusion | note the line number, move on, return only if a question asks |
| Answering from outside knowledge | the paper marks what is *written*, not what is true | every answer must be traceable to a line |
| Skipping the passage and matching keywords only | options paraphrase, so keywords mislead | use keywords to *reach* the line, then read the line |

**Time budget for a 5-question set:** first read ~2 min, questions ~20–30 s each, one final verification pass ~30 s. If a vocabulary-in-context question appears, do it first — it needs only its own sentence.""",
        "formulas": [],
        "tricks": [
            {
                "title": "Two-minute structure read",
                "body": "On the first read, do not hunt for facts. After each paragraph say its job in three words. Facts are cheap to re-find; structure is what saves you.",
            },
            {
                "title": "Vocab questions first, main idea last",
                "body": "Answer the replace-the-word question and line-specific details before the main-idea question — by then you will have re-touched half the passage and the theme is clear.",
                "example": {
                    "q": "A set has Q1 main idea, Q2 a detail from para 2, Q3 replace-the-word, Q4 inference, Q5 title.",
                    "solution": "Attempt order: Q3 → Q2 → Q4 → Q1 → Q5. The two theme questions answered last use the understanding built by the others.",
                },
            },
            {
                "title": "Line anchoring",
                "body": "Every detail question has a home line. Match a distinctive word in the question (a name, a number, an odd noun) to the passage, read two lines around it, and choose the option that paraphrases them.",
            },
        ],
        "mistakes": [
            "Answering from general knowledge because the option sounds true in real life.",
            "Spending four minutes on the first read to 'understand everything' — the first read only maps the passage.",
            "Leaving RC for the last two minutes; the 5-question set is the highest-value block in the section.",
            "Choosing an option because it copies words from the passage even though its meaning differs.",
        ],
    },
    {
        "id": "rc-main-idea",
        "title": "Main idea, central theme and best-title questions",
        "concept": f"""These questions ask what the passage as a whole says. The main idea is the claim the author keeps returning to; the title is that claim compressed into a phrase.

**Where the main idea lives:** in the opening paragraph (often the first or last sentence of it) and again, restated, in the closing lines. Middle paragraphs supply support — examples, data, objections — and are rarely the theme themselves.

**The whole-passage test.** A correct theme/title must:
- be *supported by every* paragraph (not just one example),
- be *covered by* the passage (not drag in outside ideas),
- be *no stronger* than what the author claims.

Run the three failure checks on every option: too narrow (one paragraph's detail), too broad (a general truth the passage never argues), too extreme (adds always/never or a stance the author does not take).

**Compression test for titles.** Summarise the passage to yourself in ten words, then pick the option closest to your summary — never start from the options.

{trap_table}

**Example of scope:** a passage that discusses heat islands in cities mainly to argue that local design fixes exist → theme = "urban heat is a local design problem with local solutions". "Global warming is heating the planet" is too broad; "white roofs reflect sunlight" is too narrow; "cities will become uninhabitable" is too extreme.""",
        "formulas": [],
        "tricks": [
            {
                "title": "First and last sentence sketch",
                "body": "Read only the opening and closing sentences of the passage, plus the first sentence of each middle paragraph. That skeleton usually states or implies the theme — build your ten-word summary from it before looking at options.",
                "example": {
                    "q": "Opening: 'Critics announced the death of the public library... The prediction has aged badly.' Closing: '...one of the few public institutions succeeding in both worlds.'",
                    "solution": "Skeleton says: libraries were written off, but they now serve wider social roles and deserve recognition → theme = libraries remain vital public institutions, not relics.",
                },
            },
            {
                "title": "Count the mentions",
                "body": "The concept the author repeats in different words across paragraphs is the theme. If an option's core idea appears in only one paragraph, it is a detail, not the theme.",
            },
            {
                "title": "Title vs theme wording",
                "body": "Titles are noun phrases ('The quiet comeback of the public library'); theme options are full claims. Do not reject a title for lacking a verb — reject it for wrong scope.",
            },
        ],
        "mistakes": [
            "Picking a title that names only the first paragraph's example.",
            "Choosing the broadest-sounding option; broadness without passage support is a trap, not a virtue.",
            "Confusing the author's concluding suggestion with the theme — a suggestion supports the idea, it is not the whole idea.",
            "Selecting an option because its words appear in the passage; theme options paraphrase, they rarely quote.",
        ],
    },
    {
        "id": "rc-detail-fact",
        "title": "Factual detail questions ('According to the passage…')",
        "concept": f"""These questions ask what the passage *says*, line by line. The answer is written in the passage — but the options paraphrase it, and the wrong options are engineered around it.

**Method: locate → read around → paraphrase-match.**
1. Pull the distinctive keyword from the question (a proper noun, a number, an unusual noun like *pensions* or *tin roofs*).
2. Find it in the passage; read the sentence before and after — the answer often sits just outside the keyword's own line.
3. State the answer to yourself in your own words, then choose the option that matches your sentence. Never compare options to the passage directly; compare them to your paraphrase.

**The three wrong options in detail questions:**
- **Not stated:** plausible, even true in the world, but the passage never says it.
- **Reversed:** right topic, opposite direction — often built by flipping one word (*most* ↔ *least*, *can* ↔ *cannot*).
- **Wrong scope:** takes a detail from a different paragraph and attaches it here.

**Comparatives, numbers and qualifiers deserve double attention.** If the passage says "night-time heat is *particularly* dangerous", an option that drops "particularly" and says heat is dangerous is weaker than the passage allows — and an option saying "day-time heat is the real danger" is reversed.

**"Which of the following is NOT true" variants:** mark each option TRUE or FALSE against a line; the odd one out is the answer. Two options will usually share one sentence, which helps you locate the region fast.""",
        "formulas": [],
        "tricks": [
            {
                "title": "Paraphrase before you look",
                "body": "After locating the line, cover the options, answer aloud in your own words, then uncover. This one habit defeats most engineered wrong options.",
                "example": {
                    "q": "'Why is night-time heat more dangerous than day heat?' (from a passage on heat islands)",
                    "solution": "Your paraphrase: body repairs itself during sleep, so hot nights harm health. Now match — any option about air conditioners or daytime labour is off-line.",
                },
            },
            {
                "title": "Reversal scan",
                "body": "Before marking a detail option, check its direction words: only/always/all, may/often/some, can/cannot. Wrong options flip these while keeping the same topic words.",
            },
            {
                "title": "Option pairing",
                "body": "When two options say the same thing in different words, both are wrong — a fact has one meaning. Kill the pair, then judge the remaining two.",
            },
        ],
        "mistakes": [
            "Stopping at the line containing the keyword; the answer may be in the following sentence.",
            "Choosing an option because it sounds authoritative ('studies show…') though the passage cites no such study.",
            "Missing 'EXCEPT/NOT' in the question stem and marking the true statement instead.",
            "Ignoring qualifiers like 'mainly', 'only', 'some' — detail questions turn on exactly these words.",
        ],
    },
    {
        "id": "rc-inference",
        "title": "Inference and extrapolation questions",
        "concept": f"""An inference is something the passage *strongly implies* without stating. The line between detail and inference: if the option can be pointed to as a sentence, it is a detail; if it is the unavoidable next step of a stated sentence, it is an inference.

**The must-be-true test.** Ask: if this option were false, would the passage contradict itself? For a valid inference, yes. If the passage could still stand with the option false, the option goes too far.

**Distance control.** The correct inference sits one small step from the text:
- passage: "she cannot afford the electricity that cooling demands" → inference: cooling appliances are of limited use to the poorest residents (small step ✔);
- "her city will ban air conditioners" (large step ✘);
- "she cannot afford electricity" verbatim (that is a detail, not an inference ✘ for inference questions).

**Outside knowledge is banned.** If an inference needs a fact you happen to know — a court ruling, a statistic — it is wrong for this exam. The passage is the only permitted world.

{trap_table}

**Author-intent variants** ("Why does the author mention Ahmedabad's plan?"): the answer is the point of the surrounding argument — here, that heat action is affordable and already working. Wrong options describe what the example *literally is* rather than what it *does*.""",
        "formulas": [],
        "tricks": [
            {
                "title": "One-step rule",
                "body": "Correct inference = stated idea + one logical step. If you need two steps, extra facts, or a change of scale (one city → all countries), reject it.",
                "example": {
                    "q": "Passage: 'A workforce that cannot plan a month ahead cannot borrow, train or save with confidence.'",
                    "solution": "One step: income insecurity itself blocks long-term commitments. Two steps: gig work will soon be banned (needs outside assumption) ✘.",
                },
            },
            {
                "title": "Verbatim is a verdict",
                "body": "In an inference question, an option that repeats passage wording without adding the step is wrong by definition. Cross it out first.",
            },
            {
                "title": "Extremity filter",
                "body": "Inferences with *only, never, must, inevitably* are almost always one step too far. Moderate options (*may, tends to, is likely*) fit the must-be-true test better.",
            },
        ],
        "mistakes": [
            "Importing real-world facts to justify an option the passage never supports.",
            "Treating a copied line as an inference (it is a detail).",
            "Inferring the author's personal life or politics from a neutral informational passage.",
            "Choosing an inference so weak it could follow from any passage — it must follow from *this* one.",
        ],
    },
    {
        "id": "rc-vocab-context",
        "title": "Vocabulary in context (replace-the-word / meaning questions)",
        "concept": f"""SSC RC asks the meaning of a word **as used in the passage** — which can differ from the word's common meaning. The question is local: only one sentence matters.

**The plug-in test (works on every such question):**
1. Read the sentence containing the word.
2. Substitute each option into that sentence.
3. Keep the sentence's meaning, grammar and tone intact — that option is the answer. Words are rarely synonymous in isolation; they are synonymous *in this sentence*.

**Guard the part of speech.** *Models* as a noun (examples to copy) and as a verb (poses as) fit different blanks. Identify the role of the word in its sentence before plugging in.

**Expect the shift.** Passage setters choose words with a double life:
- *cushions* an illness = protects against its impact (not bedroom cushions);
- *dipped* = declined briefly (not dipped into water);
- *interest* in banking = a charge; *interest* in reading = curiosity.
If one option matches the word's *dictionary* meaning and another matches the *sentence*, the sentence wins.

**Phrase-in-context variants** ("turn bedrooms into ovens", "marked for closure"): treat the phrase as one unit; its meaning is figurative or idiomatic within the passage. Literal word-by-word options are the bait.

**Antonym-in-context variants** ask which word is *opposite* to the passage word — still test the sentence, then flip the meaning once. Do not flip twice.""",
        "formulas": [],
        "tricks": [
            {
                "title": "Own-words first",
                "body": "Cover the options, replace the word with your own simple word, then find the option matching YOUR word. This kills the dictionary-meaning bait.",
                "example": {
                    "q": "'...no paid leave cushions an illness.' What does *cushions* mean here?",
                    "solution": "Own word: *softens/protects against*. Match options: 'protects from the effects of' ✔; 'provides comfort in the home' ✘ (dictionary bait).",
                },
            },
            {
                "title": "Tone match",
                "body": "The substitute must keep the sentence's attitude. In a critical sentence, choose the critical option; a neutral synonym that drains the criticism is wrong.",
            },
            {
                "title": "Two-line rule for phrases",
                "body": "For phrase-meaning questions, read one line before and after: figurative phrases get their meaning from the surrounding argument, not from the words themselves.",
            },
        ],
        "mistakes": [
            "Picking the option with the word's most common meaning although the sentence demands another sense.",
            "Changing the part of speech while plugging in (noun option in a verb slot).",
            "Choosing an opposite for an antonym question because it merely sounds negative.",
            "Reading five lines around the word; context questions need the sentence, at most the sentence plus its neighbour.",
        ],
    },
    {
        "id": "rc-tone-attitude",
        "title": "Tone, attitude and author's-opinion questions",
        "concept": f"""Tone questions ask *how* the author speaks, not *what* he says. Tone lives in adjectives, adverbs and contrasts — not in the facts themselves.

{tone_table}

**How to read for tone in one pass:** watch the author's evaluations. "has become a model studied by other countries" = approval. "merely shifts risk onto workers" = criticism. "The prediction has aged badly" = gentle mockery of critics. Underline one evaluative phrase per paragraph; the pattern across paragraphs is the tone.

**Author's-opinion questions** ("The author would agree with which of these?") obey the same rules as inference, with one addition — the opinion must match the author's *degree* of commitment. Authors of SSC passages usually take measured positions: they accept problems and propose workable fixes. Options claiming the author is desperate, euphoric, or completely dismissive of something almost never fit.

**Neutral passages exist.** Science and report-style passages carry no stance; the correct tone is *informative/neutral/analytical*, and options like *sarcastic, pessimistic, passionate* are wrong even when the topic sounds alarming. Do not confuse the seriousness of a subject with the mood of the writer.

**Attitude toward a specific thing** ("attitude of the author towards gig platforms"): collect every line touching that thing, note the verbs used with it (*celebrate, warn, can be applied now*), and summarise: the author is critical of the rules but not of flexibility itself. One-sided options (fully supportive / fully hostile) fail.""",
        "formulas": [],
        "tricks": [
            {
                "title": "Adjective audit",
                "body": "Sweep the passage for adjectives and adverbs with feeling (quietly, badly, remarkable, merely, confident). Three of them in the same direction fix the tone.",
                "example": {
                    "q": "Passage words: 'quietly getting hotter', 'turn bedrooms into ovens', 'plan itself out of one'.",
                    "solution": "Concerned but hopeful: the problem is real and the closing line offers a way out → tone = concerned/optimistic, not alarmed or dismissive.",
                },
            },
            {
                "title": "However counts double",
                "body": "The clause after *but/however/yet* carries the author's real position; the clause before it is the position being set aside. Tone and opinion questions key off the second half.",
            },
            {
                "title": "Degree matching",
                "body": "Match intensity, not just direction: 'sceptical' ≠ 'hostile', 'cautiously optimistic' ≠ 'confident'. Pick the option at the same temperature as the passage.",
            },
        ],
        "mistakes": [
            "Calling a fact-heavy passage 'sarcastic' because its subject is unpleasant.",
            "Reading the tone of people *quoted* in the passage as the author's own tone.",
            "Choosing an extreme tone word (outraged, euphoric) when the passage argues moderately.",
            "Forgetting that a 'balanced/analytical' option is often correct when the author gives both sides.",
        ],
    },
]

# ---------------------------------------------------------------- pyq patterns
PATTERNS = [
    {
        "pattern": "Central theme of the passage",
        "frequency": "very common",
        "howToSpot": "Stem says 'the main idea/central theme of the passage is' or 'the most appropriate title'.",
        "approach": "Compress the passage into ten words from its opening and closing lines, then match. Apply the scope checks: not one paragraph, not beyond the passage, not more extreme than the author.",
    },
    {
        "pattern": "Factual detail ('According to the passage')",
        "frequency": "very common",
        "howToSpot": "Stem names a fact, person, group or reason found in a specific line.",
        "approach": "Anchor the keyword, read the sentence plus its neighbours, build your own paraphrase, then match options to the paraphrase and check direction words.",
    },
    {
        "pattern": "Inference ('It can be inferred / the author implies')",
        "frequency": "common",
        "howToSpot": "Stem uses infer/imply/suggest, or asks what follows from a stated line.",
        "approach": "Take the stated idea plus exactly one logical step; reject verbatim copies, outside knowledge and extreme options using the must-be-true test.",
    },
    {
        "pattern": "Word or phrase meaning in context",
        "frequency": "common",
        "howToSpot": "Stem quotes a word/phrase from the passage and asks its meaning or a synonym/antonym 'as used in the passage'.",
        "approach": "Run the plug-in test on the containing sentence only; keep part of speech and tone; prefer your own replacement word before judging options.",
    },
    {
        "pattern": "Author's tone or opinion",
        "frequency": "occasional",
        "howToSpot": "Stem asks for the tone of the passage or which statement the author 'would agree with'.",
        "approach": "Audit evaluative adjectives and the clause after each contrast word; match degree, then pick the measured option consistent with the closing lines.",
    },
    {
        "pattern": "Why-does-the-author-mention X",
        "frequency": "occasional",
        "howToSpot": "Stem asks the purpose of an example, statistic or quotation inside the passage.",
        "approach": "Answer with the point the surrounding argument makes, not with what the example literally describes. Look one sentence above or below the example.",
    },
]

# ---------------------------------------------------------------- solved examples
SE = [
    q("eng-rc-s01",
      """Read the mini-passage and answer the question that follows.

\"Every winter the capital records its worst air of the year, and every winter officials promise action. Filters are distributed, construction is briefly halted, and once the wind changes, the promises are quietly shelved. The cleanup that would matter — cutting crop-stubble burning, electrifying bus fleets, enforcing industrial norms — is announced each year with less conviction than the last.\"

The central idea of the passage is:""",
      ["Delhi's winter pollution is an annual crisis met with fading commitment",
       "Air filters are the most effective response to winter smog",
       "Changes in wind direction cause Delhi's winter pollution",
       "Industrial units are the sole source of the capital's smog"],
      0,
      "The passage contrasts a recurring crisis with the weakening official response: promises made, token steps, real measures losing conviction. Option by option: (b) is contradicted — filters are the *token* step, not the effective one; (c) mentions wind only as the event that ends each episode, not as the cause; (d) is too extreme — stubble burning and bus fleets are named alongside industry. Only (a) covers the whole passage at the author's level of criticism.",
      "Theme = what is said in the opening line AND echoed at the close. Here 'every winter... promise' opens and 'less conviction than the last' closes — build the theme from that frame before reading options.",
      "easy", "rc-main-idea", "central theme", 40,
      passage="Every winter the capital records its worst air of the year, and every winter officials promise action. Filters are distributed, construction is briefly halted, and once the wind changes, the promises are quietly shelved. The cleanup that would matter — cutting crop-stubble burning, electrifying bus fleets, enforcing industrial norms — is announced each year with less conviction than the last.",
      group="rc-se1"),
    q("eng-rc-s02",
      """In the passage below, what does the word **tolerable** mean as used by the author?

\"Hospitals report more admissions during hot nights even when the days seem tolerable. Sleep is when the body repairs itself, and a bedroom that never cools denies it that chance.\"""",
      ["pleasant and comfortable", "barely bearable", "extremely dangerous", "shorter than usual"],
      1,
      "The contrast runs: *even when days seem tolerable*, hot nights still send people to hospital. For the contrast to work, tolerable days must be days people can just about cope with — so 'barely bearable' fits, and the sentence keeps working when you plug it in. 'Pleasant and comfortable' is too positive for the contrast ('even when days were pleasant, nights hospitalised people' implies days were pleasant, weakening the author's point about heat). 'Extremely dangerous' contradicts the contrast, and duration is not discussed.",
      "Plug each option into the sentence and keep the *even when* contrast true — only one option survives the plug-in test.",
      "medium", "rc-vocab-context", "word meaning in context", 35,
      passage="Hospitals report more admissions during hot nights even when the days seem tolerable. Sleep is when the body repairs itself, and a bedroom that never cools denies it that chance.",
      group="rc-se2"),
    q("eng-rc-s03",
      """\"Small branches in poorer neighbourhoods — precisely those that need them most — are often the first to be marked for closure.\" (from a passage on public libraries)

Which of the following can be **inferred** from this line?""",
      ["The libraries that are most needed face the greatest risk of being shut",
       "Municipal councils deliberately want to hurt poor neighbourhoods",
       "Rich neighbourhoods have no libraries at all",
       "All small library branches will eventually be closed"],
      0,
      "One step from the line: branches in poor areas are small, small branches are closed first, and those areas need libraries most → the most-needed branches face the highest closure risk (a). (b) adds intent ('deliberately want to hurt') — the passage blames budgets, not malice. (c) goes outside the line and reverses its implication. (d) converts 'often the first' into 'all... eventually', an extreme the passage never supports.",
      "Verbatim copy = detail, one logical step = inference, added intent/scale = wrong. Rank the options by their distance from the line.",
      "medium", "rc-inference", "inference", 40,
      passage="Small branches in poorer neighbourhoods — precisely those that need them most — are often the first to be marked for closure.",
      group="rc-se3"),
]

# ---------------------------------------------------------------- practice
PRACTICE = [
    # ---- Passage A: urban heat islands (5 Qs)
    q("eng-rc-p01",
      "Which of the following best states the central idea of the passage?",
      ["Cities trap heat through their own construction, but deliberate design changes can reverse it",
       "Global warming will make Indian cities uninhabitable within a few decades",
       "White-painted roofs are the only effective defence against summer heat",
       "Rural areas are warming faster than cities because of deforestation"],
      0,
      "Para 1 explains how city building materials and design create the heat island; para 2 gives its uneven consequences; para 3 argues local design measures work and ends 'can plan itself out of one'. (b) exaggerates beyond the passage and misattributes the effect mainly to global warming, which para 1 explicitly limits. (c) narrows to one solution although the passage lists several. (d) reverses the passage — cities are hotter, not villages.",
      "Theme = opening problem + closing claim. The passage frames heat as a *design* outcome and ends on remake-ability — that pair is the idea.",
      "easy", "rc-main-idea", "central theme", 45,
      passage=PASS_A, group="rc-pa"),
    q("eng-rc-p02",
      "According to the passage, why is night-time heat considered especially harmful?",
      ["Outdoor workers cannot complete their shifts at night",
       "The body carries out its repair processes during sleep",
       "Air conditioners stop working after sunset",
       "Hospitals admit only night-time patients during heat waves"],
      1,
      "The passage states: 'Night-time heat is particularly dangerous because sleep is when the body repairs itself; hospitals report more admissions during hot nights...' — (b) restates the stated reason. (a) describes a para-2 problem about *day* shifts of workers, not nights. (c) is never said — the passage says the poor cannot afford electricity. (d) distorts the point about admissions being higher, not restricted, at night.",
      "Anchor 'sleep' in para 2 and read the sentence — the answer is inside the 'because' clause.",
      "easy", "rc-detail-fact", "factual detail", 40,
      group="rc-pa"),
    q("eng-rc-p03",
      "The phrase 'turn bedrooms into ovens' in the passage conveys that the rooms:",
      ["are used for cooking at night", "become unbearably hot to sleep in",
       "have ovens installed for heating", "are well ventilated but poorly lit"],
      1,
      "The phrase is figurative: tin roofs under which the poorest residents live make bedrooms extremely hot, so hot that sleep is impossible — the oven image conveys unbearable heat. Literal readings — cooking or actual ovens in bedrooms — are the bait; ventilation/lighting is not discussed at all.",
      "Phrase-in-context = treat as one figurative unit; reject any option that reads the words literally.",
      "easy", "rc-vocab-context", "phrase meaning in context", 35,
      group="rc-pa"),
    q("eng-rc-p04",
      "It can be inferred from the passage that the author regards Ahmedabad's heat action plan as:",
      ["an expensive experiment that has largely failed",
       "proof that heat waves cannot be managed without foreign aid",
       "a practical example of local measures already working",
       "a plan designed only for government office buildings"],
      2,
      "The plan 'has become a model studied by other developing countries' and is cited to support the claim that local measures 'can lower local temperatures measurably within a single season'. The one-step inference: the author holds it up as working, practical proof. (a) contradicts the passage, (b) imports foreign aid — never mentioned, (c) ✔, (d) narrows the plan's scope, which the passage defines broadly (warnings plus roof subsidies).",
      "Author-intent: an example supports the argument around it — here 'solutions need not wait' and 'already working'.",
      "medium", "rc-inference", "inference", 45,
      group="rc-pa"),
    q("eng-rc-p05",
      "Which of the following best describes the author's overall approach in the passage?",
      ["Alarmed and fatalistic about the future of cities",
       "Informative analysis combined with guarded optimism about remedies",
       "Openly sarcastic about government inaction",
       "Strictly neutral, presenting data without any judgement"],
      1,
      "The author explains causes, documents unequal harm (concerned, informative), then presents workable measures and a model plan, closing on 'can plan itself out of one' (guarded optimism). (a) fails — the closing is hopeful, not fatalistic. (c) — the passage criticises no one and uses no mockery. (d) — the author clearly evaluates solutions, so 'strictly neutral' misreads the final paragraph.",
      "Tone = direction + degree. Problem + solvable ending ⇒ concerned-but-optimistic; the last sentence settles it.",
      "medium", "rc-tone-attitude", "author's tone", 40,
      group="rc-pa"),

    # ---- Passage B: gig economy (5 Qs)
    q("eng-rc-p06",
      "Which of the following would be the most appropriate title for the passage?",
      ["How Mobile Apps Deliver Food to Millions",
       "Gig Work: Flexibility Gained, Protection Pending",
       "The Coming Collapse of the Platform Economy",
       "Why Employees Prefer Offices Over Factories"],
      1,
      "The passage's two halves: flexibility is real (para 1) but risk and legal exclusion fall on workers (paras 1–2), and rules must catch up (para 3). (b) compresses exactly this. (a) narrows to one example from the opening sentence. (c) is contradicted — the author says such work 'will grow'. (d) is never discussed; the factory comparison is about which laws exist, not employee preferences.",
      "Title test: cover every paragraph, add nothing, no stance stronger than the author's — only (b) survives all three.",
      "medium", "rc-main-idea", "best title", 45,
      passage=PASS_B, group="rc-pb"),
    q("eng-rc-p07",
      "According to the passage, which of the following does the platform NOT provide to the gig worker?",
      ["The technology that connects worker and customer", "The price fixed for each task",
       "Insurance for the worker's vehicle", "Directions to the customer"],
      2,
      "Para 1 assigns technology, price-setting and customer direction to the platform, and lists 'the vehicle, the fuel, the insurance and the idle hours' as what the *worker* owns. Insurance therefore comes from the worker, not the platform — making (c) the correct NOT-provided item. (a), (b) and (d) are each explicitly on the platform's side of the list.",
      "NOT-questions: mark each option against the sentence's two-sided list; three options on one side leave the fourth.",
      "easy", "rc-detail-fact", "factual detail (NOT)", 40,
      group="rc-pb"),
    q("eng-rc-p08",
      "Why does the author say that labour laws currently offer gig workers little protection?",
      ["Because workers refuse to register under existing labour laws",
       "Because such laws were written for workplaces like factories and offices, and gig workers are classified as independent partners",
       "Because platforms operate outside the jurisdiction of national law",
       "Because labour laws apply only to workers in government service"],
      1,
      "Para 2 gives both halves of the reason: classification as 'an independent partner rather than an employee' and laws 'written for factories and offices'. (b) combines them accurately. (a) reverses agency — workers are not refusing; the classification excludes them. (c) invents a jurisdictional claim absent from the passage. (d) adds a government-service restriction that is never stated.",
      "Reason-questions: the answer is the sentence carrying 'because/so' — here the classification sentence. Match both halves, not one.",
      "easy", "rc-detail-fact", "factual detail (reason)", 40,
      group="rc-pb"),
    q("eng-rc-p09",
      "In the passage, 'no paid leave cushions an illness' suggests that an ill gig worker:",
      ["receives special leave reserved for illness", "gets paid compensation from the platform",
       "has no paid protection to fall back on when sick", "must train others during sick leave"],
      2,
      "The sentence lists absences: no minimum wage for waiting hours, no paid leave, pension contributions fully self-funded. *Cushions* here = softens the blow / provides a protective layer — so the sick worker has no paid buffer. (a) and (b) contradict the sentence (paid leave/compensation is exactly what is missing). (d) misreads cushion as a job duty — nothing about training appears.",
      "Own-words first: 'cushions an illness' = *protects against the money lost when sick*. Then match.",
      "medium", "rc-vocab-context", "phrase meaning in context", 35,
      group="rc-pb"),
    q("eng-rc-p10",
      "What does the author mean by describing the deeper cost of gig work as 'invisible'?",
      ["Platforms hide their profits from tax authorities",
       "The loss of financial stability undermines workers' ability to plan, borrow and save, though no ledger records it",
       "Customers do not see the workers who deliver to them",
       "The cost of running the app is unknown to investors"],
      1,
      "The sentence itself defines the term: 'a workforce that cannot plan a month ahead also cannot borrow, train or save with confidence' — a damage to financial planning that appears in no account book, hence invisible. (b) captures this. (a) and (d) move to taxes and investors, topics the passage never raises; (c) is literal 'seeing', exactly the misreading the word invites.",
      "When a passage defines its own metaphor in the next clause, the answer is inside that clause — match it, not the literal image.",
      "medium", "rc-inference", "inference", 45,
      group="rc-pb"),

    # ---- Passage C: public libraries (5 Qs)
    q("eng-rc-p11",
      "The passage is primarily concerned with:",
      ["the declining habit of reading printed books in cities",
       "how public libraries have outgrown predictions of their death by serving wider social needs",
       "the rising cost of coffee in public places",
       "the training that librarians receive in digital services"],
      1,
      "Para 1: the death prediction 'has aged badly'; para 2: libraries now serve homework, job searches, newspapers, coding clubs; para 3: budgets threaten them, yet 'the case for investment has rarely been stronger' — an institution 'succeeding in both worlds'. (b) covers all three. (a) is conceded only in passing ('borrowing... may have dipped') and is actually part of the mistaken prediction. (c) is an illustration in one clause. (d) is a detail of para 2.",
      "Count mentions: libraries' widened social role appears in every paragraph; each wrong option lives in a single clause.",
      "medium", "rc-main-idea", "central theme", 45,
      passage=PASS_C, group="rc-pc"),
    q("eng-rc-p12",
      "According to the passage, librarians these days:",
      ["spend more time enforcing silence than helping visitors",
       "help residents with official paperwork and online services as much as with books",
       "have stopped recommending books altogether",
       "are replaced by coding clubs in side rooms"],
      1,
      "Para 2 states: 'Librarians now spend as much time helping residents access government forms and digital services as they do recommending books' — (b) is a direct paraphrase. (a) invents enforcement duties. (c) flips 'as much time... as' into abandonment of books. (d) confuses the location (clubs *use* a side room) with staff replacement.",
      "Match the balance in the sentence: 'as much X as Y' means both continue — options that delete either half are wrong.",
      "easy", "rc-detail-fact", "factual detail", 35,
      group="rc-pc"),
    q("eng-rc-p13",
      "It can be inferred from the third paragraph that the closure of small branches affects:",
      ["only those who never visit libraries", "the neighbourhoods that depend on libraries the most",
       "librarians but not library users", "wealthy areas with large branches"],
      1,
      "The line says smaller branches in poorer neighbourhoods are 'precisely those that need them most' and are 'often the first to be marked for closure' — the one-step inference: closures hit the most dependent communities. (a) adds a group the passage never ranks; (c) divides staff from users without basis; (d) reverses the geography — poor, not wealthy, areas hold the small branches.",
      "Dash-enclosed phrases ('precisely those...') carry the author's strongest point — inference questions love them.",
      "medium", "rc-inference", "inference", 40,
      group="rc-pc"),
    q("eng-rc-p14",
      "In the passage, the word 'redundant' most nearly means:",
      ["outdated and no longer needed", "extremely expensive",
       "full of duplicated books", "protected by law"],
      0,
      "Critics believed the internet had made 'buildings full of books redundant' — that is, unnecessary, a thing whose job was over; the next sentence confirms the sense ('The prediction has aged badly' — the prediction of no-longer-needed). (b) cost is never linked to the word; (c) plays on 'duplicate copies', which the passage does not discuss; (d) is the opposite of what critics claimed.",
      "Antonym/synonym-in-context: plug your own word ('unnecessary') into the sentence first, then match; ignore options sharing nearby letters or images.",
      "easy", "rc-vocab-context", "word meaning in context", 30,
      group="rc-pc"),
    q("eng-rc-p15",
      "The tone of the author towards public libraries can best be described as:",
      ["dismissive", "supportive", "mocking", "indifferent"],
      1,
      "The author calls the library 'the last indoor public space where no purchase is expected', documents its social services warmly, concedes budget problems honestly, and ends by demanding 'recognition' for an institution 'quietly succeeding in both worlds' — a clearly supportive tone with measured criticism of funding choices. Dismissive, mocking and indifferent all contradict the evaluative language of the closing paragraph.",
      "Tone verdicts come from the closing lines: 'needs not nostalgia but recognition' is advocacy ⇒ supportive.",
      "easy", "rc-tone-attitude", "author's tone", 35,
      group="rc-pc"),
]

topic = {
    "id": "reading-comprehension",
    "sectionId": "english",
    "title": "Reading Comprehension",
    "order": 1,
    "importance": "high",
    "avgQuestions": {"tier1": 5, "tier2": 12},
    "summary": "One 250–350-word passage with 5 questions in Tier 1; 3 passages (12–15 questions) in Tier 2. Passages come from editorials, science reporting and social issues, and every answer is traceable to a line. RC is the highest-value block in the English section — five marks for one fixed routine.",
    "subtopics": SUBTOPICS,
    "pyqPatterns": PATTERNS,
    "solvedExamples": SE,
    "practice": PRACTICE,
}

if __name__ == "__main__":
    write_topic(topic)
