# -*- coding: utf-8 -*-
"""Builds content/ssc-cgl/topics/ga/physics.json. Run: py -3 build_physics.py"""
from scicommon import Q, save_topic, place

C_UNITS = """### The 7 SI base quantities
| Quantity | SI unit | Symbol |
|---|---|---|
| Length | metre | m |
| Mass | kilogram | kg |
| Time | second | s |
| Electric current | **ampere** | A |
| Thermodynamic temperature | **kelvin** | K |
| Amount of substance | **mole** | mol |
| Luminous intensity | **candela** | cd |

### Derived units asked again and again
| Quantity | Unit | Quantity | Unit |
|---|---|---|---|
| Force | **newton** (N) | Electric charge | **coulomb** (C) |
| Work / energy / heat | **joule** (J) | Potential difference | **volt** (V) |
| Power | **watt** (W) | Resistance | **ohm** (Ω) |
| Pressure | **pascal** (Pa) | Capacitance | **farad** (F) |
| Frequency | **hertz** (Hz) | Inductance | **henry** (H) |
| Magnetic field | **tesla** (T) | Magnetic flux | **weber** (Wb) |
| Power of a lens | **dioptre** (D) | Radioactivity | **becquerel** (Bq) |
| Luminous flux | lumen | Illuminance | **lux** |
| Sound level | **decibel** (dB) | Speed of ships | **knot** (nautical mile per hour) |

### Special units and conversions
| Unit | Measures | Value |
|---|---|---|
| **Light year** | **Distance** (not time) | about 9.46 × 10¹⁵ m |
| Parsec | Distance | about 3.26 light years |
| Astronomical unit | Distance | Mean Earth–Sun distance, about 1.5 × 10¹¹ m |
| Ångström | Length (wavelength) | 10⁻¹⁰ m |
| Fermi | Nuclear size | 10⁻¹⁵ m |
| Nautical mile | Distance at sea | 1,852 m |
| Horsepower | Power | about 746 W |
| Kilowatt-hour ('unit') | **Electrical energy** | 3.6 × 10⁶ J |
| Calorie | Heat | about 4.18 J |
| Atmosphere | Pressure | about 1.013 × 10⁵ Pa |

### Instruments
| Instrument | Measures / use |
|---|---|
| **Barometer** | Atmospheric pressure (Torricelli) |
| **Hygrometer** | Relative **humidity** |
| **Hydrometer** | Relative density of liquids |
| **Lactometer** | Purity (density) of **milk** |
| **Anemometer** | **Wind speed** |
| **Altimeter** | Altitude (aircraft) |
| **Ammeter / Voltmeter** | Current (in series) / potential difference (in parallel) |
| **Galvanometer** | Detects small currents |
| **Seismograph** | Earthquake waves |
| **Sphygmomanometer** | **Blood pressure** |
| **Pyrometer** | Very high temperatures (furnaces) |
| **Fathometer** | Ocean depth (echo sounding) |
| **Odometer / Speedometer** | Distance covered / speed of a vehicle |
| **Tachometer** | Rotation speed (rpm) |
| **Manometer** | Pressure of gases |
| **Audiometer** | Hearing |
"""

C_MECH = """### Newton's laws of motion
| Law | Statement | Everyday examples |
|---|---|---|
| **First (inertia)** | A body stays at rest or in uniform motion unless an external force acts | Passengers jerk forward when a bus brakes; dust leaves a beaten carpet |
| **Second** | Force = rate of change of momentum, **F = ma** | Catching a fast ball by pulling hands back (more time, less force) |
| **Third** | Every action has an equal and opposite reaction | **Rocket** propulsion, **recoil of a gun**, swimming, walking |

**Momentum** p = mv is conserved when no external force acts.

### Gravitation
- Universal law: F = G m₁m₂ / r² (**Newton**); G = 6.67 × 10⁻¹¹ N m² kg⁻².
- **g = 9.8 m/s²** on Earth's surface; it is **maximum at the poles, minimum at the equator**, and decreases with height and depth (zero at the centre).
- **Mass** stays the same everywhere; **weight** (mg) changes. On the Moon weight is about **1/6** of that on Earth.
- **Escape velocity** from Earth is about **11.2 km/s**; orbital velocity near the surface is about **7.9 km/s**.
- A **geostationary** satellite orbits about 36,000 km above the equator with a period of **24 hours**.
- Astronauts in orbit feel **weightless** because they are in free fall with the spacecraft.

### Work, energy and power
- Work W = F s cos θ; zero when force ⊥ displacement (e.g. a satellite in circular orbit).
- Kinetic energy = ½mv² (doubling speed → **4 times** KE); potential energy = mgh.
- Energy conversions: **electric motor** electrical → mechanical; **dynamo/generator** mechanical → electrical; **battery** chemical → electrical; **solar cell** light → electrical; **microphone** sound → electrical; **loudspeaker** electrical → sound.

### Fluids
- **Pressure** = force/area. Sharp knives and narrow nails work because small area → high pressure.
- **Pascal's law** — pressure applied to an enclosed liquid is transmitted equally: **hydraulic lift, hydraulic brakes, hydraulic press**.
- **Archimedes' principle** — upthrust = weight of liquid displaced; ships float, ice floats (density ~0.92 g/cm³). A body floats if its density is less than the liquid's.
- **Bernoulli's principle** — faster flow → lower pressure: **aeroplane lift**, roofs blown off in storms, atomisers.
- **Surface tension** — liquid drops are **spherical**; insects walk on water; soap and kerosene lower it (kerosene on ponds kills mosquito larvae).
- **Capillarity** — rise of oil in a lamp **wick**, ink in blotting paper, water in plant xylem.

### Simple machines — levers
| Class | Arrangement | Examples |
|---|---|---|
| **Class 1** | **Fulcrum** in the middle | Seesaw, scissors, pliers, crowbar, beam balance |
| **Class 2** | **Load** in the middle | **Nutcracker**, wheelbarrow, bottle opener |
| **Class 3** | **Effort** in the middle | **Tongs, tweezers**, fishing rod, human forearm |
"""

