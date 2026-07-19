from person import Person

# Teacher inherits Person
class Teacher(Person):

    # Constructor
    def __init__(self, name, age, subject):

        # Calling Parent Constructor
        super().__init__(name, age)

        # Teacher's own variable
        self.subject = subject

    # Method Overriding
    def get_role(self):
        return "Teacher"

    # Teacher's own method
    def teach(self):
        print(f"{self.get_name()} is teaching {self.subject}.")