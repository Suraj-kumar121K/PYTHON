"""
*
* *
* * *
* * * *
* * * * *
"""
def first_patern(num):
    for i in range(1, num + 1):
        for j in range(i):
            print("*", end=" ")
        print()    
# first_patern(5)
   
"""
* * * * *
* * * *
* * *
* *
*
"""
def second_row(num):
    for i in range(1, num + 1):
        for j in range(num - i + 1):
            print("*", end=" ")
        print()
# second_row(5)

"""
1
1 2
1 2 3
1 2 3 4
1 2 3 4 5
"""
def three_row(num):
    for i in range(1, num + 1):
        for j in range(1, i + 1):
            print(j, end=" ")
        print()
# three_row(5)

"""
1
2 2
3 3 3
4 4 4 4
5 5 5 5 5
"""
def fourth_row(num):
    for i in range(1, num + 1):
        for j in range(1, i + 1):
            print(i, end=" ")
        print()
# fourth_row(5)

# ⭐ Level 2 — Space + Pattern
"""
        *
      * *
    * * *
  * * * *
* * * * *
"""
def Space_Pattern_first(space):
    for i in range(1, space + 1):
        for j in range(space - i):
            print(" ", end=" ")
        for k in range(i):
            print("*", end=" ") 
        print()
# Space_Pattern_first(5)

       
"""
* * * * *
  * * * *
    * * *
      * *
        *
"""
# def Space_Pattern_second(num):

# Space_Pattern_second(5)

"""
        1
      1 2
    1 2 3
  1 2 3 4
1 2 3 4 5
"""
# def Space_Pattern_Three(num):

# Space_Pattern_Three(5)

# ⭐ Level 3 — Pyramid
"""
        *
      * * *
    * * * * *
  * * * * * * *
* * * * * * * * *
"""
# def Pyramid(pyr):

# Pyramid(5)

"""
        1
      1 2 3
    1 2 3 4 5
  1 2 3 4 5 6 7
1 2 3 4 5 6 7 8 9
"""
# def Pyramid(pyr):

# Pyramid(5)

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
# def Pyramid(pyr):
    
# Pyramid(5)

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

# Repeated Number Square Pattern
"""
1 1 1 1 1
2 2 2 2 2
3 3 3 3 3
4 4 4 4 4
"""
# def squre_pattern(num):

# num = int(input("Enter the number of rows: "))
# squre_pattern(num)

"""
1 1 1 1 1
0 0 0 0 0
1 1 1 1 1
0 0 0 0 0
1 1 1 1 1
"""
# def squre_pattern_first(num):

# num = int(input("Enter the number of rows: "))
# squre_pattern_first(num)

"""
1 2 3 4 5
1 2 3 4 5
1 2 3 4 5
1 2 3 4 5
1 2 3 4 5
"""
# def squre_pattern_second(num):

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
# def Right_Angled_Triangle(num): 

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
# def Right_Aligned_Increasing_Triangle(num):

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
# def Right_Aligned_Decreasing_Triangle(num):

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
# def pattern_1(num):

# num = int(input("Enter the number of rows: "))
# pattern_1(num)

"""
1 
1 0
1 0 1 
1 0 1 0 
1 0 1 0 1 
1 0 1 0 1 0 
1 0 1 0 1 0 1
"""
# def pattern(num):

# num = int(input("Enter the number of rows: "))
# pattern(num)                   

"""
5
4 4
3 3 3
2 2 2 2
1 1 1 1 1
"""
# def pattern_3(num):

# num = int(input("Enter the number of rows: "))
# pattern_3(num) 