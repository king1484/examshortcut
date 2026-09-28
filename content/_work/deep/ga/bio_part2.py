"""biology deep content — part 2: bio-diseases, bio-plants-classification, bio-branches-ecology."""
import os
import sys

sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
from _lib import Sub


def build_diseases():
    S = Sub("bio-diseases")
    S.notes = """### Disease → pathogen type
| Type | Diseases |
|---|---|
| **Bacteria** | **TB, cholera, typhoid, tetanus, leprosy, plague, whooping cough, anthrax** |
| **Virus** | **Dengue, chikungunya, rabies, polio, measles, mumps, AIDS, COVID-19, smallpox, influenza, jaundice (hepatitis)** |
| **Protozoa** | **Malaria, kala-azar, amoebiasis (dysentery), sleeping sickness** |
| **Fungus** | **Ringworm, athlete's foot** |
Memory hook: cholera–typhoid–TB–tetanus–leprosy–plague travel together as the bacterial six; dengue–rabies–polio–measles–AIDS as the viral five.

### Vectors — who carries what
**Female Anopheles** → **malaria** (Plasmodium). **Aedes aegypti** → **dengue, chikungunya, zika**. **Culex** → **filariasis/elephantiasis** (Wuchereria bancrofti). **Sandfly** → **kala-azar** (Leishmania). **Tsetse fly** → **sleeping sickness** (Trypanosoma). **Rat flea** → **plague**. Only the female mosquito bites. AIDS is NOT spread by mosquitoes — only by blood, unsafe sex and shared needles.

### Vaccines, antibiotics and the discoverers
**Edward Jenner** — the first **vaccine** (smallpox, 1796; the word comes from 'vacca', cow). **Louis Pasteur** — germ theory, pasteurisation, **rabies vaccine**. **Robert Koch** — the **TB bacterium** (Mycobacterium tuberculosis), also anthrax and cholera. **Alexander Fleming** — **penicillin, 1928**, the first antibiotic (mould *Penicillium notatum*); florey and Chain made it a medicine. **Banting and Best (1921)** — **insulin** for diabetes. **Ronald Ross** proved malaria is carried by mosquitoes (worked in India; Nobel 1902).

### Key numbers and controls
- Smallpox: the first disease **eradicated** — WHO declared it in **1980**.
- **BCG** vaccine → TB; **MMR** → measles-mumps-rubella; polio drops → **Pulse Polio** campaign.
- Normal haemoglobin ≈ **12–16 g/dL**; low → **anaemia**; genetic blood disorders: **thalassaemia, sickle-cell anaemia**.
- **Epidemic** = outbreak in a region; **pandemic** = worldwide (COVID-19); **endemic** = always present locally.
- Diseases spread through contaminated **water and food** (cholera, typhoid, jaundice) — safe drinking water and vaccination are the cheapest shields; **Joseph Lister** introduced **antiseptic surgery** (carbolic acid).

### Quick revision
- Bacterial six: TB, cholera, typhoid, tetanus, leprosy, plague. Viral five: dengue, rabies, polio, measles, AIDS. Protozoa: malaria, kala-azar, amoebiasis, sleeping sickness.
- Anopheles–malaria, Aedes–dengue, Culex–elephantiasis, sandfly–kala-azar, tsetse–sleeping sickness, rat flea–plague.
- Jenner smallpox vaccine 1796; Pasteur rabies; Koch TB; Fleming penicillin 1928; Banting & Best insulin.
- Smallpox eradicated 1980; BCG–TB; AIDS never by mosquitoes."""
    S.pattern("ga-di-p1", "Disease → pathogen type", "very common",
        "'Tuberculosis is caused by a…', 'which of these is a viral / protozoan disease', 'ringworm is caused by…', odd-one-out among disease types.",
        None,
        "1. Bacterial set: TB, cholera, typhoid, tetanus, leprosy, plague, whooping cough, anthrax.\n2. Viral set: dengue, chikungunya, rabies, polio, measles, mumps, AIDS, influenza, hepatitis, smallpox, COVID-19.\n3. Protozoa: malaria, kala-azar, amoebiasis, sleeping sickness. Fungus: ringworm, athlete's foot.\n4. Odd-one-out trick: dengue is VIRAL, malaria is PROTOZOAN — both mosquito-borne, different microbes.\nWhy: classify the disease first, then check the options against its set.",
        "**Ringworm** is caused by a —",
        "**Fungus** (not a worm, despite the name). Athlete's foot is the other classic fungal infection.")
    S.pattern("ga-di-p2", "Vector → disease", "very common",
        "'Dengue is spread by which mosquito', 'malaria is transmitted by…', 'which fly causes sleeping sickness', 'elephantiasis is carried by…'.",
        None,
        "1. Mosquito map: female **Anopheles → malaria**; **Aedes → dengue, chikungunya, zika**; **Culex → filariasis (elephantiasis)**.\n2. Other vectors: sandfly → kala-azar; tsetse fly → sleeping sickness; rat flea → plague.\n3. Only female mosquitoes bite (they need blood for eggs). AIDS never travels by mosquito.\nWhy: each vector has exactly one disease family — pair them and eliminate.",
        "**Elephantiasis** (filariasis) is transmitted by —",
        "**Culex mosquito**, carrying the worm *Wuchereria bancrofti*. Aedes gives dengue, Anopheles gives malaria.")
    S.pattern("ga-di-p3", "Vaccines and eradication", "common",
        "'BCG protects against…', 'first vaccine / who invented vaccination', 'which disease was eradicated', 'MMR stands for', Pulse Polio questions.",
        None,
        "1. Vaccine map: BCG–TB, MMR–measles/mumps/rubella, polio drops–Pulse Polio, rabies vaccine–Pasteur.\n2. History: **Jenner, smallpox, 1796** — the first vaccine ('vacca' = cow); smallpox the first **eradicated** disease (WHO, 1980).\n3. 'Vaccine' word root and the eradication year are the two most-repeated facts.",
        "The first disease to be **eradicated** worldwide (WHO, 1980) was —",
        "**Smallpox**. Jenner's 1796 cowpox vaccine against it started immunology — 'vaccine' from *vacca*, cow.")
    S.pattern("ga-di-p4", "Scientist → medicine/discovery", "very common",
        "'Penicillin was discovered by…', 'who discovered the TB bacterium', 'pasteurisation / germ theory', 'insulin was discovered by', 'who proved mosquitoes spread malaria'.",
        None,
        "1. Fleming — penicillin (1928, from *Penicillium* mould). Koch — TB, cholera, anthrax bacteria. Pasteur — germ theory, pasteurisation, rabies vaccine.\n2. Banting and Best — insulin (1921). Ronald Ross — mosquito-malaria link (Nobel 1902, work done in India).\n3. Don't mix Koch (bacteriologist) with Pasteur (the wider germ theorist).",
        "**Penicillin**, the first antibiotic, was discovered by —",
        "**Alexander Fleming** in 1928, from the mould *Penicillium notatum*. Florey and Chain later turned it into a usable drug.")
    S.pattern("ga-di-p5", "Epidemic vocabulary and lifestyle diseases", "common",
        "'A disease spread worldwide is a…', 'diabetes is caused by deficiency of…', 'AIDS is caused by / spread by', 'epidemic vs endemic vs pandemic'.",
        None,
        "1. Scale words: endemic–local and constant; epidemic–regional outbreak; pandemic–worldwide (COVID-19, 1918 flu).\n2. Diabetes: insulin deficiency (pancreas) — sugar stays in the blood. AIDS: HIV destroys helper T-cells; spread by blood/sex/needles, NOT touch or mosquitoes.\n3. Cancer = uncontrolled cell division; hypertension = persistent high BP.",
        "**COVID-19** spread across the world in 2020. Such a worldwide outbreak is called a —",
        "**Pandemic** — an epidemic that crosses countries and continents. Endemic diseases stay local; epidemics stay regional.")
    S.pattern("ga-di-p6", "Health numbers and blood disorders", "occasional",
        "'Normal haemoglobin range', 'normal WBC count', 'lifespan of RBC', 'sickle-cell / thalassaemia is a … disorder', questions that need 120 × counts.",
        None,
        "1. Normal values: haemoglobin 12–16 g/dL; RBC ≈ 5 million/mm³; WBC ≈ 6,000–8,000/mm³; platelets ≈ 1.5–4 lakh/mm³; RBC life 120 days.\n2. Genetic blood disorders: thalassaemia and sickle-cell anaemia — inherited, not infectious.\n3. Low haemoglobin = anaemia (iron); abnormal WBC rise = leukaemia.\nWhy: memorise the three normal ranges; disorders hang off them.",
        "The average lifespan of a **red blood cell** is —",
        "**120 days**; the spleen recycles the worn-out cells (its nickname: graveyard of RBCs).")

    S.q("ga-di-p1", "easy", "**Tuberculosis** is caused by a —",
        ["Bacterium", "Virus", "Protozoan", "Fungus"], "Bacterium",
        "**Mycobacterium tuberculosis** — a bacterium, identified by Robert Koch. BCG vaccination protects against it.",
        None, 15)
    S.q("ga-di-p1", "medium", "Which of these is a **protozoan** disease?",
        ["Malaria", "Dengue", "Tuberculosis", "Ringworm"], "Malaria",
        "**Malaria** — the parasite *Plasmodium* is a protozoan. Dengue is viral, TB bacterial, ringworm fungal.",
        None, 15)
    S.q("ga-di-p1", "medium", "**Cholera** and **typhoid** are caused by —",
        ["Bacteria", "Viruses", "Protozoa", "Worms"], "Bacteria",
        "Both are **bacterial**, water/food-borne: *Vibrio cholerae* and *Salmonella typhi* — the classic unsafe-water pair.",
        None, 15)
    S.q("ga-di-p2", "easy", "**Dengue** is transmitted by the —",
        ["Aedes mosquito", "Anopheles mosquito", "Culex mosquito", "Housefly"], "Aedes mosquito",
        "**Aedes aegypti** carries dengue (and chikungunya, zika) — it bites by day. Anopheles gives malaria.",
        None, 15)
    S.q("ga-di-p2", "easy", "**Malaria** is spread by the bite of —",
        ["Female Anopheles mosquito", "Male Anopheles mosquito", "Aedes mosquito", "Tsetse fly"], "Female Anopheles mosquito",
        "The **female Anopheles** injects *Plasmodium*; Ronald Ross proved the link in India. Only female mosquitoes bite.",
        None, 15)
    S.q("ga-di-p2", "medium", "**Sleeping sickness** is transmitted by the —",
        ["Tsetse fly", "Sandfly", "Rat flea", "Housefly"], "Tsetse fly",
        "The **tsetse fly** (African) carries *Trypanosoma*. The sandfly gives kala-azar; the rat flea, plague.",
        None, 15)
    S.q("ga-di-p2", "medium", "**Kala-azar** (visceral leishmaniasis) is spread by the —",
        ["Sandfly", "Aedes mosquito", "Tsetse fly", "Rat flea"], "Sandfly",
        "The **sandfly** carries the protozoan *Leishmania*. Fever with spleen enlargement is the signature.",
        None, 15)
    S.q("ga-di-p3", "easy", "The **BCG vaccine** protects against —",
        ["Tuberculosis", "Polio", "Measles", "Typhoid"], "Tuberculosis",
        "**BCG (Bacillus Calmette-Guérin)** — given at birth against TB. Polio drops and MMR cover the other diseases.",
        None, 15)
    S.q("ga-di-p3", "medium", "The **first vaccine** ever developed was against —",
        ["Smallpox", "Rabies", "Polio", "TB"], "Smallpox",
        "**Edward Jenner, 1796**, against smallpox — from 'vacca' (cow) comes the word vaccine. Smallpox was also the first eradicated disease.",
        None, 15)
    S.q("ga-di-p3", "medium", "The **MMR vaccine** protects against —",
        ["Measles, mumps and rubella", "Malaria, measles and rabies", "Mumps, meningitis and rubella", "Measles, mumps and rhinitis"], "Measles, mumps and rubella",
        "**MMR = measles, mumps, rubella** (German measles) — a live-virus shot given in childhood.",
        None, 15)
    S.q("ga-di-p4", "easy", "**Penicillin** was discovered by —",
        ["Alexander Fleming", "Louis Pasteur", "Edward Jenner", "Robert Koch"], "Alexander Fleming",
        "**Fleming, 1928** — noticed mould killing bacteria in a forgotten dish. Pasteur gave germ theory; Jenner, the first vaccine.",
        None, 15)
    S.q("ga-di-p4", "medium", "The bacterium causing **tuberculosis** was discovered by —",
        ["Robert Koch", "Louis Pasteur", "Alexander Fleming", "Joseph Lister"], "Robert Koch",
        "**Robert Koch** — the TB bacillus (1882), plus anthrax and cholera bacteria. Pasteur is the wider germ-theory man.",
        None, 15)
    S.q("ga-di-p4", "medium", "**Insulin** was discovered by —",
        ["Banting and Best", "Fleming and Florey", "Koch and Pasteur", "Watson and Crick"], "Banting and Best",
        "**Frederick Banting and Charles Best (1921)** isolated insulin — turning diabetes from a death sentence into a manageable condition.",
        None, 15)
    S.q("ga-di-p5", "medium", "A disease outbreak restricted to one **region** is an —",
        ["Epidemic", "Pandemic", "Endemic", "Sporadic"], "Epidemic",
        "**Epidemic** = regional outbreak; **pandemic** = worldwide (COVID-19); **endemic** = permanently local (malaria in some districts).",
        None, 15)
    S.q("ga-di-p5", "medium", "**AIDS** is NOT transmitted by —",
        ["Mosquito bite", "Blood transfusion", "Shared needles", "Mother to child"], "Mosquito bite",
        "HIV travels in blood and body fluids — never by mosquito bite, touch or shared meals. The virus destroys helper T-cells.",
        None, 15)
    S.q("ga-di-p6", "medium", "The average lifespan of a human **red blood cell** is —",
        ["120 days", "20 days", "1 year", "10 days"], "120 days",
        "**120 days** — the spleen then recycles them, hence its nickname 'graveyard of RBCs'.",
        None, 15)
    S.q("ga-di-p6", "medium", "**Sickle-cell anaemia** is a —",
        ["Genetic (inherited) disorder", "Bacterial infection", "Viral infection", "Dietary deficiency only"], "Genetic (inherited) disorder",
        "It is **inherited** — a gene fault makes RBCs sickle-shaped, so they clog capillaries. Thalassaemia is the other famous genetic blood disorder.",
        None, 15)
    return S


