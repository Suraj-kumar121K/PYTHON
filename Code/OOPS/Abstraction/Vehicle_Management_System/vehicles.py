from vehicle import Vehiclee
class Bike(Vehiclee):
    def __init__(self, name, model, price):
        super().__init__(name, model, price)
    
    def start(self):
        print(self.name, "starts with Kick")
        
    def stop(self):
        print(self.name, "stopped")
        
    def show_details(self):
        print("Name:", self.name)
        print("Model:", self.model)
        print("Price:", self.price)
class Car(Vehiclee):
    def __init__(self, name, model, price):
        super().__init__(name, model, price)

    def start(self):
        print(self.name, "starts with Key")

    def stop(self):
        print(self.name, "stopped")

    def show_details(self):
        print("Name:", self.name)
        print("Model:", self.model)
        print("Price:", self.price)

class ElectricCar(Vehiclee):
    def __init__(self, name, model, price):
        super().__init__(name, model, price)

    def start(self):
        print(self.name, "starts with Battery")

    def stop(self):
        print(self.name, "stopped")

    def show_details(self):
        print("Name:", self.name)
        print("Model:", self.model)
        print("Price:", self.price)