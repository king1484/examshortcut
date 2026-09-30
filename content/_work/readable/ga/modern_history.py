"""Readable rewrite of GA > Modern History (all 6 subtopics).

Plain English, facts kept exactly as in the previous notes/concept, reorganised into tables and timelines.
Patterns = question types with a method and a worked example built only from facts in the notes.
Run: python modern_history.py  (patches content/core/topics/ga/modern-history.json in place)
"""
import json
from pathlib import Path

ROOT = Path(__file__).resolve().parents[3]
TOPIC = ROOT / "core" / "topics" / "ga" / "modern-history.json"


def pat(pid, name, freq, spot, steps, why, q, ex_steps, answer):
    return {"id": pid, "name": name, "frequency": freq, "howToSpot": spot, "formula": None,
            "steps": steps, "why": why, "example": {"q": q, "steps": ex_steps, "answer": answer}}


def trick(title, body, q=None, steps=None, answer=None):
    t = {"title": title, "body": body}
    if q:
        t["example"] = {"q": q, "steps": steps, "answer": answer}
    return t


def mk(wrong, right):
    return {"wrong": wrong, "right": right}


S = {}

# ---------------------------------------------------------------- british-expansion
S["british-expansion"] = dict(
    concept=(
        "European companies came to India by sea to trade, starting in 1498. "
        "The English East India Company slowly changed from a trader into a ruler. "
        "Two battles, Plassey (1757) and Buxar (1764), gave it Bengal. "
        "Exams ask who came when, what each battle decided, and which Governor-General did what."
    ),
    notes=r"""### The Europeans arrive
Five European powers came to trade. Learn them in the order they arrived.

| Power | Year | Remember |
|---|---|---|
| **Portuguese** | **1498** | **Vasco da Gama** landed near **Calicut** (Kappad); the ruler was the Zamorin. **Albuquerque** took **Goa (1510)**. |
| **English** | **31 Dec 1600** | Charter from **Elizabeth I**. First permanent factory at **Surat (1613)**, after a naval win over the Portuguese. |
| Dutch | 1602 | VOC; Pulicat, Masulipatnam. Lost to the English at **Bedara (1759)**. |
| Danish | 1616 | Tranquebar, Serampore |
| **French** | **1664** | Company formed under **Colbert**; **Pondicherry (1674)**; **Dupleix** was the key governor |

The English then built three presidencies: **Madras (1639)**, **Bombay (1668**, part of Charles II's dowry) and **Calcutta (1690**, Job Charnock).

> **Tip:** Order of arrival: Portuguese, English, Dutch, Danish, French. Remember "**P**lease **E**at **D**al, **D**on't **F**ight".

### Plassey and Buxar: from trader to ruler
The Company first beat the French, then took Bengal.

| Battle | Date | What happened |
|---|---|---|
| **Plassey** | **23 June 1757** | **Robert Clive** defeated **Siraj-ud-Daulah**. **Mir Jafar** betrayed Siraj. |
| Wandiwash | 1760 | **Eyre Coote** defeated the French general Lally. This ended French hopes (Third Carnatic War). |
| **Buxar** | **22 Oct 1764** | **Hector Munro** defeated three rulers together: **Mir Qasim, Shuja-ud-Daula and Emperor Shah Alam II**. |

The **Treaty of Allahabad (1765)** gave the Company the **Diwani** of Bengal, Bihar and Orissa. Diwani means the right to collect revenue. It did not mean owning the land. Clive then ran a "dual government" (1765–72). **Warren Hastings** ended it.

### Wars that built the empire
| Wars | Years | Result |
|---|---|---|
| Anglo-Mysore (four wars) | 1767–1799 | Fought against Haidar Ali and **Tipu Sultan**, the "Tiger of Mysore". Tipu died defending **Srirangapatna in 1799** (Fourth war, Wellesley's time). |
| Anglo-Maratha (three wars) | 1775–1818 | First war ended by the **Treaty of Salbai (1782)**. The third war ended Peshwa rule (**1818**). |
| Anglo-Sikh (two wars) | 1845–49 | Fought after Ranjit Singh's death (1839). **Punjab annexed 1849** (Dalhousie). |

Other gains: Sind (1843, Napier), Burma, and **Awadh (1856)**, taken "for misgovernment".

### Two tools of annexation
- **Subsidiary Alliance** (**Wellesley**, **1798**): an Indian ruler kept Company troops at his cost. He lost his independence. The **Nizam of Hyderabad** signed first.
- **Doctrine of Lapse** (**Dalhousie**): if a ruler died without a son, an adopted heir was not accepted. The state "lapsed" to the Company. Examples: **Satara, Jaitpur, Sambalpur, Udaipur, Jhansi, Nagpur**.

> **Watch:** Awadh was annexed for "misgovernment", not under the Doctrine of Lapse.

### Governors-General and Viceroys
| Name | Remember for |
|---|---|
| **Warren Hastings** | First Governor-General of **Bengal** (Regulating Act 1773). Asiatic Society of Bengal (1784, founded by William Jones). Pitt's India Act 1784 added dual control. |
| **Cornwallis** (1786–93) | **Permanent Settlement (1793)**; police and judicial reforms; "father of the civil services" |
| **Wellesley** | **Subsidiary Alliance** (1798) |
| **William Bentinck** (1828–35) | First Governor-General of **India** (Charter Act 1833); **sati abolished (1829)**; English Education Act 1835 (Macaulay's Minute); thuggee suppressed |
| **Dalhousie** (1848–56) | Doctrine of Lapse; first railway **Bombay–Thane (16 April 1853)**; telegraph; postage; engineering colleges; Wood's Despatch (1854) |
| **Canning** | Last Governor-General and **first Viceroy (1858)** |
| **Lytton** | Delhi Durbar 1877 (Victoria made "Empress of India"); **Vernacular Press Act 1878**; Arms Act |
| **Ripon** | "Father of **local self-government**" (1882); **Ilbert Bill** (1883); first synchronous **census (1881)** |
| Dufferin | Congress founded (1885) |
| **Curzon** | **Partition of Bengal (1905)**; Ancient Monuments Preservation Act (1904) |
| Hardinge II | 1911: capital to shift to **Delhi**; partition annulled |
| Mountbatten | Last Viceroy; first Governor-General of free India |

**C. Rajagopalachari** was the last, and the only Indian, Governor-General.

### Three land-revenue systems
| System | Region | Who and how |
|---|---|---|
| **Permanent Settlement (1793)** | Bengal, Bihar, Odisha | **Cornwallis**. Zamindars became landowners. Revenue fixed forever. |
| **Ryotwari** | Madras, Bombay | Reed and **Thomas Munro**. Deal made directly with the **ryot** (the farmer). |
| **Mahalwari** | North-Western Provinces, Central India, parts of Punjab | **Holt Mackenzie, 1822**. Deal made with the **village estate (mahal)**. |
""",
    tricks=[
        trick("Plassey then Buxar: \"57 buys, 64 seals\"",
              "**1757 Plassey** gave the British a foothold (Clive beat Siraj). **1764 Buxar** sealed control (three rulers beaten). The **Diwani** followed in **1765**.",
              "Which battle was fought against the combined forces of Mir Qasim, Shuja-ud-Daula and Shah Alam II?",
              ["Three rulers fought together.", "Only Buxar had three Indian rulers on one side."],
              "Battle of Buxar (1764)"),
        trick("Governor-General reforms in order",
              "Cornwallis **Settles** (1793) → Wellesley **Subsidises** (1798) → Bentinck bans **Sati** (1829) → Ripon starts **Local** self-government (1882)."),
    ],
    mistakes=[
        mk("Calling Warren Hastings the first Governor-General of India.",
           "Warren Hastings = first GG of **Bengal** (1773). Bentinck = first GG of **India** (1833). Canning = first **Viceroy** (1858)."),
        mk("Placing the Ilbert Bill in Curzon's time.", "The Ilbert Bill (1883) belongs to **Ripon**."),
        mk("Saying the English set up their first factory at Calicut.",
           "The English factory was at **Surat**. Calicut is where **Vasco da Gama** landed."),
        mk("Thinking the Diwani (1765) made the Company owner of the land.",
           "Diwani was only the right to **collect revenue** in Bengal, Bihar and Orissa."),
        mk("Putting Awadh (1856) under the Doctrine of Lapse.",
           "Awadh was annexed for **misgovernment**. Lapse states include Satara, Jhansi and Nagpur."),
        mk("Mixing Ryotwari and Mahalwari.",
           "**Ryot**wari = deal with each **ryot** (Madras, Bombay). **Mahal**wari = deal with the village **mahal** (North-West)."),
    ],
    revision=[
        "Arrival: Portuguese 1498, English 1600, Dutch 1602, Danish 1616, French 1664.",
        "Plassey 1757 (Mir Jafar's betrayal) → Buxar 1764 (three rulers) → Diwani 1765 (Treaty of Allahabad).",
        "Tipu died at Srirangapatna 1799; Peshwa rule ended 1818; Punjab annexed 1849.",
        "Wellesley = Subsidiary Alliance; Dalhousie = Doctrine of Lapse + railways (1853).",
        "Cornwallis = Permanent Settlement 1793; Bentinck = sati abolished 1829.",
        "Lytton = Vernacular Press Act 1878; Ripon = local self-government 1882; Curzon = Bengal partition 1905.",
        "Revenue: Permanent (Cornwallis), Ryotwari (Munro), Mahalwari (Holt Mackenzie).",
    ],
    patterns=[
        pat("ga-be-p1", "Plassey → Buxar → Diwani chain", "very common",
            "The question names Plassey, Buxar, Mir Jafar, Shah Alam II or the Treaty of Allahabad.",
            ["Plassey 1757 = Clive against Siraj-ud-Daulah; Mir Jafar betrayed.",
             "Buxar 1764 = Hector Munro against Mir Qasim, Shuja-ud-Daula and Shah Alam II.",
             "Treaty of Allahabad 1765 = Diwani of Bengal, Bihar, Orissa.",
             "Match the name in the question to one of these three lines."],
            "These three events form one chain, so each fact points to the next.",
            "The Battle of Buxar (1764) was fought against a combined army of Mir Qasim, Shuja-ud-Daula and:\n(a) Siraj-ud-Daulah (b) Shah Alam II (c) Tipu Sultan (d) Mir Jafar",
            ["Siraj-ud-Daulah fought at Plassey, so cut (a).",
             "Mir Jafar was the traitor at Plassey, so cut (d).",
             "Tipu fought the Mysore wars, so cut (c)."],
            "(b) Emperor Shah Alam II"),
        pat("ga-be-p2", "Anglo-Mysore, Anglo-Maratha and Anglo-Sikh wars", "very common",
            "Words like \"Tipu Sultan died in\", \"which war ended Maratha power\", \"Punjab was annexed in\".",
            ["Mysore: four wars; Tipu died at Srirangapatna, 1799.",
             "Marathas: three wars; Treaty of Salbai (1782) ended the first; power ended 1818.",
             "Sikhs: two wars; Punjab annexed 1849 under Dalhousie."],
            "Each group of wars has one number and one end year; that is what the options test.",
            "Tipu Sultan was killed in 1799 while defending:",
            ["1799 is the Fourth Anglo-Mysore War.", "Tipu died defending his capital."],
            "Srirangapatna"),
        pat("ga-be-p3", "Governor-General ↔ measure", "very common",
            "\"Sati was abolished by\", \"Vernacular Press Act was passed by\", \"first railway under\" — a measure and a ruler.",
            ["Recall the one-line table: Cornwallis, Wellesley, Bentinck, Dalhousie, Lytton, Ripon, Curzon.",
             "Check the year given in the question against the ruler's time.",
             "In \"wrongly matched\" questions, look for a measure swapped with a neighbour."],
            "Each Governor-General is remembered for one or two measures, so the pair decides the answer.",
            "The Vernacular Press Act (1878) was passed during the time of:\n(a) Ripon (b) Lytton (c) Curzon (d) Dalhousie",
            ["1878 falls between Dalhousie (1850s) and Ripon (1880s).",
             "Ripon repealed the Act in 1882, so cut (a).",
             "Lytton held the Delhi Durbar in 1877 and passed this Act in 1878."],
            "(b) Lord Lytton"),
        pat("ga-be-p4", "Land-revenue systems", "common",
            "Words like zamindar, ryot, mahal, Permanent Settlement, Thomas Munro or Holt Mackenzie.",
            ["Permanent Settlement 1793: Cornwallis, Bengal-Bihar-Odisha, zamindars.",
             "Ryotwari: Reed and Thomas Munro, Madras and Bombay, each farmer.",
             "Mahalwari: Holt Mackenzie 1822, North-West, village estate."],
            "The name of each system tells you who pays: zamindar, ryot or mahal.",
            "The Ryotwari system, which settled revenue directly with each farmer, was mainly used in:",
            ["\"Ryot\" means the farmer.", "Ryotwari is linked with Reed and Thomas Munro in the south and west."],
            "Madras and Bombay presidencies"),
        pat("ga-be-p5", "European arrival: who came where and when", "common",
            "\"Vasco da Gama landed at\", \"first English factory\", \"French headquarters\", or a list of European powers.",
            ["Recall the arrival table: Portuguese 1498, English 1600, Dutch 1602, Danish 1616, French 1664.",
             "Attach one place to each: Calicut, Surat, Pulicat, Tranquebar, Pondicherry.",
             "Pick the option that matches both the power and the place."],
            "Each power has one landmark year and one landmark place.",
            "The English East India Company set up its first permanent factory at:\n(a) Calicut (b) Surat (c) Pondicherry (d) Goa",
            ["Calicut = Vasco da Gama (Portuguese), so cut (a).",
             "Pondicherry = French; Goa = Portuguese under Albuquerque."],
            "(b) Surat (1613)"),
        pat("ga-be-p6", "Arrange in chronological order", "common",
            "\"Arrange the following in the correct order\" with 3 or 4 battles, treaties or measures.",
            ["Write the year next to each item.",
             "Find the earliest item and check which options start with it.",
             "Check the last item to split any options that remain."],
            "Checking only the first and last items usually leaves one option, which saves time.",
            "Arrange in order: 1. Treaty of Allahabad 2. Battle of Plassey 3. Battle of Wandiwash 4. Battle of Buxar",
            ["Years: Allahabad 1765, Plassey 1757, Wandiwash 1760, Buxar 1764.",
             "Earliest is Plassey (2); latest is Allahabad (1)."],
            "2, 3, 4, 1"),
        pat("ga-be-p7", "First and last titles", "common",
            "\"First Governor-General of Bengal/India\", \"first Viceroy\", \"last Viceroy\", \"only Indian Governor-General\".",
            ["First GG of Bengal = Warren Hastings (1773).",
             "First GG of India = William Bentinck (1833).",
             "Last GG and first Viceroy = Canning (1858).",
             "Last Viceroy = Mountbatten; last and only Indian GG = C. Rajagopalachari."],
            "The title changed twice (1833 and 1858), so read the exact title in the question.",
            "Who was the first Governor-General of India?",
            ["\"Of India\" (not \"of Bengal\") starts with the Charter Act of 1833.",
             "Warren Hastings was GG of Bengal, so he is the trap option."],
            "Lord William Bentinck"),
    ],
)

