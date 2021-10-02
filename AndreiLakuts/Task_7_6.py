# Task 7.6
# Create console program for proving Goldbach's conjecture.
# Program accepts number for input and print result.
# For pressing 'q' program succesfully close.
# Use function from Task 7.5 for validating input,
# handle all exceptions and print user friendly output.


from Task_7_5 import is_even_and_more_than_two


def isNumberPrime(n):
    for i in range(2, n):
        if n % i == 0:
            return False
    return True


def find_goldbach_numbers(number):
    if number == 4:
        print("2 + 2 = 4")

    for i in range(3, number):
        if isNumberPrime(i):
            for l in range(i, number):
                if isNumberPrime(l) and number == (i + l):
                    print(f"{i} + {l} = {number}")


while True:
    number = input("Please, enter an integer number or 'q' for exit: ")
    if number == "q":
        print("Exit")
        break
    else:
        number = int(number)
        try:
            is_even_and_more_than_two(number)
        except Exception as error:
            print(f"Exception: {error}")
        else:
            find_goldbach_numbers(number)


