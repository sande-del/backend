# 1. Create class Book with attribute title
# 2. Add __str__ method to return the book title
# 3. Create a Book object and print it
class book:
    def __init__(self,title):
        self.title = title
     
    def  __str__(self):
        return f" The title of the book is {self.title}"
a = book("The ASHES")
print(a)
