# Basic Level Questions (English)
# 1. Create an empty list my_list and print it.
my_list = []
# print(my_list)

# 2. Create a list numbers = [5, 10, 15, 20, 25] and print only the first and last elements.
numbers = [5, 10, 15, 20, 25]
# print(numbers[0])
# print(numbers[-1])


# 3. In the list fruits = ["apple", "banana", "cherry"], add "mango" at the end using append.
fruits = ["apple", "banana", "cherry"]
fruits.append("mango")
# print(fruits)

# 4. Remove the second element ("green") from the list colors = ["red", "green", "blue", "yellow"].
colors = ["red", "green", "blue", "yellow"]
colors.remove("green")
# print(colors)

""" 5. Reverse the list [1, 2, 3, 4, 5] and print it using:
 slicing
 reverse() method 
"""
list = [1, 2, 3, 4, 5]
# Slicing
# print(list[::-1]) 

#  reverse() method 
list.reverse()
# print(list)


# 6. Write code to find how many elements are in the list marks = [78, 92, 65, 88, 45, 99].
marks = [78, 92, 65, 88, 45, 99]
# print(len(marks))

# 7. Insert "Priya" at index 1 in the list names = ["Amit", "Riya", "Sohan"].
names = ["Amit", "Riya", "Sohan"]
names.insert(1, "Priya")
# print(names)

# 8.  Count how many times 20 appears in the list [10, 20, 30, 20, 40] and print it.
list = [10, 20, 30, 20, 40]
# print(list.count(20))

# 🔹 Medium Level Questions (English)
# 9. Using list comprehension, create a list of even numbers from 1 to 20.
even_number = [i for i in range(1, 21)
               if i % 2 == 0]
# print(even_number)

# 10. Multiply each value of the list [1, 2, 3, 4, 5] by 10 and create a new list using list comprehension.
list = [1, 2, 3, 4, 5]
result = [i * 10 for i in list]
# print(result)

""" Sort the list [7, 2, 9, 1, 5, 3] in ascending order using:
sort()
sorted()"""
list = [7, 2, 9, 1, 5, 3]
# sort()
list.sort()
# print(list)

# sorted()
# print(sorted(list))

# 11. Merge two lists list1 = [1, 2, 3] and list2 = [4, 5, 6] into one list using three different methods.
list1 = [1, 2, 3]
list2 = [4, 5, 6]
# 1st Methods
# print(list1 + list2)

# 2nd Methods
list1.extend(list2)
# print(list1)

# 3rd Methods
merged = [*list1, *list2]
# print(merged)

""" 12. From the nested list
matrix = [[1, 2, 3], [4, 5, 6], [7, 8, 9]],
print the second row."""

# 13. From the same matrix, print the second column (2, 5, 8) using a loop.

# 14. Print the maximum and minimum values from the list [10, 5, 8, 12, 3] using max() and min().

# 15. Remove duplicate values from the list [1, 2, 2, 3, 4, 4, 5] without using set().

# 🔹 Advanced / Tricky Questions (English)
# Iterate through the list [1, 2, 3, 4, 5] and print each element along with its index using enumerate().

# Zip two lists a = [1, 2, 3] and b = [10, 20, 30], create pairs, and print them.

# Using list comprehension, create a list of numbers from 1 to 100 that are divisible by both 3 and 5.

# From the list words = ["hello", "world", "python", "code"], create a new list containing only words with exactly 5 letters.

# Write three ways to copy a list and show why a change in a shallow copy affects the original list.

# Print all elements of a list using a while loop (with an index variable).

# Sort the list [4, 2, 8, 1, 5] in descending order and print it.

""" Remove all negative numbers from the list
nums = [1, -2, 3, -4, 5, -6]."""