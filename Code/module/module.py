# Modul and Packages
# What is modules
# Module is a single python file (.py) containing Python code.It can include functions, classes and variables that you can reuse in other programs.


# Why use modules
# To organize code into smaller, manageable chunks.
# To reuse code across multiple programs

# # Create a module
# Save the following as mymodule.py
# def say_hello(name):
# return print(f"Hello, {name}!")

# Types of Import Statements
# 1. Import From Module: This allows importing specific functions, classes, or variables rather than the whole module.

# from math import sqrt, factorial
# print(sqrt(16))
# print(factorial(6))

# 2. Import All Names: * imports everything from a module into the current namespace.

# from math import *
# print(sqrt(16))
# print(factorial(6))

# 3. Import With Alias: You can shorten a module's name using as.

# import math as m
# print(m.pi)

# Type of modules
# 1. Built-in Modules:  built-in module is part of Python’s standard library, available as soon as you install Python. 
# Examples: 
# math → for mathema cal func ons 
# random → for random number genera on 
# os → for opera ng system tasks 
# dateme → for working with dates and mes

# Example
# import random
# print(random.randint(1, 5))

# 2. User-Defined Modules:- User-Defined Module is a module created by the programmer/user.

# Example
# import calculator
# print(calculator.add(10, 5))
# print(calculator.sub(10, 5))


# 3. External (Third-Party) Modules: External Modules or Third-Party Modules are modules created by other developers, not built into Python.

# Popular Third-Party Modules
# numpy:- Numerical calculations
# pandas:- Data analysis
# matplotlib:- Data visualization
# requests:-  API and web requests
# flask:- Web development

# Example
# import numpy as np
# arr = np.array([1, 2, 3])
# print(arr)

# Package Modules:- package is a directory containing multiple modules, usually with an __init__.py file.

# Example
# mypackage/
# │
# ├── __init__.py
# ├── add.py
# ├── sub.py

# Why Packages are Used?
# Organize code
# Manage large projects
# Avoid name conflicts
# Improve readability

import mymodule
mymodule.say_hello('Module')
