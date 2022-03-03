"""Dictionary Functions."""


__author__ = "730388398"


def invert(given_invert: dict[str, str]) -> dict[str, str]: 
    """Given the input of keys and their values, the output needs to swap them."""
    input_swap: dict[str, str] = {}
    for key in given_invert: 
        new_key = given_invert[key]
        if new_key in input_swap:
            raise KeyError("error")
        else:
            input_swap[given_invert[key]] = key
    return input_swap


def favorite_color(colors: dict[str, str]) -> str: 
    """Input the users' names and their favorite colors to see the most common favorite color."""
    if colors == dict():
        return 'Your dictionary is empty!'
    result: dict[str, int] = {}
    counter: int = 0
    counter_color: str = ""
    for key in colors:
        if colors[key] in result:
            result[colors[key]] += 1
        else:
            result[colors[key]] = 1
    for key in result:
        if result[key] > counter:
            counter_color = key
            counter = result[key]
    return counter_color


def count(values: list[str]) -> dict[str, int]: 
    """Input a list of words to see how many times each one is inputed."""
    counter_dict: dict[str, int] = dict()
    for value in values:
        if value not in counter_dict:
            counter_dict[value] = 1
        else:
            counter_dict[value] += 1
    return counter_dict