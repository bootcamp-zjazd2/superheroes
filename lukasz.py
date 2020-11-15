import random

class bohater():
    def __init__(self, name):
        self.name = name
        self.superpowers = ['lepienie garnkow', 'latanie']
        self.life_points = random.randint(1,11)

    def attack(self):
        return random.randint(1,10)
    def decrease_life(self,x):
        self.life_points -= x

Lukasz1 = bohater("Lukasz")