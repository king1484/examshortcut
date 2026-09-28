"""Phase-2 deep content for ga/world-geography. Run: py -3 world-geography.py"""
import os
import sys

sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
from _lib import apply_topic
from wg_part1 import build_universe, build_interior, build_atmosphere
from wg_part2 import build_oceans, build_continents, build_countries


def P(pattern, frequency, howToSpot, approach, subtopic, q, sol):
    return {"pattern": pattern, "frequency": frequency, "howToSpot": howToSpot, "approach": approach,
            "subtopic": subtopic, "example": {"q": q, "solution": sol}}


PYQ = [
    P("Planet superlatives", "very common",
      "'Largest/hottest/brightest/smallest planet', 'Earth's twin', 'red planet', 'which planet has rings', 'largest satellite of a planet'.",
      "Hold one anchor fact per planet and eliminate: Mercury smallest, Venus hottest-brightest-retrograde and 'Earth's twin', Mars red with Olympus Mons, Jupiter largest with Ganymede, Saturn ringed and least dense. Superlative questions are almost always about Jupiter, Saturn, Venus or Mars.",
      "wg-earth-universe",
      "Which is the largest planet of the solar system?",
      "**Jupiter** - followed by Saturn, Uranus, Neptune; its Great Red Spot is a giant storm and Ganymede is its (and the solar system's) largest satellite."),
    P("Longitude–time calculation", "occasional",
      "'Two places 15/30/60 degrees apart, what is the time difference?', 'IST is ahead of GMT by', 'crossing the IDL from east to west', '1 degree of longitude equals'.",
      "One formula does it all: 1 degree = 4 minutes, so degrees x 4 = minutes of time; east is ahead, west behind. IST = GMT + 5 h 30 min (82.5 E). Across the International Date Line: travelling eastwards, lose a day; westwards, add a day.",
      "wg-earth-universe",
      "What is the time difference between two places 15 degrees of longitude apart?",
      "**1 hour** (15 x 4 minutes = 60 minutes); the eastern place is ahead of the western one."),
    P("Interior of Earth and earthquakes", "occasional",
      "'Which discontinuity separates crust and mantle', 'which wave cannot pass through liquid', 'focus/epicentre', 'rocks are classified into', 'marble is formed from'.",
      "Two ladders solve this block. Layers top to bottom with their discontinuities - Conrad, Moho (crust-mantle), Repetti, Gutenberg (mantle-core), Lehmann - and waves P (fastest), S (blocked by liquid), L (most destructive). Rocks: igneous-sedimentary-metamorphic with the four pairs limestone-marble, sandstone-quartzite, shale-slate, granite-gneiss.",
      "wg-interior-landforms",
      "Which discontinuity separates the mantle from the core?",
      "The **Gutenberg discontinuity** (about 2,900 km deep). Moho separates the crust from the mantle."),
    P("Atmosphere layer features", "common",
      "'Weather occurs in which layer', 'aurora/ozone/meteors belong to which layer', 'composition of air', 'lapse rate', 'jet planes fly in which layer'.",
      "Place every fact in its layer: troposphere - weather, water vapour, 6.5 C/km lapse; stratosphere - ozone, calm jet routes; mesosphere - meteors burn, coldest; thermosphere/ionosphere - aurora, radio waves, ISS; exosphere - outermost. Composition: N2 78, O2 21, Ar 0.93, CO2 0.04 per cent.",
      "wg-atmosphere",
      "In which layer of the atmosphere do jet aircraft normally fly to avoid weather disturbances?",
      "The **stratosphere** - calm, cloudless air above the tropopause, with the ozone layer (15-35 km) inside it."),
    P("Local wind → region", "very common",
      "'Loo/Chinook/Foehn/Mistral/Sirocco/Harmattan is a wind of which region', 'which wind is called the snow eater/Doctor', warm-vs-cold wind matching.",
      "Learn two buckets per hemisphere pair. Warm: Loo (N. India), Chinook ('snow eater', east of Rockies), Foehn (Alps), Sirocco (Sahara to Italy, red dust), Khamsin (Egypt). Cold: Mistral (Rhone, France), Bora (Adriatic), Blizzard, Buran (Russia), Pampero (Argentina), Harmattan (West Africa, dry dust, 'The Doctor'). Region first, then hot/cold.",
      "wg-atmosphere",
      "The Chinook, known as the 'snow eater', blows down which mountains?",
      "The **Rockies** of North America - its warm dry air melts snow on the eastern (lee) slopes overnight; the Foehn is its Alpine counterpart."),
    P("Strait / canal connects", "common",
      "'Which strait separates X from Y', 'which canal connects two seas', 'Hormuz/Bab-el-Mandeb/Malacca', 'Suez vs Panama canal'.",
      "Fix each strait as four boxes - two lands, two waters: Gibraltar (Spain-Morocco, Atlantic-Mediterranean), Hormuz (Persian Gulf-Oman Gulf), Bab-el-Mandeb (Red Sea-Gulf of Aden), Malacca (Andaman-China seas), Bering (Russia-Alaska), Palk (India-Sri Lanka). Canals: Suez (Egypt, 1869, sea-level, no locks, Mediterranean-Red Sea) vs Panama (1914, locks, Atlantic-Pacific).",
      "wg-oceans",
      "The Suez Canal connects the Mediterranean Sea with the —",
      "**Red Sea.** It runs sea-level through Egypt (opened 1869) with no locks; the Panama Canal (1914) is a lock canal joining the Atlantic and Pacific."),
    P("Ocean currents and fishing grounds", "occasional",
      "'Which is a warm/cold current', 'which current keeps west Europe warm', 'which current causes fog/fishing grounds', 'current responsible for a coastal desert'.",
      "Warm set: Gulf Stream + North Atlantic Drift (west Europe mild), Kuroshio, Brazilian, Agulhas. Cold set: Labrador (Newfoundland fog and icebergs), Canary, Benguela (Namib), Humboldt/Peru (Atacama, anchovies, El Nino), Oyashio. Where warm meets cold - Grand Banks, Dogger Bank - plankton blooms make the great fishing grounds.",
      "wg-oceans",
      "Which cold current flowing along the western coast of South America is linked with the Atacama desert and the anchovy fishery?",
      "The **Humboldt (Peru) current** - cold water chills the coast (Atacama's dryness) yet upwells nutrients for anchovies; its warm-phase reversal is El Nino."),
    P("Grassland / tribe / nickname match", "common",
      "'Prairies/Pampas/Steppes/Veld are grasslands of', 'Pygmies/Bushmen/Masai/Inuit live in', 'Land of Rising Sun/Thousand Lakes/White Elephant', old-name-new-name questions.",
      "Three mini-tables. Grasslands: Prairies-North America, Pampas-Argentina, Steppes-Eurasia, Veld-South Africa, Downs-Australia, Savanna/Llanos/Campos-tropical. Tribes: Pygmies-Congo, Bushmen-Kalahari, Masai-East Africa, Inuit-Arctic, Lapps-Scandinavia, Bedouins-Arabia, Aborigines-Australia. Names: Ceylon-Sri Lanka, Siam-Thailand, Persia-Iran, Constantinople-Istanbul, Gold Coast-Ghana.",
      "wg-continents",
      "The temperate grasslands of Eurasia are called —",
      "The **Steppes** (Ukraine to Central Asia). Prairies - North America, Pampas - Argentina, Veld - South Africa."),
]

if __name__ == "__main__":
    subs = [build_universe(), build_interior(), build_atmosphere(),
            build_oceans(), build_continents(), build_countries()]
    apply_topic("world-geography", subs, PYQ)