C_HEAT_SOUND = """### Temperature and heat
- Scales: C/100 = (F − 32)/180 = (K − 273)/100. **−40° is the same on Celsius and Fahrenheit.**
- Normal body temperature **37 °C = 98.6 °F = 310 K**. **Absolute zero = 0 K = −273.15 °C**.
- Water boils at 100 °C at sea level; boiling point **falls at high altitude** (lower pressure) — a **pressure cooker** raises pressure and hence boiling point.
- Water has a **high specific heat** → coastal areas have moderate climate; used as a coolant.
- **Latent heat**: burns from **steam** are worse than from boiling water because steam gives out extra latent heat of vaporisation on condensing.
- **Anomalous expansion**: water is **densest at 4 °C**, so lakes freeze from the top and aquatic life survives below.
- **Evaporation causes cooling** — earthen pots (matka), sweating.
- Heat transfer: **conduction** (solids), **convection** (fluids — sea breeze by day, land breeze by night), **radiation** (no medium needed — Sun's heat). A **thermos flask** cuts all three.
- Dark, rough surfaces are good absorbers and good emitters; light, shiny surfaces reflect heat (white clothes in summer).

### Sound
- Sound is a **mechanical, longitudinal** wave in air — it **needs a medium** and cannot travel in a vacuum.
- Speed: **solids > liquids > gases**. In air about **332 m/s at 0 °C** and about **343 m/s at 20 °C**; it rises with **temperature** and **humidity**, but does not depend on pressure.
- Human audible range **20 Hz – 20,000 Hz**. **Infrasonic** < 20 Hz (earthquakes, elephants, whales). **Ultrasonic** > 20 kHz (**bats**, dolphins, **SONAR**, ultrasound scanning).
- **Pitch** depends on **frequency** (women's and children's voices have higher pitch); **loudness** on **amplitude**; **quality/timbre** on the waveform.
- **Echo** needs a gap of about 0.1 s → reflecting surface at least about **17 m** away.
- **Doppler effect** — apparent change in frequency when source and listener move relative to each other (siren pitch rises as it approaches; speed radars).
- **Mach number** = object speed ÷ speed of sound; > 1 is **supersonic** (causes a sonic boom).
- **Resonance** — soldiers break step while crossing a bridge.
"""

