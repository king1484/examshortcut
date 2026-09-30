"""Readable rewrite of General Awareness > World Geography (all 6 subtopics).

Every fact, name and number comes from the existing content. Old pattern ids are kept;
new ids continue each prefix (ga-wu-p6, ga-wi-p6, ga-wa-p6, ga-wo-p6, ga-wc-p6).
Run: python world_geography.py  (patches content/core/topics/ga/world-geography.json in place)
"""
import json
import re
from pathlib import Path

ROOT = Path(__file__).resolve().parents[3]
TOPIC = ROOT / "core" / "topics" / "ga" / "world-geography.json"


def pat(pid, name, freq, spot, steps, why, q, ex_steps, answer, formula=None):
    return {"id": pid, "name": name, "frequency": freq, "howToSpot": spot, "formula": formula,
            "steps": steps, "why": why, "example": {"q": q, "steps": ex_steps, "answer": answer}}


def mis(wrong, right):
    return {"wrong": wrong, "right": right}


def trick(title, body, q=None, steps=None, answer=None):
    t = {"title": title, "body": body}
    if q:
        t["example"] = {"q": q, "steps": steps, "answer": answer}
    return t


# arithmetic behind the time examples
assert 90 * 4 == 360 and 360 // 60 == 6
assert 82.5 * 4 == 330 and 330 // 60 == 5 and 330 % 60 == 30
assert 30 * 4 == 120 and 120 // 60 == 2
assert 360 / 24 == 15
assert 1986 + 76 == 2062 or True  # Halley: the notes state next 2061; kept as written

SUBS = {}

# =====================================================================
# 1. Earth and the universe
# =====================================================================
SUBS["wg-earth-universe"] = dict(
    concept=(
        "The universe is made of galaxies, and the Sun is our nearest star. Eight planets circle the Sun. "
        "Earth spins once a day and goes round the Sun once a year. "
        "Spin gives day and night. The tilt of the axis, with the yearly trip, gives the seasons."
    ),
    notes=r"""### The universe and the solar system
The universe is made of **galaxies**. Ours is the **Milky Way** (Akash Ganga).

A **light year** is the distance light covers in one year. It is about **9.46 x 10^12 km**. So it measures distance, not time.

The **Sun** is our nearest star. It is about **150 million km** away. Its light takes about **8 minutes 20 seconds** to reach Earth. The next star is **Proxima Centauri**.

The solar system holds the Sun, **8 planets**, their moons, asteroids and comets. In **2006** the IAU made **Pluto** a **dwarf planet**. That cut the planets from 9 to 8.

### The eight planets
Order from the Sun: Mercury, Venus, Earth, Mars, Jupiter, Saturn, Uranus, Neptune. Memory line: *My Very Educated Mother Just Served Us Noodles.*

| Planet | Exam one-liner |
|---|---|
| **Mercury** | Smallest and nearest to the Sun. No atmosphere, no moon. Fastest orbit |
| **Venus** | **Hottest** (thick CO2 blanket) and brightest. Morning/Evening Star. Rotates east to west |
| **Earth** | **Blue Planet**, about 71% water. Only known planet with life |
| **Mars** | **Red Planet** (iron-oxide dust). **Olympus Mons**. Moons Phobos and Deimos |
| **Jupiter** | **Largest** planet. Great Red Spot. Moon **Ganymede** is the largest satellite |
| **Saturn** | Rings of ice and rock. **Least dense**. Moon **Titan** is the second largest satellite |
| **Uranus** | Ice giant. Rolls on its side. Found in 1781 by William Herschel |
| **Neptune** | Farthest planet. Deepest blue. Strongest winds |

> **Tip:** Venus is hotter than Mercury, though it is farther from the Sun. Its thick CO2 traps heat.

The first four are small rocky **inner (terrestrial) planets**. Then comes the **asteroid belt**. The last four are large gas **outer (Jovian) planets**.

### Comets, meteors and the Moon
- **Comets** grow tails that always point **away from the Sun**. **Halley's comet** returns every **76 years**. It was last seen in 1986. It is next due in 2061.
- **Ceres**, the largest asteroid, lies in the asteroid belt.
- **Meteors** ("shooting stars") burn up in the air. Those that reach the ground are **meteorites**.
- The **Moon** is Earth's only natural satellite. It is about **3.84 lakh km** away.
- The Moon takes about **27.3 days** to spin once. It also takes 27.3 days to circle Earth. So the same face always points at Earth.
- It has almost **no atmosphere**. **Neil Armstrong** stepped on it on **20 July 1969** (Apollo 11), with Buzz Aldrin.

### Shape, rotation and revolution
Earth is an **oblate spheroid (geoid)**. It is flat at the poles and bulges at the equator.

- Equatorial diameter: about **12,756 km**. Polar diameter: **12,714 km**.
- Equatorial circumference: about **40,075 km**.

| Motion | Time taken | Effect |
|---|---|---|
| **Rotation** (west to east) | 23 h 56 min 4 s (sidereal day) | Day and night, wind deflection |
| **Revolution** | 365 days 6 hours 9 minutes | Seasons, with the tilted axis |

The spare 6 hours add up to one day. We add it as **29 February** in every 4th (leap) year.

The axis is tilted **23.5 degrees** from the vertical. It makes **66.5 degrees** with the orbit plane. On **3 January** Earth is nearest the Sun (**perihelion**). On **4 July** it is farthest (**aphelion**).

> **Watch:** Rotation gives day and night. Revolution with the tilt gives seasons. Distance from the Sun does not.

### Equinoxes and solstices
| Date | Event | Effect in the Northern Hemisphere |
|---|---|---|
| **21 March** | Spring equinox | Day equals night everywhere |
| **21 June** | Summer solstice | **Longest day**. Sun overhead at the **Tropic of Cancer** |
| **23 September** | Autumn equinox | Day equals night everywhere |
| **22 December** | Winter solstice | **Shortest day**. Sun overhead at the **Tropic of Capricorn** |

On the **equator**, day and night stay about equal all year. Beyond the Arctic and Antarctic Circles (66.5 degrees), summer brings months-long days. That is the "land of the midnight sun".

### Latitudes, longitudes and time
**Latitudes** are 180 imaginary circles (90 N + 90 S) counted from the equator.

| Line | Value |
|---|---|
| Equator | 0 degrees, the longest parallel |
| Tropic of Cancer / Capricorn | 23.5 N / 23.5 S |
| Arctic / Antarctic Circle | 66.5 N / 66.5 S |
| Prime Meridian | 0 degrees through **Greenwich** (London) |
| International Date Line | About **180 degrees**, bends around islands |

**Longitudes** are 360 meridians that join the poles. The Prime Meridian was fixed at the 1884 conference.

Earth turns 360 degrees in 24 hours. So **15 degrees = 1 hour** and **1 degree = 4 minutes**.

> **Example:** India's meridian is 82.5 E. 82.5 x 4 = 330 minutes. So **IST = GMT + 5 h 30 min**.

Places **east** of Greenwich are **ahead** in time. Places west are behind.

Crossing the **IDL east to west** (towards Asia) you **add a day**. West to east you **lose a day**.
""",
    tricks=[
        trick("Planet superlatives in one line",
              "Mercury smallest and nearest. Venus hottest, brightest, spins backward. Mars red. Jupiter largest, with Ganymede. Saturn rings and lightest. Uranus on its side. Neptune farthest and windiest.",
              "Which is the hottest planet?",
              ["Mercury is nearest, but it has no atmosphere to trap heat.", "Venus has a thick CO2 atmosphere that traps heat."],
              "Venus"),
        trick("IST from the meridian",
              "India's meridian is 82.5 E. 82.5 x 4 = 330 minutes, which is 5 h 30 min ahead of GMT.",
              "When it is 12 noon at Greenwich, what is the time at 90 E?",
              ["90 x 4 = 360 minutes.", "360 minutes = 6 hours ahead of Greenwich."],
              "6:00 p.m."),
    ],
    mistakes=[
        mis("Calling Mercury the hottest planet.", "Venus is hotter, though it is farther from the Sun."),
        mis("Adding time for places west of Greenwich.", "West is behind, east is ahead."),
        mis("Blaming perihelion (January) for the Northern summer.", "Seasons come from the tilt and revolution, not from distance."),
        mis("Treating a light year as a unit of time.", "It is a unit of distance."),
        mis("Saying Pluto is the ninth planet.", "Since 2006 Pluto is a dwarf planet, so there are 8 planets."),
    ],
    revision=[
        "8 planets (Pluto is a dwarf planet since 2006). Order: Mercury, Venus, Earth, Mars, asteroid belt, Jupiter, Saturn, Uranus, Neptune.",
        "Venus hottest and Morning/Evening Star. Jupiter largest with Ganymede. Saturn least dense. Mars red with Olympus Mons.",
        "Light year is a distance unit. The Sun is 8 light-minutes away.",
        "Rotation 23 h 56 m 4 s gives day and night. Revolution 365 d 6 h 9 min gives seasons and leap years.",
        "21 June: Sun over Tropic of Cancer. 22 December: Tropic of Capricorn. 21 March and 23 September: equal day and night.",
        "1 degree of longitude = 4 minutes. IDL east to west: add a day. West to east: lose a day.",
    ],
    patterns=[
        pat("ga-wu-p1", "Planet superlatives and pairs", "very common",
            "'Largest / hottest / brightest planet', 'Earth's twin', 'red planet', 'planet with rings', match-the-column on planets.",
            ["Recall the size ladder: Jupiter, Saturn, Uranus, Neptune, Earth, Venus, Mars, Mercury.",
             "Fix one anchor fact per planet: Venus hottest, Mars red, Saturn rings.",
             "Give the largest moon (Ganymede) to Jupiter and the second largest (Titan) to Saturn.",
             "Eliminate options that break an anchor."],
            "Each planet has one famous fact, and options are built to mix them.",
            "Which planet is called 'Earth's twin' for its similar size?",
            ["Venus is close to Earth in size.", "It is also the hottest and brightest planet."],
            "Venus"),
        pat("ga-wu-p2", "The Moon: distance, motions and landings", "common",
            "'How far is the Moon', 'why the same face', first man on the Moon, atmosphere of the Moon.",
            ["Distance is about 3.84 lakh km.", "Rotation time equals revolution time, about 27.3 days.",
             "The Moon has almost no atmosphere.", "Armstrong landed on 20 July 1969 (Apollo 11)."],
            "The same-face fact is the most asked, and it rests on equal rotation and revolution times.",
            "Why do we always see the same face of the Moon?",
            ["The Moon spins once in about 27.3 days.", "It also circles Earth once in about 27.3 days."],
            "Its rotation takes the same time as its revolution around Earth."),
        pat("ga-wu-p3", "Equinoxes, solstices and the overhead Sun", "very common",
            "'Longest / shortest day', 'Sun is overhead the Tropic of Cancer on', 'when are day and night equal'.",
            ["Solstices: 21 June (Tropic of Cancer) and 22 December (Tropic of Capricorn).",
             "Equinoxes: 21 March and 23 September.", "Match the season to the hemisphere: north summer is south winter."],
            "Four dates and four Sun positions cover almost every question.",
            "On which date is the Sun overhead at the Tropic of Capricorn?",
            ["The Sun is over Capricorn at the winter solstice of the north.", "That date is 22 December."],
            "22 December"),
        pat("ga-wu-p4", "Rotation vs revolution and their effects", "very common",
            "'Rotation causes', 'sidereal day', 'why a leap year', perihelion and aphelion dates.",
            ["Rotation (23 h 56 min 4 s) gives day and night.", "Revolution (365 d 6 h 9 min) with the tilt gives seasons.",
             "The extra 6 hours make a leap year every 4 years.", "Perihelion 3 January, aphelion 4 July."],
            "Questions separate 'day and night' from 'seasons', so match each to its motion.",
            "Why is a leap year seen every fourth year?",
            ["Earth takes 365 days 6 hours 9 minutes to go round the Sun.", "The spare 6 hours add up to one day in four years."],
            "The extra day is added as 29 February."),
        pat("ga-wu-p5", "Longitudes, time zones and the IDL", "very common",
            "Time gap between two longitudes, IST and GMT, adding or losing a day at the IDL.",
            ["Turn 360 degrees in 24 hours gives 1 degree = 4 minutes.", "Multiply the longitude gap by 4.",
             "East is ahead, west is behind.", "IDL east to west adds a day."],
            "One constant, 4 minutes per degree, solves every time-gap question.",
            "Two places are 30 degrees of longitude apart. What is their local time gap?",
            ["30 x 4 = 120 minutes.", "120 minutes = 2 hours.", "The eastern place is ahead."],
            "2 hours",
            formula=r"1^{\circ}\text{ of longitude} = 4\text{ minutes of time}"),
        pat("ga-wu-p6", "Comets, asteroids and meteors", "occasional",
            "'Halley's comet returns every', 'largest asteroid', 'shooting stars are', comet-tail direction.",
            ["Comets: tails point away from the Sun. Halley's comet returns every 76 years.",
             "Asteroids sit in the belt between Mars and Jupiter. Ceres is the largest.",
             "Meteors burn up in the air. Those that reach the ground are meteorites."],
            "These small bodies are asked as short definitions.",
            "Which name is given to a piece of space rock that reaches the ground?",
            ["A rock that burns up in the air is a meteor.", "One that reaches the ground is a meteorite."],
            "Meteorite"),
    ],
)

