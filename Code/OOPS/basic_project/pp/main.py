from book import Book
from library import LibraryManagement
library = LibraryManagement("books.txt")
while True:

    print("\n--- Library Management System ---")
    print("1. Add Book")
    print("2. View Books")
    print("3. Search Book")
    print("4. Exit")

    choice = input("Enter Choice: ")

    if choice == "1":
        book_id = input("Enter Book ID: ")
        title = input("Enter Book Title: ")
        author = input("Enter Author Name: ")

        book = Book(
            book_id,
            title,
            author
        )
        library.add_book(book)
    elif choice == "2":
        library.view_books()

    elif choice == "3":
        book_id = input("Enter Book ID: ")
        library.search_book(book_id)

    elif choice == "4":
        print("Program Closed")
        break
    else:
        print("Invalid Choice")