"""Phase-2 deep content for ga/ancient-history. Run: py -3 ancient-history.py"""
import os
import sys

sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
from _lib import apply_topic
from anc_part1 import build_indus, build_vedic, build_maha, build_buddh
from anc_part2 import build_mauryan, build_post, build_gupta, build_south, build_lit


def P(pattern, frequency, howToSpot, approach, subtopic, q, sol):
    return {"pattern": pattern, "frequency": frequency, "howToSpot": howToSpot, "approach": approach,
            "subtopic": subtopic, "example": {"q": q, "solution": sol}}


PYQ = [
    P("Harappan site ↔ find matching", "very common",
      "A Harappan city or a find (dockyard, Great Bath, ploughed field, dancing girl, signboard) is named; the matching half is asked.",
      "Hold the one-find-one-site table: Lothal = dockyard, Kalibangan = ploughed field, Chanhudaro = beads, Dholavira = reservoirs + signboard. Watch the near-pairs (ploughed field vs plough model; Bath vs granary).",
      "indus-valley",
      "The Harappan site where a ploughed field has been excavated is:",
      "Kalibangan (Rajasthan, on the Ghaggar) — a field showing criss-cross plough furrows."),
    P("Rigvedic rivers and mandalas", "very common",
      "A Rigvedic river name (Parushni, Vitasta, Asikni) or a mandala fact (Gayatri, Soma, Purusha Sukta) with modern rivers/mandalas as options.",
      "Rivers: Vitasta-Jhelum, Asikni-Chenab, Parushni-Ravi, Vipas-Beas, Sutudri-Sutlej. Mandalas: 3 Gayatri, 7 Ten Kings, 9 Soma, 10 Purusha Sukta. Hymn counts: Indra most, then Agni.",
      "vedic-age",
      "The Rigvedic river **Asikni** is the modern:",
      "Chenab — second in the chain Vitasta, Asikni, Parushni, Vipas, Sutudri = Jhelum, Chenab, Ravi, Beas, Sutlej."),
    P("Buddha's life stations and symbols", "very common",
      "A life event (enlightenment, first sermon, death) with places as options, or a symbol (lotus, horse, tree, wheel, stupa) to match.",
      "Life chain: Lumbini → Bodh Gaya → Sarnath → Kushinagar; symbols in the same order: lotus-bull, horse, Bodhi tree, wheel, stupa.",
      "buddhism-jainism",
      "The symbol associated with the Buddha's first sermon is the:",
      "Wheel (Dharmachakra) — the sermon is called Dharmachakra-pravartana, delivered at Sarnath."),
    P("Councils: place–king–president chains", "very common",
      "'The Second/Third/Fourth Buddhist (or Jain) council was held under…' or matching council to place.",
      "Buddhist: Rajagriha, Vaishali, Pataliputra, Kashmir ↔ Ajatashatru, Kalashoka, Ashoka, Kanishka ↔ Mahakassapa, Sabakami, Moggaliputta Tissa, Vasumitra. Jain: Pataliputra, Vallabhi. Outcomes: 2nd first split, 3rd Abhidhamma, 4th Hinayana-Mahayana.",
      "buddhism-jainism",
      "The Fourth Buddhist Council was presided over by:",
      "Vasumitra (with Ashvaghosha as deputy), held in Kashmir under Kanishka."),
    P("Ashoka's edicts: which edict says what", "very common",
      "'Which edict describes the Kalinga war', where Ashoka's personal name appears, script/language questions, Rummindei pillar.",
      "RE XIII = Kalinga remorse, RE XII = tolerance, Bhabru = Buddha-Dhamma-Sangha, Rummindei = Lumbini + tax cut. Personal name only at Maski/Gujarra/Nettur/Udegolam. Prakrit + Brahmi mostly; Prinsep deciphered Brahmi in 1837.",
      "mauryan-empire",
      "Which of Ashoka's Major Rock Edicts describes the Kalinga war and the king's remorse?",
      "Rock Edict XIII — it also names five Hellenistic kings with whom Ashoka exchanged Dhamma missions."),
    P("Dynasty → ruler → event chains (Magadha and after)", "very common",
      "'Who founded Pataliputra', 'under whom was the Second Council', ordering rulers of Haryanka-Shishunaga-Nanda-Maurya, post-Mauryan foreign dynasties in order.",
      "Magadha chain: Bimbisara (both teachers) → Ajatashatru (1st Council) → Udayin (Pataliputra) → Shishunaga (ends Avanti) → Kalashoka (2nd Council) → Mahapadma Nanda (Ekarat) → Dhana Nanda → Chandragupta Maurya. NW entries: Indo-Greeks → Shakas → Parthians → Kushanas.",
      "mahajanapadas",
      "Who founded Pataliputra at the Ganga–Son confluence?",
      "Udayin, the Haryanka successor of Ajatashatru — Rajagriha was the earlier capital."),
    P("Book ↔ author pairing", "very common",
      "Sanskrit/Pali/Tamil text with authors as options, or a match-the-column across kavyas, dramas, chronicles.",
      "Core pairs: Arthashastra-Kautilya, Mudrarakshasa-Vishakhadatta, Mrichchhakatika-Shudraka, Buddhacharita-Ashvaghosha, Harshacharita-Banabhatta, Rajatarangini-Kalhana, Silappadikaram-Ilango Adigal, Tolkappiyam-Tolkappiyar.",
      "ancient-literature",
      "The Sanskrit play Mrichchhakatika ('The Little Clay Cart') was written by:",
      "Shudraka — a drama about the love of Charudatta and Vasantasena."),
    P("Gupta–Harsha achievements and Chinese travellers", "very common",
      "'Napoleon of India', Prashasti composer, who defeated the Shakas/Huns, traveller-reign matching (Megasthenes, Fa-Hien, Hiuen Tsang, I-tsing).",
      "Chain: Chandragupta I (era 320) → Samudragupta (Prashasti by Harishena) → Chandragupta II (Vikramaditya, Navaratna, Fa-Hien) → Kumaragupta I (Nalanda) → Skandagupta (Huns). Travellers: Megasthenes-Chandragupta Maurya, Deimachus-Bindusara, Fa-Hien-Chandragupta II, Hiuen Tsang-Harsha, I-tsing later.",
      "gupta-harsha",
      "The Prayag Prashasti praising Samudragupta was composed by:",
      "Harishena, the court poet, on the Allahabad pillar."),
    P("Temple style ↔ dynasty ↔ site (south India)", "common",
      "A temple (Shore Temple, Kailasa at Ellora, Durga temple Aihole, Pattadakal group) with dynasties or builders as options; style questions (Dravida-Nagara-Vesara).",
      "Pallavas: Mamallapuram rathas + Shore Temple (Rajasimha), Kailasanatha Kanchi. Chalukyas: Aihole Durga temple, Pattadakal (Vesara), Pulakesin II's Aihole inscription by Ravikirti. Rashtrakuta Krishna I: Kailasa temple Ellora. Dravida = south, Nagara = north, Vesara = Deccan blend.",
      "south-dynasties",
      "The Kailasa temple at Ellora, cut out of a single rock, was built under which dynasty?",
      "The Rashtrakutas — excavated under Krishna I (8th century CE)."),
]

if __name__ == "__main__":
    subs = [build_indus(), build_vedic(), build_maha(), build_buddh(),
            build_mauryan(), build_post(), build_gupta(), build_south(), build_lit()]
    apply_topic("ancient-history", subs, PYQ)
