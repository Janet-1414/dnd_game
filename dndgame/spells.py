"""Spell system for D&D game."""

from typing import Optional
from dndgame.entity import Entity


class Spell:
    """Magical spell with level and power."""

    def __init__(self, name: str, level: int, school: str, spell_power: int) -> None:
        self.name: str = name
        self.level: int = level
        self.school: str = school
        self.spell_power: int = spell_power

    def cast(self, caster: Optional[Entity], target: Optional[Entity]) -> None:
        """Cast spell (placeholder)."""
        pass


class SpellBook:
    """Container for managing spells."""

    def __init__(self) -> None:
        self.spells: list[Spell] = []

    def add_spell(self, spell: Spell) -> None:
        """Add spell to book."""
        self.spells.append(spell)

    def get_available_spells(self, spell_level: int) -> list[Spell]:
        """Get spells up to level (list comprehension)."""
        return [s for s in self.spells if s.level <= spell_level]

    def get_spells_by_school(self, school: str) -> list[Spell]:
        """Get spells from school (list comprehension)."""
        return [s for s in self.spells if s.school == school]

    def get_spell_names(self) -> list[str]:
        """Get all spell names (map)."""
        return list(map(lambda s: s.name, self.spells))

    def get_powerful_spells(self, min_power: int) -> list[Spell]:
        """Get spells above power threshold (filter)."""
        return list(filter(lambda s: s.spell_power >= min_power, self.spells))
