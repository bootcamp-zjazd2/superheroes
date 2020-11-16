import random

class Superman():
    def __init__(self):
        self.name = 'Superdog'
        self.superpowers= ['odstraszanie','drapanie','latanie']
        self.life_points = random.randint(1,10)
    def attack(self):
        return random.randint(1,10)
    def decrease_life(self,x):
        self.life_points-=x
superdog_1 = Superman()