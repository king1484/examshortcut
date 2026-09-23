# -*- coding: utf-8 -*-
"""Builds content/ssc-cgl/topics/ga/world-geography.json. Run: py -3 build_world_geography.py"""
from scicommon import Q, save_topic, place

C_EARTH = """### Solar system (8 planets since the IAU decision of 2006, when Pluto became a **dwarf planet**)
Order from the Sun: **Mercury, Venus, Earth, Mars, Jupiter, Saturn, Uranus, Neptune** ('My Very Educated Mother Just Served Us Noodles').

| Planet | Remember it as |
|---|---|
| **Mercury** | Smallest planet, nearest to the Sun, fastest orbit |
| **Venus** | **Hottest** planet (thick CO₂ atmosphere), brightest, 'Earth's twin', **morning/evening star**, rotates **east to west** (retrograde) |
| **Earth** | 'Blue planet'; only known planet with life |
| **Mars** | '**Red planet**' (iron oxide); Olympus Mons; moons **Phobos and Deimos** |
| **Jupiter** | **Largest** planet; Great Red Spot; **Ganymede** — largest moon of the solar system |
| **Saturn** | Prominent **rings**; **least dense** (lighter than water); largest moon **Titan** |
| **Uranus** | Rotates **on its side** (extreme axial tilt); also retrograde spin |
| **Neptune** | Farthest planet; strongest winds |

Sunlight takes about **8 minutes 20 seconds** to reach the Earth. The Moon is Earth's only natural satellite; the same face always points towards Earth.

### Motions of the Earth
| Motion | Period | Effect |
|---|---|---|
| **Rotation** (west to east) | About 24 hours (sidereal day 23 h 56 m 4 s) | Day and night |
| **Revolution** | About 365¼ days | Seasons (with the tilt) |

- Axis is tilted **23½°** from the perpendicular (makes **66½°** with the orbital plane).
- **Perihelion** (nearest to Sun) about **3 January**; **aphelion** (farthest) about **4 July**.
- **Summer solstice 21 June** — longest day in the Northern Hemisphere, Sun overhead at the Tropic of Cancer. **Winter solstice 22 December** — Sun over the Tropic of Capricorn.
- **Equinoxes — 21 March and 23 September** — Sun overhead at the equator; day = night everywhere.

### Latitudes, longitudes and time
| Line | Value |
|---|---|
| Equator | 0° (longest parallel, a great circle) |
| Tropic of Cancer / Capricorn | 23½° N / 23½° S |
| Arctic / Antarctic Circle | 66½° N / 66½° S |
| Prime Meridian | 0° through **Greenwich** (London) |
| **International Date Line** | Roughly **180°**, zig-zags to avoid land |

- Earth turns 360° in 24 hours → **15° = 1 hour**, **1° = 4 minutes**.
- Places **east** of Greenwich are **ahead** in time; places west are behind.
- Crossing the IDL **westward** (e.g. USA → Japan) you **add a day**; crossing **eastward** you repeat a day.
"""

C_INTERIOR = """### Interior of the Earth
| Layer | Nature | Old name |
|---|---|---|
| **Crust** | Thinnest; continental crust mostly silica + aluminium | **SiAl** |
| **Mantle** | Silica + magnesium; upper part includes the **asthenosphere** (magma source) | **SiMa** |
| **Core** | Nickel + iron; **outer core liquid**, **inner core solid** | **NiFe** |

Discontinuities: **Conrad** (within crust), **Mohorovičić / Moho** (crust–mantle), **Gutenberg** (mantle–core), **Lehmann** (outer–inner core).

### Earthquakes
- Point of origin inside the Earth = **focus (hypocentre)**; point on the surface directly above = **epicentre**.
- **P-waves** (primary) are fastest and travel through solids, liquids and gases. **S-waves** (secondary) cannot pass through liquids — their **shadow zone** proved the outer core is liquid. **Surface (L) waves** are slowest and most destructive.
- Recorded by a **seismograph**; **Richter scale** measures **magnitude** (energy, logarithmic), **Mercalli scale** measures **intensity** (damage).

### Rocks
| Type | Formed by | Examples |
|---|---|---|
| **Igneous** ('primary rocks') | Cooling of magma/lava | **Granite** (intrusive), **basalt** (extrusive) |
| **Sedimentary** | Layers of deposits; contain **fossils** | Sandstone, shale, **limestone**, coal |
| **Metamorphic** | Heat and pressure change existing rocks | **Limestone → marble**, **sandstone → quartzite**, **shale → slate**, **granite → gneiss** |

### Volcanoes and plates
- About two-thirds of active volcanoes lie on the **Pacific 'Ring of Fire'**.
- **Stromboli** (Italy) is the 'Lighthouse of the Mediterranean'; **Vesuvius** buried Pompeii in AD 79; **Krakatoa** (Indonesia) erupted catastrophically in 1883; **Mauna Loa** (Hawaii) is the largest active volcano.
- **Fold mountains** (Himalayas, Alps, Andes, Rockies) form at **convergent** plate boundaries; **mid-ocean ridges** form at divergent boundaries; the **San Andreas Fault** is a transform boundary.
- **Continental drift** was proposed by **Alfred Wegener** (1912); the supercontinent was **Pangaea**, surrounded by the ocean **Panthalassa**.
"""

