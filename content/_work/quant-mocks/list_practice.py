import json, glob, re

for f in sorted(glob.glob(r"C:\Users\Vinay Singirikonda\Desktop\examshortcut\content\ssc-cgl\topics\quant\*.json")):
    d = json.load(open(f, encoding="utf-8"))
    qs = d.get("practice", [])
    print("=" * 8, d.get("id"), len(qs))
    for q in qs:
        t = re.sub(r"\$[^$]*\$", "L", q.get("q", ""))
        print(" -", t[:100])
    se = d.get("solvedExamples", [])
    for q in se:
        t = re.sub(r"\$[^$]*\$", "L", q.get("q", ""))
        print(" S", t[:100])
