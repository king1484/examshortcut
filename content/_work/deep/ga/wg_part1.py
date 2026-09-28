"""world-geography deep content - part 1: wg-earth-universe, wg-interior-landforms, wg-atmosphere."""
import os
import sys

sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
from _lib import Sub
from wg_notes import NOTES


def build_universe():
    S = Sub("wg-earth-universe")
    S.notes = NOTES["wg-earth-universe"].strip()
    S.pattern("ga-wu-p1", "Planet superlatives and pairs", "very common",
        "'Which is the largest/hottest/brightest planet?', 'Earth's twin', 'red planet', 'planet with rings', planet-property match-the-column.",
        None,
        "1. Size ladder: Jupiter > Saturn > Uranus > Neptune > Earth > Venus > Mars > Mercury.\n2. Venus - hottest, brightest, Morning/Evening Star, 'Earth's twin', rotates east to west; Mars - red planet with Olympus Mons; Saturn - rings, least dense.\n3. For match-the-column, fix one anchor per planet and eliminate; 'largest satellite' (Ganymede) belongs to Jupiter, second largest (Titan) to Saturn.",
        "Which planet is known as the 'Earth's twin' because of its similar size and mass?",
        "**Venus**. It is also the hottest planet (thick CO2) and the brightest, called the Morning/Evening Star.")
    S.pattern("ga-wu-p2", "The Moon: distance, motions and landings", "common",
        "'How far is the Moon', 'why does the Moon always show the same face', first man on the Moon, the Moon's atmosphere.",
        None,
        "1. Distance about **3.84 lakh km**; the Moon is Earth's only natural satellite.\n2. Its **rotation period equals its revolution period (about 27.3 days)** - hence the same face always faces Earth.\n3. It has practically **no atmosphere**; Neil Armstrong stepped on it on **20 July 1969** (Apollo 11).",
        "Why do we always see the same face of the Moon?",
        "Because the Moon's **rotation on its axis takes the same time (about 27.3 days) as its revolution** around the Earth.")
    S.pattern("ga-wu-p3", "Equinoxes, solstices and the overhead Sun", "very common",
        "'Longest/shortest day', 'the Sun is overhead the Tropic of Cancer on', 'when is day and night equal', dates with hemisphere effects.",
        None,
        "1. Solstices: **21 June** (longest day in the N. Hemisphere; Sun overhead Tropic of Cancer) and **22 December** (shortest day; Sun overhead Tropic of Capricorn).\n2. Equinoxes: **21 March** and **23 September** - day and night equal everywhere.\n3. The hemisphere rule: what is summer in the north is winter in the south; on the equator days stay about 12 hours.",
        "On which date is the Sun vertically overhead the Tropic of Capricorn?",
        "**22 December** - the winter solstice of the Northern Hemisphere (its shortest day) and the height of summer in the south.")
    S.pattern("ga-wu-p4", "Rotation vs revolution and their effects", "very common",
        "'Rotation causes', 'length of the sidereal day', 'why a leap year', perihelion and aphelion dates.",
        None,
        "1. **Rotation** (once in 23 h 56 min 4 s) causes day-night, the Sun's apparent eastward rise, tides (partly) and wind deflection.\n2. **Revolution** (365 d 6 h 9 min) with the 23.5-degree tilt causes the **seasons**; the extra 6 h gives a leap year every 4 years.\n3. Perihelion (nearest Sun) - **3 January**; aphelion (farthest) - **4 July**. In questions, separate 'day and night' (rotation) from 'seasons' (revolution).",
        "Why is a leap year observed every fourth year?",
        "The Earth takes **365 days 6 hours 9 minutes** to revolve; the leftover 6 hours collects into one extra day (29 February) every four years.")
    S.pattern("ga-wu-p5", "Longitudes, time zones and the IDL", "very common",
        "Time difference between two longitudes, IST-GMT relation, adding/losing a day across the IDL, count of latitudes/meridians.",
        "1^{\\circ}\\text{ of longitude} = 4\\text{ minutes of time}",
        "1. The Earth turns 360 degrees in 24 hours, so **1 degree = 4 minutes**; 15 degrees = 1 hour.\n2. East of Greenwich is ahead, west behind; IST is based on 82.5 E = **GMT + 5 h 30 min**.\n3. The **IDL** follows about 180 degrees: crossing **east to west (towards Asia) add a day**, west to east lose a day.",
        "Two places lie 30 degrees of longitude apart. What is the difference in their local time?",
        "30 x 4 minutes = **120 minutes = 2 hours**; the eastern place is ahead.")

    S.q("ga-wu-p1", "easy", "Which planet of the solar system is the **hottest**?",
        ["Mercury", "Venus", "Mars", "Jupiter"], "Venus",
        "**Venus** is the hottest planet because its thick carbon-dioxide atmosphere traps heat (runaway greenhouse effect); its surface is hotter even than Mercury's.",
        "Closest to the Sun is Mercury; hottest is Venus.", 15)
    S.q("ga-wu-p1", "medium", "Which planet is called the **Morning Star** and the **Evening Star**?",
        ["Mars", "Jupiter", "Venus", "Mercury"], "Venus",
        "**Venus** is the brightest planet and, seen near the horizon before sunrise or after sunset, was called the Morning and Evening Star.",
        None, 20)
    S.q("ga-wu-p1", "medium", "Which planet rotates on its axis from **east to west**, opposite to most planets?",
        ["Venus", "Earth", "Saturn", "Neptune"], "Venus",
        "**Venus** spins retrograde - east to west - so its Sun rises in the west. Uranus rolls on its side; the rest rotate west to east.",
        None, 25)
    S.q("ga-wu-p1", "hard", "Which planet is the **least dense** - so light it would float on water?",
        ["Jupiter", "Saturn", "Uranus", "Neptune"], "Saturn",
        "**Saturn's** density (about 0.7 g/cm3) is less than that of water. Its famous rings are pieces of ice and rock.",
        None, 25)
    S.q("ga-wu-p1", "medium", "The largest volcano of the solar system, **Olympus Mons**, is on which planet?",
        ["Earth", "Mars", "Venus", "Mercury"], "Mars",
        "**Olympus Mons** rises on **Mars**, the 'Red Planet' (its colour comes from iron-oxide dust). Mars has two small moons, Phobos and Deimos.",
        None, 20)
    S.q("ga-wu-p2", "easy", "The average distance of the Moon from the Earth is about:",
        ["38,400 km", "3,84,000 km", "38,40,000 km", "3.84 crore km"], "3,84,000 km",
        "The Moon is about **3,84,000 km (3.84 lakh km)** away - light takes about 1.3 seconds to cross that gap.",
        None, 15)
    S.q("ga-wu-p2", "medium", "The Moon has practically no atmosphere because:",
        ["It is too far from the Sun", "Its gravity is too weak to hold gases", "Solar winds removed only oxygen", "It never had volcanic activity"], "Its gravity is too weak to hold gases",
        "The Moon's small mass gives it very weak gravity, so it cannot retain an atmosphere; hence the sky is black even in daytime and astronauts' footprints last for ages.",
        None, 25)
    S.q("ga-wu-p2", "medium", "Who was the first human being to walk on the Moon, in July 1969?",
        ["Yuri Gagarin", "Neil Armstrong", "Buzz Aldrin", "Michael Collins"], "Neil Armstrong",
        "**Neil Armstrong** of Apollo 11 stepped onto the Moon on **20 July 1969** in the Sea of Tranquility; Buzz Aldrin followed, while Michael Collins orbited above.",
        None, 20)
    S.q("ga-wu-p3", "easy", "The Sun is vertically overhead the **Tropic of Cancer** on:",
        ["21 March", "21 June", "23 September", "22 December"], "21 June",
        "On **21 June**, the summer solstice, the Sun stands overhead the Tropic of Cancer and the Northern Hemisphere has its longest day.",
        None, 15)
    S.q("ga-wu-p3", "medium", "The Northern Hemisphere has its **shortest day** on:",
        ["21 March", "21 June", "23 September", "22 December"], "22 December",
        "On **22 December** (winter solstice) the Sun is overhead the Tropic of Capricorn; the north has its shortest day while the south enjoys midsummer.",
        None, 20)
    S.q("ga-wu-p3", "medium", "On the **equator**, the length of day and night through the year is:",
        ["Longer days in summer months", "About 12 hours each, all year", "Decided by the moon's phase", "Always more day than night"], "About 12 hours each, all year",
        "The circle of illumination always bisects the equator, so days and nights stay roughly equal there; the contrast grows towards the poles.",
        None, 25)
    S.q("ga-wu-p4", "easy", "Day and night on the Earth are caused by:",
        ["Revolution", "Rotation", "Tilt of the axis", "Revolution plus tilt"], "Rotation",
        "The Earth's **rotation** on its axis once in about 24 hours turns one half towards the Sun (day) and the other away (night). Revolution causes the seasons.",
        None, 15)
    S.q("ga-wu-p4", "medium", "The exact time the Earth takes for one rotation with respect to the stars (the sidereal day) is:",
        ["24 hours exactly", "23 hours 56 minutes 4 seconds", "23 hours 52 minutes", "24 hours 4 minutes"], "23 hours 56 minutes 4 seconds",
        "The **sidereal day is 23 h 56 min 4 s**; the solar day we use averages 24 hours because the Earth also moves along its orbit.",
        None, 25)
    S.q("ga-wu-p4", "medium", "Earth is **nearest** to the Sun (perihelion) on:",
        ["21 June", "3 January", "4 July", "23 September"], "3 January",
        "**Perihelion falls on 3 January** (about 147 million km); aphelion, the farthest point (152 million km), comes on 4 July - so the north's winter happens near the nearest point.",
        None, 25)
    S.q("ga-wu-p5", "easy", "Indian Standard Time is ahead of GMT by:",
        ["4 hours 30 minutes", "5 hours", "5 hours 30 minutes", "6 hours"], "5 hours 30 minutes",
        "IST is based on the 82.5 E meridian: 82.5 x 4 minutes = 330 minutes = **5 h 30 min** ahead of Greenwich.",
        None, 15)
    S.q("ga-wu-p5", "medium", "A traveller flying **east across the International Date Line** (from Asia towards America) must:",
        ["Add one day to the date", "Subtract (lose) one day", "Change nothing", "Set the clock back 12 hours"], "Subtract (lose) one day",
        "Across the IDL: going **east, lose a day**; going west (towards Asia), add a day. The line bends around islands so that no country is split into two dates.",
        None, 25)
    S.q("ga-wu-p5", "hard", "If the local time of place A (60 E) is 12 noon, what is the local time of place B (90 E)?",
        ["10 a.m.", "12 noon", "2 p.m.", "3 p.m."], "2 p.m.",
        "B lies 30 degrees **east** of A, so it is ahead: 30 x 4 min = 120 min = 2 hours. Local time at B = 12 noon + 2 h = **2 p.m.**",
        "East = ahead. Degrees x 4 = minutes.", 35)
    return S


