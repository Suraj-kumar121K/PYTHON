"""
1. Single Inheritance
Question 1
Create a class Animal with:
attribute: name
method: display()
Create a class Dog that inherits from Animal.
Add method sound() that prints "Dog barks".
Create an object and call both methods.
"""
class Animal:
    def __init__(self, name):
        self.name = name
    def display(self):
        print("Animal Name:", self.name)
class Dog(Animal):
    def sound(self):
        print("Dog barks")
d = Dog("Tommy")
# d.display()
# d.sound()

"""
Q2. Create a class Vehicle with:
- attribute: brand
- method: display_brand()
Create a class Car that inherits from Vehicle.
Add:
- attribute: model
- method: display_model()
Create an object and call both methods.
"""
class Vehicle:
    def __init__(self, brand):
        self.name = brand
    def display_brand(self):
        print("Brand :", self.name)
class Car(Vehicle):
    def __init__(self, brand, model):
        super().__init__(brand)
        self.model = model
    def display_model(self):
        print("Model :", self.model)
c1 = Car("Tata", "Nexon")
# c1.display_brand()
# c1.display_model()    

"""
Q3. Create a class Person with:
- attribute: name
- method: show_name()
Create a class Student that inherits from Person.
Add:
- attribute: roll_no
- method: show_roll()
Create an object and display both details.
"""
class Person:
    def __init__(self, name):
        self.name = name
    def show_name(self):
        print("Name :", self.name) 
class Student(Person):
    def __init__(self, name, roll_no):
        super().__init__(name) # Parent constructor call
        self.roll_no = roll_no
    def show_roll(self):
        print("Roll No :", self.roll_no)
        
s1 = Student("Suraj", 22)
# s1.show_name()
# s1.show_roll()

"""
Q4. Create a class Book with:
- attribute: title
- method: display_title()
Create a class EBook that inherits from Book.
Add:
- attribute: file_size
- method: display_size()
Create an object and call both methods."""


"""
Q5. Create a class Employee with:
- attribute: name
- method: display_name()
Create a class Manager that inherits from Employee.
Add:
- attribute: salary
- method: display_salary()
Create an object and display all details.
"""


"""
Q6. Create a class Mobile with:
- attribute: company
- method: display_company()
Create a class SmartPhone that inherits from Mobile.
Add:
- attribute: ram
- method: display_ram()
Create an object and call both methods.
"""


"""
Q7. Create a class Shape with:
- attribute: color
- method: display_color()
Create a class Circle that inherits from Shape.
Add:
- attribute: radius
- method: display_radius()
Create an object and display both values.
"""


"""
Q8. Create a class Bank with:
- attribute: bank_name
- method: display_bank()
Create a class Customer that inherits from Bank.
Add:
- attribute: customer_name
- method: display_customer()
Create an object and call both methods.
"""

"""
Q9. Create a class Laptop with:
- attribute: company
- method: display_company()
Create a class GamingLaptop that inherits from Laptop.
Add:
- attribute: gpu
- method: display_gpu()
Create an object and display all details.
"""


"""
Q10. Create a class Hospital with:
- attribute: hospital_name
- method: display_hospital()
Create a class Doctor that inherits from Hospital.
Add:
- attribute: specialization
- method: display_specialization()
Create an object and call both methods.
"""

# ============================================
# 1. SINGLE INHERITANCE (10 Questions)
# ============================================
# Q1. Create Person(name) and Student(name, roll) using inheritance.

# Q2. Create Vehicle(brand) and Car(brand, model).

# Q3. Create Animal(name) and Dog(name, breed).

# Q4. Create Book(title) and EBook(title, size).

# Q5. Create Employee(name) and Manager(name, salary).

# Q6. Create Mobile(company) and SmartPhone(company, ram).

# Q7. Create Shape(color) and Circle(color, radius).

# Q8. Create Bank(bank_name) and Customer(bank_name, customer_name).

# Q9. Create Laptop(company) and GamingLaptop(company, gpu).

# Q10. Create Hospital(name) and Doctor(name, specialization).