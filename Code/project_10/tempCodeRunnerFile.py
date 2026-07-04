# 7. Library Management Project
books = []
print("Welcome to Library Management System")

def add_book():
    book = input("Enter Book Name: ")
    books.append(book)
    print("Book Added successfully")

def View_Book():
    if len(books) == 0:
        print("No Books Available")
    else:
        print("\nAvailable Books:")
        for book in books:
            print(book)

def Issue_Book():
    book_issue = input("Enter a Book Name to Issue: ")
    if book_issue in books:
        books.remove(book_issue)
        print("Book Issued Successfully")
    else:
        print("Book Not Avilable")
            
def Return_Book():
    return_book = input("Enter Book Name to Return")
    books.append(return_book)
    print("Book Returned Successfully")
    
    
    
    
    
    
while True:
    print("\n=== Library Management Project ===")
    print("Enter 1 for Add Book")
    print("Enter 2 for  View Book")
    print("Enter 3 for  Issue Book")
    print("Enter 4 for  Return Book")
    print("Enter 5 for  Exit")
    
    choice = input("Enter Your choice: ")
   
    if choice == "1":
        add_book()
    elif choice == "2":
        View_Book()
    elif choice == "3":
        Issue_Book()
    elif choice == "4":
        Return_Book()
    elif choice == "5":
        print("Thank You")
        break
    else:
        print("Invalid Choice")
        
    
        