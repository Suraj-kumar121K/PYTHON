from abs_class import Vehicle

class Bike(Vehicle):

    def __init__(self, n, color):
        self.color = color
        super().__init__(n)

    def start(self):
        print("Start with kick")

class Scooty(Vehicle):

    def __init__(self, n):
        super().__init__(n)

    def start(self):
        print("Self start")

class Car(Vehicle):

    def __init__(self, n, x):
        self.no_of_grade = 6
        super().__init__(n)

    def start(self):
        print("Start with key")