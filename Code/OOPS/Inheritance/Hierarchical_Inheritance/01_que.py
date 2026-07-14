# Q1. Person → Student, Teacher
"""
Create a Person class with:
    name
    show_name()
Create two child classes:
Student
    roll_no
    show_student()
Teacher
    subject
    show_teacher()
Create one object of each class.
"""
class Person:
    def __init__(self, name):
        self.name = name

    def show_name(self):
        print("Name:", self.name)

class Student(Person):
    def __init__(self, name, roll_no):
        super().__init__(name)
        self.roll_no = roll_no

    def show_student(self):
        self.show_name()
        print("Roll No:", self.roll_no)

class Teacher(Person):
    def __init__(self, name, subject):
        super().__init__(name)
        self.subject = subject

    def show_teacher(self):
        self.show_name()
        print("Subject:", self.subject)

# Object of Student
s1 = Student("Rahul", 101)

# Object of Teacher
t1 = Teacher("Amit", "Python")

print("Student Details")
s1.show_student()

print()

print("Teacher Details")
t1.show_teacher()      


# Q2. Vehicle → Car, Bike
"""
Parent:
brand
show_brand()

Child 1:
Car
model

Child 2:
Bike
engine_cc

Display all details.
"""

# Q3. Animal → Dog, Cat
"""
Parent:
    name
Method:
   show_name()
Dog:
   breed
Cat:
   color
Display all details.
"""

# Q4. Employee → Manager, Developer

# Parent:

# name
# salary

# Manager:

# department

# Developer:

# language

# Create objects and display all information.

# Q5. BankAccount → SavingsAccount, CurrentAccount

# Parent:

# account_holder
# balance

# Method:

# show_balance()

# Savings:

# interest_rate

# Current:

# overdraft_limit

# Display all information.

# Challenge Practice (Interview Level)
# Q6. ElectronicDevice → Laptop, Mobile, Tablet

# Parent:

# company
# price

# Laptop:

# ram
# processor

# Mobile:

# camera
# battery

# Tablet:

# screen_size
# stylus_support

# Use constructors with super() and create one object of each child class.