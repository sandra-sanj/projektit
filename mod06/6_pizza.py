# Kirjoita funktio, joka saa parametreinaan pyöreän pizzan halkaisijan senttimetreinä sekä
# pizzan hinnan euroina. Funktio laskee ja palauttaa pizzan yksikköhinnan euroina per neliömetri.
# Pääohjelma kysyy käyttäjältä kahden pizzan halkaisijat ja hinnat sekä ilmoittaa,
# kumpi pizza antaa paremman vastineen rahalle (eli kummalla on alhaisempi yksikköhinta).
# Yksikköhintojen laskennassa on hyödynnettävä kirjoitettua funktiota.

from math import pi


def get_pizza_price_square_metre(diameter, price):
    radius = (diameter / 100) / 2  # first transform cm to m, then get radius by dividing by two
    area = pi * (radius ** 2 )
    return price / area


pizza1_diameter = int(input('Input first pizza diameter (cm): '))
pizza2_diameter = int(input('Input second pizza diameter (cm): '))

pizza1_price = float(input('Input first pizza price (€): '))
pizza2_price = float(input('Input second pizza price (€): '))

pizza1_price_per_square_metre = get_pizza_price_square_metre(pizza1_diameter, pizza1_price)
pizza2_price_per_square_metre = get_pizza_price_square_metre(pizza2_diameter, pizza2_price)

cheaper_pizza_diameter = False
cheaper_pizza_price_per_square_metre = False

# decide cheaper pizza by price per square metre
if pizza1_price_per_square_metre < pizza2_price_per_square_metre:
    cheaper_pizza_diameter = pizza1_diameter
    cheaper_pizza_price_per_square_metre = pizza1_price_per_square_metre

elif pizza2_price_per_square_metre < pizza1_price_per_square_metre:
    cheaper_pizza_diameter = pizza2_diameter
    cheaper_pizza_price_per_square_metre = pizza2_price_per_square_metre

if cheaper_pizza_diameter:
    print(f'Cheaper pizza: {cheaper_pizza_diameter}cm diameter '
          f'({round(cheaper_pizza_price_per_square_metre, 2)}€/m^2)')
else:
    print('Cannot say which pizza is cheaper.')
