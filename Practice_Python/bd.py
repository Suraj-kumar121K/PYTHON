# Factorial
"""n = int(input("Enter n: "))
T = 1
for i in range(1, n + 1):
    T *= i
print(T)"""

#  Print numbers divisible by 3
"""n = int(input("Enter a: "))
for i in range(1, n + 1):
    if i % 3 == 0:
        print(i)"""

# Count even numbers
"""n = int(input("Enter n: "))
count = 0
for i in range(1,n+1):
    if i % 2 == 0:
        count += 1
print(count)"""

#  Count odd numbers
"""n = int(input("Enter a number "))
count = 0
for i in range(1, n + 1):
    if i % 2 != 0:
        count += 1
print(count)"""

#  Sum of even numbers
"""n = int(input("Enter a number "))
Total = 0
for i in range(1, n + 1):
    if i % 2 == 0:
        Total += i
print(Total)"""

# Sum of odd numbers
"""n = int(input("Enter a number "))
Total = 0
for i in range(1, n + 1):
    if i % 2 != 0:
        Total += i
print(Total)"""

# Print squares
"""n = int(input("Enter n: "))
for i in range(1, n + 1):
    print(i * i)"""
    
# Print cubes
# n = int(input("Enter n: "))
# for i in range(1, n + 1):
#     print(i ** 3)
    
# Reverse table
"""for i in range(10, 0, -1):
    print("5 x", i, "=", 5*i)"""

# Find average  
"""n = int(input("Enter N: "))
total = 0
for i in range(1, n+1):
    total += i
    avg = total / n
print(avg)"""

# Multiples of 5
"""n = int(input("Enter n "))
for i in range(1, n+1):
    if i % 5 == 0:
        print(i)"""

# 🟢 EASY LEVEL (1–30)

# 1. Create a function that prints "Hello"
def pri():
    print("Hello")
# pri()

# 2. Create a function that prints your name
def my_name():
    print("Suraj")
# my_name()

# 3. Create a function to add two numbers
def add(a, b):
    return a + b
# x = int(input("x = "))
# y = int(input("y = "))
# print(add(x,y))

# 4. Create a function to subtract two numbers
def sub(a, b):
    return a - b
# x = int(input("x = "))
# y = int(input("y = "))
# print(sub(x,y))

# 5. Create a function to multiply two numbers
def mul(a, b):
    return a * b
# x = int(input("x = "))
# y = int(input("y = "))
# print(mul(x,y))

# 6. Create a function to divide two numbers
def div(a, b):
    return a/b
# x = int(input("x = "))
# y = int(input("y = "))
# print(div(x,y))

# 7. Create a function to return the square of a number
def square(n):
    return n * n
# x = int(input("square = "))
# print(square(x))

# 8. Create a function to return the cube of a number
def cube(n):
    return n**3
# x = int(input("cube = "))
# print(cube(x))

# 9. Create a function to check if a number is even or odd
def check_num(i):
    if i % 2 == 0:
        return "Even"
    else:
        return "Odd"
# x = int(input("Enter a number "))
# print(check_num(x))

# 10. Create a function to check if a number is positive or negative
def check_number(n):
    if n > 0:
        return "Positive"
    else:
        return "Negative"
# x = int(input("Enter a number "))
# print(check_number(x))

# 11. Create a function to find the maximum of two numbers
# Method 1
def max(a, b):
    return a if a > b else b # ternary operator (short if-else)
# x = int(input("x = "))
# y = int(input("y = "))
# print(max(x,y))

# Method 2
def max(a, b):
    if a > b:
        return a
    else:
        return b 
# x = int(input("x = "))
# y = int(input("y = "))
# print(max(x,y))

# 12. Create a function to find the minimum of two numbers
def mix(a, b):
    return a if a < b else b
# x = int(input("x = "))
# y = int(input("y = "))
# print(mix(x,y))

# 13. Create a function to calculate the average of three numbers
def Avg_Cal(a, b, c):
    return (a + b + c) / 3
# x = int(input("x = "))
# y = int(input("y = "))
# z = int(input("z = "))
# print(Avg_Cal(x, y, z))

# 14. Create a function to calculate the area of a circle
def area_circle(r):
    return 3.14 * r * r
