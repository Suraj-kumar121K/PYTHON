"""
1. Multilevel Inheritance
Question 3
Create
Person
Employee
Manager
Manager should access methods from both parent classes.
"""
# Solution
class Person:
    def show_name(self):
        print("Name: Suraj")
class Employee(Person):
    def show_company(self):
        print("Company: Google")
class Manager(Employee):
    def show_salary(self):
        print("Salary: 80000")
m = Manager()
# m.show_name()
# m.show_company()
# m.show_salary()

# ============================================
# 3. MULTILEVEL INHERITANCE (10 Questions)
# ============================================
# Q2. Create Animal -> Dog -> Puppy.
class Animal:
    def __init__(self, name):
        self.name = name

    def Animal_name(self):
        print("Animal Name:", self.name)

class Dog(Animal):
    def __init__(self, name, breeds):
        super().__init__(name)
        self.breeds = breeds

    def dog_breeds(self):
        print("Dog Breed:", self.breeds)

class Puppy(Dog):
    def __init__(self, name, breeds, golden):
        super().__init__(name, breeds)
        self.golden = golden

    def Puppy_golden(self):
        self.Animal_name()
        self.dog_breeds()
        print("Golden Retriever Puppy:", self.golden)

p1 = Puppy("Dog", "Labrador", "Tommy")
p1.Puppy_golden()

# ============================================
# MULTILEVEL INHERITANCE (10 Questions)
# ============================================
"""
Q1. Create
    Person
    Employee
    Manager
Manager should access methods from both parent classes.
"""

"""
Q2 Create
    Vehicle
    Car
    SportsCar
SportsCar should access methods from both parent classes.
"""

"""
Q3. Create
    Book
    EBook
    KindleBook
KindleBook should access methods from both parent classes.
"""

"""
Q4. Create
    Mobile
    SmartPhone
    AndroidPhone
AndroidPhone should access methods from both parent classes.
"""

"""
Q5. Create
    Shape
    Rectangle
    Square
Square should access methods from both parent classes.
"""

"""
Q6. Create
    School
    Teacher
    Principal
Principal should access methods from both parent classes.
"""

"""
Q7. Create
    Bank
    Account
    SavingsAccount
SavingsAccount should access methods from both parent classes.
"""

"""
Q8. Create
    Computer
    Laptop
    GamingLaptop
GamingLaptop should access methods from both parent classes.
"""

"""
Q9. Create
    Hospital
    Doctor
    Surgeon
Surgeon should access methods from both parent classes.
"""