"""Chemistry part 2: ch-acids-compounds, ch-metals-ores."""
from _ch_common import pat, mis, trick

S = {}

assert 10 ** (5 - 3) == 100
assert round(22 / 24 * 100, 2) == 91.67
assert 18 / 24 * 100 == 75

# =====================================================================
S["ch-acids-compounds"] = dict(
    concept=(
        "Acids taste sour and bases feel slippery. Indicators and the pH scale tell them apart. "
        "This lesson also holds the fixed tables that exams love: natural acids, common names of chemicals, and a few everyday reactions."
    ),
    notes=r"""### Acids, bases and indicators
An **acid** releases H⁺ ions in water and tastes sour. A **base** releases OH⁻ ions and feels slippery. A base that dissolves in water is an **alkali**.

| Indicator | In acid | In base |
|---|---|---|
| Litmus | Blue turns red | Red turns blue |
| Phenolphthalein | Colourless | Pink |
| Methyl orange | Red | Yellow |
| Turmeric | Yellow (no change) | Reddish-brown |

> **Tip:** Phenolphthalein is pink only in a base. In acid it stays colourless.

### The pH scale
The pH scale runs from 0 to 14. Below 7 is acidic, 7 is neutral and above 7 is basic. Each step is a ten-fold change in H⁺.

| Item | pH |
|---|---|
| Gastric juice (HCl) | about 1.2 to 2 |
| Lemon juice | about 2 to 2.5 |
| Pure water | 7 |
| Human blood | about 7.4 (slightly basic) |
| Milk of magnesia | about 10 |

- Tooth decay starts when mouth pH falls below about 5.5.
- Acid rain has pH below about 5.6.
- Antacids such as milk of magnesia neutralise extra stomach acid.
- An ant or bee sting injects formic acid. Rub baking soda on it. A wasp sting is alkaline, so use vinegar.

### Natural sources of acids
| Source | Acid |
|---|---|
| Vinegar | Acetic |
| Lemon, orange | Citric |
| Tamarind, grapes | Tartaric |
| Tomato, spinach | Oxalic |
| Curd, sour milk | Lactic |
| Apple | Malic |
| Ant sting, nettle | Formic |
| Stomach | Hydrochloric |

### Common names and formulae
| Common name | Chemical name and formula |
|---|---|
| Baking soda | Sodium hydrogen carbonate, NaHCO₃ |
| Washing soda | Na₂CO₃·10H₂O |
| Bleaching powder | Calcium oxychloride, CaOCl₂ |
| Plaster of Paris | CaSO₄·½H₂O |
| Gypsum | CaSO₄·2H₂O |
| Quicklime / slaked lime | CaO / Ca(OH)₂ |
| Limestone, marble, chalk | CaCO₃ |
| Caustic soda / caustic potash | NaOH / KOH |
| Blue vitriol | CuSO₄·5H₂O |
| Green vitriol | FeSO₄·7H₂O |
| White vitriol | ZnSO₄·7H₂O |
| Oil of vitriol | H₂SO₄ |
| Muriatic acid | HCl |
| Epsom salt | MgSO₄·7H₂O |
| Potash alum (fitkari) | K₂SO₄·Al₂(SO₄)₃·24H₂O, purifies water |
| Hypo | Na₂S₂O₃, used in photography |
| Laughing gas | N₂O |
| Marsh gas | CH₄ |
| Lunar caustic | AgNO₃ |
| Heavy water | D₂O |
| Dry ice | Solid CO₂ |
| Aqua regia | Conc. HNO₃ : conc. HCl in 1 : 3; dissolves gold and platinum |

> **Watch:** Aqua regia is 1 part HNO₃ to 3 parts HCl. Do not reverse it.

### Reactions in daily life
- **Neutralisation:** acid + base gives salt + water.
- **Acid + carbonate** gives salt, water and CO₂. CO₂ turns lime water milky. This is the standard CO₂ test.
- **Oxidation** is gain of oxygen or loss of electrons. **Reduction** is the opposite.
- **Rusting** needs both oxygen and moisture. Rust is hydrated iron(III) oxide, Fe₂O₃·xH₂O.
- **Rancidity** is oxidation of fats and oils. Chips packets are flushed with nitrogen to stop it.
- **Hard water:** boiling removes temporary hardness (bicarbonates). Washing soda or ion exchange removes permanent hardness (chlorides and sulphates).
- **Chlor-alkali process:** electrolysis of brine gives NaOH, Cl₂ and H₂.
- **Plaster of Paris** sets into gypsum when water is added. It is used for casts on broken bones.
- **Water of crystallisation:** CuSO₄·5H₂O is blue. Heating drives off the water and it turns white. Adding water brings the blue back.
""",
    tricks=[
        trick("Kitchen acid map",
              "Vinegar-Acetic, Lemon-Citric, Tamarind-Tartaric, Tomato-Oxalic, Curd-Lactic, Apple-Malic, Ant-Formic. Matching first letters helps: Tamarind and Tartaric, Formica (Latin for ant) and Formic.",
              "Which acid is present in tomato?",
              ["Tomato and spinach share one acid.", "That acid is oxalic."],
              "Oxalic acid"),
        trick("Vitriol colours by metal",
              "Blue vitriol is copper sulphate. Green is iron (ferrous) sulphate. White is zinc sulphate. Oil of vitriol is H₂SO₄."),
    ],
    mistakes=[
        mis("Swapping baking soda and washing soda.", "Baking soda is NaHCO₃. Washing soda is Na₂CO₃·10H₂O."),
        mis("Writing aqua regia as 3 HNO₃ : 1 HCl.", "It is 1 part HNO₃ to 3 parts HCl."),
        mis("Thinking rust forms in dry air.", "Rust needs both oxygen and moisture."),
        mis("Saying tamarind has citric acid.", "Tamarind has tartaric acid. Citric acid is in lemon."),
        mis("Removing permanent hardness by boiling.", "Boiling removes only temporary hardness. Use washing soda for permanent hardness."),
    ],
    revision=[
        "pH below 7 acid, 7 neutral, above 7 base. Blood is 7.4.",
        "Tooth decay starts below pH 5.5. Acid rain is below about 5.6.",
        "Phenolphthalein: colourless in acid, pink in base.",
        "Ant sting: formic acid. Tamarind: tartaric. Tomato: oxalic.",
        "Baking soda NaHCO₃. Washing soda Na₂CO₃·10H₂O. Caustic soda NaOH.",
        "Gypsum CaSO₄·2H₂O gives plaster of Paris CaSO₄·½H₂O.",
        "Milky lime water means CO₂. Aqua regia is HNO₃ : HCl = 1 : 3.",
    ],
    patterns=[
        pat("ga-ac-p1", "Common name and chemical formula", "very common",
            "The question says 'baking soda is', 'chemical name of washing soda', 'which is CaO', or gives a formula for a common name.",
            ["Learn the table in pairs.", "Baking soda NaHCO₃ pairs with washing soda Na₂CO₃·10H₂O.", "Quicklime CaO, lime water Ca(OH)₂, limestone CaCO₃.", "Gypsum CaSO₄·2H₂O loses water to give plaster of Paris CaSO₄·½H₂O."],
            "These names are fixed by tradition, so recall by pairs is the only route.",
            "What is the chemical formula of baking soda?",
            ["Baking soda is sodium hydrogen carbonate.", "Washing soda is the other one, Na₂CO₃·10H₂O."],
            "NaHCO₃"),
        pat("ga-ac-p2", "Natural source and acid", "very common",
            "The question says 'tamarind contains', 'the acid in an ant sting', or gives a match-the-column of foods and acids.",
            ["Recall the kitchen map.", "Tamarind and grapes: tartaric. Tomato and spinach: oxalic. Apple: malic.", "Ant sting and nettle: formic. Curd: lactic. Stomach: hydrochloric.", "For a sting, use baking soda to neutralise."],
            "Each food has one main acid that gives its sour taste.",
            "Which acid is present in tamarind?",
            ["Tamarind is not citrus.", "Grapes share its acid."],
            "Tartaric acid"),
        pat("ga-ac-p3", "Indicators and pH values", "very common",
            "The question asks 'phenolphthalein turns pink in', turmeric with a base, the pH of blood, or whether a given pH is acidic.",
            ["Recall the indicator colours.", "pH below 7 is acid, 7 is neutral, above 7 is base.", "Blood is about 7.4. Tooth enamel dissolves below pH 5.5.", "A lower pH means a stronger acid. Each unit is ten times."],
            "The pH scale counts hydrogen ions on a log scale, so one step means ten times.",
            "Solution A has pH 3 and solution B has pH 5. How much more acidic is A?",
            ["The pH differs by 2 units.", "Each unit is ten times, so 10 × 10 = 100."],
            "100 times more acidic"),
        pat("ga-ac-p4", "Salt chemistry and standard reactions", "common",
            "The question says 'CO₂ turns lime water', 'plaster of Paris is made from', chlor-alkali products, or quicklime with water.",
            ["Acid plus carbonate gives CO₂.", "CO₂ with lime water gives white CaCO₃, which looks milky.", "Heated gypsum gives plaster of Paris. Water sets it back to gypsum.", "Brine electrolysis gives NaOH, Cl₂ and H₂."],
            "Each of these is a fixed reaction, so link the input to the product.",
            "Why does lime water turn milky when CO₂ is passed through it?",
            ["CO₂ reacts with Ca(OH)₂.", "Insoluble CaCO₃ forms."],
            "Calcium carbonate forms, a standard test for CO₂"),
        pat("ga-ac-p5", "Uses of baking soda, washing soda, bleaching powder", "common",
            "The question asks which chemical is an antacid, removes hardness, or disinfects water, or why cakes rise.",
            ["Baking soda: antacid, baking powder, soda-acid extinguisher.", "Washing soda: removes permanent hardness; used for glass and borax.", "Bleaching powder: disinfects drinking water, bleaches cotton.", "Match the job to the chemical."],
            "Each chemical has a few well-known uses. Exams test only those.",
            "Permanent hardness of water is removed by adding which chemical?",
            ["Permanent hardness comes from chlorides and sulphates.", "Washing soda precipitates calcium and magnesium."],
            "Washing soda (Na₂CO₃·10H₂O)"),
        pat("ga-ac-p6", "Vitriols and water of crystallisation", "occasional",
            "The question asks 'oil of vitriol is', 'blue vitriol is', or why blue copper sulphate turns white on heating.",
            ["Recall: oil is H₂SO₄, blue is CuSO₄·5H₂O, green is FeSO₄·7H₂O, white is ZnSO₄·7H₂O.", "The dot-water is water of crystallisation.", "Heating drives it off. Moistening restores it."],
            "Fixed water molecules inside the crystal cause its colour.",
            "Blue vitriol (CuSO₄·5H₂O) is heated strongly. What colour does it turn?",
            ["It loses its five waters.", "The anhydrous salt is white."],
            "White; adding water turns it blue again"),
    ],
)

