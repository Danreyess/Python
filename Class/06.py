#Library sistem
class Book:
    def __init__(self, title, author):
        self.title = title
        self.author = author
        self.available = True

class Library:
    def __init__(self):
        self.books = []

    def add_book(self, title, author):
        book = Book(title, author)
        self.books.append(book)

    def show_books(self):
        for book in self.books:
            status = "Available" if book.available else "Borrowed"
            print(f"{book.title}: {status}")

    def borrow_book(self, title):
        for book in self.books:
            if book.title == title:
                if book.available:
                    book.available = False
                    print(f"You borrowed {book.title}")
                    return
                else:
                    print(f"{book.title} is not available")
                    return
        print("Book not found")

    def return_book(self, title):
        for book in self.books:
            if book.title == title:
                book.available = True
                print(f"You returned {book.title}")
                return

