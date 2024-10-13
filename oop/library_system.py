#classes 

class Book:
    def __init__(self, title, author):
        self.title = title
        self.author = author

class EBook(Book):
    def __init__(self, title, author, file_size):
        self.file_size = file_size

class PrintBook(Book):
    def __init__(self, title, author, page_count):
        self.page_count = page_count

class Library:
   # def __init__(self, books):
        #self.books = books
    books = []

    def add_book(self, book):
        #book = 
        books.append(book)

    def list_books(self):
        for i in books:
            print(i)

if __name__ == "__main__":
    main()
