st = int(input("Enter a Number: "))
count = 0
while st > 0:
    # digit = st % 10
    count += 1
    dt = st // 10
print(count)