C_ATMOS = """### Composition (dry air by volume)
**Nitrogen ~78%**, **Oxygen ~21%**, **Argon ~0.93%**, **Carbon dioxide ~0.04%**, plus traces of neon, helium, ozone and variable water vapour.

### Layers of the atmosphere (from the surface up)
| Layer | Key facts |
|---|---|
| **Troposphere** | All **weather**; temperature falls about **6.5 °C per km** (normal lapse rate); about 8 km thick at poles, 18 km at equator; ends at the **tropopause** |
| **Stratosphere** | Contains the **ozone layer** (absorbs UV); calm air — preferred by **jet aircraft** |
| **Mesosphere** | **Coldest** layer; **meteors burn** here |
| **Thermosphere** | Contains the **ionosphere**, which **reflects radio waves**; auroras |
| **Exosphere** | Outermost, very thin air merging into space |

### Pressure belts and planetary winds
- Equatorial low (**doldrums**), subtropical highs (**horse latitudes**, ~30°), sub-polar lows (~60°), polar highs.
- **Trade winds** blow from subtropical highs to the equator (NE trades in the north, SE trades in the south).
- **Westerlies** blow from subtropical highs towards 60°; in the Southern Hemisphere they are called the **Roaring Forties, Furious Fifties and Shrieking Sixties**.
- **Coriolis force** deflects winds to the **right in the Northern** and **left in the Southern** Hemisphere (**Ferrel's law**).

### Local winds (very common PYQ)
| Wind | Region | Nature |
|---|---|---|
| **Chinook** | Rocky Mountains (USA–Canada) | Warm, dry; '**snow eater**' |
| **Foehn** | **Alps** (Switzerland) | Warm, dry; helps grapes ripen |
| **Sirocco** | Sahara → Italy, Mediterranean | Hot, dusty; '**blood rain**' |
| **Harmattan** | West Africa | Dry, dusty from the Sahara; called '**The Doctor**' |
| **Mistral** | Rhône valley, **France** | Cold, northerly |
| **Bora** | Adriatic coast | Cold, dry |
| **Khamsin** | **Egypt** | Hot, dusty |
| **Santa Ana** | Southern California | Hot, dry; spreads wildfires |
| **Brickfielder** | Australia (Victoria) | Hot, dry |
| **Loo** | North India | Hot, dry summer wind |

### Tropical cyclones — same storm, different names
**Hurricane** (Atlantic, Caribbean), **Typhoon** (north-west Pacific — China, Japan, Philippines), **Cyclone** (Indian Ocean), **Willy-willy** (older term for north-west Australia). A **tornado** is a small, violent land funnel, most frequent in the USA.
"""

