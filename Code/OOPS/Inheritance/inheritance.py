class Car:
    @staticmethod
    def start():
        print("car started..")
        
    @staticmethod
    def stop():
        print("car stopped.")
        
class ToyotaCar(Car):
    def __init__(self, name):
        self.name = name
    
# car1 = ToyotaCar("fortuner")
# print(car1.start())
# car1 = ToyotaCar("fortuner")

# Type of Inheritance
class Fortuner(ToyotaCar):
    def __init__(Self, type):
        Self.type = type
        
car1 = Fortuner("diesel")
car1.start()