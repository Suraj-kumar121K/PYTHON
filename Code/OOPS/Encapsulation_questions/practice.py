"""
1. Student Class
Create a Student class.
Public: name
Protected: _roll_no
Private: __marks

Methods:
get_marks()
set_marks(marks) (0-100)
display()
"""
# Class
class Student:
    # Constructor
    def __init__(self, name, roll_no, marks):
        # Public Variable (Instance Variable)
        self.name = name
        # Protected Variable (Instance Variable)
        self._roll_no = roll_no
        # Private Variable (Instance Variable)
        self.__marks = marks
    # Getter Method
    def get_marks(self):
        # Return Statement
        return self.__marks
    # Setter Method
    def set_marks(self, marks):
        # Validation (if condition)
        if 0 <= marks <= 100:
            # Update Private Variable
            self.__marks = marks
            # Output
            print("Marks updated successfully.")
        else:
            print("Invalid Marks! Marks should be between 0 and 100.")

    # Display Method (Instance Method)
    def display(self):
        # Access Public Variable
        print("Name :", self.name)
        # Access Protected Variable
        print("Roll No :", self._roll_no)
        # Calling Getter Method
        print("Marks :", self.get_marks())
# Object Creation
s1 = Student("Suraj", 101, 85)
# Method Calling
s1.display()
# Setter Method Calling
s1.set_marks(95)
# Method Calling
s1.display()
# Invalid Value (Validation Check)
s1.set_marks(120)




"""
2. Employee Class
Create an Employee class.
Public: employee_name
Protected: _department
Private: __salary

Methods:
get_salary()
set_salary(salary) (salary > 0)
display()
"""



"""
3. BankAccount Class
Create a BankAccount class.
Public: account_holder
Protected: _account_type
Private: __balance

Methods:
deposit(amount)
withdraw(amount)
get_balance()
display()

Validation:
Deposit amount > 0
Withdraw amount <= balance
"""





"""
4. Car Class
Create a Car class.
Public: brand
Protected: _model
Private: __price

Methods:
get_price()
set_price(price)
display()

Validation:
Price > 0
5. Mobile Class
"""




"""
5. Create a Mobile class.
Public: brand
Protected: _model
Private: __price

Methods:
get_price()
set_price(price)
display()

Validation:
Price > 5000
"""



"""
6. Laptop Class
Create a Laptop class.
Public: brand
Protected: _processor
Private: __price

Methods:
get_price()
set_price(price)
display()

Validation:
Price > 10000
"""



"""
7. Hospital Class
Create a Hospital class.
Public: doctor_name
Protected: _specialization
Private: __fees

Methods:
get_fees()
set_fees(fees)
display()

Validation:
Fees > 0
8. Book Class
"""


"""
8. Create a Book class.
Public: title
Protected: _author
Private: __price

Methods:
get_price()
set_price(price)
display()

Validation:
Price > 100
"""



"""
9. Movie Class
Create a Movie class.
Public: movie_name
Protected: _genre
Private: __rating

Methods:
get_rating()
set_rating(rating)
display()

Validation:
Rating between 1 and 10
"""


"""
10. ATM Class

Create an ATM class.
Public: holder_name
Protected: _account_number
Private: __balance

Methods:
deposit(amount)
withdraw(amount)
get_balance()
display()

Validation:
Deposit > 0
Withdraw <= Balance
"""
"""
11. Teacher Class
Create a Teacher class.
Public: name
Protected: _subject
Private: __salary

Methods:
get_salary()
set_salary()
display()

Validation:
Salary > 20000
"""


"""
12. CricketPlayer Class
Create a CricketPlayer class.
Public: player_name
Protected: _team
Private: __runs

Methods:
get_runs()
set_runs()
display()

Validation:
Runs >= 0
"""



"""
13. College Class
Create a College class.
Public: college_name
Protected: _city
Private: __student_count

Methods:
get_student_count()
set_student_count()
display()

Validation:
Student count > 0
"""


"""
14. Product Class
Create a Product class.
Public: product_name
Protected: _category
Private: __price

Methods:
get_price()
set_price()
display()

Validation:
Price > 0
"""


"""
15. Hotel Class
Create a Hotel class.
Public: hotel_name
Protected: _location
Private: __room_price

Methods:
get_room_price()
set_room_price()
display()

Validation:
Room price > 500
"""



"""
16. Flight Class
Create a Flight class.
Public: flight_name
Protected: _destination
Private: __ticket_price

Methods:
get_ticket_price()
set_ticket_price()
display()

Validation:
Ticket price > 1000
"""

"""
17. GymMember Class
Create a GymMember class.
Public: member_name
Protected: _membership_type
Private: __fees

Methods:
get_fees()
set_fees()
display()

Validation:
Fees > 0
"""



"""
18. Patient Class
Create a Patient class.
Public: patient_name
Protected: _disease
Private: __bill

Methods:
get_bill()
set_bill()
display()

Validation:
Bill > 0
"""


"""
19. Library Class
Create a Library class.
Public: book_name
Protected: _author
Private: __fine

Methods:
get_fine()
set_fine()
display()

Validation:
Fine >= 0
"""


"""
20. ShoppingCart Class
Create a ShoppingCart class.
Public: customer_name
Protected: _cart_type
Private: __total_amount

Methods:
deposit(amount) → Add amount to cart total.
withdraw(amount) → Remove amount from cart total.
get_total_amount()
display()

Validation:
Added amount > 0
Removed amount <= total amount
"""

