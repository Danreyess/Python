class Book:
    def __init__(self, title, author, available= True):
        self.title = title
        self.autor = author
        self.available = available


    def borrow(self):
        if self.available:
            self.available = False
            print(f"You borrowed {self.title}")
        else:
            print(f"Sorry {self.title} is already borrowed")

    def return_book(self):
        self.available = True
        print(f"You returned {self.title}")

book1 = Book("1984", "George Orwell", True)
book1.borrow()
book1.return_book()
