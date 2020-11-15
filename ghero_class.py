import random
class Superhero():
    def __init__(self):
        self.name = 'Ice Queen'
        self.superpowers = ['Ice Cannon', 'Blizzard', 'Snow Wind']
        self.life_points = random.randint(0,10)
    def attack(self):
        return random.randint(0,10)
    def decrease_life(self, x):
        self.life_points -= x
superhero = Superhero()

