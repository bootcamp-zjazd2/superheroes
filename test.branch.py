import random

class Superman():
    def __init__(self):
        name = 'superman'
        superpowers = 'ab'
        life_points = random.randint(1,10)

    def attack(self):
        print(random.randint(1,10))

    def decrease_life(self, x):
        life_points = random.randint(1, 10)
        print(life_points - x)

bohater = Superman()
print(bohater.decrease_life(4))