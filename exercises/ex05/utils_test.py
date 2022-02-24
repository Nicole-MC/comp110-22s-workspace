"""Test Utils Functions.""" 


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


def test_concat() -> None: 
    evens_list: list[int] = [-2, -1, 0, 1, 2, 3, 4, 5, 6]
    subs_list: list[int] = [-2, -1, 0, 2, 3, 4, 5, 6]
    assert concat(evens_list, subs_list)