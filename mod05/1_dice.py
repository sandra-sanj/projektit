# Kirjoita ohjelma, joka kysyy käyttäjältä arpakuutioiden lukumäärän.
# Ohjelma heittää kerran kaikkia arpakuutioita ja tulostaa silmälukujen summan. Käytä for-toistorakennetta.

import random

number_of_dice = int(input('Syötä arpakuutioiden lukumäärä: '))

dice_sum = 0
for _ in range(number_of_dice):
    dice_sum += random.randint(1, 6)

print(f'Arpakuutioiden summa on {dice_sum}')

