# One-off fixes to legacy (pre-deep) text in spelling.json flagged by the batch-2 agent.
# Idempotent: every replacement is skipped once applied.
import json, pathlib

P = pathlib.Path(__file__).resolve().parents[3] / 'core' / 'topics' / 'english' / 'spelling.json'
t = json.loads(P.read_text(encoding='utf-8'))
S = t['subtopics']

FIX = [
    (0, 'concept', "(n**ei**ghbour, w**ei**gh, h**ei**ght is the 'ay'-sound family too)",
                   "(n**ei**ghbour, w**ei**gh, **ei**ght). Height is different: its 'ei' sounds like 'eye', and it is simply an exception"),
    (0, 'concept', 'counterfeit, surplus-free words like protein**', 'counterfeit, protein**'),
    (0, 'concept', '~~percieva~~', '~~percieve~~'),
    (1, 'concept', 'parallel (r at middle… l at end)', 'parallel (one r, double l in the middle, single l at the end)'),
    (2, 'concept', '**-able vs -ible:** -ible after word-ends in **-cess** (accessible), **-sist** is mixed (resistible → irresist**ible**, but …). Practical set: access**ible**, irresist**ible**, feas**ible**, audit**ible**, vis**ible**, terr**ible**, horror+horr**ible**.',
                   '**-able vs -ible:** if the stem is a complete word, it is usually -able (comfort-able, accept-able); if the stem is not a word on its own, it is usually -ible (vis-ible, aud-ible, terr-ible). Learn the exceptions as a list: access**ible**, flex**ible**, irresist**ible**. Practical set: feas**ible**, aud**ible**, vis**ible**, terr**ible**, horr**ible**.'),
    (3, 'concept', '| **parallel** | ~~paralell~~ | double r in the middle, double l at the end |',
                   '| **parallel** | ~~paralell~~ | one r, then double l in the middle: p-a-r-a-l-l-e-l |'),
    (3, 'concept', '| **skiing** | ~~skiing~~ | i-i collision is correct here |', '| **skiing** | ~~sking~~ | ski + ing: the i-i collision is correct |'),
    (3, 'concept', 'nine → ninth: the e drops (unlike nine + th = ninety is different)', 'nine → ninth: the e drops (but ninety and nineteen keep it)'),
    (3, 'concept', "\n| **collectible** | ~~collectable~~ | -IBLE (both exist, but 'collectible' is the standard noun) |", ''),
    (2, 'notes', '### Two corrections to the lists above\n', '### Two words people get wrong\n'),
    (3, 'notes', '### Corrections to the trap list above\nThree entries in the trap list above need a closer look:\n',
                 '### Three words to look at closely\n'),
]
n = 0
for i, field, old, new in FIX:
    s = S[i][field]
    if old in s:
        S[i][field] = s.replace(old, new, 1); n += 1
    else:
        assert new in s or new == '', f'neither old nor new text found: subtopic {i} {field}: {old[:50]}'

blob = json.dumps([s['concept'] for s in S], ensure_ascii=False)  # notes legitimately name the wrong forms
for bad in ['auditible', 'percieva', 'surplus-free', 'double r in the middle', '~~collectable~~']:
    assert bad not in blob, bad
P.write_text(json.dumps(t, ensure_ascii=False, indent=1) + '\n', encoding='utf-8', newline='\n')
print(f'applied {n} fixes')
