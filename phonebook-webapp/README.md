# Phonebook App with Flask

A simple Phonebook application built using Flask and SQLAlchemy to manage contacts. Users can add, edit, view, and delete contacts, with data stored in an SQLite database.

## Features

- Add a new contact (name, phone, email, address).
- Edit existing contact details.
- Delete a contact.
- View a list of all contacts.

## Technologies Used

- **Flask**: A micro web framework for Python.
- **SQLAlchemy**: ORM (Object Relational Mapper) for database interactions.
- **SQLite**: Lightweight database for storing contact information.

## Requirements

Before running the app, ensure that you have the following installed:

- Python 3.x
- Flask
- SQLAlchemy

## Installation

1. Clone the repository:

   ```bash
   git clone https://github.com/kamatealif/python-projects/phonebook-webapp.git
   cd phonebook-webapp

2. Install the Required Dependencies
    ```sh
    pip install -r requirements.txt
    ```
    or
    ```bash
    pip install flask flask_sqlalchemy
    ```
3. Setup

    1. Create the database:

        Run the following code in a Python shell to create the SQLite database and necessary tables:
        ```python 
        from app import db
        db.create_all()
        ```
    2. Run the Flask app
        ```python
        python app.py
        ```
        By default, the app will run on http://127.0.0.1:5000/.

4. Usage
* Home page (/home): Displays a list of all contacts stored in the phonebook.
* Add contact (/add): Use the form to add a new contact to the phonebook.
* Edit contact (/edit/<int:id>): Edit the details of an existing contact.
* Delete contact (/delete/<int:id>): Delete a contact from the phonebook.