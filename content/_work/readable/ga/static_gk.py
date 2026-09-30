"""Readable rewrite of General Awareness > Static GK (all 6 subtopics).

Facts are kept exactly as in the existing content. Only the wording and layout change.
Old pattern ids are kept; new ids continue each prefix (ga-ba-p6, ga-sp-p6, ...).
Run: python static_gk.py  (patches content/core/topics/ga/static-gk.json in place)
"""
import json
import re
from pathlib import Path

ROOT = Path(__file__).resolve().parents[3]
TOPIC = ROOT / "core" / "topics" / "ga" / "static-gk.json"


def pat(pid, name, freq, spot, steps, why, q, ex_steps, answer, formula=None):
    return {"id": pid, "name": name, "frequency": freq, "howToSpot": spot, "formula": formula,
            "steps": steps, "why": why, "example": {"q": q, "steps": ex_steps, "answer": answer}}


def mis(wrong, right):
    return {"wrong": wrong, "right": right}


SUBS = {}

# =====================================================================
# 1. Books & Authors
# =====================================================================
SUBS["books-authors"] = dict(
    concept=(
        "Book and author questions are pure matching. Learn the pairs in small groups: ancient texts, "
        "Mughal memoirs, freedom-era works, autobiographies, Booker winners and world classics. "
        "Each wrong option is usually a real author from the same group."
    ),
    notes=r"""### Ancient and classical texts
Most questions here ask one author for one famous book.

| Book | Author | Note |
|---|---|---|
| **Arthashastra** | Kautilya (Chanakya) | Statecraft and economy of the Mauryan age |
| **Rajatarangini** | Kalhana | Historical chronicle of Kashmir |
| **Abhijnana Shakuntalam** | Kalidasa | Most famous Sanskrit drama |
| **Mudrarakshasa** | Vishakhadatta | Story of Chanakya and Chandragupta |
| **Indica** | Megasthenes | Greek envoy's account of Mauryan India |
| **Harshacharita** | Banabhatta | Biography of Harshavardhana |
| **Panchatantra** | Vishnu Sharma | Fable collection |
| **Ramcharitmanas** | Tulsidas | Awadhi retelling of the Ramayana |

### Mughal-era chronicles
- **Baburnama** is Babur's own story. It is in Turkish and is the first autobiography of its kind in Indian history.
- **Akbarnama** and **Ain-i-Akbari** were written by Abul Fazl.
- **Tuzuk-i-Jahangiri** is Jahangir's own memoir.
- **Padshahnama** was written by Abdul Hamid Lahori. It covers Shah Jahan's reign.

> **Tip:** Wrong options swap authors inside the same period. Fix the century first, then pick the name.

### Freedom-era and modern works
| Book | Author |
|---|---|
| **Anandamath** (source of *Vande Mataram*) | Bankim Chandra Chattopadhyay |
| **Gitanjali** (Nobel 1913) | Rabindranath Tagore |
| **Hind Swaraj**, **My Experiments with Truth** | M.K. Gandhi |
| **Discovery of India**, **Glimpses of World History** | Jawaharlal Nehru |
| **Poverty and Un-British Rule in India** | Dadabhai Naoroji |
| **India Wins Freedom** | Maulana Abul Kalam Azad |
| **Annihilation of Caste** | B.R. Ambedkar |
| **Train to Pakistan** | Khushwant Singh |
| **The Guide**, **Malgudi Days**, **Swami and Friends** | R.K. Narayan |
| **A Suitable Boy** | Vikram Seth |

> **Watch:** *Vande Mataram* comes from *Anandamath*, not from Tagore. Tagore wrote *Jana Gana Mana*.

### Autobiographies and memoirs
| Book | Author |
|---|---|
| **Wings of Fire**, **Ignited Minds**, **India 2020** | A.P.J. Abdul Kalam |
| **Long Walk to Freedom** | Nelson Mandela |
| **The Story of My Life** | Helen Keller |
| **Autobiography of an Unknown Indian** | Nirad C. Chaudhuri |
| **Playing It My Way** | Sachin Tendulkar |
| **Sunny Days** | Sunil Gavaskar |
| **Straight from the Heart** | Kapil Dev |
| **The Race of My Life** | Milkha Singh |
| **Unbreakable** | M.C. Mary Kom |
| **Ace Against Odds** | Sania Mirza |
| **The Test of My Life** | Yuvraj Singh |
| **A Shot at History** | Abhinav Bindra |

### Booker Prize winners
| Book | Author | Year |
|---|---|---|
| **Midnight's Children** | Salman Rushdie | 1981 |
| **The God of Small Things** | Arundhati Roy | 1997 |
| **The Inheritance of Loss** | Kiran Desai | 2006 |
| **The White Tiger** | Aravind Adiga | 2008 |

*Midnight's Children* is also the 'Booker of Bookers'. Kiran Desai is the daughter of Anita Desai. Anita Desai was shortlisted several times but never won.

*Tomb of Sand* (*Ret Samadhi*) by Geetanjali Shree won the **International** Booker in 2022. Daisy Rockwell translated it.

### World classics
| Book | Author | Book | Author |
|---|---|---|---|
| War and Peace | Tolstoy | Crime and Punishment | Dostoevsky |
| Pride and Prejudice | Jane Austen | Hamlet, Macbeth | Shakespeare |
| Iliad, Odyssey | Homer | Don Quixote | Cervantes |
| One Hundred Years of Solitude | Marquez | The Old Man and the Sea | Hemingway |
| Animal Farm, 1984 | Orwell | The Godfather | Puzo |
| The Origin of Species | Darwin | Das Kapital | Karl Marx |
| The Wealth of Nations | Adam Smith | The Republic | Plato |
| Paradise Lost | Milton | The Canterbury Tales | Chaucer |
""",
    tricks=[
        {"title": "Booker ladder",
         "body": "Say it in order: Rushdie 81, Roy 97, Desai 06, Adiga 08. The books run Midnight's Children, God of Small Things, Inheritance of Loss, White Tiger. Geetanjali Shree (2022) won the International Booker, which is for translated fiction.",
         "example": {"q": "Who wrote *The White Tiger*, the 2008 Booker winner?",
                     "steps": ["Recall the ladder: 81, 97, 06, 08.", "The 2008 slot is the fourth book, *The White Tiger*."],
                     "answer": "Aravind Adiga"}},
        {"title": "Sports book hooks",
         "body": "Sunny Days is Sunil Gavaskar. Race of My Life is Milkha Singh, who ran races. Unbreakable is Mary Kom, the boxer. Ace Against Odds is Sania Mirza, the tennis player. Test of My Life is Yuvraj Singh, who fought cancer."},
    ],
    mistakes=[
        mis("Giving *Vande Mataram* to Tagore.", "It is from *Anandamath* by Bankim Chandra. Tagore wrote *Jana Gana Mana*."),
        mis("Saying Gandhi wrote *Unto This Last*.", "John Ruskin wrote it. Gandhi only paraphrased it in Gujarati as *Sarvodaya*."),
        mis("Giving *The Discovery of India* to another leader.", "Nehru wrote it in Ahmednagar Fort jail, 1942-46."),
        mis("Mixing Anita Desai with her daughter Kiran Desai.", "Kiran Desai won the Booker in 2006. Anita Desai never won."),
        mis("Treating the International Booker as the same prize.", "Geetanjali Shree won the International Booker in 2022, for a translated book."),
    ],
    revision=[
        "Kautilya - Arthashastra; Kalhana - Rajatarangini; Kalidasa - Shakuntalam; Megasthenes - Indica.",
        "Banabhatta - Harshacharita; Vishnu Sharma - Panchatantra; Tulsidas - Ramcharitmanas.",
        "Baburnama is Babur's own story; Akbarnama is by Abul Fazl; Tuzuk-i-Jahangiri is Jahangir's.",
        "Gandhi - Hind Swaraj and My Experiments with Truth; Nehru - Discovery of India; Tagore - Gitanjali (Nobel 1913).",
        "Booker: Rushdie 1981, Roy 1997, Kiran Desai 2006, Adiga 2008.",
        "Wings of Fire - Kalam; Long Walk to Freedom - Mandela; Playing It My Way - Tendulkar.",
    ],
    patterns=[
        pat("ga-ba-p1", "Ancient or medieval text and its author", "common",
            "The question names Arthashastra, Rajatarangini, Akbarnama or a Sanskrit drama and asks for the author.",
            ["Place the book in a period: ancient, Mauryan, Gupta or Mughal.",
             "Recall the pair from the tables above.",
             "Remove options whose author lived in a different age.",
             "Pick the one that remains."],
            "Wrong options are real authors from other periods, so time order removes them.",
            "Who wrote **Rajatarangini**, the historical chronicle of Kashmir?",
            ["Rajatarangini is a chronicle of Kashmir.", "Its author is Kalhana (12th century).", "Arthashastra is Kautilya's; Harshacharita is Banabhatta's."],
            "Kalhana"),
        pat("ga-ba-p2", "Freedom-era work and its author", "very common",
            "The stem names Hind Swaraj, Discovery of India, Anandamath or Gitanjali.",
            ["Link each leader to two books: Gandhi, Nehru, Tagore, Bankim.",
             "Match the title to its leader.",
             "Check the hint in the stem, such as Vande Mataram or Nobel 1913."],
            "Leaders are the usual distractors for each other, so a two-book link per leader settles it.",
            "**Anandamath**, the novel that gave the nation *Vande Mataram*, was written by which author?",
            ["Vande Mataram comes from Anandamath.", "Its author is Bankim Chandra Chattopadhyay.", "Discovery of India is Nehru's; Hind Swaraj is Gandhi's."],
            "Bankim Chandra Chattopadhyay"),
        pat("ga-ba-p3", "Autobiography and its author", "very common",
            "The stem says 'is the autobiography of' or asks who wrote Wings of Fire or Long Walk to Freedom.",
            ["Split the options into Indian leaders, sportspersons and foreign figures.",
             "Match Wings of Fire to Kalam, Long Walk to Freedom to Mandela.",
             "Match sports titles using the hooks: Sunny, Race, Unbreakable, Ace, Test.",
             "Remember Baburnama as the earliest autobiography linked to India."],
            "Most memoir titles hint at the writer's life or sport.",
            "**Long Walk to Freedom** is the autobiography of whom?",
            ["Long Walk to Freedom is a foreign memoir.", "Its author is Nelson Mandela.", "Wings of Fire is Kalam's; My Experiments with Truth is Gandhi's."],
            "Nelson Mandela"),
        pat("ga-ba-p4", "Booker Prize winners and their books", "common",
            "The stem names The White Tiger, Midnight's Children or The Inheritance of Loss.",
            ["Recall the ladder: Rushdie 81, Roy 97, Desai 06, Adiga 08.",
             "Match the book to its year and author.",
             "Reject Anita Desai as a winner. She was only shortlisted."],
            "Only four Indian-linked authors won the main Booker, so the ladder covers every case.",
            "Who is the author of **The White Tiger** (Booker Prize 2008)?",
            ["The 2008 winner is the fourth on the ladder.", "The book is The White Tiger.", "Its author is Aravind Adiga."],
            "Aravind Adiga"),
        pat("ga-ba-p5", "World classic and its author", "common",
            "The stem names War and Peace, One Hundred Years of Solitude, Don Quixote or The Republic.",
            ["Place the book by country: Russia, Greece, Spain, Britain or Latin America.",
             "Match it to the pair in the world classics table.",
             "Keep thinkers separate: Darwin, Marx and Adam Smith wrote non-fiction."],
            "Country clues remove most wrong options at once.",
            "**One Hundred Years of Solitude**, a landmark of magical realism, was written by whom?",
            ["It is a Latin American classic.", "Its author is Gabriel Garcia Marquez (Colombia).", "Don Quixote is Cervantes'; War and Peace is Tolstoy's."],
            "Gabriel Garcia Marquez"),
        pat("ga-ba-p6", "Modern Indian fiction", "occasional",
            "The stem names Train to Pakistan, The Guide, Malgudi Days or A Suitable Boy.",
            ["Recall the pairs: Khushwant Singh, R.K. Narayan, Vikram Seth.",
             "Use the setting hint: Train to Pakistan is a Partition novel; Malgudi is a fictional town.",
             "Reject Booker winners unless the stem mentions a prize."],
            "These books are famous but not prize winners, so a prize hint would mislead you.",
            "**Malgudi Days** is a work of which author?",
            ["Malgudi is a fictional town.", "Its creator is R.K. Narayan.", "Train to Pakistan is Khushwant Singh's."],
            "R.K. Narayan"),
    ],
)

