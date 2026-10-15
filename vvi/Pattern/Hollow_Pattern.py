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
* * * * *
*     *
*   *
* *
*
"""

# 5. Hollow Pyramid
"""
    *
   * *
  *   *
 *     *
* * * * *
"""

# 6. Hollow Inverted Pyramid
"""
* * * * *
 *     *
  *   *
   * *
    *
"""

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