"""
*
* *
* * *
* * * *
* * * * *
"""
def first_patern(num):
    for i in range(num):
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
    for i in range(num, 0, -1):
        for j in range(i):
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
        for i in range(i):    
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
def Space_Pattern_second(num):
    for i in range(1, num + 1):
        for j in range(i - 1):
            print(" ", end=" ")
        for j in range(num - i + 1):
            print("*", end=" ")
        print()
# Space_Pattern_second(5)

"""
        1
      1 2
    1 2 3
  1 2 3 4
1 2 3 4 5
"""
def Space_Pattern_Three(num):
    for i in range(1, num + 1):
        for j in range(num - i):
            print(" ", end=" ")
        for j in range(1, i + 1):
            print(j, end=" ")
        print()
# Space_Pattern_Three(5)

# ⭐ Level 3 — Pyramid
"""
        *
      * * *
    * * * * *
  * * * * * * *
* * * * * * * * *
"""
def Pyramid(pyr):
    for i in range(1, pyr + 1):
        for j in range(pyr - i):
            print(" ", end=" ")
        for j in range(2 * i - 1):
            print("*", end=" ")
        print()
# Pyramid(5)

"""
        1
      1 2 3
    1 2 3 4 5
  1 2 3 4 5 6 7
1 2 3 4 5 6 7 8 9
"""
def Pyramid(pyr):
    for i in range(1, pyr + 1):
        for j in range(pyr - i):
            print(" ", end=" ")
        for j in range(1, 2 * i):
            print(j, end=" ")
        print()
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
def Pyramid(pyr):
    for i in range(1, pyr + 1):
        for j in range(pyr - i):
            print(" ", end=" ")
        for j in range(2 * i - 1):
            print("*", end=" ")
        print()
    for i in range()

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