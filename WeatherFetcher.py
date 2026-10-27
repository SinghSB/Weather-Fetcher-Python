import requests

def weather_fetcher(target_city):
    url = "https://wttr.in/" + target_city
    try:
        response = requests.get(url)
        print(response.text)
        response.raise_for_status()  # Raise an error for bad responses
    except requests.RequestException as e:
        print(f"Error fetching weather data for {target_city}: {e}")

while True:
    user_input = input("Enter a city name or type 'quit' to exit: ")
    if user_input.lower() == 'quit':
        break
    weather_fetcher(user_input)
