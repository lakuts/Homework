# Task 5.2
# Implement a function which search for most common words
# in the file. Use data/lorem_ipsum.txt file as a example.
# def most_common_words(filepath, number_of_words=3):
#     pass
#
# print(most_common_words('lorem_ipsum.txt'))
# >>> ['donec', 'etiam', 'aliquam']
# NOTE: Remember about dots, commas, capital letters etc.


def most_common_words(input_file, number_of_words = 3):
    """most_common_words(input_file: str, number_of_words: int, as default 3)
    Function gets a file and returns "number_of_words" of the most common words"""
    from string import punctuation

    def remove_punctuation(word):
        """Function removes punctuation marks from input string"""
        for char in word:
            if char in punctuation:
                word = word.replace(char, "")

        return word

    word_counter = {}

    # Read data from input file, put the words into dictionary
    # "word_counter" and count them
    with open(input_file, 'r', encoding="utf-8") as file:
        for line in file:
            for word in line.lower().split():
                word = remove_punctuation(word)
                if word in word_counter:
                    word_counter[word] += 1
                else:
                    word_counter[word] = 1

    # Сheck if there are enough words in the dictionary.
    # Тhere should be no less than "number_of_words"
    if number_of_words > len(word_counter):
        return "ERROR: number of words in file is less than requested"

    output_list = []

    # Choose the "number_of_words" most common words
    for i in range(number_of_words):
        max_value = 0
        max_word = ""
        for word in word_counter:
            if word_counter[word] > max_value:
                max_value = word_counter[word]
                max_word = word
        output_list.append(max_word)
        del word_counter[max_word]

    return output_list


print(most_common_words('lorem_ipsum.txt'))