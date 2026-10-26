def pattern_1(num):
    for i in range(1, num + 1):
        for j in range(1, num + 1):
           print(i, end=" ")
        print()
# num = int(input("Enter a number of Rows: "))
# pattern_1(num)

def pattern_2(num):
    for i in range(1, num + 1):
        for j in range(1, num + 1):
            if i % 2 != 0:
                print("1", end=" ")
            else:
                print("0", end=" ")
        print()
# num = int(input("Enter a number of Rows: "))
# pattern_2(num)

def pattern_3(num):
    for i in range(1, num + 1):
        for j in range(1, num + 1):
           print(j, end=" ")
        print()
# num = int(input("Enter a number of Rows: "))
# pattern_3(num)

def pattern_4(num):
    for i in range(1, num + 1):
        for j in range(1, num + 1):
            if j % 2 != 0:
                print("1", end=" ")
            else:
                print("0", end=" ")
        print()
# num = int(input("Enter a number of Rows: "))
# pattern_4(num)


def pattern_5(num):
    for i in range(1, num + 1):
        for j in range(1, num + 1):
            if i == 1 or j == 1 or i == num or j == num:
                print("*", end=" ")
            else:
                print(" ", end=" ")
        print()
# num = int(input("Enter a number of Rows: "))
# pattern_5(num)

def pattern_7(num):
    for i in range(1, num + 1):
        for j in range(1, num + 1):
            print(f"({i},{j})", end=" ")
        print()
# num = int(input("Enter a number of Rows: "))
# pattern_7(num)

def pattern_12(num):
    for i in range(1, num + 1):
        for j in range(i):
            print("*", end=" ")
        print()
# num = int(input("Enter a number of Rows: "))
# pattern_12(num)

def pattern_13(num):
    for i in range(num, 0, -1):
        for j in range(i):
            print("*", end=" ")
        print()
# num = int(input("Enter a number of Rows: "))
# pattern_13(num)

def pattern_14(num):
    for i in range(1, num + 1):
        for j in range(num - i):
            print(" ", end=" ")
        for j in range(i):
            print("*", end=" ")
        print()
# num = int(input("Enter a number of Rows: "))
# pattern_14(num)

def pattern_15(num):
    for i in range(num, 0, -1):
        for j in range(num - i):
            print(" ", end=" ")
        for j in range(i):
            print("*", end=" ")
        print()
# num = int(input("Enter a number of Rows: "))
# pattern_15(num)

def pattern_16(num):
    for i in range(1, num + 1):
        for j in range(i):
            print(i, end=" ")
        print()
# num = int(input("Enter a number of Rows: "))
# pattern_16(num)

def pattern_17(num):
    for i in range(1, num + 1):
        for j in range(i):
            if i % 2 != 0:
                print("1", end=" ")
            else:
                print("0", end=" ")
        print()
# num = int(input("Enter a number of Rows: "))
# pattern_17(num)

def pattern_18(num):
    for i in range(1, num + 1):
        for j in range(1, i + 1):
            print(j, end=" ")
        print()
# num = int(input("Enter a number of Rows: "))
# pattern_18(num)

def pattern_19(num):
    for i in range(1, num + 1):
        for j in range(1, i + 1):
            if j % 2 != 0:
                print("1", end=" ")
            else:
                print("0", end=" ")
        print()
# num = int(input("Enter a number of Rows: "))
# pattern_19(num)

def pattern_20(num):
    for i in range(num, 0, -1):
        for j in range(num - i + 1):
            print(i, end=" ")
        print()
# num = int(input("Enter a number of Rows: "))
# pattern_20(num)

def pattern_21(num):
    for i in range(1, num + 1):
        for j in range(i, 0, -1):
            print(j, end=" ")
        print()
# num = int(input("Enter a number of Rows: "))
# pattern_21(num)

def pattern_22(num):
    count = 1
    for i in range(1, num + 1):
        for j in range(1, i + 1):
            print(count, end=" ")
            count += 1
        print()
# num = int(input("Enter a number of Rows: "))
# pattern_22(num)

