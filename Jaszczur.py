import random

class Wielki_Jaszczur():
    def __init__(self):
        self.name = "LizardMen"
        self.superpowers = ["plywa", "odrasta mu ogon"]
        self.life_points =random.randint(1,10)

    def attack(self):
        return random.randint(1,10)

    def decrease_life(self,damage):
        self.life_points -= damage

Jaszczur=Wielki_Jaszczur()
