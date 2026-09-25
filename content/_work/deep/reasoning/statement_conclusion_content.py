# -*- coding: utf-8 -*-
"""Notes, patterns and pyqPatterns for statement-conclusion.json (imported by statement-conclusion.py)."""
from _lib import P, PYQ

NOTES_CONC = """### What is a statement-conclusion question?
You get a short **statement** (a news line, a rule, a notice, a fact with numbers) and two or three **conclusions**. A conclusion **follows** only if the statement alone makes it definitely true, or makes it the clear, intended meaning. You are not asked whether the conclusion is true in real life. You are asked: *does this statement force it?*

Think of yourself as a strict judge. The statement is the only evidence. Anything the statement does not say is not evidence, even if it is common knowledge.

### When a conclusion follows
1. **Restatement.** It says the same thing in other words. "The library is closed on all Sundays" → "A visitor on a Sunday will find it closed."
2. **Direct consequence.** It follows by simple logic or arithmetic. "360 km in 4.5 hours" → "average speed 80 km/h".
3. **Clear, soft implication.** Words like *some*, *may*, *likely*, *at least one* make a conclusion modest. "A 5% rebate is offered for early payment" → "Some owners are likely to pay early" follows.

### When a conclusion fails
| Trap | What it looks like | Example |
|---|---|---|
| Extreme word | only, all, always, never, best, must, completely | "Exercise is the **only** way to control BP" |
| Overgeneralisation | one case turned into every case | one festival month → "**every year** in festival months" |
| Outside cause | a reason the statement never gave | "sales rose" → "because prices fell" |
| Future guess | what will happen next time | "the metro **will** cut fares again" |
| Average as limit | average read as maximum or minimum | average 80 km/h → "never exceeded 80" |
| Necessary vs sufficient | "only X are eligible" read as "every X gets it" | ten years' service → "she **will** get the award" |

### The "only" and "every" rules
These two words are opposite gates and exams love them.
- **"Only X can get Y"** means X is *necessary*. It tells you who is **out** (the non-X). It does **not** say every X gets Y. Kiran scored 55% and only those with 60% are called → Kiran is not called ✓. Someone with 70% will be selected ✗.
- **"Every X gets Y"** means X is *sufficient*. If Arun is an X, Arun gets Y ✓. But it does not say *only* X get Y.

### Data statements
When the statement has numbers, do the arithmetic. Data conclusions are either forced or contradicted — rarely in between.
- Percentage change: (new − old) ÷ old × 100. ₹40 → ₹50 is 25%; ₹10 → ₹15 is 50%. A bigger rupee rise can be a smaller percentage rise.
- Average × count = total. An average of ₹30,000 for 5 people gives a total of ₹1,50,000, but it does **not** mean each person earns ₹30,000.
- Sales revenue is not profit — cost is unknown unless given.

### Worked example
Statement: The new flyover cut travel time between the station and the bus stand from 40 minutes to 15 minutes.
I. Travel time fell by 25 minutes — arithmetic, **follows**.
II. The flyover was very costly — never mentioned, **fails**.
III. Commuters between the two places now save time — clear implication, **follows**.
Answer: only I and III.

### Quick revision
- Only the statement is evidence. Real-life truth does not matter.
- Follows: restatement, arithmetic consequence, soft clear implication.
- Fails: new extreme word, overgeneralisation, outside cause, future guess, average read as a limit.
- "Only X" = gate (non-X are out). "Every X" = guarantee for each X.
- With numbers, always compute; revenue ≠ profit; average ≠ each value.
"""

