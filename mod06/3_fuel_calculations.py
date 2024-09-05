# Kirjoita funktio, joka saa parametrinaan bensiinin määrän Yhdysvaltain nestegallonoina
# ja palauttaa paluuarvonaan vastaavan litramäärän. Kirjoita pääohjelma,
# joka kysyy gallonamäärän käyttäjältä ja muuntaa sen litroiksi. Muunnos on tehtävä aliohjelmaa hyödyntäen.
# Muuntamista jatketaan siihen saakka, kunnes käyttäjä syöttää negatiivisen gallonamäärän.
# Yksi gallona on 3,785 litraa.


def get_gallons_in_liters(gallons):
    gallon_in_liters = 3.785
    return gallons * gallon_in_liters

input_gallons = 0
while input_gallons >= 0:
    input_gallons = float(input('Input gallons: '))

    if input_gallons >= 0:
        gallons_in_liters = get_gallons_in_liters(input_gallons)
        print(gallons_in_liters)

print('Program ended.')
