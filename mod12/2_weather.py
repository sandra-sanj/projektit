import requests
import json


api_key = False
units = 'metric'
language = 'FI'

city_name = "york" #input('Enter city name: ')

try:
    request = f'https://api.openweathermap.org/data/2.5/weather?q={city_name}&appid={api_key}&units={units}&lang={language}'
    result = requests.get(request)

    if result.status_code == 200:
        json_result = result.json()

        # print json result with indents
        #print(json.dumps(json_result, indent=2))

        temperature = json_result['main']['temp']
        weather_description = json_result['weather'][0]['description']
        print(f'{weather_description.capitalize()}, {round(temperature, 1)}°C')

except requests.exceptions.RequestException as e:
    print(e)
