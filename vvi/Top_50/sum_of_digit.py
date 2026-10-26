# Write a Python program to calculate the sum of all natural numbers from 1 to n.
def Sum_Of_Numbers(num):
    sum = 0
    for i in range(1, num + 1):
        sum += i
    print(sum)
# num = int(input("Enter a Sum of number: "))
# Sum_Of_Numbers(num)


def Sum_Of_Digit(num):
    total = 0
    while num > 0:
        digit = num % 10 # last digit nikalna
        total = total + digit # add total
        num = num // 10 # Number ka last digit hataana
    print(total)
num = int(input("Enter a Sum of number: "))
Sum_Of_Digit(num)