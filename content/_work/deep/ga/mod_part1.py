"""modern-history deep content — part 1: british-expansion, revolt-1857, reform-movements."""
import os
import sys

sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
from _lib import Sub


def build_british():
    S = Sub("british-expansion")
    S.notes = """### From traders to rulers
The East India Company got its charter in **1600** and its first factory at **Surat** (1612, after the naval win over the Portuguese). It then built three presidencies: **Madras (1639)**, **Bombay (1668, from Charles II's dowry)** and **Calcutta (1690, Job Charnock)**. After beating the French (Dupleix) in the **Carnatic wars**, the Company turned on Bengal: at **Plassey (1757)** Robert Clive defeated **Siraj-ud-Daulah** through **Mir Jafar's** betrayal; at **Buxar (1764)** it defeated the combined armies of **Mir Qasim, Shuja-ud-Daula and Emperor Shah Alam II**. The **Treaty of Allahabad (1765)** gave the Company the **Diwani** (revenue rights) of Bengal-Bihar-Odisha; Clive's 'dual government' (1765–72) was ended by **Warren Hastings**, the first Governor-General under the **Regulating Act 1773** (Pitt's India Act 1784 added dual control).

### Wars that made the empire
- **Mysore:** four wars against Haidar Ali and **Tipu Sultan**; Tipu — the 'Tiger of Mysore' — died defending **Srirangapatna in 1799** (Fourth war, Wellesley).
- **Marathas:** three Anglo-Maratha wars ended Maratha power (**1818**).
- **Sikhs:** two wars after Ranjit Singh's death (1839) — Punjab **annexed 1849** (Dalhousie).
- **Others:** Sind (1843, Napier), Burma, Awadh annexed 1856 'for misgovernment'.
- **Subsidiary Alliance** (Wellesley, Nizam first in 1798): the ally kept Company troops and lost independence; **Doctrine of Lapse** (Dalhousie): adopted heirs refused — **Satara, Jaitpur, Sambalpur, Udaipur, Jhansi, Nagpur** lapsed.

### Governor-Generals' landmarks
**Cornwallis** (1786–93): **Permanent Settlement (1793)**, police and judicial reforms, 'father of the Indian civil service'. **William Bentinck** (1828–35): **sati abolished (1829)**, English education (Macaulay's Minute 1835), thuggee suppressed. **Dalhousie** (1848–56): railways (1853), telegraph, postage, engineering colleges — the infrastructure age plus annexations. **Lytton**: **Vernacular Press Act (1878)**, Arms Act, and the Delhi Durbar of 1877 proclaiming Victoria 'Empress of India'.

### The three land-revenue systems
| System | Region | Key feature |
|---|---|---|
| **Permanent Settlement (1793)** | Bengal-Bihar-Odisha | Zamindars fixed as landowners; revenue fixed forever (Cornwallis) |
| **Ryotwari** | Madras, Bombay | Settlement directly with the **ryot** (cultivator); Reed & **Thomas Munro** |
| **Mahalwari** | North-Western Provinces, Central India, parts of Punjab | Settlement with the **village estate (mahal)**; Holt Mackenzie, 1822 |

### Quick revision
- Plassey 1757 (Mir Jafar) → Buxar 1764 (triple alliance beaten) → Diwani 1765 (Treaty of Allahabad).
- Tipu died 1799 at Srirangapatna; Marathas ended 1818; Punjab 1849.
- Wellesley = Subsidiary Alliance; Dalhousie = Doctrine of Lapse + railways; Lytton = Vernacular Press Act 1878.
- Revenue trio: Permanent (Cornwallis, zamindari), Ryotwari (Munro, ryot), Mahalwari (Holt Mackenzie, village)."""
    S.pattern("ga-be-p1", "Company victories: Plassey → Buxar → Diwani chain", "very common",
        "'Who was defeated at Buxar', what the Treaty of Allahabad granted, Mir Jafar's role, order of events 1757-1765.",
        None,
        "1. **Plassey 1757** = Clive vs Siraj-ud-Daulah (Mir Jafar betrayed); **Buxar 1764** = vs Mir Qasim + Shuja-ud-Daula + Shah Alam II.\n2. **Treaty of Allahabad 1765** = **Diwani of Bengal, Bihar, Odisha** to the Company.\n3. Diwani means revenue-collection rights — not territory ownership.",
        "The **Battle of Buxar (1764)** was fought against a combined army of Mir Qasim, Shuja-ud-Daula and —",
        "**Emperor Shah Alam II** — after which the Treaty of Allahabad granted the Company the Diwani.")
    S.pattern("ga-be-p2", "Anglo wars: Mysore, Maratha, Sikh", "very common",
        "'Tipu Sultan died in which battle/war', which war ended Maratha power, year of Punjab's annexation.",
        None,
        "1. Mysore: four wars; **Tipu died at Srirangapatna, 1799** (Fourth war).\n2. Marathas: **three wars; power ended 1818**.\n3. Sikhs: two wars; **Punjab annexed 1849** (Dalhousie).",
        "Tipu Sultan was killed in **1799** at —",
        "**Srirangapatna**, during the Fourth Anglo-Mysore War.")
    S.pattern("ga-be-p3", "Governor-General ↔ policy and landmark measure", "very common",
        "'Sati was abolished by', Vernacular Press Act, Doctrine of Lapse, railways, English education — who did what.",
        None,
        "1. Cornwallis = Permanent Settlement; Bentinck = sati (1829) + English education; Dalhousie = Lapse + railways; Wellesley = Subsidiary Alliance; Lytton = Vernacular Press Act 1878.\n2. Read 'Governor-General of Bengal (1772-93)' vs 'of India (from 1833)' carefully — the title changed.\n3. In NOT-pair questions, the mismatched one usually swaps a measure between two neighbours.",
        "The **Vernacular Press Act (1878)** was passed by —",
        "**Lord Lytton** — it gagged Indian-language newspapers (repealed by Ripon in 1882).")
    S.pattern("ga-be-p4", "Land-revenue systems: zamindari, ryotwari, mahalwari", "common",
        "'The Ryotwari system was introduced by', which region had Mahalwari, Permanent Settlement features.",
        None,
        "1. **Permanent Settlement 1793 (Cornwallis)** — Bengal-Bihar-Odisha, zamindari, revenue fixed.\n2. **Ryotwari (Reed & Thomas Munro)** — Madras and Bombay; settlement with each cultivator.\n3. **Mahalwari (Holt Mackenzie, 1822)** — NW Provinces, Central India, parts of Punjab; village estate (mahal).",
        "The **Ryotwari** system, settling revenue directly with each cultivator, was developed mainly in —",
        "**Madras and Bombay** presidencies, associated with Reed and **Thomas Munro**.")

    S.q("ga-be-p1", "easy", "The **Battle of Buxar** was fought in —",
        ["1757", "1764", "1773", "1784"], "1764",
        "**Buxar, 1764**: the Company's army under Hector Munro defeated the combined forces of Mir Qasim, Shuja-ud-Daula and Shah Alam II.",
        "Plassey 1757, Buxar 1764.", 20)
    S.q("ga-be-p1", "easy", "The first **Governor-General of Bengal** (under the Regulating Act, 1773) was —",
        ["Robert Clive", "Warren Hastings", "Lord Cornwallis", "John Shore"], "Warren Hastings",
        "**Warren Hastings** became Governor-General of Bengal in 1773; the title 'Governor-General of India' began with William Bentinck (1833).",
        "Hastings first GG; Bentinck first 'of India'.", 20)
    S.q("ga-be-p2", "easy", "Tipu Sultan is called the **'Tiger of Mysore'**. He was killed in —",
        ["Third Anglo-Mysore War", "Fourth Anglo-Mysore War", "Battle of Buxar", "Second Anglo-Maratha War"], "Fourth Anglo-Mysore War",
        "Tipu died defending his capital **Srirangapatna** in the **Fourth Anglo-Mysore War (1799)** under Lord Wellesley.",
        "Tipu 1799 = Fourth war.", 20)
    S.q("ga-be-p2", "medium", "Under the **Doctrine of Lapse**, whose adoption claim as heir was rejected, leading to annexation?",
        ["Rani Lakshmibai of Jhansi", "Baji Rao II", "Nana Saheb of Bithur", "Tipu Sultan's son"], "Rani Lakshmibai of Jhansi",
        "**Dalhousie's Doctrine of Lapse** refused recognition to adopted heirs — Jhansi (Lakshmibai), Satara, Nagpur and others lapsed. Nana Saheb's pension claim was refused too.",
        "Lapse victims: Satara, Jhansi, Nagpur...", 25)
    S.q("ga-be-p3", "medium", "**English** was made the medium of higher education in India (Macaulay's Minute, 1835) under —",
        ["Lord Cornwallis", "Lord William Bentinck", "Lord Dalhousie", "Lord Ripon"], "Lord William Bentinck",
        "**Bentinck** accepted **Macaulay's Minute (1835)**, making English the medium of higher education; he also abolished sati (1829).",
        "Bentinck = 1829 sati + 1835 English.", 25)
    S.q("ga-be-p3", "hard", "Consider the statements:\n1. The Vernacular Press Act was passed in 1878.\n2. The Delhi Durbar of 1877 proclaimed Victoria 'Empress of India'.\n3. The Arms Act of Lytton's time disarmed Indians.\nWhich are correct?",
        ["1 and 2 only", "2 and 3 only", "1 and 3 only", "1, 2 and 3"], "1, 2 and 3",
        "All three belong to **Lytton's** tenure (1876–80): the press gag (1878), the 1877 Durbar, and the Arms Act.",
        "Lytton's trio: press gag, Arms Act, Durbar.", 30)
    S.q("ga-be-p4", "medium", "In the **Mahalwari** system, the unit of settlement was —",
        ["The individual ryot", "The zamindar's estate", "The village estate (mahal)", "The presidency"], "The village estate (mahal)",
        "**Mahalwari** settlement was made with the **village estate** as a whole (North-Western Provinces, Central India, parts of Punjab), following Holt Mackenzie's 1822 rules.",
        "Mahal = village estate.", 25)
    S.q("ga-be-p4", "hard", "Match:\n1. Permanent Settlement — Cornwallis\n2. Ryotwari — Thomas Munro\n3. Mahalwari — Lord Wellesley\nWhich pairs are correct?",
        ["1 and 2 only", "2 and 3 only", "1 and 3 only", "1, 2 and 3"], "1 and 2 only",
        "**Cornwallis** (Permanent Settlement) and **Munro** (Ryotwari) are right; **Mahalwari** is associated with **Holt Mackenzie**, not Wellesley.",
        "Wellesley belongs to Subsidiary Alliance — a classic distractor.", 30)
    return S


