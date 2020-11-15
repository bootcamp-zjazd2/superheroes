import random
class Superhero():
    def __init__(self, name,superpowers,life_points):
        self.name = name
        self.superpowers = superpowers
        self.life_points = life_points
    def attack(self):
        return random.randint(0,10)
    def decrease_life(self, x):
        self.life_points -= x
superhero = Superhero('Ice Queen', ['Ice Cannon', 'Blizzard', 'Snow Wind'], random.randint(0,10))
print(superhero.name)
