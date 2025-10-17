🧠 50 Important Python Variable Questions
🔹 A. Basics of Variables (1–10)

What is a variable in Python?

How do you declare a variable in Python?

Can you assign a value to a variable without declaring its type?

What is dynamic typing in Python?

Write a program to store and print your name.

What is the output of:

name = "Suraj"
print(name)


Can variable names start with a number?

Which of these are valid variable names?

name, _name, 1name, Name_1, for

What are the naming conventions for variables in Python?

Is Python case-sensitive when it comes to variable names?

🔹 B. Variable Assignment (11–18)

What does multiple assignment mean in Python?

Example:

a = b = c = 10
print(a, b, c)


What is the output of:

x, y = 5, 10
print(x + y)


How do you swap two variables without using a third variable?

Write a program to assign different types of values to variables (int, float, str).

What happens if you assign a string to a variable that previously held a number?

Can you assign different values to multiple variables in a single line?

Write a program to input two numbers and swap their values.

🔹 C. Data Types with Variables (19–26)

What is the data type of the variable x = 3.14?

Write a program to print the type of a variable using type().

What is the output of:

a = 10
b = "10"
print(type(a), type(b))


Can a variable change its data type after assignment?

Example:

x = 5
x = "Hello"
print(x)


What is the difference between integer and float variables?

Write a program to store a boolean value in a variable.

Can a variable store complex numbers in Python?

🔹 D. Global and Local Variables (27–35)

What is the difference between a local and a global variable?

Write a program using a local variable inside a function.

Write a program using a global variable inside a function.

What does the global keyword do?

What will be the output:

x = 10
def show():
    x = 5
    print(x)
show()
print(x)


What will be printed:

x = 20
def test():
    global x
    x = 50
test()
print(x)


Can you use the same variable name for local and global variables?

How do you access a global variable inside a function?

What happens if a variable is used before assignment inside a function?

🔹 E. Constants & Naming Rules (36–42)

What is a constant in Python?

Does Python have a built-in constant keyword?

How are constants usually written in Python?

Example:

PI = 3.1416
print(PI)


What will happen if you change the value of PI later?

Can variable names contain spaces?

Which variable names are invalid?

user name

user_name

userName

User-Name

🔹 F. Memory & ID Concept (43–47)

What does the id() function do in Python?

What is the output of:

a = 10
b = 10
print(id(a), id(b))


What is variable referencing in Python?

When do two variables have the same memory ID?

What happens when two variables point to the same object?

🔹 G. Application & Logic Questions (48–50)

Write a program to accept a user's name and age, then display them together.

Write a program to calculate the total and average of 3 subjects using variables.

Write a program to find the area of a rectangle using variables for length and width.
