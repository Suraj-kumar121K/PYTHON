class Account:
    pass
class InteresBearing:
    pass
class LoanAccount:
    pass
class MortgageAccount(Account, InteresBearing, LoanAccount):
    pass