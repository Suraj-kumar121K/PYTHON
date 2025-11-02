--> What is a Loop?
    A loop is used to repeat a block of code multiple times until a certain condition is met.

--> TYPE OF TWO LOOP
    1. for loop
    2. while loop

--> 1. FOOR LOOP
       A for loop in Python is used to repeat (iterate) over a sequence
Syntax
    for variable in sequence:
    # code block
--> Example 
--> 1: Using for with a list
fruits = ["apple", "banana", "cherry"]
for fruit in fruits:
    print(fruit)

--> 2: Using for with range()
for i in range(5):
    print(i)

--> 3: Custom start and end in range
for i in range(2, 10, 2): #range(start, stop, step)
    print(i)

--> Summary Table
| Keyword   |               Meaning                       |
| --------- | ------------------------------------------- |
| `for`     | starts the loop                             |
| `in`      | checks membership in a sequence             |
| `range()` | generates a sequence of numbers             |
| `else`    | optional, runs when loop completes normally |

--> 2. while Loop
A while loop in Python is used to repeat a block of code as long as a condition is true.

--> Syntax
  while condition:
   # code block

--> Example:
count = 0
while count < 5:
    print("Count:", count)
    count += 1
  
--> 🚦 Loop Control Statements
     break – stop the loop early
for i in range(10):
    if i == 5:
       break
   print(i)

--> continue – skip current iteration
for i in range(5):
    if i == 2:
        continue
    print(i)

--> else with loop 
HE else block runs only if the loop completes normally (not stopped by break).
for i in range(3):
    print(i)
else:
    print("Loop completed!")

--> 🧠 Bonus: Nested Loops
A nested loop runs the inner loop completely for every single iteration of the outer loop.

--> Syntax 
for i in range(outer_limit):
    for j in range(inner_limit):
        # code block

--> Example
1: Nested for loop
for i in range(3):
    for j in range(2):
        print(i, j)
--> 🧠 Here:
     The outer loop (i) runs 3 times.
     For each i, the inner loop (j) runs 2 times.
     So total runs = 3 × 2 = 6 times.

--> 2: Nested loop pattern
for i in range(1, 4):
    for j in range(1, i + 1):
        print("*", end=" ")
    print()
  
3: Nested while loop
i = 1
while i <= 3:
    j = 1
    while j <= 2:
        print(f"i={i}, j={j}")
        j += 1
    i += 1
