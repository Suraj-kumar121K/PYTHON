"""
3. Multilevel Inheritance
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
# Q1. Create Person -> Employee -> Manager.

# Q2. Create Animal -> Dog -> Puppy.

# Q3. Create Vehicle -> Car -> SportsCar.

# Q4. Create Book -> EBook -> KindleBook.

# Q5. Create Mobile -> SmartPhone -> AndroidPhone.

# Q6. Create Shape -> Rectangle -> Square.

# Q7. Create School -> Teacher -> Principal.

# Q8. Create Bank -> Account -> SavingsAccount.

# Q9. Create Computer -> Laptop -> GamingLaptop.

# Q10. Create Hospital -> Doctor -> Surgeon.

# ============================================
# MULTILEVEL INHERITANCE (10 Questions)
# ============================================
# Q1
# Create
# Person
# Employee
# Manager
#
# Manager should access methods from both parent classes.

# Q2
# Create
# Animal
# Dog
# Puppy
#
# Puppy should access methods from both parent classes.

# Q3
# Create
# Vehicle
# Car
# SportsCar
#
# SportsCar should access methods from both parent classes.

# Q4
# Create
# Book
# EBook
# KindleBook
#
# KindleBook should access methods from both parent classes.

# Q5
# Create
# Mobile
# SmartPhone
# AndroidPhone
#
# AndroidPhone should access methods from both parent classes.

# Q6
# Create
# Shape
# Rectangle
# Square
#
# Square should access methods from both parent classes.

# Q7
# Create
# School
# Teacher
# Principal
#
# Principal should access methods from both parent classes.

# Q8
# Create
# Bank
# Account
# SavingsAccount
#
# SavingsAccount should access methods from both parent classes.

# Q9
# Create
# Computer
# Laptop
# GamingLaptop
#
# GamingLaptop should access methods from both parent classes.

# Q10
# Create
# Hospital
# Doctor
# Surgeon
#
# Surgeon should access methods from both parent classes.