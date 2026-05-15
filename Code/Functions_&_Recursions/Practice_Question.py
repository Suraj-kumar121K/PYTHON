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
pr
# 3. Write a function to calculate area of rectangle using arguments.
# 4. Write a function to swap two numbers using arguments.
# 5. Write a function to find average of three numbers.
# 6. Write a function that accepts a student name and marks and prints result.
# 7. Write a function to calculate electricity bill using arguments.
# 8. Write a function that accepts list of numbers and prints largest number.
# 9. Write a function that accepts a string and prints its length.
# 10. Write a function to calculate factorial using arguments.