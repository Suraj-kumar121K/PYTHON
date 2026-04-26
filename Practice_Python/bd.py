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
    return b if a < b else a
x = int(input("x = "))
y = int(input("y = "))
print(mix(x,y))

# 13. Create a function to calculate the average of three numbers
# 14. Create a function to calculate the area of a circle
# 15. Create a function to convert Celsius to Fahrenheit
# 16. Create a function to find the sum of a list
# 17. Create a function to return the length of a string
# 18. Create a function to convert a string to uppercase
# 19. Create a function to convert a string to lowercase
# 20. Create a function to find the factorial of a number
# 21. Create a function to print the multiplication table of a number
# 22. Create a function to count even numbers in a list
# 23. Create a function to count odd numbers in a list
# 24. Create a function to find the maximum value in a list
# 25. Create a function to find the minimum value in a list
# 26. Create a function to check if a string is a palindrome
# 27. Create a function to reverse a string
# 28. Create a function to count vowels in a string
# 29. Create a function to count digits in a number
# 30. Create a function to check if a number is a multiple of 5
# 31. Create a function to generate Fibonacci series
# 32. Create a function to check if a number is prime
# 33. Create a function to find all prime numbers in a given range
# 34. Create a function to reverse a list (without slicing)
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