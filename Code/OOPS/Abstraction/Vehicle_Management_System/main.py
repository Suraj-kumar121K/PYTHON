from vehicles import Bike, Car, ElectricCar
bike = Bike("Honda", "Shine", 80000)
car = Car("BMW", "X5", 7000000)
electric = ElectricCar("Tesla", "Model S", 9000000)


bike.start()
bike.stop()
bike.show_details()

print("----------------")

car.start()
car.stop()
car.show_details()

print("----------------")

electric.start()
electric.stop()
electric.show_details()