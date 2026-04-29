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

# 35. Create a function to remove duplicates from a list
# 36. Create a function to sort a list (without using sort())
# 37. Create a function to merge two lists
# 38. Create a function to find common elements in two lists
# 39. Create a function to find intersection of two lists
# 40. Create a function to find union of two lists
# 41. Create a function to find the second largest element in a list
# 42. Create a function to count frequency of elements using dictionary
# 43. Create a function to count words in a string
# 44. Create a function to find the longest word in a string
# 45. Create a function to remove spaces from a string
# 46. Create a function to convert string to title case
# 47. Create a function to check Armstrong number
# 48. Create a function to find GCD of two numbers
# 49. Create a function to find LCM of two numbers
# 50. Create a function to convert binary to decimal
# 51. Create a function to convert decimal to binary
# 52. Create a function to add two matrices
# 53. Create a function to find transpose of a matrix
# 54. Create a function to multiply two matrices
# 55. Create a recursive function for factorial
# 56. Create a recursive function for Fibonacci
# 57. Create a function to find sum of digits
# 58. Create a function to find product of digits
# 59. Create a function to reverse a number
# 60. Create a function to find Armstrong numbers in a range
# 1. Take an integer input and print whether it is even or odd (use function)
# 2. Take a number and print its multiplication table using a loop inside a function
# 3. Take a list and print the sum of all elements using a function
# 4. Take a string and count vowels using loop + condition + function
# 5. Take a number and check if it is positive, negative, or zero (function)
# 6. Take 3 numbers and print the largest using function
# 7. Take a number and print factorial using loop inside function
# 8. Take a string and reverse it using loop
# 9. Take a list and count even and odd numbers
# 10. Take a number and print all multiples of 5 up to that number
# 11. Take a list and find max and min using function
# 12. Take a string and check palindrome
# 13. Take a number and count digits using loop
# 14. Take a number and print sum of digits
# 15. Take temperature in Celsius and convert to Fahrenheit
# 16. Take a list and print only even numbers
# 17. Take a string and convert to uppercase using function
# 18. Take a list and calculate average
# 19. Take a number and print Fibonacci series
# 20. Take a number and check if it is prime
# 21. Take a list and remove duplicates using loop + function
# 22. Take a string and count frequency of each character
# 23. Take a list and sort it without using sort()
# 24. Take two lists and find common elements
# 25. Take a number and check Armstrong
# 26. Take a list and find second largest element
# 27. Take a string and find longest word
# 28. Take a number and reverse it using loop
# 29. Take a number and check palindrome
# 30. Take a list and count positive and negative numbers
# 31. Take two numbers and find GCD using loop
# 32. Take two numbers and find LCM using function
# 33. Take a number and convert decimal to binary
# 34. Take binary input and convert to decimal
# 35. Take a list and create a new list with squares
# 36. Take a string and remove spaces
# 37. Take a list and merge two lists
# 38. Take a list and find sum of even numbers only
# 39. Take a number and print pattern using loop
# 40. Take a string and count words
# 41. Take a list and reverse it without slicing
# 42. Take a number and print all prime numbers up to n
# 43. Take a list and find frequency using dictionary
# 44. Take a string and check anagram (two strings)
# 45. Take a list and filter numbers divisible by 3 and 5
# 46. Take a number and print multiplication table in reverse
# 47. Take a list and find product of all elements
# 48. Take a number and check perfect number
# 49. Take a list and separate even and odd into two lists
# 50. Take a number and print sum of first n natural numbers using function