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
Create an object and call both methods.
"""
class Book:
    def __init__(self, title):
        self.title = title     
    def display_title(self):
        print("Title: ", self.title)
class EBook(Book):
    def __init__(self, title ,file_size):
        super().__init__(title)
        self.file_size = file_size
        
    def display_size(self):
        self.display_title()
        print("File size:- ", self.file_size)
b1 = EBook("sk", 500)
# b1.display_size()
        
        
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
class Employee:
    def __init__(self, name):
        self.name = name    
    def display_name(self):
        print("Name : ", self.name)
class Manager(Employee):
    def __init__(self, name, salary):
        super().__init__(name)
        self.salary = salary
        
    def display_salary(self):
        self.display_name()
        print("Salary:- ", self.salary)
b1 = Manager("suraj", 15000)
# b1.display_salary()

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
class Mobile:
    def __init__(self, company):
        self.company = company
    def display_company(self):
        print("company Name:- ", self.company)
class SmartPhone(Mobile):
    def __init__(self, company, ram):
        super().__init__(company)
        self.ram = ram
    def display_ram(self):
        self.display_company()
        print("Ram:- ", self.ram)
s1 = SmartPhone("VIVO", "8GB")
# s1.display_ram()

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
class Shape:
    def __init__(self, color):
        self.color = color
    def dis_color(self):
        print("color: ", self.color)
class Circle(Shape):
    def __init__(self, color, radius):
        super().__init__(color)
        self.radius = radius
    def display_radius(self):
        self.dis_color()
        print("Radius:", self.radius)
c1 = Circle("Red", 10)
# c1.display_radius()

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
class Bank:
    def __init__(self, bank_name):
        self.bank_name = bank_name
    def display_bank(self):
        print("Bank Name: ", self.bank_name)
class Customer(Bank):
    def __init__(self, bank_name, customer_name):
        super().__init__(bank_name)
        self.customer_name = customer_name
    def display_custome(self):
        self.display_bank()
        print("customer name:", self.customer_name)
c1 = Customer("SBI", "Suraj")
# c1.display_custome()

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
class Laptop:
    def __init__(self, company):
        self.company = company
    def display_company(self):
        print("Company Name: ", self.company)
class GamingLaptop(Laptop):
    def __init__(self, company, gpu):
        super().__init__(company)
        self.gpu = gpu
    def display_gpu(self):
        self.display_company()
        print("GPU Name:", self.gpu)
c1 = GamingLaptop("HP", "NVIDIA GeForce RTX 5090")
# c1.display_gpu()

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
class Hospital:
    def __init__(self, hospital_name):
        self.hospital_name = hospital_name
    def display_hospital(self):
        print("Hospital Name: ", self.hospital_name)
class Doctor(Hospital):
    def __init__(self, color, specialization):
        super().__init__(color)
        self.specialization = specialization
    def display_specialization(self):
        self.display_hospital()
        print("specialization: ", self.specialization)
c1 = Doctor("GNU", "kumar")
# c1.display_specialization()