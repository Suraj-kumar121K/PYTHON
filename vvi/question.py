# ============================================================
# 1. Python Basics
# ============================================================
# 1. Write a program to print "Hello, World!".
a = "Hello, World!"
# print(a)

# 2. Take two numbers as input and print their sum.
def add(a, b):
    sum = a + b
    return sum
# a = int(input("Enter first number: "))
# b = int(input("Enter second number: "))
# result = add(a, b)
# print("Sum:", result)

# 3. Take two numbers and perform +, -, *, /, and %.
def addition(num1, num2):
    return num1 + num2

def subtraction(num1, num2):
    return num1 - num2

def multiplication(num1, num2):
    return num1 * num2

def division(num1, num2):
    return num1 / num2

def modulus(num1, num2):
    return num1 % num2
# while True:
#     print("\n1. Addition")
#     print("2. Subtraction")
#     print("3. Multiplication")
#     print("4. Division")
#     print("5. Modulus")
#     print("6. Exit")

#     choice = int(input("Enter your choice: "))
#     if choice == 6:
#         break

#     num1 = float(input("Enter first number: "))
#     num2 = float(input("Enter second number: "))

#     if choice == 1:
#         print("Result:", addition(num1, num2))
#     elif choice == 2:
#         print("Result:", subtraction(num1, num2))
#     elif choice == 3:
#         print("Result:", multiplication(num1, num2))
#     elif choice == 4:
#         if num2 != 0:
#             print("Result:", division(num1, num2))
#         else:
#             print("Cannot divide by zero")
#     elif choice == 5:
#         if num2 != 0:
#             print("Result:", modulus(num1, num2))
#         else:
#             print("Cannot perform modulus by zero")
#     else:
#         print("Invalid choice")

# 4. Swap two variables without using a third variable.
def swap(a, b):
    swap_two = a, b = b, a
    return swap_two
# a = int(input("Enter first number: "))
# b = int(input("Enter second number: "))
# a, b = swap(a, b)
# print("After swapping:")
# print("a =", a)
# print("b =", b)

# 5. Check whether a number is positive, negative, or zero.
def number_positive_negative(num):
    if num > 0:
        return "Positive"
    elif num < 0:
        return "negative"
    else:
        return "zero"
# num = int(input("Enter number: "))
# result = number_positive_negative(num)
# print(result)

# 6. Check whether a number is even or odd.
def Even(num):
    if num % 2 == 0:
        print("Even")
    else:
        print("Odd")
# num = int(input("Enter number: "))
# Even(num)

# 7. Find the largest of two numbers.


# 8. Find the largest of three numbers.


# 9. Check whether a given year is a leap year.


# 10. Convert Celsius to Fahrenheit.


# ============================================================
# 2. If-Else Logic
# ============================================================
# 11. Check whether a person is eligible to vote.

# 12. Check whether a number is divisible by both 3 and 5.

# 13. Create a simple grade calculator.

# 14. Check whether a character is a vowel or consonant.

# 15. Calculate electricity bill based on units.

# 16. Check whether three sides can form a triangle.

# 17. Find the type of triangle: equilateral, isosceles, or scalene.

# 18. Create a simple login validation using username and password.

# 19. Calculate discount based on purchase amount.

# 20. Find the smallest of three numbers.


# ============================================================
# 3. Loops
# ============================================================
# 21. Print numbers from 1 to 100.
def number(num):
    numbers = []
    for i in range(num):
        numbers.append(i)
    return numbers
# num = int(input("Enter a Number: "))
# result = number(num)
# print(result)
    
# 22. Print all even numbers from 1 to 100.
def even_number(num):
    even = []
    for i in range(num):
        if i % 2 == 0:
            even.append(i)
    return even
# num = int(input("Enter a Number: "))
# result = even_number(num)
# print(result)

# 23. Print all odd numbers from 1 to 100.
def odd_num(num):
    odd = []
    for i in range(num):
        if i % 2 != 0:
            odd.append(i)
    return odd
# num1 = int(input("Enter a Number: "))
# result = odd_num(num1)
# print(result)

