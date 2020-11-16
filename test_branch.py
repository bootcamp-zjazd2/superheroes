import random

class SuperMan():
    def __init__(self):
        self.name = 'SuperMan'
        self.superpowers = ['shooting', 'fire punch', 'drilling']
        self.life_points = random.randint(1,10)

    def attack(self):
        return random.randint(1, 10)

    def decrease_life(self, x):
        self.life_points -= x

super_man1 = SuperMan()