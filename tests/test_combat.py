"""Tests for Combat class."""

import pytest
from unittest.mock import patch
from dndgame.combat import Combat
from dndgame.character import Character
from dndgame.enemy import Enemy


@pytest.fixture
def player():
    """Create test player."""
    char = Character("Hero", "Human", 10)
    char.stats = {"STR": 14, "DEX": 12, "CON": 14, "INT": 10, "WIS": 10, "CHA": 10}
    char.hp = 15
    char.max_hp = 15
    return char


@pytest.fixture
def enemy():
    """Create test enemy."""
    return Enemy("Goblin")


@pytest.fixture
def combat(player, enemy):
    """Create combat instance."""
    return Combat(player, enemy)


def test_combat_init(combat, player, enemy):
    """Test combat initialization."""
    assert combat.player == player
    assert combat.enemy == enemy
    assert combat.round == 0


def test_roll_initiative_player_first(combat):
    """Test initiative when player wins."""
    with patch("dndgame.dice.roll", side_effect=[15, 10]):
        order = combat.roll_initiative()
    assert order[0] == combat.player


def test_roll_initiative_enemy_first(combat):
    """Test initiative when enemy wins."""
    with patch("dndgame.dice.roll", side_effect=[8, 12]):
        order = combat.roll_initiative()
    assert order[0] == combat.enemy


def test_attack_hit(combat, player, enemy):
    """Test successful attack."""
    initial_hp = enemy.hp
    with patch("dndgame.dice.roll", side_effect=[20, 5]):
        damage = combat.attack(player, enemy)
    assert damage > 0
    assert enemy.hp < initial_hp


def test_attack_miss(combat, player, enemy):
    """Test missed attack."""
    initial_hp = enemy.hp
    with patch("dndgame.dice.roll", return_value=1):
        damage = combat.attack(player, enemy)
    assert damage == 0
    assert enemy.hp == initial_hp


def test_execute_round(combat):
    """Test round execution."""
    combat.initiative_order = [combat.player, combat.enemy]
    with patch("dndgame.dice.roll", side_effect=[15, 3, 15, 2]):
        should_continue = combat.execute_round()
    assert combat.round == 1


def test_combat_ends_when_defeated(combat, enemy):
    """Test combat ends when enemy defeated."""
    combat.initiative_order = [combat.player, combat.enemy]
    enemy.hp = 1
    
    with patch("dndgame.dice.roll", side_effect=[20, 10]):
        should_continue = combat.execute_round()
    assert should_continue is False
    assert not enemy.is_alive()