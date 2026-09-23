# build statement-conclusion topic (topic 14)
# Verbal judgement items are verified by a tag engine: every conclusion / assumption /
# course of action carries an explicit reason tag, and the answer is DERIVED from the tags
# (never typed by hand). Data-based items compute their tags from arithmetic.
from fractions import Fraction as Fr
import common as C

FOLLOW = {'restate', 'definite', 'implied', 'implicit', 'practical'}
NOT = {'extreme', 'outside', 'contradict', 'overgeneral', 'not-needed', 'impractical', 'necessary-not-sufficient'}

OPT_C = ['Only conclusion I follows', 'Only conclusion II follows', 'Both I and II follow', 'Neither I nor II follows']
OPT_A = ['Only assumption I is implicit', 'Only assumption II is implicit', 'Both I and II are implicit',
         'Neither I nor II is implicit']
OPT_K = ['Only course of action I follows', 'Only course of action II follows', 'Both I and II follow',
         'Neither I nor II follows']
OPT_3 = ['Only I and II follow', 'Only I and III follow', 'Only II and III follow', 'All of I, II and III follow']


def ok(tag):
    assert tag in FOLLOW or tag in NOT, tag
    return tag in FOLLOW


def verdict2(opts, t1, t2):
    a, b = ok(t1), ok(t2)
    return opts[{(True, False): 0, (False, True): 1, (True, True): 2, (False, False): 3}[(a, b)]]


def verdict3(t1, t2, t3):
    f = tuple(ok(t) for t in (t1, t2, t3))
    m = {(True, True, False): 0, (True, False, True): 1, (False, True, True): 2, (True, True, True): 3}
    assert f in m, ('no option for', f)
    return OPT_3[m[f]]


def tag_of(truth):
    return 'definite' if truth else 'contradict'


def SC(id, stmt, items, tags, kind, sol, sc, d, sub, pat, t):
    """kind: C (conclusions), A (assumptions), K (courses of action), 3 (three conclusions)."""
    if kind == '3':
        opts, ans = OPT_3, verdict3(*tags)
        head = 'Conclusions'
    else:
        opts = {'C': OPT_C, 'A': OPT_A, 'K': OPT_K}[kind]
        ans = verdict2(opts, *tags)
        head = {'C': 'Conclusions', 'A': 'Assumptions', 'K': 'Courses of action'}[kind]
    ask = {'C': 'Which of the conclusions follow(s) from the statement?',
           'A': 'Which of the assumptions is/are implicit in the statement?',
           'K': 'Which of the courses of action logically follow(s)?',
           '3': 'Which of the conclusions follow from the statement?'}[kind]
    roman = ['I', 'II', 'III']
    body = '**Statement:** ' + stmt + '\n\n**' + head + ':**\n' + '\n'.join(
        roman[i] + '. ' + x for i, x in enumerate(items)) + '\n\n' + ask
    return C.Q(id, body, opts, ans, sol, sc=sc, d=d, sub=sub, pat=pat, t=t, fixed=True)


subs = []

subs.append(C.sub(
    'conclusions', 'Statement and conclusions',
    "A **conclusion** follows only if it is **definitely true on the basis of the statement alone** (plus universal common sense). You are not asked whether it is true in real life — only whether the statement forces it.\n\n"
    "A conclusion follows when it:\n- restates the statement in other words,\n- is a direct, necessary consequence (arithmetic from given data counts), or\n- is the obvious intended implication ('may', 'some', 'likely' conclusions often pass).\n\n"
    "A conclusion fails when it:\n- uses **extreme words** (only, all, always, never, best, must) the statement never used,\n- brings in **outside facts** or a cause/effect the statement does not mention,\n- **overgeneralises** one case to 'every time' or 'everyone',\n- confuses a **necessary** condition with a **sufficient** one ('only those with X are eligible' does not make everyone with X eligible).",
    tricks=[
        C.T(
            'Extreme-word filter',
            "Circle words like only, all, always, never, surely, best, entire, must. If the conclusion has one and the statement doesn't, it almost always fails.",
            "**Q.** Statement: Regular exercise helps control blood pressure. Conclusion: Exercise is the only way to control blood pressure.\n\n**Sol.** 'Only' is new — the statement says exercise *helps*, not that nothing else works. Does not follow.",
            "New extreme word = reject."),
        C.T(
            'Necessary vs sufficient',
            "'Only X can do Y' means X is required, not that X guarantees Y. Check which direction the conclusion runs.",
            "**Q.** Statement: Only graduates can apply for the post. Riya is a graduate. Conclusion: Riya will be selected.\n\n**Sol.** Being a graduate is necessary to apply, not sufficient for selection. Does not follow.",
            "'Only' fixes a gate, not a guarantee."),
    ],
    mistakes=[
        "Accepting a conclusion because it is true in real life, though the statement is silent.",
        "Reading 'only those with X' as 'everyone with X'.",
        "Rejecting soft conclusions ('may', 'some') that the statement clearly supports.",
        "Treating an average as a maximum or minimum in data statements.",
    ]))

