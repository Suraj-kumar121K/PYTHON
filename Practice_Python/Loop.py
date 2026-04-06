# While loop
"""i = 1
while i <= 10:
    print(i)
    i += 1"""

#  Simple Counting
# 1. Print numbers from 1 to 10.
"""user = 1
while user <= 10:
    print(user)
    user += 1"""
    
# 2. Print numbers from 10 to 1.
"""a = 10
while a >= 1:
    print(a)
    a -= 1"""

# 3. Print even numbers from 1 to 20.
"""a = 0
while a <= 20:
    if a % 2 == 0:
        print(f"{a} Even number")
    a += 1"""
        
# 4. Print odd numbers from 1 to 20.
"""a = 1
while a <= 20:
    if a % 2 != 0:
        print(f"{a} Odd Number")
    a += 1"""

# 5. Print multiples of 5 from 5 to 50.
"""a = 5 
while a <= 50:
    if a % 5 == 0:
        print(a)
    a += 1"""
    
# 6. Find the sum of numbers from 1 to n (take n as input).
"""sum = int(input("Enter a Number: "))
i = 1
total = 0
while i <= sum:
    total += i
    i += 1
print(f"Sum of numbers from 1 to {sum} is {total}")"""

# 7. Countdown from 10 to 1.
"""i = 10
while i >= 1:
    print(i)
    i -= 1"""
    
# 8. Print numbers from 1 to 100 divisible by 7.
"""i = 1
while i <= 100:
    if i % 7 == 0:
        print(i)
    i += 1"""
    
# 9. Print numbers from 50 to 100 divisible by 3 and 5.
"""i = 50
while i <= 100:
    if i % 3 == 0 and i % 5 == 0:
        print(i)
    i += 1"""
    
# 10. Print the square of numbers from 1 to n.
"""n = int(input("Enter a Number: "))
i = 1
while i <= n:
    print(f"Square of {i} is {i**2}")
    i += 1"""
    
# String & Character Loops
# 11. Print all characters of a string.
"""s = input("Enter a String ")
i = 0
while i < len(s):
    print(s[i])
    i += 1"""
    
# 12. Count the number of vowels in a string.
"""s = input("Entera a String ")
i = 0
count = 0
while i < len(s):
    if s[i] in "aeiouAEIOU":
        count += 1
    i += 1
print("Number of vowels:", count)
"""
# 13. Reverse a string using a while loop.
"""s = input("Enter a String: ")
i = len(s) -1 
rev_str = ""
while i >= 0:
    rev_str += s[i]
    i -= 1
print("revers string", rev_str)"""

# 14. Count consonants in a string.


# 15. Count spaces in a string.


# 16. Count uppercase letters in a string.


# 17. Count lowercase letters in a string.


# 18. Print all digits in a string.


# 19. Print each character of a string one by one.


# 20. Find the position of the first vowel in a string.


#  Number Patterns
# 21. Print a number triangle from 1 to 5.

# 22. Find the factorial of a number n.
"""num = int(input("Enter a Number: "))
fact = 1
i = 1
while i < num:
    fact *= i
    i += 1
print(f"{num} != {fact}")"""

# 23. Print the first n numbers of the Fibonacci series.
"""num = int(input("Enter a Number: "))
i = 0
a = 0
b = 1
while i < num:
    print(a, end=" ")
    a = b
    b = a + b
    i += 1
    """
# 24. Print all prime numbers from 1 to n.
"""n = int(input("Enter n: "))  # User input
num = 2                       # Start checking from 2

while num <= n:               # Loop har number ke liye 2 se n tak
    is_prime = True           # Assume num prime hai
    i = 2                     # Check divisibility start from 2
    
    while i*i <= num:         # i*i <= num is same as i <= sqrt(num)
        if num % i == 0:      # Agar num divisible hua
            is_prime = False  # Not prime
            break             # Loop ko stop karo
        i += 1                # Next divisor check karo
    
    if is_prime:               # Agar prime hai
        print(num, end=" ")    # Print karo
    num += 1                   # Next number check karo
print(f"Prime numbers from 1 to {n}:")"""

# 25. Print all Armstrong numbers from 1 to n.
"""n = int(input("Enter a Armstrong: "))
print(f"Armstrong numbers from 1 to {n} / 1 se {n} tak ke Armstrong numbers:")
for num in range(1, n + 1):
    sum_digits = 0
    k = len(str(num))
    
    for digit_char in str(num):
        digit = int(digit_char)
        sum_digits += digit ** k
    if sum_digits == num:
        print(num, end=" ")"""

