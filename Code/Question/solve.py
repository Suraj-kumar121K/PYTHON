--> Basic Python Math Questions --
--> 1. Add two numbers. 
def add_two_number():
    a = int(input("Enter a number: "))
    b = int(input("Enter a number: "))
    adds = a + b
    print("print number: ", adds)   
# add_two_number() 

--> Multiply three numbers. 
def Multiply():
    a = int(input("Enter a number: "))
    b = int(input("Enter a number: "))
    c = int(input("Enter a number: "))
    mul = a * c * b
    print("Multiply three numbers: ", mul)
# Multiply()    

--> Find the square of the sum of two numbers. 
def square():
    a = int(input("Enter a Number: "))
    b = int(input("Enter a number: "))
    squ = (a + b)**2
    print("square of the Sum: ", squ)
# square()    
    
--> Check if a number is divisible by 
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

--> Count total digits in a number. 
def count():
    nums = int(input("Eneter a number: "))
    digit = len(str(abs(nums)))
    print("Total digits: ", digit)
# count()    
    
--> Calculate the perimeter of a square. 
def perimeter_square():
    side = float(input("Enter side length: "))
    perimeter = 0
    for i in range(4):
        perimeter += side
    print("Perimeter =", perimeter)
# perimeter_square()
