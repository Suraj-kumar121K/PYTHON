# ==========================================================
# Python OOP Inheritance Projects
# ==========================================================

# ==========================================================
# Project 1: School Management System (Single Inheritance)
# ==========================================================

# Create class Person
# Attributes:
# - name
# - age
# Method:
# - display()

# Create class Student inherits Person
# Attribute:
# - roll_no
# - marks
# Method:
# - grade()

# Create class Teacher inherits Person
# Attribute:
# - subject
# - salary
# Method:
# - teach()

# Create class Principal inherits Person
# Attribute:
# - experience
# Method:
# - manage_school()

# Create objects of Student, Teacher, and Principal.
# Call all methods.


# ==========================================================
# Project 2: Vehicle Management System (Hierarchical Inheritance)
# ==========================================================

# Create class Vehicle
# Attributes:
# - brand
# - fuel_type
# Method:
# - start()

# Create class Car inherits Vehicle
# Attributes:
# - model
# - seats

# Create class Bike inherits Vehicle
# Method:
# - helmet_required()

# Create class Truck inherits Vehicle
# Attribute:
# - load_capacity

# Create class Bus inherits Vehicle
# Attribute:
# - passengers

# Create objects of all child classes.
# Call all methods.


# ==========================================================
# Project 3: Company Management System (Multilevel Inheritance)
# ==========================================================

# Create class Person
# Attributes:
# - name
# - age

# Create class Employee inherits Person
# Attributes:
# - employee_id
# - salary

# Create class Manager inherits Employee
# Attributes:
# - department
# - bonus

# Methods:
# - display()
# - work()
# - calculate_salary()

# Create object of Manager.
# Call all methods.


# ==========================================================
# Project 4: Hospital Management System (Hierarchical Inheritance)
# ==========================================================

# Create class Hospital
# Attribute:
# - hospital_name

# Create class Doctor inherits Hospital
# Attribute:
# - specialization

# Create class Nurse inherits Hospital
# Attribute:
# - ward

# Create class Receptionist inherits Hospital
# Attribute:
# - counter_no

# Methods:
# - display()
# - duty()

# Create objects of Doctor, Nurse, and Receptionist.
# Call all methods.


# ==========================================================
# Project 5: Bank Management System (Multilevel Inheritance)
# ==========================================================

# Create class Bank
# Attribute:
# - bank_name

# Create class Account inherits Bank
# Attributes:
# - account_no
# - balance

# Create class SavingsAccount inherits Account
# Attribute:
# - interest_rate

# Methods:
# - deposit()
# - withdraw()
# - display()

# Create object of SavingsAccount.
# Perform deposit and withdraw operations.


# ==========================================================
# Project 6: Online Shopping System (Single Inheritance)
# ==========================================================

# Create class Product
# Attributes:
# - name
# - price

# Create class Electronics inherits Product
# Attribute:
# - warranty

# Create class Mobile inherits Electronics
# Attributes:
# - ram
# - storage

# Methods:
# - display()
# - final_price()

# Create object of Mobile.
# Display all details.


# ==========================================================
# Project 7: Animal Zoo Management (Hierarchical Inheritance)
# ==========================================================

# Create class Animal
# Methods:
# - eat()
# - sleep()

# Create class Dog inherits Animal
# Method:
# - sound()

# Create class Cat inherits Animal
# Method:
# - sound()

# Create class Lion inherits Animal
# Method:
# - sound()

# Create class Elephant inherits Animal
# Method:
# - sound()

# Create objects of all child classes.
# Call all methods.


# ==========================================================
# Project 8: University Management System (Hierarchical Inheritance)
# ==========================================================

# Create class Person
# Attributes:
# - name
# - age

# Create class Student inherits Person
# Attributes:
# - roll
# - marks

# Create class Professor inherits Person
# Attribute:
# - subject

# Create class Staff inherits Person
# Attribute:
# - department

# Create objects of Student, Professor, and Staff.
# Display all details.


