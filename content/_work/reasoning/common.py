"""Shared helpers for building + verifying SSC CGL reasoning content.

Every topic script builds Python dicts, asserts correctness programmatically,
then calls write_topic()/write_mock() which validate the schema and json.dump.
"""
import json
import os
import re
import string
import hashlib
from fractions import Fraction
from xml.etree import ElementTree as ET

HERE = os.path.dirname(os.path.abspath(__file__))
CONTENT = os.path.abspath(os.path.join(HERE, '..', '..'))
TOPIC_DIR = os.path.join(CONTENT, 'ssc-cgl', 'topics', 'reasoning')
MOCK_DIR = os.path.join(CONTENT, 'ssc-cgl', 'mocks', 'parts')
SECTION_DIR = os.path.join(CONTENT, 'ssc-cgl', 'sections')

TOPIC_IDS = ['analogy', 'classification', 'series', 'coding-decoding', 'mathematical-operations',
             'missing-number', 'blood-relations', 'direction-distance', 'order-ranking',
             'seating-arrangement', 'syllogism', 'venn-diagrams', 'dictionary-order',
             'statement-conclusion', 'counting-figures', 'mirror-water-image',
             'paper-folding-cutting', 'embedded-figures', 'cube-dice', 'figure-series']

# ---------------------------------------------------------------- letters
AL = string.ascii_uppercase


def p(c):
    """alphabet position A=1..Z=26"""
    return AL.index(c.upper()) + 1


def L(n):
    """letter for position n (wraps mod 26)"""
    return AL[(n - 1) % 26]


def sh(s, k):
    """shift every letter of s by k (wraps); non-letters kept"""
    return ''.join(L(p(c) + k) if c.isalpha() else c for c in s)


def shv(s, ks):
    """shift letter i of s by ks[i]"""
    assert len(s) == len(ks)
    return ''.join(L(p(c) + k) for c, k in zip(s, ks))


def opp(c):
    """opposite letter (A<->Z, B<->Y ...)"""
    return L(27 - p(c))


def opps(s):
    return ''.join(opp(c) for c in s)


def dm(a, b):
    """wrapped difference b-a mapped into -12..13"""
    d = (p(b) - p(a)) % 26
    return d - 26 if d > 13 else d


def diffs(a, b):
    return [dm(x, y) for x, y in zip(a, b)]


# ---------------------------------------------------------------- series checkers
def _const(xs):
    return len(xs) >= 2 and len(set(xs)) == 1


def simple_rules(seq):
    """Return names of 'simple' rule families that the full numeric sequence fits.
    Used to prove a wrong option is not explainable by an easier rule."""
    rules = []
    n = len(seq)
    d = [b - a for a, b in zip(seq, seq[1:])]
    if _const(d):
        rules.append('AP')
    if all(a != 0 for a in seq[:-1]):
        r = [Fraction(b, 1) / Fraction(a, 1) for a, b in zip(seq, seq[1:])]
        if _const(r):
            rules.append('GP')
    d2 = [b - a for a, b in zip(d, d[1:])]
    if len(d2) >= 2 and _const(d2):
        rules.append('D2')
    d3 = [b - a for a, b in zip(d2, d2[1:])]
    if len(d3) >= 2 and _const(d3):
        rules.append('D3')
    if len(d) >= 3 and all(x != 0 for x in d[:-1]):
        rr = [Fraction(b) / Fraction(a) for a, b in zip(d, d[1:])]
        if _const(rr):
            rules.append('DGP')
    if n >= 4 and seq[1] != seq[0]:
        # x_{k+1} = a*x_k + b  (solve from first 3 terms)
        x0, x1, x2 = map(Fraction, seq[:3])
        if x1 != x0:
            a = (x2 - x1) / (x1 - x0)
            b = x1 - a * x0
            if all(Fraction(seq[i + 1]) == a * Fraction(seq[i]) + b for i in range(n - 1)):
                rules.append('LIN(a=%s,b=%s)' % (a, b))
    if n >= 6:
        od, ev = seq[0::2], seq[1::2]
        def ok(s):
            dd = [y - x for x, y in zip(s, s[1:])]
            if _const(dd):
                return True
            if all(x != 0 for x in s[:-1]):
                rr = [Fraction(y) / Fraction(x) for x, y in zip(s, s[1:])]
                return _const(rr)
            return False
        if ok(od) and ok(ev):
            rules.append('ALT')
    return rules


