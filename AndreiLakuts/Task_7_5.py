# Task 7.5
# Implement function for check that number is even and is greater than 2.
# Throw different exceptions for this errors.
# Custom exceptions must be derived from custom base exception(not Base Exception class).


class BaseNumberCheckException(Exception):
    """Base Class"""


class NumberIsNotEven(BaseNumberCheckException):
    """ Number is not even"""

    def __str__(self):
        return "The number is not even"


class NumberIsNotGreaterThanTwo(BaseNumberCheckException):
    """ Number is not greater than two"""

    def __str__(self):
        return "The number is not greater than 2"


def is_even_and_more_than_two(number):
    """Boolean.
    Function checks number is even and is greater than 2."""
    if (number % 2) != 0:
        raise NumberIsNotEven
    if number <= 2:
        raise NumberIsNotGreaterThanTwo

    return True

# Test
# print(is_even_and_more_than_two(8))
# # print(is_even_and_more_than_two(3))
# print(is_even_and_more_than_two(-8))
