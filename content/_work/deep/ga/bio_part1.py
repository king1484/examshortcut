"""biology deep content — part 1: bio-cell, bio-human-body, bio-nutrition."""
import os
import sys

sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
from _lib import Sub


def build_cell():
    S = Sub("bio-cell")
    S.notes = """### The cell — discovery and the cell theory
**Robert Hooke** saw cork cells under his microscope in **1665** (book: *Micrographia*) — he named 'cells' but saw only dead walls. **Leeuwenhoek** first saw **living cells** ('animalcules'). **Robert Brown** discovered the **nucleus (1831)**. The **cell theory**: **Schleiden** (1838, plants) and **Schwann** (1839, animals) said all living things are made of cells; **Virchow (1855)** completed it — every cell arises from a pre-existing cell (*Omnis cellula e cellula*).

### Organelles — who does what
| Organelle | Job / title |
|---|---|
| **Mitochondria** | Respiration, ATP — **'powerhouse of the cell'**; has its own DNA |
| **Ribosome** | **Protein synthesis** — 'protein factory' |
| **Golgi body** | Packs and dispatches secretions — 'post office' |
| **Lysosome** | Digestive enzymes — **'suicide bags'** |
| **Chloroplast** | Photosynthesis (plastid); other plastids store colour/starch |
| **Nucleus** | Controls the cell; stores DNA — the 'brain' |
| **Vacuole** | Storage; big and central in plant cells |
| **Cell wall** | Rigid cellulose coat — **plant cells only** |
Plant vs animal cell: plant has a **cell wall, chloroplasts and a large central vacuole**; animal cells have **centrosomes** instead.

### Cell types and cell division
**Prokaryotes** (bacteria, blue-green algae) — no true nucleus, no membrane-bound organelles. **Eukaryotes** (plants, animals, fungi, protists) — true nucleus. Cell division: **mitosis** keeps the chromosome number (body growth, 46 → 46); **meiosis** halves it (gamete formation, 46 → 23) — the basis of sexual reproduction.

### Genetics — the science of heredity
**Gregor Mendel**, the **father of genetics**, worked on garden pea (*Pisum sativum*) and gave the laws of inheritance — dominant vs recessive traits. **Watson and Crick (1953)** gave the **DNA double-helix model**; a **gene** is a stretch of DNA coding a trait. Humans carry **46 chromosomes = 23 pairs**; the **23rd pair decides sex — XX female, XY male**, so the **father determines the child's sex**. Blood groups too are inherited traits.

### Cell records and blood cells
- **Largest human cell** — the **ovum** (egg); **longest** — the **nerve cell** (up to a metre).
- **RBC** (red blood cells): biconcave, **no nucleus**, carry oxygen on **haemoglobin** (iron); live about **120 days**.
- **WBC**: the defence cells (immunity); **platelets**: clot the blood.
- Normal counts: RBC ≈ 5 million per mm³, WBC ≈ 6,000–8,000 per mm³.

### Quick revision
- Hooke named cells (1665); Leeuwenhoek saw living ones; Brown found the nucleus; Schleiden + Schwann + Virchow = cell theory.
- Powerhouse–mitochondria; protein factory–ribosome; suicide bag–lysosome; post office–Golgi.
- Mitosis 46→46; meiosis 46→23; XX female, XY male; father decides sex.
- Mendel = father of genetics (pea plant); Watson & Crick = DNA double helix.
- Largest human cell–ovum; longest–nerve cell; RBC survives ~120 days."""
    S.pattern("ga-ce-p1", "Cell theory and discoverers", "very common",
        "'Who discovered the cell / nucleus / living cells', 'the cell theory was given by…', 'omnis cellula e cellula' attribution, year-based questions (1665, 1831, 1855).",
        None,
        "1. Timeline: 1665 Hooke (cork, named cells) → Leeuwenhoek (living cells) → 1831 Robert Brown (nucleus) → 1838–39 Schleiden + Schwann (theory) → 1855 Virchow (cells from cells).\n2. Trap: Hooke saw dead cork walls; the LIVING cells credit goes to Leeuwenhoek.\n3. Latin tag *omnis cellula e cellula* belongs to Virchow.\nWhy: each scientist has exactly one signature fact — match the year and the noun.",
        "The **cell theory** was proposed by —",
        "**Schleiden and Schwann** (1838–39), completed by Virchow. Hooke only named the cell.")
    S.pattern("ga-ce-p2", "Organelle ↔ function/nickname", "very common",
        "'Powerhouse of the cell', 'suicide bags', 'which organelle makes protein / packages secretions', 'which organelle has its own DNA'.",
        None,
        "1. Nickname table: powerhouse–mitochondria; protein factory–ribosome; post office–Golgi; suicide bag–lysosome; kitchen–chloroplast; brain–nucleus.\n2. Special facts: mitochondria and chloroplasts have their OWN DNA; RBCs are the odd cells WITHOUT a nucleus.\n3. Photosynthesis needs chloroplast + chlorophyll; respiration is the mitochondrion's job.\nWhy: the question is always one nickname or one job — recall the pair, don't reason.",
        "Which organelle is called the **'suicide bag'** of the cell?",
        "**Lysosome** — its enzymes digest the cell itself if the membrane bursts, hence the nickname.")
    S.pattern("ga-ce-p3", "Prokaryote vs eukaryote, plant vs animal cell", "common",
        "'Which is a prokaryote', 'bacteria lack a true nucleus', 'cell wall is made of cellulose in…', 'which structure is absent in animal cells'.",
        None,
        "1. Prokaryote = no true nucleus, no membrane-bound organelles (bacteria, blue-green algae); eukaryote = everything else.\n2. Plant-only structures: cell wall (cellulose), chloroplasts, large central vacuole. Animal-only: centrosome.\n3. 'Absent in animal cells' almost always answers cell wall or chloroplast.",
        "The **cell wall** of a plant cell is made of —",
        "**Cellulose** — absent in animal cells. Chitin instead builds the fungal wall.")
    S.pattern("ga-ce-p4", "Cell division and chromosome numbers", "common",
        "'The human body cell has how many chromosomes', 'chromosome number in a gamete', 'mitosis vs meiosis', 'which division keeps the number the same'.",
        None,
        "1. Human body cell = 46 chromosomes (23 pairs); gamete = 23 — meiosis halves it.\n2. Mitosis: growth and repair, number preserved (46→46). Meiosis: gamete formation, number halved (46→23).\n3. Sex chromosomes: 22 pairs are autosomes; the 23rd pair (XX/XY) decides sex — the father's sperm decides it.",
        "A human **gamete** contains how many chromosomes?",
        "**23** — meiosis halves the body-cell number of 46; fertilisation restores 46.")
    S.pattern("ga-ce-p5", "Genetics: Mendel, DNA, inheritance", "common",
        "'Father of genetics', 'the DNA double helix model was given by…', 'Mendel worked on which plant', 'who determines the sex of a child', 'a gene is a segment of…'.",
        None,
        "1. Mendel = father of genetics; plant = garden pea (*Pisum sativum*); laws of dominance and segregation.\n2. DNA double helix — Watson and Crick, 1953; gene = segment of DNA.\n3. Sex determination: mother always gives X; father gives X (girl) or Y (boy) — so the FATHER decides.\nWhy: one name + one organism + one year is the whole question.",
        "**Watson and Crick** are famous for —",
        "The **double-helix model of DNA** (1953). Mendel is the genetics-father; Crick later also worked on the genetic code.")
    S.pattern("ga-ce-p6", "Blood cells and cell records", "common",
        "'Which blood cells lack a nucleus', 'lifespan of RBC', 'which cells fight infection', 'largest / longest cell in the human body', 'which cell carries oxygen'.",
        None,
        "1. RBC: no nucleus, biconcave, haemoglobin + iron, oxygen transport, ~120-day life.\n2. WBC: defence/immunity; platelets: clotting (the third, fragment-type cell).\n3. Records: ovum = largest human cell; nerve cell = longest.",
        "The average lifespan of a human **red blood cell** is about —",
        "**120 days**; worn-out RBCs are destroyed mainly in the spleen (the 'graveyard of RBCs').")

    S.q("ga-ce-p1", "easy", "Who first saw and named **'cells'** in cork (1665)?",
        ["Robert Hooke", "Leeuwenhoek", "Robert Brown", "Louis Pasteur"], "Robert Hooke",
        "**Robert Hooke**, in *Micrographia* (1665), saw box-like dead cork walls and named them cells. Leeuwenhoek later saw living cells.",
        None, 15)
    S.q("ga-ce-p1", "medium", "The **nucleus** was discovered by —",
        ["Robert Brown", "Schleiden", "Virchow", "Watson"], "Robert Brown",
        "**Robert Brown (1831)** found the nucleus inside orchid cells. Schleiden and Schwann built the cell theory; Virchow added 'cells from cells'.",
        None, 15)
    S.q("ga-ce-p1", "medium", "*Omnis cellula e cellula* (every cell from a pre-existing cell) was stated by —",
        ["Rudolf Virchow", "Robert Hooke", "Theodor Schwann", "Gregor Mendel"], "Rudolf Virchow",
        "**Virchow (1855)** completed the cell theory with this line. Schleiden (plants) and Schwann (animals) had proposed the theory itself.",
        None, 15)
    S.q("ga-ce-p2", "easy", "The **'powerhouse of the cell'** is —",
        ["Mitochondria", "Ribosome", "Nucleus", "Golgi body"], "Mitochondria",
        "**Mitochondria** run respiration and make ATP — hence the powerhouse. They also carry their own DNA.",
        None, 15)
    S.q("ga-ce-p2", "easy", "**Protein synthesis** in a cell is done by —",
        ["Ribosomes", "Lysosomes", "Vacuoles", "Chloroplasts"], "Ribosomes",
        "**Ribosomes** are the 'protein factories'. Lysosomes digest; chloroplasts photosynthesise.",
        None, 15)
    S.q("ga-ce-p2", "medium", "Which organelles contain their **own DNA**, apart from the nucleus?",
        ["Mitochondria and chloroplasts", "Ribosomes and lysosomes", "Golgi body and vacuole", "None of these"], "Mitochondria and chloroplasts",
        "**Mitochondria and chloroplasts** are semi-autonomous — both keep their own circular DNA, a sign of their bacterial ancestors.",
        None, 20)
    S.q("ga-ce-p3", "medium", "Which structure is **absent in animal cells**?",
        ["Cell wall", "Cell membrane", "Mitochondria", "Ribosomes"], "Cell wall",
        "A **cellulose cell wall** is plant-only (with chloroplasts and a big central vacuole). Animal cells have a centrosome instead.",
        None, 15)
    S.q("ga-ce-p3", "medium", "Which of these is a **prokaryote**?",
        ["Bacterium", "Amoeba", "Mushroom", "Mango plant"], "Bacterium",
        "**Bacteria** (and blue-green algae) have no true nucleus — prokaryotes. Amoeba, fungi and plants are eukaryotes.",
        None, 15)
    S.q("ga-ce-p4", "medium", "A normal **human body cell** contains how many chromosomes?",
        ["46", "23", "48", "44"], "46",
        "**46 chromosomes = 23 pairs**; 22 pairs are autosomes, the 23rd pair carries the sex chromosomes XX or XY.",
        None, 15)
    S.q("ga-ce-p4", "medium", "During **meiosis**, the chromosome number of a human cell —",
        ["Is halved from 46 to 23", "Stays at 46", "Doubles to 92", "Becomes 44"], "Is halved from 46 to 23",
        "**Meiosis** halves the number to make gametes (23); **mitosis** keeps 46 for growth. Fertilisation adds 23 + 23 back to 46.",
        None, 20)
    S.q("ga-ce-p5", "easy", "Who is called the **father of genetics**?",
        ["Gregor Mendel", "Charles Darwin", "Watson and Crick", "Hugo de Vries"], "Gregor Mendel",
        "**Mendel**, an Austrian monk, deduced the laws of inheritance from garden-pea experiments. Darwin gave evolution; Watson and Crick, the DNA model.",
        None, 15)
    S.q("ga-ce-p5", "medium", "Mendel's experiments on heredity were performed on —",
        ["Garden pea (Pisum sativum)", "Fruit fly", "Maize", "Sunflower"], "Garden pea (Pisum sativum)",
        "**Pisum sativum** — seven clear pairs of contrasting traits (tall/dwarf, round/wrinkled…). The fruit fly was Morgan's genetics workhorse later.",
        None, 15)
    S.q("ga-ce-p5", "medium", "The **sex of a child** is determined by —",
        ["The father's chromosome (X or Y)", "The mother's chromosome", "Nutrition of the mother", "Chance alone"], "The father's chromosome (X or Y)",
        "The mother's egg always carries X; the father's sperm carries X (girl, XX) or Y (boy, XY) — so the **father determines sex**.",
        None, 15)
    S.q("ga-ce-p5", "medium", "The **double-helix model of DNA** was proposed by —",
        ["Watson and Crick", "Mendel and Darwin", "Schleiden and Schwann", "Hooke and Leeuwenhoek"], "Watson and Crick",
        "**James Watson and Francis Crick**, 1953. A gene is a segment of this DNA that codes one trait.",
        None, 15)
    S.q("ga-ce-p6", "medium", "The **largest cell** in the human body is —",
        ["The ovum (egg)", "The nerve cell", "The RBC", "The muscle cell"], "The ovum (egg)",
        "The **ovum** is the largest; the **nerve cell** is the longest (up to about a metre). RBCs are among the smallest.",
        None, 15)
    S.q("ga-ce-p6", "medium", "Which blood cells **lack a nucleus** and carry oxygen?",
        ["Red blood cells", "White blood cells", "Platelets", "Plasma cells"], "Red blood cells",
        "Mature **RBCs** throw out their nucleus to pack in more **haemoglobin** (iron-based oxygen carrier). WBCs have nuclei and fight infection.",
        None, 15)
    return S


