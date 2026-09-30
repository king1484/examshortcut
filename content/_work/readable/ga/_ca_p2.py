"""Current Affairs part 2: ca-summits, ca-days, ca-indexes.

Static layer only: facts are kept exactly as in the earlier notes. No new recent-event facts.
"""
from _eco_common import pat, mis, trick

# --- counts used in the text -------------------------------------------------------
assert 5 + 10 == 15          # UNSC seats
BIMSTEC = ["Bangladesh", "Bhutan", "India", "Myanmar", "Nepal", "Sri Lanka", "Thailand"]
assert len(BIMSTEC) == 7
QUAD = ["India", "USA", "Japan", "Australia"]
assert len(QUAD) == 4

SUBS = {}

# =====================================================================
SUBS["ca-summits"] = dict(
    concept=(
        "For every grouping, learn four things: members, headquarters, founding year and what changed recently. "
        "Members and headquarters rarely change, so learn them once. "
        "The host city and theme change every summit, so note them in one line each. "
        "India is not a member of APEC, ASEAN, G7, NATO or OPEC."
    ),
    notes=r"""### What a summit question asks
A summit question checks one of four details. They are the host, the members, the headquarters (HQ) and what changed.

Members and HQ stay the same for years. Learn them once. The host city and the theme change with every summit.

> **Example:** "G20, New Delhi, 2023. The African Union joined." One line gives the host, the year and the change.

### The groupings to know
| Grouping | Founded | HQ | Key facts |
|---|---|---|---|
| G20 | 1999 (finance ministers); leaders' summits from 2008 | None; the presidency rotates | 19 countries + European Union; African Union joined 2023 |
| BRICS | Name coined 2001; first summit 2009 | New Development Bank (NDB) at Shanghai | Brazil, Russia, India, China; South Africa 2010; expanded 2024 |
| SCO | 2001, grew out of the Shanghai Five | Beijing (anti-terror unit RATS at Tashkent) | India and Pakistan full members 2017; Belarus 2024 |
| QUAD | 2007, revived 2017 | No HQ | India, USA, Japan, Australia; leaders' meetings since 2021 |
| ASEAN | 1967, Bangkok Declaration | Jakarta | Southeast Asian bloc; India is only a dialogue partner |
| SAARC | 1985, first summit at Dhaka | Kathmandu | 8 South Asian members; SAFTA from 2006 |
| BIMSTEC | 1997 | Dhaka | 7 Bay of Bengal countries |
| Commonwealth | Modern form from the London Declaration, 1949 | London (Marlborough House) | 56 members; the British Sovereign is Head |
| NAM | 1961, Belgrade | No HQ | India is a founding member |

The 2024 BRICS entrants include Egypt, Ethiopia, Iran and the UAE. The seven BIMSTEC members are Bangladesh, Bhutan, India, Myanmar, Nepal, Sri Lanka and Thailand.

> **Tip:** Three HQs get swapped most: SCO at Beijing, SAARC at Kathmandu, BIMSTEC at Dhaka.

### The United Nations
The UN was founded in **1945** with 51 founding members. It now has **193 members**. Its HQ is in New York. Its main court, the International Court of Justice (ICJ), sits at The Hague.

The Security Council (UNSC) has 15 seats:

- **5 permanent** members with a veto: the US, UK, France, Russia and China.
- **10 non-permanent** members, elected for **two-year** terms.

India has been elected a non-permanent member **eight times**. Its latest term was 2021-22. India has long pressed for reform of the Council.

### India in or out
| India is a member | India is not a member |
|---|---|
| UN, G20, BRICS, SCO, QUAD | APEC |
| SAARC, BIMSTEC, Commonwealth, NAM | ASEAN (dialogue partner only) |
| IMF, World Bank, WTO, AIIB, ADB | G7, NATO, OPEC |

India hosts the **International Solar Alliance** with France. Its HQ is at Gurugram. India has at times led the G77, the group of developing countries at the UN.

> **Watch:** APEC is the classic trap. India trades with Pacific countries but is not an APEC member.

### How to note a summit
Write one line per summit: group, host city or country, theme, what changed.

After the host, membership change is the most asked detail. Past examples are the African Union joining the G20, Belarus joining the SCO and the BRICS expansion.

Themes are often slogans. The New Delhi G20 theme was "Vasudhaiva Kutumbakam: One Earth, One Family, One Future".
""",
    tricks=[
        trick("HQ trio",
              "SCO sits at Beijing, SAARC at Kathmandu and BIMSTEC at Dhaka. ASEAN at Jakarta is the fourth to learn.",
              "Where is the BIMSTEC secretariat?",
              ["BIMSTEC is the Bay of Bengal group.", "SAARC, the other South Asian group, is at Kathmandu.",
               "BIMSTEC is at Dhaka."],
              "Dhaka"),
        trick("Five 'not a member' names",
              "India is outside APEC, ASEAN, G7, NATO and OPEC. Any option with one of these is the answer to a 'not a member' question.",
              "India is not a member of which of these: SCO, BRICS, APEC, BIMSTEC?",
              ["SCO, BRICS and BIMSTEC all include India.", "APEC is on the 'not a member' list."],
              "APEC"),
    ],
    mistakes=[
        mis("Marking India as an APEC member.", "India is not in APEC. It is also outside ASEAN, G7, NATO and OPEC."),
        mis("Putting SAARC's HQ at Dhaka.", "SAARC is at Kathmandu. Dhaka is the BIMSTEC HQ."),
        mis("Taking 2008 as the year the G20 was founded.", "The G20 began in 1999 with finance ministers. Leaders' summits began in 2008."),
        mis("Calling India an ASEAN member.", "India is only a dialogue partner of ASEAN."),
        mis("Giving UNSC non-permanent members a five-year term.", "Their term is two years. Five is the number of permanent members."),
    ],
    revision=[
        "G20: 1999, leaders' summits from 2008, no HQ; African Union joined 2023.",
        "BRICS: first summit 2009; NDB at Shanghai; South Africa 2010; expanded 2024.",
        "SCO: 2001, Beijing; India and Pakistan joined 2017; Belarus 2024.",
        "QUAD: India, USA, Japan, Australia; revived 2017.",
        "ASEAN 1967 Jakarta. SAARC 1985 Kathmandu (8). BIMSTEC 1997 Dhaka (7).",
        "UN 1945, 193 members; UNSC = 5 permanent + 10 non-permanent (two-year terms).",
        "Commonwealth: 56 members, London. NAM: 1961, Belgrade.",
        "India is not in APEC, ASEAN, G7, NATO or OPEC.",
    ],
    patterns=[
        pat("ga-casum-p1", "Summit, host and theme", "very common",
            "'The X summit was hosted by', 'the theme of the summit was', or statements pairing a summit with a city.",
            ["Recall your one-line note: group, host, theme, change.",
             "Match the host city first.",
             "If cities are swapped, reject pairs from the wrong region.",
             "For a theme, look for the slogan you noted."],
            "Hosts and themes are the most asked details of any summit.",
            "The G20 Leaders' Summit hosted by India at New Delhi in 2023 had which theme?",
            ["The summit was India's G20 presidency.", "Its theme came from an old Sanskrit phrase.",
             "The same summit admitted the African Union."],
            "Vasudhaiva Kutumbakam: One Earth, One Family, One Future"),
        pat("ga-casum-p2", "Grouping, members and headquarters", "very common",
            "'X is headquartered at', 'how many members does X have', or a match-the-following of groups and cities.",
            ["Recall the HQ pins: SCO Beijing, SAARC Kathmandu, BIMSTEC Dhaka, ASEAN Jakarta.",
             "Add NDB Shanghai, Commonwealth London, ISA Gurugram.",
             "Recall counts: SAARC 8, BIMSTEC 7, UN 193, Commonwealth 56.",
             "Cross out any option that swaps two South Asian HQs."],
            "HQs and member counts are fixed, so a short list settles most questions.",
            "The headquarters of the Shanghai Cooperation Organisation (SCO) is at which city?",
            ["The SCO was founded in 2001.", "Its secretariat is in China's capital.",
             "Its anti-terror unit, RATS, is at Tashkent, not the HQ."],
            "Beijing"),
        pat("ga-casum-p3", "India's membership: in or out", "common",
            "'India is NOT a member of', or statements placing India inside or outside a grouping.",
            ["Recall the 'out' list: APEC, ASEAN, G7, NATO, OPEC.",
             "Check each option against it.",
             "Remember ASEAN gives India dialogue-partner status only."],
            "The 'out' list has only five names, so it is quicker than the 'in' list.",
            "India is NOT a member of which of the following? (a) SCO (b) BIMSTEC (c) APEC (d) G20",
            ["SCO: India joined in 2017.", "BIMSTEC and G20: India is a member.", "APEC is on the 'out' list."],
            "(c) APEC"),
        pat("ga-casum-p4", "Founding years and new members", "common",
            "'When did India join the SCO', 'which body joined the G20', or arranging groupings by founding year.",
            ["Recall years: UN 1945, NAM 1961, ASEAN 1967, SAARC 1985, BIMSTEC 1997, G20 1999, SCO 2001.",
             "Recall changes: India-Pakistan into SCO 2017, AU into G20 2023, BRICS expansion 2024, Belarus into SCO 2024.",
             "Match the change to the right group before reading other options."],
            "Each change belongs to one group and one year, so pair them as a unit.",
            "In which year did India and Pakistan become full members of the SCO?",
            ["The SCO was founded in 2001.", "Both countries were admitted together.", "Belarus joined later, in 2024."],
            "2017"),
        pat("ga-casum-p5", "UN structure and India at the UN", "common",
            "'How many members does the UN have', 'UNSC non-permanent members serve for', or India's UNSC terms.",
            ["UN: 1945, 193 members, HQ New York; ICJ at The Hague.",
             "UNSC: 15 seats, 5 permanent with veto plus 10 non-permanent.",
             "Non-permanent terms are two years.",
             "India has been elected eight times; latest term 2021-22."],
            "The UN numbers are fixed and asked again and again.",
            "Non-permanent members of the UN Security Council are elected for a term of how many years?",
            ["The Council has 15 seats.", "5 are permanent with a veto.", "The other 10 rotate on fixed terms."],
            "Two years"),
        pat("ga-casum-p6", "Name the grouping from its members", "occasional",
            "A list of countries is given and the grouping is asked, e.g. 'India, USA, Japan and Australia form'.",
            ["Count the countries in the list.",
             "Four democracies across the Indo-Pacific means QUAD.",
             "Seven Bay of Bengal countries means BIMSTEC.",
             "Eight South Asian countries means SAARC."],
            "Each small grouping has a member list that fits no other group.",
            "India, the USA, Japan and Australia are the four members of which grouping?",
            ["The list has exactly four countries.", "It began in 2007 and was revived in 2017.", "It has no HQ."],
            "QUAD"),
    ],
)

