# Basic Function Questions
# 1. Write a function to print "Hello Python".
def hello():
    print("Hello Python")
# hello()

# 2. Write a function to print your name and city.
def info():
    print("Suraj")
    print("Delhi")
# info()

# 3. Write a function to add two numbers.
def add(a, b):
    return a + b
# print(add(2, 3))

# 4. Write a function to subtract two numbers.
def sub(a, b):
    return a - b
# print(sub(20, 10))

# 5. Write a function to multiply two numbers.
def mul(a, b):
    return a * b
# print(mul(5, 4))

# 6. Write a function to divide two numbers.
def div(a, b):
    return a / b
# print(div(20, 4))

# 7. Write a function to find the square of a number.
def square(a):
    return a ** 2
# ab = int(input("enter a number "))
# print(square(ab))

# 8. Write a function to find the cube of a number.
def cube(a):
    return a**3
# a = int(input("enter a number "))
# print(cube(a))

# 9. Write a function to check whether a number is even or odd.
def check_num(a):
    if a % 2 == 0:
        print("Even")
    else:
        print("Odd")
# n = int(input("enter a number "))
# check_num(n)
    

# 10. Write a function to find the maximum of two numbers.
def max(a, b):
    if a > b:
        return a
    else:
        return b
# print(max(10, 24))

# Function Arguments Questions
# 1. Write a function that takes name and age as arguments and prints them.
def student(name, age):
    return f"Name: {name}\nAge: {age}"
# print(student("suraj", 23))

# 2. Write a function to calculate simple interest using arguments.
def cal(p, r, t):
    return (p * r * t)/100
# print(cal(1000, 5, 2))

# 3. Write a function to calculate area of rectangle using arguments.
def rectangle_area(length, breadth):
    area = length * breadth
    return f"Area = {area}"
# print(rectangle_area(10, 5))
    
# 4. Write a function to swap two numbers using arguments.
def swap(a, b):
    a, b = b, a
    return a , b
# print(swap(10, 20))

# 5. Write a function to find average of three numbers.
def avg(a, b, c):
    return (a + b + c) / 3
# print(avg(10, 20, 30))

# 6. Write a function that accepts a student name and marks and prints result.
def result(name, marks):
    if marks >= 40:
        return {
            "Student Name = ": name,
            "Result": "Pass"            
        }
    else:
        return {
            "Student Name = ": name,
            "Result": "Fail" 
        }
# print(result("Suraj", 50))

# 7. Write a function to calculate electricity bill using arguments.
def electricity_bill(units, rate):
    Bill = units * rate
    return f"Electricity Bill =  {Bill}"
# print(electricity_bill(5, 10))

# 8. Write a function to calculate factorial using arguments.
def factorial(n):
    fact = 1
    for i in range(1, n+1):
        fact *= i
    return f"factorial = {fact}"
# print(factorial(5))

# Positional & Keyword Arguments
# 1. Write a function using positional arguments for employee details.
def Employee(emp_id, name, salary):
    return emp_id, name, salary
# print(Employee(emp_id=101, name="Suraj", salary=50000))

# 2. Write a function using keyword arguments for student details.
def Student(name, age, marks):
    return f"Name = {name}, Age = {age}, Marks = {marks}"
# print(Student(name="Suraj", age=23, marks=379))

# 3. Write a function to calculate salary using positional arguments.
def Salary(basic, hra, da):
    total = basic + hra + da
    return total
# print("Total Salary:", Salary(20000, 5000, 3000))

# 4. Write a function using keyword arguments where order does not matter.
def info1(name, city, age):
    return name, city, age
# print(info1(name="suraj", age= 21, city="Delhi"))

# 5. Write a program mixing positional and keyword arguments.
def mix(name, age, city):
    return f"{name} is {age} year of old from {city}"
# print(mix("suraj", age=23, city="Delhi"))

# 6. Create a function with three parameters and call it in different orders using keyword arguments.
def details(a, b, c):
    return a + b + c
# print(details(c=30, a=10, b=20))

# 7. Write a function to display product details using keyword arguments.
def product(name, price, brand):
    return {
        "Name": name,
        "Price": price,
        "Brand": brand
    }
# print(product(name="Laptop", price=50000, brand="HP"))

# 8. Write a function using positional arguments to calculate area of triangle.
def triangle_area(base, height):
    area = 0.5 * base * height
    return area
# print(triangle_area(10, 5))

# 9. Write a function that takes city and state as keyword arguments.
def location(city, states):
    return city + "," + states
# print(location(city="Lakhisarai", states="Bihar"))

# 10. Write a function to print full address using positional and keyword arguments.
def address(name, city, state, pincode):
    return f"{name} live in {city},{state},{pincode}"
# print(address(name="Suraj", city="Lakhisarai", state="Bihar", pincode=811106))

# Default Arguments Questions 
# 1. Write a function with default country "India".
def user(name, country="India"):
    return name + " from " + country
# print(user("Suraj"))
# print(user("Suraj", "USA"))

# 2. Write a function with default salary value.

# 3. Write a function with default marks = 40.

# 4. Write a function to greet user with default "Guest" name.

# 5. Write a function to calculate interest with default rate = 5.

# 6. Write a function with multiple default arguments.

# 7. Write a function to print employee details with default department "IT".

# 8. Write a function where default quantity = 1.

# 9. Write a function with default message "Welcome".

# 10. Write a function to calculate bill with default tax percentage.


# **kwargs Questions
# Write a function using **kwargs to print student details.
# Write a function using **kwargs to print employee information.
# Write a function using **kwargs to display product details.
# Write a function using **kwargs to print user profile.
# Write a function using **kwargs to print dictionary items.
# Write a function using **kwargs to count total keyword arguments.
# Write a function using **kwargs to display car details.
# Write a function using **kwargs to print keys only.
# Write a function using **kwargs to print values only.
# Write a function using **kwargs to check if "name" key exists.

# Return Statement Questions
# Write a function that returns sum of two numbers.
# Write a function that returns square of a number.
# Write a function that returns cube of a number.
# Write a function that returns largest of three numbers.
# Write a function that returns factorial of a number.
# Write a function that returns reverse of a string.
# Write a function that returns count of vowels in a string.
# Write a function that returns even numbers from a list.
# Write a function that returns multiple values.
# Write a function that returns whether a number is prime or not.

# Lambda Function Question
# 1. Add Two numbers
add = lambda a, b: a + b
# print(add(10, 20))

# 2. Square of number
Square = lambda x: x*x
# print(Square(5))

# 3. Cube of number
Cube = lambda x: x**3
# print(Cube(3)) 

# 4. Even or Odd
check = lambda x : "Even" if x % 2 == 0 else "Odd"
# print(check(7))

# 5. Max of two numbers
max = lambda a, b: a if a > b else b
# print(max(10, 20))

# 6. map() - double numbers
nums = [1, 2, 3, 4, 5]
# print(list(map(lambda x: x * 2, nums)))

# 7. map() - square numbers
# 8. filter() - even numbers
# 9. filter() - > 10 numbers
# 10. names starting with A
# 11. Sort ascending
# 14. Sort dict by age