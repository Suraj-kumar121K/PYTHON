class BankAccount:
    def __init__(self, name, account_no, balance):
        self.name = name
        self._account_no = account_no
        self.__balance = balance
    def get_balance(self):
        return self.__balance
    def set_balance(self, amount):
        if amount >= 0:
            self.__balance = amount
        else:
            print("Invalid Balance")
    def deposit(self, amount):
        if amount > 0:
            self.__balance += amount
            print("Deposit Successful")
        else:
            print("Invalid Amount")
    def withdraw(self, amount):
        if amount <= self.__balance:
            self.__balance -= amount
            print("Withdraw Successful")
        else:
            print("Insufficient Balance")
    def display(self):
        print("Name :", self.name)
        print("Account No :", self._account_no)
        print("Balance :", self.__balance)
a1 = BankAccount("Suraj", 12345678, 10000)
# a1.display()
# a1.deposit(5000)
# a1.withdraw(3000)
# print("Current Balance :", a1.get_balance())
# a1.set_balance(50000)
# print("Updated Balance :", a1.get_balance())

# ==========================================
# Project 1: Student Management System
# ==========================================

# Variables
# Public -> name
# Protected -> _roll_no
# Private -> __marks

# Methods
# __init__()
# get_marks()
# set_marks()
# display()

# Logic
# 1. Create a student object.
# 2. Store name, roll number, and marks.
# 3. Marks cannot be less than 0.
# 4. Marks cannot be greater than 100.
# 5. Use getter to display marks.
# 6. Use setter to update marks.
# 7. Display all student information.


# ==========================================
# Project 2: ATM Machine
# ==========================================

# Variables
# Public -> name
# Protected -> _account_number
# Private -> __balance

# Methods
# deposit()
# withdraw()
# get_balance()
# set_balance()
# display()

# Logic
# 1. Create an account.
# 2. Deposit money.
# 3. Withdraw money.
# 4. Do not allow withdrawal if balance is insufficient.
# 5. Balance cannot become negative.
# 6. Display account details.


# ==========================================
# Project 3: Employee Salary System
# ==========================================

# Variables
# Public -> employee_name
# Protected -> _employee_id
# Private -> __salary

# Methods
# get_salary()
# set_salary()
# increase_salary()
# display()

# Logic
# 1. Store employee information.
# 2. Salary cannot be negative.
# 3. Increase salary by a given amount.
# 4. Display updated salary.


# ==========================================
# Project 4: Mobile Shop
# ==========================================

# Variables
# Public -> company
# Protected -> _model
# Private -> __price

# Methods
# get_price()
# set_price()
# discount()
# display()

# Logic
# 1. Store mobile details.
# 2. Price must be greater than zero.
# 3. Apply discount.
# 4. Display updated price.


# ==========================================
# Project 5: Bank Account
# ==========================================

# Variables
# Public -> customer_name
# Protected -> _account_number
# Private -> __balance

# Methods
# deposit()
# withdraw()
# transfer()
# display()

# Logic
# 1. Deposit money.
# 2. Withdraw money.
# 3. Transfer money to another account.
# 4. Transfer only if balance is sufficient.


# ==========================================
# Project 6: Hospital Patient Record
# ==========================================

# Variables
# Public -> patient_name
# Protected -> _patient_id
# Private -> __medical_record

# Methods
# get_record()
# set_record()
# display()

# Logic
# 1. Store patient details.
# 2. Medical record should remain private.
# 3. Update record only through setter.
# 4. Display only required information.


# ==========================================
# Project 7: Library Management
# ==========================================

# Variables
# Public -> book_name
# Protected -> _book_id
# Private -> __available_copies

# Methods
# borrow_book()
# return_book()
# get_copies()
# display()

# Logic
# 1. Borrow a book.
# 2. Reduce available copies.
# 3. Return a book.
# 4. Increase available copies.
# 5. Do not allow borrowing if no copies are available.


# ==========================================
# Project 8: Online Shopping
# ==========================================

# Variables
# Public -> product_name
# Protected -> _product_id
# Private -> __price

# Methods
# apply_discount()
# get_price()
# set_price()
# display()

# Logic
# 1. Store product information.
# 2. Price cannot be zero or negative.
# 3. Apply discount.
# 4. Display final price.


# ==========================================
# Project 9: Electricity Bill System
# ==========================================

# Variables
# Public -> customer_name
# Protected -> _meter_number
# Private -> __units

# Methods
# calculate_bill()
# get_units()
# set_units()
# display()

# Logic
# 1. Store electricity units.
# 2. Units cannot be negative.
# 3. Calculate bill using rate per unit.
# 4. Display total bill.


# ==========================================
# Project 10: Hotel Booking System
# ==========================================

# Variables
# Public -> customer_name
# Protected -> _room_number
# Private -> __room_charge

# Methods
# book_room()
# checkout()
# get_charge()
# display()

# Logic
# 1. Store booking information.
# 2. Room charge cannot be negative.
# 3. Calculate final bill.
# 4. Display booking details.