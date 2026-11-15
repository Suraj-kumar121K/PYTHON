# Find the Student with the Highest Marks
def find_topper(students):
    highest_marks = 0
    topper = ""
    for name, marks in students.items():
        if marks > highest_marks:
            highest_marks = marks
            topper = name
    print("Student Name:", topper)
    print("Highest Marks:", highest_marks)
students = {
    "Rahul": 85,
    "Amit": 92,
    "Priya": 78,
    "Rohit": 96,
    "Neha": 89
}
# find_topper(students)

# 2. Find the Frequency of Each Character
def count_frequency(text):
    frequency = {}
    for char in text:
        if char in  frequency:
            frequency[char] += 1
        else:
            frequency[char] = 1
    return frequency
# text = "programming"
# result = count_frequency(text)
# print(result)

# 3. Sort Dictionary by Values (Descending Order)
def sort_products(products):
    
    