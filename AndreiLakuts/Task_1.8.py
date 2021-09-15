# ### Task 1.8
# Write a program which makes a pretty print of a part of the multiplication table.
# Examples:
# ```
# Input:
# a = 2
# b = 4
# c = 3
# d = 7
#
# Output:
# 	3	4	5	6	7
# 2	6	8	10	12	14
# 3	9	12	15	18	21
# 4	12	16	20	24	28

a = int(input("Please, enter a: "))
b = int(input("Please, enter b: "))
c = int(input("Please, enter c: "))
d = int(input("Please, enter d: "))

# print the top line
print(end = "\t")
for i in range(c, d + 1):
    print(i, end = "\t")
print()

for i in range(a, b + 1):
    print(i, end = "\t")             # print the left column
    for j in range(c, d + 1):
        print(i * j, end = "\t")
    print()
