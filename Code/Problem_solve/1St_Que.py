# Check if a number is even or odd
def check_even_odd(num):
    if num % 2 == 0:
        print(f"{num} is even")
    else:
        print(f"{num} is odd")
num = int(input("Enter first number: "))          
# check_even_odd(num)

# Multiplication table of a number
def mul_table(num):
    for i in range(1, 11):
        print(f"{num} X {i} = { num * i}")
number = int(input("Enter a number: "))   
mul_table(number)