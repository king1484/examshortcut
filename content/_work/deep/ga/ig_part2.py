"""indian-geography deep content - part 2: ig-climate-soils, ig-agri-minerals, ig-parks."""
import os
import sys

sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
from _lib import Sub
from ig_notes import NOTES


def build_climate():
    S = Sub("ig-climate-soils")
    S.notes = NOTES["ig-climate-soils"].strip()
    S.pattern("ga-ics-p1", "SW monsoon: onset, branches and withdrawal", "very common",
        "Questions on when and where the monsoon strikes Kerala, its two branches, when it covers the country, or when it starts withdrawing.",
        None,
        "1. Onset: SW monsoon normally bursts on the Kerala coast about **1 June** and covers most of India by **mid-July**.\n2. Two branches: the **Arabian Sea branch** (heavy rain on the windward Western Ghats) and the **Bay of Bengal branch** (north-east, then up the Ganga plain).\n3. Withdrawal begins from the **north-west around mid-September**; the monsoon season is roughly June to September.",
        "The south-west monsoon normally sets in over the Kerala coast around —",
        "**1 June.** From Kerala it advances north in two branches and normally covers the whole country by mid-July.")
    S.pattern("ga-ics-p2", "Rainfall distribution, rain shadow and extremes", "very common",
        "'Which region gets the highest/lowest rainfall?', 'Why is Pune/Deccan dry?', 'rain shadow of the Western Ghats', 'Mawsynram is in which state?'",
        None,
        "1. Windward side of the Western Ghats (Konkan, Kerala, Mumbai) = very heavy rain; the leeward side (Pune, interior Karnataka, Marathwada) lies in the **rain shadow**.\n2. Wettest spots: **Mawsynram** and **Cherrapunji (Sohra)** in Meghalaya; driest: western Rajasthan (Jaisalmer).\n3. Tamil Nadu's coast stays comparatively dry in June-September because it lies in the rain shadow and is oriented away from the SW monsoon - its main rain comes later (NE monsoon).",
        "Mawsynram, one of the rainiest places on Earth, lies in which state?",
        "**Meghalaya**, in the Khasi hills. Cherrapunji (Sohra) is the other famous wet station nearby.")
    S.pattern("ga-ics-p3", "Retreating monsoon, October heat and local winds", "very common",
        "'Kalbaisakhi is associated with', 'mango showers help which crop', 'October heat', 'which wind brings winter rain to Punjab'.",
        None,
        "1. October: winds retreat, days hot and humid - **October heat**. The retreating winds pick up moisture from the Bay of Bengal and give **Oct-Dec rain to the Tamil Nadu coast** (NE monsoon).\n2. Showers: **Mango showers** (Kerala-Karnataka, mango), **Blossom showers** (Karnataka, coffee), **Kalbaisakhi/Nor'westers** (Bengal-Assam, tea-jute; **Bordoichila** in Assam).\n3. Winter: **Western disturbances** from the Mediterranean region give rain to Punjab, Haryana, west UP and J&K - vital for **rabi wheat**.",
        "Kalbaisakhi (Nor'wester) thunderstorms, which benefit the tea and jute crops, occur mainly in —",
        "**West Bengal and Assam** in spring (March-May). In Assam the same season brings the **Bordoichila** winds.")
    S.pattern("ga-ics-p4", "Soil type ↔ properties, formation and crops", "very common",
        "'Regur soil is best for', 'which soil is formed by leaching', 'black soil is deficient in', 'khadar and bhangar are types of'.",
        None,
        "1. Match soil to formation: alluvial - river deposits (khadar new, bhangar old with kankar); black (regur) - **basalt**; red/yellow - iron oxide; laterite - **intense leaching**; arid - desert; peaty - Kerala (kari).\n2. Black soil: rich in lime, iron, magnesium, potash; **poor in nitrogen, phosphorus and humus**; self-ploughing cracks; ideal for **cotton**.\n3. Laterite hardens into bricks when exposed; saline-alkaline soil (*reh, usar*) is reclaimed with **gypsum**.",
        "Black (regur) soil is well known for being deficient in —",
        "**Nitrogen, phosphorus and humus.** It is rich in lime, iron, magnesium and potash, and holds moisture well - hence its value for cotton.")
    S.pattern("ga-ics-p5", "Soil erosion and conservation", "occasional",
        "'Ravines of the Chambal are an example of', 'contour ploughing is used for', 'sheet erosion means'.",
        None,
        "1. **Gully erosion** (running water) turns land into useless **ravines** - the Chambal badlands of MP-Rajasthan-UP.\n2. **Sheet erosion** removes the topsoil uniformly; **wind erosion** strips dry open land.\n3. Remedies: contour ploughing, terrace farming, strip cropping, shelter belts, afforestation.",
        "The bare, gullied badlands along the Chambal river are a classic example of —",
        "**Gully erosion** by running water, which cuts the alluvial land into deep ravines unfit for cultivation.")

    S.q("ga-ics-p1", "easy", "The south-west monsoon normally sets in over the Kerala coast around:",
        ["1 May", "1 June", "15 June", "1 July"], "1 June",
        "The normal onset date of the SW monsoon over Kerala is about **1 June** (the 'burst of the monsoon'); the whole country is usually covered by mid-July.",
        None, 15)
    S.q("ga-ics-p1", "medium", "Which branch of the south-west monsoon gives very heavy rain on the windward side of the Western Ghats?",
        ["Bay of Bengal branch", "Arabian Sea branch", "North-east branch", "Retreating branch"], "Arabian Sea branch",
        "The **Arabian Sea branch** strikes the Western Ghats at right angles and drops very heavy rain on the windward (west) side; the Bay of Bengal branch moves up the Ganga plain.",
        None, 20)
    S.q("ga-ics-p1", "medium", "The south-west monsoon normally begins to withdraw from India around:",
        ["1 August", "Mid-August", "Mid-September", "Mid-October"], "Mid-September",
        "Withdrawal starts from the **north-west around mid-September** and the monsoon leaves the mainland by early October, after which 'October heat' follows.",
        None, 20)
    S.q("ga-ics-p2", "easy", "Which of the following records the highest average annual rainfall in India?",
        ["Cherrapunji (Sohra)", "Mawsynram", "Mumbai", "Kochi"], "Mawsynram",
        "**Mawsynram** (Meghalaya) holds the record for the highest average annual rainfall; Cherrapunji (Sohra) is close behind. Both lie in the Khasi hills.",
        None, 15)
    S.q("ga-ics-p2", "medium", "Pune, on the Deccan plateau, receives little rain during the south-west monsoon because it lies in the —",
        ["Rain shadow of the Western Ghats", "Rain shadow of the Eastern Ghats", "Path of the north-east monsoon", "Zone of the doldrums"], "Rain shadow of the Western Ghats",
        "The Western Ghats intercept the Arabian Sea branch; after the winds descend on the leeward side, they are dry - Pune and the Marathwada region fall in this **rain shadow**.",
        None, 20)
    S.q("ga-ics-p2", "hard", "Which region of India receives most of its rainfall from the retreating (north-east) monsoon?",
        ["Punjab", "Coromandel coast (Tamil Nadu)", "Konkan coast", "Malwa plateau"], "Coromandel coast (Tamil Nadu)",
        "The retreating winds pick up moisture over the **Bay of Bengal** and strike the Tamil Nadu (Coromandel) coast from the north-east, giving **October-December** rain - the main rainfall of that region.",
        None, 30)
    S.q("ga-ics-p2", "medium", "During the monsoon months the western side of the Western Ghats is wet, while the interior Deccan is comparatively dry. This is mainly due to:",
        ["Convectional rainfall", "Orographic rainfall", "Cyclonic rainfall", "Frontal rainfall"], "Orographic rainfall",
        "Moist winds are forced up by the mountains (**orographic rainfall**) and shed rain on the windward side; the leeward side stays dry. Cherrapunji's rain is also orographic.",
        None, 25)
    S.q("ga-ics-p3", "easy", "The hot, dry summer wind that blows over the plains of north India is called the:",
        ["Loo", "Bora", "Foehn", "Chinook"], "Loo",
        "The **Loo** blows over the north Indian plains in May-June. Bora and Mistral are cold European winds; Chinook and Foehn are warm descending winds of the Rockies and Alps.",
        "Loo = summer; Mistral = France; Chinook = 'snow eater' of the Rockies.", 15)
    S.q("ga-ics-p3", "medium", "The 'Kalbaisakhi' thunderstorms of eastern India are beneficial mainly for which crops?",
        ["Tea and jute", "Wheat and barley", "Cotton and maize", "Sugarcane and rice"], "Tea and jute",
        "**Kalbaisakhi** (Nor'wester) showers of Bengal-Assam help **tea and jute**. Mango showers help mango in Kerala-Karnataka; blossom showers help coffee.",
        None, 20)
    S.q("ga-ics-p3", "medium", "Winter rainfall in Punjab and Haryana, useful for the rabi wheat crop, is caused by:",
        ["Western disturbances", "Kalbaisakhi", "The retreating monsoon", "Local convection currents"], "Western disturbances",
        "**Western disturbances** - shallow depressions travelling from the Mediterranean region - bring welcome winter rain to Punjab, Haryana, west UP and J&K; the snow they drop in the mountains feeds rivers later.",
        None, 25)
    S.q("ga-ics-p3", "medium", "The sultry, hot and humid weather of early October in northern India is popularly called:",
        ["October heat", "Loo", "Bordoichila", "Mango shower"], "October heat",
        "After the monsoon withdraws, clear skies and moist air make early October days hot and humid - the **October heat**. Bordoichila is the pre-monsoon wind of Assam.",
        None, 20)
    S.q("ga-ics-p4", "easy", "The black soil of the Deccan, best suited for cotton cultivation, is also known as:",
        ["Laterite", "Regur", "Khadar", "Bhangar"], "Regur",
        "**Regur** is the black soil derived from basaltic lava of the Deccan Trap; its moisture-holding capacity and self-ploughing cracks suit cotton.",
        None, 15)
    S.q("ga-ics-p4", "medium", "Laterite soil is mainly formed by:",
        ["Leaching in hot, wet climates", "Deposition by rivers", "Volcanic ash deposits", "Wind deposition in deserts"], "Leaching in hot, wet climates",
        "Alternating heavy rain and heat **leaches** out silica and lime, leaving iron and aluminium oxides - laterite (Latin *later*, brick) hardens like brick on exposure.",
        None, 20)
    S.q("ga-ics-p4", "hard", "With reference to alluvial soils, which statement is correct?",
        ["Bhangar is the newer alluvium and khadar the older", "Khadar is the newer alluvium and bhangar the older, containing kankar nodules", "Both are equally fertile", "Bhangar is found only in Kerala"], "Khadar is the newer alluvium and bhangar the older, containing kankar nodules",
        "**Khadar** - renewed every year by fresh floods, more fertile. **Bhangar** - older, above flood level, with calcareous **kankar** nodules. The distinction applies to alluvial soils of the northern plains.",
        "K = Khadar = keeps getting renewed.", 30)
    S.q("ga-ics-p4", "medium", "Saline and alkaline (usara) soils of over-irrigated tracts are commonly reclaimed by applying:",
        ["Gypsum", "Lime", "Farmyard manure only", "Urea"], "Gypsum",
        "**Gypsum** replaces the sodium on the soil particles with calcium, improving the structure of saline-alkaline (*reh, usar*) soil.",
        None, 25)
    S.q("ga-ics-p5", "medium", "The deep ravines along the Chambal river are a result of:",
        ["Gully erosion", "Sheet erosion", "Wind deposition", "Leaching"], "Gully erosion",
        "**Gully erosion** by running water cuts the alluvial land into deep ravines unfit for cultivation. Sheet erosion removes topsoil uniformly.",
        None, 20)
    S.q("ga-ics-p5", "medium", "Which of the following is a soil-conservation measure on hill slopes?",
        ["Contour ploughing", "Shifting cultivation", "Overgrazing", "Monoculture"], "Contour ploughing",
        "Ploughing along the **contours** (level lines) checks the speed of running water down the slope; terracing and strip cropping are similar measures.",
        None, 20)
    return S


