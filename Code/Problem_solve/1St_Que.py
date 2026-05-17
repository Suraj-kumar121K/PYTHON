# Check if a number is even or odd
# def check_even_odd(num):
#     if num % 2 == 0:
#         print(f"{num} is even")
#     else:
#         print(f"{num} is odd")
# num = int(input("Enter first number: "))          
# # check_even_odd(num)

# Multiplication table of a number
# def mul_table(number):
#     for i in range(1, 11):
#         print(f"{number} X {i} = { number * i}")
# number = int(input("Enter a number: "))        
# mul_table(number)

# Swap two numbers
def swap_number(a, b):
    a, b = b, a
    print(f"Ater swaping: a = {a}, b = {b}")
# a = input("Enter first number: ")
# b = input("Enter second number: ")
# swap_number(a, b)    
    
# Reverse Number
"""num = int(input("Enter a Number: "))
temp = num
reverse = 0

=while num > 0:
    remainder = num % 10
    reverse = (reverse * 10) + remainder
    num = num // 10
print("The Given number is {} and Reverse is {}".format(temp, reverse))"""

#  Write the code to find the Fibonacci series upto the nth term.
"""num = int(input("Enter a Number: "))
n1 = 0
n2 = 1

print("Fibonacci series:")
for i in range(num):
    print(n1, end=" ")
    
    n3 = n1 + n2
    n1 = n2
    n2 = n3"""
    
# 3. Write code of Greatest Common Divisor 
def gcdFunction(num1, num2):
    if num1 > num2:
        small = num2
    else:
        small = num1
    for i in range(1, small+1):
        if (num1 % i == 0) and (num2 % i == 0):
            gcd = i
    print("GCD of two Number: {}".format(gcd))
# num1 = int(input("Enter First Number:"))
# num2 = int(input("Enter Second Number:"))
# gcdFunction(num1, num2)


# 4. Write code of  Perfect number
"""n = int(input(“Enter any number: “))
sump= 0
for i in range(1, n):
    if(n % i == 0):
        sump= sump + i
if (sump == n):
    print(“The number is a Perfect number”)
else:
    print(“The number is not a Perfect number”)"""