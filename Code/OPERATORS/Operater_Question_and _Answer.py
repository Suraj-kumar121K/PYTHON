--> 🧠Arithmetic Operators (1–10)

--> 1 Add two numbers
a = 10
b = 20
print(a + b)

--> 2️⃣ Subtract two numbers
a = 43
b = 20
print(a-b)

--> 3️⃣ Multiply two numbers
a, b = 2, 8
print(a * b)

--> 4️⃣ Divide and floor divide
a, b = 76, 2
print(a/b)

--> 5️⃣ Find remainder (modulus)
a = 15
b = 2
print(a % b)

--> 6️⃣ Power of a number
# ** is the exponentiation operator in Python.
print(2**3) # 2 × 2 × 2 = 8

--> 7️⃣ Average of three numbers
a = 5
b = 10
c = 15
print((a + b + c)/3)

--> 8️⃣ Find area of circle
"""Formula
Area of Circle = 𝜋 × 𝑟2

where
π (pi) = 3.14 (approximately)
r = radius of the circle

r = 7 → radius = 7 units
r ** 2 → radius squared = 7 × 7 = 49
3.14 * r ** 2 → 3.14 × 49 = 153.86
print(area) → displays the result"""
r = 7
area = 3.14 * r ** 2
print(area)

--> 9️⃣ Convert temperature (C → F)
"""Formula
𝐹 = ( 𝐶 × 9/5) + 32
where
--> C = Temperature in Celsius
--> F = Temperature in Fahrenheit"""

c = 30
area = (c * 9/5) + 32
print(area)

--> 🔟 Swap numbers without third variable
a, b = 10, 20
a, b = b, a
print(a, b)

--> 🧩Comparison Operators (11–20)
--> 11 Check if number is greater
a, b = 20, 5
print(a > b);

--> 12️ Equal check
a, b, = 5, 3
print(a == b);

--> 13️ Not equal
a, b = 25, 15
print(a != b)

--> 14️ Check smallest of two numbers
"""This is a Ternary Operator (also called Conditional Expression) in Python.
Syntax:
    <value_if_true> if <condition> else <value_if_false>"""
a, b = 10, 20
print(a if a < b else b)

--> 15️ Check if number lies between range
x = 23
print(20 < x < 30)

--> 16 Compare strings alphabetically
a = "apple"
b = "banana"
s = a < b
print(s)


--> 17️ Check two variables point to same object
x = y = [1, 2, 3]
print(x is y)

--> 18️ Compare list equality (values only)
a = [1, 2]
b = [1, 2]
s = a == b
print(s)

--> 19️ Compare float precision
print(round(0.1 + 0.2, 1) == 0.3)

--> 20️ Compare string lengths
a, b = "python", "java"
print(len(a) > len(b))

--> 🔢Logical Operators (21–30)
--> 21. Check if both numbers are positive
x, y = 5, 10
print(x > 0 and y > 0)

--> 22. Check if any one number is positive
x , y = -3, 7
print(x > 0 or y > 0)

--> 23. Check if both numbers are negative
a, b = -2, -3
print(a < 0 and b < 0)

--> 24. Check if a number lies between 10 and 50
x = -32
print(x > 10 and x < 50)

--> 25. Check if a number is outside 10 and 50
x = 60
print(x < 10 or x > 50)

--> 26. Use not to reverse a condition
a = 50
print(not(a > 10))

--> 27. Combine and and or
a, b, c = 10, 20, 30
print(a < b and b < c or c < a)

--> 28. Check if student passed both subjects
math = 75
science = 80
print(math >= 40 and science >= 40)

--> 29. Check if user input is valid
username = "admin"
password = "1234"
print(username == "admin" and password == "1234")

--> 30. Use not with multiple conditions
x = 15
print(not (x < 10 or x > 20))

--> 31️ Check if number is positive and even
n = 4
print(n > 0 and n % 2 == 0)

--> 32 Check if number is negative or odd
print(n < 0 or n % 2 != 0)

--> 33 Check if string is empty
s = ""
print(not s)

--> 34 Check login logic
user, pwd = "admin", "1234"
print(user == "admin" and pwd == "1234")

--> 35 Validate age range
age = 18
print(age >= 18 and age <= 60)

--> 36 Multiple conditions
x, y, z = 5, 10, 15
print(x > y < z)

--> 37 Logical NOT example
flag = False
print(not flag)

--> 38 Check if either string contains “Python”
str1 = "I am learning Python"
str2 = "Programming is fun"
print("Python" in str1 or "Python" in str2)

--> 39 Check leap year
year = int(input("Enter a year: "))

if year % 4 == 0 and (year % 100 != 0 or year % 400 == 0):
    print(year, "is a leap year")
else:
    print(year, "is not a leap year")

--> 40 Password check
password = "Sur7aj@"
print(len(password) >= 6 and any(ch.isdigit() for ch in password))