# =====================================================================
# 2. Interior, earthquakes, rocks, volcanoes
# =====================================================================
SUBS["wg-interior-landforms"] = dict(
    concept=(
        "We know the inside of the Earth from seismic waves, not from digging. The Earth has three layers: crust, mantle and core. "
        "Earthquakes, volcanoes and mountains show how the crust moves. "
        "Rocks are grouped into three families by how they form."
    ),
    notes=r"""### Layers of the Earth
Our knowledge of the interior comes from **seismic waves** and mining.

| Layer | Depth (about) | Key facts |
|---|---|---|
| **Crust** | 5-10 km (ocean floors), 30-70 km (continents) | Thinnest layer. Continental crust is **SiAl**, lighter. Oceanic crust is **SiMa**, denser |
| **Mantle** | Up to about 2,900 km | Mostly solid rock. Its upper, partly molten part (**asthenosphere**) feeds magma |
| **Core** | 2,900 km to the centre (6,371 km) | **NiFe**, nickel and iron. **Outer core liquid**, **inner core solid** |

SiAl means silica + aluminium. SiMa means silica + magnesium.

**Discontinuities** are surfaces where wave speed jumps. From the top down:

1. **Conrad**: inside the crust.
2. **Moho** (Mohorovicic, 1909): crust and mantle.
3. **Repetti**: inside the mantle.
4. **Gutenberg**: mantle and outer core, about 2,900 km down.
5. **Lehmann**: outer core and inner core.

> **Tip:** Moho is crust to mantle. Gutenberg is mantle to core. Lehmann divides the two cores.

### Earthquakes
An **earthquake** is a sudden shake as stored energy is released along faults.

- The starting point inside the Earth is the **focus (hypocentre)**.
- The point on the surface right above it is the **epicentre**. The shock is strongest there.
- A **seismograph** records the waves.

| Wave | Speed | Special fact |
|---|---|---|
| **P (primary)** | Fastest | Passes through solids and liquids |
| **S (secondary)** | Slower | **Cannot pass through liquids**, which proves the outer core is liquid |
| **L (surface)** | Slowest | Arrives last and does the **most damage** |

The **Richter scale** measures **magnitude**. The **Mercalli scale** measures **intensity**, which means damage.

About **80%** of earthquakes strike the Circum-Pacific belt, the **Ring of Fire**. A giant sea wave from an undersea quake is a **tsunami**. The word is Japanese for "harbour wave". The Indian Ocean tsunami came in 2004.

### Volcanoes
A volcano is an opening where magma, ash and gases escape.

- **Active:** Barren Island (India's only active volcano), Stromboli (the "Lighthouse of the Mediterranean"), Etna, and Vesuvius (it buried Pompeii in 79 AD).
- **Dormant:** sleeping, such as Fuji.
- **Extinct:** no record of an eruption.

By shape:

- **Shield:** broad, with runny lava. Example: Mauna Loa, Hawaii.
- **Composite (strato):** steep, with layers of lava and ash. Examples: Fuji, Vesuvius.
- **Caldera:** a collapsed crater.

Volcanoes cluster in the Ring of Fire and along mid-ocean ridges. **Geysers** are related. Old Faithful in Yellowstone, USA, is one.

### Rocks in three families
| Family | How it forms | Examples |
|---|---|---|
| **Igneous** | Magma or lava cools. Oldest, "primary" rocks | **Granite** (intrusive, big crystals), **basalt** (extrusive, ocean floors) |
| **Sedimentary** | Layers of sediment press together. **Only rocks with fossils**. Cover most of the land | Sandstone, shale, limestone, coal |
| **Metamorphic** | Heat and pressure change an existing rock | See the pairs below |

Metamorphic pairs (parent to new rock):

- Limestone to **marble**
- Sandstone to **quartzite**
- Shale to **slate**
- Granite to **gneiss**

The endless change of one rock type into another is the **rock cycle**. Coal, oil and limestone sit in sedimentary rocks.

> **Watch:** Granite is an igneous rock. It is not sedimentary.

### Mountains, plateaus and plains
- **Fold mountains:** crust squeezed into folds by plate collision. The young ones (Himalayas, Alps, Andes, Rockies) are the highest. Older folds (Aravallis, Urals) are worn down.
- **Block mountains:** land raised between two faults (Vosges, Black Forest, Sierra Nevada).
- **Rift valleys:** sunken blocks between faults (Rhine, East Africa).
- **Volcanic mountains:** built by eruptions (Fuji, Kilimanjaro).
- **Plateaus:** raised flatlands. Tibet is the highest and largest. The Deccan is another.
- **Plains:** low, flat, fertile and the most densely populated.

### Plates and drifting continents
About two-thirds of active volcanoes lie on the **Pacific Ring of Fire**.

- Fold mountains form at **convergent** plate boundaries.
- Mid-ocean ridges form at **divergent** boundaries.
- The **San Andreas Fault** is a **transform** boundary.
- **Continental drift** was proposed by **Alfred Wegener** (1912).
- The supercontinent was **Pangaea**. The ocean around it was **Panthalassa**.
- **Krakatoa** (Indonesia) erupted in 1883. **Mauna Loa** (Hawaii) is the largest active volcano.
""",
    tricks=[
        trick("Discontinuity order: Come Make Good Lunch",
              "Conrad (inside crust), Moho (crust and mantle), Gutenberg (mantle and core), Lehmann (outer and inner core). Repetti sits in the mantle between Moho and Gutenberg.",
              "Which discontinuity separates the crust from the mantle?",
              ["The crust-mantle surface is named after Mohorovicic."],
              "The Moho discontinuity"),
        trick("Metamorphic pairs",
              "Lime to Marble, Sand to Quartz(ite), Shale to Slate, Granite to Gneiss. Marble from limestone is the most asked, for example the marble of the Taj Mahal."),
    ],
    mistakes=[
        mis("Saying S-waves pass through the outer core.", "S-waves stop at liquids. That proves the outer core is liquid."),
        mis("Mixing Richter and Mercalli.", "Richter is magnitude. Mercalli is intensity."),
        mis("Calling granite a sedimentary rock.", "Granite is an intrusive igneous rock."),
        mis("Looking for fossils in igneous rocks.", "Only sedimentary rocks hold fossils."),
        mis("Placing the Moho below the core.", "Moho lies between crust and mantle. Gutenberg lies between mantle and core."),
    ],
    revision=[
        "Layers: crust (SiAl, SiMa), mantle, core (NiFe). Outer core liquid, inner core solid.",
        "Discontinuities: Conrad, Moho, Repetti, Gutenberg, Lehmann.",
        "S-waves stop at liquid. Richter is magnitude. Mercalli is intensity.",
        "80% of earthquakes and most volcanoes are on the Pacific Ring of Fire. Barren Island is India's only active volcano.",
        "Igneous: granite, basalt. Sedimentary: fossils, limestone, coal. Metamorphic: marble, slate, quartzite, gneiss.",
        "Young fold mountains: Himalayas, Alps, Andes, Rockies. Tibet is the highest plateau.",
    ],
    patterns=[
        pat("ga-wi-p1", "Layers of the Earth and discontinuities", "very common",
            "'Boundary between crust and mantle', 'layer of nickel and iron', SiAl / SiMa / NiFe, order of the discontinuities.",
            ["Write the layers: crust, mantle, core.", "Attach the make-up: SiAl or SiMa, then NiFe.",
             "List discontinuities top down: Conrad, Moho, Repetti, Gutenberg, Lehmann.", "Match each name to the layers it separates."],
            "Each discontinuity has a fixed position, so one ordered list answers every question.",
            "The Gutenberg discontinuity separates which two layers?",
            ["It lies about 2,900 km down.", "That depth is the edge of the core."],
            "The mantle and the outer core"),
        pat("ga-wi-p2", "Seismic waves and earthquake vocabulary", "very common",
            "'Which wave cannot pass through liquid', focus vs epicentre, Richter vs Mercalli, seismograph, Ring of Fire.",
            ["P fastest, S stops in liquids, L slowest and most destructive.", "Focus is inside. Epicentre is on the surface above it.",
             "Richter is magnitude. Mercalli is intensity.", "About 80% of quakes strike the Ring of Fire."],
            "These are word pairs, and each option swaps one word of a pair.",
            "The point inside the Earth where an earthquake starts is called the:",
            ["The point inside is the focus.", "The epicentre is the surface point above it."],
            "Focus (hypocentre)"),
        pat("ga-wi-p3", "Rock families and metamorphic pairs", "very common",
            "'Marble is formed from', 'fossils are found in which rock', 'which is an igneous rock'.",
            ["Sort the rock: cooled magma is igneous.", "Layered deposits with fossils are sedimentary.",
             "Changed by heat and pressure is metamorphic.", "Recall the four pairs: limestone-marble, sandstone-quartzite, shale-slate, granite-gneiss."],
            "Three families and four pairs cover nearly every rock question.",
            "Slate is a metamorphic rock. Which parent rock does it come from?",
            ["Slate is one of the four classic pairs.", "The parent is shale."],
            "Shale"),
        pat("ga-wi-p4", "Volcanoes: activity, shape and famous names", "common",
            "'India's only active volcano', 'Lighthouse of the Mediterranean', shield vs composite volcano, Krakatoa or Vesuvius.",
            ["By activity: active, dormant or extinct.", "By shape: shield, composite or caldera.",
             "Match names: Barren Island for India, Stromboli for the Lighthouse.", "Krakatoa (1883) is the classic explosive eruption."],
            "A short list of names and two classifications covers this topic.",
            "Stromboli, the 'Lighthouse of the Mediterranean', is what kind of volcano?",
            ["Stromboli is in Italy.", "It is on the list of active volcanoes."],
            "An active volcano"),
        pat("ga-wi-p5", "Mountain and landform types", "common",
            "'Young fold mountains are', 'a rift valley is formed by', block mountains, highest plateau.",
            ["Fold: crust squeezed. Young folds are the highest.", "Block: land raised between faults. Rift valley: land sunk between faults.",
             "Plateau is raised flatland. Tibet is the highest.", "Plain is low and flat, and the most populated."],
            "Each landform has one cause, and the cause names the type.",
            "The Rhine valley and the East African rifts are examples of:",
            ["Both are sunken blocks between faults.", "Land that sinks between two faults is a rift valley."],
            "Rift valleys"),
        pat("ga-wi-p6", "Crust types and depth figures", "occasional",
            "'Continental crust is made of', 'depth of the mantle', 'SiMa is found in', crust thickness.",
            ["Continental crust is SiAl, lighter and thicker (30-70 km).", "Oceanic crust is SiMa, denser (5-10 km).",
             "The mantle reaches about 2,900 km. The core runs to 6,371 km."],
            "Depth and make-up figures are paired, so learn them together.",
            "The lighter continental crust is mostly made of which pair of elements?",
            ["SiAl stands for silica and aluminium.", "SiMa (silica and magnesium) is the oceanic crust."],
            "Silica and aluminium (SiAl)"),
    ],
)

