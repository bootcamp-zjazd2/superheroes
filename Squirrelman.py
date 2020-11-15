import random
class Heroes:
    def __init__(self, name, superpowers):
        self.name = name
        self.superpowers = superpowers
        self.life_points = random.randint(1,100)

    def attack(self):
        return random.randint(1,10)

    def decrease_life(self,x):
        self.life_points -= x
Squirrelman = Heroes('Squirrelman', ['nut throw', 'scratching'])
