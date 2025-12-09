"""Tests for Character class."""

import pytest
from unittest.mock import patch
from dndgame.character import Character


def test_character_creation() -> None:
    """Test basic initialization."""
    char = Character("Test", "Human", 10)
    assert char.name == "Test"
    assert char.race == "Human"
    assert char.level == 1


def test_invalid_race() -> None:
    """Test invalid race raises error."""
    with pytest.raises(ValueError):
        Character("Bad", "Alien", 10)


def test_get_modifier() -> None:
    """Test ability modifier calculation."""
    char = Character("Test", "Human", 10)
    char.stats["STR"] = 10
    assert char.get_modifier("STR") == 0

    char.stats["STR"] = 16
    assert char.get_modifier("STR") == 3

    char.stats["STR"] = 8
    assert char.get_modifier("STR") == -1


def test_roll_stats() -> None:
    """Test stat rolling."""
    char = Character("Test", "Human", 10)
    with patch("dndgame.character.roll", return_value=12):
        char.roll_stats()

    for stat in ["STR", "DEX", "CON", "INT", "WIS", "CHA"]:
        assert char.stats[stat] == 12
    assert char.max_hp == 11


def test_racial_bonuses_human() -> None:
    """Test Human bonuses."""
    char = Character("Test", "Human", 10)
    char.stats = {"STR": 10, "DEX": 10, "CON": 10, "INT": 10, "WIS": 10, "CHA": 10}
    char.max_hp = 10
    char.hp = 10
    char.apply_racial_bonuses()

    for stat in char.stats.values():
        assert stat == 11


def test_racial_bonuses_elf() -> None:
    """Test Elf bonuses."""
    char = Character("Test", "Elf", 10)
    char.stats = {"STR": 10, "DEX": 10, "CON": 10, "INT": 10, "WIS": 10, "CHA": 10}
    char.max_hp = 10
    char.hp = 10
    char.apply_racial_bonuses()

    assert char.stats["DEX"] == 12


def test_is_alive() -> None:
    """Test is_alive method."""
    char = Character("Test", "Human", 10)
    char.hp = 5
    assert char.is_alive() is True

    char.hp = 0
    assert char.is_alive() is False


def test_take_damage() -> None:
    """Test taking damage."""
    char = Character("Test", "Human", 10)
    char.hp = 10
    char.take_damage(3)
    assert char.hp == 7

    char.take_damage(20)
    assert char.hp == 0


def test_heal() -> None:
    """Test healing."""
    char = Character("Test", "Human", 10)
    char.hp = 5
    char.max_hp = 10

    char.heal(3)
    assert char.hp == 8

    char.heal(10)
    assert char.hp == 10