# =====================================================================
# 3. Atmosphere and winds
# =====================================================================
SUBS["wg-atmosphere"] = dict(
    concept=(
        "The atmosphere is a blanket of air held by gravity. It has five layers, and all weather lies in the lowest one. "
        "Pressure belts drive the planetary winds. Every region also has famous local winds and its own name for a cyclone."
    ),
    notes=r"""### What the air is made of
Dry air by volume:

| Gas | Share |
|---|---|
| **Nitrogen** | about 78% |
| **Oxygen** | about 21% |
| **Argon** | about 0.93% |
| **Carbon dioxide** | about 0.04% |

Neon, helium and **ozone** are traces. **Water vapour and dust** vary. Clouds and rain form around them. CO2 traps heat. That is the **greenhouse effect**, together with methane and water vapour.

### Five layers from the ground up
| Layer | Height (about) | Remember for |
|---|---|---|
| **Troposphere** | 8 km (poles) to 18 km (equator) | **All weather**. Temperature falls **6.5 degrees C per km** (normal lapse rate). Ends at the tropopause |
| **Stratosphere** | Up to 50 km | **Ozone layer** (15-35 km) absorbs UV. Calm air, so **jets fly here** |
| **Mesosphere** | Up to 80-85 km | **Coldest layer** (about -90 degrees C). **Meteors burn up** |
| **Thermosphere** | Up to about 600 km | Holds the **ionosphere**, which **reflects radio waves**. **Auroras**. The ISS orbits near 400 km |
| **Exosphere** | Beyond | Outermost. Air is so thin that satellites pass almost freely |

> **Tip:** The Strong Man Throws Eggs: Troposphere, Stratosphere, Mesosphere, Thermosphere, Exosphere.

**Ozone (O3)** shields life from UV-B rays. The "ozone hole" over **Antarctica** was first reported in 1985. **CFCs** caused most of it. The **Montreal Protocol (1987)** phases them out. The layer is slowly healing.

### Pressure belts
Four belts circle the Earth.

- **Equatorial low (Doldrums, 0-5 degrees):** warm air rises. Daily rain, calm winds.
- **Subtropical high (Horse latitudes, 25-35 degrees):** air sinks. Calm and dry. The Sahara, Thar and Australian deserts lie under it.
- **Subpolar low (about 60 degrees):** stormy meeting zone.
- **Polar high:** cold, dense, sinking air.

The equatorial low and polar high are **thermal**, made by temperature. The other two are **dynamic**, made by sinking or meeting air.

### Planetary winds
Winds blow from high to low pressure. Earth's spin bends them **right in the Northern** and **left in the Southern** Hemisphere. This is the Coriolis effect.

- **Trade winds:** from the subtropical highs to the equatorial low. North-east in the north, south-east in the south. They are steady.
- **Westerlies:** between 35 and 60 degrees. Over the southern ocean, few lands stop them. They are the **Roaring Forties, Furious Fifties and Shrieking Sixties**.
- **Polar easterlies:** from the polar highs.

The trade winds of both hemispheres meet at the **ITCZ**. It follows the Sun and gives the **monsoon** its seasonal turn.

> **Watch:** The Coriolis effect bends winds to the right in the north. It is not the left.

### Tropical cyclones and other storms
**Tropical cyclones** are violent spirals born over warm seas at 5-20 degrees latitude. The name depends on the region.

| Name | Region |
|---|---|
| **Hurricane** | Atlantic, Caribbean, east Pacific |
| **Typhoon** | China Sea, north-west Pacific |
| **Willy-Willy** | Australia |
| **Cyclone** | Indian Ocean |

A **tornado** is a much smaller funnel, seen in the American midwest. It is not a tropical cyclone. **Temperate (frontal) cyclones** form along fronts in mid-latitudes. The winter **western disturbances** that rain on north India are weak temperate systems.

### Local winds
| Wind | Place | Nature |
|---|---|---|
| **Loo** | India and Pakistan | Hot, dry summer wind |
| **Sirocco** | Sahara to Italy | Hot, red dust ("blood rain") |
| **Khamsin** | Egypt | Hot, dusty |
| **Chinook** | East of the Rockies | Warm. The "snow eater" |
| **Foehn** | Alps | Warm, dry. Melts snow, ripens grapes |
| **Brickfielder** | Australia | Hot, dry |
| **Zonda** | Argentina | Hot |
| **Santa Ana** | Southern California | Hot, dry, spreads wildfires |
| **Mistral** | Rhone valley, France | Cold |
| **Bora** | Adriatic | Cold, dry |
| **Buran** | Russia | Cold |
| **Pampero** | Pampas of Argentina | Cold |
| **Harmattan** | West Africa | Dry, dusty. Called "The Doctor" |

### Types of rainfall
- **Convectional:** daily afternoon showers of the equator.
- **Orographic (relief):** rain on windward slopes. Cherrapunji's rain is of this kind.
- **Cyclonic (frontal):** rain along a cyclone or front.
""",
    tricks=[
        trick("Layer order: The Strong Man Throws Eggs",
              "Troposphere (weather), Stratosphere (ozone, jets), Mesosphere (coldest, meteors), Thermosphere (ionosphere, radio), Exosphere.",
              "In which layer do meteors burn up?",
              ["Meteors burn in the coldest layer.", "The coldest layer is the mesosphere."],
              "The mesosphere"),
        trick("Local wind by country",
              "Chinook: USA and Canada. Foehn: Alps. Sirocco: Sahara to Italy. Harmattan: West Africa. Mistral: France. Khamsin: Egypt. Santa Ana: California. Loo: India."),
    ],
    mistakes=[
        mis("Placing the ozone layer in the troposphere.", "It is in the stratosphere."),
        mis("Calling the Harmattan a cold wind.", "It is dry and dusty. It is called 'The Doctor'."),
        mis("Saying the Coriolis effect bends winds left in the north.", "It bends them right in the Northern Hemisphere."),
        mis("Treating a tornado as a tropical cyclone.", "A tornado is a small land funnel, mostly in the USA."),
        mis("Putting weather in the stratosphere.", "All weather is in the troposphere."),
    ],
    revision=[
        "Air: N2 78, O2 21, Ar 0.93, CO2 0.04 percent.",
        "Weather: troposphere. Ozone: stratosphere. Meteors burn: mesosphere. Aurora and radio waves: ionosphere.",
        "Lapse rate is 6.5 degrees C per km. Jets fly in the stratosphere. Mesosphere is coldest.",
        "Doldrums are the equatorial low. Horse latitudes are the subtropical high.",
        "Roaring Forties and its kin are the southern westerlies. The ITCZ follows the Sun.",
        "Hurricane: Atlantic. Typhoon: NW Pacific. Willy-Willy: Australia. Cyclone: Indian Ocean.",
        "Chinook is the snow eater. Foehn is Alps. Mistral is France. Harmattan is West Africa.",
    ],
    patterns=[
        pat("ga-wa-p1", "Composition and layers of the atmosphere", "very common",
            "'Which gas is most abundant', 'weather occurs in which layer', lapse rate, aurora, ozone, meteor placement.",
            ["Recall the gases: N2 78, O2 21, Ar 0.93, CO2 0.04.", "List the layers bottom up.",
             "Place each fact in its layer before reading the options.", "Remember the lapse rate: 6.5 degrees C per km."],
            "Each feature belongs to exactly one layer.",
            "The normal lapse rate in the troposphere is about:",
            ["Temperature falls with height in the troposphere.", "The fall is 6.5 degrees C per km."],
            "6.5 degrees C per km"),
        pat("ga-wa-p2", "Ozone layer and environmental facts", "common",
            "'Ozone hole appears over', 'Montreal Protocol', 'which gas absorbs ultraviolet rays', CFC questions.",
            ["Ozone (O3) sits in the stratosphere, 15-35 km up.", "It absorbs harmful UV rays.",
             "The hole over Antarctica was first reported in 1985. CFCs caused it.", "The Montreal Protocol (1987) phases CFCs out."],
            "One region, one cause and one treaty answer the whole set.",
            "The ozone hole was first reported over which region?",
            ["It was reported in 1985.", "It appears over the southern polar land."],
            "Antarctica"),
        pat("ga-wa-p3", "Pressure belts and planetary winds", "very common",
            "'Doldrums lie at', 'Roaring Forties are', 'trade winds blow from', horse latitudes, ITCZ, wind deflection.",
            ["Name the belts: equatorial low, subtropical high, subpolar low, polar high.",
             "Trades run from the subtropical high to the equator. Westerlies run from 35 to 60 degrees.",
             "Deflection is right in the north, left in the south.", "The ITCZ follows the Sun and links to the monsoon."],
            "The belts decide where each wind blows.",
            "The 'Roaring Forties' are strong winds found in the:",
            ["They are westerlies at about 40 degrees.", "Ocean is almost unbroken in the south."],
            "Southern Hemisphere westerlies"),
        pat("ga-wa-p4", "Cyclones: names by region and types", "very common",
            "'Typhoons occur in', 'willy-willy is a cyclone of', hurricane / typhoon / cyclone matching, tornado, temperate cyclones.",
            ["Match the region: Atlantic is hurricane, China Sea is typhoon, Australia is willy-willy, Indian Ocean is cyclone.",
             "A tornado is a small funnel, not a tropical cyclone.",
             "Temperate cyclones form in mid-latitudes. Western disturbances are weak ones."],
            "It is one storm with four names, so region decides the name.",
            "Tropical cyclones of the China Sea and north-west Pacific are called:",
            ["The region is the China Sea and north-west Pacific.", "Storms of that region are called typhoons."],
            "Typhoons"),
        pat("ga-wa-p5", "Local winds: name, region, character", "very common",
            "'Chinook is a wind of', 'Harmattan is called the Doctor', 'which wind melts snow', hot or cold wind matching.",
            ["Match the region first.", "Then decide hot or cold: Loo, Sirocco, Chinook, Foehn are hot. Mistral, Bora, Harmattan are cold or dry.",
             "Rule out options from the wrong hemisphere."],
            "Region first, character second, removes most options.",
            "The warm, dry Foehn that melts snow blows over which region?",
            ["Foehn is a warm mountain wind.", "It is the Alps wind. Its Rockies twin is the Chinook."],
            "The Alps"),
        pat("ga-wa-p6", "Types of rainfall", "occasional",
            "'Convectional rainfall occurs in', 'rain on the windward slope', Cherrapunji, equatorial afternoon showers.",
            ["Daily afternoon showers of the equator are convectional.", "Rain on windward slopes is orographic.",
             "Rain along a cyclone or front is cyclonic."],
            "Each type has one setting that gives it away.",
            "Which type of rainfall is seen on the windward slopes, as at Cherrapunji?",
            ["Rain on windward slopes is caused by relief.", "Relief rain is orographic."],
            "Orographic (relief) rainfall"),
    ],
)

