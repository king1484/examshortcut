# New practice questions for fill-in-the-blanks (Phase 2). opts[0] is the correct option (QA moves it).
from _lib import QA

B = "Select the most appropriate option to fill in the blank.\n\n"


def QS_FB():
    qs = []
    a = qs.append

    # ---------------- fb-collocations ----------------
    s = "fb-collocations"
    a(QA(f"{s}-p01", s, "fbc1", B + "The annual sports meet will ___ place in the second week of December.",
         ["take", "give", "make", "hold"],
         "Events **take place** — a fixed verb + noun chunk. 'Give place', 'make place' and 'hold place' are not used for an event happening.",
         "Event + happen = take place.", "easy", 30))
    a(QA(f"{s}-p02", s, "fbc1", B + "The new trainee ___ several mistakes in his first report but corrected them quickly.",
         ["made", "did", "took", "gave"],
         "Mistakes are **made** (or committed). 'Did mistakes' is the commonest Indian-English slip; 'took' and 'gave' do not partner mistake at all.",
         "make a mistake, never do a mistake.", "easy", 30))
    a(QA(f"{s}-p03", s, "fbc2", B + "Commuters were stuck for hours in ___ traffic on the highway.",
         ["heavy", "strong", "powerful", "weighty"],
         "Dense traffic is **heavy traffic**, the same partner as heavy rain. 'Strong', 'powerful' and 'weighty' are near-synonyms that refuse this noun.",
         "heavy rain, heavy traffic.", "easy", 30))
    a(QA(f"{s}-p04", s, "fbc2", B + "The bus driver had a ___ escape when the truck swerved into his lane.",
         ["narrow", "thin", "slim", "tight"],
         "Escaping danger by very little is a **narrow escape**. 'Thin', 'slim' and 'tight' all mean small, but none is the fixed partner of escape.",
         "Almost hurt = narrow escape.", "medium", 35))
    a(QA(f"{s}-p05", s, "fbc3", B + "Wear a jacket in the evening, or you may ___ a cold.",
         ["catch", "grab", "hold", "seize"],
         "Illness is **caught**: catch a cold, catch a fever. 'Grab', 'hold' and 'seize' are literal verbs of taking and do not form the idiom.",
         "catch a cold.", "easy", 30))
    a(QA(f"{s}-p06", s, "fbc3", B + "By the time the guests left, the children were ___ asleep on the sofa.",
         ["fast", "quick", "rapid", "swift"],
         "Deep sleep is **fast asleep** — here fast means firmly, not speedily. 'Quick', 'rapid' and 'swift' only carry the speed sense, so none partners asleep.",
         "fast asleep = sound asleep.", "medium", 35))
    a(QA(f"{s}-p07", s, "fbc4", B + "It is ___ and parcel of a journalist's job to verify every claim.",
         ["part", "piece", "bit", "section"],
         "The frozen expression is **part and parcel**, meaning an essential part. Its words cannot be swapped, so 'piece', 'bit' and 'section' break the idiom.",
         "part and parcel = essential part.", "medium", 35))
    a(QA(f"{s}-p08", s, "fbc4", B + "The defence lawyer's argument did not ___ water, and the appeal was dismissed.",
         ["hold", "keep", "retain", "bear"],
         "An argument that is sound **holds water**. The idiom is frozen: 'keep water', 'retain water' and 'bear water' describe containers, not reasoning. The dismissed appeal confirms the argument was weak.",
         "Valid argument = holds water.", "hard", 45))
    a(QA(f"{s}-p09", s, "fbc5", B + "After a long debate, the committee finally ___ a conclusion.",
         ["reached", "arrived", "came", "got"],
         "One **reaches a conclusion** directly. 'Arrived' needs at (arrived at a conclusion) and 'came' needs to (came to a conclusion); neither takes the noun straight after it. 'Got a conclusion' is not idiomatic.",
         "reach a conclusion / arrive AT / come TO.", "medium", 40))
    a(QA(f"{s}-p10", s, "fbc5", B + "The two companies ___ a deal worth several crores late last night.",
         ["struck", "beat", "knocked", "smashed"],
         "Agreements are **struck**: strike a deal, strike a balance, strike a bargain. 'Beat', 'knocked' and 'smashed' are hitting verbs used literally and do not form the business chunk.",
         "strike a deal / balance / bargain.", "hard", 40))

    # ---------------- fb-phrasal-verbs ----------------
    s = "fb-phrasal-verbs"
    a(QA(f"{s}-p01", s, "fbp1", B + "The opposition ___ the minister's resignation after the scam came to light.",
         ["called for", "called off", "called on", "called up"],
         "The sense needed is demanded: **called for** the resignation. 'Called off' means cancelled, 'called on' means visited or urged a person, and 'called up' means telephoned.",
         "call for = demand.", "easy", 30))
    a(QA(f"{s}-p02", s, "fbp1", B + "The bank decided to call ___ the loan when the borrower missed three instalments.",
         ["in", "on", "off", "up"],
         "To demand repayment of a loan is to **call it in**. 'Call off' would cancel the loan, which a bank would not do to a defaulter; 'call on' and 'call up' do not take a loan as object.",
         "call in a loan = demand it back.", "hard", 45))
    a(QA(f"{s}-p03", s, "fbp1", B + "After the inquiry, the rumour ___ to be completely false.",
         ["turned out", "turned up", "turned down", "turned over"],
         "The sense is 'proved to be': **turned out** to be false. 'Turned up' means appeared, 'turned down' means rejected, 'turned over' means handed over or flipped.",
         "turn out (to be) = prove.", "medium", 35))
    a(QA(f"{s}-p04", s, "fbp2", B + "Grandmother looks ___ the baby while the parents are at work.",
         ["after", "into", "for", "up"],
         "Caring for someone is **looking after** them. 'Look into' means investigate, 'look for' means search, 'look up' means find in a book or visit.",
         "look after = take care of.", "easy", 30))
    a(QA(f"{s}-p05", s, "fbp2", B + "Young cricketers look ___ to the captain as their role model.",
         ["up", "forward", "down", "back"],
         "To admire is to **look up to** someone, and the phrase 'as their role model' confirms admiration. 'Look forward to' means anticipate, 'look down' suggests contempt, and 'look back to' means recall the past.",
         "look up to = admire; look down on = despise.", "medium", 35))
    a(QA(f"{s}-p06", s, "fbp2", B + "They are looking forward ___ their grandparents during the vacation.",
         ["to meeting", "to meet", "for meeting", "meeting"],
         "In **look forward to**, 'to' is a preposition, so a gerund follows: **to meeting**. 'To meet' treats it as an infinitive — the classic trap. 'For meeting' uses the wrong particle, and bare 'meeting' drops the required to.",
         "look forward to + V-ing.", "hard", 40))
    a(QA(f"{s}-p07", s, "fbp3", B + "Because of the cyclone warning, the fair was put ___ till next month.",
         ["off", "up", "down", "across"],
         "Postponed = **put off**, and 'till next month' confirms a delay. 'Put up' means house or raise, 'put down' means suppress, 'put across' means communicate.",
         "put off = postpone.", "medium", 30))
    a(QA(f"{s}-p08", s, "fbp3", B + "The speaker failed to put ___ his ideas clearly to the audience.",
         ["across", "off", "up with", "in"],
         "Communicating ideas to listeners is **putting them across**. 'Put off' would postpone them, 'put up with' means tolerate, and 'put in' means insert or contribute.",
         "put across = communicate.", "hard", 40))
    a(QA(f"{s}-p09", s, "fbp4", B + "The workers refused to ___ in to the management's pressure.",
         ["give", "turn", "carry", "take"],
         "Surrender is **give in to**. 'Turn in' means hand over or go to bed, 'carry in' is literal, and 'take in' means absorb or deceive — none fits 'to the pressure'.",
         "give in to = yield.", "medium", 35))
    a(QA(f"{s}-p10", s, "fbp4", B + "The old tanker ___ off thick black smoke as it climbed the ghat road.",
         ["gave", "took", "called", "set"],
         "To emit is to **give off**: gave off smoke, gave off a smell. 'Took off' means left the ground, 'called off' means cancelled, 'set off' means started a journey or triggered.",
         "give off = emit.", "medium", 35))

    # ---------------- fb-verb-form-tense ----------------
    s = "fb-verb-form-tense"
    a(QA(f"{s}-p01", s, "fbt1", B + "She ___ in Pune since 2020.",
         ["has been living", "lives", "is living", "lived"],
         "'Since 2020' ties a past start to the present, so the perfect is required: **has been living**. The simple present, present continuous and simple past cannot take a since-point.",
         "since + point of time -> has/have (been).", "easy", 30))
    a(QA(f"{s}-p02", s, "fbt1", B + "We ___ each other since our school days.",
         ["have known", "know", "are knowing", "had been knowing"],
         "'Since' needs the perfect, and 'know' is a stative verb that does not take a continuous form. That leaves **have known**. 'Are knowing' and 'had been knowing' break the stative rule, and 'know' ignores since.",
         "Stative verb + since -> present perfect simple.", "medium", 40))
    a(QA(f"{s}-p03", s, "fbt2", B + "When we reached the platform, the train ___.",
         ["had already left", "has already left", "already leaves", "would already leave"],
         "Two past events: the train left first and we reached later. The earlier one takes the past perfect: **had already left**. 'Has already left' clashes with the past 'reached'.",
         "Earlier of two past events -> had + V3.", "medium", 35))
    a(QA(f"{s}-p04", s, "fbt2", B + "No sooner ___ the principal entered the hall than the students stood up.",
         ["had", "has", "did", "was"],
         "The frame is 'No sooner had + subject + V3 ... than + simple past': **had** entered. 'Did' would need the base form 'enter', 'has' clashes with 'stood', and 'was entered' is a wrong passive.",
         "No sooner HAD ... than.", "hard", 40))
    a(QA(f"{s}-p05", s, "fbt3", B + "If it ___ tomorrow, the match will be postponed.",
         ["rains", "will rain", "rained", "would rain"],
         "Type-1 conditional: the if-clause takes the simple present (**rains**) and the main clause takes will. 'Will' never enters the if-clause; 'rained' and 'would rain' belong to type 2.",
         "If + present, will + V1.", "easy", 30))
    a(QA(f"{s}-p06", s, "fbt3", B + "Had she left home earlier, she ___ the flight.",
         ["would have caught", "would catch", "will catch", "had caught"],
         "The inverted 'Had she left' is a type-3 (unreal past) condition, so the result takes **would have caught**. 'Would catch' is type 2, 'will catch' is type 1, and 'had caught' has no would.",
         "Had + subject + V3 ... would have + V3.", "hard", 40))
    a(QA(f"{s}-p07", s, "fbt4", B + "The children enjoy ___ in the rain.",
         ["playing", "to play", "play", "to playing"],
         "'Enjoy' is followed by a gerund: enjoy **playing**. 'Enjoy to play' is the common slip; 'play' and 'to playing' are not possible after enjoy.",
         "enjoy/avoid/deny + V-ing.", "easy", 30))
    a(QA(f"{s}-p08", s, "fbt4", B + "The committee decided ___ the event to December.",
         ["to postpone", "postponing", "postpone", "to postponing"],
         "'Decide' takes the infinitive: decided **to postpone**. 'Decided postponing' uses the gerund wrongly; the bare verb and 'to postponing' are ungrammatical here.",
         "decide/agree/refuse + to + V1.", "medium", 35))
    a(QA(f"{s}-p09", s, "fbt5", B + "Neither of the two answers ___ correct.",
         ["is", "are", "were", "have been"],
         "'Neither of + plural noun' takes a singular verb because neither (not one) is the head. So **is**. 'Are', 'were' and 'have been' agree with 'answers', the trap noun.",
         "neither of / each of -> singular verb.", "medium", 35))
    a(QA(f"{s}-p10", s, "fbt5", B + "The number of applicants for the post ___ increased sharply this year.",
         ["has", "have", "are", "were"],
         "'The number of' is singular (one number), so **has** increased. 'A number of' would be plural — that is the distinction being tested. 'Are increased' and 'were increased' are wrong passives with the wrong number.",
         "THE number -> singular; A number -> plural.", "hard", 40))

    # ---------------- fb-connectives-pronouns ----------------
    s = "fb-connectives-pronouns"
    a(QA(f"{s}-p01", s, "fbn1", B + "No sooner had the rain stopped ___ the children ran out to play.",
         ["than", "when", "then", "that"],
         "'No sooner' pairs only with **than**. 'When' belongs to hardly or scarcely, 'then' is a time adverb, and 'that' is not a correlative.",
         "no sooner -> than.", "easy", 25))
    a(QA(f"{s}-p02", s, "fbn1", B + "The patient had scarcely reached the hospital ___ he lost consciousness.",
         ["when", "than", "then", "so"],
         "'Scarcely' (like hardly) pairs with **when**. 'Than' is the partner of no sooner, the mix-up the question is testing; 'then' and 'so' do not complete the frame.",
         "hardly / scarcely -> when.", "medium", 30))
    a(QA(f"{s}-p03", s, "fbn2", B + "This is the house ___ roof was damaged in the storm.",
         ["whose", "which", "who", "whom"],
         "The roof belongs to the house, which is possession, so **whose** is needed ('whose' is allowed for things). 'Which roof' would start a question, and 'who' and 'whom' refer to people.",
         "Possession -> whose, even for things.", "easy", 30))
    a(QA(f"{s}-p04", s, "fbn2", B + "The scientist to ___ the award was given belongs to Kerala.",
         ["whom", "who", "which", "whose"],
         "After a preposition, the object form is required: to **whom**. 'To who' is ungrammatical, 'to which' refers to things, and 'whose' needs a following noun.",
         "Preposition + whom.", "hard", 40))
    a(QA(f"{s}-p05", s, "fbn3", B + "He was exhausted, ___ he kept working till midnight.",
         ["yet", "so", "because", "therefore"],
         "Being exhausted and still working are in contrast, so the connector is **yet**. 'So' and 'therefore' would treat working late as a result of exhaustion, and 'because' would make exhaustion its cause.",
         "Contradiction -> but / yet.", "medium", 30))
    a(QA(f"{s}-p06", s, "fbn3", B + "The flight was cancelled ___ the dense fog over the airport.",
         ["because of", "because", "although", "despite"],
         "Fog is the cause, and a noun phrase ('the dense fog') follows, so **because of** is needed. 'Because' needs a full clause, and 'although' and 'despite' express contrast, not cause.",
         "Cause + noun -> because of / owing to.", "medium", 35))
    a(QA(f"{s}-p07", s, "fbn4", B + "The students decorated the classroom ___.",
         ["themselves", "theirselves", "themself", "ourselves"],
         "The students did it without help, which calls for the reflexive of 'they': **themselves**. 'Theirselves' and 'themself' are non-standard, and 'ourselves' does not match the subject.",
         "they -> themselves.", "easy", 25))
    a(QA(f"{s}-p08", s, "fbn4", B + "The company has changed ___ logo after twenty years.",
         ["its", "it's", "its'", "it"],
         "The possessive of 'it' is **its**, with no apostrophe. 'It's' means 'it is' ('it is logo' makes no sense), 'its'' is not a word, and 'it' is not possessive.",
         "Expand it's -> it is; if nonsense, use its.", "medium", 30))
    a(QA(f"{s}-p09", s, "fbn5", B + "___ being the favourites, the team lost in the first round.",
         ["Despite", "Although", "Though", "However"],
         "A gerund phrase ('being the favourites') follows the blank, so the contrast word must take a noun or gerund: **Despite**. 'Although' and 'though' need a full clause ('Although they were the favourites'), and 'however' cannot introduce a phrase.",
         "Despite + noun / V-ing; although + clause.", "medium", 35))
    a(QA(f"{s}-p10", s, "fbn5", B + "___ he had a fracture in his wrist, he completed the exam.",
         ["Even though", "Despite", "In spite of", "Owing to"],
         "A full clause follows ('he had a fracture'), and the sense is contrast, so **Even though** fits. 'Despite' and 'In spite of' need a noun phrase ('despite the fracture'), and 'Owing to' expresses cause.",
         "Clause after the blank -> although / even though.", "hard", 40))

    # ---------------- fb-homonyms-confusables ----------------
    s = "fb-homonyms-confusables"
    a(QA(f"{s}-p01", s, "fbh1", B + "I ___ you to check the timetable before leaving.",
         ["advise", "advice", "advices", "adviser"],
         "The slot comes after the subject 'I' and takes an object, so a verb is needed: **advise**. 'Advice' is the noun (and is uncountable, so 'advices' is wrong), and 'adviser' is a person.",
         "advise = verb; advice = noun.", "easy", 25))
    a(QA(f"{s}-p02", s, "fbh1", B + "There is no ___ that the accused was present at the scene.",
         ["proof", "prove", "proves", "proven"],
         "After 'no' a noun is needed: **proof**. 'Prove' and 'proves' are verb forms, and 'proven' is a participle.",
         "proof = noun; prove = verb.", "medium", 30))
    a(QA(f"{s}-p03", s, "fbh2", B + "Tighten the screw; it has come ___.",
         ["loose", "lose", "loss", "lost"],
         "A screw that is not tight is **loose**, and 'come loose' is the phrase. 'Lose' is a verb meaning misplace, 'loss' is a noun, and 'lost' means misplaced.",
         "loose = not tight; lose = misplace.", "easy", 25))
    a(QA(f"{s}-p04", s, "fbh2", B + "Lack of sleep can seriously ___ a student's concentration.",
         ["affect", "effect", "affection", "effective"],
         "The sense is influence, and the slot follows 'can', so the verb **affect** is needed. 'Effect' as a verb means bring about, which does not fit here; 'affection' and 'effective' are the wrong parts of speech.",
         "can/will + affect; an/the + effect.", "medium", 35))
    a(QA(f"{s}-p05", s, "fbh3", B + "The ___ of the school addressed the students at the morning assembly.",
         ["principal", "principle", "principality", "principled"],
         "The head of a school is the **principal**. 'Principle' means a rule or belief, 'principality' is a state ruled by a prince, and 'principled' is an adjective.",
         "principAL = head (a pal); principLE = ruLE.", "medium", 30))
    a(QA(f"{s}-p06", s, "fbh3", B + "The car remained ___ at the signal even after the light turned green.",
         ["stationary", "stationery", "stationer", "station"],
         "Not moving = **stationary**. 'Stationery' means writing materials, a 'stationer' sells them, and 'station' is a noun that cannot describe the car here.",
         "stationARy = stAnding still; stationERy = papER.", "medium", 30))
    a(QA(f"{s}-p07", s, "fbh4", B + "The film board ___ two violent scenes before granting the certificate.",
         ["censored", "censured", "sensored", "sensed"],
         "Cutting content from a film is **censoring** it. 'Censured' means formally rebuked, which applies to people and conduct, not to scenes; 'sensored' is not a word, and 'sensed' means perceived.",
         "censor = cut content; censure = rebuke.", "medium", 35))
    a(QA(f"{s}-p08", s, "fbh4", B + "The poem contains an ___ to an episode from the Mahabharata.",
         ["allusion", "illusion", "elusion", "delusion"],
         "An indirect reference is an **allusion**, and 'allusion to' is the standard pattern. 'Illusion' is a false appearance, 'elusion' means escape, and 'delusion' is a false belief — none is a reference.",
         "allusion = reference; illusion = mirage.", "hard", 40))

    # ---------------- fb-double-blanks ----------------
    s = "fb-double-blanks"
    a(QA(f"{s}-p01", s, "fbd1", B + "___ the teachers ___ the principal was informed about the inspection.",
         ["Neither, nor", "Both, and", "Neither, or", "Either, nor"],
         "The verb is singular ('was'), which rules out 'Both ... and' (that needs 'were'). With **Neither ... nor**, the verb agrees with the nearer subject 'the principal', which is singular, so 'was' fits. 'Neither ... or' and 'Either ... nor' mix partners that never go together.",
         "Singular verb + correct partners -> neither ... nor.", "medium", 40))
    a(QA(f"{s}-p02", s, "fbd1", B + "The new policy will benefit ___ farmers ___ small traders.",
         ["not only, but also", "neither, or", "either, nor", "both, or"],
         "Only **not only ... but also** is a correct pair here. 'Neither ... or', 'either ... nor' and 'both ... or' each mix partners from different pairs.",
         "Check that the partners match first.", "easy", 30))
    a(QA(f"{s}-p03", s, "fbd1", B + "___ you finish the project on time ___ you forfeit the bonus.",
         ["Either, or", "Neither, nor", "Both, and", "Whether, nor"],
         "The sentence offers two alternatives — finish on time, or lose the bonus — so **Either ... or** fits. 'Neither ... nor' before two clauses would need inversion and would deny both. 'Both ... and' makes nonsense of the choice, and 'Whether ... nor' is not a pair.",
         "Alternatives -> either ... or.", "hard", 45))
    a(QA(f"{s}-p04", s, "fbd2", B + "After two days at sea, the missing fishermen returned home ___ and ___.",
         ["safe, sound", "null, void", "part, parcel", "odds, ends"],
         "Returning unharmed is returning **safe and sound**. 'Null and void' means legally invalid, 'part and parcel' means essential, and 'odds and ends' means small leftover items.",
         "Unhurt = safe and sound.", "easy", 30))
    a(QA(f"{s}-p05", s, "fbd2", B + "___ and ___, every candidate must carry a valid photo identity card.",
         ["First, foremost", "Null, void", "Odds, ends", "Safe, sound"],
         "The sentence opens with the most important instruction, so the idiom is **First and foremost**. The other pairs are real idioms, but none can introduce a priority.",
         "Most important point = first and foremost.", "medium", 35))
    a(QA(f"{s}-p06", s, "fbd3", B + "The office remains open ___ 9 a.m. ___ 5 p.m.",
         ["from, to", "from, and", "between, to", "since, till"],
         "A start-to-end range takes **from ... to**. 'From ... and' and 'between ... to' mix partners, and 'since' marks a starting point up to now, not a daily range.",
         "from-to; between-and — never mix.", "medium", 30))
    a(QA(f"{s}-p07", s, "fbd3", B + "The border dispute ___ India ___ its neighbour was settled through talks.",
         ["between, and", "among, and", "between, with", "from, to"],
         "Two parties take **between ... and**. 'Among' is for three or more, 'between ... with' mixes partners, and 'from ... to' marks a range, not a dispute between two sides.",
         "Two parties -> between ... and.", "medium", 35))
    a(QA(f"{s}-p08", s, "fbd4", B + "___ had he left the house ___ it began to pour.",
         ["Hardly, when", "Hardly, than", "No sooner, when", "Scarcely, than"],
         "The fixed frames are 'Hardly ... when' and 'No sooner ... than'. Only **Hardly ... when** keeps its true partner; the other three cross the pairs.",
         "Hardly/Scarcely-when; No sooner-than.", "medium", 35))
    a(QA(f"{s}-p09", s, "fbd4", B + "___ had the result been declared ___ the students started celebrating.",
         ["No sooner, than", "No sooner, when", "Hardly, than", "Scarcely, then"],
         "Only **No sooner ... than** is a matched pair. 'No sooner ... when' and 'Hardly ... than' cross the two frames, and 'then' is never a correlative partner.",
         "Match the partners; then is always a decoy.", "hard", 40))
    return qs
