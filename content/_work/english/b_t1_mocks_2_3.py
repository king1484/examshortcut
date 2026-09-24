"""Build t1-mock-2--english.json and t1-mock-3--english.json (25 Qs each).

Layout mirrors t1-mock-1: cloze 5 (Q1-5) + 15 singles (Q6-20) + RC 5 (Q21-25).
mock-2 = CGL 2025 Tier 1 difficulty (7 easy / 13 medium / 5 hard)
mock-3 = tougher final-week set      (4 easy / 13 medium / 8 hard)

Authoring convention: for every question NOT listed in `fixed`, the correct option is
written FIRST (index 0); `place_answers()` then rotates options so that correct answers
spread evenly over A/B/C/D. Error-spotting (options mirror parts a-d) and sentence
improvement ('No improvement' stays last) are authored with their real answer index
and kept as they are.

Run:  python b_t1_mocks_2_3.py
"""
import os
import random
import re
from collections import Counter

from common import q, check_question, check_groups, _dump, ENGLISH_IDS, MOCK_DIR


def make_group_q(prefix, group, passage, subtopic):
    def f(n, idx, text, options, answer, solution, shortcut=None, difficulty="medium", tsec=40, pattern=None):
        kw = {"group": group}
        if idx == 0:
            kw["passage"] = passage
        return q(f"{prefix}-{n}", text, options, answer, solution, shortcut, difficulty,
                 subtopic, pattern or f"{subtopic}-{n}", tsec, **kw)
    return f


# =========================================================================
# MOCK 2 — CGL 2025 Tier 1 level
# =========================================================================
P2 = "q-t1-mock-2-english"

M2_CLOZE = """A town's public library is often the last place where anyone may sit for hours without being (1) ___ to buy something. Students preparing for competitive examinations crowd its reading rooms because their homes are too small and too noisy for serious study. Yet in many districts these libraries are (2) ___ for want of funds: roofs leak, newspapers arrive late, and the shelves hold books that no one has asked for in decades. Reviving them would not be (3) ___. A modest budget for new titles, reliable electricity and longer opening hours would (4) ___ transform them. A library that stays open until late evening serves the young clerk who can study only after work, and it (5) ___ the town something no shopping mall can: a quiet public room that belongs to everyone."""

_c2 = make_group_q(P2, "m2-cloze", M2_CLOZE, "cloze-test")


def c2(n, options, solution, shortcut=None, difficulty="medium"):
    return _c2(n, n - 1, f"Select the most appropriate option to fill in blank number ({n}).",
               options, 0, solution, shortcut, difficulty, 40, f"cloze-blank-{n}")


