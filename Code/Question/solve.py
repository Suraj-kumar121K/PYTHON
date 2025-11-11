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
# Odd_number()

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
 
--> 15. Convert kilometers to meters. 
def kilometers_to_meters():
    kilometers = float(input("Enter distance in kilometers: "))
    meters = kilometers * 1000
    print(f"{kilometers} kilometers is equal to {meters} meters")
# kilometers_to_meters()

--> 16. Convert meters to centimeters. 
def meters_to_centimeters():
    meters = int(input("Enter distance in centimeter: "))
    centimeters = meters  * 100 
    print(f"{meters} meters is equal to {centimeters} centimeters")
# meters_to_centimeters()    

--> 17. Convert centimeters to meters.
def centimeters_to_meters():
    centimeters = float(input("Enter distance in Meters: "))
    meters = centimeters / 100
    print(f"{centimeters} centimeters is equal to {meters} meters")
# centimeters_to_meters()

--> 18. Calculate discount percentage. 
"""
Discount Percentage


                Original Price - Selling Price
Discount % =  --------------------------------- x 100
                    Original Price
"""
def percentage():
    Original_Price = int(input("Enter a Original Price: "))
    Selling_Price = int(input("Enter a Selling Price: "))
    discount_percent = (Original_Price-Selling_Price) / Original_Price * 100
    print("Discount % = ", discount_percent)
# percentage()

--> 19. Final price after discount.
"""
Final Price = Original Price-(Original Price x Discount %/100)
"""
def discount():
    original_price = float(input("Enter a original price: "))
    discount_percent = float(input("Enter a discount percent: "))
    final_price = original_price - (original_price * discount_percent / 100) 
    print("Final price = ", final_price)
# discount()  
  
--> 20. Profit or loss calculation.
"""
Profit or Loss Calculation
Profit = Selling Price - Cost Price (if SP > CP)
Loss = Cost Price - Selling Price (if SP < CP)
"""
def profit_loss():
    cost_price = int(input("Enter a cost price: "))
    selling_price = int(input("Enter a Selling Price: "))
    if selling_price > cost_price:
        profit = selling_price - cost_price
        print("profit = ", profit)
    elif selling_price < cost_price:
        loss = cost_price - selling_price
        print("Loss = ", loss)
    else:
        print("No profit, no loss") 
# profit_loss()           
    
--> 21. Average of n numbers using loop. 
"""
Average of n Numbers Using Loop
Average = Sum of all numbers / n
"""
def Avg_number(n):
    return 

--> 22. Harmonic mean of two numbers. 
"""
Harmonic Mean = 2(axb) / a+b
"""
def Harmonic_mean():
    a = float(input("Enter a number: "))
    b = float(input("Enter a number: "))
    Harmonic = 2 * (a * b)/ (a + b)
    print("Harmonic mean = ", Harmonic)
# Harmonic_mean()
    
--> 23. Find remainder when a number is divided by 7. 
"""
Remainder = Number %(mod) 7
"""
def remainder():
    n = int(input("Enter a prime digits: "))
    divided = n % 7 == 0
    print(f"number is divided by 7 = {divided} ")
# remainder() 

--> 24. Count how many digits are prime digits. 
"""
Count = Number of digits in {2,3,5,7}
"""
def count():
    n = input("Enter a Number: ")   # string me lo
    prime_digits = 0
    for d in n:
        if d in "2,3,5,7,11,13,23":
            prime_digits += 1 
    print("Number of prime digits = ", prime_digits)
# count() 

--> 25. Multiply number without multiplication operator.

def multiply():
    a = int(input("Enter a number: "))
    b = int(input("Enter a number: ")) 
    sign = 1
    if a < 0:
        sign *= -1
    if b < 0:
        sign *= -1
    a, b = abs(a), abs(b)
    result = 0
    for _ in range(b):
        result += a
    result *= sign  
    print(f"Multiplication of {a} and {b} is: {result}")
# multiply()
    
--> 26. Print multiplication table. 
def multiplication_table():
    n = int(input("Enter a number: "))
    for i in range(1, 11):
        result = n * i
        print(result)
# multiplication_table()

--> 27. Reverse digits & check palindrome. 
def palindrome():
    n = input("Enter a number: ")
    reversed = n[::-1]
    print("Reversed", reversed)
    if n == reversed:
        print("Palindrome: True")
    else:
        print("Palindrome: False")    
# palindrome()

--> 28. Sum of squares of first n natural numbers.
"""
Formula
Sum = n ( n + 1 ) ( 2n + 1) / 6
"""
def natural():
    n = int(input("Enter a natural number: "))  
    squares = n * (n + 1) * (2 * n + 1) // 6
    print("Sum of squares:", squares)
natural()
