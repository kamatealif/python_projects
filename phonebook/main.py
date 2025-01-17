import psycopg2
import csv

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

def update_contact_name(old_name, new_name):
    cur.execute('''
        UPDATE phonebook
        SET name = %s
        WHERE name = %s
    ''', (new_name, old_name))
    conn.commit()

def find_contact_by_phone(phone):
    cur.execute('SELECT * FROM phonebook WHERE phone = %s', (phone,))
    return cur.fetchone()

def count_contacts():
    cur.execute('SELECT COUNT(*) FROM phonebook')
    return cur.fetchone()[0]

def export_contacts_to_csv(filename):
    contacts = get_contacts()
    with open(filename, 'w', newline='') as csvfile:
        fieldnames = ['id', 'name', 'phone']
        writer = csv.DictWriter(csvfile, fieldnames=fieldnames)
        
        writer.writeheader()
        for contact in contacts:
            writer.writerow({'id': contact[0], 'name': contact[1], 'phone': contact[2]})
    print(f"Contacts exported to {filename} successfully.")

def import_contacts_from_csv(filename):
    with open(filename, 'r') as csvfile:
        reader = csv.DictReader(csvfile)
        for row in reader:
            add_contact(row['name'], row['phone'])
    print(f"Contacts imported from {filename} successfully.")

def handle_add_contact():
    name = input("Enter name: ")
    phone = input("Enter phone number: ")
    add_contact(name, phone)
    print("Contact added successfully.")

def handle_find_contact():
    name = input("Enter name to find: ")
    contact = find_contact(name)
    if (contact):
        print(f"Found contact: {contact}")
    else:
        print("Contact not found.")

def handle_view_all_contacts():
    contacts = get_contacts()
    print("All contacts:")
    for contact in contacts:
        print(contact)

def handle_update_contact_phone():
    name = input("Enter name to update: ")
    new_phone = input("Enter new phone number: ")
    update_contact(name, new_phone)
    print("Contact updated successfully.")

def handle_delete_contact():
    name = input("Enter name to delete: ")
    delete_contact(name)
    print("Contact deleted successfully.")

def handle_view_recent_contacts():
    limit = int(input("Enter number of recent contacts to view: "))
    contacts = get_recent_contacts(limit)
    print("Recent contacts:")
    for contact in contacts:
        print(contact)

def handle_update_contact_name():
    old_name = input("Enter current name: ")
    new_name = input("Enter new name: ")
    update_contact_name(old_name, new_name)
    print("Contact name updated successfully.")

def handle_find_contact_by_phone():
    phone = input("Enter phone number to find: ")
    contact = find_contact_by_phone(phone)
    if (contact):
        print(f"Found contact: {contact}")
    else:
        print("Contact not found.")

def handle_count_contacts():
    total_contacts = count_contacts()
    print(f"Total contacts: {total_contacts}")

def handle_export_contacts_to_csv():
    filename = input("Enter filename to export contacts (e.g., contacts.csv): ")
    export_contacts_to_csv(filename)

def handle_import_contacts_from_csv():
    filename = input("Enter filename to import contacts (e.g., contacts.csv): ")
    import_contacts_from_csv(filename)

def menu():
    while True:
        print("\nPhonebook Menu:")
        print("1. Add Contact")
        print("2. Find Contact by Name")
        print("3. View All Contacts")
        print("4. Update Contact Phone")
        print("5. Delete Contact")
        print("6. View Recent Contacts")
        print("7. Update Contact Name")
        print("8. Find Contact by Phone")
        print("9. Count Contacts")
        print("10. Export Contacts to CSV")
        print("11. Import Contacts from CSV")
        print("12. Exit")
        
        choice = input("Enter your choice: ")
        
        if choice == '1':
            handle_add_contact()
        elif choice == '2':
            handle_find_contact()
        elif choice == '3':
            handle_view_all_contacts()
        elif choice == '4':
            handle_update_contact_phone()
        elif choice == '5':
            handle_delete_contact()
        elif choice == '6':
            handle_view_recent_contacts()
        elif choice == '7':
            handle_update_contact_name()
        elif choice == '8':
            handle_find_contact_by_phone()
        elif choice == '9':
            handle_count_contacts()
        elif choice == '10':
            handle_export_contacts_to_csv()
        elif choice == '11':
            handle_import_contacts_from_csv()
        elif choice == '12':
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