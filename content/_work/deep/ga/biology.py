"""Phase-2 deep content for ga/biology. Run: py -3 biology.py"""
import os
import sys

sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
from _lib import apply_topic
from bio_part1 import build_cell, build_body, build_nutrition
from bio_part2 import build_diseases, build_plants, build_ecology


def P(pattern, frequency, howToSpot, approach, subtopic, q, sol):
    return {"pattern": pattern, "frequency": frequency, "howToSpot": howToSpot, "approach": approach,
            "subtopic": subtopic, "example": {"q": q, "solution": sol}}


PYQ = [
    P("Vitamin/mineral → deficiency disease", "very common",
      "'Scurvy / rickets / goitre / anaemia is caused by deficiency of…', 'which vitamin is fat-soluble', kwashiorkor vs marasmus, wrong-pair questions on the vitamin table.",
      "Sing the ladder: A–night blindness, B₁–beriberi, B₃–pellagra, B₁₂–pernicious anaemia, C–scurvy, D–rickets, E–sterility, K–clotting. Fat-soluble = A, D, E, K. Minerals: iron–anaemia, iodine–goitre, calcium–bones. Kwashiorkor = protein lack (swollen), marasmus = protein + calories (shrunken).",
      "bio-nutrition",
      "Deficiency of vitamin C causes:",
      "Scurvy — bleeding gums and slow healing. Sailors avoided it with citrus; amla is the richest Indian source."),
    P("Disease → pathogen type / vector", "very common",
      "'Dengue / malaria / TB is caused by or spread by…', 'which of these is a viral disease', 'elephantiasis is transmitted by', odd-one-out among pathogens.",
      "Classify first: bacteria (TB, cholera, typhoid, tetanus, leprosy, plague), virus (dengue, rabies, polio, measles, AIDS), protozoa (malaria, kala-azar, amoebiasis), fungus (ringworm). Vectors: Anopheles–malaria, Aedes–dengue/chikungunya, Culex–elephantiasis, sandfly–kala-azar, tsetse–sleeping sickness, rat flea–plague. Dengue (viral) and malaria (protozoan) both ride mosquitoes but are different microbes — the favourite odd-one-out.",
      "bio-diseases",
      "Which mosquito transmits dengue?",
      "Aedes aegypti — it bites by day and also carries chikungunya and zika. Malaria rides the female Anopheles instead."),
    P("Human body records and functions", "very common",
      "'Largest gland / largest organ / longest bone / smallest bone', 'universal blood donor', 'bile is produced in', 'pace-maker of the heart', 'how many bones in an adult'.",
      "Records: skin largest organ, liver largest gland, thyroid largest endocrine gland, femur longest bone, stapes smallest bone, 206 adult bones. Blood: O− universal donor, AB+ universal recipient, platelets clot, SA node pace-maker. Secretions: liver makes bile (gall bladder stores it, no enzymes), stomach HCl + pepsin, pancreas insulin + trypsin. Pituitary is the master gland; thyroxine needs iodine.",
      "bio-human-body",
      "The smallest bone in the human body is:",
      "Stapes, in the middle ear. The largest gland is the liver and the longest bone the femur — keep the three records separate."),
    P("Scientist → discovery (cell, vaccine, antibiotic)", "very common",
      "'Who discovered penicillin / the cell / the vaccine', 'insulin was discovered by', 'who proved mosquitoes carry malaria', match-the-column of biologists.",
      "Timeline table: Hooke–cell (1665), Leeuwenhoek–living cells, Brown–nucleus, Schleiden + Schwann–cell theory, Virchow–omnis cellula; Jenner–first vaccine (smallpox, 1796), Pasteur–rabies vaccine and pasteurisation, Koch–TB bacterium, Fleming–penicillin (1928), Banting & Best–insulin (1921), Ross–mosquito-malaria link, Mendel–genetics, Watson & Crick–DNA double helix.",
      "bio-cell",
      "Who discovered penicillin?",
      "Alexander Fleming, in 1928, from the mould Penicillium notatum. Koch identified the TB bacterium; Pasteur gave the rabies vaccine."),
    P("Cell organelles and genetics", "very common",
      "'Powerhouse of the cell / suicide bags', 'which organelle makes protein', 'human body cell has how many chromosomes', 'sex of the child is determined by', 'Mendel worked on'.",
      "Nickname pairs: mitochondria–powerhouse, ribosome–protein factory, lysosome–suicide bag, Golgi–post office; mitochondria and chloroplasts have their own DNA. Genetics: 46 chromosomes (23 pairs), meiosis halves to 23 in gametes, XX female / XY male so the father decides sex; Mendel = father of genetics (pea plant), Watson & Crick = DNA double helix.",
      "bio-cell",
      "The sex of a child is determined by:",
      "The father's sperm — it carries either X (girl, XX) or Y (boy, XY); the mother's egg always gives X."),
    P("Branch of study / culture word", "very common",
      "'Ornithology / entomology / sericulture / apiculture is the study or rearing of', 'study of cancer', 'ichthyology', match-the-column of -ology words.",
      "Branches: ornithology–birds, entomology–insects (not etymology!), ichthyology–fish, herpetology–reptiles and amphibians, mycology–fungi, cytology–cells, oncology–cancer, cardiology–heart. Cultures: apiculture–bees, sericulture–silkworms, pisciculture–fish, vermiculture–earthworms, horticulture–gardens. Decode the Latin root when unsure (api-, seri-, pisci-).",
      "bio-branches-ecology",
      "Sericulture is associated with:",
      "Rearing silkworms for silk. Apiculture keeps bees, pisciculture farms fish — root + culture decodes each word."),
    P("Plant hormones, edible parts and classification", "very common",
      "'Which hormone ripens fruit / bends shoots to light', 'potato / carrot / onion is a modified…', 'five-kingdom classification', 'monocot vs dicot', 'xylem carries…'.",
      "Hormones: auxin–elongation and phototropism, gibberellin–stem growth, cytokinin–cell division, ethylene–fruit ripening, abscisic acid–stress. Edible parts: carrot–root, potato/ginger/onion–stem, cabbage–leaf, cauliflower–flower, tomato–fruit, groundnut–seed. Classification: Linnaeus–binomial, Whittaker–5 kingdoms, bacteria in Monera; monocot one cotyledon + parallel veins, dicot two + reticulate; xylem water up, phloem food.",
      "bio-plants-classification",
      "Which plant hormone is a gas that ripens fruit?",
      "Ethylene — a ripe banana releases it and ripens neighbouring fruit. Auxin bends shoots toward light; ABA closes stomata under stress."),
    P("Scientific names", "common",
      "'The scientific name of mango / neem / rice / tiger', 'in binomial nomenclature the first word is', italics and capitalisation rules.",
      "Binomial = Genus (capital) + species (small), both italics. Mango Mangifera indica, neem Azadirachta indica, banyan Ficus benghalensis, tamarind Tamarindus indica, potato Solanum tuberosum, rice Oryza sativa, tiger Panthera tigris, frog Rana tigrina. Watch the two *-indica* pairings: mango and neem share the species name, not the genus.",
      "bio-plants-classification",
      "In Mangifera indica, the word Mangifera denotes the:",
      "Genus — the first, capitalised word; indica is the species. The binomial system is Linnaeus's."),
]

if __name__ == "__main__":
    subs = [build_cell(), build_body(), build_nutrition(), build_diseases(), build_plants(), build_ecology()]
    apply_topic("biology", subs, PYQ)
