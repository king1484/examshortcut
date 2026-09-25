# Notes + per-subtopic patterns for sentence-rearrangement (Phase 2 deep content).
from _lib import P

S = {}

S["rearr-pqrs-method"] = {
"notes": """### What the four middle parts are doing
Every PQRS middle is a small paragraph with a job to do between S1 and S6. Before you look at the options, give each part a one-word role:
- **Lead** — continues S1's subject with a general statement or a pronoun that points back to S1.
- **Support** — an example, a figure, a detail ('for example', 'in Kerala', 'children who read daily').
- **Turn** — a contrast or problem ('But', 'However', 'Yet', 'Sadly', 'Unfortunately').
- **Close** — a result, a solution or a lesson ('therefore', 'thus', 'that is why', 'the next step').
Once each part has a role, there are usually only one or two orders left to check.

### Two skeletons that cover most items
**Argument skeleton:** Lead -> Support -> Turn -> Close. *Solar power is spreading* -> panels light homes -> as a result children study -> however panels break down -> training technicians is therefore the next step.

**Problem skeleton:** Problem -> Cause -> Effect -> Response. *Lakes are dying* -> sewage flows in -> this fills them with weeds -> citizens now clean them. The Response part nearly always sits just before S6, because S6 usually looks ahead.

If the parts fit one skeleton, write the order down before you look at the options.

### S1 and S6 are clamps
- **S1 names the subject.** A part that begins 'Its route...', 'They do so because...' or 'The name referred to...' can only make sense directly after S1. That is the **S1 hook**, and it fixes the first letter.
- **S6 often points backwards.** 'It was the tastiest lunch...' needs the meal to have been mentioned just before; 'Subsidies for such machines...' needs the machines. Ask what S6's pronoun or 'such' points to. The part that supplies it is the last letter. That is the **S6 pull-back**.

With the first and last letters fixed, only two orders remain for the middle two parts, and one mandatory pair decides between them.

### The two-pair lock
Most items are designed so that two links settle everything. For example, with P-S (a pronoun pair) and R-Q (an 'as a result' pair), the answer must contain both blocks. Only PSRQ and RQPS are possible, and S1 or S6 decides which. Look for the two strongest links first instead of building the whole paragraph in your head.

### How setters build the wrong options
The three wrong strings are rarely random. Usually each one:
1. swaps two neighbouring parts (breaks one pair),
2. moves the Close part into the middle, or
3. opens with a pronoun or connector part.
When you pick your answer, name the link each wrong string breaks. If you cannot find one, check again.

### Quick revision
- Tag every part: Lead, Support, Turn, Close.
- Argument: Lead -> Support -> Turn -> Close. Problem: Problem -> Cause -> Effect -> Response.
- S1 hook fixes the first part; S6 pull-back fixes the last one.
- Two strong pairs usually decide the item — find them before reading the options.
- Every wrong string breaks a pair: name the pair it breaks.
""",
"patterns": [
 P("rpm1", "Argument skeleton (claim, support, turn, close)", "very common",
   "S1 makes a general claim; one part adds a detail or result, one begins with However/Yet, one carries therefore/thus.",
   "1. Tag the parts: Lead, Support, Turn, Close.\n2. Place the Support directly after what it supports (look for 'as a result', 'for this reason').\n3. The Turn follows the good news it contradicts; the Close sits before S6.\n\n*Why it works:* opinion paragraphs in exams almost always follow this fixed order.",
   "S1: Solar power is spreading. Parts: panels light homes / as a result children study / however these panels break down / training technicians is therefore the next step.",
   "Lead (panels) -> Support ('as a result') -> Turn ('However, these panels') -> Close ('therefore') before S6."),
 P("rpm2", "Problem skeleton (problem, cause, effect, response)", "common",
   "S1 states a problem (lakes dying, stubble burning); parts give a reason, a consequence introduced by 'This has...', and a response or remedy.",
   "1. Find the cause part — it explains S1 directly ('Untreated sewage flows in', 'They do so because').\n2. Attach the effect to it ('This has filled...').\n3. The response or remedy goes last, just before S6.\n\n*Why it works:* a remedy cannot come before the harm it answers, so the chain runs in only one direction.",
   "S1: Lakes are dying. Parts: sewage flows in / this has filled them with weeds / as the weeds choke the water, fish vanish / citizens now clean them.",
   "Cause -> 'This has' effect -> 'the weeds' result -> response last."),
 P("rpm3", "S6 pull-back", "very common",
   "S6 begins with a pronoun, 'such', or a word that needs something mentioned just before it (It was the tastiest lunch; Subsidies for such machines).",
   "1. Read S6 first and circle what it points back to.\n2. The part that supplies that noun is the last part.\n3. Build the rest backwards from it.\n\n*Why it works:* S6 is fixed, so whatever it refers to must come directly before it.",
   "S6: It was the tastiest lunch the school had ever served. One part: The harvest was cooked for the midday meal.",
   "'It' in S6 = the midday meal, so the harvest part is last; the other three follow the growing season before it."),
 P("rpm4", "S1 hook", "common",
   "One part begins with a word that only makes sense directly after S1: Its route..., The name referred to..., They do so because...",
   "1. Find the part whose first words point to S1's subject or action.\n2. Make it the first letter.\n3. Continue the chain from it using pairs.\n\n*Why it works:* 'The name' or 'They do so' has nothing to refer to anywhere except S1.",
   "S1: Chess was born in India as a game called chaturanga. Part: The name referred to the four divisions of an ancient army.",
   "'The name' = chaturanga in S1, so this part comes first; 'These divisions' must follow it."),
 P("rpm5", "Two-pair lock", "common",
   "Two parts are tied by pronouns or 'this + noun', and another two by 'as a result', 'because of these', or 'Its price'.",
   "1. Find the two strongest pairs and write them as blocks.\n2. Only two strings can contain both blocks.\n3. Use S1 or S6 to choose between them.\n\n*Why it works:* two unbreakable blocks cut 24 possible orders down to two.",
   "Parts: He used sand and clay / Because of these cheap materials, it cost little / Its low price made it popular / Impressed by this demand, an agency ordered more.",
   "Each part points back to the one before it, so the chain is fixed: materials -> cost -> price -> demand."),
]}

