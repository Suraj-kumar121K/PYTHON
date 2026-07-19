class Book:
    def __init__(self, book_id, title, author, price):
        self.book_id = book_id
        self.title = title
        self.author = author
        self.price = price

    def __str__(self):
        return self.title

    def show_book(self):
        print("Book ID :", self.book_id)
        print("Title   :", self.title)
        print("Author  :", self.author)
        print("Price   :", self.price)