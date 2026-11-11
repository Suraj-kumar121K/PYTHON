# ================================
# LIST + LOOP QUESTIONS (20)
# ================================
# 1. Print all elements of a list using loop.
"""List = [1, 2, 3, 4, 5, 6]
for i in List:
    print(i)"""

# 2. Print only even numbers from a list.
"""List = [1, 2, 3, 4, 5, 6]
for i in List:
    if i % 2 == 0:
        print(i)"""

# 3. Print only odd numbers from a list.
"""List = [1, 2, 3, 4, 5, 6]
for i in List:
    if i % 2 != 0:
        print(i)"""
        
# 4. Find sum of all elements in a list.
"""List = [1, 2, 3, 4, 5, 6]
total = 0
for i in List:
    total = total + i
print("Sum =", total)"""
    
# 5. Find maximum element in list.
"""List = [10, 43, 67, 85, 45, 64, 81, 44, 65, 98, 1, 24]
Max = List[0]
for num in List:
    if num > Max:
        Max = num
print("Maximum =", Max)"""
    

# 6. Find minimum element in list.
"""List = [10, 43, 67, 85, 45, 64, 81, 44, 65, 98, 1, 24]
Max = List[0]
for num in List:
    if num < Max:
        Max = num
print("Maximum =", Max)"""

# 7. Count total elements using loop.
"""List = [10, 43, 67, 85, 45, 64, 81, 44, 65, 98, 1, 24]
count = 0
for i in List:
    count = count + 1
print(count);"""
    
# 8. Print list in reverse order.
"""List = [10, 43, 67, 85, 45, 64, 81, 44, 65, 98, 1, 24]
reverse_List =  []
for num in range(len(List)-1,-1,-1):
    reverse_List.append(List[num])
print("Reverse List = ", reverse_List)"""

# 9. Count in list.
"""List = [10, 20, 10, 30, 10, 40, 40, 20]
freq = []
for i in List:
    if i in freq:
        freq[i] += 1
    else:
        freq[i] = 1
print(freq)"""

# 10. Create a new list with squares of elements.
"""a = [1, 2, 3, 4, 5]
rest = []
for i in a:
    rest.append(i**2)
print(rest)"""
    
# 11. Remove duplicates using loop.
"""a = [1, 2, 2, 3, 4, 4, 5]
rest = []
for i in a:
    if i not in rest:
        rest.append(i)
print(rest)"""

# 12. Print positive numbers only.
"""a = [1, -1, 2, 3, -4, 5, -8]
rest = []
for i in a:
    if i > 0:
        rest.append(i)
print(rest)"""

# 13. Print negative numbers only.
"""a = [1, -1, 2, 3, -4, 5, -8]
rest = []
for i in a:
    if i < 0:
        rest.append(i)
print(rest)"""

# 15. Merge two lists using loop.
a = [1, 2, 3, 4]
b = [5, 6, 7, 8]
rest = []
for i in range(len(a)):
    rest.append(a[i])

for i in range(len(b)):
    rest.append(b[i])
print(rest)