S["rearr-openers-closers"] = {
"notes": """### Why openers are easier to spot than middles
The first part after S1 has to connect to S1 alone, so there is only one link to check. Every other part has to connect to parts you have not placed yet. Settle the opener first, then build the chain from it.

The fastest test is the **orphan test**. Read each part as if it came straight after S1. A part fails if it contains:
- a pronoun whose noun appears only in another part ('It sat down beside the principal' when the dog is introduced in a middle part),
- a 'this/these + noun' that S1 does not supply ('This ability...', 'These halls...'),
- a follow-on word such as 'also', 'even', 'others', 'too', 'in the morning'.
Usually two or three parts fail, and the opener is obvious.

### Connectors inside a PQRS item
Connector words (However, Yet, But, Therefore) cannot open a free paragraph. In a PQRS item, though, S1 is already there, so a connector part can follow S1 directly when S1 is the claim it responds to. 'Many students think maths is only for the gifted. However, this belief is not true.' — here 'However, this belief' is the right first part, because 'this belief' is S1.

So the real rule is: **a connector follows the claim it turns on.** If that claim is S1, the connector part comes first; if the claim is in another part, it comes right after that part.

### Closers and S6
The Close part usually carries a signal: therefore, thus, hence, clearly, that is why, the need of the hour, the next step. Two checks confirm it:
1. It must follow everything it summarises — 'Hence, experts warn the species could vanish' needs the threats listed first.
2. It must lead naturally into S6. If S6 is itself a conclusion ('Saving it will need urgent action'), the Close part prepares for it.

### General before specific
When two parts could both open, choose the more general one. 'Each region cooks with what grows around it' comes before 'In Kerala, for example...'. An example needs the claim it illustrates. The words 'for example', 'in Punjab', 'during deep sleep' mark specific parts.

### Order of work
1. Orphan test on all four parts -> the opener.
2. Signal words -> the closer.
3. The two middle parts -> one pair decides.

### Quick revision
- Orphan test: pronoun, 'this + noun', also/even/others -> cannot open.
- A connector follows the claim it turns on — which can be S1 itself.
- Closers: therefore, thus, hence, clearly, that is why — they follow everything they summarise.
- General claim before its example; 'for example' is never first.
- Opener, then closer, then one pair for the middle.
""",
"patterns": [
 P("roc1", "Orphan test for the opener", "very common",
   "Two or three parts begin with pronouns or 'this + noun' (It sat down..., This ability..., Their protest...), and only one part introduces a new noun.",
   "1. Read each part as if it came straight after S1.\n2. Remove every part whose pronoun or 'this + noun' has nothing to refer to in S1.\n3. The part that remains is the opener; attach the pronoun parts to it.\n\n*Why it works:* a pronoun cannot come before the noun it refers to, so the part that introduces the noun must come first.",
   "S1: The morning assembly began as usual. Parts: Suddenly, a stray dog walked onto the stage / It sat down beside the principal / ...",
   "'It' fails the orphan test (S1 has no dog), so the 'stray dog' part opens and the 'It' part follows it directly."),
 P("roc2", "Connector follows the claim it turns on", "common",
   "One part begins with However/But/Yet and S1 (or another part) states the claim it disputes.",
   "1. Find the claim the connector answers ('this belief', 'the same device').\n2. If the claim is S1, the connector part comes first; otherwise it follows the part that makes the claim.\n3. Place its example or support right after it.\n\n*Why it works:* a contrast needs something to contrast with, and that must come just before it.",
   "S1: Many students think maths is only for the gifted. Part: However, this belief is simply not true.",
   "'This belief' is S1's claim, so the However part comes first; the research and the example support it; 'Therefore' closes."),
 P("roc3", "Closing signal part", "very common",
   "One part carries hence/therefore/clearly/that is why, or proposes a solution, and S6 is a final judgement.",
   "1. Mark the part with the closing signal.\n2. Check that everything it summarises comes before it.\n3. Place it last, just before S6, and order the rest.\n\n*Why it works:* a conclusion depends on all the points before it, so it can only go at the end.",
   "S1: Traffic jams waste millions of hours. Parts include: Clearly, the answer lies in moving people, not vehicles.",
   "'Clearly' concludes the cause, the failed fix and the contrast, so it sits just before S6."),
 P("roc4", "General before specific", "common",
   "One part makes a general claim and one or two begin with 'for example', 'in Kerala', 'during deep sleep', or name a particular case.",
   "1. Find the general claim that the specific parts illustrate.\n2. Place it before its examples.\n3. Pair the examples ('for example' ... 'on the other hand').\n\n*Why it works:* an example only makes sense after the claim it illustrates.",
   "S1: Indian cuisine changes every few hundred kilometres. Parts: Each region cooks with what grows around it / In Kerala, for example... / In Punjab, on the other hand...",
   "The general part leads, then Kerala, then Punjab ('on the other hand' needs the first example), then the summary."),
]}