# =====================================================================
# 2. Sports
# =====================================================================
SUBS["sports"] = dict(
    concept=(
        "Sports questions test four things: which trophy belongs to which game, which term belongs to which sport, "
        "how many players a side has, and Olympic facts. Learn each as a small table. "
        "The Olympic questions are the most frequent."
    ),
    notes=r"""### Trophy or cup and its sport
| Trophy | Sport |
|---|---|
| Ranji, Duleep, Irani, Deodhar, Vijay Hazare | Cricket (India) |
| The Ashes | Cricket (England v Australia) |
| Santosh Trophy | Football (states) |
| Durand Cup | Football (oldest in India, 1888) |
| Subroto Cup, I-League | Football |
| Aga Khan, Beighton, Dhyan Chand Trophy | Hockey |
| Rangaswami Cup | Hockey (national championship) |
| Sultan Azlan Shah Cup | Hockey (Malaysia) |
| Thomas Cup / Uber Cup / Sudirman Cup | Badminton (men / women / mixed) |
| Davis Cup / Billie Jean King Cup | Tennis (men / women) |
| Ryder Cup, Walker Cup | Golf |
| Swaythling Cup | Table tennis (men) |
| Ezra Cup | Polo |
| Stanley Cup | Ice hockey |
| Wightman Cup | Tennis (women, UK-USA, discontinued) |
| Ballon d'Or | Football (best player award) |

> **Tip:** Thomas is the man, Uber is the woman. Davis is for the dudes, Billie Jean King for women.

### Terms and their sport
- **Cricket:** googly, yorker, LBW, gully, cover drive, maiden over.
- **Hockey:** bully, penalty corner, dribble, scoop.
- **Tennis:** deuce, ace, love, smash, volley.
- **Badminton:** smash, drop shot. Love and deuce also appear in badminton scoring.
- **Golf:** birdie, eagle, bogey, caddie, tee.
- **Chess:** gambit, stalemate, castling, checkmate, en passant.
- **Kabaddi:** raid, bonus line. **Boxing:** punch, knock-out, uppercut.
- **Shooting:** bull's eye. **Volleyball:** spike, blocking.

### Players per side
| Players | Sport |
|---|---|
| 4 | Polo |
| 5 | Basketball |
| 6 | Volleyball, ice hockey |
| 7 | Kabaddi, water polo, netball, handball |
| 9 | Kho-kho (in the field), baseball |
| 11 | Cricket, football, hockey |
| 15 | Rugby union |

> **Rule:** Count up: basketball 5, volleyball 6, kabaddi 7. Then cricket, football and hockey are 11.

### Grand Slams and big tournaments
| Tournament | Surface or fact |
|---|---|
| Australian Open | Hard court |
| French Open (Roland Garros) | Clay |
| Wimbledon | Grass; oldest, since 1877 |
| US Open | Hard court |

The first FIFA World Cup was in **1930** in Uruguay. It is held every four years. The first Cricket World Cup was in **1975** in England, and West Indies won it.

### The Olympics
| Fact | Answer |
|---|---|
| First modern Olympics | 1896, Athens |
| Reviver | Pierre de Coubertin (IOC founded 1894, Paris) |
| Motto | Citius, Altius, Fortius (Faster, Higher, Stronger) |
| Rings | Five, for five continents |
| Marathon | 42.195 km |
| India's first appearance | 1900 Paris, Norman Pritchard, two athletics silvers |
| First hockey gold | 1928 Amsterdam (first of 8) |
| First individual medal | K.D. Jadhav, wrestling, 1952 Helsinki |
| First individual gold | Abhinav Bindra, 10 m air rifle, 2008 Beijing |
| Javelin gold | Neeraj Chopra, 87.58 m, Tokyo 2020 |

The word 'Communiter' (Together) was added to the motto in 2021. The ring colours are blue, yellow, black, green and red. Paris 2024 gave India 6 medals. Manu Bhaker won two bronzes there. Neeraj Chopra won silver. Next come Los Angeles 2028 and Brisbane 2032.

### Indian venues and milestones
- **Eden Gardens** is in Kolkata. **Wankhede** is in Mumbai. **Chepauk (M.A. Chidambaram)** is in Chennai.
- **Narendra Modi Stadium** (Motera, Ahmedabad) is the world's largest cricket stadium.
- **Salt Lake (Vivekananda Yuba Bharati Krirangan)**, Kolkata, is a football ground.
- **Major Dhyan Chand National Stadium**, Delhi, is a hockey ground.
- Viswanathan Anand became India's first chess Grandmaster in 1988. The Ranji Trophy began in 1934.
""",
    tricks=[
        {"title": "Badminton cups",
         "body": "Thomas Cup is the men's team event. Uber Cup is the women's team event. Sudirman Cup is mixed. In tennis, Davis is for men and Billie Jean King is for women.",
         "example": {"q": "India won the Thomas Cup for the first time in 2022. Which sport is this?",
                     "steps": ["Thomas Cup is the men's team event.", "It belongs to badminton."],
                     "answer": "Badminton"}},
        {"title": "Team size ladder",
         "body": "Count up from five: basketball 5, volleyball 6, kabaddi 7. Cricket, football and hockey are 11. Only polo (4) and rugby union (15) sit far from this band."},
    ],
    mistakes=[
        mis("Calling the Santosh Trophy a cricket event.", "Santosh Trophy is football. Ranji Trophy is cricket."),
        mis("Placing Roland Garros on grass.", "Roland Garros is clay. Wimbledon is the Grand Slam on grass."),
        mis("Calling Abhinav Bindra India's first Olympic gold.", "He won the first individual gold. Hockey gave team golds from 1928."),
        mis("Mixing up kabaddi (7) and kho-kho (9).", "Kabaddi fields 7 on the mat. Kho-kho has 9 in the field."),
        mis("Putting the Uber Cup under men's badminton.", "Uber is women's. Thomas is men's. Sudirman is mixed."),
    ],
    revision=[
        "Cricket: Ranji, Duleep, Irani; the Ashes is England v Australia; first Cricket World Cup 1975.",
        "Football: Santosh (states), Durand (1888); FIFA World Cup began 1930 in Uruguay.",
        "Badminton: Thomas men, Uber women, Sudirman mixed. Tennis: Davis men, Billie Jean King women.",
        "Team sizes: polo 4, basketball 5, volleyball 6, kabaddi 7, kho-kho 9, rugby 15.",
        "Olympics: 1896 Athens, Coubertin, marathon 42.195 km, five rings for five continents.",
        "India: Pritchard 1900, hockey gold 1928, Jadhav 1952, Bindra 2008, Neeraj Chopra 2020.",
    ],
    patterns=[
        pat("ga-sp-p1", "Trophy or cup and its sport", "very common",
            "The stem names Santosh, Durand, Thomas, Davis or Ryder and asks for the sport.",
            ["Group the cup by sport using the trophy table.",
             "Use the men, women and mixed rule for Thomas, Uber, Sudirman and Davis.",
             "Use the odd ones: Ryder is golf, Swaythling is table tennis, Ezra is polo.",
             "Reject options from a different sport."],
            "Trophy names carry no clue, so the table is the only way in.",
            "The **Durand Cup**, the oldest football tournament of India, was first played in which year?",
            ["The Durand Cup is a football tournament.", "It began at Shimla in 1888.", "That is 42 years before the first FIFA World Cup."],
            "1888"),
        pat("ga-sp-p2", "Sporting term and its sport", "very common",
            "The stem lists googly, yorker, gambit, deuce or bull's eye.",
            ["Read the term.", "Match it to the sport list in the notes.",
             "Watch for shared words: love and smash appear in tennis and badminton.",
             "Pick the sport where the term is unique."],
            "Every term belongs to one core sport, and a few are shared.",
            "The terms '**googly**' and '**yorker**' belong to which sport?",
            ["Both are ways of bowling.", "They belong to cricket.", "Bully and penalty corner are hockey; birdie and bogey are golf."],
            "Cricket"),
        pat("ga-sp-p3", "Number of players per side", "common",
            "The stem asks how many play in a kabaddi, water polo or polo team.",
            ["Recall the ladder: 5, 6, 7 for basketball, volleyball, kabaddi.",
             "Add the sevens: kabaddi, water polo, netball, handball.",
             "Remember the odd ones: polo 4 and rugby 15."],
            "Most sports sit in a narrow band, so only a few numbers need care.",
            "How many players does a **kabaddi** team field on the mat?",
            ["Kabaddi sits at 7 on the ladder.", "Kho-kho is 9, basketball 5 and volleyball 6."],
            "Seven"),
        pat("ga-sp-p4", "Grand Slams and major tournaments", "common",
            "The stem asks which Grand Slam is on grass or clay, or the oldest tennis tournament.",
            ["List the year order: Australian, French, Wimbledon, US.",
             "Attach the surface: hard, clay, grass, hard.",
             "Remember Wimbledon as the oldest, since 1877.",
             "For World Cups: FIFA 1930 Uruguay, Cricket 1975 England."],
            "The surface is the fact examiners ask about most.",
            "The **Australian Open** and the **US Open** are played on which type of surface?",
            ["Recall the order: hard, clay, grass, hard.", "The first and last are hard courts."],
            "Hard courts"),
        pat("ga-sp-p5", "Olympics: history, symbols and India's milestones", "very common",
            "The stem asks about the first modern Olympics, the motto, the rings, or an Indian first.",
            ["Anchor 1896 Athens and Pierre de Coubertin.",
             "Recall the motto and the five rings for five continents.",
             "Line up India's firsts: 1900, 1928, 1952, 2008, 2020.",
             "Marathon distance is 42.195 km."],
            "The Indian firsts follow one time line, so recall it in order.",
            "The five interlocking rings of the Olympic flag represent what?",
            ["There are five rings.", "They stand for the five continents united by sport.", "Coubertin designed them."],
            "The five continents"),
        pat("ga-sp-p6", "Indian stadiums and venues", "occasional",
            "The stem names Eden Gardens, Motera, Wankhede or Salt Lake and asks the city or sport.",
            ["Match each stadium to its city.", "Note the sport: Salt Lake is football, Dhyan Chand Stadium is hockey.",
             "Remember Motera as the world's largest cricket stadium."],
            "City and sport together remove most wrong options.",
            "The **Narendra Modi Stadium**, the world's largest cricket stadium, is in which city?",
            ["It is also called Motera.", "Motera is in Ahmedabad."],
            "Ahmedabad"),
    ],
)

