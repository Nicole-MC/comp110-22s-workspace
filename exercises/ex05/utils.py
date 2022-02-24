"""Unit List Testing Practice."""

__author__ = 730388398


def only_evens(numbers: list[int]) -> list[int]:
    """From an input of a list of number, return the even numbers."""
    even: list[int] = []
    i: int = 0
    while i < len(numbers): 
        if numbers[i] % 2 == 0:
            even.append(numbers[i])
            i += 1
    return even


def sub(sub_list: list[int], first: int, last: int) -> list[int]:
    """later."""
    new_list = list[int] = []
    i: int = first
    while i < last:
        new_list.append(sub_list[i])
    return new_list


def concat(evens_list: list[int], subs_list: list[int]) -> list[int]: 
    """."""
    output: list[int] = []
    i: int = 0
    while i < len(evens_list):
        output.append(evens_list[i])
        i += 1
    while i < len(subs_list):
        output.append(subs_list[i])
        i += 1
    return output