S["rearr-mandatory-pairs"] = {
"notes": """### Not all links are equally strong
A mandatory pair is two parts that must sit side by side. Rank the links you find, and trust the strong ones first:

| Strength | Link | Example |
|---|---|---|
| Very strong | Personal pronoun -> its only noun | a stray dog ... **It** sat down |
| Very strong | a + noun -> the + same noun | **a small bag** ... **The bag** was full of gold |
| Very strong | this/these/such + noun -> the part that names it | a huge challenge ... **this challenge** |
| Strong | As a result / Because of this / This has led to -> the cause | sewage flows in ... **This has** filled |
| Strong | Place words: There, Here, Inside -> the place named | moved to the US ... **There** she earned a doctorate |
| Medium | But / Yet / However -> the claim it contradicts | reach in seconds ... **Yet** a letter carries... |
| Weak | Same topic, no grammar link | two parts both about trains |

When two links point to different orders, the stronger one wins. Never break a pronoun pair to satisfy a weak topic link.

### Hidden pointers
Some pointer words are easy to miss:
- **also, too, as well** — the part is a second item and needs a first one before it.
- **Others, Some, the rest** — 'Others have built study halls' needs 'Many now lend e-books' before it.
- **Even** — 'Even the principal could not keep a straight face' needs others laughing first.
- **the same, such, so many** — they point back to a noun or number already given.

### Pairs join into chains
Pairs link up: if P-S is a pair and S-Q is a pair, then P-S-Q is one block of three. Most items are designed so that pairs cover three of the four parts and one more fact places the last part. Write the blocks down as you find them — PS, SQ -> PSQ — and the answer is almost complete.

### Checking a pair
Read the two parts together aloud. A true pair reads as one smooth thought. A false pair makes you ask 'which one?' or 'what is this about?' Check number and gender too: 'its' cannot refer to 'workers', and 'she' cannot refer to 'the farmer' if the farmer is a man.

### Contrast pairs need care
'But', 'Yet' and 'However' are only medium-strength links, because the claim they contradict can sometimes be in S1 rather than in a part. Confirm with the content: 'Yet a letter carries something a message cannot' contrasts with the speed of messages, so it must come right after the part about emails.

### Quick revision
- Rank links: pronoun, a->the, this + noun, as a result, place word > contrast > same topic.
- Hidden pointers: also, others, even, such, the same.
- Pairs join into blocks (PS + SQ = PSQ); two or three blocks usually decide the item.
- Read the pair together; check number and gender.
- The stronger link always wins.
""",
"patterns": [
 P("rmp1", "Noun -> pronoun / place-word pair", "very common",
   "One part names a person, animal or place; another begins with He/She/It/There referring to it.",
   "1. List each pronoun or place word and find the only part that names what it refers to.\n2. Join those two parts as a block.\n3. Check number and gender (she -> the science teacher, not Ravi).\n\n*Why it works:* a pronoun has to come after its noun, and usually straight after it.",
   "S1: Ravi found an injured sparrow. Parts: He carried it to the science teacher / She cleaned its wing / ...",
   "'She' can only be the science teacher, so the two parts form a pair."),
 P("rmp2", "a -> the pair", "very common",
   "A noun appears first with a/an in one part (a small bag, a small room) and with 'the' in another (The bag, the room).",
   "1. Scan for nouns that appear twice.\n2. The part with 'a + noun' comes before every part with 'the + same noun'.\n3. If the 'the' part adds detail about the object, place it directly after.\n\n*Why it works:* English introduces a thing with 'a' and refers back to it with 'the'.",
   "Parts: the old man left a small bag on the doorstep / The bag was full of gold coins.",
   "'a small bag' introduces it; 'The bag' refers back, so the order is fixed."),
 P("rmp3", "this / these + abstract noun", "common",
   "A part begins with 'this challenge', 'this effort', 'this system', 'this decline', and exactly one other part describes that challenge, effort or system.",
   "1. Underline the abstract noun after 'this'.\n2. Find the part that describes it without naming it that way.\n3. Join them; a chain of 'this' words can link three parts.\n\n*Why it works:* 'this + noun' sums up the idea just before it.",
   "Parts: Keeping so many trains on time is a huge challenge / To meet this challenge, the railways track trains by satellite / This system shows every engine's position.",
   "Challenge -> this challenge -> this system: a chain of three."),
 P("rmp4", "Contrast pair (claim -> but / yet / however)", "common",
   "One part begins with But/Yet/However and contradicts something — speed vs feeling, promise vs suitability.",
   "1. Identify exactly what the contrast part contradicts.\n2. Place it directly after the part that says that, or after S1 if S1 says it.\n3. The explanation of the contrast follows it.\n\n*Why it works:* a contrast only makes sense straight after the claim it contradicts.",
   "Parts: Emails reach people in seconds / Yet a letter carries something a message cannot / The handwriting and the paper bring the writer closer.",
   "Speed claim -> 'Yet' contrast -> what the something is: a fixed chain."),
]}

