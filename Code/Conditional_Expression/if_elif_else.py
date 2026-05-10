# Even number 
"""n = int(input("Enter a Number: "))
if n % 2 == 0:
    print("Even")
else:
    print("odd")"""
    
# Multiple of 10
"""if n % 10 == 0:
    print("yes")
else:
    print("Not")"""

# Small or Large
"""if n >= 100:
    print("Large")
else:
    print("small")"""
    
# Username Check
"""username ="Sur7aj6@"
if username == "Sur7aj6@":
    print("Welcome")
else:
    print("Wrong User")"""
    
# Password Check
"""password = 1234
if password == 1234:
    print("Login Password")
else:
    print("Wrong Password")"""
    
# Find Minimum
"""a = int(input("a = "))
b = int(input("b = "))
if a < b:
    print(a)
else:
    print(b)"""
    
# Odd Positive
"""num = int(input("Enter a positive Number: "))
if num >= 0 and num % 2 != 0:
    print("positive odd")
else:
    print("No")"""
    
# Login System
"""user = "Suraj"
pws = 1234
if user == "Suraj" and pws == 1234:
    print("Login")
else:
    print("Invalid")""" 

# Check Empty String
"""str = ""
if str == "s":
    print("Empty")
else:
    print("Not Empty")"""
    
# Largest of Three Numbers
"""a = int(input("a = "))
b = int(input("b = "))
c = int(input("c = "))
if a > b and a > c:
    print(a)
elif b > c:
    print(b)
else:
    print(c)"""
    
# ATM Withdrawal System
pin = 1234
withdrawal = 3000
balance = 10000
if pin == 12345:
    if withdrawal <= balance:
        balance -= withdrawal
        print("Withdraw Success")
        print("Remaining:", balance)
    else:
        print("Insufficient Balance")
else:
    print("Wrong PIN")