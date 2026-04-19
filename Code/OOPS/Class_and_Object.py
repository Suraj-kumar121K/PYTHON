""" --> What is OOPS
OOPS is a programming style that organizes code into classes and objects —
making it easier to understand, reuse, and maintain.

--> What is Class
    Class is a blueprint for creating objects.

--> Syntax
    class ClassName:
    # attributes
    # methods
      
 --> Example
class Employee:  # Class
    name = "Suraj"
    language = "Python"
    salary = 100000

suraj = Employee()   # Object
print(suraj.name, suraj.language) """ 

# class creation
class Suraj:
    name="Suraj"
    color="white"  # Attributes
    live="Noida"
    age="23"
# Create Object
# name = Suraj()
# print(name.color)

# Create a class Laptop with attributes: brand, RAM, Price.
# Create 2 objects
# with different values.

class Laptop:
    brand = "default"
    RAM = "8GB"
    price = "1 Lakh"
    
laptop1 = Laptop()
laptop1.brand = "Macbook"
laptop1.RAM = "16GB"
print("Laptop1 Brand - ", laptop1.brand)

laptop2 = Laptop()
laptop2.brand = "Lenovo"
print("Laptop2 Brand - ", laptop2.brand)