S["rearr-time-sequence"] = {
"notes": """### Three layers of time
A narrative item gives you time information at three levels. Use as many as you need:
1. **Markers** — dates and time words: Last December, In 2008, A few days later, That night, By dawn, The next morning, Today.
2. **Tense** — past perfect (had left) for earlier events, simple past for the main events, present (Today, only tourists climb...) for the end.
3. **Cause and effect** — the fire must start before the engines arrive; the lander must fail before it is redesigned.
Markers are the most reliable. When they are missing, use tense; when tense does not help, use cause and effect.

### Relative markers need an anchor
'Eleven years later', 'A few days later', 'Within ten minutes of the restart', 'On the eighth day' all measure from an earlier event. They cannot come first. Find the event they count from and place them after it: 'Eleven years later' needs 'In 2008'; 'the restart' needs 'half-time'.

### By-phrases close a phase
'By dawn, the flames had been put out.' 'By the final whistle, we had won.' A by-phrase describes where a stretch of action ended up, so it follows the actions inside that stretch. Setters often place it first in the wrong options.

### Flashbacks in the past perfect
'When Anil reached the station, the platform was empty. The express had left ten minutes earlier. He had missed it because he had overslept.' The past perfect parts explain the scene, and the story returns to the simple past afterwards ('Cursing his bad luck, he checked the board'). Keep the flashback parts together, directly after the scene they explain.

### Process and instruction passages
Recipes, procedures and application steps use **First -> Next / Then -> After that -> Finally**. When the markers are partly missing, use what each step needs: you cannot book an appointment before registering, and the officials cannot check documents before the appointment exists. 'At the appointment' needs a part that mentions booking it.

### Biography and history
Lives and events run in date order, but look for pointer words too: 'There she earned a doctorate' needs the part naming the country; 'Her second mission' needs the first one. Exam biographies often skip years, so rely on 'first', 'second', 'later' and 'then' as well as dates.

### Quick revision
- Use markers first, then tense, then cause and effect.
- 'Eleven years later', 'a few days later' and 'the restart' need an earlier event before them.
- By-phrases (by dawn, by the final whistle) come after the actions they sum up.
- Past perfect = flashback; keep those parts together, straight after the scene.
- Processes: each step needs the one before it — you cannot book before you register.
""",
"patterns": [
 P("rts1", "Explicit time and date markers", "very common",
   "Parts carry dates or time words: Last December, In 2008, Eleven years later, In August 2023, As soon as they reached.",
   "1. Underline every time word.\n2. Place fixed dates in order; attach each relative marker after its anchor.\n3. Fill in any part without a marker by cause and effect.\n\n*Why it works:* the markers put the events in order before you even read the options.",
   "Parts: In 2008, Chandrayaan-1 ... / Eleven years later, Chandrayaan-2's lander crashed / Scientists studied the failure / In August 2023, Chandrayaan-3 landed.",
   "2008 -> 'eleven years later' -> 'the failure' -> 2023: the markers and one pointer word fix the order."),
 P("rts2", "By-phrases and day boundaries", "common",
   "One part begins with By dawn / By the final whistle / By midnight, or with That night / The next morning.",
   "1. Find the actions the by-phrase sums up and place it after them.\n2. Place day-boundary parts (the next morning) after everything from the day before.\n3. Check that S6 continues from the last part.\n\n*Why it works:* a by-phrase describes the result of the actions before it, so it can never come first.",
   "S1: A fire broke out late on Saturday night. Parts: shopkeepers rushed out / engines arrived within twenty minutes / By dawn, the flames were out / Later that morning, officials counted the damage.",
   "People nearby act first, then the engines; 'By dawn' sums up the firefighting; 'later that morning' comes after dawn."),
 P("rts3", "Tense as a clock (past perfect flashback)", "common",
   "Parts mix had + V3 (had left, had built, had attacked) with simple past and present; there are few time words.",
   "1. Past perfect parts = earlier events or background; keep them together in order.\n2. Simple past parts continue the main story after them.\n3. Present-tense parts (Today...) come last.\n\n*Why it works:* tense shows the order of events even when there are no time words.",
   "S1: The old fort stood silent. Parts: a king had built it / armies had attacked it / over time the route shifted / today only tourists climb it.",
   "had built -> had attacked -> simple past 'shifted' -> present 'Today'."),
 P("rts4", "Process steps", "common",
   "The passage explains how to do something (a paper boat, a passport application) with First/Next/Then/Finally or steps that depend on each other.",
   "1. Use First/Finally to fix the ends.\n2. For steps without markers, ask which step each one needs before it.\n3. A step that mentions something (the appointment) comes after the step that creates it.\n\n*Why it works:* each step depends on the one before, so the order is forced.",
   "Parts: registers on the portal / After paying the fee, books an appointment / At the appointment, officials check documents / A police verification follows.",
   "Register -> pay and book -> the appointment -> verification: each step needs the one before it."),
]}

