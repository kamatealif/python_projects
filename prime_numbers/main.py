from collections import Counter
import math

def is_prime(number):
    """
    Check if a number is prime.

    Parameters:
    - number (int): The number to check.

    Returns:
    - bool: True if the number is prime, False otherwise.
    """
    if number < 2:
        return False
    if number in (2, 3):
        return True
    if number % 2 == 0 or number % 3 == 0:
        return False
    for i in range(5, int(math.sqrt(number)) + 1, 2):
        if number % i == 0:
            return False
    return True

def get_prime_factors(number):
    """
    Get the prime factors of a number.

    Parameters:
    - number (int): The number to factor.

    Returns:
    - list: A list of the prime factors of the number.
    """
    factors = []
    for i in range(2, int(math.sqrt(number)) + 1):
        while number % i == 0:
            factors.append(i)
            number //= i
    if number > 1:
        factors.append(number)
    return factors

def prime_factorization(number):
    """
    Get the prime factorization of a number in exponential form.

    Parameters:
    - number (int): The number to factor.

    Returns:
    - str: The prime factorization in the form "2^3 * 3^2".
    """
    factors = get_prime_factors(number)
    count = Counter(factors)
    return " * ".join([f"{factor}^{count[factor]}" if count[factor] > 1 else str(factor) for factor in count])

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
    - int: The previous prime number or None if no such prime exists.
    """
    number -= 1
    while number > 1 and not is_prime(number):
        number -= 1
    return number if number > 1 else None

def get_primes_in_range(start, end):
    """
    Get all prime numbers in a given range.

    Parameters:
    - start (int): The starting number.
    - end (int): The ending number.

    Returns:
    - list: A list of prime numbers in the range.
    """
    return [num for num in range(start, end + 1) if is_prime(num)]

def generate_n_primes(n):
    """
    Generate the first N prime numbers.

    Parameters:
    - n (int): The number of prime numbers to generate.

    Returns:
    - list: A list of the first N prime numbers.
    """
    primes = []
    num = 2
    while len(primes) < n:
        if is_prime(num):
            primes.append(num)
        num += 1
    return primes

def is_twin_prime(n):
    """
    Check if a number is part of a twin prime pair.

    Parameters:
    - n (int): The number to check.

    Returns:
    - bool: True if it is a twin prime, False otherwise.
    """
    return is_prime(n) and (is_prime(n - 2) or is_prime(n + 2))

def goldbach_pairs(n):
    """
    Get Goldbach pairs for an even number.

    Parameters:
    - n (int): An even number >= 4.

    Returns:
    - list: A list of tuples representing prime pairs.
    """
    if n % 2 != 0 or n < 4:
        return []
    return [(p, n - p) for p in range(2, n//2 + 1) if is_prime(p) and is_prime(n - p)]

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
        print("\nPrime Number Utilities")
        print("1. Check if a number is prime")
        print("2. Get prime factors of a number")
        print("3. Get prime factorization (exponential form)")
        print("4. Get the next prime number")
        print("5. Get the previous prime number")
        print("6. List prime numbers in a range")
        print("7. Generate the first N prime numbers")
        print("8. Check if a number is a twin prime")
        print("9. Get Goldbach pairs for an even number")
        print("10. Quit")

        choice = input("Enter your choice: ")

        if choice == "1":
            number = int(input("Enter a number: "))
            if is_prime(number):
                print(f"{number} is a prime number")
            else:
                print(f"{number} is not a prime number")
        elif choice == "2":
            number = int(input("Enter a number: "))
            factors = get_prime_factors(number)
            print(f"The prime factors are: {factors}")
        elif choice == "3":
            number = int(input("Enter a number: "))
            factorization = prime_factorization(number)
            print(f"Prime factorization: {factorization}")
        elif choice == "4":
            number = int(input("Enter a number: "))
            next_prime = get_next_prime(number)
            print(f"The next prime number is: {next_prime}")
        elif choice == "5":
            number = int(input("Enter a number: "))
            previous_prime = get_previous_prime(number)
            if previous_prime:
                print(f"The previous prime number is: {previous_prime}")
            else:
                print("There is no prime number before 2.")
        elif choice == "6":
            start = int(input("Enter start of range: "))
            end = int(input("Enter end of range: "))
            primes = get_primes_in_range(start, end)
            print(f"Prime numbers in range {start}-{end}: {primes}")
        elif choice == "7":
            n = int(input("Enter how many prime numbers you want: "))
            primes = generate_n_primes(n)
            print(f"The first {n} prime numbers are: {primes}")
        elif choice == "8":
            number = int(input("Enter a number: "))
            if is_twin_prime(number):
                print(f"{number} is a twin prime.")
            else:
                print(f"{number} is not a twin prime.")
        elif choice == "9":
            number = int(input("Enter an even number: "))
            pairs = goldbach_pairs(number)
            if pairs:
                print(f"Goldbach pairs for {number}: {pairs}")
            else:
                print("Goldbach's Conjecture is only for even numbers >= 4.")
        elif choice == "10":
            print("Goodbye!")
            break
        else:
            print("Invalid choice. Please try again.")

if __name__ == "__main__":
    main()
