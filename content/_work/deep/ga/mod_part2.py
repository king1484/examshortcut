"""modern-history deep content — part 2: early-nationalism, gandhian-era, press-books."""
import os
import sys

sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
from _lib import Sub


def build_early():
    S = Sub("early-nationalism")
    S.notes = """### The Congress is born (1885)
A retired ICS officer, **A.O. Hume**, brought 72 Indian delegates together at **Bombay** (Gokuldas Tejpal Sanskrit College) in **December 1885** — the first session of the **Indian National Congress**. Its first president was **W.C. Bonnerjee**. The "safety-valve" reading — that Hume wanted a yearly talking-shop to let out discontent — was argued by **Lala Lajpat Rai** in his book *Young India*; modern historians see it as the first all-India political platform.

### The Moderates (1885–1905)
Leaders: **Dadabhai Naoroji** (thrice president; first Indian MP in the British House of Commons, 1892; the 'Grand Old Man of India'), **S.N. Banerjea** (Indian Association, 1876; paper *Bengalee*), **Gokhale** (Servants of India Society, 1905; Gandhi's political guru), **Pherozeshah Mehta** ('Lion of Bombay'), **R.C. Dutt** (*Economic History of India*). Methods: petitions, prayers and protests — the '3P' path — trusting British justice. Their lasting contribution was **economic criticism**: Naoroji's **Drain of Wealth** theory (*Poverty and Un-British Rule in India*, 1901) showed how India's money flowed out as salaries, pensions and profits.

### Extremists (1905–1919)
**Lal-Bal-Pal** — **Lala Lajpat Rai** (Punjab Kesari), **Bal Gangadhar Tilak**, **Bipin Chandra Pal** — plus **Aurobindo Ghosh**. Tilak ran **Kesari** (Marathi) and *Mahratta* (English), started the **Ganapati (1893)** and **Shivaji (1895)** festivals, and declared **"Swaraj is my birthright and I shall have it."** Jailed for six years (1908–14) in **Mandalay**, where he wrote *Geeta Rahasya*. They wanted self-rule, not petitions, and believed in mass action, swadeshi and national education.

### Partition of Bengal (1905) and Swadeshi
**Lord Curzon** partitioned Bengal (effective **16 October 1905**) on the plea of administrative convenience — really to break Bengali nationalism: a Muslim-majority **East Bengal and Assam**, a Hindu-majority west. The answer was the **Swadeshi movement**: boycott of foreign cloth and salt, **Rakhi bandhan** (Tagore's idea), *Amar Sonar Bangla* as the marching song, national schools (the **National Council of Education, 1906**) and volunteer samitis. The partition was **annulled in 1911**.

### Split, League, reforms, reunion
- **Surat, 1907**: the session split — Moderates (Rash Behari Ghosh) vs Extremists (Tilak). The two wings **reunited at Lucknow in 1916**.
- **Muslim League, 1906**: founded at **Dacca** (Nawab Salimullah's initiative); it backed the partition and soon demanded **separate electorates**.
- **Calcutta session, 1906** (Naoroji president): the word **Swaraj** entered the Congress resolution.
- **Morley-Minto reforms, 1909**: first Indians in the executive councils (Satyendra P. Sinha), but also **separate electorates** for Muslims — Minto is called the father of communal electorates.
- **Home Rule Leagues, 1916**: Tilak's (April, Maharashtra-Karnataka-CP-Berar) and **Annie Besant's** (September, Madras; papers *New India* and *Commonweal*); Besant became Congress president in 1917.

### Quick revision
- INC 1885, Bombay, Hume; first president W.C. Bonnerjee; 72 delegates.
- Moderates: Naoroji (drain theory), Gokhale, S.N. Banerjea, Mehta, R.C. Dutt.
- Tilak: Kesari + Mahratta, Ganapati 1893, Mandalay 1908–14, Home Rule 1916.
- Curzon's partition 1905 → Swadeshi → annulled 1911; Surat split 1907, Lucknow reunion 1916.
- League 1906 Dacca; Morley-Minto 1909 = separate electorates."""
    S.pattern("ga-en-p1", "Founding of the Congress", "very common",
        "'The first session of the INC was held at…', who founded it, first president, number of delegates.",
        None,
        "1. **December 1885, Bombay** (Gokuldas Tejpal Sanskrit College).\n2. Founder-organiser: **A.O. Hume**; first president: **W.C. Bonnerjee**; 72 delegates.\n3. Watch the trap: Hume was an Englishman, but the president was Indian.",
        "The first session of the Indian National Congress (1885) was presided over by —",
        "**W.C. Bonnerjee** — with A.O. Hume as founder-organiser, at Bombay.")
    S.pattern("ga-en-p2", "Moderate leaders ↔ work or epithet", "very common",
        "'Drain of Wealth theory was given by', 'Grand Old Man of India', Gandhi's political guru, first Indian MP in Britain.",
        None,
        "1. **Naoroji** = drain theory, *Poverty and Un-British Rule in India*, first Indian MP (1892), thrice Congress president.\n2. **Gokhale** = Servants of India Society (1905), Gandhi's political guru.\n3. **S.N. Banerjea** = Indian Association 1876, *Bengalee*; **R.C. Dutt** = *Economic History of India*.",
        "The **Drain of Wealth** theory was systematically expounded by —",
        "**Dadabhai Naoroji**, in *Poverty and Un-British Rule in India* (1901).")
    S.pattern("ga-en-p3", "Extremists ↔ slogan, paper, festival", "very common",
        "'Swaraj is my birthright' — who said it, Kesari's editor, Ganapati/Shivaji festivals, Lal-Bal-Pal identification.",
        None,
        "1. **Tilak**: *Kesari* + *Mahratta*; Ganapati 1893, Shivaji 1895; 'Swaraj is my birthright…'; Mandalay 1908–14; *Geeta Rahasya*.\n2. **Lajpat Rai** = 'Punjab Kesari'; **Pal** = Bengal; **Aurobindo** = *Bande Mataram*.\n3. Don't mix Lajpat Rai's *Young India* (book, 1916) with Gandhi's *Young India* (journal, 1919).",
        "The slogan **'Swaraj is my birthright and I shall have it'** is associated with —",
        "**Bal Gangadhar Tilak** — editor of *Kesari* and *Mahratta*.")
    S.pattern("ga-en-p4", "Partition of Bengal ↔ Swadeshi response", "very common",
        "'Partition of Bengal 1905 was annulled in…', which Viceroy, what were the two provinces, Swadeshi facts.",
        None,
        "1. **Curzon**, effective **16 October 1905**: East Bengal & Assam (Muslim-majority) + west Bengal (Hindu-majority).\n2. Response: Swadeshi-boycott, Rakhi, national education (**NCE 1906**), samitis.\n3. **Annulled 1911**; the capital also moved from Calcutta to Delhi that year.",
        "The partition of Bengal (1905) was **annulled** in —",
        "**1911** — under Lord Hardinge, at the Delhi Durbar.")
    S.pattern("ga-en-p5", "Surat split, Muslim League, Lucknow reunion", "common",
        "'The Congress split at Surat in…', League's founding year and place, the Congress-League pact.",
        None,
        "1. **Surat 1907** = Moderates vs Extremists; **Lucknow 1916** = reunion + Congress-League pact.\n2. **Muslim League 1906, Dacca** (Nawab Salimullah); soon demanded separate electorates.\n3. The 1916 Lucknow Congress accepted separate electorates — remember it as the year of compromise.",
        "The All India **Muslim League** was founded in 1906 at —",
        "**Dacca**, on the initiative of **Nawab Salimullah**.")
    S.pattern("ga-en-p6", "Morley-Minto 1909 and Home Rule Leagues", "common",
        "'Separate electorates were introduced by which reform', Home Rule Leagues of 1916 — who started what and where.",
        None,
        "1. **Morley-Minto 1909** = separate electorates for Muslims (Minto: 'father of communal electorates'); S.P. Sinha in the Viceroy's council.\n2. **Home Rule 1916**: Tilak (April; Maharashtra, Karnataka, CP, Berar) and **Annie Besant** (September; Madras, rest of India).\n3. Besant's papers: *New India*, *Commonweal*; she became Congress president (1917).",
        "The **separate electorates** for Muslims were first introduced by —",
        "The **Morley-Minto reforms (Indian Councils Act, 1909)**.")

    S.q("ga-en-p1", "easy", "The **Indian National Congress** was founded in 1885 by —",
        ["Lord Dufferin", "A.O. Hume", "W.C. Bonnerjee", "Dadabhai Naoroji"], "A.O. Hume",
        "**Alan Octavian Hume**, a retired ICS officer, organised the first session at Bombay in December 1885; **W.C. Bonnerjee** presided.",
        "Hume founded, Bonnerjee presided.", 20)
    S.q("ga-en-p1", "medium", "How many delegates attended the **first session** of the Indian National Congress?",
        ["72", "100", "54", "85"], "72",
        "The Bombay session of **December 1885** had **72 delegates**, drawn mostly from professional classes of the presidencies.",
        "First session = 72 delegates.", 25)
    S.q("ga-en-p2", "easy", "Who is known as the **'Grand Old Man of India'**?",
        ["Dadabhai Naoroji", "S.N. Banerjea", "Gopal Krishna Gokhale", "R.C. Dutt"], "Dadabhai Naoroji",
        "**Naoroji** — thrice Congress president, first Indian MP in the British House of Commons (1892), author of the drain theory.",
        "Grand Old Man = Naoroji.", 20)
    S.q("ga-en-p2", "hard", "Consider the statements about Moderate leaders:\n1. Gokhale founded the Servants of India Society in 1905.\n2. S.N. Banerjea founded the Indian Association in 1876.\n3. R.C. Dutt wrote *Poverty and Un-British Rule in India*.\nWhich are correct?",
        ["1 and 2 only", "2 and 3 only", "1 and 3 only", "1, 2 and 3"], "1 and 2 only",
        "*Poverty and Un-British Rule in India* is **Naoroji's** book; **R.C. Dutt** wrote the *Economic History of India*.",
        "Swap the two economic books — that's the trap.", 30)
    S.q("ga-en-p3", "easy", "Tilak started the public **Ganapati festival** in 1893 primarily to —",
        ["Build a mass base against British rule", "Celebrate the Maratha dynasty", "Promote Sanskrit learning", "Oppose the Partition of Bengal"], "Build a mass base against British rule",
        "The **Ganapati (1893)** and **Shivaji (1895)** festivals gave Tilak a legal platform to gather and mobilise the masses.",
        "Festivals = political mobilisation under a religious cover.", 25)
    S.q("ga-en-p3", "medium", "Tilak was sentenced to six years' imprisonment in 1908 and imprisoned at —",
        ["Mandalay (Burma)", "Cellular Jail (Andamans)", "Yerwada (Pune)", "Alipore (Calcutta)"], "Mandalay (Burma)",
        "After the 1908 sedition trial over *Kesari* articles, Tilak served **1908–14 in Mandalay**, writing *Geeta Rahasya* there.",
        "Tilak = Mandalay; Savarkar = Andamans.", 25)
    S.q("ga-en-p4", "medium", "The stated purpose of the **Partition of Bengal (1905)** was —",
        ["Administrative convenience", "Separate electorates", "Defence reorganisation", "Revenue settlement"], "Administrative convenience",
        "Curzon claimed the province was too big to govern; nationalists saw the real aim — splitting Bengali unity — and launched the Swadeshi movement.",
        "Stated = administrative; real = divide the nationalists.", 25)
    S.q("ga-en-p4", "hard", "Match:\n1. Rakhi bandhan as protest — Rabindranath Tagore\n2. *Amar Sonar Bangla* — composed during Swadeshi agitation\n3. National Council of Education — 1906\nWhich are correct?",
        ["1, 2 and 3", "1 and 2 only", "2 and 3 only", "1 and 3 only"], "1, 2 and 3",
        "All three are Swadeshi-era facts: Tagore's Rakhi tying and later the song (now Bangladesh's anthem), and the **National Council of Education (1906)** for national education.",
        "Swadeshi trio: Rakhi, song, NCE 1906.", 30)
    S.q("ga-en-p5", "easy", "The Congress split into Moderates and Extremists took place at the **Surat session** of —",
        ["1905", "1906", "1907", "1909"], "1907",
        "The **1907 Surat session** (Rash Behari Ghosh's presidency disputed) split the party; the wings reunited at **Lucknow in 1916**.",
        "Surat 1907 split; Lucknow 1916 reunion.", 20)
    S.q("ga-en-p5", "medium", "At which Congress session were the **Moderates and Extremists reunited**?",
        ["Calcutta, 1906", "Lucknow, 1916", "Nagpur, 1920", "Karachi, 1931"], "Lucknow, 1916",
        "The **Lucknow session (1916)** saw the reunion and the **Congress-League pact** (which accepted separate electorates).",
        "Lucknow 1916: reunion + League pact.", 25)
    S.q("ga-en-p6", "medium", "Who among the following was the **first Indian member of the Viceroy's Executive Council** (1909)?",
        ["Satyendra Prasad Sinha", "S.P. Mookerjee", "C.R. Das", "Tej Bahadur Sapru"], "Satyendra Prasad Sinha",
        "The **Morley-Minto reforms (1909)** admitted **S.P. Sinha** (law member) to the Viceroy's Executive Council — and introduced separate electorates.",
        "Sinha in; separate electorates in — both 1909.", 25)
    S.q("ga-en-p6", "hard", "Consider the statements about the **Home Rule Leagues (1916)**:\n1. Tilak's league worked in Maharashtra, Karnataka, the Central Provinces and Berar.\n2. Annie Besant's league had its headquarters at Adyar, Madras.\n3. Both leagues demanded Dominion Status within the British Empire.\nWhich are correct?",
        ["1, 2 and 3", "1 and 2 only", "2 and 3 only", "1 and 3 only"], "1, 2 and 3",
        "All three hold: the two leagues divided the country between them (Tilak: April 1916; Besant: September 1916) and both pressed for self-government within the Empire.",
        "Two leagues, one demand: Home Rule.", 30)
    return S


