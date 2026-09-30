"""Readable rewrite of GA > Polity (all 8 subtopics).

Facts are kept exactly as in the existing lessons. Old pattern ids are kept; new ids continue each prefix.
Run: python polity.py  (patches content/core/topics/ga/polity.json in place)
"""
import json
import re
from pathlib import Path

ROOT = Path(__file__).resolve().parents[3]
TOPIC = ROOT / "core" / "topics" / "ga" / "polity.json"


def pat(pid, name, freq, spot, steps, why, q, ex_steps, answer):
    return {"id": pid, "name": name, "frequency": freq, "howToSpot": spot, "formula": None,
            "steps": steps, "why": why, "example": {"q": q, "steps": ex_steps, "answer": answer}}


def mis(wrong, right):
    return {"wrong": wrong, "right": right}


def trick(title, body, q=None, steps=None, answer=None):
    t = {"title": title, "body": body}
    if q:
        t["example"] = {"q": q, "steps": steps, "answer": answer}
    return t


SUBS = {}

# =====================================================================
# 1. Making of the Constitution
# =====================================================================
SUBS["pol-making"] = dict(
    concept=(
        "The Constituent Assembly wrote the Constitution. It was formed in 1946 under the **Cabinet Mission Plan**. "
        "Its members were elected indirectly by the provincial assemblies. "
        "The Constitution was adopted on **26 November 1949** and came into force on **26 January 1950**."
    ),
    notes=r"""### Who wrote the Constitution
The Constituent Assembly was formed in **1946** under the **Cabinet Mission Plan**. The provincial assemblies elected its members indirectly.

| Role | Person |
|---|---|
| Temporary chairman (first meeting) | Dr Sachchidananda Sinha |
| Permanent President (11 Dec 1946) | Dr Rajendra Prasad |
| Vice-President | H.C. Mukherjee |
| Constitutional Adviser | Sir B.N. Rau |
| Chairman, Drafting Committee | Dr B.R. Ambedkar |

> **Watch:** Ambedkar chaired only the Drafting Committee. The Assembly's President was Rajendra Prasad.

### Key dates in order
| Date | Event |
|---|---|
| 9 Dec 1946 | First meeting, in the Central Hall of Parliament |
| 13 Dec 1946 | Nehru moves the Objectives Resolution |
| 22 Jan 1947 | Objectives Resolution adopted. It became the seed of the Preamble |
| 29 Aug 1947 | Drafting Committee formed (7 members) |
| 4 Nov 1948 | Draft Constitution introduced |
| 26 Nov 1949 | Constitution adopted (Constitution Day) |
| 24 Jan 1950 | 284 members sign. 'Jana Gana Mana' adopted as anthem |
| 26 Jan 1950 | Constitution comes into force |

The date 26 January honours Purna Swaraj Day. The Congress had decided on complete independence at the Lahore session (Dec 1929).

### Numbers to remember
- Time taken: **2 years, 11 months, 18 days**, in **11 sessions**.
- Strength: **389** at first (292 provinces, 93 princely states, 4 chief commissioners' provinces). It fell to **299** after Partition.
- Signatures: **284** members signed.
- Cost: about **₹64 lakh**.
- Handwritten by Prem Behari Narain Raizada. The seal showed an **elephant**.
- The Assembly then served as the provisional Parliament until the first general election (1951-52).

### Committees and chairmen
| Chairman | Committees |
|---|---|
| Jawaharlal Nehru | Union Powers, Union Constitution, States |
| Sardar Patel | Provincial Constitution; Advisory Committee on Fundamental Rights and Minorities |
| Rajendra Prasad | Rules of Procedure, Steering, Flag |
| B.R. Ambedkar | Drafting |

> **Tip:** Nehru took the national committees, Patel the state and rights ones, and Prasad the procedure ones. Ambedkar held the drafting pen.

### Borrowed features
| Source | What India took |
|---|---|
| Government of India Act, 1935 | Federal scheme, Governors, judiciary, Public Service Commissions, emergency powers (the biggest source) |
| UK | Parliamentary system, rule of law, single citizenship, cabinet, bicameralism, writs |
| USA | Fundamental Rights, judicial review, independent judiciary, impeachment of the President |
| Ireland | Directive Principles, method of electing the President, 12 nominated Rajya Sabha members |
| Canada | Strong Centre, residuary powers with the Centre, Governors' appointment, advisory jurisdiction |
| Australia | Concurrent List, freedom of trade and commerce, joint sitting |
| USSR | Fundamental Duties, ideal of justice in the Preamble |
| France | Republic; liberty, equality, fraternity |
| Germany (Weimar) | Suspension of Fundamental Rights in an Emergency |
| South Africa | Amendment procedure, election of Rajya Sabha members |
| Japan | 'Procedure established by law' |

### Famous labels
- Part III of the Constitution is the **Magna Carta of India**.
- Article 32 is the **heart and soul** of the Constitution (Ambedkar's phrase).
- The 42nd Amendment is the **Mini-Constitution**.
- The CAG is the **guardian of the public purse**.

> **Rule:** The UK has no written constitution. So 'written constitution from Britain' is always a wrong option.
""",
    tricks=[
        trick("Committee to chairman",
              "Nehru took Union Powers, Union Constitution and States. Patel took Provinces and Rights. Prasad took Rules, Steering and Flag. Ambedkar took Drafting.",
              "Who chaired the Advisory Committee on Fundamental Rights and Minorities?",
              ["Rights belong to Patel's cluster.", "Patel also chaired the Provincial Constitution Committee."], "Sardar Patel"),
        trick("Borrowed features speed-pair",
              "UK: Parliament. USA: Rights. Ireland: DPSP. Canada: strong Centre. Australia: Concurrent List. USSR: Duties. France: Republic. Germany: Emergency. Japan: law procedure.",
              "Fundamental Duties are inspired by which constitution?",
              ["Duties bind citizens.", "The USSR constitution is the source. Ireland gave the DPSP."], "USSR (Russia)"),
    ],
    mistakes=[
        mis("Mixing up the adoption date (26 Nov 1949) and the enforcement date (26 Jan 1950).", "Adopted 1949, in force 1950."),
        mis("Saying Ambedkar presided over the Assembly.", "Rajendra Prasad presided. Ambedkar chaired only the Drafting Committee."),
        mis("Giving the joint sitting to Canada.", "The joint sitting came from Australia."),
        mis("Giving Fundamental Duties to Ireland.", "Duties came from the USSR. Ireland gave the Directive Principles."),
        mis("Forgetting that the Advisory Committee on Rights was Patel's.", "Patel chaired it, not Ambedkar."),
    ],
    revision=[
        "Cabinet Mission Plan 1946. Indirect election. 389 members, then 299 after Partition.",
        "First meeting 9 Dec 1946. Sinha was temporary chairman. Prasad was permanent President.",
        "Drafting Committee: 29 Aug 1947, 7 members, Ambedkar as chairman.",
        "Adopted 26 Nov 1949. In force 26 Jan 1950. Time taken: 2 years 11 months 18 days.",
        "Nehru: Objectives Resolution and Union committees. Patel: provinces and rights. Prasad: rules and flag.",
        "Biggest source: Government of India Act, 1935. Then UK, USA, Ireland, Canada, Australia.",
    ],
    patterns=[
        pat("ga-polmk-p1", "Assembly: people, dates and numbers", "very common",
            "The question asks who was temporary or permanent President, when the Assembly first met, how long it took, or how many signed.",
            ["Fix the four anchor dates: 9 Dec 1946, 26 Nov 1949, 24 Jan 1950, 26 Jan 1950.",
             "Match the person to the role: Sinha, Prasad, Mukherjee, Rau, Ambedkar.",
             "Recall the numbers: 389 then 299, 284 signatures, 11 sessions, ₹64 lakh."],
            "These facts are asked directly, so a short fact list settles the answer.",
            "The Constituent Assembly met for the first time on which date?",
            ["The first meeting was in the Central Hall of Parliament.", "Dr Sachchidananda Sinha was temporary chairman."],
            "9 December 1946"),
        pat("ga-polmk-p2", "Borrowed feature and source country", "very common",
            "A feature such as DPSP, joint sitting, Fundamental Duties, Concurrent List or writs is named. The source country is asked.",
            ["Recall the map: FRs and judicial review from the USA, DPSP from Ireland, Duties from the USSR.",
             "Recall the structure ones: strong Centre from Canada, Concurrent List and joint sitting from Australia.",
             "Then amendment procedure from South Africa, 'procedure established by law' from Japan, Emergency rights from Germany.",
             "Reject any option that gives a written constitution to the UK."],
            "Each feature has one source, so a single memory map answers every match question.",
            "The Concurrent List and the joint sitting of the two Houses were borrowed from which country?",
            ["Both belong to the Australian constitution.", "Joint sitting resolves a deadlock between the two Houses."],
            "Australia"),
        pat("ga-polmk-p3", "Committee and chairman pairing", "common",
            "The question names a committee and asks for its chairman, or gives a four-row match.",
            ["Sort committees into four groups: national, provincial and rights, procedure, drafting.",
             "Give the groups to Nehru, Patel, Prasad and Ambedkar.",
             "Watch for the two traps: the Advisory Committee is Patel's, and the Assembly's President is Prasad."],
            "The four chairmen split the committees in a clear pattern.",
            "Who chaired the Provincial Constitution Committee of the Constituent Assembly?",
            ["The provincial subjects sit in Patel's cluster.", "Nehru's cluster covers the Union and the States committee."],
            "Sardar Patel"),
        pat("ga-polmk-p4", "Government of India Act 1935 and famous labels", "common",
            "The question asks for the main source of the Constitution, or a nickname such as Mini-Constitution or heart and soul.",
            ["The largest single source is the Government of India Act, 1935.",
             "Recall the labels: 42nd Amendment is the Mini-Constitution, Part III is the Magna Carta, Article 32 is the heart and soul.",
             "The CAG is the guardian of the public purse."],
            "Labels are fixed phrases, so learn each with its owner.",
            "Which Article is called the 'heart and soul' of the Indian Constitution?",
            ["Ambedkar used this phrase.", "The article gives the right to constitutional remedies, which makes the other rights real."],
            "Article 32"),
        pat("ga-polmk-p5", "Objectives Resolution and the date ladder", "common",
            "The question asks who moved the Objectives Resolution, when it was adopted, or the order of events.",
            ["Place the events on one ladder: 9 Dec 1946, 13 Dec 1946, 22 Jan 1947, 29 Aug 1947, 4 Nov 1948, 26 Nov 1949, 26 Jan 1950.",
             "Nehru moved the Objectives Resolution. It became the seed of the Preamble.",
             "Read the question for 'moved' (13 Dec 1946) or 'adopted' (22 Jan 1947)."],
            "The same resolution has two dates, so the verb in the question decides.",
            "The Objectives Resolution was adopted by the Constituent Assembly on which date?",
            ["Nehru moved it on 13 Dec 1946.", "The Assembly adopted it later."],
            "22 January 1947"),
        pat("ga-polmk-p6", "Assembly strength and the Drafting Committee", "occasional",
            "The question asks how many members the Assembly had, how the 389 seats split, or how many served on the Drafting Committee.",
            ["Recall 389 at first and 299 after Partition.",
             "Split the 389 as 292 provinces, 93 princely states and 4 chief commissioners' provinces.",
             "Recall the Drafting Committee: formed 29 Aug 1947, 7 members, chairman Ambedkar."],
            "Numbers are easy to swap, so fix each with its source.",
            "How many members of the Constituent Assembly signed the Constitution on 24 January 1950?",
            ["The Assembly had 299 members after Partition.", "The signing count is a separate figure."],
            "284 members"),
    ],
)