M2 = [
    c2(1, ["expected", "forbidden", "prevented", "excused"],
       "The library is contrasted with shops and malls, where a visitor is **expected** to buy. 'Forbidden to buy' and 'excused to buy' make no sense here, and 'prevent' takes 'from', not 'to'.",
       "Library vs mall contrast: nobody expects you to spend.", "easy"),
    c2(2, ["languishing", "flourishing", "multiplying", "competing"],
       "'For want of funds' and the list that follows (leaking roofs, late newspapers, stale shelves) describe decline — the libraries are **languishing** (weakening from neglect). Flourishing and multiplying are the reverse; competing has no support in the passage.",
       "Colon test: the list after the colon describes the blank — decay.", "medium"),
    c2(3, ["expensive", "necessary", "possible", "useful"],
       "The next sentence speaks of a **modest budget**, so the writer is saying revival would not be **expensive**. 'Not necessary', 'not possible' and 'not useful' all contradict the writer, who clearly wants the libraries revived.",
       "The sentence after the blank ('modest budget') defines it.", "easy"),
    c2(4, ["substantially", "scarcely", "rarely", "reluctantly"],
       "The writer argues that small spending would make a big difference, so the measures would **substantially** transform the libraries. Scarcely and rarely would reverse the argument; 'reluctantly' gives feelings to a budget, which makes no sense.",
       "Positive argument → positive-degree adverb; scarcely/rarely are negative words.", "medium"),
    c2(5, ["offers", "denies", "charges", "borrows"],
       "The library **offers** the town what no mall can (offer): a free, quiet public room. 'Denies' reverses the praise; 'charges the town something' is about payment; 'borrows' makes the library take instead of give.",
       "The colon shows the good thing the library gives → offers.", "medium"),

    q(f"{P2}-6", "Select the most appropriate synonym of the given word.\n\nCANDID",
      ["frank", "secretive", "sweet", "cautious"], 0,
      "Candid means open and honest in speech — **frank**. Secretive is the opposite; 'sweet' is a sound trap (candy); cautious describes guarded speech, the reverse of candid.",
      "candid = can't hide: a candid remark / candid photo (unposed, natural).", "easy", "synonyms-antonyms", "synonym", 25),
    q(f"{P2}-7", "Select the most appropriate antonym of the given word.\n\nEPHEMERAL",
      ["permanent", "transient", "fleeting", "delicate"], 0,
      "Ephemeral means lasting a very short time; its opposite is **permanent**. Transient and fleeting are synonyms (the classic trap), and delicate describes fragility, not duration.",
      "Two options mean the same as the word? Both are synonyms — strike them and pick the opposite.", "hard", "synonyms-antonyms", "antonym", 30),
    q(f"{P2}-8", "Select the most appropriate meaning of the given idiom.\n\nTo cry over spilt milk",
      ["to regret something that cannot be undone", "to waste milk carelessly", "to weep loudly in public", "to complain about poor food"], 0,
      "Once milk is spilt it cannot be put back, so crying over it is useless: the idiom means **to regret what cannot be undone**. The other three are literal readings of the words.",
      "Idioms are never literal — cancel every option that talks about real milk or tears.", "easy", "idioms-phrases", "idiom-meaning", 25),
    q(f"{P2}-9", "Select the correctly spelt word.",
      ["Accommodate", "Accomodate", "Acommodate", "Accommodete"], 0,
      "**Accommodate** has double c AND double m: ac-com-mo-date. Accomodate drops an m, Acommodate drops a c, and Accommodete changes the ending.",
      "It is big enough to accommodate two c's and two m's.", "medium", "spelling", "spelling", 25),
    q(f"{P2}-10", "Select the correctly spelt word.",
      ["Conscientious", "Conscientous", "Consciencious", "Concientious"], 0,
      "**Conscientious** = conscience + -tious: con-sci-en-tious. Conscientous drops the i before -ous, Consciencious uses c for t, and Concientious loses the s of 'sci'.",
      "Build it from science: con + SCIEN + tious.", "hard", "spelling", "spelling", 30),
    q(f"{P2}-11", "Select the most appropriate one word for the given expression.\n\nHandwriting that cannot be read",
      ["Illegible", "Ineligible", "Illiterate", "Invisible"], 0,
      "**Illegible** (il + legible, from Latin *legere*, to read) means impossible to read. Ineligible means not qualified; illiterate describes a person who cannot read; invisible means cannot be seen.",
      "legible → read (as in 'lecture'); eligible → choose. Don't mix them.", "medium", "one-word-substitution", "ows", 25),
    q(f"{P2}-12", "Select the most appropriate option to fill in the blank.\n\nHe has been living in this city ___ 2015.",
      ["since", "for", "from", "by"], 0,
      "A perfect-continuous tense with a **point** of time takes **since**: since 2015. 'For' is used with a period (for ten years); 'from' needs a 'to/till'; 'by' marks a deadline.",
      "Point of time → since; period of time → for.", "easy", "fill-in-the-blanks", "preposition-since-for", 20),
    q(f"{P2}-13", "Select the most appropriate option to fill in the blank.\n\nDespite repeated failures, she remained ___ and kept working towards her goal.",
      ["undeterred", "uninterested", "unprepared", "undecided"], 0,
      "'Despite failures ... kept working' needs a word meaning **not discouraged** — undeterred. Uninterested and undecided clash with 'kept working towards her goal'; unprepared has nothing to do with failures.",
      "'Despite' + 'kept working' → a word for not giving up.", "medium", "fill-in-the-blanks", "fill-blank-vocab", 25),
    q(f"{P2}-14", "Select the part of the sentence that has an error.\n\nEach of the students (a) have submitted (b) the assignment on time (c) No error (d)",
      ["Each of the students", "have submitted", "the assignment on time", "No error"], 1,
      "The subject is **each**, which is singular; 'of the students' only describes it. So the verb must be singular: 'Each of the students **has** submitted...'.",
      "Each / every / either / neither + of + plural → singular verb.", "medium", "error-spotting", "error-spot-sva", 30),
    q(f"{P2}-15", "Select the part of the sentence that has an error.\n\nBeing a rainy day, (a) the school was closed (b) earlier than usual (c) No error (d)",
      ["Being a rainy day,", "the school was closed", "earlier than usual", "No error"], 0,
      "As written, 'Being a rainy day' seems to describe 'the school', which is illogical — a school is not a rainy day. An impersonal subject is needed: '**It being** a rainy day, the school was closed...'. The error is in part (a).",
      "Participle phrase must describe the next subject; if it can't, add 'It'.", "hard", "error-spotting", "error-spot-participle", 35),
    q(f"{P2}-16", "Select the most appropriate option to replace the bold part of the sentence.\n\nNo sooner did the bell ring **when the students rushed out**.",
      ["then the students rushed out", "as the students rushed out", "than the students rushed out", "No improvement"], 2,
      "'No sooner' is always paired with **than**: 'No sooner did the bell ring than the students rushed out.' 'When' belongs with hardly/scarcely; 'then' and 'as' cannot complete the comparison.",
      "No sooner → than; Hardly/Scarcely → when.", "medium", "sentence-improvement", "improvement-correlative", 30),
    q(f"{P2}-17", "Select the option that expresses the given sentence in passive voice.\n\nWho wrote this letter?",
      ["By whom was this letter written?", "By whom this letter was written?", "By whom has this letter been written?", "By whom is this letter written?"], 0,
      "In the passive, 'who' becomes **by whom**, and the question keeps the helping verb before the subject: By whom **was** this letter written? B misses the question order; C changes the tense to present perfect; D changes it to simple present.",
      "who → by whom; past simple → was/were + V3; keep question word order.", "hard", "active-passive", "interrogative-passive", 35),
    q(f"{P2}-18", "Select the option that expresses the given sentence in indirect speech.\n\nThe teacher said to the students, \"Do not make a noise.\"",
      ["The teacher told the students not to make a noise.", "The teacher told the students that do not make a noise.", "The teacher said the students not to make a noise.", "The teacher told to the students not to make a noise."], 0,
      "A negative command becomes **told/ordered + object + not to + V1**. B keeps the imperative after 'that'; C uses 'said' with a direct object; D wrongly puts 'to' after told.",
      "Negative imperative → not to + V1; 'said to' → told (no 'to').", "easy", "direct-indirect", "imperative-narration", 30),
    q(f"{P2}-19", "Choose the correct order of the parts to make a meaningful passage.\n\n**1.** Ravi opened a savings account with his first salary. **P:** Within two years the small deposits had grown into a useful sum. **Q:** He decided to put aside a fixed amount every month. **R:** When his mother fell ill, he paid for her treatment without borrowing. **S:** Some months it was hard, but he never missed a deposit. **6.** Thrift, he realised, is a form of freedom.",
      ["QSPR", "SQPR", "QPSR", "PQSR"], 0,
      "**Q** (the decision to save) follows the account opening → **S** (the effort month after month) → **P** (the result after two years) → **R** (the pay-off when his mother fell ill) → S6's lesson. S cannot come first because 'it' in S needs the saving plan from Q.",
      "Plan → effort → result → pay-off.", "medium", "sentence-rearrangement", "rearrangement", 50),
    q(f"{P2}-20", "Select the most appropriate option to fill in the blank.\n\nIf you had left home on time, you ___ the train yesterday.",
      ["would have caught", "would catch", "will catch", "had caught"], 0,
      "'If + had + V3' is the third conditional (an unreal past), so the main clause takes **would have + V3**. 'Yesterday' rules out would catch / will catch, and 'had caught' cannot be the result clause.",
      "had + V3 ↔ would have + V3.", "medium", "grammar-essentials", "conditional", 25),
]

