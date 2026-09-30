"""Rewrite reasoning/statement-conclusion.json (Phase 3 readable lessons).

Logic is checked by enumerating every possible world (all True/False combinations)
and testing whether a conclusion holds in all worlds that satisfy the statement.
Numbers are checked with Fraction.
"""
import itertools
import json
from fractions import Fraction as F
from pathlib import Path

TOPIC = Path(__file__).resolve().parents[4] / "content/core/topics/reasoning/statement-conclusion.json"


def follows(names, rules, concl):
    """Conclusion follows if it is true in every world where all rules hold."""
    for vals in itertools.product([False, True], repeat=len(names)):
        w = dict(zip(names, vals))
        if all(r(w) for r in rules) and not concl(w):
            return False
    return True


def consistent(names, rules):
    return any(all(r({**dict(zip(names, v))}) for r in rules) for v in itertools.product([False, True], repeat=len(names)))


def implies(a, b):
    return (not a) or b


def pat(pid, name, freq, spot, steps, why, q, ex_steps, answer):
    return {"id": pid, "name": name, "frequency": freq, "howToSpot": spot, "formula": None,
            "steps": steps, "why": why, "example": {"q": q, "steps": ex_steps, "answer": answer}}


def ex(q, steps, answer):
    return {"q": q, "steps": steps, "answer": answer}


# ====================== checks: conclusions ======================
# only-rule: called -> score>=60 ; Kiran scored below 60
N = ["called", "s60"]
R = [lambda w: implies(w["called"], w["s60"]), lambda w: not w["s60"]]
assert follows(N, R, lambda w: not w["called"])                       # sc-p3 follows
R2 = [lambda w: implies(w["called"], w["s60"]), lambda w: w["s60"]]
assert not follows(N, R2, lambda w: w["called"])                       # 70% does not guarantee a call
# every-rule: service>=10 -> award
N = ["service10", "award"]
R = [lambda w: implies(w["service10"], w["award"]), lambda w: w["service10"]]
assert follows(N, R, lambda w: w["award"])                             # sc-p15 follows
R = [lambda w: implies(w["service10"], w["award"]), lambda w: w["award"]]
assert not follows(N, R, lambda w: w["service10"])                     # converse does not follow
# necessary vs sufficient: graduate only can apply; Riya is a graduate; selected ->applied->grad
N = ["grad", "applied", "selected"]
R = [lambda w: implies(w["applied"], w["grad"]), lambda w: implies(w["selected"], w["applied"]), lambda w: w["grad"]]
assert not follows(N, R, lambda w: w["selected"])
assert follows(N, R, lambda w: implies(w["selected"], w["grad"]))
# rain closure: school closed because of warning
N = ["closed", "warning"]
R = [lambda w: w["closed"], lambda w: w["warning"]]
assert follows(N, R, lambda w: w["closed"]) and follows(N, R, lambda w: w["warning"])
# ridership: fare cut -> ridership rose; other causes possible
N = ["farecut", "othercause", "rose"]
R = [lambda w: w["rose"], lambda w: w["farecut"], lambda w: implies(w["farecut"] or w["othercause"], w["rose"])]
assert consistent(N, R) and not follows(N, R, lambda w: not w["othercause"])
# arithmetic
assert F(5 * 30000) == 150000 and F(360) / F(9, 2) == 80
assert 40 - 15 == 25 and F(50 - 40, 40) == F(1, 4) and F(15 - 10, 10) == F(1, 2)
assert F(92 - 80, 80) == F(3, 20) and 92 - 80 == 12 and F(12, 92) != F(1, 5) and F(92 - 80, 80) * 100 == 15
assert F(80 - 92, 92) < 0 and round(float(F(12, 92)) * 100, 1) == 13.0
assert F(500 - 400, 400) == F(1, 4)
# tricks
assert F(720, 9) == 80  # 720 km in 9 hours is 80 km/h
assert F(45, 30) == F(3, 2)

