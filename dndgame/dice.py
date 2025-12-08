"""Dice rolling utilities for D&D mechanics."""

import random


def roll(dice_type: int, number_of_dice: int) -> int:
    """Roll dice and return sum.
    
    Args:
        dice_type: Type of dice (6 for d6, 20 for d20)
        number_of_dice: How many dice to roll
        
    Returns:
        Sum of all rolls
    """
    total: int = 0
    rolls: list[int] = []
    for _ in range(number_of_dice):
        result: int = random.randint(1, dice_type)
        rolls.append(result)
        total += result
    print(f"Rolling {number_of_dice}d{dice_type}: {rolls} = {total}")
    return total


def roll_with_advantage(dice_type: int) -> int:
    """Roll twice, take highest.
    
    Args:
        dice_type: Type of dice to roll
        
    Returns:
        Higher of two rolls
    """
    return max(roll(dice_type, 1), roll(dice_type, 1))


def roll_with_disadvantage(dice_type: int) -> int:
    """Roll twice, take lowest.
    
    Args:
        dice_type: Type of dice to roll
        
    Returns:
        Lower of two rolls
    """
    return min(roll(dice_type, 1), roll(dice_type, 1))