C_OCEANS = """### Oceans
| Ocean | Key facts |
|---|---|
| **Pacific** | **Largest and deepest**; **Mariana Trench** (Challenger Deep, about 11 km) |
| **Atlantic** | Second largest, **S-shaped**; busiest shipping; Mid-Atlantic Ridge |
| **Indian** | Only ocean **named after a country** |
| **Southern** | Surrounds Antarctica |
| **Arctic** | **Smallest and shallowest** |

### Ocean currents
| Warm currents | Cold currents |
|---|---|
| **Gulf Stream** (N Atlantic, warms NW Europe) | **Labrador** (off Canada) |
| **Kuroshio** (Japan) | **Oyashio** (Japan) |
| Brazil, **Agulhas** (SE Africa), East Australian | **Humboldt / Peru** (W South America) |
| North Atlantic Drift | **Benguela** (SW Africa), **Canary**, **California**, West Australian, Falkland |

- **Cold currents** off **western coasts** of continents in the subtropics create **deserts**: Humboldt → **Atacama**, Benguela → **Namib**, California → Sonoran/Mojave, West Australian → Great Australian desert.
- Meeting of warm and cold currents creates rich **fishing grounds**: **Grand Banks** (Newfoundland) where the **Gulf Stream meets the Labrador current**; Kuroshio–Oyashio off Japan.
- **El Niño** is the periodic warming of the eastern Pacific off Peru; it tends to weaken the Indian monsoon.

### Straits and canals
| Strait | Connects / separates |
|---|---|
| **Palk** | India – Sri Lanka |
| **Gibraltar** | **Spain – Morocco**; Mediterranean ↔ Atlantic |
| **Bering** | **Russia (Asia) – Alaska (N America)**; near the Date Line |
| **Malacca** | Malay Peninsula – Sumatra; Andaman Sea ↔ South China Sea |
| **Hormuz** | **Iran – Oman**; Persian Gulf ↔ Gulf of Oman (oil route) |
| **Bab-el-Mandeb** | Yemen – Djibouti; **Red Sea ↔ Gulf of Aden** |
| **Bosphorus** | Istanbul; **Black Sea ↔ Sea of Marmara** |
| **Dover** | England – France |
| **Magellan** | South American mainland – Tierra del Fuego |
| **Sunda** | Java – Sumatra |
| **Cook** | North and South islands of New Zealand |
| **Bass** | Australia – Tasmania |

Canals: **Suez** (1869) — Mediterranean ↔ Red Sea (Egypt); **Panama** (1914) — Atlantic ↔ Pacific; **Kiel** — North Sea ↔ Baltic (Germany).
"""

C_CONT = """### Continents — superlatives
| Feature | Answer |
|---|---|
| Largest / smallest continent | **Asia** / **Australia** |
| Highest peak | **Mount Everest**, 8,848.86 m (Nepal–China, 2020 joint measurement) |
| Highest peak of Africa / S America / N America / Europe / Antarctica / Australia | **Kilimanjaro** / **Aconcagua** / **Denali** / **Elbrus** / **Vinson Massif** / **Kosciuszko** |
| Longest mountain range | **Andes** |
| Longest river | **Nile** (Africa) |
| Largest river by volume | **Amazon** (South America) |
| Largest hot desert | **Sahara**; largest desert overall is **Antarctica** |
| Driest place | **Atacama** (Chile) |
| Largest lake | **Caspian Sea** |
| Largest freshwater lake (area) | **Lake Superior** (USA–Canada) |
| Deepest (and oldest) lake | **Lake Baikal** (Russia) |
| Highest navigable lake | **Lake Titicaca** (Peru–Bolivia) |
| Lowest point on land | **Dead Sea** shore (Jordan–Israel) |
| Largest island | **Greenland** |
| Largest / smallest country | **Russia** / **Vatican City** |

### Temperate grasslands and savannas
| Name | Region |
|---|---|
| **Prairies** | North America |
| **Pampas** | Argentina |
| **Veld** | South Africa |
| **Steppes** | Eurasia (Ukraine–Kazakhstan) |
| **Downs** | Australia |
| **Canterbury** | New Zealand |
| **Llanos** | Venezuela–Colombia (tropical) |
| **Campos** | Brazil (tropical) |
| **Savanna** | Africa (tropical) |

### Tribes and their homelands
**Masai** — Kenya/Tanzania; **Bedouin** — Arabian and Saharan deserts; **Inuit (Eskimo)** — Arctic Canada, Greenland, Alaska; **Pygmies** — Congo basin; **San (Bushmen)** — Kalahari; **Maori** — New Zealand; **Aborigines** — Australia; **Sami (Lapps)** — northern Scandinavia; **Ainu** — Japan.
"""

