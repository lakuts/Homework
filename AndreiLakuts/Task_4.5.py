# Task 4.5
# Implement a function get_digits(num: int) -> Tuple[int]
# which returns a tuple of a given integer's digits. Example:
# >>> split_by_index(87178291199)
# (8, 7, 1, 7, 8, 2, 9, 1, 1, 9, 9)

def get_digits(num):
    """Function returns a tuple of a given integer's digits.
    Example: split_by_index(87178291199)
    (8, 7, 1, 7, 8, 2, 9, 1, 1, 9, 9)
    """
    output_tuple = tuple()
    while num >= 1:
        add_to_output_tuple = num % 10
        output_tuple = (add_to_output_tuple,) + output_tuple
        num = num // 10

    return output_tuple
