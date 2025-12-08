"""Main entry point for D&D Adventure game."""

from dndgame.character import Character
from dndgame.enemy import Enemy
from dndgame.combat import Combat


def get_valid_input(prompt: str, valid_options: list[str]) -> str:
    """Get validated input from user."""
    while True:
        user_input = input(prompt).strip()
        if user_input in valid_options:
            return user_input
        print(f"Invalid. Choose from: {', '.join(valid_options)}")


def get_non_empty_input(prompt: str) -> str:
    """Get non-empty input from user."""
    while True:
        user_input = input(prompt).strip()
        if user_input:
            return user_input
        print("Cannot be empty. Try again.")


def create_character() -> Character:
    """Guide user through character creation."""
    print("Welcome to D&D Adventure!")
    print("="*40)
    
    name = get_non_empty_input("\nEnter character name: ")

    print("\nChoose your race:")
    races = Character.available_races
    for i, race in enumerate(races, 1):
        desc = Character.get_race_description(race)
        print(f"{i}. {race} ({desc})")
    
    choice = get_valid_input(f"Enter choice (1-{len(races)}): ", 
                             [str(i) for i in range(1, len(races) + 1)])
    race = races[int(choice) - 1]

    print(f"\nCreating {name} the {race}...\n")
    
    character = Character(name, race, 10)
    character.roll_stats()
    character.apply_racial_bonuses()
    
    print("\nCharacter created!")
    return character


def display_character(character: Character) -> None:
    """Display character information."""
    print(f"\n{'='*40}")
    print(f"{character.name} the {character.race}")
    print(f"{'='*40}")
    print(f"Level: {character.level}")
    print(f"HP: {character.hp}/{character.max_hp}")
    print(f"AC: {character.armor_class}")
    
    print("\nAbility Scores:")
    for stat, value in character.stats.items():
        mod = character.get_modifier(stat)
        print(f"  {stat}: {value:2d} ({'+' if mod >= 0 else ''}{mod})")


def combat_encounter(player: Character, enemy_type: str) -> bool:
    """Run combat encounter. Returns True if player won."""
    enemy = Enemy(enemy_type)
    combat = Combat(player, enemy)
    winner = combat.run_combat()
    return winner == player


def main() -> None:
    """Main game loop."""
    player = create_character()
    display_character(player)
    
    game_running = True
    while game_running and player.is_alive():
        print("\n" + "="*40)
        print("What would you like to do?")
        print("="*40)
        print("1. Fight a Goblin")
        print("2. Fight an Orc")
        print("3. View character")
        print("4. Rest (restore HP)")
        print("5. Quit")

        choice = get_valid_input("Enter choice (1-5): ", ["1", "2", "3", "4", "5"])

        if choice == "1":
            if not combat_encounter(player, "Goblin"):
                print("\nGame Over!")
                game_running = False
                
        elif choice == "2":
            if not combat_encounter(player, "Orc"):
                print("\nGame Over!")
                game_running = False
                
        elif choice == "3":
            display_character(player)
            
        elif choice == "4":
            player.heal(player.max_hp)
            print(f"\n{player.name} rests!")
            print(f"HP: {player.hp}/{player.max_hp}")
            
        elif choice == "5":
            print("\nThanks for playing!")
            game_running = False

    if game_running and player.is_alive():
        print(f"\n{player.name} lives to adventure another day!")


if __name__ == "__main__":
    main()