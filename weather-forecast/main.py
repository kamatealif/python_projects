import requests

cache = {}

def menu():
    print("1. Enter the city name")
    print("2. Exit")

def show_weather(city_name):
    # Check if city is in cache
    if city_name.lower() in cache:
        print("Fetching data from cache...")
        data = cache[city_name.lower()]
    else:
        print("Fetching new data...")
        url = f"https://wttr.in/{city_name}?format=j1"
        try:
            response = requests.get(url)
            if response.status_code != 200:
                print("Error fetching data! Please check your internet connection.")
                return
            data = response.json()
            if "weather" not in data:
                print(f"Error: No weather information available for '{city_name}'.")
                return
            cache[city_name.lower()] = data  # Cache the result
        except Exception as e:
            print(f"Error: {str(e)}")
            return

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

def main():
    while True:
        menu()
        choice = input("Enter your choice: ")
        if choice == "1":
            city_name = input("Enter the city name: ").strip()
            if not city_name.isalpha():
                print("Error: Please enter a valid city name.")
                continue
            show_weather(city_name)
        elif choice == "2":
            confirm = input("Are you sure you want to exit? (yes/no): ").strip().lower()
            if confirm == "yes":
                break
        else:
            print("Invalid choice. Please try again.")

if __name__ == "__main__":
    main()
