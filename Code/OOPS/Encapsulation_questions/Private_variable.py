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
# 4. Create a Mobile class with a private __price variable.
# 5. Create a Laptop class with a private __model variable.
# 6. Create a Book class with a private __title variable.
# 7. Create a Movie class with a private __rating variable.
# 8. Create a Hospital class with a private __doctor_name variable.
# 9. Create a Bank class with a private __account_number variable.
# 10. Create a Teacher class with a private __subject variable.
# 11. Create a College class with a private __college_name variable.
# 12. Create a Bike class with a private __speed variable.
# 13. Create a Company class with a private __ceo variable.
# 14. Create a Hotel class with a private __room_number variable.
# 15. Create a Customer class with a private __email variable.
# 16. Create a School class with a private __principal variable.
# 17. Create a Restaurant class with a private __menu variable.
# 18. Create a Passport class with a private __passport_number variable.
# 19. Create a Train class with a private __coach_number variable.
# 20. Create a Flight class with a private __flight_number variable.

# ==========================================
# Level 2 (Question 21–40) Getter Method
# ==========================================

# 21. Create a Student class with get_name() method.

# 22. Create an Employee class with get_salary() method.

# 23. Create a Car class with get_brand() method.

# 24. Create a Mobile class with get_price() method.

# 25. Create a Laptop class with get_model() method.

# 26. Create a Book class with get_title() method.

# 27. Create a Movie class with get_rating() method.

# 28. Create a Teacher class with get_subject() method.

# 29. Create a Hospital class with get_doctor() method.

# 30. Create a Bank class with get_account() method.

# 31. Create a Company class with get_ceo() method.

# 32. Create a School class with get_principal() method.

# 33. Create a Hotel class with get_room() method.

# 34. Create a Customer class with get_email() method.

# 35. Create a Restaurant class with get_menu() method.

# 36. Create a Passport class with get_passport() method.

# 37. Create a Flight class with get_flight() method.

# 38. Create a College class with get_name() method.

# 39. Create a Bike class with get_speed() method.

# 40. Create a Library class with get_books() method.


# ==========================================
# Level 3 (Question 41–60) Setter Method
# ==========================================

# 41. Create a Student class with set_name() method.

# 42. Create an Employee class with set_salary() method.

# 43. Create a Mobile class with set_price() method.

# 44. Create a Car class with set_brand() method.

# 45. Create a Bike class with set_speed() method.

# 46. Create a Laptop class with set_model() method.

# 47. Create a Hospital class with set_doctor() method.

# 48. Create a Teacher class with set_subject() method.

# 49. Create a Company class with set_ceo() method.

# 50. Create a Hotel class with set_room() method.

# 51. Create a School class with set_principal() method.

# 52. Create a Customer class with set_email() method.

# 53. Create a Restaurant class with set_menu() method.

# 54. Create a Library class with set_books() method.

# 55. Create a Flight class with set_flight() method.

# 56. Create a Movie class with set_rating() method.

# 57. Create a Book class with set_title() method.

# 58. Create a Passport class with set_passport() method.

# 59. Create a Train class with set_coach() method.

# 60. Create a College class with set_name() method.


# ==========================================
# Level 4 (Question 61–80) Validation
# ==========================================

# 61. Create an Employee class where salary must be greater than 0.

# 62. Create a Student class where marks must be between 0 and 100.

# 63. Create a Person class where age must be at least 18.

# 64. Create a Product class where price cannot be negative.

# 65. Create a Bike class where speed cannot exceed 200.

# 66. Create a User class where password must contain at least 8 characters.

# 67. Create an ATM class where PIN must be exactly 4 digits.

# 68. Create a Customer class where mobile number must be exactly 10 digits.

# 69. Create a Customer class where email must contain '@'.

# 70. Create a Bank class where balance cannot be negative.

# 71. Create a Book class where book price must be positive.

# 72. Create a Movie class where rating must be between 1 and 5.

# 73. Create a Hotel class where room number must be positive.

# 74. Create a Student class where roll number must be positive.

# 75. Create an Employee class where Employee ID must start with "EMP".

# 76. Create a Flight class where flight number must start with "AI".

# 77. Create a Passport class where passport number length must be exactly 8 characters.

# 78. Create a Train class where train number must be exactly 5 digits.

# 79. Create a Student class where student name cannot be empty.

# 80. Create a Teacher class where subject name cannot be blank.

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
print("Initial Balance:", b1.get_balance())

# Deposit money
b1.deposit(5000)
print("Balance:", b1.get_balance())

# Withdraw money
b1.withdraw(3000)
print("Balance:", b1.get_balance())

# Withdraw more than balance
b1.withdraw(15000)
print("Final Balance:", b1.get_balance()) 

# 5. Create a Mobile class.
# Public: company
# Protected: _ram
# Private: __price
# Create get_price() and set_price() methods.


# 6. Create a Laptop class.
# Public: brand
# Protected: _processor
# Private: __password
# Create change_password() method.

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

# ==========================================
# Interview Level
# ==========================================
# 26. Create a Bank class using
# Public, Protected and Private variables.
# Implement Deposit, Withdraw and Balance methods.

# 27. Create an ATM class with PIN verification.
# Use Public, Protected and Private variables.

# 28. Create a Library class.
# Public: library_name
# Protected: _librarian
# Private: __books
# Add add_book(), remove_book(), show_books() methods.

# 29. Create a Hospital Management class.
# Public: hospital_name
# Protected: _doctor_name
# Private: __patients
# Add admit(), discharge(), show_patients() methods.

# 30. Create a Student Management System.
# Public: student_name
# Protected: _roll_number
# Private: __marks
# Add get_marks(), set_marks(), result(), display() methods.