M2_RC = """A generation ago, a broken radio went to the neighbourhood repairman, who opened it, found the faulty part and charged a small fee. Today a phone with a cracked screen or a tired battery is more likely to be thrown into a drawer and replaced. The change is not an accident of consumer taste. Many manufacturers glue batteries in place, use screws that ordinary tools cannot turn, and refuse to sell spare parts or repair manuals to independent shops. Some even link each part to the device's serial number through software, so that a genuine replacement screen fitted by an outsider triggers warnings or stops working altogether.

Companies defend these practices on grounds of safety and quality. A poorly fitted battery, they argue, can overheat, and an untrained technician can damage waterproof seals. There is some truth in this, but critics point out that the same companies earn handsomely from authorised repairs priced close to the cost of a new device. When repair costs nearly as much as replacement, most buyers choose replacement, and the discarded devices add to a mountain of electronic waste that grows every year.

The 'right to repair' movement asks for something modest: that owners and independent repairers be able to buy parts, tools and manuals at fair prices. Several governments have begun to listen, requiring manufacturers to supply spare parts for a fixed number of years. Such rules will not end the throwaway habit on their own, but they restore an old idea that had begun to seem quaint — that a thing you have paid for is truly yours to mend."""

_r2 = make_group_q(P2, "m2-rc", M2_RC, "reading-comprehension")


