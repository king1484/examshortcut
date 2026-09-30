"""Physics part C: electricity and magnetism, nuclear physics and scientists."""
from fractions import Fraction as Fr
from _ph_common import pat, mis, trick

S = {}
FNOTES = {}

# numeric checks
assert 1 / (Fr(1, 2) + Fr(1, 3) + Fr(1, 6)) == 1                      # 2, 3, 6 ohm in parallel
assert 2 + 3 + 6 == 11                                                # same three in series
assert Fr(6 * 3, 6 + 3) == 2                                          # 6 and 3 in parallel
assert Fr(12, 3) == 4                                                 # three 12 ohm in parallel
assert 2 * 3 == 6                                                     # 2 kW x 3 h
assert round(100 / 220, 2) == 0.45                                    # 100 W bulb at 220 V
assert Fr(220, 44) == 5                                               # V = IR
assert 2 ** 2 * 10 * 60 == 2400                                       # H = I^2 R t
assert Fr(60 * 100, 1000) == Fr(6, 1)                                 # 60 W x 100 h ... 6 units

# =====================================================================
S["ph-electricity"] = dict(
    concept=(
        "Electric current is the flow of charge, pushed by voltage and opposed by resistance. "
        "Ohm's law, series and parallel circuits and the heating effect are the core numericals. "
        "Magnetism gives us the motor, generator and transformer. "
        "The electromagnetic spectrum is a fixed order of waves with fixed uses."
    ),
    notes=r"""### Current, voltage and resistance
**Electric current** is the flow of charge. $I = \dfrac{Q}{t}$ and its unit is the ampere (A).

A **potential difference** (voltage) pushes the charges. Its unit is the volt (V). A voltmeter measures it.

**Resistance** is the wire's opposition to the flow. Its unit is the ohm (Ω).

**Ohm's law** says $V = IR$ at constant temperature. Double the voltage and the current doubles.

Resistance is $R = \rho\dfrac{L}{A}$. More length means more resistance. A thicker wire means less. It also depends on the material (resistivity ρ) and on temperature. Metals conduct best. Rubber, plastic and mica are insulators.

### Series and parallel circuits
| | Series | Parallel |
|---|---|---|
| Layout | One loop | Branches across two points |
| Common to all | Current | Voltage |
| Total resistance | $R = R_1 + R_2 + \cdots$ | $\dfrac{1}{R} = \dfrac{1}{R_1} + \dfrac{1}{R_2} + \cdots$ |
| If one bulb fuses | All go dark | Others keep working |

In parallel, the total resistance is less than the smallest branch. Homes are wired in parallel. Each appliance gets the full 220 V and works independently.

> **Example:** 2 Ω, 3 Ω and 6 Ω in parallel: $\dfrac{1}{R} = \dfrac{1}{2} + \dfrac{1}{3} + \dfrac{1}{6} = 1$. So $R = 1$ Ω.

### Power, energy and heating
Power is $P = VI = I^2R = \dfrac{V^2}{R}$. Its unit is the watt. A 100 W bulb at 220 V draws about 0.45 A.

Electricity is sold in kilowatt-hours. 1 unit = 1 kWh = 3.6 × 10⁶ J. Units = watts × hours ÷ 1000.

**Joule's law** says $H = I^2Rt$. Heat grows with current squared, resistance and time. Irons, geysers and heaters work this way.

- The bulb **filament** is tungsten. It has a very high melting point.
- Heating coils are **nichrome**. It has high resistivity.
- A **fuse** wire is a tin–lead alloy with a low melting point. It melts on excess current. It sits in series with the live wire.

### Household supply
Indian domestic supply is AC at about 220 V (220–230 V) and 50 Hz.

| Wire | Colour |
|---|---|
| Live | Red or brown |
| Neutral | Black or blue |
| Earth | Green |

The earth wire gives a safe path to the ground for metal bodies.

### Magnetism and its devices
A magnet has north and south poles. Like poles repel and unlike poles attract.

- **Oersted (1820):** a current in a wire deflects a compass. Electricity creates magnetism.
- **Electromagnet:** a coil with a soft-iron core. It is temporary. Cranes and bells use it. Steel makes permanent magnets.
- **Faraday (1831):** a changing magnetic field induces a current. This is electromagnetic induction. It runs the generator or dynamo.
- **Electric motor:** current plus a magnetic field gives rotation.
- **Transformer:** changes AC voltage by mutual induction. It works only on AC. Step-up transformers raise voltage for long-distance lines. The current falls, so the I²R loss falls. Step-down transformers lower it near homes.

> **Rule:** Fleming's left-hand rule is for the motor. The right-hand rule is for the generator. Remember "L for Motor, R for Generator".

A galvanometer becomes an **ammeter** with a low-resistance shunt in parallel. An ammeter is connected in series. A **voltmeter** has a high resistance in series inside it. It is connected in parallel.

### AC, DC and semiconductors
**AC** reverses direction again and again (mains supply). **DC** flows one way (cells, batteries).

- A **rectifier (diode)** turns AC into DC. An **inverter** turns DC into AC.
- The **transistor** (1947, Bell Labs) amplifies and switches signals.
- **Semiconductors** are silicon and germanium. They conduct between metals and insulators.
- A **pentavalent** impurity (phosphorus, arsenic) adds free electrons. That gives **n-type**.
- A **trivalent** impurity (boron, gallium) leaves holes. That gives **p-type**.

### The electromagnetic spectrum
EM waves need no medium. They travel at $c = 3 \times 10^8$ m/s in vacuum. In order of increasing wavelength:

**Gamma rays, X-rays, Ultraviolet, Visible, Infrared, Microwaves, Radio waves.**

| Wave | Use |
|---|---|
| Gamma | Cancer treatment, sterilising tools |
| X-rays | Bone imaging, airport scanners |
| Ultraviolet | Sterilisation, vitamin D in skin |
| Visible | Seeing, lasers |
| Infrared | TV remotes, night vision, heaters |
| Microwaves | Microwave ovens, radar, satellite links |
| Radio | Broadcasting, mobile phones |
""",
    tricks=[
        trick("Fleming's hands",
              "**L** comes before **M**, so Left goes with Motor. **G** is for generator, so Right goes with Generator.",
              "Which Fleming rule gives the direction of the force in an electric motor?",
              ["The motor uses a force on a current-carrying wire.", "Left for Motor."],
              "Fleming's left-hand rule"),
        trick("Spectrum order",
              "**G**ood **X**-rays **U**se **V**isible **I**nfra-**M**icro **R**adios. The wavelength rises along the list. Frequency and energy fall.",
              "Which has the longest wavelength: X-rays, UV, microwaves or gamma rays?",
              ["Order by rising wavelength: gamma, X-ray, UV, microwave.", "The last one is the longest."],
              "Microwaves"),
    ],
    mistakes=[
        mis("Thinking a fuse wire should have a high melting point.", "It must melt easily, so use a low-melting alloy."),
        mis("Saying a transformer works on DC.", "It needs changing current, so it works only on AC."),
        mis("Connecting an ammeter in parallel.", "An ammeter goes in series. A voltmeter goes in parallel."),
        mis("Adding reciprocals but forgetting to invert the answer in parallel.", "Take 1/R first, then flip it to get R."),
        mis("Using the right-hand rule for the motor.", "Motor uses the left hand. Generator uses the right hand."),
    ],
    revision=[
        "I = Q/t and V = IR. R = ρL/A: longer means more, thicker means less.",
        "Series: same current, resistances add. Parallel: same voltage, total R is smaller. Homes are parallel.",
        "P = VI. 1 unit = 1 kWh. H = I²Rt. Filament is tungsten, coil is nichrome, fuse is low-melting in the live wire.",
        "Oersted: current gives magnetism. Faraday, 1831: induction gives the generator. Left hand for motor, right for generator.",
        "A transformer works on AC only. Step-up is used for transmission. A rectifier turns AC to DC. The transistor is from 1947.",
        "EM waves by rising wavelength: gamma, X, UV, visible, IR, microwave, radio.",
    ],
    patterns=[
        pat("ga-el-p1", "Ohm's law and series or parallel circuits", "very common",
            "The question gives two or three resistors and asks total resistance, gives voltage and resistance and asks current, or asks what stays the same in series or parallel.",
            ["In series, add the resistances. The current is common.",
             "In parallel, add the reciprocals, then invert. For two resistors use R₁R₂/(R₁+R₂).",
             "Three equal resistors R in parallel give R/3.",
             "For current, use I = V/R."],
            "One path shares current (series). Branches share voltage (parallel).",
            "Resistors of 2 Ω, 3 Ω and 6 Ω are joined in parallel. Find the total resistance.",
            [r"$\dfrac{1}{R} = \dfrac{1}{2} + \dfrac{1}{3} + \dfrac{1}{6}$.", r"$= \dfrac{3+2+1}{6} = 1$.", "So R = 1 Ω, less than the smallest resistor."],
            "1 Ω",
            formula=r"V=IR,\quad R_s=R_1+R_2,\quad \frac{1}{R_p}=\frac{1}{R_1}+\frac{1}{R_2}"),
        pat("ga-el-p2", "Power, kWh and the heating effect", "very common",
            "The question gives appliance watts and hours, H = I²Rt, 'the filament is made of ...', 'why is the fuse wire low-melting', or transmission steps.",
            ["For energy, use kW × hours = units. Multiply by the tariff for rupees.",
             "For heat, use H = I²Rt with t in seconds.",
             "Filament is tungsten. Coil is nichrome. Fuse is a low-melting alloy in series with the live wire.",
             "Long lines run at high voltage so the current and I²R loss stay small."],
            "Watts times hours gives energy. Current squared gives heat.",
            "A 2 kW heater runs for 3 hours. How many units does it use?",
            ["Units = kW × hours.", "2 × 3 = 6."],
            "6 kWh, that is 6 units",
            formula=r"P=VI=I^2R=\frac{V^2}{R},\quad H=I^2Rt,\quad 1\ \text{unit}=1\ \text{kWh}"),
        pat("ga-el-p3", "Electricity and magnetism devices", "very common",
            "The question says 'The electric motor works on ...', 'a generator is based on ...', 'a transformer works on ...', asks which Fleming rule applies, or who found electromagnetic induction.",
            ["Oersted: a current makes a magnetic field.",
             "Motor: a magnetic force on a current-carrying wire. Use the left-hand rule.",
             "Generator: electromagnetic induction (Faraday). Use the right-hand rule.",
             "Transformer: mutual induction. AC only. Step-up raises V and lowers I."],
            "Each device turns one effect of electricity or magnetism into work.",
            "The working of an electric motor is based on:",
            ["A wire carries current inside a magnetic field.", "The field pushes the wire.", "The left-hand rule gives the direction."],
            "The magnetic force on a current-carrying conductor"),
        pat("ga-el-p4", "Household wiring and safety", "common",
            "The question says 'Appliances in a house are connected in ...', asks the colour of the earth wire, the job of the fuse, or mains voltage and frequency in India.",
            ["Homes use parallel wiring. Each appliance gets full voltage and has its own switch.",
             "Live is red or brown. Neutral is black. Earth is green.",
             "The fuse is low-melting and sits in series with the live wire. It melts first on overload.",
             "India uses AC at about 220 V and 50 Hz."],
            "The wiring plan protects both the appliance and the person.",
            "Which colour of insulation is used for the earth wire in India?",
            ["Live is red or brown.", "Neutral is black.", "Earth is the remaining one."],
            "Green"),
        pat("ga-el-p5", "EM spectrum order and uses", "very common",
            "The question says 'Arrange gamma to radio by wavelength', 'TV remote uses ...', 'which wave is used in radar / microwave oven' or 'UV makes which vitamin'.",
            ["Learn rising wavelength: gamma, X, UV, visible, IR, microwave, radio. Frequency runs the other way.",
             "Match uses: gamma for cancer therapy, X-ray for bones, UV for sterilising and vitamin D, IR for remotes, microwave for ovens and radar, radio for broadcast.",
             "All EM waves travel at 3 × 10⁸ m/s in vacuum and need no medium."],
            "The order and the uses are fixed facts.",
            "Which electromagnetic wave is used in TV remotes?",
            ["Remotes send invisible beams.", "They lie just beyond the red end of visible light."],
            "Infrared"),
        pat("ga-el-p6", "Semiconductors, rectifiers and electronics", "occasional",
            "The question says 'n-type is doped with ...', 'which device converts AC to DC', or asks about transistors and semiconductor materials.",
            ["Semiconductors are silicon and germanium.",
             "Pentavalent doping (P, As) gives n-type, with extra electrons. Trivalent doping (B, Ga) gives p-type, with holes.",
             "A diode is a rectifier (AC to DC). An inverter changes DC to AC. The transistor (1947) amplifies and switches."],
            "The number of outer electrons in the impurity decides n-type or p-type.",
            "A pure silicon crystal doped with a pentavalent impurity such as phosphorus becomes:",
            ["Phosphorus has one extra outer electron.", "It gives a free electron to the crystal.", "Free electrons are negative carriers."],
            "n-type"),
    ],
)
FNOTES["ph-electricity"] = {"Ohm's law": "V is voltage, I is current, R is resistance",
                            "Series resistance": "the same current flows through each",
                            "Electric power": "P is power in watt",
                            "Joule heating": "t is time in seconds"}

