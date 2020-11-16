import random

from branch_tomaszg import Jameson
from flyingcarrot import FlyingCarrotHero
from ghero_class import superhero
from hero import human_spider
from ironman import iron_man
from Jaszczur import Jaszczur
from lambert import lambert
from lukasz import Lukasz1
from plik_bartka import superdog_1
from Squirrelman import Squirrelman
from super_karen import super_Karen
from superheroes_jn import super_pies
from underdog import U1
from zadanko4 import superhero_2



jameson = Jameson()
superhero_list = [jameson,
                  FlyingCarrotHero,
                  superhero,
                  iron_man,
                  human_spider,
                  Jaszczur,
                  lambert,
                  Lukasz1,
                  superdog_1,
                  Squirrelman,
                  super_Karen,
                  super_pies,
                  U1,
                  superhero_2
                  ]

ans = ''
counter = 1
while (ans == '') & (len(superhero_list)>1):
    print(f'----------RUNDA {counter}-------------')
    for hero in superhero_list:
        print(hero.name, hero.life_points)
    fighters = random.sample(superhero_list, k=2)
    attack = []
    for fighter in fighters:
        fighter_attack = fighter.attack()
        attack.append(fighter_attack)
        print(f'Postać {fighter.name} walczy {random.choice(fighter.superpowers)} i zadaje {fighter_attack} obrazeń')

    if attack[0]>attack[1]:
        attack_points = attack[0] - attack[1]
        print(f'Postac {fighters[0].name} wygrywa z {fighters[1].name} zadajac mu {attack_points} obrazen')
        fighters[1].decrease_life(attack_points)
        if fighters[1].life_points <= 0:
            print(f'Postac {fighters[1].name} umiera')
            superhero_list.remove(fighters[1])

    elif attack[0]<attack[1]:
        attack_points = attack[1] - attack[0]
        print(f'Postac {fighters[1].name} wygrywa z {fighters[0].name} zadajac mu {attack_points} obrazen')
        fighters[0].decrease_life(attack_points)
        if fighters[0].life_points <= 0 :
            print(f'Postac {fighters[0].name} umiera')
            superhero_list.remove(fighters[0])

    else:
        print('REMIS')
        counter += 1
        continue
    counter += 1
    ans = input()

print(f'Wygrywa: {superhero_list[0].name}')