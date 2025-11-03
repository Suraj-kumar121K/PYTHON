--> 🧮 Step-by-Step Math Logic:

| Step | Meaning            | Explanation                                                                        |
| ---- | ------------------ | ---------------------------------------------------------------------------------- |
| 1️⃣  | **Outer loop (i)** | Yeh control karta hai **kitni rows (lines)** print hongi                            |
| 2️⃣  | **Inner loop (j)** | Yeh decide karta hai **har row me kitne elements** honge                            |
| 3️⃣  | **What to print**  | Yeh define karta hai ki **output me kya dikhana hai** — `*`, number, alphabet, e c. |
| 4️⃣  | **print()**        | Har row ke baad **next line** me jane ke liye                                       |

🧩 1. Square Star Pattern

* * * * * *  
* * * * * *
* * * * * *
* * * * * *
* * * * * * 
* * * * * *
--> CODE
rows = 6
for i in range(1, rows + 1):
  for j in range(1, rows + 1):
    print("*", end=" ")
  print()          

🧩 2. Right Triangle Pattern

*
* *
* * *
* * * *
* * * * *
* * * * * *

--> CODE
r = 6
for i in range(1, r + 1):
  for j in range(1, i + 1):
    print("*", end=" ")
  print() 
  
🧩 3. Inverted Right Triangle

* * * * * * 
* * * * *
* * * *
* * *
* *
*

--> CODE
row = 6
for i in range(1, row + 1):
  for j in range(i, row + 1):
    print("*", end=" ")
  print()  
   
🧩 4. Pyramid Pattern

           * 
          * *
         * * *
        * * * *
       * * * * *
      * * * * * *
     * * * * * * *
    * * * * * * * *
   * * * * * * * * *
  * * * * * * * * * *
 * * * * * * * * * * *

--> CODE 
   n = int(input("Enter number of rows: "))
   for i in range(1, n + 1):
     print(" " * (n - i), end=" ")
     print("* ", * i)
   
🧩 5. Inverted Pyramid
   
 * * * * * * * * * * *
   * * * * * * * * * 
     * * * * * * *   
       * * * * *     
         * * *       
           * 
--> CODE 
   n = int(input("Enter number of rows: "))
   for i in range(n):
     print(" " * i, end=" ")
     print("* ", * (n - i))
     
🧩 6. Diamond Pattern
       * 
      * *
     * * *
    * * * *
   * * * * *
  * * * * * *
 * * * * * * *
  * * * * * *
   * * * * *
    * * * *
     * * *
      * *
       *
--> Code
n = int(input("Enter number of rows: "))
for i in range(1, n + 1):       
    print(" " * (n - i), end=" ")
    print("* " * i)
for i in range(n - 1, 0, -1):
    print(" " * (n - i), end=" ")
    print("* " * i)   
  
🧩 7. Hollow Square

* * * * * * 
*         *
*         *
*         *
*         *
* * * * * *

--> Code  
rows = int(input("Enter number of rows: "))
cols = int(input("Enter number of columns: ")) 
for i in range(1, rows + 1):
    for j in range(1, cols + 1):
      if i == 1 or i == rows or j == 1 or j == cols:
        print("*", end=" ") 
      else:
         print(" ", end=" ")   
    print()

* * * * * * * * 
  * * * * * * * 
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
  * * * * * * * 
* * * * * * * * 


🧩 9. Hourglass Pattern
   
* * * * * * * * *
  * * * * * * *
    * * * * *
      * * *
        *
      * * *
    * * * * *
  * * * * * * *
* * * * * * * * *

--> Code  
n = 8  
for i in range(n, 0, -1):
    print("  " * (n - i), end="")  
    print("* " * i)
for i in range(2, n+1):
    print("  " * (n - i), end="") 
    print("* " * i)


🧩 10. Right Pascal’s Triangle

* 
* *             
* * *           
* * * *         
* * * * *       
* * * * * *     
* * * * *       
* * * *         
* * *             
* *                 
* 

🧩 11. Left Triangle Pattern

* 
* *       
* * *     
* * * *   
* * * * *        
* * * * * *

🧩 12. Butterfly Pattern

