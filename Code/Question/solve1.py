# Exercise 1. Arithmetic Product and Conditional Logic
"""
Practice Problem: Write a Python function that accepts two integer numbers. 
If the product of the two numbers is less than or equal to 1000, return their 
product; otherwise, return their sum.

Exercise Purpose: Learn basic control flow and the use of if-else statements. 
Understand how code decisions change output based on a mathematical threshold.

Given Input:
Case 1: number1 = 20, number2 = 30
Case 2: number1 = 40, number2 = 30

Expected Output:
The result is 600
The result is 70
"""

def multiplication_or_sum(num1, num2):
    product = num1 * num2
    if product <= 1000:
        return product
    else:
        return num1 + num2
result = multiplication_or_sum(20, 30)
print("The result is", result)

result = multiplication_or_sum(40, 30)
print("The result is", result)
    
    
# Exercise 2. Cumulative Sum of a Range
"""
Practice Problem: Iterate through the first 10 numbers (0-9). 
In each iteration, print the current number, the previous number, 
and their sum.

Exercise Purpose: This exercise teaches “State Tracking.” 
In programming, you often need to remember a value from a previous loop 
iteration to calculate results in the current one. This is the basis for 
algorithms like Fibonacci sequences or running totals.

Given Input: Range: numbers = range(10)
"""