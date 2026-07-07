# 1️⃣ Class Logic Questions
# 1. Create a Student class with name and marks
class Student:
    def show(self, name, marks):
        self.name = name
        self.marks = marks
    def student_det(self):
        print("Name:- ", self.name)
        print("Marks:- ", self.marks)
s1 = Student() # Student() = Class ka object banana and s1 = Object Reference Variable
s1.show("Suraj", 98) # Method Call with Arguments
# s1.student_det() # Method Call
        
# 2. Create a Car class with brand and speed
class Car:
    def __init__(self, brand, speed): #Constructor / Parameterized Constructor
        self.brand = brand # Instance Variable Initialization
        self.speed = speed # Instance Variable Initialization
    def show(self): # Instance Method / Normal Method
        print("brand:- ", self.brand) # Object ka brand value access karna
        print("speed:- ", self.speed)
# s1 = Car("Tata Motors", 25)
# s1.show()
# 3. Create a Mobile class with company and price
class Mobile:
    def __init__(self, company, price):
        self.company = company
        self.price = price
    def show(self):
        print("company Name: ",self.company)
        print("price: ",self.price)
# s1 = Mobile("vivo", 15000)
# s1.show()
    
# 4. Create an Employee class with salary calculation
class Employee:
    def __init__(self, name, salary, bouns):
        self.name = name
        self.salary = salary
        self.bouns = bouns
    def clas(self):
        total_salary = self.salary + self.bouns
        print("Name: ",self.name)
        print("Name: ",total_salary)
# s1 = Employee("Suraj", 16000, 5000)
# s1.clas()
    
# 5. Create a Book class with author and price
class Book:
    def __init__(self, author, price):
        self.author = author
        self.price = price
    def clas(self):
        print("Author Name: ",self.author)
        print("Price: ",self.price)
# s1 = Book("Chetan Bhagat", 230)
# s1.clas()
   
# 6. Create a Laptop class with RAM and processor
class Laptop:
    def __init__(self, ram, processor):
        self.ram = ram
        self.processor = processor
    def proce(self):
        print("RAM: ",self.ram)
        print("processor: ",self.processor)
# s1 = Laptop("8GB", "Intel i5")
# s1.proce()

# 7. Create a Bank class with balance details

# 8. Create an Animal class with a sound method

# 9. Create a Movie class with rating information

# 10. Create a College class with student count

# 2️⃣ Object Logic Questions
# 1. Create an object of Student class
# 2. Create 3 objects of Car class
# 3. Create different objects of Mobile class
# 4. Store different salaries in Employee objects
# 5. Store different authors in Book objects
# 6. Create multiple objects of Animal class
# 7. Print Laptop object data
# 8. Create a Bank account object
# 9. Display Movie object rating
# 10 Print College object name
class College:
    def __init__(self, name):
        self.name = name
# c1 = College("ABC College")
# print(c1.name)

#3️⃣ Variable Logic Questions
# 1. What is an instance variable?
# An instance variable is a variable that belongs to an object.
# It is created using self.

class Student:
    def __init__(self):
        self.name = "Suraj"
# s1 = Student()
# print(s1.name)
# 2. What is a class variable?
# A class variable is shared by all objects of the class.

class Car:
    company = "Toyota"
# c1 = Car()
# c2 = Car()

# print(c1.company)
# print(c2.company)
# 3. What is a global variable?
# A global variable is created outside the class or function.

name = "Python"
class Test:
    def show(self):
        print(name)
# t1 = Test()
# t1.show()

# 4. What is a local variable?
# A local variable is created inside a function.

class Demo:
    def show(self):
        x = 10
        print(x)
# d1 = Demo()
# d1.show()

# 5. What type of variable is self.name?
# self.name is an instance variable.
class Student:
    def __init__(self):
        self.name = "Aman"
# s1 = Student()
# print(s1.name)
# 6. Create a name variable in Student class
class Student:
    def __init__(self):
        self.name = "suraj"
# s1 = Student()
# print(s1.name)

# 7. Create a company variable in Car class


# 8. Store balance in Bank class variable
# 9. Update price variable in Mobile class
# 10. Print Employee salary variable
# Intermediate
# 11. Explain the difference between instance variable and class variable
# 12. How do all objects share a class variable?
# 13. Update a variable using an object
# 14. Initialize variables using constructor
# 15. Write logic to delete a variable
# Advanced
# 16. Create a dynamic variable
# 17. Create an object counter variable
# 18. Use a private variable
# 19. Use a protected variable
# 20. Access variables using inheritance


# 4️⃣ Method Logic Questions
# Basic
# 1. What is a normal method?
# 2. What is a static method?
# 3. What is a class method?
# 4. What is the use of self keyword?
# 5. What is the use of cls keyword?
# Code Practice
# 6. Create a display() method in Student class
# 7. Create a speed() method in Car class
# 8. Create a deposit() method in Bank class
# 9. Create a withdraw() method
# 10. Create a show_data() method in Mobile class
# Intermediate
# 11. Explain method calling logic
# 12. Call one method inside another method
# 13. Create an example of static method
# 14. Create an example of class method
# 15. Perform calculation inside instance method
# Advanced
# 16. Create an example of method overriding
# 17. Explain method overloading logic
# 18. Call parent method using super()
# 19. Use a private method
# 20. Create a polymorphism method example
# 21. Use magic method (str)
# 22. Use magic method (len)
# 23. Create an abstract method
# 24. Create a method chaining example
# 25. Create a recursive method
# 26. Create Getter and Setter methods
# 27. Use decorator methods
# 28. Compare static method and class method
# 29. Access parent and child methods
# 30. Call methods using multiple inheritance


# 5️⃣ Constructor Logic Questions
# Basic
# 1. What is a constructor?
# 2. When is init method called?
# 3. What is a default constructor?
# 4. What is a parameterized constructor?
# 5. What is the main purpose of a constructor?
# Code Practice
# 6. Create a constructor in Student class
class Studen:
    def __init__(self):
        print("Hello")
s1 = Studen()

# 7. Create a parameterized constructor in Car class

# 8. Initialize values in Mobile class using constructor
# 9. Set Employee salary using constructor
# 10. Store Bank balance using constructor
# Intermediate
# 11. Explain constructor overloading logic
# 12. How does constructor work in inheritance?
# 13. Call constructor using super()
# 14. Access parent constructor
# 15. Create child constructor
# Advanced
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


# 6️⃣ Full OOPS Mixed Logic Questions (Advanced)
# 1. Create an ATM Machine project
# 2. Create a Library Management System
# 3. Create a Student Report Card System
# 4. Create a Bank Management System
# 5. Create an Employee Payroll System
# 6. Create an Online Shopping Cart
# 7. Create a Hospital Management System
# 8. Create a Railway Reservation System
# 9. Create a Hotel Booking System
# 10. Create a School Management System
# 11. Create an E-commerce project
# 12. Create a Quiz Application
# 13. Create an Inventory Management System
# 14. Create a Parking System
# 15. Create a Voting System
# 16. Create a Bus Ticket Booking System
# 17. Create a Restaurant Billing System
# 18. Create a Cricket Score System
# 19. Create a Movie Ticket Booking System
# 20. Create an Online Exam System