# =====================================================================
# 2. Preamble, Parts and Schedules
# =====================================================================
SUBS["pol-preamble-parts"] = dict(
    concept=(
        "The Preamble is the opening statement of the Constitution. It calls India a **Sovereign, Socialist, Secular, Democratic Republic**. "
        "The **42nd Amendment (1976)** added the words socialist, secular and integrity. "
        "The Constitution has Parts, Articles and **12 Schedules**. Exams ask you to match each to its subject."
    ),
    notes=r"""### What the Preamble says
The Preamble opens with '**We, the people of India**'. So the Constitution draws its power from the people. It was framed from Nehru's Objectives Resolution (1946).

- India is a **Sovereign Socialist Secular Democratic Republic**.
- **Sovereign** means no outside power controls India.
- **Republic** means the head of state is elected, not hereditary.
- It records the adoption date, 26 November 1949.

| Ideal | What it covers |
|---|---|
| Justice | Social, economic, political |
| Liberty | Thought, expression, belief, faith, worship |
| Equality | Status and opportunity |
| Fraternity | Dignity, unity, integrity |

Justice comes from the Russian Revolution. Liberty, equality and fraternity come from the French Revolution.

### The Preamble in court
| Case | Ruling |
|---|---|
| Berubari Union (1960) | Preamble is not a part of the Constitution |
| Kesavananda Bharati (1973) | It is a part. It can be amended, but the basic structure stays |
| LIC of India (1995) | Confirmed that it is a part |

> **Rule:** The **42nd Amendment (1976)** added socialist, secular and integrity. It is the only change so far. The Preamble is non-justiciable.

### Parts and Articles
The original Constitution had 395 Articles, 22 Parts and 8 Schedules. Today it has about 470 Articles and 12 Schedules.

| Part | Subject | Articles |
|---|---|---|
| I | Union and its territory | 1-4 |
| II | Citizenship | 5-11 |
| III | Fundamental Rights | 12-35 |
| IV | Directive Principles | 36-51 |
| IV-A | Fundamental Duties | 51A |
| V | The Union | 52-151 |
| VI | The States | 152-237 |
| VIII | Union Territories | 239-242 |
| IX | Panchayats | 243-243O |
| IX-A | Municipalities | 243P-243ZG |
| XI | Centre-State relations | 245-263 |
| XV | Elections | 324-329A |
| XVII | Official language | 343-351 |
| XVIII | Emergency | 352-360 |
| XX | Amendment | 368 |

Part IX-B (cooperative societies) came with the 97th Amendment. Part VII was repealed by the 7th Amendment (1956). **Article 1** says: 'India, that is Bharat, shall be a Union of States'.

### The 12 Schedules
| No. | Content |
|---|---|
| 1 | States and Union Territories |
| 2 | Salaries of constitutional post-holders |
| 3 | Forms of oaths |
| 4 | Rajya Sabha seats |
| 5 | Scheduled Areas and Scheduled Tribes |
| 6 | Tribal areas of Assam, Meghalaya, Tripura, Mizoram |
| 7 | Union (100), State (61), Concurrent (52) Lists |
| 8 | 22 recognised languages |
| 9 | Land-reform laws (1st Amendment, 1951) |
| 10 | Anti-defection law (52nd Amendment, 1985) |
| 11 | 29 Panchayat subjects (73rd Amendment) |
| 12 | 18 Municipal subjects (74th Amendment) |

> **Tip:** Schedule 10 is for politicians (defection). Schedule 11 is for villages. Schedule 12 is for cities.

### Eighth Schedule languages
The Eighth Schedule now lists **22 languages**. Four amendments built the list.

- **Sindhi**: 21st Amendment (1967).
- **Konkani, Manipuri, Nepali**: 71st Amendment (1992).
- **Bodo, Dogri, Maithili, Santhali**: 92nd Amendment (2003).

### The Ninth Schedule shield
The Ninth Schedule protects land-reform and other laws from challenge. In the **I.R. Coelho case (2007)**, the Supreme Court said something new. Laws placed there after **24 April 1973** can still be reviewed if they destroy the basic structure.
""",
    tricks=[
        trick("Schedule story-line",
              "1 Names, 2 Salaries, 3 Oaths, 4 RS seats, 5 SC/ST areas, 6 Tribal north-east, 7 Three Lists, 8 Languages, 9 Land laws, 10 Defection, 11 Panchayat (29), 12 Municipality (18).",
              "Which Schedule contains the anti-defection provisions?",
              ["Defection is a matter for politicians.", "The 52nd Amendment (1985) added it."], "The 10th Schedule"),
        trick("Preamble keyword count",
              "Sovereign, Socialist, Secular, Democratic, Republic make five descriptors. Only Justice splits into three (social, economic, political).",
              "Which Preamble ideal has three parts?",
              ["Look at the ideal with three bracketed words.", "It traces to the Russian Revolution."], "Justice: social, economic and political"),
    ],
    mistakes=[
        mis("Saying the 44th Amendment changed the Preamble.", "It was the 42nd Amendment (1976)."),
        mis("Listing 18 languages in the Eighth Schedule.", "The count is 22 since the 92nd Amendment (2003)."),
        mis("Mixing the 9th Schedule (land laws) with the 10th (defection).", "Ninth is land laws. Tenth is defection."),
        mis("Saying the Preamble is not a part of the Constitution.", "That was Berubari (1960). Kesavananda (1973) overruled it."),
        mis("Mixing the 11th Schedule (29 subjects) with the 12th (18 subjects).", "Eleventh is panchayats (29). Twelfth is municipalities (18)."),
    ],
    revision=[
        "Preamble words in order: Sovereign, Socialist, Secular, Democratic, Republic.",
        "42nd Amendment (1976) added socialist, secular and integrity. It is the only change.",
        "Berubari (1960): not a part. Kesavananda (1973): a part, amendable within the basic structure.",
        "Part III: 12-35. Part IV: 36-51. Part IV-A: 51A. Part IX: 243-243O. Part IX-A: 243P-243ZG.",
        "Schedules: 4 is Rajya Sabha seats, 8 is 22 languages, 9 is land laws, 10 is defection.",
        "Article 1: India, that is Bharat, shall be a Union of States.",
    ],
    patterns=[
        pat("ga-polpre-p1", "Preamble keywords and the 42nd Amendment", "very common",
            "The question asks which words the 42nd Amendment added, the order of the adjectives, or what each ideal promises.",
            ["The added words are socialist, secular and integrity (42nd Amendment, 1976).",
             "Nothing else in the Preamble has changed.",
             "Recall the ideals with their brackets: justice (3), liberty (5 words), equality (2), fraternity (2)."],
            "The same trio of words is asked in many forms.",
            "The ideals of Liberty, Equality and Fraternity in the Preamble are inspired by which revolution?",
            ["France supplies these ideals and the word Republic.", "Justice comes from the Russian Revolution."],
            "The French Revolution"),
        pat("ga-polpre-p2", "Preamble in the courts", "common",
            "The question asks whether the Preamble is a part of the Constitution, or which case decided this.",
            ["Follow the chain: Berubari (1960), then Kesavananda Bharati (1973), then LIC of India (1995).",
             "Berubari said not a part. The next two said it is a part.",
             "Note the 42nd Amendment changed it once, which proves it can be amended."],
            "The three cases give one story, so the order gives the answer.",
            "In which case did the Supreme Court hold that the Preamble is a part of the Constitution?",
            ["Berubari (1960) said it is not a part.", "The 1973 case overruled it."],
            "Kesavananda Bharati (1973)"),
        pat("ga-polpre-p3", "Part and Article range matching", "very common",
            "The question asks which Articles hold a subject, or which Part deals with it.",
            ["Learn the five everyday ranges: 12-35, 36-51, 51A, 243-243O, 243P-243ZG.",
             "Add Emergency (352-360), Amendment (368), Elections (324-329), Services (308-323).",
             "Remember the odd facts: Part VII was repealed, and Tribunals sit in Part XIV-A."],
            "Ranges are fixed numbers, so one table answers every match question.",
            "Which Part of the Constitution deals with Municipalities?",
            ["Panchayats are in Part IX.", "Municipalities follow next, in Part IX-A."],
            "Part IX-A (Articles 243P to 243ZG)"),
        pat("ga-polpre-p4", "Schedule and content matching", "very common",
            "The question asks which Schedule holds a subject, such as defection, languages or panchayat subjects.",
            ["Use the anchors: 8 is languages, 9 is protected laws, 10 is defection.",
             "Then 11 is 29 panchayat subjects and 12 is 18 municipal subjects.",
             "Use the memory hook: 10 for politicians, 11 for villages, 12 for cities."],
            "Each Schedule number pairs with one subject.",
            "The Tenth Schedule of the Constitution deals with what?",
            ["It was added by the 52nd Amendment (1985).", "It decides when a legislator loses a seat for defection."],
            "Disqualification on the ground of defection"),
        pat("ga-polpre-p5", "Eighth Schedule languages", "common",
            "The question asks how many languages the Schedule has, or which amendment added a given language.",
            ["The current count is 22.",
             "Add the chain: Sindhi (21st), Konkani, Manipuri, Nepali (71st), Bodo, Dogri, Maithili, Santhali (92nd).",
             "Do not mix this list with the classical-language list."],
            "One amendment number goes with each group of languages.",
            "Which four languages did the 92nd Amendment (2003) add to the Eighth Schedule?",
            ["The 92nd Amendment took the total to 22.", "Recall the group of four added in 2003."],
            "Bodo, Dogri, Maithili and Santhali"),
        pat("ga-polpre-p6", "Seventh and Ninth Schedule details", "occasional",
            "The question asks how many items the Lists hold, or which case reviewed the Ninth Schedule.",
            ["Recall the Seventh Schedule: Union 100, State 61, Concurrent 52.",
             "The Ninth Schedule came with the 1st Amendment (1951).",
             "I.R. Coelho (2007) allows review of laws placed there after 24 April 1973."],
            "The Ninth Schedule shield has a date limit, and exams test that date.",
            "In which case did the Supreme Court hold that Ninth Schedule laws placed after 24 April 1973 can be reviewed?",
            ["24 April 1973 is the Kesavananda date.", "The case was decided in 2007."],
            "I.R. Coelho case (2007)"),
    ],
)