# 24. Find the sum of numbers from 1 to N.
def sum_num(num):
    total = 0
    for i in range(1, num + 1):
        total += i
    return total
# result = int(input("Enter a Number: "))
# num = sum_num(result)
# print(num)

# 25. Find the factorial of a number.

# 26. Print the multiplication table of a number.
def mul_table(num):
    for i in range(1, 11):
        print(f"{num} X {i} = {num * i}")
result = int(input("Enter a Number: "))
mul_table(result)


# 27. Count the number of digits in a number.

# 28. Reverse a number.

# 29. Find the sum of digits of a number.

# 30. Check whether a number is a palindrome.

# 31. Check whether a number is prime.

# 32. Print all prime numbers between 1 and 100.

# 33. Find the largest digit in a number.

# 34. Find the smallest digit in a number.

# 35. Generate the Fibonacci series.


# ============================================================
# 4. Strings — VVI
# ============================================================
# 36. Reverse a string.

# 37. Check whether a string is a palindrome.

# 38. Count the number of vowels in a string.

# 39. Count vowels and consonants separately.

# 40. Count the number of words in a sentence.

# 41. Count the frequency of each character.

# 42. Find the first non-repeating character.

# 43. Remove spaces from a string.

# 44. Convert a string to uppercase without using .upper().

# 45. Check whether two strings are anagrams.

# 46. Find the longest word in a sentence.

# 47. Find the shortest word in a sentence.

# 48. Remove duplicate characters from a string.

# 49. Count how many times a particular word appears.

# 50. Replace a particular word in a sentence.


# ============================================================
# 5. Lists — Very Important
# ============================================================
# 51. Find the largest element in a list.

# 52. Find the smallest element in a list.

# 53. Find the sum and average of list elements.

# 54. Remove duplicate elements from a list.

# 55. Find the second-largest element.

# 56. Find the second-smallest element.

# 57. Sort a list without using .sort().

# 58. Reverse a list without using .reverse().

# 59. Find common elements between two lists.

# 60. Find elements present in one list but not another.

# 61. Count the frequency of each element.

# 62. Find duplicate elements in a list.

# 63. Find the top 3 largest numbers.

# 64. Find the top 3 smallest numbers.

# 65. Separate even and odd numbers into two lists.


# ============================================================
# 6. Dictionary — VVI for Data Analysis
# ============================================================
# 66. Create a dictionary containing employee names and salaries.

# 67. Find the employee with the highest salary.

# 68. Find the employee with the lowest salary.

# 69. Calculate the average salary.

# 70. Count the frequency of words using a dictionary.

# 71. Find duplicate values in a dictionary.

# 72. Sort a dictionary by values.

# 73. Find the key having the maximum value.

# 74. Merge two dictionaries.

# 75. Create a dictionary from two lists.

# 76. Increase all employee salaries by 10%.

# 77. Find employees whose salary is greater than 50,000.

# 78. Group employees by department.

# 79. Calculate total salary by department.

# 80. Find the highest-paid employee in each department.


# ============================================================
# 7. Functions
# ============================================================
# 81. Create a function to calculate factorial.

# 82. Create a function to check prime numbers.

# 83. Create a function to find the maximum of three numbers.

# 84. Create a function to calculate average.

# 85. Create a function to remove duplicates from a list.

# 86. Create a function to count vowels.

# 87. Create a function to return the second-largest number.

# 88. Create a function to calculate simple interest.

# 89. Create a function to calculate compound interest.

# 90. Create a function to check palindrome.


# ============================================================
# 8. File Handling
# ============================================================
# 91. Read a text file using Python.

# 92. Count the number of lines in a file.

# 93. Count the number of words in a file.

# 94. Count the frequency of each word in a file.

# 95. Find the longest word in a file.

# 96. Read a CSV file using Python.

# 97. Write data into a CSV file.

# 98. Find duplicate rows in a CSV file.

# 99. Calculate the average of a numeric CSV column.

# 100. Find the highest value from a CSV column.


# ============================================================
# 🔥 Data Analyst — Most Important 20
# ============================================================
# 1. Find second-largest number.

# 2. Remove duplicates from a list.

