"""
Question 1: Vehicle System
File 1: abstract_vehicle.py

Create abstract class Vehicle
Abstract method: start()

File 2: vehicles.py
Create Bike and Car classes
Inherit Vehicle
Implement start()

File 3: main.py
Create objects and call methods
"""
from abc import ABC, abstractmethod

# Abstract Class
class Vehicle(ABC):
    # Constructor
    def __init__(self, name):
        self.name = name
    
    # Abstract Method
    @abstractmethod
    def start(self):
        pass
    