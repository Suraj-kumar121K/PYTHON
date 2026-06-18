# ⚡ Rule Yaad Karo:
"""
num % 10 → Last digit nikalta hai.
num // 10 → Last digit hata deta hai.
while num > 0 → Har digit par loop chalta hai.
"""
#1. Reverse Number
"""
num = int(input("Enter a Number: "))
rev = 0
while num > 0:
    digit = num % 10 # get the last digit
    rev = rev * 10 + digit # add the last digit
    num = num // 10 # remove the last digit
print(rev)
"""

# 2. Check whether number is a palindrome
"""
num = int(input("Enter a Number: "))
tem = num
rev = 0
while num > 0:
    digit = num % 10
    rev = rev * 10 + digit
    num = rev // 10
    if tem == rev:
        print("palindrome")
    else:
        print("Not palindrome")
"""

# 3. Count Digits in a Number.
"""num = int(input("Enter a Number: "))
count = 0
while num > 0:
    count += 1
    num = num // 10
print(count)"""

# 4. Sum of Digits
"""num = int(input("Sum of Number "))
sum = 0
while num > 0:
    digit = num % 10
    sum += digit
    num = num // 10
print("Sum of Digits = ", sum)"""

# 5. Product of Digits
"""num = int(input("Enter a Number "))
product = 1
while num > 0:
    digit = num % 10
    product *= digit
    num = num // 10
print("sum = ", product)"""

# 6. Find Largest Digit
"""num = int(input("largest Number "))
largest = 0
while num > 0:
    digit = num % 10
    if digit > largest:
        largest = digit
    num = num // 10
print(largest)"""

# 7. Find Smallest Digit
"""
num = int(input("Enter a Number: "))
smallest = 9
while num > 0:
    digit = num % 10
    if digit < smallest:
        smallest = digit
    num = num // 10
print("Smallest Digit =", smallest)
"""

# 8. Count Even Digits
"""
num = int(input("Enter a Number: "))
count = 0
while num > 0:
    digit = num % 10
    if digit % 2 == 0:
        count += 1
    num = num // 10
print("Even Digits =", count)
"""

# 9. Count Odd Digits
"""
num = int(input("Enter a Number: "))
count = 0
while num > 0:
    digit = num % 10
    if digit % 2 != 0:
        count += 1
    num = num // 10
print("Even Digits =", count)
"""

# 10. Print Digits One by One

# 11. Find Second Largest Digit
"""
num = int(input("Enter a Number: "))
largest = 0
second = 0
while num > 0:
    digit = num % 10
    if digit > largest:
        second = largest
        largest = digit
    elif digit > second and digit != largest:
        second = digit
    num = num // 10
print("Second Largest = ", second)
"""
# 12. Find Second Smallest Digit
"""
num = int(input("Enter a Number: "))
largest = 9
second = 9
while num > 0:
    digit = num % 10
    if digit < largest:
        second = largest
        largest = digit
    elif digit > second and digit != largest:
        second = digit
    num = num // 10
print("Second Largest = ", second)
"""
# 13. Check Armstrong Number

# 14. Check Strong Number

# 15. Check Perfect Number

# 16. Check Prime Number

# 17. Print Factors of a Number

# 18. Sum of Factors

# 19. Count Factors

# 20. Check Neon Number

# 21. Fibonacci Series using Loop

# 22. Find GCD (HCF) of Two Numbers

# 23. Find LCM of Two Numbers

# 24. Convert Decimal to Binary

# 25. Convert Binary to Decimal

# 26. Count Frequency of Each Digit

# 27. Remove Duplicate Digits from a Number

# 28. Print Number Pattern

# 29. Print Star Pattern

# 30. Find Missing Number in a Series