def r2(n, text, options, solution, shortcut, difficulty, tsec=45):
    return _r2(n, n - 21, text, options, 0, solution, shortcut, difficulty, tsec, f"rc-{n}")


M2 += [
    r2(21, "What is the central idea of the passage?",
       ["Manufacturers' design and pricing choices discourage repair, and fair access to parts and manuals can help reverse this.",
        "Electronic devices are too dangerous to be repaired by anyone other than the manufacturer.",
        "Consumers today simply prefer new gadgets to repaired ones.",
        "Neighbourhood repairmen should be trained by phone companies."],
       "Paragraph 1 blames design choices, paragraph 2 blames repair pricing, and paragraph 3 offers the fix (fair access to parts, tools and manuals). B turns the companies' partial excuse into the thesis; C is directly denied ('not an accident of consumer taste'); D is never proposed.",
       "Thesis = problem (paras 1-2) + remedy (para 3).", "medium", 50),
    r2(22, "According to the passage, some manufacturers link each part to the device's serial number so that —",
       ["a genuine replacement part fitted by an outsider may trigger warnings or stop working",
        "stolen phones can be traced by the police",
        "customers receive faster authorised service",
        "spare parts become cheaper for independent shops"],
       "The passage says the link means 'a genuine replacement screen fitted by an outsider triggers warnings or stops working altogether'. The other options are never mentioned.",
       "Detail question: find 'serial number' and read the 'so that' clause.", "easy", 40),
    r2(23, "Why, according to the passage, do most buyers choose replacement over repair?",
       ["Because authorised repair often costs nearly as much as a new device",
        "Because new devices are safer than repaired ones",
        "Because independent shops refuse to repair phones",
        "Because governments encourage the purchase of new devices"],
       "'When repair costs nearly as much as replacement, most buyers choose replacement.' B repeats the companies' argument, not buyers' reasoning; C reverses the facts (companies refuse to supply the shops); D contradicts paragraph 3.",
       "Match the cause–effect sentence: repair ≈ new price → replace.", "medium", 45),
    r2(24, "The word 'quaint', as used in the passage, most nearly means —",
       ["charmingly old-fashioned", "dangerous", "expensive", "illegal"],
       "The idea that you may mend what you own had begun to seem **old-fashioned** — something from 'a generation ago'. Quaint means attractively unusual or old-fashioned; it carries no sense of danger, cost or illegality.",
       "Link the word to the passage's time contrast: 'a generation ago' vs 'today'.", "medium", 40),
    r2(25, "How does the author treat the companies' safety argument?",
       ["As partly valid but not the whole story",
        "As completely convincing",
        "As entirely baseless",
        "As irrelevant to the question of repair"],
       "'There is some truth in this, **but** critics point out...' — the author grants the argument some weight and then shows the profit motive behind it. B ignores the 'but'; C ignores 'some truth'; D is wrong because the argument is about repair itself.",
       "'Some truth ... but' = partial agreement: choose the balanced option.", "hard", 50),
]


# =========================================================================
# MOCK 3 — tougher final-week set
# =========================================================================
P3 = "q-t1-mock-3-english"

M3_CLOZE = """Few inventions have spread rumour as (1) ___ as the forwarded message. A claim that once travelled by word of mouth, losing force at each retelling, now reaches thousands in minutes, often stripped of its source and (2) ___ with an urgent plea to 'share before it is deleted'. The trouble is not that people are foolish; it is that checking takes effort while forwarding takes a single tap. Researchers have found that a brief pause — even a prompt asking readers whether a headline is accurate — (3) ___ the sharing of false stories noticeably. Such nudges do not (4) ___ anyone's freedom to speak; they simply restore the moment of reflection that speed has erased. A society that learns to hesitate before it forwards will find that truth, which walks, has a fair chance of (5) ___ with lies, which run."""

_c3 = make_group_q(P3, "m3-cloze", M3_CLOZE, "cloze-test")


def c3(n, options, solution, shortcut=None, difficulty="medium"):
    return _c3(n, n - 1, f"Select the most appropriate option to fill in blank number ({n}).",
               options, 0, solution, shortcut, difficulty, 40, f"cloze-blank-{n}")


