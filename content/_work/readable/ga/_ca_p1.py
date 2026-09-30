"""Current affairs part 1: ca-strategy, ca-awards, ca-sports.

This topic is the static, how-to-prepare layer of current affairs.
Only facts already present in the old notes are used; no recent-event facts are added.
"""
from _eco_common import pat, mis, trick

# --- ordering used in examples ---------------------------------------------------
# ga-caaw-p6: 1 Jnanpith 1965, 2 Bharat Ratna 1954, 3 Dronacharya 1985, 4 Phalke 1969
_years = {1: 1965, 2: 1954, 3: 1985, 4: 1969}
assert sorted(_years, key=_years.get) == [2, 1, 4, 3]
assert 1951 < 1975  # first Asian Games before first Cricket World Cup (trick example)

SUBS = {}

# =====================================================================
SUBS["ca-strategy"] = dict(
    concept=(
        "Current affairs (CA) questions turn one news fact into one of four frames: direct recall, match-the-column, "
        "statement-based, or a bridge to static GK. Track ten news buckets every month. "
        "For each item, note the pair the exam asks, such as person and post, not the whole story. "
        "Study the last 6-12 months from one monthly source and revise it three times."
    ),
    notes=r"""### The four question frames
An exam never asks the full news story. It takes one fact and puts it in one of four frames.

| Frame | What it looks like |
|---|---|
| Direct recall | One fact, four options. "Who won the Y award?" |
| Match-the-column | Pairs such as award and field, day and theme, summit and host, index and publisher |
| Statement-based | Two or three numbered statements. One carries a wrong detail. |
| CA-to-static bridge | The news opens a door to a permanent fact |

> **Example:** A Nobel announcement is news. The question may ask the Nobel categories. That is the bridge frame.

### How to crack each frame
- **Direct recall:** you need the fact itself. Your notes must hold it as a short pair.
- **Match-the-column:** check each pair on its own. One wrong letter kills the whole option.
- **Statement-based:** hunt for the one planted error. It is usually a wrong year, a wrong ministry or a wrong city.
- **Bridge:** a summit leads to the group's members and HQ. A new scheme leads to its ministry.

> **Tip:** In a statement set, test every statement against its static root. The root never changes.

### The ten buckets to track every month
Sort every news item into one of ten buckets.

1. **Appointments and offices:** President, Governors, CJI, service chiefs, regulators, heads of world bodies.
2. **Awards and honours:** Bharat Ratna, Padma, gallantry; Nobel, Magsaysay, Booker.
3. **Sports:** winners, hosts, tournaments, records.
4. **Summits and conferences:** host country, theme, outcomes.
5. **Schemes and launches:** new schemes, portals, missions, extensions.
6. **Defence:** exercise names with the partner country, missiles, new inductions.
7. **Space:** ISRO launches, landings, satellites.
8. **Indexes and reports:** India's rank and the publisher.
9. **Important days:** especially UN days and their yearly themes.
10. **Economy:** RBI policy reviews, budgets, GST Council decisions, big reports.

### The working method
The **window** is the time span an exam draws from. Most exams use the last 6-12 months before the exam date.

- Pick **one** monthly compilation. It covers the window month by month.
- Read it once. Revise it after a month. Revise it again in the last week.
- One source revised three times beats five sources read once.

> **Rule:** Note the pairing, not the story. Person and post. Award and field. Event and host. Day and theme. Index and publisher.

### Attach news to its static root
Every news item has a permanent part. Learn that part once and it serves every future year.

| News type | Static root to learn |
|---|---|
| Award | Its structure and the year it began |
| Summit | The group's members, founding year and HQ |
| Scheme | Its ministry and launch year |
| Important day | The person or event it remembers |
| Index | Its publisher |

Often the static root **is** the answer, even when the question names a recent event.

### What to skip and what to chase
Some news is almost never asked. Skip opinion pieces, ongoing court arguments and speculation.

Other news is asked all the time. Chase **firsts, superlatives** (largest, first, fastest), **anniversaries** and India-specific items.

> **Watch:** Exams ask settled facts. An editorial view can never be a correct option.
""",
    tricks=[
        trick("Pairing drill",
              "Read a news item and write its two halves, such as 'X award, field' or 'Y summit, host'. Exams ask the halves, not the story.",
              "A new Chief Justice is sworn in. What do you note?",
              ["Skip the ceremony details.", "Note the pair: the post and the person.",
               "Add the static root: the collegium recommends and the President appoints."],
              "The post and the person, plus how the appointment is made."),
        trick("Three reads of one source",
              "Read the monthly compilation once, revise it after a month, and revise it again in exam week.",
              "You have five CA sources and little time. What is the better plan?",
              ["Pick one monthly compilation.", "Plan three rounds: first read, after a month, last week."],
              "One source revised three times."),
    ],
    mistakes=[
        mis("Reading five sources once each.", "Revise one monthly source three times."),
        mis("Studying the news story and ignoring the pairing.", "Note the pair the exam asks: person and post, award and field, day and theme."),
        mis("Assuming CA never links back to static GK.", "Attach every item to its static root, such as an index to its publisher."),
        mis("Reading opinion pieces and speculation closely.", "Skip them. Chase firsts, superlatives, anniversaries and India items."),
        mis("In a statement set, judging the whole set by one familiar fact.", "Test each statement alone. Usually one has a planted wrong year, ministry or city."),
    ],
    revision=[
        "Four frames: direct recall, match-the-column, statement-based, CA-to-static bridge.",
        "Ten buckets: appointments, awards, sports, summits, schemes, defence, space, indexes, days, economy.",
        "Window: the last 6-12 months before the exam.",
        "One monthly compilation, revised three times.",
        "Exams test the pairing: person and post, award and field, day and theme, index and publisher.",
        "Attach every news item to its static root.",
        "Firsts, superlatives and anniversaries score most. Opinion and speculation are rarely asked.",
    ],
    patterns=[
        pat("ga-castr-p2", "The ten tracking buckets", "very common",
            "'Which of the following is NOT usually asked from current affairs', or which kinds of news to track every month.",
            ["Recall the ten buckets: appointments, awards, sports, summits, schemes, defence, space, indexes, days, economy.",
             "Mark opinion, speculation, ongoing court arguments and gossip as rarely asked.",
             "Inside a bucket, prefer firsts, superlatives, anniversaries and India items.",
             "Pick the option that is not a settled fact."],
            "Exams ask settled facts, so anything that is only a view drops out.",
            "Which type of news is least likely to appear as an exam question?",
            ["Appointments, award winners and index ranks are settled facts.", "An editorial view is not a fact.",
             "Speculation can turn out false."],
            "Opinion pieces and speculation"),
        pat("ga-castr-p1", "Identify the question frame", "common",
            "The question describes how a news item was asked, or asks which method suits a frame.",
            ["List the four frames: direct recall, match-the-column, statement-based, bridge.",
             "One fact with four options is direct recall.",
             "Numbered statements with one wrong detail is statement-based.",
             "Pairs to be matched is match-the-column; news leading to a permanent fact is the bridge."],
            "Each frame has one clear shape, so the shape names the frame.",
            "A question gives three numbered statements about a summit and asks which are correct. What is the frame?",
            ["The question has numbered statements.", "Usually two are true and one has a planted error.",
             "Test each one against its static root."],
            "Statement-based"),
        pat("ga-castr-p3", "Window and revision method", "common",
            "How far back to study, how many revisions to plan, or what a monthly compilation should cover.",
            ["The standard window is the last 6-12 months before the exam.", "Banking mains may use a longer window.",
             "Use one monthly source, revised three times.", "Make every revision a pairing drill."],
            "A fixed window and one source keep the load small enough to revise.",
            "What is the usual preparation window for current affairs in a typical exam?",
            ["Most exams draw from recent months, not years.", "Monthly compilations cover the span month by month."],
            "About the last 6-12 months before the exam"),
        pat("ga-castr-p4", "CA-to-static bridging", "common",
            "A news item is shown and the question asks the permanent fact it connects to.",
            ["Name the news type: award, summit, scheme, day or index.",
             "Recall its static root: structure, members and HQ, ministry, person remembered, or publisher.",
             "Answer with the static root, not the event detail."],
            "The static root does not change from year to year, so it is safe to ask.",
            "A news item says a new Global Innovation Index edition is out. Which permanent fact does it anchor?",
            ["It is an index, so the root is the publisher.", "The publisher stays the same every edition."],
            "The Global Innovation Index is published by WIPO (World Intellectual Property Organization)."),
        pat("ga-castr-p5", "Pick the exam-worthy detail", "occasional",
            "'While reading this news, which detail should you note', or a news item followed by options of what to remember.",
            ["Find the pair inside the news: person and post, award and field, event and host.",
             "Add the static root, such as how the post is filled.",
             "Drop ceremony details, quotes and opinions."],
            "Exams ask the halves of a pair, never the colour of the story.",
            "A new Chief Justice of India is sworn in. Which detail is most worth noting?",
            ["The pair is the post and the person.", "The static root is the appointment process.",
             "The venue and guests of the ceremony are not asked."],
            "The person and the post, plus the process: collegium recommends, President appoints."),
    ],
)

