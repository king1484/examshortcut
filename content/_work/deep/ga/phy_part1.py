"""physics deep content — part 1: ph-units, ph-mechanics, ph-heat-sound."""
import os
import sys

sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
from _lib import Sub


def g(x):
    """Format a computed number the way the options print it (no trailing .0)."""
    x = round(x, 6)
    return str(int(x)) if x == int(x) else str(x)


def build_units():
    S = Sub("ph-units")
    S.notes = """### Why units matter
Every measurement has two parts: a **number** and a **unit**. "The rod is 5" means nothing; "the rod is 5 metres" is a measurement. To let scientists everywhere compare results, the world uses one agreed system — the **SI system** (Système International, adopted in 1960). Competitive exams ask more questions on units and instruments than on any other physics area, because they are pure recall.

### The seven base quantities
Base (fundamental) quantities do not depend on any other quantity. SI has exactly **seven**:

| Quantity | SI unit | Symbol |
|---|---|---|
| Length | metre | m |
| Mass | kilogram | kg |
| Time | second | s |
| Electric current | ampere | A |
| Temperature | kelvin | K |
| Amount of substance | mole | mol |
| Luminous intensity | candela | cd |

Note: the unit of temperature is **kelvin**, not "degree kelvin", and not degree Celsius.

### Derived units named after scientists
Every other quantity is **derived** by multiplying or dividing base quantities. Many derived units carry a scientist's name:
- **Force** — newton (N) = kg·m/s². **Work / energy / heat** — joule (J). **Power** — watt (W) = J/s.
- **Pressure** — pascal (Pa) = N/m². **Frequency** — hertz (Hz) = 1/s.
- **Charge** — coulomb (C). **Potential difference** — volt (V). **Resistance** — ohm (Ω). **Capacitance** — farad (F).
- **Magnetic flux** — weber (Wb). **Magnetic field** — tesla (T). **Inductance** — henry (H).
- **Radioactivity** — becquerel (Bq). **Illuminance** — lux. **Power of a lens** — dioptre (D) = 1/metre.
Some derived quantities have no special name: **momentum** is kg·m/s, **velocity** is m/s, **acceleration** is m/s², **density** is kg/m³.

### Practical (non-SI) units — the trap list
- **Light year** = distance light covers in one year ≈ 9.46 × 10¹⁵ m. It measures **distance, not time**.
- **Parsec** ≈ 3.26 light years (also distance). **Astronomical unit (AU)** = mean Earth–Sun distance ≈ 1.5 × 10¹¹ m.
- **Angstrom** = 10⁻¹⁰ m (wavelengths); **fermi** = 10⁻¹⁵ m (nuclear sizes).
- **Nautical mile** = 1852 m; **knot** = one nautical mile per hour (speed of ships and aircraft).
- **Fathom** = 6 feet, used for depth of water. **Carat** = 200 mg for gems; for gold, "carat/karat" means purity (24 carat = pure).
- **Horsepower** ≈ 746 W. **Calorie** ≈ 4.186 J. **Electron volt** ≈ 1.6 × 10⁻¹⁹ J.
- **Kilowatt-hour (kWh)** = 1 "unit" on your electricity bill = 1000 W × 3600 s = 3.6 × 10⁶ J. It is a unit of **energy, not power**.
- **Bar** = 10⁵ Pa; **1 atmosphere** ≈ 1.013 × 10⁵ Pa. **Decibel (dB)** measures loudness level.

### Scalars and vectors
A **scalar** has only size (magnitude): mass, speed, distance, time, work, energy, power, temperature. A **vector** has size and direction: displacement, velocity, acceleration, force, momentum, weight. Easy test: if "towards the north" makes sense with it, it is a vector.

### Quick conversions
- km/h to m/s: multiply by **5/18**. So 36 km/h = 10 m/s. m/s to km/h: multiply by 18/5.
- Energy bill: units (kWh) = watts × hours ÷ 1000. A 100 W bulb for 10 hours uses 1 kWh.

### Instruments — what they measure
| Instrument | Measures |
|---|---|
| Ammeter / Voltmeter | Current / potential difference |
| Galvanometer | Detects small currents |
| Barometer | Atmospheric pressure |
| Manometer | Pressure of gases |
| Hygrometer | Relative humidity |
| Hydrometer | Density of liquids |
| Lactometer | Purity of milk (its density) |
| Anemometer | Wind speed |
| Altimeter | Altitude (aircraft) |
| Seismograph | Earthquake waves |
| Sphygmomanometer | Blood pressure |
| Pyrometer | Very high temperature |
| Tachometer | Rotational speed (rpm) |
| Odometer / Speedometer | Distance run / speed of a vehicle |
| Fathometer / SONAR | Depth of sea |
| Crescograph | Growth of plants |

### Quick revision
- 7 base units: m, kg, s, A, K, mol, cd.
- Light year, parsec, AU = distance. kWh = energy (3.6 × 10⁶ J). Horsepower ≈ 746 W.
- Nautical mile = 1852 m; knot = nautical mile per hour.
- km/h × 5/18 = m/s.
- Hygro = humidity, hydro = liquid density, lacto = milk, anemo = wind, sphygmo = blood pressure."""
    S.pattern("ga-un-p1", "SI unit of a physical quantity", "very common",
        "'The SI unit of pressure / charge / magnetic flux / power is …', or 'which pair of quantity and unit is wrongly matched'.",
        None,
        "1. Decide first whether the quantity is a base quantity (7 units) or a derived one.\n2. For derived quantities, recall the scientist-named unit: N, J, W, Pa, Hz, C, V, Ω, F, Wb, T, H.\n3. If there is no named unit (momentum, velocity), build it: momentum = kg·m/s.\nWhy: every unit is fixed by an international agreement, so recall is the only method — and elimination by dimensions helps.",
        "The SI unit of magnetic field (magnetic flux density) is —",
        "**Tesla (T).** Weber is the unit of magnetic **flux**; tesla = weber per square metre.")
    S.pattern("ga-un-p2", "Instrument → what it measures", "very common",
        "An instrument name ending in '-meter' or '-graph' is given and its use is asked, or the reverse.",
        None,
        "1. Break the name into its root: hygro (moisture), hydro (water/liquid), anemo (wind), baro (weight of air = pressure), seismo (shaking), sphygmo (pulse).\n2. Pick the option that fits the root.\n3. Watch the pairs hygrometer vs hydrometer, manometer vs sphygmomanometer.\nWhy: most names are Greek roots that describe the job.",
        "An **altimeter** is used to measure —",
        "**Altitude (height above sea level)**, mainly in aircraft. It works like a barometer: pressure falls as height rises.")
    S.pattern("ga-un-p3", "Practical and astronomical units", "common",
        "Units like light year, parsec, AU, knot, nautical mile, fathom, horsepower, carat or kWh — 'is a unit of …' or 'equals …'.",
        None,
        "1. Classify the unit by quantity: light year/parsec/AU/fathom/nautical mile = distance; knot = speed; kWh/calorie/eV = energy; horsepower = power.\n2. Recall the headline value (nautical mile 1852 m, 1 hp ≈ 746 W, 1 kWh = 3.6 × 10⁶ J).\n3. Beware the word 'year' and 'hour' in a unit name — they do not make it a unit of time.",
        "A **parsec** is a unit of —",
        "**Distance** (astronomical). 1 parsec ≈ 3.26 light years.")
    S.pattern("ga-un-p4", "Base vs derived units; scalar vs vector", "common",
        "'Which is NOT a fundamental unit', 'which is a vector quantity', 'which pair are both scalars'.",
        None,
        "1. Base units: metre, kilogram, second, ampere, kelvin, mole, candela — everything else is derived.\n2. Vector check: does direction change the meaning? Velocity, force, momentum, displacement, acceleration = vectors.\n3. Speed, distance, mass, work, energy, power, time = scalars.",
        "Which of the following is a scalar quantity?\n(a) Force (b) Momentum (c) Work (d) Displacement",
        "**(c) Work.** Work has only magnitude; force, momentum and displacement all need a direction.")
    S.pattern("ga-un-p5", "Unit-conversion and energy-bill numericals", "common",
        "A speed in km/h to convert, or appliance watts × hours to turn into kWh or ₹.",
        r"1\ \text{km/h}=\tfrac{5}{18}\ \text{m/s},\quad \text{units (kWh)}=\frac{\text{W}\times\text{h}}{1000}",
        "1. For speed: multiply km/h by 5/18 to get m/s (divide by 3.6).\n2. For bills: watts × hours per day × days ÷ 1000 = units; multiply by the rate.\n3. Check the size: a 1 kW appliance for 1 hour = exactly 1 unit.\nWhy: 1 km = 1000 m and 1 h = 3600 s, so 1000/3600 = 5/18.",
        "Convert 54 km/h to m/s.",
        "54 × 5/18 = **15 m/s**.")

    S.q("ga-un-p1", "easy", "The SI unit of **pressure** is —",
        ["Pascal", "Newton", "Bar", "Atmosphere"], "Pascal",
        "Pressure = force ÷ area, so its SI unit is N/m², named **pascal (Pa)**. Bar and atmosphere are practical units; newton is the unit of force.",
        "Pressure → Pascal (both start with P).", 15)
    S.q("ga-un-p1", "easy", "The SI unit of **electric charge** is —",
        ["Coulomb", "Ampere", "Volt", "Farad"], "Coulomb",
        "Charge is measured in **coulomb (C)**; 1 C = 1 ampere × 1 second. Ampere is current, volt is potential difference, farad is capacitance.",
        None, 15)
    S.q("ga-un-p1", "medium", "Which pair of quantity and SI unit is **wrongly** matched?",
        ["Momentum – newton", "Power – watt", "Frequency – hertz", "Work – joule"], "Momentum – newton",
        "Momentum = mass × velocity, so its unit is **kg·m/s**. Newton is the unit of force. The other three pairs are correct.",
        "Momentum has no named unit — any 'named' answer for it is wrong.", 20)
    S.q("ga-un-p2", "easy", "The instrument used to measure **blood pressure** is —",
        ["Sphygmomanometer", "Manometer", "Barometer", "Stethoscope"], "Sphygmomanometer",
        "A **sphygmomanometer** (sphygmo = pulse) measures blood pressure, usually in mm of mercury. A manometer measures gas pressure, a barometer air pressure; a stethoscope only lets the doctor hear sounds.",
        None, 15)
    S.q("ga-un-p2", "medium", "An **anemometer** measures —",
        ["Wind speed", "Atmospheric pressure", "Relative humidity", "Height of aircraft"], "Wind speed",
        "**Anemo** means wind. The anemometer (rotating cups) measures wind speed. Pressure = barometer, humidity = hygrometer, height = altimeter.",
        "Anemo = wind.", 15)
    S.q("ga-un-p2", "medium", "A **lactometer** is used to test —",
        ["The purity of milk", "The fat content of butter", "The temperature of milk", "The acidity of curd"], "The purity of milk",
        "A lactometer is a special hydrometer. It measures the **density (specific gravity) of milk**; watered milk has a lower density, so the lactometer shows adulteration.",
        "Lacto = milk.", 20)
    S.q("ga-un-p2", "easy", "Which instrument records the waves produced by an **earthquake**?",
        ["Seismograph", "Altimeter", "Pyrometer", "Tachometer"], "Seismograph",
        "A **seismograph** records ground shaking. Pyrometer = very high temperature, tachometer = rpm of an engine, altimeter = altitude.",
        None, 15)
    S.q("ga-un-p3", "medium", "One **nautical mile** is equal to —",
        ["1852 m", "1609 m", "1000 m", "1760 m"], "1852 m",
        "A nautical mile is **1852 m**, used at sea and in the air. 1609 m is the ordinary (statute) mile; 1760 is the number of yards in a mile.",
        None, 20)
    S.q("ga-un-p3", "easy", "**Knot** is a unit of —",
        ["Speed of ships and aircraft", "Depth of the sea", "Distance on land", "Purity of gold"], "Speed of ships and aircraft",
        "1 knot = 1 nautical mile per hour (≈ 1.852 km/h). It is a unit of **speed**. Depth of the sea uses the fathom; purity of gold uses carat.",
        None, 15)
    S.q("ga-un-p3", "medium", "One **horsepower** is approximately equal to —",
        ["746 W", "1000 W", "550 W", "100 W"], "746 W",
        "1 horsepower ≈ **746 watt**. (550 is the value in foot-pounds per second, a common trap.)",
        None, 20)
    S.q("ga-un-p4", "medium", "Which of the following is **NOT** one of the seven SI base units?",
        ["Newton", "Kelvin", "Candela", "Mole"], "Newton",
        "The base units are metre, kilogram, second, ampere, kelvin, mole and candela. The **newton** is derived: 1 N = 1 kg·m/s².",
        "Named after a person but not in the 7-list = derived (only kelvin and ampere are both).", 20)
    S.q("ga-un-p4", "easy", "Which of the following is a **vector** quantity?",
        ["Velocity", "Speed", "Mass", "Energy"], "Velocity",
        "**Velocity** is speed in a stated direction, so it is a vector. Speed, mass and energy have only magnitude — scalars.",
        None, 15)
    kmh = 72
    ms = kmh * 5 / 18
    assert ms == 20
    S.q("ga-un-p5", "easy", "A train runs at **72 km/h**. Its speed in m/s is —",
        [g(ms) + " m/s", g(kmh * 3.6) + " m/s", "25 m/s", "72 m/s"], g(ms) + " m/s",
        "72 × 5/18 = **20 m/s**. Multiplying by 3.6 instead (259.2) is the reverse conversion and a common mistake.",
        "÷ 3.6 : 72 ÷ 3.6 = 20.", 20)
    units = 1500 * 2 * 30 / 1000
    bill = units * 6
    assert bill == 540
    S.q("ga-un-p5", "medium", "A **1500 W** geyser runs 2 hours a day for 30 days. At ₹6 per unit, the electricity cost is —",
        ["₹" + g(bill), "₹" + g(units), "₹" + g(bill * 10), "₹" + g(bill / 2)], "₹" + g(bill),
        "Energy = 1.5 kW × 2 h × 30 = **90 kWh (units)**. Cost = 90 × ₹6 = **₹540**.",
        "kW × hours × days × rate: 1.5 × 2 × 30 × 6 = 540.", 35)
    return S


