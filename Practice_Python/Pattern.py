# Simple Triangle
"""n = int(input("Enter a Number: "))
for i in range(1, n+1):  # Outer loop = rows (kitni lines print hongi)
    for j in range(1, i + 1): # Inner loop = har row me kitne stars
        print("*", end=" ") # Same line me print (newline nahi lega)
    print() # Row khatam → next line pe jaane ke liye"""

# Method 2
"""n = int(input("Enter a Number: "))
for i in range(1, n + 1):
    for j in range(2 * i):
        print("*", end=" ")
    print()"""

# Reverse Triangle
"""n = int(input("Enter a Number: "))
for i in range(n, 0, -1):
    for j in range(1, i + 1):
        print("*", end=" ")
    print()"""

"""n = int(input("enter n "))
for i in range(n):
    for j in range(n):
        print("*", end="")
    print()"""
    
"""n = int(input("enter n "))
for i in range(1, n + 1):
    for j in range(n - i):
        print(" ", end=" ")
    for k in range(i):
        print("*", end=" ")
    print()"""
    
# Q:1   
"""n = int(input("Enter n "))
for i in range(1, n + 1):
    for j in range(n):
        print(i, end=" ")
    print()"""

# Q:2   
"""n = int(input("Enter n "))
for i in range(1, n + 1):
    for j in range(i):
        if i % 2 == 1:
            print("1", end=" ")
        else:
            print("0", end=" ")
    print()"""
    
"""n = int(input("Enter n "))
for i in range(1, n + 1):
    for j in range(i):
        print(i, end=" ")
    print()"""
    
# Q:3
"""n = int(input("Enter n:- "))
for i in range(1, n + 1):
    for j in range(1, n+1):
        print(j, end=" ")
    print()"""
    
# Q:4
"""n = int(input("Enter n:- "))
for i in range(1, n+1):
    for j in range(1, n + 1):
        if j % 2 == 1:
            print("1", end=" ")
        else:
            print("0", end=" ")
    print()"""

# Printing Stars in Hollow Diamond Shape
"""n = int(input("Enter n: "))
for i in range(1, n+1):
    for j in range(1, n*2):
        if j == n - i + 1 or j == n + i - 1:
            print("*", end="")
        else:
            print(" ", end="")
    print()
for i in range(n, 0, -1):
    for j in range(1, n*2):
        if j == n - i + 1 or j == n + i - 1:
            print("*", end="")
        else:
            print(" ", end="")
    print()"""
    
"""for i in range(7):
    for j in range(7):
        if i + j == 3 or j - i == 3 or i - j == 3 or i + j == 9:
            print("*", end=" ")
        else:
            print(end=" ")
    print()"""

"""n = n = int(input("Enter n: "))
for i in range(0, n):
    for j in range(0, n):
        if i == 0 or i == n - 1 or j == 0 or j == n - 1:
            print("*", end=" ")
        else:
            print(" ", end=" ")
    print()"""
    
"""n = int(input("Enter n: "))   
for i in range(1, n + 1):
    for j in range(1, i + 1):
        print(i, end=" ")
    print()"""

