# file = open("debug.txt", "r")
# data = file.read()
# print(data)
# file.close()


with open("debug.txt", "r") as file:
    data = file.read()
    print(data)