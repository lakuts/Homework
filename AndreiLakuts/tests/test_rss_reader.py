#!/usr/bin/env python3
"""Unit-tests for RSS-reader."""

import unittest
import xml.etree.ElementTree

from rss_reader.rss_reader import RssParser

# Correct URL fot tests.
good_source = "https://news.yahoo.com/rss/"
# Wrong URL for tests
bad_source = "https://news.yaho.cm/rss/"


class TestRssParser(unittest.TestCase):
    def setUp(self):
        """setUp"""

        self.test_good_source_rss_reader = RssParser(good_source, verbose=True, version=False, json=False,
                                                     limit=3)
        self.test_bad_source_rss_reader = RssParser(bad_source, verbose=False, version=False, json=False,
                                                    limit=None)
        self.test_version_rss_reader = RssParser(good_source, verbose=False, version=True, json=False, limit=3)
        self.test_bad_limit_rss_reader = RssParser(good_source, verbose=False, version=False, json=False, limit=-3)
        self.content = self.test_good_source_rss_reader.get_content()
        self.rss_feed = self.test_good_source_rss_reader.process_content(self.content)
        self.limit_rss_feed = self.test_good_source_rss_reader.process_content(self.content)

    def test_run_parsing(self):
        """Tests for RssParser.run_pursing"""

        # Test "--version"
        self.assertEqual(self.test_version_rss_reader.run_parsing(), "Version 1.1")
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


if __name__ == '__main__':
    unittest.main()
