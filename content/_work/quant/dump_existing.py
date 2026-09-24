# -*- coding: utf-8 -*-
"""Print a compact list of existing quant question texts (topics + mock parts) for overlap review."""
import glob
import json
import os
import sys

sys.stdout.reconfigure(encoding="utf-8")
ROOT = r"C:\Users\Vinay Singirikonda\Desktop\examshortcut\content\ssc-cgl"

for p in sorted(glob.glob(os.path.join(ROOT, "topics", "quant", "*.json"))):
    d = json.load(open(p, encoding="utf-8"))
    print("==", d["id"])
    for x in d.get("solvedExamples", []) + d.get("practice", []):
        print("  -", x["q"].replace("\n", " ")[:110])
for p in sorted(glob.glob(os.path.join(ROOT, "mocks", "parts", "*--quant.json"))):
    d = json.load(open(p, encoding="utf-8"))
    print("== MOCK", d["mockId"])
    for x in d["questions"]:
        if x["subtopic"] == "data-interpretation":
            continue
        print("  -", x["subtopic"][:10], "|", x["q"].replace("\n", " ")[:100])
