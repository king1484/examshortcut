# -*- coding: utf-8 -*-
"""Builds content/ssc-cgl/topics/ga/chemistry.json. Run: py -3 build_chemistry.py"""
from scicommon import Q, save_topic, place

C_MATTER = """### States and changes of matter
- Solid, liquid, gas; **plasma** is the 4th state (Sun, stars, lightning, neon signs); **Bose–Einstein condensate** is the 5th (predicted by S.N. Bose and Einstein).
- **Sublimation** — solid turns directly into vapour: **camphor, naphthalene balls, iodine, ammonium chloride, dry ice (solid CO₂)**.
- **Physical change** is reversible, with no new substance (melting ice, dissolving sugar). **Chemical change** makes a new substance (rusting, burning, curdling of milk, digestion, cooking).

### Mixtures and their separation
| Method | Used for |
|---|---|
| **Chromatography** | Separating dyes in ink, pigments, drugs in blood |
| **Distillation** | Liquids with widely different boiling points; pure water |
| **Fractional distillation** | Components of **petroleum** and of **liquefied air** |
| **Centrifugation** | **Cream from milk**, blood tests |
| **Sublimation** | Salt + camphor / ammonium chloride |
| **Crystallisation** | Pure salt from sea water, pure copper sulphate |
| **Separating funnel** | Immiscible liquids (oil + water) |

- **Colloids** show the **Tyndall effect** (scattering of a light beam) and **Brownian motion**. Examples: **milk** (emulsion — fat in water), **fog, clouds** (liquid in gas — aerosol), **smoke** (solid in gas), **butter** (water in fat).
- True solutions (sugar or salt in water) do not show the Tyndall effect.

### Structure of the atom
| Particle | Discovered by | Charge |
|---|---|---|
| **Electron** | **J.J. Thomson** (1897, cathode rays) | −1 |
| **Proton** | Canal rays — **E. Goldstein**; identified by **Rutherford** | +1 |
| **Neutron** | **James Chadwick** (1932) | 0 |
| **Nucleus** | **Rutherford** (gold-foil / α-scattering) | + |

- **Dalton** — atomic theory (atom indivisible). **Thomson** — 'plum pudding' model. **Rutherford** — nuclear model. **Bohr** — fixed orbits/energy levels.
- Atomic number (Z) = number of protons; mass number (A) = protons + neutrons.
- **Isotopes** — same Z, different A (¹H protium, ²H **deuterium**, ³H **tritium** — the radioactive one; C-12 and C-14). **Isobars** — same A, different Z (e.g. ⁴⁰Ar and ⁴⁰Ca). **Isotones** — same number of neutrons.
- Shells hold at most **2n²** electrons: K = 2, L = 8, M = 18. Valence electrons decide chemical behaviour.
- **Avogadro number** = **6.022 × 10²³** particles per mole.
- Gas laws: **Boyle** — P ∝ 1/V (T constant); **Charles** — V ∝ T (P constant); **Avogadro** — equal volumes of gases at the same T and P have equal numbers of molecules.
"""

C_PERIODIC = """### History of classification
| Scientist | Contribution |
|---|---|
| **Döbereiner** | **Triads** (e.g. Li, Na, K) |
| **Newlands** | **Law of octaves** (every 8th element similar) |
| **Mendeleev** | Periodic table based on **atomic mass**; left gaps and predicted eka-aluminium (gallium), eka-silicon (germanium) |
| **Moseley** | **Modern periodic law** — properties depend on **atomic number** |

- The modern (long form) table has **18 groups** (vertical) and **7 periods** (horizontal); **118** named elements.
- **Group 1** — alkali metals (Li, Na, K…); **Group 2** — alkaline earth metals (Be, Mg, Ca…); **Group 17** — **halogens** (F, Cl, Br, I); **Group 18** — **noble gases** (He, Ne, Ar, Kr, Xe, Rn).
- Across a period (left → right): atomic size **decreases**, metallic character decreases, electronegativity increases. Down a group: size **increases**, metallic character increases.
- **Fluorine** is the most electronegative element.

### Record-holders (static favourites)
| Record | Answer |
|---|---|
| Most abundant element in the universe | **Hydrogen** |
| Most abundant element in Earth's crust | **Oxygen** (then silicon) |
| Most abundant **metal** in Earth's crust | **Aluminium** (then iron) |
| Most abundant gas in the atmosphere | **Nitrogen** (about 78%), then oxygen (about 21%), then argon |
| Most abundant element in the human body | **Oxygen** (by mass) |
| Lightest element / lightest metal | **Hydrogen** / **Lithium** |
| Metal that is **liquid** at room temperature | **Mercury** (Bromine is the liquid **non-metal**) |
| Metal that melts in the palm | **Gallium** (about 30 °C) |
| Hardest natural substance | **Diamond** |
| Best conductor of electricity | **Silver** (then copper) |
| Most malleable and ductile metal | **Gold** |
| Metal with the highest melting point | **Tungsten** |
| Non-metal that conducts electricity | **Graphite** |
| Lustrous non-metal | **Iodine** |

### Noble gases and their uses
- **Helium** — balloons and airships (light, non-inflammable), breathing mix for deep-sea divers.
- **Neon** — advertising signs (orange-red glow). **Argon** — filled in **electric bulbs**. **Xenon** — flash lamps. **Radon** — radioactive.
- **Metalloids**: boron, silicon, germanium, arsenic, antimony, tellurium.
"""

