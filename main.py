# Write a python program to translate a message into secored code language. use the rules below to translate normal english into secore code language.

# InCoding rules:
# if:
# the word contanins at least 3 character, remove the first letter and append it at the end . now append three characters at the starting and the end of the word.
# else:
# simply reverse the string

# decoding
# if the word contains greater than 3 character, reverse it,
# else:
# remove 3 random character from the start and end. Now remove the last letter and append it at the starting of the word.

import os
import random
import sys

CSI = "\033["
RESET = CSI + "0m"
BOLD = CSI + "1m"
BLUE = CSI + "94m"
GREEN = CSI + "92m"
YELLOW = CSI + "93m"
RED = CSI + "91m"

RANDOM_POOL = "ABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqrstuvwxyz"


def encode(message: str) -> str:
    """Encode message:
    - If len(message) >= 3: move first char to end and add 3 random chars to front and back.
    - Else: reverse the message.
    """
    message = message or ""
    start = "".join(random.sample(RANDOM_POOL, k=3))
    end = "".join(random.sample(RANDOM_POOL, k=3))
    if len(message) >= 3:
        first = message[0]
        encoded = start + message[1:] + first + end
    else:
        encoded = message[::-1]
    return encoded


def decode(message: str) -> str:
    """Decode message:
    - If len(message) > 6: strip 3-char padding on both sides then move last char to front.
    - Else: reverse the message.
    """
    message = message or ""
    if len(message) > 6:  # has padding
        middle = message[3:-3]
        if middle:
            decoded = middle[-1] + middle[:-1]
        else:
            decoded = ""
    else:
        decoded = message[::-1]
    return decoded


def print_header():
    try:
        width = os.get_terminal_size().columns
    except OSError:
        width = 60
    title = "SECORE CODE TRANSLATOR"
    print(BOLD + BLUE + title.center(width) + RESET)
    print("-" * min(width, 60))


def menu():
    print()
    print(f"{BOLD}Menu{RESET}")
    print(f"{GREEN}1{RESET}. Encode message")
    print(f"{GREEN}2{RESET}. Decode message")
    print(f"{GREEN}3{RESET}. Exit")
    print()


def prompt(message: str) -> str:
    try:
        return input(message)
    except (EOFError, KeyboardInterrupt):
        print()
        return ""


def main():
    try:
        while True:
            os.system("cls" if os.name == "nt" else "clear")
            print_header()
            menu()
            choice = prompt("Enter your choice [1-3]: ").strip()
            if choice == "1":
                msg = prompt("Enter message to encode: ").rstrip("\n")
                if not msg:
                    print(RED + "Empty input; nothing to encode." + RESET)
                else:
                    out = encode(msg)
                    print(GREEN + "\nEncoded:" + RESET, out)
                prompt("\nPress Enter to continue...")
            elif choice == "2":
                msg = prompt("Enter message to decode: ").rstrip("\n")
                if not msg:
                    print(RED + "Empty input; nothing to decode." + RESET)
                else:
                    out = decode(msg)
                    print(GREEN + "\nDecoded:" + RESET, out)
                prompt("\nPress Enter to continue...")
            elif choice == "3":
                print(YELLOW + "Goodbye!" + RESET)
                sys.exit(0)
            else:
                print(RED + "Invalid choice. Please enter 1, 2 or 3." + RESET)
                prompt("Press Enter to continue...")
    except KeyboardInterrupt:
        print("\n" + YELLOW + "Interrupted. Exiting." + RESET)
        sys.exit(0)


if __name__ == "__main__":
    main()
