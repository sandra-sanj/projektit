# Kirjoita ohjelma, joka kysyy käyttäjältä maakoodin (esimerkiksi FI) ja tulostaa kyseisessä maassa olevien
# lentokenttien lukumäärät tyypeittäin. Esimerkiksi Suomen osalta tuloksena on saatava tieto siitä,
# että pieniä lentokenttiä on 65 kappaletta, helikopterikenttiä on 15 kappaletta jne.


import mysql.connector


def count_airports_in_country_by_types(country_code):
    sql = f'SELECT name, type from airport where iso_country="{country_code}"'

    cursor = connection.cursor()
    cursor.execute(sql)
    result = cursor.fetchall()

    if cursor.rowcount > 0:

        airports_by_type = {}

        for row in result:
            airport_name = row[0]
            airport_type = row[1]

            # make new key to dict if it does not exist, else add to existing value
            if airport_type not in airports_by_type:
                airports_by_type[airport_type] = [airport_name]
            else:
                airports_by_type[airport_type].append(airport_name)

        print(f'Airport types in country with code {country_code}:')
        # print airport counts by type
        for type in airports_by_type:
            print(f'{len(airports_by_type[type])} {type}')
    return


connection = mysql.connector.connect(host='localhost',
                                     port= 3306,
                                     database='flight_game',
                                     user='sandra',
                                     password='humanbye',
                                     autocommit=True,
                                     collation='utf8mb4_general_ci')

country_code = input('Enter country code: ')
count_airports_in_country_by_types(country_code)

