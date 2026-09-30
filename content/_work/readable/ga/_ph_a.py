"""Physics part A: units, mechanics."""
from _ph_common import pat, mis, trick

S = {}
FNOTES = {}

# numeric checks used in examples below
assert 54 * 5 == 15 * 18
assert 36 * 5 == 10 * 18
assert 100 * 10 / 1000 == 1.0
assert 1000 * 3600 == 3_600_000
assert 3 ** 2 == 9

# =====================================================================
S["ph-units"] = dict(
    concept=(
        "Every measurement has a number and a unit. The world uses one agreed system, the **SI system**, "
        "which has seven base units. All other units are built from these seven. "
        "Exams ask many recall questions here: named units, practical units and instruments."
    ),
    notes=r"""### The seven base units
A measurement needs a number and a unit. "The rod is 5" means nothing. "The rod is 5 metres" does.

The **SI system** (Système International, adopted in 1960) has exactly seven base quantities. They do not depend on any other quantity.

| Quantity | SI unit | Symbol |
|---|---|---|
| Length | metre | m |
| Mass | kilogram | kg |
| Time | second | s |
| Electric current | ampere | A |
| Temperature | kelvin | K |
| Amount of substance | mole | mol |
| Luminous intensity | candela | cd |

> **Watch:** The unit of temperature is the kelvin, not "degree kelvin". Newton, joule and volt are not base units.

### Derived units with names
Every other quantity is built from the seven base ones. Many derived units carry a scientist's name.

| Quantity | Unit | Quantity | Unit |
|---|---|---|---|
| Force | newton (N) | Electric charge | coulomb (C) |
| Work, energy, heat | joule (J) | Potential difference | volt (V) |
| Power | watt (W) | Resistance | ohm (Ω) |
| Pressure | pascal (Pa) | Capacitance | farad (F) |
| Frequency | hertz (Hz) | Inductance | henry (H) |
| Magnetic field | tesla (T) | Magnetic flux | weber (Wb) |
| Power of a lens | dioptre (D) | Radioactivity | becquerel (Bq) |
| Luminous flux | lumen | Illuminance | lux |
| Sound level | decibel (dB) | Speed of ships | knot |

Some units are built from base units. Force is kg·m/s², power is J/s, pressure is N/m², and frequency is 1/s. The dioptre is 1/metre. Momentum is kg·m/s, velocity is m/s, acceleration is m/s² and density is kg/m³.

### Practical units and their values
Some units are not SI, but exams love them. Learn what each one measures.

| Unit | Measures | Value |
|---|---|---|
| Light year | Distance, not time | about 9.46 × 10¹⁵ m |
| Parsec | Distance | about 3.26 light years |
| Astronomical unit (AU) | Distance | mean Earth–Sun distance, about 1.5 × 10¹¹ m |
| Ångström | Wavelength | 10⁻¹⁰ m |
| Fermi | Nuclear size | 10⁻¹⁵ m |
| Nautical mile | Distance at sea | 1852 m |
| Knot | Speed of ships and aircraft | one nautical mile per hour |
| Fathom | Depth of water | 6 feet |
| Carat | Weight of gems | 200 mg |
| Horsepower | Power | about 746 W |
| Calorie | Heat | about 4.186 J |
| Electron volt | Energy | about 1.6 × 10⁻¹⁹ J |
| Kilowatt-hour | Energy | 3.6 × 10⁶ J |
| Bar | Pressure | 10⁵ Pa |
| Atmosphere | Pressure | about 1.013 × 10⁵ Pa |

For gold, "carat" means purity. 24 carat gold is pure.

> **Watch:** Words like "year" and "hour" inside a unit name do not make it a unit of time. A light year is distance. A kilowatt-hour is energy.

### Scalars and vectors
A **scalar** has only size. Examples: mass, speed, distance, time, work, energy, power and temperature.

A **vector** has size and direction. Examples: displacement, velocity, acceleration, force, momentum and weight.

> **Tip:** Ask if "towards the north" makes sense with the quantity. If it does, the quantity is a vector.

### Quick conversions
1. **km/h to m/s:** multiply by $\dfrac{5}{18}$. So 36 km/h is 10 m/s. Reverse it (m/s to km/h) by multiplying by $\dfrac{18}{5}$.
2. **Electricity units:** units (kWh) = watts × hours ÷ 1000. A 100 W bulb used for 10 hours uses 1 unit.

The reason is simple. 1 km is 1000 m and 1 hour is 3600 s. So 1 km/h is $\dfrac{1000}{3600} = \dfrac{5}{18}$ m/s.

> **Rule:** One "unit" on your electricity bill is 1 kWh = 1000 W × 3600 s = 3.6 × 10⁶ J. It is energy, not power.

### Instruments and what they measure
Most names carry a Greek root that gives the job away.

| Instrument | Measures |
|---|---|
| Barometer | Atmospheric pressure |
| Manometer | Pressure of gases |
| Hygrometer | Relative humidity |
| Hydrometer | Relative density of liquids |
| Lactometer | Purity (density) of milk |
| Anemometer | Wind speed |
| Altimeter | Altitude (aircraft) |
| Ammeter | Current (connect in series) |
| Voltmeter | Potential difference (connect in parallel) |
| Galvanometer | Detects small currents |
| Seismograph | Earthquake waves |
| Sphygmomanometer | Blood pressure |
| Pyrometer | Very high temperature (furnaces) |
| Fathometer or SONAR | Depth of the sea (echo sounding) |
| Odometer / Speedometer | Distance run / speed of a vehicle |
| Tachometer | Rotation speed (rpm) |
| Audiometer | Hearing |
| Crescograph | Growth of plants |
""",
    tricks=[
        trick("Base units in one line",
              "Say it as **M**etre, **K**ilogram, **S**econd, **A**mpere, **K**elvin, **M**ole, **C**andela. Anything not on this list is derived.",
              "Which of these is NOT an SI base unit: kelvin, candela, newton, mole?",
              ["List the seven base units: m, kg, s, A, K, mol, cd.", "Kelvin, candela and mole are on the list.", "Newton is not on the list."],
              "Newton. It is derived: kg·m/s²."),
        trick("Read the root of the instrument name",
              "**Hygro** is humidity. **Hydro** is liquid density. **Lacto** is milk. **Anemo** is wind. **Sphygmo** is pulse and blood pressure. **Pyro** is fire, so high temperature. **Seismo** is earthquake."),
    ],
    mistakes=[
        mis("Treating the light year as a unit of time.", "A light year is a distance: about 9.46 × 10¹⁵ m."),
        mis("Calling kWh a unit of power.", "kWh is energy. Power is measured in watt."),
        mis("Mixing up the hygrometer and the hydrometer.", "Hygro means humidity. Hydro means liquid density."),
        mis("Writing the unit of temperature as \"degree kelvin\".", "Say kelvin, symbol K."),
        mis("Calling momentum, velocity or density base quantities.", "Only seven are base. These are derived from them."),
    ],
    revision=[
        "The 7 base units are m, kg, s, A, K, mol and cd.",
        "Light year, parsec and AU are distances. Nautical mile is 1852 m. A knot is one nautical mile per hour.",
        "1 kWh = 3.6 × 10⁶ J and it is energy. 1 horsepower is about 746 W.",
        "km/h × 5/18 = m/s.",
        "Scalars: speed, work, energy, power. Vectors: velocity, force, momentum, displacement.",
        "Hygro is humidity, hydro is liquid density, lacto is milk, anemo is wind, sphygmo is blood pressure.",
    ],
    patterns=[
        pat("ga-un-p1", "SI unit of a physical quantity", "very common",
            "The question says 'The SI unit of pressure / charge / magnetic flux / power is ...' or 'which pair is wrongly matched'.",
            ["Decide if the quantity is one of the 7 base quantities.",
             "If it is derived, recall its named unit: N, J, W, Pa, Hz, C, V, Ω, F, Wb, T, H.",
             "If it has no named unit, build it from base units (momentum is kg·m/s)."],
            "Every unit is fixed by international agreement, so recall plus elimination is the method.",
            "The SI unit of magnetic field (magnetic flux density) is:",
            ["Weber is the unit of magnetic flux.", "Magnetic field is flux per square metre.", "That unit is the tesla."],
            "Tesla (T)"),
        pat("ga-un-p2", "Instrument and what it measures", "very common",
            "An instrument name ending in '-meter' or '-graph' is given and its use is asked, or the reverse.",
            ["Break the name into its root: hygro, hydro, anemo, baro, seismo, sphygmo.",
             "Pick the option that fits the root.",
             "Watch the pairs: hygrometer and hydrometer, manometer and sphygmomanometer."],
            "Most names are Greek roots that describe the job.",
            "An altimeter is used to measure:",
            ["Alti means height.", "It works like a barometer.", "Pressure falls as height rises."],
            "Altitude, mainly in aircraft"),
        pat("ga-un-p3", "Practical and astronomical units", "common",
            "Units like light year, parsec, AU, knot, nautical mile, fathom, horsepower, carat or kWh appear in 'is a unit of ...' or 'equals ...'.",
            ["Sort the unit by quantity: light year, parsec, AU, fathom and nautical mile are distance.",
             "Knot is speed. kWh, calorie and eV are energy. Horsepower is power.",
             "Recall the value: 1852 m, 746 W, 3.6 × 10⁶ J."],
            "The words 'year' and 'hour' in a unit name mislead students. The quantity decides.",
            "A parsec is a unit of:",
            ["It is used for star distances.", "1 parsec is about 3.26 light years.", "So it measures distance."],
            "Distance"),
        pat("ga-un-p4", "Base or derived unit; scalar or vector", "common",
            "The question says 'Which is NOT a fundamental unit', 'which is a vector' or 'which pair are both scalars'.",
            ["Base units: metre, kilogram, second, ampere, kelvin, mole, candela. All else is derived.",
             "Vector test: does direction change the meaning?",
             "Speed, distance, mass, work, energy, power and time are scalars."],
            "A scalar has only size. A vector needs a direction too.",
            "Which of the following is a scalar quantity? (a) Force (b) Momentum (c) Work (d) Displacement",
            ["Force needs a direction.", "Momentum and displacement need a direction.", "Work has only size."],
            "(c) Work"),
        pat("ga-un-p5", "Unit conversion and energy-bill numericals", "common",
            "A speed in km/h must be converted, or appliance watts and hours must become kWh.",
            ["For speed, multiply km/h by 5/18 to get m/s.",
             "For bills, use watts × hours ÷ 1000 to get units.",
             "Multiply units by the rate to get rupees.",
             "Check the size: a 1 kW appliance for 1 hour is exactly 1 unit."],
            "1 km = 1000 m and 1 h = 3600 s, so 1000/3600 = 5/18.",
            "Convert 54 km/h to m/s.",
            [r"Multiply by $\dfrac{5}{18}$.", r"$54 \times \dfrac{5}{18} = 15$."],
            "15 m/s",
            formula=r"1\ \text{km/h}=\tfrac{5}{18}\ \text{m/s},\quad \text{units (kWh)}=\frac{\text{W}\times\text{h}}{1000}"),
    ],
)
FNOTES["ph-units"] = {"Horsepower": "power unit", "Kilowatt-hour": "1 'unit' of electricity, a unit of energy",
                      "Light year": "a unit of distance"}