def build_gandhi():
    S = Sub("gandhian-era")
    S.notes = """### Gandhi arrives (1915)
Mohandas Karamchand Gandhi — a barrister who had forged the **satyagraha** (truth-force, passive resistance) method in South Africa from 1906 — landed in India on **9 January 1915**. Three local struggles taught India the method:
- **Champaran, 1917** (Bihar): against the forced indigo cultivation and the **tinkathia** system; **Rajkumar Shukla** brought Gandhi; his **first satyagraha in India**.
- **Ahmedabad mill strike, 1918**: for mill workers' plague bonus — his **first hunger strike**.
- **Kheda, 1918** (Gujarat): **no-revenue** campaign for famine-hit peasants, organised with **Sardar Vallabhbhai Patel**.

### 1919: Rowlatt, Jallianwala, Khilafat
The **Rowlatt Act (1919)** allowed detention without trial — 'no dalil, no vakil, no appeal'. The **Jallianwala Bagh massacre (13 April 1919)**, Amritsar: General **Dyer** fired on an unarmed Baisakhi crowd; **Rabindranath Tagore** returned his knighthood; **Udham Singh** shot Michael O'Dwyer in London (1940). The **Khilafat movement** (Ali brothers) against the Ottoman Caliphate's treatment folded into Gandhi's **Non-Cooperation Movement (1920–22)**: boycott of schools, courts, titles and foreign cloth. It was withdrawn in **February 1922** after violence at **Chauri Chaura** (Gorakhpur). The **Swaraj Party (1923)** — C.R. Das and Motilal Nehru — entered councils instead.

### From Simon to Purna Swaraj
The all-white **Simon Commission (arrived 1928)** was met with 'Go back Simon'; **Lala Lajpat Rai** was fatally injured in its Lahore lathi charge. The **Nehru Report (1928)** — Motilal Nehru — was India's first constitution draft. At **Lahore (December 1929)**, with **Jawaharlal Nehru** as president, Congress declared **Purna Swaraj**; **26 January 1930** was observed as Independence Day.

### Civil Disobedience (1930–34)
Gandhi marched **12 March 1930** from Sabarmati with 78 followers to **Dandi**, breaking the salt law on **6 April 1930**. The **Gandhi-Irwin Pact (5 March 1931)** ended the phase; Gandhi went alone to the **Second Round Table Conference (1931)**. The **Communal Award (1932)** gave separate electorates to the Depressed Classes; the **Poona Pact (September 1932)** with **Ambedkar** replaced them with reserved seats under joint electorates. The **Government of India Act, 1935** gave provincial autonomy — Congress ministries ruled 1937–39.

### 1942–47: Quit India and freedom
Rejecting the **Cripps offer (1942)** — Gandhi's 'post-dated cheque on a crashing bank' — Congress passed the **Quit India resolution on 8 August 1942** at Gowalia Tank, Bombay: **'Do or Die'**. The leaders were arrested at once; **Aruna Asaf Ali** hoisted the flag, **Usha Mehta** ran the Congress Radio; parallel governments rose at **Ballia (Chittu Pandey), Satara (Nana Patil) and Tamluk**. Meanwhile **Subhas Chandra Bose** revived the **INA** (Azad Hind government, Singapore, 1943; 'Dilli Chalo'; 'Give me blood, I will give you freedom'; Rani Jhansi Regiment — Lakshmi Sahgal). The **Cabinet Mission (1946)** — Pethick-Lawrence, Cripps, Alexander — planned the transfer; after **Direct Action Day (16 August 1946)** and the **Mountbatten Plan (3 June 1947)**, power was transferred on **15 August 1947**.

### Quick revision
- First satyagraha in India: Champaran 1917 (tinkathia, Rajkumar Shukla); then Ahmedabad 1918, Kheda 1918.
- 1919: Rowlatt Act → Jallianwala (Dyer, 13 April) → Tagore's knighthood back.
- NCM 1920–22 ends at Chauri Chaura; Swaraj Party 1923 (Das, Motilal).
- Lahore 1929 (Jawaharlal) → 26 Jan 1930 → Dandi (12 Mar–6 Apr 1930) → Gandhi-Irwin 1931 → Poona Pact 1932.
- 1942: Quit India, 'Do or Die'; Bose: Azad Hind 1943; 1946 Cabinet Mission; 15 Aug 1947."""
    S.pattern("ga-ge-p1", "Gandhi's early satyagrahas", "very common",
        "'Gandhi's first satyagraha in India was at…', tinkathia system, hunger strike, no-revenue campaign — order and facts.",
        None,
        "1. **Champaran 1917** (indigo, tinkathia; Bihar) → **Ahmedabad 1918** (mill workers, first hunger strike) → **Kheda 1918** (no revenue, with Patel).\n2. Champaran = first satyagraha in India; the SA experiments (1906) came earlier abroad.\n3. Rajkumar Shukla = the man who brought Gandhi to Champaran.",
        "In which movement did Gandhi use a **hunger strike** for the first time in India?",
        "The **Ahmedabad mill strike (1918)** — for the workers' plague bonus.")
    S.pattern("ga-ge-p2", "Rowlatt Act and Jallianwala Bagh", "very common",
        "'No vakil, no dalil, no appeal' act, Jallianwala date and general, reactions (Tagore, Udham Singh).",
        None,
        "1. **Rowlatt Act, 1919** = detention without trial → nationwide hartal.\n2. **13 April 1919, Jallianwala Bagh, Amritsar** — General **Dyer**; Baisakhi day.\n3. Reactions: **Tagore** returned his knighthood; **Udham Singh** killed **O'Dwyer** in London (1940).",
        "The Jallianwala Bagh massacre took place on —",
        "**13 April 1919** (Baisakhi day), when General Dyer's troops fired on an unarmed meeting.")
    S.pattern("ga-ge-p3", "Non-Cooperation and Chauri Chaura", "very common",
        "'Why was the Non-Cooperation Movement withdrawn', the Chauri Chaura incident, Khilafat linkage, Swaraj Party.",
        None,
        "1. **NCM 1920–22**: with Khilafat (Ali brothers); boycott of schools-courts-titles-foreign cloth.\n2. **Chauri Chaura (5 February 1922**, Gorakhpur): a mob burnt a police station — Gandhi withdrew the movement (Bardoli resolution).\n3. The council-entry wing became the **Swaraj Party (1923)** — C.R. Das and Motilal Nehru.",
        "The Non-Cooperation Movement was withdrawn in 1922 after the incident at —",
        "**Chauri Chaura** (Gorakhpur, UP), where demonstrators set a police station on fire.")
    S.pattern("ga-ge-p4", "Civil Disobedience: Dandi and the pacts", "very common",
        "Dandi March dates, salt law, Gandhi-Irwin Pact, Round Table Conference, Poona Pact, Communal Award.",
        None,
        "1. **12 March 1930** Sabarmati → **6 April 1930** salt broken at **Dandi** (78 marchers).\n2. **Gandhi-Irwin Pact, 5 March 1931** → Gandhi attends the **Second RTC (1931)** alone.\n3. **Communal Award (1932)** → **Poona Pact (1932)** with Ambedkar: reserved seats, joint electorates.",
        "The **Gandhi-Irwin Pact** was signed in —",
        "**March 1931** — ending the Civil Disobedience Movement; Gandhi then attended the Second Round Table Conference.")
    S.pattern("ga-ge-p5", "Simon to Purna Swaraj chain", "common",
        "Simon Commission facts, Nehru Report, Lahore session 1929, 26 January 1930.",
        None,
        "1. **Simon Commission** (appointed 1927, arrived 1928): all-white → boycott; **Lajpat Rai** injured at Lahore, died 17 November 1928.\n2. **Nehru Report 1928** (Motilal): first Indian constitutional draft, Dominion Status demand.\n3. **Lahore, Dec 1929**: Jawaharlal president; **Purna Swaraj**; 26 January 1930 = first Independence Day.",
        "The **Purna Swaraj** resolution was passed at the Lahore session of —",
        "**December 1929**, with Jawaharlal Nehru as president; 26 January 1930 was the first Independence Day.")
    S.pattern("ga-ge-p6", "Quit India, INA and the endgame", "common",
        "'Do or Die', Gowalia Tank, parallel governments, Azad Hind/INA facts, Cabinet Mission, Mountbatten Plan.",
        None,
        "1. **8 August 1942, Gowalia Tank, Bombay**: Quit India; 'Do or Die'; leaders arrested the same night.\n2. Underground: **Aruna Asaf Ali** (flag), **Usha Mehta** (Congress Radio); parallel governments — Ballia (Chittu Pandey), Satara (Nana Patil), Tamluk.\n3. **Bose**: Azad Hind government (Singapore, 1943), 'Give me blood…', Rani Jhansi Regiment (Lakshmi Sahgal); **Cabinet Mission 1946** → **Mountbatten Plan 3 June 1947** → **15 August 1947**.",
        "Aruna Asaf Ali is remembered in the Quit India Movement for —",
        "**Hoisting the Indian flag at Gowalia Tank maidan**, Bombay, as the leaders were arrested.")

    S.q("ga-ge-p1", "easy", "Gandhi's **first satyagraha in India** was launched at —",
        ["Kheda", "Champaran", "Ahmedabad", "Bardoli"], "Champaran",
        "**Champaran (Bihar), 1917**, against the tinkathia indigo system — Rajkumar Shukla had persuaded Gandhi to come.",
        "Champaran 1917 first; Bardoli was 1928 (Patel).", 20)
    S.q("ga-ge-p1", "medium", "The **tinkathia system**, which Gandhi fought in 1917, obliged Champaran peasants to —",
        ["Grow indigo on 3/20 of their land", "Pay revenue twice a year", "Serve as bonded labourers", "Provide free transport to indigo factories"], "Grow indigo on 3/20 of their land",
        "**Tinkathia** forced each raiyat to cultivate indigo on the **three kathas in every twenty** of his best land.",
        "Teen katha = 3/20.", 25)
    S.q("ga-ge-p1", "hard", "Arrange chronologically:\n1. Ahmedabad mill strike\n2. Champaran Satyagraha\n3. Kheda Satyagraha\n4. Return of Gandhi to India",
        ["4, 2, 1, 3", "4, 2, 3, 1", "2, 4, 1, 3", "4, 1, 2, 3"], "4, 2, 1, 3",
        "Returned **9 January 1915** → **Champaran 1917** → **Ahmedabad 1918** (mill) → **Kheda 1918** (revenue).",
        "15-17-18-18: return, Champaran, then the two 1918 fights.", 30)
    S.q("ga-ge-p2", "easy", "The **Jallianwala Bagh massacre** was carried out on the orders of —",
        ["General Dyer", "Michael O'Dwyer", "Lord Chelmsford", "General Dyer and O'Dwyer jointly"], "General Dyer",
        "Brigadier-General **Reginald Dyer** ordered the firing on 13 April 1919; O'Dwyer was the Punjab Governor — later shot dead by Udham Singh (1940).",
        "Dyer fired; O'Dwyer backed — Udham Singh shot O'Dwyer.", 20)
    S.q("ga-ge-p2", "medium", "The **Rowlatt Act (1919)** is remembered as the act of —",
        ["'No vakil, no dalil, no appeal'", "'Divide and rule'", "'Doctrine of Lapse'", "'Go back Simon'"], "'No vakil, no dalil, no appeal'",
        "The Rowlatt Act allowed arrest and detention **without trial** — no lawyer, no argument, no appeal — and was never actually used much before it was repealed.",
        "Rowlatt = detention without trial.", 20)
    S.q("ga-ge-p3", "easy", "The **Non-Cooperation Movement** was formally withdrawn after the violence at —",
        ["Chauri Chaura", "Kakori", "Bardoli", "Champaran"], "Chauri Chaura",
        "At **Chauri Chaura (Gorakhpur), 5 February 1922**, a mob set a police station ablaze; Gandhi, committed to non-violence, called off the movement.",
        "Chauri Chaura 1922 = withdrawal.", 20)
    S.q("ga-ge-p3", "medium", "The **Swaraj Party** (1923), which entered the councils, was founded by —",
        ["C.R. Das and Motilal Nehru", "Tilak and Lajpat Rai", "Nehru and Bose", "Malaviya and Lajpat Rai"], "C.R. Das and Motilal Nehru",
        "After NCM's withdrawal, **C.R. Das and Motilal Nehru** formed the Swaraj Party to fight councils from within.",
        "Das + Motilal = council entry.", 25)
    S.q("ga-ge-p4", "medium", "How many volunteers accompanied Gandhi on the **Dandi March**?",
        ["78", "100", "144", "48"], "78",
        "Gandhi left Sabarmati on **12 March 1930 with 78 followers**, covering about 240 miles to Dandi and breaking the salt law on **6 April 1930**.",
        "78 marchers, 240 miles, 24 days.", 25)
    S.q("ga-ge-p4", "hard", "Match:\n1. Communal Award — Ramsay MacDonald, 1932\n2. Poona Pact — reserved seats under joint electorates\n3. Gandhi attended the First Round Table Conference\nWhich are correct?",
        ["1 and 2 only", "2 and 3 only", "1 and 3 only", "1, 2 and 3"], "1 and 2 only",
        "Gandhi attended only the **Second** RTC (1931) — the First (1930) had no Congress representative.",
        "First RTC = no Congress; Gandhi = Second only.", 30)
    S.q("ga-ge-p5", "medium", "The **Nehru Report (1928)**, India's first constitution draft, was prepared under —",
        ["Jawaharlal Nehru", "Motilal Nehru", "Tej Bahadur Sapru", "M.R. Jayakar"], "Motilal Nehru",
        "**Motilal Nehru** chaired the committee that drafted the **Nehru Report (1928)**, demanding Dominion Status — Jinnah answered with his Fourteen Points.",
        "Report 1928 = Motilal; presidency 1929 = Jawaharlal.", 25)
    S.q("ga-ge-p5", "easy", "**26 January 1930** is significant because —",
        ["The first Independence Day was observed", "The Dandi March began", "The Poona Pact was signed", "The Simon Commission arrived"], "The first Independence Day was observed",
        "After the **Lahore Purna Swaraj resolution (Dec 1929)**, **26 January 1930** was celebrated as Independence Day — the date later chosen for the Republic (1950).",
        "26 Jan: 1930 Independence Day → 1950 Republic.", 20)
    S.q("ga-ge-p6", "easy", "The **Quit India** resolution was passed on 8 August 1942 at —",
        ["Gowalia Tank, Bombay", "Lahore", "Sevagram", "Wardha"], "Gowalia Tank, Bombay",
        "The All India Congress Committee passed Quit India at **Gowalia Tank (August Kranti Maidan), Bombay**, with Gandhi's call: **'Do or Die'**.",
        "Gowalia Tank = August Kranti Maidan.", 20)
    S.q("ga-ge-p6", "medium", "The **Rani of Jhansi Regiment** of the INA was commanded by —",
        ["Lakshmi Sahgal", "Aruna Asaf Ali", "Sucheta Kripalani", "Usha Mehta"], "Lakshmi Sahgal",
        "**Captain Lakshmi Sahgal** led the INA's women's regiment under Subhas Bose's Azad Hind government (1943).",
        "Rani Jhansi Regiment = Lakshmi Sahgal.", 25)
    S.q("ga-ge-p6", "hard", "Who among the following were the members of the **Cabinet Mission (1946)**?\n1. Lord Pethick-Lawrence\n2. Stafford Cripps\n3. A.V. Alexander\n4. Lord Wavell",
        ["1, 2 and 3", "2, 3 and 4", "1, 3 and 4", "1, 2 and 4"], "1, 2 and 3",
        "The **Cabinet Mission** = Pethick-Lawrence (Secretary of State), **Cripps** and **Alexander**. Wavell was the Viceroy, not a mission member.",
        "Three Englishmen + the Viceroy outside.", 30)
    return S


