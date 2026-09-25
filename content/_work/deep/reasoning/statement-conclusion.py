# -*- coding: utf-8 -*-
"""Deep content for statement-conclusion.json. Idempotent: upserts by id."""
import sys, os
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
from _lib import *
from statement_conclusion_content import (NOTES_CONC, NOTES_ASSUM, NOTES_COA,
                                          P_CONC, P_ASSUM, P_COA, PYQS)

T = "statement-conclusion"
d = load(T)

OPT = {
    "conclusions": ["Only conclusion I follows", "Only conclusion II follows",
                    "Both I and II follow", "Neither I nor II follows"],
    "assumptions": ["Only assumption I is implicit", "Only assumption II is implicit",
                    "Both I and II are implicit", "Neither I nor II is implicit"],
    "courses-of-action": ["Only course of action I follows", "Only course of action II follows",
                          "Both I and II follow", "Neither I nor II follows"],
}
TRI = ["Only I and II follow", "Only I and III follow", "Only II and III follow",
       "All of I, II and III follow"]
LABEL = {"conclusions": "Conclusions", "assumptions": "Assumptions",
         "courses-of-action": "Courses of action"}
ASK = {"conclusions": "Which of the conclusions follow(s) from the statement?",
       "assumptions": "Which of the assumptions is/are implicit in the statement?",
       "courses-of-action": "Which of the courses of action follow(s)?"}
ROMAN = ["I", "II", "III"]


def sq(id, sub, pat, stmt, items, verdict, solution, shortcut, diff, t=50):
    """verdict = tuple of booleans, one per item. The option is derived from it."""
    assert len(items) == len(verdict)
    body = "\n".join(f"{ROMAN[i]}. {x}" for i, x in enumerate(items))
    q = f"**Statement:** {stmt}\n\n**{LABEL[sub]}:**\n{body}\n\n{ASK[sub]}"
    if len(items) == 2:
        o = OPT[sub]
        ans = {(True, False): o[0], (False, True): o[1],
               (True, True): o[2], (False, False): o[3]}[tuple(verdict)]
    else:
        keys = {(True, True, False): TRI[0], (True, False, True): TRI[1],
                (False, True, True): TRI[2], (True, True, True): TRI[3]}
        ans = keys[tuple(verdict)]
        o = TRI
    wrong = [x for x in o if x != ans]
    return Q(id, q, ans, wrong, solution, shortcut, diff, sub, pat, t)


C, A, K = "conclusions", "assumptions", "courses-of-action"
Y, N = True, False

# ---------- data checks (computed, not typed) ----------
jan, feb = 120, 150
rise = (feb - jan) * 100 / jan
assert rise == 25
w4_total, w5_total = 4 * 15, 5 * 16
fifth = w5_total - w4_total
assert fifth == 20
# a first-four set with a box heavier than the fifth: 25+15+10+10 = 60
assert 25 + 15 + 10 + 10 == w4_total and 25 > fifth
metro = 45 * 100 / 60
assert metro == 75