def build_interior():
    S = Sub("wg-interior-landforms")
    S.notes = NOTES["wg-interior-landforms"].strip()
    S.pattern("ga-wi-p1", "Layers of the Earth and discontinuities", "very common",
        "'The boundary between crust and mantle is', 'which layer is made of nickel and iron', 'SiAl/SiMa/NiFe', ordering of Conrad-Moho-Repetti-Gutenberg-Lehmann.",
        None,
        "1. Layers: **crust (SiAl/SiMa) - mantle - core (NiFe)**; outer core liquid, inner core solid.\n2. Discontinuities top to bottom: **Conrad (in crust), Moho (crust-mantle), Repetti (in mantle), Gutenberg (mantle-outer core), Lehmann (outer-inner core)** - 'Come Make Good Lunch'.\n3. Continental crust is lighter and thicker; oceanic crust is denser basalt.",
        "The Gutenberg discontinuity separates which two layers of the Earth?",
        "The **mantle from the outer core** (about 2,900 km deep). Moho separates crust from mantle; Lehmann divides the two cores.")
    S.pattern("ga-wi-p2", "Seismic waves and earthquake vocabulary", "very common",
        "'Which wave cannot pass through liquid', focus vs epicentre, Richter vs Mercalli, seismograph, 'Ring of Fire'.",
        None,
        "1. Waves: **P** fastest (passes all matter), **S** stops in liquids (proves the outer core is molten), **L** surface waves - slowest, most destructive.\n2. **Focus** = origin inside; **epicentre** = surface point above it; waves recorded on a **seismograph**.\n3. Magnitude = **Richter** scale; damage intensity = **Mercalli** scale. About 80% of earthquakes strike the **Circum-Pacific 'Ring of Fire'**.",
        "The point inside the Earth where an earthquake originates is called the:",
        "**Focus (hypocentre)**. The point on the surface directly above it - where the shock is felt first and strongest - is the **epicentre**.")
    S.pattern("ga-wi-p3", "Rock families and metamorphic pairs", "very common",
        "'Marble is formed from', 'fossils are found in which rock', 'which is an igneous rock', classify a list of rocks.",
        None,
        "1. Three families: **igneous** (cooled magma - granite, basalt), **sedimentary** (strata, the only rocks with fossils - limestone, sandstone, shale, coal), **metamorphic** (changed by heat-pressure).\n2. Metamorphic pairs: limestone-marble, sandstone-quartzite, shale-slate, granite-gneiss.\n3. Igneous rocks are the oldest 'primary' rocks; sedimentary rocks cover most of the land surface and hold coal and oil.",
        "Slate, used for roofing, is a metamorphic rock formed from which parent rock?",
        "**Shale**. The other classic pairs: limestone-marble, sandstone-quartzite, granite-gneiss.")
    S.pattern("ga-wi-p4", "Volcanoes: activity, shape and famous names", "common",
        "'India's only active volcano', 'Lighthouse of the Mediterranean', shield vs composite volcano, Krakatoa/Vesuvius events.",
        None,
        "1. Activity: **active** (Barren Island - India's only one; Stromboli; Etna; Vesuvius), **dormant** (Fuji), **extinct**.\n2. Shape: **shield** (broad, fluid lava - Mauna Loa, Hawaii), **composite/strato** (steep, alternating layers - Fuji, Vesuvius), **caldera** (collapsed crater).\n3. Volcanoes cluster in the **Ring of Fire** and along mid-ocean ridges; Krakatoa (Indonesia, 1883) is the classic explosive eruption.",
        "Stromboli, often called the 'Lighthouse of the Mediterranean', is a/an:",
        "**Active volcano** (in the Aeolian islands, Italy) - its regular night glow guided sailors for centuries.")
    S.pattern("ga-wi-p5", "Mountain and landform types", "common",
        "'Young fold mountains are', 'rift valley is formed by', block mountains with faults, highest/largest plateaus.",
        None,
        "1. **Fold** mountains - squeezed crust; young folds (Himalaya, Alps, Andes, Rockies) are the highest, old folds (Aravallis, Urals) are worn down.\n2. **Block** mountains - raised fault blocks (Vosges, Black Forest); **rift valleys** - sunken blocks between faults (Rhine valley, East African rift).\n3. **Plateau** = raised flatland (Tibet highest and largest); **plain** = low, flat, fertile, most populated.",
        "The Rhine valley and the East African rifts are examples of:",
        "**Rift valleys** - long, narrow sunken blocks (graben) formed where land has dropped between parallel faults.")

    S.q("ga-wi-p1", "easy", "Which layer of the Earth is made mainly of **nickel and iron**?",
        ["Crust", "Mantle", "Core", "Asthenosphere"], "Core",
        "The **core (NiFe)** is iron-nickel; the outer core is liquid and the inner core solid. SiAl/SiMa describe the crust; the mantle is iron-magnesium silicate rock.",
        None, 15)
    S.q("ga-wi-p1", "medium", "The **Mohorovicic (Moho) discontinuity** separates:",
        ["Outer core from inner core", "Mantle from core", "Crust from mantle", "Upper crust from lower crust"], "Crust from mantle",
        "**Moho = crust-mantle boundary** (1909). Gutenberg separates mantle and outer core; Conrad lies within the crust; Lehmann splits the two cores.",
        None, 20)
    S.q("ga-wi-p1", "hard", "Which of the following discontinuities lies **within the mantle**?",
        ["Conrad", "Moho", "Repetti", "Gutenberg"], "Repetti",
        "**Repetti** divides the upper and lower mantle. Conrad is inside the crust, Moho is crust-mantle, Gutenberg is mantle-core, Lehmann is between the cores.",
        None, 30)
    S.q("ga-wi-p2", "easy", "Earthquake waves are recorded by an instrument called the:",
        ["Barograph", "Seismograph", "Hydrograph", "Anemometer"], "Seismograph",
        "A **seismograph** records the shock waves. Richter and Mercalli are scales for magnitude and damage, not instruments.",
        None, 15)
    S.q("ga-wi-p2", "medium", "The energy released by an earthquake (its magnitude) is measured on the:",
        ["Mercalli scale", "Richter scale", "Fujita scale", "Beaufort scale"], "Richter scale",
        "**Richter scale** = magnitude (energy). **Mercalli** = intensity of damage at a place. (Fujita rates tornadoes; Beaufort rates wind.)",
        None, 20)
    S.q("ga-wi-p2", "medium", "Which seismic waves are the **last to arrive** but cause the greatest destruction?",
        ["P-waves", "S-waves", "L-waves (surface waves)", "All arrive together"], "L-waves (surface waves)",
        "**L-waves** travel along the surface, arrive last, and shake buildings the most. P-waves are fastest; S-waves cannot cross liquids.",
        None, 25)
    S.q("ga-wi-p2", "hard", "About what share of the world's earthquakes occurs in the Circum-Pacific 'Ring of Fire'?",
        ["About 40%", "About 60%", "About 80%", "About 95%"], "About 80%",
        "Roughly **80%** of the world's largest earthquakes - and most volcanoes - occur along the ring of subduction zones fringing the Pacific Ocean.",
        None, 25)
    S.q("ga-wi-p3", "easy", "Fossils of plants and animals are found only in which type of rock?",
        ["Igneous", "Sedimentary", "Metamorphic", "All equally"], "Sedimentary",
        "Only **sedimentary rocks** form in layers at the surface, where living remains can be buried; heat and pressure in other rocks destroy them.",
        None, 15)
    S.q("ga-wi-p3", "medium", "Quartzite is the metamorphic form of which rock?",
        ["Limestone", "Shale", "Sandstone", "Granite"], "Sandstone",
        "**Sandstone - quartzite**. Limestone turns to marble, shale to slate, granite to gneiss.",
        None, 20)
    S.q("ga-wi-p3", "medium", "Granite and basalt are examples of which family of rocks?",
        ["Sedimentary", "Metamorphic", "Igneous", "Fossiliferous"], "Igneous",
        "**Igneous** rocks cool from magma or lava: granite (intrusive/plutonic, large crystals) and basalt (extrusive/volcanic, as on ocean floors and the Deccan).",
        None, 20)
    S.q("ga-wi-p3", "hard", "Which of the following is correctly matched?",
        ["Marble - metamorphosed sandstone", "Slate - metamorphosed shale", "Gneiss - metamorphosed limestone", "Quartzite - metamorphosed granite"], "Slate - metamorphosed shale",
        "**Slate comes from shale.** Marble is from limestone, gneiss from granite, quartzite from sandstone - the classic four pairs.",
        None, 30)
    S.q("ga-wi-p4", "medium", "**Barren Island**, India's only active volcano, lies in which water body?",
        ["Arabian Sea", "Bay of Bengal", "Andaman Sea", "Indian Ocean near Lakshadweep"], "Andaman Sea",
        "**Barren Island** in the **Andaman Sea** (Andaman & Nicobar Islands) erupted again from 1991 onwards; nearby Narcondam is dormant.",
        None, 20)
    S.q("ga-wi-p4", "medium", "Which of these is a **shield volcano** with broad, gently sloping sides of fluid lava?",
        ["Mount Fuji", "Mauna Loa (Hawaii)", "Mount Vesuvius", "Barren Island"], "Mauna Loa (Hawaii)",
        "**Mauna Loa** (Hawaii) is the classic shield volcano. Fuji and Vesuvius are steep composite (strato) volcanoes built of alternating lava and ash.",
        None, 25)
    S.q("ga-wi-p4", "easy", "Mount Vesuvius, whose 79 AD eruption buried the Roman town of Pompeii, is located in:",
        ["Greece", "Italy", "Turkey", "Spain"], "Italy",
        "**Vesuvius** stands near Naples, **Italy**; Pompeii lay under its ash. Etna (Sicily) and Stromboli are Italy's other famous volcanoes.",
        None, 15)
    S.q("ga-wi-p5", "easy", "The Himalayas, the Alps and the Andes are examples of:",
        ["Block mountains", "Volcanic mountains", "Young fold mountains", "Residual mountains"], "Young fold mountains",
        "They rose in the recent geological past where plates collided, so they are **young fold mountains** - the highest ranges on Earth. The Aravallis are old, worn folds.",
        None, 15)
    S.q("ga-wi-p5", "medium", "The Vosges and the Black Forest, raised between two faults, are examples of:",
        ["Fold mountains", "Block mountains", "Volcanic mountains", "Dome mountains"], "Block mountains",
        "**Block mountains** (horsts) rise between parallel faults while rift valleys (graben) sink - as on either side of the Rhine rift.",
        None, 25)
    S.q("ga-wi-p5", "medium", "Which is the highest and largest plateau in the world?",
        ["Deccan Plateau", "Tibetan Plateau", "Brazilian Plateau", "Colorado Plateau"], "Tibetan Plateau",
        "The **Tibetan Plateau** ('the roof of the world', averaging over 4,500 m) is the highest and largest; the Pamir Knot, where ranges meet, lies at its western end.",
        None, 20)
    return S


