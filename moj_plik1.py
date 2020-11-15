
import random
class Kapitan_Marvel():

    def __init__(self):
        self.name = 'Kapitan Marvel'
        self.superpowers = ['Zwiększona siła', 'Wytrzymałość', 'Zwinność', 'Odporność na truciznę']
        self.life_points = random.randint(1,10)

    def attack(self):
        return random.randint(1,10)

    def decrease_life(self, x):
        self.life_points -= x