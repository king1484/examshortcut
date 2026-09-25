# Notes + per-subtopic patterns for idioms-phrases (Phase 2 deep content).
S = {}


def P(id, name, freq, spot, logic, eq, es):
    return {"id": id, "name": name, "frequency": freq, "howToSpot": spot, "formula": None, "logic": logic,
            "example": {"q": eq, "solution": es}}


S["idiom-literal-trap"] = {
"notes": """### What an idiom is
An **idiom** is a group of words whose meaning is different from the meaning of the single words. *He let the cat out of the bag* has nothing to do with a cat or a bag. It means *he told a secret by mistake*. The words paint a picture; the idiom means what that picture stands for.

Think of the Hindi saying *naach na jaane aangan tedha* — nobody is talking about a crooked courtyard. The meaning is *blaming others for your own lack of skill*. English idioms work the same way.

### How the exam sets the trap
In SSC, Railway and Banking papers, an idiom question gives one idiom and four meanings. The wrong options are built in three standard ways:
1. **The literal option** — it repeats the actual words: *to smell a rat* → 'to smell a dead rat'.
2. **The neighbour option** — a figurative meaning that sounds close but is not the real one: *to turn a deaf ear* → 'to hear badly'.
3. **The opposite or random option** — a meaning from a different idiom, or the reverse sense.

Only one option gives the accepted, dictionary meaning.

### The four-step method
1. **Kill the literal.** If you could take a photo of what the option says, it is almost always wrong. *To break the ice* → 'to crack frozen water' is out at once.
2. **Find the picture.** Ask what the image shows. A cat escaping from a bag → something hidden comes out → a secret is revealed.
3. **Check the tone.** Is the idiom happy, sad, angry, or neutral? *In hot water* is trouble, not danger of death. Pick the option with the same strength.
4. **Plug it back.** Put the option into a small sentence in place of the idiom. *'The minister's plan ended in smoke'* → *'The plan came to nothing'* sounds right; *'The plan caused a fire'* does not.

### Idioms that look alike (pairs)
Many idioms share a word but have totally different meanings. Examiners love to put one member of the pair as the wrong option for the other.

| Idiom | Meaning | Look-alike | Its meaning |
|---|---|---|---|
| spill the beans | tell a secret | cry over spilt milk | regret what cannot be changed |
| once in a blue moon | very rarely | a bolt from the blue | a sudden shock |
| smell a rat | suspect a trick | the rat race | a tiring fight for success |
| in a nutshell | in brief | in a pickle | in a difficult situation |

Learn each pair together on one card. Then the planted twin cannot fool you.

### Idiom inside a sentence
Sometimes the idiom is placed in a sentence, and you choose its meaning. Use the sentence as a clue. *Meena was on cloud nine after the result* — the result is good news, so the meaning must be happy (*extremely happy*), not 'flying' or 'confused'.

### When you do not know the idiom
- Remove the literal options first.
- Judge the tone from the key word (*cold, dark, hot* often mean trouble; *cloud nine, red-letter* mean joy).
- Choose the option that fits a sentence you can imagine.

### Quick revision
- Idiom = fixed picture; meaning = what the picture stands for.
- Wrong options: literal, neighbour, opposite.
- Method: kill literal → find picture → check tone → plug back.
- Learn look-alike idioms in pairs.
- In a sentence, let the situation decide the meaning.
""",
"patterns": [
 P("il-p1", "Meaning of a common idiom with a literal decoy", "very common",
   "One idiom stands alone after 'Select the most appropriate meaning of the given idiom'. At least one option simply repeats the words of the idiom.",
   "1. Cross out every option you could photograph (the literal one).\n2. Say what the picture stands for in one abstract word (escape → reveal, towel thrown → give up).\n3. Pick the option that matches that word.\n\n*Why it works:* the examiner always plants the literal reading, and the real meaning is never literal.",
   "Select the most appropriate meaning of the idiom: *To let the cat out of the bag*",
   "The picture: something hidden gets out. Options about pets or bags are literal. Meaning: **to reveal a secret carelessly**."),
 P("il-p2", "Idiom used inside a sentence", "common",
   "A full sentence contains the idiom (often in bold or quotes); you must choose what it means in that sentence.",
   "1. Read the whole sentence and note whether the situation is good or bad news.\n2. Remove options that clash with the situation.\n3. Replace the idiom with each survivor; keep the one that reads naturally.\n\n*Why it works:* the sentence was written to support only the true meaning.",
   "*The plan for a new bridge is still **in the pipeline**.* What does the idiom mean?",
   "A plan 'still' in some stage → not finished. Meaning: **being planned or prepared**. 'Inside a water pipe' is the literal decoy."),
 P("il-p3", "Close figurative trap (choose the exact meaning)", "common",
   "Two or more options are figurative, not literal. One is the real meaning, another sounds related but changes the sense or strength.",
   "1. Recall the exact action in the idiom (bury = put away for ever; hatchet = weapon of the fight).\n2. Ask which option states that action's result.\n3. Reject options that are stronger, weaker or only loosely linked.\n\n*Why it works:* the neighbour option borrows one word's feeling but not the whole picture.",
   "Meaning of *To keep one's fingers crossed*: (a) to hope for good luck (b) to be sure of success (c) to hide one's hands (d) to make a promise",
   "Crossing fingers is a hope sign, not a guarantee. 'Sure of success' overshoots. Answer: **(a) to hope for good luck**."),
 P("il-p4", "Look-alike idiom pairs", "occasional",
   "The options contain the meaning of a different idiom that shares a key word (beans/milk, blue moon/blue bolt, rat/rat race).",
   "1. Notice the shared word in the stem.\n2. Recall its twin idiom and the twin's meaning.\n3. Cross out the twin's meaning; choose the one that fits the stem idiom.\n\n*Why it works:* examiners reuse the twin's meaning because it 'feels' familiar.",
   "Meaning of *In a nutshell*: (a) in trouble (b) in brief (c) inside a hard shell (d) in secret",
   "'In a pickle' means in trouble — that is the twin trap. *In a nutshell* = **(b) in brief**."),
],
}

