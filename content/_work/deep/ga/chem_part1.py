"""chemistry deep content — part 1: ch-matter-atom, ch-periodic."""
import os
import sys

sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
from _lib import Sub


def g(x):
    x = round(x, 6)
    return str(int(x)) if x == int(x) else str(x)


def build_matter():
    S = Sub("ch-matter-atom")
    S.notes = """### What is matter, and what forms does it take?
Anything that has mass and occupies space is **matter**. Besides the familiar **solid, liquid and gas**, science knows two more states: **plasma** (ionised gas — the Sun, stars, lightning, neon signs) and the **Bose–Einstein condensate** (matter cooled almost to absolute zero; predicted by S.N. Bose and Einstein).
Changes of state: melting, boiling, condensation, freezing, and **sublimation** — a solid passing straight to vapour. The sublimation set is a fixed exam list: **camphor, naphthalene balls, iodine, ammonium chloride, dry ice (solid CO₂)**.
A **physical change** changes only the form and is reversible (melting ice, dissolving sugar). A **chemical change** makes a new substance that cannot be brought back by simple means — burning, rusting, curdling of milk, cooking, digestion.

### Mixtures and how we separate them
A mixture keeps the properties of its parts; a compound does not. Separation method ↔ job:
| Method | Used for |
|---|---|
| **Chromatography** | Dyes in ink, pigments, drugs in blood |
| **Distillation** | Two liquids with very different boiling points (pure water from salt water) |
| **Fractional distillation** | Liquids boiling close together — **petroleum**, liquid air |
| **Centrifugation** | **Cream from milk**, blood/urine tests |
| **Sublimation** | Salt mixed with camphor or ammonium chloride |
| **Crystallisation** | Pure salt/copper sulphate crystals from a solution |
| **Separating funnel** | Immiscible liquids — oil and water |
| **Filtration / evaporation / magnetic separation** | Insoluble solid / dissolved solid / iron filings from sand |

### Solutions, suspensions, colloids
A **solution** (sugar in water) is clear and never settles. A **suspension** (muddy water) is cloudy and settles on standing. A **colloid** sits between the two: particles too small to see, big enough to **scatter a beam of light — the Tyndall effect** — and they jiggle constantly (**Brownian motion**). Colloid types to remember: **milk = emulsion** (liquid in liquid), **fog/clouds = aerosol** (liquid in gas), **smoke = solid in gas**, shaving cream = foam (gas in liquid), jelly = gel (liquid in solid).

### Inside the atom
- **Dalton** proposed that matter is made of indivisible atoms; **J.J. Thomson** found the **electron** and suggested a plum-pudding model; **Rutherford's gold-foil experiment** showed a tiny dense **nucleus**; **Bohr** added fixed **orbits (shells)**; **Chadwick** found the **neutron**.
- **Atomic number Z** = number of protons (the identity of the element). **Mass number A** = protons + neutrons.
- **Isotopes** — same Z, different A: hydrogen has **protium (¹H), deuterium (²H), tritium (³H)**; chlorine is ³⁵Cl and ³⁷Cl (average mass 35.5); **carbon-14** dates old remains. **Isobars** — same A, different Z (e.g. calcium-40 and argon-40).
- Electrons fill shells by the **2n² rule**: K holds 2, L holds 8, M holds 18; the outermost electrons are **valence electrons**; a full outer shell (octet) is stable.

### Counting particles — the mole
One **mole** of any substance holds **6.022 × 10²³ particles** (Avogadro's number) and weighs its molecular mass in grams. So **18 g of water = 1 mole**, and 36 g = 2 moles; 44 g of CO₂ = 1 mole. **Boyle's law**: at constant temperature, pressure × volume stays fixed (squeeze a gas, pressure rises). **Charles's law**: at constant pressure, volume grows in step with the kelvin temperature. Together: PV = nRT.

### Quick revision
- 5 states: solid, liquid, gas, **plasma**, Bose–Einstein condensate.
- Sublimation set: camphor, naphthalene, iodine, ammonium chloride, dry ice.
- Chromatography–dyes; fractional distillation–petroleum; centrifuge–cream; funnel–oil and water.
- Colloid = Tyndall + Brownian; milk = emulsion, fog = aerosol, smoke = solid in gas.
- Electron–Thomson, nucleus–Rutherford, orbits–Bohr, neutron–Chadwick.
- 1 mole = 6.022 × 10²³ particles; 18 g water = 1 mol; PV = nRT."""
    S.pattern("ga-ma-p1", "Physical vs chemical change; sublimation and states", "very common",
        "'Which is a chemical change?', 'which sublimes?', 4th/5th state of matter, 'dry ice is…'.",
        None,
        "1. New substance formed → chemical change (burning, rusting, curdling, cooking, digestion); only form changed → physical (melting, dissolving).\n2. Sublimation list: camphor, naphthalene, iodine, ammonium chloride, dry ice — nothing else sublimes at room pressure.\n3. Plasma = ionised gas in the Sun, lightning, neon signs; BEC = near absolute zero.\nWhy: the two change classes differ only in whether a NEW substance appears.",
        "Burning of a candle involves —",
        "**Both** changes: melting of wax is physical, burning of the vapour is chemical.")
    S.pattern("ga-ma-p2", "Separation method ↔ mixture", "very common",
        "'Which method separates cream from milk / components of petroleum / dyes in ink?', match-the-column of methods and mixtures.",
        None,
        "1. Match by property: different boiling points → distillation (close boiling points → fractional, e.g. petroleum); different densities → centrifugation (cream, blood); different solubility/movement → chromatography (dyes).\n2. Immiscible liquids → separating funnel; dissolved solid → evaporation/crystallisation; magnetic material → magnetic separation; sublimable solid in a mixture → sublimation.\n3. Cream-from-milk is ALWAYS centrifugation in exams.",
        "The components of **petroleum** are separated by —",
        "**Fractional distillation** — the fractions boil only a few degrees apart, so a fractionating column is needed.")
    S.pattern("ga-ma-p3", "Colloids, Tyndall effect and Brownian motion", "common",
        "'Milk is an example of…', 'scattering of light by colloidal particles is called…', which of these shows the Tyndall effect.",
        None,
        "1. Classify by dispersed phase and medium: milk = liquid in liquid = **emulsion**; fog/cloud = liquid in gas = **aerosol**; smoke = solid in gas; shaving cream = foam; jelly = gel.\n2. Light scattering by colloidal particles = **Tyndall effect**; zig-zag motion of colloidal particles = **Brownian motion**.\n3. True solutions do NOT show the Tyndall effect; suspensions do but settle down.",
        "**Fog** is a colloid in which —",
        "Water droplets (liquid) are dispersed in air (gas) — an **aerosol**.")
    S.pattern("ga-ma-p4", "Atomic models and discoverers", "common",
        "'Who proposed the plum-pudding / nuclear / planetary model?', 'which experiment discovered the nucleus?', order of models in history.",
        None,
        "1. Timeline: Dalton (atoms indivisible) → Thomson (electron; plum pudding) → Rutherford (gold foil; nucleus) → Bohr (fixed orbits) → Chadwick (neutron).\n2. Gold-foil: most alpha particles passed, few bounced → atom is mostly empty with a tiny dense positive nucleus.\n3. Bohr's orbits are the K, L, M… shells filled by the 2n² rule (2, 8, 18…).",
        "Rutherford's **gold-foil experiment** proved that —",
        "The atom has a tiny, dense, positively charged **nucleus** — most alpha particles passed straight through the foil.")
    S.pattern("ga-ma-p5", "Isotopes, isobars, atomic number and shells", "common",
        "'Same atomic number but different mass number = ?' hydrogen isotopes, average mass of chlorine, electrons in a given shell for element X.",
        r"Z=\text{protons},\quad A=\text{protons}+\text{neutrons},\quad \text{shell }n\text{ holds }2n^2",
        "1. Isotopes: same Z, different A (¹H, ²H, ³H; ³⁵Cl and ³⁷Cl → average 35.5).\n2. Isobars: same A, different Z (Ca-40, Ar-40).\n3. Shell filling 2n²: K = 2, L = 8, M = 18; for calcium (Z = 20) the arrangement is 2, 8, 8, 2.",
        "How many electrons can the **M shell** hold at most?",
        "2n² with n = 3 → 2 × 9 = **18**.")
    S.pattern("ga-ma-p6", "Mole and gas-law numericals", "occasional",
        "Moles from a given mass, number of molecules, or a Boyle/Charles volume-pressure-temperature change.",
        r"\text{moles}=\frac{\text{mass}}{\text{molar mass}},\quad P_1V_1=P_2V_2\ (\text{at fixed }T),\quad \frac{V_1}{T_1}=\frac{V_2}{T_2}\ (\text{at fixed }P)",
        "1. Find molar mass first: H₂O = 18, CO₂ = 44. Moles = given mass ÷ molar mass.\n2. Boyle: multiply each state's P and V, equate the two products.\n3. Charles: convert temperatures to **kelvin** (add 273) before dividing.\nWhy: a mole is just a counting unit, and the gas laws are simple proportionalities.",
        "A gas occupies **600 mL at 1 atm**. What pressure will squeeze it into **400 mL** at the same temperature?",
        "P₁V₁ = P₂V₂ → 1 × 600 = P₂ × 400 → P₂ = **1.5 atm**.")

    m = 36 / 18
    assert m == 2
    S.q("ga-ma-p1", "easy", "Which of the following is a **chemical** change?",
        ["Rusting of iron", "Melting of wax", "Dissolving sugar in water", "Boiling of water"], "Rusting of iron",
        "Rusting forms a **new substance (iron oxide)** and cannot be reversed by simple means. Melting, dissolving and boiling change only the form — physical changes.",
        None, 15)
    S.q("ga-ma-p1", "easy", "**Dry ice** is —",
        ["Solid carbon dioxide", "Frozen water vapour", "Solid camphor", "Ice at −40 °C"], "Solid carbon dioxide",
        "**Dry ice** is solid CO₂, which sublimes directly into gas — used for cooling and stage effects.",
        None, 15)
    S.q("ga-ma-p1", "medium", "Which of the following does **NOT** sublime?",
        ["Common salt", "Camphor", "Naphthalene", "Iodine"], "Common salt",
        "The sublimation set is **camphor, naphthalene, iodine, ammonium chloride and dry ice**. Common salt stays solid and is separated from camphor exactly by sublimation.",
        None, 15)
    S.q("ga-ma-p2", "easy", "**Cream is separated from milk** by —",
        ["Centrifugation", "Filtration", "Sublimation", "Chromatography"], "Centrifugation",
        "Spinning in a **centrifuge** throws the denser skimmed milk outward and collects the lighter cream at the centre.",
        None, 15)
    S.q("ga-ma-p2", "medium", "**Dyes in ink** can be separated by —",
        ["Chromatography", "Distillation", "Decantation", "Winnowing"], "Chromatography",
        "In **chromatography** the dye parts travel different distances up the paper because they dissolve and stick differently — used to separate dyes, pigments and drugs.",
        None, 15)
    S.q("ga-ma-p2", "medium", "A **mixture of salt and camphor** is separated by —",
        ["Sublimation", "Filtration", "Separating funnel", "Magnetic separation"], "Sublimation",
        "Camphor **sublimes** on heating and its vapour condenses on a cold surface, leaving salt behind.",
        None, 15)
    S.q("ga-ma-p3", "easy", "**Milk** is an example of —",
        ["Emulsion", "Aerosol", "Foam", "Gel"], "Emulsion",
        "Milk is liquid fat droplets dispersed in water — an **emulsion** (liquid in liquid). Fog is an aerosol; smoke is solid in gas.",
        None, 15)
    S.q("ga-ma-p3", "medium", "The **scattering of a beam of light** by colloidal particles is called the —",
        ["Tyndall effect", "Brownian motion", "Raman effect", "Photoelectric effect"], "Tyndall effect",
        "The **Tyndall effect** makes the beam's path visible in fog or a colloidal solution. **Brownian motion** is the zig-zag jitter of the particles themselves.",
        None, 15)
    S.q("ga-ma-p4", "easy", "The **plum-pudding model** of the atom was proposed by —",
        ["J.J. Thomson", "Ernest Rutherford", "Niels Bohr", "John Dalton"], "J.J. Thomson",
        "After discovering the electron, **Thomson** imagined electrons embedded in a positive sphere like plums in a pudding. Rutherford later replaced it with the nuclear model.",
        None, 15)
    S.q("ga-ma-p4", "medium", "The correct historical **order of atomic models** is —",
        ["Dalton → Thomson → Rutherford → Bohr", "Thomson → Dalton → Bohr → Rutherford", "Bohr → Rutherford → Thomson → Dalton", "Rutherford → Dalton → Thomson → Bohr"], "Dalton → Thomson → Rutherford → Bohr",
        "Dalton's indivisible atoms (1803), Thomson's electron model (1897), Rutherford's nuclear model (1911), Bohr's orbits (1913).",
        None, 20)
    S.q("ga-ma-p5", "medium", "Atoms of the same element with **different mass numbers** are called —",
        ["Isotopes", "Isobars", "Isotones", "Isomers"], "Isotopes",
        "**Isotopes** share the atomic number Z but differ in neutrons (¹H, ²H, ³H). Isobars share the mass number A instead.",
        None, 15)
    S.q("ga-ma-p5", "medium", "The average atomic mass of chlorine (³⁵Cl and ³⁷Cl) is about **35.5** because —",
        ["The two isotopes occur in the ratio 3 : 1", "Chlorine has 35.5 protons", "All atoms are identical", "Its electrons add extra mass"], "The two isotopes occur in the ratio 3 : 1",
        "³⁵Cl is about three times as abundant as ³⁷Cl, so the weighted average works out near **35.5**.",
        None, 20)
    S.q("ga-ma-p5", "hard", "Calcium has atomic number **20**. The electron arrangement **2, 8, 8, 2** means its M shell holds —",
        ["8 electrons", "2 electrons", "18 electrons", "10 electrons"], "8 electrons",
        "Filling order: K = 2, L = 8, then M begins; for calcium it stops at **8** before the N shell takes the last 2. (The M shell's maximum by 2n² is 18, but the actual count here is 8.)",
        None, 25)
    mol = 36 / 18
    assert mol == 2
    S.q("ga-ma-p6", "easy", "How many **moles** are there in **36 g of water**? (H₂O = 18 g/mol)",
        [g(mol) + " moles", "1 mole", "18 moles", "0.5 mole"], g(mol) + " moles",
        "Moles = mass ÷ molar mass = 36 ÷ 18 = **2 moles**.",
        None, 20)
    p2 = 1 * 600 / 400
    assert p2 == 1.5
    S.q("ga-ma-p6", "medium", "A gas fills **600 mL at 1 atm**. At constant temperature, the pressure needed to compress it to **400 mL** is —",
        [g(p2) + " atm", "0.67 atm", "2.5 atm", "600 atm"], g(p2) + " atm",
        "Boyle's law: P₁V₁ = P₂V₂ → 1 × 600 = P₂ × 400 → P₂ = **1.5 atm**. (0.67 atm comes from dividing the wrong way.)",
        None, 30)
    v2 = 300 * 400 / 300
    assert v2 == 400
    S.q("ga-ma-p6", "hard", "A gas occupies **300 mL at 27 °C**. Keeping the pressure constant, its volume at **127 °C** will be —",
        [g(v2) + " mL", g(300 * 127 / 27) + " mL", "225 mL", "300 mL"], g(v2) + " mL",
        "Charles's law needs **kelvin**: 27 °C = 300 K, 127 °C = 400 K. V₂ = 300 × 400/300 = **400 mL**. Using Celsius directly is the standard error.",
        None, 35)
    return S


