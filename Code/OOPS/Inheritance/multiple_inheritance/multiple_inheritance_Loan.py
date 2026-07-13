class Account:
    def __init__(self, account_number, balance):
        self.account_number = account_number
        self.balance = balance
    def deposit(self, amount):
        self.balance += amount
        print(f"Deposited {amount}. New balance is {self.balance}")
class InterestBearing:
    def calculate_interest(self, rate):
        interest = self.balance * rate
        print(f"Calculated interest is {interest}.")
        return interest
class LoanAccount:
    def __init__(self, loan_amount, interest_rate):
        self.loan_amount = loan_amount
        self.interest_rate = interest_rate
    def calculate_loan_interest(self):
        interest = self.loan_amount * self.interest_rate
        print(f"Loan interest is {interest}.")
        return interest
class MortgageAccount(Account, InterestBearing, LoanAccount):
    def __init__(self, account_number, balance, loan_amount, interest_rate):
        Account.__init__(self, account_number, balance)
        LoanAccount.__init__(self, loan_amount, interest_rate)
    def show_account_details(self):
        print(f"Account Number : {self.account_number}")
        print(f"Balance        : {self.balance}")
        print(f"Loan Amount    : {self.loan_amount}")
        print(f"Interest Rate  : {self.interest_rate}")
Mortgage_Account = MortgageAccount(1001, 5000, 20000, 0.05)
Mortgage_Account.deposit(1000)
Mortgage_Account.calculate_interest(0.03)
Mortgage_Account.calculate_loan_interest()
Mortgage_Account.show_account_details()