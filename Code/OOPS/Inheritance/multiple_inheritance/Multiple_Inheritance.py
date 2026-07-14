# ============================================
# Multiple Inheritance – 10 Practice Questions
# ============================================
"""
Question 2
Create class Father with method father_skill().
Create class Mother with method mother_skill().
Create class Child that inherits from both classes.
Call both methods.
"""
# Solution
class Father:
    def __init__(self, father_name):
        self.father_name = father_name
    def show_father(self):
        print("Father Name:", self.father_name)
class Mother:
    def __init__(self, mother_name):
        self.mother_name = mother_name
    def show_mother(self):
        print("Mother Name:", self.mother_name)
class Child(Father, Mother):
    def __init__(self, father_name, mother_name, child_name):
        Father.__init__(self, father_name)
        Mother.__init__(self, mother_name)
        self.child_name = child_name
    def show_child(self):
        print("Child Name:", self.child_name)
c1 = Child("Ram", "Sita", "Aman")
# c1.show_father()
# c1.show_mother()
# c1.show_child()

"""
Q2
Create class Writer with method write().
Create class Singer with method sing().
Create class Artist that inherits from both classes.
Call both methods.
"""
class Writer:
    def writer(self):
        print("Writing a Book")
class Singer:
    def sing(self):
        print("tum hi hai")
class Artist(Writer, Singer):
    def name(self):
        print("sonu nigam")
a1 = Artist()
# a1.writer()
# a1.sing()
# a1.name()


# ============================================
# Multiple Inheritance + Constructor Practice
# ============================================
"""
Q1. Employee Management System
Create class Person:
Constructor:
name
age

Method:
display_person()

Create class Salary:
Constructor:
salary
department

Method:
display_salary()

Create class Manager:
Inherit from both Person and Salary
Constructor me dono parent constructors call karo.
Extra attribute:
experience

Method:
display_manager()

Object create karo aur sab methods call karo.
m1 = Manager("Suraj", 25, 50000, "IT", 3)
"""
class Person:
    def __init__(self, name, age):
        self.name = name
        self.age = age
    def display_person(self):
        print("Name :", self.name)
        print("Age :", self.age)
class Salary:
    def __init__(self, salary, department):
        self.salary = salary
        self.department = department
    def display_salary(self):
        print("Net Salary :", self.salary)
        print("Net Department :", self.department)
class Manager(Person, Salary):
    def __init__(self,name, age, salary, department, experience):
        Person.__init__(self, name, age)
        Salary.__init__(self, salary, department)
        self.experience = experience
    def show_experience(self):
        Person.display_person(self)
        Salary.display_salary(self)
        print("Total Experience :", self.experience)
m1 = Manager("Suraj", 25, 50000, "IT", 3)
# m1.show_experience()

"""
Q2. Student Result System
Create class Student:

Constructor:
name
roll_no
Method:
show_student()

Create class Marks:

Constructor:
python_marks
sql_marks
Method:
show_marks()

Create class Result:
Inherit from Student and Marks
Constructor me dono parent constructors call karo.
Extra attribute:
grade
Method:
show_result()

Object:
r1 = Result("Rahul", 101, 90, 85, "A")
"""
class Student:
    def __init__(self, name, roll_no):
        self.name = name
        self.roll_no = roll_no
    def show_student(self):
        print("Name:- ",self.name)
        print("ROLL NO:- ", self.roll_no)
class Marks:
    def __init__(self, python_marks, sql_marks):
        self.python_marks = python_marks
        self.sql_marks = sql_marks
    def show_marks(self):
        print("Total Python Marks :", self.python_marks)
        print("Total SQL Marks :", self.sql_marks)
class Result:
    def __init__(self, name, roll_no, python_marks, sql_marks, grade):
        Student.__init__(self, name, roll_no)
        Marks.__init__(self, python_marks, sql_marks)
        self.grade = grade
    def show_result(self):
        Student.show_student(self)
        Marks.show_marks(self)
        print("Grade: ", self.grade)
