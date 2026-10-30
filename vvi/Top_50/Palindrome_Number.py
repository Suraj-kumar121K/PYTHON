def Palindrome_Number(nums):
    total = 0
    original = nums
    while nums > 0:
        digit = nums % 10
        total = total * 10 + digit
        nums = nums // 10
        
    if original == total:
        print("Palindrome Number")
    else:
        print("Not a Palindrome Number")
        
if __name__ == "__main__":
    try:       
        nums = int(input("Enter a Number: "))
        Palindrome_Number(nums)
    except ValueError as e:
        print("Error:", e)