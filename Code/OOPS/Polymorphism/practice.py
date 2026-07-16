# ============================================================
# Advanced Method Overriding (Runtime Polymorphism) - 10
# ============================================================

# Q1. Create an Employee class with calculate_salary().
# Create FullTimeEmployee, PartTimeEmployee, and Intern classes.
# Override calculate_salary() in each child class.

# Q2. Create a Notification class with send().
# Override it in EmailNotification, SMSNotification, and PushNotification.

# Q3. Create a Payment class with process_payment().
# Override it in CreditCardPayment, DebitCardPayment, UPI, and PayPal.

# Q4. Create a Shape class with area().
# Override it in Circle, Rectangle, Triangle, and Square.

# Q5. Create a Transport class with fare().
# Override it in Bus, Train, Flight, and Metro.

# Q6. Create an Account class with withdraw().
# Override it in SavingsAccount and CurrentAccount.

# Q7. Create a Tax class with calculate_tax().
# Override it for SalariedPerson, BusinessOwner, and Freelancer.

# Q8. Create a Food class with prepare().
# Override it in Pizza, Burger, and Pasta.

# Q9. Create a Vehicle class with fuel_type().
# Override it in Car, Bike, Truck, and ElectricCar.

# Q10. Create a Hospital class with treatment().
# Override it in Dentist, Cardiologist, and Neurologist.


# ============================================================
# Advanced Operator Overloading - 10
# ============================================================

# Q1. Overload + to add two ComplexNumber objects.

# Q2. Overload == to compare two Student objects using marks.

# Q3. Overload > to compare two Employee salaries.

# Q4. Overload < to compare two Product prices.

# Q5. Overload >= to compare two Account balances.

# Q6. Overload * to multiply two Matrix objects.

# Q7. Overload / to divide two Fraction objects.

# Q8. Overload % to calculate the remainder of two custom Number objects.

# Q9. Overload ** to calculate power between two custom Number objects.

# Q10. Overload != to compare two Book objects using ISBN.


# ============================================================
# Advanced Duck Typing - 10
# ============================================================

# Q1. Create PDFReader, WordReader, and ExcelReader classes.
# Each class should have read().
# Create one function that reads all file types.

# Q2. Create YouTubePlayer, SpotifyPlayer, and VLCPlayer.
# Each should have play().

# Q3. Create Dog, Cat, Lion, and Tiger classes.
# Each should implement sound().

# Q4. Create EmailService, SMSService, and WhatsAppService.
# Each should implement send().

# Q5. Create Car, Bike, and Boat.
# Each should implement start().

# Q6. Create Printer, Scanner, and Projector.
# Each should implement connect().

# Q7. Create Teacher, Student, and Principal.
# Each should implement introduce().

# Q8. Create CSVExporter, PDFExporter, and ExcelExporter.
# Each should implement export().

# Q9. Create Camera, MobileCamera, and DroneCamera.
# Each should implement capture().

# Q10. Create Paytm, PhonePe, and GooglePay.
# Each should implement pay().


# ============================================================
# Advanced Mixed Polymorphism - 10
# ============================================================

# Q1. Build an Online Payment System using
# Method Overriding + Duck Typing + Operator Overloading.

# Q2. Build a Hospital Management System
# using multiple doctors and compare experience.

# Q3. Build a Vehicle Rental System
# and compare rental prices.

# Q4. Build a School Management System
# with Teacher, Student, and Principal classes.

# Q5. Build an E-Commerce Product Comparison System.

# Q6. Build a Banking System
# and compare account balances.

# Q7. Build a Food Delivery Application
# with different payment methods.

# Q8. Build a Movie Ticket Booking System
# with multiple payment gateways.

# Q9. Build a File Management System
# supporting PDF, Word, Excel, and Image files.

# Q10. Build a Smart Home Automation System
# controlling TV, AC, Fan, and Light using polymorphism.

# ======================================================
# Advanced Polymorphism Coding Questions
# ======================================================

# Q1.
# Create an Employee Management System.
# Parent Class: Employee
# Child Classes: Developer, Tester, Manager
# Override work() in every child class.
# Use Duck Typing to call work().
# Compare salaries using > operator overloading.