CONCLUSIONS = dict(
    concept=(
        "You get a short statement and some conclusions. A conclusion follows only if the statement alone forces it. "
        "Real-life truth does not matter. Use only the statement as evidence."
    ),
    notes=r"""### What the question asks
You get a short **statement**: a news line, a rule, a notice or a fact with numbers. Then you get two or three **conclusions**.

A conclusion **follows** if the statement alone makes it definitely true, or makes it the clear meaning. You are not asked if it is true in real life. You are asked: does this statement force it?

Think of yourself as a strict judge. The statement is the only evidence. Anything it does not say is not evidence, even if everyone knows it.

### When a conclusion follows
1. **Restatement.** It says the same thing in other words. "The library is closed on all Sundays" gives "A visitor on a Sunday will find it closed."
2. **Direct consequence.** It comes from simple logic or arithmetic. "360 km in 4.5 hours" gives "average speed 80 km/h".
3. **Soft, clear implication.** Words like *some*, *may*, *likely* keep a conclusion modest. "A 5% rebate for early payment" gives "Some owners are likely to pay early".

### When a conclusion fails
| Fault | What it looks like | Example |
|---|---|---|
| Extreme word | only, all, always, never, best, must | "Exercise is the **only** way to control BP" |
| Too general | one case becomes every case | one festival month becomes "**every year**" |
| Outside cause | a reason the statement never gave | "sales rose" becomes "because prices fell" |
| Future guess | what will happen next time | "the metro **will** cut fares again" |
| Average as limit | an average read as a maximum | average 80 km/h becomes "never above 80" |
| Wrong direction | "only X can" read as "every X will" | ten years' service becomes "she **will** get the award" |

### The rules for only and every
These two words are opposite gates. Exams use them often.

> **Rule:** "Only X can get Y" means X is needed. It tells you who is **out**: everyone who is not X. It does not say every X gets Y.

> **Rule:** "Every X gets Y" is a guarantee for each X. If Arun is an X, Arun gets Y. It does not say only X get Y.

Kiran scored 55%, and only those with 60% are called. So Kiran is not called. But a student with 70% is not sure to be called.

### Data statements
When the statement has numbers, do the sums. Data conclusions are usually forced or contradicted.

- **Percentage change:** (new − old) ÷ old × 100. From ₹40 to ₹50 is 25%. From ₹10 to ₹15 is 50%. A bigger rupee rise can be a smaller percentage rise.
- **Average and total:** an average of ₹30,000 for 5 people gives a total of ₹1,50,000. It does not mean each person earns ₹30,000.
- **Revenue and profit:** sales are not profit. The cost is unknown unless it is given.

### Soft words and hard words
*Some*, *may*, *likely* and *at least one* are safe. *All*, *only*, *always* and *never* are risky. A soft conclusion passes if it is a fair reading. A hard word passes only if the statement used it too.

### A worked example
**Statement:** The new flyover cut the travel time between the station and the bus stand from 40 minutes to 15 minutes.

- I. Travel time fell by 25 minutes. This is arithmetic, so it follows.
- II. The flyover was very costly. The statement never says so, so it does not follow.
- III. Commuters now save time. This is a clear implication, so it follows.

Answer: only I and III.
""",
    formulas=[],
    tricks=[
        {"title": "The extreme-word filter",
         "body": "Circle words like only, all, always, never, surely, best, entire and must. If the conclusion has one and the statement does not, it almost always fails.",
         "example": ex("Statement: Regular exercise helps control blood pressure. Conclusion: Exercise is the only way to control blood pressure. Does it follow?",
                       ["The conclusion has the word 'only'. The statement does not.", "The statement says exercise helps. It does not say nothing else works."], "Does not follow")},
        {"title": "Needed is not the same as enough",
         "body": "'Only X can do Y' means X is required. It does not mean X is enough. Check which way the conclusion runs.",
         "example": ex("Statement: Only graduates can apply for the post. Riya is a graduate. Conclusion: Riya will be selected. Does it follow?",
                       ["Being a graduate is needed to apply.", "It does not guarantee selection."], "Does not follow")},
    ],
    mistakes=[
        {"wrong": "Judging the conclusion by what is true in real life.", "right": "Judge it only by the statement. Real-life facts are not evidence."},
        {"wrong": "Accepting a conclusion because it sounds sensible.", "right": "Ask if the statement forces it. Sensible is not enough."},
        {"wrong": "Reading 'only X can' as 'every X will'.", "right": "Only-X tells you who is out. It does not tell you who is in."},
        {"wrong": "Reading an average as a limit or as each value.", "right": "An average gives a total. It does not give the maximum or each value."},
        {"wrong": "Treating sales as profit.", "right": "Profit needs the cost. If the cost is not given, profit is unknown."},
        {"wrong": "Rejecting a soft word like 'some' or 'likely'.", "right": "Soft words are safe when the reading is fair."},
    ],
    revision=[
        "Only the statement is evidence. Real-life truth does not matter.",
        "Follows: restatement, arithmetic consequence, or a soft clear implication.",
        "Fails: a new extreme word, a general claim from one case, an outside cause, a future guess, or an average read as a limit.",
        "Only X can: it tells you who is out. Every X gets: a guarantee for each X.",
        "With numbers, do the sum. Revenue is not profit. An average is not each value.",
    ],
    patterns=[
        pat("sc-p1", "Extreme word, over-general claim or outside cause", "very common",
            "The conclusion has words like only, all, always or never. Or it gives a reason the statement did not give.",
            ["Underline the strong words in the conclusion.", "Check if the statement uses the same words.", "If the conclusion adds a new reason or a new extreme, it fails."],
            "A statement gives limited evidence. A new extreme or a new cause goes beyond it.",
            "Statement: Metro ridership rose after fares were cut last month. Conclusion: The fare cut is the only reason ridership rose.",
            ["The statement says ridership rose after the fare cut.", "'Only reason' is a new extreme claim.", "Other causes are not ruled out."],
            "Does not follow"),
        pat("sc-p2", "Data-based conclusion", "very common",
            "The statement has numbers, such as an average, a percentage or a total.",
            ["Do the sum the conclusion needs.", "Compare your result with the conclusion.", "An average gives a total but not each value."],
            "Numbers force some conclusions and leave others open.",
            "Statement: The average monthly salary of 5 employees is ₹30,000. Conclusions: I. The total salary is ₹1,50,000. II. Each employee earns ₹30,000.",
            ["Total = 5 × 30,000 = ₹1,50,000. So I follows.", "An average says nothing about each person. So II fails."],
            "Only I follows"),
        pat("sc-p3", "The only-rule applied to a person", "very common",
            "The statement says 'only those who...' and then names a person.",
            ["Write the gate: only X can get Y.", "Check if the person passes or fails the gate.", "A person who fails the gate is out. A person who passes is not sure to get Y."],
            "An only-rule fixes who is out, not who is in.",
            "Statement: Only students scoring at least 60% will be called for interview. Kiran scored 55%. Conclusion: Kiran will not be called.",
            ["The gate is a score of 60% or more.", "Kiran scored 55%, so she is below the gate.", "She is out."],
            "Follows"),
        pat("sc-p4", "Restatement and clear implication", "common",
            "The conclusion repeats part of the statement, or gives the plain meaning of it.",
            ["Read the statement once.", "Check if each conclusion says the same thing in other words.", "Mark the ones that add nothing new as following."],
            "A conclusion that adds nothing new cannot go beyond the statement.",
            "Statement: The school will stay closed tomorrow due to a heavy-rain warning from the weather department. Conclusions: I. Students need not come to school tomorrow. II. The weather department has warned of heavy rain.",
            ["I is the plain meaning of 'the school will stay closed'.", "II repeats a part of the statement."],
            "Both follow"),
        pat("sc-p13", "Percentage change and comparison", "common",
            "The statement gives an old value and a new value, and the conclusions give the rise or the percentage.",
            ["Find the change: new − old.", "Divide by the old value for the percentage.", "Compare with each conclusion."],
            "Percentage change always uses the old value as the base.",
            "Statement: The price of petrol rose from ₹80 to ₹92 in one year. Conclusions: I. The price rose by ₹12. II. The price rose by 15%. III. The price rose by 20%.",
            ["Rise = 92 − 80 = ₹12. So I follows.", "12 ÷ 80 = 15%. So II follows.", "III is wrong. 20% of 80 is ₹16, not ₹12."],
            "I and II follow"),
        pat("sc-p14", "A future guess", "common",
            "The conclusion says what 'will' happen later, but the statement is only about now.",
            ["Find the time in the statement.", "Find the time in the conclusion.", "If the conclusion looks ahead further than the statement, it fails."],
            "A statement about today does not force what happens later.",
            "Statement: The city announced a fare cut on the metro from next month. Conclusions: I. Metro fares will be lower from next month. II. The metro will cut fares again next year.",
            ["I repeats the announcement.", "II talks about next year, which the statement never mentions."],
            "Only I follows"),
        pat("sc-p15", "The every-rule and the wrong direction", "common",
            "The statement gives a guarantee: every X gets Y. The conclusion turns it round.",
            ["Write the rule as: X gives Y.", "A person with X gets Y. That follows.", "A person with Y must have X? That does not follow."],
            "A guarantee runs one way only. The reverse is a separate claim.",
            "Statement: Every employee with ten years of service gets an award. Arun has ten years of service. Conclusions: I. Arun gets an award. II. Every employee with an award has ten years of service.",
            ["Arun has ten years, so the rule gives him the award. I follows.", "The rule does not say others cannot get an award. II does not follow."],
            "Only I follows"),
        pat("sc-p16", "Soft words against hard words", "common",
            "One conclusion uses 'some' or 'likely' and another uses 'all' or 'every'.",
            ["Mark each conclusion soft or hard.", "A soft conclusion is a fair reading. It usually follows.", "A hard conclusion needs the statement to say it. Otherwise it fails."],
            "A statement rarely gives enough evidence for 'all' or 'always'.",
            "Statement: The bank offers 1% extra interest to senior citizens on fixed deposits. Conclusions: I. Some senior citizens are likely to prefer this bank. II. All senior citizens will move their deposits to this bank.",
            ["I says 'some' and 'likely'. It is a fair reading of the offer.", "II says 'all' and 'will'. The statement gives no such force."],
            "Only I follows"),
    ],
)

