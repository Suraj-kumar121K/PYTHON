# 1. Hello World
def hello():
    print("Hello World")
# hello()

# 2. Remove duplicates from list
def remo_dupli(List):
    rest = []
    for i in List:
        if i not in rest:
            rest.append(i)
    return rest
# print(remo_dupli([1, 2, 3, 2, 3, 2, 5, 6]))


sentence = "Coding on CodeChef"

words = sentence.split()

for word in words:
    print(f"{word} - {len(word)}")

print(f"{sentence} - {len(sentence)}")