# Q2.
# Create a Banking System.
# Parent Class: BankAccount
# Child Classes: SavingAccount, CurrentAccount
# Override interest().
# Overload == to compare account balances.


# Q3.
# Create a Shape Calculator.
# Parent Class: Shape
# Child Classes: Circle, Rectangle, Triangle
# Override area().
# Overload > to compare areas.


# Q4.
# Create a Vehicle Rental System.
# Parent Class: Vehicle
# Child Classes: Car, Bike, Bus
# Override rent_price().
# Overload + to calculate total rent.


# Q5.
# Create an Online Payment System.
# Parent Class: Payment
# Child Classes: UPI, CreditCard, DebitCard
# Override pay().
# Use Duck Typing to process all payments.


# Q6.
# Create a Student Result System.
# Store name, marks, and grade.
# Overload >, <, == operators.
# Display topper using operator overloading.


# Q7.
# Create an Animal Zoo Management System.
# Parent Class: Animal
# Child Classes: Lion, Tiger, Elephant, Monkey
# Override sound().
# Use Duck Typing to call all sounds.


# Q8.
# Create an E-commerce Product System.
# Store product name and price.
# Overload + to calculate bill.
# Overload > to compare product prices.


# Q9.
# Create a Hospital Management System.
# Parent Class: Doctor
# Child Classes: Surgeon, Dentist, Cardiologist
# Override treatment().
# Use Duck Typing to call treatment().


# Q10.
# Create a School Management System.
# Parent Class: Person
# Child Classes: Teacher, Student, Principal
# Override introduce().
# Overload == to compare ages.
# Use Duck Typing to display introductions.


# Method Overriding
# Q1. Create a Person class and override the work() method in Teacher.
class Person:
    def work(self):
        print("person work")

class Teacher(Person):
    def work(self):
        super().work()
        print("Teacher teaches students")    
obj = Teacher()
# obj.work()

# Q2. Create an Animal class and override the sound() method in Dog.
class Animal:
    def sound(self):
        print("Animal makes sound")
class Dog(Animal):
    def sound(self):
        print("Dog barks")
obj = Dog()
# obj.sound()

# Operator Overloading
# Q1. Overload the + operator to add two numbers.
class Number:
    def __init__(self, value):
        self.value = value
        
    def __add__(self, other):
        return self.value + other.value
    
n1 = Number(10)
n2 = Number(20)
# print(n1 + n2)

# Q2. Overload the - operator to subtract two numbers.
class Number:

    def __init__(self, value):
        self.value = value

    def __sub__(self, other):
        return self.value - other.value

n1 = Number(50)
n2 = Number(15)
# print(n1 - n2)

# Duck Typing
# Q1. Create Dog and Cat classes with a sound() method and call them using one function.
class Dog:
    def sound(self):
        print("Dog barks")
class Cat:
    def sound(self):
        print("Cat meows")
        
def make_sound(animal):
    animal.sound()

dog = Dog()
cat = Cat()
# make_sound(dog)
# make_sound(cat)

# Q2. Create Car and Bike classes with a move() method.
class Car:
    # move() method of Car class
    def move(self):
        print("Car is running")   # Car चल रही है

class Bike:
    # move() method of Bike class
    def move(self):
        print("Bike is running")  # Bike चल रही है

# Function that calls the move() method of any object
def start(vehicle):
    # Calls the move() method of the passed object
    vehicle.move()

# Creating a Car object
car = Car()

# Creating a Bike object
bike = Bike()

# Passing Car object to the function
# start(car)

# Passing Bike object to the function
# start(bike)

# Example 
class Demo:
    def add(self, a, b):
        print(a + b)

    def add(self, a, b, c):
        print(a + b + c)

obj = Demo()
# obj.add(10, 20, 30)

# Example 2: Method Overloading using Default Arguments
class Demo:
    def add(self, a, b, c=0):
        print(a + b + c)
obj = Demo()
# obj.add(10, 20)
# obj.add(10, 20, 30)

# Example 3: Method Overloading using *args
class Demo:
    def add(self, *numbers):
        print(sum(numbers))

obj = Demo()
# obj.add(10, 20)
# obj.add(10, 20, 30)
# obj.add(10, 20, 30, 40)