# Task 4.1
# Implement a function which receives a string
# and replaces all " symbols with ' and vise versa.

def replace_quotes(input_string):
    """Function receives a string and replaces
    all " symbols with ' and vise versa"""

    output_string = ""

    for char in input_string:
        if char == '"':
            output_string += "'"
        elif char == "'":
            output_string += '"'
        else:
            output_string += char

    return output_string