S["rearr-strategy"] = {
"notes": """### A 40-second routine
1. **Read S1 and S6 (5 s).** Note the subject and what S6 refers back to.
2. **Tag the parts (15 s).** Mark pronouns, 'this + noun', connectors, time words and closing signals.
3. **Fix one end and one pair (10 s).** The opener (orphan test) or the closer (S6 pull-back), plus the strongest pair.
4. **Eliminate (10 s).** Remove every string that breaks that end or pair; usually one is left.
You do not need to be sure of the whole paragraph — you only need to rule out three strings.

### Jumbles with no fixed ends
Without S1 and S6 you lose both clamps, so:
- Find the **independent sentence**: no pronoun pointing back, no connector, no 'this + noun', no 'also'. It opens.
- Find the **strongest pair** (a->the, pronoun, this + noun) and extend the chain from the opener.
- The **closer** is the part with a conclusion signal or a 'this + noun' that sums up the whole problem ('close this gap').
Setters often write two sentences that look independent. Choose the more general one, or the one the other refers to.

### First-sentence and last-sentence questions
Some papers ask only which sentence comes first or last. Do not arrange all four:
- **First:** apply the orphan test to every sentence. The one that passes is the answer. If two pass, the more general one wins.
- **Last:** look for the sentence that sums up ('Such conveniences...', 'Greed had cost him...') or completes the final step of a story or process, and check that nothing else must follow it.
This takes 20-30 seconds.

### When two strings survive
If you are left with two strings such as QRPS and QPRS, find the parts that are in different positions (here R and P) and test only those neighbours. Does P's 'But it has also' need R's 'This has made life easier' before it? Checking one small difference is faster than rereading the whole paragraph.

### Common traps
- **Nearly-right strings:** the wrong options often keep the correct opener and closer and swap two middle parts. Check the middle pair even when both ends match.
- **Topic similarity:** two parts about the same subject are not necessarily a pair. Only grammar links (pronoun, a->the, this + noun, connector) are reliable.
- **A strong-sounding first line:** a part with a date ('In August 2023...') feels like an opener but may be the end of the story. Check the anchors.

### Quick revision
- Routine: read S1 and S6 -> tag the parts -> fix one end and one pair -> eliminate.
- No fixed ends: independent sentence first, strongest pair next, summary last.
- First/last questions: orphan test for first; summary or final step for last.
- Two strings left: test only the parts that differ.
- Grammar links beat topic similarity; dates can be endings, not openers.
""",
"patterns": [
 P("rst1", "Paragraph jumble with no fixed ends", "common",
   "Four sentences labelled P, Q, R, S with no S1 or S6; the options are four-letter strings.",
   "1. Find the independent sentence (no pronoun, connector, 'this + noun' or 'also') — it opens.\n2. Attach the strongest pair to it.\n3. The summary or 'this + noun' sentence closes.\n\n*Why it works:* without S1 and S6, the opener has to be the one sentence that needs nothing before it.",
   "P: At the same time, many families go hungry. Q: Every year, millions of tonnes of food are wasted. R: Better cold storage could close this gap. S: Much of it rots in storage.",
   "Q is the only independent sentence; S ('Much of it') follows; P adds the contrast; R ('this gap') closes: QSPR."),
 P("rst2", "Which sentence comes first?", "common",
   "The options are just the labels P, Q, R, S and the question asks for the opening sentence.",
   "1. Apply the orphan test to each sentence.\n2. Remove every sentence with a pronoun, 'this + noun', a connector or a relative time marker.\n3. The remaining sentence is the answer.\n\n*Why it works:* you only need the opener, so arranging the other three is wasted time.",
   "P: Their destination was Dandi. Q: On reaching the sea, he picked up salt. R: In 1930, Gandhiji set out from Sabarmati Ashram. S: This simple act inspired millions.",
   "P ('Their'), Q ('he') and S ('This act') all point back; R introduces Gandhiji — R is first."),
 P("rst3", "Which sentence comes last?", "common",
   "The options are just the labels and the question asks for the closing sentence.",
   "1. Look for the sentence that sums up ('Such conveniences...', 'Greed had cost him...') or completes the last step of a story.\n2. Check that no other sentence needs to follow it (nothing else points back to it).\n3. Confirm by building the chain backwards.\n\n*Why it works:* the last sentence is the one that refers back to others but that nothing refers back to.",
   "P: Others follow this trail and carry the food home. Q: Each colony divides work. R: When a worker finds food, it leaves a trail. S: Ants are very organised.",
   "P's 'this trail' needs R, and nothing refers back to P — P is last."),
 P("rst4", "Two strings left: test only the difference", "very common",
   "You have ruled out two strings, and the remaining two differ only in the positions of two neighbouring parts.",
   "1. Write the two surviving strings one above the other.\n2. Identify the two parts that switch places.\n3. Test only that link: does one of them point back to the other?\n\n*Why it works:* the correct string and the closest wrong one differ at a single point, so testing that point decides the item.",
   "Survivors QRPS and QPRS. R: This has made life easier. P: But it has also created chances for fraud.",
   "'But it has also' needs the benefit in R before it, so R comes before P: QRPS."),
]}