S["idiom-animal-body"] = {
"notes": """### Why animals and body parts
A large share of the idioms asked in competitive exams use an **animal** or a **part of the body**. This is good news: each animal and each body part has a fixed 'character', so you can often work out the meaning even if you half-remember the idiom.

### Animal characters
| Animal | Stands for | Example idiom | Meaning |
|---|---|---|---|
| bull | facing force head-on | take the bull by the horns | face a problem boldly |
| rat | cheating, trickery | smell a rat | suspect something wrong |
| crocodile | false tears | crocodile tears | pretended sorrow |
| horse | speed, hurry | hold your horses | wait, be patient |
| wolf | hunger, danger | keep the wolf from the door | avoid starving |
| birds | targets | kill two birds with one stone | get two results from one action |
| lion | biggest, strongest | the lion's share | the largest part |
| goose | foolish effort | a wild-goose chase | a useless search |

Worked use: *Crocodile tears*. The old belief was that crocodiles 'cry' while eating. So the tears are not real → **pretended sorrow**.

### Body-part functions
| Part | Function | Example idiom | Meaning |
|---|---|---|---|
| ear | listening | turn a deaf ear | refuse to listen |
| eye | watching, agreeing | see eye to eye | agree fully |
| nose | price paid | pay through the nose | pay far too much |
| shoulder | welcome | give the cold shoulder | treat coldly, ignore |
| neck | risk | stick one's neck out | take a risk by acting boldly |
| feet | courage | get cold feet | lose courage at the last moment |
| hand | help, work | lend a hand / have one's hands full | help / be very busy |
| foot | firmness | put one's foot down | take a firm stand |
| heart | fear, feeling | heart in one's mouth | very nervous |

Worked use: *He stuck his neck out for his friend.* Neck = risk. So he **took a risk** to support his friend.

### Question types you will see
1. **Meaning of an animal idiom** — use the animal's character.
2. **Meaning of a body idiom** — use the body part's job.
3. **Idiom in a sentence** — the sentence tells you if it is good or bad.
4. **Reverse type** — a meaning is given; you choose the idiom. Here the wrong options are real idioms with other meanings, so you must know which idiom matches which job (hand = help, hands full = busy, wash hands = refuse duty).

### Traps to avoid
- *Pull someone's leg* is playful teasing, not hurting someone.
- *Cold shoulder* is not an illness.
- *Smell a rat* (suspect) is not *the rat race* (tough competition).
- *Heart in one's mouth* is fear, not love.
- *Wash one's hands of* means refusing further responsibility, not cleanliness.

### Quick revision
- Animal = character: bull (bold), rat (trick), crocodile (fake), wolf (hunger), horse (hurry).
- Body = function: ear (listen), eye (agree/watch), neck (risk), feet (courage), hand (help/busy).
- Reverse questions: match the meaning to the body part's job first.
- Keep separate cards for idioms whose picture is hard to see (cold shoulder, crocodile tears).
""",
"patterns": [
 P("iab-p1", "Meaning of an animal idiom", "very common",
   "The idiom names an animal or bird: bull, rat, crocodile, wolf, horse, birds, goose, lion.",
   "1. Recall the animal's stock character (bull = force, crocodile = fake, birds = targets).\n2. Add the verb of the idiom to that character.\n3. Choose the option that states the result in plain words.\n\n*Why it works:* animal idioms are built on the same fixed characters again and again.",
   "Meaning of *Hold your horses*: (a) to ride carefully (b) to wait and be patient (c) to own many animals (d) to hurry up",
   "Horses = hurry; holding them back = slowing down. Answer: **(b) to wait and be patient**. 'Hurry up' is the opposite."),
 P("iab-p2", "Meaning of a body-part idiom", "very common",
   "The idiom names a body part: ear, eye, nose, shoulder, neck, feet, hand, heart.",
   "1. Name the body part's job (ear = listen, hand = help).\n2. Read the idiom's action on that job.\n3. Reject options about injury or illness — they are literal.\n\n*Why it works:* each body part keeps one job across most idioms.",
   "Meaning of *To lend a hand*: (a) to give a loan (b) to help (c) to shake hands (d) to hurt someone",
   "Hand = help. Lending it = giving help. Answer: **(b) to help**."),
 P("iab-p3", "Animal or body idiom inside a sentence", "common",
   "A sentence contains the idiom; the question asks its meaning in context.",
   "1. Decide from the sentence whether the idiom is positive or negative.\n2. Apply the animal character or body function.\n3. Put the answer back in the sentence to check.\n\n*Why it works:* the context removes any option with the wrong tone.",
   "*When the results were announced, my heart was in my mouth.* The idiom means:",
   "Waiting for results → tension. Heart = feeling. Answer: **I was very nervous**."),
 P("iab-p4", "Choose the idiom for a given meaning", "common",
   "The stem gives a meaning ('to be extremely busy') and the options are four idioms, usually from the same body part.",
   "1. Recall the meaning of each option idiom quickly.\n2. Match the exact meaning, not just the body part.\n3. Beware of options using the same word with a different job.\n\n*Why it works:* all four options are real idioms, so only exact knowledge separates them.",
   "Select the idiom that means *to take a firm stand*: (a) to put one's foot down (b) to follow in someone's footsteps (c) to get cold feet (d) to put one's best foot forward",
   "Foot down = firmness. Answer: **(a) to put one's foot down**. 'Best foot forward' = try one's best; 'cold feet' = lose courage."),
],
}