def build_plants():
    S = Sub("bio-plants-classification")
    S.notes = """### Classification — the ladder
**Carolus Linnaeus**, the **father of taxonomy**, gave **binomial nomenclature** (two-word scientific name: genus + species, in italics — *Mangifera indica*). **R.H. Whittaker (1969)** gave the **five-kingdom** classification: **Monera, Protista, Fungi, Plantae, Animalia** (earlier: two kingdoms, plants and animals). Plants divide into **cryptogams** (seedless — algae, fungi, bryophytes, pteridophytes) and **phanerogams** (seed plants — gymnosperms, naked seed; angiosperms, seed inside fruit). **Monocots** (wheat, rice, maize): one seed leaf, **parallel** leaf veins, fibrous roots. **Dicots** (mango, pea, gram): two seed leaves, **reticulate** veins, taproot.

### Plant hormones
**Auxin** — cell elongation, bending to light (**phototropism**). **Gibberellin** — stem elongation, seed germination. **Cytokinin** — cell division, delays leaf ageing. **Ethylene (gas)** — **fruit ripening**. **Abscisic acid** — the stress hormone: closes stomata, promotes wilting and dormancy.

### Photosynthesis and transport
Photosynthesis in the **chloroplast** (green pigment **chlorophyll**): **6CO₂ + 6H₂O → C₆H₁₂O₆ + 6O₂** in sunlight. Leaves exchange gases through **stomata**; **transpiration** pulls water up the xylem (phloem carries food). Excess water vapour escapes mainly through the leaf's lower surface.

### Edible parts — the exam favourite
| Plant | Edible part |
|---|---|
| Carrot, radish, beetroot, turnip | **Root** |
| Potato, ginger, turmeric, onion (bulb), sugarcane | **Stem (modified)** |
| Cabbage, spinach, lettuce | **Leaves** |
| Cauliflower, broccoli | **Flower** |
| Tomato, brinjal, pumpkin, cucumber | **Fruit** |
| Groundnut, gram, mustard, rice, wheat | **Seed** |
| Apple, cashew | Fleshy **thalamus** (accessory fruit) |

### Reproduction and scientific names
Vegetative propagation: runners, bulbs, and human-made **grafting, layering, cutting, tissue culture**. Pollination agents: wind (maize, wheat — light dry pollen), water, insects (bright petals, nectar). Common scientific names: mango **Mangifera indica**, neem **Azadirachta indica**, banyan **Ficus benghalensis**, tamarind **Tamarindus indica**, potato **Solanum tuberosum**, rice **Oryza sativa**, tiger **Panthera tigris**, frog **Rana tigrina**.

### Quick revision
- Linnaeus = binomial nomenclature, father of taxonomy; Whittaker = 5 kingdoms (1969).
- Monocot: one cotyledon, parallel veins; dicot: two, reticulate veins.
- Auxin–elongation/phototropism; gibberellin–stem; cytokinin–division; ethylene–ripening; ABA–stress.
- Carrot root, potato/ginger/onion stem, cabbage leaf, cauliflower flower, tomato fruit, groundnut seed.
- Photosynthesis: 6CO₂ + 6H₂O → glucose + 6O₂; stomata = gas exchange; xylem water, phloem food."""
    S.pattern("ga-pl-p1", "Classification history and systems", "very common",
        "'Who gave binomial nomenclature / five-kingdom classification', 'which kingdom does a bacterium belong to', two-kingdom vs five-kingdom, cryptogam vs phanerogam.",
        None,
        "1. **Linnaeus** — binomial nomenclature, father of taxonomy (species plantarum, 1753). **Whittaker (1969)** — five kingdoms: Monera, Protista, Fungi, Plantae, Animalia.\n2. Bacteria sit in **Monera** (prokaryotes); moulds and mushrooms in Fungi.\n3. Cryptogams = seedless (algae to ferns); phanerogams = seed-bearing (gymnosperms naked seed, angiosperms covered).\nWhy: one scientist = one system; the kingdom of bacteria is the standard trap.",
        "The **five-kingdom** classification was proposed by —",
        "**R.H. Whittaker (1969)** — Monera, Protista, Fungi, Plantae, Animalia. Linnaeus earlier gave binomial nomenclature.")
    S.pattern("ga-pl-p2", "Edible part of the plant", "very common",
        "'Potato is a modified…', 'carrot is which plant part', 'onion is a modified…', match-the-column of plants and their edible parts.",
        None,
        "1. Roots: carrot, radish, beetroot, turnip, sweet potato.\n2. Stems: potato (tuber), ginger/turmeric (rhizome), onion/garlic (bulb), sugarcane.\n3. Leaves: cabbage, spinach, lettuce. Flower: cauliflower, broccoli. Fruit: tomato, brinjal, pumpkin. Seed: groundnut, gram, mustard.\n4. The double trap: sweet potato is a ROOT, ordinary potato a STEM; onion is a bulb (stem with fleshy leaves).\nWhy: recall by family groups — roots cluster, stems cluster, one fruit list.",
        "The **potato** we eat is a modified —",
        "**Stem** — an underground tuber with 'eyes' (buds). Sweet potato, despite the name, is a modified root.")
    S.pattern("ga-pl-p3", "Plant hormones", "very common",
        "'Which hormone ripens fruits', 'which hormone causes bending towards light', 'stress hormone of plants', 'which hormone promotes cell division'.",
        None,
        "1. Auxin — elongation, phototropism (bending to light). Gibberellin — stem length, germination. Cytokinin — cell division, delays ageing.\n2. **Ethylene (a gas) — fruit ripening**; abscisic acid — stress, stomatal closure, wilting.\n3. Ripening = ethylene; bending = auxin; wilting = ABA — three fixed one-word answers.",
        "The plant hormone responsible for **fruit ripening** is —",
        "**Ethylene** — the only gaseous plant hormone. Ripening bananas release it, so they can ripen other fruit kept nearby.")
    S.pattern("ga-pl-p4", "Photosynthesis and transport", "common",
        "'Which gas is released in photosynthesis', 'which pigment absorbs light', 'xylem carries…', 'stomata are found on…', photosynthesis word equation.",
        None,
        "1. 6CO₂ + 6H₂O → C₆H₁₂O₆ + 6O₂ — inputs CO₂ + water, outputs glucose + **oxygen**; pigment = **chlorophyll** in chloroplasts.\n2. **Xylem** carries water/minerals up; **phloem** carries food both ways.\n3. **Stomata** (mostly on the leaf's lower surface) do gas exchange and transpiration.",
        "In photosynthesis, plants **release** —",
        "**Oxygen**, splitting water in the chloroplast: 6CO₂ + 6H₂O → glucose + 6O₂ in sunlight.")
    S.pattern("ga-pl-p5", "Monocot vs dicot and reproduction", "common",
        "'Which is a monocot', 'parallel venation indicates…', 'pollination by insects / wind', 'grafting is a method of…', number of cotyledons.",
        None,
        "1. Monocots — wheat, rice, maize, onion: one cotyledon, parallel veins, fibrous roots. Dicots — mango, pea, gram, sunflower: two cotyledons, reticulate veins, taproot.\n2. Insect pollination: bright petals + nectar + scent (mustard, rose). Wind: light dry pollen (maize, wheat).\n3. Grafting, layering, cutting, tissue culture = vegetative (asexual) propagation.",
        "Which of these shows **parallel venation** (a monocot)?",
        "**Maize/wheat/rice/onion** — monocots have parallel veins and fibrous roots; mango and pea are dicots with net-like veins.")
    S.pattern("ga-pl-p6", "Scientific names and firsts", "common",
        "'The scientific name of mango / neem / rice', match-the-column of plants and binomials, father-of-taxonomy questions.",
        None,
        "1. Mango *Mangifera indica*; neem *Azadirachta indica*; banyan *Ficus benghalensis*; tamarind *Tamarindus indica*.\n2. Potato *Solanum tuberosum*; rice *Oryza sativa*; wheat *Triticum aestivum*; cat *Felis catus*; tiger *Panthera tigris*.\n3. First word = genus (capital), second = species (small), both italic — the binomial rule of Linnaeus.",
        "The scientific name of **mango** is —",
        "***Mangifera indica*** — genus *Mangifera*, species *indica*. Neem is *Azadirachta indica*.")

    S.q("ga-pl-p1", "easy", "The **five-kingdom** classification was proposed by —",
        ["R.H. Whittaker", "Carolus Linnaeus", "Ernst Haeckel", "Aristotle"], "R.H. Whittaker",
        "**Whittaker (1969)**: Monera, Protista, Fungi, Plantae, Animalia. Linnaeus gave binomial nomenclature.",
        None, 15)
    S.q("ga-pl-p1", "medium", "Who is called the **father of taxonomy**?",
        ["Carolus Linnaeus", "Charles Darwin", "Aristotle", "Whittaker"], "Carolus Linnaeus",
        "**Linnaeus** — he introduced binomial nomenclature (*Species Plantarum*, 1753): a two-word scientific name for every organism.",
        None, 15)
    S.q("ga-pl-p1", "medium", "In the five-kingdom system, **bacteria** belong to the kingdom —",
        ["Monera", "Protista", "Fungi", "Plantae"], "Monera",
        "**Monera** holds the prokaryotes — bacteria and blue-green algae. Protista is single-celled eukaryotes like Amoeba.",
        None, 15)
    S.q("ga-pl-p2", "easy", "The **potato** is a modified —",
        ["Stem", "Root", "Leaf", "Flower"], "Stem",
        "An underground **stem tuber** — the 'eyes' are buds. Sweet potato is the root; the two are the classic pair.",
        None, 15)
    S.q("ga-pl-p2", "easy", "**Carrot** is an example of an edible —",
        ["Root", "Stem", "Fruit", "Leaf"], "Root",
        "**Taproot**, swollen with stored food — like radish, beetroot, turnip. Ginger is the stem-side answer.",
        None, 15)
    S.q("ga-pl-p2", "medium", "The **onion bulb** is mainly a modified —",
        ["Stem with fleshy leaves", "Root", "Fruit", "Flower"], "Stem with fleshy leaves",
        "A **bulb** — a compressed underground stem ringed by fleshy scale leaves. Garlic is its cousin.",
        None, 20)
    S.q("ga-pl-p2", "medium", "Which part of the plant do we eat in **cauliflower**?",
        ["Flower", "Leaf", "Stem", "Root"], "Flower",
        "Cauliflower (and broccoli) is a cluster of **undeveloped flower buds**. Cabbage is the leaf; the tomato a fruit.",
        None, 15)
    S.q("ga-pl-p3", "easy", "The plant hormone that **ripens fruit** is —",
        ["Ethylene", "Auxin", "Gibberellin", "Cytokinin"], "Ethylene",
        "**Ethylene** — a gas; a ripe banana in a closed box ripens the raw fruit beside it. Auxin elongates; ABA stresses.",
        None, 15)
    S.q("ga-pl-p3", "medium", "Bending of a shoot **towards light** (phototropism) is caused by —",
        ["Auxin", "Ethylene", "Abscisic acid", "Cytokinin"], "Auxin",
        "**Auxin** collects on the shaded side and elongates those cells, so the shoot bends toward light. ABA instead closes stomata under stress.",
        None, 15)
    S.q("ga-pl-p3", "medium", "Which hormone promotes **cell division** in plants?",
        ["Cytokinin", "Ethylene", "Abscisic acid", "Auxin"], "Cytokinin",
        "**Cytokinin** — it drives cell division and delays leaf ageing (coconut water is rich in it). Gibberellin stretches stems.",
        None, 15)
    S.q("ga-pl-p4", "easy", "The gas **released during photosynthesis** is —",
        ["Oxygen", "Carbon dioxide", "Nitrogen", "Hydrogen"], "Oxygen",
        "6CO₂ + 6H₂O → C₆H₁₂O₆ + 6O₂ — the oxygen comes from splitting water. Respiration consumes oxygen instead.",
        None, 15)
    S.q("ga-pl-p4", "medium", "Which tissue carries **water** upward from the roots?",
        ["Xylem", "Phloem", "Stomata", "Cambium"], "Xylem",
        "**Xylem** = water and minerals, upward; **phloem** = food, both directions. Stomata are pores, not transport tissue.",
        None, 15)
    S.q("ga-pl-p4", "medium", "The green pigment essential for photosynthesis is —",
        ["Chlorophyll", "Haemoglobin", "Melanin", "Carotene"], "Chlorophyll",
        "**Chlorophyll** in the chloroplasts traps sunlight; it is the reason leaves are green.",
        None, 15)
    S.q("ga-pl-p5", "medium", "Which of these is a **monocot** plant?",
        ["Wheat", "Mango", "Pea", "Gram"], "Wheat",
        "**Wheat** (and rice, maize, onion) — one seed leaf, parallel veins. Mango, pea and gram are dicots.",
        None, 15)
    S.q("ga-pl-p5", "medium", "**Grafting** is a method of —",
        ["Vegetative (asexual) propagation", "Sexual reproduction", "Pollination", "Seed dispersal"], "Vegetative (asexual) propagation",
        "A stem scion is joined to a rooted stock — no seeds, so the fruit keeps the parent's quality (mango, rose). Layering and cutting are its cousins.",
        None, 15)
    S.q("ga-pl-p6", "medium", "The scientific name of **neem** is —",
        ["Azadirachta indica", "Mangifera indica", "Ficus benghalensis", "Oryza sativa"], "Azadirachta indica",
        "***Azadirachta indica***. Mango is *Mangifera indica*, banyan *Ficus benghalensis*, rice *Oryza sativa*.",
        None, 15)
    S.q("ga-pl-p6", "medium", "In binomial nomenclature, the **first word** of the scientific name denotes the —",
        ["Genus", "Species", "Family", "Order"], "Genus",
        "Genus first (capitalised), species second (small), both in italics — e.g. *Mangifera indica*. The rule is Linnaeus's.",
        None, 15)
    return S


