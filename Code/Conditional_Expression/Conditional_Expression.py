--> 🧠 What is a Conditional Expression?
    A conditional expression in Python allows you to write an if-else statement in a single line

--> 🧩 Syntax:
     x = value_if_true if condition else value_if_false

--> 📘 Example 1:
a = 10
b = 20
# Find the greater number using conditional expression
max_value = a if a > b else b
print(max_value)

Example 2:
age = 18
message = "Eligible to vote" if age >= 18 else "Not eligible"
print(message)

Example 3:
You can also nest them (though not always recommended for readability):
marks = 85
result = "Excellent" if marks >= 90 else "Good" if marks >= 75 else "Average"
print(result)

-->💡 Why use Conditional Expressions?
✅ Shorter and cleaner code
✅ Perfect for simple decisions
✅ Often used in assignments, lambdas, or list comprehensions

--> 🔍 Comparison with Normal If-Else:
if a > b:
    max_value = a
else:
    max_value = b

--> Conditional Expression:
max_value = a if a > b else b