S["idiom-colour-food"] = {
"notes": """### Colours carry feelings
In English idioms each colour usually carries the same feeling. Learn the colour and you know the family of the meaning.

| Colour | Usual meaning | Idiom | Meaning |
|---|---|---|---|
| blue | unexpected, rare | out of the blue | suddenly, without warning |
| red | anger, officialdom, special day | see red / red tape / red-letter day | become angry / official delay / a day to remember |
| green | envy, jealousy | green with envy | very jealous |
| black | disgrace | a black sheep | the one who brings shame to a family |
| white | costly and useless | a white elephant | expensive to keep but of no use |
| grey | not clear | a grey area | a matter that is not clearly right or wrong |
| silver | wealth, hope | born with a silver spoon | born in a rich family |

Worked use: *The new flyover that nobody uses but costs lakhs to maintain is a white elephant.* White = costly-useless. Meaning: **a possession that costs much but gives no benefit**.

**Watch out for red.** Red has three different families. *See red* = angry. *Red tape* = too many official rules causing delay (government files were once tied with red ribbon). *Red-letter day* = a happy, important day (special days were marked in red on calendars). Examiners put these three against each other.

### Food idioms are judgements
Food idioms use something we eat to give a judgement about a task or a person.

| Idiom | Judgement | Meaning |
|---|---|---|
| a piece of cake | easy | a very easy task |
| a hard nut to crack | difficult | a difficult problem or person |
| butter someone up | flattery | praise someone to get a favour |
| food for thought | thinking | something worth thinking about |
| a hot potato | controversy | an issue everyone avoids handling |
| in a pickle | trouble | in a difficult situation |
| the apple of one's eye | love | the person loved most |
| spill the beans | secret | reveal a secret |
| the salt of the earth | goodness | a very good, honest person |
| carry coals to Newcastle | useless supply | take something where it is already plentiful |
| a storm in a teacup | fuss | a big quarrel over a small matter |

Worked use: *Maths is a piece of cake for Arjun.* Cake = easy. So maths is **very easy** for him.

### Look-alike pairs in this bank
- *The apple of one's eye* (most loved) vs *the apple of discord* (cause of a quarrel).
- *A piece of cake* (easy) vs *a hot potato* (a touchy issue).
- *Red tape* (delay) vs *red-letter day* (happy day).
- *Born with a silver spoon* (rich from birth) vs *every cloud has a silver lining* (some good in every bad situation).

### Fill-in-the-blank use
Sometimes a sentence has a blank and four idioms as options. First decide what the sentence needs: a useless thing? a small fuss? a happy day? Then pick the idiom from that family. Check grammar too — *was ___ for her family* needs a noun phrase such as *a red-letter day*.

### Quick revision
- Blue = sudden/rare; red = anger, delay or a special day; green = envy; black = shame; white = costly-useless; grey = unclear.
- Food = judgement: cake easy, nut hard, butter flatter, potato touchy, pickle trouble, apple loved.
- Learn the look-alike pairs together.
- In blanks, decide the need first, then the family, then check grammar.
""",
"patterns": [
 P("icf-p1", "Meaning of a colour idiom", "very common",
   "The idiom contains a colour word: blue, red, green, black, white, grey, silver.",
   "1. Recall the colour's usual feeling (blue = sudden, green = envy).\n2. Read the rest of the idiom to choose inside that family.\n3. Reject options that treat the colour literally (paint, clothes, sky).\n\n*Why it works:* colour idioms share stable associations across English.",
   "Meaning of *Out of the blue*: (a) from the sky (b) suddenly and unexpectedly (c) very sad (d) far away",
   "Blue = unexpected. Answer: **(b) suddenly and unexpectedly**. 'From the sky' is the literal decoy."),
 P("icf-p2", "Meaning of a food idiom", "very common",
   "The idiom names a food item: cake, nut, butter, potato, pickle, beans, milk, apple, salt.",
   "1. Turn the food into a judgement (cake = easy, nut = hard).\n2. Pick the option with that judgement.\n3. Drop options about cooking, eating or prices.\n\n*Why it works:* food idioms always judge a task, a person or a situation.",
   "Meaning of *Food for thought*: (a) a healthy diet (b) something worth thinking about (c) a free meal (d) a boring lecture",
   "The 'food' feeds the mind. Answer: **(b) something worth thinking about**."),
 P("icf-p3", "Colour or food idiom with a look-alike twin", "common",
   "One option is the meaning of a twin idiom sharing the colour or food word (red tape vs red-letter day; apple of one's eye vs apple of discord).",
   "1. Spot the shared word.\n2. Recall both twins and their meanings.\n3. Choose the meaning of the stem idiom only.\n\n*Why it works:* the twin's meaning is planted because it feels familiar.",
   "Meaning of *Born with a silver spoon in one's mouth*: (a) hopeful in hard times (b) born in a rich family (c) fond of good food (d) very talkative",
   "'Hopeful in hard times' is the twin (silver lining). Answer: **(b) born in a rich family**."),
 P("icf-p4", "Fill the blank with a colour or food idiom", "common",
   "A sentence with a blank; four idioms as options.",
   "1. Decide what the blank needs (a useless thing, a fuss, a happy day, a useless supply).\n2. Pick the idiom from that meaning family.\n3. Read the full sentence once to check grammar and sense.\n\n*Why it works:* the sentence is written so that only one idiom's meaning fits.",
   "*The huge statue that costs lakhs to maintain but draws no visitors has become a ___.* (a) white elephant (b) black sheep (c) red-letter day (d) piece of cake",
   "Costly + useless → **(a) white elephant**."),
],
}