r1 = Result("Rahul", 101, 90, 85, "A")
# r1.show_result()
"""
Q3. Vehicle Service System
Create class Vehicle:
Constructor:
    brand
    model

Method:
    display_vehicle()

Create class Service:
Constructor:
    service_type
    cost

Method:
display_service()

Create class CarService:
Inherit from both classes.
Extra attribute:
    customer_name

Method:
display_customer()

Object:
c1 = CarService("Tata", "Nexon", "Engine Repair", 5000, "Amit")
"""
class Vechicle:
    def __init__(self, brand, model):
        self.brand = brand
        self.model = model
    
    def display_vehicle(self):
        print("Brand: ", self.brand)
        print("Model: ", self.model)
        
class Service:
    def __init__(self, service_type, cost):
        self.service_type = service_type
        self.cost = cost
    def display_service(self):
        print("Service Type: ", self.service_type)
        print("Cost: ", self.cost)
        
class CarService(Vechicle, Service):
    def __init__(self, brand, model, service_type, cost, customer_name):
        Vechicle.__init__(self, brand, model)
        Service.__init__(self, service_type, cost)
        self.customer_name = customer_name
    def display_customer(self):
        Vechicle.display_vehicle(self)
        Service.display_service(self)
        print("Customer Name:- ", self.customer_name)
c1 = CarService("Tata", "Nexon", "Engine Repair", 5000, "Amit")
# c1.display_customer()

"""
Q4. Hospital Management System
Create class Doctor:
Constructor:
    doctor_name
    specialization
Method:
   show_doctor()

Create class Patient:
Constructor:
    patient_name
    patient_problem
Method:
   show_patient()

Create class Appointment:
Inherit from both Doctor and Patient.
    Extra attribute:
    appointment_date

Method:
    show_appointment()
Object:
a1 = Appointment("Dr. Sharma","Cardiologist","Rahul","Heart Problem","13-07-2026")
"""
class Doctor:
    def __init__(self, doctor_name, specialization):
        self.doctor_name = doctor_name
        self.specialization = specialization
        
    def show_doctor(self):
        print("Doctor Name: ", self.doctor_name)
        print("specialization: ", self.specialization)
        
class Patient:
    def __init__(self, patient_name, patient_problem):
        self.patient_name = patient_name
        self.patient_problem = patient_problem
    def show_patient(self):
        print("Patient Name: ", self.patient_name)
        print("Patient Problem: ", self.patient_problem)
        
class Appointment(Doctor, Patient):
    def __init__(self, doctor_name, specialization, patient_name, patient_problem, appointment_date):
        Doctor.__init__(self, doctor_name, specialization)
        Patient.__init__(self, patient_name, patient_problem)
        self.appointment_date = appointment_date
    
    def show_appointment(self):
        Doctor.show_doctor(self)
        Patient.show_patient(self)
        print("Appointment Date:- ", self.appointment_date) 
a1 = Appointment("Dr. Sharma","Cardiologist","Rahul","Heart Problem","13-07-2026")
# a1.show_appointment()

"""
Q5. Online Shopping System
Create class Product:
Constructor:
    product_name
    price
    Method:
    show_product()

Create class Customer:
    Constructor:
    customer_name
    location
    Method:
    show_customer()

Create class Order:
Inherit from both Product and Customer.
    Extra attribute:
    quantity

Method:
    show_order()

Object:
o1 = Order("Laptop",50000,"Suraj","Noida",2)
"""
class Product:
    def __init__(self, product_name ,price):
        self.product_name = product_name
        self.price = price
        
    def show_product(self):
        print("Product Name: ", self.product_name)
        print("Product Price: ", self.price)
        
class Customer:
    def __init__(self, customer_name, location):
        self.customer_name = customer_name
        self.location = location
    def show_customer(self):
        print("Customer Name: ", self.customer_name)
        print("Customer Location: ", self.location)
        
class Order(Product, Customer):
    def __init__(self, product_name ,price, customer_name, location, quantity):
        Product.__init__(self, product_name ,price)
        Customer.__init__(self, customer_name, location)
        self.quantity = quantity
    
    def show_order(self):
        Product.show_product(self)
        Customer.show_customer(self)
        print("Order Quantity:- ", self.quantity)
o1 = Order("Laptop",50000,"Suraj","Noida",2)
o1.show_order()