subs.append(C.sub(
    'assumptions', 'Statement and assumptions',
    "An **assumption** is an unstated belief the speaker **must** hold for the statement (advice, appeal, notice, advertisement) to make sense. It is taken for granted *before* the statement is made.\n\n"
    "**Negation test**: negate the assumption. If the statement then becomes pointless or self-defeating, the assumption is implicit. Example: 'Book your tickets early to avoid the rush' assumes there will be a rush — negate it ('there will be no rush') and the advice is pointless.\n\n"
    "Assumptions are usually modest (some people, likely effect). A claimed assumption that the action will produce a **total** result (accidents will stop completely) is not needed and is not implicit.",
    tricks=[
        C.T(
            'Negation test',
            "Put 'not' in the assumption. Does the speaker still have a reason to say what they said? If not, the assumption is implicit.",
            "**Q.** Notice: 'Use the stairs during the lift maintenance on Tuesday.' Assumption: The building has stairs usable by residents.\n\n**Sol.** Negate: 'there are no usable stairs' — the notice becomes absurd. Implicit.",
            "If negation kills the statement's purpose, the assumption is implicit."),
    ],
    mistakes=[
        "Choosing assumptions that are desirable but not required.",
        "Accepting 100%-effect assumptions (will stop completely, everyone will obey).",
        "Confusing an assumption (before the statement) with a conclusion (after it).",
    ]))

subs.append(C.sub(
    'courses-of-action', 'Courses of action',
    "The statement describes a problem or situation; a **course of action** follows if it is a **practical, proportionate step** that addresses the problem (solves, reduces, or investigates it) and is within reach of the proper authority.\n\n"
    "Reject actions that are:\n- **extreme or disproportionate** (ban, shut down permanently, punish everyone),\n- **unrelated** to the stated problem, or\n- **impractical** (require the impossible, e.g. stop the monsoon).\n\n"
    "Two actions can both follow — a long-term fix (repair roads) and a short-term relief (deploy traffic police) are independent and often both valid.",
    tricks=[
        C.T(
            'Proportion check',
            "Ask: would a sensible administrator actually do this tomorrow? Investigating, repairing, warning, supplying, treating usually pass; banning, shutting forever, blaming everyone fail.",
            "**Q.** Statement: A few buses of a city route broke down this week. Action: Scrap the entire bus fleet.\n\n**Sol.** Disproportionate — a few breakdowns call for inspection and repair, not scrapping all buses. Does not follow.",
            "Fix the problem, don't nuke the system."),
    ],
    mistakes=[
        "Accepting harsh blanket bans as 'strong action'.",
        "Rejecting a valid short-term relief because it is not a permanent solution.",
        "Choosing actions that address a different problem than the one stated.",
    ]))

patterns = [
    C.P('Two conclusions (verbal)', 'very common',
        "A notice / news line / fact with two conclusions I and II.",
        "Filter extreme words and outside facts; keep restatements and clear implications."),
    C.P('Data-based statement', 'common',
        "Statement carries numbers (sales, prices, marks, speeds).",
        "Compute: percentages, differences, averages — then compare. Averages never fix maxima."),
    C.P('Only-X eligibility trap', 'common',
        "'Only those who…' plus an individual who meets the condition.",
        "Necessary is not sufficient: meeting the condition does not guarantee the outcome."),
    C.P('Three conclusions', 'occasional',
        "Three conclusions; options list pairs or all three.",
        "Judge each separately, then match the true set to an option."),
    C.P('Statement and assumption', 'common',
        "Advice, notice, advertisement or appeal; two assumptions.",
        "Negation test; reject total-effect assumptions."),
    C.P('Course of action', 'common',
        "A problem is described; two or three proposed actions.",
        "Keep practical, proportionate, relevant steps; reject bans and extremes."),
]

examples = []