def build_atmosphere():
    S = Sub("wg-atmosphere")
    S.notes = NOTES["wg-atmosphere"].strip()
    S.pattern("ga-wa-p1", "Composition and layers of the atmosphere", "very common",
        "'Which gas is most abundant', 'weather occurs in which layer', lapse-rate and layer-feature questions, aurora/ozone/meteor placement.",
        None,
        "1. Dry air: **N2 78%, O2 21%, Ar 0.93%, CO2 0.04%**; water vapour and dust vary.\n2. Layers bottom-up: **Troposphere** (all weather; lapse rate 6.5 C/km) - **Stratosphere** (ozone 15-35 km; jets) - **Mesosphere** (meteors burn; coldest) - **Thermosphere/Ionosphere** (aurora, radio reflection, ISS) - **Exosphere**.\n3. Place each fact in its layer before looking at options.",
        "The normal lapse rate - the fall of temperature with height in the troposphere - is about:",
        "**6.5 degrees C per km.** All weather is confined to the troposphere, whose top (tropopause) lies at 8 km over the poles and 18 km over the equator.")
    S.pattern("ga-wa-p2", "Ozone layer and environmental facts", "common",
        "'Ozone hole appears over', 'Montreal Protocol', 'which gas absorbs ultraviolet rays', CFC questions.",
        None,
        "1. **Ozone (O3)** in the stratosphere (15-35 km) absorbs harmful UV rays; it is a trace gas, not a layer of pure gas.\n2. The 'ozone hole' appears seasonally over **Antarctica** (first reported 1985); the main culprits are **CFCs**.\n3. The **Montreal Protocol (1987)** phased out CFCs, and the layer is slowly recovering.",
        "The ozone hole was first detected over which region?",
        "**Antarctica** - a springtime thinning of the ozone layer, blamed mainly on man-made **CFCs** and checked by the Montreal Protocol of 1987.")
    S.pattern("ga-wa-p3", "Pressure belts and planetary winds", "very common",
        "'Doldrums lie at', 'Roaring Forties are', 'trade winds blow from', horse latitudes, ITCZ, wind deflection.",
        None,
        "1. Belts: equatorial **low (Doldrums)**, subtropical **high (Horse latitudes)**, subpolar low, polar high; deserts sit under the subtropical highs.\n2. Winds: **trades** (NE in the north, SE in the south, towards the equator), **westerlies** (35-60 degrees; southern ones = Roaring Forties, Furious Fifties, Shrieking Sixties), polar easterlies.\n3. Rotation deflects winds right in the Northern and left in the Southern Hemisphere; the **ITCZ** (where trades meet) follows the Sun - the basis of the monsoon.",
        "The 'Roaring Forties' are strong winds found in the:",
        "**Southern Hemisphere westerlies** (40-50 degrees S) - so named because almost unbroken ocean lets them blow at full strength.")
    S.pattern("ga-wa-p4", "Cyclones: names by region and types", "very common",
        "'Typhoons occur in', 'willy-willy is a cyclone of', hurricane/typhoon/cyclone matching, tornado identification, temperate cyclones.",
        None,
        "1. Tropical cyclone names: **Hurricane** - Atlantic/Caribbean and east Pacific; **Typhoon** - China Sea/north-west Pacific; **Willy-Willy** - Australia; **Cyclone** - Indian Ocean.\n2. A **tornado** is a small, violent funnel (USA midwest, 'twister') - not a tropical cyclone.\n3. **Temperate (frontal) cyclones** form in mid-latitudes; India's winter 'western disturbances' are weak temperate systems that rain on Punjab-Haryana.",
        "Tropical cyclones of the China Sea and the north-west Pacific are called:",
        "**Typhoons.** The same storms are hurricanes in the Atlantic and willy-willies off Australia.")
    S.pattern("ga-wa-p5", "Local winds: name ↔ region ↔ character", "very common",
        "'Chinook is a wind of', 'Harmattan is called the Doctor', 'which wind melts snow', hot/cold local wind matching.",
        None,
        "1. Warm: **Loo** (N. India summer), **Sirocco** (Sahara to Italy, red dust), Khamsin (Egypt), **Chinook** ('snow eater', east of the Rockies), **Foehn** (Alps - melts snow, ripens vines), Brickfielder (Australia), Zonda (Argentina).\n2. Cold: **Mistral** (Rhone valley, France), **Bora** (Adriatic), **Blizzard** (snow-laden), Buran (Russia), Pampero (pampas), **Harmattan** (dry, dusty West Africa - 'The Doctor').\n3. Match region first, then hot/cold character; distractors usually come from the other hemisphere.",
        "The warm, dry **Foehn** wind that melts snow on the lee side of mountains blows over which region?",
        "The **Alps** (Europe). Its North American equivalent on the east slope of the Rockies is the **Chinook**, the 'snow eater'.")

    S.q("ga-wa-p1", "easy", "Which is the **most abundant gas** in the Earth's atmosphere?",
        ["Oxygen", "Nitrogen", "Carbon dioxide", "Argon"], "Nitrogen",
        "**Nitrogen makes up about 78%** of dry air, oxygen about 21%, argon 0.93% and CO2 about 0.04%.",
        None, 15)
    S.q("ga-wa-p1", "medium", "Clouds, rain and storms - all weather - are confined to which layer?",
        ["Stratosphere", "Mesosphere", "Troposphere", "Ionosphere"], "Troposphere",
        "Almost all water vapour lies in the **troposphere**, the lowest layer (8-18 km), so all weather happens there. Jet aircraft cruise above it, in the calm stratosphere.",
        None, 20)
    S.q("ga-wa-p1", "hard", "**Meteors** ('shooting stars') mostly burn up in which layer of the atmosphere?",
        ["Troposphere", "Stratosphere", "Mesosphere", "Exosphere"], "Mesosphere",
        "The **mesosphere** (up to 80-85 km) is dense enough to burn incoming meteors by friction - and it is also the coldest layer (about -90 degrees C).",
        None, 30)
    S.q("ga-wa-p2", "easy", "The chemical formula of **ozone** is:",
        ["O2", "O3", "CO2", "H2O2"], "O3",
        "**Ozone is O3** - three oxygen atoms per molecule; it forms a shield in the stratosphere that absorbs ultraviolet rays.",
        None, 15)
    S.q("ga-wa-p2", "medium", "The **Montreal Protocol (1987)** is an international agreement to:",
        ["Cut greenhouse gases", "Phase out ozone-depleting CFCs", "Ban ocean dumping", "Protect wetlands"], "Phase out ozone-depleting CFCs",
        "It phases out **CFCs** and related chemicals that destroy stratospheric ozone - the main cause of the ozone hole over Antarctica.",
        None, 25)
    S.q("ga-wa-p2", "medium", "Which atmospheric layer contains the ozone layer that absorbs ultraviolet radiation, and is therefore favoured by jet aircraft?",
        ["Troposphere", "Stratosphere", "Mesosphere", "Thermosphere"], "Stratosphere",
        "The **stratosphere** holds the ozone layer (15-35 km) and its calm, cloudless air suits long-haul flights.",
        None, 20)
    S.q("ga-wa-p3", "easy", "The equatorial belt of calm, rising air with daily convectional rains is called the:",
        ["Horse latitudes", "Doldrums", "Roaring Forties", "Polar high"], "Doldrums",
        "The **Doldrums** (equatorial low, 0-5 degrees) are hot, humid and windless - sailing ships were often becalmed there. The subtropical high is the 'horse latitudes' belt.",
        None, 15)
    S.q("ga-wa-p3", "medium", "In the Northern Hemisphere, the **north-east trade winds** blow:",
        ["From the equatorial low towards the subtropical high", "From the subtropical high towards the equatorial low", "From the poles towards 60 degrees", "From west to east at 35-60 degrees"], "From the subtropical high towards the equatorial low",
        "Trades flow out of the subtropical highs towards the Doldrums, deflected to become **north-east trades** in the north and **south-east trades** in the south.",
        None, 25)
    S.q("ga-wa-p3", "medium", "Winds are deflected to the **right of their path** in the Northern Hemisphere because of:",
        ["Pressure gradient", "The Earth's rotation (Coriolis effect)", "Friction with land", "Temperature inversion"], "The Earth's rotation (Coriolis effect)",
        "The **Coriolis effect** of the Earth's spin bends moving air right in the north and left in the south - shaping the trades, westerlies and cyclone spirals.",
        None, 25)
    S.q("ga-wa-p4", "easy", "A **tropical cyclone** occurring in the **Atlantic Ocean and Caribbean Sea** is called a:",
        ["Typhoon", "Hurricane", "Willy-Willy", "Tornado"], "Hurricane",
        "Atlantic and east-Pacific storms are **hurricanes**; typhoon is the name in the north-west Pacific, willy-willy off Australia, and simply cyclone in the Indian Ocean.",
        None, 15)
    S.q("ga-wa-p4", "medium", "Which of the following is **NOT** a tropical cyclone?",
        ["Hurricane", "Typhoon", "Tornado", "Willy-Willy"], "Tornado",
        "A **tornado** is a narrow, violently rotating funnel typical of the American midwest - quite different from the broad warm-sea tropical cyclones.",
        None, 20)
    S.q("ga-wa-p4", "hard", "The winter rains of Punjab and Haryana, useful for the rabi crop, come from which weather system?",
        ["Tropical cyclones of the Bay of Bengal", "Temperate depressions called western disturbances", "The retreating monsoon", "Local convectional storms"], "Temperate depressions called western disturbances",
        "**Western disturbances** are weak temperate (frontal) cyclones travelling from the Mediterranean region; they bring gentle winter rain to north-west India and snow to the hills.",
        None, 30)
    S.q("ga-wa-p5", "easy", "The warm, dry **'snow eater'** wind that blows down the eastern slopes of the Rockies in North America is the:",
        ["Loo", "Chinook", "Mistral", "Bora"], "Chinook",
        "The **Chinook** melts the winter snow on the prairie side of the Rockies overnight. The Foehn is its Alpine counterpart.",
        None, 15)
    S.q("ga-wa-p5", "medium", "The **Mistral**, a cold, dry wind that chills the Rhone valley in winter, blows over:",
        ["Spain", "France", "Italy", "Greece"], "France",
        "The **Mistral** funnels down the Rhone valley in southern **France** towards the Mediterranean; the Bora is its cold counterpart on the Adriatic.",
        None, 20)
    S.q("ga-wa-p5", "medium", "The **Sirocco**, a hot wind that carries red dust from the Sahara and sometimes drops 'blood rain' on southern Europe, blows towards:",
        ["West Africa", "Italy and the central Mediterranean", "Argentina", "Central Asia"], "Italy and the central Mediterranean",
        "The **Sirocco** picks up heat and red dust crossing the Sahara and reaches Sicily and southern Italy. The Harmattan blows westward across West Africa.",
        None, 25)
    return S
