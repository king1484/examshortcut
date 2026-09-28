"""current-affairs static deep content — part 2: ca-summits, ca-days, ca-indexes."""
import os
import sys

sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
from _lib import Sub


def build_summits():
    S = Sub("ca-summits")
    S.notes = """### What summit questions ask
Four details, every time: **host country/city of the latest summit, the group's membership, its headquarters, and what changed** (a new member, a theme, an outcome). The membership and HQ are permanent; learn them once.

### The groupings to know cold
| Grouping | Founded | HQ | Notes |
|---|---|---|---|
| **G20** | 1999 (finance ministers); leaders' summits from 2008 | No permanent HQ — rotating presidency | 19 countries + the **European Union**; the **African Union joined in 2023** (New Delhi summit) |
| **BRICS** | term coined 2001; first summit **2009** | NDB at Shanghai | Brazil, Russia, India, China, **South Africa (2010)**; expansion approved **2024** (Egypt, Ethiopia, Iran, UAE among entrants) |
| **SCO** | **2001** (from the Shanghai Five) | **Beijing** (RATS at Tashkent) | India and Pakistan full members since **2017**; Belarus joined **2024** |
| **QUAD** | 2007, revived **2017** | — (no HQ) | India, USA, Japan, Australia; leaders'-level since 2021 |
| **ASEAN** | **1967**, Bangkok Declaration | **Jakarta** | Southeast Asia's ten-nation bloc; India is a dialogue partner, not a member |
| **UN** | **1945** | New York | 51 founders; **193 members**; UNSC = **5 permanent (veto) + 10 non-permanent** (2-year terms) |
| **SAARC** | **1985** (first summit Dhaka) | **Kathmandu** | 8 South Asian members; SAFTA from 2006 |
| **BIMSTEC** | **1997** | **Dhaka** | 7 Bay of Bengal littorals: Bangladesh, Bhutan, India, Myanmar, Nepal, Sri Lanka, Thailand |
| **Commonwealth** | London Declaration 1949 (modern form) | **London** (Marlborough House) | **56 member states**; the British Sovereign is its Head |
| **NAM** | **1961 Belgrade** | — | India a founding member |

### India's membership map — a favourite trap set
**Member**: UN, G20, BRICS, SCO, QUAD, SAARC, BIMSTEC, Commonwealth, NAM, IMF/World Bank/WTO, AIIB, ADB.
**Not a member**: **APEC** (the classic trap), ASEAN (dialogue partner only), G7, NATO, OPEC. India led the **G77** (developing-countries caucus at the UN) at times and hosts the **International Solar Alliance** (HQ Gurugram) with France.

### How to note a summit in the window
One line per event: *group — host city/country — theme — what changed*. Themes are quoted in one-liners; membership changes (AU into G20, Belarus into SCO, BRICS expansion) are the second-most asked detail after hosts.

### Quick revision
- G20: 1999/2008; AU joined 2023; rotating presidency, no HQ.
- BRICS: 2009 first summit; NDB Shanghai; 2024 expansion. SCO: 2001, Beijing; India-Pak 2017.
- QUAD = India-US-Japan-Australia (revived 2017). ASEAN 1967 Jakarta; India = dialogue partner.
- UN 1945, 193 members; UNSC 5+10. SAARC 1985 Kathmandu (8). BIMSTEC 1997 Dhaka (7).
- Commonwealth 56, London. NAM 1961 Belgrade.
- India is NOT in APEC, ASEAN, G7, NATO, OPEC."""
    S.pattern("ga-casum-p1", "Summit ↔ host ↔ theme", "very common",
        "'The X summit was hosted by', statements pairing a recent summit with its host city or theme.",
        None,
        "1. For each summit in the window, memorise **group — host city/country — theme** as one line.\n2. Themes quoted in exams are usually slogans (e.g. G20 New Delhi's 'One Earth One Family One Future').\n3. When options swap cities, eliminate by continent logic first — the wrong pair is almost always from a different region.",
        "The **G20 summit hosted by India** (New Delhi, 2023) carried the theme —",
        "'**Vasudhaiva Kutumbakam — One Earth, One Family, One Future**'; the same summit admitted the **African Union** as a permanent member.")
    S.pattern("ga-casum-p2", "Group ↔ membership ↔ headquarters", "very common",
        "'The SCO is headquartered at', 'how many members does BIMSTEC have', matching groups with HQ and member counts.",
        None,
        "1. HQ pins: SCO — **Beijing**; SAARC — **Kathmandu**; BIMSTEC — **Dhaka**; ASEAN — **Jakarta**; NDB (BRICS) — **Shanghai**; Commonwealth — **London**.\n2. Counts: SAARC **8**; BIMSTEC **7**; UN **193**; Commonwealth **56**; UNSC **5 permanent + 10 non-permanent**.\n3. India-led or India-hosted bodies: International Solar Alliance — **Gurugram**.",
        "The headquarters of the **Shanghai Cooperation Organisation** is at —",
        "**Beijing** — the anti-terror arm (RATS) sits at Tashkent; India and Pakistan became full members in 2017.")
    S.pattern("ga-casum-p3", "India's membership map (in / out)", "common",
        "'India is NOT a member of', statements placing India inside or outside a grouping — APEC and ASEAN are the classic traps.",
        None,
        "1. **In**: UN, G20, BRICS, SCO, QUAD, SAARC, BIMSTEC, Commonwealth, NAM, AIIB, ADB.\n2. **Out**: **APEC** (the evergreen trap), **ASEAN** (dialogue partner only), G7, NATO, OPEC.\n3. Founding credits: India co-founded **NAM, G77 work, SAARC-era bodies and the International Solar Alliance** (with France).",
        "India is **not** a member of which grouping?",
        "**APEC** (Asia-Pacific Economic Cooperation) — despite bordering the Pacific's trade flows, India sits outside it; ASEAN membership is also absent (dialogue partner only).")
    S.pattern("ga-casum-p4", "Groupings: founding years and expansions", "common",
        "'BRICS expansion happened in', 'when did India join the SCO', ordering groups by founding year, new-member questions.",
        None,
        "1. Years: UN 1945, NAM 1961, ASEAN 1967, SAARC 1985, G20 1999, SCO 2001, BIMSTEC 1997, first BRICS summit 2009.\n2. Expansions: AU into G20 (**2023**); BRICS expansion (**2024**); Belarus into SCO (**2024**); India-Pakistan into SCO (**2017**).\n3. Match the change to the group before checking other statements.",
        "India and Pakistan became **full members of the SCO** in —",
        "**2017** — the SCO (founded 2001) admitted both together; Belarus followed as a full member in 2024.")
    S.pattern("ga-casum-p5", "UN structure and India's UN track", "common",
        "'How many members does the UN have', 'UNSC non-permanent members serve for', how many times India has been an elected UNSC member.",
        None,
        "1. UN: founded **1945**, **193 members**, HQ New York; principal judicial organ **ICJ at The Hague**.\n2. **UNSC**: 15 members — 5 permanent with veto (US, UK, France, Russia, China) + 10 non-permanent for **two-year** terms.\n3. India has been elected a **non-permanent UNSC member eight times** (latest term 2021-22) and has long pressed for permanent reform.",
        "Non-permanent members of the **UN Security Council** are elected for a term of —",
        "**Two years** — ten of the Council's fifteen seats rotate; the five permanent members hold vetoes.")

    S.q("ga-casum-p1", "easy", "The **African Union** joined the G20 as a permanent member at the —",
        ["Rome summit", "New Delhi summit (2023)", "Bali summit", "Hangzhou summit"], "New Delhi summit (2023)",
        "At the **New Delhi G20 (2023)** the AU became the second regional bloc (after the EU) with permanent membership.",
        "Delhi 2023 = AU in.", 20)
    S.q("ga-casum-p1", "medium", "**QUAD** consists of —",
        ["India, China, Russia, Brazil", "India, USA, Japan, Australia", "India, France, UAE, Israel", "USA, UK, France, Germany"], "India, USA, Japan, Australia",
        "The Quadrilateral Security Dialogue groups **India, the USA, Japan and Australia** — revived in 2017, leaders'-level since 2021.",
        "Quad = IN-US-JP-AU.", 20)
    S.q("ga-casum-p1", "medium", "**BRICS expansion**, adding members such as Egypt, Ethiopia, Iran and the UAE, took effect in —",
        ["2010", "2017", "2021", "2024"], "2024",
        "The bloc expanded from January **2024**; South Africa had joined the original BRIC in 2010, and India-Pakistan entered the SCO in 2017 — don't mix the years.",
        "BRICS+ = 2024.", 25)
    S.q("ga-casum-p2", "easy", "The headquarters of **SAARC** is at —",
        ["New Delhi", "Dhaka", "Kathmandu", "Islamabad"], "Kathmandu",
        "**Kathmandu** hosts SAARC (founded 1985, first summit at Dhaka); BIMSTEC sits at **Dhaka** — don't swap them.",
        "SAARC = Kathmandu.", 20)
    S.q("ga-casum-p2", "medium", "**BIMSTEC** groups how many member states?",
        ["Five", "Seven", "Eight", "Ten"], "Seven",
        "**Seven** Bay of Bengal littorals — Bangladesh, Bhutan, India, Myanmar, Nepal, Sri Lanka, Thailand; HQ at **Dhaka**.",
        "BIMSTEC = 7.", 25)
    S.q("ga-casum-p2", "medium", "The **ASEAN** secretariat is located at —",
        ["Bangkok", "Jakarta", "Manila", "Singapore"], "Jakarta",
        "ASEAN (Bangkok Declaration, **1967**) works from **Jakarta**; India is a dialogue partner, not a member.",
        "ASEAN = Jakarta.", 25)
    S.q("ga-casum-p2", "hard", "Match: 1. SCO 2. SAARC 3. BIMSTEC — with (i) Kathmandu (ii) Beijing (iii) Dhaka:",
        ["1-ii, 2-i, 3-iii", "1-iii, 2-ii, 3-i", "1-i, 2-iii, 3-ii", "1-ii, 2-iii, 3-i"], "1-ii, 2-i, 3-iii",
        "SCO → **Beijing**; SAARC → **Kathmandu**; BIMSTEC → **Dhaka** — the three HQs exams swap most often.",
        "Beijing, Kathmandu, Dhaka.", 30)
    S.q("ga-casum-p3", "easy", "India is **not** a member of —",
        ["BRICS", "SCO", "APEC", "BIMSTEC"], "APEC",
        "**APEC** is the classic trap — India is outside it, though it belongs to BRICS, SCO and BIMSTEC.",
        "APEC = the trap.", 20)
    S.q("ga-casum-p3", "medium", "Regarding **ASEAN**, India is —",
        ["A founding member", "A full member since 1992", "A sectoral dialogue partner, not a member", "An observer with veto"], "A sectoral dialogue partner, not a member",
        "India partners ASEAN at summit level but is **not** one of its Southeast Asian members — a fixed distinction in every grouping question.",
        "Partner, never member.", 25)
    S.q("ga-casum-p3", "hard", "Consider the statements:\n1. The Commonwealth has 56 member states.\n2. India is a member of both SAARC and BIMSTEC.\n3. India is a member of the G7.\nWhich are correct?",
        ["1 and 2 only", "1 and 3 only", "2 and 3 only", "1, 2 and 3"], "1 and 2 only",
        "Statements 1 and 2 are correct. Statement 3 is wrong — the **G7 excludes India** (US, UK, France, Germany, Italy, Japan, Canada).",
        "G7 has no India seat.", 30)
    S.q("ga-casum-p4", "easy", "The **Shanghai Cooperation Organisation** was founded in —",
        ["1996", "2001", "2009", "2017"], "2001",
        "The SCO took its present form in **2001** from the earlier Shanghai Five; India and Pakistan joined as full members in 2017.",
        "SCO = 2001.", 20)
    S.q("ga-casum-p4", "medium", "The **first BRICS summit** was held in —",
        ["2001 at Yekaterinburg", "2009 at Yekaterinburg", "2010 at Brasilia", "2015 at Shanghai"], "2009 at Yekaterinburg",
        "The acronym ('BRIC') was coined in 2001, but the **first summit came in 2009 at Yekaterinburg**; South Africa joined in 2010.",
        "2009 = first summit.", 25)
    S.q("ga-casum-p4", "medium", "Arrange by founding year (earliest first):\n1. ASEAN 2. SAARC 3. G20",
        ["1, 2, 3", "2, 1, 3", "3, 1, 2", "1, 3, 2"], "1, 2, 3",
        "ASEAN **1967** → SAARC **1985** → G20 **1999** (leaders' summits from 2008).",
        "1967 → 1985 → 1999.", 30)
    S.q("ga-casum-p5", "easy", "The **United Nations** currently has —",
        ["191 member states", "193 member states", "195 member states", "197 member states"], "193 member states",
        "**193 members** since South Sudan joined in 2011; 51 states founded the UN in 1945.",
        "UN = 193.", 20)
    S.q("ga-casum-p5", "medium", "How many times has India been elected a **non-permanent member** of the UNSC?",
        ["Five", "Six", "Seven", "Eight"], "Eight",
        "**Eight terms** — most recently 2021-22; India campaigns for a permanent seat in the reformed Council.",
        "Eight terms, latest 2021-22.", 25)
    S.q("ga-casum-p5", "hard", "Consider the statements about the UN:\n1. It was founded in 1945 with 51 members.\n2. The ICJ is its principal judicial organ, seated at The Hague.\n3. The UNSC's five permanent members are elected every two years.\nWhich are correct?",
        ["1 and 2 only", "1 and 3 only", "2 and 3 only", "1, 2 and 3"], "1 and 2 only",
        "Statements 1 and 2 are correct. Statement 3 is wrong — the **P-5 are permanent** (with veto); only the ten non-permanent seats face election, for two-year terms.",
        "Permanent means permanent.", 30)
    return S