# ex1
examples.append(SC(
    'rsn-statement-ex1',
    "The municipal corporation has announced a 5% rebate on property tax paid on or before 30 June.",
    ["Some property owners are likely to pay their tax on or before 30 June.",
     "A penalty will be charged on property tax paid after 30 June."],
    ('implied', 'outside'), 'C',
    "I: A rebate is offered precisely to encourage early payment; that some owners will respond is the clear implication — **follows**. II: The statement says nothing about a penalty; missing a rebate is not the same as paying a fine — outside information, **does not follow**. Answer: **Only I**.",
    "Rebate ≠ penalty: reject anything the statement never mentioned.",
    'easy', 'conclusions', 'two conclusions (verbal)', 45))

# ex2 data-based
sci, tot = 240, 400
com = tot - sci
t1 = tag_of(Fr(sci, tot) == Fr(60, 100))
t2 = tag_of(com > sci)
assert (t1, t2) == ('definite', 'contradict')
examples.append(SC(
    'rsn-statement-ex2',
    "In a school, 240 of the 400 students in Class XI chose the Science stream and all the others chose Commerce.",
    ["60% of the Class XI students chose Science.",
     "More Class XI students chose Commerce than Science."],
    (t1, t2), 'C',
    "I: 240 ÷ 400 = 0.6 = 60% — **follows**. II: Commerce = 400 − 240 = 160, which is less than 240 — the statement contradicts it, **does not follow**. Answer: **Only I**.",
    "Do the arithmetic; data conclusions are either forced or contradicted.",
    'easy', 'conclusions', 'data-based statement', 40))

# ex3 assumptions
examples.append(SC(
    'rsn-statement-ex3',
    "A mother tells her son, 'Carry your umbrella — the forecast says there will be heavy rain this evening.'",
    ["The weather forecast is generally reliable.",
     "The son will be outdoors this evening."],
    ('implicit', 'implicit'), 'A',
    "Negate I: 'the forecast is unreliable' — then advising an umbrella on its basis makes no sense, so I is **implicit**. Negate II: 'the son will stay indoors' — the umbrella advice becomes pointless, so II is **implicit**. Answer: **Both**.",
    "Negation test on each assumption.",
    'medium', 'assumptions', 'statement and assumption', 45))

# ex4 course of action
examples.append(SC(
    'rsn-statement-ex4',
    "Several students of a college hostel fell ill after eating dinner from the hostel mess.",
    ["The mess food and drinking water should be tested and the kitchen inspected.",
     "The hostel should be shut down permanently."],
    ('practical', 'extreme'), 'K',
    "I is a practical, proportionate step to find and remove the cause — **follows**. II is a drastic overreaction to a single incident and does not address the cause — **does not follow**. Answer: **Only I**.",
    "Investigate and fix = yes; shut down forever = no.",
    'easy', 'courses-of-action', 'course of action', 40))

# ---------------------------------------------------------------- practice
pr = []

pr.append(SC(
    'rsn-statement-1',
    "All candidates must carry an original photo identity card to the examination hall; candidates without one will not be allowed to enter.",
    ["A candidate without an original photo identity card will not be allowed into the hall.",
     "The photo identity card is the only document a candidate needs to carry."],
    ('restate', 'extreme'), 'C',
    "I simply restates the rule — **follows**. II adds 'only': the statement never says no other document (such as the admit card) is required — **does not follow**. Answer: **Only I**.",
    "Restatement passes; a new 'only' fails.",
    'easy', 'conclusions', 'two conclusions (verbal)', 35))

pr.append(SC(
    'rsn-statement-2',
    "Sales of mobile phones in the city rose sharply during the festival month of October this year.",
    ["Every year, people in the city buy more phones in festival months than in other months.",
     "Mobile phone prices were reduced in October."],
    ('overgeneral', 'outside'), 'C',
    "I stretches one year's data to 'every year' — overgeneralisation, **does not follow**. II supplies a cause (price cut) the statement never mentions — outside information, **does not follow**. Answer: **Neither**.",
    "One observation ≠ a rule; an unstated cause ≠ a conclusion.",
    'medium', 'conclusions', 'two conclusions (verbal)', 45))

dist, hrs = 360, Fr(9, 2)
t1 = tag_of(dist / hrs == 80)
assert t1 == 'definite'
pr.append(SC(
    'rsn-statement-3',
    "A train covered a distance of 360 km in 4 hours 30 minutes.",
    ["The average speed of the train was 80 km/h.",
     "The speed of the train never exceeded 80 km/h."],
    (t1, 'outside'), 'C',
    "I: 360 ÷ 4.5 = 80 km/h — **follows**. II: an average says nothing about the maximum; the train could have run faster on some stretches and slower on others — **does not follow**. Answer: **Only I**.",
    "Average speed fixes the average, never the top speed.",
    'medium', 'conclusions', 'data-based statement', 45))

