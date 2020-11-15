import random
class Underdog:
    def __init__(self, name, superpowers, life_points):
        self.name = name
        self.superpowers = ['superspeed', 'punch']
        self.life_points = random.randint(1,10)

    def attack(self):
        return random.randint(1-10)

    def decrease_life(self, x):
        self.life_points -= x

U1 = Underdog()
