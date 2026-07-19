from school_library import SchoolLibrary
from student import Student
from librarian import Librarian
from book import Book

# Create Library
library = SchoolLibrary("ABC Library", "Noida")

# Create Books
book1 = Book(101, "Python", "Guido", 500)
book2 = Book(102, "SQL", "Oracle", 450)

# Create Student and Librarian
student = Student(1, "Suraj", "BCA")
librarian = Librarian(1001, "Rahul", 30000)

# Library Details
print("\n----- Library Details -----")
library.show_library()

# Add Books
print("\n----- Add Books -----")
library.add_book(book1)
library.add_book(book2)

# Show Books
print("\n----- Available Books -----")
library.show_books()

# Student Activity
print("\n----- Student Activity -----")
student.issue_book(book1)
student.return_book(book1)

# Librarian Activity
print("\n----- Librarian Activity -----")
librarian.manage_books()

# Student Details
print("\n----- Student Details -----")
student.show_person()

# Librarian Details
print("\n----- Librarian Details -----")
librarian.show_person()

# Book Details
print("\n----- Book Details -----")
book1.show_book()