C_COUNTRIES = """### Nicknames of places
| Nickname | Place |
|---|---|
| Land of the **Rising Sun** | **Japan** |
| Land of the **Midnight Sun** | **Norway** |
| Land of **Thousand Lakes** | **Finland** |
| Land of the **White Elephant** | **Thailand** |
| Land of the **Thunder Dragon** | **Bhutan** |
| **Sugar Bowl** of the world | **Cuba** |
| **Emerald Isle** | **Ireland** |
| **Gift of the Nile** | **Egypt** |
| **Roof of the World** | **Pamir** plateau |
| **Dark Continent** | **Africa** |
| **Land of Kangaroos** | Australia |
| **Hermit Kingdom** | Korea (historically) |
| **Forbidden City** | **Lhasa** (Tibet); also the imperial palace in Beijing |
| **Windy City** | **Chicago** |
| **Big Apple** | **New York** |
| **City of Golden Gate** | **San Francisco** |
| **Eternal City** | **Rome** |

### Boundary lines
| Line | Between |
|---|---|
| **Radcliffe Line** (1947) | **India – Pakistan** (and India–Bangladesh) |
| **McMahon Line** (1914) | **India – China** (eastern sector) |
| **Durand Line** (1893) | **Pakistan – Afghanistan** |
| **38th Parallel** | **North Korea – South Korea** |
| **49th Parallel** | **USA – Canada** |
| **Oder–Neisse Line** | **Germany – Poland** |
| **Maginot Line** | French fortification facing **Germany** |
| **Mannerheim Line** | Finnish fortification against **Russia (USSR)** |
| **17th Parallel** | North and South Vietnam (1954–1976) |
"""

