"""Chemistry part 1: ch-matter-atom, ch-periodic."""
from _ch_common import pat, mis, trick

S = {}

# numeric checks used in examples
assert 1 * 600 == 1.5 * 400
assert 2 * 18 == 36 and 36 // 18 == 2
assert 2 * 3 ** 2 == 18
assert 3 * 400 / 300 == 4
assert abs(9 / 18 * 6.022e23 - 3.011e23) < 1e17

# =====================================================================
S["ch-matter-atom"] = dict(
    concept=(
        "Matter is anything with mass that takes up space. This lesson covers its states, how to separate mixtures, "
        "and what an atom is made of. It ends with the mole and two gas laws. "
        "Most questions are fact recall, plus one or two small calculations."
    ),
    notes=r"""### States of matter
Matter is anything that has mass and takes up space. It has five states.

- **Solid, liquid and gas** are the three everyday states.
- **Plasma** is the fourth state. It is ionised gas, found in the Sun, stars, lightning and neon signs.
- **Bose-Einstein condensate** is the fifth state. Matter is cooled almost to absolute zero. S.N. Bose and Einstein predicted it.

**Sublimation** is a solid turning straight into vapour. Five substances are the exam favourites: camphor, naphthalene balls, iodine, ammonium chloride and dry ice (solid CO₂).

### Physical and chemical change
A **physical change** alters only the form. It is reversible, and no new substance forms. Melting ice and dissolving sugar are examples.

A **chemical change** makes a new substance. Burning, rusting, curdling of milk, cooking and digestion are examples.

> **Tip:** Ask one question: is a new substance made? Yes means chemical. No means physical.

### Separating mixtures
A mixture keeps the properties of its parts. Match the method to the job.

| Method | Use |
|---|---|
| Chromatography | Dyes in ink, pigments, drugs in blood |
| Distillation | Liquids with very different boiling points; pure water |
| Fractional distillation | Petroleum parts, liquefied air |
| Centrifugation | Cream from milk, blood tests |
| Sublimation | Salt mixed with camphor or ammonium chloride |
| Crystallisation | Pure salt or copper sulphate from a solution |
| Separating funnel | Immiscible liquids such as oil and water |
| Filtration, evaporation, magnet | Insoluble solid, dissolved solid, iron filings from sand |

### Solutions and colloids
A **solution** (sugar in water) is clear and never settles. A **suspension** (muddy water) is cloudy and settles down.

A **colloid** lies in between. Its particles are too small to see. They still scatter a light beam. This is the **Tyndall effect**. The particles also zig-zag constantly. This is **Brownian motion**.

- Milk is an **emulsion** (liquid in liquid).
- Fog and clouds are an **aerosol** (liquid in gas).
- Smoke is a solid in gas.
- Shaving cream is a foam. Jelly is a gel.

> **Watch:** A true solution does not show the Tyndall effect. Only colloids and suspensions do.

### Inside the atom
| Particle | Found by | Charge |
|---|---|---|
| Electron | J.J. Thomson (1897, cathode rays) | -1 |
| Proton | Goldstein (canal rays); identified by Rutherford | +1 |
| Neutron | James Chadwick (1932) | 0 |

The atomic models came in this order.

1. **Dalton:** atoms cannot be split.
2. **Thomson:** plum-pudding model.
3. **Rutherford:** gold-foil experiment showed a tiny, dense nucleus.
4. **Bohr:** electrons move in fixed orbits (shells).

### Atomic number, isotopes and shells
**Atomic number Z** is the number of protons. **Mass number A** is protons plus neutrons.

- **Isotopes:** same Z, different A. Hydrogen has protium (¹H), deuterium (²H) and tritium (³H). Tritium is radioactive.
- Chlorine is ³⁵Cl and ³⁷Cl. Its average mass is 35.5. Carbon-14 is used to date old remains.
- **Isobars:** same A, different Z. Argon-40 and calcium-40 are an example.
- **Isotones:** same number of neutrons.

Shell n holds at most $2n^{2}$ electrons. So K holds 2, L holds 8 and M holds 18. The outer electrons are the valence electrons.

### The mole and the gas laws
One **mole** holds $6.022 \times 10^{23}$ particles. This is Avogadro's number. One mole weighs its molar mass in grams. So 18 g of water is 1 mole, and 44 g of CO₂ is 1 mole.

- **Boyle's law:** at fixed temperature, $P_1V_1 = P_2V_2$.
- **Charles's law:** at fixed pressure, volume rises with kelvin temperature.

> **Rule:** In Charles's law, always change °C to kelvin first. Add 273.
""",
    tricks=[
        trick("Iso-words by the letter",
              "Isotopes share the atomic number (P for protons). Isobars share A, the mass number. Isotones share neutrons.",
              "Deuterium and tritium are what to each other?",
              ["Both are hydrogen, so atomic number is 1.", "Mass numbers differ: 2 and 3."],
              "Isotopes"),
        trick("Sublimation list: CNIAD",
              "Camphor, Naphthalene, Iodine, Ammonium chloride, Dry ice. If an option is on this list, it sublimes."),
    ],
    mistakes=[
        mis("Calling milk a true solution.", "Milk is a colloid (an emulsion). It scatters light."),
        mis("Saying tritium is stable.", "Tritium is the radioactive isotope of hydrogen."),
        mis("Treating rusting or curdling as a physical change.", "Both make new substances, so both are chemical changes."),
        mis("Using Celsius in Charles's law.", "Add 273 to get kelvin before you divide."),
        mis("Using distillation for petroleum.", "Its parts boil close together. Use fractional distillation."),
    ],
    revision=[
        "Five states: solid, liquid, gas, plasma, Bose-Einstein condensate.",
        "Sublimation: camphor, naphthalene, iodine, ammonium chloride, dry ice.",
        "Chromatography for dyes; fractional distillation for petroleum; centrifuge for cream; funnel for oil and water.",
        "Colloid shows Tyndall effect and Brownian motion. Milk is an emulsion. Fog is an aerosol.",
        "Electron: Thomson. Nucleus: Rutherford. Orbits: Bohr. Neutron: Chadwick.",
        "Shell capacity is 2n². K = 2, L = 8, M = 18.",
        "One mole = 6.022 × 10²³ particles. 18 g of water = 1 mole. PV = nRT.",
    ],
    patterns=[
        pat("ga-ma-p1", "Physical vs chemical change; sublimation and states", "very common",
            "The question asks 'which is a chemical change', 'which sublimes', the 4th or 5th state, or 'dry ice is'.",
            ["Ask: is a new substance formed?", "Yes: chemical (burning, rusting, curdling, cooking, digestion). No: physical.", "For sublimation, pick from camphor, naphthalene, iodine, ammonium chloride, dry ice.", "For states: plasma is ionised gas; BEC is near absolute zero."],
            "The two change types differ only in whether a new substance appears.",
            "Burning of a candle involves which change?",
            ["Melting of wax is physical.", "Burning of the vapour is chemical."],
            "Both physical and chemical changes"),
        pat("ga-ma-p2", "Separation method and mixture", "very common",
            "The question asks 'which method separates cream from milk, petroleum parts, or dyes in ink', or gives a match-the-column.",
            ["Find the property that differs: boiling point, density, solubility, magnetism.", "Close boiling points: fractional distillation. Different densities: centrifugation.", "Immiscible liquids: separating funnel. Dyes: chromatography.", "Cream from milk is always centrifugation."],
            "Each method uses one physical property that differs between the parts.",
            "The components of petroleum are separated by which method?",
            ["The parts boil only a few degrees apart.", "A fractionating column is needed."],
            "Fractional distillation"),
        pat("ga-ma-p3", "Colloids, Tyndall effect and Brownian motion", "common",
            "The question says 'milk is an example of', 'scattering of light by particles is called', or 'which shows the Tyndall effect'.",
            ["Name the dispersed phase and the medium.", "Liquid in liquid is an emulsion; liquid in gas is an aerosol; solid in gas is smoke.", "Light scattering is the Tyndall effect. Zig-zag motion is Brownian motion.", "A true solution never shows the Tyndall effect."],
            "Colloid particles are big enough to scatter light but too small to settle.",
            "Fog is a colloid in which what is spread in what?",
            ["Water droplets are liquid.", "Air is the gas medium."],
            "Liquid in gas, an aerosol"),
        pat("ga-ma-p4", "Atomic models and discoverers", "common",
            "The question asks who proposed the plum-pudding, nuclear or orbit model, or which experiment found the nucleus.",
            ["Recall the order: Dalton, Thomson, Rutherford, Bohr, Chadwick.", "Thomson: electron and plum pudding. Rutherford: nucleus. Bohr: orbits.", "In the gold-foil test most alpha particles passed straight through. A few bounced back."],
            "Each scientist added one part to the picture of the atom.",
            "Rutherford's gold-foil experiment proved what?",
            ["Most alpha particles went straight through.", "A few bounced back."],
            "The atom has a tiny, dense, positive nucleus"),
        pat("ga-ma-p5", "Isotopes, isobars, atomic number and shells", "common",
            "The question says 'same atomic number, different mass number', asks the hydrogen isotopes, or asks electrons in a shell.",
            ["Same Z, different A: isotopes. Same A, different Z: isobars.", "Hydrogen isotopes: ¹H, ²H, ³H. Chlorine: ³⁵Cl and ³⁷Cl, average 35.5.", "Shell n holds 2n² electrons. Calcium (Z = 20) is 2, 8, 8, 2."],
            "The atomic number sets the element. The mass number only counts the heavier particles.",
            "How many electrons can the M shell hold at most?",
            ["M is the third shell, so n = 3.", "2n² = 2 × 9 = 18."],
            "18",
            formula=r"Z=\text{protons},\quad A=\text{protons}+\text{neutrons},\quad \text{shell }n\text{ holds }2n^2"),
        pat("ga-ma-p6", "Mole and gas-law numericals", "occasional",
            "You get a mass and must find moles or molecules, or a Boyle or Charles change of volume, pressure or temperature.",
            ["Find the molar mass first: H₂O is 18, CO₂ is 44.", "Moles = given mass ÷ molar mass.", "Boyle: equate the two products P × V.", "Charles: convert to kelvin, then equate V ÷ T."],
            "A mole is a counting unit, and the gas laws are simple proportions.",
            "A gas takes 600 mL at 1 atm. What pressure squeezes it into 400 mL at the same temperature?",
            ["Boyle: P₁V₁ = P₂V₂.", "1 × 600 = P₂ × 400.", "P₂ = 600 ÷ 400 = 1.5."],
            "1.5 atm",
            formula=r"\text{moles}=\frac{\text{mass}}{\text{molar mass}},\quad P_1V_1=P_2V_2\ (\text{at fixed }T),\quad \frac{V_1}{T_1}=\frac{V_2}{T_2}\ (\text{at fixed }P)"),
    ],
)