def build_body():
    S = Sub("bio-human-body")
    S.notes = """### Body records — the standard list
| Record | Answer |
|---|---|
| Largest organ | **Skin** |
| Largest gland / largest internal organ | **Liver** |
| Largest endocrine gland | **Thyroid** |
| Longest bone | **Femur** (thigh) |
| Smallest bone | **Stapes** (middle ear) |
| Smallest muscle | **Stapedius** (ear) |
| Strongest muscle (by force) | **Jaw (masseter)** |
| Bones in an adult | **206** |
| Bones in a newborn | about **300** (many fuse later) |
| Ribs | **12 pairs = 24** |
| Normal body temperature | **37 °C (98.6 °F)** |

### Blood and circulation
Blood ≈ 5 litres. **Plasma** (55%, the liquid), **RBC** (oxygen on haemoglobin), **WBC** (defence), **platelets** (clotting). **Blood groups**: ABO + Rh; **O− is the universal donor, AB+ the universal recipient**. The **heart** has 4 chambers (2 atria + 2 ventricles); its natural **pace-maker is the SA node**; humans have **double circulation** (blood passes through the heart twice per loop). Blood pressure is measured with a **sphygmomanometer**; normal ≈ **120/80 mm Hg**. A resting heart beats ≈ **72 times a minute**.

### Digestive system — organ by organ
Mouth: **salivary amylase** starts starch digestion. Stomach: **HCl** + **pepsin** (protein); a mucous lining saves the stomach from itself. Liver makes **bile** (stored in the gall bladder — **no enzymes**, it only **emulsifies fat**). Pancreas sends **trypsin** (protein) and **lipase** (fat). The **small intestine** is the real digestion + absorption site (villi); the large intestine absorbs only water.

### Endocrine glands — hormones
**Pituitary** = 'master gland' (growth hormone; under- or over-secretion gives dwarfism/gigantism). **Thyroid** = **thyroxine (contains iodine)** — deficiency causes **goitre**; **pancreas** = **insulin** (from the islets of Langerhans) controls blood sugar — its failure is **diabetes**; **adrenal** = adrenaline (the 'fight-or-flight' hormone); testes/ovaries = testosterone/estrogen.

### Excretion and the brain
**Kidneys** filter the blood in about a million **nephrons** each; urine (urea + water + salts) reaches the bladder. The **brain**: **cerebrum** (thinking, largest part), **cerebellum** (balance, posture), **medulla oblongata** (involuntary heartbeat/breathing — a spine injury there is fatal); reflex actions are handled by the **spinal cord** without waiting for the brain.

### Quick revision
- 206 adult bones; stapes smallest, femur longest; skin largest organ; liver largest gland.
- O− universal donor, AB+ universal recipient; SA node = pace-maker; BP 120/80 (sphygmomanometer).
- Bile has no enzymes (emulsifies fat); HCl + pepsin in stomach; villi absorb in the small intestine.
- Pituitary master gland; thyroxine needs iodine; insulin from pancreas fights diabetes; adrenaline = fight-or-flight.
- Cerebrum thinks, cerebellum balances, medulla keeps the heart beating."""
    S.pattern("ga-hb-p1", "Body records (largest/smallest/number)", "very common",
        "'Largest gland / largest organ / longest bone / smallest bone', 'how many bones does an adult have', 'which muscle is the smallest', number-of-ribs questions.",
        None,
        "1. Records: skin = largest organ; liver = largest gland (and largest internal organ); thyroid = largest ENDOCRINE gland; femur = longest bone; stapes = smallest bone; stapedius = smallest muscle.\n2. Numbers: adult 206 bones, newborn ≈ 300, ribs 12 pairs.\n3. Trap: 'largest gland' = liver; 'largest endocrine gland' = thyroid; both are often mixed.\nWhy: pure recall — keep one list, test the three largest-X pairs against each other.",
        "The **smallest bone** in the human body is —",
        "**Stapes** in the middle ear (about 3 mm). The smallest muscle, stapedius, sits right beside it.")
    S.pattern("ga-hb-p2", "Blood, groups and circulation", "very common",
        "'Universal donor / recipient', 'which blood cells fight infection / help clotting', 'pace-maker of the heart', 'how many chambers does the heart have', instrument for BP.",
        None,
        "1. Cells: RBC carry oxygen; WBC defend; platelets clot.\n2. Groups: O− universal donor; AB+ universal recipient; Rh factor decides +/−.\n3. Heart: 4 chambers; SA node = pace-maker; double circulation in humans.\n4. BP instrument = sphygmomanometer; normal 120/80 mm Hg; pulse ≈ 72/min resting.",
        "Which blood group is the **universal recipient**?",
        "**AB+** — it carries no anti-A or anti-B antibodies. O− is the universal donor counterpart.")
    S.pattern("ga-hb-p3", "Organ ↔ secretion/function", "very common",
        "'Insulin is secreted by…', 'bile is produced in… / stored in…', 'which organ filters the blood', 'HCl is secreted in…', 'nephron belongs to…'.",
        None,
        "1. Digestive secretions: mouth–salivary amylase; stomach–HCl + pepsin; liver–bile (stored in gall bladder, no enzymes); pancreas–trypsin + lipase (+ insulin from islets of Langerhans).\n2. Kidney: filtration unit = nephron; brain parts: cerebrum–thinking, cerebellum–balance, medulla–involuntary control.\n3. 'Bile stored where' = gall bladder; 'bile made where' = liver — split them.",
        "**Bile**, which helps digest fats, is produced by the —",
        "**Liver** (largest gland) and stored in the gall bladder; it emulsifies fat but contains no enzymes.")
    S.pattern("ga-hb-p4", "Hormone ↔ gland and deficiency", "very common",
        "'Insulin / thyroxine / adrenaline is secreted by', 'master gland', 'which hormone controls blood sugar', 'deficiency of growth hormone causes…'.",
        None,
        "1. Master gland–pituitary (growth hormone); thyroid–thyroxine (iodine; low → goitre); pancreas–insulin (diabetes); adrenal–adrenaline (fight-or-flight).\n2. Sex hormones: testes–testosterone, ovaries–estrogen.\n3. Link each hormone to its imbalance: dwarfism/gigantism–growth hormone, goitre–thyroxine, diabetes–insulin.\nWhy: gland–hormone–disease is a fixed triangle; any corner can be asked.",
        "Which gland is called the **'master gland'**?",
        "**Pituitary** — its hormones steer the other endocrine glands, including the thyroid and adrenals.")
    S.pattern("ga-hb-p5", "Digestion steps and enzymes", "common",
        "'Which enzyme digests protein / starch / fat', 'where is food fully digested and absorbed', 'function of villi', 'which juice has no enzyme', 'peristalsis is…'.",
        None,
        "1. Enzyme-to-food: amylase–starch, pepsin/trypsin–protein, lipase–fat.\n2. Small intestine = final digestion + absorption (villi increase area); large intestine = water only.\n3. Bile = no enzymes, emulsifies fat; peristalsis = wave-like muscle movement pushing food.",
        "Digested food is absorbed mainly in the —",
        "**Small intestine**, through millions of villi that multiply the absorbing surface. The large intestine takes up only water and salts.")
    S.pattern("ga-hb-p6", "Body numbers (computed)", "common",
        "'How many times does the heart beat in a day', 'normal body temperature in °F', 'how much blood does an adult have', questions needing 72 × 60 or 37 → 98.6 conversion.",
        None,
        "1. Heart: 72 beats/min → 72 × 60 × 24 = 103,680 beats/day.\n2. Temperature: 37 °C = 98.6 °F (F = 9C/5 + 32).\n3. Blood volume ≈ 5 litres; RBC count ≈ 5 million/mm³; WBC ≈ 6,000–8,000/mm³.\n4. Compute the arithmetic in your head by splitting: 72 × 60 = 4,320; × 24 ≈ 1.04 lakh.",
        "At a resting rate of **72 beats per minute**, the heart beats about how many times a **day**?",
        "72 × 60 × 24 = **103,680** — roughly 1 lakh beats a day, pumping thousands of litres.")

    S.q("ga-hb-p1", "easy", "The **largest gland** in the human body is —",
        ["Liver", "Pancreas", "Thyroid", "Pituitary"], "Liver",
        "**Liver** — largest gland and largest internal organ. The thyroid is only the largest ENDOCRINE gland.",
        None, 15)
    S.q("ga-hb-p1", "easy", "The **longest bone** in the human body is the —",
        ["Femur", "Tibia", "Humerus", "Radius"], "Femur",
        "**Femur** (thigh bone). The humerus is the upper arm; tibia and radius are lower leg and forearm bones.",
        None, 15)
    S.q("ga-hb-p1", "medium", "An adult human skeleton has how many bones?",
        ["206", "300", "230", "306"], "206",
        "**206** in an adult; a newborn starts near 300 and many fuse as it grows. Ribs add 12 pairs to the count.",
        None, 15)
    S.q("ga-hb-p1", "medium", "The **smallest muscle** in the human body is —",
        ["Stapedius", "Masseter", "Cardiac muscle", "Sartorius"], "Stapedius",
        "**Stapedius** in the middle ear moves the stapes bone. The masseter (jaw) is the strongest by force.",
        None, 15)
    S.q("ga-hb-p2", "easy", "The **universal donor** blood group is —",
        ["O negative", "AB positive", "A positive", "B negative"], "O negative",
        "**O−** has no A, B or Rh antigens, so nobody's blood rejects it. AB+ is the universal recipient.",
        None, 15)
    S.q("ga-hb-p2", "easy", "Blood **clotting** is carried out by —",
        ["Platelets", "Red blood cells", "White blood cells", "Plasma"], "Platelets",
        "**Platelets (thrombocytes)** gather at a cut and trigger fibrin formation. WBC fight germs; RBC carry oxygen.",
        None, 15)
    S.q("ga-hb-p2", "medium", "The natural **pace-maker of the heart** is —",
        ["The SA node (sino-atrial node)", "The AV node", "The medulla", "The vagus nerve"], "The SA node (sino-atrial node)",
        "The **SA node** in the right atrium fires the beat — artificial pace-makers only replace it when it fails.",
        None, 15)
    S.q("ga-hb-p2", "medium", "Blood pressure is measured with a —",
        ["Sphygmomanometer", "Thermometer", "Lactometer", "Barometer"], "Sphygmomanometer",
        "**Sphygmomanometer** — normal value 120/80 mm Hg (systolic/diastolic). A barometer measures air pressure.",
        None, 15)
    S.q("ga-hb-p3", "easy", "**Insulin**, which controls blood sugar, is secreted by the —",
        ["Pancreas", "Liver", "Thyroid", "Pituitary"], "Pancreas",
        "The **pancreas** (islets of Langerhans) secretes insulin; its shortage causes **diabetes**. The liver stores glycogen but makes no insulin.",
        None, 15)
    S.q("ga-hb-p3", "medium", "Bile is **stored** in the —",
        ["Gall bladder", "Liver", "Spleen", "Duodenum"], "Gall bladder",
        "Made in the **liver**, stored in the **gall bladder**, released into the small intestine. Bile itself has no enzymes — it only emulsifies fat.",
        None, 15)
    S.q("ga-hb-p3", "medium", "The functional (filtering) unit of the **kidney** is the —",
        ["Nephron", "Neuron", "Alveolus", "Villus"], "Nephron",
        "Each kidney packs about a million **nephrons**. Alveolus belongs to the lung, villus to the gut, neuron to nerves.",
        None, 15)
    S.q("ga-hb-p3", "medium", "Which part of the **brain** controls balance and posture?",
        ["Cerebellum", "Cerebrum", "Medulla oblongata", "Hypothalamus"], "Cerebellum",
        "**Cerebellum** — balance and coordinated movement. Cerebrum thinks; medulla runs heartbeat and breathing involuntarily.",
        None, 15)
    S.q("ga-hb-p4", "medium", "**Goitre**, a swelling of the neck, is caused by the deficiency of —",
        ["Iodine", "Iron", "Calcium", "Vitamin A"], "Iodine",
        "Iodised salt prevents it. The **thyroid** needs iodine to make **thyroxine**; without it the gland swells working harder.",
        None, 15)
    S.q("ga-hb-p4", "medium", "**Adrenaline**, the 'fight-or-flight' hormone, is secreted by the —",
        ["Adrenal gland", "Thyroid gland", "Pituitary gland", "Pancreas"], "Adrenal gland",
        "**Adrenal glands** (on the kidneys) release adrenaline in emergencies — faster heartbeat, more blood sugar, instant energy.",
        None, 15)
    S.q("ga-hb-p4", "medium", "Over-secretion of **growth hormone** in children causes —",
        ["Gigantism", "Dwarfism", "Goitre", "Diabetes"], "Gigantism",
        "Too much growth hormone from the pituitary in childhood → **gigantism**; too little → dwarfism; in adults, acromegaly.",
        None, 15)
    S.q("ga-hb-p5", "medium", "Which enzyme in **saliva** starts digesting starch?",
        ["Amylase", "Pepsin", "Lipase", "Trypsin"], "Amylase",
        "**Salivary amylase** breaks starch while you chew. Pepsin and trypsin take protein; lipase takes fat.",
        None, 15)
    S.q("ga-hb-p5", "medium", "The enzyme **pepsin**, active in the stomach, digests —",
        ["Proteins", "Fats", "Starch", "Vitamins"], "Proteins",
        "**Pepsin** needs the stomach's **HCl** (strong acid) to work on protein. Amylase handles starch and lipase fat.",
        None, 15)
    S.q("ga-hb-p6", "hard", "A person's heart beats at **72 per minute**. Roughly how many beats is that in a **day**?",
        ["103,680", "43,200", "10,368", "1,036,800"], "103,680",
        "72 × 60 = 4,320 per hour; × 24 = **103,680** per day — about 1 lakh beats daily.",
        None, 25)
    S.q("ga-hb-p6", "medium", "Normal human body temperature of **37 °C** equals —",
        ["98.6 °F", "96.8 °F", "100 °F", "89.6 °F"], "98.6 °F",
        "F = 9 × 37/5 + 32 = 66.6 + 32 = **98.6 °F** — the standard body-temperature pair.",
        None, 15)
    return S


