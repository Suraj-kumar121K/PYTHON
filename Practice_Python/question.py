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
# result = int(input("Enter a Number: "))
# mul_table(result)

# 27. Count the number of digits in a number.
def count_digits(num):
    count = 0
    while num > 0:
        num = num // 10
        count += 1
    print(count)
# result = int(input("Enter a Number: "))
# count_digits(result)

# ============================================================
# 5. Lists — Very Important
# ============================================================
# 51. Find the largest element in a list.
def Largest_element(num):
    Largest = num[0]
    for i in num:
        if i > Largest:
            Largest = i
    print(Largest)
# Step 1:
# lar = list(map(int, input("Enter numbers: ").split()))
#Largest_element(lar)

# Step 2:
# n = int(input("How many numbers: "))
# lar = []
# for i in range(n):
#     num = int(input("Enter number: "))
#     lar.append(num)
# Largest_element(lar)
    
# 52. Find the smallest element in a list.
def smallest(num):
    small = num[0]
    for i in num:
        if i < small:
            small = i
    print(small)
# step 1:
# smallest([10, 20, 5, 30])

# Step 2:
# smallests = list(map(int, input("Enter a number ").split()))
# smallest(smallests)

# 55. Find the second-largest element.
def second_largest(num):
    largest = num[0]
    second = num[0]
    for i in num:
        if i > largest:
            second = largest
            largest = i
    print(second)
# step 1:
# second_largest([10, 20, 5, 30])

# 56. Find the second-smallest element.
def second_smallest(num):
    small = num[0]
    second = num[0]
    for i in num:
        if i < small:
            second = small
            small = i
    print(second)
# step 1:
# second_smallest([10, 20, 5, 30])

# 63. Find the top 3 largest numbers.
def third_largest(num):
    largest = num[0]
    second = num[0]
    third = num[0]
    for i in num:
        if i > largest:
            third = second
            second = largest
            largest = i
        elif i > second:
            third = second
            second = i
        elif i > third:
            third = i
    return largest, second, third
# largests = third_largest([10, 20, 30, 50, 40])
# print(largests)

# 64. Find the top 3 smallest numbers.
def top_3_smallest(num):
    small = num[0]
    lower = num[0]
    very_lower = num[0]
    for i in num:
        if i < small:
            very_lower = lower
            lower = small
            small = i
        elif i < lower:
            very_lower = lower
            lower = i
        elif i < very_lower:
            very_lower = i
    return small, lower, very_lower
# largests = top_3_smallest([10, 20, 30, 50, 3, 40, 5])
# print(largests)    

# 65. Separate even and odd numbers into two lists.
num = [1, 2, 3, 4, 5, 6, 7, 8, 9]
first_list = []
second_list = []
for i in num:
    if i % 2 == 0:
        first_list.append(i)
    else:
        second_list.append(i)
print("Even:", first_list)
print("Odd:", second_list)