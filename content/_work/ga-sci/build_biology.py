# -*- coding: utf-8 -*-
"""Builds content/ssc-cgl/topics/ga/biology.json. Run: py -3 build_biology.py"""
from scicommon import Q, save_topic, place

C_CELL = """### Discoveries about the cell
| Discovery | Scientist |
|---|---|
| Cell (in cork, 1665) | **Robert Hooke** |
| First living cells, bacteria (single-lens microscope) | **Antonie van Leeuwenhoek** |
| **Nucleus** (1831) | **Robert Brown** |
| **Cell theory** | **Schleiden** (plants) and **Schwann** (animals) |
| 'Omnis cellula e cellula' — new cells come from existing cells | **Rudolf Virchow** |

### Cell organelles
| Organelle | Function / nickname |
|---|---|
| **Mitochondria** | **Powerhouse of the cell** — aerobic respiration, ATP; have their own DNA |
| **Ribosomes** | **Protein synthesis** (no membrane) |
| **Lysosomes** | **'Suicide bags'** — digestive enzymes |
| **Golgi apparatus** | Packaging and secretion |
| **Endoplasmic reticulum** | Transport; rough ER (with ribosomes) makes proteins, smooth ER makes lipids |
| **Chloroplast** | **Photosynthesis** (plants only); has its own DNA |
| **Nucleus** | Control centre; holds chromosomes (DNA) |
| **Vacuole** | Storage; large in plant cells |
| **Cell wall** | Plants (**cellulose**), fungi (**chitin**) — absent in animal cells |

- **Prokaryotes** (bacteria, blue-green algae) have **no nuclear membrane** and no membrane-bound organelles. **Eukaryotes** have a true nucleus.
- Largest cell: **ostrich egg**. Longest cell: **nerve cell (neuron)**. Smallest cell: **Mycoplasma (PPLO)**. Mature mammalian **RBCs have no nucleus**.
- **Mitosis** — body growth and repair, gives **2 identical** cells. **Meiosis** — forms **gametes**, halves the chromosome number (4 cells).

### Genetics
- **Gregor Mendel** — **father of genetics**; experiments on **garden pea** (Pisum sativum); laws of dominance, segregation and independent assortment.
- **DNA double helix** — **Watson and Crick (1953)**, using X-ray data of Rosalind Franklin and Maurice Wilkins. DNA bases: A, T, G, C (RNA has **uracil** instead of thymine).
- Humans have **46 chromosomes (23 pairs)** in body cells: 22 pairs of autosomes + 1 pair of sex chromosomes. Gametes have 23.
- **Sex of the child is decided by the father**: XX = female, XY = male.
- **Haemophilia** and **colour blindness** are **X-linked** disorders — more common in males. **Down syndrome** — an extra chromosome 21 (trisomy 21).
- **Hugo de Vries** — mutation theory. **Darwin** — natural selection (*On the Origin of Species*, 1859). **Lamarck** — inheritance of acquired characters.
- **Har Gobind Khorana** — Nobel Prize 1968 for work on the genetic code.
"""

