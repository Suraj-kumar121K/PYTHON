"""
Create an abstract class Animal with an abstract method sound().
Create Dog and Cat classes.
"""
# ABC aur abstractmethod import kiya
from abc import ABC, abstractmethod   
# Abstract Class banayi
class Animal(ABC):
    # Abstract method banaya (sirf declaration hai, implementation nahi)
    @abstractmethod
    def sound(self):
        pass

# Child Class 1 banayi jo Animal class ko inherit karti hai
class Dog(Animal):

    # Abstract method sound() ko implement kiya
    def sound(self):
        print("Dog says Bark")

# Child Class 2 banayi jo Animal class ko inherit karti hai
class Cat(Animal):

    # Abstract method sound() ko implement kiya
    def sound(self):
        print("Cat says Meow")

# Dog class ka object create kiya
dog = Dog()
# Cat class ka object create kiya
cat = Cat()
# Dog ka sound method call kiya
# dog.sound()
# Cat ka sound method call kiya
# cat.sound()

# Create an abstract class Shape with an abstract method area().
# Create Circle and Rectangle classes.
from abc import ABC, abstractmethod  
class Shape(ABC):
    @abstractmethod 
    def area(self):
        pass
class circle(Shape):
    def area(self):
        print("This is circle")
class Rectangle(Shape):
    def area(self):
        print("This is Rectangle")

cir = circle()
rect = Rectangle()
cir.area()
rect.area()

# Create an abstract class Payment with an abstract method pay().
# Create UPI, CreditCard, and Cash classes.


# Create an abstract class DataLoader with an abstract method load_data().
# Create CSVLoader, ExcelLoader, and SQLLoader classes.


# Create an abstract class Database with two abstract methods connect() and disconnect().
# Create MySQL and MongoDB classes.


# Create an abstract class BankAccount with abstract methods deposit() and withdraw().
# Create SavingsAccount and CurrentAccount classes.


# Create an abstract class FileHandler with abstract methods read() and write().
# Create TextFile and CSVFile classes.


# Create an abstract class Machine with an abstract method work().
# Create Printer and Scanner classes.