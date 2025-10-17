--> What is Operaters
    Operators are symbols or keywords used to perform operations on variables and values.
    They tell Python what kind of operation to perform.

--> Example:
    x = 10
    y = 5
    print(x + y)   # '+' is an operator that adds values

--> ⚙️ Types of Operators in Python
     
--> Python has 7 types of operators:

No.	         Operator Type	                     Description
1	     Arithmetic Operators	         Used for mathematical operations
                                             
2	     Assignment Operators	         Used to assign values to variables

3	     Comparison Operators	         Used to compare two values

4	     Logical Operators	             Used for logical conditions
                                             
5	     Bitwise Operators	             Used to perform bit-level operations

6	     Membership Operators	         Used to test membership in sequences

7	     Identity Operators	             Used to compare memory locations

--> 🔹 1. Arithmetic Operators
     Used to perform basic math operations.
         
| Operator | Description         | Example   | Output   |
| -------- | ------------------- | --------- | -------- |
| `+`      | Addition            | `10 + 5`  | 15       |
| `-`      | Subtraction         | `10 - 5`  | 5        |
| `*`      | Multiplication      | `10 * 5`  | 50       |
| `/`      | Division            | `10 / 3`  | 3.333... |
| `%`      | Modulus (remainder) | `10 % 3`  | 1        |
| `**`     | Exponent (power)    | `2 ** 3`  | 8        |
| `//`     | Floor Division      | `10 // 3` | 3        |

