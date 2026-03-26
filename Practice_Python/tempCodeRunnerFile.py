user = int(input("Enter a number "))
if  -9 <= user <= 9:
    print("single digit number")
elif -99 <= user <= 99:
    print("double digit number")
else:
    print("More than two digits")