# =====================================================================
SUBS["ca-awards"] = dict(
    concept=(
        "Learn the ladders, not the winners. Each group of awards has a fixed order, a starting year and a field. "
        "Winners change every year, but the structure stays the same. "
        "Once you know the structure, every year's news fits into it."
    ),
    notes=r"""### Civilian awards: the ladder
India has four civilian awards, from highest to fourth.

| Rank | Award |
|---|---|
| 1 | Bharat Ratna |
| 2 | Padma Vibhushan |
| 3 | Padma Bhushan |
| 4 | Padma Shri |

All four began in **1954**. The Padma awards are announced on the **eve of Republic Day**.

> **Example:** "The fourth-highest civilian award" is Padma Shri. Count down the ladder.

### Bharat Ratna firsts
The Bharat Ratna is the highest civilian honour. Exams love its "firsts".

| First | Name | Year |
|---|---|---|
| First recipients | C. Rajagopalachari, S. Radhakrishnan, C.V. Raman | 1954 |
| First posthumous | Lal Bahadur Shastri | 1966 |
| First woman | Indira Gandhi | 1971 |
| First sportsperson | Sachin Tendulkar | 2014 |

"Posthumous" means given after the person's death.

### Gallantry awards: two ladders
Gallantry awards honour bravery. There are two separate ladders.

| Level | Wartime | Peacetime |
|---|---|---|
| Highest | Param Vir Chakra | Ashoka Chakra |
| Second | Maha Vir Chakra | Kirti Chakra |
| Third | Vir Chakra | Shaurya Chakra |

The Param Vir Chakra was instituted on **26 January 1950**. Gallantry awards are announced around **Republic Day and Independence Day**.

> **Watch:** "Highest gallantry award" with no qualifier means the Param Vir Chakra.

### Literature, cinema and world prizes
- **Jnanpith Award:** the highest literary honour. First given in **1965** to **G. Sankara Kurup** (Malayalam).
- **Sahitya Akademi Award:** given by the National Akademi of Letters, set up in **1954**.
- **Dadasaheb Phalke Award:** the highest cinema honour. Instituted in **1969**. First winner: **Devika Rani**.
- **Nobel Prizes:** they come from **Alfred Nobel's will (1895)**. First given in **1901**.
- **Ramon Magsaysay Award:** the "Asian Nobel". Instituted in **1957**, presented in **Manila**.
- **Booker Prize:** the leading prize for English fiction. The **International Booker** honours translated works.
- **Oscars (Academy Awards):** given since **1929**.

### The Nobel structure
There are six Nobel categories today.

1. Physics
2. Chemistry
3. Physiology or Medicine
4. Literature
5. Peace
6. Economics, **added in 1969** (the Sveriges Riksbank prize)

The first five are the original prizes. All are given in **Stockholm**, except Peace, which is given in **Oslo**.

> **Tip:** "Which is not an original Nobel category?" The answer is Economics.

### Sports awards: the pyramid
| Award | Given for | Began |
|---|---|---|
| Major Dhyan Chand Khel Ratna | Highest sporting honour | 1991-92 |
| Arjuna Award | Consistent top performance by players | 1961 |
| Dronacharya Award | **Coaches** | 1985 |
| Major Dhyan Chand Award | Lifetime contribution to sport | 2002 |
| MAKA Trophy | Best **university** | 1956-57 |

The Khel Ratna was earlier the Rajiv Gandhi Khel Ratna. It was **renamed in 2021**.

### How an award question is built
Exams test three layers. All three are permanent.

- **The ladder:** which award is highest.
- **The start:** the year it began, or its first winner.
- **Award and field:** Dronacharya is for coaches, MAKA is for a university.
""",
    tricks=[
        trick("Ladder memory",
              "Civilian: Ratna, Vibhushan, Bhushan, Shri. Sports: Khel Ratna, Arjuna for players, Dronacharya for coaches.",
              "What is the fourth-highest civilian honour?",
              ["Bharat Ratna is first.", "Padma Vibhushan is second, Padma Bhushan third.", "The next step down is Padma Shri."],
              "Padma Shri"),
        trick("Arjuna plays, Drona teaches",
              "In the Mahabharata, Arjuna was the pupil and Drona the teacher. So Arjuna is for players and Dronacharya for coaches.",
              "The Dronacharya Award is given to whom?",
              ["Drona was a teacher.", "In sport, the teacher is the coach."],
              "Coaches"),
    ],
    mistakes=[
        mis("Calling the Param Vir Chakra a civilian award.", "It is the highest wartime gallantry award."),
        mis("Confusing Dronacharya with Arjuna.", "Dronacharya is for coaches. Arjuna is for players."),
        mis("Placing Padma Shri above Padma Bhushan.", "Order: Bharat Ratna, Padma Vibhushan, Padma Bhushan, Padma Shri."),
        mis("Mixing the wartime and peacetime ladders.", "Wartime: PVC, MVC, Vir. Peacetime: Ashoka, Kirti, Shaurya."),
        mis("Saying all Nobel Prizes are given in Stockholm.", "The Peace Prize is given in Oslo."),
        mis("Counting Economics as an original Nobel category.", "It was added in 1969. The first prizes were given in 1901."),
    ],
    revision=[
        "Civilian: Bharat Ratna > Padma Vibhushan > Padma Bhushan > Padma Shri. All from 1954.",
        "Bharat Ratna firsts: 1954 trio; posthumous Shastri 1966; woman Indira Gandhi 1971; sportsperson Tendulkar 2014.",
        "Wartime: Param Vir (1950) > Maha Vir > Vir Chakra. Peacetime: Ashoka > Kirti > Shaurya Chakra.",
        "Jnanpith 1965 (G. Sankara Kurup). Dadasaheb Phalke 1969 (Devika Rani).",
        "Nobel: will 1895, first 1901, Economics 1969, Peace in Oslo.",
        "Magsaysay: 1957, Manila, the 'Asian Nobel'. Booker: English fiction.",
        "Sports: Khel Ratna 1991-92 (renamed 2021), Arjuna 1961, Dronacharya 1985, Dhyan Chand Award 2002, MAKA for universities.",
    ],
    patterns=[
        pat("ga-caaw-p1", "Civilian awards: ladder and firsts", "very common",
            "'The highest civilian award', 'the first woman to get Bharat Ratna', ordering the Padma awards, or a first posthumous winner.",
            ["Write the ladder: Bharat Ratna, Padma Vibhushan, Padma Bhushan, Padma Shri.",
             "Recall the firsts: 1954 trio, Shastri 1966, Indira Gandhi 1971, Tendulkar 2014.",
             "Match the word in the question (woman, posthumous, sportsperson) to its row."],
            "The ladder and four firsts cover almost every civilian-award question.",
            "The first posthumous Bharat Ratna was given to whom?",
            ["Posthumous means after death.", "The first such award came in 1966.",
             "It went to the Prime Minister who died at Tashkent."],
            "Lal Bahadur Shastri (1966)"),
        pat("ga-caaw-p2", "Sports awards: award and field", "very common",
            "'The Dronacharya Award is given to', 'the highest sports honour', or 'the MAKA Trophy relates to'.",
            ["Khel Ratna is the highest sporting honour.", "Arjuna is for players, Dronacharya for coaches.",
             "Dhyan Chand Award is for lifetime contribution. MAKA is for the best university.",
             "Use the start years to cut wrong options: 1961, 1985, 2002."],
            "Each sports award has one field, so a swapped field is easy to spot.",
            "The Dronacharya Award honours whom?",
            ["Drona was a teacher in the Mahabharata.", "In sport the teacher is the coach.",
             "Players get the Arjuna Award instead."],
            "Outstanding coaches"),
        pat("ga-caaw-p3", "Nobel prize structure", "common",
            "'The Nobel Peace Prize is given at', 'which category was added in 1969', or 'whose will started the prizes'.",
            ["Origin: Alfred Nobel's will of 1895. First prizes: 1901.",
             "Five original categories. Economics was added in 1969.",
             "Venue: Oslo for Peace, Stockholm for the rest."],
            "Two dates and one venue answer most Nobel questions.",
            "Why is the Nobel Prize in Economics different from the original prizes?",
            ["The original prizes came from the 1895 will.", "They were first given in 1901.",
             "Economics came later, as the Sveriges Riksbank prize."],
            "It was added in 1969."),
        pat("ga-caaw-p4", "Gallantry awards: wartime and peacetime", "common",
            "'The highest wartime gallantry award', 'the Ashoka Chakra is given for', or ordering the Chakras.",
            ["Wartime: Param Vir, Maha Vir, Vir Chakra.", "Peacetime: Ashoka, Kirti, Shaurya Chakra.",
             "Find the word 'wartime' or 'peacetime' in the question.",
             "With no qualifier, 'highest gallantry award' means Param Vir Chakra."],
            "Most wrong options come from the other ladder.",
            "What is India's highest peacetime gallantry award?",
            ["Peacetime points to the second ladder.", "Its top step is the Ashoka Chakra.",
             "Kirti and Shaurya Chakra follow it."],
            "The Ashoka Chakra"),
        pat("ga-caaw-p5", "Literature, film and world prizes", "common",
            "'The Jnanpith Award was first won by', 'the Dadasaheb Phalke Award relates to', or 'the Asian Nobel is'.",
            ["Jnanpith is literature: 1965, G. Sankara Kurup.", "Dadasaheb Phalke is cinema: 1969, Devika Rani.",
             "Magsaysay is the Asian Nobel: 1957, Manila.", "Booker is English fiction. International Booker is translation."],
            "Each prize has one field and one first, so matching settles it.",
            "The Ramon Magsaysay Award, called the 'Asian Nobel', is presented in which city?",
            ["It is an Asian award.", "It was instituted in 1957.", "It is presented in the Philippines' capital."],
            "Manila, Philippines"),
        pat("ga-caaw-p6", "Order awards by the year they began", "occasional",
            "'Arrange in chronological order', or 'which award is the oldest' among a list of Indian awards.",
            ["Write the year next to each award.",
             "Key years: Bharat Ratna and Padma 1954, Arjuna 1961, Jnanpith 1965, Phalke 1969, Dronacharya 1985.",
             "Sort from earliest to latest."],
            "Start years are fixed facts, so a sorted list gives the answer directly.",
            "Arrange by year of starting: 1. Jnanpith 2. Bharat Ratna 3. Dronacharya 4. Dadasaheb Phalke",
            ["Jnanpith 1965, Bharat Ratna 1954, Dronacharya 1985, Phalke 1969.",
             "Sorted: 1954, 1965, 1969, 1985."],
            "2, 1, 4, 3"),
    ],
)

