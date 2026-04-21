# public attribute used
class student:
    def __init__(self, name):
        self.name = name
        
# s1 = student("Suraj")
# print(s1.name)
# # del keyword used
# del s1.name
# print(s1.name)

#Private Attribute

class Account:
    def __init__(self, acc_no, acc_pass):
        self.acc_no = acc_no
        self.__acc_pass = acc_pass
        
    def reset_pass(self):
        print(self.__acc_pass)
            
# acc1 = Account("1234", "abcd")
# print(acc1.acc_no)      
# print(acc1.reset_pass)      


class Person:
    __name = "suraj"    
    def __hello(self):
        print("Hello person!")
        
    def welcome(self):
        self.__hello()

p1 = Person()
print(p1.welcome())