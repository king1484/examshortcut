"""Ancient History part 2: Mahajanapadas, Buddhism and Jainism, Mauryan Empire."""
from _ah_common import pat, trick, mk

S = {}

# ---------------------------------------------------------------- mahajanapadas
S["mahajanapadas"] = dict(
    concept=(
        "By the 6th century BCE north India had sixteen big states called mahajanapadas. "
        "Magadha beat the rest and grew into an empire under the Haryanka, Shishunaga and Nanda dynasties. "
        "Persian and Greek invaders entered the north-west in the same age. "
        "Exams ask for capitals, rulers in order, and the two invasions."
    ),
    notes=r"""### The sixteen states
The Buddhist text **Anguttara Nikaya** lists **16 mahajanapadas**. The Jain *Bhagavati Sutra* gives a slightly different list.

| Mahajanapada | Capital | Note |
|---|---|---|
| **Magadha** | Girivraja (Rajagriha), later Pataliputra | Became the empire |
| Anga | **Champa** | Annexed by Bimbisara |
| Kashi | **Varanasi** | Absorbed by Kosala and Magadha |
| Kosala | **Shravasti** (also Ayodhya) | Eastern UP |
| **Vajji** | **Vaishali** | Republic of 8 clans, including Licchavis |
| **Malla** | **Kushinara**, Pava | Republic |
| Chedi | Shuktimati | Bundelkhand |
| Vatsa | **Kaushambi** | Near Prayagraj |
| Kuru | **Indraprastha** | Delhi-Meerut area |
| Panchala | Ahichchhatra, Kampilya | Western UP |
| Matsya | **Viratnagar** | Jaipur-Alwar area |
| Surasena | **Mathura** | UP |
| **Assaka** | Potana | **Only one south of the Vindhyas** |
| **Avanti** | **Ujjain** (north), Mahishmati (south) | Malwa |
| Gandhara | **Taxila** | North-west |
| Kamboja | Rajapura | Known for horses |

> **Tip:** Learn six pairs first: Avanti-Ujjain, Vatsa-Kaushambi, Kosala-Shravasti, Anga-Champa, Gandhara-Taxila, Matsya-Viratnagar.

Vajji and Malla were **republics**. The others were kingdoms.

### Why Magadha won
Four states were the strongest: **Magadha, Kosala, Vatsa and Avanti**. Magadha won because it had:

- **Iron mines** for weapons and ploughs.
- The rich **Ganga plain**.
- **Elephants** for its army.
- Natural forts at Rajagriha.

### The rulers in order
| Dynasty | Rulers and events |
|---|---|
| **Haryanka** | **Bimbisara**: met both Buddha and Mahavira; made marriage alliances; annexed Anga |
| | **Ajatashatru**: killed his father; fought the Vajjis; **First Buddhist Council** |
| | **Udayin**: founded **Pataliputra** at the Ganga-Son meeting point |
| **Shishunaga** | **Shishunaga**: destroyed **Avanti** |
| | **Kalashoka**: **Second Buddhist Council** at Vaishali |
| **Nanda** | **Mahapadma Nanda**: first non-Kshatriya empire builder; titles *Ekarat* and *Sarvakshatrantaka* |
| | **Dhana Nanda**: last Nanda; met Alexander; overthrown by Chandragupta Maurya |

> **Watch:** Udayin, not Ajatashatru, founded Pataliputra.

### The Persians
**Darius I** took Gandhara and the Punjab about **516 BCE**. Persian contact brought the **Kharosthi** script. It is written right to left.

### Alexander
- **Alexander** invaded in **326 BCE**.
- He beat **Porus (Puru)** at the **Hydaspes (Jhelum)**.
- His tired troops refused to go beyond the **Beas (Hyphasis)**.
- He died at Babylon in **323 BCE**.

> **Watch:** The battle was at the Jhelum. The mutiny was at the Beas.
""",
    tricks=[
        trick("Capital pairs by first letter",
              "**V**atsa-**K**aushambi and **V**ajji-**V**aishali. **A**vanti-Ujjain and **A**nga-Champa. "
              "**G**andhara-Taxila. Kuru-Indraprastha."),
        trick("Magadha order: Hari Shishu Nanda",
              "**Hary**anka, then **Shishu**naga, then **Nanda**, then Maurya. "
              "Council 1 is Ajatashatru (Haryanka). Council 2 is Kalashoka (Shishunaga).",
              "The Second Buddhist Council was held under which dynasty?",
              ["Kalashoka held it at Vaishali.", "Kalashoka belongs to the Shishunaga dynasty."],
              "Shishunaga dynasty"),
    ],
    mistakes=[
        mk("Saying Ajatashatru founded Pataliputra.", "**Udayin** founded Pataliputra."),
        mk("Putting Assaka in the north.", "Assaka is the only mahajanapada **south of the Vindhyas**. Avanti is in Malwa."),
        mk("Saying Alexander's army mutinied at the Jhelum.", "The battle with Porus was at the **Jhelum**. The mutiny was at the **Beas**."),
        mk("Mixing up Vatsa and Kosala capitals.", "Vatsa is **Kaushambi**. Kosala is **Shravasti**."),
    ],
    revision=[
        "The list of 16 mahajanapadas is in the Anguttara Nikaya (Buddhist).",
        "Capital pairs: Avanti-Ujjain, Vatsa-Kaushambi, Kosala-Shravasti, Anga-Champa, Gandhara-Taxila, Matsya-Viratnagar.",
        "Assaka is the only mahajanapada south of the Vindhyas. Vajji and Malla were republics.",
        "Dynasty chain: Haryanka, Shishunaga, Nanda, Maurya.",
        "Bimbisara, Ajatashatru (1st Council), Udayin (Pataliputra), Shishunaga (ended Avanti), Kalashoka (2nd Council), Mahapadma Nanda, Dhana Nanda.",
        "Darius I brought Kharosthi. Alexander beat Porus at the Jhelum in 326 BCE and turned back at the Beas.",
    ],
    patterns=[
        pat("ga-mah-p1", "Mahajanapada and its capital", "very common",
            "A capital or state is given with four options, or \"which pair is correctly matched\".",
            ["Recall the six key pairs.",
             "Republics have cities, not royal capitals: Vajji-Vaishali, Malla-Kushinara.",
             "Magadha had two capitals in turn: Rajagriha, then Pataliputra."],
            "Setters pick pairs from the same short list every year.",
            "The capital of the Vatsa mahajanapada was:",
            ["Vatsa is linked with a city near Prayagraj.", "That city is Kaushambi."],
            "Kaushambi"),
        pat("ga-mah-p2", "Magadhan ruler and event", "very common",
            "\"Who founded Pataliputra\", \"under which dynasty was the Second Council held\", or an order of rulers.",
            ["Recall the chain: Haryanka, Shishunaga, Nanda.",
             "Attach one event to each king: Bimbisara annexed Anga, Ajatashatru beat the Vajjis, Udayin founded Pataliputra.",
             "Shishunaga destroyed Avanti. Kalashoka held the 2nd Council. Mahapadma Nanda was Ekarat."],
            "Each king has one event, so the event names the king.",
            "Who founded Pataliputra at the meeting point of the Ganga and the Son?",
            ["Ajatashatru is the trap option.", "The Haryanka successor Udayin founded the city."],
            "Udayin"),
        pat("ga-mah-p3", "Source text, republics and odd facts", "common",
            "\"The list of 16 mahajanapadas occurs in\", \"which was a republic\", \"the only one south of the Vindhyas\".",
            ["Source: Anguttara Nikaya (Buddhist). The Jain list differs.",
             "Republics: Vajji (with Licchavis) and Malla.",
             "Extremes: Assaka in the south, Kamboja in the north-west with its horses."],
            "Each odd fact points to one state.",
            "The list of sixteen mahajanapadas appears in which Buddhist text?",
            ["The Jain Bhagavati Sutra gives a different list.", "The Buddhist list is in the Anguttara Nikaya."],
            "Anguttara Nikaya"),
        pat("ga-mah-p4", "Persian and Alexander's invasions", "common",
            "Darius I, Kharosthi script, the Hydaspes battle, the Beas mutiny.",
            ["Darius I, about 516 BCE: Gandhara and west Punjab. He brought Kharosthi.",
             "Alexander, 326 BCE: beat Porus at the Hydaspes (Jhelum).",
             "The troops refused at the Beas (Hyphasis). He died at Babylon in 323 BCE."],
            "Each event has one river, and the rivers are the traps.",
            "Alexander's army refused to march beyond which river?",
            ["The battle with Porus was at the Jhelum.", "The refusal came further east, at the Hyphasis."],
            "The Beas (Hyphasis)"),
        pat("ga-mah-p5", "Why Magadha rose", "occasional",
            "\"Which factor helped the rise of Magadha\" or \"which was NOT a reason\".",
            ["List the reasons: iron mines, Ganga plain, elephants, natural forts.",
             "Cut any option outside this list.",
             "Remember the rival powers: Kosala, Vatsa, Avanti."],
            "The list of reasons is short, so any new item is the wrong option.",
            "Which of these helped Magadha most in its early rise?\n(a) Iron mines nearby (b) Sea trade with Rome (c) A large navy (d) Silk Road tolls",
            ["Magadha had iron ores in south Bihar.", "The other options belong to later or different regions."],
            "(a) Iron mines nearby"),
        pat("ga-mah-p6", "Arrange rulers in order", "common",
            "\"Arrange in chronological order\" with three or four Magadhan kings.",
            ["Write the dynasty next to each king.",
             "Order the dynasties: Haryanka, Shishunaga, Nanda.",
             "Inside Haryanka: Bimbisara, Ajatashatru, Udayin."],
            "Placing the dynasty first gives most of the order.",
            "Arrange in order: 1. Mahapadma Nanda 2. Bimbisara 3. Udayin 4. Kalashoka",
            ["Bimbisara and Udayin are Haryanka, with Bimbisara first.", "Kalashoka is Shishunaga.", "Mahapadma Nanda is Nanda."],
            "2, 3, 4, 1"),
    ],
)