# x = int(input("area of circle = "))
# print(area_circle(x))

# 15. Create a function to convert Celsius to Fahrenheit

# 16. Create a function to find the sum of a list
def sum_list(list):
    total = 0
    for i in list:
        total += i
    return total
# num = [10, 12, 13, 15]
# print(sum_list(num))
        
# 17. Create a function to return the length of a string
def str_len(s):
    return len(s)
# name = "suraj"
# print(str_len(name))

# 18. Create a function to convert a string to uppercase
def str_upp(s):
    return s.upper()
# name = input("Enter a name = ")
# print(str_upp(name))

# 19. Create a function to convert a string to lowercase
def str_upp(s):
    return s.lower()
# name = input("Enter a name = ")
# print(str_upp(name))

# 20. Create a function to find the factorial of a number
# factorial formula(n!) = n x (n - 1) x (n - 2) x .... x 1 
def fact_num(n): 
    fact = 1
    for i in range(1, n + 1):
        fact *= i
    return fact
# num = int(input("enter a number:- "))
# print(fact_num(num))

# 21. Create a function to print the multiplication table of a number
def mul_tab(n):
    for i in range(1, 11):
        print(f"{n} x {i} = {n*i}")
# num = int(input("Enter a number = "))
# mul_tab(num)
    
# 22. Create a function to count even numbers in a list
def count_even(list):
    count = 0
    for i in list:
        if i % 2 == 0:
            count += 1
    return count
# num = [1, 2, 3, 4, 5, 6]
# print(count_even(num))

# 23. Create a function to count odd numbers in a list
def count_odd(list):
    count = 0
    for i in list:
        if i % 2 != 0:
            count += 1
    return count
# num = [1, 2, 3, 4, 5, 6, 7, 8, 9]
# print(count_odd(num))

# 24. Create a function to find the maximum value in a list
def max(list):
    maximum = 0
    for i in list:
        if i > maximum:
            maximum = i
    return maximum
# num = [12, 34, 52, 43, 68, 56, 48, 22] 
# print(max(num))  
        
# 25. Create a function to find the minimum value in a list
def find_min(list):
    minimum = list[0]   # first element se start
    for i in list:
        if i < minimum:
            minimum = i
    return minimum
# num = [12, 34, 52, 43, 68, 56, 48, 22]
# print(find_min(num))

# 26. Create a function to check if a string is a palindrome
def is_palindrome(s):
    if s == s[::-1]:
        return True
    else:
        return False
# n = input("Enter a string:- ")
# print(is_palindrome(n))

    
# 27. Create a function to reverse a string
def rev_str(s):
    return s[::-1]
s = "SURAJ"
# print(rev_str(s))

# 28. Create a function to count vowels in a string
def count_vowels(v):
    count = 0
    for i in v:
        if i in "aeiouAEIOU":
            count += 1
    return count
# word = input("Enter s string: ")
# print("Vowels =", count_vowels(word))

# 29. Create a function to count digits in a number
def count_digits(n):
    count = 0
    if n == 0:
        return 1
    while n > 0:
        n = n // 10
        count += 1
    return count

# num = int(input("Enter a number: "))
# print(count_digits(num))
     
# 30. Create a function to check if a number is a multiple of 5
def mul_num(n):
    if n % 5 == 0:
        return True
    else:
        return False
# num = int(input("Enter a number: "))
# print(mul_num(num))

# 31. Create a function to generate Fibonacci series
""" Fn = Fn-1 + Fn-2
current term = previous term + usse previous term"""
def Fib_pre(n):
    a = 0
    b = 1
    for i in range(n):
        print(a, end=" ")
        c = a + b
        a = b
        b = c
# num = int(input("Enter a number: "))
# Fib_pre(num)

# 32. Create a function to check if a number is prime
def prime_num(n):
    if n <= 1:
        return False
    for i in range(2, n):
        if n % i == 0:
            return False
    return True
# num = int(input("Enter a number: "))
# print(prime_num(num))

# 33. Create a function to find all prime numbers in a given range

# 34. Create a function to reverse a list (without slicing)
def rev_list(lst):
    new_list = []
    for i in range(len(lst) -1, -1, -1):
        new_list.append(lst[i])
    return new_list
# num = [10, 20, 30, 40]
# print(rev_list(num))

