--> What is File I/O in Python?
    File I/O in Python refers to the ability to read data from files and write data to files.
             Input (Reading) → Getting data from a file.
             Output (Writing) → Saving data to a file.

--> Types of Files
    1.Text Files (.txt, .csv, .py, etc.)
        - Human-readable
        - Can store strings and numbers in text format
    2.Binary Files (.jpg, .png, .pdf, .exe)
        - Not human-readable
        - Used for images, videos, executable files

--> Opening a File
file = open("example.txt", "mode")

--> Modes in Python:
'''
| Mode  |                         Meaning                                 |
| ----- | --------------------------------------------------------------- |
| `'r'` | Read (default) – file must exist                                |
| `'w'` | Write – creates file if it doesn’t exist, overwrites if it does |
| `'a'` | Append – adds data to the end of file                           |
| `'x'` | Create – creates file, errors if file exists                    |
| `'b'` | Binary mode – e.g., `'rb'` or `'wb'`                            |
| `'+'` | Read and write – e.g., `'r+'`                                   |
|_______|_________________________________________________________________|
'''
--> Reading a File in Python
file = open("example.txt", "r")
content = file.read()
print(content)
file.close()
                
--> Other Methods to Read a File
     1.Read line by line
       file = open("example.txt", "r")
       line = file.readline()
       print(line)
       file.close()

     2. Read all lines as a list
        file = open("example.txt", "r")
        lines = file.readlines()
        print(lines)  # prints a list of lines
        file.close()

     3. Loop through file line by line
        file = open("example.txt", "r")
        for line in file:
        print(line.strip())
        file.close()

--> Write Files in Python
    Write to a file
      file = open("example.txt", "w")
      file.write("Hello, Python!\n")
      file.write("File I/O is easy.")
      file.close()

--> Append to a file
    file = open("example.txt", "a")
    file.write("\nThis text is appended.")
    file.close()
Note: 'w' overwrites, 'a' appends

--> With Statement in Python
    Using with automatically closes the file after the block ends.
    Preferred way to work with files.

--> Reading
    with open("example.txt", "r") as file:
    content = file.read()
    print(content)

--> Writing
    with open("example.txt", "w") as file:
    file.write("This is written using with statement.")

--> Appending
    with open("example.txt", "a") as file:
    file.write("\nAppended text using with statement.")

    
--> Using with Statement (Recommended)
    with automatically closes the file after operations:
    with open("example.txt", "r") as file:
    content = file.read()
    print(content)

--> Summary Table
| Operation      |          Code Example              |
| -------------- | ---------------------------------- |
| Open file      | `file = open("file.txt", "r")`     |
| Read all       | `content = file.read()`            |
| Read line      | `line = file.readline()`           |
| Read all lines | `lines = file.readlines()`         |
| Write file     | `file.write("text")`               |
| Append file    | `file.write("append")`             |
| Close file     | `file.close()`                     |
| With statement | `with open("file.txt", "r") as f:` |
