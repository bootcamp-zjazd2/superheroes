class Superheroes():
    def __init__(self, name, superpowers, life_points):
        self.name = name
        self.superpowers = superpowers
        self.life_points = life_points
bohater1 = Superheroes('SuperPies', 'lizanie', 100)
print(bohater1.name, bohater1.superpowers, bohater1.life_points)