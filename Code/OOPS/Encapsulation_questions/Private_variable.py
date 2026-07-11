# 3. Private Variable
# Private Variable
class Student:
    def __init__(self, name):
        self.__name = name
    def display(self):
        print("Name :", self.__name)
# s1 = Student("Suraj")
# s1.display()

# Validation Example
class Employee:
    def __init__(self):
        self.__salary = 0
    def set_salary(self, salary):
        if salary > 0:
            self.__salary = salary
        else:
            print("Invalid Salary")
    def get_salary(self):
        return self.__salary
e1 = Employee()
# e1.set_salary(50000)
# print(e1.get_salary())

# Public
class Student:
    def __init__(self, name):
        self.name = name
s1 = Student("Suraj")
# print(s1.name)

# Protected Variable
class Student:
    def __init__(self, name):
        self._name = name
s1 = Student("Suraj")
# print(s1._name)

# Private Variable
class Student:
    def __init__(self, name):
        self.__name = name
s1 = Student("Suraj")
# print(s1.__name)

# AttributeError # errordega kiuki private hai esko acess karne ke liye use class ke and se access kar sakte hai baharse nahi kar sakte hai

# Setter Method
class Mobile:
    def __init__(self):
        self.__price = 0
    def set_price(self, price):
        if price > 0:
            self.__price = price
    def get_price(self):
        return self.__price
m1 = Mobile()
# m1.set_price(30000)
# print(m1.get_price())

# Getter
class Student:
    def __init__(self, name):
        self.__name = name
    def set_name(self, new_name):
        self.__name = new_name
    def get_name(self):
        return self.__name
s1 = Student("Suraj")
# s1.set_name("Rahul")
# print(s1.get_name())

# Real Example (Bank)
class Bank:
    def __init__(self, balance):
        self.__balance = balance
    def deposit(self, amount):
        self.__balance += amount
    def withdraw(self, amount):
        self.__balance -= amount
    def show_balance(self):
        print("Balance :", self.__balance)
b1 = Bank(10000)
# b1.deposit(5000)
# b1.withdraw(2000)
# b1.show_balance()

# Validation Example
class Employee:
    def __init__(self):
        self.__salary = 0
    def set_salary(self, salary):
        if salary > 0:
            self.__salary = salary
        else:
            print("Invalid Salary")
    def get_salary(self):
        return self.__salary
e1 = Employee()
# e1.set_salary(50000)
# print(e1.get_salary())

# Basic Private Variable
# 1. Create a Student class with a private __name variable and display it using a method.
class Student:
    def __init__(self, name):
        self.__name = name   # Private Variable
    def display(self):
        return self.__name
s1 = Student("Suraj")
# print(s1.display())

# 2. Create an Employee class with a private __salary variable.
class Employee:
    def __init__(self, salary):
        self.__salary = salary
    def display(self):
        return self.__salary
e1 = Employee(5000)
# print(e1.display())

# 3. Create a Car class with a private __brand variable.
class Car:
    def __init__(self, brand):
        self.__brand = brand
    def display(self):
        print("Brand :", self.__brand)
c1 = Car("BMW")
# c1.display()
        
        
# 4. Create a Mobile class with a private __price variable.
class Mobile:
    def __init__(self, price):
        self.__price = price
    def display(self):
        print("Amount :", self.__price)
c1 = Mobile(150000)
# c1.display()

# ==========================================
# Level 2 (Question 1–10) Getter Method
# ==========================================
# 1. Create a Student class with get_name() method.
class Student:
    def __init__(self, name):
        self.__name = name      # Private Variable
    def get_name(self):         # Getter Method
        return self.__name
# Object
s1 = Student("Suraj")
# Calling Getter Method
# print(s1.get_name())

# 2. Create an Employee class with get_salary() method.
class Employee:
    def __init__(self, salary):
        self.__salary = salary
    def get_salary(self):
        return self.__salary
e1 = Employee(2500000)
# print(e1.get_salary())        

# 3. Create a Car class with get_brand() method.
class Car:
    def __init__(self, brand):
        self.__brand = brand
    def get_brand(self):
        print("Brand :", self.__brand)
s1 = Car("BMW")  
# s1.get_brand()          

# 4. Create a Mobile class with get_price() method.
class Mobile:
    def __init__(self, price):
        self.__price = price
    def get_price(self):
        print("Price :", self.__price)
c1 = Mobile(52000)  
# c1.get_price()

