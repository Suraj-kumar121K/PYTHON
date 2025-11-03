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
        * * *       
      * * * * *     
    * * * * * * *     
  * * * * * * * * * 
* * * * * * * * * * *

🧩 5. Inverted Pyramid
   
 * * * * * * * * * * *
   * * * * * * * * * 
     * * * * * * *   
       * * * * *     
         * * *       
           * 

🧩 6. Diamond Pattern

        *                  
      * * *                 
    * * * * *               
  * * * * * * *             
* * * * * * * * *           
  * * * * * * *             
    * * * * *               
      * * *
        *

🧩 7. Hollow Square

* * * * * * 
*         *
*         *
*         *
*         *
* * * * * *

🧩 8. Hollow Pyramid

        *
      *   *
    *       *
  *           *
* * * * * * * * *

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

       

      
