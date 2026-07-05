class Employee:
    def __init__(self, first, last, pay):
        self.first = first
        self.last = last
        self.pay = pay
        self.email = first + '.' + last + '@company.com'
        

emp_1 = Employee()
emp_2 = Employee()
print(emp_1)
print(emp_2)

emp_1.first = 'Suraj'
emp_1.last = 'Kumar'
emp_1.email = "surajkumar2031l@gmaol.com"
emp_1.pay = 50000

emp_2.first = 'Kumar'
emp_2.last = 'Suraj'
emp_2.email = "surajkumar2031l@gmaol.com"
emp_2.pay = 40000

print(emp_1.email)
print(emp_1.pay)