SUBTOPICS = [
    {
        "id": "wg-earth-universe",
        "title": "Solar system, Earth's motions, latitudes and time",
        "concept": C_EARTH,
        "formulas": [
            {"name": "Time difference from longitude", "tex": r"\Delta t = \Delta\lambda \times 4\ \text{minutes}", "note": "1° of longitude = 4 min; 15° = 1 hour"},
            {"name": "Local time", "tex": r"T_{\text{local}} = T_{\text{GMT}} \pm \frac{\lambda}{15}\ \text{h}", "note": "+ for east longitudes, − for west"},
        ],
        "tricks": [
            {
                "title": "Planet superlatives in one line",
                "body": "**Mercury** smallest–nearest, **Venus** hottest–brightest–backward spin, **Mars** red, **Jupiter** largest (Ganymede biggest moon), **Saturn** rings–lightest, **Uranus** on its side, **Neptune** farthest–windiest.",
                "example": {"q": "Which is the hottest planet?", "solution": "Venus — not Mercury — because its thick CO₂ atmosphere traps heat."},
            },
            {
                "title": "IST from the meridian",
                "body": "India's meridian is 82½°E → 82.5 × 4 = 330 minutes = **5 h 30 min ahead of GMT**.",
                "example": {"q": "When it is 12 noon at Greenwich, what is the time at 90°E?", "solution": "90 × 4 = 360 min = 6 h ahead → 6:00 p.m."},
            },
        ],
        "mistakes": [
            "Calling Mercury the hottest planet — Venus is hotter despite being farther.",
            "Adding time for places west of Greenwich — west is behind, east is ahead.",
            "Mixing perihelion (January) with summer in the Northern Hemisphere — seasons come from the tilt, not distance.",
        ],
    },
    {
        "id": "wg-interior-landforms",
        "title": "Earth's interior, earthquakes, rocks and volcanoes",
        "concept": C_INTERIOR,
        "formulas": [],
        "tricks": [
            {
                "title": "Discontinuity order: 'Come Make Good Lunch'",
                "body": "**C**onrad (inside crust) → **M**oho (crust|mantle) → **G**utenberg (mantle|core) → **L**ehmann (outer|inner core).",
                "example": {"q": "Which discontinuity separates the crust from the mantle?", "solution": "The Mohorovičić (Moho) discontinuity."},
            },
            {
                "title": "Metamorphic pairs: 'Lime-Marble, Sand-Quartz, Shale-Slate, Granite-Gneiss'",
                "body": "The first letters of the new rock are easy: **M**arble from **L**imestone is the most asked (Taj Mahal marble).",
                "example": None,
            },
        ],
        "mistakes": [
            "Saying S-waves travel through the outer core — they cannot pass through liquids.",
            "Mixing Richter (magnitude) with Mercalli (intensity).",
            "Calling granite a sedimentary rock — it is an intrusive igneous rock.",
        ],
    },
    {
        "id": "wg-atmosphere",
        "title": "Atmosphere, pressure belts, planetary and local winds",
        "concept": C_ATMOS,
        "formulas": [],
        "tricks": [
            {
                "title": "Layer order: 'The Strong Man Throws Eggs'",
                "body": "**T**roposphere → **S**tratosphere (ozone, jets) → **M**esosphere (coldest, meteors) → **T**hermosphere (ionosphere, radio) → **E**xosphere.",
                "example": {"q": "In which layer do meteors burn up?", "solution": "The mesosphere."},
            },
            {
                "title": "Local wind by country",
                "body": "Chinook–**USA/Canada**, Foehn–**Alps**, Sirocco–**Sahara→Italy**, Harmattan–**West Africa**, Mistral–**France**, Khamsin–**Egypt**, Santa Ana–**California**, Loo–**India**.",
                "example": None,
            },
        ],
        "mistakes": [
            "Placing the ozone layer in the troposphere — it is in the stratosphere.",
            "Calling the Harmattan a cold wind — it is dry and dusty; 'Doctor' because it relieves humid heat.",
            "Saying Coriolis deflects to the left in the Northern Hemisphere — it is to the right.",
        ],
    },
    {
        "id": "wg-oceans",
        "title": "Oceans, currents, straits and canals",
        "concept": C_OCEANS,
        "formulas": [],
        "tricks": [
            {
                "title": "Cold current → desert pairs",
                "body": "**H**umboldt–**A**tacama, **B**enguela–**N**amib, **C**alifornia–**S**onoran. West coasts + cold current = dry air = desert.",
                "example": {"q": "Which cold current is responsible for the Namib desert?", "solution": "The Benguela current."},
            },
            {
                "title": "Strait → two countries",
                "body": "Gibraltar = Spain|Morocco; Hormuz = Iran|Oman; Bering = Russia|USA; Malacca = Malaysia|Indonesia; Palk = India|Sri Lanka; Dover = UK|France.",
                "example": None,
            },
        ],
        "mistakes": [
            "Calling the Gulf Stream a cold current — it is warm.",
            "Saying the Atlantic is the deepest ocean — the Pacific (Mariana Trench) is.",
            "Linking the Suez Canal to the Atlantic — it joins the Mediterranean and the Red Sea.",
        ],
    },
    {
        "id": "wg-continents",
        "title": "Continents, superlatives, grasslands and tribes",
        "concept": C_CONT,
        "formulas": [],
        "tricks": [
            {
                "title": "Grasslands: 'Pretty Pam Visits Steppe Down'",
                "body": "**P**rairies (N America), **Pam**pas (Argentina), **V**eld (S Africa), **Steppe**s (Eurasia), **Down**s (Australia).",
                "example": {"q": "The temperate grasslands of South Africa are called?", "solution": "Veld."},
            },
            {
                "title": "Lake superlatives",
                "body": "**Caspian** largest (salt), **Superior** largest freshwater, **Baikal** deepest, **Titicaca** highest navigable, **Dead Sea** lowest.",
                "example": None,
            },
        ],
        "mistakes": [
            "Calling the Sahara the largest desert overall — Antarctica is; Sahara is the largest hot desert.",
            "Saying the Amazon is the longest river — it carries the most water; the Nile is the longest.",
            "Placing the Veld in South America — it is in South Africa.",
        ],
    },
    {
        "id": "wg-countries",
        "title": "Nicknames and boundary lines",
        "concept": C_COUNTRIES,
        "formulas": [],
        "tricks": [
            {
                "title": "Sun pair",
                "body": "**Rising** Sun = **Japan** (east of Asia, first sunrise); **Midnight** Sun = **Norway** (Arctic summer).",
                "example": None,
            },
            {
                "title": "Line → neighbours: 'Radcliffe-Rift, McMahon-Mountains, Durand-Afghan'",
                "body": "Radcliffe partitioned **India–Pakistan**, McMahon runs along the Himalayas with **China**, Durand divides **Pakistan–Afghanistan**.",
                "example": {"q": "The Durand Line separates which countries?", "solution": "Pakistan and Afghanistan."},
            },
        ],
        "mistakes": [
            "Assigning the Durand Line to India–Afghanistan — today it is the Pakistan–Afghanistan border.",
            "Confusing Finland (thousand lakes) with Norway (midnight sun).",
            "Placing the 38th parallel between the two Vietnams — it divides the Koreas; Vietnam was split at the 17th.",
        ],
    },
]