NOTES_ASSUM = """### What is an assumption?
An **assumption** is an idea the speaker takes for granted *before* speaking. It is not written in the statement, but without it the statement would make no sense. When a mother says "Take your umbrella, it will rain", she assumes the umbrella will be useful and that you are going out. She never says so — she does not need to.

A conclusion comes *after* a statement (what follows from it). An assumption comes *before* it (what the speaker already believes). Keep these two apart.

### The negation test
This single test solves almost every question.
1. Take the assumption and put **not** into it.
2. Read the statement again with the negated idea in mind.
3. If the statement now becomes **pointless, foolish or self-defeating**, the assumption is **implicit**. If the statement still makes sense, the assumption is **not** implicit.

Example: Notice — "Use the stairs on Tuesday; the lift will be under repair." Assumption: the building has usable stairs. Negate it: "there are no usable stairs". Now the notice is absurd → implicit.

### Where assumptions come from
| Statement type | What it usually assumes |
|---|---|
| Advice ("Do X") | X is possible for the listener, and X will help |
| Appeal / request | the listener can and may respond |
| Notice | the readers will read it and can follow it |
| Advertisement | some buyers want what the hook offers |
| Decision / policy | the plan is feasible and will have *some* good effect |

### Assumptions that are NOT implicit
- **Total-effect claims.** "CCTV will completely stop signal jumping" — the authority only needs to expect *some* improvement. A 100% result is never required.
- **Comparisons with rivals.** An advert for a purifier need not assume it is the cheapest or the best; it only assumes people want safe water.
- **Contradictions.** An assumption that clashes with the statement ("tank cleaning will take a week" when the notice says 10 a.m. to 2 p.m.) cannot be implicit.
- **Extreme words.** "Nobody can...", "all people...", "only this method..." are rarely needed.
- **Things that would make the statement unnecessary.** "All riders already wear helmets" — if true, the helmet poster would be pointless, so the poster cannot assume it.

### Worked examples
1. Scheme: free cycles for girl students of Class IX to improve attendance. I. Some girls find it hard to reach school — negate: "none find it hard" → the scheme is pointless → **implicit**. II. Every girl will now attend daily — total effect → **not implicit**. Answer: only I.
2. The railway will add two coaches to a train during the festival season. I. More people are likely to travel then — negate: "no more people" → extra coaches pointless → **implicit**. II. The train can run with two extra coaches — negate: "it cannot" → the decision is impossible → **implicit**. Answer: both.

### Quick revision
- Assumption = unstated belief the statement depends on; it comes before the statement.
- Negation test: negate it; if the statement collapses, it is implicit.
- Advice and decisions assume feasibility and some benefit — both usually implicit.
- Reject total effects, rival comparisons, contradictions and extreme words.
- An assumption that would make the statement unnecessary is never implicit.
"""

NOTES_COA = """### What is a course of action?
The statement describes a **problem** or a situation. Each course of action is a proposed step. A course of action **follows** if a sensible authority would take it: it is **practical**, **proportionate** to the problem, and **related** to it. It should solve the problem, reduce its harm, or find out its cause.

Think of yourself as a calm, fair district officer. You do not panic, you do not punish everyone for one person's fault, and you do not ignore the problem.

### The three filters
1. **Relevance.** Does the action touch the stated problem? Poor maths results → appoint a maths teacher ✓; widen the village road ✗.
2. **Practicality.** Can it actually be done, by the proper authority, in reasonable time? Shifting a whole city's population because of a water shortage ✗.
3. **Proportion.** Is the response sized to the problem? A few students copying → act against those students and tighten invigilation ✓; cancel every student's result ✗.

### Actions that usually follow
- **Investigate**: inquiry, testing, inspection, tracing the culprits.
- **Repair or fix**: mend streetlights, correct display boards, improve drainage.
- **Relief**: rescue stranded families, send water tankers, keep hospital beds ready.
- **Awareness and regulation**: warn, advise, ration, regulate traffic until safety is checked.
- **Action as per rules** against those actually responsible.

### Actions that usually fail
- **Blanket bans**: ban all private buses because one operator overcharged.
- **Permanent shutdowns** for a one-time or local problem.
- **Punishing everyone** for the fault of a few.
- **Unrelated actions** that address a different problem.
- **Impossible or absurd steps**: stop the monsoon, never go out after dark.

### Two actions can both follow
Problems often need a **short-term relief** and a **long-term fix**. Flooded low-lying areas: send rescue teams now (relief) *and* improve drainage for the future (fix). Neither cancels the other. Do not reject a relief step because it is not permanent, and do not reject a long-term fix because it is not immediate.

### Investigate before punishing
When the cause is not yet known (a bridge cracks after two years), an **inquiry** followed by action against those found responsible is proportionate. Punishing a named person without an inquiry, or banning all bridges, is not.

### Worked example
Statement: The reservoir supplying a city has fallen to a very low level after poor rainfall.
I. Ration water and urge residents to save it — practical, related → **follows**.
II. Send tankers to areas with acute shortage — relief → **follows**.
III. Shift the population to another city — absurd and impractical → **fails**.
Answer: only I and II.

### Quick revision
- Follows = practical + proportionate + related to the stated problem.
- Good verbs: investigate, repair, relieve, regulate, warn, act as per rules.
- Bad verbs: ban all, shut forever, punish everyone, do something unrelated or impossible.
- Short-term relief and long-term fix can both follow.
- Unknown cause → inquiry first, then action against those responsible.
"""

