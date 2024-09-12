# Kirjoita ohjelma, joka kysyy käyttäjältä kahden lentokentän ICAO-koodit. Ohjelma ilmoittaa lentokenttien välisen
# etäisyyden kilometreinä. Laskenta perustuu tietokannasta haettuihin koordinaatteihin.
# Laske etäisyys geopy-kirjaston avulla.

import mysql.connector
import geopy.distance


def get_airport_name_and_coordinates_by_icao(airport_icao):
    sql = f'SELECT name, latitude_deg, longitude_deg from airport where ident="{airport_icao}"'

    cursor = connection.cursor()
    cursor.execute(sql)
    result = cursor.fetchone()

    if cursor.rowcount == 1:
        for row in result:
            return row[0], row[1], row[2]  # name, latitude, longtitude
    return False, False, False


def get_distance_between_two_airports(airport1_icao, airport2_icao):
    airport1_name, airport1_latitude, airport1_longitude = get_airport_name_and_coordinates_by_icao(airport1_icao)
    airport2_name, airport2_latitude, airport2_longitude = get_airport_name_and_coordinates_by_icao(airport2_icao)

    if not airport1_name:
        return print('Unknown first airport')
    if not airport2_name:
        return print('Unknown second airport')
    if airport1_icao == airport2_icao:
        return print('Airports are the same')

    # transform distance (km) into float
    distance_km = geopy.distance.distance((airport1_latitude, airport1_longitude),
                                          (airport2_latitude, airport2_longitude)).km

    print(f'Distance between {airport1_name} and {airport2_name} is {round(distance_km.km, 2)} km')
    return


connection = mysql.connector.connect(host='localhost',
                                     port= 3306,
                                     database='flight_game',
                                     user='sandra',
                                     password='humanbye',
                                     autocommit=True,
                                     collation='utf8mb4_general_ci')

airport1_icao = input('Enter first airport ICAO code: ')
airport2_icao = input('Enter second airport ICAO code: ')
get_distance_between_two_airports(airport1_icao, airport2_icao)