# ====================== checks: assumptions ======================
# Negation test is a logic model: statement makes sense only if assumption holds.
# model: "advice is useful" -> assumption ; if assumption is false, advice is pointless
N = ["assumption", "advice_useful"]
R = [lambda w: implies(w["advice_useful"], w["assumption"])]
assert follows(N, R + [lambda w: w["advice_useful"]], lambda w: w["assumption"])     # negation test
assert not follows(N, R, lambda w: w["assumption"])                                   # not forced without the advice being useful
# total effect is not required: statement needs "some reduction", not "complete stop"
N = ["reduces_some", "stops_all"]
R = [lambda w: implies(w["stops_all"], w["reduces_some"]), lambda w: w["reduces_some"]]
assert not follows(N, R, lambda w: w["stops_all"])
# assumption that makes the statement unnecessary: if all riders already wear helmets, poster pointless
N = ["all_already", "poster_needed"]
R = [lambda w: implies(w["all_already"], not w["poster_needed"]), lambda w: w["poster_needed"]]
assert follows(N, R, lambda w: not w["all_already"])
assert F(3, 4) > 0

ASSUMPTIONS = dict(
    concept=(
        "An assumption is an idea the speaker takes for granted before speaking. It is not written in the statement. "
        "Without it, the statement would make no sense. The negation test finds it."
    ),
    notes=r"""### What an assumption is
An **assumption** is an idea the speaker takes for granted before speaking. It is not written in the statement, but without it the statement makes no sense.

A mother says, "Take your umbrella, it will rain." She assumes you are going out, and that an umbrella will help. She never says so. She does not need to.

> **Watch:** A conclusion comes after a statement. It is what follows from it. An assumption comes before a statement. It is what the speaker already believes.

### The negation test
This one test solves almost every question.

1. Take the assumption and put **not** into it.
2. Read the statement again with the negated idea in mind.
3. If the statement becomes **pointless or self-defeating**, the assumption is **implicit**.
4. If the statement still makes sense, the assumption is **not** implicit.

> **Example:** Notice: "Use the stairs on Tuesday. The lift will be under repair." Assumption: the building has usable stairs. Negate it: "There are no usable stairs." Now the notice is absurd. So the assumption is implicit.

### Where assumptions come from
| Type of statement | What it usually assumes |
|---|---|
| Advice ("Do X") | X is possible for the listener, and X will help |
| Appeal or request | The listener can and may respond |
| Notice | Readers will read it and can follow it |
| Advertisement | Some buyers want what the advert offers |
| Decision or policy | The plan is possible and will do some good |

### Assumptions that are not implicit
- **Total effect.** "CCTV will completely stop signal jumping." The authority only needs to expect some improvement. A full result is never needed.
- **Comparison with rivals.** A purifier advert need not assume it is the cheapest or the best. It only assumes people want safe water.
- **Contradiction.** An assumption that clashes with the statement cannot be implicit.
- **Extreme words.** "Nobody can", "all people" and "only this method" are rarely needed.
- **Making the statement unnecessary.** If all riders already wear helmets, a helmet poster is pointless. So the poster cannot assume that.

### Worked examples
1. **Scheme:** free cycles for Class IX girls to improve attendance.
   - I. Some girls find it hard to reach school. Negate it: none find it hard. Then the scheme is pointless. It is **implicit**.
   - II. Every girl will now attend daily. This is a total effect. It is **not implicit**.
   - Answer: only I.
2. **Notice:** the railway will add two coaches to a train in the festival season.
   - I. More people are likely to travel then. Negate it: no more people. Then extra coaches are pointless. It is **implicit**.
   - II. The train can run with two extra coaches. Negate it: it cannot. Then the decision is impossible. It is **implicit**.
   - Answer: both.
""",
    formulas=[],
    tricks=[
        {"title": "The negation test",
         "body": "Put 'not' into the assumption. Does the speaker still have a reason to speak? If not, the assumption is implicit.",
         "example": ex("Notice: Use the stairs during the lift repair on Tuesday. Assumption: The building has stairs that residents can use. Is it implicit?",
                       ["Negate: the building has no usable stairs.", "Then the notice is absurd.", "So the assumption is implicit."], "Implicit")},
    ],
    mistakes=[
        {"wrong": "Confusing an assumption with a conclusion.", "right": "An assumption is what the speaker believes before speaking. A conclusion follows after."},
        {"wrong": "Accepting a total effect such as 'all accidents will stop'.", "right": "The speaker needs only some good effect. A total result is not implicit."},
        {"wrong": "Accepting a comparison with rivals in an advert.", "right": "An advert need not claim to be the best. It only needs some buyers."},
        {"wrong": "Accepting a strong assumption because it sounds true.", "right": "Use the negation test. If the statement still makes sense, it is not implicit."},
        {"wrong": "Accepting something that makes the statement pointless.", "right": "If the assumption would make the statement unnecessary, it is not implicit."},
    ],
    revision=[
        "An assumption is what the speaker believes before speaking.",
        "Negation test: negate it. If the statement collapses, it is implicit.",
        "Advice and decisions assume the action is possible and will do some good.",
        "Reject total effects, rival comparisons, contradictions and extreme words.",
        "An assumption that makes the statement unnecessary is not implicit.",
    ],
    patterns=[
        pat("sc-p5", "Advice or request: the negation test", "very common",
            "The statement is advice such as 'Do X' or a poster or a request.",
            ["Write the assumption in a plain sentence.", "Negate it.", "Read the statement again. If it becomes pointless, the assumption is implicit."],
            "Advice makes sense only if the action can help.",
            "Statement: 'Wear a helmet while riding,' says a traffic poster. Assumption: A helmet can reduce head injuries.",
            ["Negate: helmets do not reduce injuries.", "Then the poster is pointless."],
            "Implicit"),
        pat("sc-p6", "Advertisement or notice", "very common",
            "The statement is an advertisement, an announcement or a notice for a group of people.",
            ["Write each assumption.", "Negate each one.", "Keep only those whose negation makes the advert pointless.", "Reject extreme words like 'cannot' or 'nobody'."],
            "An advert needs some buyers. It does not need every buyer.",
            "Advertisement: 'Weekend yoga classes for busy office-goers.' Assumptions: I. Some office-goers are free on weekends. II. Office-goers cannot do yoga on weekdays.",
            ["Negate I: nobody is free on weekends. Then nobody could attend. So I is implicit.", "II says 'cannot'. The advert does not need it."],
            "Only I is implicit"),
        pat("sc-p7", "Total-effect or extreme assumption", "very common",
            "The assumption says 'completely', 'all', 'nobody' or 'only'.",
            ["Find the strong word.", "Ask: does the speaker need a full result, or only some?", "A decision needs only some good effect."],
            "A total effect is more than the statement needs.",
            "Statement: CCTV cameras will be installed at junctions to reduce signal jumping. Assumption: CCTV will completely stop signal jumping.",
            ["The aim is to reduce signal jumping.", "A full stop is not needed for the decision to make sense."],
            "Not implicit"),
        pat("sc-p8", "Decision or policy: possible and purposeful", "common",
            "The statement announces a decision, a plan or a scheme.",
            ["Ask what the plan needs: a reason and a way.", "Write each as an assumption.", "Negate each. If the plan becomes pointless or impossible, it is implicit."],
            "A plan needs a purpose and a way to carry it out.",
            "Statement: A company will open a branch in Pune to serve its growing customers there. Assumption: The company has customers in Pune.",
            ["Negate: the company has no customers in Pune.", "Then the branch has no purpose."],
            "Implicit"),
        pat("sc-p17", "Appeal or request", "common",
            "The statement asks people to do something, like 'Please do X'.",
            ["Ask: can the people do it?", "Ask: will it help?", "Do not assume that everyone will obey."],
            "A request assumes the listener can respond. It cannot assume every listener will.",
            "Statement: 'Please switch off the fans and lights when you leave the classroom,' says a school notice. Assumptions: I. Students can switch off the fans and lights. II. Every student will obey the notice.",
            ["Negate I: students cannot switch them off. Then the notice is pointless. So I is implicit.", "II is a total effect. So it is not implicit."],
            "Only I is implicit"),
        pat("sc-p18", "Comparison with rivals", "common",
            "An advert or claim praises one product, and an assumption says it is better than others.",
            ["Find the comparison, like 'better than' or 'the best'.", "Ask if the advert needs it.", "An advert only needs some people to want the product."],
            "An advert does not need to beat every rival to make sense.",
            "Advertisement: 'Use Sparkle toothpaste for stronger teeth.' Assumptions: I. Some people want stronger teeth. II. Sparkle is better than every other toothpaste.",
            ["Negate I: nobody wants stronger teeth. Then the advert is pointless. So I is implicit.", "II compares with all rivals. The advert does not need it."],
            "Only I is implicit"),
        pat("sc-p19", "An assumption that makes the statement unnecessary", "occasional",
            "An assumption says the problem is already solved, so the statement would not be needed.",
            ["Imagine the assumption is true.", "Ask if the statement is still needed.", "If it is not, the assumption is not implicit."],
            "A speaker who gives advice believes the advice is needed.",
            "Notice: 'Use the new app to book your ration slot.' Assumptions: I. Some card holders have phones and can use the app. II. All card holders already book slots by app.",
            ["Negate I: no card holder can use the app. Then the notice is pointless. So I is implicit.", "If II were true, the notice would be needless. So II is not implicit."],
            "Only I is implicit"),
    ],
)

