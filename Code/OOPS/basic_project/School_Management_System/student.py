from person import Person

class Student(Person):

    def __init__(self, id, name, class_name):
        super().__init__(id, name)
        self.class_name = class_name

    def work(self):
        print(f"{self.name} is studying in {self.class_name}.")

    def display(self):
        super().display()
        print(f"Class : {self.class_name}")
        