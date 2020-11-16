import random

class superhero():
    def __init__(self):
        self.name = "Piekielna Kaczka"
        self.superpowers = ["Thundershock", "Thunderbolt", "Thunder"]
        self.life_points = random.randint(1,10)

    def attack(self):
        return random.randint(1,10)

    def decrease_life(self, x):
        self.life_points -= x

superhero_2 = superhero()