# Kirjoita ohjelma, joka kysyy käyttäjältä nimiä siihen saakka, kunnes käyttäjä syöttää tyhjän merkkijonon.
# Kunkin nimen syöttämisen jälkeen ohjelma tulostaa joko tekstin Uusi nimi tai Aiemmin syötetty nimi sen mukaan,
# syötettiinkö nimi ensimmäistä kertaa. Lopuksi ohjelma luettelee syötetyt nimet yksi kerrallaan allekkain
# mielivaltaisessa järjestyksessä. Käytä joukkotietorakennetta nimien tallentamiseen.


names = set()

new_name = False
while new_name != '':
    new_name = input('Input a name: ')

    if new_name == '':
        break
    elif new_name in names:
        print('Name already added')
    else:
        names.add(new_name)
        print(f'Added new name {new_name}')

for name in names:
    print(name)