S["idiom-situations-people"] = {
"notes": """### Two big groups
Most idioms in competitive exams fall into two groups:
1. **Situation idioms** — they describe what is happening: trouble, hard work, sudden events, success, defeat.
2. **People idioms** — they describe a type of person: loyal, false, weak, skilled, clever.

If you know which group and which family an idiom belongs to, the right option stands out.

### Situation families
| Family | Idioms | Meaning |
|---|---|---|
| Trouble | in hot water, in a fix, in deep waters | in serious difficulty |
| Hard effort | burn the midnight oil, leave no stone unturned, move heaven and earth | work very hard / try every way |
| Sudden | at the drop of a hat, on the spur of the moment | at once / without planning |
| Money | make both ends meet, keep the wolf from the door | manage with little income |
| Change | turn over a new leaf, turn the tables | start behaving better / reverse the position |
| Winning | carry the day, bear the palm | win |
| Losing, quitting | throw in the towel, bite the dust, take to one's heels | give up / be defeated / run away |
| Health, mood | under the weather, on cloud nine | slightly ill / extremely happy |

Worked use: *The police left no stone unturned to find the child.* Effort family → **tried every possible way**.

### People families
| Type | Idioms | Meaning |
|---|---|---|
| False friend | a snake in the grass, a fair-weather friend, a wolf in sheep's clothing | hidden enemy / friend only in good times / harmful person who looks harmless |
| Weak or unimportant | a man of straw, a cog in the machine | person of no real power |
| Reliable | a man of his word, a tower of strength | keeps promises / gives strong support |
| Many skills | a jack of all trades | does many jobs, masters none |
| Second place | play second fiddle | take a less important role |

### Idioms from stories (allusions)
Some idioms come from old stories. One line of the story fixes the meaning for ever.
- **Achilles' heel** — a Greek hero could be hurt only at his heel → a weak point.
- **Bell the cat** — the mice wanted a bell on the cat, but none dared tie it → to take a big risk for everyone.
- **Pandora's box** — opening a forbidden box let out all troubles → a source of many new problems.
- **A Herculean task** — Hercules did twelve very hard labours → a task needing huge effort.
- **Midas touch** — whatever King Midas touched became gold → the ability to make money from anything.
- **A Trojan horse** — soldiers hid inside a wooden horse gifted to Troy → something harmless-looking that harms from inside.

### Fill-in-the-blank type
Read the sentence and name the family it needs. *Seeing the police, the thief ___.* The thief wants to escape → running away → **took to his heels**. Then read the sentence again with your choice.

### Common traps
- *Steal a march on* is not stealing; it means gaining an advantage quietly.
- *Pass the buck* is not about money; it means shifting blame.
- *Play second fiddle* is not about music; it means a lower role.
- *Under the weather* is not about rain; it means slightly ill.

### Quick revision
- Name the family first: trouble, effort, sudden, money, change, win, lose, health.
- People idioms: false (snake, fair-weather), weak (straw, cog), reliable (word, tower).
- Story idioms: Achilles' heel, bell the cat, Pandora's box, Herculean, Midas touch, Trojan horse.
- In blanks, match the family the sentence needs.
""",
"patterns": [
 P("isp-p1", "Meaning of a situation idiom", "very common",
   "The idiom describes an event or condition: trouble, effort, suddenness, winning, losing, health.",
   "1. Place the idiom in its family (effort, trouble, sudden...).\n2. Reject options from other families and literal options.\n3. Pick the option that states the family meaning exactly.\n\n*Why it works:* distractors are usually taken from other families.",
   "Meaning of *By leaps and bounds*: (a) very rapidly (b) by jumping (c) with great fear (d) slowly and steadily",
   "Leaps = big fast jumps → speed. Answer: **(a) very rapidly**."),
 P("isp-p2", "Meaning of a people (character) idiom", "common",
   "The idiom names a type of person: 'a ___ friend', 'a man of ___', 'a ___ in the grass'.",
   "1. Decide whether the idiom praises or criticises the person.\n2. Recall the type: false, weak, reliable, many-skilled.\n3. Choose the option with that type.\n\n*Why it works:* people idioms are labels; the label's tone removes half the options.",
   "Meaning of *A jack of all trades*: (a) a skilled mechanic (b) one who does many kinds of work but masters none (c) a rich trader (d) a lazy worker",
   "The full saying ends 'master of none'. Answer: **(b)**."),
 P("isp-p3", "Fill the blank with the right situation idiom", "common",
   "A sentence with a blank and four idioms as options.",
   "1. Read the sentence and name what is needed (run away? lower role? try harder?).\n2. Match the family.\n3. Re-read with the chosen idiom; check tense and grammar.\n\n*Why it works:* the context supports only one meaning.",
   "*Having won one medal, the athlete did not ___; she trained even harder.* (a) rest on her laurels (b) burn her boats (c) play to the gallery (d) break the ice",
   "She kept working instead of relaxing after success → **(a) rest on her laurels** (be satisfied with past success)."),
 P("isp-p4", "Idioms from stories and legends", "occasional",
   "A proper noun or story object appears: Achilles, Pandora, Hercules, Midas, Trojan, a cat with a bell.",
   "1. Recall the one-line story.\n2. Turn the story's key point into a general meaning.\n3. Reject literal options about the story's objects.\n\n*Why it works:* the story is the meaning; options that retell it literally are wrong.",
   "Meaning of *The Midas touch*: (a) a gentle touch (b) the ability to make money from anything one does (c) a royal order (d) a golden ornament",
   "Everything Midas touched turned to gold. Answer: **(b)**."),
],
}

