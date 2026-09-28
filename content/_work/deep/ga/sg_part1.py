"""static-gk deep content - part 1: books-authors, sports, awards."""
import os
import sys

sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
from _lib import Sub
from sg_notes import NOTES


def build_books():
    S = Sub("books-authors")
    S.notes = NOTES["books-authors"].strip()
    S.pattern("ga-ba-p1", "Ancient/medieval text ↔ author", "common",
        "'Who wrote Arthashastra/Rajatarangini/Akbarnama', 'Indica is an account of', Sanskrit drama questions.",
        None,
        "1. Ancient set: Kautilya-Arthashastra, Kalhana-Rajatarangini, Kalidasa-Abhijnana Shakuntalam, Vishakhadatta-Mudrarakshasa, Megasthenes-Indica, Banabhatta-Harshacharita, Vishnu Sharma-Panchatantra.\n2. Mughal set: Babur-Baburnama (own memoir), Abul Fazl-Akbarnama + Ain-i-Akbari, Jahangir-Tuzuk-i-Jahangiri.\n3. Distractors usually swap authors within the same period - eliminate by court and century.",
        "Who wrote **Rajatarangini**, the historical chronicle of Kashmir?",
        "**Kalhana** (12th century). Arthashastra - Kautilya; Harshacharita - Banabhatta.")
    S.pattern("ga-ba-p2", "Freedom-era work ↔ author", "very common",
        "'Discovery of India was written by', 'Hind Swaraj', 'Anandamath', 'Gitanjali', works of Gandhi-Nehru-Tagore-Bankim.",
        None,
        "1. Gandhi - **Hind Swaraj** and his autobiography **My Experiments with Truth**; Nehru - **Discovery of India** and **Glimpses of World History**.\n2. Bankim Chandra - **Anandamath** (source of *Vande Mataram*); Tagore - **Gitanjali** (Nobel 1913).\n3. Dadabhai Naoroji - **Poverty and Un-British Rule in India** (drain theory).",
        "**Anandamath**, the novel that gave the nation *Vande Mataram*, was written by —",
        "**Bankim Chandra Chattopadhyay**. Discovery of India - Nehru; Hind Swaraj - Gandhi.")
    S.pattern("ga-ba-p3", "Autobiography ↔ author", "very common",
        "'Wings of Fire is the autobiography of', 'Long Walk to Freedom', 'My Experiments with Truth', memoir matching.",
        None,
        "1. **Wings of Fire** - A.P.J. Abdul Kalam; **My Experiments with Truth** - M.K. Gandhi; **Long Walk to Freedom** - Nelson Mandela.\n2. **Playing It My Way** - Sachin Tendulkar; **A Shot at History** - Abhinav Bindra; **The Story of My Life** - Helen Keller.\n3. **Baburnama** is the earliest autobiography linked to India - Babur's own, in Turkish.",
        "**Long Walk to Freedom** is the autobiography of —",
        "**Nelson Mandela**. Wings of Fire - Kalam; My Experiments with Truth - Gandhi.")
    S.pattern("ga-ba-p4", "Booker Prize winners ↔ book", "common",
        "'Who wrote The White Tiger', 'Midnight's Children', 'The Inheritance of Loss', Booker-linking questions.",
        None,
        "1. Indian Booker winners: **Midnight's Children - Salman Rushdie (1981)**, **The God of Small Things - Arundhati Roy (1997)**, **The Inheritance of Loss - Kiran Desai (2006)**, **The White Tiger - Aravind Adiga (2008)**.\n2. Midnight's Children also won the 'Booker of Bookers'.\n3. Anita Desai was repeatedly shortlisted but never won - a favourite distractor next to her daughter Kiran.",
        "Who is the author of **The White Tiger** (Booker Prize 2008)?",
        "**Aravind Adiga**. The other Indian Booker books: Midnight's Children-Rushdie, God of Small Things-Roy, Inheritance of Loss-Kiran Desai.")
    S.pattern("ga-ba-p5", "World classic ↔ author", "common",
        "'War and Peace', 'One Hundred Years of Solitude', 'Don Quixote', 'The Republic', foreign classics and thinkers.",
        None,
        "1. Russia: Tolstoy-War and Peace, Dostoevsky-Crime and Punishment.\n2. Greece/Rome: Homer-Iliad + Odyssey, Plato-The Republic.\n3. West: Shakespeare-Hamlet/Macbeth, Austen-Pride and Prejudice, Cervantes-Don Quixote, Orwell-Animal Farm + 1984, Marquez-One Hundred Years of Solitude, Darwin-Origin of Species, Marx-Das Kapital, Adam Smith-Wealth of Nations.",
        "**One Hundred Years of Solitude**, a landmark of magical realism, was written by —",
        "**Gabriel Garcia Marquez** (Colombia). Don Quixote - Cervantes; War and Peace - Tolstoy.")

    S.q("ga-ba-p1", "easy", "The **Arthashastra**, the ancient treatise on statecraft, is attributed to:",
        ["Kalidasa", "Kautilya (Chanakya)", "Banabhatta", "Kalhana"], "Kautilya (Chanakya)",
        "**Kautilya (Chanakya)**, minister of Chandragupta Maurya, wrote the Arthashastra on polity, economy and spy-craft.",
        None, 15)
    S.q("ga-ba-p1", "medium", "**Indica**, an account of Mauryan India by a Greek envoy, was written by:",
        ["Ptolemy", "Megasthenes", "Herodotus", "Pliny"], "Megasthenes",
        "**Megasthenes**, ambassador of Seleucus Nicator at Chandragupta Maurya's court, wrote **Indica**; the original is lost but quoted by later writers.",
        None, 20)
    S.q("ga-ba-p1", "medium", "The **Harshacharita**, a biography of Emperor Harshavardhana, was composed by:",
        ["Banabhatta", "Vishakhadatta", "Kalidasa", "Bilhana"], "Banabhatta",
        "**Banabhatta**, Harsha's court poet, wrote the **Harshacharita** (and the prose romance Kadambari).",
        None, 20)
    S.q("ga-ba-p1", "hard", "Which Mughal emperor wrote his own memoir, the **Baburnama**?",
        ["Akbar", "Humayun", "Babur", "Jahangir"], "Babur",
        "**Babur** wrote the **Baburnama** himself in **Turkish**; the Tuzuk-i-Jahangiri is Jahangir's memoir; Akbar's story was written for him by Abul Fazl.",
        None, 25)
    S.q("ga-ba-p2", "easy", "The **Discovery of India** was written by:",
        ["Mahatma Gandhi", "Jawaharlal Nehru", "S. Radhakrishnan", "Rabindranath Tagore"], "Jawaharlal Nehru",
        "**Nehru** wrote it during his Ahmednagar prison years (1942-46); his other book is **Glimpses of World History**.",
        None, 15)
    S.q("ga-ba-p2", "medium", "Who wrote **Hind Swaraj**, the classic statement of his political philosophy?",
        ["Bal Gangadhar Tilak", "Mahatma Gandhi", "Lala Lajpat Rai", "Aurobindo Ghose"], "Mahatma Gandhi",
        "**Gandhi** wrote **Hind Swaraj** in 1909 aboard a ship from London to South Africa; his autobiography is *My Experiments with Truth*.",
        None, 20)
    S.q("ga-ba-p2", "medium", "**Gitanjali**, for which its author received the Nobel Prize for Literature in 1913, is a collection of —",
        ["Essays", "Poems (song offerings)", "Short stories", "Letters"], "Poems (song offerings)",
        "**Gitanjali** ('Song Offerings') is Tagore's collection of poems; he was the **first Asian** to win a Nobel Prize.",
        None, 20)
    S.q("ga-ba-p3", "easy", "**Wings of Fire** is the autobiography of:",
        ["Vikram Sarabhai", "A.P.J. Abdul Kalam", "Homi Bhabha", "Satish Dhawan"], "A.P.J. Abdul Kalam",
        "**Wings of Fire** traces Kalam's journey from Rameswaram to ISRO, DRDO and the Rashtrapati Bhavan.",
        None, 15)
    S.q("ga-ba-p3", "medium", "**My Experiments with Truth** is the autobiography of:",
        ["Nelson Mandela", "M.K. Gandhi", "Jawaharlal Nehru", "B.R. Ambedkar"], "M.K. Gandhi",
        "Gandhi's autobiography, first published in Gujarati, is ***The Story of My Experiments with Truth***; Mandela's is *Long Walk to Freedom*.",
        None, 15)
    S.q("ga-ba-p3", "medium", "The autobiography **A Shot at History** is associated with which sportsperson?",
        ["Sachin Tendulkar", "Milkha Singh", "Abhinav Bindra", "Mary Kom"], "Abhinav Bindra",
        "**A Shot at History: My Obsessive Journey to Olympic Gold** - shooter **Abhinav Bindra**, co-written with Rohit Brijnath.",
        None, 25)
    S.q("ga-ba-p4", "medium", "Who wrote **Midnight's Children**, winner of the 1981 Booker Prize and later the 'Booker of Bookers'?",
        ["Vikram Seth", "Salman Rushdie", "Amitav Ghosh", "Arundhati Roy"], "Salman Rushdie",
        "**Salman Rushdie's** Midnight's Children (1981) was judged the best Booker winner in 25 and 40 years of the prize.",
        None, 20)
    S.q("ga-ba-p4", "medium", "**The Inheritance of Loss**, which won the 2006 Booker Prize, was written by:",
        ["Anita Desai", "Kiran Desai", "Arundhati Roy", "Jhumpa Lahiri"], "Kiran Desai",
        "**Kiran Desai** won the 2006 Booker for The Inheritance of Loss; her mother **Anita Desai** was shortlisted several times but never won.",
        None, 25)
    S.q("ga-ba-p5", "easy", "**War and Peace** was written by the Russian novelist:",
        ["Dostoevsky", "Tolstoy", "Gogol", "Turgenev"], "Tolstoy",
        "**Leo Tolstoy** wrote War and Peace; Dostoevsky wrote Crime and Punishment.",
        None, 15)
    S.q("ga-ba-p5", "medium", "Who wrote **Don Quixote**, often called the first modern novel?",
        ["Homer", "Miguel de Cervantes", "Dante", "Victor Hugo"], "Miguel de Cervantes",
        "**Cervantes** (Spain) wrote Don Quixote; Homer is the ancient Greek author of the Iliad and the Odyssey.",
        None, 20)
    S.q("ga-ba-p5", "medium", "**The Republic**, the foundational text of Western political philosophy, was written by:",
        ["Aristotle", "Plato", "Socrates", "Cicero"], "Plato",
        "**Plato's** The Republic discusses justice and the ideal state; Aristotle wrote Politics.",
        None, 20)
    S.q("ga-ba-p5", "hard", "The books **Animal Farm** and **Nineteen Eighty-Four** were written by:",
        ["Aldous Huxley", "George Orwell", "H.G. Wells", "Rudyard Kipling"], "George Orwell",
        "**George Orwell** (Eric Blair) wrote both satires of totalitarianism; Huxley wrote Brave New World.",
        None, 20)
    return S


