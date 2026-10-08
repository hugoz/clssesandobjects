class Book:
    def __init__(self, title, author, pages):
        self.title = title
        self.author = author
        self.pages = pages

    def show_info(self):
        print("Title:", self.title)
        print("Author:", self.author)
        print("Pages:", self.pages)


book1 = Book("Harry Potter", "J.K. Rowling", 336 )
book2 = Book("The Lord of the Rings", "J.R.R. Tolkien", 1178 )

book1.show_info()
print()
book2.show_info()