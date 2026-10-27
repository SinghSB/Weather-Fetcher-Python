#Requests module will help us fetch info from the internet
import requests 

#Creating a function to fetch weather data for a given city
def weather_fetcher(target_city):
    url = "https://wttr.in/" + target_city
    #Handles errors that may occur due to network issues or invalid city names
    try:
        response = requests.get(url)
        print(response.text)
        response.raise_for_status()  # Raise an error for bad responses
    except requests.RequestException as e:
        print(f"Error fetching weather data for {target_city}: {e}")

#While loops so that the app does not close after one search and allows the user to search for multiple cities
while True:
    user_input = input("Enter a city name or type 'quit' to exit: ")
    if user_input.lower() == 'quit':
        break
    weather_fetcher(user_input)
