from abc import ABC, abstractmethod

class Vehicle(ABC):
    def __init__(self, n):
        self.no_of_types = n

    @abstractmethod
    def start(self):
        pass

    def display(self):
        print("HII I am calling from Vehicle class")