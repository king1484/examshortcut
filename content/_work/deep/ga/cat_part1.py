"""current-affairs static deep content — part 1: ca-strategy, ca-awards, ca-sports."""
import os
import sys

sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
from _lib import Sub


def build_strategy():
    S = Sub("ca-strategy")
    S.notes = """### How current-affairs questions are actually framed
CA questions rarely ask for a whole news story — they convert one news fact into one of four frames:
1. **Direct recall** — 'X won the Y award', 'who holds office Z', 'the summit was hosted by' — one fact, four options.
2. **Match-the-column** — pairs like award ↔ field, day ↔ theme, summit ↔ host, index ↔ publisher; one wrong letter kills the option.
3. **Statement-based** — 2-3 numbered statements mix one wrong detail (wrong year, wrong ministry, wrong city) into two correct ones.
4. **CA-to-static bridge** — news as a doorway to permanent facts: a Nobel announcement revisits Nobel's categories; a summit revisits the group's membership and HQ; a new scheme revisits its ministry.

### The ten recurring buckets to track every month
1. **Appointments and offices** (President, Governors, CJI, chiefs, regulators, international heads).
2. **Awards and honours** (national: Bharat Ratna, Padma, gallantry; international: Nobel, Magsaysay, Booker).
3. **Sports** — winners, hosts, tournaments, records.
4. **Summits and conferences** — host country, theme, outcomes.
5. **Schemes and launches** — new schemes, portal/mission launches, extensions.
6. **Defence exercises and deals** — exercise names (India ↔ partner), missiles, induction.
7. **Space missions** — ISRO launches, landings, satellites.
8. **Indexes and reports** — India's rank and the publisher.
9. **Important days and themes** — especially UN days and their annual themes.
10. **Economy news** — RBI policy reviews, budgets, GST council decisions, big reports.

### The working method
- **Window**: most exams draw from roughly the **previous 6-12 months** before the exam date; monthly compilations cover this systematically.
- **One source, revised thrice**: a monthly compilation read once, revised after a month, and again in the last week beats five half-read sources.
- **Note the pairing, not the story**: for every item, note (person ↔ post), (award ↔ field), (event ↔ host), (day ↔ theme), (index ↔ publisher) — exams ask the pairing.
- **Static-first reading**: attach news to its static root (a grouping's founding year, an award's instituting year) — that part never expires.
- **Skip the noise**: opinion pieces, ongoing court arguments and speculation are rarely asked; anniversaries, firsts and superlatives (largest, first, fastest) are asked constantly.

### Quick revision
- Four frames: direct recall, match-the-column, statement-based, CA-to-static bridge.
- Ten buckets: appointments, awards, sports, summits, schemes, defence, space, indexes, days, economy.
- Working window ≈ previous 6-12 months; monthly compilation + three revisions.
- Exams test the **pairing** (person↔post, award↔field, day↔theme, index↔publisher).
- Attach every news item to its static root; anniversaries, firsts and superlatives score most."""
    S.pattern("ga-castr-p1", "Identify the question frame", "common",
        "The question itself describes how a news item was asked — 'which frame converts an award announcement into match-the-column' — or asks which preparation method suits a frame.",
        None,
        "1. Four frames: direct recall (single fact), match-the-column (pairs), statement-based (one wrong detail hidden in correct ones), CA-to-static bridge (news → permanent fact).\n2. Statement-based questions are cracked by eliminating the one planted error — a wrong year, ministry or city.\n3. Match-the-column is cracked by verifying each pair independently.",
        "A question gives **three numbered statements about a summit** and asks which are correct. The frame is —",
        "**Statement-based** — typically two true statements carry one planted error (wrong host city, wrong year or wrong membership), so test each statement against its static root.")
    S.pattern("ga-castr-p2", "The ten tracking buckets", "very common",
        "'Which of the following is NOT usually asked from current affairs', categories of news to track monthly, what a monthly compilation covers.",
        None,
        "1. The ten buckets: appointments, awards, sports, summits, schemes, defence exercises, space, indexes, important days, economy.\n2. Rarely asked: opinion columns, speculation, ongoing legal argument, celebrity gossip.\n3. Most asked within buckets: **firsts, superlatives, anniversaries and India-specific items**.",
        "Which type of news is **least likely** to appear as an exam question?",
        "**Opinion pieces and speculation** — exams ask settled facts: appointments, award winners, summit hosts, index ranks and launches, never editorial views.")
    S.pattern("ga-castr-p3", "Window and revision method", "common",
        "Questions on how far back a compilation should reach, how many revisions to plan, or what the 6-month convention is.",
        None,
        "1. Standard window: the **previous 6-12 months** before the exam (longer for Banking mains).\n2. Method: one monthly source, revised **three times** (same month, after a month, exam week).\n3. Note **pairings**, not stories — every revision is a pairing drill.",
        "The usual **preparation window** for current affairs in a typical exam is —",
        "About the **previous 6-12 months** before the exam — covered through monthly compilations and revised multiple times.")
    S.pattern("ga-castr-p4", "CA-to-static bridging", "common",
        "'A Nobel announcement helps revise which static topic', questions showing a news item and asking the permanent fact it connects to.",
        None,
        "1. Every news category has a static root: awards → award structure and instituting years; summits → group membership and HQ; schemes → ministry and launch year; days → person or event commemorated.\n2. Learn the static root once — it serves every future news cycle.\n3. In the exam, the static root often IS the answer even when the question names a recent event.",
        "A news item says a new **Global Innovation Index** edition is out. The permanent fact it anchors is —",
        "The **Global Innovation Index is published by WIPO** (World Intellectual Property Organization) — the index ↔ publisher pairing never changes with the year's edition.")

    S.q("ga-castr-p1", "easy", "A question that gives **two or three numbered statements** and asks which are correct is which frame?",
        ["Direct recall", "Match-the-column", "Statement-based", "Data-interpretation"], "Statement-based",
        "The **statement-based frame** hides one wrong detail (year, ministry, host city) inside mostly true statements — eliminate the planted error and the option set collapses.",
        "Statements + 'which are correct' = statement-based.", 20)
    S.q("ga-castr-p1", "medium", "Pairing **award ↔ field, day ↔ theme, index ↔ publisher** belongs to which frame?",
        ["Direct recall", "Match-the-column", "Statement-based", "Assertion-reason"], "Match-the-column",
        "Match-the-column tests **pairs** — the safest method is checking each pair independently; one verified wrong pair eliminates the whole option.",
        "Pairs = match-the-column.", 25)
    S.q("ga-castr-p1", "medium", "In a statement-based CA question, the fastest approach is —",
        ["Read all statements twice, then guess", "Eliminate the option containing a statement with a verified factual error", "Choose the option with the most statements", "Pick the longest option"], "Eliminate the option containing a statement with a verified factual error",
        "One planted error per set is the norm — a single **verified wrong detail** (wrong year, wrong ministry) knocks out every option containing it.",
        "One error kills three options.", 25)
    S.q("ga-castr-p2", "easy", "Which of the following is a **standard CA bucket** tracked every month?",
        ["Editorial opinion columns", "Ongoing speculation about policy", "Appointments and offices", "Celebrity gossip"], "Appointments and offices",
        "Appointments (persons in posts) are one of the **ten fixed buckets** — alongside awards, sports, summits, schemes, defence, space, indexes, days and economy news.",
        "Appointments = monthly staple.", 20)
    S.q("ga-castr-p2", "medium", "Within any news bucket, the items **most frequently asked** are —",
        ["Running commentary and analysis", "Firsts, superlatives and anniversaries", "Unverified rumours", "Long-term predictions"], "Firsts, superlatives and anniversaries",
        "Exams love **firsts** (first woman, first Indian), **superlatives** (largest, fastest, highest) and **anniversaries** (X years of an event) — they are precise, checkable and timeless once asked.",
        "Firsts, bests, birthdays.", 25)
    S.q("ga-castr-p2", "hard", "Consider the statements:\n1. Sports winners form a monthly CA bucket.\n2. Index ranks and their publishers form a monthly CA bucket.\n3. The framing of a pending court case is a common question.\nWhich are correct?",
        ["1 and 2 only", "1 and 3 only", "2 and 3 only", "1, 2 and 3"], "1 and 2 only",
        "Buckets 1 and 2 are standard. Statement 3 is wrong — **unsettled court arguments and speculation are not asked**; only concluded, factual outcomes appear.",
        "Concluded facts only.", 30)
    S.q("ga-castr-p3", "easy", "The most efficient way to cover a year of current affairs is —",
        ["Daily newspapers only, no revision", "One monthly compilation revised multiple times", "Five sources read once each", "Reading only the last week's news"], "One monthly compilation revised multiple times",
        "**One source, three revisions** (same month, after a month, exam week) — coverage plus retention beats scattered single reads.",
        "One source, three passes.", 20)
    S.q("ga-castr-p3", "medium", "While noting a **new scheme announcement**, the detail to record for exams is —",
        ["The speech's full text", "Scheme ↔ ministry ↔ purpose", "The launch venue's history", "The officials present"], "Scheme ↔ ministry ↔ purpose",
        "Exams ask the **pairing**: which ministry launched it, what it provides, who is eligible. The speech's rhetoric is never the answer.",
        "Ministry + benefit = the pair.", 25)
    S.q("ga-castr-p3", "medium", "For a **summit** news item, which note is most exam-productive?",
        ["The menu at the dinner", "Host country, theme and membership changes", "The travelling delegations' size", "The weather at the venue"], "Host country, theme and membership changes",
        "Summit questions recur on **host, theme, logo, outcomes and new members** — a fixed question shape across years.",
        "Host + theme + members.", 25)
    S.q("ga-castr-p4", "easy", "A news item about a **Nobel Prize** announcement is best revised through —",
        ["The winner's biography alone", "The Nobel prize categories and their structure", "That year's other news", "Omitting it as one-time news"], "The Nobel prize categories and their structure",
        "The **static root** — six prize categories, Alfred Nobel's will, Peace at Oslo, Economics added in 1969 — serves every year's cycle and often is the tested fact.",
        "News → its permanent structure.", 20)
    S.q("ga-castr-p4", "medium", "'X years of the Constitution' as a news anniversary primarily helps revise —",
        ["That year's politics", "The Constitution's making, parts and Preamble", "Nothing — anniversaries are decorative", "The current government's record"], "The Constitution's making, parts and Preamble",
        "Anniversaries are bridges to **static topics** — the making of the Constitution, Parts, Schedules and the Preamble — the static layer exams actually test.",
        "Anniversary → static root.", 25)
    S.q("ga-castr-p4", "hard", "Consider the statements about CA preparation:\n1. The CA-to-static bridge rewards learning award structures once.\n2. Volatile items like a person's current post stay useful only until they change.\n3. CA questions never connect to static GK.\nWhich are correct?",
        ["1 and 2 only", "1 and 3 only", "2 and 3 only", "1, 2 and 3"], "1 and 2 only",
        "Statements 1 and 2 are correct — structures endure, offices change. Statement 3 is wrong: the **CA-to-static bridge is one of the four standard frames**.",
        "Structures endure; posts change.", 30)
    return S