pr.append(SC(
    'rsn-statement-4',
    "Only employees who have completed ten years of service are eligible for the long-service award. Rekha has completed twelve years of service.",
    ["Rekha is eligible for the long-service award.",
     "Rekha will receive the long-service award."],
    ('necessary-not-sufficient', 'necessary-not-sufficient'), 'C',
    "'Only those with ten years are eligible' makes ten years **necessary**, not **sufficient**: it tells us who is *excluded* (under ten years), not that everyone above ten years is eligible — there may be other conditions. So I does **not** definitely follow, and II (actually receiving it) is even further away. Answer: **Neither**.",
    "'Only X are eligible' → not-X are out; it never says X are in.",
    'hard', 'conclusions', 'only-x eligibility trap', 60))

pr.append(SC(
    'rsn-statement-5',
    "Every employee of the firm who works on a Sunday gets a compensatory day off. Arun, an employee of the firm, worked last Sunday.",
    ["Arun is entitled to a compensatory day off.",
     "Arun works on every Sunday."],
    ('definite', 'overgeneral'), 'C',
    "The rule is universal ('every employee who works on a Sunday'), and Arun satisfies it, so I **follows**. II turns one Sunday into every Sunday — **does not follow**. Answer: **Only I**.",
    "'Every X gets Y' + Arun is X → Arun gets Y. Contrast with the 'only' trap.",
    'medium', 'conclusions', 'only-x eligibility trap', 40))

nb = Fr(50 - 40, 40) * 100
pn = Fr(15 - 10, 10) * 100
assert nb == 25 and pn == 50
t1, t2 = tag_of(nb > pn), tag_of(pn == 50)
pr.append(SC(
    'rsn-statement-6',
    "The price of a notebook rose from ₹40 to ₹50, while the price of a pen rose from ₹10 to ₹15.",
    ["The price of the notebook rose by a larger percentage than the price of the pen.",
     "The price of the pen rose by 50%."],
    (t1, t2), 'C',
    "Notebook: (50 − 40)/40 = 25%. Pen: (15 − 10)/10 = 50%. I claims 25% > 50% — false, **does not follow** (a bigger rupee rise is not a bigger percentage rise). II is exactly 50% — **follows**. Answer: **Only II**.",
    "Compare percentages on the base, not the rupee jump.",
    'medium', 'conclusions', 'data-based statement', 50))

pr.append(SC(
    'rsn-statement-7',
    "Doctors advise that adults should sleep for at least seven hours a night to stay healthy.",
    ["Sleeping for more than seven hours a night is harmful for adults.",
     "Regularly sleeping for less than seven hours may affect an adult's health."],
    ('outside', 'implied'), 'C',
    "I invents a harm from sleeping more — the advice sets a minimum, not a maximum — **does not follow**. II is the direct implication of 'at least seven hours to stay healthy' and is suitably soft ('may') — **follows**. Answer: **Only II**.",
    "'At least' sets a floor; it says nothing about going above it.",
    'easy', 'conclusions', 'two conclusions (verbal)', 40))

pr.append(SC(
    'rsn-statement-8',
    "The city library will remain closed on all Sundays and on all public holidays.",
    ["The library will be closed on Republic Day, a public holiday.",
     "A reader who visits the library on a Sunday will find it closed."],
    ('definite', 'definite'), 'C',
    "I: Republic Day is a public holiday, and the library is closed on all public holidays — **follows**. II: it is closed on all Sundays — **follows**. Answer: **Both**.",
    "'All Sundays and all public holidays' covers both specific cases.",
    'easy', 'conclusions', 'two conclusions (verbal)', 35))

n, m, s = 50, 30, 35
both = m + s - n
only_s = s - both
assert both == 15 and only_s == 20
pr.append(SC(
    'rsn-statement-9',
    "In a class of 50 students, 30 passed in Mathematics and 35 passed in Science. Every student passed in at least one of the two subjects.",
    ["15 students passed in both subjects.",
     "20 students passed only in Science."],
    (tag_of(both == 15), tag_of(only_s == 20)), 'C',
    "Both = 30 + 35 − 50 = 15, so I **follows**. Only Science = 35 − 15 = 20, so II **follows**. Answer: **Both**.",
    "n(A∩B) = n(A) + n(B) − total when nobody fails both.",
    'medium', 'conclusions', 'data-based statement', 55))

