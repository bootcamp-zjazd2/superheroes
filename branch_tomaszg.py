import random
class Jameson:
    def __init__(self, name, superpowers, life_points):
        self.name = 'Jameson'
        self.superpowers = ['fire punch','ice punch', 'water punch']
        self.life_points = random.randint(1,10)

    def attack(self):
        return random.randint(1,10)

    def decrease_life(self, x):
        self.life_points -= x

Jameson = Jameson()