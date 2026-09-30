"""Physics part B: heat and sound, light."""
from fractions import Fraction as Fr
from _ph_common import pat, mis, trick

S = {}
FNOTES = {}

# numeric checks
assert Fr(9, 5) * 25 + 32 == 77
assert Fr(9, 5) * 37 + 32 == Fr(986, 10)          # 98.6 F
assert 37 + 273 == 310
assert Fr(9, 5) * -40 + 32 == -40
assert 330 * 3 // 2 == 495 and (330 * 3) % 2 == 0
assert 1 / Fr(1, 4) == 4                            # f = 0.25 m -> 4 D
assert Fr(2) + Fr(-1, 2) == Fr(3, 2)
assert Fr(3 * 10**8) / Fr(3, 2) == 2 * 10**8      # speed in glass n = 1.5
assert Fr(15 * 10**10, 3 * 10**8) == 500           # 500 s = 8 min 20 s
assert divmod(500, 60) == (8, 20)
assert 100 / Fr(50) == 2                            # 50 cm lens -> 2 D
# F = 2C: C/5 = (2C-32)/9 -> 9C = 10C - 160 -> C = 160
assert Fr(160, 5) == Fr(2 * 160 - 32, 9)

# =====================================================================
S["ph-heat-sound"] = dict(
    concept=(
        "Heat is energy that flows from a hot body to a cold one. Temperature tells how hot a body is. "
        "Sound is a wave that needs a medium, and it travels fastest in solids. "
        "Exams ask temperature conversions, everyday heat effects and sound facts."
    ),
    notes=r"""### Heat and temperature are different
**Heat** is energy that flows from a hotter body to a colder one. Its unit is the joule. The older unit is the calorie.

**Temperature** tells how hot a body is. It is the average energy of its particles. Its unit is the kelvin.

A bucket of warm water holds more heat than a cup of boiling water. The cup has the higher temperature.

### Temperature scales
| Scale | Ice melts | Water boils |
|---|---|---|
| Celsius | 0 °C | 100 °C |
| Fahrenheit | 32 °F | 212 °F |
| Kelvin | 273 K (273.15) | 373 K |

The conversions are $F = \dfrac{9}{5}C + 32$ and $K = C + 273$.

- Celsius and Fahrenheit read the same at −40°.
- Normal body temperature is 37 °C = 98.6 °F = 310 K.
- The lowest possible temperature is 0 K, called absolute zero. It is −273.15 °C.
- A clinical thermometer reads about 35 to 42 °C. A pyrometer measures very high temperatures.

> **Example:** Convert 25 °C to °F. $\dfrac{9}{5} \times 25 + 32 = 45 + 32 = 77$ °F.

### Specific heat and latent heat
- **Specific heat** is the heat needed to raise 1 kg of a substance by 1 °C. Water has a very high specific heat. It heats and cools slowly. So coastal places have mild climates, and water is used as a coolant.
- **Latent heat** is heat taken or given during a change of state, with no change in temperature. Steam at 100 °C burns more than water at 100 °C. Steam also gives out its latent heat of vaporisation when it condenses on skin.
- **Evaporation causes cooling.** A matka (earthen pot) keeps water cool. Sweat cools the body.

> **Tip:** Evaporation is faster with more surface area, more heat, wind and dry air.

### Boiling, melting and pressure
Higher pressure raises the boiling point. A pressure cooker cooks faster because water inside boils above 100 °C.

On mountains the air pressure is low. Water boils below 100 °C and food cooks slowly.

Pressure lowers the melting point of ice. This is called regelation. Two ice blocks pressed together join.

### Water expands the wrong way
Most things expand when heated. Water shrinks from 0 °C to 4 °C and then expands. So water is **densest at 4 °C**.

In winter the top of a lake freezes first. The floating ice insulates the water below, which stays near 4 °C. Fish survive.

Pipes burst in frost because water expands when it freezes. Gaps in railway tracks and sagging wires in summer show ordinary thermal expansion.

### Three ways heat travels
- **Conduction** moves heat through solids, particle to particle. A spoon handle gets hot this way. Metals conduct well. Wood, plastic and air are insulators.
- **Convection** moves heat when the liquid or gas itself moves. Examples are the sea breeze (day), the land breeze (night), boiling water and room heaters.
- **Radiation** needs no medium. The Sun's heat reaches us this way.

Dark, rough surfaces absorb and emit heat well. Light, shiny surfaces reflect it. So white clothes keep us cool in summer.

> **Note:** A thermos flask blocks all three. The vacuum stops conduction and convection. The silvered walls stop radiation.

### Sound is a mechanical wave
Sound comes from vibration. It is a **longitudinal wave** and it needs a medium. It cannot travel in a vacuum. Astronauts use radio.

| Medium | Speed of sound |
|---|---|
| Air at 0 °C | about 332 m/s |
| Air at 20 °C | about 343 m/s |
| Water | about 1500 m/s |
| Steel | about 5000 m/s or more |

The order is solids > liquids > gases. Speed rises with temperature and humidity. Pressure alone does not change it.

### Frequency, pitch and loudness
- Humans hear 20 Hz to 20,000 Hz.
- Below 20 Hz is **infrasonic**: earthquakes, elephants, whales.
- Above 20 kHz is **ultrasonic**: bats, dolphins, SONAR, scans, cleaning.
- **Pitch** depends on frequency. Women and children have higher-pitched voices.
- **Loudness** depends on amplitude. It is measured in decibels (dB).
- **Quality (timbre)** depends on the wave shape. It lets us tell a sitar from a flute on the same note.

### Echo, Doppler effect and resonance
- **Echo:** a reflected sound is heard separately if it returns after at least 0.1 s. The reflector must be about 17 m away. Distance = speed × time ÷ 2.
- **Doppler effect:** an approaching horn sounds higher. A receding one sounds lower.
- **Resonance:** a body vibrates strongly when pushed at its natural frequency. Soldiers break step on a bridge.
- **Sonic boom:** made by objects that move faster than sound. Mach number is object speed ÷ speed of sound. Above 1 is supersonic.
""",
    tricks=[
        trick("Sound speed order",
              "Solids are fastest, then liquids, then gases. A vacuum has no sound at all.",
              "Why is an approaching train heard earlier through the rail?",
              ["The rail is a solid.", "Sound is faster in solids than in air."],
              "Sound travels much faster in steel than in air"),
        trick("Pitch and loudness",
              "**P**itch goes with **F**requency. **L**oudness goes with **A**mplitude.",
              "The pitch of a sound depends on its:",
              ["Pitch is how high or low a note is.", "It follows the frequency."],
              "Frequency"),
    ],
    mistakes=[
        mis("Thinking sound speed rises with pressure.", "It rises with temperature and humidity, not pressure alone."),
        mis("Calling the sound of bats infrasonic.", "Bats use ultrasonic sound, above 20 kHz."),
        mis("Saying the boiling point rises at hill stations.", "It falls, because the air pressure is lower."),
        mis("Using 'degree kelvin' or forgetting to add 273 for kelvin.", "K = C + 273."),
        mis("Thinking water is densest at 0 °C.", "Water is densest at 4 °C."),
    ],
    revision=[
        "F = 9C/5 + 32 and K = C + 273. −40 °C = −40 °F. Body temperature 37 °C = 98.6 °F.",
        "Water has the highest specific heat and is densest at 4 °C.",
        "Steam burns worse because of latent heat. A pressure cooker raises the boiling point.",
        "Conduction: solids. Convection: fluids and breezes. Radiation: Sun, no medium needed.",
        "Sound: solids fastest, no sound in vacuum, audible range 20 Hz to 20 kHz.",
        "Pitch goes with frequency. Loudness goes with amplitude. Echo distance = vt/2.",
    ],
    patterns=[
        pat("ga-hs-p1", "Temperature scale conversion", "very common",
            "A temperature must be converted, or the question asks when two scales read the same or one is double the other.",
            [r"Write $\dfrac{C}{5}=\dfrac{F-32}{9}$.",
             "Put in the given value or the condition, such as F = C or F = 2C.",
             "Solve for the unknown. For kelvin, just add 273."],
            "100 Celsius steps cover the same range as 180 Fahrenheit steps, so the ratio is 5 to 9 with a 32° shift.",
            "Convert 25 °C to Fahrenheit.",
            [r"$F = \dfrac{9}{5}\times 25 + 32$.", "That is 45 + 32."],
            "77 °F",
            formula=r"\frac{C}{5}=\frac{F-32}{9}=\frac{K-273}{5}"),
        pat("ga-hs-p2", "Everyday heat effect and its reason", "very common",
            "The question says 'Why does steam burn more / pressure cooker cook faster / earthen pot cool water / fish survive frozen lakes / coast have mild climate?'",
            ["A state change with no temperature change points to latent heat.",
             "Slow heating or cooling of water points to high specific heat.",
             "Boiling point rises with pressure and falls with height.",
             "Cooling without a fridge points to evaporation. Lakes freezing from the top point to 4 °C density."],
            "Each everyday effect has one standard reason.",
            "Why does food take longer to cook on high mountains?",
            ["Air pressure is low there.", "Water boils below 100 °C.", "The food gets less heat."],
            "Water boils at a lower temperature, so food cooks slowly"),
        pat("ga-hs-p3", "Mode of heat transfer", "common",
            "A situation (sea breeze, Sun's heat, hot spoon handle, thermos flask, white clothes) with conduction, convection and radiation as options.",
            ["If heat moves through a solid and the solid stays still, choose conduction.",
             "If the warm fluid itself moves (breezes, boiling), choose convection.",
             "If no medium is needed, or colour matters, choose radiation."],
            "The three modes differ in how the particles take part.",
            "A land breeze at night is an example of:",
            ["At night the sea is warmer.", "Air over the sea rises.", "Cooler air from the land moves in."],
            "Convection"),
        pat("ga-hs-p4", "Speed of sound and the medium", "common",
            "The question says 'Sound travels fastest in ...', 'cannot travel through ...' or 'speed of sound increases with ...'.",
            ["Recall the order: solids > liquids > gases. A vacuum has no sound.",
             "Temperature and humidity raise the speed in air. Pressure alone does not.",
             "Recall the values: air 343 m/s, water 1500 m/s, steel 5000 m/s."],
            "Particles in a solid are closer, so the vibration passes faster.",
            "In which medium is sound fastest: air, water, steel or vacuum?",
            ["A vacuum has no sound.", "Solids carry sound fastest.", "Steel is a solid."],
            "Steel"),
        pat("ga-hs-p5", "Frequency ranges, pitch, loudness and quality", "very common",
            "The question gives the audible range, users of infrasonic or ultrasonic sound (bats, dolphins, elephants), or asks which property decides pitch, loudness or timbre.",
            ["Audible range is 20 Hz to 20 kHz. Below it is infrasonic. Above it is ultrasonic.",
             "Pitch goes with frequency. Loudness goes with amplitude (dB). Quality goes with the wave shape.",
             "Ultrasound is used in SONAR, medical scans and bat echolocation."],
            "Each property of the note is set by a different property of the wave.",
            "Sound waves of frequency 10 Hz are called:",
            ["The lower limit of hearing is 20 Hz.", "10 Hz is below it."],
            "Infrasonic"),
        pat("ga-hs-p6", "Echo, Doppler effect and resonance", "occasional",
            "An echo-distance sum, a horn whose pitch rises as it approaches, or soldiers breaking step on a bridge.",
            ["For echo, sound goes to the reflector and back. So distance = v × t ÷ 2.",
             "If the heard pitch changes because source or listener moves, it is the Doppler effect.",
             "If a body vibrates strongly at its natural frequency, it is resonance."],
            "Echo time covers a round trip, so you halve it.",
            "An echo returns in 3 s. The speed of sound is 330 m/s. How far is the wall?",
            [r"Round trip $= 330 \times 3 = 990$ m.", "One way is 990 ÷ 2."],
            "495 m",
            formula=r"d=\frac{v\times t}{2}"),
    ],
)
FNOTES["ph-heat-sound"] = {"Temperature scales": "−40 °C = −40 °F",
                           "Heat absorbed": "m is mass, c is specific heat, ΔT is the rise in temperature",
                           "Latent heat": "m is mass, L is latent heat; no temperature change during a change of state",
                           "Wave speed": "speed = frequency × wavelength",
                           "Echo distance": "sound goes to the wall and back, so halve the total"}

