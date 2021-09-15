# ### Task 1.5
# Write a Python program to sort a dictionary by key.

# input a dictionary with integer-keys and string-values
# enter "exit" key to stop input
print("""Please enter the dictionary elements in integer-key, string-value format. 
To stop input enter "exit" in the key field :
""")
input_dict = {}
while True:
    key = input("enter key: ")
    if key == "exit":
        break
    value = input("enter value: ")
    input_dict[int(key)] = value

sorted_dict = {}
for key in sorted(input_dict):
    sorted_dict[key] = input_dict[key]

print(sorted_dict)