P_CONC = [
 P("sc-p1", "Extreme word, overgeneralisation or outside cause", "very common",
   "The conclusion adds only / all / always / every year / because of, or predicts the future, while the statement is about one limited fact.",
   "1. Underline the key claim of the statement.\n2. Check the conclusion for new extreme words, a wider scope, a new cause or a future prediction.\n3. Any such addition means it does not follow; a plain restatement or 'at least one' version does.\n\n*Why it works:* the statement is the only evidence, so anything wider than it is unsupported.",
   "**Statement:** Metro ridership rose after fares were cut last month. **Conclusion:** The fare cut is the only reason ridership rose.",
   "'Only reason' is a new extreme claim — other causes are not ruled out. **Does not follow.**"),
 P("sc-p2", "Data-based conclusion (compute and compare)", "common",
   "The statement gives numbers — prices, counts, speeds, averages — and the conclusions state a difference, a percentage or a comparison.",
   "1. Compute exactly what the conclusion claims (difference, % change, total = average × count).\n2. If it matches, it follows; if it clashes, it fails.\n3. Reject claims about quantities not given (profit when only sales are known, maximum when only the average is known).\n\n*Why it works:* arithmetic either forces or contradicts a numeric claim.",
   "**Statement:** The average monthly salary of 5 employees is ₹30,000. **Conclusions:** I. Total salary is ₹1,50,000. II. Each earns ₹30,000.",
   "Total = 5 × 30,000 = ₹1,50,000 → I follows. An average says nothing about each person → II fails. **Only I.**"),
 P("sc-p3", "'Only X' and 'Every X' rule applied to a person", "common",
   "A rule with 'only those who…' or 'every … who…', then a named person and a conclusion about that person.",
   "1. 'Only X get Y' = X is necessary: non-X are out, but X are not guaranteed Y.\n2. 'Every X gets Y' = X is sufficient: any X gets Y.\n3. Place the named person against the rule and read off what is certain.\n\n*Why it works:* necessary and sufficient conditions run in opposite directions.",
   "**Statement:** Only students scoring at least 60% will be called for interview. Kiran scored 55%. **Conclusion:** Kiran will not be called.",
   "Kiran is below the gate, so she is out. **Follows.**"),
 P("sc-p4", "Restatement and clear implication (including three conclusions)", "common",
   "Conclusions that repeat the statement in other words or state its obvious purpose; sometimes three conclusions with pair options.",
   "1. Accept a conclusion that says the same thing in different words.\n2. Accept a soft, obvious implication (some, likely, can now).\n3. For three conclusions, judge each alone, then pick the matching combination.\n\n*Why it works:* a restatement cannot be false if the statement is true.",
   "**Statement:** The school will stay closed tomorrow due to a heavy-rain warning from the weather department. **Conclusions:** I. Students need not come to school tomorrow. II. The weather department has warned of heavy rain.",
   "Both repeat parts of the statement. **Both follow.**"),
]

