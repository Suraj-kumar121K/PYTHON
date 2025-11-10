--> Basic Python Math Questions --
--> 1. Add two numbers. 
def add_two_number():
    a = int(input("Enter a number: "))
    b = int(input("Enter a number: "))
    adds = a + b
    print("print number: ", adds)   
# add_two_number() 

--> 2. Multiply three numbers. 
def Multiply():
    a = int(input("Enter a number: "))
    b = int(input("Enter a number: "))
    c = int(input("Enter a number: "))
    mul = a * c * b
    print("Multiply three numbers: ", mul)
# Multiply()    

--> 3. Find the square of the sum of two numbers. 
def square():
    a = int(input("Enter a Number: "))
    b = int(input("Enter a number: "))
    squ = (a + b)**2
    print("square of the Sum: ", squ)
# square()    
    
--> 4. Check if a number is divisible by 
def divisible():
    num = int(input("Enter a number: "))
    div = int(input("Enter the divisor: "))

    if num % div == 0:
        print(f"{num} is divisible by {div}")
    else:
        print(f"{num} is NOT divisible by {div}")
# divisible()   
 
--> 5 or 3. 5. Find the largest of four numbers. 
def largest_Number():
    a = int(input("Enter fourth number: "))
    b = int(input("Enter fourth number: "))
    c = int(input("Enter fourth number: "))
    d = int(input("Enter fourth number: "))
    largest = max(a, b, c, d)
    print("largest: ", largest)
# largest_Number()

--> 6. Count total digits in a number. 
def count():
    nums = int(input("Eneter a number: "))
    digit = len(str(abs(nums)))
    print("Total digits: ", digit)
# count()    
    
--> 7. Calculate the perimeter of a square. 
def perimeter_square():
    side = float(input("Enter side length: "))
    perimeter = 0
    for i in range(4):
        perimeter += side
    print("Perimeter =", perimeter)
# perimeter_square()

--> 8. Calculate the area of a parallelogram. 
"""
      /|
     / | height (h)
    /  |
   /___|
    base
Formula
Area = base x height    
"""
def area():
    b = float(input("Enter base: "))
    h = float(input("Enter hight: "))
    parallelogram = b * h
    print("Area of parallelogram =", parallelogram)
# area()   
    
--> 9. Find the area of a trapezium. 
"""
    a (top base)
     __________
    /          \
   /            \
  /______________\
  b (bottom base)

    height = h
formula
area = 1/2(a + b) x h
"""
def area():
    a = float(input("Enter top base: "))
    b = float(input("Enter bottom base: "))
    h = float(input("Enter height: "))
    trapezium = 1/2 * (a + b) * h
    print("area of  trapezium =", trapezium)
# area()

--> 10. Convert minutes to hours and minutes. 
def convert_minutes():
    try:
        total_minutes = int(input("Enter total minutes:  "))
        
        if total_minutes < 0:
            print("Minutes cannot be negative: ")  
            return
        hours = total_minutes // 60
        remainder = total_minutes % 60
        print(f"{hours} hours {remainder} minutes")
    except ValueError:
        print("Invalid input! Please enter integer value only.")
# convert_minutes()

--> 11. Find the sum of even numbers from 1 to n. 
def even_number():
    n = int(input("Enter a even number n: "))
    total = 0
    for i in range(2, n+1, 2):
        print(i, end=" ")  
        total += i
    print("\nSum of even numbers:", total) 
# even_number() 
    
--> 12. Find the sum of odd numbers from 1 to n. 
def Odd_number():
    n = int(input("Enter a odd number n: "))
    total = 0
    for i in range(1, n+1, 2):
        print(i, end=" ")  
        total += i
    print("\nSum of even numbers:", total) 
Odd_number()

--> 13. Check if a number is a perfect square. 
def square():
    num = int(input("Enter a Number: "))
    sqrt_num  = int(num ** 0.5)
    if sqrt_num  * sqrt_num  == num:
        print(f"{num} is a perfect square {sqrt_num}")
    else:
        print(f"{num} is not a perfect square")
# square()        

--> 14. Calculates the square of the entered number.
def square():
    num = int(input("Enter a Number: "))
    sqrt_num  = num ** 2
    print(f"The square of {num} is: {sqrt_num}")
# square()  
 
