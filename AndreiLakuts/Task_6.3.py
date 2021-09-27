# Task 6.3
#     Implement The Keyword encoding and decoding for latin alphabet.
#     The Keyword Cipher uses a Keyword to rearrange the letters in the alphabet.
#     Add the provided keyword at the begining of the alphabet.
#     A keyword is used as the key, and it determines the letter
#     matchings of the cipher alphabet to the plain alphabet.
#     Repeats of letters in the word are removed, then the cipher alphabet is
#     generated with the keyword matching to A, B, C etc. until the keyword is
#     used up, whereupon the rest of the ciphertext letters are used in
#     alphabetical order, excluding those already used in the key.
# Encryption: Keyword is "Crypto"
# •	A B C D E F G H I J K L M N O P Q R S T U V W X Y Z
# •	C R Y P T O A B D E F G H I J K L M N Q S U V W X Z
# Example:
# >>> cipher = Cipher("crypto")
# >>> cipher.encode("Hello world")
# "Btggj vjmgp"
#
# >>> cipher.decode("Fjedhc dn atidsn")
# "Kojima is genius"


class Cipher:
    def __init__(self, keyword):
        self.__keyword = keyword
        self.__alphabet = ["A", "B", "C", "D", "E", "F", "G", "H", "I", "J", "K", "L", "M", "N", "O", "P", "Q", "R",
                           "S", "T", "U", "V", "W", "X", "Y", "Z"]
        self.__key_alphabet = []

        for char in self.__keyword.upper():
            if char not in self.__key_alphabet:
                self.__key_alphabet.append(char)

        for char in self.__alphabet:
            if char not in self.__key_alphabet:
                self.__key_alphabet.append(char)

    def encode(self, input_encode_string):
        self.__input_encode_string = input_encode_string
        self.__encode_string = ""

        for char in self.__input_encode_string:
            if char.islower():
                i = self.__alphabet.index(char.upper())
                self.__encode_string += self.__key_alphabet[i].lower()

            elif char.isupper():
                i = self.__alphabet.index(char)
                self.__encode_string += self.__key_alphabet[i]
            else:
                self.__encode_string += char

        print(self.__encode_string)

    def decode(self, input_decode_string):
        self.__input_decode_string = input_decode_string
        self.__decode_string = ""

        for char in self.__input_decode_string:
            if char.islower():
                i = self.__key_alphabet.index(char.upper())
                self.__decode_string += self.__alphabet[i].lower()

            elif char.isupper():
                i = self.__key_alphabet.index(char)
                self.__decode_string += self.__alphabet[i]
            else:
                self.__decode_string += char

        print(self.__decode_string)