def build_periodic():
    S = Sub("ch-periodic")
    S.notes = """### How the table grew
Chemists kept discovering elements, so they needed a map. **Döbereiner** noticed **triads** (Li–Na–K: the middle element's mass is the average of the other two). **Newlands** arranged elements by mass and found every 8th one similar — the **law of octaves**. **Mendeleev** made the real breakthrough: a table built on **atomic mass**, in which he left gaps and predicted unknown elements — his **eka-aluminium turned out to be gallium** and **eka-silicon, germanium**. Finally **H.G.J. Moseley** showed that properties depend on **atomic number**, not mass — the **modern periodic law** — and the modern table was born.

### Reading the modern table
The modern (long-form) table has **18 vertical groups** and **7 horizontal periods**; **118 elements** are named today. Elements in a group share outer-shell electrons (valency), so they behave alike.
| Region | Members |
|---|---|
| Group 1 | **Alkali metals** — Li, Na, K (very reactive, stored in kerosene) |
| Group 2 | **Alkaline earth metals** — Be, Mg, Ca |
| Groups 3–12 | **Transition metals** — Fe, Cu, Zn, Ag, Au |
| Group 17 | **Halogens** — F, Cl, Br, I (salt-formers) |
| Group 18 | **Noble (inert) gases** — He, Ne, Ar, Kr, Xe, Rn |
| Two bottom rows | **Lanthanides** and **Actinides** (includes uranium) |

### Trends — the two directions
- **Across a period (left → right):** atomic size **decreases**, metallic character **decreases**, electronegativity (pull on electrons) **increases**. Sodium is a metal; chlorine at the far right is a non-metal.
- **Down a group (top → bottom):** atomic size **increases**, metallic character **increases**, so reactivity of metals grows (K is wilder than Na).
- **Fluorine** is the **most electronegative** element; **caesium** is the most electropositive (reactive) stable metal.

### Record-holders — the static-GK list
| Record | Answer |
|---|---|
| Most abundant element in the **universe** | Hydrogen |
| Most abundant element in **Earth's crust** | Oxygen (then silicon — 'OSAIC': O, Si, Al, Fe, Ca) |
| Most abundant **metal in the crust** | Aluminium (then iron) |
| Most abundant gas in the **atmosphere** | Nitrogen (≈ 78%) |
| Most abundant element in the **human body** | Oxygen (most abundant metal in body: calcium) |
| **Lightest** element / gas | Hydrogen |
| **Lightest metal** | Lithium |
| Only **liquid metal** at room temperature | Mercury (gallium melts in the palm, ~30 °C) |
| Only **liquid non-metal** | Bromine |
| **Hardest** natural substance | Diamond (an allotrope of carbon) |
| **Softest** mineral | Talc |
| Best **conductor** among metals | Silver (graphite conducts among non-metals) |
| Most **ductile and malleable** metal | Gold |
| **Highest melting point** metal | Tungsten (used as bulb filament) |
| **Densest** natural element | Osmium |
| **First man-made** element | Technetium |
| Non-metal that conducts electricity | Graphite |

### Symbols from Latin names
Several chemical symbols come from Latin: **Na** (natrium) sodium, **K** (kalium) potassium, **Fe** (ferrum) iron, **Cu** (cuprum) copper, **Ag** (argentum) silver, **Au** (aurum) gold, **Pb** (plumbum) lead, **Sn** (stannum) tin, **Hg** (hydrargyrum) mercury, **Sb** (stibium) antimony, **W** (wolfram) tungsten. Exams love these mismatch traps — sodium is NOT 'So'.

### Quick revision
- Döbereiner triads → Newlands octaves → Mendeleev (mass, gaps) → Moseley (atomic number).
- 18 groups, 7 periods, 118 elements; group 1 alkali, 2 alkaline earth, 17 halogens, 18 noble gases.
- Across period: size ↓, metal character ↓. Down group: size ↑, metal character ↑.
- Fluorine most electronegative; caesium most electropositive stable metal.
- Records: H–universe, O–crust, Al–crust metal, N–air, Ca–body metal; Li lightest metal; Hg liquid metal; Br liquid non-metal; Au most ductile; W highest melting point."""
    S.pattern("ga-pe-p1", "Element record-holders", "very common",
        "'Most abundant element/metal in the crust/body/universe', 'lightest metal', 'only liquid metal/non-metal', 'hardest natural substance', 'first man-made element'.",
        None,
        "1. Abundance chain: H (universe) → O (crust; then Si, Al, Fe) → Al (crust metal; then Fe) → N (air 78%) → O (body; Ca is the body's top metal).\n2. Oddities: Li lightest metal, Hg liquid metal, Br liquid non-metal, graphite conducts, Au most ductile, W highest melting point, technetium first man-made.\n3. In 'odd one out' questions, check for these records first.",
        "The most abundant **metal** in the Earth's crust is —",
        "**Aluminium** (about 8%), ahead of iron. Oxygen is the most abundant element overall.")
    S.pattern("ga-pe-p2", "Symbols from Latin names", "common",
        "A wrong-symbol pair (Na–sodium, K–potassium, Fe–iron, Ag–silver, Au–gold, Pb–lead) is given and the mistake must be found.",
        None,
        "1. Memorise the Latin list: natrium–Na, kalium–K, ferrum–Fe, cuprum–Cu, argentum–Ag, aurum–Au, plumbum–Pb, stannum–Sn, hydrargyrum–Hg, stibium–Sb, wolfram–W.\n2. In 'wrong symbol' questions the answer is almost always one of these eleven.\n3. Others follow the English name (He, Ca, Zn…).",
        "Which symbol–element pair is **wrong**?\n(a) Fe–Iron (b) Au–Gold (c) Ag–Silver (d) So–Sodium",
        "**(d)** — sodium's symbol is **Na** (Latin natrium), not 'So'.")
    S.pattern("ga-pe-p3", "History of classification", "common",
        "'Law of octaves was given by…', 'Mendeleev's table was based on…', 'modern periodic law depends on…', 'eka-silicon is now called…'.",
        None,
        "1. Chain: Döbereiner triads → Newlands octaves → Mendeleev (atomic mass, gaps, predictions) → Moseley (atomic number = modern law).\n2. Mendeleev's predictions: eka-aluminium = **gallium**, eka-silicon = **germanium**.\n3. Periods run by increasing atomic number today, not mass.",
        "Mendeleev's **eka-silicon** is today's —",
        "**Germanium** (eka-aluminium became gallium).")
    S.pattern("ga-pe-p4", "Groups, periods and trends", "common",
        "'Across a period atomic size…', 'down a group metallic character…', which group an element belongs to, number of groups/periods.",
        None,
        "1. Fixed numbers: 18 groups (vertical), 7 periods (horizontal), 118 elements.\n2. Across a period: size shrinks, metallic character falls, electronegativity rises; down a group: size grows, metallic character rises.\n3. Most reactive non-metal sits at the top-right (F); most reactive metals at the bottom-left (Cs, Fr).",
        "On moving **down a group**, the metallic character of elements —",
        "**Increases** — outer electrons get farther from the nucleus and are lost more easily (K is more reactive than Na).")
    S.pattern("ga-pe-p5", "Group families (alkali, halogens, noble gases)", "common",
        "'Which group contains halogens/noble gases?', 'why are group 18 gases inert?', 'which metal is stored in kerosene?'.",
        None,
        "1. Group 1 alkali metals (Li, Na, K — soft, reactive, kerosene-stored); group 2 alkaline earth (Be, Mg, Ca).\n2. Group 17 halogens (F, Cl, Br, I — form salts, F most electronegative).\n3. Group 18 noble gases (He, Ne, Ar, Kr, Xe, Rn) have full outer shells, hence **inert**; He tops the list, Rn is radioactive.",
        "Noble gases are chemically **inert** because —",
        "Their **outermost electron shells are complete**, so they neither give, take nor share electrons easily.")

    S.q("ga-pe-p1", "easy", "The most abundant element in the **Earth's crust** is —",
        ["Oxygen", "Silicon", "Aluminium", "Iron"], "Oxygen",
        "Crust order: **O > Si > Al > Fe > Ca** (mnemonic OSAIC). Oxygen is about 46% by mass.",
        None, 15)
    S.q("ga-pe-p1", "easy", "The **lightest metal** is —",
        ["Lithium", "Sodium", "Aluminium", "Magnesium"], "Lithium",
        "**Lithium** (group 1) is the lightest of all metals — even it floats on oil. Hydrogen is lighter still, but it is not a metal.",
        None, 15)
    S.q("ga-pe-p1", "medium", "Which is the only **liquid non-metal** at room temperature?",
        ["Bromine", "Mercury", "Chlorine", "Iodine"], "Bromine",
        "**Bromine** is a fuming red-brown liquid. Mercury is the liquid *metal*; chlorine is a gas; iodine is a solid.",
        None, 15)
    S.q("ga-pe-p1", "medium", "The metal with the **highest melting point**, used as a bulb filament, is —",
        ["Tungsten", "Iron", "Platinum", "Nickel"], "Tungsten",
        "**Tungsten (W)** melts at about 3400 °C — the highest of all metals — so a white-hot filament survives. Its symbol comes from wolfram.",
        None, 15)
    S.q("ga-pe-p1", "medium", "The most abundant **metal in the human body** is —",
        ["Calcium", "Iron", "Sodium", "Zinc"], "Calcium",
        "**Calcium** (bones and teeth) tops the body's metal list; iron is the most abundant trace metal. Oxygen is the most abundant element overall.",
        None, 15)
    S.q("ga-pe-p2", "medium", "The chemical symbol of **potassium** is —",
        ["K", "P", "Po", "Pt"], "K",
        "From Latin **kalium**. P is phosphorus, Po polonium, Pt platinum.",
        None, 15)
    S.q("ga-pe-p2", "medium", "Which symbol comes from the Latin word **plumbum**?",
        ["Pb (lead)", "P (phosphorus)", "K (potassium)", "Pu (plutonium)"], "Pb (lead)",
        "**Plumbum** = lead (Pb) — the same root gives 'plumber'.",
        None, 15)
    S.q("ga-pe-p3", "easy", "The **law of octaves** was proposed by —",
        ["John Newlands", "Döbereiner", "Mendeleev", "Moseley"], "John Newlands",
        "**Newlands** arranged 56 elements by mass and found every 8th element similar — like octaves in music. Döbereiner had earlier found triads.",
        None, 15)
    S.q("ga-pe-p3", "medium", "Mendeleev's periodic table was based on —",
        ["Increasing atomic mass", "Increasing atomic number", "Number of neutrons", "Electronegativity"], "Increasing atomic mass",
        "**Mendeleev** used atomic mass and even left gaps for unknown elements. The modern table (after Moseley) uses **atomic number** instead.",
        None, 15)
    S.q("ga-pe-p3", "medium", "The **modern periodic law** states that properties of elements are a periodic function of their —",
        ["Atomic numbers", "Atomic masses", "Densities", "Valence electrons only"], "Atomic numbers",
        "**Moseley** showed atomic number (protons) — not mass — decides periodicity, fixing the anomalies of Mendeleev's table.",
        None, 15)
    S.q("ga-pe-p4", "easy", "The modern periodic table has —",
        ["18 groups and 7 periods", "7 groups and 18 periods", "8 groups and 8 periods", "18 groups and 18 periods"], "18 groups and 7 periods",
        "**18 vertical groups, 7 horizontal periods**, with 118 elements named so far.",
        None, 15)
    S.q("ga-pe-p4", "medium", "On moving **left to right across a period**, atomic size —",
        ["Decreases", "Increases", "Stays the same", "First increases, then decreases"], "Decreases",
        "Nuclear charge rises while shells stay the same, pulling electrons closer — so atoms **shrink** across a period and metallic character falls.",
        None, 15)
    S.q("ga-pe-p5", "easy", "The elements of **group 17** are called —",
        ["Halogens", "Alkali metals", "Noble gases", "Transition metals"], "Halogens",
        "**Halogens** (F, Cl, Br, I) — 'salt-formers'. Group 1 alkali metals, group 18 noble gases.",
        None, 15)
    S.q("ga-pe-p5", "medium", "Which pair of elements belongs to the **same group** of the periodic table?",
        ["Lithium and potassium", "Sodium and chlorine", "Iron and sulphur", "Helium and hydrogen"], "Lithium and potassium",
        "Li, Na and K all sit in **group 1** (alkali metals) — one outer electron each, all soft and reactive, stored under oil or kerosene.",
        None, 20)
    return S
