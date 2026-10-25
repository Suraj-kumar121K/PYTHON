# 1. Hollow Square
"""
* * * * *
*       *
*       *
*       *
* * * * *
"""
def Hollow_Square(num):
  for i in range(1, num + 1):
    for j in range(1, num + 1):
      if i == 1 or j == 1 or i == num or j == num:
        print("*", end=" ")
      else:
        print(" ", end=" ")
    print()
# num = int(input("Enter a number of Rows: "))
# Hollow_Square(num)


# 2. Hollow Rectangle
"""
* * * * * *
*         *
*         *
* * * * * *
"""
def Hollow_Rectangle(num):
  for i in range(1, num + 1):
    for j in range(1, num + 3):
      if i == 1 or j == 1 or j == num + 2 or i == num:
        print("*", end=" ")
      else:
        print(" ", end=" ")
    print()
# num = int(input("Enter a number of Rows: "))
# Hollow_Rectangle(num)
    
# 3. Hollow Right-Angled Triangle
"""
*
* *
*   *
*     *
* * * * *
"""
def Hollo_Right_triangle(num):
  for i in range(1, num + 1):
    for j in range(i):
      if i == 0 or j == 0:
        print("*", end=" ")
    print()
# num = int(input("Enter a number of Rows: "))
# Hollo_Right_triangle(num)

# 4. Hollow Inverted Right Triangle
"""
* * * * *          i = 1 | space = 0 | print 5 star
*     *            i = 2 | space = 2 | print 1 star
*   *              i = 3 | space = 1 | print 1 star
* *                i = 4 | space = 0 | print 1 star
*                  i = 5 | space = 0 | print 1 star
"""
def Hollow_Inverted_Tringle(num):
  for i in range(num , 0, -1):
    for j in range(i):
      if i == 0 or j == 0 or i == num or j == num + 1: 
        print("*", end=" ")
    print()
# num = int(input("Enter a number of Rows: "))
# Hollow_Inverted_Tringle(num)

# 5. Hollow Pyramid
"""
    *
   * *
  *   *
 *     *
* * * * *
"""
def Hollow_Pyramid(num):
  for i in range(1, num + 1):
    for j in range(num - i):
      print(" ", end=" ")
    for j in range(1, i + 1):
      if i == 0 or j==i or i == num:
        print("*", end=" ")
      else:
        print(" ", end=" ")
    print()
# num = int(input("Enter a number of Rows: "))
# Hollow_Pyramid(num)

# 6. Hollow Inverted Pyramid
"""
* * * * *
 *     *
  *   *
   * *
    *
"""
def Hollow_Pyramid(num):
  for i in range(num, 0, -1):
    for j in range(num - i):
      print(" ", end=" ")
    for j in range(1, i + 1):
      if i == 0 or j==i or i == num:
        print("*", end=" ")
      else:
        print(" ", end=" ")
    print()
# num = int(input("Enter a number of Rows: "))
# Hollow_Pyramid(num)

# 8. Hollow Hourglass
"""
* * * * *
 *     *
  *   *
   * *
  *   *
 *     *
* * * * *
"""

# 9. Hollow Rhombus
"""
    * * * * *
   *       *
  *       *
 *       *
* * * * *
"""

# 10. Hollow Butterfly
"""
*       *
* *   * *
* * * * *
* *   * *
*       *
"""

# 11. Hollow Butterfly
"""
*         *
**       **
* *     * *
*  *   *  *
*   * *   *
*  *   *  *
* *     * *
**       **
*         *
"""

# 12. Sandglass Star Pattern
"""
* * * * *
 * * * *
  * * *
   * *
    *
   * *
  * * *
 * * * *
* * * * *
"""

# 13. Hollow Left Triangle
"""
*
* *
*   *
*     *
* * * * *
"""

# 14. Hollow Right Triangle
"""
        *
      * *
    *   *
  *     *
* * * * *
"""

# 15. Hollow Diamond Pattern
"""
        *
      *   *
    *       *
  *           *
*               *
  *           *
    *       *
      *   *
        *
"""
def Hollow_Diamond_Pattern(num):
  for i in range(1, num + 1):
    for j in range(num - i):
      print(" ", end=" ")
    for j in range(1, 2 * i):
      if j == 1 or j == 2 * i - 1:
        print("*", end=" ")
      else:
        print(" ", end=" ")
    print()
  for i in range(num - 1, 0, -1):
    for j in range(num - i):
      print(" ", end=" ")
    for j in range(1, 2 * i):
      if j == 1 or j == 2 * i - 1:
        print("*", end=" ")
      else:
        print(" ", end=" ")
    print()
num = int(input("Enter a number of Rows: "))
Hollow_Diamond_Pattern(num)

"""
* * * * * * * * *
* * * * * * * * *
* *           * *
* *           * *
* *           * *
* *           * *
* *           * *
* * * * * * * * *
* * * * * * * * *
"""
def Hollow_squery_2(num):
  for i in range(1, num + 1):
    for j in range(1, num + 1):
      if i == 1 or i == 2 or i == num - 1 or i == num:
        print("*", end=" ")
      elif j == 1 or j == 2 or j == num - 1 or j == num:
        print("*", end=" ")
      else:
        print(" ", end=" ")
    print()
# num = int(input("Enter a number of Rows: "))
# Hollow_squery_2(num)

"""
*           *
  *       *
    *   *
      *
    *   *
  *       *
*           *
"""
def cross_pattern(num):
    for i in range(num, 0, -1):
        for j in range(num - i):
            print(" ", end=" ")
        for j in range(1, 2 * i):
            if j == 1 or j == 2 * i - 1:
                print("*", end=" ")
            else:
                print(" ", end=" ")
        print()
    for i in range(2, num + 1):
        for j in range(num - i):
            print(" ", end=" ")
        for j in range(1, 2 * i):
            if j == 1 or j == 2 * i - 1:
                print("*", end=" ")
            else:
                print(" ", end=" ")
        print()
# num = int(input("Enter a number of Rows: "))
# cross_pattern(num)