M3 = [
    c3(1, ["effectively", "effective", "effectiveness", "effected"],
       "The blank describes the verb 'spread' in an 'as ___ as' comparison, so an **adverb** is needed: spread rumour as effectively as. Effective is an adjective, effectiveness a noun and effected a verb form.",
       "Blank modifies a verb → -ly adverb.", "easy"),
    c3(2, ["tagged", "robbed", "deprived", "emptied"],
       "The message loses its source but gains an urgent plea: it is **tagged with** the plea. Robbed, deprived and emptied take 'of' and describe losing something, which does not fit 'with an urgent plea'.",
       "Preposition check: ___ with → tagged; robbed/deprived/emptied → of.", "medium"),
    c3(3, ["curbs", "curb", "curbing", "to curb"],
       "Ignore the part between the dashes: the subject is 'a brief pause' (singular), and the that-clause needs a finite present verb → **curbs**. 'Curb' would need a plural subject; 'curbing' and 'to curb' are not finite verbs.",
       "Remove the dash-interrupter, then match verb to subject.", "hard"),
    c3(4, ["curtail", "enhance", "express", "celebrate"],
       "The writer is answering a possible objection — that nudges limit free speech — so the verb means limit: nudges do not **curtail** freedom. 'Enhance' and 'celebrate' are not objections anyone would answer; 'express a freedom' is meaningless.",
       "'do not ___; they simply ___' — the first blank is the complaint being denied.", "medium"),
    c3(5, ["keeping pace", "keeping quiet", "keeping company", "keeping faith"],
       "Truth 'walks' and lies 'run', so the real question is whether truth can **keep pace** (move at the same speed) with lies. Keeping quiet, keeping company and keeping faith do not continue the walking-running image.",
       "Follow the image: walks vs runs → speed → pace.", "hard"),

    q(f"{P3}-6", "Select the most appropriate synonym of the given word.\n\nOSTENTATIOUS",
      ["showy", "modest", "secretive", "thoughtful"], 0,
      "Ostentatious means designed to impress others with wealth or display — **showy**. Modest is its antonym; secretive and thoughtful are unrelated.",
      "ostentatious → 'ostent' = show off (think 'ostentation').", "medium", "synonyms-antonyms", "synonym", 25),
    q(f"{P3}-7", "Select the most appropriate antonym of the given word.\n\nAMELIORATE",
      ["worsen", "improve", "soothe", "tolerate"], 0,
      "Ameliorate means to make a bad situation better (from Latin *melior*, better). Its antonym is **worsen**. Improve is the synonym trap; soothe is close in sense; tolerate is unrelated.",
      "melior = better (French meilleur) → opposite = worsen.", "hard", "synonyms-antonyms", "antonym", 30),
    q(f"{P3}-8", "Select the most appropriate meaning of the given idiom.\n\nTo call a spade a spade",
      ["to speak plainly and frankly, even if it is blunt", "to work hard in the fields", "to exaggerate a small problem", "to hide the truth behind polite words"], 0,
      "Calling a tool by its real name means **speaking plainly**, without softening the truth. The last option is the opposite; the field-work option is a literal reading; exaggeration is unrelated.",
      "Naming things exactly = frank speech.", "medium", "idioms-phrases", "idiom-meaning", 25),
    q(f"{P3}-9", "Select the INCORRECTLY spelt word.",
      ["Occassion", "Acquaintance", "Guarantee", "Perseverance"], 0,
      "The correct spelling is **occasion** — double c, single s. Acquaintance (acq-), guarantee (-ua-, -ee) and perseverance (no 'r' after the second e) are all correct.",
      "occasion: two c's, one s (the reverse of 'necessary', which has one c, two s's).", "medium", "spelling", "spelling-incorrect", 30),
    q(f"{P3}-10", "Select the correctly spelt word.",
      ["Surveillance", "Survelliance", "Surveilance", "Survaillance"], 0,
      "**Surveillance** comes from French *surveiller* (sur + veiller, to watch over): s-u-r-v-e-i-l-l-a-n-c-e. Survelliance moves the i, Surveilance drops an l, Survaillance changes 'ei' to 'ai'.",
      "sur + VEIL + lance: watch over something as if through a veil.", "hard", "spelling", "spelling", 30),
    q(f"{P3}-11", "Select the most appropriate one word for the given expression.\n\nA person who is indifferent to pleasure and pain",
      ["Stoic", "Cynic", "Hedonist", "Sceptic"], 0,
      "A **stoic** bears pleasure and pain alike without showing feeling. A cynic distrusts people's motives; a hedonist lives for pleasure; a sceptic doubts accepted beliefs.",
      "Stoic = steady; hedonist = pleasure-seeker (opposites of each other).", "medium", "one-word-substitution", "ows", 25),
    q(f"{P3}-12", "Select the most appropriate option to fill in the blank.\n\nThe minister's speech was so ___ that even his critics were persuaded.",
      ["eloquent", "verbose", "taciturn", "incoherent"], 0,
      "A speech that persuades even critics is **eloquent** (fluent and moving). Verbose means using too many words; taciturn means saying very little; incoherent means confused — none of these would persuade critics.",
      "Result clause ('even critics were persuaded') decides the tone: positive.", "medium", "fill-in-the-blanks", "fill-blank-vocab", 25),
    q(f"{P3}-13", "Select the most appropriate option to fill in the blank.\n\nThe old building was pulled ___ to make way for a metro station.",
      ["down", "off", "out", "over"], 0,
      "**Pull down** = demolish, which is what clearing space for a station needs. Pull off = achieve something difficult; pull out = withdraw; pull over = stop a vehicle at the roadside.",
      "Buildings are pulled down; plans are pulled off.", "easy", "fill-in-the-blanks", "phrasal-verb", 20),
    q(f"{P3}-14", "Select the part of the sentence that has an error.\n\nUnless you do not work hard, (a) you will not (b) pass the examination (c) No error (d)",
      ["Unless you do not work hard,", "you will not", "pass the examination", "No error"], 0,
      "'Unless' already means 'if not', so adding 'do not' creates a double negative. Correct: '**Unless you work hard**, you will not pass the examination.'",
      "Unless / until / lest never take another 'not'.", "medium", "error-spotting", "error-spot-conjunction", 30),
    q(f"{P3}-15", "Select the part of the sentence that has an error.\n\nHe is one of those leaders (a) who has never (b) broken a promise (c) No error (d)",
      ["He is one of those leaders", "who has never", "broken a promise", "No error"], 1,
      "The relative pronoun 'who' refers to 'leaders' (plural), not to 'one', so the verb must be plural: 'one of those leaders who **have** never broken a promise.'",
      "one of those + plural noun + who → plural verb.", "hard", "error-spotting", "error-spot-sva", 35),
    q(f"{P3}-16", "Select the most appropriate option to replace the bold part of the sentence.\n\nI would rather die **than to beg for mercy**.",
      ["than begging for mercy", "than beg for mercy", "but to beg for mercy", "No improvement"], 1,
      "'Would rather' is followed by the bare infinitive on **both** sides: would rather die than **beg**. 'To beg' and 'begging' break the parallel, and 'but' cannot replace 'than' in this comparison.",
      "would rather / had better → V1 (no 'to').", "medium", "sentence-improvement", "improvement-would-rather", 30),
    q(f"{P3}-17", "Select the option that expresses the given sentence in passive voice.\n\nSomebody must have stolen my purse.",
      ["My purse must have been stolen.", "My purse must had been stolen.", "My purse must have stolen.", "My purse must be stolen."], 0,
      "Modal + have + V3 becomes **modal + have been + V3** in the passive; an indefinite agent (somebody) is dropped. 'Must had' is wrong after a modal, 'must have stolen' is active, and 'must be stolen' changes the time.",
      "must have + V3 → must have been + V3; drop 'by somebody'.", "medium", "active-passive", "modal-perfect-passive", 35),
    q(f"{P3}-18", "Select the option that expresses the given sentence in indirect speech.\n\nHe said, \"Alas! I have lost my wallet.\"",
      ["He exclaimed with sorrow that he had lost his wallet.", "He exclaimed with sorrow that he has lost his wallet.", "He said alas that he had lost his wallet.", "He exclaimed with sorrow that I had lost my wallet."], 0,
      "'Alas' is replaced by **exclaimed with sorrow**; present perfect goes back to past perfect (had lost); I/my become he/his. B misses the backshift; C keeps the interjection; D does not change the pronouns.",
      "Interjection → 'exclaimed with joy/sorrow' + tense backshift.", "medium", "direct-indirect", "exclamatory-narration", 35),
    q(f"{P3}-19", "Rearrange the following sentences to form a coherent paragraph.\n\n**A.** Within a decade, the terraces were green again and the village wells held water through the summer.\n**B.** The villagers of a drought-hit hamlet once decided to stop waiting for rain and start catching it.\n**C.** The success drew visitors from neighbouring districts, who went home to dig trenches of their own.\n**D.** They dug contour trenches across the bare hillside and planted grass to hold the soil.",
      ["BDAC", "BADC", "DBAC", "BDCA"], 0,
      "**B** introduces the villagers and their decision; **D** ('They dug...') is the action; **A** is the result a decade later; **C** ('The success...') refers back to that result. D cannot open because 'They' has no referent, and C cannot come before A because the success has not yet happened.",
      "Opener has no pronoun (B); 'They' → D; 'The success' needs A before it.", "hard", "sentence-rearrangement", "para-jumble", 50),
    q(f"{P3}-20", "Select the most appropriate option to fill in the blank.\n\nLet's go for a walk, ___?",
      ["shall we", "won't we", "don't we", "shan't we"], 0,
      "A sentence beginning with **Let's** (a suggestion that includes the speaker) always takes the tag **shall we?** The other tags are ordinary auxiliary tags and do not follow 'Let's'.",
      "Let's → shall we?", "easy", "grammar-essentials", "question-tag", 20),
]

