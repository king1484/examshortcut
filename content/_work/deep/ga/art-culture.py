"""Phase-2 deep content build for ga/art-culture. Run: py -3 art-culture.py"""
import os
import sys

sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
from _lib import apply_topic
import ac_part1
import ac_part2


def P(pattern, frequency, howToSpot, approach, subtopic, q, sol):
    return {"pattern": pattern, "frequency": frequency, "howToSpot": howToSpot, "approach": approach,
            "subtopic": subtopic, "example": {"q": q, "solution": sol}}


PYQ = [
    P("Dance ↔ state", "very common",
      "A classical or folk dance named with four states as options (or a 'correctly matched pair' set).",
      "Classical nine first: TN-Bharatanatyam, UP-Kathak, Kerala-Kathakali + Mohiniyattam ('Kerala has two'), AP-Kuchipudi, Odisha-Odissi, Manipur-Manipuri, Assam-Sattriya. For folk, run the state table; NE dances fall to the mnemonic Cheraw-bamboo (Mizoram), Hojagiri-balancing (Tripura), Nongkrem-Khasi (Meghalaya).",
      "classical-dances",
      "**Kathakali** belongs to which state?",
      "**Kerala** — which also owns Mohiniyattam; Karnataka's dance-drama Yakshagana is folk, not classical."),
    P("Artist ↔ instrument / dance", "very common",
      "A maestro's name (Birju Maharaj, Bismillah Khan, Zakir Hussain, Kelucharan Mohapatra) with four art forms.",
      "One-to-one pairs: Birju Maharaj-Kathak, Rukmini Devi-Bharatanatyam (Kalakshetra), Mohapatra-Odissi, Bismillah Khan-shehnai, Ravi Shankar-sitar, Amjad Ali Khan-sarod, Zakir Hussain-tabla, Shivkumar Sharma-santoor, Chaurasia-flute.",
      "classical-dances",
      "Ustad **Bismillah Khan** was a maestro of —",
      "The **shehnai** — Bharat Ratna 2001."),
    P("Painting / craft ↔ state", "very common",
      "Madhubani, Warli, Pattachitra, Phad or a craft (Bidri, Chikankari) with four states/places.",
      "Big five paintings: Madhubani-Bihar, Warli-Maharashtra, Pattachitra-Odisha, Phad-Rajasthan, Gond-MP. Crafts: Bidriware-Bidar, Chikankari-Lucknow, Phulkari-Punjab, Pochampally-Telangana, Blue pottery-Jaipur.",
      "paintings-crafts",
      "**Warli** painting, with white stick figures on mud walls, is from —",
      "**Maharashtra** — tribal wall art of the Warli belt."),
    P("Festival / fair ↔ state", "very common",
      "Onam, Pongal, Chhath, Hornbill, Bihu or a mela (Pushkar, Sonepur, Kumbh) with state options.",
      "Onam-Kerala, Pongal-TN, Baisakhi-Punjab, Bihu-Assam, Chhath-Bihar, Hornbill-Nagaland (Dec), Losar-Ladakh. Kumbh rotates Prayagraj-Haridwar-Ujjain-Nashik; Pushkar = camels, Sonepur = cattle.",
      "festivals-fairs",
      "The **Onam** harvest festival is celebrated in —",
      "**Kerala** — Mahabali's homecoming, with Vallam Kali boat races."),
    P("UNESCO list / temple builder", "very common",
      "A recent WHS inscription and its state, or a temple (Konark, Brihadeeswara, Belur) with its builder/dynasty.",
      "Recent WHS: 2021 Ramappa-Telangana + Dholavira-Gujarat; 2023 Santiniketan-WB + Hoysala Ensembles-Karnataka; 2024 Moidams-Assam. Builders: Konark-Narasimhadeva I, Thanjavur-Rajaraja I, Belur-Vishnuvardhana, Kailasa-Krishna I.",
      "unesco-institutions",
      "The **Sun Temple at Konark** was built by —",
      "**Narasimhadeva I** of the Eastern Ganga dynasty (13th century)."),
    P("Dance ↔ feature / make-up", "common",
      "A clue described in words — green make-up, tribhanga, raslila, plate balance, chakkars, bamboo — and the dance asked.",
      "Kathakali-green make-up; Odissi-tribhanga; Manipuri-raslila; Kuchipudi-plate (tarangam); Kathak-chakkars; Mohiniyattam-lasya; Sattriya-sattra; Cheraw-bamboo; Hojagiri-balancing.",
      "classical-dances",
      "Balancing on a **brass plate (tarangam)** identifies which classical dance?",
      "**Kuchipudi** (Andhra Pradesh)."),
    P("Book/paper-era institution ↔ year", "common",
      "'Kerala Kalamandalam was founded in', 'Kalakshetra by whom', 'which Akademi and when', 'ASI's first DG'.",
      "Culture bodies: Kalamandalam 1930 (Vallathol), Kalakshetra 1936 (Rukmini Devi), ASI 1861 (Cunningham), Sangeet Natak Akademi 1953, Sahitya + Lalit Kala 1954, FTII 1960 Pune.",
      "unesco-institutions",
      "**Kerala Kalamandalam** was founded in 1930 by —",
      "Poet **Vallathol Narayana Menon**, to revive Kathakali."),
    P("UNESCO ICH element ↔ year / state", "common",
      "An intangible element (Garba, Kalbelia, Durga Puja, Kumbh, Yoga) matched to its inscription year or home state.",
      "The ICH ladder: Kutiyattam 2001, Ramlila + Vedic chanting 2008, Ramman 2009, Chhau + Kalbelia + Mudiyettu 2010, Sankirtana 2013, Yoga 2016, Kumbh 2017, Durga Puja 2021, Garba 2023.",
      "festivals-fairs",
      "**Garba** entered the UNESCO Intangible Cultural Heritage list in —",
      "**2023** — India's newest major dance element on the list."),
]

if __name__ == "__main__":
    subs = [
        ac_part1.build_classical(),
        ac_part1.build_folk(),
        ac_part1.build_music(),
        ac_part2.build_paintings(),
        ac_part2.build_architecture(),
        ac_part2.build_festivals(),
        ac_part2.build_unesco(),
    ]
    apply_topic("art-culture", subs, PYQ)