PYQ = [
    {"pattern": "Local wind → region", "frequency": "very common", "howToSpot": "'Chinook blows in...', 'Which wind is called the Doctor?'", "approach": "Use the wind–country list; watch the warm vs cold trap."},
    {"pattern": "Planet superlatives", "frequency": "very common", "howToSpot": "'Which planet is called the red planet / hottest / has most prominent rings?'", "approach": "Recite the one-line superlatives; Venus-hottest is the favourite trap."},
    {"pattern": "Strait / canal connects", "frequency": "common", "howToSpot": "'The Strait of Gibraltar connects...'", "approach": "Name the two countries and two water bodies for each strait."},
    {"pattern": "Atmosphere layer features", "frequency": "common", "howToSpot": "'Ozone layer is in...', 'Radio waves are reflected by...'", "approach": "Layer order mnemonic with one tag per layer."},
    {"pattern": "Grassland / tribe / nickname match", "frequency": "common", "howToSpot": "'Pampas are found in...', 'Land of Midnight Sun...'", "approach": "Flashcard tables; eliminate by continent."},
    {"pattern": "Interior of Earth and earthquakes", "frequency": "occasional", "howToSpot": "'Moho discontinuity lies between...', 'Richter scale measures...'", "approach": "Discontinuity mnemonic and P/S-wave behaviour."},
    {"pattern": "Ocean currents and fishing grounds", "frequency": "occasional", "howToSpot": "'Which is a cold current?', 'Grand Banks lie near...'", "approach": "Split warm vs cold lists; cold = west coast in subtropics."},
    {"pattern": "Longitude–time calculation", "frequency": "occasional", "howToSpot": "Two places with longitudes and one time given.", "approach": "Difference in degrees × 4 minutes; east is ahead."},
]

SOLVED = [
    Q("wg-ex01",
      "Which planet is known as the 'Earth's twin' and is also the hottest planet of the solar system?",
      ["Mercury", "Mars", "Venus", "Jupiter"],
      2,
      "**Venus** has nearly the same size and mass as the Earth (hence 'twin'). Its thick carbon dioxide atmosphere causes a runaway greenhouse effect, making it hotter than Mercury even though Mercury is closer to the Sun.",
      "Greenhouse beats distance: Venus > Mercury in temperature.",
      "easy", "wg-earth-universe", "planet superlatives", 20),
    Q("wg-ex02",
      "If it is 10:00 a.m. at a place on 15°W, what is the local time at a place on 75°E?",
      ["4:00 p.m.", "3:00 p.m.", "5:00 p.m.", "2:00 p.m."],
      0,
      "Longitude difference = 15 + 75 = **90°** (they are on opposite sides of Greenwich, so add). Time difference = 90 × 4 = 360 min = **6 hours**. The eastern place is ahead: 10:00 a.m. + 6 h = **4:00 p.m.**",
      "Opposite sides → add degrees; divide by 15 for hours: 90/15 = 6 h.",
      "medium", "wg-earth-universe", "longitude–time calculation", 45),
    Q("wg-ex03",
      "The Chinook, a warm and dry wind known as the 'snow eater', blows along the eastern slopes of the:",
      ["Alps", "Andes", "Rocky Mountains", "Atlas Mountains"],
      2,
      "The **Chinook** descends the eastern (leeward) slopes of the **Rocky Mountains** in the USA and Canada. It warms by compression and melts snow quickly. The similar wind of the **Alps** is the **Foehn**.",
      "Chinook — a Native American name → North America → Rockies.",
      "easy", "wg-atmosphere", "local wind → region", 20),
    Q("wg-ex04",
      "The Strait of Hormuz connects which two water bodies?",
      ["Red Sea and Gulf of Aden", "Persian Gulf and Gulf of Oman", "Black Sea and Sea of Marmara", "Mediterranean Sea and Atlantic Ocean"],
      1,
      "The **Strait of Hormuz** lies between **Iran** and **Oman** and links the **Persian Gulf** to the **Gulf of Oman** (Arabian Sea) — a key oil route. Red Sea–Gulf of Aden is Bab-el-Mandeb; Black Sea–Marmara is Bosphorus; Mediterranean–Atlantic is Gibraltar.",
      None,
      "medium", "wg-oceans", "strait connects", 25),
]

