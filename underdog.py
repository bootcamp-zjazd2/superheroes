import random
class Underdog:
    def __init__(self):
        self.name = 'dog'
        self.superpowers = ['superspeed', 'punch']
        self.life_points = random.randint(1,10)

    def attack(self):
        return random.randint(1,10)

    def decrease_life(self, x):
        self.life_points -= x

U1 = Underdog()
