# New practice questions for idioms-phrases. In every item opts[0] is the correct answer;
# QA() moves it to a deterministic position. TARGET records the idiom/phrase each question asks,
# so the build script can check that no idiom is asked twice.
from _lib import QA

TARGET = {}
M = "Select the most appropriate meaning of the given idiom.\n\n"
MP = "Select the most appropriate meaning of the given phrase.\n\n"


def mk(qid, sub, pat, target, q, opts, solution, shortcut=None, diff="medium", t=30):
    TARGET[qid] = target.lower()
    return QA(qid, sub, pat, q, opts, solution, shortcut=shortcut, diff=diff, t=t)


def QS_ID():
    qs = []
    A = qs.append
    L = "idiom-literal-trap"
    # ---- il-p1: meaning with literal decoy
    A(mk("idiom-literal-trap-p01", L, "il-p1", "break the ice", M + "To break the ice",
         ["to start a conversation among people who feel shy or stiff", "to melt ice for drinking water",
          "to end a long friendship", "to win a difficult contest"],
         "*Break the ice* = to get people talking and relaxed in a new or awkward group. 'Melt ice' is the literal decoy; the other two have nothing to do with the picture.",
         "Ice = stiffness between strangers; breaking it = starting talk.", "easy", 20))
    A(mk("idiom-literal-trap-p02", L, "il-p1", "throw in the towel", M + "To throw in the towel",
         ["to admit defeat and give up", "to clean up after a game", "to start a fight", "to change one's clothes"],
         "In boxing, a towel thrown into the ring stops the fight. So *throw in the towel* = **admit defeat and give up**. The cleaning and clothes options are literal.",
         "Towel thrown → fight stops → give up.", "medium", 20))
    A(mk("idiom-literal-trap-p03", L, "il-p1", "face the music", M + "To face the music",
         ["to accept the unpleasant results of one's own actions", "to attend a music concert",
          "to enjoy loud music", "to run away from punishment"],
         "*Face the music* = to accept criticism or punishment for what one has done. The concert and loud-music options are literal; 'run away from punishment' is the opposite.",
         "Kill the two music options; the opposite is the last trap.", "easy", 25))
    # ---- il-p2: idiom inside a sentence
    A(mk("idiom-literal-trap-p04", L, "il-p2", "turn over a new leaf",
         "Select the most appropriate meaning of the idiom in bold.\n\nAfter failing twice, Ravi decided to **turn over a new leaf** and study every day.",
         ["to start behaving in a better way", "to start reading a new book", "to plant a new tree", "to change his school"],
         "The sentence shows Ravi changing his habits after failure. *Turn over a new leaf* = **start a better way of behaving**. Book, tree and school options take 'leaf' literally or guess.",
         "Leaf = page of life; a new page = a fresh, better start.", "easy", 25))
    A(mk("idiom-literal-trap-p05", L, "il-p2", "end in smoke",
         "Select the most appropriate meaning of the idiom in bold.\n\nThe minister's promise of free laptops **ended in smoke**.",
         ["came to nothing", "caused a big fire", "was widely praised", "was kept on time"],
         "*End in smoke* = to come to nothing after much talk or effort. 'Caused a fire' is literal; 'kept on time' is the opposite.",
         "Smoke disappears → nothing is left.", "medium", 25))
    A(mk("idiom-literal-trap-p06", L, "il-p2", "on cloud nine",
         "Select the most appropriate meaning of the idiom in bold.\n\nMeena was **on cloud nine** when she cleared the exam.",
         ["extremely happy", "travelling by aeroplane", "very confused", "slightly worried"],
         "Clearing an exam is good news, so the meaning must be positive. *On cloud nine* = **extremely happy**.",
         "Good-news sentence → pick the only happy option.", "easy", 20))
    # ---- il-p3: close figurative trap
    A(mk("idiom-literal-trap-p07", L, "il-p3", "bury the hatchet", M + "To bury the hatchet",
         ["to make peace after a quarrel", "to hide a weapon in the ground", "to start a new quarrel", "to keep a secret safely"],
         "A hatchet (small axe) stands for the fight; burying it ends the fight. So *bury the hatchet* = **make peace**. 'Keep a secret' borrows the idea of burying but not the fight; 'start a quarrel' is the reverse.",
         "Weapon put away for ever = peace.", "medium", 25))
    A(mk("idiom-literal-trap-p08", L, "il-p3", "get cold feet", M + "To get cold feet",
         ["to become too nervous to do something one had planned", "to catch a cold in winter",
          "to feel lonely", "to become very lazy"],
         "*Get cold feet* = to lose courage just before doing something planned (a speech, a wedding, a jump). Laziness and loneliness are different feelings; the cold option is literal.",
         "Feet = courage to step forward; cold feet = courage fails.", "medium", 25))
    A(mk("idiom-literal-trap-p09", L, "il-p3", "sit on the fence", M + "To sit on the fence",
         ["to avoid taking sides in a dispute", "to rest after hard work", "to guard one's property", "to be very careless"],
         "A fence divides two fields; sitting on it means not stepping into either. *Sit on the fence* = **avoid taking sides**.",
         "On the fence = in neither camp.", "medium", 25))
    # ---- il-p4: look-alike pairs
    A(mk("idiom-literal-trap-p10", L, "il-p4", "cry over spilt milk", M + "To cry over spilt milk",
         ["to regret something that cannot be undone", "to reveal a secret", "to waste food carelessly", "to complain about high prices"],
         "*Cry over spilt milk* = to feel useless regret about what is already done. 'Reveal a secret' is the meaning of its look-alike *spill the beans* — the planted twin.",
         "Spilt MILK = regret; spill the BEANS = secret.", "medium", 25))
    A(mk("idiom-literal-trap-p11", L, "il-p4", "a bolt from the blue", M + "A bolt from the blue",
         ["a sudden and completely unexpected event", "something that happens very rarely",
          "a flash of lightning", "a blue-coloured object"],
         "*A bolt from the blue* = a shock that comes without any warning (like lightning from a clear sky). 'Very rarely' is the meaning of the twin *once in a blue moon*.",
         "BOLT = sudden shock; blue MOON = rare.", "hard", 25))
    A(mk("idiom-literal-trap-p12", L, "il-p4", "the rat race", M + "The rat race",
         ["a tiring and endless struggle for success in modern life", "to suspect that something is wrong",
          "a race run by animals", "a slow and relaxed life"],
         "*The rat race* = the endless competition for money and position, especially in city jobs. 'Suspect that something is wrong' belongs to the twin *smell a rat*.",
         "Rat RACE = competition; SMELL a rat = suspicion.", "hard", 30))

    B = "idiom-animal-body"
    # ---- iab-p1: animal idioms
    A(mk("idiom-animal-body-p01", B, "iab-p1", "take the bull by the horns", M + "To take the bull by the horns",
         ["to face a difficult situation boldly", "to tame a wild animal", "to run away from danger", "to argue foolishly"],
         "Grabbing a charging bull by its horns means facing the danger directly. Meaning: **deal with a difficulty boldly**. 'Run away' is the opposite; 'tame an animal' is literal.",
         "Bull = force head-on.", "easy", 20))
    A(mk("idiom-animal-body-p02", B, "iab-p1", "crocodile tears", M + "Crocodile tears",
         ["sorrow that is only pretended", "tears of great joy", "the tears of a wild animal", "deep and lasting grief"],
         "Crocodiles were believed to shed tears while eating their prey, so the tears were false. *Crocodile tears* = **pretended sorrow**. 'Deep grief' is the opposite (real sorrow).",
         "Crocodile = fake.", "easy", 20))
    A(mk("idiom-animal-body-p03", B, "iab-p1", "kill two birds with one stone", M + "To kill two birds with one stone",
         ["to achieve two aims with a single action", "to hunt with great skill", "to make two mistakes at once", "to punish two people together"],
         "One stone, two results. Meaning: **get two things done with one effort**. Example: going to the bank on the way to office.",
         "Birds = targets; one stone = one action.", "medium", 20))
    # ---- iab-p2: body-part idioms
    A(mk("idiom-animal-body-p04", B, "iab-p2", "give the cold shoulder", M + "To give someone the cold shoulder",
         ["to treat someone in a deliberately unfriendly way", "to suffer from a chill", "to give someone firm support",
          "to push someone away with force"],
         "Shoulder = welcome; a cold one = an unfriendly welcome. Meaning: **to ignore or treat someone coldly on purpose**. 'Firm support' confuses it with *a shoulder to lean on*.",
         "Cold = unfriendly, not illness.", "medium", 25))
    A(mk("idiom-animal-body-p05", B, "iab-p2", "pay through the nose", M + "To pay through the nose",
         ["to pay far more than the fair price", "to pay in cash", "to breathe with difficulty", "to pay one's bills on time"],
         "*Pay through the nose* = to be charged much too much. Example: buying water at an airport. The breathing option is literal.",
         "Nose idiom about money = paying too much.", "medium", 25))
    # ---- iab-p3: in a sentence
    A(mk("idiom-animal-body-p06", B, "iab-p3", "see eye to eye",
         "Select the most appropriate meaning of the idiom in bold.\n\nThe two brothers never **see eye to eye** on money matters.",
         ["agree with each other", "meet each other", "look at each other", "talk openly with each other"],
         "*See eye to eye* = to agree fully. 'Never see eye to eye' = they always disagree about money. 'Look at each other' is literal.",
         "Eye to eye = same view = agreement.", "easy", 20))
    A(mk("idiom-animal-body-p07", B, "iab-p3", "stick one's neck out",
         "Select the most appropriate meaning of the idiom in bold.\n\nWhen the boss asked who would take charge of the failing project, only Anil **stuck his neck out**.",
         ["took a risk by coming forward boldly", "looked around nervously", "hurt his neck", "refused to help"],
         "Neck = risk. *Stick one's neck out* = to take a risk by saying or doing something bold. Anil volunteered for a risky job.",
         "Neck out = exposed to danger = risk.", "medium", 25))
    # ---- iab-p4: choose the idiom for a meaning
    A(mk("idiom-animal-body-p08", B, "iab-p4", "have one's hands full",
         "Select the idiom that means *to be extremely busy*.",
         ["to have one's hands full", "to lend a hand", "to wash one's hands of", "to try one's hand at"],
         "*Have one's hands full* = be very busy. *Lend a hand* = help; *wash one's hands of* = refuse further responsibility; *try one's hand at* = attempt something new.",
         "Full hands = no free hand = busy.", "medium", 25))
    A(mk("idiom-animal-body-p09", B, "iab-p4", "wash one's hands of",
         "Select the idiom that means *to refuse to take any further responsibility for something*.",
         ["to wash one's hands of", "to put one's foot down", "to keep at arm's length", "to follow in someone's footsteps"],
         "*Wash one's hands of* a matter = declare you are no longer responsible for it. *Put one's foot down* = take a firm stand; *keep at arm's length* = avoid closeness; *follow in someone's footsteps* = do as an elder did.",
         "Washing hands = removing oneself from the matter.", "hard", 30))

    C = "idiom-colour-food"
    # ---- icf-p1: colour idioms
    A(mk("idiom-colour-food-p01", C, "icf-p1", "a black sheep", M + "A black sheep",
         ["a member who brings disgrace to the family or group", "a rare and costly animal", "a very shy person", "the youngest child in a family"],
         "Black = disgrace. *A black sheep* is the member whose conduct shames the family or group.",
         "Black = shame.", "easy", 20))
    A(mk("idiom-colour-food-p02", C, "icf-p1", "green with envy", M + "Green with envy",
         ["very jealous", "new to a job and inexperienced", "fond of nature", "rich and happy"],
         "Green = envy, so *green with envy* = **very jealous**. 'Inexperienced' is a different use of green (a greenhorn), not this idiom.",
         "Green + envy = jealousy.", "easy", 20))
    A(mk("idiom-colour-food-p03", C, "icf-p1", "see red", M + "To see red",
         ["to become suddenly very angry", "to notice danger ahead", "to feel ashamed", "to celebrate a victory"],
         "Red = anger here. *See red* = to lose one's temper suddenly. 'Notice danger' treats red as a signal light.",
         "Red eyes of rage → anger.", "medium", 25))
    # ---- icf-p2: food idioms
    A(mk("idiom-colour-food-p04", C, "icf-p2", "a piece of cake", M + "A piece of cake",
         ["something very easy to do", "a small reward", "a birthday gift", "a tiny share of profit"],
         "Cake = easy. *A piece of cake* = a task that needs almost no effort.",
         "Cake = easy.", "medium", 20))
    A(mk("idiom-colour-food-p05", C, "icf-p2", "a hard nut to crack", M + "A hard nut to crack",
         ["a difficult problem or a person hard to deal with", "a strong and healthy body", "a costly dry fruit", "a rude remark"],
         "Nut = hard to open. *A hard nut to crack* = a problem that is difficult to solve or a person who is difficult to handle.",
         "Nut = stubborn difficulty.", "easy", 20))
    A(mk("idiom-colour-food-p06", C, "icf-p2", "butter someone up", M + "To butter someone up",
         ["to flatter someone to win a favour", "to feed someone well", "to scold someone politely", "to help someone secretly"],
         "Butter makes things smooth. *Butter someone up* = to praise someone too much so that they will do you a favour.",
         "Butter = flattery.", "medium", 25))
    # ---- icf-p3: look-alike twins
    A(mk("idiom-colour-food-p07", C, "icf-p3", "red tape", M + "Red tape",
         ["too many official rules that cause delay", "a day worth remembering", "a danger signal", "a ribbon cut at an opening ceremony"],
         "Government files were once tied with red tape, and getting them moved was slow. *Red tape* = **official delay caused by rules**. 'A day worth remembering' is the twin *red-letter day*; the ribbon is literal.",
         "Red TAPE = delay; red-LETTER day = happy day.", "hard", 25))
    A(mk("idiom-colour-food-p08", C, "icf-p3", "the apple of one's eye", M + "The apple of one's eye",
         ["a person who is loved most", "a cause of quarrel", "a person with sharp eyesight", "a fruit seller's best fruit"],
         "*The apple of one's eye* = the person someone loves and cherishes most. 'A cause of quarrel' is the twin *apple of discord*.",
         "Apple of EYE = love; apple of DISCORD = quarrel.", "hard", 25))
    A(mk("idiom-colour-food-p09", C, "icf-p3", "a hot potato", M + "A hot potato",
         ["a sensitive issue that people avoid dealing with", "a tasty snack", "a very easy task", "a cheap bargain"],
         "A hot potato is too hot to hold, so everyone passes it on. *A hot potato* = **a touchy issue nobody wants to handle**. 'A very easy task' is the food twin *a piece of cake*.",
         "Potato = touchy issue; cake = easy.", "medium", 25))
    # ---- icf-p4: fill the blank
    A(mk("idiom-colour-food-p10", C, "icf-p4", "carry coals to newcastle",
         "Select the most appropriate idiom to fill in the blank.\n\nTaking sand to the Thar Desert to sell is like ___.",
         ["carrying coals to Newcastle", "setting the Thames on fire", "crying over spilt milk", "a storm in a teacup"],
         "Newcastle was famous for coal, so taking coal there is pointless. The desert already has endless sand → **carrying coals to Newcastle** = taking something to a place that already has plenty.",
         "Place already full of the thing → coals to Newcastle.", "medium", 30))
    A(mk("idiom-colour-food-p11", C, "icf-p4", "a storm in a teacup",
         "Select the most appropriate idiom to fill in the blank.\n\nThe quarrel over the window seat was just ___; the two friends were laughing together five minutes later.",
         ["a storm in a teacup", "a bolt from the blue", "a red-letter day", "a white elephant"],
         "A big fuss over a small matter that ends quickly = **a storm in a teacup**.",
         "Big fuss + tiny cause = storm in a teacup.", "medium", 30))
    A(mk("idiom-colour-food-p12", C, "icf-p4", "a red-letter day",
         "Select the most appropriate idiom to fill in the blank.\n\nThe day Priya received her appointment letter was ___ for the whole family.",
         ["a red-letter day", "a grey area", "a hot potato", "a black sheep"],
         "A joyful, memorable day = **a red-letter day** (special days were marked in red on calendars). The others do not describe a day.",
         "Memorable day = red-letter day.", "easy", 25))

    D = "idiom-situations-people"
    # ---- isp-p1: situation idioms
    A(mk("idiom-situations-people-p01", D, "isp-p1", "leave no stone unturned", M + "To leave no stone unturned",
         ["to try every possible means", "to search a rocky place", "to be careless in one's work", "to destroy everything"],
         "Turning every stone = searching everywhere. *Leave no stone unturned* = **make every possible effort**. 'Careless' is the opposite.",
         "Effort family.", "medium", 20))
    A(mk("idiom-situations-people-p02", D, "isp-p1", "under the weather", M + "Under the weather",
         ["slightly ill", "caught in a storm", "very rich", "out of danger"],
         "*Under the weather* = feeling a little unwell. The storm option is literal.",
         "Health family: under the weather = not well.", "easy", 20))
    A(mk("idiom-situations-people-p03", D, "isp-p1", "turn the tables", M + "To turn the tables",
         ["to reverse a situation and gain the upper hand over an opponent", "to rearrange the furniture",
          "to cheat in a game of cards", "to lose badly"],
         "*Turn the tables* = to change a losing position into a winning one against someone. 'Lose badly' is the opposite; furniture is literal.",
         "Tables turned = positions swapped.", "hard", 25))
    # ---- isp-p2: people idioms
    A(mk("idiom-situations-people-p04", D, "isp-p2", "a fair-weather friend", M + "A fair-weather friend",
         ["a friend who stays only in good times", "a friend who loves travelling", "a loyal friend in all situations", "a weather reporter"],
         "Fair weather = good times. A *fair-weather friend* disappears when trouble comes. 'A loyal friend' is the opposite.",
         "Fair weather only → not loyal.", "easy", 20))
    A(mk("idiom-situations-people-p05", D, "isp-p2", "a snake in the grass", M + "A snake in the grass",
         ["a hidden enemy who pretends to be a friend", "a dangerous wild animal", "a shy person", "a lazy worker"],
         "A snake hidden in grass strikes without warning. *A snake in the grass* = **a treacherous person who hides behind friendship**.",
         "Hidden + harmful = traitor.", "medium", 25))
    A(mk("idiom-situations-people-p06", D, "isp-p2", "a man of straw", M + "A man of straw",
         ["a person of no real importance or strength", "a farmer", "a person with a strong will", "a scarecrow"],
         "Straw is light and weak. *A man of straw* = a weak person with no real substance or power. 'Scarecrow' is literal; 'strong will' is the opposite.",
         "Straw = weak, empty.", "hard", 25))
    # ---- isp-p3: fill the blank
    A(mk("idiom-situations-people-p07", D, "isp-p3", "play second fiddle",
         "Select the most appropriate idiom to fill in the blank.\n\nTired of ___ to his elder brother in the family business, Karan started his own shop.",
         ["playing second fiddle", "carrying the day", "resting on his laurels", "taking to his heels"],
         "Karan was unhappy with a lower role → **playing second fiddle** (taking a less important position). The others mean winning, being satisfied with past success, and running away.",
         "Lower role = second fiddle.", "medium", 30))
    A(mk("idiom-situations-people-p08", D, "isp-p3", "take to one's heels",
         "Select the most appropriate idiom to fill in the blank.\n\nSeeing the police van, the pickpocket ___.",
         ["took to his heels", "broke the ice", "kept his chin up", "turned a deaf ear"],
         "A thief who sees the police runs away → **took to his heels** (ran away fast).",
         "Escape = take to one's heels.", "easy", 25))
    # ---- isp-p4: story idioms
    A(mk("idiom-situations-people-p09", D, "isp-p4", "bell the cat", M + "To bell the cat",
         ["to take a great risk for the good of others", "to tie a bell on a pet", "to warn everyone loudly", "to trap a thief"],
         "In the fable, the mice wanted a bell on the cat but nobody dared to tie it. *Bell the cat* = **to face the danger that others fear, for everyone's benefit**.",
         "Fable of the mice → the brave, risky job.", "medium", 25))
    A(mk("idiom-situations-people-p10", D, "isp-p4", "a herculean task", "Select the most appropriate meaning of the given phrase.\n\nA Herculean task",
         ["a task that needs very great effort", "a task that is very easy", "an order given by a king", "a sports competition"],
         "Hercules, the hero of Greek stories, did twelve extremely hard labours. *A Herculean task* = **a job needing enormous strength or effort**.",
         "Hercules = huge effort.", "easy", 20))
    A(mk("idiom-situations-people-p11", D, "isp-p4", "pandora's box", M + "To open Pandora's box",
         ["to start something that causes many unexpected problems", "to open a box of gifts", "to find a hidden treasure", "to solve a mystery"],
         "In the Greek story, Pandora opened a forbidden box and let all kinds of troubles into the world. *Open Pandora's box* = **start something that leads to many new problems**.",
         "Pandora = troubles let loose.", "hard", 30))

    E = "idiom-strategy"
    # ---- is-p1: complete the idiom
    A(mk("idiom-strategy-p01", E, "is-p1", "call a spade a spade",
         "Select the most appropriate word to complete the idiom.\n\nRahul does not believe in hiding the truth; he always calls a spade a ___.",
         ["spade", "shovel", "tool", "spoon"],
         "The fixed idiom is *call a spade a spade* = to speak plainly and honestly. Idioms are frozen: 'a spade a shovel' is not the idiom.",
         "Frozen form: the word repeats.", "easy", 20))
    A(mk("idiom-strategy-p02", E, "is-p1", "a finger in every pie",
         "Select the most appropriate word to complete the idiom.\n\nThe new supervisor likes to have a finger in every ___.",
         ["pie", "pot", "plate", "cake"],
         "The fixed idiom is *have a finger in every pie* = to be involved in (or meddle in) many matters.",
         "Recall the frozen chain: finger → every pie.", "medium", 25))
    A(mk("idiom-strategy-p03", E, "is-p1", "count one's chickens before they hatch",
         "Select the most appropriate word to complete the idiom.\n\nDon't count your chickens before they ___; the result is not out yet.",
         ["hatch", "grow", "sleep", "run"],
         "The fixed idiom is *don't count your chickens before they hatch* = don't depend on a gain before it is certain.",
         "Chickens come from eggs → hatch.", "easy", 20))
    # ---- is-p2: replace the phrase with an idiom
    A(mk("idiom-strategy-p04", E, "is-p2", "at daggers drawn",
         "Select the idiom that can replace the words in bold.\n\nThe two neighbours have been **openly and bitterly hostile to each other** for years.",
         ["at daggers drawn", "at sixes and sevens", "on cloud nine", "at a loose end"],
         "*At daggers drawn* = in open, bitter enmity. *At sixes and sevens* = in confusion; *on cloud nine* = very happy; *at a loose end* = having nothing to do.",
         "Weapons out = open hostility.", "medium", 30))
    A(mk("idiom-strategy-p05", E, "is-p2", "not mince matters",
         "Select the option that can replace the words in bold.\n\nPriya **always speaks plainly, without softening her words**.",
         ["never minces matters", "always beats about the bush", "always sits on the fence", "never pulls her weight"],
         "*Not mince matters (or words)* = to speak frankly without softening. *Beat about the bush* is the opposite; *sit on the fence* = avoid taking sides; *pull one's weight* = do one's fair share of work.",
         "Mince = cut small = soften; never mince = speak plainly.", "hard", 30))
    A(mk("idiom-strategy-p06", E, "is-p2", "carry the day",
         "Select the idiom that can replace the words in bold.\n\nIn the final debate, Aman's argument **won and was accepted by everyone**.",
         ["carried the day", "fell flat", "missed the bus", "went to the dogs"],
         "*Carry the day* = to win or be successful. *Fall flat* = fail to have the intended effect; *miss the bus* = lose an opportunity; *go to the dogs* = be ruined.",
         "Won = carried the day.", "medium", 25))
    # ---- is-p3: mixed-bank tone check
    A(mk("idiom-strategy-p07", E, "is-p3", "have the upper hand", M + "To have the upper hand",
         ["to have control or an advantage", "to be taller than others", "to raise one's hand to ask", "to be in a weak position"],
         "Upper = above the other. *Have the upper hand* = to be in control or in a stronger position. 'Weak position' is the opposite.",
         "Upper = stronger.", "easy", 20))
    A(mk("idiom-strategy-p08", E, "is-p3", "at sixes and sevens", M + "At sixes and sevens",
         ["in total confusion or disorder", "good at arithmetic", "thirteen years old", "in perfect order"],
         "*At sixes and sevens* = in a state of confusion or disorder. The number options are literal; 'perfect order' is the opposite.",
         "Numbers in an idiom are never literal.", "hard", 25))
    A(mk("idiom-strategy-p09", E, "is-p3", "go to the dogs", M + "To go to the dogs",
         ["to be ruined or become much worse", "to take care of pets", "to go for a morning walk", "to improve greatly"],
         "*Go to the dogs* = to decline badly or be ruined (a business, a person, a place). 'Improve greatly' is the opposite.",
         "Negative tone: dogs here = ruin.", "medium", 25))
    # ---- is-p4: opposite of the idiom
    A(mk("idiom-strategy-p10", E, "is-p4", "keep one's chin up",
         "Select the option that is OPPOSITE in meaning to the given idiom.\n\nTo keep one's chin up",
         ["to lose heart", "to stay cheerful in difficulty", "to look upward", "to shave carefully"],
         "*Keep one's chin up* = stay brave and cheerful in hard times. Its opposite is **to lose heart**. 'Stay cheerful' is the same meaning (the trap).",
         "Write the meaning (stay brave), then reverse it.", "medium", 25))
    A(mk("idiom-strategy-p11", E, "is-p4", "blow hot and cold",
         "Select the option that is OPPOSITE in meaning to the given idiom.\n\nTo blow hot and cold",
         ["to hold the same opinion firmly", "to keep changing one's opinion", "to fall ill with fever", "to cook food"],
         "*Blow hot and cold* = to keep changing one's mind, to be unsteady. Opposite: **to hold one opinion firmly**. 'Keep changing one's opinion' is the same meaning.",
         "Hot then cold = changing; opposite = steady.", "hard", 30))
    A(mk("idiom-strategy-p12", E, "is-p4", "in someone's good books",
         "Select the option that is OPPOSITE in meaning to the given idiom.\n\nTo be in someone's good books",
         ["to be out of favour with someone", "to be liked by someone", "to read many books", "to own a library"],
         "*Be in someone's good books* = to be in their favour. Opposite: **out of favour** with them. 'Liked by someone' repeats the meaning.",
         "Favour ↔ out of favour.", "medium", 25))

    F = "idiom-phrasal-verbs"
    # ---- ipv-p1: meaning
    A(mk("idiom-phrasal-verbs-p01", F, "ipv-p1", "call off", MP + "To call off",
         ["to cancel", "to telephone someone", "to shout loudly", "to invite a guest"],
         "*Call off* = cancel: *The match was called off because of rain.* The phone and shouting options use the plain verb *call*.",
         "off = stop/cancel.", "easy", 20))
    A(mk("idiom-phrasal-verbs-p02", F, "ipv-p1", "put up with", MP + "To put up with",
         ["to tolerate", "to raise something higher", "to build a house", "to agree to marry"],
         "*Put up with* = to bear or tolerate something unpleasant: *I cannot put up with this noise.*",
         "Three-word phrasal verb = tolerate.", "easy", 20))
    A(mk("idiom-phrasal-verbs-p03", F, "ipv-p1", "look down upon", MP + "To look down upon",
         ["to regard someone as inferior", "to look from a height", "to search carefully", "to respect someone"],
         "*Look down upon* = to think that someone is less important than oneself. 'Respect' is the opposite; 'from a height' is literal.",
         "down = lower status.", "medium", 25))
    # ---- ipv-p2: fill the particle
    A(mk("idiom-phrasal-verbs-p04", F, "ipv-p2", "run out of",
         "Select the most appropriate option to fill in the blank.\n\nWe have run ___ of sugar; please buy some on your way home.",
         ["out", "off", "over", "into"],
         "*Run out of* = to have no more left. Only *out* forms this phrase with *of*.",
         "Nothing left → run out of.", "easy", 20))
    A(mk("idiom-phrasal-verbs-p05", F, "ipv-p2", "break down",
         "Select the most appropriate option to fill in the blank.\n\nOur car broke ___ on the highway, so we had to wait for a mechanic.",
         ["down", "out", "up", "in"],
         "A machine that stops working *breaks down*. *Break out* is for war, fire or disease; *break up* ends a relationship; *break in* is forced entry.",
         "Machines break down.", "easy", 20))
    A(mk("idiom-phrasal-verbs-p06", F, "ipv-p2", "look into",
         "Select the most appropriate option to fill in the blank.\n\nThe police have promised to look ___ the complaint and find out the truth.",
         ["into", "up", "out", "down"],
         "*Look into* = to investigate. 'Find out the truth' confirms investigation.",
         "Investigate = look into.", "medium", 25))
    # ---- ipv-p3: same verb, different particles
    A(mk("idiom-phrasal-verbs-p07", F, "ipv-p3", "give up",
         "Select the phrasal verb that means *to stop a habit*.",
         ["give up", "give in", "give out", "give away"],
         "*Give up* smoking = stop the habit. *Give in* = surrender; *give out* = distribute or stop working; *give away* = donate or reveal.",
         "up = stop for good.", "medium", 25))
    A(mk("idiom-phrasal-verbs-p08", F, "ipv-p3", "turn down",
         "Select the phrasal verb that means *to refuse an offer or request*.",
         ["turn down", "turn up", "turn out", "turn over"],
         "*Turn down* an offer = refuse it. *Turn up* = arrive; *turn out* = prove to be; *turn over* = flip, or hand over.",
         "down = refuse.", "medium", 25))
    A(mk("idiom-phrasal-verbs-p09", F, "ipv-p3", "take after",
         "Select the phrasal verb that means *to look or behave like an older family member*.",
         ["take after", "take off", "take up", "take in"],
         "*She takes after her mother* = she resembles her mother. *Take off* = remove or leave the ground; *take up* = start a hobby or job; *take in* = deceive or absorb.",
         "after = follow an elder.", "hard", 25))
    # ---- ipv-p4: replace a word with a phrasal verb
    A(mk("idiom-phrasal-verbs-p10", F, "ipv-p4", "put out",
         "Select the phrasal verb that can replace the word in bold.\n\nThe fire brigade managed to **extinguish** the fire within an hour.",
         ["put out", "put off", "put on", "put up"],
         "*Put out* a fire = extinguish it. *Put off* = postpone; *put on* = wear or switch on; *put up* = raise or stay.",
         "out = end it.", "medium", 25))
    A(mk("idiom-phrasal-verbs-p11", F, "ipv-p4", "get over",
         "Select the phrasal verb that can replace the words in bold.\n\nMy grandfather **recovered from** his illness quickly.",
         ["got over", "got through", "got along", "got off"],
         "*Get over* an illness = recover from it. *Get through* = pass or finish; *get along* = be friendly with; *get off* = leave a bus or escape punishment.",
         "Recover = get over.", "medium", 25))
    A(mk("idiom-phrasal-verbs-p12", F, "ipv-p4", "come across",
         "Select the phrasal verb that can replace the words in bold.\n\nRamesh **happened to meet** an old school friend at the railway station.",
         ["came across", "came about", "came off", "came out"],
         "*Come across* = meet or find by chance. *Come about* = happen; *come off* = succeed or become detached; *come out* = appear or be published.",
         "By chance = come across.", "hard", 30))
    return qs
