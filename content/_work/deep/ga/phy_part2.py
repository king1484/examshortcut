"""physics deep content — part 2: ph-light, ph-modern-scientists."""
import os
import sys

sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
from _lib import Sub


def g(x):
    x = round(x, 6)
    return str(int(x)) if x == int(x) else str(x)


def build_light():
    S = Sub("ph-light")
    S.notes = """### Light — the basics
Light is a form of energy that makes things visible; in one medium it moves in straight lines (that is why shadows form). Its speed in vacuum is **c ≈ 3 × 10⁸ m/s** — the highest speed in the universe; in water or glass it slows down. **Refractive index** n = c / v, so in glass (n ≈ 1.5) light moves at about 2 × 10⁸ m/s. Sunlight takes about **8 minutes 20 seconds** to reach the Earth.

### Mirrors — which one for which job
| Mirror | Image | Standard uses |
|---|---|---|
| **Plane** | Virtual, erect, same size, **laterally inverted** | Looking glass, periscope (two mirrors at 45°) |
| **Concave** (converging) | Real inverted when the object is far; **magnified virtual image** when close | **Shaving and make-up mirrors, dentist's mirror**, torch/headlight/searchlight reflectors, solar furnaces |
| **Convex** (diverging) | **Always virtual, erect, diminished**; wide field of view | **Rear-view mirrors** of vehicles, mirrors at dangerous road bends |
A concave mirror brings parallel rays to a focus, so it collects the Sun's heat (solar furnace) or sends lamp light out as a beam (headlight). A convex mirror shows a wide, upright view of the traffic behind.

### Lenses — converging and diverging
A **convex lens** (thicker in the middle) converges rays: it is the lens of a magnifying glass, camera, projector, microscope and telescope objective, and of the eye itself. Object within F → **magnified, erect, virtual** image (magnifier); object beyond 2F → **real, inverted, diminished** image (camera). A **concave lens** always forms a **virtual, erect, diminished image** of a real object; it corrects short sight.
**Power** P = 1/f with f in **metres**; unit **dioptre (D)**. Convex power is positive, concave negative. Lenses in contact: powers simply add.

### The eye and its defects
The eye's lens forms a **real, inverted** image on the **retina**; the brain reads it upright. The nearest clear-vision distance is about **25 cm**; the far point is at infinity. **Rods** see in dim light, **cones** sense colour. About **1/16 s** of persistence of vision makes cinema possible.
| Defect | What goes wrong | Correction |
|---|---|---|
| **Myopia** (short-sightedness) | Distant objects blur — image forms **in front of** the retina (eyeball too long) | **Concave (diverging) lens** |
| **Hypermetropia** (long-sightedness) | Near objects blur — image forms **behind** the retina (eyeball too short) | **Convex (converging) lens** |
| **Presbyopia** | Old age — lens loses flexibility | **Bifocal lens** (concave top, convex bottom) |
| **Astigmatism** | Uneven curvature of the cornea | **Cylindrical lens** |
| **Cataract** | Lens turns **opaque** | Surgery; artificial lens implanted |
**Colour blindness** is not a lens problem — the retinal cones lack some colour sensors — so **no lens can correct it**; red–green confusion is the common type.

### Refraction and total internal reflection
When light passes obliquely between transparent media, it **bends (refraction)** because its speed changes: towards the normal entering a denser medium, away in a rarer one. Effects: a pencil in water looks **bent**, a pool looks **shallower**, stars **twinkle** (shifting atmospheric refraction; planets hardly twinkle), and the Sun is visible about **2 minutes before** actual sunrise and after actual sunset.
When light inside a denser medium hits the boundary with a rarer one beyond the **critical angle**, it is completely reflected back — **total internal reflection (TIR)**. This gives the **sparkle of a diamond**, carries calls through **optical fibres**, guides the endoscope, and creates the **mirage** in deserts.

### Dispersion and scattering — why the world is coloured
White light is a **mixture of seven colours** (VIBGYOR). A **prism splits it (dispersion)** because each colour bends differently: **violet most, red least**. Newton proved this by recombining the colours with a second prism. A **rainbow** is nature's prism: sunlight dispersed and totally internally reflected inside raindrops, seen with the **Sun behind** the observer; in the primary rainbow **red is on the outside**.
**Scattering** by tiny air molecules is strongest for short wavelengths (about 1/λ⁴). So **the sky looks blue**, **the Sun looks red at sunrise and sunset** (blue is scattered away en route), and **danger signals are red** (least scattered, visible farthest). A red rose in green light looks almost black: it reflects only red.

### Quick revision
- c = 3 × 10⁸ m/s; n = c/v; sunlight ≈ 8 min 20 s.
- Plane: lateral inversion. Concave mirror: shaving, dentist, headlights. Convex: rear-view.
- P = 1/f (metres), dioptre; powers add for lenses in contact.
- Myopia–concave, hypermetropia–convex, presbyopia–bifocal, astigmatism–cylindrical, cataract–surgery.
- TIR: diamond sparkle, optical fibre, mirage. Refraction: bent pencil, twinkling, early sunrise.
- Prism: violet bends most. Sky blue, danger red, sunset red — scattering."""
    S.pattern("ga-li-p1", "Mirror ↔ image/use matching", "very common",
        "'Which mirror is used as a rear-view / shaving / dentist's mirror?', 'what type of image does a convex mirror always form', properties of a plane-mirror image.",
        None,
        "1. Job decides the mirror: wide upright view → **convex**; enlarged close view or beaming light → **concave**.\n2. Convex mirror always gives virtual, erect, diminished images.\n3. Plane mirror: virtual, erect, same size, laterally inverted, image as far behind as the object is in front.",
        "A **dentist's mirror** is a —",
        "**Concave mirror.** Held close to the tooth (inside the focus) it gives an erect, magnified image.")
    S.pattern("ga-li-p2", "Lens ↔ image/use matching", "very common",
        "'Which lens is used in a magnifier/camera/projector?', 'a concave lens always forms …', 'which lens converges light'.",
        None,
        "1. Converging = **convex lens**: magnifier, camera, projector, eye lens.\n2. Diverging = **concave lens**: always virtual–erect–diminished for real objects; corrects myopia.\n3. Magnifier condition: object inside the focal length → erect magnified virtual image.",
        "A camera lens produces an image that is —",
        "**Real, inverted and diminished.** The object is far beyond 2F, so the image lands between F and 2F, close to F.")
    S.pattern("ga-li-p3", "Eye defects and their correction", "very common",
        "A defect (myopia, hypermetropia, presbyopia, astigmatism, cataract, colour blindness) and its cause or corrective lens.",
        None,
        "1. Short-sighted = myopia → **concave lens**; long-sighted = hypermetropia → **convex lens** ('My-Con, Hyper-Vex').\n2. Old-age near+far both faulty → bifocal; uneven cornea → cylindrical; cloudy lens → cataract surgery.\n3. Colour blindness has **no lens correction** — reject any lens option.",
        "Presbyopia of old age is corrected by —",
        "**Bifocal lenses** — a convex lower part for reading and a concave upper part for distance.")
    S.pattern("ga-li-p4", "Power of a lens and light-speed numericals", "common",
        "Focal length given, power asked (or reverse), lenses in contact; or distance ÷ speed-of-light time.",
        r"P=\frac{1}{f(\text{m})}\ (\text{dioptre}),\quad P=P_1+P_2,\quad t=\frac{d}{c}",
        "1. Convert the focal length to metres first: 25 cm = 0.25 m.\n2. P = 1/f; convex +, concave −. For several thin lenses in contact, add the powers.\n3. Light questions: t = distance ÷ (3 × 10⁸ m/s).\nWhy: dioptre is defined as inverse metres, so the metre conversion is the only trap.",
        "Two thin lenses of powers **+2 D** and **−0.5 D** are placed in contact. Find the power and nature of the combination.",
        "P = 2 + (−0.5) = **+1.5 D** — converging, since the net power is positive.")
    S.pattern("ga-li-p5", "Refraction and total internal reflection effects", "very common",
        "A phenomenon (bent pencil, shallow pool, twinkling stars, early sunrise, mirage, optical fibre, diamond sparkle) and its cause.",
        None,
        "1. Object looks bent/displaced/shallow, stars twinkle, Sun rises early → **refraction**.\n2. Light stays inside (diamond sparkle, optical fibre, endoscope) or a mirage → **total internal reflection**.\n3. Refraction happens because light changes **speed** between media; TIR needs denser → rarer beyond the critical angle.",
        "Why do **stars twinkle** but planets hardly do?",
        "Starlight refracts through constantly shifting layers of the atmosphere, so its brightness flickers. Planets are much closer and act as extended sources, so the changes average out.")
    S.pattern("ga-li-p6", "Dispersion, scattering and colour facts", "very common",
        "Why the sky is blue, why danger signals are red, prism/VIBGYOR order, which colour bends most, rainbow facts, object colour in coloured light.",
        None,
        "1. Sky blue / sunset red / danger red → **scattering** (blue scatters most, red least).\n2. Prism splits white light: **violet bends most, red least** (VIBGYOR from bottom to top).\n3. Rainbow: dispersion + TIR in raindrops, Sun behind the observer, red on the outer edge of the primary bow.\n4. A body shows the colour it **reflects**; it looks black in light it fully absorbs.",
        "A red rose is seen in **green light**. What colour does it appear?",
        "Almost **black** — the rose reflects only red light and absorbs green.")

    P = 100 / 25
    assert P == 4
    S.q("ga-li-p1", "easy", "Which mirror is used as a **rear-view mirror** in vehicles?",
        ["Convex mirror", "Concave mirror", "Plane mirror", "Cylindrical mirror"], "Convex mirror",
        "A **convex mirror** always gives an erect, diminished image with a **wide field of view**, so the driver sees more traffic behind.",
        None, 15)
    S.q("ga-li-p1", "medium", "A **shaving mirror** gives an erect, magnified image of the face. It must be a —",
        ["Concave mirror with the face between the pole and focus", "Convex mirror", "Plane mirror", "Concave mirror with the face beyond the centre of curvature"], "Concave mirror with the face between the pole and focus",
        "A **concave mirror** gives an erect, enlarged, virtual image only when the object is inside the focal length — that is how a shaving mirror magnifies the chin.",
        None, 25)
    S.q("ga-li-p1", "easy", "The image formed by a **plane mirror** is always —",
        ["Virtual, erect and laterally inverted", "Real and inverted", "Virtual and diminished", "Real and magnified"], "Virtual, erect and laterally inverted",
        "A plane mirror forms a virtual, erect image of the **same size**, as far behind the mirror as the object is in front, with **left and right interchanged** (lateral inversion).",
        None, 15)
    S.q("ga-li-p2", "easy", "A **magnifying glass** is a —",
        ["Convex lens used with the object inside its focal length", "Concave lens used close to the eye", "Convex mirror", "Concave mirror"], "Convex lens used with the object inside its focal length",
        "A **convex lens** held close to the object (within F) gives an erect, magnified, virtual image — the working of a simple microscope.",
        None, 15)
    S.q("ga-li-p2", "medium", "A **concave lens**, when a real object is placed before it, always forms an image that is —",
        ["Virtual, erect and diminished", "Real and inverted", "Virtual and magnified", "Real and magnified"], "Virtual, erect and diminished",
        "A diverging (concave) lens spreads the rays apart, so they only seem to meet — the image is always **virtual, erect and smaller** than the object, wherever the real object is placed.",
        None, 20)
    S.q("ga-li-p2", "medium", "Which instrument produces a **real, inverted, diminished** image on a screen/film?",
        ["Camera", "Simple microscope", "Periscope", "Kaleidoscope"], "Camera",
        "In a **camera** the object lies far beyond 2F of the convex lens, so the image is real, inverted and smaller — formed on the film or sensor. A microscope magnifies; the periscope and kaleidoscope use plane mirrors only.",
        None, 20)
    S.q("ga-li-p3", "easy", "**Hypermetropia** (long-sightedness) is corrected by using a —",
        ["Convex lens", "Concave lens", "Cylindrical lens", "Bifocal lens"], "Convex lens",
        "In hypermetropia the image forms **behind** the retina; a **convex (converging) lens** brings the image forward onto the retina. ('Hyper-Vex'.)",
        None, 15)
    S.q("ga-li-p3", "medium", "The **least distance of distinct vision** for a normal human eye is about —",
        ["25 cm", "25 mm", "2.5 m", "Infinite"], "25 cm",
        "A normal adult eye cannot focus clearly on objects closer than about **25 cm**. The far point is at infinity.",
        None, 15)
    S.q("ga-li-p3", "hard", "Why can **colour blindness** not be corrected by any lens?",
        ["It is caused by missing/defective colour-sensing cones in the retina", "The cornea is uneven", "The eyeball is too long", "The eye lens has become opaque"], "It is caused by missing/defective colour-sensing cones in the retina",
        "Colour blindness is a defect of the **cones** (red–green sensors) of the retina, not of the lens or cornea, so no external lens can fix it. Cataract (opaque lens) is the only defect here treated by replacing the lens.",
        None, 25)
    f2, p2v = 50, 100 / 50
    assert p2v == 2
    nodiv = 1 / 25
    assert abs(nodiv - 0.04) < 1e-9
    S.q("ga-li-p4", "easy", "The power of a **convex lens of focal length 25 cm** is —",
        ["+" + g(P) + " D", "−" + g(P) + " D", g(nodiv) + " D", "+" + g(1 / P) + " D"], "+" + g(P) + " D",
        "25 cm = 0.25 m; P = 1/0.25 = **+4 D** (positive because the lens is convex). Writing 1/25 = 0.04 D without converting cm to m is the common slip.",
        "P = 100/f(cm) = 100/25 = 4 D.", 20)
    S.q("ga-li-p4", "medium", "The power of a **concave lens of focal length 50 cm** is —",
        ["−" + g(p2v) + " D", "+" + g(p2v) + " D", "−" + g(1 / p2v) + " D", "−" + g(P) + " D"], "−" + g(p2v) + " D",
        "50 cm = 0.5 m; P = 1/0.5 = 2 D, and a concave lens takes the **negative sign**: **−2 D**.",
        None, 20)
    S.q("ga-li-p4", "hard", "Sunlight takes about **8 minutes 20 seconds** to reach the Earth. The Earth–Sun distance is nearly —",
        ["1.5 × 10¹¹ m", "1.5 × 10⁸ m", "3 × 10¹¹ m", "5 × 10¹⁰ m"], "1.5 × 10¹¹ m",
        "d = c × t = (3 × 10⁸) × 500 = 1.5 × 10¹¹ m (500 s = 8 min 20 s). This distance is 1 astronomical unit.",
        "3 × 10⁸ × 500 = 1.5 × 10¹¹.", 30)
    S.q("ga-li-p5", "easy", "A pencil standing in a glass of water appears **bent** at the water surface because of —",
        ["Refraction of light", "Reflection of light", "Dispersion of light", "Diffraction of light"], "Refraction of light",
        "Light changes speed going from water to air, so the rays bend (**refraction**) and the underwater part looks raised and bent.",
        None, 15)
    S.q("ga-li-p5", "medium", "The **sparkle of a diamond** is mainly because of —",
        ["Total internal reflection", "High specific heat", "Dispersion only", "Refraction into the stone"], "Total internal reflection",
        "Diamond's very high refractive index (about 2.4) gives a small critical angle, so light entering the stone bounces inside it many times by **total internal reflection** before coming out.",
        None, 20)
    S.q("ga-li-p5", "medium", "The Sun appears about **2 minutes before actual sunrise** because of —",
        ["Atmospheric refraction", "Scattering of light", "Total internal reflection", "Dispersion in clouds"], "Atmospheric refraction",
        "Sunlight bends through the denser layers of the atmosphere, so we see the Sun's image while it is still below the horizon — about 2 minutes early (and 2 minutes late at sunset).",
        None, 20)
    S.q("ga-li-p5", "medium", "**Optical fibres** carry light signals over long distances using —",
        ["Total internal reflection", "Refraction", "Diffraction", "Polarisation"], "Total internal reflection",
        "Light entering the thin glass fibre hits its wall beyond the critical angle and is repeatedly totally internally reflected, staying inside the fibre. Endoscopes work the same way.",
        None, 20)
    S.q("ga-li-p6", "easy", "**Danger signal lights are red** because red light —",
        ["Is scattered the least and is visible from far away", "Has the highest frequency", "Travels fastest in air", "Is least absorbed by the atmosphere"], "Is scattered the least and is visible from far away",
        "Red has the **longest wavelength** in visible light, so air molecules scatter it least — it stays strong and visible over the greatest distance.",
        None, 15)
    S.q("ga-li-p6", "easy", "In the dispersion of white light by a prism, the colour **deviated (bent) the most** is —",
        ["Violet", "Red", "Green", "Yellow"], "Violet",
        "Violet has the shortest wavelength and slows the most in glass, so it bends most; red bends least. The order is VIBGYOR from the base of the spectrum upward.",
        None, 15)
    S.q("ga-li-p6", "medium", "A **rainbow** is formed by —",
        ["Dispersion and total internal reflection of sunlight in raindrops", "Reflection of sunlight by clouds", "Refraction of sunlight in dust particles", "Scattering of sunlight by air molecules"], "Dispersion and total internal reflection of sunlight in raindrops",
        "Sunlight entering a raindrop is dispersed, reflected inside (TIR), and leaves dispersed again — splitting into VIBGYOR. The bow is always seen with the **Sun behind** the observer.",
        None, 20)
    S.q("ga-li-p6", "medium", "The **sky appears blue** because —",
        ["Air molecules scatter blue light more than red", "The sea reflects blue light upward", "Blue light travels fastest in air", "The atmosphere absorbs red light completely"], "Air molecules scatter blue light more than red",
        "Scattering by tiny air molecules is strongest for short wavelengths, and blue/violet scatter the most — so scattered blue light reaches the eye from every direction.",
        None, 20)
    return S


