"""Phase-2 deep content for ga/current-affairs — full static rebuild.

The topic was month-based (mar-2026 … sep-2026 + standing-anchors) with practice whose
`subtopic` pointed at the topic id, which fails the deep-content contract. This script
replaces subtopics/practice/pyqPatterns/solvedExamples with the static 'how to prepare
current affairs' topic: question frames, award/sports/summit categories, important days
and indexes. Topic-level fields (id, sectionId, order, importance, avgQuestions) carry over.
Run: py -3 ca-topic.py
"""
import os
import sys

sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
from _lib import Sub, load, save, verify, report
from cat_part1 import build_strategy, build_awards, build_sports
from cat_part2 import build_summits, build_days, build_indexes


def mk(sid, title, concept, tricks, mistakes, sub):
    entry = {
        "id": sid,
        "title": title,
        "concept": concept,
        "tricks": tricks,
        "formulas": [],
        "mistakes": mistakes,
        "notes": sub.notes,
        "patterns": sub.patterns,
    }
    return entry, sub.questions


def se(n, pattern, diff, q, opts, ans_idx, sol, sc=None, t=30):
    return {"id": f"ca-se{n:02d}", "q": q, "figure": None, "options": list(opts),
            "answer": ans_idx, "solution": sol, "shortcut": sc, "difficulty": diff,
            "subtopic": "current-affairs", "pattern": pattern, "timeSec": t}


def P(pattern, frequency, howToSpot, approach, subtopic, q, sol):
    return {"pattern": pattern, "frequency": frequency, "howToSpot": howToSpot, "approach": approach,
            "subtopic": subtopic, "example": {"q": q, "solution": sol}}


