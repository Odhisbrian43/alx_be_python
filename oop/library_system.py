#classes 

class Book:
    def __init__(self, title, author):
        self.title = title
        self.author = author
    def __str__(self):
        book =  f"Book: {self.title} by {self.author}"
        return book

class EBook(Book):
    def __init__(self, title, author, file_size):
        super().__init__(title, author)
        self.file_size = file_size
    def __str__(self):
        book = f"EBook: {self.title} by {self.author}, file size: {self.file_size}KB"
        return book

class PrintBook(Book):
    def __init__(self, title, author, page_count):
        super().__init__(title, author)
        self.page_count = page_count
    def __str__(self):
        book =  f"PrintBook: {self.title} by {self.author}, Page Count: {self.page_count}"
        return book

class Library:
    def __init__(self):
        #self.books = books
        self.books = []
    #books = []

    def add_book(self, book):
        #book = 
        self.books.append(book)

    def list_books(self):
        for i in self.books:
            print(i)

if __name__ == "__main__":
    main()
