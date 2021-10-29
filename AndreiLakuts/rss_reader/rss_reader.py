#!/usr/bin/env python3

"""
[Iteration 4] One-shot command-line RSS reader.
"""

from urllib.request import urlopen
from urllib.request import urlretrieve
from datetime import datetime
import xml.etree.ElementTree as ET
import argparse
import json
import os
import base64

VERSION = "Version 1.4"


class RssParser:
    """Basic rss parser class. Contains methods for receiving and processing RSS channels"""

    def __init__(self, source: str, version: bool, json: bool, verbose: bool, limit: int, date: int, to_html: str,
                 to_fb2: str):
        """
        __init__ method

        :param source: str, RSS URL
        :param version: bool, if True prints VERSION
        :param json: bool, if True prints content in JSON format
        :param verbose: bool, if True prints logs to stdout
        :param limit: int, number of printed news. If not specified, print all available news.
        :param date: int, date in format YYYYMMDD. If specified, print news from cache for this date.
        :param to_html: str, path to folder. If specified, save news to this folder in file rss_news.html.
        :param to_fb2: str, path to folder. If specified, save news to this folder in file rss_news.fb2.
        """

        self.source = source
        self.version = version
        self.json = json
        self.verbose = verbose
        self.limit = limit
        self.date = date
        self.to_html_path = to_html
        self.to_fb2_path = to_fb2

        self.content = ""
        self.news_amount = 0
        self.full_path_to_image_cache = ""
        self.binaries = ""

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

                if self.to_html_path:
                    self.print_if_verbose(f"'run_parsing' method calls 'save_to_html' method: \n")
                    self.save_to_html(self.rss_feed)

                if self.to_fb2_path:
                    self.print_if_verbose(f"'run_parsing' method calls 'save_to_fb2' method: \n")
                    self.save_to_fb2(self.rss_feed)

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

                if self.to_html_path:
                    self.print_if_verbose(f"'run_parsing' method calls 'save_to_html' method: \n")
                    self.save_to_html(self.rss_feed)

                if self.to_fb2_path:
                    self.print_if_verbose(f"'run_parsing' method calls 'save_to_fb2' method: \n")
                    self.save_to_fb2(self.rss_feed)

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
                f"There are {self.news_amount} news in the feed. \n"
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

        POSSIBLE_IMAGE_TAGS = ("content", "thumbnail", "image")
        POSSIBLE_IMAGE_ATTR = ("url", "href")

        for item in channel.iterfind("item"):
            child_news = {}
            child_news["Title"] = item.findtext("title")
            child_news["Link"] = item.findtext("link")
            child_news["PubDate"] = self.get_formatted_date(item.findtext("pubDate"))
            child_news["Source"] = item.findtext("source")
            child_news["ImageLink"] = None
            child_news["ImageCacheName"] = None

            for tag in POSSIBLE_IMAGE_TAGS:
                for item_field in item:
                    if tag in item_field.tag:
                        for attr in POSSIBLE_IMAGE_ATTR:
                            if attr in item_field.attrib:
                                child_news["ImageLink"] = item_field.attrib[attr]
                                child_news["ImageCacheName"] = \
                                    f"{''.join(char for char in child_news['Link'] if char.isalnum())}.jpg"
                                break
                    if child_news["ImageLink"]:
                        break
                if child_news["ImageLink"]:
                    break

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

        if not os.path.exists("image_cache"):
            os.mkdir("image_cache")
        os.chdir("image_cache")
        self.full_path_to_image_cache = os.getcwd()
        os.chdir("..")

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
                        self.save_image_to_image_cache(news["ImageLink"], f"{news['ImageCacheName']}")
                is_append_flag = True

        if not is_append_flag:
            data_from_cache.append({rss_feed_to_cache_title: rss_feed["News"]})
            for news in rss_feed["News"]:
                self.save_image_to_image_cache(news["ImageLink"], f"{news['ImageCacheName']}")

        with open("rss_reader_cache.json", "w", encoding="utf-8") as cache_file:
            json.dump(data_from_cache, cache_file, indent=3)

        os.chdir("..")

        self.print_if_verbose(
            f"News were added to cache successfully. \n"
            f"Method 'save_news_to_cache' is finished. \n"
        )

        return data_from_cache

    def save_image_to_image_cache(self, image_url, image_name):
        """Method saves images to local image_cache"""

        self.print_if_verbose(
            f"Method 'save_image_to_image_cache' is working: \n"
            f"Saving image to image_cache... \n"
        )

        os.chdir("image_cache")

        try:
            urlretrieve(image_url, image_name)
            self.print_if_verbose(f"Image was saved successfully. \n")
        except Exception as error:
            self.print_if_verbose(f"{error} - image was not saved. \n")

        self.print_if_verbose(f"Method 'save_image_to_image_cache' is finished. \n")

        os.chdir("..")

        return True

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
            os.chdir("image_cache")
            self.full_path_to_image_cache = os.getcwd()
            os.chdir("..")
        except:
            pass

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
        """Method prints logs to stdout"""

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

    def save_to_html(self, rss_feed, date=None):
        """Method saves RSS-feed content to HTML-file.
        If path is wrong returns exception."""

        self.print_if_verbose(f"Method 'save_to_html' is working: \n")

        add_to_html_file = "<!DOCTYPE html>\n<html lang='en'>\n<head>\n<meta charset='UTF-8'>\n</head>\n<body>\n"

        if not os.path.exists(self.to_html_path):
            try:
                os.makedirs(self.to_html_path)
            except Exception as error:
                print(f"Exception {error} - wrong path! File was not created!")
                return

        os.chdir(self.to_html_path)

        with open("rss_news.html", "w", encoding="utf-8") as html_file:
            html_file.writelines(add_to_html_file)

            if self.date:
                for news in rss_feed:
                    html_file.writelines(self.add_to_html(news))
            else:
                for news in rss_feed["News"]:
                    html_file.writelines(self.add_to_html(news))

            add_to_html_file = "</body>\n</html>\n"
            html_file.writelines(add_to_html_file)

        self.print_if_verbose(
            f"File {self.to_html_path}{os.sep}rss_news.html was created successfully. \n"
            f"Method 'save_to_html' is finished.\n"
        )

        return True

    def add_to_html(self, news: dict) -> str:
        """
        Method converts a news to HTML-format.
        :param news: dict
        :return: str, add_to_html_file
        """

        add_to_html_file = ""
        add_to_html_file += f"<h2>Title: {news['Title']}</h2>\n"
        add_to_html_file += f"<a href={news['Link']}>Link to news</a><br>\n"
        add_to_html_file += f"<p>PubDate: {news['PubDate']}</p>\n"
        add_to_html_file += f"<p>Source: {news['Source']}</p>\n"
        full_path_to_image = f"{self.full_path_to_image_cache}{os.sep}{news['ImageCacheName']}"
        add_to_html_file += f"<img height='120' src='{full_path_to_image}' alt='No image'>\n<br>\n<br>\n"

        return add_to_html_file

    def save_to_fb2(self, rss_feed, date=None):
        """Method saves RSS-feed content to FB2-file.
        If path is wrong returns exception."""

        self.print_if_verbose(f"Method 'save_to_fb2' is working: \n")

        if not os.path.exists(self.to_fb2_path):
            try:
                os.makedirs(self.to_fb2_path)
            except Exception as error:
                print(f"Exception {error} - wrong path! File was not created!")
                return

        os.chdir(self.to_fb2_path)

        with open("rss_news.fb2", "w", encoding="utf-8") as fb2_file:
            fb2_file.writelines(f"<?xml version='1.0' encoding='UTF-8'?>\n")
            fb2_file.writelines(
                f"<FictionBook xmlns='http://www.gribuser.ru/xml/fictionbook/2.0' "
                f"xmlns:l='http://www.w3.org/1999/xlink'>\n")
            fb2_file.writelines(f"  <body>\n")
            fb2_file.writelines(f"    <section>\n")

            if self.date:
                for news in rss_feed:
                    fb2_file.writelines(self.add_to_fb2(news))
            else:
                for news in rss_feed["News"]:
                    fb2_file.writelines(self.add_to_fb2(news))

            fb2_file.writelines(f"    </section>\n")
            fb2_file.writelines("  </body>\n")
            fb2_file.writelines(self.binaries)
            fb2_file.writelines("</FictionBook>\n")

        self.print_if_verbose(
            f"File {self.to_fb2_path}{os.sep}rss_news.fb2 was created successfully. \n"
            f"Method 'save_to_fb2' is finished.\n"
        )

        return True

    def add_to_fb2(self, news: dict) -> str:
        """
        Method converts a news to FB2-format.
        :param news: dict
        :return: str, add_to_fb2_file
        """

        add_to_fb2_file = ""
        add_to_fb2_file += f"      <p>Title: {news['Title']}</p>\n"
        add_to_fb2_file += f"      <p><a l:href='{news['Link']}'> 'Link to news' </a></p>\n"
        add_to_fb2_file += f"      <p>PubDate: {news['PubDate']}</p>\n"
        add_to_fb2_file += f"      <p>Source: {news['Source']}</p>\n"

        if news['ImageCacheName']:
            add_to_fb2_file += f"      <p><image l:href='#{news['ImageCacheName']}'/></p>\n"
            with open(f"{self.full_path_to_image_cache}{os.sep}{news['ImageCacheName']}", "rb") as img_file:
                b64_string = base64.b64encode(img_file.read())
                self.binaries += f"<binary id='{news['ImageCacheName']}' " \
                                 f"content-type='image/jpeg'>{b64_string.decode('utf-8')}</binary>\n"

        add_to_fb2_file += f"      <empty-line/>\n"

        return add_to_fb2_file


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
    parser.add_argument("--to_html", type=str, help="Path to folder where news will be saved in file rss_news.html")
    parser.add_argument("--to_fb2", type=str, help="Path to folder where news will be saved in file rss_news.fb2")

    args = parser.parse_args()

    rss_parser = RssParser(args.source, args.version, args.json, args.verbose, args.limit, args.date, args.to_html,
                           args.to_fb2)

    rss_parser.run_parsing()


if __name__ == '__main__':
    main_program()