C_BODY = """### Record-holders of the human body
| Fact | Answer |
|---|---|
| Largest organ | **Skin** |
| Largest gland / largest internal organ | **Liver** |
| Longest bone | **Femur** (thigh bone) |
| Smallest bone | **Stapes** (middle ear) |
| Bones in an adult | **206** (about 300 at birth; many fuse) |
| Strongest/hardest substance | **Tooth enamel** |
| Master gland | **Pituitary** |
| Largest part of the brain | **Cerebrum** |
| Functional unit of the kidney | **Nephron** |
| Structural and functional unit of the nervous system | **Neuron** |
| Normal body temperature | **37 °C (98.6 °F)** |
| Normal blood pressure | About **120/80 mm Hg** |
| Normal resting heart rate | About **72 beats per minute** |

### Blood and circulation
- **William Harvey** described the circulation of blood.
- **RBCs** carry oxygen with **haemoglobin (iron-containing)**, live about **120 days**, are made in **red bone marrow**; the **spleen** is the 'graveyard of RBCs'. **WBCs** fight infection (immunity). **Platelets** help **clotting**.
- Blood groups — **Karl Landsteiner** (ABO). **O** is the **universal donor** (O negative, strictly) and **AB** the **universal recipient** (AB positive, strictly). The **Rh factor** was also found by Landsteiner and Wiener (named after the rhesus monkey).
- The human **heart** has **4 chambers**; the **SA node** is the natural **pacemaker**. Arteries carry blood **away** from the heart (all oxygenated except the pulmonary artery); veins carry blood **to** the heart (all deoxygenated except the pulmonary vein).

### Digestion
| Where | Secretion / enzyme | Action |
|---|---|---|
| Mouth | **Salivary amylase (ptyalin)** | Starch → maltose |
| Stomach | **HCl + pepsin** | Kills germs; proteins → peptides |
| Liver | **Bile** (stored in the **gall bladder**) | **Emulsifies fats** — contains no enzyme |
| Pancreas | Trypsin, lipase, amylase | Proteins, fats, starch |
| Small intestine | Villi | Most **absorption** of digested food |
| Large intestine | — | Absorbs **water** |

- The **small intestine** is the longest part of the alimentary canal.

### Nervous and endocrine systems
- **Cerebrum** — intelligence, memory, voluntary actions. **Cerebellum** — **balance and coordination**. **Medulla oblongata** — involuntary actions (**heartbeat, breathing**, swallowing).

| Gland | Hormone | Note |
|---|---|---|
| **Pituitary** | Growth hormone and others | 'Master gland' |
| **Thyroid** | **Thyroxine** (needs iodine) | Deficiency → goitre |
| **Pancreas** (islets of Langerhans) | **Insulin** (β-cells), glucagon (α-cells) | Insulin **lowers blood sugar**; lack → **diabetes mellitus** |
| **Adrenal** | **Adrenaline** | 'Fight or flight' hormone |
| **Testes / ovaries** | Testosterone / oestrogen, progesterone | Sex hormones |

- The **pancreas** is both an endocrine and an exocrine gland. Insulin was isolated by **Banting and Best** (1921).
- In the **eye**, the **retina** holds the image; the **cornea** is what is donated in eye donation.
- The **lungs'** air sacs (**alveoli**) are the site of gas exchange.
"""

C_NUTRITION = """### Vitamins
| Vitamin | Chemical name | Deficiency disease | Sources |
|---|---|---|---|
| **A** | Retinol | **Night blindness**, xerophthalmia | Carrot, milk, fish-liver oil |
| **B1** | **Thiamine** | **Beriberi** | Whole grains |
| **B2** | Riboflavin | Cracked lips and mouth corners | Milk, eggs |
| **B3** | Niacin | **Pellagra** (the '3 D's' — dermatitis, diarrhoea, dementia) | Groundnut, meat |
| **B9** | Folic acid | Anaemia | Green leafy vegetables |
| **B12** | **Cobalamin** (contains **cobalt**) | **Pernicious anaemia** | Animal foods |
| **C** | **Ascorbic acid** | **Scurvy** (bleeding gums) | **Amla**, citrus fruits |
| **D** | **Calciferol** | **Rickets** (children), osteomalacia (adults) | **Sunlight**, fish oil |
| **E** | **Tocopherol** | Reproductive problems/sterility; an **antioxidant** | Vegetable oils, nuts |
| **K** | Phylloquinone | **Blood does not clot** (haemorrhage) | Green leafy vegetables |

- **Fat-soluble: A, D, E, K**. **Water-soluble: B-complex and C** (not stored; C is destroyed by heating).
- Vitamin D is made in the **skin in sunlight**. The word 'vitamine' was coined by **Casimir Funk**.

### Minerals
| Mineral | Role / deficiency |
|---|---|
| **Iron** | Haemoglobin; deficiency → **anaemia** |
| **Iodine** | Thyroxine; deficiency → **goitre** |
| **Calcium, phosphorus** | Bones and teeth |
| **Sodium, potassium** | Nerve impulses, fluid balance |
| **Fluorine** | Tooth enamel (excess → fluorosis) |

### Macronutrients
- Energy per gram: **fat about 9 kcal**, carbohydrate about 4 kcal, protein about 4 kcal.
- **Proteins** are 'body-building' foods; **carbohydrates** are the main energy source; **roughage (fibre)** helps bowel movement.
- **Kwashiorkor** — protein deficiency (swollen belly); **marasmus** — deficiency of both protein and calories.
"""

