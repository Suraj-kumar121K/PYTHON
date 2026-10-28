def Armstrong_Number(nums):
    original = nums
    total = 0
    power = len(str(nums))
    while nums > 0:
        digit = nums % 10
        total = total + digit ** power
        nums = nums // 10
    if total == original:
        print(original, "is an Armstrong Number")
    else:
        print(original, "is not an Armstrong Number")
        
if __name__ == "__main__":
    try:
        nums = int(input("Enter digit: "))
        Armstrong_Number(nums)
    except Exception as e:
            print("Error:", e)