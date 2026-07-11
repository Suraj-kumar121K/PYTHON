# Q1. Create a Person class with `name` and `display()` method. Inherit it into Student class.
class Person: # parent (base) class hai.
    def __init__(self, name):
        self.name = name

    def display(self):
        print("Name:", self.name)
#Student ek child class hai.
class Student(Person): # (Person) ka matlab Student Person class ko inherit kar raha hai.
    def study(self):
        print("Student is studying")
s = Student("Suraj")
# s.display()
# s.study()

# Q2. Create an Animal class with eat() method. Inherit it into Dog class and call both methods.
class Animal:
    def eat(self):
        print("Animal is eating")       
class Dog(Animal):
    def bark(self):
        print("Dog is barking")
d = Dog()
# d.eat()
# d.bark()

# Q3. Create a Vehicle class with start() method. Create a Car class that inherits from it.
class Vehicle:
    def start(self):
        print("Vehicle started")
class Car(Vehicle):
    def drive(self):
        print("Car is driving")
c = Car()
# c.start()
# c.drive()

# Q4. Create an Employee class with company variable. Access it from Developer class.
class Employee:
    def __init__(self):
        self.company = "Google"

class Developer(Employee):
    def show(self):
        print("Company :", self.company)
d = Developer()
# d.show()
    
# Q5. Create a Bird class with fly() method. Create Parrot class using inheritance.
class Bird:
    def fly(self):
        print("Bird is fly")
class Parrot(Bird):
    def speak(self):
        print("Parrot can speak")
p = Parrot()
# p.fly()
# p.speak()

# Q6. Create a Shape class with draw() method. Create Circle class.
class Shape:
    def draw(self):
        print('Drawing Shape')
        
class Circle(Shape):
    def area(self):
        print("Are of Circle")
c = Circle()
# c.draw()
# c.area()

# Q7. Create a Bank class with bank_name variable. Inherit it into Customer.
class Bank:
    def __init__(self):
        self.bank_name = "State Bank"
class Customer(Bank):
    def show(self):
        print("Bank Name :", self.bank_name)
c = Customer()
c.show()

