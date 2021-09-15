# ### Task 1.2
# Write a Python program to count the number of characters (character frequency)
# in a string (ignore case of letters).
# Examples:
# ```
# Input: 'Oh, it is python'
# Output: {',': 1, ' ': 3, 'o': 2, 'h': 2, 'i': 2, 't': 2, 's': 1, 'p': 1, 'y': 1, 'n': 1}

# input a string and make it lower
input_string = input("Please, enter a string: ").lower()

# create an empty dictionary
char_counter = {}

for char in input_string:
    if char in char_counter:
        char_counter[char] += 1
    else:
        char_counter[char] = 1

print(char_counter)