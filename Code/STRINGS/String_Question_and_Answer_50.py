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