def build_revolt():
    S = Sub("revolt-1857")
    S.notes = """### The spark and the tinder
On **29 March 1857** at **Barrackpore**, **Mangal Pandey** of the **34th Native Infantry** attacked his officers over the **greased cartridges** of the new Enfield rifle (rumoured greased with cow and pig fat) — he was hanged on 8 April. On **10 May 1857** the sepoys at **Meerut** (85 troopers of the 3rd Light Cavalry, dismissed for refusing cartridges, were jailed) broke out, marched to Delhi and proclaimed the old **Bahadur Shah II** 'Emperor of India'. The greased cartridge was only the **immediate cause**.

### Deeper causes
- **Political:** Doctrine of Lapse annexations (Satara, Jhansi, Nagpur), Awadh annexed (1856), disrespect to the Mughal house, Nana Saheb's pension denied.
- **Economic:** heavy land revenue, ruin of handicrafts (de-industrialisation), drain of wealth, loss of zamindari and talukdari rights.
- **Social-religious:** reform laws (sati abolition), the Religious Disabilities Act (1850, converts could inherit), rumours about railways-telegraphs, missionary activity.
- **Military:** sepoys' pay and promotion grievances, the **General Service Enlistment Act (1856)** (service across the sea, feared caste-loss), Indians barred from officer ranks.

### Centres and leaders
| Centre | Leader |
|---|---|
| Delhi | Bahadur Shah II (general **Bakht Khan**) |
| **Kanpur** | **Nana Saheb** (with **Tantia Tope**, Azimullah Khan) |
| **Lucknow** | **Begum Hazrat Mahal** |
| **Jhansi** | **Rani Lakshmibai** |
| **Arrah/Jagdishpur (Bihar)** | **Kunwar Singh** |
| Faizabad | **Maulvi Ahmadullah Shah** |
| **Bareilly** | **Khan Bahadur Khan** |

The revolt spread through the Ganga plain, central India and parts of the Deccan; Bombay, Madras, Punjab (mostly) and Bengal proper stayed quiet — so it is called a 'sepoy mutiny' by some historians and the 'First War of Independence' (V.D. Savarkar's phrase) by others.

### Suppression and aftermath
Delhi fell in **September 1857**; the Emperor was tried and exiled to **Rangoon**. Jhansi's Rani died fighting at **Gwalior (June 1858)**; Tantia Tope was captured and hanged (1859). The **Government of India Act, 1858** ended Company rule — a **Secretary of State for India** took charge, the Governor-General became **Viceroy** (**Canning** first), and **Queen Victoria's Proclamation** (Allahabad, 1 November 1858) promised no more annexations and religious non-interference. The army was reconstituted along 'divide and rule' lines.

### Peasant and tribal uprisings
- **Paika rebellion, 1817** (Odisha) — **Bakshi Jagabandhu** against the British land system.
- **Kol uprising, 1831** (Chotanagpur) — tribal lands taken by outsiders.
- **Santhal Hul, 1855-56** — **Sidhu and Kanhu** Murmu against moneylenders and colonial revenue.
- **Munda Ulgulan, 1899-1900** — **Birsa Munda**; led to the Chotanagpur Tenancy Act (1908).
- **Faraizi movement** (Bengal, Dudu Mian); **Moplah uprisings** (Malabar, peaks in 1921).

### Quick revision
- Immediate cause: greased cartridges; spark: Barrackpore (Mangal Pandey, 34th NI); outbreak: Meerut, 10 May 1857.
- Centre-leader pairs: Kanpur-Nana Saheb, Lucknow-Hazrat Mahal, Jhansi-Lakshmibai, Arrah-Kunwar Singh, Bareilly-Khan Bahadur Khan, Faizabad-Ahmadullah Shah.
- Aftermath: Act of 1858 ends Company rule; Viceroy Canning; Queen's Proclamation, Allahabad, 1 Nov 1858.
- Uprisings: Paika 1817 (Jagabandhu), Santhal 1855 (Sidhu-Kanhu), Munda 1899 (Birsa)."""
    S.pattern("ga-re-p1", "1857 centres ↔ leaders matching", "very common",
        "'Who led the revolt at X', match-the-column of centres and leaders, 'Kunwar Singh fought at'.",
        None,
        "1. The table: Delhi-Bahadur Shah II, Kanpur-Nana Saheb, Lucknow-Hazrat Mahal, Jhansi-Lakshmibai, Arrah-Kunwar Singh, Faizabad-Ahmadullah Shah, Bareilly-Khan Bahadur Khan.\n2. Assistant leaders: Tantia Tope (Kanpur campaign), Bakht Khan (Delhi).\n3. Kunwar Singh is the aged Bihar hero — Jagdishpur/Arrah, not Gwalior.",
        "Who led the Revolt of 1857 at **Arrah (Bihar)**?",
        "**Kunwar Singh**, the 80-year-old zamindar of Jagdishpur.")
    S.pattern("ga-re-p2", "Causes: immediate trigger and deeper discontent", "very common",
        "'Immediate cause of 1857', greased cartridges, General Service Enlistment Act, annexation causes, 'which was NOT a cause'.",
        None,
        "1. **Immediate**: Enfield greased cartridges (cow-pig rumour) → Mangal Pandey, Barrackpore, 34th NI.\n2. Deeper: Lapse annexations, Awadh 1856, revenue burden, de-industrialisation, 1856 Enlistment Act, reform laws.\n3. In 'NOT a cause' questions, look for something post-1857 (e.g. Partition of Bengal) — that's the odd one.",
        "The **General Service Enlistment Act (1856)** worried sepoys because it —",
        "Required service **across the sea**, which many believed would cost them caste.")
    S.pattern("ga-re-p3", "Course, suppression and the 1858 Act", "common",
        "'Revolt began at Meerut on', Bahadur Shah's fate, Government of India Act 1858 provisions, Queen's Proclamation.",
        None,
        "1. Chain: Barrackpore (29 March) → Meerut (10 May 1857) → Delhi proclaimed; Delhi falls September 1857.\n2. **Bahadur Shah II** — tried and exiled to **Rangoon**; sons shot by Hodson.\n3. **Act of 1858**: Company ends, Secretary of State, **Viceroy = Canning**; Queen's Proclamation (Allahabad, 1 Nov 1858) promises no annexation, no religious interference.",
        "The **Government of India Act, 1858** did which of the following?",
        "Ended East India Company rule; India came under the Crown, with a Secretary of State and the Viceroy (Canning) at the head.")
    S.pattern("ga-re-p4", "Peasant and tribal uprisings ↔ leaders", "common",
        "'Santhal rebellion was led by', Birsa Munda's movement, Paika rebellion, Faraizi/Moplah facts.",
        None,
        "1. **Paika 1817 — Bakshi Jagabandhu** (Odisha); **Kol 1831** (Chotanagpur); **Santhal Hul 1855 — Sidhu & Kanhu**.\n2. **Munda Ulgulan 1899-1900 — Birsa Munda** (later honoured as 'Dharti Aba'); Chotanagpur Tenancy Act 1908 followed.\n3. Faraizi = Bengal (Dudu Mian); Moplah = Malabar (peaks 1921).",
        "The **Santhal rebellion (1855-56)**, called the Hul, was led by —",
        "**Sidhu and Kanhu** Murmu — against moneylenders and colonial revenue men.")

    S.q("ga-re-p1", "easy", "Who led the Revolt of 1857 at **Jhansi**?",
        ["Begum Hazrat Mahal", "Rani Lakshmibai", "Kunwar Singh", "Tantia Tope"], "Rani Lakshmibai",
        "**Rani Lakshmibai** fought for Jhansi (her adopted heir was refused under the Doctrine of Lapse) and died at Gwalior in June 1858.",
        "Jhansi-Lakshmibai, Lucknow-Hazrat Mahal.", 20)
    S.q("ga-re-p1", "medium", "**Kunwar Singh**, the aged leader of the 1857 revolt, was associated with —",
        ["Bareilly", "Arrah (Jagdishpur), Bihar", "Faizabad", "Gwalior"], "Arrah (Jagdishpur), Bihar",
        "**Kunwar Singh** of Jagdishpur, near Arrah in Bihar, fought the British through 1857-58.",
        "Arrah = Kunwar Singh.", 25)
    S.q("ga-re-p1", "hard", "Match:\n1. Bareilly — Khan Bahadur Khan\n2. Faizabad — Maulvi Ahmadullah Shah\n3. Gwalior — Bakht Khan\nWhich are correct?",
        ["1 and 2 only", "2 and 3 only", "1 and 3 only", "1, 2 and 3"], "1 and 2 only",
        "Bareilly-**Khan Bahadur Khan** and Faizabad-**Ahmadullah Shah** are right; **Bakht Khan** was the rebel general at **Delhi**, not Gwalior.",
        "Gwalior belongs to the Rani; Bakht Khan to Delhi.", 30)
    S.q("ga-re-p2", "easy", "The **immediate cause** of the Revolt of 1857 was —",
        ["Heavy land revenue", "Rumours about greased cartridges", "The Doctrine of Lapse", "Famine in Awadh"], "Rumours about greased cartridges",
        "The new **Enfield rifle cartridges**, rumoured greased with cow and pig fat, sparked the revolt — the deeper causes were political, economic and military.",
        "Immediate = cartridges; deeper = annexations + revenue.", 20)
    S.q("ga-re-p2", "medium", "**Mangal Pandey** belonged to which regiment?",
        ["3rd Light Cavalry", "34th Native Infantry", "19th Native Infantry", "5th Madras Regiment"], "34th Native Infantry",
        "Mangal Pandey of the **34th Native Infantry** attacked officers at **Barrackpore** on 29 March 1857; the regiment was disbanded.",
        "Barrackpore + 34th NI.", 25)
    S.q("ga-re-p2", "medium", "The annexation of **Awadh in 1856** was justified by the British on the ground of —",
        ["The Doctrine of Lapse", "Misgovernment (bad administration)", "A treaty obligation", "A plebiscite of talukdars"], "Misgovernment (bad administration)",
        "**Awadh** was annexed in **1856** on grounds of 'misgovernment' — not Lapse. The annexation alienated the talukdars and sepoys (many were from Awadh).",
        "Lapse for adopted heirs; Awadh = misgovernment.", 25)
    S.q("ga-re-p3", "easy", "The Revolt of 1857 **broke out in full** at Meerut on —",
        ["29 March 1857", "10 May 1857", "1 November 1857", "8 June 1858"], "10 May 1857",
        "On **10 May 1857** the Meerut sepoys mutinied and marched to Delhi, proclaiming Bahadur Shah II. (29 March = Barrackpore/Mangal Pandey.)",
        "Barrackpore 29 March, Meerut 10 May.", 20)
    S.q("ga-re-p3", "medium", "After the fall of Delhi (1857), **Bahadur Shah II** was —",
        ["Executed at Delhi", "Exiled to Rangoon", "Restored as Emperor", "Sent to the Andamans"], "Exiled to Rangoon",
        "The old emperor was tried at Delhi and **exiled to Rangoon**, where he died in 1862; his sons were shot by Captain Hodson.",
        "Rangoon, not execution.", 25)
    S.q("ga-re-p3", "hard", "Consider the statements:\n1. The Act of 1858 created the office of Secretary of State for India.\n2. Canning became the first Viceroy.\n3. The Queen's Proclamation was issued at Allahabad.\nWhich are correct?",
        ["1 and 2 only", "2 and 3 only", "1 and 3 only", "1, 2 and 3"], "1, 2 and 3",
        "All three are standard outcomes of 1858: the Secretary of State (with a 15-member Council), **Canning** as first Viceroy, and the **Proclamation at Allahabad** (1 November 1858).",
        "The 1858 package: SoS + Viceroy + Allahabad Proclamation.", 30)
    S.q("ga-re-p4", "medium", "The **Paika rebellion (1817)** of Odisha was led by —",
        ["Birsa Munda", "Bakshi Jagabandhu", "Sidhu Murmu", "Dudu Mian"], "Bakshi Jagabandhu",
        "**Bakshi Jagabandhu Bidyadhar**, the Paika (soldier-landholder) chief of Khurda, led the 1817 rebellion against British land and revenue changes.",
        "Paika = Jagabandhu (Odisha).", 25)
    S.q("ga-re-p4", "medium", "**Birsa Munda's** Ulgulan (1899-1900) was aimed at —",
        ["Driving out the British and outsiders from tribal land", "Abolishing sati", "Restoring Peshwa rule", "Ending the indigo contract system"], "Driving out the British and outsiders from tribal land",
        "The **Ulgulan** ('Great Tumult') of the Munda tribes demanded self-rule of tribal lands; its aftermath included the **Chotanagpur Tenancy Act (1908)**.",
        "Birsa = tribal self-rule; indigo = Champaran.", 25)
    S.q("ga-re-p4", "hard", "Which pair of uprising and leader is **incorrectly** matched?",
        ["Santhal Hul — Sidhu and Kanhu", "Kol uprising (1831) — Chotanagpur tribals", "Faraizi movement — Dudu Mian", "Moplah uprisings — Malabar's Paikas"], "Moplah uprisings — Malabar's Paikas",
        "The **Moplahs are Muslim peasants of Malabar**, not Paikas (the Paikas are Odisha's soldier-landholders of the 1817 rebellion). The other three pairs are correct.",
        "Paika = Odisha; Moplah = Malabar.", 30)
    return S


