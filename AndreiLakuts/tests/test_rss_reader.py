#!/usr/bin/env python3
"""Unit-tests for RSS-reader."""

import unittest
import xml.etree.ElementTree

from rss_reader.rss_reader import RssParser

# Correct URL fot tests.
good_source = "https://news.yahoo.com/rss/"

# Wrong URL for tests
bad_source = "https://news.yaho.cm/rss/"

# test_rss_feed for test print_content_from_cache() method
test_rss_feed = [{
    'Title': "Test title",
    'Link': 'https://test.link.com',
    'PubDate': '20211022',
    'Source': 'Test source'
}]

# test_rss_feed for test save_news_to_cache() method
test_to_cache_rss_feed = {
    'Feed': 'Test Feed',
    'Description': 'Test Description',
    'Link': 'https://news.yahoo.com/rss/',
    'Language': 'en-US',
    'News': [
        {'Title': "Test Title",
         'Link': 'https://test.link.com/test.html',
         'PubDate': '20211022',
         'Source': 'Test Source'}
    ]
}

# test result for test save_news_to_cache() method
test_to_cache_rss_feed_result = [
    {'https://news.yahoo.com/rss/': [
        {'Link': 'https://test.link.com/test.html',
         'PubDate': '20211022',
         'Source': 'Test Source',
         'Title': 'Test Title'}
    ]
    }
]

# test result for test get_content_from_cache() method
test_from_cache_rss_feed_result = [
    {'Link': 'https://test.link.com/test.html',
     'PubDate': '20211022',
     'Source': 'Test Source',
     'Title': 'Test Title'}
]


class TestRssParser(unittest.TestCase):
    """TestRssParser class contains tests for RssParser"""

    def setUp(self):
        """setUp"""

        self.test_good_source_rss_reader = RssParser(good_source, verbose=True, version=False, json=False,
                                                     limit=3, date=None)
        self.test_bad_source_rss_reader = RssParser(bad_source, verbose=False, version=False, json=False,
                                                    limit=None, date=None)
        self.test_version_rss_reader = RssParser(good_source, verbose=False, version=True, json=False, limit=3,
                                                 date=None)
        self.test_bad_limit_rss_reader = RssParser(good_source, verbose=False, version=False, json=False, limit=-3,
                                                   date=None)
        self.test_date_rss_reader = RssParser(good_source, verbose=False, version=False, json=False, limit=2,
                                              date=20211022)
        self.content = self.test_good_source_rss_reader.get_content()
        self.rss_feed = self.test_good_source_rss_reader.process_content(self.content)
        self.limit_rss_feed = self.test_good_source_rss_reader.process_content(self.content)

    def test_run_parsing(self):
        """Tests for RssParser.run_pursing"""

        # Test "--version"
        self.assertEqual(self.test_version_rss_reader.run_parsing(), "Version 1.3")
        # Test wrong limit "--limit -3"
        self.assertEqual(self.test_bad_limit_rss_reader.run_parsing(), "Limit must be greater than 0!")

    def test_get_content(self):
        """Tests for RssParser.get_content"""

        # Test: get_content().tag mast be "channel"
        self.assertEqual(self.test_good_source_rss_reader.get_content().tag, "channel")
        # Test: type(self.content) must be xml.etree.ElementTree.Element
        self.assertEqual(type(self.content), xml.etree.ElementTree.Element)

    def test_process_content(self):
        """Tests for RssParser.process_content"""

        # Test: type(self.content) must be dict
        self.assertEqual(type(self.test_good_source_rss_reader.process_content(self.content)), dict)
        # Test: if "--limit 3" len(self.limit_rss_feed["News"]) must be 3
        self.assertEqual(len(self.limit_rss_feed["News"]), 3)

    def test_print_content(self):
        """Tests for RssParser.print_content"""

        # RssParser.print_content() must return "Content is printed in STANDARD format"
        self.assertEqual(self.test_good_source_rss_reader.print_content(self.rss_feed),
                         "Content is printed in STANDARD format")

    def test_print_json_content(self):
        """Tests for RssParser.print_json_content"""

        # RssParser.print_json_content() must return "Content is printed in JSON format"
        self.assertEqual(self.test_good_source_rss_reader.print_json_content(self.rss_feed),
                         "Content is printed in JSON format")

    def test_print_if_verbose(self):
        """Tests for RssParser.print_if_verbose"""

        self.assertEqual(self.test_good_source_rss_reader.print_if_verbose(f"Start program."), "Start program.")

    def test_get_content_bad_source(self):
        """Tests for RssParser.get_content if URL is wrong"""

        # Test: if URL is wrong RssParser.get_content returns None"
        self.assertEqual(self.test_bad_source_rss_reader.get_content(), None)

    def test_print_content_from_cache(self):
        """Test for RssParser.print_content_from_cache"""

        self.assertEqual(self.test_good_source_rss_reader.print_content_from_cache(test_rss_feed),
                         "Content is printed from cache")

    def test_save_news_to_cache(self):
        """Test for RssParser.save_news_to_cache"""

        self.assertEqual(self.test_good_source_rss_reader.save_news_to_cache(test_to_cache_rss_feed),
                         test_to_cache_rss_feed_result)

    def test_get_content_from_cache(self):
        """Test for RssParser.get_content_from_cache"""

        self.assertEqual(self.test_date_rss_reader.get_content_from_cache(), test_from_cache_rss_feed_result)

    def test_runparsing(self):
        """Test for RssParser.run_parsing"""

        self.assertEqual(self.test_date_rss_reader.run_parsing(), "Program execution completed!")


if __name__ == '__main__':
    unittest.main()