# =====================================================================
S["ph-modern-scientists"] = dict(
    concept=(
        "The atom has a nucleus of protons and neutrons with electrons around it. "
        "Radioactivity, fission and fusion come from the nucleus. "
        "Exams ask who found what, which invention belongs to whom, and India's nuclear and space firsts."
    ),
    notes=r"""### Inside the atom
An atom has a tiny, dense **nucleus** of protons and neutrons. Electrons move around it.

- **Electron:** negative charge. Found by J.J. Thomson (1897) in cathode-ray experiments.
- **Proton:** positive charge. Seen in canal rays by E. Goldstein.
- **Neutron:** no charge. Discovered by James Chadwick (1932).
- **Nucleus:** shown by Rutherford's gold-foil experiment (1911). Most alpha particles went straight through and a few bounced back. So nearly all the mass and positive charge sit in a tiny centre.
- **Bohr (1913):** added fixed orbits for electrons.

### Radioactivity
**Henri Becquerel (1896)** found that uranium salts give out invisible, penetrating rays. This is radioactivity. It belongs to heavy, unstable nuclei.

**Marie and Pierre Curie** discovered polonium and radium. Marie Curie won Nobel Prizes in Physics (1903) and Chemistry (1911).

| Ray | What it is | Penetration |
|---|---|---|
| Alpha | Helium nucleus | Least. Paper stops it. |
| Beta | Fast electron | Medium. Aluminium stops it. |
| Gamma | Electromagnetic wave | Most. Thick lead needed. |

A **Geiger–Müller counter** detects radiation. **Willard Libby's carbon-14 dating** finds the age of old organic remains.

### Fission, fusion and reactors
- **Fission:** a heavy nucleus such as U-235 splits when a neutron hits it. It releases energy and more neutrons. That is a chain reaction. Uncontrolled, it is the atom bomb (Hiroshima, 1945). Controlled, it makes electricity.
- **Fusion:** light nuclei (hydrogen isotopes) join into a heavier one. It powers the Sun and stars, and the hydrogen bomb.
- Both follow Einstein's $E = mc^2$. A little lost mass becomes a lot of energy.

> **Rule:** Fission means split. Fusion means join. Reactors use fission, not fusion.

In a reactor, the **moderator** (heavy water, graphite) slows neutrons. **Control rods** (cadmium, boron) absorb neutrons. A coolant carries the heat away.

### India's atomic and space firsts
**Homi J. Bhabha** is the father of India's nuclear programme. He set up the Tata Institute of Fundamental Research (1945) and BARC at Trombay.

| Item | Fact |
|---|---|
| Apsara (1956) | First research reactor in Asia |
| Tarapur (1969) | First nuclear power station, Maharashtra |
| Pokhran-I (1974) | First nuclear test, "Smiling Buddha" |
| Pokhran-II | May 1998 |
| ISRO | Formed in 1969 |
| Aryabhata (1975) | First Indian satellite |
| Chandrayaan-1 (2008) | Found water molecules on the Moon |
| Mangalyaan (2013) | Reached Mars orbit at the first attempt |
| Chandrayaan-3 (23 Aug 2023) | First soft landing near the Moon's south pole |
| Aditya-L1 (2023) | India's first solar mission |

**Vikram Sarabhai** is the father of India's space programme. 23 August is now National Space Day. **Rakesh Sharma (1984)** was the first Indian in space. **Shubhanshu Shukla (2025, Axiom-4)** was the first Indian to visit the International Space Station.

### Inventions and who made them
| Invention or discovery | Person |
|---|---|
| Laws of motion, gravitation | Isaac Newton |
| Astronomical telescope | Galileo Galilei |
| Barometer | Evangelista Torricelli |
| Improved steam engine | James Watt |
| Electromagnetic induction, dynamo | Michael Faraday |
| Telephone | Alexander Graham Bell |
| Electric bulb, phonograph | Thomas Edison |
| Radio (wireless) | Guglielmo Marconi |
| Television | John Logie Baird |
| Telegraph | Samuel Morse |
| Aeroplane (1903) | Wright brothers |
| X-rays | Wilhelm Röntgen (first Physics Nobel, 1901) |
| Laser (1960) | Theodore Maiman |
| Dynamite | Alfred Nobel |
| Crescograph | J.C. Bose |
| Raman effect | C.V. Raman (Nobel 1930) |
| Chandrasekhar limit | S. Chandrasekhar (Nobel 1983) |
| Bose–Einstein statistics | Satyendra Nath Bose |

Einstein gave the theory of relativity. His Nobel Prize (1921) was for the photoelectric effect.

A **laser** gives an intense beam of one wavelength, in step (coherent). It is used in surgery, barcode scanners, CD/DVD players and optical-fibre communication. At CERN's Large Hadron Collider (2012), scientists found the **Higgs boson**, the "God particle". It explains why other particles have mass.
""",
    tricks=[
        trick("Fission or fusion",
              "**Fission** means split: heavy nucleus to lighter ones (reactors, atom bomb). **Fusion** means join: light nuclei to a heavier one (Sun, hydrogen bomb).",
              "The energy of the Sun comes from:",
              ["The Sun is made mostly of hydrogen.", "Hydrogen nuclei join into helium.", "Joining is fusion."],
              "Nuclear fusion"),
        trick("Particle discoverers",
              "Electron: **T**homson (1897). Nucleus: **R**utherford. Neutron: **Chad**wick (1932). Proton rays: Goldstein."),
    ],
    mistakes=[
        mis("Saying Einstein won the Nobel Prize for relativity.", "It was for the photoelectric effect (1921)."),
        mis("Saying the moderator absorbs neutrons.", "The moderator slows them. Control rods (cadmium, boron) absorb them."),
        mis("Crediting Edison with the telephone.", "The telephone was Alexander Graham Bell's. Edison made the bulb and phonograph."),
        mis("Saying a reactor uses fusion.", "Reactors use fission. Fusion powers the Sun and the hydrogen bomb."),
        mis("Taking gamma rays as particles.", "Gamma rays are electromagnetic waves, the most penetrating of the three."),
    ],
    revision=[
        "Electron: Thomson. Proton: Goldstein (canal rays). Neutron: Chadwick. Nucleus: Rutherford. Orbits: Bohr.",
        "Radioactivity: Becquerel. Radium and polonium: the Curies. C-14 dating: Libby. Counter: Geiger.",
        "Alpha is a helium nucleus. Beta is an electron. Gamma is an EM wave and the most penetrating.",
        "Fission is heavy splitting (reactor, atom bomb). Fusion is light joining (Sun, H-bomb). E = mc².",
        "Bhabha is atomic, Sarabhai is space. Apsara 1956, Tarapur 1969, Pokhran 1974 and 1998.",
        "Aryabhata 1975. Chandrayaan-3 landed on 23 Aug 2023. Mangalyaan reached Mars orbit at the first attempt.",
    ],
    patterns=[
        pat("ga-ms-p1", "Particle or ray and its discoverer", "very common",
            "The question says 'Who discovered the neutron / electron / proton / X-rays / radioactivity / nucleus?' or gives a match-the-column.",
            ["Particles: electron by J.J. Thomson, proton by Goldstein, neutron by Chadwick, nucleus by Rutherford.",
             "Rays: X-rays by Röntgen, radioactivity by Becquerel, radium by the Curies.",
             "Models: gold-foil experiment by Rutherford, orbits by Bohr."],
            "Each name is fixed by history, so only recall and elimination work.",
            "The canal rays that led to the discovery of the proton were observed by:",
            ["Thomson found the electron in cathode rays.", "Chadwick found the neutron in 1932.", "Canal rays belong to Goldstein."],
            "E. Goldstein"),
        pat("ga-ms-p2", "Device and its inventor", "very common",
            "The question says 'Who invented the telephone / television / radio / electric bulb / dynamo / steam engine / aeroplane?'",
            ["Bell made the telephone. Baird made television. Marconi made radio. Edison made the bulb and phonograph. Morse made the telegraph.",
             "Faraday found induction and the dynamo. Watt improved the steam engine. The Wright brothers built the aeroplane (1903). Galileo used the astronomical telescope. Torricelli made the barometer.",
             "Drop near-names. J.C. Bose did pioneering microwave work, but the exam answer for radio is Marconi."],
            "Inventions are fixed facts, so match each device to one name.",
            "The television was invented by:",
            ["Telephone is Bell.", "Radio is Marconi.", "Television is Baird."],
            "John Logie Baird"),
        pat("ga-ms-p3", "Radioactivity and alpha, beta, gamma", "common",
            "The question asks 'Which radiation is most penetrating?', 'an alpha particle is ...', who found radioactivity, or which instrument detects radiation.",
            ["Radioactivity: Becquerel (1896). Radium and polonium: the Curies.",
             "Alpha is a helium nucleus of 2 protons and 2 neutrons. Paper stops it. Beta is a fast electron. Gamma is an EM wave and the most penetrating.",
             "The Geiger–Müller counter detects radiation. Libby's C-14 dating ages old remains."],
            "The three rays differ in what they are and how far they go.",
            "An alpha particle is identical to:",
            ["An alpha particle has 2 protons and 2 neutrons.", "That is the makeup of helium-4.", "It has no electrons."],
            "A helium nucleus"),
        pat("ga-ms-p4", "Fission or fusion; reactor parts", "very common",
            "The question says 'The Sun's energy comes from ...', 'an atom bomb works on ...', 'control rods are made of ...', or compares the two bombs.",
            ["If a heavy nucleus splits, it is fission (reactors, atom bomb).",
             "If light nuclei join, it is fusion (Sun and stars, hydrogen bomb).",
             "Moderator slows neutrons (heavy water, graphite). Control rods absorb them (cadmium, boron). A coolant removes heat."],
            "Both follow E = mc². The size of the nuclei tells you which process it is.",
            "The energy of the Sun and stars is due to:",
            ["Stars are mostly hydrogen.", "Hydrogen nuclei join into helium.", "This releases energy through E = mc²."],
            "Nuclear fusion"),
        pat("ga-ms-p5", "India's atomic and space milestones", "common",
            "The question asks for the first reactor, power station, satellite, Mars or Moon mission, the fathers of the two programmes, Pokhran tests or National Space Day.",
            ["Atomic: Bhabha is the father. Apsara 1956 was the first research reactor. Tarapur 1969 was the first power station. Pokhran tests were 1974 and 1998.",
             "Space: Sarabhai is the father. ISRO 1969. Aryabhata 1975. Chandrayaan-1 2008. Mangalyaan 2013. Chandrayaan-3 landed on 23 Aug 2023. Aditya-L1 is the solar mission.",
             "Rakesh Sharma was the first Indian in space (1984). Shubhanshu Shukla was the first Indian on the ISS (2025)."],
            "Each milestone is a fixed name, place or date.",
            "India's first nuclear power station was set up at:",
            ["Apsara was a research reactor, at Trombay (1956).", "A power station came later, in 1969."],
            "Tarapur, Maharashtra (1969)"),
        pat("ga-ms-p6", "Modern physics miscellany", "common",
            "One-line fact questions on E = mc², the 'God particle', laser properties, carbon dating or first Nobel Prizes.",
            ["E = mc² is Einstein's. Mass can turn into energy. It is the base of fission and fusion.",
             "The Higgs boson (the 'God particle') was found at CERN's LHC in 2012.",
             "Laser light has one wavelength, is coherent and is highly directional.",
             "Carbon-14 dating is Libby's method for fossils and old organic objects."],
            "Each fact is a short, fixed statement.",
            "The 'God particle' whose existence was confirmed at CERN in 2012 is the:",
            ["It explains why particles have mass.", "It was predicted by Peter Higgs."],
            "Higgs boson"),
    ],
)
FNOTES["ph-modern-scientists"] = {"Mass–energy equivalence": "E is energy, m is mass, c is the speed of light"}
