class Book:
    def __init__(self, title, author, isbn):
        self.title = title
        self.author = author
        self.isbn = isbn


class Library:
    def __init__(self):
        self.books = []

    def add_book(self, book):
        self.books.append(book)

    def remove_book(self, book):
        self.books.remove(book)

    def display(self):
        for b in self.books:
            print(f"{b.title} - {b.author}")


lib = Library()

b1 = Book("Python", "Guido", "123")
b2 = Book("Java", "James", "456")

lib.add_book(b1)
lib.add_book(b2)

lib.display()

lib.remove_book(b1)
print("After removing:")
lib.display()