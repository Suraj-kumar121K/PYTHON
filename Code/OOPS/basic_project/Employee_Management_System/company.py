from abc import ABC, abstractmethod
class Company(ABC):
    def __init__(self, company_name, location):
        self.__company_name = company_name
        self.__location = location
        
    def show_method(self):
        print("Company Name", self.__company_name)
        print("Company Name", self.__location)
    
    @abstractmethod
    def hire_employee(self):
        pass
    
    @abstractmethod
    def fire_employee(self):
        pass
      
 