class ATM:
    def __init__(self):
        # database (account: [pin, balance, transactions])
        self.users = {
            "1001": ["1234", 5000, []],
            "1002": ["4321", 3000, []]
        }
        self.current_user = None

    # LOGIN SYSTEM
    def login(self):
        acc = input("Enter Account Number: ")
        pin = input("Enter PIN: ")

        if acc in self.users and self.users[acc][0] == pin:
            self.current_user = acc
            print("Login Successful!")
            return True
        else:
            print("Invalid Credentials")
            return False

    # CHECK BALANCE
    def check_balance(self):
        print("Balance:", self.users[self.current_user][1])

    # DEPOSIT
    def deposit(self):
        amount = int(input("Enter amount to deposit: "))
        self.users[self.current_user][1] += amount
        self.users[self.current_user][2].append(f"+{amount} Deposited")
        print("Deposit Successful!")

    # WITHDRAW
    def withdraw(self):
        amount = int(input("Enter amount to withdraw: "))

        if amount <= self.users[self.current_user][1]:
            self.users[self.current_user][1] -= amount
            self.users[self.current_user][2].append(f"-{amount} Withdrawn")
            print("Withdrawal Successful!")
        else:
            print("Insufficient Balance")

    # MINI STATEMENT
    def mini_statement(self):
        print("\n--- Mini Statement ---")
        for t in self.users[self.current_user][2][-5:]:
            print(t)

    # MENU
    def menu(self):
        if not self.login():
            return

        while True:
            print("\n--- ATM MENU ---")
            print("1. Check Balance")
            print("2. Deposit")
            print("3. Withdraw")
            print("4. Mini Statement")
            print("5. Logout")

            choice = input("Enter choice: ")

            if choice == "1":
                self.check_balance()

            elif choice == "2":
                self.deposit()

            elif choice == "3":
                self.withdraw()

            elif choice == "4":
                self.mini_statement()

            elif choice == "5":
                print("Logged out successfully!")
                break

            else:
                print("Invalid Choice")


# RUN PROGRAM
atm = ATM()
atm.menu()