def build_nutrition():
    S = Sub("bio-nutrition")
    S.notes = """### Vitamins → deficiency diseases (the top table)
| Vitamin | Chemical name | Deficiency disease | Source |
|---|---|---|---|
| **A** | Retinol | **Night blindness**, xerophthalmia | Carrot, papaya, milk |
| **B₁** | Thiamine | **Beriberi** | Whole grains, pulses |
| **B₂** | Riboflavin | Cheilosis (cracked lips) | Milk, eggs |
| **B₃** | Niacin | **Pellagra** (3 Ds) | Groundnut |
| **B₁₂** | Cyanocobalamin | **Pernicious anaemia** | Meat, milk |
| **C** | Ascorbic acid | **Scurvy** (bleeding gums) | Amla, citrus |
| **D** | Calciferol | **Rickets** (children), osteomalacia (adults) | Sunlight, fish oil |
| **E** | Tocopherol | Sterility | Wheat germ |
| **K** | Phylloquinone | **Poor clotting** | Green leafy vegetables |
**Fat-soluble**: **A, D, E, K** (stored in the body — excess can harm). **Water-soluble**: **B-complex and C** (washed out daily). **Casimir Funk (1912)** coined the word 'vitamine'. Sunlight on the skin makes **vitamin D**. Cooking destroys vitamin C most easily.

### Minerals → deficiency
**Iron** → **anaemia** (haemoglobin is iron-based); **iodine** → **goitre** (thyroxine); **calcium** → weak bones/teeth; **phosphorus** → bones + ATP; **fluorine** → too little causes dental caries, too much causes **fluorosis**; **sodium and potassium** → nerve and muscle function. Zinc: wound healing and immunity.

### Malnutrition — the two classics
**Kwashiorkor**: protein deficiency *with* adequate calories — swollen belly, oedema, thin limbs, in children 1–3 years. **Marasmus**: deficiency of *both* protein and calories — the child is all skin and bones, under one year old. One-line hold: **kwashiorkor = swollen, marasmus = shrunken**. Obesity is the opposite imbalance; **roughage** (fibre) prevents constipation.

### Food energy — the numbers
| Component | Energy |
|---|---|
| Carbohydrate | **4 kcal/g** |
| Protein | **4 kcal/g** |
| Fat | **9 kcal/g** |
Fat carries more than twice the energy per gram — hence a **30 g** fat snack gives 30 × 9 = 270 kcal. A balanced diet splits roughly 60% carbohydrates, 25–30% fat, 10–15% protein of the calories. **Basal metabolic rate (BMR)** is the resting burn; an adult needs ≈ 2,000–2,500 kcal/day.

### Quick revision
- A–night blindness, B₁–beriberi, B₃–pellagra, B₁₂–pernicious anaemia, C–scurvy, D–rickets, E–sterility, K–clotting.
- Fat-soluble A D E K; water-soluble B and C; 'vitamine' = Casimir Funk; vitamin D from sunlight.
- Iron–anaemia, iodine–goitre, calcium–bones, fluorine–caries/fluorosis.
- Kwashiorkor = protein (swollen); marasmus = protein + calories (shrunken).
- Energy: carb 4, protein 4, fat 9 kcal/g."""
    S.pattern("ga-nu-p1", "Vitamin → deficiency disease", "very common",
        "'Scurvy is caused by deficiency of…', 'rickets / beriberi / night blindness / pernicious anaemia', wrong-pair questions on the vitamin table.",
        None,
        "1. Sing the ladder: A–night blindness, B₁–beriberi, B₃–pellagra, B₁₂–pernicious anaemia, C–scurvy, D–rickets, E–sterility, K–clotting.\n2. Alphabet anchor: C = Citrus = scurvy (sailors); D = sun = rickets; K = Koagulation = clotting.\n3. In wrong-pair questions, check D–rickets and C–scurvy first — they are the usual deliberate swaps.\nWhy: fixed pairs, zero logic — pure table recall.",
        "**Pernicious anaemia** is caused by the deficiency of —",
        "**Vitamin B₁₂ (cyanocobalamin)**. Ordinary iron-deficiency anaemia is a different, more common condition.")
    S.pattern("ga-nu-p2", "Vitamin sources and fat/water solubility", "common",
        "'Which vitamins are fat-soluble', 'which vitamin is made in the skin by sunlight', 'rich source of vitamin C', 'which vitamin is destroyed by cooking'.",
        None,
        "1. Fat-soluble = **A, D, E, K** (they store in the liver/fat); water-soluble = B-complex, C.\n2. Sunlight → vitamin D in the skin; cooking destroys **vitamin C** the most.\n3. Sources: A–carrot/papaya, C–amla/citrus, D–fish oil/sun, K–green leafy vegetables.",
        "Which set contains **only fat-soluble** vitamins?",
        "**A, D, E, K** — remember the word KEDA/ADKE. B-complex and C wash out with water every day.")
    S.pattern("ga-nu-p3", "Mineral → deficiency/role", "common",
        "'Goitre is due to deficiency of…', 'anaemia is caused by lack of…', 'which mineral builds bones and teeth', 'fluorosis is due to excess…'.",
        None,
        "1. Iron–anaemia (haemoglobin); iodine–goitre (thyroxine); calcium+phosphorus–bones/teeth; fluorine–caries (less) or fluorosis (more).\n2. Sodium/potassium–nerve signals; zinc–healing and immunity.\n3. Both 'too little' and 'too much' of fluorine harm — a favourite trick option.",
        "**Anaemia** (low haemoglobin) most commonly results from the deficiency of —",
        "**Iron** — haemoglobin is an iron pigment, so iron-poor blood carries less oxygen (fatigue, pale skin).")
    S.pattern("ga-nu-p4", "Malnutrition: kwashiorkor vs marasmus", "common",
        "'Kwashiorkor is caused by deficiency of…', 'swollen belly disease of children', 'difference between kwashiorkor and marasmus', protein-calorie malnutrition questions.",
        None,
        "1. **Kwashiorkor**: protein deficient, calories adequate → oedema, swollen belly, thin limbs (age 1–3).\n2. **Marasmus**: protein AND calories deficient → skin-and-bones, no swelling (below 1 year).\n3. Memory line: kwashiorkor = swollen, marasmus = shrunken.",
        "A child with a **swollen belly** but relatively adequate calorie intake suffers from —",
        "**Kwashiorkor** — protein deficiency; the swelling is oedema. Marasmus children are instead wasted and shrunken.")
    S.pattern("ga-nu-p5", "Food energy values (computed)", "common",
        "'How much energy does 1 g of fat/carbohydrate give', a snack's total calories from given grams, 'which nutrient gives maximum energy', BMR questions.",
        None,
        "1. Fixed values: carbohydrate 4 kcal/g, protein 4 kcal/g, **fat 9 kcal/g**.\n2. Fat gives the most energy per gram — the standard 'maximum energy' answer.\n3. Compute totals part-wise: (fat g × 9) + (carb g × 4) + (protein g × 4); split multiplication into tens to stay fast.",
        "A snack has **20 g fat** and **10 g carbohydrate**. Its energy is about —",
        "20 × 9 + 10 × 4 = 180 + 40 = **220 kcal** — fat dominates because it carries 9 kcal/g.")
    S.pattern("ga-nu-p6", "Vitamin history and misc facts", "occasional",
        "'Who coined the word vitamin', 'which vitamin is called ascorbic acid', chemical names of vitamins, 'deficiency of which vitamin affects gums'.",
        None,
        "1. **Casimir Funk** coined 'vitamine' (1912).\n2. Chemical names: A–retinol, B₁–thiamine, B₂–riboflavin, B₁₂–cyanocobalamin, C–ascorbic acid, D–calciferol, E–tocopherol, K–phylloquinone.\n3. Bleeding gums = scurvy = vitamin C (ascorbic acid) — the acid name is the giveaway.",
        "The word **'vitamine'** was coined by —",
        "**Casimir Funk (1912)**. He thought all such factors were amines; the final 'e' was later dropped.")

    S.q("ga-nu-p1", "easy", "**Rickets** in children is caused by the deficiency of —",
        ["Vitamin D", "Vitamin C", "Vitamin A", "Vitamin K"], "Vitamin D",
        "**Vitamin D** (with calcium) hardens bones; its lack bends them — rickets. In adults the same lack gives osteomalacia.",
        None, 15)
    S.q("ga-nu-p1", "easy", "**Scurvy** (bleeding gums) is caused by the deficiency of —",
        ["Vitamin C", "Vitamin D", "Vitamin B₁₂", "Vitamin A"], "Vitamin C",
        "**Vitamin C (ascorbic acid)** — sailors got scurvy on long voyages without fresh citrus. Amla is the richest Indian source.",
        None, 15)
    S.q("ga-nu-p1", "medium", "**Beriberi** results from the deficiency of —",
        ["Vitamin B₁ (thiamine)", "Vitamin B₃ (niacin)", "Vitamin B₂ (riboflavin)", "Vitamin B₁₂"], "Vitamin B₁ (thiamine)",
        "**B₁ (thiamine)** — common where polished rice replaces whole grain. B₃ gives pellagra; B₂ cheilosis.",
        None, 15)
    S.q("ga-nu-p1", "medium", "**Night blindness** is an early sign of the deficiency of —",
        ["Vitamin A", "Vitamin C", "Vitamin D", "Vitamin K"], "Vitamin A",
        "**Vitamin A (retinol)** — carrots and papaya are rich sources; advanced lack causes xerophthalmia and corneal damage.",
        None, 15)
    S.q("ga-nu-p1", "medium", "**Pellagra** is caused by the deficiency of —",
        ["Niacin (vitamin B₃)", "Thiamine (B₁)", "Folic acid", "Vitamin C"], "Niacin (vitamin B₃)",
        "**B₃ (niacin)** — the '3 Ds': dermatitis, diarrhoea, dementia (and death if untreated). Groundnut is a good source.",
        None, 15)
    S.q("ga-nu-p1", "medium", "**Vitamin K** deficiency mainly causes —",
        ["Delayed blood clotting", "Night blindness", "Scurvy", "Sterility"], "Delayed blood clotting",
        "**K = Koagulation** — the liver needs it to make clotting factors. Green leafy vegetables supply it.",
        None, 15)
    S.q("ga-nu-p2", "medium", "Which group is **entirely fat-soluble**?",
        ["A, D, E, K", "B, C, D, A", "A, B, C, K", "C, D, E, B"], "A, D, E, K",
        "**A, D, E, K** — they store in fat and liver, so excess can be toxic. B-complex and C are water-soluble and need daily intake.",
        None, 15)
    S.q("ga-nu-p2", "medium", "Which vitamin is synthesised in the **skin** on exposure to sunlight?",
        ["Vitamin D", "Vitamin A", "Vitamin E", "Vitamin B₁"], "Vitamin D",
        "UV light converts a skin sterol into **vitamin D** — the 'sunshine vitamin'. Deficiency gives rickets (children) and osteomalacia (adults).",
        None, 15)
    S.q("ga-nu-p2", "medium", "The richest common Indian source of **vitamin C** is —",
        ["Amla", "Milk", "Wheat", "Butter"], "Amla",
        "**Amla** tops the list (with guava close behind). Citrus fruits are famous but amla has several times more.",
        None, 15)
    S.q("ga-nu-p3", "easy", "**Goitre** is caused by the deficiency of —",
        ["Iodine", "Iron", "Zinc", "Magnesium"], "Iodine",
        "**Iodine** is part of thyroxine; without it the thyroid swells. Iodised salt is the prevention.",
        None, 15)
    S.q("ga-nu-p3", "medium", "**Anaemia** is chiefly caused by the deficiency of —",
        ["Iron", "Calcium", "Iodine", "Sodium"], "Iron",
        "**Iron** builds the haemoglobin that carries oxygen; low iron → pale, tired, breathless. Vitamin B₁₂ deficiency gives the rarer pernicious anaemia.",
        None, 15)
    S.q("ga-nu-p3", "medium", "**Fluorosis** (mottling of teeth and bones) is caused by —",
        ["Excess fluorine in water", "Deficiency of fluorine", "Excess iron", "Deficiency of calcium"], "Excess fluorine in water",
        "**Too much fluorine** in drinking water causes fluorosis; a little protects against dental caries — the dose makes the poison.",
        None, 15)
    S.q("ga-nu-p4", "medium", "**Kwashiorkor** is caused by the severe deficiency of —",
        ["Protein", "Fats", "Vitamin C", "Carbohydrate only"], "Protein",
        "**Protein deficiency** with enough calories — swollen belly and oedema in children aged 1–3. Marasmus lacks protein AND calories.",
        None, 15)
    S.q("ga-nu-p4", "medium", "**Marasmus** differs from kwashiorkor because in marasmus the child lacks —",
        ["Both protein and calories", "Only protein", "Only vitamins", "Only minerals"], "Both protein and calories",
        "**Marasmus = protein + calorie deficiency** — the infant is wasted, skin and bones, under a year old. Kwashiorkor children swell instead.",
        None, 15)
    S.q("ga-nu-p5", "medium", "Which nutrient gives the **maximum energy per gram**?",
        ["Fat (9 kcal/g)", "Protein (4 kcal/g)", "Carbohydrate (4 kcal/g)", "Vitamins"], "Fat (9 kcal/g)",
        "**Fat — 9 kcal/g**, more than double carbohydrate or protein. That is why the body stores spare energy as fat.",
        None, 15)
    S.q("ga-nu-p5", "hard", "A food packet contains **30 g carbohydrate** and **10 g protein**. Its total energy is —",
        ["160 kcal", "120 kcal", "200 kcal", "360 kcal"], "160 kcal",
        "Carb 30 × 4 = 120 kcal; protein 10 × 4 = 40 kcal; total = **160 kcal**. Had it been fat, each gram would count 9.",
        None, 25)
    S.q("ga-nu-p6", "medium", "The word **'vitamine'** was coined by —",
        ["Casimir Funk", "Alexander Fleming", "Louis Pasteur", "Robert Koch"], "Casimir Funk",
        "**Casimir Funk (1912)** coined 'vitamine' while studying beriberi. Fleming discovered penicillin — a different hall of fame.",
        None, 15)
    S.q("ga-nu-p6", "medium", "**Ascorbic acid** is the chemical name of —",
        ["Vitamin C", "Vitamin D", "Vitamin E", "Vitamin A"], "Vitamin C",
        "**Vitamin C = ascorbic acid**. Retinol–A, calciferol–D, tocopherol–E, thiamine–B₁, cyanocobalamin–B₁₂.",
        None, 15)
    return S