C_ACIDS = """### Acids, bases and indicators
| Indicator | In acid | In base |
|---|---|---|
| **Litmus** | Blue → **red** | Red → **blue** |
| **Phenolphthalein** | **Colourless** | **Pink** |
| **Methyl orange** | **Red** | **Yellow** |
| **Turmeric** | Yellow (no change) | **Reddish-brown** |

- **pH scale** (Sørensen): 0–14 at 25 °C. **< 7 acidic, 7 neutral, > 7 basic.** pH = −log[H⁺]; each unit is a **10-fold** change in H⁺.
- Typical values: **gastric juice about 1.2–2** (HCl), lemon juice about 2–2.5, **pure water 7**, **human blood about 7.4** (slightly basic), milk of magnesia about 10.
- **Tooth decay** starts when mouth pH falls below about **5.5**. **Antacids** (milk of magnesia — Mg(OH)₂, baking soda) neutralise excess stomach acid.
- **Ant and bee stings** inject **formic (methanoic) acid** — rub baking soda. **Wasp stings** are alkaline — use vinegar.
- **Acid rain** has pH below about 5.6.

### Natural sources of acids
| Source | Acid |
|---|---|
| Vinegar | **Acetic** |
| Lemon, orange (citrus) | **Citric** |
| **Tamarind**, grapes | **Tartaric** |
| **Tomato**, spinach | **Oxalic** |
| **Curd**, sour milk | **Lactic** |
| Apple | **Malic** |
| **Ant sting, nettle** | **Formic** |
| Stomach | **Hydrochloric** |

### Common names of compounds
| Common name | Chemical name / formula |
|---|---|
| **Baking soda** | Sodium hydrogen carbonate, **NaHCO₃** |
| **Washing soda** | Sodium carbonate decahydrate, **Na₂CO₃·10H₂O** |
| **Bleaching powder** | Calcium oxychloride, **CaOCl₂** |
| **Plaster of Paris** | Calcium sulphate hemihydrate, **CaSO₄·½H₂O** |
| **Gypsum** | **CaSO₄·2H₂O** |
| Common salt | NaCl |
| **Quicklime** / **slaked lime** | **CaO** / **Ca(OH)₂** |
| Limestone, marble, chalk | **CaCO₃** |
| Caustic soda / caustic potash | NaOH / KOH |
| **Blue vitriol** | Copper sulphate, CuSO₄·5H₂O |
| **Green vitriol** | Ferrous sulphate, FeSO₄·7H₂O |
| **White vitriol** | Zinc sulphate, ZnSO₄·7H₂O |
| **Oil of vitriol** | Sulphuric acid, H₂SO₄ |
| **Muriatic acid** | Hydrochloric acid, HCl |
| **Epsom salt** | MgSO₄·7H₂O |
| **Potash alum** (fitkari) | K₂SO₄·Al₂(SO₄)₃·24H₂O — water purification |
| **Hypo** | Sodium thiosulphate, Na₂S₂O₃ — photography |
| **Laughing gas** | Nitrous oxide, **N₂O** |
| **Dry ice** | Solid CO₂ |
| **Heavy water** | D₂O — moderator in reactors |
| **Marsh gas** | Methane, CH₄ |
| **Lunar caustic** | Silver nitrate, AgNO₃ |
| Sal ammoniac | Ammonium chloride, NH₄Cl |
| **Aqua regia** | Conc. HNO₃ + conc. HCl in **1 : 3** — dissolves gold and platinum |

### Types of reactions and everyday chemistry
- **Oxidation** = gain of oxygen / loss of electrons; **reduction** = the opposite. **Redox** reactions do both.
- **Rusting** of iron needs **both oxygen and water** (moisture); rust is hydrated iron(III) oxide, Fe₂O₃·xH₂O. Prevention: painting, oiling, **galvanisation (zinc coating)**, alloying (stainless steel).
- **Rancidity** — oxidation of fats/oils; chips packets are flushed with **nitrogen** to prevent it.
- **Neutralisation**: acid + base → salt + water. **Displacement**: a more reactive metal displaces a less reactive one (iron nail turns brown in copper sulphate solution).
- **Hard water**: **temporary** hardness (bicarbonates of Ca and Mg) is removed by **boiling**; **permanent** hardness (chlorides and sulphates) by **washing soda** or ion exchange.
- **Plaster of Paris** sets into gypsum when mixed with water — used for **plasters on fractured bones** and statues.
"""

