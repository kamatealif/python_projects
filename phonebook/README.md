# Phonebook Application

This is a simple phonebook application implemented in Python using PostgreSQL as the database. It allows you to add, view, update, delete, and search for contacts in the phonebook. Additionally, you can export and import contacts to/from a CSV file.

## Features

- Add a contact to the phonebook
- View all contacts in the phonebook
- Find a contact by name
- Update a contact's phone number
- Delete a contact from the phonebook
- View recent contacts
- Update a contact's name
- Find a contact by phone number
- Count the total number of contacts
- Export contacts to a CSV file
- Import contacts from a CSV file

## Requirements

- Python 3.x
- PostgreSQL
- psycopg2 library

## Installation

1. Clone the repository or download the script.
2. Navigate to the directory containing the script.
3. Install the required library:

    ```sh
    pip install psycopg2
    ```

4. Set up your PostgreSQL database and update the connection details in the script:

    ```python
    conn = psycopg2.connect(
        dbname="your_dbname",
        user="your_username",
        password="your_password",
        host="your_host",
        port="your_port"
    )
    ```

## Usage

1. Run the script using Python:

    ```sh
    python main.py
    ```

2. Follow the on-screen instructions to interact with the phonebook application.

## Example

```sh
Phonebook Menu:
1. Add Contact
2. Find Contact by Name
3. View All Contacts
4. Update Contact Phone
5. Delete Contact
6. View Recent Contacts
7. Update Contact Name
8. Find Contact by Phone
9. Count Contacts
10. Export Contacts to CSV
11. Import Contacts from CSV
12. Exit
Enter your choice: 1
Enter name: Alice
Enter phone number: 123-456-7890
Contact added successfully.

Phonebook Menu:
1. Add Contact
2. Find Contact by Name
3. View All Contacts
4. Update Contact Phone
5. Delete Contact
6. View Recent Contacts
7. Update Contact Name
8. Find Contact by Phone
9. Count Contacts
10. Export Contacts to CSV
11. Import Contacts from CSV
12. Exit
Enter your choice: 3
All contacts:
(1, 'Alice', '123-456-7890')