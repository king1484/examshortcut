import json, glob, re, os

def norm(s):
    s = re.sub(r'[*_`]', '', s or '')
    return re.sub(r'\s+', ' ', s).strip().lower()

topic = set()
for f in glob.glob('content/ssc-cgl/topics/reasoning/*.json'):
    d = json.load(open(f, encoding='utf-8'))
    for src in (d.get('solvedExamples', []), d.get('practice', [])):
        for p in src:
            topic.add((norm(p.get('q', '')), norm(p.get('figure') or '')))
print('topic bank:', len(topic), 'unique qs')

parts = {}
for f in glob.glob('content/ssc-cgl/mocks/parts/*--reasoning.json'):
    d = json.load(open(f, encoding='utf-8'))
    parts[os.path.basename(f)] = [(norm(q.get('q', '')), norm(q.get('figure') or '')) for q in d['questions']]

for name, qs in parts.items():
    dups = [q for q in qs if q in topic]
    print(name, 'dups vs topic bank:', len(dups))
    for q in dups[:4]:
        print('    ', q[0][:90])

names = sorted(parts)
if len(names) == 2:
    both = set(parts[names[0]]) & set(parts[names[1]])
    print('cross-part dups:', len(both))
    for q in list(both)[:4]:
        print('    ', q[0][:90])
