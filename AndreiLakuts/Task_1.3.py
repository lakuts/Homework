# ### Task 1.3
# Write a Python program that accepts a comma separated sequence of words as input
# and prints the unique words in sorted form.
# Examples:
# ```
# Input: ['red', 'white', 'black', 'red', 'green', 'black']
# Output: ['black', 'green', 'red', 'white', 'red']

print("""Please, enter a comma separated sequence of words, 
for example red,blue,white,red,white :""")
input_list = input().split(',')

sorted_unique_list = []

for word in input_list:
    if word not in sorted_unique_list:
        sorted_unique_list.append(word)

sorted_unique_list.sort()
print(sorted_unique_list)
