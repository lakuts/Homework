# Task 4.3
# Implement a function which works the same as str.split method
# (without using str.split itself, ofcourse).

def string_split(input_string, delimiter=" ", max_split=None):
    """string_split(input_string: str, delimiter: str, max_split: int >= 0) -> list[str]
    Function converts a string into a list where items separated by "delimiter" (as defauld " ").
    Delimiter can be an empty string "".
    When max_split is specified, the list will contain the specified number of elements plus one."""

    output_list = []

    if max_split == None or max_split > len(input_string):
        max_split = len(input_string)

    # if max_split == 0 or input_string is empty or one char:
    if max_split == 0 or len(input_string) <= 1:
        output_list.append(input_string)
        return output_list

    # if delimiter is empty string:
    if delimiter == "":
        for i in range(max_split):
            output_list.append(input_string[i])
            pointer = i
        output_list.append(input_string[pointer + 1:])
        return output_list

    # other cases
    pointer = 0
    list_item_index = 0
    step = len(delimiter)
    while delimiter in input_string[pointer:] and list_item_index < max_split:
        delimiter_index = input_string.index(delimiter, pointer)
        output_list.append(input_string[pointer:delimiter_index])
        pointer += delimiter_index - pointer + step
        list_item_index +=1
    output_list.append(input_string[pointer:])
    return output_list