# ====================== checks: courses of action ======================
assert 2 * 3 + 1 == 7
COURSES = dict(
    concept=(
        "The statement describes a problem. A course of action is a step to deal with it. "
        "A step follows if it is practical, proportionate and related to the problem, and the right authority can take it."
    ),
    notes=r"""### What a course of action is
The statement describes a **problem**. Each course of action is a proposed step. A step **follows** if a sensible authority would take it. It must be **practical**, **proportionate** and **related** to the problem. It should solve the problem, reduce the harm, or find the cause.

Think of yourself as a calm district officer. You do not panic. You do not punish everyone for one person's fault. You do not ignore the problem.

### The three filters
1. **Relevance.** Does the step touch the problem? Poor maths results: appoint a maths teacher. Widening the village road is unrelated.
2. **Practicality.** Can the right authority do it in reasonable time? Moving a whole city's people because of a water shortage cannot be done.
3. **Proportion.** Is the step the right size? A few students copying: act against them and tighten watch. Cancelling every result is too much.

### Steps that usually follow
- **Investigate:** an inquiry, a test, an inspection, tracing the people responsible.
- **Repair:** mend streetlights, correct display boards, improve drainage.
- **Relief:** rescue stranded families, send water tankers, keep hospital beds ready.
- **Warn and regulate:** give warnings, ration supply, control traffic until safety is checked.
- **Rule-based action** against those actually responsible.

### Steps that usually fail
- **Blanket bans.** Banning all private buses because one operator overcharged.
- **Permanent shutdowns** for a one-time or local problem.
- **Punishing everyone** for the fault of a few.
- **Unrelated steps** that deal with a different problem.
- **Impossible steps.** Stopping the monsoon, or never going out after dark.

### Short-term relief and long-term fix
A problem often needs both. Low areas are flooded. Send rescue teams now. Improve drainage for the future. Neither cancels the other.

> **Tip:** Do not reject a relief step because it is not permanent. Do not reject a long-term fix because it is not immediate.

### Investigate before punishing
If the cause is not known, an **inquiry** is the sensible first step. A bridge cracks after two years. Order an inquiry, then act against those found responsible. Punishing a named person without an inquiry is too early. Banning all bridges is too much.

### A worked example
**Statement:** The reservoir that supplies a city has fallen to a very low level after poor rainfall.

- I. Ration water and urge people to save it. It is practical and related, so it follows.
- II. Send tankers to areas with severe shortage. It is relief, so it follows.
- III. Shift the population to another city. It is absurd, so it does not follow.

Answer: only I and II.
""",
    formulas=[],
    tricks=[
        {"title": "The proportion check",
         "body": "Ask: would a sensible official do this tomorrow? Inspecting, repairing, warning, supplying and treating usually pass. Banning, shutting forever and blaming everyone usually fail.",
         "example": ex("Statement: A few buses on a city route broke down this week. Action: Scrap the entire bus fleet. Does it follow?",
                       ["A few breakdowns call for inspection and repair.", "Scrapping every bus is out of proportion."], "Does not follow")},
    ],
    mistakes=[
        {"wrong": "Picking a strong step because it sounds firm.", "right": "Pick the step that is practical and in proportion."},
        {"wrong": "Rejecting a relief step because it is not permanent.", "right": "Relief and a long-term fix can both follow."},
        {"wrong": "Accepting a step that punishes everyone.", "right": "Act against those responsible. Do not punish the innocent."},
        {"wrong": "Accepting a step unrelated to the problem.", "right": "Check that the step touches the stated problem."},
        {"wrong": "Punishing a person before an inquiry when the cause is unknown.", "right": "Order an inquiry first. Then act against those found responsible."},
    ],
    revision=[
        "A step follows if it is practical, in proportion and related to the problem.",
        "Good verbs: investigate, repair, relieve, regulate, warn, act as per rules.",
        "Poor verbs: ban all, shut forever, punish everyone, do something unrelated or impossible.",
        "Short-term relief and a long-term fix can both follow.",
        "Unknown cause: inquiry first, then action against those responsible.",
    ],
    patterns=[
        pat("sc-p9", "A practical fix against a blanket ban", "very common",
            "One step targets the cause. Another bans or removes something across the whole system.",
            ["Find the size of the problem.", "Match the size of each step to it.", "Reject a step that is far too big."],
            "A local problem needs a local step.",
            "Statement: Fake ₹500 notes are circulating in a district. Actions: I. Trace the gang printing them. II. Withdraw all ₹500 notes in the country.",
            ["I goes after the cause.", "II is a nationwide step for a district problem."],
            "Only I follows"),
        pat("sc-p10", "Short-term relief plus long-term fix", "very common",
            "The problem has an urgent side and a lasting side, and both are offered as steps.",
            ["Find the urgent need.", "Find the lasting cause.", "Accept a step for each if it is sensible."],
            "The two steps work on different parts of the problem.",
            "Statement: Low-lying areas are flooded and families are stranded. Actions: I. Send rescue teams. II. Improve drainage in these areas.",
            ["I helps stranded families now.", "II prevents a repeat later."],
            "Both follow"),
        pat("sc-p11", "An unrelated step", "very common",
            "One of the steps deals with something the statement does not mention.",
            ["Name the problem in one line.", "Ask if the step touches it.", "Reject steps that do not."],
            "A step must be linked to the stated problem.",
            "Statement: Passengers miss trains because display boards show wrong platforms. Actions: I. Check and correct the display system. II. Reduce ticket prices.",
            ["I fixes the display problem.", "II has no link to wrong platforms."],
            "Only I follows"),
        pat("sc-p12", "Punishing all against acting on those responsible", "common",
            "One step punishes a whole group. Another targets only those at fault.",
            ["Find who is at fault.", "Check if the step reaches only them.", "Reject a step that punishes the innocent."],
            "A fair step targets only those at fault.",
            "Statement: A few students were caught copying. Actions: I. Cancel the results of all students. II. Act against those caught and tighten invigilation.",
            ["I punishes students who did nothing wrong.", "II targets the guilty and stops repeats."],
            "Only II follows"),
        pat("sc-p20", "Inquiry before action when the cause is unknown", "common",
            "The statement gives a fault but not its cause, such as a collapse or a crack.",
            ["Check if the cause is stated.", "If it is not, an inquiry is sensible.", "Punish only after the inquiry."],
            "You cannot fairly blame anyone until you know the cause.",
            "Statement: A newly built bridge developed cracks within two years. Actions: I. Order an inquiry and act against those found responsible. II. Close all bridges in the state permanently.",
            ["I finds the cause and acts on it.", "II is far too big for one bridge."],
            "Only I follows"),
        pat("sc-p21", "Permanent shutdown for a local problem", "common",
            "A step shuts down a service or a business for good, and the problem is limited.",
            ["Ask if a smaller step would solve it.", "Prefer a limit or a fix.", "Reject the permanent shutdown."],
            "A fix or a limit solves the problem without destroying the service.",
            "Statement: Noise from a factory disturbs nearby residents at night. Actions: I. Ask the factory to fit noise barriers and limit night work. II. Shut the factory permanently.",
            ["I lowers the noise and keeps the factory open.", "II is out of proportion."],
            "Only I follows"),
        pat("sc-p22", "Awareness, repair and regulation together", "common",
            "The problem is a health or safety risk, and steps include warnings, repairs and controls.",
            ["Match each step to the risk.", "Accept sensible steps, even if more than one.", "Reject steps that limit people's lives without reason."],
            "Several steps can help, as long as each is practical and in proportion.",
            "Statement: Dengue cases have risen in a town after heavy rain. Actions: I. Start fogging and clear stagnant water. II. Run an awareness campaign about mosquito breeding. III. Stop people from leaving their homes for a month.",
            ["I removes the mosquitoes' breeding places.", "II teaches people how to help.", "III is out of proportion and cannot be done."],
            "Only I and II follow"),
    ],
)

