"""Dictionary Functions Testing."""

__author__ = "730388398"


from dictionary import favorite_color
from dictionary import invert
from dictionary import count
import pytest


def test_invert() -> None:
    """Test a dictionary."""
    given_invert: dict[str, str] = {'a': 'z', 'b': 'y', 'c': 'x'}
    assert(invert.given_invert)


def test_invert_use() -> None:
    """Test a dictionary."""
    given_invert: dict[str, str] = {'george': 'gogy', 'louis': 'lou', 'harold': 'harry'}
    assert(invert.given_invert)


def test_favorite_colors() -> None:
    """Test."""
    colors: dict = {"george": "blue", "louis": "blue", "alex": "red", "karl": "purple", "clay": "green", "nick": "red", "nicole": "blue"}
    assert(favorite_color.colors)


def test_favorite_colors_use() -> None:
    """Test."""
    colors: dict = {"emma": "green", "nicole": "green", "sarah": "pink", "george": "blue"}
    assert(favorite_color.colors)


def test_favorite_colors_tie() -> None:
    """Test colors for a tie."""
    colors: dict = {"emma": "green", "nicole": "green", "sarah": "pink", "george": "blue", "clay": "blue"}
    assert(favorite_color.colors)


with pytest.raises(KeyError):
    colors: dict[str, str] = {"nicole": "black", "george": "blue", "sarah": "pink", "dream": "black", "louis": "blue"}
    favorite_color(colors)


def test_counter() -> None:
    """Test for list."""
    values: list = ["berries", "berries", "veggies", "protein", "water", "berries", "water"]
    assert(count.values)


def test_counter_small() -> None:
    """Test for small values."""
    values: list = ["a", "b", "a", "c", "d"]
    assert(count.values)


def test_counter_large() -> None:
    """Test for large values."""
    values: list = ["z", "a", "y", "b", "x", "c", "q", "z", "z", "z", "z", "z", "a", "q", "q", "x"]
    assert(count.values)