def build_ecology():
    S = Sub("bio-branches-ecology")
    S.notes = """### Branches of study — the -ology table
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
Trap pair: en**tom**ology = insects (not etymology — words). Apiology = bees; malacology = molluscs.

### Culture words — rearing living things
**Apiculture** = honeybees (honey). **Sericulture** = silkworms (silk). **Pisciculture** = fish. **Aquaculture** = water organisms. **Horticulture** = garden plants. **Floriculture** = flowers. **Vermiculture** = earthworms. **Silviculture** = forest trees. **Poultry** farming = fowl. India's colour revolutions: **Green** — food grain (M.S. Swaminathan in India; Norman Borlaug worldwide), **White** — milk (**Verghese Kurien**, Operation Flood), **Blue** — fish, **Yellow** — oilseeds.

### Ecosystem and the 10% law
An **ecosystem** = living community + its physical surroundings. Food chain: **producers** (green plants) → **herbivores** (primary consumers) → **carnivores** (secondary, tertiary). **Lindeman's 10% law**: only about **10% of energy passes to the next level** — 10,000 J of producers gives 1,000 J to herbivores, 100 J to small carnivores, 10 J to big ones. **Decomposers** (bacteria, fungi) recycle nutrients. A **food web** is interlinked chains; **bioaccumulation** makes toxins concentrate up the chain.

### Cycles, conservation, biodiversity
**Nitrogen cycle**: soil nitrogen → plants (via **Rhizobium** bacteria in legume root nodules) → animals → back to soil. **Carbon cycle** ties respiration, photosynthesis and fuels. Conservation firsts: **Jim Corbett National Park (1936)** — India's first; **Project Tiger (1973)**; **Chipko movement (1973)** — villagers hugging trees. **IUCN Red List** ranks threatened species (extinct → vulnerable → least concern); the **Red Data Book** records them. Ramsar sites = wetlands.

### Pollution and milestones
Air: CO, SO₂, NOₓ, particulates; **BOD** (biochemical oxygen demand) measures water pollution — higher BOD, dirtier water. **Silent Spring** (Rachel Carson, 1962) warned against pesticides like **DDT**. Cloning milestone: **Dolly the sheep (1996)**, first cloned mammal. **Norman Borlaug** = father of the Green Revolution; **Salim Ali** = the birdman of India.

### Quick revision
- Ornithology–birds, entomology–insects, ichthyology–fish, herpetology–reptiles, mycology–fungi, oncology–cancer.
- Apiculture–bees, sericulture–silk, pisciculture–fish, vermiculture–worms, silviculture–trees.
- 10% law (Lindeman): 10,000 → 1,000 → 100 → 10 J up the chain.
- Corbett 1936 first park; Project Tiger 1973; Chipko 1973; Dolly the sheep 1996.
- Green–Swaminathan/Borlaug, White–Kurien, Blue–fish; Rhizobium fixes nitrogen in legume nodules."""
    S.pattern("ga-br-p1", "Branch of study → organism", "very common",
        "'Ornithology is the study of…', 'entomology / ichthyology / herpetology / mycology', 'study of cancer / heart / eye', odd-one-out among -ology branches.",
        None,
        "1. Animals: ornithology–birds, entomology–insects, ichthyology–fishes, herpetology–reptiles+amphibians, apiology–bees.\n2. Micro/inner: mycology–fungi, virology–viruses, cytology–cells, histology–tissues.\n3. Medical: oncology–cancer, cardiology–heart, ophthalmology–eye, nephrology–kidney.\n4. Kill the trap: entomology is insects, NOT etymology (words).\nWhy: root + animal = answer; cluster-learn five at a time.",
        "**Entomology** is the study of —",
        "**Insects**. Don't confuse with etymology (word origins). Ichthyology is fish; ornithology, birds.")
    S.pattern("ga-br-p2", "Culture/rearing word ↔ creature", "very common",
        "'Sericulture is associated with…', 'apiculture / pisciculture / vermiculture', 'which culture is for flowers', match-the-column of cultures.",
        None,
        "1. Apiculture–bees (honey); sericulture–silkworms (silk); pisciculture–fish; aquaculture–water organisms.\n2. Horticulture–gardens; floriculture–flowers; vermiculture–earthworms; silviculture–trees.\n3. Root logic helps: api- (bee), seri- (silk), pisci- (fish), vermi- (worm), silvi- (forest).\nWhy: each word is Latin root + culture; decode the root when unsure.",
        "**Sericulture** is the rearing of —",
        "**Silkworms** for silk production. Apiculture keeps bees, pisciculture fish.")
    S.pattern("ga-br-p3", "Food chain and the 10% law (computed)", "very common",
        "'Producers trap 10,000 J, energy at the third level', 'the 10% law was given by…', 'which are primary consumers', 'energy flow is always…'.",
        None,
        "1. Chain: producers → primary (herbivores) → secondary → tertiary; energy flows one way, decreasing.\n2. **Lindeman's 10% law**: keep chopping a zero — 10,000 J → 1,000 J (2nd level) → 100 J (3rd) → 10 J (4th) → 1 J (5th).\n3. 'Third trophic level' = second consumer = small carnivores: 100 J from a 10,000 J base. Count levels, not names.",
        "Producers store **10,000 J**. By the 10% law, the energy reaching the **third trophic level** is —",
        "10,000 → 1,000 (herbivores) → **100 J** (small carnivores). Each step keeps only a tenth.")
    S.pattern("ga-br-p4", "Conservation firsts and biodiversity", "common",
        "'First national park of India', 'Project Tiger was launched in…', 'Chipko movement', 'IUCN Red List', 'which bacteria fix nitrogen in legumes'.",
        None,
        "1. Jim Corbett (1936) = first national park; Project Tiger (1973); Chipko movement (1973, tree-hugging, Sunderlal Bahuguna).\n2. IUCN Red List + Red Data Book = threatened species records; Ramsar = wetlands.\n3. **Rhizobium** in legume root nodules fixes atmospheric nitrogen — the natural fertiliser.",
        "India's **first national park** (1936) is —",
        "**Jim Corbett National Park** (Uttarakhand; originally Hailey). Project Tiger began there in 1973.")
    S.pattern("ga-br-p5", "Colour revolutions and scientists", "common",
        "'White Revolution is related to…', 'father of the Green Revolution', 'who is the birdman of India', 'Blue Revolution'.",
        None,
        "1. Green–food grain (M.S. Swaminathan in India; Norman Borlaug worldwide); White–milk (Verghese Kurien, Operation Flood); Blue–fish; Yellow–oilseeds.\n2. Salim Ali = birdman of India; Rachel Carson = *Silent Spring* (DDT warning); Dolly the sheep (1996) = first cloned mammal.\n3. Pair the colour with the produce first, then attach the name.",
        "The **White Revolution** (Operation Flood) in India is associated with —",
        "**Milk production**, led by **Verghese Kurien** (Amul). Green was food grain, Blue was fish.")
    S.pattern("ga-br-p6", "Ecology basics and pollution measures", "common",
        "'BOD measures…', 'which organisms are decomposers', 'ozone layer position', 'food web is…', 'bioaccumulation'.",
        None,
        "1. **BOD** (biochemical oxygen demand) — higher value = more polluted water.\n2. Decomposers = bacteria and fungi recycling nutrients; food web = many interlinked food chains.\n3. Pollutants like DDT **bioaccumulate** up the food chain — top predators get the most.\n4. Ozone layer sits in the stratosphere; CFCs were its destroyer (Montreal Protocol, 1987).",
        "**BOD** (biochemical oxygen demand) of a water sample indicates —",
        "Its **pollution level**: more organic waste means bacteria consume more oxygen, so a HIGHER BOD means dirtier water.")

    S.q("ga-br-p1", "easy", "**Ornithology** is the study of —",
        ["Birds", "Insects", "Fishes", "Reptiles"], "Birds",
        "**Ornithology = birds** (Salim Ali, the birdman of India, was its greatest name here). Entomology is insects.",
        None, 15)
    S.q("ga-br-p1", "medium", "**Ichthyology** is the study of —",
        ["Fishes", "Birds", "Fungi", "Cells"], "Fishes",
        "**Ichthyology = fishes**. Mycology is fungi; cytology, cells; histology, tissues.",
        None, 15)
    S.q("ga-br-p1", "medium", "**Mycology** is the study of —",
        ["Fungi", "Viruses", "Muscles", "Soil"], "Fungi",
        "**Mycology = fungi** — yeasts, moulds, mushrooms. Virology studies viruses.",
        None, 15)
    S.q("ga-br-p1", "medium", "**Oncology** is the branch of medicine dealing with —",
        ["Cancer", "Heart", "Kidney", "Eye"], "Cancer",
        "**Oncology = cancer** study and treatment. Cardiology–heart, nephrology–kidney, ophthalmology–eye.",
        None, 15)
    S.q("ga-br-p2", "easy", "**Apiculture** is associated with the rearing of —",
        ["Honeybees", "Silkworms", "Fishes", "Earthworms"], "Honeybees",
        "**Apiculture = bee-keeping** for honey and wax. Sericulture is silkworms; pisciculture, fish.",
        None, 15)
    S.q("ga-br-p2", "easy", "**Sericulture** is related to —",
        ["Silk production", "Fish farming", "Flower growing", "Poultry"], "Silk production",
        "**Sericulture** rears silkworms on mulberry leaves to produce raw silk.",
        None, 15)
    S.q("ga-br-p2", "medium", "**Pisciculture** deals with —",
        ["Fish farming", "Bee-keeping", "Forest trees", "Earthworms"], "Fish farming",
        "**Pisciculture = fish culture** (the Blue Revolution). Vermiculture rears earthworms; silviculture, trees.",
        None, 15)
    S.q("ga-br-p3", "hard", "Producers in a food chain trap **10,000 J** of energy. By the **10% law**, the energy at the **third trophic level** is —",
        ["100 J", "1,000 J", "10 J", "1 J"], "100 J",
        "10% each step: 10,000 → **1,000 J** (primary consumers) → **100 J** (secondary carnivores = 3rd level) → 10 J (4th).",
        None, 25)
    S.q("ga-br-p3", "medium", "The **10% law** of energy flow in ecosystems was given by —",
        ["Lindeman", "Odum", "Darwin", "Tansley"], "Lindeman",
        "**Raymond Lindeman** — only about a tenth of the energy passes to the next trophic level. Odum wrote the classic ecology textbook; Tansley coined 'ecosystem'.",
        None, 20)
    S.q("ga-br-p3", "medium", "In a food chain, **green plants** are called —",
        ["Producers", "Consumers", "Decomposers", "Predators"], "Producers",
        "**Producers** — they make food by photosynthesis and feed the whole chain; animals are consumers, bacteria and fungi the decomposers.",
        None, 15)
    S.q("ga-br-p4", "medium", "India's **first national park**, set up in 1936, is —",
        ["Jim Corbett National Park", "Kaziranga National Park", "Gir National Park", "Kanha National Park"], "Jim Corbett National Park",
        "**Jim Corbett** (Uttarakhand, first named Hailey) — 1936. Kaziranga holds rhinos, Gir the lions, Kanha tigers.",
        None, 15)
    S.q("ga-br-p4", "medium", "**Project Tiger** was launched in —",
        ["1973", "1969", "1980", "1986"], "1973",
        "**Project Tiger, 1973**, started from Corbett. The **Chipko movement** is also 1973 — tree-hugging villagers of Uttarakhand.",
        None, 15)
    S.q("ga-br-p4", "medium", "Which bacterium fixes atmospheric **nitrogen in legume root nodules**?",
        ["Rhizobium", "Lactobacillus", "Streptococcus", "Salmonella"], "Rhizobium",
        "**Rhizobium** lives in pea/gram/bean nodules and turns N₂ into usable compounds — why farmers rotate legumes.",
        None, 15)
    S.q("ga-br-p5", "easy", "The **Green Revolution** in India is associated with —",
        ["M.S. Swaminathan", "Verghese Kurien", "Salim Ali", "Sam Pitroda"], "M.S. Swaminathan",
        "**M.S. Swaminathan** led India's Green Revolution (high-yield wheat/rice); **Norman Borlaug** is its world father. Kurien = White Revolution (milk).",
        None, 15)
    S.q("ga-br-p5", "medium", "The **White Revolution** (Operation Flood) made India self-sufficient in —",
        ["Milk", "Wheat", "Fish", "Oilseeds"], "Milk",
        "**Milk** — Operation Flood, led by **Verghese Kurien** (Amul). Blue = fish, Yellow = oilseeds, Green = food grain.",
        None, 15)
    S.q("ga-br-p5", "medium", "Who is known as the **'birdman of India'**?",
        ["Salim Ali", "M.S. Swaminathan", "Homi Bhabha", "C.V. Raman"], "Salim Ali",
        "**Salim Ali** — the great ornithologist whose bird surveys and books mapped India's birdlife.",
        None, 15)
    S.q("ga-br-p6", "medium", "**Dolly the sheep** (1996) is famous as the first —",
        ["Cloned mammal", "Test-tube mammal", "Genetically modified crop", "Transgenic fish"], "Cloned mammal",
        "**Dolly** — the first mammal cloned from an adult cell (Roslin Institute, Scotland, 1996), a landmark of biotechnology.",
        None, 15)
    S.q("ga-br-p6", "medium", "A **higher BOD** value of a water sample means the water is —",
        ["More polluted", "Cleaner", "Colder", "Saltier"], "More polluted",
        "**Biochemical oxygen demand** — more organic waste feeds more bacteria, which gulp more oxygen: high BOD = dirty water.",
        None, 15)
    return S
