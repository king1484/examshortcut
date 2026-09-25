# New practice items for sentence-rearrangement (Phase 2).
# Each item lists its four parts in the CORRECT logical order A, B, C, D, plus `labels`: the P/Q/R/S label shown for
# A, B, C, D (so `labels` is also the answer string). `cons` are the written ordering constraints in A-D terms:
#   "A-B"  A immediately before B      "A<C"  A somewhere before C      "^A"  A first      "D$"  D last
# The build script proves that exactly one of the 24 orders satisfies every constraint, and that it is ABCD.
# Solutions use {A}..{D} (rendered as the bold label) and {ANS} (the answer string).

PQRS = "pqrs"      # S1 and S6 fixed, options are 4-letter strings
JUMBLE = "jumble"  # no fixed ends, options are 4-letter strings
FIRST = "first"    # options P/Q/R/S, which comes first
LAST = "last"      # options P/Q/R/S, which comes last


def R(sid, n, pat, kind, parts, labels, cons, sol, short, diff, t=45, s1=None, s6=None):
    # n is only a draft number; the build script numbers items p01.. per subtopic in list order
    return {"id": None, "sub": sid, "pat": pat, "kind": kind, "parts": parts, "labels": labels,
            "cons": cons.split(), "sol": sol, "short": short, "diff": diff, "t": t, "s1": s1, "s6": s6}


