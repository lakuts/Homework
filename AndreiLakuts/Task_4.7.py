# Task 4.7
# Implement a function foo(List[int]) -> List[int]
# which, given a list of integers, return a new list
# such that each element at index i of the new list is
# the product of all the numbers in the original array except the one at i.
# Example:
# >>> foo([1, 2, 3, 4, 5])
# [120, 60, 40, 30, 24]
#
# >>> foo([3, 2, 1])
# [2, 3, 6]

def foo(input_list):
    """ foo(input_list[int]) -> output_list[int]
    Function returns a list such that each element at
    index i of the new list is the product of all the numbers
    in the original list except the one at i."""

    output_list = []
    product = 1
    for number in input_list:
        product *= number

    for i in range(len(input_list)):
        output_list.append(int(product / input_list[i]))

    return output_list