def build_days():
    S = Sub("ca-days")
    S.notes = """### The day ↔ purpose ↔ person framework
Important-day questions come in two stable shapes: **day ↔ what it commemorates** (person, event, charter) and **day ↔ theme of the year** (the theme changes annually — quote only if asked in-window; the day itself never changes). National days usually commemorate a person's birth or a national event; UN days mark charters, conventions and global causes.

### National days — the permanent dozen
| Day | Commemorates |
|---|---|
| **12 January** — National Youth Day | Birth of **Swami Vivekananda** |
| **15 January** — Army Day | **K.M. Cariappa** became first Indian Commander-in-Chief (1949) |
| **28 February** — National Science Day | **Raman effect** discovery (1928) |
| **11 May** — National Technology Day | **Pokhran tests** (11 May 1998) |
| **1 July** — National Doctors' Day | Dr. **B.C. Roy** (birth & death) |
| **29 August** — National Sports Day | **Major Dhyan Chand** |
| **5 September** — Teachers' Day | Dr. **S. Radhakrishnan** |
| **14 September** — Hindi Diwas | Hindi adopted as official language (1949) |
| **31 October** — National Unity Day | Birth of **Sardar Patel** |
| **14 November** — Children's Day | Birth of **Jawaharlal Nehru** |
| **26 November** — Constitution Day | Constitution adopted (1949); observed since **2015** |
| **4 December** — Navy Day | **Operation Trident** (1971) |
| **22 December** — National Mathematics Day | **Srinivasa Ramanujan**; since **2012** |
| **25 December** — Good Governance Day | Birth of **Atal Bihari Vajpayee** |

Defence triple: Army 15 Jan, Air Force **8 October**, Navy 4 December.

### UN international days — the high-frequency set
- **8 March** Women's Day; **22 March** World Water Day; **7 April** World Health Day (WHO founded 1948); **22 April** Earth Day; **3 May** World Press Freedom Day; **5 June** World Environment Day (from the 1972 Stockholm Conference); **21 June** **International Day of Yoga** (UN-declared in 2014 on India's proposal, first observed 2015); **29 July** International Tiger Day; **8 September** International Literacy Day; **2 October** International Day of Non-Violence (Gandhi's birthday); **24 October** UN Day; **10 December** Human Rights Day (UDHR adopted 1948).

### The working method
1. Memorise the **person or event** behind each national day — the exam asks 'National Sports Day marks whose birth anniversary', never the date alone.
2. For UN days, learn the **cause and the Indian connection** (Yoga proposed by India; Environment Day born of Stockholm 1972).
3. Note each year's **theme** for days inside the exam window — themes appear as fill-in-the-blank one-liners.
4. Anniversaries (e.g. '75 years of the Constitution') ride on these same dates — the static date is the anchor.

### Quick revision
- Person-days: Youth 12 Jan (Vivekananda), Sports 29 Aug (Dhyan Chand), Teachers 5 Sep (Radhakrishnan), Unity 31 Oct (Patel), Children 14 Nov (Nehru), Maths 22 Dec (Ramanujan).
- Event-days: Science 28 Feb (Raman effect), Technology 11 May (Pokhran 1998), Navy 4 Dec (Trident), Constitution 26 Nov (adopted 1949).
- Defence: Army 15 Jan, Air Force 8 Oct, Navy 4 Dec.
- UN set: Yoga 21 Jun (India's proposal), Environment 5 Jun, Health 7 Apr, HR 10 Dec, Non-Violence 2 Oct, UN Day 24 Oct."""
    S.pattern("ga-caday-p1", "Day ↔ person commemorated", "very common",
        "'National Sports Day marks whose birth anniversary', 'Teachers' Day commemorates', matching person-days with names.",
        None,
        "1. Person-days: Vivekananda 12 Jan; B.C. Roy 1 Jul; Dhyan Chand 29 Aug; Radhakrishnan 5 Sep; Patel 31 Oct; Nehru 14 Nov; Ramanujan 22 Dec; Vajpayee 25 Dec.\n2. The exam asks the **person**, not the date — recall who, then check the date.\n3. Two teacher-linked days: Teachers' Day (Radhakrishnan) vs Education Day 11 Nov (**Maulana Azad**).",
        "**National Sports Day** (29 August) commemorates —",
        "Major **Dhyan Chand**, the hockey legend — his birth anniversary; the sports awards are conferred on this day.")
    S.pattern("ga-caday-p2", "Day ↔ event commemorated", "very common",
        "'National Science Day marks', 'Constitution Day is observed because', event-days: Raman effect, Pokhran, Trident, adoption of the Constitution.",
        None,
        "1. Event-days: Science 28 Feb (**Raman effect, 1928**); Technology 11 May (**Pokhran, 1998**); Navy 4 Dec (**Operation Trident, 1971**); Constitution 26 Nov (**adoption, 1949**); Hindi 14 Sep (**official-language resolution, 1949**).\n2. Constitution Day has been observed since **2015** — often asked with its year.\n3. Army Day links to **Cariappa (1949)** — a person-event hybrid.",
        "**National Science Day** (28 February) marks the discovery of —",
        "The **Raman effect** (1928) — C.V. Raman's light-scattering work that later won the Nobel Prize.")
    S.pattern("ga-caday-p3", "UN international days and Indian links", "very common",
        "'Which day did the UN declare on India's proposal', 'World Environment Day is', matching UN days with causes and dates.",
        None,
        "1. **Yoga — 21 June**: proposed by India, UN-declared **2014**, first observed **2015** — the highest-frequency UN day.\n2. Other pins: Environment 5 Jun (Stockholm 1972 origin), Health 7 Apr (WHO, 1948), HR 10 Dec (UDHR, 1948), Non-Violence 2 Oct (Gandhi), UN Day 24 Oct, Press Freedom 3 May.\n3. The annual **theme** is the second layer — quote it only within the window.",
        "The **International Day of Yoga** (21 June) was declared by the UN in —",
        "**December 2014**, on **India's proposal** — first observed worldwide on 21 June **2015**.")
    S.pattern("ga-caday-p4", "Defence and service days", "common",
        "'Air Force Day is observed on', 'Navy Day commemorates', the three service days and their events.",
        None,
        "1. Army — **15 January** (Cariappa, 1949); Air Force — **8 October** (its 1932 raising); Navy — **4 December** (Operation Trident, 1971).\n2. Ordering hook: January → October → December.\n3. Navy Day's Trident was the 1971 missile attack on Karachi harbour — the event asked alongside the date.",
        "**Indian Air Force Day** is observed on —",
        "**8 October** — marking the IAF's raising in 1932; Army Day (15 January) and Navy Day (4 December) complete the trio.")

    S.q("ga-caday-p1", "easy", "**National Youth Day** (12 January) marks the birth anniversary of —",
        ["Swami Vivekananda", "Sardar Patel", "B.R. Ambedkar", "Subhas Chandra Bose"], "Swami Vivekananda",
        "**Swami Vivekananda**, born 12 January 1863 — the day anchors the National Youth Festival.",
        "Youth = Vivekananda.", 20)
    S.q("ga-caday-p1", "easy", "**National Unity Day** (31 October) commemorates —",
        ["Jawaharlal Nehru", "Sardar Vallabhbhai Patel", "Lal Bahadur Shastri", "Bhagat Singh"], "Sardar Vallabhbhai Patel",
        "The **Iron Man's** birth anniversary (31 October 1875) — Rashtriya Ekta Diwas, observed since 2014.",
        "Unity = Patel.", 20)
    S.q("ga-caday-p1", "medium", "**National Education Day** (11 November) honours —",
        ["Dr. S. Radhakrishnan", "Maulana Abul Kalam Azad", "Dr. B.R. Ambedkar", "Madan Mohan Malaviya"], "Maulana Abul Kalam Azad",
        "**Maulana Azad**, independent India's first Education Minister, born 11 November 1888 — don't confuse with Teachers' Day (5 September, Radhakrishnan).",
        "Education Day = Azad.", 25)
    S.q("ga-caday-p1", "medium", "**National Mathematics Day** (22 December) marks the birth of —",
        ["Aryabhata", "Srinivasa Ramanujan", "Bhaskara", "C.V. Raman"], "Srinivasa Ramanujan",
        "**Ramanujan** (born 22 December 1887); the day has been observed since **2012**, his 125th birth-anniversary year.",
        "Maths = Ramanujan, since 2012.", 25)
    S.q("ga-caday-p1", "hard", "Arrange by date within the year:\n1. Teachers' Day 2. Children's Day 3. National Sports Day",
        ["3, 1, 2", "1, 2, 3", "2, 3, 1", "3, 2, 1"], "3, 1, 2",
        "Sports Day **29 August** → Teachers' Day **5 September** → Children's Day **14 November**.",
        "Aug, Sep, Nov.", 30)
    S.q("ga-caday-p2", "easy", "**National Technology Day** (11 May) commemorates —",
        ["The first computer in India", "The Pokhran nuclear tests of 1998", "ISRO's founding", "The Green Revolution"], "The Pokhran nuclear tests of 1998",
        "The **Pokhran-II tests of 11 May 1998**; ISRO-related milestones are marked separately, not on this day.",
        "11 May = Pokhran.", 20)
    S.q("ga-caday-p2", "medium", "**Constitution Day** (26 November) has been observed since —",
        ["1949", "1950", "2015", "2019"], "2015",
        "The Constitution was **adopted on 26 November 1949** and came into force on 26 January 1950; the observance began in **2015** (the 125th birth-anniversary year of Ambedkar).",
        "Adopted '49, observed since 2015.", 25)
    S.q("ga-caday-p2", "medium", "**Navy Day** (4 December) commemorates —",
        ["Operation Vijay", "Operation Trident", "Operation Meghdoot", "Operation Blue Star"], "Operation Trident",
        "**Operation Trident** — the 1971 missile attack on Karachi harbour; the other operations belong to different services and years.",
        "Trident = Navy Day.", 25)
    S.q("ga-caday-p2", "hard", "Consider the statements:\n1. National Science Day marks the Raman effect (1928).\n2. Army Day is observed on 15 January.\n3. Hindi Diwas marks the adoption of Hindi as official language in 1949.\nWhich are correct?",
        ["1, 2 and 3", "1 and 2 only", "2 and 3 only", "1 and 3 only"], "1, 2 and 3",
        "All three are settled: 28 February (Raman 1928), 15 January (Cariappa 1949), 14 September (1949 resolution).",
        "Raman, Cariappa, 1949 — all true.", 30)
    S.q("ga-caday-p3", "easy", "The **International Day of Yoga** (21 June) was first observed in —",
        ["2014", "2015", "2016", "2017"], "2015",
        "The UN declared it in **December 2014** on India's proposal; the first global Yoga Day fell on **21 June 2015**.",
        "Declared '14, first '15.", 20)
    S.q("ga-caday-p3", "medium", "**World Environment Day** (5 June) traces its origin to —",
        ["The Paris Agreement", "The 1972 Stockholm Conference", "The Rio Earth Summit", "The Kyoto Protocol"], "The 1972 Stockholm Conference",
        "The UN Conference on the Human Environment at **Stockholm (1972)** both created UNEP and gave the day its start; Rio (1992) came later.",
        "Stockholm 1972.", 25)
    S.q("ga-caday-p3", "medium", "**Human Rights Day** (10 December) marks the adoption of —",
        ["The UN Charter", "The Universal Declaration of Human Rights", "The Geneva Conventions", "The ICC statute"], "The Universal Declaration of Human Rights",
        "The **UDHR, adopted 10 December 1948** — the UN Charter (1945) and Geneva Conventions are separate instruments.",
        "UDHR = 10-12-1948.", 25)
    S.q("ga-caday-p4", "easy", "**Indian Air Force Day** is observed on —",
        ["15 January", "8 October", "4 December", "16 December"], "8 October",
        "**8 October** — the IAF was raised in 1932; 16 December marks Vijay Diwas (1971 victory).",
        "IAF = 8 October.", 20)
    S.q("ga-caday-p4", "medium", "Match the service day: 1. Army 2. Air Force 3. Navy — with (i) 8 October (ii) 4 December (iii) 15 January:",
        ["1-iii, 2-i, 3-ii", "1-i, 2-ii, 3-iii", "1-ii, 2-i, 3-iii", "1-iii, 2-ii, 3-i"], "1-iii, 2-i, 3-ii",
        "Army **15 January** → Air Force **8 October** → Navy **4 December** — chronology makes the trio easy to hold.",
        "Jan, Oct, Dec.", 25)
    S.q("ga-caday-p4", "medium", "**Army Day** (15 January) recalls —",
        ["The raising of the Indian Army", "K.M. Cariappa becoming the first Indian Commander-in-Chief", "The 1965 war's beginning", "The Kargil victory"], "K.M. Cariappa becoming the first Indian Commander-in-Chief",
        "On **15 January 1949** **K.M. Cariappa** took over as the first Indian Commander-in-Chief of the Army.",
        "Cariappa, 1949.", 25)
    return S


