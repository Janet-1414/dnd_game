"""Base entity class for all combat participants."""

from abc import ABC


class Entity(ABC):
    """Base class for all entities in combat.

    Attributes:
        name: Entity name
        stats: Ability scores dict
        hp: Current hit points
        max_hp: Maximum hit points
        armor_class: Defense rating
        level: Entity level
    """

    def __init__(
        self, name: str, max_hp: int, armor_class: int = 10, level: int = 1
    ) -> None:
        self.name: str = name
        self.stats: dict[str, int] = {
            "STR": 10,
            "DEX": 10,
            "CON": 10,
            "INT": 10,
            "WIS": 10,
            "CHA": 10,
        }
        self.hp: int = max_hp
        self.max_hp: int = max_hp
        self.armor_class: int = armor_class
        self.level: int = level

    def get_modifier(self, stat: str) -> int:
        """Calculate ability modifier from stat."""
        return (self.stats[stat] - 10) // 2

    def is_alive(self) -> bool:
        """Check if entity is alive."""
        return self.hp > 0

    def take_damage(self, damage: int) -> None:
        """Reduce HP by damage amount."""
        self.hp = max(0, self.hp - damage)

    def heal(self, amount: int) -> None:
        """Restore HP up to max."""
        self.hp = min(self.max_hp, self.hp + amount)