C_DISEASES = """### Diseases by pathogen
| Pathogen | Diseases |
|---|---|
| **Bacteria** | **Tuberculosis**, **cholera**, **typhoid**, **diphtheria**, **tetanus**, **whooping cough** (pertussis), **leprosy**, **plague**, bacterial pneumonia |
| **Viruses** | **AIDS (HIV)**, **polio**, **measles**, mumps, **chickenpox**, **smallpox**, **rabies**, hepatitis, influenza, **dengue**, chikungunya, common cold, COVID-19 |
| **Protozoa** | **Malaria** (*Plasmodium*), **kala-azar** (*Leishmania*), amoebic dysentery (*Entamoeba*), sleeping sickness (*Trypanosoma*) |
| **Fungi** | **Ringworm**, athlete's foot |
| **Worms (helminths)** | **Filariasis / elephantiasis** (*Wuchereria*), ascariasis |

### Vectors
| Vector | Disease(s) |
|---|---|
| **Female Anopheles** mosquito | **Malaria** |
| **Aedes** mosquito (*A. aegypti*) | **Dengue**, **chikungunya**, yellow fever, Zika |
| **Culex** mosquito | **Filariasis**, Japanese encephalitis |
| **Rat flea** | **Plague** |
| **Sandfly** | **Kala-azar** |
| **Tsetse fly** | **Sleeping sickness** |
| Housefly | Carries germs of cholera, typhoid (mechanically) |

- **Rabies** (hydrophobia) spreads through the bite of an infected dog or other mammal.

### Vaccines, drugs and discoverers
| Discovery | Scientist |
|---|---|
| **Smallpox vaccine** (1796) — first vaccine | **Edward Jenner** |
| **Rabies vaccine**, pasteurisation, germ theory | **Louis Pasteur** |
| **TB bacterium** (1882), cholera bacterium | **Robert Koch** |
| **Penicillin** (1928) — first antibiotic | **Alexander Fleming** |
| Injectable (killed) **polio vaccine** | **Jonas Salk** |
| **Oral polio vaccine** | **Albert Sabin** |
| Malaria is spread by mosquitoes (Nobel 1902) | **Ronald Ross** |
| Blood groups | **Karl Landsteiner** |
| First human heart transplant (1967) | **Christiaan Barnard** |

- **BCG** — tuberculosis; **DPT** — diphtheria, pertussis, tetanus; **MMR** — measles, mumps, rubella.
- **Smallpox** was declared **eradicated** by WHO in **1980**. India was certified **polio-free** in **2014**.
- Diagnostic tests: **Widal — typhoid**, **ELISA — HIV/AIDS**, **Mantoux — tuberculosis**.
- **Antibiotics act on bacteria, not on viruses.**
- Non-communicable: diabetes, hypertension, cancer (**leukaemia** = blood cancer). **Jaundice** affects the **liver**; **conjunctivitis** — eyes; **glaucoma** / **cataract** — eyes; **arthritis** — joints.
"""

C_PLANTS = """### Classification
- **Carolus Linnaeus** — **father of taxonomy**; **binomial nomenclature** (genus + species, e.g. *Homo sapiens*).
- **R.H. Whittaker (1969)** — **five-kingdom** classification: **Monera** (bacteria), **Protista**, **Fungi**, **Plantae**, **Animalia**.
- Viruses are not placed in these kingdoms; they are 'living' only inside a host cell.

### Scientific names (frequently asked)
| Organism | Scientific name |
|---|---|
| Human | *Homo sapiens* |
| Mango | *Mangifera indica* |
| Tiger / Lion | *Panthera tigris* / *Panthera leo* |
| Peacock | *Pavo cristatus* |
| Neem | *Azadirachta indica* |
| Rice / Wheat | *Oryza sativa* / *Triticum aestivum* |
| Potato | *Solanum tuberosum* |
| Pea | *Pisum sativum* |
| Onion | *Allium cepa* |
| Banyan | *Ficus benghalensis* |
| Housefly | *Musca domestica* |

### Plant physiology
- **Photosynthesis** occurs in **chloroplasts** using **chlorophyll**; the **oxygen released comes from water**.
- **Xylem** carries **water and minerals** upward; **phloem** carries **food** (translocation).
- **Transpiration** — loss of water through **stomata**.
- **Nitrogen fixation** — **Rhizobium** bacteria in the **root nodules of legumes** (pulses); blue-green algae (e.g. *Anabaena*) in paddy fields.
- **Insectivorous plants**: **pitcher plant** (*Nepenthes*), Venus flytrap, sundew — they grow in nitrogen-poor soil. **Parasite**: *Cuscuta* (amarbel).

### Plant hormones
| Hormone | Main role |
|---|---|
| **Auxin** | Cell elongation, apical dominance, phototropism, rooting |
| **Gibberellin** | Stem elongation, seed germination, fruit size |
| **Cytokinin** | **Cell division**, delays ageing of leaves |
| **Abscisic acid (ABA)** | **'Stress hormone'** — dormancy, **closes stomata**, leaf fall |
| **Ethylene** | **Fruit ripening** (the only **gaseous** hormone) |

### Edible parts
| Plant | Edible part |
|---|---|
| **Potato** | **Stem** (tuber) |
| **Ginger, turmeric** | **Stem** (rhizome) |
| Onion | Bulb (fleshy leaf bases on a short stem) |
| **Carrot, radish, sweet potato, beetroot** | **Root** |
| **Cauliflower** | **Inflorescence** (flower) |
| **Apple** | **Thalamus** (false fruit) |
| **Mango** | Mesocarp |
| **Coconut** | **Endosperm** |
| Spinach, cabbage | Leaves |

### Animal facts
- Largest animal: **blue whale**. Largest bird: **ostrich**. Egg-laying mammals: **platypus, echidna**. The only mammal that truly flies: **bat**.
- Whales, dolphins and bats are **mammals**; fish breathe with **gills**; frogs are **amphibians**.
- **Cold-blooded**: fish, amphibians, reptiles. **Warm-blooded**: birds, mammals.
- Insects have **6 legs**; spiders have **8** (arachnids, not insects). The **earthworm** is the 'farmer's friend'.
"""

