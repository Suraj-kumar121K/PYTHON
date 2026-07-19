from libary import Library

class SchoolLibrary(Library):
    def __init__(self, library_name ,location):
        super().__init__(library_name ,location)
        self.books = []
    
    def add_book(self, book):
        self.books.append(book)
        print(f"{book} has been added successfully.")
        
    def remove_book(self, book):
        if book in self.books:
            self.books.remove(book)
            print(f"{book} has been removed successfully.")
        else:
            print(f"{book} is not available in the library.")
    
    def show_books(self):
        if len(self.books) == 0:
            print("No books available.")
        else:
            print("\nAvailable Books:")
            for book in self.books:
                print("-", book)