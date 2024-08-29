# Kirjoita peli, jossa tietokone arpoo kokonaisluvun väliltä 1..10.
# Kone arvuuttelee lukua pelaajalta siihen asti, kunnes tämä arvaa oikein.
# Kunkin arvauksen jälkeen ohjelma tulostaa tekstin Liian suuri arvaus, Liian pieni arvaus tai Oikein.
# Huomaa, että tietokone ei saa vaihtaa lukuaan arvauskertojen välissä.

import random

random_number = random.randint(1, 10)
print('Pelataan numeronarvauspeliä. Kone arpoo kokonaisluvun välillä 1..10 ja tehtäväsi on arvata numero.')

player_number = None

while player_number != random_number:
    player_number = int(input('Syötä arvaus: '))

    if player_number < random_number:
        print('Arvaus on liian pieni.')

    elif player_number > random_number:
        print('Arvaus on liian iso.')
else:
    print('Oikein!')