if __name__ == "__main__":
    specs = [
        ("ca-strategy", "How current-affairs questions are framed", build_strategy()),
        ("ca-awards", "Award categories to track — structure, not winners", build_awards()),
        ("ca-sports", "Sports events and how tournament news is asked", build_sports()),
        ("ca-summits", "Summits, groupings and organisations to track", build_summits()),
        ("ca-days", "Important days — national and UN framework", build_days()),
        ("ca-indexes", "Indexes and reports — index ↔ publisher", build_indexes()),
    ]
    concepts = {
        "ca-strategy": "CA questions come in four frames — **direct recall**, **match-the-column**, **statement-based** and the **CA-to-static bridge**. Track ten buckets monthly: appointments, awards, sports, summits, schemes, defence, space, indexes, days, economy. Note the **pairing** (person↔post, award↔field, day↔theme, index↔publisher), work from a 6-12 month window, and revise one monthly source three times.",
        "ca-awards": "Learn the ladders, not the winners: civilian **Bharat Ratna (1954) > Padma Vibhushan > Padma Bhushan > Padma Shri**; gallantry wartime **PVC > MVC > Vir Chakra**, peacetime **Ashoka > Kirti > Shaurya Chakra**; sports **Khel Ratna (1991-92, renamed 2021) > Arjuna (1961) > Dronacharya (1985, coaches)**; literature **Jnanpith (1965)**, cinema **Dadasaheb Phalke (1969)**; global **Nobel (1901, Economics 1969, Peace at Oslo)** and **Magsaysay (1957, Manila)**.",
        "ca-sports": "For every tournament note five: **host, motto/theme, mascot, champion, India's highlight**. Cycles: Olympics/CWG/Asian Games/FIFA/ODI WC four-yearly; T20 WC and Thomas/Uber biennial; IPL and Khelo India annual. Firsts: Olympics 1896 Athens, Winter 1924, CWG 1930, Asian Games 1951 New Delhi, Cricket WC 1975. India: 1900 debut, 8 hockey golds, Bindra 2008, Thomas Cup 2022.",
        "ca-summits": "Note **host city, theme, membership change, HQ** per summit. Anchors: UN 1945 (193 members, UNSC 5+10), NAM 1961, ASEAN 1967 Jakarta, SAARC 1985 Kathmandu (8), BIMSTEC 1997 Dhaka (7), G20 1999/2008 (AU joined 2023), SCO 2001 Beijing (India-Pak 2017), first BRICS summit 2009 (NDB Shanghai), Commonwealth 56/London. India is **not** in APEC, ASEAN, G7, NATO or OPEC.",
        "ca-days": "National person-days: Youth 12 Jan (Vivekananda), Sports 29 Aug (Dhyan Chand), Teachers 5 Sep (Radhakrishnan), Unity 31 Oct (Patel), Children 14 Nov (Nehru), Maths 22 Dec (Ramanujan). Event-days: Science 28 Feb (Raman effect), Technology 11 May (Pokhran 1998), Constitution 26 Nov (adopted 1949, observed since 2015). Defence: Army 15 Jan, Air Force 8 Oct, Navy 4 Dec. UN set: Yoga 21 Jun (India's proposal, first 2015), Environment 5 Jun, Human Rights 10 Dec.",
        "ca-indexes": "The whole game is **index ↔ publisher**: HDI — UNDP; Happiness — UN SDSN; Innovation — WIPO; WEO — IMF; Human Capital — World Bank; Gender Gap/Risks/Tourism — WEF; Corruption — Transparency International; Hunger — Concern Worldwide + Welthungerhilfe (NGOs, not UN); Peace — IEP; Press Freedom — RSF; ASER — Pratham; SDG India and Innovation indexes — NITI Aayog; FI-Index — RBI. Doing Business (World Bank) discontinued 2021 → B-READY 2024.",
    }
    tricks = {
        "ca-strategy": [{"title": "Pairing drill", "body": "Read any news item and write its two halves — e.g. 'X award → field', 'Y summit → host'. Exams ask the halves, not the story.", "example": {"q": "A new Chief Justice is sworn in. What do you note?", "solution": "Post ↔ person (and the appointment mechanism — collegium recommendation, President's appointment) — not the ceremony details."}}],
        "ca-awards": [{"title": "Ladder memory", "body": "Civilian: **Ratna > Vibhushan > Bhushan > Shri**. Sports: **Khel Ratna > Arjuna (players) > Dronacharya (coaches)** — teachers below students is the joke that fixes the order.", "example": {"q": "Fourth-highest civilian honour?", "solution": "Padma Shri — count down the ladder; 'Shri' rhymes with 'fourth' is a common mnemonic."}}],
        "ca-sports": [{"title": "Cycle split", "body": "Four-yearly: Olympics, Winter, CWG, Asian Games, FIFA, ODI WC. **Two-yearly: T20 WC, Thomas/Uber**. Annual: IPL, Ranji, Khelo India.", "example": {"q": "How often is the T20 World Cup held?", "solution": "Every two years — the ODI World Cup is the four-yearly one."}}],
        "ca-summits": [{"title": "HQ trio", "body": "**SCO — Beijing; SAARC — Kathmandu; BIMSTEC — Dhaka** — the three most-swapped headquarters. ASEAN sits at Jakarta as the fourth.", "example": {"q": "BIMSTEC's secretariat is at?", "solution": "Dhaka — while SAARC (the other South Asian bloc) is at Kathmandu."}}],
        "ca-days": [{"title": "Person-day strings", "body": "Chain them by date: **12 Jan Vivekananda → 1 Jul B.C. Roy → 29 Aug Dhyan Chand → 5 Sep Radhakrishnan → 31 Oct Patel → 14 Nov Nehru → 22 Dec Ramanujan**.", "example": {"q": "National Sports Day honours whom?", "solution": "Major Dhyan Chand — 29 August; the sports awards are conferred the same day."}}],
        "ca-indexes": [{"title": "UN vs NGO split", "body": "UN bodies: UNDP (HDI), SDSN (Happiness), WIPO (Innovation), IMF (WEO). NGOs: **Hunger = Concern + Welthungerhilfe**, Peace = IEP, Press = RSF, ASER = Pratham, Corruption = TI.", "example": {"q": "Who publishes the Global Hunger Index?", "solution": "Two NGOs — Concern Worldwide and Welthungerhilfe; any UN body in the options is the trap."}}],
    }
    mistakes = {
        "ca-strategy": ["Reading five sources once each instead of one source revised thrice.", "Studying the news story while ignoring the pairing the exam actually asks.", "Assuming CA never connects back to static GK."],
        "ca-awards": ["Calling Param Vir Chakra a civilian award — it is the highest *wartime gallantry* medal.", "Confusing Dronacharya (coaches) with Arjuna (players).", "Placing Padma Shri above Padma Bhushan."],
        "ca-sports": ["Mixing the two-year T20 World Cup cycle with the four-yearly ODI World Cup.", "Swapping Thomas Cup (badminton) into football or tennis options.", "Attributing the first Asian Games to Bangkok instead of New Delhi (1951)."],
        "ca-summits": ["Marking India an APEC member — it is not.", "Putting SAARC's HQ at Dhaka (that is BIMSTEC); SAARC sits at Kathmandu.", "Confusing the G20's founding (1999) with its first leaders' summit (2008)."],
        "ca-days": ["Equating Constitution Day (26 Nov, adoption 1949) with Republic Day (26 Jan, in force 1950).", "Confusing Teachers' Day (Radhakrishnan, 5 Sep) with National Education Day (Azad, 11 Nov).", "Placing Air Force Day on 4 December — that is Navy Day; the IAF day is 8 October."],
        "ca-indexes": ["Attributing the Global Hunger Index to a UN body — it is published by two NGOs.", "Crediting the HDI to the World Bank; it belongs to UNDP.", "Reciting last year's rank without checking the current edition — ranks, unlike publishers, expire."],
    }
    subtopics, practice = [], []
    for sid, title, sub in specs:
        entry, qs = mk(sid, title, concepts[sid], tricks[sid], mistakes[sid], sub)
        subtopics.append(entry)
        practice.extend(qs)

    PYQ = [
        P("Award categories and structures in the news", "very common",
          "'X award is given in the field of', 'the highest civilian award', 'Dronacharya honours whom', plus statement sets on instituting years and first recipients.",
          "Revise ladders, not winners: Bharat Ratna > Padma Vibhushan > Padma Bhushan > Padma Shri (all 1954); PVC > MVC > Vir (wartime) and Ashoka > Kirti > Shaurya (peacetime); Khel Ratna > Arjuna (players) > Dronacharya (coaches) > Dhyan Chand (lifetime) > MAKA (university). Years: Jnanpith 1965, Phalke 1969, Nobel 1901/Economics 1969, Magsaysay 1957.",
          "ca-awards",
          "The **Dronacharya Award** is given to —",
          "Outstanding **coaches** (instituted 1985) — players receive the Arjuna Award."),
        P("Sports event facts: host, motto, mascot and tally", "very common",
          "'The X tournament was hosted by', 'which country won', 'the mascot was', or statements mixing host, champion and cycle.",
          "One line per event in the window: host — champion — India's highlight — any record. Cycles: four-yearly (Olympics, CWG, Asian Games, FIFA, ODI WC), biennial (T20 WC, Thomas/Uber), annual (IPL, Khelo India). Static pins: Olympics 1896 Athens/IOC Lausanne, Asian Games 1951 New Delhi, Cricket WC 1975.",
          "ca-sports",
          "The **Thomas Cup** is related to which sport?",
          "**Badminton** (men's team) — Uber Cup is the women's counterpart; India first won in 2022."),
        P("Summits and groupings: host, theme, membership, HQ", "very common",
          "'The latest X summit was held at', 'who chairs/members', 'the headquarters of the grouping is', and India in-or-out statements.",
          "Memorise per group: HQ and members first (SCO Beijing, SAARC Kathmandu-8, BIMSTEC Dhaka-7, ASEAN Jakarta, UN New York-193, Commonwealth London-56), then the window's host and theme. India in: G20, BRICS, SCO, QUAD, SAARC, BIMSTEC, Commonwealth. India out: APEC, ASEAN, G7, NATO, OPEC.",
          "ca-summits",
          "The **African Union** became a permanent G20 member at which summit?",
          "The **New Delhi G20 (2023)** — the second regional bloc after the EU."),
        P("Important days: day ↔ person/event ↔ theme", "very common",
          "'X day is observed to commemorate', 'whose birth anniversary', matching columns of days, months and causes.",
          "Person-days: Vivekananda 12 Jan, B.C. Roy 1 Jul, Dhyan Chand 29 Aug, Radhakrishnan 5 Sep, Patel 31 Oct, Nehru 14 Nov, Ramanujan 22 Dec. Event-days: Raman effect 28 Feb, Pokhran 11 May 1998, Trident 4 Dec, Constitution adoption 26 Nov (since 2015). UN set: Yoga 21 Jun (India's proposal, first 2015), Environment 5 Jun, HR 10 Dec.",
          "ca-days",
          "**National Science Day** (28 February) commemorates —",
          "The discovery of the **Raman effect** (1928)."),
        P("Indexes and reports: index ↔ publisher", "very common",
          "'Which organisation releases the X index', match-the-column of indexes and publishers, and 'which pairing is wrong' options.",
          "Grid by publisher family: UNDP (HDI), UN SDSN (Happiness, global SDG), WIPO (Innovation), IMF (WEO), World Bank (Human Capital; Doing Business discontinued 2021 → B-READY), WEF (Gender Gap, Risks, Tourism), Transparency International (corruption CPI), IEP (Peace), RSF (Press Freedom), Concern + Welthungerhilfe (Hunger — the NGO trap), IMD, EIU, Yale/Columbia (EPI). India: NITI (SDG India, Innovation), RBI (FI-Index), Pratham (ASER).",
          "ca-indexes",
          "The **Global Hunger Index** is released by —",
          "**Concern Worldwide and Welthungerhilfe** — two NGOs; naming a UN body is the planted error."),
        P("Appointments: tracking post ↔ office", "very common",
          "'Who has been appointed as', match-the-column of posts and persons, and 'which office does X hold' one-liners from the window.",
          "For every appointment note **person ↔ post** in one line, and the appointment layer beneath it: President appoints Governors, CJI, CEC, CAG; collegium route for judges; regulators by the government under their Acts. Posts change — revise the window's list twice before the exam; the appointment mechanism itself is static and permanent.",
          "ca-strategy",
          "A Governor of a state is appointed by —",
          "The **President** of India (Article 155) — the static layer under every gubernatorial appointment news item."),
        P("Statement-based current affairs", "very common",
          "Two or three numbered statements blend one wrong detail — a wrong host city, ministry, year or publisher — into otherwise correct news facts.",
          "Attack the most checkable statement first: years, publishers and HQs rarely change, so a wrong one is quickly provable. 'APEC member', 'WPI target', 'Padma Shri highest', 'SAARC at Dhaka' are recurring planted errors. One verified falsehood eliminates every option containing that statement.",
          "ca-strategy",
          "Consider: 1. NITI Aayog releases the SDG India Index. 2. The Global Hunger Index is a UNDP product. Which are correct?",
          "Statement 1 only — the Hunger Index belongs to **Concern Worldwide + Welthungerhilfe**, not UNDP."),
        P("CA-to-static bridge questions", "common",
          "A news item (award, summit, launch, day) is cited and the question pivots to its permanent structure — founding year, article, ministry, organising body.",
          "Keep a bridge list per bucket: award news → instituting year and first recipient; summit news → group founding and HQ; scheme news → ministry and launch year; day news → the person or event commemorated; index news → publisher. The static layer is the durable half of the question — learn it once, reuse every cycle.",
          "ca-strategy",
          "A news item reports the newest **Human Development Report**. The permanent fact to recall is —",
          "The **HDI is published by the UNDP** — publisher pairings outlive every edition."),
    ]

    solved = [
        se(1, "ga-caaw-p2", "medium",
           "Match the sports award with its field:\n1. Khel Ratna 2. Dronacharya 3. MAKA Trophy\n(i) coaches (ii) university (iii) highest sporting honour",
           ["1-iii, 2-i, 3-ii", "1-i, 2-ii, 3-iii", "1-ii, 2-iii, 3-i", "1-iii, 2-ii, 3-i"],
           0,
           "Khel Ratna is the **highest sporting honour** (1991-92, renamed 2021), Dronacharya (1985) goes to **coaches**, and the MAKA Trophy (1956-57) to the best **university**. Work the field column first; the years confirm.",
           "Ratna=highest, Drona=coach, MAKA=university."),
        se(2, "ga-caday-p1", "easy",
           "**National Sports Day** is observed on 29 August to mark the birth anniversary of —",
           ["Sardar Patel", "Major Dhyan Chand", "Jawaharlal Nehru", "Swami Vivekananda"],
           1,
           "**Major Dhyan Chand**, the hockey wizard — 29 August; the sports awards are conferred the same day. Patel rides 31 October, Nehru 14 November and Vivekananda 12 January.",
           "Hockey wizard = 29 August."),
        se(3, "ga-cain-p2", "medium",
           "The **Global Hunger Index** is published by —",
           ["UNDP and FAO", "The World Food Programme", "Concern Worldwide and Welthungerhilfe", "The WHO"],
           2,
           "Two NGOs — **Concern Worldwide (Ireland) and Welthungerhilfe (Germany)**. Every UN body in the options is the planted trap; the GHI has never been a UN product.",
           "Hunger = two NGOs, never UN."),
    ]

    data = load("current-affairs")
    data["title"] = "Current Affairs — How to Prepare"
    data["summary"] = ("The static layer of current affairs: how CA questions are framed, the award, sports, summit, "
                       "day and index categories to track every month, and the pairing-based method to revise them — "
                       "structure that never expires, whatever the news cycle.")
    data["subtopics"] = subtopics
    data["practice"] = practice
    data["pyqPatterns"] = PYQ
    data["solvedExamples"] = solved
    verify(data)
    save("current-affairs", data)
    report("current-affairs", data)
