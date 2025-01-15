class Library:
    def __init__(self):
        self.books = []

    def add_book(self, title, author):
        book = {'title': title, 'author': author, 'borrowed': False}
        self.books.append(book)
        print(f"Book '{title}' by {author} added to the library.")

    def view_books(self):
        if not self.books:
            print("No books in the library.")
            return
        for idx, book in enumerate(self.books, start=1):
            status = "Borrowed" if book['borrowed'] else "Available"
            print(f"{idx}. {book['title']} by {book['author']} - {status}")

    def borrow_book(self, title):
        for book in self.books:
            if book['title'].lower() == title.lower() and not book['borrowed']:
                book['borrowed'] = True
                print(f"You have borrowed '{title}'.")
                return
        print(f"Book '{title}' is not available.")

    def return_book(self, title):
        for book in self.books:
            if book['title'].lower() == title.lower() and book['borrowed']:
                book['borrowed'] = False
                print(f"You have returned '{title}'.")
                return
        print(f"Book '{title}' was not borrowed.")

def main():
    library = Library()
    while True:
        print("\nLibrary Management System")
        print("1. Add Book")
        print("2. View Books")
        print("3. Borrow Book")
        print("4. Return Book")
        print("5. Exit")
        choice = input("Enter your choice: ")

        if choice == '1':
            title = input("Enter book title: ")
            author = input("Enter book author: ")
            library.add_book(title, author)
        elif choice == '2':
            library.view_books()
        elif choice == '3':
            title = input("Enter book title to borrow: ")
            library.borrow_book(title)
        elif choice == '4':
            title = input("Enter book title to return: ")
            library.return_book(title)
        elif choice == '5':
            print("Exiting the system.")
            break
        else:
            print("Invalid choice. Please try again.")

if __name__ == "__main__":
    main()