M3_RC = """Every translator knows the old Italian jibe that the translator is a traitor. The charge is unfair, but it contains a truth that readers rarely consider: no sentence survives the passage from one language to another unchanged. Words carry histories, sounds and associations that have no exact equivalents elsewhere. A Hindi speaker who calls a friend 'yaar' conveys an ease that 'friend' only approximates, and a pun that delights in one tongue may fall flat, or even offend, in another.

The translator must therefore choose, again and again, what to preserve and what to sacrifice. Some aim at fidelity to the letter, keeping the original's structure even when it sounds stiff; others aim at fidelity to the effect, rewriting freely so that the new reader laughs where the old reader laughed. Neither approach is simply right. A literal rendering of a legal contract is a virtue; a literal rendering of a comic poem may be a small crime.

What makes the work remarkable is that the best translators remain nearly invisible. When a translated novel reads as though it had been written in our own language, we praise the author and forget the person who made the book possible. Perhaps that is the final paradox of the craft: its highest success is to be overlooked, and the traitor's truest loyalty is shown in a thousand decisions that no reader ever notices."""

_r3 = make_group_q(P3, "m3-rc", M3_RC, "reading-comprehension")


def r3(n, text, options, solution, shortcut, difficulty, tsec=50):
    return _r3(n, n - 21, text, options, 0, solution, shortcut, difficulty, tsec, f"rc-{n}")


