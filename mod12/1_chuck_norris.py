import requests

try:
    result = requests.get('https://api.chucknorris.io/jokes/random')
    if result.status_code == 200:
        result_json = result.json()
        print(result_json['value'])

except requests.exceptions.RequestException as e:
    print('Error')
