# Task 4.2
# Write a function that check whether a string is a palindrome or not.
# Usage of any reversing functions is prohibited.

def is_palindrome(input_string):
    """Function checks if the string is a palindrome.
    It returns True if it is and False if it isn't."""

    left_index = 0
    right_index = len(input_string) - 1
    palindrome = True

    while left_index < right_index:
        if input_string[left_index] != input_string[right_index]:
            return False
        left_index += 1
        right_index -= 1

    return True
