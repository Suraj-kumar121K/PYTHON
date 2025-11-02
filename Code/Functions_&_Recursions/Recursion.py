--> 🧠 What is Recursion in Python?
Recursion means a function calling itself again and again until a condition is met.

--> Syntax:
def function_name():
    # some code
    function_name()   # function calls itself

--> Example 
1: Print numbers using recursion
def show(n):
    if n == 0:        
        return
    print(n)
    show(n - 1)       
show(5)
