# Muokkaa edellistä funktiota siten, että funktio saa parametrinaan nopan tahkojen yhteismäärän.
# Muokatun funktion avulla voit heitellä esimerkiksi 21-tahkoista roolipelinoppaa.
# Edellisestä tehtävästä poiketen nopan heittelyä jatketaan pääohjelmassa kunnes saadaan nopan maksimisilmäluku,
# joka kysytään käyttäjältä ohjelman suorituksen alussa.


import random


def random_die(number_of_sides):
    return random.randint(1, number_of_sides)

die_result = None
dice_thrown = 0

die_sides = int(input('Input number of sides for die: '))

while die_result != die_sides:
    dice_thrown += 1

    die_result = random_die(die_sides)
    print(die_result)

print(f'Total of {dice_thrown} dice were thrown')