# =====================================================================
SUBS["ca-days"] = dict(
    concept=(
        "Each important day marks a person, an event or a global cause. "
        "Exams ask what the day marks more often than the date itself. "
        "Learn the fixed date and the reason behind it. The yearly theme changes, so note it only for the current year."
    ),
    notes=r"""### Two kinds of day questions
A day question links a date to what it marks. Most national days mark a person's birth or a national event. UN days mark a global cause or a charter.

The date of a day never changes. Its theme changes every year.

> **Example:** 29 August is National Sports Day. It marks the birth of Major Dhyan Chand. The exam asks "whose birth?", not just "which date?".

### Days that honour a person
| Date | Day | Person |
|---|---|---|
| 12 January | National Youth Day | Birth of Swami Vivekananda |
| 1 July | National Doctors' Day | Dr B.C. Roy (birth and death) |
| 29 August | National Sports Day | Major Dhyan Chand |
| 5 September | Teachers' Day | Dr S. Radhakrishnan |
| 31 October | National Unity Day | Birth of Sardar Patel |
| 11 November | National Education Day | Maulana Azad |
| 14 November | Children's Day | Birth of Jawaharlal Nehru |
| 22 December | National Mathematics Day | Srinivasa Ramanujan; since 2012 |
| 25 December | Good Governance Day | Birth of Atal Bihari Vajpayee |

> **Tip:** Read the chain by month: Vivekananda, B.C. Roy, Dhyan Chand, Radhakrishnan, Patel, Nehru, Ramanujan.

### Days that mark an event
| Date | Day | Event |
|---|---|---|
| 28 February | National Science Day | Discovery of the Raman effect (1928) |
| 11 May | National Technology Day | Pokhran tests (11 May 1998) |
| 14 September | Hindi Diwas | Hindi adopted as official language (1949) |
| 26 November | Constitution Day | Constitution adopted (1949); observed since 2015 |

> **Watch:** Constitution Day (26 November) marks adoption in 1949. Republic Day (26 January) marks the Constitution coming into force in 1950.

### The defence trio
- **Army Day, 15 January:** K.M. Cariappa became the first Indian Commander-in-Chief in 1949.
- **Air Force Day, 8 October:** the Indian Air Force was raised in 1932.
- **Navy Day, 4 December:** Operation Trident (1971), the missile attack on Karachi harbour.

The order runs January, October, December.

### UN international days
| Date | Day | Link |
|---|---|---|
| 8 March | International Women's Day | |
| 22 March | World Water Day | |
| 7 April | World Health Day | WHO founded 1948 |
| 22 April | Earth Day | |
| 3 May | World Press Freedom Day | |
| 5 June | World Environment Day | Born of the 1972 Stockholm Conference |
| 21 June | International Day of Yoga | India's proposal |
| 29 July | International Tiger Day | |
| 8 September | International Literacy Day | |
| 2 October | International Day of Non-Violence | Gandhi's birthday |
| 24 October | UN Day | |
| 10 December | Human Rights Day | UDHR adopted 1948 |

Yoga Day is the most asked. The UN declared it in December 2014 on India's proposal. It was first observed in 2015.

### How to study days
1. Learn the **person or event** behind each national day.
2. For UN days, learn the **cause and any Indian link**, such as Yoga Day.
3. Note the **theme** only for days inside your exam window.
4. Anniversaries, like 75 years of the Constitution, fall on these same dates. The fixed date is the anchor.
""",
    tricks=[
        trick("Person-day chain",
              "Go by month: 12 Jan Vivekananda, 1 Jul B.C. Roy, 29 Aug Dhyan Chand, 5 Sep Radhakrishnan, 31 Oct Patel, 14 Nov Nehru, 22 Dec Ramanujan.",
              "National Sports Day honours whom?",
              ["National Sports Day is 29 August.", "In the chain, 29 August is Dhyan Chand.",
               "The national sports awards are given on this day."],
              "Major Dhyan Chand"),
        trick("Services by month",
              "Army comes first in the year (15 January), Air Force next (8 October), Navy last (4 December).",
              "Which service day falls on 4 December?",
              ["4 December is the last of the three dates.", "The last one is the Navy."],
              "Navy Day"),
    ],
    mistakes=[
        mis("Treating Constitution Day and Republic Day as the same.", "Constitution Day (26 Nov) marks adoption in 1949. Republic Day (26 Jan) marks it coming into force in 1950."),
        mis("Linking Teachers' Day to Maulana Azad.", "Teachers' Day (5 Sep) is Radhakrishnan. National Education Day (11 Nov) is Azad."),
        mis("Putting Air Force Day on 4 December.", "4 December is Navy Day. Air Force Day is 8 October."),
        mis("Saying Yoga Day was first observed in 2014.", "The UN declared it in December 2014. It was first observed in 2015."),
        mis("Learning only the dates.", "Learn who or what each day marks. That is what the question asks."),
    ],
    revision=[
        "Youth 12 Jan (Vivekananda), Sports 29 Aug (Dhyan Chand), Teachers 5 Sep (Radhakrishnan).",
        "Unity 31 Oct (Patel), Children 14 Nov (Nehru), Maths 22 Dec (Ramanujan), Good Governance 25 Dec (Vajpayee).",
        "Science 28 Feb (Raman effect), Technology 11 May (Pokhran 1998).",
        "Constitution Day 26 Nov: adopted 1949; observed since 2015.",
        "Army 15 Jan, Air Force 8 Oct, Navy 4 Dec (Operation Trident).",
        "Yoga 21 Jun: India's proposal, UN declared 2014, first observed 2015.",
        "Environment 5 Jun, Health 7 Apr, Non-Violence 2 Oct, UN Day 24 Oct, Human Rights 10 Dec.",
    ],
    patterns=[
        pat("ga-caday-p1", "Day and the person it honours", "very common",
            "'National Sports Day marks whose birth anniversary', 'Teachers' Day commemorates', or a day-person match.",
            ["Identify the day named in the question.",
             "Recall the person from the chain.",
             "Check the date only after you have the person.",
             "Separate Teachers' Day (Radhakrishnan) from Education Day (Azad)."],
            "The exam asks the person, not the date alone.",
            "National Sports Day, observed on 29 August, commemorates the birth anniversary of whom?",
            ["29 August is National Sports Day.", "It honours a hockey legend.", "The sports awards are given on this day."],
            "Major Dhyan Chand"),
        pat("ga-caday-p2", "Day and the event it marks", "very common",
            "'National Science Day marks', 'Constitution Day is observed because', or event-days like Pokhran and Trident.",
            ["Identify the event-day in the question.",
             "Recall the event and its year: Raman effect 1928, Pokhran 1998, Constitution adopted 1949.",
             "For Constitution Day, remember it has been observed since 2015."],
            "Event-days are asked with the event and often its year.",
            "National Science Day, observed on 28 February, marks the discovery of what?",
            ["28 February is National Science Day.", "It marks C.V. Raman's light-scattering discovery of 1928.",
             "This work later won the Nobel Prize."],
            "The Raman effect"),
        pat("ga-caday-p3", "UN international days and Indian links", "very common",
            "'Which day did the UN declare on India's proposal', 'World Environment Day is observed on', or a UN day-date match.",
            ["Start with Yoga Day: 21 June, India's proposal, declared 2014, first observed 2015.",
             "Recall the other pins: Environment 5 Jun, Health 7 Apr, Human Rights 10 Dec.",
             "Link each day to its cause: Stockholm 1972, WHO 1948, UDHR 1948.",
             "Treat the yearly theme as a separate, current-year fact."],
            "Yoga Day is the highest-frequency UN day because of its India link.",
            "The UN declared 21 June as the International Day of Yoga in which year?",
            ["India proposed the day.", "The UN adopted it in December 2014.", "The first Yoga Day was held in 2015."],
            "2014 (December)"),
        pat("ga-caday-p4", "Defence and service days", "common",
            "'Air Force Day is observed on', 'Navy Day commemorates', or the three service days.",
            ["Army Day: 15 January (Cariappa, 1949).",
             "Air Force Day: 8 October (raised 1932).",
             "Navy Day: 4 December (Operation Trident, 1971).",
             "Use the order January, October, December."],
            "Only three dates, and the swap between Air Force and Navy is the usual trick.",
            "Indian Air Force Day is observed on which date?",
            ["Army Day is 15 January.", "Navy Day is 4 December.", "Air Force Day marks the 1932 raising."],
            "8 October"),
        pat("ga-caday-p5", "Look-alike days", "common",
            "Two similar days in one question, e.g. 'Constitution Day differs from Republic Day because', or teacher-linked days.",
            ["Write the two days side by side.",
             "Recall what each one marks.",
             "Constitution Day: adoption, 1949. Republic Day: in force, 1950.",
             "Teachers' Day: Radhakrishnan. Education Day: Azad."],
            "These pairs share a theme, so only the reason behind each date separates them.",
            "Constitution Day (26 November) is observed to mark what?",
            ["Republic Day (26 January) marks the Constitution coming into force in 1950.",
             "Constitution Day marks the earlier step.", "The Constitution was adopted on 26 November 1949."],
            "Adoption of the Constitution in 1949"),
        pat("ga-caday-p6", "Date given, name the day", "common",
            "Only a date is given: 'Which day is observed on 22 December?' or 'What is celebrated on 11 May?'.",
            ["Place the date in the month chain.",
             "Recall the day that sits on it.",
             "Add the person or event to confirm."],
            "Fixed dates make the reverse question as easy as the forward one.",
            "Which day is observed in India on 22 December?",
            ["22 December is the last person-day before Good Governance Day.",
             "It honours Srinivasa Ramanujan.", "It has been observed since 2012."],
            "National Mathematics Day"),
    ],
)

