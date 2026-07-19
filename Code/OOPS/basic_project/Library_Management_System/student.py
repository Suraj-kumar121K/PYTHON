from person import Person

class Student(Person):
    def __init__(self, name, person_id, course):
        super().__init__(name, person_id)
        self.course = course

    def issue_book(self, book):
        print(f"{self.get_name()} issued {book}")

    def return_book(self, book):
        print(f"{self.get_name()} returned {book}")

    def show_person(self):
        super().show_person()
        print("Course :", self.course)