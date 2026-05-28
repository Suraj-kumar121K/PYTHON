suraj = [12, 94.4, 66.4, 23, 56]
# print(suraj)
# print(type(suraj))
# print(suraj[0])
# print(suraj[1])

# Slicing
student = ["Suraj", 22, "Kumar", "Anish"]
# print(student)
# print(student[1:4])
# print(student[:2])

# List Methods
# Add Value in List
student.append("Monu")
# print(student)

student.insert(1, 10)
# print(student)

student.pop(1)
# print(student)

# Remove duplicate elements from a list
num = [1, 2, 3, 4, 5, 6, 6, 7,32, 32, 2, 4]
result = list(set(num))
# print(result)

# Reverse a list without using built-in functions
num = [1, 2, 3, 4, 5, 6, 7]
res = []
for it in num[::-1]:
    res.append(it)
# print(res)
    
# Merge two lists
num_1 = [1, 2, 3, 4, 5, 6, 6, 7,32, 32, 2, 4]
num_2 = [1, 2, 3, 4, 5, 6, 7]
result = num_1 + num_2
# print(result)

# Find the largest element in a list
"""num_1 = [1, 2, 3, 4, 5, 6, 7, 32]
lar = num_1[0]

for i in num_1:
    if i > lar:
        lar = i
print(lar)"""
        
# Append:- add last element
"""list = [10, 20, 30, 40]
list.append(100)
print(list)"""

# insert():- Adds element at specific position.
"""list = [10, 20, 30, 40]
list.insert(2, 100)
print(list)"""

# Extend():- Adds multiple elements from another list.
"""list = [10, 20, 30, 40]
list.extend([100, 101])
print(list)"""

#remove():- Removes first matching value.
# pop():- Removes element by index (default last).
# clear():- Removes all elements.
# index():-Returns position of element.
# count():- Counts occurrences.
# sort():- Sorts list ascending.
# reverse():- Reverses list.
# copy():- Creates shallow copy.

# Remove value 20 from a list.
"""list = [10, 20, 30, 40, 50]
list.remove(20)
print(list)"""

# Remove last element and print it.
"""list = [10, 20, 30, 40, 50]
add = list.pop()
print(add)"""

# Empty the list.
"""list = [10, 20, 30, 40, 50]
list.clear()
print(list)"""

# Find position of value 30.
"""list = [10, 20, 30, 40, 50]
add = list.index(20)
print(add)"""

# 1. Remove duplicates
"""list = [10, 20, 30, 40, 50, 20, 30]
res = []
for i in list:
    if i not in res:
        res.append(i)
print(res)"""


"""List = [10, 20, "suraj", 30.0]
print(List)
print("Length = ",len(List))"""

