# Task 4.6
# Implement a function get_longest_word(s: str) -> str
# which returns the longest word in the given string.
# The word can contain any symbols except whitespaces ( , \n, \t and so on).
# If there are multiple longest words in the string with a same length
# return the word that occures first. Example:
# >>> get_longest_word('Python is simple and effective!')
# # 'effective!'
#
# >>> get_longest_word('Any pythonista like namespaces a lot.')
# 'pythonista'

def get_longest_word(input_string):
    """Function get_longest_word(input_string: string) -> longest_word: string
    returns the longest word in the given string."""

    longest_word = ""
    for word in input_string.split():
        if len(word) > len(longest_word):
            longest_word = word

    return longest_word