PRACTICE = [
    Q("wg-q01",
      "Which planet has the largest moon of the solar system, Ganymede?",
      ["Saturn", "Jupiter", "Uranus", "Neptune"],
      1,
      "**Ganymede**, a moon of **Jupiter**, is the largest natural satellite in the solar system — bigger than Mercury. Saturn's largest moon is Titan.",
      None, "easy", "wg-earth-universe", "planet superlatives", 20),
    Q("wg-q02",
      "On which date does the Northern Hemisphere experience its longest day?",
      ["21 March", "21 June", "23 September", "22 December"],
      1,
      "On **21 June** (summer solstice) the Sun is overhead at the **Tropic of Cancer**, giving the Northern Hemisphere its longest day. 21 March and 23 September are equinoxes; 22 December is the winter solstice.",
      None, "easy", "wg-earth-universe", "solstice and equinox", 20),
    Q("wg-q03",
      "A traveller crossing the International Date Line from east to west (for example, from the USA to Japan) will:",
      ["repeat the same day", "gain one day on the calendar", "lose one hour", "see no change in date"],
      1,
      "Moving **westward** across the IDL the calendar jumps **one day ahead** (e.g. Monday becomes Tuesday). Moving eastward the date goes back one day, so a day is repeated.",
      "West-bound = skip ahead a day; East-bound = repeat a day.", "medium", "wg-earth-universe", "International Date Line", 25),
    Q("wg-q04",
      "The boundary between the Earth's crust and the mantle is called the:",
      ["Gutenberg discontinuity", "Lehmann discontinuity", "Mohorovičić discontinuity", "Conrad discontinuity"],
      2,
      "The **Mohorovičić (Moho) discontinuity** separates the crust from the mantle. Gutenberg separates mantle and core, Lehmann separates outer and inner core, and Conrad lies within the crust.",
      "'Come Make Good Lunch' — Moho is second.", "easy", "wg-interior-landforms", "interior discontinuities", 20),
    Q("wg-q05",
      "Marble is a metamorphic rock formed from which rock?",
      ["Sandstone", "Shale", "Granite", "Limestone"],
      3,
      "Heat and pressure recrystallise **limestone** (calcium carbonate) into **marble**. Sandstone becomes quartzite, shale becomes slate and granite becomes gneiss.",
      None, "easy", "wg-interior-landforms", "rock transformation", 20),
    Q("wg-q06",
      "Which seismic waves cannot travel through liquids?",
      ["P-waves", "S-waves", "Surface waves", "Both P- and S-waves"],
      1,
      "**S-waves** (secondary, transverse) cannot pass through liquids. Their absence beyond about 103° from the epicentre (the S-wave shadow zone) showed that the **outer core is liquid**. P-waves pass through all states.",
      None, "medium", "wg-interior-landforms", "seismic waves", 25),
    Q("wg-q07",
      "The ozone layer, which absorbs harmful ultraviolet radiation, lies mainly in the:",
      ["Troposphere", "Mesosphere", "Stratosphere", "Thermosphere"],
      2,
      "The **ozone layer** lies in the **stratosphere** (roughly 15–35 km). The troposphere has weather, the mesosphere burns meteors and the thermosphere contains the ionosphere.",
      None, "easy", "wg-atmosphere", "atmosphere layers", 20),
    Q("wg-q08",
      "The dry, dusty Harmattan wind, locally called 'The Doctor', blows over:",
      ["West Africa", "Egypt", "Southern France", "California"],
      0,
      "The **Harmattan** blows from the Sahara over **West Africa** towards the Guinea coast. Its dryness brings relief from humid heat, hence 'The Doctor'. Egypt has the Khamsin, France the Mistral and California the Santa Ana.",
      None, "medium", "wg-atmosphere", "local wind → region", 20),
    Q("wg-q09",
      "Tropical cyclones in the north-west Pacific Ocean (near China, Japan and the Philippines) are called:",
      ["Hurricanes", "Typhoons", "Willy-willies", "Tornadoes"],
      1,
      "They are **typhoons**. The same kind of storm is a **hurricane** in the Atlantic/Caribbean and a **cyclone** in the Indian Ocean. A tornado is a small land funnel, not a tropical cyclone.",
      None, "easy", "wg-atmosphere", "cyclone names", 20),
    Q("wg-q10",
      "Which of the following is a cold ocean current?",
      ["Gulf Stream", "Kuroshio", "Humboldt (Peru) Current", "Agulhas Current"],
      2,
      "The **Humboldt (Peru) Current** flows north along the west coast of South America and is **cold**; it supports rich fisheries and helps create the Atacama desert. Gulf Stream, Kuroshio and Agulhas are warm currents.",
      "Cold currents hug western coasts in the subtropics.", "medium", "wg-oceans", "warm vs cold current", 20),
    Q("wg-q11",
      "The Strait of Gibraltar separates which two countries?",
      ["Spain and Morocco", "Italy and Tunisia", "France and Algeria", "Portugal and Morocco"],
      0,
      "The **Strait of Gibraltar** lies between **Spain** (Europe) and **Morocco** (Africa) and links the Mediterranean Sea with the Atlantic Ocean.",
      None, "easy", "wg-oceans", "strait connects", 20),
    Q("wg-q12",
      "Which is the deepest lake in the world?",
      ["Lake Superior", "Caspian Sea", "Lake Baikal", "Lake Titicaca"],
      2,
      "**Lake Baikal** in Siberia (Russia) is the deepest and oldest lake and holds the largest volume of fresh water. The Caspian is the largest lake by area, Superior the largest freshwater lake by area and Titicaca the highest navigable lake.",
      None, "medium", "wg-continents", "lake superlatives", 20),
    Q("wg-q13",
      "The temperate grasslands of Argentina are known as:",
      ["Prairies", "Pampas", "Steppes", "Downs"],
      1,
      "The **Pampas** are the temperate grasslands of **Argentina** (and Uruguay). Prairies are in North America, Steppes in Eurasia and Downs in Australia.",
      None, "easy", "wg-continents", "grassland → region", 20),
    Q("wg-q14",
      "Which country is known as the 'Land of the Midnight Sun'?",
      ["Finland", "Japan", "Norway", "Iceland"],
      2,
      "**Norway** lies largely north of the Arctic Circle, where the Sun stays visible at midnight in summer. Finland is the 'Land of Thousand Lakes' and Japan the 'Land of the Rising Sun'.",
      None, "easy", "wg-countries", "country nickname", 15),
    Q("wg-q15",
      "The Durand Line forms the boundary between:",
      ["India and China", "India and Pakistan", "Pakistan and Afghanistan", "India and Nepal"],
      2,
      "The **Durand Line** (1893, drawn by Sir Mortimer Durand) marks the **Pakistan–Afghanistan** border. India–China is the McMahon Line and India–Pakistan is the Radcliffe Line.",
      None, "easy", "wg-countries", "boundary line", 20),
]

place(PRACTICE, [1, 3, 0, 2, 3, 1, 0, 2, 3, 1, 0, 2, 1, 3, 0])

topic = {
    "id": "world-geography",
    "sectionId": "ga",
    "title": "World Geography",
    "importance": "medium",
    "avgQuestions": {"tier1": 1, "tier2": 1},
    "summary": "Solar system, Earth's motions and time, interior and rocks, atmosphere and winds, oceans and currents, continental superlatives and boundary lines. CGL usually asks one question here — local winds, planets, straits and 'largest/longest' facts dominate.",
    "subtopics": SUBTOPICS,
    "pyqPatterns": PYQ,
    "solvedExamples": SOLVED,
    "practice": PRACTICE,
}

if __name__ == "__main__":
    save_topic(topic)
