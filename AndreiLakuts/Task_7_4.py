# Task 7.4
# Implement decorator for supressing exceptions.
# If exception not occure write log to console.


# there weren't exceptions during the execution of the function


def decorator_ignore_exceptions(input_function):
    def wrapper(*args, **kwargs):
        result = None
        try:
            result = input_function(*args, **kwargs)
            print("There weren't exceptions during the execution of the function")
        except:
            pass
        return result

    return wrapper


# Test
# @decorator_ignore_exceptions
# def f(a, b):
#     print(a + b)
#     return a / b
#
#
# print(f(10, 2))
# print(f(10, 0))
