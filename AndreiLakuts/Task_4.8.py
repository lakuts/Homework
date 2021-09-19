# Task 4.8
# Implement a function get_pairs(lst: List) -> List[Tuple]
# which returns a list of tuples containing pairs of elements.
# Pairs should be formed as in the example.
# If there is only one element in the list return None instead.
# Example:
# >>> get_pairs([1, 2, 3, 8, 9])
# [(1, 2), (2, 3), (3, 8), (8, 9)]
#
# >>> get_pairs(['need', 'to', 'sleep', 'more'])
# [('need', 'to'), ('to', 'sleep'), ('sleep', 'more')]
#
# >>> get_pairs([1])
# None

def get_pairs(input_list):
    """get_pairs(input_list: list) -> list[tuple]
    Function returns a list of tuples containing adjacent pairs of elements."""

    if len(input_list) <= 1:
        return None

    output_list = []
    for i in range(len(input_list) - 1):
        output_list.append((input_list[i], input_list[i + 1]))

    return output_list
