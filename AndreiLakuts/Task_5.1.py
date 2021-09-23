# Task 5.1
# Open file data/unsorted_names.txt in data folder.
# Sort the names and write them to a new file called sorted_names.txt.
# Each name should start with a new line as in the following example:
# Adele
# Adrienne
# ...
# Willodean
# Xavier


def sort_file(unsorted_file_name, sorted_file_name = "sorted_names.txt"):
    """sort_file(unsorted_file_name: str, sorted_file_name: str):
    Function gets names of the input unsorted file and output sorted file
    (as default "sorted_names.txt").
    """

    # write data from input file to the list "names"
    with open(unsorted_file_name, 'r', encoding="utf-8") as file:
        names = file.read().splitlines()

    # sort list "names"
    names.sort()

    # write data from "names" to the output file
    with open(sorted_file_name, 'w+', encoding="utf-8") as file:
        for name in names:
            file.write(name + "\n")


sort_file("unsorted_names.txt")