# =====================================================================
S["ch-periodic"] = dict(
    concept=(
        "The periodic table arranges all elements in order of atomic number. Its columns are groups and its rows are periods. "
        "Elements in one group behave alike, and properties change in a steady way across a period and down a group. "
        "Exams also ask fixed record-holders and Latin-name symbols."
    ),
    notes=r"""### How the table grew
Chemists needed a map for the elements they kept finding. Four names matter.

| Scientist | Idea |
|---|---|
| Döbereiner | Triads, such as Li, Na, K |
| Newlands | Law of octaves: every 8th element is similar |
| Mendeleev | Table built on atomic mass, with gaps left for unknown elements |
| Moseley | Modern periodic law: properties depend on atomic number |

Mendeleev predicted eka-aluminium and eka-silicon. They turned out to be gallium and germanium.

> **Watch:** Mendeleev used atomic mass. Moseley used atomic number.

### Reading the modern table
The modern table has **18 groups** (vertical) and **7 periods** (horizontal). It names **118 elements**. Elements in one group have the same number of outer electrons, so they behave alike.

| Region | Members |
|---|---|
| Group 1 | Alkali metals: Li, Na, K. Very reactive. |
| Group 2 | Alkaline earth metals: Be, Mg, Ca |
| Groups 3-12 | Transition metals: Fe, Cu, Zn, Ag, Au |
| Group 17 | Halogens: F, Cl, Br, I |
| Group 18 | Noble gases: He, Ne, Ar, Kr, Xe, Rn |
| Two bottom rows | Lanthanides and actinides |

Noble gases have full outer shells. This is why they are inert.

### Trends in the table
- **Across a period (left to right):** atomic size falls. Metallic character falls. Electronegativity (pull on electrons) rises.
- **Down a group (top to bottom):** atomic size rises. Metallic character rises. Metals get more reactive, so K is wilder than Na.

Sodium is a metal. Chlorine, at the far right, is a non-metal. **Fluorine** is the most electronegative element.

> **Tip:** Picture the table. Reactive non-metals sit at the top right. Reactive metals sit at the bottom left.

### Record-holders
| Record | Answer |
|---|---|
| Most abundant in the universe | Hydrogen |
| Most abundant in Earth's crust | Oxygen, then silicon |
| Most abundant metal in the crust | Aluminium, then iron |
| Most abundant gas in air | Nitrogen (about 78%) |
| Most abundant in the human body | Oxygen (top metal: calcium) |
| Lightest element / lightest metal | Hydrogen / Lithium |
| Liquid metal / liquid non-metal | Mercury / Bromine |
| Metal that melts in the palm | Gallium (about 30 °C) |
| Hardest natural substance | Diamond |
| Softest mineral | Talc |
| Best metal conductor | Silver |
| Most ductile and malleable metal | Gold |
| Highest melting point metal | Tungsten |
| Densest natural element | Osmium |
| First man-made element | Technetium |
| Non-metal that conducts | Graphite |

The crust order is **OSAIC**: Oxygen, Silicon, Aluminium, Iron, Calcium.

### Symbols from Latin names
Some symbols come from Latin names. They are common exam traps.

| Symbol | Latin name | Element |
|---|---|---|
| Na | natrium | Sodium |
| K | kalium | Potassium |
| Fe | ferrum | Iron |
| Cu | cuprum | Copper |
| Ag | argentum | Silver |
| Au | aurum | Gold |
| Pb | plumbum | Lead |
| Sn | stannum | Tin |
| Hg | hydrargyrum | Mercury |
| Sb | stibium | Antimony |
| W | wolfram | Tungsten |

> **Watch:** The symbol for sodium is Na, never So.

### Noble gases and metalloids
- **Helium:** balloons, airships and deep-sea diver breathing mixes.
- **Neon:** advertising signs with an orange-red glow.
- **Argon:** filled inside electric bulbs.
- **Xenon:** flash lamps. **Radon** is radioactive.
- **Metalloids:** boron, silicon, germanium, arsenic, antimony, tellurium.
""",
    tricks=[
        trick("Crust order: OSAIC",
              "Oxygen, Silicon, Aluminium, Iron, Calcium. So the top element is O and the top metal is Al.",
              "Which is the most abundant metal in the Earth's crust?",
              ["Read OSAIC and skip the non-metals O and Si.", "The first metal is aluminium."],
              "Aluminium"),
        trick("Two liquids at room temperature",
              "Mercury is the liquid metal. Bromine is the liquid non-metal. Gallium and caesium melt just above room temperature."),
    ],
    mistakes=[
        mis("Saying Mendeleev's table used atomic number.", "Mendeleev used atomic mass. Moseley used atomic number."),
        mis("Naming iron as the most abundant metal in the crust.", "It is aluminium. Iron comes second."),
        mis("Naming oxygen as the most abundant gas in air.", "It is nitrogen, about 78%. Oxygen is about 21%."),
        mis("Writing the symbol of sodium as So.", "Use the Latin name: natrium gives Na."),
        mis("Thinking size grows across a period.", "Size falls left to right and rises down a group."),
    ],
    revision=[
        "Döbereiner triads, Newlands octaves, Mendeleev atomic mass, Moseley atomic number.",
        "18 groups, 7 periods, 118 elements.",
        "Group 1 alkali, group 2 alkaline earth, group 17 halogens, group 18 noble gases.",
        "Across a period size and metallic character fall. Down a group both rise.",
        "Fluorine is the most electronegative element.",
        "Hydrogen: universe. Oxygen: crust. Aluminium: crust metal. Nitrogen: air.",
        "Li lightest metal, Hg liquid metal, Br liquid non-metal, Au most ductile, W highest melting point.",
    ],
    patterns=[
        pat("ga-pe-p1", "Element record-holders", "very common",
            "The question says 'most abundant', 'lightest metal', 'only liquid metal', 'hardest natural substance' or 'first man-made element'.",
            ["Match the phrase to the record table.", "Abundance chain: H (universe), O (crust), Al (crust metal), N (air), O (body).", "Oddities: Li lightest metal, Hg liquid metal, Br liquid non-metal, graphite conducts.", "In odd-one-out questions, check the records first."],
            "These records are fixed facts, so recall is the only route.",
            "The most abundant metal in the Earth's crust is which?",
            ["Oxygen is the top element but not a metal.", "Aluminium (about 8%) comes before iron."],
            "Aluminium"),
        pat("ga-pe-p2", "Symbols from Latin names", "common",
            "A list of symbol and element pairs is given, and you must find the wrong pair.",
            ["Learn the eleven Latin symbols.", "Check each pair against the Latin name.", "The wrong pair is almost always one of these eleven.", "Other symbols follow the English name (He, Ca, Zn)."],
            "The Latin names explain symbols that do not match the English name.",
            "Which pair is wrong? (a) Fe-Iron (b) Au-Gold (c) Ag-Silver (d) So-Sodium",
            ["Sodium comes from natrium.", "Its symbol is Na."],
            "(d)"),
        pat("ga-pe-p3", "History of classification", "common",
            "The question asks who gave the law of octaves, what Mendeleev's table was based on, or what eka-silicon is now called.",
            ["Recall the chain: Döbereiner, Newlands, Mendeleev, Moseley.", "Mendeleev used atomic mass and left gaps.", "Eka-aluminium became gallium. Eka-silicon became germanium.", "Modern periods follow atomic number."],
            "Each step fixed a weakness in the one before it.",
            "Mendeleev's eka-silicon is today's which element?",
            ["Mendeleev left a gap under silicon.", "The element found later fits that gap."],
            "Germanium"),
        pat("ga-pe-p4", "Groups, periods and trends", "common",
            "The question asks how size or metallic character changes across a period or down a group, or how many groups exist.",
            ["Remember the fixed numbers: 18 groups, 7 periods, 118 elements.", "Across a period: size and metallic character fall.", "Down a group: size and metallic character rise.", "Most reactive non-metal is F. Most reactive metals are at the bottom left."],
            "More shells down a group put the outer electrons farther away, so they leave easily.",
            "Moving down a group, what happens to metallic character?",
            ["Outer electrons are farther from the nucleus.", "They are lost more easily, so K is more reactive than Na."],
            "It increases"),
        pat("ga-pe-p5", "Group families (alkali, halogens, noble gases)", "common",
            "The question asks which group holds halogens or noble gases, why group 18 is inert, or which metal is kept in kerosene.",
            ["Group 1 is alkali: Li, Na, K. They are soft, reactive and kept in kerosene.", "Group 17 is halogens: F, Cl, Br, I.", "Group 18 is noble gases with full outer shells.", "Helium is first in group 18. Radon is radioactive."],
            "A full outer shell means the atom has no need to give, take or share electrons.",
            "Why are noble gases chemically inert?",
            ["Look at the outer shell.", "It is already complete."],
            "Their outer shells are full, so they do not give, take or share electrons easily"),
    ],
)
