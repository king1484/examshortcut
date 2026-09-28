"""Phase-2 deep content build for ga/modern-history. Run: py -3 modern-history.py"""
import os
import sys

sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
from _lib import apply_topic
import mod_part1
import mod_part2


def P(pattern, frequency, howToSpot, approach, subtopic, q, sol):
    return {"pattern": pattern, "frequency": frequency, "howToSpot": howToSpot, "approach": approach,
            "subtopic": subtopic, "example": {"q": q, "solution": sol}}


PYQ = [
    P("Event ↔ year chronology", "very common",
      "Arrange 3–4 events in order, or 'which happened first/last'. The single most repeated modern-history ask, from Plassey to independence.",
      "Fix anchor years once (1757, 1857, 1885, 1905, 1919, 1930, 1942, 1947) and slot each event against them; never rely on 'feel' — place the two events you are sure of and the order falls out.",
      "gandhian-era",
      "Arrange: (1) Jallianwala Bagh (2) Chauri Chaura (3) Dandi March (4) Quit India.",
      "1919 → 1922 → 1930 → 1942, so the order is 1, 2, 3, 4."),
    P("Governor-General/Viceroy ↔ event or reform", "very common",
      "'Who was the Governor-General when…', 'the Doctrine of Lapse was applied by', or a match-the-column of Viceroys and events.",
      "Memorise the spine: Cornwallis (judicial), Bentinck (social reforms, sati), Dalhousie (annexations, railways), Lytton (press gag), Ripon (local self-government), Curzon (partition of Bengal), Minto (Morley-Minto). Each Viceroy owns 1–2 tag facts.",
      "british-expansion",
      "Under which Governor-General was the **Doctrine of Lapse** used to annex princely states?",
      "**Dalhousie** (1848–56) — Satara, Jhansi, Nagpur and others annexed by refusing adopted heirs."),
    P("1857 revolt centre ↔ leader", "common",
      "A centre (Kanpur, Lucknow, Jhansi, Bareilly…) is named and its leader asked, often as match-the-column.",
      "Six pairs settle it: Delhi–Bahadur Shah II, Kanpur–Nana Saheb, Lucknow–Begum Hazrat Mahal, Jhansi–Rani Lakshmibai, Bareilly–Khan Bahadur Khan, Bihar (Jagdishpur)–Kunwar Singh.",
      "revolt-1857",
      "Who led the 1857 revolt at **Kanpur**?",
      "**Nana Saheb** — with Tantia Tope as his commander and the seized treasury; Lucknow belongs to Begum Hazrat Mahal, not him."),
    P("Congress session ↔ president / resolution", "very common",
      "'The Lahore session of 1929 was presided over by', 'Purna Swaraj was declared at…', or the session where a famous word entered the resolution.",
      "Pin the famous sessions: 1885 Bombay (Bonnerjee), 1906 Calcutta (Naoroji — 'Swaraj'), 1907 Surat (split), 1916 Lucknow (reunion), 1929 Lahore (Jawaharlal — Purna Swaraj), 1931 Karachi (Fundamental Rights), 1942 (Quit India, AICC).",
      "early-nationalism",
      "At which session did the Congress resolve to strive for **'Swaraj'** (1906)?",
      "The **Calcutta session of 1906**, with Dadabhai Naoroji in the chair."),
    P("Newspaper / book ↔ editor / author", "very common",
      "'Kesari was edited by', 'Discovery of India was written by', and match-the-column sets mixing papers and books in one question.",
      "Cluster by person: Tilak (Kesari, Mahratta, Geeta Rahasya), Gandhi (Young India, Navajivan, Harijan, Hind Swaraj, Experiments), Nehru (Toward Freedom, Glimpses, Discovery), Naoroji vs R.C. Dutt for the two economics books.",
      "press-books",
      "The author of ***India Wins Freedom*** is —",
      "**Maulana Abul Kalam Azad** — Rajendra Prasad wrote *India Divided*; don't swap the pair."),
    P("Movement ↔ its features", "very common",
      "Statements about a movement (its trigger, methods, where it spread, why it ended) with 'which is/are correct'.",
      "For each movement fix four anchors — trigger event, signature method, geographic spread, end event. Example, Civil Disobedience: salt law broken at Dandi, no-revenue/no-tax, spread widest in Gujarat and Tamil belt, ended by the Gandhi-Irwin Pact.",
      "gandhian-era",
      "The Civil Disobedience Movement was launched in 1930 by —",
      "Breaking the **salt law at Dandi** (6 April 1930), after the 12 March march from Sabarmati."),
    P("Slogan / quote ↔ person", "common",
      "'Swaraj is my birthright' — who said it, 'Do or Die', 'Give me blood', 'Dilli Chalo', and other one-line attributions.",
      "Attribute by decade and method: Tilak (birthright), Gandhi (Do or Die, the three monkeys), Bose (Dilli Chalo, Give me blood), Bhagat Singh (Inquilab Zindabad popularised), Nehru (the tryst with destiny, 1947).",
      "early-nationalism",
      "'Give me blood, I will give you freedom' was said by —",
      "**Subhas Chandra Bose**, to the INA in 1944."),
    P("19th-century reform ↔ reformer and society", "common",
      "'The Brahmo Samaj was founded by', statements on widow remarriage, sati abolition, Aligarh movement, and their year-provision mix.",
      "Track reformer → society → year: Ram Mohan Roy (Brahmo Sabha 1828, sati abolished 1829 with Bentinck), Dayananda (Arya Samaj 1875), Ramakrishna–Vivekananda (Mission 1897), Syed Ahmad Khan (MAO College 1875), Phule (Satyashodhak Samaj 1873).",
      "reform-movements",
      "The practice of **sati** was legally abolished in 1829 through the efforts of —",
      "**Raja Ram Mohan Roy**, whose campaign persuaded Lord William Bentinck to pass the regulation."),
]

if __name__ == "__main__":
    subs = [
        mod_part1.build_british(),
        mod_part1.build_revolt(),
        mod_part1.build_reform(),
        mod_part2.build_early(),
        mod_part2.build_gandhi(),
        mod_part2.build_press(),
    ]
    apply_topic("modern-history", subs, PYQ)
