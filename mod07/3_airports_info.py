# Kirjoita ohjelma lentoasematietojen hakemiseksi ja tallentamiseksi. Ohjelma kysyy käyttäjältä,
# haluaako tämä syöttää uuden lentoaseman, hakea jo syötetyn lentoaseman tiedot vai lopettaa.
# Jos käyttäjä valitsee uuden lentoaseman syöttämisen, ohjelma kysyy käyttäjältä lentoaseman ICAO-koodin ja nimen.
# Jos käyttäjä valitsee haun, ohjelma kysyy ICAO-koodin ja tulostaa sitä vastaavan lentoaseman nimen.
# Jos käyttäjä haluaa lopettaa, ohjelman suoritus päättyy.
# Käyttäjä saa valita uuden toiminnon miten monta kertaa tahansa aina siihen asti, kunnes hän haluaa lopettaa.
# (ICAO-koodi on lentoaseman yksilöivä tunniste. Esimerkiksi Helsinki-Vantaan lentoaseman ICAO-koodi on EFHK.
# Löydät koodeja helposti selaimen avulla.)


airports_database = dict()

def try_add_to_database(key, value):
    if key not in airports_database:
        airports_database[key] = value
        return True
    return False


def try_search_database(key):
    if key in airports_database:
        return airports_database[key]
    return False


print('Input and search airports from database')

user_command = False
while user_command != 'exit':
    user_command = input('\nInput one of the available commands (input, search, exit): ')

    if user_command == 'exit':
        continue

    elif user_command == 'input':
        airport_icoa_code = input('Enter airport ICOA code: ')
        airport_name = input('Enter airport name: ')

        result = try_add_to_database(airport_icoa_code, airport_name)
        if result:
            print('Added airport to database.')
        else:
            print('Airport already in database.')

    elif user_command == 'search':
        airport_icoa_code = input('Enter airport ICOA code to search: ')
        result = try_search_database(airport_icoa_code)

        if result:
            print(f'{airport_icoa_code}: {result}')
        else:
            print('Airport not found.')

    else:
        print('Unknown command.')

else:
    print('Exited program.')

print(f'Database contents: {airports_database}')
