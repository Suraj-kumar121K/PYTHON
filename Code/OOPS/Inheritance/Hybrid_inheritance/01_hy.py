class Person1:
    def show_person(self):
        print("I am a Person")


# Hierarchical Inheritance
class Student1(Person1):
    def show_student(self):
        print("I am a Student")

class Teacher(Person1):
    def show_teacher(self):
        print("I am a Teacher")

# Multiple Inheritance
class TeachingAssistant1(Student1, Teacher):
    def show_ta(self):
        print("I am a Teaching Assistant")
# Object
# ta = TeachingAssistant1()
# ta.show_person()
# ta.show_student()
# ta.show_teacher()
# ta.show_ta()

# Hybrid Inheritance me constructor wala example
class Person:
    def __init__(self, name):
        self.name = name
        print("Person Constructor")

class Student(Person):
    def __init__(self, name, roll_no):
        Person.__init__(self, name)
        self.roll_no = roll_no
        print("Student Constructor")

class Teacher(Person):
    def __init__(self, name, subject):
        Person.__init__(self, name)
        self.subject = subject
        print("Teacher Constructor")

class TeachingAssistant(Student, Teacher):
    def __init__(self, name, roll_no, subject):
        Student.__init__(self, name, roll_no)
        Teacher.__init__(self, name, subject)
        print("Teaching Assistant Constructor")

    def display(self):
        print("Name:", self.name)
        print("Roll No:", self.roll_no)
        print("Subject:", self.subject)
ta = TeachingAssistant("Rahul", 101, "Python")
# ta.display()

"""
Q1. Person → Student, Teacher → Monitor
Parent Class: Person
        name

Child Class 1: Student
        roll_no

Child Class 2: Teacher
        subject

Hybrid Class: Monitor(Student, Teacher)
        section

Create object:
m1 = Monitor("Rahul", 101, "Python", "A")
"""



"""
Q2. Vehicle → Car, Bike → ElectricVehicle
Parent
    brand
Car
    model
Bike
    engine_cc
ElectricVehicle(Car, Bike)
    battery
Object:
e1 = ElectricVehicle("Tata", "Nexon", 150, "40 kWh")
"""

"""
Q3. Employee → Developer, Tester → TeamLead
Employee
    name

Developer
    language

Tester
    tool

TeamLead
    team_name

Object:
    t1 = TeamLead("Suraj", "Python", "Selenium", "Analytics")
"""

"""
Q4. Animal → Dog, Cat → Pet
Animal
    name
Dog
    breed
Cat
    color
Pet
    owner

Object:
p1 = Pet("Tommy", "Labrador", "Brown", "Rahul")
"""


"""
Q5. College → Student, Faculty → HOD
College
    college_name
Student
    roll_no
Faculty
    subject
HOD
    department

Object:
h1 = HOD("ABC College", 101, "Python", "Computer Science")
"""


"""
Q6. Bank → SavingAccount, CurrentAccount → PremiumAccount
Bank  
    bank_name
SavingAccount
    account_no
CurrentAccount
    ifsc
PremiumAccount
    balance
Object:
    p1 = PremiumAccount("SBI", 12345, "SBIN0001", 50000)
"""


"""
Q7. Person → Employee, Customer → Manager
Parent Class: Person
    Attributes:
    name
    age

Child 1: Employee
    employee_id

Child 2: Customer
    customer_id

Hybrid Class: Manager(Employee, Customer)
    department

Object
m1 = Manager("Suraj", 24, "EMP101", "CUS501", "IT")
"""

"""
Q8. Device → Laptop, Mobile → SmartDevice
Device:
    company
Laptop:
    ram
Mobile:
    camera
SmartDevice:
    price

Object
s1 = SmartDevice("HP", "16GB", "64MP", 65000)
"""

"""
Q9. University → Student, Professor → ResearchAssistant
University:
    university_name
Student:
    roll_no
Professor:
    subject
ResearchAssistant:
    stipend
Object
r1 = ResearchAssistant("MAKAUT", 101, "Python", 12000)
"""

"""
Q10. Vehicle → Car, Truck → Transport
Vehicle:
    brand
Car:
    model
Truck:
    capacity
Transport:
    owner_name
Object
t1 = Transport("Tata", "Nexon", "20 Ton", "Rahul")
"""

"""
Q11. Hospital → Doctor, Nurse → Surgeon
Hospital:
    hospital_name
Doctor:
    specialization
Nurse:
    experience
Surgeon:
    surgery_type
Object
s1 = Surgeon("AIIMS", "Cardiology", 8, "Heart Surgery")
"""