# =====================================================================
# 3. Fundamental Rights, DPSP, Duties
# =====================================================================
SUBS["pol-fundamental-rights"] = dict(
    concept=(
        "**Fundamental Rights** (Part III, Articles 12-35) protect you against the State. You can enforce them in court. "
        "**Directive Principles** (Part IV) are goals for the government, and no court enforces them. "
        "**Fundamental Duties** (Article 51A) are duties of citizens."
    ),
    notes=r"""### The six Fundamental Rights
Part III is the **Magna Carta of India**. It was borrowed chiefly from the USA. 'State' in Article 12 means the government and its agencies.

| Right | Articles |
|---|---|
| Equality | 14-18 |
| Freedom | 19-22 |
| Against exploitation | 23-24 |
| Freedom of religion | 25-28 |
| Cultural and educational | 29-30 |
| Constitutional remedies | 32 |

The Right to Property (Article 31) was deleted by the **44th Amendment (1978)**. It is now a legal right under **Article 300A**.

### Articles inside the rights
- **Article 14**: equality before law.
- **Article 15**: no discrimination.
- **Article 16**: equal opportunity in public jobs.
- **Article 17**: abolishes untouchability.
- **Article 18**: abolishes titles.
- **Article 19**: six freedoms. They are speech and expression, assembly, association, movement, residence and profession.
- **Article 21**: life and personal liberty.
- **Article 21A**: free, compulsory education for ages 6-14 (86th Amendment, 2002).
- **Article 23-24**: ban on trafficking and forced labour, and no child below 14 in factories.

The **103rd Amendment (2019)** added 10% EWS reservation in Articles 15(6) and 16(6).

> **Tip:** Count the blocks 14-18, 19-22, 23-24, 25-28, 29-30, 32. Articles 20 and 21 are never suspended in an Emergency.

### The five writs
Article 32 lets you go to the Supreme Court for a writ. Ambedkar called it the '**heart and soul**' of the Constitution. High Courts issue writs under **Article 226**, with a wider scope.

| Writ | Use |
|---|---|
| Habeas corpus | 'Produce the body'. Against illegal detention |
| Mandamus | 'We command'. Orders an official to do the duty |
| Prohibition | Stops a lower court from exceeding its power |
| Certiorari | Quashes an order passed without power |
| Quo warranto | 'By what authority'. Challenges illegal holding of office |

### Directive Principles
Part IV (Articles 36-51) came from **Ireland**. It is non-justiciable but 'fundamental in the governance of the country'.

| Group | Key articles |
|---|---|
| Gandhian | 40 village panchayats, 43 cottage industries, 43B cooperatives, 46 weaker sections, 47 nutrition, 48 agriculture |
| Socialist | 38, 39, 39A free legal aid, 41, 42, 43A workers' participation |
| Liberal-intellectual | 44 uniform civil code, 45, 48A environment, 49, 50, 51 |

The 42nd Amendment added 39A, 43A and 48A. The 86th Amendment rewrote Article 45 for early childhood care.

### Fundamental Duties
The **Swaran Singh Committee** recommended them. The **42nd Amendment (1976)** added ten duties in Article 51A. The **86th Amendment (2002)** added the eleventh. It asks parents to give education to children aged 6-14. The idea came from the **USSR** constitution.

### Cases that shaped the rights
| Case | Point |
|---|---|
| Champakam Dorairajan (1951) | Rights prevail over DPSP |
| Kesavananda Bharati (1973) | Basic structure doctrine |
| Maneka Gandhi (1978) | Any law limiting Article 21 must be fair, just and reasonable |
| Minerva Mills (1980) | The balance of Rights and DPSP is basic structure |
| Puttaswamy (2017) | Right to privacy is part of Article 21 |
""",
    tricks=[
        trick("FR article blocks",
              "14-18 Equality, 19-22 Freedom, 23-24 Exploitation, 25-28 Religion, 29-30 Culture and Education, 32 Remedies. The blocks hold 5, 4, 2, 4, 2 and 1 articles.",
              "Under which Article is untouchability abolished?",
              ["It is the first Article after equality before law and no discrimination.", "It sits in the Equality block, 14-18."], "Article 17"),
        trick("Duty amendment pair",
              "The 42nd Amendment gave ten duties. The 86th gave the eleventh and also inserted Article 21A.",
              "Which amendment added the eleventh Fundamental Duty?",
              ["The eleventh duty is about education of children aged 6-14.", "The same amendment inserted Article 21A."], "The 86th Amendment, 2002"),
    ],
    mistakes=[
        mis("Calling the Right to Property a Fundamental Right.", "It is Article 300A, a legal right, since the 44th Amendment (1978)."),
        mis("Thinking all rights are suspended in a national Emergency.", "Articles 20 and 21 are never suspended."),
        mis("Believing DPSP can be enforced in court.", "They are non-justiciable."),
        mis("Saying Article 32 is a legal right like Article 226.", "Article 32 is itself a Fundamental Right. Article 226 is wider."),
        mis("Confusing prohibition with certiorari.", "Prohibition stops a case midway. Certiorari quashes a finished order."),
        mis("Giving Fundamental Duties to Ireland.", "Duties came from the USSR. Ireland gave the DPSP."),
    ],
    revision=[
        "Six rights: Equality 14-18, Freedom 19-22, Exploitation 23-24, Religion 25-28, Culture 29-30, Remedies 32.",
        "Article 17 is untouchability. Article 21 is life and liberty. Article 21A is education for ages 6-14.",
        "Five writs: habeas corpus, mandamus, prohibition, certiorari, quo warranto.",
        "Article 32 is the Supreme Court. Article 226 is the High Court, with wider scope.",
        "DPSP came from Ireland. Article 44 is the uniform civil code.",
        "Duties: Swaran Singh Committee, 42nd Amendment gave 10, 86th Amendment gave the 11th.",
        "Minerva Mills (1980): the balance of Rights and DPSP is basic structure.",
    ],
    patterns=[
        pat("ga-polfr-p1", "Article and Fundamental Right mapping", "very common",
            "The question asks which Article gives a right, or gives a four-row Article and right match.",
            ["Learn the blocks: 14-18, 19-22, 23-24, 25-28, 29-30, 32.",
             "Remember that property is not a Fundamental Right. It is Article 300A.",
             "Recall the favourites: 17 untouchability, 21 life and liberty, 21A education, 32 writs."],
            "Each block belongs to one right, so the block gives the answer.",
            "The abolition of untouchability is guaranteed under which Article?",
            ["Untouchability is a form of inequality.", "It is the fourth Article of the equality block."],
            "Article 17"),
        pat("ga-polfr-p2", "Which writ for which situation", "very common",
            "A situation is described, such as illegal detention or an official who is not doing his duty. The writ is asked.",
            ["Illegal detention means habeas corpus.",
             "Duty not done means mandamus. Illegal office holder means quo warranto.",
             "Court orders: stopping a case midway is prohibition. Quashing a finished order is certiorari.",
             "Article 32 is the Supreme Court. Article 226 is the High Court."],
            "Each situation has exactly one writ.",
            "A person illegally detained by the police should move the court for which writ?",
            ["The person is being held without authority.", "The court will order the person to be produced."],
            "Habeas corpus"),
        pat("ga-polfr-p3", "DPSP classification and Article recall", "common",
            "The question asks which principle is Gandhian, or which Article gives the uniform civil code.",
            ["Gandhian: 40, 43, 43B, 46, 47, 48.",
             "Socialist: 38, 39, 39A, 41, 42, 43A. Liberal-intellectual: 44, 45, 48A, 49, 50, 51.",
             "Recall Article 44 as the uniform civil code.",
             "DPSP are non-justiciable, but 'fundamental in the governance of the country'."],
            "The three-way split sorts every DPSP article.",
            "Article 44 of the Constitution provides for what?",
            ["Article 44 is a liberal-intellectual directive.", "It concerns a common civil law for all citizens."],
            "A uniform civil code"),
        pat("ga-polfr-p4", "Fundamental Duties: count, source, amendments", "common",
            "The question asks how many duties there are, which committee recommended them, or which amendment added the eleventh.",
            ["The count is 11 today.",
             "The 42nd Amendment (1976) added 10. The 86th Amendment (2002) added the 11th.",
             "The source is the Swaran Singh Committee. The model is the USSR.",
             "The 11th duty is about educating children aged 6-14."],
            "The 10 plus 1 count and its two amendments are the whole question.",
            "The 11th Fundamental Duty asks parents and guardians to do what?",
            ["It was added by the 86th Amendment.", "It concerns children between 6 and 14 years."],
            "Provide opportunities for education to their child or ward aged 6 to 14"),
        pat("ga-polfr-p5", "Rights against DPSP and landmark cases", "occasional",
            "The question asks which case held the rights supreme, or which case made the rights-DPSP balance basic structure.",
            ["Champakam Dorairajan (1951): rights prevail over DPSP. This led to the 1st Amendment.",
             "Kesavananda Bharati (1973): basic structure. Minerva Mills (1980): the rights-DPSP balance is basic structure.",
             "Maneka Gandhi (1978): the procedure under Article 21 must be fair, just and reasonable."],
            "One case goes with each idea, so match the idea to the case.",
            "Which case held that the balance between Fundamental Rights and Directive Principles is part of the basic structure?",
            ["The case is from 1980.", "It struck down the 42nd Amendment's attempt to put DPSP above the rights."],
            "Minerva Mills (1980)"),
        pat("ga-polfr-p6", "Article 19 and Article 21 details", "common",
            "The question asks how many freedoms Article 19 has, or what Article 21 and 21A protect.",
            ["Article 19 has six freedoms: speech and expression, assembly, association, movement, residence, profession.",
             "The property freedom went out with the 44th Amendment.",
             "Article 21 is life and personal liberty. Maneka Gandhi (1978) and Puttaswamy (2017) shaped it.",
             "Article 21A is free, compulsory education for ages 6-14."],
            "These two Articles carry most of the case-law questions.",
            "The right to privacy was read into which Article in Puttaswamy (2017)?",
            ["Privacy connects to personal liberty.", "That is the Article on life and personal liberty."],
            "Article 21"),
    ],
)

