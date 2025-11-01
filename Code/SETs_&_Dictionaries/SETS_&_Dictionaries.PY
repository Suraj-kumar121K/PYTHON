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
