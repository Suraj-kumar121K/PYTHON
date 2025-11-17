--> Basic Python Math Questions 
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
Sum = n(n + 1)(2n + 1) / 6
"""
def natural():
    n = int(input("Enter a natural number: "))  
    squares = n * (n + 1) * (2 * n + 1) // 6
    print("Sum of squares:", squares)
# natural()

--> 29. Count even digits in number. 
def Count_even_digits():
    n = input("Enter a number: ")
    Even = 0
    for digit in n:
        if int(digit) % 2 == 0:
            Even += 1
    print("Number of even digits: ",Even)
# Count_even_digits()    

--> 30. Count odd digits in number. 
def Count_odd_digits():
    n = input("Enter a number: ")
    Even = 0
    for digit in n:
        if int(digit) % 2 != 0:
            Even += 1
    print("Number of odd digits: ",Even)
# Count_odd_digits() 

--> 31. Find first digit of number. 
def first_digit():
    n = input("Enter a number: ")
    digit = int(n[0])
    print("first digit = ", digit)
# first_digit()

--> 32. Find last digit of number. 
def last_digit():
    n = input("Enter a number: ")
    digit = int(n[-1])
    print("last digit = ", digit)
# last_digit()

--> Intermediate Python Math Questions 
--> 33. Sum of cubes of first n natural numbers.
"""
Formula for sum of cubes
1 * 3 + 2 * 3 + 3 * 3 +⋯+ n3 = (2n(n+1)/2) ** 2
"""
def cubes():
    n = int(input("Enter a number: "))
    sum_Cubes = 0
    for i in range(1, n+1):
        sum_Cubes += i ** 3
    print("sum of cubes: ", sum_Cubes)
# cubes()         
 
--> 34. Write a Python program to display the cubes of the first n natural numbers.
def first_cubes():
    n = int(input("Enter a natural number: "))
    cubes = pow(n, 3)
    print("cubes = ", cubes)

 
--> 35. Given 2 strings, return their concatenation, except omit the first char of each. The strings will be at least length 1.
'''
non_start('Hello', 'There') → 'ellohere'
non_start('java', 'code') → 'avaode'
non_start('shotl', 'java') → 'hotlava'''

def non_start(a, b):
    return a[1:] + b[1:]
# print(non_start('Hello', 'There'))
# print(non_start('java', 'code'))
# print(non_start('shotl', 'java'))

--> 36. Given two strings, a and b, return the result of putting them together in the order abba, e.g. "Hi" and "Bye" returns "HiByeByeHi".
make_abba('Hi', 'Bye') → 'HiByeByeHi'
make_abba('Yo', 'Alice') → 'YoAliceAliceYo'
make_abba('What', 'Up') → 'WhatUpUpWhat '''

def make_abba(a, b):
    return a + b + b + a
# print(make_abba('Hi', 'Bye'))
# print(make_abba('Yo', 'Alice'))
# print(make_abba('What', 'Up'))

--> 37. Given a string, return a new string made of 3 copies of the last 2 chars of the original string. The string length will be at least 2.
"""
extra_end('Hello') → 'lololo'
extra_end('ab') → 'ababab'
extra_end('Hi') → 'HiHiHi'
"""
def extra_end(str):
    return str[-2:] * 3
# print(extra_end('Hello'))
# print(extra_end('ab'))
# print(extra_end('Hi'))

--> 38. Given a string, return a version without the first and last char, so "Hello" yields "ell". The string length will be at least 2.
"""
without_end('Hello') → 'ell'
without_end('java') → 'av'
without_end('coding') → 'odin
"""
def without_end(str): 
    return str[1:-1]
# print(without_end('Hello'))
# print(without_end('java'))
# print(without_end('coding'))

--> 39. Given a string, return a "rotated left 2" version where the first 2 chars are moved to the end. The string length will be at least 2.
"""
left2('Hello') → 'lloHe'
left2('java') → 'vaja'
left2('Hi') → 'Hi'
'''
def left2(str):
    return str[2:] + str[:2]
# print(left2('Hello'))
# print(left2('java'))
# print(left2('Hi'))


--> 40. The web is built with HTML strings like "<i>Yay</i>" which draws Yay as italic text. In this example, the "i" tag makes <i> and </i> which surround the word "Yay". Given tag and word strings, create the HTML string with tags around the word, e.g. "<i>Yay</i>".
"""
make_tags('i', 'Yay') → '<i>Yay</i>'
make_tags('i', 'Hello') → '<i>Hello</i>'
make_tags('cite', 'Yay') → '<cite>Yay</cite>'
'''
def make_tags(tag, word):
    return "<"+ tag + ">" + word + "</" + tag + ">" 
# print(make_tags('i', 'Yay'))
# print(make_tags('i', 'Hello'))
# print(make_tags('cite', 'Yay'))