def check_number_series(terms, options, correct, must_fit=None):
    """terms: list with exactly one '?' ; options: 4 values; correct: the intended value.
    Asserts: correct is in options; no WRONG option makes the sequence fit a simple rule family."""
    assert terms.count('?') == 1
    assert correct in options, (correct, options)
    m = terms.index('?')
    for o in options:
        seq = [o if t == '?' else t for t in terms]
        r = simple_rules(seq)
        if o != correct:
            assert not r, 'wrong option %r fits simple rule %r in %r' % (o, r, seq)
        elif must_fit:
            assert must_fit in ' '.join(r), (r, seq)
    return True


def slot_ok(pos):
    """letter positions of one slot through the series: constant wrapped step, or constant 2nd diff,
    or alternating constant steps"""
    d = [((b - a) % 26) for a, b in zip(pos, pos[1:])]
    if _const(d):
        return True
    dd = [((y - x) % 26) for x, y in zip(d, d[1:])]
    if len(dd) >= 2 and _const(dd):
        return True
    if len(pos) >= 5:
        if _const(d[0::2]) and _const(d[1::2]):
            return True
    return False


def check_letter_series(clusters, options, correct):
    """clusters: list of equal-length strings with one '?'. Wrong options must break every simple slot rule."""
    assert correct in options
    m = clusters.index('?')
    k = len(correct)
    for o in options:
        full = [o if c == '?' else c for c in clusters]
        if len(o) != k:
            continue
        slots_fit = all(slot_ok([p(w[i]) for w in full]) for i in range(k))
        if o == correct:
            assert slots_fit, ('correct does not fit simple slot rules', full)
        else:
            assert not slots_fit, ('wrong option also fits', o, full)
    return True


# ---------------------------------------------------------------- question builder
def _h(s):
    return int(hashlib.md5(s.encode()).hexdigest(), 16)


def Q(id, q, opts, ans, sol, sc=None, d='medium', sub='', pat='', t=45, fig=None, fixed=False, place=None):
    """Build a question. `ans` is the correct option VALUE (not index).
    Unless fixed=True the options are cyclically rotated so the answer lands on a pseudo-random slot."""
    opts = [o if isinstance(o, str) else str(o) for o in opts]
    ans = ans if isinstance(ans, str) else str(ans)
    assert len(opts) == 4, (id, opts)
    assert len(set(opts)) == 4, ('duplicate options', id, opts)
    assert opts.count(ans) == 1, ('answer not in options', id, ans, opts)
    if not fixed:
        target = place if place is not None else _h(id) % 4
        cur = opts.index(ans)
        k = (cur - target) % 4
        opts = opts[k:] + opts[:k]
    idx = opts.index(ans)
    assert d in ('easy', 'medium', 'hard')
    return {'id': id, 'q': q, 'figure': fig, 'options': opts, 'answer': idx, 'solution': sol,
            'shortcut': sc, 'difficulty': d, 'subtopic': sub, 'pattern': pat, 'timeSec': t}


def sub(id, title, concept, formulas=None, tricks=None, mistakes=None):
    return {'id': id, 'title': title, 'concept': concept, 'formulas': formulas or [],
            'tricks': tricks or [], 'mistakes': mistakes or []}


def F(name, tex, note=''):
    return {'name': name, 'tex': tex, 'note': note}


def T(title, body, q, solution):
    return {'title': title, 'body': body, 'example': {'q': q, 'solution': solution}}


def P(pattern, freq, spot, approach):
    assert freq in ('very common', 'common', 'occasional')
    return {'pattern': pattern, 'frequency': freq, 'howToSpot': spot, 'approach': approach}


# ---------------------------------------------------------------- validation + writing
def _check_svg(s, where):
    try:
        el = ET.fromstring(s)
    except ET.ParseError as e:
        raise AssertionError('bad svg in %s: %s' % (where, e))
    assert el.tag.endswith('svg'), where
    assert 'viewBox' in el.attrib, ('svg needs viewBox', where)
    low = s.lower()
    assert 'href' not in low and 'http://' not in low.replace('http://www.w3.org/2000/svg', '') and 'https://' not in low, where
    assert len(s) < 9000, ('svg too big', where, len(s))


