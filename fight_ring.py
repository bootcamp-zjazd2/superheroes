import random
import time
from super_karen import super_Karen
from flyingcarrot import FlyingCarrotHero
from ghero_class import superhero
from hero import HumanSpider

# here should be a list of possible choices
heroes = [super_Karen, FlyingCarrotHero, superhero, HumanSpider]
random.shuffle(heroes)

hero_a, hero_b = random.choices(heroes, k=2)


weapon_a = random.choices(hero_a.superpowers)[0]
weapon_b = random.choices(hero_b.superpowers)[0]


def intro(h_a, h_b, round_nr, time_delay):
    """
    Intro: initialize the fight sequence of each round.

    :param time_delay: Pause between steps [s]
    :param round_nr: Round number
    :param h_a: Hero 1
    :param h_b: Hero 2
    """
    print(f'ROUND {round_nr}\n')
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


def play_round(h_a, h_b, round_nr, time_delay):
    """
    Play main fight sequence.
    :param h_a: Hero 1
    :param h_b: Hero 2
    :param round_nr: Round number
    :param time_delay: Pause between steps [s]
    :return: 
    """
    while h_a.life_points > 0 and h_b.life_points > 0:
        print(f"{h_a.name} has {h_a.life_points} life points "
              f"and {h_a.name} has {h_a.life_points} life points.")
        h_a_attack = h_a.attack()
        h_b_attack = h_b.attack()
        print(f"{h_a.name} attacks with {weapon_a} and inflicts {h_a_attack} damage points.\n"
              f"{h_b.name} attacks with {weapon_b} and inflicts {h_b_attack} damage points.")

        if h_a_attack > h_b_attack:
            h_b.decrease_life(h_a_attack - h_b_attack)
            print(f"{h_b.name} has lost {h_a_attack - h_b_attack} life points.")
        elif h_a_attack < h_b_attack:
            h_a.decrease_life(h_b_attack - h_a_attack)
            print(f"{h_a.name} has lost {h_b_attack - h_a_attack} life points.")
        else:
            print(f"DRAW!!! \n"
                  f"Ladies and gentlemen, what a game!!!")
        input('press Enter to continue')
    # End of the round
    if h_a.life_points <= 0:
        print(f"{h_a.name} bleeds to death...\n"
              f"and the winner of the round\n"
              f"is\n"
              f"{h_b.name.upper()}!!!")
    else:
        print(f"{h_b.name} bleeds to death..."
              f"and the winner of the round\n"
              f"is\n"
              f"{h_a.name.upper()}!!!")
    print(f'End do ROUND {round_nr}.')


intro(hero_a, hero_b, 1, 1)
play_round(hero_a, hero_b, 1, 1)
