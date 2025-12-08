"""Combat system for encounters."""

from typing import Optional
from dndgame.dice import roll
from dndgame.entity import Entity


class Combat:
    """Manages turn-based combat."""
    
    def __init__(self, player: Entity, enemy: Entity) -> None:
        self.player: Entity = player
        self.enemy: Entity = enemy
        self.round: int = 0
        self.initiative_order: list[Entity] = []
        self.combat_log: list[str] = []

    def roll_initiative(self) -> list[Entity]:
        """Roll initiative for turn order."""
        player_init: int = roll(20, 1) + self.player.get_modifier("DEX")
        enemy_init: int = roll(20, 1) + self.enemy.get_modifier("DEX")

        print(f"\n{self.player.name} initiative: {player_init}")
        print(f"{self.enemy.name} initiative: {enemy_init}")

        if player_init >= enemy_init:
            self.initiative_order = [self.player, self.enemy]
            print(f"{self.player.name} goes first!\n")
        else:
            self.initiative_order = [self.enemy, self.player]
            print(f"{self.enemy.name} goes first!\n")

        return self.initiative_order

    def attack(self, attacker: Entity, defender: Entity) -> int:
        """Perform attack roll and apply damage."""
        attack_roll: int = roll(20, 1) + attacker.get_modifier("STR")
        
        print(f"{attacker.name} attacks {defender.name}!")
        print(f"Attack roll: {attack_roll} vs AC {defender.armor_class}")
        
        if attack_roll >= defender.armor_class:
            damage: int = roll(6, 1) + attacker.get_modifier("STR")
            damage = max(1, damage)
            defender.take_damage(damage)
            
            log = f"{attacker.name} hit for {damage} damage!"
            print(log)
            self.combat_log.append(log)
            return damage
        else:
            log = f"{attacker.name} missed!"
            print(log)
            self.combat_log.append(log)
            return 0

    def execute_round(self) -> bool:
        """Execute one combat round. Returns True if combat continues."""
        self.round += 1
        print(f"\n{'='*40}")
        print(f"ROUND {self.round}")
        print(f"{'='*40}")
        
        for entity in self.initiative_order:
            if not entity.is_alive():
                continue
            
            opponent = self.enemy if entity == self.player else self.player
            if not opponent.is_alive():
                break
            
            print(f"\n{entity.name}'s turn:")
            self.attack(entity, opponent)
            
            print(f"\n{self.player.name} HP: {self.player.hp}/{self.player.max_hp}")
            print(f"{self.enemy.name} HP: {self.enemy.hp}/{self.enemy.max_hp}")
            
            if not opponent.is_alive():
                print(f"\n{opponent.name} defeated!")
                return False
        
        return True

    def run_combat(self) -> Optional[Entity]:
        """Run complete combat. Returns winner."""
        print(f"\n{'='*40}")
        print(f"COMBAT: {self.player.name} vs {self.enemy.name}")
        print(f"{'='*40}")
        
        self.roll_initiative()
        
        while self.player.is_alive() and self.enemy.is_alive():
            if not self.execute_round():
                break
        
        if self.player.is_alive():
            print(f"\n{self.player.name} is victorious!")
            return self.player
        else:
            print(f"\n{self.player.name} has fallen!")
            return self.enemy