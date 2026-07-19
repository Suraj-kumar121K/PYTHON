# School Class
class School:

    # Constructor
    def __init__(self, name):

        # Instance Variable
        self.name = name

        # List of Student Objects
        self.students = []

        # List of Teacher Objects
        self.teachers = []

    # Object as Parameter
    def add_student(self, student):

        # Aggregation
        # Adding Student Object into School
        self.students.append(student)

    # Object as Parameter
    def add_teacher(self, teacher):

        # Aggregation
        self.teachers.append(teacher)

    # Display All Students
    def show_students(self):

        print("\nStudents")
        print("---------")

        # Loop through Object List
        for s in self.students:

            # Calling Parent Method
            s.display()

            # Runtime Polymorphism
            print("Role :", s.get_role())

            print("Roll :", s.roll)
            print()

    # Display All Teachers
    def show_teachers(self):

        print("\nTeachers")
        print("---------")

        # Loop through Object List
        for t in self.teachers:

            t.display()

            # Runtime Polymorphism
            print("Role :", t.get_role())

            print("Subject :", t.subject)
            print()