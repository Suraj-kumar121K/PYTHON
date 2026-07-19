"""
Employee Management System

Create an abstract class Employee.
Constructor:
    name
    id
    salary

Abstract Methods:
    work()
    calculate_bonus()
    show_details()

Child Classes:
    Developer
    Data Analyst
    Manager
"""
from abc import ABC,abstractmethod
class Employee(ABC):
    def __init__(self, id, name, salary):
        self.id = id
        self.name = name
        self.salary = salary
        
    @abstractmethod
    def work(self):
        pass
        
    @abstractmethod
    def calculate_bonus(self):
        pass
        
    @abstractmethod
    def show_details(self):
        pass
        
        