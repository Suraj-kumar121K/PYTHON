# Repeated Number Square Pattern
"""
1 1 1 1 1
2 2 2 2 2
3 3 3 3 3
4 4 4 4 4
"""
def squre_pattern(num):
    for i in range(1, num + 1):
        for j in range(1, num + 1):
            print(i, end=" ")
        print()
# num = int(input("Enter the number of rows: "))
# squre_pattern(num)

"""
1 1 1 1 1
0 0 0 0 0
1 1 1 1 1
0 0 0 0 0
1 1 1 1 1
"""
def squre_pattern_first(num):
    for i in range(1, num + 1):
        for j in range(1, num + 1):
            if i % 2 != 0:
                print(1, end=" ")
            else:
                print(0, end=" ")
        print()
# num = int(input("Enter the number of rows: "))
# squre_pattern_first(num)

"""
1 2 3 4 5
1 2 3 4 5
1 2 3 4 5
1 2 3 4 5
1 2 3 4 5
"""
def squre_pattern_second(num):
    for i in range(1, num + 1):
        for j in range(1, num + 1):
                print(j, end=" ")
        print()
# num = int(input("Enter the number of rows: "))
# squre_pattern_second(num)

# Inverted Right-Angled Triangle Pattern
"""
* * * * * *
* * * * *
* * * *
* * * 
* *
*
"""
def Right_Angled_Triangle(num): 
    for i in range(num, 0, -1):
        for j in range(i):
            print("*", end=" ")
        print()
# num = int(input("Enter the number of rows: "))
# Right_Angled_Triangle(num)

# Right-Aligned Increasing Triangle Pattern
"""
            *
          * *
        * * *
      * * * *
    * * * * *
  * * * * * *
* * * * * * *
"""
def Right_Aligned_Increasing_Triangle(num):
    for i in range(1, num + 1):
        for j in range(num - i):
            print(" ", end=" ")
        for k in range(i):
            print("*", end=" ")
        print()
# num = int(input("Enter the number of rows: "))
# Right_Aligned_Increasing_Triangle(num)

# Right-Aligned Decreasing Triangle Pattern
"""
* * * * * *
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
        for k in range(num - i + 1):
            print("*", end=" ")
        print()
# num = int(input("Enter the number of rows: "))
# Right_Aligned_Decreasing_Triangle(num)

"""
1 
1 2 
1 2 3 
1 2 3 4 
1 2 3 4 5 
1 2 3 4 5 6 
1 2 3 4 5 6 7
"""
def pattern_1(num):
    for i in range(1, num + 1):
        for j in range(1, i + 1):
            print(j, end=" ")
        print()
num = int(input("Enter the number of rows: "))
pattern_1(num)