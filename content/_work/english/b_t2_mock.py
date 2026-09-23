from common import q, write_mock

# =========================================================================
# MOCK 2 — Tier 2 (45 Qs: cloze 5 + RC-A 5 + RC-B 5 + 30 singles)
# =========================================================================

M2_CLOZE_PASSAGE = """People once trusted the morning paper because editors checked every claim. On social media, no editor stands between a rumour and its audience. A false story can (1) ___ across the country within hours, while the correction travels slowly, if at all. Researchers call this asymmetry the central problem of the digital age: falsehood is easy to (2) ___ and hard to undo. Regulation helps at the margins, but the stronger defence is a (3) ___ reader — one who pauses before sharing, checks the source, and notices when a headline is designed to inflame rather than (4) ___. Schools now teach such habits as 'media literacy', treating scepticism as a skill rather than a (5) ___."""

def m2_cloze(n, options, answer, solution, shortcut=None, difficulty="medium", tsec=40):
    stem = f"Select the most appropriate option to fill in blank number ({n})."
    if n == 1:
        return q(f"eng-m2-{n:02d}", stem, options, answer, solution, shortcut, difficulty,
                 "cloze-test", f"cloze-blank-{n}", 40, passage=M2_CLOZE_PASSAGE, group="m2-cloze")
    return q(f"eng-m2-{n:02d}", stem, options, answer, solution, shortcut, difficulty,
             "cloze-test", f"cloze-blank-{n}", tsec, group="m2-cloze")

M2_CLOZE = [
    m2_cloze(1, ["spread", "sleep", "sink", "shrink"], 0,
      "A false story 'can ___ across the country within hours' — movement across space: **spread**. Sleep, sink and shrink reverse or ignore the 'across' frame."),
    m2_cloze(2, ["create", "destroy", "mend", "measure"], 0,
      "The contrast is 'easy to ___ and hard to undo' — creation vs undoing: falsehood is easy to **create**. Destroy and mend belong to the undoing side; measure breaks the pair."),
    m2_cloze(3, ["cautious", "reckless", "clumsy", "noisy"], 0,
      "The reader who 'pauses before sharing, checks the source' is a **cautious** reader. Reckless is the designed opposite; clumsy and noisy do not describe checking habits."),
    m2_cloze(4, ["inform", "perform", "deform", "reform"], 0,
      "Headlines designed to inflame rather than ___ — the opposite of inflaming is **informing**. The -form family supplies the decoys; only inform fits the communication sense.",
      "-form decoy set: pick by prefix meaning, then by sense.", "medium", 40),
    m2_cloze(5, ["flaw", "feast", "festival", "favour"], 0,
      "'Scepticism as a skill rather than a ___' — the old view treats doubting as a personal **flaw**. Feast and festival are nonsense in the frame; favour reverses the meaning."),
]

M2_RC_A = """Mangroves are the quiet guardians of tropical coastlines. Growing in the mud where rivers meet the sea, they tolerate salt that would kill any ordinary plant and anchor themselves on stilted roots that grip shifting silt. Their services are out of proportion to their fame. A healthy mangrove belt absorbs the fury of storm surges, holding back waves that would otherwise flatten villages. Their tangled roots are nurseries for fish and crabs, which is why fishermen's catches rise, not fall, near mangrove forests. They also store extraordinary amounts of carbon, locking it in waterlogged soil where it can remain for centuries.

Yet the world has lost about a third of its mangroves since 1980. Shrimp farms, coastal apartments and ports have taken their place, often with government blessing, because a mangrove looks like wasted land while a shrimp pond looks like income. The accounting is dishonest. When the next cyclone arrives, the cost of lost mangroves returns as destroyed houses and ruined fisheries — expenses charged not to the developers who profited but to villagers who never signed anything.

Some countries have begun to fight back. Restoration projects in the Sundarbans and along the Vietnamese coast hire villagers to plant saplings and guard the young forests, paying them from disaster-preparedness budgets. The logic is simple: a mangrove is cheaper than a sea wall and lasts longer. Protecting coasts, it turns out, is less about concrete than about remembering what already works."""