def build_sports():
    S = Sub("sports")
    S.notes = NOTES["sports"].strip()
    S.pattern("ga-sp-p1", "Trophy / cup ↔ sport", "very common",
        "'Santosh/Durand/Thomas/Davis/Ryder trophy is associated with', match-the-column on cups.",
        None,
        "1. Cricket: Ranji, Duleep, Irani, Deodhar, Vijay Hazare; the **Ashes** = England v Australia.\n2. Football: **Santosh** (states of India), **Durand** (oldest Indian tournament, 1888), Ballon d'Or (player award). Hockey: Aga Khan, Beighton, Rangaswami, Sultan Azlan Shah.\n3. Rackets: **Thomas (men) / Uber (women) / Sudirman (mixed)** in badminton; **Davis (men) / Billie Jean King (women)** in tennis; **Ryder Cup** = golf; **Swaythling Cup** = table tennis; **Ezra Cup** = polo.",
        "The **Durand Cup**, the oldest football tournament of India, was first played in —",
        "**1888** at Shimla - older than the FIFA World Cup by 42 years; the Santosh Trophy is the national championship for states.")
    S.pattern("ga-sp-p2", "Sporting term ↔ sport", "very common",
        "'Googly/yorker belong to', 'gambit/checkmate', 'deuce/ace/love', 'bull's eye', term matching.",
        None,
        "1. Cricket: googly, yorker, LBW, gully, cover drive, silly point.\n2. Hockey: bully, penalty corner, dribble, scoop. Tennis: deuce, ace, love, smash, volley; badminton shares love and smash.\n3. Golf: birdie, eagle, bogey, caddie, tee; Chess: gambit, castling, stalemate, checkmate; Shooting: bull's eye.",
        "The terms '**googly**' and '**yorker**' are associated with which sport?",
        "**Cricket**. Bully and penalty corner belong to hockey; birdie and bogey to golf.")
    S.pattern("ga-sp-p3", "Number of players per side", "common",
        "'How many players in a kabaddi/water polo/polo team', team-size ordering questions.",
        None,
        "1. Eleven: cricket, football, hockey. Fifteen: rugby union.\n2. Smaller sides: kabaddi **7**, kho-kho **9**, volleyball **6**, basketball **5**, water polo **7**, baseball **9**, polo **4**.\n3. Recall the odd ones - polo 4, kabaddi 7, rugby 15 - the rest sit in a narrow band.",
        "How many players does a **kabaddi** team field on the mat?",
        "**Seven**. Kho-kho fields nine; basketball five; volleyball six.")
    S.pattern("ga-sp-p4", "Grand Slams and major tournaments ↔ surface / venue", "common",
        "'Which Grand Slam is played on grass/clay', 'oldest tennis tournament', 'Wimbledon is played at'.",
        None,
        "1. Order of the year: Australian Open (hard) - **Roland Garros** (clay) - **Wimbledon** (grass) - US Open (hard).\n2. Wimbledon is the oldest (since 1877) and played at the All England Club, London.\n3. First FIFA World Cup - **1930, Uruguay**; first Cricket World Cup - **1975, England**.",
        "The **Australian Open** and the **US Open** are played on which type of surface?",
        "**Hard courts**. The French Open (Roland Garros) is on clay and Wimbledon on grass.")
    S.pattern("ga-sp-p5", "Olympics: history, symbols and India's milestones", "very common",
        "'First modern Olympics', 'Olympic motto', 'five rings represent', 'first Indian individual medal/gold', marathon distance.",
        None,
        "1. First modern Olympics - **1896, Athens**; revived by **Baron Pierre de Coubertin**; IOC founded 1894 (Paris).\n2. Motto - **Citius, Altius, Fortius** ('Together' added 2021); five rings = five continents; marathon = **42.195 km**.\n3. India: Norman Pritchard 1900 (two silvers); hockey gold from **1928 Amsterdam** (8 in all); K.D. Jadhav 1952 first individual medal; **Abhinav Bindra 2008** first individual gold; **Neeraj Chopra Tokyo 2020** javelin gold (87.58 m).",
        "The five interlocking rings of the Olympic flag represent —",
        "The **five continents** of the world united by sport; the rings were designed by Coubertin and first flown in 1920.")

    S.q("ga-sp-p1", "easy", "The **Ranji Trophy** is associated with which sport?",
        ["Hockey", "Cricket", "Football", "Badminton"], "Cricket",
        "The **Ranji Trophy** (since 1934) is India's premier first-class cricket championship, named after Ranjitsinhji.",
        None, 15)
    S.q("ga-sp-p1", "medium", "The **Sudirman Cup** is a world mixed-team championship of which sport?",
        ["Table tennis", "Badminton", "Squash", "Tennis"], "Badminton",
        "**Sudirman Cup** = badminton mixed teams; **Thomas Cup** = men, **Uber Cup** = women.",
        None, 20)
    S.q("ga-sp-p1", "medium", "The **Ryder Cup** is a team competition in which sport, contested between the USA and Europe?",
        ["Tennis", "Golf", "Rowing", "Shooting"], "Golf",
        "The **Ryder Cup** is golf's USA v Europe biennial match; the Davis Cup is tennis's equivalent for nations.",
        None, 15)
    S.q("ga-sp-p1", "hard", "The **Swaythling Cup** is awarded in which sport?",
        ["Squash", "Table tennis (men's world championship)", "Billiards", "Bridge"], "Table tennis (men's world championship)",
        "The **Swaythling Cup** goes to the men's team champion of world table tennis; the Corbillon Cup is the women's equivalent.",
        None, 30)
    S.q("ga-sp-p2", "easy", "The term '**bull's eye**' is associated with which sport?",
        ["Archery and shooting", "Boxing", "Cricket", "Volleyball"], "Archery and shooting",
        "A **bull's eye** is the centre of the target in archery and shooting events.",
        None, 15)
    S.q("ga-sp-p2", "medium", "The terms '**gambit**' and '**castling**' belong to which sport?",
        ["Cards", "Chess", "Carrom", "Billiards"], "Chess",
        "A **gambit** is an opening sacrifice, **castling** a king-rook move - both chess terms.",
        None, 15)
    S.q("ga-sp-p2", "medium", "'**Birdie**' and '**eagle**', terms for strokes under par, belong to which sport?",
        ["Badminton", "Golf", "Tennis", "Squash"], "Golf",
        "**Golf**: one under par = birdie, two under = eagle, one over = bogey.",
        None, 15)
    S.q("ga-sp-p3", "medium", "A **water polo** team has how many players in the pool?",
        ["Five", "Six", "Seven", "Nine"], "Seven",
        "**Water polo - seven** a side (six field players plus a goalkeeper). Kabaddi also fields seven.",
        None, 20)
    S.q("ga-sp-p3", "medium", "A **rugby union** team fields how many players?",
        ["Eleven", "Thirteen", "Fifteen", "Seventeen"], "Fifteen",
        "**Rugby union - fifteen** a side; rugby league plays thirteen.",
        None, 20)
    S.q("ga-sp-p3", "hard", "Which team sport has exactly **four** players per side?",
        ["Polo", "Basketball", "Kabaddi", "Softball"], "Polo",
        "**Polo - four** mounted players a side. Basketball is five, kabaddi seven, baseball nine.",
        None, 25)
    S.q("ga-sp-p4", "medium", "Which Grand Slam tennis tournament is the **oldest**, first played in 1877?",
        ["US Open", "Wimbledon", "French Open", "Australian Open"], "Wimbledon",
        "**Wimbledon** (All England Club, London, grass) began in 1877 - the oldest tennis tournament in the world.",
        None, 20)
    S.q("ga-sp-p4", "medium", "The first **FIFA World Cup** football tournament (1930) was hosted and won by:",
        ["Brazil", "Uruguay", "Italy", "Argentina"], "Uruguay",
        "**Uruguay** hosted and won in 1930, beating Argentina in the final; the tournament is held every four years.",
        None, 20)
    S.q("ga-sp-p4", "hard", "The first **Cricket World Cup** (1975) was hosted by England. Which team won it?",
        ["Australia", "West Indies", "India", "England"], "West Indies",
        "The **West Indies**, captained by Clive Lloyd, beat Australia in the 1975 final at Lord's.",
        None, 30)
    S.q("ga-sp-p5", "easy", "The first modern **Olympic Games** (1896) were held in:",
        ["Paris", "Athens", "Rome", "London"], "Athens",
        "**Athens, 1896** - revived by Pierre de Coubertin; the IOC had been founded in Paris in 1894.",
        None, 15)
    S.q("ga-sp-p5", "easy", "The Olympic motto 'Citius, Altius, Fortius' means:",
        ["Faster, Higher, Stronger", "Peace, Unity, Sport", "Mind, Body, Spirit", "Play the game"], "Faster, Higher, Stronger",
        "**Citius, Altius, Fortius** = Faster, Higher, Stronger (Latin); 'Communiter' (Together) was added in 2021.",
        None, 15)
    S.q("ga-sp-p5", "medium", "The **marathon** race in athletics is run over which distance?",
        ["40 km", "42.195 km", "44.5 km", "45.195 km"], "42.195 km",
        "**42.195 km**, fixed from the 1908 London route; the legend traces it to the Greek runner Pheidippides.",
        None, 20)
    S.q("ga-sp-p5", "medium", "Who won India's **first individual Olympic medal**, a wrestling bronze at Helsinki 1952?",
        ["Khashaba Jadhav", "Norman Pritchard", "Milkha Singh", "Leander Paes"], "Khashaba Jadhav",
        "**K.D. Jadhav** (wrestling, 1952 Helsinki) - India's first individual Olympic medal. Norman Pritchard had won two athletics silvers for India back in 1900.",
        None, 25)
    S.q("ga-sp-p5", "medium", "**Neeraj Chopra's** Tokyo 2020 gold medal came in which athletics event?",
        ["Shot put", "Javelin throw", "Discus throw", "Long jump"], "Javelin throw",
        "**Javelin throw** - his winning throw measured **87.58 m**; it was India's second-ever individual Olympic gold.",
        None, 20)
    S.q("ga-sp-p5", "medium", "India's first chess **Grandmaster** (1988) is:",
        ["D. V. Prasad", "Viswanathan Anand", "Pentala Harikrishna", "Vidit Gujrathi"], "Viswanathan Anand",
        "**Viswanathan Anand** became India's first GM in 1988; he later won the world championship in multiple formats.",
        None, 20)
    return S


