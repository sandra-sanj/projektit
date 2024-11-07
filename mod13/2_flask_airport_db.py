import mysql.connector
from flask import Flask, Response, request, render_template
import json


connection = mysql.connector.connect(
    host='localhost',
    port= 3306,
    database='flight_game',
    user='sandra',
    password='humanbye',
    autocommit=True,
    collation='utf8mb4_general_ci'
)


def get_airport_info_by_icao(airport_icao):
    sql = f'SELECT name, municipality from airport where ident="{airport_icao}"'

    cursor = connection.cursor()
    cursor.execute(sql)
    result = cursor.fetchone()

    if not result: return False

    name = result[0]
    municipality = result[1]
    return name, municipality


app = Flask(__name__)
@app.route('/kentta/<icao>')
def kentta(icao):
    try:
        icao = str(icao)
        name, municipality = get_airport_info_by_icao(icao)

        tilakoodi = 200
        vastaus = {
            'ICAO': icao,
            'Name': name,
            'Municipality': municipality,
        }
    except ValueError:
        tilakoodi = 400
        vastaus = {
            'status': tilakoodi,
            'teksti': 'Virheellinen icao',
        }
    jsonvast = json.dumps(vastaus)
    return Response(response=jsonvast, status=tilakoodi, mimetype='application/json')


@app.errorhandler(404)
def page_not_found(virhekoodi):
    return render_template('error404.html'), 404


if __name__ == '__main__':
    app.run(use_reloader=True, host='127.0.0.1', port=3000)
