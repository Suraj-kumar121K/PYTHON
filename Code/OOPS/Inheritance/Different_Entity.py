class Person:
    def __init__(self, name, email):
        self.__name = name
        self.__email = email
    def print_basic_details(self):
        print("Name is: ", self.__name) 
        print("Email is: ", self.__email)
     
class Employee:
    def __init__(self, emp_id, emp_dep):
        self.emp_id = emp_id
        self.emp_dep = emp_dep
    def print_emp_data(self):
        print("Emp ID: ", self.emp_id)
        print("Department: ", self.emp_dep)
        
class Manager(Person, Employee):
    def __init__(self, name, email, emp_id, emp_dep, team_size):
        Person.__init__(self, name, email)
        Employee.__init__(self, emp_id, emp_dep)
        self.team_size = team_size
    
    def print_data(self):
        Person.print_basic_details(self)
        Employee.print_emp_data(self)
        print("Team Size: ", self.team_size)
        
m1 = Manager("Suraj","kumarsuraj2031k@gmail.com",123,"IT",10)
m1.print_data()
            