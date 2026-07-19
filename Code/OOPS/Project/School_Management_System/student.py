from person import Person

# Student inherits Person
class Student(Person):

    # Constructor
    def __init__(self, name, age, roll):

        # Calling Parent Constructor
        # Constructor Chaining
        super().__init__(name, age)

        # Student's own data member
        self.roll = roll

    # Method Overriding
    # Implementing abstract method
    def get_role(self):
        return "Student"

    # Student's own method
    def study(self):
        print(f"{self.get_name()} is studying.")