C_METALS = """### Ores
| Metal | Main ore(s) |
|---|---|
| **Aluminium** | **Bauxite** (Al₂O₃·2H₂O) |
| **Iron** | **Haematite** (Fe₂O₃), **magnetite** (Fe₃O₄), siderite |
| **Copper** | **Copper pyrites / chalcopyrite**, malachite, cuprite |
| **Zinc** | **Zinc blende** (ZnS), calamine |
| **Lead** | **Galena** (PbS) |
| **Mercury** | **Cinnabar** (HgS) |
| **Tin** | **Cassiterite** (SnO₂) |
| **Uranium** | **Pitchblende** |
| **Silver** | Argentite |
| **Sodium** | Rock salt |
| **Magnesium** | Magnesite, dolomite, carnallite |
| **Calcium** | Limestone, gypsum |

### Metallurgy steps
- **Concentration** — **froth flotation** for sulphide ores (pine oil used); magnetic separation; gravity separation.
- **Calcination** — heating **carbonate** ores in limited air; **roasting** — heating **sulphide** ores in excess air.
- **Reduction** — with carbon (iron in a **blast furnace**) or by electrolysis (aluminium — **Hall–Héroult** process; sodium, potassium).
- **Refining** — electrolytic refining (copper), with the impure metal as the anode.

### Reactivity series
**K > Na > Ca > Mg > Al > Zn > Fe > Pb > (H) > Cu > Hg > Ag > Au**
- Metals above hydrogen give H₂ with dilute acids; **copper, silver and gold do not**.
- **Sodium and potassium are stored under kerosene** (they react violently with air and water). **White phosphorus is stored under water** (it catches fire in air).
- Gold and platinum are **noble metals** — very unreactive.

### Alloys
| Alloy | Composition | Use |
|---|---|---|
| **Brass** | **Copper + Zinc** | Utensils, fittings |
| **Bronze** | **Copper + Tin** | Statues, medals, bells |
| **Bell metal** | Copper + Tin (higher tin) | Bells |
| **Gun metal** | Copper + Tin + Zinc | Gears, castings |
| **German silver** | Copper + Zinc + Nickel (**no silver**) | Utensils, decorative items |
| **Solder** | **Lead + Tin** | Joining electrical wires (low melting point) |
| **Stainless steel** | Iron + **Chromium** + Nickel + Carbon | Cutlery, utensils (does not rust) |
| **Duralumin** | Aluminium + Copper + Magnesium + Manganese | **Aircraft** bodies |
| **Magnalium** | Aluminium + Magnesium | Light instruments |
| **Nichrome** | Nickel + Chromium | Heater coils |
| **Amalgam** | **Any metal + Mercury** | Dental fillings (silver–tin amalgam) |

### Gold purity
- **24 carat = pure gold.** Purity % = (carat ÷ 24) × 100, so **22 carat ≈ 91.67%**, 18 carat = 75%.
- Jewellery gold is alloyed with **copper or silver** to make it harder.
"""

