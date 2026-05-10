"""ATM Machine Project
        Best project for conditions.
Features:
 Check balance
 Deposit
 Withdraw
 Pin verification""" 

balance = int(input("Enate a balance: "))
Withdraw = int(input("Enate a Amount: "))  
pin = 1234

user_pin = int(input("Enate pin: "))
if user_pin == pin:
    print("1. Check Balance")
    print("2. Withdraw")
    
    choice =  int(input("Enate choice: "))  
    if choice == 1:
        print("Blance =", balance)
    elif choice == 2:
        amount = int(input("Enter amount: "))
        if amount <= balance:
            balance -= amount
            print("Remaining Balance:", balance)
        else:
            print("Insufficient Balance")
else:
    print("Wrong PIN")
    
