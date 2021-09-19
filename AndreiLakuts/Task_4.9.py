# Task 4.9
# Implement a bunch of functions which receive a changeable number of strings and return next parameters:
# 1.	characters that appear in all strings
# 2.	characters that appear in at least one string
# 3.	characters that appear at least in two strings
# 4.	characters of alphabet, that were not used in any string
# Note: use string.ascii_lowercase for list of alphabet letters
# test_strings = ["hello", "world", "python", ]
# print(test_1_1(*strings))
# >>> {'o'}
# print(test_1_2(*strings))
# >>> {'d', 'e', 'h', 'l', 'n', 'o', 'p', 'r', 't', 'w', 'y'}
# print(test_1_3(*strings))
# >>> {'h', 'l', 'o'}
# print(test_1_4(*strings))
# >>> {'a', 'b', 'c', 'f', 'g', 'i', 'j', 'k', 'm', 'q', 's', 'u', 'v', 'x', 'z'}

def test_1_1(*args):
    """test_1_1(string1: str, ... , stringN: str)
    Function returns characters that appear in all strings.
    Case-insensitive"""

    import string
    alphabet = set(string.ascii_lowercase)
    characters_in_all_strings = alphabet

    for string in args:
        characters_in_all_strings.intersection_update(set(string.lower()))

    return characters_in_all_strings


def test_1_2(*args):
    """test_1_2(string1: str, ... , stringN: str)
    Function returns characters that appear in at least one string.
    Case-insensitive"""

    all_characters_in_all_string = set()

    for string in args:
        all_characters_in_all_string.update(set(string))

    return all_characters_in_all_string


def test_1_3(*args):
    """test_1_3(string1: str, ... , stringN: str)
    Function returns characters that appear at least in two strings.
    Case-insensitive"""

    characters_in_two_string = set()

    for i in range(len(args) - 1):
        for j in range(i + 1, len(args)):
            characters_in_two_string.update(set(args[i]) & set(args[j]))

    return characters_in_two_string


def test_1_4(*args):
    """test_1_4(string1: str, ... , stringN: str)
    Function returns characters of alphabet, that were not used in any string.
    Case-insensitive"""

    import string
    alphabet = set(string.ascii_lowercase)
    characters_not_in_any_string = alphabet

    for string in args:
        characters_not_in_any_string.difference_update(set(string.lower()))

    return characters_not_in_any_string
