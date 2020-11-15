import random
import super_karen

# here should be a list of possible choices
heroes = [super_karen.super_Karen, super_karen.super_Karen, super_karen.super_Karen]

hero_A, hero_B = random.choices(heroes, k=2)

# Intro xD
weapon_A = random.choices(hero_A.superpowers)[0]
weapon_B = random.choices(hero_B.superpowers)[0]

print(f"Hero {hero_A.name}'s weapon of choice is {weapon_A}!!! \n"
      f"......aaaaaaaaand.......\n"
      f"hero {hero_B.name}'s weapon of choice is {weapon_B}!!!")
input('press Enter to continue')
n = 3
while n > 0:
    print(n)
    n -= 1
print(f"FIGHT!!!\n"
          f"...and let the gods choose their fate!!!")

# main fight sequence
while hero_A.life_points > 0 and hero_B.life_points > 0:
    print(f"{hero_A.name} has {hero_A.life_points} life points "
          f"and {hero_A.name} has {hero_A.life_points} life points.")
    hero_A_attack = hero_A.attack()
    hero_B_attack = hero_B.attack()
    print(f"{hero_A.name} attacks with {weapon_A} and inflicts {hero_A_attack} damage points.\n"
          f"{hero_B.name} attacks with {weapon_B} and inflicts {hero_B_attack} damage points.")

    if hero_A_attack > hero_B_attack:
        hero_B.decrease_life(hero_A_attack - hero_B_attack)
        print(f"{hero_B.name} has lost {hero_A_attack - hero_B_attack} life points.")
    elif hero_A_attack < hero_B_attack:
        hero_A.decrease_life(hero_B_attack - hero_A_attack)
        print(f"{hero_A.name} has lost {hero_B_attack - hero_A_attack} life points.")
    else:
        print(f"DRAW!!! \n"
              f"Ladies and gentlemen, what a game!!!")
    input('press Enter to continue')

if hero_A.life_points <= 0:
    print(f"{hero_B.name} bleeds to death...\n"
          f"and the winner\n"
          f"is\n"
          f"{hero_A.name.upper()}!!!")
else:
    print(f"{hero_A.name} bleeds to death..."
          f"and the winner\n"
          f"is\n"
          f"{hero_B.name.upper()}!!!")