C_LIGHT = """### Basics
- Speed of light in vacuum **c ≈ 3 × 10⁸ m/s**; slower in water and glass. Refractive index n = c / v.
- **Diamond** has a very high refractive index (about 2.42) → small critical angle → **sparkles** by total internal reflection.

### Mirrors
| Mirror | Image nature | Uses |
|---|---|---|
| **Plane** | Virtual, erect, same size, **laterally inverted** | Looking glass, periscope |
| **Concave** (converging) | Real/inverted or virtual/enlarged | **Shaving/make-up mirror, dentist's mirror, torch & headlight reflector**, solar furnace |
| **Convex** (diverging) | Always **virtual, erect, diminished**; wide field of view | **Rear-view mirror** of vehicles, street corners |

### Lenses and the eye
| Defect | Cause | Correction |
|---|---|---|
| **Myopia** (short-sightedness) | Image forms **in front of** retina | **Concave** lens |
| **Hypermetropia** (long-sightedness) | Image forms **behind** retina | **Convex** lens |
| **Presbyopia** | Ageing, weak ciliary muscles | **Bifocal** lens |
| **Astigmatism** | Uneven cornea curvature | **Cylindrical** lens |

- **Power** P = 1/f (f in metres), unit **dioptre**; convex lens +, concave lens −.
- Normal eye: near point **25 cm**, far point infinity. **Rods** — dim light; **cones** — colour. Image on the retina is real and inverted.
- **Persistence of vision** (about 1/16 s) makes cinema possible.

### Refraction phenomena
- A pencil looks bent in water; a pool looks **shallower** than it is.
- **Twinkling of stars** — atmospheric refraction (planets do not twinkle much as they are nearer, extended sources).
- Sun is visible about **2 minutes before** actual sunrise and after actual sunset.
- **Total internal reflection**: **optical fibres**, **mirage**, sparkle of diamond. Needs light going from denser to rarer medium beyond the critical angle.

### Dispersion and scattering
- White light splits into **VIBGYOR** through a prism (**Newton**); **violet deviates most, red least**. A **rainbow** forms by refraction, dispersion and internal reflection in raindrops and is seen **opposite the Sun**.
- **Scattering** is stronger for shorter wavelengths (Rayleigh) → the **sky is blue**; the Sun looks **red at sunrise/sunset** (long path); **danger signals are red** (least scattered, seen from far). The sky looks **black** to astronauts in space (no atmosphere to scatter).
- **Raman effect** — **C.V. Raman**, discovered 28 Feb 1928 (**National Science Day**), Nobel Prize **1930**.
- Primary colours of light: **Red, Green, Blue**; R + G = yellow, G + B = cyan, R + B = magenta; all three = white.
"""

C_ELEC = """### Current electricity
- Current I = Q/t (ampere); potential difference in volt; resistance in ohm.
- **Ohm's law**: **V = IR** (at constant temperature).
- Resistance R = ρL/A — doubles with length, falls with thicker wire; depends on material and temperature.
- **Series**: R = R₁ + R₂ + … (same current). **Parallel**: 1/R = 1/R₁ + 1/R₂ + … (same voltage). **Household appliances are connected in parallel** so each gets full voltage and works independently.
- Power **P = VI = I²R = V²/R**. Commercial energy unit = **kWh** (1 unit).
- **Joule's heating** H = I²Rt → heater, iron, filament bulb. Filament is **tungsten** (very high melting point); heating coils are **nichrome** (high resistivity). A **fuse** wire has a **low melting point** (tin–lead alloy) and is connected in series with the live wire.
- Indian domestic supply: **AC, 220–230 V, 50 Hz**. Wire colours: live — red/brown, neutral — black/blue, earth — green.

### Magnetism and electromagnetism
- **Oersted** (1820): a current produces a magnetic field.
- **Faraday**: electromagnetic induction (1831) — basis of the **generator/dynamo** and **transformer**.
- **Fleming's left-hand rule → motor**; **right-hand rule → generator**.
- **Transformer** works only on **AC**; step-up for long-distance transmission (reduces current and I²R loss), step-down near homes.
- A galvanometer becomes an **ammeter** with a low resistance **shunt in parallel**, and a **voltmeter** with a high resistance in **series**.
- **Rectifier (diode)** converts AC → DC; **inverter** converts DC → AC. The **transistor** (1947, Bell Labs) amplifies and switches.
- Semiconductors: **silicon, germanium**. Doping with **pentavalent** (phosphorus, arsenic) → **n-type**; **trivalent** (boron, gallium) → **p-type**.

### Electromagnetic spectrum (increasing wavelength)
**Gamma rays → X-rays → Ultraviolet → Visible → Infrared → Microwaves → Radio waves.**

| Wave | Use |
|---|---|
| Gamma | Cancer treatment, sterilising |
| X-ray | Bone imaging, airport scanners |
| UV | Sterilisation, vitamin D in skin |
| Infrared | **TV remotes**, night vision, heating |
| Microwave | **Microwave ovens, radar**, satellite links |
| Radio | Broadcasting, mobile communication |
"""

