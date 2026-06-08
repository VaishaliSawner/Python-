class Library:
    def __init__(self):
        self.books = []

    def add_book(self, book):
        self.books.append(book)

    def remove_book(self, book):
        if book in self.books:
            self.books.remove(book)

    def display(self):
        for b in self.books:
            print(b)


lib = Library()
lib.add_book("Python")
lib.add_book("Java")

lib.display()

lib.remove_book("Python")
print("After removing:")
lib.display()