# =====================================================================
S["ch-metals-ores"] = dict(
    concept=(
        "Metals shine, bend and carry electricity, and a few exceptions are popular exam picks. "
        "This lesson pairs each metal with its ore, walks through the steps of extraction, and lists the reactivity series and alloy recipes. "
        "It ends with rusting and gold purity."
    ),
    notes=r"""### Metals and non-metals
Metals are lustrous, malleable, ductile and sonorous. They conduct heat and electricity. Non-metals are mostly dull, brittle and poor conductors.

The exceptions are the exam favourites.

- **Mercury** is a liquid metal.
- **Sodium and potassium** are soft metals. A knife cuts them.
- **Graphite** is a non-metal that conducts electricity.
- **Iodine** is a lustrous non-metal.
- **Diamond** is the hardest natural substance, and it is a non-metal.

### Ore and metal
| Metal | Main ore |
|---|---|
| Aluminium | Bauxite (Al₂O₃·2H₂O) |
| Iron | Haematite (Fe₂O₃), magnetite (Fe₃O₄), siderite |
| Copper | Copper pyrites (chalcopyrite), malachite, cuprite |
| Zinc | Zinc blende (ZnS), calamine |
| Lead | Galena (PbS) |
| Mercury | Cinnabar (HgS) |
| Tin | Cassiterite (SnO₂) |
| Uranium | Pitchblende |
| Silver | Argentite |
| Sodium | Rock salt |
| Magnesium | Magnesite, dolomite, carnallite |
| Calcium | Limestone, gypsum |

### Extracting a metal
Metallurgy has four steps.

1. **Concentration.** Froth flotation suits sulphide ores. Pine oil is used. Magnetic and gravity separation also work.
2. **Convert to oxide.** Calcination heats a carbonate ore in limited air. Roasting heats a sulphide ore in excess air.
3. **Reduction.** Carbon reduces iron in the blast furnace. Very reactive metals need electrolysis: aluminium (Hall-Héroult process), sodium, potassium.
4. **Refining.** In electrolytic refining the impure metal is the anode. Pure metal collects on the cathode. Copper is refined this way.

> **Tip:** Calcination goes with carbonate. Roasting goes with sulphide.

### The reactivity series
$$\text{K} > \text{Na} > \text{Ca} > \text{Mg} > \text{Al} > \text{Zn} > \text{Fe} > \text{Pb} > (\text{H}) > \text{Cu} > \text{Hg} > \text{Ag} > \text{Au}$$

- Metals above hydrogen give H₂ with dilute acids. Copper, silver and gold do not.
- Sodium and potassium are stored under kerosene. White phosphorus is stored under water.
- Gold and platinum are noble metals. They occur free in nature.
- A more reactive metal displaces a less reactive one from its salt solution. An iron nail in copper sulphate turns brown.

### Rusting and corrosion
Rusting needs **both air and moisture**. Rust is hydrated iron oxide, Fe₂O₃·xH₂O.

- **Prevention:** galvanisation (zinc coating), painting, greasing, electroplating, and alloying into stainless steel.
- Silver tarnishes black (Ag₂S). Copper grows a green coat of basic copper carbonate.
- Aluminium protects itself with a thin oxide film. Anodising makes it thicker.

### Alloys
| Alloy | Made of | Use |
|---|---|---|
| Brass | Copper + zinc | Utensils, fittings |
| Bronze | Copper + tin | Statues, medals |
| Bell metal | Copper + more tin | Bells, gongs |
| Gun metal | Copper + tin + zinc | Gears, castings |
| German silver | Copper + zinc + nickel (no silver) | Utensils |
| Solder | Lead + tin | Joins wires; low melting point |
| Stainless steel | Iron + chromium + nickel + carbon | Cutlery |
| Duralumin | Aluminium + copper + magnesium + manganese | Aircraft |
| Magnalium | Aluminium + magnesium | Light instruments |
| Nichrome | Nickel + chromium | Heater coils |
| Invar | Iron + nickel | Pendulums, tapes |
| Amalgam | Any metal + mercury | Dental fillings |

### Gold purity
24 carat is pure gold. Use $\text{Purity}\,(\%) = \dfrac{\text{carat}}{24} \times 100$. So 18 carat is 75%, and 22 carat is about 91.67%. Jewellery gold is mixed with copper or silver to make it hard.
""",
    tricks=[
        trick("Reactivity series sentence",
              "Please Stop Calling Me A Zebra, I Like Her Calling Me Smart Goat gives Potassium, Sodium, Calcium, Magnesium, Aluminium, Zinc, Iron, Lead, Hydrogen, Copper, Mercury, Silver, Gold."),
        trick("Brass or bronze",
              "Brass has zinc. Bronze has tin. Both have copper.",
              "Bronze is an alloy of which metals?",
              ["Bronze is a copper alloy.", "The partner metal is tin."],
              "Copper and tin"),
    ],
    mistakes=[
        mis("Believing German silver contains silver.", "It is copper, zinc and nickel."),
        mis("Naming haematite as an aluminium ore.", "Haematite is iron. Bauxite is aluminium."),
        mis("Saying solder has a high melting point.", "Solder melts easily. That is why it joins wires."),
        mis("Mixing up calcination and roasting.", "Calcination is for carbonates in limited air. Roasting is for sulphides in excess air."),
        mis("Saying brass is copper and tin.", "Brass is copper and zinc. Bronze is copper and tin."),
    ],
    revision=[
        "Calcination: carbonate. Roasting: sulphide. Froth flotation: sulphide ores.",
        "Bauxite: Al. Haematite: Fe. Cinnabar: Hg. Zinc blende: Zn. Galena: Pb. Cassiterite: Sn. Pitchblende: U.",
        "K > Na > Ca > Mg > Al > Zn > Fe > Pb > H > Cu > Hg > Ag > Au.",
        "Cu, Ag and Au give no H₂ with dilute acid.",
        "Brass: Cu + Zn. Bronze: Cu + Sn. Solder: Pb + Sn. Duralumin: Al + Cu. Nichrome: Ni + Cr.",
        "Rusting needs air and moisture. Galvanising is a zinc coat.",
        "Amalgam is a metal with mercury. 24 carat is pure gold.",
    ],
    patterns=[
        pat("ga-mo-p1", "Ore and metal matching", "very common",
            "The question says 'bauxite is the ore of', 'cinnabar is an ore of', or gives a match-the-column of ores and metals.",
            ["Learn the headline pairs: bauxite-Al, haematite-Fe, cinnabar-Hg, galena-Pb.", "Add zinc blende-Zn, cassiterite-Sn, copper pyrites-Cu, pitchblende-U, rock salt-Na.", "Extra ores: calamine is zinc; magnetite and siderite are iron.", "In a match, fix the surest pair first and chain the rest."],
            "Ore names are fixed, so recall by pairs works better than logic.",
            "Cinnabar is an ore of which metal?",
            ["Cinnabar is HgS.", "Hg is mercury."],
            "Mercury"),
        pat("ga-mo-p2", "Alloy and composition", "very common",
            "The question asks 'brass is an alloy of', 'which alloy contains tin', or what is added to iron for stainless steel.",
            ["Copper family: brass Cu + Zn, bronze Cu + Sn, bell metal Cu + more Sn, German silver Cu + Zn + Ni.", "Iron family: stainless steel Fe + Cr + Ni, invar Fe + Ni.", "Others: duralumin Al + Cu, magnalium Al + Mg, solder Pb + Sn, nichrome Ni + Cr.", "Amalgam always has mercury."],
            "Each alloy has a fixed recipe, and the second metal is what exams test.",
            "Brass is an alloy of which metals?",
            ["Brass is a copper alloy.", "The partner is zinc, not tin."],
            "Copper and zinc"),
        pat("ga-mo-p3", "Metallurgy steps and processes", "common",
            "The question says 'roasting is used for', 'calcination vs roasting', 'froth flotation', or 'which metal is extracted by electrolysis'.",
            ["Concentrate the ore. Froth flotation is for sulphide ores.", "Calcination: carbonate ore, limited air. Roasting: sulphide ore, excess air.", "Reduce with carbon (iron) or by electrolysis (Al, Na).", "Refine copper electrolytically with the impure metal as the anode."],
            "Each step prepares the ore for the next, from ore to pure metal.",
            "Roasting is done for which type of ore?",
            ["Roasting uses excess air.", "It turns sulphides into oxides and drives off SO₂."],
            "Sulphide ores"),
        pat("ga-mo-p4", "Reactivity series consequences", "common",
            "The question asks which metal gives no H₂ with dilute acid, why sodium is kept in kerosene, or which metal occurs free.",
            ["Write the series: K, Na, Ca, Mg, Al, Zn, Fe, Pb, H, Cu, Hg, Ag, Au.", "Metals above H give H₂ with dilute acids.", "Top metals burn in moist air, so keep them under kerosene.", "Bottom metals occur free. A more reactive metal displaces a less reactive one."],
            "Position in the series tells you how eagerly a metal reacts.",
            "Which metal will not liberate hydrogen from dilute hydrochloric acid?",
            ["Find hydrogen in the series.", "Copper lies below it."],
            "Copper (also silver, gold, mercury)"),
        pat("ga-mo-p5", "Corrosion and its prevention", "common",
            "The question says 'rusting requires', 'galvanisation is coating with', 'green coating on copper', or 'anodising is done on'.",
            ["Rusting needs air and moisture together.", "Prevent with galvanising, paint, oil, electroplating, anodising or alloying.", "Colours: iron is red-brown rust; copper is green; silver is black."],
            "Each prevention method keeps air or water away from the metal.",
            "A green coating slowly forms on a copper vessel left in damp air. What is it?",
            ["Copper reacts slowly with moist air.", "It forms basic copper carbonate."],
            "Basic copper carbonate (silver turns black with Ag₂S)"),
        pat("ga-mo-p6", "Metal and non-metal exceptions, gold carat", "common",
            "The question asks which metal is liquid or soft, which non-metal conducts, the most ductile metal, or a carat purity.",
            ["Exceptions: Hg liquid; Na and K soft; graphite conducts; iodine lustrous.", "Best metal conductor: silver. Most ductile: gold. Highest melting point: tungsten.", "Purity = carat ÷ 24 × 100."],
            "The exceptions break the general rule, so questions love them.",
            "Which non-metal conducts electricity?",
            ["Carbon layers in graphite hold free electrons.", "These carry current."],
            "Graphite"),
    ],
)