# =====================================================================
# 4. Union and State Executive
# =====================================================================
SUBS["pol-executive"] = dict(
    concept=(
        "The **President** is head of the State, and the **Prime Minister** heads the government. "
        "The President is elected indirectly, and the Vice-President by both Houses of Parliament. "
        "The **Governor** is the President's counterpart in a state, with a narrower pardon power."
    ),
    notes=r"""### The President: Articles 52-62
| Item | Fact |
|---|---|
| Electors | Elected MPs, elected MLAs of the states, and elected MLAs of Delhi and Puducherry |
| Who does not vote | Nominated members and MLCs |
| Method | Proportional representation, single transferable vote, secret ballot |
| Vote value | Based on the 1971 census |
| Qualification | Citizen, 35 years, fit to be a Lok Sabha member |
| Term | 5 years |
| Oath | Given by the Chief Justice of India (Article 60) |
| Disputes | Decided by the Supreme Court (Article 71) |

**Impeachment (Article 61)** is for 'violation of the Constitution'. Either House can bring the charge. It needs two-thirds of the total membership, and the other House investigates. Notice is 14 days.

### Powers of the President
- **Ordinance (Article 123)**: only when Parliament is not in session. It lapses six weeks after Parliament reassembles.
- **Pardon (Article 72)**: covers death sentences, courts-martial and Union-law offences.

| Term | Meaning |
|---|---|
| Pardon | Full absolution |
| Commutation | Lighter kind of punishment |
| Remission | Smaller amount of punishment |
| Respite | Lesser sentence for a special reason |
| Reprieve | Temporary stay |

**Vetoes:** absolute (withhold assent), suspensive (return a bill once), and pocket (no action, no time limit). Zail Singh used a pocket veto on the Indian Post Office (Amendment) Bill, 1986. On state bills the President has an absolute veto (Article 201).

### The Vice-President: Articles 63-71
All members of both Houses elect the Vice-President, elected and nominated. State legislatures take no part.

- The Vice-President is ex-officio Chairman of the Rajya Sabha.
- He acts as President in a vacancy for at most 6 months.
- Removal starts only in the Rajya Sabha. It needs an effective majority and 14 days' notice. The Lok Sabha then agrees by simple majority.

### Prime Minister and Council of Ministers
- Article 74: the Council of Ministers aids and advises the President.
- Article 75(3): the Council is collectively responsible to the Lok Sabha.
- The **91st Amendment (2003)** caps the Council at 15% of the House, with a minimum of 12. The same cap applies in states.
- A minister who is not an MP must win a seat within 6 months.
- The Attorney-General (Article 76) can speak in Parliament but cannot vote.

### The Governor: Articles 153-161
The President appoints the Governor. The term is 5 years, but he holds office at the President's pleasure.

| Power | President | Governor |
|---|---|---|
| Pardon | Article 72 | Article 161 |
| Death sentence | Can pardon | Cannot pardon (can suspend, remit, commute) |
| Court-martial | Covered | Not covered |
| Ordinance | Article 123 | Article 213 |

The Governor can reserve state bills for the President (Articles 200-201).

### Current office-holders
As on 23 September 2026, **Droupadi Murmu** is the 15th President. She took office on 25 July 2022 and is the first tribal President. **C.P. Radhakrishnan** is the 15th Vice-President, since 12 September 2025.

> **Watch:** Office-holders change. Check the names again just before your exam.
""",
    tricks=[
        trick("Electoral college contrast",
              "The President is elected by elected MPs and elected MLAs. The Vice-President is elected by all MPs of both Houses, including the nominated ones.",
              "Do nominated Rajya Sabha members vote in the Vice-Presidential election?",
              ["The Vice-President's college is all members of both Houses.", "Nominated members are excluded only from the President's college."], "Yes, they vote"),
        trick("Pardon ladder",
              "The President's Article 72 covers court-martial and death sentences. The Governor's Article 161 covers neither.",
              "Can a Governor pardon a death sentence?",
              ["Article 161 is narrower than Article 72.", "A Governor can only suspend, remit or commute it."], "No. Only the President can pardon it"),
    ],
    mistakes=[
        mis("Saying the Vice-President gives the oath to the President.", "The Chief Justice of India gives the oath."),
        mis("Thinking the Vice-President's removal starts in the Lok Sabha.", "It starts only in the Rajya Sabha (Article 67(b))."),
        mis("Giving the 15% cap on ministers to the 52nd Amendment.", "The 15% cap is from the 91st Amendment. The 52nd is anti-defection."),
        mis("Letting nominated members vote for the President.", "Nominated members and MLCs do not vote for the President."),
        mis("Saying a Governor can pardon a death sentence.", "Only the President can. The Governor may suspend, remit or commute."),
    ],
    revision=[
        "President: elected MPs and elected MLAs (states, Delhi, Puducherry). PR by STV. 1971 census values.",
        "Impeachment: Article 61. Ground: violation of the Constitution. Either House can start.",
        "Vetoes: absolute, suspensive, pocket. The pocket veto was used in 1986.",
        "Ordinance: Article 123. It lapses six weeks after reassembly. Pardon: Article 72.",
        "Vice-President: elected by all members of both Houses, and removed only via the Rajya Sabha.",
        "Council of Ministers: at most 15% (minimum 12) by the 91st Amendment.",
        "Governor: the President's pleasure. No pardon of a death sentence (Article 161).",
    ],
    patterns=[
        pat("ga-polexe-p1", "President's election and impeachment", "very common",
            "The question asks who elects the President, which members do not vote, which census sets vote values, or how impeachment works.",
            ["Electors: elected MPs, elected MLAs of states, Delhi and Puducherry. Nominated members and MLCs stay out.",
             "The method is proportional representation by single transferable vote, with a secret ballot.",
             "Vote values use the 1971 census.",
             "Impeachment (Article 61): ground is violation of the Constitution, and either House can begin."],
            "One electoral college list answers most of the questions.",
            "The value of an MLA's vote in the Presidential election is calculated from which census?",
            ["The base was frozen for this purpose.", "The year is 1971."],
            "The 1971 census"),
        pat("ga-polexe-p2", "President's powers: veto, ordinance, pardon", "very common",
            "The question asks which bill saw a pocket veto, which Article gives ordinances, or what the President can pardon.",
            ["Vetoes: absolute (withhold), suspensive (return once), pocket (no time limit).",
             "Ordinances come from Article 123. They lapse six weeks after Parliament reassembles.",
             "Pardon is Article 72. It covers death sentences, courts-martial and Union-law offences.",
             "Learn the five shades: pardon, commutation, remission, respite, reprieve."],
            "Three powers are tested together in statement questions.",
            "The 'pocket veto' of the President means what?",
            ["The Constitution sets no time limit for assent.", "Zail Singh used it in 1986."],
            "Keeping a bill without acting on it"),
        pat("ga-polexe-p3", "Vice-President: election and removal", "common",
            "The question asks who elects the Vice-President, how he is removed, or who acts as President.",
            ["The electors are all members of both Houses, elected and nominated.",
             "The Vice-President is ex-officio Chairman of the Rajya Sabha.",
             "He can act as President for up to 6 months.",
             "Removal starts in the Rajya Sabha with 14 days' notice and an effective majority."],
            "The Vice-President's college differs from the President's, and that is what exams test.",
            "The Vice-President of India is elected by whom?",
            ["State legislatures take no part.", "Elected and nominated MPs both vote."],
            "All members of both Houses of Parliament"),
        pat("ga-polexe-p4", "PM and Council of Ministers", "common",
            "The question asks about collective responsibility, the 15% cap, a non-member minister's 6-month window, or the Attorney-General.",
            ["The Council is collectively responsible to the Lok Sabha (Article 75(3)).",
             "The 91st Amendment caps it at 15% of the House, minimum 12. States have the same cap.",
             "A minister who is not an MP must win a seat within 6 months.",
             "The Attorney-General (Article 76) can speak in Parliament but not vote."],
            "These four facts cover the statement questions on this topic.",
            "The 91st Amendment caps the Union Council of Ministers at what limit?",
            ["The cap is a share of a House.", "The floor is 12 ministers."],
            "15% of the strength of the Lok Sabha"),
        pat("ga-polexe-p5", "Governor: appointment, powers, pardon", "common",
            "The question asks who appoints the Governor, whether he can pardon a death sentence, or how state bills are reserved.",
            ["The President appoints the Governor. He holds office at the President's pleasure. Nominal term: 5 years.",
             "Under Article 161 he cannot pardon a death sentence.",
             "He can reserve state bills for the President (Articles 200-201). Ordinances are Article 213."],
            "The Governor's powers are a narrower copy of the President's.",
            "Which statement about the Governor's pardoning power is correct?",
            ["Article 161 applies to state-law offences.", "A death sentence pardon lies with the President."],
            "The Governor can suspend, remit or commute a death sentence but cannot pardon it"),
        pat("ga-polexe-p6", "Current office-holders", "occasional",
            "The question asks who is the current President or Vice-President, or which number they are.",
            ["Recall the President: Droupadi Murmu, 15th President, since 25 July 2022.",
             "She is the first tribal President.",
             "Recall the Vice-President: C.P. Radhakrishnan, 15th, since 12 September 2025."],
            "Current-affairs style questions use these names and numbers.",
            "Who is the 15th President of India, in office since 25 July 2022?",
            ["She is also the first tribal President.", "Her office began on 25 July 2022."],
            "Droupadi Murmu"),
    ],
)

