'''
Remove all non numbers from a string

convert the string to an integer, and multiply it by the length of original string
'''


def multiply_by_len(original_str, processed_int):
    return processed_int * len(original_str)

def process_string(the_string):
    keep_list = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
    new_str = ''
    for char in the_string:
        if char in keep_list:
            new_str += char

    return int(new_str)