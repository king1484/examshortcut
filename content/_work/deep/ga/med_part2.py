"""medieval-history deep content — part 2: marathas-sikhs, bhakti-sufi, sources-travellers."""
import os
import sys

sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
from _lib import Sub


def build_maratha():
    S = Sub("marathas-sikhs")
    S.notes = """### Shivaji builds a kingdom
**Shivaji** (born 1630 at **Shivneri**; father Shahaji, mother **Jijabai**) carved a state out of Bijapur's Deccan with hill forts and light cavalry: Torna, Rajgad, Sinhagad (where **Tanaji Malusare** fell — 'the fort is won, but the lion is lost'). He killed Bijapur general **Afzal Khan** at **Pratapgarh (1659)**, raided Surat, and humbled Shaista Khan at Pune. **Jai Singh's** pressure forced the **Treaty of Purandar (1665)** — ceding 23 of his forts — and the Agra visit-escape (1666). In **1674** he was crowned **Chhatrapati** at **Raigad** (rituals by Gaga Bhatt). His **Ashtapradhan** (eight ministers) ran the state: **Peshwa** (prime), Senapati, Amatya (finance), Sachiv, Mantri, Nyayadhish, Panditrao, Sumant (foreign affairs). Revenue used **kathi assessment**; the army was paid in cash, forts were the backbone.

### The Peshwas and the confederacy
Balaji Vishwanath (first Peshwa, 1713) won back Maratha rights from the weak Mughals; his son **Baji Rao I** (1720–40) carried Maratha arms to Malwa, Bundelkhand and Delhi's gates; **Balaji Baji Rao** saw the disaster at the **Third Battle of Panipat (1761)**, where **Ahmad Shah Abdali** crushed the Marathas. Power then lay with the confederacy houses: **Scindia (Gwalior), Holkar (Indore), Gaekwad (Baroda), Bhonsle (Nagpur)** under the Peshwa at Pune. The three **Anglo-Maratha wars** — the first ended by the **Treaty of Salbai (1782)**; the second began when **Baji Rao II** signed the **Treaty of Bassein (1802)** (subsidiary alliance); the third (1817–18) ended Maratha power.

### The ten Sikh Gurus
**Guru Nanak** (born 1469 at **Talwandi**, now Nankana Sahib) preached one God, **langar** (community kitchen) and honest work. **Angad** (the **Gurmukhi** script), **Amar Das**, **Ram Das** (founded Amritsar), **Arjan Dev** (compiled the **Adi Granth**; executed 1606 by Jahangir), **Hargobind** (Miri-Piri, the armed saint), **Har Rai**, **Har Krishan**, **Tegh Bahadur** (executed 1675 by Aurangzeb), and **Guru Gobind Singh** — who created the **Khalsa** at **Anandpur Sahib on Baisakhi 1699**, the five K's, and declared the **Granth** the Guru eternal. **Banda Bahadur** carried the Khalsa fight (executed 1716); the **misls** (confederacies) ended with **Maharaja Ranjit Singh** (Sukerchakia misl) taking **Lahore (1799)** and ruling Punjab till 1839.

### Quick revision
- Shivaji: Pratapgarh-Afzal Khan (1659), Purandar (1665, Jai Singh), Agra escape (1666), coronation 1674 (Raigad, Chhatrapati).
- Ashtapradhan: Peshwa first among eight; Sumant = foreign affairs.
- Peshwa ladder: Balaji Vishwanath → Baji Rao I → Balaji Baji Rao (Panipat 1761); Salbai 1782, Bassein 1802.
- Gurus: Nanak (Talwandi) → Arjan (Adi Granth, 1606) → Tegh Bahadur (1675) → Gobind (Khalsa 1699).
- After Gobind Singh: Banda Bahadur (1716), misls, Ranjit Singh (Lahore 1799)."""
    S.pattern("ga-mr-p1", "Shivaji: conquests, treaty, coronation, Ashtapradhan", "very common",
        "Pratapgarh-Afzal Khan, Purandar-Agra, 1674 Raigad coronation, Ashtapradhan ministers and their portfolios.",
        None,
        "1. Battle chain: **Pratapgarh 1659 (Afzal Khan) → Purandar 1665 (Jai Singh, 23 forts) → Agra escape 1666**.\n2. **1674, Raigad, Chhatrapati** — rituals by Gaga Bhatt.\n3. Ashtapradhan: **Peshwa** (prime), Senapati (army), Amatya (finance), Sumant (foreign), Nyayadhish (justice).",
        "Shivaji was crowned **Chhatrapati** in 1674 at —",
        "**Raigad** — after which he styled himself Chhatrapati Shivaji Maharaj.")
    S.pattern("ga-mr-p2", "Peshwas, confederacy houses and Anglo-Maratha wars", "very common",
        "'Who was the first Peshwa', Panipat 1761, confederacy house ↔ seat matching, Salbai-Bassein treaties.",
        None,
        "1. Peshwa ladder: **Balaji Vishwanath → Baji Rao I → Balaji Baji Rao** (Panipat 1761).\n2. Houses: **Scindia-Gwalior, Holkar-Indore, Gaekwad-Baroda, Bhonsle-Nagpur**, Peshwa-Pune.\n3. Wars: **Salbai 1782** (ends 1st), **Bassein 1802** (Baji Rao II accepts subsidiary alliance; begins 2nd), 3rd ends Maratha rule (1818).",
        "Which Maratha confederacy house was based at **Gwalior**?",
        "The **Scindias** (Holkar = Indore, Gaekwad = Baroda, Bhonsle = Nagpur).")
    S.pattern("ga-mr-p3", "Sikh Gurus in order and their landmarks", "very common",
        "'Who compiled the Adi Granth', birthplace of Guru Nanak, Miri-Piri, order-of-gurus questions.",
        None,
        "1. Landmark set: Nanak (Talwandi, langar), Angad (Gurmukhi), Ram Das (Amritsar), **Arjan Dev (Adi Granth, executed 1606)**, Hargobind (**Miri-Piri**).\n2. **Tegh Bahadur executed 1675**; **Gobind Singh — Khalsa, Baisakhi 1699, Anandpur Sahib**.\n3. Gobind Singh declared the **Granth** the eternal Guru.",
        "Who compiled the **Adi Granth**, the original Sikh scripture?",
        "**Guru Arjan Dev** (the 5th Guru) — executed at Lahore in 1606 under Jahangir.")
    S.pattern("ga-mr-p4", "After the tenth Guru: Khalsa continuity to Ranjit Singh", "common",
        "Banda Bahadur's fate, the misls, Ranjit Singh's rise and capital, five K's.",
        None,
        "1. **Banda Bahadur** led the Khalsa after 1708; executed at Delhi (1716).\n2. **Misls** = Khalsa confederacies; **Ranjit Singh** of the **Sukerchakia** misl took **Lahore (1799)** — 'Maharaja of Punjab'.\n3. Khalsa's **five K's**: kesh, kangha, kara, kachchha, kirpan.",
        "Maharaja Ranjit Singh belonged to which Sikh **misl**?",
        "The **Sukerchakia** misl — he captured Lahore in 1799 and built the Sikh empire.")

    S.q("ga-mr-p1", "easy", "Shivaji was formally crowned **Chhatrapati** in 1674 at —",
        ["Pratapgarh", "Purandar", "Raigad", "Sinhagad"], "Raigad",
        "The coronation (**1674**) took place at **Raigad** fort, with the scholar Gaga Bhatt officiating.",
        "Coronation = Raigad 1674.", 20)
    S.q("ga-mr-p1", "easy", "Which Bijapur general did Shivaji kill at **Pratapgarh (1659)**?",
        ["Afzal Khan", "Shaista Khan", "Jai Singh", "Rustam-e-Zaman"], "Afzal Khan",
        "**Afzal Khan** was killed in a tiger-claw encounter at Pratapgarh; Shaista Khan (Mughal) was Shivaji's Pune adversary.",
        "Pratapgarh = Afzal Khan.", 20)
    S.q("ga-mr-p1", "medium", "The **Treaty of Purandar (1665)**, by which Shivaji ceded 23 forts, followed the campaign of —",
        ["Shaista Khan", "Mirza Raja Jai Singh", "Diler Khan", "Aurangzeb personally"], "Mirza Raja Jai Singh",
        "Rajput general **Mirza Raja Jai Singh** (of Amber) besieged Purandar; the treaty led to Shivaji's Agra visit and famous escape (1666).",
        "Purandar-Agra both trace to Jai Singh.", 25)
    S.q("ga-mr-p1", "medium", "In Shivaji's **Ashtapradhan**, the **Peshwa** was —",
        ["The commander of cavalry", "The prime minister and first among the eight", "The chief justice", "The keeper of royal seals"], "The prime minister and first among the eight",
        "The **Peshwa** headed the eight ministers; **Senapati** led the army, **Amatya** finance, **Sumant/Dabir** foreign affairs, **Nyayadhish** justice.",
        "Peshwa = PM of the eight.", 25)
    S.q("ga-mr-p2", "easy", "The **first Peshwa** of the Marathas was —",
        ["Baji Rao I", "Balaji Vishwanath", "Balaji Baji Rao", "Nana Fadnavis"], "Balaji Vishwanath",
        "**Balaji Vishwanath** (Peshwa from 1713) founded the Peshwa line; Baji Rao I made it great; Balaji Baji Rao faced Panipat.",
        "First = Balaji Vishwanath.", 20)
    S.q("ga-mr-p2", "medium", "The **Treaty of Salbai (1782)** concluded —",
        ["The First Anglo-Maratha War", "The Second Anglo-Maratha War", "The Third Anglo-Maratha War", "The Third Battle of Panipat"], "The First Anglo-Maratha War",
        "**Salbai (1782)**, signed under Warren Hastings, ended the **First** Anglo-Maratha War (with Nana Fadnavis' Pune regime).",
        "Salbai = 1st; Bassein = 2nd.", 25)
    S.q("ga-mr-p2", "hard", "Match the confederacy house with its seat:\n1. Holkar — Indore  2. Gaekwad — Baroda  3. Bhonsle — Gwalior\nWhich are correct?",
        ["1 and 2 only", "2 and 3 only", "1 and 3 only", "1, 2 and 3"], "1 and 2 only",
        "**Holkar-Indore** and **Gaekwad-Baroda** are right; **Bhonsle ruled Nagpur**, while **Gwalior** belonged to the **Scindias**.",
        "Gwalior = Scindia — the classic trap.", 30)
    S.q("ga-mr-p3", "easy", "Guru Nanak was born in 1469 at —",
        ["Amritsar", "Anandpur Sahib", "Talwandi", "Kartarpur"], "Talwandi",
        "**Talwandi** (Rai Bhoe di Talwandi, now **Nankana Sahib** in Pakistan) is Guru Nanak's birthplace.",
        "Talwandi = Nankana Sahib.", 20)
    S.q("ga-mr-p3", "medium", "The policy of **Miri-Piri** (temporal and spiritual authority), symbolised by two swords, belongs to —",
        ["Guru Arjan Dev", "Guru Hargobind", "Guru Tegh Bahadur", "Guru Angad"], "Guru Hargobind",
        "**Guru Hargobind** (6th Guru) wore two swords — Miri (temporal power) and Piri (spiritual) — after his father Arjan's execution.",
        "Hargobind = the soldier-saint.", 25)
    S.q("ga-mr-p3", "medium", "The **Khalsa** was created by Guru Gobind Singh at —",
        ["Amritsar, 1675", "Anandpur Sahib, Baisakhi 1699", "Lahore, 1708", "Kartarpur, 1700"], "Anandpur Sahib, Baisakhi 1699",
        "On **Baisakhi of 1699** at **Anandpur Sahib**, Guru Gobind Singh founded the Khalsa with the Panj Pyare and the five K's.",
        "1699 + Baisakhi + Anandpur — all three go together.", 25)
    S.q("ga-mr-p4", "medium", "**Banda Bahadur**, who led the Khalsa after Guru Gobind Singh, was executed in 1716 by —",
        ["Aurangzeb", "Bahadur Shah I", "Farrukh Siyar", "Jahandar Shah"], "Farrukh Siyar",
        "**Farrukh Siyar** executed Banda Bahadur at Delhi in **1716** after his capture at Gurdas Nangal.",
        "Banda Bahadur's end = 1716, Farrukh Siyar.", 25)
    S.q("ga-mr-p4", "hard", "Consider the statements:\n1. Ranjit Singh captured Lahore in 1799.\n2. The Khalsa was formed before Banda Bahadur's leadership.\n3. Guru Gobind Singh named the Adi Granth as the eternal Guru.\nWhich are correct?",
        ["1 and 2 only", "2 and 3 only", "1 and 3 only", "1, 2 and 3"], "1, 2 and 3",
        "All three are standard: **Lahore 1799**, the **Khalsa (1699)** predating Banda Bahadur, and **1708**'s declaration of the Granth as Guru.",
        "Chain: Khalsa 1699 → Granth-Guru 1708 → Banda → misls → Ranjit.", 30)
    return S


