import random

class Wielki_Jaszczur():
    def __init__(self,name="LizardMen",superpowers=["plywa", "odrasta mu ogon"]):
        self.name=name
        self.superpowers=superpowers
        self.life_points=random.randint(1,10)

    def attack(self):
        return random.randint(1,10)

    def decrease_life(self,damage):
        self.life_points -= damage

Jaszczur=Wielki_Jaszczur()