def check_question(qd, where, subids=None):
    keys = ['id', 'q', 'figure', 'options', 'answer', 'solution', 'shortcut', 'difficulty', 'subtopic', 'pattern', 'timeSec']
    for k in keys:
        assert k in qd, (where, 'missing', k)
    assert isinstance(qd['q'], str) and qd['q'].strip(), where
    assert len(qd['options']) == 4 and len(set(qd['options'])) == 4, where
    assert qd['answer'] in (0, 1, 2, 3), where
    assert qd['solution'] and qd['solution'].strip(), where
    assert qd['difficulty'] in ('easy', 'medium', 'hard'), where
    assert re.fullmatch(r'[a-z0-9]+(-[a-z0-9]+)*', qd['id']), ('bad id', qd['id'])
    if subids is not None:
        assert qd['subtopic'] in subids, (where, qd['id'], qd['subtopic'])
    if qd['figure']:
        _check_svg(qd['figure'], where + ':' + qd['id'] + ':figure')
    for i, o in enumerate(qd['options']):
        if o.lstrip().startswith('<svg'):
            _check_svg(o, where + ':' + qd['id'] + ':opt%d' % i)
    assert isinstance(qd['timeSec'], int) and 10 <= qd['timeSec'] <= 240, where


def write_topic(t):
    assert t['id'] in TOPIC_IDS
    assert t['order'] == TOPIC_IDS.index(t['id']) + 1
    assert t['sectionId'] == 'reasoning'
    assert t['importance'] in ('high', 'medium', 'low')
    assert 2 <= len(t['subtopics']) <= 6, ('subtopics', len(t['subtopics']))
    assert 4 <= len(t['pyqPatterns']) <= 8, ('patterns', len(t['pyqPatterns']))
    assert 3 <= len(t['solvedExamples']) <= 5, ('examples', len(t['solvedExamples']))
    assert 12 <= len(t['practice']) <= 15, ('practice', len(t['practice']))
    subids = [s['id'] for s in t['subtopics']]
    assert len(set(subids)) == len(subids)
    ntricks = 0
    for s in t['subtopics']:
        assert s['concept'].strip() and s['mistakes'], s['id']
        assert s['tricks'], ('no trick', s['id'])
        ntricks += len(s['tricks'])
        for tr in s['tricks']:
            assert tr['example']['q'] and tr['example']['solution']
        for f in s['formulas']:
            assert not f['tex'].startswith('$'), f
    assert ntricks >= 2
    ids = set()
    for grp in ('solvedExamples', 'practice'):
        for qd in t[grp]:
            check_question(qd, t['id'] + ':' + grp, subids)
            assert qd['id'] not in ids, ('dup id', qd['id'])
            ids.add(qd['id'])
            if grp == 'solvedExamples':
                assert qd['shortcut'], ('example needs shortcut', qd['id'])
    qs = [x['q'] for x in t['solvedExamples'] + t['practice']]
    assert len(set(qs)) == len(qs) or all(x['figure'] for x in t['solvedExamples'] + t['practice'] if qs.count(x['q']) > 1), 'duplicate question text'
    # answer-slot spread sanity
    slots = [x['answer'] for x in t['practice']]
    assert max(slots.count(i) for i in range(4)) <= len(slots) * 0.55, ('answers bunched', slots)
    order = ['id', 'sectionId', 'title', 'order', 'importance', 'avgQuestions', 'summary', 'subtopics',
             'pyqPatterns', 'solvedExamples', 'practice']
    out = {k: t[k] for k in order}
    path = os.path.join(TOPIC_DIR, t['id'] + '.json')
    with open(path, 'w', encoding='utf-8') as f:
        json.dump(out, f, ensure_ascii=False, indent=1)
    json.load(open(path, encoding='utf-8'))
    print('wrote', path, '| subtopics', len(subids), '| patterns', len(t['pyqPatterns']),
          '| examples', len(t['solvedExamples']), '| practice', len(t['practice']))


def topic(id, title, importance, avg, summary, subtopics, patterns, examples, practice):
    return {'id': id, 'sectionId': 'reasoning', 'title': title, 'order': TOPIC_IDS.index(id) + 1,
            'importance': importance, 'avgQuestions': avg, 'summary': summary, 'subtopics': subtopics,
            'pyqPatterns': patterns, 'solvedExamples': examples, 'practice': practice}


def write_mock(mock_id, questions, n):
    assert len(questions) == n, (mock_id, len(questions), n)
    ids = set()
    for qd in questions:
        check_question(qd, mock_id)
        assert qd['subtopic'] in TOPIC_IDS, (qd['id'], qd['subtopic'])
        assert qd['id'] not in ids
        ids.add(qd['id'])
    path = os.path.join(MOCK_DIR, mock_id + '--reasoning.json')
    with open(path, 'w', encoding='utf-8') as f:
        json.dump({'mockId': mock_id, 'sectionId': 'reasoning', 'questions': questions}, f, ensure_ascii=False, indent=1)
    json.load(open(path, encoding='utf-8'))
    print('wrote', path, len(questions))