C_ORGANIC = """### Carbon and its compounds
- Carbon forms long chains and rings (**catenation**) and has valency **4** (tetravalency).
- **Allotropes**: **diamond** (hardest, bad conductor, each C bonded to 4), **graphite** (soft, layered, **conducts electricity** — pencil 'lead', lubricant, electrodes), **fullerene** (C₆₀ buckminsterfullerene), **graphene** (single layer of graphite).
- Hydrocarbons: **alkanes** single bonds (CₙH₂ₙ₊₂, saturated), **alkenes** double bond (CₙH₂ₙ), **alkynes** triple bond (CₙH₂ₙ₋₂).
- **Methanol** is poisonous (can cause blindness); **ethanol** is the alcohol in drinks and is blended with petrol. **Vinegar** is about 5–8% acetic acid. **Esters** have a fruity smell.
- **Soap** = sodium or potassium salt of long-chain fatty acids, made by **saponification** (fat + NaOH). Soap forms **scum** in hard water; **detergents** work in hard water too.
- **Hydrogenation** of vegetable oil with a **nickel catalyst** gives vanaspati ghee.

### Fuels
| Fuel | Main component |
|---|---|
| **CNG** | **Methane** |
| **LPG** | **Butane** (with propane); **ethyl mercaptan** is added for smell to detect leaks |
| **Biogas / gobar gas** | **Methane** (plus CO₂) |
| **Oxy-acetylene flame** | **Acetylene (ethyne)** — welding and cutting |
| Water gas | CO + H₂ |
| Producer gas | CO + N₂ |

- **Hydrogen** has the highest calorific value by mass. **Octane number** rates petrol; **cetane number** rates diesel.
- Coal by carbon content: **anthracite > bituminous > lignite > peat**.
- **Ethylene (ethene)** is used for artificial **ripening** of fruits (calcium carbide, which releases acetylene, is banned for this).

### Polymers
| Polymer | Monomer / note |
|---|---|
| **Polythene** | Ethene |
| **PVC** | Vinyl chloride — pipes |
| **Teflon** | **Tetrafluoroethylene** — **non-stick cookware** |
| **Bakelite** | **Phenol + formaldehyde** — **thermosetting**, electrical switches |
| **Nylon** | First fully synthetic fibre |
| **Natural rubber** | **Isoprene** (polyisoprene) |
| **Rayon** | 'Artificial silk' from **cellulose** |
| **Melamine** | Thermosetting — crockery |

- **Vulcanisation** — heating rubber with **sulphur** (Charles Goodyear) to make it hard and elastic.
- **Thermoplastics** (polythene, PVC) soften on heating; **thermosetting plastics** (Bakelite, melamine) do not.

### Industrial processes
| Process | Product | Catalyst |
|---|---|---|
| **Haber** | **Ammonia** | **Iron** |
| **Contact** | **Sulphuric acid** | **Vanadium pentoxide** (V₂O₅) |
| **Ostwald** | **Nitric acid** | Platinum |
| **Solvay** | **Sodium carbonate** | — |
| **Chlor-alkali** | NaOH, Cl₂, H₂ (electrolysis of brine) | — |

- **Glass** = silica (sand) + sodium carbonate + limestone, fused; **borosilicate (Pyrex)** resists heat; cobalt oxide gives blue glass.
- **Portland cement** (Joseph Aspdin); **gypsum** is added to slow its setting.

### Pollution and poisons
| Substance | Effect |
|---|---|
| **SO₂, NO₂** | **Acid rain** (damage to the Taj Mahal — 'marble cancer') |
| **CFCs** | **Ozone layer depletion** |
| CO₂, CH₄, N₂O, water vapour | **Greenhouse effect** |
| **Carbon monoxide** | Binds haemoglobin (carboxyhaemoglobin) — suffocation |
| **Methyl isocyanate (MIC)** | **Bhopal gas tragedy, 1984** |
| **Mercury** | **Minamata disease** (Japan) |
| **Cadmium** | **Itai-itai disease** (Japan) |
| **Arsenic** | Black-foot disease; groundwater contamination |
| **Excess fluoride** | **Fluorosis** (teeth and bones) |
| **Nitrate** in water | **Blue baby syndrome** |
| **Lead** | Plumbism (lead poisoning) |
"""