C_BRANCHES = """### Branches of study (-ologies)
| Branch | Study of | Branch | Study of |
|---|---|---|---|
| **Ornithology** | **Birds** | **Entomology** | **Insects** |
| **Ichthyology** | **Fish** | **Herpetology** | Reptiles and amphibians |
| **Mycology** | **Fungi** | **Phycology** | **Algae** |
| **Cytology** | Cells | **Histology** | Tissues |
| **Genetics** | Heredity | **Taxonomy** | Classification |
| **Palaeontology** | Fossils | **Anthropology** | Humans / human cultures |
| **Pathology** | Diseases | **Virology** | Viruses |
| **Cardiology** | Heart | **Nephrology** | Kidneys |
| **Dermatology** | Skin | **Haematology** | Blood |
| **Oncology** | **Cancer** | **Ophthalmology** | Eyes |
| **Osteology** | Bones | **Neurology** | Nervous system |
| **Pomology** | **Fruits** | **Olericulture** | Vegetables |
| **Floriculture** | Flowers | **Horticulture** | Garden crops |

### Culture / rearing
| Term | Rearing of |
|---|---|
| **Apiculture** | **Honey bees** |
| **Sericulture** | **Silkworms** (silk) |
| **Pisciculture** | **Fish** |
| **Viticulture** | **Grapes** |
| **Lac culture** | Lac insects |

### Ecology
- 'Ecology' was coined by **Ernst Haeckel**; 'ecosystem' by **A.G. Tansley (1935)**.
- A **food chain** runs: **producers** (green plants) → **primary consumers** (herbivores) → secondary consumers → tertiary consumers. **Decomposers** (bacteria, fungi) recycle nutrients.
- **10% law (Lindeman)**: only about **10% of energy** passes to the next trophic level; the rest is lost mostly as heat. Hence food chains are short (usually 3–5 levels).
- The **pyramid of energy is always upright**; the pyramid of biomass in a pond can be inverted.
- **Biomagnification** — non-degradable chemicals like **DDT** and mercury **increase in concentration** at higher trophic levels.
- The flow of energy is **one-way**; nutrients **cycle**.
"""