def build_bhakti():
    S = Sub("bhakti-sufi")
    S.notes = """### Two roads to the same God
The **Bhakti** and **Sufi** movements of the medieval centuries answered ritual-heavy religion with love, devotion and the people's languages — and quietly attacked caste.

### Bhakti in the south first
The **Alvars** (devotees of **Vishnu**) and **Nayanars** (devotees of **Shiva**) sang between the 6th and 9th centuries; the **Tevaram** hymns belong to the Nayanars (Appar, Sambandar, Sundarar); **Andal** is the woman Alvar. Philosophically, **Shankaracharya** taught **Advaita** (non-dualism), **Ramanuja** **Vishishtadvaita** (qualified non-dualism), **Madhva** **Dvaita** (dualism), Vallabhacharya **Shuddhadvaita**.

### The north Indian wave
**Ramananda** (Varanasi) opened bhakti to all castes; his disciples included **Kabir** and Ravidas. **Kabir**, the weaver of Varanasi/Benares, mocked ritual on both sides and preached nirguna bhakti — his sayings live in the **Bijak**. **Guru Nanak** founded what became Sikhism (langar, honest labour, one God). **Tulsidas** gave Rama-bhakti in **Awadhi** (*Ramcharitmanas*); **Suras** sang Krishna in **Braj** (*Sursagar*); **Mirabai** sang for Krishna; **Tukaram's abhangas** (Marathi) belong to the **Varkari** sect worshipping **Vithoba at Pandharpur** (Namdev too); **Chaitanya** swept **Bengal-Odisha** with kirtans; Shankaradeva carried Vaishnavism to Assam.

### Sufism — Islamic mysticism
Sufi orders are **silsilas** ('chains' of master-to-disciple succession); the relationship is **pir-murid**; practice includes **zikr** (recitation) and **sama** (musical gatherings — the root of qawwali). The four main Indian silsilas:
- **Chishti** — the Indian chain began with **Khwaja Moinuddin Chishti** (Ajmer), through Qutbuddin Bakhtiyar Kaki, **Baba Farid**, **Nizamuddin Auliya** (Delhi) and Nasiruddin Chiragh; it avoided the court and served all communities.
- **Suhrawardi** — **Bahauddin Zakariya** (Multan), accepted state service.
- **Naqshbandi** — **Sheikh Ahmad Sirhindi** (revivalist).
- **Qadiri** — Sufism's oldest order, later Dara Shikoh's inclination.
Saints' tombs became **dargahs** — pilgrimage (ziyarat) centres.

### What they changed
Vernacular languages flowered (Bijak, Manas, abhangas), caste distinctions weakened at the level of devotional community, and bhakti-sufi shrines (Ajmer, Pandharpur, dargahs of Delhi) became shared spaces.

### Quick revision
- Alvars-Vishnu, Nayanars-Shiva; Tevaram = Nayanar hymns; Andal = woman Alvar.
- Advaita-Shankara, Vishishtadvaita-Ramanuja, Dvaita-Madhva.
- Kabir-Bijak; Tulsidas-Awadhi; Sur-Braj; Tukaram-Marathi abhangas (Varkari, Vithoba-Pandharpur); Chaitanya-Bengal.
- Silsilas: Chishti (Moinuddin → Nizamuddin), Suhrawardi (Bahauddin Zakariya), Naqshbandi (Sirhindi), Qadiri.
- Sama = music; pir-murid; dargah = tomb-shrine."""
    S.pattern("ga-bs-p1", "Alvars, Nayanars and the Acharyas", "common",
        "'Alvars were devotees of', Nayanar hymn collections, Advaita-Vishishtadvaita-Dvaita founders.",
        None,
        "1. **Alvars = Vishnu**, **Nayanars = Shiva**; Tevaram = Nayanar hymns (Appar, Sambandar, Sundarar); Andal = woman Alvar.\n2. Schools: **Advaita-Shankaracharya, Vishishtadvaita-Ramanuja, Dvaita-Madhva**, Shuddhadvaita-Vallabhacharya.\n3. Ramanuja's school influenced South Indian Vaishnavism directly.",
        "The **Alvars** of south India were devotees of —",
        "**Vishnu** — the Nayanars were the Shiva-devotee counterparts.")
    S.pattern("ga-bs-p2", "North Indian Bhakti saints ↔ sect, language, work", "very common",
        "Kabir-Bijak, Tulsidas-Awadhi, Tukaram-Marathi, Chaitanya-Bengal, Varkari-Vithoba, nirguna vs saguna.",
        None,
        "1. Language anchors: **Tulsidas-Awadhi, Sur-Braj, Tukaram & Namdev-Marathi, Chaitanya-Bengal, Kabir-sadhan mix**.\n2. Works: Kabir-**Bijak**; Tulsidas-**Ramcharitmanas**; Sur-**Sursagar**.\n3. Sects: **Varkari = Vithoba of Pandharpur**; nirguna (Kabir, Nanak) vs saguna (Tulsidas, Sur, Mira).",
        "Tukaram's **abhangas** are composed in which language?",
        "**Marathi** — he belongs to the Varkari sect of Pandharpur.")
    S.pattern("ga-bs-p3", "Sufi silsilas ↔ founders and saints", "very common",
        "'Which silsila did X belong to', Ajmer dargah, Multan saint, meaning of silsila and sama.",
        None,
        "1. **Chishti**: Moinuddin (Ajmer) → Qutbuddin Bakhtiyar Kaki → **Baba Farid** → **Nizamuddin Auliya** → Nasiruddin Chiragh.\n2. **Suhrawardi-Bahauddin Zakariya (Multan)**; **Naqshbandi-Ahmad Sirhindi**; **Qadiri** = oldest.\n3. Terms: **silsila = chain/order**, pir-murid, **sama = musical recital**, dargah = tomb-shrine.",
        "The Suhrawardi silsila in India is associated with which saint?",
        "**Bahauddin Zakariya** of Multan — unlike the Chishtis, his order accepted state service.")
    S.pattern("ga-bs-p4", "Shared features of Bhakti and Sufi movements", "common",
        "Statement questions: caste criticism, vernacular use, guru-disciple bond, devotional equality — which statements are true.",
        None,
        "1. Common ground: devotion above ritual, **use of people's languages**, criticism of caste, the **guru's** centrality, devotional equality.\n2. Neither movement was 'anti-temple' as a whole — judge each statement, not the cliché.\n3. Shared spaces: dargahs and temple towns; qawwali grew from sama.",
        "Which was a common feature of both the Bhakti and Sufi movements?",
        "Use of **vernacular languages** and a devotional path open to all castes and communities.")

    S.q("ga-bs-p1", "medium", "The **Vishishtadvaita** (qualified non-dualism) philosophy was taught by —",
        ["Shankaracharya", "Ramanuja", "Madhvacharya", "Vallabhacharya"], "Ramanuja",
        "**Ramanuja** taught Vishishtadvaita; Shankara = Advaita; Madhva = Dvaita; Vallabha = Shuddhadvaita.",
        "Vishishta = qualified = Ramanuja.", 25)
    S.q("ga-bs-p1", "medium", "The **Tevaram** hymns are associated with —",
        ["Alvar saints", "Nayanar saints", "Sufi saints", "Sikh Gurus"], "Nayanar saints",
        "The **Tevaram** is the Nayanars' Shiva-bhakti hymn collection (Appar, Sambandar, Sundarar).",
        "Tevaram = Nayanar (Shiva).", 25)
    S.q("ga-bs-p2", "easy", "The sayings of **Kabir** are collected in the —",
        ["Bijak", "Sursagar", "Ramaini of Tulsidas", "Gathasaptasati"], "Bijak",
        "Kabir's verses live in the **Bijak** (kept by his followers) and in Sikh and Dadu panth collections.",
        "Bijak = Kabir.", 20)
    S.q("ga-bs-p2", "easy", "**Chaitanya Mahaprabhu**, the Krishna-bhakti saint, belonged to —",
        ["Maharashtra", "Gujarat", "Bengal", "Punjab"], "Bengal",
        "**Chaitanya** of Navadwip (Bengal) spread Krishna-bhakti through **kirtan** across Bengal and Odisha.",
        "Chaitanya = Bengal's kirtan saint.", 20)
    S.q("ga-bs-p2", "medium", "The **Varkari** sect, with its pilgrim movement to Pandharpur, worships —",
        ["Vithoba", "Venkateshwara", "Jagannath", "Khandoba"], "Vithoba",
        "The **Varkari** pilgrims (Namdev, Tukaram, Janabai) worship **Vithoba (Vitthal)** at **Pandharpur** on the Chandrabhaga.",
        "Varkari = Pandharpur = Vithoba.", 25)
    S.q("ga-bs-p3", "easy", "The dargah of **Khwaja Moinuddin Chishti** is at —",
        ["Delhi", "Ajmer", "Multan", "Pakpattan"], "Ajmer",
        "**Moinuddin Chishti** settled at **Ajmer**; his dargah ('Gharib Nawaz') is India's most visited Sufi shrine.",
        "Moinuddin = Ajmer.", 20)
    S.q("ga-bs-p3", "medium", "In Sufi practice, the musical recital of devotion is called —",
        ["Zikr", "Sama", "Silsila", "Riwayat"], "Sama",
        "**Sama** is the musical recital (root of qawwali); **zikr** is silent/chanted remembrance; **silsila** is the order's chain.",
        "Sama = song; zikr = chant.", 25)
    S.q("ga-bs-p3", "hard", "Match the silsila with its Indian anchor:\n1. Naqshbandi — Ahmad Sirhindi\n2. Chishti — Nizamuddin Auliya\n3. Suhrawardi — Baba Farid\nWhich are correct?",
        ["1 and 2 only", "2 and 3 only", "1 and 3 only", "1, 2 and 3"], "1 and 2 only",
        "**Sirhindi** anchors the Naqshbandi and **Nizamuddin** the Chishti order in Delhi; **Baba Farid** was Chishti (Pakpattan), while the **Suhrawardi** anchor is **Bahauddin Zakariya** (Multan).",
        "Farid = Chishti, Zakariya = Suhrawardi — don't swap.", 30)
    S.q("ga-bs-p4", "easy", "Both Bhakti and Sufi saints chiefly communicated in —",
        ["Sanskrit and Arabic", "The languages of the common people", "Persian only", "Pali"], "The languages of the common people",
        "Both movements deliberately used **vernaculars** — Awadhi, Braj, Marathi, Punjabi, Bengali, and Persian-Hindavi — to reach ordinary people.",
        "Vernacular reach is their shared signature.", 20)
    S.q("ga-bs-p4", "medium", "The relation between a Sufi master and his disciple is termed —",
        ["Guru-shishya", "Pir-murid", "Ustad-shagird", "Acharya-shishya"], "Pir-murid",
        "In Sufism the master is the **pir** (sheikh) and the disciple the **murid**; initiation into the order creates the silsila link.",
        "Pir-murid is the Sufi pair.", 25)
    return S


