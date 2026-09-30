"""Readable rewrite: English > Idioms & Phrases (6 subtopics). Idempotent. Run with Python312."""
import sys
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parent))
from _rd_common import pat, mis, trick, sub, apply  # noqa: E402

SUBS = {}

# ---------------------------------------------------------------- 1. literal trap
SUBS["idiom-literal-trap"] = sub(
    concept=("An idiom is a fixed group of words whose meaning is not the meaning of the separate words. "
             "The words paint a picture, and the meaning is what the picture stands for. "
             "The exam always plants a literal option, so cross it out first."),
    notes=r"""
### What an idiom is
An **idiom** is a group of words with a meaning that is different from its single words.

*He let the cat out of the bag.* This has nothing to do with a cat or a bag. It means he told a secret by mistake.

The words paint a picture. The idiom means what that picture stands for.

### How wrong options are built
An idiom question gives one idiom and four meanings. The wrong options come in three kinds.
1. **The literal option.** It repeats the actual words: *smell a rat* becomes "to smell a dead rat".
2. **The neighbour option.** A figurative meaning that sounds close but is not right: *turn a deaf ear* becomes "to hear badly".
3. **The opposite or random option.** It has the reverse sense or belongs to another idiom.

Only one option gives the accepted meaning.

### The four-step method
1. **Kill the literal.** If you could take a photo of what the option says, it is almost always wrong. *Break the ice* does not mean to crack frozen water.
2. **Find the picture.** A cat escapes from a bag. Something hidden comes out. So a secret is revealed.
3. **Check the tone.** Is the idiom happy, sad, angry or neutral? *In hot water* means trouble, not danger of death.
4. **Plug it back.** Put the option into a small sentence. *The plan ended in smoke* becomes *the plan came to nothing*. That sounds right.

> **Rule:** If an option can be pictured physically, cross it out first.

### Idioms that look alike
Many idioms share a word but mean different things. Examiners put one twin in the options for the other.
| Idiom | Meaning | Look-alike | Its meaning |
|---|---|---|---|
| spill the beans | tell a secret | cry over spilt milk | waste regret on what cannot be undone |
| once in a blue moon | very rarely | a bolt from the blue | a sudden shock |
| smell a rat | suspect a trick | the rat race | a tiring fight for success |
| in a nutshell | in brief | in a pickle | in a difficult situation |

> **Tip:** Learn each pair together on one card. Then the planted twin cannot fool you.

### Idiom inside a sentence
Sometimes the idiom sits in a sentence. Use the sentence as a clue.

*Meena was on cloud nine after the result.* The result is good news. So the meaning is extremely happy.

### When you do not know the idiom
- Remove the literal options first.
- Judge the tone from the key word. Cold, dark and hot often mean trouble. Cloud nine and red-letter mean joy.
- Choose the option that fits a sentence you can imagine.

> **Watch:** Two figurative options can look alike. Pick the one that names the outcome the idiom records. Bite the dust means be defeated, not be wounded.
""",
    patterns=[
        pat("il-p1", "Idiom with a literal decoy", "very common",
            "One idiom stands alone under 'select the most appropriate meaning'. At least one option repeats its words.",
            ["Cross out every option you could photograph.", "Ask what picture the idiom paints.",
             "Say what the picture stands for.", "Pick the option that matches."],
            "The literal option is always planted as bait.",
            "Let the cat out of the bag: (a) to free a pet (b) to reveal a secret (c) to buy a bag (d) to hide a pet",
            ["Free a pet and hide a pet are literal.", "A cat escaping means something hidden comes out.", "So a secret is revealed."],
            "(b) to reveal a secret"),
        pat("il-p2", "Idiom inside a sentence", "very common",
            "A full sentence holds the idiom, often in bold, and you choose its meaning there.",
            ["Read the whole sentence.", "Decide if the situation is good or bad.", "Remove options with the wrong tone.",
             "Plug the meaning back."],
            "The situation fixes the tone.",
            "Meena was on cloud nine after the result. (a) extremely happy (b) flying (c) confused (d) ill",
            ["The result is good news.", "Flying is literal. Confused and ill are wrong in tone.", "Extremely happy fits."],
            "(a) extremely happy"),
        pat("il-p3", "Close figurative trap", "common",
            "Two options are figurative. One is the real meaning. The other sounds related but changes the sense or strength.",
            ["List the two figurative options.", "Ask what result the idiom records.", "Pick the one that states that result."],
            "The neighbour option is the most common trap after the literal one.",
            "Bite the dust: (a) be wounded (b) be defeated (c) clean a floor (d) be tired",
            ["Clean a floor is literal.", "Wounded and tired are related but not the record of the idiom.", "Bite the dust means be defeated."],
            "(b) be defeated"),
        pat("il-p4", "Look-alike idiom pairs", "common",
            "The options include the meaning of another idiom that shares a key word: beans and milk, blue moon and blue bolt.",
            ["Name the twin idiom in the options.", "Recall what the twin means.", "Cross out the twin's meaning."],
            "Twin idioms are planted for readers who match on one word.",
            "Spill the beans: (a) regret what cannot be changed (b) tell a secret (c) waste food (d) cook a meal",
            ["Option (a) is the meaning of cry over spilt milk.", "Waste food and cook a meal are literal.", "Spill the beans means tell a secret."],
            "(b) tell a secret"),
        pat("il-p5", "Tone check", "common",
            "The options differ in strength: suspect, be sure, be certain.",
            ["Mark the idiom as mild, strong or neutral.", "Match the strength of each option.",
             "Reject options that overshoot."],
            "A right idea in the wrong strength is still wrong.",
            "Smell a rat: (a) to suspect that something is wrong (b) to be certain of theft (c) to smell something rotten (d) to feel ill",
            ["Smell something rotten is literal.", "Certain of theft overshoots.", "Suspect is at the right strength."],
            "(a) to suspect that something is wrong"),
    ],
    mistakes=[
        mis("Choosing the option that repeats the words of the idiom.", "Cross out any option you could photograph. It is a literal decoy."),
        mis("Learning an idiom by its words but not its picture.", "Learn the picture and what it stands for."),
        mis("Ignoring the tone of the idiom.", "Say if it is happy, sad or angry. Pick the same tone."),
        mis("Matching on one shared word (beans, milk).", "Look-alike idioms share a word but not a meaning. Learn them in pairs."),
        mis("Skipping the sentence in a context question.", "Let the situation in the sentence fix the meaning."),
    ],
    revision=[
        "An idiom is a fixed picture. The meaning is what the picture stands for.",
        "Wrong options: literal, neighbour, opposite.",
        "Method: kill the literal, find the picture, check the tone, plug back.",
        "Learn look-alike idioms in pairs.",
        "In a sentence, the situation decides the meaning.",
    ],
    tricks=[
        trick("Photo test",
              "If you could take a photo of what an option says, it is almost always wrong. This removes one option in nearly every question.",
              "Break the ice: (a) to crack frozen water (b) to start a conversation among strangers (c) to feel cold (d) to make a drink",
              ["Crack frozen water and make a drink are pictures.", "Feel cold is also literal.", "Start a conversation is the figurative meaning."],
              "(b) to start a conversation among strangers"),
        trick("Plug-back check",
              "Put your chosen meaning into a sentence in place of the idiom. If the sentence sounds natural, keep it."),
        trick("Tone from the key word",
              "Cold, dark and hot often signal trouble. Cloud nine and red-letter signal joy. Use this when you do not know an idiom."),
    ],
)

