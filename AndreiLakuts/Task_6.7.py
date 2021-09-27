# Task 6.7
# Implement a Pagination class helpful to arrange text on pages and list
# content on given page. The class should take in a text and a positive
# integer which indicate how many symbols will be allowed per each page
# (take spaces into account as well). You need to be able to get the amount
# of whole symbols in text, get a number of pages that came out and method
# that accepts the page number and return quantity of symbols on this page.
# If the provided number of the page is missing print the warning message
# "Invalid index. Page is missing". If you're familliar with using of
# Excpetions in Python display the error message in this way. Pages indexing starts with 0.
# Example:
# >>> pages = Pagination('Your beautiful text', 5)
# >>> pages.page_count
# 4
# >>> pages.item_count
# 19
#
# >>> pages.count_items_on_page(0)
# 5
# >>> pages.count_items_on_page(3)
# 4
# >>> pages.count_items_on_page(4)
# Exception: Invalid index. Page is missing.
# Optional: implement searching/filtering pages by symblos/words and displaying
# pages with all the symbols on it. If you're querying by symbol that appears
# on many pages or if you are querying by the word that is splitted in two
# return an array of all the occurences.
# Example:
# >>> pages.find_page('Your')
# [0]
# >>> pages.find_page('e')
# [1, 3]
# >>> pages.find_page('beautiful')
# [1, 2]
# >>> pages.find_page('great')
# Exception: 'great' is missing on the pages
# >>> pages.display_page(0)
# 'Your '

import math


class Pagination:
    all_pages = {}

    def __init__(self, text, symbols_per_page):
        self.text = text
        self.symbols_per_page = symbols_per_page
        self.p_count = self.page_count()

    def add_all_pages(self):
        """add pages to dict all_pages"""
        i = 0
        for count in range(self.p_count - 1):
            self.all_pages[count] = self.text[i:i + self.symbols_per_page]
            i += self.symbols_per_page
        # add the last page
        self.all_pages[count + 1] = self.text[i:]
        return self.all_pages

    def page_count(self):
        self.p_count = math.ceil(len(self.text) / self.symbols_per_page)
        return self.p_count

    def item_count(self):
        self.i_count = len(self.text)
        return self.i_count

    def count_items_on_page(self, page_number):
        if page_number not in self.all_pages:
            raise Exception(f"Invalid index. Page is missing")
        return len(self.all_pages[page_number])

    def display_page(self, page_number):
        if page_number not in self.all_pages:
            raise Exception(f"Invalid index. Page is missing")
        return self.all_pages[page_number]

    def find_page(self, find_text):
        if find_text not in self.text:
            raise Exception(f"'{find_text}' is missing on the pages")
        else:
            self.f_page = []
            i = self.text.find(find_text)

            while i > -1:

                left_i = i
                right_i = i + len(find_text)

                left_page_i = left_i // self.symbols_per_page
                right_page_i = right_i // self.symbols_per_page + 1
                for page in range(left_page_i, right_page_i):
                    if page not in self.f_page:
                        self.f_page.append(page)

                i = right_i
                i = self.text.find(find_text, i)

        return self.f_page



# Tests
# pages = Pagination('Your beautiful text', 5)
# print(pages.page_count())
# print(pages.item_count())
# print(pages.add_all_pages())
# print(pages.count_items_on_page(0))
# print(pages.count_items_on_page(3))
# # print(pages.count_items_on_page(4))
# print(pages.display_page(3))
# print(pages.display_page(1))
# print(pages.display_page(1))
# print(pages.find_page('o'))
# print(pages.find_page('e'))
# print(pages.find_page('text'))
# print(pages.find_page('beautiful'))

# pages2 = Pagination('beautiful YourYour  beautiful text', 5)
# print(pages2.find_page('Your'))
# print(pages2.find_page('YYYYour'))
# print(pages.find_page('Your'))
# print(pages.find_page('e'))
# print(pages2.find_page('beautiful'))
# print(pages.find_page('great'))
