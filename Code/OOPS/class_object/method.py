# simple method
class Student:
    def show(self):
        print("Hello world")
s1 = Student()
# s1.show()

# company name
class Mobile:
    def show(self):
        print("Samsung")

s1 = Mobile()
# s1.show()

# Fan ON/OFF
class Fan:
    def on(self):
        print("Fan ON")
    def off(self):
        print("Fan OFF")
f1 = Fan()
# f1.on()
# f1.off()

# Student Name
class Student:
    def show(self, name):
        print("Student Name ", name)
s1 = Student()
# s1.show("Suraj")

# Addition
class Addition:
    def add(xyz, a, b):
        return a + b
s1 = Addition()
print(s1.add(10, 20))
        