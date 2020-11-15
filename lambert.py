import random
class Lambert():
    def __init__(self):
        self.name = 'Lambert'
        self.superpowers = ['kontrola umysłu', 'zamrażająca petarda',
                            'wiedźmiński sierpowy', 'eliksir zwiększonej siły',
                            'sokole oko']
        self.life_points = random.randint(1,10)

    def attack(self):
        return random.randint(1,10)

    def decrease_life(self, x):
        self.life_points -= x


lambert = Lambert()
