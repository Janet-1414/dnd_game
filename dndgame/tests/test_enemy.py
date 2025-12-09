"""Tests for Enemy class."""

import pytest
from dndgame.enemy import Enemy


def test_enemy_creation() -> None:
    """Test creating enemy from template."""
    goblin = Enemy("Goblin")
    assert goblin.name == "Goblin"
    assert goblin.enemy_type == "Goblin"
    assert goblin.max_hp == 7
    assert goblin.armor_class == 13


def test_enemy_custom_name() -> None:
    """Test enemy with custom name."""
    goblin = Enemy("Goblin", "Grok")
    assert goblin.name == "Grok"
    assert goblin.enemy_type == "Goblin"


def test_invalid_enemy_type() -> None:
    """Test invalid enemy type."""
    with pytest.raises(ValueError):
        Enemy("Dragon")


def test_enemy_stats() -> None:
    """Test enemy stats loaded correctly."""
    orc = Enemy("Orc")
    assert orc.stats["STR"] == 16
    assert orc.stats["CON"] == 16


def test_enemy_modifier() -> None:
    """Test enemy ability modifiers."""
    goblin = Enemy("Goblin")
    assert goblin.get_modifier("DEX") == 2
    assert goblin.get_modifier("STR") == -1


def test_enemy_alive() -> None:
    """Test enemy is_alive."""
    goblin = Enemy("Goblin")
    assert goblin.is_alive() is True
    
    goblin.take_damage(100)
    assert goblin.is_alive() is False