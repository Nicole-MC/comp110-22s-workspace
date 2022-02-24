"""Test Utils Functions.""" 

__author__ = 730388398

from exercises.ex05.utils import only_evens, sub, concat


def test_only_evens_edge() -> None:
    numbers: list[int] = []
    assert only_evens(numbers) == 4


def test_only_evens_use() -> None: 
    numbers: list[int] = [-2, -1, 0, 1, 2, 3, 4, 5, 6]
    assert only_evens(numbers)


def test_only_evens_use2() -> None:
    numbers: list[int] = [-4, -9, 2, -12]
    assert only_evens(numbers) == [] 


def test_sub_edge() -> None:
    sub_list: list[int] = []
    first: int = 1
    last: int = 3
    assert sub(sub_list, first, last) == [10, 20, 30]
 

def test_sub_use() -> None:
    sub_list: list[int] = [-2, -1, 0, 2, 3, 4, 5, 6]
    first: int = 1
    last: int = 7
    assert sub(sub_list, first, last)


def test_sub_use1() -> None: 
    sub_list: list[int] = [-1, 3, 6, 8, 10]
    first: int = -1
    last: int = 7
    assert sub(sub_list, first, last) 


def test_sub_use2() -> None: 
    sub_list: list[int] = []
    first: int = 0
    last: int = 7
    assert sub(sub_list, first, last)


def test_concat_edge() -> None: 
    evens_list: list[int] = []
    subs_list: list[int] = []
    assert concat(evens_list, subs_list)


def test_concat_use1() -> None: 
    evens_list: list[int] = [-2, -1, 0, 1, 2, 3, 4, 5, 6]
    subs_list: list[int] = [-2, -1, 0, 2, 3, 4, 5, 8]
    assert concat(evens_list, subs_list)


def test_concat_use2() -> None: 
    evens_list: list[int] = [-2, -1, 0, 1, 2, 3, 4]
    subs_list: list[int] = [-2, -1, 0, 2, 3, 4, 5, 6, 28]
    assert concat(evens_list, subs_list)