# ---------------------------------------------------------------- revolt-1857
S["revolt-1857"] = dict(
    concept=(
        "In 1857, Indian soldiers of the Company army, called sepoys, rose in revolt. "
        "It spread across north and central India before the British crushed it. "
        "In 1858 the British Crown took over India from the Company. "
        "Peasant and tribal revolts are asked in the same set of questions."
    ),
    notes=r"""### The spark: greased cartridges
The revolt had one quick trigger and many deeper causes. The trigger was a rumour about the new **Enfield rifle**.

Its cartridges were said to be greased with **cow and pig fat**. Soldiers had to bite them open. This was only the **immediate cause**.

| Date | Place | What happened |
|---|---|---|
| **29 March 1857** | **Barrackpore** | **Mangal Pandey** of the **34th Native Infantry** attacked his officers. He was hanged on 8 April. |
| **10 May 1857** | **Meerut** | 85 troopers of the 3rd Light Cavalry had been jailed for refusing the cartridges. The sepoys broke out and marched to Delhi. |
| Next | Delhi | They proclaimed the old **Bahadur Shah II (Zafar)** "Emperor of India". |

> **Watch:** Barrackpore was the first spark. The revolt itself **broke out at Meerut** on 10 May.

### Deeper causes
- **Political:** Doctrine of Lapse (Satara, Jhansi, Nagpur); Awadh annexed (1856); disrespect to the Mughal family; Nana Saheb's pension stopped.
- **Economic:** heavy land revenue; ruin of handicrafts; drain of wealth; loss of zamindari and talukdari rights.
- **Social and religious:** reform laws such as sati abolition; the Religious Disabilities Act (1850) let converts inherit property; rumours about railways and telegraphs; missionary work.
- **Military:** poor pay and promotion; Indians kept out of officer ranks; the **General Service Enlistment Act (1856)** meant service across the sea, which many feared would cost them caste.

> **Tip:** In a "which was NOT a cause" question, look for an event after 1857, such as the Partition of Bengal.

### Centres, leaders and British officers
| Centre | Indian leader | British officer |
|---|---|---|
| Delhi | Bahadur Shah II; General **Bakht Khan** | John Nicholson, Hodson |
| **Kanpur** | **Nana Saheb**, with **Tantia Tope** and Azimullah Khan | Colin Campbell |
| **Lucknow** | **Begum Hazrat Mahal** | Colin Campbell |
| **Jhansi** | **Rani Lakshmibai** | **Hugh Rose** |
| **Arrah / Jagdishpur (Bihar)** | **Kunwar Singh**, aged about 80 | William Taylor, Vincent Eyre |
| Faizabad | **Maulvi Ahmadullah Shah** | — |
| **Bareilly** | **Khan Bahadur Khan** | — |

The revolt spread through the Ganga plain, central India and parts of the Deccan. Bombay, Madras, Bengal proper and most of Punjab stayed quiet. Some historians call it a "sepoy mutiny". **V.D. Savarkar** called it the "**First War of Independence**".

### How it ended
- **September 1857:** the British took back Delhi. Bahadur Shah was tried and exiled to **Rangoon**. Hodson shot his sons.
- **June 1858:** Rani Lakshmibai died fighting at **Gwalior**.
- **1859:** Tantia Tope was captured and hanged.

The **Governor-General** during the revolt was **Canning**.

### The Act of 1858
The **Government of India Act, 1858** ended Company rule. India came under the British **Crown**.
- A **Secretary of State for India** took charge in London.
- The Governor-General got the title **Viceroy**. **Canning** was the first.
- **Queen Victoria's Proclamation** was read at **Allahabad on 1 November 1858**. It promised no more annexations and no interference in religion.
- The army was rebuilt on "divide and rule" lines.

### Peasant and tribal uprisings
| Movement | Year | Region | Leader or key fact |
|---|---|---|---|
| **Paika rebellion** | 1817 | Odisha | **Bakshi Jagabandhu**; against the British land system |
| Kol uprising | 1831 | Chotanagpur | Tribal lands taken by outsiders |
| **Santhal Hul** | 1855–56 | Rajmahal hills (Jharkhand) | **Sidhu and Kanhu** Murmu; against moneylenders and revenue men |
| **Indigo revolt** | 1859–60 | Bengal | The play *Neel Darpan* by Dinabandhu Mitra |
| **Munda Ulgulan** | 1899–1900 | Chotanagpur | **Birsa Munda** ("Dharti Aba"); led to the Chotanagpur Tenancy Act (1908) |
| Faraizi movement | — | Bengal | Dudu Mian |
| Moplah uprising | peak 1921 | Malabar (Kerala) | Linked to the Khilafat movement |
| **Bardoli Satyagraha** | 1928 | Gujarat | **Vallabhbhai Patel**; he earned the title **"Sardar"** |
| Tebhaga | 1946 | Bengal | Sharecroppers asked for two-thirds of the crop |
""",
    tricks=[
        trick("1857 pairs: \"Kanpur Nana, Lucknow Lady, Jhansi Rani, Bihar Kunwar\"",
              "**K**anpur–**N**ana Saheb · **L**ucknow–Begum Hazrat Mahal (the Lady) · **J**hansi–Rani Lakshmibai · **B**ihar (Jagdishpur)–Kunwar Singh, the old hero.",
              "Kunwar Singh led the revolt of 1857 in which region?",
              ["\"Bihar Kunwar\" in the memory line.", "His home was Jagdishpur; he fought at Arrah."],
              "Jagdishpur / Arrah, Bihar"),
        trick("Tribal movements by first letter",
              "**S**anthal = **S**idhu (1855) · **M**unda = Birsa, at the **m**illennium's end (1899–1900)."),
    ],
    mistakes=[
        mk("Saying the revolt broke out at Barrackpore.",
           "Barrackpore was Mangal Pandey's earlier act (29 March). The revolt **broke out at Meerut** (10 May 1857)."),
        mk("Saying Colin Campbell defeated Rani Lakshmibai.",
           "Rani Lakshmibai was defeated by **Hugh Rose**. Campbell fought at Kanpur and Lucknow."),
        mk("Saying Bahadur Shah Zafar was sent to the Andamans.", "He was exiled to **Rangoon**."),
        mk("Linking Kunwar Singh with Gwalior.", "Kunwar Singh fought in **Bihar** (Arrah, Jagdishpur). Gwalior is where the Rani died."),
        mk("Calling the greased cartridge the main cause.",
           "It was only the **immediate** cause. The deeper causes were political, economic, social and military."),
        mk("Mixing the Santhal Hul and the Munda Ulgulan.",
           "Santhal Hul 1855–56 = **Sidhu and Kanhu**. Munda Ulgulan 1899–1900 = **Birsa Munda**."),
    ],
    revision=[
        "Trigger: greased Enfield cartridges (cow and pig fat rumour).",
        "Barrackpore, 29 March 1857 (Mangal Pandey) → Meerut, 10 May 1857 (outbreak) → Delhi.",
        "Kanpur–Nana Saheb, Lucknow–Hazrat Mahal, Jhansi–Lakshmibai, Arrah–Kunwar Singh, Bareilly–Khan Bahadur Khan.",
        "Hugh Rose defeated the Rani; Colin Campbell took Kanpur and Lucknow.",
        "Bahadur Shah II exiled to Rangoon; Delhi fell in September 1857.",
        "Act of 1858: Crown rule, Secretary of State, Canning first Viceroy; Proclamation at Allahabad, 1 Nov 1858.",
        "Uprisings: Paika 1817, Kol 1831, Santhal 1855, Indigo 1859, Munda 1899, Bardoli 1928, Tebhaga 1946.",
    ],
    patterns=[
        pat("ga-re-p1", "1857 centre ↔ leader", "very common",
            "\"Who led the revolt at…\", or a match-the-column of centres and leaders.",
            ["Recall the seven pairs: Delhi, Kanpur, Lucknow, Jhansi, Arrah, Faizabad, Bareilly.",
             "Remember the helpers too: Tantia Tope (Kanpur), Bakht Khan (Delhi).",
             "Match first the pairs you are surest of, then cut options."],
            "Every centre had one main leader, so one sure pair removes most options.",
            "Match: A. Kanpur B. Lucknow C. Jhansi D. Bareilly with 1. Begum Hazrat Mahal 2. Khan Bahadur Khan 3. Nana Saheb 4. Rani Lakshmibai",
            ["Kanpur–Nana Saheb (3); Lucknow–Hazrat Mahal (1).",
             "Jhansi–Lakshmibai (4); Bareilly–Khan Bahadur Khan (2)."],
            "A-3, B-1, C-4, D-2"),
        pat("ga-re-p2", "Causes: immediate trigger and deeper causes", "very common",
            "\"Immediate cause of the revolt\", \"General Service Enlistment Act\", or \"which was NOT a cause\".",
            ["Immediate cause = greased cartridges of the Enfield rifle.",
             "Deeper causes: political, economic, social-religious, military.",
             "For a \"NOT a cause\" option, pick anything that happened after 1857."],
            "A cause must come before the event, so later events are always wrong.",
            "Which of these was NOT a cause of the Revolt of 1857?\n(a) Doctrine of Lapse (b) General Service Enlistment Act (c) Partition of Bengal (d) Annexation of Awadh",
            ["Lapse, Awadh (1856) and the 1856 Act all came before 1857.",
             "The Partition of Bengal came in 1905."],
            "(c) Partition of Bengal"),
        pat("ga-re-p3", "Course of the revolt and the Act of 1858", "common",
            "\"The revolt began at Meerut on\", Bahadur Shah's fate, or what the 1858 Act did.",
            ["Timeline: Barrackpore 29 March → Meerut 10 May 1857 → Delhi → Delhi falls September 1857.",
             "Bahadur Shah II: tried and exiled to Rangoon.",
             "1858 Act: Crown rule, Secretary of State, Viceroy (Canning), Queen's Proclamation."],
            "The 1858 Act is the one big change that followed the revolt.",
            "The Government of India Act, 1858 did which of these?",
            ["It ended Company rule; the Crown took over.",
             "A Secretary of State was created; Canning became the first Viceroy."],
            "Transferred rule from the East India Company to the British Crown"),
        pat("ga-re-p4", "Peasant or tribal uprising ↔ leader", "common",
            "\"The Santhal rebellion was led by\", Birsa Munda, Paika rebellion, Bardoli, Tebhaga.",
            ["Recall the uprisings table: movement, year, region, leader.",
             "Tie each tribe to its leader: Santhal–Sidhu and Kanhu, Munda–Birsa.",
             "Use the region to cut options: Odisha, Chotanagpur, Bengal, Malabar, Gujarat."],
            "Each uprising has one leader and one region, and the options mix them up.",
            "The Santhal rebellion of 1855–56, called the Hul, was led by:",
            ["Santhal = Sidhu, by the first letter.", "Birsa Munda led the Munda Ulgulan, a different tribe."],
            "Sidhu and Kanhu Murmu"),
        pat("ga-re-p5", "British officer who crushed the revolt", "occasional",
            "\"Who suppressed the revolt at…\" or \"Hugh Rose fought against\".",
            ["Jhansi → Hugh Rose.", "Kanpur and Lucknow → Colin Campbell.",
             "Delhi → John Nicholson, Hodson.", "Bihar → William Taylor, Vincent Eyre."],
            "Only four British names repeat, so the centre fixes the officer.",
            "The British officer who defeated Rani Lakshmibai was:\n(a) Colin Campbell (b) Hugh Rose (c) John Nicholson (d) Hodson",
            ["Campbell = Kanpur and Lucknow; Nicholson and Hodson = Delhi.", "Jhansi = Hugh Rose."],
            "(b) Hugh Rose"),
        pat("ga-re-p6", "Order of uprisings", "occasional",
            "\"Arrange these movements in chronological order\" with tribal or peasant revolts.",
            ["Write the year next to each: Paika 1817, Kol 1831, Santhal 1855, Indigo 1859, Munda 1899.",
             "Later ones: Moplah 1921, Bardoli 1928, Tebhaga 1946.",
             "Check the first and last items against the options."],
            "Years are far apart, so sorting takes seconds once the years are known.",
            "Arrange in order: 1. Munda Ulgulan 2. Paika rebellion 3. Santhal Hul 4. Indigo revolt",
            ["Paika 1817, Santhal 1855, Indigo 1859, Munda 1899.",
             "So the order is 2, 3, 4, 1."],
            "2, 3, 4, 1"),
    ],
)

