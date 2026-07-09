"""
class Student:
    def __init__(self):
        print("Hello World")
# s1 = Student()
"""
# Constructor with Parameters
"""
class Student:
    def __init__(self, name, age):
        self.name = name
        self.age = age
        
    def show(self):
        print("name", self.name)
        print("Age", self.age)
# s1 = Student("Suraj", 21)
# s1.show()
"""

# mobile
"""
class Mobile:
    def __init__(self, Company, Price):
        self.Company = Company
        self.Price = Price
        
    def show(self):
        print("Company Name: ", self.Company)
        print("Mobile price: ", self.Price)
s1 = Mobile("Samsung", 21000)
s2 = Mobile("Vivo", 25000)
# s1.show() # object ka data print karta hai
# s2.show()
"""
"""
class Students:
    def __init__(self, name, age):
        self.name = name
        self.age = age
    def show(self):
        print("Name", self.name)
        print("Age", self.age)
# m1 = Students("Rahul", 21)
# m1.show()
"""

# 3. Rectangle Area
"""
class Rectangle:
    def __init__(self, length, width):
        self.length = length
        self.width = width
    def show(self):
        result = self.length * self.width
        print("Area", result)
s1 = Rectangle(10, 5)
# s1.show()
"""

# Multiple Students using Loop
"""
class Students:
    def __init__(self, name, age):
        self.name = name
        self.age = age
    def show(self):
        print("Name:- ", self.name)
        print("Age:- ", self.age)
        print("Succesfully Add Name")

for i in range(3):
    Name = input("Enter Name: ")
    Age = int(input("Enter Age: "))
    
    # s = Students(Name, Age)
    # s.show()
"""   
# Constructor Logic Questions
# 1. What is a constructor?
# 2. When is init method called?
# 3. What is a default constructor?
# 4. What is a parameterized constructor?
# 5. What is the main purpose of a constructor?
# Code Practice
# 6. Create a constructor in Student class
"""
class Studen:
    def __init__(self):
        print("Hello")
s1 = Studen()
"""
# 7. Create a parameterized constructor in Car class
# 8. Initialize values in Mobile class using constructor
# 9. Set Employee salary using constructor
# 10. Store Bank balance using constructor
# 11. Explain constructor overloading logic
# 12. How does constructor work in inheritance?
# 13. Call constructor using super()
# 14. Access parent constructor
# 15. Create child constructor
# 16. Explain multiple constructors logic
# 17. Create constructor with default arguments
# 18. Take dynamic values in constructor
# 19. Create object counter using constructor
# 20. Explain private constructor concept
# 21. What is a destructor (del)?
# 22. Create constructor chaining example
# 23. Add validation logic inside constructor
# 24. Create singleton constructor logic
# 25. Create constructor example with inheritance

# =========================================
# 3️⃣ Constructor Practice Questions
# =========================================

# Default constructor ka example banao
# Parameterized constructor ka example banao
# Student class me constructor use karo
# Employee salary constructor se lo
# Book name constructor se initialize karo
# Car model constructor se lo
# Mobile brand constructor me pass karo
# Bank balance constructor me initialize karo
# Animal name constructor se set karo
# Multiple objects constructor ke through banao
    
    
class stdd:
    def __init__(self, name, age):
        self.name = name
        self.age = age
# s1 = stdd("Suraj", 23)
# print(s1.name) 
# print(s1.age) 

# car class
class Car:
    def __init__(self, brand, model, price):
        self.brand = brand
        self.model = model
        self.price = price  
s1 = Car("BMW", "X5", 500000)
# print(s1.brand)
# print(s1.model)
# print(s1.price)

# AttributeError tab aata hai jab aap object ke kisi aise variable (attribute)
# ya method ko access karte ho jo object ke andar bana hi nahi hota.

# 3. Mobile Class
class mobile:
    def __init__(self, company, price):
        self.company = company
        self.price = price
s1 = mobile("VIVO", 15000)
# print(s1.name)
# print(s1.price)

# Create Multiple Objects
class Sk:
    def __init__(self, name, age):
        self.name = name
        self.age = age
# s1 = Sk("Suraj", 22)
# s2 = Sk("Kumar", 26)
# s3 = Sk("Rahul", 28)
# print(s1.name)
# print(s2.name)
# print(s3.name)
# print(s1.age)
# print(s2.age)
# print(s3.age)

class Dog:
    def __init__(self, name, breed):
        self.name = name
        self.breed = breed
# d1 = Dog("Tommy", "Labrador")
# d2 = Dog("Bruno", "German Shepherd")
# print(d1.name, d1.breed)
# print(d2.name, d2.breed)

# Constructor + Method
class Student:
    def __init__(self, name, marks):
        self.name = name
        self.marks = marks
    def display(self):
        print("Name :", self.name)
        print("marks :", self.marks)
# s1 = Student("Suraj", 83)
# s1.display()

