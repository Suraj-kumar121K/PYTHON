--> 🧠Arithmetic Operators (1–10)

--> 1️⃣ Add two numbers
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
