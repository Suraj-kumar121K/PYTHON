from abc import ABC, abstractmethod
class Library(ABC):
    def __init__(self, library_name ,location):
        self.__library_name = library_name
        self.__location = location
    
    def show_library(self):
        print("Library Name: ", self.__library_name)
        print("Location: ", self.__location)
    
    @abstractmethod
    def add_book(self):
        pass
    
    @abstractmethod
    def remove_book(self):
        pass