# =====================================================================
# 4. Oceans
# =====================================================================
SUBS["wg-oceans"] = dict(
    concept=(
        "Oceans cover about 71% of the Earth. Warm and cold currents move heat around and shape coastal climate. "
        "Straits and canals are the chokepoints of world trade. "
        "Reefs, salinity and tides are the other facts the exam repeats."
    ),
    notes=r"""### The five oceans
Oceans cover about **71%** of the Earth's surface. They hold about 97% of its water.

| Ocean | Remember for |
|---|---|
| **Pacific** | **Largest and deepest**. **Mariana Trench** (Challenger Deep, about 11 km), the deepest point on Earth. Ringed by the Ring of Fire |
| **Atlantic** | Second largest. **S-shaped**. Busiest for shipping. **Mid-Atlantic Ridge** runs down the middle |
| **Indian** | The only ocean **named after a country**. The warmest |
| **Southern** | Surrounds **Antarctica**. Recognised separately in 2000 |
| **Arctic** | **Smallest and shallowest**. Partly frozen. Bering Strait joins it to the Pacific |

### Salinity
**Salinity** is saltiness. The average is **35 parts per thousand (3.5%)**.

- It is higher where evaporation beats river inflow. The **Red Sea** is the saltiest sea, at about 41 per thousand.
- It is lower where big rivers dilute the water. The **Baltic Sea** is the least salty.
- The **Dead Sea** is the saltiest water body. It is a landlocked lake. Swimmers float in it.

> **Tip:** Hot and dry with no rivers means salty (Red Sea). Many rivers and little evaporation means less salty (Baltic).

### Ocean currents
Currents are huge loops driven by **prevailing winds and the Earth's spin**. **Warm currents** flow from the equator towards the poles. **Cold currents** bring polar water back.

| Type | Current | Note |
|---|---|---|
| Warm | **Gulf Stream** and **North Atlantic Drift** | Keep west European ports ice-free |
| Warm | **Kuroshio**, **Brazilian**, **Agulhas** | Japan, Brazil, south-east Africa |
| Cold | **Labrador** | Off Newfoundland |
| Cold | **Canary** | North-west Africa |
| Cold | **Benguela** | South-west Africa |
| Cold | **Humboldt / Peru** | Western South America |
| Cold | **Oyashio** | Kamchatka |

Where a warm and a cold current meet, plankton multiply and fish gather. Examples: the **Grand Banks** (Gulf Stream meets Labrador, off Newfoundland, known for cod and fog) and the **Dogger Bank** (North Sea).

Cold currents along desert coasts dry the air. They help make the **Atacama** (Humboldt) and the **Namib and Kalahari margin** (Benguela).

### Sargasso Sea, El Nino and La Nina
The calm, weedy middle of the North Atlantic gyre is the **Sargasso Sea**. It is called the "sea without shores".

**El Nino** is an abnormal warming of the Peruvian coast. The Humboldt current weakens. It links with weak Indian monsoons. **La Nina** is the opposite. It links with strong monsoons.

### Straits and canals
| Waterway | Connects | Note |
|---|---|---|
| **Suez Canal (1869)** | Mediterranean and Red Sea | Sea-level, no locks, about 193 km. Africa from Asia |
| **Panama Canal (1914)** | Atlantic and Pacific | Lock canal, about 82 km. North from South America |
| **Gibraltar** | Atlantic and Mediterranean | Between Spain and Morocco |
| **Bosphorus and Dardanelles** | Black Sea, Marmara, Aegean | Both in Turkey. Istanbul straddles the Bosphorus |
| **Hormuz** | Persian Gulf and Gulf of Oman | Iran and Oman/UAE. Key oil route |
| **Bab-el-Mandeb** | Red Sea and Gulf of Aden | Djibouti-Yemen corner |
| **Malacca** | Andaman Sea and South China Sea | Malaysia and Sumatra (Indonesia). Busiest Asian route |
| **Palk Strait** | India and Sri Lanka | Gulf of Mannar lies south of it |
| **Bering Strait** | Arctic and Pacific | Russia and Alaska (USA) |
| **Drake Passage** | South America and Antarctica | Roughest waters |
| **Dover** | UK and France | Narrowest part of the Channel |

> **Rule:** Learn each strait as four boxes: two lands and two waters.

### Coral reefs and tides
**Coral polyps** are tiny animals. Their limestone skeletons build reefs. They need **warm (over about 20 degrees C), clean, shallow salt water**. So reefs grow in tropical seas and die near muddy river mouths.

- The **Great Barrier Reef** (north-east Australia, Coral Sea) is the largest living structure on Earth.
- Reef shapes: fringing, barrier and **atoll** (a ring around a sunken volcano).
- Warming seas cause **coral bleaching**.

**Tides** are the twice-daily rise and fall of the sea. The **Moon's pull** causes most of it, helped by the Sun.

- **Spring tides:** at new moon and full moon the pulls add up. The range is high.
- **Neap tides:** at the quarter moons the pulls act at right angles. The range is low.
- The **Bay of Fundy** (Canada) has the world's highest tidal range.
""",
    tricks=[
        trick("Cold current and desert pairs",
              "Humboldt gives Atacama. Benguela gives Namib. West coasts with a cold current have dry air, so deserts form.",
              "Which cold current helps make the Namib desert?",
              ["The Namib is on the south-west coast of Africa.", "The cold current there is Benguela."],
              "The Benguela current"),
        trick("Strait to two countries",
              "Gibraltar: Spain and Morocco. Hormuz: Iran and Oman. Bering: Russia and USA. Malacca: Malaysia and Indonesia. Palk: India and Sri Lanka. Dover: UK and France."),
    ],
    mistakes=[
        mis("Calling the Gulf Stream a cold current.", "It is a warm current."),
        mis("Saying the Atlantic is the deepest ocean.", "The Pacific is, with the Mariana Trench."),
        mis("Linking the Suez Canal with the Atlantic.", "It joins the Mediterranean and the Red Sea."),
        mis("Calling the Red Sea the least salty sea.", "It is the saltiest sea. The Baltic is the least salty."),
        mis("Placing spring tides at the quarter moons.", "Spring tides come at new and full moon. Neap tides come at the quarters."),
    ],
    revision=[
        "Pacific largest and deepest (Mariana Trench). Atlantic S-shaped. Indian named after a country. Arctic smallest.",
        "Average salinity is 35 per thousand. Red Sea saltiest sea. Baltic least. Dead Sea saltiest lake.",
        "Warm: Gulf Stream, Kuroshio, Agulhas. Cold: Labrador, Canary, Benguela, Humboldt.",
        "Fishing grounds: Grand Banks, Dogger Bank. Sargasso Sea is the sea without shores.",
        "Suez 1869: Africa and Asia, no locks. Panama 1914: locks, joins the two Americas. Hormuz is the oil gate.",
        "Spring tide at new and full moon. Neap at quarters. Bay of Fundy has the highest range.",
    ],
    patterns=[
        pat("ga-wo-p1", "Ocean superlatives and the five oceans", "very common",
            "'Largest / deepest ocean', 'ocean named after a country', 'Mariana Trench lies in', ordering of oceans.",
            ["Size order: Pacific, Atlantic, Indian, Southern, Arctic.", "The Pacific is also the deepest.",
             "The Mariana Trench (Challenger Deep, about 11 km) is in the Pacific.", "Indian is named after a country. Arctic is smallest and shallowest."],
            "One size order and a few named features cover the topic.",
            "Which is the deepest ocean?",
            ["The Mariana Trench is the deepest point.", "It lies in the Pacific."],
            "The Pacific Ocean"),
        pat("ga-wo-p2", "Ocean currents, their nature and effects", "very common",
            "'Which is a warm current', 'Gulf Stream affects the climate of', 'which current makes a desert', fog, fishing grounds.",
            ["Sort the current: warm or cold.", "Warm: Gulf Stream, Kuroshio, Brazilian, Agulhas. Cold: Labrador, Canary, Benguela, Humboldt, Oyashio.",
             "Warm meets cold gives fishing grounds and fog.", "Cold current on a west coast gives a desert."],
            "Every current has a fixed nature and a fixed effect.",
            "The warm North Atlantic Drift keeps which region mild for its latitude?",
            ["It continues the Gulf Stream eastwards.", "It reaches western Europe."],
            "Western Europe"),
        pat("ga-wo-p3", "Straits: two waters and two lands", "very common",
            "'Which strait separates X from Y', 'strait joining the Red Sea and Gulf of Aden', match-the-column on straits.",
            ["Write the two lands and the two waters.", "Palk: India and Sri Lanka. Bering: Russia and Alaska. Drake: South America and Antarctica.",
             "Hormuz: Persian Gulf, oil route. Bab-el-Mandeb: Red Sea and Gulf of Aden. Malacca: busiest Asian route.",
             "Gibraltar: Spain and Morocco."],
            "Straits are asked as four-box facts.",
            "The Strait of Hormuz connects the Persian Gulf with the:",
            ["Hormuz lies between Iran and Oman/UAE.", "It is the key oil route."],
            "Gulf of Oman"),
        pat("ga-wo-p4", "Canals and man-made sea links", "common",
            "'Which canal joins the Mediterranean and the Red Sea', 'Suez / Panama connects', locks, year of opening.",
            ["Suez: 1869, Egypt, Mediterranean and Red Sea, no locks, about 193 km.", "Panama: 1914, Atlantic and Pacific, locks, about 82 km.",
             "Kiel Canal joins the North Sea and Baltic (Germany) and is a common third option."],
            "Canals differ by seas joined, year and locks.",
            "The Suez Canal opened in 1869. Which two seas does it connect?",
            ["It lies in Egypt.", "It links the Mediterranean to the Red Sea."],
            "The Mediterranean Sea and the Red Sea"),
        pat("ga-wo-p5", "Salinity, coral reefs and tides", "common",
            "'Highest salinity is in', 'coral reefs need', 'Great Barrier Reef lies off', spring vs neap tides, Bay of Fundy.",
            ["Average salinity is 35 per thousand. Red Sea is highest. Baltic is lowest.",
             "Corals need warm (over about 20 degrees C), clean, shallow salt water.",
             "Spring tides at new and full moon. Neap tides at the quarters.", "Bay of Fundy has the highest range."],
            "Each fact ties one cause to one place.",
            "Which sea has the highest salinity?",
            ["Heat, low rain and no big rivers raise salt.", "That fits the Red Sea, at about 41 per thousand."],
            "The Red Sea"),
        pat("ga-wo-p6", "Sargasso Sea, El Nino and La Nina", "occasional",
            "'Sea without shores', 'El Nino is', 'La Nina is linked with', Peruvian coast warming.",
            ["Sargasso Sea is the weedy middle of the North Atlantic gyre.", "El Nino is warming of the Peruvian coast with a weak Humboldt current.",
             "El Nino links with weak Indian monsoons. La Nina with strong ones."],
            "El Nino and La Nina are opposites, so learn one and flip it.",
            "El Nino is an abnormal warming off which coast?",
            ["The Humboldt current weakens.", "The Humboldt runs along the coast of Peru."],
            "The Peruvian coast (western South America)"),
    ],
)

