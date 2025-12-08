"""Enemy creatures for combat."""

from typing import ClassVar
from dndgame.entity import Entity


ENEMY_TEMPLATES: dict[str, dict[str, int | dict[str, int]]] = {
    "Goblin": {
        "hp": 7, "ac": 13, "level": 1,
        "stats": {"STR": 8, "DEX": 14, "CON": 10, "INT": 10, "WIS": 8, "CHA": 8}
    },
    "Orc": {
        "hp": 15, "ac": 13, "level": 2,
        "stats": {"STR": 16, "DEX": 12, "CON": 16, "INT": 7, "WIS": 11, "CHA": 10}
    },
}


class Enemy(Entity):
    """Enemy creature from template."""
    
    available_types: ClassVar[list[str]] = list(ENEMY_TEMPLATES.keys())
    
    def __init__(self, enemy_type: str, name: str | None = None) -> None:
        if enemy_type not in ENEMY_TEMPLATES:
            raise ValueError(f"Invalid enemy type: {enemy_type}")
        
        template = ENEMY_TEMPLATES[enemy_type]
        display_name = name if name else enemy_type
        
        super().__init__(
            name=display_name,
            max_hp=int(template["hp"]),
            armor_class=int(template["ac"]),
            level=int(template["level"])
        )
        
        self.enemy_type: str = enemy_type
        if isinstance(template["stats"], dict):
            self.stats = template["stats"].copy()