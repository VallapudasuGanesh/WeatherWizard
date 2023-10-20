import requests

def get_weather(api_key, city):
    url = f'http://api.openweathermap.org/data/2.5/weather?q={city}&appid={api_key}&units=metric'
    response = requests.get(url)
    data = response.json()
    return data

def display_weather(data):
    if data['cod'] == '404':
        print('City not found')
    else:
        city = data['name']
        country = data['sys']['country']
        temp = data['main']['temp']
        description = data['weather'][0]['description']
        print(f'Weather in {city}, {country}:')
        print(f'Temperature: {temp}°C')
        print(f'Description: {description}')

if __name__ == '__main__':
    api_key = 'faa15aea2b75a282752b5e251cbf354d'  # Replace with your actual API key
    city = input('Enter city name: ')
    weather_data = get_weather(api_key, city)
    display_weather(weather_data)
