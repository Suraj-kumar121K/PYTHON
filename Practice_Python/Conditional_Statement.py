# num = int(input("Enter a number "))
"""if num > 0:
    if num % 2 == 0:
        print("Positive Even")
    else:
        print("Positive odd")
else:
    print("Zero or Negative")"""
    
"""if num % 2 == 0 and num > 10:
    print("Even and Big Number")
elif num % 2 != 0 and num > 10:
    print("Odd and Big Number")
elif num % 2 == 0:
    print("Even but Small Number")
else:
    print("Odd and small Number")"""
    
"""if num > 100:
    print("Big Number")
elif num % 2 == 0:
    print("Even but small number")
else:
    print("Odd and Small Number")"""
    
"""if num > 40:
    print("Heatwave Alter")
elif num < 0:
    print("Freezing Alert")
else:
    print("Normal Weather")"""
    
"""age = int(input("Enter a age "))
income = int(input("Enter a income "))
credit_score = int(input("Enter a credit score "))
if age >= 21"""

# age = int(input("Enter age ")) 
# income = int(input("Enter income ")) 
# credit_score = int(input("Enter credit score "))
# if age >= 21 and income >= 45000 and credit_score >=700:
#     print("Eligible for Loan")
# else:
#     print("Not Eligible") 

# Leap year
"""year = int(input("Enter a year "))
if(year % 4 == 0 and year % 100 != 0) or (year % 400 == 0):
    print("Leap Year")
else:
    print("Not Leap Year")"""
"""1. Age & Income Check
Logical Operator practice Question
age = int(input("Enter a age "))
income = int(input("Enter a income "))
if age >= 18 and income >= 50000:
    print("Eligible for loan ")
else:
    print("Not eligible")"""

# 2. Temperature Alert 
"""temp = int(input("Enter a Temperature "))
if temp < 0 or temp >= 35:
    print("Extreme weather")
else:
    print("Normal weather")"""
    
#3. Number Range Check
"""user = int(input("Enter a number "))
if user >= 10 and user <= 50:
    print("Number is in range")
else:
    print("Number is out of range")"""
  
#4. Password Validation  
"""passw = input("Enter a password ")
if len(passw) >= 8 and '@' in passw:
    print("Strong password")
else:
    print("Weak password")"""

#5. Even or Odd & Positive Check
"""number = int(input("Enter a number "))
if number % 2 == 0 and number > 0:
    print("Positive Even")
elif number % 2 != 0 and number > 0:
    print("Positive Odd")
else:
    print("Negative Number or Zero")"""
    
#6. Voting & Citizenship Check
"""age = int(input("Enter a age "))
citizenship = input("Enter a citizenship ")
if age >= 18 and citizenship == "Yes":
    print("Eligible to vote")
else:
    print("Not eligible to vote")"""
    
#7. Discount Eligibility
"""amount = float(input("Enter purchase amount: "))
membership = input("Enter membership type (Gold/Silver/None): ")
Product = ["Gold", "Sliver", "Watch"]
if amount > 1000 or membership in Product:
    print("Discount Applied")
else:
    print("No Discount")"""
    
# Smart Number Analyzer
def Smart_Analyze(num):
    if num > 0:
        print("Positive")
    elif num < 0:
        print("Negative")
    else:
        print("Zero")
    if num % 2 == 0:
        print("Even")
    else:
        print("Odd")
    if num % 5 == 0:
        print("Multiple of 5")
    else:
        print("Not Multiple of 5")
        
# num = int(input("Enter a number: "))
# Smart_Analyze(num)

def result(marks):
    if marks >= 90:
        print('A+')
    elif marks >= 70:
        print('B+')
    elif marks >= 50:
        print('C')
    elif marks >= 33:
        print('D')
    else:
        print("Fail")
# marks = int(input("Enter marks: "))
# result(marks)