# =====================================================================
# 5. Parliament and Judiciary
# =====================================================================
SUBS["pol-parliament-judiciary"] = dict(
    concept=(
        "**Parliament** is the President, the Rajya Sabha and the Lok Sabha. "
        "A **Money Bill** starts only in the Lok Sabha, and the Rajya Sabha has 14 days to return it. "
        "The **Supreme Court** has 34 judges, and its judges are picked through the collegium."
    ),
    notes=r"""### Parliament: Articles 79-122
| Item | Lok Sabha | Rajya Sabha |
|---|---|---|
| Ceiling | 552 (530 states, 20 UTs) | 250 (238 elected, 12 nominated) |
| Minimum age | 25 | 30 |
| Term | 5 years | 6 years, one-third retire every 2 years |
| Dissolved? | Yes | No, it is permanent |
| Presiding officer | Speaker | Chairman (Vice-President) |

The two nominated Anglo-Indian Lok Sabha seats ended with the **104th Amendment (2020)**. The 12 Rajya Sabha nominees are chosen for literature, science, art and social service. MLAs elect the Rajya Sabha members by single transferable vote.

- The gap between two sessions cannot exceed **6 months**.
- Quorum is **one-tenth** of the membership.
- The **Speaker** has a casting vote and certifies Money Bills. The Speaker also presides over joint sittings.

### Joint sitting and Money Bills
**Article 108** allows a joint sitting to break a deadlock on an ordinary bill. It never applies to Money Bills or Constitution Amendment Bills. Only **three** joint sittings have been held: Dowry Prohibition Bill (1961), Banking Service Commission (Repeal) Bill (1978) and POTA (2002).

A **Money Bill (Article 110)**:
1. Starts only in the Lok Sabha.
2. Needs the President's recommendation.
3. Goes to the Rajya Sabha, which returns it within **14 days** and can only recommend.
4. The Speaker's certificate is final.

### Motions and committees
A **no-confidence motion** is moved only in the Lok Sabha. It needs the support of 50 members. Cut motions are policy cut (Rs 1), economy cut (a stated sum) and token cut (Rs 100).

| Committee | Members | Note |
|---|---|---|
| Public Accounts | 22 (15 LS + 7 RS) | Chairman from the Opposition. Examines CAG reports |
| Estimates | 30, all from Lok Sabha | Chairman from the ruling side |
| Public Undertakings | 22 (15 LS + 7 RS) | |

### The Supreme Court: Articles 124-147
The sanctioned strength is **34 judges** including the CJI. The President appoints them on the **collegium's** advice (Second and Third Judges cases). The NJAC (99th Amendment, 2014) was struck down in 2015. Judges retire at **65**.

Removal needs 'proved misbehaviour or incapacity' and a special majority of both Houses. The Judges (Inquiry) Act, 1968 governs the process. It starts with 100 Lok Sabha or 50 Rajya Sabha members.

| Article | Jurisdiction |
|---|---|
| 131 | Original (Centre-state disputes) |
| 32 | Writs |
| 132-136 | Appellate. Article 136 is special leave to appeal |
| 137 | Review |
| 143 | Advisory (President's reference) |
| 141 | Law declared binds all courts |

The **basic structure** doctrine comes from Kesavananda Bharati (1973).

### High Courts and Lok Adalats
- There are **25 High Courts**. Calcutta, Bombay and Madras (1862) are the oldest.
- A High Court judge retires at **62**. The President appoints after consulting the CJI and the Governor.
- **Article 226** gives High Courts a writ power wider than Article 32. It covers legal rights too.
- **Lok Adalat** awards (Legal Services Authorities Act, 1987) are deemed civil-court decrees.

> **Note:** As on the source date, the Lok Sabha Speaker is **Om Birla** (18th Lok Sabha). The CJI is **Justice Surya Kant** (53rd CJI, since 24 November 2025).
""",
    tricks=[
        trick("Committee trio numbers",
              "PAC has 22, Public Undertakings has 22, Estimates has 30. Estimates is drawn only from the Lok Sabha.",
              "Which parliamentary committee examines the CAG's reports?",
              ["The CAG audits accounts.", "The Public Accounts Committee reads the audit reports."], "The Public Accounts Committee"),
        trick("Writ first letters",
              "H-M-P-C-Q stands for Habeas, Mandamus, Prohibition, Certiorari, Quo warranto. Prohibition stops a case early. Certiorari quashes after.",
              "Which writ stops a lower court from exceeding its jurisdiction before it decides?",
              ["The word 'before' points to prohibition.", "Certiorari works after the order is passed."], "Prohibition"),
    ],
    mistakes=[
        mis("Thinking a joint sitting can pass a Constitution Amendment Bill.", "Article 108 excludes Money Bills and Constitution Amendment Bills."),
        mis("Thinking the Rajya Sabha can be dissolved.", "It is permanent. One-third retire every two years."),
        mis("Saying the sanctioned strength of the Supreme Court is 31.", "It is 34, including the CJI."),
        mis("Thinking the Rajya Sabha can reject a Money Bill.", "It can only recommend. It has 14 days to return the bill."),
        mis("Mixing the retirement ages.", "Supreme Court judges retire at 65. High Court judges retire at 62."),
    ],
    revision=[
        "Lok Sabha: age 25, term 5 years. Rajya Sabha: max 250, age 30, permanent, 6-year terms.",
        "Gap between sessions: at most 6 months. Quorum: one-tenth.",
        "Money Bill: Lok Sabha only, President's recommendation, 14 days for the Rajya Sabha, Speaker certifies.",
        "Three joint sittings so far. Never for Money Bills or Constitution Amendment Bills.",
        "PAC: 22, Opposition chairman. Estimates: 30, all Lok Sabha.",
        "Supreme Court: 34 judges, retirement 65, collegium. High Court: retirement 62.",
        "Jurisdictions: 131 original, 136 special leave, 137 review, 141 binding law, 143 advisory.",
    ],
    patterns=[
        pat("ga-polvj-p1", "Money Bill and bill procedures", "very common",
            "The question asks where a Money Bill can start, how long the Rajya Sabha has, or whose certificate decides.",
            ["A Money Bill (Article 110) starts only in the Lok Sabha, on the President's recommendation.",
             "The Rajya Sabha has 14 days and can only recommend.",
             "The Speaker's certificate is final.",
             "A joint sitting never applies to Money Bills."],
            "The Money Bill route is fixed, and each step is asked separately.",
            "The Rajya Sabha must return a Money Bill to the Lok Sabha within how many days?",
            ["It can only make recommendations.", "The Lok Sabha may accept or reject them."],
            "14 days"),
        pat("ga-polvj-p2", "Motions and financial committees", "common",
            "The question asks how many members support a no-confidence motion, or which committee has only Lok Sabha members.",
            ["A no-confidence motion is moved only in the Lok Sabha, with 50 members' support.",
             "Estimates has 30, all Lok Sabha. PAC and Public Undertakings have 22 each (15 + 7).",
             "The PAC chairman is from the Opposition by convention.",
             "Cut motions: policy Rs 1, economy a stated sum, token Rs 100."],
            "Small numbers on committees are asked in statement form.",
            "The Estimates Committee of Parliament consists of how many members?",
            ["It is drawn only from one House.", "That House is the Lok Sabha."],
            "30 members, all from the Lok Sabha"),
        pat("ga-polvj-p3", "Parliament's structure: numbers, ages, sessions", "very common",
            "The question asks the maximum strength of the Rajya Sabha, the minimum age, the nominated members or the gap between sessions.",
            ["Recall the numbers: Lok Sabha 552, Rajya Sabha 250 (238 elected + 12 nominated).",
             "Recall the ages: 25 for the Lok Sabha and 30 for the Rajya Sabha.",
             "Recall the terms: Lok Sabha 5 years, Rajya Sabha 6 years with one-third retiring every 2 years.",
             "The gap between sessions is at most 6 months. Quorum is one-tenth."],
            "Structural numbers are asked directly.",
            "The Rajya Sabha can have at most how many members?",
            ["Some are elected and some are nominated.", "Add 238 and 12."],
            "250"),
        pat("ga-polvj-p4", "Supreme Court: appointment, removal, jurisdiction", "very common",
            "The question asks how judges are appointed, why they can be removed, or which Article gives advisory jurisdiction.",
            ["The strength is 34. The President appoints on the collegium's advice. The NJAC was struck down in 2015.",
             "Removal: proved misbehaviour or incapacity, special majority of both Houses, Judges (Inquiry) Act, 1968.",
             "Anchor the Articles: 131 original, 136 special leave, 137 review, 141 binding, 143 advisory.",
             "Judges retire at 65."],
            "Each jurisdiction has its own Article number.",
            "Under which jurisdiction does the Supreme Court answer questions of law referred by the President?",
            ["The President makes a reference.", "The court gives an opinion, not a judgment."],
            "Advisory jurisdiction (Article 143)"),
        pat("ga-polvj-p5", "High Courts and Lok Adalats", "occasional",
            "The question asks the retirement age of a High Court judge, who appoints, or what a Lok Adalat award is.",
            ["High Court judges retire at 62. The President appoints after consulting the CJI and the Governor.",
             "Article 226 is wider than Article 32.",
             "A Lok Adalat award is deemed a civil-court decree, and no appeal lies on merits."],
            "These small facts fill out the statement questions.",
            "Every Lok Adalat award is deemed to be what?",
            ["Lok Adalats are set up under the 1987 Act.", "The award is binding on the parties."],
            "A decree of a civil court"),
        pat("ga-polvj-p6", "Joint sittings held so far", "occasional",
            "The question asks how many joint sittings have been held, or which bills they were on.",
            ["Article 108 provides for a joint sitting.",
             "Three have been held: Dowry Prohibition Bill (1961), Banking Service Commission (Repeal) Bill (1978), POTA (2002).",
             "It is never used for Money Bills or Constitution Amendment Bills."],
            "The three bills are a stock question.",
            "Which 2002 measure was passed at a joint sitting of Parliament?",
            ["It was an anti-terror law.", "Its short name is POTA."],
            "POTA (Prevention of Terrorism Bill)"),
    ],
)

