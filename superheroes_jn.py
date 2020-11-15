import random

class SuperPies():
    def __init__(self):
        self.name = 'Super Lindor'
        self.superpowers = ['lizanie', 'podjadanie', 'szczekanie']
        self.life_points = random.randint(1,10)

    def attack(self):
        return random.randint(1, 10)

    def decrease_life(self, x):
        self.life_points -= x

super_pies = SuperPies()