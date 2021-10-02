# Task 7.3
# Implement decorator with context manager support for writing
# execution time to log-file. See contextlib module.

import time
from contextlib import ContextDecorator


class log_timer(ContextDecorator):
    def __init__(self, log_file="log_timer.log", method="a"):
        self.log_file = log_file
        self.method = method

    def __enter__(self):
        self.start = time.time()
        return self

    def __exit__(self, *exc):
        self.finish = time.time()
        with open(self.log_file, self.method) as log_file:
            log_file.write(f"Execution time: {self.finish - self.start} seconds \n")
        return False


@log_timer()
def one_sllep(seconds=5):
    time.sleep(seconds)



# Test
# def two_sllep(seconds=5):
#     time.sleep(seconds)
#
#
# one_sllep()
#
# with log_timer():
#     two_sllep()
