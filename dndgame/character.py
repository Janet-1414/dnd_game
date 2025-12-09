"""Character creation and management."""

from typing import ClassVar
from dndgame.dice import roll
from dndgame.entity import Entity


RACES: dict[str, dict[str, int]] = {
    "Human": {"STR": 1, "DEX": 1, "CON": 1, "INT": 1, "WIS": 1, "CHA": 1},
    "Elf": {"DEX": 2},
    "Dwarf": {"CON": 2},
    "Halfling": {"DEX": 2},
    "Orc": {"STR": 2, "CON": 1},
}


class Character(Entity):
    """Player character with race and stats."""

    available_races: ClassVar[list[str]] = list(RACES.keys())

    def __init__(self, name: str, race: str, base_hp: int) -> None:
        if race not in RACES:
            raise ValueError(
                f"Invalid race: {race}. Must be one of {self.available_races}"
            )

        super().__init__(name=name, max_hp=base_hp, armor_class=10, level=1)
        self.race: str = race
        self.base_hp: int = base_hp

    def roll_stats(self) -> None:
        """Roll 3d6 for each ability score."""
        print("Rolling stats...\n")
        for stat in ["STR", "DEX", "CON", "INT", "WIS", "CHA"]:
            print(f"Rolling {stat}...")
            self.stats[stat] = roll(6, 3)
        self.max_hp = self.base_hp + self.get_modifier("CON")
        self.hp = self.max_hp

    def apply_racial_bonuses(self) -> None:
        """Apply racial stat bonuses."""
        for stat, bonus in RACES[self.race].items():
            self.stats[stat] += bonus
        self.max_hp = self.base_hp + self.get_modifier("CON")
        self.hp = self.max_hp

    @classmethod
    def get_race_description(cls, race: str) -> str:
        """Get racial bonus description."""
        if race not in RACES:
            return "Unknown race"
        return ", ".join(f"+{v} {s}" for s, v in RACES[race].items())
