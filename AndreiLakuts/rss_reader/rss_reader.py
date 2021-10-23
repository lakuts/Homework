#!/usr/bin/env python3

"""
[Iteration 3] One-shot command-line RSS reader.
"""

from urllib.request import urlopen
from datetime import datetime
import xml.etree.ElementTree as ET
import argparse
import json
import os

VERSION = "Version 1.3"


class RssParser:
    """Basic rss parser class. Contains methods for receiving and processing RSS channels"""

    def __init__(self, source: str, version: bool, json: bool, verbose: bool, limit: int, date: int):
        """
        __init__ method

        :param source: str, RSS URL
        :param version: bool, if True prints VERSION
        :param json: bool, if True prints content in JSON format
        :param verbose: bool, if True prints logs to stdout
        :param limit: int, number of printed news. If not specified, print all available news.
        :param date: int, date in format YYYYMMDD. If specified, print news from cache for this date.
        """

        self.source = source
        self.version = version
        self.json = json
        self.verbose = verbose
        self.limit = limit
        self.date = date
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
        elif self.date:
            if len(str(self.date)) != 8:
                print("Wrong date format!")
            else:
                self.print_if_verbose(
                    f"Method 'run_parsing' is working: \n"
                    f"'run_parsing' method calls 'get_content_from_cache' method: \n")
                self.rss_feed = self.get_content_from_cache()
                if self.rss_feed:
                    if self.json:
                        self.print_if_verbose(f"'run_parsing' method calls 'print_json_content' method: \n")
                        self.print_json_content(self.rss_feed)
                    else:
                        self.print_if_verbose(f"'run_parsing' method calls 'print_content_from_cache' method: \n")
                        self.print_content_from_cache(self.rss_feed)

        else:
            self.print_if_verbose(
                f"Method 'run_parsing' is working: \n"
                f"'run_parsing' method calls 'get_content' method: \n")
            self.content = self.get_content()

            if self.content:
                self.print_if_verbose(f"'run_parsing' method calls 'process_content' method: \n")
                self.rss_feed = self.process_content(self.content)

                self.print_if_verbose(f"'run_parsing' method calls 'save_news_to_cache' method: \n")
                self.save_news_to_cache(self.rss_feed)

                if self.json:
                    self.print_if_verbose(f"'run_parsing' method calls 'print_json_content' method: \n")
                    self.print_json_content(self.rss_feed)
                else:
                    self.print_if_verbose(f"'run_parsing' method calls 'print_content' method: \n")
                    self.print_content(self.rss_feed)

        self.print_if_verbose(f"Program execution completed!")

        return "Program execution completed!"

    def get_content(self):
        """
        Method gets content of the RSS feed and converts it to XML.
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
            child_news["PubDate"] = self.get_formatted_date(item.findtext('pubDate'))
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

    def save_news_to_cache(self, rss_feed):
        """Method saves RSS-feed content to cache."""

        self.print_if_verbose(
            f"Method 'save_news_to_cache' is working: \n"
            f"Saving news to cache... \n"
        )

        rss_feed_to_cache_title = self.source

        if not os.path.exists("cache"):
            os.mkdir("cache")

        os.chdir("cache")

        try:
            with open("rss_reader_cache.json", "r", encoding="utf-8") as cache_file:
                data_from_cache = json.load(cache_file)
        except:
            data_from_cache = [{rss_feed_to_cache_title: []}]
            self.print_if_verbose(f"Cache file does not exist, a new one will be created. \n")

        is_append_flag = False

        for feed in data_from_cache:
            if rss_feed_to_cache_title in feed.keys():
                for news in rss_feed["News"]:
                    if news not in feed[rss_feed_to_cache_title]:
                        feed[rss_feed_to_cache_title].append(news)
                is_append_flag = True

        if not is_append_flag:
            data_from_cache.append({rss_feed_to_cache_title: rss_feed["News"]})

        with open("rss_reader_cache.json", "w", encoding="utf-8") as cache_file:
            json.dump(data_from_cache, cache_file, indent=3)

        os.chdir("..")

        self.print_if_verbose(
            f"News were added to cache succesыfully. \n"
            f"Method 'save_news_to_cache' is finished. \n"
        )

        return data_from_cache

    def get_content_from_cache(self):
        """
        Method gets content from cache and converts it to list.
        :return: rss_feed, list
        """

        rss_feed = []
        news_to_show = 0

        try:
            self.print_if_verbose(
                f"Method 'get_content_from_cache' is working: \n"
                f"Trying to get content from cache..."
            )
            os.chdir("cache")
        except Exception as error:
            print(f"{error}: cache does not exists!")
            return

        try:
            with open("rss_reader_cache.json", "r", encoding="utf-8") as cache_file:
                data_from_cache = json.load(cache_file)
                self.print_if_verbose(f"Content from cache has been received successfully. \n")
        except Exception as error:
            self.print_if_verbose(f"{error}: cache file does not exist! \n")
            return

        if self.source:
            for feed in data_from_cache:
                if self.source in feed.keys():
                    for news in feed[self.source]:
                        if news["PubDate"] == str(self.date):
                            rss_feed.append(news)
                            news_to_show += 1
                            if self.limit and news_to_show == self.limit:
                                break
                if self.limit and news_to_show == self.limit:
                    break
        else:
            for channel in data_from_cache:
                for feed_link in channel:
                    for news in channel[feed_link]:
                        if news["PubDate"] == str(self.date):
                            rss_feed.append(news)
                            news_to_show += 1
                            if self.limit and news_to_show == self.limit:
                                break
                if self.limit and news_to_show == self.limit:
                    break

        os.chdir("..")

        self.news_amount = len(rss_feed)

        if self.news_amount == 0:
            print(f"There is no news in cache for specified date. \n")
        else:
            self.print_if_verbose(f"There is {self.news_amount} news in cache for specified date. \n")

        self.print_if_verbose(f"Method 'get_content_from_cache' is finished. \n")

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

        self.print_if_verbose(f"Method 'print_json_content' is finished. \n")

        return "Content is printed in JSON format"

    def print_content_from_cache(self, rss_feed):
        """Method prints RSS-feed content from cache."""

        self.print_if_verbose(f"Method 'print_content_from_cache' is working: \n")

        for news in rss_feed:
            for key in news.keys():
                print(f"{key}: {news[key]}")
            print()

        self.print_if_verbose(f"Method 'print_content_from_cache' is finished. \n")

        return "Content is printed from cache"

    def print_if_verbose(self, log):
        """Method prints logs in stdout"""

        if self.verbose:
            print(log)
            return log

    def get_formatted_date(self, date):
        """
        Method converts date to format "%Y%m%d" if format of the date
        is in "possible_datetime_formats", else returns date unchanged.
        """

        formatted_date = date

        possible_datetime_formats = [
            "%Y-%m-%dT%H:%M:%S%z",  # "2021-10-19T16:46:02Z"
            "%a, %d %b %Y %H:%M:%S %z",  # "Tue, 19 Oct 2021 21:00:13 +0300"
            "%a, %d %b %Y %H:%M:%S %Z",  # "Tue, 19 Oct 2021 18:54:00 GMT"
            "%a, %d %b %Y %H:%M:%S",  # "Tue, 19 Oct 2021 18:54:00"
        ]

        for format in possible_datetime_formats:
            try:
                formatted_date = datetime.strptime(date, format).strftime("%Y%m%d")
            except:
                pass
        return formatted_date


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
    parser.add_argument("--date", type=str, help="Date (str) in format YYYYMMDD. Print news from cache for this date")

    args = parser.parse_args()

    rss_parser = RssParser(args.source, args.version, args.json, args.verbose, args.limit, args.date)
    rss_parser.run_parsing()


if __name__ == '__main__':
    main_program()
