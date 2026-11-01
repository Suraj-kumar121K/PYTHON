def Pattern_11(num):
    for i in range(1, num + 1):
        for j in range(1, num + 1):

            if (i == 1 and j != 2 or
                i == 2 and (j == 1 or j == 3) or
                i == 3 or
                i == 4 and (j == 3 or j == 5) or
                i == 5 and (j == 1 or j == 2 or j == 3 or j == 5)):
                print("*", end=" ")
            else:
                print(" ", end=" ")
        print()
num = int(input("Enter number of rows: "))
Pattern_11(num)