def build_agri():
    S = Sub("ig-agri-minerals")
    S.notes = NOTES["ig-agri-minerals"].strip()
    S.pattern("ga-iam-p1", "Crop ↔ season (kharif, rabi, zaid)", "very common",
        "'Which of the following is a rabi/kharif crop?', 'zaid crops are grown when', matching a list of crops to a season.",
        None,
        "1. **Kharif** - sown with the monsoon (June-July), harvested Sep-Oct: rice, jowar, bajra, maize, cotton, jute, groundnut, soybean, tur.\n2. **Rabi** - sown in winter (Oct-Nov), harvested Mar-Apr: wheat, barley, gram, mustard, peas.\n3. **Zaid** - short summer season (Mar-June): watermelon, muskmelon, cucumber, fodder. 'Not a kharif crop' questions are usually answered by wheat or mustard (rabi).",
        "Which of the following is a **rabi** crop?\n(a) Cotton (b) Mustard (c) Maize (d) Groundnut",
        "(b) **Mustard** - sown in October-November and harvested in March-April. Cotton, maize and groundnut are kharif crops.")
    S.pattern("ga-iam-p2", "Crop ↔ leading state / growing conditions", "very common",
        "'Golden fibre is', 'which state is the largest producer of coffee', 'Baba Budan hills are associated with'.",
        None,
        "1. Stable pairs: **tea-Assam, coffee-Karnataka, rubber-Kerala, jute-West Bengal, sugarcane-UP, wheat-UP, groundnut-Gujarat**; Kerala = spice garden.\n2. Conditions hooks: tea - well-drained slopes, cool moist climate; jute - alluvial deltaic soil and standing water; coffee - Baba Budan hills, shade.\n3. Rice/cotton leadership shifts between states year to year - treat those as current affairs, not static GK.",
        "The 'golden fibre' of India, grown mainly in West Bengal, is —",
        "**Jute.** It needs deltaic alluvial soil and abundant water for retting; India is the world's largest producer of jute.")
    S.pattern("ga-iam-p3", "Revolution colour ↔ product (and pioneer)", "very common",
        "'Operation Flood is associated with', 'which revolution relates to fish production', 'White Revolution pioneer'.",
        None,
        "1. Green - food grains (**M.S. Swaminathan** in India, mid-1960s HYV); White - milk (**Verghese Kurien**, Operation Flood 1970, Anand/Amul).\n2. Blue - fish; Yellow - oilseeds; Silver - eggs/poultry; Round - potato; Golden - horticulture and honey; Pink - onion/prawn (occasionally asked).\n3. Superlatives: India is the world's largest producer of **milk, pulses and jute**.",
        "Operation Flood (1970), which made India the world's largest milk producer, is linked to which revolution?",
        "The **White Revolution**, led by **Dr Verghese Kurien** from Anand (Gujarat), home of Amul.")
    S.pattern("ga-iam-p4", "Mineral / energy resource ↔ location", "very common",
        "'Jharia is famous for', 'largest lignite deposit', 'oldest oil refinery', match-the-column on minerals.",
        None,
        "1. Coal: **Jharia** (largest coking-coal field, Jharkhand), **Raniganj** (oldest, WB, 1774), Korba (Chhattisgarh), Talcher (Odisha).\n2. Oil: **Digboi** (Assam, oldest refinery, 1901), **Mumbai High** (offshore Arabian Sea), Ankleshwar and Koyali (Gujarat). Lignite - **Neyveli** (TN).\n3. Metals: iron - Bailadila (Chhattisgarh), Bellary-Sandur (Karnataka); bauxite - Odisha (Koraput); mica - Koderma (Jharkhand); copper - Khetri (Rajasthan); zinc-lead - Zawar (Rajasthan); gold - **Hutti** (Karnataka; Kolar closed in 2001).",
        "India's largest reserves of bauxite lie in which state?",
        "**Odisha** - the Panchpatmali deposits in Koraput district are the country's largest, feeding the aluminium industry.")
    S.pattern("ga-iam-p5", "Major port ↔ speciality", "common",
        "'Which port is called tidal', 'deepest landlocked port', 'which port handles containers/iron ore', artificial vs natural harbours.",
        None,
        "1. West coast: **Deendayal (Kandla)** - tidal port; **Mumbai** - largest natural harbour; **JNPT** - largest container port among major ports; **Mormugao** - iron-ore exports; Kochi; New Mangalore.\n2. East coast: **Chennai** - artificial harbour; **Kamarajar (Ennore)** - first corporatised major port; **Visakhapatnam** - deepest landlocked and protected port; **Paradip**; **Kolkata (Syama Prasad Mookerjee)** - riverine port with Haldia dock; Tuticorin (V.O. Chidambaranar).\n3. Pair the adjective with the port: tidal-Kandla, artificial-Chennai, riverine-Kolkata, deepest-Vizag.",
        "Which major port of India is known as a tidal port?",
        "**Deendayal Port, Kandla** (Gujarat), on the Gulf of Kutch - tides govern the entry of ships into its basins.")

    S.q("ga-iam-p1", "easy", "Which of the following is a **kharif** crop?",
        ["Wheat", "Gram", "Cotton", "Mustard"], "Cotton",
        "**Cotton** is sown with the monsoon and picked in autumn. Wheat, gram and mustard are rabi (winter) crops.",
        None, 15)
    S.q("ga-iam-p1", "easy", "Watermelon and cucumber are typical crops of which season?",
        ["Kharif", "Rabi", "Zaid", "Year-round plantation"], "Zaid",
        "**Zaid** is the short summer season (March-June) for melons, cucumber and fodder - between the rabi harvest and the kharif sowing.",
        None, 15)
    S.q("ga-iam-p1", "medium", "Which group of crops is sown in October-November and harvested around March-April?",
        ["Rice, jowar, bajra", "Wheat, barley, gram", "Jute, cotton, groundnut", "Maize, tur, soybean"], "Wheat, barley, gram",
        "That is the **rabi** season. Rice, jowar, jute and maize are monsoon (kharif) crops; tur (arhar) is also kharif.",
        None, 20)
    S.q("ga-iam-p2", "easy", "The leading producer of coffee in India is:",
        ["Kerala", "Karnataka", "Tamil Nadu", "Assam"], "Karnataka",
        "**Karnataka** grows roughly 70% of India's coffee (Arabica and Robusta), in Kodagu, Chikmagalur and the Baba Budan hills.",
        None, 15)
    S.q("ga-iam-p2", "medium", "Coffee cultivation in India began in the Baba Budan hills, which lie in which state?",
        ["Tamil Nadu", "Kerala", "Karnataka", "Andhra Pradesh"], "Karnataka",
        "The **Baba Budan (Chandra Drona) hills** of Chikmagalur district, Karnataka, are the traditional home of Indian coffee - legend says seeds were brought from Yemen in the 17th century.",
        None, 20)
    S.q("ga-iam-p2", "medium", "Jute cultivation in India is concentrated in West Bengal mainly because of:",
        ["Black soil and low rainfall", "Deltaic alluvial soil and abundant water for retting", "Laterite soil on hill slopes", "Cold winters"], "Deltaic alluvial soil and abundant water for retting",
        "Jute needs the **Ganga-Brahmaputra delta's** new alluvium, high temperature and heavy rain, plus still water in which the fibre is **retted** (softened).",
        None, 25)
    S.q("ga-iam-p2", "medium", "Which state is called the 'spice garden of India'?",
        ["Karnataka", "Kerala", "Goa", "Maharashtra"], "Kerala",
        "**Kerala** produces pepper, cardamom, ginger, turmeric and other spices; it is also the leading rubber producer.",
        None, 15)
    S.q("ga-iam-p3", "easy", "The White Revolution of India is associated with:",
        ["Fish production", "Milk production", "Oilseeds", "Food grains"], "Milk production",
        "The **White Revolution** (Operation Flood, 1970) made India the world's largest milk producer; its architect was **Dr Verghese Kurien**.",
        None, 15)
    S.q("ga-iam-p3", "medium", "The 'Yellow Revolution' in India is related to increased production of:",
        ["Sunflower only", "Oilseeds", "Pulses", "Bananas"], "Oilseeds",
        "**Yellow Revolution** = oilseeds (mustard, groundnut, soybean, sunflower). Green - food grains; Blue - fish; Golden - horticulture/honey.",
        None, 20)
    S.q("ga-iam-p3", "medium", "The 'Blue Revolution' in India refers to development in:",
        ["Drinking water supply", "Fish and aquaculture production", "Indigo cultivation", "Irrigation canals"], "Fish and aquaculture production",
        "The **Blue Revolution** covers fisheries and aquaculture. Indigo is a dye crop with no 'revolution' attached to it.",
        None, 20)
    S.q("ga-iam-p3", "hard", "Match the revolution with its product:\n1. Silver  2. Round  3. Golden\nProducts: (i) Potato (ii) Horticulture/honey (iii) Eggs/poultry",
        ["1-(iii), 2-(i), 3-(ii)", "1-(i), 2-(iii), 3-(ii)", "1-(ii), 2-(i), 3-(iii)", "1-(iii), 2-(ii), 3-(i)"], "1-(iii), 2-(i), 3-(ii)",
        "**Silver** = eggs/poultry, **Round** = potato, **Golden** = horticulture and honey. (Also: Yellow = oilseeds, Blue = fish.)",
        None, 30)
    S.q("ga-iam-p4", "easy", "Digboi, the site of India's oldest oil refinery (1901), is in which state?",
        ["Assam", "Gujarat", "Maharashtra", "Odisha"], "Assam",
        "**Digboi** (Tinsukia district, Assam) has India's oldest working refinery. Gujarat's fields (Ankleshwar) and the offshore **Mumbai High** came later.",
        None, 15)
    S.q("ga-iam-p4", "medium", "India's largest lignite deposits, worked at Neyveli, are in which state?",
        ["Tamil Nadu", "Jharkhand", "Rajasthan", "Gujarat"], "Tamil Nadu",
        "**Neyveli** (Tamil Nadu) holds the largest lignite (brown coal) reserves; the mines and thermal plants there are famous.",
        None, 20)
    S.q("ga-iam-p4", "medium", "The largest coking coalfield of India is:",
        ["Raniganj", "Jharia", "Korba", "Talcher"], "Jharia",
        "**Jharia** (Dhanbad, Jharkhand) holds the bulk of India's coking coal. Raniganj (West Bengal) is the oldest field (1774) but has mostly non-coking coal.",
        None, 20)
    S.q("ga-iam-p4", "hard", "Which of the following is the only major gold mine still in operation in India?",
        ["Kolar Gold Fields", "Hutti", "Ramagiri", "Sonapahar"], "Hutti",
        "**Hutti** (Raichur district, Karnataka) is India's only operating large gold mine. **Kolar Gold Fields**, once the deepest mine in India, closed in 2001.",
        None, 30)
    S.q("ga-iam-p4", "medium", "Khetri, a well-known copper belt of India, lies in which state?",
        ["Jharkhand", "Rajasthan", "Madhya Pradesh", "Odisha"], "Rajasthan",
        "**Khetri** (Jhunjhunu district, Rajasthan) is a classic copper belt; Malanjkhand (Madhya Pradesh) and Singhbhum (Jharkhand) are the other major copper areas.",
        None, 20)
    S.q("ga-iam-p5", "medium", "Which major port is described as the deepest landlocked and protected port of India?",
        ["Chennai", "Kochi", "Visakhapatnam", "Paradip"], "Visakhapatnam",
        "**Visakhapatnam** (Andhra Pradesh) lies sheltered between land and Dolphin's Nose headland - the deepest landlocked and protected major port.",
        None, 20)
    S.q("ga-iam-p5", "easy", "Which of these is an artificial harbour of India?",
        ["Mumbai", "Chennai", "Mormugao", "Kandla"], "Chennai",
        "**Chennai** is India's main artificial harbour (a man-made basin closed by rubble mound breakwaters). Mumbai is a natural harbour; Mormugao exports iron ore.",
        None, 15)
    S.q("ga-iam-p5", "medium", "Mumbai High is famous as a/an:",
        ["Offshore oil and natural gas field", "Mountain pass", "Deep-water port", "Iron-ore belt"], "Offshore oil and natural gas field",
        "**Mumbai High** is an offshore field in the Arabian Sea, about 160 km west of Mumbai; oil and gas are piped ashore to refineries at Mumbai and elsewhere.",
        None, 20)
    S.q("ga-iam-p5", "medium", "The Kandla (Deendayal) port on the Gulf of Kutch is best known as a —",
        ["Riverine port", "Tidal port", "Container-only port", "Naval base"], "Tidal port",
        "Ships at **Kandla** depend on the tide to enter and leave its basins - hence 'tidal port'. Kolkata is the riverine port; JNPT handles the most containers among major ports.",
        None, 20)
    return S


