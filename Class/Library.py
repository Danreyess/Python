
class Book:
    def __init__(self, title, author):
        self.title = title
        self.author = author
        self.available = True

class Library:
    def __init__(self):
        self.books = []

    def add_books(self, title, author):
        book = Book(title, author)
        self.books.append(book)

    def show_books(self):
        for book in self.books:
            status = "Available" if book.available else "Not available"
            print(f"{book.title}: {status}")

    def borrow_book(self, title):
        for book in self.books:
            if book.title == title:
                book.available = False
                print("Book borrowed")
                return
            else:
                print("Book not available")
                return
        print("Book not found")

    def return_book(self, title):
        for book in self.books:
            if book.title == title:
                book.available = True
                print("Book returned")
                return
book1 = Library()
book1.add_books("My first book", "guillermo")
book1.borrow_book("My first book")
book1.show_books()



# add
# show
# borrow
# return