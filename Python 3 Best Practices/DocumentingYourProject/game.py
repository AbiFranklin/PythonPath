import random
from gamedemo import Player, Weapon


class Game:
    """
    Implements the game mechanics. See `run()` for flow.
    """
    def __init__(self, player1, player2):
        self.p1 = player1
        self.p2 = player2

    def run(self):
        print(self.p1)
        print(self.p2)
        while self.p1.is_alive and self.p2.is_alive:
            attacker, defender = (
                (self.p1, self.p2) if random.choice([True, False]) else (self.p2, self.p1)
            )
            print(f"\n{attacker.name} attacks!")
            damage = attacker.weapon.attack()
            defender.take_hit(damage)
            print(f"{defender.name} takes {damage} damage and is now at {defender.health} health.")
        winner = self.p1 if self.p1.is_alive else self.p2
        print(f"\n🏆 {winner.name} wins with {winner.health} health left!")


if __name__ == "__main__":
    random.seed()
    knight_weapon = Weapon("The Knight", "sword", 20, "Clang")
    dragon_weapon = Weapon("The Dragon", "firebreath", 25, "Fwoosh")

    g = Game(
        Player("The Knight", knight_weapon),
        Player("The Dragon", dragon_weapon),
    )
    g.run()
