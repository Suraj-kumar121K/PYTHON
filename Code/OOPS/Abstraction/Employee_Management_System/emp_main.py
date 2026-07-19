from employee_details import *
# -------- Runtime Polymorphism --------
employees = [
    Developer(101, "Suraj", 50000),
    Data_Analyst(102,"Rahul", 45000),
    Manager(103,"Priya", 70000)
]

for emp in employees:
    emp.show_details()
    emp.work()
    emp.calculate_bonus()
    print("-" * 40)