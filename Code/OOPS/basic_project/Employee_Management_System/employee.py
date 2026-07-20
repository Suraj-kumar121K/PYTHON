from company import Company
class Employee(Company):

    def __init__(self, company_name, location, emp_id, name, salary):
        super().__init__(company_name, location)
        self.__emp_id = emp_id
        self.__name = name
        self.__salary = salary

    def show_details(self):
        self.show_method()
        print("Employee ID :", self.__emp_id)
        print("Name        :", self.__name)
        print("Salary      :", self.__salary)

    @property
    def name(self):
        return self.__name

    @property
    def salary(self):
        return self.__salary