--> What is Sets
A set is an unordered collection of unique elements.
®️ Duplicates are automatically removed.
®️ Elements are immutable, but the set itself is mutable.
s = {1, 2, 3, 4, 4, 2}
print(s)  

--> Properties of Set
    Unordered → no index.
    Mutable → can add or remove elements.
    No duplicate elements.
s1 = {1, 2, 3}
s2 = set([1, 2, 2, 3])
print(s2)  
s3 = set()

--> Set Methods
|      Method            |           Description                  |
| ---------------------- | -------------------------------------- |
| add()                  | Add element                            |
| remove()               | Remove element (error if not found)    |
| discard()              | Remove element (no error if not found) |
| pop()                  | Remove arbitrary element               |
| clear()                | Remove all elements                    |
| union()                | Combine sets                           |
| intersection()         | Common elements                        |
| difference()           | Elements in one but not the other      |
| symmetric_difference() | Elements in either set but not both    |
| issubset()             | Check if set is subset of another      |
| issuperset()           | Check if set is superset of another    |

-->Creating Sets
s1 = {1, 2, 3}
s2 = set([1, 2, 2, 3])
print(s2)  
s3 = set()

--> Basic Set Operations
--> Add elements
s = {1, 2, 3}
s.add(4)
print(s) }

--> Remove elements
s.remove(2)  
s.discard(5)  

--> Pop elements
s.pop()  

--> Clear all
s.clear()
print(s) 

--> Set Operations (Mathematical)
A = {1, 2, 3, 4}
B = {3, 4, 5, 6}
print(A | B) 
print(A & B)  
print(A - B) 
print(A ^ B)  

--> What is Dictionaries
    A dictionary is an unordered collection of key-value pairs.
        Keys must be unique and immutable.
        Values can be any data type.
        Dictionaries are mutable.

--> Creating a dictionary
    d = {"name": "Suraj", "age": 20}
    print(d["name"]) 

--> Dictionary Operations
    Access Elements
    print(d["age"])       
    print(d.get("name"))   

--> Add/Update
   d["city"] = "Delhi"   
   d["age"] = 21         

--> Remove
   d.pop("city")         
   d.popitem()            
   del d["age"]           
   d.clear()             

--> Keys, Values, Items
    print(d.keys())   
    print(d.values())  
    print(d.items())   

--> Dictionary Methods
|   Method  |         Description       |
| --------- | ------------------------- |
| get()     | Access value safely       |
| keys()    | Returns all keys          |
| values()  | Returns all values        |
| items()   | Returns key-value pairs   |
| update()  | Merge dictionaries        |
| pop()     | Remove specific key       |
| popitem() | Remove last inserted item |
| clear()   | Clear dictionary          |

--> Example
student = {"name": "Ankit", "marks": 85, "age": 18}
student["city"] = "Mumbai"
student["marks"] = 90
for key, value in student.items():
    print(key, ":", value)
