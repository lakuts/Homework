# Task 5.4
# Look through file modules/legb.py.
# 1.	Find a way to call inner_function without moving it from inside of enclosed_function.


a = "I am global variable!"


def enclosing_funcion():
    a = "I am variable from enclosed function!"

    def inner_function():
        a = "I am local variable!"
        print(a)

    # call inner_function() inside enclosing_funcion()
    inner_function()


enclosing_funcion()
