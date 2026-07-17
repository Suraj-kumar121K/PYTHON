from abstract_vehicle import Vehicle

# Child Class 1
class Bike(Vehicle):

    def start(self):
        print(self.name, "starts with Kick")


# Child Class 2
class Car(Vehicle):

    def start(self):
        print(self.name, "starts with Key")