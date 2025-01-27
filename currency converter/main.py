import requests
import json

# Define a function to display the menu
def display_menu():
    print("\n")
    print("Currency Converter Menu:")
    print("1. Convert Currency")
    print("2. Show Country Currencies")
    print("3. Show All Exchange Rates")
    print("4. Fetch and Save Exchange Rates")
    print("5. Exit")

# Define a function to convert currency
def convert_currency(amount, from_currency, to_currency):
    try:
        
        url = f"https://moneymorph.dev/api/convert/{amount}/{from_currency}/{to_currency}"
        response = requests.get(url)
        if response.status_code == 200:
            data = response.json()
        else:
            print("Failed to fetch conversion data. Please try again.")
            return
    

        print("Conversion Result:")
        print(f"From: {data['request']['from']}")
        print(f"To: {data['request']['to']}")
        print(f"Amount: {data['request']['amount']}")
        print(f"Rate: {data['response']}")
        print(f"Total amount: {float(data['request']['amount']) * data['response']}")
    except Exception as e:
        print(f"An error occurred: {e}")

# Define a function to show country currencies
def show_country_currencies():
    try:
        url = "https://moneymorph.dev/api/currencies"
        response = requests.get(url)
        if response.status_code == 200:
            data = response.json()
            print("Country Currencies:")
            for country, currency in data.items():
                print(f"{country}: {currency}")
        else:
            print("Failed to fetch country-currency data. Please try again.")
    except Exception as e:
        print(f"An error occurred: {e}")

# Define a function to show all exchange rates
def show_all_exchange_rates():
    try:
        url = "https://moneymorph.dev/api/latest"
        response = requests.get(url)
        if response.status_code == 200:
            data = response.json()
        else:
            print("Failed to fetch exchange rates. Please try again.")
            return
    
        

        print("Exchange Rates:")
        print(f"Base Currency: {data['base']}")
        rates = data['rates']
        for country, currency in rates.items():
            print(f"{country}: {currency}")
    except Exception as e:
        print(f"An error occurred: {e}")

# Define a function to load stored exchange rates
def load_exchange_rates():
    try:
        with open("exchange_rates.json", "r") as f:
            data = json.load(f)
            return data
    except FileNotFoundError:
        return None

# Define the main function
def main():

    while True:
        display_menu()
        choice = input("Enter your choice: ")

        match choice:
            case "1":
                amount = input("Enter the amount to convert: ")
                if not amount.replace('.', '', 1).isdigit():
                    print("Invalid amount. Please enter a number.")
                    continue
                from_currency = input("Enter the from currency (e.g. USD, EUR, etc.): ").upper()
                to_currency = input("Enter the to currency (e.g. USD, EUR, etc.): ").upper()

                if not from_currency and not to_currency:
                    print("Currency codes cannot be empty.")
                    continue

                convert_currency(amount, from_currency, to_currency)
               
            case "2":
                show_country_currencies()
            case "3":
                show_all_exchange_rates()
            case "4":
                print("Fetching exchange rates...")
                url = "https://moneymorph.dev/api/latest"
                response = requests.get(url)
                if response.status_code == 200:
                    data = response.json()
                    print("Exchange rates fetched successfully!")
                    print("Saving to exchange_rates.json...")
                    with open("exchange_rates.json", "w") as f:
                        json.dump(data, f)
                    print("Exchange rates saved successfully!")
                else:
                    print("Failed to fetch exchange rates. Please try again.")
            case "5":
                exit()
            case _:
                print("Invalid choice. Please try again.")

if __name__ == "__main__":
    main()