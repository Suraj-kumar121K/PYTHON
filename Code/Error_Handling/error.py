# 1. ZeroDivisionError
"""try:
    a = 10
    b = 0
except ZeroDivisionError:
    print("Cannot divide by zero")"""
    
# 2. ValueError (int conversion)
"""try:
    num = int(input("Enter number: "))
except ValueError:
    print("Invalid input")"""
    
# 3. IndexError
"""try:
    a = [1, 2, 3]
    print(a[10])
except IndexError:
    print("Index not found")"""
    
# 4. KeyError
"""try:
    d = {"name": "Suraj"}
    print(d["age"])
except KeyError:
    print("Key not found")"""
    
# 5. Safe int conversion
"""try:
    num = int(input("Enter number: "))
except ValueError:
    print("Please enter valid integer")"""
    
# 1. Divide two numbers
"""try:
    a = int(input("Enter a: "))
    b = int(input("Enter b: "))
    print(a / b)
except ZeroDivisionError:
    print("Cannot divide by zero")"""
  
# Calculator  
"""
try:
    a = int(input())
    b = int(input())
    op = input()

    if op == "+":
        print(a + b)
    elif op == "-":
        print(a - b)
    elif op == "*":
        print(a * b)
    elif op == "/":
        print(a / b)
    else:
        print("Invalid operator")
except ZeroDivisionError:
    print("Cannot divide by zero")
except ValueError:
    print("Invalid input")"""
    
    
import os
FILE_NAME = "students.txt"
# ➤ Add Student
def add_student():
    try:
        roll = input("Enter Roll No: ")
        name = input("Enter Name: ")
        marks = float(input("Enter Marks: "))

        with open(FILE_NAME, "a") as f:
            f.write(f"{roll},{name},{marks}\n")

        print("Student added successfully!")

    except ValueError:
        print("Invalid input! Marks must be a number.")

    except Exception as e:
        print("Error:", e)


# ➤ View Students
def view_students():
    try:
        if not os.path.exists(FILE_NAME):
            print("No file found!")
            return

        with open(FILE_NAME, "r") as f:
            data = f.readlines()

            if len(data) == 0:
                print("No student records found.")
                return

            print("\n--- Student List ---")
            for line in data:
                roll, name, marks = line.strip().split(",")
                print(f"Roll: {roll}, Name: {name}, Marks: {marks}")

    except Exception as e:
        print("Error:", e)


# ➤ Search Student
def search_student():
    try:
        roll_search = input("Enter Roll No to search: ")

        with open(FILE_NAME, "r") as f:
            found = False

            for line in f:
                roll, name, marks = line.strip().split(",")

                if roll == roll_search:
                    print(f"Found → Roll: {roll}, Name: {name}, Marks: {marks}")
                    found = True
                    break

            if not found:
                print("Student not found!")

    except FileNotFoundError:
        print("File not found!")

    except Exception as e:
        print("Error:", e)


# ➤ Delete Student
def delete_student():
    try:
        roll_delete = input("Enter Roll No to delete: ")

        with open(FILE_NAME, "r") as f:
            lines = f.readlines()

        with open(FILE_NAME, "w") as f:
            found = False

            for line in lines:
                roll, name, marks = line.strip().split(",")

                if roll != roll_delete:
                    f.write(line)
                else:
                    found = True

        if found:
            print("Student deleted successfully!")
        else:
            print("Student not found!")

    except FileNotFoundError:
        print("File not found!")

    except Exception as e:
        print("Error:", e)


# ➤ Main Menu
while True:
    print("\n===== STUDENT MANAGEMENT =====")
    print("1. Add Student")
    print("2. View Students")
    print("3. Search Student")
    print("4. Delete Student")
    print("5. Exit")

    try:
        choice = int(input("Enter choice: "))

        if choice == 1:
            add_student()
        elif choice == 2:
            view_students()
        elif choice == 3:
            search_student()
        elif choice == 4:
            delete_student()
        elif choice == 5:
            print("Exiting...")
            break
        else:
            print("Invalid choice!")

    except ValueError:
        print("Please enter a number between 1-5")