def build_reform():
    S = Sub("reform-movements")
    S.notes = """### Awakening the 19th century
**Raja Ram Mohan Roy** — the 'father of modern India' — began with the Atmiya Sabha (1814) and founded the **Brahmo Sabha/Samaj (1828)**, preaching monotheism and against idolatry. He campaigned against **sati** (abolished **1829** under Bentinck, with his persuasion), for widow remarriage, a free press and English education; his works include the *Gift to Monotheists*. **Debendranath Tagore** (Tattvabodhini Sabha) and **Keshab Chandra Sen** later led the Brahmo Samaj through its splits.
**Ishwar Chandra Vidyasagar** carried the widow-remarriage campaign to law — the **Hindu Widows' Remarriage Act, 1856** — and wrote the Bengali primer *Borno Porichoy*. **Prarthana Samaj (1867**, Atmaram Pandurang; **M.G. Ranade**, Bhandarkar) worked for theistic worship and social reform in Bombay. **Swami Dayanand Saraswati** founded the **Arya Samaj (1875)** — 'Back to the Vedas', **shuddhi** (reconversion), DAV education. **Swami Vivekananda** founded the **Ramakrishna Mission (1897)** (Chicago address 1893) on service. The **Theosophical Society** (1875, New York; **Blavatsky & Olcott**; Indian HQ **Adyar, 1882**) found its Indian voice in **Annie Besant**. **Sir Syed Ahmed Khan** began the Aligarh movement — **MAO College (1875)**, later Aligarh Muslim University — for modern education among Muslims. The **Deccan Education Society (1884**, Tilak-Agarkar, Fergusson College) and **Gokhale's Servants of India Society (1905)** trained public workers.

### Lower-caste and regional assertions
**Jyotirao and Savitribai Phule** — Satyashodhak Samaj (**1873**) and Pune's first girls' school (1848). **Sri Narayana Guru** (Kerala) — the Ezhava reformer who consecrated the Aruvippuram Shiva shrine (1888) and inspired the **SNDP Yogam (1903)** — 'one caste, one religion, one God for man'. **Periyar E.V. Ramaswamy** launched the **Self-Respect Movement (1925)** in Tamil country for caste and gender equality. **Sikh revival** — the Singh Sabha (1873, Amritsar). In Maharashtra, **Gopal Baba Walangkar** and later **Shahu Maharaj** pushed reserved seats and caste reform; B.R. Ambedkar's **Mahad Satyagraha (1927)** opened the struggle for untouchable rights.

### The legislation timeline
**1829** sati abolished (Regulation XVII) · **1856** widow remarriage legal · **1891** Age of Consent Act (raised to 12) · **1929** Child Marriage Restraint (**Sarda**) Act — marriage age 18 (boys) and 14 (girls).

### Quick revision
- Roy-Brahmo 1828-sati; Vidyasagar-Widow Remarriage Act 1856; Prarthana 1867-Ranade; Arya 1875-Dayanand.
- Ramakrishna Mission 1897-Vivekananda; Theosophy 1875 (Adyar) - Besant; Aligarh-MAO 1875-Sir Syed.
- Phule-Satyashodhak 1873; Narayana Guru-SNDP-Kerala; Periyar-Self-Respect 1925.
- Law years: sati 1829, remarriage 1856, consent 1891, Sarda 1929."""
    S.pattern("ga-rf-p1", "Organisation ↔ founder ↔ year", "very common",
        "'Who founded X Samaj/Sabha in year Y', match-the-column across Brahmo, Prarthana, Arya, Ramakrishna Mission.",
        None,
        "1. Chain: Atmiya Sabha 1814 → **Brahmo 1828 (Roy)** → **Prarthana 1867 (Atmaram Pandurang)** → **Arya 1875 (Dayanand)** → **Ramakrishna Mission 1897 (Vivekananda)**.\n2. Auxiliary bodies: Theosophical Society 1875 (Blavatsky-Olcott), Aligarh MAO College 1875 (Sir Syed), Satyashodhak 1873 (Phule).\n3. Don't swap Prarthana (Bombay, theistic) with Brahmo (Calcutta, monotheist).",
        "The **Prarthana Samaj** was founded in 1867 by —",
        "**Atmaram Pandurang** — with M.G. Ranade and R.G. Bhandarkar as its famous workers.")
    S.pattern("ga-rf-p2", "Reformer ↔ cause ↔ work", "very common",
        "'Who campaigned for widow remarriage', 'Kesari vs Borno Porichoy', education-for-all pioneers, shuddhi.",
        None,
        "1. **Vidyasagar** = widow remarriage campaign + *Borno Porichoy*; **Roy** = sati abolition; **Dayanand** = Back to the Vedas + shuddhi.\n2. **Phule** = girls' school (1848) + Satyashodhak; **Narayana Guru** = Ezhava upliftment; **Periyar** = Self-Respect.\n3. Vedic-revival vs Western-education lines: Arya Samaj (Vedic) vs Brahmo (rationalist universalism).",
        "Who organised the campaign that led to the **Hindu Widows' Remarriage Act, 1856**?",
        "**Ishwar Chandra Vidyasagar** — petitions, Sanskrit scholarly defence, and a public fund for remarried widows.")
    S.pattern("ga-rf-p3", "Reform legislation timeline", "common",
        "'Sati was abolished in', Age of Consent Act details, Sarda Act year and ages, order of the four laws.",
        None,
        "1. **1829 sati (Regulation XVII)** → **1856 widow remarriage** → **1891 Age of Consent (12)** → **1929 Sarda Act (18/14)**.\n2. All four are legislative landmarks — exams often ask 'which came first' or exact ages.\n3. Bentinck signed sati's abolition; the Sarda Act is pre-Independence's child-marriage law.",
        "The **Sarda Act (1929)** fixed the minimum marriage age at —",
        "**18 for boys and 14 for girls** (Child Marriage Restraint Act).")
    S.pattern("ga-rf-p4", "Regional and lower-caste movements", "common",
        "Sri Narayana Guru's Kerala work, Periyar's Self-Respect Movement, Singh Sabha, Mahad Satyagraha.",
        None,
        "1. **Narayana Guru** (Kerala, Ezhava): Aruvippuram 1888, SNDP Yogam 1903, 'one caste, one religion, one God'.\n2. **Periyar E.V. Ramaswamy**: Self-Respect Movement **1925** (Tamil Nadu).\n3. **Singh Sabha 1873** (Sikh revival); **Mahad Satyagraha 1927** (Ambedkar, water-tank rights).",
        "The **Self-Respect Movement (1925)** was launched by —",
        "**Periyar E.V. Ramaswamy** — for caste equality and women's dignity in Tamil society.")

    S.q("ga-rf-p1", "easy", "The **Brahmo Samaj** was founded in 1828 by —",
        ["Keshab Chandra Sen", "Raja Ram Mohan Roy", "Debendranath Tagore", "Ishwar Chandra Vidyasagar"], "Raja Ram Mohan Roy",
        "**Ram Mohan Roy** founded the Brahmo Sabha (later Samaj) in **1828** — preaching monotheism and against idol worship.",
        "Roy = Brahmo 1828.", 20)
    S.q("ga-rf-p1", "medium", "The **Ramakrishna Mission** was founded in 1897 by —",
        ["Ramakrishna Paramhansa", "Swami Vivekananda", "Annie Besant", "M.G. Ranade"], "Swami Vivekananda",
        "**Vivekananda** founded the Ramakrishna Mission (1897) in his guru Ramakrishna's name — its motto: service to man as service to God.",
        "Mission = Vivekananda; guru = Ramakrishna.", 25)
    S.q("ga-rf-p1", "hard", "The **Mohammedan Anglo-Oriental (MAO) College** of 1875, which became Aligarh Muslim University, was founded by —",
        ["Muhammad Iqbal", "Sir Syed Ahmed Khan", "Maulana Azad", "Rahmat Ali"], "Sir Syed Ahmed Khan",
        "**Sir Syed Ahmed Khan** founded MAO College (1875) — the heart of the Aligarh movement for modern education among Muslims.",
        "Aligarh = Sir Syed.", 30)
    S.q("ga-rf-p2", "easy", "Who opened one of the first **girls' schools** in Pune in 1848?",
        ["Jyotirao and Savitribai Phule", "Gopal Krishna Gokhale", "Ranade", "Bal Shastri Jambhekar"], "Jyotirao and Savitribai Phule",
        "**Savitribai Phule**, taught by and working with **Jyotirao Phule**, ran the pioneering girls' school at Bhide Wada, Pune (1848).",
        "1848 Pune girls' school = the Phules.", 20)
    S.q("ga-rf-p2", "medium", "The **Theosophical Society**'s international headquarters at **Adyar** (1882) is near which city?",
        ["Bombay", "Madras (Chennai)", "Calcutta", "Benares"], "Madras (Chennai)",
        "The Theosophical Society (founded 1875 in New York by **Blavatsky and Olcott**) moved its headquarters to **Adyar, Madras**, in 1882; Annie Besant led it later.",
        "Adyar = Theosophy = Madras.", 25)
    S.q("ga-rf-p2", "hard", "**Servants of India Society** (1905), which trained dedicated public workers, was founded by —",
        ["Gopal Krishna Gokhale", "Dadabhai Naoroji", "Pherozeshah Mehta", "W.C. Bonnerjee"], "Gopal Krishna Gokhale",
        "**Gokhale** founded the Servants of India Society in 1905 — he was also Gandhi's acknowledged political guru.",
        "Gokhale = Servants of India (1905).", 30)
    S.q("ga-rf-p3", "easy", "The **Hindu Widows' Remarriage Act** was passed in —",
        ["1829", "1856", "1891", "1929"], "1856",
        "The **Widows' Remarriage Act (1856)** legalised widow remarriage — Vidyasagar's campaign. Sati was banned in 1829.",
        "1829 sati, 1856 remarriage.", 20)
    S.q("ga-rf-p3", "medium", "Arrange the reform laws chronologically:\n1. Sarda Act  2. Sati abolition  3. Age of Consent Act  4. Widow Remarriage Act",
        ["2, 4, 3, 1", "4, 2, 3, 1", "2, 3, 4, 1", "4, 3, 2, 1"], "2, 4, 3, 1",
        "**Sati (1829) → Widow Remarriage (1856) → Age of Consent (1891) → Sarda Act (1929)**.",
        "Years 29-56-91-29 in that order.", 25)
    S.q("ga-rf-p3", "medium", "The **Age of Consent Act, 1891** raised the age of consent for girls to —",
        ["10 years", "12 years", "14 years", "16 years"], "12 years",
        "The **Age of Consent Act (1891)** raised it from 10 to **12** years — passed after the Rukhmabai and Phulmoni controversies.",
        "1891 = 12; Sarda Act = marriage ages 18/14.", 25)
    S.q("ga-rf-p4", "medium", "**Sri Narayana Guru**, who consecrated the Aruvippuram temple (1888), worked among the —",
        ["Nairs of Kerala", "Ezhavas of Kerala", "Reddys of Andhra", "Mahars of Maharashtra"], "Ezhavas of Kerala",
        "**Sri Narayana Guru** led the Ezhava reform movement in Kerala and inspired the **SNDP Yogam (1903)**.",
        "Narayana Guru = Ezhava = Kerala.", 25)
    S.q("ga-rf-p4", "medium", "Which reform movement's motto was **'one caste, one religion, one God for man'**?",
        ["Brahmo Samaj", "Arya Samaj", "The movement of Sri Narayana Guru", "Prarthana Samaj"], "The movement of Sri Narayana Guru",
        "**Sri Narayana Guru's** famous formulation summarised his anti-caste universalism in Kerala.",
        "The one-caste line = Narayana Guru.", 25)
    S.q("ga-rf-p4", "hard", "Consider the statements:\n1. Arya Samaj launched shuddhi (reconversion) ceremonies.\n2. The Singh Sabha (1873) worked for Sikh revival.\n3. The Mahad Satyagraha (1927) was led by Periyar.\nWhich are correct?",
        ["1 and 2 only", "2 and 3 only", "1 and 3 only", "1, 2 and 3"], "1 and 2 only",
        "Statements 1 and 2 are right. The **Mahad Satyagraha was led by B.R. Ambedkar**, not Periyar (whose movement is the Self-Respect Movement).",
        "Mahad = Ambedkar — the classic swap.", 30)
    return S