# ---------------------------------------------------------------- 2. animal and body
SUBS["idiom-animal-body"] = sub(
    concept=("Many exam idioms use an animal or a body part. Each animal has a fixed character and each body part a fixed job. "
             "Use that to work out an idiom even when you half remember it."),
    notes=r"""
### Why animals and body parts
Many idioms in exams name an **animal** or a **part of the body**. Each one has a fixed character. So you can often decode an idiom even if you only half remember it.

### Animal characters
| Animal | Stands for | Idiom | Meaning |
|---|---|---|---|
| bull | facing force head-on | take the bull by the horns | face a problem boldly |
| rat | cheating, trickery | smell a rat | suspect something is wrong |
| crocodile | false tears | crocodile tears | pretended sorrow |
| horse | speed, hurry | hold your horses | wait, be patient |
| wolf | hunger | keep the wolf from the door | avoid hunger |
| birds | targets | kill two birds with one stone | get two results from one action |
| lion | biggest share | the lion's share | the largest part |
| goose | foolish effort | a wild-goose chase | a pointless search |
| cat | hidden thing | let the cat out of the bag | reveal a secret |

> **Example:** Crocodile tears. The old belief was that crocodiles cry while eating. So the tears are not real. The meaning is pretended sorrow.

### Body-part jobs
| Part | Job | Idiom | Meaning |
|---|---|---|---|
| ear | listening | turn a deaf ear | refuse to listen |
| eye | watching, agreeing | see eye to eye | agree fully |
| nose | price paid | pay through the nose | pay far too much |
| shoulder | welcome | give the cold shoulder | treat someone coldly |
| neck | risk | stick your neck out | take a risk by acting boldly |
| feet | courage | get cold feet | lose courage at the last moment |
| hand | help, work | lend a hand | give help |
| hands | work | have your hands full | be very busy |
| foot | firmness | put your foot down | take a firm stand |
| heart | fear, feeling | heart in your mouth | very nervous |
| leg | play | pull someone's leg | tease playfully |

### More body idioms
- *Bite the dust*: be defeated or fail completely.
- *Bury the hatchet*: end a quarrel and make peace.
- *Wash your hands of*: refuse any more responsibility.
- *Keep at arm's length*: avoid becoming friendly with.
- *Cost an arm and a leg*: be extremely expensive.
- *Keep an eye on*: watch carefully.

### Four question types
1. **Animal idiom.** Use the animal's character.
2. **Body idiom.** Use the body part's job.
3. **Idiom in a sentence.** The sentence tells you if it is good or bad.
4. **Reverse type.** A meaning is given and you choose the idiom. The wrong options are real idioms of the same body part. Match the job exactly. Hand is help, hands full is busy, wash hands is refuse duty.

> **Watch:** Some idioms have no clear picture. Keep one flash card each for cold shoulder, bite the dust and crocodile tears.
""",
    patterns=[
        pat("iab-p1", "Animal idiom meaning", "very common",
            "The idiom names an animal or bird: bull, rat, crocodile, wolf, horse, goose, lion.",
            ["Name the animal.", "Recall its character.", "Match the character to an option.", "Cross out the literal option."],
            "Each animal keeps the same character in every idiom.",
            "Take the bull by the horns: (a) to face a difficulty boldly (b) to buy a bull (c) to run away (d) to lose a bet",
            ["Buy a bull is literal.", "The bull stands for facing force head-on.", "So it means to face a difficulty boldly."],
            "(a) to face a difficulty boldly"),
        pat("iab-p2", "Body-part idiom meaning", "very common",
            "The idiom names a body part: ear, eye, nose, shoulder, neck, feet, hand, heart.",
            ["Name the body part.", "Recall its job.", "Match the job to an option."],
            "Each body part has a job that carries into the idiom.",
            "Turn a deaf ear: (a) to hear badly (b) to refuse to listen (c) to listen carefully (d) to be ill",
            ["Ear is listening.", "Hear badly is the neighbour trap.", "Deaf ear means refusing to listen."],
            "(b) to refuse to listen"),
        pat("iab-p3", "Animal or body idiom in a sentence", "common",
            "A sentence holds the idiom, and you choose its meaning in context.",
            ["Read the sentence.", "Decide if the situation is good or bad.", "Use the animal or body job.",
             "Plug it back."],
            "The sentence confirms the character.",
            "He stuck his neck out for his friend. (a) took a risk (b) hurt himself (c) ran away (d) told a lie",
            ["Neck stands for risk.", "The action helps a friend, so the tone is bold.", "Took a risk fits."],
            "(a) took a risk"),
        pat("iab-p4", "Choose the idiom for a meaning", "common",
            "The stem gives a meaning and the options are four idioms, usually of one body part.",
            ["Say the meaning in two words.", "Match each idiom to its meaning.", "Pick the one that fits exactly."],
            "The wrong options are real idioms with other meanings.",
            "Which idiom means to be extremely busy? (a) lend a hand (b) have one's hands full (c) wash one's hands of (d) keep at arm's length",
            ["Lend a hand is help.", "Wash hands is refuse duty and arm's length is avoid friendship.", "Hands full is busy."],
            "(b) have one's hands full"),
        pat("iab-p5", "Playful or hostile trap", "occasional",
            "An option gives a harmful meaning for a mild idiom (pull someone's leg, give the cold shoulder).",
            ["Mark the idiom as mild or hostile.", "Cross out options with the wrong strength.", "Pick the option that fits."],
            "Body idioms are often milder or colder than the literal picture.",
            "Pull someone's leg: (a) to hurt someone (b) to tease someone playfully (c) to help someone walk (d) to trip someone",
            ["Hurt, help walk and trip are literal.", "Leg stands for playful force.", "Tease playfully fits."],
            "(b) to tease someone playfully"),
    ],
    mistakes=[
        mis("Reading pull someone's leg as hurting someone.", "It means to tease playfully."),
        mis("Reading cold shoulder as an illness.", "It means to treat someone coldly."),
        mis("Mixing smell a rat with the rat race.", "Smell a rat means suspect a trick. The rat race is a tiring fight for success."),
        mis("Reading heart in your mouth as love.", "It means extreme fear or nervousness."),
        mis("Reading wash your hands of as cleanliness.", "It means to refuse any more responsibility."),
    ],
    revision=[
        "Animal is character: bull bold, rat trick, crocodile fake, wolf hunger, horse hurry.",
        "Body is job: ear listen, eye watch or agree, neck risk, feet courage, hand help.",
        "Reverse questions: match the meaning to the body part's job first.",
        "Keep separate cards for cold shoulder and crocodile tears.",
        "Hands full is busy. Wash hands is refuse duty.",
    ],
    tricks=[
        trick("Character first",
              "Name the animal or body part, then recall its character or job. The meaning usually follows.",
              "Keep the wolf from the door: (a) to scare a wolf (b) to earn enough to avoid hunger (c) to close a door (d) to be a wolf",
              ["Scare a wolf and close a door are literal.", "Wolf stands for hunger.", "The meaning is to earn enough to avoid hunger."],
              "(b) to earn enough to avoid hunger"),
        trick("Body parts in sets",
              "Learn hand idioms together: lend a hand, have your hands full, wash your hands of. The job is help or work."),
        trick("One card for opaque idioms",
              "Write a card for each idiom whose picture is hard to see. Read those cards first in revision."),
    ],
)