SUBTOPICS = [
    {
        "id": "bio-cell",
        "title": "Cell, organelles and genetics",
        "concept": C_CELL,
        "formulas": [],
        "tricks": [
            {
                "title": "Organelle nicknames: 'Power-Mito, Suicide-Lyso, Protein-Ribo, Packing-Golgi'",
                "body": "These four nicknames answer most organelle questions.",
                "example": {"q": "Which organelle is called the 'suicide bag' of the cell?", "solution": "Lysosome."},
            },
            {
                "title": "Cell discoverers in order",
                "body": "**Hooke** saw it (1665, dead cork) → **Leeuwenhoek** saw it alive → **Brown** saw the nucleus → **Schleiden–Schwann** made the theory → **Virchow** said cells come from cells.",
                "example": None,
            },
        ],
        "mistakes": [
            "Saying Leeuwenhoek discovered the cell — Hooke coined the term; Leeuwenhoek first saw living cells.",
            "Saying the mother decides the child's sex — the father's X or Y sperm does.",
            "Giving animal cells a cell wall — only plants, fungi and bacteria have one.",
        ],
    },
    {
        "id": "bio-human-body",
        "title": "Human body — organs, blood, digestion, glands",
        "concept": C_BODY,
        "formulas": [
            {"name": "Body mass index", "tex": r"\text{BMI} = \frac{\text{mass (kg)}}{\text{height (m)}^{2}}", "note": "18.5–24.9 is the normal range (WHO)"},
        ],
        "tricks": [
            {
                "title": "Blood group giving: 'O gives, AB takes'",
                "body": "**O** has no A/B antigens → can **give** to all. **AB** has no anti-A/anti-B antibodies → can **take** from all.",
                "example": {"q": "The universal recipient blood group is?", "solution": "AB."},
            },
            {
                "title": "Brain parts: 'Cerebrum thinks, Cerebellum balances, Medulla keeps you alive'",
                "body": "Thinking/memory — cerebrum; balance/posture — cerebellum; heartbeat/breathing — medulla oblongata.",
                "example": None,
            },
        ],
        "mistakes": [
            "Saying bile contains digestive enzymes — it only emulsifies fats.",
            "Answering thyroid for the master gland — it is the pituitary.",
            "Naming the heart or liver as the largest organ — skin is the largest organ; liver is the largest gland/internal organ.",
        ],
    },
    {
        "id": "bio-nutrition",
        "title": "Vitamins, minerals and nutrition",
        "concept": C_NUTRITION,
        "formulas": [],
        "tricks": [
            {
                "title": "Fat-soluble vitamins: 'KADE' (or 'ADEK')",
                "body": "A, D, E, K dissolve in fat and are stored in the body; B and C dissolve in water.",
                "example": None,
            },
            {
                "title": "Deficiency pairs: 'A-Andha (night blind), B1-Beriberi, C-sCurvy, D-Deformed bones (rickets), K-Klotting'",
                "body": "Add **B3 — Pellagra** ('3 D's) and **B12 — Pernicious anaemia** (cobalt).",
                "example": {"q": "Deficiency of which vitamin causes beriberi?", "solution": "Vitamin B1 (thiamine)."},
            },
        ],
        "mistakes": [
            "Linking scurvy to vitamin D — scurvy is vitamin C; rickets is vitamin D.",
            "Calling vitamin C fat-soluble — it is water-soluble and destroyed by cooking heat.",
            "Mixing up kwashiorkor (protein only) and marasmus (protein + calories).",
        ],
    },
    {
        "id": "bio-diseases",
        "title": "Diseases, pathogens, vectors and vaccines",
        "concept": C_DISEASES,
        "formulas": [],
        "tricks": [
            {
                "title": "Bacterial diseases: 'TB, Cholera, Typhoid, Diphtheria, Tetanus, Leprosy, Plague, Pertussis'",
                "body": "If the disease is in this list it is bacterial; the rest of the common ones (polio, measles, AIDS, dengue, rabies, chickenpox, hepatitis) are viral. Malaria and kala-azar are protozoan.",
                "example": {"q": "Which of these is a viral disease: typhoid, cholera, measles, tetanus?", "solution": "Measles."},
            },
            {
                "title": "Mosquito map: 'Anopheles-Malaria, Aedes-Dengue, Culex-Filaria'",
                "body": "**A**edes also spreads chikungunya, yellow fever and Zika (day-biting). Only the **female** mosquito bites for blood.",
                "example": None,
            },
        ],
        "mistakes": [
            "Calling malaria a bacterial or viral disease — it is protozoan (Plasmodium).",
            "Crediting Pasteur with the smallpox vaccine — that was Jenner; Pasteur made the rabies vaccine.",
            "Thinking antibiotics cure viral infections — they act only on bacteria.",
        ],
    },
    {
        "id": "bio-plants-classification",
        "title": "Classification, plants, hormones and animal facts",
        "concept": C_PLANTS,
        "formulas": [
            {"name": "Photosynthesis", "tex": r"6CO_2 + 6H_2O \xrightarrow[\text{chlorophyll}]{\text{sunlight}} C_6H_{12}O_6 + 6O_2", "note": "O₂ comes from water"},
            {"name": "Aerobic respiration", "tex": r"C_6H_{12}O_6 + 6O_2 \rightarrow 6CO_2 + 6H_2O + \text{energy (ATP)}", "note": ""},
        ],
        "tricks": [
            {
                "title": "Underground but not a root",
                "body": "**Potato, ginger, turmeric, onion** grow underground but are **stems** (they have nodes/buds or 'eyes'). **Carrot, radish, sweet potato, beetroot** are true **roots**.",
                "example": {"q": "The edible part of ginger is?", "solution": "A modified stem (rhizome)."},
            },
            {
                "title": "Five kingdoms: 'My Pet Fish Plays Alone'",
                "body": "**M**onera, **P**rotista, **F**ungi, **P**lantae, **A**nimalia — Whittaker, 1969.",
                "example": None,
            },
        ],
        "mistakes": [
            "Calling sweet potato a stem and potato a root — it is the other way round.",
            "Saying the oxygen from photosynthesis comes from CO₂ — it comes from water.",
            "Calling the bat a bird or the whale a fish — both are mammals.",
        ],
    },
    {
        "id": "bio-branches-ecology",
        "title": "Branches of biology and ecology",
        "concept": C_BRANCHES,
        "formulas": [
            {"name": "10% law of energy transfer", "tex": r"E_{n} = E_{1} \times (0.1)^{\,n-1}", "note": "E₁ = energy at the producer level, n = trophic level"},
        ],
        "tricks": [
            {
                "title": "Culture words by root",
                "body": "**Api** = bee (apiary), **Seri** = silk, **Pisci** = fish (Pisces), **Viti** = vine/grapes, **Pomo** = fruit (pomegranate), **Olera** = vegetables.",
                "example": {"q": "Sericulture is the rearing of?", "solution": "Silkworms."},
            },
            {
                "title": "Study-of roots",
                "body": "**Ornitho** = bird, **Ento** = insect, **Ichthyo** = fish, **Herpeto** = creeping animals, **Myco** = fungus, **Phyco** = seaweed/algae, **Onco** = tumour, **Nephro** = kidney.",
                "example": None,
            },
        ],
        "mistakes": [
            "Confusing entomology (insects) with etymology (word origins).",
            "Mixing up pisciculture (fish) and pomology (fruits).",
            "Saying energy cycles in an ecosystem — it flows one way; nutrients cycle.",
        ],
    },
]