# ---------------------------------------------------------------- reform-movements
S["reform-movements"] = dict(
    concept=(
        "In the 19th century, Indian reformers fought practices like sati, child marriage and caste discrimination. "
        "They set up groups called Samaj or Sabha. "
        "Exams ask the founder, the year and the main aim of each group, and the laws reformers pushed for."
    ),
    notes=r"""### Ram Mohan Roy and the Brahmo Samaj
**Raja Ram Mohan Roy** is called the "father of modern India". He began the reform age in Bengal.

- **Atmiya Sabha (1815)**: the group that came before the Brahmo Samaj.
- **Brahmo Sabha / Samaj (1828)**: belief in one God (monotheism) and no idol worship.
- He campaigned against **sati**. It was abolished in **1829** under Bentinck.
- He also worked for widow remarriage, a free press and English education. He wrote *Gift to Monotheists*.

Later the Brahmo Samaj was led, through its splits, by **Debendranath Tagore** (Tattvabodhini Sabha, 1839) and **Keshab Chandra Sen**.

**Young Bengal (1820s)**: radical students of Hindu College led by **Henry Vivian Derozio**.

### Organisations to know
| Organisation | Year | Founder | Remember for |
|---|---|---|---|
| **Prarthana Samaj** | 1867 | **Atmaram Pandurang** (Bombay) | **M.G. Ranade**, R.G. Bhandarkar; worship of God plus social reform |
| **Satyashodhak Samaj** | **1873** | **Jyotirao Phule** | Book ***Gulamgiri*** (1873); rights of lower castes |
| Singh Sabha | 1873 | Amritsar | Sikh revival |
| **Arya Samaj** | **1875** | **Swami Dayanand Saraswati** (Bombay) | ***Satyarth Prakash***; "Back to the Vedas"; **shuddhi** (reconversion); DAV schools |
| **Theosophical Society** | 1875 | **Madame Blavatsky and Col. Olcott** (New York) | Indian headquarters at **Adyar, Madras (1882)**; **Annie Besant** led it later |
| Aligarh Movement | 1875 | **Sir Syed Ahmad Khan** | Muhammadan Anglo-Oriental (MAO) College → **AMU (1920)**; modern education for Muslims |
| Deccan Education Society | 1884 | Tilak and Agarkar | Fergusson College |
| **Ramakrishna Mission** | **1897** | **Swami Vivekananda** | Belur Math; service to people; Chicago speech 1893 |
| Servants of India Society | 1905 | **Gokhale** | Trained public workers |

> **Tip:** **1875** is the year of three: Arya Samaj, Theosophical Society and the Aligarh MAO College.

> **Watch:** The Ramakrishna Mission was founded by **Vivekananda**, not by Ramakrishna Paramahamsa himself.

### Vidyasagar and the reform laws
**Ishwar Chandra Vidyasagar** turned the widow-remarriage campaign into law. He sent petitions, argued from Sanskrit texts and raised a fund for remarried widows. He also wrote the Bengali primer *Borno Porichoy*.

| Year | Law | Reformer behind it |
|---|---|---|
| **1829** | Bengal Sati Regulation (Regulation XVII) | Ram Mohan Roy (signed by Bentinck) |
| **1856** | **Hindu Widows' Remarriage Act** | **Ishwar Chandra Vidyasagar** |
| **1891** | Age of Consent Act (age raised to 12) | Behramji Malabari |
| **1929** | **Sarda Act** (Child Marriage Restraint Act) | Har Bilas Sarda; marriage age **18 for boys, 14 for girls** |

> **Rule:** The law years go 1829, 1856, 1891, 1929. Each is roughly a generation apart.

### Lower-caste and regional movements
- **Jyotirao and Savitribai Phule**: Satyashodhak Samaj (1873); Pune's first girls' school (1848).
- **Sree Narayana Guru** (Kerala, Ezhava community): set up the Aruvippuram Shiva shrine (1888). He inspired the **SNDP Yogam (1903)**. Motto: "One caste, one religion, one God for man".
- **Periyar E.V. Ramasamy**: **Self-Respect Movement (1925)** in Tamil Nadu, for caste and gender equality.
- **Maharashtra**: Gopal Baba Walangkar and later **Shahu Maharaj** pushed for reserved seats and caste reform.
- **B.R. Ambedkar**: **Mahad Satyagraha (1927)** for the right of untouchables to use a public water tank.

### Two ways of reform
The reformers took two broad paths.
- **Back to old texts:** the Arya Samaj went back to the Vedas.
- **Reason and modern learning:** the Brahmo Samaj stressed reason and one God for all; the Aligarh movement pushed modern education.

> **Watch:** Prarthana Samaj was in **Bombay**; Brahmo Samaj was in **Calcutta**. Do not swap them.
""",
    tricks=[
        trick("1875: the year of three",
              "**Arya Samaj** (Dayanand), **Theosophical Society** (Blavatsky and Olcott) and the **Aligarh MAO College** (Sir Syed) all date to **1875**.",
              "Which two of these began in the same year: Arya Samaj, Brahmo Samaj, Theosophical Society, Ramakrishna Mission?",
              ["Brahmo 1828, Ramakrishna Mission 1897.", "Arya Samaj 1875 and Theosophical Society 1875."],
              "Arya Samaj and Theosophical Society"),
        trick("Founder hooks by first letter",
              "**R**am Mohan = **R**eform of sati (Brahmo, 1828) · **D**ayanand = **D**iscover the Vedas (Arya) · **P**hule = **P**eople of lower castes (Satyashodhak) · **V**ivekananda = **V**edanta and service (Ramakrishna Mission, 1897)."),
    ],
    mistakes=[
        mk("Saying Ramakrishna Paramahamsa founded the Ramakrishna Mission.", "It was founded by his disciple **Vivekananda** in **1897**."),
        mk("Saying the Theosophical Society was founded at Adyar.", "It was founded in **New York** (1875). Its Indian headquarters moved to Adyar later."),
        mk("Giving the 1856 Widow Remarriage Act to Ram Mohan Roy.",
           "1856 widow remarriage = **Vidyasagar**. 1829 sati abolition = Ram Mohan Roy's campaign."),
        mk("Swapping Prarthana Samaj and Brahmo Samaj.",
           "Prarthana = 1867, Bombay, Atmaram Pandurang. Brahmo = 1828, Calcutta, Ram Mohan Roy."),
        mk("Placing the Self-Respect Movement in Kerala.",
           "Self-Respect (1925) = **Periyar**, Tamil Nadu. Kerala = Sree Narayana Guru, SNDP Yogam (1903)."),
    ],
    revision=[
        "Roy: Atmiya Sabha 1815 → Brahmo Samaj 1828 → sati abolished 1829.",
        "Prarthana 1867 (Atmaram Pandurang, Ranade); Satyashodhak 1873 (Phule, Gulamgiri).",
        "1875: Arya Samaj (Dayanand), Theosophical Society (Blavatsky, Olcott), MAO College (Sir Syed).",
        "Ramakrishna Mission 1897 (Vivekananda, Belur Math).",
        "Laws: sati 1829, widow remarriage 1856, age of consent 1891, Sarda Act 1929 (18/14).",
        "Narayana Guru–SNDP 1903–Kerala; Periyar–Self-Respect 1925; Ambedkar–Mahad 1927.",
    ],
    patterns=[
        pat("ga-rf-p1", "Organisation ↔ founder ↔ year", "very common",
            "\"Who founded the X Samaj?\" or a match-the-column of Samajs and founders.",
            ["Recall the main chain: Brahmo 1828 (Roy), Prarthana 1867 (Atmaram Pandurang), Arya 1875 (Dayanand), Ramakrishna Mission 1897 (Vivekananda).",
             "Add the others: Satyashodhak 1873 (Phule), Theosophical 1875, MAO College 1875.",
             "Match the pair you are surest of, then cut options."],
            "Each organisation has one founder, so one sure pair removes wrong options fast.",
            "The Prarthana Samaj was founded in 1867 by:\n(a) Ram Mohan Roy (b) Atmaram Pandurang (c) Dayanand Saraswati (d) Keshab Chandra Sen",
            ["Roy = Brahmo; Dayanand = Arya; cut (a) and (c).",
             "Keshab Chandra Sen led the Brahmo Samaj later; cut (d)."],
            "(b) Atmaram Pandurang"),
        pat("ga-rf-p2", "Reformer ↔ cause or work", "very common",
            "\"Who campaigned for widow remarriage?\", \"Borno Porichoy was written by\", \"shuddhi is linked to\".",
            ["Vidyasagar = widow remarriage + *Borno Porichoy*.",
             "Roy = sati; Dayanand = Back to the Vedas + shuddhi.",
             "Phule = girls' school 1848; Narayana Guru = Ezhava rights; Periyar = Self-Respect."],
            "Every famous reformer is tied to one cause, and the question names that cause.",
            "Who led the campaign that resulted in the Hindu Widows' Remarriage Act, 1856?",
            ["Widow remarriage + 1856 point to one person.",
             "He sent petitions and raised a fund for remarried widows."],
            "Ishwar Chandra Vidyasagar"),
        pat("ga-rf-p3", "Reform laws: year and details", "common",
            "\"Sati was abolished in\", \"Sarda Act fixed the age at\", or the order of the four laws.",
            ["1829 sati → 1856 widow remarriage → 1891 age of consent (12) → 1929 Sarda Act.",
             "Sarda Act ages: 18 for boys, 14 for girls.",
             "Match each law with its reformer if names are given."],
            "Only four laws are asked, and their years are far apart.",
            "The Sarda Act (1929) fixed the minimum marriage age at:",
            ["Sarda Act = Child Marriage Restraint Act.", "Boys 18, girls 14."],
            "18 for boys and 14 for girls"),
        pat("ga-rf-p4", "Regional and lower-caste movements", "common",
            "Sree Narayana Guru, Periyar, SNDP, Singh Sabha, Mahad Satyagraha, Satyashodhak.",
            ["Kerala = Narayana Guru: Aruvippuram 1888, SNDP Yogam 1903.",
             "Tamil Nadu = Periyar: Self-Respect Movement 1925.",
             "Maharashtra = Phule (1873), Mahad Satyagraha (Ambedkar, 1927); Punjab = Singh Sabha 1873."],
            "Tying each movement to a state removes most wrong options.",
            "The Self-Respect Movement (1925) was started by:",
            ["1925 + Tamil Nadu + caste and gender equality.", "That is Periyar E.V. Ramasamy."],
            "Periyar E.V. Ramasamy"),
        pat("ga-rf-p5", "Same year or odd one out", "common",
            "\"Which two were founded in the same year?\" or \"Which was NOT founded in 1875?\"",
            ["Write the year next to each option.",
             "Remember the clusters: 1873 (Satyashodhak, Singh Sabha) and 1875 (Arya, Theosophical, MAO).",
             "Pick the pair that shares a year, or the one that breaks it."],
            "Two year clusters cover most of these questions.",
            "Which of these was NOT founded in 1875?\n(a) Arya Samaj (b) Theosophical Society (c) Ramakrishna Mission (d) MAO College, Aligarh",
            ["Arya, Theosophical and MAO are the 1875 trio.", "Ramakrishna Mission is 1897."],
            "(c) Ramakrishna Mission"),
        pat("ga-rf-p6", "Arrange organisations in order", "occasional",
            "\"Arrange in chronological order\" with three or four reform bodies.",
            ["Write the year next to each.",
             "Find the earliest and check which options start with it.",
             "Use the last item to confirm."],
            "Most reform bodies have well-known years, so the order follows directly.",
            "Arrange in order: 1. Arya Samaj 2. Brahmo Samaj 3. Ramakrishna Mission 4. Prarthana Samaj",
            ["Brahmo 1828, Prarthana 1867, Arya 1875, Ramakrishna Mission 1897.", "So 2, 4, 1, 3."],
            "2, 4, 1, 3"),
        pat("ga-rf-p7", "Organisation ↔ place", "occasional",
            "\"Where was X founded?\" or \"headquarters of\" (New York, Adyar, Belur, Bombay, Aligarh).",
            ["Theosophical: founded in New York, Indian headquarters at Adyar (Madras).",
             "Ramakrishna Mission: Belur Math. Prarthana and Arya Samaj: Bombay.",
             "Brahmo: Calcutta. Singh Sabha: Amritsar. MAO College: Aligarh."],
            "Place questions often use the founding city as a trap against the later headquarters.",
            "The Theosophical Society was first founded at:",
            ["It later had its Indian headquarters at Adyar, which is the trap.", "Blavatsky and Olcott founded it abroad in 1875."],
            "New York"),
    ],
)