# ---------------------------------------------------------------- 3. colour and food
SUBS["idiom-colour-food"] = sub(
    concept=("In English idioms each colour carries a feeling, and food is used to judge a task or a person. "
             "Learn the colour or food and you know the family of the meaning. "
             "Watch the look-alike pairs, such as red tape and red-letter day."),
    notes=r"""
### Colours carry feelings
Each colour usually points to one family of meaning.
| Colour | Usual meaning | Idiom | Meaning |
|---|---|---|---|
| blue | unexpected, rare | out of the blue | suddenly, without warning |
| blue | unexpected, rare | once in a blue moon | very rarely |
| red | anger | see red | become suddenly angry |
| red | officialdom | red tape | too many official rules causing delay |
| red | special day | a red-letter day | a day to remember |
| green | envy | green with envy | very jealous |
| black | disgrace | a black sheep | the one who brings shame to a group |
| white | costly, useless | a white elephant | costly to keep and of no use |
| grey | unclear | a grey area | a matter not clearly right or wrong |
| silver | wealth | born with a silver spoon | born into a rich family |

> **Example:** A flyover that nobody uses but costs lakhs to maintain is a white elephant. It is a possession that costs much and gives no benefit.

### Watch out for red
Red has three families.
- *See red* means to become angry.
- *Red tape* means too many official rules causing delay.
- *Red-letter day* means a happy, important day. Special days were marked in red on calendars.

Examiners put these three against each other.

### Food idioms are judgements
A food idiom uses something we eat to judge a task or a person.
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
| the salt of the earth | goodness | a very good, dependable person |
| carry coals to Newcastle | useless supply | take something to a place that has plenty |
| a storm in a teacup | fuss | a big quarrel over a small matter |

> **Example:** Maths is a piece of cake for Arjun. Cake means easy, so maths is very easy for him.

### Look-alike pairs
- *The apple of one's eye* (most loved) and *the apple of discord* (cause of a quarrel).
- *A piece of cake* (easy) and *a hot potato* (a touchy issue).
- *Red tape* (delay) and *red-letter day* (a happy day).
- *Born with a silver spoon* (rich from birth) and *every cloud has a silver lining* (some good in every bad situation).

### Blank-filling questions
A sentence has a blank and four idioms as options.
1. Decide what the sentence needs: a useless thing, a small fuss, a happy day.
2. Pick the idiom of that family.
3. Check the grammar. A blank after *was* needs a noun phrase such as *a red-letter day*.
""",
    patterns=[
        pat("icf-p1", "Colour idiom meaning", "very common",
            "The idiom holds a colour word: blue, red, green, black, white, grey, silver.",
            ["Name the colour.", "Recall its usual feeling.", "Match the feeling to an option.", "Cross out the literal option."],
            "A colour keeps one feeling across many idioms.",
            "Once in a blue moon: (a) very rarely (b) at night (c) very often (d) in a hurry",
            ["Blue stands for rare or unexpected.", "At night is literal.", "Very often is the opposite."], "(a) very rarely"),
        pat("icf-p2", "Food idiom meaning", "very common",
            "The idiom names a food: cake, nut, butter, potato, pickle, beans, milk, apple, salt.",
            ["Name the food.", "Recall the judgement it gives.", "Match to an option."],
            "Food idioms judge a task or a person.",
            "A piece of cake: (a) a birthday treat (b) a task needing almost no effort (c) a costly gift (d) a sweet dish",
            ["Birthday treat and sweet dish are literal.", "Cake stands for easy.", "The meaning is a task needing almost no effort."],
            "(b) a task needing almost no effort"),
        pat("icf-p3", "Look-alike twin", "common",
            "One option is the meaning of a twin idiom that shares the colour or food word.",
            ["Name the twin idiom.", "Recall its meaning.", "Cross that meaning out."],
            "The twin is planted for readers who match only the colour.",
            "Red tape: (a) a happy day (b) excessive official delay (c) sudden anger (d) a costly item",
            ["A happy day is red-letter day.", "Sudden anger is see red.", "Red tape is excessive official delay."],
            "(b) excessive official delay"),
        pat("icf-p4", "Fill the blank with an idiom", "common",
            "A sentence has a blank and four idioms as options.",
            ["Decide what the sentence needs.", "Pick the idiom of that family.", "Read the sentence again."],
            "The sentence names the need before the options do.",
            "The flyover that nobody uses but costs lakhs to maintain is a ___. (a) white elephant (b) black sheep (c) red-letter day (d) hot potato",
            ["The sentence describes something costly and useless.", "Black sheep is a person and red-letter day is a happy day.", "White elephant fits."],
            "(a) white elephant"),
        pat("icf-p5", "Choose the idiom for a meaning", "occasional",
            "The stem gives a meaning and the options are four idioms of one colour or food family.",
            ["Say the meaning in two words.", "Match each idiom to its meaning.", "Pick the exact fit."],
            "The wrong options are real idioms with other meanings.",
            "A person who brings shame to his family: (a) black sheep (b) white elephant (c) dark horse (d) grey area",
            ["Shame points to black.", "White elephant is a costly useless thing.", "Grey area is unclear."], "(a) black sheep"),
    ],
    mistakes=[
        mis("Mixing red tape with a red-letter day.", "Red tape is delay. A red-letter day is a happy day."),
        mis("Mixing the apple of one's eye with the apple of discord.", "The first is most loved. The second is a cause of a quarrel."),
        mis("Reading a food idiom literally (a piece of cake as a treat).", "Food idioms judge a task or a person. Cake means easy."),
        mis("Filling a blank without checking the grammar.", "After was, choose a noun phrase such as a red-letter day."),
        mis("Learning colours without their feelings.", "Learn the feeling: blue unexpected, green envy, black disgrace."),
    ],
    revision=[
        "Blue is sudden or rare. Red is anger, delay or a special day. Green is envy. Black is shame. White is costly and useless. Grey is unclear.",
        "Food is judgement: cake easy, nut hard, butter flattery, potato touchy, pickle trouble, apple loved.",
        "Learn look-alike pairs together.",
        "In blanks, decide the need first, then the family, then check grammar.",
    ],
    tricks=[
        trick("Colour to feeling",
              "Say the colour and its feeling before you read the options. Blue means sudden or rare, and the options then sort themselves.",
              "Out of the blue: (a) completely unexpectedly (b) very sadly (c) after a long wait (d) at sea",
              ["Blue stands for unexpected.", "At sea is literal.", "Completely unexpectedly fits."], "(a) completely unexpectedly"),
        trick("Food gives a verdict",
              "Ask what verdict the food gives: easy, hard, flattery or trouble. That is the meaning."),
        trick("Pair cards",
              "Write the twins on one card: red tape and red-letter day, apple of the eye and apple of discord."),
    ],
)

