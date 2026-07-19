from abc import ABC, abstractmethod

# Abstract Class
class Person(ABC):

    # Constructor
    def __init__(self, name, age):

        # Encapsulation (Private Variables)
        self.__name = name
        self.__age = age

    # Getter Method (Encapsulation)
    def get_name(self):
        return self.__name

    # Getter Method (Encapsulation)
    def get_age(self):
        return self.__age

    # Abstract Method
    # Child class must implement this method.
    @abstractmethod
    def get_role(self):
        pass

    # Normal Method
    def display(self):
        print(f"Name : {self.__name}")
        print(f"Age  : {self.__age}")