# =====================================================================
# 3. Awards & Honours
# =====================================================================
SUBS["awards"] = dict(
    concept=(
        "Award questions ask who got the first one, what a prize is for, or which year it began. "
        "Learn four groups: civilian honours, gallantry awards, Nobel laureates and sports awards. "
        "Then add the big international prizes by field."
    ),
    notes=r"""### Civilian honours
The order of precedence is **Bharat Ratna, Padma Vibhushan, Padma Bhushan, Padma Shri**. All four began in **1954**. The Padma awards are announced on Republic Day eve.

| Bharat Ratna fact | Answer |
|---|---|
| First three (1954) | C. Rajagopalachari, S. Radhakrishnan, C.V. Raman |
| First woman | Indira Gandhi (1971) |
| First posthumous | Lal Bahadur Shastri (1966) |
| First sportsperson | Sachin Tendulkar (2014) |
| First non-Indians | Khan Abdul Ghaffar Khan (1987), Nelson Mandela (1990) |

Normally at most three Bharat Ratnas are given in a year.

> **Tip:** Remember RRR for 1954: Rajagopalachari, Radhakrishnan, Raman.

### Gallantry awards
The **Param Vir Chakra** (1950) is the highest wartime gallantry award. Below it come the Maha Vir Chakra and the Vir Chakra. The **Ashoka Chakra** (1952) is its peacetime counterpart.

The first Param Vir Chakra went to **Major Somnath Sharma** (1947, posthumous).

### Nobel Prizes
The prizes began in 1901. The categories are Physics, Chemistry, Medicine, Literature and Peace. Economics was added in 1969 by Sweden's central bank, not under Nobel's will.

| Person | Year | Field |
|---|---|---|
| Rabindranath Tagore | 1913 | Literature (first Asian) |
| C.V. Raman | 1930 | Physics |
| Hargobind Khorana | 1968 | Medicine |
| Mother Teresa | 1979 | Peace |
| Amartya Sen | 1998 | Economics |
| V. Ramakrishnan | 2009 | Chemistry |
| Kailash Satyarthi | 2014 | Peace (with Malala Yousafzai) |
| Abhijit Banerjee | 2019 | Economics |

**Marie Curie** was the first woman laureate (Physics 1903). She is the only one to win in two sciences (Chemistry 1911).

### Literary and arts awards
| Award | Started | Key fact |
|---|---|---|
| Jnanpith | 1965 | Highest literary award; first winner G. Sankara Kurup (Malayalam, *Odakkuzhal*) |
| Sahitya Akademi | 1955 | Literature, 24 languages |
| Dadasaheb Phalke | 1969 | Highest cinema honour; first winner Devika Rani |

### International prizes by field
- **Booker:** English fiction; first awarded 1969 to P.H. Newby.
- **Pulitzer (1917):** American journalism and letters.
- **Oscar (Academy Award):** film. **Grammy:** music. **Pritzker:** architecture.
- **Abel Prize (2003, Norway)** and **Fields Medal:** mathematics. The Fields Medal is for work done under 40, every four years.
- **Turing Award:** computer science. **Kalinga Prize:** popularising science (UNESCO).
- **Ramon Magsaysay (1958):** the 'Asian Nobel', named after a Philippine president.
- **Gandhi Peace Prize (1995):** set up by India; first won by Julius Nyerere of Tanzania.

### Sports awards of India
| Award | Started | For |
|---|---|---|
| Major Dhyan Chand Khel Ratna | 1991-92 | Highest sports honour |
| Arjuna | 1961 | Sportspersons |
| Dronacharya | 1985 | Coaches |
| Dhyan Chand Award | 2002 | Lifetime achievement in sport |
| MAKA Trophy | - | Best university in sports |

The Khel Ratna was renamed from Rajiv Gandhi Khel Ratna in **2021**. Its first winner was **Viswanathan Anand**.

> **Watch:** Dronacharya is for coaches. Arjuna is for players.
""",
    tricks=[
        {"title": "RRR 1954",
         "body": "The first Bharat Ratnas were Rajagopalachari, Radhakrishnan and Raman. Three Rs, one year: 1954.",
         "example": {"q": "Who was NOT among the first Bharat Ratna recipients in 1954? (a) C.V. Raman (b) S. Radhakrishnan (c) Jawaharlal Nehru (d) C. Rajagopalachari",
                     "steps": ["The 1954 trio is the three Rs.", "Nehru is not among them; he received it in 1955."],
                     "answer": "(c) Jawaharlal Nehru"}},
        {"title": "Award decade ladder",
         "body": "1950s: Bharat Ratna (1954). 1960s: Arjuna (1961), Jnanpith (1965), Phalke (1969). 1980s: Dronacharya (1985). 1990s: Khel Ratna (1991-92)."},
    ],
    mistakes=[
        mis("Giving Dronacharya to players.", "Dronacharya is for coaches. Arjuna is for players."),
        mis("Naming Prithviraj Kapoor as the first Phalke winner.", "Devika Rani was first. Prithviraj Kapoor received it in 1971, after his death."),
        mis("Mixing the Khel Ratna with the Dhyan Chand Award.", "The Khel Ratna was renamed in 2021. The Dhyan Chand Award for lifetime work is separate."),
        mis("Saying Nehru got a Bharat Ratna in 1954.", "The 1954 trio was Rajagopalachari, Radhakrishnan and Raman."),
        mis("Using the Param Vir Chakra for peacetime bravery.", "Param Vir Chakra is wartime. Ashoka Chakra is its peacetime counterpart."),
    ],
    revision=[
        "1954: Bharat Ratna and the three Padma awards; first trio Rajagopalachari, Radhakrishnan, Raman.",
        "Param Vir Chakra: first to Major Somnath Sharma (posthumous); peacetime equal is Ashoka Chakra.",
        "Nobel: Tagore 1913, Raman 1930, Khorana 1968, Mother Teresa 1979, Sen 1998, Ramakrishnan 2009, Satyarthi 2014, Banerjee 2019.",
        "Jnanpith 1965 (Kurup); Phalke 1969 (Devika Rani); Magsaysay 1958; Gandhi Peace Prize 1995 (Nyerere).",
        "Khel Ratna first winner Anand; Dronacharya is for coaches; Arjuna is for players.",
        "Fields Medal and Abel Prize are for mathematics; Turing is for computer science.",
    ],
    patterns=[
        pat("ga-aw-p1", "Bharat Ratna: firsts and recipients", "very common",
            "The stem asks for the first Bharat Ratna recipient, or the first woman, posthumous or sportsperson.",
            ["Anchor 1954 and the RRR trio.", "Recall the firsts: woman Indira Gandhi (1971), posthumous Shastri (1966), sportsperson Tendulkar (2014).",
             "Remember the order of precedence: Bharat Ratna, Padma Vibhushan, Padma Bhushan, Padma Shri."],
            "Each 'first' has exactly one name, so recall by category.",
            "Who was the **first sportsperson** to receive the Bharat Ratna?",
            ["Bharat Ratna to a sportsperson came in 2014.", "The recipient was Sachin Tendulkar.", "He was announced with C.N.R. Rao and was its youngest recipient at 40."],
            "Sachin Tendulkar"),
        pat("ga-aw-p2", "Nobel Prize: categories and Indian laureates", "very common",
            "The stem asks for the first Indian laureate, a laureate by year, or when Economics was added.",
            ["Recall the table in year order.", "Match field to name: Tagore Literature, Raman Physics, Khorana Medicine.",
             "For Peace: Mother Teresa 1979, Satyarthi 2014.", "Economics: Sen 1998, Banerjee 2019; the prize dates from 1969."],
            "Year and field together fix each laureate.",
            "Who was the **first Indian** to win a Nobel Prize?",
            ["The earliest Indian laureate is in 1913.", "Tagore won the Literature prize that year for Gitanjali.", "Raman's Physics prize came in 1930."],
            "Rabindranath Tagore"),
        pat("ga-aw-p3", "Gallantry awards: hierarchy and firsts", "common",
            "The stem asks for the highest gallantry award, the first PVC or the peacetime equivalent.",
            ["Write the wartime ladder: Param Vir Chakra, Maha Vir Chakra, Vir Chakra.",
             "Recall the first PVC: Major Somnath Sharma (1947, posthumous).",
             "Pair the peacetime award: Ashoka Chakra."],
            "The ladder gives the answer to both rank and equivalence questions.",
            "The **Ashoka Chakra** is awarded for what?",
            ["It is the peacetime counterpart of the Param Vir Chakra.", "It honours bravery or self-sacrifice away from the battlefield."],
            "Peacetime gallantry"),
        pat("ga-aw-p4", "Literary, arts and international prizes", "very common",
            "The stem asks the highest literary award, the first Phalke winner, or the field of Abel, Fields or Turing.",
            ["India first: Jnanpith 1965 (Kurup), Phalke 1969 (Devika Rani).",
             "Then world prizes: Booker, Pulitzer, Magsaysay, Gandhi Peace Prize.",
             "Then specialist prizes: Abel and Fields for mathematics, Turing for computer science."],
            "Field and year make each prize unique.",
            "The **Fields Medal**, awarded every four years, honours achievement in which field?",
            ["The Fields Medal is a mathematics prize.", "It goes only to mathematicians under 40.", "The Abel Prize (2003) is mathematics' other big award."],
            "Mathematics"),
        pat("ga-aw-p5", "Sports awards of India", "common",
            "The stem asks the highest sporting honour, the first Khel Ratna, or what Arjuna and Dronacharya are for.",
            ["Recall the Khel Ratna, first winner Anand, renamed 2021.",
             "Pair Dronacharya with coaches and Arjuna with players.",
             "Add Dhyan Chand Award for lifetime work and MAKA Trophy for the best university."],
            "Each award has one audience: player, coach or institution.",
            "The **Arjuna Award** (instituted 1961) is given for what?",
            ["Arjuna is for players.", "It honours consistent outstanding performance by sportspersons.", "The Dronacharya Award honours their coaches."],
            "Outstanding performance by sportspersons"),
        pat("ga-aw-p6", "Start year of an award", "common",
            "The stem asks in which year Jnanpith, Phalke, Magsaysay or the Khel Ratna began.",
            ["Recall the decade ladder: 1950s, 1960s, 1980s, 1990s.",
             "Match the exact year: Jnanpith 1965, Phalke 1969, Magsaysay 1958, Gandhi Peace Prize 1995.",
             "Cross-check with the field, such as literature or cinema."],
            "The decade ladder narrows four options to one.",
            "The **Dadasaheb Phalke Award** for cinema was instituted in which year?",
            ["Phalke fits the 1960s rung.", "It began in 1969.", "Its first winner was Devika Rani."],
            "1969"),
    ],
)

