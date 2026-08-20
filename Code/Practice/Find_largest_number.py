# largest number
num = [10, 25, 8, 40, 15, 30]
largest = num[0]
for i in num:
    if i > largest:
        largest = i
print(largest)