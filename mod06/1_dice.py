# Kirjoita parametriton funktio, joka palauttaa paluuarvonaan satunnaisen nopan silmäluvun väliltä 1..6.
# Kirjoita pääohjelma, joka heittää noppaa niin kauan kunnes tulee kuutonen.
# Pääohjelma tulostaa kunkin heiton jälkeen saadun silmäluvun.

import random


def random_die():
    return random.randint(1, 6)

die_result = None
dice_thrown = 0

while die_result != 6:
    dice_thrown += 1

    die_result = random_die()
    print(die_result)

print(f'Total of {dice_thrown} dice were thrown')
