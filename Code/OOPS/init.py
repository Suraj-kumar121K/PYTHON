""" class Student:
    school_Name = "ABC School"
    def __init__(self):
        print("Where a new object is created I am called automaticaly")

student_01 = Student()  # init method will be called      
student_02 = Student() """     

# Create class Student that takes 3 marks and has a method average()
class Student:
    def __init__(self, name, ListOfMarks):
        self.name = name
        self.ListOfMarks = ListOfMarks
    
    def average(self):
        sum = 0
        for Value in self.ListOfMarks:
            sum = sum + Value
            
        average = sum / 3
        print("Average is:", average)

student1 = Student("Suraj", [90, 98, 99])
student1.average()