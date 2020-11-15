import random

class Superheroes():
    def __init__(self):
        self.name = 'SuperPies'
        self.superpowers = ['lizanie', 'podjadanie']
        self.life_points = random.randint(1,10)

    def attack(self):
        return random.randint(1,10)

    def decrease_life(self, x):
        self.life_points -= x

super_pies = Superheroes()