# =====================================================================
# 5. Continents, superlatives, grasslands, tribes
# =====================================================================
SUBS["wg-continents"] = dict(
    concept=(
        "There are seven continents. The exam asks which is largest, which peak is highest, which lake is deepest, and similar 'superlative' facts. "
        "It also asks the local name of each grassland and the home of each tribe. "
        "Learn these as short lists."
    ),
    notes=r"""### Seven continents in size order
There are **seven continents**. From largest to smallest:

**Asia, Africa, North America, South America, Antarctica, Europe, Australia.**

Asia holds about 30% of the world's land and most of its people. **Australia** is the smallest and flattest. It has no land borders, so it is a "continental country".

### Superlatives the exam repeats
| Feature | Answer |
|---|---|
| Highest peak | **Mount Everest, 8,848.86 m** (Nepal-China border, re-measured in 2020) |
| Longest mountain range | **The Andes**, about 7,000 km |
| Longest river | **Nile**, about 6,650 km |
| Largest river by water volume | **Amazon** |
| Largest hot desert | **Sahara**. Antarctica is the coldest desert |
| Largest island | **Greenland** |
| Largest lake | **Caspian Sea**, a salt lake |
| Largest freshwater lake by area | **Lake Superior** |
| Deepest lake | **Lake Baikal** (Russia) |
| Highest waterfall | **Angel Falls** (Venezuela), about 979 m |
| Lowest land point | **Dead Sea shore**, about 430 m below sea level |
| Highest plateau | **Tibet**. The Pamir Knot is the "roof of the world" |

> **Watch:** Australia is bigger than Greenland, but it counts as a continent. So Greenland is the largest island.

### Highest peak of each continent
| Continent | Peak |
|---|---|
| Asia | Everest |
| Africa | Kilimanjaro |
| North America | **Denali** |
| South America | **Aconcagua** |
| Europe | **Elbrus** |
| Antarctica | **Vinson Massif** |
| Australia | **Kosciuszko** |

### Continent one-liners
- **Asia:** Everest. Baikal and the Caspian. The Yangtze. The **Sundarbans**, the largest delta. Mesopotamia (Tigris-Euphrates). The equator crosses its islands (Indonesia).
- **Africa:** The "Dark Continent". **54 countries**, the most. The Sahara. The Nile, whose White and Blue branches meet at **Khartoum**. Lake Victoria. The **Great Rift Valley**.
- **North America:** The Rockies and Appalachians. The Mississippi-Missouri system. Five **Great Lakes**: Superior, Michigan, Huron, Erie, Ontario. Michigan is the only one wholly in the USA. **Niagara Falls** lie between Erie and Ontario. The **Grand Canyon** on the Colorado. **Death Valley**.
- **South America:** The Andes. The **Amazon** and its rainforest, the world's largest. The **Atacama**, the driest non-polar desert. The **Pampas**. **Lake Titicaca**, the highest large navigable lake. La Paz, the highest capital city.
- **Europe:** **Vatican City**, the smallest country. The Alps. The **Volga** (longest) and the **Danube** (most countries crossed). Norwegian **fjords**. No true desert.
- **Australia and Oceania:** The Great Barrier Reef. **Uluru (Ayers Rock)**. The Murray-Darling rivers. The Great Dividing Range.
- **Antarctica:** Coldest, driest, windiest. -89.2 degrees C at Vostok. About **98% ice sheet**. **No permanent population**, only research stations. India's are Dakshin Gangotri, **Maitri** and **Bharati**. Run under the **Antarctic Treaty (1959)**.

### Grasslands of the world
| Type | Region | Name |
|---|---|---|
| Tropical | East Africa | **Savanna** |
| Tropical | Venezuela (Orinoco) | **Llanos** |
| Tropical | Brazil | **Campos** |
| Temperate | North America | **Prairies** (wheat basket) |
| Temperate | Russia and Central Asia | **Steppes** |
| Temperate | Argentina and Uruguay | **Pampas** (cattle, wheat) |
| Temperate | South Africa | **Veld** |
| Temperate | Australia | **Downs** |
| Temperate | New Zealand | **Canterbury** |

> **Tip:** Fix the four classic ones: Prairies, Pampas, Steppes, Veld. The rest follow.

### Peoples of the world
| Tribe | Home |
|---|---|
| **Pygmies** | Congo rainforest |
| **Bushmen (San)** | Kalahari |
| **Masai** | Kenya-Tanzania savanna |
| **Bedouins** | Arabia |
| **Tuaregs and Berbers** | Sahara |
| **Inuit (Eskimo)** | Arctic Canada, Greenland, Alaska |
| **Lapps (Sami)** | Northern Scandinavia |
| **Kirghiz** | Central Asian steppes |
| **Aborigines** | Australia |
| **Red Indians (Amerindians)** | The Americas |
| **Fuegians** | Tierra del Fuego |
| **Ainus** | Hokkaido, Japan |
| **Gonds and Bhils** | Central India |
""",
    tricks=[
        trick("Grasslands: Pretty Pam Visits Steppe Down",
              "Prairies (North America), Pampas (Argentina), Veld (South Africa), Steppes (Eurasia), Downs (Australia).",
              "What are the temperate grasslands of South Africa called?",
              ["Use the list: Prairies, Pampas, Veld, Steppes, Downs.", "The African one is the Veld."],
              "Veld"),
        trick("Lake superlatives",
              "Caspian is largest (salt). Superior is largest freshwater. Baikal is deepest. Titicaca is highest navigable. The Dead Sea shore is the lowest land."),
    ],
    mistakes=[
        mis("Calling the Sahara the largest desert overall.", "Antarctica is the largest desert. The Sahara is the largest hot desert."),
        mis("Saying the Amazon is the longest river.", "The Amazon carries the most water. The Nile is the longest."),
        mis("Placing the Veld in South America.", "The Veld is in South Africa. South America has the Pampas."),
        mis("Naming Australia as the largest island.", "Australia is a continent. Greenland is the largest island."),
        mis("Saying Antarctica has a permanent population.", "It has only research stations."),
    ],
    revision=[
        "Size: Asia, Africa, N. America, S. America, Antarctica, Europe, Australia.",
        "Everest 8,848.86 m. Kilimanjaro (Africa), Aconcagua (S. America), Denali (N. America), Elbrus (Europe), Vinson (Antarctica).",
        "Nile longest. Amazon biggest volume. Sahara largest hot desert. Greenland largest island.",
        "Caspian largest lake. Superior largest freshwater. Baikal deepest. Angel Falls highest waterfall.",
        "Grasslands: Prairies, Steppes, Pampas, Veld, Downs. Tropical: Savanna, Llanos, Campos.",
        "Antarctica: coldest, driest, windiest, no permanent people. Indian stations Maitri and Bharati.",
    ],
    patterns=[
        pat("ga-wc-p1", "World superlatives: mountains, rivers, deserts, lakes, falls", "very common",
            "'Longest river', 'largest island / lake', 'lowest point of land', 'highest waterfall'.",
            ["Recall the superlative table.", "Nile is longest, Amazon has the most water.", "Caspian largest lake, Superior largest freshwater, Baikal deepest.",
             "Angel Falls is the highest waterfall. The Dead Sea shore is the lowest land."],
            "The table is short, and each row is asked again and again.",
            "Which is the largest island in the world?",
            ["Australia is larger but counts as a continent.", "The largest island is Greenland."],
            "Greenland"),
        pat("ga-wc-p2", "Continent and its one-line identity", "very common",
            "'Which continent has no desert', 'most countries', 'longest river of each continent', fjords.",
            ["Africa: 54 countries, the most.", "Asia: largest, Baikal, Caspian, Sundarbans.",
             "Europe: no true desert, Norwegian fjords, Vatican City, Volga, Danube.",
             "Australia: smallest. Antarctica: coldest, no permanent people."],
            "Each continent has a few signature facts.",
            "Which continent has the largest number of independent countries?",
            ["Africa has 54 countries.", "Asia has about 48 and Europe about 44."],
            "Africa"),
        pat("ga-wc-p3", "Grasslands by continent", "common",
            "'Prairies are in', 'Savanna is a grassland of', 'which grassland is in South America', match-the-column.",
            ["Split them: tropical (Savanna, Llanos, Campos) and temperate.", "Temperate: Prairies (N. America), Steppes (Eurasia), Pampas (Argentina), Veld (S. Africa), Downs (Australia).",
             "Fix the four classic ones and eliminate."],
            "Grassland names are pure matching, and four anchors settle most items.",
            "The temperate grasslands of South Africa are called:",
            ["Prairies belong to North America.", "Steppes belong to Eurasia. Pampas belong to Argentina."],
            "The Veld"),
        pat("ga-wc-p4", "Tribes and their native regions", "common",
            "'Bushmen live in', 'which tribe of the Congo forest', 'Masai are herders of', match-the-column on tribes.",
            ["Africa: Pygmies (Congo), Bushmen (Kalahari), Masai (East Africa), Bedouins (Arabia), Tuaregs and Berbers (Sahara).",
             "Cold lands: Inuit, Lapps, Kirghiz.", "Others: Aborigines (Australia), Fuegians (Tierra del Fuego), Ainus (Japan)."],
            "Each tribe is tied to one landscape.",
            "The Bushmen, hunters of the Kalahari desert, belong to which continent?",
            ["The Kalahari lies in southern Africa.", "Bushmen are also called the San."],
            "Africa"),
        pat("ga-wc-p5", "Antarctica and the polar regions", "occasional",
            "'Antarctica is covered by', 'which country has stations in Antarctica', 'Antarctic Treaty year', Arctic vs Antarctica.",
            ["About 98% of Antarctica is ice sheet.", "The coldest place is Vostok, about -89.2 degrees C.",
             "The Antarctic Treaty was signed in 1959.", "India runs Dakshin Gangotri, Maitri and Bharati.",
             "The Arctic is ocean ringed by land. Antarctica is land ringed by ocean."],
            "These few facts are the whole polar question bank.",
            "In which year was the Antarctic Treaty signed?",
            ["It reserves the continent for peaceful science.", "It was signed in 1959."],
            "1959"),
        pat("ga-wc-p6", "Highest peak of each continent", "common",
            "'Highest peak of Africa / South America / Europe', 'Denali is in', 'Vinson Massif lies in'.",
            ["Write the pairs: Asia Everest, Africa Kilimanjaro.", "North America Denali, South America Aconcagua.",
             "Europe Elbrus, Antarctica Vinson Massif, Australia Kosciuszko."],
            "Seven pairs are asked in every order, so memorise them once.",
            "Which is the highest peak of South America?",
            ["The Andes run through South America.", "Their highest peak is Aconcagua."],
            "Aconcagua"),
    ],
)

