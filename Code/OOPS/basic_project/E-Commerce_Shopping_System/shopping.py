from abc import ABC, abstractmethod
class Shopping(ABC):
    def __init__(self, store_name, location):
        self.store_name = store_name
        self.location = location
    
    def show_store(self):
        print("Store Name :", self.store_name)
        print("Store Location:", self.location)
    
    @abstractmethod
    def add_product(self):
        pass
    
    @abstractmethod
    def remove_product(self):
        pass