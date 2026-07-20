from company import Company
class ITCompany(Company):
    def __init__(self, comapny_name, location, technologies):
        super().__init__(comapny_name, location)
        self.technologies = technologies
        
    def hire_employee(self):
        print("Hiring Software Engineers, Python Developers, and Data Analysts.")

    def fire_employee(self):
        print("Removing employees based on performance or company policy.")

    def show_technology(self):
        print("Technologies Used:", ", ".join(self.technologies))
        
 
        
        