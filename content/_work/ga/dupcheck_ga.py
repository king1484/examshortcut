import json, glob, re, os

def norm(s):
    return re.sub(r'\s+', ' ', re.sub(r'[*_`]', '', s or '')).strip().lower()

topic = set()
for f in glob.glob('../../ssc-cgl/topics/ga/*.json'):
    d = json.load(open(f, encoding='utf-8'))
    for src in (d.get('solvedExamples', []), d.get('practice', [])):
        for p in src:
            topic.add((norm(p.get('q', '')), norm(p.get('figure') or '')))
print('ga topic bank:', len(topic), 'unique qs')

parts = {}
for f in glob.glob('../../ssc-cgl/mocks/parts/*--ga.json'):
    d = json.load(open(f, encoding='utf-8'))
    parts[os.path.basename(f)] = [(norm(q.get('q', '')), norm(q.get('figure') or '')) for q in d['questions']]

for name, qs in parts.items():
    dups = [q for q in qs if q in topic]
    print(name, 'dups vs topic bank:', len(dups))
    for q in dups[:4]:
        print('     ', q[0][:90])

names = sorted(parts)
for i in range(len(names)):
    for j in range(i + 1, len(names)):
        both = set(parts[names[i]]) & set(parts[names[j]])
        print(f'cross {names[i][:12]} vs {names[j][:12]}:', len(both))
        for q in list(both)[:3]:
            print('     ', q[0][:90])
