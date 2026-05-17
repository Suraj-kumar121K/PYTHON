todos = []
add_new = True
while add_new():
    new_todo = input("Todo: ")
    todos.append(new_todo)
    count = input("Continue? (Y/N)")
    
    if count.lower() == "n":
        add_new = False
        
print(todos)