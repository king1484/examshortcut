# shared mock kit: exec helper sections of the topic scripts + duplicate checks
import json
import os
import re
import common as C

HERE = os.path.dirname(os.path.abspath(__file__))

# ---------------------------------------------------------------- helper namespaces
# each topic script's helpers live above its `subs =` line; exec that slice into its own namespace
CUT = {'t02_classification.py': 29, 't04_coding.py': 96, 't05_mathops.py': 71,
       't06_missing_number.py': 93, 't07_blood_relations.py': 91, 't08_direction.py': 33,
       't09_order_ranking.py': 29, 't10_seating.py': 31, 't11_syllogism.py': 49,
       't12_venn.py': 36, 't13_dictionary.py': 23, 't15_counting.py': 33,
       't16_mirror.py': 105, 't17_folding.py': 67, 't18_embedded.py': 136,
       't19_cube.py': 55, 't20_figseries.py': 49}


def load(name):
    src = open(os.path.join(HERE, name), encoding='utf-8').read().split('\n')
    body = '\n'.join(src[:CUT[name]])
    ns = {'__name__': 'mk.' + name}
    exec(compile(body, name, 'exec'), ns)
    return ns


CL = load('t02_classification.py')   # is_prime, is_sq, is_cube, steps
CD = load('t04_coding.py')           # nat_word_codes, check_word_code, check_number_coding, families_fit
MO = load('t05_mathops.py')          # ev, ltr, fmt, py_ops, disp_ops, expr_str, apply_map, swap_vals
MN = load('t06_missing_number.py')   # ds, rev2, FAMS, fitting, check_missing
BL = load('t07_blood_relations.py')  # person, reset, rel, check_rel
DR = load('t08_direction.py')        # dist, heading_after + engines.walk/dir_name
OR = load('t09_order_ranking.py')    # other_end, check_order
SE = load('t10_seating.py')          # lin_sols, circ_sols, one
SY = load('t11_syllogism.py')        # ALL/NO/SOME/SOMENOT/ONLYFEW, syl
VN = load('t12_venn.py')             # rel_models, ent, poss, check_rel
DI = load('t13_dictionary.py')       # word_rank, brute_rank
CF = load('t15_counting.py')         # fig, cev, grid, FIG, count_triangles, count_rects
MI = load('t16_mirror.py')           # str_q, fig_q, clock_mirror, eleven60
PF = load('t17_folding.py')          # S, folds, fold_q, stages, distractors
EM = load('t18_embedded.py')         # find_q, contain_q, M, N
CB = load('t19_cube.py')             # views_q, net_opp_q, net_cube_q, paint_counts, opp_unique
FS = load('t20_figseries.py')        # st, key, series_q, slots8

from engines import walk, dir_name, count_triangles, count_rects  # noqa: E402

# ---------------------------------------------------------------- duplicate checks
def _norm(s):
    s = re.sub(r'[*_`]', '', s or '')
    return re.sub(r'\s+', ' ', s).strip().lower()


_topic_keys = set()
for _tid in C.TOPIC_IDS:
    _d = json.load(open(os.path.join(C.TOPIC_DIR, _tid + '.json'), encoding='utf-8'))
    for _src in (_d.get('solvedExamples', []), _d.get('practice', [])):
        for _p in _src:
            _topic_keys.add((_norm(_p.get('q', '')), _norm(_p.get('figure') or '')))
assert len(_topic_keys) > 350, len(_topic_keys)

_seen = {}   # mockId -> set of (q, figure) keys, shared across all mocks in this run


def fresh(qd, mock):
    key = (_norm(qd['q']), _norm(qd['figure'] or ''))
    assert key not in _topic_keys, ('duplicates a topic question', qd['id'])
    seen = _seen.setdefault(mock, set())
    for other, keys in _seen.items():
        assert key not in keys, ('duplicates mock', other, qd['id'])
    seen.add(key)
    return qd


# sub-topic labels used inside topic scripts -> the topic id the mock schema needs
SUBTOPIC_MAP = {
    'fold-punch': 'paper-folding-cutting', 'find-hidden': 'embedded-figures',
    'contains-part': 'embedded-figures', 'dice-positions': 'cube-dice',
    'cube-nets': 'cube-dice', 'painted-cubes': 'cube-dice',
    'movement-rotation': 'figure-series', 'addition-change': 'figure-series',
    'triangles': 'counting-figures', 'straight-lines': 'counting-figures',
    'rectangles': 'counting-figures', 'mirror-image': 'mirror-water-image',
    'water-image': 'mirror-water-image',
}


def move(qd, idx):
    """rotate the option list so the answer sits at index idx (rebalancing the key)."""
    opts = qd['options']
    ans = opts[qd['answer']]
    k = (qd['answer'] - idx) % 4
    qd['options'] = opts[k:] + opts[:k]
    assert qd['options'][idx] == ans
    qd['answer'] = idx
    return qd


def fix_subtopics(questions):
    for q in questions:
        q['subtopic'] = SUBTOPIC_MAP.get(q['subtopic'], q['subtopic'])
        assert q['subtopic'] in C.TOPIC_IDS, (q['id'], q['subtopic'])


def answer_spread(questions, label):
    from collections import Counter
    c = Counter(q['answer'] for q in questions)
    print(label, 'answers:', dict(sorted(c.items())))
    assert max(c.values()) - min(c.values()) <= 5, c
    return c


def finish(mock_id, questions, n):
    assert len(questions) == n
    ids = [q['id'] for q in questions]
    assert len(set(ids)) == n
    fix_subtopics(questions)
    for qd in questions:
        fresh(qd, mock_id)
    answer_spread(questions, mock_id)
    C.write_mock(mock_id, questions, n)
    return questions