def build_awards():
    S = Sub("awards")
    S.notes = NOTES["awards"].strip()
    S.pattern("ga-aw-p1", "Bharat Ratna: firsts and recipients", "very common",
        "'Who received the first Bharat Ratna', 'first woman/posthumous/sportsperson Bharat Ratna', order of civilian awards.",
        None,
        "1. Instituted **1954**; first trio (1954) - **C. Rajagopalachari, S. Radhakrishnan, C.V. Raman**.\n2. First woman - Indira Gandhi (1971); first posthumous - Lal Bahadur Shastri (1966); first sportsperson - **Sachin Tendulkar (2014)**.\n3. Precedence: Bharat Ratna > **Padma Vibhushan** > Padma Bhushan > Padma Shri - all civilian awards began in 1954.",
        "Who was the **first sportsperson** to receive the Bharat Ratna?",
        "**Sachin Tendulkar** (announced 2014, along with C.N.R. Rao) - also its youngest recipient at 40.")
    S.pattern("ga-aw-p2", "Nobel Prize: categories and Indian laureates", "very common",
        "'First Indian Nobel laureate', 'who won the Nobel for X year', 'Economics was added when', Peace prize pairs.",
        None,
        "1. Indians: Tagore 1913 (Literature), Raman 1930 (Physics), Khorana 1968 (Medicine), Mother Teresa 1979 (Peace), Sen 1998 (Economics), Ramakrishnan 2009 (Chemistry), Satyarthi 2014 (Peace), Banerjee 2019 (Economics).\n2. **Tagore** was the first non-white and first Asian laureate (Literature 1913).\n3. Economics prize (1969) is given by Sweden's central bank, not under Nobel's will; **Marie Curie** won Physics 1903 and Chemistry 1911.",
        "Who was the **first Indian** to win a Nobel Prize?",
        "**Rabindranath Tagore** - Literature, 1913, for Gitanjali. C.V. Raman won Physics in 1930.")
    S.pattern("ga-aw-p3", "Gallantry awards: hierarchy and firsts", "common",
        "'Highest gallantry award', 'first Param Vir Chakra', 'peacetime equivalent of PVC', Ashoka Chakra questions.",
        None,
        "1. Wartime ladder: **Param Vir Chakra > Maha Vir Chakra > Vir Chakra**.\n2. **First PVC - Major Somnath Sharma (1947, posthumous)**; peacetime counterpart - **Ashoka Chakra**.\n3. Peace-time/in-service awards also include the Sena/Nau-sena/Vayu Sena Medals.",
        "The **Ashoka Chakra** is awarded for —",
        "The most conspicuous **bravery or self-sacrifice away from the battlefield (peacetime)** - the peacetime counterpart of the Param Vir Chakra.")
    S.pattern("ga-aw-p4", "Literary, arts and international prizes", "very common",
        "'Highest literary award of India', 'first Dadasaheb Phalke', 'Abel/Fields/Turing are given for', 'Gandhi Peace Prize first winner'.",
        None,
        "1. India: **Jnanpith (1965)** - highest literary award (first G. Sankara Kurup); **Dadasaheb Phalke (1969)** - highest cinema honour (first Devika Rani).\n2. World: Booker (1969), Pulitzer (1917), Magsaysay (1958, 'Asian Nobel'), Gandhi Peace Prize (1995, first Julius Nyerere).\n3. Specialist prizes: **Abel** - mathematics (Norway, 2003); **Fields Medal** - mathematics, under 40, every 4 years; **Turing** - computer science.",
        "The **Fields Medal**, awarded every four years, honours achievement in which field?",
        "**Mathematics** - and only mathematicians aged **under 40**; the Abel Prize (2003) is mathematics' other big award.")
    S.pattern("ga-aw-p5", "Sports awards of India", "common",
        "'Highest sporting honour of India', 'first Khel Ratna', 'Dronacharya/Arjuna given for', year-pair questions.",
        None,
        "1. Highest: **Major Dhyan Chand Khel Ratna** (first 1991-92 to Viswanathan Anand; renamed in 2021).\n2. **Dronacharya (1985)** - coaches; **Arjuna (1961)** - sportspersons; **Dhyan Chand Award** - lifetime contribution.\n3. **MAKA Trophy** - best sports university/inter-university sport.",
        "The **Arjuna Award** (instituted 1961) is given for —",
        "Consistent **outstanding performance by sportspersons** over four years; the Dronacharya Award honours their coaches.")

    S.q("ga-aw-p1", "medium", "Which of the following is the **highest civilian award** of India?",
        ["Padma Vibhushan", "Bharat Ratna", "Param Vir Chakra", "Padma Bhushan"], "Bharat Ratna",
        "**Bharat Ratna** ('Jewel of India') is the highest civilian award; the Param Vir Chakra is the highest *wartime gallantry* award.",
        None, 15)
    S.q("ga-aw-p1", "medium", "The **first woman** to receive the Bharat Ratna was:",
        ["Mother Teresa", "Indira Gandhi", "Sarojini Naidu", "M.S. Subbulakshmi"], "Indira Gandhi",
        "**Indira Gandhi** (1971). Mother Teresa received it in 1980; M.S. Subbulakshmi in 1998.",
        None, 25)
    S.q("ga-aw-p1", "medium", "The Padma awards, in descending order of precedence, are:",
        ["Shri, Bhushan, Vibhushan", "Vibhushan, Bhushan, Shri", "Bhushan, Shri, Vibhushan", "Vibhushan, Shri, Bhushan"], "Vibhushan, Bhushan, Shri",
        "**Padma Vibhushan > Padma Bhushan > Padma Shri**, all instituted in 1954, below the Bharat Ratna.",
        None, 20)
    S.q("ga-aw-p2", "easy", "Who was the **first Indian** to win the Nobel Prize in Physics?",
        ["Homi Bhabha", "C.V. Raman", "S.N. Bose", "M.N. Saha"], "C.V. Raman",
        "**C.V. Raman** (1930) for the Raman effect; Tagore's 1913 prize was in Literature.",
        None, 15)
    S.q("ga-aw-p2", "medium", "**Kailash Satyarthi** shared the 2014 Nobel Peace Prize with —",
        ["Malala Yousafzai", "Barack Obama", "Kofi Annan", "Aung San Suu Kyi"], "Malala Yousafzai",
        "Satyarthi (child rights) shared it with **Malala Yousafzai** (Pakistan) - education for all children.",
        None, 20)
    S.q("ga-aw-p2", "hard", "Who is the only person to have won **two Nobel Prizes in different sciences**?",
        ["Linus Pauling", "Marie Curie", "John Bardeen", "Frederick Sanger"], "Marie Curie",
        "**Marie Curie** - Physics 1903 and Chemistry 1911; the first woman laureate. (Pauling and Bardeen also won two Nobels, but one of theirs was Peace or in the same field.)",
        None, 30)
    S.q("ga-aw-p3", "easy", "India's **highest wartime gallantry award** is the:",
        ["Ashoka Chakra", "Param Vir Chakra", "Maha Vir Chakra", "Kirti Chakra"], "Param Vir Chakra",
        "**Param Vir Chakra** - literally 'wheel of the supreme hero'; the Ashoka Chakra is its peacetime counterpart.",
        None, 15)
    S.q("ga-aw-p3", "medium", "The **first Param Vir Chakra** was awarded posthumously to which officer of the 1947-48 Kashmir operations?",
        ["Major Somnath Sharma", "Major Dhan Singh Thapa", "Captain Vikram Batra", "Major Shaitan Singh"], "Major Somnath Sharma",
        "**Major Somnath Sharma** (Kumaon Regiment) fell at Badgam, November 1947 - the first PVC.",
        None, 25)
    S.q("ga-aw-p4", "easy", "India's **highest award in cinema** is the:",
        ["National Film Award for Best Feature Film", "Dadasaheb Phalke Award", "Filmfare Award", "IIFA Award"], "Dadasaheb Phalke Award",
        "The **Dadasaheb Phalke Award** (from 1969) honours lifetime contribution to Indian cinema; the first went to Devika Rani.",
        None, 15)
    S.q("ga-aw-p4", "medium", "The **Abel Prize**, since 2003 called the 'Nobel of mathematics', is awarded by which country?",
        ["Sweden", "Norway", "USA", "France"], "Norway",
        "**Norway** (by its Academy of Science and Letters) gives the Abel Prize; the Fields Medal is the other great mathematics award.",
        None, 25)
    S.q("ga-aw-p4", "medium", "The **Ramon Magsaysay Award**, often called the 'Asian Nobel', is given by which country's foundation?",
        ["India", "Philippines", "Japan", "Singapore"], "Philippines",
        "The **Philippines** (Ramon Magsaysay Award Foundation, Manila), from 1958, in memory of President Magsaysay.",
        None, 20)
    S.q("ga-aw-p4", "hard", "The first **Gandhi Peace Prize** (1995), instituted by the Government of India, went to:",
        ["Nelson Mandela", "Julius Nyerere", "Mother Teresa", "Aung San Suu Kyi"], "Julius Nyerere",
        "**Julius Nyerere**, former President of Tanzania, won the first Gandhi Peace Prize (1995).",
        None, 30)
    S.q("ga-aw-p5", "medium", "Who was the **first recipient** of India's highest sporting honour (Khel Ratna), in 1991-92?",
        ["Sachin Tendulkar", "Viswanathan Anand", "Milkha Singh", "P.T. Usha"], "Viswanathan Anand",
        "Chess world champion **Viswanathan Anand** received the first Rajiv Gandhi Khel Ratna (1991-92); renamed after Major Dhyan Chand in 2021.",
        None, 25)
    S.q("ga-aw-p5", "medium", "The **Dhyan Chand Award** is given for —",
        ["Coaching excellence", "Lifetime achievement in sports", "Best university in sports", "Best school in sports"], "Lifetime achievement in sports",
        "**Dhyan Chand Award** = lifetime contribution to sport; Dronacharya = coaches; Arjuna = players; MAKA = universities.",
        None, 20)
    return S
