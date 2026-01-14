""" Read File
f = open("file.txt", "r")
# data = f.read()
# print(data)

line1 = f.readline()
print(line1)

line2 = f.readline()
print(line2)

# print(type(data))

f.close()
        """
        
        
"""WRITE FILE    
  
f = open("file.txt", "a") 

f.write("Then I'll move to ReactJS")

f.write("\n After that nodejs")

f.close()
        """
        
        
"""With Open      
with open("file.txt") as f:
    data = f.read()
    print(data) 
    
with open("file.txt", "w") as f:
        f.write("new data")
        """ 
        
        
"""Deleting File  
import os
os.remove("f.txt");  """    