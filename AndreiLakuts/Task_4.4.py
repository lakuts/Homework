# Task 4.4
# Implement a function split_by_index(s: str, indexes: List[int]) -> List[str]
# which splits the s string by indexes specified in indexes. Wrong indexes must be ignored.
# Examples:
# >>> split_by_index("pythoniscool,isn'tit?", [6, 8, 12, 13, 18])
# ["python", "is", "cool", ",", "isn't", "it?"]
#
# >>> split_by_index("no luck", [42])
# ["no luck"]

def split_by_index(input_string, index_list):
    """split_by_index(input_string: str, index_list[int]) -> list[str]
    Function splits string by indexes specified in index_list.
    Wrong indexes (index <= 0, and index >= len(input_string) are ignored."""

    output_list = []
    input_string_pointer = 0

    for index_list_pointer in index_list:
        if index_list_pointer <= 0:
            continue
        output_list.append(input_string[input_string_pointer:index_list_pointer])
        input_string_pointer = index_list_pointer
        if input_string_pointer >= len(input_string):
            break

    if input_string_pointer < len(input_string):
        output_list.append(input_string[input_string_pointer:])

    return output_list
