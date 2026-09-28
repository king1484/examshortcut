"""world-geography deep content - part 2: wg-oceans, wg-continents, wg-countries."""
import os
import sys

sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
from _lib import Sub
from wg_notes import NOTES


def build_oceans():
    S = Sub("wg-oceans")
    S.notes = NOTES["wg-oceans"].strip()
    S.pattern("ga-wo-p1", "Ocean superlatives and the five oceans", "very common",
        "'Largest/deepest ocean', 'which ocean is named after a country', 'Mariana Trench lies in', ordering of the five oceans.",
        None,
        "1. Size order: **Pacific > Atlantic > Indian > Southern > Arctic**; Pacific is also the deepest and holds most of the world's water.\n2. Deepest point: **Mariana Trench (Challenger Deep, about 11 km)** in the **Pacific**.\n3. The **Indian Ocean** is the only one named after a country; the **Southern Ocean** (2000) encircles Antarctica; the **Arctic** is the smallest and shallowest.",
        "Which is the deepest ocean of the world?",
        "The **Pacific Ocean** - it holds the Mariana Trench, whose **Challenger Deep (about 11 km)** is the deepest known point on Earth.")
    S.pattern("ga-wo-p2", "Ocean currents ↔ nature ↔ effects", "very common",
        "'Which is a warm current', 'Gulf Stream affects the climate of', 'which current makes a desert', fog and fishing grounds.",
        None,
        "1. Warm: **Gulf Stream + North Atlantic Drift** (keeps west Europe warm), Kuroshio, Brazilian, Agulhas, Eskimo-free East Australian.\n2. Cold: **Labrador** (icebergs, fog off Newfoundland), **Canary** (Canary Islands), **Benguela** (Namib), **Humboldt/Peru** (Atacama, rich anchovies, El Nino connection), Oyashio.\n3. Where a warm and cold current meet (Grand Banks, Dogger Bank) plankton blooms - hence the world's best **fishing grounds**; cold currents running along coasts make the **Atacama and Namib deserts**.",
        "The warm North Atlantic Drift keeps the climate of which region unusually mild for its latitude?",
        "**Western Europe (British Isles, Norway's coast)** - it is the eastward continuation of the Gulf Stream; the Labrador cold current meets the Gulf Stream near Newfoundland, making the Grand Banks foggy and rich in fish.")
    S.pattern("ga-wo-p3", "Straits: two water bodies and two lands", "very common",
        "'Which strait separates X from Y', 'which strait connects the Red Sea and the Gulf of Aden', match-the-column on straits.",
        None,
        "1. **Palk Strait** - India-Sri Lanka (Gulf of Mannar south of it); **Bering Strait** - Russia-Alaska (Arctic-Pacific); **Drake Passage** - South America-Antarctica (roughest).\n2. **Hormuz** - Persian Gulf (oil route); **Bab-el-Mandeb** - Red Sea-Gulf of Aden; **Malacca** - Andaman Sea-China Sea (longest, busiest); **Bosphorus + Dardanelles** - Black Sea-Mediterranean through Turkey.\n3. **Gibraltar** - Spain (Europe)-Morocco (Africa), Atlantic-Mediterranean. Learn each strait as four boxes: two lands, two waters.",
        "The Strait of Hormuz connects the Persian Gulf with the:",
        "**Gulf of Oman (Arabian Sea)** - the world's most important oil-shipping bottleneck between Iran and Oman/UAE.")
    S.pattern("ga-wo-p4", "Canals and man-made sea links", "common",
        "'Which canal joins the Mediterranean and the Red Sea', 'Suez/Panama canal connects', locks, year of opening.",
        None,
        "1. **Suez Canal (1869)** - Mediterranean-Red Sea; in **Egypt**; sea-level, **no locks**, about 193 km; Europe-Asia trade shortcut.\n2. **Panama Canal (1914)** - Atlantic-Pacific; in **Panama**; a **lock** canal about 82 km; joins Colon to Panama City.\n3. 'Kiel Canal' joins the North Sea and the Baltic (Germany) - a favourite third option.",
        "The Suez Canal, opened in 1869, lies in which country and connects which two seas?",
        "It lies in **Egypt** and joins the **Mediterranean Sea with the Red Sea**, cutting the Europe-Asia voyage by about 7,000 km; being sea-level, it has no locks.")
    S.pattern("ga-wo-p5", "Salinity, coral reefs and tides", "common",
        "'Highest salinity is in', 'coral reefs need', 'Great Barrier Reef lies off', spring vs neap tides, Bay of Fundy.",
        None,
        "1. Average ocean salinity **35 per mille**; highest in the **Red Sea (about 41)** - hot, dry, no fresh rivers; lowest in the **Baltic** (many rivers, low evaporation). **Dead Sea** = saltiest lake, bodies float.\n2. Corals need **clean, shallow, warm (over 20 C), salt water**; types: fringing, barrier, **atoll** (ring); **Great Barrier Reef** off Queensland (Australia) is the largest living structure; warm-water stress causes **bleaching**.\n3. Tides: **spring tides** - new/full moon (highest); **neap tides** - first/third quarter (lowest); **Bay of Fundy** (Canada) = highest tidal range.",
        "Which water body has the highest average salinity among the seas?",
        "The **Red Sea** (about 41 per mille) - high evaporation, low rainfall and hardly any fresh-water rivers. The Baltic has the lowest.")

    S.q("ga-wo-p1", "easy", "Which is the **largest ocean** in the world?",
        ["Atlantic", "Indian", "Pacific", "Arctic"], "Pacific",
        "The **Pacific** is the largest and deepest ocean - it covers more area than all the land put together and holds the Mariana Trench.",
        None, 15)
    S.q("ga-wo-p1", "medium", "The Mariana Trench, the deepest known point of the oceans, lies in which ocean?",
        ["Atlantic Ocean", "Indian Ocean", "Southern Ocean", "Pacific Ocean"], "Pacific Ocean",
        "The **Mariana Trench** (Challenger Deep, about 11 km deep) lies in the western **Pacific**, near the Mariana Islands.",
        None, 20)
    S.q("ga-wo-p1", "medium", "Which ocean is the **only one named after a country**?",
        ["Atlantic Ocean", "Indian Ocean", "Southern Ocean", "Arctic Ocean"], "Indian Ocean",
        "The **Indian Ocean** takes its name from India; it is the third largest and the warmest ocean.",
        None, 15)
    S.q("ga-wo-p1", "hard", "Which of these oceans was designated as a separate ocean most recently (in 2000), encircling Antarctica?",
        ["Arctic Ocean", "Southern Ocean", "Indian Ocean", "Atlantic Ocean"], "Southern Ocean",
        "The **Southern Ocean** (Antarctic Ocean), circumscribing Antarctica, was recognised separately around **2000**; the Arctic remains the smallest ocean.",
        None, 25)
    S.q("ga-wo-p2", "easy", "Which of the following is a **warm ocean current**?",
        ["Labrador", "Canary", "Gulf Stream", "Benguela"], "Gulf Stream",
        "The **Gulf Stream** is a warm current of the Atlantic; Labrador, Canary and Benguela are all cold currents.",
        None, 15)
    S.q("ga-wo-p2", "medium", "Icebergs off Newfoundland and the fog over the Grand Banks are caused mainly by the meeting of:",
        ["Gulf Stream and Canary current", "Kuroshio and Oyashio currents", "Gulf Stream and Labrador current", "Brazilian and Benguela currents"], "Gulf Stream and Labrador current",
        "The warm **Gulf Stream** meets the cold **Labrador current** off Newfoundland - fog and icebergs at the Grand Banks, plus rich fishing grounds where plankton thrives.",
        None, 25)
    S.q("ga-wo-p2", "medium", "The Atacama desert of South America owes its extreme dryness partly to the cold current flowing along its coast, called the:",
        ["Brazilian current", "Humboldt (Peru) current", "Agulhas current", "Guinea current"], "Humboldt (Peru) current",
        "The cold **Humboldt (Peru) current** cools the air, so little rain falls - making the Atacama. Its warm-water reversal is **El Nino**.",
        None, 25)
    S.q("ga-wo-p2", "hard", "The meeting of which two currents creates the rich Dogger Bank fishing ground of the North Sea?",
        ["Gulf Stream and Labrador", "North Atlantic Drift and Arctic cold current", "Kuroshio and Oyashio", "Benguela and Agulhas"], "North Atlantic Drift and Arctic cold current",
        "Where the warm **North Atlantic Drift** meets cold Arctic water over the submerged moraine of the **Dogger Bank**, plankton abounds - hence herring and cod. Grand Banks is its Atlantic twin.",
        None, 30)
    S.q("ga-wo-p3", "medium", "The Bosphorus and the Dardanelles straits, connecting the Black Sea with the Mediterranean, lie in which country?",
        ["Greece", "Russia", "Turkey", "Bulgaria"], "Turkey",
        "Both straits pass through **Turkey** - the Bosphorus at Istanbul (Sea of Marmara between them) and the Dardanelles towards the Aegean.",
        None, 20)
    S.q("ga-wo-p3", "medium", "Which strait separates India from Sri Lanka?",
        ["Malacca Strait", "Palk Strait", "Bass Strait", "Taiwan Strait"], "Palk Strait",
        "The **Palk Strait** lies between India (Tamil Nadu) and northern Sri Lanka; the Gulf of Mannar is south of it, with Adam's Bridge shoals in between.",
        None, 15)
    S.q("ga-wo-p3", "hard", "Which strait connects the **Red Sea** with the **Gulf of Aden** and lies between Yemen and Djibouti?",
        ["Strait of Hormuz", "Bab-el-Mandeb", "Strait of Malacca", "Bering Strait"], "Bab-el-Mandeb",
        "**Bab-el-Mandeb** ('Gate of Tears') guards the southern entrance to the Red Sea; Hormuz guards the Persian Gulf, Malacca the Andaman Sea-China Sea route.",
        None, 25)
    S.q("ga-wo-p4", "easy", "The Panama Canal connects the Atlantic Ocean with the:",
        ["Pacific Ocean", "Indian Ocean", "Arctic Ocean", "Mediterranean Sea"], "Pacific Ocean",
        "The **Panama Canal** (opened 1914) cuts across the Isthmus of Panama between the Atlantic (Caribbean) and the **Pacific**; it is a lock canal.",
        None, 15)
    S.q("ga-wo-p4", "medium", "Which statement about the **Suez Canal** is correct?",
        ["It is in Panama and has six locks", "It is in Egypt, is a sea-level canal without locks", "It connects the Atlantic and Pacific oceans", "It was opened in 1914"], "It is in Egypt, is a sea-level canal without locks",
        "The **Suez Canal** (1869, Egypt) runs sea-level from Port Said to Suez - **no locks** - and shortens the Europe-Asia route. Panama (1914) is the lock canal.",
        None, 25)
    S.q("ga-wo-p4", "medium", "The Kiel Canal connects the:",
        ["Mediterranean and Red Sea", "North Sea and Baltic Sea", "Black Sea and Aegean Sea", "Atlantic and Pacific"], "North Sea and Baltic Sea",
        "The **Kiel Canal** (Germany) joins the North Sea with the Baltic - a favourite distractor alongside Suez and Panama.",
        None, 20)
    S.q("ga-wo-p5", "easy", "The average salinity of ocean water is about:",
        ["15 parts per thousand", "25 parts per thousand", "35 parts per thousand", "50 parts per thousand"], "35 parts per thousand",
        "Ocean water averages **35 per mille** (about 3.5% salt). The Red Sea reaches about 41; the Baltic may fall below 10.",
        None, 15)
    S.q("ga-wo-p5", "medium", "Corals cannot grow in which of the following conditions?",
        ["Warm water above 20 C", "Clean, sediment-free water", "Deep water beyond the sunlight zone", "Salt water of normal ocean salinity"], "Deep water beyond the sunlight zone",
        "Corals need **shallow, sunlit, clean, warm (over 20 C) salt water** - they live in symbiosis with algae that require light. Cold or muddy water kills them.",
        None, 25)
    S.q("ga-wo-p5", "easy", "The Great Barrier Reef, the largest coral reef of the world, lies off the coast of:",
        ["Brazil", "Australia", "South Africa", "Indonesia"], "Australia",
        "The **Great Barrier Reef** stretches about 2,000 km off Queensland, north-east **Australia** - the largest structure built by living organisms.",
        None, 15)
    S.q("ga-wo-p5", "hard", "**Spring tides**, the highest tides of the month, occur when:",
        ["The Moon is in its first quarter", "The Sun, Moon and Earth are in a straight line (new or full moon)", "The Moon is farthest from Earth", "Strong winds pile water on the shore"], "The Sun, Moon and Earth are in a straight line (new or full moon)",
        "At new and full moon the Sun's and Moon's pulls combine - spring tides; at the quarters (neap tides) they work at right angles and the range is least. The Bay of Fundy (Canada) has the world's highest tidal range.",
        None, 25)
    return S


