# 🧩 1. Square Star Pattern
"""
* * * * * *  
* * * * * *
* * * * * *
* * * * * *
* * * * * * 
* * * * * * """
"""
n = int(input("Enter a Number "))
for i in range(1, n + 1):
    for j in range(1, n + 1):
        print("*", end=" ")
    print()
"""

# 🧩 2. Right Triangle Pattern
"""
*
* *
* * *
* * * *
* * * * *
* * * * * *
"""
"""
n = int(input("Enter a Number "))
for i in range(1, n + 1):
    for j in range(1, n + 1):
        if j <= i:
            print("*", end=" ")
        else:
            print(' ', end=" ")
    print()
"""

# 🧩 3. Inverted Right Triangle
"""
* * * * * * 
* * * * *
* * * *
* * *
* *
*
"""
"""
n = int(input("Enter a Number "))
for i in range(n, 0, -1):
    for j in range(i):
        print("*", end=" ")
    print()
"""
"""
 
"""
# n = int(input("Enter a Number "))

"""for i in range(n):

    # Left space
    for j in range(n - i - 1):
        print(" ", end=" ")
    # Star with extra space
    for k in range(i + 1):
        print("*", end="   ")
    print()"""

"""
        *   
      *   *   
    *   *   *   
  *   *   *   *   
*   *   *   *   *
  *  *   *   * 
    *  *   * 
     *   * 
       *     

"""
"""
# n = int(input("Enter a Number "))

# Upper Part
for i in range(n):
    # Space
    for j in range(n - i - 1):
        print(" ", end=" ")
    # Star
    for k in range(i + 1):
        print("*", end="   ")
    print()

# Lower Part
for i in range(n - 1, 0, -1):
    # Space
    for j in range(n - i):
        print(" ", end=" ")
    # Star
    for k in range(i):
        print("*", end="   ")
    print()
"""
"""
* * * * * *
* * * * *
* * * *
* * *
* *
*
* *
* * *
* * * *
* * * * *
* * * * * *
"""
"""
* * * * * *
* * * * *
* * * *
* * *
* *
*
* *
* * *
* * * *
* * * * *
* * * * * *
"""
"""
n = int(input("Enter a number: "))
for i in range(n, 0, -1):
    for j in range(i):
        print("*", end=" ")
    print()

for i in range(2, n + 1):
    for j in range(i):
        print("*", end=" ")
    print()
"""
"""
* * * * * *
  * * * * *
    * * * *
      * * *
        * *
          *
"""
"""
n = int(input("Entere a number "))
for i in range(n, 0, -1):
    for j in range(n - i):
        print(" ", end=" ")
    for k in range(i):
        print("*", end=" ") 
    print()
"""
"""
* * * * * *
  * * * * *
    * * * *
      * * *
        * *
          *
        * *
      * * * 
    * * * *
  * * * * *
* * * * * *
"""
"""
n = int(input("Entere a number ")) # i har baar decrease ho raha hai.
for i in range(n, 0, -1):
    for j in range(n - i):
        print(" ", end=" ")
    for k in range(i):
        print("*", end=" ") 
    print()
for i in range(2, n + 1):
    for j in range(n - i):
        print(" ", end=" ")
    for k in range(i):
        print("*", end=" ") 
    print()
"""
"""
* * * * * * 
 * * * * * 
  * * * * 
   * * * 
    * * 
     * 
"""
"""
n = int(input("Entere a number "))
for i in range(1, n + 1):
    for j in range(i):
        print(" ", end="")
    for k in range(n - i):
        print("*", end=" ")
    print()
"""

"""
     * 
    * * 
   * * * 
  * * * * 
 * * * * * 
* * * * * *
"""
"""n = int(input("Entere a number "))
for i in range(1, n + 1):
    for j in range(n - i):
        print(" ", end="")
    for k in range(i):
        print("*", end=" ")
    print()"""

"""
* * * * * * 
 * * * * * 
  * * * * 
   * * * 
    * * 
     * 
    * * 
   * * * 
  * * * * 
 * * * * * 
* * * * * *
"""
"""
n = int(input("Entere a number "))
for i in range(1, n + 1):
    for j in range(i - 1):
        print(" ", end="")
    for k in range(n - i + 1):
        print("*", end=" ")
    print()
for i in range(2, n + 1):
    for j in range(n - i):
        print(" ", end="")
    for k in range(i):
        print("*", end=" ")
    print()
"""
    
"""
* * * * * * * * * * * * 
* * * * *     * * * * *
* * * *         * * * *
* * *             * * *
* *                 * *
*                     * 
* *                 * *
* * *             * * *
* * * *         * * * *
* * * * *     * * * * *
* * * * * * * * * * * *
"""

"""
n = int(input("Enter a Number: "))
for i in range(1, n + 1):
    for j in range(1, 2*n):
        if i == n or i + j == n + 1 or j - i == n - 1:
            print("* ", end=" ")
        else:
            print(" ", end="  ")
    print()
"""   
"""
n = int(input("Enter a Number: "))
for i in range(1, n + 1):
    for j in range(1, 2 * n):
        if i == n or i + j == n + 1 or j - i == n - 1:
            print("*", end=" ")
        else:
            print(" ", end=" ")
    print()
"""

"""
n = int(input("Enter a Number: "))
for i in range(1, 2 * n):
    for j in range(1, 2 * n):
        if (
            i == n
            or i + j == n + 1 
            or j - i == n - 1 
            or i - j == n - 1 
            or j + i == 3 * n - 1
            ):
            print("*", end=" ")
        else:
            print(" ", end=" ")
    print()
"""