SUBTOPICS = [
    {
        "id": "ch-matter-atom",
        "title": "Matter, separation methods and atomic structure",
        "concept": C_MATTER,
        "formulas": [
            {"name": "Moles from mass", "tex": r"n = \frac{m}{M}", "note": "M = molar mass in g/mol"},
            {"name": "Number of particles", "tex": r"N = n \times N_A,\quad N_A = 6.022 \times 10^{23}", "note": "Avogadro number"},
            {"name": "Boyle's law", "tex": r"P_1V_1 = P_2V_2", "note": "temperature constant"},
            {"name": "Charles's law", "tex": r"\frac{V_1}{T_1} = \frac{V_2}{T_2}", "note": "pressure constant, T in kelvin"},
            {"name": "Ideal gas equation", "tex": r"PV = nRT", "note": "R = 8.314 J mol⁻¹ K⁻¹"},
            {"name": "Maximum electrons in a shell", "tex": r"2n^{2}", "note": "K = 2, L = 8, M = 18"},
        ],
        "tricks": [
            {
                "title": "Iso-words by the letter",
                "body": "Isot**o**pes — same atomic number (same **p**rotons, 'P for isoto-P-es'). Isob**a**rs — same **A** (mass number). Isoto**n**es — same **n**eutrons.",
                "example": {"q": "Deuterium and tritium are?", "solution": "Isotopes of hydrogen — same atomic number 1, different mass numbers."},
            },
            {
                "title": "Sublimation set: 'Camphor, Naphthalene, Iodine, Ammonium chloride, Dry ice' — 'CNIAD'",
                "body": "If an option is one of these, it is the sublimating substance.",
                "example": None,
            },
        ],
        "mistakes": [
            "Calling milk a true solution — it is a colloid (emulsion).",
            "Saying tritium is stable — it is the radioactive isotope of hydrogen.",
            "Treating rusting or curdling as a physical change — both are chemical changes.",
        ],
    },
    {
        "id": "ch-periodic",
        "title": "Periodic table, elements and record-holders",
        "concept": C_PERIODIC,
        "formulas": [],
        "tricks": [
            {
                "title": "Crust order: 'OSAIC' — Oxygen, Silicon, Aluminium, Iron, Calcium",
                "body": "So the most abundant element is O and the most abundant **metal** is Al.",
                "example": {"q": "Most abundant metal in the Earth's crust?", "solution": "Aluminium."},
            },
            {
                "title": "Two liquids at room temperature",
                "body": "**Mercury** — metal; **Bromine** — non-metal. Gallium and caesium melt just above room temperature.",
                "example": None,
            },
        ],
        "mistakes": [
            "Saying Mendeleev's table was based on atomic number — it used atomic mass; Moseley used atomic number.",
            "Answering iron for the most abundant metal in the crust — it is aluminium.",
            "Answering oxygen for the most abundant gas in air — it is nitrogen.",
        ],
    },
    {
        "id": "ch-acids-compounds",
        "title": "Acids, bases, pH, common compounds and reactions",
        "concept": C_ACIDS,
        "formulas": [
            {"name": "pH", "tex": r"\text{pH} = -\log_{10}[\text{H}^{+}]", "note": "pH + pOH = 14 at 25 °C"},
            {"name": "Neutralisation", "tex": r"\text{Acid} + \text{Base} \rightarrow \text{Salt} + \text{H}_2\text{O}", "note": ""},
            {"name": "Setting of Plaster of Paris", "tex": r"\text{CaSO}_4\cdot\tfrac{1}{2}\text{H}_2\text{O} + 1\tfrac{1}{2}\,\text{H}_2\text{O} \rightarrow \text{CaSO}_4\cdot 2\text{H}_2\text{O}", "note": "PoP → gypsum"},
        ],
        "tricks": [
            {
                "title": "Kitchen acid map: 'Vinegar-Acetic, Lemon-Citric, Tamarind-Tartaric, Tomato-Oxalic, Curd-Lactic, Apple-Malic, Ant-Formic'",
                "body": "Pairs that start alike help: **T**amarind–**T**artaric, **A**pple–m**A**lic (think 'mAlus', the apple genus), **F**ormica (Latin for ant)–**F**ormic.",
                "example": {"q": "Which acid is present in tomato?", "solution": "Oxalic acid."},
            },
            {
                "title": "Phenolphthalein goes 'Pink in Base'",
                "body": "'**P**henol → **P**ink' only in a base; in acid it stays colourless.",
                "example": None,
            },
            {
                "title": "Vitriol colours by metal",
                "body": "**Blue** — copper (CuSO₄ crystals are blue), **Green** — iron (ferrous), **White** — zinc; **Oil** of vitriol — H₂SO₄.",
                "example": None,
            },
        ],
        "mistakes": [
            "Swapping baking soda (NaHCO₃) and washing soda (Na₂CO₃·10H₂O).",
            "Writing aqua regia as 3 HNO₃ : 1 HCl — it is 1 HNO₃ : 3 HCl.",
            "Thinking rust forms in dry air — it needs both oxygen and moisture.",
        ],
    },
    {
        "id": "ch-metals-ores",
        "title": "Metals, ores, metallurgy and alloys",
        "concept": C_METALS,
        "formulas": [
            {"name": "Gold purity", "tex": r"\text{Purity}\,(\%) = \frac{\text{carat}}{24} \times 100", "note": "22 ct ≈ 91.67%"},
        ],
        "tricks": [
            {
                "title": "Reactivity series: 'Please Stop Calling Me A Zebra, I Like Her Calling Me Smart Goat'",
                "body": "**P**otassium, **S**odium, **C**alcium, **M**agnesium, **A**luminium, **Z**inc, **I**ron, **L**ead, **H**ydrogen, **C**opper, **M**ercury, **S**ilver, **G**old.",
                "example": None,
            },
            {
                "title": "Brass vs Bronze",
                "body": "**Br-a-ss** has **Z**inc (think 'brass band with **Z**ing'); **Bronze** has **T**in (bron**ze** medal — 'third'/tin). Both are copper-based.",
                "example": {"q": "Bronze is an alloy of?", "solution": "Copper and tin."},
            },
        ],
        "mistakes": [
            "Believing German silver contains silver — it is copper, zinc and nickel.",
            "Naming haematite as an aluminium ore — it is iron; bauxite is aluminium.",
            "Saying solder has a high melting point — its low melting point is the whole point.",
        ],
    },
    {
        "id": "ch-organic-everyday",
        "title": "Carbon compounds, fuels, polymers, industry and pollution",
        "concept": C_ORGANIC,
        "formulas": [
            {"name": "Alkane / alkene / alkyne", "tex": r"C_nH_{2n+2},\quad C_nH_{2n},\quad C_nH_{2n-2}", "note": ""},
            {"name": "Haber process", "tex": r"N_2 + 3H_2 \rightleftharpoons 2NH_3", "note": "iron catalyst"},
            {"name": "Complete combustion of methane", "tex": r"CH_4 + 2O_2 \rightarrow CO_2 + 2H_2O", "note": ""},
        ],
        "tricks": [
            {
                "title": "Process → product: 'Haber-Ammonia, Contact-Sulphuric, Ostwald-Nitric, Solvay-Soda'",
                "body": "Pair the catalysts too: Haber — **Fe**, Contact — **V₂O₅**, Ostwald — **Pt**.",
                "example": {"q": "Which catalyst is used in the Contact process?", "solution": "Vanadium pentoxide (V₂O₅)."},
            },
            {
                "title": "Japanese diseases: 'Mina-Mercury, Itai-Cadmium'",
                "body": "**M**inamata — **M**ercury; Itai-itai ('ouch-ouch', bone pain) — **Cad**mium.",
                "example": None,
            },
        ],
        "mistakes": [
            "Saying LPG is mainly methane — LPG is mainly butane; CNG and biogas are mainly methane.",
            "Calling Bakelite a thermoplastic — it is thermosetting.",
            "Naming phosgene for the Bhopal tragedy — the gas was methyl isocyanate.",
        ],
    },
]

