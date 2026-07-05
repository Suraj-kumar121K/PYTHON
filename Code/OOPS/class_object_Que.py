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