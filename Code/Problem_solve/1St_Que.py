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
a = input("Enter first number: ")
b = input("Enter second number: ")
swap_number(a, b)    
    