# 26. Print all palindrome numbers from 1 to n.
"""num = int(input("Enter a number "))
temp = num
reverse = 0
while temp > 0:
    digits = temp % 10
    reverse = reverse * 10 + digits
    temp = temp // 10
if num == reverse:
    print("palindrome numbers")
else:
    print("Not palindrome numbers")"""
        
# 27. Print the multiplication table of any number.
"""num = int(input("Enter a Number "))
i = 1
while i <= 10:
    print(f"{num} X {i} = ", num * i)
    i += 1
"""
# 28. Reverse a number.
"""num = int(input("Enter a Number: "))
temp = num
reverse = 0

while temp > 0:
    digit = temp % 10
    reverse = reverse * 10 + digit
    temp = temp // 10

print("Reverse number is:", reverse)"""

# 29. Print digits of a number one by one.
# 30. Find the sum of digits of a number.

#  Logical / Mixed Questions
# 31. Create a number guessing game (1–50).
# 32. Ask for a password repeatedly until the correct one is entered.

# 33. Take a number as input and check if it is prime.

# 34. Take a number as input and check if it is an Armstrong number.

# 35. Take a number as input and find its factorial.

# 36. Find the sum of all even digits of a number.

# 37. Find the sum of all odd digits of a number.

# 38. Reverse a number using a while loop.

# 39. Print numbers from 1 to n divisible by 4.

# 40. Keep taking numbers as input from the user and calculate their sum until the user enters 0.

# FOR LOOP
# 🔹 Beginner Level (1–15)
# 1. Print numbers from 1 to 10.
"""for i in range(1, 11):
    print(i)"""
    
# 2. Print numbers from 10 to 1 in reverse.
"""for i in range(11, 1, -1):
    print(i)"""
    
# 3. Print all even numbers from 1 to 20.
"""for i in range(0,21,2):
    print(f"{i} Even Number")"""

# 4. Print all odd numbers from 1 to 20.
"""for i in range(1, 21, 2):
    print(i)"""
    
# 5. Print the square of numbers from 1 to 10.
"""for i in range(1, 11):
    print(f"{i} Square Number {i*i}")"""
    
# 6. Print the cube of numbers from 1 to 10.
"""for i in range(1, 11):
    print(f"{i} Square Number {i**3}")"""
    
# 7. Print numbers divisible by 3 between 1 and 30.
"""for var in range(3,30,3):
    print(var)"""
        
# 8. Print the first 10 multiples of 5.


# 9. Print all characters of a string one by one.
text = "Suraj"
for i in text:
    print(i)
    
# 10. Print all vowels in a given string.
# 11. Print all consonants in a given string.
# 12. Count the number of characters in a string.
# 13. Print all numbers from 1 to 50 that are divisible by both 2 and 5.
# 14. Print factorial of a number n.
# 15. Print the sum of first n natural numbers.

# 🔹 Intermediate Level (16–30)
# 16. Print the multiplication table of a given number.
# 17. Print all prime numbers between 1 and 50.
# 18. Print all numbers from 1 to n and their squares.
# 19. Print all numbers from 1 to n and their cubes.
# 20. Print numbers from 1 to 100 that are divisible by 7.
# 21. Print Fibonacci series up to n terms.
# 22. Reverse a string using a for loop.
# 23. Count the number of vowels in a string.
# 24. Count the number of digits in a string.
# 25. Print the sum of all digits of a number.
# 26. Print all characters of a string in uppercase.
# 27. Print all characters of a string in lowercase.
# 28. Print ASCII values of all characters in a string.
# 29. Print the sum of even numbers from 1 to n.
# 30. Print the sum of odd numbers from 1 to n.

# 🔹 Advanced Level (31–40)
# 31. Print a right-angled triangle pattern of * of height n.
# 32. Print a pyramid pattern of numbers up to n.
# 33. Print a diamond pattern using *.
# 34. Print all palindromic numbers from 1 to 100.
# 35. Print all numbers divisible by 3 but not by 5 between 1 and 50.
# 36. Print all characters of a string except spaces.
# 37. Print all words of a sentence separately.
# 38. Print numbers from 1 to 50 skipping multiples of 4.
# 39. Print a pattern of numbers like this:
#     1
#     12
#     123
#     1234
# 40. Print the multiplication table for numbers 1 to 10.

