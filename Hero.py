class Hobbit():
    def __init__(self):
        import random
        self.name = 'Bilbo_Baggins'
        self.superpowers = ['the One Ring stealing', 'two beers at once', "double lunch", 'pickpocketing', 'sneaking']
        self.life_points = random.randint(1, 10)

    def attack(self):
        import random
        return random.randint(1, 10)
    def decrease_life(self, x):
        self.life_points -= x

hobbit1 = Hobbit()