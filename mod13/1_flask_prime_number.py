from flask import Flask, Response, request, render_template
import json


def get_is_prime_number(number):
    is_prime_number = True
    if number <= 1:
        is_prime_number = False

    for num in range(2, number - 1):
        if number % num == 0:
            is_prime_number = False
    return is_prime_number


app = Flask(__name__)
@app.route('/alkuluku/<luku>')
def alkuluku(luku):
    try:
        """
        # kysely selaimessa http://127.0.0.1:3000/alkuluku?luku=5
        args = request.args
        luku = float(args.get('luku'))
        """
        luku = int(luku)

        tilakoodi = 200
        vastaus = {
            'Number': luku,
            'isPrime': bool(get_is_prime_number(luku)),
        }
    except ValueError:
        tilakoodi = 400
        vastaus = {
            'status': tilakoodi,
            'teksti': 'Virheellinen luku',
        }

    jsonvast = json.dumps(vastaus)
    return Response(response=jsonvast, status=tilakoodi, mimetype='application/json')


@app.errorhandler(404)
def page_not_found(virhekoodi):
    return render_template('error404.html'), 404
    """
    vastaus = {
        'status': '404',
        'teksti': 'Virheellinen päätepiste',
    }
    
    jsonvast = json.dumps(vastaus)
    return Response(response=jsonvast, status=404, mimetype='application/json')
    """


if __name__ == '__main__':
    app.run(use_reloader=True, host='127.0.0.1', port=3000)
