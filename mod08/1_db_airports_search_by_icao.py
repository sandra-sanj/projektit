# Kirjoita ohjelma, joka kysyy käyttäjältä lentoaseman ICAO-koodin. Ohjelma hakee ja tulostaa koodia vastaavan
# lentokentän nimen ja sen sijaintikunnan kurssilla käytettävästä lentokenttätietokannasta.
# ICAO-koodi on tallennettuna airport-taulun ident-sarakkeeseen.


import mysql.connector


def search_airport_by_icao(airport_icao):
    sql = f'SELECT name, municipality from airport where ident="{airport_icao}"'

    cursor = connection.cursor()
    cursor.execute(sql)
    result = cursor.fetchall()

    if cursor.rowcount > 0:
        for row in result:
            airport_name = row[0]
            airport_municipality = row[1]
            print(f'{airport_name} is located in {airport_municipality}')

    return


connection = mysql.connector.connect(host='localhost',
                                     port= 3306,
                                     database='flight_game',
                                     user='sandra',
                                     password='humanbye',
                                     autocommit=True,
                                     collation='utf8mb4_general_ci')

airport_icao = input('Enter airport ICAO code: ')
search_airport_by_icao(airport_icao)
