class Employee:
    def __init__(self, name, employee_id):
        self.name = name
        self.__employee_id = employee_id

    def print_detail(self):
        print("Employee ID :", self.__employee_id)

class Manager(Employee):
    def __init__(self, name, employee_id, department):
        super().__init__(name, employee_id)
        self.department = department

class ProjectManager(Manager):
    def __init__(self, name, employee_id, department, project_handled):
        super().__init__(name, employee_id, department)
        self.project_handled = project_handled

    def print_details(self):
        print("Name :", self.name)
        super().print_detail()
        print("Department :", self.department)
        print("Projects :", self.project_handled)

obj1 = ProjectManager(
    "Suraj",
    123,
    "IT",
    ["Training", "YouTube"]
)
# obj1.print_details()

# Practice Question
class Animal:
    def eat(self):
        print("Animal can eat")
class Dog(Animal):
    def bark(self):
        print("Dog can brak")
    
class Puppy(Dog):
    def sleep(self):
        print("Puppy is sleeping")
p = Puppy()
# p.eat()
# p.bark()
# p.sleep()

# Practice Question (Constructor)
class Person:
    def __init__(self, name):
        self.name = name

class Employee(Person):
    def __init__(self, name, company):
        super().__init__(name)
        self.company = company

class Manager(Employee):
    def __init__(self, name, company, salary):
        super().__init__(name, company)
        self.salary = salary

    def display(self):
        print("Name:", self.name)
        print("Company:", self.company)
        print("Salary:", self.salary)

m = Manager("Suraj", "Google", 90000)
# m.display()

# Q1. Student → Marks → Result
class Student:
    def __init__(self, name):
        self.name = name
class Marks(Student):
    def __init__(self, name, python_marks):
        super().__init__(name)
        self.python_marks = python_marks
class Result(Marks):
    def __init__(self, name, python_marks, grade):
        super().__init__(name, python_marks)
        self.grade = grade
    def display(self):
        print("name: ", self.name)
        print("Python Marks: ", self.python_marks)
        print("Grade: ", self.grade)
r1 = Result("Suraj", 90, 1)
# r1.display()

# Q2. Person → Employee → Manager
class Person:
    def __init__(self, name):
        self.name = name

class Employee(Person):
    def __init__(self, name, company):
        super().__init__(name)
        self.company = company

class Manager(Employee):
    def __init__(self, name, company, salary):
        super().__init__(name, company)
        self.salary = salary

    def display(self):
        print("Name:", self.name)
        print("Company:", self.company)
        print("Salary:", self.salary)

m1 = Manager("Suraj", "Google", 90000)
# m1.display()

# Q3. Vehicle → Car → SportsCar
"""
brand
model
top_speed
"""

# Q4. Animal → Dog → Puppy
"""
name
breed
age
"""

# Q5. Book → EBook → PDFBook
"""
title
author
size
"""

# Q6. Mobile → SmartPhone → Android
"""
company
ram
version
"""

# Q7. Bank → SavingAccount → PremiumAccount
"""
account_no
balance
reward_points
"""

# Q8. College → Department → Student
"""
college_name
department
student_name
"""

# Q9. Laptop → Windows → GamingLaptop
"""
brand
ram
graphics_card
"""

# Q10. Hospital → Doctor → Surgeon
"""
hospital_name
doctor_name
specialization
"""