# =====================================================================
SUBS["ca-sports"] = dict(
    concept=(
        "Every tournament question uses the same five details: host, motto or theme, mascot, champion, and India's highlight. "
        "Note these five for each event in your window. "
        "Learn each event's cycle, organiser and first edition once, because they never change."
    ),
    notes=r"""### How sports news is asked
Every sports question reuses five details.

1. Host country or city
2. Motto or theme
3. Mascot
4. Champion and runner-up
5. India's performance: medals, records, firsts

Note these five for every event in your window. Learn the **cycle** and **organiser** of each event once.

> **Rule:** The five details change each edition. The cycle, organiser and first edition never change.

### The recurring events and their cycles
A cycle is how often an event is held.

| Event | Cycle | Fixed facts |
|---|---|---|
| Summer Olympics | 4 years | Modern Games from 1896, Athens |
| Winter Olympics | 4 years, offset | First in 1924, Chamonix |
| Paralympics | With the Olympics | For athletes with disabilities |
| Commonwealth Games | 4 years | Began as British Empire Games, 1930, Hamilton |
| Asian Games | 4 years | First in 1951, New Delhi; run by the OCA |
| FIFA World Cup | 4 years | First in 1930, Uruguay |
| Cricket World Cup (ODI) | 4 years | First in 1975, England |
| T20 World Cup | 2 years | India won the first, in 2007 |
| Thomas Cup / Uber Cup | 2 years | Men's / women's badminton team events |
| IPL | Every year | BCCI's T20 league, from 2008 |
| Ranji Trophy | Every year | Indian first-class cricket (1934), named after Ranjitsinhji |
| Khelo India Games | Every year | From 2018; school and university levels |

> **Tip:** Only two items here run every two years: the T20 World Cup and the Thomas and Uber Cups.

### Olympic basics
The modern Olympics began at **Athens in 1896**. **Pierre de Coubertin** revived them.

- The **IOC** (International Olympic Committee) was founded in **1894**. Its HQ is at **Lausanne**.
- The motto is "Citius, Altius, Fortius - Communiter". It means faster, higher, stronger - together.
- "Communiter" (together) was added in **2021**.
- The symbol is **five interlocking rings**.

### India's permanent sports facts
- **1900 Paris:** India's first Olympics. **Norman Pritchard** won two athletics silvers.
- **Hockey:** eight Olympic golds. The run began at **1928 Amsterdam**. The last gold came at **1980 Moscow**.
- **Abhinav Bindra:** first individual Olympic gold, **2008**, 10 m air rifle.
- **Neeraj Chopra:** javelin gold at the Tokyo Games.
- **Cricket World Cup:** first win in **1983** under Kapil Dev at Lord's. Second in **2011** under M.S. Dhoni.
- **T20 World Cup:** India won the first edition, in **2007**.
- **Thomas Cup:** India's first win came in **2022**.

### Oldest and first
Exams like superlatives, which are words like "oldest" or "first".

| Superlative | Answer |
|---|---|
| Asia's oldest football tournament | Durand Cup, 1888 |
| Oldest tennis championship | Wimbledon, 1877 |
| Men's tennis team cup | Davis Cup |

> **Example:** "The Durand Cup is linked to which sport?" Football. It is Asia's oldest football cup.

### How to note a tournament
Write one line per event in your window.

*event, year, host, champion, India's highlight, any record*

A statement question usually swaps **one** item in this line. It is most often a wrong host city or a wrong champion. The other items stay true.

> **Watch:** Check each statement alone. One false detail makes that statement wrong, even if the rest is true.
""",
    tricks=[
        trick("Cycle split",
              "Every four years: Olympics, Winter Olympics, CWG, Asian Games, FIFA, ODI World Cup. Every two years: T20 World Cup, Thomas and Uber Cups. Every year: IPL, Ranji, Khelo India.",
              "How often is the T20 World Cup held?",
              ["The ODI World Cup is the four-yearly one.", "The T20 World Cup is in the two-year group."],
              "Every two years"),
        trick("First editions in date order",
              "Athens 1896, Chamonix 1924, Hamilton and Uruguay 1930, New Delhi 1951, England 1975.",
              "Which came first: the first Asian Games or the first Cricket World Cup?",
              ["Asian Games: 1951.", "Cricket World Cup: 1975."],
              "The first Asian Games (1951)"),
    ],
    mistakes=[
        mis("Mixing the two-year T20 World Cup with the four-year ODI World Cup.", "T20 is every two years. ODI is every four years."),
        mis("Putting the Thomas Cup under football or tennis.", "The Thomas Cup is men's badminton. The Uber Cup is women's badminton."),
        mis("Placing the first Asian Games in Bangkok.", "The first Asian Games were in New Delhi, 1951."),
        mis("Calling the Durand Cup a hockey or cricket event.", "It is football, Asia's oldest cup, from 1888."),
        mis("Saying India's first individual Olympic gold came in hockey.", "Hockey golds are team golds. Abhinav Bindra won the first individual gold in 2008."),
    ],
    revision=[
        "Note five per event: host, motto or theme, mascot, champion, India's highlight.",
        "Olympics 1896 Athens (Coubertin). IOC 1894, Lausanne. Winter Games 1924 Chamonix.",
        "CWG from 1930 Hamilton. Asian Games 1951 New Delhi. FIFA 1930 Uruguay.",
        "ODI World Cup from 1975; India won 1983 and 2011. T20 World Cup every two years; India won 2007.",
        "IPL 2008, Ranji 1934, Khelo India 2018. Thomas and Uber Cups are badminton.",
        "India: first Olympics 1900; eight hockey golds (1928-1980); Bindra 2008; Thomas Cup 2022.",
        "Durand Cup 1888 (football). Wimbledon 1877 (tennis). Davis Cup is men's tennis.",
    ],
    patterns=[
        pat("ga-casp-p1", "Tournament to sport or organiser", "very common",
            "'The Thomas Cup is related to which sport', 'the Ranji Trophy is linked to', or 'which body runs the IPL'.",
            ["Recall the cup and sport pairs: Thomas and Uber badminton, Davis tennis, Santosh football, Ranji cricket, Durand football.",
             "Recall organisers: IPL is BCCI; Asian Games is the OCA.",
             "Look for the option with a swapped sport."],
            "The wrong option is usually a real cup placed under the wrong sport.",
            "The Thomas Cup is associated with which sport?",
            ["It is a team event for men.", "Its women's version is the Uber Cup.", "Both are badminton."],
            "Men's badminton"),
        pat("ga-casp-p3", "Olympic facts", "very common",
            "'The modern Olympics began in', 'the IOC HQ is at', 'the Olympic motto is', or questions on rings and founder.",
            ["Modern Games: Athens, 1896, revived by Pierre de Coubertin.", "IOC: founded 1894, HQ at Lausanne.",
             "Motto: faster, higher, stronger - together. 'Together' added in 2021.", "Winter Games: first in 1924 at Chamonix."],
            "A handful of fixed Olympic facts covers most options.",
            "Where is the headquarters of the International Olympic Committee?",
            ["The IOC was founded in 1894.", "Its HQ is in Switzerland."],
            "Lausanne, Switzerland"),
        pat("ga-casp-p4", "India's permanent sports records", "very common",
            "'India's first individual Olympic gold', 'how many hockey golds', or 'India first won the Thomas Cup in'.",
            ["First Olympics: 1900 Paris, Norman Pritchard.", "Hockey: eight golds, 1928 to 1980.",
             "First individual gold: Abhinav Bindra, 2008.", "Cricket: 1983 ODI, 2007 T20, 2011 ODI. Thomas Cup: 2022."],
            "These India facts are settled history, so they return every year.",
            "Who won India's first individual Olympic gold medal?",
            ["Hockey golds were team golds.", "The first individual gold came in 2008.", "It was in 10 m air rifle."],
            "Abhinav Bindra (2008)"),
        pat("ga-casp-p2", "Cycles and first editions", "common",
            "'How often is the T20 World Cup held', 'the first Asian Games were held at', or 'the first Cricket World Cup was in'.",
            ["Sort the event into four-yearly, two-yearly or yearly.",
             "Recall the first edition: Olympics 1896, Winter 1924, CWG 1930, Asian Games 1951, FIFA 1930, ODI 1975.",
             "Match the year and host to the options."],
            "Cycles and first editions never change, so they are safe to learn once.",
            "Which city hosted the first Asian Games?",
            ["The first Asian Games were in 1951.", "They were held on Indian soil."],
            "New Delhi (1951)"),
        pat("ga-casp-p5", "Champion, host and mascot statements", "common",
            "Numbered statements that mix one wrong host, champion or sport into true sports facts.",
            ["Take each statement alone.", "Check the host city and champion first. These are swapped most often.",
             "Then check the sport and the organiser.", "Pick the option with only the true statements."],
            "Usually only one detail is planted wrong, so a careful check of each line finds it.",
            "Consider: 1. The IPL is conducted by the BCCI. 2. The Durand Cup is a hockey tournament. 3. Wimbledon is the oldest tennis championship. Which are correct?",
            ["1 is true: the IPL is BCCI's league.", "2 is false: the Durand Cup is football.",
             "3 is true: Wimbledon dates from 1877."],
            "1 and 3 only"),
        pat("ga-casp-p6", "Oldest and first tournaments", "occasional",
            "Words like 'oldest', 'first' or 'named after' with a tournament.",
            ["Durand Cup: Asia's oldest football cup, 1888.", "Wimbledon: oldest tennis championship, 1877.",
             "Ranji Trophy: first-class cricket, named after Ranjitsinhji."],
            "Superlatives are fixed facts and appear often in sports sets.",
            "Asia's oldest football tournament is which one?",
            ["It started in 1888.", "It is played in India."],
            "The Durand Cup"),
    ],
)
