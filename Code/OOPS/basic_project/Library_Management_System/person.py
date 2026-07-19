class Person:
    def __init__(self, person_id, name):
        self.__person_id = person_id
        self.__name = name
    
    def get_id(self):
        return self.__person_id
    
    def get_name(self):
        return self.__name
    
    def show_person(self):
       print("Person ID :", self.__person_id)
       print("Name :", self.__name)
        