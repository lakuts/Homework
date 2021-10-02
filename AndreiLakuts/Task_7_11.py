# Task 7.11
# Implement a generator which will geterate Fibonacci numbers endlessly.
# Example:
# gen = endless_fib_generator()
# while True:
#     print(next(gen))
# >>> 1 1 2 3 5 8 13 ...

import time


def endless_fib_generator():
    value_minus_two, value_minus_one = 0, 1

    while True:
        value = value_minus_two + value_minus_one
        yield value_minus_one
        value_minus_two, value_minus_one = value_minus_one, value


# Test
# gen = endless_fib_generator()
# while True:
#     time.sleep(0.1)
#     print(next(gen), end=" ")
