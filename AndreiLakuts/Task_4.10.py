# Implement a function that takes a number as an argument and
# returns a dictionary, where the key is a number and
# the value is the square of that number.
# print(generate_squares(5))
# >>> {1: 1, 2: 4, 3: 9, 4: 16, 5: 25}

def generate_squares(number):
    """generate_squares(number: int)
    function gets a number as an argument and
    returns a dictionary, where the key is a number and
    the value is the square of that number."""

    output_dictionary = {n: n ** 2 for n in range(1, number + 1)}

    return output_dictionary

