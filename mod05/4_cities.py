# Kirjoita ohjelma, joka kysyy käyttäjältä viiden kaupungin nimet yksi kerrallaan
# (käytä for-toistorakennetta nimien kysymiseen) ja tallentaa ne listarakenteeseen.
# Lopuksi ohjelma tulostaa kaupunkien nimet yksi kerrallaan allekkain samassa järjestyksessä kuin ne syötettiin.
# käytä for-toistorakennetta nimien kysymiseen ja for/in toistorakennetta niiden läpikäymiseen.


city_names = []

for _ in range(5):
    city = input('Syötä kaupungin nimi: ')
    city_names.append(city)

print('\nSyötettyjen kaupunkien nimet järjestyksessä: ')
for city in city_names:
    print(city)