class Employee:
    def __init__(self, name, salary):
        self.name = name
        self.salary = salary

    def show(self):
        print(self.name)
        print(self.salary)
# e1 = Employee("Aman", 60000)
# e1.show()

# Default Constructor Value
class Student:
    def __init__(self, name="Unknown", age=0):
        self.name = name
        self.age = age
# s1 = Student()
# print(s1.name)
# print(s1.age)

class Car:
    def __init__(self, brand="No Brand", price=0):
        self.brand = brand
        self.price = price
# c1 = Car()
# print(c1.brand)
# print(c1.price)

"""
Inhe khud solve karo:
3. Create a Product class with id, name, and price.
4. Create a Hospital class with doctor_name and specialization.
5. Create a CricketPlayer class with name, team, and runs.
6. Create a Bike class with brand, model, and price.
7. Create a Customer class with customer_id, name, and mobile.
8. Create a Library class with book_name, author, and copies.
9. Create a Restaurant class with food_name, price, and rating.
10. Create a Company class with company_name, location, and employees.
Bonus Challenge

Ek Student class banao jisme constructor(कन्स्ट्रक्टर) name, age, aur marks le. Ek display()
method banao jo saari details print kare, aur is_pass() method banao jo bataye 
ki student pass hai ya fail (maan lo marks >= 33 pass hai).
"""

# 1. Create a College class with name and city.
# Q2. self.name = name ka matlab?
# Left side (self.name) → Object ka instance variable.
# Right side (name) → Constructor ka parameter.
# s1 = College("BCET", "Durgapur")
# Parameter (name)  ─────►  Instance Variable (self.name)
class College:
    def __init__(self, name, city):
        self.name = name
        self.city = city
s1 = College("BCET", "Durgapur")
# print(s1.name)
# print(s1.city)

# 2. Create a Teacher class with name, subject, and salary. 
class Teacher:
    def __init__(self, name, subject, salary):
        self.name = name
        self.subject = subject
        self.salary = salary
s1 = Teacher("Suraj", "Math", 25000)
# print(s1.name)
# print(s1.subject)
# print(s1.salary)

"""
Constructor + Method Practice (20 Questions)
1. Student Class
Create a Student class with name, age, and marks.
Create a display() method to print all details.
Create an is_pass() method to check if the student passed (marks >= 33).

2. Employee Class
Create an Employee class with name, salary, and department.
Create a display() method.
Create a bonus() method that prints 10% bonus.

3. Car Class
Create a Car class with brand, model, and price.
Create a display() method.
Create an expensive() method that checks if the price is greater than 10,00,000.

4. BankAccount Class
Create a BankAccount class with holder_name and balance.
Create a display() method.
Create an is_rich() method that checks if the balance is greater than 1,00,000.

5. Book Class
Create a Book class with title, author, and pages.
Create a display() method.
Create an is_big_book() method that checks if the book has more than 300 pages.

6. Mobile Class
Create a Mobile class with company, model, and price.
Create a display() method.
Create a discount_price() method that gives a 10% discount.

7. Movie Class
Create a Movie class with title, rating, and duration.
Create a display() method.
Create a hit_or_flop() method (rating >= 8 means Hit).

8. Product Class
Create a Product class with product_name, price, and quantity.
Create a display() method.
Create a total_cost() method.

9. Teacher Class
Create a Teacher class with name, subject, and salary.
Create a display() method.
Create an annual_salary() method.

10. Laptop Class
Create a Laptop class with brand, ram, and price.
Create a display() method.
Create an upgrade_ram() method that adds 8GB RAM.

11. Hospital Class
Create a Hospital class with doctor_name, specialization, and experience.
Create a display() method.
Create an is_experienced() method (experience >= 10 years).

12. College Class
Create a College class with name, city, and students.
Create a display() method.
Create an is_large_college() method (students > 5000).

13. CricketPlayer Class
Create a CricketPlayer class with name, team, and runs.
Create a display() method.
Create a century() method that checks if runs are >= 100.

14. Bike Clas
Create a Bike class with brand, model, and mileage.
Create a display() method.
Create a good_mileage() method (mileage >= 50).

15. Customer Clas
Create a Customer class with name, age, and city.
Create a display() method.
Create an is_senior_citizen() method (age >= 60).

16. Restaurant Clas
Create a Restaurant class with food_name, price, and rating.
Create a display() method.
Create a recommended() method (rating >= 4.5).

17. Company Class
Create a Company class with name, employees, and location.
Create a display() method.
Create an is_big_company() method (employees >= 1000).

18. Animal Class
Create an Animal class with name, type, and age.
Create a display() method.
Create an is_old() method (age >= 10).

19. Library Class
Create a Library class with book_name, author, and copies.
Create a display() method.
Create an available() method that checks whether copies are greater than 0.

20. CinemaTicket Class
Create a CinemaTicket class with movie_name, seat_number, and price.
Create a display() method.
Create an is_premium() method that checks if the ticket price is greater than 500.
"""