P_ASSUM = [
 P("sc-p5", "Advice or request — the negation test", "very common",
   "Someone advises or requests: 'Do X', 'Please do X', 'Carry X'.",
   "1. Negate each assumption.\n2. If the advice becomes pointless (it would not help, or the listener cannot follow it), the assumption is implicit.\n3. If the advice still makes sense, or the assumption contradicts it, it is not implicit.\n\n*Why it works:* advice only makes sense if it is possible and useful.",
   "**Statement:** 'Wear a helmet while riding,' says a traffic poster. **Assumption:** A helmet can reduce head injuries.",
   "Negate: helmets do not reduce injuries → the poster is pointless. **Implicit.**"),
 P("sc-p6", "Advertisement or notice", "common",
   "An advert with a hook (price, speed, convenience) or a notice asking readers to do something.",
   "1. An advert assumes some buyers value its hook — implicit.\n2. It does not assume it beats every rival — not implicit.\n3. A notice assumes readers can act on it; anything contradicting the notice's own details is not implicit.\n\n*Why it works:* the advert or notice would be useless without its audience responding.",
   "**Advertisement:** 'Weekend yoga classes for busy office-goers.' **Assumptions:** I. Some office-goers are free on weekends. II. Office-goers cannot do yoga on weekdays.",
   "Negate I → nobody could attend → implicit. II is an extreme 'cannot' the advert does not need. **Only I.**"),
 P("sc-p7", "Total-effect or extreme assumption (trap)", "common",
   "One assumption says the step will work completely, for everyone, always.",
   "1. Spot the total words: completely, every, all, never again.\n2. A decision-maker needs only some benefit, so the total claim is not implicit.\n3. The modest partner ('some people may…') usually is implicit.\n\n*Why it works:* nobody plans only for perfect outcomes; partial benefit is enough reason to act.",
   "**Statement:** CCTV cameras will be installed at junctions to reduce signal jumping. **Assumption:** CCTV will completely stop signal jumping.",
   "Only some reduction is needed for the decision to make sense. **Not implicit.**"),
 P("sc-p8", "Decision or policy — feasibility and purpose", "common",
   "A government body or company announces a plan: add coaches, open a branch, launch a scheme.",
   "1. The plan assumes a need exists (customers, travellers, a problem to solve).\n2. It assumes the plan can actually be carried out.\n3. It does not assume unrelated extra steps (closing other branches) or total success.\n\n*Why it works:* a sensible authority acts only when there is a need and the step is possible.",
   "**Statement:** A company will open a branch in Pune to serve its growing customers there. **Assumption:** The company has customers in Pune.",
   "Negate: no customers in Pune → the branch has no purpose. **Implicit.**"),
]

P_COA = [
 P("sc-p9", "Practical fix vs blanket ban", "very common",
   "One action repairs, traces or regulates the problem; the other bans, withdraws or stops something for everyone.",
   "1. Ask whether the action targets the actual cause.\n2. Keep repairs, inquiries and action as per rules.\n3. Reject bans that punish the many for a local problem.\n\n*Why it works:* a sensible authority fixes the fault, not the whole system.",
   "**Statement:** Fake ₹500 notes are circulating in a district. **Actions:** I. Trace the gang printing them. II. Withdraw all ₹500 notes in the country.",
   "I targets the cause. II is a nationwide overreaction to a district problem. **Only I.**"),
 P("sc-p10", "Short-term relief plus long-term fix", "common",
   "A disaster or crisis, with one action giving immediate relief and another preventing a repeat (sometimes a third absurd action).",
   "1. Relief steps (rescue, tankers, extra beds) follow.\n2. Preventive steps (drainage, cleaning breeding sites) also follow.\n3. Reject only the absurd or extreme third option.\n\n*Why it works:* relief and prevention solve different parts of the same problem.",
   "**Statement:** Low-lying areas are flooded and families are stranded. **Actions:** I. Send rescue teams. II. Improve drainage in these areas.",
   "Relief now and prevention later are both sensible. **Both follow.**"),
 P("sc-p11", "Unrelated action", "common",
   "One action sounds useful in general but does not touch the problem stated.",
   "1. Name the problem in three words (poor maths results, wrong platform display).\n2. Keep actions that address those words.\n3. Reject anything aimed at a different issue, however good it sounds.\n\n*Why it works:* a course of action must follow from THIS statement, not from general wishes.",
   "**Statement:** Passengers miss trains because display boards show wrong platforms. **Actions:** I. Check and correct the display system. II. Reduce ticket prices.",
   "Only I touches the display problem. **Only I.**"),
 P("sc-p12", "Punish all vs act against those responsible", "common",
   "Wrongdoing by a few (copying, poor construction) with one action punishing everyone and another investigating or acting against the guilty.",
   "1. Keep action against those actually responsible, as per rules.\n2. Keep an inquiry when the cause is not yet known.\n3. Reject collective punishment of the innocent.\n\n*Why it works:* proportion means the response is aimed at the wrongdoers only.",
   "**Statement:** A few students were caught copying. **Actions:** I. Cancel results of all students. II. Act against those caught and tighten invigilation.",
   "I punishes the innocent. II is proportionate. **Only II.**"),
]

