"""Set of funcions for PyNEng."""


def int_in_list(a_list):
    """Convert a_list elements to int type."""
    for position, elem in enumerate(a_list):
        a_list[position] = int(elem)
    return a_list


def split_this(long_string):
    """Return both strip and split methods of string."""
    return long_string.strip().split()
