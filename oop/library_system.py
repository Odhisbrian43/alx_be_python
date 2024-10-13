#classes 

class Book:
    def __init__(self, title, author):
        self.title = title
        self.author = author
    def __str__(self):

class EBook(Book):
    def __init__(self, title, author, file_size):
        super().__init__(title, author)
        self.file_size = file_size
    def __str__(self):

class PrintBook(Book):
    def __init__(self, title, author, page_count):
        super().__init__(title, author)
        self.page_count = page_count
    def __str__(self):

class Library:
    def __init__(self, books):
        self.books = []
    #books = []

    def add_book(self, book):
        #book = 
        books.append(book)

    def list_books(self):
        for i in books:
            print(i)

if __name__ == "__main__":
    main()