# ---------------------------------------------------------------- buddhism-jainism
S["buddhism-jainism"] = dict(
    concept=(
        "Buddhism and Jainism began in the 6th century BCE in the Magadha region. "
        "Both preached ahimsa and used the people's language. "
        "Exams ask about the Buddha's five life events, the four Buddhist councils, the 24 Tirthankaras and Mahavira's vows."
    ),
    notes=r"""### Why two new faiths rose
Both faiths began in the Magadha-Vaishali belt. Ritual religion had become costly and full of animal sacrifice. Merchants wanted simpler, ethical teaching.

Both preached **ahimsa** and used the people's language. Early Buddhism used **Pali**. Jainism used **Prakrit (Ardhamagadhi)**.

### The Buddha's life
| Event | Place | Symbol |
|---|---|---|
| Birth | **Lumbini** (Nepal) | Lotus and bull |
| Renunciation, age 29 | Left on horse **Kanthaka** with charioteer **Channa** | Horse |
| Enlightenment, age 35 | **Bodh Gaya**, under the Bodhi tree | Bodhi tree |
| First sermon | **Sarnath** (Deer Park) | Wheel |
| Death, age 80 | **Kushinagar** (Malla republic) | Stupa |

He was a **Shakya** prince. His father was Suddhodana and his mother was Mahamaya. His wife was **Yashodhara** and his son was **Rahula**.

> **Tip:** Symbols in order: lotus, horse, tree, wheel, stupa.

### What the Buddha taught
- **Four Noble Truths:** the world has sorrow; desire causes it; it can end; the Eightfold Path ends it.
- **Eightfold Path:** the **Middle Path** between luxury and harsh austerity.
- **Tri-ratna:** Buddha, Dhamma, Sangha.
- **Tripitaka:** *Vinaya* (monastic rules), *Sutta* (talks), *Abhidhamma* (philosophy).
- **Jatakas** are stories of the Buddha's earlier births.

### The four Buddhist Councils
| Council | Place | King | President | Result |
|---|---|---|---|---|
| 1st, 483 BCE | Rajagriha | Ajatashatru | Mahakassapa | Sutta (Ananda) and Vinaya (Upali) compiled |
| 2nd, 383 BCE | Vaishali | Kalashoka | Sabakami | Split: Sthaviravadins and Mahasanghikas |
| 3rd, 250 BCE | Pataliputra | Ashoka | Moggaliputta Tissa | Abhidhamma added; missions sent |
| 4th, c. 72 CE | Kundalvana, Kashmir | Kanishka | Vasumitra (deputy Ashvaghosha) | Split: Hinayana and Mahayana |

> **Tip:** Places are Raj-Vaish-Pat-Kash. Kings are A-K-A-K.

### Jainism
There are **24 Tirthankaras**.

| No. | Name | Symbol |
|---|---|---|
| 1 | **Rishabhanatha** (Adinatha) | Bull |
| 22 | Neminatha | Conch |
| 23 | **Parshvanatha** | Snake |
| 24 | **Mahavira** | Lion |

**Parshvanatha** was a prince of Varanasi. He gave **four vows**: ahimsa, satya, asteya, aparigraha.

**Mahavira** was born at **Kundagrama** near Vaishali. He gained **kaivalya** at 42 and died at **Pavapuri** at 72. He **added the fifth vow, Brahmacharya**. His titles were *Jina* and *Nirgrantha*.

The Jain **tri-ratna** is right faith, right knowledge and right conduct.

- **Sects:** Digambara (sky-clad, led by Bhadrabahu) and Shvetambara (white-clad, Sthulabhadra).
- **Councils:** first at Pataliputra (c. 300 BCE), second at Vallabhi (Gujarat, 5th to 6th century CE).

### Texts and monuments
- **Milindapanha:** dialogue of Menander (Milinda) and the monk Nagasena.
- **Nagarjuna** was a Mahayana philosopher of the Madhyamika school.
- **Gommateshwara (Bahubali)** statue, Shravanabelagola, Karnataka, c. 983 CE, built by Chamundaraya.
- **Dilwara** Jain temples, Mount Abu.
- **Nalanda:** founded by Kumaragupta I. **Vikramashila:** Dharmapala. **Odantapuri:** Gopala.

> **Watch:** Nalanda is Gupta. Vikramashila is Pala.
""",
    tricks=[
        trick("Councils: places, kings, presidents",
              "Places: **Raj**agriha, **Vaish**ali, **Pat**aliputra, **Kash**mir. "
              "Kings: **A**jatashatru, **K**alashoka, **A**shoka, **K**anishka. "
              "Presidents: Maha-Saba-Moggali-Vasu.",
              "Who presided over the Third Buddhist Council?",
              ["Third means Pataliputra and Ashoka.", "The third name in the chain is Moggaliputta Tissa."],
              "Moggaliputta Tissa"),
        trick("Buddha symbols in order",
              "Birth lotus, renunciation horse, enlightenment tree, first sermon wheel, death stupa."),
        trick("Tirthankara symbols",
              "Bull begins and lion ends. The 22nd has a conch. The 23rd has a snake."),
    ],
    mistakes=[
        mk("Saying Mahavira gave all five vows.", "Parshvanatha gave four. Mahavira **added Brahmacharya**."),
        mk("Mixing Sarnath and Bodh Gaya.", "Enlightenment is at **Bodh Gaya**. First sermon is at **Sarnath**. Death is at **Kushinagar**."),
        mk("Swapping the splits of the 2nd and 4th councils.", "2nd: Sthaviravadins and Mahasanghikas. 4th: Hinayana and Mahayana."),
        mk("Saying the Palas founded Nalanda.", "Nalanda was founded by **Kumaragupta I** of the Guptas. Vikramashila is Pala."),
    ],
    revision=[
        "Life chain: Lumbini, Bodh Gaya, Sarnath, Kushinagar. Symbols: lotus, horse, tree, wheel, stupa.",
        "Councils: Rajagriha, Vaishali, Pataliputra, Kashmir. Kings A-K-A-K. Presidents Maha-Saba-Moggali-Vasu.",
        "2nd council: first split. 3rd: Abhidhamma. 4th: Hinayana and Mahayana.",
        "Tirthankaras: 1 bull, 22 conch, 23 snake (four vows), 24 lion (added Brahmacharya).",
        "Jain sects: Digambara and Shvetambara. Councils at Pataliputra and Vallabhi.",
        "Gommateshwara is at Shravanabelagola. Nalanda is Kumaragupta I. Vikramashila is Dharmapala.",
    ],
    patterns=[
        pat("ga-bud-p1", "Buddha's life event, place and symbol", "very common",
            "\"Where did the Buddha attain enlightenment\", \"symbol of Mahaparinirvana\", or an order of life events.",
            ["Recall the chain: Lumbini, renunciation at 29, Bodh Gaya at 35, Sarnath, Kushinagar at 80.",
             "Recall the symbols: lotus, horse, tree, wheel, stupa.",
             "Extras: horse Kanthaka, charioteer Channa, wife Yashodhara, son Rahula."],
            "Five events with five places and five symbols cover the whole topic.",
            "Where did Gautama Buddha attain Mahaparinirvana?",
            ["Death is the last event in the chain.", "It took place in the Malla republic."],
            "Kushinagar, at age 80"),
        pat("ga-bud-p2", "Buddhist council with place, king, president, result", "very common",
            "\"The Fourth Council was held under\", \"which council added the Abhidhamma\", council-president pairs.",
            ["Places: Rajagriha, Vaishali, Pataliputra, Kashmir.",
             "Kings: Ajatashatru, Kalashoka, Ashoka, Kanishka.",
             "Presidents: Mahakassapa, Sabakami, Moggaliputta Tissa, Vasumitra.",
             "Results: 2nd first split, 3rd Abhidhamma, 4th Hinayana and Mahayana."],
            "One table of four rows gives every answer.",
            "Which Buddhist council led to the split into Hinayana and Mahayana?",
            ["Hinayana and Mahayana is the last split.", "It was held in Kashmir under Kanishka."],
            "The Fourth Council (c. 72 CE), president Vasumitra, deputy Ashvaghosha"),
        pat("ga-bud-p3", "Tirthankaras, Mahavira and the vows", "very common",
            "\"Who was the 23rd Tirthankara\", \"which vow was added by Mahavira\", \"kaivalya at the age of\".",
            ["Numbers: 1 Rishabha (bull), 22 Neminatha (conch), 23 Parshvanatha (snake), 24 Mahavira (lion).",
             "Mahavira: Kundagrama, kaivalya at 42, death at Pavapuri at 72.",
             "Parshva gave four vows. Mahavira added Brahmacharya."],
            "The number, symbol and vow facts are the whole question bank.",
            "Which vow did Mahavira add to the four preached by Parshvanatha?",
            ["The four old vows were ahimsa, satya, asteya, aparigraha.", "The new vow concerns celibacy."],
            "Brahmacharya"),
        pat("ga-bud-p4", "Texts, sects and monuments", "common",
            "\"Milindapanha is a dialogue between\", \"Gommateshwara is at\", \"Vikramashila was founded by\".",
            ["Texts: Tripitaka, Jatakas, Milindapanha (Menander and Nagasena).",
             "Jain monuments: Gommateshwara at Shravanabelagola, Dilwara at Mount Abu.",
             "Monasteries: Nalanda (Kumaragupta I), Vikramashila (Dharmapala), Odantapuri (Gopala)."],
            "Each text or place has one name attached.",
            "The Milindapanha records a dialogue between the monk Nagasena and which king?",
            ["The king is an Indo-Greek.", "His Indian name is Milinda."],
            "Menander (Milinda)"),
        pat("ga-bud-p5", "Teachings and tri-ratna", "common",
            "\"Tri-ratna of Buddhism\", \"Middle Path\", \"Four Noble Truths\", \"Jain tri-ratna\".",
            ["Buddhist tri-ratna: Buddha, Dhamma, Sangha.",
             "Jain tri-ratna: right faith, right knowledge, right conduct.",
             "Middle Path is the Eightfold Path."],
            "The two tri-ratnas differ, and setters swap them.",
            "Which of these is the Jain tri-ratna?\n(a) Buddha, Dhamma, Sangha (b) Right faith, right knowledge, right conduct (c) Ahimsa, satya, asteya (d) Sutta, Vinaya, Abhidhamma",
            ["Option (a) is the Buddhist tri-ratna.", "Option (d) is the Tripitaka."],
            "(b) Right faith, right knowledge, right conduct"),
        pat("ga-bud-p6", "Jain sects and councils", "occasional",
            "\"Digambara\", \"Shvetambara\", \"Vallabhi\", \"12 Angas\", \"Bhadrabahu\".",
            ["Digambara: sky-clad, led by Bhadrabahu.",
             "Shvetambara: white-clad, Sthulabhadra.",
             "First council at Pataliputra (12 Angas). Second at Vallabhi, where the canon was written."],
            "Two sects and two councils make a small table.",
            "The second Jain council, where the canon was written down, was held at:",
            ["The first council was at Pataliputra.", "The second was in Gujarat."],
            "Vallabhi"),
    ],
)

