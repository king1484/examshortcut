"""Deterministic checks for unofficial reports; never invent replacement facts."""
import copy
import re
from urllib.parse import urlparse


def publisher_key(source):
    if source.get('kind') == 'video':
        return source.get('channel', '').strip().casefold() or urlparse(source['url']).hostname
    return (urlparse(source['url']).hostname or '').removeprefix('www.').casefold()


def attempts(value, maximum):
    if not isinstance(value, str):
        return None
    match = re.fullmatch(r"\s*(\d{1,3})(?:\s*[-–—]\s*(\d{1,3}))?(?:\s+overall)?\s*", value, re.I)
    if not match:
        return None
    low, high = int(match[1]), int(match[2] or match[1])
    return value.strip() if 0 <= low <= high <= maximum else None


def recalled_question(text):
    if not isinstance(text, str) or len(text.strip()) < 8:
        return False
    # Questions asked by reviewers about the exam are not questions in the exam.
    interview = r"difficulty|tougher|consumed most time|how many guesses|how many .*solved|new pattern .*appeared|what made reasoning|sectional tim|how was (?:the |your )?(?:exam|paper|shift)|how many attempts|what was your accuracy|did you find .*difficult|are .*questions (?:lengthy|easy|hard)|how is time management|what type of .*questions (?:appear|were asked)"
    return not re.search(interview, text, re.I)


def source_shift_labels(title):
    matches = re.findall(r'\b([123])(?:st|nd|rd)\s*shift\b|\bshift\s*([123])\b', title.lower())
    return {int(label) for pair in matches for label in pair if label}


def balanced_videos(videos, maximum, ordinals):
    buckets = {s: [] for s in (1, 2, 3)}
    general = []
    for video in videos:
        labels = [s for s in buckets if any(k in video['title'].lower() for k in ordinals[s])]
        (buckets[labels[0]] if len(labels) == 1 else general).append(video)
    selected = []
    while any(buckets.values()) and len(selected) < maximum:
        for bucket in buckets.values():
            if bucket and len(selected) < maximum:
                selected.append(bucket.pop(0))
    return (selected + general)[:maximum]


def sanitize_facts(fact):
    fact = copy.deepcopy(fact)
    fact['good_attempts'] = attempts(fact.get('good_attempts'), 100)
    for section in (fact.get('sections') or {}).values():
        if isinstance(section, dict):
            section['good_attempts'] = attempts(section.get('good_attempts'), 25)
    fact['asked'] = [q for q in fact.get('asked', []) if isinstance(q, dict) and recalled_question(q.get('q'))]
    return fact


def sanitize_shift(shift):
    shift = copy.deepcopy(shift)
    notices = list(shift.get('qualityNotes') or [])
    if shift.get('status') in ('pending', 'not-held'):
        return shift
    if shift.get('auto') and shift.get('sources'):
        sources = shift['sources']
        shift['sources'] = [s for s in sources if not source_shift_labels(s['name']) or shift['shift'] in source_shift_labels(s['name'])]
        if len(sources) != len(shift['sources']):
            notices.append('A source labelled for a different shift was removed. The remaining summary has limited coverage and needs further corroboration.')
    value = shift.get('goodAttempts')
    if value and value != 'Not reliably reported' and not attempts(value, 100):
        shift['goodAttempts'] = 'Not reliably reported'
        notices.append('An invalid overall attempt figure was withheld; no replacement estimate was made.')
    for section in shift.get('sections', []):
        value = section.get('goodAttempts')
        if value and not attempts(value, section.get('questions', 25)):
            section.pop('goodAttempts', None)
            notices.append('An invalid section attempt figure was withheld; the section has 25 questions.')
        for topic in section.get('topics', []):
            value = topic.get('count')
            if value and not attempts(value, section.get('questions', 25)):
                topic.pop('count', None)
    original = shift.get('asked', [])
    shift['asked'] = [q for q in original if isinstance(q, dict) and recalled_question(q.get('q'))]
    if len(original) != len(shift['asked']):
        notices.append('Review-interview prompts were removed from the recalled-question list.')
    if notices:
        shift['qualityNotes'] = list(dict.fromkeys(notices))
        if shift.get('auto'):
            shift['status'] = 'partial'
    return shift
