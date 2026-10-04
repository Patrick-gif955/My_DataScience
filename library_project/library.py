class Book:
    def __init__(self,title,author):
        self.author = author
        self.title= title

    def name (self):
        return f"{self.title} by {self.author}"

class Library:
    def __init__(self,):
        self.books = []
        self.borrowed = []
       
    def add_books(self, book):
        self.books.append(book)
        return f"{book.title} by {book.author}"
    def show_book(self):
        lib = [f"{book.title} by {book.author} " for book in self.books]
        return "\n".join(lib)

    def borrow_book(self, title):
        self.title = title
                  
        for book in self.books:
                if title.lower() == book.title.lower():
                    self.books.remove(book)
                    self.borrowed.append(book)
                    return f"You have successfully borrrowed {book.title} by {book.author}"
                
        return f"Book not found"
    def return_book(self, title):
        self.title = title
        
        for book in self.borrowed:
                if title.lower() == book.title.lower():
                    self.borrowed.remove(book)
                    self.books.append(book)
                    return f"Thank You for returning {book.title} by {book.author}"
        
        return f"This book wasn't borrowed from this library"             

b1 = Book("Atomic Habbits", "James Clear" )
b2 = Book("Don't leave anything for later", "Library Mindset" )
b3 = Book("Things Fall Apart", "Chinua Achebe")

libry = Library()
libry.add_books(b1)
libry.add_books(b2)
libry.add_books(b3)
print(f"___My Libry__")

print("__All Library Books__")
print(libry.show_book())

print("__Borrowed Books__")
print(libry.borrow_book("Things Fall Apart"))
print(libry.borrow_book("atomic habbits"))
print("__Returned Books__")
print(libry.return_book("Things fall Apart"))
print(libry.return_book("ATOMIC HABBITS"))
print("__List Of Books__")
print(libry.show_book())