# Task 7.2
# Implement context manager for opening and working with file,
# including handling exceptions with @contextmanager decorator.


from contextlib import contextmanager


@contextmanager
def open_file(file_name, method="r"):
    try:
        file = open(file_name, method)
        yield file
    except Exception as error:
        print(f"Exception: {error}")
    finally:
        file.close()


# Test

# with open_file('demo.txt', 'w') as file:
#     file.write("Hello -2! \n")
#
# with open_file('demo.txt', 'r') as file:
#     file.write("Hello -3! \n")
#
# with open_file('demo.txt', 'a') as file:
#     file.write("Hello -4! \n")