def pattern_23(num):
    count = num * (num + 1) // 2  
    for i in range(1, num + 1):  
        for j in range(1, i + 1): 
            print(count, end=" ") 
            count -= 1
            print(" ", end=" ")             
        print()                    
# num = int(input("Enter a number of Rows: "))
# pattern_23(num)


def pattern_24(num):
    count = 1  
    for i in range(1, num + 1):  
        count += i - 1  
        for j in range(i, 0, -1):  
            print(count, end="   ")
            count -= 1  
        count += i + 1  
        print()
# num = int(input("Enter a number of Rows: "))
# pattern_24(num)

def pattern_26(num): 
    count = 0
    for i in range(1, num + 1):  
        for j in range(i):
            print(chr(65 + count), end=" ")
            count += 1
        print()
# num = int(input("Enter a number of Rows: "))
# pattern_26(num)

def pattern_28(num):
    for i in range(1, num + 1):  
        for j in range(i):
            print(chr(64 + i), end=" ")
        print()
# num = int(input("Enter a number of Rows: "))
# pattern_28(num)

def pattern_29(num):
    for i in range(1, num + 1):  
        for j in range(i):
            print(chr(65 + j), end=" ")
        print()
# num = int(input("Enter a number of Rows: "))
# pattern_29(num)

def pattern_30(num):
    for i in range(num, 0, -1):
        for j in range(num - i + 1):
            print(chr(64 + i), end="  ")
        print()
# num = int(input("Enter a number of Rows: "))
# pattern_30(num)

def pattern_31(num):
    for i in range(1, num + 1):
        for j in range(i, 0, -1):
            print(chr(64 + j), end="  ")
        print()
# num = int(input("Enter a number of Rows: "))
# pattern_31(num)

def pattern_32(num):
    for i in range(1, num + 1):
        for j in range(num - i):
            print(" ", end=" ")
        for j in range(1, i + 1):
            print(i, end=" ")
        print()
# num = int(input("Enter a number of Rows: "))
# pattern_32(num)

def pattern_33(num):
    for i in range(1, num + 1):
        for j in range(num - i):
            print(" ", end=" ")
        for j in range(1, i + 1):
            if i % 2 != 0:
                print("1", end=" ")
            else:
                print("0", end=" ")
        print()
# num = int(input("Enter a number of Rows: "))
# pattern_33(num)

def pattern_34(num):
    for i in range(1, num + 1):
        for j in range(num - i):
            print(" ", end=" ")
        for j in range(1, i + 1):
                print(j, end=" ")
        print()
# num = int(input("Enter a number of Rows: "))
# pattern_34(num)

def pattern_35(num):
    for i in range(1, num + 1):
        for j in range(num - i):
            print(" ", end=" ")
        for j in range(1, i + 1):
            if j % 2 != 0:
                print("1", end=" ")
            else:
                print("0", end=" ")
        print()
# num = int(input("Enter a number of Rows: "))
# pattern_35(num)

def pattern_67(num):
    for i in range(1, num + 1):
        for j in range(num - i):
            print(" ", end=" ")
        for j in range(2 * i - 1):
            print("*", end=" ")
        print()
# num = int(input("Enter a number of Rows: "))
# pattern_67(num)

def pattern_68(num):
    for i in range(1, num + 1):
        for j in range(num - i):
            print(" ", end=" ")
        for j in range(2 * i - 1):
            print(i, end=" ")
        print()
# num = int(input("Enter a number of Rows: "))
# pattern_68(num)

def pattern_69(num):
    for i in range(1, num + 1):
        for j in range(num - i):
            print(" ", end=" ")
        for j in range(2 * i - 1):
            if i % 2 != 0:
                print("1", end=" ")
            else:
                print("0", end=" ")
        print()
# num = int(input("Enter a number of Rows: "))
# pattern_69(num)

def pattern_70(num):
    for i in range(num, 0, -1):
        for j in range(i - 1):
            print(" ", end=" ")
        for j in range(2 * (num - i) + 1):
            print(i, end=" ")
        print()
# num = int(input("Enter a number of Rows: "))
# pattern_70(num)