# =========================================
# 1️⃣ Class Practice Questions
# =========================================
# Student class banao
# Car class banao
# Mobile class banao
# Employee class banao
# Book class banao
# Laptop class banao
# Bank class banao
# Animal class banao
# Movie class banao
# College class banao

# =========================================
# 2️⃣ Object Practice Questions
# =========================================

# Student class ka object banao
# Car class ke 3 objects banao
# Mobile class ke different objects create karo
# Employee object bana kar data print karo
# Book object bana kar book name print karo
# Animal object bana kar sound print karo
# Laptop object create karo
# Bank object bana kar account details print karo
# Movie object bana kar movie name print karo
# College object create karo aur data access karo

# Student
class Student:
    def __init__(self, name, age, course):
        self.name = name
        self.age = age
        self.course = course
    def display(self):
        print("Name :", self.name)
        print("Age :", self.age)
        print("Course :", self.course)
s1 = Student("Suraj", 22, "Python")
s2 = Student("Rahul", 21, "Data Analysis")

# s1.display()
# print()
# s2.display()

# Employee:
class Employee:
    def __init__(self, name, salary, department):
        self.name = name
        self.salary = salary
        self.department = department
        
    def display(self):
        print("Name :", self.name)
        print("Salary :", self.salary)
        print("Department :", self.department)
s1 = Employee("Suraj", 50000, "IT")
s2 = Employee("Rahul", 10000, "HR")

# s1.display()
# print()
# s2.display()

class Car:
    def __init__(self, brand, model, price):
        self.brand = brand
        self.model = model
        self.price = price
    
    def display(self):
        print("Brand :", self.brand)
        print("Model :", self.model)
        print("Price :", self.price)
    
c1 = Car("Toyota", "Fortuner", 4500000)               
c2 = Car("Hyundai", "Creta", 1800000)  

# c1.display()             
# print()
# c1.display()            

# Book
class Book:
    def __init__(self, name, author, price):
        self.name = name
        self.author = author 
        self.price = price
    
    def display(self):
        print("Book :", self.name)
        print("Author :", self.author)
        print("Price :", self.price)
b1 = Book("Python", "Guido", 499)
b2 = Book("SQL", "John", 350)

# b1.display()
# print()
# b2.display()

# Bank Class (4 Methods)
# Class Declaration (Class banana)
class Bank:
    # Constructor (Special Method)
    # Object create hote hi automatically call hota hai.
    def __init__(self, name, balance):
        # Instance Variable
        # Customer ka name object ke andar store hota hai.
        self.name = name
        # Instance Variable
        # Customer ka balance object ke andar store hota hai.
        self.balance = balance
    # Instance Method
    # Account me paise jama (Deposit) karta hai.
    def deposit(self, amount):
        # Assignment Operator (+=)
        # Current balance me amount add karta hai.
        self.balance += amount
        # Output Statement
        print(amount, "Deposited Successfully")
    # Instance Method
    # Account se paise nikalta hai.
    def withdraw(self, amount):
        # Conditional Statement (if)
        # Check karta hai ki balance enough hai ya nahi.
        if amount <= self.balance:
            # Assignment Operator (-=)
            # Balance me se amount minus karta hai.
            self.balance -= amount
            # Output Statement
            print(amount, "Withdraw Successfully")
        # Else Block
        else:
            print("Insufficient Balance")
    # Instance Method
    # Current balance dikhata hai.
    def check_balance(self):
        # Output Statement
        print("Current Balance:", self.balance)
    # Instance Method
    # Customer ki details dikhata hai.
    def display(self):
        # Output Statement
        print("Customer Name:", self.name)
        # Output Statement
        print("Balance:", self.balance)

# Object Creation
# b1 = Bank("Suraj", 100000)

# Method Calling
# b1.display()

# Method Calling
# b1.deposit(5000)

# Method Calling
# b1.withdraw(3000)

# Method Calling
# b1.check_balance()

"""
1. Student Management
Class: Student
Variables:
name
age
marks

Methods:
display()
show_marks()
result()
grade()

Objects:
2 Students
"""
class  Students:
    def __init__(self, name, age, marks):
        self.name = name
        self.age = age
        self.marks = marks
    
    def display(self):
        print("Name", self.name) 
        
    def show_marks(self):
        print("marks", self.marks)
    
    def result(self):
        if self.marks >= 40:
            print("pass")
        else:
            print("Fail")
    
    def grade(self):
        if self.marks >= 90:
            print("Grade A")
        elif self.marks >= 75:
            print("Grade B")
        else:
            print("Grade C")
# s1 = Students("Suraj", 25, 85)
# s1.display()
# s1.show_marks()
# s1.result()
# s1.grade()

"""
2. Bank Management
Class: Bank

Variables:
customer_name
account_number
balance

Methods:
deposit()
withdraw()
check_balance()
display()

Objects:
2 Customers
"""


"""
3. Employee Management
Class: Employee

Variables:
name
salary
department

Methods:
display()
bonus()
increment()
show_salary()

Objects:
2 Employees
"""

"""
4. Library Management
Class: Library
Variables:
book_name
author
price

Methods:
display()
issue_book()
return_book()
book_info()

Objects:
2 Books
"""

"""
5. Mobile Shop
Class: Mobile

Variables:
brand
model
price

Methods:
display()
discount()
change_price()
mobile_info()

Objects:
2 Mobiles
"""

"""
6. Car Showroom
Class: Car

Variables:
brand
model
price

Methods:
display()
start()
stop()
car_info()

Objects:
2 Cars
"""

"""
7. Hospital
Class: Patient

Variables:
name
disease
age

Methods:
display()
admit()
discharge()
patient_info()

Objects:
2 Patients
"""

"""
8. College
Class: College

Variables:
student_name
course
fees

Methods:
display()
pay_fees()
course_details()
student_info()

Objects:
2 Students
"""

"""
9. Movie
Class: Movie

Variables:
name
hero
rating

Methods:
display()
show_rating()
hit_or_flop()
movie_info()

Objects:
2 Movies
"""

"""
10. Shopping Cart
Class: Product

Variables:
product_name
price
quantity

Methods:
display()
total_price()
discount()
bill()

Objects:
2 Products
"""
