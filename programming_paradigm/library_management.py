#library

class Book:

    def __init__(self, title, author, _is_checked_out):
        self.title = title
        self.author = author
        self.__is_checked_out = _is_checked_out
    def book_id(self):
        self.book_id = f"{self.tile} by {self.author} {_is_checked_out}"
        return self.book_id
class Library:
    __books = []

    def add_book(self, title, author):
        self.title = input()
        self.author = input()
        __books.appand("{self.title}, {self.author}") 
    def check_out_book(self, title):
        if self.title in __books:
            pass
    def return_book(self, title):
        if self.title in __books:
            False
    def list_available_books(self):
        for i in __books:
            print(i)
