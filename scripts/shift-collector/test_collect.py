import contextlib
import datetime as dt
import io
import json
import os
import tempfile
import unittest
from unittest.mock import Mock, patch

import collect


DAY = dt.date(2026, 10, 16)
VIDEO = {"id": "review1", "title": "SSC CGL 16 October 2026 1st shift analysis", "channel": "Exam review"}


class CollectionAvailability(unittest.TestCase):
    def test_proxy_pool_encodes_credentials_deduplicates_and_hides_invalid_entries(self):
        with contextlib.redirect_stderr(io.StringIO()) as output:
            routes = collect.parse_proxy_pool('proxy.test:8080:user:name:p@ss\nhttp://second.test:8000\nhttp://second.test:8000\ninvalid:secret\n')
        self.assertEqual(routes, ['http://user:name%3Ap%40ss@proxy.test:8080', 'http://second.test:8000'])
        self.assertNotIn('secret', output.getvalue())

    def test_environment_pool_precedes_legacy_single_proxy(self):
        with patch.dict(os.environ, {'YT_PROXIES': 'http://pool.test:8080\nhttp://other.test:8080', 'YT_PROXY': 'http://legacy.test:8080'}):
            self.assertEqual(collect._proxy_urls(), ['http://pool.test:8080', 'http://other.test:8080', 'http://legacy.test:8080'])

    def test_second_search_proxy_is_used_by_remaining_workers(self):
        def search(query, **options):
            if options['proxy'] == 'http://dead.test:8080':
                raise collect.yt_dlp.utils.DownloadError('unreachable')
            self.assertEqual(options['proxy'], 'http://working.test:8080')
            self.assertTrue(options['use_proxy'])
            return [VIDEO]
        with patch.object(collect, 'PROXY', 'http://dead.test:8080'), \
             patch.object(collect, 'EXTRA_PROXIES', ['http://working.test:8080']), \
             patch.object(collect, 'yt_search', side_effect=search) as requests:
            self.assertEqual(collect.find_videos(DAY, None), [VIDEO])
            self.assertEqual(requests.call_count, 11)

    def test_transcript_tries_next_proxy_before_direct_or_fallback(self):
        with patch.object(collect, 'PROXY', 'http://dead.test:8080'), \
             patch.object(collect, 'EXTRA_PROXIES', ['http://working.test:8080']), \
             patch.object(collect, 'UNAVAILABLE_TRANSCRIPT_ROUTES', set()), \
             patch.object(collect, 'yt_transcript', side_effect=[{'text': '', 'route_unavailable': True}, {'text': 'review', 'lang': 'en'}]) as fetch, \
             patch.object(collect, 'api_transcript') as fallback:
            self.assertEqual(collect.transcript('video')['text'], 'review')
            self.assertEqual([call.kwargs['proxy'] for call in fetch.call_args_list], ['http://dead.test:8080', 'http://working.test:8080'])
            fallback.assert_not_called()

    def test_missing_captions_does_not_disable_youtube_for_other_videos(self):
        with patch.object(collect, 'PROXY', None), patch.object(collect, 'EXTRA_PROXIES', []), \
             patch.object(collect, 'UNAVAILABLE_TRANSCRIPT_ROUTES', set()), \
             patch.object(collect, 'yt_transcript', side_effect=[{'text': '', 'error': 'no captions'}, {'text': 'second video', 'lang': 'en'}]), \
             patch.object(collect, 'api_transcript', return_value={'text': 'fallback', 'lang': 'en'}):
            self.assertFalse(collect.transcript('first')['yt_blocked'])
            self.assertEqual(collect.transcript('second')['text'], 'second video')

    def test_blocked_routes_are_not_retried_for_every_video(self):
        with patch.object(collect, 'PROXY', 'http://blocked.test:8080'), patch.object(collect, 'EXTRA_PROXIES', []), \
             patch.object(collect, 'UNAVAILABLE_TRANSCRIPT_ROUTES', set()), \
             patch.object(collect, 'yt_transcript', return_value={'text': '', 'blocked': True}) as fetch, \
             patch.object(collect, 'api_transcript', return_value={'text': 'fallback', 'lang': 'en'}):
            self.assertTrue(collect.transcript('first')['yt_blocked'])
            self.assertEqual(collect.transcript('second')['text'], 'fallback')
            self.assertEqual(fetch.call_count, 2)

    def test_transcript_requests_have_bounded_network_timeouts(self):
        with patch.object(collect.requests.Session, 'request', return_value=Mock()) as request:
            collect.TranscriptSession().get('https://www.youtube.com/watch?v=synthetic')
            self.assertEqual(request.call_args.kwargs['timeout'], 15)

    def test_malformed_fallback_response_does_not_crash_collection(self):
        response = Mock(status_code=200)
        response.json.side_effect = ValueError('upstream returned HTML')
        with patch.object(collect.requests, 'get', return_value=response):
            self.assertEqual(collect.api_transcript('video')['error'], 'api: invalid JSON')

    def test_dead_proxy_switches_remaining_searches_to_direct_once(self):
        calls = []
        def search(query, **options):
            calls.append(options["use_proxy"])
            if options["use_proxy"]:
                raise collect.yt_dlp.utils.DownloadError("proxy connection failed")
            return [VIDEO]
        with patch.object(collect, "PROXY", "http://private-proxy"), patch.object(collect, "yt_search", side_effect=search):
            self.assertEqual(collect.find_videos(DAY, None), [VIDEO])
        self.assertEqual(calls.count(True), 1)
        self.assertGreater(calls.count(False), 1)

    def test_one_failed_query_does_not_discard_successful_queries(self):
        def search(query, **options):
            if "all shift" in query:
                raise collect.yt_dlp.utils.DownloadError("temporary search failure")
            return [VIDEO]
        with patch.object(collect, "PROXY", None), patch.object(collect, "yt_search", side_effect=search):
            self.assertEqual(collect.find_videos(DAY, None), [VIDEO])

    def test_network_outage_writes_article_pack_without_crashing(self):
        article = {"title": "SSC CGL 16 October analysis", "url": "https://example.org/review", "text": "Reported review"}
        with tempfile.TemporaryDirectory() as directory, \
             patch.object(collect, "HERE", directory), patch.object(collect, "CACHE", os.path.join(directory, "cache")), \
             patch.object(collect, "PROXY", "http://private-proxy"), \
             patch.object(collect, "yt_search", side_effect=collect.yt_dlp.utils.DownloadError("private credential in upstream error")), \
             patch.object(collect, "web_articles", return_value=[article]) as web, \
             patch("sys.argv", ["collect.py", "--date", DAY.isoformat()]), \
             contextlib.redirect_stderr(io.StringIO()) as errors:
            collect.main()
            with open(os.path.join(directory, "packs", DAY.isoformat(), "pack.json"), encoding="utf8") as stream:
                pack = json.load(stream)
            self.assertEqual(pack["videos"], [])
            self.assertEqual(pack["articles"], [article])
            web.assert_called_once_with(DAY, None)
            self.assertNotIn("private credential", errors.getvalue())

    def test_programming_error_is_not_hidden_as_network_outage(self):
        with patch.object(collect, "yt_search", side_effect=ValueError("unexpected result shape")):
            with self.assertRaises(ValueError):
                collect.find_videos(DAY, None)

    def test_article_search_does_not_depend_on_youtube_proxy(self):
        search = Mock(text='<a class="result__a" href="https://example.org/review">SSC CGL review</a>')
        article = Mock(text="<main>SSC CGL 16 October 2026 first shift analysis</main>")
        with patch.object(collect, "PROXIES", {"https": "http://offline-proxy"}), \
             patch.object(collect.requests, "post", return_value=search) as post, \
             patch.object(collect.requests, "get", return_value=article):
            self.assertEqual(len(collect.web_articles(DAY, None)), 1)
            self.assertNotIn("proxies", post.call_args.kwargs)

    def test_upstream_http_error_does_not_become_article_content(self):
        search = Mock()
        search.raise_for_status.side_effect = collect.requests.HTTPError("503")
        with patch.object(collect.requests, "post", return_value=search):
            self.assertEqual(collect.web_articles(DAY, None), [])


if __name__ == "__main__":
    unittest.main()
