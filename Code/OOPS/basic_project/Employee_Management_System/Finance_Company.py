from company import Company
class FinanceCompany(Company):
    def __init__(self, company_name, location, service):
        super().__init__(company_name, location)
        self.service = service

    def hire_employee(self):
        print("Hiring Accountants, Financial Analysts, and Auditors.")

    def fire_employee(self):
        print("Employees are terminated according to company regulations.")

    def show_service(self):
        print("Service:", self.service)