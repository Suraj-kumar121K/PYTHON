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
# print("Student Details")
# s1.show_student()
# print()
# print("Teacher Details")
# t1.show_teacher()      


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
# Q2. Vehicle → Car, Bike
class Parent:
    def __init__(self, brand):
        self.brand = brand

    def show_brand(self):
        print("Brand Name:", self.brand)

class Child_1(Parent):
    def __init__(self, brand, car, model):
        super().__init__(brand)
        self.car = car
        self.model = model

    def show_child_1(self):
        self.show_brand()
        print("Car:", self.car)
        print("Model:", self.model)

class Child_2(Parent):
    def __init__(self, brand, bike, engine_cc):
        super().__init__(brand)
        self.bike = bike
        self.engine_cc = engine_cc

    def show_child_2(self):
        self.show_brand()
        print("Bike:", self.bike)
        print("Engine CC:", self.engine_cc)

# Car Object
c1 = Child_1("Toyota", "Fortuner", "2025")
# Bike Object
b1 = Child_2("Yamaha", "R15", "155cc")
# print("----- Car Details -----")
# c1.show_child_1()
# print()
# print("----- Bike Details -----")
# b1.show_child_2()


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
class Parent:
    def __init__(self, name):
        self.name  = name
    
    def show_name(self):
        print("Name :", self.name)

class Dog(Parent):
    def __init__(self, name, breed):
        super().__init__(name)
        self.breed = breed
        
    def show_dog(self):
        self.show_name()
        print("Breed :", self.breed)
        
class Cat(Parent):
    def __init__(self, name, color):
        super().__init__(name)
        self.color = color
        
    def show_cat(self):
        self.show_name()
        print("Color :", self.color)
d1 = Dog("Tommy", "Labrador")
c1 = Cat("Kitty", "White")
# print("Dog Details")
# d1.show_dog()
# print()
# print("Cat Details")
# c1.show_cat()

# Q4. Employee → Manager, Developer
"""
Parent:
    name
    salary
Manager:
    department
    
Developer:
    language
Create objects and display all information.
"""
class Parent:
    def __init__(self, name, salary):
        self.name = name
        self.salary = salary
    
    def show_name_salary(self):
        print("Name :", self.name)
        print("Salary :", self.salary)

class Manager(Parent):
    def __init__(self, name, salary, department):
        super().__init__(name, salary)
        self.department = department
    
    def show_manager(self):
        self.show_name_salary()
        print("Department :", self.department)
        
class Developer(Parent):
    def __init__(self, name, salary, language):
        super().__init__(name, salary)
        self.language = language
    
    def show_developer(self):
        self.show_name_salary()
        print("Language :", self.language)

m1 = Manager("Suraj", 200000, "IT")
d1 = Developer("Suraj", 200000, "Hindi")
# print("Manager Details")
# m1.show_manager()
# print()
# print("Developer Details")    
# d1.show_developer()

# Q5. BankAccount → SavingsAccount, CurrentAccount
"""
# Parent:
    account_holder
    balance

# Method:
    show_balance()
    
Savings:
    interest_rate
    
Current:
    overdraft_limit
    
Display all information.
"""
class Parent:
    def __init__(self, account_holder, balance):
        self.account_holder = account_holder
        self.balance = balance
        
    def show_balance(self):
        print("Bank Holder Name: ", self.account_holder)
        print("Balance: ", self.balance)
        
class Savings(Parent):
    def __init__(self, account_holder, balance, interest_rate):
        super().__init__(account_holder, balance)
        self.interest_rate = interest_rate
    def show_saving(self):
        self.show_balance()
        print("Rate OF Interest", self.interest_rate)
        
class Current(Parent):
    def __init__(self, account_holder, balance, overdraft_limit):
        super().__init__(account_holder, balance)
        self.overdraft_limit = overdraft_limit
    
    def show_current(self):
        self.show_balance()
        print("Overdraf Limit :", self.overdraft_limit)

s1 = Savings("Suraj", 500000, 9.99)
c1 = Current("Rahul", 500000, 50000)
# print("Savings Account")
# s1.show_saving()
# print()
# print("Current Account")
# c1.show_current()


# Challenge Practice (Interview Level)
# Q6. ElectronicDevice → Laptop, Mobile, Tablet
"""
Parent:
    company
    price

Laptop:
    ram
    processor

Mobile:
    camera
    battery

Tablet:
    screen_size
    stylus_support
Use constructors with super() and create one object of each child class.
"""