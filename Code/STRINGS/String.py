--> What is String
    a string is a sequence of characters enclosed in quotes.

-->  You can use:
     Single quotes ' '
     Double quotes " "
     Triple quotes ''' ''' or """ """ (for multi-line strings)

--> 🟢 Example:
        a ='suraj' # Single quoted string
        b = "suraj" # Double quoted string
        c = '''suraj''' # Triple quoted string
        d = """suraj""" # Multiline quoted Line

--> ✍️ 2. String Creation
          You can create strings in different ways:
a = 'Python'
b = "Learning"
c = '''Data Science'''

--> 🔤 3. Accessing Characters
          Strings are index-based — each character has a position (index).

Character      --	 P	 y	 t  	h  	o  	n
                   -----------------------
Index	         --  0	 1	 2	  3	  4	  5
                   ------------------------
Negative Index --  (-5) (-4) (-3) (-2) (-1)

--> The index in a sting starts from 0 to (length -1) in Python. In order to slice a string, we use

--> Example:
word = "Python"
print(word[0])   # P
print(word[5])   # n

--> 🔁 4. String Slicing
        You can extract parts of a string using slice syntax:
-->  Syntex:
        string[start:end:step]

--> Example:
s = "Python"
print(s[0:4])    # Pyth
print(s[:4])     # Pyth (default start = 0)
print(s[2:])     # thon (default end = end)
print(s[::-1])   # nohtyP (reverse string)

--> 🧮 String Operations
        Python allows many operations on strings.

Operation	                  Example	                    Output
Concatenation	         "Hello" + "World"	              "HelloWorld"

Repetition	                "Hi" * 3	                  "HiHiHi"

Length	                   len("Hello")	                   5

Membership	              'H' in "Hello"	               True

--> 🧰 6. String Methods
            Python strings have built-in methods.

--> Here are some common ones 👇

  Method	                Description	                       Example
.upper()	          Converts to uppercase	            "python".upper() → "PYTHON"
    
.lower()	          Converts to lowercase	            "HELLO".lower() → "hello"
    
.title()	          Capitalizes each word	            "hello world".title()

.strip()	          Removes spaces	                " hi ".strip()

.replace(a, b)	      Replaces text	                    "apple".replace("a","A")

.find(sub)	          Finds substring index	            "python".find("th") → 2
    
.count(sub)	          Counts occurrences	            "banana".count("a") → 3
    
.split()	          Splits string by space	        "a b c".split() → ['a','b','c']

.join(list)	          Joins list into string	        "-".join(['a','b','c']) → 'a-b-c'

--> 🧩 7. String Formatting
           Used to insert variables inside strings.
              
--> ✅ Using f-string (modern way):
name = "Suraj"
age = 20
print(f"My name is {name} and I am {age} years old.")

--> ✅ Using .format():
print("My name is {} and I am {} years old.".format("Suraj", 20))

--> 🧱 8. Escape Sequences
           Used to insert special characters.

Code	      Meaning	           Example
\'	          Single quote	       'It\'s fine'

\"	          Double quote	       "He said \"Yes\""

\\	          Backslash	           "C:\\folder\\file.txt"

\n	          New line	           "Hello\nWorld"

\t	          Tab space	           "Name\tAge"


--> 🧠 10. Important Notes
       Strings are sequences, so you can loop over them:
--> Code         
       for ch in "Python":
       print(ch)


--> Strings can be compared:
print("apple" == "Apple")   # False
print("a" < "b")            # True (based on ASCII values)

# 🌟 STRING IN PYTHON - FULL EXAMPLES 🌟

--> String Creation
single_quote = 'Hello'
double_quote = "World"
multi_line = """This is
a multi-line string."""
print("1. String Creation:")
print(single_quote)
print(double_quote)
print(multi_line)
print("-" * 40)

--> String Indexing and Slicing
text = "Python"
print("2. Indexing and Slicing:")
print("Full String:", text)
print("First character:", text[0])
print("Last character:", text[-1])
print("Slice [0:4]:", text[0:4])       # Pyth
print("Slice [2:]:", text[2:])         # thon
print("Slice [::2] (skip 1 char):", text[::2])  # Pto
print("Reverse string:", text[::-1])
print("-" * 40)

--> String Operations
a = "Hello"
b = "Python"
print("3. String Operations:")
print("Concatenation:", a + " " + b)
print("Repetition:", a * 3)
print("Length of a:", len(a))
print("'H' in a:", 'H' in a)
print("'z' not in a:", 'z' not in a)
print("-" * 40)

--> String Methods
sample = "  hello world  "
print("4. String Methods:")
print("Original:", repr(sample))
print("Uppercase:", sample.upper())
print("Lowercase:", sample.lower())
print("Title Case:", sample.title())
print("Stripped:", sample.strip())
print("Replace:", sample.replace("world", "Python"))
print("Find 'o':", sample.find('o'))
print("Count 'l':", sample.count('l'))
print("Split:", sample.split())
print("Join:", "-".join(['a', 'b', 'c']))
print("-" * 40)

--> Escape Sequences
print("5. Escape Sequences:")
print("Line break:\nHello\nWorld")
print("Tab space:\tPython\tRocks")
print("Quote inside string: \"Hello!\"")
print("Backslash: C:\\Users\\Python")
print("-" * 40)

--> String Formatting
name = "Suraj"
age = 20
print("6. String Formatting:")
print("Using format() -> My name is {} and I am {} years old.".format(name, age))
print(f"Using f-string -> My name is {name} and I am {age} years old.")
print("-" * 40)

--> Immutability
s = "Hello"
print("7. String Immutability:")
print("Before change:", s)
# s[0] = "Y"  # ❌ This will give an error
s = "Y" + s[1:]
print("After change:", s)
print("-" * 40)

--> Looping through a String
print("8. Loop through string:")
for ch in "Python":
    print(ch, end=" ")
print("\n" + "-" * 40)

--> Comparison
print("9. String Comparison:")
print("apple" == "Apple")  # False
print("a" < "b")           # True (ASCII value comparison)
print("-" * 40)

--> Summary Example
msg = "Python is fun!"
print("10. Summary Example:")
print("Message:", msg)
print("Uppercase:", msg.upper())
print("Reverse:", msg[::-1])
print("Count of 'n':", msg.count('n'))
print("Does it contain 'fun'? ->", 'fun' in msg)
