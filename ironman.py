import random

class IronMan():
    def __init__(self):
        self.name = 'Tony Stark'
        self.superpowers = ['sonic_attack', 'missile_projection']
        self.life_points = random.randint(1, 10)

    def attack(self):
        return random.randint(1, 10)

    def decrease_life(self, x):
        self.life_points -= x


iron_man = IronMan()