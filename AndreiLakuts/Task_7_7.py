# Task 7.7
# Implement your custom collection called MyNumberCollection.
# It should be able to contain only numbers. It should NOT inherit any other collections.
# If user tries to add a string or any non numerical object there, exception TypeError should be raised.
# Method init sholud be able to take either start,end,step arguments,
# where start - first number of collection, end - last number of collection or
# some ordered iterable collection (see the example). Implement following functionality:
# •	appending new element to the end of collection
# •	concatenating collections together using +
# •	when element is addressed by index(using []), user should get square of the addressed element.
# •	when iterated using cycle for, elements should be given normally
# •	user should be able to print whole collection as if it was list. Example:
# col1 = MyNumberCollection(0, 5, 2)
# print(col1)
# >>> [0, 2, 4, 5]
# col2 = MyNumberCollection((1,2,3,4,5))
# print(col2)
# >>> [1, 2, 3, 4, 5]
# col3 = MyNumberCollection((1,2,3,"4",5))
# >>> TypeError: MyNumberCollection supports only numbers!
# col1.append(7)
# print(col1)
# >>> [0, 2, 4, 5, 7]
# col2.append("string")
# >>> TypeError: 'string' - object is not a number!
# print(col1 + col2)
# >>> [0, 2, 4, 5, 7, 1, 2, 3, 4, 5]
# print(col1)
# >>> [0, 2, 4, 5, 7]
# print(col2)
# >>> [1, 2, 3, 4, 5]
# print(col2[4])
# >>> 25
# for item in col1:
#     print(item)
# >>> 0 2 4 5 7

class MyNumberCollection:
    def __init__(self, start=None, end=None, step=None):
        self.start = start
        self.end = end
        self.step = step
        self.collection = []

        if self.step:
            self.collection = [i for i in range(self.start, self.end, self.step)]
            self.collection.append(self.end)
        else:
            try:
                # check that all elements are numbers using "sum"
                sum(self.start)
            except Exception:
                print(f"TypeError: MyNumberCollection supports only numbers!")
            else:
                self.collection = [i for i in self.start]

    def __str__(self):
        return str(self.collection)

    def __add__(self, other):
        return self.collection + other.collection

    def append(self, value):
        try:
            # check that all elements are numbers using "sum"
            sum(value, 1)
        except Exception:
            print(f"TypeError: {value} - object is not a number!")
        else:
            self.collection.append(value)

    def __iter__(self):
        self.iteration_index = -1
        return self

    def __next__(self):
        self.iteration_index += 1
        if self.iteration_index < len(self.collection):
            return self.collection[self.iteration_index]
        else:
            raise StopIteration

    def __getitem__(self, index):
        return self.collection[index] ** 2


# Test
# col1 = MyNumberCollection(0, 5, 2)
# print(col1)
#
# col2 = MyNumberCollection((1, 2, 3, 4, 5))
#
# col3 = MyNumberCollection((1, 2, 3, "4", 5))
# print(col3)
# print(col3.start)
# print(col3.step)
# print(col3.end)
#
# col1.append(7)
# print(col1)
#
# col2.append("string")
# print(col2)
#
# col4 = MyNumberCollection([1, 2, 3, 4, 5])
# print(col4)
#
# print(col1 + col2)
# print(col1)
# print(col2)
#
# print(col2[4])
#
# col5 = col1 + col2
# print(col5)
#
# for item in col5:
#     print(item, end=" ")