C_MODERN = """### Nuclear physics
- **Radioactivity** discovered by **Henri Becquerel** (1896); **Marie and Pierre Curie** discovered **polonium and radium**.
- **Alpha** (helium nucleus) — least penetrating; **beta** (electrons); **gamma** (EM waves) — most penetrating.
- **Carbon-14 dating** (W.F. Libby) estimates the age of fossils and ancient organic remains.
- **Nuclear fission** — a heavy nucleus (e.g. **U-235**) splits on neutron capture → **atom bomb**, **nuclear power reactors**. **Nuclear fusion** — light nuclei (hydrogen isotopes) join → **energy of the Sun and stars**, hydrogen bomb.
- Mass–energy equivalence **E = mc²** (**Einstein**).
- In a reactor: **moderator** slows neutrons (**heavy water**, graphite); **control rods** absorb neutrons (**cadmium, boron**); coolant (water, liquid sodium).
- India: **Apsara** (1956, Trombay) — first research reactor in Asia; **Tarapur** (1969) — first nuclear power station. **Homi J. Bhabha** — father of India's nuclear programme; **Vikram Sarabhai** — father of India's space programme.

### Inventions and discoveries
| Invention / discovery | Person |
|---|---|
| Laws of motion, gravitation | **Isaac Newton** |
| Telescope (astronomical use), thermometer (thermoscope) | **Galileo Galilei** |
| Barometer | **Evangelista Torricelli** |
| Improved steam engine | **James Watt** |
| Electromagnetic induction, dynamo | **Michael Faraday** |
| Telephone | **Alexander Graham Bell** |
| Electric bulb, phonograph | **Thomas Edison** |
| Radio (wireless telegraphy) | **Guglielmo Marconi** (J.C. Bose did pioneering microwave work) |
| Television | **John Logie Baird** |
| X-rays | **Wilhelm Röntgen** (first Physics Nobel, 1901) |
| Electron | **J.J. Thomson** |
| Nucleus (gold-foil experiment) | **Ernest Rutherford** |
| Neutron | **James Chadwick** (1932) |
| Theory of relativity, photoelectric effect | **Albert Einstein** (Nobel 1921 for the photoelectric effect) |
| Aeroplane (1903) | **Wright brothers** |
| Laser (1960) | **Theodore Maiman** |
| Dynamite | **Alfred Nobel** |
| Crescograph (plant growth) | **J.C. Bose** |
| Raman effect | **C.V. Raman** (Nobel 1930) |
| Chandrasekhar limit | **S. Chandrasekhar** (Nobel 1983) |
| Bose–Einstein statistics ('boson') | **Satyendra Nath Bose** |
"""

