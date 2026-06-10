def hello():
    print("Hello World")
# hello()

# 2. Addition Function
def add(a, b):
    print( a + b)
    
# add(10, 20)

# 3. Function with Return
def squ(n):
    return n * n
result = (squ(5))
# print(result)
    
# 4. Even Odd Function
def even_odd(a):
    if a % 2 == 0:
        return "Even"
    elif a % 2 != 0:
        return "Odd"
    else:
        return "zero"
# print(even_odd(0))

# 5. Largest Number Function
def lar(a, b):
    if a > b:
        return a
    else:
        return b
# print("Largest number is:", lar(20, 30))

# 6. Default Argument
def defa(a = "hello"):
    return a
# print(defa())
# print(defa("suraj"))

# 7. Keyword Argument
def student(name, age):
    print(name, age)

# student(age=20, name="Ravi")

# 8. *args Example
def total(*numbers):
    print(numbers)
# total(10, 20, 30, 40)

# 9. **kwargs Example
def info(**data):
    print(data)
# info(name="Suraj", age=20)

# 11. Recursive Function
def fact(n):
    if n == 1:
        return 1
    return n * fact(n - 1)

# print(fact(5))

# 12. Calculator Function
def Calculator(a, b, op):
    a = int(input("Enter a number: "))
    b = int(input("Enter a number: "))
    if op == "add":
        return a + b
    elif op == "neg":
        return a - b
    elif op == "sqr":
        return a * b
    else:
        return "Invalid Operator"
# print(Calculator(10, 20, "add"))

# 1. Write a function to add two numbers.
def add_two(a, b):
    return a + b
# print(add_two(10, 20))

# 2. Write a function to find square of a number.
def square(n):
    return n * n
res = square(5)
# print(res)

# 3. Write a function to check even or odd.
def eve(n):
    if n % 2 == 0:
        return "Even"
    else:
        return "odd"
# print(eve(5))

# 4. Write a function to find largest of two numbers.
def largest_of_two(a, b):
    if a > b:
        return a
    else:
        return b
# print("largest of two num = ",largest_of_two(25, 42))

# 5. Write a function to find largest of three numbers.
def largest_of_three(a, b, c):
    if a > b and a > c:
        return a
    elif b > a and b > c:
        return b
    else:
        return c
# print("largest of three num = ",  largest_of_three(30, 45, 40))


# 6. Write a function to calculate factorial.
def fact(n):
    result = 1
    for i in range(1, n + 1):
        result *= i
    return result
# print(fact(5))

# 7. Write a function to check prime number.
def prime_number(n):
    if n <= 1:
        return "Not Prime"
    for i in range(2, n):
        if n % i == 0:
            return "not prime"
    return "Prime"
# n = int(input("Enter a Number: "))
# print(prime_number(n))

# 8. Write a function to print Fibonacci series.
def Fibonacci_series(n):
    a = 0
    b = 1
    
    for i in range(n):
        print(a)
        c = a + b
        a = b
        b = c
# num = int(input("Enter a Number: "))
# Fibonacci_series(num)

# 9. Write a function to reverse a string.
def reverse_string(text):
    rev = ""
    for i in text:
        rev = i + rev
    return rev
# print(reverse_string("hello"))

# 10. Write a function to check palindrome string.

# 11. Write a function to count vowels in a string.
    
# 12. Write a function to find sum of list elements.
List = [1, 2, 3, 4, 5, 6]

def fun_list(List):
    total = 0
    for i in List:
        total += i
    return total
# print(fun_list(List))

# 13. Write a function to find maximum element in a list.
List_1 = [10, 20, 30, 60, 8]
def max_list(List_1):
    largest = List_1[0]
    for i in List_1:
        if i > largest:
            m = i
    return maxes
print(max_list(List_1))
        
    

# 14. Write a function to find minimum element in a list.

# 15. Write a function to sort a list.

# 16. Write a function using default arguments.

# 17. Write a function using keyword arguments.

# 18. Write a function using *args.

# 19. Write a function using **kwargs.

# 20. Write a recursive function for factorial.

# 21. Write a recursive function for Fibonacci.

# 22. Write a lambda function to find square.

# 23. Write a lambda function to add two numbers.

# 24. Write a function using map().

# 25. Write a function using filter().

# 26. Write a function using reduce().

# 27. Write a nested function example.

# 28. Write a decorator function.

# 29. Write a generator function.

# 30. Write a function returning multiple values.

# 31. Write a function to check Armstrong number.

# 32. Write a function to generate OTP.

# 33. Write a function for login validation.

# 34. Write a function for email validation.

# 35. Write a function to count words in a string.

# 36. Write a function to remove duplicates from a list.

# 37. Write a function to merge two lists.

# 38. Write a function to find common elements in two lists.

# 39. Write a function to check leap year.

# 40. Write a function to calculate simple interest.

# 41. Write a function to calculate compound interest.

# 42. Write a function to print multiplication table.

# 43. Write a function to convert Celsius to Fahrenheit.

# 44. Write a function to find GCD of two numbers.

# 45. Write a function to find LCM of two numbers.

# 46. Write a function to check strong password.

# 47. Write a function to calculate average of list.

# 48. Write a function to count uppercase and lowercase letters.

# 49. Write a function to find second largest number.

# 50. Write a function to flatten nested list.

# 1. Write a decorator function to calculate execution time.

# 2. Write a decorator to check login before function execution.

# 3. Write a recursive function for binary search.

# 4. Write a recursive function to solve Tower of Hanoi.

# 5. Write a recursive function to find sum of digits.

# 6. Write a closure function example.

# 7. Write a function that returns another function.

# 8. Write a lambda function with map() to square list elements.

# 9. Write a lambda function with filter() to get prime numbers.

# 10. Write a lambda function with reduce() to multiply all numbers.

# 11. Write a generator function for Fibonacci series.

# 12. Write a generator for infinite even numbers.

# 13. Write a custom iterator class.

# 14. Write a memoization decorator.

# 15. Write a caching function using dictionary.

# 16. Write a function to validate password using regex.

# 17. Write a function to validate email using regex.

# 18. Write a function to count frequency of words in a file.

# 19. Write a function to read CSV file and return data.

# 20. Write a function to write data into JSON file.

# 21. Write a higher-order function example.

# 22. Write a callback function example.

# 23. Write a function using *args and **kwargs together.

# 24. Write a function to flatten deeply nested lists.

# 25. Write a function to remove duplicates without using set().

# 26. Write a function to rotate a list.

# 27. Write a function to check anagram strings.

# 28. Write a function to compress a string.

# 29. Write a function to decompress a string.

# 30. Write a function to find missing number in list.

# 31. Write a function to merge dictionaries.

# 32. Write a function to sort dictionary by values.

# 33. Write a function to find top 3 largest numbers.

# 34. Write a function to implement stack using functions.

# 35. Write a function to implement queue using functions.

# 36. Write a function to create ATM system.

# 37. Write a function for student management system.

# 38. Write a function for bank management system.

# 39. Write a function to perform CRUD operations.

# 40. Write a function to encrypt and decrypt text.

# 41. Write a function to create OTP system with expiry time.

# 42. Write a function to implement rate limiter.

# 43. Write a function to retry failed API calls.

# 44. Write a function to log function calls into file.

# 45. Write a function to profile memory usage.

# 46. Write a function to compare execution time of two functions.

# 47. Write a function to create custom exception.

# 48. Write a function to validate user input dynamically.

# 49. Write a function to implement pagination logic.

# 50. Write a function to simulate multithreading tasks.