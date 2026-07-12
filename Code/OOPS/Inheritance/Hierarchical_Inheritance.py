"""
4. Hierarchical Inheritance
Question 4
Create parent class Vehicle.
Create child classes
Car
Bike
Both should inherit from Vehicle.
"""
# Solution
class Vehicle:
    def fuel(self):
        print("Vehicle uses fuel")
class Car(Vehicle):
    def wheels(self):
        print("Car has 4 wheels")
class Bike(Vehicle):
    def wheels(self):
        print("Bike has 2 wheels")
c = Car()
b = Bike()
# c.fuel()
# c.wheels()
# b.fuel()
# b.wheels()

# ============================================
# 4. HIERARCHICAL INHERITANCE (10 Questions)
# ============================================
# Q1. Create parent class Animal. Create child classes Dog and Cat.

# Q2. Create parent class Vehicle. Create child classes Car and Bike.

# Q3. Create parent class Employee. Create child classes Developer and Tester.

# Q4. Create parent class Shape. Create child classes Circle and Rectangle.

# Q5. Create parent class Person. Create child classes Student and Teacher.

# Q6. Create parent class Book. Create child classes Novel and Magazine.

# Q7. Create parent class Mobile. Create child classes Android and iPhone.

# Q8. Create parent class Bank. Create child classes SBI and HDFC.

# Q9. Create parent class Appliance. Create child classes TV and Refrigerator.

# Q10. Create parent class Fruit. Create child classes Apple and Mango.

# ==========================================
# Hierarchical Inheritance (10 Questions)
# ==========================================

# Q1
# Create parent class Animal.
#
# Create child classes:
# - Dog
# - Cat
#
# Both should inherit from Animal.
# Each child should have its own method.


# Q2
# Create parent class Person.
#
# Create child classes:
# - Student
# - Teacher
#
# Both should inherit from Person.
# Each child should display its own information.


# Q3
# Create parent class Employee.
#
# Create child classes:
# - Developer
# - Tester
#
# Both should inherit from Employee.
# Each child should have its own work method.


# Q4
# Create parent class Vehicle.
#
# Create child classes:
# - Car
# - Bike
#
# Both should inherit from Vehicle.
# Each child should have its own method.


# Q5
# Create parent class Shape.
#
# Create child classes:
# - Circle
# - Rectangle
#
# Both should inherit from Shape.
# Each child should have its own method.


# Q6
# Create parent class Book.
# Create child classes:
# - Novel
# - Magazine
# Both should inherit from Book.
# Each child should display its own details.


# Q7
# Create parent class Mobile.
# Create child classes:
# - Android
# - iPhone
# Both should inherit from Mobile.
# Each child should have its own feature method.


# Q8
# Create parent class Bank.
#
# Create child classes:
# - SBI
# - HDFC
#
# Both should inherit from Bank.
# Each child should display its own services.


# Q9
# Create parent class Hospital.
#
# Create child classes:
# - Doctor
# - Nurse
#
# Both should inherit from Hospital.
# Each child should have its own duty method.


# Q10
# Create parent class Appliance.
#
# Create child classes:
# - WashingMachine
# - Refrigerator
#
# Both should inherit from Appliance.
# Each child should have its own function method.