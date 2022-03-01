"""Dictionary Functions."""


__author__ = "730388398"


def invert(given_invert: dict) -> dict[str, str]: 
    """Given the input of keys and their values, the output needs to swap them."""
    input_swap = {}
    for key, value in given_invert: 
        input_swap.values = key
        input_swap.keys = value
    return input_swap


def favorite_color(colors: dict[str, str]) -> str: 
    """Input the users' names and their favorite colors to see the most common favorite color."""
    color_counter_dict = {}
    for key, value in colors.items():
        if value not in color_counter_dict:
            color_counter_dict[value] = 0
        else:
            color_counter_dict[value] += 1
    return max(color_counter_dict)


# def count(values: list[str]) -> dict[str, int]: 
#     """Input a list of words to see how many times each one is inputed."""
