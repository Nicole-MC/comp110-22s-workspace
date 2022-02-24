"""Test Utils Functions.""" 

__author__ = 730388398


from utils import only_evens
from utils import sub
from utils import concat


def test_only_evens() -> None:
    """Test an empty list for only_evens."""
    numbers: list[int] = []
    assert only_evens(numbers)


def test_only_evens_use() -> None: 
    """Test list of numbers."""
    numbers: list[int] = [-2, -1, 0, 1, 2, 3, 4, 5, 6]
    assert only_evens(numbers)


def test_only_evens_use2() -> None:
    """Test a list of numbers that have negatives."""
    numbers: list[int] = [-4, -9, 2, 12]
    assert only_evens(numbers)


def test_sub() -> None:
    """Test an empty list."""
    sub_list: list[int] = []
    first: int = 0
    last: int = 0
    assert sub(sub_list, first, last) == []
 

def test_sub_use() -> None:
    """Test list with a negative starting number and an index greater than the length."""
    sub_list: list[int] = [-2, -1, 0, 2, 3, 4, 5, 6]
    first: int = 1
    last: int = 20
    assert sub(sub_list, first, last)


def test_sub_use1() -> None:
    """Test list with a negative first index.""" 
    sub_list: list[int] = [-1, -3, -6, 8, 10]
    first: int = 1
    last: int = 5
    assert sub(sub_list, first, last) 


def test_sub_use2() -> None:
    """Test empty list for sub.""" 
    sub_list: list[int] = []
    first: int = 0
    last: int = 0
    assert sub(sub_list, first, last)


def test_concat() -> None: 
    """Test empty lists for concat."""
    evens_list: list[int] = []
    subs_list: list[int] = []
    assert concat(evens_list, subs_list)


def test_concat_use1() -> None: 
    """Test of same length and ints."""
    evens_list: list[int] = [-2, -1, 0, 1, 2, 3]
    subs_list: list[int] = [-2, -1, 0, 2, 3]
    assert concat(evens_list, subs_list)


def test_concat_use2() -> None: 
    """Test 2 lists on the same length with different ints."""
    evens_list: list[int] = [1, 2, 4, 6]
    subs_list: list[int] = [0, 3, 5, 7]
    assert concat(evens_list, subs_list)