# 5. Create a Laptop class with get_model() method.
class Laptop:
    def __init__(self, model):
        self.__model = model
    def get_model(self):
        print("Model :", self.__model)
c1 = Laptop(52000)  
# c1.get_model()

# 6. Create a Book class with get_title() method.
class Book:
    def __init__(self, title):
        self.__title = title
    def get_title(self):
        print("title :", self.__title)
c1 = Book("Python Programming")  
# c1.get_title()

# 7. Create a Movie class with get_rating() method.
class Movie:
    def __init__(self, rating):
        self.__rating = rating
    def get_rating(self):
        print("Rating :", self.__rating)
c1 = Movie(4.5)  
# c1.get_rating()

# 8. Create a Teacher class with get_subject() method.
class Teacher:
    def __init__(self, subject):
        self.__subject = subject
    def get_subject(self):
        print("Subject :", self.__subject)
t1 = Teacher("Hindi") 
# t1.get_subject()

# 9. Create a Hospital class with get_doctor() method.
class Hospital:
    def __init__(self, doctor):
        self.__doctor = doctor
    def get_doctor(self):
        print("Doctor :", self.__doctor)
h1 = Hospital("Suraj")
# h1.get_doctor()


# 10. Create a Bank class with get_account() method.
class Bank:
    def __init__(self, account):
        self.__account = account
    def get_account(self):
        print("account :", self.__account)
h1 = Bank("Suraj")
# h1.get_account()

# ==========================================
# Level 3 (Question 1–10) Setter Method
# ==========================================
# 6. Create a Book class with get_title() method.
class Book:
    def __init__(self, title):
        self.__title = title
    # Getter Method
    def get_title(self):
        return self.__title
    # Setter Method
    def set_title(self, new_title):
        self.__title = new_title
# Object
b1 = Book("Python Programming")
# print("Before:", b1.get_title())
b1.set_title("Data Analysis with Python")
# print("After :", b1.get_title())

# 2. Create an Employee class with set_salary() method.


# 3. Create a Mobile class with set_price() method.

# 4. Create a Car class with set_brand() method.

# 5. Create a Bike class with set_speed() method.

# 6. Create a Laptop class with set_model() method.

# 7. Create a Hospital class with set_doctor() method.

# 8. Create a Teacher class with set_subject() method.

# 9. Create a Company class with set_ceo() method.

# 10. Create a Hotel class with set_room() method.


# ==========================================
# Level 4 (Question 1–10) Validation
# ==========================================
# 1. Create an Employee class where salary must be greater than 0.

# 2. Create a Student class where marks must be between 0 and 100.

# 3. Create a Person class where age must be at least 18.

# 4. Create a Product class where price cannot be negative.

# 5. Create a Bike class where speed cannot exceed 200.

# 6. Create a User class where password must contain at least 8 characters.

# 7. Create an ATM class where PIN must be exactly 4 digits.

# 8. Create a Customer class where mobile number must be exactly 10 digits.

# 9. Create a Customer class where email must contain '@'.

# 10. Create a Bank class where balance cannot be negative.


# ==========================================
# Public + Protected + Private Mix Questions
# ==========================================
# 1. Create a Student class.
# Public: name
# Protected: _roll_no
# Private: __marks
# Create a display() method.
class Student:
    def __init__(self, name, roll_no, marks):
        self.name = name          # Public
        self._roll_no = roll_no   # Protected
        self.__marks = marks      # Private

    def display(self):
        print("Name :", self.name)
        print("Roll No :", self._roll_no)
        print("Marks :", self.__marks)
# Object
s1 = Student("Suraj", 101, 89)
# Access Public Variable
# print(s1.name)
# Access Protected Variable
# print(s1._roll_no)
# Access Private Variable (Not Allowed)
# print(s1.__marks)
# Access Private Variable using Method
# s1.display()

# 2. Create an Employee class.
# Public: employee_name
# Protected: _department
# Private: __salary
# Create get_salary() method.
class Employee:
    def __init__(self, employee_name, department, salary):
        self.employee_name = employee_name
        self._department = department
        self.__salary = salary             
    def get_salary(self):
        return self.__salary   
    def display(self):
       print("Employee :", self.employee_name) 
       print("Departmant :", self._department) 
       print("Employee :", self.get_salary()) 
# e1 = Employee("Suraj", "IT", 15000)
# e1.display()
        
