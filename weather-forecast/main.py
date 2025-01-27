# weather forecast cli tool too get the weather forecast of a city by entering the city name
import requests
import json


def menu():
    print("1. Enter the city name: ")
    print("2. Exit")

def show_weather(city_name):
    url = f"https://wttr.in/{city_name}?format=j1"
    try:
        response = requests.get(url)
        if response.status_code == 200:
            data = response.json()
            if "weather" in data:
                print("Weather Information:")
                print("---------------------")
                print(f"Location:")
                print(f"  Country: {data['nearest_area'][0]['country'][0]['value']}")
                print(f"  City: {data['nearest_area'][0]['areaName'][0]['value']}")
                print(f"  Region: {data['nearest_area'][0]['region'][0]['value']}")
                print()
                print("Current Weather:")
                print(f"  Temperature: {data['current_condition'][0]['temp_C']}°C")
                print(f"  Condition: {data['current_condition'][0]['weatherDesc'][0]['value']}")
                print(f"  Humidity: {data['current_condition'][0]['humidity']}%")
                print(f"  Wind: {data['current_condition'][0]['windspeedKmph']} Km/h")
                print(f"  Pressure: {data['current_condition'][0]['pressure']} hPa")
                print(f"  Visibility: {data['current_condition'][0]['visibility']} km")
                print(f"  Precipitation: {data['current_condition'][0]['precipMM']} mm")
                print()
                print("Astronomical Information:")
                print(f"  Sunrise: {data['weather'][0]['astronomy'][0]['sunrise']}")
                print(f"  Sunset: {data['weather'][0]['astronomy'][0]['sunset']}")
                print()
                print(f"Last Updated: {data['current_condition'][0]['observation_time']}")
            else:
                print("City not found!")
        else:
            print("Error fetching data!")
    except Exception as e:
        print(f"Error: {str(e)}")


def main():
    while True:
        menu()
        choice = input("Enter your choice: ")
        if choice == "1":
            city_name = input("Enter the city name:").strip()
            if not city_name.isalpha():
                print(f"Error: Please enter a valid city name.")
                continue
            show_weather(city_name);

if __name__ == "__main__":
    main();