# 🔹 Part 1: break Practice (1–20)
# 1. Print numbers from 1 to 10 but stop at 5.
# 2. Print numbers 1 to 20 but stop when a number divisible by 7 is found.
# 3. Print numbers from 1 to 50, stop when you find the first number divisible by both 3 and 5.
# 4. Ask user for numbers and stop when they enter 0.
# 5. Print characters of a string but stop at first vowel.
# 6. Print numbers 1 to 100, stop at the first prime number greater than 50.
# 7. Print numbers 1 to n, stop if a number is perfect square.
# 8. Print numbers 1–20, stop when sum of printed numbers exceeds 50.
# 9. Find first negative number in a list and print it.
# 10. Ask user for input repeatedly, stop when they type "exit".
# 11. Print numbers 1–100, stop when you find a number ending with 7.
# 12. Find first word in a sentence with length greater than 5.
# 13. Print first 5 even numbers using a loop with break.
# 14. Stop printing numbers from 1 to 50 after printing the first 3 multiples of 4.
# 15. Stop reading characters from a string when 'z' is encountered.
# 16. Stop printing numbers from 1 to n if the sum of digits equals 10.
# 17. Stop reading numbers from a list when a prime number is found.
# 18. Stop asking user for numbers after 3 invalid inputs.
# 19. Print numbers from 1 to 100, stop at the first palindrome number greater than 50.
# 20. Stop a loop when the product of numbers exceeds 1000.

# 🔹 Part 2: continue Practice (21–40)
# 21. Print numbers 1–20 skipping even numbers.
# 22. Print numbers 1–20 skipping odd numbers.
# 23. Print numbers 1–50 skipping multiples of 3.
# 24. Print numbers 1–50 skipping numbers divisible by both 2 and 5.
# 25. Print all characters in a string except vowels.
# 26. Print numbers 1–100 skipping multiples of 7.
# 27. Print numbers 1–50 skipping numbers whose digits sum to 5.
# 28. Print numbers 1–20, skip the first 3 numbers divisible by 2.
# 29. Print numbers 1–30 skipping prime numbers.
# 30. Print numbers 1–50 skipping perfect squares.
# 31. Print all words of a sentence except the word "the".
# 32. Print numbers 1–100 skipping multiples of 4.
# 33. Print numbers 1–50 skipping numbers ending with 5.
# 34. Print ASCII values of characters in a string skipping spaces.
# 35. Print numbers 1–50 skipping numbers divisible by 3 but not 5.
# 36. Print numbers 1–50 skipping numbers containing digit 7.
# 37. Print numbers 1–20 skipping first 2 even numbers.
# 38. Print numbers 1–100 skipping numbers divisible by 2 or 3.
# 39. Print numbers 1–50 skipping numbers whose square is greater than 400.
# 40. Print characters in a string skipping every second character.

# 🔹 Part 3: pass Practice (41–50)
# 41. Use pass in a loop iterating 1–10 without doing anything.
# 42. Create a loop over a string and pass for vowels, print consonants.
# 43. Loop through numbers 1–20, pass for odd numbers, print even numbers.
# 44. Loop over a list, pass for negative numbers, print positive numbers.
# 45. Use pass in a nested loop structure (like triangle pattern).
# 46. Loop over words in a sentence, pass for word "skip", print others.
# 47. Use pass in a while loop counting from 1–10.
# 48. Use pass in a loop when number divisible by 3, print others.
# 49. Loop from 1–10, pass for prime numbers, print non-prime numbers.
# 50. Loop through numbers 1–20, pass for multiples of 5, print the rest.

# 🔹 Part 4: Mixed break, continue, pass (51–60)
# 51. Print numbers 1–50, stop if divisible by 7 (break), skip even numbers (continue).
# 52. Print characters in a string, skip vowels (continue), stop at 'z' (break).
# 53. Loop 1–20, skip numbers divisible by 3 (continue), pass for odd numbers (pass).
# 54. Print numbers 1–100, stop at first number whose digits sum to 10 (break).
# 55. Print numbers 1–50 skipping numbers divisible by 5 (continue) and stop at 37 (break).
# 56. Loop through a sentence, skip "a" (continue), pass for punctuation (pass).
# 57. Print numbers 1–20, skip multiples of 4 (continue), stop at 17 (break).
# 58. Loop 1–50, pass for numbers divisible by 3, skip numbers divisible by 7, print rest.
# 59. Print first 10 characters of a string, skip spaces (continue), stop at punctuation (break).
# 60. Loop numbers 1–100, skip numbers divisible by 2 (continue), pass numbers divisible by 5 (pass), print others.

