"""chemistry deep content — part 2: ch-acids-compounds, ch-metals-ores, ch-organic-everyday."""
import os
import sys

sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
from _lib import Sub


def build_acids():
    S = Sub("ch-acids-compounds")
    S.notes = """### Acids, bases and how we test them
An **acid** releases H⁺ ions in water (sour taste); a **base** releases OH⁻ ions (slippery feel) — a soluble base is an **alkali**. Indicators tell them apart:
| Indicator | In acid | In base |
|---|---|---|
| Litmus | Blue → **red** | Red → **blue** |
| Phenolphthalein | **Colourless** | **Pink** |
| Methyl orange | **Red** | **Yellow** |
| Turmeric | Yellow (no change) | **Reddish-brown** |
The **pH scale** (Sørensen) runs 0–14: below 7 acidic, 7 neutral, above 7 basic; each step is a **ten-fold** change. Key values: gastric juice ≈ 1–2 (HCl), lemon ≈ 2, pure water 7, **blood ≈ 7.4** (slightly basic), milk of magnesia ≈ 10. **Tooth decay begins below pH 5.5**; **acid rain** is below about 5.6. **Antacids** (milk of magnesia Mg(OH)₂) neutralise excess stomach acid; an **ant sting** injects **formic acid** — soothe it with baking soda.

### Where natural acids come from
Vinegar → **acetic**; lemon/orange → **citric**; **tamarind and grapes** → **tartaric**; **tomato and spinach** → **oxalic**; curd/sour milk → **lactic**; apple → **malic**; ant sting/nettle → **formic**; stomach → **hydrochloric**. This table is asked in nearly every paper.

### Common names and formulae — the core table
| Common name | Chemical name / formula |
|---|---|
| Baking soda | Sodium bicarbonate, **NaHCO₃** |
| Washing soda | Sodium carbonate, **Na₂CO₃·10H₂O** |
| Common salt | **NaCl** |
| Caustic soda | Sodium hydroxide, **NaOH** |
| Caustic potash | **KOH** |
| Bleaching powder | **Ca(OCl)Cl** (calcium oxychloride) |
| Plaster of Paris | Calcium sulphate hemihydrate, **CaSO₄·½H₂O** |
| Gypsum | **CaSO₄·2H₂O** |
| Quicklime | **CaO** |
| Limestone, marble, chalk | **CaCO₃** |
| Lime water | **Ca(OH)₂** |
| Milk of magnesia | **Mg(OH)₂** |
| Laughing gas | **N₂O** |
| Blue vitriol | **CuSO₄·5H₂O** |
| Green vitriol | **FeSO₄·7H₂O** |
| White vitriol | **ZnSO₄·7H₂O** |
| Oil of vitriol | **H₂SO₄** (sulphuric acid) |
| Alum (fitkari) | **KAl(SO₄)₂·12H₂O** |
| Heavy water | **D₂O** |
| Dry ice | Solid **CO₂** |
| Quartz, sand | **SiO₂** |

### Reactions and everyday chemistry
- **Neutralisation**: acid + base → salt + water. Acid + metal → salt + **H₂**; acid + carbonate → salt + water + **CO₂** (the gas turns **lime water milky** — the standard test for CO₂).
- **Chlor-alkali process**: electrolysis of brine (NaCl solution) gives **NaOH + Cl₂ + H₂**.
- **Baking soda** (NaHCO₃): mild, non-poisonous antacid; raises cakes and idli batter with CO₂; in soda acid fire extinguishers. **Washing soda** (Na₂CO₃·10H₂O): removes permanent hardness of water, cleans glass, makes borax and glass. **Bleaching powder** (Ca(OCl)Cl): disinfects drinking water, bleaches cotton.
- **Plaster of Paris**: made by heating gypsum to 100 °C; on adding water it sets back into hard gypsum — casts for fractures, statues, chalk.
- **Water of crystallisation**: CuSO₄·5H₂O is blue; on heating it loses water and turns white, regaining colour on moistening.

### Quick revision
- pH: <7 acid, 7 neutral, >7 base; blood 7.4; tooth decay below 5.5; acid rain below 5.6.
- Phenolphthalein: colourless in acid, pink in base. Ant sting = formic acid; tamarind = tartaric; tomato = oxalic.
- Baking soda NaHCO₃; washing soda Na₂CO₃·10H₂O; caustic soda NaOH; bleaching powder Ca(OCl)Cl.
- Plaster of Paris CaSO₄·½H₂O from gypsum CaSO₄·2H₂O; lime water milky = CO₂ test.
- Vitriols: oil–H₂SO₄, blue–CuSO₄·5H₂O, green–FeSO₄·7H₂O, white–ZnSO₄."""
    S.pattern("ga-ac-p1", "Common name ↔ chemical name/formula", "very common",
        "'Baking soda is…', 'chemical name of washing soda / bleaching powder / plaster of Paris', 'which is CaO', formula asked for a common name.",
        None,
        "1. Learn the core table by pairing: baking soda NaHCO₃ ↔ washing soda Na₂CO₃·10H₂O; quicklime CaO ↔ lime water Ca(OH)₂ ↔ limestone CaCO₃.\n2. Gypsum CaSO₄·2H₂O loses water → plaster of Paris CaSO₄·½H₂O.\n3. Vitriol family: oil of vitriol H₂SO₄; blue CuSO₄·5H₂O; green FeSO₄·7H₂O; white ZnSO₄.\nWhy: these names are fixed by tradition, so the only route is the pair-table.",
        "The chemical formula of **baking soda** is —",
        "**NaHCO₃** (sodium bicarbonate). Washing soda is the stronger base Na₂CO₃·10H₂O.")
    S.pattern("ga-ac-p2", "Natural source → acid", "very common",
        "'Tamarind contains…', 'the acid in an ant sting is…', 'which acid is in curd/tomato/apple', match-the-column of foods and acids.",
        None,
        "1. Kitchen map: vinegar–acetic, lemon–citric, tamarind+grapes–tartaric, tomato+spinach–oxalic, curd–lactic, apple–malic, ant sting+nettle–formic, stomach–HCl.\n2. Trap pairs: tamarind is TARTARIC (not citric); tomato is OXALIC; apple is MALIC.\n3. Base for an ant sting: baking soda (neutralises the acid).",
        "The acid present in **tamarind** is —",
        "**Tartaric acid** (grapes also contain it). Lemon gives citric acid, curd lactic acid.")
    S.pattern("ga-ac-p3", "Indicators and pH values", "very common",
        "'Phenolphthalein turns pink in…', 'what colour does turmeric give with a base', pH of blood/tooth decay threshold, 'solution of pH 3 is…'.",
        None,
        "1. Indicator colours: litmus blue→red in acid; phenolphthalein colourless in acid, PINK in base; methyl orange red in acid, yellow in base; turmeric reddish-brown in base.\n2. pH: <7 acid, 7 neutral (pure water), >7 base; blood ≈ 7.4 (slightly basic); tooth enamel dissolves below pH 5.5.\n3. Lower pH = stronger acid; each pH unit is a ten-fold change.",
        "A solution has **pH = 3**; another has **pH = 5**. The first is —",
        "**100 times more acidic** — each unit below 7 multiplies H⁺ ten-fold (3 is two units below 5).")
    S.pattern("ga-ac-p4", "Salt chemistry and standard reactions", "common",
        "'CO₂ turns lime water…', 'plaster of Paris is made from…', chlor-alkali products, what happens when water is added to quicklime.",
        None,
        "1. Acid + carbonate → CO₂; CO₂ + Ca(OH)₂ (lime water) → white CaCO₃ = milkiness (the CO₂ test).\n2. Gypsum heated → plaster of Paris; water added → sets to gypsum again (fracture casts).\n3. Chlor-alkali: electrolysis of brine → NaOH + Cl₂ + H₂.\n4. Quicklime + water → slaked lime, releasing much heat.",
        "**Lime water turns milky** when CO₂ is passed through it because —",
        "Insoluble **calcium carbonate (CaCO₃)** forms — the standard test for carbon dioxide.")
    S.pattern("ga-ac-p5", "Uses of baking soda, washing soda, bleaching powder", "common",
        "'Which chemical is used as an antacid / to remove hardness of water / to disinfect water', why cakes rise, composition of a soda-acid extinguisher.",
        None,
        "1. Baking soda NaHCO₃: antacid, baking powder (CO₂ makes dough rise), fire extinguishers, mild alkali for stings.\n2. Washing soda Na₂CO₃·10H₂O: removes **permanent hardness**, glass and borax manufacture.\n3. Bleaching powder Ca(OCl)Cl: sterilises drinking water, bleaches cotton, makes chloroform.\n4. Match the job to the chemical; 'permanent hardness' always points to washing soda.",
        "Permanent hardness of water is removed by adding —",
        "**Washing soda (Na₂CO₃·10H₂O)**, which precipitates the calcium and magnesium ions.")
    S.pattern("ga-ac-p6", "Vitriols and water of crystallisation", "occasional",
        "'Oil of vitriol is…', 'blue vitriol is…', why blue copper sulphate turns white on heating, formula with dot-water.",
        None,
        "1. Vitriol set: oil of vitriol = H₂SO₄; blue vitriol = CuSO₄·5H₂O; green vitriol = FeSO₄·7H₂O; white vitriol = ZnSO₄·7H₂O.\n2. The dot-water is **water of crystallisation**: heating drives it off (blue → white); moistening restores it.\n3. Same idea: washing soda's 10H₂O; gypsum's 2H₂O.",
        "On strong heating, **blue vitriol (CuSO₄·5H₂O)** turns —",
        "**White**, as it loses its five waters of crystallisation; adding water turns it blue again.")

    S.q("ga-ac-p1", "easy", "The chemical name of **baking soda** is —",
        ["Sodium bicarbonate", "Sodium carbonate", "Sodium hydroxide", "Sodium chloride"], "Sodium bicarbonate",
        "Baking soda = **sodium bicarbonate (NaHCO₃)** — a mild, non-poisonous base used in food and as an antacid.",
        None, 15)
    S.q("ga-ac-p1", "medium", "**Caustic soda** is —",
        ["NaOH", "KOH", "Na₂CO₃", "NaCl"], "NaOH",
        "**Caustic soda** = sodium hydroxide (NaOH), made with chlorine and hydrogen by electrolysis of brine. KOH is caustic potash.",
        None, 15)
    S.q("ga-ac-p1", "medium", "**Plaster of Paris** is chemically —",
        ["CaSO₄·½H₂O", "CaSO₄·2H₂O", "CaO", "CaCO₃"], "CaSO₄·½H₂O",
        "Plaster of Paris is **calcium sulphate hemihydrate**, made by heating gypsum (CaSO₄·2H₂O); with water it sets back to hard gypsum.",
        None, 20)
    S.q("ga-ac-p1", "medium", "**Bleaching powder** is chemically —",
        ["Calcium oxychloride", "Calcium oxide", "Calcium sulphate", "Calcium carbonate"], "Calcium oxychloride",
        "**Ca(OCl)Cl** — calcium oxychloride — disinfects drinking water and bleaches cotton.",
        None, 20)
    S.q("ga-ac-p2", "easy", "The acid present in **lemon** is —",
        ["Citric acid", "Acetic acid", "Tartaric acid", "Lactic acid"], "Citric acid",
        "Lemon and orange give **citric acid**. Vinegar–acetic; tamarind–tartaric; curd–lactic.",
        None, 15)
    S.q("ga-ac-p2", "medium", "An **ant sting** hurts because it injects —",
        ["Formic acid, which baking soda neutralises", "Lactic acid, which lime water neutralises", "An alkali, which vinegar neutralises", "Oxalic acid, which salt neutralises"], "Formic acid, which baking soda neutralises",
        "The sting injects **formic (methanoic) acid**; rubbing baking soda (a mild base) neutralises it. A wasp sting is alkaline — vinegar is used there instead.",
        None, 20)
    S.q("ga-ac-p2", "medium", "**Oxalic acid** is found in —",
        ["Tomato and spinach", "Curd", "Vinegar", "Apple"], "Tomato and spinach",
        "**Oxalic acid** — tomato and spinach. Curd has lactic acid; vinegar acetic; apple malic.",
        None, 15)
    S.q("ga-ac-p3", "easy", "**Phenolphthalein** turns —",
        ["Pink in a basic solution", "Pink in an acidic solution", "Red in a basic solution", "Colourless in a basic solution"], "Pink in a basic solution",
        "Phenolphthalein is **colourless in acid and pink in base** — the classic 'Pink in Base' pair.",
        None, 15)
    S.q("ga-ac-p3", "medium", "The pH of **human blood** is about —",
        ["7.4", "5.5", "6.4", "9.0"], "7.4",
        "Blood is kept between 7.35 and 7.45 — **slightly basic**. 5.5 is the tooth-decay threshold; 9 is like milk of magnesia.",
        None, 15)
    S.q("ga-ac-p3", "medium", "**Tooth decay** begins when the pH of the mouth falls below about —",
        ["5.5", "7.0", "4.0", "2.0"], "5.5",
        "Below **pH 5.5** mouth acids (made by bacteria from sugar) start dissolving tooth enamel — the standard exam value.",
        None, 15)
    S.q("ga-ac-p3", "hard", "The pH of a solution changes from **4 to 2**. Its hydrogen-ion concentration —",
        ["Becomes 100 times more", "Becomes 100 times less", "Becomes double", "Stays the same"], "Becomes 100 times more",
        "Each pH unit is a **ten-fold** change in H⁺; two units means 10 × 10 = 100 times more acidic.",
        None, 25)
    S.q("ga-ac-p4", "easy", "**Carbon dioxide** passed through lime water turns it —",
        ["Milky", "Blue", "Pink", "Colourless"], "Milky",
        "CO₂ reacts with dissolved Ca(OH)₂ to form insoluble **calcium carbonate** — a white milky precipitate. This is the standard test for CO₂.",
        None, 15)
    S.q("ga-ac-p4", "medium", "The **chlor-alkali process** (electrolysis of brine) produces —",
        ["NaOH, chlorine and hydrogen", "NaCl, water and oxygen", "Sodium metal and chlorine only", "Washing soda and bleaching powder only"], "NaOH, chlorine and hydrogen",
        "Electrolysing concentrated brine gives **caustic soda at the cathode, chlorine at the anode and hydrogen** — the 'chlor-alkali' trio.",
        None, 20)
    S.q("ga-ac-p4", "medium", "Adding water to **quicklime (CaO)** gives —",
        ["Slaked lime with much heat released", "Limestone and CO₂", "Plaster of Paris", "Nothing — CaO is insoluble"], "Slaked lime with much heat released",
        "CaO + H₂O → **Ca(OH)₂ (slaked lime)** + heat — an exothermic combination used in whitewashing.",
        None, 20)
    S.q("ga-ac-p5", "medium", "**Permanent hardness** of water is removed by —",
        ["Washing soda", "Boiling", "Baking soda", "Bleaching powder"], "Washing soda",
        "**Washing soda (Na₂CO₃·10H₂O)** precipitates the Ca²⁺/Mg²⁺ ions that cause permanent hardness. Boiling only removes temporary (bicarbonate) hardness.",
        None, 20)
    S.q("ga-ac-p5", "medium", "Cakes and idli batter turn **fluffy** because baking soda —",
        ["Releases CO₂ on heating with an acid", "Releases oxygen", "Absorbs water", "Kills the bacteria"], "Releases CO₂ on heating with an acid",
        "NaHCO₃ + acid (or heat) gives **CO₂ bubbles** that puff up the dough. The same reaction pressurises soda-acid fire extinguishers.",
        None, 20)
    S.q("ga-ac-p6", "medium", "**Oil of vitriol** is the old name for —",
        ["Sulphuric acid", "Nitric acid", "Hydrochloric acid", "Acetic acid"], "Sulphuric acid",
        "**H₂SO₄** — called oil of vitriol. Blue vitriol is CuSO₄·5H₂O, green vitriol FeSO₄·7H₂O, white vitriol ZnSO₄.",
        None, 15)
    S.q("ga-ac-p6", "medium", "When **blue copper sulphate crystals** are heated strongly, they —",
        ["Turn white as water of crystallisation is lost", "Melt into blue liquid", "Turn black instantly into copper", "Remain blue"], "Turn white as water of crystallisation is lost",
        "Heating drives off the 5H₂O; the anhydrous CuSO₄ left behind is **white** — and turns blue again if moistened.",
        None, 20)
    return S


