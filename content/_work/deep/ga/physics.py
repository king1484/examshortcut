"""Phase-2 deep content for ga/physics. Run: py -3 physics.py"""
import os
import sys

sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
from _lib import apply_topic
from phy_part1 import build_units, build_mech, build_hs
from phy_part2 import build_light, build_modern
from phy_part3 import build_elec


def P(pattern, frequency, howToSpot, approach, subtopic, q, sol):
    return {"pattern": pattern, "frequency": frequency, "howToSpot": howToSpot, "approach": approach,
            "subtopic": subtopic, "example": {"q": q, "solution": sol}}


PYQ = [
    P("SI unit of a quantity", "very common",
      "'The SI unit of magnetic flux / pressure / power of a lens is …', or a wrong-pair question mixing base and derived units.",
      "Learn the seven base units (m, kg, s, A, K, mol, cd) and the scientist-named derived units: newton, joule, watt, pascal, hertz, coulomb, volt, ohm, weber, tesla. Kill the traps: light year measures distance, kWh measures energy.",
      "ph-units",
      "The SI unit of magnetic flux is:",
      "Weber (Wb). Magnetic flux density (field) is measured in tesla — weber per square metre."),
    P("Instrument → what it measures", "very common",
      "An instrument name ending in -meter or -graph with its use asked: hygrometer, lactometer, anemometer, sphygmomanometer, seismograph.",
      "Read the Greek root: hygro (moisture), hydro (liquid), lacto (milk), anemo (wind), baro (air weight = pressure), seismo (quake), sphygmo (pulse). Then match the job to the root.",
      "ph-units",
      "Which instrument measures the relative humidity of air?",
      "Hygrometer — 'hygro' means moisture. The hydrometer (and lactometer for milk) measures liquid density instead."),
    P("Everyday phenomenon → principle", "very common",
      "A daily-life effect — rocket, gun recoil, hydraulic brakes, floating ship, aeroplane lift, pressure cooker, sea breeze — and options listing laws/principles.",
      "Sort by story: resistance to a change of state → inertia (first law); force spread over more time → second law/momentum; push one way, move the other → third law; enclosed liquid force → Pascal; floating/upthrust → Archimedes; fast air, low pressure → Bernoulli; boiling/steam/cooling → latent heat, specific heat, evaporation.",
      "ph-mechanics",
      "Hydraulic brakes work on the principle of:",
      "Pascal's law — pressure applied to an enclosed liquid is transmitted equally in all directions, so a small pedal force becomes a large braking force."),
    P("Inventor / discoverer", "very common",
      "'Who discovered the neutron?', 'who invented the television/telephone?', a match-the-column of scientists, devices and particles.",
      "Two tables to hold: particles (electron–Thomson, proton–Goldstein, neutron–Chadwick, nucleus–Rutherford, radioactivity–Becquerel, X-rays–Röntgen) and devices (Bell–telephone, Baird–TV, Marconi–radio, Edison–bulb, Faraday–dynamo, Watt–steam engine, Wright brothers–aeroplane).",
      "ph-modern-scientists",
      "Who discovered the neutron?",
      "James Chadwick (1932) — the neutral particle in the nucleus."),
    P("Eye defects and mirror/lens uses", "very common",
      "'Myopia is corrected by…', 'which mirror is used as a rear-view mirror / in a torch?', 'which lens always forms a virtual diminished image?'",
      "Fix the pairs: myopia–concave, hypermetropia–convex, presbyopia–bifocal, astigmatism–cylindrical; concave mirror = shaving/dentist/headlight, convex mirror = rear-view; convex lens = magnifier/camera, concave lens = diverging, always virtual-erect-diminished.",
      "ph-light",
      "Myopia (short-sightedness) is corrected by using a:",
      "Concave (diverging) lens — it pushes the image that forms in front of the retina back onto the retina."),
    P("Simple numericals (lens power, resistance, energy, temperature)", "very common",
      "A one-step calculation: power of a lens from focal length, two resistors in parallel, appliance watts into kWh, a temperature conversion, km/h to m/s.",
      "Memorise four one-liners: P = 1/f (f in metres, dioptre), 1/Rp = 1/R1 + 1/R2, units = W × h ÷ 1000, F = 9C/5 + 32 and km/h × 5/18 = m/s. Do the arithmetic in powers of ten to avoid slips.",
      "ph-electricity",
      "Two resistors of 6 Ω and 3 Ω are connected in parallel. What is their equivalent resistance?",
      "1/R = 1/6 + 1/3 = 1/2, so R = 2 Ω — for two resistors, product over sum: (6 × 3)/(6 + 3) = 2 Ω."),
    P("Sound properties and uses", "common",
      "'Sound cannot travel through…', 'bats navigate using…', audible range, which property gives pitch/loudness, echo and Doppler questions.",
      "Sound is longitudinal and needs a medium (fastest in solids, none in vacuum). Audible 20 Hz–20 kHz; below = infrasonic, above = ultrasonic (bats, SONAR, scans). Pitch ↔ frequency, loudness ↔ amplitude (dB).",
      "ph-heat-sound",
      "The pitch of a sound is determined by its:",
      "Frequency — higher frequency sounds shriller. Amplitude decides loudness."),
]

if __name__ == "__main__":
    subs = [build_units(), build_mech(), build_hs(), build_light(), build_elec(), build_modern()]
    apply_topic("physics", subs, PYQ)