# =====================================================================
S["ph-light"] = dict(
    concept=(
        "Light travels in straight lines at about 3 × 10⁸ m/s in vacuum. "
        "Mirrors reflect it, lenses and glass bend it, and a prism splits it into colours. "
        "Exams ask which mirror or lens to use, eye defects, and why the sky is blue."
    ),
    notes=r"""### Light, the basics
Light is a form of energy that makes things visible. In one medium it moves in straight lines. That is why shadows form.

- The speed of light in vacuum is $c \approx 3 \times 10^8$ m/s. It is the highest speed in the universe.
- Light slows down in water and glass.
- **Refractive index** is $n = \dfrac{c}{v}$. In glass, $n \approx 1.5$, so light moves at about $2 \times 10^8$ m/s.
- Sunlight takes about 8 minutes 20 seconds to reach the Earth.
- Diamond has a very high refractive index, about 2.42. It has a small critical angle, so it sparkles.

### Mirrors and their jobs
| Mirror | Image | Standard uses |
|---|---|---|
| Plane | Virtual, erect, same size, laterally inverted | Looking glass, periscope |
| Concave (converging) | Real and inverted if the object is far. Magnified virtual image if close. | Shaving and make-up mirror, dentist's mirror, headlight and torch reflectors, solar furnace |
| Convex (diverging) | Always virtual, erect, diminished. Wide field of view. | Rear-view mirror, mirrors at road bends |

A concave mirror brings parallel rays to a focus. So it collects the Sun's heat, or sends lamp light out as a beam.

> **Tip:** Need a wide view? Choose convex. Need an enlarged image or a beam? Choose concave.

### Lenses
A **convex lens** is thicker in the middle. It converges rays. It is used in a magnifier, camera, projector, microscope, telescope objective and the eye.

- Object inside F: image is magnified, erect and virtual (a magnifier).
- Object beyond 2F: image is real, inverted and diminished (a camera).

A **concave lens** always forms a virtual, erect, diminished image of a real object. It corrects short sight.

**Power** is $P = \dfrac{1}{f}$, with f in metres. The unit is the dioptre (D). Convex power is positive. Concave power is negative. For thin lenses in contact, powers simply add.

> **Example:** A lens of focal length 25 cm has $f = 0.25$ m. Its power is $\dfrac{1}{0.25} = +4$ D.

### The eye and its defects
The eye lens forms a real, inverted image on the retina. The brain reads it upright.

- Nearest clear vision is about 25 cm. The far point is at infinity.
- Rods work in dim light. Cones sense colour.
- Persistence of vision is about 1/16 s. It makes cinema possible.

| Defect | What goes wrong | Correction |
|---|---|---|
| Myopia (short sight) | Image forms in front of the retina | Concave lens |
| Hypermetropia (long sight) | Image forms behind the retina | Convex lens |
| Presbyopia | Old age, lens loses flexibility | Bifocal lens |
| Astigmatism | Uneven curve of the cornea | Cylindrical lens |
| Cataract | Lens turns opaque | Surgery |

Colour blindness is not a lens problem. The cones lack some colour sensors. No lens can correct it.

### Refraction and total internal reflection
Light bends when it passes at a slant between clear media. This is **refraction**. The speed changes. Light bends towards the normal in a denser medium.

- A pencil in water looks bent. A pool looks shallower.
- Stars twinkle because of shifting layers of air. Planets hardly twinkle.
- The Sun is seen about 2 minutes before actual sunrise and after actual sunset.

**Total internal reflection (TIR)** happens when light goes from a denser to a rarer medium beyond the critical angle. All the light reflects back. It gives the sparkle of a diamond, optical fibres, the endoscope and the mirage.

### Dispersion and scattering
White light is a mixture of seven colours, VIBGYOR. A prism splits it. This is **dispersion**. Violet bends most and red bends least. Newton recombined the colours with a second prism.

A **rainbow** forms by refraction, dispersion and internal reflection in raindrops. It is seen with the Sun behind you. In the primary rainbow, red is on the outside.

**Scattering** by air molecules is stronger for short wavelengths. So:
- The sky looks blue.
- The Sun looks red at sunrise and sunset.
- Danger signals are red, because red scatters least and is seen from far.
- The sky looks black to astronauts, because space has no air to scatter light.

> **Note:** The Raman effect was found by C.V. Raman on 28 February 1928. That day is National Science Day. He won the Nobel Prize in 1930.

Light primaries are red, green and blue. Red + green is yellow, green + blue is cyan, red + blue is magenta. All three make white. A red rose in green light looks almost black, because it reflects only red.
""",
    tricks=[
        trick("Eye defect and its lens",
              "**My**opia goes with **con**cave. **Hyper**metropia goes with con**vex**. A short-sighted eye needs a diverging lens to push the image back onto the retina.",
              "A person who cannot see distant objects clearly needs which lens?",
              ["Cannot see far means short sight, or myopia.", "Myopia goes with a concave lens."],
              "A concave (diverging) lens"),
        trick("Mirror by job",
              "Need a wide view? Use convex (rear-view). Need an enlarged image or a focused beam? Use concave (shaving, dentist, headlight)."),
    ],
    mistakes=[
        mis("Explaining the blue sky by reflection or refraction.", "The cause is scattering of short wavelengths."),
        mis("Saying red bends most in a prism.", "Violet bends most and red bends least."),
        mis("Choosing a concave mirror for a vehicle rear-view.", "Vehicles use convex mirrors for a wide view."),
        mis("Leaving the focal length in centimetres in P = 1/f.", "Convert to metres first: 25 cm = 0.25 m."),
        mis("Offering a lens as the cure for colour blindness.", "No lens can correct it."),
    ],
    revision=[
        "c = 3 × 10⁸ m/s. n = c/v. Sunlight takes about 8 min 20 s to reach Earth.",
        "Plane mirror: lateral inversion. Concave: shaving, dentist, headlight. Convex: rear-view.",
        "P = 1/f (metres) in dioptre. Powers add for lenses in contact.",
        "Myopia: concave. Hypermetropia: convex. Presbyopia: bifocal. Astigmatism: cylindrical. Cataract: surgery.",
        "TIR: diamond sparkle, optical fibre, mirage. Refraction: bent pencil, twinkling, early sunrise.",
        "Violet bends most in a prism. Blue sky, red sunset and red danger signals come from scattering.",
    ],
    patterns=[
        pat("ga-li-p1", "Mirror, image and use", "very common",
            "The question asks which mirror is a rear-view, shaving or dentist's mirror, or which image a convex mirror forms, or plane mirror properties.",
            ["Let the job decide. A wide upright view needs convex. An enlarged close view or a beam needs concave.",
             "A convex mirror always gives a virtual, erect, diminished image.",
             "A plane mirror image is virtual, erect, same size and laterally inverted."],
            "Each mirror bends rays in a fixed way, so each has fixed jobs.",
            "A dentist's mirror is a:",
            ["The mirror is held close to the tooth.", "The image must be erect and magnified.", "Only a concave mirror does that."],
            "Concave mirror"),
        pat("ga-li-p2", "Lens, image and use", "very common",
            "The question says 'Which lens is used in a magnifier / camera / projector?', 'a concave lens always forms ...' or 'which lens converges light'.",
            ["A converging lens is a convex lens: magnifier, camera, projector, eye lens.",
             "A diverging lens is a concave lens. For real objects the image is virtual, erect and diminished.",
             "For a magnifier, keep the object inside the focal length."],
            "Convex lenses converge light. Concave lenses spread it out.",
            "A camera lens produces an image that is:",
            ["The object is far beyond 2F.", "The image lands between F and 2F.", "It is real, inverted and diminished."],
            "Real, inverted and diminished"),
        pat("ga-li-p3", "Eye defects and correction", "very common",
            "A defect (myopia, hypermetropia, presbyopia, astigmatism, cataract, colour blindness) is given with its cause or lens.",
            ["Short-sighted is myopia, so choose a concave lens. Long-sighted is hypermetropia, so choose a convex lens.",
             "Old-age trouble with near and far points to a bifocal lens. Uneven cornea points to a cylindrical lens. A cloudy lens is cataract, treated by surgery.",
             "Colour blindness has no lens correction, so reject any lens option."],
            "Each defect has one fixed cause and one fixed cure.",
            "Presbyopia of old age is corrected by:",
            ["Both near and far vision are weak.", "One lens needs two parts.", "Bifocal lenses have a convex lower part and a concave upper part."],
            "Bifocal lenses"),
        pat("ga-li-p4", "Lens power and light-speed numericals", "common",
            "A focal length is given and power is asked (or the reverse), lenses are in contact, or a distance is divided by the speed of light.",
            ["Convert the focal length to metres first.",
             "Use P = 1/f. Convex is positive and concave is negative.",
             "For lenses in contact, add the powers.",
             "For light travel time, use t = d ÷ (3 × 10⁸ m/s)."],
            "The dioptre means 1 per metre, so the metre conversion is the only trap.",
            "Two thin lenses of powers +2 D and −0.5 D are placed in contact. Find the power and nature of the combination.",
            ["Add the powers: 2 + (−0.5) = 1.5.", "The net power is positive."],
            "+1.5 D, a converging combination",
            formula=r"P=\frac{1}{f(\text{m})}\ (\text{dioptre}),\quad P=P_1+P_2,\quad t=\frac{d}{c}"),
        pat("ga-li-p5", "Refraction and total internal reflection effects", "very common",
            "A phenomenon (bent pencil, shallow pool, twinkling star, early sunrise, mirage, optical fibre, diamond sparkle) with its cause asked.",
            ["If an object looks bent, shifted or shallow, or stars twinkle, or the Sun rises early, the cause is refraction.",
             "If light stays inside (diamond, optical fibre, endoscope) or a mirage forms, the cause is total internal reflection.",
             "TIR needs light going from a denser to a rarer medium beyond the critical angle."],
            "Refraction comes from a change of speed between media.",
            "Why do stars twinkle but planets hardly do?",
            ["Starlight refracts through shifting layers of air.", "So its brightness flickers.", "Planets are closer and act as extended sources, so the changes average out."],
            "Atmospheric refraction"),
        pat("ga-li-p6", "Dispersion, scattering and colour facts", "very common",
            "The question asks why the sky is blue, why danger signals are red, the VIBGYOR order, which colour bends most, rainbow facts, or an object's colour in coloured light.",
            ["Blue sky, red sunset and red danger signals all come from scattering.",
             "In a prism violet bends most and red bends least.",
             "For a rainbow, remember dispersion plus internal reflection in raindrops, the Sun behind you, and red on the outer edge of the primary bow.",
             "A body shows the colour it reflects. It looks black in light it fully absorbs."],
            "Short wavelengths scatter most, and different colours bend by different amounts.",
            "A red rose is seen in green light. What colour does it appear?",
            ["The rose reflects only red light.", "Green light has no red in it.", "So the rose absorbs the green light."],
            "Almost black"),
    ],
)
FNOTES["ph-light"] = {"Power of a lens": "f in metres gives the power in dioptre",
                      "Lens formula": "u is object distance, v is image distance",
                      "Mirror formula": "f = R/2, R is the radius of curvature",
                      "Refractive index": "c = 3 × 10⁸ m/s, v is speed in the medium"}
