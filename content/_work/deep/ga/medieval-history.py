"""Phase-2 deep content for ga/medieval-history. Run: py -3 medieval-history.py"""
import os
import sys

sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
from _lib import apply_topic
from med_part1 import build_early, build_sultanate, build_vijaya, build_mughals
from med_part2 import build_maratha, build_bhakti, build_sources


def P(pattern, frequency, howToSpot, approach, subtopic, q, sol):
    return {"pattern": pattern, "frequency": frequency, "howToSpot": howToSpot, "approach": approach,
            "subtopic": subtopic, "example": {"q": q, "solution": sol}}


PYQ = [
    P("Delhi Sultanate: sultan ↔ reform or act", "very common",
      "'Which sultan introduced the tanka', market reforms, iqta, experiments of MBT, welfare works of Firoz Shah.",
      "Map every reform to its sultan: Iltutmish (tanka-jital, Forty), Balban (sijda-paibos), Alauddin (markets, chehra-daag, Siri), MBT (Daulatabad, token currency), Firoz Shah (canals, jizya on Brahmanas). Check dynasty order when an option mixes reigns.",
      "delhi-sultanate",
      "Which Delhi Sultan introduced the silver tanka and copper jital?",
      "Iltutmish — the currency reform of the Slave dynasty's consolidator."),
    P("Mughal rulers ↔ battles, orders and monuments", "very common",
      "Panipat-Khanwa-Chausa chain, Akbar's administration, Roe's embassy, Taj/Peacock Throne, Aurangzeb's acts.",
      "Battles: Panipat 1526 (Babur-Lodi), Khanwa 1527 (Babur-Rana Sanga), Chausa/Kannauj 1539-40 (Sher Shah-Humayun), 2nd Panipat 1556 (Akbar-Hemu). Reforms: Todar Mal's dahsala, zat-sawar. Monuments: Taj (Shah Jahan-Mumtaz), Peacock Throne. Aurangzeb: jizya 1679, Tegh Bahadur 1675.",
      "mughals",
      "In the Battle of Haldighati (1576), the Mughal army was commanded by:",
      "Raja Man Singh (of Amber), fighting Maharana Pratap."),
    P("Bhakti-Sufi saints ↔ sect, work and language", "very common",
      "Saint-work-language triple matching (Tulsidas-Awadhi, Kabir-Bijak, Khusrau-Nizamuddin), silsila identification.",
      "Anchors: Kabir-Bijak, Tulsidas-Ramcharitmanas (Awadhi), Tukaram-abhangas (Marathi, Varkari), Chaitanya-Bengal, Khusrau-Persian (Nizamuddin's disciple). Silsilas: Chishti (Moinuddin-Ajmer, Nizamuddin-Delhi), Suhrawardi (Bahauddin Zakariya-Multan).",
      "bhakti-sufi",
      "Amir Khusrau, the 'Parrot of India', was a disciple of which Sufi saint?",
      "Nizamuddin Auliya of the Chishti order (Delhi)."),
    P("Traveller ↔ ruler/court matching", "very common",
      "'Who came from Morocco', which court a traveller saw, order of visits, books like Rihla and Si-yu-ki.",
      "Ladder: Marco Polo-Pandya, Ibn Battuta-MBT (Rihla), Conti-Vijayanagara (Deva Raya I), Razzaq-Deva Raya II, Nikitin-Bahmani, Paes-Krishnadevaraya, Fitch-Akbar, Roe-Jahangir, Tavernier-Bernier-later Mughals.",
      "sources-travellers",
      "Which traveller–ruler pair is NOT correctly matched?",
      "Test each pair against the ladder; the mismatched one (e.g. pairing Ibn Battuta with a Vijayanagara king) is the answer."),
    P("Sikh Gurus in order and Khalsa facts", "common",
      "'Who compiled the Adi Granth', birthplace of Nanak, Khalsa 1699, execution years of Arjan and Tegh Bahadur.",
      "Chain: Nanak (Talwandi) → Angad (Gurmukhi) → ... → Arjan (Adi Granth, 1606) → Hargobind (Miri-Piri) → Tegh Bahadur (1675) → Gobind Singh (Khalsa, Baisakhi 1699, Anandpur; Granth as Guru).",
      "marathas-sikhs",
      "The Khalsa was founded at Anandpur Sahib in 1699 by:",
      "Guru Gobind Singh, the tenth Guru, on Baisakhi day."),
    P("Chola rulers ↔ achievements (navy, temples, Uttaramerur)", "very common",
      "'Gangaikonda' title, Brihadeshwara builder, Srivijaya expedition, kudavolai village elections.",
      "Vijayalaya (founder, 850) → Rajaraja I (Brihadeshwara Thanjavur) → Rajendra I (Gangaikondacholapuram, navy vs Srivijaya). Uttaramerur inscriptions (Parantaka I) = kudavolai elections, variyam committees, ur-sabha-nagaram.",
      "early-medieval",
      "Which Chola ruler sent a naval expedition against Srivijaya?",
      "Rajendra I — to protect the China trade route."),
    P("Vijayanagara ↔ Bahmani: founders, dynasties, five sultanates", "common",
      "Founders and dates (1336 Hampi, 1347 Gulbarga), Krishnadevaraya's court, five sultanates and their houses, Talikota 1565.",
      "Vijayanagara: Harihara-Bukka (Sangama) → Saluva → Tuluva (Krishnadevaraya) → Aravidu (Rama Raya). Bahmani: Hasan Gangu; heirs Bijapur (Adil Shahi), Ahmadnagar (Nizam Shahi), Golconda (Qutb Shahi), Berar (Imad Shahi), Bidar (Barid Shahi). Talikota 1565 ends the empire.",
      "vijayanagara-bahmani",
      "The Battle of Talikota (1565) was fought between Vijayanagara and:",
      "A coalition of the five Deccan sultanates; Rama Raya was executed after the defeat."),
    P("Maratha administration and the confederacy", "common",
      "Ashtapradhan portfolios, Peshwa line, confederacy house ↔ seat, Anglo-Maratha war treaties.",
      "Ashtapradhan: Peshwa (prime), Sumant (foreign), Amatya (finance), Senapati (army). Peshwas: Balaji Vishwanath → Baji Rao I → Balaji Baji Rao. Houses: Scindia-Gwalior, Holkar-Indore, Gaekwad-Baroda, Bhonsle-Nagpur. Salbai 1782 ends 1st war; Bassein 1802 begins 2nd.",
      "marathas-sikhs",
      "In Shivaji's Ashtapradhan, the minister in charge of foreign affairs was the:",
      "Sumant (also called Dabir) — the Peshwa headed the council as prime minister."),
]

if __name__ == "__main__":
    subs = [build_early(), build_sultanate(), build_vijaya(), build_mughals(),
            build_maratha(), build_bhakti(), build_sources()]
    apply_topic("medieval-history", subs, PYQ)
