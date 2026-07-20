class Student:
    def __init__(self, name, roll_no, marks):
        self.name = name
        self.roll_no = roll_no
        self.marks = marks

    def display(self):
        print(f"Name: {self.name}, Roll No: {self.roll_no}, Marks: {self.marks}")


class StudentManagement:
    def __init__(self, filename):
        self.filename = filename
    # Add student data to file
    def add_student(self, student):
        with open(self.filename, "a") as file:
            file.write(
                f"{student.name},{student.roll_no},{student.marks}\n"
            )
        print("Student added successfully")

    # Display all students
    def view_students(self):
        try:
            with open(self.filename, "r") as file:
                print("\nStudent Records:")
                for line in file:
                    name, roll, marks = line.strip().split(",")
                    student = Student(name, roll, marks)
                    student.display()
        except FileNotFoundError:
            print("No records found")

    # Search student by roll number
    def search_student(self, roll_no):
        found = False
        try:
            with open(self.filename, "r") as file:
                for line in file:
                    name, roll, marks = line.strip().split(",")
                    if roll == roll_no:
                        print("\nStudent Found:")
                        student = Student(name, roll, marks)
                        student.display()
                        found = True
            if not found:
                print("Student not found")
        except FileNotFoundError:
            print("File does not exist")


# Main Program
system = StudentManagement("students.txt")
while True:
    print("\n--- Student Management System ---")
    print("1. Add Student")
    print("2. View Students")
    print("3. Search Student")
    print("4. Exit")
    
    choice = input("Enter choice: ")
    if choice == "1":
        name = input("Enter name: ")
        roll = input("Enter roll number: ")
        marks = input("Enter marks: ")

        student = Student(name, roll, marks)
        system.add_student(student)

    elif choice == "2":
        system.view_students()
    elif choice == "3":
        roll = input("Enter roll number to search: ")
        system.search_student(roll)
    elif choice == "4":
        print("Program closed")
        break
    else:
        print("Invalid choice")