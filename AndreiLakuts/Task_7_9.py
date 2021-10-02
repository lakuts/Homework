# Task 7.9
# Implement an iterator class EvenRange, which accepts start and end of the interval
# as an init arguments and gives only even numbers during iteration.
# If user tries to iterate after it gave all possible numbers Out of numbers! should be printed.
# Note: Do not use function range() at all Example:
# er1 = EvenRange(7,11)
# next(er1)
# >>> 8
# next(er1)
# >>> 10
# next(er1)
# >>> "Out of numbers!"
# next(er1)
# >>> "Out of numbers!"
# er2 = EvenRange(3, 14)
# for number in er2:
#     print(number)
# >>> 4 6 8 10 12 "Out of numbers!"

class EvenRange:
    def __init__(self, start, finish):
        self.start = start + int(start % 2)
        self.finish = finish
        self.step = self.start

    def __iter__(self):
        return self

    def __next__(self):
        self.rez = self.step
        if self.rez < self.finish:
            self.step += 2
            return self.rez
        if self.rez >= self.finish:
            print("Out of numbers!")
            raise StopIteration


#Test
# er2 = EvenRange(1, 15)
# for number in er2:
#     print(number, end=" ")