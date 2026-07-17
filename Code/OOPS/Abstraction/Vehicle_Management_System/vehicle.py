"""
File 1: vehicle.py
Create an abstract class Vehicle.

Properties:
   1. name
   2. model
   3. price

Constructor use karo.

Abstract methods:
    1. start()
    2. stop()
    3. show_details()

File 2: vehicles.py
Create child classes:
1. Bike

Methods:
    1. start()
    2. stop()
    3. show_details()
2. Car

Methods:
    1. start()
    2. stop()
    3. show_details()
    
3. ElectricCar

Methods:
    start()
    stop()
    show_details()
"""
from abc import ABC, abstractmethod
class Vehiclee(ABC):
    def __init__(self, name, model, price):
        self.name = name
        self.model = model
        self.price = price
    @ abstractmethod
    def start(self):
        pass
    
    @ abstractmethod
    def stop(self):
        pass
    
    @ abstractmethod
    def show_details(self):
        pass