from employee import Employee
class Developer(Employee):
    def work(self):
        print(f"{self.name} is writing Python code.")
    
    def calculate_bonus(self):
        bonus = self.salary * 0.15
        print(f"Bonus = ₹{bonus}")

    def show_details(self):
        print("\n------ Developer Details ------")
        print("ID     :", self.id)
        print("Name   :", self.name)
        print("Salary :", self.salary)
        
class Data_Analyst(Employee):
    def work(self):
        print(f"{self.name} is analyzing data.")
    
    def calculate_bonus(self):
        bonus = self.salary * 0.25
        print(f"Bonus = ₹{bonus}")

    def show_details(self):
        print("\n------ Analyzing Data Details ------")
        print("ID     :", self.id)
        print("Name   :", self.name)
        print("Salary :", self.salary)
   
class Manager(Employee):
    def work(self):
        print(f"{self.name}  is managing the team.")
    
    def calculate_bonus(self):
        bonus = self.salary * 0.25
        print(f"Bonus = ₹{bonus}")

    def show_details(self):
        print("\n------ Manager Details ------")
        print("ID     :", self.id)
        print("Name   :", self.name)
        print("Salary :", self.salary)     
        