# =====================================================================
# 6. Amendments
# =====================================================================
SUBS["pol-amendments"] = dict(
    concept=(
        "**Article 368** (Part XX) is the rule for amending the Constitution. "
        "Most amendments need a special majority. Federal items also need half the state legislatures. "
        "The basic structure doctrine of **Kesavananda Bharati (1973)** limits the power."
    ),
    notes=r"""### Three routes to amend
The amendment power sits in **Article 368**, borrowed from South Africa.

| Route | Used for |
|---|---|
| Simple majority (outside Article 368) | New states, state boundaries, citizenship rules, salaries of constitutional post-holders, Second, Fifth and Sixth Schedules |
| Special majority | Most amendments, including Fundamental Rights |
| Special majority plus half the state legislatures | Federal items |

A **special majority** means a majority of the total membership of each House plus two-thirds of members present and voting.

Federal items are the election of the President (Articles 54-55), executive power of Union and states, the Supreme Court and High Courts, the Seventh Schedule, states' representation in Parliament and Article 368 itself.

> **Rule:** A Constitution Amendment Bill never goes to a joint sitting. The President must give assent (24th Amendment).

### Early landmarks
| Amendment | What it did |
|---|---|
| 1st (1951) | Ninth Schedule, Articles 31A and 31B, reasonable restrictions |
| 7th (1956) | States reorganisation, ended A/B/C/D classes, repealed Part VII |
| 24th (1971) | Parliament can amend any part, including Fundamental Rights |
| 42nd (1976) | Mini-Constitution: socialist, secular, integrity, Fundamental Duties, LS term to 6 years |
| 44th (1978) | Property out of Part III (Article 300A), 'armed rebellion' replaces 'internal disturbance', LS term back to 5 years |

> **Tip:** The 44th corrected what the 42nd overdid.

### Amendments from 1985 to 2003
| Amendment | What it did |
|---|---|
| 52nd (1985) | Anti-defection law, Tenth Schedule |
| 61st (1988; in force 1989) | Voting age 21 to 18 (Article 326) |
| 65th (1990) | National Commission for SC/ST (Article 338) |
| 69th (1991) | Delhi as National Capital Territory |
| 71st (1992) | Konkani, Manipuri, Nepali added to Eighth Schedule |
| 73rd and 74th (1992) | Panchayats and Municipalities |
| 86th (2002) | Article 21A, Article 45 rewritten, 11th duty |
| 89th (2003) | Separate commission for ST (Article 338A) |
| 91st (2003) | Council of Ministers capped at 15% (minimum 12) |
| 92nd (2003) | Bodo, Dogri, Maithili, Santhali added (22 languages) |

### Amendments from 2011 to 2023
| Amendment | What it did |
|---|---|
| 97th (2011) | Cooperative societies, Part IX-B |
| 99th (2014) | NJAC, struck down in 2015 |
| 100th (2015) | India-Bangladesh Land Boundary Agreement |
| 101st (2016) | GST: Articles 246A, 269A, 279A (GST Council) |
| 102nd (2018) | Constitutional status for the Backward Classes Commission (Article 338B) |
| 103rd (2019) | 10% EWS reservation (Articles 15(6), 16(6)) |
| 104th (2020) | Ended Anglo-Indian nominations. Extended SC/ST seats in legislatures |
| 105th (2021) | States can identify OBCs again (Article 342A) |
| 106th (2023) | One-third of seats for women in Lok Sabha, state assemblies and Delhi assembly |

The 106th takes effect after delimitation, and lasts 15 years. **106 amendments** had been enacted by September 2023.

### Decade clusters
- 1950s: structure (1st, 7th).
- 1970s: power (24th, 42nd, 44th).
- 1980s: politics (52nd, 61st).
- 1990s: grass roots (73rd, 74th) and languages (71st, 92nd).
- 2000s: rights and cooperatives (86th, 91st, 97th).
- 2010s and 2020s: economy and equality (101st to 106th).
""",
    tricks=[
        trick("Decade clusters",
              "1950s structural (1st, 7th). 1970s power (24, 42, 44). 1980s politics (52, 61). 1990s grass roots (73, 74). 2010s and 2020s economy and equality (101 GST, 103 EWS, 106 women).",
              "Which amendment lowered the voting age from 21 to 18?",
              ["It is a 1980s political change.", "It amended Article 326."], "The 61st Amendment"),
        trick("42 versus 44",
              "The 44th undid parts of the 42nd. Lok Sabha term went from 6 back to 5 years. 'Internal disturbance' became 'armed rebellion'. Property moved from a right to Article 300A.",
              "Which amendment replaced 'internal disturbance' with 'armed rebellion' in Article 352?",
              ["It restrained the Emergency power.", "It also deleted the Right to Property."], "The 44th Amendment, 1978"),
    ],
    mistakes=[
        mis("Giving the 10% EWS reservation to the 102nd Amendment.", "EWS is the 103rd. The 102nd gave constitutional status to the Backward Classes Commission."),
        mis("Thinking the 106th (women's seats) applies at once.", "It takes effect after delimitation."),
        mis("Thinking the NJAC still works.", "The 99th Amendment was struck down in 2015."),
        mis("Saying ratification by states is needed for every amendment.", "It is needed only for federal items."),
        mis("Sending an amendment bill to a joint sitting.", "Article 108 excludes Constitution Amendment Bills."),
    ],
    revision=[
        "Three routes: simple majority (outside 368), special majority, special majority plus half the states.",
        "Ratification list: President's election, Supreme Court and High Courts, Seventh Schedule, state representation, Article 368.",
        "42nd is the Mini-Constitution. 44th removed property and added 'armed rebellion'.",
        "52nd: defection. 61st: voting age 18. 73rd and 74th: Panchayats and Municipalities.",
        "86th: Article 21A and the 11th duty. 101st: GST. 103rd: EWS 10%. 106th: women's one-third.",
        "No joint sitting for an amendment bill. The President must give assent.",
    ],
    patterns=[
        pat("ga-polam-p1", "Amendment procedure and state ratification", "very common",
            "The question asks which provisions need half the states, or what majority amends Fundamental Rights.",
            ["A special majority is a majority of total membership plus two-thirds of those present and voting.",
             "Fundamental Rights are amended by this route.",
             "Ratification by half the states applies only to federal items.",
             "Simple-majority items (new states, boundaries) sit outside Article 368."],
            "Knowing the three routes settles all the procedure questions.",
            "Amendment of which provision needs ratification by at least half the state legislatures?",
            ["Look for a federal item.", "The election of the President and the Seventh Schedule are examples."],
            "Any federal provision, such as the President's election or the Seventh Schedule"),
        pat("ga-polam-p2", "42nd and 44th: the twin landmarks", "very common",
            "The question asks which amendment is the Mini-Constitution, or which removed the right to property.",
            ["The 42nd (1976) added socialist, secular, integrity, Fundamental Duties and moved the Lok Sabha term to 6 years.",
             "The 44th (1978) moved property to Article 300A and replaced 'internal disturbance' with 'armed rebellion'.",
             "Remember them as a pair: the 42nd added, the 44th corrected."],
            "The two amendments are linked, so one story covers both.",
            "The words 'armed rebellion' in Article 352 replaced which earlier expression?",
            ["The 44th Amendment made this change.", "The old ground was vaguer."],
            "Internal disturbance"),
        pat("ga-polam-p3", "Recent amendments, 2016 to 2023", "common",
            "The question asks what the 101st, 103rd or 106th Amendment deals with.",
            ["101st is GST. 102nd is the Backward Classes Commission (Article 338B). 103rd is EWS 10%.",
             "104th ended Anglo-Indian nominations. 105th lets states identify OBCs. 106th is women's one-third.",
             "99th (NJAC) was struck down. 100th is the Land Boundary Agreement. 97th is cooperatives."],
            "Each number has one topic, so a ladder answers every match.",
            "The 106th Constitutional Amendment Act (2023) provides for what?",
            ["It is about women's seats.", "It applies after delimitation."],
            "One-third reservation of seats for women in the Lok Sabha and state assemblies"),
        pat("ga-polam-p4", "Older amendments: one-line recall", "common",
            "The question asks which amendment lowered the voting age, added the anti-defection law, or made Delhi an NCT.",
            ["Numbers ladder: 1st Ninth Schedule, 7th reorganisation, 52nd defection, 61st voting age, 69th Delhi.",
             "Then 73rd and 74th local bodies, 86th Article 21A, 91st ministry cap, 92nd four languages.",
             "Give each number a one-word hook: 61 eighteen, 69 Delhi, 101 GST."],
            "A hook per number keeps the ladder easy to recall.",
            "The voting age was reduced from 21 to 18 years by which amendment?",
            ["It amended Article 326.", "It came in the late 1980s."],
            "The 61st Amendment"),
        pat("ga-polam-p5", "Amendments between 1990 and 2003", "occasional",
            "The question asks which amendment created the SC/ST commissions, added a language or capped the ministry.",
            ["65th: National Commission for SC/ST (Article 338). 89th: separate commission for ST (Article 338A).",
             "71st added Konkani, Manipuri, Nepali. 92nd added Bodo, Dogri, Maithili, Santhali.",
             "91st caps the Council of Ministers at 15%."],
            "Commissions and languages are asked as matching pairs.",
            "Which amendment (2003) created a separate National Commission for Scheduled Tribes under Article 338A?",
            ["It came in 2003.", "Its number is between 88 and 90."],
            "The 89th Amendment"),
    ],
)