# ---------------------------------------------------------------- early-nationalism
S["early-nationalism"] = dict(
    concept=(
        "The Indian National Congress was founded in 1885. "
        "Its first leaders, the Moderates, asked the British for reforms through petitions. "
        "The Extremists wanted self-rule and used mass protest. "
        "From 1905 to 1916 came the Bengal partition, a Congress split, separate electorates and Home Rule."
    ),
    notes=r"""### The Congress is born (1885)
**A.O. Hume**, a retired British civil servant, called 72 Indian delegates to **Bombay**. They met at Gokuldas Tejpal Sanskrit College on **28 December 1885**. This was the first session of the **Indian National Congress (INC)**. The first president was **W.C. Bonnerjee**. The Viceroy was **Dufferin**.

Some said Hume wanted a "safety valve" to let out Indian anger. **Lala Lajpat Rai** argued this in his book *Young India*. Modern historians see the Congress as the first all-India political platform.

> **Watch:** The founder-organiser (Hume) was British. The first president (Bonnerjee) was Indian.

### The Moderates (1885–1905)
Moderates used petitions, prayers and protests, the "3P" method. They trusted British justice.

| Leader | Remember for |
|---|---|
| **Dadabhai Naoroji** | "Grand Old Man of India"; president three times; first Indian MP in the British House of Commons (1892); **Drain of Wealth** theory in *Poverty and Un-British Rule in India* (1901) |
| **Gopal Krishna Gokhale** | Servants of India Society (1905); **Gandhi's political guru** |
| **Surendranath Banerjea** | Indian Association (1876); paper *Bengalee* |
| Pherozeshah Mehta | "Lion of Bombay" |
| R.C. Dutt | *Economic History of India* |

The **drain of wealth** means India's money flowed to Britain as salaries, pensions and profits.

### The Extremists (1905–1919)
Extremists wanted self-rule (swaraj), not petitions. They used mass action, swadeshi and national education.
- **Lal-Bal-Pal:** **Lala Lajpat Rai** ("Punjab Kesari"), **Bal Gangadhar Tilak**, **Bipin Chandra Pal** (Bengal). **Aurobindo Ghosh** joined them.
- **Tilak:** papers *Kesari* (Marathi) and *Mahratta* (English). Started the **Ganapati (1893)** and **Shivaji (1895)** festivals.
- Tilak's slogan: **"Swaraj is my birthright and I shall have it."**
- Tilak was jailed in **Mandalay** (1908–14), where he wrote *Gita Rahasya*.

### Partition of Bengal and Swadeshi
**Lord Curzon** split Bengal. It took effect on **16 October 1905**. The stated reason was easier administration. The real aim was to weaken Bengali nationalism.
- East: **East Bengal and Assam**, Muslim-majority.
- West: Bengal, Hindu-majority.

The reply was the **Swadeshi and Boycott movement**:
- boycott of foreign cloth and salt;
- **Raksha Bandhan** as a sign of unity (Tagore's idea); *Amar Sonar Bangla* as the marching song;
- national schools (**National Council of Education, 1906**) and volunteer groups (samitis).

The partition was **annulled in 1911** at the Delhi Durbar, under **Hardinge**. The capital was to shift from Calcutta to **Delhi**.

### Year by year, 1906 to 1916
| Year | Event | Key fact |
|---|---|---|
| **1906** | **Muslim League** | Founded at **Dacca** (Nawab Salimullah). Backed the partition; soon asked for separate electorates. |
| 1906 | Calcutta session | President Naoroji; the word **Swaraj** first used in a Congress resolution |
| **1907** | **Surat split** | Moderates (president Rash Behari Ghosh) against Extremists (Tilak) |
| **1909** | **Morley–Minto Reforms** (Indian Councils Act) | **Separate electorates** for Muslims; Satyendra P. Sinha became the first Indian in the Viceroy's executive council. Minto: "father of communal electorates". |
| 1911 | Delhi Durbar | Partition annulled; capital to Delhi |
| **1916** | **Lucknow Pact** | Congress–League pact; Moderates and Extremists reunite; Congress accepted separate electorates |
| **1916** | **Home Rule Leagues** | **Tilak** (April, Belgaum; Maharashtra, Karnataka, Central Provinces, Berar) and **Annie Besant** (September, Madras; rest of India) |

Besant ran the papers *New India* and *Commonweal*. She became Congress president in 1917.

> **Tip:** 1905 split of Bengal → 1906 League → 1907 split of Congress → 1909 separate electorates.

### Early revolutionaries
- **Chapekar brothers**: Poona, 1897.
- **Khudiram Bose and Prafulla Chaki**: Muzaffarpur, 1908.
- **India House, London**: Shyamji Krishna Varma.
- **Ghadar Party (1913)**: **Lala Har Dayal**, Sohan Singh Bhakna; headquarters **Yugantar Ashram, San Francisco**.
- **Komagata Maru** incident: 1914.
""",
    tricks=[
        trick("Five-six-seven-nine: \"Split, League, Split, Separate\"",
              "**1905** Bengal split → **1906** Muslim League → **1907** Congress split (Surat) → **1909** separate electorates (Morley–Minto).",
              "Separate electorates for Muslims were first introduced by:",
              ["Separate electorates = the \"9\" in 5-6-7-9.", "1909 = Morley–Minto Reforms (Indian Councils Act)."],
              "Morley–Minto Reforms, 1909"),
        trick("Home Rule twins: \"TAB then BSM\"",
              "**T**ilak first (**A**pril, **B**elgaum) → **B**esant next (**S**eptember, **M**adras)."),
    ],
    mistakes=[
        mk("Putting the Surat split in 1905.", "Surat split = **1907**. 1905 is the Bengal partition."),
        mk("Calling Tilak Gandhi's political guru.", "Gandhi's political guru was the Moderate **Gokhale**."),
        mk("Saying the Lucknow Pact (1916) was between Moderates and Extremists only.",
           "The pact was between the **Congress and the Muslim League**. The two Congress wings also reunited there."),
        mk("Naming A.O. Hume the first Congress president.", "Hume organised it. The first president was **W.C. Bonnerjee**."),
        mk("Mixing Lajpat Rai's *Young India* with Gandhi's.",
           "Lajpat Rai's *Young India* is a **book**. Gandhi's *Young India* is a **journal**."),
        mk("Saying Besant's Home Rule League came first.", "**Tilak's** came first (April 1916). Besant's came in September 1916."),
    ],
    revision=[
        "INC: 28 Dec 1885, Bombay, 72 delegates; Hume organised; Bonnerjee presided; Viceroy Dufferin.",
        "Moderates: Naoroji (drain theory, first Indian MP 1892), Gokhale, S.N. Banerjea, Mehta, R.C. Dutt.",
        "Extremists: Lal-Bal-Pal + Aurobindo; Tilak = Kesari, Mahratta, Mandalay, Gita Rahasya.",
        "Curzon's partition effective 16 Oct 1905 → Swadeshi → annulled 1911.",
        "1906 League (Dacca) and Swaraj at Calcutta; 1907 Surat split; 1909 Morley–Minto separate electorates.",
        "1916: Lucknow Pact + Home Rule (Tilak April, Besant September).",
        "Ghadar Party 1913: Har Dayal, San Francisco; Komagata Maru 1914.",
    ],
    patterns=[
        pat("ga-en-p1", "Founding of the Congress", "very common",
            "\"The first session of the INC was held at\", founder, first president, number of delegates.",
            ["Place and date: Bombay, 28 December 1885.",
             "Organiser: A.O. Hume. First president: W.C. Bonnerjee.",
             "Delegates: 72. Viceroy: Dufferin."],
            "The same five facts cover every question on the founding.",
            "The first session of the Indian National Congress (1885) was presided over by:\n(a) A.O. Hume (b) W.C. Bonnerjee (c) Dadabhai Naoroji (d) Surendranath Banerjea",
            ["Hume organised it but did not preside; cut (a).", "The first president was Bonnerjee."],
            "(b) W.C. Bonnerjee"),
        pat("ga-en-p2", "Moderate leader ↔ work or title", "very common",
            "\"Drain of Wealth theory\", \"Grand Old Man of India\", \"Gandhi's political guru\", \"Lion of Bombay\".",
            ["Naoroji = drain theory, Grand Old Man, first Indian MP (1892).",
             "Gokhale = Servants of India Society, Gandhi's guru.",
             "Banerjea = Indian Association, *Bengalee*; Mehta = Lion of Bombay; R.C. Dutt = *Economic History of India*."],
            "Each Moderate has one title or book that the question uses as the clue.",
            "The Drain of Wealth theory was put forward by:",
            ["Drain of wealth = India's money flowing out as salaries, pensions and profits.",
             "It is in *Poverty and Un-British Rule in India* (1901)."],
            "Dadabhai Naoroji"),
        pat("ga-en-p3", "Extremist ↔ slogan, paper or festival", "very common",
            "\"Swaraj is my birthright\", *Kesari*, Ganapati festival, Lal-Bal-Pal, Punjab Kesari.",
            ["Tilak = *Kesari* + *Mahratta*, Ganapati 1893, Shivaji 1895, the Swaraj slogan.",
             "Lajpat Rai = Punjab Kesari; Pal = Bengal; Aurobindo = *Bande Mataram*.",
             "Check the language: *Kesari* Marathi, *Mahratta* English."],
            "Tilak owns most of the clues, so first test whether the answer is Tilak.",
            "The slogan \"Swaraj is my birthright and I shall have it\" was given by:",
            ["Swaraj slogan + Kesari editor = one leader.", "He was jailed in Mandalay."],
            "Bal Gangadhar Tilak"),
        pat("ga-en-p4", "Partition of Bengal and Swadeshi", "very common",
            "\"Partition of Bengal was annulled in\", which Viceroy, the two new provinces, Swadeshi methods.",
            ["Curzon; effective 16 October 1905.",
             "East Bengal and Assam (Muslim-majority) + West Bengal (Hindu-majority).",
             "Reply: Swadeshi, boycott, Raksha Bandhan, National Council of Education 1906.",
             "Annulled 1911 under Hardinge at the Delhi Durbar."],
            "The partition story has a fixed start (Curzon 1905) and end (Hardinge 1911).",
            "The partition of Bengal (1905) was annulled in:",
            ["Curzon made it; Hardinge undid it.", "The Delhi Durbar also announced the capital shift."],
            "1911"),
        pat("ga-en-p5", "Surat split, Muslim League and Lucknow reunion", "common",
            "\"The Congress split at Surat in\", League's founding place, Congress–League pact.",
            ["Surat 1907: Moderates (Rash Behari Ghosh) against Extremists (Tilak).",
             "Muslim League 1906 at Dacca, Nawab Salimullah.",
             "Lucknow 1916: reunion + Congress–League pact."],
            "Split in 1907 and reunion in 1916 bracket this whole period.",
            "The All India Muslim League was founded in 1906 at:",
            ["1906 League + Nawab Salimullah.", "It was founded in East Bengal's main city."],
            "Dacca"),
        pat("ga-en-p6", "Morley–Minto 1909 and Home Rule Leagues", "common",
            "\"Separate electorates were introduced by\", Home Rule Leagues — who, when, where.",
            ["Morley–Minto 1909 = separate electorates; S.P. Sinha in the council.",
             "Home Rule 1916: Tilak (April, Belgaum) and Besant (September, Madras).",
             "Besant's papers: *New India*, *Commonweal*."],
            "Both are linked to one year each: 1909 and 1916.",
            "Annie Besant started her Home Rule League in 1916 at:",
            ["Tilak started his first, in April, at Belgaum.", "Besant followed in September."],
            "Madras"),
        pat("ga-en-p7", "Arrange events of 1885–1916", "common",
            "\"Arrange in chronological order\" with INC, partition, League, Surat, Morley–Minto, Lucknow.",
            ["Write the year beside each item.",
             "Use the memory chain: 1885 → 1905 → 1906 → 1907 → 1909 → 1911 → 1916.",
             "Check first and last items against the options."],
            "Every event here has a different year, so sorting is exact.",
            "Arrange in order: 1. Surat split 2. Morley–Minto Reforms 3. Partition of Bengal 4. Lucknow Pact",
            ["Partition 1905, Surat 1907, Morley–Minto 1909, Lucknow 1916.", "So 3, 1, 2, 4."],
            "3, 1, 2, 4"),
        pat("ga-en-p8", "Early revolutionaries ↔ event", "occasional",
            "Khudiram Bose, Chapekar brothers, Ghadar Party, India House, Komagata Maru.",
            ["Chapekar brothers = Poona, 1897.", "Khudiram Bose and Prafulla Chaki = Muzaffarpur, 1908.",
             "Ghadar Party 1913 = Har Dayal, Yugantar Ashram, San Francisco.",
             "India House, London = Shyamji Krishna Varma."],
            "Each revolutionary group has one place, which is the usual clue.",
            "The Ghadar Party (1913) had its headquarters at:",
            ["Ghadar = Lala Har Dayal and Sohan Singh Bhakna.", "Headquarters: Yugantar Ashram in the USA."],
            "San Francisco"),
    ],
)

