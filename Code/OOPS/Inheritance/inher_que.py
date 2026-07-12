# 1. Basic Inheritance (10 Questions)
# Q1. Create a Person class and inherit it into Student.
class Person:
    def show(self):
        print("I am a Person")
class Student(Person):
    def study(self):
        print("I go to school")
d = Student()
# d.shoe()
# d.show()

# Q2. Create a Vehicle class and inherit it into Car.
class Vehicle:
    def show(self):
        print("I have a vehical")
class Car(Vehicle):
    def drive(self):
        print("I drive a car.")
c = Car()
# c.show()
# c.drive()

# Q3. Create an Animal class and inherit it into Dog.

# Q4. Create an Employee class and inherit it into Manager.

# Q5. Create a Book class and inherit it into EBook.

# Q6. Create a Mobile class and inherit it into SmartPhone.

# Q7. Create a Shape class and inherit it into Rectangle.

# Q8. Create a BankAccount class and inherit it into SavingsAccount.

# Q9. Create a Laptop class and inherit it into GamingLaptop.

# Q10. Create a Teacher class and inherit it into Professor.
class Teacher:
    def teach(self):
        print("I do research")
class Professor(Teacher):
    def research(self):
        print("I cover two school")
p = Professor()
# p.teach()
# p.research()


# 2. Constructor Inheritance
# Syntax
class Person:
    def __init__(self, name):
        self.name = name
class Student(Person):
    def __init__(self, name, roll):
        super().__init__(name)
        self.roll = roll
s = Student("Suraj", 101)
# print(s.name)
# print(s.roll)

# Example
class Person:
    def __init__(self, name):
        self.name = name #Jo bhi object banega, us object ke andar name naam ka instance variable create hoga.
class Student(Person):
    def __init__(self, name, roll): #Jab Student ka object banega to ye constructor chalega.
        super().__init__(name) # Yahi Constructor Inheritance hai. | Parent class (Person) ka constructor call karo.
        self.roll = roll
s = Student("Suraj", 101)
# print(s.name)
# print(s.roll)

# Example
# Parent Class
class Vechicle:
    # Parent Constructor
    def __init__(self, brand):
        # Object ke andar brand naam ka instance variable ban raha hai
        self.brand = brand
# Child Class (Vehicle ko inherit kar rahi hai)
class Car(Vechicle):
    # Child Constructor
    def __init__(self, brand, model):
        # Parent constructor ko call kar raha hai
        # Yahan "Toyota" parent constructor me pass hoga
        super().__init__(brand)
        # Child apna khud ka instance variable bana raha hai
        self.model = model
    # Display Method
    def display(self):
        # Parent constructor se bana hua variable print hoga
        print("Brand :", self.brand)
        # Child constructor se bana hua variable print hoga
        print("model :", self.model)
# Car class ka object create ho raha hai | brand = "Toyota" | model = "Fortuner"
# c1 = Car("Toyota", "Fortuner")
# Object ki details print karne ke liye display() method call ho raha hai
# c1.display()

# Parent and Child Constructors Together
class Employee:
    def __init__(self, name):
        print("Parent Constructor")
        self.name = name
class Developer(Employee):
    def __init__(self, name, language):
        print("Child Constructor")
        super().__init__(name)
        self.language = language
d = Developer("Suraj", "Python")

# Q1. Create Person(name) and Student(name, roll) using super().__init__().

# Q2. Create Vehicle(brand) and Car(brand, model).

# Q3. Create Employee(name) and Manager(name, salary).

# Q4. Create Animal(name) and Dog(name, breed).

# Q5. Create Book(title) and EBook(title, size).

# Q6. Create Mobile(company) and SmartPhone(company, ram).

# Q7. Create Laptop(brand) and GamingLaptop(brand, gpu).

# Q8. Create Bank(balance) and Savings(balance, interest_rate).

# Q9. Create Teacher(name) and Professor(name, subject).

# Q10. Create Shape(color) and Rectangle(color, length, width).

# 3. super() Function (10 Questions)

# Q1. Use super() to call the parent constructor.

# Q2. Use super() to call a parent method.

# Q3. Print parent class information using super().

# Q4. Access parent constructor before adding child variables.

# Q5. Create Employee and Developer using super().

# Q6. Create Person and Teacher using super().

# Q7. Create Animal and Cat using super().

# Q8. Create Vehicle and Bike using super().

# Q9. Create Shape and Circle using super().

# Q10. Create Computer and Laptop using super().

# 4. Method Overriding (10 Questions)

# Q1. Create Animal and override sound() in Dog.

# Q2. Create Vehicle and override start() in Car.

# Q3. Create Employee and override work() in Manager.

# Q4. Create Person and override display() in Student.

# Q5. Create Book and override details() in EBook.

# Q6. Create Shape and override area() in Rectangle.

# Q7. Create BankAccount and override withdraw() in SavingsAccount.

# Q8. Create Mobile and override specification() in SmartPhone.

# Q9. Create Teacher and override introduce() in Professor.

# Q10. Create Laptop and override show_info() in GamingLaptop.

# 5. isinstance() and issubclass() (10 Questions)

# Q1. Check whether a Student object is an instance of Student.

# Q2. Check whether a Student object is an instance of Person.

# Q3. Check whether Car is a subclass of Vehicle.

# Q4. Check whether Dog is a subclass of Animal.

# Q5. Check whether Manager is a subclass of Employee.

# Q6. Check whether SmartPhone is a subclass of Mobile.

# Q7. Check whether Rectangle is a subclass of Shape.

# Q8. Check whether GamingLaptop is a subclass of Laptop.

# Q9. Create three-level inheritance (Person → Employee → Manager) and check isinstance() for each level.

# Q10. Create two unrelated classes and verify that issubclass() returns False.