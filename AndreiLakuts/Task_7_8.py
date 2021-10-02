# Task 7.8
# Implement your custom iterator class called MySquareIterator
# which gives squares of elements of collection it iterates through.
# Example:
# lst = [1, 2, 3, 4, 5]
# itr = MySquareIterator(lst)
# for item in itr:
#     print(item)
# >>> 1 4 9 16 25

class MySquareIterator:
    def __init__(self, input_object):
        self.input_object = input_object

    def __iter__(self):
        for i in self.input_object:
            yield i ** 2


# Test
# lst = [1, 2, 3, 4, 5]
# lst = (1, 2.87, -3.95, 4000, 5)
# lst = {1, 2, 3, 4, 5}
# itr = MySquareIterator(lst)
# for item in itr:
#     print(item, end=" ")