def build_metals():
    S = Sub("ch-metals-ores")
    S.notes = """### Metals, non-metals and the exceptions
Metals are **lustrous, malleable, ductile, good conductors** of heat and electricity, and sonorous. Non-metals are mostly dull, brittle and insulating. The exceptions carry the marks: **mercury** is a liquid metal; **sodium and potassium** are soft metals cut with a knife; **graphite** (a non-metal) conducts electricity; **iodine** is a lustrous non-metal; **diamond**, the hardest natural substance, is a non-metal.

### Ore → metal
| Metal | Main ore(s) |
|---|---|
| **Aluminium** | **Bauxite** |
| **Iron** | **Haematite**, magnetite, siderite |
| **Copper** | Copper pyrites (chalcopyrite), malachite |
| **Zinc** | Zinc blende (ZnS), calamine |
| **Lead** | Galena (PbS) |
| **Mercury** | Cinnabar (HgS) |
| **Tin** | Cassiterite |
| **Uranium** | Pitchblende |
| **Sodium** | Rock salt |
| **Calcium** | Limestone, gypsum |

### Metallurgy — the four steps
1. **Concentration** of the ore: **froth flotation** for sulphide ores (powdered ore + pine oil + air — sulphide sticks to the froth); magnetic separation for magnetic ores; gravity separation.
2. **Conversion to oxide**: **calcination** = heat a **carbonate** ore in limited air; **roasting** = heat a **sulphide** ore in excess air. Memory hook: **C**alcination–**C**arbonate, roasting–sulphide.
3. **Reduction** to metal: carbon/CO in the **blast furnace** (iron); **electrolysis** for very reactive metals — aluminium (**Hall–Héroult process**), sodium, magnesium.
4. **Refining**: **electrolytic refining** — impure metal at the anode dissolves and pure metal deposits on the cathode (used for copper).

### Reactivity series and its uses
**K > Na > Ca > Mg > Al > Zn > Fe > Pb > (H) > Cu > Hg > Ag > Au.**
- Metals above hydrogen release **H₂** from dilute acids; **copper, silver, gold do not**.
- **Na and K are stored under kerosene** (they catch fire in moist air); Ca and Mg need care too.
- Metals below hydrogen occur **free in nature** (gold, platinum).
- A more reactive metal **displaces** a less reactive one from its salt solution (iron nail in copper sulphate turns the solution green).

### Corrosion and its prevention
**Rusting** needs **both air and moisture**; rust is hydrated iron oxide (Fe₂O₃·xH₂O). Protection: **galvanisation** (coating with zinc — even the zinc's position above iron in the reactivity series lets it sacrifice itself), painting, greasing, electroplating, and alloying to **stainless steel**. Silver **tarnishes** black (Ag₂S with sulphur in air); copper grows a **green patina** (basic copper carbonate); aluminium protects itself with a thin oxide film (made thicker by **anodising**).

### Alloys — composition list
| Alloy | Composition | Use / note |
|---|---|---|
| **Brass** | Cu + **Zn** | Utensils, decor; not Cu+Sn |
| **Bronze** | Cu + **Sn** | Statues, bells |
| **Bell metal** | Cu + Sn (more Sn) | Bells, gongs |
| **Stainless steel** | Fe + Cr + Ni (+ C) | Cutlery; rust-free |
| **Duralumin** | Al + Cu (+ Mg, Mn) | Aircraft — light and strong |
| **Solder** | **Pb + Sn** | Joining wires; low melting point |
| **German silver** | Cu + Zn + Ni | Cutlery (no real silver) |
| **Nichrome** | Ni + Cr (+ Fe) | Heating coils — high resistance |
| **Invar** | Fe + Ni | Very low expansion — pendulums, tapes |
| **Amalgam** | Any metal + **mercury** | Dental fillings (except iron/platinum) |

Gold purity: **24 carat = pure**; 22 carat gold = 22/24 ≈ **91.6%** gold.

### Quick revision
- Calcination–carbonate, roasting–sulphide; froth flotation–sulphide ores; electrolysis–Al, Na.
- Al→bauxite, Fe→haematite, Hg→cinnabar, Zn→zinc blende, Pb→galena, Sn→cassiterite, U→pitchblende.
- K > Na > Ca > Mg > Al > Zn > Fe > Pb > H > Cu > Hg > Ag > Au; Cu/Ag/Au give no H₂ with dilute acid.
- Brass Cu+Zn, bronze Cu+Sn, solder Pb+Sn, duralumin Al+Cu, stainless Fe+Cr+Ni, nichrome Ni+Cr.
- Rusting = air + moisture; galvanising = zinc coat; amalgam = metal + mercury; 24 carat pure."""
    S.pattern("ga-mo-p1", "Ore → metal matching", "very common",
        "'Bauxite is the ore of…', 'cinnabar / galena / pitchblende is an ore of which metal', match-the-column of ores and metals.",
        None,
        "1. Headline pairs: bauxite–aluminium, haematite–iron, cinnabar–mercury, galena–lead, zinc blende–zinc, cassiterite–tin, copper pyrites–copper, pitchblende–uranium, rock salt–sodium.\n2. Trap: calamine is also zinc (with zinc blende); magnetite and siderite also iron.\n3. In match-the-columns, fix the surest pair first (bauxite–Al) and chain the rest.\nWhy: each metal's name echoes in its ore except the classic traps, so recall by pair, not by logic.",
        "**Cinnabar** is an ore of —",
        "**Mercury** (HgS). Heating cinnabar in air gives mercury vapour + SO₂ — an extraction by roasting alone.")
    S.pattern("ga-mo-p2", "Alloy → composition", "very common",
        "'Brass is an alloy of…', 'which alloy contains tin', 'stainless steel is made by adding…to iron', distinguish brass from bronze.",
        None,
        "1. Copper family: brass = Cu + **Zn**; bronze = Cu + **Sn**; bell metal = Cu + Sn (tin-rich); german silver = Cu + Zn + Ni.\n2. Iron family: stainless steel = Fe + Cr + Ni; invar = Fe + Ni.\n3. Light metals: duralumin = Al + Cu; magnalium = Al + Mg; solder = Pb + Sn; nichrome = Ni + Cr; amalgam = metal + Hg.\n4. The classic trap: brass is Zn, bronze is Sn.",
        "**Brass** is an alloy of —",
        "**Copper and zinc.** Bronze is the copper–tin one; german silver is copper + zinc + nickel.")
    S.pattern("ga-mo-p3", "Metallurgy steps and processes", "common",
        "'Roasting is used for … ores', 'calcination vs roasting', 'froth flotation separates…', 'which metal is extracted by electrolysis', 'Hall–Héroult process is for…'.",
        None,
        "1. Concentration: froth flotation for **sulphide** ores (pine oil); gravity/magnetic separation.\n2. Oxide conversion: **calcination = carbonate ore, limited air; roasting = sulphide ore, excess air**.\n3. Reduction: carbon in the blast furnace (Fe); **electrolysis for Al, Na, Mg** (Hall–Héroult for aluminium).\n4. Refining: electrolytic — impure anode, pure cathode (copper).",
        "**Roasting** is done for —",
        "**Sulphide ores in excess air** — it converts them to oxides, driving off SO₂. Calcination is the carbonate-ore, limited-air version.")
    S.pattern("ga-mo-p4", "Reactivity series consequences", "common",
        "'Which metal does not give H₂ with dilute acid', 'why is sodium stored in kerosene', 'which metal occurs free in nature', displacement-reaction questions.",
        None,
        "1. Order: K > Na > Ca > Mg > Al > Zn > Fe > Pb > H > Cu > Hg > Ag > Au.\n2. Above H → H₂ from dilute acids; Cu/Ag/Au do not react so.\n3. Top metals (K, Na, Ca) catch fire in moist air → stored under kerosene; bottom metals (Au, Pt) occur free.\n4. A more reactive metal displaces a less reactive metal from its salt solution.",
        "Which metal will **NOT** liberate hydrogen from dilute hydrochloric acid?",
        "**Copper** — it lies below hydrogen in the reactivity series (so do silver, gold, mercury).")
    S.pattern("ga-mo-p5", "Corrosion and its prevention", "common",
        "'Rusting requires…', 'galvanisation is coating iron with…', 'green coating on copper / black coating on silver', 'anodising is done on…'.",
        None,
        "1. Rusting needs **both air and moisture**; rust is hydrated iron(III) oxide.\n2. Prevention: galvanisation (zinc coat), painting/oiling, electroplating, anodising (thicker oxide on aluminium), alloying (stainless steel).\n3. Colour clues: iron–red-brown rust; copper–green basic carbonate; silver–black Ag₂S tarnish.",
        "A **green coating** slowly appears on a copper vessel left in damp air. It is —",
        "**Basic copper carbonate** — copper reacts slowly with moist air (O₂, H₂O and CO₂). Silver instead turns black with silver sulphide.")
    S.pattern("ga-mo-p6", "Metal/non-metal properties and exceptions", "common",
        "'Which metal is liquid / soft / stored in kerosene', 'which non-metal conducts electricity', 'most ductile metal', carat-purity of gold.",
        None,
        "1. Exceptions: Hg liquid metal; Na, K soft metals; graphite conducts; iodine lustrous; diamond hard but non-metal.\n2. Best conductor among metals – silver; most ductile/malleable – gold; highest melting point – tungsten.\n3. Purity: 24 carat pure; 22 carat ≈ 91.6%; carat also = 200 mg for gems.",
        "Which **non-metal** conducts electricity?",
        "**Graphite** — free electrons between its carbon layers carry current, so it serves as electrodes.")

    S.q("ga-mo-p1", "easy", "**Bauxite** is the chief ore of —",
        ["Aluminium", "Iron", "Copper", "Zinc"], "Aluminium",
        "**Bauxite** (Al₂O₃·2H₂O) gives aluminium; iron comes from haematite and magnetite.",
        None, 15)
    S.q("ga-mo-p1", "medium", "**Galena** is the principal ore of —",
        ["Lead", "Mercury", "Tin", "Silver"], "Lead",
        "**Galena (PbS)** is lead sulphide. Cinnabar is mercury's ore; cassiterite, tin's.",
        None, 15)
    S.q("ga-mo-p1", "medium", "**Pitchblende** is an important ore of —",
        ["Uranium", "Radium", "Lead", "Thorium"], "Uranium",
        "**Pitchblende** is uranium oxide (U₃O₈) — the Curies processed tonnes of it to find radium.",
        None, 15)
    S.q("ga-mo-p2", "easy", "**Brass** is an alloy of —",
        ["Copper and zinc", "Copper and tin", "Iron and nickel", "Lead and tin"], "Copper and zinc",
        "**Brass = Cu + Zn**; bronze = Cu + Sn. Both look golden, but the second metal differs.",
        None, 15)
    S.q("ga-mo-p2", "medium", "**Solder**, used for joining wires, is an alloy of —",
        ["Lead and tin", "Copper and zinc", "Iron and carbon", "Nickel and chromium"], "Lead and tin",
        "**Solder (Pb + Sn)** has a low melting point, so it melts and flows around the joint easily.",
        None, 15)
    S.q("ga-mo-p2", "medium", "**Stainless steel** resists corrosion mainly because of the added —",
        ["Chromium and nickel", "Tin and lead", "Zinc and copper", "Sulphur and phosphorus"], "Chromium and nickel",
        "Stainless steel = **iron + chromium (about 10–20%) + nickel** (+ carbon). The chromium forms a protective oxide skin.",
        None, 15)
    S.q("ga-mo-p3", "medium", "**Froth flotation** is used to concentrate —",
        ["Sulphide ores", "Oxide ores", "Carbonate ores", "Native gold"], "Sulphide ores",
        "Powdered sulphide ore is mixed with water, **pine oil** and air: the sulphide particles stick to the froth and float, the gangue sinks.",
        None, 20)
    S.q("ga-mo-p3", "medium", "**Calcination** involves heating —",
        ["Carbonate ores in limited air", "Sulphide ores in excess air", "Any ore with carbon", "The pure metal"], "Carbonate ores in limited air",
        "**Calcination = carbonate ore, limited air** (CO₂ is driven off); **roasting = sulphide ore, excess air** (SO₂ escapes). Both leave the oxide.",
        None, 20)
    S.q("ga-mo-p3", "medium", "**Aluminium** is extracted from its oxide by —",
        ["Electrolysis (Hall–Héroult process)", "Heating with carbon in a blast furnace", "Froth flotation", "Heating alone"], "Electrolysis (Hall–Héroult process)",
        "Aluminium is too reactive to reduce with carbon, so molten alumina is **electrolysed** (Hall–Héroult). Iron, less reactive, is reduced by carbon in the blast furnace.",
        None, 20)
    S.q("ga-mo-p4", "easy", "**Sodium** is stored under **kerosene** because it —",
        ["Reacts violently with air and moisture", "Is lighter than water", "Melts at room temperature", "Is radioactive"], "Reacts violently with air and moisture",
        "K and Na are at the top of the reactivity series; exposed to moist air they catch fire. Kerosene keeps air and water away.",
        None, 15)
    S.q("ga-mo-p4", "medium", "Which metal occurs **free (native)** in nature?",
        ["Gold", "Sodium", "Calcium", "Aluminium"], "Gold",
        "**Gold** (and platinum) sit at the bottom of the reactivity series — too unreactive to form compounds — so they are dug up as the free metal.",
        None, 15)
    S.q("ga-mo-p4", "medium", "An **iron nail** dipped in copper sulphate solution —",
        ["Turns the solution green and gets copper deposited", "Dissolves completely", "Turns the solution blue", "Shows no change"], "Turns the solution green and gets copper deposited",
        "Iron is **more reactive** than copper: Fe displaces Cu from CuSO₄, forming green FeSO₄; red-brown copper coats the nail.",
        None, 20)
    S.q("ga-mo-p5", "easy", "**Rusting of iron** requires —",
        ["Both air (oxygen) and moisture", "Only oxygen", "Only water", "Carbon dioxide"], "Both air (oxygen) and moisture",
        "Iron rusts only when **oxygen and water** are both present; rust is hydrated iron(III) oxide. Boiled water without air, or dry air alone, does not rust iron.",
        None, 15)
    S.q("ga-mo-p5", "medium", "**Galvanisation** is coating iron with a thin layer of —",
        ["Zinc", "Tin", "Chromium", "Nickel"], "Zinc",
        "**Zinc** coating — galvanisation — protects buckets and roofs; zinc corrodes first (sacrificial protection). Coating with tin gives a tin can instead.",
        None, 15)
    S.q("ga-mo-p6", "easy", "Which metal is **liquid at room temperature**?",
        ["Mercury", "Sodium", "Bromine", "Gallium"], "Mercury",
        "**Mercury** is the only common liquid metal. Bromine is a liquid but a non-metal; gallium melts slightly above room temperature (in your palm).",
        None, 15)
    S.q("ga-mo-p6", "medium", "Pure gold is **24 carat**. The gold content of **22-carat** jewellery is about —",
        ["91.6%", "75%", "88%", "99%"], "91.6%",
        "22/24 = **0.916 ≈ 91.6%** gold; the rest (copper/silver) hardens it. Pure gold is too soft for daily wear.",
        None, 20)
    return S