def ITEMS():
    it = []
    a = it.append

    # ---------------- rearr-pqrs-method ----------------
    s = "rearr-pqrs-method"
    a(R(s, 16, "rpm1", PQRS, [
        "Millions now practise it daily in parks and studios.",
        "Many of them say it has lowered their stress.",
        "However, many learn it only from online videos.",
        "Beginners should therefore start under a trained teacher."],
        "RPSQ", "A-B C-D B<C D$",
        "Lead {A} continues S1 ('it' = yoga). {B}'s 'Many of them' needs the millions in {A}, giving the pair {A}{B}. The Turn {C} ('However') contrasts with these benefits, and the Close {D} ('therefore') draws the lesson from it. S6's warning about wrong postures follows the advice to find a teacher. {ANS}.",
        "Lead-Support-Turn-Close: 'them' pair, then However, then therefore.", "easy", 40,
        s1="Yoga has become popular across the world.",
        s6="A wrong posture can do more harm than good."))
    a(R(s, 17, "rpm1", PQRS, [
        "Bills can now be paid in seconds from a phone.",
        "This has saved people countless trips to the branch.",
        "But the same convenience has opened doors to fraud.",
        "Customers must therefore never share their OTP with anyone."],
        "QSPR", "A-B B<C C-D D$",
        "{A} gives the Lead fact, and {B}'s 'This has saved' refers to it. {C}'s 'the same convenience' can only come after the benefit is described, and its 'But' turns the argument. {D} is the Close ('therefore') drawn from the fraud risk, and S6's 'this warning' refers back to it. {ANS}.",
        "'the same convenience' needs the benefit first; S6's 'this warning' fixes the last part.", "medium", 45,
        s1="Online banking has changed how Indians handle money.",
        s6="Banks, too, keep repeating this warning."))
    a(R(s, 18, "rpm2", PQRS, [
        "Farmers burn the leftover rice straw to clear their fields quickly.",
        "The smoke drifts to the cities and mixes with the winter fog.",
        "This thick smog sends thousands to hospital with breathing trouble.",
        "Some states now pay farmers to use straw-cutting machines instead."],
        "SQRP", "A-B B-C D$",
        "Problem skeleton. Cause: {A}, straw is burnt. Effect: {B}, 'The smoke' of that burning. Harm: {C}, 'This thick smog' is the smoke mixed with fog. Response: {D}, machines instead of burning. S6's 'such machines' refers to {D}, so it is last. {ANS}.",
        "Cause -> effect -> harm -> response; 'such machines' in S6 pulls the response to the end.", "easy", 40,
        s1="Stubble burning chokes north India every winter.",
        s6="Subsidies for such machines, experts say, must be extended further."))
    a(R(s, 19, "rpm2", PQRS, [
        "Many spend over six hours a day scrolling through short videos.",
        "Such constant screen time leaves little room for sleep.",
        "Tired and restless, they then struggle to focus in class.",
        "Some schools have now introduced phone-free hours to break the habit."],
        "PRSQ", "A-B B-C D$",
        "{A} states the problem in numbers. {B}'s 'Such constant screen time' sums up {A}. {C}'s 'Tired' is the effect of lost sleep, so it follows {B}. {D} is the response, and S6's 'these schools' refers to it. {ANS}.",
        "'Such' sums up the part before it; S6's 'these schools' fixes the response last.", "medium", 45,
        s1="Mobile phone addiction is rising among teenagers.",
        s6="Early results from these schools are encouraging."))
    a(R(s, 20, "rpm3", PQRS, [
        "Residents donated old books and a few steel shelves.",
        "Volunteers arranged the books on these shelves by subject.",
        "They also kept a register so that anyone could borrow a book for a week.",
        "Within a month, more than two hundred people had borrowed books."],
        "RSPQ", "A-B B-C D$",
        "S6 begins 'Such a response', so the part it refers to — {D}, two hundred borrowers — must be last. Working back: {C}'s 'They also' refers to the volunteers in {B}, and {B}'s 'these shelves' refers to {A}. {ANS}.",
        "Start from S6: 'Such a response' = the borrowers, then chain back through 'They also' and 'these shelves'.", "medium", 45,
        s1="Our colony started a small library in an empty garage.",
        s6="Such a response has encouraged the colony to open a reading corner for children."))
    a(R(s, 21, "rpm3", PQRS, [
        "Two men entered the shop wearing helmets.",
        "While one threatened the owner, the other filled a bag with gold chains.",
        "A camera across the road recorded their faces as they removed the helmets outside.",
        "The police sent these pictures to every airport and railway station."],
        "QPSR", "A-B C-D B<C D$",
        "S6 says the thieves were caught at an airport, which refers back to {D}, the police alert to airports. {D}'s 'these pictures' needs the camera in {C}. {B}'s 'one ... the other' needs the two men of {A}. The robbery happens before they walk out, so {B} comes before {C}. {ANS}.",
        "S6 (airport) -> alert part last; 'these pictures' and 'one ... the other' give two pairs.", "medium", 45,
        s1="Last month, a jewellery shop in our town was robbed.",
        s6="The thieves were caught boarding a flight a week later."))
    a(R(s, 22, "rpm4", PQRS, [
        "Its route runs for over 700 km along the western coast.",
        "Along the way, it passes through more than 90 tunnels.",
        "The longest of these tunnels is over 6 km long.",
        "Monsoon journeys on the line are especially popular with tourists."],
        "SRPQ", "A-B B-C D$",
        "{A}'s 'Its route' can only point to the railway line in S1, so it comes first. {B}'s 'Along the way' needs that route, and {C}'s 'these tunnels' needs {B}. S6's 'then' means during the monsoon, so {D} sits just before it. {ANS}.",
        "S1 hook 'Its route' opens; 'these tunnels' pairs; S6's 'then' pulls the monsoon part last.", "easy", 40,
        s1="The Konkan Railway is one of India's most scenic railway lines.",
        s6="Waterfalls then appear beside the track at almost every bend."))
    a(R(s, 23, "rpm4", PQRS, [
        "They do so because the shallow salt marshes are full of tiny shrimp and algae.",
        "This food is what gives the birds their famous pink colour.",
        "The birds also build mud-mound nests on the flat islands of the Rann.",
        "Because of this, the region is often called 'Flamingo City'."],
        "PSQR", "^A A-B C-D",
        "'They do so' repeats S1's action (flying to the Rann), so {A} must come first. {B}'s 'This food' is the shrimp and algae of {A}. {C} adds a second fact with 'also', and {D}'s 'Because of this' — the nesting colony — names the place, so {C}{D} is a pair. {ANS}.",
        "'They do so' is an S1 hook; then two pairs: food and nests.", "hard", 50,
        s1="Every winter, thousands of flamingos fly to the Rann of Kutch.",
        s6="Bird-watchers arrive in large numbers to see the colony."))
    a(R(s, 24, "rpm5", PQRS, [
        "He designed a bamboo house that stands on stilts above the water level.",
        "Because the bamboo is grown locally, each house costs very little.",
        "Its low cost soon attracted the attention of the state government.",
        "The government has now ordered five hundred such houses for riverside villages."],
        "RQSP", "A-B B-C C-D",
        "Every part points back to the one before it: 'He' = the engineer in S1 ({A}); 'the bamboo' = {A}'s bamboo house ({B}); 'Its low cost' = {B}'s cheap houses ({C}); 'The government' = the state government in {C} ({D}). A chain of three pairs fixes the whole order. {ANS}.",
        "Pointer chain: He -> the bamboo -> Its low cost -> The government.", "medium", 45,
        s1="A young engineer in Assam wanted to build cheap houses for flood-hit families.",
        s6="Families moving in say they no longer fear the monsoon."))
    a(R(s, 25, "rpm5", PQRS, [
        "A Delhi start-up now collects these clothes from homes.",
        "It sorts them into those that can be worn again and those that cannot.",
        "The wearable ones are washed and given to families in need.",
        "The rest are shredded and woven into floor mats."],
        "SPRQ", "A-B B-C C-D D$",
        "{B}'s 'It' is the start-up in {A}. {B} makes two groups, and {C} ('The wearable ones') and {D} ('The rest') take them in order — 'the rest' only makes sense after the first group is mentioned. S6's 'These mats' refers to {D}, so it is last. {ANS}.",
        "'It' pair + 'the wearable ones ... the rest' pair; S6's 'These mats' confirms the end.", "hard", 50,
        s1="Indian households throw away tonnes of old clothes every year.",
        s6="These mats are sold to pay for the whole operation."))

    # ---------------- rearr-openers-closers ----------------
    s = "rearr-openers-closers"
    a(R(s, 16, "roc1", PQRS, [
        "A Class 8 student displayed a robot that sorts dry and wet waste.",
        "It picked up plastic bottles and dropped them into the blue bin.",
        "Watching this, the chief guest asked her how long it had taken to build.",
        "She replied that it had taken her three months of weekends."],
        "QRPS", "^A A-B B-C C-D",
        "Orphan test: {B} ('It'), {C} ('Watching this') and {D} ('She replied') all point back to something not in S1. Only {A} introduces a new noun, so it opens. Then 'It' = the robot, 'this' = the sorting, 'She replied' = the answer to the guest's question. {ANS}.",
        "Three pronoun parts fail the orphan test; the part with 'A Class 8 student' opens.", "easy", 40,
        s1="The annual science fair opened in our school hall on Friday.",
        s6="The robot won the first prize."))
    a(R(s, 17, "roc1", PQRS, [
        "A large elephant was standing on the tracks ahead.",
        "The driver sounded the horn several times, but it refused to move.",
        "Only then did we notice that its calf was stuck between the rails.",
        "Forest guards arrived and gently freed the little one."],
        "RSQP", "A-B B-C C-D",
        "{A} introduces the elephant, so it passes the orphan test and opens. {B}'s 'it refused' needs the elephant. {C}'s 'Only then' needs the failed horn in {B}. {D}'s 'the little one' is the calf in {C}. {ANS}.",
        "New noun opens; 'Only then' follows the failed attempt; 'the little one' = the calf.", "medium", 45,
        s1="Our train stopped suddenly in the middle of a forest.",
        s6="Mother and calf walked slowly back into the trees, and the train moved on."))
    a(R(s, 18, "roc1", PQRS, [
        "A retired teacher refused to accept this.",
        "She collected signatures from over three thousand residents.",
        "Their petition reached the district collector within a week.",
        "He ordered that the building be repaired instead."],
        "SQPR", "A-B B-C C-D",
        "{A}'s 'this' is the planned demolition in S1, so it passes the orphan test. {B}'s 'She' is the teacher, {C}'s 'Their petition' is the residents' signatures, and {D}'s 'He' is the collector. Each part points back to the one before it. {ANS}.",
        "'this' pointing to S1 is allowed; She -> Their -> He chain follows.", "medium", 45,
        s1="The old library in our town was about to be demolished.",
        s6="Today the library is busier than ever."))
    a(R(s, 19, "roc2", PQRS, [
        "However, this belief is only partly true.",
        "The body, in fact, needs the healthy fats found in nuts and fish.",
        "What it does not need is the excess sugar in sweets and soft drinks.",
        "A sensible diet should therefore cut sugar rather than fat."],
        "QSRP", "^A B-C D$",
        "'This belief' is S1's claim, so the However part {A} follows S1 directly. {C}'s 'What it does not need' contrasts with {B}'s 'needs', so they form a pair. {D}'s 'therefore' draws the conclusion, and S6's 'Such a diet' refers to it. {ANS}.",
        "A connector can open a PQRS item when it answers S1 itself.", "medium", 45,
        s1="Many people believe that eating fat makes you fat.",
        s6="Such a diet also keeps the heart healthy."))
    a(R(s, 20, "roc2", PQRS, [
        "Buyers like them because they cost very little to run.",
        "A full charge costs less than a cup of tea.",
        "Yet charging points are still hard to find outside big cities.",
        "Until this changes, many families will hesitate to switch."],
        "PRQS", "A-B C-D B<C",
        "{A} gives the reason for buying and {B} is its proof (the cheap charge), so they form a pair. 'Yet' in {C} contrasts with the whole positive case, so it follows {B} rather than S1. {D}'s 'this' is the shortage of charging points, so {C}{D} is a pair. {ANS}.",
        "Here the Yet part answers a part, not S1 — it follows the good news it contradicts.", "hard", 50,
        s1="Electric scooters are being sold in record numbers in Indian cities.",
        s6="Oil companies have now promised a charger at every petrol pump."))
    a(R(s, 21, "roc3", PQRS, [
        "Hosts often cook for far more guests than actually attend.",
        "Much of the leftover food ends up in the garbage.",
        "Meanwhile, thousands in the same city go to bed hungry.",
        "Clearly, the extra food must reach those who need it."],
        "RQPS", "A-B B<C D$",
        "{D} begins with 'Clearly' and concludes from everything before it, so it is last. {B}'s 'the leftover food' needs the extra cooking in {A}. {C}'s 'Meanwhile' contrasts hunger with the waste already described. {ANS}.",
        "'Clearly' marks the closing part; cause -> waste -> contrast before it.", "easy", 40,
        s1="Food is wasted at almost every Indian wedding.",
        s6="Several groups now collect wedding leftovers for night shelters."))
    a(R(s, 22, "roc3", PQRS, [
        "Rising temperatures melt more ice each summer than winter snow can replace.",
        "As a result, some glaciers have retreated by over a kilometre.",
        "This loss threatens the rivers that millions depend on for water.",
        "Hence, experts say, cutting emissions is now a matter of survival."],
        "SRQP", "A-B B-C D$",
        "'Hence' marks {D} as the closer. Before it: the cause {A}, 'As a result' {B}, and 'This loss' {C}, which sums up the retreat. {ANS}.",
        "Closing signal (Hence) last; cause -> result -> 'This loss' before it.", "medium", 45,
        s1="Several of India's glaciers are shrinking fast.",
        s6="Saving the glaciers will need action from every country."))
    a(R(s, 23, "roc4", PQRS, [
        "Each region has its own harvest festival and its own name for it.",
        "In Punjab, for example, farmers dance the bhangra at Baisakhi.",
        "In Tamil Nadu, on the other hand, families cook sweet pongal in new pots.",
        "Yet all these festivals share the same spirit of thanksgiving."],
        "SPQR", "^A A<B B-C D$",
        "{A} is the general claim, so it opens. {B}'s 'for example' illustrates it. {C}'s 'on the other hand' needs a first example before it. {D}'s 'all these festivals' sums up both examples. {ANS}.",
        "General first; 'for example' before 'on the other hand'; 'all these' last.", "easy", 40,
        s1="India celebrates the harvest in many different ways.",
        s6="They thank nature for a good crop and pray for the next one."))
    a(R(s, 24, "roc4", PQRS, [
        "Scientists have found that it stays busy through the night.",
        "During deep sleep, for instance, it stores the day's memories.",
        "During dream sleep, it sorts and links these memories with older ones.",
        "A good night's sleep is therefore as important for learning as study itself."],
        "QRSP", "A<B B-C D$",
        "{A} is the general finding; {B} ('for instance') gives the first specific case, and {C}'s 'these memories' needs {B}. {D}'s 'therefore' concludes, and S6's 'this' refers back to it. {ANS}.",
        "General finding -> 'for instance' -> 'these memories' -> therefore.", "medium", 45,
        s1="Sleep is not simply a time when the brain switches off.",
        s6="Students who stay up all night before an exam forget this."))

    # ---------------- rearr-mandatory-pairs ----------------
    s = "rearr-mandatory-pairs"
    a(R(s, 16, "rmp1", PQRS, [
        "She had come from a village school that had just twenty students.",
        "Such a large class made her so nervous that she hardly spoke.",
        "Our class teacher then asked Anu, the monitor, to help her settle in.",
        "The two soon became inseparable friends."],
        "PSRQ", "A-B B-C C-D",
        "'She' in {A} = Meena from S1. {B}'s 'Such a large class' contrasts with the twenty students in {A}, so the two form a pair. {C}'s 'then' is the teacher's response to her nervousness. {D}'s 'The two' needs both Meena and Anu, so it follows {C}. {ANS}.",
        "'The two' needs both names; 'Such a large class' needs the twenty students.", "easy", 40,
        s1="A new girl, Meena, joined our class in July.",
        s6="Today Meena is one of the most popular students in school."))
    a(R(s, 17, "rmp1", PQRS, [
        "After studying aeronautical engineering in Chandigarh, she moved to the United States.",
        "There she earned a doctorate and joined NASA.",
        "In 1997, she became the first woman of Indian origin to fly into space.",
        "Her second mission, in 2003, ended in tragedy when the shuttle Columbia broke up on its return."],
        "RPQS", "A-B B<C C<D",
        "'There' in {B} needs the country named in {A}, so they form a pair. Joining NASA comes before flying for it, so {B} is before {C}. 'Her second mission' needs the first flight of 1997, so {C} is before {D}. {ANS}.",
        "Place word 'There' pairs with the country; 'second mission' follows the first.", "medium", 45,
        s1="Kalpana Chawla was born in Karnal, Haryana, in 1962.",
        s6="India still remembers her as a hero."))
    a(R(s, 18, "rmp2", PQRS, [
        "He asked for some food and a place to rest for the night.",
        "The farmer shared his simple meal and gave the stranger a mat by the fire.",
        "The next morning, the traveller left a small clay pot on the doorstep.",
        "Inside the pot, the farmer found a bag of seeds and a note."],
        "SRPQ", "A-B B<C C-D",
        "'He' in {A} is the traveller from S1. {B}'s meal and mat answer {A}'s request. {C}'s 'The next morning' follows the night. {C} introduces 'a small clay pot', and {D}'s 'Inside the pot' refers back to it, so {C}{D} is an a -> the pair. {ANS}.",
        "a small clay pot -> the pot: the 'a' part comes first.", "easy", 40,
        s1="One evening, an old traveller knocked at the door of a poor farmer.",
        s6="The note said, 'Kindness, like these seeds, always grows.'"))
    a(R(s, 19, "rmp2", PQRS, [
        "It came with a rusty chain and a torn seat.",
        "A mechanic nearby replaced the chain for fifty rupees.",
        "The seat was harder to fix, so my mother stitched a new cover for it.",
        "By evening, the bicycle looked almost new."],
        "RQSP", "A<B A<C B-C D$",
        "{A} introduces 'a rusty chain and a torn seat'. {B}'s 'the chain' and {C}'s 'The seat' refer back to it. {C}'s 'harder' compares with the easy chain repair, so {B}{C} is a pair. {D}'s 'By evening' sums up the day's work. {ANS}.",
        "a chain / a seat -> the chain / the seat; 'harder' compares with the part before it.", "medium", 45,
        s1="Last Sunday, my father brought home a second-hand bicycle.",
        s6="My sister took the first ride around the colony."))
    a(R(s, 20, "rmp3", PQRS, [
        "The old drains of the city were built for far less rain.",
        "This problem gets worse when plastic waste blocks them.",
        "To tackle this, the city now cleans its main drains every May.",
        "This effort has reduced waterlogging at several spots."],
        "QPRS", "A-B B-C C-D",
        "A chain of 'this' words: {B}'s 'This problem' = the undersized drains of {A}; {C}'s 'To tackle this' = the blocked drains of {B}; {D}'s 'This effort' = the cleaning in {C}. {ANS}.",
        "this problem -> this -> this effort: each sums up the part before it.", "medium", 45,
        s1="Every monsoon, many Mumbai streets flood within hours.",
        s6="Experts, however, say the drains themselves must be rebuilt."))
    a(R(s, 21, "rmp3", PQRS, [
        "This trend is strongest in small towns, not just in the big cities.",
        "Cheap internet has made it possible to sell across the country from there.",
        "Government schemes also offer loans without security to first-time founders.",
        "These two factors have together created thousands of new businesses."],
        "SQRP", "^A A-B B<C D$",
        "{A}'s 'This trend' is S1's trend, so it comes first. {B}'s 'from there' = the small towns in {A}. {C}'s 'also' makes it a second factor, so it follows {B}. {D}'s 'These two factors' needs both {B} and {C}, so it is last. {ANS}.",
        "'These two factors' can only come after both factors; 'also' marks the second.", "hard", 50,
        s1="Many young Indians are choosing to start their own businesses.",
        s6="Many of them now employ people from their own towns."))
    a(R(s, 22, "rmp4", PQRS, [
        "People now take hundreds of photographs on a single trip.",
        "Yet very few of these pictures are ever looked at again.",
        "Most stay buried in the phone until it is full or lost.",
        "Printing a few favourite photos, therefore, may be the best way to keep memories alive."],
        "PQSR", "A-B B-C D$",
        "{B}'s 'Yet ... these pictures' contradicts the huge number in {A}, so they form a contrast pair. {C}'s 'Most' continues from the pictures that are never seen again. {D}'s 'therefore' concludes. {ANS}.",
        "Yet + these pictures follows the claim it contradicts.", "medium", 45,
        s1="Smartphones have put a camera in almost every pocket.",
        s6="An album on the shelf is still opened far more often than a phone gallery."))
    a(R(s, 23, "rmp4", PQRS, [
        "But their careless use is now making them less effective.",
        "Many patients stop the course as soon as they feel better.",
        "The bacteria that survive then multiply and become resistant.",
        "Such resistant infections kill more than a million people worldwide every year."],
        "RSQP", "A-B B-C C-D",
        "{A}'s 'But their careless use' contrasts with S1's claim that antibiotics save lives, so it follows S1 directly. {B} is an example of careless use. {C}'s 'The bacteria that survive' are those left when the course is stopped early. {D}'s 'Such resistant infections' needs {C}. {ANS}.",
        "The 'But' part answers S1 here; then example -> surviving bacteria -> such infections.", "hard", 50,
        s1="Antibiotics have saved millions of lives since the 1940s.",
        s6="Doctors therefore urge patients to finish every course they begin."))

    # ---------------- rearr-time-sequence ----------------
    s = "rearr-time-sequence"
    a(R(s, 16, "rts1", PQRS, [
        "It was launched from Sriharikota in November 2013.",
        "Ten months later, in September 2014, it entered orbit around Mars.",
        "India thus became the first country to reach Mars on its very first attempt.",
        "The orbiter kept sending pictures for nearly eight years, until contact was lost in 2022."],
        "PSRQ", "A<B B-C D$",
        "The dates run 2013 -> 2014 -> 2022. 'Ten months later' in {B} needs the launch in {A}. 'thus' in {C} draws the result of reaching orbit, so it follows {B}. S6's 'a mission planned to last just six months' comments on {D}'s eight years, so {D} is last. {ANS}.",
        "Dates in order; 'Ten months later' anchors to the launch; 'thus' follows success.", "easy", 40,
        s1="India's Mars Orbiter Mission is remembered as a triumph of low-cost engineering.",
        s6="Not bad for a mission that was planned to last just six months."))
    a(R(s, 17, "rts1", PQRS, [
        "In the dressing room, the coach told us to stop panicking and pass the ball more.",
        "Within ten minutes of the restart, our captain headed in a corner.",
        "Twenty minutes later, our youngest player levelled the score at 2-2.",
        "The winning goal came in the very last minute of the match."],
        "SPRQ", "A<B B-C C<D",
        "Half-time talk {A} comes before 'the restart' in {B}. 'Twenty minutes later' in {C} counts from {B}'s goal (1-2 -> 2-2). The winner {D} comes last in the match. {ANS}.",
        "Relative markers need an anchor: restart after the dressing room, 'twenty minutes later' after the first goal.", "medium", 45,
        s1="At half-time, our school football team was trailing 0-2 in the district final.",
        s6="By the final whistle, the whole school was on the field celebrating."))
    a(R(s, 18, "rts2", PQRS, [
        "Within hours, hundreds of trucks and cars were stuck near Zojila pass.",
        "Army teams reached the stranded travellers that evening with blankets and hot food.",
        "By Wednesday morning, snowploughs had cleared a single lane.",
        "Later that day, the vehicles were escorted slowly down to Sonamarg."],
        "QPSR", "A<B B<C C-D",
        "Tuesday afternoon (S1) -> within hours {A} -> that evening {B} -> 'By Wednesday morning' {C}, which sums up the night's clearing -> 'Later that day' {D}, which needs Wednesday. {ANS}.",
        "The by-phrase sums up the night's work; 'Later that day' anchors to Wednesday.", "medium", 45,
        s1="Heavy snow began falling on the Srinagar-Leh highway on Tuesday afternoon.",
        s6="The highway was fully reopened only after a week."))
    a(R(s, 19, "rts2", PQRS, [
        "By 5 o'clock, the hall was full of parents.",
        "At 5.30, just as the lights were being tested, the power went off.",
        "For the next forty minutes, teachers searched the neighbourhood for a generator.",
        "By the time the lights came back on, the audience had been waiting for over an hour."],
        "RSQP", "A<B B-C C<D",
        "The clock runs 5.00 {A} -> 5.30 {B}. 'For the next forty minutes' in {C} counts from the power cut in {B}. {D}'s by-phrase sums up the whole wait — from 5 o'clock to after 6 — so it comes after the search. {ANS}.",
        "Two by-phrases: the first sets the scene, the second sums up the wait and comes last.", "hard", 50,
        s1="The school's annual day was to begin at 6 p.m.",
        s6="The children, however, performed so well that nobody complained."))
    a(R(s, 20, "rts3", PQRS, [
        "Her bus had broken down halfway to the city.",
        "She had waited twenty minutes for another one before giving up.",
        "She had then run the last two kilometres in the rain.",
        "Seeing her soaked and breathless, the invigilator let her in with a warning."],
        "SQPR", "A-B B-C D$",
        "S1 sets the scene in the simple past. {A}, {B} and {C} are a past-perfect flashback explaining why she was late: breakdown -> 'another one' (bus) -> 'then' ran. {D} returns to the simple past and the main story, and S6 follows it. {ANS}.",
        "Past-perfect parts form the flashback; the simple-past part resumes the story.", "medium", 45,
        s1="When Meera reached the examination hall, the doors had already closed.",
        s6="She finished the paper with five minutes to spare."))
    a(R(s, 21, "rts3", PQRS, [
        "A British engineer had built it in 1890 to guard ships from the rocks.",
        "For over a century, its keepers had lit the lamp every evening.",
        "Then, in 2005, satellite navigation made the light unnecessary.",
        "Today, it serves as a small museum for tourists."],
        "PSQR", "A<B B-C D$",
        "Tense acts as a clock. 'had built' {A} is the earliest event, and 'had lit' for a century {B} follows the building. 'Then, in 2005' {C} ends that period. The present tense in {D} ('Today') is last. {ANS}.",
        "Past perfect -> simple past -> present: the tenses run in the order of the events.", "hard", 50,
        s1="The old lighthouse at the end of our beach no longer shines.",
        s6="Visitors can climb its 120 steps for a view of the whole coast."))
    a(R(s, 22, "rts4", PQRS, [
        "First, boil water with crushed ginger and cardamom.",
        "Next, add the tea leaves and let them simmer for two minutes.",
        "Once the water turns dark brown, pour in the milk and sugar.",
        "Finally, strain the tea into cups."],
        "RQPS", "^A A<B B<C D$",
        "'First' {A} and 'Finally' {D} fix the ends. {C}'s 'Once the water turns dark brown' needs the tea leaves from {B}. {ANS}.",
        "First/Finally fix the ends; the colour change needs the tea leaves.", "easy", 35,
        s1="Making a cup of masala tea is simple.",
        s6="Serve it hot with biscuits."))
    a(R(s, 23, "rts4", PQRS, [
        "First, the applicant downloads the bank's app and enters her mobile number.",
        "An OTP sent to that number confirms her identity.",
        "She then uploads photos of her PAN card and Aadhaar card.",
        "Once the documents are checked, a short video call with a bank officer completes the process."],
        "QSRP", "^A A-B C-D",
        "'First' {A} opens, and {B}'s 'that number' needs the number entered in {A}. {D}'s 'the documents' are the cards uploaded in {C}, so {C}{D} is a pair. Each step needs the one before it. {ANS}.",
        "Step dependencies: number -> OTP; upload -> documents checked.", "medium", 45,
        s1="Opening a savings account online now takes about fifteen minutes.",
        s6="The account number arrives by SMS the same day."))

    # ---------------- rearr-strategy ----------------
    s = "rearr-strategy"
    a(R(s, 1, "rst1", JUMBLE, [
        "The Sundarbans is the largest mangrove forest in the world.",
        "It is also the only mangrove forest that is home to tigers.",
        "These tigers have learnt to swim between the islands.",
        "Rising sea levels, however, are now swallowing the islands they depend on."],
        "RPSQ", "^A A-B B-C C-D",
        "Only {A} needs nothing before it — it names the Sundarbans. {B}'s 'It is also' refers to it, {C}'s 'These tigers' refers to {B}, and {D}'s 'they' and 'the islands' refer to {C}. {ANS}.",
        "No fixed ends: the one independent sentence opens, then follow the pointers.", "easy", 40))
    a(R(s, 2, "rst1", JUMBLE, [
        "Libraries were once places only for silent reading.",
        "Many have now become busy community centres.",
        "Children attend storytelling sessions there on weekends.",
        "Adults, too, use their free computers to apply for jobs."],
        "QSPR", "^A A-B B<C C<D",
        "{A} is the only independent sentence. {B}'s 'Many' refers to the libraries and 'now' contrasts with 'once'. {C}'s 'there' needs the centres. {D}'s 'too' adds a second group, so it follows the children. {ANS}.",
        "Independent sentence first; 'too' marks the second of two examples.", "medium", 45))
    a(R(s, 3, "rst1", JUMBLE, [
        "For centuries, sailors used the stars to find their way at sea.",
        "The compass, which came later, made this far easier.",
        "Today, satellites tell a ship its exact position to within a few metres.",
        "Yet many navy officers are still trained to read the stars in case the satellite signal fails."],
        "SRQP", "A-B C-D B<C",
        "{B}'s 'this' is the navigation described in {A}, and 'which came later' places the compass after the stars. 'Today' in {C} comes after both older methods. {D}'s 'Yet' and 'the satellite signal' need {C}, so it ends the paragraph — the date-like 'Today' is not the ending here. {ANS}.",
        "Older -> later -> Today -> Yet: the contrast part closes.", "hard", 50))
    a(R(s, 4, "rst2", FIRST, [
        "A young boy got off the bus at the village stop one evening.",
        "He was carrying a small bag and looked lost.",
        "The shopkeeper nearby asked him whom he was looking for.",
        "The boy replied that he had come to find his grandfather."],
        "QPRS", "A-B B<C C-D",
        "Orphan test: 'He', 'asked him' and 'The boy replied' all point back to someone already introduced. Only {A} introduces 'A young boy', so it is first. Full order: {ANS}.",
        "The sentence with 'a' + new noun passes the orphan test.", "easy", 30))
    a(R(s, 5, "rst2", FIRST, [
        "The banyan is India's national tree.",
        "Its roots grow down from the branches and look like extra trunks.",
        "Over time, these hanging roots can spread a single tree over several acres.",
        "The Great Banyan near Kolkata, for example, looks like a small forest from a distance."],
        "RPQS", "A-B B-C C-D",
        "'Its roots', 'these hanging roots' and 'for example' all depend on an earlier sentence. {A} names the banyan and needs nothing before it, so it comes first. Full order: {ANS}.",
        "Pointers (Its, these, for example) rule out three sentences.", "medium", 35))
    a(R(s, 6, "rst2", FIRST, [
        "Festivals in India are often tied to rivers and the sea.",
        "In Bengal, for instance, Durga idols are immersed in the river at the end of the festival.",
        "Kerala's boat races, similarly, draw crowds of thousands every August.",
        "Boats with over a hundred rowers race to the beat of songs."],
        "QRPS", "A-B B<C C-D",
        "Two sentences look independent: the general claim {A} and the Kerala sentence {C}. But {C} contains 'similarly', so it needs an earlier example, and the Bengal sentence's 'for instance' needs the general claim before it. The general sentence {A} is first. Full order: {ANS}.",
        "When two sentences look independent, check for hidden pointers (similarly) — the general claim wins.", "hard", 45))
    a(R(s, 7, "rst3", LAST, [
        "A miser once sold everything he owned and bought a lump of gold.",
        "He buried it in a hole beside his garden wall.",
        "Every night he dug it up just to look at it.",
        "One day a thief, who had been watching him, stole the gold."],
        "QPRS", "A-B B<C C<D",
        "The story runs buy -> bury -> dig up nightly -> theft. {D}'s thief 'had been watching him' dig, so it comes after the nightly digging, and no sentence points back to the theft. {D} is last. Full order: {ANS}.",
        "The sentence that points back to all the others and is pointed to by none is last.", "easy", 30))
    a(R(s, 8, "rst3", LAST, [
        "Most of us blame factories and farms for India's water crisis.",
        "Yet a surprising amount of water is lost inside our own homes.",
        "A single dripping tap, for example, can waste thousands of litres a year.",
        "Clearly, the key to saving water lies in fixing these small leaks at home."],
        "RQSP", "A-B B-C C-D",
        "{D} begins with 'Clearly' and its 'these small leaks' needs the dripping tap in {C}, so it sums up the paragraph and is last. Full order: {ANS}.",
        "Conclusion signal + 'these' pointer = the last sentence.", "medium", 35))
    a(R(s, 9, "rst3", LAST, [
        "A student once asked his teacher how he could become wise.",
        "The teacher asked him in turn, 'Do you know that you know very little?'",
        "The student admitted that he knew almost nothing.",
        "'Then you have already taken the first step,' replied the teacher."],
        "SQRP", "A-B B-C C-D",
        "The dialogue runs question {A} -> counter-question {B} -> admission {C} -> reply {D}. The admission sounds like an ending, but the teacher's 'Then you have already taken the first step' answers it, so the reply {D} is last. Full order: {ANS}.",
        "In a dialogue, the last line answers the one before it — do not stop at the first line that sounds final.", "medium", 40))
    a(R(s, 10, "rst4", PQRS, [
        "Even a roadside vegetable seller now displays a QR code.",
        "Customers simply scan it and pay in seconds.",
        "This has reduced the need to carry cash or look for change.",
        "But it has also made people spend more freely than before."],
        "QSRP", "A-B B-C C-D",
        "{B}'s 'it' is the QR code in {A}, and {C}'s 'This' is paying by scanning. If you are left with two strings that differ only in the order of {C} and {D}, test that link: 'But it has also' needs a benefit before it, so {C} comes before {D}. {ANS}.",
        "When two strings survive, test only the swapped pair: 'But ... also' follows the benefit.", "medium", 45,
        s1="UPI has changed the way Indians pay for everyday things.",
        s6="Many now check their bank balance only at the end of the month."))
    a(R(s, 11, "rst4", PQRS, [
        "Workers first covered the heap with thick layers of clay and soil.",
        "On this new surface they planted grass and hundreds of saplings.",
        "Within three years, the saplings had grown into a small forest.",
        "Birds that had not been seen in the area for decades began to return."],
        "PSRQ", "A-B B-C C-D",
        "'this new surface' in {B} is the soil layer of {A}. 'the saplings' in {C} were planted in {B}. The birds in {D} return to the forest, so {D} follows {C}. The nearest wrong strings swap two neighbouring parts; each swap breaks one of these pointers. {ANS}.",
        "Check the one link that the surviving strings disagree on.", "medium", 45,
        s1="The city decided to turn an old rubbish dump into a park.",
        s6="The park now draws walkers every morning."))
    a(R(s, 12, "rst4", JUMBLE, [
        "Honeybees and other pollinators help produce about a third of the food we eat.",
        "Their numbers, however, have been falling sharply in many countries.",
        "Pesticides and the loss of wild flowers are the main reasons for this decline.",
        "Farmers who plant flowering hedges around their fields are helping to reverse it."],
        "SPQR", "A-B B-C C-D",
        "{A} is the only independent sentence. 'Their numbers' in {B} refers to the pollinators, 'this decline' in {C} is the falling numbers, and 'reverse it' in {D} needs the decline. {ANS}.",
        "Independent sentence, then Their -> this decline -> it.", "easy", 40))
    return it