# =====================================================================
# 7. Panchayati Raj, Municipalities and Emergency
# =====================================================================
SUBS["pol-local-bodies-emergency"] = dict(
    concept=(
        "The **73rd Amendment** made Panchayats constitutional. The **74th Amendment** did the same for Municipalities. "
        "Emergency provisions sit in Part XVIII (Articles 352-360). "
        "There are three kinds: National (352), President's Rule (356) and Financial (360)."
    ),
    notes=r"""### Panchayati Raj committees
| Committee | Year | Idea |
|---|---|---|
| Balwant Rai Mehta | 1957 | Three-tier system |
| Ashok Mehta | 1977 | Two-tier: Zila Parishad and Mandal Panchayat |
| G.V.K. Rao | 1985 | District as the basic unit of planning |
| L.M. Singhvi | 1986 | Constitutional status, Gram Sabha as the base |
| P.K. Thungon | 1988 | Constitutional recognition |

The scheme began at **Nagaur, Rajasthan, on 2 October 1959**. Nehru inaugurated it.

> **Tip:** Balwant is three. Ashok is two. Singhvi is constitutional status.

### The 73rd Amendment (1992): Part IX
It took effect on **24 April 1993**, now National Panchayati Raj Day.

- The **Gram Sabha** is the base. It includes all registered voters of a village.
- Three tiers: village, intermediate, Zila Parishad. States with under 20 lakh people may skip the middle tier.
- Term: 5 years. Elections follow within 6 months if a panchayat is dissolved.
- Seats are reserved for SC/ST in proportion. At least **one-third** of seats are for women. Many states give 50%. Bihar was first, in 2006.
- **State Election Commission** (Article 243K) runs the elections.
- **State Finance Commission** (Article 243-I) reviews finances every **5 years**.
- The **Eleventh Schedule** lists **29 subjects**.

### The 74th Amendment (1992): Part IX-A
It took effect on **1 June 1993**. Articles are 243P-243ZG. The **Twelfth Schedule** lists **18 subjects**.

| Area | Body |
|---|---|
| Transitional area | Nagar Panchayat |
| Smaller urban area | Municipal Council |
| Larger urban area | Municipal Corporation |

Wards committees are needed for municipalities with 3 lakh or more people. The 97th Amendment (2011) added Part IX-B for cooperative societies.

### National Emergency: Article 352
It has been proclaimed **three times**: 1962 (China), 1971 (Pakistan) and 1975.

- Grounds: war, external aggression, **armed rebellion** (the 44th Amendment replaced 'internal disturbance').
- Both Houses must approve within **one month**. Each approval lasts **6 months** and can be renewed.
- **Article 358** suspends Article 19 automatically, only in war or external aggression.
- **Article 359** lets the President suspend other rights by order. Articles 20 and 21 can never be suspended.

### President's Rule and Financial Emergency
**President's Rule (Article 356)** applies when a state's constitutional machinery fails.

- First used in **Kerala in 1959**. It has been imposed over 130 times.
- Parliament must approve within **2 months**. It lasts 6 months at a time, up to **3 years**.
- **S.R. Bommai (1994)** made the proclamation subject to judicial review. It also said a ministry's majority is tested on the floor of the House.

**Financial Emergency (Article 360)** covers threats to financial stability. Salaries of officials, including judges, can be cut. It has **never been imposed**.
""",
    tricks=[
        trick("Committee tier rhyme",
              "Balwant-3 (1957), Ashok-2 (1977), Rao-district (1985), Singhvi-Constitution (1986). Remember the years as 57, 77, 85, 86.",
              "Which committee's report led to the Nagaur launch on 2 October 1959?",
              ["The Nagaur launch followed the 1957 report.", "That committee recommended a three-tier system."], "The Balwant Rai Mehta Committee"),
        trick("Emergency digits",
              "352 is National, with three proclamations (1962, 1971, 1975). 356 is President's Rule, first used in Kerala in 1959. 360 is Financial, used zero times.",
              "Which state first faced President's Rule in 1959?",
              ["Recall the state first placed under Article 356.", "The elected government of E.M.S. Namboodiripad was dismissed."], "Kerala"),
    ],
    mistakes=[
        mis("Saying the 73rd Amendment created Panchayats in 1959.", "1959 is only Rajasthan's launch. Constitutional status came in 1992-93."),
        mis("Mixing the 11th Schedule (29 subjects) with the 12th (18).", "Eleventh is panchayats. Twelfth is municipalities."),
        mis("Saying a Financial Emergency was declared once.", "Article 360 has never been used."),
        mis("Swapping the two Mehtas.", "Balwant Rai is three-tier. Ashok Mehta is two-tier."),
        mis("Thinking Article 19 is suspended in every Emergency.", "Article 358 applies only in war or external aggression."),
    ],
    revision=[
        "73rd: Part IX, 24 April 1993, three tiers, Gram Sabha, 29 subjects, SEC and SFC every 5 years.",
        "Committees: Balwant Rai three-tier (1957), Ashok Mehta two-tier (1977), Singhvi constitutional status (1986).",
        "74th: Part IX-A, 1 June 1993, 18 subjects, Nagar Panchayat, Council, Corporation.",
        "National Emergency: 'armed rebellion', approval within one month, renewal every 6 months.",
        "Articles 20 and 21 are never suspended. Article 358 suspends Article 19 automatically.",
        "President's Rule: 2-month approval, 6-month spells, 3-year limit. Bommai (1994): judicial review.",
        "Financial Emergency (Article 360) has never been proclaimed.",
    ],
    patterns=[
        pat("ga-polloc-p1", "73rd Amendment structure", "very common",
            "The question asks what the Gram Sabha consists of, who runs panchayat elections, or how many subjects the Eleventh Schedule has.",
            ["The base is the Gram Sabha: all registered voters of the village.",
             "The tiers are village, intermediate and Zila Parishad. States under 20 lakh may skip the middle tier.",
             "Term 5 years. Women get at least one-third. The SEC (243K) runs elections.",
             "The SFC (243-I) meets every 5 years. The Eleventh Schedule has 29 subjects."],
            "Every structural fact has one number or article.",
            "A State Finance Commission is constituted once in how many years?",
            ["It reviews the finances of panchayats.", "Article 243-I gives the rule."],
            "Five years"),
        pat("ga-polloc-p2", "Committee and recommendation", "very common",
            "The question asks which committee recommended a two-tier system or constitutional status.",
            ["Balwant Rai Mehta (1957): three-tier. Ashok Mehta (1977): two-tier.",
             "G.V.K. Rao (1985): district planning. Singhvi (1986): constitutional status and Gram Sabha.",
             "Thungon (1988): constitutional recognition.",
             "Do not swap the two Mehtas."],
            "Each committee has one headline idea.",
            "Which committee recommended a two-tier Panchayati Raj system with Zila Parishad and Mandal Panchayat?",
            ["It is a 1977 committee.", "It is not the Balwant Rai Mehta Committee."],
            "The Ashok Mehta Committee (1977)"),
        pat("ga-polloc-p3", "74th Amendment and urban bodies", "common",
            "The question asks how many subjects the Twelfth Schedule has, or which body suits a transitional area.",
            ["The Twelfth Schedule has 18 subjects. Part IX-A took effect on 1 June 1993.",
             "Transitional area: Nagar Panchayat. Smaller urban: Municipal Council. Larger urban: Municipal Corporation.",
             "Wards committees are needed above 3 lakh people."],
            "The three bodies match three sizes of area.",
            "For a transitional area, the 74th Amendment provides for which body?",
            ["Smaller urban areas get Councils.", "Larger ones get Corporations."],
            "A Nagar Panchayat"),
        pat("ga-polloc-p4", "National Emergency (Article 352)", "very common",
            "The question asks which amendment introduced 'armed rebellion', the approval period, or which rights are never suspended.",
            ["Grounds: war, external aggression, armed rebellion (44th Amendment).",
             "Both Houses approve within one month. Renewals last 6 months each.",
             "Article 358 suspends Article 19 automatically in war or external aggression.",
             "Article 359 allows suspension of other rights. Articles 20 and 21 are never suspended."],
            "The 44th Amendment sits behind most of the numbers.",
            "Which Fundamental Rights can never be suspended during an Emergency?",
            ["The 44th Amendment protected two Articles.", "They cover conviction protection and life and liberty."],
            "Articles 20 and 21"),
        pat("ga-polloc-p5", "President's Rule and Financial Emergency", "common",
            "The question asks the approval period for Article 356, the maximum duration, or which case made it reviewable.",
            ["Article 356: approval within 2 months, 6-month spells, maximum 3 years.",
             "S.R. Bommai (1994): judicial review, and a majority test on the floor of the House.",
             "Article 360 has never been used."],
            "Bommai and the time limits carry most of the marks.",
            "Which case held that a proclamation under Article 356 is subject to judicial review?",
            ["It was decided in 1994.", "It also said the majority is tested in the House."],
            "S.R. Bommai v. Union of India (1994)"),
        pat("ga-polloc-p6", "Panchayati Raj milestones", "occasional",
            "The question asks where or when Panchayati Raj began, or when the 73rd Amendment took effect.",
            ["The scheme was launched at Nagaur, Rajasthan, on 2 October 1959.",
             "The 73rd Amendment took effect on 24 April 1993 (National Panchayati Raj Day).",
             "Bihar was first to raise women's reservation to 50% (2006)."],
            "Dates and places are fixed and easy to test.",
            "On which date is National Panchayati Raj Day observed?",
            ["It marks the day the 73rd Amendment took effect.", "The year was 1993."],
            "24 April"),
    ],
)