PYQ = [
    {"pattern": "Vitamin/mineral → deficiency disease", "frequency": "very common", "howToSpot": "'Deficiency of vitamin __ causes...', 'Chemical name of vitamin C...'", "approach": "Vitamin table with chemical names; ADEK fat-soluble."},
    {"pattern": "Disease → pathogen type / vector", "frequency": "very common", "howToSpot": "'Which is a bacterial disease?', 'Dengue is spread by...'", "approach": "Bacterial list trick; mosquito map."},
    {"pattern": "Human body records and functions", "frequency": "very common", "howToSpot": "'Largest gland', 'Smallest bone', 'Insulin is secreted by...'", "approach": "Body records table; gland–hormone table."},
    {"pattern": "Scientist → discovery (cell, vaccine, antibiotic)", "frequency": "common", "howToSpot": "'Penicillin was discovered by...', 'Who discovered the cell?'", "approach": "Discoverer tables in cell and disease subtopics."},
    {"pattern": "Cell organelles and genetics", "frequency": "common", "howToSpot": "'Powerhouse of the cell', 'Number of chromosomes in humans'", "approach": "Organelle nicknames; 46 chromosomes; father decides sex."},
    {"pattern": "Branch of study / culture word", "frequency": "common", "howToSpot": "'Ornithology is the study of...', 'Apiculture is...'", "approach": "Decode the Greek/Latin root."},
    {"pattern": "Plant hormones, edible parts and classification", "frequency": "common", "howToSpot": "'Hormone for fruit ripening', 'Edible part of potato', 'Five-kingdom classification'", "approach": "Hormone table; underground-stem trick; Whittaker 1969."},
    {"pattern": "Scientific names", "frequency": "occasional", "howToSpot": "'Scientific name of mango/neem/tiger'", "approach": "Learn the short table; genus is capitalised, species lowercase."},
]

