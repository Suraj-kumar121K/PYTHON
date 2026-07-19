class School:

    def __init__(self, school_name, address):
        self.school_name = school_name
        self.address = address
        self.teachers = []
        self.students = []

    def add_teacher(self, teacher):
        self.teachers.append(teacher)

    def add_student(self, student):
        self.students.append(student)

    def display(self):

        print("\n========== SCHOOL ==========")
        print("School :", self.school_name)
        print("Address :", self.address)

        print("\n------ Teachers ------")
        for teacher in self.teachers:
            teacher.display()
            teacher.work()
            print()

        print("------ Students ------")
        for student in self.students:
            student.display()
            student.work()
            print()