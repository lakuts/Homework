# ### Task 1.7
# Write a Python program to convert a given tuple of positive integers into an integer.
# Examples:
# ```
# Input: (1, 2, 3, 4)
# Output: 1234

# input a tuple
print("""Please, enter a space separated sequence of numbers, 
for example 1 2 3 4 :""")
input_tuple = tuple(input().split())

# convert a tuple to string
string_input_tuple = ""
for i in input_tuple:
    string_input_tuple += str(i)

convert_to_integer = int(string_input_tuple)

print(convert_to_integer)