--> EXAMPLES
a = 10
b = 3
print("Addition:", a + b)
print("Subtraction:", a - b)
print("Multiplication:", a * b)
print("Division:", a / b)
print("Floor Division:", a // b)
print("Modulus:", a % b)
print("Exponent:", a ** b)
         
--> 🔹 2. Assignment Operators
       Used to assign values to variables.
       They can also modify existing values.
| Operator | Example   | Same As       |
| -------- | --------- | ------------- |
| `=`      | `x = 5`   | Assign 5 to x |
| `+=`     | `x += 3`  | `x = x + 3`   |
| `-=`     | `x -= 3`  | `x = x - 3`   |
| `*=`     | `x *= 3`  | `x = x * 3`   |
| `/=`     | `x /= 3`  | `x = x / 3`   |
| `%=`     | `x %= 3`  | `x = x % 3`   |
| `**=`    | `x **= 3` | `x = x ** 3`  |
| `//=`    | `x //= 3` | `x = x // 3`  |

-->  Example 
x = 10
x += 5
print(x)  # 15
x *= 2
print(x)  # 30

-->🔹 3. Comparison Operators (Relational)
Used to compare two values.
Always return True or False.
| Operator | Meaning                  | Example  | Result |
| -------- | ------------------------ | -------- | ------ |
| `==`     | Equal to                 | `5 == 5` | True   |
| `!=`     | Not equal to             | `5 != 3` | True   |
| `>`      | Greater than             | `5 > 3`  | True   |
| `<`      | Less than                | `5 < 3`  | False  |
| `>=`     | Greater than or equal to | `5 >= 5` | True   |
| `<=`     | Less than or equal to    | `3 <= 5` | True   |

--> Example
a = 10
b = 20
print(a == b)  # False
print(a != b)  # True
print(a < b)   # True

-->🔹4. Logical Operators
Used to combine conditional statements.
Return True or False.
| Operator | Description             | Example             | Result |
| -------- | ----------------------- | ------------------- | ------ |
| `and`    | True if both are true   | `(5 > 3 and 6 > 4)` | True   |
| `or`     | True if any one is true | `(5 > 3 or 6 < 4)`  | True   |
| `not`    | Reverses the result     | `not(5 > 3)`        | False  |

--> Example
a = 5
b = 10
print(a > 2 and b > 5)   # True
print(a > 10 or b > 5)   # True
print(not(a > 2))        # False

-->🔹 5. Bitwise Operators
      Used to perform operations on binary (bit) numbers.
| Operator | Name        | Example  | Explanation            |    |                        |
| -------- | ----------- | -------- | ---------------------- | -- | ---------------------- |
| `&`      | AND         | `5 & 3`  | 0101 & 0011 → 0001 (1) |    |                        |
| `        | `           | OR       | `5                     | 3` | 0101 | 0011 → 0111 (7) |
| `^`      | XOR         | `5 ^ 3`  | 0101 ^ 0011 → 0110 (6) |    |                        |
| `~`      | NOT         | `~5`     | -(5+1) = -6            |    |                        |
| `<<`     | Left Shift  | `5 << 1` | 10                     |    |                        |
| `>>`     | Right Shift | `5 >> 1` | 2                      |    |                        |

--> Example
a = 5  # 0101
b = 3  # 0011
print(a & b)   # 1
print(a | b)   # 7
print(a ^ b)   # 6
print(~a)      # -6
print(a << 1)  # 10
print(a >> 1)  # 2

--> 🧩 6. Operator Precedence (Order of Execution)
        Python follows a priority order when evaluating expressions:
| Priority | Operator Type                               | Example             |
| -------- | ------------------------------------------- | ------------------- |
| 1        | Parentheses `( )`                           | `(3 + 2) * 5`       |
| 2        | Exponentiation `**`                         | `2 ** 3`            |
| 3        | Multiplication / Division / Floor / Modulus | `*`, `/`, `//`, `%` |
| 4        | Addition / Subtraction                      | `+`, `-`            |
| 5        | Comparison                                  | `==`, `<`, `>`      |
| 6        | Logical Operators                           | `not`, `and`, `or`  |

--> # 🌟 Python Operators Full Example 🌟

a = 10
b = 5
# Arithmetic
print("Addition:", a + b)
print("Subtraction:", a - b)
print("Multiplication:", a * b)
print("Division:", a / b)

# Assignment
x = 10
x += 5
print("x after += 5:", x)

# Comparison
print(a == b)
print(a > b)

# Logical
print(a > 5 and b < 10)
print(not(a < b))

# Bitwise
print(a & b, a | b, a ^ b, ~a, a << 1, a >> 1)

# Membership
text = "Python"
print('P' in text, 'x' not in text)

# Identity
y = a
z = 10
print(a is y, a is z)

--> 🧩 Operator Problems in Python (With Solutions)

--> ✔️1. Add two numbers using arithmetic operators
a = 10
b = 5
print("Sum =", a + b)

--> ✔️2. Find the remainder when a number is divided by another
a = 17
b = 4
print("Remainder =", a % b)

--> ✔️3. Calculate area of a rectangle using * operator
length = 6
width = 3
area = length * width
print("Area =", area)


--> ✔️4. Swap two numbers using assignment operators
a = 5
b = 7
a, b = b, a
print("a =", a, "b =", b)


Output: a = 7 b = 5

--> ✔️5. Increase a number by 10 using += operator
x = 25
x += 10
print("After += 10 →", x)

--> ✔️6. Check which number is greater
a = 15
b = 12
print("a is greater:", a > b)

--> ✔️7. Check if two numbers are equal
a = 50
b = 50
print("Equal?", a == b)


Output: Equal? True

--> ✔️8. Find maximum of three numbers using logical operators

a, b, c = 20, 45, 30
if a > b and a > c:
    print("Max =", a)
elif b > a and b > c:
    print("Max =", b)
else:
    print("Max =", c)

--> ✔️9. Check if a number is between 10 and 50
x = 25
print(10 < x < 50)

--> ✔️10. Check if a number is even using modulus operator
n = 8
if n % 2 == 0:
    print("Even")
else:
    print("Odd")

--> ✔️11. Check if both conditions are true (using and)
a = 10
b = 20
print(a > 5 and b < 25)

--> ✔️12. Check if any condition is true (using or)
a = 3
b = 8
print(a > 5 or b > 5)

--> ✔️13. Reverse a boolean value (using not)
x = True
print(not x)

--> ✔️14. Check membership of a letter
name = "Python"
print('y' in name)
print('z' not in name)

--> ✔️15. Compare identity of two variables
a = [1, 2, 3]
b = a
c = [1, 2, 3]
print(a is b)   # True (same object)
print(a is c)   # False (different object)

--> ✔️16. Check if a number is positive, negative, or zero
num = -5
if num > 0:
    print("Positive")
elif num == 0:
    print("Zero")
else:
    print("Negative")

--> ✔️17. Use bitwise AND, OR, XOR
a = 5   # 0101
b = 3   # 0011
print("AND:", a & b)
print("OR:", a | b)
print("XOR:", a ^ b)

--> ✔️ 18. Multiply a number by 2 using left shift
a = 5
print("5 << 1 =", a << 1)

--> ✔️ 19. Divide a number by 2 using right shift
a = 10
print("10 >> 1 =", a >> 1)

--> ✔️ 20. Use all operators in one example
a = 10
b = 4

print("Add:", a + b)
print("Sub:", a - b)
print("Mul:", a * b)
print("Div:", a / b)
print("Mod:", a % b)
print("Exp:", a ** b)
print("Floor:", a // b)

a += 2
print("After += 2:", a)

print("Comparison:", a > b)
print("Logical:", a > 5 and b < 10)
print("Membership:", 'a' in 'apple')
print("Identity:", a is b)
