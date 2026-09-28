"""Phase-2 deep content for ga/chemistry. Run: py -3 chemistry.py"""
import os
import sys

sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
from _lib import apply_topic
from chem_part1 import build_matter, build_periodic
from chem_part2 import build_acids, build_metals, build_organic


def P(pattern, frequency, howToSpot, approach, subtopic, q, sol):
    return {"pattern": pattern, "frequency": frequency, "howToSpot": howToSpot, "approach": approach,
            "subtopic": subtopic, "example": {"q": q, "solution": sol}}


PYQ = [
    P("Common name → chemical name/formula", "very common",
      "'Baking soda is chemically…', 'the formula of washing soda / bleaching powder / plaster of Paris', 'which is called oil of vitriol', wrong-pair questions on the common-names table.",
      "Hold one master table: baking soda NaHCO₃, washing soda Na₂CO₃·10H₂O, caustic soda NaOH, bleaching powder Ca(OCl)Cl, plaster of Paris CaSO₄·½H₂O, gypsum CaSO₄·2H₂O, quicklime CaO, limestone CaCO₃, plus the vitriols (oil–H₂SO₄, blue–CuSO₄·5H₂O, green–FeSO₄·7H₂O, white–ZnSO₄). In wrong-pair questions, test the Ca-family against the Na-family first.",
      "ch-acids-compounds",
      "Plaster of Paris is chemically:",
      "Calcium sulphate hemihydrate, CaSO₄·½H₂O — made by heating gypsum (CaSO₄·2H₂O); it sets back to gypsum with water."),
    P("Natural source → acid", "very common",
      "'The acid in tamarind / curd / tomato / lemon / ant sting', match-the-column of foods, stings and acids.",
      "Kitchen map: vinegar–acetic, lemon/orange–citric, tamarind and grapes–tartaric, tomato and spinach–oxalic, curd–lactic, apple–malic, ant sting and nettle–formic, stomach–HCl. Traps to kill: tamarind is tartaric (not citric), tomato is oxalic.",
      "ch-acids-compounds",
      "The acid present in an ant sting is:",
      "Formic (methanoic) acid — neutralised by rubbing a mild base such as baking soda."),
    P("Indicators and pH", "very common",
      "'Phenolphthalein is colourless in…', 'turmeric turns…with a base', 'the pH of blood / the tooth-decay threshold', 'solution of pH 4 vs pH 6 — which is more acidic'.",
      "Colours: litmus blue→red in acid; phenolphthalein colourless in acid, pink in base; methyl orange red in acid, yellow in base; turmeric reddish-brown in base. pH ladder: gastric ≈ 1–2, lemon ≈ 2, water 7, blood ≈ 7.4, tooth decay < 5.5, acid rain < 5.6; each unit is a ten-fold change.",
      "ch-acids-compounds",
      "Phenolphthalein gives which colour in a basic solution?",
      "Pink — it is colourless in acids. 'Pink in Base' is the pair to remember."),
    P("Ore → metal and alloy → composition", "very common",
      "'Bauxite / cinnabar / galena / pitchblende is the ore of…', 'brass / bronze / solder / stainless steel is an alloy of…', 'which alloy contains tin'.",
      "Two lists. Ores: bauxite–Al, haematite–Fe, cinnabar–Hg, galena–Pb, zinc blende–Zn, cassiterite–Sn, copper pyrites–Cu, pitchblende–U, rock salt–Na. Alloys: brass Cu+Zn, bronze Cu+Sn, solder Pb+Sn, stainless Fe+Cr+Ni, duralumin Al+Cu, nichrome Ni+Cr, amalgam metal+Hg. The classic trap is brass–Zn vs bronze–Sn.",
      "ch-metals-ores",
      "Brass is an alloy of:",
      "Copper and zinc. Bronze is the copper–tin alloy — the most common wrong option."),
    P("Periodic table and element records", "very common",
      "'Who is the father of the periodic table', 'which is the lightest / most abundant element', symbols from Latin names, element by group (alkali, halogen, noble gas), modern vs Mendeleev.",
      "Anchor facts: Mendeleev–periodic table (by atomic weight), Moseley–modern (by atomic number), Newlands–octaves, Doberiener–triads; H lightest, He most abundant in the universe, O most abundant in the earth's crust, Fe most abundant metal in the crust; Na from natrium, K from kalium, Au from aurum, Fe from ferrum; Group 1 alkali, 17 halogen, 18 noble gases; 7 periods, 18 groups.",
      "ch-periodic",
      "The chemical symbol of sodium, from its Latin name, is:",
      "Na (natrium). Potassium is K (kalium), gold Au (aurum), iron Fe (ferrum)."),
    P("Industrial process, polymer or fuel component", "very common",
      "'The Haber process gives…', 'CNG / LPG / biogas mainly contains…', 'first synthetic fibre / first plastic', 'vulcanisation is done with…', 'which process makes sulphuric acid'.",
      "Processes: Haber–NH₃, Contact–H₂SO₄, Ostwald–HNO₃, Solvay–Na₂CO₃. Fuels: CNG and biogas–methane, LPG–butane (ethyl mercaptan for smell), welding–acetylene, best coal–anthracite. Polymers: nylon first synthetic fibre, bakelite first plastic, Teflon non-stick, PVC pipes, vulcanisation = rubber + sulphur.",
      "ch-organic-everyday",
      "The Solvay process is used to manufacture:",
      "Sodium carbonate (washing soda). Haber gives ammonia, Contact gives sulphuric acid, Ostwald gives nitric acid."),
    P("Pollutant → disease/disaster", "common",
      "'Minamata disease is caused by…', 'the Bhopal gas tragedy leaked…', 'which gas causes acid rain', 'CFCs deplete…', 'why is carbon monoxide poisonous'.",
      "Pairs: Minamata–mercury, itai-itai–cadmium (both Japan); Bhopal 1984–methyl isocyanate; acid rain–SO₂ + NOₓ; ozone hole–CFCs (Montreal Protocol 1987); CO binds haemoglobin ~200× more strongly than oxygen; greenhouse gases CO₂/CH₄ (Kyoto 1997, Paris 2015).",
      "ch-organic-everyday",
      "Minamata disease is caused by poisoning with:",
      "Mercury — contaminated fish in Minamata Bay, Japan. Cadmium is the itai-itai culprit."),
    P("Atomic structure and isotopes", "common",
      "'Who discovered the electron / proton / neutron', 'the number of electrons in an atom equals…', 'isotopes differ in…', 'maximum electrons in a shell', 'which radiation is charged'.",
      "Discoverers: electron–J.J. Thomson, proton–Goldstein, neutron–Chadwick, nucleus–Rutherford, planetary model–Bohr. Identity rules: atomic number Z = protons = electrons; mass number A = protons + neutrons; isotopes differ in neutrons, isobars in mass number. Shell n holds 2n² (2, 8, 18, 32). Cathode rays = electrons; α-particles are positive, β negative, γ neutral.",
      "ch-matter-atom",
      "Isotopes of an element differ in the number of:",
      "Neutrons — same protons (so same element), different mass numbers. Isobars instead share the mass number."),
]

if __name__ == "__main__":
    subs = [build_matter(), build_periodic(), build_acids(), build_metals(), build_organic()]
    apply_topic("chemistry", subs, PYQ)
