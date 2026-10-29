def Largest_Number(nums):
    largest = nums[0]
    for i in range(len(nums)):
        if nums[i] > largest:
            largest = nums[i]
    print("Largest number:", largest)

if __name__ == "__main__":
    try:
        nums = list(map(int, input("Enter a Largest Number: ").split()))
        Largest_Number(nums)
        
    except ValueError as e:
        print("Error: Please enter valid integers.", e)