from abc import ABC, abstractmethod
class Person(ABC):
    def __init__(self, id, name):
        self.id = id
        self.name = name
    def display(self):
        print(f"ID : {self.id}")
        print(f"Name : {self.name}")

    @abstractmethod
    def work(self):
        pass