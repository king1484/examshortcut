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