def build_indexes():
    S = Sub("ca-indexes")
    S.notes = """### The index ↔ publisher grid — the whole subtopic
Index questions overwhelmingly ask **who releases which index**. Learn the publisher columns; ranks change every edition, publishers never do.

| Index | Publisher | Note |
|---|---|---|
| **Human Development Index (HDI)** | **UNDP** (Human Development Report) | Health + education + income; since 1990 |
| World Happiness Report | UN Sustainable Development Solutions Network (SDSN) | March releases |
| Global SDG Index | UN SDSN | Tracks the 17 SDGs |
| **Global Innovation Index** | **WIPO** (Geneva) | Innovation inputs/outputs |
| World Economic Outlook; Global Financial Stability Report | **IMF** | Flagship macro reports |
| Human Capital Index | **World Bank** | Part of the Human Capital Project |
| **Global Gender Gap Report**; Global Risks Report; Travel & Tourism Development Index | **World Economic Forum** (Davos) | WEF's trio |
| **Corruption Perceptions Index** | **Transparency International** (Berlin) | Higher score = cleaner |
| **Global Peace Index** | Institute for Economics & Peace (Sydney) | — |
| **Global Hunger Index** | **Concern Worldwide + Welthungerhilfe** | Two NGOs — not a UN body (classic trap) |
| Henley Passport Index | Henley & Partners | Visa-free access |
| World Competitiveness Index | **IMD** (Lausanne) | — |
| Environmental Performance Index | **Yale + Columbia** universities | Biennial-ish |
| Democracy Index; Global Liveability Index | EIU (Economist Intelligence Unit) | — |
| World Press Freedom Index | **Reporters Without Borders** (RSF) | 3 May links to Press Freedom Day |
| Ease of Doing Business | **DISCONTINUED by the World Bank (2021)** | Replaced by **Business Ready (B-READY)** from 2024 |

### India's own indexes and reports
- **NITI Aayog**: **SDG India Index**, **India Innovation Index** (with Institute for Competitiveness), Composite Water Management Index, Multidimensional Poverty Index (national).
- **RBI**: Financial Inclusion Index (FI-Index), and its Handbook of Statistics.
- **MoSPI**: CPI, IIP and the household-consumption surveys (the official statistical base).
- **ASER** (Annual Status of Education Report) — by the NGO **Pratham**, on rural schooling.
- **EF-PII**-style environment reports and the Economic Survey (DEA) round out the domestic set.

### How to answer
1. Match the **publisher first** — three options usually die on a wrong UN family member (e.g. 'Global Hunger Index — UNDP' is false).
2. Know the **UN family vs NGOs** split: UNDP/UNSDSN/WHO/FAO/UNEP/UNICEF are UN bodies; Transparency International, IEP, Concern Worldwide, Pratham, RSF are not.
3. Note **India's rank only within the window** — it changes with each edition; the pairing is permanent.
4. Discontinued and renamed lists matter: Doing Business → **B-READY**; Global Competitiveness paused by WEF.

### Quick revision
- UN bodies: HDI — UNDP; Happiness & SDG — UN SDSN; WEO — IMF; Human Capital — World Bank; Innovation — WIPO.
- WEF trio: Gender Gap, Global Risks, Travel & Tourism. CPI (corruption) — Transparency International, Berlin.
- NGOs: Hunger — Concern + Welthungerhilfe; Peace — IEP; Press Freedom — RSF; ASER — Pratham; EPI — Yale/Columbia; IMD — competitiveness.
- India: SDG India & Innovation indexes — NITI Aayog; FI-Index — RBI; ASER — Pratham.
- Doing Business (World Bank) discontinued 2021 → B-READY."""
    S.pattern("ga-cain-p1", "Index ↔ UN-family publisher", "very common",
        "'The Human Development Index is released by', 'which body publishes the Global Innovation Index', matching indexes with UN organisations.",
        None,
        "1. UN-family pins: **HDI — UNDP**; **Happiness — UN SDSN**; **Innovation — WIPO**; WEO — IMF; Human Capital — World Bank.\n2. Don't migrate publishers inside the UN family — 'HDI by UNESCO' or 'Innovation by UNDP' are the planted errors.\n3. The HDI rides inside the **Human Development Report** — often asked together.",
        "The **Global Innovation Index** is released by —",
        "**WIPO** (World Intellectual Property Organization), Geneva — not UNDP or the WEF.")
    S.pattern("ga-cain-p2", "Index ↔ non-UN publishers (NGOs, think tanks)", "very common",
        "'The Global Hunger Index is released by', 'the Corruption Perceptions Index comes from', matching NGO/think-tank indexes.",
        None,
        "1. **Global Hunger Index — Concern Worldwide + Welthungerhilfe** (two NGOs, not UN — the classic trap).\n2. **Corruption Perceptions Index — Transparency International** (Berlin); **Global Peace Index — IEP**; **Press Freedom — RSF**; **Democracy/Liveability — EIU**; **EPI — Yale + Columbia**; **Competitiveness — IMD**.\n3. WEF's own trio: Gender Gap, Global Risks, Travel & Tourism.",
        "The **Global Hunger Index** is published by —",
        "**Concern Worldwide (Ireland) and Welthungerhilfe (Germany)** — two NGOs; any option naming UNDP/FAO/WHO is wrong.")
    S.pattern("ga-cain-p3", "India-specific indexes and their publishers", "common",
        "'The SDG India Index is released by', 'ASER is published by', 'the FI-Index belongs to', matching Indian indexes.",
        None,
        "1. **NITI Aayog**: SDG India Index, India Innovation Index, Composite Water Index, national MPI.\n2. **RBI**: Financial Inclusion (FI) Index; **MoSPI**: CPI/IIP base data.\n3. **ASER — Pratham** (NGO) on rural learning levels; Economic Survey — Department of Economic Affairs.",
        "The **SDG India Index** is released by —",
        "**NITI Aayog** — tracking states and UTs on the 17 SDGs; the *global* SDG index, by contrast, comes from the UN SDSN.")
    S.pattern("ga-cain-p4", "Discontinued, renamed and replaced indexes", "common",
        "'The Ease of Doing Business index was replaced by', statements noting a discontinued index or a new publisher.",
        None,
        "1. **Ease of Doing Business — discontinued by the World Bank in 2021**; its successor is **Business Ready (B-READY)**, first edition **2024**.\n2. WEF paused its Global Competitiveness Report; older indexes survive in past editions only.\n3. When a question cites a discontinued index, the answer usually turns on **who discontinued it and when**.",
        "The World Bank **discontinued its Ease of Doing Business rankings** in —",
        "**2021**, replacing the series with **Business Ready (B-READY)** from 2024 after a data-irregularity review.")

    S.q("ga-cain-p1", "easy", "The **Human Development Index (HDI)** is released in the —",
        ["World Development Report", "Human Development Report", "Global Risks Report", "World Economic Outlook"], "Human Development Report",
        "The **UNDP's Human Development Report** carries the HDI — health, education and income combined; the WDR belongs to the World Bank and the WEO to the IMF.",
        "HDI lives in the HDR.", 20)
    S.q("ga-cain-p1", "medium", "The **Global Innovation Index** is published by —",
        ["UNDP", "WIPO", "The World Bank", "The World Economic Forum"], "WIPO",
        "**WIPO**, the World Intellectual Property Organization at Geneva, publishes the GII.",
        "Innovation = WIPO.", 20)
    S.q("ga-cain-p1", "medium", "The **World Happiness Report** is published by —",
        ["The United Nations SDSN", "The World Bank", "IMF", "The WHO"], "The United Nations SDSN",
        "The **UN Sustainable Development Solutions Network** issues the report each March — not the WHO or the World Bank.",
        "Happiness = SDSN.", 25)
    S.q("ga-cain-p1", "hard", "Match: 1. HDI 2. World Economic Outlook 3. Global Innovation Index — with (i) IMF (ii) UNDP (iii) WIPO:",
        ["1-ii, 2-i, 3-iii", "1-i, 2-ii, 3-iii", "1-ii, 2-iii, 3-i", "1-iii, 2-i, 3-ii"], "1-ii, 2-i, 3-iii",
        "HDI → **UNDP**; WEO → **IMF**; GII → **WIPO** — the standard UN-family triple.",
        "UNDP, IMF, WIPO.", 30)
    S.q("ga-cain-p2", "easy", "The **Corruption Perceptions Index** is released by —",
        ["The World Bank", "Transparency International", "UNDP", "The WEF"], "Transparency International",
        "**Transparency International (Berlin)** publishes the CPI — higher score means a cleaner public sector.",
        "Corruption = TI, Berlin.", 20)
    S.q("ga-cain-p2", "medium", "The **Global Peace Index** is released by —",
        ["The United Nations", "Institute for Economics & Peace", "Interpol", "The World Bank"], "Institute for Economics & Peace",
        "The Sydney-based **IEP**, a think tank — not a UN body; it also issues the Positive Peace report.",
        "Peace = IEP, Sydney.", 25)
    S.q("ga-cain-p2", "medium", "The **World Press Freedom Index** is compiled by —",
        ["UNESCO", "Reporters Without Borders", "The UN General Assembly", "The International Press Institute"], "Reporters Without Borders",
        "**RSF** publishes the annual index each **3 May** — World Press Freedom Day — while UNESCO runs the related prize and day.",
        "Press freedom = RSF.", 25)
    S.q("ga-cain-p2", "hard", "Which pairing is **wrong**?",
        ["Global Gender Gap — WEF", "Environmental Performance Index — Yale and Columbia", "Global Hunger Index — UNDP", "World Competitiveness — IMD"], "Global Hunger Index — UNDP",
        "The **Global Hunger Index belongs to Concern Worldwide + Welthungerhilfe**, not UNDP — all other pairs are correct.",
        "Hunger is NGO-published.", 30)
    S.q("ga-cain-p3", "easy", "The **SDG India Index** is released by —",
        ["The Ministry of Statistics", "NITI Aayog", "The RBI", "The Finance Commission"], "NITI Aayog",
        "**NITI Aayog** tracks states and UTs on the SDGs; MoSPI handles official statistical series instead.",
        "SDG India = NITI.", 20)
    S.q("ga-cain-p3", "medium", "The **Annual Status of Education Report (ASER)** is published by —",
        ["The HRD Ministry", "NCERT", "The NGO Pratham", "NITI Aayog"], "The NGO Pratham",
        "**Pratham**, an NGO, surveys rural children's reading and arithmetic each year — an outside-the-government report exams quote often.",
        "ASER = Pratham.", 25)
    S.q("ga-cain-p3", "medium", "The **Financial Inclusion Index (FI-Index)** is released by —",
        ["SEBI", "The RBI", "NABARD", "The Finance Ministry"], "The RBI",
        "The **RBI's** FI-Index tracks banking, credit and insurance penetration in one number.",
        "FI-Index = RBI.", 25)
    S.q("ga-cain-p4", "easy", "The World Bank's **Ease of Doing Business** rankings were discontinued in —",
        ["2018", "2019", "2021", "2023"], "2021",
        "Discontinued in **2021** after a data review; the successor series **Business Ready (B-READY)** began in 2024.",
        "Died 2021 → B-READY.", 20)
    S.q("ga-cain-p4", "medium", "The successor to the discontinued **Doing Business** rankings is —",
        ["B-READY", "Global Competitiveness Index", "Human Capital Index", "Governance Index"], "B-READY",
        "**Business Ready (B-READY)**, first released in **2024** by the World Bank, replaced Doing Business.",
        "B-READY = the heir.", 25)
    S.q("ga-cain-p4", "hard", "Consider the statements:\n1. The WEF publishes the Global Gender Gap Report.\n2. The HDI is published by the World Bank.\n3. The India Innovation Index is a NITI Aayog product.\nWhich are correct?",
        ["1 and 3 only", "1 and 2 only", "2 and 3 only", "1, 2 and 3"], "1 and 3 only",
        "Statements 1 and 3 are correct. Statement 2 is wrong — the **HDI belongs to the UNDP**, not the World Bank.",
        "WEF gender gap; UNDP HDI; NITI innovation.", 30)
    return S
