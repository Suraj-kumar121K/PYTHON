# 1. Reverse string without slicing
"""
stri = "Suraj"
rev=""
for i in stri:
    rev = i + rev
print(rev)
"""

# 2. Count frequency of elements
"""
list = [1, 2, 3, 4, 5, 6, 6]
count = {}
for i in list:
    count[i] = count.get(i,0)+1
print(count)
"""

# 3. Find duplicate values
"""
list = [1, 2, 3, 2, 3, 5, 6, 5,]
for i in list:
    if list.count(i) > 1:
        print(i)
"""

# 4. Remove duplicates without set
"""
list = [1,2,2,3,4,4]
new = []
for i in list:
    if i not in new:
        new.append(i)
print(new)
"""

# 5. Find second largest number
"""
list = [10, 20 , 30, 40]
largest = list[0]
second = list[0]
for i in list:
    if i > largest:
        second = largest
        largest = i
print(second)
"""

# 21. Matrix addition
"""
a=[[1,2],[3,4]]
b=[[5,6],[7,8]]

for i in range(2):
    for j in range(2):
        print(a[i][j]+b[i][j])
"""