def build_modern():
    S = Sub("ph-modern-scientists")
    S.notes = """### Inside the atom
An atom has a tiny dense **nucleus** (protons + neutrons) with **electrons** moving around it. The particles were found one by one:
- **Electron** — negative charge, found by **J.J. Thomson (1897)** in cathode-ray experiments.
- **Proton** — positive charge, seen in **canal rays** by **E. Goldstein**.
- **Neutron** — no charge, discovered by **James Chadwick (1932)**.
- **Nucleus** — shown by **Rutherford's gold-foil experiment (1911)**: most alpha particles passed straight through, a few bounced back, so nearly all mass and positive charge sit in a tiny centre. **Bohr (1913)** added fixed orbits for electrons.

### Radioactivity
**Henri Becquerel (1896)** discovered that uranium salts give out invisible penetrating rays — **radioactivity**, a property of heavy unstable nuclei. **Marie and Pierre Curie** discovered **polonium and radium**; Marie Curie won Nobel Prizes in **both Physics (1903) and Chemistry (1911)** — the only person with Nobels in two different sciences. The **alpha** ray is a helium nucleus (least penetrating, stopped by paper), **beta** is a fast electron (stopped by aluminium), and **gamma** is an electromagnetic wave (most penetrating, needs thick lead). A **Geiger–Müller counter** detects radiation. **Willard Libby's carbon-14 dating** finds the age of old organic remains from the C-14 left in them.

### Fission, fusion and reactors
- **Nuclear fission**: a heavy nucleus such as **U-235** splits into two smaller nuclei when hit by a neutron, releasing energy and more neutrons — a **chain reaction**. Uncontrolled → **atom bomb** (Hiroshima, 1945). Controlled in reactors → electricity.
- **Nuclear fusion**: two light nuclei (hydrogen isotopes) **join** into a heavier one — this powers the **Sun and stars**, and the **hydrogen bomb** (far more destructive than a fission bomb).
- Both follow Einstein's **E = mc²**: a little lost mass becomes a lot of energy.
- In a reactor: the **moderator** (heavy water, graphite) slows neutrons, **control rods** (cadmium, boron) absorb neutrons to control the chain reaction, and a coolant carries the heat away. Reactors use **fission**, not fusion.

### India's atomic and space programmes
**Homi J. Bhabha** is the father of India's nuclear programme; he set up the **Tata Institute of Fundamental Research (1945)** and **BARC** at Trombay. **Apsara (1956)** was India's (and Asia's) first research reactor; **Tarapur in Maharashtra (1969)** is India's first nuclear power station. India's first nuclear test was at **Pokhran in 1974** ("Smiling Buddha"); Pokhran-II followed in **May 1998**. In space, **Vikram Sarabhai** is the father of the Indian space programme and **ISRO was formed in 1969**. **Aryabhata (1975)** was the first Indian satellite. **Chandrayaan-1 (2008)** found water molecules on the Moon; **Mangalyaan (Mars Orbiter Mission, 2013)** made India the first country to reach Mars orbit in its first attempt; **Chandrayaan-3 (23 August 2023)** made India the first nation to soft-land near the Moon's south pole — the date is now **National Space Day**. **Aditya-L1 (2023)** is India's first solar mission. **Rakesh Sharma (1984)** was the first Indian in space; **Shubhanshu Shukla (2025, Axiom-4)** the first Indian to visit the International Space Station.

### Inventions — who did what
| Invention / discovery | Person |
|---|---|
| Laws of motion, gravitation | Newton |
| Astronomical telescope | Galileo |
| Barometer | Torricelli |
| Improved steam engine | James Watt |
| Electromagnetic induction, dynamo | Michael Faraday |
| Telephone | Alexander Graham Bell |
| Electric bulb, phonograph | Thomas Edison |
| Radio (wireless) | Guglielmo Marconi |
| Television | John Logie Baird |
| Telegraph | Samuel Morse |
| Aeroplane | Wright brothers (1903) |
| X-rays | Wilhelm Röntgen (first Physics Nobel, 1901) |
| Laser (first working, ruby) | Theodore Maiman (1960) |
A **laser** gives an intense beam of one wavelength, in step (coherent) — used in surgery, barcode scanners, CD/DVD players and optical-fibre communication. At CERN's **Large Hadron Collider (2012)** scientists found the **Higgs boson**, the "God particle" that explains why other particles have mass.

### Quick revision
- Electron–Thomson, proton–Goldstein (canal rays), neutron–Chadwick, nucleus–Rutherford, orbits–Bohr.
- Radioactivity–Becquerel; radium/polonium–Curies; C-14 dating–Libby; counter–Geiger.
- α = helium nucleus, β = electron, γ = EM wave (most penetrating).
- Fission = heavy splits (reactor, atom bomb); fusion = light join (Sun, H-bomb); E = mc².
- Bhabha (atomic), Sarabhai (space); Apsara 1956, Tarapur 1969, Pokhran 1974/1998.
- Aryabhata 1975, Chandrayaan-3 land 23-08-2023, Mars orbit first try 2014."""
    S.pattern("ga-ms-p1", "Particle or ray ↔ discoverer", "very common",
        "'Who discovered the neutron/electron/proton/X-rays/radioactivity/nucleus?' or a match-the-column of particles and scientists.",
        None,
        "1. Particles: electron–J.J. Thomson, proton–E. Goldstein (canal rays), neutron–James Chadwick, nucleus–Rutherford.\n2. Rays: X-rays–Röntgen, radioactivity–Becquerel, radium–Curies.\n3. Models: gold-foil experiment–Rutherford, orbits–Bohr.\nWhy: each name is fixed by history, so only recall plus elimination works.",
        "The **canal rays** that led to the discovery of the proton were observed by —",
        "**E. Goldstein.** J.J. Thomson found the electron in cathode rays; Chadwick found the neutron in 1932.")
    S.pattern("ga-ms-p2", "Device ↔ inventor", "very common",
        "'Who invented the telephone/television/radio/electric bulb/dynamo/steam engine/aeroplane?'",
        None,
        "1. Bell–telephone, Baird–television, Marconi–radio, Edison–bulb and phonograph, Morse–telegraph.\n2. Faraday–electromagnetic induction and dynamo, Watt–improved steam engine, Wright brothers–aeroplane (1903), Galileo–astronomical telescope, Torricelli–barometer.\n3. Eliminate near-names: J.C. Bose did pioneering radio/microwave work but wireless telegraphy's exam answer is Marconi.",
        "The **television** was invented by —",
        "**John Logie Baird** (first public demonstration, 1926). Telephone–Bell, radio–Marconi.")
    S.pattern("ga-ms-p3", "Radioactivity and alpha/beta/gamma", "common",
        "'Which radiation has the most penetrating power?', 'an alpha particle is …', who discovered radioactivity, which instrument detects radiation.",
        None,
        "1. Radioactivity–Becquerel (1896); radium and polonium–the Curies.\n2. α = helium nucleus (2 protons + 2 neutrons), stopped by paper; β = fast electron; γ = electromagnetic wave, most penetrating.\n3. Detection: Geiger–Müller counter. Dating of old remains: carbon-14 (Libby).",
        "An **alpha (α) particle** is identical to —",
        "A **helium nucleus** — 2 protons and 2 neutrons, no electrons.")
    S.pattern("ga-ms-p4", "Fission vs fusion; reactor parts", "very common",
        "'The Sun's energy comes from…', 'an atom bomb works on…', 'control rods are made of…', difference between the two bombs.",
        None,
        "1. Heavy nucleus splits → **fission** (reactors, atom bomb).\n2. Light nuclei join → **fusion** (Sun and stars, hydrogen bomb).\n3. Reactor parts: moderator slows neutrons (heavy water/graphite); control rods absorb them (cadmium/boron); coolant removes heat.\nWhy: both processes follow E = mc², but the size of the nucleus tells you which one it is.",
        "The energy of the **Sun and stars** is due to —",
        "**Nuclear fusion** — hydrogen nuclei join into helium at enormous temperature and pressure, releasing energy per E = mc².")
    S.pattern("ga-ms-p5", "India's atomic and space milestones", "common",
        "First reactor/power station/satellite/Mars or Moon mission, fathers of the two programmes, Pokhran tests, National Space Day.",
        None,
        "1. Atomic: Bhabha (father), Apsara 1956 (first research reactor), Tarapur 1969 (first power station), Pokhran 1974 and 1998.\n2. Space: Sarabhai (father), ISRO 1969, Aryabhata 1975 (first satellite), Chandrayaan-1 2008, Mangalyaan 2013 (Mars orbit, first attempt), Chandrayaan-3 south-pole landing on 23 Aug 2023 (National Space Day), Aditya-L1 solar mission.\n3. Persons: Rakesh Sharma first Indian in space (1984); Shubhanshu Shukla first Indian on the ISS (2025).",
        "India's **first nuclear power station** was set up at —",
        "**Tarapur, Maharashtra (1969).** Apsara (1956, Trombay) was the first research reactor.")
    S.pattern("ga-ms-p6", "Modern physics miscellany", "common",
        "E = mc², the 'God particle', laser properties, carbon dating, first Nobels — one-line fact questions from modern physics.",
        None,
        "1. E = mc² — Einstein: mass can convert into energy; the base of both fission and fusion.\n2. Higgs boson ('God particle') — found at CERN's LHC in 2012.\n3. Laser light: one wavelength (monochromatic), in step (coherent), highly directional.\n4. Carbon-14 dating — Willard Libby; ages of fossils and old organic objects.",
        "The **'God particle'** whose existence was confirmed at CERN in 2012 is the —",
        "**Higgs boson**, predicted by Peter Higgs; it explains how other particles get their mass.")

    S.q("ga-ms-p1", "easy", "Which subatomic particle carries a **negative** charge?",
        ["Electron", "Proton", "Neutron", "Photon"], "Electron",
        "The **electron** (found by J.J. Thomson) is negatively charged; the proton is positive; the neutron has no charge.",
        None, 15)
    S.q("ga-ms-p1", "medium", "**Canal rays**, whose study led to the discovery of the proton, were observed by —",
        ["E. Goldstein", "J.J. Thomson", "James Chadwick", "Ernest Rutherford"], "E. Goldstein",
        "Goldstein's **canal rays** (anode rays) are streams of positive particles — protons. Thomson found the electron, Chadwick the neutron, Rutherford the nucleus.",
        None, 20)
    S.q("ga-ms-p1", "easy", "**X-rays** were discovered by —",
        ["Wilhelm Röntgen", "Henri Becquerel", "Marie Curie", "J.J. Thomson"], "Wilhelm Röntgen",
        "**Röntgen** discovered X-rays in 1895 and received the first-ever Nobel Prize in Physics (1901). Becquerel found radioactivity; the Curies found radium.",
        None, 15)
    S.q("ga-ms-p1", "medium", "The existence of a small, dense, positively charged **nucleus** was established by —",
        ["Rutherford's gold-foil experiment", "Thomson's cathode-ray experiment", "Chadwick's beryllium experiment", "Bohr's orbit calculations"], "Rutherford's gold-foil experiment",
        "In Rutherford's gold-foil experiment (1911) most alpha particles passed through the foil but a few bounced back, showing that nearly all the positive charge and mass sit in a tiny nucleus.",
        None, 20)
    S.q("ga-ms-p2", "easy", "The **telephone** was invented by —",
        ["Alexander Graham Bell", "Thomas Edison", "Guglielmo Marconi", "Samuel Morse"], "Alexander Graham Bell",
        "**Bell** patented the telephone (1876). Edison — bulb and phonograph; Marconi — radio; Morse — telegraph.",
        None, 15)
    S.q("ga-ms-p2", "medium", "The **television** was invented by —",
        ["John Logie Baird", "C.V. Raman", "Guglielmo Marconi", "Michael Faraday"], "John Logie Baird",
        "The Scottish inventor **John Logie Baird** demonstrated television in 1926. Marconi is radio; Faraday worked on electromagnetic induction.",
        None, 15)
    S.q("ga-ms-p2", "easy", "The **dynamo (electric generator)** is based on electromagnetic induction, discovered by —",
        ["Michael Faraday", "James Watt", "Nikola Tesla", "Oersted"], "Michael Faraday",
        "**Faraday** discovered electromagnetic induction (1831) — a changing magnetic field induces current — the principle of the dynamo and transformer.",
        None, 15)
    S.q("ga-ms-p3", "medium", "Which radiation from a radioactive substance has the **greatest penetrating power**?",
        ["Gamma rays", "Alpha particles", "Beta particles", "Cathode rays"], "Gamma rays",
        "Order of penetration: **gamma (electromagnetic wave) > beta (electron) > alpha (helium nucleus)**. Alpha is stopped even by paper; gamma needs thick lead.",
        None, 20)
    S.q("ga-ms-p3", "medium", "**Radioactivity** was discovered by —",
        ["Henri Becquerel", "Pierre Curie", "Lord Kelvin", "Wilhelm Röntgen"], "Henri Becquerel",
        "**Becquerel** noticed uranium salts emitting penetrating rays in 1896. Marie and Pierre Curie then discovered polonium and radium.",
        None, 15)
    S.q("ga-ms-p3", "medium", "The age of ancient organic remains is estimated by —",
        ["Carbon-14 dating", "Uranium fission", "X-ray diffraction", "Spectroscopy of iron"], "Carbon-14 dating",
        "**Carbon-14 dating** (developed by Willard Libby) measures how much radioactive C-14 is left in dead organic matter.",
        None, 20)
    S.q("ga-ms-p4", "easy", "The energy of the **Sun** is produced by —",
        ["Nuclear fusion", "Nuclear fission", "Chemical combustion", "Gravitational contraction"], "Nuclear fusion",
        "In the Sun's core, hydrogen nuclei **fuse** into helium, converting a little mass into huge energy (E = mc²).",
        None, 15)
    S.q("ga-ms-p4", "medium", "The **atom bomb** dropped on Hiroshima worked on —",
        ["Uncontrolled nuclear fission of uranium", "Uncontrolled nuclear fusion of hydrogen", "Controlled fission in a reactor", "Chemical explosion of TNT"], "Uncontrolled nuclear fission of uranium",
        "The atom bomb is an uncontrolled **fission** chain reaction (U-235). The hydrogen bomb is the fusion (thermonuclear) one; a reactor is *controlled* fission.",
        None, 20)
    S.q("ga-ms-p4", "medium", "In a nuclear reactor, the chain reaction is controlled by inserting rods of —",
        ["Cadmium or boron", "Graphite or heavy water", "Uranium-235", "Lead or steel"], "Cadmium or boron",
        "**Control rods** of cadmium or boron absorb excess neutrons and keep the chain reaction steady. Graphite/heavy water are moderators (they slow neutrons, not absorb).",
        None, 20)
    S.q("ga-ms-p5", "easy", "Who is called the **father of India's nuclear programme**?",
        ["Homi J. Bhabha", "Vikram Sarabhai", "A.P.J. Abdul Kalam", "C.V. Raman"], "Homi J. Bhabha",
        "**Homi J. Bhabha** founded India's atomic energy effort (TIFR, BARC). Sarabhai is the father of the space programme; Kalam is the 'Missile Man'.",
        None, 15)
    S.q("ga-ms-p5", "medium", "India's first research reactor, **Apsara**, became critical in —",
        ["1956", "1969", "1974", "1948"], "1956",
        "**Apsara** (Trombay, 1956) was India's — and Asia's — first research reactor. Tarapur (1969) was the first nuclear *power* station; 1974 was Pokhran-I.",
        None, 20)
    S.q("ga-ms-p5", "medium", "The first Indian satellite, launched in **1975**, was named —",
        ["Aryabhata", "Rohini", "INSAT-1A", "Bhaskara"], "Aryabhata",
        "**Aryabhata** (1975) was India's first satellite, named after the ancient mathematician. Rohini was the first carried by India's own SLV-3 (1980).",
        None, 20)
    S.q("ga-ms-p5", "hard", "**National Space Day** (23 August) marks —",
        ["Chandrayaan-3's landing near the Moon's south pole", "The launch of Aryabhata", "Mangalyaan entering Mars orbit", "The founding of ISRO"], "Chandrayaan-3's landing near the Moon's south pole",
        "On **23 August 2023** Chandrayaan-3's Vikram lander touched down near the lunar south pole — India became the first country to do so; the date is now National Space Day.",
        None, 25)
    S.q("ga-ms-p5", "easy", "The **first Indian to travel into space** was —",
        ["Rakesh Sharma", "Kalpana Chawla", "Shubhanshu Shukla", "Vikram Sarabhai"], "Rakesh Sharma",
        "Sqn Ldr **Rakesh Sharma** flew to the Salyut-7 space station in 1984 on a Soviet spacecraft. Kalpana Chawla was the first woman of Indian origin in space; Shubhanshu Shukla (2025) was the first Indian on the ISS.",
        None, 15)
    S.q("ga-ms-p6", "easy", "The famous equation **E = mc²** was given by —",
        ["Albert Einstein", "Isaac Newton", "Max Planck", "Niels Bohr"], "Albert Einstein",
        "Einstein's mass–energy equivalence says a small mass m converts into energy E = mc², with c the speed of light — the basis of nuclear energy.",
        None, 15)
    S.q("ga-ms-p6", "medium", "The **'God particle'**, confirmed at CERN's Large Hadron Collider in 2012, is the —",
        ["Higgs boson", "Neutrino", "Positron", "Meson"], "Higgs boson",
        "The **Higgs boson**, predicted by Peter Higgs, explains how particles acquire mass. It was hunted down at the LHC in 2012.",
        None, 20)
    S.q("ga-ms-p6", "medium", "Laser light is used in surgery and fibre-optic communication because it is —",
        ["Highly monochromatic, coherent and directional", "Made of many random wavelengths", "Strongly radioactive", "Cooler than ordinary light"], "Highly monochromatic, coherent and directional",
        "LASER = Light Amplification by Stimulated Emission of Radiation: one wavelength, waves in step (coherent), and a tight beam — ideal for precision work and carrying signals along optical fibres.",
        None, 20)
    return S
