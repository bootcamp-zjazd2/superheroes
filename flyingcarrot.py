import random

class FlyingCarrot():
    def __init__(self):
        self.name = 'Flying Carrot'
        self.superpowers= ['latanie','lewitacja','hipnoza']
        self.life_points = random.randint(1,10)
    def attack(self):
        return random.randint(1,10)
    def decrease_life(self,x):
        self.life_points-=x

FlyingCarrot = FlyingCarrot()


