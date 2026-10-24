def Hollow_square(num):
    for i in range(1, num + 1):
        for j in range(1, num + 1):
            if i == 1 or i == 2 or i == num - 1 or i == num:
                print("*", end=" ")
            elif j == 1 or j == 2 or j == num - 1 or j == num:
                print("*", end=" ")
            else:
                print(" ", end=" ")
        print()

num = int(input("Enter a number of Rows: "))
Hollow_square(num)