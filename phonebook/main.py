import psycopg2

# Connect to PostgreSQL database
conn = psycopg2.connect(
    dbname="your_dbname",
    user="your_username",
    password="your_password",
    host="your_host",
    port="your_port"
)
cur = conn.cursor()

# Create phonebook table
cur.execute('''
    CREATE TABLE IF NOT EXISTS phonebook (
        id SERIAL PRIMARY KEY,
        name VARCHAR(100),
        phone VARCHAR(15)
    )
''')
conn.commit()

def add_contact(name, phone):
    cur.execute('''
        INSERT INTO phonebook (name, phone)
        VALUES (%s, %s)
    ''', (name, phone))
    conn.commit()

def get_contacts():
    cur.execute('SELECT * FROM phonebook')
    return cur.fetchall()

def find_contact(name):
    cur.execute('SELECT * FROM phonebook WHERE name = %s', (name,))
    return cur.fetchone()

def delete_contact(name):
    cur.execute('DELETE FROM phonebook WHERE name = %s', (name,))
    conn.commit()

# Example usage
add_contact('Alice', '123-456-7890')
add_contact('Bob', '987-654-3210')

print(get_contacts())
print(find_contact('Alice'))

delete_contact('Alice')
print(get_contacts())

# Close the connection
cur.close()
conn.close()
def update_contact(name, new_phone):
    cur.execute('''
        UPDATE phonebook
        SET phone = %s
        WHERE name = %s
    ''', (new_phone, name))
    conn.commit()

def get_recent_contacts(limit=5):
    cur.execute('SELECT * FROM phonebook ORDER BY id DESC LIMIT %s', (limit,))
    return cur.fetchall()

# Example usage
update_contact('Bob', '111-222-3333')
print(find_contact('Bob'))

print(get_recent_contacts())
def menu():
    while True:
        print("\nPhonebook Menu:")
        print("1. Add Contact")
        print("2. Find Contact by Name")
        print("3. View All Contacts")
        print("4. Update Contact")
        print("5. Delete Contact")
        print("6. View Recent Contacts")
        print("7. Exit")
        
        choice = input("Enter your choice: ")
        
        if choice == '1':
            name = input("Enter name: ")
            phone = input("Enter phone number: ")
            add_contact(name, phone)
            print("Contact added successfully.")
        elif choice == '2':
            name = input("Enter name to find: ")
            contact = find_contact(name)
            if contact:
                print(f"Found contact: {contact}")
            else:
                print("Contact not found.")
        elif choice == '3':
            contacts = get_contacts()
            print("All contacts:")
            for contact in contacts:
                print(contact)
        elif choice == '4':
            name = input("Enter name to update: ")
            new_phone = input("Enter new phone number: ")
            update_contact(name, new_phone)
            print("Contact updated successfully.")
        elif choice == '5':
            name = input("Enter name to delete: ")
            delete_contact(name)
            print("Contact deleted successfully.")
        elif choice == '6':
            limit = int(input("Enter number of recent contacts to view: "))
            contacts = get_recent_contacts(limit)
            print("Recent contacts:")
            for contact in contacts:
                print(contact)
        elif choice == '7':
            print("Exiting...")
            break
        else:
            print("Invalid choice. Please try again.")

if __name__ == "__main__":
    try:
        menu()
    finally:
        cur.close()
        conn.close()