# =====================================================================
# 4. Important Days
# =====================================================================
SUBS["important-days"] = dict(
    concept=(
        "Days questions ask for a date, a person or a reason. Most national days honour a birth anniversary. "
        "Most world days follow a founding date or a UN decision. Learn them by month and by person."
    ),
    notes=r"""### Days that honour a person
| Date | Day | Person or reason |
|---|---|---|
| 12 Jan | National Youth Day | Swami Vivekananda |
| 30 Jan | Martyrs' Day | Gandhi's assassination |
| 28 Feb | National Science Day | Raman effect (1928) |
| 1 Jul | National Doctors' Day | Dr B.C. Roy |
| 29 Aug | National Sports Day | Major Dhyan Chand |
| 5 Sep | Teachers' Day | Dr S. Radhakrishnan |
| 15 Sep | Engineers' Day | Sir M. Visvesvaraya |
| 2 Oct | Gandhi Jayanti | Mahatma Gandhi |
| 31 Oct | National Unity Day | Sardar Patel |
| 14 Nov | Children's Day | Jawaharlal Nehru |
| 22 Dec | National Mathematics Day | Srinivasa Ramanujan |
| 23 Dec | Kisan Diwas | Chaudhary Charan Singh |
| 25 Dec | Good Governance Day | A.B. Vajpayee |

Mathematics Day has been observed since 2012.

> **Watch:** Science Day marks the Raman effect, not Raman's birthday.

### National days with their own reason
- **24 Jan:** National Girl Child Day.
- **25 Jan:** National Voters' Day. The Election Commission was founded on 25 Jan 1950.
- **26 Jan:** Republic Day. The Constitution came into force in 1950.
- **11 May:** National Technology Day, for the Pokhran tests of 11 May 1998.
- **14 Sep:** Hindi Diwas. Hindi was adopted as the official language in 1949.
- **15 Aug:** Independence Day.
- **26 Nov:** Constitution Day (Samvidhan Divas). The Constitution was adopted in 1949.

### Defence forces days
| Day | Date | Reason |
|---|---|---|
| Army Day | 15 Jan | K.M. Cariappa became the first Indian Commander-in-Chief in 1949 |
| Air Force Day | 8 Oct | IAF founded in 1932 |
| Navy Day | 4 Dec | Operation Trident, 1971 |

### International days
| Date | Day |
|---|---|
| 8 Mar | International Women's Day |
| 22 Mar | World Water Day |
| 7 Apr | World Health Day (WHO founded 1948) |
| 22 Apr | Earth Day |
| 1 May | International Labour Day |
| 5 Jun | World Environment Day |
| 21 Jun | International Day of Yoga (first observed 2015, proposed by India) |
| 29 Jul | International Tiger Day |
| 12 Aug | International Youth Day |
| 8 Sep | International Literacy Day |
| 16 Sep | World Ozone Day (Montreal Protocol) |
| 16 Oct | World Food Day (FAO founded 1945) |
| 24 Oct | United Nations Day (UN founded 1945) |
| 1 Dec | World AIDS Day |
| 10 Dec | Human Rights Day (UDHR 1948) |

### The two constitution dates
Adoption and enforcement are different days.

- **26 November 1949:** adopted. This is Constitution Day.
- **26 January 1950:** came into force. This is Republic Day.

The date 26 January honours the 1930 Purna Swaraj declaration. Independence Day, 15 August 1947, is a separate event.

> **Tip:** Feb and Nov anchors: 28 Feb is the Raman effect, 26 Nov is adoption.
""",
    tricks=[
        {"title": "Birthday days",
         "body": "Pair the day with the person. 12 Jan Vivekananda, 29 Aug Dhyan Chand, 5 Sep Radhakrishnan, 15 Sep Visvesvaraya, 14 Nov Nehru, 22 Dec Ramanujan.",
         "example": {"q": "National Mathematics Day (22 December) honours whom?",
                     "steps": ["Recall the person list.", "22 Dec pairs with Srinivasa Ramanujan, born 22 Dec 1887."],
                     "answer": "Srinivasa Ramanujan"}},
        {"title": "Two constitution anchors",
         "body": "26 Nov 1949 is adoption, so it is Constitution Day. 26 Jan 1950 is enforcement, so it is Republic Day."},
    ],
    mistakes=[
        mis("Calling 26 January Constitution Day.", "Constitution Day is 26 November (adoption). Republic Day is 26 January (enforcement)."),
        mis("Saying Science Day is Raman's birthday.", "28 Feb marks the discovery of the Raman effect in 1928. His birthday is 7 Nov."),
        mis("Swapping Teachers' Day and Engineers' Day.", "Teachers' Day, 5 Sep, is Radhakrishnan. Engineers' Day, 15 Sep, is Visvesvaraya."),
        mis("Mixing Hindi Diwas with a Constitution date.", "Hindi Diwas is 14 Sep, for the 1949 official-language decision."),
        mis("Mixing up the three forces days.", "Army 15 Jan, Air Force 8 Oct, Navy 4 Dec."),
    ],
    revision=[
        "Birth-linked: 12 Jan Vivekananda, 1 Jul B.C. Roy, 29 Aug Dhyan Chand, 5 Sep Radhakrishnan, 15 Sep Visvesvaraya, 14 Nov Nehru, 22 Dec Ramanujan.",
        "28 Feb Science (Raman 1928); 11 May Technology (Pokhran 1998); 25 Jan Voters; 14 Sep Hindi.",
        "7 Apr Health (WHO 1948); 16 Oct Food (FAO 1945); 24 Oct UN (1945); 10 Dec Human Rights (UDHR 1948).",
        "Yoga 21 June, first observed 2015, proposed by India; Earth Day 22 April; Water 22 March.",
        "Army 15 Jan, Air Force 8 Oct, Navy 4 Dec (Operation Trident).",
        "Adopted 26 Nov 1949; in force 26 Jan 1950.",
    ],
    patterns=[
        pat("ga-id-p1", "Day and the person it honours", "very common",
            "The stem asks whose birth anniversary Sports Day, Teachers' Day, Youth Day or Mathematics Day marks.",
            ["Find the profession in the day's name.", "Look up the person-date row in the table.",
             "Remember 30 Jan as Martyrs' Day, the day Gandhi was assassinated (1948)."],
            "Most national days honour one person, so the profession gives it away.",
            "**National Mathematics Day** (22 December) marks the birth anniversary of whom?",
            ["The day belongs to mathematics.", "It marks Srinivasa Ramanujan's birth (22 December 1887).", "It has been observed since 2012."],
            "Srinivasa Ramanujan"),
        pat("ga-id-p2", "National day and its date", "very common",
            "The stem names Voters' Day, Technology Day, Hindi Diwas or Unity Day and asks the date or reason.",
            ["Group January days: 24 Girl Child, 25 Voters, 26 Republic.",
             "Anchor 11 May with Pokhran 1998 and 14 Sep with Hindi 1949.",
             "Anchor 31 Oct with Sardar Patel and 28 Feb with the Raman effect."],
            "Each date links to one event, so recall the event.",
            "**National Unity Day**, on 31 October, celebrates the birth anniversary of whom?",
            ["31 October is Sardar Vallabhbhai Patel's birthday.", "He is the 'Iron Man' who integrated the princely states."],
            "Sardar Vallabhbhai Patel"),
        pat("ga-id-p3", "International day and its date", "very common",
            "The stem names World Water, Health, Environment, Food or Yoga Day.",
            ["Split the year: spring (Mar-May), mid-year (Jun-Aug), year-end (Oct-Dec).",
             "Match the day: 22 Mar Water, 7 Apr Health, 5 Jun Environment, 21 Jun Yoga.",
             "Match year-end days: 16 Oct Food, 24 Oct UN, 1 Dec AIDS, 10 Dec Human Rights."],
            "Sorting by season keeps twenty dates manageable.",
            "**World Health Day** is observed on 7 April because of which event?",
            ["World Health Day follows the WHO.", "The World Health Organization was founded on 7 April 1948."],
            "WHO was founded on 7 April 1948"),
        pat("ga-id-p4", "Defence forces days", "common",
            "The stem asks the date of Army, Navy or Air Force Day, or the Operation Trident link.",
            ["Recall Army 15 Jan (Cariappa, 1949).", "Recall Air Force 8 Oct (IAF founded 1932).",
             "Recall Navy 4 Dec (Operation Trident, 1971)."],
            "There are only three dates, each with one reason.",
            "**Indian Navy Day** is celebrated on which date?",
            ["Navy Day recalls Operation Trident of 1971.", "It falls on 4 December.", "Army Day is 15 Jan and Air Force Day is 8 Oct."],
            "4 December"),
        pat("ga-id-p5", "Republic-era constitutional days", "occasional",
            "The stem asks why 26 January is Republic Day, or when Samvidhan Divas falls.",
            ["Separate adoption (26 Nov 1949) from enforcement (26 Jan 1950).",
             "Link 26 Jan to the 1930 Purna Swaraj declaration.",
             "Add 25 Jan: Voters' Day, since the Election Commission began on 25 Jan 1950."],
            "Two close dates are the usual trap, so state both.",
            "Why is **Republic Day** celebrated on 26 January?",
            ["The Constitution came into force on 26 January 1950.", "The date honours the 1930 Purna Swaraj declaration."],
            "The Constitution came into force on 26 January 1950"),
    ],
)