def m2_rc_a(n, qtext, options, answer, solution, shortcut=None, difficulty="medium", tsec=50):
    if n == 6:
        return q(f"eng-m2-{n:02d}", qtext, options, answer, solution, shortcut, difficulty,
                 "reading-comprehension", f"rc-a-{n}", tsec, passage=M2_RC_A, group="m2-rc-a")
    return q(f"eng-m2-{n:02d}", qtext, options, answer, solution, shortcut, difficulty,
             "reading-comprehension", f"rc-a-{n}", tsec, group="m2-rc-a")

M2_RC_A_QS = [
    m2_rc_a(6, "What is the central idea of the passage?",
      ["Mangroves deliver irreplaceable coastal protection, and clearing them is a false economy.", "Shrimp farming should be banned in all coastal states.", "Mangroves are valuable mainly because they store carbon.", "Sea walls are cheaper and better than mangroves."], 0,
      "The passage lists protection, fisheries and carbon value, then attacks the accounting that treats mangroves as 'wasted land' and closes with 'cheaper than a sea wall' — a false-economy argument. B overreaches beyond the text; C shrinks the value to one service; D reverses the comparison.",
      "Thesis = final line: remembering what already works.", "medium", 50),
    m2_rc_a(7, "According to the passage, fishermen's catches rise near mangrove forests because —",
      ["the tangled roots serve as nurseries for fish and crabs", "fishing is banned near mangrove forests", "mangrove soil releases nutrients into boats", "fishermen prefer to camp under the trees"], 0,
      "The passage states the roots 'are nurseries for fish and crabs, which is why fishermen's catches rise.' B, C and D invent causes the passage never gives.",
      "'which is why' hands you the cause on a plate.", "easy", 45),
    m2_rc_a(8, "The author calls the accounting of mangrove land 'dishonest' because —",
      ["the costs of clearing fall on villagers who never shared the profits", "shrimp ponds earn no income at all", "villagers refuse to plant saplings", "cyclones strike only mangrove-free coasts"], 0,
      "The passage's charge: expenses of mangrove loss are 'charged not to the developers who profited but to villagers who never signed anything' — a misattribution of cost. B exaggerates; C and D contradict or invent.",
      "Follow the cost: who pays vs who profits.", "medium", 50),
    m2_rc_a(9, "The phrase 'out of proportion to their fame' suggests that mangrove services are —",
      ["greater than commonly recognised", "equal to their reputation", "smaller than assumed", "unrelated to coastal safety"], 0,
      "'Out of proportion to their fame' = their real services exceed how famous they are — **greater than commonly recognised**. The examples that follow (storm protection, nurseries, carbon) confirm the sense of under-appreciation.",
      "Idiom read: fame small, services large.", "medium", 45),
    m2_rc_a(10, "The author's attitude toward the clearing of mangroves can best be described as —",
      ["critical of the economics that justify it", "cheerfully indifferent", "openly celebratory", "mildly curious but neutral"], 0,
      "Words like 'dishonest' accounting and the closing irony ('less about concrete than about remembering what already works') mark **criticism of the economics**. Indifference, celebration and neutrality all clash with the author's explicit charges.",
      "Tone words: 'dishonest', 'never signed anything' → critical.", "medium", 45),
]

M2_RC_B = """The discovery of penicillin in 1928 promised an end to bacterial death, and for decades the promise held. Simple infections stopped killing; surgery became safer; chemotherapy and transplants became possible only because antibiotics stood guard against the infections they invite. That golden age is ending. Bacteria reproduce in hours, and every course of antibiotics kills the susceptible cells and leaves the resistant ones to multiply. The more we use these drugs, the faster resistance evolves — and we use them carelessly: for viral colds they cannot cure, in feedlots to fatten animals, and in courses patients abandon once they feel better.

The pipeline, meanwhile, is dry. A new antibiotic earns money for a fortnight before doctors lock it away as a last resort, so pharmaceutical companies have fled the field. The result is a slow-motion emergency: common procedures are regaining the risks of a century ago, and some infections now answer to no drug at all.

The remedies are unglamorous. Doctors must prescribe narrowly and briefly; hospitals must screen and isolate carriers; farmers must cut routine dosing; and patients must finish the courses they start. Above all, the economics must change: public money, not pill sales, should fund the discovery of new drugs, because a drug we hope never to use widely is still a drug we cannot live without. Resistance is not a distant threat. It is the bill arriving for eighty years of careless spending."""