# ---------------------------------------------------------------- gandhian-era
S["gandhian-era"] = dict(
    concept=(
        "Gandhi returned to India in 1915 and led the freedom struggle through mass movements. "
        "Each movement has a year, a cause and an end. "
        "Exams mostly ask dates, places, session presidents and pacts, often as a chronological order question."
    ),
    notes=r"""### Gandhi's first three struggles
Gandhi landed in India on **9 January 1915**, now **Pravasi Bharatiya Divas**. He had built the method of **satyagraha** (truth-force, peaceful resistance) in South Africa from 1906.

| Year | Struggle | Key fact |
|---|---|---|
| **1917** | **Champaran**, Bihar | Against forced indigo growing (**tinkathia** system). **Rajkumar Shukla** brought Gandhi. His **first satyagraha in India**. |
| 1918 | **Ahmedabad** mill strike | For workers' plague bonus. His **first hunger strike**. |
| 1918 | **Kheda**, Gujarat | **No-revenue** campaign for famine-hit farmers, with **Vallabhbhai Patel** |

### Rowlatt to Swaraj Party (1919 to 1923)
- **Rowlatt Act (1919):** arrest without trial — "no dalil, no vakil, no appeal". A nationwide hartal followed.
- **Jallianwala Bagh, Amritsar (13 April 1919, Baisakhi):** **General Dyer** fired on an unarmed crowd. **Tagore** gave up his knighthood. The **Hunter Committee** enquired. **Udham Singh** shot Michael O'Dwyer in London (1940).
- **Khilafat movement** (Ali brothers): joined with Gandhi's **Non-Cooperation Movement (NCM)**. NCM began on **1 August 1920**. A Calcutta special session approved it; the Nagpur session ratified it. People boycotted schools, courts, titles and foreign cloth.
- **Chauri Chaura (5 February 1922, Gorakhpur):** a mob burnt a police station. Gandhi withdrew the NCM (Bardoli resolution).
- **Swaraj Party (1923):** **C.R. Das and Motilal Nehru**; they entered the councils.

### From Simon to Purna Swaraj
- **Simon Commission** (appointed 1927, arrived 1928): all-white, met with "**Simon Go Back**". **Lala Lajpat Rai** was hurt in a lathi charge at Lahore and died on 17 November 1928.
- **Nehru Report (1928)**, by Motilal Nehru: first Indian draft constitution; asked for Dominion Status.
- **Lahore session (December 1929)**: president **Jawaharlal Nehru**; **Purna Swaraj** (complete independence) resolution. **26 January 1930** was the first Independence Day.

### Civil Disobedience (1930–34)
Gandhi's **Dandi March** broke the salt law.
- Started **12 March 1930** from **Sabarmati Ashram** with **78** followers.
- About **385 km** (240 miles); salt law broken at Dandi on **6 April 1930**.

| Year | Event | Key fact |
|---|---|---|
| 1931 | **Gandhi–Irwin Pact** (5 March) | Ended this phase; Gandhi went alone to the **Second Round Table Conference** |
| 1931 | **Karachi session** | President **Vallabhbhai Patel**; resolution on **Fundamental Rights and Economic Policy** |
| 1932 | **Communal Award** | Separate electorates for the Depressed Classes |
| 1932 | **Poona Pact** (24 Sept) | **Gandhi and Ambedkar**: reserved seats instead, within joint electorates |
| 1935 | **Government of India Act** | Provincial autonomy; basis of much of the Constitution; Congress ministries 1937–39 |

### Quit India and the INA (1939–1945)
- **1939, Tripuri:** Subhas Bose was re-elected president, then resigned and formed the **Forward Bloc**.
- **1940:** August Offer; **Individual Satyagraha** — **Vinoba Bhave** was the first satyagrahi.
- **March 1942:** **Cripps Mission** — Gandhi called it a "post-dated cheque on a crashing bank".
- **8 August 1942:** **Quit India** resolution at **Gowalia Tank, Bombay**; slogan **"Do or Die"**. Leaders were arrested at once. **Aruna Asaf Ali** hoisted the flag. **Usha Mehta** ran the Congress Radio. Parallel governments came up at **Ballia** (Chittu Pandey), **Satara** (Nana Patil) and **Tamluk**.
- **21 October 1943:** **Subhas Bose** proclaimed the **Azad Hind Government** in **Singapore**. INA slogan: "**Delhi Chalo**". He also said "Give me blood, I will give you freedom". The **Rani Jhansi Regiment** was led by Lakshmi Sahgal.

### Road to freedom (1946–47)
| Date | Event |
|---|---|
| 1946 | RIN (navy) mutiny; **Cabinet Mission** — Pethick-Lawrence, Cripps, Alexander |
| 16 Aug 1946 | **Direct Action Day** |
| 2 Sept 1946 | Interim Government formed |
| 3 June 1947 | **Mountbatten Plan** |
| 18 July 1947 | Indian Independence Act |
| **15 Aug 1947** | Independence |

### Revolutionaries of the 1920s and 1930s
| Event | Date | People |
|---|---|---|
| **Kakori train action** | 9 Aug 1925 | **Ram Prasad Bismil, Ashfaqulla Khan** (HRA) |
| HSRA formed | 1928 | Bhagat Singh, **Chandrashekhar Azad** (Feroz Shah Kotla, Delhi) |
| Central Assembly bomb | **8 April 1929** | **Bhagat Singh and Batukeshwar Dutt** |
| Chittagong armoury raid | 1930 | **Surya Sen** |
| Hanged | **23 March 1931** | Bhagat Singh, Rajguru, Sukhdev (Martyrs' Day) |

> **Tip:** Session presidents: **Lahore 1929 = Jawaharlal**, **Karachi 1931 = Patel**, **Tripuri 1939 = Bose**.
""",
    tricks=[
        trick("Gandhi's first three: \"C-A-K, 17-18-18\"",
              "**C**hamparan 1917 (indigo, Bihar) → **A**hmedabad 1918 (mill workers, hunger strike) → **K**heda 1918 (farmers, revenue).",
              "Gandhi's first hunger strike in India was during:",
              ["Hunger strike = the \"A\" in C-A-K.", "Ahmedabad 1918, for the mill workers' bonus."],
              "Ahmedabad mill strike, 1918"),
        trick("Session presidents: \"J-P-B\" from 29 to 39",
              "**Lahore 1929 = Jawaharlal** (Purna Swaraj) · **Karachi 1931 = Patel** (Fundamental Rights) · **Tripuri 1939 = Bose**."),
        trick("Dandi numbers",
              "**12 March** start · **6 April** salt law broken · **78** marchers · about **385 km** (240 miles) · from **Sabarmati Ashram**."),
    ],
    mistakes=[
        mk("Saying Purna Swaraj was declared on 26 January 1930.",
           "It was **adopted at Lahore in December 1929**. 26 January 1930 was the first Independence Day."),
        mk("Saying the Poona Pact was between Gandhi and Irwin.",
           "Poona Pact (1932) = **Gandhi and Ambedkar**. Gandhi–Irwin Pact = 1931."),
        mk("Placing the Quit India launch in Delhi.", "Quit India was launched at **Gowalia Tank, Bombay**, on 8 August 1942."),
        mk("Saying the Azad Hind Government was set up in Rangoon or Tokyo.", "It was proclaimed in **Singapore** (21 October 1943)."),
        mk("Calling Champaran Gandhi's first hunger strike.",
           "Champaran (1917) was his first **satyagraha** in India. The first **hunger strike** was at Ahmedabad (1918)."),
        mk("Mixing the Communal Award and the Poona Pact.",
           "Communal Award gave **separate** electorates. Poona Pact replaced them with **reserved seats in joint** electorates."),
    ],
    revision=[
        "Return 9 Jan 1915 → Champaran 1917 → Ahmedabad and Kheda 1918.",
        "1919: Rowlatt Act → Jallianwala (13 April, Dyer) → Tagore gives up knighthood.",
        "NCM 1 Aug 1920 → Chauri Chaura 5 Feb 1922 → Swaraj Party 1923.",
        "Simon 1928 → Nehru Report 1928 → Lahore 1929 (Purna Swaraj) → 26 Jan 1930.",
        "Dandi 12 March–6 April 1930 → Gandhi–Irwin 5 March 1931 → Poona Pact 24 Sept 1932.",
        "Quit India 8 Aug 1942, Gowalia Tank, \"Do or Die\"; Azad Hind, Singapore, 21 Oct 1943.",
        "Mountbatten Plan 3 June 1947 → Independence Act 18 July → 15 Aug 1947.",
        "Bhagat Singh: Assembly bomb 8 April 1929; hanged 23 March 1931.",
    ],
    patterns=[
        pat("ga-ge-p1", "Gandhi's early satyagrahas", "very common",
            "\"Gandhi's first satyagraha in India\", tinkathia, first hunger strike, no-revenue campaign.",
            ["Champaran 1917 = indigo, tinkathia, Bihar, first satyagraha.",
             "Ahmedabad 1918 = mill workers, first hunger strike.",
             "Kheda 1918 = no revenue, with Patel."],
            "The three struggles differ in one word each: indigo, mill, revenue.",
            "In which struggle did Gandhi first use a hunger strike in India?\n(a) Champaran (b) Kheda (c) Ahmedabad mill strike (d) Bardoli",
            ["Champaran = first satyagraha, not hunger strike; cut (a).",
             "Kheda = no-revenue; Bardoli (1928) was Patel's movement."],
            "(c) Ahmedabad mill strike, 1918"),
        pat("ga-ge-p2", "Rowlatt Act and Jallianwala Bagh", "very common",
            "\"No dalil, no vakil, no appeal\", Jallianwala date, General Dyer, reactions.",
            ["Rowlatt Act 1919 = arrest without trial.",
             "Jallianwala: 13 April 1919, Baisakhi, Amritsar, General Dyer.",
             "Reactions: Tagore gave up his knighthood; Hunter Committee; Udham Singh shot O'Dwyer (1940)."],
            "The Rowlatt Act led straight to the Amritsar meeting, so the facts come as a set.",
            "Who gave up his knighthood in protest against the Jallianwala Bagh massacre?",
            ["Massacre: 13 April 1919.", "The poet who returned his title was Tagore."],
            "Rabindranath Tagore"),
        pat("ga-ge-p3", "Non-Cooperation and Chauri Chaura", "very common",
            "\"Why was the NCM withdrawn?\", Chauri Chaura, Khilafat, Swaraj Party.",
            ["NCM began 1 August 1920, joined with Khilafat.",
             "Chauri Chaura, 5 February 1922: police station burnt, NCM withdrawn.",
             "Swaraj Party 1923: C.R. Das and Motilal Nehru."],
            "Violence at Chauri Chaura broke Gandhi's non-violence rule, so he stopped the movement.",
            "The Non-Cooperation Movement was withdrawn in 1922 after the incident at:",
            ["1922 + violence + police station.", "The place was in Gorakhpur district."],
            "Chauri Chaura"),
        pat("ga-ge-p4", "Dandi March and the pacts", "very common",
            "Dandi dates, salt law, Gandhi–Irwin Pact, Round Table Conference, Communal Award, Poona Pact.",
            ["Dandi: 12 March–6 April 1930, 78 marchers, from Sabarmati.",
             "Gandhi–Irwin Pact: 5 March 1931; then Second Round Table Conference.",
             "Communal Award 1932 → Poona Pact 1932 (Gandhi and Ambedkar)."],
            "One pact per year: 1931 with Irwin, 1932 with Ambedkar.",
            "The Poona Pact of 1932 was signed between Gandhi and:\n(a) Lord Irwin (b) B.R. Ambedkar (c) Jinnah (d) Subhas Bose",
            ["Irwin is the 1931 pact; cut (a).", "The Poona Pact settled seats for the Depressed Classes."],
            "(b) B.R. Ambedkar"),
        pat("ga-ge-p5", "Simon Commission to Purna Swaraj", "common",
            "Simon Commission, Lajpat Rai's death, Nehru Report, Lahore 1929, 26 January 1930.",
            ["Simon: appointed 1927, arrived 1928, all-white, \"Simon Go Back\".",
             "Lajpat Rai hurt at Lahore; died 17 November 1928.",
             "Nehru Report 1928 (Motilal); Lahore December 1929 (Jawaharlal), Purna Swaraj."],
            "Each step answered the previous one, so the order is fixed.",
            "The Purna Swaraj resolution was passed at the Lahore session under the presidency of:",
            ["Lahore, December 1929.", "Session presidents: Lahore = Jawaharlal."],
            "Jawaharlal Nehru"),
        pat("ga-ge-p6", "Quit India, INA and the last steps", "common",
            "\"Do or Die\", Gowalia Tank, parallel governments, Azad Hind, Cabinet Mission, Mountbatten Plan.",
            ["Quit India: 8 August 1942, Gowalia Tank, Bombay, \"Do or Die\".",
             "Heroes: Aruna Asaf Ali (flag), Usha Mehta (radio); Ballia, Satara, Tamluk.",
             "Bose: Azad Hind, Singapore, 21 October 1943.",
             "Cabinet Mission 1946 → Mountbatten Plan 3 June 1947 → 15 August 1947."],
            "The last five years have many firsts, but each name has one clear role.",
            "Aruna Asaf Ali is remembered in the Quit India Movement for:",
            ["Leaders were arrested the night of 8 August 1942.", "She raised the flag at Gowalia Tank, Bombay."],
            "Hoisting the flag at Gowalia Tank"),
        pat("ga-ge-p7", "Arrange freedom-movement events in order", "very common",
            "\"Arrange in chronological order\" with any four events from 1915 to 1947.",
            ["Write the year (and month if two share a year) beside each item.",
             "Find the earliest; keep only options that start with it.",
             "Check the last item to pick between the rest."],
            "This is the most asked question type in the topic, and years settle it.",
            "Arrange in order: 1. Dandi March 2. Chauri Chaura 3. Quit India 4. Jallianwala Bagh",
            ["Jallianwala 1919, Chauri Chaura 1922, Dandi 1930, Quit India 1942.", "So 4, 2, 1, 3."],
            "4, 2, 1, 3"),
        pat("ga-ge-p8", "Revolutionary ↔ action", "common",
            "Kakori, Assembly bomb, Chittagong raid, HSRA, Bhagat Singh's execution.",
            ["Kakori 1925 = Bismil, Ashfaqulla Khan.",
             "HSRA 1928 = Bhagat Singh, Chandrashekhar Azad.",
             "Assembly bomb 8 April 1929 = Bhagat Singh, B.K. Dutt; Chittagong 1930 = Surya Sen.",
             "23 March 1931 = Bhagat Singh, Rajguru, Sukhdev hanged."],
            "Each action has one or two names, so match the event first.",
            "Who threw a bomb in the Central Legislative Assembly on 8 April 1929 along with Bhagat Singh?",
            ["Rajguru and Sukhdev were hanged with him but did not throw the bomb.", "His partner in the Assembly was B.K. Dutt."],
            "Batukeshwar Dutt"),
    ],
)