# =====================================================================
SUBS["ca-indexes"] = dict(
    concept=(
        "Index questions mostly ask who publishes an index. Publishers stay the same, while ranks change every edition. "
        "Split the publishers into UN bodies, the World Economic Forum, NGOs and Indian bodies. "
        "The Global Hunger Index comes from two NGOs, not the UN."
    ),
    notes=r"""### The publisher is the question
Most index questions ask which body releases which index. India's rank changes with every edition. The publisher does not.

> **Example:** "Global Hunger Index, released by UNDP" is false. Two NGOs publish it.

So learn the publishers first. Note a rank only for the current edition.

### Indexes from UN bodies
| Index | Publisher | Note |
|---|---|---|
| Human Development Index (HDI) | UNDP | Inside the Human Development Report; health, education, income; since 1990 |
| World Happiness Report | UN Sustainable Development Solutions Network (SDSN) | Released in March |
| Global SDG Index | UN SDSN | Tracks the 17 SDGs |
| Global Innovation Index | WIPO, Geneva | Innovation inputs and outputs |
| World Economic Outlook; Global Financial Stability Report | IMF | Flagship reports |
| Human Capital Index | World Bank | Part of the Human Capital Project |

### World Economic Forum reports
The World Economic Forum (WEF) is known for its Davos meeting. It publishes three reports asked in exams:

- Global Gender Gap Report
- Global Risks Report
- Travel and Tourism Development Index

The WEF has paused its Global Competitiveness Report.

### Indexes from NGOs and other bodies
| Index | Publisher |
|---|---|
| Corruption Perceptions Index | Transparency International, Berlin |
| Global Peace Index | Institute for Economics and Peace (IEP), Sydney |
| Global Hunger Index | Concern Worldwide (Ireland) and Welthungerhilfe (Germany) |
| World Press Freedom Index | Reporters Without Borders (RSF) |
| Henley Passport Index | Henley and Partners |
| World Competitiveness Index | IMD, Lausanne |
| Environmental Performance Index | Yale and Columbia universities |
| Democracy Index; Global Liveability Index | Economist Intelligence Unit (EIU) |

In the Corruption Perceptions Index, a higher score means a cleaner country. The Henley index measures visa-free access. Press Freedom links to World Press Freedom Day on 3 May.

> **Watch:** The Global Hunger Index is the classic trap. Any UN body in the options is wrong.

### India's own indexes
- **NITI Aayog:** SDG India Index, India Innovation Index (with the Institute for Competitiveness), Composite Water Management Index, national Multidimensional Poverty Index.
- **RBI:** Financial Inclusion Index (FI-Index) and its Handbook of Statistics.
- **MoSPI:** CPI, IIP and household consumption surveys.
- **Pratham (an NGO):** ASER, the Annual Status of Education Report, on rural schooling.
- **Department of Economic Affairs:** the Economic Survey.

> **Tip:** SDG India Index is NITI Aayog. The global SDG Index is UN SDSN.

### Indexes that ended or changed
The World Bank **discontinued** its Ease of Doing Business ranking in **2021**, after a review of data irregularities. Its successor is **Business Ready (B-READY)**, first released in **2024**.

A question on a retired index usually asks who stopped it and when.

### How to answer
1. Match the publisher first. Wrong options often name the wrong UN body.
2. Sort the body: UN, WEF, NGO or Indian.
3. Check any rank against the current edition only.
""",
    tricks=[
        trick("UN or NGO",
              "UN bodies: UNDP (HDI), SDSN (Happiness), WIPO (Innovation), IMF (WEO). NGOs: Concern and Welthungerhilfe (Hunger), IEP (Peace), RSF (Press), Pratham (ASER), TI (Corruption).",
              "Who publishes the Global Hunger Index?",
              ["Hunger sits on the NGO side.", "Two NGOs publish it together.", "Any UN body in the options is wrong."],
              "Concern Worldwide and Welthungerhilfe"),
        trick("WEF trio",
              "Gender Gap, Global Risks, Travel and Tourism: three WEF reports. If an option says WEF for one of these, it is right.",
              "The Global Gender Gap Report is released by whom?",
              ["Gender Gap is one of the WEF trio."],
              "World Economic Forum"),
    ],
    mistakes=[
        mis("Giving the Global Hunger Index to a UN body.", "Two NGOs publish it: Concern Worldwide and Welthungerhilfe."),
        mis("Giving the HDI to the World Bank.", "The HDI is UNDP's, inside the Human Development Report."),
        mis("Quoting last year's rank as current.", "Ranks change every edition. Check the current one; publishers do not change."),
        mis("Mixing the SDG India Index with the global SDG Index.", "SDG India Index is NITI Aayog. The global one is UN SDSN."),
        mis("Treating Ease of Doing Business as a live ranking.", "The World Bank stopped it in 2021. B-READY replaced it from 2024."),
        mis("Reading a higher Corruption Perceptions Index score as more corrupt.", "A higher score means cleaner."),
    ],
    revision=[
        "HDI: UNDP. Happiness and global SDG Index: UN SDSN. Innovation: WIPO.",
        "World Economic Outlook: IMF. Human Capital Index: World Bank.",
        "WEF trio: Gender Gap, Global Risks, Travel and Tourism.",
        "Corruption: Transparency International (Berlin). Peace: IEP. Press Freedom: RSF.",
        "Hunger: Concern Worldwide + Welthungerhilfe (NGOs, not UN).",
        "EPI: Yale + Columbia. Competitiveness: IMD. Democracy, Liveability: EIU.",
        "SDG India and India Innovation Index: NITI Aayog. FI-Index: RBI. ASER: Pratham.",
        "Doing Business ended 2021; B-READY from 2024.",
    ],
    patterns=[
        pat("ga-cain-p1", "Index and its UN publisher", "very common",
            "'The Human Development Index is released by', 'which body publishes the Global Innovation Index'.",
            ["Recall the UN pins: HDI UNDP, Happiness SDSN, Innovation WIPO.",
             "Add WEO IMF and Human Capital World Bank.",
             "Reject options that move an index to another UN body.",
             "Remember the HDI appears inside the Human Development Report."],
            "Wrong options usually swap one UN body for another, so exact pairs matter.",
            "The Global Innovation Index is released by which organisation?",
            ["Innovation is linked to intellectual property.", "The UN body for that is WIPO, based in Geneva.",
             "UNDP and the WEF are the usual wrong options."],
            "WIPO (World Intellectual Property Organization)"),
        pat("ga-cain-p2", "Index and its non-UN publisher", "very common",
            "'The Global Hunger Index is released by', 'the Corruption Perceptions Index comes from'.",
            ["Recall Hunger: Concern Worldwide and Welthungerhilfe.",
             "Recall Corruption: Transparency International; Peace: IEP; Press: RSF.",
             "Recall Democracy and Liveability: EIU; EPI: Yale and Columbia; Competitiveness: IMD.",
             "If a UN body appears for an NGO index, reject it."],
            "These bodies are not UN agencies, which is exactly what the options test.",
            "The Global Hunger Index is published by which of the following?",
            ["Hunger is an NGO index.", "Concern Worldwide is from Ireland.", "Welthungerhilfe is from Germany."],
            "Concern Worldwide and Welthungerhilfe"),
        pat("ga-cain-p3", "Indian indexes and their publishers", "common",
            "'The SDG India Index is released by', 'ASER is published by', 'the FI-Index is compiled by'.",
            ["NITI Aayog: SDG India, India Innovation, Water Management, national MPI.",
             "RBI: FI-Index. MoSPI: CPI and IIP.",
             "Pratham: ASER. Department of Economic Affairs: Economic Survey."],
            "Indian indexes come from a short list of bodies, each with its own area.",
            "The SDG India Index is released by which body?",
            ["It ranks states and UTs on the 17 SDGs.", "The global SDG Index is UN SDSN.",
             "The Indian version comes from the government think tank."],
            "NITI Aayog"),
        pat("ga-cain-p4", "Discontinued and replaced indexes", "common",
            "'The Ease of Doing Business index was replaced by', or a statement about a stopped report.",
            ["Doing Business: stopped by the World Bank in 2021.",
             "Its successor: Business Ready (B-READY), first released in 2024.",
             "WEF: Global Competitiveness Report paused.",
             "Check who stopped it and when."],
            "Retired indexes test the publisher and the year.",
            "In which year did the World Bank discontinue its Ease of Doing Business rankings?",
            ["A review found data irregularities.", "The World Bank stopped the ranking.", "B-READY followed from 2024."],
            "2021"),
        pat("ga-cain-p5", "World Economic Forum reports", "common",
            "'The Global Gender Gap Report is released by', 'Global Risks Report is published by'.",
            ["Recall the WEF trio: Gender Gap, Global Risks, Travel and Tourism.",
             "If the index is one of these, choose the WEF.",
             "Do not give Gender Gap to a UN body."],
            "Three reports share one publisher, so one list answers them all.",
            "The Global Risks Report is published by which organisation?",
            ["Global Risks is in the WEF trio.", "The other two are Gender Gap and Travel and Tourism."],
            "World Economic Forum (WEF)"),
        pat("ga-cain-p6", "What an index measures", "occasional",
            "'In the Corruption Perceptions Index, a higher score means', 'the HDI is based on', 'the Henley index ranks'.",
            ["HDI: health, education and income.",
             "Corruption Perceptions Index: higher score means cleaner.",
             "Henley Passport Index: visa-free access.",
             "Global SDG Index and SDG India Index: the 17 SDGs."],
            "A few indexes are asked for what they measure, not who publishes them.",
            "The Human Development Index is built on which three areas?",
            ["UNDP publishes the HDI.", "It combines a long life, learning and living standard.",
             "Those map to health, education and income."],
            "Health, education and income"),
    ],
)
