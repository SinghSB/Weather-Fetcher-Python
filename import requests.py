import requests

def weather_fetcher():
    target_city = input("Enter a city name: ")
    url = "https://wttr.in/" + target_city
    response = requests.get(url)

    print(response)

weather_fetcher()