def build_organic():
    S = Sub("ch-organic-everyday")
    S.notes = """### Carbon — the backbone chemical
Carbon bonds to itself in long chains and rings (**catenation**) and always shows valency **4 (tetravalency)** — together these give it millions of compounds, the field of organic chemistry. Its **allotropes**: **diamond** (hardest natural substance, does not conduct, each C bonded to 4 others), **graphite** (soft, slippery, **conducts electricity** — pencil 'lead', electrodes, lubricant), **fullerene (C₆₀)** and **graphene** (one-atom-thick sheet).
Hydrocarbons: **alkanes** — single bonds, saturated, CₙH₂ₙ₊₂ (methane CH₄, ethane); **alkenes** — one double bond, CₙH₂ₙ (ethene); **alkynes** — one triple bond, CₙH₂ₙ₋₂ (ethyne = acetylene).

### Fuels — what burns in what
| Fuel | Main component |
|---|---|
| **CNG** | **Methane** |
| **LPG** | **Butane** (+ propane); **ethyl mercaptan** added for smell |
| **Biogas (gobar gas)** | **Methane** (+ CO₂) |
| **Oxy-acetylene flame** | **Ethyne (acetylene)** — welding/cutting (~3000 °C) |
| Water gas | CO + H₂ |
| Producer gas | CO + N₂ |
Coal grades rise with carbon: peat → lignite → bituminous → **anthracite** (best). Petroleum ('black gold') is separated by **fractional distillation** into refinery gas, petrol, naphtha, kerosene, diesel, lubricating oil and bitumen (road tar, residue).

### Everyday carbon compounds
- **Methanol (wood spirit)** is poisonous — even small doses cause blindness; **ethanol** is drinkable alcohol, blended into petrol.
- **Vinegar** = 5–8% acetic acid. **Esters** (acid + alcohol) give fruits their smell.
- **Soap** = sodium/potassium salt of a long-chain fatty acid, made by **saponification** (fat + NaOH). In hard water soap forms useless **scum**; **detergents** work even in hard water.
- **Hydrogenation**: vegetable oil + H₂ with a **nickel catalyst** → vanaspati ghee (solid fat).

### Industrial processes — name ↔ product
| Process | Product |
|---|---|
| **Haber** | **Ammonia** (N₂ + 3H₂, iron catalyst) |
| **Contact** | **Sulphuric acid** (V₂O₅ catalyst) |
| **Ostwald** | **Nitric acid** (from ammonia, Pt catalyst) |
| **Solvay** | **Sodium carbonate** (washing soda) |
| **Bosch** | Hydrogen (from water gas) |

### Polymers and fibres
Polymers are giant molecules of repeating units. **Natural**: cotton (cellulose), silk and wool (proteins), starch, natural rubber. **Vulcanisation** (Charles Goodyear, 1839) heats rubber with **sulphur** — tyres get strength and elasticity. **Synthetic**: **polythene** (from ethene — bags), **PVC** (pipes, insulation), **Teflon/PTFE** (non-stick pans), **nylon** (first fully synthetic fibre, 1935 — ropes, parachutes), **bakelite** (first plastic, hard, thermosetting — switch boards), **rayon** ('artificial silk', made from wood cellulose).

### Pollution — pollutant ↔ effect
- **Carbon monoxide (CO)** binds haemoglobin ~200 times more strongly than O₂ → suffocation deaths from geysers and coal stoves.
- **SO₂ and NOₓ** → **acid rain**; **SO₂** was the killer of the London smog (1952).
- **Mercury** → **Minamata disease**; **cadmium** → **itai-itai disease** (both Japan, 1950s–60s).
- **CFCs** (old fridge/aerosol gases) ate the **ozone layer** — phased out by the **Montreal Protocol (1987)**; the ozone layer lies in the **stratosphere**.
- **Greenhouse gases** (CO₂, CH₄, water vapour) drive global warming; the **Kyoto Protocol (1997)** and **Paris Agreement (2015)** target emissions. The **Bhopal gas tragedy (1984)** was **methyl isocyanate (MIC)**.

### Quick revision
- CNG/biogas–methane; LPG–butane (smelly ethyl mercaptan); welding–acetylene; anthracite–best coal.
- Haber–NH₃, Contact–H₂SO₄, Ostwald–HNO₃, Solvay–Na₂CO₃.
- Nylon first synthetic fibre; bakelite first plastic; vulcanisation = rubber + sulphur; Teflon non-stick.
- Methanol poison, ethanol safe-ish; soap scums in hard water, detergent does not; hydrogenation uses nickel.
- CO–haemoglobin poison; Minamata–Hg; itai-itai–Cd; CFC–ozone (Montreal 1987); Bhopal–MIC 1984."""
    S.pattern("ga-or-p1", "Fuel ↔ main component", "very common",
        "'CNG is mainly…', 'LPG contains…', 'why does LPG smell', 'which gas is used in welding', 'best variety of coal'.",
        None,
        "1. Gas family: CNG and biogas = **methane**; LPG = **butane** (+ propane); welding = **acetylene (ethyne)** with oxygen.\n2. LPG leaks are smellable because **ethyl mercaptan** is added — the gas itself is odourless.\n3. Coal ranking by carbon: peat < lignite < bituminous < **anthracite**; petroleum splits by fractional distillation (bitumen last).\nWhy: each fuel is a named hydrocarbon, so the answer is recall plus the one-line use.",
        "The gas used with oxygen in a **welding torch** is —",
        "**Acetylene (ethyne)** — its oxy-acetylene flame reaches about 3000 °C and cuts steel.")
    S.pattern("ga-or-p2", "Industrial process ↔ product", "very common",
        "'Haber process gives…', 'sulphuric acid is made by the … process', 'Ostwald process produces…', match-the-column of processes and chemicals.",
        None,
        "1. Fix the four: **Haber → ammonia; Contact → sulphuric acid; Ostwald → nitric acid; Solvay → sodium carbonate**.\n2. Catalyst tags: Haber–iron, Contact–V₂O₅, Ostwald–platinum.\n3. In match-the-columns, anchor on ammonia (Haber) — the rest fall into place by elimination.",
        "The **Contact process** manufactures —",
        "**Sulphuric acid (H₂SO₄)** — SO₂ is oxidised to SO₃ over a V₂O₅ catalyst, then absorbed in water.")
    S.pattern("ga-or-p3", "Polymers, plastics and fibres", "very common",
        "'First synthetic fibre / first plastic', 'Teflon is used for…', 'vulcanisation of rubber is done with…', 'rayon is called artificial…', natural vs synthetic classification.",
        None,
        "1. Records: **nylon = first fully synthetic fibre; bakelite = first plastic (thermosetting); rayon = artificial silk from cellulose**.\n2. Uses: polythene–bags, PVC–pipes, Teflon–non-stick, nylon–ropes and parachutes.\n3. Vulcanisation = natural rubber + **sulphur** (Goodyear) → tyres.\n4. Natural fibres: cotton–cellulose; silk/wool–protein; synthetic: nylon, polyester, acrylic.",
        "**Vulcanised rubber** is made by heating natural rubber with —",
        "**Sulphur** — cross-links form between chains, making the rubber strong, elastic and heat-resistant (tyres).")
    S.pattern("ga-or-p4", "Allotropes and hydrocarbon families", "common",
        "'Which allotrope of carbon conducts electricity', 'hardest natural substance', 'alkane/alkene/alkyne general formula', 'which hydrocarbon is saturated'.",
        None,
        "1. Allotropes: diamond (hardest, non-conductor), graphite (soft, conducts), fullerene C₆₀, graphene.\n2. Families: alkane CₙH₂ₙ₊₂ (single bonds, saturated); alkene CₙH₂ₙ (double); alkyne CₙH₂ₙ₋₂ (triple).\n3. Methane (CH₄) is the simplest alkane and the main gas in CNG/biogas.",
        "Which general formula belongs to an **alkyne**?",
        "**CₙH₂ₙ₋₂** — the triple bond (as in acetylene, C₂H₂) leaves fewer hydrogens than an alkene.")
    S.pattern("ga-or-p5", "Everyday carbon chemistry", "common",
        "'Which alcohol causes blindness', 'vinegar contains…', 'why does soap fail in hard water', 'hydrogenation of oils uses which catalyst', 'esters give…'.",
        None,
        "1. Alcohols: **methanol = poison (blindness, death)**; ethanol = the alcohol in drinks and petrol blends.\n2. Vinegar = 5–8% **acetic acid**; esters (acid + alcohol) = fruity smells.\n3. Soap = fatty-acid salt made by **saponification**; forms scum with hard-water Ca²⁺/Mg²⁺ — detergents do not.\n4. **Hydrogenation** of vegetable oil uses a **nickel catalyst** → vanaspati.",
        "Soap does not lather well in **hard water** because —",
        "Ca²⁺/Mg²⁺ ions react with soap to form insoluble **scum**; synthetic detergents are made to work even so.")
    S.pattern("ga-or-p6", "Pollutant ↔ disease or event", "common",
        "'Minamata disease is caused by…', 'which gas causes acid rain', 'CFCs damage…', 'Bhopal gas tragedy leaked…', 'why is CO poisonous'.",
        None,
        "1. Japanese diseases: **Minamata–mercury; itai-itai–cadmium**.\n2. CO binds **haemoglobin** far more strongly than oxygen → carbon monoxide poisoning.\n3. **SO₂ + NOₓ → acid rain**; **CFCs → ozone-hole** (Montreal Protocol 1987); Bhopal 1984 leaked **methyl isocyanate (MIC)**.\n4. Greenhouse gases: CO₂, CH₄ — Kyoto 1997, Paris 2015.",
        "**Minamata disease** resulted from poisoning by —",
        "**Mercury** — factory effluent in Japan entered fish, and fish-eating villagers were poisoned. (Cadmium caused itai-itai.)")

    S.q("ga-or-p1", "easy", "**CNG** used in vehicles consists mainly of —",
        ["Methane", "Butane", "Ethylene", "Acetylene"], "Methane",
        "Compressed Natural Gas is mostly **methane (CH₄)**. LPG is mainly butane; biogas is also methane-rich.",
        None, 15)
    S.q("ga-or-p1", "medium", "A strong smell is added to **LPG** so leaks are noticed. The added substance is —",
        ["Ethyl mercaptan", "Ethyl alcohol", "Acetone", "Ammonia"], "Ethyl mercaptan",
        "Butane and propane are odourless, so a trace of **ethyl mercaptan** gives LPG its characteristic smell as a safety alarm.",
        None, 20)
    S.q("ga-or-p1", "medium", "The **best grade of coal**, with the highest carbon content, is —",
        ["Anthracite", "Lignite", "Peat", "Bituminous"], "Anthracite",
        "Carbon content rises peat → lignite → bituminous → **anthracite** (over ~90% carbon) — the hottest, cleanest-burning coal.",
        None, 15)
    S.q("ga-or-p2", "easy", "The **Haber process** is used to manufacture —",
        ["Ammonia", "Sulphuric acid", "Nitric acid", "Sodium carbonate"], "Ammonia",
        "**Haber process**: N₂ + 3H₂ → 2NH₃ over an iron catalyst — the base of all nitrogen fertilisers.",
        None, 15)
    S.q("ga-or-p2", "medium", "**Nitric acid** is manufactured by the —",
        ["Ostwald process", "Contact process", "Solvay process", "Haber process"], "Ostwald process",
        "**Ostwald** oxidises ammonia to nitric acid over platinum. Contact gives sulphuric acid; Solvay gives washing soda; Haber gives ammonia.",
        None, 15)
    S.q("ga-or-p2", "medium", "The catalyst used in the **Contact process** for sulphuric acid is —",
        ["Vanadium pentoxide (V₂O₅)", "Iron", "Platinum", "Nickel"], "Vanadium pentoxide (V₂O₅)",
        "**V₂O₅** oxidises SO₂ to SO₃ in the Contact process. Iron (Haber), platinum (Ostwald) and nickel (hydrogenation) are the other exam catalysts.",
        None, 20)
    S.q("ga-or-p3", "easy", "The **first fully synthetic fibre** was —",
        ["Nylon", "Rayon", "Cotton", "Wool"], "Nylon",
        "**Nylon** (1935) was the first man-made fibre made entirely in a factory. Rayon is 'artificial silk' made from natural cellulose, so it is semi-synthetic.",
        None, 15)
    S.q("ga-or-p3", "medium", "**Teflon**, the coating of non-stick pans, is —",
        ["Polytetrafluoroethylene (PTFE)", "Polyvinyl chloride", "Polythene", "Bakelite"], "Polytetrafluoroethylene (PTFE)",
        "**Teflon = PTFE** — slippery and heat-resistant, so nothing sticks. PVC makes pipes; polythene bags; bakelite switchboards.",
        None, 15)
    S.q("ga-or-p3", "medium", "Natural rubber is **vulcanised** by heating it with —",
        ["Sulphur", "Carbon", "Oxygen", "Nitrogen"], "Sulphur",
        "**Vulcanisation** (Goodyear, 1839): sulphur cross-links the rubber chains, giving strength and elasticity — hence tyres.",
        None, 15)
    S.q("ga-or-p4", "easy", "The **hardest natural substance** is —",
        ["Diamond", "Graphite", "Quartz", "Tungsten"], "Diamond",
        "**Diamond**, an allotrope of carbon, is hardest — every carbon is bonded to four others in a rigid network. Graphite, the other allotrope, is soft and slippery.",
        None, 15)
    S.q("ga-or-p4", "medium", "Which allotrope of carbon **conducts electricity**?",
        ["Graphite", "Diamond", "Fullerene C₆₀", "Charcoal"], "Graphite",
        "**Graphite** has free electrons between its layers — used as electrodes. Diamond is an insulator despite being the hardest substance.",
        None, 15)
    S.q("ga-or-p4", "medium", "Compounds of carbon with only **single bonds** are called —",
        ["Alkanes (saturated)", "Alkenes", "Alkynes", "Aromatics"], "Alkanes (saturated)",
        "**Alkanes** (CₙH₂ₙ₊₂) are saturated — methane, ethane, propane. Alkenes carry a double bond, alkynes a triple bond.",
        None, 15)
    S.q("ga-or-p5", "medium", "Which alcohol is **highly poisonous** and can cause blindness?",
        ["Methanol", "Ethanol", "Glycerol", "Sorbitol"], "Methanol",
        "**Methanol (wood spirit)** damages the optic nerve — a few teaspoons cause blindness or death. Ethanol is the ordinary alcohol of drinks.",
        None, 15)
    S.q("ga-or-p5", "medium", "**Vinegar** is a solution of about 5–8% —",
        ["Acetic acid in water", "Citric acid in water", "Ethanol in water", "Formic acid in water"], "Acetic acid in water",
        "Vinegar = dilute **acetic acid (CH₃COOH)**, made by fermenting ethanol. Citric acid is lemon's; formic acid is the ant sting's.",
        None, 15)
    S.q("ga-or-p5", "medium", "**Hydrogenation** of vegetable oil into vanaspati ghee uses **nickel** as —",
        ["Catalyst", "Reactant", "Solvent", "Preservative"], "Catalyst",
        "Ni **speeds up** the addition of hydrogen to the oil's double bonds but is not consumed — a catalyst. The oil turns solid at room temperature.",
        None, 20)
    S.q("ga-or-p6", "easy", "**Minamata disease** is caused by poisoning with —",
        ["Mercury", "Cadmium", "Lead", "Arsenic"], "Mercury",
        "**Mercury** in factory waste entered fish in Minamata Bay, Japan. **Cadmium** causes itai-itai disease — the other 'Japanese disease' pair.",
        None, 15)
    S.q("ga-or-p6", "medium", "**Carbon monoxide** is dangerous because it —",
        ["Binds haemoglobin much more strongly than oxygen", "Burns the lungs", "Dissolves the blood cells", "Raises blood pressure"], "Binds haemoglobin much more strongly than oxygen",
        "CO attaches to haemoglobin about **200 times** more tightly than O₂, so the blood can carry less oxygen — suffocation without choking.",
        None, 20)
    S.q("ga-or-p6", "medium", "The **Bhopal gas tragedy (1984)** involved the leakage of —",
        ["Methyl isocyanate (MIC)", "Chlorine", "Carbon monoxide", "Sulphur dioxide"], "Methyl isocyanate (MIC)",
        "MIC gas escaped from a pesticide plant in Bhopal — the world's worst industrial disaster. London's 1952 killer smog was mainly SO₂.",
        None, 20)
    return S
