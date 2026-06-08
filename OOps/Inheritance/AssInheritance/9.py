class LibraryItems:
    def __init__(self,title):
        self.__title=title
        self.__is_borrowed=False


    def get_title(self):
        return self.__title
    

    def is_borrowed(self):
        return self.__is_borrowed
    


    def borrow_items(self):
        if self.__is_borrowed:
            print("Item is already borrowed")
        else:
            self.__is_borrowed=True
            print("Item borrowed successfully" )


class Book(LibraryItems):
    pass

class Magazine(LibraryItems):
    pass

class Newspaper(LibraryItems):
    pass


b=Book("Python Programming")
b.borrow_items()

M=Magazine("Tech Magazine")
M.borrow_items()

N=Newspaper("Times of India")
N.borrow_items()