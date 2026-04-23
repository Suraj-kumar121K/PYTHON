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
num_1 = [1, 2, 3, 4, 5, 6, 7, 32]
lar = num_1[0]

for i in num_1:
    if i > lar:
        lar = i
print(lar)
        
# Find the second largest number in a list
# Sort a list in ascending order
# Extract even numbers into a separate list
# Count odd numbers in a list
# Count frequency of an element in a list
# Find the sum of all elements in a list
# Remove negative numbers from a list
# Rotate a list (left/right rotation)
# Flatten a nested list
# Find common elements between two lists
# Divide a list into chunks