pr.append(SC(
    'rsn-statement-10',
    "All the seats for the evening show of the play were sold out two days before the show.",
    ["There was high demand for tickets to the evening show.",
     "The morning show of the play was also sold out.",
     "At least some tickets for the evening show were sold before the day of the show."],
    ('implied', 'outside', 'definite'), '3',
    "I: selling out two days early clearly indicates high demand — **follows**. II: nothing is said about the morning show — **does not follow**. III: all seats were gone two days before, so tickets were certainly sold before the show day — **follows**. Answer: **Only I and III**.",
    "Judge each conclusion alone, then find the matching pair.",
    'medium', 'conclusions', 'three conclusions', 55))

pr.append(SC(
    'rsn-statement-11',
    "Advertisement: 'Learn to swim in just 15 days — join our summer swimming camp!'",
    ["Some people want to learn swimming in a short time.",
     "Nobody can learn swimming in less than 15 days."],
    ('implicit', 'not-needed'), 'A',
    "I: the '15 days' pitch only attracts customers if people value quick learning — negate it and the advert loses its point, so I is **implicit**. II: the camp need not believe faster learning is impossible; it only claims 15 days is enough — **not implicit**. Answer: **Only I**.",
    "An advert assumes its hook appeals to someone; it assumes nothing about rivals.",
    'medium', 'assumptions', 'statement and assumption', 45))

pr.append(SC(
    'rsn-statement-12',
    "The state transport department has decided to put up road-safety hoardings along the national highway.",
    ["Road accidents on the highway will stop completely once the hoardings are put up.",
     "At least some drivers will read the hoardings and may drive more carefully."],
    ('not-needed', 'implicit'), 'A',
    "I demands a 100% effect — the department only needs to expect *some* benefit, so I is **not implicit**. II: negate it ('no driver will read them') and the decision becomes pointless, so II is **implicit**. Answer: **Only II**.",
    "Reject total-effect assumptions; keep the modest one the plan depends on.",
    'medium', 'assumptions', 'statement and assumption', 45))

pr.append(SC(
    'rsn-statement-13',
    "The class teacher said, 'Please submit your filled forms by Friday so that I can send the list to the office on Monday.'",
    ["The students are in a position to submit the forms by Friday.",
     "The list to be sent to the office depends on the students' forms."],
    ('implicit', 'implicit'), 'A',
    "Negate I: 'students cannot submit by Friday' — the request is pointless, so I is **implicit**. Negate II: 'the list does not need the forms' — then linking the deadline to Monday's list makes no sense, so II is **implicit**. Answer: **Both**.",
    "Both halves of the teacher's sentence rest on one assumption each.",
    'medium', 'assumptions', 'statement and assumption', 45))

pr.append(SC(
    'rsn-statement-14',
    "After the monsoon, a large number of potholes have appeared on the city's main road, causing long traffic jams every day.",
    ["The municipal body should repair the potholes as early as possible.",
     "All vehicles should be banned from the main road until the next monsoon.",
     "Traffic police should be deployed on the road to manage the jams until the repairs are completed."],
    ('practical', 'extreme', 'practical'), '3',
    "I fixes the root cause — **follows**. II is a disproportionate ban that paralyses the city and does not repair anything — **does not follow**. III is a sensible short-term relief while repairs go on — **follows**. Answer: **Only I and III**.",
    "A permanent fix and a temporary relief can both be valid.",
    'medium', 'courses-of-action', 'course of action', 55))

pr.append(SC(
    'rsn-statement-15',
    "Farmers in a district report that a new type of pest has been damaging their standing crops.",
    ["The farmers should be told to stop cultivation in the district.",
     "Agricultural experts should be sent to identify the pest and advise the farmers on control measures."],
    ('extreme', 'practical'), 'K',
    "I is drastic and destroys the farmers' livelihood instead of tackling the pest — **does not follow**. II is a practical step that addresses the actual problem — **follows**. Answer: **Only II**.",
    "Tackle the pest, not the farming.",
    'easy', 'courses-of-action', 'course of action', 35))

assert len(pr) == 15

t = C.topic(
    'statement-conclusion', 'Statement & Conclusion', 'medium', {'tier1': '0-1', 'tier2': '1-2'},
    "Judge what a short statement definitely supports: conclusions (forced or clearly implied by the statement alone), assumptions (what the speaker must take for granted — use the negation test) and courses of action (practical, proportionate responses). The traps are predictable: extreme words, outside facts, overgeneralisation, averages read as limits, and 'only X are eligible' misread as a guarantee.",
    subs, patterns, examples, pr)

C.write_topic(t)
print('OK statement-conclusion')
