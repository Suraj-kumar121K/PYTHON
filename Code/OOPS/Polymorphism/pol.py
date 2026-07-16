# Polymorphism | poly:- many | morphism:- forms
# 1. Duck Type
# method Overloading
# operator Overloading
# method Overiding

# 1. Method Overriding (Runtime Polymorphism)
# Parent Class
class Parent:
    # Parent Method
    def show(self):
        print("Parent Class")
# Child Class
class Child(Parent):
    # Method Overriding
    def show(self):
        print("Child Class")
# Object Creation
obj = Child()
# Method Calling
# obj.show()

# 2. Method Overloading (Using *args)
# Class
class Demo:

    # Method
    def add(self, *args):
        print(sum(args))

# Object Creation
obj = Demo()

# Method Calling
# obj.add(10, 20)
# obj.add(10, 20, 30)

# Duck Typing (Polymorphism)
# First Class
class Dog:

    # Method
    def sound(self):
        print("Dog Barks")
# Second Class
class Cat:
    # Method
    def sound(self):
        print("Cat Meows")
# Function
def make_sound(animal):
    animal.sound()
# Object Creation
dog = Dog()
cat = Cat()
# Function Calling
# make_sound(dog)
# make_sound(cat)

# Example (+ Operator Overloading)
# Class
class Number:
    # Constructor
    def __init__(self, value):
        self.value = value

    # Operator Overloading (+)
    def __add__(self, other):
        return self.value + other.value
# Object Creation
n1 = Number(10)
n2 = Number(20)

# Operator Calling
# print(n1 + n2)


# Method Overriding
class Parent:
    def method(self):
        pass
class Child(Parent):
    def method(self):
        pass
obj = Child()
# obj.method()

# Parent Class
class Parent:
    # Parent Method
    def show(self):
        print("This is Parent Class")

# Child Class
class Child(Parent):
    # Method Overriding
    def show(self):
        print("This is Child Class")

# Object Creation
obj = Child()

# Method Calling
# obj.show()