def build_mech():
    S = Sub("ph-mechanics")
    S.notes = """### Motion in simple words
A body is in **motion** when its position changes with time. **Distance** is the total path covered (scalar); **displacement** is the straight-line gap from start to end with direction (vector). **Speed** = distance ÷ time; **velocity** = displacement ÷ time. **Acceleration** is the rate of change of velocity (m/s²). Walking once round a circular park gives a large distance but **zero displacement**.

### Newton's three laws
1. **First law (inertia):** a body stays at rest or keeps moving in a straight line unless an outside force acts. Examples: passengers fall **forward** when a moving bus brakes (inertia of motion); they fall **backward** when a stopped bus starts suddenly (inertia of rest); dust leaves a carpet when it is beaten. **Mass is the measure of inertia.**
2. **Second law:** force = mass × acceleration ($F = ma$); force is also the rate of change of **momentum** ($p = mv$). A cricketer pulls his hands back while catching — he increases the time of impact, so the force on his hands is smaller. Cars have crumple zones and air bags for the same reason.
3. **Third law:** every action has an equal and opposite reaction. Rockets and jet planes, recoil of a gun, swimming, walking (we push the ground back, it pushes us forward).
**Conservation of momentum:** without outside force, total momentum stays constant — the gun recoils because bullet and gun share zero total momentum.

### Gravitation
Newton's law: every two masses attract with force $F = Gm_1m_2/r^2$, where G = 6.67 × 10⁻¹¹ N·m²/kg² (the same everywhere in the universe). Near the Earth this pull gives **g ≈ 9.8 m/s²**.
- g is **maximum at the poles** and **minimum at the equator** (the Earth bulges at the equator and spins).
- g **decreases with height** and **with depth**; it is **zero at the Earth's centre**.
- **Mass** (kg) never changes; **weight** = mg (newton) changes with place. On the Moon, g is about **1/6** of Earth's, so a 60 kg person still has 60 kg mass but weighs one-sixth as much.
- In a freely falling lift or an orbiting spacecraft, people feel **weightless**.
- **Escape velocity** from Earth ≈ **11.2 km/s**; it does not depend on the mass of the object. Orbital speed close to the surface ≈ 7.9 km/s.
- A **geostationary satellite** circles above the equator at about 36,000 km, with a period of **24 hours**, so it appears fixed in the sky — used for TV and weather.

### Work, energy and power
**Work** = force × displacement in the direction of force (joule). No displacement means no work — a man holding a heavy box still does no work on it. A force at right angles to motion (like the centripetal force in circular motion) does **zero work**.
**Kinetic energy** = ½mv² — doubling speed makes it **four times**. **Potential energy** = mgh. Energy only changes form: a falling stone turns PE into KE. **Power** = work ÷ time (watt).

### Fluids — the principle behind the gadget
| Principle | Idea | Everyday use |
|---|---|---|
| **Pascal's law** | Pressure on an enclosed liquid spreads equally in all directions | Hydraulic lift, hydraulic brakes, hydraulic press |
| **Archimedes' principle** | Upthrust = weight of liquid displaced | Ships float, hydrometer, lactometer, submarines |
| **Bernoulli's principle** | Where a fluid moves faster, its pressure is lower | Lift on aeroplane wings, roofs blown off in storms, atomiser/sprayer |
| **Surface tension** | Liquid surface acts like a stretched skin | Spherical drops, insects walking on water; soap lowers it |
| **Capillarity** | Liquid rises in thin tubes | Oil in a lamp wick, blotting paper, towels |
| **Viscosity** | Internal friction of fluids | Honey flows slowly; liquid viscosity falls when heated |
Ice floats because it is **less dense** than water (about 0.92 g/cm³). A ship floats but an iron nail sinks because the ship's shape displaces much more water.

### Levers
A lever has a **fulcrum (F)**, a **load (L)** and an **effort (E)**. The class is fixed by what sits **in the middle**:
- **Class 1 — F in the middle:** seesaw, scissors, pliers, crowbar, beam balance.
- **Class 2 — L in the middle:** nutcracker, wheelbarrow, bottle opener, lemon squeezer.
- **Class 3 — E in the middle:** tongs, forceps, fishing rod, human forearm, broom.
Class 2 always gives mechanical advantage; class 3 never does but gives speed and control.

### Quick revision
- Inertia ↔ mass; F = ma; action = reaction (rocket, recoil).
- g: max at poles, min at equator, zero at the centre; Moon ≈ 1/6.
- Escape velocity 11.2 km/s; geostationary period 24 h.
- KE ∝ v² (double speed → 4× KE); work = 0 if no displacement or force ⟂ motion.
- Pascal → hydraulic; Archimedes → floating; Bernoulli → aeroplane lift.
- Lever middle: F-L-E = class 1-2-3."""
    S.pattern("ga-me-p1", "Everyday event → Newton's law / momentum", "very common",
        "A daily-life situation (bus braking, rocket, gun recoil, cricketer catching, carpet beating) and options listing the laws.",
        None,
        "1. Body resists a change in its state of rest/motion → **first law (inertia)**.\n2. Force reduced by taking more time, or F = ma → **second law / momentum change**.\n3. Push one way, move the other (rocket, recoil, swimming) → **third law / conservation of momentum**.\nWhy: each law describes one distinct effect, and the story tells you which.",
        "When a carpet is beaten with a stick, the dust comes out. This is due to —",
        "**Inertia of rest (Newton's first law).** The carpet moves, the dust tends to stay at rest and separates.")
    S.pattern("ga-me-p2", "Gravitation, weight and satellites", "very common",
        "Questions on g at poles/equator/centre, weight on the Moon, escape velocity, geostationary orbit, weightlessness.",
        r"W = mg,\quad g_{moon}\approx \tfrac{1}{6}g_{earth}",
        "1. Mass is fixed; weight changes with g.\n2. g: poles > equator; decreases up and down; zero at the centre.\n3. Key numbers: g ≈ 9.8 m/s², escape 11.2 km/s, geostationary 24 h at ~36,000 km.",
        "A body has a mass of 30 kg on Earth. What is its mass on the Moon?",
        "**30 kg.** Mass never changes with place; only weight falls to about one-sixth.")
    S.pattern("ga-me-p3", "Fluid principle → application", "very common",
        "A device or effect (hydraulic brake, floating ship, aeroplane lift, lamp wick, round raindrops) and a list of principles.",
        None,
        "1. Enclosed liquid, force multiplied → **Pascal**.\n2. Floating / sinking / upthrust → **Archimedes**.\n3. Fast-moving air, low pressure → **Bernoulli**.\n4. Drops, skin-like surface → **surface tension**; rising in thin tubes → **capillarity**; thick flow → **viscosity**.",
        "The roof of a hut is blown off during a storm. Which principle explains this?",
        "**Bernoulli's principle** — fast wind above the roof lowers the pressure there; the higher pressure inside pushes the roof up.")
    S.pattern("ga-me-p4", "Class of lever", "common",
        "A tool (scissors, nutcracker, forceps, wheelbarrow, human arm) and 'is a lever of class …'.",
        None,
        "1. Locate fulcrum, load and effort on the tool.\n2. See which one is in the middle: **F → class 1, L → class 2, E → class 3** (F-L-E = 1-2-3).\n3. Double-check with the standard list: forceps/tongs/arm are class 3.",
        "A **bottle opener** is a lever of which class?",
        "**Class 2** — the cap (load) is between the fulcrum (edge resting on the top) and your hand (effort).")
    S.pattern("ga-me-p5", "Work, energy and power basics", "common",
        "'If velocity is doubled, KE becomes…', 'work done when …', or a small power calculation.",
        r"KE=\tfrac12 mv^2,\quad PE=mgh,\quad P=\frac{W}{t}",
        "1. KE depends on v², so v × k gives KE × k².\n2. Work = F × s × cos θ — zero if s = 0 or the force is perpendicular to motion.\n3. Power = work (mgh for lifting) ÷ time.",
        "A body's velocity is made three times. Its kinetic energy becomes —",
        "KE ∝ v², so 3² = **9 times**.")

    S.q("ga-me-p1", "easy", "Passengers standing in a moving bus fall **forward** when the driver brakes suddenly. This is due to —",
        ["Inertia of motion", "Inertia of rest", "Newton's third law", "Friction of the floor"], "Inertia of motion",
        "The feet stop with the bus, but the upper body keeps moving forward because of **inertia of motion** (Newton's first law).",
        None, 15)
    S.q("ga-me-p1", "medium", "A cricketer pulls his hands backward while catching a fast ball in order to —",
        ["Increase the time of impact and so reduce the force", "Reduce the time of impact", "Increase the momentum of the ball", "Increase the force on the ball"], "Increase the time of impact and so reduce the force",
        "Force = change in momentum ÷ time. The ball's momentum must fall to zero anyway; taking **more time** makes the force on the palms **smaller** (Newton's second law).",
        "Same idea: air bags, crumple zones, sand in a long-jump pit.", 20)
    S.q("ga-me-p1", "easy", "The upward motion of a **rocket** is based on —",
        ["Newton's third law of motion", "Newton's first law of motion", "Law of gravitation", "Pascal's law"], "Newton's third law of motion",
        "The rocket pushes hot gases **downward** (action); the gases push the rocket **upward** (reaction) — Newton's third law, also seen as conservation of momentum.",
        None, 15)
    wt = 600 / 6
    S.q("ga-me-p2", "easy", "A man weighs **600 N** on the Earth. His weight on the Moon will be about —",
        [g(wt) + " N", "600 N", "3600 N", "0 N"], g(wt) + " N",
        "g on the Moon is about **1/6** of Earth's, so weight ≈ 600 ÷ 6 = **100 N**. His **mass** stays the same.",
        None, 20)
    S.q("ga-me-p2", "medium", "The **escape velocity** from the Earth's surface is about —",
        ["11.2 km/s", "7.9 km/s", "3 km/s", "42 km/s"], "11.2 km/s",
        "An object must be launched at about **11.2 km/s** to escape Earth's gravity. 7.9 km/s is the orbital speed just above the surface.",
        None, 15)
    S.q("ga-me-p2", "medium", "The acceleration due to gravity (g) at the **centre of the Earth** is —",
        ["Zero", "Maximum", "9.8 m/s²", "Infinite"], "Zero",
        "g falls as we go deeper, because less mass lies 'below' us. At the centre the pull from all sides cancels and **g = 0**.",
        "g is zero at the centre, largest at the poles.", 15)
    S.q("ga-me-p2", "medium", "A **geostationary satellite** completes one orbit round the Earth in —",
        ["24 hours", "12 hours", "90 minutes", "27 days"], "24 hours",
        "It orbits above the equator at about 36,000 km, taking **24 hours** — the same as Earth's rotation — so it looks fixed from the ground. 90 minutes is typical of low-orbit satellites; 27 days is roughly the Moon's orbit.",
        None, 15)
    S.q("ga-me-p3", "easy", "A ship made of steel floats on water because of —",
        ["Archimedes' principle", "Pascal's law", "Bernoulli's principle", "Newton's first law"], "Archimedes' principle",
        "The hollow ship displaces a large volume of water; the upthrust (weight of displaced water) equals the ship's weight — **Archimedes' principle**.",
        None, 15)
    S.q("ga-me-p3", "medium", "The upward **lift** on the wings of an aeroplane is explained by —",
        ["Bernoulli's principle", "Archimedes' principle", "Pascal's law", "Hooke's law"], "Bernoulli's principle",
        "Air flows faster over the curved upper surface of the wing, so pressure there is lower than below — the pressure difference lifts the plane (**Bernoulli**).",
        None, 20)
    S.q("ga-me-p3", "easy", "Oil rises up the wick of a lamp because of —",
        ["Capillary action", "Viscosity", "Buoyancy", "Osmosis"], "Capillary action",
        "The wick has many fine channels that act like thin tubes; oil climbs them by **capillarity**. Blotting paper works the same way.",
        None, 15)
    S.q("ga-me-p4", "medium", "The **human forearm** lifting a weight works as a lever of —",
        ["Class 3", "Class 1", "Class 2", "It is not a lever"], "Class 3",
        "Elbow = fulcrum, weight in the hand = load, biceps pull between them = effort. Effort in the middle → **class 3**.",
        "E in the middle = 3.", 20)
    S.q("ga-me-p4", "medium", "Which of the following is a **Class 2** lever?",
        ["Wheelbarrow", "Fishing rod", "Seesaw", "Forceps"], "Wheelbarrow",
        "In a **wheelbarrow** the wheel is the fulcrum, the load sits in the middle, and effort is at the handles — class 2. Seesaw is class 1; fishing rod and forceps are class 3.",
        None, 20)
    ratio = 2 ** 2
    S.q("ga-me-p5", "easy", "If the speed of a moving body is **doubled**, its kinetic energy becomes —",
        [g(ratio) + " times", "2 times", "Half", "8 times"], g(ratio) + " times",
        "KE = ½mv². Doubling v multiplies v² by 2² = **4**.",
        "KE follows the square of speed.", 15)
    m, gg, h, t = 50, 10, 12, 20
    P = m * gg * h / t
    assert P == 300
    S.q("ga-me-p5", "hard", "A boy of mass **50 kg** runs up a staircase **12 m** high in **20 s**. Taking g = 10 m/s², his power is —",
        [g(P) + " W", g(m * gg * h) + " W", g(m * h / t) + " W", g(P * 2) + " W"], g(P) + " W",
        "Work = mgh = 50 × 10 × 12 = 6000 J. Power = 6000 ÷ 20 = **300 W**.",
        "mgh ÷ t in one line.", 40)
    return S


