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
# Ans
def multiplication_or_sum(num1, num2):
    product = num1 * num2
    if product <= 1000:
        return product
    else:
        return num1 + num2
# result = multiplication_or_sum(20, 30)
# print("The result is", result)

# result = multiplication_or_sum(40, 30)
# print("The result is", result)
    
    
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
# Ans
"""print("Printing current and previous number sum in a range(10)")
previous_num = 0
for i in range(10):
    total = previous_num + i
    print(f"Current Number {i} Previous Number {previous_num} Sum: ", total)
    previous_num = i
print(previous_num)"""

# Exercise 3. String Indexing and Even Slicing
"""
Practice Problem: Display only those characters which are present at an even 
index number in given string.

Exercise Purpose: Understand how data is stored in memory using zero-based 
indexing. In most languages, the first character is at position 0, the second 
at 1, and so on. Mastering indexing is vital for data parsing.

Given Input: String: "pynative"
"""
def remove_chars(word, n):
    print('Original string:', word)
    res = word[n:]
    return res

# print("Removing characters from a string")
# print(remove_chars("pynative", 4))
# print(remove_chars("pynative", 2))