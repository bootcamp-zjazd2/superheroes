import random
class Superman:
    def __init__(self, name, superpowers, life_points):
        self.name = name
        self.superpowers = superpowers
        superpowers = ['latanie', 'oddychanie pod woda', 'fire resisance']
        self.life_points = life_points

    def attack(self):
        points = random.randint(1,10)
        return points

    def decrease_life(self, x):
        self.life_points = self.life_points - x
        return self.life_points

superman = Superman('Jameson', 'fire resistance', random.randint(1,10))
print(superman.name, superman.superpowers, superman.life_points)

print(superman.decrease_life(1))