PYQ = [
    {"pattern": "Common name → chemical name/formula", "frequency": "very common", "howToSpot": "'Chemical formula of baking soda / Plaster of Paris / bleaching powder is...'", "approach": "Learn the common-names table; watch hydrates (PoP ½H₂O vs gypsum 2H₂O)."},
    {"pattern": "Natural source → acid", "frequency": "very common", "howToSpot": "'Which acid is found in tamarind / tomato / curd?'", "approach": "Use the kitchen acid map."},
    {"pattern": "Ore → metal and alloy → composition", "frequency": "very common", "howToSpot": "'Bauxite is an ore of...', 'Brass is an alloy of...'", "approach": "Ores and alloys tables; German silver has no silver."},
    {"pattern": "Indicators and pH", "frequency": "common", "howToSpot": "'Phenolphthalein in a basic solution turns...', 'pH of human blood...'", "approach": "Indicator colour table; blood 7.4, gastric juice ~2."},
    {"pattern": "Periodic table and element records", "frequency": "common", "howToSpot": "'Modern periodic table is based on...', 'Most abundant metal in crust...'", "approach": "Moseley = atomic number; OSAIC; mercury & bromine are liquids."},
    {"pattern": "Industrial process, polymer or fuel component", "frequency": "common", "howToSpot": "'Haber process is used to make...', 'Teflon is a polymer of...', 'Main component of CNG...'", "approach": "Process–product–catalyst table; polymer–monomer table."},
    {"pattern": "Pollutant → disease/disaster", "frequency": "occasional", "howToSpot": "'Minamata disease is caused by...', 'Bhopal gas tragedy gas...'", "approach": "Pollution table."},
    {"pattern": "Atomic structure and isotopes", "frequency": "occasional", "howToSpot": "'Isotopes have the same...', 'Electron was discovered by...'", "approach": "Iso-words trick; discoverer table."},
]

