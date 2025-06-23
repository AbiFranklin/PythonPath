class Weapon:
    """
    The Weapon class represents a weapon used by a character in the game.
    """
    def __init__(self, name, weapon, damage, sound):
        self.name = name
        self.weapon = weapon
        self.damage = damage
        self.sound = sound

    def attack(self):
        """
        Simulate an attack with this weapon.

        :return: The amount of damage dealt.
        """
        print(f"{self.sound}! {self.name} attacks with {self.weapon} "
              f"and deals {self.damage} damage!")
        return self.damage

    def __str__(self):
        return f"{self.sound}! {self.name} does damage {self.damage} with {self.weapon}"
    

class Player:
    """
    The Player class represents a player in the game.
    """
    def __init__(self, name, weapon):
        self.name = name
        self.weapon = weapon
        self.health = 100

    def take_hit(self, damage):
        """
        Called when the player takes a hit from the opponent's weapon.

        :param damage: The amount of damage taken.
        :return: The updated health value.
        """
        self.health -= damage
        return self.health

    @property
    def is_alive(self):
        return self.health > 0

    def __str__(self):
        return f"{self.name} with {self.weapon.weapon} (Health: {self.health})"
