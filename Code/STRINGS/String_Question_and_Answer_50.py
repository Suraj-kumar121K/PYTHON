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

# 23. Reverse a string
name = "suraj"
print(name[::-1])

# 24. Check if a string is palindrome
s = "Manan"
print(s == s[::-1])

# 25. Count vowels in a string
s = "suraj"
vowels = "aeiouAEIOU"
count = sum(1 for ch in s if ch in vowels)
print("Number of vowels", count)

# 26. Find frequency of each character
s = 'manan'
freq = {}
for ch in s:
    freq[ch] = freq.get(ch, 0) + 1
print(freq)
    

# 27. Remove duplicates from string
s = "manan"
result = "".join(sorted(set(s), key=s.index))
print("without duplicates:", result)

# 28. Check if two strings are anagrams
s1 = "listen"
s2 = "silent"

if sorted(s1) == sorted(s2):
    print("Anagrams")
else:
    print("Not Anagrams")    

# 29. Print even index characters
s = "suraj"
print("Even index characters", s[::2])

# 30. Print odd index characters
s = "Kumar"
print("Odd index characters:", s[1::2])

# 31. Convert string to list without split()
s = "hello"
lst = list(s)
print(lst)

# 32. Find the longest word in a sentence
sentence = "Python is a powerful programming language"
words = sentence.split()
longest = max(words, key=len)
print("Longest word:", longest)

# 33. Check if string contains only digits
s = "12345"
print(s.isdigit())

# 34. Count uppercase and lowercase letters
s = "Hello World"
upper = sum(1 for ch in s if ch.isupper())
lower = sum(1 for ch in s if ch.islower())
print("Uppercase:", upper)
print("Lowercase:", lower)

# 35. Replace spaces with hyphens
s = "Python is fun"
print(s.replace(" ", "-"))

# 36. Remove punctuation from a string
import string
s = "Hello, world!!!"
clean = "".join(ch for ch in s if ch not in string.punctuation)
print(clean)

# 37. Find the first non-repeating character
s = "aabbccdeeff"
for ch in s:
    if s.count(ch) == 1:
        print("First non-repeating:", ch)
    break

# 38. Print substring from given start and end index
s = "programming"
start, end = 3, 8
print(s[start:end])

# 39. Convert string to ASCII values
s = "ABC"
ascii_values = [ord(ch) for ch in s]
print(ascii_values)