SUBTOPICS = [
    {
        "id": "ph-units",
        "title": "SI units, conversions and measuring instruments",
        "concept": C_UNITS,
        "formulas": [
            {"name": "Kilowatt-hour", "tex": r"1\ \text{kWh} = 3.6 \times 10^{6}\ \text{J}", "note": "1 'unit' of electricity"},
            {"name": "Horsepower", "tex": r"1\ \text{hp} \approx 746\ \text{W}", "note": ""},
            {"name": "Light year", "tex": r"1\ \text{ly} \approx 9.46 \times 10^{15}\ \text{m}", "note": "a unit of distance"},
        ],
        "tricks": [
            {
                "title": "Base-unit roll call: 'Mighty Kings Seldom Answer Kind Monks Correctly'",
                "body": "**M**etre, **K**ilogram, **S**econd, **A**mpere, **K**elvin, **M**ole, **C**andela — the 7 SI base units. Anything else (newton, joule, volt, watt…) is **derived**.",
                "example": {"q": "Which of these is NOT an SI base unit: kelvin, candela, newton, mole?", "solution": "Newton — it is derived (kg m s⁻²)."},
            },
            {
                "title": "'Meter' by what it measures",
                "body": "**Hygro** = humidity (hygiene/water), **Hydro** = liquid density, **Lacto** = milk, **Anemo** = wind (Greek *anemos*), **Sphygmo** = pulse/BP, **Pyro** = fire/high temperature, **Seismo** = earthquake, **Alti** = altitude.",
                "example": None,
            },
        ],
        "mistakes": [
            "Treating the light year as a unit of time — it is a distance.",
            "Using kWh as a unit of power — it is a unit of energy.",
            "Confusing hygrometer (humidity) with hydrometer (liquid density).",
        ],
    },
    {
        "id": "ph-mechanics",
        "title": "Motion, gravitation, work-energy, fluids and levers",
        "concept": C_MECH,
        "formulas": [
            {"name": "First equation of motion", "tex": r"v = u + at", "note": ""},
            {"name": "Second equation of motion", "tex": r"s = ut + \tfrac{1}{2}at^{2}", "note": ""},
            {"name": "Third equation of motion", "tex": r"v^{2} = u^{2} + 2as", "note": ""},
            {"name": "Newton's second law", "tex": r"F = ma = \frac{\Delta p}{\Delta t}", "note": "p = mv"},
            {"name": "Law of gravitation", "tex": r"F = \frac{G m_1 m_2}{r^{2}}", "note": "G = 6.67 × 10⁻¹¹ N m² kg⁻²"},
            {"name": "Kinetic and potential energy", "tex": r"KE = \tfrac{1}{2}mv^{2},\quad PE = mgh", "note": ""},
            {"name": "Work and power", "tex": r"W = Fs\cos\theta,\quad P = \frac{W}{t}", "note": "1 W = 1 J/s"},
            {"name": "Pressure", "tex": r"P = \frac{F}{A},\quad P_{\text{liquid}} = h\rho g", "note": "unit pascal"},
        ],
        "tricks": [
            {
                "title": "Lever class by the middle item: 'FLE = 1-2-3'",
                "body": "Whatever sits in the **middle** decides the class: **F**ulcrum → 1, **L**oad → 2, **E**ffort → 3. Nutcracker has the load (nut) in the middle → class 2; tongs are squeezed in the middle → class 3.",
                "example": {"q": "A wheelbarrow is which class of lever?", "solution": "Class 2 — the load lies between the wheel (fulcrum) and the handles (effort)."},
            },
            {
                "title": "Squares in energy",
                "body": "KE ∝ v²: double the speed → 4× KE; triple → 9×. Momentum ∝ v: double speed → 2× momentum.",
                "example": None,
            },
        ],
        "mistakes": [
            "Saying mass changes on the Moon — only weight changes.",
            "Believing g is greatest at the equator — it is greatest at the poles.",
            "Attributing rocket motion to the first law — it is the third law (action–reaction).",
        ],
    },
    {
        "id": "ph-heat-sound",
        "title": "Heat, temperature and sound",
        "concept": C_HEAT_SOUND,
        "formulas": [
            {"name": "Temperature scales", "tex": r"\frac{C}{100} = \frac{F-32}{180} = \frac{K-273}{100}", "note": "−40 °C = −40 °F"},
            {"name": "Heat absorbed", "tex": r"Q = mc\,\Delta T", "note": "c = specific heat"},
            {"name": "Latent heat", "tex": r"Q = mL", "note": "no temperature change during phase change"},
            {"name": "Wave speed", "tex": r"v = f\lambda", "note": "speed = frequency × wavelength"},
            {"name": "Echo distance", "tex": r"d = \frac{v\,t}{2}", "note": "sound travels to the wall and back"},
        ],
        "tricks": [
            {
                "title": "Sound speed order: 'Steel Shouts, Water Whispers, Air Awaits'",
                "body": "Solids fastest, liquids next, gases slowest; vacuum — no sound at all (astronauts use radio).",
                "example": None,
            },
            {
                "title": "Pitch–frequency, Loudness–amplitude",
                "body": "'**P**itch = **F**requency' (PF like 'Provident Fund'), '**L**oudness = **A**mplitude' (LA like 'Los Angeles').",
                "example": {"q": "The pitch of a sound depends on its?", "solution": "Frequency."},
            },
        ],
        "mistakes": [
            "Thinking sound speed rises with pressure — it rises with temperature and humidity, not pressure.",
            "Calling bats' sounds infrasonic — they are ultrasonic.",
            "Saying boiling point rises at hill stations — it falls because air pressure is lower.",
        ],
    },
    {
        "id": "ph-light",
        "title": "Light — mirrors, lenses, eye, dispersion and scattering",
        "concept": C_LIGHT,
        "formulas": [
            {"name": "Power of a lens", "tex": r"P = \frac{1}{f\,(\text{m})} = \frac{100}{f\,(\text{cm})}", "note": "unit dioptre"},
            {"name": "Lens formula", "tex": r"\frac{1}{f} = \frac{1}{v} - \frac{1}{u}", "note": "Cartesian sign convention"},
            {"name": "Mirror formula", "tex": r"\frac{1}{f} = \frac{1}{v} + \frac{1}{u}", "note": "f = R/2"},
            {"name": "Refractive index", "tex": r"n = \frac{c}{v}", "note": "c = 3 × 10⁸ m/s"},
        ],
        "tricks": [
            {
                "title": "Eye defect lens: 'My-Con, Hyper-Vex'",
                "body": "**My**opia → **Con**cave; **Hyper**metropia → con**vex**. Short-sighted people cannot see far — a diverging lens pushes the image back onto the retina.",
                "example": {"q": "A person who cannot see distant objects clearly needs which lens?", "solution": "A concave (diverging) lens — the defect is myopia."},
            },
            {
                "title": "Mirror by job",
                "body": "Need a **wide view** → convex (vehicle rear view). Need an **enlarged or focused** image/beam → concave (shaving, dentist, headlight).",
                "example": None,
            },
        ],
        "mistakes": [
            "Explaining the blue sky by reflection or refraction — it is scattering.",
            "Saying red deviates most in a prism — violet deviates most, red least.",
            "Choosing a concave mirror for rear-view — vehicles use convex mirrors.",
        ],
    },
    {
        "id": "ph-electricity",
        "title": "Electricity, magnetism and the EM spectrum",
        "concept": C_ELEC,
        "formulas": [
            {"name": "Ohm's law", "tex": r"V = IR", "note": ""},
            {"name": "Series resistance", "tex": r"R_s = R_1 + R_2 + \cdots", "note": ""},
            {"name": "Parallel resistance", "tex": r"\frac{1}{R_p} = \frac{1}{R_1} + \frac{1}{R_2} + \cdots", "note": "two resistors: R₁R₂/(R₁+R₂)"},
            {"name": "Electric power", "tex": r"P = VI = I^{2}R = \frac{V^{2}}{R}", "note": ""},
            {"name": "Joule heating", "tex": r"H = I^{2}Rt", "note": ""},
            {"name": "Resistance of a wire", "tex": r"R = \rho\frac{L}{A}", "note": "ρ = resistivity"},
        ],
        "tricks": [
            {
                "title": "Fleming hands: 'Left for Motor, Right for Generator' (L-M, R-G)",
                "body": "Remember as the alphabet — **L** comes before **M**; **G** is 'generated' by the **R**ight hand.",
                "example": None,
            },
            {
                "title": "EM spectrum order: 'Good X-rays Use Visible Infra-Micro Radios'",
                "body": "**G**amma → **X**-ray → **U**V → **V**isible → **I**R → **M**icrowave → **R**adio: wavelength increases, frequency and energy decrease.",
                "example": {"q": "Which has the longest wavelength: X-rays, UV, microwaves, gamma rays?", "solution": "Microwaves."},
            },
        ],
        "mistakes": [
            "Assuming a fuse should have a high melting point — it must melt easily.",
            "Thinking a transformer works on DC — it needs changing current (AC).",
            "Connecting an ammeter in parallel — it goes in series; a voltmeter goes in parallel.",
        ],
    },
    {
        "id": "ph-modern-scientists",
        "title": "Nuclear physics, inventions and scientists",
        "concept": C_MODERN,
        "formulas": [
            {"name": "Mass–energy equivalence", "tex": r"E = mc^{2}", "note": "Einstein"},
        ],
        "tricks": [
            {
                "title": "Fission vs fusion",
                "body": "**Fission = split** (heavy → lighter, reactors, atom bomb). **Fusion = fuse** (light → heavier, **Sun**, hydrogen bomb).",
                "example": {"q": "The Sun's energy comes from?", "solution": "Nuclear fusion of hydrogen into helium."},
            },
            {
                "title": "Particle discoverers: 'Tom Ran Chasing'",
                "body": "Electron — **T**homson (1897); nucleus/proton — **R**utherford; neutron — **Chad**wick (1932).",
                "example": None,
            },
        ],
        "mistakes": [
            "Naming Einstein's Nobel for relativity — it was for the photoelectric effect.",
            "Calling the moderator the neutron absorber — control rods (cadmium/boron) absorb; the moderator slows neutrons.",
            "Crediting Edison with the telephone — it was Graham Bell.",
        ],
    },
]