# 3. Create a Car class.
# Public: brand
# Protected: _model
# Private: __price
# Create display() method.
class Car:
    def __init__(self, brand, model, price):
        self.brand = brand
        self._model = model
        self.__price = price
    def get_price(self):
        return self.__price
    def display(self):
        print("Brand :-", self.brand)
        print("Model :-", self._model)
        print("Price :-", self.get_price())
# c1 = Car("BMW", "X5", 250000)
# c1.display()

# 4. Create a BankAccount class.
# Public: account_holder
# Protected: _account_type
# Private: __balance
# Create deposit(), withdraw(), and get_balance() methods.
class Bankaccount:
    def __init__(self, account_holder, account_type, balance):
        self.account_holder = account_holder
        self._account_type = account_type
        self.__balance = balance   
    def deposit(self, amount):
        self.__balance += amount
        print(f"₹{amount} deposited successfully.")
    def withdraw(self, amount):
        if amount <= self.__balance:
            self.__balance -= amount
            print(f"₹{amount} withdrawn successfully.")
        else:
            print("Insufficient Balance!")           
    def get_balance(self):
        return self.__balance
# Object
b1 = Bankaccount("Suraj", "Savings", 10000)
# Display initial balance
# print("Initial Balance:", b1.get_balance())
# Deposit money
# b1.deposit(5000)
# print("Balance:", b1.get_balance())
# Withdraw money
# b1.withdraw(3000)
# print("Balance:", b1.get_balance())
# Withdraw more than balance
# b1.withdraw(15000)
# print("Final Balance:", b1.get_balance()) 

# 5. Create a Mobile class.
# Public: company
# Protected: _ram
# Private: __price
# Create get_price() and set_price() methods.
class Mobile:
    def __init__(self, company, ram, price):
        self.company = company
        self._ram = ram
        self.__price = price      
    def get_price(self):
        return self.__price
    def set_price(self, new_price):
        self.__price = new_price
    def display(self):
        print("Mobile Name:", self.company)
        print("Mobile ram:", self._ram)
        print("new Price :", self.get_price())       
m1 = Mobile("VIVO", "8GB",15000)
# m1.display()
# m1.set_price(20000)
# print("New Price :", m1.get_price())    

# 6. Create a Laptop class.
# Public: brand
# Protected: _processor
# Private: __password
# Create change_password() method.
class Laptop:
    def __init__(self, brand, processor, password):
        self.brand = brand
        self._processor = processor
        self.__password = password
    def change_password(self, new_password):
        self.__password = new_password
        print("Password changed successfully.")
    def display(self):
        print("Brand :", self.brand)
        print("Processor :", self._processor)
        print("Password :", self.__password)
l1 = Laptop("HP", "Intel i5", "abc123")
# print("Before Changing Password:")
# l1.display()
# l1.change_password("Sur7aj6@")
# print()
# print("After Changing Password:")
# l1.display()

# 7. Create a Teacher class.
# Public: name
# Protected: _subject
# Private: __salary
# Create get_salary() method.


# 8. Create a Hospital class.
# Public: hospital_name
# Protected: _doctor
# Private: __patient_count
# Create admit_patient() method.


# 9. Create a Movie class.
# Public: movie_name
# Protected: _director
# Private: __rating
# Create set_rating() method.


# 10. Create a Company class.
# Public: company_name
# Protected: _location
# Private: __ceo_salary
# Create get_ceo_salary() method.


# 11. Create a College class.
# Public: college_name
# Protected: _course
# Private: __fees
# Create get_fees() method.


# 12. Create a School class.
# Public: school_name
# Protected: _principal
# Private: __student_count
# Create display() method.


# 13. Create a Passport class.
# Public: holder_name
# Protected: _country
# Private: __passport_number
# Create get_passport() method.


# 14. Create a Flight class.
# Public: flight_name
# Protected: _destination
# Private: __ticket_price
# Create set_ticket_price() method.

# 15. Create a Bike class.
# Public: brand
# Protected: _engine
# Private: __speed
# Create increase_speed() method.

# ==========================================
# Validation + Access Modifier
# ==========================================
# 16. Employee salary must be greater than 0.

# 17. Student marks must be between 0 and 100.

# 18. Product price cannot be negative.

# 19. Bank balance cannot be negative.

# 20. Password must contain at least 8 characters.

# 21. ATM PIN must be exactly 4 digits.

# 22. Mobile number must contain exactly 10 digits.

# 23. Email must contain '@'.

# 24. Flight number must start with "AI".

# 25. Employee ID must start with "EMP".