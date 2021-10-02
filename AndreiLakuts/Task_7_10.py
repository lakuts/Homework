# Task 7.10
# Implement a generator which will generate odd numbers endlessly. Example:
# gen = endless_generator()
# while True:
#     print(next(gen))
# >>> 1 3 5 7 ... 128736187263 128736187265 ...

import time

def endless_generator():
    i = 1
    while True:
        yield i
        i += 2


#Test
# gen = endless_generator()
# while True:
#     time.sleep(0.1)
#     print(next(gen), end = " ")