M3 += [
    r3(21, "Which of the following best expresses the central idea of the passage?",
       ["Translation always involves choosing what to keep and what to lose, and good translators succeed by making those choices go unnoticed.",
        "Translators are traitors who distort the works they translate.",
        "A literal translation is always better than a free one.",
        "Humour can never be translated from one language into another."],
       "The passage moves from 'nothing survives unchanged' to 'the translator must choose' to 'the best translators are invisible'. B is the jibe the author calls unfair; C is denied ('Neither approach is simply right'); D overstates 'may fall flat'.",
       "Reject the option that repeats a view the author rejects (the jibe).", "medium", 50),
    r3(22, "According to the passage, a literal rendering is a virtue in the case of —",
       ["a legal contract", "a comic poem", "a translated novel", "an everyday conversation in Hindi"],
       "'A literal rendering of a legal contract is a virtue; a literal rendering of a comic poem may be a small crime.' The other options come from other parts of the passage but are not called virtues of literal translation.",
       "Locate 'virtue' and read the noun it is attached to.", "easy", 40),
    r3(23, "The example of the word 'yaar' is used to show that —",
       ["some words carry shades of meaning that have no exact equivalent in another language",
        "Hindi is a richer language than English",
        "friendship is valued more in India than elsewhere",
        "translators should avoid informal words"],
       "The example comes right after 'Words carry histories, sounds and associations that have no exact equivalents elsewhere' — 'friend' only **approximates** 'yaar'. The passage makes no claim that one language is richer, and makes no cultural or stylistic ruling.",
       "An example proves the sentence just before it.", "medium", 45),
    r3(24, "The phrase 'a small crime' suggests that a literal translation of a comic poem —",
       ["would destroy the humour the poem was meant to create",
        "is punishable under copyright law",
        "would make the poem too long",
        "is impossible to attempt"],
       "The phrase is figurative. Comedy depends on effect ('the new reader laughs where the old reader laughed'), so a word-for-word version kills the joke — that is the 'crime'. There is no legal sense, length is never discussed, and 'impossible' is contradicted by the idea of 'may be'.",
       "Figurative phrase → read it through the contrast (contract = letter, poem = effect).", "hard", 50),
    r3(25, "What is the 'final paradox' that the author refers to?",
       ["A translator's greatest success lies in not being noticed.",
        "Translators are praised more than the authors they translate.",
        "The most accurate translations are always the least readable.",
        "A translator must be disloyal to both languages at once."],
       "The next words explain it: 'its highest success is to be overlooked' — the better the translator, the less anyone notices. B reverses the passage ('we praise the author and forget the person'); C and D are not stated.",
       "A 'paradox' is usually explained right after the colon — read it back.", "hard", 50),
]