SOLVED = [
    Q("ch-ex01",
      "What is the chemical formula of Plaster of Paris?",
      ["CaSO₄·2H₂O", "CaSO₄·½H₂O", "CaCO₃", "CaOCl₂"],
      1,
      "**Plaster of Paris** is calcium sulphate **hemihydrate**, CaSO₄·½H₂O, made by heating gypsum (CaSO₄·2H₂O) to about 373 K. On mixing with water it sets back into gypsum. CaCO₃ is limestone and CaOCl₂ is bleaching powder.",
      "PoP = 'half water'; gypsum = 'two water'.",
      "easy", "ch-acids-compounds", "common name → formula", 20),
    Q("ch-ex02",
      "What is the percentage of pure gold in 22-carat gold (approximately)?",
      ["88.5%", "91.7%", "95.8%", "22%"],
      1,
      "24 carat is pure gold, so 22 carat = 22/24 × 100 = **91.67%**. The rest is usually copper or silver for hardness.",
      "22/24 = 11/12 ≈ 0.9167.",
      "easy", "ch-metals-ores", "carat purity", 25),
    Q("ch-ex03",
      "Which gas leaked in the Bhopal gas tragedy of 1984?",
      ["Phosgene", "Methyl isocyanate", "Mustard gas", "Hydrogen sulphide"],
      1,
      "On the night of 2–3 December 1984, **methyl isocyanate (MIC)** leaked from the Union Carbide pesticide plant in Bhopal, causing one of the world's worst industrial disasters.",
      None,
      "easy", "ch-organic-everyday", "pollutant → disaster", 15),
    Q("ch-ex04",
      "Brass is an alloy of:",
      ["Copper and tin", "Copper and zinc", "Iron and nickel", "Lead and tin"],
      1,
      "**Brass = copper + zinc.** Copper + tin is **bronze**, and lead + tin is **solder**.",
      "Brass-Zinc, Bronze-Tin.",
      "easy", "ch-metals-ores", "alloy composition", 15),
]