--> 41. Given a string, return the string made of its 
first two chars, so the String "Hello" yields "He". 
If the string is shorter than length 2, 
return whatever there is, so "X" yields "X", 
and the empty string "" yields the empty string "".
"""
first_two('Hello') → 'He'
first_two('abcdefg') → 'ab'
first_two('ab') → 'ab' '''
def first_two(str):
  return str[0:2]
# print(first_two('Hello'))
# print(first_two('abcdefg'))
# print(first_two('ab'))

--> 42. Given 2 strings, a and b, return a string of the 
form short+long+short, with the shorter string on 
the outside and the longer string on the inside. 
The strings will not be the same length, but they 
may be empty (length 0).
"""
combo_string('Hello', 'hi') → 'hiHellohi'
combo_string('hi', 'Hello') → 'hiHellohi'
combo_string('aaa', 'b') → 'baaab'
"""
def combo_string(a, b):
    if len(a) < len(b):
        short = a
        long = b
    else:
        short = b
        long = a    
    return short + long + short
# print(combo_string('Hello', 'hi'))
# print(combo_string('Hello', 'hi'))
# print(combo_string('aaa', 'b'))s


--> 43. Given 2 strings, return their concatenation, 
except omit the first char of each. The strings 
will be at least length 1.
"""
non_start('Hello', 'There') → 'ellohere'
non_start('java', 'code') → 'avaode'
non_start('shotl', 'java') → 'hotlava'
"""
def non_start(a, b):
    return a[1:] + b[1:]
# print(non_start('Hello', 'There'))
# print(non_start('java', 'code'))
# print(non_start('shotl', 'java'))

--> 44. What is 257 + 684?
def Add(a, b):
    return a + b
# print(Add(257, 684))

--> 45. Subtract 938 from 1542.
def subtract(a, b):
    return a - b
# print(subtract(1542, 938))    

--> 46. Multiply 123 x 45.
def multiply(a, b):
    return a * b
# print(multiply(123, 45))

# 48. Divide 144 ÷ 12.
def divide(a, b):
    return a / b
# print(divide(144, 12))
    

# 49. Find the remainder when 987 is divided by 13.
def remainder1(a, b):
    return a % b
# print(remainder1(987, 13))

# 50. Solve 45% of 360.
def precentage(a, b):
    return (a * b) / 100
print(precentage(45, 360))

# 51. Find the square of 27.
def square(a):
    return a * a
# print(square(27))

# 52. Find the cube of 12.
def cube(a):
    return a ** 3
# print(cube(12))

# 53. If a number x + 35 = 100, find x
# 10. Calculate 7! (factorial of 7).
def factorial(n):
    result = 1
    for i in range(1, n + 1):
        result *= i
    return result
# print(factorial(7))        

# 54. Convert 0.75 to a fraction.
def fraction(x):
    s = str(x)
    decimals = len(s.split('.')[1])
    numerator = int(x*(10 ** decimals))
    denominator = 10 ** decimals
    
    def gcd(a, b):
        while b:
            a, b = b, a % b
            return a
    g = gcd(numerator, denominator)
    return numerator // g, denominator // g  
# num , den = fraction(0.75)  
# print(f"{num}/{den}")

# 55. Find the LCM of 12 and 18.
def LCM(a, b):
    # hight number
    num = max(a, b)
    # infinite loop
    while True:
        # Check Condition
        if num % a == 0 and num % b == 0:
            return num
        num += 1 # num = num + 1
# print(LCM(12, 18))

# 56. Find the HCF of 56 and 98.
def HCf(a, b):
    # lowerst number
    num = min(a, b)
    hcf_value = 1
    # condition check 1 to 98
    for i in range(1, num + 1):
        # condition check true ya false
        if a % i == 0 and b % i == 0:
            hcf_value = i
    return hcf_value        
# print(HCf(56, 98))        

# Section 5: Python Programming Logic (25 Questions)
# 57. Write Python code to print numbers 1 to 10.
def print_number():
    for i in range(1, 11):
        print(i)
# print_number()

# 58. Python program to check if a number is even or odd.
def even_odd_check(n):
    if n % 2 == 0:
        return f"{n} is Even"
    else:
        return f"{n} is Odd"
# print(even_odd_check(12))        
# print(even_odd_check(13))        
            
# 59. Program to calculate factorial of a number.
def factorial(n):
    # factorial me multiply hota hai
    fact = 1
    # 1 se n tak
    for i in range(1, n + 1):
        fact *= i
    return fact
# print(factorial(3))

# 60. Program to find sum of elements in a list.
def sum_of_elements(numbers):
    num = 0
    for n in numbers: # range number jenret karta hai list nahi 
        num += n
    return num    
arr = [1, 2, 3, 4, 5]
# print(sum(arr))

# 61. Find largest number in a list.
def largest_numbers(numbers):
    total = numbers[0]
    for n in numbers:
        if n > total:
            total = n
    return total    
arr = [1, 2, 3 ,4, 5, 12]    
print(largest_numbers(arr))
    
    


