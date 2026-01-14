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

"""with open("practice.txt", "w") as f:
    f.write("Hi everyone\nwe are learning File I/O\n")
    f.write("using Java.\nI like programming in java,")"""
    
"""with open("practice.txt", "r") as f:
    data = f.read()
        
new_data = data.replace("Java", "Python") 
print(new_data)       

with open("practice.txt", "w") as f:
    f.write(new_data)"""
    
# Search if the word "learning" exists in the file or not.
def check_for_word():
    word = "learning"
    with open("practice.txt", "r") as f:
        data = f.read()
        if(word in data):
            print("Found")
        else:
            print("not found") 
# check_for_word()    

# WAF to find in which line of the file does the word "learning" occur first.
# Print -1 if word not found.           
def check_for_line():
    word = "learning"
    data = True
    line_no = 1
    with open("practice.txt", "r") as f:
        while data:
            data = f.readline()
            if(word in data):
                print(line_no)
            line_no += 1  