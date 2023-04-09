import requests
import random
import time

api_key = '4e22f203135d43af2e8096b046560020'
cities = ['New York','Bahamas','Tokyo', 'Toronto', 'Miami', 'Germany', 'Portugal','China']


def get_temp(city):
    url = f'http://api.openweathermap.org/data/2.5/weather?q={city}&appid={"4e22f203135d43af2e8096b046560020"}&units=metric'
    response = requests.get(url)

    if response.status_code == 200:
        data = response.json()
        temperature = data['main']['temp']
        print(f'The current temperature in {city} is {temperature} degrees Celsius.')
        if city not in cities:  # Adds User picked city to the list of cities if it isn't in list
            cities.append(city) 
    else:
        print(f'Error fetching weather for {city}: {response.status_code} {response.reason}')

city = input('Enter a city or country name: ')

get_temp(city)

while True:
    choice = input('Would you like to see the temperature for another city?\nEnter "yes" or "no"\n')

    if choice.lower() == 'yes':
        get_temp(city)
    elif choice.lower() == 'no':
        print("As per my programming, I will show you a random temp from the list...")
        city = random.choice(cities)
        get_temp(city)
        time.sleep(3)
        print("This is the updated list: ")
        print(cities)
    else:
        print('Invalid choice.  Please enter "yes" or "no".')


