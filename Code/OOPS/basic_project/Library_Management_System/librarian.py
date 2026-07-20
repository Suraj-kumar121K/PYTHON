from person import Person
class Librarian(Person):
    def __init__(self, name, person_id, salary):
        super().__init__(name, person_id)
        self.salary = salary

    def manage_books(self):
        print(f"{self.get_name()} is managing books.")

    def show_person(self):
        super().show_person()
        print("Salary :", self.salary)