# =========================================================================
# Balancing + writing
# =========================================================================
FIXED_SUBTOPICS = {"error-spotting", "sentence-improvement"}


def place_answers(qs, seed_base):
    """Rotate options of non-fixed questions so answers spread ~evenly with no run > 2."""
    fixed = [x for x in qs if x["subtopic"] in FIXED_SUBTOPICS]
    free = [x for x in qs if x["subtopic"] not in FIXED_SUBTOPICS]
    for x in free:
        assert x["answer"] == 0, f"{x['id']}: authoring convention is correct-option-first"
    have = Counter(x["answer"] for x in fixed)
    n = len(qs)
    quota = [n // 4] * 4
    for i in range(n % 4):
        quota[i] += 1
    for seed in range(seed_base, seed_base + 5000):
        rng = random.Random(seed)
        order = [0, 1, 2, 3]
        rng.shuffle(order)
        need = []
        for rank, pos in enumerate(order):
            need += [pos] * max(0, quota[rank] - have[pos])
        need = need[:len(free)]
        while len(need) < len(free):
            need.append(rng.randrange(4))
        rng.shuffle(need)
        tgt = dict(zip([x["id"] for x in free], need))
        seq = [tgt.get(x["id"], x["answer"]) for x in qs]
        runs = max(len(list(g)) for g in _runs(seq))
        if runs <= 2:
            break
    for x in free:
        t = tgt[x["id"]]
        k = (0 - t) % 4
        opts = x["options"]
        x["options"] = opts[k:] + opts[:k]
        x["answer"] = t
        assert x["options"][t] == opts[0]
    return qs


def _runs(seq):
    out, cur = [], [seq[0]]
    for a in seq[1:]:
        if a == cur[-1]:
            cur.append(a)
        else:
            out.append(cur)
            cur = [a]
    out.append(cur)
    return out


def write(mock_id, qs, want_diff):
    assert len(qs) == 25, f"{mock_id}: {len(qs)}"
    ids = set()
    for x in qs:
        assert x["id"] not in ids, x["id"]
        ids.add(x["id"])
        assert re.fullmatch(rf"q-{mock_id}-english-\d+", x["id"]), x["id"]
        assert not re.search(r"option\s*\(?\s*[0-9]", x["solution"], re.I), x["id"]
        check_question(x, set(ENGLISH_IDS))
    groups = check_groups(qs)
    assert sorted(len(v) for v in groups.values()) == [5, 5]
    topics = Counter(x["subtopic"] for x in qs)
    expect = {"cloze-test": 5, "reading-comprehension": 5, "synonyms-antonyms": 2, "idioms-phrases": 1,
              "spelling": 2, "one-word-substitution": 1, "fill-in-the-blanks": 2, "error-spotting": 2,
              "sentence-improvement": 1, "active-passive": 1, "direct-indirect": 1,
              "sentence-rearrangement": 1, "grammar-essentials": 1}
    assert dict(topics) == expect, dict(topics)
    diff = Counter(x["difficulty"] for x in qs)
    assert (diff["easy"], diff["medium"], diff["hard"]) == want_diff, dict(diff)
    path = _dump(os.path.join(MOCK_DIR, f"{mock_id}--english.json"),
                 {"mockId": mock_id, "sectionId": "english", "questions": qs})
    ans = [x["answer"] for x in qs]
    print(f"OK {path}")
    print(f"   answers A/B/C/D = {[ans.count(i) for i in range(4)]}  seq={''.join('ABCD'[a] for a in ans)}")
    print(f"   difficulty easy/medium/hard = {diff['easy']}/{diff['medium']}/{diff['hard']}")


if __name__ == "__main__":
    write("t1-mock-2", place_answers(M2, 200), (7, 13, 5))
    write("t1-mock-3", place_answers(M3, 300), (4, 13, 8))
