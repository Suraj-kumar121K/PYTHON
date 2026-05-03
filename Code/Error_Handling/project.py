# Mini Project: Basic Calculator with Error Handling

def calculator():
    try:
        num1 = float(input("Enter first number: "))
        num2 = float(input("Enter second number: "))
        operator = float(input("Choose operator (+, -, *, /): "))
        
        if operator == "+":
            print("Result:", num1 + num2)
        elif operator == "-":
            print("Result:", num1 - num2)
        elif operator == "*":
            print("Result:", num1 * num2)
        elif operator == "/":
            print("Result:", num1 / num2)
        else:
            print("❌ Invalid operator")
    except ValueError:
        print("❌ Please enter numbers only.")
    except ZeroDivisionError:
        print("❌ Division by zero not allowed.")
    finally:
        print("Thank you for using calculator!")
calculator()