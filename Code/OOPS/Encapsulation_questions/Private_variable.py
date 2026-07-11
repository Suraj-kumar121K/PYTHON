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
e1.set_salary(50000)
print(e1.get_salary())

# Public
class Student:
    def __init__(self, name):
        self.name = name
s1 = Student("Suraj")
print(s1.name)

# Protected Variable
class Student:
    def __init__(self, name):
        self._name = name
s1 = Student("Suraj")
print(s1._name)

# Private Variable
class Student:
    def __init__(self, name):
        self.__name = name
s1 = Student("Suraj")
print(s1.__name)

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

class Student:
    def __init__(self, name):
        self.__name = name
    def get_name(self):
        return self.__name
# s1 = Student("Suraj")
# print(s1.get_name())















# Basic Private Variable
# 1. Create a Student class with a private __name variable and display it using a method.


# 2. Create an Employee class with a private __salary variable.
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