# ---------------- apply ----------------
SUBS = {"conclusions": CONCLUSIONS, "assumptions": ASSUMPTIONS, "courses-of-action": COURSES}
dfrac = lambda x: x.replace(r"\frac", r"\dfrac")
data = json.loads(TOPIC.read_text(encoding="utf-8"))
all_ids = [p_["id"] for s in SUBS.values() for p_ in s["patterns"]]
assert len(all_ids) == len(set(all_ids)), "duplicate pattern id"
for sub in data["subtopics"]:
    new = SUBS.pop(sub["id"])
    old_ids = {p_["id"] for p_ in sub.get("patterns", [])}
    new_ids = {p_["id"] for p_ in new["patterns"]}
    assert old_ids <= new_ids, (sub["id"], old_ids - new_ids)
    notes = new["notes"].strip() + "\n"
    assert 2500 <= len(notes) <= 5000, (sub["id"], len(notes))
    sub["concept"] = new["concept"]
    sub["notes"] = notes
    sub["patterns"] = new["patterns"]
    sub["mistakes"] = [{k: dfrac(v) for k, v in m_.items()} for m_ in new["mistakes"]]
    sub["revision"] = [dfrac(r) for r in new["revision"]]
    sub["tricks"] = new["tricks"]
    sub["formulas"] = new["formulas"]
    print(f"{sub['id']}: {len(notes)} chars, {len(new['patterns'])} patterns (was {len(old_ids)})")
assert not SUBS, list(SUBS)
TOPIC.write_text(json.dumps(data, ensure_ascii=False, indent=1) + "\n", encoding="utf-8", newline="\n")
print("statement-conclusion updated")
