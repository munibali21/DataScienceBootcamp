import datetime

# Book class to represent a book
class Book:
    def __init__(self, book_id, title, author):
        self.book_id = book_id
        self.title = title
        self.author = author
        self.issued_to = None
        self.issue_date = None

# Library class to manage the books
class Library:
    def __init__(self):
        self.books = []

    def add_book(self, book):
        self.books.append(book)
        print("Book added successfully.")

    def issue_book(self, book_id, student_id):
        book = self.find_book(book_id)
        if book:
            if book.issued_to:
                print("Book already issued to another student.")
            else:
                book.issued_to = student_id
                book.issue_date = datetime.date.today()
                print("Book issued successfully.")
        else:
            print("Book not found.")

    def return_book(self, book_id):
        book = self.find_book(book_id)
        if book:
            if book.issued_to:
                book.issued_to = None
                book.issue_date = None
                print("Book returned successfully.")
            else:
                print("Book is not issued to any student.")
        else:
            print("Book not found.")

    def delete_book(self, book_id):
        book = self.find_book(book_id)
        if book:
            self.books.remove(book)
            print("Book deleted successfully.")
        else:
            print("Book not found.")

    def find_book(self, book_id):
        for book in self.books:
            if book.book_id == book_id:
                return book
        return None

    def search_book(self, book_id):
        book = self.find_book(book_id)
        if book:
            print("Book ID:", book.book_id)
            print("Title:", book.title)
            print("Author:", book.author)
            if book.issued_to:
                print("Issued to:", book.issued_to)
                print("Issue Date:", book.issue_date)
            else:
                print("Not issued to any student.")
        else:
            print("Book not found.")

    def show_books(self):
        if self.books:
            print("Books in the library:")
            for book in self.books:
                print("Book ID:", book.book_id)
                print("Title:", book.title)
                print("Author:", book.author)
                if book.issued_to:
                    print("Issued to:", book.issued_to)
                    print("Issue Date:", book.issue_date)
                else:
                    print("Not issued to any student.")
                print("-----")
        else:
            print("No books in the library.")

# Main function to run the library management system
def main():
    library = Library()

    while True:
        print("1. Add Book")
        print("2. Issue Book")
        print("3. Return Book")
        print("4. Delete Book")
        print("5. Search Book")
        print("6. Show Books")
        print("7. Exit")
        choice = input("Enter your choice (1-7): ")

        if choice == '1':
            book_id = input("Enter Book ID: ")
            title = input("Enter Title: ")
            author = input("Enter Author: ")
            book = Book(book_id, title, author)
            library.add_book(book)

        elif choice == '2':
            book_id = input("Enter Book ID: ")
            student_id = input("Enter Student ID: ")
            library.issue_book(book_id, student_id)

        elif choice == '3':
            book_id = input("Enter Book ID: ")
            library.return_book(book_id)

        elif choice == '4':
            book_id = input("Enter Book ID: ")
            library.delete_book(book_id)

        elif choice == '5':
            book_id = input("Enter Book ID: ")
            library.search_book(book_id)

        elif choice == '6':
            library.show_books()

        elif choice == '7':
            print("Exiting... Thank you!")
            break

        else:
            print("Invalid choice. Please try again.")

if __name__ == '__main__':
    main()