def build_press():
    S = Sub("press-books")
    S.notes = """### Why the press mattered
The national movement ran on print. Newspapers created all-India opinion, spread boycott calls, and paid for it with prosecution. Know the paper, its editor and its language — that trio is the whole question bank.

### Early national press
**Raja Ram Mohan Roy** was the pioneer: *Sambad Kaumudi* (Bengali, 1821) and *Mirat-ul-Akbar* (Persian, 1822). **Amrita Bazar Patrika** (1868, the Ghosh brothers — Sisir Kumar and Motilal) began in Bengali; when the **Vernacular Press Act (1878)** gagged Indian-language papers, it converted itself into an English daily **overnight**. *The Hindu* (Madras, 1878) was founded by **G. Subramania Iyer**. **Surendranath Banerjea** edited *Bengalee*; *Kesari* (Marathi) and *Mahratta* (English), both 1881, were **Tilak's** platforms. The **Vernacular Press Act (1878)** — Lytton's 'Gagging Act' — was repealed by **Ripon in 1882**; earlier, **Metcalfe (1835)** had earned the title 'liberator of the Indian press'.

### Papers of the freedom struggle
**Gandhi**: *Young India* (English) and *Navajivan* (Gujarati) during NCM; *Harijan* (1933) for the anti-untouchability work. **Annie Besant**: *New India* and *Commonweal*. **Maulana Azad**: Urdu *Al-Hilal* (1912) and *Al-Balagh*. **Muhammad Ali** (of the Ali brothers): *Comrade*. **Aurobindo Ghosh**: *Bande Mataram*; **Bipin Chandra Pal** worked on it too. Sir Syed's *Tahdhib-ul-Akhlaq* carried the Aligarh message.

### The books to memorise
| Book | Author |
|---|---|
| *Poverty and Un-British Rule in India* (1901) | Dadabhai Naoroji |
| *Economic History of India* | R.C. Dutt |
| *Hind Swaraj* (1909) | Gandhi |
| *My Experiments with Truth* (autobiography, 1927) | Gandhi |
| *Geeta Rahasya* (in Mandalay jail) | Tilak |
| *Ghulamgiri* (1873) | Jyotiba Phule |
| *Annihilation of Caste* (1936) | B.R. Ambedkar |
| *The Indian Struggle* (1935) | Subhas Chandra Bose |
| *Toward Freedom* (autobiography, 1936) | Jawaharlal Nehru |
| *Glimpses of World History* (1934) | Jawaharlal Nehru |
| *Discovery of India* (1946) | Jawaharlal Nehru |
| *India Wins Freedom* | Maulana Abul Kalam Azad |
| *India Divided* | Rajendra Prasad |
| *Unhappy India* (1928) | Lala Lajpat Rai |

### Songs and symbols from print
**Bankim Chandra Chatterjee's** novel *Anandamath* (1882) gave the song **Vande Mataram**, first sung at the **1896 Calcutta Congress session** by Rabindranath Tagore. Tagore's *Amar Sonar Bangla* was written during the 1905 Swadeshi agitation.

### Quick revision
- Roy: Sambad Kaumudi (Bengali) + Mirat-ul-Akbar (Persian).
- Amrita Bazar Patrika: Ghosh brothers; turned English overnight after the 1878 Act.
- Gandhi: Young India, Navajivan, Harijan (1933). Besant: New India, Commonweal. Azad: Al-Hilal.
- Naoroji: Poverty and Un-British Rule; Dutt: Economic History; Bose: Indian Struggle.
- Nehru: Toward Freedom, Glimpses, Discovery; Azad: India Wins Freedom."""
    S.pattern("ga-pb-p1", "Newspaper ↔ editor/founder", "very common",
        "'Who edited Kesari', 'New India was published by', match-the-column of papers and editors.",
        None,
        "1. Tilak = *Kesari* + *Mahratta*; Besant = *New India* + *Commonweal*; Gandhi = *Young India* + *Navajivan* + *Harijan*.\n2. Azad = *Al-Hilal*; Muhammad Ali = *Comrade*; S.N. Banerjea = *Bengalee*; Aurobindo = *Bande Mataram*.\n3. Watch the near-pair: *New India* is Besant's paper — not Pal's, not Nehru's.",
        "The newspaper ***New India***, which carried the Home Rule campaign, was started by —",
        "**Annie Besant** — her other paper was *Commonweal*.")
    S.pattern("ga-pb-p2", "Book ↔ author", "very common",
        "'Who wrote Discovery of India', 'Ghulamgiri is a work by', match-the-column of books and authors.",
        None,
        "1. Gandhi = *Hind Swaraj* + *My Experiments with Truth*; Nehru = *Toward Freedom* + *Glimpses* + *Discovery of India*.\n2. Economic pair: Naoroji (*Poverty and Un-British Rule*) vs R.C. Dutt (*Economic History of India*).\n3. Azad = *India Wins Freedom*; Prasad = *India Divided*; Bose = *The Indian Struggle*; Ambedkar = *Annihilation of Caste*.",
        "The book ***Discovery of India*** was written by —",
        "**Jawaharlal Nehru**, during his Ahmednagar prison years (1946).")
    S.pattern("ga-pb-p3", "Press laws: 1878 Act and press freedom", "common",
        "'Vernacular Press Act was passed by/repealed by', which paper changed language overnight, Metcalfe's title.",
        None,
        "1. **Vernacular Press Act, 1878** — Lord **Lytton**; repealed by **Ripon, 1882**.\n2. **Amrita Bazar Patrika** turned into an English paper overnight to escape it.\n3. **Metcalfe (1835)** = 'liberator of the Indian press'.",
        "The **Vernacular Press Act (1878)** was repealed by —",
        "**Lord Ripon**, in 1882.")
    S.pattern("ga-pb-p4", "Gandhi's journals", "common",
        "'Harijan was started in', which paper during Non-Cooperation, language of Navajivan.",
        None,
        "1. NCM years: *Young India* (English) and *Navajivan* (Gujarati).\n2. ***Harijan*** (1933): English weekly for the anti-untouchability campaign; sister papers *Harijan Bandhu* (Gujarati), *Harijan Sevak* (Hindi).\n3. *Indian Opinion* (1903) was Gandhi's South African paper.",
        "Gandhi started the English weekly ***Harijan*** in —",
        "**1933**, for the removal of untouchability.")
    S.pattern("ga-pb-p5", "Anandamath, Vande Mataram and protest writings", "common",
        "Source of Vande Mataram, where it was first sung, Amar Sonar Bangla's origin, Unhappy India as a reply to Mother India.",
        None,
        "1. *Anandamath* (1882) by **Bankim Chandra Chatterjee** contains **Vande Mataram**; first sung by **Tagore** at the **1896 Calcutta Congress**.\n2. Tagore's ***Amar Sonar Bangla*** (1905 Swadeshi) later became Bangladesh's anthem.\n3. Lajpat Rai's *Unhappy India* (1928) answered Katherine Mayo's *Mother India*.",
        "The song ***Vande Mataram*** first appeared in —",
        "Bankim Chandra Chatterjee's novel ***Anandamath*** (1882).")

    S.q("ga-pb-p1", "easy", "***Kesari*** and ***Mahratta***, started in 1881, were edited by —",
        ["Gopal Krishna Gokhale", "Bal Gangadhar Tilak", "Bipin Chandra Pal", "Aurobindo Ghosh"], "Bal Gangadhar Tilak",
        "**Tilak** ran *Kesari* in Marathi and *Mahratta* in English — both from Pune; his 1908 *Kesari* articles led to the Mandalay sentence.",
        "Kesari (Marathi) + Mahratta (English) = Tilak.", 20)
    S.q("ga-pb-p1", "medium", "***Bengalee***, the newspaper associated with the Indian Association (1876), was edited by —",
        ["Surendranath Banerjea", "W.C. Bonnerjee", "R.C. Dutt", "Pherozeshah Mehta"], "Surendranath Banerjea",
        "**S.N. Banerjea** used *Bengalee* to campaign for civil rights and against the 1905 partition; he founded the Indian Association in 1876.",
        "Banerjea = Bengalee.", 25)
    S.q("ga-pb-p1", "hard", "Which newspaper, founded in 1868, **changed its language from Bengali to English overnight** to escape the Vernacular Press Act?",
        ["Amrita Bazar Patrika", "The Hindu", "Bengalee", "Sambad Kaumudi"], "Amrita Bazar Patrika",
        "The **Ghosh brothers' Amrita Bazar Patrika** began as a Bengali paper (Jessore, 1868); in 1878 it converted to English overnight to dodge Lytton's gag.",
        "1878 Act → overnight English switch.", 30)
    S.q("ga-pb-p2", "easy", "The book ***Ghulamgiri*** (Slavery, 1873) was written by —",
        ["Jyotiba Phule", "B.R. Ambedkar", "Raja Ram Mohan Roy", "Periyar E.V. Ramaswamy"], "Jyotiba Phule",
        "**Phule's *Ghulamgiri*** attacked caste slavery and the tyranny of the 'higher' castes.",
        "Ghulamgiri = Phule.", 20)
    S.q("ga-pb-p2", "medium", "***The Indian Struggle* (1935)**, covering 1920–34, was written by —",
        ["Subhas Chandra Bose", "Jawaharlal Nehru", "V.D. Savarkar", "Rajendra Prasad"], "Subhas Chandra Bose",
        "**Bose's *The Indian Struggle*** narrated the national movement of 1920–34; the book was promptly banned in British India.",
        "Indian Struggle = Bose; Discovery = Nehru.", 25)
    S.q("ga-pb-p2", "hard", "Match:\n1. *India Wins Freedom* — Maulana Abul Kalam Azad\n2. *India Divided* — Rajendra Prasad\n3. *Unhappy India* — Lala Lajpat Rai\nWhich are correct?",
        ["1, 2 and 3", "1 and 2 only", "2 and 3 only", "1 and 3 only"], "1, 2 and 3",
        "All three pairings are right: Azad's memoir, Prasad's partition critique, and Lajpat Rai's 1928 reply to *Mother India*.",
        "Freedom-Divided-Unhappy: Azad, Prasad, Lajpat Rai.", 30)
    S.q("ga-pb-p3", "easy", "The **Vernacular Press Act (1878)** — the 'Gagging Act' — was passed by —",
        ["Lord Ripon", "Lord Lytton", "Lord Curzon", "Lord Dufferin"], "Lord Lytton",
        "**Lytton** gagged Indian-language papers in 1878; **Ripon repealed** it in 1882.",
        "Lytton gags, Ripon releases.", 20)
    S.q("ga-pb-p4", "medium", "During the **Non-Cooperation Movement**, Gandhi's English journal was —",
        ["Young India", "Harijan", "Navajivan", "Indian Opinion"], "Young India",
        "Gandhi ran ***Young India*** (English) and ***Navajivan*** (Gujarati) in the NCM years; *Harijan* began only in 1933.",
        "Young India (EN) + Navajivan (Guj) = NCM; Harijan = 1933.", 25)
    S.q("ga-pb-p4", "medium", "Gandhi's *Indian Opinion*, his first journal, was published from —",
        ["South Africa", "Gujarat", "Maharashtra", "London"], "South Africa",
        "Gandhi started ***Indian Opinion*** in **1903 in South Africa**, years before his Indian journals.",
        "Indian Opinion = SA, 1903.", 25)
    S.q("ga-pb-p5", "easy", "The song ***Vande Mataram*** occurs in Bankim Chandra Chatterjee's novel —",
        ["Anandamath", "Devi Chaudhurani", "Durgeshnandini", "Kapalkundala"], "Anandamath",
        "***Anandamath* (1882)** contains Vande Mataram; Tagore first sang it at the **1896 Calcutta session** of the Congress.",
        "Anandamath → Vande Mataram.", 20)
    S.q("ga-pb-p5", "medium", "Rabindranath Tagore composed ***Amar Sonar Bangla*** during —",
        ["The Swadeshi movement against the 1905 partition", "The Non-Cooperation Movement", "The Quit India Movement", "The Jallianwala protests"], "The Swadeshi movement against the 1905 partition",
        "Written during the **1905 anti-partition agitation**, the song is now the national anthem of **Bangladesh**.",
        "1905 Swadeshi song → Bangladesh anthem.", 25)
    S.q("ga-pb-p2", "hard", "Consider the statements:\n1. *Hind Swaraj* was written by Gandhi in 1909.\n2. *Geeta Rahasya* was composed by Tilak in prison.\n3. *Annihilation of Caste* was an undelivered speech of Nehru.\nWhich are correct?",
        ["1 and 2 only", "2 and 3 only", "1 and 3 only", "1, 2 and 3"], "1 and 2 only",
        "*Annihilation of Caste* (1936) is **Ambedkar's** undelivered address to the Jat-Pat-Todak Mandal, not Nehru's.",
        "Caste annihilation = Ambedkar's speech.", 30)
    S.q("ga-pb-p3", "medium", "Which Governor-General is called the **'liberator of the Indian press'**?",
        ["Lord Metcalfe", "Lord Bentinck", "Lord Ripon", "Lord Canning"], "Lord Metcalfe",
        "**Charles Metcalfe** removed press restrictions in 1835 — press freedom stayed until the 1878 Act; Ripon later repealed that Act.",
        "Metcalfe 1835 liberates; Lytton 1878 gags; Ripon 1882 repeals.", 25)
    return S
