"""
Shopping Cart
Concepts:
list
append()
remove()
loop

Features:
Add Product
Remove Product
View Cart
"""

"""
cart = []

def add_product():
    product = input("Enter Product Name: ")
    cart.append(product)
    print("Product Added")

def view_project():
    if len(cart) == 0:
        print("Cart Empty")
    else:
        print("\nCart Items")
        for item in cart:
            print(item)
            
def remove_product():
    product = input("Enter Product Name Remove: ")
    if product in cart:
        cart.remove(product)
        print("Product Removed")
    else:
        print("Product Not Found")
    
while True:
    print("\n ----- Shoping Cart ----")
    print("1. Add Project")
    print("2. View Cart")
    print("3. Remove Product")
    print("4. Exit")
    choice = input("Enter Choice:")
    if choice == "1":
        add_product()
    elif choice == "2":
        view_project()
    elif choice == "3":
        remove_product()
    elif choice == "4":
        print("Program Closed")
        break
    else:
        print("Invalid Choice")
""" 
"""
Python CRUD Project
CRUD ka matlab hota hai:
C → Create
R → Read
U → Update
D → Delete
Ye Python ka bahut important project hai. Isse:
list
function
loop
condition
input/output

sab strong ho jata hai.
"""
# 1. Student CRUD Project
"""
Logic
1. Create
Take the student name from the user and add it to the list.
2. Read
Display all students from the list.
3. Update
Find the old student name and replace it with a new name.
4. Delete
Remove the student name from the list.
"""
"""students = []

def create_student():
    name = input("Enter Student Name: ")
    students.append(name) # list me new item add karta hai.
    print("Student Added")

def read_student():
    if len(students) == 0: # Agar list empty hai to length 0 hogi.
        print("No Students Found")
    else:
        print("\nStudent List")
        for student in students:
            print(student)

def update_student():
    old_name = input("Enter Old Name: ") # Check karta hai ki old name list me hai ya nahi.
    if old_name in students:
        new_name = input("Enter New Name: ")
        index = students.index(old_name) # index() old name ki position nikalta hai.
        students[index] = new_name
        print("Student Updated") # Old name ko new name se replace karta hai.
    else:
        print("Student Not Found")

def delete_student():
    name = input("Enter Name Delete: ")
    if name in students:
        students.remove(name) # list se item delete karta hai.
        print("Student Deleted")
    else:
        print("Student Not Found")

while True:
    print("\n--- CRUD MENU ---")
    print("1. Create Student")
    print("2. Read Student")
    print("3. Update Student")
    print("4. Delete Student")
    print("5. Exit")

    choice = input("Enter Choice: ")
    if choice == "1":
        create_student()
    elif choice == "2":
        read_student()
    elif choice == "3":
        update_student()
    elif choice == "4":
        delete_student()
    elif choice == "5":
        print("Program Closed")
        break
    else:
        print("Invalid Choice")"""
        
        
        
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
    print("1. Add Book")
    print("2. View Book")
    print("3. Issue Book")
    print("4. Return Book")
    print("5. Exit")
    
    choice = input("Enter Your choice: ")
    if choice == "5":
        print("Thank You")
        break
    
    if choice == "1":
        add_book()
    elif choice == "2":
        View_Book()
    elif choice == "3":
        Issue_Book()
    elif choice == "4":
        Return_Book()
    else:
        print("Invalid Choice")
        
    
        