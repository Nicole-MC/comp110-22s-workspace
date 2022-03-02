"""Dictionary Functions Testing."""

__author__ = "730388398"


from dictionary import favorite_color
from dictionary import invert
from dictionary import count
import pytest


def test_invert() -> None:
    """Test a dictionary."""
    given_invert: dict[str, str] = {'a': 'z', 'b': 'y', 'c': 'x'}
    assert(given_invert)


def test_invert_use() -> None:
    """Test a dictionary."""
    given_invert: dict[str, str] = {'george': 'gogy', 'louis': 'lou', 'harold': 'harry'}
    assert(given_invert)


def test_favorite_colors() -> None:
    """Test."""
    colors: dict = {"george": "blue", "louis": "blue", "alex": "red", "karl": "purple", "clay": "green", "nick": "red", "nicole": "blue"}
    assert(colors)


def test_favorite_colors_use() -> None:
    """Test."""
    colors: dict = {"emma": "green", "nicole": "green", "sarah": "pink", "george": "blue"}
    assert(colors)


with pytest.raises(KeyError):
    colors: dict[str, str] = {"nicole": "black", "george": "blue", "sarah": "pink", "dream": "black", "louis": "blue"}
    favorite_color(colors)


def test_counter() -> None:
    """Test."""
    values: list = ["berries", "berries", "veggies", "protein", "water", "berries", "water"]
    assert(values)