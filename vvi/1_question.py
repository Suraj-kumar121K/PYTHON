# Number & Logic
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

# 3. Check Prime Number 

# 4. Print Prime Numbers from 1 to N 

# 5. Find Factorial of a Number 

# 6. Find Fibonacci Series 

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
print(gcd(18, 12))

# 9. Find LCM of Two Numbers 
def lcm(a, b):
    multiple = max(a, b)
    while True:
        if multiple % a == 0 and multiple % b == 0:
            return multiple
        multiple += 1
# print(lcm(4, 6))

# 10. Find Sum of Digits
# 11.	Reverse a String 
# 12.	Check Palindrome String 
# 13.	Count Vowels and Consonants 
# 14.	Count Character Frequency 
# 15.	Find First Non-Repeating Character 
# 16.	Check Two Strings are Anagrams 
# 17.	Remove Duplicate Characters 
# 18.	Find Duplicate Characters 
# 19.	Find Largest Word in a String 
# 20.	Count Words in a Sentence
# 21.	Find Largest Element Without max() 
# 22.	Find Second Largest Element 
# 23.	Remove Duplicates from List 
# 24.	Find Duplicate Elements 
# 25.	Find Missing Number from List
# 26.	26. Two Sum Problem 
# 27.	Three Sum Problem 
# 28.	Find Maximum Subarray Sum 
# 29.	Find Common Elements in 3 Lists 
# 30.	Merge Two Sorted Lists 
# 31.	Remove Duplicates from Sorted List 
# 32.	Find Majority Element 
# 33.	Find All Pairs with Given Sum 
# 34.	Rotate a List by K Positions 
# 35.	Find Missing and Duplicate Number

