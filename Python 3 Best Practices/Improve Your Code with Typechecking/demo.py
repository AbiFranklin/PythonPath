# Causes TypeError: TypeError: unsupported operand type(s) for +: 'int' and 'str'
# def average(a,b,c):
#     return (a + b + c) / 3

# print(average(1, '5', 7))


# # Does not cause TypeError
# def average(a: int, b: int, c: int) -> float:
#     return (a + b + c) / 3


# print(average(1, 5, 7))  # Output: 4.333333333333333

# # declare the type of a variable
# age: int = 1

# # Before Python 3.5, type hints were not available. You had to use comments to indicate types.
# age = 1  # type: int


# class Player:
#     """
#     A class representing a player in a game.
#     :ivar health: The health of the player.

#     """

#     def __init__(self, name, weapon):
#         """
#         Create a new Player instance.

#         :param name: The name of the player.
#         :param weapon: The weapon of the player.

#         Weapon not currently imported, but should be a class that represents a weapon.
#         (self, name: str, weapon: Weapon, health: int = 100) -> None:

#         """
#         self.name = name
#         self.weapon = weapon
#         self.health = 100

#     def take_hit(self, damage: int) -> None:
#         """
#         Reduce the player's health by the damage taken.

#         :param damage: The amount of damage taken.
#         """
#         self.health -= damage
#         return self.health

#     @property
#     def is_alive(self) -> bool:
#         """
#         Check if the player is alive.

#         :return: True if the player is alive, False otherwise.
#         """
#         return self.health > 0

#     def __str__(self) -> str:
#         return f"Player(name={self.name}, weapon={self.weapon}, health={self.health})"

# If we were creating an instance of a player and we put the arguments in the wrong order, we would get a
# TypeError, but it would show on the line where we create the instance, not where we define the class.

# Type hints for collections
# x: list[int] = [1, 2, 3]  # List of integers
# y: set[str] = {"a", "b", "c"}  # Set of strings

# Type hints for dictionaries
# x: dict[str, int] = {
#     "a": 1,
#     "b": 2,
# }  # Dictionary with string keys and integer values

# Type hints for tuples of fixed length
# x: tuple[int, str] = (1, "a")  # Tuple with an integer and a string

# Type hints for tuples of variable length
# x: tuple[int, ...] = (1, 2, 3)  # Tuple with variable number of integers

# from typeing import List, Dict, Tuple, Set

# Type hints using typing module
# x: List[int] = [1, 2, 3]  # List of integers
# y: Set[str] = {"a", "b", "c"}  # Set of strings
# z: Dict[str, int] = {
#     "a": 1,
#     "b": 2,
# }  # Dictionary with string keys and integer values
# w: Tuple[int, str] = (1, "a")  # Tuple with an integer and a string
# t: Tuple[int, ...] = (1, 2, 3)  # Tuple with variable number of integers

from typing import Any


def max_avg(d: dict[Any, list[float]]) -> float:
    """
    Calculate the maximum average of a dictionary where each key maps to a list of floats.

    :param d: A dictionary with keys of any type and values as lists of floats.
    :return: The maximum average of the lists in the dictionary.
    """
    return max(sum(lst) / len(lst) for lst in d.values())


# print(max_avg({"a": [1, 2, 3], 20: [5.0, 6.0, 7.0], None: ["a", "b", "c"]}))
# Output: 6.0 (from the list [5.0, 6.0, 7.0])

def roots(l: list[int]) -> list[float]:
    """
    Calculate the square roots of a list of integers.

    :param l: A list of integers.
    :return: A list of square roots of the integers.
    """
    return [x ** 0.5 for x in l]

print (roots(range(100)))