S["idiom-strategy"] = {
"notes": """### How idioms appear in the paper
Idioms are a small but steady part of the English section. Most papers ask one or two direct idiom questions. Idioms also hide inside cloze tests, sentence improvement and fill-in-the-blank items. The pool of idioms examiners use is small and repeats often, so a well-built list of about 300 idioms covers most of what you will see.

### The different formats
1. **Meaning of the idiom** — one idiom, four meanings. The most common.
2. **Replace the phrase** — a sentence has a plain phrase underlined; you choose the idiom that can replace it. *'They are in bitter open hostility'* → *'They are at daggers drawn'*.
3. **Complete the idiom** — one word of a fixed idiom is missing: *calls a spade a ___*. Idioms are frozen, so only the original word is correct. 'A spade a shovel' is simply wrong.
4. **Opposite meaning** — choose the option opposite to the idiom's meaning. First find the meaning, then find its opposite. The option that gives the same meaning is the trap.
5. **Idiom inside a passage** — the context gives it away.

### Idioms are frozen
You cannot change the words of an idiom. *A hard nut to crack*, never *a hard nut to break*. *Every cloud has a silver lining*, never *a golden lining*. This is why the 'complete the idiom' type has only one defensible answer. When you learn an idiom, learn its exact words.

### A 30-day plan
- **Days 1–10:** learn 10 new idioms a day. For each, make one sentence about your own life: *I burnt the midnight oil before my mock test.*
- **Days 11–20:** 10 new + revise 15 old each day. Revise by family (animals, body, colours, food, situations, people).
- **Days 21–30:** 10 new + revise 25 old + a 20-question self-test. Any idiom you get wrong twice goes on a short **weak list**. Revise that list every week.

Your own sentence is what you remember in the exam. Reading a list alone fades fast.

### In the exam hall (20 seconds per idiom)
1. Kill the literal option.
2. Find the picture and the family.
3. Check the tone: positive or negative?
4. Plug the answer back into a sentence.

If you do not know the idiom at all, judge its tone from the key words and pick the option with the same tone. This beats a blind guess.

### Opposite-meaning questions
Write the meaning in two words first. *Keep one's chin up* = stay cheerful. Now the opposite is *lose heart*. The option that says 'stay brave' has the **same** meaning and is the planted trap.

### Quick revision
| Format | First step |
|---|---|
| Meaning | Kill the literal option |
| Replace the phrase | Find the idiom with exactly that meaning |
| Complete the idiom | Recall the frozen original word |
| Opposite | Write the meaning, then reverse it |
| In a passage | Use the situation to fix the tone |

- 10 new idioms a day, one own sentence each, weekly weak list.
- Idioms are frozen: never accept a changed word.
""",
"patterns": [
 P("is-p1", "Complete the idiom (missing word)", "occasional",
   "An idiom appears with one word blanked, and the options are four similar words (spade/shovel, pie/pot).",
   "1. Recall the idiom in its exact frozen form.\n2. Say it aloud with each option; only the original sounds right.\n3. Do not pick a 'logical' synonym — idioms do not allow them.\n\n*Why it works:* an idiom is a fixed chain of words, so any substitute breaks it.",
   "Complete the idiom: *Every cloud has a silver ___.* (a) lining (b) border (c) colour (d) edge",
   "The fixed form is *every cloud has a silver lining* = there is some good in every bad situation. Answer: **(a) lining**."),
 P("is-p2", "Replace the underlined phrase with an idiom", "common",
   "A sentence has a plain-English phrase in bold or underlined; the options are idioms that could replace it.",
   "1. Restate the bold phrase in two or three words.\n2. Find the option idiom with exactly that meaning.\n3. Re-read the sentence with the idiom to check grammar.\n\n*Why it works:* only one option's meaning matches the phrase; the others are real idioms with different meanings.",
   "Replace the bold part: *The workers **were dismissed from their jobs** last week.* (a) got the sack (b) got cold feet (c) turned the tables (d) broke the ice",
   "Dismissed = lost their jobs → **(a) got the sack**."),
 P("is-p3", "Mixed-bank idiom meaning (tone check)", "common",
   "A less familiar idiom from any family, with options of different tones.",
   "1. Kill literal options.\n2. Judge the idiom's tone from its key word (upper = advantage, dogs = ruin).\n3. Pick the option with the same tone and a sensible picture.\n\n*Why it works:* even when memory fails, tone plus picture usually leaves one option.",
   "Meaning of *To be in the same boat*: (a) to travel together (b) to face the same difficulty (c) to be close friends (d) to share money",
   "Everyone in one boat sinks or floats together → shared trouble. Answer: **(b)**."),
 P("is-p4", "Opposite in meaning to an idiom", "occasional",
   "The stem asks for the option OPPOSITE in meaning to the idiom.",
   "1. Write the idiom's meaning in two words.\n2. Reverse it.\n3. Choose that option; reject the option that repeats the meaning.\n\n*Why it works:* the planted trap is the synonym of the idiom's meaning.",
   "Opposite in meaning to *To be on cloud nine*: (a) to be very happy (b) to be very sad (c) to fly high (d) to be very busy",
   "Cloud nine = very happy; opposite = **(b) to be very sad**. (a) is the same meaning, the trap."),
],
}

