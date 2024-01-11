class Library:
    def __init__(self):
        self.no_of_books = 0
        self.books = []

    def add_book(self, book):
        self.books.append(book)
        self.no_of_books = len(self.books)

    def use_book(self, book_name):
        if book_name in self.books:  # Check if the book is in the library
            self.books.remove(book_name)  # Remove the specified book from the list
            self.no_of_books = len(self.books)  
            print(f"'{book_name}' has been taken by the user from the library.")
        else:
            print(f"'{book_name}' is not available in the library.")

    def show(self):
        print(f"There are {self.no_of_books} books:")
        for book in self.books:
            print(book)

l1 = Library()

while True:
    book_name = input("Enter a book (type 'quit' to stop): ")

    if book_name.lower() == 'quit':
        break

    l1.add_book(book_name)

l1.show()

use = input('Enter which book do you want to use: ')
l1.use_book(use)

l1.show()
