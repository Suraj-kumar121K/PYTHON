from school import School
from student import Student
from teacher import Teacher

school = School("ABC School")

s1 = Student("Rahul", 18, 101)
s2 = Student("Amit", 19, 102)

t1 = Teacher("Sharma", 40, "Python")
t2 = Teacher("Anita", 35, "SQL")

school.add_student(s1)
school.add_student(s2)

school.add_teacher(t1)
school.add_teacher(t2)

school.show_students()

school.show_teachers()

s1.study()
t1.teach()