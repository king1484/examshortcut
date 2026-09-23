import json

base = r"C:\Users\Vinay Singirikonda\Desktop\examshortcut\content\ssc-cgl\topics\quant"
for t in ["geometry", "data-interpretation", "statistics", "average", "profit-loss-discount", "mixture-alligation", "time-work", "time-speed-distance", "ratio-proportion", "percentage", "mensuration-2d", "mensuration-3d"]:
    d = json.load(open(base + "\\" + t + ".json", encoding="utf-8"))
    for q in d.get("solvedExamples", []):
        print(t, "| S:", q["q"][:130], "=>", q["options"][q["answer"]][:40])
