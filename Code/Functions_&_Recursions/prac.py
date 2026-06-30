# Hello
def Hello():
    print("Hello")
# Hello()

# Add Two Numbers
def add(a, b):
    return a + b
# print(add(10, 20))

# Square of Number
def Square(n):
    return n * n
# print(Square(5))

# Even or Odd
def Even_odd(n):
    if n % 2 == 0:
        return "Even"
    else:
        return "Odd"
# print(Even_odd(8))

# Largest of Two Number
def Largest(a, b):
    if a > b:
        return a
    else:
        return b
# print(Largest(20, 50))

# Name and Age Function
def Name_age(name, age):
    print('Age', age)
    print('Name', name)
# print(Name_age("Suraj", 23))

# lambda Addition
"""add = lambda a, b: a + b
print(add(10, 20))"""

# Lambda with map()
num = [1, 2, 3, 4]
result = list(map(lambda x: x * x, num))
# print(result)

# Lambda with filter()
nums = [1, 2, 3, 4, 5, 6]
result = list(filter(lambda x: x % 2 == 0, nums))
# print(result)

# Sort using Lambda
students = [("Ram", 80), ("Shyam", 60), ("Mohan", 90)]
students.sort(key=lambda x: x[1])
print(students)

# Decorator Function
def decorator(func):
    def wrapper():
        print("Before Function")
        func()
        print("After Function")
    return wrapper
@decorator
def hello():
    print("Hello")
# hello()

# Table Program
def table(n):
    for i in range(1, 11):
        print(f"{n} x {i} = {n*i}")
table(5)