# =====================================================================
# 5. National Symbols & Firsts
# =====================================================================
SUBS["national-symbols-firsts"] = dict(
    concept=(
        "This topic has two halves. The first is India's national symbols, with the flag, emblem, anthem and song. "
        "The second is a list of famous firsts, especially women's firsts. "
        "Each fact has one clean answer, so learn the pairs."
    ),
    notes=r"""### National symbols
| Symbol | Identity |
|---|---|
| Animal | Tiger (1973) |
| Bird | Peacock (declared 1963) |
| Flower | Lotus |
| Tree | Banyan |
| Fruit | Mango |
| River | Ganga (2008) |
| Aquatic animal | Gangetic river dolphin (2009) |
| Heritage animal | Elephant (2010) |
| Calendar | Saka calendar (used with the Gregorian since 1957) |
| Gazette | Gazette of India |

### The flag
The flag was designed on the lines suggested by **Pingali Venkayya**. It was adopted on **22 July 1947**.

- The ratio of length to width is **3 : 2**.
- The centre has a navy-blue **Ashoka Chakra with 24 spokes**. It comes from the Sarnath Lion Capital.
- Saffron means courage and sacrifice. White means truth and peace. Green means faith and prosperity.

The Flag Code of India was liberalised in 2002, and again in 2021, to let the public hoist the flag.

### Emblem, anthem and song
| Item | Details |
|---|---|
| State emblem | Lion Capital of Ashoka at Sarnath; adopted 26 Jan 1950 |
| Motto | *Satyameva Jayate* ('truth alone triumphs'), from the Mundaka Upanishad |
| National anthem | *Jana Gana Mana* by Tagore; adopted 24 Jan 1950; about 52 seconds |
| National song | *Vande Mataram* by Bankim Chandra Chattopadhyay, from *Anandamath* |

*Vande Mataram* was first sung at the 1896 Congress session.

> **Rule:** Emblem 26 Jan 1950, anthem 24 Jan 1950. The anthem comes two days before the emblem.

### Firsts among women
| First | Person |
|---|---|
| Governor of a state | Sarojini Naidu (UP, 1947) |
| Chief Minister | Sucheta Kripalani (UP, 1963) |
| Prime Minister | Indira Gandhi (1966) |
| President of India | Pratibha Patil (2007) |
| Lok Sabha Speaker | Meira Kumar (2009) |
| IPS officer | Kiran Bedi (1972) |
| Supreme Court judge | M. Fathima Beevi (1989) |
| Indian-born woman in space | Kalpana Chawla (1997) |
| Indian woman on Everest | Bachendri Pal (1984) |
| Indian woman to swim the English Channel | Arati Saha (1959) |
| INC President | Annie Besant (1917); first Indian woman Sarojini Naidu (1925) |

> **Tip:** Sarojini governs, Sucheta chiefs. Both come from UP.

### Firsts in public office
| First | Person |
|---|---|
| President / Vice-President | Rajendra Prasad / S. Radhakrishnan |
| Prime Minister | Jawaharlal Nehru (longest-serving) |
| Indian Governor-General | C. Rajagopalachari (the only Indian one) |
| Chief Justice of India | H.J. Kania |
| Chief Election Commissioner | Sukumar Sen |
| Field Marshal | Sam Manekshaw (1973) |

### Firsts in science and infrastructure
- **Rakesh Sharma** was the first Indian in space (1984, Soyuz T-11).
- **Aryabhata** was the first satellite (1975). **Mangalyaan**, the Mars orbiter, flew in 2013.
- **Chandrayaan-3** soft-landed near the lunar south pole on 23 August 2023. That date is National Space Day.
- **Raja Harishchandra** (1913, Dadasaheb Phalke) was the first feature film.
- The first passenger railway ran from Bombay to Thane on 16 April 1853.
- The first census was in 1872, and regular from 1881. The first Five-Year Plan began in 1951. The first bank was Bank of Hindustan (1770).
""",
    tricks=[
        {"title": "Women firsts hook",
         "body": "Sarojini Governs, Sucheta Chiefs. Governor is Sarojini Naidu (1947). Chief Minister is Sucheta Kripalani (1963). Both from UP.",
         "example": {"q": "Who was India's first woman Chief Minister?",
                     "steps": ["Chief Minister links to Sucheta.", "She held office in Uttar Pradesh in 1963."],
                     "answer": "Sucheta Kripalani"}},
        {"title": "Flag numbers",
         "body": "Length to width is 3 : 2. The chakra has 24 spokes. The designer is Pingali Venkayya."},
    ],
    mistakes=[
        mis("Placing *Satyameva Jayate* in the Rigveda.", "It comes from the Mundaka Upanishad."),
        mis("Calling the whale shark the national aquatic animal.", "The national aquatic animal is the Gangetic river dolphin."),
        mis("Calling Rajagopalachari the first Governor-General of independent India.", "Mountbatten was first. Rajagopalachari was the first and last Indian one."),
        mis("Giving Sarojini Naidu the first Chief Minister post.", "She was the first woman Governor. Sucheta Kripalani was the first woman Chief Minister."),
        mis("Swapping the anthem and emblem dates.", "Anthem 24 Jan 1950. Emblem 26 Jan 1950."),
    ],
    revision=[
        "Tiger, peacock, lotus, banyan, mango, Ganga, Gangetic dolphin, elephant, Saka calendar.",
        "Flag: Venkayya, 22 July 1947, 3 : 2, 24 spokes. Emblem: Sarnath, 26 Jan 1950, Mundaka Upanishad.",
        "Anthem adopted 24 Jan 1950 (Tagore). Vande Mataram is by Bankim Chandra, from Anandamath.",
        "Women firsts: Naidu (Governor), Kripalani (CM), Patil (President), Bedi (IPS), Chawla (space), Pal (Everest).",
        "Manekshaw Field Marshal 1973; Rakesh Sharma 1984; Aryabhata 1975; railway 1853.",
        "Chandrayaan-3 landed 23 Aug 2023, now National Space Day.",
    ],
    patterns=[
        pat("ga-nf-p1", "National symbol and its identity", "very common",
            "The stem asks the national aquatic animal, tree, fruit, river or heritage animal.",
            ["Recall the symbol table.", "Match the newer ones by year: river 2008, dolphin 2009, elephant 2010.",
             "Reject look-alikes such as whale shark or lion."],
            "Each symbol has a single identity, so the table settles it.",
            "Which is India's **national heritage animal**?",
            ["Heritage animal was declared in 2010.", "It is the Asian elephant.", "The Gangetic dolphin is the aquatic animal."],
            "Elephant"),
        pat("ga-nf-p2", "Flag facts: design, dates, code", "common",
            "The stem asks who designed the flag, its ratio, the spokes or the adoption date.",
            ["Recall Venkayya, 22 July 1947.", "Recall the ratio 3 : 2 and 24 spokes.",
             "Recall the colours: saffron courage, white truth and peace, green faith and prosperity."],
            "Four numbers and one name cover every flag question.",
            "How many **spokes** does the Ashoka Chakra on the national flag have?",
            ["The chakra is navy blue.", "It comes from the Sarnath Lion Capital.", "It has 24 spokes."],
            "24"),
        pat("ga-nf-p3", "Anthem, song, emblem and calendar", "very common",
            "The stem asks the anthem's adoption date, the source of Vande Mataram or the emblem's origin.",
            ["Recall the anthem: Tagore, 24 Jan 1950, about 52 seconds.",
             "Recall the song: Bankim Chandra, Anandamath.",
             "Recall the emblem: Sarnath, 26 Jan 1950, Mundaka Upanishad motto."],
            "The two January 1950 dates are the usual trap.",
            "India's **national anthem** was adopted on which date?",
            ["The anthem is Jana Gana Mana by Tagore.", "It was adopted on 24 January 1950.", "The emblem followed on 26 January 1950."],
            "24 January 1950"),
        pat("ga-nf-p4", "Firsts among women", "very common",
            "The stem asks the first woman Chief Minister, Governor, President, IPS officer or Everest climber.",
            ["Recall the women firsts table.", "Use the hook: Sarojini Governs, Sucheta Chiefs.",
             "Match space, Everest and IPS: Chawla, Pal, Bedi.", "For INC: Annie Besant first, Sarojini Naidu first Indian woman."],
            "Each office has one name, and the office is the clue.",
            "Who was the **first woman Chief Minister** of an Indian state?",
            ["Chief Minister links to Sucheta.", "Sucheta Kripalani led Uttar Pradesh in 1963.", "Sarojini Naidu was the first woman Governor."],
            "Sucheta Kripalani"),
        pat("ga-nf-p5", "Firsts in offices, science and infrastructure", "common",
            "The stem asks the first Field Marshal, Indian in space, satellite, feature film or railway.",
            ["Recall offices: Prasad, Nehru, Manekshaw.",
             "Recall space: Rakesh Sharma 1984, Chawla 1997, Aryabhata 1975.",
             "Recall beginnings: Raja Harishchandra 1913, railway 1853, census 1872."],
            "Each first is a single name or year.",
            "Who was the **first Field Marshal** of the Indian Army?",
            ["The first Field Marshal was named in 1973.", "He was Sam Manekshaw, Army chief in the 1971 war.", "K.M. Cariappa and Arjan Singh followed in 1986 and 2002."],
            "Sam Manekshaw"),
        pat("ga-nf-p6", "Firsts in high office and law", "common",
            "The stem asks the first Chief Justice, Chief Election Commissioner or Governor-General.",
            ["Recall the pairs: Kania, Sukumar Sen, Rajagopalachari.",
             "For Governor-General: Mountbatten was first, Rajagopalachari the first Indian.",
             "Add women: Fathima Beevi (SC judge 1989), Indira Gandhi (PM 1966)."],
            "Each office has one first holder, so match the office.",
            "Who was the **first Chief Election Commissioner** of India?",
            ["The first CEC came after the Election Commission was set up in 1950.", "He was Sukumar Sen."],
            "Sukumar Sen"),
    ],
)

