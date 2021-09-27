# Task 6.5
# A singleton is a class that allows only a single instance of itself to be
# created and gives access to that created instance.
# Implement singleton logic inside your custom class using a method to initialize class instance.
# Example:
# >>> p = Sun.inst()
# >>> f = Sun.inst()
# >>> p is f
# True

class Sun:

    def __new__(cls):
        if hasattr(cls, 'instance'):
            return cls.instance
        else:
            cls.instance = super(Sun, cls).__new__(cls)
            return cls.instance

    def inst():
        return Sun()


# Test
# p = Sun.inst()
# f = Sun.inst()
# x = Sun.inst()
#
# print(p is f)
#
# print(p, id(p))
# print(f, id(f))
# print(x, id(x))