# ---------------------------------------------------------------- press-books
S["press-books"] = dict(
    concept=(
        "Newspapers and books spread the ideas of the freedom movement across India. "
        "Most questions name a paper or a book and ask who started or wrote it. "
        "Learn each one as a pair: paper with editor, book with author."
    ),
    notes=r"""### Why the press mattered
The national movement ran on print. Newspapers built all-India opinion and spread calls for boycott. Their editors often faced cases and jail.

Learn three things for each paper: its editor, its language and its year.

> **Example:** *Kesari* → Tilak → Marathi. *Mahratta* → Tilak → English.

### The first papers and press laws
- ***Bengal Gazette* (1780)**: **James Augustus Hicky**. The first newspaper in India, in English.
- **Raja Ram Mohan Roy**: *Sambad Kaumudi* (Bengali, 1821) and *Mirat-ul-Akbar* (Persian, 1822).
- **Metcalfe (1835)** was called the "liberator of the Indian press".
- ***Amrita Bazar Patrika* (1868)**: the Ghosh brothers, Sisir Kumar and Motilal. It began in Bengali.
- ***The Hindu* (1878, Madras)**: **G. Subramania Iyer**.
- **Vernacular Press Act (1878)**: Lytton's "Gagging Act". It gagged Indian-language papers. *Amrita Bazar Patrika* became an English paper **overnight** to escape it. **Ripon** repealed the Act in **1882**.

### Papers of the freedom struggle
| Paper | Language | Person |
|---|---|---|
| *Bengalee* | English | Surendranath Banerjea |
| *Kesari* / *Mahratta* (1881) | Marathi / English | **Bal Gangadhar Tilak** |
| *Indian Opinion* (1903) | English, Gujarati and others | Gandhi (South Africa) |
| *Young India* / *Navajivan* | English / Gujarati | **Gandhi**, in the Non-Cooperation years |
| ***Harijan*** (1933) | English weekly | **Gandhi**, against untouchability |
| ***Al-Hilal*** (1912), *Al-Balagh* | Urdu | **Maulana Abul Kalam Azad** |
| *Comrade* | English | Mohammad Ali Jauhar (one of the Ali brothers) |
| *Bande Mataram* | English | **Aurobindo Ghosh**, with Bipin Chandra Pal |
| *New India*, *Commonweal* | English | **Annie Besant** |
| *Mooknayak* (1920) | Marathi | **B.R. Ambedkar** |
| *National Herald* (1938) | English | Jawaharlal Nehru |
| *Tahdhib-ul-Akhlaq* | — | Sir Syed Ahmad Khan (Aligarh message) |

*Harijan* also had sister papers: *Harijan Bandhu* (Gujarati) and *Harijan Sevak* (Hindi).

> **Tip:** Gandhi's papers are **Y-N-H**: *Young India*, *Navajivan*, *Harijan* (plus *Indian Opinion* in South Africa).

### Books and their authors
| Book | Author |
|---|---|
| *Poverty and Un-British Rule in India* (1901) | **Dadabhai Naoroji** (drain theory) |
| *Economic History of India* | R.C. Dutt |
| *Anandamath* (1882) | **Bankim Chandra Chattopadhyay** |
| *Gita Rahasya* | Tilak, written in **Mandalay** jail |
| ***Hind Swaraj*** (1909) | **Gandhi** |
| *My Experiments with Truth* (autobiography, 1927) | Gandhi |
| *Gulamgiri* (1873) | Jyotirao Phule |
| *Annihilation of Caste* (1936) | B.R. Ambedkar |
| *The Indian Struggle* (1935) | Subhas Chandra Bose |
| *Glimpses of World History* (1934) | Jawaharlal Nehru |
| *Toward Freedom* (autobiography, 1936) | Jawaharlal Nehru |
| *The Discovery of India* (1946) | Jawaharlal Nehru, written in **Ahmednagar Fort** jail |
| *India Wins Freedom* | Maulana Abul Kalam Azad |
| *India Divided* | Rajendra Prasad |
| *Unhappy India* (1928) | Lala Lajpat Rai; a reply to Katherine Mayo's *Mother India* |
| *Why I Am an Atheist* | Bhagat Singh |
| *Neel Darpan* (play) | Dinabandhu Mitra |

> **Rule:** Nehru has three books to know: *Glimpses* (1934), *Toward Freedom* (1936), *Discovery* (1946).

### Songs that came from print
- **Vande Mataram** comes from Bankim Chandra's novel ***Anandamath*** (1882). **Tagore** first sang it at the **1896 Calcutta Congress session**.
- **Tagore** wrote ***Amar Sonar Bangla*** during the 1905 Swadeshi movement. It later became Bangladesh's national anthem.
- *Jana Gana Mana* is also by **Tagore**, not Bankim.
""",
    tricks=[
        trick("Gandhi's papers: \"YNH\"",
              "**Y**oung India · **N**avajivan · **H**arijan (plus *Indian Opinion* from South Africa). Any other paper in the options belongs to someone else.",
              "Which of these was NOT edited by Gandhi: Young India, Harijan, Kesari, Navajivan?",
              ["Y-N-H covers Young India, Navajivan and Harijan.", "Kesari is left over; it was Tilak's Marathi paper."],
              "Kesari"),
        trick("Books written in jail",
              "Tilak → *Gita Rahasya* in **Mandalay**. Nehru → *The Discovery of India* in **Ahmednagar Fort**."),
    ],
    mistakes=[
        mk("Giving *Al-Hilal* to Mohammad Ali.", "*Al-Hilal* = **Abul Kalam Azad**. *Comrade* = **Mohammad Ali Jauhar**."),
        mk("Saying *Anandamath* was written by Tagore.",
           "*Anandamath* is by **Bankim Chandra**. *Jana Gana Mana* and *Amar Sonar Bangla* are by **Tagore**."),
        mk("Saying Ripon passed the Vernacular Press Act.", "**Lytton** passed it (1878). **Ripon** repealed it (1882)."),
        mk("Giving *New India* to Bipin Chandra Pal or Nehru.", "*New India* was **Annie Besant's** paper, with *Commonweal*."),
        mk("Mixing Naoroji's and R.C. Dutt's books.",
           "Naoroji = *Poverty and Un-British Rule in India*. Dutt = *Economic History of India*."),
    ],
    revision=[
        "First newspaper: Bengal Gazette (1780), James Augustus Hicky.",
        "Roy: Sambad Kaumudi (Bengali) + Mirat-ul-Akbar (Persian).",
        "Vernacular Press Act 1878 (Lytton) → repealed 1882 (Ripon); Amrita Bazar Patrika turned English overnight.",
        "Tilak: Kesari + Mahratta; Besant: New India + Commonweal; Azad: Al-Hilal; Ambedkar: Mooknayak.",
        "Gandhi: Indian Opinion, Young India, Navajivan, Harijan (1933); Hind Swaraj (1909).",
        "Nehru: Glimpses 1934, Toward Freedom 1936, Discovery of India 1946.",
        "Vande Mataram from Anandamath (1882), first sung by Tagore at Calcutta, 1896.",
    ],
    patterns=[
        pat("ga-pb-p1", "Newspaper ↔ editor or founder", "very common",
            "\"Who edited Kesari?\", \"New India was published by\", or a match-the-column of papers and editors.",
            ["Recall the big four: Tilak (Kesari, Mahratta), Gandhi (Young India, Navajivan, Harijan), Besant (New India, Commonweal), Azad (Al-Hilal).",
             "Then the rest: Banerjea (Bengalee), Mohammad Ali (Comrade), Aurobindo (Bande Mataram), Ambedkar (Mooknayak).",
             "Match the sure pairs first and cut options."],
            "Each paper has one main editor, so one sure pair clears most options.",
            "The newspaper *New India*, which carried the Home Rule campaign, was started by:\n(a) Bipin Chandra Pal (b) Annie Besant (c) Jawaharlal Nehru (d) Tilak",
            ["Home Rule + *New India* point to the September 1916 League leader.",
             "Nehru's paper was *National Herald*; Tilak's was *Kesari*."],
            "(b) Annie Besant"),
        pat("ga-pb-p2", "Book ↔ author", "very common",
            "\"Who wrote The Discovery of India?\", \"Gulamgiri is a work of\", or a book–author match.",
            ["Gandhi: Hind Swaraj, My Experiments with Truth.",
             "Nehru: Glimpses, Toward Freedom, Discovery of India.",
             "Naoroji vs R.C. Dutt: Poverty and Un-British Rule vs Economic History.",
             "Azad: India Wins Freedom; Prasad: India Divided; Bose: The Indian Struggle; Ambedkar: Annihilation of Caste."],
            "Most book questions draw from this short list of leaders.",
            "The book *The Discovery of India* was written by:",
            ["It was written in Ahmednagar Fort jail and published in 1946.", "It is one of Nehru's three books."],
            "Jawaharlal Nehru"),
        pat("ga-pb-p3", "Press laws", "common",
            "\"Vernacular Press Act was passed/repealed by\", \"liberator of the Indian press\", paper that changed language overnight.",
            ["Vernacular Press Act 1878 = Lytton.", "Repealed 1882 = Ripon.",
             "Metcalfe 1835 = liberator of the press.", "Amrita Bazar Patrika became English overnight."],
            "Only three names and one paper appear in press-law questions.",
            "The Vernacular Press Act (1878) was repealed by:",
            ["Lytton passed it in 1878.", "Ripon, the next reformer Viceroy, repealed it in 1882."],
            "Lord Ripon (1882)"),
        pat("ga-pb-p4", "Gandhi's journals", "common",
            "\"Harijan was started in\", paper of the Non-Cooperation years, language of Navajivan.",
            ["South Africa: Indian Opinion (1903).",
             "Non-Cooperation: Young India (English), Navajivan (Gujarati).",
             "Harijan (1933): English weekly; Harijan Bandhu (Gujarati), Harijan Sevak (Hindi)."],
            "Gandhi's papers change with his phase of work, so the year points to the paper.",
            "Gandhi started the English weekly *Harijan* in:",
            ["*Harijan* was for the campaign against untouchability.", "It came after Civil Disobedience began."],
            "1933"),
        pat("ga-pb-p5", "Anandamath, Vande Mataram and protest writing", "common",
            "Source of Vande Mataram, where it was first sung, Amar Sonar Bangla, Unhappy India.",
            ["Vande Mataram: from Anandamath (1882), Bankim Chandra.",
             "First sung by Tagore at the 1896 Calcutta Congress.",
             "Amar Sonar Bangla: Tagore, 1905; later Bangladesh's anthem.",
             "Unhappy India (1928): Lajpat Rai's reply to *Mother India*."],
            "Song questions test the book, the writer and the first singing together.",
            "The song Vande Mataram first appeared in:",
            ["The song is by Bankim Chandra.", "It is part of his 1882 novel."],
            "Anandamath"),
        pat("ga-pb-p6", "Odd one out: not by this person", "common",
            "\"Which of these was NOT edited/written by X?\"",
            ["List X's papers or books from memory.",
             "Tick every option that is on the list.",
             "The option left over is the answer; check who it really belongs to."],
            "Knowing a person's full list is faster than checking each option alone.",
            "Which of these books was NOT written by Jawaharlal Nehru?\n(a) Glimpses of World History (b) Toward Freedom (c) India Wins Freedom (d) The Discovery of India",
            ["Nehru's three: Glimpses, Toward Freedom, Discovery.", "*India Wins Freedom* is by Maulana Azad."],
            "(c) India Wins Freedom"),
        pat("ga-pb-p7", "Language of a paper", "occasional",
            "\"Kesari was published in which language?\" or \"Al-Hilal was an ___ weekly\".",
            ["Marathi: Kesari, Mooknayak. English: Mahratta, Young India, New India, Bengalee.",
             "Gujarati: Navajivan. Urdu: Al-Hilal. Bengali: Sambad Kaumudi. Persian: Mirat-ul-Akbar.",
             "Watch pairs by one editor that use two languages."],
            "Some editors ran two papers in two languages, which is the usual trap.",
            "*Mirat-ul-Akbar*, started by Ram Mohan Roy in 1822, was published in:",
            ["Roy had two papers.", "Sambad Kaumudi was Bengali; Mirat-ul-Akbar was the other one."],
            "Persian"),
    ],
)

# ---------------------------------------------------------------- apply
data = json.loads(TOPIC.read_text(encoding="utf-8"))
by_id = {s["id"]: s for s in data["subtopics"]}
assert set(S) == set(by_id), (set(S) ^ set(by_id))
new_ids = [p["id"] for s in S.values() for p in s["patterns"]]
assert len(new_ids) == len(set(new_ids)), "duplicate pattern id"
for sid, new in S.items():
    sub = by_id[sid]
    old = {p["id"] for p in sub.get("patterns", [])}
    assert old <= {p["id"] for p in new["patterns"]}, (sid, old)
    n = new["notes"].strip() + "\n"
    assert 2500 <= len(n) <= 5000, (sid, len(n))
    sub.update(concept=new["concept"], notes=n, patterns=new["patterns"], mistakes=new["mistakes"],
               revision=new["revision"], tricks=new["tricks"])
    print(f"{sid}: notes {len(n)} chars, {len(new['patterns'])} patterns (was {len(old)})")
TOPIC.write_text(json.dumps(data, ensure_ascii=False, indent=1) + "\n", encoding="utf-8")