# ---------------------------------------------------------------- 4. situations and people
SUBS["idiom-situations-people"] = sub(
    concept=("Many idioms describe situations, such as trouble, effort or suddenness, and types of people, such as false, weak or reliable. "
             "Sort each idiom into a family and the right option stands out. "
             "A few idioms come from old stories, and one line of the story gives the meaning."),
    notes=r"""
### Two big groups
1. **Situation idioms** describe what is happening: trouble, hard work, sudden events, success, defeat.
2. **People idioms** describe a type of person: loyal, false, weak, skilled.

Find the group and the family. Then the answer stands out.

### Situation families
| Family | Idioms | Meaning |
|---|---|---|
| Trouble | in hot water | in serious trouble |
| Hard effort | burn the midnight oil | work late into the night |
| Hard effort | leave no stone unturned | try every possible means |
| Hard effort | move heaven and earth | make the greatest effort |
| Sudden | at the drop of a hat | instantly |
| Sudden | on the spur of the moment | without planning |
| Sudden | a bolt from the blue | a sudden shock |
| Money | make both ends meet | live within a small income |
| Change | turn over a new leaf | begin a better way of living |
| Change | turn the tables | reverse the position |
| Winning | carry the day | win |
| Losing | throw in the towel | admit defeat and give up |
| Losing | take to one's heels | run away quickly |
| Mood, health | on cloud nine | extremely happy |
| Mood, health | under the weather | slightly ill |

> **Example:** The police left no stone unturned to find the child. This is the effort family. The meaning is tried every possible way.

### More situation idioms
- *A blessing in disguise*: a misfortune that turns out well.
- *Out of the frying pan into the fire*: from a bad situation into a worse one.
- *Face the music*: accept the unpleasant results of one's acts.
- *Pass the buck*: shift blame or duty to someone else.
- *End in smoke*: come to nothing.
- *Against all odds*: despite every difficulty.
- *In the doldrums*: low in spirits or activity.

### People families
| Type | Idiom | Meaning |
|---|---|---|
| False friend | a snake in the grass | a treacherous enemy hiding as a friend |
| False friend | a fair-weather friend | a friend only in good days |
| False friend | a wolf in sheep's clothing | a dangerous person who looks harmless |
| Weak | a man of straw | a person of no substance |
| Weak | a cog in the machine | an unimportant worker in a big system |
| Reliable | a man of his word | one who keeps his promises |
| Reliable | a tower of strength | a person who gives firm support |
| Many skills | a jack of all trades | does many jobs, masters none |
| Second place | play second fiddle | accept a lower role |

### Idioms from stories
One line of the old story fixes the meaning.
- **Achilles' heel**: a Greek hero could be hurt only at his heel. It means a weak point.
- **Bell the cat**: the mice wanted a bell on the cat, but none dared tie it. It means take a big risk for everyone.
- **Pandora's box**: opening a forbidden box let out all troubles. It means a source of many problems.
- **A Herculean task**: Hercules did twelve very hard labours. It means a task needing huge effort.
- **Midas touch**: whatever King Midas touched became gold. It means the ability to make money from anything.
- **A Trojan horse**: soldiers hid inside a wooden horse. It means something harmless-looking that harms from inside.

> **Watch:** *Pass the buck* is not about money. *Steal a march on* is not stealing. *Under the weather* is not about rain.
""",
    patterns=[
        pat("isp-p1", "Situation idiom meaning", "very common",
            "The idiom describes an event or condition: trouble, effort, suddenness, winning, losing, health.",
            ["Name the family.", "Recall the meaning of that family.", "Cross out the literal option.", "Pick the match."],
            "One family word tells you the answer.",
            "Leave no stone unturned: (a) to try every possible means (b) to clean the ground (c) to give up early (d) to break stones",
            ["Clean the ground and break stones are literal.", "Give up early is the opposite.", "The idiom is in the effort family."],
            "(a) to try every possible means"),
        pat("isp-p2", "People idiom meaning", "very common",
            "The idiom names a type of person: a ___ friend, a man of ___, a ___ in the grass.",
            ["Name the type: false, weak or reliable.", "Recall the idiom in that type.", "Pick the match."],
            "People idioms come in fixed types.",
            "A snake in the grass: (a) a lazy person (b) a treacherous enemy hiding as a friend (c) a snake catcher (d) a loyal helper",
            ["Snake catcher is literal.", "Loyal helper is the opposite.", "A snake hides and strikes, so it is a treacherous enemy."],
            "(b) a treacherous enemy hiding as a friend"),
        pat("isp-p3", "Fill the blank with a situation idiom", "common",
            "A sentence has a blank and four idioms as options.",
            ["Read the sentence.", "Name the family it needs.", "Pick the idiom of that family.", "Read the full sentence again."],
            "The sentence shows the family before the options do.",
            "Seeing the police, the thief ___. (a) took to his heels (b) burnt the midnight oil (c) turned over a new leaf (d) played second fiddle",
            ["The thief wants to escape.", "That is running away.", "Took to his heels fits."], "(a) took to his heels"),
        pat("isp-p4", "Idioms from stories", "common",
            "A name or story object appears: Achilles, Pandora, Hercules, Midas, Trojan, a cat with a bell.",
            ["Recall the story in one line.", "Turn the story into a meaning.", "Pick the option that matches."],
            "The story line fixes the meaning.",
            "Achilles' heel: (a) a sore foot (b) a weak point (c) a great strength (d) a fast runner",
            ["A sore foot is literal.", "The hero could be hurt only at his heel.", "So it means a weak point."], "(b) a weak point"),
        pat("isp-p5", "Bad to worse and blame idioms", "common",
            "The idiom describes a change in a situation or a shift of blame.",
            ["Name the situation: worse, blame or result.", "Recall the idiom for it.", "Reject the literal option."],
            "These idioms record an outcome, not an action.",
            "Out of the frying pan into the fire: (a) from a bad situation into a worse one (b) from cooking to eating (c) from cold to warm (d) from work to rest",
            ["Cooking to eating is literal.", "Frying pan is bad and fire is worse.", "So it means from bad to worse."],
            "(a) from a bad situation into a worse one"),
    ],
    mistakes=[
        mis("Reading pass the buck as passing money.", "It means to shift blame or duty to someone else."),
        mis("Reading steal a march on as stealing.", "It means to gain an advantage over someone."),
        mis("Reading under the weather as being in the rain.", "It means slightly ill."),
        mis("Reading play second fiddle as music.", "It means to accept a lower role."),
        mis("Guessing a story idiom without the story.", "Recall the one-line story and turn it into a meaning."),
    ],
    revision=[
        "Name the family first: trouble, effort, sudden, money, change, win, lose, health.",
        "False people: snake in the grass, fair-weather friend, wolf in sheep's clothing.",
        "Weak people: man of straw, cog in the machine. Reliable: man of his word, tower of strength.",
        "Story idioms: Achilles' heel, bell the cat, Pandora's box, Herculean, Midas touch, Trojan horse.",
        "In blanks, match the family the sentence needs.",
    ],
    tricks=[
        trick("Family first",
              "Name the family of the situation before you read the options. Effort, trouble and suddenness cover a large share.",
              "At the drop of a hat: (a) instantly (b) carefully (c) slowly (d) angrily",
              ["The idiom is in the sudden family.", "Carefully and slowly are the opposite.", "Instantly fits."], "(a) instantly"),
        trick("One line per story",
              "Store each story idiom as one line: Achilles, heel, weak point. Do not learn the whole story."),
        trick("Read the whole sentence",
              "In a blank question, say what the person does. Escape means took to his heels. Hard work means burnt the midnight oil."),
    ],
)