def build_hs():
    S = Sub("ph-heat-sound")
    S.notes = """### Heat and temperature are different
**Heat** is energy that flows from a hotter body to a colder one (unit: joule; older unit calorie). **Temperature** tells how hot a body is — the average energy of its particles (unit: kelvin). A bucket of warm water holds more heat than a cup of boiling water, though the cup is at a higher temperature.

### Temperature scales
| Scale | Ice melts | Water boils |
|---|---|---|
| Celsius | 0 °C | 100 °C |
| Fahrenheit | 32 °F | 212 °F |
| Kelvin | 273 K (273.15) | 373 K |
Conversions: $F = \\frac{9}{5}C + 32$ and $K = C + 273$. Celsius and Fahrenheit agree at **−40°**. Normal body temperature is **37 °C = 98.6 °F**. The lowest possible temperature is **0 K (absolute zero) = −273.15 °C**. A clinical thermometer reads about 35–42 °C; a **pyrometer** measures very high temperatures (furnaces).

### Specific heat and latent heat
- **Specific heat** is the heat needed to raise 1 kg of a substance by 1 °C. **Water has a very high specific heat**, so it heats and cools slowly. That is why coastal places have mild climates, why water is used in car radiators and hot-water bottles.
- **Latent heat** is heat taken or given during a change of state **without any change in temperature**. Steam at 100 °C burns more than water at 100 °C because it also releases its large latent heat of vaporisation when it condenses on skin. Ice at 0 °C cools a drink better than water at 0 °C because melting absorbs latent heat.
- **Evaporation causes cooling**: water in an earthen pot (matka) stays cool, sweating cools the body, a wet cloth feels cold. Evaporation is faster with more surface area, heat, wind and dry air.

### Boiling, melting and pressure
Higher pressure **raises** the boiling point — a **pressure cooker** cooks faster because water boils above 100 °C inside it. On mountains air pressure is low, water boils below 100 °C, and food cooks slowly. Pressure **lowers** the melting point of ice (regelation — two ice blocks pressed together join).

### Anomalous expansion of water
Most things expand on heating. Water contracts from 0 °C to **4 °C** and then expands, so it is **densest at 4 °C**. In winter the top of a lake freezes first and floating ice insulates the water below, which stays near 4 °C — fish survive. Pipes burst in frost because water expands on freezing. Gaps in railway tracks and sagging electric wires in summer are examples of ordinary thermal expansion.

### Three ways heat travels
- **Conduction** — through solids, particle to particle (hot spoon handle). Metals conduct well; wood, plastic and air are insulators.
- **Convection** — by movement of the liquid or gas itself. **Sea breeze** (day) and **land breeze** (night), boiling water, room heaters.
- **Radiation** — no medium needed; the **Sun's heat** reaches us this way. Dark, rough surfaces absorb and emit well; white clothes keep us cool in summer.
A **thermos flask** blocks all three: vacuum (conduction and convection) and silvered walls (radiation).

### Sound — a mechanical wave
Sound is produced by vibration and travels as a **longitudinal wave** that needs a medium; it **cannot travel in vacuum** (astronauts use radio). Speed of sound: about **343 m/s in air** at 20 °C (≈ 332 m/s at 0 °C), ≈ 1500 m/s in water, ≈ 5000 m/s or more in steel — **solids > liquids > gases**. Speed rises with **temperature** and **humidity**; pressure alone does not change it.

### Frequency ranges and characteristics
- Human audible range: **20 Hz to 20,000 Hz**. Below 20 Hz = **infrasonic** (earthquakes, elephants, whales). Above 20 kHz = **ultrasonic** (bats, dolphins, SONAR, ultrasound scans, cleaning).
- **Pitch** depends on **frequency** (women and children have higher-pitched voices). **Loudness** depends on **amplitude**, measured in **decibel (dB)**. **Quality (timbre)** depends on the waveform — it lets us tell a sitar from a flute at the same note.

### Echo, Doppler effect and resonance
- **Echo**: reflected sound heard separately if it returns after at least 0.1 s — needs a reflector about 17 m away. Distance = speed × time ÷ 2.
- **Doppler effect**: an approaching horn sounds higher-pitched, a receding one lower.
- **Resonance**: a body vibrates strongly when pushed at its natural frequency — soldiers break step on bridges; tuning a radio.
- **Sonic boom**: produced by objects moving faster than sound (supersonic).

### Quick revision
- F = 9C/5 + 32; K = C + 273; −40 °C = −40 °F; body 37 °C = 98.6 °F.
- Water: highest specific heat, densest at 4 °C.
- Steam burns worse — latent heat. Pressure cooker — higher boiling point.
- Conduction (solids), convection (fluids, breezes), radiation (Sun, no medium).
- Sound: solids fastest, vacuum none; 20 Hz–20 kHz; pitch ↔ frequency, loudness ↔ amplitude."""
    S.pattern("ga-hs-p1", "Temperature scale conversion", "very common",
        "A temperature in one scale to convert, or 'at what temperature do two scales read the same / one reads double the other'.",
        r"\frac{C}{5}=\frac{F-32}{9}=\frac{K-273}{5}",
        "1. Write C/5 = (F − 32)/9.\n2. Substitute the given value (or the condition, e.g. F = C or F = 2C) and solve.\n3. For Kelvin just add 273.\nWhy: 100 Celsius divisions cover the same range as 180 Fahrenheit divisions, so the ratio is 5 : 9 with a 32° offset.",
        "Convert 25 °C to Fahrenheit.",
        "F = 9/5 × 25 + 32 = 45 + 32 = **77 °F**.")
    S.pattern("ga-hs-p2", "Everyday heat effect → reason", "very common",
        "'Why does steam burn more / pressure cooker cook faster / earthen pot cool water / fish survive frozen lakes / coastal climate mild?'",
        None,
        "1. Change of state with no temperature change → **latent heat**.\n2. Slow heating/cooling of water → **high specific heat**.\n3. Boiling point up with pressure, down at altitude.\n4. Cooling without a fridge → **evaporation**.\n5. Lakes freeze from the top → **anomalous expansion** (max density at 4 °C).",
        "Why does food take longer to cook on high mountains?",
        "Air pressure is low, so water **boils below 100 °C**; food gets less heat and cooks slowly.")
    S.pattern("ga-hs-p3", "Mode of heat transfer", "common",
        "A situation (sea breeze, Sun's heat, hot spoon handle, thermos flask, white clothes) and options conduction/convection/radiation.",
        None,
        "1. Heat moves through a solid without the solid moving → **conduction**.\n2. The warm fluid itself moves (breezes, boiling) → **convection**.\n3. No medium / across empty space / colour matters → **radiation**.",
        "Land breeze blowing at night is an example of —",
        "**Convection** — the sea is warmer at night, air over it rises, and cooler air from the land moves in.")
    S.pattern("ga-hs-p4", "Speed of sound and the medium", "common",
        "'Sound travels fastest in…', 'cannot travel through…', 'speed of sound increases with…'.",
        None,
        "1. Order: solids > liquids > gases; vacuum = no sound.\n2. Temperature and humidity raise the speed in air; pressure alone does not change it.\n3. Remember air ≈ 343 m/s, water ≈ 1500 m/s, steel ≈ 5000 m/s.",
        "Why is the sound of an approaching train heard earlier by putting an ear to the rail?",
        "Sound travels **much faster in steel** (a solid) than in air.")
    S.pattern("ga-hs-p5", "Frequency ranges; pitch, loudness, quality", "very common",
        "Audible range, infrasonic/ultrasonic users (bats, dolphins, elephants), or which property of a wave decides pitch/loudness/timbre.",
        None,
        "1. Audible 20 Hz–20 kHz; below = infrasonic; above = ultrasonic.\n2. Pitch ↔ frequency; loudness ↔ amplitude (dB); quality ↔ waveform.\n3. Ultrasound uses: SONAR, medical scans, bats' echolocation.",
        "Sound waves of frequency 10 Hz are called —",
        "**Infrasonic** — they are below the 20 Hz lower limit of human hearing.")
    S.pattern("ga-hs-p6", "Echo, Doppler effect and resonance", "occasional",
        "Echo-distance numericals, 'pitch of approaching horn rises', 'soldiers break step on a bridge'.",
        r"d=\frac{v\times t}{2}",
        "1. Echo: sound goes to the reflector and back, so distance = v × t ÷ 2.\n2. Change in heard pitch because source/listener moves → **Doppler effect**.\n3. Large vibration at the natural frequency → **resonance**.",
        "An echo returns in 3 s; speed of sound is 330 m/s. How far is the reflecting wall?",
        "d = 330 × 3 ÷ 2 = **495 m**.")

    F = 9 / 5 * 37 + 32
    assert abs(F - 98.6) < 1e-9
    S.q("ga-hs-p1", "easy", "Normal human body temperature **37 °C** on the Fahrenheit scale is —",
        ["98.6 °F", "99.6 °F", "96.6 °F", "69 °F"], "%.1f °F" % F,
        "F = 9/5 × 37 + 32 = 66.6 + 32 = **98.6 °F**. Just adding 32 (69) is the common slip.",
        None, 20)
    C = 32 / (2 - 9 / 5)
    assert abs(C - 160) < 1e-9
    S.q("ga-hs-p1", "hard", "At what Celsius temperature is the Fahrenheit reading **exactly double** the Celsius reading?",
        [g(C) + " °C", "80 °C", "40 °C", "−40 °C"], g(C) + " °C",
        "Put F = 2C in F = 9C/5 + 32: 2C − 1.8C = 32 → 0.2C = 32 → **C = 160 °C** (and F = 320 °F). −40 is where the two readings are **equal**, not double.",
        None, 40)
    K = 50 + 273
    S.q("ga-hs-p1", "easy", "A temperature of **50 °C** on the Kelvin scale is (take 0 °C = 273 K) —",
        [g(K) + " K", "223 K", "122 K", "50 K"], g(K) + " K",
        "K = C + 273 = 50 + 273 = **323 K**. (Subtracting gives 223, a common slip.)",
        None, 15)
    S.q("ga-hs-p2", "easy", "Food cooks faster in a **pressure cooker** because —",
        ["The higher pressure raises the boiling point of water", "The higher pressure lowers the boiling point of water", "Steel conducts heat faster", "Less water evaporates, so no heat is lost"], "The higher pressure raises the boiling point of water",
        "Trapped steam increases pressure, so water boils at about 120 °C instead of 100 °C; the hotter water cooks food faster.",
        None, 15)
    S.q("ga-hs-p2", "easy", "Water kept in an **earthen pot (matka)** stays cool because of —",
        ["Evaporation", "Condensation", "Radiation", "Conduction"], "Evaporation",
        "Water seeps through the pot's tiny pores and **evaporates** from the outside surface, taking latent heat from the water inside.",
        None, 15)
    S.q("ga-hs-p2", "medium", "Fish survive in lakes that freeze in winter because water has its **maximum density** at —",
        ["4 °C", "0 °C", "100 °C", "−4 °C"], "4 °C",
        "Water is densest at **4 °C** (anomalous expansion). Colder water and ice float on top, the ice layer insulates, and water at the bottom stays near 4 °C.",
        None, 20)
    S.q("ga-hs-p2", "medium", "Places near the sea have a milder climate than inland places mainly because water has a —",
        ["High specific heat", "Low specific heat", "High density", "Low boiling point"], "High specific heat",
        "Water's **high specific heat** means the sea heats up and cools down slowly, keeping nearby land from getting very hot or very cold.",
        None, 20)
    S.q("ga-hs-p3", "easy", "Heat from the **Sun** reaches the Earth by —",
        ["Radiation", "Conduction", "Convection", "Reflection"], "Radiation",
        "Space between the Sun and the Earth is almost empty; only **radiation** needs no medium.",
        None, 15)
    S.q("ga-hs-p3", "medium", "A **thermos (vacuum) flask** keeps tea hot because it reduces heat loss by —",
        ["Conduction, convection and radiation", "Conduction only", "Radiation only", "Convection only"], "Conduction, convection and radiation",
        "The vacuum between the double walls stops **conduction and convection**, and the silvered walls reflect back **radiation** — all three are reduced.",
        None, 20)
    S.q("ga-hs-p4", "easy", "Sound travels **fastest** in —",
        ["Steel", "Water", "Air", "Vacuum"], "Steel",
        "Sound is fastest in solids (steel ≈ 5000 m/s or more), slower in water (≈ 1500 m/s), slower still in air (≈ 343 m/s), and does not travel in vacuum.",
        None, 15)
    S.q("ga-hs-p4", "medium", "The speed of sound in air **increases** when —",
        ["The temperature of the air rises", "The temperature of the air falls", "Air pressure rises at constant temperature", "The loudness of the sound increases"], "The temperature of the air rises",
        "Warmer air carries sound faster (about 0.6 m/s per °C). At constant temperature, pressure changes do not affect it, and loudness has no effect on speed.",
        None, 20)
    S.q("ga-hs-p5", "easy", "The normal range of human hearing is —",
        ["20 Hz to 20,000 Hz", "2 Hz to 2,000 Hz", "200 Hz to 200,000 Hz", "20 kHz to 200 kHz"], "20 Hz to 20,000 Hz",
        "Humans hear **20 Hz – 20 kHz**. Below is infrasonic, above is ultrasonic.",
        None, 15)
    S.q("ga-hs-p5", "medium", "The **pitch** of a sound depends on its —",
        ["Frequency", "Amplitude", "Speed", "Loudness"], "Frequency",
        "Higher **frequency** = higher pitch (a shrill sound). Amplitude decides loudness; speed depends on the medium.",
        "Pitch ↔ frequency; loudness ↔ amplitude.", 15)
    S.q("ga-hs-p5", "medium", "Bats find their way in the dark using —",
        ["Ultrasonic sound", "Infrasonic sound", "Infrared rays", "Radio waves"], "Ultrasonic sound",
        "Bats emit **ultrasonic** squeaks (above 20 kHz) and listen for echoes — echolocation. The same idea is used in SONAR.",
        None, 15)
    d = 340 * 2 / 2
    S.q("ga-hs-p6", "medium", "A boy hears the echo of his shout from a cliff **2 s** later. If sound travels at **340 m/s**, the cliff is —",
        [g(d) + " m away", g(340 * 2) + " m away", g(d / 2) + " m away", g(340 * 4) + " m away"], g(d) + " m away",
        "Sound travels to the cliff and back: 2d = 340 × 2 → d = **340 m**. Forgetting to halve gives 680 m.",
        "Halve the total path.", 30)
    S.q("ga-hs-p6", "medium", "The whistle of an **approaching** train sounds higher-pitched than that of a receding one. This is due to —",
        ["Doppler effect", "Resonance", "Echo", "Refraction of sound"], "Doppler effect",
        "When the source moves towards the listener, more waves reach per second — heard frequency rises. This is the **Doppler effect**.",
        None, 15)
    S.q("ga-hs-p6", "medium", "Soldiers are asked to **break step** while crossing a bridge in order to avoid —",
        ["Resonance", "Echo", "Doppler effect", "Interference of light"], "Resonance",
        "Marching in step could match the bridge's natural frequency, causing large **resonant** vibrations that may damage it.",
        None, 15)
    return S
