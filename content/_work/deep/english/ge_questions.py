# New practice questions for grammar-essentials. In every item opts[0] is the correct answer;
# QA() moves it to a deterministic position.
from _lib import QA

FILL = "Select the most appropriate option to fill in the blank.  "
ERR = ("The following sentence has been divided into parts. One of them contains an error. "
       "Select the part that contains the error.\n\n")
IMP = ("Select the most appropriate option to substitute the highlighted segment in the given sentence. "
       "If no substitution is required, select 'No substitution required'.\n\n")
TAG = "Select the correct question tag.  "


def mk(qid, sub, pat, q, opts, solution, shortcut=None, diff="medium", t=30):
    return QA(qid, sub, pat, q, opts, solution, shortcut=shortcut, diff=diff, t=t)


def QS_GE():
    qs = []
    A = qs.append
    PS = "ge-parts-of-speech"
    TE = "ge-tenses"
    SV = "ge-subject-verb-agreement"
    AD = "ge-articles-determiners"
    PR = "ge-prepositions-conjunctions"
    MC = "ge-modals-conditionals"
    CQ = "ge-comparison-question-tags"
    NI = "ge-non-finites-inversion"

    # ---------------- ge-parts-of-speech (pos) ----------------
    A(mk("ge-parts-of-speech-p01", PS, "pos-p1", FILL + "She gave me some useful ___ before the interview.",
         ["advice", "advices", "advises", "advising"],
         "**Advice** is uncountable — no plural -s, no 'an'. 'Advises' is the verb form; the slot needs a noun after 'some useful'.",
         "advice never takes -s.", "easy", 25))
    A(mk("ge-parts-of-speech-p02", PS, "pos-p1", ERR + "The furnitures in this room / was bought last year / from a local carpenter / by my uncle.",
         ["The furnitures in this room", "was bought last year", "from a local carpenter", "by my uncle."],
         "**Furniture** is uncountable, so 'the furnitures' is the error; once corrected to 'the furniture', the singular verb 'was bought' is right.",
         "furniture, luggage, information: no -s.", "medium", 30))
    A(mk("ge-parts-of-speech-p03", PS, "pos-p1", FILL + "How much ___ does the journey take?",
         ["time", "times", "hour", "hours"],
         "'Much' goes with an uncountable noun → **time**. 'Hours' is countable and would need 'how many'.",
         "much + uncountable.", "easy", 20))
    A(mk("ge-parts-of-speech-p04", PS, "pos-p2", FILL + "Hard work is the key to ___.",
         ["success", "succeed", "successful", "successfully"],
         "After 'the key to' (here a preposition) we need a noun → **success**. The family: succeed (verb), successful (adjective), successfully (adverb).",
         "the + noun after key to.", "easy", 25))
    A(mk("ge-parts-of-speech-p05", PS, "pos-p2", FILL + "He was praised for his ___ behaviour at the function.",
         ["courteous", "courtesy", "courteously", "courtesies"],
         "An adjective is needed before the noun 'behaviour' → **courteous**. 'Courtesy' is the noun, 'courteously' the adverb.",
         "before a noun → adjective.", "medium", 25))
    A(mk("ge-parts-of-speech-p06", PS, "pos-p2", FILL + "The manager spoke ___ to the careless clerk.",
         ["harshly", "harsh", "harshness", "harsher"],
         "'Spoke' is an action verb, so an adverb is needed → **harshly**. 'Harsh' would describe a thing, not the manner of speaking.",
         "action verb + -ly.", "medium", 25))
    A(mk("ge-parts-of-speech-p07", PS, "pos-p3", FILL + "The flowers smell ___.",
         ["sweet", "sweetly", "sweetness", "sweeter"],
         "'Smell' here is a linking verb (= are when smelled), so it takes an adjective → **sweet**. 'Sweetly' would describe the act of smelling.",
         "linking verb + adjective.", "easy", 20))
    A(mk("ge-parts-of-speech-p08", PS, "pos-p3", FILL + "He looked ___ when he heard about the accident.",
         ["sad", "sadly", "sadness", "sadden"],
         "'Looked' means 'seemed' — a linking verb — so the adjective **sad** describes his state. 'Sadly' would mean he looked in a sad manner.",
         "look = seem → adjective.", "hard", 30))
    A(mk("ge-parts-of-speech-p09", PS, "pos-p4", FILL + "Between you and ___, the plan will not work.",
         ["me", "I", "mine", "myself"],
         "After the preposition 'between' the object form is needed → **me**. 'I' is only for subject jobs.",
         "preposition + object pronoun.", "easy", 20))
    A(mk("ge-parts-of-speech-p10", PS, "pos-p4", FILL + "The company announced ___ annual results yesterday.",
         ["its", "it's", "theirs", "there"],
         "The owner form before a noun is **its**. 'It's' = it is; 'theirs' is a standalone possessive; 'there' shows place.",
         "its + noun, no apostrophe.", "medium", 25))
    A(mk("ge-parts-of-speech-p11", PS, "pos-p4", FILL + "Rahul and ___ are going to the book fair.",
         ["I", "me", "mine", "myself"],
         "The pronoun is part of the subject of 'are going', so the subject form **I** is needed. Test by dropping Rahul: '*I* am going'.",
         "subject job → I.", "easy", 20))

    # ---------------- ge-tenses (ten) ----------------
    A(mk("ge-tenses-p01", TE, "ten-p1", FILL + "She ___ to Chennai last year.",
         ["moved", "has moved", "had moved", "moves"],
         "'Last year' is a finished past time signal → simple past **moved**. Present perfect needs a since/for signal; past perfect needs an earlier action.",
         "last year → V2.", "easy", 20))
    A(mk("ge-tenses-p02", TE, "ten-p1", FILL + "I have known him ___ 2015.",
         ["since", "for", "from", "by"],
         "A point of time (2015) takes **since**; 'for' measures a length (for eight years).",
         "since + point, for + period.", "medium", 20))
    A(mk("ge-tenses-p03", TE, "ten-p1", FILL + "Look! The cat ___ on the roof again.",
         ["is sitting", "sits", "sat", "has sat"],
         "'Look!' signals an action happening now → present continuous **is sitting**.",
         "Look! = now.", "easy", 20))
    A(mk("ge-tenses-p04", TE, "ten-p2", FILL + "As soon as the results ___, we will celebrate.",
         ["are declared", "will be declared", "will declare", "were declared"],
         "Inside a time clause ('as soon as') the present tense carries future meaning → **are declared**. 'Will' appears only in the main clause.",
         "no will after as soon as.", "medium", 30))
    A(mk("ge-tenses-p05", TE, "ten-p2", FILL + "If it ___ tomorrow, the match will be cancelled.",
         ["rains", "will rain", "rain", "rained"],
         "First conditional: the if-clause takes the simple present → **rains**; 'will be cancelled' stands in the main clause.",
         "if + present, will + V1.", "medium", 25))
    A(mk("ge-tenses-p06", TE, "ten-p2", FILL + "I will call you when I ___ home.",
         ["reach", "will reach", "reached", "am reaching"],
         "The time clause after 'when' takes the simple present for future meaning → **reach**.",
         "when-clause → present.", "medium", 25))
    A(mk("ge-tenses-p07", TE, "ten-p3", FILL + "The patient had died before the doctor ___.",
         ["arrived", "had arrived", "arrives", "arrive"],
         "The earlier action (death) already carries 'had died', so the later action takes the simple past → **arrived**.",
         "earlier = had V3, later = V2.", "medium", 25))
    A(mk("ge-tenses-p08", TE, "ten-p3", FILL + "The players ___ the field before the rain started.",
         ["had left", "left", "have left", "were leaving"],
         "Two past actions: leaving happened before the rain started, so the earlier one takes the past perfect → **had left**.",
         "before + earlier action → had V3.", "medium", 25))
    A(mk("ge-tenses-p09", TE, "ten-p4", FILL + "It ___ since morning.",
         ["has been raining", "is raining", "rained", "had been raining"],
         "'Since morning' + still going on → present perfect continuous **has been raining**.",
         "since + still running → has been V-ing.", "medium", 25))
    A(mk("ge-tenses-p10", TE, "ten-p4", FILL + "The workers ___ on this bridge for two years now.",
         ["have been working", "are working", "worked", "work"],
         "'For two years' measures a duration that continues to the present → present perfect continuous **have been working**.",
         "for + period up to now.", "easy", 25))
    A(mk("ge-tenses-p11", TE, "ten-p4", FILL + "He was exhausted because he ___ for six hours.",
         ["had been walking", "was walking", "has been walking", "walked"],
         "The walking continued up to a past moment (was exhausted), so step one tense back → past perfect continuous **had been walking**.",
         "duration before a past point.", "hard", 30))

    # ---------------- ge-subject-verb-agreement (sva) ----------------
    A(mk("ge-subject-verb-agreement-p01", SV, "sva-p1", FILL + "The list of candidates ___ been published.",
         ["has", "have", "are", "were"],
         "The head noun is **list** (singular); the of-phrase does not change it → has been published.",
         "cover the of-phrase.", "easy", 25))
    A(mk("ge-subject-verb-agreement-p02", SV, "sva-p1", FILL + "The bouquet of roses ___ on the table.",
         ["is", "are", "were", "have"],
         "Subject = bouquet (singular); roses only describes it → **is**.",
         "bouquet, not roses.", "easy", 20))
    A(mk("ge-subject-verb-agreement-p03", SV, "sva-p2", FILL + "Every one of the players ___ praised by the coach.",
         ["was", "were", "have", "are"],
         "'Every one' stays singular even with a plural after of → **was**.",
         "every one → singular.", "medium", 25))
    A(mk("ge-subject-verb-agreement-p04", SV, "sva-p2", FILL + "Each of the girls ___ given a certificate.",
         ["was", "were", "are", "have"],
         "Each → always singular → **was**.",
         "each → singular.", "easy", 20))
    A(mk("ge-subject-verb-agreement-p05", SV, "sva-p3", FILL + "Neither the manager nor the workers ___ present at the meeting.",
         ["were", "was", "is", "has"],
         "With neither...nor the verb follows the nearer subject — **workers** (plural) → were.",
         "verb follows the nearer subject.", "medium", 25))
    A(mk("ge-subject-verb-agreement-p06", SV, "sva-p3", FILL + "Either Ram or his brothers ___ to blame for the loss.",
         ["are", "is", "was", "has"],
         "Nearer subject = brothers (plural) → **are**.",
         "either...or: proximity rule.", "medium", 25))
    A(mk("ge-subject-verb-agreement-p07", SV, "sva-p4", FILL + "The committee ___ its decision yesterday.",
         ["announced", "announce", "have announced", "announcing"],
         "The committee acts as one unit → singular; the past signal 'yesterday' fixes **announced** (not 'has announced').",
         "committee as one body.", "medium", 25))
    A(mk("ge-subject-verb-agreement-p08", SV, "sva-p4", FILL + "Mathematics ___ my favourite subject.",
         ["is", "are", "were", "have"],
         "Subjects ending in -ics (mathematics, physics, economics) take a singular verb → **is**.",
         "-ics subjects are singular.", "easy", 20))
    A(mk("ge-subject-verb-agreement-p09", SV, "sva-p2", FILL + "More than one student ___ selected for the final round.",
         ["was", "were", "have", "are"],
         "'More than one' is followed by a singular noun and a singular verb → **was** — the exam's favourite surprise.",
         "more than one → singular.", "hard", 30))
    A(mk("ge-subject-verb-agreement-p10", SV, "sva-p1", ERR + "The price of these shoes / are too high / for a student / to afford.",
         ["are too high", "The price of these shoes", "for a student", "to afford."],
         "The head noun is **price** (singular), so the error is the plural verb: 'are too high' should be 'is too high'.",
         "price is the subject.", "medium", 30))

    # ---------------- ge-articles-determiners (art) ----------------
    A(mk("ge-articles-determiners-p01", AD, "art-p1", FILL + "He is ___ honest officer.",
         ["an", "a", "the", "one"],
         "'Honest' begins with a silent h — the first sound is 'o' → **an**.",
         "sound, not spelling.", "easy", 20))
    A(mk("ge-articles-determiners-p02", AD, "art-p1", FILL + "She is ___ MLA from Bihar.",
         ["an", "a", "the", "one"],
         "MLA is read letter by letter: 'em' — a vowel sound → **an**.",
         "an MLA, an M.A., an X-ray.", "medium", 20))
    A(mk("ge-articles-determiners-p03", AD, "art-p1", FILL + "My cousin joined ___ university in Delhi last month.",
         ["a", "an", "the", "one"],
         "'University' begins with the consonant sound 'yu' → **a**, whatever the spelling suggests.",
         "a university, a European.", "medium", 20))
    A(mk("ge-articles-determiners-p04", AD, "art-p2", FILL + "___ Ganga is considered a holy river.",
         ["The", "A", "An", "No article"],
         "River names take **the**: the Ganga, the Yamuna, the Nile.",
         "rivers take the.", "easy", 20))
    A(mk("ge-articles-determiners-p05", AD, "art-p2", FILL + "This is ___ best novel I have ever read.",
         ["the", "a", "an", "one"],
         "A superlative (best) always carries **the**.",
         "superlative → the.", "medium", 20))
    A(mk("ge-articles-determiners-p06", AD, "art-p2", FILL + "The sun rises in ___ east.",
         ["the", "a", "an", "one"],
         "Directions take **the**: the east, the north, the west.",
         "directions take the.", "medium", 20))
    A(mk("ge-articles-determiners-p07", AD, "art-p3", IMP + "He goes to **the school** every day.",
         ["goes to school", "go to school", "goes to the schools", "No substitution required"],
         "When 'school' is used for its purpose (studying), no article is used → **goes to school**. 'The school' would mean the building.",
         "purpose-use: no article.", "medium", 30))
    A(mk("ge-articles-determiners-p08", AD, "art-p3", IMP + "**The man** is mortal.",
         ["Man", "A man", "The men", "No substitution required"],
         "'Man' meaning the human race takes no article → **Man is mortal**.",
         "man (human race): no article.", "hard", 30))
    A(mk("ge-articles-determiners-p09", AD, "art-p4", FILL + "Give me ___ time to think; I am almost done.",
         ["a little", "little", "the little", "a few"],
         "'Time' is uncountable, and the speaker needs some (positive sense) → **a little**. Plain 'little' would mean almost none.",
         "a little = some.", "medium", 25))
    A(mk("ge-articles-determiners-p10", AD, "art-p4", FILL + "He is new in the city and has ___ friends here.",
         ["few", "a few", "the few", "a little"],
         "'Friends' is countable, and being new implies almost none → **few** (negative sense). 'A few' would mean some.",
         "few = hardly any.", "hard", 30))
    A(mk("ge-articles-determiners-p11", AD, "art-p1", FILL + "I found ___ one-rupee coin on the pavement.",
         ["a", "an", "the", "some"],
         "'One' begins with the consonant sound 'wu' → **a** one-rupee coin.",
         "a one-rupee coin.", "hard", 30))

    # ---------------- ge-prepositions-conjunctions (pre) ----------------
    A(mk("ge-prepositions-conjunctions-p01", PR, "pre-p1", FILL + "The meeting has been fixed ___ Monday morning.",
         ["on", "in", "at", "by"],
         "Days and dates take **on**: on Monday, on 15 August.",
         "on + day.", "easy", 20))
    A(mk("ge-prepositions-conjunctions-p02", PR, "pre-p1", FILL + "We reached the airport ___ 6 o'clock in the evening.",
         ["at", "on", "in", "by"],
         "Exact clock times take **at**: at 6 o'clock, at noon.",
         "at + clock time.", "medium", 20))
    A(mk("ge-prepositions-conjunctions-p03", PR, "pre-p1", FILL + "My cousin lives ___ Bengaluru.",
         ["in", "at", "on", "into"],
         "Large places — cities, states, countries — take **in**; 'at' is for small specific points (at Andheri).",
         "in + city.", "medium", 20))
    A(mk("ge-prepositions-conjunctions-p04", PR, "pre-p2", FILL + "She is very fond ___ classical music.",
         ["of", "for", "with", "to"],
         "The fixed pair is **fond of**.",
         "fond of.", "easy", 20))
    A(mk("ge-prepositions-conjunctions-p05", PR, "pre-p2", FILL + "Ravi is very good ___ mathematics.",
         ["at", "in", "on", "for"],
         "Skill words take **at**: good at, brilliant at, bad at.",
         "good at.", "medium", 20))
    A(mk("ge-prepositions-conjunctions-p06", PR, "pre-p2", FILL + "The manager was angry ___ the delay in delivery.",
         ["at", "with", "on", "for"],
         "**Angry at** a thing or situation; angry **with** a person. The delay is a thing → at.",
         "angry at a thing.", "hard", 30))
    A(mk("ge-prepositions-conjunctions-p07", PR, "pre-p3", FILL + "The prize money was divided ___ the two winners.",
         ["between", "among", "in", "into"],
         "Two parties → **between**; three or more treated as a mass → among.",
         "between = two.", "easy", 20))
    A(mk("ge-prepositions-conjunctions-p08", PR, "pre-p3", FILL + "He has been working in this office ___ five years.",
         ["for", "since", "from", "during"],
         "A length of time takes **for**; since needs a starting point (since 2021).",
         "for + period.", "medium", 20))
    A(mk("ge-prepositions-conjunctions-p09", PR, "pre-p4", FILL + "No sooner did the bell ring ___ the students rushed out.",
         ["than", "when", "then", "that"],
         "The welded pair is **No sooner ... than**; mixing it with 'when' is the classic planted error.",
         "no sooner...than.", "medium", 25))
    A(mk("ge-prepositions-conjunctions-p10", PR, "pre-p4", FILL + "She is not only intelligent ___ hardworking.",
         ["but also", "and also", "but even", "as well"],
         "The correlative pair is **not only ... but also**, and both parts must join parallel words.",
         "not only...but also.", "medium", 25))

    # ---------------- ge-modals-conditionals (mod) ----------------
    A(mk("ge-modals-conditionals-p01", MC, "mod-p1", FILL + "He can ___ three languages fluently.",
         ["speak", "speaks", "speaking", "to speak"],
         "After a modal the base verb is used → **speak**. No -s, no -ing, no to.",
         "modal + V1.", "easy", 20))
    A(mk("ge-modals-conditionals-p02", MC, "mod-p1", ERR + "You should / to consult a doctor / immediately after / the fever returns.",
         ["to consult a doctor", "You should", "immediately after", "the fever returns."],
         "A modal is never followed by to: 'should consult' is correct, so **'to consult a doctor'** carries the error.",
         "should + V1, no to.", "medium", 30))
    A(mk("ge-modals-conditionals-p03", MC, "mod-p2", FILL + "You look exhausted; you ___ have worked all night.",
         ["must", "can", "shall", "would"],
         "A sure deduction about the past takes **must have** + V3. 'Can have' is not used for deduction; 'should have' would find fault rather than deduce.",
         "must have = sure past.", "medium", 30))
    A(mk("ge-modals-conditionals-p04", MC, "mod-p2", FILL + "You ___ have taken my permission before using my laptop.",
         ["should", "must", "can", "may"],
         "Criticising a past action that did not happen takes **should have** + V3. 'Must have' would only deduce, not find fault.",
         "should have = past fault.", "hard", 30))
    A(mk("ge-modals-conditionals-p05", MC, "mod-p3", FILL + "If I ___ you, I would apologise at once.",
         ["were", "was", "am", "had been"],
         "Second conditional (unreal present) uses **were** for every subject: If I were you...",
         "if I were you.", "medium", 25))
    A(mk("ge-modals-conditionals-p06", MC, "mod-p3", FILL + "If it rains, the match ___ postponed.",
         ["will be", "would be", "would have been", "is"],
         "First conditional: if + present, main clause **will be** + V3. 'Would' belongs to the second conditional.",
         "real chance → will.", "medium", 25))
    A(mk("ge-modals-conditionals-p07", MC, "mod-p3", FILL + "If he had prepared well, he ___ the examination.",
         ["would have passed", "would pass", "will pass", "had passed"],
         "Third conditional: had + V3 in the if-clause → **would have** + V3 in the main clause.",
         "had V3 → would have V3.", "hard", 30))
    A(mk("ge-modals-conditionals-p08", MC, "mod-p4", FILL + "___ I use your phone for an urgent call?",
         ["May", "Shall", "Should", "Would"],
         "Formal permission is asked with **May I**. 'Shall I' offers a service; 'should' asks duty.",
         "May I = permission.", "medium", 20))
    A(mk("ge-modals-conditionals-p09", MC, "mod-p4", FILL + "When I was young, I ___ play cricket every evening.",
         ["used to", "am used to", "was used to", "use to"],
         "A stopped past habit is **used to** + V1. 'Be used to' means 'be accustomed to' and needs -ing after it.",
         "used to = past habit.", "medium", 25))
    A(mk("ge-modals-conditionals-p10", MC, "mod-p1", FILL + "She need not ___ anything about the incident.",
         ["say", "to say", "saying", "says"],
         "'Need not' behaves like a modal → base verb **say**.",
         "need not + V1.", "medium", 25))

    # ---------------- ge-comparison-question-tags (cmp) ----------------
    A(mk("ge-comparison-question-tags-p01", CQ, "cmp-p1", FILL + "This road is ___ than that one.",
         ["narrower", "more narrow", "narrowest", "most narrow"],
         "Comparative with 'than' → one marker: **narrower**. 'More narrow' doubles the marker.",
         "than → -er form.", "easy", 20))
    A(mk("ge-comparison-question-tags-p02", CQ, "cmp-p1", IMP + "Gold is **more costlier** than silver.",
         ["costlier", "most costlier", "more costly", "No substitution required"],
         "'More costlier' doubles the comparative marker; keep only one → **costlier**.",
         "never more + -er.", "medium", 30))
    A(mk("ge-comparison-question-tags-p03", CQ, "cmp-p1", FILL + "He is the ___ boy in the class.",
         ["tallest", "taller", "most tallest", "more tall"],
         "'The ... in the class' signals a superlative → **tallest**.",
         "the ... in → superlative.", "easy", 20))
    A(mk("ge-comparison-question-tags-p04", CQ, "cmp-p2", FILL + "Mumbai is larger than ___ city in India.",
         ["any other", "any", "all other", "others"],
         "Mumbai is itself an Indian city, so 'other' excludes it → **any other** city.",
         "member of the group → any other.", "medium", 25))
    A(mk("ge-comparison-question-tags-p05", CQ, "cmp-p2", FILL + "Kalidasa is greater than ___ poet in Sanskrit literature.",
         ["any other", "any", "all the", "some other"],
         "Kalidasa is a Sanskrit poet, so the comparison must exclude him → **any other** poet.",
         "exclude the subject itself.", "hard", 30))
    A(mk("ge-comparison-question-tags-p06", CQ, "cmp-p3", TAG + "She sings well, ___",
         ["doesn't she?", "isn't she?", "does she?", "won't she?"],
         "'Sings' needs the auxiliary does; the positive sentence takes a negative tag → **doesn't she?**",
         "aux copy + flip.", "easy", 20))
    A(mk("ge-comparison-question-tags-p07", CQ, "cmp-p3", TAG + "They haven't finished the work, ___",
         ["have they?", "haven't they?", "do they?", "didn't they?"],
         "Negative sentence → positive tag, copying the auxiliary have → **have they?**",
         "negative → positive tag.", "medium", 20))
    A(mk("ge-comparison-question-tags-p08", CQ, "cmp-p4", TAG + "Let's go for a walk, ___",
         ["shall we?", "will we?", "don't we?", "won't we?"],
         "The fixed tag for a Let's suggestion is **shall we?**",
         "Let's → shall we.", "medium", 20))
    A(mk("ge-comparison-question-tags-p09", CQ, "cmp-p4", TAG + "Open the window, ___",
         ["will you?", "do you?", "shall we?", "are you?"],
         "An imperative takes **will you?** as its tag.",
         "command → will you.", "medium", 20))
    A(mk("ge-comparison-question-tags-p10", CQ, "cmp-p4", TAG + "I am late for the class, ___",
         ["aren't I?", "amn't I?", "not I?", "don't I?"],
         "The fixed tag for 'I am' is **aren't I?** — the one place English drops 'am not'.",
         "I am → aren't I.", "hard", 25))

    # ---------------- ge-non-finites-inversion (nfi) ----------------
    A(mk("ge-non-finites-inversion-p01", NI, "nfi-p1", FILL + "He avoided ___ the question directly.",
         ["answering", "to answer", "answer", "answered"],
         "'Avoid' is on the gerund list → avoid + V-**ing** → answering.",
         "avoid + -ing.", "easy", 20))
    A(mk("ge-non-finites-inversion-p02", NI, "nfi-p1", FILL + "She is fond of ___ detective novels.",
         ["reading", "to read", "read", "reads"],
         "After a preposition (of) the verb takes the gerund → **reading**.",
         "preposition + -ing.", "medium", 25))
    A(mk("ge-non-finites-inversion-p03", NI, "nfi-p1", FILL + "I enjoy ___ to music while working.",
         ["listening", "to listen", "listen", "listened"],
         "'Enjoy' is on the gerund list → enjoy + V-**ing** → listening.",
         "enjoy + -ing.", "medium", 20))
    A(mk("ge-non-finites-inversion-p04", NI, "nfi-p2", FILL + "He promised ___ the assignment by Friday.",
         ["to finish", "finishing", "finish", "finished"],
         "'Promise' takes the to-infinitive → **to finish**.",
         "promise + to V1.", "medium", 25))
    A(mk("ge-non-finites-inversion-p05", NI, "nfi-p2", FILL + "Remember ___ the lights before you leave the office.",
         ["to switch off", "switching off", "switch off", "switched off"],
         "A duty still ahead → remember + **to** + V1. 'Remember switching' would recall a past act.",
         "remember to = duty ahead.", "hard", 30))
    A(mk("ge-non-finites-inversion-p06", NI, "nfi-p3", FILL + "The teacher made the boy ___ the poem aloud.",
         ["recite", "to recite", "reciting", "recited"],
         "'Make' takes object + bare infinitive → **recite**; no 'to' after make in the active voice.",
         "make + V1 (no to).", "easy", 25))
    A(mk("ge-non-finites-inversion-p07", NI, "nfi-p3", FILL + "Let him ___ what he thinks is right.",
         ["do", "to do", "doing", "does"],
         "'Let' also takes the bare infinitive → let him **do**.",
         "let + V1.", "easy", 20))
    A(mk("ge-non-finites-inversion-p08", NI, "nfi-p4", FILL + "No sooner had she seen the snake ___ she fainted.",
         ["than", "when", "that", "then"],
         "**No sooner ... than** is a welded pair; 'when' belongs to hardly/scarcely.",
         "no sooner...than.", "medium", 25))
    A(mk("ge-non-finites-inversion-p09", NI, "nfi-p4", FILL + "Never ___ such a beautiful sunset.",
         ["have I seen", "I have seen", "I saw", "did I saw"],
         "A negative opener (Never) forces inversion: auxiliary before subject → **have I seen**.",
         "never + aux + subject.", "medium", 25))
    A(mk("ge-non-finites-inversion-p10", NI, "nfi-p4", FILL + "Scarcely had he sat down ___ the phone rang.",
         ["when", "than", "that", "then"],
         "**Scarcely ... when** is the fixed pair (than pairs with no sooner, not scarcely).",
         "scarcely...when.", "hard", 30))

    return qs