def build_continents():
    S = Sub("wg-continents")
    S.notes = NOTES["wg-continents"].strip()
    S.pattern("ga-wc-p1", "World superlatives: mountains, rivers, deserts, lakes, falls", "very common",
        "'Longest river', 'highest peak of each continent', 'largest island/lake', 'lowest point of land', 'highest waterfall'.",
        None,
        "1. Peaks: Everest (Asia, 8,848.86 m), Kilimanjaro (Africa), Denali (N. America), Aconcagua (S. America), Elbrus (Europe), Vinson (Antarctica), Kosciuszko (Australia).\n2. Rivers: **Nile longest (about 6,650 km)**, **Amazon largest by volume**; Deserts: **Sahara** largest hot desert; Lakes: **Caspian** largest, **Superior** largest freshwater, **Baikal** deepest, **Titicaca** highest navigable.\n3. Extremes: **Angel Falls** highest (979 m), **Dead Sea** lowest land (about 430 m below sea level), **Greenland** largest island, **Andes** longest mountains, **Tibet** highest plateau.",
        "Which is the largest island in the world?",
        "**Greenland** - about 21.6 lakh sq km; Australia is larger but counted as a continent, not an island.")
    S.pattern("ga-wc-p2", "Continent ↔ one-line identity", "very common",
        "'Which continent has no desert', 'most countries', 'longest river of each continent', 'fjords', continent lists.",
        None,
        "1. **Africa** - 54 countries, the most; the Nile (longest river) and the Sahara; the Great Rift Valley; Blue and White Nile meet at Khartoum; Lake Victoria largest African lake.\n2. **Asia** - largest continent; Lake Baikal (deepest), Caspian (largest lake), Yangtze (longest Asian river), Sundarbans; Mesopotamia ('cradle of civilisation').\n3. **Europe** - no hot desert; fjords in Norway; Vatican smallest country; Volga longest river of Europe; Danube passes through the most countries (10+). **Australia** - smallest continent; Great Barrier Reef, Uluru, Murray-Darling. **Antarctica** - coldest (-89.2 C at Vostok), no permanent population, 98% under ice; Antarctic Treaty 1959.",
        "Which continent has the largest number of independent countries?",
        "**Africa** - 54 countries. (Asia has about 48; Europe about 44.)")
    S.pattern("ga-wc-p3", "Grasslands by continent", "common",
        "'Prairies are in', 'Savanna is a grassland of', 'which grassland is in South America', match-the-column on temperate/tropical grasslands.",
        None,
        "1. Tropical: **Savanna** (Africa), **Llanos** (Venezuela), **Campos** (Brazil), 'Downs' (Australia).\n2. Temperate: **Prairies** (North America), **Steppes** (Eurasia/Russia), **Pampas** (Argentina - wheat, beef), **Veld** (South Africa), **Downs** (Australia), Canterbury (New Zealand).\n3. Fix the four classic ones - Prairies, Pampas, Steppes, Veld - and the rest follow by elimination.",
        "The temperate grasslands of South Africa are called:",
        "The **Veld**. (Prairies - North America, Steppes - Eurasia, Pampas - Argentina, Downs - Australia.)")
    S.pattern("ga-wc-p4", "Tribes and their native regions", "common",
        "'Bushmen live in', 'which tribe of the Congo forest', 'Masai are cattle herders of', match-the-column on tribes.",
        None,
        "1. Africa: **Pygmies** - Congo basin; **Bushmen** - Kalahari; **Masai** - East Africa (Kenya-Tanzania); **Bedouins** - Arabia; **Tuaregs/Berbers** - Sahara.\n2. Cold lands: **Inuit (Eskimos)** - Arctic Canada/Greenland/Alaska; **Lapps** - northern Scandinavia; **Kirghiz** - Central Asian steppes.\n3. Others: **Aborigines** - Australia; **Red Indians** - North America; **Fuegians** - Tierra del Fuego; **Ainus** - Japan.",
        "The Bushmen, famous hunters of the Kalahari desert, belong to which continent?",
        "**Africa** - the Kalahari lies in Botswana/Namibia. Pygmies are their Congo-basin counterparts.")
    S.pattern("ga-wc-p5", "Antarctica and the polar regions", "occasional",
        "'Antarctica is covered by', 'which country has research stations in Antarctica', 'Antarctic Treaty year', Arctic vs Antarctica.",
        None,
        "1. Antarctica: about **98% under an ice sheet**, average 2,000 m thick; coldest place **Vostok, about -89.2 C**; highest peak **Vinson Massif**; **no permanent human population**.\n2. The **Antarctic Treaty (1959, in force 1961)** reserves the continent for peaceful scientific use; India runs the **Dakshin Gangotri, Maitri and Bharati** stations.\n3. Arctic vs Antarctica: the Arctic is an **ocean** ringed by land (Inuit live there); Antarctica is **land** ringed by ocean.",
        "The Antarctic Treaty, which keeps the continent for peaceful scientific activity, was signed in:",
        "**1959** (in force 1961). India's Antarctic stations are **Dakshin Gangotri, Maitri and Bharati**.")

    S.q("ga-wc-p1", "easy", "The longest river in the world is generally taken to be the:",
        ["Amazon", "Nile", "Yangtze", "Mississippi"], "Nile",
        "The **Nile (about 6,650 km)** is the longest; the **Amazon** is the largest by volume of water. The Yangtze is the longest of Asia.",
        None, 15)
    S.q("ga-wc-p1", "medium", "The highest peak of **South America** is:",
        ["Mount Vinson", "Mount Aconcagua", "Mount Denali", "Mount Elbrus"], "Mount Aconcagua",
        "**Aconcagua** (Argentina, about 6,960 m) tops South America. Vinson - Antarctica, Denali - North America, Elbrus - Europe.",
        None, 20)
    S.q("ga-wc-p1", "medium", "Which is the **largest freshwater lake** in the world by area?",
        ["Lake Baikal", "Lake Victoria", "Lake Superior", "Lake Titicaca"], "Lake Superior",
        "**Lake Superior** (USA-Canada) is the largest freshwater lake by area; Baikal is the **deepest**; the Caspian is the largest lake overall but salty.",
        None, 20)
    S.q("ga-wc-p1", "medium", "Angel Falls, the highest waterfall in the world, is located in:",
        ["Brazil", "Venezuela", "Argentina", "Peru"], "Venezuela",
        "**Angel Falls** (about 979 m) drops from the Auyan-tepui tableland in **Venezuela**.",
        None, 15)
    S.q("ga-wc-p1", "hard", "The lowest point of the Earth's land surface is:",
        ["Death Valley", "The Dead Sea shore", "The Qattara Depression", "Lake Assal"], "The Dead Sea shore",
        "The **Dead Sea** shore (Israel-Jordan) lies about **430 m below sea level** - the lowest land on Earth; its water is also the saltiest of lakes.",
        None, 25)
    S.q("ga-wc-p2", "easy", "Which continent is the largest by area?",
        ["Africa", "Asia", "North America", "Europe"], "Asia",
        "**Asia** (about 44 million sq km) is the largest continent, with Africa second and Australia the smallest.",
        None, 15)
    S.q("ga-wc-p2", "medium", "The Blue Nile and the White Nile meet at:",
        ["Cairo", "Khartoum", "Aswan", "Addis Ababa"], "Khartoum",
        "They join at **Khartoum** (Sudan); the Blue Nile comes from Lake Tana in Ethiopia and carries most of the flood water.",
        None, 20)
    S.q("ga-wc-p2", "medium", "The fjord coast, carved by glaciers into deep sea inlets, is a typical feature of:",
        ["Norway", "Portugal", "Greece", "France"], "Norway",
        "**Norway's** west coast is the classic land of **fjords**. The Volga is Europe's longest river; the Danube crosses the most countries.",
        None, 15)
    S.q("ga-wc-p2", "hard", "Which continent is **completely covered** in the statements: (1) no permanent population, (2) about 98% under an ice sheet?",
        ["Arctic region", "Antarctica", "Australia", "Greenland (as a continent)"], "Antarctica",
        "**Antarctica** - scientists stay temporarily at research stations (India: Dakshin Gangotri, Maitri, Bharati); it is the coldest continent (Vostok, about -89 C).",
        None, 25)
    S.q("ga-wc-p2", "medium", "The Great Dividing Range and the Murray-Darling basin are features of:",
        ["South Africa", "Australia", "Argentina", "New Zealand"], "Australia",
        "The **Great Dividing Range** runs along Australia's east coast; the Murray-Darling is its chief river system. Uluru (Ayers Rock) lies in the centre.",
        None, 20)
    S.q("ga-wc-p3", "easy", "The temperate grasslands of **North America** are called:",
        ["Pampas", "Prairies", "Steppes", "Veld"], "Prairies",
        "**Prairies** - North America (wheat belt of Canada-USA). Pampas - Argentina; Steppes - Eurasia; Veld - South Africa.",
        "Prairies-Pampas-Steppes-Veld = NA-SA-Eurasia-Africa.", 15)
    S.q("ga-wc-p3", "medium", "The **Pampas** grasslands, famous for wheat and beef cattle, lie in:",
        ["South Africa", "Argentina", "Hungary", "Australia"], "Argentina",
        "The **Pampas** of Argentina (and Uruguay) are among the world's great farm lands; Buenos Aires stands on their edge.",
        None, 15)
    S.q("ga-wc-p3", "medium", "Match the grassland with its continent:\n1. Llanos  2. Campos  3. Canterbury\n(i) New Zealand (ii) Venezuela (iii) Brazil",
        ["1-(ii), 2-(iii), 3-(i)", "1-(i), 2-(ii), 3-(iii)", "1-(iii), 2-(ii), 3-(i)", "1-(ii), 2-(i), 3-(iii)"], "1-(ii), 2-(iii), 3-(i)",
        "**Llanos** - Venezuela (Orinoco), **Campos** - Brazil, **Canterbury** - New Zealand. All three are tropical (or southern temperate) grasslands.",
        None, 25)
    S.q("ga-wc-p4", "easy", "The **Inuit (Eskimos)** traditionally live in the:",
        ["Kalahari desert", "Arctic regions of North America and Greenland", "Congo basin", "Pampas"], "Arctic regions of North America and Greenland",
        "The **Inuit** are the indigenous people of the Arctic (Alaska, Canada, Greenland); the igloo and the kayak belong to their culture.",
        None, 15)
    S.q("ga-wc-p4", "medium", "The **Pygmies**, known as forest dwellers of short stature, live in the:",
        ["Sahara desert", "Congo basin", "Kalahari desert", "Savanna of East Africa"], "Congo basin",
        "**Pygmies** - equatorial rainforests of the **Congo basin**. Bushmen - Kalahari; Masai - East African savanna; Tuaregs - Sahara.",
        None, 20)
    S.q("ga-wc-p4", "medium", "The **Lapps** (Sami), traditional reindeer herders, are found in:",
        ["Northern Scandinavia", "Central Siberia", "Mongolia", "Alaska"], "Northern Scandinavia",
        "The **Lapps** live in northern Norway, Sweden, Finland and the Kola peninsula; the Kirghiz are their steppe counterparts in Central Asia.",
        None, 20)
    S.q("ga-wc-p5", "easy", "Which country operates the Indian Antarctic research stations **Maitri** and **Bharati**?",
        ["India", "Russia", "Australia", "Chile"], "India",
        "**India** runs **Maitri** and **Bharati** (and the earlier, now-buried **Dakshin Gangotri**) - its first expedition reached Antarctica in 1981-82.",
        None, 15)
    S.q("ga-wc-p5", "hard", "The **Arctic** is different from Antarctica mainly because the Arctic is:",
        ["Land surrounded by ocean", "An ocean surrounded by land", "A desert with no ice", "Warmer than all continents"], "An ocean surrounded by land",
        "The Arctic is a **frozen ocean** ringed by the lands of North America, Europe and Asia; **Antarctica is land** ringed by the Southern Ocean.",
        None, 30)
    return S