def m2_rc_b(n, qtext, options, answer, solution, shortcut=None, difficulty="medium", tsec=50):
    if n == 11:
        return q(f"eng-m2-{n:02d}", qtext, options, answer, solution, shortcut, difficulty,
                 "reading-comprehension", f"rc-b-{n}", tsec, passage=M2_RC_B, group="m2-rc-b")
    return q(f"eng-m2-{n:02d}", qtext, options, answer, solution, shortcut, difficulty,
             "reading-comprehension", f"rc-b-{n}", tsec, group="m2-rc-b")

M2_RC_B_QS = [
    m2_rc_b(11, "What is the central idea of the passage?",
      ["Antibiotic resistance is a self-inflicted crisis that demands changed habits, incentives and funding.", "Penicillin was the most important discovery of the twentieth century.", "Pharmaceutical companies should sell more antibiotics to fund research.", "Viral colds can be cured by finishing antibiotic courses."], 0,
      "The passage traces resistance to careless use, a broken market and dry pipelines, then prescribes discipline plus public funding — a self-made crisis with known remedies. B is background, not the thesis; C reverses the economics argument; D contradicts the text (colds are viral).",
      "Remedy paragraph = the thesis restated in actions.", "medium", 50),
    m2_rc_b(12, "Why have pharmaceutical companies abandoned the development of new antibiotics?",
      ["New antibiotics are quickly reserved as last-resort drugs and so earn little", "Antibiotics are too expensive to manufacture", "Doctors refuse to prescribe newly launched drugs", "Bacteria no longer respond to any known compound"], 0,
      "The passage's explanation: 'A new antibiotic earns money for a fortnight before doctors lock it away as a last resort, so pharmaceutical companies have fled the field.' B, C and D are not given anywhere.",
      "'so' clause = the stated cause; quote it.", "medium", 50),
    m2_rc_b(13, "The closing metaphor 'the bill arriving for eighty years of careless spending' implies that —",
      ["decades of antibiotic misuse have created today's danger", "hospitals have overspent their budgets on medicines", "patients must pay more for antibiotics in future", "penicillin was discovered eighty years too late"], 0,
      "Careless spending = decades of overuse and misuse; the bill = resistance now confronting us. The metaphor condemns past behaviour, not hospital accounts, retail prices or the date of discovery.",
      "Map the metaphor: spending = misuse, bill = consequences.", "hard", 55),
    m2_rc_b(14, "The word 'unglamorous' as used for the remedies suggests that they are —",
      ["plain and requiring everyday discipline", "glamorous but costly", "secret and experimental", "available only in hospitals"], 0,
      "The remedies listed — prescribe briefly, screen carriers, finish courses — are ordinary acts of discipline, hence **plain, unexciting**. The word signals modesty of the measures, not glamour, secrecy or location.",
      "Un- + glamour: stripped of excitement.", "easy", 45),
    m2_rc_b(15, "Which of the following would be the most suitable title for the passage?",
      ["The Slow End of the Antibiotic Era", "The Glorious Reign of Penicillin", "How Feedlots Fatten Animals", "Viral Colds and Their Cures"], 0,
      "The passage's arc — golden age, its end, the causes, the remedies — is captured by **The Slow End of the Antibiotic Era**. B covers only the opening; C and D each echo a single line, not the argument.",
      "Title test: does it cover every paragraph's role?", "medium", 45),
]

