import random
import time
from super_karen import super_Karen
from flyingcarrot import FlyingCarrotHero
from ghero_class import superhero
from ironman import iron_man
from Jaszczur import Jaszczur
from lambert import lambert
from lukasz import Lukasz1
# from plik_bartka import superdog_1

# here should be a list of possible choices
heroes = [super_Karen, FlyingCarrotHero, superhero, iron_man, Jaszczur, lambert, Lukasz1]
random.shuffle(heroes)


def intro(h_a, h_b, round_nr, time_delay, weapon_a, weapon_b):
    """
    Intro: initialize the fight sequence of each round.

    :param time_delay: Pause between steps [s]
    :param round_nr: Round number
    :param h_a: Hero 1
    :param h_b: Hero 2
    """
    print(f'ROUND {round_nr}.\n')
    time.sleep(time_delay)
    print(f"Hero {h_a.name}'s weapon of choice is {weapon_a}!!!\n"
          f"......aaaaaaaaand.......")
    time.sleep(time_delay)
    print(f"hero {h_b.name}'s weapon of choice is {weapon_b}!!!")
    time.sleep(time_delay)
    print('Beggining countdown.')

    n = 3
    while n > 0:
        print(n)
        time.sleep(time_delay)
        n -= 1
    print("FIGHT!!!")
    time.sleep(.3)
    print("...and let odds be with you!!!")
    return


def play_round(h_a, h_b, round_nr, time_delay, weapon_a, weapon_b):
    """
    Play main fight sequence.
    :param h_a: Hero 1
    :param h_b: Hero 2
    :param round_nr: Round number
    :param time_delay: Pause between steps [s]
    :return: 
    """
    while h_a.life_points > 0 and h_b.life_points > 0:
        time.sleep(time_delay / 2)
        print(f"{h_a.name} has {h_a.life_points} life points "
              f"and {h_b.name} has {h_b.life_points} life points.")
        h_a_attack = h_a.attack()
        h_b_attack = h_b.attack()
        print(f"{h_a.name} attacks with {weapon_a} and inflicts {h_a_attack} damage points.")
        time.sleep(time_delay/2)
        print(f"{h_b.name} attacks with {weapon_b} and inflicts {h_b_attack} damage points.")
        time.sleep(time_delay / 2)
        if h_a_attack > h_b_attack:
            h_b.decrease_life(h_a_attack - h_b_attack)
            print(f"{h_b.name} has lost {h_a_attack - h_b_attack} life points.")
        elif h_a_attack < h_b_attack:
            h_a.decrease_life(h_b_attack - h_a_attack)
            print(f"{h_a.name} has lost {h_b_attack - h_a_attack} life points.")
        else:
            print(f"DRAW!!! \n"
                  f"Ladies and gentlemen, what a game!!!")
        time.sleep(time_delay)
    # End of the round
    if h_a.life_points <= 0:
        print(f"{h_a.name} bleeds to death...\n"
              f"and the winner of the round\n"
              f"is\n"
              f"{h_b.name.upper()}!!!")
        dead = h_a
    else:
        print(f"{h_b.name} bleeds to death..."
              f"and the winner of the round\n"
              f"is\n"
              f"{h_a.name.upper()}!!!")
        dead = h_b
    print(f'End of ROUND {round_nr}.\n')
    time.sleep(time_delay)
    return dead


def game(hero_list, delay_time):
    round_number = 0
    while len(hero_list) != 1:
        round_number += 1
        hero_a = hero_list[0]
        hero_b = hero_list[1]
        print(f'------------> MATCH <------------\n'
              f'{hero_a.name.upper()}    VS  {hero_b.name.upper()}')
        weapon_a = random.choices(hero_a.superpowers)[0]
        weapon_b = random.choices(hero_b.superpowers)[0]
        intro(hero_a, hero_b, round_number, delay_time, weapon_a, weapon_b)
        game = play_round(hero_a, hero_b, round_number, delay_time, weapon_a, weapon_b)
        hero_list.remove(game)
    time.sleep(delay_time)
    print(f'The ultimate winner is {hero_list[0].name.upper()}!!!')


game(heroes, .5)
