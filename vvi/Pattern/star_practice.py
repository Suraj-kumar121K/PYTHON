# 1. Increasing Triangle Pattern
"""
*
* *
* * *
* * * *
* * * * *
"""
def Increasing_Triangle(num):
  for i in range(1, num + 1):
    for j in range(1, i + 1):
      print("*", end=" ")
    print()
# num = int(input("Enter a number of Rows: "))
# Increasing_Triangle(num)

# 2. Decreasing Triangle Pattern
"""
* * * * *
* * * *
* * *
* *
*
"""
def Decreasing_Triangle(num):
  for i in range(1, num + 1):
    for j in range(num - i + 1):
      print("*", end=" ")
    print()
# num = int(input("Enter a number of Rows: "))
# Decreasing_Triangle(num)

# Level 2 — Space + Patterns
# 4. Right-Aligned Increasing Triangle Pattern
"""
        *
      * *
    * * *
  * * * *
* * * * *
"""
def Right_Aligned_Increasing_Triangle(num):
  for i in range(1, num + 1):
    for j in range(num - i):
      print(" ", end=" ")
    for j in range(1, i + 1):
      print("*", end=" ")
    print()
# num = int(input("Enter a number of Rows: "))
# Right_Aligned_Increasing_Triangle(num)

# 5. Right-Aligned Decreasing Triangle Pattern
"""
* * * * *
  * * * *
    * * *
      * *
        *
"""
def Right_Aligned_Decreasing_Triangle(num):
  for i in range(1, num + 1):
    for j in range(i - 1):
      print(" ", end=" ")
    for j in range(num - i + 1):
      print("*", end=" ")
    print()
# num = int(input("Enter a number of Rows: "))
# Right_Aligned_Decreasing_Triangle(num)
    
# Level 3 — Pyramid Patterns
# 6. Pyramid Pattern
"""
        *
      * * *
    * * * * *
  * * * * * * *
* * * * * * * * *
"""
def Pyramid_Pattern(num):
  for i in range(1, num + 1): 
    for j in range(num - i):
      print(" ", end=" ")
    for j in range(2 * i - 1):
      print("*", end=" ")
    print()
# num = int(input("Enter a number of Rows: "))
# Pyramid_Pattern(num)
'''
 Row              Space(num - i)            Stars(2 * i - 1)
 i=1                5 - 1 = 4                 2 * 1 - 1 = 1
 i=2                5 - 2 = 3                 2 * 2 - 1 = 3
 i=3                5 - 3 = 2                 2 * 3 - 1 = 5
 i=4                5 - 4 = 1                 2 * 4 - 1 = 7
 i=5                5 - 5 = 0                 2 * 5 - 1 = 9
'''

# 7. Diamond Pattern
"""
        *
      * * *
    * * * * *
  * * * * * * *
* * * * * * * * *
  * * * * * * *
    * * * * *
      * * *
        *
"""
def Diamond_Pattern(num):
  for i in range(1, num + 1):
    for j in range(num - i):
      print(" ", end=" ")
    for j in range(2 * i - 1):
      print("*", end=" ")
    print()
  for i in range(num - 1, 0, -1):
    for j in range(num - i):
      print(" ", end=" ")
    for j in range(2 * i - 1):
      print("*", end=" ")
    print()
num = int(input("Enter a number of Rows: "))
Diamond_Pattern(num)