# 3. Find duplicate elements.

# 4. Count frequency of elements.

# 5. Find common elements between two lists.

# 6. Find top 3 numbers.

# 7. Find average of numbers.

# 8. Find prime numbers.

# 9. Generate Fibonacci series.

# 10. Check whether a number/string is a palindrome.

# 11. Count vowels and consonants.

# 12. Find character frequency in a string.

# 13. Find the longest word.

# 14. Find the employee with the highest salary using a dictionary.

# 15. Calculate average salary using a dictionary.

# 16. Filter employees with salary > 50,000.

# 17. Calculate total salary by department.

# 18. Find the highest-paid employee by department.

# 19. Read and analyze a CSV file.

# 20. Find duplicates and missing values from a CSV dataset.

#================= 1. Advanced Functions & Logic ==================================

# 101. Write a function that accepts any number of arguments using *args.

# 102. Write a function that accepts any number of keyword arguments using **kwargs.

# 103. Create a function that returns another function.

# 104. Create a function that accepts another function as an argument.

# 105. Write a recursive function to calculate factorial.

# 106. Write a recursive function to calculate Fibonacci numbers.

# 107. Write a recursive function to calculate the sum of digits.

# 108. Create a lambda function to calculate the square of a number.

# 109. Use lambda with sorted() to sort a list of dictionaries by salary.

# 110. Use map() to calculate the square of every number in a list.

# 111. Use filter() to find even numbers from a list.

# 112. Use reduce() to calculate the product of all numbers.

# 113. Use list comprehension to generate squares from 1 to 20.

# 114. Use dictionary comprehension to create number-square pairs.

# 115. Use set comprehension to find unique vowels from a string.

#2. Exception Handling
# 116. Handle division by zero using try-except.

# 117. Handle invalid user input using try-except.

# 118. Handle multiple types of exceptions.

# 119. Use try-except-else to process valid input.

# 120. Use try-except-finally while working with a file.

# 121. Create a custom exception for invalid salary.

# 122. Create a custom exception for invalid age.

# 123. Create a custom exception for insufficient account balance.

# 124. Write a program that continues running even if one input is invalid.

# 125. Create a function that raises an exception when a number is negative.

#OOPs — Very Important

# 126. Create a class Employee with name, age, and salary attributes.

# 127. Create an object of the Employee class and display its details.

# 128. Create a class Student with a constructor.

# 129. Create a class BankAccount with deposit() and withdraw() methods.

# 130. Create a class Rectangle with methods to calculate area and perimeter.

# 131. Create a class Employee with a method to calculate annual salary.

# 132. Create a class Product with price and quantity and calculate total amount.

# 133. Create a class Car with start(), stop(), and display_info() methods.

# 134. Create a class Customer and store customer information.

# 135. Create a class Sales and calculate total sales.

# 4. Encapsulation
# 136. Create a class Employee with a private salary attribute.

# 137. Create getter and setter methods for salary.

# 138. Prevent negative salary using a setter method.

# 139. Create a BankAccount class with a private balance.

# 140. Allow balance modification only through deposit() and withdraw() methods.

#5. Inheritance
# 141. Create a Person class and inherit it into an Employee class.

# 142. Create a Vehicle class and inherit it into Car and Bike classes.

# 143. Create an Employee class and inherit it into Manager and Developer classes.

# 144. Override a parent class method in a child class.

# 145. Demonstrate single inheritance.

# 146. Demonstrate multilevel inheritance.

# 147. Demonstrate multiple inheritance.

# 148. Use super() to call the parent class constructor.

# 149. Create different employee classes with different salary calculations.

# 150. Create a hierarchy of Company → Department → Employee.

#6. Polymorphism
# 151. Create different classes with the same method name.

# 152. Create Dog and Cat classes with the same speak() method.

# 153. Demonstrate method overriding.

# 154. Create different payment classes with a common pay() method.

# 155. Create different employee classes with a common calculate_salary() method.

# 156. Demonstrate polymorphism using a list of objects.

# 157. Create Shape, Circle, and Rectangle classes with an area() method.

#7. Abstraction
# 158. Create an abstract Shape class with an abstract area() method.

