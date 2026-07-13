class Employee:
    def __init__(self, name, employee_id):
        self.name = name
        self.__employee_id = employee_id

    def print_detail(self):
        print("Employee ID :", self.__employee_id)

class Manager(Employee):
    def __init__(self, name, employee_id, department):
        super().__init__(name, employee_id)
        self.department = department

class ProjectManager(Manager):
    def __init__(self, name, employee_id, department, project_handled):
        super().__init__(name, employee_id, department)
        self.project_handled = project_handled

    def print_details(self):
        print("Name :", self.name)
        super().print_detail()
        print("Department :", self.department)
        print("Projects :", self.project_handled)

obj1 = ProjectManager(
    "Suraj",
    123,
    "IT",
    ["Training", "YouTube"]
)

obj1.print_details()