PYQ = [
    {"pattern": "SI unit of a quantity", "frequency": "very common", "howToSpot": "'The SI unit of magnetic flux / power of lens / pressure is...'", "approach": "Learn the derived-unit table; watch light year (distance) and kWh (energy) traps."},
    {"pattern": "Instrument → what it measures", "frequency": "very common", "howToSpot": "'Hygrometer is used to measure...'", "approach": "Decode the prefix (hygro, hydro, lacto, anemo, sphygmo, pyro)."},
    {"pattern": "Everyday phenomenon → principle", "frequency": "very common", "howToSpot": "'Sky appears blue due to...', 'Rocket works on...', 'Hydraulic brakes work on...'", "approach": "Map phenomenon to law: scattering, third law, Pascal's law, Bernoulli, TIR."},
    {"pattern": "Inventor / discoverer", "frequency": "common", "howToSpot": "'Who invented the telephone?', 'Neutron was discovered by...'", "approach": "Inventions table; Indian scientists (Raman, Bose, Bhabha) are favourites."},
    {"pattern": "Eye defects and mirror/lens uses", "frequency": "common", "howToSpot": "'Myopia is corrected by...', 'Rear-view mirror is...'", "approach": "My-Con/Hyper-Vex; wide view = convex mirror."},
    {"pattern": "Simple numericals (power of lens, resistance, energy units, temperature)", "frequency": "common", "howToSpot": "Small numbers with one formula.", "approach": "P = 100/f(cm); parallel = product/sum; kWh = kW × h; C = (F − 32) × 5/9."},
    {"pattern": "Sound properties", "frequency": "occasional", "howToSpot": "'Sound cannot travel through...', 'Bats use...'", "approach": "Medium needed; ultra > 20 kHz; pitch–frequency."},
]

