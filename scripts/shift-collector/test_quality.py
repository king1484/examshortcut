import unittest
from quality import attempts, recalled_question, sanitize_shift, sanitize_facts, balanced_videos, source_shift_labels, publisher_key, is_shift_source, supported_attempt_total


class QualityChecks(unittest.TestCase):
    def test_merged_total_needs_explicit_count_evidence(self):
        self.assertFalse(supported_attempt_total('83–87 overall', [{'good_attempts': None, 'mentions': ['Accuracy 87%']}]))
        self.assertFalse(supported_attempt_total('95–100 overall', [{'good_attempts': '75–80'}]))
        self.assertTrue(supported_attempt_total('75–85 overall', [{'good_attempts': '75–80'}, {'good_attempts': '80–85'}]))

    def test_survey_is_not_shift_evidence(self):
        survey = {'name': 'RealMocks attempts analysis', 'url': 'https://realmocks.com/attempts-analysis/ssc-cgl-2026'}
        self.assertFalse(is_shift_source(survey))
        original = {'auto': True, 'shift': 3, 'status': 'reported', 'sources': [survey, {'name': 'Video', 'url': 'https://youtube.com/watch?v=x'}],
                    'goodAttempts': '83–87 overall', 'summary': 'The paper was moderate. Good attempts were 83% to 87%.',
                    'observations': ['Average attempts were 84.8.', 'Reasoning required careful reading.']}
        result = sanitize_shift(original)
        self.assertEqual(result['goodAttempts'], 'Not reliably reported')
        self.assertEqual(result['summary'], 'The paper was moderate.')
        self.assertEqual(result['observations'], ['Reasoning required careful reading.'])
        self.assertEqual(len(result['sources']), 1)
        self.assertEqual(result['status'], 'partial')
        self.assertEqual(sanitize_shift(result), result)

    def test_contradictory_total_is_withheld(self):
        original = {'auto': True, 'status': 'reported', 'goodAttempts': '17–18 overall',
                    'sections': [{'questions': 25, 'goodAttempts': s} for s in ['20–22', '14–17', '16–19', '20–23']]}
        result = sanitize_shift(original)
        self.assertEqual(result['goodAttempts'], 'Not reliably reported')
        self.assertEqual(result['status'], 'partial')
        original['goodAttempts'] = '75–80 overall'
        self.assertEqual(sanitize_shift(original)['goodAttempts'], '75–80 overall')

    def test_distinct_publisher_not_article_titles(self):
        a = {'kind': 'article', 'channel': 'First title', 'url': 'https://www.example.com/a'}
        b = {'kind': 'article', 'channel': 'Second title', 'url': 'https://example.com/b'}
        self.assertEqual(publisher_key(a), publisher_key(b))
        self.assertEqual(publisher_key({'kind': 'video', 'channel': ' Channel A ', 'url': 'https://youtube.com/watch?v=a'}), 'channel a')

    def test_scope_and_ranges(self):
        self.assertEqual(attempts('20–23', 25), '20–23')
        self.assertEqual(attempts('75–90 overall', 100), '75–90 overall')
        for value in ['70–80', '18–75', '26', '23–20', '-1', '25 in 8 min', 'most']:
            self.assertIsNone(attempts(value, 25))

    def test_exam_question_not_interview(self):
        self.assertTrue(recalled_question('What is the SI unit of magnetic flux?'))
        self.assertFalse(recalled_question('Which math topics consumed most time?'))
        self.assertFalse(recalled_question('How many guesses were taken?'))
        self.assertFalse(recalled_question('What was the difficulty of the comprehension passage?'))
        for question in ['Are Math questions lengthy or normal?', 'How is time management in Math?',
                         'What type of English questions appear?', 'How many attempts did you score in reasoning?',
                         'What was your accuracy in General Awareness?', 'Did you find Quantitative Aptitude difficult?',
                         'How many attempts in English comprehension?']:
            self.assertFalse(recalled_question(question), question)

    def test_cleanup_preserves_valid_evidence(self):
        original = {'auto': True, 'status': 'reported', 'goodAttempts': '75–90 overall',
                    'sections': [{'id': 'quant', 'questions': 25, 'goodAttempts': '70–80',
                                  'topics': [{'topic': 'Geometry', 'count': '2-3'}]}],
                    'asked': [{'q': 'How many guesses were taken?'}, {'q': 'What is the SI unit of magnetic flux?'}]}
        result = sanitize_shift(original)
        self.assertEqual(result['status'], 'partial')
        self.assertNotIn('goodAttempts', result['sections'][0])
        self.assertEqual(result['sections'][0]['topics'][0]['count'], '2-3')
        self.assertEqual(len(result['asked']), 1)
        self.assertEqual(sanitize_shift(result), result)
        self.assertEqual(original['sections'][0]['goodAttempts'], '70–80')

    def test_filter_before_merge(self):
        result = sanitize_facts({'good_attempts': '80', 'sections': {'quant': {'good_attempts': '80'}}, 'asked': []})
        self.assertEqual(result['good_attempts'], '80')
        self.assertIsNone(result['sections']['quant']['good_attempts'])

    def test_later_shift_is_not_starved(self):
        videos = [{'id': str(n), 'title': '1st shift'} for n in range(12)]
        videos += [{'id': 's2', 'title': '2nd shift'}, {'id': 's3', 'title': '3rd shift'}]
        selected = balanced_videos(videos, 6, {1: ['1st'], 2: ['2nd'], 3: ['3rd']})
        self.assertEqual([v['id'] for v in selected[:3]], ['0', 's2', 's3'])
        self.assertEqual(len(selected), 6)
        self.assertEqual(source_shift_labels('10 October 1st shift review'), {1})
        self.assertEqual(source_shift_labels('Shift 2 and Shift 3'), {2, 3})

    def test_other_shift_source_withheld(self):
        result = sanitize_shift({'auto': True, 'shift': 2, 'status': 'reported', 'sources': [
            {'name': 'Channel - 1st shift analysis', 'url': 'a'}, {'name': 'Channel B - 2nd shift analysis', 'url': 'b'}]})
        self.assertEqual(result['sources'], [{'name': 'Channel B - 2nd shift analysis', 'url': 'b'}])
        self.assertEqual(result['status'], 'partial')


if __name__ == '__main__':
    unittest.main()
