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
# d = Developer("Suraj", "Python")

# Q1. Create Person(name) and Student(name, roll) using super().__init__().
class Person:
    def __init__(self, name):
        self.name = name
class Student(Person):
    def __init__(self, name, roll):
        super().__init__(name)
        self.roll = roll
    
    def display(self):
        print("Name :", self.name)
        print("ROLL :", self.roll)
s = Student("Suraj", 20)
# s.display()

# Q2. Create Vehicle(brand) and Car(brand, model).
class Vehicle:
    def __init__(self, brand):
        self.brand = brand
class Car(Vehicle):
    def __init__(self, brand, model):
        super().__init__(brand)
        self.model = model
    def display(self):
        print("Brand :", self.brand)
        print("Model :", self.model)
c1 = Car("tata", "Nexon")
# c1.display()

# Q3. Create Employee(name) and Manager(name, salary).
class Employee:
    def __init__(self, name):
        self.name = name  
class Manager(Employee):
    def __init__(self, name, salary):
        super().__init__(name)
        self.salary = salary
    def display(self):
        print("Name :", self.name)
        print("Salary :", self.salary)
m1 = Manager("Suraj", 15000)
# m1.display()
            
# Q4. Create Animal(name) and Dog(name, breed).
class Animal:
    def __init__(self, name):
        self.name = name
class Dog(Animal):
    def __init__(self, name, breed):
        super().__init__(name)
        self.breed = breed
    def display(self):
        print("Name :", self.name)
        print("Breed :", self.breed)
d1 = Dog("Rahul", "Labrador")
# d1.display()

# Q5. Create Book(title) and EBook(title, size).
class Book:
    def __init__(self,title):
        self.title = title
class EBook(Book):
    def __init__(self, title, size):
        super().__init__(title)
        self.size = size
    def display(self):
        print("Title :", self.title)
        print("Size :", self.size)
e1 = EBook("Nexon", 28)
# e1.display()

# Q6. Create Mobile(company) and SmartPhone(company, ram).

# Q7. Create Laptop(brand) and GamingLaptop(brand, gpu).

# Q8. Create Bank(balance) and Savings(balance, interest_rate).

# Q9. Create Teacher(name) and Professor(name, subject).

# Q10. Create Shape(color) and Rectangle(color, length, width).

# 3. super() Function
# Q1. Use super() to call the parent constructor.
# Parent Class
class Animal:
    # Parent constructor
    def __init__(self, name):
        self.name = name      # Parent instance variable
# Child Class
class Dog(Animal):
    # Child constructor
    def __init__(self, name, breed):
        # Calls the parent constructor
        super().__init__(name)
        # Child instance variable
        self.breed = breed
    # Child method
    def display(self):
        print("Dog Name :", self.name)
        print("Breed :", self.breed)
# Creating object of Child class
d1 = Dog("Tommy", "Labrador")
# Calling display method
d1.display()

# Q2. Use super() to call a parent method.

# Q3. Print parent class information using super().

# Q4. Access parent constructor before adding child variables.

# Q5. Create Employee and Developer using super().

# Q6. Create Person and Teacher using super().

# Q7. Create Animal and Cat using super().

# Q8. Create Vehicle and Bike using super().

# Q9. Create Shape and Circle using super().

# Q10. Create Computer and Laptop using super().

# 4. Method Overriding
# Q1. Create Animal and override sound() in Dog.
# Parent Class
class Animal:
    def sound(self):
        print("Animal makes a sound")
# Child Class
class Dog(Animal):
    # 👇 Method Overriding ho raha hai.
    # Parent class ka sound() method yahan same name se dobara banaya gaya hai.
    # Isliye Dog ka sound() method Parent wale method ko replace (override) kar deta hai.
    def sound(self):
        print("Dog barks")
# Object of Child Class
d1 = Dog()
# Child class ka overridden method call hoga
d1.sound()
"""
Rule of Method Overriding
Parent aur Child dono me same method name hona chahiye.
Child class Parent ke method ko naye implementation ke saath likhti hai.
Jab Child object se method call karte hain, to Child ka method execute hota 
hai, Parent ka nahi.
Yaad rakhne ka shortcut:
Method Overriding = Child class Parent ke same method ko dobara likhti hai 
(same name, naya behavior).
"""

# Q2. Create Vehicle and override start() in Car.

# Q3. Create Employee and override work() in Manager.

# Q4. Create Person and override display() in Student.

# Q5. Create Book and override details() in EBook.

# Q6. Create Shape and override area() in Rectangle.

# Q7. Create BankAccount and override withdraw() in SavingsAccount.

# Q8. Create Mobile and override specification() in SmartPhone.

# Q9. Create Teacher and override introduce() in Professor.

# Q10. Create Laptop and override show_info() in GamingLaptop.

# 5. isinstance() and issubclass()
# Q1. Check whether a Student object is an instance of Student.
# Parent Class
class Student:
    # Constructor to initialize the student's name
    def __init__(self, name):
        self.name = name
# Creating an object of Student class
s1 = Student("Suraj")
# Displaying the student's name
print("Student Name :", s1.name)
# Checking whether s1 is an instance (object) of Student class
result = isinstance(s1, Student)
# Printing the result
print("Is s1 an instance of Student?", result)
"""
Yaad Rakho:
✅ isinstance() → Object ko check karta hai.
✅ issubclass() → Class ko check karta hai.
"""

# Q2. Check whether a Student object is an instance of Person.

# Q3. Check whether Car is a subclass of Vehicle.

# Q4. Check whether Dog is a subclass of Animal.

# Q5. Check whether Manager is a subclass of Employee.

# Q6. Check whether SmartPhone is a subclass of Mobile.

# Q7. Check whether Rectangle is a subclass of Shape.

# Q8. Check whether GamingLaptop is a subclass of Laptop.

# Q9. Create three-level inheritance (Person → Employee → Manager) and check isinstance() for each level.