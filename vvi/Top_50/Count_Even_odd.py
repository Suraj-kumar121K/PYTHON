def Count_Even_Odd(nums):
    Even = 0
    Odd = 0
    while nums > 0:
        digit = nums % 10
        if digit % 2 == 0:
            Even += 1
        else:
            Odd += 1
        nums = nums // 10
    print("Even Digits Count:", Even)
    print("Odd Digits Count:", Odd)
    
if __name__ == "__main__":
    try:
        nums = int(input("Enter a Number: "))
        Count_Even_Odd(nums)
    except ValueError as e:
        print("Error", e)