# =====================================================================
# 6. Organisations, capitals, currencies, parliaments
# =====================================================================
SUBS["organisations-countries"] = dict(
    concept=(
        "This topic is four match-the-column lists. They are organisation and headquarters, currency and country, "
        "parliament and country, and capitals. Learn each list in small city groups."
    ),
    notes=r"""### United Nations family
The UN was founded on 24 October 1945. Its headquarters is in New York.

| Body | HQ | Founded |
|---|---|---|
| UNICEF | New York | 1946 |
| UNDP | New York | 1965 |
| UNESCO | Paris | 1945 |
| WHO | Geneva | 1948 |
| ILO | Geneva | 1919 |
| WTO | Geneva | 1995 |
| ICRC | Geneva | 1863 |
| FAO | Rome | 1945 |
| WFP | Rome | 1961 |
| UNEP | Nairobi | 1972 |
| IAEA | Vienna | 1957 |
| OPEC | Vienna | 1960 |
| ICJ | The Hague | 1945 |
| OPCW | The Hague | 1997 |
| IMF, World Bank | Washington DC | 1944 (Bretton Woods) |

Other Geneva bodies are UNHCR and WMO. IFAD is in Rome and UN-Habitat is in Nairobi.

> **Tip:** Geneva is health, trade and labour. Rome is food. Nairobi is the environment.

### Other international bodies
| Body | HQ | Founded |
|---|---|---|
| NATO | Brussels | 1949 |
| ASEAN | Jakarta | 1967 |
| SAARC | Kathmandu | 1985 |
| BIMSTEC | Dhaka | 1997 |
| ADB | Manila | 1966 |
| AIIB | Beijing | 2016 |
| NDB (BRICS bank) | Shanghai | 2015 |
| International Solar Alliance | Gurugram (India) | 2015 |
| FIFA | Zurich | 1904 |
| IOC | Lausanne | 1894 |
| INTERPOL | Lyon | 1923 |
| ICAO | Montreal | 1944 |
| IMO | London | 1948 |
| ICC (cricket) | Dubai | 1909 |

WWF is in Gland, Switzerland. Amnesty International is in London.

### Currencies
| Region | Country and currency |
|---|---|
| South Asia | India, Pakistan, Nepal, Sri Lanka: rupee. Bangladesh: taka. Bhutan: ngultrum (at par with the Indian rupee). Maldives: rufiyaa. Afghanistan: afghani |
| East and South-East Asia | China: yuan (renminbi). Japan: yen. South Korea: won. Thailand: baht. Malaysia: ringgit. Indonesia: rupiah. Vietnam: dong. Philippines: peso. Myanmar: kyat. Mongolia: tugrik |
| West Asia and Russia | Russia: rouble. Turkey: lira. Saudi Arabia: riyal. UAE: dirham. Israel: shekel. Iran: rial |
| The West | UK: pound sterling. USA, Canada, Australia: dollar. Eurozone: euro. Switzerland: franc |
| Africa | South Africa: rand. Nigeria: naira. Kenya: shilling. Egypt: pound |
| Latin America | Brazil: real. Argentina, Mexico: peso |

> **Tip:** East of India: Taka, Ngultrum, Kyat. That is Bangladesh, Bhutan, Myanmar.

### Parliaments of the world
| Country | Parliament |
|---|---|
| India | Sansad (Lok Sabha and Rajya Sabha) |
| Israel | Knesset |
| Japan | Diet |
| China | National People's Congress |
| Iran | Majlis |
| Germany | Bundestag |
| Russia | Federal Assembly (lower house: Duma) |
| Bangladesh | Jatiya Sangsad |
| Pakistan | Majlis-e-Shoora |
| France, South Korea | National Assembly |
| Turkey | Grand National Assembly |
| Nordic: Denmark, Norway, Sweden | Folketing, Storting, Riksdag |
| Poland | Sejm |
| Iceland | Althing (among the oldest) |
| USA | Congress |
| UK | Parliament (Commons and Lords) |

### Capitals often asked
- Australia: **Canberra**. Canada: **Ottawa**. Brazil: Brasilia.
- New Zealand: Wellington. Nigeria: Abuja. Turkey: Ankara.
- Myanmar: **Nay Pyi Taw**. Kazakhstan: Astana.
- Sri Lanka: Sri Jayawardenepura Kotte (administrative).
""",
    tricks=[
        {"title": "Geneva, Rome, Nairobi",
         "body": "Geneva holds health, trade and labour bodies: WHO, WTO, ILO. Rome holds food bodies: FAO, WFP, IFAD. Nairobi holds UNEP, the environment body.",
         "example": {"q": "The headquarters of the Food and Agriculture Organization (FAO) is in which city?",
                     "steps": ["FAO is a food body.", "Food bodies sit in Rome."],
                     "answer": "Rome"}},
        {"title": "Neighbour currencies",
         "body": "East of India: Bangladesh uses the taka, Bhutan the ngultrum and Myanmar the kyat. Nepal, Sri Lanka and Pakistan use the rupee."},
    ],
    mistakes=[
        mis("Placing UNESCO in Geneva.", "UNESCO is in Paris."),
        mis("Mixing the Diet and the Knesset.", "Japan's parliament is the Diet. Israel's is the Knesset."),
        mis("Naming Sydney as Australia's capital.", "The capital is Canberra."),
        mis("Naming Toronto as Canada's capital.", "The capital is Ottawa."),
        mis("Putting the WTO in Washington.", "The WTO is in Geneva. The IMF and World Bank are in Washington DC."),
    ],
    revision=[
        "New York: UN, UNICEF, UNDP. Geneva: WHO, ILO, WTO, ICRC. Paris: UNESCO. Rome: FAO, WFP.",
        "Nairobi: UNEP. Vienna: IAEA, OPEC. The Hague: ICJ, OPCW. Washington DC: IMF, World Bank.",
        "Brussels NATO, Jakarta ASEAN, Kathmandu SAARC, Manila ADB, Dubai ICC, Lausanne IOC, Lyon INTERPOL.",
        "Taka Bangladesh, ngultrum Bhutan, kyat Myanmar, baht Thailand, rand South Africa, real Brazil.",
        "Knesset Israel, Diet Japan, Majlis Iran, Bundestag Germany, Duma Russia, Folketing Denmark, Storting Norway.",
        "Founding years: ILO 1919, UN and FAO 1945, WHO 1948, NATO 1949, ASEAN 1967, SAARC 1985, WTO 1995.",
    ],
    patterns=[
        pat("ga-oc-p1", "UN bodies and their headquarters", "very common",
            "The stem asks where UNESCO, WHO, FAO or UNICEF is headquartered.",
            ["Group by city: New York, Geneva, Paris, Rome, Nairobi, Vienna, The Hague.",
             "Use the theme: health, trade and labour to Geneva; food to Rome.",
             "Remember UNESCO alone in Paris."],
            "City groups turn twenty bodies into seven lists.",
            "The **International Court of Justice** sits in which city?",
            ["The ICJ is a UN court.", "It sits at The Hague, in the Peace Palace.", "The UN itself is in New York."],
            "The Hague"),
        pat("ga-oc-p2", "International bodies, headquarters and founding years", "very common",
            "The stem names NATO, ASEAN, SAARC, ADB, AIIB, FIFA or ICC and asks the HQ or year.",
            ["Recall the second table.", "Pair regional groups: Brussels, Jakarta, Kathmandu, Dhaka.",
             "Pair banks: ADB Manila, AIIB Beijing, NDB Shanghai.", "Pair sport bodies: FIFA Zurich, IOC Lausanne, ICC Dubai."],
            "Each body has one city and one year.",
            "The **International Solar Alliance**, founded at India's initiative, has its headquarters in which city?",
            ["The alliance was founded in 2015.", "Its headquarters is in Gurugram, India.", "It is the first treaty-based international organisation headquartered in India."],
            "Gurugram"),
        pat("ga-oc-p3", "Currency and its country", "very common",
            "The stem asks the currency of Bangladesh, Thailand, Indonesia or South Africa.",
            ["Use the region table.", "Do South Asia first: taka, ngultrum, rufiyaa, afghani, and rupee elsewhere.",
             "Then East Asia: yuan, yen, won, baht, ringgit, rupiah, dong, kyat.",
             "Then the rest: rouble, riyal, dirham, shekel, rand, naira, real, peso."],
            "Regions reduce the currency list to a few short groups.",
            "The currency of **Indonesia** is the what?",
            ["Indonesia is in South-East Asia.", "Its currency is the rupiah.", "Malaysia uses the ringgit, Thailand the baht, Vietnam the dong."],
            "Rupiah"),
        pat("ga-oc-p4", "Parliament and its country", "very common",
            "The stem asks whose parliament is the Knesset, Diet, Majlis or Bundestag, or whose lower house is the Duma.",
            ["Recall the core pairs: Israel Knesset, Japan Diet, Iran Majlis, Germany Bundestag.",
             "Add the Nordic set: Folketing, Storting, Riksdag.",
             "Add Russia: Federal Assembly, with the Duma as lower house."],
            "Parliament names are unique, so the pair table is enough.",
            "The **Bundestag** is the lower house of the parliament of which country?",
            ["The Bundestag is German.", "The Diet is Japan's; the Knesset is Israel's; the Riksdag is Sweden's."],
            "Germany"),
        pat("ga-oc-p5", "Organisation and its founding year", "common",
            "The stem asks when WHO, ASEAN or NATO was established, or names the Bretton Woods twins.",
            ["Anchor 1945: UN (24 Oct), FAO (16 Oct), UNESCO.",
             "Anchor 1944: IMF and World Bank at Bretton Woods.",
             "Line up the rest: WHO 1948, NATO 1949, IAEA 1957, OPEC 1960, ASEAN 1967, SAARC 1985, WTO 1995.",
             "Remember older bodies: ILO 1919, ICRC 1863, FIFA 1904, IOC 1894."],
            "The years form a single time line.",
            "The **IMF and the World Bank** were conceived at which 1944 conference?",
            ["Both were set up in 1944.", "The conference was at Bretton Woods, New Hampshire, USA.", "So they are called the Bretton Woods twins."],
            "Bretton Woods"),
        pat("ga-oc-p6", "Capital cities often confused", "common",
            "The stem asks the capital of Australia, Canada, Brazil, Turkey or Myanmar.",
            ["Recall the list: Canberra, Ottawa, Brasilia, Ankara, Nay Pyi Taw.",
             "Reject the big city: not Sydney, Toronto or Rio.",
             "Add the rest: Wellington, Abuja, Astana."],
            "The largest city is usually the wrong option.",
            "What is the capital of **Australia**?",
            ["The largest city is Sydney, but it is not the capital.", "The capital is Canberra."],
            "Canberra"),
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
        print("  long:", sub["id"], ln[:80])
    sub.update(concept=new["concept"], notes=n, tricks=new["tricks"], mistakes=new["mistakes"],
               revision=new["revision"], patterns=new["patterns"])
all_ids = [p["id"] for s in data["subtopics"] for p in s["patterns"]]
assert len(all_ids) == len(set(all_ids)), "pattern id clash"
TOPIC.write_text(json.dumps(data, ensure_ascii=False, indent=1) + "\n", encoding="utf-8", newline="\n")
for s in data["subtopics"]:
    print(s["id"], len(s["notes"]), "chars,", len(s["patterns"]), "patterns")