SINGLES = [
    q("eng-m2-16", "Select the most appropriate synonym of the given word.\n\nRESILIENT",
      ["tough", "fragile", "sleepy", "costly"], 0,
      "Resilient = able to spring back, **tough**. Fragile is the antonym; sleepy and costly are unrelated.",
      "resilient → rebounds → tough.", "easy", "synonyms-antonyms", "synonym", 25),
    q("eng-m2-17", "Select the most appropriate synonym of the given word.\n\nFRUGAL",
      ["thrifty", "wasteful", "rich", "hungry"], 0,
      "Frugal = careful with money, **thrifty**. Wasteful is the antonym; rich and hungry describe other things entirely.",
      "frugal → saving → thrifty.", "easy", "synonyms-antonyms", "synonym", 25),
    q("eng-m2-18", "Select the most appropriate antonym of the given word.\n\nARID",
      ["humid", "dry", "sandy", "barren"], 0,
      "Arid = extremely dry; its antonym is **humid** (moist). Dry is a synonym; sandy and barren are companions of arid land, not opposites.",
      "arid–humid, dry–wet.", "easy", "synonyms-antonyms", "antonym", 25),
    q("eng-m2-19", "Select the most appropriate antonym of the given word.\n\nWEALTH",
      ["poverty", "riches", "property", "fortune"], 0,
      "Wealth (great riches) ↔ **poverty** (great want). Riches, property and fortune are synonyms of wealth.",
      "wealth ↔ want: poverty.", "easy", "synonyms-antonyms", "antonym", 25),
    q("eng-m2-20", "Select the correctly spelt word.",
      ["Bureaucracy", "Bureacracy", "Bureaucrasy", "Burocracy"], 0,
      "From French 'bureau' (office) + 'cracy' (rule): **bureaucracy** — bureau keeps its eau order; the ending is -cracy, not -crasy.",
      "bureau + cracy: two chunks, no merging.", "hard", "spelling", "spelling", 30),
    q("eng-m2-21", "Select the correctly spelt word.",
      ["Skeleton", "Skelaton", "Sceleton", "Skelleton"], 0,
      "The word is **skeleton** — s-k-e-l-e-t-o-n: e in both middle syllables, one l. Skelaton swaps a vowel; sceleton invents a c; skelleton doubles the l.",
      "skele-TON: no c, no double l.", "medium", "spelling", "spelling", 30),
    q("eng-m2-22", "Select the most appropriate one word for the given expression.\n\nOne who can use both hands with equal ease",
      ["Ambidextrous", "Ambiguous", "Ambivalent", "Ambulatory"], 0,
      "**Ambidextrous** = able to use both hands equally well. Ambiguous means unclear in meaning; ambivalent means having mixed feelings; ambulatory means able to walk.",
      "ambi- (both) + dextrous (right-handed skill).", "easy", "one-word-substitution", "ows", 25),
    q("eng-m2-23", "Select the most appropriate one word for the given expression.\n\nA place where bees are kept",
      ["Apiary", "Aviary", "Aquarium", "Granary"], 0,
      "Bees live in an **apiary** (Latin apis, bee). An aviary houses birds; an aquarium keeps fish; a granary stores grain.",
      "api- = bee (as in beekeeping, apiculture).", "easy", "one-word-substitution", "ows", 25),
    q("eng-m2-24", "Select the most appropriate meaning of the given idiom.\n\nA bolt from the blue",
      ["a sudden and completely unexpected shock", "a flash of lightning during a storm", "a blue-coloured missile", "a thunderclap heard at noon"], 0,
      "A bolt (lightning) from a clear blue sky = **a totally unforeseen shock**. The weather options translate the image literally instead of figuratively.",
      "Blue sky + lightning = shock out of nowhere.", "easy", "idioms-phrases", "idiom-meaning", 25),
    q("eng-m2-25", "Select the most appropriate meaning of the given idiom.\n\nTo steal a march on someone",
      ["to gain an advantage over someone secretly", "to march at night without permission", "to snatch a stick while marching", "to walk away with stolen goods"], 0,
      "From military marches: starting the march before the rival realises — **to gain a secret advantage**. No theft or night-walking is involved.",
      "March first, quietly → head start.", "medium", "idioms-phrases", "idiom-meaning", 30),
    q("eng-m2-26", "Select the most appropriate option to fill in the blank.\n\nHe has been living in Pune ___ 2010.",
      ["since", "for", "from", "by"], 0,
      "A point of time in the present perfect takes **since** (since 2010); 'for' takes a length (for ten years). 'From' needs from…to; 'by' marks a deadline.",
      "since + point, for + period.", "easy", "fill-in-the-blanks", "preposition", 25),
    q("eng-m2-27", "Select the most appropriate option to fill in the blank.\n\nShe prefers coffee ___ tea.",
      ["to", "than", "then", "at"], 0,
      "'Prefer' takes **to**: prefer coffee to tea. 'Than' belongs to comparatives; 'then' is a time word; 'at' is not a collocation.",
      "prefer X to Y — never prefer than.", "easy", "fill-in-the-blanks", "preposition", 25),
    q("eng-m2-28", "Select the most appropriate option to fill in the blank.\n\nThe child was bitten ___ a stray dog yesterday.",
      ["by", "with", "from", "of"], 0,
      "In a passive sentence the doer takes **by**: bitten by a dog. With marks the instrument (bitten with a stick would need an instrument), and from/of are impossible here.",
      "passive + doer = by.", "easy", "fill-in-the-blanks", "preposition", 25),
    q("eng-m2-29", "Select the most appropriate option to fill in the blank.\n\nEach of the players ___ given a medal after the final.",
      ["was", "were", "are", "have been"], 0,
      "'Each of + plural noun' is grammatically singular: Each **was** given. Were/are/have been all agree with 'players' — the classic trap.",
      "each, every, either, neither → singular verb.", "medium", "fill-in-the-blanks", "grammar-fit", 30),
    q("eng-m2-30", "Select the part of the sentence that has an error.\n\nThe police (a) is investigating (b) the theft reported last night (c) No error (d)",
      ["The police", "is investigating", "the theft reported last night", "No error"], 1,
      "'Police' is a plural-only noun: The police **are** investigating. The error is in part (b).",
      "police, cattle, people — always plural.", "medium", "error-spotting", "error-spot", 35),
    q("eng-m2-31", "Select the part of the sentence that has an error.\n\nHe returned back (a) from Mumbai (b) last evening (c) No error (d)",
      ["He returned back", "from Mumbai", "last evening", "No error"], 0,
      "'Returned' already contains the sense of coming back; 'returned back' is a redundancy: 'He returned from Mumbai last evening.'",
      "Redundancy watch: return back, repeat again, revert back.", "easy", "error-spotting", "error-spot", 30),
    q("eng-m2-32", "Select the option that will improve the underlined part of the sentence.\n\nMr Rao is senior than any other officer in the office.",
      ["senior to", "senior from", "more senior than", "No improvement"], 0,
      "Adjectives of Latin origin — senior, junior, superior, inferior, prior — take **to**, not 'than': senior to any other officer.",
      "senior/junior/superior/inferior + to.", "easy", "sentence-improvement", "improvement", 25),
    q("eng-m2-33", "Select the option that will improve the underlined part of the sentence.\n\nShe has been working here since five years.",
      ["for five years", "from five years", "since five year", "No improvement"], 0,
      "A period of time takes **for**: for five years. 'Since' needs a starting point (since 2019).",
      "since + point, for + duration.", "easy", "sentence-improvement", "improvement", 25),
    q("eng-m2-34", "Select the option that will improve the underlined part of the sentence.\n\nI asked him that where he was going.",
      ["I asked him where he was going", "I asked him that where was he going", "I asked him where was he going", "No improvement"], 0,
      "In reported questions, 'that' never introduces the question and the order must be statement order: asked him **where he was going**. B doubles the connective and keeps question order; C keeps question order.",
      "asked + wh-word + statement order; no 'that'.", "medium", "sentence-improvement", "improvement", 30),
    q("eng-m2-35", "Select the option that expresses the given sentence in indirect speech.\n\n\"Please wait here,\" the guard said to us.",
      ["The guard requested us to wait there.", "The guard requested us to wait here.", "The guard ordered us to waiting there.", "The guard said us to wait there."], 0,
      "Please → **requested**; here → **there** in reported speech; infinitive structure to wait. B strands 'here'; C breaks the to-infinitive; D writes the impossible 'said us'.",
      "request + object + to + V1; here → there.", "easy", "direct-indirect", "narration", 30),
    q("eng-m2-36", "Select the option that expresses the given sentence in indirect speech.\n\nRita said, \"I am learning French now.\"",
      ["Rita said that she was learning French then.", "Rita said that she is learning French now.", "Rita said that she was learning French now.", "Rita told that she was learning French then."], 0,
      "Past reporter: am → **was**, now → **then**, I → she. B skips both shifts; C shifts the tense but strands 'now'; D uses 'told' without a listener.",
      "now → then travels with the backshift.", "medium", "direct-indirect", "narration", 30),
    q("eng-m2-37", "Select the option that expresses the given sentence in direct speech.\n\nHe said that he would complete the work the next day.",
      ["He said, \"I will complete the work tomorrow.\"", "He said, \"I would complete the work tomorrow.\"", "He said, \"I will complete the work the next day.\"", "He said, \"He will complete the work tomorrow.\""], 0,
      "Reverse: would → **will**, the next day → **tomorrow**, he → **I** inside quotes. B keeps would in the quote; C leaves reported time words; D keeps the third person.",
      "would → will; the next day → tomorrow; he → I.", "medium", "direct-indirect", "narration", 35),
    q("eng-m2-38", "Select the option that expresses the given sentence in passive voice.\n\nSomeone has broken the window pane.",
      ["The window pane has been broken.", "The window pane has broken.", "The window pane was broken by someone.", "The window pane is broken by someone."], 0,
      "Present perfect → **has been + V3**; the vague agent 'someone' is dropped. B drops 'been'; C and D shift the tense to past and present.",
      "has + V3 → has been + V3; someone vanishes.", "easy", "active-passive", "active-to-passive", 30),
    q("eng-m2-39", "Select the option that expresses the given sentence in active voice.\n\nThe match was won by our team.",
      ["Our team won the match.", "Our team has won the match.", "Our team was winning the match.", "Our team had won the match."], 0,
      "'Was + V3' → simple past active: **won**. B, C and D each shift the tense (perfect, continuous, past perfect).",
      "was + V3 → V2.", "easy", "active-passive", "passive-to-active", 25),
    q("eng-m2-40", "Choose the correct order of the parts to make a meaningful sentence.\n\n**1.** The library remained silent. **P:** A boy turned pages slowly. **Q:** An old man slept in his chair. **R:** Outside, rain drummed on the windows. **S:** The librarian stamped returned books. **6.** Inside, the afternoon passed gently.",
      ["RPSQ", "RQPS", "PRQS", "RSPQ"], 0,
      "S6's 'Inside' signals a before-and-after chain: **R** opens with the outside rain (contrast set up) → then inside: **P** the boy, **S** the librarian at work, **Q** the sleeping man as the closing image before S6. RPSQ.",
      "Outside-to-inside contrast; the quietest image closes.", "medium", "sentence-rearrangement", "rearrangement", 50),
    q("eng-m2-41", "Choose the correct order of the parts to make a meaningful sentence.\n\n**1.** Bees are vanishing from our fields. **P:** Without bees, fruit yields fall sharply. **Q:** Farmers have started renting beehives. **R:** Pesticides destroy the wild plants bees feed on. **S:** Scientists blame pesticide overuse. **6.** A rented hive, after all, is a poor substitute.",
      ["SRPQ", "RSPQ", "SPRQ", "SRQP"], 0,
      "**S** names the blame → **R** explains the mechanism (pesticides kill bee-feed plants) → **P** the consequence (yields fall) → **Q** the farmers' response (renting hives) → S6's verdict on that response. SRPQ.",
      "Blame → mechanism → effect → response; response needs S6's comment.", "hard", "sentence-rearrangement", "rearrangement", 55),
    q("eng-m2-42", "Select the most appropriate option to fill in the blank.\n\nIf I ___ you, I would apologise at once.",
      ["were", "am", "had been", "be"], 0,
      "Unreal conditions about the present use the subjunctive: If I **were** you. 'Am' states a false fact; 'had been' would need 'would have apologised'; 'be' is not finite.",
      "Unreal present → were for all persons.", "medium", "grammar-essentials", "grammar-conditionals", 30),
    q("eng-m2-43", "Select the most appropriate option to fill in the blank.\n\nHardly had he reached the station ___ the train left.",
      ["when", "than", "then", "while"], 0,
      "**Hardly … when** is the fixed pair (No sooner … than is the sibling). 'Than' belongs to no sooner; then and while do not form the correlative.",
      "hardly/scarcely … when; no sooner … than.", "medium", "grammar-essentials", "grammar-connectives", 30),
    q("eng-m2-44", "Select the part of the sentence that has an error.\n\nNeither of the two players (a) were present (b) at the match (c) No error (d)",
      ["Neither of the two players", "were present", "at the match", "No error"], 1,
      "'Neither of + plural noun' takes a **singular** verb: Neither … **was** present. The plural verb agrees wrongly with 'players'.",
      "neither/either/each of + plural noun → singular verb.", "medium", "error-spotting", "error-spot", 35),
    q("eng-m2-45", "Select the most appropriate option to fill in the blank.\n\nNo sooner did the results appear ___ the website crashed.",
      ["than", "when", "then", "that"], 0,
      "**No sooner … than** is the fixed correlative (with inversion: No sooner did …). 'When' pairs with hardly; then and that form no pair.",
      "no sooner … than — memorise as a pair.", "medium", "grammar-essentials", "grammar-connectives", 30),
]

if __name__ == "__main__":
    questions = M2_CLOZE + M2_RC_A_QS + M2_RC_B_QS + SINGLES
    write_mock("t2-mock-1", questions, 45)
