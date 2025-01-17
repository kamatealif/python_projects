import json
import os

class ExpenseTracker:
    def __init__(self, filename='expenses.json'):
        self.filename = filename
        self.expenses = self.load_expenses()

    def load_expenses(self):
        if os.path.exists(self.filename):
            with open(self.filename, 'r') as file:
                return json.load(file)
        return []

    def save_expenses(self):
        with open(self.filename, 'w') as file:
            json.dump(self.expenses, file, indent=4)

    def add_expense(self, description, amount):
        expense = {'description': description, 'amount': amount}
        self.expenses.append(expense)
        self.save_expenses()

    def delete_expense(self, index):
        if 0 <= index < len(self.expenses):
            del self.expenses[index]
            self.save_expenses()

    def list_expenses(self):
        for i, expense in enumerate(self.expenses):
            print(f"{i}. {expense['description']} - ${expense['amount']}")

def main():
    tracker = ExpenseTracker()

    while True:
        print("\nExpense Tracker")
        print("1. Add Expense")
        print("2. Delete Expense")
        print("3. List Expenses")
        print("4. Exit")
        choice = input("Choose an option: ")

        if choice == '1':
            description = input("Enter description: ")
            amount = float(input("Enter amount: "))
            tracker.add_expense(description, amount)
        elif choice == '2':
            tracker.list_expenses()
            index = int(input("Enter the index of the expense to delete: "))
            tracker.delete_expense(index)
        elif choice == '3':
            tracker.list_expenses()
        elif choice == '4':
            break
        else:
            print("Invalid choice. Please try again.")

if __name__ == '__main__':
    main()