*        *
**      **
***    ***
****  ****
**********
****  ****
***    ***
**      **
*        *

🧩 13. Patterns with Borders and Diagonals

* * * * * * 
* *       *
*   *     *
*     *   *
*       * *
* * * * * *  

🧩 14. Hollow Square with Anti-Diagonals
   
* * * * * * 
*       * *
*     *   *
*   *     *
* *       *
* * * * * *

🧩 15. Hollow Square with Cross (X) and Inner Diagonal
   
* * * * * * 
* *     * *
*   * *   *
*   * *   *
* *     * *
* * * * * *

🧩 16. X / Diamond Shape Patterns   
   
*         * 
  *     * 
    * *   
    * *   
  *     * 
*         *

🧩 17. Hollow Squares and Rectangles   
   
* * * * * *  
* * * * * *
* * * * * *
*         *
*         *
* * * * * * 

🧩 18. Hollow Rectangle with Extra Bottom Fill   
   
* * * * * *
*         *
*         *
* * * * * *  
* * * * * *
* * * * * *
   
🧩 19. Hollow Rectangles with Inner Patterns
   
* * * * * *
* * *     *
* * *     *
* * *     *  
* * *     *
* * * * * *
   
🧩 20. Hollow Rectangle with Right Fill
   
* * * * * *
*     * * *
*     * * *  
*     * * *
*     * * *
* * * * * *
   
🧩 21. Complex Hollow Rectangle
   
* * * * * * 
* * * * * *
*   * * * *
*     * * *
*       * *
* * * * * *
   
🧩 22. Hollow Square with Left-Aligned Increasing Diagonal 
   
* * * * * * 
* *       *
* * *     *
* * * *   *
* * * * * *       
* * * * * *
   
🧩 23. Hollow Rectangle with Left Block
   
* * * * * *
* * *     *
* * *     *
* * *     *
*         *  
*         *
* * * * * *
   
🧩 24. Hollow Rectangle with Right Block
   
* * * * * *
*     * * *
*     * * *
*     * * *
*         *  
*         *
* * * * * *
   
🧩 25. Hollow Rectangle with Bottom-Left Block
   
* * * * * *
*         *
*         *
* * *     *
* * *     *  
* * *     *
* * * * * *
   
🧩 26. Hollow Rectangle with Bottom-Right Block
   
* * * * * *
*         *
*         *
*     * * *
*     * * *  
*     * * *
* * * * * *

🧩 27. Large Star Squares / Diamond Shapes
   
* * * * * * * * * * *
* *                 *
* * *               *
* * * *             *
* * * * *           *
* * * * * *         *
* * * * *           *
* * * *             *
* * *               *  
* *                 *
* * * * * * * * * * *

🧩 28. Nested Hollow Squares with Inner Diamond  

* * * * * * * * * * *
* * * * * * * * * * *
*   * * * * * * *   *
*     * * * * *     *
*       * * *       *
*         *         *
*                   *
*                   *
*                   *  
*                   *
* * * * * * * * * * *
   
🧩 29. Nested Hollow Squares with Inner Inverted Diamond
   
* * * * * * * * * * *
*                 * *
*               * * *
*             * * * *
*           * * * * *
*         * * * * * *
*           * * * * *
*             * * * *
*               * * *  
*                 * *
* * * * * * * * * * *
   
🧩 30. Hollow Square with Centered Diamond
   
* * * * * * * * * * *
*                   *
*                   *
*                   *
*                   *
*         *         *
*       * * *       *
*     * * * * *     *
*   * * * * * * *   *  
* * * * * * * * * * *
* * * * * * * * * * *

🧩 31. Right-Aligned Triangle
   
          *
        * *
      * * *    
    * * * *      
  * * * * *        
* * * * * *   
   
🧩 32. Right-Aligned Inverted Pyramid
   
* * * * * * 
  * * * * *
    * * * *
      * * *
        * *
          *
       
🧩 33. Hourglass / Diamond with Full Base      
   
          *
        * *
      * * *
    * * * *
  * * * * *
* * * * * *
  * * * * *
    * * * *
      * * *  
        * *
          *

       

      
