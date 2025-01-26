# Import the necessary libraries
import requests
import json

# Define a function to display the menu
def menu():
    # Print the menu options
    print("\n")
    print("Currency Converter Menu:")
    print("1. Convert Currency")
    print("2. Show Country Currencies")
    print("3. Show All Exchange Rates")
    print("4. Exit")

# Define a function to convert currency
def convert(amount, from_currency, to_currency, data=None):
    """
    Convert currency using the online API or stored exchange rates.

    Args:
        amount (str): The amount to convert
        from_currency (str): The from currency
        to_currency (str): The to currency
        data (dict, optional): The stored exchange rates. Defaults to None.
    """
    try:
        # If data is None, use the online API to get the conversion data
        if data is None:
            url = f"https://moneymorph.dev/api/convert/{amount}/{from_currency}/{to_currency}"
            response = requests.get(url)
            if response.status_code == 200:
                data = response.json()
            else:
                print("Failed to fetch conversion data. Please try again.")
                return

        # Print the conversion result
        print(f"Conversion Result:")
        print(f"From: {data['request']['from']}")
        print(f"To: {data['request']['to']}")
        print(f"Amount: {data['request']['amount']}")
        print(f"Rate: {data['response']}")
        print(f"Total amount : {data['request']['amount'] * data['response']}")
    except Exception as e:
        # Print any errors that occur
        print(f"An error occurred: {e}")

# Define a function to show country currencies
def show_country_currency():
    """
    Show country currencies using the online API.
    """
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
def show_all_rates(data=None):
    """
    Show all exchange rates using the online API or stored exchange rates.

    Args:
        data (dict, optional): The stored exchange rates. Defaults to None.
    """
    try:
        # If data is None, use the online API to get the exchange rates
        if data is None:
            url = "https://moneymorph.dev/api/latest"
            response = requests.get(url)
            if response.status_code == 200:
                data = response.json()
            else:
                print("Failed to fetch exchange rates. Please try again.")
                return

        # Print the exchange rates
        print("Exchange Rates:")
        print(f"Base Currency: {data['base']}")
        rates = data['rates']
        for country, currency in rates.items():
            print(f"{country}: {currency}")
    except Exception as e:
        print(f"An error occurred: {e}")

# Define a function to load stored exchange rates
def load_exchange_rates():
    """
    Load stored exchange rates from the exchange_rates.json file.
    """
    try:
        with open("exchange_rates.json", "r") as f:
            data = json.load(f)
            return data
    except FileNotFoundError:
        return None

# Define the main function
def main():
    # Load stored exchange rates
    exchange_rates = load_exchange_rates()

    # Loop until the user chooses to exit
    while True:
        # Display the menu
        menu()

        # Get the user's choice
        choice = input("Enter your choice: ")

        # Handle the user's choice
        match choice:
            case "1":
                # Convert currency
                amount = input("Enter the amount to convert: ")
                if not amount.isdigit():
                    print("Invalid amount. Please enter a number.")
                    continue
                from_currency = input("Enter the from currency (e.g. USD, EUR, etc.): ").upper()
                to_currency = input("Enter the to currency (e.g. USD, EUR, etc.): ").upper()

                if not from_currency and not to_currency:
                    print("Currency codes cannot be empty.")
                    continue

                # Use stored exchange rates if available
                if exchange_rates is None:
                    convert(amount, from_currency, to_currency)
                else:
                    convert(amount, from_currency, to_currency, exchange_rates)
            case "2":
                # Show country currencies
                show_country_currency()
            case "3":
                # Show all exchange rates
                show_all_rates(exchange_rates)
            case "4":
                # Fetch and save exchange rates
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
                # Exit the program
                exit()
            case _:
                # Handle invalid choices
                print("Invalid choice. Please try again.")

# Run the main function
if __name__ == "__main__":
    main()