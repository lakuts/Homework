# ### Task 1.4
# Create a program that asks the user for a number and then prints out a list of all the
# [divisors](https://en.wikipedia.org/wiki/Divisor) of that number.
# Examples:
# ```
# Input: 60
# Output: {1, 2, 3, 4, 5, 6, 10, 12, 15, 20, 30, 60}

number = int(input("Please, enter a number: "))

divisors = []

i = 1
while i ** 2 <= number:
    if number % i == 0:
        divisors.append(i)
        if i != number // i:
            divisors.append(number // i)
    i += 1

divisors.sort()
print(divisors)