def build_countries():
    S = Sub("wg-countries")
    S.notes = NOTES["wg-countries"].strip()
    S.pattern("ga-wy-p1", "Country nicknames", "very common",
        "'Which country is called the Land of the Rising Sun', 'Land of Thousand Lakes', 'Land of White Elephant', nickname matching.",
        None,
        "1. Sun/light: **Rising Sun - Japan**, **Midnight Sun - Norway**, Morning Calm - Korea, Land of the Maple Leaf - Canada.\n2. Water/nature: **Thousand Lakes - Finland**, Fire and Ice - Iceland, Long White Cloud (Aotearoa) - New Zealand, **Thunder Dragon - Bhutan**, Emerald Isle - Ireland.\n3. Symbols/food: **White Elephant - Thailand**, Sugar Bowl - Cuba, Gift of the Nile - Egypt, Playground of Europe - Switzerland, Land of the Golden Fleece - Australia.",
        "Which country is called the 'Land of the Thunder Dragon'?",
        "**Bhutan** - 'Druk Yul' in Dzongkha, the land of the thunder dragon; its flag also bears the dragon.")
    S.pattern("ga-wy-p2", "City nicknames", "common",
        "'Big Apple', 'City of Seven Hills', 'Eternal City', 'City of Light', which-city-is-called questions.",
        None,
        "1. **New York - Big Apple**; **Rome - Eternal City / City of Seven Hills**; **Paris - City of Light**; **Chicago - Windy City**.\n2. **Venice - City of Canals**; **Beijing - the Forbidden City** (after the imperial palace); **Johannesburg - City of Gold** (gold mines); San Francisco - Golden Gate City.\n3. Distractors usually swap a European city pair - Rome and Paris are the classic confusion.",
        "Which city is known as the 'Big Apple'?",
        "**New York**. Rome is the 'Eternal City' and the 'City of Seven Hills'; Paris the 'City of Light'.")
    S.pattern("ga-wy-p3", "Boundary lines and borders", "very common",
        "'Durand/Radcliffe/McMahon line separates', '38th parallel divides', '49th parallel', 'Maginot line', match-the-column.",
        None,
        "1. India: **Durand Line (1893)** - Pakistan-Afghanistan; **Radcliffe Line (1947)** - India-Pakistan; **McMahon Line (1914)** - India-China (Arunachal side).\n2. Koreas - **38th Parallel**; USA-Canada - **49th Parallel**; North-South Vietnam - **17th Parallel**.\n3. Fortification lines: **Maginot** - France-Germany (WW2 defences); **Hindenburg** - German WW1 line; **Oder-Neisse** - Germany-Poland; **Mannerheim** - Finland-Russia.",
        "The McMahon Line is the boundary between:",
        "**India and China** - drawn at the 1914 Simla Convention, running along the eastern (Arunachal Pradesh) sector; the Durand Line separates Pakistan and Afghanistan.")
    S.pattern("ga-wy-p4", "Old names → new names", "very common",
        "'Siam is the old name of', 'Ceylon is now', 'Constantinople', old-new matching for countries and cities.",
        None,
        "1. Countries: **Ceylon - Sri Lanka (1972)**, Burma - Myanmar (1989), Siam - Thailand, Persia - Iran (1935), Abyssinia - Ethiopia, Formosa - Taiwan, Gold Coast - Ghana (1957), Rhodesia - Zimbabwe (1980), East Pakistan - Bangladesh (1971).\n2. Cities: **Constantinople - Istanbul**, Peking - Beijing, Rangoon - Yangon, Saigon - Ho Chi Minh City, Batavia - Jakarta, Leningrad - St Petersburg.\n3. Indian cities: Bombay-Mumbai, Madras-Chennai, Calcutta-Kolkata - but exam questions normally ask the foreign ones.",
        "'Siam' was the former name of which country?",
        "**Thailand.** Ceylon became Sri Lanka; Burma became Myanmar; Persia became Iran.")
    S.pattern("ga-wy-p5", "Capitals on rivers", "very common",
        "'Which capital stands on the Danube', 'Baghdad is on which river', 'Paris is on the Seine', capital-river matching.",
        None,
        "1. Own small rivers: **London - Thames, Paris - Seine, Rome - Tiber, Moscow - Moskva, Berlin - Spree, Warsaw - Vistula, Prague - Vltava, Ottawa - Ottawa, Washington - Potomac.**\n2. Big rivers: **Cairo - Nile, Baghdad - Tigris, Khartoum - confluence of Blue and White Nile, Delhi - Yamuna, Dhaka - Buriganga, Bangkok - Chao Phraya, Hanoi - Red River, Seoul - Han.**\n3. **Danube** flows through Vienna, Bratislava, Budapest and Belgrade - four capitals on one river.",
        "Which river flows through Vienna, Budapest and Belgrade - three European capitals?",
        "The **Danube** - it also passes through Bratislava, making four capitals on one river; the Rhine does not touch any capital.")

    S.q("ga-wy-p1", "easy", "Which country is known as the 'Land of the Rising Sun'?",
        ["China", "Japan", "South Korea", "Thailand"], "Japan",
        "**Japan** - Nippon, 'origin of the sun', from its position east of the Asian mainland; its flag shows the sun disc.",
        None, 15)
    S.q("ga-wy-p1", "easy", "Which country is called the 'Land of a Thousand Lakes'?",
        ["Canada", "Finland", "Norway", "Sweden"], "Finland",
        "**Finland** actually has about 1.88 lakh lakes; Canada has more lakes overall but Finland owns the nickname.",
        None, 15)
    S.q("ga-wy-p1", "medium", "The 'Land of the White Elephant' is:",
        ["Myanmar", "Thailand", "Sri Lanka", "Cambodia"], "Thailand",
        "**Thailand** - the white elephant was a royal symbol; it appears on the old flag. Bhutan is the 'Thunder Dragon' land.",
        None, 15)
    S.q("ga-wy-p1", "medium", "Which country is called the 'Land of the Midnight Sun' because summer days never fully end in its north?",
        ["Iceland", "Norway", "Denmark", "Ireland"], "Norway",
        "**Norway** - north of the Arctic Circle the summer Sun never sets. Iceland is 'Fire and Ice'; Ireland the 'Emerald Isle'.",
        None, 20)
    S.q("ga-wy-p2", "easy", "Which city is called the 'Eternal City'?",
        ["Athens", "Rome", "Cairo", "Jerusalem"], "Rome",
        "**Rome** - also the 'City of Seven Hills'; Athens is the 'City of Violet Crowns' in older literature.",
        None, 15)
    S.q("ga-wy-p2", "medium", "The 'Windy City', famous for its strong lake breezes, is:",
        ["Boston", "Chicago", "Seattle", "Denver"], "Chicago",
        "**Chicago**, on Lake Michigan, is the Windy City; New York is the Big Apple; San Francisco the Golden Gate City.",
        None, 15)
    S.q("ga-wy-p2", "medium", "Johannesburg, the centre of a great mining region, is called the:",
        ["City of Gold", "Mother City", "Rainbow City", "Diamond City"], "City of Gold",
        "**Johannesburg** grew on the Witwatersrand **gold** reefs. Kimberley, not Johannesburg, is linked with diamonds.",
        None, 15)
    S.q("ga-wy-p3", "easy", "The Radcliffe Line (1947) is the boundary between:",
        ["India and China", "India and Pakistan", "India and Bangladesh", "Pakistan and Afghanistan"], "India and Pakistan",
        "The **Radcliffe Line** was drawn in **1947** at Partition between India and (West) Pakistan; the Durand Line (1893) separates Pakistan and Afghanistan.",
        None, 15)
    S.q("ga-wy-p3", "medium", "The **38th Parallel** is associated with the boundary between:",
        ["North Korea and South Korea", "Vietnam's north and south (former)", "USA and Canada", "Poland and Germany"], "North Korea and South Korea",
        "The **38th Parallel** divides the two Koreas (armistice line, 1953). The 17th Parallel divided Vietnam; the 49th Parallel runs along much of the US-Canada border.",
        None, 20)
    S.q("ga-wy-p3", "medium", "The Maginot Line, a chain of concrete fortifications of the 1930s, was built by which country on its border with Germany?",
        ["Belgium", "France", "Netherlands", "Switzerland"], "France",
        "**France** built the **Maginot Line**; German forces simply went around it in 1940. The Hindenburg Line was Germany's own WW1 defence line.",
        None, 25)
    S.q("ga-wy-p3", "hard", "Which of the following is correctly matched?",
        ["Durand Line - India and China", "McMahon Line - India and Pakistan", "Oder-Neisse Line - Germany and Poland", "Mannerheim Line - Norway and Russia"], "Oder-Neisse Line - Germany and Poland",
        "The **Oder-Neisse Line** runs along the Oder and Neisse rivers between Germany and Poland. Durand - Pak-Afghan; McMahon - India-China; Mannerheim - Finland-Russia.",
        None, 30)
    S.q("ga-wy-p4", "easy", "'Ceylon' was the former name of which country?",
        ["Maldives", "Sri Lanka", "Myanmar", "Mauritius"], "Sri Lanka",
        "**Ceylon** became **Sri Lanka** in **1972** when it became a republic; its capital is Sri Jayawardenepura Kotte (Colombo is the commercial hub).",
        None, 15)
    S.q("ga-wy-p4", "medium", "The city once called **Constantinople** is today known as:",
        ["Ankara", "Istanbul", "Izmir", "Bursa"], "Istanbul",
        "**Constantinople** was renamed **Istanbul** (officially from 1930); Ankara is Turkey's capital. Peking-Beijing and Rangoon-Yangon are parallel cases.",
        None, 15)
    S.q("ga-wy-p4", "medium", "'Gold Coast', a former British colony, is the old name of which country?",
        ["Zimbabwe", "Ghana", "Nigeria", "Kenya"], "Ghana",
        "**Gold Coast** became **Ghana** at independence in **1957** - the first sub-Saharan colony to gain freedom. Rhodesia became Zimbabwe (1980).",
        None, 20)
    S.q("ga-wy-p5", "easy", "Baghdad, the capital of Iraq, stands on the bank of which river?",
        ["Euphrates", "Tigris", "Nile", "Jordan"], "Tigris",
        "**Baghdad - Tigris.** Cairo stands on the Nile; Khartoum at the Blue-White Nile confluence.",
        None, 15)
    S.q("ga-wy-p5", "easy", "The capital of Egypt, Cairo, is situated on which river?",
        ["Congo", "Niger", "Nile", "Zambezi"], "Nile",
        "**Cairo - Nile**; Egypt itself is the 'Gift of the Nile'.",
        None, 15)
    S.q("ga-wy-p5", "medium", "Which of the following capital-river pairs is **wrong**?",
        ["Paris - Seine", "Moscow - Moskva", "Berlin - Rhine", "Warsaw - Vistula"], "Berlin - Rhine",
        "**Berlin stands on the Spree** (and the Havel); the Rhine flows through Cologne and Rotterdam, not a capital.",
        None, 20)
    S.q("ga-wy-p5", "medium", "Bangkok, the capital of Thailand, lies on which river?",
        ["Mekong", "Chao Phraya", "Irrawaddy", "Salween"], "Chao Phraya",
        "**Bangkok - Chao Phraya** ('River of Kings'). Hanoi - Red River; Dhaka - Buriganga; Yangon - Yangon river.",
        None, 20)
    S.q("ga-wy-p5", "hard", "Which single European river flows through the greatest number of capital cities?",
        ["Rhine", "Danube", "Seine", "Volga"], "Danube",
        "The **Danube** passes through **Vienna (Austria), Bratislava (Slovakia), Budapest (Hungary) and Belgrade (Serbia)** - four capitals; the Volga is Europe's longest river but has no capital on it.",
        None, 30)
    return S
