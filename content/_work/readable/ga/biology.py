"""Readable rewrite of GA > Biology (all 6 subtopics).

Facts are kept exactly as in the previous notes/patterns; only the wording and structure change.
Numeric examples are asserted below. Old pattern ids are kept.
Run: python biology.py  (patches content/core/topics/ga/biology.json in place; idempotent)
"""
import json
from fractions import Fraction
from pathlib import Path

ROOT = Path(__file__).resolve().parents[3]
TOPIC = ROOT / "core" / "topics" / "ga" / "biology.json"


def pat(pid, name, freq, spot, steps, why, q, ex_steps, answer, formula=None):
    return {"id": pid, "name": name, "frequency": freq, "howToSpot": spot, "formula": formula,
            "steps": steps, "why": why, "example": {"q": q, "steps": ex_steps, "answer": answer}}


def mis(wrong, right):
    return {"wrong": wrong, "right": right}


# ---------------------------------------------------------------- asserted numbers
assert 72 * 60 * 24 == 103680
assert Fraction(9 * 37, 5) + 32 == Fraction(986, 10)          # 37 C = 98.6 F
assert Fraction(54) / Fraction(3, 2) ** 2 == 24               # BMI 54 kg, 1.5 m
assert 18.5 <= 24 <= 24.9
assert 30 * 9 == 270
assert 20 * 9 + 10 * 4 == 220
assert 25 * 4 + 10 * 4 + 10 * 9 == 230
assert 23 * 2 == 46 and 46 // 2 == 23
assert 22 * 2 + 2 == 46
e = [10000]
for _ in range(4):
    e.append(e[-1] // 10)
assert e == [10000, 1000, 100, 10, 1]
assert Fraction(10000) * Fraction(1, 10) ** (3 - 1) == 100    # third level
assert Fraction(5000) * Fraction(1, 10) ** (2 - 1) == 500     # second level of 5000 J
assert 12 * 2 == 24

SUBS = {}

# =====================================================================
# 1. Cell
# =====================================================================
SUBS["bio-cell"] = dict(
    concept=(
        "The cell is the basic unit of life. Each organelle inside it has one job and one nickname, "
        "such as mitochondria as the powerhouse. Cells divide by mitosis for growth and by meiosis to make gametes. "
        "Genetics adds a few names and numbers: Mendel, Watson and Crick, and 46 human chromosomes."
    ),
    notes=r"""### Who found what about the cell
Each scientist has one signature fact. Match the fact to the name.

| Discovery | Scientist |
|---|---|
| Cell (in cork, 1665) | **Robert Hooke** |
| First living cells, bacteria (single-lens microscope) | **Antonie van Leeuwenhoek** |
| **Nucleus** (1831) | **Robert Brown** |
| **Cell theory** | **Schleiden** (plants) and **Schwann** (animals) |
| 'Omnis cellula e cellula': new cells come from existing cells | **Rudolf Virchow** |

> **Watch:** Hooke saw dead cork walls and named the cell. Leeuwenhoek was the first to see living cells.

### Cell organelles
An organelle is a small working part inside the cell.

| Organelle | Job or nickname |
|---|---|
| **Mitochondria** | **Powerhouse of the cell**. Aerobic respiration, ATP. Has its own DNA |
| **Ribosomes** | **Protein synthesis**. No membrane |
| **Lysosomes** | **'Suicide bags'**. Hold digestive enzymes |
| **Golgi apparatus** | Packaging and secretion |
| **Endoplasmic reticulum** | Transport. Rough ER (with ribosomes) makes proteins. Smooth ER makes lipids |
| **Chloroplast** | **Photosynthesis**. Plants only. Has its own DNA |
| **Nucleus** | Control centre. Holds the chromosomes (DNA) |
| **Vacuole** | Storage. Large in plant cells |
| **Cell wall** | Plants (**cellulose**) and fungi (**chitin**). Absent in animal cells |

> **Tip:** Four nicknames answer most questions: mitochondria = power, lysosome = suicide bag, ribosome = protein, Golgi = packing.

### Cell types and cell records
- **Prokaryotes** (bacteria, blue-green algae) have **no nuclear membrane** and no membrane-bound organelles.
- **Eukaryotes** have a true nucleus.
- Largest cell: **ostrich egg**. Longest cell: **nerve cell (neuron)**. Smallest cell: **Mycoplasma (PPLO)**.
- The ovum is the largest human cell.
- Mature mammalian **RBCs have no nucleus**. An RBC lives about 120 days. The spleen removes worn-out RBCs.

### Cell division
| | Mitosis | Meiosis |
|---|---|---|
| Purpose | Body growth and repair | Makes **gametes** |
| Cells formed | **2 identical** cells | 4 cells |
| Chromosome number | Stays the same | Halved |

Take a human cell. Mitosis keeps 46. Meiosis gives 23 in each gamete.

### Genetics basics
- **Gregor Mendel** is the **father of genetics**. He worked on the **garden pea** (Pisum sativum).
- His laws are dominance, segregation and independent assortment.
- **DNA double helix**: **Watson and Crick (1953)**, using X-ray data of Rosalind Franklin and Maurice Wilkins.
- DNA bases are A, T, G, C. RNA has **uracil** in place of thymine.

### Human chromosomes and inheritance
Body cells hold **46 chromosomes (23 pairs)**. That is 22 pairs of autosomes plus 1 pair of sex chromosomes. Gametes hold 23.

> **Rule:** The father decides the sex of the child. XX is female. XY is male.

- **Haemophilia** and **colour blindness** are **X-linked**. They are more common in males.
- **Down syndrome** is an extra chromosome 21 (trisomy 21).

### Theories and names to know
- **Hugo de Vries**: mutation theory.
- **Darwin**: natural selection (*On the Origin of Species*, 1859).
- **Lamarck**: inheritance of acquired characters.
- **Har Gobind Khorana**: Nobel Prize 1968 for work on the genetic code.
""",
    tricks=[
        {"title": "Organelle nicknames: Power-Mito, Suicide-Lyso, Protein-Ribo, Packing-Golgi",
         "body": "These four nicknames answer most organelle questions.",
         "example": {"q": "Which organelle is called the 'suicide bag' of the cell?",
                     "steps": ["Suicide points to self-digestion.", "Lysosomes hold digestive enzymes."],
                     "answer": "Lysosome."}},
        {"title": "Cell discoverers in order",
         "body": "Hooke saw the cell (1665, dead cork). Leeuwenhoek saw it alive. Brown saw the nucleus. Schleiden and Schwann made the theory. Virchow said cells come from cells.",
         "example": None},
    ],
    mistakes=[
        mis("Saying Leeuwenhoek discovered the cell.", "Hooke named the cell. Leeuwenhoek first saw living cells."),
        mis("Saying the mother decides the child's sex.", "The father decides it. His sperm carries X or Y."),
        mis("Giving animal cells a cell wall.", "Only plants, fungi and bacteria have one."),
        mis("Thinking meiosis makes two identical cells.", "Mitosis gives 2 identical cells. Meiosis gives 4 cells with half the chromosomes."),
        mis("Saying every cell has a nucleus.", "Prokaryotes have none. Mature mammalian RBCs have none."),
    ],
    revision=[
        "Hooke 1665 cork; Leeuwenhoek living cells; Brown nucleus 1831; Schleiden-Schwann theory; Virchow: cells from cells.",
        "Mitochondria: powerhouse. Lysosome: suicide bag. Ribosome: protein. Golgi: packaging.",
        "Cell wall: cellulose in plants, chitin in fungi. Absent in animal cells.",
        "Largest cell: ostrich egg. Longest: neuron. Smallest: Mycoplasma.",
        "Mitosis: 2 identical cells. Meiosis: gametes, chromosomes halved.",
        "Human: 46 chromosomes (23 pairs). Gamete: 23. Father decides sex.",
        "Mendel: pea. Watson and Crick: DNA 1953. Down syndrome: trisomy 21.",
    ],
    formulas=[],
    patterns=[
        pat("ga-ce-p1", "Cell theory and discoverers", "very common",
            "Words like 'who discovered the cell / nucleus / living cells', 'cell theory', 'omnis cellula e cellula', or a year (1665, 1831).",
            ["Read the noun: cell, living cell, nucleus or theory.", "Match it to its one scientist from the table.", "Use the year to break ties: 1665 Hooke, 1831 Brown."],
            "Each scientist has exactly one signature fact.",
            "The cell theory was proposed by which pair of scientists?",
            ["Theory means Schleiden (plants) and Schwann (animals).", "Hooke only named the cell.", "Virchow added that cells come from cells."],
            "Schleiden and Schwann"),
        pat("ga-ce-p2", "Organelle and its function or nickname", "very common",
            "'Powerhouse of the cell', 'suicide bags', 'which organelle makes protein', 'which organelle has its own DNA'.",
            ["Find the nickname or job in the question.", "Recall the pair from the organelle table.", "For own DNA, choose mitochondria or chloroplast."],
            "The question is always one nickname or one job.",
            "Which organelle is called the 'suicide bag' of the cell?",
            ["Suicide bag means it digests the cell itself.", "Lysosomes hold digestive enzymes."],
            "Lysosome"),
        pat("ga-ce-p3", "Prokaryote vs eukaryote, plant vs animal cell", "common",
            "'Which is a prokaryote', 'no true nucleus', 'cell wall is made of', 'absent in animal cells'.",
            ["Bacteria and blue-green algae are prokaryotes. Everything else is eukaryote.", "Cell wall, chloroplast and large vacuole mark plant cells.", "For 'absent in animal cells', pick cell wall or chloroplast."],
            "Prokaryotes lack a nuclear membrane and membrane-bound organelles.",
            "The cell wall of a plant cell is made of what?",
            ["Plants use cellulose in the wall.", "Fungi use chitin."],
            "Cellulose"),
        pat("ga-ce-p4", "Cell division and chromosome numbers", "common",
            "'Chromosomes in a human body cell', 'chromosomes in a gamete', 'mitosis vs meiosis', 'which division keeps the number the same'.",
            ["Body cell: 46. Gamete: 23.", "Growth and repair means mitosis: the number stays.", "Gamete formation means meiosis: the number halves."],
            "Meiosis halves the number so fertilisation can restore it.",
            "A human gamete contains how many chromosomes?",
            ["A body cell has 46.", "Meiosis halves it: 46 / 2 = 23."],
            "23"),
        pat("ga-ce-p5", "Genetics: Mendel, DNA and inheritance", "common",
            "'Father of genetics', 'DNA double helix', 'Mendel worked on which plant', 'who decides the sex of a child'.",
            ["Match the name to its one fact.", "Mendel is the garden pea. Watson and Crick is 1953.", "Sex: the mother always gives X. The father gives X or Y."],
            "One name, one organism and one year make up the whole question.",
            "Watson and Crick are famous for which work?",
            ["Their year is 1953.", "They built the model of DNA."],
            "The double-helix model of DNA"),
        pat("ga-ce-p6", "Blood cells and cell records", "common",
            "'Which blood cells lack a nucleus', 'lifespan of RBC', 'largest / longest cell', 'which cell carries oxygen'.",
            ["RBC has no nucleus, carries oxygen and lives about 120 days.", "WBC defends. Platelets clot the blood.", "Records: ovum is the largest human cell. Nerve cell is the longest."],
            "Each blood cell has one job.",
            "What is the average lifespan of a human red blood cell?",
            ["RBCs live about 120 days.", "The spleen removes worn-out RBCs."],
            "About 120 days"),
    ],
)

# =====================================================================
# 2. Human body
# =====================================================================
SUBS["bio-human-body"] = dict(
    concept=(
        "This subtopic is a list of standard facts: body records, blood and heart, digestion, hormones and the brain. "
        "Learn each fact as a pair, such as bile and liver or insulin and pancreas. "
        "A few numbers (206 bones, 37 °C, 120/80) are asked again and again."
    ),
    notes=r"""### Body records
These records are asked in almost every paper.

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

> **Watch:** Largest gland is the liver. Largest endocrine gland is the thyroid. Do not mix the two.

### Blood and circulation
An adult has about 5 litres of blood. It has four parts.

| Part | Job |
|---|---|
| **Plasma** (55%) | The liquid part |
| **RBC** | Carries oxygen on haemoglobin |
| **WBC** | Defence |
| **Platelets** | Clotting |

- **Blood groups**: ABO plus Rh. **O− is the universal donor. AB+ is the universal recipient.**
- The **heart** has 4 chambers: 2 atria and 2 ventricles.
- Its natural **pace-maker is the SA node**.
- Humans have **double circulation**. Blood passes through the heart twice per loop.
- A **sphygmomanometer** measures blood pressure. Normal is about **120/80 mm Hg**.
- A resting heart beats about **72 times a minute**.

> **Example:** In one day the heart beats $72 \times 60 \times 24 = 103{,}680$ times. That is about 1 lakh beats.

### Digestive system, organ by organ
| Organ | What it does |
|---|---|
| Mouth | **Salivary amylase** starts starch digestion |
| Stomach | **HCl** and **pepsin** (protein). A mucous lining protects the stomach |
| Liver | Makes **bile**. The gall bladder stores it |
| Pancreas | Sends **trypsin** (protein) and **lipase** (fat) |
| Small intestine | Final digestion and absorption (villi) |
| Large intestine | Absorbs only water |

> **Rule:** Bile has **no enzymes**. It only **emulsifies fat**, which means it breaks fat into tiny drops.

### Endocrine glands and hormones
A hormone is a chemical messenger made by a gland.

| Gland | Hormone and effect |
|---|---|
| **Pituitary** | 'Master gland'. Growth hormone. Too little gives dwarfism, too much gives gigantism |
| **Thyroid** | **Thyroxine** (contains iodine). Deficiency causes **goitre** |
| **Pancreas** | **Insulin** (from the islets of Langerhans) controls blood sugar. Failure is **diabetes** |
| **Adrenal** | Adrenaline, the 'fight-or-flight' hormone |
| Testes / ovaries | Testosterone / estrogen |

### Excretion and the brain
- **Kidneys** filter the blood. Each has about a million **nephrons**.
- Urine holds urea, water and salts. It reaches the bladder.
- **Cerebrum**: thinking. It is the largest part of the brain.
- **Cerebellum**: balance and posture.
- **Medulla oblongata**: involuntary heartbeat and breathing. A spine injury there is fatal.
- The **spinal cord** handles reflex actions without waiting for the brain.

### Body numbers
Body mass index (BMI) tells if weight suits height.

$$\text{BMI} = \dfrac{\text{mass (kg)}}{\text{height (m)}^{2}}$$

The normal range is 18.5 to 24.9 (WHO). Take 54 kg and 1.5 m. Then $\dfrac{54}{1.5^{2}} = 24$, which is normal.

> **Tip:** Convert 37 °C to Fahrenheit with $F = \dfrac{9C}{5} + 32 = 66.6 + 32 = 98.6$.
""",
    tricks=[
        {"title": "Blood group giving: O gives, AB takes",
         "body": "O has no A or B antigens, so it can give to all. AB has no anti-A or anti-B antibodies, so it can take from all.",
         "example": {"q": "The universal recipient blood group is?",
                     "steps": ["AB has no anti-A or anti-B antibodies.", "So it accepts blood from all groups."],
                     "answer": "AB"}},
        {"title": "Brain parts: Cerebrum thinks, Cerebellum balances, Medulla keeps you alive",
         "body": "Thinking and memory: cerebrum. Balance and posture: cerebellum. Heartbeat and breathing: medulla oblongata.",
         "example": None},
    ],
    mistakes=[
        mis("Saying bile contains digestive enzymes.", "Bile has no enzymes. It only emulsifies fats."),
        mis("Answering thyroid for the master gland.", "The master gland is the pituitary."),
        mis("Naming the heart or liver as the largest organ.", "Skin is the largest organ. The liver is the largest gland and internal organ."),
        mis("Answering liver for the largest endocrine gland.", "The largest endocrine gland is the thyroid."),
        mis("Saying bile is made in the gall bladder.", "The liver makes bile. The gall bladder only stores it."),
    ],
    revision=[
        "206 adult bones. Stapes smallest. Femur longest. Skin largest organ. Liver largest gland.",
        "O− universal donor. AB+ universal recipient. SA node is the pace-maker.",
        "BP 120/80 mm Hg (sphygmomanometer). Heart about 72 beats a minute.",
        "Bile: no enzymes, emulsifies fat. Stomach: HCl and pepsin. Villi absorb in the small intestine.",
        "Pituitary: master gland. Thyroxine needs iodine. Insulin from pancreas. Adrenaline: fight-or-flight.",
        "Cerebrum thinks, cerebellum balances, medulla keeps the heart beating.",
        "Body temperature 37 °C = 98.6 °F.",
    ],
    formulas=[
        {"name": "Body mass index", "tex": "\\text{BMI} = \\frac{\\text{mass (kg)}}{\\text{height (m)}^{2}}",
         "note": "Mass in kilograms divided by height in metres squared. 18.5–24.9 is the normal range (WHO)"},
    ],
    patterns=[
        pat("ga-hb-p1", "Body records (largest, smallest, number)", "very common",
            "'Largest gland / organ', 'longest bone', 'smallest bone', 'how many bones does an adult have'.",
            ["Find the record word: largest, smallest or longest.", "Recall it from the records table.", "Test 'largest gland' (liver) against 'largest endocrine gland' (thyroid)."],
            "This is pure recall from one short list.",
            "What is the smallest bone in the human body?",
            ["It sits in the middle ear.", "Its name is stapes."],
            "Stapes"),
        pat("ga-hb-p2", "Blood, groups and circulation", "very common",
            "'Universal donor / recipient', 'which blood cells fight infection', 'pace-maker of the heart', 'BP instrument'.",
            ["RBC carries oxygen. WBC defends. Platelets clot.", "O− gives to all. AB+ takes from all.", "SA node is the pace-maker. Sphygmomanometer measures BP."],
            "Each blood part and each blood group has one role.",
            "Which blood group is the universal recipient?",
            ["Universal recipient means it can take from all groups.", "AB+ has no anti-A or anti-B antibodies."],
            "AB+"),
        pat("ga-hb-p3", "Organ and its secretion or function", "very common",
            "'Insulin is secreted by', 'bile is produced in', 'which organ filters the blood', 'HCl is secreted in'.",
            ["Split the question: made where, stored where.", "Use the digestive table for enzymes.", "Use the brain list for cerebrum, cerebellum and medulla."],
            "Making and storing are different: the liver makes bile, the gall bladder stores it.",
            "Bile, which helps digest fats, is produced by which organ?",
            ["Bile is made in the largest gland.", "The gall bladder only stores it."],
            "Liver"),
        pat("ga-hb-p4", "Hormone, gland and deficiency", "very common",
            "'Insulin / thyroxine / adrenaline is secreted by', 'master gland', 'which hormone controls blood sugar'.",
            ["Match hormone to gland: thyroxine to thyroid, insulin to pancreas.", "Link the hormone to its problem: goitre, diabetes, dwarfism.", "Any corner of gland, hormone and disease can be asked."],
            "Gland, hormone and disease form a fixed triangle.",
            "Which gland is called the master gland?",
            ["Its hormones steer the other glands.", "Growth hormone comes from it."],
            "Pituitary"),
        pat("ga-hb-p5", "Digestion steps and enzymes", "common",
            "'Which enzyme digests protein / starch / fat', 'where is food absorbed', 'function of bile'.",
            ["Amylase acts on starch. Pepsin and trypsin act on protein. Lipase acts on fat.", "The small intestine does final digestion and absorption.", "The large intestine takes only water."],
            "Each enzyme works on one food type.",
            "Digested food is absorbed mainly in which organ?",
            ["Villi increase the surface area.", "They line the small intestine."],
            "Small intestine"),
        pat("ga-hb-p6", "Body numbers (computed)", "common",
            "'How many times does the heart beat in a day', 'normal body temperature in °F', 'how much blood does an adult have'.",
            ["Write the given rate, such as 72 a minute.", "Multiply by 60 and by 24 for a day.", "For temperature use F = 9C/5 + 32."],
            "Split the multiplication into easy steps.",
            "At 72 beats per minute, about how many times does the heart beat in a day?",
            ["72 × 60 = 4,320 beats an hour.", "4,320 × 24 = 103,680."],
            "103,680 (about 1 lakh)"),
    ],
)

# =====================================================================
# 3. Nutrition
# =====================================================================
SUBS["bio-nutrition"] = dict(
    concept=(
        "Vitamins and minerals are needed in small amounts. Lack of each one causes a named disease. "
        "Most questions ask for the pair: the vitamin and its disease, or the mineral and its problem. "
        "A few energy numbers (4, 4 and 9 kcal per gram) come with them."
    ),
    notes=r"""### Vitamin and its deficiency disease
This table is the most asked table in the topic.

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

> **Tip:** Scurvy is C. Rickets is D. These two are the usual swaps in wrong-pair questions.

### Fat-soluble and water-soluble
- **Fat-soluble**: **A, D, E, K**. The body stores them, so too much can harm.
- **Water-soluble**: **B-complex and C**. They wash out daily.
- **Casimir Funk (1912)** coined the word 'vitamine'.
- Sunlight on the skin makes **vitamin D**.
- Cooking destroys vitamin C most easily.

### Minerals and their role
| Mineral | Role or deficiency |
|---|---|
| **Iron** | **Anaemia** (haemoglobin is iron-based) |
| **Iodine** | **Goitre** (thyroxine) |
| **Calcium** | Weak bones and teeth |
| **Phosphorus** | Bones and ATP |
| **Fluorine** | Too little causes dental caries. Too much causes **fluorosis** |
| **Sodium, potassium** | Nerve and muscle function |
| Zinc | Wound healing and immunity |

> **Watch:** Fluorine harms in both directions: too little and too much.

### Malnutrition: the two classics
| | Kwashiorkor | Marasmus |
|---|---|---|
| Lacks | Protein (calories are adequate) | Protein **and** calories |
| Look | Swollen belly, oedema, thin limbs | All skin and bones |
| Age | 1 to 3 years | Under one year |

> **Rule:** Kwashiorkor is swollen. Marasmus is shrunken.

Obesity is the opposite imbalance. **Roughage** (fibre) prevents constipation.

### Food energy
| Component | Energy |
|---|---|
| Carbohydrate | **4 kcal/g** |
| Protein | **4 kcal/g** |
| Fat | **9 kcal/g** |

Fat gives more than twice the energy per gram. A **30 g** fat snack gives $30 \times 9 = 270$ kcal.

> **Example:** A snack has 20 g fat and 10 g carbohydrate. Energy is $20 \times 9 + 10 \times 4 = 180 + 40 = 220$ kcal.

A balanced diet splits the calories roughly into 60% carbohydrates, 25 to 30% fat and 10 to 15% protein. **Basal metabolic rate (BMR)** is the energy burnt at rest. An adult needs about 2,000 to 2,500 kcal a day.
""",
    tricks=[
        {"title": "Fat-soluble vitamins: KADE (or ADEK)",
         "body": "A, D, E and K dissolve in fat and are stored in the body. B and C dissolve in water.",
         "example": None},
        {"title": "Deficiency pairs: A-Andha (night blind), B1-Beriberi, C-sCurvy, D-Deformed bones (rickets), K-Klotting",
         "body": "Add B3 with Pellagra ('3 D's) and B12 with Pernicious anaemia (cobalt).",
         "example": {"q": "Deficiency of which vitamin causes beriberi?",
                     "steps": ["Beriberi starts with B.", "It goes with thiamine."],
                     "answer": "Vitamin B1 (thiamine)"}},
    ],
    mistakes=[
        mis("Linking scurvy to vitamin D.", "Scurvy is vitamin C. Rickets is vitamin D."),
        mis("Calling vitamin C fat-soluble.", "It is water-soluble and cooking heat destroys it."),
        mis("Mixing up kwashiorkor and marasmus.", "Kwashiorkor lacks protein only. Marasmus lacks protein and calories."),
        mis("Saying fat gives 4 kcal per gram.", "Fat gives 9 kcal per gram. Carbohydrate and protein give 4."),
        mis("Treating fluorine as harmless in large amounts.", "Too much fluorine causes fluorosis. Too little causes caries."),
    ],
    revision=[
        "A night blindness, B₁ beriberi, B₃ pellagra, B₁₂ pernicious anaemia, C scurvy, D rickets, E sterility, K clotting.",
        "Fat-soluble: A, D, E, K. Water-soluble: B and C.",
        "'Vitamine' was coined by Casimir Funk. Vitamin D comes from sunlight.",
        "Iron gives anaemia, iodine gives goitre, calcium gives bones, fluorine gives caries or fluorosis.",
        "Kwashiorkor: protein lack, swollen. Marasmus: protein and calories lack, shrunken.",
        "Energy: carbohydrate 4, protein 4, fat 9 kcal per gram.",
    ],
    formulas=[],
    patterns=[
        pat("ga-nu-p1", "Vitamin and deficiency disease", "very common",
            "'Scurvy is caused by deficiency of', 'rickets', 'beriberi', 'night blindness', 'pernicious anaemia'.",
            ["Read the disease name.", "Find it in the vitamin table.", "Check D with rickets and C with scurvy first."],
            "The pairs are fixed, so no reasoning is needed.",
            "Pernicious anaemia is caused by the deficiency of which vitamin?",
            ["Pernicious anaemia goes with cobalt.", "The vitamin is cyanocobalamin."],
            "Vitamin B₁₂"),
        pat("ga-nu-p2", "Vitamin sources and solubility", "very common",
            "'Which vitamins are fat-soluble', 'made in the skin by sunlight', 'rich source of vitamin C'.",
            ["Fat-soluble means A, D, E, K.", "Sunlight on skin makes vitamin D.", "Cooking destroys vitamin C the most."],
            "The body stores fat-soluble vitamins and washes out the rest.",
            "Which set contains only fat-soluble vitamins?",
            ["Recall the word KADE.", "The set is A, D, E, K."],
            "A, D, E, K"),
        pat("ga-nu-p3", "Mineral and deficiency or role", "common",
            "'Goitre is due to deficiency of', 'anaemia is caused by lack of', 'which mineral builds bones and teeth'.",
            ["Iron gives anaemia.", "Iodine gives goitre.", "Calcium and phosphorus build bones and teeth."],
            "Each mineral has one headline role.",
            "Anaemia (low haemoglobin) most commonly results from deficiency of which mineral?",
            ["Haemoglobin is an iron pigment.", "Less iron means less oxygen carried."],
            "Iron"),
        pat("ga-nu-p4", "Malnutrition: kwashiorkor vs marasmus", "common",
            "'Kwashiorkor is caused by', 'swollen belly disease of children', 'difference between kwashiorkor and marasmus'.",
            ["Swollen belly and oedema means kwashiorkor.", "Skin and bones means marasmus.", "Kwashiorkor lacks protein. Marasmus lacks protein and calories."],
            "Swollen against shrunken separates the two.",
            "A child with a swollen belly but adequate calorie intake suffers from what?",
            ["The swelling is oedema.", "Only protein is lacking."],
            "Kwashiorkor"),
        pat("ga-nu-p5", "Food energy values (computed)", "common",
            "'How much energy does 1 g of fat give', a snack's total calories from given grams.",
            ["Recall: carbohydrate 4, protein 4, fat 9 kcal per gram.", "Multiply each part by its value.", "Add the parts."],
            "Fat gives the most energy per gram.",
            "A snack has 25 g carbohydrate, 10 g protein and 10 g fat. What is its energy?",
            ["Carbohydrate: 25 × 4 = 100.", "Protein: 10 × 4 = 40.", "Fat: 10 × 9 = 90.", "Total: 100 + 40 + 90."],
            "230 kcal"),
        pat("ga-nu-p6", "Vitamin history and chemical names", "occasional",
            "'Who coined the word vitamin', 'which vitamin is ascorbic acid', chemical names of vitamins.",
            ["Casimir Funk coined 'vitamine' in 1912.", "Match the chemical name from the table.", "Ascorbic acid means scurvy means vitamin C."],
            "The chemical name is often a giveaway for the disease.",
            "The word 'vitamine' was coined by whom?",
            ["He coined it in 1912.", "His name is Casimir Funk."],
            "Casimir Funk (1912)"),
    ],
)

# =====================================================================
# 4. Diseases
# =====================================================================
SUBS["bio-diseases"] = dict(
    concept=(
        "Every common disease belongs to one pathogen type: bacteria, virus, protozoa or fungus. "
        "Many are carried by one named vector, such as a mosquito or fly. "
        "Add the vaccine and the scientist who found it, and most questions are covered."
    ),
    notes=r"""### Disease and pathogen type
A pathogen is a germ that causes disease. Sort each disease into its group first.

| Type | Diseases |
|---|---|
| **Bacteria** | **TB, cholera, typhoid, tetanus, leprosy, plague, whooping cough, anthrax** |
| **Virus** | **Dengue, chikungunya, rabies, polio, measles, mumps, AIDS, COVID-19, smallpox, influenza, jaundice (hepatitis)** |
| **Protozoa** | **Malaria, kala-azar, amoebiasis (dysentery), sleeping sickness** |
| **Fungus** | **Ringworm, athlete's foot** |

> **Tip:** The bacterial six are cholera, typhoid, TB, tetanus, leprosy and plague. The viral five are dengue, rabies, polio, measles and AIDS.

### Vectors: who carries what
A vector is a living carrier of a pathogen.

| Vector | Disease |
|---|---|
| **Female Anopheles** | **Malaria** (Plasmodium) |
| **Aedes aegypti** | **Dengue, chikungunya, zika** |
| **Culex** | **Filariasis or elephantiasis** (Wuchereria bancrofti) |
| **Sandfly** | **Kala-azar** (Leishmania) |
| **Tsetse fly** | **Sleeping sickness** (Trypanosoma) |
| **Rat flea** | **Plague** |

Only the female mosquito bites.

> **Watch:** AIDS is never spread by mosquitoes. It spreads only by blood, unsafe sex and shared needles.

### Vaccines, antibiotics and discoverers
| Scientist | Contribution |
|---|---|
| **Edward Jenner** | First **vaccine**: smallpox, 1796. 'Vaccine' comes from 'vacca', cow |
| **Louis Pasteur** | Germ theory, pasteurisation, **rabies vaccine** |
| **Robert Koch** | **TB bacterium** (Mycobacterium tuberculosis), also anthrax and cholera |
| **Alexander Fleming** | **Penicillin, 1928**, the first antibiotic (mould *Penicillium notatum*) |
| Florey and Chain | Made penicillin into a medicine |
| **Banting and Best (1921)** | **Insulin** for diabetes |
| **Ronald Ross** | Proved mosquitoes carry malaria (worked in India, Nobel 1902) |
| **Joseph Lister** | **Antiseptic surgery** (carbolic acid) |

### Key numbers and controls
- Smallpox was the first disease **eradicated**. WHO declared it in **1980**.
- **BCG** vaccine protects against TB. **MMR** covers measles, mumps and rubella.
- Polio drops belong to the **Pulse Polio** campaign.
- Cholera, typhoid and jaundice spread through contaminated **water and food**.
- Safe drinking water and vaccination are the cheapest shields.

### Scale words
| Word | Meaning |
|---|---|
| **Endemic** | Always present in a local area |
| **Epidemic** | Outbreak in a region |
| **Pandemic** | Worldwide outbreak (COVID-19) |

### Blood values and disorders
- Normal haemoglobin is about **12 to 16 g/dL**. Low haemoglobin is **anaemia**.
- Normal RBC count is about 5 million per mm³. WBC is about 6,000 to 8,000 per mm³.
- An RBC lives about 120 days.
- **Thalassaemia** and **sickle-cell anaemia** are genetic blood disorders. They do not spread from person to person.

> **Note:** Antibiotics act only on bacteria. They do not cure viral infections.
""",
    tricks=[
        {"title": "Bacterial diseases: TB, Cholera, Typhoid, Diphtheria, Tetanus, Leprosy, Plague, Pertussis",
         "body": "A disease in this list is bacterial. Polio, measles, AIDS, dengue, rabies, chickenpox and hepatitis are viral. Malaria and kala-azar are protozoan.",
         "example": {"q": "Which of these is a viral disease: typhoid, cholera, measles, tetanus?",
                     "steps": ["Typhoid, cholera and tetanus are bacterial.", "Measles is on the viral list."],
                     "answer": "Measles"}},
        {"title": "Mosquito map: Anopheles-Malaria, Aedes-Dengue, Culex-Filaria",
         "body": "Aedes also spreads chikungunya, yellow fever and Zika (day-biting). Only the female mosquito bites for blood.",
         "example": None},
    ],
    mistakes=[
        mis("Calling malaria a bacterial or viral disease.", "Malaria is protozoan (Plasmodium)."),
        mis("Crediting Pasteur with the smallpox vaccine.", "Jenner made it. Pasteur made the rabies vaccine."),
        mis("Thinking antibiotics cure viral infections.", "Antibiotics act only on bacteria."),
        mis("Thinking ringworm is caused by a worm.", "Ringworm is a fungal infection."),
        mis("Saying mosquitoes spread AIDS.", "AIDS spreads only by blood, unsafe sex and shared needles."),
    ],
    revision=[
        "Bacterial six: TB, cholera, typhoid, tetanus, leprosy, plague. Viral five: dengue, rabies, polio, measles, AIDS.",
        "Protozoa: malaria, kala-azar, amoebiasis, sleeping sickness. Fungus: ringworm, athlete's foot.",
        "Anopheles: malaria. Aedes: dengue. Culex: elephantiasis. Sandfly: kala-azar. Tsetse: sleeping sickness. Rat flea: plague.",
        "Jenner: smallpox vaccine 1796. Pasteur: rabies. Koch: TB. Fleming: penicillin 1928. Banting and Best: insulin.",
        "Smallpox eradicated 1980. BCG for TB. Pandemic means worldwide.",
        "Haemoglobin 12 to 16 g/dL. Thalassaemia and sickle-cell are genetic.",
    ],
    formulas=[],
    patterns=[
        pat("ga-di-p1", "Disease and pathogen type", "very common",
            "'TB is caused by a', 'which is a viral / protozoan disease', 'ringworm is caused by'.",
            ["Name the disease.", "Find its group: bacteria, virus, protozoa or fungus.", "Check the options against that group."],
            "Classify the disease first, then eliminate options.",
            "Ringworm is caused by which type of pathogen?",
            ["It is not a worm.", "It is a skin infection of a fungus."],
            "Fungus"),
        pat("ga-di-p2", "Vector and disease", "very common",
            "'Dengue is spread by which mosquito', 'malaria is transmitted by', 'which fly causes sleeping sickness'.",
            ["Recall the vector table.", "Anopheles gives malaria, Aedes gives dengue, Culex gives filariasis.", "Remember only the female mosquito bites."],
            "Each vector carries one family of disease.",
            "Elephantiasis (filariasis) is transmitted by which vector?",
            ["The worm is Wuchereria bancrofti.", "Its carrier is the Culex mosquito."],
            "Culex mosquito"),
        pat("ga-di-p3", "Vaccines and eradication", "common",
            "'BCG protects against', 'first vaccine', 'which disease was eradicated', 'MMR'.",
            ["BCG is for TB. MMR is for measles, mumps and rubella.", "Jenner's smallpox vaccine came in 1796.", "Smallpox was eradicated in 1980."],
            "The vaccine word root and the eradication year are the most repeated facts.",
            "Which was the first disease eradicated worldwide?",
            ["WHO declared it in 1980.", "Jenner's 1796 vaccine fought it."],
            "Smallpox"),
        pat("ga-di-p4", "Scientist and medicine or discovery", "common",
            "'Penicillin was discovered by', 'who discovered the TB bacterium', 'pasteurisation', 'insulin'.",
            ["Fleming: penicillin 1928.", "Koch: TB bacterium. Pasteur: germ theory, rabies vaccine.", "Banting and Best: insulin 1921."],
            "Do not mix Koch, the bacteriologist, with Pasteur.",
            "Penicillin, the first antibiotic, was discovered by whom?",
            ["It came from the mould Penicillium notatum.", "The year was 1928."],
            "Alexander Fleming"),
        pat("ga-di-p5", "Epidemic words and lifestyle diseases", "common",
            "'A disease spread worldwide is a', 'diabetes is caused by lack of', 'AIDS is caused by'.",
            ["Local and constant is endemic. Regional is epidemic. Worldwide is pandemic.", "Diabetes means lack of insulin from the pancreas.", "AIDS does not spread by touch or mosquitoes."],
            "Scale words differ only by how far the disease spreads.",
            "COVID-19 spread across the world in 2020. What is such an outbreak called?",
            ["It crossed countries and continents.", "That is beyond an epidemic."],
            "Pandemic"),
        pat("ga-di-p6", "Health numbers and blood disorders", "occasional",
            "'Normal haemoglobin range', 'lifespan of RBC', 'sickle-cell is a', 'thalassaemia'.",
            ["Haemoglobin: 12 to 16 g/dL.", "RBC life: 120 days.", "Sickle-cell and thalassaemia are genetic blood disorders."],
            "Learn the normal values. The disorders hang off them.",
            "The average lifespan of a red blood cell is how long?",
            ["Recall the normal value.", "The spleen removes old cells."],
            "120 days"),
    ],
)

# =====================================================================
# 5. Plants and classification
# =====================================================================
SUBS["bio-plants-classification"] = dict(
    concept=(
        "This subtopic covers how living things are named and grouped, plant hormones, photosynthesis "
        "and which part of a plant we eat. Each item is a one-word pair. "
        "Learn the pairs in small groups, such as roots together and stems together."
    ),
    notes=r"""### Classification: the ladder
**Carolus Linnaeus** is the **father of taxonomy**. He gave **binomial nomenclature**, a two-word scientific name of genus plus species, written in italics. Example: *Mangifera indica*.

**R.H. Whittaker (1969)** gave the **five-kingdom** system.

1. **Monera**
2. **Protista**
3. **Fungi**
4. **Plantae**
5. **Animalia**

Earlier systems used two kingdoms: plants and animals.

Plants divide into two big groups.

| Group | Meaning | Examples |
|---|---|---|
| **Cryptogams** | Seedless | Algae, fungi, bryophytes, pteridophytes |
| **Phanerogams** | Seed plants | Gymnosperms (naked seed), angiosperms (seed inside fruit) |

### Monocot and dicot
| | Monocot | Dicot |
|---|---|---|
| Seed leaves | One | Two |
| Leaf veins | **Parallel** | **Reticulate** (net-like) |
| Roots | Fibrous | Taproot |
| Examples | Wheat, rice, maize | Mango, pea, gram |

> **Tip:** Parallel veins mean monocot. Net-like veins mean dicot.

### Plant hormones
| Hormone | Job |
|---|---|
| **Auxin** | Cell elongation. Bending to light (**phototropism**) |
| **Gibberellin** | Stem elongation. Seed germination |
| **Cytokinin** | Cell division. Delays leaf ageing |
| **Ethylene** (gas) | **Fruit ripening** |
| **Abscisic acid** | Stress hormone. Closes stomata. Promotes wilting and dormancy |

### Photosynthesis and transport
Photosynthesis happens in the **chloroplast**, which holds the green pigment **chlorophyll**. Sunlight drives it.

$$6CO_2 + 6H_2O \rightarrow C_6H_{12}O_6 + 6O_2$$

> **Rule:** The oxygen released comes from water, not from carbon dioxide.

- Leaves exchange gases through **stomata**.
- **Transpiration** pulls water up the xylem.
- Phloem carries food.
- Excess water vapour escapes mainly through the lower surface of the leaf.

### Edible parts of plants
| Plant | Edible part |
|---|---|
| Carrot, radish, beetroot, turnip | **Root** |
| Potato, ginger, turmeric, onion (bulb), sugarcane | **Stem (modified)** |
| Cabbage, spinach, lettuce | **Leaves** |
| Cauliflower, broccoli | **Flower** |
| Tomato, brinjal, pumpkin, cucumber | **Fruit** |
| Groundnut, gram, mustard, rice, wheat | **Seed** |
| Apple, cashew | Fleshy **thalamus** (accessory fruit) |

> **Watch:** Potato, ginger, turmeric and onion grow underground but are stems. Sweet potato is a true root.

### Reproduction and scientific names
Vegetative propagation uses runners and bulbs. People add **grafting, layering, cutting and tissue culture**. Wind pollinates maize and wheat, which have light dry pollen. Insects visit bright petals with nectar.

| Organism | Scientific name |
|---|---|
| Mango | *Mangifera indica* |
| Neem | *Azadirachta indica* |
| Banyan | *Ficus benghalensis* |
| Tamarind | *Tamarindus indica* |
| Potato | *Solanum tuberosum* |
| Rice | *Oryza sativa* |
| Tiger | *Panthera tigris* |
| Frog | *Rana tigrina* |
""",
    tricks=[
        {"title": "Underground but not a root",
         "body": "Potato, ginger, turmeric and onion grow underground but are stems. They have nodes or buds (eyes). Carrot, radish, sweet potato and beetroot are true roots.",
         "example": {"q": "The edible part of ginger is?",
                     "steps": ["Ginger has nodes and buds.", "So it is not a root."],
                     "answer": "A modified stem (rhizome)"}},
        {"title": "Five kingdoms: My Pet Fish Plays Alone",
         "body": "Monera, Protista, Fungi, Plantae, Animalia. Whittaker, 1969.",
         "example": None},
    ],
    mistakes=[
        mis("Calling sweet potato a stem and potato a root.", "Potato is a stem. Sweet potato is a root."),
        mis("Saying the oxygen from photosynthesis comes from CO₂.", "It comes from water."),
        mis("Calling the bat a bird or the whale a fish.", "Both are mammals."),
        mis("Placing bacteria in the kingdom Plantae.", "Bacteria belong to Monera."),
        mis("Giving Linnaeus credit for the five-kingdom system.", "Linnaeus gave binomial names. Whittaker gave five kingdoms."),
    ],
    revision=[
        "Linnaeus: binomial nomenclature, father of taxonomy. Whittaker: 5 kingdoms (1969).",
        "Monocot: one seed leaf, parallel veins. Dicot: two, reticulate veins.",
        "Auxin: elongation and phototropism. Gibberellin: stem. Cytokinin: division. Ethylene: ripening. ABA: stress.",
        "Carrot root, potato, ginger and onion stem, cabbage leaf, cauliflower flower, tomato fruit, groundnut seed.",
        "Photosynthesis: 6CO₂ + 6H₂O gives glucose + 6O₂. Stomata: gas exchange. Xylem: water. Phloem: food.",
    ],
    formulas=[
        {"name": "Photosynthesis", "tex": "6CO_2 + 6H_2O \\xrightarrow[\\text{chlorophyll}]{\\text{sunlight}} C_6H_{12}O_6 + 6O_2",
         "note": "O₂ comes from water. Inputs are carbon dioxide and water. Outputs are glucose and oxygen"},
        {"name": "Aerobic respiration", "tex": "C_6H_{12}O_6 + 6O_2 \\rightarrow 6CO_2 + 6H_2O + \\text{energy (ATP)}",
         "note": "The reverse of photosynthesis in terms of matter. It releases energy as ATP"},
    ],
    patterns=[
        pat("ga-pl-p1", "Classification history and systems", "very common",
            "'Who gave binomial nomenclature', 'five-kingdom classification', 'which kingdom does a bacterium belong to'.",
            ["Linnaeus: binomial names. Whittaker: five kingdoms.", "Bacteria go in Monera.", "Cryptogams have no seeds. Phanerogams have seeds."],
            "One scientist gave one system.",
            "The five-kingdom classification was proposed by whom?",
            ["The five kingdoms are Monera, Protista, Fungi, Plantae, Animalia.", "The year was 1969."],
            "R.H. Whittaker"),
        pat("ga-pl-p2", "Edible part of the plant", "very common",
            "'Potato is a modified', 'carrot is which plant part', 'onion is a modified'.",
            ["Name the food.", "Find its group in the edible-parts table.", "Watch the trap: potato is a stem, sweet potato is a root."],
            "Recall works best by family: roots together, stems together.",
            "The potato we eat is a modified what?",
            ["It grows underground.", "It has eyes, which are buds."],
            "Stem (tuber)"),
        pat("ga-pl-p3", "Plant hormones", "very common",
            "'Which hormone ripens fruits', 'bending towards light', 'stress hormone of plants'.",
            ["Ripening: ethylene.", "Bending to light: auxin.", "Wilting and stress: abscisic acid."],
            "Three one-word answers cover most questions.",
            "Which plant hormone is responsible for fruit ripening?",
            ["This hormone is a gas.", "It is ethylene."],
            "Ethylene"),
        pat("ga-pl-p4", "Photosynthesis and transport", "common",
            "'Which gas is released in photosynthesis', 'which pigment absorbs light', 'xylem carries', 'stomata'.",
            ["Inputs: CO₂ and water. Outputs: glucose and oxygen.", "Chlorophyll in chloroplasts absorbs light.", "Xylem carries water up. Phloem carries food."],
            "The equation gives every answer.",
            "In photosynthesis, which gas do plants release?",
            ["Read the right side of the equation.", "The gas comes from water."],
            "Oxygen"),
        pat("ga-pl-p5", "Monocot vs dicot and reproduction", "common",
            "'Which is a monocot', 'parallel venation', 'pollination by wind', 'grafting'.",
            ["Parallel veins and fibrous roots mean monocot.", "Wheat, rice and maize are monocots.", "Grafting, layering, cutting and tissue culture are vegetative propagation."],
            "Vein pattern separates monocots from dicots.",
            "A plant shows parallel venation. Which group is it?",
            ["Parallel veins point to one seed leaf.", "Examples are wheat and maize."],
            "Monocot"),
        pat("ga-pl-p6", "Scientific names and firsts", "common",
            "'The scientific name of mango / neem / rice', match the column of plants and binomials.",
            ["Recall the two-word name.", "The first word is genus, the second is species.", "Both are italic."],
            "Linnaeus set the two-word rule.",
            "What is the scientific name of mango?",
            ["Genus is Mangifera.", "Species is indica."],
            "Mangifera indica"),
    ],
)

# =====================================================================
# 6. Branches and ecology
# =====================================================================
SUBS["bio-branches-ecology"] = dict(
    concept=(
        "Most questions here decode a word: ornithology is birds, sericulture is silk. "
        "The rest are ecology facts: the food chain, the 10% energy rule, and India's conservation firsts. "
        "Learn the word roots and the dates in small clusters."
    ),
    notes=r"""### Branches of study
The word ending -ology means the study of. The front part tells you what.

| Branch | Studies |
|---|---|
| **Ornithology** | **Birds** |
| **Entomology** | **Insects** |
| **Ichthyology** | **Fishes** |
| **Herpetology** | **Reptiles and amphibians** |
| **Mycology** | **Fungi** |
| **Virology** | Viruses |
| **Cytology** | Cells |
| **Histology** | Tissues |
| **Oncology** | Cancer |
| **Cardiology** | Heart |
| **Ophthalmology** | Eye |
| **Anthology** | Flowers |

Apiology is bees. Malacology is molluscs.

> **Watch:** Entomology is insects. Etymology is the study of word origins.

### Culture words: rearing living things
| Word | Rears or grows |
|---|---|
| **Apiculture** | Honeybees (honey) |
| **Sericulture** | Silkworms (silk) |
| **Pisciculture** | Fish |
| **Aquaculture** | Water organisms |
| **Horticulture** | Garden plants |
| **Floriculture** | Flowers |
| **Vermiculture** | Earthworms |
| **Silviculture** | Forest trees |
| **Poultry** | Fowl |

> **Tip:** Decode the root: api is bee, seri is silk, pisci is fish, vermi is worm, silvi is forest.

### Colour revolutions in India
- **Green**: food grain. M.S. Swaminathan in India. Norman Borlaug worldwide.
- **White**: milk. **Verghese Kurien**, Operation Flood.
- **Blue**: fish.
- **Yellow**: oilseeds.

### Ecosystem and the 10% law
An **ecosystem** is a living community plus its physical surroundings.

The food chain runs in one direction.

1. **Producers** (green plants)
2. **Herbivores** (primary consumers)
3. **Carnivores** (secondary and tertiary consumers)

**Decomposers** (bacteria and fungi) recycle nutrients. A **food web** is many chains linked together.

> **Rule:** Lindeman's 10% law says only about 10% of energy passes to the next level.

$$E_n = E_1 \times (0.1)^{n-1}$$

Here $E_1$ is the producer energy and $n$ is the level. Take 10,000 J at the producers. The herbivores get 1,000 J. Small carnivores get 100 J. Big carnivores get 10 J.

Energy flows one way. Nutrients cycle. **Bioaccumulation** makes toxins build up along the chain.

### Cycles and conservation
- **Nitrogen cycle**: soil nitrogen goes to plants, then animals, then back to soil. **Rhizobium** bacteria in legume root nodules fix the nitrogen.
- The **carbon cycle** ties together respiration, photosynthesis and fuels.
- **Jim Corbett National Park (1936)** is India's first national park.
- **Project Tiger** began in 1973.
- The **Chipko movement (1973)**: villagers hugged trees to save them.
- The **IUCN Red List** ranks threatened species (extinct, vulnerable, least concern). The **Red Data Book** records them.
- Ramsar sites are wetlands.

### Pollution and milestones
- Air pollutants: CO, SO₂, NOₓ and particulates.
- **BOD** (biochemical oxygen demand) measures water pollution. Higher BOD means dirtier water.
- ***Silent Spring*** (Rachel Carson, 1962) warned against pesticides like **DDT**.
- **Dolly the sheep (1996)** was the first cloned mammal.
- **Norman Borlaug** is the father of the Green Revolution.
- **Salim Ali** is the birdman of India.
""",
    tricks=[
        {"title": "Culture words by root",
         "body": "Api is bee (apiary). Seri is silk. Pisci is fish (Pisces). Viti is vine or grapes. Pomo is fruit (pomegranate). Olera is vegetables.",
         "example": {"q": "Sericulture is the rearing of what?",
                     "steps": ["Seri means silk.", "Silk comes from silkworms."],
                     "answer": "Silkworms"}},
        {"title": "Study-of roots",
         "body": "Ornitho is bird. Ento is insect. Ichthyo is fish. Herpeto is creeping animals. Myco is fungus. Phyco is seaweed or algae. Onco is tumour. Nephro is kidney.",
         "example": None},
    ],
    mistakes=[
        mis("Confusing entomology (insects) with etymology (word origins).", "Entomology is insects."),
        mis("Mixing up pisciculture (fish) and pomology (fruits).", "Pisci means fish. Pomo means fruit."),
        mis("Saying energy cycles in an ecosystem.", "Energy flows one way. Nutrients cycle."),
        mis("Reading 10% law as 90% passing on.", "Only 10% passes to the next level. The rest is lost."),
        mis("Giving Swaminathan credit for the White Revolution.", "White Revolution (milk) is Verghese Kurien. Swaminathan is Green."),
    ],
    revision=[
        "Ornithology birds, entomology insects, ichthyology fish, herpetology reptiles, mycology fungi, oncology cancer.",
        "Apiculture bees, sericulture silk, pisciculture fish, vermiculture worms, silviculture trees.",
        "10% law (Lindeman): 10,000, 1,000, 100, 10 J up the chain.",
        "Corbett 1936 first park. Project Tiger 1973. Chipko 1973. Dolly the sheep 1996.",
        "Green: Swaminathan and Borlaug. White: Kurien. Blue: fish. Yellow: oilseeds.",
        "Rhizobium fixes nitrogen in legume nodules. Higher BOD means dirtier water.",
    ],
    formulas=[
        {"name": "10% law of energy transfer", "tex": "E_{n} = E_{1} \\times (0.1)^{\\,n-1}",
         "note": "E₁ = energy at the producer level, n = trophic level. Each step keeps one tenth"},
    ],
    patterns=[
        pat("ga-br-p1", "Branch of study and organism", "very common",
            "'Ornithology is the study of', 'entomology', 'ichthyology', 'herpetology', 'study of cancer'.",
            ["Split the word into root and -ology.", "Recall the root: ornitho is bird, ento is insect.", "Kill the trap: entomology is not etymology."],
            "Root plus -ology gives the answer.",
            "Entomology is the study of what?",
            ["Ento means insect.", "Etymology is a different word."],
            "Insects"),
        pat("ga-br-p2", "Culture or rearing word and creature", "very common",
            "'Sericulture is associated with', 'apiculture', 'pisciculture', 'vermiculture'.",
            ["Split the word: root plus culture.", "Api is bee, seri is silk, pisci is fish, vermi is worm.", "Silvi means forest trees."],
            "Each word is a Latin root plus culture.",
            "Sericulture is the rearing of what?",
            ["Seri means silk.", "Silk comes from silkworms."],
            "Silkworms"),
        pat("ga-br-p3", "Food chain and the 10% law (computed)", "common",
            "'Producers trap 10,000 J, energy at the third level', 'the 10% law was given by', 'primary consumers'.",
            ["Count the levels from the producers as level 1.", "Multiply by 0.1 once for each step.", "Third level means two steps."],
            "Each step keeps only a tenth.",
            "Producers store 10,000 J. By the 10% law, how much energy reaches the third trophic level?",
            ["Level 1: 10,000 J.", "Level 2 (herbivores): 1,000 J.", "Level 3 (small carnivores): 100 J."],
            "100 J"),
        pat("ga-br-p4", "Conservation firsts and biodiversity", "common",
            "'First national park of India', 'Project Tiger was launched in', 'Chipko movement', 'IUCN Red List'.",
            ["Jim Corbett: 1936, first park.", "Project Tiger and Chipko: 1973.", "Red Data Book and IUCN list threatened species."],
            "Names and years come in fixed pairs.",
            "India's first national park (1936) is which park?",
            ["It was set up in 1936.", "Project Tiger began here in 1973."],
            "Jim Corbett National Park"),
        pat("ga-br-p5", "Colour revolutions and scientists", "common",
            "'White Revolution is related to', 'father of the Green Revolution', 'birdman of India'.",
            ["Match the colour to the produce first.", "Then attach the name.", "Salim Ali is the birdman. Rachel Carson wrote Silent Spring."],
            "Colour first, name second.",
            "The White Revolution (Operation Flood) in India is associated with what?",
            ["White means milk.", "Verghese Kurien led it."],
            "Milk production"),
        pat("ga-br-p6", "Ecology basics and pollution measures", "occasional",
            "'BOD measures', 'which organisms are decomposers', 'food web is', 'bioaccumulation'.",
            ["BOD: higher value means more polluted water.", "Decomposers are bacteria and fungi.", "Toxins like DDT build up along the food chain."],
            "Ecology terms have short fixed meanings.",
            "BOD of a water sample indicates what?",
            ["More organic waste means bacteria use more oxygen.", "So higher BOD means dirtier water."],
            "Its pollution level"),
    ],
)


# ---------------------------------------------------------------- patch JSON
data = json.loads(TOPIC.read_text(encoding="utf-8"))
by_id = {s["id"]: s for s in data["subtopics"]}
assert set(SUBS) == set(by_id), set(SUBS) ^ set(by_id)
all_ids = [p["id"] for s in SUBS.values() for p in s["patterns"]]
assert len(all_ids) == len(set(all_ids))
for sid, new in SUBS.items():
    sub = by_id[sid]
    old = {p["id"] for p in sub.get("patterns", [])}
    assert old <= {p["id"] for p in new["patterns"]}, (sid, old)
    n = new["notes"].strip() + "\n"
    sub.update(concept=new["concept"], notes=n, patterns=new["patterns"], mistakes=new["mistakes"],
               revision=new["revision"], tricks=new["tricks"], formulas=new["formulas"])
    print(f"{sid}: notes {len(n)} chars, {len(new['patterns'])} patterns (was {len(old)})")
with open(TOPIC, "w", encoding="utf-8", newline="\n") as f:
    json.dump(data, f, ensure_ascii=False, indent=1)
    f.write("\n")
