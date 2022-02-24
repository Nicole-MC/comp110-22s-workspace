"""Test Utils Functions.""" 


from exercises.ex05.utils import only_evens


def test_only_evens_edge() -> None:
    numbers: list[int] = []
    assert only_evens(numbers) == 4


def test_only_evens_use() -> None:
    numbers: list[int] = [0, 1, 2, 3]
    assert only_evens(numbers)


def test_only_evens_use2() -> None:
    numbers: list[int] = [4, 9, 2, 10]
    assert only_evens(numbers)