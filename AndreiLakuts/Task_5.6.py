# Task 5.6
# Implement a decorator call_once which runs a function or
# method once and caches the result. All consecutive calls to this
# function should return cached result no matter the arguments.
# @call_once
# def sum_of_numbers(a, b):
#     return a + b
#
# print(sum_of_numbers(13, 42))
# >>> 55
# print(sum_of_numbers(999, 100))
# >>> 55
# print(sum_of_numbers(134, 412))
# >>> 55
# print(sum_of_numbers(856, 232))
# >>> 55


def call_once(fn):
    """decorator for function sum_of_numbers():"""
    cash_result = None

    def wrapper(*args):
        nonlocal cash_result
        if cash_result is None:
            cash_result = fn(*args)
            return cash_result
        else:
            return cash_result

    return wrapper


@call_once
def sum_of_numbers(a, b):
    return a + b

