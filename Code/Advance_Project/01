# Bank Management System (Advanced Mini Project)
"""Concepts Used:
function
while loop
list
dictionary
condition"""

accounts = []
def create_account():
    name = input("Enter Name: ")
    balance = int(input("Enter Balance: "))
    account = {
        "name": name,
        "balance": balance
    }
    accounts.append(account)
    print("Account Created")

def view_accounts():
    if len(accounts) == 0:
        print("No Accounts Found")
    else:
        for acc in accounts:
            print("\nName:", acc["name"])
            print("Balance:", acc["balance"])

def deposit():
    name = input("Enter Name: ")
    amount = int(input("Enter Deposit Amount: "))
    for acc in accounts:
        if acc["name"] == name:
            acc["balance"] += amount
            print("Deposit Success")
            return
    print("Account Not Found")

def withdraw():
    name = input("Enter Name: ")
    amount = int(input("Enter Withdraw Amount: "))

    for acc in accounts:
        if acc["name"] == name:
            if amount <= acc["balance"]:
                acc["balance"] -= amount
                print("Withdraw Success")
            else:
                print("Insufficient Balance")
            return
    print("Account Not Found")

while True:
    print("\n--- BANK SYSTEM ---")
    print("1. Create Account")
    print("2. View Accounts")
    print("3. Deposit")
    print("4. Withdraw")
    print("5. Exit")
    choice = input("Enter Choice: ")
    if choice == "1":
        create_account()
    elif choice == "2":
        view_accounts()
    elif choice == "3":
        deposit()
    elif choice == "4":
        withdraw()
    elif choice == "5":
        print("Program Closed")
        break
    else:
        print("Invalid Choice")