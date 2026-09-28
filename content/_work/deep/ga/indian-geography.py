"""Phase-2 deep content for ga/indian-geography. Run: py -3 indian-geography.py"""
import os
import sys

sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
from _lib import apply_topic
from ig_part1 import build_location, build_physio, build_rivers
from ig_part2 import build_climate, build_agri, build_parks


def P(pattern, frequency, howToSpot, approach, subtopic, q, sol):
    return {"pattern": pattern, "frequency": frequency, "howToSpot": howToSpot, "approach": approach,
            "subtopic": subtopic, "example": {"q": q, "solution": sol}}


PYQ = [
    P("Pass / national park / dam → state or river", "very common",
      "A place name is given with four states (Nathu La, Kuno, Kaziranga) or four rivers (Hirakud, Tehri, Sardar Sarovar); sometimes an animal is matched to a park.",
      "Keep three grouped tables in your head: passes and peaks by state, dam-river pairs, and the animal-first park list (rhino-Kaziranga, lion-Gir, hangul-Dachigam). Strike options from the wrong region first; the odd one usually belongs to a neighbouring state's list.",
      "ig-physiography",
      "The Sardar Sarovar dam is built on which river?",
      "The **Narmada** (Gujarat). Tehri - Bhagirathi, Hirakud - Mahanadi, Bhakra Nangal - Sutlej are the neighbours in the same table."),
    P("River origin / confluence / tributary", "very common",
      "'Which river rises at Amarkantak?', 'Devprayag is the meeting place of', 'which is a left-bank tributary of the Ganga'.",
      "Learn peninsular sources as flashcards (Godavari-Trimbakeshwar, Krishna-Mahabaleshwar, Kaveri-Talakaveri, Narmada-Son-Amarkantak) and the Panch Prayag chain 'Very Nice Kids Read Daily' for the Alaknanda confluences. For tributaries, remember that peninsular rivers (Yamuna system, Son) join the Ganga on the right bank.",
      "ig-rivers",
      "The Bhagirathi and the Alaknanda meet at —",
      "**Devprayag**, where the Ganga proper is said to be formed; the Alaknanda has already received the Dhauliganga, Nandakini, Pindar and Mandakini upstream."),
    P("Soil type properties and crops", "common",
      "'Regur soil is best suited for', 'which soil is formed by leaching', 'black soil is deficient in', 'khadar differs from bhangar how'.",
      "Link each soil to its parent rock or process and one signature crop: black (basalt)-cotton, laterite (leaching)-tea/cashew, alluvial-rice-wheat, arid-millet. For deficiency questions, black soil is rich in lime-iron-magnesia-potash but poor in nitrogen, phosphorus and humus.",
      "ig-climate-soils",
      "Which soil is formed by intense leaching in hot, wet regions?",
      "**Laterite** soil - poor in humus, rich in iron and aluminium, and brick-hard when dry; with manuring it grows tea, coffee and cashew."),
    P("Tropic of Cancer / Standard Meridian / neighbour borders", "common",
      "'Which state does NOT lie on the Tropic of Cancer', 'longest/shortest border is with', '82°30'E passes through'.",
      "Two 5-8 state lists settle everything: Tropic - Gujarat, Rajasthan, MP, Chhattisgarh, Jharkhand, WB, Tripura, Mizoram; Meridian 82°30'E - UP, MP, Chhattisgarh, Odisha, AP. Border order: Bangladesh > China > Pakistan > Nepal > Myanmar > Bhutan > Afghanistan.",
      "ig-location",
      "India's longest international land border is with which country?",
      "**Bangladesh** (about 4,097 km), touching WB, Assam, Meghalaya, Tripura and Mizoram; the shortest is Afghanistan (106 km)."),
    P("Crop season and agricultural revolutions", "common",
      "'Which is a rabi crop?', 'Operation Flood is associated with', 'the Blue Revolution relates to'.",
      "Monsoon-sown = kharif (rice, cotton, jute, maize); winter-sown = rabi (wheat, gram, mustard); summer = zaid (melons). Match revolution colours to products - Green food grains, White milk (Kurien), Blue fish, Yellow oilseeds, Silver eggs.",
      "ig-agri-minerals",
      "Which of the following is a rabi crop?",
      "**Wheat** (also gram, barley, mustard). Rice, cotton, jute and maize belong to the kharif season."),
    P("Mineral / oil field / port location", "occasional",
      "'Jharia is famous for', 'which is the oldest oil refinery', 'which port is called tidal', match-the-column on minerals and ports.",
      "Learn the mineral-place table as flashcards: Jharia-coking coal, Neyveli-lignite, Digboi-first refinery, Bailadila-iron, Koderma-mica, Khetri-copper, Zawar-zinc, Hutti-gold (Kolar closed). Port adjectives: tidal-Kandla, artificial-Chennai, riverine-Kolkata, deepest landlocked-Visakhapatnam, containers-JNPT.",
      "ig-agri-minerals",
      "Which of these ports is known as a riverine port?",
      "**Kolkata (Syama Prasad Mookerjee Port)** - about 128 km up the Hugli, with the Haldia dock downstream."),
    P("Local winds and monsoon features", "occasional",
      "'Mango showers occur in', 'Kalbaisakhi benefits which crop', 'October heat', 'which wind brings winter rain to Punjab'.",
      "Pair each wind/shower with region and crop: Loo-summer north India, mango showers-Kerala-Karnataka mango, blossom showers-coffee, Kalbaisakhi-Bengal-Assam tea/jute, western disturbances-rabi wheat. Tamil Nadu's main rain comes from the retreating (NE) monsoon in Oct-Dec.",
      "ig-climate-soils",
      "The pre-monsoon thunderstorms called Kalbaisakhi are most common in —",
      "**West Bengal and Assam** (March-May); they help the tea and jute crops. In Assam the same season's wind is called Bordoichila."),
]

if __name__ == "__main__":
    subs = [build_location(), build_physio(), build_rivers(),
            build_climate(), build_agri(), build_parks()]
    apply_topic("indian-geography", subs, PYQ)