def build_parks():
    S = Sub("ig-parks")
    S.notes = NOTES["ig-parks"].strip()
    S.pattern("ga-pk-p1", "Protection years: first NP, Project Tiger, biosphere, Project Elephant", "common",
        "'Which was the first national park', 'Project Tiger was launched in', 'first biosphere reserve'.",
        None,
        "1. Chain: **1936** - Hailey NP (now **Jim Corbett**, Uttarakhand); **1973** - Project Tiger (from Corbett); **1986** - **Nilgiri** biosphere reserve; **1992** - Project Elephant.\n2. Project Tiger is the flagship conservation programme; Corbett is its first reserve.\n3. The biosphere-reserve idea (11 in the first list) is different from a national park - do not mix the two 'firsts'.",
        "Project Tiger, launched in 1973, began with which reserve?",
        "**Jim Corbett National Park** (Uttarakhand) - which itself was India's first national park, set up in 1936 as Hailey National Park.")
    S.pattern("ga-pk-p2", "National park ↔ state/UT", "very common",
        "A park name with four states as options, or 'how many parks does X state have'.",
        None,
        "1. Assam: Kaziranga, Manas, Dibru-Saikhowa, Nameri. MP: Kanha, Bandhavgarh, Pench, Panna, Satpura, Kuno.\n2. Rajasthan: Ranthambore, Sariska, Keoladeo, Desert NP. Kerala: Silent Valley, Eravikulam, Periyar.\n3. Special states: **Hemis - Ladakh**, **Dachigam - J&K**, **Keibul Lamjao - Manipur**, **Namdapha - Arunachal Pradesh**, **Bhitarkanika - Odisha**, **Khangchendzonga - Sikkim**. **Madhya Pradesh has the most national parks.**",
        "Kaziranga National Park, a UNESCO World Heritage Site, is located in which state?",
        "**Assam**, on the southern bank of the Brahmaputra. Manas is the state's other famous UNESCO-listed park.")
    S.pattern("ga-pk-p3", "Park ↔ famous animal", "very common",
        "'Which park is famous for one-horned rhinoceros', 'Asiatic lion is found in', 'only floating national park', animal-first recall.",
        None,
        "1. Rhino - **Kaziranga**; lion - **Gir** (Gujarat); tahr - **Eravikulam**; lion-tailed macaque - **Silent Valley**; hangul - **Dachigam**; snow leopard - **Hemis**.\n2. Sangai deer in the **only floating NP - Keibul Lamjao** on Loktak lake (Manipur); saltwater crocodile - **Bhitarkanika**; four big cats - **Namdapha**.\n3. Tigers have many parks (Kanha, Bandhavgarh, Ranthambore, Sundarbans) - the question usually gives a rarer animal.",
        "The Asiatic lion's last natural home is —",
        "**Gir National Park** (Gir forest, Gujarat). Kaziranga shelters the one-horned rhino; Dachigam the hangul deer.")
    S.pattern("ga-pk-p4", "UNESCO natural heritage sites and protected-area categories", "occasional",
        "'Which national park is a World Heritage Site', 'Khangchendzonga is what type of site', 'biosphere reserve vs national park'.",
        None,
        "1. UNESCO natural sites: Kaziranga, Manas, Keoladeo (1985), Sundarbans (1987), Nanda Devi & Valley of Flowers, Great Himalayan NP, Western Ghats cluster, Khangchendzonga.\n2. **Khangchendzonga (Sikkim, 2016)** is India's first **mixed** heritage site (nature + culture).\n3. Categories: national park (strictest) > wildlife sanctuary > biosphere reserve (largest, includes people); Ramsar sites are wetlands.",
        "Khangchendzonga National Park, inscribed on the World Heritage list in 2016, is special because it is —",
        "A **mixed** heritage site - it is valued for both its natural features and the culture of the Sikkimese people. It lies in Sikkim.")
    S.pattern("ga-pk-p5", "Wetlands, sanctuaries and mass-nesting sites", "occasional",
        "'Olive Ridley turtles nest at', 'which lake has Irrawaddy dolphins', 'phumdis are found in', Ramsar wetlands.",
        None,
        "1. **Gahirmatha** (Odisha) marine sanctuary - mass nesting (*arribada*) of **Olive Ridley turtles**; the Odisha coast also has Rushikulya nesting beaches.\n2. **Chilika** lake (Odisha) - Irrawaddy dolphins and winter migratory birds; **Loktak** (Manipur) - floating *phumdis*.\n3. Keoladeo (Bharatpur) - the classic bird sanctuary; the Siberian crane once wintered there.",
        "Olive Ridley turtles are famous for mass nesting (arribada) at which place?",
        "**Gahirmatha**, on the Odisha coast - a marine sanctuary where lakhs of turtles nest together; Rushikulya is the other Odisha nesting beach.")

    S.q("ga-pk-p1", "easy", "Which was the first national park of India?",
        ["Kaziranga", "Jim Corbett", "Gir", "Kanha"], "Jim Corbett",
        "**Jim Corbett NP** (Uttarakhand), established in **1936** as Hailey National Park, is India's first national park and the first Project Tiger reserve (1973).",
        None, 15)
    S.q("ga-pk-p1", "medium", "Project Tiger was launched in:",
        ["1969", "1973", "1986", "1992"], "1973",
        "**Project Tiger** began in **1973** from Corbett. 1986 = first biosphere reserve (Nilgiri); 1992 = Project Elephant.",
        "Year chain: 36 - 73 - 86 - 92.", 20)
    S.q("ga-pk-p1", "medium", "India's first biosphere reserve, set up in 1986, is:",
        ["Gulf of Mannar", "Nilgiri", "Nanda Devi", "Sundarbans"], "Nilgiri",
        "The **Nilgiri Biosphere Reserve** (1986) spans Tamil Nadu, Kerala and Karnataka at the junction of the Western and Eastern Ghats. Gulf of Mannar and Nanda Devi came in the later lists.",
        None, 25)
    S.q("ga-pk-p1", "hard", "Project Elephant, launched in 1992, is a scheme of the Government of India for:",
        ["Capturing wild elephants for temples", "Conservation of elephants and their habitats", "Export of ivory", "Domesticating elephants for forest work"], "Conservation of elephants and their habitats",
        "**Project Elephant (1992)** protects elephants, their corridors and habitats, and addresses man-animal conflict. Elephant was declared a National Heritage Animal of India in 2010.",
        None, 25)
    S.q("ga-pk-p2", "easy", "Dachigam National Park, the home of the hangul (Kashmir stag), is located in:",
        ["Himachal Pradesh", "Jammu & Kashmir", "Uttarakhand", "Ladakh"], "Jammu & Kashmir",
        "**Dachigam NP** near Srinagar (J&K) protects the **hangul**. Hemis, the snow-leopard park, is in the adjoining UT of Ladakh.",
        None, 15)
    S.q("ga-pk-p2", "medium", "Silent Valley National Park, famous for the lion-tailed macaque, is in which state?",
        ["Karnataka", "Tamil Nadu", "Kerala", "Andhra Pradesh"], "Kerala",
        "**Silent Valley** (Palakkad district, Kerala) preserves a rare stretch of untouched rainforest and the endangered **lion-tailed macaque**. Eravikulam (Nilgiri tahr) is also in Kerala.",
        None, 20)
    S.q("ga-pk-p2", "medium", "Which national park lies in Manipur?",
        ["Namdapha", "Keibul Lamjao", "Bhitarkanika", "Dudhwa"], "Keibul Lamjao",
        "**Keibul Lamjao** (Manipur) is the world's **only floating national park**, on the phumdis of Loktak lake. Namdapha is in Arunachal Pradesh; Bhitarkanika in Odisha; Dudhwa in UP.",
        None, 20)
    S.q("ga-pk-p2", "hard", "Which state has the largest number of national parks in India?",
        ["Rajasthan", "Madhya Pradesh", "Assam", "Uttarakhand"], "Madhya Pradesh",
        "**Madhya Pradesh** (Kanha, Bandhavgarh, Pench, Panna, Satpura, Kuno, Madhav, Van Vihar and others) tops the list - it is also called the 'Tiger State'.",
        None, 25)
    S.q("ga-pk-p3", "easy", "The one-horned rhinoceros is mainly protected in which national park?",
        ["Gir", "Kaziranga", "Kanha", "Ranthambore"], "Kaziranga",
        "**Kaziranga NP** (Assam) holds the largest population of the **one-horned rhinoceros**; it is also a tiger reserve and a UNESCO site (1985).",
        None, 15)
    S.q("ga-pk-p3", "easy", "The last remaining natural habitat of the **Asiatic lion** is:",
        ["Bandipur", "Gir", "Sundarbans", "Corbett"], "Gir",
        "The **Gir forest** (Gujarat) is the only natural home of the Asiatic lion. Bandipur has tigers and elephants; Sundarbans the Royal Bengal tiger in mangroves.",
        None, 15)
    S.q("ga-pk-p3", "medium", "The Keibul Lamjao National Park, home of the Sangai deer, is unique because it —",
        ["Is the largest national park of India", "Floats on a lake", "Is a marine park", "Lies above 5,000 m"], "Floats on a lake",
        "**Keibul Lamjao** floats on the **phumdis** (floating vegetation mats) of **Loktak lake** in Manipur - the only floating national park in the world.",
        None, 20)
    S.q("ga-pk-p3", "medium", "The Nilgiri tahr, an endangered mountain goat, is protected mainly at:",
        ["Eravikulam National Park", "Periyar Reserve", "Bandipur National Park", "Nagarhole National Park"], "Eravikulam National Park",
        "**Eravikulam NP** (Kerala, Anaimalai hills near Munnar) was created chiefly for the **Nilgiri tahr**. Periyar is known for elephants; Bandipur and Nagarhole for tigers.",
        None, 25)
    S.q("ga-pk-p3", "medium", "Which is the largest national park of India?",
        ["Hemis", "Kaziranga", "Kanha", "Sundarbans"], "Hemis",
        "**Hemis NP** (Ladakh, about 4,400 sq km) is India's largest national park and a key habitat of the **snow leopard**.",
        None, 25)
    S.q("ga-pk-p3", "hard", "In September 2022, cheetahs were reintroduced to India at which national park?",
        ["Kuno", "Panna", "Satpura", "Bandhavgarh"], "Kuno",
        "**Kuno National Park** (Madhya Pradesh) received cheetahs translocated from **Namibia** in September 2022, decades after the species died out in India.",
        None, 25)
    S.q("ga-pk-p3", "medium", "The hangul (Kashmir stag) is the state animal of Jammu & Kashmir and is found mainly in:",
        ["Hemis National Park", "Dachigam National Park", "Salim Ali National Park", "Kishtwar National Park"], "Dachigam National Park",
        "**Dachigam NP**, near Srinagar, is the main refuge of the **hangul**, a critically endangered central Asian red deer.",
        None, 25)
    S.q("ga-pk-p4", "medium", "Which of the following national parks was declared a UNESCO World Heritage Site in 1985?",
        ["Kaziranga", "Sundarbans", "Bhitarkanika", "Kuno"], "Kaziranga",
        "**Kaziranga**, **Manas** and **Keoladeo** were all inscribed in **1985**; the Sundarbans followed in 1987. Bhitarkanika and Kuno are not UNESCO natural sites.",
        "1985 trio: Kaziranga, Manas, Keoladeo.", 25)
    S.q("ga-pk-p4", "hard", "The Nanda Devi and Valley of Flowers National Parks in Uttarakhand are jointly inscribed on the World Heritage list. The Valley of Flowers is best known for:",
        ["Snow leopards", "Alpine meadows rich in wildflowers", "Mangrove forests", "Marine turtles"], "Alpine meadows rich in wildflowers",
        "The **Valley of Flowers** is a high-altitude Himalayan valley famous for its alpine flower meadows; the adjacent Nanda Devi park shelters snow leopard and Himalayan musk deer.",
        None, 30)
    S.q("ga-pk-p5", "medium", "Gahirmatha, famous for the mass nesting of Olive Ridley turtles, is a marine sanctuary in:",
        ["Andhra Pradesh", "Odisha", "West Bengal", "Tamil Nadu"], "Odisha",
        "**Gahirmatha** (Bhitarkanika coast, Odisha) hosts the world's largest known rookery of **Olive Ridley turtles**; Rushikulya, further south, is the other Odisha nesting site.",
        None, 25)
    S.q("ga-pk-p5", "easy", "Chilika lake, a Ramsar wetland famous for migratory birds and Irrawaddy dolphins, is in which state?",
        ["West Bengal", "Odisha", "Andhra Pradesh", "Assam"], "Odisha",
        "**Chilika** (Odisha) is India's largest brackish-water lagoon; Nalaban island inside it is a bird sanctuary. Pulicat (AP-TN) is the other big lagoon.",
        None, 15)
    return S