PYQS = [
 PYQ("Two conclusions (verbal)", "very common",
     "A notice, news line or fact followed by two conclusions I and II.",
     "Judge each conclusion only against the statement. Reject new extreme words, wider scope, outside causes and future guesses. Keep restatements and clear, soft implications.",
     "conclusions",
     "**Statement:** Sales of phones rose sharply in October this year. **Conclusions:** I. Every year phone sales rise in festival months. II. Phone prices were cut in October.",
     "I overgeneralises one year; II adds an unstated cause. **Neither follows.**"),
 PYQ("Data-based statement", "common",
     "The statement carries numbers — prices, marks, distances, averages.",
     "Do the arithmetic the conclusion claims. Percentages are on the old value; average × count = total; an average never fixes a maximum; sales are not profit.",
     "conclusions",
     "**Statement:** A notebook rose from ₹40 to ₹50 and a pen from ₹10 to ₹15. **Conclusion:** The notebook price rose by a larger percentage.",
     "Notebook 25%, pen 50% → **does not follow.**"),
 PYQ("Only-X eligibility trap", "common",
     "'Only those who…' or 'every… who…' with a named person.",
     "'Only X' is a gate: non-X are out, X are not guaranteed. 'Every X' is a guarantee: each X gets it. Read the person against the correct direction.",
     "conclusions",
     "**Statement:** Only employees with ten years' service are eligible for an award. Rekha has twelve years. **Conclusion:** Rekha will receive the award.",
     "Ten years is necessary, not sufficient → **does not follow.**"),
 PYQ("Three conclusions", "occasional",
     "Three conclusions; options list pairs or all three.",
     "Judge each conclusion separately, write ✓ or ✗ beside it, then match the pattern of ticks to the options.",
     "conclusions",
     "**Statement:** A flyover cut travel time from 40 to 15 minutes. I. Time fell by 25 minutes. II. The flyover was costly. III. Commuters save time.",
     "I ✓ (arithmetic), II ✗ (not mentioned), III ✓ → **only I and III.**"),
 PYQ("Statement and assumption", "common",
     "Advice, notice, advertisement or decision with two assumptions.",
     "Use the negation test: negate the assumption; if the statement becomes pointless, it is implicit. Reject total effects, rival comparisons and contradictions.",
     "assumptions",
     "**Statement:** 'Book tickets early to avoid the rush.' **Assumption:** There is likely to be a rush.",
     "Negate: no rush → the advice is pointless → **implicit.**"),
 PYQ("Decision / policy assumption", "common",
     "A government or company decision followed by assumptions about need and feasibility.",
     "A decision assumes a need exists and that the step can be carried out. It does not assume total success or unrelated extra steps.",
     "assumptions",
     "**Statement:** Two extra coaches will be added to a train in the festival season. **Assumption:** The train can run with two extra coaches.",
     "Negate: it cannot → the decision is impossible → **implicit.**"),
 PYQ("Course of action", "common",
     "A problem is described; two or three proposed actions.",
     "Keep practical, proportionate and related steps — investigate, repair, relieve, regulate, act as per rules. Reject bans, permanent shutdowns, collective punishment and unrelated steps.",
     "courses-of-action",
     "**Statement:** Several hostel students fell ill after dinner. **Actions:** I. Test the food and inspect the kitchen. II. Shut the hostel permanently.",
     "I is proportionate; II is an overreaction → **only I.**"),
 PYQ("Relief plus prevention", "occasional",
     "A crisis with one immediate-relief action and one long-term preventive action.",
     "Both types are valid and do not cancel each other. Reject only the third, absurd option if there is one.",
     "courses-of-action",
     "**Statement:** Dengue cases have risen sharply. **Actions:** I. Fogging and removal of stagnant water. II. Hospitals keep extra beds ready.",
     "Prevention and relief → **both follow.**"),
]
