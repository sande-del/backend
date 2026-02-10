# 1. Create a class Library with attribute books (list of book titles)
# 2. Implement __len__ to return number of books
# 3. Create a Library object with 3 books
# 4. Print the length of the library
class library:
    def __init__(self,titles):
        self.titles = titles
    def __len__(self):
        return len(self.titles)
t = library(["love with roses", "the broken nose", "the pilot"])
print(len(t))

        