# ---------------------------------------------------------------- 5. phrasal verbs
SUBS["idiom-phrasal-verbs"] = sub(
    concept=("A phrasal verb is a verb joined with a small word called a particle, such as up, off, out or in. "
             "Together they give a new meaning, like give up, which means stop. "
             "They appear in idiom questions, fill-in-the-blank and error spotting."),
    notes=r"""
### What a phrasal verb is
A **phrasal verb** is a verb plus a small word called a **particle**. The particle can be up, off, out, in, on, down, after, into or over.

Together they give a new meaning that you often cannot guess from the verb alone.
- *give* means hand over. *give up* means stop doing something.
- *call* means phone or shout. *call off* means cancel.

Exams test them as a meaning question, a blank to fill with a particle, or a word to replace.

### What the particles usually mean
These are tendencies, not strict rules. They still help.
| Particle | Usual idea | Examples |
|---|---|---|
| off | stop, cancel, leave | call off (cancel), put off (postpone), take off (leave the ground) |
| out | finish, remove, appear | run out of (finish), put out (extinguish), break out (start suddenly) |
| up | complete, stop, arrive | give up (stop), turn up (arrive), bring up (raise a child) |
| down | reduce, fail, refuse | break down (stop working), turn down (refuse), look down upon (despise) |
| in | enter, yield | give in (surrender), hand in (submit), break in (enter by force) |
| after | follow, care | look after (take care of), take after (resemble an elder) |
| into | examine, meet | look into (investigate), run into (meet by chance) |
| over | recover, check | get over (recover from), look over (check quickly) |

### One verb, many meanings
Examiners fix the verb and change the particle.
| Verb | Particle | Meaning |
|---|---|---|
| give | up, in, away, out | stop a habit, surrender, donate or reveal, distribute |
| turn | down, up, out | refuse, arrive, prove to be |
| take | after, off, up | resemble, leave the ground, start a hobby |
| break | down, out, in, up | stop working, start suddenly, enter by force, end a relationship |
| come | across, about | meet by chance, happen |
| put | off, out, up with | postpone, extinguish, tolerate |

> **Example:** The car broke ___ on the highway. Cars stop working, so the answer is *broke down*. *Broke out* is for war, fire or disease. *Broke in* is for thieves.

### Three-word phrasal verbs
Some phrasal verbs have two particles. They must stay together.
- *put up with*: tolerate.
- *run out of*: have none left.
- *look down upon*: despise.
- *look forward to*: wait eagerly.

> **Watch:** Do not drop the second particle. "We have run out sugar" is wrong. Say "run out **of** sugar".

### How to answer
1. **Meaning questions.** Replace the phrasal verb with one word, such as cancel or tolerate, and test it in a sentence.
2. **Particle blanks.** Read the whole sentence. The subject (a car, a fire, a meeting) shows which particle fits.
3. **Replace-the-word questions.** The bold word is formal, such as extinguish or postpone. Find the phrasal verb that means the same.
""",
    patterns=[
        pat("ipv-p1", "Meaning of a phrasal verb", "very common",
            "A phrase such as 'to call off' or 'to put up with' is given. The options are short meanings.",
            ["Split the verb and the particle.", "Recall the particle's usual idea.", "Try each option in a sentence."],
            "The particle carries the new meaning.",
            "To call off: (a) to cancel (b) to phone (c) to shout (d) to visit",
            ["Phone and shout are the meanings of call alone.", "Off means stop or cancel.", "Call off means to cancel."], "(a) to cancel"),
        pat("ipv-p2", "Fill in the particle", "very common",
            "A sentence has a blank right after a verb. The options are particles.",
            ["Read the whole sentence.", "Name the subject: a car, a fire, a meeting.", "Pick the particle that fits that subject."],
            "The subject shows which meaning is needed.",
            "The car broke ___ on the highway. (a) in (b) out (c) down (d) off",
            ["Cars stop working.", "Break in is for thieves and break out is for war or fire.", "Break down is right."], "(c) down"),
        pat("ipv-p3", "Same verb, different particles", "common",
            "All options share one verb: give up, give in, give away, give out.",
            ["Say the meaning in one word.", "Match each option to its meaning.", "Pick the exact one."],
            "Only the particle changes the meaning.",
            "The rebels finally ___ and laid down their weapons. (a) gave up (b) gave in (c) gave away (d) gave out",
            ["The rebels stopped fighting.", "Give in means surrender.", "Give away means donate and give out means distribute."],
            "(b) gave in"),
        pat("ipv-p4", "Replace a formal word", "common",
            "A sentence has a formal verb in bold (extinguish, postpone, recover). The options are phrasal verbs.",
            ["Say the formal word in plain words.", "Match a phrasal verb to it.", "Check the sentence again."],
            "A phrasal verb is the everyday form of a formal word.",
            "The firemen quickly EXTINGUISHED the fire. (a) put off (b) put out (c) put up (d) put down",
            ["Extinguish means stop a fire.", "Put off means postpone.", "Put out fits."], "(b) put out"),
        pat("ipv-p5", "Three-word phrasal verb", "common",
            "The blank sits after a two-part verb such as run out ___ or look forward ___.",
            ["Recall the full phrase.", "Do not drop the second particle.", "Pick the particle that completes it."],
            "These phrases are fixed.",
            "We have run out ___ sugar. (a) from (b) of (c) off (d) with",
            ["The phrase is run out of.", "It means have none left.", "Of completes it."], "(b) of"),
    ],
    mistakes=[
        mis("Guessing a phrasal verb from the verb alone.", "The particle changes the meaning. Learn the whole phrase."),
        mis("Mixing put off and put out.", "Put off means postpone. Put out means extinguish."),
        mis("Writing 'run out sugar'.", "Write 'run out of sugar'. Keep both particles."),
        mis("Mixing break down, break out and break in.", "Down means stop working. Out means start suddenly. In means enter by force."),
        mis("Learning particles as strict rules.", "They are tendencies. Learn each common phrase with its meaning."),
    ],
    revision=[
        "off is cancel or stop. out is finish or remove. up is stop or arrive. down is refuse or fail. after is care or resemble. into is investigate.",
        "call off cancel, put off postpone, put out extinguish, put up with tolerate.",
        "give up stop, give in surrender, turn down refuse, take after resemble.",
        "break down stops working, break out starts suddenly, come across meets by chance, get over recovers.",
        "Keep three-word phrases whole: run out of, look forward to.",
    ],
    tricks=[
        trick("Swap for one word",
              "Replace the phrasal verb with one plain word, such as cancel, refuse or tolerate. Test it in the sentence.",
              "The meeting was put off. It was: (a) postponed (b) cancelled forever (c) held early (d) put out",
              ["Put off means postpone.", "Cancelled forever and held early do not fit.", "Postponed fits."], "(a) postponed"),
        trick("Subject shows the particle",
              "A car breaks down. A fire breaks out. A thief breaks in. The subject picks the particle."),
        trick("Learn by verb",
              "Learn one verb with all its particles in one sitting: give up, give in, give away, give out."),
    ],
)

