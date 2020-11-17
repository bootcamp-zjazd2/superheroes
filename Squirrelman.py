import random
class Heroes:
    def __init__(self):
        self.name = 'Squirrelman'
        self.superpowers = ['nut throw', 'scratching']
        self.life_points = random.randint(1,10)

    def attack(self):
        return random.randint(1,10)

    def decrease_life(self,x):
        self.life_points -= x

squirrelman = Heroes()