# =====================================================================
S["ph-mechanics"] = dict(
    concept=(
        "Motion, force, gravity, energy, fluids and levers make up this subtopic. "
        "Exams ask which law or principle explains an everyday event. "
        "Learn each law with one example, plus the key numbers for gravity and energy."
    ),
    notes=r"""### Motion in simple words
A body is in motion when its position changes with time.

- **Distance** is the total path covered. It is a scalar.
- **Displacement** is the straight-line gap from start to end, with direction. It is a vector.
- **Speed** is distance ÷ time. **Velocity** is displacement ÷ time.
- **Acceleration** is the rate of change of velocity. Its unit is m/s².

Walk once round a circular park. The distance is large but the displacement is zero.

### Newton's three laws
| Law | Statement | Everyday example |
|---|---|---|
| First (inertia) | A body stays at rest or in uniform motion unless an outside force acts. | Passengers jerk forward when a bus brakes. Dust leaves a beaten carpet. |
| Second | Force = mass × acceleration, $F = ma$. It is also the rate of change of momentum. | A cricketer pulls his hands back while catching. |
| Third | Every action has an equal and opposite reaction. | Rocket, gun recoil, swimming, walking. |

**Momentum** is $p = mv$. It stays constant when no outside force acts. That is why a gun recoils when it fires.

More on the first law: mass measures inertia. Passengers fall forward when a moving bus brakes (inertia of motion). They fall backward when a stopped bus starts suddenly (inertia of rest).

> **Tip:** Pulling the hands back while catching a ball increases the time of impact. So the force on the hands is smaller. Cars use air bags and crumple zones for the same reason.

### Gravitation
Every two masses attract each other. Newton's law is $F = \dfrac{Gm_1m_2}{r^2}$, with $G = 6.67 \times 10^{-11}$ N m² kg⁻². Near the Earth this pull gives $g = 9.8$ m/s².

- g is greatest at the poles and least at the equator.
- g falls with height and with depth. It is zero at the Earth's centre.
- **Mass** never changes. **Weight** is $mg$ and changes with place.
- On the Moon, weight is about $\dfrac{1}{6}$ of the Earth value. A 60 kg person still has a mass of 60 kg.
- Escape velocity from Earth is about 11.2 km/s. Orbital velocity near the surface is about 7.9 km/s.
- A geostationary satellite orbits about 36,000 km above the equator with a period of 24 hours.
- Astronauts in orbit feel weightless because they are in free fall with the spacecraft.

> **Watch:** Mass is in kilogram and stays fixed. Weight is in newton and changes.

### Work, energy and power
**Work** is $W = Fs\cos\theta$. It is zero if there is no displacement or if the force is at right angles to the motion. A satellite in circular orbit is an example of zero work.

- **Kinetic energy** is $\tfrac{1}{2}mv^2$. Double the speed and KE becomes 4 times.
- **Potential energy** is $mgh$.
- **Power** is work ÷ time. Its unit is the watt.

Energy only changes form. A falling stone turns PE into KE.

| Device | Energy change |
|---|---|
| Electric motor | Electrical to mechanical |
| Dynamo or generator | Mechanical to electrical |
| Battery | Chemical to electrical |
| Solar cell | Light to electrical |
| Microphone | Sound to electrical |
| Loudspeaker | Electrical to sound |

### Fluids
Pressure is force ÷ area. A knife is sharp because a small area gives high pressure.

| Principle | Idea | Use |
|---|---|---|
| Pascal's law | Pressure on an enclosed liquid spreads equally | Hydraulic lift, brakes, press |
| Archimedes' principle | Upthrust = weight of liquid displaced | Ships, hydrometer, lactometer, submarines |
| Bernoulli's principle | Faster flow means lower pressure | Aeroplane lift, roofs blown off, atomiser |
| Surface tension | The surface acts like a stretched skin | Round drops, insects on water |
| Capillarity | Liquid rises in thin tubes | Lamp wick, blotting paper, plant xylem |
| Viscosity | Internal friction of a fluid | Honey flows slowly |

Ice floats because its density (about 0.92 g/cm³) is less than water's. A body floats if its density is less than the liquid's. A ship floats because its shape displaces a lot of water. Soap and kerosene lower surface tension. Kerosene on ponds kills mosquito larvae. Liquid viscosity falls when heated.

### Levers
A lever has a **fulcrum**, a **load** and an **effort**. The class depends on which one sits in the middle.

| Class | In the middle | Examples |
|---|---|---|
| Class 1 | Fulcrum | Seesaw, scissors, pliers, crowbar, beam balance |
| Class 2 | Load | Nutcracker, wheelbarrow, bottle opener, lemon squeezer |
| Class 3 | Effort | Tongs, forceps, tweezers, fishing rod, human forearm, broom |

> **Rule:** Fulcrum, Load, Effort in the middle gives class 1, 2, 3. Class 2 always gives mechanical advantage. Class 3 gives speed and control.
""",
    tricks=[
        trick("Lever class from the middle item",
              "Whatever sits in the middle decides the class. **F** is 1, **L** is 2, **E** is 3.",
              "A wheelbarrow is which class of lever?",
              ["The wheel is the fulcrum, at one end.", "The handles are the effort, at the other end.", "The load sits in the middle."],
              "Class 2"),
        trick("Squares in energy",
              "KE depends on $v^2$. Double the speed and KE is 4 times. Triple it and KE is 9 times. Momentum only doubles when speed doubles."),
    ],
    mistakes=[
        mis("Saying mass changes on the Moon.", "Mass stays the same. Only weight becomes about one-sixth."),
        mis("Thinking g is greatest at the equator.", "g is greatest at the poles and least at the equator."),
        mis("Explaining rocket motion with the first law.", "It is the third law (action and reaction)."),
        mis("Saying work is done by holding a heavy box still.", "There is no displacement, so the work is zero."),
        mis("Placing tongs in class 2 because they hold a load.", "The effort is in the middle, so they are class 3."),
    ],
    revision=[
        "Inertia measures mass. F = ma. Action equals reaction (rocket, recoil).",
        "g is maximum at the poles, minimum at the equator and zero at the centre. Moon weight is about 1/6.",
        "Escape velocity is 11.2 km/s. A geostationary satellite has a period of 24 h.",
        "KE ∝ v². Work is zero if there is no displacement or the force is perpendicular to motion.",
        "Pascal gives hydraulics. Archimedes gives floating. Bernoulli gives aeroplane lift.",
        "Lever middle: fulcrum, load, effort gives class 1, 2, 3.",
    ],
    patterns=[
        pat("ga-me-p1", "Everyday event and Newton's law", "very common",
            "A daily-life story (bus braking, rocket, gun recoil, cricketer catching, carpet beating) with the laws as options.",
            ["If a body resists a change in rest or motion, choose the first law.",
             "If force is reduced by taking more time, or the question uses F = ma, choose the second law.",
             "If you push one way and move the other way (rocket, recoil, swimming), choose the third law."],
            "Each law explains one kind of effect, and the story tells you which.",
            "When a carpet is beaten with a stick, the dust comes out. This is due to:",
            ["The carpet moves suddenly.", "The dust tends to stay at rest.", "That is inertia of rest."],
            "Inertia of rest (Newton's first law)"),
        pat("ga-me-p2", "Gravitation, weight and satellites", "very common",
            "The question asks about g at poles, equator or centre, weight on the Moon, escape velocity, geostationary orbit or weightlessness.",
            ["Mass is fixed. Weight changes with g.",
             "g is larger at the poles than at the equator. It falls up and down, and is zero at the centre.",
             "Recall the numbers: g 9.8 m/s², escape velocity 11.2 km/s, geostationary period 24 h at about 36,000 km."],
            "Weight is mass times g, so only g changes from place to place.",
            "A body has a mass of 30 kg on Earth. What is its mass on the Moon?",
            ["Mass does not depend on place.", "Only the weight falls to about one-sixth."],
            "30 kg",
            formula=r"W = mg,\quad g_{moon}\approx \tfrac{1}{6}g_{earth}"),
        pat("ga-me-p3", "Fluid principle and its use", "very common",
            "A device or effect (hydraulic brake, floating ship, aeroplane lift, lamp wick, round raindrop) with principles as options.",
            ["Enclosed liquid and multiplied force point to Pascal.",
             "Floating, sinking or upthrust points to Archimedes.",
             "Fast air and low pressure point to Bernoulli.",
             "A skin-like surface points to surface tension. Rise in thin tubes points to capillarity."],
            "Each principle has a small set of classic examples.",
            "The roof of a hut is blown off in a storm. Which principle explains this?",
            ["Fast wind moves over the roof.", "Fast flow means low pressure above.", "Higher pressure inside pushes the roof up."],
            "Bernoulli's principle"),
        pat("ga-me-p4", "Class of a lever", "common",
            "A tool (scissors, nutcracker, forceps, wheelbarrow, human arm) is given and 'lever of class ...' is asked.",
            ["Find the fulcrum, load and effort on the tool.",
             "See which one is in the middle.",
             "Fulcrum gives class 1, load gives class 2, effort gives class 3."],
            "The position of the middle item fixes the class.",
            "A bottle opener is a lever of which class?",
            ["The fulcrum is the edge on the cap top.", "Your hand gives the effort at the far end.", "The cap (load) is between them."],
            "Class 2"),
        pat("ga-me-p5", "Work, energy and power basics", "common",
            "The question says 'If velocity is doubled, KE becomes ...', 'work done when ...', or asks a small power sum.",
            [r"KE depends on $v^2$. A speed multiplied by k gives KE multiplied by $k^2$.",
             "Work is F × s × cos θ. It is zero if s = 0 or the force is perpendicular to motion.",
             "Power is work ÷ time. For lifting, work is mgh."],
            "The square in KE makes energy grow faster than speed.",
            "A body's velocity is made three times. Its kinetic energy becomes:",
            [r"KE $\propto v^2$.", "3² = 9."],
            "9 times",
            formula=r"KE=\tfrac12 mv^2,\quad PE=mgh,\quad P=\frac{W}{t}"),
    ],
)
FNOTES["ph-mechanics"] = {"First equation of motion": "v is final speed, u is initial speed, a is acceleration, t is time",
                          "Second equation of motion": "s is the distance covered",
                          "Third equation of motion": "no time needed",
                          "Kinetic and potential energy": "m is mass, v is speed, h is height",
                          "Pressure": "h is depth, ρ is density"}
