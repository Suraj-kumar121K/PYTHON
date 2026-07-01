Tasks =  [] # Ye list sab tasks store karegi.
print("Welcome Message")

def add_task():
    task = input("Enter task: ") # User se task leta hai.
    Tasks.append(task) # List me task add karta hai.
    print("Task Added")

def view_task():
    print("View")
    
def remove_task():
    print("remove view")

while True:
    print("\n1. Add Task")
    print("1. view Task")
    print("3. Remove Task")
    print("4.. Exit Task")
    
    choice = input("Enter a choice: ")
    if choice == "1":
        add_task()
 
    elif choice == "2":
        view_task()
        
    elif choice == "3":
        remove_task()
        
    if choice == "4":
        print("Program Close")
        break
    else:
        print("Invalid Choice")