# 159. Create Circle and Rectangle classes based on the Shape class.

# 160. Create an abstract Employee class with calculate_salary().

# 161. Create PermanentEmployee and ContractEmployee classes.

# 162. Create an abstract Payment class with a pay() method.

# 163. Implement CreditCardPayment and UPI_Payment classes.

#8. Magic / Dunder Methods
# 164. Implement __str__() in an Employee class.

# 165. Implement __repr__() for a Product class.

# 166. Implement __len__() for a custom collection class.

# 167. Implement __eq__() to compare two Employee objects.

# 168. Implement __lt__() to compare employees by salary.

# 169. Implement __add__() to add two objects.

# 170. Create a custom class that supports len().

# 171. Create a custom class that supports + operator.

#9. Class & Static Methods
# 172. Create a class method to create an Employee object from a string.

# 173. Create a static method to validate an email address.

# 174. Create a static method to validate salary.

# 175. Demonstrate the difference between instance, class, and static methods.

# 176. Create a class that keeps track of the total number of employees.

#10. Iterators & Generators
# 177. Create a custom iterator that generates numbers from 1 to N.

# 178. Create a generator that generates even numbers.

# 179. Create a generator for Fibonacci numbers.

# 180. Create a generator that reads a large file line by line.

# 181. Create a generator that yields one employee at a time.

# 182. Compare a list and generator for memory usage.

#11. Decorators
# 183. Create a simple decorator that prints a message before a function.

# 184. Create a decorator that measures execution time.

# 185. Create a decorator that checks whether a user is authorized.

# 186. Create a decorator that logs function calls.

# 187. Create a decorator that validates function arguments.

# 188. Create a decorator that counts how many times a function is called.

#12. File & Data Processing
# 189. Read a large CSV file without loading everything into memory.

# 190. Count duplicate records from a CSV file.

# 191. Find missing values from a CSV file.

# 192. Find the highest salary from an employee CSV file.

# 193. Calculate department-wise average salary from a CSV file.

# 194. Find the top 5 employees by salary.

# 195. Find employees whose salary is above the company average.

# 196. Find the department with the highest total salary.

# 197. Find duplicate customer records.

# 198. Create a summary report from a sales CSV file.

#13. Advanced Python — Data Analyst Logic
# 199. Find the top 10 customers by total revenue.

# 200. Find customers who have never placed an order.

# 201. Find the highest-selling product.

# 202. Find the highest-revenue product.

# 203. Calculate monthly revenue.

# 204. Calculate month-over-month revenue growth.

# 205. Calculate a running total of sales.

# 206. Find the second-highest salary in each department.

# 207. Find the top 3 employees in each department.

# 208. Find customers whose total spending is above the average customer spending.

# 209. Find products that have never been sold.

# 210. Find customers who made more than one purchase.

# 211. Find customers whose second purchase happened within 30 days.

# 212. Find inactive customers who have not purchased in the last 90 days.

# 213. Find the highest-selling product in each category.

# 214. Find the category with the highest total revenue.

# 215. Calculate each product's percentage contribution to total revenue.

#14. OOPs + Data Analyst — Advanced
# 216. Create an Employee class and calculate department-wise salary.

# 217. Create a Customer class and calculate customer lifetime spending.

# 218. Create a Product class and calculate product revenue.

# 219. Create an Order class containing customer and product information.

# 220. Create Customer, Product, and Order classes and connect them.

# 221. Create a SalesReport class that calculates total sales and average sales.

# 222. Create an Employee class with salary validation using encapsulation.

# 223. Create different employee types using inheritance.

# 224. Use polymorphism to calculate salary for different employee types.

# 225. Create an abstract Report class and implement SalesReport and CustomerReport.

# 226. Create a class that reads a CSV file and generates summary statistics.

# 227. Create a DataAnalyzer class with methods for:
#     - total sales
#     - average sales
#     - top products
#     - top customers

# 228. Create a reusable class for calculating business KPIs.

# 229. Create a SalesDashboard class that prepares data for visualization.

# 230. Create a complete mini sales analysis system using OOPs.