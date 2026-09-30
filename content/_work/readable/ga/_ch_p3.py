"""Chemistry part 3: ch-organic-everyday."""
from _ch_common import pat, mis, trick

S = {}

# alkyne C2H2 fits CnH2n-2 with n=2
assert 2 * 2 - 2 == 2
# methane fits CnH2n+2 with n=1
assert 2 * 1 + 2 == 4

S["ch-organic-everyday"] = dict(
    concept=(
        "Carbon forms long chains, so it makes millions of compounds. "
        "This lesson covers carbon forms, fuels, polymers, factory processes and pollution. "
        "Nearly every question asks you to match a name to its product, use or effect."
    ),
    notes=r"""### Carbon and its forms
Carbon joins to itself in chains and rings. This is **catenation**. Its valency is 4, called tetravalency.

**Allotropes** are different forms of one element.

- **Diamond:** hardest natural substance. It does not conduct.
- **Graphite:** soft and slippery. It conducts electricity. It is used in pencils, electrodes and lubricants.
- **Fullerene (C₆₀):** a ball of 60 carbon atoms.
- **Graphene:** a single layer of graphite.

### Hydrocarbons
| Family | Bonds | General formula |
|---|---|---|
| Alkane | Single, saturated | $C_nH_{2n+2}$ |
| Alkene | One double bond | $C_nH_{2n}$ |
| Alkyne | One triple bond | $C_nH_{2n-2}$ |

Methane (CH₄) is the simplest alkane. Ethene is an alkene. Ethyne (acetylene, C₂H₂) is an alkyne.

### Fuels
| Fuel | Main component |
|---|---|
| CNG | Methane |
| LPG | Butane (with propane) |
| Biogas (gobar gas) | Methane, plus CO₂ |
| Oxy-acetylene flame | Ethyne (acetylene), for welding and cutting |
| Water gas | CO + H₂ |
| Producer gas | CO + N₂ |

- LPG has no smell. **Ethyl mercaptan** is added so a leak can be smelt.
- Hydrogen has the highest calorific value by mass.
- Octane number rates petrol. Cetane number rates diesel.
- Coal ranks by carbon: peat, lignite, bituminous, anthracite. Anthracite is best.
- Fractional distillation splits petroleum into refinery gas, petrol, naphtha, kerosene, diesel, lubricating oil and bitumen.
- Ethylene ripens fruit. Calcium carbide is banned for this.

### Everyday carbon compounds
- **Methanol** is poisonous. It can cause blindness. **Ethanol** is the alcohol in drinks and is blended with petrol.
- **Vinegar** is about 5 to 8% acetic acid.
- **Esters** give fruits their smell.
- **Soap** is a sodium or potassium salt of a long-chain fatty acid. **Saponification** (fat + NaOH) makes it.
- Soap forms scum in hard water. **Detergents** work in hard water too.
- **Hydrogenation** of vegetable oil uses a nickel catalyst. It gives vanaspati ghee.

> **Watch:** Methanol is poison. Ethanol is the drinking alcohol.

### Polymers
A polymer is a giant molecule made of repeating units.

| Polymer | Note |
|---|---|
| Polythene | From ethene; bags |
| PVC | From vinyl chloride; pipes |
| Teflon | From tetrafluoroethylene; non-stick cookware |
| Bakelite | Phenol + formaldehyde; first plastic; thermosetting; switches |
| Nylon | First fully synthetic fibre |
| Natural rubber | Polyisoprene |
| Rayon | Artificial silk from cellulose |
| Melamine | Thermosetting; crockery |

- **Vulcanisation** heats rubber with sulphur (Charles Goodyear). It makes rubber hard and elastic.
- **Thermoplastics** (polythene, PVC) soften on heating. **Thermosetting plastics** (Bakelite, melamine) do not.

### Factory processes
| Process | Product | Catalyst |
|---|---|---|
| Haber | Ammonia | Iron |
| Contact | Sulphuric acid | Vanadium pentoxide (V₂O₅) |
| Ostwald | Nitric acid | Platinum |
| Solvay | Sodium carbonate | none |
| Chlor-alkali | NaOH, Cl₂ and H₂ from brine | none |

Glass is silica (sand), sodium carbonate and limestone fused together. Borosilicate (Pyrex) resists heat. Portland cement was made by Joseph Aspdin. Gypsum is added to slow its setting.

### Pollution and poisons
| Substance | Effect |
|---|---|
| SO₂, NO₂ | Acid rain; damage to the Taj Mahal |
| CFCs | Ozone layer depletion |
| CO₂, CH₄, N₂O, water vapour | Greenhouse effect |
| Carbon monoxide | Binds haemoglobin; suffocation |
| Methyl isocyanate (MIC) | Bhopal gas tragedy, 1984 |
| Mercury | Minamata disease, Japan |
| Cadmium | Itai-itai disease, Japan |
| Arsenic | Black-foot disease; groundwater |
| Excess fluoride | Fluorosis of teeth and bones |
| Nitrate in water | Blue baby syndrome |
| Lead | Plumbism |

> **Tip:** Minamata starts with M, like Mercury. Itai-itai means ouch-ouch, and cadmium is the cause.
""",
    tricks=[
        trick("Process to product",
              "Haber gives ammonia. Contact gives sulphuric acid. Ostwald gives nitric acid. Solvay gives soda. Catalysts: Haber Fe, Contact V₂O₅, Ostwald Pt.",
              "Which catalyst is used in the Contact process?",
              ["The Contact process makes sulphuric acid.", "Its catalyst is vanadium pentoxide."],
              "V₂O₅"),
        trick("Japanese diseases",
              "Minamata goes with mercury. Itai-itai (bone pain) goes with cadmium."),
    ],
    mistakes=[
        mis("Saying LPG is mainly methane.", "LPG is mainly butane. CNG and biogas are mainly methane."),
        mis("Calling Bakelite a thermoplastic.", "Bakelite is thermosetting."),
        mis("Naming phosgene for the Bhopal tragedy.", "The gas was methyl isocyanate (MIC)."),
        mis("Mixing up methanol and ethanol.", "Methanol is poisonous. Ethanol is the drinking alcohol."),
        mis("Saying detergent forms scum in hard water.", "Soap forms scum. Detergents work in hard water."),
    ],
    revision=[
        "CNG and biogas: methane. LPG: butane with ethyl mercaptan for smell. Welding: acetylene.",
        "Anthracite is the best coal.",
        "Haber: NH₃. Contact: H₂SO₄. Ostwald: HNO₃. Solvay: Na₂CO₃.",
        "Nylon is the first synthetic fibre. Bakelite is the first plastic.",
        "Vulcanisation is rubber plus sulphur. Teflon is non-stick.",
        "Hydrogenation uses a nickel catalyst. Soap scums in hard water.",
        "CO binds haemoglobin. Minamata: Hg. Itai-itai: Cd. CFC: ozone. Bhopal: MIC, 1984.",
    ],
    patterns=[
        pat("ga-or-p1", "Fuel and main component", "very common",
            "The question says 'CNG is mainly', 'LPG contains', 'why does LPG smell', 'gas used in welding' or 'best coal'.",
            ["CNG and biogas are methane.", "LPG is butane with propane. Ethyl mercaptan gives it a smell.", "Welding uses acetylene (ethyne) with oxygen.", "Coal ranking: peat, lignite, bituminous, anthracite."],
            "Each fuel is a named hydrocarbon, so the answer is recall plus one use.",
            "Which gas is used with oxygen in a welding torch?",
            ["The flame must be very hot.", "The gas is ethyne."],
            "Acetylene (ethyne)"),
        pat("ga-or-p2", "Industrial process and product", "very common",
            "The question says 'Haber process gives', 'sulphuric acid is made by', or gives a match-the-column of processes and chemicals.",
            ["Fix four pairs: Haber-ammonia, Contact-sulphuric acid, Ostwald-nitric acid, Solvay-sodium carbonate.", "Add catalysts: Haber iron, Contact V₂O₅, Ostwald platinum.", "Anchor on ammonia and eliminate the rest."],
            "Each process is named after its inventor or its method and is fixed.",
            "The Contact process makes which chemical?",
            ["SO₂ is oxidised to SO₃ over V₂O₅.", "SO₃ is absorbed to make the acid."],
            "Sulphuric acid (H₂SO₄)"),
        pat("ga-or-p3", "Polymers, plastics and fibres", "very common",
            "The question asks the first synthetic fibre, the first plastic, a use of Teflon, or what vulcanisation uses.",
            ["Records: nylon is the first fully synthetic fibre. Bakelite is the first plastic.", "Uses: polythene bags, PVC pipes, Teflon non-stick, nylon ropes and parachutes.", "Vulcanisation is natural rubber with sulphur.", "Cotton is cellulose. Silk and wool are protein."],
            "Polymers are named for their monomer or their use, and exams test both.",
            "Vulcanised rubber is made by heating natural rubber with what?",
            ["Goodyear found the method.", "The added element is sulphur."],
            "Sulphur"),
        pat("ga-or-p4", "Allotropes and hydrocarbon families", "common",
            "The question asks which carbon form conducts, the hardest natural substance, a general formula, or which hydrocarbon is saturated.",
            ["Diamond is hardest and does not conduct. Graphite conducts.", "Alkane $C_nH_{2n+2}$ is saturated. Alkene $C_nH_{2n}$. Alkyne $C_nH_{2n-2}$.", "Methane is the simplest alkane."],
            "A double or triple bond takes the place of hydrogen atoms, so the formula loses hydrogens.",
            "Which general formula belongs to an alkyne?",
            ["An alkyne has a triple bond.", "Acetylene C₂H₂ fits $C_nH_{2n-2}$ with n = 2."],
            "$C_nH_{2n-2}$"),
        pat("ga-or-p5", "Everyday carbon chemistry", "common",
            "The question asks which alcohol causes blindness, what vinegar contains, why soap fails in hard water, or the catalyst for hydrogenation.",
            ["Methanol is poison. Ethanol is drinkable.", "Vinegar is 5 to 8% acetic acid.", "Soap is made by saponification and forms scum in hard water.", "Hydrogenation of oil uses nickel and gives vanaspati."],
            "Each item links one chemical to one everyday fact.",
            "Why does soap not lather well in hard water?",
            ["Hard water has calcium and magnesium ions.", "They react with soap to form insoluble scum."],
            "Scum forms; detergents work even in hard water"),
        pat("ga-or-p6", "Pollutant and disease or event", "common",
            "The question says 'Minamata disease is caused by', 'which gas causes acid rain', 'CFCs damage', or 'Bhopal gas leaked'.",
            ["Minamata: mercury. Itai-itai: cadmium.", "CO binds haemoglobin far more strongly than oxygen.", "SO₂ and NOₓ cause acid rain. CFCs harm the ozone layer (Montreal Protocol 1987).", "Bhopal 1984 was methyl isocyanate. Greenhouse gases: CO₂, CH₄."],
            "Each pollutant harms one target, and exams pair them.",
            "Minamata disease resulted from poisoning by which metal?",
            ["Factory waste in Japan entered fish.", "The pollutant was mercury."],
            "Mercury (cadmium caused itai-itai)"),
    ],
)