def build_awards():
    S = Sub("ca-awards")
    S.notes = """### Civilian awards — the ladder
| Award | Key facts |
|---|---|
| **Bharat Ratna** | Highest civilian honour; instituted **1954**; first: **C. Rajagopalachari, S. Radhakrishnan, C.V. Raman** (1954); first woman: **Indira Gandhi** (1971); first posthumous: **Lal Bahadur Shastri** (1966); first sportsperson: **Sachin Tendulkar** (2014) |
| **Padma Vibhushan** | Second-highest civilian award |
| **Padma Bhushan** | Third-highest |
| **Padma Shri** | Fourth-highest; all Padma awards instituted **1954**, announced on **Republic Day eve** |

### Gallantry awards — two ladders
- **Wartime**: **Param Vir Chakra** (highest, instituted 26 January 1950) → **Maha Vir Chakra** → **Vir Chakra**.
- **Peacetime**: **Ashoka Chakra** (highest peacetime) → **Kirti Chakra** → **Shaurya Chakra**. Gallantry awards are announced around **Republic Day and Independence Day**.

### Literary, film and global prizes
- **Jnanpith Award** — highest literary honour; first given **1965** to **G. Sankara Kurup** (Malayalam).
- **Sahitya Akademi Award** — given by the National Akademi of Letters (est. 1954).
- **Dadasaheb Phalke Award** — highest cinema honour; instituted **1969**; first recipient **Devika Rani**.
- **Nobel Prizes** — from **Alfred Nobel's will (1895)**, first awarded **1901**; six categories: Physics, Chemistry, Physiology or Medicine, Literature, Peace, and the **Economics prize added in 1969** (Sveriges Riksbank prize). All are awarded in **Stockholm** except **Peace, awarded in Oslo**.
- **Ramon Magsaysay Award** — the 'Asian Nobel', instituted **1957**, presented at **Manila**.
- **Booker Prize** — leading English-fiction prize; **International Booker** honours translated works.

### Sports awards — the pyramid
| Award | Field | Instituted |
|---|---|---|
| **Major Dhyan Chand Khel Ratna** | Highest sporting honour (named **renamed in 2021** from Rajiv Gandhi Khel Ratna, instituted 1991-92) | 1991-92 |
| **Arjuna Award** | Consistent outstanding performance | 1961 |
| **Dronacharya Award** | **Coaches** | 1985 |
| **Major Dhyan Chand Award** (lifetime achievement) | Contribution to sports | 2002 |
| **MAKA Trophy** | Best **university** | 1956-57 |

### Reading an award question
Exams test three layers, all permanent: the **ladder** (which is highest), the **instituting year / first recipient**, and **award ↔ field** matching (Dronacharya = coaches, MAKA = university). The winner of the current cycle changes; the structure never does — revise the structure once and every year's news plugs in.

### Quick revision
- Civilian ladder: Bharat Ratna (1954) > Padma Vibhushan > Padma Bhushan > Padma Shri; announced Republic Day eve.
- Bharat Ratna firsts: 1954 trio; woman — Indira Gandhi; posthumous — Shastri; sportsperson — Tendulkar.
- Gallantry: wartime PVC-MVC-Vir; peacetime Ashoka-Kirti-Shaurya.
- Jnanpith 1965 (Sankara Kurup); Dadasaheb Phalke 1969 (Devika Rani); Nobel 1901, Economics 1969, Peace in Oslo.
- Magsaysay 1957 Manila; Booker for English fiction.
- Sports: Khel Ratna 1991-92 (renamed 2021), Arjuna 1961, Dronacharya 1985 (coaches), Dhyan Chand 2002 (lifetime), MAKA (university)."""
    S.pattern("ga-caaw-p1", "Civilian awards: ladder and firsts", "very common",
        "'Which is the highest civilian award', 'the first woman to receive Bharat Ratna', ordering of Padma awards, first posthumous or sportsperson facts.",
        None,
        "1. Ladder: **Bharat Ratna > Padma Vibhushan > Padma Bhushan > Padma Shri**; all instituted **1954**, announced **Republic Day eve**.\n2. Bharat Ratna firsts: 1954 trio (Rajagopalachari, Radhakrishnan, Raman); woman — **Indira Gandhi 1971**; posthumous — **Shastri 1966**; sportsperson — **Tendulkar 2014**.\n3. 'Fourth-highest civilian honour' = **Padma Shri** — a frequent answer.",
        "The **first posthumous Bharat Ratna** was awarded to —",
        "**Lal Bahadur Shastri** (1966) — honoured the year after his death at Tashkent; the award's first woman recipient was Indira Gandhi (1971).")
    S.pattern("ga-caaw-p2", "Sports awards: award ↔ field matching", "very common",
        "'Dronacharya Award is given to', 'the highest sports honour is', 'MAKA Trophy relates to', matching each sports award with its field.",
        None,
        "1. **Khel Ratna** = highest sporting honour (renamed Major Dhyan Chand Khel Ratna in **2021**; instituted 1991-92).\n2. **Dronacharya = coaches** (1985); **Arjuna = players** (1961); **Dhyan Chand Award = lifetime contribution** (2002); **MAKA = best university**.\n3. Year anchors kill wrong options instantly.",
        "The **Dronacharya Award** honours —",
        "Outstanding **coaches** — instituted 1985; players receive the Arjuna Award instead.")
    S.pattern("ga-caaw-p3", "Nobel prize structure", "common",
        "'The Nobel Peace Prize is awarded at', 'which category was added in 1969', 'the Nobel prizes are given from whose bequest'.",
        None,
        "1. Origin: **Alfred Nobel's will (1895)**; first awarded **1901**; five original categories.\n2. **Economics (1969)** is the later 'Sveriges Riksbank' prize — the classic 'which is NOT an original Nobel' answer.\n3. Venue: **Oslo for Peace**, **Stockholm for the rest**.",
        "The Nobel Prize in **Economics** differs from the original prizes because —",
        "It was **added in 1969** (the Sveriges Riksbank Prize) — the original five came from Alfred Nobel's 1895 will, first given in 1901.")
    S.pattern("ga-caaw-p4", "Gallantry awards: wartime vs peacetime", "common",
        "'The highest wartime gallantry award', 'Ashoka Chakra is given for', ordering questions on Chakra series.",
        None,
        "1. Wartime ladder: **Param Vir Chakra > Maha Vir Chakra > Vir Chakra** (PVC instituted 26 January 1950).\n2. Peacetime ladder: **Ashoka Chakra > Kirti Chakra > Shaurya Chakra**.\n3. Never mix the ladders — 'highest gallantry award' without a qualifier means **PVC (wartime)**.",
        "India's **highest peacetime gallantry award** is —",
        "The **Ashoka Chakra** — wartime equivalent is the Param Vir Chakra (1950); Kirti Chakra and Shaurya Chakra follow it.")
    S.pattern("ga-caaw-p5", "Literature, film and international prizes", "common",
        "'The Jnanpith Award was first won by', 'Dadasaheb Phalke Award relates to', 'the Asian Nobel is', matching prizes with fields and first recipients.",
        None,
        "1. **Jnanpith** — highest literary award, first **1965**, **G. Sankara Kurup**; **Sahitya Akademi** — the Akademi's own award.\n2. **Dadasaheb Phalke (1969, Devika Rani)** — highest cinema honour; **Booker** — English fiction; **International Booker** — translation.\n3. **Magsaysay (1957, Manila)** — the 'Asian Nobel'; **Oscars/Academy Awards** — since 1929.",
        "The **Ramon Magsaysay Award**, often called the 'Asian Nobel', is presented in —",
        "**Manila, Philippines** — instituted in **1957** for public service and leadership across Asia.")

    S.q("ga-caaw-p1", "easy", "India's **highest civilian award** is —",
        ["Padma Vibhushan", "Bharat Ratna", "Param Vir Chakra", "Padma Shri"], "Bharat Ratna",
        "**Bharat Ratna** (1954) tops the civilian ladder; Param Vir Chakra is a *gallantry* award, not civilian.",
        "Civilian top = Bharat Ratna.", 20)
    S.q("ga-caaw-p1", "easy", "The **fourth-highest** civilian award of India is —",
        ["Padma Shri", "Padma Bhushan", "Bharat Ratna", "Ashoka Chakra"], "Padma Shri",
        "Order: Bharat Ratna → Padma Vibhushan → Padma Bhushan → **Padma Shri**.",
        "Shri = 4th.", 20)
    S.q("ga-caaw-p1", "medium", "The **first woman** to receive the Bharat Ratna was —",
        ["Mother Teresa", "Indira Gandhi", "Sarojini Naidu", "Lata Mangeshkar"], "Indira Gandhi",
        "**Indira Gandhi (1971)**; Mother Teresa (1980) and Lata Mangeshkar (2001) came later.",
        "1971 = Indira.", 25)
    S.q("ga-caaw-p1", "medium", "Padma awards are ordinarily announced on the eve of —",
        ["Independence Day", "Republic Day", "Gandhi Jayanti", "Constitution Day"], "Republic Day",
        "The Padma list is announced on **Republic Day eve** (25 January); gallantry awards also cluster around 26 January and 15 August.",
        "Eve of 26 January.", 25)
    S.q("ga-caaw-p2", "easy", "The **highest sporting honour** of India is the —",
        ["Arjuna Award", "Major Dhyan Chand Khel Ratna Award", "Dronacharya Award", "MAKA Trophy"], "Major Dhyan Chand Khel Ratna Award",
        "The **Khel Ratna** (instituted 1991-92, renamed after Major Dhyan Chand in 2021) is the top sports award.",
        "Khel Ratna = top.", 20)
    S.q("ga-caaw-p2", "medium", "The **Dronacharya Award** is given to outstanding —",
        ["Players", "Coaches", "Sports journalists", "Universities"], "Coaches",
        "**Dronacharya (1985) = coaches** — named after the teacher of archery in the Mahabharata; players get the Arjuna Award.",
        "Guru award = Dronacharya.", 20)
    S.q("ga-caaw-p2", "medium", "The **MAKA Trophy** is awarded to the best —",
        ["State sports council", "University in sports", "Sports journalist", "Para-athlete"], "University in sports",
        "The **Maulana Abul Kalam Azad (MAKA) Trophy** (1956-57) honours the best **university** in sports.",
        "MAKA = university.", 25)
    S.q("ga-caaw-p2", "hard", "Arrange by instituting year (earliest first):\n1. Arjuna Award 2. Dronacharya Award 3. Khel Ratna",
        ["1, 2, 3", "2, 1, 3", "3, 1, 2", "1, 3, 2"], "1, 2, 3",
        "Arjuna **1961** → Dronacharya **1985** → Khel Ratna **1991-92** (renamed Major Dhyan Chand Khel Ratna, 2021).",
        "1961 → 1985 → 1991.", 30)
    S.q("ga-caaw-p3", "easy", "The **Nobel Peace Prize** is awarded in —",
        ["Stockholm", "Oslo", "Geneva", "Copenhagen"], "Oslo",
        "Peace is conferred at **Oslo** (by the Norwegian Nobel Committee); all other categories are presented at **Stockholm**.",
        "Peace = Oslo.", 20)
    S.q("ga-caaw-p3", "medium", "Which Nobel category was **not** part of Alfred Nobel's original will?",
        ["Literature", "Physics", "Economics", "Peace"], "Economics",
        "Nobel's 1895 will listed five prizes; **Economics** was added in **1969** as the Sveriges Riksbank memorial prize.",
        "Economics = the latecomer (1969).", 25)
    S.q("ga-caaw-p3", "medium", "The first Nobel Prizes were awarded in —",
        ["1895", "1901", "1911", "1945"], "1901",
        "Nobel signed his will in **1895**; the first prizes followed in **1901**.",
        "Will 1895 → prizes 1901.", 25)
    S.q("ga-caaw-p4", "easy", "India's **highest wartime gallantry award** is the —",
        ["Ashoka Chakra", "Param Vir Chakra", "Vir Chakra", "Kirti Chakra"], "Param Vir Chakra",
        "**Param Vir Chakra** (instituted 26 January 1950) is the top wartime gallantry medal; Ashoka Chakra heads the peacetime ladder.",
        "PVC = wartime top.", 20)
    S.q("ga-caaw-p4", "medium", "Which of the following is a **peacetime** gallantry award?",
        ["Vir Chakra", "Maha Vir Chakra", "Kirti Chakra", "Param Vir Chakra"], "Kirti Chakra",
        "Peacetime ladder: **Ashoka Chakra > Kirti Chakra > Shaurya Chakra**. The MVC and Vir Chakra are wartime medals.",
        "Kirti = peacetime No. 2.", 25)
    S.q("ga-caaw-p5", "easy", "The **Jnanpith Award** is associated with —",
        ["Cinema", "Literature", "Science", "Journalism"], "Literature",
        "The **Jnanpith** is India's highest literary honour — first given in **1965** to **G. Sankara Kurup**.",
        "Jnanpith = literature.", 20)
    S.q("ga-caaw-p5", "medium", "The **Dadasaheb Phalke Award**, first given to Devika Rani, honours —",
        ["Literature", "Cinema", "Classical music", "Painting"], "Cinema",
        "The highest Indian **cinema** honour — instituted **1969**, first recipient **Devika Rani**.",
        "Phalke = cinema's father's award.", 25)
    S.q("ga-caaw-p5", "hard", "Consider the statements:\n1. The first Bharat Ratnas were conferred in 1954.\n2. The Ramon Magsaysay Award is presented in Manila.\n3. The Bharat Ratna can be awarded posthumously.\nWhich are correct?",
        ["1, 2 and 3", "1 and 2 only", "2 and 3 only", "1 and 3 only"], "1, 2 and 3",
        "All three are correct — the 1954 first batch, the Manila-based Magsaysay (1957), and posthumous conferral (Shastri, 1966) are settled facts.",
        "1954, Manila, posthumous — all true.", 30)
    return S


