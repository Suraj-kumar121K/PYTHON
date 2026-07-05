class Student:
    def __init__(self):
        print("Hello World")
# s1 = Student()

# Constructor with Parameters
class Student:
    def __init__(self, name, age):
        self.name = name
        self.age = age
        
    def show(self):
        print("name", self.name)
        print("Age", self.age)
# s1 = Student("Suraj", 21)
# s1.show()

# mobile
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

class Student:
    def __init__(self, name, age):
        self.name = name
        self.age = age
    def show(self):
        print("Name", self.name)
        print("Age", self.age)
# m1 = Student("Rahul", 21)
# m1.show()

# 3. Rectangle Area
class Rectangle:
    def __init__(self, length, width):
        self.length = length
        self.width = width
    def show(self):
        result = self.length * self.width
        print("Area", result)
s1 = Rectangle(10, 5)
# s1.show()

# Multiple Students using Loop
class Student:
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
    
    s = Student(Name, Age)
    # s.show()
    


    