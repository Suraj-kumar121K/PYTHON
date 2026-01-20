# # Level 1 – Very Basic (1–15)
# # 1.Create an empty tuple in two different ways and print both.
# # Create a tuple with 5 names of your friends and print it.
# # What symbol is used to define a tuple? ( ) or [ ] or { } ?
# # Create a tuple with only one element: 100. Print it and its type.
# # Why do we need a comma when creating a single-element tuple? Try without comma and explain the result.
# # Create a tuple with mixed data types: int, str, float, bool. Print it.
# # Print the type of this: t = (5)
# # Print the type of this: t = (5,)
# # Create a tuple using the tuple() function from a list [10,20,30].
# # Check if tuples are ordered (try accessing by index).
# Check if tuples allow duplicate values. Create one with duplicates.
# Use len() to find how many items are in ( "a", "b", "c", "a", "d" )
# Access the first element of colors = ("red", "green", "blue")
# Access the last element of numbers = (1,2,3,4,5,6,7) using negative index.
# Try to change the second element of (10, 20, 30) to 99. What happens? Explain.

# Level 2 – Indexing, Slicing & Unpacking (16–28)
# Slice the tuple (0,1,2,3,4,5,6,7,8,9) to get elements from index 2 to 7.
# Get every second element from (10,20,30,40,50,60,70) using slicing.
# Reverse the tuple ( "python", "is", "fun" ) using slicing.
# Get a tuple with only odd-indexed elements from (1,2,3,4,5,6,7,8).
# Unpack this tuple into 3 variables: person = ("Amit", 25, "Delhi")
# Use * to collect remaining values while unpacking: t = (1,2,3,4,5,6)
# What will be printed?
# a, b, *c = (10, 20, 30, 40, 50)
# print(a, b, c)
# Create a tuple of 4 fruits and unpack it directly in a print statement.
# Check if "apple" is present in ("banana", "apple", "cherry") using in operator.
# Use not in to check if 100 is not present in (5,10,15,20).
# Find the index of first occurrence of 7 in (3,7,2,7,9,7).
# Count how many times "java" appears in ("python", "java", "java", "c++").
# Try to use tuple.index() when the item is not present. What error do you get?

# Level 3 – Operations, Conversion & Built-ins (29–40)
# Concatenate two tuples: t1 = (1,2) and t2 = (3,4)
# Repeat a tuple 3 times: ("hi",) * 3
# Create a tuple of numbers from 1 to 10 using range() and tuple().
# Convert this list to tuple: ["Monday", "Tuesday", "Wednesday"]
# Convert this tuple back to list: (10.5, 20.5, 30.5)
# Find the maximum value in (45, 78, 12, 99, 63)
# Find the minimum value in (-5, -1, -10, 0, -3)
# Use sum() on (10, 20, 30, 40)
# Sort the tuple (5, 1, 8, 3, 9, 2) (hint: you cannot sort directly — how to do it?)
# Check whether two tuples are equal: (1,2,3) == (1,2,3) and (1,2,3) == (3,2,1)
# Compare (10,20) > (5,30) — explain the result.
# Create a tuple containing another tuple (nested tuple): student name + marks tuple.

# Level 4 – Advanced / Tricky / Interview-style (41–50)
# Why can we modify a list inside a tuple? Demonstrate with code.
# Example: t = (1, [2,3], 4) → append 5 to the list and print t
# Can we put a tuple inside another tuple? Show example.
# Remove duplicates from (1,2,2,3,3,4,5,5) without using set (convert → list → unique → tuple)
# Create a tuple of squares of numbers 1 to 10 using generator expression + tuple()
# Use zip() to create a tuple of pairs from two lists: names and marks
# What is printed?
# a = (1,2,3)b = aa = a + (4,)
# print(b)
# Explain why this works but changing tuple directly does not:Pythont = ( [1,2], 3 )
# t[0].append(99)
# print(t)
# Create a one-liner to reverse a tuple without slicing.
# Check memory usage difference between large list vs large tuple (conceptual question — optional code).
# Write a function that takes any number of arguments and returns them as a tuple.