SOLVED = [
    Q("ph-ex01",
      "Which of the following is the SI unit of luminous intensity?",
      ["Lux", "Lumen", "Candela", "Watt"],
      2,
      "**Candela** is one of the 7 SI **base** units and measures luminous intensity. The **lumen** is luminous flux and the **lux** is illuminance (lumen per square metre); the watt is power.",
      "Of the three light units only candela is a base unit — 'Mighty Kings … Correctly' ends with C.",
      "easy", "ph-units", "SI unit of a quantity", 20),
    Q("ph-ex02",
      "What is the power of a convex lens of focal length 50 cm?",
      ["+0.5 D", "+2 D", "−2 D", "+5 D"],
      1,
      "P = 1/f with f in metres. f = 50 cm = 0.5 m, so P = 1/0.5 = **+2 D**. The sign is positive because a convex lens is converging.",
      "P = 100 / f(cm) = 100/50 = 2; convex → +.",
      "easy", "ph-light", "power of lens numerical", 30),
    Q("ph-ex03",
      "The sky appears blue because of:",
      ["Reflection of light by the ocean", "Refraction of light by the atmosphere", "Scattering of light by air molecules", "Total internal reflection of light"],
      2,
      "Air molecules scatter shorter wavelengths far more than longer ones (**Rayleigh scattering**, ∝ 1/λ⁴). Blue light is scattered all over the sky, so it looks blue. The same effect makes the rising and setting Sun look red.",
      "Colour of the sky/sunset/danger signal → always scattering.",
      "easy", "ph-light", "phenomenon → principle", 20),
    Q("ph-ex04",
      "At what temperature do the Celsius and Fahrenheit scales show the same reading?",
      ["0°", "−32°", "−40°", "100°"],
      2,
      "Put C = F = x in F = (9/5)C + 32: x = 1.8x + 32 → −0.8x = 32 → **x = −40**.",
      "Memorise: −40 is the only common reading.",
      "medium", "ph-heat-sound", "temperature conversion", 30),
]

