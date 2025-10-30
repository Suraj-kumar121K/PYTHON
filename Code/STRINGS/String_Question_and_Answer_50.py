1.  What is a string in Python?
    A string is a sequence of characters enclosed in quotes (' or ").

2. How do you create a string in Python?
   S = 'Suraj'

3. What is the difference between single, double, and triple quotes?
   | Type of Quotes    | Example                        | Used For                             | Notes                                                         |
   | ----------------- | ------------------------------ | ------------------------------------ | ------------------------------------------------------------- |
   | **Single Quotes** | `'Hello'`                      | For short single-line strings        | You can include double quotes inside easily: `'He said "Hi"'` |
   | **Double Quotes** | `"Hello"`                      | Also for single-line strings         | You can include single quotes easily: `"It's a nice day"`     |
   | **Triple Quotes** | `'''Hello'''` or `"""Hello"""` | For multi-line strings or docstrings | Allows both single and double quotes inside without escaping  |

1. Single Quotes
   name = 'Suraj'
   msg = 'He said "Python is fun"'
   print(msg)

2. Double Quotes
   text = "It's a great day"
   print(text)

3. Triple Quotes
  --> Multi-line text
  --> Docstrings (documentation inside functions or classes)
   msg = """Hello Suraj,
   Welcome to Python programming!
   Let's learn strings."""
   print(msg)

# 4. How to access characters from a string?
s = "Suraj"
print(s[0])
print(s[-1])

# 5. How do you find the length of a string
name = 'Suraj1'
print(len(name))

# 6. How to slice a string?
```
You can slice a string using the slice operator — [:].
Syntax:
    string[start:end:step]
start → index to begin (inclusive)
end → index to stop (exclusive)
step → interval or skip value (optional)

Value-->             S   U   R   A   J   
Index-->             0   1   2   3   4   
Negative Indexes--> -5  -4  -3  -2  -1
```
str = "Suraj"
print(str[:-4])
print(str[-1])

# 7. How to concatenate two strings?
s = "Suraj"
name = "Kumar"
print(s + " " + name)

# 8. How to repeat a string?
s = "Suraj"
print(s * 2)

# 9. How to check if a substring exists?
name = "Suraj Kumar"
print("Suraj" in name)
print("Java" not in name)

# 10. Give examples of commonly used escape sequences.
      | Code  |    Meaning   |         Example          |        Output        |
      | ----- | ------------ | ------------------------ | -------------------- |
      | `\'`  | Single quote | `'It\'s fine'`           | `It's fine`          |
      | `\"`  | Double quote | `"He said \"Yes\""`      | `He said "Yes"`      |
      | `\\`  | Backslash    | `"C:\\folder\\file.txt"` | `C:\folder\file.txt` |
      | `\n`  | New line     | `"Hello\nWorld"`         |                      |
      | `\t`  | Tab space    | `"Name\tAge"`            | `Name    Age`        |
--> Code
# Escape Sequence Examples
print('It\'s a good day')
print("He said \"Hello!\"")
print("C:\\Users\\Admin\\Desktop")
print("Hello\nWorld")
print("Name\tAge")


# 11. How to convert a string to uppercase/lowercase?
s = "Suraj Kumar"
print(s.upper())
print(s.lower())

# 11. How to remove whitespace?
name = "Mohan Kumar"
print(name.strip())

# 12. How to replace part of a string?
name = "I Love Mom"
print(name.replace("Mom", "Dad"))

-->      String Methods

# 13. title()
s = "Kumar"
print(s.title())

# 14. capitalize()
s = "i Am Suraj"
print(s.capitalize())

# 15. count()
s = "manan"
print(s.count("a"))

# 16. index()
s = "We are Going"
print(s.index("Going"))

# 17. find()
s = "hello world"
print(s.find("world")) 

# 18. startswith() and endswith()
s = "python"
print(s.startswith("py")) 
print(s.endswith("on"))   

# 19. split()
s = "apple,banana,cherry"
print(s.split(","))  

# 20. join()
lst = ['apple', 'banana', 'cherry']
print("-".join(lst))  

# 21. swapcase()
s = "Python"
print(s.swapcase())  

-->  String Program Questions
