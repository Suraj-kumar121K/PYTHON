# 1. Reverse a number 
def reverse(num):
    rev = 0

    while num > 0:
        digit = num % 10
        rev = rev * 10 + digit
        num = num // 10
    print(rev)
# reverse(123456)

# 2. Check Palindrome Number 
def Palindrome(num):
    original = num
    reverse = 0
    while num > 0:
        digit = num % 10
        reverse = reverse * 10 + digit
        num = num // 10
    if  original == reverse:
        print("Palindrome Number ")
    else:
        print("Not Palindrome Number")
# Palindrome(121)
 

# 6. Find Fibonacci Series 
def fib(num):
    a = 0
    b = 1
    for i in range(num):
        print(a, end=" ")
        a, b = b, a + b
# fib(10)

# 7. Check Armstrong Number 
def armstrong(num):
    original = num
    digits = len(str(num))
    total = 0
    while num > 0:
        digit = num % 10
        total = total + digit ** digits
        num = num // 10
    if total == original:
        print("Armstrong Number")
    else:
        print("Not Armstrong Number")
# armstrong(123)

# 8. Find GCD/HCF of Two Numbers 
def gcd(a, b):
    smaller = min(a, b)
    while smaller > 0:
        if a % smaller == 0 and b % smaller == 0:
            return smaller
        smaller -= 1
# print(gcd(18, 12))

# 9. Find LCM of Two Numbers 
def lcm(a, b):
    multiple = max(a, b)
    while True:
        if multiple % a == 0 and multiple % b == 0:
            return multiple
        multiple += 1
# print(lcm(4, 6))

# Q1. Write a Python program to find the largest number in a list.
def Largest_Number(num):
    largest = num[0]
    for i in num:
        if i > largest:
            largest = i
    print(largest)
# Largest_Number([10, 20, 50, 30, 40, 1])

# Q2. Write a Python program to find the smallest number in a list.
num = [10, 20, 50, 30, 40, 1]
smaller = num[0]
for i in num:
    if i < smaller:
        smaller = i
# print(smaller)

# Q3. Write a Python program to find the second largest number in a list.
num = [10, 20, 50, 30, 40, 1]
largest = num[0]
second = num[0]
for i in num:
    if i > largest:
        second = largest
        largest = i
    elif i > second and i != largest:
        second = i
# print(second)

# program Two Sum
def two_sum(num, target):
    for i in range(len(num)):
        for j in range(i + 1, len(num)):
            if num[i] + num[j] == target:
                return [i, j]
num = [2, 7, 11, 15]
target = 18
result = two_sum(num, target)
print(result)