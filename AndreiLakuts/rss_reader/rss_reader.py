#!/usr/bin/env python3

"""
[Iteration 1] One-shot command-line RSS reader.
"""

from urllib.request import urlopen
import xml.etree.ElementTree as ET
import argparse
import json

VERSION = "Version 1.1"


class RssParser:
    """Basic rss parser class. Contains methods for receiving and processing RSS channels"""

    def __init__(self, source: str, version: bool, json: bool, verbose: bool, limit: int):
        """
        __init__ method

        :param source: str, RSS URL
        :param version: bool, if True prints VERSION
        :param json: bool, if True prints content in JSON format
        :param verbose: bool, if True prints logs to stdout
        :param limit: int, number of printed news. If not specified, print all available news.
        """

        self.source = source
        self.version = version
        self.json = json
        self.verbose = verbose
        self.limit = limit
        self.content = ""
        self.news_amount = 0

        self.print_if_verbose(
            f"Start program. \n\n"
            f"RssParser Class object was created. \n"
        )

    def run_parsing(self):
        """
        Runs class-methods according to the input parameters.
        :return: None
        """

        if self.version:
            print(f'"{VERSION}"')
            return VERSION
        elif self.limit is not None and self.limit <= 0:
            print("Limit must be greater than 0!")
            return "Limit must be greater than 0!"
        else:
            self.print_if_verbose(
                f"Method 'run_parsing' is working: \n"
                f"'run_parsing' method calls 'get_content' method: \n")
            self.content = self.get_content()

            if self.content:
                self.print_if_verbose(f"'run_parsing' method calls 'process_content' method: \n")
                self.rss_feed = self.process_content(self.content)

                if self.json:
                    self.print_if_verbose(f"'run_parsing' method calls 'print_json_content' method: \n")
                    self.print_json_content(self.rss_feed)
                else:
                    self.print_if_verbose(f"'run_parsing' method calls 'print_content' method: \n")
                    self.print_content(self.rss_feed)

        self.print_if_verbose(f"Program execution completed!")

    def get_content(self):
        """
        Method gets content of the RSS feed and converts it to CML.
        If URL is wrong returns exception.
        :return: self.content, XML element.
        """
        try:
            self.print_if_verbose(
                f"Method 'get_content' is working: \n"
                f"Trying to get content from RSS source: {self.source} ..."
            )

            rss_xml = urlopen(self.source).read().decode("utf-8")
            self.news_amount = rss_xml.count("<item>")
            xml_tree = ET.ElementTree(ET.fromstring(rss_xml))
            self.content = xml_tree.find('channel')

            self.print_if_verbose(
                f"Content of the RSS-source has been received successfully. \n"
                f"Tere are {self.news_amount} news in the feed. \n"
                f"Method 'get_content' is finished. \n"
            )

            return self.content

        except Exception as error:
            print(f"Exception {error}- wrong URL! The program is stopped.")

    def process_content(self, channel) -> dict:
        """
        Method gets XML element and converts it to dict.
        :param channel: XML element.
        :return: rss_feed, dict
        """

        self.print_if_verbose(f"Method 'process_content' is working:")

        if self.limit is None or self.limit >= self.news_amount:
            self.limit = self.news_amount

        rss_feed = {}
        rss_feed["Feed"] = channel.findtext('title')
        rss_feed["Description"] = channel.findtext('description')
        rss_feed["Link"] = channel.findtext('link')
        rss_feed["Language"] = channel.findtext('language')
        rss_feed["News"] = []

        append_news_to_rss_feed = 0

        self.print_if_verbose(f"Adding data to the work dict 'rss_feed'...")

        for item in channel.iterfind('item'):
            child_news = {}
            child_news["Title"] = item.findtext('title')
            child_news["Link"] = item.findtext('link')
            child_news["PubDate"] = item.findtext('pubDate')
            child_news["Source"] = item.findtext('source')
            rss_feed["News"].append(child_news)

            append_news_to_rss_feed += 1
            if append_news_to_rss_feed == self.limit:
                break

        self.print_if_verbose(
            f"{append_news_to_rss_feed} news were added. \n"
            f"Method 'process_content' is finished. \n"
        )

        return rss_feed

    def print_content(self, rss_feed):
        """Method prints RSS-feed content in standard format."""

        self.print_if_verbose(
            f"Method 'print_content' is working: \n"
            f"Print information about RSS-feed: \n"
        )

        for key in rss_feed:
            if type(rss_feed[key]) != list:
                print(f"{key}: {rss_feed[key]}")

        print()

        self.print_if_verbose(f"\n{self.limit} news will be shown: \n")

        news_number = 1
        for news in rss_feed["News"]:
            print("News", news_number)
            for item in news:
                print(f"{item}: {news[item]}")
            print()
            news_number += 1

        self.print_if_verbose(
            f"{self.limit} news of {self.news_amount} are showed. \n"
            f"Method 'print_content' is finished.\n"
        )

        return "Content is printed in STANDARD format"

    def print_json_content(self, rss_feed):
        """Method prints RSS-feed content in JSON format."""

        self.print_if_verbose(
            f"Method 'print_json_content' is working: \n"
            f"RSS feed will be printed in JSON format: \n"
        )

        json_content = json.dumps(rss_feed, indent=3)
        print(json_content)

        self.print_if_verbose(
            f"{self.limit} news of {self.news_amount} are showed \n"
            f"Method 'print_json_content' is finished. \n"
        )

        return "Content is printed in JSON format"

    def print_if_verbose(self, log):
        """Method prints logs in stdout"""
        if self.verbose:
            print(log)
            return log


def main_program():
    """
    Main program: gets input parameters and creates RssParser-class object with these parameters.
    :return: None
    """
    parser = argparse.ArgumentParser(description="Pure Python command-line RSS reader.")

    parser.add_argument("source", type=str, nargs="?", help="RSS URL")

    parser.add_argument("--version", help="Show program version and exit", action="store_true")
    parser.add_argument("--json", help="Print result as JSON in stdout", action="store_true")
    parser.add_argument("--verbose", help="Outputs verbose status messages", action="store_true")
    parser.add_argument("--limit", type=int, help="Limit (int) news topics if this parameter provided")

    args = parser.parse_args()

    rss_parser = RssParser(args.source, args.version, args.json, args.verbose, args.limit)
    rss_parser.run_parsing()


if __name__ == '__main__':
    main_program()