# ---------------------------------------------------------------- 6. strategy
SUBS["idiom-strategy"] = sub(
    concept=("Idioms are a small but steady part of the English section. The pool is small and repeats often, "
             "so a bank of about 300 idioms covers most papers. Learn in a 30-day plan and use your own sentences."),
    notes=r"""
### How idioms appear
Idioms give a small but steady number of marks. Most papers ask one or two direct idiom questions. Idioms also hide inside cloze tests, sentence improvement and fill-in-the-blank items.

The pool of idioms that examiners use is small and repeats often. A list of about 300 idioms covers most of what you will see.

### Question formats
1. **Meaning of the idiom.** One idiom, four meanings. The most common.
2. **Replace the phrase.** A plain phrase is underlined, and you choose the idiom that can replace it. *They are in bitter open hostility* becomes *they are at daggers drawn*.
3. **Complete the idiom.** One word is missing: *calls a spade a ___*. Only the original word is correct.
4. **Opposite meaning.** Find the meaning first, then its opposite.
5. **Idiom inside a passage.** The context gives the tone.

### Idioms are frozen
You cannot change the words of an idiom. It is *a hard nut to crack*, never *a hard nut to break*. It is *every cloud has a silver lining*, never *a golden lining*.

That is why a complete-the-idiom question has only one defensible answer. When you learn an idiom, learn its exact words.

### The 30-day plan
| Days | Daily work |
|---|---|
| 1 to 10 | 10 new idioms, one sentence of your own for each |
| 11 to 20 | 10 new and 15 old, revised by family |
| 21 to 30 | 10 new, 25 old and one 20-question self-test |

Any idiom you miss twice goes on a short **weak list**. Revise that list once a week.

> **Tip:** Your own sentence is what you remember in the exam. A list read alone fades fast. Example: I burnt the midnight oil before my mock test.

### In the exam hall
About 20 seconds per idiom.
1. Kill the literal option.
2. Find the picture and the family.
3. Check the tone: positive or negative.
4. Plug the answer back into a sentence.

If you do not know the idiom, judge the tone from the key words. Pick the option with the same tone. This beats a blind guess.

### Sorting idioms by family
Group idioms so that one cue recalls many.
- **Effort:** burn the midnight oil, leave no stone unturned, move heaven and earth.
- **Trouble:** in hot water, in a pickle, out of the frying pan into the fire.
- **Secrets:** spill the beans, let the cat out of the bag.
- **Defeat:** bite the dust, throw in the towel.

When two idioms in a question sit in one family, compare their exact meanings.

### After each mock test
List every idiom you missed. Write its meaning and one sentence of your own. Read the list again after two days and after a week.

> **Note:** Ten idioms known well are worth more than fifty half known.

### Opposite-meaning questions
Write the meaning in two words first. *Keep one's chin up* means stay cheerful. So the opposite is lose heart.

> **Watch:** The option that says "stay brave" has the same meaning. It is the planted trap.
""",
    patterns=[
        pat("is-p1", "Complete the idiom", "very common",
            "An idiom has one word blanked, and the options are four close words (spade, shovel, tool).",
            ["Recall the idiom in full.", "Say the missing word.", "Reject every changed word."],
            "Idioms are frozen, so only the original word is correct.",
            "He always calls a spade a ___. (a) shovel (b) spade (c) tool (d) digger",
            ["The idiom is call a spade a spade.", "It means to speak plainly.", "Only the original word is correct."], "(b) spade"),
        pat("is-p2", "Replace the phrase with an idiom", "common",
            "A plain phrase is underlined and the options are idioms.",
            ["Say the meaning of the phrase in two words.", "Match each idiom to a meaning.", "Pick the exact one."],
            "The answer is the idiom with exactly that meaning.",
            "They are in bitter open hostility. (a) at daggers drawn (b) on cloud nine (c) in the doldrums (d) under the weather",
            ["The meaning is open and bitter enmity.", "Cloud nine is joy and doldrums is low spirits.", "At daggers drawn fits."], "(a) at daggers drawn"),
        pat("is-p3", "Idiom from any family with a tone check", "very common",
            "A less known idiom appears and the options differ in tone.",
            ["Kill the literal option.", "Judge the tone from the key word.", "Pick the option with the same tone."],
            "Tone alone beats a blind guess.",
            "In the doldrums: (a) in high spirits (b) low in spirits or activity (c) in great danger (d) in a hurry",
            ["Doldrums sounds low.", "High spirits is the opposite.", "Low in spirits fits."], "(b) low in spirits or activity"),
        pat("is-p4", "Opposite in meaning to an idiom", "common",
            "The stem asks for the option opposite in meaning to the idiom.",
            ["Write the meaning of the idiom in two words.", "Reverse it in your mind.", "Cross out the option that has the same meaning."],
            "The option with the same meaning is the planted trap.",
            "Opposite of KEEP ONE'S CHIN UP: (a) stay brave (b) lose heart (c) work hard (d) speak plainly",
            ["Keep one's chin up means stay cheerful.", "Stay brave has the same meaning.", "The opposite is lose heart."], "(b) lose heart"),
        pat("is-p5", "Frozen wording in a proverb", "occasional",
            "A well-known saying has one word blanked or changed in the options.",
            ["Recall the saying word for word.", "Find the option with the original word.", "Reject the near words."],
            "A changed word makes a wrong idiom.",
            "Every cloud has a silver ___. (a) lining (b) edge (c) coat (d) spoon",
            ["The saying is every cloud has a silver lining.", "It means some good in every bad situation.", "Lining is the original word."], "(a) lining"),
    ],
    mistakes=[
        mis("Reading a list of idioms once.", "Write one sentence of your own for each idiom."),
        mis("Accepting a changed word in an idiom.", "Idioms are frozen. Learn the exact words."),
        mis("Choosing the same meaning in an opposite question.", "Write the meaning first, then reverse it."),
        mis("Learning idioms in alphabet order.", "Learn by family so the clusters help recall."),
        mis("Spending too long on one unknown idiom.", "Judge the tone, pick an option and move on."),
    ],
    revision=[
        "10 new idioms a day, one sentence each, a weekly weak list.",
        "Idioms are frozen. Never accept a changed word.",
        "Formats: meaning, replace the phrase, complete the idiom, opposite, in a passage.",
        "Exam steps: kill the literal, find the picture, check the tone, plug back.",
        "Opposite question: meaning first, then reverse. Cross out the same-meaning option.",
    ],
    tricks=[
        trick("Own sentence",
              "Write one sentence of your own for each idiom. The sentence is what you remember under pressure."),
        trick("Format first",
              "Name the format before you start. Meaning, replace, complete or opposite. Each has its own first step."),
        trick("Same-meaning trap",
              "In an opposite question, the option with the same meaning as the idiom is always wrong.",
              "Opposite of A TOWER OF STRENGTH: (a) a strong supporter (b) an unreliable person (c) a tall building (d) a man of his word",
              ["A tower of strength gives firm support.", "Strong supporter and man of his word mean the same.", "An unreliable person is the opposite."],
              "(b) an unreliable person"),
    ],
)

if __name__ == "__main__":
    apply("idioms-phrases", SUBS)
