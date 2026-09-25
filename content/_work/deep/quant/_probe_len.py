"""Probe: print notes lengths for a topic's subs without applying. Usage: py -3 _probe_len.py m2d"""
import sys
import m2d_part1
import m2d_part2
import m3d_part1
import m3d_part2

mods = {"m2d": [m2d_part1, m2d_part2],
        "m3d": [m3d_part1, m3d_part2]}

if __name__ == "__main__":
    key = sys.argv[1] if len(sys.argv) > 1 else "m2d"
    for mod in mods[key]:
        for name in dir(mod):
            if name.startswith("build_"):
                S = getattr(mod, name)()
                print(f"{S.id:24} {len(S.notes):6}")