NEW = [
 # ---------------- conclusions ----------------
 sq("conclusions-p01", C, "sc-p1",
    "Ravi scored the highest marks in Class X of his school this year.",
    ["Ravi is the most intelligent student of the school.",
     "No other Class X student of his school scored more than Ravi this year."],
    (N, Y),
    "I turns one exam result into a claim about intelligence across the whole school — a new, wider claim, so it **does not follow**. II simply restates 'highest marks' — **follows**. Answer: **only II**.",
    "Marks in one exam ≠ 'most intelligent'. Restatement follows.", "easy", 40),
 sq("conclusions-p02", C, "sc-p1",
    "After a new bus route was started, the number of students reaching the village school late fell.",
    ["The new bus route is the only reason fewer students now come late.",
     "The bus route will be extended to other villages next year."],
    (N, N),
    "I adds the extreme word 'only'; other causes are not ruled out — **does not follow**. II predicts a future plan that the statement never mentions — **does not follow**. Answer: **neither**.",
    "'Only reason' and future plans are both outside the statement.", "medium"),
 sq("conclusions-p03", C, "sc-p2",
    "A shop sold 120 shirts in January and 150 shirts in February.",
    ["The number of shirts sold rose by 25% from January to February.",
     "The shop made more profit in February than in January."],
    (Y, N),
    f"I: rise = (150 − 120) ÷ 120 × 100 = {rise:g}% — **follows**. II: profit depends on prices and costs, which are not given; more pieces sold does not prove more profit — **does not follow**. Answer: **only I**.",
    "Percentage change is on the old value. Sales ≠ profit.", "medium"),
 sq("conclusions-p04", C, "sc-p2",
    "The average weight of 4 boxes is 15 kg. When a fifth box is added, the average of the 5 boxes becomes 16 kg.",
    ["The fifth box weighs 20 kg.",
     "The fifth box is heavier than each of the first four boxes."],
    (Y, N),
    f"I: total of 5 boxes = 5 × 16 = {w5_total} kg; total of 4 = 4 × 15 = {w4_total} kg; fifth = {fifth} kg — **follows**. II: the first four only average 15 kg; they could be 25, 15, 10 and 10 kg, and 25 kg is heavier than the fifth box — **does not follow**. Answer: **only I**.",
    "New item = new total − old total. An average never fixes the largest value.", "hard", 60),
 sq("conclusions-p05", C, "sc-p3",
    "Only residents of the housing society can use its swimming pool. Meena is not a resident of the society.",
    ["Meena cannot use the society's swimming pool.",
     "Every resident of the society uses the swimming pool."],
    (Y, N),
    "'Only residents' is a gate: anyone who is not a resident is out, so I **follows**. The gate says who *may* use the pool, not that every resident *does* — II **does not follow**. Answer: **only I**.",
    "'Only X' tells you who is out, never that every X does it.", "medium"),
 sq("conclusions-p06", C, "sc-p3",
    "Every customer who shops for more than ₹2,000 at a store gets a free cloth bag. Sunil got a free cloth bag from the store.",
    ["Sunil shopped for more than ₹2,000.",
     "A customer who shops for ₹2,500 at the store gets a free cloth bag."],
    (N, Y),
    "The rule says shopping above ₹2,000 is *enough* for a bag; it does not say it is the *only* way to get one, so from Sunil's bag we cannot work backwards — I **does not follow**. ₹2,500 is more than ₹2,000, so that customer is covered by 'every' — II **follows**. Answer: **only II**.",
    "'Every X gets Y' runs forward (X → Y), not backward (Y → X).", "hard", 60),
 sq("conclusions-p07", C, "sc-p4",
    "Water supply in Ward 5 will be stopped on Thursday from 9 a.m. to 1 p.m. for repair of the pipeline.",
    ["Residents of Ward 5 will not get piped water at 11 a.m. on Thursday.",
     "The pipeline serving Ward 5 needs repair."],
    (Y, Y),
    "11 a.m. lies inside the 9 a.m.–1 p.m. shutdown — I **follows**. The shutdown is 'for repair of the pipeline', so II restates the stated reason — **follows**. Answer: **both**.",
    "Restatements of the time window and the stated reason both follow.", "easy", 40),
 sq("conclusions-p08", C, "sc-p4",
    "From next month, the bank will stay open till 7 p.m. on weekdays instead of closing at 4 p.m.",
    ["The bank will stay open three hours longer on weekdays.",
     "The bank will also remain open on Sundays.",
     "Customers will be able to visit the bank at 6 p.m. on a weekday next month."],
    (Y, N, Y),
    "I: 4 p.m. to 7 p.m. is 3 hours — **follows**. II: only weekdays are mentioned — **does not follow**. III: 6 p.m. is within the new timing — **follows**. Answer: **only I and III**.",
    "Tick each conclusion separately, then match the pair.", "medium", 55),
 sq("conclusions-p09", C, "sc-p2",
    "Out of the 60 employees of an office, 45 travel to work by metro.",
    ["75% of the employees travel to work by metro.",
     "15 employees travel to work by car."],
    (Y, N),
    f"I: 45 ÷ 60 × 100 = {metro:g}% — **follows**. II: 15 employees do not use the metro, but they may walk, cycle or take a bus — 'by car' is not given — **does not follow**. Answer: **only I**.",
    "The remainder is 'not metro', not any particular mode.", "easy", 40),

 # ---------------- assumptions ----------------
 sq("assumptions-p01", A, "sc-p5",
    "'Drink only boiled water during the monsoon,' the doctor advised the villagers.",
    ["Boiling can make water safer to drink.",
     "The villagers are able to boil their drinking water."],
    (Y, Y),
    "Negate I: boiling does not make water safer — the advice becomes pointless, so I is **implicit**. Negate II: villagers cannot boil water — then the advice cannot be followed, so II is **implicit**. Answer: **both**.",
    "Advice assumes it helps AND that the listener can follow it.", "easy", 40),
 sq("assumptions-p02", A, "sc-p5",
    "A father told his daughter, 'Leave home by 8 a.m., or you will miss the 9 a.m. bus.'",
    ["The daughter needs to catch the 9 a.m. bus.",
     "The bus stop is exactly one hour away from home."],
    (Y, N),
    "Negate I: she does not need that bus — the warning is pointless, so I is **implicit**. II fixes the travel time at 'exactly' one hour; the father only needs the journey to take enough time that leaving later is risky — II is **not implicit**. Answer: **only I**.",
    "Words like 'exactly' make an assumption too precise to be needed.", "medium"),
 sq("assumptions-p03", A, "sc-p5",
    "'Book your train tickets at least a month in advance for Diwali travel,' a travel agent told his customers.",
    ["Tickets for Diwali travel may not be available closer to the date.",
     "Train fares are lower when tickets are booked a month in advance."],
    (Y, N),
    "Negate I: tickets will be easily available even later — booking early is pointless, so I is **implicit**. Negate II: fares are the same — the advice still makes sense because of availability, so II is **not implicit**. Answer: **only I**.",
    "If the advice survives the negation, the assumption is not needed.", "medium"),
 sq("assumptions-p04", A, "sc-p6",
    "Advertisement: 'Fresh vegetables delivered to your door within 30 minutes — order on our app!'",
    ["Some people want fresh vegetables delivered quickly.",
     "Some people are able to place orders through a mobile app."],
    (Y, Y),
    "Negate I: nobody wants quick delivery — the advert's hook is useless, so I is **implicit**. Negate II: nobody can order through an app — no one can respond, so II is **implicit**. Answer: **both**.",
    "An advert assumes its hook attracts someone and that someone can respond.", "easy", 40),
 sq("assumptions-p05", A, "sc-p6",
    "Notice in a housing society: 'The overhead water tank will be cleaned on Sunday from 10 a.m. to 2 p.m. Residents are requested to store water in advance.'",
    ["Residents will read the notice before Sunday.",
     "Cleaning the tank will take a whole week."],
    (Y, N),
    "Negate I: nobody reads it in time — the notice is useless, so I is **implicit**. II contradicts the notice, which gives a four-hour window — **not implicit**. Answer: **only I**.",
    "An assumption that contradicts the statement can never be implicit.", "medium"),
 sq("assumptions-p06", A, "sc-p6",
    "Advertisement: 'Our water purifier removes 99% of germs. Buy one for your family's health.'",
    ["All other water purifiers remove fewer germs than this one.",
     "Some buyers are concerned about germs in their drinking water."],
    (N, Y),
    "I compares the product with every rival; the advert makes no such claim and does not need it — **not implicit**. Negate II: no buyer cares about germs — the hook '99% of germs' is useless, so II is **implicit**. Answer: **only II**.",
    "Adverts assume buyer interest, not superiority over all rivals.", "medium"),
 sq("assumptions-p07", A, "sc-p7",
    "The municipal corporation has decided to plant 10,000 trees along city roads to reduce air pollution.",
    ["After the trees are planted, the city will become completely free of air pollution.",
     "Trees can help reduce air pollution to some extent."],
    (N, Y),
    "I expects a total result; the corporation only needs some reduction to make the plan worthwhile — **not implicit**. Negate II: trees do nothing for pollution — the decision is pointless, so II is **implicit**. Answer: **only II**.",
    "'Completely' = total effect = not implicit. 'To some extent' = implicit.", "medium"),
 sq("assumptions-p08", A, "sc-p7",
    "A school has started a daily 15-minute reading period to improve students' reading habits.",
    ["Every student will become a regular reader within a month.",
     "At present, some students do not have a good reading habit."],
    (N, Y),
    "I is a total, time-bound result that no school can assume — **not implicit**. Negate II: every student already reads well — there is nothing to improve and the new period loses its purpose, so II is **implicit**. Answer: **only II**.",
    "A step meant 'to improve' something assumes there is room to improve.", "hard", 55),
 sq("assumptions-p09", A, "sc-p8",
    "The railway has decided to run a special train between Delhi and Patna during the Chhath festival.",
    ["Many people will want to travel between Delhi and Patna during the festival.",
     "The railway has enough coaches and staff to run one more train."],
    (Y, Y),
    "Negate I: no extra travellers — the special train is pointless, so I is **implicit**. Negate II: the railway cannot run another train — the decision cannot be carried out, so II is **implicit**. Answer: **both**.",
    "A decision assumes a need (demand) and feasibility (resources).", "hard", 55),
 sq("assumptions-p10", A, "sc-p8",
    "A bank has decided to install ATMs in 50 villages of a district.",
    ["The bank will close all its branches in the district.",
     "People in these villages are likely to use the ATMs."],
    (N, Y),
    "I is an unrelated extra step; opening ATMs does not require closing branches — **not implicit**. Negate II: nobody will use the ATMs — the decision is pointless, so II is **implicit**. Answer: **only II**.",
    "Reject unrelated extra steps; keep the need behind the decision.", "medium"),
 sq("assumptions-p11", A, "sc-p7",
    "The government will give free cooking-gas connections to poor families to reduce smoke inside homes.",
    ["Some poor families use fuels that produce smoke while cooking.",
     "Every poor family will stop using firewood completely."],
    (Y, N),
    "Negate I: no poor family uses smoky fuel — the scheme has no purpose, so I is **implicit**. II expects a complete change by every family; some reduction is enough reason for the scheme — **not implicit**. Answer: **only I**.",
    "Total words — every, completely — mark the trap.", "easy", 40),

 # ---------------- courses of action ----------------
 sq("courses-of-action-p01", K, "sc-p9",
    "Many streetlights in a colony have not been working for two weeks, and residents feel unsafe at night.",
    ["The civic body should repair the streetlights at once.",
     "Residents should be banned from going out after dark."],
    (Y, N),
    "I fixes the actual problem — **follows**. II restricts everyone instead of fixing the lights — impractical and unfair, **does not follow**. Answer: **only I**.",
    "Fix the fault; do not ban the people.", "easy", 40),
 sq("courses-of-action-p02", K, "sc-p9",
    "A private bus operator was found charging passengers double the fixed fare on a route.",
    ["All private buses in the state should be banned.",
     "Action should be taken against the operator as per the rules."],
    (N, Y),
    "I punishes every operator in the state for one operator's fault — a blanket ban, **does not follow**. II targets the one who broke the rule — **follows**. Answer: **only II**.",
    "One offender → act on that offender, not the whole sector.", "medium"),
 sq("courses-of-action-p03", K, "sc-p9",
    "Cracks have appeared in a bridge that was built only two years ago.",
    ["Heavy vehicles should not be allowed on the bridge until engineers check it.",
     "An inquiry should be held into the construction and action taken against those found responsible.",
     "The state should stop building new bridges."],
    (Y, Y, N),
    "I is an immediate safety step — **follows**. II finds the cause and fixes responsibility — **follows**. III is a sweeping reaction to one bridge's defect — **does not follow**. Answer: **only I and II**.",
    "Safety now + inquiry follows; a blanket stop does not.", "hard", 60),
 sq("courses-of-action-p04", K, "sc-p10",
    "Dengue cases in the city have risen sharply this month.",
    ["The civic body should clear stagnant water where mosquitoes breed.",
     "Government hospitals should set up special fever counters."],
    (Y, Y),
    "I attacks the cause (breeding sites) — **follows**. II gives relief to those already ill — **follows**. Prevention and relief do not cancel each other. Answer: **both**.",
    "Prevention + relief can both follow.", "easy", 40),
 sq("courses-of-action-p05", K, "sc-p10",
    "Heavy rain has flooded the low-lying areas of a town and many families are stranded.",
    ["Rescue teams with boats should be sent to the flooded areas.",
     "Drainage in these areas should be improved before the next monsoon."],
    (Y, Y),
    "I is urgent relief for stranded families — **follows**. II prevents a repeat — **follows**. One is short-term, the other long-term; both are sensible. Answer: **both**.",
    "Do not reject relief for being temporary or a fix for being slow.", "medium"),
 sq("courses-of-action-p06", K, "sc-p10",
    "The reservoir that supplies water to a city has fallen to a very low level after poor rainfall.",
    ["Water should be rationed and residents urged to use it carefully.",
     "Tankers should be sent to areas facing an acute shortage.",
     "The city's population should be shifted to another city."],
    (Y, Y, N),
    "I stretches the available water — **follows**. II gives relief where it is worst — **follows**. III is absurd and impractical — **does not follow**. Answer: **only I and II**.",
    "Reject only the absurd option; relief steps can all follow.", "hard", 60),
 sq("courses-of-action-p07", K, "sc-p11",
    "Passengers are missing trains because the display boards at a station often show wrong platform numbers.",
    ["The display system should be checked and corrected.",
     "Ticket prices of all trains should be reduced."],
    (Y, N),
    "I fixes the exact cause of the problem — **follows**. II has nothing to do with wrong platform numbers — **does not follow**. Answer: **only I**.",
    "Name the problem; keep only actions that touch it.", "easy", 40),
 sq("courses-of-action-p08", K, "sc-p11",
    "For three years, the Class X mathematics results of a village school have been very poor.",
    ["The road to the village should be widened.",
     "A qualified mathematics teacher should be appointed and extra classes arranged."],
    (N, Y),
    "I may be useful in general but does not address poor maths results — **does not follow**. II directly targets the weak subject — **follows**. Answer: **only II**.",
    "A good-sounding action on a different problem does not follow.", "medium"),
 sq("courses-of-action-p09", K, "sc-p12",
    "A few students of a college were caught copying in the final examination.",
    ["The results of all students of the college should be cancelled.",
     "Action should be taken against those caught and invigilation should be made stricter."],
    (N, Y),
    "I punishes honest students for the fault of a few — **does not follow**. II acts on the wrongdoers and prevents a repeat — **follows**. Answer: **only II**.",
    "Act against the few who did wrong, not against everyone.", "medium"),
 sq("courses-of-action-p10", K, "sc-p12",
    "Some shopkeepers in a market were found selling adulterated milk.",
    ["Milk samples from shops in the market should be tested and those found guilty punished.",
     "All milk shops in the city should be closed permanently."],
    (Y, N),
    "I identifies and punishes the actual offenders — **follows**. II shuts every honest shop in the whole city for ever — disproportionate, **does not follow**. Answer: **only I**.",
    "Test, trace, punish the guilty — never shut everything.", "medium"),
 sq("courses-of-action-p11", K, "sc-p11",
    "Every summer, many people in a town fall ill due to heatstroke.",
    ["All offices in the town should be closed for the entire summer.",
     "A new cricket stadium should be built in the town."],
    (N, N),
    "I is impractical — a town cannot stop all work for months — **does not follow**. II is unrelated to heatstroke — **does not follow**. Useful steps would be awareness drives, drinking-water points or treatment facilities. Answer: **neither**.",
    "When both options are extreme or unrelated, 'neither' is the answer.", "medium"),
]

upsert(d["practice"], NEW)

set_sub(d, C, notes=NOTES_CONC, patterns=P_CONC)
set_sub(d, A, notes=NOTES_ASSUM, patterns=P_ASSUM)
set_sub(d, K, notes=NOTES_COA, patterns=P_COA)
d["pyqPatterns"] = PYQS

errs = finish(T, d)
assert not errs, errs
