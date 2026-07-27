# folder ko dekh sakte hai open kar ke
file = open("story.txt", "r")
# read kar raha hai file ko
data = file.read()
# convert the upper cher 
data = data.upper()
# check kar raha hai word ke ander present hai ya nahi
if "RIYA" in data:
    print("Yes Riya word is present in the file")
else:
    print("NO")
# print kar raha hai jo file ke ander hai
print("Data of the file is: ", data)