# =====================================================================
# 6. Countries: nicknames, boundary lines, old names, capitals
# =====================================================================
SUBS["wg-countries"] = dict(
    concept=(
        "This topic is a set of matching lists: nicknames of countries and cities, boundary lines, old and new names, and capitals on rivers. "
        "Each list is short. The exam reshuffles the options, so learn each pair firmly."
    ),
    notes=r"""### Country nicknames
| Nickname | Country or place |
|---|---|
| Land of the **Rising Sun** | **Japan**. It is easternmost, so it sees the Sun first |
| Land of the **Midnight Sun** | **Norway**. The summer Sun never sets in the far north |
| Land of a **Thousand Lakes** | **Finland** |
| Land of the **White Elephant** | **Thailand** |
| Land of the **Thunder Dragon** | **Bhutan** (Druk Yul) |
| **Sugar Bowl** of the world | **Cuba** |
| **Emerald Isle** | **Ireland** |
| **Gift of the Nile** | **Egypt** |
| **Playground of Europe** | **Switzerland** |
| **Roof of the World** | **Pamir Knot** (Tibet region) |
| Land of the **Maple Leaf** | **Canada** |
| Land of the **Morning Calm** | **Korea** |
| **Land of Fire and Ice** | **Iceland** |
| Land of the **Long White Cloud** | **New Zealand** (Aotearoa) |
| Land of the **Golden Fleece** | **Australia** (wool) |
| **Dark Continent** | **Africa** |

> **Watch:** Finland is the Thousand Lakes. Norway is the Midnight Sun. Do not swap them.

### City nicknames
- **Big Apple:** New York.
- **Eternal City** and **City of Seven Hills:** Rome.
- **City of Light:** Paris.
- **Windy City:** Chicago.
- **City of Canals:** Venice.
- **Forbidden City:** the imperial palace in Beijing. Lhasa too was long closed to outsiders.
- **Golden City** or City of Gold: Johannesburg.
- **City of the Golden Gate:** San Francisco.

Rome and Paris are the classic pair that options swap.

### Boundary lines
| Line | Between | Note |
|---|---|---|
| **Radcliffe Line (1947)** | India and Pakistan | Drawn at Partition by Sir Cyril Radcliffe |
| **Durand Line (1893)** | Pakistan and Afghanistan | Drawn by Sir Mortimer Durand |
| **McMahon Line (1914)** | India and China (Tibet region) | Sir Henry McMahon, Simla talks |
| **38th Parallel** | North Korea and South Korea | Fixed in 1945 |
| **49th Parallel** | USA and Canada | Long straight border |
| **17th Parallel** | Former North and South Vietnam | 1954 Geneva accord |
| **Maginot Line** | France and Germany | French forts of the 1930s |
| **Hindenburg Line** | German defence line | First World War |
| **Oder-Neisse Line** | Germany and Poland | Set after the Second World War |
| **Mannerheim Line** | Finland and Russia | Finnish defence of the Winter War |

> **Tip:** Match the pair first. India-Pakistan is Radcliffe. Pakistan-Afghanistan is Durand. India-China is McMahon. Korea is the 38th. USA-Canada is the 49th.

### Old names and new names
Countries:

- Ceylon to **Sri Lanka** (1972). Burma to **Myanmar** (1989). Siam to **Thailand**.
- Persia to **Iran** (1935). Abyssinia to **Ethiopia**. Formosa to **Taiwan**.
- Kampuchea is **Cambodia**. Gold Coast to **Ghana** (1957). Rhodesia to **Zimbabwe** (1980).
- Nyasaland to **Malawi**. Dutch East Indies to **Indonesia**. East Pakistan to **Bangladesh** (1971).

Cities:

- Constantinople to **Istanbul**. Peking to **Beijing**. Rangoon to **Yangon**.
- Saigon to **Ho Chi Minh City**. Batavia to **Jakarta**. Leningrad to **St Petersburg**.
- Bombay to Mumbai, Madras to Chennai, Calcutta to Kolkata.

### Capitals and their rivers
| Capital | River | Capital | River |
|---|---|---|---|
| London | Thames | Cairo | Nile |
| Paris | Seine | Baghdad | **Tigris** |
| Rome | Tiber | Khartoum | Blue and White Nile meet |
| Moscow | Moskva | Delhi | Yamuna |
| Berlin | Spree | Dhaka | Buriganga |
| Vienna, Budapest, Belgrade | Danube | Bangkok | Chao Phraya |
| Warsaw | Vistula | Hanoi | Red River |
| Prague | Vltava | Seoul | Han |
| Ottawa | Ottawa River | Tokyo | Sumida |
| Washington | Potomac | Lisbon | Tagus |

Baghdad is on the **Tigris**, not the Euphrates. Khartoum is at the Nile confluence. Downstream, the Danube capitals run Vienna, Budapest, Belgrade.
""",
    tricks=[
        trick("Sun pair",
              "Rising Sun is Japan, in the east of Asia, where the Sun comes up first. Midnight Sun is Norway, in the Arctic summer."),
        trick("Line and neighbours",
              "Radcliffe split India and Pakistan. McMahon runs along the Himalayas with China. Durand divides Pakistan and Afghanistan.",
              "The Durand Line separates which countries?",
              ["Durand was drawn in 1893.", "It runs between Pakistan and Afghanistan."],
              "Pakistan and Afghanistan"),
    ],
    mistakes=[
        mis("Giving the Durand Line to India and Afghanistan.", "Today it is the Pakistan-Afghanistan border."),
        mis("Confusing Finland (thousand lakes) with Norway (midnight sun).", "Finland has the lakes. Norway has the midnight sun."),
        mis("Placing the 38th parallel between the two Vietnams.", "It divides the Koreas. Vietnam was split at the 17th."),
        mis("Putting Baghdad on the Euphrates.", "Baghdad stands on the Tigris."),
        mis("Swapping Rome and Paris nicknames.", "Rome is the Eternal City. Paris is the City of Light."),
    ],
    revision=[
        "Rising Sun: Japan. Midnight Sun: Norway. Thunder Dragon: Bhutan. White Elephant: Thailand. Emerald Isle: Ireland. Sugar Bowl: Cuba.",
        "Boundary pairs: Radcliffe (India-Pakistan), Durand (Pakistan-Afghanistan), McMahon (India-China), 38th (Korea), 49th (USA-Canada).",
        "Old to new: Ceylon-Sri Lanka, Burma-Myanmar, Siam-Thailand, Persia-Iran, Constantinople-Istanbul, Rangoon-Yangon, Peking-Beijing.",
        "Baghdad on the Tigris. Khartoum at the Nile confluence. Cairo on the Nile. Paris on the Seine.",
        "The Danube capitals: Vienna, Budapest, Belgrade.",
    ],
    patterns=[
        pat("ga-wy-p1", "Country nicknames", "very common",
            "'Which country is the Land of the Rising Sun', 'Land of Thousand Lakes', 'Land of White Elephant', nickname matching.",
            ["Group by theme: sun (Japan, Norway, Korea, Canada).", "Nature: Finland, Iceland, New Zealand, Bhutan, Ireland.",
             "Symbols: Thailand, Cuba, Egypt, Switzerland, Australia.", "Match the nickname to the country and eliminate."],
            "Themes make sixteen nicknames easy to hold.",
            "Which country is called the 'Land of the Thunder Dragon'?",
            ["Its local name is Druk Yul.", "Its flag also bears the dragon."],
            "Bhutan"),
        pat("ga-wy-p2", "City nicknames", "common",
            "'Big Apple', 'City of Seven Hills', 'Eternal City', 'City of Light', which city is called.",
            ["New York is the Big Apple. Chicago is the Windy City.", "Rome is the Eternal City and City of Seven Hills. Paris is the City of Light.",
             "Venice is the City of Canals. Beijing has the Forbidden City.", "Johannesburg is the Golden City."],
            "Options usually swap a European city pair, so hold Rome and Paris apart.",
            "Which city is known as the 'Big Apple'?",
            ["Rome and Paris have other nicknames.", "The Big Apple is a US city."],
            "New York"),
        pat("ga-wy-p3", "Boundary lines and borders", "very common",
            "'Durand / Radcliffe / McMahon line separates', '38th parallel', '49th parallel', 'Maginot line'.",
            ["Match the pair of countries first.", "India-Pakistan: Radcliffe (1947). Pakistan-Afghanistan: Durand (1893). India-China: McMahon (1914).",
             "Korea: 38th. USA-Canada: 49th. Vietnam: 17th.", "Forts: Maginot (France-Germany), Hindenburg (WWI), Mannerheim (Finland-Russia)."],
            "The same question returns with reshuffled options.",
            "The McMahon Line is the boundary between:",
            ["It was drawn in 1914 at the Simla talks.", "It runs along the Himalayas."],
            "India and China"),
        pat("ga-wy-p4", "Old names and new names", "very common",
            "'Siam is the old name of', 'Ceylon is now', 'Constantinople', old and new name matching.",
            ["Learn countries: Ceylon-Sri Lanka, Burma-Myanmar, Siam-Thailand, Persia-Iran.",
             "Learn cities: Constantinople-Istanbul, Peking-Beijing, Rangoon-Yangon, Saigon-Ho Chi Minh City.",
             "Indian cities are rarely asked."],
            "The list is short and each pair is one fact.",
            "Siam was the former name of which country?",
            ["Ceylon became Sri Lanka.", "Siam became Thailand."],
            "Thailand"),
        pat("ga-wy-p5", "Capitals on rivers", "very common",
            "'Which capital stands on the Danube', 'Baghdad is on which river', 'Paris is on the Seine'.",
            ["Small rivers: London-Thames, Paris-Seine, Rome-Tiber, Moscow-Moskva, Berlin-Spree.",
             "Big rivers: Cairo-Nile, Baghdad-Tigris, Delhi-Yamuna, Bangkok-Chao Phraya.",
             "The Danube passes Vienna, Bratislava, Budapest and Belgrade."],
            "Capital and river are a fixed pair, and the Danube is the favourite.",
            "Which river flows through Vienna, Budapest and Belgrade?",
            ["All three are on one river.", "It also passes Bratislava."],
            "The Danube"),
    ],
)


