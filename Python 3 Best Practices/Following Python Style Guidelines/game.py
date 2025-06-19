"""
game.py
-------------

This module contains the Game class that implements the actual game
mechanics as well as the __main__ construct to run the game.
"""

#  pylint: disable=invalid-name
__author__ = "Abi Franklin"

# Imports should be on separate lines
# Imports should be grouped in the following order:
# 1. Standard library imports
# 2. Related third-party imports
# 3. Local application/library specific imports
# The groups should be separated by a single blank line
import random

from gamedemo import weapons, player


# Two blank lines before and after top level classes and functions
class Game:
    def __init__(self, player1, player2):
        self.p1 = player1
        self.p2 = player2

    # One blank line between methods in a class

    def run(self):
        # Indent with 4 spaces
        print(self.p1)
        print(self.p2)
        while self.p1.is_alive and self.p2.is_alive:
            if random.choice([True, False]):
                attacker = self.p1
                defender = self.p2
            else:
                attacker = self.p2
                defender = self.p1
            dmg, sound = attacker.weapon.attack()
            print(attacker.name, "attacks:", sound)
            print(defender.name, "takes", dmg, "damage")
            defender.take_hit(dmg)
        print(attacker.name, "won with", attacker.health, "health left")


# Two blank lines before and after top level classes and functions
if __name__ == "__main__":
    random.seed()
    g = Game(
        player.Player("The Knight", weapons.Sword()),
        player.Player("The Dragon", weapons.FireBreath()),
    )
    g.run()


# Other Style Guidelines
# Use spaces not tabs for indentation
# Maximum line length is 79 characters
# Continuation lines should align wrapped elements with opening delimiter
# Naming:
# - Module names should be short, all lowercase, and can include underscores
# - Class names should use CamelCase
# - Function names should be lowercase, with words separated by underscores
# - Constants should be all uppercase with words separated by underscores
# - Variables should be lowercase, with words separated by underscores
# - Private variables should start with an underscore
# Documentation:
# - Use docstrings for all public modules, classes, and functions
# - Refer to the PEP 257 for docstring conventions
