"""physics deep content — part 3: ph-electricity (electricity, magnetism, EM spectrum)."""
import math
import os
import sys

sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
from _lib import Sub


def g(x):
    x = round(x, 6)
    return str(int(x)) if x == int(x) else str(x)


def build_elec():
    S = Sub("ph-electricity")
    S.notes = """### Current, voltage, resistance
**Electric current** is the flow of charge: I = Q/t, unit **ampere (A)**. Charges move because a **potential difference (voltage)** pushes them — unit **volt (V)**, measured by a voltmeter. The wire fights the flow with **resistance** — unit **ohm (Ω)**, measured by connecting the meter readings: R = V/I.
**Ohm's law**: at constant temperature, $V = I R$. Double the voltage and the current doubles.
What changes resistance? R = ρL/A — **more length, more resistance; thicker wire, less resistance**; it depends on the material (its resistivity ρ) and on temperature. Metals conduct best; rubber, plastic and mica are insulators.

### Series and parallel circuits
- **Series**: components in one loop; the **same current** flows through all; resistances **add** (R = R₁ + R₂ + …); one bulb fuses and the whole string goes dark.
- **Parallel**: branches across the same two points; the **same voltage** across each; 1/R = 1/R₁ + 1/R₂ + …, so total resistance is **less than the smallest** branch; each appliance works independently.
Household appliances are connected in **parallel** so that each gets the full 220 V and switching off the TV does not kill the fan.

### Power, energy and the heating effect
- Power P = VI = I²R = V²/R, unit **watt**. A 100 W bulb at 220 V draws about 0.45 A.
- Energy sold in **kilowatt-hours**: 1 unit = 1 kWh = 3.6 × 10⁶ J. Units = watts × hours ÷ 1000.
- **Joule's law of heating**: H = I²Rt — heat grows with current², resistance and time; this warms the iron, geyser and heater.
- Materials: the bulb filament is **tungsten** (extremely high melting point); heating coils are **nichrome** (high resistivity); a **fuse** wire (tin–lead alloy) has a **low melting point**, melts on excess current and breaks the circuit — it sits **in series with the live wire**.
- Indian domestic supply: **AC, about 220 V at 50 Hz**. Wiring colours: **live — red/brown, neutral — black, earth — green** (a safety path to the ground for metal bodies).

### Magnetism and electromagnetic devices
Every magnet has a north and a south pole; **like poles repel, unlike attract**. **Oersted (1820)** showed that a current-carrying wire deflects a compass — **electricity creates magnetism**. A coil with a **soft-iron core** is an **electromagnet** (temporary magnet; cranes, electric bells); steel makes **permanent** magnets.
- **Electromagnetic induction (Faraday, 1831)**: a changing magnetic field induces a current — the working of the **generator/dynamo** (motion → electricity).
- **Electric motor**: electricity + magnetic field → rotation. Remember the hands: **Fleming's LEFT hand → motor, RIGHT hand → generator** ('left = motor, both start with letters after F').
- **Transformer**: changes AC voltage by mutual induction — **works only on AC**. Step-up transformers raise voltage for long-distance transmission (current falls, so I²R line loss falls); step-down transformers bring it back near homes.
- Meters: a galvanometer becomes an **ammeter** with a **low-resistance shunt in parallel** (ammeter sits in series, so it must be nearly resistance-free); a **voltmeter** has **high resistance in series** inside and is connected in **parallel** with the component.

### AC, DC and semiconductors
Current that reverses direction periodically is **AC** (mains supply); steady one-way current is **DC** (cells, batteries). A **rectifier** (diode) converts AC → DC; an **inverter** converts DC → AC. The **transistor** (1947, Bell Labs) amplifies and switches signals — the heart of electronics.
**Semiconductors** (silicon, germanium) conduct halfway between metals and insulators. Doping with a **pentavalent** impurity (phosphorus, arsenic) adds free electrons → **n-type**; a **trivalent** one (boron, gallium) leaves holes → **p-type**. Joined p–n layers make diodes, chips and solar cells.

### The electromagnetic spectrum
EM waves need no medium and travel at c = 3 × 10⁸ m/s. By **increasing wavelength** (decreasing frequency):
**Gamma rays → X-rays → Ultraviolet → Visible → Infrared → Microwaves → Radio waves.**
| Wave | Typical use |
|---|---|
| Gamma | Cancer treatment, sterilising medical tools |
| X-rays | Bone imaging, airport security |
| UV | Sterilisation; makes vitamin D in skin |
| Visible | Seeing; lasers |
| Infrared | **TV remotes**, night vision, heaters |
| Microwave | **Microwave ovens, radar**, satellite links |
| Radio | Broadcasting, mobile phones |

### Quick revision
- I = Q/t (A); V = IR (Ohm); R = ρL/A — longer more, thicker less.
- Series: same current, R adds. Parallel: same voltage, R shrinks; homes are parallel.
- P = VI; 1 unit = 1 kWh; H = I²Rt; filament tungsten, coil nichrome, fuse low-melting in the live wire.
- Oersted: current → magnetism; Faraday 1831: induction → generator. Left hand motor, right hand generator.
- Transformer: AC only; step-up for transmission. Rectifier AC→DC; transistor 1947.
- EM waves by rising wavelength: Gamma, X, UV, Visible, IR, Microwave, Radio."""
    S.pattern("ga-el-p1", "Ohm's law and series/parallel circuits", "very common",
        "Find total resistance of two or three resistors, or the current for a given voltage and resistance; 'what stays the same in series/parallel'.",
        r"V=IR,\quad R_s=R_1+R_2,\quad \frac{1}{R_p}=\frac{1}{R_1}+\frac{1}{R_2}",
        "1. Series: just add the resistances; the current is common.\n2. Parallel: add the reciprocals, then invert; for two resistors use R1R2/(R1+R2). Three equal resistors R in parallel give R/3.\n3. Ohm's law: I = V/R.\nWhy: one path shares current (series), branches share voltage (parallel).",
        "Resistors of **2 Ω, 3 Ω and 6 Ω** are joined in parallel. Find the total resistance.",
        "1/R = 1/2 + 1/3 + 1/6 = 1 → R = **1 Ω**, less than the smallest resistor.")
    S.pattern("ga-el-p2", "Power, kWh and the heating effect", "very common",
        "Appliance watts into units/₹, H = I²Rt, 'filament is made of…', 'why is the fuse wire low-melting', transformer/transmission steps.",
        r"P=VI=I^2R=\frac{V^2}{R},\quad H=I^2Rt,\quad 1\ \text{unit}=1\ \text{kWh}",
        "1. Energy: kW × hours = units; multiply by the tariff for rupees.\n2. Heat: H = I²Rt with t in seconds.\n3. Materials: filament–tungsten (very high melting point), coil–nichrome (high resistivity), fuse–low-melting alloy in series with the live wire.\n4. Long transmission lines run at high voltage so the current (and I²R loss) stays small.",
        "A **2 kW** heater runs for **3 hours**. How many units does it use?",
        "2 kW × 3 h = **6 kWh = 6 units**.")
    S.pattern("ga-el-p3", "Electricity ↔ magnetism devices", "very common",
        "'The electric motor works on…', 'a generator is based on…', 'a transformer works on…', which Fleming rule applies, who discovered electromagnetic induction.",
        None,
        "1. Oersted: current produces a magnetic field (compass deflects).\n2. Motor: magnetic force on a current-carrying conductor → rotation — Fleming's **left**-hand rule.\n3. Generator: electromagnetic induction (Faraday) — Fleming's **right**-hand rule.\n4. Transformer: mutual induction, AC only; step-up raises V, lowers I.\nMnemonic: 'Left for Motor, Right for Generator'.",
        "The working of an **electric motor** is based on —",
        "The magnetic **force on a current-carrying conductor** placed in a magnetic field — Fleming's left-hand rule gives the direction.")
    S.pattern("ga-el-p4", "Household wiring and safety", "common",
        "'Appliances in a house are connected in…', colour of the earth wire, the job of the fuse, mains voltage and frequency in India.",
        None,
        "1. Homes: **parallel** — full voltage to each appliance, independent switches.\n2. Wires: live red/brown, neutral black, **earth green** — a safety path for leaking current.\n3. Fuse: low-melting wire **in series with the live wire**; melts first on overload.\n4. India: AC, about 220 V, 50 Hz.",
        "Which colour of insulation is used for the **earth wire** in India?",
        "**Green.** Live is red/brown, neutral is black, earth is green.")
    S.pattern("ga-el-p5", "EM spectrum order and uses", "very common",
        "'Arrange gamma…radio by wavelength/frequency', 'TV remote uses…', 'which wave is used in radar/microwave oven', 'UV produces which vitamin'.",
        None,
        "1. Memorise rising wavelength: Gamma → X → UV → Visible → IR → Microwave → Radio (frequency rises the other way).\n2. Uses: gamma–cancer therapy, X–bones/scanner, UV–sterilising + vitamin D, IR–remotes/night vision, microwave–oven/radar, radio–broadcast.\n3. All EM waves travel at 3 × 10⁸ m/s in vacuum and need no medium.",
        "Which electromagnetic wave is used in **TV remotes**?",
        "**Infrared** radiation — beyond the red end of the visible spectrum.")
    S.pattern("ga-el-p6", "Semiconductors, rectifiers and electronics", "occasional",
        "'n-type is doped with…', 'which device converts AC to DC', facts about transistors and semiconductor materials.",
        None,
        "1. Semiconductors: silicon, germanium.\n2. Pentavalent doping (P, As) → **n-type** (extra electrons); trivalent (B, Ga) → **p-type** (holes).\n3. Diode = rectifier, AC → DC; inverter = DC → AC; transistor (1947) amplifies and switches.",
        "A pure silicon crystal doped with a **pentavalent** impurity such as phosphorus becomes —",
        "**n-type** — each phosphorus atom donates one free electron (negative charge carriers).")

    I = 220 / 44
    assert I == 5
    S.q("ga-el-p1", "easy", "Two resistors of **4 Ω and 6 Ω** are connected in series. Their total resistance is —",
        ["10 Ω", "2.4 Ω", "24 Ω", "1 Ω"], g(4 + 6) + " Ω",
        "In series, resistances simply add: 4 + 6 = **10 Ω** (2.4 Ω is what a parallel combination would give).",
        None, 20)
    rp = 1 / (1 / 2 + 1 / 3 + 1 / 6)
    assert math.isclose(rp, 1.0)
    S.q("ga-el-p1", "medium", "Resistors of **2 Ω, 3 Ω and 6 Ω** are in parallel. The equivalent resistance is —",
        [g(rp) + " Ω", "11 Ω", "2 Ω", "0.5 Ω"], g(rp) + " Ω",
        "1/R = 1/2 + 1/3 + 1/6 = 1, so R = **1 Ω**. In parallel the total is always less than the smallest resistor.",
        None, 25)
    S.q("ga-el-p1", "easy", "By **Ohm's law**, the current through a **44 Ω** resistor connected to **220 V** is —",
        [g(I) + " A", "0.2 A", "44 A", "9680 A"], g(I) + " A",
        "I = V/R = 220/44 = **5 A**. Multiplying instead of dividing gives 9680 — the classic trap.",
        None, 20)
    S.q("ga-el-p1", "medium", "In a **series** circuit, which quantity remains the **same** through every component?",
        ["Current", "Voltage", "Resistance", "Power"], "Current",
        "A series circuit offers one path, so the **same current** passes through each component; the supply voltage, however, divides among them.",
        None, 15)
    units2 = 2000 * 3 / 1000
    assert units2 == 6
    S.q("ga-el-p2", "easy", "A **2000 W** heater runs for 3 hours. The electrical energy consumed is —",
        [g(units2) + " kWh", g(2000 * 3) + " kWh", "1.5 kWh", "0.6 kWh"], g(units2) + " kWh",
        "Energy = 2 kW × 3 h = **6 kWh = 6 units**. 1 unit of electricity is 1 kilowatt-hour.",
        None, 20)
    H = 4 * 25 * 60
    assert H == 6000
    S.q("ga-el-p2", "hard", "A current of **2 A** flows through a **25 Ω** resistor for **1 minute**. The heat produced is —",
        [g(H) + " J", g(H / 60) + " J", g(H * 2) + " J", "50 J"], g(H) + " J",
        "H = I²Rt = 2² × 25 × 60 = 4 × 25 × 60 = **6000 J**. Forgetting to convert 1 minute into 60 s gives 100 J.",
        None, 35)
    S.q("ga-el-p2", "easy", "The filament of an electric bulb is made of **tungsten** because tungsten has —",
        ["A very high melting point", "A very low melting point", "Zero resistance", "A very low density"], "A very high melting point",
        "The filament glows white-hot; **tungsten's very high melting point** (about 3400 °C) lets it glow without melting. Nichrome (high resistivity) is used for heating coils.",
        None, 15)
    S.q("ga-el-p2", "medium", "A **fuse wire** is so designed that it —",
        ["Melts quickly when the current exceeds the safe limit", "Never melts", "Has a very high melting point", "Increases the current in the circuit"], "Melts quickly when the current exceeds the safe limit",
        "A fuse is a **low-melting-point** alloy wire (tin–lead) placed **in series with the live wire**; excess current heats and melts it, breaking the circuit.",
        None, 20)
    S.q("ga-el-p3", "medium", "The direction of force on a current-carrying conductor in a magnetic field is given by —",
        ["Fleming's left-hand rule", "Fleming's right-hand rule", "Ohm's law", "Right-hand thumb rule"], "Fleming's left-hand rule",
        "**Fleming's left-hand rule** gives the force (motor effect); the right-hand rule gives the induced current in a generator. 'Left for Motor, Right for Generator.'",
        None, 20)
    S.q("ga-el-p3", "easy", "An **electric generator** converts —",
        ["Mechanical energy into electrical energy", "Electrical energy into mechanical energy", "Chemical energy into electrical energy", "Heat energy into light energy"], "Mechanical energy into electrical energy",
        "A generator (dynamo) uses **electromagnetic induction** (Faraday, 1831): turning a coil in a magnetic field induces a current. A motor does the reverse.",
        None, 15)
    S.q("ga-el-p3", "medium", "A **transformer** works —",
        ["Only on AC", "Only on DC", "On both AC and DC equally", "On neither"], "Only on AC",
        "A transformer works by **mutual induction**, which needs a *changing* magnetic field — so it works only on alternating current. A steady DC gives no induced voltage.",
        None, 20)
    S.q("ga-el-p3", "medium", "The core of an **electromagnet** is made of **soft iron** because soft iron —",
        ["Magnetises quickly and loses its magnetism just as quickly", "Retains magnetism permanently", "Is a poor conductor", "Is very light"], "Magnetises quickly and loses its magnetism just as quickly",
        "Soft iron is a **temporary magnet** material: it becomes a strong magnet while current flows and demagnetises when it stops — ideal for cranes and electric bells. Steel holds magnetism and makes permanent magnets.",
        None, 20)
    S.q("ga-el-p4", "easy", "Household electrical appliances are connected in **parallel** because —",
        ["Each appliance gets the full supply voltage and works independently", "It saves wire", "The total resistance increases", "The current through each appliance is the same"], "Each appliance gets the full supply voltage and works independently",
        "In **parallel** every branch receives the full 220 V and can be switched off alone; in series all appliances would share the voltage and one fault would stop everything.",
        None, 20)
    S.q("ga-el-p4", "easy", "The colour of insulation on the **earth wire** of Indian domestic wiring is —",
        ["Green", "Red", "Black", "Blue"], "Green",
        "Live — red/brown, neutral — black, **earth — green**. The earth wire connects metal bodies of appliances to the ground for safety.",
        None, 15)
    S.q("ga-el-p4", "medium", "The standard **AC mains supply** in Indian homes is —",
        ["220 V, 50 Hz", "110 V, 60 Hz", "220 V, 5 Hz", "50 V, 220 Hz"], "220 V, 50 Hz",
        "India uses alternating current at about **220 V and 50 Hz** (the current reverses 50 times a second). 110 V/60 Hz is the American standard.",
        None, 15)
    S.q("ga-el-p5", "medium", "Arranged by **increasing wavelength**, the correct order is —",
        ["Gamma → X-rays → UV → Visible → Infrared → Microwave → Radio", "Radio → Microwave → Infrared → Visible → UV → X-rays → Gamma", "X-rays → Gamma → UV → Visible → Infrared → Microwave → Radio", "Visible → UV → X-rays → Gamma → Radio → Microwave → Infrared"], "Gamma → X-rays → UV → Visible → Infrared → Microwave → Radio",
        "Gamma rays have the shortest wavelength, radio waves the longest. Frequency increases in the reverse order. Mnemonic: 'Good X-rays Use Visible Infra-Micro Radios'.",
        None, 25)
    S.q("ga-el-p5", "easy", "**Microwave ovens** and **radar** use —",
        ["Microwaves", "Radio waves", "Ultraviolet rays", "Gamma rays"], "Microwaves",
        "**Microwaves** (between infrared and radio waves) are strongly absorbed by water molecules — perfect for heating food — and reflect well off objects, so radar uses them.",
        None, 15)
    S.q("ga-el-p5", "medium", "**Ultraviolet** radiation falling on the skin helps produce —",
        ["Vitamin D", "Vitamin A", "Vitamin C", "Vitamin K"], "Vitamin D",
        "UV-B converts a skin chemical into **vitamin D** — sunlight is the natural source. UV lamps also sterilise water and surgical tools.",
        None, 15)
    S.q("ga-el-p6", "hard", "A silicon crystal doped with a **trivalent** impurity such as boron becomes —",
        ["p-type semiconductor", "n-type semiconductor", "An insulator", "A superconductor"], "p-type semiconductor",
        "Trivalent atoms (boron, gallium) leave one bond short of an electron, creating **holes** — positive carriers — so the crystal is **p-type**. Pentavalent doping (phosphorus, arsenic) gives n-type.",
        None, 25)
    S.q("ga-el-p6", "medium", "A **rectifier** is a device that converts —",
        ["AC into DC", "DC into AC", "AC into mechanical energy", "Low voltage DC into high voltage DC"], "AC into DC",
        "Diodes act as **rectifiers**, turning alternating current into one-way (direct) current — chargers and power supplies do this. The reverse (DC → AC) is an inverter.",
        None, 20)
    return S
