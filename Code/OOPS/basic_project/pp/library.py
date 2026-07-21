from book import Book
class LibraryManagement:
    def __init__(self, filename):
        self.filename = filename
    # Add Book
    def add_book(self, book):
        with open(self.filename, "a") as file:
            file.write(
                f"{book.book_id},{book.title},{book.author}\n"
            )
        print("Book Added Successfully")
    # View Books
    def view_books(self):
        try:
            with open(self.filename, "r") as file:
                print("\nBook Records:")
                for line in file:
                    book_id, title, author = line.strip().split(",")
                    book = Book(
                        book_id,
                        title,
                        author
                    )
                    book.display()
        except FileNotFoundError:
            print("No Books Found")
    # Search Book
    def search_book(self, book_id):
        found = False
        try:
            with open(self.filename,"r") as file:
                for line in file:
                    id, title, author = line.strip().split(",")
                    if id == book_id:
                        print("\nBook Found")
                        book = Book(
                            id,
                            title,
                            author
                        )
                        book.display()
                        found = True
            if not found:
                print("Book Not Found")
        except FileNotFoundError:
            print("File Not Found")