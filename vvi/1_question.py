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
 

# 3. Find Fibonacci Series 
def fib(num):
    a = 0
    b = 1
    for i in range(num):
        print(a, end=" ")
        a, b = b, a + b
# fib(10)

# 4. Check Armstrong Number 
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

# 5. Find GCD/HCF of Two Numbers 
def gcd(a, b):
    smaller = min(a, b)
    while smaller > 0:
        if a % smaller == 0 and b % smaller == 0:
            return smaller
        smaller -= 1
# print(gcd(18, 12))

# 6. Find LCM of Two Numbers 
def lcm(a, b):
    multiple = max(a, b)
    while True:
        if multiple % a == 0 and multiple % b == 0:
            return multiple
        multiple += 1
# print(lcm(4, 6))

# 7. Write a Python program to find the largest number in a list.
def Largest_Number(num):
    largest = num[0]
    for i in num:
        if i > largest:
            largest = i
    print(largest)
# Largest_Number([10, 20, 50, 30, 40, 1])

# 8. Write a Python program to find the smallest number in a list.
num = [10, 20, 50, 30, 40, 1]
smaller = num[0]
for i in num:
    if i < smaller:
        smaller = i
# print(smaller)

# 9. Write a Python program to find the second largest number in a list.
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

# 10. program Two Sum
def two_sum(num, target):
    for i in range(len(num)):
        for j in range(i + 1, len(num)):
            if num[i] + num[j] == target:
                return [i, j]
num = [2, 7, 11, 15]
target = 18
result = two_sum(num, target)
# print(result)

# 11. Write a program to count the number of characters in a string.
def count_number(name):
    count = 0
    for char in name:
        count += 1
    return count
# print(count_number("Suraj Kumar"))


# 12. Write a program to reverse a string.
def reverse_str(name):
    rev = ""
    i = len(name) - 1
    while i >= 0:
        rev += name[i]
        i -= 1
    return rev
# print(reverse_str("Suraj Kumar Raj"))

def reverse_list(number):
    list = []
    i = len(number) - 1
    while i >= 0:
        list.append(number[i])
        i -= 1
    return list
# print(reverse_list([10, 20, 30, 40]))

# 21. Find the first non-repeating character in a string.
def first_non_repeating(s):
    frequency = {}
    # Step 1: Count frequency
    for char in s:
        frequency[char] = frequency.get(char, 0) + 1
    # Step 2: Find first character with frequency 1
    for char in s:
        if frequency[char] == 1:
            return char
    return None
# print(first_non_repeating("swiss"))

# 22. Find duplicate characters in a string.
def duplicate_characters(s):
    frequency = {}
    for char in s:
        frequency[char] = frequency.get(char, 0) + 1
    duplicates = []
    for char in frequency:
        if frequency[char] > 1:
            duplicates.append(char)
    return duplicates
# print(duplicate_characters("programming"))

# 23. Find the frequency of each character in a string.
def character_frequency(s):
    frequency = {}
    for char in s:
        frequency[char] = frequency.get(char, 0) + 1
    return frequency
print(character_frequency("hello"))

# 24. Check whether two strings are anagrams.
def is_anagram(s1, s2):
    s1 = s1.replace(" ", "").lower()
    s2 = s2.replace(" ", "").lower()
    if len(s1) != len(s2):
        return False
    frequency = {}
    for char in s1:
        frequency[char] = frequency.get(char, 0) + 1
    for char in s2:
        if char not in frequency:
            return False
        frequency[char] -= 1
        if frequency[char] < 0:
            return False
    return True
print(is_anagram("listen", "silent"))

# 25. Find the largest word in a sentence.
def largest_word(sentence):
    words = sentence.split()

    largest = ""

    for word in words:
        if len(word) > len(largest):
            largest = word

    return largest


print(largest_word("Python is very powerful"))

# 27. Reverse each word of a sentence.
def reverse_each_word(sentence):
    words = sentence.split()

    result = []

    for word in words:
        result.append(word[::-1])

    return " ".join(result)
print(reverse_each_word("Python is easy"))

# 28. Remove duplicate characters from a string.
def remove_duplicates(s):
    result = ""

    for char in s:
        if char not in result:
            result += char

    return result
print(remove_duplicates("programming"))

# 29. Find the most frequent character in a string.
def most_frequent_character(s):
    frequency = {}

    for char in s:
        frequency[char] = frequency.get(char, 0) + 1

    max_frequency = 0
    result = None

    for char in s:
        if frequency[char] > max_frequency:
            max_frequency = frequency[char]
            result = char

    return result
print(most_frequent_character("programming"))