def build_sources():
    S = Sub("sources-travellers")
    S.notes = """### Chronicles of the court
- **Sultanate histories:** **Ziauddin Barani** — *Tarikh-i-Firoz Shahi* (and *Fatawa-i-Jahandari*, advice to kings); **Amir Khusrau** — the 'Parrot of India' (Persian poet, *Khamsa*, *Tughlaq Nama*); Isami's *Futuh-us-Salatin*.
- **Mughal memoirs and histories:** **Babur** — *Baburnama* in Turkish; **Gulbadan Begum** — *Humayun-nama*; **Abul Fazl** — *Akbarnama* (three volumes, the third being the **Ain-i-Akbari**, the administration gazetteer); **Jahangir** — his own *Tuzuk-i-Jahangiri*; **Abdul Hamid Lahori** — *Badshahnama (Padshahnama)* on Shah Jahan.
These histories are court-centred: they praise patrons, so their numbers and claims need cross-checking with coins, inscriptions, architecture and the independent view of foreign travellers. Barani, for instance, writes as an orthodox critic of MBT's policies — useful, but angled.

### The travellers' ladder
| Traveller | From | Visited | Note |
|---|---|---|---|
| **Marco Polo** | Venice | Pandya coast (1290s) | 'Pearl fishery' accounts |
| **Ibn Battuta** | Morocco | MBT's Delhi (as qazi) | Book: *Rihla* |
| **Nicolo Conti** | Venice | Vijayanagara (Deva Raya I) | — |
| **Abdur Razzaq** | Persia (Timurid) | Vijayanagara (Deva Raya II) | Hampi's splendour |
| **Athanasius Nikitin** | Russia | Bahmani kingdom | *Voyage to India* |
| **Domingo Paes / Duarte Barbosa** | Portugal | Krishnadevaraya's court | Bazaars of Hampi |
| **Ralph Fitch** | England | Akbar's reign (1583) | First English merchant |
| **William Hawkins / Thomas Roe** | England | Jahangir's court | Roe = James I's ambassador (1615) |
| **Tavernier, Bernier, Manucci** | France/Italy | Mughal India (17th c.) | Diamond trade; Peacock Throne |

### Vernacular classics of the age
**Malik Muhammad Jayasi's Padmavat** (Awadhi Sufi romance), Sur's Braj poetry, Tulsidas' Awadhi *Manas*, Tukaram's Marathi abhangas, and Krishnadevaraya's Telugu **Amuktamalyada** — the medieval literary map is multilingual, and each classic doubles as a social source: the *Padmavat* for Sufi storytelling, the *Ain* for prices and regulations, *Rihla* for daily Delhi under MBT.

### What each source is best for
- **Administration:** the **Ain-i-Akbari** (mansabs, provinces, prices) and Sher Shah's revenue papers referenced by later writers.
- **Daily life and courts:** **Ibn Battuta's Rihla**, Paes' Hampi bazaars, Bernier's Delhi and the Peacock Throne.
- **Trade:** Tavernier on diamonds, Marco Polo on the pearl fishery, Nikitin on Bahmani markets.
- **Court politics:** Barani for the Tughlaqs, Badauni's *Muntakhab-ut-Tawarikh* (an orthodox critic of Akbar) against Abul Fazl's praise — read both ends.

### Quick revision
- Barani-*Tarikh-i-Firoz Shahi*; Abul Fazl-*Akbarnama* (Ain = vol. 3); Lahori-*Badshahnama*; Babur-Turkish memoir.
- Travellers: Marco Polo-Pandya; Ibn Battuta-MBT (*Rihla*); Conti & Paes-Vijayanagara; Razzaq-Deva Raya II; Nikitin-Bahmani; Fitch-Akbar; Roe-Jahangir.
- Jayasi-*Padmavat* (Awadhi); Khusrau wrote chiefly in Persian.
- Court histories are partisan — the exam often asks 'who visited whom', so memorise the ladder."""
    S.pattern("ga-st-p1", "Chronicle ↔ author (Sultanate and Mughal)", "very common",
        "'Tarikh-i-Firoz Shahi was written by', who wrote Badshahnama, Ain-i-Akbari as part of Akbarnama.",
        None,
        "1. Sultanate: **Barani-Tarikh-i-Firoz Shahi (+ Fatawa-i-Jahandari)**; Khusrau-Persian poet (*Tughlaq Nama*).\n2. Mughal: Babur-*Baburnama* (Turkish); Abul Fazl-*Akbarnama* (Ain = vol. 3); Lahori-*Badshahnama*; Gulbadan-*Humayun-nama*.\n3. Match emperor to historian before answering match-the-column.",
        "The *Tarikh-i-Firoz Shahi*, a history of the Tughlaq age, was written by —",
        "**Ziauddin Barani**, who also wrote the political guide *Fatawa-i-Jahandari*.")
    S.pattern("ga-st-p2", "Foreign travellers ↔ the courts they visited", "very common",
        "'Ibn Battuta came from', 'Abdur Razzaq visited whose court', Marco Polo in the Pandya kingdom, Roe-Jahangir.",
        None,
        "1. The ladder: Marco Polo-Pandya; **Ibn Battuta-MBT (Rihla)**; Conti-Vijayanagara (Deva Raya I); **Razzaq-Deva Raya II**; Nikitin-Bahmani; Paes-Krishnadevaraya; **Fitch-Akbar; Roe-Jahangir**.\n2. Ibn Battuta = **Morocco**, served as Delhi's **qazi**.\n3. Roe's embassy (1615) opened English trade — a recurring 'why' question.",
        "Who visited the court of **Deva Raya II** of Vijayanagara as an envoy of Persia?",
        "**Abdur Razzaq** — his account praises Hampi's wealth.")
    S.pattern("ga-st-p3", "Regional and vernacular classics of the medieval age", "common",
        "Padmavat-Jayasi, Khusrau's language, Amuktamalyada, Humayun-nama by Gulbadan Begum.",
        None,
        "1. **Jayasi's Padmavat** — Awadhi Sufi romance; Khusrau wrote chiefly **Persian**.\n2. **Gulbadan Begum** (Humayun's sister) wrote the *Humayun-nama* — a rare woman chronicler.\n3. Krishnadevaraya's *Amuktamalyada* = Telugu court classic.",
        "***Padmavat*, the Awadhi Sufi romance of Alauddin and Padmini, was written by —",
        "**Malik Muhammad Jayasi** (1540).")
    S.pattern("ga-st-p4", "Mughal court literature and autobiographies", "very common",
        "'Tuzuk-i-Jahangiri is an autobiography of', Baburnama language, Ain-i-Akbari's place in Akbarnama, Badshahnama author.",
        None,
        "1. Two royal autobiographies: **Babur (Baburnama, Turkish)** and **Jahangir (Tuzuk-i-Jahangiri)**.\n2. **Ain-i-Akbari = third volume of Akbarnama** (Abul Fazl) — administration, provinces, foods, regulations.\n3. **Abdul Hamid Lahori** chronicled Shah Jahan (*Badshahnama*).",
        "The **Ain-i-Akbari** is which part of Abul Fazl's Akbarnama?",
        "The **third volume** — the administrative gazetteer of Akbar's empire.")

    S.q("ga-st-p1", "easy", "The **Baburnama**, the first Mughal memoir, was written by Babur himself in —",
        ["Persian", "Turkish", "Arabic", "Hindavi"], "Turkish",
        "Babur wrote in **Chagatai Turkish**; it was later rendered into Persian for the court.",
        "Babur's memoirs = Turkish.", 20)
    S.q("ga-st-p1", "medium", "***Badshahnama* (Padshahnama)**, the official history of Shah Jahan's reign, was written by —",
        ["Abul Fazl", "Abdul Hamid Lahori", "Ziauddin Barani", "Inayat Khan"], "Abdul Hamid Lahori",
        "**Abdul Hamid Lahori** compiled the *Badshahnama*; Abul Fazl wrote for Akbar and Barani for the Tughlaq age.",
        "Shah Jahan-Lahori.", 25)
    S.q("ga-st-p1", "hard", "Consider the statements:\n1. Barani wrote both a history and a mirror-for-princes.\n2. Amir Khusrau is credited with the Tughlaq Nama.\n3. Isami's Futuh-us-Salatin deals with the Bahmani court.\nWhich are correct?",
        ["1 and 2 only", "2 and 3 only", "1 and 3 only", "1, 2 and 3"], "1 and 2 only",
        "Barani wrote the *Tarikh-i-Firoz Shahi* and *Fatawa-i-Jahandari*; Khusrau wrote the *Tughlaq Nama*. **Isami's *Futuh-us-Salatin* is a Sultanate-Deccan verse history (Delhi Sultans), not a Bahmani court chronicle.**",
        "Statement 3 swaps the court — check each work's subject.", 30)
    S.q("ga-st-p2", "easy", "The Venetian traveller **Marco Polo** visited —",
        ["The Bahmani kingdom", "The Pandya kingdom's coast", "Akbar's court", "Harsha's Kanauj"], "The Pandya kingdom's coast",
        "**Marco Polo** (1290s) travelled along the Coromandel coast, describing the Pandya pearl fishery.",
        "Marco Polo = the pearl coast.", 20)
    S.q("ga-st-p2", "medium", "The Russian traveller **Athanasius Nikitin** visited —",
        ["Vijayanagara under Krishnadevaraya", "The Bahmani kingdom", "MBT's Delhi", "Bengal under the Senas"], "The Bahmani kingdom",
        "**Nikitin** (*Voyage to India*, 15th century) travelled in the **Bahmani** kingdom; his account is a Russian classic.",
        "Nikitin = Bahmani.", 25)
    S.q("ga-st-p2", "medium", "The English merchant **Ralph Fitch** travelled in India during the reign of —",
        ["Babur", "Akbar", "Jahangir", "Shah Jahan"], "Akbar",
        "**Ralph Fitch** (1583–91) was the first English merchant-traveller to describe Mughal India — he came in **Akbar's** reign, decades before Roe.",
        "Fitch before the Company: Akbar's time.", 25)
    S.q("ga-st-p3", "easy", "**Amir Khusrau**, the 'Parrot of India', wrote his poetry mainly in —",
        ["Turkish", "Persian", "Arabic", "Braj"], "Persian",
        "**Amir Khusrau** was the great **Persian** poet of the Sultanate (he also played with Hindavi in couplets); he served several sultans and sat at Nizamuddin Auliya's feet.",
        "Khusrau = Persian court poetry.", 20)
    S.q("ga-st-p3", "medium", "The **Humayun-nama** was written by —",
        ["Abul Fazl", "Gulbadan Begum", "Badauni", "Jauhar"], "Gulbadan Begum",
"**Gulbadan Banu Begum**, Humayun's sister, wrote the *Humayun-nama* — a rare woman's inside view of the Mughal household.",
        "Humayun's sister = the chronicler.", 25)
    S.q("ga-st-p4", "easy", "***Tuzuk-i-Jahangiri*** is —",
        ["A biography of Jahangir by Abul Fazl", "Jahangir's own autobiography", "A history by Badauni", "A travelogue by Tavernier"], "Jahangir's own autobiography",
        "**Jahangir** wrote his memoirs himself (*Tuzuk-i-Jahangiri/Jahangirnama*) — as Babur had before him.",
        "Two Mughal autobiographies: Babur, Jahangir.", 20)
    S.q("ga-st-p4", "hard", "Consider the statements:\n1. The Ain-i-Akbari records provincial administration and regulations.\n2. Abul Fazl completed the Akbarnama in three volumes.\n3. Badauni's Muntakhab-ut-Tawarikh is hostile to Akbar's religious policies.\nWhich are correct?",
        ["1 and 2 only", "2 and 3 only", "1 and 3 only", "1, 2 and 3"], "1, 2 and 3",
        "All three are standard: the **Ain** details administration, the **Akbarnama** ran to three volumes, and **Badauni** (an orthodox critic) wrote the *Muntakhab-ut-Tawarikh*.",
        "Friendly (Abul Fazl) vs hostile (Badauni) lenses on the same reign.", 30)
    return S
