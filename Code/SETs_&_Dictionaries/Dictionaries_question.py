# Level 1 – Very Basic (1–15)

# Create an empty dictionary in two different ways and print both.
# Create a dictionary with 3 key-value pairs (name, age, city) and print it.
# What symbols are used to define a dictionary? {} or () or [] ?
# Create a dictionary using the dict() constructor from a list of tuples: [("a", 1), ("b", 2)]
# Create a dictionary with integer keys and string values.
# Print the type of this: d = {} vs d = dict()
# Can dictionary keys be duplicated? Create one with duplicate keys and explain what happens.
# Can dictionary values be duplicated? Show an example.
# Use len() to find how many key-value pairs are in {"x":10, "y":20, "z":30, "x":99}
# Access the value of key "name" in person = {"name": "Suraj", "age": 25}
# Try to access a non-existing key like "country" — what error do you get?
# Add a new key "profession": "Student" to an existing dictionary and print it.
# Change the value of "age" to 26 in the person dictionary.
# Remove the key "city" from {"name":"A", "city":"Delhi", "age":30} using del
# Remove and return a value using pop() — what happens if the key doesn't exist?

# Level 2 – Access, Update & Methods (16–28)

# Use .get() to safely access "salary" (return 0 if missing) in {"name":"Ram", "age":28}
# Use .get() with a default value "Unknown" for missing key "email"
# Check if "age" exists in a dictionary using in operator.
# Get all keys as a list using .keys()
# Get all values as a list using .values()
# Get all key-value pairs as tuples using .items()
# Loop through a dictionary and print only keys.
# Loop through a dictionary and print only values.
# Loop through .items() and print "Key: x → Value: y"
# Merge two dictionaries using  operator (Python 3.9+)
# Merge two dictionaries using .update() method.
# Clear all items from a dictionary using .clear()
# Create a shallow copy of a dictionary using .copy()

# Level 3 – Iteration, Sorting & Built-ins (29–40)

# Sort a dictionary by keys (ascending) and print as sorted list of tuples.
# Sort a dictionary by values (descending) — return a new dictionary.
# Use sorted() with items() to sort by value.
# Find the sum of all values in {"a":10, "b":20, "c":30}
# Find the maximum and minimum value in a dictionary of numbers.
# Count frequency of words in this sentence using a dictionary: "hello world hello python world"
# Invert a dictionary (swap keys and values) — assume values are unique.
# Create a dictionary from two lists using zip(): keys = ["name","age"], values = ["Suraj",25]
# Create a dictionary using dictionary comprehension: keys 1–10, values = square of key
# Create a dictionary comprehension that filters even keys only.
# Remove all keys that start with "a" from a dictionary.
# Create a dictionary where keys are characters of a string and values are their counts.

# Level 4 – Nested Dictionaries & Advanced / Tricky (41–50)

# Create a nested dictionary for a student: {"name":"A", "marks":{"math":85, "sci":90}}
# Access "math" marks from the nested student dictionary.
# Add a new subject "eng":88 to the nested marks dictionary.
# Loop through a nested dictionary and print all student names and their average marks.
# Handle missing keys in nested dictionary safely using .get()
# What happens when you do d = {} then d[1] = [2,3] then d[1].append(4) — explain mutability.
# Can lists be dictionary keys? Try and explain the error.
# Use setdefault() to add a key only if it doesn't exist (with default value []).
# Given list of students and their marks in two separate lists — create dict using zip.
# Write a function that takes any number of keyword arguments (**kwargs) and returns them as a dictionary.