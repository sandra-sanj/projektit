import requests
import json


api_key = False
kelvin = 273.15

city_name = input('Enter city name: ')

try:
    request = f'https://api.openweathermap.org/data/2.5/weather?q={city_name}&appid={api_key}'
    result = requests.get(request)

    if result.status_code == 200:
        json_result = result.json()

        temperature = json_result['main']['temp']
        temperature_celcius = temperature - kelvin
        weather_description = json_result['weather'][0]['description']
        print(f'{weather_description.capitalize()}, {round(temperature_celcius, 1)}°C')

except requests.exceptions.RequestException as e:
    print(e)