SOLVED = [
    Q("bio-ex01",
      "Deficiency of vitamin C causes:",
      ["Rickets", "Scurvy", "Beriberi", "Night blindness"],
      1,
      "Vitamin C (**ascorbic acid**) is needed to make collagen; its deficiency causes **scurvy** — bleeding and swollen gums, slow wound healing. Rickets is vitamin D, beriberi is B1 and night blindness is A.",
      "C → sCurvy.",
      "easy", "bio-nutrition", "vitamin → deficiency", 15),
    Q("bio-ex02",
      "Which blood group is known as the universal donor?",
      ["A", "B", "AB", "O"],
      3,
      "Group **O** red cells carry **no A or B antigens**, so they are not attacked by the recipient's anti-A or anti-B antibodies — **O is the universal donor** (strictly O negative). **AB** is the universal recipient.",
      "O gives, AB takes.",
      "easy", "bio-human-body", "blood group", 15),
    Q("bio-ex03",
      "Malaria is caused by:",
      ["A bacterium", "A virus", "A protozoan", "A fungus"],
      2,
      "Malaria is caused by the **protozoan *Plasmodium*** and spread by the bite of an infected **female Anopheles** mosquito. Ronald Ross proved the mosquito link (Nobel 1902).",
      "Malaria and kala-azar → protozoa.",
      "easy", "bio-diseases", "disease → pathogen", 15),
    Q("bio-ex04",
      "The edible part of the potato is a:",
      ["Root", "Stem", "Leaf", "Fruit"],
      1,
      "The potato is a **tuber — a modified underground stem**. Its 'eyes' are buds at nodes, which roots do not have. Sweet potato, by contrast, is a modified root.",
      "Eyes/buds → stem.",
      "easy", "bio-plants-classification", "edible part", 15),
]

