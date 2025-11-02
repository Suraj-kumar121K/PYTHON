--> What is File I/O in Python?
    File Input/Output (I/O) is how your Python program reads data from a file (input) and writes data to a file (output).
    🔥Python provides built-in functions and methods to handle files.

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
--> Reading from a File
file = open("example.txt", "r")  # open in read mode
content = file.read()           # read whole file
print(content)
file.close()                    # always close the file

-->✔️Other reading methods:
file.readline() → reads one line at a time
file.readlines() → returns a list of lines

--> Writing to a File
file = open("example.txt", "w")  # open in write mode
file.write("Hello, Python!\n")
file.write("File I/O is easy.")
file.close()

--> Using with Statement (Recommended)
    with automatically closes the file after operations:
with open("example.txt", "r") as file:
    content = file.read()
    print(content)
    
with open("example.txt", "a") as file:
    file.write("\nThis is appended text.")

--> Full Read and Write Program
# Write data
with open("data.txt", "w") as f:
    f.write("Python File I/O\n")
    f.write("This is a sample file.")
# Read data
with open("data.txt", "r") as f:
    content = f.read()
    print("File Content:\n", content)
