from branch_tomaszg import Jameson
from flyingcarrot import FlyingCarrotHero
from ghero_class import superhero
# from hero import HumanSpider
from ironman import iron_man
from Jaszczur import Jaszczur
from KapitanMarvel import kapitan_Marvel
from lambert import lambert
from plik_bartka import superdog_1
from Squirrelman import squirrelman
from super_karen import super_Karen
from superheroes_jn import super_pies
from lukasz import lukasz
from underdog import U1
from zadanko4 import piekielna_kaczka

import random

supehero_list = [Jameson, FlyingCarrotHero, superhero,
                 iron_man, Jaszczur, kapitan_Marvel, lambert, superdog_1, squirrelman,
                 super_Karen, super_pies, lukasz, U1, piekielna_kaczka]

fighters = random.sample(supehero_list, k=4)
player_1 = fighters[0]
player_2 = fighters[1]
player_3 = fighters[2]
player_4 = fighters[3]

print('----------------GRA SUPERHEROES-------------')
print('\n')
print(f'--------------------WALKA-------------------')
print('\n')
print(f'{player_1.name} {player_1.life_points}HP oraz {player_3.name} {player_3.life_points}HP'
      f' VS {player_2.name} {player_2.life_points}HP oraz {player_4.name} {player_4.life_points}HP')
print('\n'
      '')
round_num = 1

while player_1.life_points > 0 and player_2.life_points > 0 and player_3.life_points > 0 and player_4.life_points > 0:

    print(f'-------------------RUNDA {round_num}-------------------- ')
    round_num += 1

    print(f'Walka: {player_1.name} {player_1.life_points}HP vs {player_2.name} {player_2.life_points}HP')

    attack_f1 = player_1.attack()
    attack_f2 = player_2.attack()
    weapon_f1 = random.choices(player_1.superpowers, k=1)
    weapon_f2 = random.choices(player_2.superpowers, k=1)

    print(f'{player_1.name} atakuje moca: {weapon_f1[0].upper()} i zadaje {attack_f1} obrazen')
    print(f'{player_2.name} atakuje moca: {weapon_f2[0].upper()} i zadaje {attack_f2} obrazen')

    if attack_f1 < attack_f2:
        player_1.decrease_life(attack_f2 - attack_f1)
        print(f'{player_1.name} traci {attack_f2 - attack_f1} punktow zycia')
    elif attack_f1 > attack_f2:
        player_2.decrease_life(attack_f1 - attack_f2)
        print(f'{player_2.name} traci {attack_f1 - attack_f2} punktow zycia')
    if attack_f1 == attack_f2:
        print("REMIS - Walka trwa dalej!")
        continue

    print(f'{player_1.name} pozostalo {player_1.life_points}')
    print(f'{player_2.name} pozostalo {player_2.life_points}')

    if player_1.life_points <= 0:
        print(f'{player_1.name} WYGRYWA!!!')
        player_1 = player_3

    if player_2.life_points <= 0:
        print(f'{player_2.name} WYGRYWA!!!')
        player_2 = player_4

    print('\n')
