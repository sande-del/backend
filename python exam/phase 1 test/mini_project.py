# Challenge 4 — Mini OOP Project: Library Management
# 1. Create a class Book with attributes: title, author, status (available or borrowed)
# 2. Create a class Library to store a list of books
# 3. Add methods to Library:
#    - add_book(book) to add a book
#    - borrow_book(title) to borrow a book if available
#    - return_book(title) to return a borrowed book
# 4. Test by:
#    - Creating 2-3 books
#    - Adding them to the library
#    - Borrowing one book
#    - Returning the borrowed book
class book:
    def __init__(self,title,author,status):
        self.title =title
        self.author = author
        self.status = "available"
class library:
    def add_book(self):
        
        