PRACTICE = [
    Q("ch-q01",
      "The chemical name of baking soda is:",
      ["Sodium carbonate", "Sodium hydrogen carbonate", "Sodium chloride", "Sodium hydroxide"],
      1,
      "Baking soda is **sodium hydrogen carbonate (sodium bicarbonate), NaHCO₃**. Sodium carbonate (Na₂CO₃·10H₂O) is washing soda, and sodium hydroxide is caustic soda.",
      None, "easy", "ch-acids-compounds", "common name → formula", 15),
    Q("ch-q02",
      "Which acid is present in tamarind?",
      ["Citric acid", "Tartaric acid", "Oxalic acid", "Lactic acid"],
      1,
      "Tamarind contains **tartaric acid**. Citrus fruits have citric acid, tomato has oxalic acid and curd has lactic acid.",
      "Tamarind–Tartaric.", "easy", "ch-acids-compounds", "natural source → acid", 15),
    Q("ch-q03",
      "The pH of human blood is approximately:",
      ["6.4", "7.4", "8.4", "5.4"],
      1,
      "Human blood is **slightly basic, about pH 7.4** (normal range about 7.35–7.45), kept steady by buffer systems.",
      None, "easy", "ch-acids-compounds", "pH value", 15),
    Q("ch-q04",
      "What colour does phenolphthalein show in a basic solution?",
      ["Colourless", "Pink", "Yellow", "Red"],
      1,
      "Phenolphthalein is **colourless in acidic and neutral** solutions and turns **pink in basic** solutions.",
      "Phenol → Pink in base.", "easy", "ch-acids-compounds", "indicator colour", 15),
    Q("ch-q05",
      "Bauxite is the chief ore of:",
      ["Iron", "Aluminium", "Copper", "Zinc"],
      1,
      "**Bauxite** (hydrated aluminium oxide) is the chief ore of **aluminium**, extracted by electrolysis (Hall–Héroult process).",
      None, "easy", "ch-metals-ores", "ore → metal", 15),
    Q("ch-q06",
      "Solder, used for joining electrical wires, is an alloy of:",
      ["Copper and zinc", "Lead and tin", "Copper and tin", "Iron and chromium"],
      1,
      "**Solder = lead + tin.** Its low melting point lets it melt easily and join wires. Copper + zinc is brass, copper + tin is bronze.",
      None, "easy", "ch-metals-ores", "alloy composition", 15),
    Q("ch-q07",
      "Which metal is stored under kerosene to prevent it from reacting with air and moisture?",
      ["Sodium", "Aluminium", "Copper", "Mercury"],
      0,
      "**Sodium** (and potassium) react vigorously with oxygen and water — sodium can catch fire — so they are kept **under kerosene**. White phosphorus, a non-metal, is stored under water.",
      None, "easy", "ch-metals-ores", "storage of reactive elements", 15),
    Q("ch-q08",
      "Which metal is a liquid at normal room temperature?",
      ["Gallium", "Mercury", "Bromine", "Sodium"],
      1,
      "**Mercury** is the metal that is liquid at room temperature. **Bromine** is also liquid but is a **non-metal**. Gallium melts at about 30 °C — in the palm — but is solid at a normal room temperature of about 25 °C.",
      "Liquid metal = Hg; liquid non-metal = Br.", "easy", "ch-periodic", "element record", 20),
    Q("ch-q09",
      "The modern periodic table is based on:",
      ["Atomic mass", "Atomic number", "Number of neutrons", "Atomic volume"],
      1,
      "Henry **Moseley** showed that the properties of elements are periodic functions of their **atomic number**, which is the basis of the modern periodic law. Mendeleev's table was based on atomic mass.",
      None, "easy", "ch-periodic", "periodic law", 15),
    Q("ch-q10",
      "Isotopes of an element have the same:",
      ["Mass number", "Atomic number", "Number of neutrons", "Physical properties"],
      1,
      "**Isotopes** have the **same atomic number** (protons) but **different mass numbers** because their neutron counts differ. Their chemical properties are similar; physical properties such as density differ.",
      "Isoto-P-es = same Protons.", "easy", "ch-matter-atom", "isotopes", 15),
    Q("ch-q11",
      "Which of the following substances undergoes sublimation?",
      ["Common salt", "Camphor", "Sugar", "Sand"],
      1,
      "**Camphor** changes directly from solid to vapour — **sublimation**. Naphthalene, iodine, ammonium chloride and dry ice also sublime.",
      "CNIAD.", "easy", "ch-matter-atom", "sublimation", 15),
    Q("ch-q12",
      "The Haber process is used for the manufacture of:",
      ["Sulphuric acid", "Ammonia", "Nitric acid", "Sodium carbonate"],
      1,
      "The **Haber process** combines nitrogen and hydrogen over an **iron catalyst** to make **ammonia**. Sulphuric acid comes from the Contact process, nitric acid from the Ostwald process and sodium carbonate from the Solvay process.",
      None, "easy", "ch-organic-everyday", "industrial process → product", 15),
    Q("ch-q13",
      "Teflon, used in non-stick cookware, is a polymer of:",
      ["Vinyl chloride", "Tetrafluoroethylene", "Isoprene", "Ethene"],
      1,
      "**Teflon** is polytetrafluoroethylene (PTFE), made from **tetrafluoroethylene**. Vinyl chloride gives PVC, isoprene gives natural rubber and ethene gives polythene.",
      None, "medium", "ch-organic-everyday", "polymer → monomer", 20),
    Q("ch-q14",
      "The main constituent of CNG (compressed natural gas) is:",
      ["Butane", "Methane", "Propane", "Ethane"],
      1,
      "CNG is mostly **methane**. LPG is mainly **butane** with propane.",
      "CNG/biogas → methane; LPG → butane.", "easy", "ch-organic-everyday", "fuel component", 15),
    Q("ch-q15",
      "Minamata disease is caused by poisoning from:",
      ["Cadmium", "Mercury", "Lead", "Arsenic"],
      1,
      "**Minamata disease** (Japan, 1950s) was caused by **methylmercury** in industrial wastewater, which accumulated in fish. Cadmium caused itai-itai disease.",
      "Mina-Mercury, Itai-Cadmium.", "medium", "ch-organic-everyday", "pollutant → disease", 15),
]

place(PRACTICE, [2, 0, 3, 1, 1, 3, 0, 2, 3, 1, 0, 2, 1, 3, 0])

topic = {
    "id": "chemistry",
    "sectionId": "ga",
    "title": "Chemistry",
    "importance": "medium",
    "avgQuestions": {"tier1": 1, "tier2": 1},
    "summary": "Matter and atomic structure, the periodic table and element records, acids-bases-pH and common compound names, ores and alloys, carbon compounds, fuels, polymers, industrial processes and pollution. CGL asks 1-2 direct factual questions.",
    "subtopics": SUBTOPICS,
    "pyqPatterns": PYQ,
    "solvedExamples": SOLVED,
    "practice": PRACTICE,
}

if __name__ == "__main__":
    save_topic(topic)