def build_sports():
    S = Sub("ca-sports")
    S.notes = """### How sports CA is asked
Every tournament question recycles the same five details: **host country/city, motto or theme, mascot, the champion (and runner-up), and India's performance** (medal tally, records, firsts). Note those five for every event in your window; learn the **cycle and organiser** of each event permanently.

### The recurring events and their cycles
| Event | Cycle | Structural facts |
|---|---|---|
| **Olympics (Summer)** | 4 years | Modern Games from **1896 Athens**, revived by **Pierre de Coubertin**; **IOC** (1894) at **Lausanne**; motto 'Citius, Altius, **Communius**' (together, added 2021); five rings |
| **Winter Olympics** | 4 years, offset | First: **1924 Chamonix** |
| **Paralympics** | with Olympics | For athletes with disabilities |
| **Commonwealth Games** | 4 years | Began as **British Empire Games, 1930 Hamilton** |
| **Asian Games** | 4 years | First: **1951 New Delhi**; run by the **OCA** |
| **FIFA World Cup** | 4 years | First: **1930 Uruguay** |
| **ICC Cricket World Cup (ODI)** | 4 years | First: **1975 England**; India won **1983, 2011** |
| **ICC T20 World Cup** | 2 years | India won the first, **2007** |
| **IPL** | annual | BCCI's T20 league, from **2008** |
| **Ranji Trophy** | annual | Indian first-class championship (1934), named after **Ranjitsinhji** |
| **Khelo India Games** | annual | From **2018**, school + university tiers |
| **Thomas Cup / Uber Cup** | 2 years | Men's / women's **badminton** team events |

### India anchors — permanent facts
- First Olympics participation: **1900 Paris** (**Norman Pritchard**, two athletics silvers).
- **Hockey: eight Olympic golds** — the run began at **1928 Amsterdam**; last gold **1980 Moscow**.
- First **individual** Olympic gold: **Abhinav Bindra** (2008, 10 m air rifle); **Neeraj Chopra** took javelin gold at the Tokyo Games.
- First Cricket World Cup win: **1983** under Kapil Dev at Lord's; T20 in **2007**; 2011 under M.S. Dhoni.
- India won the **Thomas Cup** for the first time in **2022** — a settled historical fact now.

### How to note a tournament
For each event in the window, record one line: *event — year — host — champion — India's highlight — any record*. Statements in exams typically swap **one** of these (a wrong host city or a wrong champion); the rest stay true. Superlatives recur too: oldest tournament (Durand Cup, 1888, Asia's oldest football cup), oldest tennis event (Wimbledon, 1877), the Davis Cup in men's tennis.

### Quick revision
- Note five: host, motto/theme, mascot, champion, India's highlight.
- Olympics 1896 Athens (Coubertin); IOC Lausanne; Winter 1924 Chamonix; CWG from 1930 Hamilton.
- Asian Games first at **New Delhi (1951)**; FIFA WC 1930; Cricket WC 1975 (India: 1983, 2011); T20 biennial.
- IPL 2008; Ranji 1934; Khelo India 2018; Thomas/Uber = badminton team cups.
- India: 1900 first participation; hockey 8 golds; Bindra first individual gold (2008); Thomas Cup 2022."""
    S.pattern("ga-casp-p1", "Tournament ↔ sport / organiser matching", "very common",
        "'Thomas Cup is related to which sport', 'the Ranji Trophy is associated with', 'which body conducts the IPL', matching events with sports.",
        None,
        "1. Cup ↔ sport pins: **Thomas (men) / Uber (women)** = badminton; **Davis** = tennis; **Santosh** = football (states); **Ranji** = cricket (first-class); **Durand** = football (Asia's oldest, 1888).\n2. **IPL** = BCCI (from 2008); **Khelo India** = government's annual games (2018).\n3. The odd option in such questions is usually a swapped sport.",
        "The **Thomas Cup** is associated with —",
        "**Men's badminton** (team event) — its women's counterpart is the **Uber Cup**; India first won the Thomas Cup in 2022.")
    S.pattern("ga-casp-p2", "Cycles and first editions", "common",
        "'How often is the T20 World Cup held', 'the first Asian Games were held at', 'the first Cricket World Cup was played in', year and cycle questions.",
        None,
        "1. 4-yearly: Olympics, Winter Olympics (offset), CWG, Asian Games, FIFA WC, ODI Cricket WC. **Biennial**: T20 WC, Thomas/Uber Cups.\n2. First editions: Olympics **1896 Athens**; Winter **1924**; CWG **1930**; Asian Games **1951 New Delhi**; FIFA **1930**; ODI WC **1975**.\n3. Annual: IPL (2008), Ranji (1934), Khelo India (2018).",
        "The **first Asian Games** were hosted by —",
        "**New Delhi (1951)** — a home-soil first that exams return to; the Games are held every four years under the OCA.")
    S.pattern("ga-casp-p3", "Olympic facts", "very common",
        "'The modern Olympics began in', 'the IOC is headquartered at', 'the Olympic motto is', questions on rings, motto, founder.",
        None,
        "1. Modern Games: **1896 Athens**, revived by **Pierre de Coubertin**; **IOC (1894)** sits at **Lausanne**.\n2. Motto: 'Citius, Altius, **Communius**' (Faster, Higher, Stronger-*Together* — 'Communius' added 2021); **five interlocking rings**.\n3. Winter Games separate, first **1924 Chamonix**; Paralympics follow the main Games.",
        "The headquarters of the **International Olympic Committee** is at —",
        "**Lausanne, Switzerland** — the IOC, founded in 1894, revived the Games at Athens in 1896.")
    S.pattern("ga-casp-p4", "India-specific sports records", "very common",
        "'India's first individual Olympic gold', 'how many hockey golds', 'India first won the Thomas Cup in', permanent India anchors.",
        None,
        "1. **1900 Paris** = first participation (Norman Pritchard); **hockey = 8 Olympic golds** (1928-1980 era).\n2. **Abhinav Bindra (2008)** = first individual gold; **Neeraj Chopra** = javelin gold (Tokyo Games).\n3. Cricket: 1983 (ODI), 2007 (T20), 2011; **Thomas Cup 2022** first win.",
        "India's first **individual Olympic gold medal** was won by —",
        "**Abhinav Bindra** — 10 m air rifle at the **2008 Beijing** Games; the hockey team had won team golds since 1928.")
    S.pattern("ga-casp-p5", "Champion-host-mascot statement sets", "common",
        "Statements mixing one wrong host city, champion or mascot into correct sports facts; ordering of tournaments by year.",
        None,
        "1. For every event in the window, memorise the line: event — host — champion — India's highlight.\n2. In statements, the wrong detail is usually the **host city** or **champion**; years and sports are less often swapped.\n3. Superlatives recur: Durand (1888) oldest in Asia; Wimbledon (1877) oldest in tennis.",
        "Consider: 1. The IPL is conducted by the BCCI. 2. The Durand Cup is a hockey tournament. 3. Wimbledon is the oldest tennis championship. Which are correct?",
        "Statements 1 and 3 only — the **Durand Cup is football** (Asia's oldest, since 1888); IPL-BCCI and Wimbledon's seniority are correct.")

    S.q("ga-casp-p1", "easy", "The **Thomas Cup** is associated with —",
        ["Football", "Badminton", "Tennis", "Hockey"], "Badminton",
        "The **Thomas Cup** is the men's team badminton world championship; women play for the **Uber Cup**.",
        "Thomas/Uber = badminton.", 20)
    S.q("ga-casp-p1", "medium", "The **Ranji Trophy** is India's premier —",
        ["Football league", "First-class cricket championship", "Kabaddi league", "Chess tournament"], "First-class cricket championship",
        "Started **1934** and named after **Ranjitsinhji**, it is the domestic first-class championship; the IPL (2008) is the T20 league.",
        "Ranji = first-class, 1934.", 25)
    S.q("ga-casp-p1", "medium", "The **Durand Cup**, Asia's oldest football tournament, began in —",
        ["1888", "1911", "1934", "1951"], "1888",
        "The **Durand Cup (1888)** is Asia's oldest football tournament — a favourite superlative question.",
        "Durand 1888 = oldest.", 25)
    S.q("ga-casp-p2", "easy", "The **FIFA World Cup** was first held in —",
        ["1930", "1950", "1966", "1970"], "1930",
        "Uruguay hosted and won the first FIFA World Cup in **1930**; the tournament runs every four years.",
        "FIFA 1930, Uruguay.", 20)
    S.q("ga-casp-p2", "medium", "The **ICC T20 World Cup** is held —",
        ["Every year", "Every two years", "Every four years", "Every five years"], "Every two years",
        "The T20 World Cup is **biennial**; the ODI World Cup is four-yearly (first 1975).",
        "T20 = 2-year cycle.", 25)
    S.q("ga-casp-p2", "medium", "The **Commonwealth Games** began as the British Empire Games in —",
        ["1911", "1930", "1951", "1958"], "1930",
        "First held at **Hamilton, Canada in 1930** as the British Empire Games; four-yearly thereafter.",
        "Hamilton 1930.", 25)
    S.q("ga-casp-p3", "easy", "The **modern Olympic Games** began in —",
        ["1896 at Athens", "1900 at Paris", "1924 at Paris", "1936 at Berlin"], "1896 at Athens",
        "**1896, Athens** — revived by Pierre de Coubertin; the IOC (1894) is headquartered at **Lausanne**.",
        "Athens 1896.", 20)
    S.q("ga-casp-p3", "medium", "The Olympic motto 'Citius, Altius, Communius' adds which idea?",
        ["Fairness", "Together", "Friendship only", "Speed"], "Together",
        "**Communius = 'Together'**, added in 2021 to 'Faster, Higher, Stronger' — the newest static layer of the motto.",
        "Communius = together (2021).", 25)
    S.q("ga-casp-p3", "medium", "The first **Winter Olympics** were held at —",
        ["Chamonix", "Oslo", "Innsbruck", "Lake Placid"], "Chamonix",
        "**Chamonix, 1924** — the Winter Games run in a separate four-year cycle from the Summer Games.",
        "Chamonix 1924.", 25)
    S.q("ga-casp-p4", "easy", "India first participated in the Olympics in —",
        ["1896", "1900", "1920", "1928"], "1900",
        "**1900 Paris** — Norman Pritchard won two athletics silvers; hockey's gold run began only in 1928.",
        "1900 = first participation.", 20)
    S.q("ga-casp-p4", "medium", "How many **Olympic hockey golds** has India won?",
        ["Six", "Seven", "Eight", "Nine"], "Eight",
        "**Eight golds** — from Amsterdam 1928 to Moscow 1980, the longest run in Olympic hockey.",
        "Hockey = 8.", 20)
    S.q("ga-casp-p4", "hard", "Arrange India's sporting firsts chronologically:\n1. First Olympic hockey gold 2. First individual Olympic gold 3. First Cricket World Cup win",
        ["1, 3, 2", "3, 1, 2", "1, 2, 3", "2, 3, 1"], "1, 3, 2",
        "Hockey gold **1928** → Cricket World Cup **1983** → individual gold (Bindra) **2008**.",
        "1928 → 1983 → 2008.", 30)
    S.q("ga-casp-p5", "easy", "The **Indian Premier League (IPL)** began in —",
        ["2005", "2008", "2010", "2013"], "2008",
        "The BCCI launched the T20 IPL in **2008** — annual since then.",
        "IPL = 2008.", 20)
    S.q("ga-casp-p5", "medium", "Consider the statements:\n1. The first Cricket World Cup was played in 1975.\n2. India won the ODI World Cup in 1983 and 2011.\n3. The Santosh Trophy is a tennis event.\nWhich are correct?",
        ["1 and 2 only", "1 and 3 only", "2 and 3 only", "1, 2 and 3"], "1 and 2 only",
        "Statements 1 and 2 are correct. Statement 3 is wrong — the **Santosh Trophy is football** (inter-state championship).",
        "Santosh = football.", 30)
    S.q("ga-casp-p5", "medium", "**Khelo India Games** were launched in —",
        ["2014", "2016", "2018", "2020"], "2018",
        "**Khelo India (2018)** — annual school and university games to build a sporting pipeline.",
        "Khelo = 2018.", 25)
    return S
