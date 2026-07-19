from person import Person

class Teacher(Person):

    def __init__(self, id, name, subject):
        super().__init__(id, name)
        self.subject = subject

    def work(self):
        print(f"{self.name} is teaching {self.subject}.")

    def display(self):
        super().display()
        print(f"Subject : {self.subject}")