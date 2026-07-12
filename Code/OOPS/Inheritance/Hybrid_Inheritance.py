"""
5. Hybrid Inheritance
Hybrid = Multiple + Multilevel

Question 5
Create
GrandFather
Father inherits GrandFather
Mother
Child inherits Father and Mother
Call all methods.
"""
class GrandFather:
    def land(self):
        print("GrandFather has land")
class Father(GrandFather):
    def car(self):
        print("Father has car")
class Mother:
    def jewellery(self):
        print("Mother has jewellery")
class Child(Father, Mother):
    def laptop(self):
        print("Child has laptop")
c = Child()
# c.land()
# c.car()
# c.jewellery()
# c.laptop()

# ============================================
# 5. HYBRID INHERITANCE (10 Questions)
# ============================================
# Q1. Create GrandFather -> Father, Mother,
# then Child(Father, Mother).

# Q2. Create Animal -> Dog, Pet, then PetDog(Dog, Pet).

# Q3. Create Person -> Employee, Trainer, then Manager(Employee, Trainer).

# Q4. Create Vehicle -> Car, Electric, then ElectricCar(Car, Electric).

# Q5. Create Book -> EBook, Downloadable, then KindleBook(EBook, Downloadable).

# Q6. Create Mobile -> SmartPhone, Camera, then FlagshipPhone(SmartPhone, Camera).

# Q7. Create School -> Teacher, Researcher, then Professor(Teacher, Researcher).

# Q8. Create Computer -> Laptop, TouchScreen, then ConvertibleLaptop(Laptop, TouchScreen).

# Q9. Create Hospital -> Doctor, Surgeon, then ChiefDoctor(Doctor, Surgeon).

# Q10. Create Bank -> Account, Loan, then PremiumAccount(Account, Loan).

# ================================
# Hybrid Inheritance Practice
# ================================
# Q1
# Create:
# GrandFather
# Father inherits GrandFather
# Mother
# Child inherits Father and Mother
# Call all methods.

# Q2
# Create:
# Animal
# Dog inherits Animal
# Pet
# PetDog inherits Dog and Pet
# Call all methods.

# Q3
# Create:
# Person
# Employee inherits Person
# Trainer
# Manager inherits Employee and Trainer
# Call all methods.

# Q4
# Create:
# Vehicle
# Car inherits Vehicle
# Electric
# ElectricCar inherits Car and Electric
# Call all methods.

# Q5
# Create:
# Book
# EBook inherits Book
# Downloadable
# KindleBook inherits EBook and Downloadable
# Call all methods.

# Q6
# Create:
# Mobile
# SmartPhone inherits Mobile
# Camera
# FlagshipPhone inherits SmartPhone and Camera
# Call all methods.

# Q7
# Create:
# School
# Teacher inherits School
# Researcher
# Professor inherits Teacher and Researcher
# Call all methods.

# Q8
# Create:
# Computer
# Laptop inherits Computer
# TouchScreen
# ConvertibleLaptop inherits Laptop and TouchScreen
# Call all methods.

# Q9
# Create:
# Hospital
# Doctor inherits Hospital
# Surgeon
# ChiefDoctor inherits Doctor and Surgeon
# Call all methods.

# Q10
# Create:
# Bank
# Account inherits Bank
# Loan
# PremiumAccount inherits Account and Loan
# Call all methods.