# =====================================================================
# 8. Constitutional and statutory bodies
# =====================================================================
SUBS["pol-bodies"] = dict(
    concept=(
        "**Constitutional bodies** exist because an Article says so, such as the Election Commission and the CAG. "
        "**Statutory bodies** exist because a law of Parliament created them, such as the NHRC and Lokpal. "
        "**NITI Aayog** is neither. A Cabinet resolution created it."
    ),
    notes=r"""### Constitutional bodies
| Body | Article | Head (as on 23 Sep 2026) |
|---|---|---|
| Election Commission | 324 | CEC Gyanesh Kumar (26th CEC, since Feb 2025) |
| UPSC | 315-323 | Dr Ajay Kumar (since 15 May 2025) |
| CAG | 148 | K. Sanjay Murthy (15th CAG, since Nov 2024) |
| Attorney-General | 76 | R. Venkataramani (16th AG, extended till 30 Sep 2027) |
| Finance Commission | 280 | 16th FC: Dr Arvind Panagariya |

> **Watch:** Names change. Learn the structure now and re-check the names just before your exam.

### Election Commission (Article 324)
It conducts elections to Parliament, state assemblies and the offices of President and Vice-President. Since **1993** it has three members: the CEC and two Election Commissioners with equal powers.

- The **CEC** can be removed only like a Supreme Court judge.
- The other Commissioners are removed on the CEC's recommendation.
- Local-body elections belong to the State Election Commissions.
- Appointments follow the 2023 Act: PM, Leader of Opposition (LS) and a Union Minister.

### UPSC and CAG
- **UPSC (Articles 315-323)**: members serve **6 years or till 65**. Expenses are charged on the Consolidated Fund. State PSC members retire at 62.
- **CAG (Article 148)**: the '**guardian of the public purse**'. Term 6 years or 65. He cannot hold any further government post. He audits the Union and states, and reports go to the President or Governor. The **PAC** examines these reports.

### Finance Commission (Article 280)
It is quasi-judicial and set up **every five years**. It has a Chairman and four members.

- It recommends how central taxes are shared: between Centre and states (vertical) and among states (horizontal).
- It also recommends grants-in-aid and support for panchayats and municipalities.
- Its advice is **not binding**.
- The 16th FC report was tabled on **1 February 2026**. The award period is **2026-31**. The states' share stays **41%** of the divisible pool.

### Statutory and other bodies
| Body | Parent law |
|---|---|
| CVC | CVC Act, 2003 |
| CIC | RTI Act, 2005 |
| NHRC | Protection of Human Rights Act, 1993 |
| Lokpal | Lokpal and Lokayuktas Act, 2013 |
| NGT | National Green Tribunal Act, 2010 |
| NCW | National Commission for Women Act, 1990 |
| NITI Aayog | Cabinet resolution, 1 Jan 2015 (neither) |

NITI Aayog replaced the Planning Commission (1950). The PM chairs it.

### Other constitutional posts
- **Advocate-General** (Article 165): the state's chief law officer.
- **NCSC** (Article 338) and **NCBC** (Article 338B).
- **Special Officer for Linguistic Minorities** (Article 350B).
- **Attorney-General** can speak in Parliament but cannot vote.

> **Rule:** If the source is an Article, the body is constitutional. If the source is a dated Act, it is statutory.
""",
    tricks=[
        trick("Article blocks for bodies",
              "76 AG, 148 CAG, 280 FC, 315 UPSC, 324 EC. Reading upward gives the order AG, CAG, FC, UPSC, EC.",
              "Under which Article is the Comptroller and Auditor General appointed?",
              ["Recall the block after 76.", "The Article is 148."], "Article 148"),
        trick("Statutory versus constitutional filter",
              "A dated Act (NHRC 1993, CVC 2003, CIC 2005, Lokpal 2013) means statutory. An Article number means constitutional. NITI Aayog is neither.",
              "Name a high-profile advisory body that is neither constitutional nor statutory.",
              ["It was set up by a Cabinet resolution in 2015.", "It replaced the Planning Commission."], "NITI Aayog"),
    ],
    mistakes=[
        mis("Calling NITI Aayog a statutory body.", "It was created by a Cabinet resolution."),
        mis("Saying the 15th FC still governs transfers.", "From FY 2026-27 the 16th FC (41% share, 2026-31) applies."),
        mis("Saying the Estimates Committee examines CAG reports.", "The Public Accounts Committee does."),
        mis("Thinking the Finance Commission's advice is binding.", "It is advisory."),
        mis("Thinking the Election Commission runs panchayat elections.", "State Election Commissions run local-body elections."),
    ],
    revision=[
        "Election Commission: Article 324, multi-member since 1993, CEC removed like a Supreme Court judge.",
        "UPSC: Article 315, 6 years or 65, expenses charged on the Consolidated Fund.",
        "CAG: Article 148, guardian of the public purse, 6 years or 65, PAC examines reports.",
        "Finance Commission: Article 280, every 5 years, Chairman and four members, advice not binding.",
        "Statutory: CVC, CIC, NHRC, Lokpal, NGT, NCW. NITI Aayog is executive.",
        "NCSC: Article 338. NCBC: Article 338B. Linguistic minorities officer: Article 350B.",
    ],
    patterns=[
        pat("ga-polbo-p1", "Election Commission structure and removal", "very common",
            "The question asks how many members the EC has, how the CEC can be removed, or who conducts Presidential elections.",
            ["It has been multi-member since 1993: the CEC and two Election Commissioners with equal powers.",
             "The CEC is removed like a Supreme Court judge. Others are removed on the CEC's recommendation.",
             "It conducts elections to Parliament, state legislatures and the President and Vice-President.",
             "Local-body elections belong to the State Election Commissions."],
            "Structure and removal are fixed rules.",
            "In what manner can the Chief Election Commissioner be removed?",
            ["The rule copies another high office.", "It is the same as for a Supreme Court judge."],
            "In the same manner as a Judge of the Supreme Court"),
        pat("ga-polbo-p2", "UPSC and CAG: tenure and features", "common",
            "The question asks the CAG's nickname, UPSC members' tenure, or which expenses are charged on the Consolidated Fund.",
            ["UPSC: Article 315, 6 years or till 65, expenses charged on the Consolidated Fund.",
             "CAG: Article 148, 6 years or 65, no further government post.",
             "The CAG audits Union and state accounts and reports to the President or Governor.",
             "The PAC examines his reports."],
            "The two bodies share the '6 years or 65' rule.",
            "The CAG of India is appointed by the President under which Article?",
            ["The Article number sits between 76 and 280.", "It is the 148th."],
            "Article 148"),
        pat("ga-polbo-p3", "Finance Commission", "common",
            "The question asks how often it is formed, who sits on it, or whether its advice binds.",
            ["Article 280: quasi-judicial, formed every five years.",
             "It has a Chairman and four members.",
             "It recommends tax sharing (vertical and horizontal) and grants-in-aid.",
             "Its advice is not binding."],
            "The five-year cycle and non-binding advice are the usual tests.",
            "The Finance Commission is normally formed once in how many years?",
            ["It is set by Article 280.", "It is quasi-judicial."],
            "Every five years"),
        pat("ga-polbo-p4", "Constitutional, statutory and executive bodies", "very common",
            "The question asks which body is constitutional, what created NITI Aayog, or which is the odd one out.",
            ["Constitutional: EC, UPSC, CAG, Finance Commission, NCSC (338), NCBC (338B).",
             "Statutory: CVC (2003), CIC (2005), NHRC (1993), Lokpal (2013), NGT (2010), NCW (1990).",
             "Executive: NITI Aayog (Cabinet resolution, 1 Jan 2015)."],
            "The parent law or Article gives the answer at once.",
            "Which of these is not a statutory body: CVC, CIC, NHRC or NITI Aayog?",
            ["The CVC, CIC and NHRC each rest on an Act.", "One was created by a Cabinet resolution."],
            "NITI Aayog"),
        pat("ga-polbo-p5", "Rights commissions and special officers", "occasional",
            "The question asks under which Article the NCSC sits, or which amendment gave NCBC constitutional status.",
            ["NCSC is Article 338. The separate ST commission is Article 338A.",
             "NCBC is Article 338B, given constitutional status by the 102nd Amendment (2018).",
             "The Special Officer for linguistic minorities is Article 350B."],
            "Each body has its own Article number.",
            "The NCBC was given constitutional status by which amendment?",
            ["It inserted Article 338B.", "It came in 2018."],
            "The 102nd Amendment"),
        pat("ga-polbo-p6", "Current heads and latest Finance Commission", "occasional",
            "The question names a current post and asks who holds it, or asks about the latest Finance Commission.",
            ["Recall the CEC, UPSC Chairman, CAG and Attorney-General from the first table.",
             "Recall the 16th FC: Dr Arvind Panagariya, award 2026-31, states' share 41%.",
             "Re-check the names before the exam."],
            "Current names are the one part of this topic that changes.",
            "The 16th Finance Commission recommends what share of the divisible pool for states?",
            ["The share is the same as the 15th FC.", "The award period is 2026-31."],
            "41%"),
    ],
)


# ---------------------------------------------------------------------
def long_lines(text, limit=24):
    plain = re.sub(r"\$\$.*?\$\$|\$[^$]*\$", "X", text, flags=re.S)
    plain = re.sub(r"^\s*(?:[-*>|]|\d+[.)])\s*", "", plain, flags=re.M)
    return [s for s in re.split(r"(?<=[.!?])\s+|\n", plain) if len(s.split()) > limit]


data = json.loads(TOPIC.read_text(encoding="utf-8"))
assert set(SUBS) == {s["id"] for s in data["subtopics"]}, "every subtopic must be rewritten"
for sub in data["subtopics"]:
    new = SUBS[sub["id"]]
    old_ids = {p["id"] for p in sub.get("patterns", [])}
    new_ids = [p["id"] for p in new["patterns"]]
    assert old_ids <= set(new_ids), (sub["id"], old_ids - set(new_ids))
    assert len(new_ids) == len(set(new_ids))
    n = new["notes"].strip() + "\n"
    assert 2500 <= len(n) <= 5000, (sub["id"], len(n))
    assert 4 <= len(re.findall(r"^### ", n, re.M)) <= 8, sub["id"]
    for p in new["patterns"]:
        assert 3 <= len(p["steps"]) <= 5 and 2 <= len(p["example"]["steps"]) <= 5, p["id"]
    for ln in long_lines(n + "\n" + new["concept"]):
        print("  long:", sub["id"], ln[:90])
    sub.update(concept=new["concept"], notes=n, tricks=new["tricks"], mistakes=new["mistakes"],
               revision=new["revision"], patterns=new["patterns"])
    sub.pop("formulas", None) if not sub.get("formulas") else None
all_ids = [p["id"] for s in data["subtopics"] for p in s["patterns"]]
assert len(all_ids) == len(set(all_ids)), "pattern id clash"
TOPIC.write_text(json.dumps(data, ensure_ascii=False, indent=1) + "\n", encoding="utf-8", newline="\n")
for s in data["subtopics"]:
    print(s["id"], len(s["notes"]), "chars,", len(s["patterns"]), "patterns")
