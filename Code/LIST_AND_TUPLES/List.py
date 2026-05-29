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

# Add an element in list vs tuple
"""list = [1, 2, 3]
list.append(4)
print("List =", list)"""

# Difference between append() and extend()
"""List = [1, 2, 3]
List.append([4, 5])
List.extend([6, 7])
print(List)"""

# 1. Create a list and print it
"""lst = [1, 2, 3]
print(lst)"""

# 2. Create a tuple and print it
"""lst = (1, 2, 3)
print(lst)"""

# 3. Access first and last element of a list
"""lst = [1, 2, 3, 4, 5, 6]
print(lst[0])
print(lst[-1])"""

# 4. Access first and last element of a tuple
"""lst = (1, 2, 3, 4, 5, 6)
print(lst[0])
print(lst[-1])"""

# 5. Find length of list
"""lst = [1, 2, 3, 4, 56, 6, 7, 8]
t = 0
for i in lst:
    t += 1
print(t)
print(len(lst))"""

# 6. Find length of tuple
"""lst = (1, 2, 3, 4, 5, 6, 7, 8)
t = 0
for i in lst:
    t += 1
print(t)"""

# 7. Append an element to a list
"""lst = [1, 2, 3, 4, 56, 6, 7, 8]
lst.append(56)
print(lst)"""

# 8. Insert an element at a specific position in list
"""lst = [1, 2, 3, 4, 56, 6, 7, 8]
lst.insert(0, 100)
print(lst)"""

# 9. Remove an element from list
"""lst = [1, 2, 3, 4, 56, 6, 7, 8]
lst.remove(56)
print(lst)"""

# 10. Pop last element from list
"""lst = [1, 2, 3, 4, 5, 6, 7, 8]
lst.pop()
print(lst)"""

# 11. Convert list to tuple
"""List = [1, 2, 3, 4]
a = tuple(List)
print(a)"""

# 12. Convert tuple to list
"""t = (1, 2, 3)
b = list[t]
print(b)"""

# 13. Reverse a list
"""lst = [1, 2, 3]
lst.reverse()
print(lst)"""

# 14. Reverse a tuple
"""t = (1, 2, 3)
d = t[::-1]
print(d)"""

# 15. Sort a list in ascending order
"""lst = [1, 3, 2]
lst.sort()
print(lst)"""

# 16. Sort a list in descending order
"""lst = [1, 2, 3]
lst.sort(reverse=True)
print(lst)"""

# 17. Remove duplicates from list
"""lst = [1, 2, 2, 3]
# result = list(set(lst))
# print(result)
t = []
for i in lst:
    if i not in t:
        t.append(i)
print(t)"""

# 18. Count frequency of elements in list

# 19. Find sum of all elements in list
"""List = [10, 20, 40, 70]
total = 0
for i in List:
    total += i
print(total)"""

# 20. Multiply all elements in list
"""List = [1, 2, 3, 4]
t = 1
for i in List:
    t *= i
print(t)"""

# 21. Swap first and last element in list
"""List = [1, 2, 3, 4] # [4, 2, 3, 1]
List = [1, 2, 3, 4] # [1, 3, 2, 4]
temp = List[1]
List[1] = List[-2]
List[-2] = temp
print(List)"""

# Swap number
"""List = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10] # Swap = [1, 4, 3, 2, 7,8, 5, 6, 9, 10]
temp = List[1] 
List[1] = List[-7]
List[-7] = temp
temp = List[4] 
List[4] = List[-4]
List[-4] = temp
temp = List[5] 
List[5] = List[-3]
List[-3] = temp
print(List)"""


# 22. Find second largest number in list
List = [1, 2, 3, 4, 5, 6, 7]
# second largest 
"""largest = List[0]
Second = List[0]
for i in List:
    if i > largest:
        Second = largest
        largest = i 
print(Second)"""
    
# Largest 
"""largest = List[0]
for i in List:
    if i > largest:
        largest = i
print(largest)"""

# 23. Find second smallest number in list
"""smaller = List[0]
for i in List:
    if i < smaller:
        smailler = i
print(smaller)"""

# 24. Merge two lists


# 25. Merge two tuples

# 26. Find common elements in two lists

# 27. Find unique elements in list

# 28. Convert list of tuples into list of lists

# 29. Convert list of lists into list

# 30. Find index of element in list

# 31. Find index of element in tuple

# 32. Slice a list (first 5 elements)

# 1. Remove all even numbers from list
# 1. Remove all odd numbers from list
# 1. Check if list is sorted
# 1. Find all duplicates in list
# 1. Flatten a nested list
# 1. Find largest element without max()
# 1. Find smallest element without min()
# 1. Rotate list by k positions
# 1. Split list into even and odd lists
# 1. Convert tuple of tuples into dictionary
# 1. Count occurrences using dictionary
# 1. Find most frequent element in list
# 1. Check if two lists are identical
# 1. Create tuple with single elements
# 1. Demonstrate why tuple is immutable 