S["idiom-phrasal-verbs"] = {
"title": "Phrasal verbs (verb + particle phrases)",
"concept": "A **phrasal verb** is a verb joined with a small word (a particle) such as *up, off, out, in, after, down*. Together they make a new meaning: *give* + *up* = stop doing something. Idiom sections and fill-in-the-blank questions often test these phrases.",
"formulas": [],
"tricks": [
 {"title": "Particle meanings", "body": "*off* often means stop or cancel (call off, put off); *out* means finish or remove (run out, put out); *up* means complete or give up; *after* means follow or care for (look after, take after)."},
 {"title": "Same verb, four particles", "body": "When all four options share one verb (break down / out / up / in), say the sentence with each and keep the one whose meaning fits the whole sentence."},
 {"title": "One-word swap", "body": "Replace the phrasal verb with a single formal word to check it: put out = extinguish, call off = cancel, put up with = tolerate, come across = meet by chance."},
],
"mistakes": [
 "Guessing from the verb alone: *give in* (surrender) and *give up* (stop a habit) differ only in the particle.",
 "Mixing *put off* (postpone) with *put out* (extinguish).",
 "Reading *look down upon* literally as looking from a height; it means to think someone is inferior.",
 "Using *look after* (take care of) where *look into* (investigate) is needed.",
],
"notes": """### What is a phrasal verb?
A **phrasal verb** is a verb + a small word called a **particle** (up, off, out, in, on, down, after, into, over). Together they give a new meaning that you often cannot guess from the verb alone.
- *give* = hand over, but *give up* = stop doing something.
- *call* = phone or shout, but *call off* = cancel.

In competitive exams they appear in three places: the idioms-and-phrases question ('meaning of the phrase *put up with*'), fill-in-the-blank ('The meeting was put ___'), and error spotting or sentence improvement.

### What the particles usually mean
The particle is the key. These are tendencies, not strict rules, but they help a lot.

| Particle | Usual idea | Examples |
|---|---|---|
| off | stop, cancel, leave | call off (cancel), put off (postpone), take off (plane leaves the ground) |
| out | finish, remove, appear | run out of (finish), put out (extinguish), break out (start suddenly) |
| up | complete, stop, arrive | give up (stop a habit), turn up (arrive), bring up (raise a child) |
| down | reduce, fail, refuse | break down (stop working), turn down (refuse), look down upon (despise) |
| in | enter, yield | give in (surrender), hand in (submit), break in (enter by force) |
| after | follow, care | look after (take care of), take after (resemble an elder) |
| into | examine, meet | look into (investigate), run into (meet by chance) |
| over | recover, examine | get over (recover from), look over (check quickly) |

### One verb, many meanings
Examiners like to fix one verb and change the particle.

| Verb | + particle | Meaning |
|---|---|---|
| give | up / in / away / out | stop a habit / surrender / donate or reveal / distribute or run short |
| turn | down / up / out | refuse / arrive / prove to be |
| take | after / off / up | resemble / remove or leave the ground / start a hobby |
| break | down / out / in / up | stop working / start suddenly / enter by force / end a relationship |
| come | across / about | meet by chance / happen |
| put | off / out / up with | postpone / extinguish / tolerate |

Worked use: *The car broke ___ on the highway.* Cars stop working → **broke down**. *Broke out* is for war, fire or disease. *Broke in* is for thieves.

### Three-word phrasal verbs
Some phrasal verbs have two particles and must stay together: *put up with* (tolerate), *run out of* (have none left), *look down upon* (despise), *look forward to* (wait eagerly). Do not drop the second particle: 'We have run out sugar' is wrong; say 'run out **of** sugar'.

### How to answer
1. **Meaning questions:** replace the phrasal verb with a one-word meaning (cancel, tolerate, extinguish) and test it in a sentence.
2. **Particle blanks:** read the whole sentence. The subject (a car, a fire, a meeting) tells you which particle makes sense.
3. **Replace-the-word questions:** the bold word is formal (extinguish, postpone, recover); find the phrasal verb that equals it.

### Quick revision
- off = cancel/stop; out = finish/remove; up = stop/arrive; down = refuse/fail; after = care/resemble; into = investigate.
- call off = cancel; put off = postpone; put out = extinguish; put up with = tolerate.
- give up = stop a habit; give in = surrender; turn down = refuse; take after = resemble.
- break down = stop working; break out = start suddenly; come across = meet by chance; get over = recover.
""",
"patterns": [
 P("ipv-p1", "Meaning of a phrasal verb", "common",
   "A phrase like 'to call off' or 'to put up with' is given as the idiom/phrase; options are one-word or short meanings.",
   "1. Recall the particle's idea (off = stop/cancel).\n2. Replace the phrase with each option in a small sentence.\n3. Reject options that use the verb's plain meaning (call = phone).\n\n*Why it works:* the particle changes the verb's meaning, and the plain-verb option is the planted trap.",
   "Meaning of *To bring up*: (a) to lift something (b) to raise and educate a child (c) to carry upstairs (d) to arrive early",
   "*Bring up* a child = raise the child. Answer: **(b)**."),
 P("ipv-p2", "Fill in the particle", "common",
   "A sentence with a blank right after a verb; options are particles (off, on, up, out, down, in).",
   "1. Find the subject and object (a car, a fire, sugar).\n2. Say the sentence with each particle.\n3. Keep the only one that makes sense for that subject.\n\n*Why it works:* each verb + particle pair has a fixed meaning; the subject allows only one.",
   "*The students were asked to hand ___ their answer sheets.* (a) in (b) on (c) off (d) up",
   "*Hand in* = submit. Answer: **(a) in**."),
 P("ipv-p3", "Same verb, different particles", "common",
   "All four options share one verb (give up / give in / give away / give out) and a meaning is asked for.",
   "1. Recall what each particle adds to the verb.\n2. Match the given meaning exactly.\n3. Beware of a close pair (give up vs give in).\n\n*Why it works:* only the particle changes, so knowing particle ideas separates the options.",
   "Select the phrasal verb that means *to meet by chance*: (a) run into (b) run out (c) run over (d) run away",
   "*Run into* someone = meet by chance. Answer: **(a)**."),
 P("ipv-p4", "Replace a word with a phrasal verb", "common",
   "A sentence has a formal verb in bold (extinguish, recover, postpone); options are phrasal verbs.",
   "1. Keep the bold word's meaning in mind.\n2. Test each phrasal verb in its place.\n3. Watch the tense: the option must match (got over, not get over, in a past sentence).\n\n*Why it works:* each formal word has one common phrasal-verb equal.",
   "Replace the bold word: *The plane **departed** at 6 a.m.* (a) took off (b) took up (c) took after (d) took in",
   "Planes *take off* = leave the ground. Answer: **(a) took off**."),
],
}
