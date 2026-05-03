# Exception Handling with try and except
"""try:
    num = int(input("Enter a number: "))
    print(10 / num)
except:
    print("Oops! Something went wrong.")"""
    
# Handling Specific Exceptions
"""try:
    num = int(input("Enter a number: "))
    print(10 / num)
except ValueError:
    print("❌ Please enter a valid number.")
except ZeroDivisionError:
    print("❌ Division by zero is not allowed.")"""
    
# Using else with try-except
"""try:
    num = int(input("Enter a number: "))
    print("Square:", num ** 2)
except ValueError:
    print("Invalid input, please enter a number.")
else:
    print("✅ Program ran successfully!")"""

# Custom Exceptions
"""class NegativeNumberError(Exception):
    pass

def check_number(num):
    if num < 0:
        raise NegativeNumberError("Negative numbers are not allowed.")
    else:
        print("Number is valid!")

try:
    check_number(-5)
except NegativeNumberError as e:
    print("❌ Error:", e)"""