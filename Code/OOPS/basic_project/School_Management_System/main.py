from school import School
from teacher import Teacher
from student import Student

school = School("ABC Public School", "Delhi")

teacher1 = Teacher(101, "Rahul", "Mathematics")
teacher2 = Teacher(102, "Priya", "Science")

student1 = Student(1, "Aman", "10th")
student2 = Student(2, "Neha", "9th")

school.add_teacher(teacher1)
school.add_teacher(teacher2)

school.add_student(student1)
school.add_student(student2)

school.display()