PRACTICE = [
    Q("ph-q01",
      "A light year is a unit of:",
      ["Time", "Distance", "Intensity of light", "Speed"],
      1,
      "A **light year** is the **distance** light travels in one year — about **9.46 × 10¹⁵ m**. It is used for astronomical distances, not time.",
      None, "easy", "ph-units", "special unit trap", 15),
    Q("ph-q02",
      "Which instrument is used to measure the relative humidity of air?",
      ["Hydrometer", "Hygrometer", "Barometer", "Anemometer"],
      1,
      "A **hygrometer** measures humidity. A hydrometer measures the relative density of liquids, a barometer measures atmospheric pressure and an anemometer measures wind speed.",
      "Hygro ↔ humidity; hydro ↔ liquid.", "easy", "ph-units", "instrument → quantity", 15),
    Q("ph-q03",
      "The SI unit of magnetic flux is:",
      ["Tesla", "Weber", "Henry", "Gauss"],
      1,
      "Magnetic **flux** is measured in **weber (Wb)**. **Tesla** is the unit of magnetic field (flux density), **henry** is inductance and **gauss** is a CGS unit of field.",
      None, "medium", "ph-units", "SI unit of a quantity", 20),
    Q("ph-q04",
      "A 100 W bulb glows for 10 hours. How much electrical energy does it consume?",
      ["10 kWh", "1 kWh", "0.1 kWh", "1000 kWh"],
      1,
      "Energy = power × time = 100 W × 10 h = 1,000 Wh = **1 kWh** (1 unit).",
      "W × h ÷ 1000 = kWh.", "easy", "ph-units", "energy unit numerical", 25),
    Q("ph-q05",
      "The recoil of a gun when a bullet is fired is an example of:",
      ["Newton's first law of motion", "Newton's third law / conservation of momentum", "Law of inertia of direction", "Newton's law of gravitation"],
      1,
      "The bullet is pushed forward and the gun is pushed back with an equal and opposite force (**third law**). Equivalently, the total momentum of gun + bullet stays zero (**conservation of momentum**).",
      None, "easy", "ph-mechanics", "phenomenon → law", 20),
    Q("ph-q06",
      "Hydraulic brakes in vehicles work on the principle of:",
      ["Archimedes' principle", "Bernoulli's principle", "Pascal's law", "Newton's law of cooling"],
      2,
      "**Pascal's law**: pressure applied to an enclosed incompressible fluid is transmitted equally in all directions. Hydraulic brakes, lifts and presses use it.",
      "Anything 'hydraulic' → Pascal.", "easy", "ph-mechanics", "phenomenon → principle", 20),
    Q("ph-q07",
      "The value of acceleration due to gravity (g) on the Earth's surface is:",
      ["Maximum at the equator", "Maximum at the poles", "Same everywhere", "Maximum at the Tropic of Cancer"],
      1,
      "The Earth is slightly flattened at the poles, so the poles are closer to the centre, and there is no rotational effect there. Hence **g is maximum at the poles** and minimum at the equator.",
      None, "medium", "ph-mechanics", "gravity variation", 20),
    Q("ph-q08",
      "A nutcracker is an example of which class of lever?",
      ["Class 1", "Class 2", "Class 3", "It is not a lever"],
      1,
      "In a nutcracker the **load (nut) lies between** the hinge (fulcrum) and the hands (effort), making it a **class 2** lever, like a wheelbarrow and a bottle opener.",
      "Middle item = Load → class 2.", "medium", "ph-mechanics", "lever class", 20),
    Q("ph-q09",
      "Why do steam burns cause more severe injuries than boiling water at the same temperature?",
      ["Steam has higher specific heat", "Steam releases extra latent heat when it condenses", "Steam is at a higher pressure", "Steam penetrates the skin faster"],
      1,
      "Steam at 100 °C gives out its **latent heat of vaporisation** (about 2,260 J per gram) as it condenses on skin, in addition to the heat released by cooling. Boiling water gives only the cooling heat.",
      None, "medium", "ph-heat-sound", "phenomenon → principle", 25),
    Q("ph-q10",
      "Bats navigate in the dark using:",
      ["Infrasonic waves", "Ultrasonic waves", "Infrared rays", "Radio waves"],
      1,
      "Bats emit **ultrasonic** sounds (above 20 kHz) and locate obstacles and prey from the echoes — **echolocation**, the same idea as SONAR.",
      None, "easy", "ph-heat-sound", "sound properties", 15),
    Q("ph-q11",
      "Sound cannot travel through:",
      ["Water", "Steel", "Vacuum", "Air"],
      2,
      "Sound is a mechanical wave and needs a **material medium**. It travels fastest in solids, then liquids, then gases, and **not at all in a vacuum**.",
      None, "easy", "ph-heat-sound", "sound properties", 15),
    Q("ph-q12",
      "Myopia (short-sightedness) is corrected by using a:",
      ["Convex lens", "Concave lens", "Bifocal lens", "Cylindrical lens"],
      1,
      "In **myopia** the image of a distant object forms **in front of the retina**. A **concave (diverging) lens** spreads the rays so the image moves back onto the retina.",
      "My-Con, Hyper-Vex.", "easy", "ph-light", "eye defect correction", 15),
    Q("ph-q13",
      "The sparkling of a diamond is mainly due to:",
      ["Dispersion of light", "Total internal reflection", "Scattering of light", "Interference of light"],
      1,
      "Diamond's high refractive index (about 2.42) gives it a small critical angle (about 24°), so light entering it undergoes repeated **total internal reflection** before emerging — making it sparkle.",
      None, "medium", "ph-light", "phenomenon → principle", 20),
    Q("ph-q14",
      "Two resistors of 6 Ω and 3 Ω are connected in parallel. What is their equivalent resistance?",
      ["9 Ω", "2 Ω", "4.5 Ω", "0.5 Ω"],
      1,
      "For two resistors in parallel, R = R₁R₂/(R₁ + R₂) = (6 × 3)/(6 + 3) = 18/9 = **2 Ω**.",
      "Parallel result is always smaller than the smallest resistor (3 Ω) — only 2 Ω or 0.5 Ω qualify; product/sum gives 2.", "medium", "ph-electricity", "resistance combination numerical", 30),
    Q("ph-q15",
      "Who discovered the neutron?",
      ["J.J. Thomson", "Ernest Rutherford", "James Chadwick", "Niels Bohr"],
      2,
      "**James Chadwick** discovered the neutron in **1932** (Nobel Prize 1935). Thomson discovered the electron and Rutherford the atomic nucleus.",
      "'Tom Ran Chasing' — the third particle goes to Chadwick.", "easy", "ph-modern-scientists", "discoverer", 15),
]

place(PRACTICE, [1, 0, 2, 3, 0, 2, 1, 3, 3, 1, 2, 0, 3, 1, 0])

topic = {
    "id": "physics",
    "sectionId": "ga",
    "title": "Physics",
    "importance": "medium",
    "avgQuestions": {"tier1": 1, "tier2": 1},
    "summary": "SI units and instruments, laws of motion, gravitation, fluids, heat, sound, light, electricity, EM waves, nuclear physics and famous inventions. CGL asks 1-2 questions — mostly units, instruments and 'which principle explains this everyday effect'.",
    "subtopics": SUBTOPICS,
    "pyqPatterns": PYQ,
    "solvedExamples": SOLVED,
    "practice": PRACTICE,
}

if __name__ == "__main__":
    save_topic(topic)
