def is_prime(number):
    """
    Check if a number is prime.

    Parameters:
    - number (int): The number to check.

    Returns:
    - bool: True if the number is prime, False otherwise.
    """
    if number > 1:
        # Check if the number is divisible by any number between 2 and the number
        for i in range(2, number):
            if number % i == 0:
                return False
        return True
    else:
        return False

def get_prime_factors(number):
    """
    Get the prime factors of a number.

    Parameters:
    - number (int): The number to factor.

    Returns:
    - list: A list of the prime factors of the number.
    """
    factors = []
    for i in range(2, number):
        while number % i == 0:
            factors.append(i)
            number //= i
    if number > 1:
        factors.append(number)
    return factors

def get_next_prime(number):
    """
    Get the next prime number.

    Parameters:
    - number (int): The number to start from.

    Returns:
    - int: The next prime number.
    """
    number += 1
    while not is_prime(number):
        number += 1
    return number

def get_previous_prime(number):
    """
    Get the previous prime number.

    Parameters:
    - number (int): The number to start from.

    Returns:
    - int: The previous prime number.
    """
    number -= 1
    while not is_prime(number):
        number -= 1
    return number

def main():
    """
    The main function of the program.

    This function displays a menu and allows the user to interact with the program.

    Parameters:
    - None

    Returns:
    - None
    """
    while True:
        print("\nPrime Number Checker")
        print("1. Check if a number is prime")
        print("2. Get prime factors of a number")
        print("3. Get the next prime number")
        print("4. Get the previous prime number")
        print("5. Quit")

        choice = input("Enter your choice: ")

        if choice == "1":
            number = int(input("Enter a number: "))
            if is_prime(number):
                print(f"{number} is a prime number")
            else:
                print(f"{number} is not a prime number")
                factors = get_prime_factors(number)
                print(f"The prime factors are: {factors}")
        elif choice == "2":
            number = int(input("Enter a number: "))
            factors = get_prime_factors(number)
            print(f"The prime factors are: {factors}")
        elif choice == "3":
            number = int(input("Enter a number: "))
            next_prime = get_next_prime(number)
            print(f"The next prime number is: {next_prime}")
        elif choice == "4":
            number = int(input("Enter a number: "))
            previous_prime = get_previous_prime(number)
            print(f"The previous prime number is: {previous_prime}")
        elif choice == "5":
            print("Goodbye!")
            break
        else:
            print("Invalid choice. Please try again.")

if __name__ == "__main__":
    main()