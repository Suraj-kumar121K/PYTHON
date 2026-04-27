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
n = int(input("Enter a Number: "))
for i in range(n, 0, -1):
    for j in range(1, i + 1):
        print("*", end=" ")
    print()