# ==========================================================
# Project 9: Smart Devices System (Hybrid Inheritance)
# ==========================================================
# Create class Device
# Attribute:
# - company
# Create class SmartPhone inherits Device
# Attribute:
# - ram
# Create class Camera
# Attribute:
# - megapixel
# Create class FlagshipPhone inherits SmartPhone and Camera
# Attribute:
# - ai_camera
# Method:
# - display()
# Create object of FlagshipPhone.
# Display all details.


# ==========================================================
# Project 10: Library Management System (Hybrid Inheritance)
# ==========================================================
# Create class LibraryItem
# Create class Book inherits LibraryItem
# Create class EBook inherits Book
# Create class Downloadable
# Create class KindleBook inherits EBook and Downloadable
# Methods:
# - issue()
# - return_book()
# - download()

# Create object of KindleBook.
# Call all methods.


# ==========================================================
# Bonus Challenge (Apply to Every Project)
# ==========================================================
# 1. Create constructors (__init__) in every class.
# 2. Use super().__init__() wherever required.
# 3. Create one method in every class.
# 4. Override one method in the child class.
# 5. Check Method Resolution Order (MRO):
#    print(ClassName.mro())
# 6. Check object type:
#    isinstance(object_name, ClassName)
# 7. Check inheritance:
#    issubclass(ChildClass, ParentClass)
# 8. Print all object details using display().
# 9. Create at least two objects for every child class.
# 10. Add user input to make the project interactive.


"""
Project 1: School Management System ⭐ (Single Inheritance)
Classes
Person
   │
   ├── Student
   ├── Teacher
   └── Principal
Person
name
age
display()
Student
roll_no
marks
grade()
Teacher
subject
salary
teach()
Principal
experience
manage_school()
"""

"""
Project 2: Vehicle Management System ⭐⭐⭐ (Hierarchical Inheritance)
Vehicle
   │
   ├── Car
   ├── Bike
   ├── Truck
   └── Bus

Vehicle

brand
fuel_type
start()

Car

model
seats

Bike

helmet_required()

Truck

load_capacity()

Bus

passengers()
"""

"""
Project 3: Company Management System ⭐⭐⭐
Person
   │
Employee
   │
Manager

Person

name
age

Employee

employee_id
salary

Manager

department
bonus

Methods

display()
work()
calculate_salary()
"""

"""
Project 4: Hospital Management ⭐⭐⭐
Hospital
     │
     ├── Doctor
     ├── Nurse
     └── Receptionist
Hospital
hospital_name
Doctor

specialization
Nurse
ward
Receptionist
counter_no

Methods
display()
duty()
"""
"""
Project 5: Bank Management ⭐⭐⭐⭐
Bank
    │
Account
    │
SavingsAccount

Bank

bank_name

Account

account_no
balance

SavingsAccount

interest_rate

Methods

deposit()
withdraw()
display()
"""
"""
Project 6: Online Shopping ⭐⭐⭐⭐
Product
      │
Electronics
      │
Mobile

Product

name
price

Electronics

warranty

Mobile

ram
storage

Methods

display()
final_price()
"""
"""
Project 7: Animal Zoo ⭐⭐⭐
Animal
     │
     ├── Dog
     ├── Cat
     ├── Lion
     └── Elephant

Methods

eat()
sleep()

Each child

sound()
"""
"""
Project 8: University Management ⭐⭐⭐⭐
Person
   │
   ├── Student
   ├── Professor
   └── Staff

Attributes

name
age

Student

roll
marks

Professor

subject

Staff

department
"""
"""
Project 9: Smart Devices ⭐⭐⭐⭐⭐ (Hybrid Inheritance)
Device
   │
SmartPhone
   │
        Camera
           │
FlagshipPhone

Device

company

SmartPhone

ram

Camera

megapixel

FlagshipPhone

AI Camera

Methods

display()
"""

"""Project 10: Library Management ⭐⭐⭐⭐⭐
LibraryItem
        │
      Book
        │
    EBook

Downloadable
        │
    KindleBook

Methods

issue()
return_book()
download()

python comment kar ke do"""