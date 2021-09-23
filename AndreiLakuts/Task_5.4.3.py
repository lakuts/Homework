# Task 5.4
# Look through file modules/legb.py.
# 3.	Modify ONE LINE in inner_function to make it print variable 'a' form enclosing function.


a = "I am global variable!"


def enclosing_funcion():
    a = "I am variable from enclosed function!"

    def inner_function():
        # replaced "a = "I am local variable!"" with "nonlocal a"
        nonlocal a
        print(a)

    # call inner_function() inside enclosing_funcion()
    inner_function()


enclosing_funcion()
