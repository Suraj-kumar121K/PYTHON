# Level 1 – Very Basic (1–15)
# 1. Create an empty dictionary in two different ways and print both.
d1 = {}
d2 = dict()
# print(d1)
# print(d2)

# 2. Create a dictionary with 3 key-value pairs (name, age, city) and print it.
person = {
    "name": "Suraj",
    "age": 25,
    "city": "Delhi"
}
# print(person)

# 3. What symbols are used to define a dictionary? {} or () or [] ?

# 4. Create a dictionary using the dict() constructor from a list of tuples: [("a", 1), ("b", 2)]
d = dict([("a", 1), ("b", 2)])
# print(d)

# 5. Create a dictionary with integer keys and string values.
person = {1: "one", 2: "two", 3: "three"}
# print(person)

# 6. Print the type of this: d = {} vs d = dict()
d = {}
d1 = ()
# print(type(d))
# print(type(d1))

# 7. Can dictionary keys be duplicated? Create one with duplicate keys and explain what happens.


# 8. Can dictionary values be duplicated? Show an example.


# 9. Use len() to find how many key-value pairs are in {"x":10, "y":20, "z":30, "x":99}
data = {"x":10,
       "Y":20,
       "Z":30,
       "x":99 
        }
# print(len(data))
# print(data)

# 10. Access the value of key "name" in person = {"name": "Suraj", "age": 25}
person = {"name": "Suraj", "age": 25}
# print(person["name"])

# 11. Try to access a non-existing key like "country" — what error do you get?
person = {"name": "Suraj", "age": 25}
# print(person["country"])

# 12. Add a new key "profession": "Student" to an existing dictionary and print it.
person = {"name": "Suraj", "age": 25}
person["profession"] = "Student"
# print(person)

# 13. Change the value of "age" to 26 in the person dictionary.
person =  {"name":"A", "city":"Delhi", "age":30}
person["age"] = 23
# print(person)

# 14. Remove the key "city" from {"name":"A", "city":"Delhi", "age":30} using del
person =  {"name":"A", "city":"Delhi", "age":30}
# ad = person.pop("city")
# print(ad)
# print(person)

# 15 Remove and return a value using pop() — what happens if the key doesn't exist?
person = {
    "name": "Suraj",
    "age": 25
}
value = person.pop("age")
# print(value)
# print(person)

# Level 2 – Access, Update & Methods (16–28)
# Use .get() to safely access "salary" (return 0 if missing) in {"name":"Ram", "age":28}
data = {"name":"Ram", "age":28}
salary = data.get("Salary",0)
# print(salary)

# Use .get() with a default value "Unknown" for missing key "email"
data = {"name":"Ram", "age":28}
email = data.get("email","Unknon")
# print(email)

# Check if "age" exists in a dictionary using in operator.
data = {"name":"Ram", "age":28}
# print("age" in data)

# Get all keys as a list using .keys()
data = {"name":"Ram", "age":28}
# print(data.keys())

# Get all values as a list using .values()
data = {"name":"Ram", "age":28}
# print(data.values())

# Get all key-value pairs as tuples using .items()
data = {"name":"Ram", "age":28}
# print(list(data.items()))

# Loop through a dictionary and print only keys.
"""data = {"name":"Suraj", "age":23}
for key in data:
    print(key)"""

# Loop through a dictionary and print only values.
"""data = {"name":"Suraj", "age":23}
for values in data.values():
    print(values)"""

# Loop through .items() and print "Key: x → Value: y"
"""data = {"name":"Suraj", "age":23}
for key in data.items():
    print("key:", key, "→ Value:", value)"""
    
# Merge two dictionaries using  operator.
d1 = {"a":1}
d2 = {"b":2}
d3 = d1 | d2
# print(d3)

# Merge two dictionaries using .update() method.
d1 = {"a":1}
d2 = {"b":2}
d1.update(d2)
# print(d1)

# Clear all items from a dictionary using .clear()
data = {"name":"Ram", "age":28}
data.clear()
# print(data)

# Create a shallow copy of a dictionary using .copy()
data = {"name":"Ram", "age":28}
new_data = data.copy()
# print(new_data)

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