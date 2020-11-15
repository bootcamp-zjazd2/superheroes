import random
class Karen():
    def __init__(self):
        self.name = 'Karen'
        self.superpowers = ['Offend Enemy', 'Talk to manager']
        self.life_points = random.randint(1, 11)

    def attack(self):
        return random.randint(1, 11)

    def decrease_life(self, x):
        self.life_points -= x

super_Karen = Karen()