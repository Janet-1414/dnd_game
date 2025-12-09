from unittest.mock import patch
from dndgame.dice import roll, roll_with_advantage, roll_with_disadvantage


def test_roll() -> None:
    """Test basic dice rolling with mocked random values."""
    with patch("random.randint", return_value=4):
        result = roll(6, 1)
        assert result == 4

    with patch("random.randint", return_value=3):
        result = roll(20, 2)
        assert result == 6

    with patch("random.randint", side_effect=[1, 2]):
        result = roll(6, 1)
        assert result == 1

        result = roll(20, 1)
        assert result == 2


def test_roll_with_advantage() -> None:
    """Test advantage rolls (take highest of two)."""
    with patch("random.randint", side_effect=[3, 5]):
        result = roll_with_advantage(20)
        assert result == 5

    with patch("random.randint", side_effect=[6, 2]):
        result = roll_with_advantage(6)
        assert result == 6


def test_roll_with_disadvantage() -> None:
    """Test disadvantage rolls (take lowest of two)."""
    with patch("random.randint", side_effect=[3, 5]):
        result = roll_with_disadvantage(20)
        assert result == 3

    with patch("random.randint", side_effect=[6, 2]):
        result = roll_with_disadvantage(6)
        assert result == 2