PRACTICE = [
    Q("bio-q01",
      "Which organelle is known as the 'powerhouse of the cell'?",
      ["Ribosome", "Mitochondria", "Golgi apparatus", "Lysosome"],
      1,
      "**Mitochondria** carry out aerobic respiration and produce **ATP**, the cell's energy currency — hence 'powerhouse'. Ribosomes make proteins and lysosomes are the 'suicide bags'.",
      None, "easy", "bio-cell", "organelle function", 15),
    Q("bio-q02",
      "Who first discovered the cell, in 1665?",
      ["Robert Brown", "Robert Hooke", "Antonie van Leeuwenhoek", "Rudolf Virchow"],
      1,
      "**Robert Hooke** observed box-like compartments in a thin slice of **cork** in 1665 and called them 'cells'. Robert Brown discovered the nucleus (1831) and Leeuwenhoek first saw living cells.",
      None, "easy", "bio-cell", "scientist → discovery", 15),
    Q("bio-q03",
      "In a food chain, producers trap 10,000 J of energy. According to the 10% law, how much energy reaches the secondary consumers?",
      ["1,000 J", "100 J", "10 J", "10,000 J"],
      1,
      "Only about **10%** passes to each next level: producers 10,000 J → primary consumers 1,000 J → **secondary consumers 100 J**.",
      "Two steps up = divide by 100.", "medium", "bio-branches-ecology", "10% law numerical", 25),
    Q("bio-q04",
      "Which is the largest gland in the human body?",
      ["Pancreas", "Liver", "Thyroid", "Pituitary"],
      1,
      "The **liver** is the largest gland (and largest internal organ). It secretes bile, stores glycogen and detoxifies substances. The pituitary is the 'master gland', not the largest.",
      None, "easy", "bio-human-body", "body record", 15),
    Q("bio-q05",
      "The smallest bone in the human body is:",
      ["Stapes", "Femur", "Malleus", "Incus"],
      0,
      "The **stapes** (stirrup) in the **middle ear** is the smallest bone. The femur (thigh bone) is the longest. Malleus and incus are the other two ear ossicles, both larger than the stapes.",
      None, "easy", "bio-human-body", "body record", 15),
    Q("bio-q06",
      "Insulin is secreted by:",
      ["Liver", "Pancreas", "Adrenal gland", "Thyroid gland"],
      1,
      "**Insulin** is secreted by the **β-cells of the islets of Langerhans in the pancreas**. It lowers blood glucose; lack of it causes **diabetes mellitus**.",
      None, "easy", "bio-human-body", "gland → hormone", 15),
    Q("bio-q07",
      "Rickets in children is caused by deficiency of:",
      ["Vitamin A", "Vitamin D", "Vitamin B1", "Vitamin K"],
      1,
      "**Vitamin D (calciferol)** helps absorb calcium and phosphorus. Without it bones stay soft and bend — **rickets** in children, osteomalacia in adults. Sunlight lets the skin make vitamin D.",
      "D → Deformed bones.", "easy", "bio-nutrition", "vitamin → deficiency", 15),
    Q("bio-q08",
      "Goitre is caused by deficiency of:",
      ["Iron", "Iodine", "Calcium", "Sodium"],
      1,
      "**Iodine** is needed to make **thyroxine**. When it is short, the thyroid gland enlarges — **goitre**. Iron deficiency causes anaemia.",
      None, "easy", "bio-nutrition", "mineral → deficiency", 15),
    Q("bio-q09",
      "Vitamin K is essential for:",
      ["Vision", "Clotting of blood", "Healthy gums", "Bone formation"],
      1,
      "**Vitamin K** is needed to make clotting factors (such as prothrombin) in the liver; its deficiency leads to excessive bleeding. Vision needs vitamin A, gums need C, bones need D.",
      "K → Klotting.", "easy", "bio-nutrition", "vitamin function", 15),
    Q("bio-q10",
      "Dengue fever is transmitted by which mosquito?",
      ["Female Anopheles", "Aedes", "Culex", "Mansonia"],
      1,
      "**Dengue** (a viral disease) is spread by the day-biting **Aedes** mosquito (*Aedes aegypti*), which also spreads chikungunya, Zika and yellow fever. Anopheles spreads malaria and Culex spreads filariasis.",
      None, "easy", "bio-diseases", "disease → vector", 15),
    Q("bio-q11",
      "Penicillin, the first antibiotic, was discovered by:",
      ["Louis Pasteur", "Alexander Fleming", "Edward Jenner", "Robert Koch"],
      1,
      "**Alexander Fleming** discovered penicillin in **1928** from the mould *Penicillium notatum*. Jenner made the smallpox vaccine, Pasteur the rabies vaccine, and Koch discovered the TB bacterium.",
      None, "easy", "bio-diseases", "scientist → discovery", 15),
    Q("bio-q12",
      "Tuberculosis is caused by a:",
      ["Virus", "Bacterium", "Protozoan", "Fungus"],
      1,
      "TB is caused by the bacterium ***Mycobacterium tuberculosis***, discovered by Robert Koch (1882). The **BCG** vaccine protects against it and the **Mantoux** test detects infection.",
      None, "easy", "bio-diseases", "disease → pathogen", 15),
    Q("bio-q13",
      "Which plant hormone is responsible for the ripening of fruits?",
      ["Auxin", "Ethylene", "Cytokinin", "Gibberellin"],
      1,
      "**Ethylene**, a gaseous hormone, speeds up **fruit ripening**. Auxin controls cell elongation, cytokinin promotes cell division and gibberellin causes stem elongation.",
      None, "easy", "bio-plants-classification", "plant hormone", 15),
    Q("bio-q14",
      "The five-kingdom classification of living organisms was proposed by:",
      ["Carolus Linnaeus", "R.H. Whittaker", "Ernst Haeckel", "Charles Darwin"],
      1,
      "**R.H. Whittaker** proposed the five kingdoms — Monera, Protista, Fungi, Plantae, Animalia — in **1969**. Linnaeus gave binomial nomenclature and the two-kingdom system.",
      "My Pet Fish Plays Alone — Whittaker.", "easy", "bio-plants-classification", "classification", 15),
    Q("bio-q15",
      "Ornithology is the study of:",
      ["Insects", "Birds", "Fish", "Fungi"],
      1,
      "**Ornithology** is the study of **birds** (Greek *ornis*, bird). Insects — entomology, fish — ichthyology, fungi — mycology.",
      None, "easy", "bio-branches-ecology", "branch of study", 15),
]

place(PRACTICE, [3, 1, 0, 2, 0, 3, 1, 2, 0, 3, 1, 2, 1, 0, 3])

topic = {
    "id": "biology",
    "sectionId": "ga",
    "title": "Biology",
    "importance": "high",
    "avgQuestions": {"tier1": 2, "tier2": 2},
    "summary": "Cell and genetics, human body systems, vitamins and minerals, diseases with pathogens, vectors and vaccines, plant physiology and classification, and branches of biology with ecology. Biology is the most-asked science area in CGL GA — mostly direct one-line facts.",
    "subtopics": SUBTOPICS,
    "pyqPatterns": PYQ,
    "solvedExamples": SOLVED,
    "practice": PRACTICE,
}

if __name__ == "__main__":
    save_topic(topic)
