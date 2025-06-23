class Weapons:
    def __init__(self, name, weapon):
        self.name = name
        self.weapon = weapon

    def __str__(self):
        return f"{self.name} does damage with {self.weapon}"
    
class Player:
    def __init__(self, name, weapon):
        self.name = name
        self.weapon = weapon
        self.health = 100
        self.is_alive = True

    def take_hit(self, damage):
        self.health -= damage
        if self.health <= 0:
            self.is_alive = False
            print(f"{self.name} has been defeated!")

    def __str__(self):
        return f"{self.name} with {self.weapon}"