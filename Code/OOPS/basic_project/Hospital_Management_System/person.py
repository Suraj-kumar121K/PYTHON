from abc import ABC, abstractmethod
class Person(ABC):
    def __init__(self, name, age):
        self.__name = name
        self.__age = age
    
    def show_details(self):
        print("Name :", self.__name)
        print("Age  :", self.__age)
        
    @abstractmethod
    def work(self):
        pass