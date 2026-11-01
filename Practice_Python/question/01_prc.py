def Count_Marks(students):
    result = {}

    for name, marks in students.items():
        if marks in result:
            result[marks] += 1
        else:
            result[marks] = 1

    print(result)


students = {
    "Amit": 85,
    "Rahul": 70,
    "Priya": 92,
    "Rohit": 70,
    "Neha": 92
}

Count_Marks(students)