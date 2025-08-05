# Parent Class: Library
class Library:
    def __init__(self, book_list):
        self.available_books = book_list

    def display_books(self):
        print(" Available Books:")
        for book in self.available_books:
            print(f"- {book}")

    def borrow_book(self, book_name):
        if book_name in self.available_books:
            self.available_books.remove(book_name)
            print(f" You have borrowed '{book_name}'. Enjoy reading!")
        else:
            print(f"Sorry, '{book_name}' is not available.")

    def return_book(self, book_name):
        self.available_books.append(book_name)
        print(f"Thanks for returning '{book_name}'!")

# Child Class: User (inherits Library)
class User(Library):
    def __init__(self, book_list):
        super().__init__(book_list)

    def request_book(self):
        book = input("\nEnter the name of the book you want to borrow: ")
        self.borrow_book(book)

    def return_book_user(self):
        book = input("\nEnter the name of the book you want to return: ")
        self.return_book(book)

# Main Program
def main():
    library_books = ["Harry Potter", "The Alchemist", "Rich Dad Poor Dad", "Python Basics"]
    user = User(library_books)

    while True:
        print(" Library Menu ")
        print("1. Display available books")
        print("2. Borrow a book")
        print("3. Return a book")
        print("4. Exit")

        choice = input("Enter your choice (1-4): ")

        if choice == '1':
            user.display_books()
        elif choice == '2':
            user.request_book()
        elif choice == '3':
            user.return_book_user()
        elif choice == '4':
            print("Thank you for using the Library System!")
            break
        else:
            print("Invalid choice. Please try again.")

if __name__ =="__main__":
    main()
