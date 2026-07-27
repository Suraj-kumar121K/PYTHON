with open("story.txt", "r") as s:
    data = s.read()
    data = data.capitalize()
    print("File Open:", data)