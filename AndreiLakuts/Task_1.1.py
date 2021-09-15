# ### Task 1.1
# Write a Python program to calculate the length of a string
# without using the `len` function.

string = input("Please, enter a string: ")
string_length = 0
for char in string:
    string_length += 1
print("String length is:", string_length)
