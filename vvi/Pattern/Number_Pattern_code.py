# ⭐ Level 1 — Number Patterns
# 1. Number Diamond Pattern
"""
        1
      1 2
    1 2 3
  1 2 3 4
1 2 3 4 5
  1 2 3 4
    1 2 3
      1 2
        1
"""

# 2. Repeated Number Square Pattern
"""
1 1 1 1 1
2 2 2 2 2
3 3 3 3 3
4 4 4 4 4
5 5 5 5 5
"""
def Square_Pattern(num):
  for i in range(1, num + 1):
    for j in range(1, num + 1):
      print(i, end=" ")
    print()
# num = int(input("Enter the Num of Rows: "))
# Square_Pattern(num)

# 3. Alternating 1-0 Square Pattern
"""
1 1 1 1 1
0 0 0 0 0
1 1 1 1 1
0 0 0 0 0
1 1 1 1 1
"""
def Square_Pattern(num):
  for i in range(1, num + 1):
    for j in range(1, num + 1):
      if i % 2 != 0:
        print("1", end=" ")
      else:
        print("0", end=" ")
    print()
# num = int(input("Enter the Num of Rows: "))
# Square_Pattern(num)

# 4. Sequential Number Square Pattern
"""
1 2 3 4 5
1 2 3 4 5
1 2 3 4 5
1 2 3 4 5
1 2 3 4 5
"""
def Square_Pattern(num):
  for i in range(1, num + 1):
    for j in range(1, num + 1):
        print(j, end=" ")
    print()
# num = int(input("Enter the Num of Rows: "))
# Square_Pattern(num)

# 5. Increasing Number Triangle
"""
1
1 2
1 2 3
1 2 3 4
1 2 3 4 5
"""
def increasing_Triangle(num):
  for i in range(1, num + 1):
    for j in range(1, i + 1):
      print(j, end=" ")
    print()
# num = int(input("Enter the Num of Rows: "))
# increasing_Triangle(num)
    
# 6. Alternating Number Triangle
"""
1
1 0
1 0 1
1 0 1 0
1 0 1 0 1
"""
def Alternating_Triangle(num):
  for i in range(1, num + 1):
    for j in range(1, i + 1):
      if j % 2 != 0:
        print("1", end=" ")
      else:
        print("0", end=" ")
    print()
# num = int(input("Enter the Num of Rows: "))
# Alternating_Triangle(num)

# 7. Decreasing Repeated Number Triangle
"""
5
4 4
3 3 3
2 2 2 2
1 1 1 1 1
"""
def Decreasing_Repeated_Triangle(num):
  for i in range(num, 0, -1):
    for j in range(num - i + 1):
      print(i, end=" ")
    print()
# num = int(input("Enter the Num of Rows: "))
# Decreasing_Repeated_Triangle(num)

# ⭐ Level 2 — Number Pyramid
# 8. Centered Number Pyramid
"""
        1
      1 2 3
    1 2 3 4 5
  1 2 3 4 5 6 7
1 2 3 4 5 6 7 8 9
"""
def Number_Pyramid(num):
  for i in range(1, num + 1):
    for j in range(num - i):
      print(" ", end=" ")
    for j in range(2 * i - 1):
      print(j + 1, end=" ")
    print()
# num = int(input("Enter the Num of Rows: "))
# Number_Pyramid(num)
"""
        1 
      1 2 3 
    1 2 3 4 5 
  1 2 3 4 5 6 7 
1 2 3 4 5 6 7 8 9 
  1 2 3 4 5 6 7 
    1 2 3 4 5 
      1 2 3 
        1 
"""
def Number_Pyramid_1(num):
  for i in range(1, num + 1):
    for j in range(num - i):
      print(" ", end=" ")
    for j in range(2 * i - 1):
      print(j + 1, end=" ")
    print()
  for i in range(num - 1, 0, -1):
    for j in range(num - i):
      print(" ", end=" ")
    for j in range(2 * i - 1):
      print(j + 1, end=" ")
    print()   
# num = int(input("Enter the Num of Rows: "))
# Number_Pyramid_1(num)


"""
(1,1)  (1,2)  (1,3)  (1,4)  (1,5)
(2,1)  (2,2)  (2,3)  (2,4)  (2,5)
(3,1)  (3,2)  (3,3)  (3,4)  (3,5)
(4,1)  (4,2)  (4,3)  (4,4)  (4,5)
(5,1)  (5,2)  (5,3)  (5,4)  (5,5)
"""

def Row_Column(num):
    for i in range(1, num + 1):
        for j in range(1, num + 1):
            print(f"({i},{j})", end="  ")
        print()
num = int(input("Enter the number of Rows: "))
Row_Column(num)