# ---------------------------------------------------------------- mauryan-empire
S["mauryan-empire"] = dict(
    concept=(
        "The Mauryas built the first empire that covered almost all India. "
        "Chandragupta founded it and Ashoka is its most famous king. "
        "Ashoka's edicts on rocks and pillars are our main source. "
        "Exams ask about rulers, edicts, officers, Greek visitors and Mauryan art."
    ),
    notes=r"""### The rulers
| Ruler | Reign | Key facts |
|---|---|---|
| **Chandragupta Maurya** | 322 to 298 BCE | Overthrew Dhana Nanda with **Chanakya (Kautilya)**; faced **Seleucus Nicator** in 305 BCE |
| **Bindusara** | 298 to 273 BCE | Title **Amitraghata** ("slayer of foes"); followed the **Ajivika** sect |
| **Ashoka** | c. 268 to 232 BCE | **Kalinga war, 261 BCE**; turned to Buddhism; *Dhamma* policy |
| **Brihadratha** | Last king | Killed by **Pushyamitra Shunga** in 185 BCE |

In the treaty of 305 BCE Seleucus received **500 war elephants**. Chandragupta received the eastern satrapies and a marriage alliance. The Greeks called him **Sandrocottus**.

Late in life Chandragupta became a Jain. He went to **Shravanabelagola** with **Bhadrabahu**.

### Foreign visitors and books
- **Megasthenes** came from Seleucus to Chandragupta's court. His book **Indica** survives only in fragments.
- **Deimachus** came to Bindusara from Antiochus I.
- The **Arthashastra** by Kautilya is a book on statecraft with 15 books (*adhikaranas*).

> **Watch:** Megasthenes served Seleucus. Deimachus served Antiochus I.

### Ashoka and Dhamma
The Kalinga war of **261 BCE** was in Ashoka's 8th regnal year. The bloodshed made him turn to **Dhamma**. Dhamma is a code of conduct, not a new religion. It means tolerance, ahimsa, kindness to servants and animals, and respect for all sects.

He held the **Third Buddhist Council**. He called himself **Devanampiya Piyadasi** (beloved of the gods).

### Ashoka's edicts
| Type | Facts |
|---|---|
| **Major Rock Edicts** (14) | **RE II** medical care; **RE V** Dhamma Mahamattas; **RE XII** tolerance; **RE XIII** Kalinga war and remorse |
| **Kalinga Edicts** | Dhauli and Jaugada, Odisha: "All men are my children" |
| **Minor Rock Edicts** | **Maski** names the king as "Ashoka" |
| **Bhabru edict** | Faith in Buddha, Dhamma and Sangha |
| **Rummindei pillar** | Visit to Lumbini |
| **Pillar Edicts** (7) | Delhi-Topra pillar has all seven |

- Language is **Prakrit**. Script is mostly **Brahmi**.
- **Kharosthi** is used at Shahbazgarhi and Mansehra. **Greek and Aramaic** are used at Kandahar.
- **James Prinsep** deciphered Brahmi in **1837**.

> **Tip:** Edict numbers: 2 hospital, 5 officers, 12 tolerance, 13 Kalinga.

### How the empire was run
| Officer | Job |
|---|---|
| **Samaharta** | Chief revenue collector |
| **Sannidhata** | Treasurer and storekeeper |
| **Gudhapurusha** | Spies |
| **Kumara** | Prince governing a province |

Provinces included Taxila, Ujjain, Tosali and Suvarnagiri. The usual land tax was **one-sixth** (*bhaga*). Megasthenes said Pataliputra was run by **6 committees of 5 members**.

### Art and the end
- **Sarnath Lion Capital** became the **National Emblem** on **26 January 1950**. Its shaft is polished **Chunar sandstone**.
- **Barabar caves** in Bihar were cut for the **Ajivikas**.
- **Didarganj Yakshi** is a fly-whisk bearer, now in the Patna Museum.
- After weak later kings, **Brihadratha** was killed by his general **Pushyamitra Shunga** in **185 BCE**.
""",
    tricks=[
        trick("Edict numbers: 2, 5, 12, 13",
              "**2** hospital ward. **5** officer rank. **12** faiths tolerated. **13** the unlucky war.",
              "Which Major Rock Edict records Ashoka's remorse after Kalinga?",
              ["Use the number line: 13 is the war.", "13 is Kalinga."],
              "Rock Edict XIII"),
        trick("Dynasty start dates: 322, 185, 73",
              "Maurya begins in **322** BCE. Shunga begins in **185** BCE. Kanva begins in **73** BCE."),
    ],
    mistakes=[
        mk("Saying Megasthenes and Deimachus served the same court.",
           "Megasthenes served Seleucus at Chandragupta's court. Deimachus served Antiochus I at Bindusara's court."),
        mk("Mixing the faiths of the three kings.",
           "Chandragupta ended as a **Jain**. Bindusara followed **Ajivikas**. Ashoka became **Buddhist**."),
        mk("Saying the Major Rock Edicts name \"Ashoka\".",
           "They use **Devanampiya Piyadasi**. The name Ashoka appears in **Maski**."),
        mk("Saying John Marshall deciphered Brahmi.", "**James Prinsep** deciphered Brahmi in 1837."),
    ],
    revision=[
        "322 BCE: Chandragupta and Chanakya end the Nandas. Megasthenes and Indica at his court.",
        "Seleucus treaty 305 BCE: 500 elephants for eastern satrapies and a marriage alliance.",
        "Kalinga 261 BCE led to Dhamma. Edicts in Prakrit and Brahmi. Prinsep deciphered them in 1837.",
        "RE XIII Kalinga. RE XII tolerance. Bhabru Buddha-Dhamma-Sangha. Rummindei Lumbini.",
        "Samaharta collects. Sannidhata is treasurer. Gudhapurushas are spies.",
        "Lion Capital is the National Emblem. Barabar caves are Ajivika. Brihadratha fell in 185 BCE.",
    ],
    patterns=[
        pat("ga-mau-p1", "Which edict says what", "very common",
            "\"Which edict describes the Kalinga war\", \"where does the name Ashoka appear\", script or language questions.",
            ["Anchor: RE XIII Kalinga, RE XII tolerance, Bhabru Buddha-Dhamma-Sangha, Rummindei Lumbini.",
             "The name Ashoka appears in Minor Rock Edicts such as Maski. Elsewhere he is Devanampiya Piyadasi.",
             "Script: Brahmi mostly, Kharosthi in the north-west, Greek and Aramaic at Kandahar."],
            "Each edict has one theme and one site.",
            "Which Ashokan edict records the king's faith in the Buddha, Dhamma and Sangha?",
            ["The message is about faith in the three jewels.", "It was found near Jaipur."],
            "The Bhabru (Bairat) edict"),
        pat("ga-mau-p2", "Mauryan officers and machinery", "common",
            "\"Who was the Samaharta\", spy wings, provincial governors, Dhamma Mahamattas.",
            ["Samaharta collects revenue. Sannidhata is the treasurer.",
             "Provinces were held by Kumara princes.",
             "Spies are gudhapurushas."],
            "Job titles come in pairs, so learn them as pairs.",
            "In Mauryan administration, the officer who collected revenue was the:",
            ["The treasurer was the Sannidhata.", "The collector is the other officer."],
            "Samaharta"),
        pat("ga-mau-p3", "Chandragupta, Chanakya and the Greeks", "very common",
            "The founding of the empire, the Arthashastra, the Seleucus treaty, Indica.",
            ["322 BCE: Chandragupta and Kautilya end Dhana Nanda.",
             "305 BCE treaty: 500 elephants for the eastern satrapies and a marriage alliance.",
             "Visitors: Megasthenes at Chandragupta's court and Deimachus at Bindusara's."],
            "The treaty terms and the visitors are asked in almost every paper.",
            "Under the Mauryan treaty with Seleucus in 305 BCE, Chandragupta gave Seleucus:",
            ["Seleucus received animals for war.", "The number was 500."],
            "500 war elephants"),
        pat("ga-mau-p4", "Art, architecture and the end of the dynasty", "common",
            "Lion Capital, Barabar caves, polished pillars, Brihadratha and Pushyamitra.",
            ["Polished Chunar sandstone pillars. Lion Capital is the National Emblem.",
             "Barabar caves were cut for the Ajivikas.",
             "Brihadratha was killed in 185 BCE by Pushyamitra Shunga."],
            "Each art item has one link, and the end date is fixed.",
            "The Barabar hill caves of the Mauryan age were given to which sect?",
            ["Bindusara followed this sect.", "The sect is the Ajivikas."],
            "The Ajivika sect"),
        pat("ga-mau-p5", "Ashoka's life and Dhamma", "common",
            "\"Kalinga war year\", \"Devanampiya Piyadasi\", \"Dhamma Mahamattas\", \"Third Council\".",
            ["Kalinga war: 261 BCE, in his 8th regnal year.",
             "Dhamma: a code of conduct, not a new religion.",
             "Dhamma Mahamattas appear in RE V. He held the Third Buddhist Council."],
            "Dhamma questions test whether you know it was ethics, not ritual.",
            "In which year of his reign did Ashoka fight the Kalinga war?",
            ["The war was in 261 BCE.", "Ashoka fought it early in his reign."],
            "The 8th regnal year (261 BCE)"),
        pat("ga-mau-p6", "Mauryan king and his faith", "occasional",
            "\"Which king followed the Ajivikas\", \"became a Jain\", \"Amitraghata\".",
            ["Chandragupta: Jain at the end, with Bhadrabahu at Shravanabelagola.",
             "Bindusara: Amitraghata, Ajivika follower.",
             "Ashoka: Buddhist."],
            "Each king has one faith, and the options swap them.",
            "Which Mauryan king took the title Amitraghata?",
            ["The title means slayer of foes.", "He was Chandragupta's son."],
            "Bindusara"),
    ],
)
