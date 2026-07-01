# Calculator Project
"""print("welcome to calculater")
def add(a, b):
    return a + b

def sub(a, b):
    return a - b

def mul(a, b):
    return a * b

def div(a, b):
    return a / b

while True:
    print("\n1.Add")
    print("2.Subtract")
    print("3.Multiply")
    print("4.Divide")
    print("5.Exit")
    choice = input("Enter a Number: ")
    if choice == "5":
        print("Program End")
        break
    a = int(input("Enter a Number:- "))
    b = int(input("Enter a Number:- "))
    if choice == "1":
        print("Add Number: ", add(a, b))
    elif choice == "2":
        print("Subtraction: ",sub(a, b))
    if choice == "3":
        print("multiply: ", mul(a, b))
    if choice == "4":
        print("Divide: ", div(a, b))
    else:
        print("Invalid Choice")"""
        
# check even and Odd
"""def check(num):
    if num % 2 == 0:
        return "Even"
    else:
        return "Odd"

while True:
    num = int(input("Enter a Number: "))
    print(check(num))
    stop = input("Stop Yes/No: ")
    if stop == "Yes":
        print("Program Stopped")
        break"""
        
# 3. Table Generator

"""def table(num):
    for i in range(1, 11):
        print(f"{i} x {num} =", num * i)
while True:
    num = int(input("Enter a Number: "))
    print(table(num))
    
    choice = input("Enter Yes/No: ")
    if choice == "Yes":
        print("End Table")
        break
"""

# Student Result System
"""def student(total):
    if total >= 90:
        return "Gread A"
    elif total >= 60:
        return "Gread B"
    elif total >= 35:
        return "Gread C"
    else:
        return "Fail"
    
while True:
    num = int(input("Enter a Number: "))
    print(student(num))
    
    stop = input("Stop Yes/No: ")
    if stop == "Yes":
        print("stop Program")
        break
"""    

# 5. Simple ATM Machine
"""balance = int(input("Enter a Amount: "))
def Check_Balance():
    print("Blance ",balance)

def withdraw(Amount):
    global balance
    if Amount <= balance:
        balance -= Amount
        print("Withdraw Amount")
    else:
        print("Insufficient Balance")

while True:
    print("\n1.Check Balance")
    print("2.Withdraw")
    print("3.Exit")
    
    choice = input("Enter a Number: ")
    if choice == "1":
        Check_Balance()
        
    elif choice == "2":
        Amount = int(input("Enter a Amount:- "))
        withdraw(Amount)
        
    elif choice == "3":
        print("End Program")
        break
    else:
        print("Invalid Choice")
"""