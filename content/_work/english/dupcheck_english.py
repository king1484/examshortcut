"""English duplicate check (mirrors ../ga/dupcheck_ga.py). Run from this directory.

Compares every *--english.json mock part against the English topic bank
(solvedExamples + practice) and against every other English mock part.
Key = normalised (q, figure, passage): strip * _ `, collapse whitespace, lowercase.
Passage is included so that generic cloze/RC stems ('fill in blank number (1)')
are only flagged when the passage is also the same, and the sorted option set is
included because spelling stems ('Select the correctly spelt word.') are generic.
A second, stricter pass flags any repeated *answer word* for vocab-type subtopics
(spelling / synonyms-antonyms / one-word-substitution / idioms-phrases).
"""
import json, glob, re, os


def norm(s):
    return re.sub(r'\s+', ' ', re.sub(r'[*_`]', '', s or '')).strip().lower()


def keyed(qs):
    out, passage = [], ''
    for q in qs:
        if q.get('passage'):
            passage = q['passage']
        elif not q.get('group'):
            passage = ''
        opts = tuple(sorted(norm(o) for o in q.get('options', [])))
        out.append((norm(q.get('q', '')), norm(q.get('figure') or ''), norm(passage), opts))
    return out


topic = set()
for f in glob.glob('../../ssc-cgl/topics/english/*.json'):
    d = json.load(open(f, encoding='utf-8'))
    for src in (d.get('solvedExamples', []), d.get('practice', [])):
        topic.update(keyed(src))
print('english topic bank:', len(topic), 'unique qs')

parts = {}
for f in glob.glob('../../ssc-cgl/mocks/parts/*--english.json'):
    d = json.load(open(f, encoding='utf-8'))
    parts[os.path.basename(f)] = keyed(d['questions'])

total = 0
for name, qs in sorted(parts.items()):
    dups = [q for q in qs if q in topic]
    inner = len(qs) - len(set(qs))
    total += len(dups) + inner
    print(name, 'dups vs topic bank:', len(dups), '| within file:', inner)
    for q in dups[:4]:
        print('     ', q[0][:90])

names = sorted(parts)
for i in range(len(names)):
    for j in range(i + 1, len(names)):
        both = set(parts[names[i]]) & set(parts[names[j]])
        total += len(both)
        print(f'cross {names[i][:12]} vs {names[j][:12]}:', len(both))
        for q in list(both)[:3]:
            print('     ', q[0][:90])

# stricter pass: the same tested word/idiom must not recur between the new mocks and anything else
VOCAB = {'spelling', 'synonyms-antonyms', 'one-word-substitution', 'idioms-phrases'}


def tested(q):
    lines = [l for l in q['q'].split('\n') if l.strip()]
    head = norm(lines[-1]) if len(lines) > 1 else ''
    return head or norm(q['options'][q['answer']])


seen = {}
for f in glob.glob('../../ssc-cgl/topics/english/*.json'):
    d = json.load(open(f, encoding='utf-8'))
    for q in d.get('solvedExamples', []) + d.get('practice', []):
        if q.get('subtopic', d.get('id')) in VOCAB or d.get('id') in VOCAB:
            seen.setdefault(tested(q), []).append('topic:' + d.get('id', ''))
for f in glob.glob('../../ssc-cgl/mocks/parts/*--english.json'):
    d = json.load(open(f, encoding='utf-8'))
    for q in d['questions']:
        if q['subtopic'] in VOCAB:
            seen.setdefault(tested(q), []).append(os.path.basename(f).split('--')[0])
vocab_rep = {k: v for k, v in seen.items() if len(v) > 1 and any(s in ('t1-mock-2', 't1-mock-3') for s in v)}
print('vocab repeats involving t1-mock-2/3:', len(vocab_rep))
for k, v in vocab_rep.items():
    print('     ', k[:60], v)
print('TOTAL DUPS:', total)