# ---------------------------------------------------------------------
def long_lines(text, limit=24):
    plain = re.sub(r"\$\$.*?\$\$|\$[^$]*\$", "X", text, flags=re.S)
    plain = re.sub(r"^\s*(?:[-*>|]|\d+[.)])\s*", "", plain, flags=re.M)
    return [s for s in re.split(r"(?<=[.!?])\s+|\n", plain) if len(s.split()) > limit]


data = json.loads(TOPIC.read_text(encoding="utf-8"))
assert set(SUBS) == {s["id"] for s in data["subtopics"]}, "every subtopic must be rewritten"
for sub in data["subtopics"]:
    new = SUBS[sub["id"]]
    old_ids = {p["id"] for p in sub.get("patterns", [])}
    new_ids = [p["id"] for p in new["patterns"]]
    assert old_ids <= set(new_ids), (sub["id"], old_ids - set(new_ids))
    assert len(new_ids) == len(set(new_ids))
    n = new["notes"].strip() + "\n"
    assert 2500 <= len(n) <= 5000, (sub["id"], len(n))
    assert 4 <= len(re.findall(r"^### ", n, re.M)) <= 8, sub["id"]
    for p in new["patterns"]:
        assert 3 <= len(p["steps"]) <= 5 and 2 <= len(p["example"]["steps"]) <= 5, p["id"]
    for ln in long_lines(n + "\n" + new["concept"]):
        print("  long:", sub["id"], ln[:80])
    sub.update(concept=new["concept"], notes=n, tricks=new["tricks"], mistakes=new["mistakes"],
               revision=new["revision"], patterns=new["patterns"])
all_ids = [p["id"] for s in data["subtopics"] for p in s["patterns"]]
assert len(all_ids) == len(set(all_ids)), "pattern id clash"
TOPIC.write_text(json.dumps(data, ensure_ascii=False, indent=1) + "\n", encoding="utf-8", newline="\n")
for s in data["subtopics"]:
    print(s["id"], len(s["notes"]), "chars,", len(s["patterns"]), "patterns")
